"""A hundred-year hazard timeline, built on rates rather than cumulative probabilities.

The 2026-2036 register asks analysts for P(at least once by date T). That works
over a decade and fails over a century: anything with a steady hazard saturates
toward certainty, and a companion audit measured the register's *discriminating
variance actually falling* as the window lengthened — 41.9 at 2036, 35.7 at 2056.
A longer window carried less information about which future we are in.

Rates do not have that failure mode. "Once per 340 years on average" means the
same thing over a century as over a decade, and P(at least once) is derived from
it rather than elicited. So this module takes recurrence intervals as primary.

Three things it does that a naive rate table would not:

  RATE UNCERTAINTY. Every interval is a central estimate inside a wide range —
  a megathrust interval is known to within a factor of two, "nuclear war" to
  within maybe an order of magnitude. Intervals are sampled lognormally from the
  elicited range, so the reported probability carries that uncertainty instead
  of pretending the central estimate is the truth.

  NON-STATIONARITY. Asteroid flux is flat over a century. Lethal wet-bulb
  frequency is not. Each hazard carries a trend that ramps its rate across the
  window, because assuming stationarity for a hundred years is the main way a
  table like this goes wrong.

  NESTING. "Any nuclear detonation in anger", "regional nuclear war" and "full
  strategic exchange" are not three independent hazards — the second and third
  are subsets of the first. Summing their rates triple-counts. Aggregates
  therefore run over a maximal antichain, and the excluded members keep their own
  individual numbers.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

START_YEAR = 2026
HORIZON_YEARS = 100

# How much a hazard's rate is multiplied by at the end of the century.
TREND_MULTIPLIER = {
    "rising_strongly": 3.0,
    "rising": 1.8,
    "flat": 1.0,
    "falling": 0.6,
    "falling_strongly": 0.35,
    "unknown": 1.0,
}
# An unknown trend is not a flat trend — it is a flat trend plus extra ignorance,
# so it widens the sampled rate range rather than only setting a multiplier.
UNKNOWN_TREND_EXTRA_SIGMA = 0.35

Z90 = 1.6448536269514722


@dataclass(frozen=True)
class Hazard:
    id: str
    category: str
    name: str
    criteria: str
    recurrence: float          # central estimate, years between occurrences
    recurrence_low: float      # more frequent end of the ~90% range
    recurrence_high: float     # rarer end
    trend: str
    severity: float            # 0-10, saturates
    deaths_log10: float        # log10 expected deaths per occurrence; does not saturate
    warning_time: str
    anthropogenic: str
    reversibility: str
    evidence: str
    confidence: str
    family: str = ""
    note: str = ""

    @property
    def rate(self) -> float:
        """Occurrences per year at present conditions."""
        return 1.0 / max(self.recurrence, 1e-9)

    @property
    def counted(self) -> bool:
        """Does this rest on a real counted record, or is it judgement with a number?

        The distinction matters more than any individual figure. A reader who
        cannot tell them apart will treat "nuclear war once per 150 years" as
        having the standing of "M9 megathrust once per 350 years", and it does not.
        """
        e = self.evidence.lower()
        judged = any(
            k in e for k in
            ("judgement", "judgment", "elicit", "no historical", "never occurred",
             "speculative", "extrapolat", "no base rate", "unprecedented")
        )
        return self.confidence in ("high", "medium") and not judged

    def sigma(self) -> float:
        """Lognormal spread implied by the elicited 90% range."""
        lo = max(min(self.recurrence_low, self.recurrence_high), 1e-9)
        hi = max(self.recurrence_low, self.recurrence_high, 1e-9)
        s = (np.log(hi) - np.log(lo)) / (2 * Z90) if hi > lo else 0.25
        if self.trend == "unknown":
            s = float(np.hypot(s, UNKNOWN_TREND_EXTRA_SIGMA))
        return max(s, 0.05)

    def cumulative_hazard(self, years: float, recurrence: float | None = None) -> float:
        """Integrated rate over [0, years], with the trend ramp applied.

        The rate ramps linearly from 1x today to TREND_MULTIPLIER at the century's
        end, so the integral is closed-form rather than needing quadrature.
        """
        r = recurrence if recurrence is not None else self.recurrence
        m = TREND_MULTIPLIER.get(self.trend, 1.0)
        base = 1.0 / max(r, 1e-9)
        return base * (years + (m - 1.0) * years * years / (2.0 * HORIZON_YEARS))


def parse(items: list[dict], family: str = "") -> list[Hazard]:
    out: list[Hazard] = []
    for it in items:
        try:
            out.append(
                Hazard(
                    id=str(it["id"]),
                    category=str(it.get("category", "other")),
                    name=str(it.get("name", "")),
                    criteria=str(it.get("resolution_criteria", "")),
                    recurrence=float(it["recurrence_years"]),
                    recurrence_low=float(it.get("recurrence_low") or it["recurrence_years"]),
                    recurrence_high=float(it.get("recurrence_high") or it["recurrence_years"]),
                    trend=str(it.get("rate_trend", "flat")),
                    severity=float(it.get("severity_0_10") or 0),
                    deaths_log10=float(it.get("expected_deaths_log10") or 0),
                    warning_time=str(it.get("warning_time", "unknown")),
                    anthropogenic=str(it.get("anthropogenic", "natural")),
                    reversibility=str(it.get("reversibility", "recoverable_decades")),
                    evidence=str(it.get("base_rate_evidence", "")),
                    confidence=str(it.get("confidence", "low")),
                    family=family,
                    note=str(it.get("note", "")),
                )
            )
        except (KeyError, TypeError, ValueError):
            continue
    return out


def probability_curve(
    h: Hazard, rng: np.random.Generator, n_draws: int = 4000
) -> dict:
    """P(at least once by each decade) with a credible band from rate uncertainty.

    The band is the honest part. A megathrust interval known to within a factor of
    two produces a narrow band; "nuclear war" spans an order of magnitude and
    produces a wide one, which is exactly the signal a reader needs.
    """
    draws = np.exp(rng.normal(np.log(max(h.recurrence, 1e-9)), h.sigma(), n_draws))
    decades = np.arange(10, HORIZON_YEARS + 1, 10, dtype=float)

    p = np.empty((n_draws, len(decades)))
    for i, yrs in enumerate(decades):
        lam = np.array([h.cumulative_hazard(yrs, r) for r in draws])
        p[:, i] = 1.0 - np.exp(-lam)

    return {
        "decades": [int(START_YEAR + d) for d in decades],
        "mean": p.mean(axis=0).tolist(),
        "lo": np.quantile(p, 0.05, axis=0).tolist(),
        "hi": np.quantile(p, 0.95, axis=0).tolist(),
        "p_century": float(p[:, -1].mean()),
        "p_century_lo": float(np.quantile(p[:, -1], 0.05)),
        "p_century_hi": float(np.quantile(p[:, -1], 0.95)),
        "expected_count_century": float(
            np.mean([h.cumulative_hazard(HORIZON_YEARS, r) for r in draws])
        ),
    }


def maximal_antichain(hazards: list[Hazard], nested: list[dict]) -> set[str]:
    """Ids to EXCLUDE from aggregates because a broader hazard already covers them.

    `nested` entries look like {"ids": [...], "keep": id}. Everything else in the
    group is a subset of `keep` and would be counted twice.
    """
    drop: set[str] = set()
    known = {h.id for h in hazards}
    for group in nested:
        ids = [i for i in group.get("ids", []) if i in known]
        keep = group.get("keep")
        if len(ids) < 2 or keep not in ids:
            continue
        drop.update(i for i in ids if i != keep)
    return drop


def aggregate(
    hazards: list[Hazard], rng: np.random.Generator, exclude: set[str] | None = None,
    n_draws: int = 3000,
) -> dict:
    """Century-scale totals over a non-overlapping hazard set.

    Deaths are summed in linear space from the log10 estimates, then reported
    back as a log — expected deaths are dominated by the rare enormous events, and
    averaging logs would hide exactly that.
    """
    exclude = exclude or set()
    live = [h for h in hazards if h.id not in exclude]

    tiers = {}
    for label, lo in (("mass_casualty_1e4", 4.0), ("catastrophe_1e6", 6.0),
                      ("global_1e7", 7.0), ("civilisational_1e8", 8.0)):
        subset = [h for h in live if h.deaths_log10 >= lo]
        # Sampled jointly so the reported P(>=1) carries rate uncertainty rather
        # than compounding central estimates.
        counts = np.zeros(n_draws)
        for h in subset:
            r = np.exp(rng.normal(np.log(max(h.recurrence, 1e-9)), h.sigma(), n_draws))
            lam = np.array([h.cumulative_hazard(HORIZON_YEARS, ri) for ri in r])
            counts += rng.poisson(lam)
        tiers[label] = {
            "threshold_deaths": float(10 ** lo),
            "n_hazards": len(subset),
            "expected_events": float(counts.mean()),
            "p_at_least_one": float((counts >= 1).mean()),
            "p_two_or_more": float((counts >= 2).mean()),
            "p_none": float((counts == 0).mean()),
        }

    exp_deaths = sum(
        h.cumulative_hazard(HORIZON_YEARS) * (10 ** h.deaths_log10) for h in live
    )
    return {
        "n_hazards_total": len(hazards),
        "n_hazards_counted": len(live),
        "n_excluded_as_nested": len(exclude),
        "tiers": tiers,
        "expected_deaths_century": exp_deaths,
        "expected_deaths_log10": float(np.log10(max(exp_deaths, 1.0))),
    }


def by_decade(hazards: list[Hazard], exclude: set[str] | None = None) -> list[dict]:
    """Expected occurrences per decade, split by category — the timeline itself."""
    exclude = exclude or set()
    live = [h for h in hazards if h.id not in exclude]
    cats = sorted({h.category for h in live})

    rows = []
    for d in range(10):
        y0, y1 = d * 10, (d + 1) * 10
        row = {"decade": f"{START_YEAR + y0}s", "start": START_YEAR + y0}
        total = 0.0
        for c in cats:
            v = sum(
                h.cumulative_hazard(y1) - h.cumulative_hazard(y0)
                for h in live if h.category == c
            )
            row[c] = v
            total += v
        row["total"] = total
        rows.append(row)
    return rows

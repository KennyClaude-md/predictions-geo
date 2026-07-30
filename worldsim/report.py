"""Turning the ensemble into something a person can read and argue with."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from .timeline import quarter_at

DOMAIN_TITLES = {
    "geopolitics": "Great-power conflict & geopolitics",
    "climate": "Climate & Earth systems",
    "economy": "Global macroeconomy & finance",
    "ai": "AI, compute & transformative technology",
    "energy": "Energy systems & critical materials",
    "demographics": "Demography & migration",
    "health": "Pandemics, biosecurity & global health",
    "politics": "Political stability & governance",
    "foodwater": "Food, water & agriculture",
    "israel": "Israel, the Levant & the Red Sea",
}


def pct(x: float) -> str:
    v = x * 100
    if v >= 99.5:
        return ">99%"
    if v < 0.5:
        return "<0.5%"
    if v < 10:
        return f"{v:.1f}%"
    return f"{v:.0f}%"


def band(lo: float, hi: float) -> str:
    return f"[{pct(lo)}–{pct(hi)}]"


class ReportBuilder:
    def __init__(self, ctx: dict):
        self.ctx = ctx
        self.lines: list[str] = []

    def w(self, s: str = "") -> None:
        self.lines.append(s)

    def build(self) -> str:
        c = self.ctx
        self._header()
        self._method()
        self._headline()
        self._aggregate()
        self._archetypes()
        self._by_domain()
        self._cascades()
        self._dependence()
        self._continuous()
        self._sensitivity()
        self._disagreement()
        self._critiques()
        self._calendar()
        self._limits()
        return "\n".join(self.lines)

    # -- sections ---------------------------------------------------------

    def _header(self) -> None:
        c = self.ctx
        self.w("# World Futures Simulation — Forecast Report")
        self.w()
        self.w(f"**Simulation date:** {c['as_of']}  ")
        self.w(f"**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  ")
        self.w(
            f"**Paths:** {c['n_paths_total']:,} across "
            f"{c['n_worldviews']} worldviews × {c['n_worlds']} parameter worlds  "
        )
        self.w(f"**Risk nodes:** {c['n_risks']} · **causal edges:** {c['n_edges']} · "
               f"**latent factors:** {c['n_latents']} · "
               f"**continuous variables:** {c['n_continuous']}")
        self.w()
        self.w("---")
        self.w()

    def _method(self) -> None:
        self.w("## How to read this")
        self.w()
        self.w(
            "Every number below is the output of a survival-process Monte Carlo, not a "
            "guess written directly. Ten domains were parameterised against current "
            "sources, audited for base-rate discipline, then red-teamed from three "
            "directions. Each of those opinions is run as a separate worldview and the "
            "results are pooled by weight."
        )
        self.w()
        self.w(
            "**The bracketed range is not the range of outcomes** — the event either "
            "happens or it doesn't. It is the range of *the probability itself* across "
            "parameter worlds: how much the answer moves depending on whose model of the "
            "world you accept. A wide bracket means the forecast is fragile. Monte Carlo "
            "noise has been subtracted out, so what remains is real disagreement."
        )
        self.w()
        errs = [
            v["final_error_pp"]
            for v in self.ctx["calibration"].values()
            if v.get("final_error_pp") is not None
        ]
        self.w(
            f"**Calibration check:** simulated marginals reproduce the elicited "
            f"cumulative probabilities to within "
            f"{max(errs) if errs else float('nan'):.2f} percentage points "
            f"(worst node, worst worldview). This matters: the dependency network is "
            f"tuned to reshape the *joint* distribution — which events co-occur — "
            f"without inflating any individual probability above what the underlying "
            f"analysis actually claimed."
        )
        self.w()

    def _headline(self) -> None:
        self.w("## Headline forecasts")
        self.w()
        self.w(
            "Ranked by expected systemic impact — probability by 2036 multiplied by "
            "severity — rather than by probability alone, because a 12% chance of "
            "something that reorders the world outranks a near-certainty that doesn't."
        )
        self.w()
        self.w("| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Impact |")
        self.w("|---|-------|--------:|--------:|--------:|:---------------:|----:|")
        for i, r in enumerate(self.ctx["headline"], 1):
            self.w(
                f"| {i} | **{r['name']}** | {pct(r['p2027'])} | {pct(r['p2031'])} | "
                f"{pct(r['p2036'])} | {band(r['lo2036'], r['hi2036'])} | {r['severity']:.0f} |"
            )
        self.w()

    def _aggregate(self) -> None:
        a = self.ctx["aggregate"]
        self.w("## The decade in aggregate")
        self.w()
        self.w(
            "Individual probabilities are the easy part. The question that actually "
            "determines how the 2030s feel is how many high-impact events land, and "
            "whether they land together."
        )
        self.w()
        self.w(
            "**Read the impact rating carefully.** Analysts were asked for *global "
            "systemic impact if it occurs*, where 10 is civilization-altering — that is "
            "a measure of magnitude, not of badness. A transformative AI capability "
            "milestone legitimately scores 9 on it. These are high-impact events, not a "
            "count of catastrophes."
        )
        self.w()
        self.w("| Impact tier | Nodes | Expected count | Median | P(none) | P(≥2) | P(≥3) |")
        self.w("|---|---:|---:|---:|---:|---:|---:|")
        for thr in (6, 7, 8, 9):
            t = a["tiers"][f"ge{thr}"]
            self.w(
                f"| **{thr}+ / 10** | {t['n_nodes']} | {t['expected']:.1f} | "
                f"{t['deciles'][2]:.0f} | {pct(t['p_zero'])} | {pct(t['p_ge_2'])} | "
                f"{pct(t['p_ge_3'])} |"
            )
        self.w()
        self.w(self.ctx["aggregate_commentary"])
        self.w()
        if self.ctx.get("severity_note"):
            self.w(self.ctx["severity_note"])
            self.w()

    def _archetypes(self) -> None:
        self.w("## Scenario archetypes")
        self.w()
        self.w(
            "Paths were clustered on which major events fired and on the shape of the "
            "systemic-stress trajectory. These are not scenarios written in advance and "
            "then assigned probabilities — they are the shapes the simulation actually "
            "produced, priced by how much of the path mass fell into each."
        )
        self.w()
        for a in self.ctx["archetypes"]:
            self.w(f"### {a['label']} — **{pct(a['probability'])}**")
            self.w()
            self.w(a["description"])
            self.w()
            if a["signature"]:
                self.w("Distinguishing features (rate within this cluster vs. overall):")
                self.w()
                for s in a["signature"]:
                    self.w(f"- {s}")
                self.w()

    def _by_domain(self) -> None:
        self.w("## Full results by domain")
        self.w()
        for dom, rows in self.ctx["by_domain"].items():
            self.w(f"### {DOMAIN_TITLES.get(dom, dom)}")
            self.w()
            self.w("| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |")
            self.w("|---|---:|---:|---:|:---:|---:|---|")
            for r in rows:
                timing = (
                    quarter_at(int(round(r["median_quarter"]))).label
                    if r["median_quarter"] is not None
                    else "—"
                )
                self.w(
                    f"| {r['name']} | {pct(r['p2027'])} | {pct(r['p2031'])} | "
                    f"{pct(r['p2036'])} | {band(r['lo2036'], r['hi2036'])} | "
                    f"{r['severity']:.0f} | {timing} |"
                )
            self.w()
            self.w("<details><summary>Resolution criteria</summary>")
            self.w()
            for r in rows:
                self.w(f"- **{r['name']}** — {r['resolution']}")
            self.w()
            self.w("</details>")
            self.w()

    def _cascades(self) -> None:
        self.w("## How bad decades begin")
        self.w()
        self.w(
            "Among paths where at least three high-severity events fired, these are the "
            "most common opening sequences, in order of occurrence."
        )
        self.w()
        self.w("| Frequency | First | Then | Then |")
        self.w("|---:|---|---|---|")
        for ch in self.ctx["chains"]:
            self.w(
                f"| {pct(ch['share'])} | {ch['names'][0]} | {ch['names'][1]} | "
                f"{ch['names'][2]} |"
            )
        self.w()
        self.w(self.ctx["chain_commentary"])
        self.w()

    def _dependence(self) -> None:
        self.w("## Where the correlations are")
        self.w()
        self.w(
            "The clearest way to read a dependency is the contrast between P(A given B) "
            "and P(A given not-B) — how much learning one event would move your estimate "
            "of the other. Ranked by odds ratio rather than by lift, because lift is "
            "mechanically capped by the base rates: two events at 80% each cannot show a "
            "lift above 1.25 however tightly coupled they are, so ranking high-probability "
            "nodes by lift returns a table of 1.0× entries and hides every real dependency. "
            "This is the part of the model a spreadsheet of independent probabilities "
            "cannot produce, and it is where tail risk lives."
        )
        self.w()
        self.w("| Event A | Event B | P(A given B) | P(A given not-B) | Odds ratio |")
        self.w("|---|---|---:|---:|---:|")
        for p in self.ctx["pairs"]:
            self.w(
                f"| {p['a']} | {p['b']} | **{pct(p['cond'])}** | {pct(p['cond_not'])} | "
                f"{p['odds_ratio']:.1f}× |"
            )
        self.w()

    def _continuous(self) -> None:
        self.w("## Continuous indicators")
        self.w()
        self.w(
            "These evolve on a Gaussian copula driven by each path's own systemic-stress "
            "index, so the bad tails of these distributions are populated by the same "
            "paths that fired the bad events — not by independent noise."
        )
        self.w()
        self.w("| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |")
        self.w("|---|---:|:---:|:---:|")
        for v in self.ctx["continuous"]:
            self.w(
                f"| {v['name']} ({v['unit']}) | {v['current']:.4g} | "
                f"{v['q2031'][0]:.3g} / **{v['q2031'][1]:.3g}** / {v['q2031'][2]:.3g} | "
                f"{v['q2036'][0]:.3g} / **{v['q2036'][1]:.3g}** / {v['q2036'][2]:.3g} |"
            )
        self.w()

    def _sensitivity(self) -> None:
        self.w("## What drives the outcome")
        self.w()
        self.w(
            "Share of the variance in peak systemic stress attributable to each event "
            "firing at all. High-scoring nodes are the ones worth watching, because "
            "learning how they resolve collapses the most uncertainty about everything "
            "else."
        )
        self.w()
        self.w(
            "*Read with one caveat:* the stress index is built from these same events, so "
            "part of any node's score is its own contribution rather than its influence "
            "on others. The ranking is still informative — it combines probability, "
            "impact rating and correlation with the rest of the system in one number — "
            "but it is not a pure causal-influence measure, and a node cannot score high "
            "here without being either likely or heavy."
        )
        self.w()
        self.w("| Event | Variance share | P(by 2036) | Impact |")
        self.w("|---|---:|---:|---:|")
        for s in self.ctx["sensitivity"]:
            self.w(
                f"| {s['name']} | {s['share']*100:.1f}% | {pct(s['p2036'])} | "
                f"{s['severity']:.0f} |"
            )
        self.w()

    def _disagreement(self) -> None:
        self.w("## Where the worldviews disagree most")
        self.w()
        self.w(
            "The five parameterisations — raw analyst, audited, outside-view base rates, "
            "structural-break inside view, and prediction-market check — converge on most "
            "nodes. These are the ones where they don't, and they are exactly the "
            "forecasts you should hold most loosely."
        )
        self.w()
        self.w("| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |")
        self.w("|---|---:|---:|---:|---:|---:|---:|")
        for d in self.ctx["disagreement"]:
            vals = " | ".join(pct(v) for v in d["by_view"])
            self.w(f"| {d['name']} | {vals} | {d['spread']*100:.0f}pp |")
        self.w()

    def _critiques(self) -> None:
        crits = self.ctx.get("critiques") or []
        if not crits:
            return
        self.w("## What the red team said")
        self.w()
        word = {1: "One lens", 2: "Two lenses", 3: "Three lenses"}.get(
            len(crits), f"{len(crits)} lenses"
        )
        verb = "attacked" if len(crits) != 1 else "attacked"
        self.w(
            f"{word} {verb} the parameter set from different directions. Their numeric "
            "corrections are already in the forecast, carried by their own worldviews. "
            "Their reasoning is reproduced here because some of it is more useful than "
            "the numbers — and because a reader deserves to see the case against the "
            "model alongside its output."
        )
        self.w()
        for c in crits:
            self.w(f"### {c['lens']}")
            self.w()
            self.w(f"*{c['n_corrections']} specific corrections proposed.*")
            self.w()
            self.w(c["critique"])
            self.w()
            if c["bias"]:
                self.w(f"**Systematic bias estimate.** {c['bias']}")
                self.w()
            if c["missing_scenarios"]:
                self.w("**Scenarios it says are missing entirely:**")
                self.w()
                for m in c["missing_scenarios"][:8]:
                    self.w(f"- {m}")
                self.w()

    def _calendar(self) -> None:
        cal = self.ctx.get("calendar") or []
        if not cal:
            return
        self.w("## What to watch, and when")
        self.w()
        self.w(
            "Dated forcing functions the analysts flagged. These are the model's "
            "*inputs*, not its outputs — the scheduled moments when a hazard gets "
            "resolved or reset. More actionable than any single probability on this "
            "page, because they are the points at which you get to update."
        )
        self.w()
        self.w("| Date | Domain | Event | Why it matters |")
        self.w("|---|---|---|---|")
        for e in cal[:45]:
            self.w(
                f"| `{e['date']}` | {e['domain']} | **{e['name']}** | {e['why']} |"
            )
        self.w()

    def _limits(self) -> None:
        self.w("## What this model cannot do")
        self.w()
        for line in self.ctx["limits"]:
            self.w(f"- {line}")
        self.w()
        self.w("---")
        self.w()
        self.w(
            "*Generated by the `worldsim` Monte Carlo engine. Parameters, dependency "
            "structure, and red-team corrections are in `params/`; rerun with "
            "`python run_simulation.py`.*"
        )


def write_outputs(ctx: dict, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "forecast_report.md").write_text(ReportBuilder(ctx).build())

    serialisable = json.loads(json.dumps(ctx, default=_json_default))
    (outdir / "forecast.json").write_text(json.dumps(serialisable, indent=2))


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)

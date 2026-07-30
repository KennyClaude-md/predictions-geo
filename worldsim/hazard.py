"""Turning elicited cumulative probabilities into per-quarter hazard rates.

Analysts give a handful of points on each risk's CDF — P(by end-2027), P(by
end-2031), P(by end-2036), and for the long horizon P(by end-2046) and P(by
end-2056). The simulator needs a per-quarter firing probability. This module does
that inversion for an arbitrary number of anchors, plus the numerical housekeeping
that keeps it honest:

  * isotonic repair, because elicited cumulatives are frequently non-monotone;
  * clamping away from 0 and 1, because log(0) ends simulations badly;
  * a piecewise-constant hazard within each elicitation segment, which is the
    maximum-entropy choice given we only observe a few points on the CDF.

A note on why hazard rather than "roll a die once against the cumulative": we
need events to have *times*, so that a Taiwan contingency in 2027 can propagate
into semiconductor and financial nodes in 2028 while the same event in 2035
cannot. Survival modelling gives us that for free.

A note on the long horizon: a piecewise-constant hazard across five anchors can
represent a rate that falls as a window closes or rises as forcing compounds,
which is exactly what a 30-year run needs and what a single constant-hazard
extrapolation past 2036 could not do.
"""

from __future__ import annotations

import numpy as np

from .timeline import YEARS_PER_QUARTER, active

# Elicited probabilities are never taken at face value at the extremes: a stated
# 0% becomes 0.05% and a stated 100% becomes 99.5%. Forecasters who write 0 or 100
# essentially never mean it literally, and the log-odds machinery needs finite values.
P_FLOOR = 0.0005
P_CEIL = 0.995


def _as_fraction(pct: float) -> float:
    return float(np.clip(pct / 100.0, P_FLOOR, P_CEIL))


def isotonic_cumulative(*pcts: float) -> tuple[float, ...]:
    """Force a non-decreasing cumulative sequence with minimal movement.

    Pool-adjacent-violators over any number of points. When an analyst writes a
    *decreasing* cumulative sequence it usually means they were thinking about
    per-period rates rather than cumulatives, so averaging the offending run is
    the least-assumption repair.
    """
    vals = [_as_fraction(p) for p in pcts]
    if all(a <= b for a, b in zip(vals, vals[1:])):
        return tuple(vals)

    blocks: list[tuple[float, float]] = []  # (pooled value, weight)
    for v in vals:
        blocks.append((v, 1.0))
        while len(blocks) > 1 and blocks[-2][0] > blocks[-1][0]:
            v2, w2 = blocks.pop()
            v1, w1 = blocks.pop()
            blocks.append(((v1 * w1 + v2 * w2) / (w1 + w2), w1 + w2))

    out: list[float] = []
    for v, w in blocks:
        out.extend([v] * int(round(w)))
    return tuple(out[: len(vals)])


def piecewise_quarter_hazard(
    *pcts: float, max_quarter: int | None = None
) -> np.ndarray:
    """Per-quarter hazard array of length n_quarters, from the anchor CDF points.

    One constant-hazard segment per anchor. Across segments the rate is free to
    rise or fall, which is what lets the model represent "acute risk over the next
    two years, then it settles down" as distinct from "slow-building".

    `max_quarter` caps where a node can still fire. Some criteria are locked to a
    near-term context — "the 2026-27 El Nino", "Census 2027", a named living
    official leaving office — and must not accrue hazard for decades after they
    have become unresolvable.
    """
    h = active()
    anchors = h.anchor_quarters
    n_q = h.n_quarters
    if len(pcts) != len(anchors):
        raise ValueError(
            f"horizon {h.name} expects {len(anchors)} anchors, got {len(pcts)}"
        )

    cum = isotonic_cumulative(*pcts)
    surv = [1.0 - c for c in cum]

    hazard = np.empty(n_q, dtype=np.float64)
    prev_q, prev_s = 0, 1.0
    for q, s in zip(anchors, surv):
        seg_years = (q - prev_q) * YEARS_PER_QUARTER
        # Continuous-time hazard per year within this segment.
        h_year = -np.log(max(s / prev_s, 1e-9)) / seg_years
        hazard[prev_q:q] = h_year
        prev_q, prev_s = q, s

    # Annual continuous hazard -> per-quarter discrete probability.
    out = 1.0 - np.exp(-hazard * YEARS_PER_QUARTER)
    if max_quarter is not None and max_quarter < n_q:
        out[max_quarter:] = 0.0
    return out


def logit(p: np.ndarray | float) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=np.float64), 1e-12, 1 - 1e-12)
    return np.log(p / (1.0 - p))


def expit(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -60.0, 60.0)))


def cumulative_from_quarter_hazard(h: np.ndarray) -> np.ndarray:
    """CDF implied by a per-quarter hazard vector, for verification."""
    return 1.0 - np.cumprod(1.0 - np.clip(h, 0.0, 1.0))

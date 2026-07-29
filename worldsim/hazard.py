"""Turning elicited cumulative probabilities into per-quarter hazard rates.

Analysts give us three numbers per risk: P(happens by end-2027), P(by end-2031),
P(by end-2036). The simulator needs a per-quarter firing probability. This module
does that inversion, plus the numerical housekeeping that keeps it honest:

  * isotonic repair, because elicited cumulatives are frequently non-monotone;
  * clamping away from 0 and 1, because log(0) ends simulations badly;
  * a piecewise-constant hazard within each elicitation segment, which is the
    maximum-entropy choice given we only observe three points on the CDF.

A note on why hazard rather than "roll a die once against the cumulative": we
need events to have *times*, so that a Taiwan contingency in 2027 can propagate
into semiconductor and financial nodes in 2028 while the same event in 2035
cannot. Survival modelling gives us that for free.
"""

from __future__ import annotations

import numpy as np

from .timeline import ANCHOR_QUARTERS, N_QUARTERS, YEARS_PER_QUARTER

# Elicited probabilities are never taken at face value at the extremes: a stated
# 0% becomes 0.05% and a stated 100% becomes 99.5%. Forecasters who write 0 or 100
# essentially never mean it literally, and the log-odds machinery needs finite values.
P_FLOOR = 0.0005
P_CEIL = 0.995


def clamp_prob(p: float) -> float:
    return float(np.clip(p / 100.0 if p > 1.0 else p, P_FLOOR, P_CEIL))


def _as_fraction(pct: float) -> float:
    return float(np.clip(pct / 100.0, P_FLOOR, P_CEIL))


def isotonic_cumulative(p1: float, p2: float, p3: float) -> tuple[float, float, float]:
    """Force P(2027) <= P(2031) <= P(2036) with minimal movement.

    Pool-adjacent-violators on three points, done longhand. When an analyst writes
    a *decreasing* cumulative sequence it usually means they were thinking about
    per-period rates rather than cumulatives, so averaging the offending pair is
    the least-assumption repair.
    """
    a, b, c = _as_fraction(p1), _as_fraction(p2), _as_fraction(p3)
    if a <= b <= c:
        return a, b, c
    # Pool violating adjacent pairs until monotone.
    vals = [a, b, c]
    weights = [1.0, 1.0, 1.0]
    blocks: list[tuple[float, float]] = []
    for v, w in zip(vals, weights):
        blocks.append((v, w))
        while len(blocks) > 1 and blocks[-2][0] > blocks[-1][0]:
            v2, w2 = blocks.pop()
            v1, w1 = blocks.pop()
            pooled = (v1 * w1 + v2 * w2) / (w1 + w2)
            blocks.append((pooled, w1 + w2))
    out: list[float] = []
    for v, w in blocks:
        out.extend([v] * int(round(w)))
    return float(out[0]), float(out[1]), float(out[2])


def piecewise_quarter_hazard(p2027: float, p2031: float, p2036: float) -> np.ndarray:
    """Per-quarter hazard array of length N_QUARTERS.

    Within each elicitation segment the hazard is constant; across segments it is
    free to rise or fall, which is what lets the model represent e.g. "acute risk
    over the next two years, then it settles down" versus "slow-building".
    """
    a, b, c = isotonic_cumulative(p2027, p2031, p2036)

    q1 = ANCHOR_QUARTERS["p_by_2027_pct"]
    q2 = ANCHOR_QUARTERS["p_by_2031_pct"]
    q3 = ANCHOR_QUARTERS["p_by_2036_pct"]

    surv = [1.0 - a, 1.0 - b, 1.0 - c]
    # Continuous-time hazard per year within each segment.
    seg_years = [
        q1 * YEARS_PER_QUARTER,
        (q2 - q1) * YEARS_PER_QUARTER,
        (q3 - q2) * YEARS_PER_QUARTER,
    ]
    h_year = [
        -np.log(max(surv[0], 1e-9)) / seg_years[0],
        -np.log(max(surv[1] / surv[0], 1e-9)) / seg_years[1],
        -np.log(max(surv[2] / surv[1], 1e-9)) / seg_years[2],
    ]

    hazard = np.empty(N_QUARTERS, dtype=np.float64)
    hazard[:q1] = h_year[0]
    hazard[q1:q2] = h_year[1]
    hazard[q2:q3] = h_year[2]

    # Convert annual continuous hazard to a per-quarter discrete probability.
    return 1.0 - np.exp(-hazard * YEARS_PER_QUARTER)


def logit(p: np.ndarray | float) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=np.float64), 1e-12, 1 - 1e-12)
    return np.log(p / (1.0 - p))


def expit(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -60.0, 60.0)))


def cumulative_from_quarter_hazard(h: np.ndarray) -> np.ndarray:
    """CDF implied by a per-quarter hazard vector, for verification."""
    return 1.0 - np.cumprod(1.0 - np.clip(h, 0.0, 1.0))

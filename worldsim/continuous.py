"""Continuous state variables, coupled to the discrete world through a copula.

Analysts gave each continuous quantity (global GDP growth, temperature anomaly,
Brent, cereal stocks-to-use, ...) a current value and 2031 deciles. Rather than
invent an event-by-event transmission matrix — which would be a large pile of
made-up coefficients — we do something more honest:

  * the *marginal* distribution of each variable at each date comes straight from
    the elicited deciles, fitted as a two-piece normal so skew survives;
  * the *dependence* on the discrete world comes from a Gaussian copula whose
    driver is the path's own systemic-stress index.

So a path where a Taiwan contingency and a sovereign-debt spiral both fire lands
in the bad tail of GDP growth and the fat tail of oil, without anyone having to
hand-specify "Taiwan blockade => Brent +$38". The elicited marginals are
preserved exactly; only the joint changes.
"""

from __future__ import annotations

import numpy as np
from scipy import stats

from .params import ContinuousVar
from .timeline import N_QUARTERS

Z90 = 1.2815515655446004
# Quarters over which a fired event's contribution to systemic stress decays by 1/e.
STRESS_DECAY_QUARTERS = 11.0
# Median drift is extrapolated past the 2031 anchor at reduced slope: analysts
# anchored on 2031 and linear continuation to 2036 usually overshoots.
POST_ANCHOR_SLOPE_DAMP = 0.6
ANCHOR_Q = 22  # end-2031


def systemic_stress(fire_time: np.ndarray, severity: np.ndarray) -> np.ndarray:
    """Global Systemic Stress Index per path per quarter, shape (n_paths, T).

    Every fired event contributes its *signed* severity, decaying exponentially
    afterwards. A world where three severity-8 events fire in the same 18 months
    scores far higher than one where the same three are spread across a decade —
    which is the point: simultaneity is what breaks systems, not the count.

    Pass signed severity (severity x valence). Stabilising events — a durable
    ceasefire, emissions peaking — then subtract from stress rather than adding to
    it. With unsigned severity the index reads good news as a crisis.
    """
    n = fire_time.shape[0]
    out = np.zeros((n, N_QUARTERS), dtype=np.float32)
    ft = fire_time.astype(np.int16)
    sev = severity.astype(np.float32)
    for t in range(1, N_QUARTERS + 1):
        age = t - ft
        live = (ft >= 0) & (age >= 0)
        decay = np.exp(-np.maximum(age, 0) / STRESS_DECAY_QUARTERS, dtype=np.float32)
        out[:, t - 1] = (live * decay * sev[None, :]).sum(axis=1)
    return out


def stress_percentile(gssi: np.ndarray) -> np.ndarray:
    """Standardise stress to a normal score per quarter, for copula use."""
    n, T = gssi.shape
    z = np.empty_like(gssi, dtype=np.float32)
    for t in range(T):
        col = gssi[:, t]
        ranks = stats.rankdata(col, method="average")
        u = (ranks - 0.5) / n
        z[:, t] = stats.norm.ppf(u).astype(np.float32)
    return z


class TwoPieceNormal:
    """Normal with different spread either side of the median.

    Fitted to (p10, p50, p90). Keeps the elicited asymmetry — which matters,
    because almost every variable here is skewed (growth has a long left tail,
    oil and food prices have long right tails).
    """

    def __init__(self, p10: float, p50: float, p90: float):
        self.median = float(p50)
        self.s_lo = max(abs(p50 - p10) / Z90, 1e-9)
        self.s_hi = max(abs(p90 - p50) / Z90, 1e-9)

    def ppf(self, z: np.ndarray) -> np.ndarray:
        return self.median + np.where(z < 0, z * self.s_lo, z * self.s_hi)


def simulate_continuous(
    variables: list[ContinuousVar],
    stress_z: np.ndarray,
    stress_loadings: dict[str, float],
    rng: np.random.Generator,
) -> dict[str, np.ndarray]:
    """Return {var_id: (n_paths, T) values}.

    Idiosyncratic innovation is a persistent AR(1) so that trajectories look like
    trajectories rather than independent draws stapled together, then rank-mapped
    back to standard normal before the copula step so the elicited marginals are
    not distorted by the persistence.
    """
    n, T = stress_z.shape
    out: dict[str, np.ndarray] = {}

    phi = 0.86  # quarterly persistence of the idiosyncratic component
    for var in variables:
        rho = float(np.clip(stress_loadings.get(var.id, 0.0), -0.95, 0.95))

        eps = np.empty((n, T), dtype=np.float32)
        prev = rng.standard_normal(n).astype(np.float32)
        for t in range(T):
            prev = phi * prev + np.sqrt(1 - phi**2) * rng.standard_normal(n).astype(np.float32)
            eps[:, t] = prev

        z = rho * stress_z + np.sqrt(max(1 - rho**2, 0.0)) * eps

        dist = TwoPieceNormal(var.p10, var.p50, var.p90)
        vals = np.empty((n, T), dtype=np.float32)
        for t in range(1, T + 1):
            # Uncertainty widens diffusively; the elicited deciles pin t = ANCHOR_Q.
            scale = np.sqrt(t / ANCHOR_Q)
            if t <= ANCHOR_Q:
                med = var.current + (dist.median - var.current) * (t / ANCHOR_Q)
            else:
                slope = (dist.median - var.current) / ANCHOR_Q
                med = dist.median + slope * POST_ANCHOR_SLOPE_DAMP * (t - ANCHOR_Q)
            shaped = dist.ppf(z[:, t - 1]) - dist.median
            vals[:, t - 1] = med + shaped * scale
        out[var.id] = vals
    return out



"""Parameter compilation for GEO-SIM.

Takes the loosely-structured JSON produced by the domain-intelligence fleet and
compiles it into dense numpy arrays the engine can march forward. This module is
where every judgement call about *units* lives, so it is worth stating them once:

Indicators are modelled in their natural units (degrees C, ppm, percent of GDP,
index points). Wherever a parameter is expressed in "SDs" -- driver
elasticities, event impacts, coupling strengths -- the SD in question is the
indicator's *stationary* standard deviation, computed from its annual
innovation volatility and its mean-reversion rate rather than taken on faith.

z-scores are measured against the indicator's attractor, not against its
starting value. That is deliberate: an indicator that starts far from its
long-run attractor should register as stressed from quarter zero, and one with
a persistent drift should register as increasingly stressed over the horizon.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

# Confidence tags from the analysts become the width of the per-path lognormal
# jitter applied to each event's base hazard. This is how epistemic uncertainty
# (we don't know the hazard) enters alongside aleatoric uncertainty (the world
# is stochastic even if we did).
CONFIDENCE_SIGMA = {"low": 0.75, "medium": 0.48, "high": 0.30}

# Floor on mean reversion used when converting annual innovation volatility into
# a stationary SD. Without it, a near-random-walk indicator would be assigned an
# infinite scale and every elasticity referencing it would silently vanish.
KAPPA_FLOOR = 0.15

QUARTERS_PER_YEAR = 4


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", str(s).strip().lower()).strip("_")


@dataclass
class Indicator:
    key: str
    label: str
    domain: str
    value: float
    unit: str
    as_of: str
    source: str
    drift: float
    vol: float
    floor: float
    ceiling: float
    kappa: float
    attractor: float
    scale: float = 0.0

    def compute_scale(self) -> None:
        """Stationary SD of the OU process, bounded by the admissible range."""
        k = max(self.kappa, KAPPA_FLOOR)
        stat = self.vol / math.sqrt(2.0 * k)
        span = abs(self.ceiling - self.floor)
        if span > 0:
            stat = min(stat, span / 4.0)
        self.scale = max(stat, 1e-9)


@dataclass
class Event:
    id: str
    domain: str
    statement: str
    resolution_criteria: str
    reference_class: str
    base_rate_annual: float
    hazard_multiplier_now: float
    p_by: dict[float, float]
    drivers: list[str]
    elasticities: list[float]
    impacts: list[str]
    impact_sizes: list[float]
    absorbing: bool
    confidence: str
    reasoning: str
    prior_hazard: float = 0.0
    calibration_offset: float = 0.0


@dataclass
class Coupling:
    src: str
    dst: str
    strength: float
    lag_q: int
    mechanism: str


@dataclass
class Contagion:
    if_event: str
    then_event: str
    multiplier: float
    decay_q: float
    mechanism: str


@dataclass
class Stabilizer:
    trigger: str
    damps: str
    strength: float
    mechanism: str


@dataclass
class Regime:
    name: str
    description: str
    p0: float
    persistence: float
    hazard_mult: float
    vol_mult: float
    growth_offset: float
    coop_offset: float


# Horizons the analysts were asked to quote, expressed as years from 2026-07-29.
# 2027 and 2030 mean "end of that calendar year"; 2036 likewise.
HORIZON_YEARS = {2027: 1.42, 2030: 4.42, 2036: 10.42}


@dataclass
class CompiledParams:
    """Dense arrays plus the metadata needed to interpret them."""

    indicators: list[Indicator]
    events: list[Event]
    regimes: list[Regime]
    contagions: list[Contagion]
    stabilizers: list[Stabilizer]
    couplings: list[Coupling]
    dropped: list[str] = field(default_factory=list)

    # populated by build()
    ikey: dict[str, int] = field(default_factory=dict)
    ekey: dict[str, int] = field(default_factory=dict)
    x0: np.ndarray = None
    drift: np.ndarray = None
    vol: np.ndarray = None
    lo: np.ndarray = None
    hi: np.ndarray = None
    kappa: np.ndarray = None
    attractor: np.ndarray = None
    scale: np.ndarray = None
    coupling_by_lag: dict[int, np.ndarray] = field(default_factory=dict)
    chol: np.ndarray = None
    base_hazard: np.ndarray = None
    elasticity: np.ndarray = None
    impact: np.ndarray = None
    absorbing: np.ndarray = None
    conf_sigma: np.ndarray = None
    contagion_idx: tuple = None
    stab_idx: tuple = None
    regime_p0: np.ndarray = None
    regime_trans_q: np.ndarray = None
    regime_hazard: np.ndarray = None
    regime_vol: np.ndarray = None
    regime_growth: np.ndarray = None
    regime_coop: np.ndarray = None
    contagion_decay: np.ndarray = None
    contagion_decay_factor: np.ndarray = None
    calib_offset: np.ndarray = None
    growth_idx: int = -1
    coop_idx: int = -1


def implied_hazard(ev: Event) -> float:
    """Recover a constant annual hazard from the analyst's cumulative quotes.

    The three elicited cumulative probabilities over-determine a single hazard,
    so we take a precision-weighted average in log-survival space and blend the
    result with the bottom-up base_rate x multiplier. Longer horizons carry more
    information about the hazard and are weighted accordingly, but the near
    horizon is not discarded -- disagreement between them is real signal about
    whether the analyst thinks risk is front- or back-loaded.
    """
    ests, weights = [], []
    for year, t in HORIZON_YEARS.items():
        p = ev.p_by.get(year)
        if p is None:
            continue
        p = min(max(float(p), 1e-4), 0.9985)
        ests.append(-math.log(1.0 - p) / t)
        weights.append(math.sqrt(t))

    bottom_up = max(ev.base_rate_annual * ev.hazard_multiplier_now, 1e-6)
    if not ests:
        return bottom_up

    top_down = float(np.average(ests, weights=weights))
    top_down = max(top_down, 1e-6)

    # Geometric blend: the cumulative quotes are what the analyst actually
    # reasoned about and get the majority weight, but the explicit reference
    # class keeps a stubbornly low base rate from being argued away entirely.
    w = 0.65
    return math.exp(w * math.log(top_down) + (1 - w) * math.log(bottom_up))


def load(domain_files: list[Path], coupling_file: Path) -> CompiledParams:
    indicators: list[Indicator] = []
    events: list[Event] = []
    couplings: list[Coupling] = []
    seen_i, seen_e = set(), set()

    for fp in sorted(domain_files):
        with open(fp) as fh:
            d = json.load(fh)
        dom = d.get("domain", fp.stem)

        for raw in d.get("indicators", []):
            key = _slug(raw["key"])
            if key in seen_i:
                continue
            seen_i.add(key)
            lo = float(raw.get("floor", -1e9))
            hi = float(raw.get("ceiling", 1e9))
            if hi <= lo:
                lo, hi = -1e9, 1e9
            ind = Indicator(
                key=key,
                label=raw.get("label", key),
                domain=dom,
                value=float(raw["value"]),
                unit=raw.get("unit", ""),
                as_of=raw.get("as_of", ""),
                source=raw.get("source", ""),
                drift=float(raw.get("annual_drift", 0.0)),
                vol=abs(float(raw.get("annual_vol", 0.0))) or 1e-6,
                floor=lo,
                ceiling=hi,
                kappa=min(max(float(raw.get("mean_reversion", 0.2)), 0.0), 2.0),
                attractor=float(raw.get("attractor", raw["value"])),
            )
            ind.compute_scale()
            indicators.append(ind)

        for raw in d.get("events", []):
            eid = _slug(raw["id"])
            if eid in seen_e:
                continue
            seen_e.add(eid)
            events.append(
                Event(
                    id=eid,
                    domain=dom,
                    statement=raw.get("statement", eid),
                    resolution_criteria=raw.get("resolution_criteria", ""),
                    reference_class=raw.get("reference_class", ""),
                    base_rate_annual=max(float(raw.get("base_rate_annual", 0.01)), 1e-6),
                    hazard_multiplier_now=max(float(raw.get("hazard_multiplier_now", 1.0)), 1e-3),
                    p_by={
                        2027: raw.get("p_by_2027"),
                        2030: raw.get("p_by_2030"),
                        2036: raw.get("p_by_2036"),
                    },
                    drivers=[_slug(x) for x in raw.get("drivers", [])],
                    elasticities=[float(x) for x in raw.get("driver_elasticities", [])],
                    impacts=[_slug(x) for x in raw.get("impacts", [])],
                    impact_sizes=[float(x) for x in raw.get("impact_sizes", [])],
                    absorbing=bool(raw.get("absorbing", False)),
                    confidence=str(raw.get("confidence", "medium")).lower(),
                    reasoning=raw.get("reasoning", ""),
                )
            )

        for c in d.get("couplings", []):
            couplings.append(
                Coupling(_slug(c["from"]), _slug(c["to"]), float(c.get("strength", 0.0)),
                         int(round(float(c.get("lag_quarters", 0)))), c.get("mechanism", ""))
            )

    with open(coupling_file) as fh:
        cp = json.load(fh)

    for c in cp.get("cross_domain_couplings", []):
        couplings.append(
            Coupling(_slug(c["from"]), _slug(c["to"]), float(c.get("strength", 0.0)),
                     int(round(float(c.get("lag_quarters", 0)))), c.get("mechanism", ""))
        )

    regimes = [
        Regime(
            name=r["name"],
            description=r.get("description", ""),
            p0=float(r.get("initial_probability", 0.0)),
            persistence=min(max(float(r.get("annual_persistence", 0.8)), 0.05), 0.995),
            hazard_mult=max(float(r.get("hazard_multiplier", 1.0)), 1e-3),
            vol_mult=max(float(r.get("vol_multiplier", 1.0)), 1e-3),
            growth_offset=float(r.get("growth_offset", 0.0)),
            coop_offset=float(r.get("cooperation_offset", 0.0)),
        )
        for r in cp.get("regimes", [])
    ]

    contagions = [
        Contagion(_slug(c["if_event"]), _slug(c["then_event"]),
                  max(float(c.get("hazard_multiplier", 1.0)), 1e-3),
                  max(float(c.get("decay_quarters", 4)), 0.5), c.get("mechanism", ""))
        for c in cp.get("contagion_rules", [])
    ]

    stabilizers = [
        Stabilizer(_slug(s["trigger"]), _slug(s["damps"]),
                   abs(float(s.get("strength", 0.0))), s.get("mechanism", ""))
        for s in cp.get("stabilizing_feedbacks", [])
    ]

    params = CompiledParams(indicators, events, regimes, contagions, stabilizers, couplings)
    _build(params, cp.get("shock_correlations", []), cp.get("regime_transition_matrix"))
    return params


def _nearest_psd(a: np.ndarray) -> np.ndarray:
    """Project a hand-authored correlation matrix onto the PSD cone.

    Analysts specify correlations pairwise and pairwise-consistent does not mean
    jointly consistent, so this is load-bearing rather than defensive.
    """
    a = (a + a.T) / 2.0
    w, v = np.linalg.eigh(a)
    w = np.clip(w, 1e-8, None)
    a = v @ np.diag(w) @ v.T
    d = np.sqrt(np.clip(np.diag(a), 1e-12, None))
    a = a / np.outer(d, d)
    np.fill_diagonal(a, 1.0)
    return a


def _build(P: CompiledParams, shock_corrs: list, trans: list | None) -> None:
    K = len(P.indicators)
    E = len(P.events)
    P.ikey = {ind.key: i for i, ind in enumerate(P.indicators)}
    P.ekey = {ev.id: i for i, ev in enumerate(P.events)}

    P.x0 = np.array([i.value for i in P.indicators], dtype=np.float64)
    P.drift = np.array([i.drift for i in P.indicators], dtype=np.float64)
    P.vol = np.array([i.vol for i in P.indicators], dtype=np.float64)
    P.lo = np.array([i.floor for i in P.indicators], dtype=np.float64)
    P.hi = np.array([i.ceiling for i in P.indicators], dtype=np.float64)
    P.kappa = np.array([i.kappa for i in P.indicators], dtype=np.float64)
    P.attractor = np.array([i.attractor for i in P.indicators], dtype=np.float64)
    P.scale = np.array([i.scale for i in P.indicators], dtype=np.float64)

    # --- couplings, grouped by lag so each lag is one dense matmul -----------
    by_lag: dict[int, np.ndarray] = {}
    for c in P.couplings:
        if c.src not in P.ikey or c.dst not in P.ikey:
            P.dropped.append(f"coupling {c.src}->{c.dst} (unknown indicator)")
            continue
        if c.src == c.dst:
            P.dropped.append(f"coupling {c.src}->{c.dst} (self-loop)")
            continue
        lag = min(max(c.lag_q, 0), 8)
        M = by_lag.setdefault(lag, np.zeros((K, K)))
        # Elasticities are additive when two analysts describe the same channel;
        # clipping keeps a single overheated edge from dominating the system.
        M[P.ikey[c.dst], P.ikey[c.src]] += float(np.clip(c.strength, -1.2, 1.2))
    for lag in by_lag:
        by_lag[lag] = np.clip(by_lag[lag], -1.5, 1.5)
    P.coupling_by_lag = by_lag

    # --- innovation correlation ---------------------------------------------
    R = np.eye(K)
    for sc in shock_corrs:
        a, b = _slug(sc.get("a", "")), _slug(sc.get("b", ""))
        if a in P.ikey and b in P.ikey and a != b:
            rho = float(np.clip(sc.get("rho", 0.0), -0.95, 0.95))
            R[P.ikey[a], P.ikey[b]] = rho
            R[P.ikey[b], P.ikey[a]] = rho
    P.chol = np.linalg.cholesky(_nearest_psd(R))

    # --- events --------------------------------------------------------------
    P.base_hazard = np.zeros(E)
    P.elasticity = np.zeros((E, K))
    P.impact = np.zeros((E, K))
    P.absorbing = np.zeros(E, dtype=bool)
    P.conf_sigma = np.zeros(E)

    for j, ev in enumerate(P.events):
        ev.prior_hazard = implied_hazard(ev)
        P.base_hazard[j] = ev.prior_hazard
        P.absorbing[j] = ev.absorbing
        P.conf_sigma[j] = CONFIDENCE_SIGMA.get(ev.confidence, 0.48)
        for name, el in zip(ev.drivers, ev.elasticities):
            if name in P.ikey:
                P.elasticity[j, P.ikey[name]] += float(np.clip(el, -1.5, 1.5))
            else:
                P.dropped.append(f"driver {name} for {ev.id} (unknown indicator)")
        for name, sz in zip(ev.impacts, ev.impact_sizes):
            if name in P.ikey:
                P.impact[j, P.ikey[name]] += float(np.clip(sz, -6.0, 6.0))
            else:
                P.dropped.append(f"impact {name} for {ev.id} (unknown indicator)")

    # --- contagion -----------------------------------------------------------
    src, dst, mult, decay = [], [], [], []
    for c in P.contagions:
        if c.if_event in P.ekey and c.then_event in P.ekey and c.if_event != c.then_event:
            src.append(P.ekey[c.if_event])
            dst.append(P.ekey[c.then_event])
            mult.append(float(np.clip(c.multiplier, 0.05, 25.0)))
            decay.append(float(np.clip(c.decay_q, 0.5, 40.0)))
        else:
            P.dropped.append(f"contagion {c.if_event}->{c.then_event} (unknown event)")
    P.contagion_idx = (
        np.array(src, dtype=np.int64), np.array(dst, dtype=np.int64),
        np.log(np.array(mult)) if mult else np.zeros(0),
        np.array(decay) if decay else np.zeros(0),
    )

    # Per-target decay: an event's inherited amplification fades at the average
    # rate of the rules pointing at it, defaulting to four quarters.
    decay_per_event = np.full(E, 4.0)
    if dst:
        acc = np.zeros(E)
        cnt = np.zeros(E)
        np.add.at(acc, np.array(dst), np.array(decay))
        np.add.at(cnt, np.array(dst), 1.0)
        hit = cnt > 0
        decay_per_event[hit] = acc[hit] / cnt[hit]
    P.contagion_decay = decay_per_event
    P.contagion_decay_factor = np.exp(-1.0 / np.maximum(decay_per_event, 0.5))

    # No calibration applied until Simulator.calibrate() runs.
    P.calib_offset = np.zeros(E)

    # --- stabilizing feedbacks ----------------------------------------------
    st, sd, ss = [], [], []
    for s in P.stabilizers:
        if s.trigger in P.ikey and s.damps in P.ikey:
            st.append(P.ikey[s.trigger])
            sd.append(P.ikey[s.damps])
            ss.append(float(np.clip(s.strength, 0.0, 1.5)))
        else:
            P.dropped.append(f"stabilizer {s.trigger}->{s.damps} (unknown indicator)")
    P.stab_idx = (np.array(st, dtype=np.int64), np.array(sd, dtype=np.int64), np.array(ss))

    # --- regimes -------------------------------------------------------------
    Rn = len(P.regimes)
    p0 = np.array([r.p0 for r in P.regimes], dtype=np.float64)
    p0 = p0 / p0.sum() if p0.sum() > 0 else np.full(Rn, 1.0 / Rn)
    P.regime_p0 = p0
    P.regime_hazard = np.array([r.hazard_mult for r in P.regimes])
    P.regime_vol = np.array([r.vol_mult for r in P.regimes])
    P.regime_growth = np.array([r.growth_offset for r in P.regimes])
    P.regime_coop = np.array([r.coop_offset for r in P.regimes])

    A = np.array(trans, dtype=np.float64) if trans else None
    if A is None or A.shape != (Rn, Rn):
        # Fall back to persistence-on-the-diagonal with the remainder spread over
        # the other regimes in proportion to their unconditional weight.
        A = np.zeros((Rn, Rn))
        for i, r in enumerate(P.regimes):
            A[i] = (1 - r.persistence) * p0 / max(p0.sum() - p0[i], 1e-9)
            A[i, i] = 0.0
            A[i, i] = r.persistence
    A = np.clip(A, 0.0, None)
    A = A / A.sum(axis=1, keepdims=True)
    P.regime_trans_q = _quarterly_root(A)

    P.growth_idx = _find(P.ikey, ["global_gdp_growth", "world_gdp_growth", "gdp_growth"])
    P.coop_idx = _find(P.ikey, ["multilateral_cooperation_index", "institutional_trust_index"])


def _find(keys: dict[str, int], candidates: list[str]) -> int:
    for c in candidates:
        if c in keys:
            return keys[c]
    for c in candidates:
        for k, i in keys.items():
            if c in k:
                return i
    return -1


def _quarterly_root(A: np.ndarray) -> np.ndarray:
    """Fourth root of an annual transition matrix, with a safe fallback.

    The principal matrix root of a stochastic matrix is not guaranteed to be
    stochastic. When it isn't, the first-order approximation I + (A-I)/4 is
    both stochastic and accurate for the sticky matrices regimes produce.
    """
    try:
        from scipy.linalg import fractional_matrix_power

        Q = np.real(fractional_matrix_power(A, 0.25))
        if np.all(Q > -1e-9) and np.allclose(Q.sum(axis=1), 1.0, atol=1e-6):
            Q = np.clip(Q, 0.0, None)
            return Q / Q.sum(axis=1, keepdims=True)
    except Exception:
        pass
    Q = np.eye(A.shape[0]) + (A - np.eye(A.shape[0])) / QUARTERS_PER_YEAR
    Q = np.clip(Q, 0.0, None)
    return Q / Q.sum(axis=1, keepdims=True)

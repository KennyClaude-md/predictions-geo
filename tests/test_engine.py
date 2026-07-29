#!/usr/bin/env python3
"""Validation suite for the GEO-SIM engine.

These are not smoke tests. Each one checks the engine against a quantity that
can be derived analytically or bounded on theoretical grounds, because a
simulator whose numbers nobody can check is a random number generator with
opinions.

Run: python tests/test_engine.py
"""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from geosim import Simulator, load  # noqa: E402

PASS, FAIL = [], []


def check(name: str, cond: bool, detail: str = "") -> None:
    (PASS if cond else FAIL).append(name)
    print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))


def build(indicators, events, coupling=None, tmp=None):
    """Write a minimal parameter set to disk and compile it.

    Goes through the real loader rather than constructing CompiledParams
    directly, so the tests cover unit conversion and key resolution too.
    """
    d = Path(tmp or tempfile.mkdtemp())
    (d / "domain_test.json").write_text(json.dumps({
        "domain": "test", "current_state_summary": "", "indicators": indicators,
        "events": events, "couplings": [], "key_uncertainties": [],
        "surprises_2026": [], "sources": [],
    }))
    base = {"cross_domain_couplings": [], "shock_correlations": [], "regimes": [],
            "regime_transition_matrix": [], "contagion_rules": [],
            "stabilizing_feedbacks": [], "notes": ""}
    base.update(coupling or {})
    (d / "coupling.json").write_text(json.dumps(base))
    return load(sorted(d.glob("domain_*.json")), d / "coupling.json")


def ind(key, value=50.0, vol=5.0, mr=0.2, attr=None, drift=0.0, lo=-1e6, hi=1e6):
    return {"key": key, "label": key, "value": value, "unit": "u", "as_of": "2026-07",
            "source": "test", "annual_drift": drift, "annual_vol": vol, "floor": lo,
            "ceiling": hi, "mean_reversion": mr, "attractor": value if attr is None else attr}


def ev(eid, h, absorbing=True, drivers=(), elas=(), impacts=(), sizes=(), conf="high"):
    """Event whose cumulative quotes are exactly consistent with hazard h."""
    return {"id": eid, "statement": eid, "resolution_criteria": "", "reference_class": "",
            "base_rate_annual": h, "hazard_multiplier_now": 1.0,
            "p_by_2027": 1 - math.exp(-h * 1.42), "p_by_2030": 1 - math.exp(-h * 4.42),
            "p_by_2036": 1 - math.exp(-h * 10.42), "drivers": list(drivers),
            "driver_elasticities": list(elas), "impacts": list(impacts),
            "impact_sizes": list(sizes), "absorbing": absorbing, "confidence": conf,
            "reasoning": ""}


# --------------------------------------------------------------------------- #
def test_hazard_recovery():
    """Constant-hazard events must reproduce 1-exp(-h*t) with no jitter."""
    print("\n[1] analytic hazard recovery")
    hs = [0.005, 0.02, 0.08, 0.25]
    P = build([ind("a")], [ev(f"e{i}", h) for i, h in enumerate(hs)])
    sim = Simulator(P, horizon_years=10.0, seed=1, param_uncertainty=False)
    r = sim.run(n_paths=120_000, chunk=20_000, coupled=False, record_paths=0, verbose=False)
    for i, h in enumerate(hs):
        got = float((r["fire_q"][:, i] >= 0).mean())
        want = 1 - math.exp(-h * 10.0)
        se = math.sqrt(want * (1 - want) / 120_000)
        check(f"h={h}: sim {got:.4f} vs analytic {want:.4f}", abs(got - want) < max(4 * se, 0.006),
              f"{abs(got - want) / max(se, 1e-9):.1f} sigma")


def test_absorbing():
    """Absorbing events fire at most once; recurring ones can fire repeatedly."""
    print("\n[2] absorbing vs recurring")
    P = build([ind("a")], [ev("abs", 0.3, absorbing=True), ev("rec", 0.3, absorbing=False)])
    sim = Simulator(P, horizon_years=10.0, seed=2, param_uncertainty=False)
    r = sim.run(n_paths=40_000, chunk=20_000, coupled=False, record_paths=0, verbose=False)
    check("absorbing never fires twice", int(r["fire_count"][:, 0].max()) == 1,
          f"max={int(r['fire_count'][:, 0].max())}")
    check("recurring does fire twice", int(r["fire_count"][:, 1].max()) > 1,
          f"max={int(r['fire_count'][:, 1].max())}, mean={r['fire_count'][:, 1].mean():.2f}")


def test_ou_variance():
    """Terminal variance must match the OU solution vol^2/(2k)*(1-e^-2kT)."""
    print("\n[3] Ornstein-Uhlenbeck terminal variance")
    for mr, vol in ((0.4, 6.0), (0.15, 3.0)):
        P = build([ind("a", value=50.0, vol=vol, mr=mr)], [ev("e", 0.001)])
        sim = Simulator(P, horizon_years=10.0, seed=3, param_uncertainty=False)
        r = sim.run(n_paths=60_000, chunk=20_000, coupled=False, record_paths=0, verbose=False)
        got = float(r["x_final"][:, 0].std())
        want = math.sqrt(vol**2 / (2 * mr) * (1 - math.exp(-2 * mr * 10.0)))
        # Euler-Maruyama at quarterly steps carries a small discretisation bias.
        check(f"mr={mr} vol={vol}: sd {got:.3f} vs OU {want:.3f}",
              abs(got - want) / want < 0.06, f"{100 * (got - want) / want:+.1f}%")


def test_fat_tails():
    """Innovations must be leptokurtic -- a Gaussian world understates tails."""
    print("\n[4] fat-tailed innovations")
    P = build([ind("a", vol=5.0, mr=0.0)], [ev("e", 0.001)])
    sim = Simulator(P, horizon_years=0.25, seed=4, param_uncertainty=False)
    r = sim.run(n_paths=200_000, chunk=50_000, coupled=False, record_paths=0, verbose=False)
    d = r["x_final"][:, 0] - 50.0
    z = d / d.std()
    kurt = float((z**4).mean())
    p4 = float((np.abs(z) > 4).mean())
    check(f"excess kurtosis {kurt - 3:.2f} > 1", kurt > 4.0)
    check(f"P(|z|>4) = {p4:.5f} exceeds Gaussian 6.3e-5", p4 > 3e-4)


def test_calibration():
    """After calibration, decoupled marginals must match the elicited priors."""
    print("\n[5] calibration convergence (with driver-induced Jensen bias)")
    P = build(
        [ind("a", vol=8.0, mr=0.1, drift=2.0), ind("b", vol=4.0, mr=0.3)],
        [ev("e0", 0.02, drivers=("a",), elas=(0.6,), conf="low"),
         ev("e1", 0.10, drivers=("a", "b"), elas=(0.5, -0.4), conf="medium"),
         ev("e2", 0.004, drivers=("b",), elas=(0.8,), conf="high")],
    )
    sim = Simulator(P, horizon_years=10.42, seed=5)
    targets = sim.calibrate(n=60_000, iters=4, verbose=False)
    r = sim.run(n_paths=120_000, chunk=20_000, coupled=False, record_paths=0, verbose=False)
    for j, e in enumerate(P.events):
        got = float(r["fired"][:, j].mean())
        check(f"{e.id}: sim {got:.4f} vs target {targets[j]:.4f}",
              abs(got - targets[j]) < 0.015, f"delta {got - targets[j]:+.4f}")


def test_contagion():
    """A contagion rule must raise P(B|A) above P(B)."""
    print("\n[6] contagion raises conditional hazard")
    P = build([ind("a")], [ev("trigger", 0.15), ev("target", 0.05)],
              coupling={"contagion_rules": [{"if_event": "trigger", "then_event": "target",
                                             "hazard_multiplier": 6.0, "decay_quarters": 8,
                                             "mechanism": "test"}]})
    sim = Simulator(P, horizon_years=10.0, seed=6, param_uncertainty=False)
    r = sim.run(n_paths=80_000, chunk=20_000, coupled=True, record_paths=0, verbose=False)
    a = r["fired"][:, 0]
    pb = float(r["fired"][:, 1].mean())
    pb_a = float(r["fired"][a, 1].mean())
    pb_na = float(r["fired"][~a, 1].mean())
    check(f"P(B|A)={pb_a:.4f} > P(B|~A)={pb_na:.4f}", pb_a > pb_na + 0.01,
          f"lift {pb_a / max(pb, 1e-9):.2f}x")


def test_coupling_transmission():
    """Coupling must transmit variance from one indicator to another."""
    print("\n[7] cross-indicator transmission")
    P = build([ind("src", vol=10.0, mr=0.1), ind("dst", vol=0.5, mr=0.1)], [ev("e", 0.001)],
              coupling={"cross_domain_couplings": [{"from": "src", "to": "dst", "strength": 0.9,
                                                    "lag_quarters": 1, "mechanism": "t",
                                                    "confidence": "high"}]})
    sim = Simulator(P, horizon_years=10.0, seed=7, param_uncertainty=False)
    on = sim.run(n_paths=30_000, chunk=15_000, coupled=True, record_paths=0, verbose=False)
    off = sim.run(n_paths=30_000, chunk=15_000, coupled=False, record_paths=0, verbose=False)
    s_on, s_off = float(on["x_final"][:, 1].std()), float(off["x_final"][:, 1].std())
    check(f"dst sd coupled {s_on:.3f} > decoupled {s_off:.3f}", s_on > 1.3 * s_off,
          f"{s_on / s_off:.2f}x")
    r = float(np.corrcoef(on["x_final"][:, 0], on["x_final"][:, 1])[0, 1])
    check(f"src/dst terminal correlation {r:.3f} > 0.3", r > 0.3)


def test_stabilizers():
    """Stress-triggered feedbacks must compress the tails they target."""
    print("\n[8] stabilizing feedbacks damp excursions")
    inds = [ind("trig", vol=10.0, mr=0.05), ind("victim", vol=10.0, mr=0.05)]
    evs = [ev("e", 0.001)]
    plain = build(inds, evs)
    damped = build(inds, evs, coupling={"stabilizing_feedbacks": [
        {"trigger": "victim", "damps": "victim", "strength": 1.2, "mechanism": "t"}]})
    a = Simulator(plain, horizon_years=10.0, seed=8, param_uncertainty=False).run(
        n_paths=30_000, chunk=15_000, coupled=True, record_paths=0, verbose=False)
    b = Simulator(damped, horizon_years=10.0, seed=8, param_uncertainty=False).run(
        n_paths=30_000, chunk=15_000, coupled=True, record_paths=0, verbose=False)
    sa, sb = float(a["x_final"][:, 1].std()), float(b["x_final"][:, 1].std())
    check(f"damped sd {sb:.2f} < undamped {sa:.2f}", sb < sa * 0.95, f"{sb / sa:.2f}x")


def test_monotonicity_and_determinism():
    """Cumulative probabilities must be non-decreasing; runs must reproduce."""
    print("\n[9] monotonicity and reproducibility")
    P = build([ind("a", vol=6.0, drift=1.0)],
              [ev(f"e{i}", h, drivers=("a",), elas=(0.5,)) for i, h in enumerate([0.01, 0.05, 0.2])])
    sim = Simulator(P, horizon_years=10.42, seed=9)
    r1 = sim.run(n_paths=20_000, chunk=10_000, coupled=True, record_paths=0, verbose=False)
    r2 = Simulator(P, horizon_years=10.42, seed=9).run(
        n_paths=20_000, chunk=10_000, coupled=True, record_paths=0, verbose=False)
    check("identical seeds reproduce exactly", bool(np.array_equal(r1["fire_q"], r2["fire_q"])))
    ok = True
    for j in range(len(P.events)):
        fq = r1["fire_q"][:, j]
        ps = [float(((fq >= 0) & (fq <= q)).mean()) for q in (5, 17, 41)]
        ok &= ps[0] <= ps[1] <= ps[2]
    check("P(2027) <= P(2030) <= P(2036) for all events", ok)


def test_uncertainty_decomposition():
    """Parameter uncertainty must widen outcome dispersion, not just shift it."""
    print("\n[10] epistemic uncertainty widens the distribution")
    P = build([ind("a", vol=6.0)],
              [ev(f"e{i}", 0.08, conf="low", absorbing=True) for i in range(12)])
    kw = dict(n_paths=40_000, chunk=20_000, coupled=False, record_paths=0, verbose=False)
    known = Simulator(P, horizon_years=10.42, seed=10, param_uncertainty=False).run(**kw)
    unknown = Simulator(P, horizon_years=10.42, seed=10, param_uncertainty=True).run(**kw)
    sk = float(known["fired"].sum(axis=1).std())
    su = float(unknown["fired"].sum(axis=1).std())
    check(f"event-count sd {su:.3f} (uncertain) > {sk:.3f} (known params)", su > sk * 1.05,
          f"{su / sk:.2f}x")


if __name__ == "__main__":
    print("GEO-SIM engine validation")
    for fn in (test_hazard_recovery, test_absorbing, test_ou_variance, test_fat_tails,
               test_calibration, test_contagion, test_coupling_transmission, test_stabilizers,
               test_monotonicity_and_determinism, test_uncertainty_decomposition):
        fn()
    print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
    if FAIL:
        for f in FAIL:
            print(f"  FAILED: {f}")
        sys.exit(1)

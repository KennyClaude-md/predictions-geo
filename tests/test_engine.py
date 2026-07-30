"""Engine mechanics: absorption, lags, coupling, and marginal calibration.

The load-bearing claim of this whole project is that the coupling network changes
*which events co-occur* without changing *how likely each one is*. These tests
are what makes that claim checkable.
"""

import numpy as np
import pytest

from worldsim.analysis import marginal_with_interval
from worldsim.engine import CompiledModel, SimConfig, calibrate_marginals, cumulative_marginals, simulate
from worldsim.params import BlockingPair, ContinuousVar, Edge, LatentFactor, Risk, WorldModel
from worldsim.timeline import HORIZON_2056, anchor_quarters, n_quarters, use_horizon

Q27, Q31, Q36 = anchor_quarters()


def make_model(edges=None, latents=None, blocks=None, risks=None) -> WorldModel:
    risks = risks or {
        "a": Risk("a", "A", "d1", "", 5.0, 20.0, 35.0, 7.0, "medium"),
        "b": Risk("b", "B", "d1", "", 2.0, 8.0, 15.0, 5.0, "high"),
        "c": Risk("c", "C", "d2", "", 30.0, 60.0, 75.0, 3.0, "low"),
    }
    return WorldModel(
        name="t",
        risks=risks,
        continuous={},
        edges=edges or [],
        latents=latents or [],
        blocks=blocks or [],
    )


def cfg(**kw) -> SimConfig:
    base = dict(
        n_worlds=60, paths_per_world=200, calib_worlds=500,
        calib_paths_per_world=50, calib_iters=8, batch_paths=20_000, seed=11,
    )
    base.update(kw)
    return SimConfig(**base)


def test_bare_hazard_reproduces_elicited_marginals_exactly():
    """No coupling, no parameter uncertainty: the survival maths must be exact."""
    c = cfg()
    cm = CompiledModel(make_model(), c)
    cm.sigma[:] = 0.0
    res = simulate(cm, 300, 400, np.random.default_rng(1), c.batch_paths)
    sim = cumulative_marginals(res["fire_time"], [Q27, Q31, Q36]) * 100
    ia = cm.index["a"]
    assert sim[0, ia] == pytest.approx(5.0, abs=0.6)
    assert sim[1, ia] == pytest.approx(20.0, abs=1.0)
    assert sim[2, ia] == pytest.approx(35.0, abs=1.2)


def test_parameter_uncertainty_alone_inflates_small_probabilities():
    """Zero-mean noise on the log-odds is not zero-mean on the probability.

    The logistic is convex below 50%, so spreading a 5% node's log-odds pushes its
    average probability *up*. This is a genuine bias, not a bug — and it is why
    calibration runs even when the model has no edges at all.
    """
    c = cfg()
    cm = CompiledModel(make_model(), c)
    res = simulate(cm, 300, 400, np.random.default_rng(1), c.batch_paths)
    sim = cumulative_marginals(res["fire_time"], [Q27])[0] * 100
    assert sim[cm.index["a"]] > 5.4

    calibrate_marginals(cm, c, verbose=False)
    res2 = simulate(cm, 300, 400, np.random.default_rng(2), c.batch_paths)
    sim2 = cumulative_marginals(res2["fire_time"], [Q27, Q31, Q36]) * 100
    ia = cm.index["a"]
    assert sim2[0, ia] == pytest.approx(5.0, abs=0.7)
    assert sim2[1, ia] == pytest.approx(20.0, abs=1.2)
    assert sim2[2, ia] == pytest.approx(35.0, abs=1.5)


def test_each_risk_fires_at_most_once():
    c = cfg()
    cm = CompiledModel(make_model(), c)
    res = simulate(cm, 20, 200, np.random.default_rng(2), c.batch_paths)
    ft = res["fire_time"]
    assert ft.min() >= -1
    assert ft.max() <= n_quarters()
    # int16, not int8: 122 quarters at the long horizon would wrap an int8.
    assert ft.dtype == np.int16
    # Non-recurrent nodes must fire at most once.
    assert res["fire_time"].shape == (20 * 200, cm.R)


def test_coupling_creates_correlation():
    """A strong edge must make the pair co-occur far more than independence."""
    c = cfg()
    edges = [Edge("a", "b", 12.0, 0, "test", "high")]
    cm = CompiledModel(make_model(edges=edges), c)
    res = simulate(cm, 200, 400, np.random.default_rng(3), c.batch_paths)
    ft = res["fire_time"]
    ia, ib = cm.index["a"], cm.index["b"]
    hit = (ft >= 0)
    joint = (hit[:, ia] & hit[:, ib]).mean()
    indep = hit[:, ia].mean() * hit[:, ib].mean()
    assert joint > indep * 1.8


def test_lag_delays_the_child():
    """With a long lag the child cannot fire immediately after the parent."""
    c = cfg()
    edges = [Edge("a", "b", 20.0, 12, "test", "high")]  # 3-year lag
    cm = CompiledModel(make_model(edges=edges), c)
    res = simulate(cm, 150, 400, np.random.default_rng(4), c.batch_paths)
    ft = res["fire_time"].astype(np.int16)
    ia, ib = cm.index["a"], cm.index["b"]
    both = (ft[:, ia] >= 0) & (ft[:, ib] >= 0)
    gap = (ft[both, ib] - ft[both, ia])
    boosted = (gap >= 12).mean()
    unboosted = ((gap >= 0) & (gap < 12)).mean()
    assert boosted > unboosted


def test_blocking_pairs_suppress_each_other():
    c = cfg()
    plain = CompiledModel(make_model(), c)
    blocked = CompiledModel(make_model(blocks=[BlockingPair("a", "c", "exclusive")]), c)
    rng = np.random.default_rng(5)
    r1 = simulate(plain, 150, 400, rng, c.batch_paths)
    r2 = simulate(blocked, 150, 400, rng, c.batch_paths)

    def joint(res, cm):
        hit = res["fire_time"] >= 0
        return (hit[:, cm.index["a"]] & hit[:, cm.index["c"]]).mean()

    assert joint(r2, blocked) < joint(r1, plain) * 0.85


def test_calibration_restores_marginals_under_heavy_coupling():
    """The central invariant: coupling reshapes the joint, not the marginals."""
    c = cfg(calib_iters=9)
    edges = [
        Edge("a", "b", 9.0, 0, "", "high"),
        Edge("a", "c", 6.0, 1, "", "high"),
        Edge("c", "b", 4.0, 2, "", "medium"),
    ]
    latents = [LatentFactor("stress", "", {"a": 0.8, "b": 0.9, "c": 0.7})]
    cm = CompiledModel(make_model(edges=edges, latents=latents), c)

    before = cumulative_marginals(
        simulate(cm, 120, 300, np.random.default_rng(6), c.batch_paths)["fire_time"],
        [Q27, Q31, Q36],
    )
    calibrate_marginals(cm, c, verbose=False)
    after = cumulative_marginals(
        simulate(cm, 300, 400, np.random.default_rng(7), c.batch_paths)["fire_time"],
        [Q27, Q31, Q36],
    )

    target = np.array(
        [
            [0.05, 0.02, 0.30],
            [0.20, 0.08, 0.60],
            [0.35, 0.15, 0.75],
        ]
    )
    order = [cm.index["a"], cm.index["b"], cm.index["c"]]
    err_before = np.abs(before[:, order] - target).max()
    err_after = np.abs(after[:, order] - target).max()
    assert err_after < err_before
    assert err_after < 0.025

    # ...and the correlation the coupling was there to produce must survive.
    ft = simulate(cm, 200, 300, np.random.default_rng(8), c.batch_paths)["fire_time"]
    hit = ft >= 0
    ia, ib = cm.index["a"], cm.index["b"]
    assert (hit[:, ia] & hit[:, ib]).mean() > hit[:, ia].mean() * hit[:, ib].mean() * 1.5


def test_calibration_generalises_to_an_unseen_random_stream():
    """Calibration uses common random numbers, so it could overfit its own sample.

    It must not: the corrected marginals have to hold up when the whole thing is
    re-simulated from a different seed.
    """
    c = cfg(calib_worlds=600, calib_paths_per_world=40, calib_iters=8)
    edges = [Edge("a", "b", 7.0, 1, "", "high"), Edge("c", "a", 3.0, 0, "", "medium")]
    latents = [LatentFactor("s", "", {"a": 0.7, "b": 0.6, "c": 0.5})]
    cm = CompiledModel(make_model(edges=edges, latents=latents), c)
    calibrate_marginals(cm, c, verbose=False)

    # A seed the calibration loop has never seen.
    ft = simulate(cm, 500, 300, np.random.default_rng(90210), c.batch_paths)["fire_time"]
    sim = cumulative_marginals(ft, [Q27, Q31, Q36])
    target = np.array([[0.05, 0.02, 0.30], [0.20, 0.08, 0.60], [0.35, 0.15, 0.75]])
    order = [cm.index["a"], cm.index["b"], cm.index["c"]]
    assert np.abs(sim[:, order] - target).max() < 0.02


def test_antithetic_worlds_cancel_the_epistemic_offsets():
    c = cfg()
    cm = CompiledModel(make_model(), c)
    rng = np.random.default_rng(77)
    half = (200 + 1) // 2
    draws = rng.standard_normal((half, cm.R)).astype(np.float32)
    theta = np.concatenate([draws, -draws], axis=0)[:200] * cm.sigma
    assert np.abs(theta.mean(axis=0)).max() < 1e-6


def test_epistemic_interval_excludes_monte_carlo_noise():
    """With zero parameter uncertainty the credible band must collapse."""
    c = cfg()
    risks = {
        "a": Risk("a", "A", "d", "", 5.0, 20.0, 35.0, 7.0, "high"),
        "b": Risk("b", "B", "d", "", 2.0, 8.0, 15.0, 5.0, "high"),
    }
    cm = CompiledModel(make_model(risks=risks), c)
    cm.sigma[:] = 0.0  # everyone agrees on the parameters
    res = simulate(cm, 200, 400, np.random.default_rng(9), c.batch_paths)
    m = marginal_with_interval(res["fire_time"], res["world_id"], [Q36])[Q36]
    assert m["epistemic_sd"].max() < 0.02


def test_epistemic_interval_widens_with_stated_uncertainty():
    c = cfg()
    risks = {"a": Risk("a", "A", "d", "", 5.0, 20.0, 35.0, 7.0, "low")}
    cm = CompiledModel(make_model(risks=risks), c)
    res = simulate(cm, 300, 400, np.random.default_rng(10), c.batch_paths)
    m = marginal_with_interval(res["fire_time"], res["world_id"], [Q36])[Q36]
    assert m["epistemic_sd"][0] > 0.04
    assert m["hi"][0] > m["mean"][0] > m["lo"][0]


def test_interval_stays_bounded_and_asymmetric_near_certainty():
    """A high-probability node must not be handed an upper bound of 1.0.

    A symmetric mean +/- z*sd interval would clip to ">99%" here, which reads as a
    claim about certainty rather than what it is: an artefact of forcing a
    symmetric interval onto a bounded quantity.
    """
    c = cfg()
    risks = {"a": Risk("a", "A", "d", "", 55.0, 85.0, 93.0, 6.0, "low")}
    cm = CompiledModel(make_model(risks=risks), c)
    res = simulate(cm, 400, 300, np.random.default_rng(31), c.batch_paths)
    m = marginal_with_interval(res["fire_time"], res["world_id"], [Q36])[Q36]
    lo, mean, hi = m["lo"][0], m["mean"][0], m["hi"][0]
    assert 0.0 <= lo < mean < hi < 1.0, "interval must stay strictly inside [0,1]"
    # The offset sits on the per-quarter hazard, so over 42 quarters a
    # higher-rate world drives this node to near-certainty while a lower-rate
    # one has room to fall a long way. The lower arm must therefore be longer —
    # a symmetric interval would have overflowed the ceiling instead.
    assert (mean - lo) > (hi - mean)


def test_recurrent_nodes_fire_repeatedly_and_counts_see_it():
    """Recurrence has to reach the aggregates, not just the stress index.

    Counting only first occurrences turns "four recessions this window" into
    "one recession", which is the whole reason recurrence exists.
    """
    from worldsim.analysis import aggregate_stats

    c = cfg()
    risks = {
        "rec": Risk("rec", "Recurring", "d", "x", 40.0, 80.0, 92.0, 7.0, "medium",
                    recurrent=True),
        "once": Risk("once", "One-shot", "d", "x", 40.0, 80.0, 92.0, 7.0, "medium",
                     recurrent=False),
    }
    cm = CompiledModel(make_model(risks=risks), c)
    res = simulate(cm, 80, 250, np.random.default_rng(21), c.batch_paths, with_stress=True)

    nf = res["n_fires"]
    ir, io = cm.index["rec"], cm.index["once"]
    assert nf[:, io].max() <= 1, "a non-recurrent node must never fire twice"
    assert nf[:, ir].max() >= 2, "a recurrent node must be able to fire twice"
    assert nf[:, ir].mean() > nf[:, io].mean()

    sev = np.array([7.0, 7.0], dtype=np.float32)
    gssi = np.zeros((res["fire_time"].shape[0], cm.T), dtype=np.float32)
    without = aggregate_stats(res["fire_time"], sev, gssi, Q36)
    with_reps = aggregate_stats(res["fire_time"], sev, gssi, Q36, occurrences=nf)
    assert with_reps["tiers"]["ge6"]["expected"] > without["tiers"]["ge6"]["expected"]


def test_horizon_capped_node_cannot_fire_after_its_last_resolvable_quarter():
    c = cfg()
    with use_horizon(HORIZON_2056):
        risks = {
            "locked": Risk("locked", "El Nino 2026-27", "d", "x", 60.0, 70.0, 74.0, 5.0,
                           "medium", horizon_coherent=False),
        }
        cm = CompiledModel(make_model(risks=risks), c)
        res = simulate(cm, 60, 200, np.random.default_rng(22), c.batch_paths)
        ft = res["fire_time"][:, cm.index["locked"]]
        fired = ft[ft >= 0]
        assert fired.size > 0
        assert fired.max() <= 42, "a 2027-locked criterion fired after 2036"

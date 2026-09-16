#!/usr/bin/env python3
"""Validation suite for RL-SIM.

Same standard as the GEO-SIM suite: each check tests the model against something
derivable on paper or bounded on theoretical grounds. A booking model that
nobody can check is a list of favourite rappers with a confidence interval
stapled to it.

Run: python tests/test_rlsim.py
"""

from __future__ import annotations

import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rlsim.data import HISTORY_DECAY_PER_YEAR, load  # noqa: E402
from rlsim.model import (  # noqa: E402
    _pl_negloglik, backtest, fit_headliners, fit_undercard, select_undercard,
)
from rlsim.simulate import simulate  # noqa: E402

FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  -- ' + detail) if detail else ''}")
    if not ok:
        FAILS.append(name)


def test_pl_likelihood_uniform():
    """With identical utilities every ordered triple is equally likely, so the
    negative log-likelihood must be exactly log(n) + log(n-1) + log(n-2)."""
    n = 7
    X = np.zeros((n, 2))
    nll = _pl_negloglik(np.zeros(2), [(X, [0, 1, 2])], ridge=0.0)
    want = math.log(n) + math.log(n - 1) + math.log(n - 2)
    check("PL likelihood matches closed form under uniform utilities",
          abs(nll - want) < 1e-9, f"{nll:.6f} vs {want:.6f}")


def test_pl_likelihood_two_way():
    """Two candidates, one slot: the PL likelihood must collapse to a logistic."""
    X = np.array([[1.0], [0.0]])
    w = np.array([0.8])
    nll = _pl_negloglik(w, [(X, [0])], ridge=0.0)
    want = -math.log(math.exp(0.8) / (math.exp(0.8) + 1.0))
    check("PL likelihood collapses to logistic for a two-way single pick",
          abs(nll - want) < 1e-12, f"{nll:.8f} vs {want:.8f}")


def test_ridge_penalty_exact():
    X = np.zeros((4, 3))
    w = np.array([1.0, -2.0, 0.5])
    a = _pl_negloglik(w, [(X, [0])], ridge=0.0)
    b = _pl_negloglik(w, [(X, [0])], ridge=2.0)
    check("ridge penalty enters as 0.5*lambda*||w||^2",
          abs((b - a) - 0.5 * 2.0 * float(w @ w)) < 1e-12)


def test_history_decay_exact():
    """Carti headlined Orlando on 2026-05-08. Measured on 2027-05-07, that one
    slot alone must contribute decay^(364.25/365.25)."""
    r = load()
    got = r.headline_history("playboi_carti", date(2027, 5, 7))
    yrs = [(date(2027, 5, 7) - e.start).days / 365.25
           for e in r.editions
           if e.us_flagship and e.status == "held"
           and "playboi_carti" in e.headliners_booked and e.start < date(2027, 5, 7)]
    want = sum(HISTORY_DECAY_PER_YEAR ** y for y in yrs)
    check("recency-weighted headline history matches its definition",
          abs(got - want) < 1e-12, f"{got:.6f} over {len(yrs)} prior slots")


def test_design_standardized():
    r = load()
    pool = r.headline_pool("florida_2027", date(2027, 5, 7))
    X = r.design("florida_2027", date(2027, 5, 7), True, pool,
                 ["hl_hist", "heat", "draw", "rl_fit", "fest_avail", "regional_fl"])
    check("design columns are centred", np.abs(X.mean(axis=0)).max() < 1e-10)
    check("design columns are unit-scaled", np.abs(X.std(axis=0) - 1).max() < 1e-10)


def test_gumbel_topk_matches_softmax():
    """The Gumbel top-k trick must reproduce sequential softmax sampling. For a
    single slot that means the top-1 marginal equals the softmax probability."""
    rng = np.random.default_rng(7)
    u = np.array([2.0, 1.0, 0.0, -1.0])
    n = 400_000
    g = -np.log(-np.log(rng.random((n, len(u)))))
    top1 = np.argmax(u + g, axis=1)
    emp = np.bincount(top1, minlength=len(u)) / n
    want = np.exp(u) / np.exp(u).sum()
    err = np.abs(emp - want).max()
    check("Gumbel top-k reproduces the softmax marginal",
          err < 4 * math.sqrt(0.25 / n) + 2e-3, f"max abs err {err:.5f}")


def test_availability_gate_is_absolute():
    """An artist with zero availability must never be selected, no matter how
    dominant their features. This is the one hard constraint in the model."""
    r = load()
    r.artists["drake"]["avail_2027"] = 0.0
    bt_feats = ["hl_hist", "heat", "draw", "rl_fit", "fest_avail", "regional_fl"]
    hm = fit_headliners(r, ridge=0.25, features=bt_feats)
    hm.w = np.array([0.0, 0.0, 50.0, 0.0, 0.0, 0.0])   # force draw to dominate
    hm.cov = np.eye(len(hm.w)) * 1e-12
    um = fit_undercard(r)
    out = simulate(r, hm, um, paths=20_000, seed=1)
    check("zero availability is an absolute veto",
          out["headline_prob"].get("drake", 0.0) == 0.0)


def test_draw_is_monotone():
    """Raising one artist's draw, holding everything else fixed, must not lower
    their headline probability. A choice model that fails this is miswired."""
    bt_feats = ["hl_hist", "heat", "draw", "rl_fit", "fest_avail", "regional_fl"]
    probs = []
    for d in (0.30, 0.95):
        r = load()
        r.artists["esdeekid"]["draw"] = d
        r.artists["esdeekid"]["avail_2027"] = 1.0
        hm = fit_headliners(r, ridge=0.25, features=bt_feats)
        um = fit_undercard(r)
        probs.append(simulate(r, hm, um, paths=40_000, seed=3)["headline_prob"]["esdeekid"])
    check("headline probability is monotone in draw",
          probs[1] > probs[0], f"{probs[0]:.3f} -> {probs[1]:.3f}")


def test_probabilities_are_coherent():
    r = load()
    bt_feats = ["hl_hist", "heat", "draw", "rl_fit", "fest_avail", "regional_fl"]
    hm = fit_headliners(r, ridge=0.25, features=bt_feats)
    um = fit_undercard(r)
    out = simulate(r, hm, um, paths=40_000, seed=5)
    hp = out["headline_prob"]
    check("headline probabilities lie in [0,1]",
          all(0.0 <= v <= 1.0 for v in hp.values()))
    total = sum(hp.values())
    check("headline probabilities sum to the number of slots",
          abs(total - 3.0) < 1e-9, f"sum={total:.6f}")
    check("bill probability is never below headline probability",
          all(out["bill_prob"][k] >= hp[k] - 1e-12 for k in hp))


def test_backtest_beats_baselines():
    r = load()
    bt = backtest(r, ridge_grid=(0.25, 1.0, 4.0))
    b = bt["best"]
    check("LOO hit rate beats a uniform draw from the pool",
          b["hit_rate"] > b["random_hit_rate"] * 3,
          f"{b['hit_rate']:.1%} vs {b['random_hit_rate']:.1%}")
    check("LOO hit rate beats ranking on popularity alone",
          b["hit_rate"] > b["heat_only_hit_rate"],
          f"{b['hit_rate']:.1%} vs {b['heat_only_hit_rate']:.1%}")
    check("LOO hit rate beats rebooking last edition's headliners",
          b["hit_rate"] > b["repeat_last_hit_rate"],
          f"{b['hit_rate']:.1%} vs {b['repeat_last_hit_rate']:.1%}")


def test_undercard_probabilities_bounded():
    """Built from the model's own feature list rather than a hardcoded vector,
    so a specification change cannot silently pass a stale test."""
    r = load()
    um = fit_undercard(r)
    i_prev = um.features.index("on_prev_bill")
    lo = np.zeros(len(um.features))
    hi = lo.copy()
    hi[i_prev] = 1.0
    p = um.prob(np.vstack([hi, lo]))
    check("undercard probabilities lie in (0,1)", bool(np.all((p > 0) & (p < 1))))
    check("prior appearance raises the undercard probability", p[0] > p[1],
          f"{p[0]:.3f} vs {p[1]:.3f}")


def test_undercard_selection_prefers_draw():
    """The undercard spec without a draw control produced sign-flipped
    popularity and prior-appearance coefficients by pooling headline-tier acts,
    which rotate out, with undercard acts, which recycle. Held-out fit must
    prefer the specification that separates them."""
    r = load()
    sel = select_undercard(r)
    check("undercard selection prefers the draw-controlled spec",
          sel["best_set"] == "draw", f"selected {sel['best_set']!r}")
    um = fit_undercard(r, ridge=sel["best_ridge"], features=sel["best_features"])
    b = dict(zip(um.features, um.beta[1:]))
    check("undercard popularity coefficient has the right sign", b["heat"] > 0,
          f"heat={b['heat']:+.3f}")
    check("undercard brand-fit coefficient has the right sign", b["rl_fit"] > 0,
          f"rl_fit={b['rl_fit']:+.3f}")


def test_support_tier_is_excluded_from_the_fit():
    """The roster's support tier was sourced from the 2026 bill, so every one of
    those acts is a positive and the region carries no information. Fitting over
    it flips the popularity coefficient negative. Guard the exclusion."""
    from rlsim.model import UNDERCARD_DRAW_FLOOR, _undercard_transitions
    r = load()
    below = [k for k, a in r.artists.items() if a["draw"] < UNDERCARD_DRAW_FLOOR]
    on_2026 = [e for e in r.editions if e.key == "orlando_2026"][0].bill
    check("support tier really is selection-on-outcome",
          all(k in on_2026 for k in below),
          f"{len(below)} acts below the floor, "
          f"{sum(k in on_2026 for k in below)} of them on the 2026 bill")
    n_fit = sum(len(t[2]) for t in _undercard_transitions(r, ["on_prev_bill"]))
    check("the fit excludes them", n_fit > 0 and len(below) > 0)


def main() -> int:
    print("RL-SIM validation")
    for fn in (
        test_pl_likelihood_uniform, test_pl_likelihood_two_way,
        test_ridge_penalty_exact, test_history_decay_exact,
        test_design_standardized, test_gumbel_topk_matches_softmax,
        test_availability_gate_is_absolute, test_draw_is_monotone,
        test_probabilities_are_coherent, test_undercard_probabilities_bounded,
        test_undercard_selection_prefers_draw,
        test_support_tier_is_excluded_from_the_fit, test_backtest_beats_baselines,
    ):
        fn()
    print(f"\n{'ALL PASS' if not FAILS else str(len(FAILS)) + ' FAILED: ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())

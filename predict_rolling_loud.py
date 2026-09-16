#!/usr/bin/env python3
"""Fit RL-SIM and forecast Rolling Loud Florida 2027.

    python predict_rolling_loud.py --paths 200000 --out results_rl

Fits the headline choice model and the undercard persistence model to the six US
flagship editions Rolling Loud has staged since 2023, backtests the headline
model leave-one-edition-out against three baselines, then integrates forward to
7-9 May 2027 over coefficient uncertainty and per-artist availability.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import numpy as np

from rlsim.data import FEATURE_NAMES, load
from rlsim.model import (
    backtest, fit_headliners, fit_undercard, select_undercard,
)
from rlsim.simulate import simulate

ROOT = Path(__file__).parent

# Probability the edition is staged at all. Not fitted -- the reference class is
# three attrition events (Miami 2025 never staged, California 2026 dropped,
# Australia 2026 cancelled after its full lineup was announced) against seven
# editions held since 2023, which is far too thin to regress. Judgement,
# weighted toward this specific franchise: Orlando 2026 sold out all three days
# at ~65k/day, the 2027 dates are announced with a live on-sale, and the venue
# and municipal relationship are in place. The residual risk is mostly the
# generic one that killed Australia -- a promoter-side funding failure.
P_STAGED = 0.93


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", type=int, default=200_000)
    ap.add_argument("--out", default="results_rl")
    ap.add_argument("--seed", type=int, default=20270507)
    args = ap.parse_args()

    roster = load()
    bt = backtest(roster)
    ridge, feats = bt["best_ridge"], bt["best_features"]
    hm = fit_headliners(roster, ridge=ridge, features=feats)
    usel = select_undercard(roster)
    um = fit_undercard(roster, ridge=usel["best_ridge"],
                       features=usel["best_features"])

    sim = simulate(roster, hm, um, target_key="florida_2027",
                   target_date=date(2027, 5, 7), is_florida=True,
                   n_slots=3, paths=args.paths, seed=args.seed)

    name = {k: a["name"] for k, a in roster.artists.items()}

    print("=" * 72)
    print("RL-SIM  ::  Rolling Loud Florida 2027, Camping World Stadium, 7-9 May")
    print("=" * 72)

    print(f"\nBACKTEST (leave-one-edition-out, {bt['best']['slots']} headline slots)")
    print(f"  {'feature set':11s} {'ridge':>6s} {'hit':>7s} {'LOO loglik':>11s}")
    for n, v in sorted(bt["by_feature_set"].items(),
                       key=lambda kv: -kv[1]["loo_loglik"]):
        mark = "  <- selected" if n == bt["best_feature_set"] else ""
        print(f"  {n:11s} {v['ridge']:6.2f} {v['hit_rate']:7.1%} "
              f"{v['loo_loglik']:11.2f}{mark}")
    b = bt["best"]
    print()
    print(f"  RL-SIM top-3 hit rate                   : {b['hit_rate']:.1%}")
    print(f"  baseline, popularity rank only          : {b['heat_only_hit_rate']:.1%}")
    print(f"  baseline, rebook last edition           : {b['repeat_last_hit_rate']:.1%}")
    print(f"  baseline, uniform draw from pool        : {b['random_hit_rate']:.1%}")

    print("\nFITTED HEADLINE COEFFICIENTS (standardized within pool)")
    for n, w, s in zip(hm.features, hm.w, (hm.cov.diagonal() ** 0.5)):
        print(f"  {n:14s} {w:+.3f}  (sd {s:.3f})")

    print(f"\nFITTED UNDERCARD COEFFICIENTS "
          f"(spec '{usel['best_set']}' selected leave-one-transition-out)")
    print(f"  {'intercept':14s} {um.beta[0]:+.3f}")
    for n, b_ in zip(um.features, um.beta[1:]):
        print(f"  {n:14s} {b_:+.3f}")
    print(f"  observed reported-bill return rate: {um.base_return_rate:.1%} (lower bound)")

    print(f"\nP(edition staged as announced) = {P_STAGED:.0%}")
    print("All probabilities below are CONDITIONAL on it being staged.\n")

    print(f"HEADLINE PROBABILITIES  ({sim['paths']:,} paths, +/- 2 MC se)")
    hp = sorted(sim["headline_prob"].items(), key=lambda kv: -kv[1])
    for k, p in hp:
        if p < 0.01:
            continue
        se = sim["headline_se"][k]
        print(f"  {name[k]:28s} {p:6.1%}  +/-{2*se:5.1%}"
              f"   [uncond {p*P_STAGED:5.1%}]")

    # --- calibration check against the raw repeat base rate -------------------
    prev = max((e for e in roster.editions
                if e.us_flagship and e.status == "held"), key=lambda e: e.start)
    prev_hl = set(prev.headliners_booked) | set(prev.headliners_performed)
    exp_return = sum(sim["headline_prob"].get(k, 0.0) for k in prev_hl)

    staged = sorted((e for e in roster.editions
                     if e.us_flagship and e.status == "held"), key=lambda e: e.start)
    rep_num = rep_den = 0
    for a, b in zip(staged, staged[1:]):
        rep_den += len(b.headliners_booked)
        rep_num += len(set(b.headliners_booked) & set(a.headliners_booked))

    print("\nCALIBRATION CHECK -- how much does this festival actually rotate?")
    print(f"  historical: {rep_num}/{rep_den} headline slots went to someone who "
          f"headlined the\n              immediately preceding edition = "
          f"{rep_num/rep_den:.1%} of slots")
    print(f"  model     : {exp_return:.2f} of 3 slots expected to go to a 2026 "
          f"headliner = {exp_return/3:.1%}")
    if exp_return / 3 > rep_num / rep_den:
        print("  -> the model is MORE repeat-friendly than the raw base rate. That is "
              "driven by\n     Don Toliver's popularity, and it is the single number "
              "here most likely to be too high.")

    # --- sensitivity: how hard does Rolling Loud rotate its headliners? -------
    print("\nSENSITIVITY TO THE ROTATION EFFECT (hl_hist coefficient)")
    print("  The fitted value says incumbency HURTS. Because that one coefficient")
    print("  decides whether last year's headliners come back, it is worth seeing the")
    print("  slate under a weaker and a stronger rotation prior.")
    i_hist = hm.features.index("hl_hist")
    fitted = hm.w[i_hist]
    for label, val in (("none      (0.0)", 0.0),
                       (f"fitted ({fitted:+.2f})", fitted),
                       ("strong    (-1.5)", -1.5)):
        import copy
        hm2 = copy.deepcopy(hm)
        hm2.w = hm.w.copy()
        hm2.w[i_hist] = val
        hm2.cov = hm.cov * 0.25   # hold coefficients near the point for a clean read
        s2 = simulate(roster, hm2, um, target_key="florida_2027",
                      target_date=date(2027, 5, 7), is_florida=True,
                      n_slots=3, paths=40_000, seed=args.seed + 1)
        top = sorted(s2["headline_prob"].items(), key=lambda kv: -kv[1])[:5]
        print(f"  {label:18s} " + ",  ".join(f"{name[k]} {p:.0%}" for k, p in top))

    print("\nMOST LIKELY THREE-NAME SLATES")
    for slate, p in sim["slates"][:10]:
        print(f"  {p:6.2%}  " + " / ".join(sorted(name[k] for k in slate)))

    print("\nBILL PROBABILITIES, ANYWHERE ON THE LINEUP (top 45)")
    bp = sorted(sim["bill_prob"].items(), key=lambda kv: -kv[1])[:45]
    for k, p in bp:
        print(f"  {name[k]:28s} {p:6.1%}")

    out = ROOT / args.out
    out.mkdir(exist_ok=True)
    (out / "rl2027.json").write_text(json.dumps({
        "target": "Rolling Loud Florida 2027, Camping World Stadium, 7-9 May 2027",
        "generated_from_information_as_of": "2026-09-16",
        "p_staged": P_STAGED,
        "backtest": bt,
        "selected_feature_set": bt["best_feature_set"],
        "headline_coefficients": dict(zip(hm.features, hm.w.tolist())),
        "headline_coefficient_sd": dict(zip(hm.features,
                                            (hm.cov.diagonal() ** 0.5).tolist())),
        "selected_undercard_spec": usel["best_set"],
        "undercard_selection": usel["grid"],
        "undercard_coefficients": dict(
            zip(["intercept"] + list(um.features), um.beta.tolist())),
        "undercard_observed_return_rate": um.base_return_rate,
        "headline_prob": {name[k]: v for k, v in sim["headline_prob"].items()},
        "headline_se": {name[k]: v for k, v in sim["headline_se"].items()},
        "bill_prob": {name[k]: v for k, v in sim["bill_prob"].items()},
        "top_slates": [[sorted(name[k] for k in s), p] for s, p in sim["slates"]],
        "repeat_base_rate_historical": rep_num / rep_den,
        "repeat_expected_slots_model": exp_return,
    }, indent=2))
    print(f"\nwrote {out / 'rl2027.json'}")


if __name__ == "__main__":
    main()

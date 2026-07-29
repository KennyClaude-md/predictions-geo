#!/usr/bin/env python3
"""Drive a full GEO-SIM run and write every artifact the report needs.

    python run_simulation.py --paths 200000 --out results

Two runs happen. The decoupled run holds each domain in isolation and is used
both to calibrate hazards against the analysts' elicited priors and as the
counterfactual against which systemic amplification is measured. The coupled
run turns on cross-domain transmission, contagion, regimes and stabilizing
feedbacks, and is the one that produces the headline numbers.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from geosim import Simulator, load
from geosim import analysis as an

ROOT = Path(__file__).parent

# Events severe enough that a decade containing several of them is a decade
# people will name. Used for the systemic-clustering metrics.
SEVERE = [
    "taiwan_blockade_or_quarantine", "taiwan_invasion", "us_china_direct_armed_clash",
    "nato_russia_direct_clash", "article5_invocation", "korea_major_conflict",
    "iran_nuclear_breakout", "iran_nuclear_test", "new_nuclear_weapons_state",
    "hormuz_disruption_30d", "global_recession", "major_sovereign_default_g20",
    "global_equity_drawdown_40pct", "dollar_confidence_crisis", "china_financial_crisis",
    "pandemic_1m_deaths", "pandemic_10m_deaths", "ai_enabled_cyber_catastrophe",
    "ai_enabled_bio_incident", "ai_driven_labor_shock", "major_state_collapse",
    "civil_war_onset_major_state", "interstate_battle_deaths_100k_year",
    "single_year_disaster_loss_500bn", "critical_mineral_embargo", "oil_above_150_sustained",
    "major_famine_declaration", "amoc_collapse_signal", "loss_of_control_incident",
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", type=int, default=200_000)
    ap.add_argument("--chunk", type=int, default=10_000)
    ap.add_argument("--record", type=int, default=6_000)
    ap.add_argument("--horizon", type=float, default=10.5)
    ap.add_argument("--seed", type=int, default=20260729)
    ap.add_argument("--params", type=str, default="params")
    ap.add_argument("--out", type=str, default="results")
    args = ap.parse_args()

    pdir = ROOT / args.params
    odir = ROOT / args.out
    odir.mkdir(parents=True, exist_ok=True)

    domain_files = sorted(pdir.glob("domain_*.json"))
    if not domain_files:
        raise SystemExit(f"no domain_*.json found in {pdir}")

    t0 = time.time()
    print(f"Loading {len(domain_files)} domain parameter sets...")
    P = load(domain_files, pdir / "coupling.json")
    print(
        f"  {len(P.indicators)} indicators, {len(P.events)} events, "
        f"{len(P.couplings)} couplings, {len(P.contagions)} contagion rules, "
        f"{len(P.stabilizers)} stabilizers, {len(P.regimes)} regimes"
    )
    if P.aliases:
        weak = sorted(P.aliases.items(), key=lambda kv: kv[1]["score"])
        print(f"  {len(P.aliases)} cross-references resolved by name matching "
              f"(review the low scores):")
        for ref, a in weak:
            print(f"    {a['score']:.2f}  {ref}  ->  {a['to']}")
    if P.dropped:
        print(f"  {len(P.dropped)} parameter references dropped (unresolved keys)")
        for d in P.dropped[:15]:
            print(f"    - {d}")

    sim = Simulator(P, horizon_years=args.horizon, seed=args.seed)

    print("\nCalibrating hazards against elicited priors (decoupled baseline)...")
    targets = sim.calibrate(n=max(args.paths // 4, 40_000), iters=4)

    print(f"\nDecoupled run ({args.paths:,} paths)...")
    dec = sim.run(n_paths=args.paths, chunk=args.chunk, coupled=False, record_paths=0)

    print(f"\nCoupled run ({args.paths:,} paths)...")
    cou = sim.run(n_paths=args.paths, chunk=args.chunk, coupled=True, record_paths=args.record)

    print("\nAnalysing...")
    events = an.event_table(P, cou, dec)
    severe_present = [e for e in SEVERE if e in P.ekey]

    headline = sorted(events, key=lambda r: -r["p_2036"])
    focus = [e["id"] for e in headline if e["id"] in severe_present][:22]

    out = {
        "meta": {
            "version": "1.0.0",
            "epoch": "2026-07-29",
            "horizon_years": args.horizon,
            "quarters": sim.T,
            "paths": int(args.paths),
            "seed": args.seed,
            "n_indicators": len(P.indicators),
            "n_events": len(P.events),
            "n_couplings": len(P.couplings),
            "n_contagion_rules": len(P.contagions),
            "n_stabilizers": len(P.stabilizers),
            "runtime_seconds": None,
            "dropped_references": P.dropped,
            "resolved_aliases": P.aliases,
        },
        "events": events,
        "calibration": [
            {
                "id": ev.id,
                "target_p2036": float(targets[j]),
                "fitted_offset_log_hazard": float(P.calib_offset[j]),
                "prior_hazard_annual": float(ev.prior_hazard),
                "effective_hazard_annual": float(ev.prior_hazard * np.exp(P.calib_offset[j])),
            }
            for j, ev in enumerate(P.events)
        ],
        "regimes": an.regime_summary(P, cou),
        "systemic": an.systemic_metrics(P, cou, severe_present),
        "conditional": an.conditional_matrix(P, cou, focus),
        "scenarios": an.scenario_clusters(P, cou, k=6),
        "sensitivity": an.sensitivity(P, cou, severe_present),
        "indicators_terminal": an.indicator_terminal(P, cou),
        "timelines": an.event_timelines(P, cou),
    }
    out["meta"]["runtime_seconds"] = round(time.time() - t0, 1)

    fans = an.indicator_fans(P, cou["traj"])

    (odir / "results.json").write_text(json.dumps(out, indent=1))
    (odir / "fans.json").write_text(json.dumps(fans))
    np.savez_compressed(
        odir / "raw.npz",
        fire_q=cou["fire_q"].astype(np.int16),
        fired=cou["fired"],
        x_final=cou["x_final"].astype(np.float32),
        regime_time=cou["regime_time"].astype(np.float32),
        event_ids=np.array([e.id for e in P.events]),
        indicator_keys=np.array([i.key for i in P.indicators]),
    )

    print(f"\nDone in {out['meta']['runtime_seconds']}s -> {odir}/")
    print("\nTop 20 by P(by 2036):")
    for r in headline[:20]:
        amp = r["amplification"]
        print(
            f"  {r['p_2036'] * 100:5.1f}%  (+-{r['se_2036'] * 196:.1f})  "
            f"[iso {r['p_indep_2036'] * 100:4.1f}%, amp {amp:4.2f}x]  {r['id']}"
        )

    s = out["systemic"]
    print(
        f"\nSevere-shock count by 2036: mean {s['mean_count']:.2f}, "
        f"P(>=2)={s['p_at_least_2']:.3f} (indep {s['independent_p_at_least_2']:.3f}), "
        f"P(>=4)={s['p_at_least_4']:.3f}"
    )


if __name__ == "__main__":
    main()

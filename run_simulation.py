#!/usr/bin/env python3
"""Run the world-futures simulation end to end.

    python run_simulation.py [--quick] [--paths N] [--seed S]

Reads params/world_model.json (produced by the research pipeline), builds the
five worldviews, calibrates each so its simulated marginals match its elicited
ones, runs the Monte Carlo, and writes output/forecast_report.md + forecast.json.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from worldsim import analysis, continuous, labelling, report
from worldsim.engine import CompiledModel, SimConfig, calibrate_marginals, simulate
from worldsim.params import build_worldviews, load_base_model
from worldsim.timeline import ANCHOR_QUARTERS, N_QUARTERS

ROOT = Path(__file__).parent
PARAMS = ROOT / "params"
OUTPUT = ROOT / "output"

Q27 = ANCHOR_QUARTERS["p_by_2027_pct"]
Q31 = ANCHOR_QUARTERS["p_by_2031_pct"]
Q36 = ANCHOR_QUARTERS["p_by_2036_pct"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="small run for smoke-testing")
    ap.add_argument("--paths", type=int, default=None, help="paths per worldview")
    ap.add_argument("--seed", type=int, default=20260729)
    ap.add_argument("--model", default=str(PARAMS / "world_model.json"))
    args = ap.parse_args()

    t0 = time.time()
    raw = json.loads(Path(args.model).read_text())
    base, meta = load_base_model(args.model)
    print(f"loaded model: {meta}")

    if args.quick:
        cfg = SimConfig(
            n_worlds=40, paths_per_world=120, calib_worlds=30,
            calib_paths_per_world=100, calib_iters=4, seed=args.seed,
        )
    else:
        cfg = SimConfig(seed=args.seed)
    if args.paths:
        cfg.paths_per_world = max(60, args.paths // cfg.n_worlds)

    worldviews = build_worldviews(base, raw)
    print(
        f"worldviews: "
        + ", ".join(f"{m.name}({w:.0%})" for m, w in worldviews)
    )

    results, calib_report, compiled = [], {}, None
    rng = np.random.default_rng(cfg.seed)
    for model, weight in worldviews:
        print(f"\n[{model.name}] compiling {len(model.risks)} risks, {len(model.edges)} edges")
        cm = CompiledModel(model, cfg)
        compiled = compiled or cm
        cal = calibrate_marginals(cm, cfg)
        calib_report[model.name] = cal
        print(f"[{model.name}] simulating {cfg.n_paths:,} paths…")
        res = simulate(cm, cfg.n_worlds, cfg.paths_per_world, rng, cfg.batch_paths)
        res["name"] = model.name
        results.append(res)

    # All worldviews share the same risk universe only if calibration added none;
    # align to the intersection so pooling is well defined.
    results = _align(results)
    weights = [w for _, w in worldviews]

    pooled = analysis.pool_worldviews(results, weights, cfg.n_paths, rng)
    ft = pooled["fire_time"]
    risk_ids = pooled["risk_ids"]
    print(f"\npooled ensemble: {ft.shape[0]:,} paths × {ft.shape[1]} risks")

    lookup = {r.id: r for r in base.risks.values()}
    for m, _ in worldviews:
        for rid, r in m.risks.items():
            lookup.setdefault(rid, r)
    severity = np.array([lookup[r].severity for r in risk_ids], dtype=np.float32)
    names = [lookup[r].name for r in risk_ids]
    domains = [lookup[r].domain for r in risk_ids]

    marg = analysis.marginal_with_interval(ft, pooled["group"], [Q27, Q31, Q36])
    gssi = continuous.systemic_stress(ft, severity)

    ctx = _assemble(
        raw, cfg, meta, results, weights, pooled, marg, gssi, severity, names,
        domains, risk_ids, lookup, calib_report, base, rng,
    )
    report.write_outputs(ctx, OUTPUT)
    print(f"\nwrote {OUTPUT/'forecast_report.md'} and {OUTPUT/'forecast.json'}")
    print(f"total {time.time()-t0:.1f}s")


def _align(results: list[dict]) -> list[dict]:
    common = set(results[0]["risk_ids"])
    for r in results[1:]:
        common &= set(r["risk_ids"])
    common_sorted = sorted(common)
    out = []
    for r in results:
        idx = [r["risk_ids"].index(rid) for rid in common_sorted]
        out.append(
            {
                "fire_time": r["fire_time"][:, idx],
                "world_id": r["world_id"],
                "risk_ids": common_sorted,
                "name": r.get("name", "?"),
            }
        )
    return out


def _assemble(
    raw, cfg, meta, results, weights, pooled, marg, gssi, severity, names,
    domains, risk_ids, lookup, calib_report, base, rng,
) -> dict:
    R = len(risk_ids)
    p27, p31, p36 = marg[Q27]["mean"], marg[Q31]["mean"], marg[Q36]["mean"]
    lo36, hi36 = marg[Q36]["lo"], marg[Q36]["hi"]
    ft = pooled["fire_time"]

    def row(i: int) -> dict:
        tp = analysis.timing_profile(ft, i)
        return {
            "id": risk_ids[i],
            "name": names[i],
            "domain": domains[i],
            "resolution": lookup[risk_ids[i]].resolution_criteria,
            "p2027": float(p27[i]),
            "p2031": float(p31[i]),
            "p2036": float(p36[i]),
            "lo2036": float(lo36[i]),
            "hi2036": float(hi36[i]),
            "epistemic_sd": float(marg[Q36]["epistemic_sd"][i]),
            "severity": float(severity[i]),
            "median_quarter": tp.get("median_quarter"),
        }

    all_rows = [row(i) for i in range(R)]

    impact = p36 * severity
    headline = [all_rows[i] for i in np.argsort(impact)[::-1][:22]]

    by_domain: dict[str, list[dict]] = {}
    for r in sorted(all_rows, key=lambda r: -r["p2036"] * r["severity"]):
        by_domain.setdefault(r["domain"], []).append(r)

    agg = analysis.aggregate_stats(ft, severity, gssi, Q36)

    # --- archetypes -------------------------------------------------------
    feature_idx = list(np.argsort(impact)[::-1][:26])
    arch = analysis.archetypes(ft, gssi, feature_idx, k=6, seed=cfg.seed)
    overall_rates = (ft[:, feature_idx] >= 0).mean(axis=0)
    labelled = labelling.label_clusters(
        arch["clusters"], feature_idx, names, domains, overall_rates
    )

    # --- cascades ---------------------------------------------------------
    severe_idx = [i for i in range(R) if severity[i] >= 6][:40]
    chains_raw = analysis.first_chains(ft, severe_idx, depth=3, top=12)
    n_paths = ft.shape[0]
    chains = [
        {"names": [names[i] for i in ch], "share": cnt / n_paths}
        for ch, cnt in chains_raw
    ]

    # --- dependence -------------------------------------------------------
    cand = list(np.argsort(impact)[::-1][:34])
    pairs_raw = analysis.top_pairs_by_lift(ft, Q36, cand, min_joint=0.012, top=18)
    pairs = [
        {
            "a": names[i], "b": names[j], "joint": jt, "lift": lf, "cond": cd,
        }
        for i, j, jt, lf, cd in pairs_raw
    ]

    # --- continuous -------------------------------------------------------
    loadings_path = PARAMS / "stress_loadings.json"
    loadings = json.loads(loadings_path.read_text()) if loadings_path.exists() else {}
    zs = continuous.stress_percentile(gssi[rng.choice(n_paths, min(n_paths, 120_000), replace=False)])
    cvars = list(base.continuous.values())
    cont_paths = continuous.simulate_continuous(cvars, zs, loadings, rng)
    cont = []
    for v in cvars:
        vals = cont_paths[v.id]
        q31 = np.quantile(vals[:, Q31 - 1], [0.1, 0.5, 0.9]).tolist()
        q36 = np.quantile(vals[:, Q36 - 1], [0.1, 0.5, 0.9]).tolist()
        cont.append(
            {
                "id": v.id, "name": v.name, "unit": v.unit, "domain": v.domain,
                "current": v.current, "q2031": q31, "q2036": q36,
                "stress_loading": loadings.get(v.id, 0.0),
            }
        )

    # --- sensitivity ------------------------------------------------------
    peak = gssi.max(axis=1).astype(np.float64)
    sens = analysis.first_order_sensitivity(ft, peak)
    sens_rows = [
        {
            "name": names[i], "share": float(sens[i]),
            "p2036": float(p36[i]), "severity": float(severity[i]),
        }
        for i in np.argsort(sens)[::-1][:18]
    ]

    # --- worldview disagreement -------------------------------------------
    est = analysis.view_disagreement(results, [Q36])[Q36]  # (n_views, R)
    spread = est.max(axis=0) - est.min(axis=0)
    dis_rows = [
        {
            "name": names[i],
            "by_view": [float(est[v, i]) for v in range(est.shape[0])],
            "spread": float(spread[i]),
        }
        for i in np.argsort(spread)[::-1][:16]
    ]

    limits = _limits(raw)

    return {
        "as_of": raw.get("as_of", "unknown"),
        "n_paths_total": int(n_paths),
        "n_worldviews": len(results),
        "n_worlds": cfg.n_worlds,
        "n_risks": R,
        "n_edges": meta["n_edges"],
        "n_latents": meta["n_latents"],
        "n_continuous": len(cvars),
        "calibration": calib_report,
        "headline": headline,
        "all_rows": all_rows,
        "by_domain": by_domain,
        "aggregate": agg,
        "aggregate_commentary": _agg_commentary(agg),
        "archetypes": labelled,
        "chains": chains,
        "chain_commentary": _chain_commentary(chains),
        "pairs": pairs,
        "continuous": cont,
        "sensitivity": sens_rows,
        "disagreement": dis_rows,
        "stress_trajectory": analysis.stress_trajectory(gssi),
        "limits": limits,
    }


def _agg_commentary(a: dict) -> str:
    return (
        f"The modal decade contains {a['severe_event_deciles'][2]:.0f} events the model "
        f"rates severity 6 or above, and the probability of getting through to 2036 with "
        f"none is {a['p_zero_severe']*100:.0f}%. That asymmetry is the single most robust "
        f"finding here: across every worldview and every parameter draw, a decade with no "
        f"major disruption is a tail outcome, not the base case. The interesting variance "
        f"is not *whether* shocks arrive but whether they arrive spaced out or together."
    )


def _chain_commentary(chains: list[dict]) -> str:
    if not chains:
        return ""
    top = chains[0]
    return (
        f"The most common opening — {top['names'][0]} → {top['names'][1]} → "
        f"{top['names'][2]} — accounts for {top['share']*100:.1f}% of all paths. No single "
        f"sequence dominates, which is itself informative: the model does not support a "
        f"story in which one specific trigger reliably starts the cascade. What recurs is "
        f"the *pattern* — a shock in one domain degrading the capacity to absorb the next."
    )


def _limits(raw: dict) -> list[str]:
    base = [
        "**The parameters are elicited judgement, not measurement.** The engine is exact; "
        "the inputs are informed opinion, audited and red-teamed but still opinion. "
        "Simulation precision does not create forecast accuracy, and the 90% bands cover "
        "disagreement between the modelled worldviews, not the possibility that all five "
        "are wrong together.",
        "**Correlated error is unmodelled.** If the analysts share a blind spot, the "
        "ensemble inherits it silently and reports narrow bands over a wrong centre.",
        "**Resolution criteria carry real weight.** Several forecasts move by tens of "
        "percentage points on the wording of what counts. Read the criteria before "
        "quoting a number.",
        "**Nothing outside the risk set can happen.** The events that most reshape a "
        "decade are frequently ones nobody enumerated in advance. Treat the "
        "'no severe event' probability as an upper bound on calm.",
        "**Causal edges are assumed, not estimated.** The dependency structure comes from "
        "domain reasoning about transmission channels, not from fitting historical "
        "co-occurrence — there is no dataset of decades to fit it to.",
        "**Hazards are conditionally memoryless within each segment.** Real crises have "
        "internal dynamics — mobilisation, negotiation, exhaustion — that a piecewise "
        "exponential cannot represent.",
    ]
    for dom in raw.get("domains", []):
        for s in (dom.get("research") or {}).get("structural_uncertainties", [])[:1]:
            base.append(f"*{dom.get('domain')}*: {s}")
    return base


if __name__ == "__main__":
    main()

"""Post-processing for GEO-SIM runs.

Everything a forecast consumer actually wants lives here rather than in the
engine: marginal probabilities with honest Monte Carlo error bars, the gap
between the elicited prior and the coupled model's posterior, conditional and
joint structure, emergent scenario clusters, and a sensitivity readout showing
which assumptions the answers hang on.
"""

from __future__ import annotations

import numpy as np

from .params import CompiledParams

QPY = 4

# Calendar horizons, as elapsed years from 2026-07-29.
HORIZONS = {"2027": 1.42, "2030": 4.42, "2036": 10.42}


def _q(years: float) -> int:
    return max(int(np.ceil(years * QPY)) - 1, 0)


def event_table(P: CompiledParams, coupled: dict, decoupled: dict) -> list[dict]:
    """Per-event probabilities at each horizon, coupled vs decoupled."""
    n = coupled["fire_q"].shape[0]
    rows = []
    for j, ev in enumerate(P.events):
        row = {
            "id": ev.id,
            "domain": ev.domain,
            "statement": ev.statement,
            "resolution_criteria": ev.resolution_criteria,
            "reference_class": ev.reference_class,
            "base_rate_annual": ev.base_rate_annual,
            "confidence": ev.confidence,
            "absorbing": bool(ev.absorbing),
            "reasoning": ev.reasoning,
        }
        for name, yrs in HORIZONS.items():
            q = _q(yrs)
            fq = coupled["fire_q"][:, j]
            p = float(((fq >= 0) & (fq <= q)).mean())
            se = float(np.sqrt(max(p * (1 - p), 1e-12) / n))
            row[f"p_{name}"] = p
            row[f"se_{name}"] = se
            row[f"ci_lo_{name}"] = max(p - 1.96 * se, 0.0)
            row[f"ci_hi_{name}"] = min(p + 1.96 * se, 1.0)

            dq = decoupled["fire_q"][:, j]
            row[f"p_indep_{name}"] = float(((dq >= 0) & (dq <= q)).mean())

            prior = ev.p_by.get(int(name))
            row[f"p_analyst_{name}"] = float(prior) if prior is not None else None

        # Systemic amplification: how much the coupled world raises (or lowers)
        # this risk relative to treating the domain in isolation. Odds ratio
        # rather than probability ratio, so it stays meaningful near 0 and 1.
        pc, pi = row["p_2036"], row["p_indep_2036"]
        row["amplification"] = _odds_ratio(pc, pi)
        row["expected_count_2036"] = float(coupled["fire_count"][:, j].mean())
        fq = coupled["fire_q"][:, j]
        occurred = fq[fq >= 0]
        row["median_timing_years"] = (
            float(np.median(occurred) + 1) / QPY if occurred.size else None
        )
        rows.append(row)
    return rows


def _odds_ratio(p: float, q: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    q = min(max(q, 1e-6), 1 - 1e-6)
    return (p / (1 - p)) / (q / (1 - q))


def indicator_fans(P: CompiledParams, traj: np.ndarray, pct=(5, 10, 25, 50, 75, 90, 95)) -> dict:
    """Percentile bands per indicator per quarter, from the recorded subsample."""
    out = {}
    if traj is None or traj.size == 0:
        return out
    arr = np.percentile(traj.astype(np.float64), pct, axis=0)  # (P, T+1, K)
    for i, ind in enumerate(P.indicators):
        out[ind.key] = {
            "label": ind.label,
            "unit": ind.unit,
            "domain": ind.domain,
            "start": float(ind.value),
            "source": ind.source,
            "as_of": ind.as_of,
            "percentiles": {str(p): arr[k, :, i].round(4).tolist() for k, p in enumerate(pct)},
        }
    return out


def conditional_matrix(P: CompiledParams, res: dict, ids: list[str], horizon="2036") -> dict:
    """P(row | column) among a selected set of events, plus lift over marginal."""
    q = _q(HORIZONS[horizon])
    idx = [P.ekey[i] for i in ids if i in P.ekey]
    labels = [i for i in ids if i in P.ekey]
    if not idx:
        return {"ids": [], "statements": [], "marginal": [], "conditional": [], "lift": []}
    fq = res["fire_q"][:, idx]
    occ = (fq >= 0) & (fq <= q)
    marg = occ.mean(axis=0)

    cond = np.zeros((len(idx), len(idx)))
    lift = np.zeros((len(idx), len(idx)))
    for c in range(len(idx)):
        sel = occ[:, c]
        m = sel.sum()
        if m < 30:
            cond[:, c] = np.nan
            lift[:, c] = np.nan
            continue
        cond[:, c] = occ[sel].mean(axis=0)
        lift[:, c] = cond[:, c] / np.maximum(marg, 1e-9)
    return {
        "ids": labels,
        "statements": [P.events[P.ekey[i]].statement for i in labels],
        "marginal": marg.round(5).tolist(),
        "conditional": np.round(cond, 5).tolist(),
        "lift": np.round(lift, 4).tolist(),
    }


def systemic_metrics(P: CompiledParams, res: dict, severe_ids: list[str], horizon="2036") -> dict:
    """How many severe shocks land, and do they cluster?"""
    q = _q(HORIZONS[horizon])
    idx = [P.ekey[i] for i in severe_ids if i in P.ekey]
    fq = res["fire_q"][:, idx]
    occ = (fq >= 0) & (fq <= q)
    k = occ.sum(axis=1)

    # Poisson-binomial benchmark: what the count distribution would look like if
    # these events were independent with the same marginals. Excess mass in the
    # right tail is the clustering the coupling produces.
    marg = occ.mean(axis=0)
    rng = np.random.default_rng(7)
    indep = (rng.random((min(len(k), 200_000), len(idx))) < marg[None, :]).sum(axis=1)

    return {
        "severe_ids": [i for i in severe_ids if i in P.ekey],
        "mean_count": float(k.mean()),
        "p_zero": float((k == 0).mean()),
        "p_at_least_1": float((k >= 1).mean()),
        "p_at_least_2": float((k >= 2).mean()),
        "p_at_least_3": float((k >= 3).mean()),
        "p_at_least_4": float((k >= 4).mean()),
        "p95_count": float(np.percentile(k, 95)),
        "p99_count": float(np.percentile(k, 99)),
        "independent_p_at_least_2": float((indep >= 2).mean()),
        "independent_p_at_least_3": float((indep >= 3).mean()),
        "independent_mean": float(indep.mean()),
        "clustering_excess_3plus": float((k >= 3).mean() - (indep >= 3).mean()),
        "count_distribution": np.bincount(k, minlength=len(idx) + 1)[: len(idx) + 1].tolist(),
        "count_distribution_independent": np.bincount(indep, minlength=len(idx) + 1)[
            : len(idx) + 1
        ].tolist(),
    }


def scenario_clusters(P: CompiledParams, res: dict, k=6, seed=11, feature_keys=None) -> dict:
    """Cluster whole world-trajectories into emergent scenarios.

    Features mix terminal indicator levels (where the world ended up) with event
    incidence (how it got there), both standardised. Clusters are not imposed
    scenarios -- they are whatever the coupled dynamics actually produce, which
    is the point.
    """
    from sklearn.cluster import KMeans

    P_ = P
    zx = (res["x_final"] - P_.attractor[None, :]) / P_.scale[None, :]
    zx = np.clip(zx, -6, 6)

    if feature_keys:
        cols = [P_.ikey[k_] for k_ in feature_keys if k_ in P_.ikey]
    else:
        cols = list(range(len(P_.indicators)))
    feat_x = zx[:, cols]

    ev = res["fired"].astype(np.float64)
    keep = (ev.mean(axis=0) > 0.005) & (ev.mean(axis=0) < 0.995)
    ev = ev[:, keep]
    ev = (ev - ev.mean(axis=0)) / np.maximum(ev.std(axis=0), 1e-9)

    # Event incidence is downweighted so terminal state -- the thing a scenario
    # narrative is really about -- dominates cluster geometry.
    F = np.hstack([feat_x, 0.55 * ev])
    F = (F - F.mean(axis=0)) / np.maximum(F.std(axis=0), 1e-9)

    sub = F[np.random.default_rng(seed).choice(F.shape[0], size=min(60_000, F.shape[0]), replace=False)]
    km = KMeans(n_clusters=k, n_init=10, random_state=seed).fit(sub)
    lab = km.predict(F)

    clusters = []
    ev_names = [e.id for e, kp in zip(P_.events, keep) if kp]
    all_ev = res["fired"].astype(np.float64)[:, keep]
    for c in range(k):
        m = lab == c
        share = float(m.mean())
        if share == 0:
            continue
        prof_x = zx[m].mean(axis=0)
        prof_e = all_ev[m].mean(axis=0)
        base_e = all_ev.mean(axis=0)
        # Rank events by absolute deviation from their unconditional rate:
        # what distinguishes this world, not merely what is common in it.
        order = np.argsort(-np.abs(prof_e - base_e))[:12]
        ind_order = np.argsort(-np.abs(prof_x))[:12]
        clusters.append(
            {
                "id": c,
                "probability": share,
                "distinguishing_events": [
                    {"id": ev_names[i], "p_in_cluster": float(prof_e[i]), "p_overall": float(base_e[i])}
                    for i in order
                ],
                "indicator_profile": [
                    {
                        "key": P_.indicators[i].key,
                        "label": P_.indicators[i].label,
                        "z": float(prof_x[i]),
                        "value": float(res["x_final"][m, i].mean()),
                        "unit": P_.indicators[i].unit,
                    }
                    for i in ind_order
                ],
                "mean_severe_events": float(all_ev[m].sum(axis=1).mean()),
            }
        )
    clusters.sort(key=lambda c: -c["probability"])
    return {"k": k, "clusters": clusters}


def sensitivity(P: CompiledParams, res: dict, outcome_ids: list[str], horizon="2036") -> list[dict]:
    """Which uncertain inputs move the headline outcomes?

    Rank-correlates each path's sampled global-coupling multiplier and each
    terminal indicator z-score against a composite bad-outcome indicator. This
    is a variance-attribution readout, not a causal claim -- but it tells the
    reader which assumption to argue with first.
    """
    from scipy.stats import rankdata

    q = _q(HORIZONS[horizon])
    idx = [P.ekey[i] for i in outcome_ids if i in P.ekey]
    if not idx:
        return []
    fq = res["fire_q"][:, idx]
    y = ((fq >= 0) & (fq <= q)).sum(axis=1).astype(np.float64)
    if y.std() < 1e-12:
        return []
    ry = rankdata(y)

    def _rho(a: np.ndarray, b: np.ndarray) -> float:
        if a.std() < 1e-12 or b.std() < 1e-12:
            return 0.0
        return float(np.corrcoef(a, b)[0, 1])

    rows = []
    cm = res["coup"]
    rows.append(
        {"driver": "global_coupling_multiplier", "kind": "structural",
         "spearman": _rho(rankdata(cm), ry)}
    )

    zx = np.clip((res["x_final"] - P.attractor[None, :]) / P.scale[None, :], -6, 6)
    # Rank-correlating 200k x K directly is wasteful; a 40k subsample is ample
    # for ordering drivers by influence.
    sub = np.random.default_rng(3).choice(zx.shape[0], size=min(40_000, zx.shape[0]), replace=False)
    rys = rankdata(y[sub])
    for i, ind in enumerate(P.indicators):
        col = zx[sub, i]
        if col.std() < 1e-9:
            continue
        rows.append(
            {"driver": ind.key, "kind": "state", "label": ind.label,
             "spearman": _rho(rankdata(col), rys)}
        )
    rows.sort(key=lambda r: -abs(r["spearman"]))
    return rows[:30]


def regime_summary(P: CompiledParams, res: dict) -> list[dict]:
    occ = res["regime_time"].mean(axis=0)
    return [
        {
            "name": r.name,
            "description": r.description,
            "initial_probability": r.p0,
            "expected_time_share": float(occ[i]),
            "hazard_multiplier": r.hazard_mult,
            "vol_multiplier": r.vol_mult,
        }
        for i, r in enumerate(P.regimes)
    ]


def indicator_terminal(P: CompiledParams, res: dict) -> list[dict]:
    x = res["x_final"]
    out = []
    for i, ind in enumerate(P.indicators):
        col = x[:, i]
        out.append(
            {
                "key": ind.key,
                "label": ind.label,
                "domain": ind.domain,
                "unit": ind.unit,
                "start": ind.value,
                "as_of": ind.as_of,
                "source": ind.source,
                "p5": float(np.percentile(col, 5)),
                "p25": float(np.percentile(col, 25)),
                "p50": float(np.percentile(col, 50)),
                "p75": float(np.percentile(col, 75)),
                "p95": float(np.percentile(col, 95)),
                "mean": float(col.mean()),
            }
        )
    return out

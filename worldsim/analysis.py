"""Reading answers out of the path ensemble.

Everything here operates on the pooled fire-time matrix. The pooling is weighted
sampling across worldviews, so a statistic computed on the pool is already the
ensemble-averaged statistic; and because every path still carries the id of the
parameter world it came from, we can separate "the world is uncertain" from "we
are uncertain about the world".
"""

from __future__ import annotations


import numpy as np
from scipy.cluster.vq import kmeans2

from .timeline import N_QUARTERS, horizon_label

Z90 = 1.6448536269514722


# --------------------------------------------------------------------------
# Pooling across worldviews
# --------------------------------------------------------------------------


def pool_worldviews(results: list[dict], weights: list[float], n_target: int, rng) -> dict:
    """Weighted resample of paths across worldviews into one ensemble sample.

    Each path keeps a `group` label identifying (worldview, parameter world), so
    downstream code can decompose variance into epistemic and Monte Carlo parts.
    """
    fires, groups, views = [], [], []
    offset = 0
    for vi, (res, w) in enumerate(zip(results, weights)):
        take = int(round(n_target * w))
        n_avail = res["fire_time"].shape[0]
        idx = rng.choice(n_avail, size=min(take, n_avail), replace=take > n_avail)
        fires.append(res["fire_time"][idx])
        groups.append(res["world_id"][idx].astype(np.int64) + offset)
        views.append(np.full(len(idx), vi, dtype=np.int8))
        offset += int(res["world_id"].max()) + 1
    return {
        "fire_time": np.concatenate(fires, axis=0),
        "group": np.concatenate(groups),
        "view": np.concatenate(views),
        "risk_ids": results[0]["risk_ids"],
    }


# --------------------------------------------------------------------------
# Marginals with epistemic intervals
# --------------------------------------------------------------------------


def marginal_with_interval(
    fire_time: np.ndarray, group: np.ndarray, quarters: list[int]
) -> dict[int, dict[str, np.ndarray]]:
    """P(risk fires by q) plus a 90% credible interval on that probability.

    The interval is the spread of the estimate across parameter worlds, with the
    within-world binomial noise subtracted off. Skipping that subtraction is the
    classic way to report intervals that are mostly Monte Carlo error dressed up
    as knowledge.

    The subtraction is done by *shrinking* each world's estimate toward the
    ensemble mean by sqrt(V_epistemic / V_total) and then taking empirical
    quantiles of the shrunken estimates. Reporting mean +/- z*sd instead would be
    wrong at the edges: a node at 88% would be handed an upper bound above 1 and
    clipped to ">99%", which reads as a claim about certainty when it is really
    an artefact of forcing a symmetric interval onto a bounded quantity. Shrinking
    keeps the interval inside [0, 1] and keeps its asymmetry.
    """
    order = np.argsort(group, kind="stable")
    g_sorted = group[order]
    ft_sorted = fire_time[order]
    bounds = np.flatnonzero(np.diff(g_sorted)) + 1
    starts = np.concatenate(([0], bounds))
    ends = np.concatenate((bounds, [len(g_sorted)]))

    R = fire_time.shape[1]
    out: dict[int, dict[str, np.ndarray]] = {}
    for q in quarters:
        hit = ((ft_sorted >= 0) & (ft_sorted <= q)).astype(np.float32)
        n_groups = len(starts)
        p_g = np.empty((n_groups, R), dtype=np.float64)
        m_g = np.empty(n_groups, dtype=np.float64)
        for i, (s, e) in enumerate(zip(starts, ends)):
            p_g[i] = hit[s:e].mean(axis=0)
            m_g[i] = e - s
        w = m_g / m_g.sum()
        mean = (p_g * w[:, None]).sum(axis=0)
        v_total = (w[:, None] * (p_g - mean) ** 2).sum(axis=0)
        v_binom = (w[:, None] * (p_g * (1 - p_g) / np.maximum(m_g, 1)[:, None])).sum(axis=0)
        v_epi = np.maximum(v_total - v_binom, 0.0)
        sd = np.sqrt(v_epi)

        lam = np.sqrt(v_epi / np.maximum(v_total, 1e-12))
        shrunk = mean[None, :] + lam[None, :] * (p_g - mean[None, :])
        lo, hi = np.quantile(shrunk, [0.05, 0.95], axis=0)

        out[q] = {
            "mean": mean,
            "lo": np.clip(np.minimum(lo, mean), 0.0, 1.0),
            "hi": np.clip(np.maximum(hi, mean), 0.0, 1.0),
            "epistemic_sd": sd,
        }
    return out


def view_disagreement(results: list[dict], quarters: list[int]) -> dict[int, np.ndarray]:
    """Spread of the point estimate across the five worldviews (max - min)."""
    out = {}
    for q in quarters:
        est = np.stack(
            [
                ((r["fire_time"] >= 0) & (r["fire_time"] <= q)).mean(axis=0)
                for r in results
            ]
        )
        out[q] = est
    return out


# --------------------------------------------------------------------------
# Joint structure
# --------------------------------------------------------------------------



def first_chains(
    fire_time: np.ndarray, severe_idx: list[int], depth: int = 3, top: int = 25
) -> list[tuple[list[int], int]]:
    """Most common opening sequences of high-severity events.

    Answers "when a bad decade starts, what does it start with, and what follows",
    which is a more useful thing to know than any single marginal.
    """
    ft = fire_time[:, severe_idx].astype(np.int16)
    ft = np.where(ft < 0, 9999, ft)
    order = np.argsort(ft, axis=1, kind="stable")
    sorted_t = np.take_along_axis(ft, order, axis=1)
    valid = sorted_t[:, :depth] < 9999
    keep = valid.all(axis=1)
    if keep.sum() == 0:
        return []
    seq = order[keep][:, :depth]
    base = len(severe_idx) + 1
    code = np.zeros(seq.shape[0], dtype=np.int64)
    for d in range(depth):
        code = code * base + seq[:, d]
    uniq, counts = np.unique(code, return_counts=True)
    best = np.argsort(counts)[::-1][:top]
    out = []
    for b in best:
        c = int(uniq[b])
        chain = []
        for _ in range(depth):
            chain.append(severe_idx[c % base])
            c //= base
        out.append((chain[::-1], int(counts[b])))
    return out


# --------------------------------------------------------------------------
# Scenario archetypes
# --------------------------------------------------------------------------


def archetypes(
    fire_time: np.ndarray,
    gssi: np.ndarray,
    feature_idx: list[int],
    k: int = 6,
    seed: int = 7,
    sample: int = 80_000,
) -> dict:
    """Cluster paths into recognisable futures and price each one.

    The clustering is on which major events fired plus the shape of the stress
    trajectory, so clusters come out as things like "contained decade",
    "fragmentation without war", "compound crisis". The output that matters is
    the probability mass on each.
    """
    n = fire_time.shape[0]
    hit = ((fire_time[:, feature_idx] >= 0)).astype(np.float32)
    peak = gssi.max(axis=1, keepdims=True)
    late = gssi[:, -8:].mean(axis=1, keepdims=True)
    early = gssi[:, :12].mean(axis=1, keepdims=True)
    X = np.hstack([hit, peak, late, early]).astype(np.float32)

    mu, sd = X.mean(axis=0), X.std(axis=0) + 1e-6
    Xs = (X - mu) / sd

    rng = np.random.default_rng(seed)
    sub = rng.choice(n, size=min(sample, n), replace=False)
    centroids, _ = kmeans2(Xs[sub], k, minit="++", seed=seed, iter=60)

    # Assign in blocks: the (n, k, features) intermediate is too big to materialise.
    labels = np.empty(n, dtype=np.int32)
    for s in range(0, n, 50_000):
        block = Xs[s : s + 50_000]
        dd = ((block[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2)
        labels[s : s + 50_000] = dd.argmin(axis=1)

    overall = hit.mean(axis=0)
    clusters = []
    for c in range(k):
        m = labels == c
        if m.sum() == 0:
            continue
        rates = hit[m].mean(axis=0)
        clusters.append(
            {
                "cluster": int(c),
                "probability": float(m.mean()),
                "peak_stress_median": float(np.median(peak[m])),
                # Where this cluster's typical peak sits in the distribution of
                # peaks across *all* paths. A rank among five clusters would say
                # only "calmest of five"; this says how calm in absolute terms.
                "peak_stress_pctile": float((peak[:, 0] < np.median(peak[m])).mean()),
                "terminal_stress_median": float(np.median(late[m])),
                "event_rates": rates,
                # Standardised excess: raw excess penalised by how variable the
                # event is. Without this the "distinguishing" features are just
                # the near-universal events, which distinguish nothing.
                "excess_z": (rates - overall) / np.sqrt(np.maximum(overall * (1 - overall), 1e-6)),
                "n_events_mean": float(hit[m].sum(axis=1).mean()),
            }
        )
    clusters.sort(key=lambda c: -c["probability"])
    return {"clusters": clusters, "labels": labels, "overall_rates": overall}


# --------------------------------------------------------------------------
# Sensitivity and aggregate outcome statistics
# --------------------------------------------------------------------------


def first_order_sensitivity(fire_time: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Share of the variance in `target` explained by each risk firing at all.

    For a binary driver this is exact rather than an approximation:
    Var(E[Y|X]) = p(1-p)(E[Y|1] - E[Y|0])^2.
    """
    hit = (fire_time >= 0)
    p = hit.mean(axis=0)
    var_y = target.var()
    n = fire_time.shape[0]
    sums = hit.T.astype(np.float64) @ target
    counts = hit.sum(axis=0)
    m1 = sums / np.maximum(counts, 1)
    m0 = (target.sum() - sums) / np.maximum(n - counts, 1)
    # A risk that never fires (or always fires) explains no variance by definition.
    never_varies = (counts == 0) | (counts == n)
    contrib = p * (1 - p) * (m1 - m0) ** 2
    contrib[never_varies] = 0.0
    return contrib / max(var_y, 1e-12)


def aggregate_stats(
    fire_time: np.ndarray, severity: np.ndarray, gssi: np.ndarray, quarter: int
) -> dict:
    """Event counts by impact tier — pass severity already zeroed on non-destabilising nodes.

    Reported across several thresholds rather than one, because a single cutoff
    hides the shape. "Severity >= 6" turns out to be a wide band containing both
    a US recession and a nuclear detonation, so any single-threshold headline
    either sounds absurd or buries the tail.

    Note that severity is *impact magnitude*, not badness: analysts were asked
    "global systemic impact if it occurs, 10 = civilization-altering", so a
    transformative AI capability milestone can legitimately score 9. Report these
    as high-impact events, never as catastrophes.
    """
    hit = ((fire_time >= 0) & (fire_time <= quarter))
    peak = gssi[:, :quarter].max(axis=1)

    tiers: dict[str, dict] = {}
    counts: dict[int, np.ndarray] = {}
    for thr in (6, 7, 8, 9):
        n = hit[:, severity >= thr].sum(axis=1)
        counts[thr] = n
        tiers[f"ge{thr}"] = {
            "n_nodes": int((severity >= thr).sum()),
            "expected": float(n.mean()),
            "deciles": np.quantile(n, [0.1, 0.25, 0.5, 0.75, 0.9]).tolist(),
            "p_zero": float((n == 0).mean()),
            "p_ge_1": float((n >= 1).mean()),
            "p_ge_2": float((n >= 2).mean()),
            "p_ge_3": float((n >= 3).mean()),
            "p_ge_5": float((n >= 5).mean()),
        }

    return {
        "tiers": tiers,
        # Kept as the primary headline pair: 6+ is the broad "notable disruption"
        # band, 9+ is the genuinely order-changing tail.
        "expected_severe_events": float(counts[6].mean()),
        "severe_event_deciles": np.quantile(counts[6], [0.1, 0.25, 0.5, 0.75, 0.9]).tolist(),
        "p_zero_severe": float((counts[6] == 0).mean()),
        "p_ge_3_severe": float((counts[6] >= 3).mean()),
        "p_ge_5_severe": float((counts[6] >= 5).mean()),
        "expected_catastrophic_events": float(counts[9].mean()),
        "p_any_catastrophic": float((counts[9] >= 1).mean()),
        "p_two_plus_catastrophic": float((counts[9] >= 2).mean()),
        "peak_stress_quantiles": np.quantile(peak, [0.05, 0.25, 0.5, 0.75, 0.95]).tolist(),
    }


def stress_trajectory(gssi: np.ndarray) -> dict:
    return {
        "quarters": list(range(1, N_QUARTERS + 1)),
        "labels": [horizon_label(q) for q in range(1, N_QUARTERS + 1)],
        **{
            f"p{int(q*100)}": np.quantile(gssi, q, axis=0).tolist()
            for q in (0.05, 0.25, 0.5, 0.75, 0.95)
        },
    }


def timing_profile(fire_time: np.ndarray, idx: int) -> dict:
    """When, conditional on happening at all, does this event tend to land?"""
    ft = fire_time[:, idx]
    fired = ft[ft >= 0]
    if fired.size == 0:
        return {"p_ever": 0.0}
    return {
        "p_ever": float((ft >= 0).mean()),
        "median_quarter": float(np.median(fired)),
        "q25": float(np.quantile(fired, 0.25)),
        "q75": float(np.quantile(fired, 0.75)),
    }


def top_pairs_by_lift(
    fire_time: np.ndarray, quarter: int, candidate_idx: list[int], min_joint: float, top: int
) -> list[tuple[int, int, float, float, float]]:
    """Pairs whose co-occurrence is most amplified relative to independence."""
    hit = ((fire_time >= 0) & (fire_time <= quarter))[:, candidate_idx].astype(np.float32)
    n = hit.shape[0]
    p = hit.mean(axis=0)
    joint = (hit.T @ hit) / n
    indep = np.outer(p, p)
    lift = joint / np.maximum(indep, 1e-12)
    out = []
    for i in range(len(candidate_idx)):
        for j in range(i + 1, len(candidate_idx)):
            if joint[i, j] >= min_joint:
                out.append(
                    (
                        candidate_idx[i],
                        candidate_idx[j],
                        float(joint[i, j]),
                        float(lift[i, j]),
                        float(joint[i, j] / max(p[j], 1e-9)),
                    )
                )
    out.sort(key=lambda r: -r[3])
    return out[:top]

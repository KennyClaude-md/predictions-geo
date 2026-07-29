"""Naming the clusters the simulation produced.

Deliberately rule-based rather than hand-written. If the clusters get renamed
every time the parameters change, that is correct behaviour — the archetypes are
supposed to be a finding, not a framing chosen in advance.
"""

from __future__ import annotations

import numpy as np

DOMAIN_WORDS = {
    "geopolitics": "great-power conflict",
    "climate": "climate stress",
    "economy": "financial and macro stress",
    "ai": "technological discontinuity",
    "energy": "energy disruption",
    "demographics": "demographic strain",
    "health": "health emergency",
    "politics": "institutional breakdown",
    "foodwater": "food and water stress",
}

STRESS_TIERS = [
    (0.15, "Quiet"),
    (0.40, "Manageable"),
    (0.65, "Turbulent"),
    (0.85, "Severe"),
    (1.01, "Compound crisis"),
]


def _tier(rank: float) -> str:
    for cut, name in STRESS_TIERS:
        if rank <= cut:
            return name
    return "Compound crisis"


def label_clusters(
    clusters: list[dict],
    feature_idx: list[int],
    names: list[str],
    domains: list[str],
    overall_rates: np.ndarray,
) -> list[dict]:
    peaks = np.array([c["peak_stress_median"] for c in clusters])
    order = np.argsort(np.argsort(peaks)) / max(len(peaks) - 1, 1)

    out = []
    used: set[str] = set()
    for i, c in enumerate(clusters):
        rates = c["event_rates"]
        excess = rates - overall_rates
        top = np.argsort(excess)[::-1][:6]

        # Which domains are over-represented, weighted by how over-represented.
        dom_weight: dict[str, float] = {}
        for t in top:
            if excess[t] <= 0.03:
                continue
            d = domains[feature_idx[t]]
            dom_weight[d] = dom_weight.get(d, 0.0) + float(excess[t])
        ranked_doms = sorted(dom_weight, key=lambda d: -dom_weight[d])[:2]

        tier = _tier(float(order[i]))
        if ranked_doms:
            theme = " and ".join(DOMAIN_WORDS.get(d, d) for d in ranked_doms)
            label = f"{tier} decade — {theme}"
        else:
            label = f"{tier} decade — no dominant driver"
        if label in used:
            label = f"{label} (variant)"
        used.add(label)

        signature = []
        for t in top:
            if excess[t] <= 0.04:
                continue
            signature.append(
                f"**{names[feature_idx[t]]}** — {rates[t]*100:.0f}% here vs "
                f"{overall_rates[t]*100:.0f}% overall"
            )

        below = np.argsort(excess)[:3]
        for t in below:
            if excess[t] >= -0.08:
                continue
            signature.append(
                f"{names[feature_idx[t]]} — *suppressed*: {rates[t]*100:.0f}% here vs "
                f"{overall_rates[t]*100:.0f}% overall"
            )

        desc = _describe(tier, ranked_doms, c)
        out.append(
            {
                "label": label,
                "probability": c["probability"],
                "description": desc,
                "signature": signature,
                "peak_stress_median": c["peak_stress_median"],
                "n_events_mean": c["n_events_mean"],
            }
        )
    return out


def _describe(tier: str, doms: list[str], c: dict) -> str:
    n = c["n_events_mean"]
    base = {
        "Quiet": (
            "Trend continuation. The scheduled stresses arrive on schedule and are "
            "absorbed; nothing in this cluster forces a structural break."
        ),
        "Manageable": (
            "Serious but sequential. Shocks land, institutions bend, and each one is "
            "substantially resolved before the next arrives."
        ),
        "Turbulent": (
            "Overlapping crises with intact institutions. Response capacity is strained "
            "but not exhausted, and recovery between shocks is incomplete."
        ),
        "Severe": (
            "Concurrent failure across domains. Shocks arrive faster than systems absorb "
            "them, and the response to one degrades the capacity to answer the next."
        ),
        "Compound crisis": (
            "Correlated systemic failure. Multiple high-severity events fire in a narrow "
            "window and reinforce each other; this is the cluster where the coupling "
            "structure dominates the marginals."
        ),
    }[tier]
    driver = ""
    if doms:
        driver = (
            " The distinguishing driver is "
            + " compounded by ".join(DOMAIN_WORDS.get(d, d) for d in doms)
            + "."
        )
    return f"{base}{driver} Mean count of tracked major events: {n:.1f}."

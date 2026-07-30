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
    "israel": "Middle East conflict",
}

# Tiers are keyed to where the cluster's typical peak stress sits in the
# distribution of peaks across every simulated path — an absolute statement about
# the model's own output, not a rank among however many clusters we asked for.
STRESS_TIERS = [
    (0.20, "Contained"),
    (0.45, "Manageable"),
    (0.70, "Turbulent"),
    (0.88, "Severe"),
    (1.01, "Compound crisis"),
]

# A feature must be this many standard deviations from its overall rate to count
# as distinguishing. Raw excess would surface the near-universal events, which by
# definition distinguish nothing.
Z_THRESHOLD = 0.25


def _tier(pctile: float) -> str:
    for cut, name in STRESS_TIERS:
        if pctile <= cut:
            return name
    return "Compound crisis"


def label_clusters(
    clusters: list[dict],
    feature_idx: list[int],
    names: list[str],
    domains: list[str],
    overall_rates: np.ndarray,
    valence: np.ndarray | None = None,
) -> list[dict]:
    out = []
    used: set[str] = set()
    for c in clusters:
        rates = c["event_rates"]
        z = c["excess_z"]
        excess = rates - overall_rates

        # Only destabilising events name the cluster's theme. A cluster
        # distinguished by an outbreak of peace is not a "conflict" decade.
        destab = (
            np.ones(len(feature_idx), dtype=bool)
            if valence is None
            else np.array([valence[i] > 0 for i in feature_idx])
        )
        # An event that fires in almost every path cannot distinguish one cluster
        # from another, however large its z-score looks.
        destab &= overall_rates < 0.95

        # Mask once and read the masked array everywhere below. Masking only the
        # sort order lets an excluded event survive into the loop and name the
        # cluster's theme whenever the feature list is short.
        z_up = np.where(destab, z, -np.inf)
        z_down = np.where(destab, z, np.inf)

        top = np.argsort(z_up)[::-1][:6]
        dom_weight: dict[str, float] = {}
        for t in top:
            if z_up[t] <= Z_THRESHOLD:
                continue
            d = domains[feature_idx[t]]
            dom_weight[d] = dom_weight.get(d, 0.0) + float(z_up[t])
        ranked_doms = sorted(dom_weight, key=lambda d: -dom_weight[d])[:2]

        tier = _tier(float(c.get("peak_stress_pctile", 0.5)))
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
            if z_up[t] <= Z_THRESHOLD:
                continue
            signature.append(
                f"**{names[feature_idx[t]]}** — {rates[t]*100:.0f}% here vs "
                f"{overall_rates[t]*100:.0f}% overall"
            )

        for t in np.argsort(z_down)[:3]:
            if z_down[t] >= -Z_THRESHOLD:
                continue
            signature.append(
                f"{names[feature_idx[t]]} — *suppressed*: {rates[t]*100:.0f}% here vs "
                f"{overall_rates[t]*100:.0f}% overall"
            )

        out.append(
            {
                "label": label,
                "probability": c["probability"],
                "description": _describe(tier, ranked_doms, c),
                "signature": signature,
                "peak_stress_median": c["peak_stress_median"],
                "peak_stress_pctile": c.get("peak_stress_pctile"),
                "n_events_mean": c["n_events_mean"],
            }
        )
    return out


def _describe(tier: str, doms: list[str], c: dict) -> str:
    base = {
        "Contained": (
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
    pk = c.get("peak_stress_pctile")
    where = (
        f" Typical peak stress sits at the {pk*100:.0f}th percentile of all simulated paths."
        if pk is not None
        else ""
    )
    return f"{base}{driver}{where}"

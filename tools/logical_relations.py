#!/usr/bin/env python3
"""Logical relations between risk nodes, and the coherence repairs they imply.

Nine analysts wrote independently, so the register contains pairs whose
resolution criteria stand in a strict logical relation that their probabilities
violate. These are not calibration disagreements — they are arithmetic errors,
and they can be repaired without taking a view on who is right about the world.

Two kinds:

  IMPLICATION — event A's criteria strictly entail event B's, so P(B) >= P(A) at
  every horizon. The Hormuz pair is the clean case: geopolitics requires transit
  below 50% of baseline for >=30 consecutive days, economy requires the same
  threshold for >=14 days. Any 30-day episode contains a 14-day one. Yet the
  30-day node is priced 76% by 2036 and the 14-day node 27% — a 49-point
  violation. Repair raises the weaker node to the stronger node's probability;
  it never lowers the stronger one, because the implication says nothing about
  whether the subset estimate is too high.

  EQUIVALENCE — identical criteria under two ids, where the analysts simply
  disagree. The two FAO Food Price Index nodes both resolve on "monthly value
  above 160.0, surpassing the March 2022 record of 160.3" and are priced 48% and
  60% by 2036. Neither is privileged, so they are pooled in log-odds.

Found by the market-calibration red-team lens, which checked axioms rather than
just prices.

    python tools/logical_relations.py [world_model.json] [logical_relations.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# "stronger" entails "weaker": whenever stronger happens, weaker happens too.
IMPLICATIONS = [
    {
        "stronger": "geopolitics_hormuz_major_closure",
        "weaker": "economy_hormuz_closure",
        "reason": "Both use the same <50%-of-2025-baseline threshold; the stronger "
                  "requires 30 consecutive days, the weaker 14. Every 30-day episode "
                  "contains a 14-day one.",
    },
    {
        "stronger": "energy_hormuz_reclosure",
        "weaker": "economy_hormuz_closure",
        "reason": "A fall below 25% of baseline for 14+ days is a fall below 50% of "
                  "baseline for 14+ days.",
    },
    {
        "stronger": "ai_bio_mass_casualty",
        "weaker": "health_bioterror_attack_10_deaths",
        "reason": "An AI-assisted deliberate biological release killing >=10 is a "
                  "deliberate biological release killing >=10.",
    },
    {
        "stronger": "ai_bio_mass_casualty",
        "weaker": "health_ai_enabled_bio_incident",
        "reason": "A confirmed AI-assisted release killing >=10 is a confirmed "
                  "incident in which AI materially assisted a bio actor.",
    },
    {
        "stronger": "geopolitics_iran_nuclear_weapon",
        "weaker": "geopolitics_new_nuclear_weapons_state",
        "reason": "Iran acquiring a weapon is a state that does not now possess "
                  "nuclear weapons acquiring one.",
    },
    {
        "stronger": "geopolitics_china_taiwan_invasion",
        "weaker": "geopolitics_us_china_lethal_clash",
        "reason": "Not strictly entailed — an unopposed invasion is conceivable — so "
                  "this is left to the coupling network instead.",
        "skip": True,
    },
]

# Identical criteria under two ids; the analysts disagree and neither is privileged.
EQUIVALENCES = [
    {
        "members": ["climate_food_price_shock", "foodwater_ffpi_above_160"],
        "reason": "Both resolve on the FAO Food Price Index monthly value exceeding "
                  "160.0, both citing the March 2022 record of 160.3.",
    },
    {
        "members": ["geopolitics_iran_regime_change", "politics_iran_islamic_republic_ends"],
        "reason": "Both resolve on the Islamic Republic ceasing to govern Iran.",
    },
    {
        "members": ["geopolitics_putin_exit", "politics_russia_leadership_change"],
        "reason": "Both resolve on Putin ceasing to hold paramount power.",
    },
    {
        "members": ["economy_oil_120", "energy_oil_price_spike_120"],
        "reason": "Brent above $120 — a settlement print versus a monthly average, "
                  "close enough that a 2x probability gap is analyst disagreement.",
    },
]


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("params/world_model.json")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("params/logical_relations.json")

    model = json.loads(src.read_text())
    probs: dict[str, tuple[float, float, float]] = {}
    for dom in model.get("domains", []):
        for r in (dom.get("research") or {}).get("discrete_risks", []) or []:
            probs[str(r["id"])] = (
                float(r.get("p_by_2027_pct") or 0),
                float(r.get("p_by_2031_pct") or 0),
                float(r.get("p_by_2036_pct") or 0),
            )
        for m in ((dom.get("calibration") or {}).get("missing_risks") or []):
            p31 = float(m.get("p_by_2031_pct") or 0)
            probs[str(m["id"])] = (p31 * 0.4, p31, min(p31 * 1.6, 99.0))

    impl = []
    for rel in IMPLICATIONS:
        if rel.get("skip"):
            print(f"  skipped (not strict): {rel['stronger']} -> {rel['weaker']}")
            continue
        s, w = rel["stronger"], rel["weaker"]
        if s not in probs or w not in probs:
            print(f"  missing node, skipping: {s} -> {w}")
            continue
        gaps = [round(probs[s][i] - probs[w][i], 1) for i in range(3)]
        violated = max(gaps) > 0.5
        impl.append({**rel, "gaps_pp": gaps, "violated": violated})
        flag = "VIOLATED" if violated else "ok"
        print(f"  {flag:9s} {s[:38]:40s} => {w[:34]:36s} gaps {gaps}")

    equiv = []
    for rel in EQUIVALENCES:
        present = [m for m in rel["members"] if m in probs]
        if len(present) < 2:
            print(f"  missing node, skipping equivalence: {rel['members']}")
            continue
        spread = [
            round(max(probs[m][i] for m in present) - min(probs[m][i] for m in present), 1)
            for i in range(3)
        ]
        equiv.append({**rel, "members": present, "spread_pp": spread})
        print(f"  equivalence {' ~ '.join(m[:26] for m in present):58s} spread {spread}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps({"implications": impl, "equivalences": equiv}, indent=2))
    n_viol = sum(1 for i in impl if i["violated"])
    print(f"\nwrote {dst}: {len(impl)} implications ({n_viol} violated), "
          f"{len(equiv)} equivalences")


if __name__ == "__main__":
    main()

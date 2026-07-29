#!/usr/bin/env python3
"""Group risk nodes that describe one real-world event.

Nine analysts wrote their registers independently, so the same shock appears
several times. `worldsim/dedupe.py` screens for candidates automatically; this
file is the curated decision, because the screen cannot tell the two cases apart:

  TRUE DUPLICATE — the same event under two ids, e.g. Putin ceasing to hold
  power, enumerated by both the geopolitics and the politics analyst.

  NESTED THRESHOLD — different bars on one axis. The three Hormuz nodes are a
  full closure (28% by 2036), a 50%-of-baseline reduction sustained 30 days
  (76%), and a 14-day re-closure. Those are genuinely different questions and
  their separate probabilities are all worth reporting.

Both corrupt the same statistics. Counting "Hormuz partly closed" and "Hormuz
fully closed" as two high-impact events tallies one crisis twice, and the stress
index adds its severity twice. So for *aggregate* purposes each family
contributes only its highest-impact member; every node keeps its own marginal in
the per-node tables, which is where the distinct thresholds belong.

Families are NOT merged and NOT deleted. Nesting is a logical implication the
coupling network is the right place to express.

    python tools/duplicate_families.py [world_model.json] [families.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

FAMILIES: list[dict] = [
    {
        "name": "Strait of Hormuz disruption",
        "kind": "nested",
        "members": [
            "geopolitics_hormuz_major_closure",
            "economy_hormuz_closure",
            "energy_hormuz_reclosure",
        ],
        "note": "Different severity bars on one strait: >=30 days below 50% of "
                "baseline, sustained effective closure, and a 14-day re-closure.",
    },
    {
        "name": "Brent above $120",
        "kind": "duplicate",
        "members": ["economy_oil_120", "energy_oil_price_spike_120"],
        "note": "Settlement price versus monthly average — the same oil shock.",
    },
    {
        "name": "FAO Food Price Index above 160",
        "kind": "duplicate",
        "members": ["climate_food_price_shock", "foodwater_ffpi_above_160"],
        "note": "Identical threshold on the identical index.",
    },
    {
        "name": "Putin leaves power",
        "kind": "duplicate",
        "members": ["geopolitics_putin_exit", "politics_russia_leadership_change"],
        "note": "Same event, enumerated by the geopolitics and politics analysts.",
    },
    {
        "name": "The Islamic Republic falls",
        "kind": "duplicate",
        "members": ["geopolitics_iran_regime_change", "politics_iran_islamic_republic_ends"],
        "note": "Same event under two ids.",
    },
    {
        "name": "State cyberattack takes down a grid",
        "kind": "duplicate",
        "members": ["energy_grid_cyber_major_outage", "geopolitics_grid_cyberattack_nato"],
        "note": "Major OECD outage versus >=24h loss to >=1m people in NATO — the "
                "same class of incident at near-identical scale.",
    },
    {
        "name": "Taiwan semiconductor supply shock",
        "kind": "duplicate",
        "members": ["ai_taiwan_supply_shock", "economy_taiwan_chip_shock"],
        "note": "Both auditors added the same contingency to their own domain.",
    },
    {
        "name": "Mass-casualty biological attack",
        "kind": "nested",
        "members": [
            "health_bioterror_attack_10_deaths",
            "ai_bio_mass_casualty",
            "health_ai_enabled_bio_incident",
        ],
        "note": "Any deliberate attack killing >=10, the AI-assisted subset of "
                "that, and any acknowledged AI-enabled bio incident.",
    },
]


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("params/world_model.json")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("params/duplicate_families.json")

    model = json.loads(src.read_text())
    known: dict[str, float] = {}
    for dom in model.get("domains", []):
        for r in (dom.get("research") or {}).get("discrete_risks", []) or []:
            known[str(r.get("id"))] = float(r.get("severity_0_10") or 0)
        for m in ((dom.get("calibration") or {}).get("missing_risks") or []):
            known[str(m.get("id"))] = float(m.get("severity_0_10") or 0)

    out = []
    for fam in FAMILIES:
        present = [m for m in fam["members"] if m in known]
        missing = [m for m in fam["members"] if m not in known]
        if len(present) < 2:
            print(f"  skip '{fam['name']}': only {len(present)} member(s) in the register")
            continue
        # The representative is the highest-impact member: aggregate counts should
        # reflect the most consequential reading of the event, not the mildest.
        rep = max(present, key=lambda m: (known[m], m))
        out.append({**fam, "members": present, "representative": rep, "suppressed": [
            m for m in present if m != rep]})
        if missing:
            print(f"  note '{fam['name']}': {len(missing)} listed id(s) not in register")

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(out, indent=2))
    n_sup = sum(len(f["suppressed"]) for f in out)
    print(f"wrote {dst}: {len(out)} families, {n_sup} nodes suppressed from aggregates")
    for f in out:
        print(f"  {f['kind']:9s} {f['name'][:42]:44s} keep {f['representative']}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Assign each risk node a valence: does it push the world toward stress or away?

Analysts were asked for the *magnitude* of an event's global impact, so severity
is unsigned — a durable ceasefire and a nuclear detonation can both score 7. The
simulation needs the sign as well, or the stress index reads an outbreak of peace
as a crisis and the archetype labeller calls that decade "compound crisis".

Everything defaults to +1 (destabilising), which is the right prior for an
enumerated risk register. Only the exceptions are listed here, so the file stays
short enough to actually audit.

    python tools/classify_valence.py [world_model.json] [valence.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# -1 : stabilising. Occurrence reduces systemic stress.
STABILISING = {
    # Conflict termination and arms control
    "geopolitics_ukraine_durable_ceasefire",
    "geopolitics_us_russia_strategic_arms_deal",
    "geopolitics_unsc_permanent_expansion",
    # Climate: the good-news nodes
    "climate_fossil_co2_confirmed_peak",
    "climate_methane_growth_halts",
    "climate_srm_governance_regime",
    # Governance of frontier technology
    "ai_us_china_binding_agreement",
    # Energy transition milestones — these are the good-news nodes of the set
    "energy_global_coal_demand_structural_decline",
    "energy_china_emissions_sustained_decline",
    "energy_global_oil_demand_peak",
    "energy_solar_terawatt_year",
    "energy_western_smr_first_power",
    "energy_hydrogen_scale_milestone",
    # Health governance and disease-control wins
    "health_pandemic_agreement_in_force",
    "health_pabs_annex_adopted",
    "health_polio_wpv1_interrupted",
    "health_us_rejoins_who",
    # Demography: a fertility floor being escaped, and lifespan recovering
    "demographics_korea_tfr_reaches_1",
    "demographics_us_life_expectancy_80",
    # Food and water (ids provisional until that domain lands)
    "foodwater_transboundary_water_treaty",
    "foodwater_famine_declarations_end",
}

# 0 : genuinely ambiguous. Contributes no signed stress, still simulated and
# still available as a cascade parent — it just doesn't move the index either way.
AMBIGUOUS = {
    "geopolitics_iran_regime_change",
    "climate_billion_dollar_climate_judgment",
    "economy_china_mega_bailout",
    "ai_export_controls_relaxed",
    "ai_federal_preemption_enacted",
    "ai_ai_theorem_top_journal",
    "ai_robotaxi_5m_weekly",
    "ai_china_leaderboard_top",
    "ai_state_datacenter_moratorium",
    # Governance outcomes that are contested rather than good-or-bad. These are
    # electoral and succession events: which way they cut is a political
    # judgement the model has no business encoding as systemic stress.
    "politics_dem_control_a_chamber_2027",
    "politics_rn_holds_french_presidency",
    "politics_afd_enters_government",
    "politics_reform_uk_leads_government",
    "politics_russia_leadership_change",
    "politics_xi_departure",
    "politics_iran_islamic_republic_ends",
    # Cheap oil helps consumers, hurts producers and the transition's economics.
    "energy_oil_price_collapse_45",
    # Policy responses to strain: they signal the strain as much as they relieve it.
    "demographics_eu_third_country_return_hubs",
    "demographics_major_pronatalist_spending_surge",
    # A scheduled statistical release, not an event.
    "demographics_india_census_provisional_totals",
}

# Substring rules for nodes the explicit lists miss — the research pipeline names
# its own ids, so a run that adds domains should not silently misclassify.
STABILISING_HINTS = (
    "ceasefire", "peace_deal", "peace_agreement", "treaty_in_force",
    "arms_control", "_deescalat", "emissions_peak", "_recovery_",
)
AMBIGUOUS_HINTS = ("_governance_", "_regulat", "_moratorium", "_bailout", "_rescue")


def classify(risk_id: str) -> float:
    if risk_id in STABILISING:
        return -1.0
    if risk_id in AMBIGUOUS:
        return 0.0
    low = risk_id.lower()
    if any(h in low for h in STABILISING_HINTS):
        return -1.0
    if any(h in low for h in AMBIGUOUS_HINTS):
        return 0.0
    return 1.0


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("params/world_model.json")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("params/valence.json")

    model = json.loads(src.read_text())
    out: dict[str, float] = {}
    for dom in model.get("domains", []):
        for r in (dom.get("research") or {}).get("discrete_risks", []) or []:
            rid = str(r.get("id", ""))
            if rid:
                out[rid] = classify(rid)
        for miss in ((dom.get("calibration") or {}).get("missing_risks") or []):
            rid = str(miss.get("id", ""))
            if rid:
                out[rid] = classify(rid)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(dict(sorted(out.items())), indent=2))

    n_stab = sum(1 for v in out.values() if v < 0)
    n_amb = sum(1 for v in out.values() if v == 0)
    print(f"wrote {dst}: {len(out)} nodes")
    print(f"  destabilising : {len(out) - n_stab - n_amb}")
    print(f"  stabilising   : {n_stab}")
    print(f"  ambiguous     : {n_amb}")
    unmatched = [k for k in STABILISING | AMBIGUOUS if k not in out]
    if unmatched:
        print(f"  listed but not in model ({len(unmatched)}): {', '.join(sorted(unmatched))}")


if __name__ == "__main__":
    main()

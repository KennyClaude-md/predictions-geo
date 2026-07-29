#!/usr/bin/env python3
"""Correlate each continuous indicator with the systemic-stress index.

The continuous layer uses a Gaussian copula: marginals come from the analysts'
elicited deciles, dependence comes from each path's own stress index. This file
supplies the one missing number per variable — the correlation rho.

Signs are the whole point. A stressed decade means *lower* global growth and
*higher* gold; getting one of those backwards puts the bad tail of an indicator
in the wrong half of the path distribution. Magnitudes are deliberately moderate:
these are directional judgements about co-movement, not fitted coefficients.

Ambiguity is recorded as a small number rather than a confident one. USD/JPY is
the clean example — yen strengthens as a haven in acute stress, but Japanese
fiscal deterioration pushes the other way over a decade, so it gets -0.15.

    python tools/stress_loadings.py [world_model.json] [stress_loadings.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LOADINGS: dict[str, float] = {
    # --- geopolitics: conflict intensity and its transmission channels ---
    "geo_battle_deaths_annual": 0.70,
    "geo_hormuz_crude_flow": -0.60,
    "geo_active_state_conflicts": 0.60,
    "geo_global_milex_pct_gdp": 0.55,
    "geo_brent_crude_usd": 0.55,
    "geo_suez_container_transits": -0.55,
    "geo_us_milex_pct_gdp": 0.45,
    "geo_europe_nato_milex_pct_gdp": 0.45,
    "geo_taiwan_adiz_sorties": 0.45,
    "geo_deployed_strategic_warheads": 0.45,
    "geo_ukraine_monthly_territory_change": 0.30,
    # Acute crises push reserves *into* the dollar; a decade of fragmentation
    # pushes them out. The second effect dominates over this horizon, weakly.
    "geo_usd_reserve_share": -0.25,

    # --- climate: forcing and its visible consequences ---
    "fao_food_price_index": 0.55,
    "reef_bleaching_stress_pct": 0.40,
    "gmst_anomaly_era5": 0.35,
    "arctic_sept_ice_min": -0.30,
    "amazon_deforestation_brazil": 0.30,
    "nino34_oni_annual_max": 0.25,
    "ocean_heat_content_increment": 0.25,
    "co2_mauna_loa_annual": 0.20,
    "ch4_global_mean": 0.20,
    "global_mean_sea_level": 0.15,
    # Near zero by cancellation, not by irrelevance: a stressed decade burns more
    # fossil fuel through energy insecurity and less through weaker demand.
    "fossil_co2_emissions": 0.10,

    # --- macro and markets ---
    "global_gdp_growth": -0.65,
    "brent_crude": 0.55,
    "sp500_level": -0.55,
    "china_gdp_growth": -0.50,
    "gold_price": 0.50,
    "us_debt_gdp": 0.45,
    "us_effective_tariff_rate": 0.45,
    "us_cpi_yoy": 0.40,
    "ust_10y": 0.25,
    "usd_reserve_share": -0.25,
    "fed_funds_upper": 0.15,
    "usdjpy": -0.15,

    # --- AI and compute: mostly a financial-cycle exposure ---
    "hyperscaler_capex_usd_b": -0.30,
    "nvidia_dc_revenue_usd_b": -0.30,
    "frontier_lab_arr_usd_b": -0.25,
    "cn_open_weight_token_share": 0.20,
    "metr_horizon_log2_hours": 0.20,
    "frontier_train_flop_log10": 0.15,
    "global_dc_electricity_twh": 0.15,
    "driverless_rides_log10_m_wk": -0.15,
    "gpt4_class_cost_log10": 0.0,
    "btos_ai_adoption_emp_wt": 0.0,
}

# Fallback for variables added by domains that ran after this file was written.
# Matched against the id and the human-readable name, first hit wins.
HINTS: list[tuple[tuple[str, ...], float]] = [
    (("battle_death", "conflict", "displac", "refugee", "famine", "insecur"), 0.60),
    (("price_index", "food_price", "fertiliser", "fertilizer"), 0.50),
    (("gold", "volatility", "spread", "debt_gdp", "tariff"), 0.40),
    (("brent", "crude", "oil_price", "gas_price", "lng"), 0.45),
    (("growth", "gdp", "output", "yield_per", "harvest", "stocks_to_use"), -0.50),
    (("equity", "index_level", "sp500", "capex", "investment"), -0.35),
    (("transit", "throughput", "shipment", "trade_volume"), -0.45),
    (("temperature", "anomaly", "emission", "concentration", "sea_level"), 0.20),
    (("ice_extent", "ice_min", "glacier", "reservoir", "aquifer", "storage"), -0.25),
    (("life_expectancy", "immunis", "immuniz", "coverage", "access"), -0.30),
    (("mortality", "deaths", "resistance", "outbreak", "burden"), 0.45),
    (("fertility", "population", "migration", "urbanis", "urbaniz"), 0.10),
]


def loading_for(var_id: str, name: str) -> float:
    if var_id in LOADINGS:
        return LOADINGS[var_id]
    hay = f"{var_id} {name}".lower()
    for keys, rho in HINTS:
        if any(k in hay for k in keys):
            return rho
    return 0.0


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("params/world_model.json")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("params/stress_loadings.json")

    model = json.loads(src.read_text())
    out: dict[str, float] = {}
    explicit = fallback = zero = 0
    for dom in model.get("domains", []):
        for c in (dom.get("research") or {}).get("continuous_variables", []) or []:
            cid = str(c.get("id", ""))
            if not cid:
                continue
            rho = loading_for(cid, str(c.get("name", "")))
            out[cid] = rho
            if cid in LOADINGS:
                explicit += 1
            elif rho != 0.0:
                fallback += 1
            else:
                zero += 1

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(dict(sorted(out.items())), indent=2))
    print(f"wrote {dst}: {len(out)} variables")
    print(f"  explicit  : {explicit}")
    print(f"  by hint   : {fallback}")
    print(f"  unsigned  : {zero}  (independent of the discrete world)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate a structurally-valid but fictional world_model.json.

Purely for exercising the pipeline — shape and edge cases, never content. Used in
CI and for smoke tests so the engine can be validated without needing the research
pipeline to have run.
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

DOMAINS = [
    "geopolitics", "climate", "economy", "ai", "energy",
    "demographics", "health", "politics", "foodwater",
]


def build(seed: int = 3) -> dict:
    rng = random.Random(seed)
    domains = []
    all_ids = []

    for d in DOMAINS:
        risks = []
        for i in range(12):
            p27 = rng.uniform(0.3, 30)
            p31 = min(99.0, p27 * rng.uniform(1.4, 3.2))
            p36 = min(99.4, p31 * rng.uniform(1.05, 1.7))
            rid = f"{d}_risk_{i}"
            all_ids.append(rid)
            risks.append(
                {
                    "id": rid,
                    "name": f"Synthetic {d} event {i}",
                    "resolution_criteria": "placeholder criterion for pipeline testing",
                    "p_by_2027_pct": round(p27, 2),
                    "p_by_2031_pct": round(p31, 2),
                    "p_by_2036_pct": round(p36, 2),
                    "reasoning": "synthetic",
                    "base_rate_anchor": "synthetic",
                    "severity_0_10": round(rng.uniform(2, 9), 1),
                    "confidence": rng.choice(["low", "medium", "high"]),
                    "contrarian_case": "synthetic",
                }
            )
        cvars = []
        for j in range(5):
            cur = rng.uniform(1, 100)
            p50 = cur * rng.uniform(0.8, 1.3)
            cvars.append(
                {
                    "id": f"{d}_var_{j}",
                    "name": f"Synthetic {d} indicator {j}",
                    "unit": "units",
                    "current_value": round(cur, 3),
                    "annual_drift": round((p50 - cur) / 5, 4),
                    "annual_vol": round(cur * 0.08, 4),
                    "p10_2031": round(p50 * 0.75, 3),
                    "p50_2031": round(p50, 3),
                    "p90_2031": round(p50 * 1.4, 3),
                    "notes": "synthetic",
                }
            )
        domains.append(
            {
                "domain": d,
                "title": d,
                "research": {
                    "domain": d,
                    "state_of_play": "synthetic",
                    "indicators": [],
                    "scheduled_events": [],
                    "discrete_risks": risks,
                    "continuous_variables": cvars,
                    "feedback_loops": [],
                    "structural_uncertainties": ["synthetic uncertainty"],
                    "sources": ["synthetic"],
                },
                "calibration": {
                    "domain": d,
                    "verdict": "minor_issues",
                    "adjustments": [
                        {
                            "risk_id": risks[0]["id"],
                            "field": "p_by_2031_pct",
                            "original_pct": risks[0]["p_by_2031_pct"],
                            "revised_pct": round(risks[0]["p_by_2031_pct"] * 0.7, 2),
                            "justification": "synthetic",
                        }
                    ],
                    "coherence_violations": [],
                    "missing_risks": [],
                    "overall_bias": "synthetic",
                },
            }
        )

    edges = []
    for _ in range(70):
        s, t = rng.sample(all_ids, 2)
        edges.append(
            {
                "source_id": s,
                "target_id": t,
                "odds_multiplier": round(rng.choice([0.4, 1.5, 2.2, 3.5, 6.0]), 2),
                "lag_years": rng.choice([0, 0.5, 1, 2]),
                "mechanism": "synthetic",
                "confidence": "medium",
            }
        )

    latents = []
    for k in range(4):
        latents.append(
            {
                "name": f"factor_{k}",
                "description": "synthetic",
                "loadings": [
                    {"risk_id": rid, "loading": round(rng.uniform(-0.4, 0.9), 2)}
                    for rid in rng.sample(all_ids, 30)
                ],
            }
        )

    redteam = []
    for lens in ["outside-view base rates", "structural break", "market check"]:
        redteam.append(
            {
                "lens": lens,
                "headline_critique": "synthetic",
                "specific_corrections": [
                    {
                        "risk_id": rid,
                        "claim": "synthetic",
                        "direction": rng.choice(["too_high", "too_low"]),
                        "suggested_pct": round(rng.uniform(1, 60), 1),
                        "evidence": "synthetic",
                    }
                    for rid in rng.sample(all_ids, 14)
                ],
                "systematic_bias_estimate": "synthetic",
                "missing_scenarios": [],
            }
        )

    return {
        "as_of": "2026-07-29",
        "domains": domains,
        "coupling": {
            "conditional_edges": edges,
            "latent_factors": latents,
            "blocking_pairs": [
                {"a_id": all_ids[0], "b_id": all_ids[5], "reason": "synthetic"}
            ],
            "notes": "synthetic",
        },
        "redteam": redteam,
        "risk_count": len(all_ids),
    }


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "params/synthetic_model.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(), indent=2))
    print(f"wrote {out}")

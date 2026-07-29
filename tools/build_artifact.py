#!/usr/bin/env python3
"""Turn output/forecast.json into a self-contained HTML page.

The template holds all the markup, styling and chart code; this script does
nothing but shape the payload it reads. Keeping the split there means the page
can be edited as a page rather than as Python string concatenation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "artifact_template.html"

DOMAIN_LABELS = {
    "geopolitics": "Great-power conflict & geopolitics",
    "climate": "Climate & Earth systems",
    "economy": "Global macroeconomy & finance",
    "ai": "AI, compute & transformative technology",
    "energy": "Energy systems & critical materials",
    "demographics": "Demography & migration",
    "health": "Pandemics, biosecurity & global health",
    "politics": "Political stability & governance",
    "foodwater": "Food, water & agriculture",
}
SHORT = {
    "geopolitics": "Geopolitics", "climate": "Climate", "economy": "Economy",
    "ai": "AI & tech", "energy": "Energy", "demographics": "Demography",
    "health": "Health", "politics": "Politics", "foodwater": "Food & water",
}


def q_label(q: float | None) -> str:
    if q is None:
        return "—"
    idx = int(round(q))
    total = (2026 * 4 + 2) + max(idx - 1, 0)
    return f"{total // 4}Q{total % 4 + 1}"


def sig(x: float, n: int = 3) -> float:
    if x == 0:
        return 0.0
    from math import floor, log10

    return round(x, max(0, n - 1 - int(floor(log10(abs(x))))))


def build(fc: dict, seed: int) -> dict:
    agg = fc["aggregate"]
    errs = [
        v["final_error_pp"]
        for v in fc["calibration"].values()
        if v.get("final_error_pp") is not None
    ]
    cal_pp = max(errs) if errs else 0.0

    tiles = [
        {
            "label": "Severe events expected",
            "value": f"{agg['expected_severe_events']:.1f}",
            "sub": f"severity ≥ 6, through 2036 · 10th–90th pct "
                   f"{agg['severe_event_deciles'][0]:.0f}–{agg['severe_event_deciles'][4]:.0f}",
        },
        {
            "label": "A decade with none",
            "value": _pct(agg["p_zero_severe"]),
            "sub": "probability no severity ≥ 6 event fires at all — the quiet case is a tail, "
                   "not the base case",
        },
        {
            "label": "At least one catastrophic",
            "value": _pct(agg["p_any_catastrophic"]),
            "sub": f"severity ≥ 8 · two or more: {_pct(agg['p_two_plus_catastrophic'])}",
        },
        {
            "label": "Three or more severe",
            "value": _pct(agg["p_ge_3_severe"]),
            "sub": f"five or more: {_pct(agg['p_ge_5_severe'])} — the compound case is where "
                   f"the coupling structure dominates",
        },
    ]

    st = fc["stress_trajectory"]
    stress = {
        "labels": [l.split(" ")[0] for l in st["labels"]],
        "p5": [round(v, 2) for v in st["p5"]],
        "p25": [round(v, 2) for v in st["p25"]],
        "p50": [round(v, 2) for v in st["p50"]],
        "p75": [round(v, 2) for v in st["p75"]],
        "p95": [round(v, 2) for v in st["p95"]],
        "caption": (
            "Index units are severity-weighted and decay-discounted, so the level is only "
            "meaningful relative to itself. The widening gap between the median and the 95th "
            "percentile is the model saying the downside is far more variable than the "
            "central case."
        ),
    }

    def row(r: dict) -> dict:
        return {
            "name": r["name"],
            "domain": r["domain"],
            "domain_label": SHORT.get(r["domain"], r["domain"]),
            "resolution": r["resolution"],
            "p2027": r["p2027"], "p2031": r["p2031"], "p2036": r["p2036"],
            "lo2036": r["lo2036"], "hi2036": r["hi2036"],
            "severity": r["severity"],
            "timing": q_label(r.get("median_quarter")),
        }

    domains = []
    for dom, rows in fc["by_domain"].items():
        domains.append(
            {
                "key": dom,
                "label": DOMAIN_LABELS.get(dom, dom),
                "rows": [row(r) for r in rows],
            }
        )
    domains.sort(key=lambda d: -sum(r["p2036"] * r["severity"] for r in d["rows"]))

    return {
        "meta": {
            "as_of": fc["as_of"],
            "n_paths": fc["n_paths_total"],
            "n_worlds": fc["n_worlds"] * fc["n_worldviews"],
            "n_risks": fc["n_risks"],
            "n_edges": fc["n_edges"],
            "calibration_pp": cal_pp,
            "seed": seed,
        },
        "tiles": tiles,
        "topline_note": fc["aggregate_commentary"],
        "stress": stress,
        "headline": [row(r) for r in fc["headline"]],
        "archetypes": fc["archetypes"],
        "chains": fc["chains"][:10],
        "chain_note": fc["chain_commentary"],
        "pairs": fc["pairs"],
        "sensitivity": fc["sensitivity"],
        "disagreement": fc["disagreement"],
        "continuous": [
            {
                "name": c["name"], "unit": c["unit"], "current": sig(c["current"]),
                "q2031": [sig(v) for v in c["q2031"]],
                "q2036": [sig(v) for v in c["q2036"]],
            }
            for c in fc["continuous"]
        ],
        "domains": domains,
        "limits": fc["limits"],
    }


def _pct(x: float) -> str:
    v = x * 100
    if v >= 99.5:
        return ">99%"
    if v < 0.5:
        return "<0.5%"
    if v < 10:
        return f"{v:.1f}%"
    return f"{v:.0f}%"


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "output" / "forecast.json"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "output" / "forecast.html"
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 20260729

    fc = json.loads(src.read_text())
    payload = build(fc, seed)
    html = TEMPLATE.read_text().replace(
        "__DATA__", json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")
    )
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html)
    print(f"wrote {dst} ({len(html)/1024:.0f} KB)")


if __name__ == "__main__":
    main()

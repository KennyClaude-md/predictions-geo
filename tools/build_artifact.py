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

    t9 = agg["tiers"]["ge9"]
    t6 = agg["tiers"]["ge6"]
    tiles = [
        {
            "label": "Order-changing events",
            "value": f"{t9['expected']:.1f}",
            "sub": f"expected count through 2036 across the {t9['n_nodes']} nodes rated "
                   f"9 or 10 out of 10 for global impact",
        },
        {
            "label": "A decade with none of them",
            "value": _pct(t9["p_zero"]),
            "sub": "probability nothing in that top tier fires at all — the quiet case is a "
                   "tail outcome, not the base case",
        },
        {
            "label": "Two or more at once",
            "value": _pct(t9["p_ge_2"]),
            "sub": f"three or more: {_pct(t9['p_ge_3'])} — the compound case, where the "
                   f"coupling structure dominates the individual probabilities",
        },
        {
            "label": "Notable disruptions",
            "value": f"{t6['expected']:.0f}",
            "sub": f"the broader 6+/10 band, out of {t6['n_nodes']} nodes — wide enough to "
                   f"hold both a US recession and a Taiwan contingency",
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
        "caption": _stress_caption(st),
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
        "severity_note": fc.get("severity_note", ""),
        "tiers": [
            {
                "label": f"{thr}+ / 10",
                "n_nodes": agg["tiers"][f"ge{thr}"]["n_nodes"],
                "expected": agg["tiers"][f"ge{thr}"]["expected"],
                "median": agg["tiers"][f"ge{thr}"]["deciles"][2],
                "p_zero": agg["tiers"][f"ge{thr}"]["p_zero"],
                "p_ge_2": agg["tiers"][f"ge{thr}"]["p_ge_2"],
                "p_ge_3": agg["tiers"][f"ge{thr}"]["p_ge_3"],
            }
            for thr in (6, 7, 8, 9)
        ],
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


def _stress_caption(st: dict) -> str:
    """Describe the trajectory this run actually produced, not a remembered one."""
    p50, p95, p5 = st["p50"], st["p95"], st["p5"]
    peak_i = max(range(len(p50)), key=lambda i: p50[i])
    peak_q = st["labels"][peak_i].split(" ")[0]
    spread_early = p95[min(8, len(p95) - 1)] - p5[min(8, len(p5) - 1)]
    spread_late = p95[-1] - p5[-1]
    shape = (
        "widens through the decade, so the further out you look the more the outcome "
        "depends on which world you are in"
        if spread_late > spread_early * 1.05
        else "narrows after the early years — not because the future gets more "
        "predictable, but because every node fires at most once, so the pool of "
        "un-fired risk depletes"
    )
    return (
        f"Index units are impact-weighted and decay-discounted, so the level means "
        f"nothing in isolation — only relative to itself. The median peaks around "
        f"{peak_q}. The 5th-to-95th spread {shape}."
    )


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

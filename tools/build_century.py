#!/usr/bin/env python3
"""Assemble the 100-year hazard timeline from the elicitation journal.

Reads the five hazard families and the audit, applies the audit's nesting
findings so subsets are not counted alongside the supersets that contain them,
computes per-hazard probability curves and century aggregates, and writes both a
markdown report and the JSON the page renders from.

    python tools/build_century.py <journal.jsonl>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from worldsim.century import (  # noqa: E402
    HORIZON_YEARS,
    START_YEAR,
    aggregate,
    by_decade,
    maximal_antichain,
    parse,
    probability_curve,
)

ROOT = Path(__file__).resolve().parent.parent

CATEGORY_LABEL = {
    "nuclear": "Nuclear",
    "geophysical": "Geophysical",
    "space": "Space & solar",
    "climate": "Climate & Earth systems",
    "biological": "Biological",
    "technological": "Technological",
    "societal": "Societal & conflict",
    "ecological": "Ecological",
}

WARNING_LABEL = {
    "none": "none", "minutes": "minutes", "hours": "hours", "days": "days",
    "months": "months", "years": "years", "decades": "decades",
}


def pct(x: float) -> str:
    v = x * 100
    if v >= 99.5:
        return ">99%"
    if v < 0.1:
        return "<0.1%"
    if v < 10:
        return f"{v:.1f}%"
    return f"{v:.0f}%"


def interval(years: float) -> str:
    """Human-readable recurrence interval."""
    if years < 1:
        return f"{years * 12:.0f} months"
    if years < 1000:
        return f"{years:,.0f} yr"
    if years < 1_000_000:
        return f"{years / 1000:,.0f}k yr"
    return f"{years / 1_000_000:,.1f}M yr"


def load(journal: Path) -> tuple[list, dict]:
    families, audit = [], {}
    for line in journal.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("type") != "result":
            continue
        r = rec.get("result")
        if not isinstance(r, dict):
            continue
        if "rate_corrections" in r:
            audit = r
        elif "hazards" in r:
            families.append(r)
    return families, audit


def main() -> None:
    journal = Path(sys.argv[1])
    families, audit = load(journal)
    if not families:
        raise SystemExit(f"no hazard families in {journal}")

    hazards = []
    for f in families:
        hazards.extend(parse(f["hazards"], family=str(f.get("family", ""))))
    print(f"{len(hazards)} hazards across {len(families)} families")

    # Apply the auditor's rate corrections before anything is computed from them.
    corrections = {c["id"]: c for c in (audit.get("rate_corrections") or [])}
    if corrections:
        fixed = []
        for h in hazards:
            c = corrections.get(h.id)
            if c and c.get("suggested_recurrence"):
                from dataclasses import replace

                lo, hi = h.recurrence_low, h.recurrence_high
                scale = float(c["suggested_recurrence"]) / max(h.recurrence, 1e-9)
                h = replace(
                    h,
                    recurrence=float(c["suggested_recurrence"]),
                    recurrence_low=lo * scale,
                    recurrence_high=hi * scale,
                )
            fixed.append(h)
        hazards = fixed
        print(f"applied {len(corrections)} auditor rate corrections")

    nested = [
        {"ids": g.get("ids", []), "keep": (g.get("ids") or [None])[0]}
        for g in (audit.get("double_counting") or [])
        if len(g.get("ids") or []) > 1
    ]
    # The auditor names the group; the broadest member is the one to keep, and
    # that is the one with the largest expected occurrence rate.
    by_id = {h.id: h for h in hazards}
    for g in nested:
        present = [i for i in g["ids"] if i in by_id]
        if present:
            g["ids"] = present
            g["keep"] = min(present, key=lambda i: by_id[i].recurrence)
    exclude = maximal_antichain(hazards, nested)
    print(f"nesting: {len(nested)} groups, {len(exclude)} hazards excluded from aggregates")

    rng = np.random.default_rng(20260729)
    rows = []
    for h in sorted(hazards, key=lambda h: -h.deaths_log10):
        curve = probability_curve(h, rng)
        rows.append(
            {
                "id": h.id, "category": h.category, "category_label":
                    CATEGORY_LABEL.get(h.category, h.category),
                "name": h.name, "criteria": h.criteria,
                "recurrence": h.recurrence, "recurrence_text": interval(h.recurrence),
                "recurrence_low": h.recurrence_low, "recurrence_high": h.recurrence_high,
                "trend": h.trend, "severity": h.severity,
                "deaths_log10": h.deaths_log10,
                "deaths_text": f"~10^{h.deaths_log10:.0f}",
                "warning": WARNING_LABEL.get(h.warning_time, h.warning_time),
                "anthropogenic": h.anthropogenic, "reversibility": h.reversibility,
                "evidence": h.evidence, "confidence": h.confidence,
                "counted": h.counted, "note": h.note,
                "nested_under": next(
                    (g["keep"] for g in nested if h.id in g["ids"] and h.id != g["keep"]),
                    None,
                ),
                **{k: curve[k] for k in
                   ("decades", "mean", "lo", "hi", "p_century", "p_century_lo",
                    "p_century_hi", "expected_count_century")},
            }
        )

    agg = aggregate(hazards, rng, exclude=exclude)
    timeline = by_decade(hazards, exclude=exclude)

    out = {
        "as_of": "2026-07-29",
        "start_year": START_YEAR,
        "horizon_years": HORIZON_YEARS,
        "hazards": rows,
        "aggregate": agg,
        "timeline": timeline,
        "categories": sorted({h.category for h in hazards}),
        "audit": {
            "verdict": audit.get("verdict", "unknown"),
            "headline": audit.get("headline", ""),
            "counted_vs_judged": audit.get("well_vs_poorly_constrained", ""),
            "caveats": audit.get("century_caveats", []),
            "double_counting": audit.get("double_counting", []),
        },
        "family_notes": [
            {"family": f.get("family"), "method": f.get("method_note", ""),
             "saturation": f.get("saturation_notes", [])}
            for f in families
        ],
        "n_counted": sum(1 for r in rows if r["counted"]),
        "n_judged": sum(1 for r in rows if not r["counted"]),
    }

    dst = ROOT / "output" / "century.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(out, indent=2))
    print(f"wrote {dst}")

    _report(out, ROOT / "output" / "century_timeline.md")
    print(f"wrote {ROOT / 'output' / 'century_timeline.md'}")

    t = agg["tiers"]
    print()
    print(f"  expected deaths this century (order of magnitude): "
          f"10^{agg['expected_deaths_log10']:.1f}")
    for k, v in t.items():
        print(f"  {k:22s} P(>=1) {pct(v['p_at_least_one']):>6}  "
              f"E[events] {v['expected_events']:.2f}  ({v['n_hazards']} hazards)")


def _report(d: dict, path: Path) -> None:
    L: list[str] = []
    w = L.append
    a = d["aggregate"]

    w("# A hundred-year disaster timeline, 2026–2126")
    w("")
    w(f"**{len(d['hazards'])} hazards** across {len(d['categories'])} categories. "
      f"Rates, not cumulative probabilities — see the note below on why.")
    w("")
    w("---")
    w("")
    w("## How to read this")
    w("")
    w("The primary number for every hazard is its **recurrence interval**: the mean "
      "years between occurrences at present conditions. Probabilities are derived "
      "from it, not elicited directly.")
    w("")
    w("That choice is forced. Over a century, *P(at least once)* saturates toward "
      "certainty for anything with a steady hazard and stops carrying information — "
      "a companion audit on this project measured the register's discriminating "
      "variance **falling** as its window lengthened. A rate does not degrade that "
      "way: \"once per 340 years\" means the same thing over any window.")
    w("")
    w(f"**{d['n_counted']} of {len(d['hazards'])} rates rest on a counted record** "
      f"— asteroid flux, megathrust paleoseismology, pandemics since 1600. The other "
      f"{d['n_judged']} are judgement with a number attached. Both are in the table; "
      f"the *Basis* column tells you which is which, and you should read a judged "
      f"rate as an order of magnitude at best.")
    w("")

    w("## The century in aggregate")
    w("")
    w("| Threshold | Hazards | Expected events | P(at least one) | P(two or more) |")
    w("|---|---:|---:|---:|---:|")
    names = {
        "mass_casualty_1e4": "≥10,000 deaths",
        "catastrophe_1e6": "≥1 million deaths",
        "global_1e7": "≥10 million deaths",
        "civilisational_1e8": "≥100 million deaths",
    }
    for k, label in names.items():
        t = a["tiers"][k]
        w(f"| **{label}** | {t['n_hazards']} | {t['expected_events']:.2f} | "
          f"{pct(t['p_at_least_one'])} | {pct(t['p_two_or_more'])} |")
    w("")
    w(f"Nesting removed **{a['n_excluded_as_nested']}** hazards from these totals — "
      f"a regional nuclear war is a subset of \"any nuclear detonation in anger\", not "
      f"a separate event, and summing them would double-count. Excluded hazards keep "
      f"their own rows below.")
    w("")

    w("## Timeline: expected occurrences per decade")
    w("")
    cats = [c for c in d["categories"]]
    w("| Decade | " + " | ".join(CATEGORY_LABEL.get(c, c) for c in cats) + " | Total |")
    w("|---" * (len(cats) + 2) + "|")
    for row in d["timeline"]:
        cells = " | ".join(f"{row.get(c, 0):.2f}" for c in cats)
        w(f"| **{row['start']}s** | {cells} | **{row['total']:.2f}** |")
    w("")
    w("Rising totals are not an artefact — several hazard classes carry an explicit "
      "upward rate trend across the century, and the table integrates it.")
    w("")

    for cat in cats:
        rows = [h for h in d["hazards"] if h["category"] == cat]
        if not rows:
            continue
        w(f"## {CATEGORY_LABEL.get(cat, cat)}")
        w("")
        w("| Hazard | Recurrence | P(by 2126) | 90% band | Deaths | Warning | Basis |")
        w("|---|---:|---:|:---:|---:|---|---|")
        for h in sorted(rows, key=lambda r: -r["p_century"]):
            star = " ⁽ⁿ⁾" if h["nested_under"] else ""
            w(f"| {h['name']}{star} | {h['recurrence_text']} | "
              f"**{pct(h['p_century'])}** | {pct(h['p_century_lo'])}–{pct(h['p_century_hi'])} | "
              f"{h['deaths_text']} | {h['warning']} | "
              f"{'counted' if h['counted'] else 'judged'} |")
        w("")
        w("<details><summary>Resolution criteria and evidence</summary>")
        w("")
        for h in sorted(rows, key=lambda r: -r["p_century"]):
            w(f"- **{h['name']}** — {h['criteria']}")
            w(f"  - *Basis:* {h['evidence']}")
        w("")
        w("</details>")
        w("")

    w("## What the auditor said")
    w("")
    w(f"**Verdict: {d['audit']['verdict']}**")
    w("")
    w(d["audit"]["headline"])
    w("")
    if d["audit"]["counted_vs_judged"]:
        w("### Counted versus judged")
        w("")
        w(d["audit"]["counted_vs_judged"])
        w("")
    if d["audit"]["caveats"]:
        w("### Caveats")
        w("")
        for c in d["audit"]["caveats"]:
            w(f"- {c}")
        w("")

    path.write_text("\n".join(L))


if __name__ == "__main__":
    main()

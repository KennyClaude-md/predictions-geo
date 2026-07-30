#!/usr/bin/env python3
"""Merge an additional research domain into the register.

Used to add the Israel / Levant sub-domain after the main nine had already been
parameterised, coupled and red-teamed. The domain's own coupling edges are folded
into the shared coupling block, and any edge referencing a node that does not
exist is dropped loudly rather than silently — a new domain is exactly where
id drift shows up.

    python tools/integrate_domain.py <domain.json> [world_model.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    dom_path = Path(sys.argv[1])
    model_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("params/world_model.json")

    dom = json.loads(dom_path.read_text())
    model = json.loads(model_path.read_text())

    key = "israel" if "israel" in str(dom.get("domain", "")).lower() else (
        dom_path.stem.replace("_domain", "")
    )

    known = set()
    for d in model["domains"]:
        for r in (d.get("research") or {}).get("discrete_risks", []) or []:
            known.add(str(r.get("id")))
        for m in ((d.get("calibration") or {}).get("missing_risks") or []):
            known.add(str(m.get("id")))

    existing = [d for d in model["domains"] if d.get("domain") == key]
    if existing:
        model["domains"] = [d for d in model["domains"] if d.get("domain") != key]
        print(f"  replacing existing '{key}' domain")

    new_ids = {str(r["id"]) for r in dom["discrete_risks"]}
    clash = new_ids & known
    if clash:
        print(f"  WARNING id clash with the existing register: {sorted(clash)}")

    model["domains"].append(
        {
            "domain": key,
            "title": str(dom.get("domain", key)),
            "research": {
                k: v for k, v in dom.items() if k != "coupling_edges"
            },
            # No calibration audit was run for this domain; say so rather than
            # letting a missing key imply a clean bill of health.
            "calibration": None,
        }
    )

    # Fold the domain's own edges into the shared coupling block.
    coupling = model.setdefault("coupling", {})
    edges = coupling.setdefault("conditional_edges", [])
    before = len(edges)
    valid = known | new_ids
    kept, dropped = 0, []
    for e in dom.get("coupling_edges") or []:
        s, t = str(e.get("source_id")), str(e.get("target_id"))
        if s in valid and t in valid and s != t:
            edges.append(e)
            kept += 1
        else:
            dropped.append(f"{s} -> {t}")

    model["risk_count"] = sum(
        len((d.get("research") or {}).get("discrete_risks", []) or [])
        for d in model["domains"]
    )
    model_path.write_text(json.dumps(model, indent=2))

    print(f"wrote {model_path}")
    print(f"  domain '{key}': {len(dom['discrete_risks'])} risks, "
          f"{len(dom.get('continuous_variables') or [])} indicators")
    print(f"  edges: {before} -> {len(edges)}  (kept {kept}, dropped {len(dropped)})")
    for d in dropped:
        print(f"    dropped (unknown node): {d}")
    print(f"  register total: {model['risk_count']} research risks across "
          f"{len(model['domains'])} domains")


if __name__ == "__main__":
    main()

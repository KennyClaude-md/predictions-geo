#!/usr/bin/env python3
"""Assemble params/world_model.json from a research workflow's journal.

The workflow writes one JSON line per completed agent. Reading the journal
directly — rather than only the workflow's final return value — means a run that
dies partway through is still worth something: whatever agents finished are
recovered and the simulation runs on the domains that landed.

    python tools/collect_workflow.py <journal.jsonl> [out.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Maps the analysts' prose domain titles back to the short keys the engine uses.
DOMAIN_KEYS = {
    "great-power": "geopolitics",
    "geopolit": "geopolitics",
    "climate": "climate",
    "macroecon": "economy",
    "economy": "economy",
    "ai,": "ai",
    "compute": "ai",
    "energy": "energy",
    "demograph": "demographics",
    "pandemic": "health",
    "health": "health",
    "political stability": "politics",
    "governance": "politics",
    "food": "foodwater",
    "water": "foodwater",
}


def domain_key(title: str, risks: list) -> str:
    """Prefer the id prefix the analyst actually used; fall back to the title."""
    for r in risks:
        rid = str(r.get("id", ""))
        if "_" in rid:
            head = rid.split("_")[0]
            if head in set(DOMAIN_KEYS.values()):
                return head
    low = title.lower()
    for frag, key in DOMAIN_KEYS.items():
        if frag in low:
            return key
    return "unknown"


def classify(result: dict) -> str:
    if "discrete_risks" in result:
        return "research"
    if "adjustments" in result or "coherence_violations" in result:
        return "calibration"
    if "conditional_edges" in result:
        return "coupling"
    if "specific_corrections" in result:
        return "redteam"
    return "unknown"


def main() -> None:
    journal = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("params/world_model.json")

    research: dict[str, dict] = {}
    calibration: dict[str, dict] = {}
    coupling: dict = {}
    redteam: list[dict] = []

    for line in journal.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("type") != "result":
            continue
        r = rec.get("result")
        if not isinstance(r, dict):
            continue
        kind = classify(r)
        if kind == "research":
            key = domain_key(str(r.get("domain", "")), r.get("discrete_risks", []))
            research[key] = r
        elif kind == "calibration":
            key = str(r.get("domain", "")).strip().lower()
            if key not in research:
                key = domain_key(key, [])
            calibration[key] = r
        elif kind == "coupling":
            coupling = r
        elif kind == "redteam":
            redteam.append(r)

    domains = []
    for key, res in research.items():
        domains.append(
            {
                "domain": key,
                "title": res.get("domain", key),
                "research": res,
                "calibration": calibration.get(key),
            }
        )

    payload = {
        "as_of": "2026-07-29",
        "domains": domains,
        "coupling": coupling,
        "redteam": redteam,
        "risk_count": sum(len(d["research"].get("discrete_risks", [])) for d in domains),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2))

    print(f"wrote {out}")
    print(f"  domains     : {len(domains)} ({', '.join(sorted(research))})")
    print(f"  calibrations: {len(calibration)}")
    print(f"  risks       : {payload['risk_count']}")
    print(f"  edges       : {len(coupling.get('conditional_edges', []) or [])}")
    print(f"  latents     : {len(coupling.get('latent_factors', []) or [])}")
    print(f"  redteam     : {len(redteam)}")


if __name__ == "__main__":
    main()

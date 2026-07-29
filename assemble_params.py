#!/usr/bin/env python3
"""Collect domain parameter sets from the intelligence fleets into params/.

Two fleets run concurrently over overlapping domain lists, so a domain may be
produced twice. This picks the better version per domain and reports what is
still missing, which is what gates the integrator step.

Preference order, highest first:
  1. audited     -- an adversarial critic rewrote it (its reasoning carries
                    [AUDIT: ...] markers). This is the version whose arithmetic
                    has been rechecked and whose facts have been spot-searched.
  2. more events -- a richer parameter set, all else equal
  3. newer       -- later mtime breaks remaining ties
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SCRATCH = Path("/tmp/claude-0/-home-user-predictions-geo/"
               "4ef724a0-1ef7-5686-a134-b384c2ebb707/scratchpad")
SOURCES = [SCRATCH / "geosim", SCRATCH / "geosim_b"]

EXPECTED = ["powers", "eurasia", "mideast", "climate", "macro", "ai_tech",
            "demog_health", "energy_res", "governance"]

REQUIRED_KEYS = ["domain", "indicators", "events", "couplings"]


def audited(d: dict) -> bool:
    return any("[AUDIT" in (e.get("reasoning") or "") for e in d.get("events", []))


def score(path: Path) -> tuple:
    try:
        d = json.loads(path.read_text())
    except Exception:
        return (-1, -1, -1)
    if any(k not in d for k in REQUIRED_KEYS):
        return (-1, -1, -1)
    if not d.get("indicators") or not d.get("events"):
        return (-1, -1, -1)
    return (int(audited(d)), len(d["events"]), path.stat().st_mtime)


def main() -> None:
    out = ROOT / "params"
    out.mkdir(exist_ok=True)
    found, missing = {}, []

    for dom in EXPECTED:
        cands = [s / f"domain_{dom}.json" for s in SOURCES]
        cands = [c for c in cands if c.exists() and score(c)[0] >= 0]
        if not cands:
            missing.append(dom)
            continue
        best = max(cands, key=score)
        s = score(best)
        shutil.copy(best, out / f"domain_{dom}.json")
        d = json.loads(best.read_text())
        found[dom] = {
            "source": best.parent.name,
            "audited": bool(s[0]),
            "indicators": len(d["indicators"]),
            "events": len(d["events"]),
            "couplings": len(d.get("couplings", [])),
        }

    for dom, i in found.items():
        flag = "audited" if i["audited"] else "RAW    "
        print(f"  {flag}  {dom:14s} {i['indicators']:>3d} ind  {i['events']:>3d} ev  "
              f"{i['couplings']:>3d} coup   [{i['source']}]")
    if missing:
        print(f"\n  missing: {', '.join(missing)}")

    n_aud = sum(1 for i in found.values() if i["audited"])
    print(f"\n{len(found)}/{len(EXPECTED)} domains present, {n_aud} audited")
    print(f"totals: {sum(i['indicators'] for i in found.values())} indicators, "
          f"{sum(i['events'] for i in found.values())} events")

    cf = out / "coupling.json"
    print(f"coupling.json: {'present' if cf.exists() else 'MISSING (run the integrator)'}")
    sys.exit(0 if not missing else 1)


if __name__ == "__main__":
    main()

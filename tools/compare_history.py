#!/usr/bin/env python3
"""Put the forward stress index, the July 2026 baseline, and WW2 on one axis.

Reads the back-cast workflow's journal, computes each series with the forward
run's own decay kernel, and prints the comparison together with the audit's
caveats — which are not decoration. The number this produces is a ratio between
one measured series and two elicited ones, and it is quotable enough to be
misused.

    python tools/compare_history.py <backcast_journal.jsonl> [forecast.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from worldsim.backcast import (  # noqa: E402
    contributions,
    parse_events,
    peak,
    quarter_index,
    trajectory,
    value_at,
)

BASELINE_QUARTER = "2026Q3"


def load_journal(path: Path) -> dict:
    out: dict[str, dict] = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("type") != "result":
            continue
        r = rec.get("result")
        if not isinstance(r, dict):
            continue
        if "reconciled_events" in r:
            out["audit"] = r
        elif "events" in r:
            era = str(r.get("era", "")).lower()
            key = "baseline" if "baseline" in era or "2026" in era else f"ww2_{len(out)}"
            out[key] = r
    return out


def main() -> None:
    journal = Path(sys.argv[1])
    fc_path = (
        Path(sys.argv[2]) if len(sys.argv) > 2
        else Path(__file__).resolve().parent.parent / "output" / "forecast.json"
    )
    data = load_journal(journal)
    audit = data.get("audit")
    baseline_set = data.get("baseline")

    if not audit or not baseline_set:
        print(f"incomplete journal: have {sorted(data)}")
        return

    # --- WW2, from the reconciled list ---
    ww2 = parse_events(audit["reconciled_events"])
    lo = min(e.onset_quarter for e in ww2)
    hi = max(e.onset_quarter for e in ww2) + 24
    ww2_peak, ww2_peak_q = peak(ww2, lo, hi)

    # --- current baseline ---
    base = parse_events(baseline_set["events"])
    base_now = value_at(base, BASELINE_QUARTER)

    # --- forward simulation ---
    fc = json.loads(fc_path.read_text())
    st = fc["stress_trajectory"]
    fwd_peak_med = max(st["p50"])
    fwd_peak_q = st["labels"][st["p50"].index(fwd_peak_med)].split()[0]
    fwd_peak_p95 = max(st["p95"])
    fwd_end_med = st["p50"][-1]

    print("=" * 78)
    print("GLOBAL SYSTEMIC STRESS INDEX — three series, one kernel")
    print("=" * 78)
    print()
    print(f"  {'series':<52} {'index':>8}  {'when':>8}")
    print(f"  {'-'*52} {'-'*8}  {'-'*8}")
    print(f"  {'Current baseline (already-live stressors)':<52} {base_now:8.1f}  {BASELINE_QUARTER:>8}")
    print(f"  {'Forward sim, median peak (NEW events only)':<52} {fwd_peak_med:8.1f}  {fwd_peak_q:>8}")
    print(f"  {'Forward sim, 95th-pct peak (NEW events only)':<52} {fwd_peak_p95:8.1f}  {fwd_peak_q:>8}")
    print(f"  {'Forward sim, median at end of horizon':<52} {fwd_end_med:8.1f}  {'2036Q4':>8}")
    print(f"  {'WW2 era, back-cast peak':<52} {ww2_peak:8.1f}  {ww2_peak_q:>8}")
    print()
    print("  Baseline-inclusive forward totals (adding the decayed 2026 baseline):")
    b_at = {}
    for lab in ("2029Q3", "2031Q4", "2036Q4"):
        b_at[lab] = value_at(base, lab)
    print(f"    median peak + baseline  ~ {fwd_peak_med + b_at['2029Q3']:.0f}")
    print(f"    95th pct peak + baseline ~ {fwd_peak_p95 + b_at['2029Q3']:.0f}")
    print()
    print(f"  RATIOS vs WW2 peak ({ww2_peak:.0f}):")
    print(f"    current baseline            {base_now / ww2_peak * 100:5.1f}%")
    print(f"    forward median peak         {(fwd_peak_med + b_at['2029Q3']) / ww2_peak * 100:5.1f}%")
    print(f"    forward 95th-pct peak       {(fwd_peak_p95 + b_at['2029Q3']) / ww2_peak * 100:5.1f}%")
    print()

    print("-" * 78)
    print(f"CURRENT BASELINE COMPOSITION at {BASELINE_QUARTER}  (total {base_now:.1f})")
    print("-" * 78)
    for name, val in contributions(base, BASELINE_QUARTER)[:14]:
        print(f"  {val:6.2f}  {name[:66]}")
    print()

    print("-" * 78)
    print(f"WW2 RECONCILED EVENT SET  ({len(ww2)} nodes, peak {ww2_peak:.0f} at {ww2_peak_q})")
    print("-" * 78)
    for e in sorted(ww2, key=lambda e: e.onset_quarter):
        from worldsim.backcast import quarter_label

        print(f"  {quarter_label(e.onset_quarter):>7}  sev {e.severity:4.1f}  {e.name[:56]}")
    print()
    print(f"  contributions at the peak quarter {ww2_peak_q}:")
    for name, val in contributions(ww2, ww2_peak_q)[:8]:
        print(f"    {val:6.2f}  {name[:62]}")
    print()

    print("-" * 78)
    print(f"AUDIT VERDICT: {audit['verdict']}")
    print("-" * 78)
    print(audit["granularity_assessment"][:1400])
    print()
    if audit.get("scale_warnings"):
        print("SCALE WARNINGS:")
        for w in audit["scale_warnings"]:
            print(f"  - {w}")
        print()
    print("COMPARABILITY CAVEATS:")
    for c in audit["comparability_caveats"]:
        print(f"  - {c}")

    # Machine-readable, for the report layer.
    out = {
        "baseline_quarter": BASELINE_QUARTER,
        "baseline_index": base_now,
        "baseline_events": [
            {"name": e.name, "onset": e.onset_quarter, "severity": e.severity} for e in base
        ],
        "forward_peak_median": fwd_peak_med,
        "forward_peak_p95": fwd_peak_p95,
        "forward_peak_quarter": fwd_peak_q,
        "forward_end_median": fwd_end_med,
        "ww2_peak": ww2_peak,
        "ww2_peak_quarter": ww2_peak_q,
        "ww2_events": [
            {"name": e.name, "onset": e.onset_quarter, "severity": e.severity} for e in ww2
        ],
        "verdict": audit["verdict"],
        "caveats": audit["comparability_caveats"],
        "scale_warnings": audit.get("scale_warnings", []),
    }
    dst = Path(__file__).resolve().parent.parent / "output" / "history_comparison.json"
    dst.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {dst}")


if __name__ == "__main__":
    main()

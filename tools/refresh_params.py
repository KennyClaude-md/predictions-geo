#!/usr/bin/env python3
"""Rebuild every derived parameter file from a research workflow journal.

Order matters: the risk register has to exist before anything can be classified
against it, and the calibration auditors add risks, so valence and duplicate
families must be regenerated after the audits land — not before.

    python tools/refresh_params.py <journal.jsonl>
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEPS = [
    ("collect_workflow.py", "risk register from the workflow journal"),
    ("classify_valence.py", "stabilising / ambiguous / destabilising"),
    ("stress_loadings.py", "indicator correlations with systemic stress"),
    ("duplicate_families.py", "one event enumerated across several domains"),
]


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: refresh_params.py <journal.jsonl>")
    journal = sys.argv[1]

    for script, what in STEPS:
        args = [sys.executable, str(ROOT / "tools" / script)]
        if script == "collect_workflow.py":
            args += [journal, str(ROOT / "params" / "world_model.json")]
        print(f"\n--- {script}  ({what})")
        res = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
        print(res.stdout.rstrip())
        if res.returncode != 0:
            print(res.stderr.rstrip())
            raise SystemExit(f"{script} failed")

    print("\nparameters refreshed. Run: python run_simulation.py")


if __name__ == "__main__":
    main()

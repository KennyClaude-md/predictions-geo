"""Putting the stress index on a historical axis.

The forward simulation's index starts at zero and only accumulates stress from
register events that fire during the run. That makes two natural questions
unanswerable as built:

  * what is the *current* level, given the world already has an active Iran
    conflict, a Hormuz blockade and the Ukraine war running on 2026-07-29?
  * how does any of it compare to a period we already know was catastrophic?

Both need the same index computed over an event set that isn't the register. This
module does exactly that, and imports the decay constant from `continuous`
rather than restating it — a back-cast on a different kernel would be worthless,
and the failure would be silent.

The hard part is not arithmetic, it is GRANULARITY. The register carries an entire
contingency as one node: a Chinese invasion of Taiwan is a single severity-10
entry, not separate entries for the landing, the air campaign, the blockade and
the semiconductor collapse. Decompose a historical war more finely than that and
the comparison inflates by construction. So the event sets this module consumes
are elicited under an explicit granularity constraint and audited for it, and the
audit's caveats travel with the number.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np

from .continuous import STRESS_DECAY_QUARTERS


@dataclass(frozen=True)
class HistoricalEvent:
    name: str
    onset_quarter: int  # absolute quarter index, see quarter_index()
    severity: float
    note: str = ""


def quarter_index(label: str) -> int:
    """Absolute quarter number from a 'YYYY-QN' or 'YYYYQN' label.

    Absolute rather than relative so 1939 and 2026 land on one axis and the decay
    arithmetic is identical for both.
    """
    m = re.match(r"^\s*(\d{4})\s*-?\s*[Qq]([1-4])\s*$", str(label))
    if not m:
        raise ValueError(f"unparseable quarter label: {label!r}")
    year, q = int(m.group(1)), int(m.group(2))
    return year * 4 + (q - 1)


def quarter_label(index: int) -> str:
    return f"{index // 4}Q{index % 4 + 1}"


def parse_events(items: list[dict]) -> list[HistoricalEvent]:
    out = []
    for it in items:
        try:
            oq = quarter_index(it.get("onset", ""))
        except ValueError:
            continue
        out.append(
            HistoricalEvent(
                name=str(it.get("name", "")),
                onset_quarter=oq,
                severity=float(it.get("severity_0_10") or 0.0),
                note=str(it.get("note") or it.get("ruler_comparison") or ""),
            )
        )
    return out


def trajectory(
    events: list[HistoricalEvent], start: int, end: int
) -> tuple[np.ndarray, list[str]]:
    """Index value per quarter over [start, end], same kernel as the forward run."""
    n = end - start + 1
    idx = np.zeros(n, dtype=np.float64)
    for t in range(n):
        q = start + t
        total = 0.0
        for e in events:
            age = q - e.onset_quarter
            if age >= 0:
                total += e.severity * np.exp(-age / STRESS_DECAY_QUARTERS)
        idx[t] = total
    return idx, [quarter_label(start + t) for t in range(n)]


def peak(events: list[HistoricalEvent], start: int, end: int) -> tuple[float, str]:
    idx, labels = trajectory(events, start, end)
    i = int(np.argmax(idx))
    return float(idx[i]), labels[i]


def value_at(events: list[HistoricalEvent], quarter: str) -> float:
    """Index at a single quarter — used for the current baseline."""
    q = quarter_index(quarter)
    return float(
        sum(
            e.severity * np.exp(-(q - e.onset_quarter) / STRESS_DECAY_QUARTERS)
            for e in events
            if q >= e.onset_quarter
        )
    )


def contributions(events: list[HistoricalEvent], quarter: str) -> list[tuple[str, float]]:
    """Per-event contribution at one quarter, largest first.

    Shows how much of a level is one fresh shock versus many decayed ones, which
    is the distinction the index exists to make.
    """
    q = quarter_index(quarter)
    rows = [
        (e.name, e.severity * float(np.exp(-(q - e.onset_quarter) / STRESS_DECAY_QUARTERS)))
        for e in events
        if q >= e.onset_quarter
    ]
    rows.sort(key=lambda r: -r[1])
    return rows

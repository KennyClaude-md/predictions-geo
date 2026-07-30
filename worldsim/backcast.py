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


# --------------------------------------------------------------------------
# Granularity-invariant measures
# --------------------------------------------------------------------------
#
# The summed index is NOT comparable across event sets of different size. It has
# to be said plainly because the failure is not subtle: the forward register
# carries 159 destabilising nodes totalling 1011 severity points, while the Second
# World War at register-matched coarseness is 17 nodes totalling 143. A sum over
# the former beats a sum over the latter by construction, and the back-cast duly
# reports that July 2026 is 1.6x WW2 — which is false, and is a fact about the
# arithmetic rather than about the world.
#
# What survives a change of granularity:
#
#   worst_active   the single highest decayed severity live at a moment. Splitting
#                  one node into three does not change it.
#   concurrent(s)  how many events of severity >= s are still live. Robust as long
#                  as both sides enumerate at similar coarseness *for that tier*,
#                  which the high tiers do.
#   top_k          the summed index restricted to the k highest-severity nodes,
#                  with k matched across the sets being compared. This is the
#                  closest thing to a like-for-like sum.


def worst_active(events: list[HistoricalEvent], quarter: str) -> float:
    """Highest decayed severity live at `quarter`. Invariant to node splitting."""
    q = quarter_index(quarter)
    vals = [
        e.severity * float(np.exp(-(q - e.onset_quarter) / STRESS_DECAY_QUARTERS))
        for e in events
        if q >= e.onset_quarter
    ]
    return max(vals) if vals else 0.0


def concurrent_above(
    events: list[HistoricalEvent], quarter: str, min_severity: float, live_floor: float = 0.5
) -> int:
    """Count events of severity >= min_severity still 'live' at `quarter`.

    Live means the decay factor has not yet fallen below `live_floor` — by default
    within about 7.6 quarters of onset. Counting concurrency rather than summing
    severity is what makes this comparable across registers of different size.
    """
    q = quarter_index(quarter)
    n = 0
    for e in events:
        if e.severity < min_severity or q < e.onset_quarter:
            continue
        if np.exp(-(q - e.onset_quarter) / STRESS_DECAY_QUARTERS) >= live_floor:
            n += 1
    return n


def top_k_events(events: list[HistoricalEvent], k: int) -> list[HistoricalEvent]:
    """The k highest-severity events, for a count-matched comparison."""
    return sorted(events, key=lambda e: -e.severity)[:k]


def profile(events: list[HistoricalEvent], start: int, end: int, k: int) -> dict:
    """All four measures over a window, reported at the peak of each."""
    idx, labels = trajectory(events, start, end)
    top = top_k_events(events, k)
    idx_k, _ = trajectory(top, start, end)

    worst = [worst_active(events, lab) for lab in labels]
    conc8 = [concurrent_above(events, lab, 8.0) for lab in labels]
    conc9 = [concurrent_above(events, lab, 9.0) for lab in labels]

    i_sum, i_k, i_w, i_c = (
        int(np.argmax(idx)), int(np.argmax(idx_k)), int(np.argmax(worst)), int(np.argmax(conc8))
    )
    return {
        "sum_peak": float(idx[i_sum]), "sum_peak_at": labels[i_sum],
        "topk_peak": float(idx_k[i_k]), "topk_peak_at": labels[i_k], "k": k,
        "worst_active_peak": float(worst[i_w]), "worst_active_at": labels[i_w],
        "concurrent8_peak": int(max(conc8)), "concurrent8_at": labels[i_c],
        "concurrent9_peak": int(max(conc9)),
        "n_events": len(events),
        "severity_mass": float(sum(e.severity for e in events)),
    }

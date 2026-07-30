"""Simulation clock, parameterised by horizon.

The model runs on a quarterly grid anchored at 2026-07-01. Quarterly is a
deliberate compromise: fine enough that cascade lags (a blockade in Q1 hitting
chip supply by Q3) are representable, coarse enough that a large path count
finishes in minutes.

Elicitation anchors land on exact quarter boundaries by design, which is why
analysts were asked for cumulative probabilities at end-2027 / end-2031 / end-2036
(and, for the long horizon, end-2046 / end-2056) rather than round year counts.

The active horizon is module state with one explicit setter. That is a deliberate
choice over threading a config object through six modules: every consumer reads
it through a function call rather than importing a constant, so there is no
stale-import failure mode, and `use_horizon()` doubles as a context manager so a
test can switch horizons without leaking into the next one.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field

START_YEAR = 2026
START_QUARTER = 3  # 2026Q3 is the first simulated period
YEARS_PER_QUARTER = 0.25


@dataclass(frozen=True)
class Horizon:
    """One simulation horizon: its length and its elicitation anchors."""

    name: str
    n_quarters: int
    # Elicitation field name -> quarter index (1-based, = quarters elapsed).
    anchors: dict[str, int] = field(default_factory=dict)

    @property
    def anchor_quarters(self) -> list[int]:
        return sorted(self.anchors.values())

    @property
    def anchor_fields(self) -> list[str]:
        return [f for f, _ in sorted(self.anchors.items(), key=lambda kv: kv[1])]

    @property
    def n_segments(self) -> int:
        return len(self.anchors)

    def __post_init__(self) -> None:
        qs = self.anchor_quarters
        if qs and qs[-1] != self.n_quarters:
            raise ValueError(
                f"{self.name}: last anchor {qs[-1]} must equal n_quarters "
                f"{self.n_quarters}; the final segment has to end at the horizon"
            )
        if len(set(qs)) != len(qs):
            raise ValueError(f"{self.name}: duplicate anchor quarters {qs}")


HORIZON_2036 = Horizon(
    name="2036",
    n_quarters=42,  # 2026Q3 .. 2036Q4
    anchors={"p_by_2027_pct": 6, "p_by_2031_pct": 22, "p_by_2036_pct": 42},
)

HORIZON_2056 = Horizon(
    name="2056",
    n_quarters=122,  # 2026Q3 .. 2056Q4
    anchors={
        "p_by_2027_pct": 6,
        "p_by_2031_pct": 22,
        "p_by_2036_pct": 42,
        "p_by_2046_pct": 82,
        "p_by_2056_pct": 122,
    },
)

_active: Horizon = HORIZON_2036


def active() -> Horizon:
    return _active


def set_horizon(h: Horizon) -> None:
    global _active
    _active = h


@contextmanager
def use_horizon(h: Horizon):
    """Temporarily activate a horizon. Restores the previous one on exit."""
    global _active
    prev = _active
    _active = h
    try:
        yield h
    finally:
        _active = prev


def n_quarters() -> int:
    return _active.n_quarters


def anchor_quarters() -> list[int]:
    return _active.anchor_quarters


def anchor_fields() -> list[str]:
    return _active.anchor_fields


@dataclass(frozen=True)
class Quarter:
    year: int
    q: int

    @property
    def label(self) -> str:
        return f"{self.year}Q{self.q}"


def quarter_at(index: int) -> Quarter:
    """Quarter reached after `index` steps. index=0 is the pre-simulation state."""
    total = (START_YEAR * 4 + (START_QUARTER - 1)) + max(index - 1, 0)
    return Quarter(total // 4, total % 4 + 1)


def years_elapsed(index: int) -> float:
    return index * YEARS_PER_QUARTER


def horizon_label(index: int) -> str:
    q = quarter_at(index)
    return f"{q.label} (+{years_elapsed(index):.2f}y)"

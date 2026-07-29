"""Simulation clock.

The whole model runs on a quarterly grid anchored at 2026-07-01. Quarterly is a
deliberate compromise: fine enough that cascade lags (a blockade in Q1 hitting
chip supply by Q3) are representable, coarse enough that 480k paths finish in
minutes.

The three elicitation horizons land on exact quarter boundaries, which is why
the analysts were asked for cumulative probabilities at end-2027 / end-2031 /
end-2036 rather than round year counts.
"""

from __future__ import annotations

from dataclasses import dataclass

START_YEAR = 2026
START_QUARTER = 3  # 2026Q3 is the first simulated period
N_QUARTERS = 42  # 2026Q3 .. 2036Q4 inclusive
YEARS_PER_QUARTER = 0.25

# Quarter index (1-based, = number of quarters elapsed) of each elicitation anchor.
ANCHOR_QUARTERS = {
    "p_by_2027_pct": 6,  # end of 2027
    "p_by_2031_pct": 22,  # end of 2031
    "p_by_2036_pct": 42,  # end of 2036
}


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

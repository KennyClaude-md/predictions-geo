"""The historical back-cast must use the forward run's kernel, exactly."""

import numpy as np
import pytest

from worldsim.backcast import (
    HistoricalEvent,
    contributions,
    parse_events,
    peak,
    quarter_index,
    quarter_label,
    trajectory,
    value_at,
)
from worldsim.continuous import STRESS_DECAY_QUARTERS, systemic_stress


def test_quarter_labels_round_trip_across_centuries():
    for lab in ["1936Q1", "1939-Q3", "1945Q3", "2026Q3", "2036Q4"]:
        assert quarter_label(quarter_index(lab)) == lab.replace("-", "")
    assert quarter_index("1939Q4") - quarter_index("1939Q1") == 3
    assert quarter_index("2026Q1") - quarter_index("1939Q1") == 87 * 4


def test_rejects_unparseable_labels():
    with pytest.raises(ValueError):
        quarter_index("nineteen thirty nine")
    with pytest.raises(ValueError):
        quarter_index("1939Q5")


def test_backcast_kernel_matches_the_forward_simulation_exactly():
    """A back-cast on a different decay constant would be worthless, silently.

    Drives the forward engine's systemic_stress() and this module's trajectory()
    with the same single event and requires identical output.
    """
    sev = np.array([7.0], dtype=np.float32)
    fire = np.array([[3]], dtype=np.int8)  # fires at forward-quarter 3
    fwd = systemic_stress(fire, sev)[0]

    base = quarter_index("2026Q3")
    ev = [HistoricalEvent("x", base + 2, 7.0)]  # forward q3 == index 2 of the grid
    back, _ = trajectory(ev, base, base + len(fwd) - 1)

    assert np.allclose(fwd, back, atol=1e-4), "kernels diverge"


def test_simultaneity_dominates_count():
    """Four shocks in two years must outscore the same four spread over a decade."""
    b = quarter_index("1940Q1")
    together = [HistoricalEvent(f"e{i}", b + i * 2, 10.0) for i in range(4)]
    apart = [HistoricalEvent(f"e{i}", b + i * 10, 10.0) for i in range(4)]
    p_together, _ = peak(together, b, b + 60)
    p_apart, _ = peak(apart, b, b + 60)
    assert p_together > p_apart * 1.8


def test_decay_reaches_one_over_e_at_the_stated_horizon():
    b = quarter_index("2000Q1")
    ev = [HistoricalEvent("x", b, 10.0)]
    later = quarter_label(b + int(STRESS_DECAY_QUARTERS))
    assert value_at(ev, later) == pytest.approx(10.0 / np.e, rel=1e-6)


def test_events_before_the_window_still_contribute_decayed():
    """The current baseline is mostly old shocks that have not fully decayed."""
    ev = [HistoricalEvent("old", quarter_index("2022Q1"), 9.0)]
    v = value_at(ev, "2026Q3")
    assert 0 < v < 9.0
    assert v == pytest.approx(9.0 * np.exp(-18 / STRESS_DECAY_QUARTERS), rel=1e-6)


def test_contributions_rank_fresh_shocks_over_stale_ones():
    ev = [
        HistoricalEvent("stale big", quarter_index("2020Q1"), 10.0),
        HistoricalEvent("fresh small", quarter_index("2026Q2"), 5.0),
    ]
    rows = contributions(ev, "2026Q3")
    assert rows[0][0] == "fresh small"


def test_parse_events_skips_unparseable_rows_without_dying():
    got = parse_events([
        {"name": "ok", "onset": "1941Q2", "severity_0_10": 10},
        {"name": "bad", "onset": "sometime in 1941", "severity_0_10": 10},
    ])
    assert [e.name for e in got] == ["ok"]

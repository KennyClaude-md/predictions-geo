"""The hazard inversion has to be exactly right — everything else sits on it."""

import numpy as np
import pytest

from worldsim.hazard import (
    cumulative_from_quarter_hazard,
    isotonic_cumulative,
    piecewise_quarter_hazard,
)
from worldsim.timeline import (
    HORIZON_2036,
    HORIZON_2056,
    Horizon,
    active,
    anchor_quarters,
    use_horizon,
)


@pytest.mark.parametrize(
    "p",
    [
        (1.0, 5.0, 12.0),
        (0.2, 0.9, 2.0),
        (30.0, 62.0, 80.0),
        (85.0, 93.0, 97.0),
        (0.05, 0.1, 0.15),
        (12.0, 12.0, 12.0),
    ],
)
def test_roundtrip_hits_the_anchors_2036(p):
    """Fit a hazard to the anchor CDF points, recover those points."""
    with use_horizon(HORIZON_2036):
        h = piecewise_quarter_hazard(*p)
        cdf = cumulative_from_quarter_hazard(h)
        for target, q in zip(p, anchor_quarters()):
            assert cdf[q - 1] * 100 == pytest.approx(target, abs=0.05)


@pytest.mark.parametrize(
    "p",
    [
        (1.0, 5.0, 12.0, 25.0, 40.0),
        (0.2, 0.9, 2.0, 4.0, 6.0),
        (30.0, 62.0, 80.0, 92.0, 96.0),
        (58.0, 75.0, 91.0, 95.0, 97.0),
        (12.0, 12.0, 12.0, 12.0, 12.0),
        (5.0, 20.0, 35.0, 35.0, 35.0),  # window closes: no further hazard
    ],
)
def test_roundtrip_hits_the_anchors_2056(p):
    with use_horizon(HORIZON_2056):
        h = piecewise_quarter_hazard(*p)
        assert len(h) == 122
        cdf = cumulative_from_quarter_hazard(h)
        for target, q in zip(p, anchor_quarters()):
            assert cdf[q - 1] * 100 == pytest.approx(target, abs=0.05)


def test_wrong_anchor_count_is_an_error_not_a_silent_truncation():
    with use_horizon(HORIZON_2056):
        with pytest.raises(ValueError, match="expects 5 anchors"):
            piecewise_quarter_hazard(5.0, 20.0, 35.0)


def test_horizon_context_manager_restores_the_previous_horizon():
    before = active().name
    with use_horizon(HORIZON_2056):
        assert active().name == "2056"
    assert active().name == before


def test_horizon_rejects_a_final_anchor_that_misses_the_end():
    with pytest.raises(ValueError, match="must equal n_quarters"):
        Horizon(name="bad", n_quarters=100, anchors={"a": 6, "b": 42})


def test_non_monotone_input_is_repaired_not_crashed():
    a, b, c = isotonic_cumulative(40.0, 10.0, 60.0)
    assert a <= b <= c
    # Pooling the violating pair conserves their mean.
    assert (a + b) / 2 == pytest.approx(0.25, abs=1e-9)


def test_isotonic_handles_five_points_and_long_violating_runs():
    out = isotonic_cumulative(50.0, 40.0, 30.0, 60.0, 70.0)
    assert all(a <= b for a, b in zip(out, out[1:]))
    assert out[0] == pytest.approx(0.40, abs=1e-9)  # the 50/40/30 run pools to 40
    assert len(out) == 5


def test_extremes_are_clamped_inside_the_open_interval():
    h = piecewise_quarter_hazard(0.0, 0.0, 100.0)
    assert np.all(np.isfinite(h))
    assert np.all(h >= 0) and np.all(h < 1)


def test_hazard_is_piecewise_constant_across_segments():
    Q = anchor_quarters()
    h = piecewise_quarter_hazard(5.0, 30.0, 40.0)
    assert len(np.unique(np.round(h[: Q[0]], 12))) == 1
    assert len(np.unique(np.round(h[Q[0] : Q[1]], 12))) == 1
    assert len(np.unique(np.round(h[Q[1] : Q[2]], 12))) == 1
    # This example front-loads risk, so early hazard must exceed late hazard.
    assert h[0] > h[-1]


def test_flat_cumulative_after_first_anchor_gives_near_zero_later_hazard():
    Q = anchor_quarters()
    h = piecewise_quarter_hazard(20.0, 20.0, 20.0)
    assert h[Q[0] + 1] < 1e-6


def test_max_quarter_stops_a_horizon_locked_node_from_accruing_hazard():
    """A criterion tied to a 2027 event must not keep firing in the 2050s."""
    with use_horizon(HORIZON_2056):
        h = piecewise_quarter_hazard(60.0, 70.0, 74.0, 74.0, 74.0, max_quarter=22)
        assert np.all(h[22:] == 0.0)
        assert h[:22].sum() > 0
        cdf = cumulative_from_quarter_hazard(h)
        assert cdf[-1] == pytest.approx(cdf[21], abs=1e-12)

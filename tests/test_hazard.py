"""The hazard inversion has to be exactly right — everything else sits on it."""

import numpy as np
import pytest

from worldsim.hazard import (
    cumulative_from_quarter_hazard,
    isotonic_cumulative,
    piecewise_quarter_hazard,
)
from worldsim.timeline import ANCHOR_QUARTERS

Q = [ANCHOR_QUARTERS[k] for k in ("p_by_2027_pct", "p_by_2031_pct", "p_by_2036_pct")]


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
def test_roundtrip_hits_the_anchors(p):
    """Fit a hazard to three cumulative probabilities, recover those probabilities."""
    h = piecewise_quarter_hazard(*p)
    cdf = cumulative_from_quarter_hazard(h)
    for target, q in zip(p, Q):
        assert cdf[q - 1] * 100 == pytest.approx(target, abs=0.05)


def test_non_monotone_input_is_repaired_not_crashed():
    a, b, c = isotonic_cumulative(40.0, 10.0, 60.0)
    assert a <= b <= c
    # Pooling the violating pair conserves their mean.
    assert (a + b) / 2 == pytest.approx(0.25, abs=1e-9)


def test_extremes_are_clamped_inside_the_open_interval():
    h = piecewise_quarter_hazard(0.0, 0.0, 100.0)
    assert np.all(np.isfinite(h))
    assert np.all(h >= 0) and np.all(h < 1)


def test_hazard_is_piecewise_constant_across_the_three_segments():
    h = piecewise_quarter_hazard(5.0, 30.0, 40.0)
    assert len(np.unique(np.round(h[: Q[0]], 12))) == 1
    assert len(np.unique(np.round(h[Q[0] : Q[1]], 12))) == 1
    assert len(np.unique(np.round(h[Q[1] : Q[2]], 12))) == 1
    # This example front-loads risk, so early hazard must exceed late hazard.
    assert h[0] > h[-1]


def test_flat_cumulative_after_first_anchor_gives_near_zero_later_hazard():
    h = piecewise_quarter_hazard(20.0, 20.0, 20.0)
    assert h[Q[0] + 1] < 1e-6

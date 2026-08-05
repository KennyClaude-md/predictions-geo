"""Rate-based century arithmetic: the maths a 100-year table stands on."""

import numpy as np
import pytest

from worldsim.century import (
    HORIZON_YEARS,
    Hazard,
    aggregate,
    by_decade,
    maximal_antichain,
    parse,
    probability_curve,
)


def hz(**kw) -> Hazard:
    base = dict(
        id="x", category="geophysical", name="X", criteria="c",
        recurrence=100.0, recurrence_low=50.0, recurrence_high=200.0,
        trend="flat", severity=7.0, deaths_log10=6.0, warning_time="none",
        anthropogenic="natural", reversibility="recoverable_decades",
        evidence="counted geological record, n=12", confidence="high",
    )
    base.update(kw)
    return Hazard(**base)


def test_flat_rate_reproduces_the_poisson_survival_formula():
    """A once-per-century hazard is 63% over a century, not 100%."""
    h = hz(recurrence=100.0, trend="flat")
    assert h.cumulative_hazard(100) == pytest.approx(1.0)
    assert 1 - np.exp(-h.cumulative_hazard(100)) == pytest.approx(0.6321, abs=1e-3)
    # And half the window gives half the integrated hazard.
    assert h.cumulative_hazard(50) == pytest.approx(0.5)


def test_rare_hazards_do_not_saturate_over_a_century():
    """The whole reason for using rates: a 10,000-year event stays ~1%."""
    h = hz(recurrence=10_000.0, recurrence_low=5_000.0, recurrence_high=20_000.0)
    p = 1 - np.exp(-h.cumulative_hazard(HORIZON_YEARS))
    assert 0.005 < p < 0.02


def test_rising_trend_raises_the_integrated_hazard_and_falling_lowers_it():
    flat = hz(trend="flat").cumulative_hazard(HORIZON_YEARS)
    rising = hz(trend="rising_strongly").cumulative_hazard(HORIZON_YEARS)
    falling = hz(trend="falling_strongly").cumulative_hazard(HORIZON_YEARS)
    assert rising > flat > falling
    # Ramp is linear to 3x, so the century integral is the mean multiplier of 2x.
    assert rising == pytest.approx(flat * 2.0, rel=1e-6)


def test_trend_only_bites_late_in_the_window():
    """A ramp must not retroactively change the near-term rate."""
    flat, rising = hz(trend="flat"), hz(trend="rising_strongly")
    assert rising.cumulative_hazard(1) == pytest.approx(flat.cumulative_hazard(1), rel=0.02)
    assert rising.cumulative_hazard(100) > flat.cumulative_hazard(100) * 1.9


def test_wider_elicited_range_gives_a_wider_credible_band():
    rng = np.random.default_rng(4)
    tight = probability_curve(hz(recurrence_low=90.0, recurrence_high=110.0), rng)
    loose = probability_curve(hz(recurrence_low=20.0, recurrence_high=500.0), rng)
    assert (loose["p_century_hi"] - loose["p_century_lo"]) > \
           (tight["p_century_hi"] - tight["p_century_lo"]) * 2


def test_unknown_trend_widens_the_band_beyond_its_stated_range():
    rng = np.random.default_rng(5)
    known = probability_curve(hz(trend="flat"), rng)
    unknown = probability_curve(hz(trend="unknown"), rng)
    assert (unknown["p_century_hi"] - unknown["p_century_lo"]) > \
           (known["p_century_hi"] - known["p_century_lo"])


def test_nested_hazards_are_excluded_from_aggregates():
    """Summing 'any detonation', 'regional war' and 'strategic exchange' triple-counts."""
    hs = [
        hz(id="any_detonation", recurrence=60.0, deaths_log10=6.0),
        hz(id="regional_war", recurrence=200.0, deaths_log10=8.0),
        hz(id="strategic_exchange", recurrence=800.0, deaths_log10=9.0),
    ]
    nested = [{"ids": ["any_detonation", "regional_war", "strategic_exchange"],
               "keep": "any_detonation"}]
    drop = maximal_antichain(hs, nested)
    assert drop == {"regional_war", "strategic_exchange"}

    rng = np.random.default_rng(6)
    naive = aggregate(hs, rng, exclude=set(), n_draws=400)
    fixed = aggregate(hs, rng, exclude=drop, n_draws=400)
    assert fixed["tiers"]["catastrophe_1e6"]["expected_events"] < \
           naive["tiers"]["catastrophe_1e6"]["expected_events"]
    assert fixed["n_excluded_as_nested"] == 2


def test_counted_and_judged_evidence_are_distinguished():
    counted = hz(evidence="paleoseismic record, 11 events since 1700", confidence="high")
    judged = hz(evidence="expert elicitation; no historical instance", confidence="low")
    assert counted.counted is True
    assert judged.counted is False


def test_expected_deaths_are_summed_linearly_not_in_log_space():
    """One 1e9 hazard must dominate a hundred 1e4 hazards, as it does in reality."""
    big = hz(id="big", recurrence=1000.0, deaths_log10=9.0)
    smalls = [hz(id=f"s{i}", recurrence=10.0, deaths_log10=4.0) for i in range(100)]
    rng = np.random.default_rng(7)
    agg = aggregate([big] + smalls, rng, n_draws=200)
    # 0.1 x 1e9 = 1e8 from the big one; 10 x 1e4 x 100 = 1e7 from the smalls.
    assert agg["expected_deaths_log10"] > 8.0


def test_decade_rows_partition_the_century():
    hs = [hz(id="a", recurrence=50.0), hz(id="b", category="nuclear", recurrence=200.0)]
    rows = by_decade(hs)
    assert len(rows) == 10
    assert rows[0]["decade"] == "2026s" and rows[-1]["start"] == 2116
    total = sum(r["total"] for r in rows)
    expected = sum(h.cumulative_hazard(HORIZON_YEARS) for h in hs)
    assert total == pytest.approx(expected, rel=1e-9)


def test_parse_skips_malformed_rows_without_dying():
    got = parse([
        {"id": "ok", "recurrence_years": 100, "severity_0_10": 5, "expected_deaths_log10": 5},
        {"id": "bad", "severity_0_10": 5},
    ])
    assert [h.id for h in got] == ["ok"]

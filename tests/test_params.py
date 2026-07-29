"""Parameter loading, worldview construction, valence, and cluster labelling."""

import json

import numpy as np
import pytest

from worldsim.labelling import label_clusters
from worldsim.params import (
    Risk,
    WorldModel,
    apply_redteam,
    build_worldviews,
    load_base_model,
)
from worldsim.validate import check


def write_model(tmp_path, risks, coupling=None, redteam=None, calibration=None):
    payload = {
        "as_of": "2026-07-29",
        "domains": [
            {
                "domain": "d1",
                "research": {
                    "discrete_risks": risks,
                    "continuous_variables": [],
                    "sources": ["x"],
                    "structural_uncertainties": ["y"],
                },
                "calibration": calibration,
            }
        ],
        "coupling": coupling or {},
        "redteam": redteam or [],
    }
    p = tmp_path / "m.json"
    p.write_text(json.dumps(payload))
    return p


def mk(rid, p27=5.0, p31=20.0, p36=35.0, sev=6.0, conf="medium"):
    return {
        "id": rid, "name": rid.upper(), "resolution_criteria": "crisp",
        "p_by_2027_pct": p27, "p_by_2031_pct": p31, "p_by_2036_pct": p36,
        "severity_0_10": sev, "confidence": conf,
    }


def test_edges_referencing_unknown_nodes_are_dropped_not_crashed():
    """Red-teamers and modellers rename ids; a dangling edge must not take the run down."""
    import tempfile, pathlib

    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        p = write_model(
            tmp, [mk("a"), mk("b")],
            coupling={"conditional_edges": [
                {"source_id": "a", "target_id": "b", "odds_multiplier": 3, "lag_years": 1},
                {"source_id": "a", "target_id": "ghost", "odds_multiplier": 3, "lag_years": 0},
                {"source_id": "a", "target_id": "a", "odds_multiplier": 3, "lag_years": 0},
            ]},
        )
        model, meta = load_base_model(p)
        assert meta["n_edges"] == 1
        assert meta["dropped_edges"] == 2


def test_valence_defaults_to_destabilising_and_is_overridable():
    import tempfile, pathlib

    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        p = write_model(tmp, [mk("a"), mk("peace_deal_x")])
        v = tmp / "v.json"
        v.write_text(json.dumps({"peace_deal_x": -1}))
        model, meta = load_base_model(p, v)
        assert model.risks["a"].valence == 1.0
        assert model.risks["peace_deal_x"].valence == -1.0
        assert model.risks["peace_deal_x"].signed_severity == -6.0
        assert meta["n_stabilising"] == 1


def test_redteam_correction_shifts_the_whole_curve_not_just_one_point():
    """A lens quotes one number; the corrected curve must keep its shape."""
    model = WorldModel(
        "base",
        {"a": Risk("a", "A", "d", "", 10.0, 30.0, 50.0, 5.0)},
        {}, [], [], [],
    )
    out = apply_redteam(
        model,
        [{"lens": "outside-view base rates", "specific_corrections": [
            {"risk_id": "a", "claim": "", "direction": "too_high", "suggested_pct": 15.0,
             "evidence": ""}]}],
        "outside_view",
    )
    r = out.risks["a"]
    assert r.p2031 == pytest.approx(15.0, abs=0.01)
    assert r.p2027 < 10.0 and r.p2036 < 50.0
    assert r.p2027 < r.p2031 < r.p2036, "monotonicity must survive the shift"


def test_extreme_redteam_swings_are_only_partially_trusted():
    """A 5% -> 70% correction usually means a different question reading."""
    model = WorldModel(
        "base", {"a": Risk("a", "A", "d", "", 2.0, 5.0, 9.0, 5.0)}, {}, [], [], []
    )
    out = apply_redteam(
        model,
        [{"lens": "structural break", "specific_corrections": [
            {"risk_id": "a", "claim": "", "direction": "too_low", "suggested_pct": 70.0,
             "evidence": ""}]}],
        "structural_break",
    )
    assert 5.0 < out.risks["a"].p2031 < 70.0


def test_worldview_weights_sum_to_one():
    import tempfile, pathlib

    with tempfile.TemporaryDirectory() as td:
        p = write_model(pathlib.Path(td), [mk("a"), mk("b")])
        base, _ = load_base_model(p)
        views = build_worldviews(base, json.loads(p.read_text()))
        assert len(views) == 5
        assert sum(w for _, w in views) == pytest.approx(1.0)


def test_validation_flags_unscoreable_and_non_monotone_nodes():
    model = WorldModel(
        "m",
        {
            "ok": Risk("ok", "OK", "d", "crisp criteria", 5.0, 20.0, 35.0, 5.0),
            "bad": Risk("bad", "BAD", "d", "", 40.0, 10.0, 60.0, 5.0),
        },
        {}, [], [], [],
    )
    res = check(model)
    kinds = {i["kind"] for i in res["issues"]}
    assert "no_resolution_criteria" in kinds
    assert "non_monotone_cumulative" in kinds
    assert not res["ok"], "a node with no resolution criteria is an error, not a warning"


def test_cluster_labels_ignore_stabilising_events_when_naming_the_theme():
    """A cluster distinguished by an outbreak of peace is not a 'conflict' decade."""
    names = ["Ceasefire", "Bank failure", "Heatwave"]
    domains = ["geopolitics", "economy", "climate"]
    valence = np.array([-1.0, 1.0, 1.0])
    overall = np.array([0.5, 0.3, 0.3])
    clusters = [{
        "probability": 1.0,
        "peak_stress_median": 10.0,
        "peak_stress_pctile": 0.75,
        "event_rates": np.array([0.95, 0.55, 0.31]),
        "excess_z": (np.array([0.95, 0.55, 0.31]) - overall)
        / np.sqrt(overall * (1 - overall)),
        "n_events_mean": 2.0,
    }]
    out = label_clusters(clusters, [0, 1, 2], names, domains, overall, valence)
    assert "financial and macro stress" in out[0]["label"]
    assert "great-power conflict" not in out[0]["label"]
    assert all("Ceasefire" not in s for s in out[0]["signature"])


def test_auditor_added_risks_reach_every_worldview():
    """A node present in only one worldview falls out of the pooled intersection."""
    import tempfile, pathlib

    with tempfile.TemporaryDirectory() as td:
        p = write_model(
            pathlib.Path(td), [mk("a")],
            calibration={
                "domain": "d1", "verdict": "major_issues", "adjustments": [],
                "coherence_violations": [],
                "missing_risks": [{
                    "id": "a_missed", "name": "Missed", "resolution_criteria": "crisp",
                    "p_by_2031_pct": 25.0, "severity_0_10": 7.0, "reasoning": "omitted",
                }],
            },
        )
        base, _ = load_base_model(p)
        assert "a_missed" not in base.risks
        views = build_worldviews(base, json.loads(p.read_text()), {"a_missed": 1.0})
        for model, _ in views:
            assert "a_missed" in model.risks, f"{model.name} is missing the added node"
        r = views[0][0].risks["a_missed"]
        assert r.p2027 < r.p2031 < r.p2036
        assert r.p2031 == pytest.approx(25.0, abs=0.01)


def test_duplicate_screen_separates_same_event_from_opposite_events():
    """Two bars on one axis pointing opposite ways are not the same event."""
    from worldsim.dedupe import find_duplicate_clusters, representatives

    model = WorldModel(
        "m",
        {
            "a_oil_high": Risk("a_oil_high", "Brent above $120", "economy",
                               "Brent crude settles above 120 USD per barrel", 5, 20, 35, 6.0),
            "b_oil_high": Risk("b_oil_high", "Brent above $120", "energy",
                               "Brent crude monthly average above 120 USD per barrel", 6, 22, 37, 5.0),
            "c_oil_low": Risk("c_oil_low", "Brent below $45", "energy",
                              "Brent crude monthly average below 45 USD per barrel", 5, 18, 30, 4.0),
        },
        {}, [], [], [],
    )
    clusters = find_duplicate_clusters(model)
    flat = {tuple(sorted(c)) for c in clusters}
    assert ("a_oil_high", "b_oil_high") in flat, "the same event under two ids must group"
    assert not any("c_oil_low" in c for c in clusters), "opposite thresholds must not group"

    # The representative is the higher-impact member; the other is suppressed.
    drop = representatives(model, clusters)
    assert drop == {"b_oil_high"}


def test_coherence_repair_survives_later_adjustments():
    """An implication is an invariant every worldview must satisfy.

    Enforcing it once on the shared register is not enough — the calibration
    audit and each red-team lens move nodes independently and pull a repaired
    pair back apart.
    """
    import tempfile, pathlib

    with tempfile.TemporaryDirectory() as td:
        p = write_model(
            pathlib.Path(td),
            [mk("wide", 10.0, 20.0, 27.0), mk("narrow", 58.0, 70.0, 76.0)],
            calibration={
                "domain": "d1", "verdict": "major_issues", "coherence_violations": [],
                "missing_risks": [],
                # The auditor pushes the strict event even higher, re-breaking it.
                "adjustments": [{
                    "risk_id": "narrow", "field": "p_by_2036_pct",
                    "original_pct": 76.0, "revised_pct": 88.0, "justification": "",
                }],
            },
        )
        base, _ = load_base_model(p)
        relations = {
            "equivalences": [],
            "implications": [{"stronger": "narrow", "weaker": "wide", "reason": ""}],
        }
        views = build_worldviews(base, json.loads(p.read_text()), {}, relations)
        for model, _ in views:
            w, n = model.risks["wide"], model.risks["narrow"]
            assert w.p2027 >= n.p2027, f"{model.name}: 2027 implication violated"
            assert w.p2031 >= n.p2031, f"{model.name}: 2031 implication violated"
            assert w.p2036 >= n.p2036, f"{model.name}: 2036 implication violated"
        # The auditor's revision stands, and the weaker node was raised to match.
        audited = next(m for m, _ in views if m.name == "audited")
        assert audited.risks["narrow"].p2036 == 88.0
        assert audited.risks["wide"].p2036 == 88.0


def test_equivalent_nodes_are_pooled_not_maximised():
    """Identical criteria, disagreeing analysts: neither is privileged."""
    model = WorldModel(
        "m",
        {
            "x": Risk("x", "X", "d", "same criteria", 10.0, 30.0, 48.0, 5.0),
            "y": Risk("y", "Y", "d", "same criteria", 20.0, 50.0, 60.0, 5.0),
        },
        {}, [], [], [],
    )
    from worldsim.params import enforce_coherence

    out = enforce_coherence(model, {"equivalences": [{"members": ["x", "y"]}], "implications": []})
    assert out.risks["x"].p2036 == pytest.approx(out.risks["y"].p2036)
    # Pooled in log-odds, so strictly between the two inputs — not the max.
    assert 48.0 < out.risks["x"].p2036 < 60.0

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

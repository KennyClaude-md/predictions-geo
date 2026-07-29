"""Parameter model: loading, validation, and worldview construction.

The simulator never trusts a single set of numbers. Research analysts produced
one parameterisation, a per-domain calibration auditor produced corrections, and
three red-team lenses (outside-view base rates, structural-break inside view,
prediction-market check) produced further corrections. Each of those is a
*worldview* — a coherent but distinct opinion about how the world works.

We run all of them and weight the resulting paths, so the reported credible
intervals contain genuine model disagreement rather than just Monte Carlo noise.
That is the difference between "23%" and "23%, and here is how much that number
depends on who you believe".
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, replace
from pathlib import Path

from .timeline import YEARS_PER_QUARTER

# Epistemic spread on each risk's baseline log-odds, by the analyst's own stated
# confidence. These are wide on purpose: stated confidence is itself overconfident.
CONFIDENCE_SIGMA = {"high": 0.30, "medium": 0.50, "low": 0.80}
DEFAULT_SIGMA = 0.50

# How much weight each worldview carries in the ensemble. Grounded in the
# forecasting-tournament result that base-rate discipline and market deference
# beat unaided expert judgement, tempered by the fact that liquid markets do not
# exist for most of these questions and base rates fail across regime changes.
WORLDVIEW_WEIGHTS = {
    "analyst": 0.12,
    "audited": 0.28,
    "outside_view": 0.22,
    "structural_break": 0.16,
    "market_check": 0.22,
}


@dataclass
class Risk:
    id: str
    name: str
    domain: str
    resolution_criteria: str
    p2027: float
    p2031: float
    p2036: float
    severity: float
    confidence: str = "medium"
    reasoning: str = ""
    base_rate_anchor: str = ""
    contrarian_case: str = ""

    @property
    def sigma(self) -> float:
        return CONFIDENCE_SIGMA.get(self.confidence, DEFAULT_SIGMA)


@dataclass
class ContinuousVar:
    id: str
    name: str
    domain: str
    unit: str
    current: float
    drift: float
    vol: float
    p10: float
    p50: float
    p90: float
    notes: str = ""


@dataclass
class Edge:
    source: str
    target: str
    odds_multiplier: float
    lag_quarters: int
    mechanism: str = ""
    confidence: str = "medium"

    @property
    def log_odds(self) -> float:
        return math.log(max(self.odds_multiplier, 1e-3))


@dataclass
class LatentFactor:
    name: str
    description: str
    loadings: dict[str, float] = field(default_factory=dict)
    # Half-life of the factor's autocorrelation, in years. Systemic moods persist.
    half_life_years: float = 3.0


@dataclass
class BlockingPair:
    a: str
    b: str
    reason: str = ""


@dataclass
class WorldModel:
    """One complete, internally consistent opinion about the world."""

    name: str
    risks: dict[str, Risk]
    continuous: dict[str, ContinuousVar]
    edges: list[Edge]
    latents: list[LatentFactor]
    blocks: list[BlockingPair]
    provenance: list[str] = field(default_factory=list)

    def copy_with(self, name: str) -> "WorldModel":
        return WorldModel(
            name=name,
            risks={k: replace(v) for k, v in self.risks.items()},
            continuous=self.continuous,
            edges=self.edges,
            latents=self.latents,
            blocks=self.blocks,
            provenance=list(self.provenance),
        )


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------


def _num(x, default=0.0) -> float:
    try:
        v = float(x)
        return v if math.isfinite(v) else default
    except (TypeError, ValueError):
        return default


def load_base_model(path: str | Path) -> tuple[WorldModel, dict]:
    """Read the research workflow's JSON output into a WorldModel."""
    raw = json.loads(Path(path).read_text())

    risks: dict[str, Risk] = {}
    continuous: dict[str, ContinuousVar] = {}
    provenance: list[str] = []

    for dom in raw.get("domains", []):
        dkey = dom.get("domain", "unknown")
        research = dom.get("research") or {}
        for r in research.get("discrete_risks", []) or []:
            rid = str(r.get("id", "")).strip()
            if not rid:
                continue
            if rid in risks:
                # Two analysts landing on the same id is rare but must not silently
                # overwrite; suffix and keep both so the coupling layer can still
                # resolve whichever one the modeler referenced.
                rid = f"{rid}__2"
            risks[rid] = Risk(
                id=rid,
                name=str(r.get("name", rid)),
                domain=dkey,
                resolution_criteria=str(r.get("resolution_criteria", "")),
                p2027=_num(r.get("p_by_2027_pct")),
                p2031=_num(r.get("p_by_2031_pct")),
                p2036=_num(r.get("p_by_2036_pct")),
                severity=_num(r.get("severity_0_10"), 3.0),
                confidence=str(r.get("confidence", "medium")).lower(),
                reasoning=str(r.get("reasoning", "")),
                base_rate_anchor=str(r.get("base_rate_anchor", "")),
                contrarian_case=str(r.get("contrarian_case", "")),
            )
        for c in research.get("continuous_variables", []) or []:
            cid = str(c.get("id", "")).strip()
            if not cid or cid in continuous:
                continue
            continuous[cid] = ContinuousVar(
                id=cid,
                name=str(c.get("name", cid)),
                domain=dkey,
                unit=str(c.get("unit", "")),
                current=_num(c.get("current_value")),
                drift=_num(c.get("annual_drift")),
                vol=abs(_num(c.get("annual_vol"), 1.0)),
                p10=_num(c.get("p10_2031")),
                p50=_num(c.get("p50_2031")),
                p90=_num(c.get("p90_2031")),
                notes=str(c.get("notes", "")),
            )
        provenance.extend(research.get("sources", []) or [])

    coupling = raw.get("coupling") or {}
    known = set(risks)

    edges: list[Edge] = []
    dropped_edges = 0
    for e in coupling.get("conditional_edges", []) or []:
        s, t = str(e.get("source_id", "")), str(e.get("target_id", ""))
        if s not in known or t not in known or s == t:
            dropped_edges += 1
            continue
        mult = _num(e.get("odds_multiplier"), 1.0)
        if mult <= 0:
            dropped_edges += 1
            continue
        edges.append(
            Edge(
                source=s,
                target=t,
                odds_multiplier=float(min(max(mult, 0.05), 25.0)),
                lag_quarters=int(round(_num(e.get("lag_years"), 0.0) / YEARS_PER_QUARTER)),
                mechanism=str(e.get("mechanism", "")),
                confidence=str(e.get("confidence", "medium")).lower(),
            )
        )

    latents: list[LatentFactor] = []
    for lf in coupling.get("latent_factors", []) or []:
        loadings = {}
        for ld in lf.get("loadings", []) or []:
            rid = str(ld.get("risk_id", ""))
            if rid in known:
                loadings[rid] = float(max(min(_num(ld.get("loading")), 1.0), -1.0))
        if loadings:
            latents.append(
                LatentFactor(
                    name=str(lf.get("name", f"factor{len(latents)}")),
                    description=str(lf.get("description", "")),
                    loadings=loadings,
                )
            )

    blocks = []
    for bp in coupling.get("blocking_pairs", []) or []:
        a, b = str(bp.get("a_id", "")), str(bp.get("b_id", ""))
        if a in known and b in known and a != b:
            blocks.append(BlockingPair(a=a, b=b, reason=str(bp.get("reason", ""))))

    model = WorldModel(
        name="analyst",
        risks=risks,
        continuous=continuous,
        edges=edges,
        latents=latents,
        blocks=blocks,
        provenance=provenance,
    )
    meta = {
        "n_risks": len(risks),
        "n_continuous": len(continuous),
        "n_edges": len(edges),
        "dropped_edges": dropped_edges,
        "n_latents": len(latents),
        "n_blocks": len(blocks),
    }
    return model, meta


# --------------------------------------------------------------------------
# Worldview construction
# --------------------------------------------------------------------------

_FIELD_MAP = {
    "p_by_2027_pct": "p2027",
    "p_by_2031_pct": "p2031",
    "p_by_2036_pct": "p2036",
    "severity_0_10": "severity",
}

# A correction that moves a probability by more than this many percentage points
# is applied at partial strength. Red-teamers, given licence to disagree, produce
# occasional 5%->60% swings that reflect a different question reading rather than
# a genuine calibration insight.
MAX_TRUSTED_SWING = 35.0
PARTIAL_STRENGTH = 0.55


def _blend(original: float, revised: float) -> float:
    swing = abs(revised - original)
    if swing <= MAX_TRUSTED_SWING:
        return revised
    return original + (revised - original) * PARTIAL_STRENGTH


def apply_calibration(model: WorldModel, raw: dict) -> WorldModel:
    """Apply the per-domain calibration auditor's adjustments and added risks."""
    out = model.copy_with("audited")
    applied = 0
    for dom in raw.get("domains", []):
        cal = dom.get("calibration") or {}
        for adj in cal.get("adjustments", []) or []:
            rid = str(adj.get("risk_id", ""))
            fld = _FIELD_MAP.get(str(adj.get("field", "")))
            if rid not in out.risks or not fld:
                continue
            cur = getattr(out.risks[rid], fld)
            setattr(out.risks[rid], fld, _blend(cur, _num(adj.get("revised_pct"), cur)))
            applied += 1
        # Risks the auditor thought were missing enter with a single anchor point;
        # we fan it out to the three horizons on a constant-hazard assumption.
        for miss in cal.get("missing_risks", []) or []:
            rid = str(miss.get("id", "")).strip()
            if not rid or rid in out.risks:
                continue
            p31 = _num(miss.get("p_by_2031_pct"))
            out.risks[rid] = Risk(
                id=rid,
                name=str(miss.get("name", rid)),
                domain=dom.get("domain", "unknown"),
                resolution_criteria=str(miss.get("resolution_criteria", "")),
                p2027=_constant_hazard_extrapolate(p31, 22, 6),
                p2031=p31,
                p2036=_constant_hazard_extrapolate(p31, 22, 42),
                severity=_num(miss.get("severity_0_10"), 3.0),
                confidence="low",
                reasoning=str(miss.get("reasoning", "")),
                base_rate_anchor="added by calibration audit",
            )
    out.provenance.append(f"calibration adjustments applied: {applied}")
    return out


def _constant_hazard_extrapolate(p_pct: float, from_q: int, to_q: int) -> float:
    p = min(max(p_pct / 100.0, 1e-4), 0.995)
    surv = (1.0 - p) ** (to_q / from_q)
    return float((1.0 - surv) * 100.0)


def apply_redteam(model: WorldModel, redteam: list[dict], lens_key: str) -> WorldModel:
    """Build a worldview from one red-team lens's corrections."""
    out = model.copy_with(lens_key)
    lens = None
    for rt in redteam:
        if lens_key.split("_")[0] in str(rt.get("lens", "")).lower().replace("-", "_"):
            lens = rt
            break
    if lens is None:
        # Fall back to positional matching when the agent renamed its own lens.
        idx = {"outside_view": 0, "structural_break": 1, "market_check": 2}.get(lens_key)
        if idx is not None and idx < len(redteam):
            lens = redteam[idx]
    if lens is None:
        return out

    applied = 0
    for corr in lens.get("specific_corrections", []) or []:
        rid = str(corr.get("risk_id", ""))
        if rid not in out.risks:
            continue
        suggested = _num(corr.get("suggested_pct"), -1.0)
        if suggested < 0:
            continue
        r = out.risks[rid]
        # A lens quotes one number; we read it as a statement about the 2031
        # anchor and shift the whole hazard curve by the same log-odds delta so
        # the corrected curve keeps its shape.
        delta = _logit_pct(suggested) - _logit_pct(r.p2031)
        r.p2027 = _shift_pct(r.p2027, delta)
        r.p2031 = _blend(r.p2031, suggested)
        r.p2036 = _shift_pct(r.p2036, delta)
        applied += 1
    out.provenance.append(f"{lens_key}: {applied} corrections from '{lens.get('lens', '?')}'")
    return out


def _logit_pct(pct: float) -> float:
    p = min(max(pct / 100.0, 1e-4), 0.9995)
    return math.log(p / (1 - p))


def _shift_pct(pct: float, delta: float) -> float:
    x = _logit_pct(pct) + delta
    return float(100.0 / (1.0 + math.exp(-max(min(x, 40.0), -40.0))))


def build_worldviews(base: WorldModel, raw: dict) -> list[tuple[WorldModel, float]]:
    """Return [(model, ensemble weight)] covering the full range of opinion."""
    audited = apply_calibration(base, raw)
    redteam = raw.get("redteam", []) or []

    views = [
        (base, WORLDVIEW_WEIGHTS["analyst"]),
        (audited, WORLDVIEW_WEIGHTS["audited"]),
        (apply_redteam(audited, redteam, "outside_view"), WORLDVIEW_WEIGHTS["outside_view"]),
        (apply_redteam(audited, redteam, "structural_break"), WORLDVIEW_WEIGHTS["structural_break"]),
        (apply_redteam(audited, redteam, "market_check"), WORLDVIEW_WEIGHTS["market_check"]),
    ]
    total = sum(w for _, w in views)
    return [(m, w / total) for m, w in views]

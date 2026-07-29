"""Coherence checks on the loaded parameter set.

Elicited parameters arrive with predictable pathologies: non-monotone
cumulatives, severity ratings that don't match the described event, causal edges
pointing at nodes that were renamed, latent loadings that all point the same way
so every factor becomes the same factor. None of these crash the engine — they
just quietly degrade it. This module surfaces them before a run rather than after.
"""

from __future__ import annotations

import numpy as np

from .params import WorldModel


def check(model: WorldModel) -> dict:
    issues: list[dict] = []

    _check_monotone(model, issues)
    _check_degenerate(model, issues)
    _check_edges(model, issues)
    _check_latents(model, issues)
    _check_severity(model, issues)
    _check_duplicates(model, issues)

    by_sev = {}
    for level in ("error", "warning", "note"):
        by_sev[level] = [i for i in issues if i["level"] == level]
    return {
        "issues": issues,
        "counts": {k: len(v) for k, v in by_sev.items()},
        "ok": not by_sev["error"],
    }


def _check_monotone(model: WorldModel, issues: list) -> None:
    for r in model.risks.values():
        if not (r.p2027 <= r.p2031 <= r.p2036):
            issues.append(
                {
                    "level": "warning",
                    "kind": "non_monotone_cumulative",
                    "risk": r.id,
                    "detail": f"{r.p2027:.1f} -> {r.p2031:.1f} -> {r.p2036:.1f}; "
                    "isotonic repair will pool the violating pair",
                }
            )


def _check_degenerate(model: WorldModel, issues: list) -> None:
    for r in model.risks.values():
        if r.p2036 >= 99.5:
            issues.append(
                {
                    "level": "note",
                    "kind": "near_certain",
                    "risk": r.id,
                    "detail": f"P(2036)={r.p2036:.1f}% is being clamped; a node this "
                    "certain carries no information and will show as >99%",
                }
            )
        if r.p2036 <= 0.2:
            issues.append(
                {
                    "level": "note",
                    "kind": "near_impossible",
                    "risk": r.id,
                    "detail": f"P(2036)={r.p2036:.3f}% — below the resolution of "
                    "this many paths",
                }
            )
        if not r.resolution_criteria.strip():
            issues.append(
                {
                    "level": "error",
                    "kind": "no_resolution_criteria",
                    "risk": r.id,
                    "detail": "unscoreable: no resolution criteria given",
                }
            )


def _check_edges(model: WorldModel, issues: list) -> None:
    seen: dict[tuple[str, str], int] = {}
    for e in model.edges:
        key = (e.source, e.target)
        seen[key] = seen.get(key, 0) + 1
        if abs(e.odds_multiplier - 1.0) < 0.05:
            issues.append(
                {
                    "level": "note",
                    "kind": "null_edge",
                    "risk": f"{e.source}->{e.target}",
                    "detail": f"odds multiplier {e.odds_multiplier:.2f} is effectively 1",
                }
            )
    for key, n in seen.items():
        if n > 1:
            issues.append(
                {
                    "level": "warning",
                    "kind": "duplicate_edge",
                    "risk": f"{key[0]}->{key[1]}",
                    "detail": f"specified {n} times; effects compound multiplicatively",
                }
            )

    # A node whose inbound multipliers can collectively swamp its baseline is a
    # node whose elicited marginal is being carried entirely by the calibration
    # loop pushing the baseline into the floor.
    inbound: dict[str, float] = {}
    for e in model.edges:
        if e.odds_multiplier > 1:
            inbound[e.target] = inbound.get(e.target, 0.0) + e.log_odds
    for rid, total in inbound.items():
        if total > 6.0:
            issues.append(
                {
                    "level": "warning",
                    "kind": "edge_dominated",
                    "risk": rid,
                    "detail": f"inbound log-odds sum {total:.1f} (odds x{np.exp(total):.0f}) "
                    "if all parents fire; baseline will be driven very low to compensate",
                }
            )


def _check_latents(model: WorldModel, issues: list) -> None:
    if len(model.latents) < 2:
        return
    keys = sorted({rid for lf in model.latents for rid in lf.loadings})
    if not keys:
        return
    mat = np.array(
        [[lf.loadings.get(k, 0.0) for k in keys] for lf in model.latents], dtype=float
    )
    for i in range(len(model.latents)):
        for j in range(i + 1, len(model.latents)):
            a, b = mat[i], mat[j]
            denom = np.linalg.norm(a) * np.linalg.norm(b)
            if denom < 1e-9:
                continue
            cos = float(a @ b / denom)
            if cos > 0.8:
                issues.append(
                    {
                        "level": "warning",
                        "kind": "collinear_latents",
                        "risk": f"{model.latents[i].name} ~ {model.latents[j].name}",
                        "detail": f"cosine similarity {cos:.2f}: these are one factor "
                        "wearing two names, and double-count their shared correlation",
                    }
                )


def _check_severity(model: WorldModel, issues: list) -> None:
    sev = np.array([r.severity for r in model.risks.values()])
    if sev.size and sev.mean() > 6.5:
        issues.append(
            {
                "level": "warning",
                "kind": "severity_inflation",
                "risk": "(global)",
                "detail": f"mean severity {sev.mean():.1f}/10 — if almost everything is "
                "severe then the stress index cannot discriminate between decades",
            }
        )

    # Rater drift. Each domain was scored by a different analyst against the same
    # nominal 0-10 scale, and they do not use it the same way. Where one domain
    # sits well above the rest, its nodes dominate the stress index and the
    # impact ranking for reasons that are about the rater, not the world.
    by_dom: dict[str, list[float]] = {}
    for r in model.risks.values():
        by_dom.setdefault(r.domain, []).append(r.severity)
    if len(by_dom) >= 3:
        means = {d: float(np.mean(v)) for d, v in by_dom.items() if len(v) >= 4}
        if means:
            overall = float(np.mean(list(means.values())))
            for d, m in sorted(means.items(), key=lambda kv: -kv[1]):
                if abs(m - overall) >= 1.2:
                    direction = "above" if m > overall else "below"
                    issues.append(
                        {
                            "level": "warning",
                            "kind": "severity_rater_drift",
                            "risk": f"domain:{d}",
                            "detail": f"mean severity {m:.2f} vs {overall:.2f} across "
                            f"domains — this rater sits {abs(m-overall):.2f} points "
                            f"{direction} the others, so cross-domain severity "
                            f"comparisons are not on a common scale",
                        }
                    )


def _check_duplicates(model: WorldModel, issues: list) -> None:
    """Screen for one event enumerated twice; the decision stays curated."""
    from .dedupe import find_duplicate_clusters

    for cluster in find_duplicate_clusters(model):
        issues.append(
            {
                "level": "note",
                "kind": "possible_duplicate",
                "risk": " ~ ".join(cluster),
                "detail": "these read as the same event or as nested thresholds on "
                "one axis; confirm they are handled in params/duplicate_families.json "
                "or they will be counted separately in aggregates",
            }
        )


def format_report(result: dict, limit: int = 40) -> str:
    lines = [
        f"validation: {result['counts']['error']} errors, "
        f"{result['counts']['warning']} warnings, {result['counts']['note']} notes"
    ]
    order = {"error": 0, "warning": 1, "note": 2}
    for issue in sorted(result["issues"], key=lambda i: order[i["level"]])[:limit]:
        lines.append(f"  [{issue['level']:7s}] {issue['kind']:26s} {issue['risk']}")
        lines.append(f"            {issue['detail']}")
    remaining = len(result["issues"]) - limit
    if remaining > 0:
        lines.append(f"  ... and {remaining} more")
    return "\n".join(lines)

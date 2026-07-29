"""Finding the same event enumerated twice.

Nine analysts wrote their registers independently, so the same world-event shows
up under several ids: a Strait of Hormuz closure appears in geopolitics, in
economy and in energy. Left alone this is not a cosmetic problem —

  * aggregate counts triple-count one shock,
  * the stress index adds its severity three times,
  * and worst, the three copies fire *independently*, so the model computes
    P(at least one Hormuz closure) as if three separate straits could close.

Detection is deliberately conservative: content-token overlap over the name and
resolution criteria, with agreement on any numeric thresholds mentioned. A false
positive would merge two genuinely distinct risks, which is worse than missing
one, so the bar is set high and everything it finds is reported for inspection
rather than silently applied.
"""

from __future__ import annotations

import re

from .params import WorldModel

STOPWORDS = {
    "a", "an", "the", "of", "or", "and", "in", "on", "at", "to", "for", "by",
    "is", "are", "be", "been", "with", "from", "any", "least", "more", "than",
    "that", "this", "it", "its", "as", "not", "no", "new", "least", "over",
    "within", "during", "per", "into", "out", "up", "down", "least", "one",
    "which", "who", "whose", "must", "may", "would", "will", "has", "have",
    "counts", "count", "if", "resolves", "yes", "resolution", "criteria",
}

# Tokens that carry most of the identifying signal — a pair sharing these is far
# more likely to be the same event than a pair sharing generic prose.
JACCARD_THRESHOLD = 0.42
MIN_SHARED_CONTENT = 4


def _tokens(text: str) -> set[str]:
    words = re.findall(r"[a-z]+", text.lower())
    return {w for w in words if w not in STOPWORDS and len(w) > 2}


def _numbers(text: str) -> set[str]:
    return set(re.findall(r"\d+(?:\.\d+)?", text.replace(",", "")))


def _signature(risk) -> tuple[set[str], set[str]]:
    blob = f"{risk.name} {risk.resolution_criteria}"
    return _tokens(blob), _numbers(blob)


def find_duplicate_clusters(model: WorldModel) -> list[list[str]]:
    """Group risk ids that appear to describe the same underlying event."""
    ids = sorted(model.risks)
    sigs = {rid: _signature(model.risks[rid]) for rid in ids}

    parent = {rid: rid for rid in ids}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i, a in enumerate(ids):
        ta, na = sigs[a]
        if not ta:
            continue
        for b in ids[i + 1 :]:
            tb, nb = sigs[b]
            if not tb:
                continue
            shared = ta & tb
            if len(shared) < MIN_SHARED_CONTENT:
                continue
            jac = len(shared) / len(ta | tb)
            if jac < JACCARD_THRESHOLD:
                continue
            # If both state numeric thresholds and none coincide, they are
            # probably different bars on the same axis — related, not identical.
            if na and nb and not (na & nb):
                continue
            union(a, b)

    groups: dict[str, list[str]] = {}
    for rid in ids:
        groups.setdefault(find(rid), []).append(rid)
    return [sorted(g) for g in groups.values() if len(g) > 1]


def representatives(model: WorldModel, clusters: list[list[str]]) -> set[str]:
    """One id per cluster — the highest-severity member, ties broken by id.

    Used to keep aggregate counts and the stress index from adding the same
    shock several times. Non-representatives still simulate: they keep their own
    marginals, which are what the report quotes per node.
    """
    drop: set[str] = set()
    for cluster in clusters:
        keep = max(cluster, key=lambda r: (model.risks[r].severity, r))
        drop.update(c for c in cluster if c != keep)
    return drop


def describe(model: WorldModel, clusters: list[list[str]]) -> str:
    lines = [f"{len(clusters)} near-duplicate cluster(s):"]
    for cluster in clusters:
        lines.append("  " + " ~ ".join(cluster))
        for rid in cluster:
            r = model.risks[rid]
            lines.append(f"      [{r.domain}] sev {r.severity:.0f} — {r.name[:78]}")
    return "\n".join(lines)

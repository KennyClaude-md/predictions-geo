"""Assign a predicted bill to Friday, Saturday and Sunday.

This is the weakest claim in the whole forecast and it should be read that way.
Day-level rosters are barely reported: across every edition in the dataset I can
recover the full headline day-split for two of them, plus a fragment of one day's
undercard. Two observations cannot support a fitted model, so this is an explicit
rule, stated so it can be argued with, rather than a fit dressed up as one.

Two rules, both grounded in what little is observable:

  1. *Saturday takes the biggest draw.* Miami 2023 put Travis Scott there and
     Orlando 2026 put Playboi Carti there -- the top-draw act in both cases.
     Sunday takes the next, Friday the third. Note that Miami 2023 also had
     Carti, an equal-draw act, on Friday, so this rule is a tendency and not a
     law even within its two data points.

  2. *Each day clusters around its headliner's lane.* This is visible in the one
     undercard fragment I have: Orlando 2026's NBA YoungBoy Sunday carried Sexyy
     Red, OsamaSon, Che and Skrilla. Acts are therefore assigned to the day whose
     headliner shares their scene, subject to days coming out roughly equal,
     because a festival cannot put half its bill on one afternoon.

Women are spread rather than clustered: Rolling Loud bills visibly balance them
across days, so `women_rap` is excluded from scene-matching and distributed.
"""

from __future__ import annotations

DAYS = ("FRIDAY", "SATURDAY", "SUNDAY")

# Saturday first: the headline slate is sorted by draw and dealt in this order.
DEAL_ORDER = (1, 2, 0)

SAME_SCENE_BONUS = 1.0
CROSS_SCENE_BASE = 0.25


def assign_days(roster, headliners: list[str], undercard: list[str]) -> dict:
    """Return {day: {'headliner': key, 'acts': [keys]}}.

    `headliners` and `undercard` are artist keys, undercard already in billing
    order (most prominent first) so that the greedy pass places the names that
    matter most while every day still has room.
    """
    arts = roster.artists

    # Rule 1 -- deal the headline slate by draw, Saturday first.
    ranked = sorted(headliners, key=lambda k: -arts[k]["draw"])
    day_of = {}
    for slot, key in zip(DEAL_ORDER, ranked):
        day_of[DAYS[slot]] = key

    out = {d: {"headliner": day_of[d], "acts": []} for d in DAYS}
    cap = -(-len(undercard) // 3)          # ceiling, so the last day isn't starved

    # Rule 2 -- greedy scene matching under an equal-size constraint.
    for key in undercard:
        scene = arts[key].get("scene", "opium_rage")
        spread = scene == "women_rap"
        best, best_score = None, None
        for d in DAYS:
            if len(out[d]["acts"]) >= cap:
                continue
            hl_scene = arts[out[d]["headliner"]].get("scene", "opium_rage")
            if spread:
                score = 0.0                # no scene pull; balance decides
            else:
                score = (SAME_SCENE_BONUS if scene == hl_scene
                         else CROSS_SCENE_BASE)
            # Prefer the emptier day when scores tie, which is what produces the
            # spread for women_rap and keeps the three days comparable.
            score -= 0.02 * len(out[d]["acts"])
            if best_score is None or score > best_score:
                best, best_score = d, score
        if best is None:                    # every day at capacity
            best = min(DAYS, key=lambda d: len(out[d]["acts"]))
        out[best]["acts"].append(key)

    return out

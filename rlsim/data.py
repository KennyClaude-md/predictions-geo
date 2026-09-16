"""Load the Rolling Loud parameter files and build per-edition design matrices.

Every judgement about *when* a feature is measured lives here. A booking is
decided months before doors, so an edition's features are read from the popularity
column closest to when the talent buyer was actually committing money -- roughly
five months out. Using the popularity an artist had on the day of the show would
leak the future into the fit and make the backtest meaningless.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import numpy as np

PARAMS = Path(__file__).resolve().parent.parent / "params"

# Which popularity column stands in for "what the buyer knew" at each edition.
# Chosen as the snapshot nearest five months before doors, which is the observed
# median gap between a Rolling Loud lineup reveal and the festival itself.
BOOKING_EPOCH = {
    "cali_2023": "2022-10",
    "miami_2023": "2023-02",
    "cali_2024": "2023-10",
    "miami_2024": "2024-07",
    "cali_2025": "2024-10",
    "orlando_2026": "2025-12",
    "florida_2027": "2026-09",
}

# Headline history decays: a slot four years ago says less about this year's
# booking than a slot last year. 0.65/yr gives a prior headline roughly half the
# weight after 18 months, which is the timescale on which this festival's
# headline slate visibly turns over.
HISTORY_DECAY_PER_YEAR = 0.65

# Artists below this popularity rank at booking time are not treated as
# candidates to close a night. Generous on purpose: Ken Carson was rank ~22 when
# Rolling Loud first put him on a headline line, so a tight cut would have made
# his booking unexplainable rather than merely surprising.
HEADLINE_POOL_RANK_CUT = 60

# Candidate feature sets. Which one to use is a model-selection question, not a
# taste question, so all four are scored leave-one-edition-out in model.backtest
# and the winner is reported alongside the losers.
#
#   base      the obvious five
#   draw      adds headline DRAW -- the size of room an act sells on their own
#             name -- which is what separates cultural heat from a night-closer
#   b2b       adds an explicit back-to-back term so serial incumbency (Carti)
#             can be told apart from a one-off repeat
#   full      both
FEATURE_SETS = {
    "base": ["hl_hist", "heat", "rl_fit", "fest_avail", "regional_fl"],
    "draw": ["hl_hist", "heat", "draw", "rl_fit", "fest_avail", "regional_fl"],
    "b2b":  ["hl_hist", "back_to_back", "heat", "rl_fit", "fest_avail", "regional_fl"],
    "full": ["hl_hist", "back_to_back", "heat", "draw", "rl_fit", "fest_avail",
             "regional_fl"],
}
FEATURE_NAMES = FEATURE_SETS["full"]


def _heat(rank: float) -> float:
    """Popularity rank -> a score that is linear in log-rank.

    Rank differences matter multiplicatively, not additively: the gap between
    #1 and #5 is a different kind of gap than between #51 and #55. log(100/rank)
    puts a top act near 4.6 and the 100th-hottest at 0.
    """
    return float(np.log(100.0 / max(float(rank), 1.0)))


@dataclass
class Edition:
    key: str
    brand: str
    start: date
    status: str
    us_flagship: bool
    headliners_booked: list[str]
    headliners_performed: list[str]
    undercard_reported: list[str]
    days: int = 0
    notes: str = ""

    @property
    def is_florida(self) -> bool:
        return "Florida" in self.brand or "Miami" in self.brand

    @property
    def bill(self) -> set[str]:
        """Everyone known to have been billed, headline or not."""
        return set(self.headliners_booked) | set(self.undercard_reported)


@dataclass
class Roster:
    artists: dict[str, dict]
    editions: list[Edition]
    forward: list[dict]
    composition: dict = field(default_factory=dict)

    # --- feature construction -------------------------------------------------

    def headline_history(self, artist: str, before: date) -> float:
        """Recency-weighted count of prior US flagship headline bookings."""
        total = 0.0
        for e in self.editions:
            if not e.us_flagship or e.start >= before or e.status == "never_staged":
                continue
            if artist in e.headliners_booked:
                years = (before - e.start).days / 365.25
                total += HISTORY_DECAY_PER_YEAR ** years
        return total

    def prior_bill_count(self, artist: str, before: date) -> int:
        """How many prior staged editions this artist appeared on at all."""
        return sum(
            1 for e in self.editions
            if e.start < before and e.status == "held" and artist in e.bill
        )

    def on_previous_flagship(self, artist: str, before: date) -> bool:
        prev = [e for e in self.editions
                if e.us_flagship and e.status == "held" and e.start < before]
        if not prev:
            return False
        return artist in max(prev, key=lambda e: e.start).bill

    def rank_at(self, artist: str, epoch: str) -> float | None:
        r = self.artists[artist]["heat_rank"].get(epoch)
        return None if r is None else float(r)

    def headline_pool(self, edition_key: str, when: date) -> list[str]:
        """Candidate closers: anyone hot enough at booking time, plus whoever
        actually got the slot (so an unexpected booking is scored as a surprise
        rather than silently dropped from the likelihood)."""
        epoch = BOOKING_EPOCH[edition_key]
        pool = []
        for key, a in self.artists.items():
            rank = self.rank_at(key, epoch)
            if rank is None:
                continue
            if rank <= HEADLINE_POOL_RANK_CUT and a["tier"] in ("headline", "upper"):
                pool.append(key)
        ed = next((e for e in self.editions if e.key == edition_key), None)
        if ed is not None:
            for k in ed.headliners_booked:
                if k in self.artists and k not in pool:
                    pool.append(k)
        return sorted(set(pool))

    def headlined_previous_flagship(self, artist: str, before: date) -> bool:
        """Did this artist close a night at the immediately preceding edition?"""
        prev = [e for e in self.editions
                if e.us_flagship and e.status == "held" and e.start < before]
        if not prev:
            return False
        return artist in max(prev, key=lambda e: e.start).headliners_booked

    def design(self, edition_key: str, when: date, is_florida: bool,
               pool: list[str], features: list[str] | None = None) -> np.ndarray:
        """Feature matrix for one edition's candidate pool, standardized within
        the pool so coefficients are comparable across editions of different
        depth."""
        feats = features or FEATURE_NAMES
        epoch = BOOKING_EPOCH[edition_key]
        rows = []
        for k in pool:
            a = self.artists[k]
            rank = self.rank_at(k, epoch)
            col = {
                "hl_hist": self.headline_history(k, when),
                "back_to_back": 1.0 if self.headlined_previous_flagship(k, when) else 0.0,
                "heat": _heat(rank if rank is not None else 200.0),
                "draw": a["draw"],
                "rl_fit": a["rl_fit"],
                "fest_avail": a["fest_avail"],
                "regional_fl": a["regional_fl"] * (1.0 if is_florida else 0.0),
            }
            rows.append([col[f] for f in feats])
        X = np.asarray(rows, dtype=float)
        # Centre and scale within the pool. Location shifts cancel in a
        # conditional logit, but scaling keeps the ridge penalty meaningful.
        sd = X.std(axis=0)
        sd[sd < 1e-9] = 1.0
        return (X - X.mean(axis=0)) / sd


def load(params_dir: Path | None = None) -> Roster:
    d = Path(params_dir) if params_dir else PARAMS
    eds_raw = json.loads((d / "rolling_loud_editions.json").read_text())
    arts_raw = json.loads((d / "rolling_loud_artists.json").read_text())

    editions = [
        Edition(
            key=e["key"], brand=e["brand"],
            start=date.fromisoformat(e["start"]), status=e["status"],
            us_flagship=e.get("us_flagship", False),
            headliners_booked=e.get("headliners_booked", []),
            headliners_performed=e.get("headliners_performed", []),
            undercard_reported=e.get("undercard_reported", []),
            days=e.get("days", 0), notes=e.get("notes", ""),
        )
        for e in eds_raw["editions"]
    ]
    editions.sort(key=lambda e: e.start)

    artists = {a["key"]: a for a in arts_raw["artists"]}

    # Only the US flagship editions feed the fit, so only those must resolve
    # fully against the artist table. International bills carry local headliners
    # (Karan Aujla, Wiz Khalifa) that are deliberately not modelled here.
    known = set(artists)
    for e in editions:
        if not e.us_flagship:
            continue
        for k in e.headliners_booked:
            if k not in known:
                raise ValueError(f"{e.key}: headliner {k!r} missing from artist table")

    return Roster(
        artists=artists,
        editions=editions,
        forward=eds_raw["confirmed_forward_calendar"],
        composition=arts_raw.get("structural_composition", {}),
    )

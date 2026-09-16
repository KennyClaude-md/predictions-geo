"""Integrate the fitted models forward over parameter and availability uncertainty.

Three things are uncertain and all three are sampled per path rather than fixed
at a point estimate:

  1. *The coefficients.* Drawn from the asymptotic sampling distribution of the
     fitted conditional logit. With eighteen bookings in the fit this spread is
     wide, and pretending otherwise would produce confident nonsense.
  2. *Availability.* An artist can be unwilling, unaffordable, on someone else's
     stage, or in custody. Each is gated by a per-artist Bernoulli before the
     choice model ever sees them. This is what stops the model from handing a
     headline slot to whoever happens to be most famous.
  3. *Which three get picked.* Given coefficients and an available pool, the
     slate is a Plackett-Luce draw, sampled with the Gumbel top-k trick, which
     is exactly equivalent to sequential softmax selection without replacement
     and vectorises.

Reported probabilities carry Monte Carlo standard errors. Those error bars
describe sampling noise and nothing else -- they say how precisely the model has
been integrated, not how likely the model is to be right.
"""

from __future__ import annotations

from datetime import date

import numpy as np

from .data import BOOKING_EPOCH, Roster, _heat
from .model import HeadlinerModel, UndercardModel, undercard_row


def simulate(roster: Roster, hm: HeadlinerModel, um: UndercardModel,
             target_key: str = "florida_2027",
             target_date: date = date(2027, 5, 7),
             is_florida: bool = True,
             n_slots: int = 3,
             paths: int = 200_000,
             undercard_rank_cut: int = 110,
             seed: int = 20270507) -> dict:
    rng = np.random.default_rng(seed)

    # --- headline pool --------------------------------------------------------
    pool = roster.headline_pool(target_key, target_date)
    X = roster.design(target_key, target_date, is_florida, pool, hm.features)
    avail = np.array([roster.artists[k]["avail_2027"] for k in pool])

    # Coefficient draws. One set of coefficients per path, so a path is a
    # coherent world rather than an average of incoherent ones.
    L = np.linalg.cholesky(hm.cov + 1e-9 * np.eye(len(hm.w)))
    W = hm.w + rng.standard_normal((paths, len(hm.w))) @ L.T

    U = W @ X.T                                    # paths x pool utilities
    is_avail = rng.random((paths, len(pool))) < avail
    # Everyone must be available for the slate to be fillable; if fewer than
    # n_slots are free the pool cut was too tight, which we check rather than
    # silently paper over.
    if (is_avail.sum(axis=1) < n_slots).any():
        short = int((is_avail.sum(axis=1) < n_slots).sum())
        raise RuntimeError(f"{short} paths had fewer than {n_slots} available acts")

    gumbel = -np.log(-np.log(rng.random((paths, len(pool)))))
    scores = np.where(is_avail, U + gumbel, -np.inf)
    chosen = np.argpartition(-scores, n_slots - 1, axis=1)[:, :n_slots]

    counts = np.zeros(len(pool))
    np.add.at(counts, chosen.ravel(), 1)
    hl_p = counts / paths

    # Joint slates, as sorted index tuples.
    slates: dict[tuple, int] = {}
    for row in np.sort(chosen, axis=1):
        t = tuple(row)
        slates[t] = slates.get(t, 0) + 1

    # --- undercard ------------------------------------------------------------
    epoch = BOOKING_EPOCH[target_key]
    prev = max((e for e in roster.editions if e.us_flagship and e.status == "held"),
               key=lambda e: e.start)
    uc_keys, uc_rows, uc_avail = [], [], []
    for k, a in roster.artists.items():
        rank = roster.rank_at(k, epoch)
        if rank is None or rank > undercard_rank_cut:
            continue
        uc_keys.append(k)
        uc_rows.append(undercard_row(
            roster, k, rank, k in prev.bill, is_florida,
            roster.prior_bill_count(k, target_date), um.features))
        uc_avail.append(a["avail_2027"])
    uc_p = um.prob(np.asarray(uc_rows)) * np.asarray(uc_avail)

    # An artist who lands a headline slot is trivially on the bill; anywhere-on-
    # the-bill probability is the union of the two routes.
    hl_index = {k: i for i, k in enumerate(pool)}
    bill_p = {}
    for i, k in enumerate(uc_keys):
        p_hl = hl_p[hl_index[k]] if k in hl_index else 0.0
        bill_p[k] = p_hl + (1.0 - p_hl) * float(uc_p[i])
    for k in pool:
        if k not in bill_p:
            bill_p[k] = float(hl_p[hl_index[k]])

    se = lambda p: float(np.sqrt(max(p * (1 - p), 0.0) / paths))

    return {
        "paths": paths,
        "pool": pool,
        "headline_prob": {k: float(hl_p[i]) for i, k in enumerate(pool)},
        "headline_se": {k: se(float(hl_p[i])) for i, k in enumerate(pool)},
        "bill_prob": bill_p,
        "slates": sorted(
            (((pool[i] for i in t), c / paths) for t, c in slates.items()),
            key=lambda kv: -kv[1],
        )[:0] or [
            ([pool[i] for i in t], c / paths)
            for t, c in sorted(slates.items(), key=lambda kv: -kv[1])[:25]
        ],
        "expected_returning_share": float(np.mean([
            bill_p[k] for k in bill_p if k in prev.bill
        ])),
    }

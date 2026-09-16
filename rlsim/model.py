"""The two fitted models and their honest evaluation.

Headliners are a *choice* problem: from a pool of acts who could close a night,
three get picked. That is a conditional logit, fitted by maximum likelihood over
the six US flagship editions staged since 2023. Eighteen bookings is not much
data, so the fit is ridge-penalised and the penalty is chosen by leave-one-
edition-out predictive likelihood rather than by taste.

The undercard is a *persistence* problem: Rolling Loud rebuilds most of its bill
each year from the previous one plus that season's risers, so the useful question
per artist is a probability of appearing at all. That is a logistic regression on
edition-to-edition transitions.

`backtest()` is the part that matters. It scores the headline model against three
baselines a sceptic would reasonably propose -- rank by popularity alone, rebook
last year's headliners, or draw from the pool at random -- because a model that
cannot beat "rebook last year" has not earned the extra machinery.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp, expit

from .data import BOOKING_EPOCH, FEATURE_NAMES, FEATURE_SETS, Roster, _heat

# Editions the headline model is fitted on: US flagship, actually staged, and
# carrying a booked headline slate. Australia and India are excluded -- a
# different market, a different budget and a different booking process.
def fit_editions(roster: Roster) -> list:
    return [e for e in roster.editions
            if e.us_flagship and e.status == "held" and e.headliners_booked]


@dataclass
class HeadlinerModel:
    w: np.ndarray
    cov: np.ndarray
    ridge: float
    n_slots: int
    loglik: float
    features: list = None

    def utilities(self, X: np.ndarray, w: np.ndarray | None = None) -> np.ndarray:
        return X @ (self.w if w is None else w)


def _pl_negloglik(w: np.ndarray, blocks: list[tuple[np.ndarray, list[int]]],
                  ridge: float) -> float:
    """Plackett-Luce negative log-likelihood with a ridge penalty.

    Headliners are announced as a set, not a ranking. Treating the billing order
    as a draw order is an approximation; it is unbiased for the set-membership
    question we actually care about and avoids summing over permutations of a
    pool of fifty.
    """
    nll = 0.0
    for X, chosen in blocks:
        u = X @ w
        remaining = np.ones(len(u), dtype=bool)
        for c in chosen:
            nll -= u[c] - logsumexp(u[remaining])
            remaining[c] = False
    return nll + 0.5 * ridge * float(w @ w)


def _numeric_hessian(f, w: np.ndarray, eps: float = 1e-4) -> np.ndarray:
    n = len(w)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            wpp, wpm, wmp, wmm = (w.copy() for _ in range(4))
            wpp[i] += eps; wpp[j] += eps
            wpm[i] += eps; wpm[j] -= eps
            wmp[i] -= eps; wmp[j] += eps
            wmm[i] -= eps; wmm[j] -= eps
            H[i, j] = H[j, i] = (f(wpp) - f(wpm) - f(wmp) + f(wmm)) / (4 * eps * eps)
    return H


_DESIGN_CACHE: dict = {}


def design_for(roster: Roster, edition, features):
    """Pool and design matrix for one edition, memoised.

    The backtest rebuilds these for every (feature set, ridge, fold) triple and
    they never change, so caching turns a few hundred redundant rebuilds into
    one per edition.
    """
    ck = (id(roster), edition.key, tuple(features) if features else None)
    if ck not in _DESIGN_CACHE:
        pool = roster.headline_pool(edition.key, edition.start)
        X = roster.design(edition.key, edition.start, edition.is_florida,
                          pool, features)
        _DESIGN_CACHE[ck] = (pool, X)
    return _DESIGN_CACHE[ck]


def _blocks(roster: Roster, editions, features=None) -> list[tuple[np.ndarray, list[int]]]:
    out = []
    for e in editions:
        pool, X = design_for(roster, e, features)
        idx = {k: i for i, k in enumerate(pool)}
        chosen = [idx[k] for k in e.headliners_booked if k in idx]
        if chosen:
            out.append((X, chosen))
    return out


def fit_headliners(roster: Roster, ridge: float = 1.0,
                   editions=None, features=None,
                   with_cov: bool = True) -> HeadlinerModel:
    feats = list(features or FEATURE_NAMES)
    eds = fit_editions(roster) if editions is None else editions
    blocks = _blocks(roster, eds, feats)
    k = len(feats)
    f = lambda w: _pl_negloglik(w, blocks, ridge)
    best = None
    # Multi-start: the likelihood is convex in w for a fixed pool, but the ridge
    # path can be flat enough that a single start lands on a shoulder.
    for seed in range(4):
        rng = np.random.default_rng(seed)
        x0 = rng.normal(scale=0.3, size=k)
        r = minimize(f, x0, method="L-BFGS-B")
        if best is None or r.fun < best.fun:
            best = r
    # The covariance costs O(k^2) extra likelihood evaluations and is only used
    # to sample coefficient uncertainty in the forward run, never in the
    # backtest -- so the backtest turns it off.
    if with_cov:
        H = _numeric_hessian(f, best.x)
        try:
            cov = np.linalg.inv(H)
            if not np.all(np.isfinite(cov)) or np.any(np.diag(cov) <= 0):
                raise np.linalg.LinAlgError
        except np.linalg.LinAlgError:
            cov = np.eye(k) * 0.25
    else:
        cov = np.eye(k) * 0.25
    return HeadlinerModel(w=best.x, cov=cov, ridge=ridge,
                          n_slots=3, loglik=-best.fun, features=feats)


# ---------------------------------------------------------------------------
# Backtest
# ---------------------------------------------------------------------------

def _topk_from_scores(scores: np.ndarray, k: int) -> list[int]:
    return list(np.argsort(-scores)[:k])


def _score_config(roster: Roster, eds, features, ridge) -> dict:
    hits = model_ll = 0.0
    heat_hits = prev_hits = rand_hits = 0.0
    slots = 0
    for held in eds:
        train = [e for e in eds if e.key != held.key]
        m = fit_headliners(roster, ridge=ridge, editions=train, features=features,
                           with_cov=False)

        pool, X = design_for(roster, held, features)
        idx = {k: i for i, k in enumerate(pool)}
        truth = [k for k in held.headliners_booked if k in idx]
        k_slots = len(truth)
        if not k_slots:
            continue
        slots += k_slots

        u = X @ m.w
        pred = set(pool[i] for i in _topk_from_scores(u, k_slots))
        hits += len(pred & set(truth))
        model_ll += -_pl_negloglik(m.w, [(X, [idx[k] for k in truth])], 0.0)

        # Baseline 1: rank by popularity at booking time alone.
        epoch = BOOKING_EPOCH[held.key]
        heat = np.array([_heat(roster.rank_at(k, epoch) or 200.0) for k in pool])
        heat_hits += len(set(pool[i] for i in _topk_from_scores(heat, k_slots)) & set(truth))

        # Baseline 2: rebook the previous staged flagship's headliners, topping
        # up by popularity if that edition had fewer slots.
        prior = [e for e in eds if e.start < held.start]
        if prior:
            last = max(prior, key=lambda e: e.start)
            guess = [k for k in last.headliners_booked if k in idx][:k_slots]
            if len(guess) < k_slots:
                for i in _topk_from_scores(heat, len(pool)):
                    if pool[i] not in guess:
                        guess.append(pool[i])
                    if len(guess) == k_slots:
                        break
            prev_hits += len(set(guess) & set(truth))

        # Baseline 3: uniform draw from the pool (exact expectation).
        rand_hits += k_slots * k_slots / len(pool)

    return {
        "slots": slots,
        "hit_rate": hits / slots,
        "heat_only_hit_rate": heat_hits / slots,
        "repeat_last_hit_rate": prev_hits / slots,
        "random_hit_rate": rand_hits / slots,
        "loo_loglik": model_ll,
    }


def backtest(roster: Roster,
             ridge_grid=(0.25, 0.5, 1.0, 2.0, 4.0, 8.0),
             feature_sets=None) -> dict:
    """Leave-one-edition-out over both the feature set and the ridge penalty.

    For each held-out edition the model is refitted on the other five and asked
    to name that edition's headline slate. The winning configuration is the one
    with the best LOO predictive log-likelihood -- chosen on held-out fit, never
    on in-sample fit or on which answer looks nicer.

    Reported against three baselines a sceptic would propose. The standing
    caveat applies to every number here: popularity ranks for pre-2026 editions
    were assigned retrospectively, so this is an OPTIMISTIC bound on genuine
    out-of-sample skill, not an estimate of it.
    """
    eds = fit_editions(roster)
    sets = feature_sets or FEATURE_SETS
    grid = {}
    for name, feats in sets.items():
        for ridge in ridge_grid:
            grid[(name, ridge)] = _score_config(roster, eds, feats, ridge)

    best_key = max(grid, key=lambda k: grid[k]["loo_loglik"])
    by_set = {}
    for name in sets:
        k = max((k for k in grid if k[0] == name), key=lambda k: grid[k]["loo_loglik"])
        by_set[name] = {"ridge": k[1], **grid[k]}

    return {
        "grid": {f"{n}|{r}": v for (n, r), v in grid.items()},
        "by_feature_set": by_set,
        "best_feature_set": best_key[0],
        "best_features": list(sets[best_key[0]]),
        "best_ridge": best_key[1],
        "best": grid[best_key],
    }


# ---------------------------------------------------------------------------
# Undercard persistence
# ---------------------------------------------------------------------------

# Fitted without `draw`, the undercard model pooled two populations that behave
# oppositely: headline-tier acts, which Rolling Loud rotates OUT year to year,
# and undercard acts, which it recycles. That forced the popularity and
# prior-appearance coefficients negative, and the model then punished exactly
# the artists with the strongest recurrence records. Controlling for draw
# separates the two populations. Which specification to use is settled by
# held-out fit in `select_undercard`, not by preference.
UNDERCARD_SETS = {
    "base": ["on_prev_bill", "heat", "rl_fit", "regional_fl", "prior_bills"],
    "draw": ["on_prev_bill", "heat", "draw", "rl_fit", "regional_fl", "prior_bills"],
}
UNDERCARD_FEATURES = UNDERCARD_SETS["draw"]


@dataclass
class UndercardModel:
    beta: np.ndarray
    ridge: float
    n_obs: int
    base_return_rate: float
    coverage_note: str
    features: list = None

    def prob(self, x: np.ndarray) -> np.ndarray:
        return expit(x @ self.beta[1:] + self.beta[0])


def undercard_row(roster: Roster, key: str, rank: float, on_prev: bool,
                  is_florida: bool, prior_bills: float, features) -> list:
    a = roster.artists[key]
    col = {
        "on_prev_bill": 1.0 if on_prev else 0.0,
        "heat": _heat(rank),
        "draw": a["draw"],
        "rl_fit": a["rl_fit"],
        "regional_fl": a["regional_fl"] * (1.0 if is_florida else 0.0),
        "prior_bills": float(prior_bills),
    }
    return [col[f] for f in features]


def _undercard_rows(roster: Roster, target, prev, features,
                    universe_rank_cut=110):
    epoch = BOOKING_EPOCH[target.key]
    rows, ys, keys = [], [], []
    for k in roster.artists:
        rank = roster.rank_at(k, epoch)
        if rank is None or rank > universe_rank_cut:
            continue
        rows.append(undercard_row(
            roster, k, rank, k in prev.bill, target.is_florida,
            roster.prior_bill_count(k, target.start), features))
        ys.append(1.0 if k in target.bill else 0.0)
        keys.append(k)
    return np.asarray(rows), np.asarray(ys), keys


def _undercard_transitions(roster: Roster, features, min_prev_reported: int = 10):
    staged = sorted((e for e in roster.editions
                     if e.us_flagship and e.status == "held"), key=lambda e: e.start)
    out = []
    for prev, cur in zip(staged, staged[1:]):
        if len(prev.undercard_reported) < min_prev_reported:
            continue
        X, y, _ = _undercard_rows(roster, cur, prev, features)
        prev_named = set(prev.undercard_reported) | set(prev.headliners_booked)
        out.append((cur.key, X, y, len(prev_named & cur.bill), len(prev_named)))
    return out


def _fit_logistic(X, y, ridge):
    Xd = np.column_stack([np.ones(len(X)), X])

    def nll(b):
        z = Xd @ b
        return float(np.sum(np.logaddexp(0, z) - y * z) + 0.5 * ridge * b[1:] @ b[1:])

    return minimize(nll, np.zeros(Xd.shape[1]), method="L-BFGS-B").x


def select_undercard(roster: Roster, ridge_grid=(0.5, 1.0, 2.0, 4.0)) -> dict:
    """Leave-one-transition-out over undercard specifications.

    Two usable transitions is a two-fold split and nothing more; this settles a
    binary specification question and should not be read as validation of the
    undercard model's calibration, which remains its weakest point.
    """
    out = {}
    for name, feats in UNDERCARD_SETS.items():
        trans = _undercard_transitions(roster, feats)
        for ridge in ridge_grid:
            ll = 0.0
            for i, (_, X, y, _, _) in enumerate(trans):
                tr = [t for j, t in enumerate(trans) if j != i]
                b = _fit_logistic(np.vstack([t[1] for t in tr]),
                                  np.concatenate([t[2] for t in tr]), ridge)
                z = np.column_stack([np.ones(len(X)), X]) @ b
                ll += float(np.sum(y * z - np.logaddexp(0, z)))
            out[(name, ridge)] = ll
    best = max(out, key=out.get)
    return {"grid": {f"{n}|{r}": v for (n, r), v in out.items()},
            "best_set": best[0], "best_features": list(UNDERCARD_SETS[best[0]]),
            "best_ridge": best[1], "best_loo_loglik": out[best]}


def fit_undercard(roster: Roster, ridge: float = 2.0, features=None,
                  min_prev_reported: int = 10) -> UndercardModel:
    feats = list(features or UNDERCARD_FEATURES)
    trans = _undercard_transitions(roster, feats, min_prev_reported)
    X = np.vstack([t[1] for t in trans])
    y = np.concatenate([t[2] for t in trans])
    returns_num = sum(t[3] for t in trans)
    returns_den = sum(t[4] for t in trans)
    beta = _fit_logistic(X, y, ridge)
    return UndercardModel(
        beta=beta, ridge=ridge, n_obs=len(y), features=feats,
        base_return_rate=returns_num / max(returns_den, 1),
        coverage_note=(
            "Undercard rosters are reconstructed from trade coverage, which prints "
            "roughly the top 25-30 of a 78-act bill. An artist absent from a prior "
            "edition's reported roster may still have played it, so the fitted "
            "return rate is a LOWER BOUND on true bill-to-bill persistence, and "
            "these probabilities are scoped to artists prominent enough that a "
            "booking would be reported."
        ),
    )

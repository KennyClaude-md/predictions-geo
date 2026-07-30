"""The Monte Carlo core.

Each simulated path is one possible future. Within a path, every risk node is a
survival process: it has not happened yet, and each quarter it draws against a
hazard that depends on

    baseline (from the elicited cumulative probabilities)
  + epistemic offset  (this parameter-world's opinion about that node)
  + latent factors    (slow-moving global moods: hostility, fragility, forcing)
  + parent effects    (what has already happened, with lags)

Two-level sampling matters here. The outer level draws a *parameter world* — one
coherent opinion about all the hazards at once. The inner level draws paths
within it. Spread across the outer level is epistemic uncertainty (we don't know
the rates); spread within it is aleatory (the world is stochastic). Reporting a
single number blends the two and hides which one is doing the work.

Two features exist for the long horizon and are near-inert at ten years:

  RECURRENCE. Nodes flagged recurrent keep drawing after they fire, because over
  thirty years a recession or an oil spike happens several times. `fire_time`
  still records only the *first* occurrence, which is what the elicited
  "P(at least once by T)" means and what calibration therefore targets; the
  repeat occurrences feed the stress index and the event counts.

  HORIZON CAPPING. Nodes whose criteria are locked to a near-term context stop
  accruing hazard at their last resolvable quarter, so "the 2026-27 El Nino"
  cannot fire in 2053.

Stress is accumulated inside the loop rather than reconstructed afterwards,
because with recurrence a fire-time matrix no longer contains enough information
to rebuild it.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .continuous import STRESS_DECAY_QUARTERS
from .hazard import expit, logit, piecewise_quarter_hazard
from .params import BlockingPair, WorldModel
from .timeline import YEARS_PER_QUARTER, active, anchor_quarters, n_quarters

NEVER = -1
# Hazard multiplier applied to a node whose mutually-exclusive partner has fired.
BLOCK_MULTIPLIER = 0.18
# Per-quarter hazard is clipped here: no node becomes a certainty within one
# quarter no matter how many parents have fired.
MAX_QUARTER_HAZARD = 0.55


@dataclass
class SimConfig:
    n_worlds: int = 700
    paths_per_world: int = 500
    batch_paths: int = 30_000
    seed: int = 20260729
    latent_half_life_years: float = 3.0
    # Epistemic variance dominates the calibration signal, so the efficient
    # allocation is many parameter worlds with few paths each — not the reverse.
    calib_worlds: int = 1400
    calib_paths_per_world: int = 50
    calib_iters: int = 10
    # Full stress trajectories kept for quantile bands. Summaries are kept for
    # every path; trajectories only for a sample, because (n_paths x quarters)
    # floats is the one array that does not fit at the long horizon.
    traj_sample: int = 40_000

    @property
    def n_paths(self) -> int:
        return self.n_worlds * self.paths_per_world


class CompiledModel:
    """Flattened, array-shaped view of a WorldModel, ready for the hot loop."""

    def __init__(self, model: WorldModel, config: SimConfig):
        self.model = model
        self.config = config
        self.horizon = active()
        self.risk_ids = sorted(model.risks)
        self.index = {rid: i for i, rid in enumerate(self.risk_ids)}
        R = len(self.risk_ids)
        self.R = R
        T = n_quarters()
        self.T = T

        self.severity = np.array(
            [model.risks[r].severity for r in self.risk_ids], dtype=np.float32
        )
        self.signed_severity = np.array(
            [model.risks[r].signed_severity for r in self.risk_ids], dtype=np.float32
        )
        self.sigma = np.array([model.risks[r].sigma for r in self.risk_ids], dtype=np.float32)
        self.domains = [model.risks[r].domain for r in self.risk_ids]
        self.recurrent = np.array(
            [bool(model.risks[r].recurrent) for r in self.risk_ids], dtype=bool
        )

        # Baseline per-quarter hazard from the elicited CDF, shape (T, R).
        haz = np.empty((T, R), dtype=np.float64)
        self.extrapolated = np.zeros(R, dtype=bool)
        for rid in self.risk_ids:
            r = model.risks[rid]
            j = self.index[rid]
            vals, was_extrapolated = r.anchor_values()
            self.extrapolated[j] = was_extrapolated
            haz[:, j] = piecewise_quarter_hazard(*vals, max_quarter=r.max_quarter())
        self.base_hazard = haz
        # Multiplicative correction learned by the marginal-calibration loop,
        # one factor per (elicitation segment, risk).
        self.n_segments = self.horizon.n_segments
        self.hazard_scale = np.ones((self.n_segments, R), dtype=np.float64)

        # --- edges, including blocking pairs expressed as protective edges ---
        edges = list(model.edges) + _blocks_as_edges(model.blocks)
        self.edge_src = np.array([self.index[e.source] for e in edges], dtype=np.int32)
        self.edge_tgt = np.array([self.index[e.target] for e in edges], dtype=np.int32)
        self.edge_lm = np.array([e.log_odds for e in edges], dtype=np.float32)
        self.edge_lag = np.array(
            [max(0, min(e.lag_quarters, T)) for e in edges], dtype=np.int16
        )
        self.edges = edges
        self.E = len(edges)

        # --- latent factor loadings, shape (K, R) ---
        K = max(len(model.latents), 1)
        loadings = np.zeros((K, R), dtype=np.float32)
        for k, lf in enumerate(model.latents):
            for rid, val in lf.loadings.items():
                loadings[k, self.index[rid]] = val
        self.loadings = loadings
        self.K = K
        # Loadings are unit-scale opinions; this converts them to log-odds impact.
        self.latent_gain = np.float32(0.85)

        phi = 0.5 ** (YEARS_PER_QUARTER / config.latent_half_life_years)
        self.latent_phi = np.float32(phi)
        self.latent_innov = np.float32(np.sqrt(1.0 - phi**2))

    def segment_of_quarter(self) -> np.ndarray:
        """Map each quarter index (0-based) to its elicitation segment."""
        seg = np.empty(self.T, dtype=np.int16)
        prev = 0
        for s, q in enumerate(anchor_quarters()):
            seg[prev:q] = s
            prev = q
        return seg

    def effective_hazard(self) -> np.ndarray:
        seg = self.segment_of_quarter()
        return np.clip(self.base_hazard * self.hazard_scale[seg, :], 0.0, 0.90)

    def base_logit(self) -> np.ndarray:
        """Log-odds of the baseline hazard; -inf where a node cannot fire."""
        h = self.effective_hazard()
        out = np.full_like(h, -60.0, dtype=np.float32)
        live = h > 0
        out[live] = logit(h[live]).astype(np.float32)
        return out


def _blocks_as_edges(blocks: list[BlockingPair]):
    from .params import Edge

    out = []
    for bp in blocks:
        out.append(Edge(bp.a, bp.b, BLOCK_MULTIPLIER, 0, "mutual exclusion", "medium"))
        out.append(Edge(bp.b, bp.a, BLOCK_MULTIPLIER, 0, "mutual exclusion", "medium"))
    return out


def simulate(
    cm: CompiledModel,
    n_worlds: int,
    paths_per_world: int,
    rng: np.random.Generator,
    batch_paths: int = 30_000,
    antithetic: bool = True,
    with_stress: bool = False,
    traj_sample: int = 40_000,
) -> dict:
    """Run the Monte Carlo.

    Parameter worlds are drawn in antithetic pairs: every offset +theta is matched
    by a -theta. The sample mean of the epistemic offsets is then exactly zero
    rather than approximately zero, which roughly halves the standard error on
    every marginal without costing a single extra path. This matters most for the
    calibration loop, which otherwise spends its iterations chasing sampling noise.

    Returns
        fire_time : (n_paths, R) int16, quarter of FIRST occurrence or -1
        world_id  : (n_paths,) int32, which parameter world each path belongs to
      and when `with_stress`:
        n_fires      : (n_paths, R) uint8, occurrence count (recurrent nodes >1)
        stress_peak / stress_early / stress_late : (n_paths,) float32
        stress_traj  : (k, T) float32 sample, for quantile bands
    """
    R, T = cm.R, cm.T
    n_paths = n_worlds * paths_per_world
    base_logit = cm.base_logit()

    # int16, not int8: the long horizon has 122 quarters and int8 would wrap.
    fire_time = np.full((n_paths, R), NEVER, dtype=np.int16)
    world_id = np.repeat(np.arange(n_worlds, dtype=np.int32), paths_per_world)

    n_fires = np.zeros((n_paths, R), dtype=np.uint8) if with_stress else None
    s_peak = np.zeros(n_paths, dtype=np.float32) if with_stress else None
    s_early = np.zeros(n_paths, dtype=np.float32) if with_stress else None
    s_late = np.zeros(n_paths, dtype=np.float32) if with_stress else None
    traj_keep: list[np.ndarray] = []
    traj_budget = traj_sample if with_stress else 0

    early_q = max(1, min(12, T))
    late_q = max(1, min(8, T))
    decay = np.float32(np.exp(-1.0 / STRESS_DECAY_QUARTERS))

    # One epistemic offset per parameter world, shared by all its paths.
    if antithetic:
        half = (n_worlds + 1) // 2
        draws = rng.standard_normal((half, R)).astype(np.float32)
        theta_worlds = np.concatenate([draws, -draws], axis=0)[:n_worlds] * cm.sigma
    else:
        theta_worlds = rng.standard_normal((n_worlds, R)).astype(np.float32) * cm.sigma

    worlds_per_batch = max(1, batch_paths // paths_per_world)
    for w0 in range(0, n_worlds, worlds_per_batch):
        w1 = min(w0 + worlds_per_batch, n_worlds)
        nb = (w1 - w0) * paths_per_world
        lo, hi = w0 * paths_per_world, w1 * paths_per_world

        theta = np.repeat(theta_worlds[w0:w1], paths_per_world, axis=0)
        latent = rng.standard_normal((nb, cm.K)).astype(np.float32)  # stationary start
        ft = np.full((nb, R), NEVER, dtype=np.int16)
        cnt = np.zeros((nb, R), dtype=np.uint8) if with_stress else None
        cur = np.zeros(nb, dtype=np.float32) if with_stress else None
        traj = np.zeros((nb, T), dtype=np.float32) if with_stress else None

        for t in range(1, T + 1):
            latent *= cm.latent_phi
            latent += cm.latent_innov * rng.standard_normal((nb, cm.K)).astype(np.float32)

            z = base_logit[t - 1][None, :] + theta
            z = z + cm.latent_gain * (latent @ cm.loadings)

            # Parent effects. Looping over edges beats a dense (nb,E)@(E,R) matmul
            # by two orders of magnitude here — E is small and each edge touches
            # exactly one column.
            #
            # Fire times for this quarter are written after the draw, so a parent
            # is only visible to its children from the *following* quarter. That
            # makes lag=0 mean "next quarter", and removes any dependence on the
            # order edges happen to be listed in.
            for e in range(cm.E):
                src = ft[:, cm.edge_src[e]]
                act = (src >= 0) & ((t - src) >= cm.edge_lag[e])
                z[:, cm.edge_tgt[e]] += cm.edge_lm[e] * act

            p = expit(z.astype(np.float64))
            np.minimum(p, MAX_QUARTER_HAZARD, out=p)
            # A node with no baseline hazard this quarter cannot be revived by a
            # parent: horizon capping is a statement about resolvability, not risk.
            p[:, :] = np.where(base_logit[t - 1][None, :] <= -59.0, 0.0, p)

            u = rng.random((nb, R))
            fires = u < p
            if not cm.recurrent.all():
                # Non-recurrent nodes fire once; recurrent ones keep drawing.
                fires &= cm.recurrent[None, :] | (ft < 0)

            if fires.any():
                first = fires & (ft < 0)
                ft[first] = t
                if with_stress:
                    np.add(cnt, fires, out=cnt, casting="unsafe")

            if with_stress:
                cur *= decay
                cur += (fires * cm.signed_severity[None, :]).sum(axis=1)
                traj[:, t - 1] = cur

        fire_time[lo:hi] = ft
        if with_stress:
            n_fires[lo:hi] = cnt
            s_peak[lo:hi] = traj.max(axis=1)
            s_early[lo:hi] = traj[:, :early_q].mean(axis=1)
            s_late[lo:hi] = traj[:, -late_q:].mean(axis=1)
            if traj_budget > 0:
                take = min(traj_budget, nb)
                traj_keep.append(traj[:take].copy())
                traj_budget -= take

    out = {"fire_time": fire_time, "world_id": world_id, "risk_ids": cm.risk_ids}
    if with_stress:
        out.update(
            n_fires=n_fires,
            stress_peak=s_peak,
            stress_early=s_early,
            stress_late=s_late,
            stress_traj=(
                np.concatenate(traj_keep, axis=0) if traj_keep
                else np.zeros((0, T), dtype=np.float32)
            ),
        )
    return out


def cumulative_marginals(fire_time: np.ndarray, quarters: list[int]) -> np.ndarray:
    """P(fired at least once by q) for each risk, shape (len(quarters), R)."""
    ft = fire_time.astype(np.int32)
    out = np.empty((len(quarters), ft.shape[1]), dtype=np.float64)
    for i, q in enumerate(quarters):
        out[i] = ((ft >= 0) & (ft <= q)).mean(axis=0)
    return out


def calibrate_marginals(cm: CompiledModel, config: SimConfig, verbose: bool = True) -> dict:
    """Tune baseline hazards so simulated marginals reproduce elicited ones.

    Without this step the coupling layer would silently inflate every probability:
    latent factors add convexity, and parent effects only ever push hazard up. The
    resulting numbers would be higher than any analyst actually claimed, while
    looking like they came from the analysts.

    With it, the elicited marginals are respected and the dependency structure
    does what it should — reshape the *joint* distribution, producing correlated
    world-states and non-trivial conditionals, at fixed marginals.

    Recurrent nodes calibrate on first-occurrence too, because "P(at least once by
    T)" is the quantity that was elicited. Their repeat firings are a consequence
    of the fitted rate, not a separate free parameter.
    """
    anchors = anchor_quarters()
    n_seg = len(anchors)

    # The target is the elicited CDF itself — the uncorrected baseline hazard,
    # before any scaling this loop has already applied.
    target_cdf = 1.0 - np.cumprod(1.0 - cm.base_hazard, axis=0)
    target = np.stack([target_cdf[q - 1] for q in anchors])

    tgt_surv = 1.0 - np.clip(target, 1e-6, 0.999)
    tgt_H = np.empty((n_seg, cm.R))
    prev = np.ones(cm.R)
    for s in range(n_seg):
        tgt_H[s] = -np.log(tgt_surv[s] / prev)
        prev = tgt_surv[s]

    history = []
    for it in range(config.calib_iters):
        # Common random numbers: the same draws every iteration, so successive
        # estimates differ only because the parameters changed. Without this the
        # loop oscillates around the fixed point at the amplitude of its own
        # Monte Carlo error instead of settling into it.
        res = simulate(
            cm,
            config.calib_worlds,
            config.calib_paths_per_world,
            np.random.default_rng(config.seed + 991),
            batch_paths=config.batch_paths,
        )
        sim = cumulative_marginals(res["fire_time"], anchors)
        sim_surv = 1.0 - np.clip(sim, 1e-6, 0.9995)
        sim_H = np.empty((n_seg, cm.R))
        prev = np.ones(cm.R)
        for s in range(n_seg):
            sim_H[s] = -np.log(sim_surv[s] / prev)
            prev = sim_surv[s]

        err = np.abs(sim - target).max()
        history.append(float(err))
        if verbose:
            print(
                f"    calib iter {it}: max |sim-target| = {err*100:5.2f}pp   "
                f"mean = {np.abs(sim-target).mean()*100:5.3f}pp"
            )
        if err < 0.004 and it >= 2:
            break

        ratio = tgt_H / np.maximum(sim_H, 1e-9)
        # Damped multiplicative update, with the damping increasing over the run:
        # early iterations need to move far, later ones need to stop moving.
        step = 0.85 if it < 3 else 0.55
        cm.hazard_scale *= np.clip(ratio, 0.2, 5.0) ** step
        cm.hazard_scale = np.clip(cm.hazard_scale, 1e-4, 1e4)

    return {"history": history, "final_error_pp": history[-1] * 100 if history else None}

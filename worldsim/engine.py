"""The Monte Carlo core.

Each simulated path is one possible decade. Within a path, every risk node is a
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

Absorbing by construction: each node fires at most once, and we record *when*.
Everything downstream — marginals at any horizon, conditional probabilities,
cascade chains, the stress index — is derived from that fire-time matrix.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .hazard import expit, logit, piecewise_quarter_hazard
from .params import BlockingPair, WorldModel
from .timeline import ANCHOR_QUARTERS, N_QUARTERS, YEARS_PER_QUARTER

NEVER = -1
# Hazard multiplier applied to a node whose mutually-exclusive partner has fired.
BLOCK_MULTIPLIER = 0.18
# Per-quarter hazard is clipped here: no node is allowed to become a certainty
# within one quarter no matter how many parents have fired.
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

    @property
    def n_paths(self) -> int:
        return self.n_worlds * self.paths_per_world


class CompiledModel:
    """Flattened, array-shaped view of a WorldModel, ready for the hot loop."""

    def __init__(self, model: WorldModel, config: SimConfig):
        self.model = model
        self.config = config
        self.risk_ids = sorted(model.risks)
        self.index = {rid: i for i, rid in enumerate(self.risk_ids)}
        R = len(self.risk_ids)
        self.R = R

        self.severity = np.array(
            [model.risks[r].severity for r in self.risk_ids], dtype=np.float32
        )
        self.sigma = np.array([model.risks[r].sigma for r in self.risk_ids], dtype=np.float32)
        self.domains = [model.risks[r].domain for r in self.risk_ids]

        # Baseline per-quarter hazard from the elicited CDF, shape (T, R).
        haz = np.empty((N_QUARTERS, R), dtype=np.float64)
        for rid in self.risk_ids:
            r = model.risks[rid]
            haz[:, self.index[rid]] = piecewise_quarter_hazard(r.p2027, r.p2031, r.p2036)
        self.base_hazard = haz
        # Multiplicative correction learned by the marginal-calibration loop,
        # one factor per (elicitation segment, risk).
        self.hazard_scale = np.ones((3, R), dtype=np.float64)

        # --- edges, including blocking pairs expressed as protective edges ---
        edges = list(model.edges) + _blocks_as_edges(model.blocks)
        self.edge_src = np.array([self.index[e.source] for e in edges], dtype=np.int32)
        self.edge_tgt = np.array([self.index[e.target] for e in edges], dtype=np.int32)
        self.edge_lm = np.array([e.log_odds for e in edges], dtype=np.float32)
        self.edge_lag = np.array(
            [max(0, min(e.lag_quarters, N_QUARTERS)) for e in edges], dtype=np.int16
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
        """Map each quarter index (0-based) to its elicitation segment 0/1/2."""
        q1 = ANCHOR_QUARTERS["p_by_2027_pct"]
        q2 = ANCHOR_QUARTERS["p_by_2031_pct"]
        seg = np.full(N_QUARTERS, 2, dtype=np.int8)
        seg[:q1] = 0
        seg[q1:q2] = 1
        return seg

    def effective_hazard(self) -> np.ndarray:
        seg = self.segment_of_quarter()
        return np.clip(self.base_hazard * self.hazard_scale[seg, :], 1e-9, 0.90)

    def base_logit(self) -> np.ndarray:
        return logit(self.effective_hazard()).astype(np.float32)


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
    collect_latent: bool = False,
    antithetic: bool = True,
) -> dict:
    """Run the Monte Carlo and return fire times plus world labels.

    Parameter worlds are drawn in antithetic pairs: every offset +theta is matched
    by a -theta. The sample mean of the epistemic offsets is then exactly zero
    rather than approximately zero, which roughly halves the standard error on
    every marginal without costing a single extra path. This matters most for the
    calibration loop, which otherwise spends its iterations chasing sampling noise.

    Returns
        fire_time : (n_paths, R) int8, quarter index of first occurrence or -1
        world_id  : (n_paths,) int32, which parameter world each path belongs to
    """
    R = cm.R
    n_paths = n_worlds * paths_per_world
    base_logit = cm.base_logit()  # (T, R)

    fire_time = np.full((n_paths, R), NEVER, dtype=np.int8)
    world_id = np.repeat(np.arange(n_worlds, dtype=np.int32), paths_per_world)

    # One epistemic offset per parameter world, shared by all its paths.
    if antithetic:
        half = (n_worlds + 1) // 2
        draws = rng.standard_normal((half, R)).astype(np.float32)
        theta_worlds = np.concatenate([draws, -draws], axis=0)[:n_worlds] * cm.sigma
    else:
        theta_worlds = rng.standard_normal((n_worlds, R)).astype(np.float32) * cm.sigma

    latent_trace = None
    if collect_latent:
        latent_trace = np.zeros((N_QUARTERS, cm.K), dtype=np.float32)

    # Batches must not split a parameter world across boundaries.
    worlds_per_batch = max(1, batch_paths // paths_per_world)
    for w0 in range(0, n_worlds, worlds_per_batch):
        w1 = min(w0 + worlds_per_batch, n_worlds)
        nb = (w1 - w0) * paths_per_world
        lo = w0 * paths_per_world
        hi = w1 * paths_per_world

        theta = np.repeat(theta_worlds[w0:w1], paths_per_world, axis=0)  # (nb, R)
        latent = rng.standard_normal((nb, cm.K)).astype(np.float32)  # stationary start
        ft = np.full((nb, R), NEVER, dtype=np.int16)

        for t in range(1, N_QUARTERS + 1):
            latent *= cm.latent_phi
            latent += cm.latent_innov * rng.standard_normal((nb, cm.K)).astype(np.float32)
            if collect_latent:
                latent_trace[t - 1] += latent.mean(axis=0) * nb

            z = base_logit[t - 1][None, :] + theta
            z = z + cm.latent_gain * (latent @ cm.loadings)

            # Parent effects. Looping over edges beats a dense (nb,E)@(E,R) matmul
            # by two orders of magnitude here — E is small and each edge touches
            # exactly one column.
            for e in range(cm.E):
                src = ft[:, cm.edge_src[e]]
                active = (src >= 0) & ((t - src) >= cm.edge_lag[e])
                z[:, cm.edge_tgt[e]] += cm.edge_lm[e] * active

            p = expit(z.astype(np.float64))
            np.minimum(p, MAX_QUARTER_HAZARD, out=p)
            alive = ft < 0
            u = rng.random((nb, R))
            fires = alive & (u < p)
            if fires.any():
                ft[fires] = t

        fire_time[lo:hi] = ft.astype(np.int8)

    out = {"fire_time": fire_time, "world_id": world_id, "risk_ids": cm.risk_ids}
    if collect_latent:
        out["latent_trace"] = latent_trace / n_paths
    return out


def cumulative_marginals(fire_time: np.ndarray, quarters: list[int]) -> np.ndarray:
    """P(fired by q) for each risk, shape (len(quarters), R)."""
    ft = fire_time.astype(np.int16)
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
    """
    q1 = ANCHOR_QUARTERS["p_by_2027_pct"]
    q2 = ANCHOR_QUARTERS["p_by_2031_pct"]
    q3 = ANCHOR_QUARTERS["p_by_2036_pct"]
    anchors = [q1, q2, q3]

    target = np.empty((3, cm.R), dtype=np.float64)
    raw_h = np.empty((N_QUARTERS, cm.R), dtype=np.float64)
    for rid in cm.risk_ids:
        j = cm.index[rid]
        raw_h[:, j] = cm.base_hazard[:, j]
    target_cdf = 1.0 - np.cumprod(1.0 - raw_h, axis=0)
    for i, q in enumerate(anchors):
        target[i] = target_cdf[q - 1]

    # Segment-conditional cumulative hazards we are trying to match.
    tgt_surv = 1.0 - np.clip(target, 1e-6, 0.999)
    tgt_H = np.empty((3, cm.R))
    tgt_H[0] = -np.log(tgt_surv[0])
    tgt_H[1] = -np.log(tgt_surv[1] / tgt_surv[0])
    tgt_H[2] = -np.log(tgt_surv[2] / tgt_surv[1])

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
        sim_H = np.empty((3, cm.R))
        sim_H[0] = -np.log(sim_surv[0])
        sim_H[1] = -np.log(sim_surv[1] / sim_surv[0])
        sim_H[2] = -np.log(sim_surv[2] / sim_surv[1])

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

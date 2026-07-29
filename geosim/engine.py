"""GEO-SIM Monte Carlo core.

The world is modelled as a coupled stochastic dynamical system marched forward
in quarterly steps. Four things happen at every step, in this order:

  1. The regime switches (or doesn't). Regimes are a slow Markov layer that
     scales volatility and crisis hazards globally -- the model's way of saying
     that the same tension index means something different in 1995 than in 1938.
  2. Continuous indicators evolve: mean reversion toward a drifting attractor,
     plus lagged cross-domain coupling, plus correlated fat-tailed innovations,
     plus stabilizing feedbacks that only engage once a variable is stressed.
  3. Discrete events fire or don't, with hazards modulated by indicator levels,
     by the regime, and by whatever else has already fired (contagion).
  4. Events that fired shock the indicators, closing the loop.

Two features matter more than the rest for the credibility of the output.

First, *parameter uncertainty is sampled per path*. Every path draws its own
hazards, volatilities, drifts and coupling strengths from priors centred on the
analysts' estimates. A run therefore integrates over "we don't know the
parameters" as well as "the world is random", which is the difference between
an honest interval and a fake one.

Second, *hazards are calibrated in two passes*. Because hazard is exponential in
indicator z-scores, the average hazard across paths exceeds the hazard at the
average state -- Jensen's inequality would silently inflate every probability
above what the analysts actually said. Pass one fits a per-event offset against
a decoupled baseline so marginals reproduce the elicited priors. Pass two turns
contagion and regimes on and holds those offsets fixed. The gap between the two
is not noise: it is the model's estimate of systemic amplification, and it is
reported as a first-class output.
"""

from __future__ import annotations

import math

import numpy as np

from .params import CompiledParams

QPY = 4
DT = 1.0 / QPY

# Student-t degrees of freedom for indicator innovations. Five is deliberately
# heavy: macro-financial and conflict series have kurtosis far above Gaussian,
# and a Gaussian world model is the single most common way forecasts understate
# tail risk.
NU = 5.0

Z_CLIP = 4.0          # z-scores beyond this stop moving hazards
LOGH_CLIP = 3.0       # total log-hazard modulation, i.e. 0.05x .. 20x
MAX_Q_PROB = 0.6      # no event may be near-certain within a single quarter

# Fraction of each event's log-hazard uncertainty that is common across all
# events rather than idiosyncratic -- i.e. how correlated the analysts'
# errors are. Set from the forecasting-aggregation convention that a
# meaningful minority of elicitation error is method-level rather than
# question-level.
HAZARD_SHARED = 0.35


class Simulator:
    def __init__(self, P: CompiledParams, horizon_years: float = 10.5, seed: int = 20260729,
                 param_uncertainty: bool = True):
        self.P = P
        self.T = int(round(horizon_years * QPY))
        self.seed = seed
        # When False, every path uses the analysts' central parameter values.
        # Running both ways decomposes the forecast's uncertainty into the part
        # that is irreducible given the parameters and the part that is just not
        # knowing them -- and makes the engine analytically testable.
        self.param_uncertainty = param_uncertainty
        self.K = len(P.indicators)
        self.E = len(P.events)
        self.R = len(P.regimes)
        self.max_lag = max(P.coupling_by_lag.keys(), default=0)

    # ------------------------------------------------------------------ #
    # per-path parameter draws: epistemic uncertainty
    # ------------------------------------------------------------------ #
    def _draw_params(self, rng, n, coupled: bool):
        P = self.P
        d = {}
        jit = self.param_uncertainty
        logh = np.log(np.maximum(P.base_hazard, 1e-9))[None, :] + P.calib_offset[None, :]

        if jit:
            # Hazards: lognormal around the elicited value, width set by the
            # analyst's own stated confidence.
            #
            # The error is split into a shared component and an idiosyncratic
            # one. Purely independent jitter would say the analysts are wrong
            # about each event in unrelated directions, so their errors cancel
            # in aggregate and the *number* of shocks in a decade is known far
            # better than any individual shock. That is not how forecasting
            # miscalibration works: an elicitation process that is systematically
            # too jumpy is too jumpy about everything at once. HAZARD_SHARED is
            # the fraction of log-hazard error variance that is common, and it
            # is what keeps the tail of the shock-count distribution honest.
            c = rng.standard_normal((n, 1))
            i = rng.standard_normal((n, self.E))
            err = math.sqrt(HAZARD_SHARED) * c + math.sqrt(1.0 - HAZARD_SHARED) * i
            d["hazard"] = np.exp(logh + P.conf_sigma[None, :] * err)

            # Volatility is itself uncertain, and uncertainty about volatility is
            # multiplicative -- hence lognormal rather than additive jitter.
            d["vol"] = P.vol[None, :] * np.exp(0.22 * rng.standard_normal((n, self.K)))

            # Drift uncertainty has a floor so that indicators the analysts
            # marked as trendless are not treated as known to be trendless.
            drift_sd = 0.35 * np.abs(P.drift) + 0.12 * P.vol
            d["drift"] = P.drift[None, :] + drift_sd[None, :] * rng.standard_normal((n, self.K))

            # Mean reversion: how fast the world snaps back is genuinely contested.
            d["kappa"] = np.clip(
                P.kappa[None, :] * np.exp(0.30 * rng.standard_normal((n, self.K))), 0.0, 2.5
            )
        else:
            d["hazard"] = np.repeat(np.exp(logh), n, axis=0)
            d["vol"] = np.repeat(P.vol[None, :], n, axis=0)
            d["drift"] = np.repeat(P.drift[None, :], n, axis=0)
            d["kappa"] = np.repeat(P.kappa[None, :], n, axis=0)

        # Coupling strengths get one shared multiplier per path per lag matrix.
        # A common factor is the right structure: the live disagreement is
        # whether the world is tightly or loosely coupled overall, not whether
        # any individual edge is mis-signed.
        if not coupled:
            d["coup_mult"] = np.zeros((n, 1, 1))
            d["contagion_mult"] = np.zeros((n, 1))
        elif jit:
            d["coup_mult"] = 1.0 + 0.35 * rng.standard_normal((n, 1, 1))
            d["contagion_mult"] = np.clip(1.0 + 0.30 * rng.standard_normal((n, 1)), 0.0, None)
        else:
            d["coup_mult"] = np.ones((n, 1, 1))
            d["contagion_mult"] = np.ones((n, 1))
        return d

    # ------------------------------------------------------------------ #
    # one chunk of paths
    # ------------------------------------------------------------------ #
    def _run_chunk(self, rng, n, coupled: bool, record_paths: int = 0):
        P = self.P
        T, K, E, R = self.T, self.K, self.E, self.R
        pd = self._draw_params(rng, n, coupled)

        x = np.repeat(P.x0[None, :], n, axis=0)
        hist = [np.zeros((n, K)) for _ in range(self.max_lag + 1)]  # z history ring

        fired = np.zeros((n, E), dtype=bool)
        fire_q = np.full((n, E), -1, dtype=np.int32)   # quarter of first firing
        fire_count = np.zeros((n, E), dtype=np.int16)
        log_amp = np.zeros((n, E))                      # live contagion amplification
        exhaustion = np.zeros((n, E))                   # post-event recurrence damping

        regime = rng.choice(R, size=n, p=P.regime_p0) if R else np.zeros(n, dtype=int)
        regime_time = np.zeros((n, R))

        c_src, c_dst, c_logmult, c_decay = P.contagion_idx
        s_trig, s_damp, s_str = P.stab_idx
        has_contagion = coupled and len(c_src) > 0

        traj = np.zeros((min(record_paths, n), T + 1, K), dtype=np.float32) if record_paths else None
        if traj is not None:
            traj[:, 0, :] = x[: traj.shape[0]]

        # Peak stress observed along the path, in z units. Used downstream to
        # separate "ended badly" from "went through hell and recovered".
        peak_z = np.zeros((n, K))

        for t in range(T):
            # --- 1. regime transition ---------------------------------------
            # Regimes are switched off in the decoupled calibration pass so
            # that their contribution shows up as measured amplification rather
            # than being absorbed into the fitted offsets.
            if R and coupled:
                u = rng.random(n)
                cdf = np.cumsum(P.regime_trans_q[regime], axis=1)
                regime = (u[:, None] > cdf).sum(axis=1).clip(0, R - 1)
                regime_time[np.arange(n), regime] += 1
                rv = P.regime_vol[regime]
                rh = P.regime_hazard[regime]
            else:
                rv = np.ones(n)
                rh = np.ones(n)

            # --- 2. continuous dynamics -------------------------------------
            target = P.attractor[None, :] + pd["drift"] * (t * DT)
            dx = pd["kappa"] * (target - x) * DT + pd["drift"] * DT

            if coupled and P.coupling_by_lag:
                cz = np.zeros((n, K))
                for lag, M in P.coupling_by_lag.items():
                    zl = hist[-1 - lag] if lag < len(hist) else hist[0]
                    cz += zl @ M.T
                dx += pd["coup_mult"][:, 0, :] * cz * P.scale[None, :] * DT

            # Correlated Student-t innovations. One chi-square mixing variable
            # per path per quarter keeps the correlation structure intact while
            # producing joint tail events -- the crises that arrive together.
            #
            # The (NU-2) numerator normalises the mixture to unit variance.
            # A t_nu variate has variance nu/(nu-2), so the naive sqrt(nu/chi2)
            # scaling silently inflates every indicator's volatility by 29% at
            # nu=5 -- the analysts' elicited annual_vol would not mean what they
            # said it meant.
            g = rng.standard_normal((n, K)) @ P.chol.T
            mix = np.sqrt((NU - 2.0) / rng.chisquare(NU, size=(n, 1)))
            shock = g * mix * pd["vol"] * np.sqrt(DT) * rv[:, None]
            dx += shock

            x = x + dx

            # Stabilizing feedbacks: a restoring force that only switches on
            # once the trigger is more than 1 SD from its attractor. Modelling
            # these as always-on would just be extra mean reversion; the point
            # is that societies mobilise responses in proportion to visible
            # stress, and only once it is visible.
            if coupled and len(s_trig):
                z_now = np.clip((x - P.zref[None, :]) / P.scale[None, :], -Z_CLIP, Z_CLIP)
                stress = np.maximum(np.abs(z_now[:, s_trig]) - 1.0, 0.0) * np.sign(z_now[:, s_trig])
                damp = stress * s_str[None, :] * P.scale[s_damp][None, :] * DT
                np.subtract.at(x.T, s_damp, damp.T)

            x = np.clip(x, P.lo[None, :], P.hi[None, :])

            z = np.clip((x - P.zref[None, :]) / P.scale[None, :], -Z_CLIP, Z_CLIP)
            peak_z = np.maximum(peak_z, np.abs(z))
            hist.append(z)
            if len(hist) > self.max_lag + 1:
                hist.pop(0)

            # --- 3. event hazards -------------------------------------------
            logmod = np.clip(z @ P.elasticity.T, -LOGH_CLIP, LOGH_CLIP)
            h = pd["hazard"] * np.exp(logmod)
            if coupled:
                h = h * rh[:, None] * np.exp(np.clip(log_amp, -LOGH_CLIP, LOGH_CLIP))
            h = h * np.exp(-exhaustion)

            # Absorbing events cannot recur; non-absorbing ones can, which is
            # what makes "recession" and "war" behave differently from
            # "first nuclear detonation since 1945".
            live = ~(fired & P.absorbing[None, :])
            p = np.minimum(1.0 - np.exp(-h * DT), MAX_Q_PROB) * live
            hit = rng.random((n, E)) < p

            # --- 4. feedback into the world ---------------------------------
            if hit.any():
                newly = hit & ~fired
                fire_q[newly] = t
                fired |= hit
                fire_count += hit.astype(np.int16)

                # Impacts are expressed in SDs of the target indicator.
                x = x + (hit.astype(np.float64) @ P.impact) * P.scale[None, :]
                x = np.clip(x, P.lo[None, :], P.hi[None, :])

                if has_contagion:
                    trig = hit[:, c_src].astype(np.float64)
                    add = trig * c_logmult[None, :] * pd["contagion_mult"]
                    np.add.at(log_amp.T, c_dst, add.T)

                # Exhaustion: having just happened, a thing is briefly less
                # likely to happen again. Wars deplete materiel, crises deplete
                # political appetite, and markets that just crashed are cheap.
                exhaustion += hit.astype(np.float64) * 0.9

            if has_contagion:
                # Each event decays its inherited amplification at its own rate:
                # a shipping disruption fades in two quarters, a proliferation
                # cascade does not.
                log_amp *= P.contagion_decay_factor[None, :]
            exhaustion *= np.exp(-1.0 / 6.0)

            if traj is not None:
                traj[:, t + 1, :] = x[: traj.shape[0]]

        return {
            "x_final": x,
            "fired": fired,
            "fire_q": fire_q,
            "fire_count": fire_count,
            "regime_time": regime_time / max(self.T, 1),
            "regime_final": regime,
            "peak_z": peak_z,
            "traj": traj,
            "draws": {k: v for k, v in pd.items() if k in ("coup_mult", "contagion_mult")},
        }

    # ------------------------------------------------------------------ #
    # calibration: make decoupled marginals reproduce the elicited priors
    # ------------------------------------------------------------------ #
    def calibrate(self, n=48_000, iters=4, verbose=True):
        P = self.P
        P.calib_offset = np.zeros(self.E)
        target = np.array(
            [
                min(max(float(ev.p_by.get(2036) or 1 - np.exp(-ev.prior_hazard * 10.42)), 5e-4), 0.995)
                for ev in P.events
            ]
        )

        for it in range(iters):
            rng = np.random.default_rng(self.seed + 9000 + it)
            res = self._run_chunk(rng, n, coupled=False)
            sim = res["fired"].mean(axis=0)
            sim = np.clip(sim, 1e-4, 0.9995)
            # Exact correction under a constant-hazard assumption; iterating
            # handles the state-dependence that makes it inexact.
            adj = np.log(np.log(1 - target) / np.log(1 - sim))
            P.calib_offset += np.clip(adj, -2.5, 2.5)
            if verbose:
                err = np.abs(sim - target)
                print(
                    f"  calibration pass {it + 1}: median |err| = {np.median(err):.4f}, "
                    f"max |err| = {err.max():.4f} ({P.events[int(err.argmax())].id})"
                )
        return target

    # ------------------------------------------------------------------ #
    def run(self, n_paths=200_000, chunk=10_000, coupled=True, record_paths=6_000, verbose=True):
        chunks = int(np.ceil(n_paths / chunk))
        out = {"fired": [], "fire_q": [], "fire_count": [], "x_final": [],
               "regime_time": [], "peak_z": [], "coup": []}
        traj = None
        left = record_paths

        for c in range(chunks):
            rng = np.random.default_rng(self.seed + 1000 * (2 if coupled else 3) + c)
            n = min(chunk, n_paths - c * chunk)
            rec = min(left, n)
            r = self._run_chunk(rng, n, coupled=coupled, record_paths=rec)
            left -= rec
            if r["traj"] is not None and r["traj"].shape[0]:
                traj = r["traj"] if traj is None else np.concatenate([traj, r["traj"]], axis=0)
            for k in ("fired", "fire_q", "fire_count", "x_final", "regime_time", "peak_z"):
                out[k].append(r[k])
            out["coup"].append(r["draws"]["coup_mult"][:, 0, 0])
            if verbose and (c + 1) % 5 == 0:
                print(f"  ...{(c + 1) * chunk:,}/{n_paths:,} paths")

        merged = {k: np.concatenate(v, axis=0) for k, v in out.items()}
        merged["traj"] = traj
        return merged

# GEO-SIM

A coupled Monte Carlo simulator of world futures, run from a fixed epoch of
**2026-07-29** out to **end-2036**.

The output is a set of calibrated probabilities with Monte Carlo error bars,
plus the things a single probability can't tell you: which risks amplify each
other, how many severe shocks a decade is likely to contain, and what
distinguishable worlds the dynamics actually produce.

See **[REPORT.md](REPORT.md)** for the findings.

## What it is

Most "world forecast" exercises are a list of independent guesses. The
interesting structure is in the couplings — a Taiwan contingency is not an
isolated draw, it is correlated with semiconductor supply, equity drawdowns,
inflation, and alliance politics, and those in turn feed back into the hazard of
further events. GEO-SIM models that explicitly.

The world is a state vector of continuous indicators plus a set of discrete
events with state-dependent hazards, marched forward in quarterly steps:

1. **Regimes.** A slow Markov layer scales volatility and crisis hazards
   globally. The same tension index means something different in 1995 than in
   1938, and regimes are how the model says so.
2. **Continuous dynamics.** Mean reversion toward a drifting attractor, lagged
   cross-domain coupling, correlated Student-t innovations (ν=5 — macro and
   conflict series are not Gaussian), and stabilizing feedbacks that engage
   only once a variable is visibly stressed.
3. **Discrete events.** Hazards modulated by indicator z-scores, by the
   prevailing regime, and by what has already fired (contagion).
4. **Feedback.** Events that fire shock the indicators, closing the loop.

## Why the numbers should be taken seriously (and where they shouldn't)

**Parameter uncertainty is sampled per path.** Every path draws its own
hazards, volatilities, drifts and coupling strengths from priors centred on the
analysts' estimates, with widths set by the analysts' own stated confidence. A
run therefore integrates over "we don't know the parameters" as well as "the
world is random." That is the difference between an honest interval and a
decorative one.

**Hazards are calibrated in two passes.** Hazard is exponential in indicator
z-scores, so the average hazard across paths exceeds the hazard at the average
state — Jensen's inequality would silently inflate every probability above what
the analysts actually said. Pass one fits a per-event offset against a decoupled
baseline until marginals reproduce the elicited priors. Pass two turns on
coupling, contagion and regimes, holding those offsets fixed.

The gap between the two passes is the headline diagnostic. It is not noise: it
is the model's estimate of **systemic amplification**, reported per event as an
odds ratio. An event whose isolated probability is 6% but whose coupled
probability is 11% is telling you that most of its risk arrives through other
people's crises.

**What this cannot do.** It cannot know the parameters. Every number downstream
inherits the analysts' judgement, and on questions with thin reference classes —
great-power war, loss-of-control incidents, AMOC collapse — that judgement is
doing most of the work and the Monte Carlo error bars are the *least* important
source of uncertainty. The error bars quantify sampling noise only. Treat the
decoupled-vs-coupled spread and the sensitivity table as the real uncertainty
statement, and read the reference class before believing any single figure.

## Parameter provenance

Parameters were elicited from nine domain analysts, each required to web-ground
its current-state numbers to July 2026 rather than rely on training data, and
each then rewritten by an adversarial calibration auditor checking for:

- arithmetic incoherence between annual hazard and cumulative quotes
- monotonicity violations across horizons
- base-rate neglect and invented reference classes
- recency bias extrapolating 2025–26 headlines into permanent trends
- aggregate over-prediction of discontinuity
- unrealistic volatilities, checked against how the series has actually moved

A tenth agent built the cross-domain transmission matrix, shock correlations,
regime definitions, contagion rules and — importantly — the **stabilizing
feedbacks**. A model without negative feedback produces garbage doom numbers,
because in the real world high prices destroy demand, wars exhaust belligerents,
central banks backstop, and elections remove unpopular governments.

## Running it

```bash
pip install numpy scipy pandas scikit-learn
python run_simulation.py --paths 200000 --out results
```

Roughly 7 minutes for 200k paths on 4 cores. Outputs land in `results/`:

| file | contents |
|---|---|
| `results.json` | event probabilities, calibration diagnostics, regimes, systemic metrics, conditional matrix, scenario clusters, sensitivity |
| `fans.json` | per-indicator percentile bands per quarter |
| `raw.npz` | per-path firing quarters, terminal states, regime occupancy |

Useful flags: `--paths`, `--chunk` (memory/speed tradeoff), `--record` (paths
kept for fan charts), `--horizon`, `--seed`.

## Layout

```
geosim/params.py     parameter compilation, unit conventions, hazard inference
geosim/engine.py     the Monte Carlo core
geosim/analysis.py   probabilities, conditionals, clustering, sensitivity
run_simulation.py    driver
params/              analyst-produced parameter sets (provenance in-file)
results/             run outputs
```

## Conventions worth knowing before editing parameters

- Indicators are in natural units. Anything expressed "in SDs" — driver
  elasticities, event impacts, coupling strengths — refers to the indicator's
  *stationary* SD, derived from its annual innovation volatility and its
  mean-reversion rate, not asserted.
- z-scores are measured against the attractor, not the starting value. An
  indicator that starts far from its long-run level registers as stressed from
  quarter zero; one with persistent drift becomes more stressed over the
  horizon. Both are intended.
- `absorbing: true` means the event cannot recur. That is what makes
  "first nuclear detonation since 1945" behave differently from "recession".

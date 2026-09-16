# predictions-geo

Two forecasting models that share one stance: a forecast you cannot score is not
a forecast. Both fit or elicit explicit parameters, validate against something
checkable, and report calibrated probabilities with their own limits stated.

- **[GEO-SIM](#geo-sim)** — coupled Monte Carlo simulator of world futures,
  2026–2036. See **[REPORT.md](REPORT.md)**.
- **[RL-SIM](#rl-sim)** — fitted booking model for Rolling Loud lineups. See
  **[ROLLING_LOUD_2027.md](ROLLING_LOUD_2027.md)**.

---

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


---

# RL-SIM

A fitted choice model for Rolling Loud lineups, run against **Rolling Loud
Florida 2027** (Camping World Stadium, Orlando, 7–9 May 2027 — dates announced
15 September 2026, lineup not yet announced).

See **[ROLLING_LOUD_2027.md](ROLLING_LOUD_2027.md)** for the forecast.

## What it is

Festival lineups are normally "forecast" by listing plausible names. That is a
ranking, not a forecast, and nothing about it can be scored afterwards. RL-SIM
instead fits an explicit model to the bookings Rolling Loud has actually made.

**Headliners are a choice problem.** From a pool of acts who could close a
night, three get picked. That is a conditional logit (Plackett-Luce), fitted by
penalised maximum likelihood to the 18 headline bookings across the six US
flagship editions staged since 2023.

**The undercard is a persistence problem.** Rolling Loud rebuilds most of each
bill from the previous one plus that season's risers, so the per-artist question
is a probability of appearing at all. That is a logistic regression on
edition-to-edition transitions.

Both the feature set and the regularisation strength are chosen by **held-out
predictive likelihood** — leave-one-edition-out for headliners,
leave-one-transition-out for the undercard — never by which answer looks better.

## Why the numbers should be taken seriously (and where they shouldn't)

**It beats the baselines a sceptic would propose.** Leave-one-edition-out, each
held-out slate predicted by a model refitted on the other five:

| | top-3 hit rate |
|---|---|
| RL-SIM | **66.7%** |
| rank by popularity alone | 22.2% |
| rebook last edition's headliners | 16.7% |
| uniform draw from the pool | 7.0% |

**Model selection found a real effect.** Adding *draw* — the size of room an act
sells on their own name, as distinct from how culturally hot they are —
improved held-out likelihood by ten log points and stopped the model promoting
buzzing club acts to stadium headliners. The same control was needed in the
undercard model for the opposite reason, and fixed two sign-flipped
coefficients there.

**Uncertainty is sampled, not decorated.** Every path draws its own coefficients
from the fit's asymptotic sampling distribution and its own availability gate
per artist, so a run integrates over "we don't know the parameters" as well as
"booking is stochastic."

**What this cannot do.** It is fitted to eighteen headline bookings. The
Monte Carlo error bars are sampling noise and are the least important source of
uncertainty in the output. Worse, popularity ranks for pre-2026 editions were
assigned retrospectively, so the backtest is an *optimistic bound* on genuine
out-of-sample skill. With a pool of fifty acts and eighteen observations there
is no capacity to learn artist-specific effects — "Drake has declined to play
this festival for eleven years" enters only through a hand-assigned
availability term. Read §8 of the report before believing any single figure.

## Running it

```bash
pip install numpy scipy
python predict_rolling_loud.py --paths 200000 --out results_rl
python tests/test_rlsim.py     # 20 validation checks
```

## Layout

```
rlsim/data.py                      parameter loading, feature construction, timing conventions
rlsim/model.py                     both fitted models, model selection, backtest
rlsim/simulate.py                  forward Monte Carlo
predict_rolling_loud.py            driver
params/rolling_loud_editions.json  edition history, provenance in-file
params/rolling_loud_artists.json   artist features, per-artist reasoning in-file
tests/test_rlsim.py                validation suite
```

## Conventions worth knowing before editing parameters

- **Features are measured at booking time**, roughly five months before doors,
  not on the day of the show. Using show-day popularity would leak the future
  into the fit and make the backtest meaningless.
- **`fest_avail` is a stable trait** (does this kind of act take third-party
  festival bookings) and **`avail_2027` is a year-specific constraint**
  (schedule, legal status, stated intent). They must stay disjoint. Writing one
  risk into both multiplies it — an earlier version did exactly that and buried
  NBA YoungBoy at 2% despite his having been signed to close the previous
  edition.
- **`draw` is not `heat`.** Draw is the room you sell on your own name; heat is
  how much the culture is talking about you. Conflating them is the single
  biggest modelling error available here.
- Undercard rosters are reconstructed from trade press, which prints roughly the
  top 25–30 of a 78-act bill, so measured return rates are lower bounds and
  undercard probabilities are scoped to artists whose booking would be reported.

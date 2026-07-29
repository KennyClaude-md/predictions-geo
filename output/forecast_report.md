# World Futures Simulation — Forecast Report

**Simulation date:** 2026-07-29  
**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  
**Paths:** 4,800 across 5 worldviews × 40 parameter worlds  
**Risk nodes:** 108 · **causal edges:** 70 · **latent factors:** 4 · **continuous variables:** 45

---

## How to read this

Every number below is the output of a survival-process Monte Carlo, not a guess written directly. Nine domains were parameterised against current sources, audited for base-rate discipline, then red-teamed from three directions. Each of those opinions is run as a separate worldview and the results are pooled by weight.

**The bracketed range is not the range of outcomes** — the event either happens or it doesn't. It is the range of *the probability itself* across parameter worlds: how much the answer moves depending on whose model of the world you accept. A wide bracket means the forecast is fragile. Monte Carlo noise has been subtracted out, so what remains is real disagreement.

**Calibration check:** simulated marginals reproduce the elicited cumulative probabilities to within 3.63 percentage points (worst node, worst worldview). This matters: the dependency network is tuned to reshape the *joint* distribution — which events co-occur — without inflating any individual probability above what the underlying analysis actually claimed.

## Headline forecasts

Ranked by expected systemic impact — probability by 2036 multiplied by severity — rather than by probability alone, because a 12% chance of something that reorders the world outranks a near-certainty that doesn't.

| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Sev |
|---|-------|--------:|--------:|--------:|:---------------:|----:|
| 1 | **Synthetic energy event 5** | 26% | 81% | 99% | [95%–>99%] | 8 |
| 2 | **Synthetic geopolitics event 6** | 21% | 63% | 97% | [91%–>99%] | 8 |
| 3 | **Synthetic geopolitics event 9** | 24% | 69% | 90% | [79%–>99%] | 8 |
| 4 | **Synthetic health event 9** | 28% | 58% | 92% | [75%–>99%] | 7 |
| 5 | **Synthetic health event 10** | 19% | 51% | 85% | [56%–>99%] | 8 |
| 6 | **Synthetic climate event 7** | 25% | 55% | 90% | [67%–>99%] | 7 |
| 7 | **Synthetic ai event 2** | 20% | 82% | 99% | [95%–>99%] | 6 |
| 8 | **Synthetic energy event 11** | 22% | 59% | 98% | [88%–>99%] | 6 |
| 9 | **Synthetic demographics event 3** | 26% | 79% | 99% | [97%–>99%] | 6 |
| 10 | **Synthetic foodwater event 7** | 19% | 60% | 78% | [46%–>99%] | 8 |
| 11 | **Synthetic health event 11** | 24% | 69% | 98% | [91%–>99%] | 6 |
| 12 | **Synthetic foodwater event 9** | 25% | 52% | 81% | [56%–>99%] | 7 |
| 13 | **Synthetic economy event 1** | 16% | 55% | 69% | [28%–>99%] | 8 |
| 14 | **Synthetic energy event 7** | 19% | 54% | 87% | [62%–>99%] | 6 |
| 15 | **Synthetic energy event 1** | 18% | 52% | 66% | [45%–86%] | 8 |
| 16 | **Synthetic health event 3** | 25% | 51% | 70% | [34%–>99%] | 7 |
| 17 | **Synthetic demographics event 8** | 20% | 57% | 81% | [54%–>99%] | 6 |
| 18 | **Synthetic economy event 5** | 22% | 36% | 56% | [5.9%–>99%] | 9 |
| 19 | **Synthetic demographics event 9** | 28% | 53% | 64% | [21%–>99%] | 8 |
| 20 | **Synthetic ai event 11** | 24% | 79% | 86% | [55%–>99%] | 6 |
| 21 | **Synthetic demographics event 1** | 20% | 62% | 76% | [47%–>99%] | 6 |
| 22 | **Synthetic foodwater event 8** | 28% | 58% | 84% | [53%–>99%] | 5 |

## The decade in aggregate

Individual probabilities are the easy part. The question that actually determines whether the 2030s feel survivable is how many serious shocks land, and whether they land together.

| Statistic (through 2036) | Value |
|---|---|
| Expected number of severity ≥ 6 events | **27.9** |
| Severe-event count, 10th–90th percentile | 24 – 32 (median 28) |
| P(no severity ≥ 6 event at all) | <0.5% |
| P(3 or more severe events) | >99% |
| P(5 or more severe events) | >99% |
| P(at least one severity ≥ 8 event) | **>99%** |
| P(two or more severity ≥ 8 events) | >99% |

The modal decade contains 28 events the model rates severity 6 or above, and the probability of getting through to 2036 with none is 0%. That asymmetry is the single most robust finding here: across every worldview and every parameter draw, a decade with no major disruption is a tail outcome, not the base case. The interesting variance is not *whether* shocks arrive but whether they arrive spaced out or together.

## Scenario archetypes

Paths were clustered on which major events fired and on the shape of the systemic-stress trajectory. These are not scenarios written in advance and then assigned probabilities — they are the shapes the simulation actually produced, priced by how much of the path mass fell into each.

### Quiet decade — great-power conflict and health emergency — **46%**

Trend continuation. The scheduled stresses arrive on schedule and are absorbed; nothing in this cluster forces a structural break. The distinguishing driver is great-power conflict compounded by health emergency. Mean count of tracked major events: 20.4.

Distinguishing features (rate within this cluster vs. overall):

- **Synthetic geopolitics event 9** — 100% here vs 90% overall
- **Synthetic health event 9** — 100% here vs 92% overall

### Compound crisis decade — health emergency and energy disruption — **36%**

Correlated systemic failure. Multiple high-severity events fire in a narrow window and reinforce each other; this is the cluster where the coupling structure dominates the marginals. The distinguishing driver is health emergency compounded by energy disruption. Mean count of tracked major events: 21.9.

Distinguishing features (rate within this cluster vs. overall):

- **Synthetic geopolitics event 9** — 100% here vs 90% overall
- **Synthetic health event 9** — 100% here vs 92% overall
- **Synthetic energy event 1** — 73% here vs 66% overall
- **Synthetic health event 3** — 77% here vs 70% overall
- **Synthetic demographics event 9** — 72% here vs 64% overall
- **Synthetic energy event 2** — 65% here vs 58% overall

### Turbulent decade — health emergency and financial and macro stress — **9.4%**

Overlapping crises with intact institutions. Response capacity is strained but not exhausted, and recovery between shocks is incomplete. The distinguishing driver is health emergency compounded by financial and macro stress. Mean count of tracked major events: 20.1.

Distinguishing features (rate within this cluster vs. overall):

- **Synthetic health event 9** — 100% here vs 92% overall
- **Synthetic economy event 1** — 75% here vs 69% overall
- Synthetic geopolitics event 9 — *suppressed*: 0% here vs 90% overall

### Severe decade — no dominant driver — **8.0%**

Concurrent failure across domains. Shocks arrive faster than systems absorb them, and the response to one degrades the capacity to answer the next. Mean count of tracked major events: 19.8.

Distinguishing features (rate within this cluster vs. overall):

- Synthetic health event 9 — *suppressed*: 0% here vs 92% overall

### Manageable decade — energy disruption and financial and macro stress — **0.9%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is energy disruption compounded by financial and macro stress. Mean count of tracked major events: 19.2.

Distinguishing features (rate within this cluster vs. overall):

- **Synthetic energy event 1** — 76% here vs 66% overall
- **Synthetic economy event 5** — 66% here vs 56% overall
- **Synthetic demographics event 8** — 88% here vs 81% overall
- **Synthetic ai event 11** — 93% here vs 86% overall
- Synthetic energy event 5 — *suppressed*: 0% here vs 99% overall
- Synthetic climate event 5 — *suppressed*: 46% here vs 64% overall
- Synthetic foodwater event 9 — *suppressed*: 66% here vs 81% overall

## Full results by domain

### Energy systems & critical materials

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic energy event 5 | 26% | 81% | 99% | [95%–>99%] | 8 | 2028Q4 |
| Synthetic energy event 11 | 22% | 59% | 98% | [88%–>99%] | 6 | 2030Q2 |
| Synthetic energy event 7 | 19% | 54% | 87% | [62%–>99%] | 6 | 2030Q2 |
| Synthetic energy event 1 | 18% | 52% | 66% | [45%–86%] | 8 | 2029Q2 |
| Synthetic energy event 2 | 26% | 39% | 58% | [30%–86%] | 7 | 2028Q4 |
| Synthetic energy event 8 | 26% | 67% | 89% | [71%–>99%] | 4 | 2029Q2 |
| Synthetic energy event 0 | 23% | 46% | 86% | [62%–>99%] | 2 | 2031Q2 |
| Synthetic energy event 10 | 23% | 49% | 82% | [46%–>99%] | 2 | 2030Q1 |
| Synthetic energy event 3 | 12% | 32% | 45% | [22%–68%] | 4 | 2029Q4 |
| Synthetic energy event 4 | 11% | 26% | 38% | [<0.5%–80%] | 4 | 2030Q2 |
| Synthetic energy event 6 | 4.6% | 11% | 17% | [8.7%–26%] | 7 | 2030Q3 |
| Synthetic energy event 9 | 6.2% | 6.7% | 11% | [<0.5%–46%] | 8 | 2027Q4 |

<details><summary>Resolution criteria</summary>

- **Synthetic energy event 5** — placeholder criterion for pipeline testing
- **Synthetic energy event 11** — placeholder criterion for pipeline testing
- **Synthetic energy event 7** — placeholder criterion for pipeline testing
- **Synthetic energy event 1** — placeholder criterion for pipeline testing
- **Synthetic energy event 2** — placeholder criterion for pipeline testing
- **Synthetic energy event 8** — placeholder criterion for pipeline testing
- **Synthetic energy event 0** — placeholder criterion for pipeline testing
- **Synthetic energy event 10** — placeholder criterion for pipeline testing
- **Synthetic energy event 3** — placeholder criterion for pipeline testing
- **Synthetic energy event 4** — placeholder criterion for pipeline testing
- **Synthetic energy event 6** — placeholder criterion for pipeline testing
- **Synthetic energy event 9** — placeholder criterion for pipeline testing

</details>

### Great-power conflict & geopolitics

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic geopolitics event 6 | 21% | 63% | 97% | [91%–>99%] | 8 | 2030Q1 |
| Synthetic geopolitics event 9 | 24% | 69% | 90% | [79%–>99%] | 8 | 2029Q2 |
| Synthetic geopolitics event 1 | 17% | 43% | 71% | [55%–87%] | 5 | 2030Q3 |
| Synthetic geopolitics event 10 | 14% | 31% | 44% | [19%–68%] | 8 | 2029Q3 |
| Synthetic geopolitics event 11 | 27% | 40% | 49% | [31%–67%] | 6 | 2027Q4 |
| Synthetic geopolitics event 2 | 6.7% | 23% | 31% | [9.9%–52%] | 8 | 2030Q1 |
| Synthetic geopolitics event 7 | 19% | 50% | 82% | [51%–>99%] | 3 | 2030Q3 |
| Synthetic geopolitics event 0 | 10% | 17% | 28% | [7.1%–49%] | 6 | 2030Q2 |
| Synthetic geopolitics event 3 | 12% | 34% | 40% | [23%–58%] | 3 | 2029Q2 |
| Synthetic geopolitics event 4 | 12% | 17% | 27% | [16%–38%] | 3 | 2029Q1 |
| Synthetic geopolitics event 8 | 4.7% | 7.3% | 8.8% | [<0.5%–22%] | 9 | 2027Q4 |
| Synthetic geopolitics event 5 | 0.9% | 3.9% | 6.5% | [2.4%–11%] | 4 | 2031Q2 |

<details><summary>Resolution criteria</summary>

- **Synthetic geopolitics event 6** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 9** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 1** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 10** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 11** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 2** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 7** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 0** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 3** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 4** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 8** — placeholder criterion for pipeline testing
- **Synthetic geopolitics event 5** — placeholder criterion for pipeline testing

</details>

### Pandemics, biosecurity & global health

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic health event 9 | 28% | 58% | 92% | [75%–>99%] | 7 | 2030Q1 |
| Synthetic health event 10 | 19% | 51% | 85% | [56%–>99%] | 8 | 2030Q1 |
| Synthetic health event 11 | 24% | 69% | 98% | [91%–>99%] | 6 | 2029Q2 |
| Synthetic health event 3 | 25% | 51% | 70% | [34%–>99%] | 7 | 2029Q1 |
| Synthetic health event 2 | 18% | 48% | 52% | [9.6%–95%] | 8 | 2028Q4 |
| Synthetic health event 6 | 22% | 28% | 40% | [1.7%–79%] | 7 | 2027Q4 |
| Synthetic health event 1 | 26% | 49% | 56% | [12%–>99%] | 4 | 2028Q1 |
| Synthetic health event 5 | 14% | 39% | 41% | [9.4%–73%] | 4 | 2028Q4 |
| Synthetic health event 8 | 14% | 30% | 41% | [25%–57%] | 4 | 2029Q2 |
| Synthetic health event 0 | 7.8% | 11% | 20% | [<0.5%–49%] | 7 | 2031Q2 |
| Synthetic health event 7 | 13% | 28% | 31% | [16%–46%] | 4 | 2028Q4 |
| Synthetic health event 4 | 3.8% | 7.4% | 12% | [<0.5%–24%] | 2 | 2030Q1 |

<details><summary>Resolution criteria</summary>

- **Synthetic health event 9** — placeholder criterion for pipeline testing
- **Synthetic health event 10** — placeholder criterion for pipeline testing
- **Synthetic health event 11** — placeholder criterion for pipeline testing
- **Synthetic health event 3** — placeholder criterion for pipeline testing
- **Synthetic health event 2** — placeholder criterion for pipeline testing
- **Synthetic health event 6** — placeholder criterion for pipeline testing
- **Synthetic health event 1** — placeholder criterion for pipeline testing
- **Synthetic health event 5** — placeholder criterion for pipeline testing
- **Synthetic health event 8** — placeholder criterion for pipeline testing
- **Synthetic health event 0** — placeholder criterion for pipeline testing
- **Synthetic health event 7** — placeholder criterion for pipeline testing
- **Synthetic health event 4** — placeholder criterion for pipeline testing

</details>

### Climate & Earth systems

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic climate event 7 | 25% | 55% | 90% | [67%–>99%] | 7 | 2030Q1 |
| Synthetic climate event 5 | 25% | 52% | 65% | [34%–95%] | 7 | 2028Q4 |
| Synthetic climate event 8 | 18% | 59% | 81% | [63%–99%] | 5 | 2029Q4 |
| Synthetic climate event 9 | 16% | 58% | 77% | [30%–>99%] | 4 | 2029Q3 |
| Synthetic climate event 6 | 9.1% | 31% | 52% | [23%–82%] | 5 | 2031Q1 |
| Synthetic climate event 3 | 21% | 52% | 61% | [16%–>99%] | 4 | 2028Q4 |
| Synthetic climate event 11 | 11% | 27% | 31% | [7.7%–54%] | 6 | 2028Q4 |
| Synthetic climate event 1 | 14% | 21% | 25% | [<0.5%–56%] | 7 | 2027Q4 |
| Synthetic climate event 10 | 16% | 22% | 30% | [<0.5%–64%] | 6 | 2027Q4 |
| Synthetic climate event 4 | 17% | 24% | 32% | [<0.5%–73%] | 2 | 2027Q4 |
| Synthetic climate event 0 | 2.9% | 5.7% | 14% | [<0.5%–34%] | 3 | 2032Q4 |
| Synthetic climate event 2 | 1.5% | 3.5% | 4.0% | [1.6%–6.4%] | 7 | 2029Q1 |

<details><summary>Resolution criteria</summary>

- **Synthetic climate event 7** — placeholder criterion for pipeline testing
- **Synthetic climate event 5** — placeholder criterion for pipeline testing
- **Synthetic climate event 8** — placeholder criterion for pipeline testing
- **Synthetic climate event 9** — placeholder criterion for pipeline testing
- **Synthetic climate event 6** — placeholder criterion for pipeline testing
- **Synthetic climate event 3** — placeholder criterion for pipeline testing
- **Synthetic climate event 11** — placeholder criterion for pipeline testing
- **Synthetic climate event 1** — placeholder criterion for pipeline testing
- **Synthetic climate event 10** — placeholder criterion for pipeline testing
- **Synthetic climate event 4** — placeholder criterion for pipeline testing
- **Synthetic climate event 0** — placeholder criterion for pipeline testing
- **Synthetic climate event 2** — placeholder criterion for pipeline testing

</details>

### AI, compute & transformative technology

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic ai event 2 | 20% | 82% | 99% | [95%–>99%] | 6 | 2028Q4 |
| Synthetic ai event 11 | 24% | 79% | 86% | [55%–>99%] | 6 | 2028Q3 |
| Synthetic ai event 8 | 13% | 35% | 47% | [7.6%–86%] | 7 | 2029Q3 |
| Synthetic ai event 4 | 12% | 30% | 53% | [19%–87%] | 6 | 2031Q1 |
| Synthetic ai event 0 | 18% | 21% | 31% | [<0.5%–64%] | 6 | 2027Q3 |
| Synthetic ai event 5 | 4.9% | 16% | 23% | [<0.5%–58%] | 8 | 2030Q2 |
| Synthetic ai event 10 | 25% | 70% | 76% | [47%–>99%] | 2 | 2028Q4 |
| Synthetic ai event 6 | 9.7% | 17% | 23% | [<0.5%–59%] | 8 | 2028Q4 |
| Synthetic ai event 9 | 7.1% | 18% | 23% | [<0.5%–51%] | 5 | 2029Q3 |
| Synthetic ai event 3 | 13% | 22% | 32% | [2.5%–62%] | 4 | 2029Q4 |
| Synthetic ai event 7 | 13% | 19% | 33% | [<0.5%–75%] | 3 | 2030Q1 |
| Synthetic ai event 1 | 3.9% | 7.1% | 7.8% | [3.2%–12%] | 8 | 2028Q1 |

<details><summary>Resolution criteria</summary>

- **Synthetic ai event 2** — placeholder criterion for pipeline testing
- **Synthetic ai event 11** — placeholder criterion for pipeline testing
- **Synthetic ai event 8** — placeholder criterion for pipeline testing
- **Synthetic ai event 4** — placeholder criterion for pipeline testing
- **Synthetic ai event 0** — placeholder criterion for pipeline testing
- **Synthetic ai event 5** — placeholder criterion for pipeline testing
- **Synthetic ai event 10** — placeholder criterion for pipeline testing
- **Synthetic ai event 6** — placeholder criterion for pipeline testing
- **Synthetic ai event 9** — placeholder criterion for pipeline testing
- **Synthetic ai event 3** — placeholder criterion for pipeline testing
- **Synthetic ai event 7** — placeholder criterion for pipeline testing
- **Synthetic ai event 1** — placeholder criterion for pipeline testing

</details>

### Demography & migration

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic demographics event 3 | 26% | 79% | 99% | [97%–>99%] | 6 | 2029Q1 |
| Synthetic demographics event 8 | 20% | 57% | 81% | [54%–>99%] | 6 | 2029Q4 |
| Synthetic demographics event 9 | 28% | 53% | 64% | [21%–>99%] | 8 | 2028Q3 |
| Synthetic demographics event 1 | 20% | 62% | 76% | [47%–>99%] | 6 | 2029Q2 |
| Synthetic demographics event 4 | 21% | 48% | 65% | [28%–>99%] | 6 | 2029Q2 |
| Synthetic demographics event 6 | 17% | 49% | 56% | [15%–97%] | 7 | 2028Q4 |
| Synthetic demographics event 7 | 20% | 37% | 44% | [17%–71%] | 7 | 2028Q2 |
| Synthetic demographics event 2 | 16% | 54% | 68% | [38%–98%] | 4 | 2029Q4 |
| Synthetic demographics event 0 | 25% | 34% | 54% | [33%–76%] | 4 | 2029Q1 |
| Synthetic demographics event 11 | 13% | 33% | 52% | [34%–70%] | 3 | 2030Q3 |
| Synthetic demographics event 5 | 5.1% | 12% | 17% | [2.6%–31%] | 7 | 2029Q3 |
| Synthetic demographics event 10 | 6.4% | 12% | 15% | [<0.5%–36%] | 7 | 2028Q4 |

<details><summary>Resolution criteria</summary>

- **Synthetic demographics event 3** — placeholder criterion for pipeline testing
- **Synthetic demographics event 8** — placeholder criterion for pipeline testing
- **Synthetic demographics event 9** — placeholder criterion for pipeline testing
- **Synthetic demographics event 1** — placeholder criterion for pipeline testing
- **Synthetic demographics event 4** — placeholder criterion for pipeline testing
- **Synthetic demographics event 6** — placeholder criterion for pipeline testing
- **Synthetic demographics event 7** — placeholder criterion for pipeline testing
- **Synthetic demographics event 2** — placeholder criterion for pipeline testing
- **Synthetic demographics event 0** — placeholder criterion for pipeline testing
- **Synthetic demographics event 11** — placeholder criterion for pipeline testing
- **Synthetic demographics event 5** — placeholder criterion for pipeline testing
- **Synthetic demographics event 10** — placeholder criterion for pipeline testing

</details>

### Food, water & agriculture

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic foodwater event 7 | 19% | 60% | 78% | [46%–>99%] | 8 | 2029Q2 |
| Synthetic foodwater event 9 | 25% | 52% | 81% | [56%–>99%] | 7 | 2030Q1 |
| Synthetic foodwater event 8 | 28% | 58% | 84% | [53%–>99%] | 5 | 2029Q2 |
| Synthetic foodwater event 0 | 19% | 36% | 53% | [36%–69%] | 7 | 2029Q4 |
| Synthetic foodwater event 6 | 22% | 36% | 55% | [17%–93%] | 6 | 2029Q3 |
| Synthetic foodwater event 10 | 17% | 42% | 58% | [38%–78%] | 5 | 2029Q4 |
| Synthetic foodwater event 2 | 7.4% | 21% | 33% | [1.9%–65%] | 9 | 2030Q4 |
| Synthetic foodwater event 3 | 17% | 57% | 91% | [71%–>99%] | 3 | 2030Q2 |
| Synthetic foodwater event 11 | 17% | 24% | 32% | [11%–53%] | 7 | 2027Q4 |
| Synthetic foodwater event 4 | 15% | 25% | 34% | [<0.5%–69%] | 4 | 2028Q4 |
| Synthetic foodwater event 5 | 15% | 21% | 27% | [6.8%–47%] | 4 | 2027Q4 |
| Synthetic foodwater event 1 | 7.7% | 12% | 18% | [6.2%–31%] | 3 | 2029Q1 |

<details><summary>Resolution criteria</summary>

- **Synthetic foodwater event 7** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 9** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 8** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 0** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 6** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 10** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 2** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 3** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 11** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 4** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 5** — placeholder criterion for pipeline testing
- **Synthetic foodwater event 1** — placeholder criterion for pipeline testing

</details>

### Global macroeconomy & finance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic economy event 1 | 16% | 55% | 69% | [28%–>99%] | 8 | 2029Q2 |
| Synthetic economy event 5 | 22% | 36% | 56% | [5.9%–>99%] | 9 | 2029Q2 |
| Synthetic economy event 11 | 26% | 45% | 48% | [30%–66%] | 9 | 2027Q4 |
| Synthetic economy event 2 | 23% | 34% | 47% | [16%–79%] | 7 | 2028Q1 |
| Synthetic economy event 6 | 10% | 24% | 41% | [<0.5%–82%] | 5 | 2030Q4 |
| Synthetic economy event 3 | 16% | 40% | 49% | [33%–66%] | 4 | 2029Q2 |
| Synthetic economy event 7 | 21% | 30% | 50% | [18%–83%] | 4 | 2030Q1 |
| Synthetic economy event 10 | 9.3% | 27% | 34% | [<0.5%–76%] | 6 | 2029Q2 |
| Synthetic economy event 0 | 13% | 24% | 45% | [16%–73%] | 4 | 2031Q3 |
| Synthetic economy event 4 | 17% | 39% | 44% | [18%–70%] | 4 | 2028Q4 |
| Synthetic economy event 9 | 10% | 17% | 22% | [4.5%–40%] | 8 | 2028Q3 |
| Synthetic economy event 8 | 6.0% | 12% | 19% | [8.4%–29%] | 6 | 2030Q2 |

<details><summary>Resolution criteria</summary>

- **Synthetic economy event 1** — placeholder criterion for pipeline testing
- **Synthetic economy event 5** — placeholder criterion for pipeline testing
- **Synthetic economy event 11** — placeholder criterion for pipeline testing
- **Synthetic economy event 2** — placeholder criterion for pipeline testing
- **Synthetic economy event 6** — placeholder criterion for pipeline testing
- **Synthetic economy event 3** — placeholder criterion for pipeline testing
- **Synthetic economy event 7** — placeholder criterion for pipeline testing
- **Synthetic economy event 10** — placeholder criterion for pipeline testing
- **Synthetic economy event 0** — placeholder criterion for pipeline testing
- **Synthetic economy event 4** — placeholder criterion for pipeline testing
- **Synthetic economy event 9** — placeholder criterion for pipeline testing
- **Synthetic economy event 8** — placeholder criterion for pipeline testing

</details>

### Political stability & governance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Synthetic politics event 0 | 30% | 48% | 70% | [45%–96%] | 6 | 2029Q1 |
| Synthetic politics event 1 | 20% | 49% | 65% | [22%–>99%] | 4 | 2029Q2 |
| Synthetic politics event 5 | 9.0% | 24% | 33% | [5.1%–61%] | 8 | 2029Q4 |
| Synthetic politics event 9 | 22% | 61% | 87% | [52%–>99%] | 3 | 2029Q3 |
| Synthetic politics event 6 | 13% | 40% | 43% | [5.7%–80%] | 6 | 2028Q4 |
| Synthetic politics event 10 | 24% | 59% | 68% | [42%–94%] | 3 | 2028Q4 |
| Synthetic politics event 11 | 11% | 20% | 33% | [4.5%–61%] | 5 | 2030Q2 |
| Synthetic politics event 8 | 3.9% | 11% | 16% | [<0.5%–33%] | 7 | 2030Q1 |
| Synthetic politics event 7 | 4.1% | 11% | 16% | [5.4%–27%] | 6 | 2030Q1 |
| Synthetic politics event 3 | 6.5% | 14% | 19% | [<0.5%–46%] | 5 | 2029Q4 |
| Synthetic politics event 2 | 14% | 26% | 31% | [20%–42%] | 2 | 2028Q3 |
| Synthetic politics event 4 | 8.2% | 17% | 30% | [16%–43%] | 2 | 2031Q1 |

<details><summary>Resolution criteria</summary>

- **Synthetic politics event 0** — placeholder criterion for pipeline testing
- **Synthetic politics event 1** — placeholder criterion for pipeline testing
- **Synthetic politics event 5** — placeholder criterion for pipeline testing
- **Synthetic politics event 9** — placeholder criterion for pipeline testing
- **Synthetic politics event 6** — placeholder criterion for pipeline testing
- **Synthetic politics event 10** — placeholder criterion for pipeline testing
- **Synthetic politics event 11** — placeholder criterion for pipeline testing
- **Synthetic politics event 8** — placeholder criterion for pipeline testing
- **Synthetic politics event 7** — placeholder criterion for pipeline testing
- **Synthetic politics event 3** — placeholder criterion for pipeline testing
- **Synthetic politics event 2** — placeholder criterion for pipeline testing
- **Synthetic politics event 4** — placeholder criterion for pipeline testing

</details>

## How bad decades begin

Among paths where at least three high-severity events fired, these are the most common opening sequences, in order of occurrence.

| Frequency | First | Then | Then |
|---:|---|---|---|
| <0.5% | Synthetic climate event 7 | Synthetic demographics event 6 | Synthetic demographics event 9 |
| <0.5% | Synthetic demographics event 6 | Synthetic demographics event 9 | Synthetic economy event 1 |
| <0.5% | Synthetic ai event 0 | Synthetic climate event 7 | Synthetic energy event 2 |
| <0.5% | Synthetic ai event 6 | Synthetic demographics event 3 | Synthetic climate event 5 |
| <0.5% | Synthetic ai event 0 | Synthetic demographics event 4 | Synthetic demographics event 9 |
| <0.5% | Synthetic demographics event 3 | Synthetic demographics event 9 | Synthetic economy event 1 |
| <0.5% | Synthetic climate event 10 | Synthetic economy event 1 | Synthetic foodwater event 11 |
| <0.5% | Synthetic demographics event 9 | Synthetic energy event 2 | Synthetic energy event 5 |
| <0.5% | Synthetic climate event 5 | Synthetic demographics event 3 | Synthetic demographics event 6 |
| <0.5% | Synthetic climate event 5 | Synthetic climate event 7 | Synthetic economy event 2 |
| <0.5% | Synthetic climate event 5 | Synthetic climate event 7 | Synthetic demographics event 1 |
| <0.5% | Synthetic climate event 1 | Synthetic demographics event 3 | Synthetic energy event 5 |

The most common opening — Synthetic climate event 7 → Synthetic demographics event 6 → Synthetic demographics event 9 — accounts for 0.1% of all paths. No single sequence dominates, which is itself informative: the model does not support a story in which one specific trigger reliably starts the cascade. What recurs is the *pattern* — a shock in one domain degrading the capacity to absorb the next.

## Where the correlations are

Pairs whose joint occurrence most exceeds what independence would predict. *Lift* is P(both) ÷ P(A)·P(B): a lift of 3 means these two show up together three times more often than chance. This is the part of the model that a spreadsheet of independent probabilities cannot produce, and it is where tail risk actually lives.

| Event A | Event B | P(both) | Lift | P(A given B) |
|---|---|---:|---:|---:|
| Synthetic economy event 1 | Synthetic foodwater event 0 | 41% | 1.1× | 78% |
| Synthetic economy event 5 | Synthetic ai event 8 | 28% | 1.1× | 60% |
| Synthetic economy event 5 | Synthetic demographics event 4 | 39% | 1.1× | 59% |
| Synthetic economy event 5 | Synthetic demographics event 6 | 33% | 1.0× | 59% |
| Synthetic energy event 2 | Synthetic foodwater event 0 | 32% | 1.0× | 60% |
| Synthetic economy event 1 | Synthetic ai event 11 | 62% | 1.0× | 72% |
| Synthetic health event 3 | Synthetic geopolitics event 10 | 32% | 1.0× | 72% |
| Synthetic health event 2 | Synthetic geopolitics event 1 | 38% | 1.0× | 54% |
| Synthetic demographics event 9 | Synthetic foodwater event 0 | 35% | 1.0× | 66% |
| Synthetic ai event 11 | Synthetic climate event 5 | 57% | 1.0× | 89% |
| Synthetic energy event 7 | Synthetic foodwater event 0 | 47% | 1.0× | 90% |
| Synthetic health event 10 | Synthetic ai event 8 | 41% | 1.0× | 87% |
| Synthetic demographics event 8 | Synthetic ai event 8 | 39% | 1.0× | 83% |
| Synthetic foodwater event 7 | Synthetic foodwater event 0 | 42% | 1.0× | 80% |
| Synthetic climate event 7 | Synthetic foodwater event 0 | 48% | 1.0× | 91% |
| Synthetic health event 3 | Synthetic energy event 2 | 41% | 1.0× | 71% |
| Synthetic foodwater event 9 | Synthetic health event 2 | 43% | 1.0× | 82% |
| Synthetic foodwater event 7 | Synthetic energy event 1 | 52% | 1.0× | 80% |

## Continuous indicators

These evolve on a Gaussian copula driven by each path's own systemic-stress index, so the bad tails of these distributions are populated by the same paths that fired the bad events — not by independent noise.

| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |
|---|---:|:---:|:---:|
| Synthetic geopolitics indicator 0 (units) | 17.15 | 15.7 / **20.9** / 29.3 | 15.9 / **23.2** / 35 |
| Synthetic geopolitics indicator 1 (units) | 96.5 | 90.6 / **121** / 170 | 92.6 / **136** / 201 |
| Synthetic geopolitics indicator 2 (units) | 57.34 | 50 / **66.7** / 93.2 | 48.3 / **71.2** / 108 |
| Synthetic geopolitics indicator 3 (units) | 21.9 | 19.9 / **26.7** / 37 | 20 / **29.3** / 43.5 |
| Synthetic geopolitics indicator 4 (units) | 57.78 | 41 / **54.3** / 76 | 34.2 / **53.2** / 83 |
| Synthetic climate indicator 0 (units) | 47.16 | 40.8 / **54.2** / 75.5 | 39.2 / **57.2** / 86.5 |
| Synthetic climate indicator 1 (units) | 35.91 | 31 / **41.8** / 57.9 | 30.2 / **44.3** / 67.1 |
| Synthetic climate indicator 2 (units) | 74.06 | 44.5 / **60.3** / 84.6 | 32.2 / **52.3** / 85.5 |
| Synthetic climate indicator 3 (units) | 6.997 | 5.95 / **7.98** / 11.2 | 5.77 / **8.52** / 13 |
| Synthetic climate indicator 4 (units) | 96.37 | 67.3 / **90.1** / 126 | 54.1 / **84.9** / 134 |
| Synthetic economy indicator 0 (units) | 98.7 | 75.5 / **101** / 142 | 67.7 / **101** / 156 |
| Synthetic economy indicator 1 (units) | 95.07 | 90.3 / **120** / 168 | 92.1 / **133** / 199 |
| Synthetic economy indicator 2 (units) | 22.99 | 20.3 / **26.9** / 37.8 | 19.9 / **29.2** / 43.9 |
| Synthetic economy indicator 3 (units) | 83.83 | 71 / **94.9** / 133 | 69 / **101** / 154 |
| Synthetic economy indicator 4 (units) | 52.38 | 37.1 / **49.2** / 69.1 | 31.1 / **47.9** / 74.9 |
| Synthetic ai indicator 0 (units) | 16.55 | 10.5 / **13.8** / 19.3 | 7.7 / **12.3** / 20.2 |
| Synthetic ai indicator 1 (units) | 39.19 | 29.2 / **39.1** / 54.6 | 25.5 / **38.9** / 60.8 |
| Synthetic ai indicator 2 (units) | 31.11 | 21.6 / **29** / 40.7 | 17.8 / **27.8** / 43.7 |
| Synthetic ai indicator 3 (units) | 98.81 | 74.5 / **99.5** / 140 | 67.2 / **101** / 156 |
| Synthetic ai indicator 4 (units) | 13.63 | 8.16 / **10.9** / 15.3 | 5.63 / **9.5** / 15.7 |
| Synthetic energy indicator 0 (units) | 4.591 | 4.12 / **5.44** / 7.59 | 3.98 / **5.83** / 8.88 |
| Synthetic energy indicator 1 (units) | 51.62 | 45 / **59.9** / 83.7 | 43.7 / **64.5** / 97.2 |
| Synthetic energy indicator 2 (units) | 11.57 | 10.2 / **13.6** / 19.2 | 10 / **14.7** / 22.2 |
| Synthetic energy indicator 3 (units) | 93.52 | 57.3 / **77.1** / 107 | 41.9 / **68.2** / 110 |
| Synthetic energy indicator 4 (units) | 33.1 | 26.9 / **35.8** / 50.2 | 24.7 / **37.2** / 56.9 |
| Synthetic demographics indicator 0 (units) | 83.63 | 75.9 / **101** / 140 | 76 / **111** / 168 |
| Synthetic demographics indicator 1 (units) | 56.16 | 44.4 / **58.9** / 81.6 | 39.9 / **59.5** / 92.2 |
| Synthetic demographics indicator 2 (units) | 72.35 | 66.7 / **89.3** / 125 | 68.6 / **98.6** / 146 |
| Synthetic demographics indicator 3 (units) | 40.63 | 35.3 / **47.3** / 66.2 | 35 / **50.8** / 76.8 |
| Synthetic demographics indicator 4 (units) | 96.07 | 73.4 / **99.1** / 138 | 66.5 / **102** / 156 |
| Synthetic health indicator 0 (units) | 67.02 | 53.5 / **70.4** / 98.7 | 47.8 / **72.5** / 113 |
| Synthetic health indicator 1 (units) | 6.893 | 4.86 / **6.51** / 9.12 | 4.06 / **6.28** / 9.79 |
| Synthetic health indicator 2 (units) | 73.06 | 63.4 / **85.5** / 119 | 62.4 / **92** / 139 |
| Synthetic health indicator 3 (units) | 64.94 | 56.5 / **75.4** / 105 | 54.6 / **81.9** / 123 |
| Synthetic health indicator 4 (units) | 15.8 | 11.6 / **15.4** / 21.8 | 10 / **15.4** / 24 |
| Synthetic politics indicator 0 (units) | 94.98 | 71.1 / **94.1** / 133 | 61.9 / **94.1** / 146 |
| Synthetic politics indicator 1 (units) | 55.71 | 45.7 / **61.1** / 85.6 | 42.5 / **63.9** / 97.8 |
| Synthetic politics indicator 2 (units) | 63.73 | 61.5 / **82.5** / 116 | 64.5 / **92.2** / 139 |
| Synthetic politics indicator 3 (units) | 68.98 | 48.9 / **65** / 91.9 | 40.1 / **63.5** / 99.9 |
| Synthetic politics indicator 4 (units) | 86.14 | 67.4 / **90.4** / 125 | 60.6 / **91.9** / 142 |
| Synthetic foodwater indicator 0 (units) | 18.88 | 17.6 / **23.6** / 33.2 | 17.7 / **26.1** / 39.3 |
| Synthetic foodwater indicator 1 (units) | 72.25 | 53.7 / **71** / 99.7 | 46.7 / **71.2** / 110 |
| Synthetic foodwater indicator 2 (units) | 37.73 | 30.1 / **40.2** / 56.4 | 27.8 / **41.7** / 62.9 |
| Synthetic foodwater indicator 3 (units) | 60.05 | 41.2 / **54.7** / 76.5 | 33.1 / **51.8** / 82.1 |
| Synthetic foodwater indicator 4 (units) | 1.267 | 0.864 / **1.15** / 1.61 | 0.69 / **1.1** / 1.72 |

## What drives the outcome

Share of the variance in peak systemic stress attributable to each event firing at all. High-scoring nodes are the ones worth watching, because learning their resolution collapses the most uncertainty about everything else.

| Event | Variance share | P(by 2036) | Severity |
|---|---:|---:|---:|
| Synthetic foodwater event 10 | 3.0% | 58% | 5 |
| Synthetic demographics event 7 | 2.9% | 44% | 7 |
| Synthetic foodwater event 0 | 2.4% | 53% | 7 |
| Synthetic geopolitics event 2 | 2.1% | 31% | 8 |
| Synthetic ai event 3 | 2.0% | 32% | 4 |
| Synthetic economy event 11 | 2.0% | 48% | 9 |
| Synthetic climate event 6 | 1.9% | 52% | 5 |
| Synthetic foodwater event 6 | 1.9% | 55% | 6 |
| Synthetic health event 3 | 1.8% | 70% | 7 |
| Synthetic foodwater event 2 | 1.7% | 33% | 9 |
| Synthetic economy event 2 | 1.6% | 47% | 7 |
| Synthetic demographics event 5 | 1.6% | 17% | 7 |
| Synthetic politics event 6 | 1.6% | 43% | 6 |
| Synthetic economy event 0 | 1.6% | 45% | 4 |
| Synthetic ai event 0 | 1.5% | 31% | 6 |
| Synthetic energy event 2 | 1.4% | 58% | 7 |
| Synthetic economy event 7 | 1.4% | 50% | 4 |
| Synthetic economy event 10 | 1.4% | 34% | 6 |

## Where the worldviews disagree most

The five parameterisations — raw analyst, audited, outside-view base rates, structural-break inside view, and prediction-market check — converge on most nodes. These are the ones where they don't, and they are exactly the forecasts you should hold most loosely.

| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |
|---|---:|---:|---:|---:|---:|---:|
| Synthetic climate event 9 | 90% | 90% | 27% | 88% | 89% | 63pp |
| Synthetic energy event 9 | 2.4% | 2.1% | 3.3% | 55% | 2.1% | 53pp |
| Synthetic politics event 9 | 94% | 95% | 95% | 44% | 94% | 51pp |
| Synthetic economy event 7 | 58% | 58% | 58% | 10% | 59% | 49pp |
| Synthetic ai event 7 | 25% | 26% | 26% | 72% | 25% | 48pp |
| Synthetic ai event 0 | 23% | 20% | 20% | 35% | 62% | 42pp |
| Synthetic economy event 10 | 44% | 46% | 26% | 5.2% | 44% | 40pp |
| Synthetic health event 6 | 26% | 25% | 55% | 26% | 64% | 39pp |
| Synthetic ai event 11 | 95% | 94% | 94% | 95% | 57% | 38pp |
| Synthetic climate event 4 | 18% | 22% | 53% | 56% | 20% | 38pp |
| Synthetic economy event 1 | 84% | 81% | 59% | 80% | 46% | 37pp |
| Synthetic climate event 10 | 32% | 29% | 13% | 46% | 31% | 33pp |
| Synthetic geopolitics event 7 | 87% | 88% | 61% | 89% | 90% | 29pp |
| Synthetic health event 5 | 48% | 46% | 21% | 49% | 49% | 28pp |
| Synthetic ai event 5 | 17% | 18% | 18% | 16% | 43% | 27pp |
| Synthetic geopolitics event 10 | 37% | 37% | 36% | 38% | 63% | 27pp |

## What this model cannot do

- **The parameters are elicited judgement, not measurement.** The engine is exact; the inputs are informed opinion, audited and red-teamed but still opinion. Simulation precision does not create forecast accuracy, and the 90% bands cover disagreement between the modelled worldviews, not the possibility that all five are wrong together.
- **Correlated error is unmodelled.** If the analysts share a blind spot, the ensemble inherits it silently and reports narrow bands over a wrong centre.
- **Resolution criteria carry real weight.** Several forecasts move by tens of percentage points on the wording of what counts. Read the criteria before quoting a number.
- **Nothing outside the risk set can happen.** The events that most reshape a decade are frequently ones nobody enumerated in advance. Treat the 'no severe event' probability as an upper bound on calm.
- **Causal edges are assumed, not estimated.** The dependency structure comes from domain reasoning about transmission channels, not from fitting historical co-occurrence — there is no dataset of decades to fit it to.
- **Hazards are conditionally memoryless within each segment.** Real crises have internal dynamics — mobilisation, negotiation, exhaustion — that a piecewise exponential cannot represent.
- *geopolitics*: synthetic uncertainty
- *climate*: synthetic uncertainty
- *economy*: synthetic uncertainty
- *ai*: synthetic uncertainty
- *energy*: synthetic uncertainty
- *demographics*: synthetic uncertainty
- *health*: synthetic uncertainty
- *politics*: synthetic uncertainty
- *foodwater*: synthetic uncertainty

---

*Generated by the `worldsim` Monte Carlo engine. Parameters, dependency structure, and red-team corrections are in `params/`; rerun with `python run_simulation.py`.*
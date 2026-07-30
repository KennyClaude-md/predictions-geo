# World Futures Simulation — Forecast Report

**Simulation date:** 2026-07-29  
**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  
**Paths:** 350,000 across 5 worldviews × 700 parameter worlds  
**Risk nodes:** 240 · **causal edges:** 118 · **latent factors:** 6 · **continuous variables:** 112

---

## How to read this

Every number below is the output of a survival-process Monte Carlo, not a guess written directly. Ten domains were parameterised against current sources, audited for base-rate discipline, then red-teamed from three directions. Each of those opinions is run as a separate worldview and the results are pooled by weight.

**The bracketed range is not the range of outcomes** — the event either happens or it doesn't. It is the range of *the probability itself* across parameter worlds: how much the answer moves depending on whose model of the world you accept. A wide bracket means the forecast is fragile. Monte Carlo noise has been subtracted out, so what remains is real disagreement.

**Calibration check:** simulated marginals reproduce the elicited cumulative probabilities to within 1.53 percentage points (worst node, worst worldview). This matters: the dependency network is tuned to reshape the *joint* distribution — which events co-occur — without inflating any individual probability above what the underlying analysis actually claimed.

## Headline forecasts

Ranked by expected systemic impact — probability by 2036 multiplied by severity — rather than by probability alone, because a 12% chance of something that reorders the world outranks a near-certainty that doesn't.

| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Impact |
|---|-------|--------:|--------:|--------:|:---------------:|----:|
| 1 | **Frontier agent reaches a 1-work-month 50%-reliability task horizon** | 8.7% | 65% | 76% | [42%–98%] | 9 |
| 2 | **Civil war onset in a country of 50 million or more that was at peace in mid-2026** | 28% | 65% | 83% | [59%–98%] | 8 |
| 3 | **Japan 10-year government bond yield reaches 3.00%** | 58% | 74% | 91% | [51%–>99%] | 7 |
| 4 | **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** | 63% | 76% | 79% | [44%–98%] | 8 |
| 5 | **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** | 88% | 93% | 98% | [94%–>99%] | 6 |
| 6 | **New round of major direct Israel-Iran exchange** | 52% | 76% | 83% | [61%–97%] | 7 |
| 7 | **China annual births fall below 7.0 million** | 45% | 96% | 97% | [91%–>99%] | 6 |
| 8 | **China's extraterritorial rare-earth export control regime enters into force** | 45% | 76% | 83% | [55%–98%] | 7 |
| 9 | **Renewed major US and/or Israeli air campaign against Iran** | 19% | 55% | 78% | [38%–>99%] | 7 |
| 10 | **A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test** | 15% | 45% | 68% | [27%–99%] | 8 |
| 11 | **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** | 18% | 57% | 75% | [47%–94%] | 7 |
| 12 | **Nvidia suffers a ≥50% peak-to-trough drawdown** | 28% | 65% | 83% | [57%–97%] | 6 |
| 13 | **US recession with NBER-dated peak in the window** | 25% | 58% | 83% | [59%–98%] | 6 |
| 14 | **A single training run of ≥1e28 FLOP is publicly reported** | 9.2% | 71% | 82% | [58%–98%] | 6 |
| 15 | **US unemployment rate ≥6.0% for three consecutive months** | 14% | 56% | 82% | [56%–97%] | 6 |
| 16 | **China reports annual real GDP growth below 4.0%** | 21% | 66% | 82% | [57%–98%] | 6 |
| 17 | **China's officially reported population falls below 1.400 billion** | 58% | 96% | 98% | [93%–>99%] | 5 |
| 18 | **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** | 15% | 45% | 61% | [34%–84%] | 8 |
| 19 | **New IPC/CH Famine (Phase 5) classification anywhere** | 69% | 93% | 97% | [91%–>99%] | 5 |
| 20 | **Disintegration of the Thwaites Eastern Ice Shelf** | 13% | 38% | 60% | [22%–96%] | 8 |
| 21 | **A top-4 US hyperscaler guides annual capex down year-over-year** | 21% | 74% | 80% | [57%–96%] | 6 |
| 22 | **Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt** | 15% | 45% | 68% | [28%–99%] | 7 |

## The decade in aggregate

Individual probabilities are the easy part. The question that actually determines how the 2030s feel is how many high-impact events land, and whether they land together.

**Read the impact rating carefully.** Analysts were asked for *global systemic impact if it occurs*, where 10 is civilization-altering — that is a measure of magnitude, not of badness. A transformative AI capability milestone legitimately scores 9 on it. These are high-impact events, not a count of catastrophes.

| Impact tier | Nodes | Expected count | Median | P(none) | P(≥2) | P(≥3) |
|---|---:|---:|---:|---:|---:|---:|
| **6+ / 10** | 117 | 53.1 | 53 | <0.5% | >99% | >99% |
| **7+ / 10** | 73 | 27.3 | 27 | <0.5% | >99% | >99% |
| **8+ / 10** | 42 | 12.2 | 12 | <0.5% | >99% | >99% |
| **9+ / 10** | 14 | 2.7 | 3 | 3.5% | 79% | 51% |

The 6+ band is broad — it contains a US recession alongside a Taiwan contingency — so the headline that the median decade fires 53 of its 117 nodes says less about danger than it first appears. The discriminating number is the tier above: across 14 nodes rated 9 or 10 for global impact, the model expects 2.7 of them this decade, puts 96% on at least one and 79% on two or more. That is the finding: a decade with no order-changing event is a minority outcome, and the interesting variance is not *whether* they arrive but whether they arrive spaced out or together.

**A caveat on cross-domain comparison.** Each domain was rated by a different analyst against the same nominal 0–10 scale, and they did not use it identically: *geopolitics* averages 7.7 while *foodwater* averages 5.5 (overall 6.3). Some of that gap is real — great-power conflict genuinely carries more systemic weight than a macro data print — but some of it is rater drift, and it means the impact ranking tilts toward whichever domain scored most generously. Compare probabilities across domains freely; compare severities within a domain.

## Scenario archetypes

Paths were clustered on which major events fired and on the shape of the systemic-stress trajectory. These are not scenarios written in advance and then assigned probabilities — they are the shapes the simulation actually produced, priced by how much of the path mass fell into each.

### Manageable decade — institutional breakdown and technological discontinuity — **30%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is institutional breakdown compounded by technological discontinuity. Typical peak stress sits at the 35th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 100% here vs 83% overall
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — 100% here vs 83% overall
- **New round of major direct Israel-Iran exchange** — 100% here vs 83% overall
- **Japan 10-year government bond yield reaches 3.00%** — 100% here vs 91% overall

### Severe decade — institutional breakdown and Middle East conflict — **25%**

Concurrent failure across domains. Shocks arrive faster than systems absorb them, and the response to one degrades the capacity to answer the next. The distinguishing driver is institutional breakdown compounded by israel. Typical peak stress sits at the 84th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 98% here vs 83% overall
- **New round of major direct Israel-Iran exchange** — 97% here vs 83% overall
- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — 92% here vs 79% overall
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — 94% here vs 83% overall

### Manageable decade — Middle East conflict and institutional breakdown — **15%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is Middle East conflict compounded by institutional breakdown. Typical peak stress sits at the 40th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **New round of major direct Israel-Iran exchange** — 99% here vs 83% overall
- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 98% here vs 83% overall
- Nvidia suffers a ≥50% peak-to-trough drawdown — *suppressed*: 26% here vs 83% overall
- Japan 10-year government bond yield reaches 3.00% — *suppressed*: 59% here vs 91% overall

### Manageable decade — no dominant driver — **15%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 35th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- New round of major direct Israel-Iran exchange — *suppressed*: 0% here vs 83% overall
- Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) — *suppressed*: 32% here vs 79% overall

### Manageable decade — Middle East conflict — **15%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is Middle East conflict. Typical peak stress sits at the 44th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **New round of major direct Israel-Iran exchange** — 93% here vs 83% overall
- Civil war onset in a country of 50 million or more that was at peace in mid-2026 — *suppressed*: 0% here vs 83% overall

## Full results by domain

### AI, compute & transformative technology

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | 8.7% | 65% | 76% | [42%–98%] | 9 | 2029Q3 |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 18% | 57% | 75% | [47%–94%] | 7 | 2029Q4 |
| Nvidia suffers a ≥50% peak-to-trough drawdown | 28% | 65% | 83% | [57%–97%] | 6 | 2029Q2 |
| A single training run of ≥1e28 FLOP is publicly reported | 9.2% | 71% | 82% | [58%–98%] | 6 | 2029Q2 |
| US unemployment rate ≥6.0% for three consecutive months | 14% | 56% | 82% | [56%–97%] | 6 | 2030Q2 |
| A top-4 US hyperscaler guides annual capex down year-over-year | 21% | 74% | 80% | [57%–96%] | 6 | 2028Q4 |
| Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt | 15% | 45% | 68% | [28%–99%] | 7 | 2030Q1 |
| A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 23% | 63% | 84% | [63%–97%] | 5 | 2029Q3 |
| China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab | 3.5% | 28% | 58% | [20%–96%] | 7 | 2032Q1 |
| A top-5 Western frontier lab exits frontier training | 11% | 45% | 66% | [36%–90%] | 6 | 2030Q3 |
| A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month | 20% | 55% | 68% | [38%–93%] | 5 | 2029Q2 |
| Frontier capability plateau: 24 months with no material aggregate benchmark advance | 7.4% | 25% | 42% | [12%–83%] | 8 | 2030Q4 |
| US driverless robotaxi services exceed 5 million paid rides per week | 5.6% | 67% | 80% | [55%–97%] | 4 | 2029Q3 |
| US licenses its current-flagship datacenter GPU for general commercial sale to China | 14% | 42% | 52% | [18%–88%] | 6 | 2029Q2 |
| Confirmed theft or leak of frontier model weights | 6.6% | 22% | 38% | [10%–77%] | 8 | 2031Q1 |
| Grid emergency or load-shed event officially attributed in part to datacenter demand | 12% | 38% | 60% | [20%–97%] | 5 | 2030Q2 |
| Court judgment or settlement >=$5B against a frontier lab over training data, or an injunction restricting training on copyrighted corpora | 9.1% | 30% | 49% | [16%–89%] | 6 | 2030Q4 |
| US Congress enacts broad federal preemption of state AI laws | 12% | 34% | 54% | [28%–82%] | 5 | 2030Q2 |
| US enacts binding federal pre-deployment evaluation or licensing requirements for frontier models | 7.1% | 24% | 41% | [12%–81%] | 6 | 2031Q1 |
| A top mathematics journal publishes a paper whose central theorem was found primarily by AI | 12% | 51% | 75% | [49%–95%] | 3 | 2030Q1 |
| A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections | 14% | 38% | 50% | [26%–80%] | 4 | 2029Q3 |
| Taiwan Strait event materially disrupts advanced-node or CoWoS output | 2.5% | 9.1% | 16% | [3.3%–41%] | 10 | 2031Q2 |
| Binding US-China agreement on frontier AI compute or model thresholds | 1.5% | 8.0% | 16% | [6.2%–31%] | 4 | 2032Q1 |
| AI-assisted biological attack causing ≥10 deaths, officially confirmed | 1.3% | 4.0% | 6.3% | [<0.5%–18%] | 9 | 2030Q4 |
| A quantum computer publicly factors an RSA-2048 modulus | <0.5% | 1.4% | 6.6% | [2.1%–15%] | 8 | 2033Q4 |

<details><summary>Resolution criteria</summary>

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — METR (or a successor methodology it endorses) publishes a 50%-reliability time horizon of ≥167 hours of human-expert task time for a publicly deployed or externally evaluated frontier model.
- **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** — A government agency, CERT, or the victim organization publicly confirms an attack in which AI agents autonomously executed the majority of intrusion steps, AND documented direct losses exceed $1B (2026 USD) or the attack disrupted power, water, telecom, or payments service for >1 million people for >6 hours.
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — Nvidia's split-adjusted closing share price falls at least 50% below its all-time closing high, at any point in the window.
- **A single training run of ≥1e28 FLOP is publicly reported** — Epoch AI, a lab's own technical report, or two independent credible technical analyses attribute ≥1e28 FLOP of training compute to a single model training run.
- **US unemployment rate ≥6.0% for three consecutive months** — BLS headline U-3 seasonally adjusted unemployment rate is at or above 6.0% in three consecutive monthly releases.
- **A top-4 US hyperscaler guides annual capex down year-over-year** — Microsoft, Alphabet, Amazon, or Meta states in an official earnings release or call that its expected full-fiscal-year capital expenditures will be LOWER than the prior fiscal year's actual capex.
- **Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt** — A company or SPV whose primary business is AI/datacenter compute defaults on, or completes a distressed exchange of, >=$5B (2026 USD) of debt or lease obligations; or a rating agency downgrades >=$5B of AI-datacenter-backed debt to below investment grade.
- **A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI** — A Fortune 500 (US) or Fortune Global 500 company announces a workforce reduction of ≥10,000 positions in a single announcement, and its official communications name AI/automation as the primary stated cause (not merely one factor among several).
- **China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab** — Credible public confirmation (company announcement, government statement, or two independent major-outlet reports) that a China-built EUV scanner is exposing wafers in a commercial production fab, not merely a lab or prototype.
- **A top-5 Western frontier lab exits frontier training** — One of OpenAI, Anthropic, Google DeepMind, xAI, or Meta Superintelligence Labs is acquired, dissolved, files for bankruptcy protection, or publicly announces it will stop pretraining frontier-scale models.
- **A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month** — A model developed by a China-headquartered organization holds the top overall rank on Artificial Analysis's Intelligence Index or LMArena's overall text leaderboard continuously for at least 30 days.
- **Frontier capability plateau: 24 months with no material aggregate benchmark advance** — The top score on Artificial Analysis's Intelligence Index (or an endorsed successor composite) increases by less than 5 index points over any 24-consecutive-month period beginning after 2027-01-01.
- **US driverless robotaxi services exceed 5 million paid rides per week** — Publicly reported paid rides in fully driverless (no human safety operator in vehicle) commercial services in the US total ≥5,000,000 in a single week, summed across all operators.
- **US licenses its current-flagship datacenter GPU for general commercial sale to China** — BIS policy permits general (not narrowly case-by-case) export to Chinese commercial customers of Nvidia's then-current top-of-line datacenter accelerator, within one product generation of the US-available flagship.
- **Confirmed theft or leak of frontier model weights** — A frontier lab, a government agency, or two independent major outlets confirm that the full weights of a model within one generation of a Western frontier release were exfiltrated by an unauthorized party or publicly leaked.
- **Grid emergency or load-shed event officially attributed in part to datacenter demand** — A US RTO/ISO, NERC, or a state utility commission issues an official finding that a load-shed event, EEA-2/EEA-3 emergency, or rolling blackout affecting >100,000 customers was caused in part by datacenter load growth.
- **Court judgment or settlement >=$5B against a frontier lab over training data, or an injunction restricting training on copyrighted corpora** — A US or EU court enters final judgment, or a lab announces a settlement, of >=$5B (2026 USD) arising from training-data copyright/IP claims; OR a court issues an injunction (not stayed within 90 days) barring a frontier lab from training on a major copyrighted corpus.
- **US Congress enacts broad federal preemption of state AI laws** — A bill preempting state AI regulation across a broad category (beyond a single narrow domain like deepfakes) is signed into law by the President.
- **US enacts binding federal pre-deployment evaluation or licensing requirements for frontier models** — Federal legislation or a binding rule with statutory authority is enacted requiring pre-deployment safety evaluation, reporting, or licensing for models above a compute or capability threshold, applicable to private-sector deployment (not merely federal procurement).
- **A top mathematics journal publishes a paper whose central theorem was found primarily by AI** — A paper appears in Annals of Mathematics, JAMS, Inventiones, Acta Mathematica, or Duke Mathematical Journal in which the authors explicitly state that the principal new theorem was discovered or proved primarily by an AI system rather than by the human authors.
- **A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections** — A US state enacts into law (governor's signature or veto override) a moratorium, ban, or binding numerical cap on new datacenter grid interconnections above a stated size threshold, applying statewide.
- **Taiwan Strait event materially disrupts advanced-node or CoWoS output** — TSMC publicly suspends or reduces N3/N2 or CoWoS output for >=30 consecutive days, or advanced-node/HBM/CoWoS exports from Taiwan fall >=25% month-over-month, as a direct result of military action, blockade, quarantine, or interdiction by the PRC.
- **Binding US-China agreement on frontier AI compute or model thresholds** — The US and China both sign a treaty, executive agreement, or equivalent binding instrument containing specific, verifiable commitments on frontier AI training compute limits, model capability thresholds, or mutual inspection.
- **AI-assisted biological attack causing ≥10 deaths, officially confirmed** — A national government, WHO, or equivalent official body confirms a deliberate biological release causing ≥10 human deaths, and officially states that AI tools materially assisted the design, synthesis planning, or acquisition of the agent.
- **A quantum computer publicly factors an RSA-2048 modulus** — A verifiable public demonstration in which a quantum computer factors a 2048-bit RSA modulus, with the factorization independently confirmed and the computation not reducible to classical pre-processing or special-structure moduli.

</details>

### Political stability & governance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Civil war onset in a country of 50 million or more that was at peace in mid-2026 | 28% | 65% | 83% | [59%–98%] | 8 | 2029Q1 |
| AfD enters government at German federal or Land level | 12% | 48% | 71% | [44%–93%] | 7 | 2030Q2 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 15% | 45% | 61% | [34%–84%] | 8 | 2029Q4 |
| Single US political-violence attack killing ten or more people | 25% | 62% | 78% | [51%–97%] | 6 | 2029Q1 |
| Democrats control at least one chamber of Congress from January 2027 | 90% | 90% | 90% | [79%–97%] | 5 | 2026Q4 |
| A calendar year with three or more successful coups d'etat worldwide | 45% | 74% | 85% | [63%–98%] | 5 | 2027Q4 |
| Vladimir Putin ceases to be Russia's paramount leader | 7.1% | 25% | 48% | [23%–75%] | 8 | 2031Q4 |
| Saudi succession from King Salman | 36% | 80% | 95% | [77%–>99%] | 4 | 2028Q3 |
| Xi Jinping ceases to be CCP General Secretary | 4.5% | 17% | 40% | [11%–80%] | 9 | 2032Q3 |
| National Rally (or RN-aligned candidate) wins the French presidency | 35% | 35% | 51% | [27%–79%] | 7 | 2027Q3 |
| Criminal conviction of a major US opposition figure in a prosecution widely coded as politically motivated | 7.9% | 26% | 44% | [12%–86%] | 7 | 2030Q4 |
| The Islamic Republic of Iran ceases to exist as a governing system | 9.4% | 23% | 33% | [10%–67%] | 9 | 2030Q1 |
| Overt US military strike inside Mexican territory without Mexican consent | 25% | 35% | 39% | [19%–68%] | 7 | 2027Q3 |
| Nigerian 2027 general election breakdown | 6.4% | 22% | 38% | [9.6%–79%] | 7 | 2031Q1 |
| Major democratic rupture or mass communal violence in India | 5.0% | 17% | 30% | [7.4%–67%] | 8 | 2031Q2 |
| Reform UK leads a UK government | 3.1% | 29% | 39% | [10%–78%] | 6 | 2030Q2 |
| Contested certification of the 2028 US presidential election | 3.9% | 14% | 25% | [5.5%–58%] | 9 | 2031Q2 |
| US President formally invokes the Insurrection Act over a state's objection | 21% | 32% | 37% | [18%–63%] | 6 | 2027Q3 |
| US executive branch openly defies a final Supreme Court order | 7.2% | 13% | 17% | [3.3%–42%] | 9 | 2028Q4 |
| Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice | 5.6% | 13% | 21% | [8.0%–40%] | 7 | 2030Q2 |
| Global autocratization wave inflects | 9.3% | 30% | 50% | [16%–90%] | 2 | 2030Q4 |
| Trump formally pursues a third presidential term | 4.0% | 8.1% | 9.8% | [3.6%–19%] | 8 | 2028Q4 |
| An EU member state initiates exit from the EU | 2.0% | 6.0% | 8.4% | [3.0%–17%] | 8 | 2030Q1 |
| Armed confrontation between US state-controlled forces and federal forces | 3.1% | 6.3% | 8.2% | [1.4%–23%] | 8 | 2029Q2 |

<details><summary>Resolution criteria</summary>

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — A country with population of at least 50 million, not experiencing an armed conflict with at least 1,000 battle-related deaths in 2025, records at least 1,000 battle-related deaths in a single calendar year in an internal armed conflict, per UCDP/PRIO coding.
- **AfD enters government at German federal or Land level** — The AfD holds at least one ministerial post in a German federal or state (Land) government, or formally signs a written toleration/confidence-and-supply agreement supporting such a government. Issue-by-issue parliamentary cooperation does not count.
- **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** — In any V-Dem annual Democracy Report from 2027 through 2037, a NATO or EU member state that was coded as a liberal or electoral democracy in the 2026 report is coded as an electoral autocracy or closed autocracy. Turkey's and Hungary's pre-2026 coding do not qualify.
- **Single US political-violence attack killing ten or more people** — A single attack on US soil kills at least 10 people (excluding perpetrators) and is officially determined by federal law enforcement, or coded by START/GTD, as politically, religiously, racially or ideologically motivated. Ordinary criminal and non-ideological mass shootings excluded.
- **Democrats control at least one chamber of Congress from January 2027** — Following the 3 November 2026 elections, Democrats (including caucusing independents) hold a majority of seats in the US House and/or Senate when the new Congress convenes on 3 January 2027.
- **A calendar year with three or more successful coups d'etat worldwide** — In any single calendar year from 2026 onward, at least three successful coups d'etat occur globally, where 'successful' means the coup leadership holds effective power for at least seven days, per Powell-Thyne / Cline Center coding.
- **Vladimir Putin ceases to be Russia's paramount leader** — Putin is no longer president of Russia (or, if the office is restructured, no longer the recognized paramount decision-maker) for a continuous period exceeding 60 days, through death, incapacity, resignation, removal or coup.
- **Saudi succession from King Salman** — King Salman bin Abdulaziz (b. December 1935) ceases to be King of Saudi Arabia through death, incapacity or abdication, and a successor is proclaimed, by end-2031.
- **Xi Jinping ceases to be CCP General Secretary** — Xi Jinping is no longer General Secretary of the Chinese Communist Party for a continuous period exceeding 60 days, for any reason.
- **National Rally (or RN-aligned candidate) wins the French presidency** — A candidate endorsed by, or a member of, Rassemblement National (or its formal successor) is elected President of France in the 2027 or 2032 presidential election and inaugurated.
- **Criminal conviction of a major US opposition figure in a prosecution widely coded as politically motivated** — By end-2031, a sitting or former US governor, senator, House member in leadership, cabinet secretary, presidential nominee, or FBI/CIA director is convicted at trial in a federal prosecution that at least three of AP/Reuters/NYT/WSJ/WaPo characterize as politically motivated or retaliatory, or that Protect Democracy's Retaliatory Action Tracker records as such.
- **The Islamic Republic of Iran ceases to exist as a governing system** — A government controls Tehran that does not derive its authority from velayat-e faqih - the office of Supreme Leader is abolished, left vacant for more than 12 months with no successor, or subordinated to a non-clerical executive - sustained for at least 90 days.
- **Overt US military strike inside Mexican territory without Mexican consent** — The US government publicly acknowledges, or three major wire services confirm, a US military kinetic strike (manned aircraft, drone, missile or ground raid) on a target inside Mexican sovereign territory that the Mexican federal government publicly states it did not consent to.
- **Nigerian 2027 general election breakdown** — The February 2027 Nigerian general election produces at least 500 election-related deaths within 90 days of polling per ACLED, OR the presidential result is annulled or the transfer of power prevented or delayed beyond the 29 May 2027 inauguration date, OR the military intervenes in the transfer of power.
- **Major democratic rupture or mass communal violence in India** — By end-2031, either (a) V-Dem downgrades India from electoral autocracy to closed autocracy, or (b) India records at least 1,000 deaths in communal, sectarian or state-repression political violence in a single calendar year per ACLED or UCDP coding, or (c) a national election is postponed beyond its constitutional deadline or its result is not accepted by the losing coalition.
- **Reform UK leads a UK government** — A Reform UK MP is appointed Prime Minister of the United Kingdom.
- **Contested certification of the 2028 US presidential election** — Following the 7 November 2028 election, at least one state transmits competing slates of presidential electors to Congress, OR a state fails to certify by the Electoral Count Reform Act's safe-harbour deadline and the dispute reaches Congress or the Supreme Court, OR the joint session on 6 January 2029 sustains an objection to a state's electors.
- **US President formally invokes the Insurrection Act over a state's objection** — A presidential proclamation expressly invoking 10 U.S.C. sections 251-255 (the Insurrection Act) to deploy federal troops or federalized National Guard for domestic law enforcement inside a US state whose governor has publicly objected, confirmed by the Federal Register and major wire services.
- **US executive branch openly defies a final Supreme Court order** — The executive branch publicly and knowingly fails to comply with a final, non-stayed order of the US Supreme Court for more than 30 days, and this non-compliance is (a) asserted in a filing or opinion by the Court or a lower court on remand, or (b) reported as such by at least three of AP/Reuters/NYT/WSJ/WaPo. Slow-walking with a colorable legal argument does not count.
- **Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice** — A sitting US president, vice president, member of the House or Senate, Senate-confirmed cabinet secretary, or Supreme Court justice is killed in an attack determined by federal law enforcement to be politically, ideologically or personally-grievance motivated. Natural death, accident and ordinary criminal robbery excluded.
- **Global autocratization wave inflects** — In any V-Dem Democracy Report from 2028 through 2032, either the count of countries coded as currently autocratizing falls below 35, OR the number of democratizing countries exceeds the number autocratizing; alternatively, any Freedom in the World edition through 2032 records more countries improving than declining.
- **Trump formally pursues a third presidential term** — Donald Trump files FEC paperwork as a candidate for president in 2028, is placed on a primary ballot in any state as a presidential candidate, or is formally nominated as the Republican presidential or vice-presidential candidate for 2028.
- **An EU member state initiates exit from the EU** — An EU member state's government formally notifies the European Council under Article 50 TEU, or a nationally binding referendum on EU membership is held in a member state.
- **Armed confrontation between US state-controlled forces and federal forces** — A US governor issues an order directing state law enforcement or state-controlled National Guard to physically block or detain federal agents/troops, AND an armed confrontation occurs producing at least one death or at least one state officer detaining a federal officer (or vice versa) at gunpoint. Litigation, non-cooperation policies and protest-line scuffles do not count.

</details>

### Global macroeconomy & finance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Sustained effective closure of the Strait of Hormuz | 69% | 78% | 82% | [53%–98%] | 8 | 2026Q4 |
| Japan 10-year government bond yield reaches 3.00% | 58% | 74% | 91% | [51%–>99%] | 7 | 2027Q2 |
| US recession with NBER-dated peak in the window | 25% | 58% | 83% | [59%–98%] | 6 | 2029Q3 |
| China reports annual real GDP growth below 4.0% | 21% | 66% | 82% | [57%–98%] | 6 | 2029Q2 |
| Global recession (world real GDP growth below 2.0% in a calendar year) | 12% | 38% | 62% | [39%–83%] | 7 | 2030Q4 |
| Brent crude settles above $120/bbl | 38% | 57% | 70% | [38%–90%] | 6 | 2027Q4 |
| US Treasury market dysfunction requiring emergency Fed intervention | 9.8% | 32% | 52% | [17%–92%] | 8 | 2030Q3 |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 7.1% | 40% | 57% | [21%–93%] | 7 | 2030Q1 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 11% | 28% | 49% | [24%–74%] | 8 | 2031Q1 |
| Wave of emerging-market sovereign defaults or restructurings | 31% | 60% | 76% | [49%–94%] | 5 | 2028Q4 |
| S&P 500 falls 30%+ from its all-time closing high | 15% | 45% | 63% | [40%–85%] | 6 | 2030Q1 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 15% | 35% | 56% | [32%–79%] | 6 | 2030Q3 |
| Disorderly yen move | 11% | 34% | 55% | [19%–94%] | 6 | 2030Q3 |
| Disorderly broad dollar depreciation | 9.5% | 30% | 50% | [15%–91%] | 6 | 2030Q3 |
| US 10-year Treasury yield closes at or above 6.00% | 6.1% | 24% | 37% | [17%–59%] | 8 | 2030Q3 |
| Formal breach of Federal Reserve independence | 7.3% | 24% | 41% | [11%–82%] | 7 | 2031Q1 |
| US CPI inflation returns to 5.0%+ year over year | 22% | 43% | 56% | [28%–83%] | 5 | 2029Q1 |
| US dollar share of allocated FX reserves falls below 50% | 2.1% | 23% | 45% | [22%–72%] | 6 | 2031Q4 |
| China announces a central-government property/LGFV rescue of RMB 5trn or more | 13% | 33% | 51% | [17%–89%] | 5 | 2030Q2 |
| US average effective tariff rate exceeds 15% | 18% | 41% | 50% | [21%–82%] | 5 | 2029Q1 |
| Systemic financial market infrastructure outage | 4.7% | 16% | 28% | [6.7%–64%] | 7 | 2031Q1 |
| Taiwan semiconductor supply disruption with global market resolution | 3.2% | 11% | 20% | [4.3%–51%] | 9 | 2031Q2 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 4.6% | 15% | 24% | [6.0%–54%] | 7 | 2030Q4 |
| Major stablecoin failure or sustained depeg | 17% | 29% | 39% | [11%–79%] | 4 | 2028Q4 |
| US inflation undershoot / deflation scare | 5.7% | 20% | 34% | [9.2%–74%] | 4 | 2031Q1 |

<details><summary>Resolution criteria</summary>

- **Sustained effective closure of the Strait of Hormuz** — Seaborne crude and condensate transits through the Strait of Hormuz fall more than 50% below the 2025 monthly average for at least 14 consecutive days, per IEA, EIA, Kpler or Vortexa reporting, at any point from August 2026 onward.
- **Japan 10-year government bond yield reaches 3.00%** — The 10-year JGB benchmark yield closes at or above 3.00% on any day in the window.
- **US recession with NBER-dated peak in the window** — NBER Business Cycle Dating Committee assigns a business-cycle peak dated between August 2026 and the end of the stated year. Later announcement is fine; the peak date is what counts.
- **China reports annual real GDP growth below 4.0%** — China's National Bureau of Statistics reports full-year real GDP growth below 4.0% for any calendar year in the window, in the initial annual release.
- **Global recession (world real GDP growth below 2.0% in a calendar year)** — IMF WEO (October vintage of the following year) reports world real GDP growth at market or PPP weights below 2.0% for any calendar year in the window. Resolves YES on the first such year.
- **Brent crude settles above $120/bbl** — ICE Brent front-month futures settle at or above $120.00/bbl on any trading day in the window.
- **US Treasury market dysfunction requiring emergency Fed intervention** — The Federal Reserve announces unscheduled purchases of Treasury securities, a new or expanded standing repo/dealer facility, or explicit market-functioning operations (not policy QE and not routine reserve management) in response to disorderly conditions in the Treasury or repo market, at any point in the window.
- **AI capex bust: aggregate hyperscaler capex falls 20%+ year over year** — Combined calendar-year capital expenditure of Microsoft, Alphabet, Amazon, Meta and Oracle, as reported in audited annual filings, comes in at least 20% below the prior calendar year's reported total, for any year in the window.
- **Failure or extraordinary rescue of a bank with over $250bn in assets** — A bank holding company with more than $250bn in total assets in the US, EU, UK, Switzerland, Japan or China fails, is placed into resolution, is forced into a state-brokered merger, or receives an extraordinary government capital injection or central bank emergency liquidity facility created specifically for it.
- **Wave of emerging-market sovereign defaults or restructurings** — At least three additional sovereigns, each with more than $10bn in external public debt, default on external commercial debt or formally enter a comprehensive debt restructuring or a new IMF Extended Fund Facility of at least $3bn, between August 2026 and the end of the stated year.
- **S&P 500 falls 30%+ from its all-time closing high** — S&P 500 records a daily close at least 30% below its prior all-time closing high, at any point in the window.
- **Large private-credit vehicle suspends redemptions or enters wind-down** — A private credit fund, BDC or interval fund with at least $20bn NAV fully suspends redemptions (beyond pro-rating within stated quarterly limits) for at least one month, or is placed into wind-down or forced sale, in the US, UK or EU.
- **Disorderly yen move** — USD/JPY closes above 180, or moves more than 15 yen in either direction within any 20 trading days, in the window.
- **Disorderly broad dollar depreciation** — The Fed's broad nominal trade-weighted dollar index falls 20% or more from its trailing 24-month high within any 24-month period in the window.
- **US 10-year Treasury yield closes at or above 6.00%** — The constant-maturity 10-year US Treasury yield (H.15 / Treasury daily par yield curve) closes at or above 6.00% on any day in the window.
- **Formal breach of Federal Reserve independence** — A sitting US president attempts to remove or demote a Federal Reserve governor or the chair for policy reasons, issues a directive on the policy rate that the Board acts on, or legislation altering the FOMC's control of the policy rate is enacted — any one, in the window.
- **US CPI inflation returns to 5.0%+ year over year** — BLS reports headline CPI-U at or above 5.0% year over year for any single month in the window.
- **US dollar share of allocated FX reserves falls below 50%** — IMF COFER reports the US dollar share of allocated global foreign exchange reserves below 50.0% for any quarter in the window.
- **China announces a central-government property/LGFV rescue of RMB 5trn or more** — China's State Council, MOF or PBOC announces a single package of central-government fiscal support, debt assumption or recapitalization directed at the property sector and/or local government financing vehicles totalling at least RMB 5 trillion, announced as one program.
- **US average effective tariff rate exceeds 15%** — Penn Wharton Budget Model or Yale Budget Lab reports a US average effective tariff rate on all imports above 15.0% for at least one full month in the window.
- **Systemic financial market infrastructure outage** — A systemically important FMI — a major CCP, CLS, DTCC, Fedwire, TARGET2, SWIFT, or a top-three custodian — suffers an outage or compromise preventing settlement for more than 24 hours, or a central bank extends emergency liquidity explicitly because of it.
- **Taiwan semiconductor supply disruption with global market resolution** — Monthly semiconductor exports from Taiwan fall more than 40% below the trailing twelve-month average for two consecutive months, for any reason (blockade, quarantine, conflict, or major natural disaster), in the window.
- **France or Italy 10-year spread over Bunds exceeds 300bp** — The 10-year OAT-Bund or BTP-Bund spread closes above 300 basis points for five consecutive trading days, or the ECB formally activates the Transmission Protection Instrument for either sovereign.
- **Major stablecoin failure or sustained depeg** — A stablecoin with at least $20bn market capitalization trades more than 5% below its peg for more than 24 consecutive hours, or its issuer suspends or fails to honor redemptions for more than 24 hours.
- **US inflation undershoot / deflation scare** — US core PCE inflation prints below 1.0% year over year for three consecutive months, or headline CPI-U prints negative year over year for any month, in the window.

</details>

### Great-power conflict & geopolitics

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 63% | 76% | 79% | [44%–98%] | 8 | 2027Q1 |
| Durable Russia-Ukraine ceasefire (>=180 consecutive days) | 33% | 71% | 88% | [70%–98%] | 7 | 2028Q4 |
| Renewed major US and/or Israeli air campaign against Iran | 19% | 55% | 78% | [38%–>99%] | 7 | 2029Q4 |
| A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test | 15% | 45% | 68% | [27%–99%] | 8 | 2030Q1 |
| A second US kinetic operation to remove or kill a sitting foreign head of state or government | 13% | 40% | 62% | [22%–98%] | 7 | 2030Q2 |
| PRC forces cause the death of a Philippine serviceman or coast guardsman | 12% | 38% | 60% | [21%–97%] | 7 | 2030Q2 |
| Iran formally withdraws from the Nuclear Non-Proliferation Treaty | 15% | 45% | 68% | [27%–99%] | 6 | 2030Q1 |
| Vladimir Putin ceases to hold effective power in Russia | 6.9% | 25% | 49% | [16%–88%] | 8 | 2031Q4 |
| New US-Russia agreement capping deployed strategic nuclear warheads | 19% | 39% | 51% | [17%–87%] | 6 | 2029Q2 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 6.3% | 23% | 38% | [14%–72%] | 8 | 2031Q1 |
| Lethal DPRK-ROK military exchange | 9.7% | 31% | 50% | [16%–90%] | 6 | 2030Q3 |
| The Islamic Republic ceases to govern Iran | 9.4% | 24% | 33% | [8.0%–72%] | 8 | 2029Q4 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 6.0% | 19% | 28% | [11%–48%] | 9 | 2030Q2 |
| North Korea conducts a seventh nuclear explosive test | 11% | 30% | 44% | [22%–72%] | 5 | 2030Q1 |
| India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months | 6.0% | 17% | 27% | [12%–47%] | 8 | 2030Q3 |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 4.1% | 15% | 27% | [5.5%–65%] | 8 | 2031Q2 |
| PRC seizes or occupies a Taiwan-administered offshore island | 3.8% | 13% | 24% | [5.0%–56%] | 7 | 2031Q2 |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 3.1% | 11% | 20% | [4.4%–53%] | 7 | 2031Q2 |
| Lethal armed clash between Chinese and Japanese state forces | 3.1% | 10% | 17% | [3.9%–40%] | 8 | 2031Q1 |
| A jihadist insurgent group controls a Sahelian national capital for >=7 days | 7.0% | 18% | 25% | [11%–45%] | 5 | 2029Q4 |
| Direct US-PRC military exchange causing at least one fatality | 2.0% | 7.2% | 13% | [5.7%–26%] | 9 | 2031Q3 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 2.2% | 5.5% | 12% | [4.1%–23%] | 10 | 2032Q2 |
| NATO invokes Article 5 in response to a Russian attack | 3.0% | 7.3% | 11% | [3.7%–24%] | 10 | 2030Q1 |
| US initiates withdrawal from NATO, or any member formally invokes Article 13 | 2.0% | 4.8% | 7.7% | [2.6%–15%] | 9 | 2030Q3 |
| A nuclear weapon is detonated in an act of war or hostility anywhere in the world | 1.1% | 4.0% | 6.8% | [0.6%–17%] | 10 | 2031Q2 |
| UN Security Council permanent membership formally expanded | 0.5% | 1.4% | 2.9% | [1.0%–6.4%] | 3 | 2032Q1 |

<details><summary>Resolution criteria</summary>

- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — Crude-plus-condensate transit through Hormuz, per EIA/Vortexa/Kpler monthly data, falls below 50% of the 2025 monthly average for at least 30 consecutive days, in an episode beginning on or after 1 August 2026.
- **Durable Russia-Ukraine ceasefire (>=180 consecutive days)** — A ceasefire covering the entire land front between Russian and Ukrainian forces holds for at least 180 consecutive days without resumption of sustained offensive ground operations or systematic long-range strikes on cities, as assessed by ISW/OSCE-successor monitoring or equivalent consensus reporting. Short holiday truces (e.g. April/May 2026) do NOT count.
- **Renewed major US and/or Israeli air campaign against Iran** — At least 100 US and/or Israeli strikes on targets inside Iran within any 30-day window beginning on or after 1 August 2026, per credible multi-source reporting or US/Israeli government statement.
- **A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test** — The United States, Russia or China conducts a supercritical nuclear explosive test (yield above zero, excluding subcritical and hydrodynamic experiments), confirmed by the testing state or by CTBTO/national technical means.
- **A second US kinetic operation to remove or kill a sitting foreign head of state or government** — US forces, after 1 August 2026, conduct a military operation that captures, kills, or directly precipitates within 30 days the removal from power of the sitting head of state or government of a UN member state, excluding the January 2026 Venezuela and February 2026 Iran operations.
- **PRC forces cause the death of a Philippine serviceman or coast guardsman** — An action by PLA, PLAN, China Coast Guard or maritime-militia units (including ramming, water cannon, boarding or fire) directly causes at least one death among Philippine armed forces, coast guard or government-chartered personnel, confirmed by the Philippine government.
- **Iran formally withdraws from the Nuclear Non-Proliferation Treaty** — Iran deposits formal notice of withdrawal under NPT Article X with the depositary governments and the UN Security Council, or that withdrawal takes effect.
- **Vladimir Putin ceases to hold effective power in Russia** — Putin ceases to serve as President of the Russian Federation, or is assessed by consensus of major-power governments no longer to exercise effective control over Russian state decision-making, for any reason including death, incapacity, resignation or removal.
- **New US-Russia agreement capping deployed strategic nuclear warheads** — The US and Russia sign a bilateral agreement (treaty, executive agreement, or formal reciprocal political commitment announced by both heads of state) that establishes a numerical ceiling on deployed strategic nuclear warheads or delivery vehicles.
- **A state that does not now possess nuclear weapons tests a device or is confirmed to possess one** — Any state other than the US, Russia, UK, France, China, India, Pakistan, Israel and North Korea either (a) conducts a nuclear explosive test, (b) officially declares possession of an assembled nuclear weapon, or (c) is assessed by the IAEA or by the US intelligence community in a public statement to possess one.
- **Lethal DPRK-ROK military exchange** — An exchange of fire or attack between DPRK and ROK forces causing at least five combined military or civilian deaths, confirmed by either government or by the UN Command.
- **The Islamic Republic ceases to govern Iran** — The office of Supreme Leader (Velayat-e Faqih) is abolished, vacated without a successor for more than 90 days, or a government not derived from the clerical/IRGC establishment exercises effective control of Tehran; as assessed by consensus of major-power governments.
- **PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days** — PRC state organs (PLA, Coast Guard or maritime authorities) publicly declare a quarantine, inspection regime or blockade of Taiwan's ports/airspace AND enforce it by boarding, turning back or interdicting at least ten commercial vessels or aircraft, sustained for at least seven consecutive days.
- **North Korea conducts a seventh nuclear explosive test** — A nuclear explosive test on DPRK territory confirmed by CTBTO seismic/radionuclide detection or by US/ROK/Japanese government statement.
- **India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months** — Direct state-on-state armed conflict between Indian and Pakistani forces producing at least 1,000 combined military and civilian deaths within any rolling 12-month period, per UCDP or ACLED coding.
- **Iran tests or is confirmed to possess an assembled nuclear weapon** — Iran conducts a nuclear explosive test, publicly declares possession, or is publicly assessed by the IAEA or the US intelligence community to possess at least one assembled nuclear weapon.
- **PRC seizes or occupies a Taiwan-administered offshore island** — PLA, PAP or China Coast Guard forces land on and establish administrative or military control over Pratas (Dongsha), Taiping (Itu Aba), Kinmen, Matsu or Wuqiu, maintained for at least 72 consecutive hours, confirmed by Taiwan MND or US government statement.
- **State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country** — A cyberattack publicly attributed by the victim government or by the EU/NATO to a state or state-sponsored actor causes loss of electrical supply to at least one million people for at least 24 consecutive hours in a NATO or OECD member state.
- **Lethal armed clash between Chinese and Japanese state forces** — An exchange of fire or deliberate ramming between PLA/CCG and JSDF/JCG units resulting in at least one death, confirmed by either government.
- **A jihadist insurgent group controls a Sahelian national capital for >=7 days** — JNIM, ISSP/ISWAP or a successor jihadist organisation exercises effective control of Bamako, Ouagadougou or Niamey (including the presidential palace and central districts) for at least seven consecutive days, per ACLED coding or UN/Security Council reporting.
- **Direct US-PRC military exchange causing at least one fatality** — An exchange of fire (kinetic, including missile, air, naval or ground fire) between US and PLA/PAP/China Coast Guard forces resulting in at least one death on either side, acknowledged by either government or confirmed by credible multi-source reporting.
- **PRC launches an amphibious or airborne assault on Taiwan's main island** — PLA forces conduct an opposed landing or airborne insertion on Taiwan proper (not offshore islands) involving at least 1,000 personnel, confirmed by Taiwan MND or US government statement.
- **NATO invokes Article 5 in response to a Russian attack** — The North Atlantic Council formally invokes Article 5 of the Washington Treaty citing an armed attack attributable to Russia or Belarus.
- **US initiates withdrawal from NATO, or any member formally invokes Article 13** — The US President formally notifies the depositary of intent to withdraw under Article 13 of the North Atlantic Treaty, or any other member state does so.
- **A nuclear weapon is detonated in an act of war or hostility anywhere in the world** — A nuclear explosive device is detonated with hostile intent against a state, non-state actor or territory (excluding tests, accidents and demonstration detonations over unpopulated own territory), confirmed by the detonating state or by CTBTO/national technical means.
- **UN Security Council permanent membership formally expanded** — An amendment to the UN Charter expanding the number of permanent Security Council members enters into force following ratification by two-thirds of member states including all five current permanent members.

</details>

### Climate & Earth systems

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | 88% | 93% | 98% | [94%–>99%] | 6 | 2027Q1 |
| Global fossil CO2 emissions confirmed to have peaked | 9.9% | 36% | 69% | [42%–93%] | 7 | 2031Q3 |
| Disintegration of the Thwaites Eastern Ice Shelf | 13% | 38% | 60% | [22%–96%] | 8 | 2030Q2 |
| FAO Food Price Index exceeds 160 in any month | 14% | 44% | 71% | [41%–91%] | 6 | 2030Q4 |
| Long-term (multi-decadal) 1.5C breach formally declared | 4.9% | 40% | 84% | [59%–97%] | 5 | 2032Q1 |
| New record-low Antarctic sea ice minimum extent | 15% | 45% | 68% | [28%–99%] | 6 | 2030Q1 |
| A calendar year at or above 1.65C above pre-industrial | 61% | 90% | 97% | [88%–>99%] | 4 | 2027Q2 |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | 72% | 75% | 76% | [58%–94%] | 5 | 2027Q1 |
| Global insured natural catastrophe losses exceed $200bn in a calendar year | 13% | 40% | 62% | [24%–97%] | 6 | 2030Q2 |
| Combined Lake Powell + Lake Mead storage falls below 20% of capacity | 20% | 44% | 65% | [37%–89%] | 5 | 2029Q4 |
| Single heat event with >= 100,000 attributed excess deaths | 9.1% | 26% | 44% | [23%–67%] | 7 | 2030Q4 |
| A new record warmest calendar year, exceeding 2024 | 78% | 94% | 99% | [96%–>99%] | 3 | 2027Q2 |
| A second G20 economy formally withdraws from the Paris Agreement | 6.5% | 22% | 38% | [10%–78%] | 7 | 2031Q1 |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 5.9% | 19% | 36% | [17%–65%] | 6 | 2031Q3 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 1.8% | 13% | 26% | [6.5%–61%] | 8 | 2032Q1 |
| Formal international SRM governance decision adopted | 14% | 31% | 40% | [11%–80%] | 4 | 2029Q2 |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 4.0% | 11% | 19% | [4.0%–47%] | 8 | 2031Q1 |
| Final court judgment ordering >= $1bn in climate damages | 1.7% | 11% | 25% | [5.5%–61%] | 6 | 2032Q3 |
| Global mean methane annual growth rate falls to zero or below | 1.9% | 8.3% | 17% | [3.3%–47%] | 5 | 2032Q1 |
| VEI 6+ volcanic eruption with measurable global cooling | 2.6% | 9.2% | 17% | [3.1%–41%] | 5 | 2031Q3 |
| State-backed solar radiation management deployment announced or conducted | 0.7% | 5.9% | 10% | [1.8%–28%] | 8 | 2031Q2 |
| AMOC declared to have crossed a tipping point | <0.5% | 1.9% | 5.0% | [<0.5%–14%] | 10 | 2033Q1 |
| Arctic Ocean practically ice-free (extent below 1.0 million km2) | <0.5% | 1.7% | 8.2% | [2.1%–26%] | 5 | 2033Q4 |

<details><summary>Resolution criteria</summary>

- **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** — NOAA Coral Reef Watch reports that Alert Level 1 or higher bleaching-level heat stress affected at least 60% of the world's coral reef area within any rolling 12-month period.
- **Global fossil CO2 emissions confirmed to have peaked** — The Global Carbon Project reports global fossil CO2 emissions below the previous all-time high in two consecutive calendar years, with the peak year identified in the published Global Carbon Budget.
- **Disintegration of the Thwaites Eastern Ice Shelf** — Satellite observation (ESA/NASA, confirmed by NSIDC or a peer-reviewed publication) shows the Thwaites Eastern Ice Shelf has lost at least 50% of its 2020 area through fracture and calving within a three-year period.
- **FAO Food Price Index exceeds 160 in any month** — The FAO Food Price Index (nominal, 2014-2016 = 100) records a monthly value above 160.0, exceeding the March 2022 all-time high of 160.3.
- **Long-term (multi-decadal) 1.5C breach formally declared** — The WMO, IPCC (in AR7 or a special report), or the UNFCCC Global Stocktake formally states that the long-term global mean temperature increase - defined as a 20-year mean or current human-induced warming - has exceeded 1.5C above 1850-1900.
- **New record-low Antarctic sea ice minimum extent** — NSIDC reports an Antarctic daily minimum sea ice extent below the February 2023 record of 1.79 million km2.
- **A calendar year at or above 1.65C above pre-industrial** — ERA5 annual global mean surface temperature anomaly relative to 1850-1900 is >= 1.65C for a full calendar year, as published in the Copernicus Global Climate Highlights.
- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — NOAA CPC's Oceanic Nino Index (3-month running mean Nino3.4 anomaly, ERSSTv5 with the operational base period) reaches or exceeds +2.0C for at least one overlapping season during the 2026-27 event.
- **Global insured natural catastrophe losses exceed $200bn in a calendar year** — Swiss Re sigma or Munich Re NatCatSERVICE reports global insured losses from natural catastrophes above US$200 billion (nominal) for a single calendar year.
- **Combined Lake Powell + Lake Mead storage falls below 20% of capacity** — US Bureau of Reclamation end-of-month reservoir reports show combined active storage in Lake Powell and Lake Mead below 20% of combined live capacity.
- **Single heat event with >= 100,000 attributed excess deaths** — A peer-reviewed study or national statistical office attributes at least 100,000 excess deaths to a single heat wave or heat season within one country or contiguous region over a window of 90 days or less.
- **A new record warmest calendar year, exceeding 2024** — Copernicus ERA5 (with NASA GISTEMP and NOAA as corroboration) reports a calendar year with a global mean surface temperature anomaly exceeding the 2024 value (1.60C above 1850-1900) at the annual announcement in the following January.
- **A second G20 economy formally withdraws from the Paris Agreement** — A G20 member other than the United States deposits formal notification of withdrawal from the Paris Agreement with the UN Secretary-General.
- **Verified wet-bulb temperature of 35C sustained for three or more hours** — A quality-controlled surface station observation (or a national meteorological service's official record) documents a wet-bulb temperature of at least 35.0C sustained for at least three consecutive hours, confirmed in a peer-reviewed publication or by a national met service.
- **Amazon basin becomes a net annual carbon source for three consecutive years** — Peer-reviewed literature (atmospheric inversion, aircraft profile, or eddy-covariance synthesis accepted by the Global Carbon Project) establishes that the Amazon basin as a whole was a net annual source of carbon to the atmosphere in three consecutive calendar years.
- **Formal international SRM governance decision adopted** — UNEA, the UNFCCC COP, the CBD COP, or a comparable treaty body adopts a formal decision or instrument establishing an international governance framework for solar radiation modification (whether a non-use agreement, a research governance regime, or a moratorium codification), beyond the existing non-binding CBD language.
- **Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months** — The RAPID-MOCHA-WBTS array at 26N (or a successor observing system accepted as the reference by the AMOC research community) reports a 12-month running mean overturning transport at least 30% below the 2004-2023 mean, confirmed in a peer-reviewed publication.
- **Final court judgment ordering >= $1bn in climate damages** — A court of final instance (highest domestic court, or a binding international tribunal) issues a non-appealable judgment ordering a state or a company to pay at least US$1 billion in damages, compensation, or a compliance fund specifically for climate change harms.
- **Global mean methane annual growth rate falls to zero or below** — NOAA GML reports a global mean CH4 annual increase of 0.0 ppb or less for a calendar year in its published trends series.
- **VEI 6+ volcanic eruption with measurable global cooling** — A volcanic eruption of VEI 6 or greater (Smithsonian GVP classification) injects sufficient stratospheric sulphate that WMO, NASA GISS or Copernicus attributes at least 0.1C of global mean cooling to it in the following one to two years.
- **State-backed solar radiation management deployment announced or conducted** — A national government formally announces a stratospheric aerosol injection deployment programme (as distinct from research), or a state or state-backed entity conducts SAI at a scale exceeding 0.1 Tg of injected aerosol precursor per year, as confirmed by independent monitoring or official statement.
- **AMOC declared to have crossed a tipping point** — A major assessment body (IPCC, WMO, or a National Academies-equivalent) or a strong majority of the published AMOC literature states that the AMOC has crossed a critical threshold and is on an irreversible trajectory toward collapse (maximum strength below 5 Sv) under current forcing.
- **Arctic Ocean practically ice-free (extent below 1.0 million km2)** — NSIDC daily sea ice extent for the Arctic falls below 1.0 million km2 on at least one day.

</details>

### Israel, the Levant & the Red Sea

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| New round of major direct Israel-Iran exchange | 52% | 76% | 83% | [61%–97%] | 7 | 2027Q3 |
| Sustained Bab el-Mandeb / Red Sea shipping disruption | 55% | 72% | 79% | [54%–97%] | 6 | 2027Q2 |
| Resumption of major Israeli hostilities in Gaza | 30% | 58% | 70% | [43%–94%] | 5 | 2028Q3 |
| Full Israel-Saudi normalisation | 15% | 43% | 55% | [30%–80%] | 6 | 2029Q3 |
| Israel-Syria security agreement signed | 35% | 54% | 61% | [34%–87%] | 5 | 2027Q4 |
| New major Israel-Hezbollah war round | 22% | 48% | 60% | [32%–87%] | 5 | 2028Q4 |
| Major intra-Palestinian armed conflict | 33% | 57% | 65% | [38%–89%] | 4 | 2027Q4 |
| US suspension of a major arms category to Israel | 8.1% | 28% | 40% | [18%–67%] | 6 | 2030Q2 |
| New IPC Famine classification in Gaza | 14% | 30% | 37% | [17%–62%] | 5 | 2029Q1 |
| Adverse ICJ merits ruling on the Genocide Convention | 1.9% | 18% | 37% | [9.8%–77%] | 5 | 2032Q1 |
| De jure Israeli annexation of West Bank territory | 8.1% | 21% | 29% | [13%–52%] | 6 | 2029Q4 |
| Gaza peace-plan phase 2 substantively implemented | 12% | 33% | 43% | [12%–85%] | 4 | 2029Q3 |
| Functional collapse of the Palestinian Authority | 7.9% | 24% | 33% | [15%–56%] | 5 | 2030Q1 |
| Israeli constitutional crisis over defiance of the High Court | 19% | 33% | 40% | [19%–67%] | 4 | 2028Q2 |
| Ten billion dollars of Gaza reconstruction actually disbursed | 4.0% | 24% | 39% | [10%–79%] | 4 | 2030Q4 |
| Third-Intifada-scale violence in the West Bank | 6.7% | 21% | 30% | [13%–52%] | 5 | 2030Q2 |
| Direct Israel-Turkey military clash | 6.0% | 15% | 20% | [4.2%–49%] | 6 | 2029Q3 |
| Mass permanent departure of Gazans | 4.9% | 14% | 19% | [4.2%–45%] | 6 | 2029Q4 |
| Israel-Lebanon peace treaty with diplomatic relations | 3.9% | 15% | 22% | [4.9%–51%] | 5 | 2030Q4 |
| Hezbollah disarmament certified complete | 7.9% | 19% | 26% | [6.0%–60%] | 4 | 2029Q4 |
| Rupture of the Egyptian or Jordanian peace treaty | 4.1% | 12% | 17% | [6.9%–32%] | 6 | 2030Q2 |
| Israel abandons nuclear opacity | 1.1% | 3.0% | 5.0% | [1.5%–11%] | 8 | 2031Q1 |

<details><summary>Resolution criteria</summary>

- **New round of major direct Israel-Iran exchange** — After 1 Jan 2027, any 30-day window containing ≥50 Iranian missiles or one-way drones launched at Israeli territory, or ≥50 Israeli strike sorties against targets on Iranian territory.
- **Sustained Bab el-Mandeb / Red Sea shipping disruption** — Monthly transit volumes through Bab el-Mandeb fall ≥50% below the 2023 monthly average for ≥90 consecutive days after 1 Aug 2026, per IMF PortWatch or Lloyd's List Intelligence.
- **Resumption of major Israeli hostilities in Gaza** — After 1 Aug 2026, either (a) ≥1,000 Palestinian fatalities recorded in Gaza in any rolling 90-day window (Gaza MoH or OCHA), or (b) Israeli ground forces advance beyond the yellow line and hold new territory in ≥2 Gaza governorates for ≥14 consecutive days.
- **Full Israel-Saudi normalisation** — Saudi Arabia and Israel establish full diplomatic relations (ambassadors accredited or embassies opened), or Saudi Arabia signs an accession instrument to the Abraham Accords.
- **Israel-Syria security agreement signed** — Israel and Syria sign a publicly acknowledged written security or non-belligerency agreement that includes Israeli withdrawal from at least part of the positions taken after December 2024.
- **New major Israel-Hezbollah war round** — After a ≥180-day lull, ≥500 fatalities in Lebanon from Israeli military operations within any 90-day window, or an Israeli ground advance north of the Litani held ≥14 days.
- **Major intra-Palestinian armed conflict** — ≥100 Palestinian fatalities from fighting between Palestinian factions, clans or ISF-aligned militias (Gaza or West Bank) within any rolling 12-month window, per ACLED.
- **US suspension of a major arms category to Israel** — The US government publicly suspends, withholds or blocks delivery of a major weapons category or an approved FMS package to Israel for ≥90 continuous days, acknowledged by the administration or confirmed by congressional notification.
- **New IPC Famine classification in Gaza** — The IPC (or its Famine Review Committee) classifies any Gaza governorate in Phase 5 Famine at any point after 1 Aug 2026.
- **Adverse ICJ merits ruling on the Genocide Convention** — The ICJ issues a final judgment on the merits in South Africa v. Israel finding Israel in breach of one or more obligations under the Genocide Convention.
- **De jure Israeli annexation of West Bank territory** — The Knesset enacts in third reading, and the government brings into force, legislation applying Israeli sovereignty, law and administration to territory in the West Bank beyond the 1967 East Jerusalem municipal boundary.
- **Gaza peace-plan phase 2 substantively implemented** — By the horizon date, ≥5,000 ISF personnel deployed inside Gaza simultaneously AND the Board of Peace or ISF command publicly certifies that decommissioning of Hamas heavy weapons (crew-served and above) has begun.
- **Functional collapse of the Palestinian Authority** — The PA either formally dissolves, or fails to pay ≥2 consecutive months of civil-service salaries while losing effective security control of ≥2 governorate capitals to non-PA armed actors, sustained ≥90 days.
- **Israeli constitutional crisis over defiance of the High Court** — The Israeli government formally announces non-compliance with a binding High Court of Justice ruling, or removes the Attorney General or a Supreme Court justice in defiance of a court injunction, with the non-compliance persisting ≥60 days.
- **Ten billion dollars of Gaza reconstruction actually disbursed** — Cumulative external reconstruction and recovery financing disbursed (not pledged) for Gaza reaches US$10bn in 2026 dollars, per World Bank, Board of Peace or Palestine Donor Group reporting.
- **Third-Intifada-scale violence in the West Bank** — ≥1,000 combined Israeli and Palestinian conflict fatalities in the West Bank, East Jerusalem and inside Israel from Israeli-Palestinian violence (excluding Gaza operations and state-on-state missile exchanges) within any rolling 12-month window, per ACLED or OCHA.
- **Direct Israel-Turkey military clash** — A kinetic engagement between Turkish and Israeli state forces (including strikes on the other's forces, aircraft, vessels or territory) causing ≥1 death or ≥1 aircraft or vessel loss, acknowledged by either government or confirmed by ≥2 major wire services.
- **Mass permanent departure of Gazans** — UN, IOM or receiving-state records show ≥100,000 people who resided in Gaza in 2023 living outside Gaza and the West Bank for ≥12 continuous months.
- **Israel-Lebanon peace treaty with diplomatic relations** — Israel and Lebanon sign, and both ratify or bring into force, a treaty establishing diplomatic relations (embassies or accredited ambassadors), going beyond the June 2026 security framework.
- **Hezbollah disarmament certified complete** — The Lebanese government declares completion of disarmament of all non-state armed groups nationwide AND the United States or the UN Security Council formally endorses that assessment.
- **Rupture of the Egyptian or Jordanian peace treaty** — Egypt or Jordan formally suspends, abrogates or declares void its peace treaty with Israel, or severs diplomatic relations with the Israeli mission closed for ≥12 continuous months.
- **Israel abandons nuclear opacity** — The Israeli government officially acknowledges possession of nuclear weapons, or a nuclear explosive test is attributed to Israel by the CTBTO or by ≥2 of the P5.

</details>

### Demography & migration

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China annual births fall below 7.0 million | 45% | 96% | 97% | [91%–>99%] | 6 | 2028Q1 |
| China's officially reported population falls below 1.400 billion | 58% | 96% | 98% | [93%–>99%] | 5 | 2027Q3 |
| Best-available global TFR estimate falls below 2.1 | 3.3% | 30% | 60% | [22%–97%] | 7 | 2031Q4 |
| Next UN WPP revision moves peak world population below 10.0 billion or earlier than 2070 | 23% | 62% | 84% | [48%–>99%] | 5 | 2029Q2 |
| PISA 2025 shows no recovery in OECD-average mathematics | 68% | 68% | 68% | [40%–91%] | 6 | 2026Q4 |
| Japan annual births (Japanese nationals) fall below 600,000 | 40% | 93% | 96% | [84%–>99%] | 4 | 2028Q1 |
| India publishes provisional Census 2027 population totals | 55% | 92% | 95% | [82%–>99%] | 4 | 2027Q3 |
| India enacts reapportionment of Lok Sabha seats on post-2026 census population | 10% | 33% | 54% | [18%–93%] | 7 | 2030Q3 |
| US total fertility rate falls below 1.50 | 4.0% | 46% | 75% | [48%–96%] | 5 | 2030Q4 |
| US removals plus returns exceed one million in a fiscal year | 13% | 40% | 62% | [25%–97%] | 6 | 2030Q2 |
| Two million or more Ukrainian refugees return to Ukraine | 15% | 46% | 68% | [27%–99%] | 5 | 2030Q1 |
| US life expectancy at birth reaches 80.0 years | 18% | 55% | 83% | [39%–>99%] | 4 | 2029Q4 |
| Global forced displacement exceeds 130 million | 11% | 33% | 55% | [27%–82%] | 6 | 2030Q4 |
| US Census Bureau officially reports negative net international migration | 23% | 44% | 54% | [16%–93%] | 6 | 2028Q3 |
| Remittances to low- and middle-income countries fall 10% or more year-on-year | 8.9% | 28% | 47% | [14%–88%] | 6 | 2030Q4 |
| EU return hubs operationalized at scale | 12% | 32% | 47% | [14%–90%] | 5 | 2030Q1 |
| Global life expectancy falls by 0.5 years or more in a single year | 4.6% | 16% | 28% | [6.7%–64%] | 8 | 2031Q2 |
| Youth-led protests topple three or more Sub-Saharan African governments in a three-year window | 6.0% | 30% | 44% | [13%–83%] | 5 | 2030Q2 |
| A G7 country cuts permanent immigration by three quarters | 4.2% | 24% | 30% | [3.6%–72%] | 7 | 2029Q3 |
| Nigeria completes a national census and the result diverges more than 10% from the prior UN estimate | 5.8% | 20% | 34% | [8.5%–74%] | 6 | 2031Q1 |
| Gulf Cooperation Council migrant worker stock falls 15% or more from its peak | 4.0% | 14% | 25% | [5.8%–57%] | 6 | 2031Q2 |
| South Korea total fertility rate reaches 1.00 or above | 3.0% | 21% | 37% | [17%–62%] | 4 | 2031Q2 |
| China's population is revised down by 15 million or more | 2.8% | 16% | 24% | [5.8%–55%] | 6 | 2030Q2 |
| China's direct birth and childcare subsidies reach 0.5% of GDP | 3.0% | 19% | 31% | [7.6%–69%] | 4 | 2031Q1 |

<details><summary>Resolution criteria</summary>

- **China annual births fall below 7.0 million** — China's National Bureau of Statistics reports annual births below 7,000,000 for any calendar year, in its regular January statistical communique or the annual Statistical Yearbook.
- **China's officially reported population falls below 1.400 billion** — NBS reports a year-end national population (mainland, excluding HK/Macau/Taiwan) below 1,400 million.
- **Best-available global TFR estimate falls below 2.1** — A UN DESA World Population Prospects revision (or UN Population Division estimate) reports a global total fertility rate below 2.10 for the then-current year.
- **Next UN WPP revision moves peak world population below 10.0 billion or earlier than 2070** — A UN DESA World Population Prospects revision published after July 2026 reports a medium-variant peak world population below 10,000,000,000, or a medium-variant peak year earlier than 2070.
- **PISA 2025 shows no recovery in OECD-average mathematics** — OECD PISA 2025 results report an OECD-average mathematics score equal to or below the PISA 2022 OECD-average mathematics score (472 points).
- **Japan annual births (Japanese nationals) fall below 600,000** — Japan's MHLW Vital Statistics report annual births to Japanese nationals below 600,000 for any calendar year, in preliminary or final figures.
- **India publishes provisional Census 2027 population totals** — The Registrar General and Census Commissioner of India publishes provisional population totals from Census 2027, covering the population enumeration phase with a reference date of 1 March 2027.
- **India enacts reapportionment of Lok Sabha seats on post-2026 census population** — India enacts a constitutional amendment or Delimitation Act fixing revised Lok Sabha seat allocations across states based on Census 2027 (or later) population figures.
- **US total fertility rate falls below 1.50** — CDC/NCHS reports a US total fertility rate below 1,500 births per 1,000 women (i.e. TFR < 1.50) for any calendar year, provisional or final.
- **US removals plus returns exceed one million in a fiscal year** — DHS Office of Homeland Security Statistics (or ICE/CBP annual reporting) reports combined removals, returns, and expulsions exceeding 1,000,000 for a single fiscal year.
- **Two million or more Ukrainian refugees return to Ukraine** — UNHCR reports cumulative refugee returns to Ukraine of 2,000,000 or more since the reporting baseline, or reports the Ukrainian refugee population in Europe falling by 2,000,000 or more from its peak.
- **US life expectancy at birth reaches 80.0 years** — NCHS reports US period life expectancy at birth of 80.0 years or more for a single calendar year, in final or provisional mortality reports.
- **Global forced displacement exceeds 130 million** — UNHCR Global Trends (or Mid-Year Trends) reports total forcibly displaced persons exceeding 130,000,000 at any reporting date.
- **US Census Bureau officially reports negative net international migration** — A Census Bureau Vintage population estimates release (or an official Census Bureau revision) reports negative net international migration for any 12-month estimating period.
- **Remittances to low- and middle-income countries fall 10% or more year-on-year** — World Bank / KNOMAD reports nominal USD remittance flows to low- and middle-income countries declining 10% or more versus the prior year.
- **EU return hubs operationalized at scale** — At least three EU member states have transferred a cumulative total of 1,000 or more rejected asylum applicants or asylum seekers to designated 'return hubs' or processing centres in non-EU third countries under the Returns Regulation or bilateral arrangements, as documented by the European Commission, EUAA, or a major NGO monitor.
- **Global life expectancy falls by 0.5 years or more in a single year** — UN WPP, IHME GBD, or WHO reports global period life expectancy at birth declining by 0.5 years or more relative to the prior year.
- **Youth-led protests topple three or more Sub-Saharan African governments in a three-year window** — In any rolling 36-month window, heads of state or heads of government in three or more Sub-Saharan African countries resign, are removed, or flee within 90 days of the onset of mass protests that contemporaneous major-outlet reporting characterizes as youth-led or 'Gen Z' protests.
- **A G7 country cuts permanent immigration by three quarters** — A G7 member's official annual permanent-residence/settlement admissions (e.g. US lawful permanent residents, Canada PR admissions, UK settlement grants) fall below 25% of that country's 2024 level for a full fiscal or calendar year, per the responsible national agency.
- **Nigeria completes a national census and the result diverges more than 10% from the prior UN estimate** — Nigeria's National Population Commission publishes national population totals from a census conducted after 2006, and the figure differs by more than 10% from the UN WPP estimate for Nigeria published immediately prior.
- **Gulf Cooperation Council migrant worker stock falls 15% or more from its peak** — UN DESA International Migrant Stock estimates, or combined national labour-force statistics for Saudi Arabia, UAE, Qatar, Kuwait, Oman and Bahrain, show the foreign-born or non-national workforce at least 15% below its post-2020 peak.
- **South Korea total fertility rate reaches 1.00 or above** — Statistics Korea reports an annual total fertility rate of 1.00 or higher for any calendar year.
- **China's population is revised down by 15 million or more** — An official Chinese government source (NBS communique, the 2030 national census, or a published statistical yearbook revision) reports a national population figure at least 15,000,000 below the previously published estimate for a comparable date.
- **China's direct birth and childcare subsidies reach 0.5% of GDP** — Combined central and local government direct cash transfers for childbirth and childcare in China exceed 0.5% of nominal GDP in a single fiscal year, per Ministry of Finance budget documents or credible reporting aggregating central and provincial outlays.

</details>

### Energy systems & critical materials

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China's extraterritorial rare-earth export control regime enters into force | 45% | 76% | 83% | [55%–98%] | 7 | 2027Q4 |
| Strait of Hormuz closed again for 14+ consecutive days | 54% | 61% | 66% | [31%–89%] | 8 | 2027Q2 |
| Qatari LNG force majeure removing 15%+ of global LNG supply for 60+ days | 20% | 55% | 78% | [39%–>99%] | 6 | 2029Q4 |
| Major producing state imposes an export ban or nationalisation on a critical mineral | 16% | 48% | 71% | [30%–>99%] | 6 | 2030Q1 |
| Loss of Russian uranium enrichment and conversion services to Western utilities | 12% | 38% | 60% | [22%–97%] | 7 | 2030Q2 |
| Brent monthly average above $120/bbl | 38% | 57% | 68% | [39%–89%] | 6 | 2027Q4 |
| Grid equipment supply chain forces cancellation or multi-year deferral of major interconnection programmes | 21% | 58% | 81% | [42%–>99%] | 5 | 2029Q3 |
| Severe rare-earth supply cutoff to the US or EU | 27% | 43% | 50% | [17%–84%] | 8 | 2027Q4 |
| China energy-related CO2 emissions decline three consecutive years | 4.9% | 45% | 71% | [31%–99%] | 5 | 2030Q3 |
| EU ETS2 delayed, price-capped or materially diluted | 23% | 62% | 85% | [48%–>99%] | 4 | 2029Q2 |
| US data-center electricity demand growth collapses | 11% | 33% | 53% | [18%–93%] | 6 | 2030Q3 |
| Global oil demand declines year-on-year outside recession or supply shock | 6.7% | 35% | 63% | [25%–97%] | 5 | 2031Q1 |
| Inverter-driven systemic grid collapse in a major OECD system | 8.9% | 30% | 49% | [15%–90%] | 6 | 2030Q4 |
| LME copper exceeds $15,000/tonne | 12% | 38% | 53% | [18%–92%] | 5 | 2029Q4 |
| A Western SMR delivers first commercial grid power | 3.7% | 64% | 87% | [65%–>99%] | 3 | 2030Q1 |
| Firm load shedding in a major US RTO | 17% | 46% | 61% | [36%–87%] | 4 | 2029Q3 |
| European gas price returns to crisis levels | 31% | 42% | 48% | [20%–77%] | 5 | 2027Q3 |
| Global coal demand falls 3%+ below the 2025 level | 6.7% | 46% | 73% | [46%–96%] | 3 | 2030Q3 |
| Lithium carbonate price exceeds $40,000/tonne | 16% | 37% | 45% | [13%–86%] | 4 | 2029Q1 |
| Cyberattack causes a major OECD power outage | 5.5% | 17% | 30% | [7.9%–64%] | 6 | 2031Q1 |
| Brent monthly average below $45/bbl | 9.2% | 33% | 40% | [19%–66%] | 4 | 2029Q2 |
| Annual global solar PV installations exceed 1,000 GW | 5.7% | 40% | 73% | [45%–96%] | 2 | 2031Q2 |
| Nuclear accident rated INES Level 5 or above | 6.4% | 12% | 21% | [8.0%–39%] | 6 | 2030Q3 |
| Coordinated physical attack causes a major OECD outage | 4.1% | 13% | 21% | [4.3%–56%] | 5 | 2030Q4 |
| Global installed water electrolysis capacity reaches 25 GW | 2.0% | 19% | 49% | [23%–77%] | 2 | 2032Q3 |

<details><summary>Resolution criteria</summary>

- **China's extraterritorial rare-earth export control regime enters into force** — The October 2025 expanded rare-earth export control measures (extraterritorial 0.1% de minimis provisions and expanded element list) are in legal force and being applied to licence applications for at least 30 consecutive days, per MOFCOM announcements, at any point before the stated year-end.
- **Strait of Hormuz closed again for 14+ consecutive days** — Commercial tanker transits through the Strait of Hormuz fall below 25% of the 2025 daily average for 14 or more consecutive days, per Lloyd's List / Kpler / IEA Oil Market Report tracking, at any point after 1 Aug 2026.
- **Qatari LNG force majeure removing 15%+ of global LNG supply for 60+ days** — QatarEnergy declares force majeure or otherwise suspends loadings such that Qatari LNG exports fall below 40% of their 2025 monthly average for 60 or more consecutive days, per Kpler/ICIS tracking, at any point after 1 Aug 2026.
- **Major producing state imposes an export ban or nationalisation on a critical mineral** — A country accounting for 20% or more of global mined supply of lithium, cobalt, nickel, copper or rare earths imposes an export ban, export quota cut of 30%+, or nationalisation/forced-equity measure that removes 15% or more of global supply for 3+ months.
- **Loss of Russian uranium enrichment and conversion services to Western utilities** — Rosatom/TENEX deliveries of enrichment (SWU) or conversion services to US and EU utilities fall by more than 70% year-on-year for four or more consecutive quarters, whether by sanction, counter-sanction or contract termination, per Euratom Supply Agency and US DOE/EIA reporting.
- **Brent monthly average above $120/bbl** — The calendar-month average of front-month Brent futures settlements exceeds $120.00/bbl (nominal USD) in any month after 1 Aug 2026, per ICE settlement data.
- **Grid equipment supply chain forces cancellation or multi-year deferral of major interconnection programmes** — A G7 transmission system operator or major US RTO publicly defers or cancels 10 GW or more of already-approved interconnection or transmission capacity, citing large power transformer, HVDC converter or gas turbine unavailability as the stated primary cause.
- **Severe rare-earth supply cutoff to the US or EU** — Chinese exports of NdPr oxide/metal or heavy rare earths (Dy, Tb) to either the United States or the European Union fall by more than 50% year-on-year for three or more consecutive months, per China customs data.
- **China energy-related CO2 emissions decline three consecutive years** — IEA or CREA reports China's energy-related CO2 emissions declining year-on-year in three consecutive calendar years, with the third such year at or before the stated year.
- **EU ETS2 delayed, price-capped or materially diluted** — The EU formally postpones ETS2's start beyond 2027, or amends the directive to impose a binding price ceiling below EUR 60/tCO2, or exempts a whole covered sector (buildings or road transport), before 31 December 2028.
- **US data-center electricity demand growth collapses** — US data-center electricity consumption grows less than 3% year-on-year in any calendar year, or declines, per EIA/LBNL reporting — versus the 15-20%/yr trend.
- **Global oil demand declines year-on-year outside recession or supply shock** — IEA Oil Market Report reports total global oil demand for a calendar year below the preceding calendar year, in a year with positive global real GDP growth above 2% and no Hormuz-class supply disruption. 2026 is excluded from resolution due to the Hormuz shock.
- **Inverter-driven systemic grid collapse in a major OECD system** — A frequency, voltage or oscillation event causes loss of supply to 5 million or more customers for 6 or more hours across a national or multi-national synchronous area in the OECD, with the official investigation identifying inverter-based resource dynamics, insufficient system inertia or protection mis-coordination as a primary or contributing cause.
- **LME copper exceeds $15,000/tonne** — LME 3-month copper settles above $15,000/tonne (nominal USD) on a monthly average basis.
- **A Western SMR delivers first commercial grid power** — A small modular reactor (nameplate under 300 MWe) in an OECD member country, excluding South Korea's existing SMART-class designs, synchronises to the grid and delivers commercial electricity, confirmed by the national regulator or IAEA PRIS.
- **Firm load shedding in a major US RTO** — PJM, ERCOT, MISO or SPP orders involuntary firm load shed (rolling blackouts) affecting 500,000 or more customers during a declared capacity or energy emergency.
- **European gas price returns to crisis levels** — TTF front-month natural gas futures settle above EUR 100/MWh on any trading day.
- **Global coal demand falls 3%+ below the 2025 level** — IEA reports global coal demand (Mt or Mtce) for some calendar year at or before the stated year at least 3% below the reported 2025 level, confirming structural decline rather than noise.
- **Lithium carbonate price exceeds $40,000/tonne** — Battery-grade lithium carbonate, China spot (SMM or Fastmarkets assessment), exceeds $40,000/tonne on a monthly average basis.
- **Cyberattack causes a major OECD power outage** — A cyber intrusion causes loss of electricity supply to 500,000 or more customers for 6 or more hours in an OECD member country, with cyber causation publicly confirmed by the relevant national CERT, regulator or system operator.
- **Brent monthly average below $45/bbl** — The calendar-month average of front-month Brent futures settlements falls below $45.00/bbl (nominal USD) in any month after 1 Aug 2026.
- **Annual global solar PV installations exceed 1,000 GW** — Global solar PV capacity additions in a calendar year exceed 1,000 GWdc, as reported by BNEF, IEA or SolarPower Europe.
- **Nuclear accident rated INES Level 5 or above** — The IAEA International Nuclear Event Scale assigns a rating of Level 5 (accident with wider consequences) or higher to an event at a civil nuclear power reactor or spent fuel facility anywhere in the world.
- **Coordinated physical attack causes a major OECD outage** — A deliberate physical attack (sabotage, arson, gunfire, explosive) causes loss of electricity supply to 500,000 or more customers for 24 or more hours in an OECD member country, confirmed as deliberate by law enforcement.
- **Global installed water electrolysis capacity reaches 25 GW** — IEA Global Hydrogen Review reports cumulative installed and operating water electrolysis capacity worldwide of 25 GW or more.

</details>

### Food, water & agriculture

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| New IPC/CH Famine (Phase 5) classification anywhere | 69% | 93% | 97% | [91%–>99%] | 5 | 2027Q2 |
| Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously | 26% | 61% | 77% | [50%–96%] | 6 | 2029Q1 |
| FAO Food Price Index reaches an all-time high above 160 | 15% | 44% | 71% | [39%–92%] | 6 | 2030Q3 |
| GRFC reports more than 300 million people in acute food insecurity | 18% | 71% | 84% | [58%–98%] | 5 | 2029Q2 |
| New World screwworm or FMD establishes in the US or EU cattle herd | 15% | 45% | 68% | [28%–99%] | 5 | 2030Q1 |
| Thai 5% broken rice benchmark exceeds US$650/tonne | 9.0% | 27% | 48% | [23%–75%] | 7 | 2031Q2 |
| WFP annual contributions fall below US$5 billion | 34% | 56% | 64% | [38%–89%] | 5 | 2027Q4 |
| Cyberattack or physical sabotage halts a top-5 global agri-food processor or a major water utility | 20% | 55% | 78% | [39%–>99%] | 4 | 2029Q3 |
| World Bank monthly urea price exceeds US$800/tonne | 27% | 46% | 61% | [35%–87%] | 5 | 2028Q3 |
| Ukrainian seaborne grain exports fall below 1 Mt in a calendar month | 62% | 75% | 76% | [48%–95%] | 4 | 2027Q1 |
| DAP/phosphate rock price exceeds US$1,000/tonne on a monthly average | 12% | 38% | 60% | [23%–96%] | 5 | 2030Q3 |
| Mississippi River or Panama Canal low-water event materially disrupts US grain exports | 35% | 80% | 96% | [78%–>99%] | 3 | 2028Q3 |
| Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months | 58% | 89% | 95% | [78%–>99%] | 3 | 2027Q3 |
| World cereal production falls 4%+ year-on-year (multi-breadbasket failure) | 11% | 19% | 33% | [15%–61%] | 8 | 2030Q3 |
| India physically curtails Indus western-river flows to Pakistan | 5.6% | 17% | 36% | [18%–59%] | 7 | 2032Q1 |
| World cereal stocks-to-use ratio falls below 28% | 7.0% | 24% | 36% | [17%–59%] | 7 | 2030Q3 |
| FAO declares a desert locust upsurge or plague affecting three or more countries | 13% | 39% | 62% | [23%–97%] | 4 | 2030Q3 |
| Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab | 5.2% | 14% | 25% | [5.7%–59%] | 8 | 2031Q1 |
| Hormuz fertilizer flows normalise (downside-risk-off event) | 58% | 85% | 92% | [75%–>99%] | 2 | 2027Q2 |
| Three or more countries/territories in confirmed IPC Famine simultaneously | 5.7% | 17% | 26% | [6.0%–61%] | 7 | 2030Q4 |
| Colorado River enters 2027 without an agreed post-2026 framework | 34% | 34% | 35% | [16%–64%] | 3 | 2027Q1 |
| Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water | 3.0% | 7.9% | 13% | [5.1%–24%] | 8 | 2030Q4 |

<details><summary>Resolution criteria</summary>

- **New IPC/CH Famine (Phase 5) classification anywhere** — The IPC Famine Review Committee or a CH equivalent confirms Famine (IPC Phase 5) — with reasonable evidence or higher — for at least one geographic area not already so classified as of 2026-07-29, published on ipcinfo.org.
- **Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously** — Per the IFPRI Food and Fertilizer Export Restrictions Tracker, at least two countries each ranking in the global top 10 for wheat, maize or rice exports have in force, simultaneously and for at least 60 consecutive days, a new (post-2026-07-29) export ban or quota estimated to cut that country's exports of the staple by 25% or more.
- **FAO Food Price Index reaches an all-time high above 160** — The FAO Food Price Index (2014-2016=100, nominal) monthly value exceeds 160.0, surpassing the March 2022 record of 160.3.
- **GRFC reports more than 300 million people in acute food insecurity** — Any edition of the Global Report on Food Crises published in 2027-2036 reports more than 300.0 million people in IPC/CH Phase 3 or above for its reference year.
- **New World screwworm or FMD establishes in the US or EU cattle herd** — USDA APHIS, WOAH or the European Commission confirms sustained autochthonous transmission of New World screwworm (Cochliomyia hominivorax) north of the Mexico-US border, or an FMD outbreak in an FMD-free country of the G7, triggering a national movement standstill or export ban of 30+ days.
- **Thai 5% broken rice benchmark exceeds US$650/tonne** — FAO GIEWS / Thai Rice Exporters Association monthly average f.o.b. price for Thai white rice 5% broken exceeds US$650 per tonne.
- **WFP annual contributions fall below US$5 billion** — WFP's published annual contribution total for any calendar year 2026-2036 is below US$5.0 billion (nominal), per wfp.org contributions data.
- **Cyberattack or physical sabotage halts a top-5 global agri-food processor or a major water utility** — A publicly confirmed cyber or sabotage incident forces a 7+ day shutdown of national-scale operations at a top-5 global meat, grain-trading or fertilizer company, or causes a 7+ day loss of service at a water utility serving 1m+ people, per company disclosure, CISA/ENISA advisory or national regulator.
- **World Bank monthly urea price exceeds US$800/tonne** — World Bank Pink Sheet monthly average urea (Middle East, bulk, f.o.b.) exceeds US$800 per tonne in any month.
- **Ukrainian seaborne grain exports fall below 1 Mt in a calendar month** — Ukrainian Ministry of Agrarian Policy or UGA monthly data show total seaborne grain and oilseed exports below 1.0 million tonnes in any single calendar month (normal 2024-26 range ~3-5 Mt/month).
- **DAP/phosphate rock price exceeds US$1,000/tonne on a monthly average** — World Bank Pink Sheet monthly average DAP (f.o.b. US Gulf) exceeds US$1,000 per tonne in any month.
- **Mississippi River or Panama Canal low-water event materially disrupts US grain exports** — USDA Grain Transportation Report or Army Corps data show either (a) Mississippi barge freight rates above 800% of tariff benchmark, or draft/tow restrictions in force on the Lower Mississippi, for 30+ consecutive days, or (b) Panama Canal transit slots cut 30%+ below normal for 60+ consecutive days.
- **Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months** — USDA, Eurostat, WOAH or the national statistical agency of a G20 member reports a decline of 10% or more, within any rolling 12-month window, in national laying-hen inventory or national pig inventory, attributed principally to an animal disease epizootic (HPAI, ASF, FMD or successor).
- **World cereal production falls 4%+ year-on-year (multi-breadbasket failure)** — FAO's Cereal Supply and Demand Brief reports world cereal production for a calendar year at least 4.0% below the prior year's outturn (using FAO's own revised series at the time of the following year's July brief).
- **India physically curtails Indus western-river flows to Pakistan** — Pakistan's IRSA rim-station data, corroborated by satellite/independent hydrological analysis, show a sustained reduction of 20% or more over at least four consecutive weeks in Chenab or Jhelum inflows attributable to Indian storage operations or diversion, and not to natural hydrology.
- **World cereal stocks-to-use ratio falls below 28%** — FAO's Cereal Supply and Demand Brief reports a world cereal stocks-to-use ratio below 28.0% for any marketing year.
- **FAO declares a desert locust upsurge or plague affecting three or more countries** — FAO Desert Locust Watch raises the situation to 'Upsurge' or 'Plague' with swarms reported in three or more countries simultaneously for 60+ days.
- **Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab** — CIMMYT, BGRI, FAO or a national plant protection agency confirms establishment of a Ug99-lineage stem rust race, a novel highly virulent stripe rust race defeating deployed resistance, or wheat blast (Magnaporthe oryzae Triticum), in Indian or Pakistani Punjab or Haryana, with documented field-scale infection.
- **Hormuz fertilizer flows normalise (downside-risk-off event)** — World Bank or IFA data show Middle East seaborne urea and ammonia export volumes recovering to 90% or more of their 2024-25 monthly average for three consecutive months.
- **Three or more countries/territories in confirmed IPC Famine simultaneously** — At any point in a calendar year, IPC/FRC-confirmed Famine (Phase 5) classifications are simultaneously in force for areas in three or more distinct countries or territories.
- **Colorado River enters 2027 without an agreed post-2026 framework** — On 1 January 2027, no seven-state consensus agreement and no signed federal Record of Decision governs Lake Powell/Lake Mead operations for calendar 2027, with operations instead running under an interim stopgap, unilateral federal action, or litigation.
- **Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water** — ACLED or equivalent records a state-attributed kinetic attack (air, missile, drone or special-forces) on the Grand Ethiopian Renaissance Dam or associated Ethiopian water infrastructure, or a direct armed exchange between Egyptian and Ethiopian forces publicly framed by either government as arising from the Nile water dispute.

</details>

### Pandemics, biosecurity & global health

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| PEPFAR terminated, absorbed, or cut by more than half from its FY2024 level | 15% | 45% | 68% | [28%–99%] | 7 | 2030Q1 |
| Multiple US states abolish or gut school-entry vaccine mandates | 19% | 55% | 79% | [41%–>99%] | 6 | 2029Q4 |
| US federal government de-recommends a core routine childhood vaccine and the change survives | 39% | 58% | 63% | [26%–95%] | 6 | 2027Q3 |
| Cholera resurgence with oral cholera vaccine stockpile failure | 17% | 50% | 73% | [33%–>99%] | 5 | 2029Q4 |
| United States formally loses measles elimination status | 80% | 88% | 90% | [72%–>99%] | 4 | 2026Q4 |
| A single US influenza season with at least 50,000 estimated deaths | 15% | 45% | 68% | [28%–99%] | 5 | 2030Q1 |
| Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin | 11% | 33% | 46% | [12%–85%] | 7 | 2029Q4 |
| Large autochthonous arbovirus transmission in continental Europe or the continental US | 19% | 55% | 79% | [41%–>99%] | 4 | 2029Q4 |
| Two consecutive years of rising global new HIV infections | 1.8% | 42% | 50% | [16%–89%] | 6 | 2029Q4 |
| WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency | 55% | 94% | 99% | [95%–>99%] | 3 | 2027Q4 |
| WHO declares an influenza pandemic (any subtype) | 6.6% | 21% | 35% | [18%–55%] | 8 | 2031Q1 |
| Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases | 41% | 44% | 44% | [14%–82%] | 6 | 2027Q1 |
| A newly emerged pathogen causes at least 1 million cumulative deaths worldwide | 2.0% | 12% | 26% | [7.1%–53%] | 10 | 2032Q2 |
| PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly | 52% | 80% | 86% | [62%–99%] | 3 | 2027Q3 |
| WHO Pandemic Agreement enters into force | 2.0% | 52% | 76% | [50%–96%] | 3 | 2030Q2 |
| Paralytic poliomyelitis from circulating vaccine-derived poliovirus in a high-income country | 11% | 36% | 56% | [19%–95%] | 4 | 2030Q3 |
| US reports at least 5,000 confirmed measles cases in a single calendar year | 18% | 58% | 72% | [41%–94%] | 3 | 2029Q2 |
| Sustained human-to-human transmission of an H5 influenza virus | 3.1% | 10% | 21% | [8.7%–39%] | 9 | 2031Q4 |
| United States formally rejoins the World Health Organization | 1.1% | 27% | 41% | [17%–68%] | 4 | 2030Q3 |
| Global interruption of wild poliovirus type 1 transmission | 3.0% | 25% | 46% | [22%–74%] | 3 | 2031Q3 |
| Deliberate biological attack causes at least 10 confirmed human deaths | 2.2% | 5.3% | 10% | [1.8%–25%] | 8 | 2031Q3 |
| Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution | 2.1% | 6.2% | 11% | [1.8%–29%] | 7 | 2031Q2 |
| Ebola causes a confirmed secondary transmission chain outside Africa | 6.7% | 12% | 18% | [6.6%–40%] | 4 | 2029Q3 |
| WHO declares a global emergency over an antimicrobial-resistant pathogen | 1.1% | 4.1% | 8.1% | [2.8%–15%] | 5 | 2031Q4 |

<details><summary>Resolution criteria</summary>

- **PEPFAR terminated, absorbed, or cut by more than half from its FY2024 level** — US enacted appropriations or a binding reorganization reduce dedicated PEPFAR/global HIV bilateral funding below 50% of the FY2024 enacted level for a full fiscal year, or the programme is formally dissolved into a successor account with no ring-fenced HIV line.
- **Multiple US states abolish or gut school-entry vaccine mandates** — At least five US states have, via statute or binding regulation in effect, eliminated school-entry immunization requirements for one or more core antigens, or adopted universal opt-out (any-reason philosophical exemption granted on request without documentation), at any point in the window.
- **US federal government de-recommends a core routine childhood vaccine and the change survives** — CDC's published child and adolescent immunization schedule removes a currently universally-recommended antigen (MMR, DTaP, IPV, Hib, PCV, rotavirus, varicella, or the hepatitis B birth dose) from universal recommendation - moving it to shared clinical decision-making, risk-based, or off-schedule - and that change is in effect and not judicially stayed for at least 6 continuous months.
- **Cholera resurgence with oral cholera vaccine stockpile failure** — WHO reports at least 6,000 cholera deaths globally in a single calendar year, or formally announces that the global OCV stockpile has been unable to meet the single-dose emergency standard for a continuous period of 12 months or more.
- **United States formally loses measles elimination status** — PAHO's Regional Verification Commission (or WHO) formally announces that the United States no longer meets measles elimination criteria, or the US government/CDC publicly acknowledges loss of elimination status.
- **A single US influenza season with at least 50,000 estimated deaths** — CDC in-season or final burden estimates put deaths from seasonal influenza at 50,000 or more for a single season within the window.
- **Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin** — A national government, law enforcement agency, or frontier AI developer publicly confirms a specific incident in which AI systems materially assisted a person or group in designing, acquiring, or synthesizing a pathogen or toxin of biosecurity concern (beyond generic capability-evaluation results or red-team exercises).
- **Large autochthonous arbovirus transmission in continental Europe or the continental US** — At least 1,000 locally acquired cases of dengue, chikungunya or Oropouche virus disease reported in a single calendar year in continental Europe or the continental United States (excluding territories such as Puerto Rico).
- **Two consecutive years of rising global new HIV infections** — UNAIDS reports annual new HIV infections higher than the preceding year in two consecutive reporting years, reversing the multi-decade decline.
- **WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency** — WHO's Director-General determines a new Public Health Emergency of International Concern (or pandemic emergency under the amended IHR) for an event distinct from the standing polio PHEIC and the Ebola Bundibugyo PHEIC declared 17 May 2026, at any point in the window.
- **WHO declares an influenza pandemic (any subtype)** — WHO formally declares an influenza pandemic, or declares a PHEIC/pandemic emergency for a novel influenza A virus with confirmed sustained community-level human-to-human transmission in at least two WHO regions.
- **Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases** — WHO/AFRO situation reports for the outbreak declared 15 May 2026 (or its recognized continuation) record at least 10,000 cumulative laboratory-confirmed cases across all affected countries.
- **A newly emerged pathogen causes at least 1 million cumulative deaths worldwide** — A pathogen not endemically circulating in humans as of 1 Jan 2026 is credibly estimated by WHO, IHME, or a peer-reviewed consensus source to have caused at least 1,000,000 cumulative human deaths (reported or excess) within the stated horizon.
- **PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly** — A World Health Assembly (regular or special session) formally adopts the Pathogen Access and Benefit-Sharing annex to the WHO Pandemic Agreement.
- **WHO Pandemic Agreement enters into force** — The 60th instrument of ratification, acceptance, approval or accession to the WHO Pandemic Agreement is deposited, bringing the Agreement into force.
- **Paralytic poliomyelitis from circulating vaccine-derived poliovirus in a high-income country** — A national health authority in a World Bank high-income country confirms at least one case of paralytic poliomyelitis caused by circulating vaccine-derived poliovirus (any type) with onset within the window.
- **US reports at least 5,000 confirmed measles cases in a single calendar year** — CDC's official measles surveillance reports at least 5,000 confirmed cases for any single calendar year within the window.
- **Sustained human-to-human transmission of an H5 influenza virus** — WHO or a national health authority publicly confirms an H5 (any neuraminidase) influenza cluster with at least three sequential generations of human-to-human transmission, or a cluster of at least 10 epidemiologically linked human cases with no plausible animal or environmental exposure for the majority.
- **United States formally rejoins the World Health Organization** — The United States formally notifies WHO of resumption of membership, or deposits an instrument of acceptance of the WHO Constitution, and pays or commits to assessed contributions.
- **Global interruption of wild poliovirus type 1 transmission** — Zero wild poliovirus type 1 cases with onset in any 12 consecutive calendar months, per GPEI reporting, with the 12-month window closing inside the horizon.
- **Deliberate biological attack causes at least 10 confirmed human deaths** — A government or international body attributes at least 10 human deaths to a deliberate release of a biological agent (state or non-state actor) in a single incident or campaign.
- **Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution** — A national health authority, WHO, or an official government investigation publicly attributes an outbreak of at least 50 laboratory-confirmed human infections to a laboratory-acquired infection or a containment/biosafety breach.
- **Ebola causes a confirmed secondary transmission chain outside Africa** — A national health authority in a country outside the WHO African Region confirms at least one locally acquired Ebola (any species) infection in a person who was not infected in Africa, at any point in the window.
- **WHO declares a global emergency over an antimicrobial-resistant pathogen** — WHO declares a PHEIC, pandemic emergency, or equivalent formal global health emergency whose primary basis is an antimicrobial-resistant bacterial or fungal pathogen (for example pan-resistant Klebsiella, XDR typhoid, Candida auris, or drug-resistant gonorrhoea).

</details>

## How bad decades begin

Among paths where at least three high-severity events fired, these are the most common opening sequences, in order of occurrence.

| Frequency | First | Then | Then |
|---:|---|---|---|
| 1.3% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics |
| 0.9% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China annual births fall below 7.0 million |
| 0.6% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | US Census Bureau officially reports negative net international migration |
| 0.6% | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million |
| 0.5% | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |
| 0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China reports annual real GDP growth below 4.0% |
| <0.5% | Nvidia suffers a ≥50% peak-to-trough drawdown | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | A top-4 US hyperscaler guides annual capex down year-over-year |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | Nvidia suffers a ≥50% peak-to-trough drawdown |
| <0.5% | China annual births fall below 7.0 million | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption |
| <0.5% | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |

The most common opening — Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window → China annual births fall below 7.0 million → PISA 2025 shows no recovery in OECD-average mathematics — accounts for 1.3% of all paths. No single sequence dominates, which is itself informative: the model does not support a story in which one specific trigger reliably starts the cascade. What recurs is the *pattern* — a shock in one domain degrading the capacity to absorb the next.

## Where the correlations are

The clearest way to read a dependency is the contrast between P(A given B) and P(A given not-B) — how much learning one event would move your estimate of the other. Ranked by odds ratio rather than by lift, because lift is mechanically capped by the base rates: two events at 80% each cannot show a lift above 1.25 however tightly coupled they are, so ranking high-probability nodes by lift returns a table of 1.0× entries and hides every real dependency. This is the part of the model a spreadsheet of independent probabilities cannot produce, and it is where tail risk lives.

| Event A | Event B | P(A given B) | P(A given not-B) | Odds ratio |
|---|---|---:|---:|---:|
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | New round of major direct Israel-Iran exchange | **87%** | 39% | 10.7× |
| Nvidia suffers a ≥50% peak-to-trough drawdown | A top-4 US hyperscaler guides annual capex down year-over-year | **91%** | 52% | 8.7× |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **81%** | 48% | 4.6× |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | **83%** | 54% | 4.2× |
| US recession with NBER-dated peak in the window | Global recession (world real GDP growth below 2.0% in a calendar year) | **91%** | 70% | 4.1× |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | A single training run of ≥1e28 FLOP is publicly reported | **80%** | 56% | 3.2× |
| FAO Food Price Index reaches an all-time high above 160 | GRFC reports more than 300 million people in acute food insecurity | **74%** | 51% | 2.8× |
| US unemployment rate ≥6.0% for three consecutive months | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **85%** | 67% | 2.7× |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **77%** | 61% | 2.2× |
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Long-term (multi-decadal) 1.5C breach formally declared | **98%** | 97% | 2.0× |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | A single training run of ≥1e28 FLOP is publicly reported | **77%** | 64% | 1.9× |
| Japan 10-year government bond yield reaches 3.00% | Nvidia suffers a ≥50% peak-to-trough drawdown | **92%** | 86% | 1.9× |
| A single training run of ≥1e28 FLOP is publicly reported | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **84%** | 74% | 1.9× |
| US recession with NBER-dated peak in the window | A top-4 US hyperscaler guides annual capex down year-over-year | **85%** | 75% | 1.9× |
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | New IPC/CH Famine (Phase 5) classification anywhere | **98%** | 97% | 1.7× |
| Japan 10-year government bond yield reaches 3.00% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | **91%** | 86% | 1.7× |
| Sustained Bab el-Mandeb / Red Sea shipping disruption | FAO Food Price Index reaches an all-time high above 160 | **82%** | 73% | 1.7× |
| Japan 10-year government bond yield reaches 3.00% | China's extraterritorial rare-earth export control regime enters into force | **92%** | 87% | 1.6× |

## Continuous indicators

These evolve on a Gaussian copula driven by each path's own systemic-stress index, so the bad tails of these distributions are populated by the same paths that fired the bad events — not by independent noise.

| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |
|---|---:|:---:|:---:|
| World military expenditure as share of global GDP (percent of global GDP) | 2.5 | 2.6 / **2.9** / 3.25 | 2.71 / **3.12** / 3.6 |
| Global state-based armed conflict battle deaths per year (thousands of deaths per year) | 160 | 54.8 / **130** / 245 | 10.1 / **114** / 272 |
| Brent crude oil price (USD per barrel (annual average)) | 86 | 45.2 / **72.2** / 140 | 27 / **64.4** / 159 |
| US military expenditure as share of US GDP (percent of GDP) | 3.2 | 2.95 / **3.3** / 3.7 | 2.87 / **3.35** / 3.9 |
| European NATO members' aggregate defence spending as share of GDP (percent of GDP) | 2.65 | 3 / **3.35** / 3.75 | 3.25 / **3.73** / 4.29 |
| PLA aircraft sorties entering Taiwan's ADIZ per year (sorties per year) | 3600 | 2.4e+03 / **5e+03** / 7.81e+03 | 2.18e+03 / **5.77e+03** / 9.63e+03 |
| US dollar share of allocated global FX reserves (percent) | 58 | 51 / **54** / 57 | 47.7 / **51.8** / 56 |
| Weekly container-ship transits of the Suez Canal (transits per week) | 30 | 22 / **62** / 87.9 | 24.2 / **79.4** / 116 |
| Combined US + Russia deployed strategic nuclear warheads (warheads) | 3200 | 3.15e+03 / **3.72e+03** / 4.35e+03 | 3.22e+03 / **4.01e+03** / 4.88e+03 |
| Net monthly Russian territorial gain in Ukraine (km2 per month (negative = Ukrainian recapture)) | 104 | -30 / **7.78** / 175 | -97.4 / **-44.5** / 184 |
| Number of active state-based armed conflicts (>=25 battle deaths/year) (count) | 61 | 47.9 / **58** / 68 | 42.6 / **56.4** / 70.2 |
| Crude and condensate transiting the Strait of Hormuz (million barrels per day) | 8 | 5 / **18** / 21 | 5.51 / **23.4** / 27.6 |
| Annual global mean surface temperature anomaly (ERA5, vs 1850-1900) (C) | 1.47 | 1.48 / **1.62** / 1.78 | 1.51 / **1.7** / 1.92 |
| Annual mean CO2 concentration at Mauna Loa (ppm) | 429.4 | 440 / **442** / 445 | 446 / **449** / 453 |
| NOAA global mean atmospheric methane (ppb) | 1945 | 1.97e+03 / **1.98e+03** / 2e+03 | 1.98e+03 / **2e+03** / 2.02e+03 |
| Global fossil CO2 emissions (Global Carbon Project) (GtCO2/yr) | 38.1 | 35.6 / **38.3** / 40.1 | 34.7 / **38.4** / 40.9 |
| Global mean sea level (satellite altimetry, above 1993 baseline) (mm) | 112 | 132 / **138** / 144 | 144 / **152** / 160 |
| Arctic sea ice September minimum extent (NSIDC) (million km2) | 4.3 | 3.35 / **3.98** / 4.55 | 2.94 / **3.8** / 4.59 |
| Annual maximum 3-month ONI (Nino3.4) (C) | 2.4 | -0.896 / **0.402** / 1.7 | -2.49 / **-0.698** / 1.1 |
| Share of global reef area under Alert Level 1+ heat stress, rolling 12 months (% of global reef area) | 55 | 32.1 / **61.9** / 88 | 24.5 / **65.7** / 101 |
| Brazilian Legal Amazon annual deforestation (INPE PRODES) (km2/yr) | 5796 | 3.11e+03 / **4.92e+03** / 9.79e+03 | 1.91e+03 / **4.41e+03** / 1.12e+04 |
| FAO Food Price Index (nominal) (index, 2014-2016 = 100) | 130.3 | 121 / **140** / 167 | 119 / **145** / 183 |
| Annual increase in global 0-2000m ocean heat content (ZJ/yr) | 23 | 13 / **25** / 37 | 9.61 / **26** / 42.6 |
| Brent crude oil price (USD per barrel) | 84 | 41.8 / **78.3** / 150 | 24.8 / **74.6** / 174 |
| US 10-year Treasury yield (percent) | 4.62 | 3.09 / **4.8** / 6.3 | 2.54 / **4.9** / 6.98 |
| US CPI inflation, year over year (percent) | 3.5 | 1.2 / **2.6** / 4.9 | 0.184 / **2.11** / 5.3 |
| Federal funds target rate, upper bound (percent) | 3.75 | 1.74 / **3.49** / 5.25 | 0.951 / **3.37** / 5.78 |
| S&P 500 index level (index points) | 7412 | 6.08e+03 / **9.99e+03** / 1.6e+04 | 6.02e+03 / **1.14e+04** / 1.97e+04 |
| Global real GDP growth (percent per year) | 3 | 1.6 / **3.2** / 4.2 | 1.1 / **3.31** / 4.69 |
| China reported real GDP growth (percent per year) | 4.6 | 1.9 / **3.4** / 4.8 | 0.666 / **2.75** / 4.68 |
| US federal debt held by the public / GDP (percent) | 100 | 106 / **111** / 119 | 110 / **117** / 128 |
| USD share of allocated FX reserves (IMF COFER) (percent) | 56.5 | 47 / **52** / 57 | 42.6 / **49.6** / 56.5 |
| Gold price (USD per troy ounce) | 4040 | 3.1e+03 / **4.7e+03** / 7.3e+03 | 2.87e+03 / **5.07e+03** / 8.68e+03 |
| USD/JPY exchange rate (yen per dollar) | 163.6 | 118 / **152** / 193 | 98.7 / **146** / 202 |
| US average effective tariff rate on all imports (percent) | 6 | 2.97 / **8** / 18 | 2.16 / **9.14** / 22.9 |
| Log10 of training compute for the largest publicly-known training run (log10(FLOP)) | 26.7 | 28 / **28.8** / 29.5 | 28.8 / **29.9** / 30.9 |
| Global data center electricity consumption (TWh per year) | 590 | 831 / **1.03e+03** / 1.35e+03 | 992 / **1.27e+03** / 1.71e+03 |
| Combined annual capex, Microsoft + Alphabet + Amazon + Meta (USD billions per year) | 700 | 470 / **980** / 1.5e+03 | 431 / **1.13e+03** / 1.85e+03 |
| Nvidia annual data center revenue (USD billions per year) | 330 | 232 / **541** / 869 | 225 / **654** / 1.11e+03 |
| Combined annualized revenue run-rate, OpenAI + Anthropic (USD billions) | 72 | 165 / **351** / 622 | 247 / **502** / 877 |
| Log2 of METR 50%-reliability task time horizon (log2(hours of human-expert task time)) | 1.6 | 5.4 / **8.1** / 10.8 | 7.89 / **11.6** / 15.4 |
| Log10 of API price for GPT-4-class capability (log10(USD per million input tokens)) | -0.4 | -2.2 / **-1.8** / -1.4 | -3.11 / **-2.56** / -2.01 |
| Chinese open-weight models' share of OpenRouter tokens (percent) | 61 | 32 / **60** / 82.9 | 20.7 / **59.3** / 91.2 |
| Log10 of US paid fully-driverless rides per week (millions) (log10(millions of rides per week)) | -0.3 | 0.201 / **0.898** / 1.4 | 0.589 / **1.55** / 2.25 |
| US AI adoption in production, employment-weighted (Census BTOS) (percent of employment at AI-using firms) | 32 | 45 / **56** / 68 | 53.9 / **69.1** / 85.7 |
| Global total fertility rate (births per woman) | 2.23 | 2.03 / **2.12** / 2.21 | 1.94 / **2.06** / 2.18 |
| China annual births (million births per year) | 7.92 | 4.6 / **5.9** / 7.39 | 3 / **4.8** / 6.87 |
| US total fertility rate (births per woman) | 1.585 | 1.44 / **1.51** / 1.59 | 1.37 / **1.47** / 1.58 |
| Global forcibly displaced persons (million people) | 117.8 | 103 / **120** / 140 | 97.7 / **121** / 149 |
| US net international migration (thousand persons per year) | 320 | -151 / **622** / 1.4e+03 | -275 / **785** / 1.86e+03 |
| EU+ annual asylum applications (thousand applications per year) | 822 | 318 / **700** / 1.35e+03 | 107 / **633** / 1.53e+03 |
| India total fertility rate (births per woman) | 1.9 | 1.62 / **1.73** / 1.83 | 1.48 / **1.64** / 1.77 |
| World population (billion people) | 8.3 | 8.57 / **8.63** / 8.69 | 8.73 / **8.81** / 8.89 |
| China population aged 60 and over (percent of total population) | 22.9 | 27.1 / **28** / 28.8 | 29.5 / **30.8** / 31.9 |
| US annual drug overdose deaths (thousand deaths per year) | 70 | 34 / **55.1** / 80 | 17.8 / **47** / 81.3 |
| South Korea total fertility rate (births per woman) | 0.8 | 0.74 / **0.87** / 1 | 0.73 / **0.909** / 1.09 |
| Japan annual births (Japanese nationals) (thousand births per year) | 670 | 464 / **538** / 608 | 364 / **466** / 563 |
| Brent crude oil price (USD/bbl (nominal)) | 73 | 42.1 / **72.1** / 128 | 29.9 / **71.4** / 149 |
| Annual global solar PV capacity additions (GWdc/yr) | 650 | 640 / **879** / 1.18e+03 | 675 / **1.01e+03** / 1.42e+03 |
| Lithium-ion battery pack price (volume-weighted, all segments) (USD/kWh (nominal)) | 105 | 54.9 / **72** / 95 | 30.5 / **54.1** / 85.9 |
| China share of global rare-earth separation and refining (% of global refined output) | 87 | 72 / **79** / 87 | 65 / **74.6** / 85.7 |
| US data center electricity consumption (TWh/yr) | 225 | 320 / **465** / 680 | 395 / **595** / 894 |
| EU average wholesale electricity price (EUR/MWh (nominal)) | 80 | 40.1 / **66.1** / 118 | 22.2 / **58.3** / 130 |
| Global coal demand (Mt/yr) | 8800 | 7.7e+03 / **8.47e+03** / 9.05e+03 | 7.23e+03 / **8.29e+03** / 9.09e+03 |
| Uranium spot price (USD/lb U3O8) | 88 | 55.1 / **105** / 185 | 45.7 / **114** / 225 |
| Global oil (liquids) demand (million b/d) | 104.5 | 102 / **106** / 109 | 102 / **107** / 112 |
| Global LNG liquefaction nameplate capacity (Mtpa) | 510 | 655 / **712** / 755 | 744 / **822** / 882 |
| Global EV share of new light-vehicle sales (% of new sales) | 22.4 | 32 / **40** / 48 | 38.5 / **49.6** / 60.7 |
| Henry Hub natural gas price (USD/MMBtu (nominal)) | 3.7 | 2.48 / **4.2** / 6.98 | 2.12 / **4.47** / 8.33 |
| Cumulative confirmed H5N1-infected US dairy herds (herds) | 1166 | 1.3e+03 / **1.82e+03** / 2.6e+03 | 1.46e+03 / **2.17e+03** / 3.25e+03 |
| Confirmed human H5 (any NA) influenza cases reported globally per year (cases/year) | 14 | 2.93 / **16** / 65.3 | -0.886 / **17.3** / 85.2 |
| US confirmed measles cases per calendar year (cases/year) | 2900 | 896 / **3.8e+03** / 9e+03 | 306 / **4.29e+03** / 1.15e+04 |
| US kindergarten MMR vaccination coverage (% of kindergartners) | 92.5 | 89 / **90.6** / 92.2 | 87.4 / **89.6** / 91.8 |
| Global DTP3 immunization coverage (% of surviving infants) | 85 | 81.8 / **83.9** / 86 | 80.4 / **83.3** / 86.2 |
| Deaths directly attributable to bacterial AMR (million deaths/year) | 1.2 | 1.16 / **1.31** / 1.46 | 1.16 / **1.37** / 1.58 |
| International financing for HIV in low- and middle-income countries (US$ billions/year) | 7.3 | 3.2 / **5.4** / 7.79 | 1.32 / **4.36** / 7.67 |
| US adults currently using GLP-1 drugs for weight loss (% of adults) | 12.4 | 16 / **23** / 31 | 19.1 / **28.8** / 39.8 |
| US adult obesity prevalence (Gallup self-reported) (% of adults) | 36.4 | 31.5 / **33.4** / 35.3 | 29.1 / **31.7** / 34.4 |
| WHO approved base programme budget per biennium (US$ billions/biennium) | 4.2 | 3.4 / **4.1** / 5.1 | 3.08 / **4.04** / 5.42 |
| Global malaria deaths (thousand deaths/year) | 610 | 560 / **635** / 715 | 545 / **649** / 759 |
| CDC full-time federal workforce (thousand FTEs) | 9 | 6.6 / **8.2** / 9.91 | 5.55 / **7.76** / 10.1 |
| US presidential net approval (approve minus disapprove, aggregate) (percentage points) | -19 | -29 / **-10.1** / 5.91 | -31.5 / **-5.11** / 16.9 |
| Number of countries coded as currently autocratizing by V-Dem (countries) | 44 | 37 / **45** / 54 | 34.6 / **45.5** / 58 |
| Countries with net decline in Freedom House score in a given year (countries) | 54 | 40.1 / **51** / 63 | 34.3 / **49.4** / 66 |
| Share of world population living in Freedom House 'Free' countries (percent) | 21 | 15 / **20** / 24 | 12.5 / **19.4** / 25 |
| AfD federal voting intention (percent) | 27 | 19 / **28** / 36 | 16 / **28.5** / 39.6 |
| French RN first-round national vote share (presidential/legislative) (percent) | 35 | 28 / **36** / 44 | 25.5 / **36.6** / 47.6 |
| Reform UK voting intention (percent) | 26 | 14 / **24** / 35 | 9.02 / **22.9** / 38.2 |
| Successful coups d'etat worldwide per calendar year (coups) | 2 | -0.00494 / **2** / 5.01 | -0.756 / **2.03** / 6.12 |
| US terrorism and targeted-violence events per year (START/BDI coding) (events) | 1050 | 716 / **1.23e+03** / 1.78e+03 | 627 / **1.33e+03** / 2.08e+03 |
| Gallup average 'great deal / quite a lot' confidence across nine US institutions (percent) | 27 | 21 / **26** / 31 | 18.5 / **25.4** / 32.4 |
| ACLED-recorded political violence events worldwide per year (events) | 1.85e+05 | 1.5e+05 / **1.97e+05** / 2.48e+05 | 1.39e+05 / **2.04e+05** / 2.74e+05 |
| FAO Food Price Index (nominal) (index, 2014-2016=100) | 130.3 | 112 / **146** / 198 | 107 / **154** / 226 |
| World cereal stocks-to-use ratio (percent) | 32 | 27.8 / **31.2** / 34.6 | 26.1 / **30.8** / 35.5 |
| World cereal production (million tonnes per calendar year) | 2983 | 2.96e+03 / **3.12e+03** / 3.29e+03 | 2.97e+03 / **3.2e+03** / 3.43e+03 |
| Urea price (Middle East granular, f.o.b.) (USD per tonne) | 520 | 232 / **443** / 854 | 109 / **400** / 967 |
| People in acute food insecurity (IPC/CH Phase 3+, GRFC) (million people) | 266 | 225 / **290** / 356 | 212 / **303** / 394 |
| People in IPC/CH Phase 5 (Catastrophe) (million people) | 1.4 | 0.346 / **1.6** / 3.49 | -0.0184 / **1.7** / 4.31 |
| CBOT front-month wheat price (USD per bushel) | 6.9 | 5.1 / **7.7** / 12.2 | 4.53 / **8.17** / 14.4 |
| Thai white rice 5% broken, f.o.b. (USD per tonne) | 365 | 249 / **405** / 661 | 212 / **427** / 779 |
| Lake Mead elevation (feet above mean sea level) | 1053 | 992 / **1.03e+03** / 1.07e+03 | 965 / **1.02e+03** / 1.07e+03 |
| WFP annual contributions received (USD billion, nominal) | 6.5 | 3.29 / **5.5** / 7.8 | 1.89 / **4.94** / 8.15 |
| Global undernourishment headcount (PoU) (million people) | 645 | 530 / **602** / 675 | 478 / **579** / 679 |
| Share of marine fish stocks within biologically sustainable levels (percent) | 62.4 | 57.5 / **60** / 62.4 | 55.2 / **58.7** / 62 |
| Israeli defence spending as share of GDP (% of GDP) | 7.9 | 4.6 / **6.09** / 8.8 | 3.05 / **5.12** / 8.85 |
| Israeli settler population in the West Bank (excl. East Jerusalem) (thousands of persons) | 530 | 585 / **613** / 648 | 620 / **658** / 707 |
| Cumulative external reconstruction financing disbursed for Gaza (USD billions (2026)) | 1.2 | 1.77 / **7.5** / 28.2 | 3.09 / **10.9** / 39.2 |
| Estimated Hezbollah rocket and missile inventory (thousands of units) | 15 | 4.97 / **24** / 67.8 | 2.74 / **29.1** / 89.9 |
| Bab el-Mandeb transit volume relative to 2023 baseline (index, 2023 = 100) | 48 | 31.6 / **71.9** / 99.9 | 30.2 / **85** / 124 |
| Annual conflict fatalities in the West Bank and East Jerusalem (persons per year) | 330 | 110 / **303** / 1.3e+03 | 20.8 / **286** / 1.67e+03 |
| Israeli net migration balance (thousands of persons per year) | -12 | -48.3 / **4.05** / 38.1 | -59.4 / **12.8** / 59.7 |
| Days per year with direct Israel-Iran or US-Iran kinetic exchange (days per year) | 110 | -0.0216 / **12.3** / 160 | -58.1 / **-40.7** / 163 |

## What drives the outcome

Share of the variance in peak systemic stress attributable to each event firing at all. High-scoring nodes are the ones worth watching, because learning how they resolve collapses the most uncertainty about everything else.

*Read with one caveat:* the stress index is built from these same events, so part of any node's score is its own contribution rather than its influence on others. The ranking is still informative — it combines probability, impact rating and correlation with the rest of the system in one number — but it is not a pure causal-influence measure, and a node cannot score high here without being either likely or heavy.

| Event | Variance share | P(by 2036) | Impact |
|---|---:|---:|---:|
| Global recession (world real GDP growth below 2.0% in a calendar year) | 4.5% | 62% | 7 |
| Severe rare-earth supply cutoff to the US or EU | 3.2% | 50% | 8 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 2.7% | 28% | 9 |
| S&P 500 falls 30%+ from its all-time closing high | 2.7% | 63% | 6 |
| Direct US-PRC military exchange causing at least one fatality | 2.5% | 13% | 9 |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 2.5% | 79% | 8 |
| US average effective tariff rate exceeds 15% | 2.5% | 50% | 5 |
| Brent crude settles above $120/bbl | 2.1% | 70% | 6 |
| New round of major direct Israel-Iran exchange | 2.0% | 83% | 7 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 1.9% | 12% | 10 |
| Brent monthly average above $120/bbl | 1.9% | 68% | 6 |
| US 10-year Treasury yield closes at or above 6.00% | 1.8% | 37% | 8 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 1.8% | 49% | 8 |
| Wave of emerging-market sovereign defaults or restructurings | 1.6% | 76% | 5 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 1.6% | 56% | 6 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 1.4% | 61% | 8 |
| China reports annual real GDP growth below 4.0% | 1.3% | 82% | 6 |
| WFP annual contributions fall below US$5 billion | 1.2% | 64% | 5 |

## Where the worldviews disagree most

The five parameterisations — raw analyst, audited, outside-view base rates, structural-break inside view, and prediction-market check — converge on most nodes. These are the ones where they don't, and they are exactly the forecasts you should hold most loosely.

| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |
|---|---:|---:|---:|---:|---:|---:|
| Japan 10-year government bond yield reaches 3.00% | 61% | 94% | 94% | 94% | 99% | 38pp |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 76% | 88% | 56% | 88% | 87% | 32pp |
| A G7 country cuts permanent immigration by three quarters | 21% | 39% | 10% | 39% | 39% | 29pp |
| Strait of Hormuz closed again for 14+ consecutive days | 41% | 69% | 69% | 69% | 69% | 28pp |
| US life expectancy at birth reaches 80.0 years | 62% | 85% | 86% | 86% | 86% | 24pp |
| Brent crude settles above $120/bbl | 52% | 71% | 70% | 71% | 75% | 23pp |
| Brent monthly average above $120/bbl | 51% | 69% | 71% | 70% | 74% | 23pp |
| US reports at least 5,000 confirmed measles cases in a single calendar year | 58% | 72% | 72% | 72% | 80% | 22pp |
| FAO Food Price Index reaches an all-time high above 160 | 54% | 73% | 75% | 73% | 72% | 21pp |
| Global oil demand declines year-on-year outside recession or supply shock | 68% | 58% | 58% | 79% | 58% | 21pp |
| FAO Food Price Index exceeds 160 in any month | 54% | 73% | 75% | 73% | 72% | 21pp |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 50% | 35% | 30% | 34% | 35% | 20pp |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 39% | 47% | 59% | 47% | 47% | 20pp |
| Severe rare-earth supply cutoff to the US or EU | 33% | 52% | 52% | 52% | 52% | 19pp |
| Sustained effective closure of the Strait of Hormuz | 76% | 88% | 69% | 88% | 88% | 19pp |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 23% | 23% | 23% | 23% | 41% | 18pp |

## What the red team said

Three lenses attacked the parameter set from different directions. Their numeric corrections are already in the forecast, carried by their own worldviews. Their reasoning is reproduced here because some of it is more useful than the numbers — and because a reader deserves to see the case against the model alongside its output.

### Structural-break / inside-view: where the 1950-2025 generating process is dead and the model is still sampling from it

*10 specific corrections proposed.*

This parameter set has one systematic, diagnosable failure, and it is not "too dramatic." It is that **threshold events on already-trending variables are priced as surprises rather than as trend arrivals.** Wherever a discrete risk sits on top of a continuous generator in `params/world_model.json`, the discrete node sits below what the model's own drift and quantiles imply — 12 of 12 cases I checked, all in the same direction. That is a bias, not noise.

The clearest instance: `frontier_train_flop_log10` has `p10_2031 = 28.0`, sitting exactly on the 1e28 threshold. The model's own generator therefore says ~93% by 2031. The discrete node says 58%. Same pattern on `metr_horizon_log2_hours` (generator 63% terminal, node 55%, and the node is a ratchet so it should exceed terminal), `global_tfr` (39% terminal, node 20%), `china_gdp_growth` (71% for the 2031 print alone, node 52% cumulative — a cumulative below a single in-window year is a hard incoherence).

The mechanism is double-discounting. The analyst bends the trend once when setting the continuous drift (METR: naive drift 1.3 gives 8.62 by 2031, they wrote 8.1), then applies the same "exponentials bend, base rates rule" haircut again at the discrete node. The reference class is invoked twice against evidence it has already been charged for.

Where the regime is genuinely broken, this bites hardest. Fertility: the UN transition model assumes convergence to ~1.8 and a floor. Observed global TFR fell 2.72→2.25 in nine years (−0.05/yr) against the model's assumed −0.022/yr, and every WPP/IHME revision since 2015 has moved down — serially correlated revisions are the signature of a prior the data keeps breaking. China growth: "Beijing prints within 0.3pp of target" was generated by land finance and property, which have ended; the target now follows the economy, and the model's own −0.24pp/yr drift concedes it.

Conversely, the pure-shock geopolitical nodes (Article 5, Taiwan invasion, nuclear use, grid cyber) are defensible or mildly high. The catalog is well-calibrated on things that go bang and badly complacent on things that arrive on schedule.

**Systematic bias estimate.** TOO COMPLACENT, and specifically so — not uniformly. The bias is concentrated in one identifiable node class and is close to absent elsewhere.

Measured: across the 12 nodes where a discrete threshold risk sits on top of a continuous generator in the model's own parameter file, the discrete node understates the generator-implied probability in 12 of 12 cases. Mean gap is +16.1 percentage points; mean log-odds gap is 0.87, i.e. the affected nodes run at roughly 1/2.4 of the odds their own generators imply (median 1/1.9). Directional unanimity at n=12 has a null probability of 2^-12 = 0.024%, so this is a bias, not sampling noise.

Diagnosis: double-discounting. The analyst bends the trend once when eliciting the continuous drift (METR naive 8.62 written as 8.1; global TFR observed -0.05/yr written as -0.022), then applies the same base-rate/reference-class haircut again at the discrete threshold. The reference class is charged twice against evidence it has already been paid for. Because the engine calibrates baselines to reproduce the elicited discrete marginals (README: "coupling reshapes the joint distribution, not the marginals"), this bias survives calibration untouched — the simulation faithfully reproduces the understatement, and the continuous variables and the discrete risks can disagree by a factor of two without any test failing. That is a structural gap in the engine, not just in the parameters: there is no consistency check binding a threshold node to its own generator.

Scope: I would apply a +1.9x to +2.4x odds correction to roughly 25-35 of the 159 nodes — the trend-arrival class (AI compute and capability, fertility, China growth, committed climate forcing, JGB/UST/reserve-share duration nodes, EV and oil demand). Median correction for those: +12 to +25pp.

For the pure-shock class — Article 5, Taiwan invasion, nuclear use in anger, grid cyberattack, AMOC tipping, unilateral SRM, UNSC expansion — the parameters are defensible or mildly too dramatic, and I would not move them upward on structural-break grounds. Several (grid_cyberattack_nato 20%, wetbulb_35c 30%, arctic_practically_ice_free 4%) are too high against zero-instance records.

Net verdict: too complacent by roughly 1.5x in odds on the affected subset, approximately unbiased on the shock subset, therefore mildly too complacent overall. The catalog is well-calibrated on things that go bang and poorly calibrated on things that arrive on schedule — exactly backwards for a decade in which the arriving things are the ones whose generating processes have changed.

**Scenarios it says are missing entirely:**

- Nuclear uploading with no discrete node. The model forecasts geo_deployed_strategic_warheads rising +95/yr to a 2031 median of 3720, yet there is no risk for 'US or Russia publicly exceeds the former New START ceiling of 1,550 deployed strategic warheads.' That is the most legible, most likely-to-fire post-arms-control event in the window (~55% by 2031), and the natural parent for new_nuclear_weapons_state, us_russia_strategic_arms_deal and dprk_nuclear_test. Its absence means the proliferation cascade runs off Iran and ROK narratives rather than off the arms-race variable the model already tracks.
- Taiwan semiconductor disruption decoupled from military action. The catalog prices invasion (6%) and quarantine (14%) but has no node for 'TSMC advanced-node (<=5nm) output falls >=50% for >=3 months for any cause.' The transmission channel that makes Taiwan matter to the economy and AI domains can fire without a shot: a Hualien-class earthquake, grid instability under AI load, a cyber incident, or an export-control action on Taiwan-fabbed Chinese-designed silicon. Conditioning the semiconductor shock exclusively on PLA action understates it substantially; I would put the disruption node at ~18% by 2031 against a ~20% union of the military nodes.
- State capture or requisition of frontier compute. The catalog has ai_state_datacenter_moratorium (58%) and ai_export_controls_relaxed (42%) but nothing in the seizure direction: a US Defense Production Act invocation over datacenter capacity or GPU allocation, a sovereign taking an equity or golden-share position in a frontier lab, or a national-security review blocking a training run. With hyperscaler_capex_usd_b at a 2031 median of 980bn and frontier_lab_arr_usd_b at 350bn, compute becomes strategically indistinguishable from enrichment capacity, and the historical analogue (uranium, telecoms, 1980s semiconductors) is state intervention, not laissez-faire. ~30% by 2031.
- Extended-deterrence intermediate step. Between the status quo and geopolitics_new_nuclear_weapons_state there is a far more likely observable that is absent: 'a US ally formally requests, or the US agrees to, forward-deployment of US nuclear weapons or a NATO-style nuclear-sharing arrangement in ROK, Poland, or Japan.' This is the step that either relieves or confirms proliferation pressure, has live political support in two of the three, and fires years before any indigenous programme would. ~30% by 2031. Without it the proliferation node has no early-warning parent and the cascade is all-or-nothing.
- Upward revision of committed warming. Every climate node treats the forcing as known and asks only whether thresholds are crossed. There is no node for 'IPCC AR7, WMO, or an equivalent assessment formally revises equilibrium climate sensitivity, the aerosol-masking term, or the remaining 1.5C carbon budget materially upward.' The 2023-2024 anomaly the analyst repeatedly calls partly unexplained is precisely the observation that would force such a revision, and AR7 lands inside the window. This is the climate analogue of a parameter-world shift and would move a dozen downstream nodes at once. ~35% by 2031.
- Demographic repricing event. The catalog covers births and TFR thresholds but not the institutional consequence that makes them matter: 'UN WPP or a G7 sovereign officially revises its long-run population or dependency-ratio projection down enough to trigger a pension or sovereign-debt reassessment (a rating action, or a statutory retirement-age change of >=2 years in a G7 country).' Fertility collapse transmits to the economy domain through fiscal projections, not birth counts, and no node currently carries that edge. ~40% by 2031.
- Collapse of the AI evaluation and disclosure regime. Several AI nodes (ai_metr_month_horizon, ai_1e28_flop_run, ai_china_leaderboard_top) depend on third parties continuing to measure and publish. There is no node for 'frontier labs collectively cease providing pre-deployment access to independent evaluators, or compute ceases to be reconstructable from public data.' This is a resolution-infrastructure risk that would render multiple nodes permanently NO regardless of underlying capability — a systematic downward bias on the whole AI block currently smuggled into the capability estimates rather than modelled explicitly. ~25% by 2031.

### Outside-view / base-rate hazard audit: implied per-year hazards recomputed from each p2031 and compared against the model's own stated reference classes and the 75-year historical record

*20 specific corrections proposed.*

Converting every p2031 to a per-year hazard (window = 5.42 years, h = -ln(1-p)/5.42) and comparing it to the base_rate_anchor the model itself wrote produces one clean, quantified finding: **the catalog discounts what it has counted and inflates what it has not.**

For nodes whose reference class contains zero or one historical instance, the implied hazard runs 2-8x the model's own stated base rate. politics_us_open_defiance_supreme_court: anchor "under 0.5%/yr", implied 4.1%/yr (8.2x). politics_us_armed_federal_state_confrontation: anchor "well under 0.5%/yr", implied 2.6%/yr — above even the rule-of-three 95% upper bound (3/150 = 2.0%/yr) for 150 years of zeros. geopolitics_grid_cyberattack_nato: anchor "well under 1%/yr", implied 4.1%/yr, for an event two-to-three orders of magnitude beyond anything ever achieved (Ukraine 2015: 230k customers, 6 hours). climate_wetbulb_35c_sustained implies 6.6%/yr for a three-hour exceedance with zero confirmed instances in 45 years.

For nodes whose reference class is well populated, the implied hazard runs 0.5-0.75x the stated base rate. foodwater_livestock_epizootic_g20: anchor 50-55%/yr, implied 26%/yr — the model halved its own number. economy_large_bank_failure: anchor ~10%/yr, implied 5.5%/yr. health_pandemic_1m_deaths: anchor post-1970 3.6%/yr, implied 2.36%/yr, discounted for "improved countermeasures" that COVID already falsified. politics_us_federal_official_assassinated: anchor ~3%/yr, implied 2.35%/yr, in a scenario the model elsewhere describes as the most violent US political environment in decades. politics_xi_departure rests on a base-rate anchor that counts only Hua Guofeng, omitting Hu Yaobang (1987) and Zhao Ziyang (1989) — both sitting General Secretaries removed, which is exactly what the criterion asks — understating the political-removal hazard by roughly an order of magnitude.

Median ratio (implied hazard ÷ own anchor): ~3.5x for zero-instance classes, ~0.65x for populated classes. That ~5x divergence is the signature of narrative-driven rather than frequency-driven parameterization. Separately, the duplicate-family resolver picks geopolitics_hormuz_major_closure (70%) as representative over economy_hormuz_closure (22%) and energy_hormuz_reclosure (34%) — selecting the member with the *strictest* bar and the *highest* probability, a logical nesting inversion that propagates the most dramatic member into the simulation.

**Systematic bias estimate.** Too dramatic, but modestly and unevenly — and mis-shaped far more than it is mis-levelled.

Quantified: for the ten nodes I checked whose reference class contains zero or one historical instance, the median ratio of implied per-year hazard to the model's OWN stated base rate is ~3.5x (range 1.9x to 8.2x, plus two nodes with an infinite ratio against zero-instance classes). For the six nodes whose reference class contains three or more instances, the median ratio is ~0.65x (range 0.50x to 0.77x). The divergence between the two regimes is therefore roughly 5x. This is the classic forecasting-tournament signature: over-prediction of novel change, under-prediction of boring recurrence.

Net effect on aggregate severity-weighted mass is smaller than that sounds. Summing (delta_p x severity) over my twenty corrections gives roughly -880 points from the over-stated set and +560 from the under-stated set, a net of about -320 pct-points x severity against a catalog total on the order of 35,000-40,000. Extrapolating the two regime multipliers across the full catalog (roughly 60 zero-instance-class nodes, roughly 45 well-populated-class nodes), I estimate the catalog is about 1.10-1.20x too dramatic in total expected severity-weighted harm — i.e. correct to within about 15%.

The structural problems are worse than the level problem and matter more for a simulation:
1. Mis-allocation. Probability mass sits on unprecedented adversarial and institutional-rupture events and is missing from recurring natural, epidemiological, financial and actuarial hazards. A simulation run on these parameters will generate futures whose failure modes are cyberattacks, constitutional crises and blockades, and almost never epizootics, reactor accidents, bank rescues or leaders simply dying.
2. Duplicate-family representative selection. Where families disagree, the resolver has in several cases elected the more dramatic member (Hormuz 70% over 22%/34%; FFPI 42% over 33%), which converts analyst disagreement into an upward bias rather than into uncertainty.
3. Hazard-shape inversion. Numerous nodes imply a DECLINING per-year hazard from 2027-2031 to 2032-2036 (Taiwan quarantine, UST 6%, Colorado storage, US CPI) while their own reasoning describes rising structural drivers. The 2027 column is the most inflated throughout — near-term narrative salience is being priced as probability.
4. Self-contradiction is the dominant error type, not disagreement with me. In at least twelve of the twenty corrections above, the correct number is recoverable from the base_rate_anchor the model itself wrote. A cheap and high-yield fix: mechanically recompute every p2031 from its own stated anchor hazard and require an explicit, evidenced multiplier wherever the posted number diverges by more than 1.5x in either direction.

**Scenarios it says are missing entirely:**

- Geophysical hazards are entirely absent. No node for an M8.5+ earthquake striking a megacity (base rate ~1 per 10-15 years globally for M8.5+, with Tokyo/Istanbul/Tehran/Lima exposure), no VEI-6+ eruption (~1 per 50-100 years, i.e. 5-10% by 2031, with a Pinatubo-scale climate signal that would directly contaminate the climate domain's temperature nodes), no Tohoku-class tsunami. These have the best-characterized base rates in the entire problem space and carry zero probability mass.
- Extreme space weather. A Carrington/May-1921-class geomagnetic storm is estimated at roughly 0.7-1.9%/yr (4-10% by 2031), and we are near solar maximum. This is glaring because the catalog contains TWO adversarial grid-down nodes (geopolitics_grid_cyberattack_nato 20%, energy_grid_physical_sabotage_major 20%) and zero natural ones — it models the pathway with no historical instances and omits the pathway with several.
- Actuarial leadership mortality as a first-class node. All-cause mortality for an 80-year-old male is ~4-6%/yr, i.e. ~25% over the window, yet the catalog prices only politics_us_federal_official_assassinated (12%). Presidential incapacity or death in office is both more likely than assassination and has different downstream dynamics. The same gap applies to any leader-transition node priced without a life-table term.
- A new interstate war outside the five enumerated dyads. The catalog names Russia-Ukraine, China-Taiwan, US-China, China-Japan and India-Pakistan, implicitly assigning zero to everything else. New interstate conflicts with 1,000+ battle deaths onset roughly once per 3-5 years globally; live candidates include Venezuela-Guyana, Algeria-Morocco, Ethiopia-Eritrea, Cambodia-Thailand, Azerbaijan-Armenia and Serbia-Kosovo. A 'some other dyad' residual node at ~35-50% by 2031 is required for the enumeration to be exhaustive.
- Mass-casualty terrorism in Western Europe. The catalog covers US political violence in detail and Sahel jihadism, but has no node for a 50+ death attack in Western Europe — a class with roughly one event per 3-4 years from 2004 to 2017 and roughly zero since 2020, which is exactly the kind of genuinely two-sided uncertainty a simulation should carry.
- Financial market-structure failure. There are nodes for yields, bank failure and private credit, but none for Treasury market dysfunction, a failed auction, or a central counterparty (CCP) failure. The 2019 repo squeeze and the March 2020 dash-for-cash give a real base rate of roughly one plumbing crisis per 5-7 years, and the stablecoin node's own reasoning identifies the T-bill market as the transmission channel without a node to transmit into.
- Non-influenza pandemic emergence. health_influenza_pandemic_declared covers flu and health_pandemic_1m_deaths is the only catch-all. There is no node for a coronavirus, paramyxovirus (Nipah) or arbovirus emergence with sustained transmission below the 1m-death bar — which is where most of the actual probability mass sits, and which is what a PHEIC node at 92% is implicitly absorbing without structure.
- A biosafety recurrence with better historical grounding. health_lab_origin_outbreak_confirmed sits at 6%, but the 2019-20 Lanzhou brucellosis leak (10,000+ officially attributed human infections, official attribution to a vaccine plant) would have resolved that criterion YES within the last decade. Including it in the reference class roughly doubles the anchor. Its omission is a further instance of the pattern above: a populated reference class treated as empty.

### Market / consensus-calibration red team: node-by-node comparison against live Polymarket, Kalshi, Metaculus prices and published institutional forecasts (NOAA/CPC, IMF, FAO, PAHO, METR), as of 29 July 2026.

*14 specific corrections proposed.*

Judged against actual prices, this parameter set is not uniformly "too dramatic." It is bimodally miscalibrated, and the split falls almost exactly along the line of whether a tradeable contract exists.

Where a liquid market or an issuing agency publishes a number, the set is systematically BELOW it. Polymarket prices "China blockade Taiwan in 2026" at 8% for five remaining months; the model prices 5% for seventeen (geopolitics_china_taiwan_quarantine_or_blockade). Polymarket prices "Iran Nuke before 2027" at 22-35%; the model says 5%. Polymarket prices Taiwan invasion by 30 Jun 2027 at 10%; the model says 1.5% through end-2027. NOAA/CPC's July 2026 discussion gives 81% for a very strong El Nino in OND; the model says 74% and then illegally accrues it to 85/90 on a criterion locked to the 2026-27 event. Kalshi has 2027 recession at 41% on top of 17.5% for 2026; the model says 33% for a window covering both. Metaculus implies ~5% for a non-test nuclear detonation by 2030; the model says 3.5% by 2031. The 10y JGB closed at 2.76% on 28 July and printed 2.901% mid-month; the model's own reasoning text still says "from ~2% to 3%" and prices 26%/50%.

Where no market exists, the set runs hot on vivid, unprecedented events: a 1M-people/24h state cyber-blackout at 20%, a practically ice-free Arctic at 4%/21%, a sustained 35C wet-bulb at 30%, UNSC expansion at 2.5%.

Worse than either is an outright axiom violation. economy_hormuz_closure (>50% below baseline for 14+ days) is strictly implied by geopolitics_hormuz_major_closure (same threshold, 30+ days) yet is priced 22% against 70% — a 48-point coherence break, with energy_hormuz_reclosure at 34% as a third inconsistent copy. climate_food_price_shock (FFPI >160) sits at 33% while the strictly harder foodwater_ffpi_above_160 (all-time high >160.3) sits at 42%. Any aggregation over this catalog is currently summing incoherent and double-counted mass.

**Systematic bias estimate.** Not uniformly biased — bimodally biased, with the split determined by whether a price exists.

(A) Market-comparable nodes: systematically TOO COMPLACENT by roughly 2x. Taking the eight nodes above where I could source a live contract or an issuing-agency number and applying a standard longshot/criteria haircut to the market, the model's values average about 0.45-0.55x the defensible market-consistent value. Worst offenders: economy_jgb_3pct (~0.5x at 2027, ~0.54x at 2031, and factually anchored to a stale spot level), geopolitics_iran_nuclear_weapon (~0.4x), geopolitics_china_taiwan_quarantine_or_blockade (~0.55x), geopolitics_china_taiwan_invasion (~0.4x). Even the flagship tail, geopolitics_nuclear_use_in_anger, sits below Metaculus.

(B) Non-market catastrophe nodes: TOO DRAMATIC by roughly 1.8-2.0x. Where the event is vivid, unprecedented and unpriceable — grid_cyberattack_nato, arctic_practically_ice_free, wetbulb_35c_sustained, amazon_net_carbon_source, climate_billion_dollar_climate_judgment, unsc_permanent_expansion — the numbers run about double what base rates plus the stated resolution wording support. The tell is that in almost every case the model's own contrarian paragraph contains the correct argument and the headline number ignores it.

(C) Coherence: the catalog is not a probability distribution. Three overlapping Hormuz nodes violate monotonicity by up to 48 points; two FFPI nodes are inverted; Iran regime change is double-listed across domains (26% and 27%) and would be double-counted by any severity aggregation; el_nino accrues probability on a criterion locked to a single 2026-27 event. Fix these before tuning any levels — they corrupt the aggregate more than any single mis-priced node.

Net effect on a simulation: because the complacent nodes cluster in high-frequency macro/geopolitical drivers and the dramatic nodes cluster in low-frequency terminal states, the parameter set will under-generate ordinary turbulence and over-generate exotic catastrophe. The world it simulates is too quiet on the way to being too apocalyptic. The single highest-value fix is economy_jgb_3pct; the single highest-value structural fix is the Hormuz monotonicity violation.

**Scenarios it says are missing entirely:**

- US-Venezuela / Western Hemisphere escalation. The catalog's reasoning text repeatedly cites 'the Venezuela intervention' and 'the 2026 Venezuela/Iran precedents' as drivers of OTHER risks, but there is no risk_id for it. An active US military operation in the hemisphere is being used as an exogenous input while carrying no probability, no severity and no uncertainty of its own. politics_us_strike_inside_mexico (44%) is the only hemispheric node and covers a different country.
- Taiwan semiconductor supply disruption WITHOUT invasion or blockade. There is no node for a TSMC production halt from earthquake, drought, grid failure, cyber incident, or export-control retaliation. This is plausibly the largest single economic tail in the entire catalog and it is only reachable through two nodes priced at 6% and 14%. The 2024 Hualien quake and Taiwan's recurring water crises are the base-rate evidence.
- Frontier model weight exfiltration by a state actor. The AI domain covers cyberattacks BY AI (ai_major_cyber_incident) and bio-misuse (ai_bio_mass_casualty) but not theft of frontier weights, which is the modal proliferation pathway named in essentially every lab and USG threat model and which would invalidate ai_export_controls_relaxed, ai_china_leaderboard_top and ai_us_china_binding_agreement simultaneously.
- Advanced-economy sovereign funding accident distinct from spread widening. economy_euro_periphery_stress measures a 300bp spread and economy_ust_6pct measures a yield level, but neither captures a failed or tailed auction, a gilt-LDI-style forced-deleveraging spiral, or an emergency central bank intervention in the primary market. The 2022 UK episode resolved NO on both existing criteria while being the closest advanced-economy funding accident in decades.
- Measurement-infrastructure failure as a first-class risk. At least six nodes depend on observing systems that may not survive the window: RAPID (climate_amoc_30pct_weakening, flagged as funding-fragile in the model's own text), METR's ability to run 167-hour evals, IMF COFER continuity, NOAA Coral Reef Watch methodology, PISA participation, and the Global Carbon Project. The catalog treats resolution machinery as exogenous and certain. Several risks should carry an explicit 'unresolvable' branch.
- Climate-driven insurance and mortgage market withdrawal. No node covers a major insurer exiting a US state or an EU country at scale, a state residual-market insolvency, or GSE/lender repricing of coastal and wildfire mortgage risk. This is the transmission channel by which climate becomes a financial-stability event, and it is absent from both the climate and economy domains.
- Undersea cable, GPS and space-segment disruption. The catalog has grid cyber and grid physical sabotage nodes but nothing on subsea telecom/data cables, GNSS jamming or spoofing at scale, or an anti-satellite event or Kessler cascade. Baltic and Red Sea cable incidents in 2024-2026 are the live base rate, and a serious event would hit finance, aviation and energy simultaneously.
- Assassination or sudden incapacity of a major non-US leader. politics_us_federal_official_assassinated (12%) covers the US; politics_russia_leadership_change and politics_xi_departure cover departure generically. There is no node for the violent or sudden removal of a leader in India, Saudi Arabia, Pakistan, Israel, Turkey or a G7 state, despite several of these being single points of failure for other nodes in the catalog.

## What to watch, and when

Dated forcing functions the analysts flagged. These are the model's *inputs*, not its outputs — the scheduled moments when a hazard gets resolved or reset. More actionable than any single probability on this page, because they are the points at which you get to update.

| Date | Domain | Event | Why it matters |
|---|---|---|---|
| `2026-07-31` | economy | **Section 232 pharmaceutical tariffs take effect** | First major sectoral replacement for the expired Section 122 surcharge; sets the template for rebuilding tariff walls on Section 232 legal footing after the Supreme Court struck IEEPA. |
| `2026-08` | geopolitics | **Deadline from 14 June US-Iran MoU to formally end the 2026 Iran war (60 days)** | Failure already partly realised via July strikes/blockade; a formal collapse re-prices Hormuz risk and Gulf insurance. |
| `2026-08` | economy | **Jackson Hole symposium — Warsh's first as Fed chair** | Earliest venue for the new chair to articulate a framework. Warsh has historically favored a smaller balance sheet and rules-based policy; a doctrinal break would reprice the entire term structure. |
| `2026-08` | ai | **Nvidia Q2 FY2027 earnings (guided ~$91B revenue)** | The single highest-information event for the AI capex cycle. A miss or soft guide during an ongoing Nasdaq correction would be the clearest bubble-deflation trigger. |
| `2026-08` | energy | **OPEC+ August production tranche and subsequent ministerials** | OPEC+ has signalled it will proceed with scheduled increases into an already ~2 Mb/d surplus, prioritising market share over price. Determines whether Brent breaks below $60. |
| `2026-08` | politics | **EU AI Act Article 50 transparency/labelling obligations become enforceable** | First binding regime requiring disclosure of AI-generated content, fines to 6% of global revenue; sets the global template for synthetic-media governance and will be stress-tested against the 2026-27 European election cycle. |
| `2026-08-02` | ai | **EU AI Act: Commission GPAI enforcement powers and penalties activate (up to €15M / 3% turnover); Art.50 synthetic-media transparency applies** | First moment the EU can actually fine frontier model providers. Sets precedent for whether the AI Act has teeth or becomes a paper regime. |
| `2026-08-07` | foodwater | **FAO Food Price Index, July 2026 release** | First index reading capturing the July Black Sea escalation and the urea spike; a jump above ~136 would signal the benign H1 regime has ended. |
| `2026-08-12` | foodwater | **USDA August WASDE with first survey-based US corn/soybean yields** | Resolves the biggest single uncertainty in the 2026/27 global maize balance sheet after a heat-stressed US summer and a 24 Mt y/y stock draw. |
| `2026-08-15` | foodwater | **Reclamation August 24-Month Study sets 2027 Colorado River shortage tier** | Determines mandatory Lower Basin cuts for 2027 and is the operative trigger for Arizona/Nevada/Mexico agricultural curtailment. |
| `2026-08-16` | energy | **US-Iran 60-day truce nominal expiry** | The ceasefire framework signed 17 Jun 2026 that reopened the Strait of Hormuz is time-limited. Non-renewal is the highest-probability near-term trigger for a repeat oil shock. |
| `2026-08-16` | israel | **Expiry of the 60-day US-Iran MoU ceasefire window** | The MoU's ceasefire, Hormuz demining and downblending commitments all run on this clock; lapse without a successor deal is the most likely trigger for a renewed strike campaign and a fresh oil spike. |
| `2026-09` | geopolitics | **18th BRICS Summit, New Delhi (India presidency)** | Tests whether de-dollarization moves from rhetoric to plumbing (BRICS Pay, gold-linked Unit, CBDC interoperability) or is again shelved by India. |
| `2026-09` | climate | **Arctic sea ice September minimum 2026** | First minimum under a developing super El Nino and after a record-tying winter maximum; a sub-4.0 million km2 reading would be the first since 2012 and would shift ice-free-Arctic timelines. |
| `2026-09` | economy | **September FOMC with Summary of Economic Projections** | First full dot plot under Warsh. Market currently prices hikes toward ~4% by year-end — the SEP either validates a hiking cycle or breaks it. |
| `2026-09` | politics | **German Land elections: Saxony-Anhalt, Mecklenburg-Vorpommern, Berlin** | AfD is favoured or near-first in both eastern states; a first-place finish with no available coalition partner is the most likely trigger for a formal crisis over the CDU 'firewall'. |
| `2026-09` | politics | **Russian State Duma election** | Managed election, but seat allocation and any United Russia weakness are the main public signal about elite cohesion and post-Putin positioning. |
| `2026-09-08` | demographics | **PISA 2025 initial results release (OECD)** | First global measure of whether post-COVID learning loss has been recovered; 90+ countries, science as focal domain plus a new digital-learning domain. |
| `2026-09-13` | politics | **Swedish general election** | Tests whether Sweden Democrats convert confidence-and-supply into cabinet seats - a bellwether for Nordic normalization of the radical right. |
| `2026-09-14` | health | **IGWG8 negotiations on PABS annex to the WHO Pandemic Agreement** | The Pandemic Agreement cannot open for signature or ratification until the PABS annex is adopted; failure here freezes the entire post-COVID legal architecture for another year. |
| `2026-09-30` | demographics | **India Census 2027 Phase I houselisting operations** | Completion of the housing census; first hard national count since 2011 and the gateway to caste enumeration and parliamentary delimitation. |
| `2026-09-30` | israel | **Phase 2 of LAF disarmament of Hezbollah north of the Litani** | Four extendable months from mid-2026; an Israeli assessment that phase 2 has failed is the stated predicate for resuming operations in Lebanon. |
| `2026-10-01` | climate | **US Interior Department deadline to finalize post-2026 Colorado River operations** | Seven basin states failed to reach consensus twice; federal imposition creates high probability of Compact litigation reaching the Supreme Court, the largest water-allocation fight in US history. |
| `2026-10-01` | economy | **US fiscal year 2027 begins; appropriations deadline** | Shutdown risk with a ~$1.9trn deficit and interest above $1trn; also the point at which Section 232 revenue replaces expired Section 122 revenue in the baseline. |
| `2026-10` | economy | **IMF/World Bank Annual Meetings and WEO releases (semiannual)** | Recurring forcing function for consensus growth and debt-sustainability revisions; October 2026 GFSR is the likely venue for a formal private-credit and AI-debt warning. |
| `2026-10-01` | demographics | **India census reference date for snow-bound regions (Ladakh, J&K, HP, Uttarakhand)** | First actual population enumeration in India in 16 years; early signal of count quality and of self-enumeration uptake. |
| `2026-10-01` | demographics | **US FY2027 Presidential Determination on refugee admissions** | Sets the legal ceiling on US resettlement; FY2026 was a record-low 7,500 and the FY2027 number is a direct read on regime persistence. |
| `2026-10-01` | health | **FY2027 US appropriations deadline / start of fiscal year** | Second test of whether Congress again rejects proposed deep CDC/NIH/global health cuts, or whether impoundment and rescission tactics succeed. |
| `2026-10` | health | **WHO Global Tuberculosis Report (annual)** | First clean measure of whether 2025-26 financing cuts reversed the multi-year TB mortality decline. |
| `2026-10` | politics | **Israeli Knesset election (legally due)** | Post-war coalition realignment; outcome drives regional escalation risk and the durability of judicial-overhaul-era institutional damage. |
| `2026-10-04` | climate | **Brazil general election (first round)** | Determines whether the 50% cumulative Amazon deforestation reduction since 2022 continues or reverses; the single largest lever on land-use emissions and Amazon tipping risk. |
| `2026-10-04` | politics | **Brazilian general election (presidential first round)** | Largest Latin American democracy; determines whether the 2022-23 institutional crisis was resolved or merely deferred, and shapes the regional bloc's posture toward US intervention in Venezuela. |
| `2026-10-13` | ai | **US interagency assessment of nucleic acid synthesis screening framework due** | Determines whether DNA synthesis screening becomes mandatory in the US as AI protein-design tools erode existing sequence-based screens. |
| `2026-10-19` | climate | **CBD COP17, Yerevan, Armenia** | First Global Review of Kunming-Montreal GBF implementation; will quantify how far behind the 30x30 target the world is and whether resource mobilisation targets are met. |
| `2026-10-27` | israel | **Israeli Knesset election** | Determines whether the next government pursues de jure annexation and further judicial legislation, or trades territory for Saudi normalisation; also decides the Haredi conscription settlement. |
| `2026-11` | geopolitics | **Expiry of the US-China tariff truce agreed at Busan** | If it lapses, rare-earth export controls and tech restrictions resume, raising the economic-coercion baseline around Taiwan. |
| `2026-11` | climate | **Global Carbon Budget 2026 release** | Will show whether 2026 fossil CO2 exceeded the 38.1 GtCO2 record, and how the El Nino suppressed the tropical land carbon sink. |
| `2026-11` | health | **PAHO Regional Verification Commission review of US measles elimination status** | First formal test of whether the US loses measles elimination for the first time since 2000 - a high-salience symbolic and diplomatic shock with knock-on effects for regional certification. |
| `2026-11-03` | geopolitics | **US midterm elections** | Determines congressional constraint on unilateral force use (Venezuela, Iran), Ukraine funding, and NATO drawdown politics. |
| `2026-11-03` | economy | **US midterm elections** | Determines whether tariff authority, fiscal expansion, and Fed oversight change hands. A divided Congress raises debt-ceiling and shutdown risk for 2027-2028. |
| `2026-11-03` | ai | **US midterm elections** | Datacenter electricity bills and AI job anxiety are live campaign issues; outcome shapes whether federal preemption of state AI law is achievable in the 120th Congress. |
| `2026-11-03` | demographics | **US midterm elections** | Immigration is the top-salience issue; a change in House control constrains further statutory restriction and appropriations for enforcement. |
| `2026-11-03` | energy | **US midterm elections** | Determines whether the OBBBA clean-energy rollback is entrenched, softened or extended; also shapes FEOC enforcement and permitting-reform prospects. |
| `2026-11-03` | health | **US midterm elections** | Determines congressional appropriations and oversight leverage over HHS vaccine policy for FY2028-29; a chamber flip changes the constraint set on ACIP/CDC actions. |
| `2026-11-03` | politics | **US midterm elections** | The single biggest forcing function in this domain. Divided government would restore subpoena power and appropriations leverage; disputes over the six redrawn state maps create the most plausible near-term certification crisis. |

## What this model cannot do

- **The parameters are elicited judgement, not measurement.** The engine is exact; the inputs are informed opinion, audited and red-teamed but still opinion. Simulation precision does not create forecast accuracy, and the 90% bands cover disagreement between the modelled worldviews, not the possibility that all five are wrong together.
- **Correlated error is unmodelled.** If the analysts share a blind spot, the ensemble inherits it silently and reports narrow bands over a wrong centre.
- **Resolution criteria carry real weight.** Several forecasts move by tens of percentage points on the wording of what counts. Read the criteria before quoting a number.
- **Nothing outside the risk set can happen.** The events that most reshape a decade are frequently ones nobody enumerated in advance. Treat the 'no severe event' probability as an upper bound on calm.
- **Causal edges are assumed, not estimated.** The dependency structure comes from domain reasoning about transmission channels, not from fitting historical co-occurrence — there is no dataset of decades to fit it to.
- **Hazards are conditionally memoryless within each segment.** Real crises have internal dynamics — mobilisation, negotiation, exhaustion — that a piecewise exponential cannot represent.
- **Every node fires at most once, which understates the late 2030s.** The elicited quantity is P(happens at least once by date T), so the reported probabilities are right. But the register mixes one-shot structural events (an AMOC tipping point) with recurring ones (a US recession, an oil spike), and treating a recession as absorbing means the model cannot have a second one. That is why the stress index declines after its late-2020s peak: the pool of un-fired risk depletes. Read the trajectory for its early shape and its spread, not for its level in 2035.
- *geopolitics*: Leadership mortality and succession are the largest unmodelled discontinuity. Putin (73), Trump (80), Khamenei's untested successor Mojtaba, Kim Jong Un's health, and Xi's post-purge PLA all sit on single points of failure. A single actuarial event could invert the sign of several of these forecasts within weeks, and no reference class gives useful conditional probabilities for what follows. The 2026 Iranian case shows that even an externally-imposed succession produces outcomes (short-run consolidation) opposite to the intuitive prediction.
- *climate*: The post-2023 warming acceleration is not fully explained. The 2023-24 jump exceeded CMIP6 expectations and candidate causes - declining planetary albedo from reduced low-cloud cover, aerosol unmasking, Hunga Tonga stratospheric water vapour - have very different implications. If reduced cloud cover is a genuine positive feedback newly engaged, every temperature trajectory here shifts up 0.2-0.4C by 2036 and effective climate sensitivity is higher than assumed. If it was a transient confluence, current anomalies partially relax and the trend reasserts at 0.25C/decade. This single uncertainty dominates the temperature distribution and I cannot resolve it.
- *economy*: AI as a genuine total factor productivity shock. If AI raises trend productivity growth by even 0.5-1.0pp, then debt/GDP paths, equity valuations at CAPE 40.9, and the sustainability of a 4.6% 10-year all look completely different — the denominator grows out of the problem, and what looks like a bubble is a correctly-priced regime change. Every risk in this model that is anchored on debt sustainability or valuation reversion is conditionally wrong in that world. Conversely, if AI capex proves to be a depreciating expense rather than a productive asset, the same nodes are far too optimistic. I have no reliable way to distinguish these ex ante and the model should be run under both regimes.
- *ai*: Measurement collapse: there is no agreed capability metric that survives saturation. MMLU is dead, HLE is at 53%, ARC-AGI-2 is at 85% while ARC-AGI-3 is under 1%, and METR's time-horizon figures differ by 6x across sources I searched this session. Every capability-conditioned probability in this model inherits that ambiguity, and 'AGI' questions may be permanently unresolvable rather than merely uncertain.
- *demographics*: Whether ultra-low fertility has a floor at all. Every projection in this domain, including the UN's, assumes mean reversion of TFR toward roughly 1.6-1.8 in the very-low-fertility countries. If that assumption is simply wrong — if there is no floor and Korea's 0.8 is a waypoint rather than a trough — then peak population arrives decades earlier and every dependency-ratio and pension model in existence is optimistic. Conversely, if Korea's two-year rise proves that most of the decline was tempo (postponement) rather than quantum (foregone births), a large mechanical rebound is coming and the depopulation literature is overshooting. These two possibilities are both live and imply opposite policy conclusions.
- *energy*: AI compute demand could be wrong by a factor of three in either direction, and it is the single largest new driver in this model. A capex retrenchment - from inference efficiency gains, model commoditisation, or a financing shock - would remove the demand pull currently justifying gas turbine orders into 2030, uranium at 17-month highs, nuclear restarts and most of the grid-scarcity narrative. Conversely a buildout at announced scale would break the grid in several US regions and pull coal and gas retirements forward by years. Every datacenter-linked variable here is conditional on a regime that may not persist.
- *health*: Measurement collapse can masquerade as improvement. Every headline indicator here is a detection-adjusted quantity, and detection capacity is falling sharply and unevenly - CDC workforce down roughly a third, WHO budget cut a fifth with 45% of the remainder unfunded, and Ebola suspected-case declines in Ituri that experts read as testing breakdown. A simulation calibrated on reported counts will systematically understate burden and, worse, will read weakening surveillance as declining risk. A serious version of this model needs an explicit latent-true-incidence layer with a time-varying, regime-dependent ascertainment fraction.
- *politics*: Index construction is doing much of the work. V-Dem's expert-coder panels and Freedom House's analyst scoring both revise back-series annually and both added the US, UK and Italy as 'autocratizers' in the same edition. Some of the measured global decline is real institutional change; an unknown but non-trivial share is coder sentiment about a small number of high-salience leaders, plus coverage expansion. If the indices partly measure elite mood, a simulation that treats them as ground truth will mistake a measurement regime shift for a world-state shift - and will also miss backsliding where no panel is watching closely.
- *foodwater*: Chinese stock opacity. China is reported to hold roughly half of world wheat and over 60% of world maize stocks. The headline 32.0% stocks-to-use ratio, which is the model's main comfort signal, may be materially overstated as a global buffer — the tradeable ex-China ratio is closer to 18-20%. If Chinese reserves are also smaller or lower-quality than reported, the entire price-response function of this model is miscalibrated and shocks would transmit far more violently than simulated.
- *israel*: Whether the June-2026 US-Iran MoU converts into a durable agreement with verified downblending, or lapses in mid-August 2026 into renewed campaigning. Almost every other node in this sub-domain is conditioned on this branch, and the two branches differ by a factor of two to three in most probabilities.

---

*Generated by the `worldsim` Monte Carlo engine. Parameters, dependency structure, and red-team corrections are in `params/`; rerun with `python run_simulation.py`.*
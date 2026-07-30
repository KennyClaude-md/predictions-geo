# World Futures Simulation — Forecast Report

**Simulation date:** 2026-07-29  
**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  
**Paths:** 4,800 across 5 worldviews × 40 parameter worlds  
**Risk nodes:** 240 · **causal edges:** 118 · **latent factors:** 6 · **continuous variables:** 112

---

## How to read this

Every number below is the output of a survival-process Monte Carlo, not a guess written directly. Nine domains were parameterised against current sources, audited for base-rate discipline, then red-teamed from three directions. Each of those opinions is run as a separate worldview and the results are pooled by weight.

**The bracketed range is not the range of outcomes** — the event either happens or it doesn't. It is the range of *the probability itself* across parameter worlds: how much the answer moves depending on whose model of the world you accept. A wide bracket means the forecast is fragile. Monte Carlo noise has been subtracted out, so what remains is real disagreement.

**Calibration check:** simulated marginals reproduce the elicited cumulative probabilities to within 7.10 percentage points (worst node, worst worldview). This matters: the dependency network is tuned to reshape the *joint* distribution — which events co-occur — without inflating any individual probability above what the underlying analysis actually claimed.

## Headline forecasts

Ranked by expected systemic impact — probability by 2036 multiplied by severity — rather than by probability alone, because a 12% chance of something that reorders the world outranks a near-certainty that doesn't.

| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Impact |
|---|-------|--------:|--------:|--------:|:---------------:|----:|
| 1 | **Frontier agent reaches a 1-work-month 50%-reliability task horizon** | 10% | 65% | 76% | [44%–98%] | 9 |
| 2 | **Civil war onset in a country of 50 million or more that was at peace in mid-2026** | 29% | 66% | 83% | [64%–98%] | 8 |
| 3 | **Japan 10-year government bond yield reaches 3.00%** | 57% | 75% | 93% | [53%–>99%] | 7 |
| 4 | **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** | 62% | 74% | 78% | [45%–98%] | 8 |
| 5 | **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** | 88% | 93% | 98% | [93%–99%] | 6 |
| 6 | **New round of major direct Israel-Iran exchange** | 54% | 77% | 84% | [63%–98%] | 7 |
| 7 | **China annual births fall below 7.0 million** | 45% | 96% | 98% | [91%–99%] | 6 |
| 8 | **China's extraterritorial rare-earth export control regime enters into force** | 45% | 77% | 83% | [57%–98%] | 7 |
| 9 | **Renewed major US and/or Israeli air campaign against Iran** | 18% | 55% | 83% | [49%–99%] | 7 |
| 10 | **A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test** | 17% | 45% | 66% | [25%–98%] | 8 |
| 11 | **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** | 18% | 57% | 74% | [43%–97%] | 7 |
| 12 | **Nvidia suffers a ≥50% peak-to-trough drawdown** | 28% | 66% | 84% | [59%–97%] | 6 |
| 13 | **US recession with NBER-dated peak in the window** | 25% | 57% | 84% | [63%–98%] | 6 |
| 14 | **A single training run of ≥1e28 FLOP is publicly reported** | 9.1% | 72% | 83% | [60%–97%] | 6 |
| 15 | **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** | 14% | 43% | 61% | [38%–82%] | 8 |
| 16 | **China's officially reported population falls below 1.400 billion** | 58% | 96% | 98% | [94%–99%] | 5 |
| 17 | **US unemployment rate ≥6.0% for three consecutive months** | 15% | 56% | 82% | [53%–98%] | 6 |
| 18 | **Disintegration of the Thwaites Eastern Ice Shelf** | 9.8% | 35% | 61% | [22%–97%] | 8 |
| 19 | **China reports annual real GDP growth below 4.0%** | 21% | 65% | 81% | [54%–97%] | 6 |
| 20 | **A top-4 US hyperscaler guides annual capex down year-over-year** | 23% | 75% | 81% | [58%–96%] | 6 |
| 21 | **New IPC/CH Famine (Phase 5) classification anywhere** | 69% | 93% | 97% | [92%–99%] | 5 |
| 22 | **Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt** | 15% | 44% | 68% | [30%–98%] | 7 |

## The decade in aggregate

Individual probabilities are the easy part. The question that actually determines how the 2030s feel is how many high-impact events land, and whether they land together.

**Read the impact rating carefully.** Analysts were asked for *global systemic impact if it occurs*, where 10 is civilization-altering — that is a measure of magnitude, not of badness. A transformative AI capability milestone legitimately scores 9 on it. These are high-impact events, not a count of catastrophes.

| Impact tier | Nodes | Expected count | Median | P(none) | P(≥2) | P(≥3) |
|---|---:|---:|---:|---:|---:|---:|
| **6+ / 10** | 117 | 53.1 | 53 | <0.5% | >99% | >99% |
| **7+ / 10** | 73 | 27.4 | 27 | <0.5% | >99% | >99% |
| **8+ / 10** | 42 | 12.2 | 12 | <0.5% | >99% | >99% |
| **9+ / 10** | 14 | 2.7 | 3 | 4.2% | 78% | 51% |

The 6+ band is broad — it contains a US recession alongside a Taiwan contingency — so the headline that the median decade fires 53 of its 117 nodes says less about danger than it first appears. The discriminating number is the tier above: across 14 nodes rated 9 or 10 for global impact, the model expects 2.7 of them this decade, puts 96% on at least one and 78% on two or more. That is the finding: a decade with no order-changing event is a minority outcome, and the interesting variance is not *whether* they arrive but whether they arrive spaced out or together.

**A caveat on cross-domain comparison.** Each domain was rated by a different analyst against the same nominal 0–10 scale, and they did not use it identically: *geopolitics* averages 7.7 while *foodwater* averages 5.5 (overall 6.3). Some of that gap is real — great-power conflict genuinely carries more systemic weight than a macro data print — but some of it is rater drift, and it means the impact ranking tilts toward whichever domain scored most generously. Compare probabilities across domains freely; compare severities within a domain.

## Scenario archetypes

Paths were clustered on which major events fired and on the shape of the systemic-stress trajectory. These are not scenarios written in advance and then assigned probabilities — they are the shapes the simulation actually produced, priced by how much of the path mass fell into each.

### Severe decade — technological discontinuity and institutional breakdown — **33%**

Concurrent failure across domains. Shocks arrive faster than systems absorb them, and the response to one degrades the capacity to answer the next. The distinguishing driver is technological discontinuity compounded by institutional breakdown. Typical peak stress sits at the 76th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — 96% here vs 76% overall
- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 99% here vs 83% overall
- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — 91% here vs 78% overall
- **New round of major direct Israel-Iran exchange** — 95% here vs 84% overall

### Manageable decade — technological discontinuity and institutional breakdown — **30%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is technological discontinuity compounded by institutional breakdown. Typical peak stress sits at the 29th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — 100% here vs 76% overall
- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 100% here vs 83% overall
- Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) — *suppressed*: 63% here vs 78% overall
- New round of major direct Israel-Iran exchange — *suppressed*: 72% here vs 84% overall

### Manageable decade — institutional breakdown — **18%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is institutional breakdown. Typical peak stress sits at the 43th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 100% here vs 83% overall
- Frontier agent reaches a 1-work-month 50%-reliability task horizon — *suppressed*: 0% here vs 76% overall
- AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption — *suppressed*: 51% here vs 74% overall

### Manageable decade — no dominant driver — **16%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 40th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- Civil war onset in a country of 50 million or more that was at peace in mid-2026 — *suppressed*: 0% here vs 83% overall

### Manageable decade — no dominant driver (variant) — **3.2%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 42th percentile of all simulated paths.

## Full results by domain

### AI, compute & transformative technology

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | 10% | 65% | 76% | [44%–98%] | 9 | 2029Q2 |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 18% | 57% | 74% | [43%–97%] | 7 | 2029Q4 |
| Nvidia suffers a ≥50% peak-to-trough drawdown | 28% | 66% | 84% | [59%–97%] | 6 | 2029Q2 |
| A single training run of ≥1e28 FLOP is publicly reported | 9.1% | 72% | 83% | [60%–97%] | 6 | 2029Q2 |
| US unemployment rate ≥6.0% for three consecutive months | 15% | 56% | 82% | [53%–98%] | 6 | 2030Q1 |
| A top-4 US hyperscaler guides annual capex down year-over-year | 23% | 75% | 81% | [58%–96%] | 6 | 2028Q4 |
| Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt | 15% | 44% | 68% | [30%–98%] | 7 | 2030Q2 |
| A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 25% | 64% | 83% | [56%–98%] | 5 | 2029Q3 |
| China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab | 3.5% | 30% | 59% | [23%–97%] | 7 | 2031Q4 |
| A top-5 Western frontier lab exits frontier training | 9.8% | 44% | 66% | [39%–88%] | 6 | 2030Q3 |
| Frontier capability plateau: 24 months with no material aggregate benchmark advance | 6.9% | 25% | 43% | [13%–81%] | 8 | 2031Q1 |
| A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month | 21% | 55% | 67% | [36%–93%] | 5 | 2029Q1 |
| US licenses its current-flagship datacenter GPU for general commercial sale to China | 14% | 45% | 55% | [17%–93%] | 6 | 2029Q3 |
| US driverless robotaxi services exceed 5 million paid rides per week | 5.0% | 67% | 79% | [54%–97%] | 4 | 2029Q3 |
| Court judgment or settlement >=$5B against a frontier lab over training data, or an injunction restricting training on copyrighted corpora | 9.1% | 31% | 51% | [13%–92%] | 6 | 2030Q4 |
| Grid emergency or load-shed event officially attributed in part to datacenter demand | 12% | 37% | 59% | [18%–98%] | 5 | 2030Q3 |
| Confirmed theft or leak of frontier model weights | 5.5% | 21% | 37% | [7.8%–74%] | 8 | 2031Q1 |
| US Congress enacts broad federal preemption of state AI laws | 11% | 34% | 56% | [30%–80%] | 5 | 2030Q4 |
| US enacts binding federal pre-deployment evaluation or licensing requirements for frontier models | 8.6% | 26% | 43% | [9.5%–89%] | 6 | 2030Q3 |
| A top mathematics journal publishes a paper whose central theorem was found primarily by AI | 13% | 51% | 74% | [50%–96%] | 3 | 2030Q1 |
| A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections | 14% | 38% | 51% | [27%–78%] | 4 | 2029Q4 |
| Taiwan Strait event materially disrupts advanced-node or CoWoS output | 2.8% | 8.9% | 16% | [1.7%–41%] | 10 | 2031Q2 |
| Binding US-China agreement on frontier AI compute or model thresholds | 1.5% | 8.9% | 17% | [4.3%–32%] | 4 | 2031Q4 |
| AI-assisted biological attack causing ≥10 deaths, officially confirmed | 1.4% | 4.8% | 6.9% | [1.7%–20%] | 9 | 2030Q4 |
| A quantum computer publicly factors an RSA-2048 modulus | <0.5% | 1.4% | 6.8% | [3.7%–12%] | 8 | 2033Q3 |

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
- **Frontier capability plateau: 24 months with no material aggregate benchmark advance** — The top score on Artificial Analysis's Intelligence Index (or an endorsed successor composite) increases by less than 5 index points over any 24-consecutive-month period beginning after 2027-01-01.
- **A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month** — A model developed by a China-headquartered organization holds the top overall rank on Artificial Analysis's Intelligence Index or LMArena's overall text leaderboard continuously for at least 30 days.
- **US licenses its current-flagship datacenter GPU for general commercial sale to China** — BIS policy permits general (not narrowly case-by-case) export to Chinese commercial customers of Nvidia's then-current top-of-line datacenter accelerator, within one product generation of the US-available flagship.
- **US driverless robotaxi services exceed 5 million paid rides per week** — Publicly reported paid rides in fully driverless (no human safety operator in vehicle) commercial services in the US total ≥5,000,000 in a single week, summed across all operators.
- **Court judgment or settlement >=$5B against a frontier lab over training data, or an injunction restricting training on copyrighted corpora** — A US or EU court enters final judgment, or a lab announces a settlement, of >=$5B (2026 USD) arising from training-data copyright/IP claims; OR a court issues an injunction (not stayed within 90 days) barring a frontier lab from training on a major copyrighted corpus.
- **Grid emergency or load-shed event officially attributed in part to datacenter demand** — A US RTO/ISO, NERC, or a state utility commission issues an official finding that a load-shed event, EEA-2/EEA-3 emergency, or rolling blackout affecting >100,000 customers was caused in part by datacenter load growth.
- **Confirmed theft or leak of frontier model weights** — A frontier lab, a government agency, or two independent major outlets confirm that the full weights of a model within one generation of a Western frontier release were exfiltrated by an unauthorized party or publicly leaked.
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
| Civil war onset in a country of 50 million or more that was at peace in mid-2026 | 29% | 66% | 83% | [64%–98%] | 8 | 2029Q1 |
| AfD enters government at German federal or Land level | 13% | 49% | 72% | [51%–91%] | 7 | 2030Q2 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 14% | 43% | 61% | [38%–82%] | 8 | 2029Q4 |
| Single US political-violence attack killing ten or more people | 24% | 60% | 76% | [51%–97%] | 6 | 2029Q1 |
| Democrats control at least one chamber of Congress from January 2027 | 90% | 90% | 90% | [80%–97%] | 5 | 2026Q4 |
| A calendar year with three or more successful coups d'etat worldwide | 45% | 73% | 85% | [66%–98%] | 5 | 2027Q4 |
| Vladimir Putin ceases to be Russia's paramount leader | 6.8% | 25% | 50% | [24%–79%] | 8 | 2031Q4 |
| National Rally (or RN-aligned candidate) wins the French presidency | 36% | 36% | 52% | [25%–81%] | 7 | 2027Q2 |
| Saudi succession from King Salman | 37% | 78% | 91% | [57%–>99%] | 4 | 2028Q2 |
| Xi Jinping ceases to be CCP General Secretary | 3.8% | 14% | 38% | [9.3%–78%] | 9 | 2032Q4 |
| Criminal conviction of a major US opposition figure in a prosecution widely coded as politically motivated | 9.0% | 28% | 44% | [12%–87%] | 7 | 2030Q3 |
| The Islamic Republic of Iran ceases to exist as a governing system | 8.7% | 23% | 33% | [10%–71%] | 9 | 2030Q1 |
| Overt US military strike inside Mexican territory without Mexican consent | 24% | 35% | 39% | [16%–70%] | 7 | 2027Q3 |
| Nigerian 2027 general election breakdown | 6.6% | 22% | 39% | [9.5%–82%] | 7 | 2031Q1 |
| Major democratic rupture or mass communal violence in India | 5.9% | 20% | 33% | [5.3%–72%] | 8 | 2030Q4 |
| Reform UK leads a UK government | 2.8% | 28% | 39% | [11%–79%] | 6 | 2030Q2 |
| US President formally invokes the Insurrection Act over a state's objection | 23% | 32% | 37% | [16%–62%] | 6 | 2027Q3 |
| Contested certification of the 2028 US presidential election | 4.9% | 14% | 24% | [4.8%–60%] | 9 | 2030Q4 |
| Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice | 5.9% | 14% | 22% | [7.3%–40%] | 7 | 2030Q2 |
| US executive branch openly defies a final Supreme Court order | 6.3% | 11% | 15% | [1.9%–40%] | 9 | 2028Q4 |
| Global autocratization wave inflects | 8.7% | 29% | 49% | [13%–88%] | 2 | 2030Q4 |
| Trump formally pursues a third presidential term | 3.3% | 7.3% | 9.1% | [3.8%–16%] | 8 | 2029Q2 |
| An EU member state initiates exit from the EU | 1.5% | 5.8% | 8.2% | [4.0%–15%] | 8 | 2030Q2 |
| Armed confrontation between US state-controlled forces and federal forces | 2.6% | 5.9% | 8.0% | [1.2%–23%] | 8 | 2029Q4 |

<details><summary>Resolution criteria</summary>

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — A country with population of at least 50 million, not experiencing an armed conflict with at least 1,000 battle-related deaths in 2025, records at least 1,000 battle-related deaths in a single calendar year in an internal armed conflict, per UCDP/PRIO coding.
- **AfD enters government at German federal or Land level** — The AfD holds at least one ministerial post in a German federal or state (Land) government, or formally signs a written toleration/confidence-and-supply agreement supporting such a government. Issue-by-issue parliamentary cooperation does not count.
- **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** — In any V-Dem annual Democracy Report from 2027 through 2037, a NATO or EU member state that was coded as a liberal or electoral democracy in the 2026 report is coded as an electoral autocracy or closed autocracy. Turkey's and Hungary's pre-2026 coding do not qualify.
- **Single US political-violence attack killing ten or more people** — A single attack on US soil kills at least 10 people (excluding perpetrators) and is officially determined by federal law enforcement, or coded by START/GTD, as politically, religiously, racially or ideologically motivated. Ordinary criminal and non-ideological mass shootings excluded.
- **Democrats control at least one chamber of Congress from January 2027** — Following the 3 November 2026 elections, Democrats (including caucusing independents) hold a majority of seats in the US House and/or Senate when the new Congress convenes on 3 January 2027.
- **A calendar year with three or more successful coups d'etat worldwide** — In any single calendar year from 2026 onward, at least three successful coups d'etat occur globally, where 'successful' means the coup leadership holds effective power for at least seven days, per Powell-Thyne / Cline Center coding.
- **Vladimir Putin ceases to be Russia's paramount leader** — Putin is no longer president of Russia (or, if the office is restructured, no longer the recognized paramount decision-maker) for a continuous period exceeding 60 days, through death, incapacity, resignation, removal or coup.
- **National Rally (or RN-aligned candidate) wins the French presidency** — A candidate endorsed by, or a member of, Rassemblement National (or its formal successor) is elected President of France in the 2027 or 2032 presidential election and inaugurated.
- **Saudi succession from King Salman** — King Salman bin Abdulaziz (b. December 1935) ceases to be King of Saudi Arabia through death, incapacity or abdication, and a successor is proclaimed, by end-2031.
- **Xi Jinping ceases to be CCP General Secretary** — Xi Jinping is no longer General Secretary of the Chinese Communist Party for a continuous period exceeding 60 days, for any reason.
- **Criminal conviction of a major US opposition figure in a prosecution widely coded as politically motivated** — By end-2031, a sitting or former US governor, senator, House member in leadership, cabinet secretary, presidential nominee, or FBI/CIA director is convicted at trial in a federal prosecution that at least three of AP/Reuters/NYT/WSJ/WaPo characterize as politically motivated or retaliatory, or that Protect Democracy's Retaliatory Action Tracker records as such.
- **The Islamic Republic of Iran ceases to exist as a governing system** — A government controls Tehran that does not derive its authority from velayat-e faqih - the office of Supreme Leader is abolished, left vacant for more than 12 months with no successor, or subordinated to a non-clerical executive - sustained for at least 90 days.
- **Overt US military strike inside Mexican territory without Mexican consent** — The US government publicly acknowledges, or three major wire services confirm, a US military kinetic strike (manned aircraft, drone, missile or ground raid) on a target inside Mexican sovereign territory that the Mexican federal government publicly states it did not consent to.
- **Nigerian 2027 general election breakdown** — The February 2027 Nigerian general election produces at least 500 election-related deaths within 90 days of polling per ACLED, OR the presidential result is annulled or the transfer of power prevented or delayed beyond the 29 May 2027 inauguration date, OR the military intervenes in the transfer of power.
- **Major democratic rupture or mass communal violence in India** — By end-2031, either (a) V-Dem downgrades India from electoral autocracy to closed autocracy, or (b) India records at least 1,000 deaths in communal, sectarian or state-repression political violence in a single calendar year per ACLED or UCDP coding, or (c) a national election is postponed beyond its constitutional deadline or its result is not accepted by the losing coalition.
- **Reform UK leads a UK government** — A Reform UK MP is appointed Prime Minister of the United Kingdom.
- **US President formally invokes the Insurrection Act over a state's objection** — A presidential proclamation expressly invoking 10 U.S.C. sections 251-255 (the Insurrection Act) to deploy federal troops or federalized National Guard for domestic law enforcement inside a US state whose governor has publicly objected, confirmed by the Federal Register and major wire services.
- **Contested certification of the 2028 US presidential election** — Following the 7 November 2028 election, at least one state transmits competing slates of presidential electors to Congress, OR a state fails to certify by the Electoral Count Reform Act's safe-harbour deadline and the dispute reaches Congress or the Supreme Court, OR the joint session on 6 January 2029 sustains an objection to a state's electors.
- **Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice** — A sitting US president, vice president, member of the House or Senate, Senate-confirmed cabinet secretary, or Supreme Court justice is killed in an attack determined by federal law enforcement to be politically, ideologically or personally-grievance motivated. Natural death, accident and ordinary criminal robbery excluded.
- **US executive branch openly defies a final Supreme Court order** — The executive branch publicly and knowingly fails to comply with a final, non-stayed order of the US Supreme Court for more than 30 days, and this non-compliance is (a) asserted in a filing or opinion by the Court or a lower court on remand, or (b) reported as such by at least three of AP/Reuters/NYT/WSJ/WaPo. Slow-walking with a colorable legal argument does not count.
- **Global autocratization wave inflects** — In any V-Dem Democracy Report from 2028 through 2032, either the count of countries coded as currently autocratizing falls below 35, OR the number of democratizing countries exceeds the number autocratizing; alternatively, any Freedom in the World edition through 2032 records more countries improving than declining.
- **Trump formally pursues a third presidential term** — Donald Trump files FEC paperwork as a candidate for president in 2028, is placed on a primary ballot in any state as a presidential candidate, or is formally nominated as the Republican presidential or vice-presidential candidate for 2028.
- **An EU member state initiates exit from the EU** — An EU member state's government formally notifies the European Council under Article 50 TEU, or a nationally binding referendum on EU membership is held in a member state.
- **Armed confrontation between US state-controlled forces and federal forces** — A US governor issues an order directing state law enforcement or state-controlled National Guard to physically block or detain federal agents/troops, AND an armed confrontation occurs producing at least one death or at least one state officer detaining a federal officer (or vice versa) at gunpoint. Litigation, non-cooperation policies and protest-line scuffles do not count.

</details>

### Global macroeconomy & finance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Japan 10-year government bond yield reaches 3.00% | 57% | 75% | 93% | [53%–>99%] | 7 | 2027Q3 |
| Sustained effective closure of the Strait of Hormuz | 68% | 76% | 81% | [55%–98%] | 8 | 2026Q4 |
| US recession with NBER-dated peak in the window | 25% | 57% | 84% | [63%–98%] | 6 | 2029Q4 |
| China reports annual real GDP growth below 4.0% | 21% | 65% | 81% | [54%–97%] | 6 | 2029Q2 |
| Global recession (world real GDP growth below 2.0% in a calendar year) | 11% | 39% | 62% | [37%–85%] | 7 | 2030Q4 |
| Brent crude settles above $120/bbl | 40% | 60% | 71% | [38%–93%] | 6 | 2027Q4 |
| US Treasury market dysfunction requiring emergency Fed intervention | 9.1% | 32% | 52% | [19%–93%] | 8 | 2030Q4 |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 7.8% | 42% | 58% | [26%–92%] | 7 | 2030Q1 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 11% | 29% | 49% | [23%–75%] | 8 | 2030Q4 |
| S&P 500 falls 30%+ from its all-time closing high | 15% | 45% | 64% | [42%–87%] | 6 | 2030Q2 |
| Wave of emerging-market sovereign defaults or restructurings | 31% | 58% | 74% | [45%–91%] | 5 | 2028Q3 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 16% | 36% | 57% | [32%–81%] | 6 | 2030Q2 |
| Disorderly yen move | 12% | 37% | 55% | [19%–94%] | 6 | 2030Q2 |
| Disorderly broad dollar depreciation | 8.7% | 31% | 51% | [14%–91%] | 6 | 2030Q4 |
| US 10-year Treasury yield closes at or above 6.00% | 6.5% | 25% | 37% | [18%–59%] | 8 | 2030Q3 |
| US CPI inflation returns to 5.0%+ year over year | 21% | 42% | 55% | [27%–80%] | 5 | 2029Q1 |
| Formal breach of Federal Reserve independence | 6.8% | 21% | 38% | [12%–74%] | 7 | 2031Q2 |
| China announces a central-government property/LGFV rescue of RMB 5trn or more | 13% | 34% | 53% | [17%–85%] | 5 | 2030Q3 |
| US dollar share of allocated FX reserves falls below 50% | 2.1% | 24% | 44% | [19%–72%] | 6 | 2031Q3 |
| US average effective tariff rate exceeds 15% | 15% | 38% | 47% | [20%–80%] | 5 | 2029Q2 |
| Taiwan semiconductor supply disruption with global market resolution | 3.9% | 14% | 23% | [2.2%–58%] | 9 | 2030Q4 |
| Systemic financial market infrastructure outage | 4.5% | 16% | 30% | [6.1%–68%] | 7 | 2031Q3 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 5.2% | 16% | 24% | [2.9%–54%] | 7 | 2030Q2 |
| Major stablecoin failure or sustained depeg | 17% | 29% | 39% | [7.4%–77%] | 4 | 2028Q4 |
| US inflation undershoot / deflation scare | 5.2% | 19% | 36% | [9.1%–80%] | 4 | 2031Q3 |

<details><summary>Resolution criteria</summary>

- **Japan 10-year government bond yield reaches 3.00%** — The 10-year JGB benchmark yield closes at or above 3.00% on any day in the window.
- **Sustained effective closure of the Strait of Hormuz** — Seaborne crude and condensate transits through the Strait of Hormuz fall more than 50% below the 2025 monthly average for at least 14 consecutive days, per IEA, EIA, Kpler or Vortexa reporting, at any point from August 2026 onward.
- **US recession with NBER-dated peak in the window** — NBER Business Cycle Dating Committee assigns a business-cycle peak dated between August 2026 and the end of the stated year. Later announcement is fine; the peak date is what counts.
- **China reports annual real GDP growth below 4.0%** — China's National Bureau of Statistics reports full-year real GDP growth below 4.0% for any calendar year in the window, in the initial annual release.
- **Global recession (world real GDP growth below 2.0% in a calendar year)** — IMF WEO (October vintage of the following year) reports world real GDP growth at market or PPP weights below 2.0% for any calendar year in the window. Resolves YES on the first such year.
- **Brent crude settles above $120/bbl** — ICE Brent front-month futures settle at or above $120.00/bbl on any trading day in the window.
- **US Treasury market dysfunction requiring emergency Fed intervention** — The Federal Reserve announces unscheduled purchases of Treasury securities, a new or expanded standing repo/dealer facility, or explicit market-functioning operations (not policy QE and not routine reserve management) in response to disorderly conditions in the Treasury or repo market, at any point in the window.
- **AI capex bust: aggregate hyperscaler capex falls 20%+ year over year** — Combined calendar-year capital expenditure of Microsoft, Alphabet, Amazon, Meta and Oracle, as reported in audited annual filings, comes in at least 20% below the prior calendar year's reported total, for any year in the window.
- **Failure or extraordinary rescue of a bank with over $250bn in assets** — A bank holding company with more than $250bn in total assets in the US, EU, UK, Switzerland, Japan or China fails, is placed into resolution, is forced into a state-brokered merger, or receives an extraordinary government capital injection or central bank emergency liquidity facility created specifically for it.
- **S&P 500 falls 30%+ from its all-time closing high** — S&P 500 records a daily close at least 30% below its prior all-time closing high, at any point in the window.
- **Wave of emerging-market sovereign defaults or restructurings** — At least three additional sovereigns, each with more than $10bn in external public debt, default on external commercial debt or formally enter a comprehensive debt restructuring or a new IMF Extended Fund Facility of at least $3bn, between August 2026 and the end of the stated year.
- **Large private-credit vehicle suspends redemptions or enters wind-down** — A private credit fund, BDC or interval fund with at least $20bn NAV fully suspends redemptions (beyond pro-rating within stated quarterly limits) for at least one month, or is placed into wind-down or forced sale, in the US, UK or EU.
- **Disorderly yen move** — USD/JPY closes above 180, or moves more than 15 yen in either direction within any 20 trading days, in the window.
- **Disorderly broad dollar depreciation** — The Fed's broad nominal trade-weighted dollar index falls 20% or more from its trailing 24-month high within any 24-month period in the window.
- **US 10-year Treasury yield closes at or above 6.00%** — The constant-maturity 10-year US Treasury yield (H.15 / Treasury daily par yield curve) closes at or above 6.00% on any day in the window.
- **US CPI inflation returns to 5.0%+ year over year** — BLS reports headline CPI-U at or above 5.0% year over year for any single month in the window.
- **Formal breach of Federal Reserve independence** — A sitting US president attempts to remove or demote a Federal Reserve governor or the chair for policy reasons, issues a directive on the policy rate that the Board acts on, or legislation altering the FOMC's control of the policy rate is enacted — any one, in the window.
- **China announces a central-government property/LGFV rescue of RMB 5trn or more** — China's State Council, MOF or PBOC announces a single package of central-government fiscal support, debt assumption or recapitalization directed at the property sector and/or local government financing vehicles totalling at least RMB 5 trillion, announced as one program.
- **US dollar share of allocated FX reserves falls below 50%** — IMF COFER reports the US dollar share of allocated global foreign exchange reserves below 50.0% for any quarter in the window.
- **US average effective tariff rate exceeds 15%** — Penn Wharton Budget Model or Yale Budget Lab reports a US average effective tariff rate on all imports above 15.0% for at least one full month in the window.
- **Taiwan semiconductor supply disruption with global market resolution** — Monthly semiconductor exports from Taiwan fall more than 40% below the trailing twelve-month average for two consecutive months, for any reason (blockade, quarantine, conflict, or major natural disaster), in the window.
- **Systemic financial market infrastructure outage** — A systemically important FMI — a major CCP, CLS, DTCC, Fedwire, TARGET2, SWIFT, or a top-three custodian — suffers an outage or compromise preventing settlement for more than 24 hours, or a central bank extends emergency liquidity explicitly because of it.
- **France or Italy 10-year spread over Bunds exceeds 300bp** — The 10-year OAT-Bund or BTP-Bund spread closes above 300 basis points for five consecutive trading days, or the ECB formally activates the Transmission Protection Instrument for either sovereign.
- **Major stablecoin failure or sustained depeg** — A stablecoin with at least $20bn market capitalization trades more than 5% below its peg for more than 24 consecutive hours, or its issuer suspends or fails to honor redemptions for more than 24 hours.
- **US inflation undershoot / deflation scare** — US core PCE inflation prints below 1.0% year over year for three consecutive months, or headline CPI-U prints negative year over year for any month, in the window.

</details>

### Great-power conflict & geopolitics

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 62% | 74% | 78% | [45%–98%] | 8 | 2027Q1 |
| Durable Russia-Ukraine ceasefire (>=180 consecutive days) | 34% | 69% | 86% | [63%–98%] | 7 | 2028Q3 |
| Renewed major US and/or Israeli air campaign against Iran | 18% | 55% | 83% | [49%–99%] | 7 | 2030Q1 |
| A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test | 17% | 45% | 66% | [25%–98%] | 8 | 2029Q4 |
| A second US kinetic operation to remove or kill a sitting foreign head of state or government | 14% | 39% | 63% | [22%–98%] | 7 | 2030Q2 |
| PRC forces cause the death of a Philippine serviceman or coast guardsman | 13% | 40% | 59% | [18%–98%] | 7 | 2030Q1 |
| Iran formally withdraws from the Nuclear Non-Proliferation Treaty | 16% | 47% | 68% | [28%–98%] | 6 | 2029Q4 |
| Vladimir Putin ceases to hold effective power in Russia | 7.9% | 26% | 49% | [13%–90%] | 8 | 2031Q3 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 6.3% | 23% | 42% | [17%–69%] | 8 | 2031Q3 |
| New US-Russia agreement capping deployed strategic nuclear warheads | 21% | 40% | 52% | [17%–86%] | 6 | 2029Q1 |
| Lethal DPRK-ROK military exchange | 9.3% | 29% | 49% | [16%–90%] | 6 | 2030Q4 |
| The Islamic Republic ceases to govern Iran | 9.5% | 24% | 33% | [9.3%–69%] | 8 | 2029Q4 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 5.0% | 18% | 27% | [11%–48%] | 9 | 2030Q2 |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 3.7% | 15% | 28% | [2.7%–59%] | 8 | 2031Q2 |
| India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months | 5.5% | 17% | 27% | [9.2%–52%] | 8 | 2030Q4 |
| North Korea conducts a seventh nuclear explosive test | 9.6% | 29% | 43% | [22%–70%] | 5 | 2030Q2 |
| PRC seizes or occupies a Taiwan-administered offshore island | 3.6% | 14% | 24% | [5.5%–56%] | 7 | 2031Q1 |
| Lethal armed clash between Chinese and Japanese state forces | 3.1% | 11% | 18% | [2.6%–46%] | 8 | 2031Q1 |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 2.7% | 9.5% | 18% | [2.0%–45%] | 7 | 2031Q4 |
| NATO invokes Article 5 in response to a Russian attack | 3.5% | 7.6% | 12% | [4.1%–24%] | 10 | 2030Q1 |
| A jihadist insurgent group controls a Sahelian national capital for >=7 days | 7.0% | 18% | 24% | [8.9%–44%] | 5 | 2029Q3 |
| Direct US-PRC military exchange causing at least one fatality | 2.8% | 7.3% | 13% | [4.8%–25%] | 9 | 2031Q2 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 1.8% | 4.9% | 12% | [4.3%–21%] | 10 | 2032Q3 |
| US initiates withdrawal from NATO, or any member formally invokes Article 13 | 2.3% | 5.5% | 9.7% | [2.7%–22%] | 9 | 2031Q1 |
| A nuclear weapon is detonated in an act of war or hostility anywhere in the world | 0.7% | 3.2% | 5.6% | [2.3%–13%] | 10 | 2031Q2 |
| UN Security Council permanent membership formally expanded | 0.6% | 1.6% | 3.3% | [3.3%–3.3%] | 3 | 2032Q1 |

<details><summary>Resolution criteria</summary>

- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — Crude-plus-condensate transit through Hormuz, per EIA/Vortexa/Kpler monthly data, falls below 50% of the 2025 monthly average for at least 30 consecutive days, in an episode beginning on or after 1 August 2026.
- **Durable Russia-Ukraine ceasefire (>=180 consecutive days)** — A ceasefire covering the entire land front between Russian and Ukrainian forces holds for at least 180 consecutive days without resumption of sustained offensive ground operations or systematic long-range strikes on cities, as assessed by ISW/OSCE-successor monitoring or equivalent consensus reporting. Short holiday truces (e.g. April/May 2026) do NOT count.
- **Renewed major US and/or Israeli air campaign against Iran** — At least 100 US and/or Israeli strikes on targets inside Iran within any 30-day window beginning on or after 1 August 2026, per credible multi-source reporting or US/Israeli government statement.
- **A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test** — The United States, Russia or China conducts a supercritical nuclear explosive test (yield above zero, excluding subcritical and hydrodynamic experiments), confirmed by the testing state or by CTBTO/national technical means.
- **A second US kinetic operation to remove or kill a sitting foreign head of state or government** — US forces, after 1 August 2026, conduct a military operation that captures, kills, or directly precipitates within 30 days the removal from power of the sitting head of state or government of a UN member state, excluding the January 2026 Venezuela and February 2026 Iran operations.
- **PRC forces cause the death of a Philippine serviceman or coast guardsman** — An action by PLA, PLAN, China Coast Guard or maritime-militia units (including ramming, water cannon, boarding or fire) directly causes at least one death among Philippine armed forces, coast guard or government-chartered personnel, confirmed by the Philippine government.
- **Iran formally withdraws from the Nuclear Non-Proliferation Treaty** — Iran deposits formal notice of withdrawal under NPT Article X with the depositary governments and the UN Security Council, or that withdrawal takes effect.
- **Vladimir Putin ceases to hold effective power in Russia** — Putin ceases to serve as President of the Russian Federation, or is assessed by consensus of major-power governments no longer to exercise effective control over Russian state decision-making, for any reason including death, incapacity, resignation or removal.
- **A state that does not now possess nuclear weapons tests a device or is confirmed to possess one** — Any state other than the US, Russia, UK, France, China, India, Pakistan, Israel and North Korea either (a) conducts a nuclear explosive test, (b) officially declares possession of an assembled nuclear weapon, or (c) is assessed by the IAEA or by the US intelligence community in a public statement to possess one.
- **New US-Russia agreement capping deployed strategic nuclear warheads** — The US and Russia sign a bilateral agreement (treaty, executive agreement, or formal reciprocal political commitment announced by both heads of state) that establishes a numerical ceiling on deployed strategic nuclear warheads or delivery vehicles.
- **Lethal DPRK-ROK military exchange** — An exchange of fire or attack between DPRK and ROK forces causing at least five combined military or civilian deaths, confirmed by either government or by the UN Command.
- **The Islamic Republic ceases to govern Iran** — The office of Supreme Leader (Velayat-e Faqih) is abolished, vacated without a successor for more than 90 days, or a government not derived from the clerical/IRGC establishment exercises effective control of Tehran; as assessed by consensus of major-power governments.
- **PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days** — PRC state organs (PLA, Coast Guard or maritime authorities) publicly declare a quarantine, inspection regime or blockade of Taiwan's ports/airspace AND enforce it by boarding, turning back or interdicting at least ten commercial vessels or aircraft, sustained for at least seven consecutive days.
- **Iran tests or is confirmed to possess an assembled nuclear weapon** — Iran conducts a nuclear explosive test, publicly declares possession, or is publicly assessed by the IAEA or the US intelligence community to possess at least one assembled nuclear weapon.
- **India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months** — Direct state-on-state armed conflict between Indian and Pakistani forces producing at least 1,000 combined military and civilian deaths within any rolling 12-month period, per UCDP or ACLED coding.
- **North Korea conducts a seventh nuclear explosive test** — A nuclear explosive test on DPRK territory confirmed by CTBTO seismic/radionuclide detection or by US/ROK/Japanese government statement.
- **PRC seizes or occupies a Taiwan-administered offshore island** — PLA, PAP or China Coast Guard forces land on and establish administrative or military control over Pratas (Dongsha), Taiping (Itu Aba), Kinmen, Matsu or Wuqiu, maintained for at least 72 consecutive hours, confirmed by Taiwan MND or US government statement.
- **Lethal armed clash between Chinese and Japanese state forces** — An exchange of fire or deliberate ramming between PLA/CCG and JSDF/JCG units resulting in at least one death, confirmed by either government.
- **State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country** — A cyberattack publicly attributed by the victim government or by the EU/NATO to a state or state-sponsored actor causes loss of electrical supply to at least one million people for at least 24 consecutive hours in a NATO or OECD member state.
- **NATO invokes Article 5 in response to a Russian attack** — The North Atlantic Council formally invokes Article 5 of the Washington Treaty citing an armed attack attributable to Russia or Belarus.
- **A jihadist insurgent group controls a Sahelian national capital for >=7 days** — JNIM, ISSP/ISWAP or a successor jihadist organisation exercises effective control of Bamako, Ouagadougou or Niamey (including the presidential palace and central districts) for at least seven consecutive days, per ACLED coding or UN/Security Council reporting.
- **Direct US-PRC military exchange causing at least one fatality** — An exchange of fire (kinetic, including missile, air, naval or ground fire) between US and PLA/PAP/China Coast Guard forces resulting in at least one death on either side, acknowledged by either government or confirmed by credible multi-source reporting.
- **PRC launches an amphibious or airborne assault on Taiwan's main island** — PLA forces conduct an opposed landing or airborne insertion on Taiwan proper (not offshore islands) involving at least 1,000 personnel, confirmed by Taiwan MND or US government statement.
- **US initiates withdrawal from NATO, or any member formally invokes Article 13** — The US President formally notifies the depositary of intent to withdraw under Article 13 of the North Atlantic Treaty, or any other member state does so.
- **A nuclear weapon is detonated in an act of war or hostility anywhere in the world** — A nuclear explosive device is detonated with hostile intent against a state, non-state actor or territory (excluding tests, accidents and demonstration detonations over unpopulated own territory), confirmed by the detonating state or by CTBTO/national technical means.
- **UN Security Council permanent membership formally expanded** — An amendment to the UN Charter expanding the number of permanent Security Council members enters into force following ratification by two-thirds of member states including all five current permanent members.

</details>

### Climate & Earth systems

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | 88% | 93% | 98% | [93%–99%] | 6 | 2027Q1 |
| Disintegration of the Thwaites Eastern Ice Shelf | 9.8% | 35% | 61% | [22%–97%] | 8 | 2031Q1 |
| Global fossil CO2 emissions confirmed to have peaked | 9.3% | 36% | 69% | [38%–91%] | 7 | 2031Q3 |
| FAO Food Price Index exceeds 160 in any month | 14% | 44% | 70% | [38%–92%] | 6 | 2030Q3 |
| Long-term (multi-decadal) 1.5C breach formally declared | 5.2% | 42% | 84% | [60%–97%] | 5 | 2031Q4 |
| New record-low Antarctic sea ice minimum extent | 15% | 43% | 67% | [26%–98%] | 6 | 2030Q1 |
| A calendar year at or above 1.65C above pre-industrial | 62% | 91% | 97% | [87%–>99%] | 4 | 2027Q2 |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | 71% | 74% | 75% | [56%–95%] | 5 | 2027Q1 |
| Global insured natural catastrophe losses exceed $200bn in a calendar year | 13% | 40% | 62% | [22%–98%] | 6 | 2030Q2 |
| Combined Lake Powell + Lake Mead storage falls below 20% of capacity | 20% | 42% | 62% | [35%–86%] | 5 | 2029Q4 |
| Single heat event with >= 100,000 attributed excess deaths | 9.3% | 25% | 43% | [23%–67%] | 7 | 2031Q1 |
| A new record warmest calendar year, exceeding 2024 | 78% | 94% | 99% | [97%–99%] | 3 | 2027Q2 |
| A second G20 economy formally withdraws from the Paris Agreement | 6.5% | 22% | 39% | [8.9%–84%] | 7 | 2031Q1 |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 5.8% | 21% | 37% | [18%–67%] | 6 | 2031Q2 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 1.8% | 14% | 26% | [1.8%–65%] | 8 | 2031Q3 |
| Formal international SRM governance decision adopted | 15% | 33% | 41% | [9.8%–82%] | 4 | 2029Q1 |
| Final court judgment ordering >= $1bn in climate damages | 1.4% | 10% | 26% | [6.1%–57%] | 6 | 2032Q3 |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 4.0% | 9.2% | 16% | [2.1%–42%] | 8 | 2031Q2 |
| VEI 6+ volcanic eruption with measurable global cooling | 2.9% | 9.6% | 18% | [2.3%–44%] | 5 | 2031Q2 |
| State-backed solar radiation management deployment announced or conducted | 0.8% | 6.3% | 11% | [2.0%–26%] | 8 | 2031Q1 |
| Global mean methane annual growth rate falls to zero or below | 1.8% | 7.3% | 15% | [1.8%–37%] | 5 | 2032Q1 |
| AMOC declared to have crossed a tipping point | 0.5% | 2.3% | 5.0% | [1.4%–14%] | 10 | 2032Q3 |
| Arctic Ocean practically ice-free (extent below 1.0 million km2) | <0.5% | 1.7% | 8.5% | [1.9%–32%] | 5 | 2033Q4 |

<details><summary>Resolution criteria</summary>

- **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** — NOAA Coral Reef Watch reports that Alert Level 1 or higher bleaching-level heat stress affected at least 60% of the world's coral reef area within any rolling 12-month period.
- **Disintegration of the Thwaites Eastern Ice Shelf** — Satellite observation (ESA/NASA, confirmed by NSIDC or a peer-reviewed publication) shows the Thwaites Eastern Ice Shelf has lost at least 50% of its 2020 area through fracture and calving within a three-year period.
- **Global fossil CO2 emissions confirmed to have peaked** — The Global Carbon Project reports global fossil CO2 emissions below the previous all-time high in two consecutive calendar years, with the peak year identified in the published Global Carbon Budget.
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
- **Final court judgment ordering >= $1bn in climate damages** — A court of final instance (highest domestic court, or a binding international tribunal) issues a non-appealable judgment ordering a state or a company to pay at least US$1 billion in damages, compensation, or a compliance fund specifically for climate change harms.
- **Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months** — The RAPID-MOCHA-WBTS array at 26N (or a successor observing system accepted as the reference by the AMOC research community) reports a 12-month running mean overturning transport at least 30% below the 2004-2023 mean, confirmed in a peer-reviewed publication.
- **VEI 6+ volcanic eruption with measurable global cooling** — A volcanic eruption of VEI 6 or greater (Smithsonian GVP classification) injects sufficient stratospheric sulphate that WMO, NASA GISS or Copernicus attributes at least 0.1C of global mean cooling to it in the following one to two years.
- **State-backed solar radiation management deployment announced or conducted** — A national government formally announces a stratospheric aerosol injection deployment programme (as distinct from research), or a state or state-backed entity conducts SAI at a scale exceeding 0.1 Tg of injected aerosol precursor per year, as confirmed by independent monitoring or official statement.
- **Global mean methane annual growth rate falls to zero or below** — NOAA GML reports a global mean CH4 annual increase of 0.0 ppb or less for a calendar year in its published trends series.
- **AMOC declared to have crossed a tipping point** — A major assessment body (IPCC, WMO, or a National Academies-equivalent) or a strong majority of the published AMOC literature states that the AMOC has crossed a critical threshold and is on an irreversible trajectory toward collapse (maximum strength below 5 Sv) under current forcing.
- **Arctic Ocean practically ice-free (extent below 1.0 million km2)** — NSIDC daily sea ice extent for the Arctic falls below 1.0 million km2 on at least one day.

</details>

### israel

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| New round of major direct Israel-Iran exchange | 54% | 77% | 84% | [63%–98%] | 7 | 2027Q3 |
| Sustained Bab el-Mandeb / Red Sea shipping disruption | 54% | 72% | 78% | [54%–97%] | 6 | 2027Q3 |
| Resumption of major Israeli hostilities in Gaza | 31% | 58% | 69% | [35%–92%] | 5 | 2028Q2 |
| Full Israel-Saudi normalisation | 15% | 44% | 56% | [32%–83%] | 6 | 2029Q2 |
| Israel-Syria security agreement signed | 35% | 55% | 61% | [34%–89%] | 5 | 2027Q4 |
| New major Israel-Hezbollah war round | 22% | 48% | 60% | [34%–87%] | 5 | 2029Q1 |
| Major intra-Palestinian armed conflict | 34% | 59% | 67% | [39%–89%] | 4 | 2027Q4 |
| US suspension of a major arms category to Israel | 8.6% | 28% | 39% | [18%–68%] | 6 | 2030Q2 |
| New IPC Famine classification in Gaza | 15% | 31% | 38% | [16%–69%] | 5 | 2028Q4 |
| Functional collapse of the Palestinian Authority | 8.8% | 26% | 35% | [14%–59%] | 5 | 2030Q1 |
| Adverse ICJ merits ruling on the Genocide Convention | 2.1% | 16% | 35% | [7.8%–70%] | 5 | 2032Q2 |
| Gaza peace-plan phase 2 substantively implemented | 13% | 32% | 43% | [7.1%–87%] | 4 | 2029Q3 |
| De jure Israeli annexation of West Bank territory | 7.3% | 20% | 28% | [12%–52%] | 6 | 2030Q1 |
| Ten billion dollars of Gaza reconstruction actually disbursed | 5.3% | 26% | 41% | [10%–86%] | 4 | 2030Q3 |
| Israeli constitutional crisis over defiance of the High Court | 18% | 32% | 39% | [14%–68%] | 4 | 2028Q2 |
| Third-Intifada-scale violence in the West Bank | 7.7% | 21% | 30% | [11%–53%] | 5 | 2030Q1 |
| Direct Israel-Turkey military clash | 6.4% | 17% | 22% | [2.1%–56%] | 6 | 2029Q4 |
| Mass permanent departure of Gazans | 6.3% | 15% | 20% | [4.7%–46%] | 6 | 2029Q3 |
| Israel-Lebanon peace treaty with diplomatic relations | 5.0% | 16% | 24% | [4.9%–56%] | 5 | 2030Q3 |
| Hezbollah disarmament certified complete | 7.9% | 20% | 27% | [7.3%–63%] | 4 | 2029Q4 |
| Rupture of the Egyptian or Jordanian peace treaty | 4.3% | 11% | 17% | [5.9%–29%] | 6 | 2030Q3 |
| Israel abandons nuclear opacity | 0.8% | 2.5% | 4.3% | [2.1%–8.6%] | 8 | 2031Q3 |

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
- **Functional collapse of the Palestinian Authority** — The PA either formally dissolves, or fails to pay ≥2 consecutive months of civil-service salaries while losing effective security control of ≥2 governorate capitals to non-PA armed actors, sustained ≥90 days.
- **Adverse ICJ merits ruling on the Genocide Convention** — The ICJ issues a final judgment on the merits in South Africa v. Israel finding Israel in breach of one or more obligations under the Genocide Convention.
- **Gaza peace-plan phase 2 substantively implemented** — By the horizon date, ≥5,000 ISF personnel deployed inside Gaza simultaneously AND the Board of Peace or ISF command publicly certifies that decommissioning of Hamas heavy weapons (crew-served and above) has begun.
- **De jure Israeli annexation of West Bank territory** — The Knesset enacts in third reading, and the government brings into force, legislation applying Israeli sovereignty, law and administration to territory in the West Bank beyond the 1967 East Jerusalem municipal boundary.
- **Ten billion dollars of Gaza reconstruction actually disbursed** — Cumulative external reconstruction and recovery financing disbursed (not pledged) for Gaza reaches US$10bn in 2026 dollars, per World Bank, Board of Peace or Palestine Donor Group reporting.
- **Israeli constitutional crisis over defiance of the High Court** — The Israeli government formally announces non-compliance with a binding High Court of Justice ruling, or removes the Attorney General or a Supreme Court justice in defiance of a court injunction, with the non-compliance persisting ≥60 days.
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
| China annual births fall below 7.0 million | 45% | 96% | 98% | [91%–99%] | 6 | 2028Q1 |
| China's officially reported population falls below 1.400 billion | 58% | 96% | 98% | [94%–99%] | 5 | 2027Q3 |
| Next UN WPP revision moves peak world population below 10.0 billion or earlier than 2070 | 23% | 62% | 85% | [48%–99%] | 5 | 2029Q2 |
| Best-available global TFR estimate falls below 2.1 | 4.3% | 33% | 60% | [15%–98%] | 7 | 2031Q2 |
| PISA 2025 shows no recovery in OECD-average mathematics | 68% | 68% | 68% | [43%–89%] | 6 | 2026Q4 |
| US removals plus returns exceed one million in a fiscal year | 11% | 40% | 65% | [26%–98%] | 6 | 2030Q3 |
| India enacts reapportionment of Lok Sabha seats on post-2026 census population | 9.7% | 34% | 55% | [20%–91%] | 7 | 2030Q3 |
| Japan annual births (Japanese nationals) fall below 600,000 | 39% | 93% | 96% | [83%–99%] | 4 | 2028Q1 |
| US total fertility rate falls below 1.50 | 3.9% | 47% | 76% | [46%–97%] | 5 | 2030Q4 |
| India publishes provisional Census 2027 population totals | 53% | 91% | 94% | [80%–99%] | 4 | 2027Q3 |
| Two million or more Ukrainian refugees return to Ukraine | 14% | 41% | 67% | [28%–98%] | 5 | 2030Q3 |
| US life expectancy at birth reaches 80.0 years | 19% | 57% | 84% | [40%–99%] | 4 | 2029Q3 |
| Global forced displacement exceeds 130 million | 11% | 31% | 54% | [26%–78%] | 6 | 2031Q1 |
| US Census Bureau officially reports negative net international migration | 25% | 44% | 54% | [14%–94%] | 6 | 2028Q2 |
| Remittances to low- and middle-income countries fall 10% or more year-on-year | 8.0% | 27% | 47% | [14%–84%] | 6 | 2031Q1 |
| EU return hubs operationalized at scale | 12% | 33% | 49% | [16%–86%] | 5 | 2030Q1 |
| Global life expectancy falls by 0.5 years or more in a single year | 4.7% | 15% | 29% | [5.5%–59%] | 8 | 2031Q3 |
| Youth-led protests topple three or more Sub-Saharan African governments in a three-year window | 6.2% | 32% | 45% | [13%–80%] | 5 | 2030Q2 |
| Nigeria completes a national census and the result diverges more than 10% from the prior UN estimate | 5.4% | 20% | 34% | [8.9%–76%] | 6 | 2031Q1 |
| A G7 country cuts permanent immigration by three quarters | 4.3% | 22% | 28% | [2.3%–62%] | 7 | 2029Q3 |
| South Korea total fertility rate reaches 1.00 or above | 2.8% | 21% | 36% | [13%–58%] | 4 | 2031Q2 |
| China's population is revised down by 15 million or more | 3.5% | 17% | 24% | [6.1%–50%] | 6 | 2030Q2 |
| Gulf Cooperation Council migrant worker stock falls 15% or more from its peak | 4.0% | 14% | 23% | [5.1%–51%] | 6 | 2031Q1 |
| China's direct birth and childcare subsidies reach 0.5% of GDP | 2.8% | 17% | 29% | [8.2%–58%] | 4 | 2031Q1 |

<details><summary>Resolution criteria</summary>

- **China annual births fall below 7.0 million** — China's National Bureau of Statistics reports annual births below 7,000,000 for any calendar year, in its regular January statistical communique or the annual Statistical Yearbook.
- **China's officially reported population falls below 1.400 billion** — NBS reports a year-end national population (mainland, excluding HK/Macau/Taiwan) below 1,400 million.
- **Next UN WPP revision moves peak world population below 10.0 billion or earlier than 2070** — A UN DESA World Population Prospects revision published after July 2026 reports a medium-variant peak world population below 10,000,000,000, or a medium-variant peak year earlier than 2070.
- **Best-available global TFR estimate falls below 2.1** — A UN DESA World Population Prospects revision (or UN Population Division estimate) reports a global total fertility rate below 2.10 for the then-current year.
- **PISA 2025 shows no recovery in OECD-average mathematics** — OECD PISA 2025 results report an OECD-average mathematics score equal to or below the PISA 2022 OECD-average mathematics score (472 points).
- **US removals plus returns exceed one million in a fiscal year** — DHS Office of Homeland Security Statistics (or ICE/CBP annual reporting) reports combined removals, returns, and expulsions exceeding 1,000,000 for a single fiscal year.
- **India enacts reapportionment of Lok Sabha seats on post-2026 census population** — India enacts a constitutional amendment or Delimitation Act fixing revised Lok Sabha seat allocations across states based on Census 2027 (or later) population figures.
- **Japan annual births (Japanese nationals) fall below 600,000** — Japan's MHLW Vital Statistics report annual births to Japanese nationals below 600,000 for any calendar year, in preliminary or final figures.
- **US total fertility rate falls below 1.50** — CDC/NCHS reports a US total fertility rate below 1,500 births per 1,000 women (i.e. TFR < 1.50) for any calendar year, provisional or final.
- **India publishes provisional Census 2027 population totals** — The Registrar General and Census Commissioner of India publishes provisional population totals from Census 2027, covering the population enumeration phase with a reference date of 1 March 2027.
- **Two million or more Ukrainian refugees return to Ukraine** — UNHCR reports cumulative refugee returns to Ukraine of 2,000,000 or more since the reporting baseline, or reports the Ukrainian refugee population in Europe falling by 2,000,000 or more from its peak.
- **US life expectancy at birth reaches 80.0 years** — NCHS reports US period life expectancy at birth of 80.0 years or more for a single calendar year, in final or provisional mortality reports.
- **Global forced displacement exceeds 130 million** — UNHCR Global Trends (or Mid-Year Trends) reports total forcibly displaced persons exceeding 130,000,000 at any reporting date.
- **US Census Bureau officially reports negative net international migration** — A Census Bureau Vintage population estimates release (or an official Census Bureau revision) reports negative net international migration for any 12-month estimating period.
- **Remittances to low- and middle-income countries fall 10% or more year-on-year** — World Bank / KNOMAD reports nominal USD remittance flows to low- and middle-income countries declining 10% or more versus the prior year.
- **EU return hubs operationalized at scale** — At least three EU member states have transferred a cumulative total of 1,000 or more rejected asylum applicants or asylum seekers to designated 'return hubs' or processing centres in non-EU third countries under the Returns Regulation or bilateral arrangements, as documented by the European Commission, EUAA, or a major NGO monitor.
- **Global life expectancy falls by 0.5 years or more in a single year** — UN WPP, IHME GBD, or WHO reports global period life expectancy at birth declining by 0.5 years or more relative to the prior year.
- **Youth-led protests topple three or more Sub-Saharan African governments in a three-year window** — In any rolling 36-month window, heads of state or heads of government in three or more Sub-Saharan African countries resign, are removed, or flee within 90 days of the onset of mass protests that contemporaneous major-outlet reporting characterizes as youth-led or 'Gen Z' protests.
- **Nigeria completes a national census and the result diverges more than 10% from the prior UN estimate** — Nigeria's National Population Commission publishes national population totals from a census conducted after 2006, and the figure differs by more than 10% from the UN WPP estimate for Nigeria published immediately prior.
- **A G7 country cuts permanent immigration by three quarters** — A G7 member's official annual permanent-residence/settlement admissions (e.g. US lawful permanent residents, Canada PR admissions, UK settlement grants) fall below 25% of that country's 2024 level for a full fiscal or calendar year, per the responsible national agency.
- **South Korea total fertility rate reaches 1.00 or above** — Statistics Korea reports an annual total fertility rate of 1.00 or higher for any calendar year.
- **China's population is revised down by 15 million or more** — An official Chinese government source (NBS communique, the 2030 national census, or a published statistical yearbook revision) reports a national population figure at least 15,000,000 below the previously published estimate for a comparable date.
- **Gulf Cooperation Council migrant worker stock falls 15% or more from its peak** — UN DESA International Migrant Stock estimates, or combined national labour-force statistics for Saudi Arabia, UAE, Qatar, Kuwait, Oman and Bahrain, show the foreign-born or non-national workforce at least 15% below its post-2020 peak.
- **China's direct birth and childcare subsidies reach 0.5% of GDP** — Combined central and local government direct cash transfers for childbirth and childcare in China exceed 0.5% of nominal GDP in a single fiscal year, per Ministry of Finance budget documents or credible reporting aggregating central and provincial outlays.

</details>

### Energy systems & critical materials

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China's extraterritorial rare-earth export control regime enters into force | 45% | 77% | 83% | [57%–98%] | 7 | 2027Q4 |
| Strait of Hormuz closed again for 14+ consecutive days | 55% | 61% | 66% | [33%–87%] | 8 | 2027Q2 |
| Qatari LNG force majeure removing 15%+ of global LNG supply for 60+ days | 22% | 56% | 76% | [40%–99%] | 6 | 2029Q2 |
| Loss of Russian uranium enrichment and conversion services to Western utilities | 14% | 40% | 60% | [21%–98%] | 7 | 2030Q1 |
| Major producing state imposes an export ban or nationalisation on a critical mineral | 16% | 47% | 69% | [32%–98%] | 6 | 2030Q1 |
| Grid equipment supply chain forces cancellation or multi-year deferral of major interconnection programmes | 17% | 57% | 83% | [44%–99%] | 5 | 2029Q4 |
| Brent monthly average above $120/bbl | 36% | 57% | 69% | [35%–90%] | 6 | 2027Q4 |
| Severe rare-earth supply cutoff to the US or EU | 26% | 43% | 51% | [17%–82%] | 8 | 2027Q4 |
| China energy-related CO2 emissions decline three consecutive years | 3.6% | 42% | 71% | [32%–98%] | 5 | 2031Q1 |
| EU ETS2 delayed, price-capped or materially diluted | 23% | 62% | 85% | [52%–99%] | 4 | 2029Q2 |
| US data-center electricity demand growth collapses | 10% | 34% | 54% | [19%–92%] | 6 | 2030Q4 |
| Global oil demand declines year-on-year outside recession or supply shock | 5.4% | 35% | 64% | [24%–98%] | 5 | 2031Q2 |
| Inverter-driven systemic grid collapse in a major OECD system | 7.7% | 29% | 50% | [16%–89%] | 6 | 2031Q1 |
| LME copper exceeds $15,000/tonne | 12% | 38% | 54% | [17%–90%] | 5 | 2029Q4 |
| A Western SMR delivers first commercial grid power | 3.9% | 64% | 89% | [72%–98%] | 3 | 2030Q1 |
| European gas price returns to crisis levels | 31% | 43% | 49% | [21%–75%] | 5 | 2027Q3 |
| Firm load shedding in a major US RTO | 18% | 47% | 61% | [37%–87%] | 4 | 2029Q2 |
| Global coal demand falls 3%+ below the 2025 level | 7.7% | 48% | 73% | [46%–97%] | 3 | 2030Q3 |
| Lithium carbonate price exceeds $40,000/tonne | 14% | 35% | 44% | [13%–86%] | 4 | 2029Q2 |
| Brent monthly average below $45/bbl | 9.1% | 36% | 44% | [24%–71%] | 4 | 2029Q2 |
| Cyberattack causes a major OECD power outage | 5.0% | 15% | 27% | [7.0%–64%] | 6 | 2031Q3 |
| Annual global solar PV installations exceed 1,000 GW | 5.8% | 40% | 73% | [46%–97%] | 2 | 2031Q3 |
| Nuclear accident rated INES Level 5 or above | 5.5% | 11% | 19% | [3.8%–39%] | 6 | 2030Q4 |
| Coordinated physical attack causes a major OECD outage | 4.9% | 14% | 22% | [5.2%–61%] | 5 | 2030Q3 |
| Global installed water electrolysis capacity reaches 25 GW | 1.6% | 18% | 49% | [23%–77%] | 2 | 2032Q4 |

<details><summary>Resolution criteria</summary>

- **China's extraterritorial rare-earth export control regime enters into force** — The October 2025 expanded rare-earth export control measures (extraterritorial 0.1% de minimis provisions and expanded element list) are in legal force and being applied to licence applications for at least 30 consecutive days, per MOFCOM announcements, at any point before the stated year-end.
- **Strait of Hormuz closed again for 14+ consecutive days** — Commercial tanker transits through the Strait of Hormuz fall below 25% of the 2025 daily average for 14 or more consecutive days, per Lloyd's List / Kpler / IEA Oil Market Report tracking, at any point after 1 Aug 2026.
- **Qatari LNG force majeure removing 15%+ of global LNG supply for 60+ days** — QatarEnergy declares force majeure or otherwise suspends loadings such that Qatari LNG exports fall below 40% of their 2025 monthly average for 60 or more consecutive days, per Kpler/ICIS tracking, at any point after 1 Aug 2026.
- **Loss of Russian uranium enrichment and conversion services to Western utilities** — Rosatom/TENEX deliveries of enrichment (SWU) or conversion services to US and EU utilities fall by more than 70% year-on-year for four or more consecutive quarters, whether by sanction, counter-sanction or contract termination, per Euratom Supply Agency and US DOE/EIA reporting.
- **Major producing state imposes an export ban or nationalisation on a critical mineral** — A country accounting for 20% or more of global mined supply of lithium, cobalt, nickel, copper or rare earths imposes an export ban, export quota cut of 30%+, or nationalisation/forced-equity measure that removes 15% or more of global supply for 3+ months.
- **Grid equipment supply chain forces cancellation or multi-year deferral of major interconnection programmes** — A G7 transmission system operator or major US RTO publicly defers or cancels 10 GW or more of already-approved interconnection or transmission capacity, citing large power transformer, HVDC converter or gas turbine unavailability as the stated primary cause.
- **Brent monthly average above $120/bbl** — The calendar-month average of front-month Brent futures settlements exceeds $120.00/bbl (nominal USD) in any month after 1 Aug 2026, per ICE settlement data.
- **Severe rare-earth supply cutoff to the US or EU** — Chinese exports of NdPr oxide/metal or heavy rare earths (Dy, Tb) to either the United States or the European Union fall by more than 50% year-on-year for three or more consecutive months, per China customs data.
- **China energy-related CO2 emissions decline three consecutive years** — IEA or CREA reports China's energy-related CO2 emissions declining year-on-year in three consecutive calendar years, with the third such year at or before the stated year.
- **EU ETS2 delayed, price-capped or materially diluted** — The EU formally postpones ETS2's start beyond 2027, or amends the directive to impose a binding price ceiling below EUR 60/tCO2, or exempts a whole covered sector (buildings or road transport), before 31 December 2028.
- **US data-center electricity demand growth collapses** — US data-center electricity consumption grows less than 3% year-on-year in any calendar year, or declines, per EIA/LBNL reporting — versus the 15-20%/yr trend.
- **Global oil demand declines year-on-year outside recession or supply shock** — IEA Oil Market Report reports total global oil demand for a calendar year below the preceding calendar year, in a year with positive global real GDP growth above 2% and no Hormuz-class supply disruption. 2026 is excluded from resolution due to the Hormuz shock.
- **Inverter-driven systemic grid collapse in a major OECD system** — A frequency, voltage or oscillation event causes loss of supply to 5 million or more customers for 6 or more hours across a national or multi-national synchronous area in the OECD, with the official investigation identifying inverter-based resource dynamics, insufficient system inertia or protection mis-coordination as a primary or contributing cause.
- **LME copper exceeds $15,000/tonne** — LME 3-month copper settles above $15,000/tonne (nominal USD) on a monthly average basis.
- **A Western SMR delivers first commercial grid power** — A small modular reactor (nameplate under 300 MWe) in an OECD member country, excluding South Korea's existing SMART-class designs, synchronises to the grid and delivers commercial electricity, confirmed by the national regulator or IAEA PRIS.
- **European gas price returns to crisis levels** — TTF front-month natural gas futures settle above EUR 100/MWh on any trading day.
- **Firm load shedding in a major US RTO** — PJM, ERCOT, MISO or SPP orders involuntary firm load shed (rolling blackouts) affecting 500,000 or more customers during a declared capacity or energy emergency.
- **Global coal demand falls 3%+ below the 2025 level** — IEA reports global coal demand (Mt or Mtce) for some calendar year at or before the stated year at least 3% below the reported 2025 level, confirming structural decline rather than noise.
- **Lithium carbonate price exceeds $40,000/tonne** — Battery-grade lithium carbonate, China spot (SMM or Fastmarkets assessment), exceeds $40,000/tonne on a monthly average basis.
- **Brent monthly average below $45/bbl** — The calendar-month average of front-month Brent futures settlements falls below $45.00/bbl (nominal USD) in any month after 1 Aug 2026.
- **Cyberattack causes a major OECD power outage** — A cyber intrusion causes loss of electricity supply to 500,000 or more customers for 6 or more hours in an OECD member country, with cyber causation publicly confirmed by the relevant national CERT, regulator or system operator.
- **Annual global solar PV installations exceed 1,000 GW** — Global solar PV capacity additions in a calendar year exceed 1,000 GWdc, as reported by BNEF, IEA or SolarPower Europe.
- **Nuclear accident rated INES Level 5 or above** — The IAEA International Nuclear Event Scale assigns a rating of Level 5 (accident with wider consequences) or higher to an event at a civil nuclear power reactor or spent fuel facility anywhere in the world.
- **Coordinated physical attack causes a major OECD outage** — A deliberate physical attack (sabotage, arson, gunfire, explosive) causes loss of electricity supply to 500,000 or more customers for 24 or more hours in an OECD member country, confirmed as deliberate by law enforcement.
- **Global installed water electrolysis capacity reaches 25 GW** — IEA Global Hydrogen Review reports cumulative installed and operating water electrolysis capacity worldwide of 25 GW or more.

</details>

### Food, water & agriculture

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| New IPC/CH Famine (Phase 5) classification anywhere | 69% | 93% | 97% | [92%–99%] | 5 | 2027Q2 |
| Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously | 24% | 61% | 76% | [55%–92%] | 6 | 2029Q1 |
| GRFC reports more than 300 million people in acute food insecurity | 17% | 72% | 85% | [57%–98%] | 5 | 2029Q2 |
| FAO Food Price Index reaches an all-time high above 160 | 15% | 43% | 70% | [38%–91%] | 6 | 2030Q3 |
| New World screwworm or FMD establishes in the US or EU cattle herd | 16% | 45% | 68% | [28%–98%] | 5 | 2030Q1 |
| Thai 5% broken rice benchmark exceeds US$650/tonne | 8.4% | 26% | 48% | [21%–76%] | 7 | 2031Q3 |
| WFP annual contributions fall below US$5 billion | 35% | 56% | 63% | [39%–86%] | 5 | 2027Q4 |
| Ukrainian seaborne grain exports fall below 1 Mt in a calendar month | 62% | 76% | 77% | [52%–97%] | 4 | 2027Q1 |
| World Bank monthly urea price exceeds US$800/tonne | 27% | 47% | 61% | [35%–84%] | 5 | 2028Q3 |
| Cyberattack or physical sabotage halts a top-5 global agri-food processor or a major water utility | 20% | 54% | 76% | [36%–99%] | 4 | 2029Q4 |
| DAP/phosphate rock price exceeds US$1,000/tonne on a monthly average | 10% | 36% | 59% | [22%–98%] | 5 | 2030Q4 |
| Mississippi River or Panama Canal low-water event materially disrupts US grain exports | 32% | 83% | 97% | [86%–>99%] | 3 | 2028Q3 |
| Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months | 59% | 90% | 96% | [77%–>99%] | 3 | 2027Q3 |
| World cereal production falls 4%+ year-on-year (multi-breadbasket failure) | 12% | 21% | 33% | [17%–55%] | 8 | 2030Q1 |
| India physically curtails Indus western-river flows to Pakistan | 5.0% | 17% | 36% | [15%–61%] | 7 | 2032Q2 |
| FAO declares a desert locust upsurge or plague affecting three or more countries | 14% | 42% | 62% | [20%–98%] | 4 | 2030Q1 |
| World cereal stocks-to-use ratio falls below 28% | 6.5% | 23% | 35% | [15%–61%] | 7 | 2030Q3 |
| Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab | 5.4% | 15% | 27% | [2.2%–63%] | 8 | 2031Q2 |
| Three or more countries/territories in confirmed IPC Famine simultaneously | 5.0% | 17% | 27% | [7.7%–59%] | 7 | 2030Q4 |
| Hormuz fertilizer flows normalise (downside-risk-off event) | 59% | 84% | 91% | [73%–99%] | 2 | 2027Q2 |
| Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water | 2.8% | 7.8% | 13% | [3.8%–25%] | 8 | 2030Q4 |
| Colorado River enters 2027 without an agreed post-2026 framework | 31% | 32% | 32% | [13%–59%] | 3 | 2027Q1 |

<details><summary>Resolution criteria</summary>

- **New IPC/CH Famine (Phase 5) classification anywhere** — The IPC Famine Review Committee or a CH equivalent confirms Famine (IPC Phase 5) — with reasonable evidence or higher — for at least one geographic area not already so classified as of 2026-07-29, published on ipcinfo.org.
- **Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously** — Per the IFPRI Food and Fertilizer Export Restrictions Tracker, at least two countries each ranking in the global top 10 for wheat, maize or rice exports have in force, simultaneously and for at least 60 consecutive days, a new (post-2026-07-29) export ban or quota estimated to cut that country's exports of the staple by 25% or more.
- **GRFC reports more than 300 million people in acute food insecurity** — Any edition of the Global Report on Food Crises published in 2027-2036 reports more than 300.0 million people in IPC/CH Phase 3 or above for its reference year.
- **FAO Food Price Index reaches an all-time high above 160** — The FAO Food Price Index (2014-2016=100, nominal) monthly value exceeds 160.0, surpassing the March 2022 record of 160.3.
- **New World screwworm or FMD establishes in the US or EU cattle herd** — USDA APHIS, WOAH or the European Commission confirms sustained autochthonous transmission of New World screwworm (Cochliomyia hominivorax) north of the Mexico-US border, or an FMD outbreak in an FMD-free country of the G7, triggering a national movement standstill or export ban of 30+ days.
- **Thai 5% broken rice benchmark exceeds US$650/tonne** — FAO GIEWS / Thai Rice Exporters Association monthly average f.o.b. price for Thai white rice 5% broken exceeds US$650 per tonne.
- **WFP annual contributions fall below US$5 billion** — WFP's published annual contribution total for any calendar year 2026-2036 is below US$5.0 billion (nominal), per wfp.org contributions data.
- **Ukrainian seaborne grain exports fall below 1 Mt in a calendar month** — Ukrainian Ministry of Agrarian Policy or UGA monthly data show total seaborne grain and oilseed exports below 1.0 million tonnes in any single calendar month (normal 2024-26 range ~3-5 Mt/month).
- **World Bank monthly urea price exceeds US$800/tonne** — World Bank Pink Sheet monthly average urea (Middle East, bulk, f.o.b.) exceeds US$800 per tonne in any month.
- **Cyberattack or physical sabotage halts a top-5 global agri-food processor or a major water utility** — A publicly confirmed cyber or sabotage incident forces a 7+ day shutdown of national-scale operations at a top-5 global meat, grain-trading or fertilizer company, or causes a 7+ day loss of service at a water utility serving 1m+ people, per company disclosure, CISA/ENISA advisory or national regulator.
- **DAP/phosphate rock price exceeds US$1,000/tonne on a monthly average** — World Bank Pink Sheet monthly average DAP (f.o.b. US Gulf) exceeds US$1,000 per tonne in any month.
- **Mississippi River or Panama Canal low-water event materially disrupts US grain exports** — USDA Grain Transportation Report or Army Corps data show either (a) Mississippi barge freight rates above 800% of tariff benchmark, or draft/tow restrictions in force on the Lower Mississippi, for 30+ consecutive days, or (b) Panama Canal transit slots cut 30%+ below normal for 60+ consecutive days.
- **Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months** — USDA, Eurostat, WOAH or the national statistical agency of a G20 member reports a decline of 10% or more, within any rolling 12-month window, in national laying-hen inventory or national pig inventory, attributed principally to an animal disease epizootic (HPAI, ASF, FMD or successor).
- **World cereal production falls 4%+ year-on-year (multi-breadbasket failure)** — FAO's Cereal Supply and Demand Brief reports world cereal production for a calendar year at least 4.0% below the prior year's outturn (using FAO's own revised series at the time of the following year's July brief).
- **India physically curtails Indus western-river flows to Pakistan** — Pakistan's IRSA rim-station data, corroborated by satellite/independent hydrological analysis, show a sustained reduction of 20% or more over at least four consecutive weeks in Chenab or Jhelum inflows attributable to Indian storage operations or diversion, and not to natural hydrology.
- **FAO declares a desert locust upsurge or plague affecting three or more countries** — FAO Desert Locust Watch raises the situation to 'Upsurge' or 'Plague' with swarms reported in three or more countries simultaneously for 60+ days.
- **World cereal stocks-to-use ratio falls below 28%** — FAO's Cereal Supply and Demand Brief reports a world cereal stocks-to-use ratio below 28.0% for any marketing year.
- **Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab** — CIMMYT, BGRI, FAO or a national plant protection agency confirms establishment of a Ug99-lineage stem rust race, a novel highly virulent stripe rust race defeating deployed resistance, or wheat blast (Magnaporthe oryzae Triticum), in Indian or Pakistani Punjab or Haryana, with documented field-scale infection.
- **Three or more countries/territories in confirmed IPC Famine simultaneously** — At any point in a calendar year, IPC/FRC-confirmed Famine (Phase 5) classifications are simultaneously in force for areas in three or more distinct countries or territories.
- **Hormuz fertilizer flows normalise (downside-risk-off event)** — World Bank or IFA data show Middle East seaborne urea and ammonia export volumes recovering to 90% or more of their 2024-25 monthly average for three consecutive months.
- **Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water** — ACLED or equivalent records a state-attributed kinetic attack (air, missile, drone or special-forces) on the Grand Ethiopian Renaissance Dam or associated Ethiopian water infrastructure, or a direct armed exchange between Egyptian and Ethiopian forces publicly framed by either government as arising from the Nile water dispute.
- **Colorado River enters 2027 without an agreed post-2026 framework** — On 1 January 2027, no seven-state consensus agreement and no signed federal Record of Decision governs Lake Powell/Lake Mead operations for calendar 2027, with operations instead running under an interim stopgap, unilateral federal action, or litigation.

</details>

### Pandemics, biosecurity & global health

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Multiple US states abolish or gut school-entry vaccine mandates | 21% | 56% | 78% | [37%–99%] | 6 | 2029Q3 |
| PEPFAR terminated, absorbed, or cut by more than half from its FY2024 level | 15% | 46% | 66% | [22%–98%] | 7 | 2030Q1 |
| US federal government de-recommends a core routine childhood vaccine and the change survives | 40% | 58% | 64% | [23%–98%] | 6 | 2027Q3 |
| Cholera resurgence with oral cholera vaccine stockpile failure | 14% | 48% | 76% | [35%–99%] | 5 | 2030Q2 |
| United States formally loses measles elimination status | 81% | 89% | 90% | [73%–98%] | 4 | 2026Q4 |
| A single US influenza season with at least 50,000 estimated deaths | 16% | 47% | 68% | [31%–98%] | 5 | 2029Q4 |
| Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin | 11% | 35% | 46% | [8.9%–88%] | 7 | 2029Q4 |
| Large autochthonous arbovirus transmission in continental Europe or the continental US | 19% | 57% | 81% | [42%–99%] | 4 | 2029Q4 |
| Two consecutive years of rising global new HIV infections | 1.6% | 42% | 50% | [13%–89%] | 6 | 2029Q4 |
| WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency | 54% | 93% | 98% | [94%–99%] | 3 | 2027Q4 |
| WHO declares an influenza pandemic (any subtype) | 8.0% | 22% | 36% | [20%–53%] | 8 | 2030Q3 |
| A newly emerged pathogen causes at least 1 million cumulative deaths worldwide | 2.2% | 12% | 27% | [9.8%–49%] | 10 | 2032Q2 |
| PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly | 51% | 81% | 87% | [65%–98%] | 3 | 2027Q3 |
| Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases | 38% | 42% | 42% | [16%–79%] | 6 | 2027Q1 |
| WHO Pandemic Agreement enters into force | 2.1% | 52% | 76% | [47%–97%] | 3 | 2030Q2 |
| Paralytic poliomyelitis from circulating vaccine-derived poliovirus in a high-income country | 8.8% | 34% | 56% | [21%–90%] | 4 | 2030Q4 |
| US reports at least 5,000 confirmed measles cases in a single calendar year | 18% | 59% | 72% | [43%–93%] | 3 | 2029Q2 |
| Sustained human-to-human transmission of an H5 influenza virus | 3.2% | 11% | 20% | [6.7%–41%] | 9 | 2031Q3 |
| United States formally rejoins the World Health Organization | 1.1% | 28% | 41% | [14%–72%] | 4 | 2030Q2 |
| Global interruption of wild poliovirus type 1 transmission | 3.1% | 24% | 45% | [24%–72%] | 3 | 2031Q3 |
| Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution | 1.8% | 5.6% | 11% | [1.7%–35%] | 7 | 2032Q1 |
| Deliberate biological attack causes at least 10 confirmed human deaths | 2.0% | 5.7% | 9.4% | [2.2%–23%] | 8 | 2031Q1 |
| Ebola causes a confirmed secondary transmission chain outside Africa | 7.4% | 13% | 18% | [5.8%–40%] | 4 | 2029Q2 |
| WHO declares a global emergency over an antimicrobial-resistant pathogen | 1.0% | 4.4% | 8.9% | [2.8%–18%] | 5 | 2032Q1 |

<details><summary>Resolution criteria</summary>

- **Multiple US states abolish or gut school-entry vaccine mandates** — At least five US states have, via statute or binding regulation in effect, eliminated school-entry immunization requirements for one or more core antigens, or adopted universal opt-out (any-reason philosophical exemption granted on request without documentation), at any point in the window.
- **PEPFAR terminated, absorbed, or cut by more than half from its FY2024 level** — US enacted appropriations or a binding reorganization reduce dedicated PEPFAR/global HIV bilateral funding below 50% of the FY2024 enacted level for a full fiscal year, or the programme is formally dissolved into a successor account with no ring-fenced HIV line.
- **US federal government de-recommends a core routine childhood vaccine and the change survives** — CDC's published child and adolescent immunization schedule removes a currently universally-recommended antigen (MMR, DTaP, IPV, Hib, PCV, rotavirus, varicella, or the hepatitis B birth dose) from universal recommendation - moving it to shared clinical decision-making, risk-based, or off-schedule - and that change is in effect and not judicially stayed for at least 6 continuous months.
- **Cholera resurgence with oral cholera vaccine stockpile failure** — WHO reports at least 6,000 cholera deaths globally in a single calendar year, or formally announces that the global OCV stockpile has been unable to meet the single-dose emergency standard for a continuous period of 12 months or more.
- **United States formally loses measles elimination status** — PAHO's Regional Verification Commission (or WHO) formally announces that the United States no longer meets measles elimination criteria, or the US government/CDC publicly acknowledges loss of elimination status.
- **A single US influenza season with at least 50,000 estimated deaths** — CDC in-season or final burden estimates put deaths from seasonal influenza at 50,000 or more for a single season within the window.
- **Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin** — A national government, law enforcement agency, or frontier AI developer publicly confirms a specific incident in which AI systems materially assisted a person or group in designing, acquiring, or synthesizing a pathogen or toxin of biosecurity concern (beyond generic capability-evaluation results or red-team exercises).
- **Large autochthonous arbovirus transmission in continental Europe or the continental US** — At least 1,000 locally acquired cases of dengue, chikungunya or Oropouche virus disease reported in a single calendar year in continental Europe or the continental United States (excluding territories such as Puerto Rico).
- **Two consecutive years of rising global new HIV infections** — UNAIDS reports annual new HIV infections higher than the preceding year in two consecutive reporting years, reversing the multi-decade decline.
- **WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency** — WHO's Director-General determines a new Public Health Emergency of International Concern (or pandemic emergency under the amended IHR) for an event distinct from the standing polio PHEIC and the Ebola Bundibugyo PHEIC declared 17 May 2026, at any point in the window.
- **WHO declares an influenza pandemic (any subtype)** — WHO formally declares an influenza pandemic, or declares a PHEIC/pandemic emergency for a novel influenza A virus with confirmed sustained community-level human-to-human transmission in at least two WHO regions.
- **A newly emerged pathogen causes at least 1 million cumulative deaths worldwide** — A pathogen not endemically circulating in humans as of 1 Jan 2026 is credibly estimated by WHO, IHME, or a peer-reviewed consensus source to have caused at least 1,000,000 cumulative human deaths (reported or excess) within the stated horizon.
- **PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly** — A World Health Assembly (regular or special session) formally adopts the Pathogen Access and Benefit-Sharing annex to the WHO Pandemic Agreement.
- **Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases** — WHO/AFRO situation reports for the outbreak declared 15 May 2026 (or its recognized continuation) record at least 10,000 cumulative laboratory-confirmed cases across all affected countries.
- **WHO Pandemic Agreement enters into force** — The 60th instrument of ratification, acceptance, approval or accession to the WHO Pandemic Agreement is deposited, bringing the Agreement into force.
- **Paralytic poliomyelitis from circulating vaccine-derived poliovirus in a high-income country** — A national health authority in a World Bank high-income country confirms at least one case of paralytic poliomyelitis caused by circulating vaccine-derived poliovirus (any type) with onset within the window.
- **US reports at least 5,000 confirmed measles cases in a single calendar year** — CDC's official measles surveillance reports at least 5,000 confirmed cases for any single calendar year within the window.
- **Sustained human-to-human transmission of an H5 influenza virus** — WHO or a national health authority publicly confirms an H5 (any neuraminidase) influenza cluster with at least three sequential generations of human-to-human transmission, or a cluster of at least 10 epidemiologically linked human cases with no plausible animal or environmental exposure for the majority.
- **United States formally rejoins the World Health Organization** — The United States formally notifies WHO of resumption of membership, or deposits an instrument of acceptance of the WHO Constitution, and pays or commits to assessed contributions.
- **Global interruption of wild poliovirus type 1 transmission** — Zero wild poliovirus type 1 cases with onset in any 12 consecutive calendar months, per GPEI reporting, with the 12-month window closing inside the horizon.
- **Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution** — A national health authority, WHO, or an official government investigation publicly attributes an outbreak of at least 50 laboratory-confirmed human infections to a laboratory-acquired infection or a containment/biosafety breach.
- **Deliberate biological attack causes at least 10 confirmed human deaths** — A government or international body attributes at least 10 human deaths to a deliberate release of a biological agent (state or non-state actor) in a single incident or campaign.
- **Ebola causes a confirmed secondary transmission chain outside Africa** — A national health authority in a country outside the WHO African Region confirms at least one locally acquired Ebola (any species) infection in a person who was not infected in Africa, at any point in the window.
- **WHO declares a global emergency over an antimicrobial-resistant pathogen** — WHO declares a PHEIC, pandemic emergency, or equivalent formal global health emergency whose primary basis is an antimicrobial-resistant bacterial or fungal pathogen (for example pan-resistant Klebsiella, XDR typhoid, Candida auris, or drug-resistant gonorrhoea).

</details>

## How bad decades begin

Among paths where at least three high-severity events fired, these are the most common opening sequences, in order of occurrence.

| Frequency | First | Then | Then |
|---:|---|---|---|
| 1.4% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics |
| 0.9% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China annual births fall below 7.0 million |
| 0.8% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | US Census Bureau officially reports negative net international migration |
| 0.6% | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |
| 0.5% | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China reports annual real GDP growth below 4.0% |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | Nvidia suffers a ≥50% peak-to-trough drawdown |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | A top-5 Western frontier lab exits frontier training |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt |
| <0.5% | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | US Census Bureau officially reports negative net international migration |

The most common opening — Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window → China annual births fall below 7.0 million → PISA 2025 shows no recovery in OECD-average mathematics — accounts for 1.4% of all paths. No single sequence dominates, which is itself informative: the model does not support a story in which one specific trigger reliably starts the cascade. What recurs is the *pattern* — a shock in one domain degrading the capacity to absorb the next.

## Where the correlations are

The clearest way to read a dependency is the contrast between P(A given B) and P(A given not-B) — how much learning one event would move your estimate of the other. Ranked by odds ratio rather than by lift, because lift is mechanically capped by the base rates: two events at 80% each cannot show a lift above 1.25 however tightly coupled they are, so ranking high-probability nodes by lift returns a table of 1.0× entries and hides every real dependency. This is the part of the model a spreadsheet of independent probabilities cannot produce, and it is where tail risk lives.

| Event A | Event B | P(A given B) | P(A given not-B) | Odds ratio |
|---|---|---:|---:|---:|
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | New round of major direct Israel-Iran exchange | **86%** | 32% | 13.4× |
| Nvidia suffers a ≥50% peak-to-trough drawdown | A top-4 US hyperscaler guides annual capex down year-over-year | **92%** | 54% | 9.1× |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **82%** | 49% | 4.6× |
| US recession with NBER-dated peak in the window | Global recession (world real GDP growth below 2.0% in a calendar year) | **91%** | 72% | 4.0× |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | **83%** | 56% | 3.9× |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | A single training run of ≥1e28 FLOP is publicly reported | **81%** | 55% | 3.4× |
| GRFC reports more than 300 million people in acute food insecurity | FAO Food Price Index reaches an all-time high above 160 | **90%** | 74% | 3.1× |
| US unemployment rate ≥6.0% for three consecutive months | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **84%** | 68% | 2.6× |
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | New IPC/CH Famine (Phase 5) classification anywhere | **98%** | 96% | 2.4× |
| A single training run of ≥1e28 FLOP is publicly reported | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **85%** | 70% | 2.4× |
| Japan 10-year government bond yield reaches 3.00% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | **93%** | 85% | 2.3× |
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | **98%** | 96% | 2.3× |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | **77%** | 61% | 2.1× |
| Japan 10-year government bond yield reaches 3.00% | Nvidia suffers a ≥50% peak-to-trough drawdown | **94%** | 87% | 2.1× |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | A single training run of ≥1e28 FLOP is publicly reported | **77%** | 63% | 1.9× |
| Sustained Bab el-Mandeb / Red Sea shipping disruption | FAO Food Price Index reaches an all-time high above 160 | **82%** | 70% | 1.9× |
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China's extraterritorial rare-earth export control regime enters into force | **98%** | 97% | 1.9× |
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Long-term (multi-decadal) 1.5C breach formally declared | **98%** | 97% | 1.9× |

## Continuous indicators

These evolve on a Gaussian copula driven by each path's own systemic-stress index, so the bad tails of these distributions are populated by the same paths that fired the bad events — not by independent noise.

| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |
|---|---:|:---:|:---:|
| World military expenditure as share of global GDP (percent of global GDP) | 2.5 | 2.61 / **2.9** / 3.25 | 2.69 / **3.12** / 3.59 |
| Global state-based armed conflict battle deaths per year (thousands of deaths per year) | 160 | 53.6 / **129** / 245 | 11.5 / **113** / 272 |
| Brent crude oil price (USD per barrel (annual average)) | 86 | 44.4 / **71.5** / 140 | 27.2 / **64.5** / 157 |
| US military expenditure as share of US GDP (percent of GDP) | 3.2 | 2.95 / **3.3** / 3.69 | 2.87 / **3.35** / 3.89 |
| European NATO members' aggregate defence spending as share of GDP (percent of GDP) | 2.65 | 2.99 / **3.34** / 3.75 | 3.25 / **3.74** / 4.3 |
| PLA aircraft sorties entering Taiwan's ADIZ per year (sorties per year) | 3600 | 2.37e+03 / **4.95e+03** / 7.83e+03 | 2.18e+03 / **5.76e+03** / 9.67e+03 |
| US dollar share of allocated global FX reserves (percent) | 58 | 50.9 / **54** / 56.9 | 47.7 / **51.8** / 56 |
| Weekly container-ship transits of the Suez Canal (transits per week) | 30 | 21.2 / **62.3** / 87.9 | 24.5 / **79.1** / 115 |
| Combined US + Russia deployed strategic nuclear warheads (warheads) | 3200 | 3.15e+03 / **3.72e+03** / 4.33e+03 | 3.19e+03 / **4e+03** / 4.87e+03 |
| Net monthly Russian territorial gain in Ukraine (km2 per month (negative = Ukrainian recapture)) | 104 | -30.1 / **7.11** / 166 | -96.5 / **-44.9** / 188 |
| Number of active state-based armed conflicts (>=25 battle deaths/year) (count) | 61 | 48.2 / **58.2** / 68.1 | 42.6 / **56.1** / 69.8 |
| Crude and condensate transiting the Strait of Hormuz (million barrels per day) | 8 | 4.77 / **17.7** / 21 | 5.39 / **23.5** / 27.6 |
| Annual global mean surface temperature anomaly (ERA5, vs 1850-1900) (C) | 1.47 | 1.48 / **1.62** / 1.78 | 1.52 / **1.7** / 1.93 |
| Annual mean CO2 concentration at Mauna Loa (ppm) | 429.4 | 440 / **442** / 445 | 446 / **449** / 452 |
| NOAA global mean atmospheric methane (ppb) | 1945 | 1.97e+03 / **1.98e+03** / 2e+03 | 1.98e+03 / **2e+03** / 2.02e+03 |
| Global fossil CO2 emissions (Global Carbon Project) (GtCO2/yr) | 38.1 | 35.6 / **38.3** / 40.1 | 34.7 / **38.4** / 40.9 |
| Global mean sea level (satellite altimetry, above 1993 baseline) (mm) | 112 | 132 / **138** / 144 | 144 / **153** / 161 |
| Arctic sea ice September minimum extent (NSIDC) (million km2) | 4.3 | 3.34 / **3.98** / 4.55 | 2.94 / **3.81** / 4.6 |
| Annual maximum 3-month ONI (Nino3.4) (C) | 2.4 | -0.853 / **0.415** / 1.72 | -2.49 / **-0.671** / 1.16 |
| Share of global reef area under Alert Level 1+ heat stress, rolling 12 months (% of global reef area) | 55 | 32.9 / **62** / 88.5 | 24 / **66.5** / 102 |
| Brazilian Legal Amazon annual deforestation (INPE PRODES) (km2/yr) | 5796 | 3.16e+03 / **4.98e+03** / 9.79e+03 | 1.86e+03 / **4.38e+03** / 1.12e+04 |
| FAO Food Price Index (nominal) (index, 2014-2016 = 100) | 130.3 | 121 / **140** / 167 | 120 / **145** / 182 |
| Annual increase in global 0-2000m ocean heat content (ZJ/yr) | 23 | 13.2 / **25.2** / 36.8 | 9.95 / **26.1** / 42 |
| Brent crude oil price (USD per barrel) | 84 | 42 / **79.2** / 151 | 26 / **74.7** / 178 |
| US 10-year Treasury yield (percent) | 4.62 | 3.08 / **4.8** / 6.32 | 2.5 / **4.87** / 6.97 |
| US CPI inflation, year over year (percent) | 3.5 | 1.16 / **2.6** / 4.88 | 0.217 / **2.12** / 5.22 |
| Federal funds target rate, upper bound (percent) | 3.75 | 1.75 / **3.51** / 5.26 | 0.991 / **3.4** / 5.84 |
| S&P 500 index level (index points) | 7412 | 6.04e+03 / **9.94e+03** / 1.59e+04 | 5.93e+03 / **1.15e+04** / 1.95e+04 |
| Global real GDP growth (percent per year) | 3 | 1.55 / **3.18** / 4.16 | 1.09 / **3.33** / 4.7 |
| China reported real GDP growth (percent per year) | 4.6 | 1.91 / **3.39** / 4.8 | 0.651 / **2.76** / 4.69 |
| US federal debt held by the public / GDP (percent) | 100 | 106 / **111** / 119 | 110 / **117** / 128 |
| USD share of allocated FX reserves (IMF COFER) (percent) | 56.5 | 47.1 / **52.1** / 57.1 | 42.4 / **49.5** / 56.6 |
| Gold price (USD per troy ounce) | 4040 | 3.15e+03 / **4.73e+03** / 7.4e+03 | 2.87e+03 / **5.09e+03** / 8.61e+03 |
| USD/JPY exchange rate (yen per dollar) | 163.6 | 119 / **153** / 193 | 97.7 / **145** / 203 |
| US average effective tariff rate on all imports (percent) | 6 | 3.04 / **7.91** / 18 | 2.14 / **8.99** / 23.2 |
| Log10 of training compute for the largest publicly-known training run (log10(FLOP)) | 26.7 | 28 / **28.8** / 29.5 | 28.8 / **30** / 30.9 |
| Global data center electricity consumption (TWh per year) | 590 | 832 / **1.03e+03** / 1.35e+03 | 997 / **1.27e+03** / 1.7e+03 |
| Combined annual capex, Microsoft + Alphabet + Amazon + Meta (USD billions per year) | 700 | 477 / **989** / 1.5e+03 | 436 / **1.13e+03** / 1.84e+03 |
| Nvidia annual data center revenue (USD billions per year) | 330 | 223 / **535** / 871 | 235 / **655** / 1.13e+03 |
| Combined annualized revenue run-rate, OpenAI + Anthropic (USD billions) | 72 | 166 / **351** / 629 | 245 / **502** / 883 |
| Log2 of METR 50%-reliability task time horizon (log2(hours of human-expert task time)) | 1.6 | 5.36 / **8.06** / 10.8 | 7.92 / **11.7** / 15.3 |
| Log10 of API price for GPT-4-class capability (log10(USD per million input tokens)) | -0.4 | -2.19 / **-1.79** / -1.4 | -3.12 / **-2.56** / -2.02 |
| Chinese open-weight models' share of OpenRouter tokens (percent) | 61 | 31 / **59.9** / 83.1 | 20.9 / **59.8** / 91.2 |
| Log10 of US paid fully-driverless rides per week (millions) (log10(millions of rides per week)) | -0.3 | 0.164 / **0.896** / 1.4 | 0.602 / **1.57** / 2.25 |
| US AI adoption in production, employment-weighted (Census BTOS) (percent of employment at AI-using firms) | 32 | 44.9 / **55.7** / 68.2 | 53.4 / **69.3** / 85.3 |
| Global total fertility rate (births per woman) | 2.23 | 2.03 / **2.12** / 2.21 | 1.94 / **2.06** / 2.19 |
| China annual births (million births per year) | 7.92 | 4.64 / **5.93** / 7.42 | 2.98 / **4.82** / 6.87 |
| US total fertility rate (births per woman) | 1.585 | 1.44 / **1.51** / 1.59 | 1.37 / **1.47** / 1.58 |
| Global forcibly displaced persons (million people) | 117.8 | 103 / **120** / 141 | 98 / **121** / 149 |
| US net international migration (thousand persons per year) | 320 | -155 / **627** / 1.42e+03 | -253 / **790** / 1.88e+03 |
| EU+ annual asylum applications (thousand applications per year) | 822 | 319 / **704** / 1.35e+03 | 108 / **631** / 1.53e+03 |
| India total fertility rate (births per woman) | 1.9 | 1.62 / **1.73** / 1.83 | 1.49 / **1.64** / 1.78 |
| World population (billion people) | 8.3 | 8.57 / **8.63** / 8.69 | 8.73 / **8.81** / 8.89 |
| China population aged 60 and over (percent of total population) | 22.9 | 27.1 / **28** / 28.8 | 29.5 / **30.8** / 31.9 |
| US annual drug overdose deaths (thousand deaths per year) | 70 | 34.7 / **55** / 79.3 | 18.3 / **46.7** / 81.6 |
| South Korea total fertility rate (births per woman) | 0.8 | 0.738 / **0.871** / 1 | 0.728 / **0.909** / 1.09 |
| Japan annual births (Japanese nationals) (thousand births per year) | 670 | 462 / **538** / 608 | 364 / **468** / 563 |
| Brent crude oil price (USD/bbl (nominal)) | 73 | 42.2 / **71.7** / 128 | 29.4 / **71.1** / 148 |
| Annual global solar PV capacity additions (GWdc/yr) | 650 | 638 / **885** / 1.19e+03 | 672 / **1e+03** / 1.43e+03 |
| Lithium-ion battery pack price (volume-weighted, all segments) (USD/kWh (nominal)) | 105 | 55.7 / **72.7** / 94.9 | 30.3 / **54.3** / 85.7 |
| China share of global rare-earth separation and refining (% of global refined output) | 87 | 71.9 / **78.9** / 86.7 | 65.3 / **74.7** / 85.8 |
| US data center electricity consumption (TWh/yr) | 225 | 325 / **465** / 677 | 400 / **596** / 891 |
| EU average wholesale electricity price (EUR/MWh (nominal)) | 80 | 40.4 / **65.8** / 117 | 23.2 / **58.9** / 128 |
| Global coal demand (Mt/yr) | 8800 | 7.7e+03 / **8.47e+03** / 9.04e+03 | 7.21e+03 / **8.27e+03** / 9.1e+03 |
| Uranium spot price (USD/lb U3O8) | 88 | 54.6 / **106** / 186 | 47 / **116** / 230 |
| Global oil (liquids) demand (million b/d) | 104.5 | 102 / **106** / 110 | 102 / **107** / 112 |
| Global LNG liquefaction nameplate capacity (Mtpa) | 510 | 654 / **712** / 755 | 744 / **821** / 884 |
| Global EV share of new light-vehicle sales (% of new sales) | 22.4 | 31.7 / **39.8** / 47.8 | 38.4 / **49.7** / 60.6 |
| Henry Hub natural gas price (USD/MMBtu (nominal)) | 3.7 | 2.49 / **4.18** / 7.03 | 2.17 / **4.47** / 8.29 |
| Cumulative confirmed H5N1-infected US dairy herds (herds) | 1166 | 1.3e+03 / **1.82e+03** / 2.62e+03 | 1.47e+03 / **2.17e+03** / 3.27e+03 |
| Confirmed human H5 (any NA) influenza cases reported globally per year (cases/year) | 14 | 2.43 / **16** / 64 | -1.03 / **16.9** / 84.6 |
| US confirmed measles cases per calendar year (cases/year) | 2900 | 845 / **3.78e+03** / 8.94e+03 | 453 / **4.41e+03** / 1.14e+04 |
| US kindergarten MMR vaccination coverage (% of kindergartners) | 92.5 | 89 / **90.6** / 92.2 | 87.4 / **89.6** / 91.8 |
| Global DTP3 immunization coverage (% of surviving infants) | 85 | 81.8 / **83.9** / 86 | 80.3 / **83.3** / 86.2 |
| Deaths directly attributable to bacterial AMR (million deaths/year) | 1.2 | 1.16 / **1.31** / 1.46 | 1.16 / **1.37** / 1.58 |
| International financing for HIV in low- and middle-income countries (US$ billions/year) | 7.3 | 3.21 / **5.4** / 7.75 | 1.32 / **4.4** / 7.68 |
| US adults currently using GLP-1 drugs for weight loss (% of adults) | 12.4 | 16.1 / **23** / 31.3 | 19 / **28.7** / 40 |
| US adult obesity prevalence (Gallup self-reported) (% of adults) | 36.4 | 31.5 / **33.4** / 35.3 | 29 / **31.7** / 34.4 |
| WHO approved base programme budget per biennium (US$ billions/biennium) | 4.2 | 3.42 / **4.1** / 5.12 | 3.1 / **4.04** / 5.44 |
| Global malaria deaths (thousand deaths/year) | 610 | 560 / **633** / 715 | 548 / **649** / 761 |
| CDC full-time federal workforce (thousand FTEs) | 9 | 6.6 / **8.17** / 9.86 | 5.53 / **7.75** / 10.1 |
| US presidential net approval (approve minus disapprove, aggregate) (percentage points) | -19 | -28.9 / **-10.2** / 5.94 | -31.9 / **-5.07** / 16.8 |
| Number of countries coded as currently autocratizing by V-Dem (countries) | 44 | 37.1 / **45** / 53.9 | 34.3 / **45.6** / 58.1 |
| Countries with net decline in Freedom House score in a given year (countries) | 54 | 39.9 / **51.3** / 63.3 | 34.4 / **49.2** / 66.1 |
| Share of world population living in Freedom House 'Free' countries (percent) | 21 | 15 / **20** / 24 | 12.7 / **19.5** / 25 |
| AfD federal voting intention (percent) | 27 | 19.1 / **28.1** / 36.1 | 16 / **28.6** / 39.6 |
| French RN first-round national vote share (presidential/legislative) (percent) | 35 | 28 / **36.1** / 44.2 | 25.4 / **36.4** / 47.4 |
| Reform UK voting intention (percent) | 26 | 13.7 / **24.1** / 35 | 9.22 / **22.9** / 38.5 |
| Successful coups d'etat worldwide per calendar year (coups) | 2 | 0.0295 / **2** / 5.04 | -0.716 / **2.02** / 6.22 |
| US terrorism and targeted-violence events per year (START/BDI coding) (events) | 1050 | 713 / **1.23e+03** / 1.77e+03 | 621 / **1.32e+03** / 2.1e+03 |
| Gallup average 'great deal / quite a lot' confidence across nine US institutions (percent) | 27 | 21 / **25.9** / 31.2 | 18.7 / **25.5** / 32.4 |
| ACLED-recorded political violence events worldwide per year (events) | 1.85e+05 | 1.51e+05 / **1.97e+05** / 2.48e+05 | 1.4e+05 / **2.04e+05** / 2.76e+05 |
| FAO Food Price Index (nominal) (index, 2014-2016=100) | 130.3 | 113 / **146** / 198 | 106 / **155** / 229 |
| World cereal stocks-to-use ratio (percent) | 32 | 27.8 / **31.3** / 34.7 | 26 / **30.8** / 35.5 |
| World cereal production (million tonnes per calendar year) | 2983 | 2.95e+03 / **3.13e+03** / 3.28e+03 | 2.96e+03 / **3.2e+03** / 3.42e+03 |
| Urea price (Middle East granular, f.o.b.) (USD per tonne) | 520 | 233 / **441** / 845 | 99.7 / **390** / 962 |
| People in acute food insecurity (IPC/CH Phase 3+, GRFC) (million people) | 266 | 225 / **291** / 355 | 212 / **303** / 392 |
| People in IPC/CH Phase 5 (Catastrophe) (million people) | 1.4 | 0.38 / **1.61** / 3.45 | -0.0212 / **1.71** / 4.25 |
| CBOT front-month wheat price (USD per bushel) | 6.9 | 5.07 / **7.68** / 12.1 | 4.64 / **8.32** / 14.4 |
| Thai white rice 5% broken, f.o.b. (USD per tonne) | 365 | 245 / **405** / 661 | 207 / **423** / 767 |
| Lake Mead elevation (feet above mean sea level) | 1053 | 992 / **1.03e+03** / 1.07e+03 | 963 / **1.02e+03** / 1.07e+03 |
| WFP annual contributions received (USD billion, nominal) | 6.5 | 3.3 / **5.51** / 7.77 | 1.82 / **4.98** / 8.14 |
| Global undernourishment headcount (PoU) (million people) | 645 | 531 / **602** / 675 | 481 / **579** / 680 |
| Share of marine fish stocks within biologically sustainable levels (percent) | 62.4 | 57.4 / **60** / 62.4 | 55.2 / **58.8** / 62 |
| Israeli defence spending as share of GDP (% of GDP) | 7.9 | 4.62 / **6.15** / 8.82 | 3.06 / **5.2** / 8.88 |
| Israeli settler population in the West Bank (excl. East Jerusalem) (thousands of persons) | 530 | 585 / **613** / 647 | 619 / **659** / 707 |
| Cumulative external reconstruction financing disbursed for Gaza (USD billions (2026)) | 1.2 | 1.9 / **7.49** / 29 | 3.23 / **10.9** / 38.7 |
| Estimated Hezbollah rocket and missile inventory (thousands of units) | 15 | 5.01 / **25.4** / 69 | 3.12 / **29.9** / 90.3 |
| Bab el-Mandeb transit volume relative to 2023 baseline (index, 2023 = 100) | 48 | 31.6 / **72.3** / 98.8 | 29.3 / **83.8** / 125 |
| Annual conflict fatalities in the West Bank and East Jerusalem (persons per year) | 330 | 107 / **298** / 1.29e+03 | 16.4 / **282** / 1.66e+03 |
| Israeli net migration balance (thousands of persons per year) | -12 | -47.9 / **3.35** / 37.6 | -59.1 / **13.2** / 60.2 |
| Days per year with direct Israel-Iran or US-Iran kinetic exchange (days per year) | 110 | 0.15 / **12.6** / 159 | -58.3 / **-41.6** / 160 |

## What drives the outcome

Share of the variance in peak systemic stress attributable to each event firing at all. High-scoring nodes are the ones worth watching, because learning how they resolve collapses the most uncertainty about everything else.

*Read with one caveat:* the stress index is built from these same events, so part of any node's score is its own contribution rather than its influence on others. The ranking is still informative — it combines probability, impact rating and correlation with the rest of the system in one number — but it is not a pure causal-influence measure, and a node cannot score high here without being either likely or heavy.

| Event | Variance share | P(by 2036) | Impact |
|---|---:|---:|---:|
| Global recession (world real GDP growth below 2.0% in a calendar year) | 4.1% | 62% | 7 |
| Severe rare-earth supply cutoff to the US or EU | 2.4% | 51% | 8 |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 2.4% | 78% | 8 |
| Brent crude settles above $120/bbl | 2.3% | 71% | 6 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 2.3% | 27% | 9 |
| US average effective tariff rate exceeds 15% | 2.3% | 47% | 5 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 2.2% | 49% | 8 |
| S&P 500 falls 30%+ from its all-time closing high | 2.1% | 64% | 6 |
| Wave of emerging-market sovereign defaults or restructurings | 2.0% | 74% | 5 |
| Direct US-PRC military exchange causing at least one fatality | 1.8% | 13% | 9 |
| New round of major direct Israel-Iran exchange | 1.7% | 84% | 7 |
| US 10-year Treasury yield closes at or above 6.00% | 1.7% | 37% | 8 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 1.7% | 61% | 8 |
| Brent monthly average above $120/bbl | 1.6% | 69% | 6 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 1.6% | 57% | 6 |
| US federal government de-recommends a core routine childhood vaccine and the change survives | 1.6% | 64% | 6 |
| China's extraterritorial rare-earth export control regime enters into force | 1.5% | 83% | 7 |
| US recession with NBER-dated peak in the window | 1.5% | 84% | 6 |

## Where the worldviews disagree most

The five parameterisations — raw analyst, audited, outside-view base rates, structural-break inside view, and prediction-market check — converge on most nodes. These are the ones where they don't, and they are exactly the forecasts you should hold most loosely.

| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |
|---|---:|---:|---:|---:|---:|---:|
| Japan 10-year government bond yield reaches 3.00% | 62% | 97% | 96% | 96% | 99% | 37pp |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 74% | 87% | 54% | 86% | 87% | 33pp |
| A G7 country cuts permanent immigration by three quarters | 21% | 38% | 8.2% | 35% | 36% | 29pp |
| Strait of Hormuz closed again for 14+ consecutive days | 42% | 69% | 69% | 70% | 69% | 28pp |
| US life expectancy at birth reaches 80.0 years | 63% | 85% | 85% | 88% | 88% | 25pp |
| Brent crude settles above $120/bbl | 53% | 73% | 71% | 73% | 78% | 25pp |
| Brent monthly average above $120/bbl | 51% | 69% | 73% | 70% | 75% | 24pp |
| FAO Food Price Index reaches an all-time high above 160 | 54% | 70% | 76% | 69% | 70% | 22pp |
| FAO Food Price Index exceeds 160 in any month | 55% | 71% | 77% | 71% | 70% | 21pp |
| Severe rare-earth supply cutoff to the US or EU | 34% | 55% | 54% | 53% | 53% | 20pp |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 50% | 35% | 30% | 34% | 36% | 20pp |
| US reports at least 5,000 confirmed measles cases in a single calendar year | 59% | 73% | 73% | 73% | 79% | 20pp |
| Global oil demand declines year-on-year outside recession or supply shock | 69% | 60% | 60% | 79% | 59% | 20pp |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 40% | 47% | 59% | 47% | 48% | 20pp |
| European gas price returns to crisis levels | 32% | 51% | 50% | 50% | 51% | 19pp |
| A single training run of ≥1e28 FLOP is publicly reported | 74% | 83% | 82% | 93% | 82% | 19pp |

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
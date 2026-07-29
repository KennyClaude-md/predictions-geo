# World Futures Simulation — Forecast Report

**Simulation date:** 2026-07-29  
**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  
**Paths:** 4,800 across 5 worldviews × 40 parameter worlds  
**Risk nodes:** 72 · **causal edges:** 0 · **latent factors:** 0 · **continuous variables:** 45

---

## How to read this

Every number below is the output of a survival-process Monte Carlo, not a guess written directly. Nine domains were parameterised against current sources, audited for base-rate discipline, then red-teamed from three directions. Each of those opinions is run as a separate worldview and the results are pooled by weight.

**The bracketed range is not the range of outcomes** — the event either happens or it doesn't. It is the range of *the probability itself* across parameter worlds: how much the answer moves depending on whose model of the world you accept. A wide bracket means the forecast is fragile. Monte Carlo noise has been subtracted out, so what remains is real disagreement.

**Calibration check:** simulated marginals reproduce the elicited cumulative probabilities to within 0.60 percentage points (worst node, worst worldview). This matters: the dependency network is tuned to reshape the *joint* distribution — which events co-occur — without inflating any individual probability above what the underlying analysis actually claimed.

## Headline forecasts

Ranked by expected systemic impact — probability by 2036 multiplied by severity — rather than by probability alone, because a 12% chance of something that reorders the world outranks a near-certainty that doesn't.

| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Sev |
|---|-------|--------:|--------:|--------:|:---------------:|----:|
| 1 | **Frontier agent reaches a 1-work-month 50%-reliability task horizon** | 12% | 55% | 76% | [36%–98%] | 9 |
| 2 | **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** | 57% | 69% | 77% | [54%–93%] | 8 |
| 3 | **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** | 82% | 93% | 96% | [89%–99%] | 6 |
| 4 | **US recession with NBER-dated peak in the window** | 34% | 66% | 85% | [62%–98%] | 6 |
| 5 | **A top-4 US hyperscaler guides annual capex down year-over-year** | 16% | 61% | 81% | [58%–97%] | 6 |
| 6 | **China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab** | 7.2% | 41% | 68% | [29%–98%] | 7 |
| 7 | **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** | 20% | 49% | 67% | [37%–92%] | 7 |
| 8 | **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** | 72% | 85% | 90% | [79%–97%] | 5 |
| 9 | **A single training run of ≥1e28 FLOP is publicly reported** | 12% | 57% | 74% | [47%–97%] | 6 |
| 10 | **Global recession (world real GDP growth below 2.0% in a calendar year)** | 12% | 38% | 63% | [33%–86%] | 7 |
| 11 | **US unemployment rate ≥6.0% for three consecutive months** | 18% | 55% | 73% | [43%–97%] | 6 |
| 12 | **China reports annual real GDP growth below 4.0%** | 18% | 52% | 71% | [43%–94%] | 6 |
| 13 | **AI capex bust: aggregate hyperscaler capex falls 20%+ year over year** | 4.7% | 35% | 60% | [29%–92%] | 7 |
| 14 | **Japan 10-year government bond yield reaches 3.00%** | 25% | 49% | 60% | [31%–90%] | 7 |
| 15 | **A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI** | 35% | 72% | 83% | [60%–98%] | 5 |
| 16 | **Nvidia suffers a ≥50% peak-to-trough drawdown** | 29% | 55% | 67% | [40%–91%] | 6 |
| 17 | **S&P 500 falls 30%+ from its all-time closing high** | 16% | 46% | 64% | [37%–89%] | 6 |
| 18 | **A calendar year at or above 1.65C above pre-industrial** | 56% | 81% | 92% | [75%–99%] | 4 |
| 19 | **Long-term (multi-decadal) 1.5C breach formally declared** | 4.9% | 32% | 73% | [45%–97%] | 5 |
| 20 | **Brent crude settles above $120/bbl** | 37% | 50% | 60% | [31%–87%] | 6 |
| 21 | **Large private-credit vehicle suspends redemptions or enters wind-down** | 26% | 44% | 55% | [26%–83%] | 6 |
| 22 | **Failure or extraordinary rescue of a bank with over $250bn in assets** | 10% | 26% | 40% | [16%–65%] | 8 |

## The decade in aggregate

Individual probabilities are the easy part. The question that actually determines whether the 2030s feel survivable is how many serious shocks land, and whether they land together.

| Statistic (through 2036) | Value |
|---|---|
| Expected number of severity ≥ 6 events | **18.8** |
| Severe-event count, 10th–90th percentile | 15 – 22 (median 19) |
| P(no severity ≥ 6 event at all) | <0.5% |
| P(3 or more severe events) | >99% |
| P(5 or more severe events) | >99% |
| P(at least one severity ≥ 8 event) | **>99%** |
| P(two or more severity ≥ 8 events) | 99% |

The modal decade contains 19 events the model rates severity 6 or above, and the probability of getting through to 2036 with none is 0%. That asymmetry is the single most robust finding here: across every worldview and every parameter draw, a decade with no major disruption is a tail outcome, not the base case. The interesting variance is not *whether* shocks arrive but whether they arrive spaced out or together.

## Scenario archetypes

Paths were clustered on which major events fired and on the shape of the systemic-stress trajectory. These are not scenarios written in advance and then assigned probabilities — they are the shapes the simulation actually produced, priced by how much of the path mass fell into each.

### Manageable decade — technological discontinuity and financial and macro stress — **36%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is technological discontinuity compounded by financial and macro stress. Typical peak stress sits at the 30th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI** — 100% here vs 83% overall
- **US recession with NBER-dated peak in the window** — 100% here vs 85% overall
- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — 100% here vs 90% overall

### Severe decade — climate stress and financial and macro stress — **32%**

Concurrent failure across domains. Shocks arrive faster than systems absorb them, and the response to one degrades the capacity to answer the next. The distinguishing driver is climate stress compounded by financial and macro stress. Typical peak stress sits at the 80th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — 100% here vs 90% overall
- **US recession with NBER-dated peak in the window** — 95% here vs 85% overall

### Manageable decade — climate stress — **22%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is climate stress. Typical peak stress sits at the 39th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — 100% here vs 90% overall
- US recession with NBER-dated peak in the window — *suppressed*: 46% here vs 85% overall
- A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI — *suppressed*: 42% here vs 83% overall

### Turbulent decade — great-power conflict — **5.0%**

Overlapping crises with intact institutions. Response capacity is strained but not exhausted, and recovery between shocks is incomplete. The distinguishing driver is great-power conflict. Typical peak stress sits at the 67th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — 88% here vs 77% overall
- The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) — *suppressed*: 0% here vs 90% overall

### Manageable decade — no dominant driver — **4.9%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 22th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) — *suppressed*: 0% here vs 90% overall
- Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) — *suppressed*: 60% here vs 77% overall
- A calendar year at or above 1.65C above pre-industrial — *suppressed*: 85% here vs 92% overall

## Full results by domain

### AI, compute & transformative technology

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | 12% | 55% | 76% | [36%–98%] | 9 | 2029Q4 |
| A top-4 US hyperscaler guides annual capex down year-over-year | 16% | 61% | 81% | [58%–97%] | 6 | 2029Q4 |
| China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab | 7.2% | 41% | 68% | [29%–98%] | 7 | 2030Q4 |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 20% | 49% | 67% | [37%–92%] | 7 | 2029Q3 |
| A single training run of ≥1e28 FLOP is publicly reported | 12% | 57% | 74% | [47%–97%] | 6 | 2029Q3 |
| US unemployment rate ≥6.0% for three consecutive months | 18% | 55% | 73% | [43%–97%] | 6 | 2029Q2 |
| A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 35% | 72% | 83% | [60%–98%] | 5 | 2028Q2 |
| Nvidia suffers a ≥50% peak-to-trough drawdown | 29% | 55% | 67% | [40%–91%] | 6 | 2028Q3 |
| US driverless robotaxi services exceed 5 million paid rides per week | 9.9% | 59% | 79% | [55%–98%] | 4 | 2029Q4 |
| A top-5 Western frontier lab exits frontier training | 9.8% | 36% | 52% | [28%–76%] | 6 | 2030Q1 |
| A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month | 21% | 45% | 59% | [27%–87%] | 5 | 2029Q1 |
| US licenses its current-flagship datacenter GPU for general commercial sale to China | 18% | 38% | 49% | [17%–85%] | 6 | 2029Q1 |
| A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections | 29% | 59% | 67% | [37%–93%] | 4 | 2028Q2 |
| US Congress enacts broad federal preemption of state AI laws | 19% | 41% | 53% | [25%–79%] | 5 | 2029Q1 |
| A top mathematics journal publishes a paper whose central theorem was found primarily by AI | 22% | 59% | 74% | [51%–97%] | 3 | 2029Q2 |
| A quantum computer publicly factors an RSA-2048 modulus | <0.5% | 2.8% | 11% | [3.6%–22%] | 8 | 2033Q3 |
| AI-assisted biological attack causing ≥10 deaths, officially confirmed | 1.6% | 4.3% | 9.4% | [2.0%–24%] | 9 | 2032Q2 |
| Binding US-China agreement on frontier AI compute or model thresholds | 1.6% | 8.5% | 17% | [4.5%–30%] | 4 | 2032Q1 |

<details><summary>Resolution criteria</summary>

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — METR (or a successor methodology it endorses) publishes a 50%-reliability time horizon of ≥167 hours of human-expert task time for a publicly deployed or externally evaluated frontier model.
- **A top-4 US hyperscaler guides annual capex down year-over-year** — Microsoft, Alphabet, Amazon, or Meta states in an official earnings release or call that its expected full-fiscal-year capital expenditures will be LOWER than the prior fiscal year's actual capex.
- **China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab** — Credible public confirmation (company announcement, government statement, or two independent major-outlet reports) that a China-built EUV scanner is exposing wafers in a commercial production fab, not merely a lab or prototype.
- **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** — A government agency, CERT, or the victim organization publicly confirms an attack in which AI agents autonomously executed the majority of intrusion steps, AND documented direct losses exceed $1B (2026 USD) or the attack disrupted power, water, telecom, or payments service for >1 million people for >6 hours.
- **A single training run of ≥1e28 FLOP is publicly reported** — Epoch AI, a lab's own technical report, or two independent credible technical analyses attribute ≥1e28 FLOP of training compute to a single model training run.
- **US unemployment rate ≥6.0% for three consecutive months** — BLS headline U-3 seasonally adjusted unemployment rate is at or above 6.0% in three consecutive monthly releases.
- **A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI** — A Fortune 500 (US) or Fortune Global 500 company announces a workforce reduction of ≥10,000 positions in a single announcement, and its official communications name AI/automation as the primary stated cause (not merely one factor among several).
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — Nvidia's split-adjusted closing share price falls at least 50% below its all-time closing high, at any point in the window.
- **US driverless robotaxi services exceed 5 million paid rides per week** — Publicly reported paid rides in fully driverless (no human safety operator in vehicle) commercial services in the US total ≥5,000,000 in a single week, summed across all operators.
- **A top-5 Western frontier lab exits frontier training** — One of OpenAI, Anthropic, Google DeepMind, xAI, or Meta Superintelligence Labs is acquired, dissolved, files for bankruptcy protection, or publicly announces it will stop pretraining frontier-scale models.
- **A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month** — A model developed by a China-headquartered organization holds the top overall rank on Artificial Analysis's Intelligence Index or LMArena's overall text leaderboard continuously for at least 30 days.
- **US licenses its current-flagship datacenter GPU for general commercial sale to China** — BIS policy permits general (not narrowly case-by-case) export to Chinese commercial customers of Nvidia's then-current top-of-line datacenter accelerator, within one product generation of the US-available flagship.
- **A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections** — A US state enacts into law (governor's signature or veto override) a moratorium, ban, or binding numerical cap on new datacenter grid interconnections above a stated size threshold, applying statewide.
- **US Congress enacts broad federal preemption of state AI laws** — A bill preempting state AI regulation across a broad category (beyond a single narrow domain like deepfakes) is signed into law by the President.
- **A top mathematics journal publishes a paper whose central theorem was found primarily by AI** — A paper appears in Annals of Mathematics, JAMS, Inventiones, Acta Mathematica, or Duke Mathematical Journal in which the authors explicitly state that the principal new theorem was discovered or proved primarily by an AI system rather than by the human authors.
- **A quantum computer publicly factors an RSA-2048 modulus** — A verifiable public demonstration in which a quantum computer factors a 2048-bit RSA modulus, with the factorization independently confirmed and the computation not reducible to classical pre-processing or special-structure moduli.
- **AI-assisted biological attack causing ≥10 deaths, officially confirmed** — A national government, WHO, or equivalent official body confirms a deliberate biological release causing ≥10 human deaths, and officially states that AI tools materially assisted the design, synthesis planning, or acquisition of the agent.
- **Binding US-China agreement on frontier AI compute or model thresholds** — The US and China both sign a treaty, executive agreement, or equivalent binding instrument containing specific, verifiable commitments on frontier AI training compute limits, model capability thresholds, or mutual inspection.

</details>

### Great-power conflict & geopolitics

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 57% | 69% | 77% | [54%–93%] | 8 | 2027Q2 |
| Durable Russia-Ukraine ceasefire (>=180 consecutive days) | 40% | 77% | 87% | [63%–98%] | 7 | 2028Q1 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 5.5% | 21% | 38% | [12%–73%] | 8 | 2031Q2 |
| North Korea conducts a seventh nuclear explosive test | 17% | 43% | 56% | [30%–81%] | 5 | 2029Q3 |
| The Islamic Republic ceases to govern Iran | 8.5% | 24% | 35% | [7.7%–73%] | 8 | 2030Q1 |
| New US-Russia agreement capping deployed strategic nuclear warheads | 11% | 30% | 44% | [13%–82%] | 6 | 2030Q1 |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 6.2% | 20% | 33% | [2.8%–70%] | 7 | 2031Q1 |
| India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months | 6.3% | 17% | 27% | [13%–49%] | 8 | 2030Q2 |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 5.4% | 18% | 26% | [2.5%–60%] | 8 | 2030Q1 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 5.1% | 14% | 21% | [5.8%–35%] | 9 | 2030Q2 |
| Direct US-PRC military exchange causing at least one fatality | 3.7% | 12% | 20% | [7.0%–38%] | 9 | 2031Q1 |
| NATO invokes Article 5 in response to a Russian attack | 2.7% | 9.6% | 14% | [4.4%–28%] | 10 | 2030Q3 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 1.5% | 6.5% | 14% | [3.6%–29%] | 10 | 2032Q2 |
| Lethal armed clash between Chinese and Japanese state forces | 2.9% | 9.3% | 16% | [2.0%–46%] | 8 | 2031Q2 |
| A jihadist insurgent group controls a Sahelian national capital for >=7 days | 7.6% | 19% | 25% | [7.4%–51%] | 5 | 2029Q3 |
| US initiates withdrawal from NATO, or any member formally invokes Article 13 | 2.4% | 4.7% | 8.3% | [2.8%–18%] | 9 | 2031Q1 |
| A nuclear weapon is detonated in an act of war or hostility anywhere in the world | 0.9% | 4.0% | 7.1% | [1.4%–19%] | 10 | 2031Q2 |
| UN Security Council permanent membership formally expanded | <0.5% | 2.3% | 5.8% | [4.2%–8.3%] | 3 | 2032Q4 |

<details><summary>Resolution criteria</summary>

- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — Crude-plus-condensate transit through Hormuz, per EIA/Vortexa/Kpler monthly data, falls below 50% of the 2025 monthly average for at least 30 consecutive days, in an episode beginning on or after 1 August 2026.
- **Durable Russia-Ukraine ceasefire (>=180 consecutive days)** — A ceasefire covering the entire land front between Russian and Ukrainian forces holds for at least 180 consecutive days without resumption of sustained offensive ground operations or systematic long-range strikes on cities, as assessed by ISW/OSCE-successor monitoring or equivalent consensus reporting. Short holiday truces (e.g. April/May 2026) do NOT count.
- **A state that does not now possess nuclear weapons tests a device or is confirmed to possess one** — Any state other than the US, Russia, UK, France, China, India, Pakistan, Israel and North Korea either (a) conducts a nuclear explosive test, (b) officially declares possession of an assembled nuclear weapon, or (c) is assessed by the IAEA or by the US intelligence community in a public statement to possess one.
- **North Korea conducts a seventh nuclear explosive test** — A nuclear explosive test on DPRK territory confirmed by CTBTO seismic/radionuclide detection or by US/ROK/Japanese government statement.
- **The Islamic Republic ceases to govern Iran** — The office of Supreme Leader (Velayat-e Faqih) is abolished, vacated without a successor for more than 90 days, or a government not derived from the clerical/IRGC establishment exercises effective control of Tehran; as assessed by consensus of major-power governments.
- **New US-Russia agreement capping deployed strategic nuclear warheads** — The US and Russia sign a bilateral agreement (treaty, executive agreement, or formal reciprocal political commitment announced by both heads of state) that establishes a numerical ceiling on deployed strategic nuclear warheads or delivery vehicles.
- **State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country** — A cyberattack publicly attributed by the victim government or by the EU/NATO to a state or state-sponsored actor causes loss of electrical supply to at least one million people for at least 24 consecutive hours in a NATO or OECD member state.
- **India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months** — Direct state-on-state armed conflict between Indian and Pakistani forces producing at least 1,000 combined military and civilian deaths within any rolling 12-month period, per UCDP or ACLED coding.
- **Iran tests or is confirmed to possess an assembled nuclear weapon** — Iran conducts a nuclear explosive test, publicly declares possession, or is publicly assessed by the IAEA or the US intelligence community to possess at least one assembled nuclear weapon.
- **PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days** — PRC state organs (PLA, Coast Guard or maritime authorities) publicly declare a quarantine, inspection regime or blockade of Taiwan's ports/airspace AND enforce it by boarding, turning back or interdicting at least ten commercial vessels or aircraft, sustained for at least seven consecutive days.
- **Direct US-PRC military exchange causing at least one fatality** — An exchange of fire (kinetic, including missile, air, naval or ground fire) between US and PLA/PAP/China Coast Guard forces resulting in at least one death on either side, acknowledged by either government or confirmed by credible multi-source reporting.
- **NATO invokes Article 5 in response to a Russian attack** — The North Atlantic Council formally invokes Article 5 of the Washington Treaty citing an armed attack attributable to Russia or Belarus.
- **PRC launches an amphibious or airborne assault on Taiwan's main island** — PLA forces conduct an opposed landing or airborne insertion on Taiwan proper (not offshore islands) involving at least 1,000 personnel, confirmed by Taiwan MND or US government statement.
- **Lethal armed clash between Chinese and Japanese state forces** — An exchange of fire or deliberate ramming between PLA/CCG and JSDF/JCG units resulting in at least one death, confirmed by either government.
- **A jihadist insurgent group controls a Sahelian national capital for >=7 days** — JNIM, ISSP/ISWAP or a successor jihadist organisation exercises effective control of Bamako, Ouagadougou or Niamey (including the presidential palace and central districts) for at least seven consecutive days, per ACLED coding or UN/Security Council reporting.
- **US initiates withdrawal from NATO, or any member formally invokes Article 13** — The US President formally notifies the depositary of intent to withdraw under Article 13 of the North Atlantic Treaty, or any other member state does so.
- **A nuclear weapon is detonated in an act of war or hostility anywhere in the world** — A nuclear explosive device is detonated with hostile intent against a state, non-state actor or territory (excluding tests, accidents and demonstration detonations over unpopulated own territory), confirmed by the detonating state or by CTBTO/national technical means.
- **UN Security Council permanent membership formally expanded** — An amendment to the UN Charter expanding the number of permanent Security Council members enters into force following ratification by two-thirds of member states including all five current permanent members.

</details>

### Climate & Earth systems

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | 82% | 93% | 96% | [89%–99%] | 6 | 2027Q1 |
| Global fossil CO2 emissions confirmed to have peaked | 8.7% | 50% | 79% | [56%–97%] | 7 | 2030Q3 |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | 72% | 85% | 90% | [79%–97%] | 5 | 2027Q1 |
| A calendar year at or above 1.65C above pre-industrial | 56% | 81% | 92% | [75%–99%] | 4 | 2027Q3 |
| Long-term (multi-decadal) 1.5C breach formally declared | 4.9% | 32% | 73% | [45%–97%] | 5 | 2032Q2 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 9.0% | 22% | 38% | [6.0%–81%] | 8 | 2030Q4 |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 13% | 30% | 50% | [23%–79%] | 6 | 2030Q3 |
| FAO Food Price Index exceeds 160 in any month | 19% | 35% | 49% | [26%–73%] | 6 | 2029Q2 |
| Single heat event with >= 100,000 attributed excess deaths | 8.3% | 26% | 42% | [19%–71%] | 7 | 2030Q4 |
| A new record warmest calendar year, exceeding 2024 | 79% | 94% | 97% | [91%–99%] | 3 | 2027Q1 |
| Combined Lake Powell + Lake Mead storage falls below 20% of capacity | 22% | 43% | 54% | [27%–84%] | 5 | 2028Q4 |
| Final court judgment ordering >= $1bn in climate damages | 4.6% | 17% | 34% | [7.2%–70%] | 6 | 2031Q4 |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 4.4% | 12% | 20% | [5.9%–42%] | 8 | 2030Q4 |
| Formal international SRM governance decision adopted | 7.6% | 24% | 39% | [12%–81%] | 4 | 2031Q1 |
| Global mean methane annual growth rate falls to zero or below | 3.8% | 16% | 30% | [5.2%–67%] | 5 | 2031Q3 |
| State-backed solar radiation management deployment announced or conducted | 1.6% | 6.7% | 16% | [2.7%–35%] | 8 | 2032Q4 |
| Arctic Ocean practically ice-free (extent below 1.0 million km2) | 0.7% | 4.3% | 22% | [7.7%–38%] | 5 | 2033Q3 |
| AMOC declared to have crossed a tipping point | 0.8% | 1.8% | 4.1% | [1.7%–9.3%] | 10 | 2032Q2 |

<details><summary>Resolution criteria</summary>

- **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** — NOAA Coral Reef Watch reports that Alert Level 1 or higher bleaching-level heat stress affected at least 60% of the world's coral reef area within any rolling 12-month period.
- **Global fossil CO2 emissions confirmed to have peaked** — The Global Carbon Project reports global fossil CO2 emissions below the previous all-time high in two consecutive calendar years, with the peak year identified in the published Global Carbon Budget.
- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — NOAA CPC's Oceanic Nino Index (3-month running mean Nino3.4 anomaly, ERSSTv5 with the operational base period) reaches or exceeds +2.0C for at least one overlapping season during the 2026-27 event.
- **A calendar year at or above 1.65C above pre-industrial** — ERA5 annual global mean surface temperature anomaly relative to 1850-1900 is >= 1.65C for a full calendar year, as published in the Copernicus Global Climate Highlights.
- **Long-term (multi-decadal) 1.5C breach formally declared** — The WMO, IPCC (in AR7 or a special report), or the UNFCCC Global Stocktake formally states that the long-term global mean temperature increase - defined as a 20-year mean or current human-induced warming - has exceeded 1.5C above 1850-1900.
- **Amazon basin becomes a net annual carbon source for three consecutive years** — Peer-reviewed literature (atmospheric inversion, aircraft profile, or eddy-covariance synthesis accepted by the Global Carbon Project) establishes that the Amazon basin as a whole was a net annual source of carbon to the atmosphere in three consecutive calendar years.
- **Verified wet-bulb temperature of 35C sustained for three or more hours** — A quality-controlled surface station observation (or a national meteorological service's official record) documents a wet-bulb temperature of at least 35.0C sustained for at least three consecutive hours, confirmed in a peer-reviewed publication or by a national met service.
- **FAO Food Price Index exceeds 160 in any month** — The FAO Food Price Index (nominal, 2014-2016 = 100) records a monthly value above 160.0, exceeding the March 2022 all-time high of 160.3.
- **Single heat event with >= 100,000 attributed excess deaths** — A peer-reviewed study or national statistical office attributes at least 100,000 excess deaths to a single heat wave or heat season within one country or contiguous region over a window of 90 days or less.
- **A new record warmest calendar year, exceeding 2024** — Copernicus ERA5 (with NASA GISTEMP and NOAA as corroboration) reports a calendar year with a global mean surface temperature anomaly exceeding the 2024 value (1.60C above 1850-1900) at the annual announcement in the following January.
- **Combined Lake Powell + Lake Mead storage falls below 20% of capacity** — US Bureau of Reclamation end-of-month reservoir reports show combined active storage in Lake Powell and Lake Mead below 20% of combined live capacity.
- **Final court judgment ordering >= $1bn in climate damages** — A court of final instance (highest domestic court, or a binding international tribunal) issues a non-appealable judgment ordering a state or a company to pay at least US$1 billion in damages, compensation, or a compliance fund specifically for climate change harms.
- **Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months** — The RAPID-MOCHA-WBTS array at 26N (or a successor observing system accepted as the reference by the AMOC research community) reports a 12-month running mean overturning transport at least 30% below the 2004-2023 mean, confirmed in a peer-reviewed publication.
- **Formal international SRM governance decision adopted** — UNEA, the UNFCCC COP, the CBD COP, or a comparable treaty body adopts a formal decision or instrument establishing an international governance framework for solar radiation modification (whether a non-use agreement, a research governance regime, or a moratorium codification), beyond the existing non-binding CBD language.
- **Global mean methane annual growth rate falls to zero or below** — NOAA GML reports a global mean CH4 annual increase of 0.0 ppb or less for a calendar year in its published trends series.
- **State-backed solar radiation management deployment announced or conducted** — A national government formally announces a stratospheric aerosol injection deployment programme (as distinct from research), or a state or state-backed entity conducts SAI at a scale exceeding 0.1 Tg of injected aerosol precursor per year, as confirmed by independent monitoring or official statement.
- **Arctic Ocean practically ice-free (extent below 1.0 million km2)** — NSIDC daily sea ice extent for the Arctic falls below 1.0 million km2 on at least one day.
- **AMOC declared to have crossed a tipping point** — A major assessment body (IPCC, WMO, or a National Academies-equivalent) or a strong majority of the published AMOC literature states that the AMOC has crossed a critical threshold and is on an irreversible trajectory toward collapse (maximum strength below 5 Sv) under current forcing.

</details>

### Global macroeconomy & finance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Sev | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| US recession with NBER-dated peak in the window | 34% | 66% | 85% | [62%–98%] | 6 | 2028Q4 |
| Global recession (world real GDP growth below 2.0% in a calendar year) | 12% | 38% | 63% | [33%–86%] | 7 | 2030Q4 |
| China reports annual real GDP growth below 4.0% | 18% | 52% | 71% | [43%–94%] | 6 | 2029Q3 |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 4.7% | 35% | 60% | [29%–92%] | 7 | 2031Q1 |
| Japan 10-year government bond yield reaches 3.00% | 25% | 49% | 60% | [31%–90%] | 7 | 2028Q3 |
| S&P 500 falls 30%+ from its all-time closing high | 16% | 46% | 64% | [37%–89%] | 6 | 2029Q4 |
| Brent crude settles above $120/bbl | 37% | 50% | 60% | [31%–87%] | 6 | 2027Q3 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 26% | 44% | 55% | [26%–83%] | 6 | 2028Q2 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 10% | 26% | 40% | [16%–65%] | 8 | 2030Q2 |
| Wave of emerging-market sovereign defaults or restructurings | 21% | 47% | 61% | [29%–86%] | 5 | 2029Q1 |
| China announces a central-government property/LGFV rescue of RMB 5trn or more | 21% | 42% | 52% | [16%–97%] | 5 | 2028Q4 |
| US average effective tariff rate exceeds 15% | 28% | 41% | 50% | [19%–88%] | 5 | 2027Q4 |
| US dollar share of allocated FX reserves falls below 50% | 1.9% | 18% | 39% | [16%–70%] | 6 | 2032Q2 |
| US 10-year Treasury yield closes at or above 6.00% | 5.0% | 18% | 29% | [9.9%–52%] | 8 | 2030Q4 |
| US CPI inflation returns to 5.0%+ year over year | 21% | 36% | 47% | [24%–72%] | 5 | 2028Q3 |
| Sustained effective closure of the Strait of Hormuz | 15% | 23% | 28% | [8.6%–53%] | 8 | 2027Q4 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 7.1% | 19% | 27% | [5.4%–61%] | 7 | 2030Q1 |
| Major stablecoin failure or sustained depeg | 16% | 31% | 40% | [9.5%–87%] | 4 | 2029Q1 |

<details><summary>Resolution criteria</summary>

- **US recession with NBER-dated peak in the window** — NBER Business Cycle Dating Committee assigns a business-cycle peak dated between August 2026 and the end of the stated year. Later announcement is fine; the peak date is what counts.
- **Global recession (world real GDP growth below 2.0% in a calendar year)** — IMF WEO (October vintage of the following year) reports world real GDP growth at market or PPP weights below 2.0% for any calendar year in the window. Resolves YES on the first such year.
- **China reports annual real GDP growth below 4.0%** — China's National Bureau of Statistics reports full-year real GDP growth below 4.0% for any calendar year in the window, in the initial annual release.
- **AI capex bust: aggregate hyperscaler capex falls 20%+ year over year** — Combined calendar-year capital expenditure of Microsoft, Alphabet, Amazon, Meta and Oracle, as reported in audited annual filings, comes in at least 20% below the prior calendar year's reported total, for any year in the window.
- **Japan 10-year government bond yield reaches 3.00%** — The 10-year JGB benchmark yield closes at or above 3.00% on any day in the window.
- **S&P 500 falls 30%+ from its all-time closing high** — S&P 500 records a daily close at least 30% below its prior all-time closing high, at any point in the window.
- **Brent crude settles above $120/bbl** — ICE Brent front-month futures settle at or above $120.00/bbl on any trading day in the window.
- **Large private-credit vehicle suspends redemptions or enters wind-down** — A private credit fund, BDC or interval fund with at least $20bn NAV fully suspends redemptions (beyond pro-rating within stated quarterly limits) for at least one month, or is placed into wind-down or forced sale, in the US, UK or EU.
- **Failure or extraordinary rescue of a bank with over $250bn in assets** — A bank holding company with more than $250bn in total assets in the US, EU, UK, Switzerland, Japan or China fails, is placed into resolution, is forced into a state-brokered merger, or receives an extraordinary government capital injection or central bank emergency liquidity facility created specifically for it.
- **Wave of emerging-market sovereign defaults or restructurings** — At least three additional sovereigns, each with more than $10bn in external public debt, default on external commercial debt or formally enter a comprehensive debt restructuring or a new IMF Extended Fund Facility of at least $3bn, between August 2026 and the end of the stated year.
- **China announces a central-government property/LGFV rescue of RMB 5trn or more** — China's State Council, MOF or PBOC announces a single package of central-government fiscal support, debt assumption or recapitalization directed at the property sector and/or local government financing vehicles totalling at least RMB 5 trillion, announced as one program.
- **US average effective tariff rate exceeds 15%** — Penn Wharton Budget Model or Yale Budget Lab reports a US average effective tariff rate on all imports above 15.0% for at least one full month in the window.
- **US dollar share of allocated FX reserves falls below 50%** — IMF COFER reports the US dollar share of allocated global foreign exchange reserves below 50.0% for any quarter in the window.
- **US 10-year Treasury yield closes at or above 6.00%** — The constant-maturity 10-year US Treasury yield (H.15 / Treasury daily par yield curve) closes at or above 6.00% on any day in the window.
- **US CPI inflation returns to 5.0%+ year over year** — BLS reports headline CPI-U at or above 5.0% year over year for any single month in the window.
- **Sustained effective closure of the Strait of Hormuz** — Seaborne crude and condensate transits through the Strait of Hormuz fall more than 50% below the 2025 monthly average for at least 14 consecutive days, per IEA, EIA, Kpler or Vortexa reporting, at any point from August 2026 onward.
- **France or Italy 10-year spread over Bunds exceeds 300bp** — The 10-year OAT-Bund or BTP-Bund spread closes above 300 basis points for five consecutive trading days, or the ECB formally activates the Transmission Protection Instrument for either sovereign.
- **Major stablecoin failure or sustained depeg** — A stablecoin with at least $20bn market capitalization trades more than 5% below its peg for more than 24 consecutive hours, or its issuer suspends or fails to honor redemptions for more than 24 hours.

</details>

## How bad decades begin

Among paths where at least three high-severity events fired, these are the most common opening sequences, in order of occurrence.

| Frequency | First | Then | Then |
|---:|---|---|---|
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | US recession with NBER-dated peak in the window | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) |
| <0.5% | Nvidia suffers a ≥50% peak-to-trough drawdown | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Large private-credit vehicle suspends redemptions or enters wind-down | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Brent crude settles above $120/bbl | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) |
| <0.5% | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | Nvidia suffers a ≥50% peak-to-trough drawdown | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Brent crude settles above $120/bbl | US recession with NBER-dated peak in the window |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | Brent crude settles above $120/bbl |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | Nvidia suffers a ≥50% peak-to-trough drawdown |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | FAO Food Price Index exceeds 160 in any month |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | Japan 10-year government bond yield reaches 3.00% | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China reports annual real GDP growth below 4.0% | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) |
| <0.5% | Nvidia suffers a ≥50% peak-to-trough drawdown | Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |

The most common opening — Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window → US recession with NBER-dated peak in the window → Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) — accounts for 0.4% of all paths. No single sequence dominates, which is itself informative: the model does not support a story in which one specific trigger reliably starts the cascade. What recurs is the *pattern* — a shock in one domain degrading the capacity to absorb the next.

## Where the correlations are

Pairs whose joint occurrence most exceeds what independence would predict. *Lift* is P(both) ÷ P(A)·P(B): a lift of 3 means these two show up together three times more often than chance. This is the part of the model that a spreadsheet of independent probabilities cannot produce, and it is where tail risk actually lives.

| Event A | Event B | P(both) | Lift | P(A given B) |
|---|---|---:|---:|---:|
| Large private-credit vehicle suspends redemptions or enters wind-down | Amazon basin becomes a net annual carbon source for three consecutive years | 22% | 1.1× | 58% |
| Failure or extraordinary rescue of a bank with over $250bn in assets | North Korea conducts a seventh nuclear explosive test | 24% | 1.0× | 42% |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | Amazon basin becomes a net annual carbon source for three consecutive years | 31% | 1.0× | 80% |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | Single heat event with >= 100,000 attributed excess deaths | 26% | 1.0× | 63% |
| Failure or extraordinary rescue of a bank with over $250bn in assets | A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 16% | 1.0× | 42% |
| Large private-credit vehicle suspends redemptions or enters wind-down | Failure or extraordinary rescue of a bank with over $250bn in assets | 23% | 1.0× | 57% |
| Global recession (world real GDP growth below 2.0% in a calendar year) | FAO Food Price Index exceeds 160 in any month | 32% | 1.0× | 65% |
| Global recession (world real GDP growth below 2.0% in a calendar year) | US average effective tariff rate exceeds 15% | 33% | 1.0× | 65% |
| Japan 10-year government bond yield reaches 3.00% | Single heat event with >= 100,000 attributed excess deaths | 26% | 1.0× | 62% |
| Failure or extraordinary rescue of a bank with over $250bn in assets | US dollar share of allocated FX reserves falls below 50% | 16% | 1.0× | 42% |
| FAO Food Price Index exceeds 160 in any month | US dollar share of allocated FX reserves falls below 50% | 20% | 1.0× | 51% |
| Large private-credit vehicle suspends redemptions or enters wind-down | US dollar share of allocated FX reserves falls below 50% | 23% | 1.0× | 57% |
| Large private-credit vehicle suspends redemptions or enters wind-down | A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 21% | 1.0× | 57% |
| US average effective tariff rate exceeds 15% | US dollar share of allocated FX reserves falls below 50% | 20% | 1.0× | 52% |
| Amazon basin becomes a net annual carbon source for three consecutive years | Verified wet-bulb temperature of 35C sustained for three or more hours | 20% | 1.0× | 39% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | Amazon basin becomes a net annual carbon source for three consecutive years | 30% | 1.0× | 78% |
| Brent crude settles above $120/bbl | US dollar share of allocated FX reserves falls below 50% | 24% | 1.0× | 62% |
| Large private-credit vehicle suspends redemptions or enters wind-down | Verified wet-bulb temperature of 35C sustained for three or more hours | 28% | 1.0× | 57% |

## Continuous indicators

These evolve on a Gaussian copula driven by each path's own systemic-stress index, so the bad tails of these distributions are populated by the same paths that fired the bad events — not by independent noise.

| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |
|---|---:|:---:|:---:|
| World military expenditure as share of global GDP (percent of global GDP) | 2.5 | 2.61 / **2.9** / 3.25 | 2.7 / **3.11** / 3.62 |
| Global state-based armed conflict battle deaths per year (thousands of deaths per year) | 160 | 53.3 / **132** / 250 | 13.9 / **113** / 270 |
| Brent crude oil price (USD per barrel (annual average)) | 86 | 44.8 / **73.1** / 139 | 27.3 / **65.1** / 156 |
| US military expenditure as share of US GDP (percent of GDP) | 3.2 | 2.94 / **3.3** / 3.7 | 2.87 / **3.36** / 3.88 |
| European NATO members' aggregate defence spending as share of GDP (percent of GDP) | 2.65 | 2.99 / **3.35** / 3.76 | 3.25 / **3.73** / 4.3 |
| PLA aircraft sorties entering Taiwan's ADIZ per year (sorties per year) | 3600 | 2.44e+03 / **5.04e+03** / 7.85e+03 | 2.14e+03 / **5.72e+03** / 9.6e+03 |
| US dollar share of allocated global FX reserves (percent) | 58 | 51 / **54** / 56.9 | 47.6 / **51.8** / 56 |
| Weekly container-ship transits of the Suez Canal (transits per week) | 30 | 22.4 / **61.9** / 87.6 | 23.3 / **78.7** / 115 |
| Combined US + Russia deployed strategic nuclear warheads (warheads) | 3200 | 3.15e+03 / **3.73e+03** / 4.36e+03 | 3.2e+03 / **4.01e+03** / 4.87e+03 |
| Net monthly Russian territorial gain in Ukraine (km2 per month (negative = Ukrainian recapture)) | 104 | -29.9 / **8.17** / 168 | -96.8 / **-43** / 191 |
| Number of active state-based armed conflicts (>=25 battle deaths/year) (count) | 61 | 47.8 / **58** / 68 | 42.6 / **56.2** / 70 |
| Crude and condensate transiting the Strait of Hormuz (million barrels per day) | 8 | 5.05 / **18** / 21 | 5.2 / **23.5** / 27.6 |
| Annual global mean surface temperature anomaly (ERA5, vs 1850-1900) (C) | 1.47 | 1.48 / **1.62** / 1.78 | 1.51 / **1.7** / 1.92 |
| Annual mean CO2 concentration at Mauna Loa (ppm) | 429.4 | 440 / **442** / 445 | 446 / **449** / 452 |
| NOAA global mean atmospheric methane (ppb) | 1945 | 1.97e+03 / **1.98e+03** / 2e+03 | 1.98e+03 / **2e+03** / 2.02e+03 |
| Global fossil CO2 emissions (Global Carbon Project) (GtCO2/yr) | 38.1 | 35.6 / **38.2** / 40.1 | 34.7 / **38.4** / 40.8 |
| Global mean sea level (satellite altimetry, above 1993 baseline) (mm) | 112 | 132 / **138** / 144 | 144 / **152** / 161 |
| Arctic sea ice September minimum extent (NSIDC) (million km2) | 4.3 | 3.34 / **3.98** / 4.53 | 2.94 / **3.79** / 4.57 |
| Annual maximum 3-month ONI (Nino3.4) (C) | 2.4 | -0.916 / **0.392** / 1.66 | -2.47 / **-0.689** / 1.09 |
| Share of global reef area under Alert Level 1+ heat stress, rolling 12 months (% of global reef area) | 55 | 32.1 / **62.1** / 88.4 | 25.4 / **66.2** / 103 |
| Brazilian Legal Amazon annual deforestation (INPE PRODES) (km2/yr) | 5796 | 3.12e+03 / **5e+03** / 9.79e+03 | 2e+03 / **4.58e+03** / 1.12e+04 |
| FAO Food Price Index (nominal) (index, 2014-2016 = 100) | 130.3 | 121 / **140** / 167 | 120 / **146** / 182 |
| Annual increase in global 0-2000m ocean heat content (ZJ/yr) | 23 | 12.7 / **25.1** / 36.7 | 9.06 / **26.1** / 42.5 |
| Brent crude oil price (USD per barrel) | 84 | 41.4 / **76.9** / 149 | 24 / **75.9** / 174 |
| US 10-year Treasury yield (percent) | 4.62 | 3.08 / **4.81** / 6.34 | 2.48 / **4.87** / 6.99 |
| US CPI inflation, year over year (percent) | 3.5 | 1.19 / **2.6** / 4.88 | 0.181 / **2.13** / 5.3 |
| Federal funds target rate, upper bound (percent) | 3.75 | 1.79 / **3.51** / 5.26 | 0.902 / **3.33** / 5.77 |
| S&P 500 index level (index points) | 7412 | 6.19e+03 / **1e+04** / 1.6e+04 | 6.12e+03 / **1.14e+04** / 1.99e+04 |
| Global real GDP growth (percent per year) | 3 | 1.59 / **3.2** / 4.21 | 1.17 / **3.27** / 4.69 |
| China reported real GDP growth (percent per year) | 4.6 | 1.87 / **3.4** / 4.8 | 0.697 / **2.76** / 4.65 |
| US federal debt held by the public / GDP (percent) | 100 | 106 / **111** / 119 | 110 / **117** / 128 |
| USD share of allocated FX reserves (IMF COFER) (percent) | 56.5 | 47.1 / **51.9** / 56.9 | 42.6 / **49.7** / 56.5 |
| Gold price (USD per troy ounce) | 4040 | 3.1e+03 / **4.71e+03** / 7.21e+03 | 2.85e+03 / **5.05e+03** / 8.57e+03 |
| USD/JPY exchange rate (yen per dollar) | 163.6 | 119 / **153** / 194 | 98.5 / **145** / 203 |
| US average effective tariff rate on all imports (percent) | 6 | 3.02 / **7.99** / 18.2 | 2.15 / **9.03** / 22.6 |
| Log10 of training compute for the largest publicly-known training run (log10(FLOP)) | 26.7 | 28 / **28.8** / 29.5 | 28.8 / **29.9** / 30.9 |
| Global data center electricity consumption (TWh per year) | 590 | 827 / **1.03e+03** / 1.34e+03 | 1.01e+03 / **1.27e+03** / 1.72e+03 |
| Combined annual capex, Microsoft + Alphabet + Amazon + Meta (USD billions per year) | 700 | 487 / **989** / 1.5e+03 | 435 / **1.14e+03** / 1.86e+03 |
| Nvidia annual data center revenue (USD billions per year) | 330 | 243 / **550** / 880 | 224 / **660** / 1.12e+03 |
| Combined annualized revenue run-rate, OpenAI + Anthropic (USD billions) | 72 | 161 / **356** / 613 | 242 / **505** / 870 |
| Log2 of METR 50%-reliability task time horizon (log2(hours of human-expert task time)) | 1.6 | 5.37 / **8.08** / 10.7 | 7.91 / **11.7** / 15.3 |
| Log10 of API price for GPT-4-class capability (log10(USD per million input tokens)) | -0.4 | -2.2 / **-1.8** / -1.4 | -3.13 / **-2.57** / -2 |
| Chinese open-weight models' share of OpenRouter tokens (percent) | 61 | 32.4 / **60.4** / 83.2 | 21.3 / **59.6** / 90.6 |
| Log10 of US paid fully-driverless rides per week (millions) (log10(millions of rides per week)) | -0.3 | 0.204 / **0.886** / 1.4 | 0.591 / **1.55** / 2.24 |
| US AI adoption in production, employment-weighted (Census BTOS) (percent of employment at AI-using firms) | 32 | 44.5 / **56** / 68.1 | 53.9 / **68.9** / 85.5 |

## What drives the outcome

Share of the variance in peak systemic stress attributable to each event firing at all. High-scoring nodes are the ones worth watching, because learning their resolution collapses the most uncertainty about everything else.

| Event | Variance share | P(by 2036) | Severity |
|---|---:|---:|---:|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | 2.0% | 76% | 9 |
| Sustained effective closure of the Strait of Hormuz | 1.8% | 28% | 8 |
| NATO invokes Article 5 in response to a Russian attack | 1.8% | 14% | 10 |
| Japan 10-year government bond yield reaches 3.00% | 1.6% | 60% | 7 |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 1.5% | 77% | 8 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 1.5% | 40% | 8 |
| Brent crude settles above $120/bbl | 1.4% | 60% | 6 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 1.3% | 21% | 9 |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 1.3% | 26% | 8 |
| China reports annual real GDP growth below 4.0% | 1.3% | 71% | 6 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 1.1% | 27% | 7 |
| Direct US-PRC military exchange causing at least one fatality | 1.0% | 20% | 9 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 1.0% | 14% | 10 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 1.0% | 38% | 8 |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 1.0% | 20% | 8 |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 1.0% | 67% | 7 |
| Global recession (world real GDP growth below 2.0% in a calendar year) | 0.9% | 63% | 7 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 0.9% | 38% | 8 |

## Where the worldviews disagree most

The five parameterisations — raw analyst, audited, outside-view base rates, structural-break inside view, and prediction-market check — converge on most nodes. These are the ones where they don't, and they are exactly the forecasts you should hold most loosely.

| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |
|---|---:|---:|---:|---:|---:|---:|
| Iran tests or is confirmed to possess an assembled nuclear weapon | 30% | 25% | 24% | 25% | 25% | 5pp |
| Amazon basin becomes a net annual carbon source for three consecutive years | 35% | 38% | 39% | 38% | 38% | 4pp |
| A jihadist insurgent group controls a Sahelian national capital for >=7 days | 24% | 28% | 25% | 25% | 26% | 3pp |
| Global mean methane annual growth rate falls to zero or below | 29% | 32% | 28% | 29% | 29% | 3pp |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 33% | 33% | 33% | 34% | 31% | 3pp |
| US average effective tariff rate exceeds 15% | 51% | 51% | 52% | 49% | 51% | 3pp |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 58% | 61% | 60% | 60% | 58% | 3pp |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 40% | 37% | 37% | 38% | 37% | 3pp |
| US recession with NBER-dated peak in the window | 85% | 84% | 86% | 84% | 85% | 3pp |
| US dollar share of allocated FX reserves falls below 50% | 41% | 39% | 40% | 38% | 40% | 3pp |
| Final court judgment ordering >= $1bn in climate damages | 35% | 33% | 35% | 32% | 32% | 3pp |
| A top-5 Western frontier lab exits frontier training | 53% | 53% | 53% | 51% | 52% | 3pp |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 39% | 40% | 42% | 41% | 39% | 3pp |
| Major stablecoin failure or sustained depeg | 40% | 42% | 40% | 39% | 41% | 3pp |
| The Islamic Republic ceases to govern Iran | 34% | 35% | 36% | 35% | 34% | 3pp |
| Durable Russia-Ukraine ceasefire (>=180 consecutive days) | 88% | 88% | 88% | 90% | 88% | 3pp |

## What this model cannot do

- **The parameters are elicited judgement, not measurement.** The engine is exact; the inputs are informed opinion, audited and red-teamed but still opinion. Simulation precision does not create forecast accuracy, and the 90% bands cover disagreement between the modelled worldviews, not the possibility that all five are wrong together.
- **Correlated error is unmodelled.** If the analysts share a blind spot, the ensemble inherits it silently and reports narrow bands over a wrong centre.
- **Resolution criteria carry real weight.** Several forecasts move by tens of percentage points on the wording of what counts. Read the criteria before quoting a number.
- **Nothing outside the risk set can happen.** The events that most reshape a decade are frequently ones nobody enumerated in advance. Treat the 'no severe event' probability as an upper bound on calm.
- **Causal edges are assumed, not estimated.** The dependency structure comes from domain reasoning about transmission channels, not from fitting historical co-occurrence — there is no dataset of decades to fit it to.
- **Hazards are conditionally memoryless within each segment.** Real crises have internal dynamics — mobilisation, negotiation, exhaustion — that a piecewise exponential cannot represent.
- *geopolitics*: Leadership mortality and succession are the largest unmodelled discontinuity. Putin (73), Trump (80), Khamenei's untested successor Mojtaba, Kim Jong Un's health, and Xi's post-purge PLA all sit on single points of failure. A single actuarial event could invert the sign of several of these forecasts within weeks, and no reference class gives useful conditional probabilities for what follows. The 2026 Iranian case shows that even an externally-imposed succession produces outcomes (short-run consolidation) opposite to the intuitive prediction.
- *climate*: The post-2023 warming acceleration is not fully explained. The 2023-24 jump exceeded CMIP6 expectations and candidate causes - declining planetary albedo from reduced low-cloud cover, aerosol unmasking, Hunga Tonga stratospheric water vapour - have very different implications. If reduced cloud cover is a genuine positive feedback newly engaged, every temperature trajectory here shifts up 0.2-0.4C by 2036 and effective climate sensitivity is higher than assumed. If it was a transient confluence, current anomalies partially relax and the trend reasserts at 0.25C/decade. This single uncertainty dominates the temperature distribution and I cannot resolve it.
- *economy*: AI as a genuine total factor productivity shock. If AI raises trend productivity growth by even 0.5-1.0pp, then debt/GDP paths, equity valuations at CAPE 40.9, and the sustainability of a 4.6% 10-year all look completely different — the denominator grows out of the problem, and what looks like a bubble is a correctly-priced regime change. Every risk in this model that is anchored on debt sustainability or valuation reversion is conditionally wrong in that world. Conversely, if AI capex proves to be a depreciating expense rather than a productive asset, the same nodes are far too optimistic. I have no reliable way to distinguish these ex ante and the model should be run under both regimes.
- *ai*: Measurement collapse: there is no agreed capability metric that survives saturation. MMLU is dead, HLE is at 53%, ARC-AGI-2 is at 85% while ARC-AGI-3 is under 1%, and METR's time-horizon figures differ by 6x across sources I searched this session. Every capability-conditioned probability in this model inherits that ambiguity, and 'AGI' questions may be permanently unresolvable rather than merely uncertain.

---

*Generated by the `worldsim` Monte Carlo engine. Parameters, dependency structure, and red-team corrections are in `params/`; rerun with `python run_simulation.py`.*
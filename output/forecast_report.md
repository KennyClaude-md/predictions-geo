# World Futures Simulation — Forecast Report

**Simulation date:** 2026-07-29  
**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  
**Paths:** 4,800 across 5 worldviews × 40 parameter worlds  
**Risk nodes:** 159 · **causal edges:** 0 · **latent factors:** 0 · **continuous variables:** 104

---

## How to read this

Every number below is the output of a survival-process Monte Carlo, not a guess written directly. Nine domains were parameterised against current sources, audited for base-rate discipline, then red-teamed from three directions. Each of those opinions is run as a separate worldview and the results are pooled by weight.

**The bracketed range is not the range of outcomes** — the event either happens or it doesn't. It is the range of *the probability itself* across parameter worlds: how much the answer moves depending on whose model of the world you accept. A wide bracket means the forecast is fragile. Monte Carlo noise has been subtracted out, so what remains is real disagreement.

**Calibration check:** simulated marginals reproduce the elicited cumulative probabilities to within 0.33 percentage points (worst node, worst worldview). This matters: the dependency network is tuned to reshape the *joint* distribution — which events co-occur — without inflating any individual probability above what the underlying analysis actually claimed.

## Headline forecasts

Ranked by expected systemic impact — probability by 2036 multiplied by severity — rather than by probability alone, because a 12% chance of something that reorders the world outranks a near-certainty that doesn't.

| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Impact |
|---|-------|--------:|--------:|--------:|:---------------:|----:|
| 1 | **Civil war onset in a country of 50 million or more that was at peace in mid-2026** | 41% | 75% | 88% | [68%–99%] | 8 |
| 2 | **Frontier agent reaches a 1-work-month 50%-reliability task horizon** | 13% | 56% | 77% | [36%–99%] | 9 |
| 3 | **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** | 56% | 69% | 74% | [46%–97%] | 8 |
| 4 | **China annual births fall below 7.0 million** | 46% | 92% | 97% | [90%–99%] | 6 |
| 5 | **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** | 82% | 93% | 96% | [89%–99%] | 6 |
| 6 | **US recession with NBER-dated peak in the window** | 33% | 66% | 85% | [54%–98%] | 6 |
| 7 | **China's officially reported population falls below 1.400 billion** | 57% | 96% | 98% | [92%–99%] | 5 |
| 8 | **China's extraterritorial rare-earth export control regime enters into force** | 45% | 64% | 70% | [45%–93%] | 7 |
| 9 | **China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab** | 5.3% | 41% | 69% | [30%–98%] | 7 |
| 10 | **New IPC/CH Famine (Phase 5) classification anywhere** | 74% | 93% | 97% | [91%–99%] | 5 |
| 11 | **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** | 18% | 48% | 68% | [37%–97%] | 7 |
| 12 | **A top-4 US hyperscaler guides annual capex down year-over-year** | 16% | 62% | 78% | [48%–98%] | 6 |
| 13 | **Single US political-violence attack killing ten or more people** | 28% | 59% | 75% | [45%–97%] | 6 |
| 14 | **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** | 73% | 85% | 89% | [73%–98%] | 5 |
| 15 | **A calendar year with three or more successful coups d'etat worldwide** | 52% | 80% | 88% | [64%–99%] | 5 |
| 16 | **A single training run of ≥1e28 FLOP is publicly reported** | 14% | 59% | 73% | [45%–93%] | 6 |
| 17 | **US unemployment rate ≥6.0% for three consecutive months** | 19% | 55% | 72% | [47%–96%] | 6 |
| 18 | **Global recession (world real GDP growth below 2.0% in a calendar year)** | 11% | 37% | 61% | [29%–86%] | 7 |
| 19 | **Japan 10-year government bond yield reaches 3.00%** | 26% | 49% | 60% | [35%–90%] | 7 |
| 20 | **Nvidia suffers a ≥50% peak-to-trough drawdown** | 30% | 57% | 70% | [42%–92%] | 6 |
| 21 | **China reports annual real GDP growth below 4.0%** | 18% | 52% | 70% | [38%–94%] | 6 |
| 22 | **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** | 22% | 42% | 52% | [28%–79%] | 8 |

## The decade in aggregate

Individual probabilities are the easy part. The question that actually determines how the 2030s feel is how many high-impact events land, and whether they land together.

**Read the impact rating carefully.** Analysts were asked for *global systemic impact if it occurs*, where 10 is civilization-altering — that is a measure of magnitude, not of badness. A transformative AI capability milestone legitimately scores 9 on it. These are high-impact events, not a count of catastrophes.

| Impact tier | Nodes | Expected count | Median | P(none) | P(≥2) | P(≥3) |
|---|---:|---:|---:|---:|---:|---:|
| **6+ / 10** | 84 | 35.1 | 35 | <0.5% | >99% | >99% |
| **7+ / 10** | 55 | 18.0 | 18 | <0.5% | >99% | >99% |
| **8+ / 10** | 36 | 9.7 | 10 | <0.5% | >99% | >99% |
| **9+ / 10** | 12 | 2.4 | 2 | 3.8% | 76% | 43% |

The 6+ band is broad — it contains a US recession alongside a Taiwan contingency — so the headline that the median decade fires 35 of its 84 nodes says less about danger than it first appears. The discriminating number is the tier above: across 12 nodes rated 9 or 10 for global impact, the model expects 2.4 of them this decade, puts 96% on at least one and 76% on two or more. That is the finding: a decade with no order-changing event is a minority outcome, and the interesting variance is not *whether* they arrive but whether they arrive spaced out or together.

**A caveat on cross-domain comparison.** Each domain was rated by a different analyst against the same nominal 0–10 scale, and they did not use it identically: *geopolitics* averages 8.1 while *demographics* averages 5.7 (overall 6.5). Some of that gap is real — great-power conflict genuinely carries more systemic weight than a macro data print — but some of it is rater drift, and it means the impact ranking tilts toward whichever domain scored most generously. Compare probabilities across domains freely; compare severities within a domain.

## Scenario archetypes

Paths were clustered on which major events fired and on the shape of the systemic-stress trajectory. These are not scenarios written in advance and then assigned probabilities — they are the shapes the simulation actually produced, priced by how much of the path mass fell into each.

### Manageable decade — financial and macro stress and institutional breakdown — **34%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is financial and macro stress compounded by institutional breakdown. Typical peak stress sits at the 32th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **China reports annual real GDP growth below 4.0%** — 100% here vs 70% overall
- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 100% here vs 88% overall

### Severe decade — financial and macro stress and institutional breakdown — **28%**

Concurrent failure across domains. Shocks arrive faster than systems absorb them, and the response to one degrades the capacity to answer the next. The distinguishing driver is financial and macro stress compounded by institutional breakdown. Typical peak stress sits at the 82th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **China reports annual real GDP growth below 4.0%** — 90% here vs 70% overall
- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 100% here vs 88% overall

### Manageable decade — institutional breakdown — **23%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is institutional breakdown. Typical peak stress sits at the 44th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — 100% here vs 88% overall
- China reports annual real GDP growth below 4.0% — *suppressed*: 0% here vs 70% overall

### Manageable decade — no dominant driver — **11%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 42th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- Civil war onset in a country of 50 million or more that was at peace in mid-2026 — *suppressed*: 0% here vs 88% overall

### Manageable decade — no dominant driver (variant) — **3.2%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 35th percentile of all simulated paths.

## Full results by domain

### Political stability & governance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Civil war onset in a country of 50 million or more that was at peace in mid-2026 | 41% | 75% | 88% | [68%–99%] | 8 | 2028Q1 |
| Democrats control at least one chamber of Congress from January 2027 | 88% | 90% | 92% | [86%–97%] | 5 | 2026Q4 |
| AfD enters government at German federal or Land level | 16% | 49% | 65% | [36%–90%] | 7 | 2029Q4 |
| Single US political-violence attack killing ten or more people | 28% | 59% | 75% | [45%–97%] | 6 | 2029Q1 |
| A calendar year with three or more successful coups d'etat worldwide | 52% | 80% | 88% | [64%–99%] | 5 | 2027Q3 |
| National Rally (or RN-aligned candidate) wins the French presidency | 44% | 44% | 62% | [39%–86%] | 7 | 2027Q2 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 22% | 42% | 52% | [28%–79%] | 8 | 2028Q3 |
| Overt US military strike inside Mexican territory without Mexican consent | 32% | 43% | 48% | [23%–75%] | 7 | 2027Q3 |
| The Islamic Republic of Iran ceases to exist as a governing system | 13% | 26% | 36% | [6.2%–73%] | 9 | 2029Q2 |
| Xi Jinping ceases to be CCP General Secretary | 4.6% | 16% | 35% | [6.0%–78%] | 9 | 2032Q2 |
| Vladimir Putin ceases to be Russia's paramount leader | 5.7% | 19% | 39% | [17%–61%] | 8 | 2032Q1 |
| US President formally invokes the Insurrection Act over a state's objection | 30% | 42% | 47% | [26%–73%] | 6 | 2027Q3 |
| Reform UK leads a UK government | 2.4% | 26% | 33% | [9.6%–69%] | 6 | 2030Q1 |
| US executive branch openly defies a final Supreme Court order | 9.6% | 17% | 21% | [2.7%–43%] | 9 | 2028Q2 |
| Armed confrontation between US state-controlled forces and federal forces | 7.1% | 14% | 17% | [2.3%–37%] | 8 | 2028Q4 |
| Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice | 4.9% | 12% | 18% | [7.5%–32%] | 7 | 2030Q2 |
| Trump formally pursues a third presidential term | 4.9% | 10% | 10% | [3.8%–20%] | 8 | 2028Q1 |
| An EU member state initiates exit from the EU | 2.0% | 5.9% | 10% | [3.3%–21%] | 8 | 2030Q4 |

<details><summary>Resolution criteria</summary>

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — A country with population of at least 50 million, not experiencing an armed conflict with at least 1,000 battle-related deaths in 2025, records at least 1,000 battle-related deaths in a single calendar year in an internal armed conflict, per UCDP/PRIO coding.
- **Democrats control at least one chamber of Congress from January 2027** — Following the 3 November 2026 elections, Democrats (including caucusing independents) hold a majority of seats in the US House and/or Senate when the new Congress convenes on 3 January 2027.
- **AfD enters government at German federal or Land level** — The AfD holds at least one ministerial post in a German federal or state (Land) government, or formally signs a written toleration/confidence-and-supply agreement supporting such a government. Issue-by-issue parliamentary cooperation does not count.
- **Single US political-violence attack killing ten or more people** — A single attack on US soil kills at least 10 people (excluding perpetrators) and is officially determined by federal law enforcement, or coded by START/GTD, as politically, religiously, racially or ideologically motivated. Ordinary criminal and non-ideological mass shootings excluded.
- **A calendar year with three or more successful coups d'etat worldwide** — In any single calendar year from 2026 onward, at least three successful coups d'etat occur globally, where 'successful' means the coup leadership holds effective power for at least seven days, per Powell-Thyne / Cline Center coding.
- **National Rally (or RN-aligned candidate) wins the French presidency** — A candidate endorsed by, or a member of, Rassemblement National (or its formal successor) is elected President of France in the 2027 or 2032 presidential election and inaugurated.
- **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** — In any V-Dem annual Democracy Report from 2027 through 2037, a NATO or EU member state that was coded as a liberal or electoral democracy in the 2026 report is coded as an electoral autocracy or closed autocracy. Turkey's and Hungary's pre-2026 coding do not qualify.
- **Overt US military strike inside Mexican territory without Mexican consent** — The US government publicly acknowledges, or three major wire services confirm, a US military kinetic strike (manned aircraft, drone, missile or ground raid) on a target inside Mexican sovereign territory that the Mexican federal government publicly states it did not consent to.
- **The Islamic Republic of Iran ceases to exist as a governing system** — A government controls Tehran that does not derive its authority from velayat-e faqih - the office of Supreme Leader is abolished, left vacant for more than 12 months with no successor, or subordinated to a non-clerical executive - sustained for at least 90 days.
- **Xi Jinping ceases to be CCP General Secretary** — Xi Jinping is no longer General Secretary of the Chinese Communist Party for a continuous period exceeding 60 days, for any reason.
- **Vladimir Putin ceases to be Russia's paramount leader** — Putin is no longer president of Russia (or, if the office is restructured, no longer the recognized paramount decision-maker) for a continuous period exceeding 60 days, through death, incapacity, resignation, removal or coup.
- **US President formally invokes the Insurrection Act over a state's objection** — A presidential proclamation expressly invoking 10 U.S.C. sections 251-255 (the Insurrection Act) to deploy federal troops or federalized National Guard for domestic law enforcement inside a US state whose governor has publicly objected, confirmed by the Federal Register and major wire services.
- **Reform UK leads a UK government** — A Reform UK MP is appointed Prime Minister of the United Kingdom.
- **US executive branch openly defies a final Supreme Court order** — The executive branch publicly and knowingly fails to comply with a final, non-stayed order of the US Supreme Court for more than 30 days, and this non-compliance is (a) asserted in a filing or opinion by the Court or a lower court on remand, or (b) reported as such by at least three of AP/Reuters/NYT/WSJ/WaPo. Slow-walking with a colorable legal argument does not count.
- **Armed confrontation between US state-controlled forces and federal forces** — A US governor issues an order directing state law enforcement or state-controlled National Guard to physically block or detain federal agents/troops, AND an armed confrontation occurs producing at least one death or at least one state officer detaining a federal officer (or vice versa) at gunpoint. Litigation, non-cooperation policies and protest-line scuffles do not count.
- **Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice** — A sitting US president, vice president, member of the House or Senate, Senate-confirmed cabinet secretary, or Supreme Court justice is killed in an attack determined by federal law enforcement to be politically, ideologically or personally-grievance motivated. Natural death, accident and ordinary criminal robbery excluded.
- **Trump formally pursues a third presidential term** — Donald Trump files FEC paperwork as a candidate for president in 2028, is placed on a primary ballot in any state as a presidential candidate, or is formally nominated as the Republican presidential or vice-presidential candidate for 2028.
- **An EU member state initiates exit from the EU** — An EU member state's government formally notifies the European Council under Article 50 TEU, or a nationally binding referendum on EU membership is held in a member state.

</details>

### AI, compute & transformative technology

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | 13% | 56% | 77% | [36%–99%] | 9 | 2029Q4 |
| China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab | 5.3% | 41% | 69% | [30%–98%] | 7 | 2031Q1 |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 18% | 48% | 68% | [37%–97%] | 7 | 2029Q4 |
| A top-4 US hyperscaler guides annual capex down year-over-year | 16% | 62% | 78% | [48%–98%] | 6 | 2029Q3 |
| A single training run of ≥1e28 FLOP is publicly reported | 14% | 59% | 73% | [45%–93%] | 6 | 2029Q3 |
| US unemployment rate ≥6.0% for three consecutive months | 19% | 55% | 72% | [47%–96%] | 6 | 2029Q3 |
| Nvidia suffers a ≥50% peak-to-trough drawdown | 30% | 57% | 70% | [42%–92%] | 6 | 2028Q3 |
| A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 36% | 72% | 83% | [53%–98%] | 5 | 2028Q2 |
| A top-5 Western frontier lab exits frontier training | 11% | 38% | 53% | [27%–80%] | 6 | 2030Q1 |
| US driverless robotaxi services exceed 5 million paid rides per week | 10.0% | 61% | 79% | [56%–97%] | 4 | 2029Q4 |
| US licenses its current-flagship datacenter GPU for general commercial sale to China | 22% | 42% | 52% | [16%–91%] | 6 | 2028Q3 |
| A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month | 20% | 46% | 57% | [31%–85%] | 5 | 2028Q4 |
| US Congress enacts broad federal preemption of state AI laws | 21% | 43% | 54% | [26%–82%] | 5 | 2029Q1 |
| A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections | 28% | 58% | 65% | [34%–90%] | 4 | 2028Q2 |
| A top mathematics journal publishes a paper whose central theorem was found primarily by AI | 22% | 59% | 74% | [45%–94%] | 3 | 2029Q2 |
| A quantum computer publicly factors an RSA-2048 modulus | <0.5% | 2.1% | 11% | [4.6%–21%] | 8 | 2033Q3 |
| Binding US-China agreement on frontier AI compute or model thresholds | 1.3% | 8.0% | 16% | [4.6%–30%] | 4 | 2032Q1 |
| AI-assisted biological attack causing ≥10 deaths, officially confirmed | 0.9% | 3.1% | 6.9% | [2.3%–16%] | 9 | 2032Q3 |

<details><summary>Resolution criteria</summary>

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — METR (or a successor methodology it endorses) publishes a 50%-reliability time horizon of ≥167 hours of human-expert task time for a publicly deployed or externally evaluated frontier model.
- **China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab** — Credible public confirmation (company announcement, government statement, or two independent major-outlet reports) that a China-built EUV scanner is exposing wafers in a commercial production fab, not merely a lab or prototype.
- **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** — A government agency, CERT, or the victim organization publicly confirms an attack in which AI agents autonomously executed the majority of intrusion steps, AND documented direct losses exceed $1B (2026 USD) or the attack disrupted power, water, telecom, or payments service for >1 million people for >6 hours.
- **A top-4 US hyperscaler guides annual capex down year-over-year** — Microsoft, Alphabet, Amazon, or Meta states in an official earnings release or call that its expected full-fiscal-year capital expenditures will be LOWER than the prior fiscal year's actual capex.
- **A single training run of ≥1e28 FLOP is publicly reported** — Epoch AI, a lab's own technical report, or two independent credible technical analyses attribute ≥1e28 FLOP of training compute to a single model training run.
- **US unemployment rate ≥6.0% for three consecutive months** — BLS headline U-3 seasonally adjusted unemployment rate is at or above 6.0% in three consecutive monthly releases.
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — Nvidia's split-adjusted closing share price falls at least 50% below its all-time closing high, at any point in the window.
- **A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI** — A Fortune 500 (US) or Fortune Global 500 company announces a workforce reduction of ≥10,000 positions in a single announcement, and its official communications name AI/automation as the primary stated cause (not merely one factor among several).
- **A top-5 Western frontier lab exits frontier training** — One of OpenAI, Anthropic, Google DeepMind, xAI, or Meta Superintelligence Labs is acquired, dissolved, files for bankruptcy protection, or publicly announces it will stop pretraining frontier-scale models.
- **US driverless robotaxi services exceed 5 million paid rides per week** — Publicly reported paid rides in fully driverless (no human safety operator in vehicle) commercial services in the US total ≥5,000,000 in a single week, summed across all operators.
- **US licenses its current-flagship datacenter GPU for general commercial sale to China** — BIS policy permits general (not narrowly case-by-case) export to Chinese commercial customers of Nvidia's then-current top-of-line datacenter accelerator, within one product generation of the US-available flagship.
- **A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month** — A model developed by a China-headquartered organization holds the top overall rank on Artificial Analysis's Intelligence Index or LMArena's overall text leaderboard continuously for at least 30 days.
- **US Congress enacts broad federal preemption of state AI laws** — A bill preempting state AI regulation across a broad category (beyond a single narrow domain like deepfakes) is signed into law by the President.
- **A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections** — A US state enacts into law (governor's signature or veto override) a moratorium, ban, or binding numerical cap on new datacenter grid interconnections above a stated size threshold, applying statewide.
- **A top mathematics journal publishes a paper whose central theorem was found primarily by AI** — A paper appears in Annals of Mathematics, JAMS, Inventiones, Acta Mathematica, or Duke Mathematical Journal in which the authors explicitly state that the principal new theorem was discovered or proved primarily by an AI system rather than by the human authors.
- **A quantum computer publicly factors an RSA-2048 modulus** — A verifiable public demonstration in which a quantum computer factors a 2048-bit RSA modulus, with the factorization independently confirmed and the computation not reducible to classical pre-processing or special-structure moduli.
- **Binding US-China agreement on frontier AI compute or model thresholds** — The US and China both sign a treaty, executive agreement, or equivalent binding instrument containing specific, verifiable commitments on frontier AI training compute limits, model capability thresholds, or mutual inspection.
- **AI-assisted biological attack causing ≥10 deaths, officially confirmed** — A national government, WHO, or equivalent official body confirms a deliberate biological release causing ≥10 human deaths, and officially states that AI tools materially assisted the design, synthesis planning, or acquisition of the agent.

</details>

### Great-power conflict & geopolitics

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Durable Russia-Ukraine ceasefire (>=180 consecutive days) | 41% | 78% | 87% | [65%–98%] | 7 | 2028Q1 |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 56% | 69% | 74% | [46%–97%] | 8 | 2027Q2 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 7.4% | 23% | 38% | [7.3%–75%] | 8 | 2030Q4 |
| The Islamic Republic ceases to govern Iran | 11% | 25% | 36% | [9.1%–72%] | 8 | 2029Q4 |
| North Korea conducts a seventh nuclear explosive test | 17% | 42% | 55% | [28%–83%] | 5 | 2029Q2 |
| New US-Russia agreement capping deployed strategic nuclear warheads | 9.5% | 28% | 42% | [11%–81%] | 6 | 2030Q2 |
| India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months | 5.9% | 18% | 29% | [14%–49%] | 8 | 2030Q3 |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 5.4% | 20% | 32% | [7.5%–67%] | 7 | 2030Q3 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 5.0% | 13% | 21% | [8.1%–38%] | 9 | 2030Q3 |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 5.4% | 14% | 22% | [2.0%–47%] | 8 | 2030Q2 |
| Direct US-PRC military exchange causing at least one fatality | 3.1% | 10.0% | 19% | [4.2%–39%] | 9 | 2031Q4 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 1.7% | 6.2% | 14% | [3.4%–27%] | 10 | 2032Q2 |
| NATO invokes Article 5 in response to a Russian attack | 2.8% | 7.9% | 13% | [5.4%–22%] | 10 | 2030Q4 |
| Lethal armed clash between Chinese and Japanese state forces | 2.5% | 9.1% | 15% | [2.0%–39%] | 8 | 2031Q1 |
| A jihadist insurgent group controls a Sahelian national capital for >=7 days | 6.2% | 18% | 24% | [10%–44%] | 5 | 2029Q4 |
| US initiates withdrawal from NATO, or any member formally invokes Article 13 | 2.5% | 5.7% | 9.6% | [3.3%–19%] | 9 | 2030Q4 |
| A nuclear weapon is detonated in an act of war or hostility anywhere in the world | 1.3% | 4.1% | 6.9% | [2.0%–17%] | 10 | 2031Q1 |
| UN Security Council permanent membership formally expanded | 0.6% | 3.0% | 6.8% | [3.4%–13%] | 3 | 2032Q2 |

<details><summary>Resolution criteria</summary>

- **Durable Russia-Ukraine ceasefire (>=180 consecutive days)** — A ceasefire covering the entire land front between Russian and Ukrainian forces holds for at least 180 consecutive days without resumption of sustained offensive ground operations or systematic long-range strikes on cities, as assessed by ISW/OSCE-successor monitoring or equivalent consensus reporting. Short holiday truces (e.g. April/May 2026) do NOT count.
- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — Crude-plus-condensate transit through Hormuz, per EIA/Vortexa/Kpler monthly data, falls below 50% of the 2025 monthly average for at least 30 consecutive days, in an episode beginning on or after 1 August 2026.
- **A state that does not now possess nuclear weapons tests a device or is confirmed to possess one** — Any state other than the US, Russia, UK, France, China, India, Pakistan, Israel and North Korea either (a) conducts a nuclear explosive test, (b) officially declares possession of an assembled nuclear weapon, or (c) is assessed by the IAEA or by the US intelligence community in a public statement to possess one.
- **The Islamic Republic ceases to govern Iran** — The office of Supreme Leader (Velayat-e Faqih) is abolished, vacated without a successor for more than 90 days, or a government not derived from the clerical/IRGC establishment exercises effective control of Tehran; as assessed by consensus of major-power governments.
- **North Korea conducts a seventh nuclear explosive test** — A nuclear explosive test on DPRK territory confirmed by CTBTO seismic/radionuclide detection or by US/ROK/Japanese government statement.
- **New US-Russia agreement capping deployed strategic nuclear warheads** — The US and Russia sign a bilateral agreement (treaty, executive agreement, or formal reciprocal political commitment announced by both heads of state) that establishes a numerical ceiling on deployed strategic nuclear warheads or delivery vehicles.
- **India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months** — Direct state-on-state armed conflict between Indian and Pakistani forces producing at least 1,000 combined military and civilian deaths within any rolling 12-month period, per UCDP or ACLED coding.
- **State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country** — A cyberattack publicly attributed by the victim government or by the EU/NATO to a state or state-sponsored actor causes loss of electrical supply to at least one million people for at least 24 consecutive hours in a NATO or OECD member state.
- **PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days** — PRC state organs (PLA, Coast Guard or maritime authorities) publicly declare a quarantine, inspection regime or blockade of Taiwan's ports/airspace AND enforce it by boarding, turning back or interdicting at least ten commercial vessels or aircraft, sustained for at least seven consecutive days.
- **Iran tests or is confirmed to possess an assembled nuclear weapon** — Iran conducts a nuclear explosive test, publicly declares possession, or is publicly assessed by the IAEA or the US intelligence community to possess at least one assembled nuclear weapon.
- **Direct US-PRC military exchange causing at least one fatality** — An exchange of fire (kinetic, including missile, air, naval or ground fire) between US and PLA/PAP/China Coast Guard forces resulting in at least one death on either side, acknowledged by either government or confirmed by credible multi-source reporting.
- **PRC launches an amphibious or airborne assault on Taiwan's main island** — PLA forces conduct an opposed landing or airborne insertion on Taiwan proper (not offshore islands) involving at least 1,000 personnel, confirmed by Taiwan MND or US government statement.
- **NATO invokes Article 5 in response to a Russian attack** — The North Atlantic Council formally invokes Article 5 of the Washington Treaty citing an armed attack attributable to Russia or Belarus.
- **Lethal armed clash between Chinese and Japanese state forces** — An exchange of fire or deliberate ramming between PLA/CCG and JSDF/JCG units resulting in at least one death, confirmed by either government.
- **A jihadist insurgent group controls a Sahelian national capital for >=7 days** — JNIM, ISSP/ISWAP or a successor jihadist organisation exercises effective control of Bamako, Ouagadougou or Niamey (including the presidential palace and central districts) for at least seven consecutive days, per ACLED coding or UN/Security Council reporting.
- **US initiates withdrawal from NATO, or any member formally invokes Article 13** — The US President formally notifies the depositary of intent to withdraw under Article 13 of the North Atlantic Treaty, or any other member state does so.
- **A nuclear weapon is detonated in an act of war or hostility anywhere in the world** — A nuclear explosive device is detonated with hostile intent against a state, non-state actor or territory (excluding tests, accidents and demonstration detonations over unpopulated own territory), confirmed by the detonating state or by CTBTO/national technical means.
- **UN Security Council permanent membership formally expanded** — An amendment to the UN Charter expanding the number of permanent Security Council members enters into force following ratification by two-thirds of member states including all five current permanent members.

</details>

### Demography & migration

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China annual births fall below 7.0 million | 46% | 92% | 97% | [90%–99%] | 6 | 2028Q1 |
| China's officially reported population falls below 1.400 billion | 57% | 96% | 98% | [92%–99%] | 5 | 2027Q3 |
| Best-available global TFR estimate falls below 2.1 | 2.5% | 18% | 59% | [21%–94%] | 7 | 2032Q4 |
| Japan annual births (Japanese nationals) fall below 600,000 | 40% | 90% | 96% | [82%–>99%] | 4 | 2028Q2 |
| India publishes provisional Census 2027 population totals | 45% | 93% | 96% | [82%–99%] | 4 | 2028Q1 |
| PISA 2025 shows no recovery in OECD-average mathematics | 59% | 59% | 59% | [36%–85%] | 6 | 2027Q1 |
| US total fertility rate falls below 1.50 | 5.3% | 36% | 66% | [35%–93%] | 5 | 2031Q2 |
| Global forced displacement exceeds 130 million | 12% | 33% | 46% | [20%–73%] | 6 | 2029Q4 |
| EU return hubs operationalized at scale | 14% | 42% | 55% | [17%–93%] | 5 | 2029Q3 |
| US Census Bureau officially reports negative net international migration | 24% | 39% | 44% | [9.8%–82%] | 6 | 2027Q4 |
| US life expectancy at birth reaches 80.0 years | 4.9% | 35% | 63% | [25%–98%] | 4 | 2031Q2 |
| Youth-led protests topple three or more Sub-Saharan African governments in a three-year window | 13% | 33% | 47% | [11%–92%] | 5 | 2029Q4 |
| China's population is revised down by 15 million or more | 3.6% | 25% | 31% | [2.4%–67%] | 6 | 2029Q4 |
| A G7 country cuts permanent immigration by three quarters | 4.8% | 14% | 21% | [3.6%–45%] | 7 | 2030Q1 |
| China's direct birth and childcare subsidies reach 0.5% of GDP | 2.6% | 19% | 31% | [5.0%–72%] | 4 | 2031Q1 |
| South Korea total fertility rate reaches 1.00 or above | 2.5% | 20% | 28% | [13%–48%] | 4 | 2030Q3 |

<details><summary>Resolution criteria</summary>

- **China annual births fall below 7.0 million** — China's National Bureau of Statistics reports annual births below 7,000,000 for any calendar year, in its regular January statistical communique or the annual Statistical Yearbook.
- **China's officially reported population falls below 1.400 billion** — NBS reports a year-end national population (mainland, excluding HK/Macau/Taiwan) below 1,400 million.
- **Best-available global TFR estimate falls below 2.1** — A UN DESA World Population Prospects revision (or UN Population Division estimate) reports a global total fertility rate below 2.10 for the then-current year.
- **Japan annual births (Japanese nationals) fall below 600,000** — Japan's MHLW Vital Statistics report annual births to Japanese nationals below 600,000 for any calendar year, in preliminary or final figures.
- **India publishes provisional Census 2027 population totals** — The Registrar General and Census Commissioner of India publishes provisional population totals from Census 2027, covering the population enumeration phase with a reference date of 1 March 2027.
- **PISA 2025 shows no recovery in OECD-average mathematics** — OECD PISA 2025 results report an OECD-average mathematics score equal to or below the PISA 2022 OECD-average mathematics score (472 points).
- **US total fertility rate falls below 1.50** — CDC/NCHS reports a US total fertility rate below 1,500 births per 1,000 women (i.e. TFR < 1.50) for any calendar year, provisional or final.
- **Global forced displacement exceeds 130 million** — UNHCR Global Trends (or Mid-Year Trends) reports total forcibly displaced persons exceeding 130,000,000 at any reporting date.
- **EU return hubs operationalized at scale** — At least three EU member states have transferred a cumulative total of 1,000 or more rejected asylum applicants or asylum seekers to designated 'return hubs' or processing centres in non-EU third countries under the Returns Regulation or bilateral arrangements, as documented by the European Commission, EUAA, or a major NGO monitor.
- **US Census Bureau officially reports negative net international migration** — A Census Bureau Vintage population estimates release (or an official Census Bureau revision) reports negative net international migration for any 12-month estimating period.
- **US life expectancy at birth reaches 80.0 years** — NCHS reports US period life expectancy at birth of 80.0 years or more for a single calendar year, in final or provisional mortality reports.
- **Youth-led protests topple three or more Sub-Saharan African governments in a three-year window** — In any rolling 36-month window, heads of state or heads of government in three or more Sub-Saharan African countries resign, are removed, or flee within 90 days of the onset of mass protests that contemporaneous major-outlet reporting characterizes as youth-led or 'Gen Z' protests.
- **China's population is revised down by 15 million or more** — An official Chinese government source (NBS communique, the 2030 national census, or a published statistical yearbook revision) reports a national population figure at least 15,000,000 below the previously published estimate for a comparable date.
- **A G7 country cuts permanent immigration by three quarters** — A G7 member's official annual permanent-residence/settlement admissions (e.g. US lawful permanent residents, Canada PR admissions, UK settlement grants) fall below 25% of that country's 2024 level for a full fiscal or calendar year, per the responsible national agency.
- **China's direct birth and childcare subsidies reach 0.5% of GDP** — Combined central and local government direct cash transfers for childbirth and childcare in China exceed 0.5% of nominal GDP in a single fiscal year, per Ministry of Finance budget documents or credible reporting aggregating central and provincial outlays.
- **South Korea total fertility rate reaches 1.00 or above** — Statistics Korea reports an annual total fertility rate of 1.00 or higher for any calendar year.

</details>

### Climate & Earth systems

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | 82% | 93% | 96% | [89%–99%] | 6 | 2027Q1 |
| Global fossil CO2 emissions confirmed to have peaked | 10% | 52% | 77% | [48%–97%] | 7 | 2030Q2 |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | 73% | 85% | 89% | [73%–98%] | 5 | 2027Q1 |
| A calendar year at or above 1.65C above pre-industrial | 54% | 82% | 93% | [77%–99%] | 4 | 2027Q3 |
| Long-term (multi-decadal) 1.5C breach formally declared | 4.6% | 33% | 73% | [42%–97%] | 5 | 2032Q1 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 7.9% | 23% | 39% | [10%–79%] | 8 | 2031Q1 |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 12% | 29% | 50% | [27%–76%] | 6 | 2031Q1 |
| Single heat event with >= 100,000 attributed excess deaths | 8.1% | 24% | 42% | [18%–71%] | 7 | 2031Q1 |
| A new record warmest calendar year, exceeding 2024 | 79% | 94% | 97% | [91%–99%] | 3 | 2027Q1 |
| FAO Food Price Index exceeds 160 in any month | 18% | 34% | 49% | [18%–83%] | 6 | 2029Q2 |
| Combined Lake Powell + Lake Mead storage falls below 20% of capacity | 25% | 44% | 56% | [30%–82%] | 5 | 2028Q3 |
| Final court judgment ordering >= $1bn in climate damages | 4.3% | 17% | 35% | [9.7%–71%] | 6 | 2032Q1 |
| Formal international SRM governance decision adopted | 8.4% | 26% | 40% | [11%–84%] | 4 | 2030Q3 |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 4.2% | 11% | 19% | [1.8%–44%] | 8 | 2031Q2 |
| Global mean methane annual growth rate falls to zero or below | 3.8% | 15% | 28% | [5.6%–57%] | 5 | 2031Q3 |
| State-backed solar radiation management deployment announced or conducted | 0.9% | 4.8% | 14% | [2.5%–36%] | 8 | 2033Q2 |
| Arctic Ocean practically ice-free (extent below 1.0 million km2) | <0.5% | 3.3% | 21% | [7.7%–41%] | 5 | 2034Q1 |
| AMOC declared to have crossed a tipping point | 0.6% | 2.1% | 5.5% | [2.0%–13%] | 10 | 2032Q4 |

<details><summary>Resolution criteria</summary>

- **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** — NOAA Coral Reef Watch reports that Alert Level 1 or higher bleaching-level heat stress affected at least 60% of the world's coral reef area within any rolling 12-month period.
- **Global fossil CO2 emissions confirmed to have peaked** — The Global Carbon Project reports global fossil CO2 emissions below the previous all-time high in two consecutive calendar years, with the peak year identified in the published Global Carbon Budget.
- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — NOAA CPC's Oceanic Nino Index (3-month running mean Nino3.4 anomaly, ERSSTv5 with the operational base period) reaches or exceeds +2.0C for at least one overlapping season during the 2026-27 event.
- **A calendar year at or above 1.65C above pre-industrial** — ERA5 annual global mean surface temperature anomaly relative to 1850-1900 is >= 1.65C for a full calendar year, as published in the Copernicus Global Climate Highlights.
- **Long-term (multi-decadal) 1.5C breach formally declared** — The WMO, IPCC (in AR7 or a special report), or the UNFCCC Global Stocktake formally states that the long-term global mean temperature increase - defined as a 20-year mean or current human-induced warming - has exceeded 1.5C above 1850-1900.
- **Amazon basin becomes a net annual carbon source for three consecutive years** — Peer-reviewed literature (atmospheric inversion, aircraft profile, or eddy-covariance synthesis accepted by the Global Carbon Project) establishes that the Amazon basin as a whole was a net annual source of carbon to the atmosphere in three consecutive calendar years.
- **Verified wet-bulb temperature of 35C sustained for three or more hours** — A quality-controlled surface station observation (or a national meteorological service's official record) documents a wet-bulb temperature of at least 35.0C sustained for at least three consecutive hours, confirmed in a peer-reviewed publication or by a national met service.
- **Single heat event with >= 100,000 attributed excess deaths** — A peer-reviewed study or national statistical office attributes at least 100,000 excess deaths to a single heat wave or heat season within one country or contiguous region over a window of 90 days or less.
- **A new record warmest calendar year, exceeding 2024** — Copernicus ERA5 (with NASA GISTEMP and NOAA as corroboration) reports a calendar year with a global mean surface temperature anomaly exceeding the 2024 value (1.60C above 1850-1900) at the annual announcement in the following January.
- **FAO Food Price Index exceeds 160 in any month** — The FAO Food Price Index (nominal, 2014-2016 = 100) records a monthly value above 160.0, exceeding the March 2022 all-time high of 160.3.
- **Combined Lake Powell + Lake Mead storage falls below 20% of capacity** — US Bureau of Reclamation end-of-month reservoir reports show combined active storage in Lake Powell and Lake Mead below 20% of combined live capacity.
- **Final court judgment ordering >= $1bn in climate damages** — A court of final instance (highest domestic court, or a binding international tribunal) issues a non-appealable judgment ordering a state or a company to pay at least US$1 billion in damages, compensation, or a compliance fund specifically for climate change harms.
- **Formal international SRM governance decision adopted** — UNEA, the UNFCCC COP, the CBD COP, or a comparable treaty body adopts a formal decision or instrument establishing an international governance framework for solar radiation modification (whether a non-use agreement, a research governance regime, or a moratorium codification), beyond the existing non-binding CBD language.
- **Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months** — The RAPID-MOCHA-WBTS array at 26N (or a successor observing system accepted as the reference by the AMOC research community) reports a 12-month running mean overturning transport at least 30% below the 2004-2023 mean, confirmed in a peer-reviewed publication.
- **Global mean methane annual growth rate falls to zero or below** — NOAA GML reports a global mean CH4 annual increase of 0.0 ppb or less for a calendar year in its published trends series.
- **State-backed solar radiation management deployment announced or conducted** — A national government formally announces a stratospheric aerosol injection deployment programme (as distinct from research), or a state or state-backed entity conducts SAI at a scale exceeding 0.1 Tg of injected aerosol precursor per year, as confirmed by independent monitoring or official statement.
- **Arctic Ocean practically ice-free (extent below 1.0 million km2)** — NSIDC daily sea ice extent for the Arctic falls below 1.0 million km2 on at least one day.
- **AMOC declared to have crossed a tipping point** — A major assessment body (IPCC, WMO, or a National Academies-equivalent) or a strong majority of the published AMOC literature states that the AMOC has crossed a critical threshold and is on an irreversible trajectory toward collapse (maximum strength below 5 Sv) under current forcing.

</details>

### Global macroeconomy & finance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| US recession with NBER-dated peak in the window | 33% | 66% | 85% | [54%–98%] | 6 | 2028Q4 |
| Global recession (world real GDP growth below 2.0% in a calendar year) | 11% | 37% | 61% | [29%–86%] | 7 | 2030Q4 |
| Japan 10-year government bond yield reaches 3.00% | 26% | 49% | 60% | [35%–90%] | 7 | 2028Q3 |
| China reports annual real GDP growth below 4.0% | 18% | 52% | 70% | [38%–94%] | 6 | 2029Q3 |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 7.9% | 40% | 58% | [20%–98%] | 7 | 2030Q2 |
| S&P 500 falls 30%+ from its all-time closing high | 14% | 45% | 64% | [35%–90%] | 6 | 2030Q1 |
| Brent crude settles above $120/bbl | 33% | 49% | 59% | [35%–85%] | 6 | 2027Q4 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 29% | 48% | 57% | [30%–82%] | 6 | 2027Q4 |
| Wave of emerging-market sovereign defaults or restructurings | 25% | 49% | 62% | [32%–91%] | 5 | 2028Q4 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 9.5% | 26% | 39% | [19%–62%] | 8 | 2030Q1 |
| US average effective tariff rate exceeds 15% | 32% | 43% | 53% | [19%–91%] | 5 | 2027Q3 |
| China announces a central-government property/LGFV rescue of RMB 5trn or more | 20% | 40% | 51% | [17%–89%] | 5 | 2028Q4 |
| US CPI inflation returns to 5.0%+ year over year | 22% | 36% | 47% | [24%–76%] | 5 | 2028Q2 |
| US 10-year Treasury yield closes at or above 6.00% | 5.5% | 18% | 29% | [13%–51%] | 8 | 2030Q4 |
| US dollar share of allocated FX reserves falls below 50% | 2.2% | 17% | 38% | [17%–60%] | 6 | 2032Q2 |
| Sustained effective closure of the Strait of Hormuz | 15% | 22% | 28% | [11%–47%] | 8 | 2027Q4 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 9.8% | 24% | 31% | [6.2%–69%] | 7 | 2029Q3 |
| Major stablecoin failure or sustained depeg | 15% | 30% | 40% | [9.3%–78%] | 4 | 2029Q2 |

<details><summary>Resolution criteria</summary>

- **US recession with NBER-dated peak in the window** — NBER Business Cycle Dating Committee assigns a business-cycle peak dated between August 2026 and the end of the stated year. Later announcement is fine; the peak date is what counts.
- **Global recession (world real GDP growth below 2.0% in a calendar year)** — IMF WEO (October vintage of the following year) reports world real GDP growth at market or PPP weights below 2.0% for any calendar year in the window. Resolves YES on the first such year.
- **Japan 10-year government bond yield reaches 3.00%** — The 10-year JGB benchmark yield closes at or above 3.00% on any day in the window.
- **China reports annual real GDP growth below 4.0%** — China's National Bureau of Statistics reports full-year real GDP growth below 4.0% for any calendar year in the window, in the initial annual release.
- **AI capex bust: aggregate hyperscaler capex falls 20%+ year over year** — Combined calendar-year capital expenditure of Microsoft, Alphabet, Amazon, Meta and Oracle, as reported in audited annual filings, comes in at least 20% below the prior calendar year's reported total, for any year in the window.
- **S&P 500 falls 30%+ from its all-time closing high** — S&P 500 records a daily close at least 30% below its prior all-time closing high, at any point in the window.
- **Brent crude settles above $120/bbl** — ICE Brent front-month futures settle at or above $120.00/bbl on any trading day in the window.
- **Large private-credit vehicle suspends redemptions or enters wind-down** — A private credit fund, BDC or interval fund with at least $20bn NAV fully suspends redemptions (beyond pro-rating within stated quarterly limits) for at least one month, or is placed into wind-down or forced sale, in the US, UK or EU.
- **Wave of emerging-market sovereign defaults or restructurings** — At least three additional sovereigns, each with more than $10bn in external public debt, default on external commercial debt or formally enter a comprehensive debt restructuring or a new IMF Extended Fund Facility of at least $3bn, between August 2026 and the end of the stated year.
- **Failure or extraordinary rescue of a bank with over $250bn in assets** — A bank holding company with more than $250bn in total assets in the US, EU, UK, Switzerland, Japan or China fails, is placed into resolution, is forced into a state-brokered merger, or receives an extraordinary government capital injection or central bank emergency liquidity facility created specifically for it.
- **US average effective tariff rate exceeds 15%** — Penn Wharton Budget Model or Yale Budget Lab reports a US average effective tariff rate on all imports above 15.0% for at least one full month in the window.
- **China announces a central-government property/LGFV rescue of RMB 5trn or more** — China's State Council, MOF or PBOC announces a single package of central-government fiscal support, debt assumption or recapitalization directed at the property sector and/or local government financing vehicles totalling at least RMB 5 trillion, announced as one program.
- **US CPI inflation returns to 5.0%+ year over year** — BLS reports headline CPI-U at or above 5.0% year over year for any single month in the window.
- **US 10-year Treasury yield closes at or above 6.00%** — The constant-maturity 10-year US Treasury yield (H.15 / Treasury daily par yield curve) closes at or above 6.00% on any day in the window.
- **US dollar share of allocated FX reserves falls below 50%** — IMF COFER reports the US dollar share of allocated global foreign exchange reserves below 50.0% for any quarter in the window.
- **Sustained effective closure of the Strait of Hormuz** — Seaborne crude and condensate transits through the Strait of Hormuz fall more than 50% below the 2025 monthly average for at least 14 consecutive days, per IEA, EIA, Kpler or Vortexa reporting, at any point from August 2026 onward.
- **France or Italy 10-year spread over Bunds exceeds 300bp** — The 10-year OAT-Bund or BTP-Bund spread closes above 300 basis points for five consecutive trading days, or the ECB formally activates the Transmission Protection Instrument for either sovereign.
- **Major stablecoin failure or sustained depeg** — A stablecoin with at least $20bn market capitalization trades more than 5% below its peg for more than 24 consecutive hours, or its issuer suspends or fails to honor redemptions for more than 24 hours.

</details>

### Energy systems & critical materials

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China's extraterritorial rare-earth export control regime enters into force | 45% | 64% | 70% | [45%–93%] | 7 | 2027Q3 |
| China energy-related CO2 emissions decline three consecutive years | 11% | 50% | 72% | [38%–98%] | 5 | 2030Q1 |
| Global oil demand declines year-on-year outside recession or supply shock | 9.3% | 41% | 67% | [24%–98%] | 5 | 2030Q4 |
| Strait of Hormuz closed again for 14+ consecutive days | 22% | 33% | 40% | [21%–63%] | 8 | 2027Q4 |
| Firm load shedding in a major US RTO | 23% | 55% | 68% | [39%–92%] | 4 | 2028Q4 |
| LME copper exceeds $15,000/tonne | 13% | 38% | 53% | [17%–92%] | 5 | 2029Q4 |
| A Western SMR delivers first commercial grid power | 4.1% | 57% | 86% | [59%–98%] | 3 | 2030Q3 |
| Severe rare-earth supply cutoff to the US or EU | 14% | 26% | 32% | [13%–61%] | 8 | 2028Q3 |
| Brent monthly average above $120/bbl | 14% | 30% | 41% | [17%–68%] | 6 | 2029Q3 |
| Cyberattack causes a major OECD power outage | 9.8% | 27% | 40% | [11%–81%] | 6 | 2030Q1 |
| Global coal demand falls 3%+ below the 2025 level | 12% | 54% | 79% | [53%–98%] | 3 | 2030Q1 |
| Brent monthly average below $45/bbl | 18% | 36% | 47% | [23%–77%] | 4 | 2029Q1 |
| Lithium carbonate price exceeds $40,000/tonne | 18% | 38% | 46% | [13%–86%] | 4 | 2028Q4 |
| Annual global solar PV installations exceed 1,000 GW | 10% | 58% | 79% | [51%–98%] | 2 | 2029Q4 |
| European gas price returns to crisis levels | 12% | 25% | 31% | [12%–52%] | 5 | 2029Q1 |
| Coordinated physical attack causes a major OECD outage | 5.8% | 19% | 31% | [6.1%–72%] | 5 | 2030Q4 |
| Nuclear accident rated INES Level 5 or above | 3.9% | 12% | 19% | [3.8%–39%] | 6 | 2030Q3 |
| Global installed water electrolysis capacity reaches 25 GW | 1.6% | 18% | 40% | [19%–68%] | 2 | 2032Q2 |

<details><summary>Resolution criteria</summary>

- **China's extraterritorial rare-earth export control regime enters into force** — The October 2025 expanded rare-earth export control measures (extraterritorial 0.1% de minimis provisions and expanded element list) are in legal force and being applied to licence applications for at least 30 consecutive days, per MOFCOM announcements, at any point before the stated year-end.
- **China energy-related CO2 emissions decline three consecutive years** — IEA or CREA reports China's energy-related CO2 emissions declining year-on-year in three consecutive calendar years, with the third such year at or before the stated year.
- **Global oil demand declines year-on-year outside recession or supply shock** — IEA Oil Market Report reports total global oil demand for a calendar year below the preceding calendar year, in a year with positive global real GDP growth above 2% and no Hormuz-class supply disruption. 2026 is excluded from resolution due to the Hormuz shock.
- **Strait of Hormuz closed again for 14+ consecutive days** — Commercial tanker transits through the Strait of Hormuz fall below 25% of the 2025 daily average for 14 or more consecutive days, per Lloyd's List / Kpler / IEA Oil Market Report tracking, at any point after 1 Aug 2026.
- **Firm load shedding in a major US RTO** — PJM, ERCOT, MISO or SPP orders involuntary firm load shed (rolling blackouts) affecting 500,000 or more customers during a declared capacity or energy emergency.
- **LME copper exceeds $15,000/tonne** — LME 3-month copper settles above $15,000/tonne (nominal USD) on a monthly average basis.
- **A Western SMR delivers first commercial grid power** — A small modular reactor (nameplate under 300 MWe) in an OECD member country, excluding South Korea's existing SMART-class designs, synchronises to the grid and delivers commercial electricity, confirmed by the national regulator or IAEA PRIS.
- **Severe rare-earth supply cutoff to the US or EU** — Chinese exports of NdPr oxide/metal or heavy rare earths (Dy, Tb) to either the United States or the European Union fall by more than 50% year-on-year for three or more consecutive months, per China customs data.
- **Brent monthly average above $120/bbl** — The calendar-month average of front-month Brent futures settlements exceeds $120.00/bbl (nominal USD) in any month after 1 Aug 2026, per ICE settlement data.
- **Cyberattack causes a major OECD power outage** — A cyber intrusion causes loss of electricity supply to 500,000 or more customers for 6 or more hours in an OECD member country, with cyber causation publicly confirmed by the relevant national CERT, regulator or system operator.
- **Global coal demand falls 3%+ below the 2025 level** — IEA reports global coal demand (Mt or Mtce) for some calendar year at or before the stated year at least 3% below the reported 2025 level, confirming structural decline rather than noise.
- **Brent monthly average below $45/bbl** — The calendar-month average of front-month Brent futures settlements falls below $45.00/bbl (nominal USD) in any month after 1 Aug 2026.
- **Lithium carbonate price exceeds $40,000/tonne** — Battery-grade lithium carbonate, China spot (SMM or Fastmarkets assessment), exceeds $40,000/tonne on a monthly average basis.
- **Annual global solar PV installations exceed 1,000 GW** — Global solar PV capacity additions in a calendar year exceed 1,000 GWdc, as reported by BNEF, IEA or SolarPower Europe.
- **European gas price returns to crisis levels** — TTF front-month natural gas futures settle above EUR 100/MWh on any trading day.
- **Coordinated physical attack causes a major OECD outage** — A deliberate physical attack (sabotage, arson, gunfire, explosive) causes loss of electricity supply to 500,000 or more customers for 24 or more hours in an OECD member country, confirmed as deliberate by law enforcement.
- **Nuclear accident rated INES Level 5 or above** — The IAEA International Nuclear Event Scale assigns a rating of Level 5 (accident with wider consequences) or higher to an event at a civil nuclear power reactor or spent fuel facility anywhere in the world.
- **Global installed water electrolysis capacity reaches 25 GW** — IEA Global Hydrogen Review reports cumulative installed and operating water electrolysis capacity worldwide of 25 GW or more.

</details>

### Food, water & agriculture

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| New IPC/CH Famine (Phase 5) classification anywhere | 74% | 93% | 97% | [91%–99%] | 5 | 2027Q1 |
| Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously | 25% | 54% | 68% | [39%–93%] | 6 | 2029Q1 |
| GRFC reports more than 300 million people in acute food insecurity | 41% | 66% | 74% | [50%–96%] | 5 | 2027Q4 |
| FAO Food Price Index reaches an all-time high above 160 | 18% | 43% | 60% | [29%–87%] | 6 | 2029Q3 |
| World cereal production falls 4%+ year-on-year (multi-breadbasket failure) | 8.9% | 28% | 45% | [22%–72%] | 8 | 2030Q3 |
| World Bank monthly urea price exceeds US$800/tonne | 44% | 58% | 66% | [42%–90%] | 5 | 2027Q2 |
| WFP annual contributions fall below US$5 billion | 34% | 57% | 64% | [35%–90%] | 5 | 2027Q4 |
| Ukrainian seaborne grain exports fall below 1 Mt in a calendar month | 63% | 70% | 73% | [45%–97%] | 4 | 2027Q1 |
| Thai 5% broken rice benchmark exceeds US$650/tonne | 9.1% | 29% | 41% | [20%–69%] | 7 | 2030Q1 |
| Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months | 49% | 75% | 86% | [68%–98%] | 3 | 2027Q4 |
| Three or more countries/territories in confirmed IPC Famine simultaneously | 11% | 27% | 35% | [7.1%–81%] | 7 | 2029Q3 |
| India physically curtails Indus western-river flows to Pakistan | 6.9% | 22% | 34% | [17%–53%] | 7 | 2030Q3 |
| World cereal stocks-to-use ratio falls below 28% | 6.4% | 23% | 34% | [18%–54%] | 7 | 2030Q2 |
| Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab | 5.6% | 15% | 26% | [2.7%–60%] | 8 | 2031Q1 |
| Hormuz fertilizer flows normalise (downside-risk-off event) | 57% | 85% | 93% | [78%–99%] | 2 | 2027Q3 |
| Colorado River enters 2027 without an agreed post-2026 framework | 47% | 50% | 52% | [27%–75%] | 3 | 2027Q1 |
| Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water | 3.7% | 8.8% | 13% | [4.3%–26%] | 8 | 2030Q1 |

<details><summary>Resolution criteria</summary>

- **New IPC/CH Famine (Phase 5) classification anywhere** — The IPC Famine Review Committee or a CH equivalent confirms Famine (IPC Phase 5) — with reasonable evidence or higher — for at least one geographic area not already so classified as of 2026-07-29, published on ipcinfo.org.
- **Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously** — Per the IFPRI Food and Fertilizer Export Restrictions Tracker, at least two countries each ranking in the global top 10 for wheat, maize or rice exports have in force, simultaneously and for at least 60 consecutive days, a new (post-2026-07-29) export ban or quota estimated to cut that country's exports of the staple by 25% or more.
- **GRFC reports more than 300 million people in acute food insecurity** — Any edition of the Global Report on Food Crises published in 2027-2036 reports more than 300.0 million people in IPC/CH Phase 3 or above for its reference year.
- **FAO Food Price Index reaches an all-time high above 160** — The FAO Food Price Index (2014-2016=100, nominal) monthly value exceeds 160.0, surpassing the March 2022 record of 160.3.
- **World cereal production falls 4%+ year-on-year (multi-breadbasket failure)** — FAO's Cereal Supply and Demand Brief reports world cereal production for a calendar year at least 4.0% below the prior year's outturn (using FAO's own revised series at the time of the following year's July brief).
- **World Bank monthly urea price exceeds US$800/tonne** — World Bank Pink Sheet monthly average urea (Middle East, bulk, f.o.b.) exceeds US$800 per tonne in any month.
- **WFP annual contributions fall below US$5 billion** — WFP's published annual contribution total for any calendar year 2026-2036 is below US$5.0 billion (nominal), per wfp.org contributions data.
- **Ukrainian seaborne grain exports fall below 1 Mt in a calendar month** — Ukrainian Ministry of Agrarian Policy or UGA monthly data show total seaborne grain and oilseed exports below 1.0 million tonnes in any single calendar month (normal 2024-26 range ~3-5 Mt/month).
- **Thai 5% broken rice benchmark exceeds US$650/tonne** — FAO GIEWS / Thai Rice Exporters Association monthly average f.o.b. price for Thai white rice 5% broken exceeds US$650 per tonne.
- **Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months** — USDA, Eurostat, WOAH or the national statistical agency of a G20 member reports a decline of 10% or more, within any rolling 12-month window, in national laying-hen inventory or national pig inventory, attributed principally to an animal disease epizootic (HPAI, ASF, FMD or successor).
- **Three or more countries/territories in confirmed IPC Famine simultaneously** — At any point in a calendar year, IPC/FRC-confirmed Famine (Phase 5) classifications are simultaneously in force for areas in three or more distinct countries or territories.
- **India physically curtails Indus western-river flows to Pakistan** — Pakistan's IRSA rim-station data, corroborated by satellite/independent hydrological analysis, show a sustained reduction of 20% or more over at least four consecutive weeks in Chenab or Jhelum inflows attributable to Indian storage operations or diversion, and not to natural hydrology.
- **World cereal stocks-to-use ratio falls below 28%** — FAO's Cereal Supply and Demand Brief reports a world cereal stocks-to-use ratio below 28.0% for any marketing year.
- **Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab** — CIMMYT, BGRI, FAO or a national plant protection agency confirms establishment of a Ug99-lineage stem rust race, a novel highly virulent stripe rust race defeating deployed resistance, or wheat blast (Magnaporthe oryzae Triticum), in Indian or Pakistani Punjab or Haryana, with documented field-scale infection.
- **Hormuz fertilizer flows normalise (downside-risk-off event)** — World Bank or IFA data show Middle East seaborne urea and ammonia export volumes recovering to 90% or more of their 2024-25 monthly average for three consecutive months.
- **Colorado River enters 2027 without an agreed post-2026 framework** — On 1 January 2027, no seven-state consensus agreement and no signed federal Record of Decision governs Lake Powell/Lake Mead operations for calendar 2027, with operations instead running under an interim stopgap, unilateral federal action, or litigation.
- **Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water** — ACLED or equivalent records a state-attributed kinetic attack (air, missile, drone or special-forces) on the Grand Ethiopian Renaissance Dam or associated Ethiopian water infrastructure, or a direct armed exchange between Egyptian and Ethiopian forces publicly framed by either government as arising from the Nile water dispute.

</details>

### Pandemics, biosecurity & global health

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| US federal government de-recommends a core routine childhood vaccine and the change survives | 44% | 58% | 62% | [25%–97%] | 6 | 2027Q2 |
| United States formally loses measles elimination status | 80% | 87% | 89% | [71%–98%] | 4 | 2027Q1 |
| Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases | 53% | 55% | 55% | [21%–90%] | 6 | 2027Q1 |
| Two consecutive years of rising global new HIV infections | 7.0% | 43% | 51% | [14%–92%] | 6 | 2029Q3 |
| WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency | 56% | 92% | 97% | [91%–99%] | 3 | 2027Q3 |
| WHO declares an influenza pandemic (any subtype) | 5.7% | 19% | 33% | [16%–52%] | 8 | 2031Q1 |
| PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly | 53% | 79% | 84% | [58%–98%] | 3 | 2027Q3 |
| A newly emerged pathogen causes at least 1 million cumulative deaths worldwide | 4.0% | 14% | 25% | [2.7%–58%] | 10 | 2031Q2 |
| Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin | 5.2% | 19% | 33% | [6.5%–72%] | 7 | 2031Q1 |
| WHO Pandemic Agreement enters into force | 2.2% | 51% | 75% | [48%–97%] | 3 | 2030Q2 |
| Sustained human-to-human transmission of an H5 influenza virus | 4.2% | 13% | 23% | [8.1%–42%] | 9 | 2031Q1 |
| US reports at least 5,000 confirmed measles cases in a single calendar year | 13% | 41% | 55% | [31%–78%] | 3 | 2029Q4 |
| United States formally rejoins the World Health Organization | 1.5% | 23% | 37% | [15%–62%] | 4 | 2031Q1 |
| Global interruption of wild poliovirus type 1 transmission | 2.7% | 26% | 46% | [22%–71%] | 3 | 2031Q2 |
| Ebola causes a confirmed secondary transmission chain outside Africa | 13% | 22% | 30% | [9.8%–56%] | 4 | 2028Q4 |
| Deliberate biological attack causes at least 10 confirmed human deaths | 1.8% | 5.9% | 12% | [1.9%–30%] | 8 | 2031Q4 |
| Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution | 2.0% | 6.0% | 10% | [1.8%–28%] | 7 | 2031Q1 |
| WHO declares a global emergency over an antimicrobial-resistant pathogen | 0.9% | 4.7% | 9.5% | [3.1%–20%] | 5 | 2032Q1 |

<details><summary>Resolution criteria</summary>

- **US federal government de-recommends a core routine childhood vaccine and the change survives** — CDC's published child and adolescent immunization schedule removes a currently universally-recommended antigen (MMR, DTaP, IPV, Hib, PCV, rotavirus, varicella, or the hepatitis B birth dose) from universal recommendation - moving it to shared clinical decision-making, risk-based, or off-schedule - and that change is in effect and not judicially stayed for at least 6 continuous months.
- **United States formally loses measles elimination status** — PAHO's Regional Verification Commission (or WHO) formally announces that the United States no longer meets measles elimination criteria, or the US government/CDC publicly acknowledges loss of elimination status.
- **Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases** — WHO/AFRO situation reports for the outbreak declared 15 May 2026 (or its recognized continuation) record at least 10,000 cumulative laboratory-confirmed cases across all affected countries.
- **Two consecutive years of rising global new HIV infections** — UNAIDS reports annual new HIV infections higher than the preceding year in two consecutive reporting years, reversing the multi-decade decline.
- **WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency** — WHO's Director-General determines a new Public Health Emergency of International Concern (or pandemic emergency under the amended IHR) for an event distinct from the standing polio PHEIC and the Ebola Bundibugyo PHEIC declared 17 May 2026, at any point in the window.
- **WHO declares an influenza pandemic (any subtype)** — WHO formally declares an influenza pandemic, or declares a PHEIC/pandemic emergency for a novel influenza A virus with confirmed sustained community-level human-to-human transmission in at least two WHO regions.
- **PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly** — A World Health Assembly (regular or special session) formally adopts the Pathogen Access and Benefit-Sharing annex to the WHO Pandemic Agreement.
- **A newly emerged pathogen causes at least 1 million cumulative deaths worldwide** — A pathogen not endemically circulating in humans as of 1 Jan 2026 is credibly estimated by WHO, IHME, or a peer-reviewed consensus source to have caused at least 1,000,000 cumulative human deaths (reported or excess) within the stated horizon.
- **Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin** — A national government, law enforcement agency, or frontier AI developer publicly confirms a specific incident in which AI systems materially assisted a person or group in designing, acquiring, or synthesizing a pathogen or toxin of biosecurity concern (beyond generic capability-evaluation results or red-team exercises).
- **WHO Pandemic Agreement enters into force** — The 60th instrument of ratification, acceptance, approval or accession to the WHO Pandemic Agreement is deposited, bringing the Agreement into force.
- **Sustained human-to-human transmission of an H5 influenza virus** — WHO or a national health authority publicly confirms an H5 (any neuraminidase) influenza cluster with at least three sequential generations of human-to-human transmission, or a cluster of at least 10 epidemiologically linked human cases with no plausible animal or environmental exposure for the majority.
- **US reports at least 5,000 confirmed measles cases in a single calendar year** — CDC's official measles surveillance reports at least 5,000 confirmed cases for any single calendar year within the window.
- **United States formally rejoins the World Health Organization** — The United States formally notifies WHO of resumption of membership, or deposits an instrument of acceptance of the WHO Constitution, and pays or commits to assessed contributions.
- **Global interruption of wild poliovirus type 1 transmission** — Zero wild poliovirus type 1 cases with onset in any 12 consecutive calendar months, per GPEI reporting, with the 12-month window closing inside the horizon.
- **Ebola causes a confirmed secondary transmission chain outside Africa** — A national health authority in a country outside the WHO African Region confirms at least one locally acquired Ebola (any species) infection in a person who was not infected in Africa, at any point in the window.
- **Deliberate biological attack causes at least 10 confirmed human deaths** — A government or international body attributes at least 10 human deaths to a deliberate release of a biological agent (state or non-state actor) in a single incident or campaign.
- **Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution** — A national health authority, WHO, or an official government investigation publicly attributes an outbreak of at least 50 laboratory-confirmed human infections to a laboratory-acquired infection or a containment/biosafety breach.
- **WHO declares a global emergency over an antimicrobial-resistant pathogen** — WHO declares a PHEIC, pandemic emergency, or equivalent formal global health emergency whose primary basis is an antimicrobial-resistant bacterial or fungal pathogen (for example pan-resistant Klebsiella, XDR typhoid, Candida auris, or drug-resistant gonorrhoea).

</details>

## How bad decades begin

Among paths where at least three high-severity events fired, these are the most common opening sequences, in order of occurrence.

| Frequency | First | Then | Then |
|---:|---|---|---|
| 0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China's extraterritorial rare-earth export control regime enters into force |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | US Census Bureau officially reports negative net international migration |
| <0.5% | Nvidia suffers a ≥50% peak-to-trough drawdown | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | US recession with NBER-dated peak in the window |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | Japan 10-year government bond yield reaches 3.00% |
| <0.5% | US unemployment rate ≥6.0% for three consecutive months | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Nvidia suffers a ≥50% peak-to-trough drawdown | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million |
| <0.5% | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |
| <0.5% | PISA 2025 shows no recovery in OECD-average mathematics | China's extraterritorial rare-earth export control regime enters into force | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China annual births fall below 7.0 million |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | China's extraterritorial rare-earth export control regime enters into force |

The most common opening — Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window → China annual births fall below 7.0 million → PISA 2025 shows no recovery in OECD-average mathematics — accounts for 0.5% of all paths. No single sequence dominates, which is itself informative: the model does not support a story in which one specific trigger reliably starts the cascade. What recurs is the *pattern* — a shock in one domain degrading the capacity to absorb the next.

## Where the correlations are

Pairs whose joint occurrence most exceeds what independence would predict. *Lift* is P(both) ÷ P(A)·P(B): a lift of 3 means these two show up together three times more often than chance. This is the part of the model that a spreadsheet of independent probabilities cannot produce, and it is where tail risk actually lives.

| Event A | Event B | P(both) | Lift | P(A given B) |
|---|---|---:|---:|---:|
| Global recession (world real GDP growth below 2.0% in a calendar year) | AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 36% | 1.0× | 62% |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | S&P 500 falls 30%+ from its all-time closing high | 38% | 1.0× | 60% |
| A single training run of ≥1e28 FLOP is publicly reported | Best-available global TFR estimate falls below 2.1 | 44% | 1.0× | 74% |
| Japan 10-year government bond yield reaches 3.00% | AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 36% | 1.0× | 62% |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | GRFC reports more than 300 million people in acute food insecurity | 44% | 1.0× | 59% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | FAO Food Price Index reaches an all-time high above 160 | 47% | 1.0× | 78% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | Japan 10-year government bond yield reaches 3.00% | 47% | 1.0× | 78% |
| Japan 10-year government bond yield reaches 3.00% | S&P 500 falls 30%+ from its all-time closing high | 39% | 1.0× | 62% |
| China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab | US unemployment rate ≥6.0% for three consecutive months | 51% | 1.0× | 71% |
| Best-available global TFR estimate falls below 2.1 | FAO Food Price Index reaches an all-time high above 160 | 36% | 1.0× | 60% |
| Global recession (world real GDP growth below 2.0% in a calendar year) | S&P 500 falls 30%+ from its all-time closing high | 40% | 1.0× | 62% |
| US federal government de-recommends a core routine childhood vaccine and the change survives | FAO Food Price Index reaches an all-time high above 160 | 38% | 1.0× | 64% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | Single US political-violence attack killing ten or more people | 58% | 1.0× | 78% |
| S&P 500 falls 30%+ from its all-time closing high | US federal government de-recommends a core routine childhood vaccine and the change survives | 41% | 1.0× | 65% |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | US unemployment rate ≥6.0% for three consecutive months | 50% | 1.0× | 69% |
| US recession with NBER-dated peak in the window | Best-available global TFR estimate falls below 2.1 | 51% | 1.0× | 86% |
| Best-available global TFR estimate falls below 2.1 | S&P 500 falls 30%+ from its all-time closing high | 38% | 1.0× | 60% |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 47% | 1.0× | 91% |

## Continuous indicators

These evolve on a Gaussian copula driven by each path's own systemic-stress index, so the bad tails of these distributions are populated by the same paths that fired the bad events — not by independent noise.

| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |
|---|---:|:---:|:---:|
| World military expenditure as share of global GDP (percent of global GDP) | 2.5 | 2.6 / **2.89** / 3.24 | 2.7 / **3.12** / 3.59 |
| Global state-based armed conflict battle deaths per year (thousands of deaths per year) | 160 | 56.3 / **129** / 243 | 8.6 / **114** / 270 |
| Brent crude oil price (USD per barrel (annual average)) | 86 | 44.4 / **71.8** / 138 | 26.7 / **63.8** / 156 |
| US military expenditure as share of US GDP (percent of GDP) | 3.2 | 2.96 / **3.3** / 3.71 | 2.86 / **3.35** / 3.92 |
| European NATO members' aggregate defence spending as share of GDP (percent of GDP) | 2.65 | 3.01 / **3.36** / 3.76 | 3.24 / **3.72** / 4.28 |
| PLA aircraft sorties entering Taiwan's ADIZ per year (sorties per year) | 3600 | 2.42e+03 / **4.97e+03** / 7.78e+03 | 2.16e+03 / **5.79e+03** / 9.65e+03 |
| US dollar share of allocated global FX reserves (percent) | 58 | 50.9 / **54** / 57 | 47.7 / **51.8** / 55.9 |
| Weekly container-ship transits of the Suez Canal (transits per week) | 30 | 22 / **62** / 88.2 | 23.1 / **79.9** / 114 |
| Combined US + Russia deployed strategic nuclear warheads (warheads) | 3200 | 3.14e+03 / **3.71e+03** / 4.34e+03 | 3.22e+03 / **4.02e+03** / 4.87e+03 |
| Net monthly Russian territorial gain in Ukraine (km2 per month (negative = Ukrainian recapture)) | 104 | -29.3 / **10.2** / 180 | -96.6 / **-42.5** / 188 |
| Number of active state-based armed conflicts (>=25 battle deaths/year) (count) | 61 | 48 / **58** / 68.4 | 42.6 / **56.2** / 69.7 |
| Crude and condensate transiting the Strait of Hormuz (million barrels per day) | 8 | 5 / **18** / 21.1 | 5.77 / **23.5** / 27.6 |
| Annual global mean surface temperature anomaly (ERA5, vs 1850-1900) (C) | 1.47 | 1.48 / **1.62** / 1.78 | 1.5 / **1.71** / 1.93 |
| Annual mean CO2 concentration at Mauna Loa (ppm) | 429.4 | 440 / **442** / 445 | 446 / **449** / 453 |
| NOAA global mean atmospheric methane (ppb) | 1945 | 1.97e+03 / **1.98e+03** / 2e+03 | 1.98e+03 / **2e+03** / 2.02e+03 |
| Global fossil CO2 emissions (Global Carbon Project) (GtCO2/yr) | 38.1 | 35.5 / **38.3** / 40.1 | 34.7 / **38.5** / 41 |
| Global mean sea level (satellite altimetry, above 1993 baseline) (mm) | 112 | 132 / **138** / 144 | 144 / **152** / 160 |
| Arctic sea ice September minimum extent (NSIDC) (million km2) | 4.3 | 3.36 / **3.97** / 4.56 | 2.94 / **3.79** / 4.59 |
| Annual maximum 3-month ONI (Nino3.4) (C) | 2.4 | -0.888 / **0.428** / 1.7 | -2.43 / **-0.708** / 1.15 |
| Share of global reef area under Alert Level 1+ heat stress, rolling 12 months (% of global reef area) | 55 | 32.8 / **62.2** / 88.6 | 23.4 / **65.4** / 102 |
| Brazilian Legal Amazon annual deforestation (INPE PRODES) (km2/yr) | 5796 | 3.11e+03 / **4.86e+03** / 9.7e+03 | 1.89e+03 / **4.47e+03** / 1.11e+04 |
| FAO Food Price Index (nominal) (index, 2014-2016 = 100) | 130.3 | 121 / **141** / 168 | 119 / **145** / 182 |
| Annual increase in global 0-2000m ocean heat content (ZJ/yr) | 23 | 12.9 / **24.8** / 36.9 | 9.69 / **25.8** / 42.4 |
| Brent crude oil price (USD per barrel) | 84 | 41.1 / **78.4** / 151 | 23.6 / **74.7** / 175 |
| US 10-year Treasury yield (percent) | 4.62 | 3.08 / **4.8** / 6.31 | 2.59 / **4.91** / 7.01 |
| US CPI inflation, year over year (percent) | 3.5 | 1.21 / **2.59** / 4.85 | 0.18 / **2.1** / 5.25 |
| Federal funds target rate, upper bound (percent) | 3.75 | 1.76 / **3.52** / 5.28 | 0.936 / **3.42** / 5.79 |
| S&P 500 index level (index points) | 7412 | 6.09e+03 / **9.96e+03** / 1.61e+04 | 6.09e+03 / **1.14e+04** / 1.99e+04 |
| Global real GDP growth (percent per year) | 3 | 1.62 / **3.22** / 4.23 | 1.11 / **3.32** / 4.67 |
| China reported real GDP growth (percent per year) | 4.6 | 1.93 / **3.42** / 4.82 | 0.71 / **2.8** / 4.64 |
| US federal debt held by the public / GDP (percent) | 100 | 106 / **111** / 119 | 110 / **117** / 128 |
| USD share of allocated FX reserves (IMF COFER) (percent) | 56.5 | 47.2 / **52.1** / 57 | 42.7 / **49.6** / 56.3 |
| Gold price (USD per troy ounce) | 4040 | 3.1e+03 / **4.7e+03** / 7.26e+03 | 2.86e+03 / **5.05e+03** / 8.57e+03 |
| USD/JPY exchange rate (yen per dollar) | 163.6 | 118 / **152** / 193 | 98.5 / **146** / 202 |
| US average effective tariff rate on all imports (percent) | 6 | 2.87 / **7.88** / 17.9 | 2.17 / **8.99** / 23.1 |
| Log10 of training compute for the largest publicly-known training run (log10(FLOP)) | 26.7 | 28 / **28.8** / 29.5 | 28.8 / **29.9** / 30.9 |
| Global data center electricity consumption (TWh per year) | 590 | 832 / **1.03e+03** / 1.34e+03 | 987 / **1.26e+03** / 1.71e+03 |
| Combined annual capex, Microsoft + Alphabet + Amazon + Meta (USD billions per year) | 700 | 477 / **986** / 1.51e+03 | 442 / **1.15e+03** / 1.85e+03 |
| Nvidia annual data center revenue (USD billions per year) | 330 | 230 / **536** / 867 | 230 / **655** / 1.11e+03 |
| Combined annualized revenue run-rate, OpenAI + Anthropic (USD billions) | 72 | 163 / **349** / 627 | 244 / **509** / 873 |
| Log2 of METR 50%-reliability task time horizon (log2(hours of human-expert task time)) | 1.6 | 5.41 / **8.05** / 10.8 | 7.91 / **11.7** / 15.3 |
| Log10 of API price for GPT-4-class capability (log10(USD per million input tokens)) | -0.4 | -2.2 / **-1.8** / -1.4 | -3.12 / **-2.58** / -2.02 |
| Chinese open-weight models' share of OpenRouter tokens (percent) | 61 | 32 / **59.7** / 82.7 | 20.8 / **59.1** / 90.8 |
| Log10 of US paid fully-driverless rides per week (millions) (log10(millions of rides per week)) | -0.3 | 0.204 / **0.91** / 1.41 | 0.568 / **1.55** / 2.24 |
| US AI adoption in production, employment-weighted (Census BTOS) (percent of employment at AI-using firms) | 32 | 44.9 / **56** / 68 | 54.2 / **69.1** / 85.8 |
| Global total fertility rate (births per woman) | 2.23 | 2.03 / **2.12** / 2.21 | 1.93 / **2.06** / 2.18 |
| China annual births (million births per year) | 7.92 | 4.61 / **5.92** / 7.39 | 3.01 / **4.83** / 6.86 |
| US total fertility rate (births per woman) | 1.585 | 1.44 / **1.51** / 1.59 | 1.37 / **1.47** / 1.58 |
| Global forcibly displaced persons (million people) | 117.8 | 103 / **120** / 140 | 97.2 / **121** / 149 |
| US net international migration (thousand persons per year) | 320 | -160 / **613** / 1.4e+03 | -306 / **765** / 1.84e+03 |
| EU+ annual asylum applications (thousand applications per year) | 822 | 318 / **697** / 1.36e+03 | 119 / **633** / 1.51e+03 |
| India total fertility rate (births per woman) | 1.9 | 1.62 / **1.73** / 1.83 | 1.49 / **1.64** / 1.77 |
| World population (billion people) | 8.3 | 8.57 / **8.63** / 8.69 | 8.73 / **8.81** / 8.89 |
| China population aged 60 and over (percent of total population) | 22.9 | 27.1 / **28** / 28.8 | 29.6 / **30.8** / 31.9 |
| US annual drug overdose deaths (thousand deaths per year) | 70 | 33.8 / **55.3** / 80 | 17.9 / **47.7** / 81.6 |
| South Korea total fertility rate (births per woman) | 0.8 | 0.739 / **0.871** / 1 | 0.724 / **0.907** / 1.09 |
| Japan annual births (Japanese nationals) (thousand births per year) | 670 | 464 / **538** / 609 | 361 / **466** / 561 |
| Brent crude oil price (USD/bbl (nominal)) | 73 | 41.4 / **72.8** / 129 | 29.8 / **70.9** / 149 |
| Annual global solar PV capacity additions (GWdc/yr) | 650 | 644 / **883** / 1.17e+03 | 674 / **1.01e+03** / 1.42e+03 |
| Lithium-ion battery pack price (volume-weighted, all segments) (USD/kWh (nominal)) | 105 | 55.1 / **72.2** / 95 | 30.1 / **53.6** / 86.6 |
| China share of global rare-earth separation and refining (% of global refined output) | 87 | 71.9 / **79** / 87 | 65.1 / **74.7** / 86.1 |
| US data center electricity consumption (TWh/yr) | 225 | 313 / **463** / 688 | 392 / **594** / 891 |
| EU average wholesale electricity price (EUR/MWh (nominal)) | 80 | 40.3 / **65.8** / 118 | 23 / **60.2** / 128 |
| Global coal demand (Mt/yr) | 8800 | 7.71e+03 / **8.47e+03** / 9.03e+03 | 7.23e+03 / **8.29e+03** / 9.08e+03 |
| Uranium spot price (USD/lb U3O8) | 88 | 54.7 / **107** / 185 | 45.3 / **115** / 223 |
| Global oil (liquids) demand (million b/d) | 104.5 | 102 / **106** / 109 | 102 / **107** / 112 |
| Global LNG liquefaction nameplate capacity (Mtpa) | 510 | 656 / **712** / 755 | 743 / **823** / 881 |
| Global EV share of new light-vehicle sales (% of new sales) | 22.4 | 32.1 / **40.1** / 48.1 | 38.7 / **49.9** / 60.9 |
| Henry Hub natural gas price (USD/MMBtu (nominal)) | 3.7 | 2.46 / **4.15** / 6.99 | 2.09 / **4.44** / 8.18 |
| Cumulative confirmed H5N1-infected US dairy herds (herds) | 1166 | 1.29e+03 / **1.84e+03** / 2.6e+03 | 1.48e+03 / **2.21e+03** / 3.28e+03 |
| Confirmed human H5 (any NA) influenza cases reported globally per year (cases/year) | 14 | 2.82 / **16.7** / 64.9 | -0.522 / **18.2** / 85.1 |
| US confirmed measles cases per calendar year (cases/year) | 2900 | 1.02e+03 / **3.88e+03** / 9.05e+03 | 379 / **4.41e+03** / 1.15e+04 |
| US kindergarten MMR vaccination coverage (% of kindergartners) | 92.5 | 89.1 / **90.6** / 92.2 | 87.4 / **89.6** / 91.8 |
| Global DTP3 immunization coverage (% of surviving infants) | 85 | 81.8 / **83.9** / 86 | 80.4 / **83.3** / 86.1 |
| Deaths directly attributable to bacterial AMR (million deaths/year) | 1.2 | 1.16 / **1.31** / 1.45 | 1.17 / **1.37** / 1.58 |
| International financing for HIV in low- and middle-income countries (US$ billions/year) | 7.3 | 3.17 / **5.36** / 7.84 | 1.35 / **4.33** / 7.69 |
| US adults currently using GLP-1 drugs for weight loss (% of adults) | 12.4 | 16.1 / **23.2** / 31 | 19.3 / **28.6** / 39.5 |
| US adult obesity prevalence (Gallup self-reported) (% of adults) | 36.4 | 31.5 / **33.4** / 35.3 | 29.1 / **31.7** / 34.2 |
| WHO approved base programme budget per biennium (US$ billions/biennium) | 4.2 | 3.42 / **4.12** / 5.11 | 3.07 / **4.02** / 5.41 |
| Global malaria deaths (thousand deaths/year) | 610 | 562 / **635** / 713 | 542 / **646** / 763 |
| CDC full-time federal workforce (thousand FTEs) | 9 | 6.61 / **8.19** / 9.89 | 5.54 / **7.81** / 10.1 |
| US presidential net approval (approve minus disapprove, aggregate) (percentage points) | -19 | -28.4 / **-10.4** / 5.81 | -31.9 / **-5.56** / 17 |
| Number of countries coded as currently autocratizing by V-Dem (countries) | 44 | 37.2 / **45.1** / 53.9 | 34.1 / **45.4** / 57.9 |
| Countries with net decline in Freedom House score in a given year (countries) | 54 | 40.3 / **51.2** / 63.1 | 34.1 / **49.4** / 65.9 |
| Share of world population living in Freedom House 'Free' countries (percent) | 21 | 14.9 / **19.8** / 23.9 | 12.5 / **19.4** / 24.8 |
| AfD federal voting intention (percent) | 27 | 19.1 / **27.8** / 36.1 | 16.1 / **28.6** / 39.4 |
| French RN first-round national vote share (presidential/legislative) (percent) | 35 | 28 / **35.9** / 43.8 | 25.3 / **36.6** / 47.3 |
| Reform UK voting intention (percent) | 26 | 13.8 / **23.9** / 35 | 9.12 / **22.8** / 37.9 |
| Successful coups d'etat worldwide per calendar year (coups) | 2 | -0.0355 / **1.96** / 4.94 | -0.773 / **1.97** / 6.17 |
| US terrorism and targeted-violence events per year (START/BDI coding) (events) | 1050 | 721 / **1.24e+03** / 1.81e+03 | 633 / **1.32e+03** / 2.09e+03 |
| Gallup average 'great deal / quite a lot' confidence across nine US institutions (percent) | 27 | 21 / **26** / 30.9 | 18.5 / **25.5** / 32.3 |
| ACLED-recorded political violence events worldwide per year (events) | 1.85e+05 | 1.5e+05 / **1.97e+05** / 2.47e+05 | 1.39e+05 / **2.03e+05** / 2.73e+05 |
| FAO Food Price Index (nominal) (index, 2014-2016=100) | 130.3 | 112 / **147** / 197 | 109 / **156** / 226 |
| World cereal stocks-to-use ratio (percent) | 32 | 27.8 / **31.2** / 34.7 | 26.1 / **30.8** / 35.5 |
| World cereal production (million tonnes per calendar year) | 2983 | 2.95e+03 / **3.12e+03** / 3.3e+03 | 2.97e+03 / **3.2e+03** / 3.43e+03 |
| Urea price (Middle East granular, f.o.b.) (USD per tonne) | 520 | 235 / **444** / 852 | 105 / **409** / 962 |
| People in acute food insecurity (IPC/CH Phase 3+, GRFC) (million people) | 266 | 225 / **289** / 356 | 214 / **303** / 389 |
| People in IPC/CH Phase 5 (Catastrophe) (million people) | 1.4 | 0.357 / **1.58** / 3.49 | -0.0203 / **1.73** / 4.31 |
| CBOT front-month wheat price (USD per bushel) | 6.9 | 5.15 / **7.77** / 12.2 | 4.45 / **8.13** / 14.3 |
| Thai white rice 5% broken, f.o.b. (USD per tonne) | 365 | 244 / **403** / 664 | 211 / **440** / 784 |
| Lake Mead elevation (feet above mean sea level) | 1053 | 992 / **1.03e+03** / 1.07e+03 | 964 / **1.02e+03** / 1.07e+03 |
| WFP annual contributions received (USD billion, nominal) | 6.5 | 3.33 / **5.55** / 7.78 | 1.95 / **4.95** / 8.17 |
| Global undernourishment headcount (PoU) (million people) | 645 | 530 / **601** / 675 | 481 / **580** / 679 |
| Share of marine fish stocks within biologically sustainable levels (percent) | 62.4 | 57.4 / **60** / 62.4 | 55.2 / **58.7** / 62 |

## What drives the outcome

Share of the variance in peak systemic stress attributable to each event firing at all. High-scoring nodes are the ones worth watching, because learning how they resolve collapses the most uncertainty about everything else.

*Read with one caveat:* the stress index is built from these same events, so part of any node's score is its own contribution rather than its influence on others. The ranking is still informative — it combines probability, impact rating and correlation with the rest of the system in one number — but it is not a pure causal-influence measure, and a node cannot score high here without being either likely or heavy.

| Event | Variance share | P(by 2036) | Impact |
|---|---:|---:|---:|
| Failure or extraordinary rescue of a bank with over $250bn in assets | 1.2% | 39% | 8 |
| PISA 2025 shows no recovery in OECD-average mathematics | 1.2% | 59% | 6 |
| Strait of Hormuz closed again for 14+ consecutive days | 1.1% | 40% | 8 |
| Overt US military strike inside Mexican territory without Mexican consent | 1.1% | 48% | 7 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 1.0% | 39% | 8 |
| China's extraterritorial rare-earth export control regime enters into force | 0.9% | 70% | 7 |
| US executive branch openly defies a final Supreme Court order | 0.9% | 21% | 9 |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 0.9% | 74% | 8 |
| US average effective tariff rate exceeds 15% | 0.8% | 53% | 5 |
| Japan 10-year government bond yield reaches 3.00% | 0.7% | 60% | 7 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 0.7% | 52% | 8 |
| US federal government de-recommends a core routine childhood vaccine and the change survives | 0.7% | 62% | 6 |
| Severe rare-earth supply cutoff to the US or EU | 0.6% | 32% | 8 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 0.6% | 38% | 8 |
| Brent monthly average above $120/bbl | 0.5% | 41% | 6 |
| Civil war onset in a country of 50 million or more that was at peace in mid-2026 | 0.5% | 88% | 8 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 0.5% | 31% | 7 |
| Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases | 0.5% | 55% | 6 |

## Where the worldviews disagree most

The five parameterisations — raw analyst, audited, outside-view base rates, structural-break inside view, and prediction-market check — converge on most nodes. These are the ones where they don't, and they are exactly the forecasts you should hold most loosely.

| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |
|---|---:|---:|---:|---:|---:|---:|
| Cyberattack causes a major OECD power outage | 37% | 40% | 38% | 42% | 39% | 5pp |
| Coordinated physical attack causes a major OECD outage | 28% | 30% | 33% | 29% | 31% | 5pp |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 20% | 18% | 20% | 16% | 18% | 5pp |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 30% | 32% | 33% | 32% | 29% | 4pp |
| US Census Bureau officially reports negative net international migration | 42% | 46% | 45% | 43% | 42% | 4pp |
| New US-Russia agreement capping deployed strategic nuclear warheads | 44% | 43% | 40% | 42% | 42% | 4pp |
| Three or more countries/territories in confirmed IPC Famine simultaneously | 35% | 34% | 36% | 34% | 38% | 4pp |
| Xi Jinping ceases to be CCP General Secretary | 33% | 35% | 34% | 36% | 33% | 4pp |
| Global oil demand declines year-on-year outside recession or supply shock | 67% | 66% | 69% | 70% | 66% | 3pp |
| The Islamic Republic ceases to govern Iran | 36% | 36% | 38% | 35% | 35% | 3pp |
| Single US political-violence attack killing ten or more people | 75% | 75% | 73% | 74% | 77% | 3pp |
| Brent crude settles above $120/bbl | 60% | 58% | 61% | 60% | 61% | 3pp |
| Global mean methane annual growth rate falls to zero or below | 27% | 27% | 27% | 30% | 29% | 3pp |
| Lethal armed clash between Chinese and Japanese state forces | 14% | 16% | 15% | 14% | 17% | 3pp |
| Severe rare-earth supply cutoff to the US or EU | 29% | 32% | 31% | 30% | 31% | 3pp |
| Armed confrontation between US state-controlled forces and federal forces | 17% | 18% | 19% | 16% | 16% | 3pp |

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
| `2026-09` | geopolitics | **18th BRICS Summit, New Delhi (India presidency)** | Tests whether de-dollarization moves from rhetoric to plumbing (BRICS Pay, gold-linked Unit, CBDC interoperability) or is again shelved by India. |
| `2026-09` | climate | **Arctic sea ice September minimum 2026** | First minimum under a developing super El Nino and after a record-tying winter maximum; a sub-4.0 million km2 reading would be the first since 2012 and would shift ice-free-Arctic timelines. |
| `2026-09` | economy | **September FOMC with Summary of Economic Projections** | First full dot plot under Warsh. Market currently prices hikes toward ~4% by year-end — the SEP either validates a hiking cycle or breaks it. |
| `2026-09` | politics | **German Land elections: Saxony-Anhalt, Mecklenburg-Vorpommern, Berlin** | AfD is favoured or near-first in both eastern states; a first-place finish with no available coalition partner is the most likely trigger for a formal crisis over the CDU 'firewall'. |
| `2026-09` | politics | **Russian State Duma election** | Managed election, but seat allocation and any United Russia weakness are the main public signal about elite cohesion and post-Putin positioning. |
| `2026-09-08` | demographics | **PISA 2025 initial results release (OECD)** | First global measure of whether post-COVID learning loss has been recovered; 90+ countries, science as focal domain plus a new digital-learning domain. |
| `2026-09-13` | politics | **Swedish general election** | Tests whether Sweden Democrats convert confidence-and-supply into cabinet seats - a bellwether for Nordic normalization of the radical right. |
| `2026-09-14` | health | **IGWG8 negotiations on PABS annex to the WHO Pandemic Agreement** | The Pandemic Agreement cannot open for signature or ratification until the PABS annex is adopted; failure here freezes the entire post-COVID legal architecture for another year. |
| `2026-09-30` | demographics | **India Census 2027 Phase I houselisting operations** | Completion of the housing census; first hard national count since 2011 and the gateway to caste enumeration and parliamentary delimitation. |
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
| `2026-11-09` | climate | **COP31, Antalya, Turkey (Turkey host, Australia presiding over negotiations)** | First COP after US Paris withdrawal took effect; NDC 3.0 synthesis exposes the remaining emissions gap; first COP to reckon with the ICJ advisory opinion's legal implications. |
| `2026-11-09` | energy | **COP31, Antalya, Turkey** | First COP assessing the full set of 2035 NDCs. Turkish presidency is pushing a '35 by 35' global electrification target (electricity to 35% of final energy from ~20%), which if adopted becomes a reference point for grid and power-sector investment. |
| `2026-11-10` | energy | **Expiry of China's 12-month suspension of expanded rare-earth export controls** | The single most consequential scheduled date in critical materials. Default absent action is snap-back of the October 2025 extraterritorial 0.1% de minimis regime, which would hit autos, defence, wind and robotics supply chains globally. |

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

---

*Generated by the `worldsim` Monte Carlo engine. Parameters, dependency structure, and red-team corrections are in `params/`; rerun with `python run_simulation.py`.*
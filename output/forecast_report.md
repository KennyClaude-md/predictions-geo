# World Futures Simulation — Forecast Report

**Simulation date:** 2026-07-29  
**Horizon:** 2026Q3 → 2036Q4 (42 quarters)  
**Paths:** 4,800 across 5 worldviews × 40 parameter worlds  
**Risk nodes:** 218 · **causal edges:** 89 · **latent factors:** 6 · **continuous variables:** 104

---

## How to read this

Every number below is the output of a survival-process Monte Carlo, not a guess written directly. Nine domains were parameterised against current sources, audited for base-rate discipline, then red-teamed from three directions. Each of those opinions is run as a separate worldview and the results are pooled by weight.

**The bracketed range is not the range of outcomes** — the event either happens or it doesn't. It is the range of *the probability itself* across parameter worlds: how much the answer moves depending on whose model of the world you accept. A wide bracket means the forecast is fragile. Monte Carlo noise has been subtracted out, so what remains is real disagreement.

**Calibration check:** simulated marginals reproduce the elicited cumulative probabilities to within 6.20 percentage points (worst node, worst worldview). This matters: the dependency network is tuned to reshape the *joint* distribution — which events co-occur — without inflating any individual probability above what the underlying analysis actually claimed.

## Headline forecasts

Ranked by expected systemic impact — probability by 2036 multiplied by severity — rather than by probability alone, because a 12% chance of something that reorders the world outranks a near-certainty that doesn't.

| # | Event | by 2027 | by 2031 | by 2036 | 90% band (2036) | Impact |
|---|-------|--------:|--------:|--------:|:---------------:|----:|
| 1 | **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** | 73% | 82% | 86% | [62%–98%] | 8 |
| 2 | **Civil war onset in a country of 50 million or more that was at peace in mid-2026** | 28% | 65% | 82% | [58%–98%] | 8 |
| 3 | **Frontier agent reaches a 1-work-month 50%-reliability task horizon** | 7.3% | 63% | 73% | [42%–97%] | 9 |
| 4 | **Japan 10-year government bond yield reaches 3.00%** | 52% | 71% | 91% | [44%–99%] | 7 |
| 5 | **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** | 87% | 93% | 99% | [96%–99%] | 6 |
| 6 | **China's extraterritorial rare-earth export control regime enters into force** | 46% | 77% | 84% | [58%–98%] | 7 |
| 7 | **China annual births fall below 7.0 million** | 44% | 94% | 96% | [88%–99%] | 6 |
| 8 | **Renewed major US and/or Israeli air campaign against Iran** | 19% | 56% | 79% | [45%–99%] | 7 |
| 9 | **A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test** | 17% | 46% | 67% | [26%–98%] | 8 |
| 10 | **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** | 19% | 57% | 77% | [55%–96%] | 7 |
| 11 | **Nvidia suffers a ≥50% peak-to-trough drawdown** | 26% | 64% | 85% | [59%–98%] | 6 |
| 12 | **US recession with NBER-dated peak in the window** | 27% | 60% | 84% | [64%–98%] | 6 |
| 13 | **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** | 15% | 45% | 63% | [38%–85%] | 8 |
| 14 | **US unemployment rate ≥6.0% for three consecutive months** | 14% | 58% | 83% | [65%–97%] | 6 |
| 15 | **A single training run of ≥1e28 FLOP is publicly reported** | 7.5% | 69% | 82% | [56%–97%] | 6 |
| 16 | **China's officially reported population falls below 1.400 billion** | 58% | 97% | 99% | [94%–99%] | 5 |
| 17 | **PEPFAR terminated, absorbed, or cut by more than half from its FY2024 level** | 15% | 46% | 70% | [30%–98%] | 7 |
| 18 | **A top-4 US hyperscaler guides annual capex down year-over-year** | 20% | 76% | 82% | [54%–98%] | 6 |
| 19 | **China reports annual real GDP growth below 4.0%** | 19% | 64% | 81% | [61%–97%] | 6 |
| 20 | **New IPC/CH Famine (Phase 5) classification anywhere** | 69% | 94% | 97% | [92%–99%] | 5 |
| 21 | **Multiple US states abolish or gut school-entry vaccine mandates** | 16% | 55% | 81% | [38%–99%] | 6 |
| 22 | **Disintegration of the Thwaites Eastern Ice Shelf** | 13% | 39% | 60% | [21%–97%] | 8 |

## The decade in aggregate

Individual probabilities are the easy part. The question that actually determines how the 2030s feel is how many high-impact events land, and whether they land together.

**Read the impact rating carefully.** Analysts were asked for *global systemic impact if it occurs*, where 10 is civilization-altering — that is a measure of magnitude, not of badness. A transformative AI capability milestone legitimately scores 9 on it. These are high-impact events, not a count of catastrophes.

| Impact tier | Nodes | Expected count | Median | P(none) | P(≥2) | P(≥3) |
|---|---:|---:|---:|---:|---:|---:|
| **6+ / 10** | 110 | 50.6 | 51 | <0.5% | >99% | >99% |
| **7+ / 10** | 71 | 26.4 | 26 | <0.5% | >99% | >99% |
| **8+ / 10** | 41 | 11.9 | 12 | <0.5% | >99% | >99% |
| **9+ / 10** | 14 | 2.6 | 2 | 4.0% | 77% | 49% |

The 6+ band is broad — it contains a US recession alongside a Taiwan contingency — so the headline that the median decade fires 51 of its 110 nodes says less about danger than it first appears. The discriminating number is the tier above: across 14 nodes rated 9 or 10 for global impact, the model expects 2.6 of them this decade, puts 96% on at least one and 77% on two or more. That is the finding: a decade with no order-changing event is a minority outcome, and the interesting variance is not *whether* they arrive but whether they arrive spaced out or together.

**A caveat on cross-domain comparison.** Each domain was rated by a different analyst against the same nominal 0–10 scale, and they did not use it identically: *geopolitics* averages 7.7 while *foodwater* averages 5.5 (overall 6.4). Some of that gap is real — great-power conflict genuinely carries more systemic weight than a macro data print — but some of it is rater drift, and it means the impact ranking tilts toward whichever domain scored most generously. Compare probabilities across domains freely; compare severities within a domain.

## Scenario archetypes

Paths were clustered on which major events fired and on the shape of the systemic-stress trajectory. These are not scenarios written in advance and then assigned probabilities — they are the shapes the simulation actually produced, priced by how much of the path mass fell into each.

### Severe decade — technological discontinuity — **39%**

Concurrent failure across domains. Shocks arrive faster than systems absorb them, and the response to one degrades the capacity to answer the next. The distinguishing driver is technological discontinuity. Typical peak stress sits at the 76th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **A top-4 US hyperscaler guides annual capex down year-over-year** — 97% here vs 82% overall
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — 97% here vs 85% overall

### Manageable decade — technological discontinuity — **37%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is technological discontinuity. Typical peak stress sits at the 29th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **A top-4 US hyperscaler guides annual capex down year-over-year** — 98% here vs 82% overall
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — 97% here vs 85% overall
- Frontier agent reaches a 1-work-month 50%-reliability task horizon — *suppressed*: 57% here vs 73% overall
- AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption — *suppressed*: 62% here vs 77% overall
- US unemployment rate ≥6.0% for three consecutive months — *suppressed*: 72% here vs 83% overall

### Manageable decade — technological discontinuity (variant) — **20%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is technological discontinuity. Typical peak stress sits at the 39th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — 86% here vs 73% overall
- A top-4 US hyperscaler guides annual capex down year-over-year — *suppressed*: 22% here vs 82% overall
- Nvidia suffers a ≥50% peak-to-trough drawdown — *suppressed*: 37% here vs 85% overall
- US recession with NBER-dated peak in the window — *suppressed*: 72% here vs 84% overall

### Manageable decade — no dominant driver — **3.5%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. Typical peak stress sits at the 44th percentile of all simulated paths.

### Manageable decade — financial and macro stress — **1.5%**

Serious but sequential. Shocks land, institutions bend, and each one is substantially resolved before the next arrives. The distinguishing driver is financial and macro stress. Typical peak stress sits at the 29th percentile of all simulated paths.

Distinguishing features (rate within this cluster vs. overall):

- **China reports annual real GDP growth below 4.0%** — 91% here vs 81% overall
- A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem — *suppressed*: 49% here vs 63% overall
- AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption — *suppressed*: 64% here vs 77% overall

## Full results by domain

### Great-power conflict & geopolitics

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 73% | 82% | 86% | [62%–98%] | 8 | 2027Q1 |
| Durable Russia-Ukraine ceasefire (>=180 consecutive days) | 33% | 74% | 91% | [78%–98%] | 7 | 2028Q4 |
| Renewed major US and/or Israeli air campaign against Iran | 19% | 56% | 79% | [45%–99%] | 7 | 2029Q4 |
| A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test | 17% | 46% | 67% | [26%–98%] | 8 | 2029Q4 |
| A second US kinetic operation to remove or kill a sitting foreign head of state or government | 14% | 40% | 62% | [29%–97%] | 7 | 2030Q3 |
| PRC forces cause the death of a Philippine serviceman or coast guardsman | 12% | 40% | 62% | [25%–97%] | 7 | 2030Q2 |
| Vladimir Putin ceases to hold effective power in Russia | 11% | 34% | 53% | [18%–90%] | 8 | 2030Q3 |
| Iran formally withdraws from the Nuclear Non-Proliferation Treaty | 16% | 45% | 67% | [26%–98%] | 6 | 2029Q4 |
| New US-Russia agreement capping deployed strategic nuclear warheads | 19% | 39% | 53% | [14%–90%] | 6 | 2029Q3 |
| Lethal DPRK-ROK military exchange | 12% | 34% | 52% | [15%–90%] | 6 | 2030Q2 |
| A state that does not now possess nuclear weapons tests a device or is confirmed to possess one | 5.6% | 18% | 33% | [9.8%–65%] | 8 | 2031Q2 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 5.2% | 19% | 28% | [12%–49%] | 9 | 2030Q3 |
| The Islamic Republic ceases to govern Iran | 8.9% | 23% | 31% | [7.3%–74%] | 8 | 2029Q3 |
| North Korea conducts a seventh nuclear explosive test | 11% | 32% | 45% | [23%–71%] | 5 | 2030Q1 |
| India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months | 5.9% | 18% | 27% | [11%–46%] | 8 | 2030Q3 |
| Iran tests or is confirmed to possess an assembled nuclear weapon | 2.5% | 10% | 20% | [3.3%–43%] | 8 | 2031Q3 |
| Lethal armed clash between Chinese and Japanese state forces | 3.7% | 11% | 19% | [6.5%–39%] | 8 | 2031Q1 |
| PRC seizes or occupies a Taiwan-administered offshore island | 3.3% | 12% | 21% | [3.2%–42%] | 7 | 2031Q2 |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 3.3% | 11% | 20% | [2.3%–48%] | 7 | 2031Q3 |
| Direct US-PRC military exchange causing at least one fatality | 2.4% | 8.2% | 14% | [5.8%–26%] | 9 | 2031Q2 |
| A jihadist insurgent group controls a Sahelian national capital for >=7 days | 6.6% | 18% | 25% | [11%–44%] | 5 | 2030Q1 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 1.9% | 5.7% | 13% | [4.0%–25%] | 10 | 2032Q3 |
| NATO invokes Article 5 in response to a Russian attack | 2.8% | 6.3% | 9.4% | [3.5%–18%] | 10 | 2029Q3 |
| US initiates withdrawal from NATO, or any member formally invokes Article 13 | 1.9% | 4.8% | 8.3% | [3.1%–17%] | 9 | 2031Q1 |
| A nuclear weapon is detonated in an act of war or hostility anywhere in the world | 0.8% | 3.4% | 5.8% | [1.6%–15%] | 10 | 2031Q2 |
| UN Security Council permanent membership formally expanded | 0.6% | 1.2% | 3.0% | [1.6%–6.8%] | 3 | 2032Q4 |

<details><summary>Resolution criteria</summary>

- **Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026)** — Crude-plus-condensate transit through Hormuz, per EIA/Vortexa/Kpler monthly data, falls below 50% of the 2025 monthly average for at least 30 consecutive days, in an episode beginning on or after 1 August 2026.
- **Durable Russia-Ukraine ceasefire (>=180 consecutive days)** — A ceasefire covering the entire land front between Russian and Ukrainian forces holds for at least 180 consecutive days without resumption of sustained offensive ground operations or systematic long-range strikes on cities, as assessed by ISW/OSCE-successor monitoring or equivalent consensus reporting. Short holiday truces (e.g. April/May 2026) do NOT count.
- **Renewed major US and/or Israeli air campaign against Iran** — At least 100 US and/or Israeli strikes on targets inside Iran within any 30-day window beginning on or after 1 August 2026, per credible multi-source reporting or US/Israeli government statement.
- **A recognised nuclear-weapon state (US, Russia or China) conducts a nuclear explosive test** — The United States, Russia or China conducts a supercritical nuclear explosive test (yield above zero, excluding subcritical and hydrodynamic experiments), confirmed by the testing state or by CTBTO/national technical means.
- **A second US kinetic operation to remove or kill a sitting foreign head of state or government** — US forces, after 1 August 2026, conduct a military operation that captures, kills, or directly precipitates within 30 days the removal from power of the sitting head of state or government of a UN member state, excluding the January 2026 Venezuela and February 2026 Iran operations.
- **PRC forces cause the death of a Philippine serviceman or coast guardsman** — An action by PLA, PLAN, China Coast Guard or maritime-militia units (including ramming, water cannon, boarding or fire) directly causes at least one death among Philippine armed forces, coast guard or government-chartered personnel, confirmed by the Philippine government.
- **Vladimir Putin ceases to hold effective power in Russia** — Putin ceases to serve as President of the Russian Federation, or is assessed by consensus of major-power governments no longer to exercise effective control over Russian state decision-making, for any reason including death, incapacity, resignation or removal.
- **Iran formally withdraws from the Nuclear Non-Proliferation Treaty** — Iran deposits formal notice of withdrawal under NPT Article X with the depositary governments and the UN Security Council, or that withdrawal takes effect.
- **New US-Russia agreement capping deployed strategic nuclear warheads** — The US and Russia sign a bilateral agreement (treaty, executive agreement, or formal reciprocal political commitment announced by both heads of state) that establishes a numerical ceiling on deployed strategic nuclear warheads or delivery vehicles.
- **Lethal DPRK-ROK military exchange** — An exchange of fire or attack between DPRK and ROK forces causing at least five combined military or civilian deaths, confirmed by either government or by the UN Command.
- **A state that does not now possess nuclear weapons tests a device or is confirmed to possess one** — Any state other than the US, Russia, UK, France, China, India, Pakistan, Israel and North Korea either (a) conducts a nuclear explosive test, (b) officially declares possession of an assembled nuclear weapon, or (c) is assessed by the IAEA or by the US intelligence community in a public statement to possess one.
- **PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days** — PRC state organs (PLA, Coast Guard or maritime authorities) publicly declare a quarantine, inspection regime or blockade of Taiwan's ports/airspace AND enforce it by boarding, turning back or interdicting at least ten commercial vessels or aircraft, sustained for at least seven consecutive days.
- **The Islamic Republic ceases to govern Iran** — The office of Supreme Leader (Velayat-e Faqih) is abolished, vacated without a successor for more than 90 days, or a government not derived from the clerical/IRGC establishment exercises effective control of Tehran; as assessed by consensus of major-power governments.
- **North Korea conducts a seventh nuclear explosive test** — A nuclear explosive test on DPRK territory confirmed by CTBTO seismic/radionuclide detection or by US/ROK/Japanese government statement.
- **India-Pakistan fighting causing >=1,000 combined battle deaths in 12 months** — Direct state-on-state armed conflict between Indian and Pakistani forces producing at least 1,000 combined military and civilian deaths within any rolling 12-month period, per UCDP or ACLED coding.
- **Iran tests or is confirmed to possess an assembled nuclear weapon** — Iran conducts a nuclear explosive test, publicly declares possession, or is publicly assessed by the IAEA or the US intelligence community to possess at least one assembled nuclear weapon.
- **Lethal armed clash between Chinese and Japanese state forces** — An exchange of fire or deliberate ramming between PLA/CCG and JSDF/JCG units resulting in at least one death, confirmed by either government.
- **PRC seizes or occupies a Taiwan-administered offshore island** — PLA, PAP or China Coast Guard forces land on and establish administrative or military control over Pratas (Dongsha), Taiping (Itu Aba), Kinmen, Matsu or Wuqiu, maintained for at least 72 consecutive hours, confirmed by Taiwan MND or US government statement.
- **State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country** — A cyberattack publicly attributed by the victim government or by the EU/NATO to a state or state-sponsored actor causes loss of electrical supply to at least one million people for at least 24 consecutive hours in a NATO or OECD member state.
- **Direct US-PRC military exchange causing at least one fatality** — An exchange of fire (kinetic, including missile, air, naval or ground fire) between US and PLA/PAP/China Coast Guard forces resulting in at least one death on either side, acknowledged by either government or confirmed by credible multi-source reporting.
- **A jihadist insurgent group controls a Sahelian national capital for >=7 days** — JNIM, ISSP/ISWAP or a successor jihadist organisation exercises effective control of Bamako, Ouagadougou or Niamey (including the presidential palace and central districts) for at least seven consecutive days, per ACLED coding or UN/Security Council reporting.
- **PRC launches an amphibious or airborne assault on Taiwan's main island** — PLA forces conduct an opposed landing or airborne insertion on Taiwan proper (not offshore islands) involving at least 1,000 personnel, confirmed by Taiwan MND or US government statement.
- **NATO invokes Article 5 in response to a Russian attack** — The North Atlantic Council formally invokes Article 5 of the Washington Treaty citing an armed attack attributable to Russia or Belarus.
- **US initiates withdrawal from NATO, or any member formally invokes Article 13** — The US President formally notifies the depositary of intent to withdraw under Article 13 of the North Atlantic Treaty, or any other member state does so.
- **A nuclear weapon is detonated in an act of war or hostility anywhere in the world** — A nuclear explosive device is detonated with hostile intent against a state, non-state actor or territory (excluding tests, accidents and demonstration detonations over unpopulated own territory), confirmed by the detonating state or by CTBTO/national technical means.
- **UN Security Council permanent membership formally expanded** — An amendment to the UN Charter expanding the number of permanent Security Council members enters into force following ratification by two-thirds of member states including all five current permanent members.

</details>

### Political stability & governance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Civil war onset in a country of 50 million or more that was at peace in mid-2026 | 28% | 65% | 82% | [58%–98%] | 8 | 2029Q1 |
| AfD enters government at German federal or Land level | 12% | 49% | 72% | [44%–94%] | 7 | 2030Q2 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 15% | 45% | 63% | [38%–85%] | 8 | 2029Q4 |
| Single US political-violence attack killing ten or more people | 21% | 61% | 78% | [52%–97%] | 6 | 2029Q2 |
| Democrats control at least one chamber of Congress from January 2027 | 89% | 89% | 90% | [80%–96%] | 5 | 2026Q4 |
| A calendar year with three or more successful coups d'etat worldwide | 46% | 75% | 85% | [62%–98%] | 5 | 2027Q4 |
| Saudi succession from King Salman | 37% | 77% | 93% | [72%–>99%] | 4 | 2028Q3 |
| Vladimir Putin ceases to be Russia's paramount leader | 4.7% | 19% | 45% | [24%–69%] | 8 | 2032Q3 |
| National Rally (or RN-aligned candidate) wins the French presidency | 34% | 34% | 50% | [26%–76%] | 7 | 2027Q3 |
| Xi Jinping ceases to be CCP General Secretary | 4.4% | 16% | 39% | [10%–81%] | 9 | 2032Q3 |
| The Islamic Republic of Iran ceases to exist as a governing system | 13% | 27% | 36% | [12%–73%] | 9 | 2029Q2 |
| Criminal conviction of a major US opposition figure in a prosecution widely coded as politically motivated | 9.0% | 27% | 44% | [13%–83%] | 7 | 2030Q4 |
| Nigerian 2027 general election breakdown | 7.1% | 24% | 40% | [9.9%–79%] | 7 | 2031Q1 |
| Overt US military strike inside Mexican territory without Mexican consent | 26% | 35% | 39% | [16%–73%] | 7 | 2027Q3 |
| Major democratic rupture or mass communal violence in India | 4.9% | 16% | 28% | [5.7%–71%] | 8 | 2031Q1 |
| US President formally invokes the Insurrection Act over a state's objection | 23% | 33% | 37% | [16%–68%] | 6 | 2027Q3 |
| Reform UK leads a UK government | 2.7% | 26% | 37% | [13%–72%] | 6 | 2030Q2 |
| Contested certification of the 2028 US presidential election | 3.4% | 12% | 22% | [2.3%–55%] | 9 | 2031Q3 |
| US executive branch openly defies a final Supreme Court order | 9.0% | 16% | 19% | [2.3%–46%] | 9 | 2028Q2 |
| Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice | 5.5% | 14% | 20% | [11%–35%] | 7 | 2030Q1 |
| Global autocratization wave inflects | 9.9% | 32% | 52% | [16%–91%] | 2 | 2030Q3 |
| Trump formally pursues a third presidential term | 4.7% | 8.4% | 9.8% | [4.0%–19%] | 8 | 2028Q2 |
| Armed confrontation between US state-controlled forces and federal forces | 3.0% | 6.9% | 9.4% | [1.7%–32%] | 8 | 2029Q4 |
| An EU member state initiates exit from the EU | 1.8% | 6.5% | 9.1% | [3.6%–17%] | 8 | 2030Q2 |

<details><summary>Resolution criteria</summary>

- **Civil war onset in a country of 50 million or more that was at peace in mid-2026** — A country with population of at least 50 million, not experiencing an armed conflict with at least 1,000 battle-related deaths in 2025, records at least 1,000 battle-related deaths in a single calendar year in an internal armed conflict, per UCDP/PRIO coding.
- **AfD enters government at German federal or Land level** — The AfD holds at least one ministerial post in a German federal or state (Land) government, or formally signs a written toleration/confidence-and-supply agreement supporting such a government. Issue-by-issue parliamentary cooperation does not count.
- **A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem** — In any V-Dem annual Democracy Report from 2027 through 2037, a NATO or EU member state that was coded as a liberal or electoral democracy in the 2026 report is coded as an electoral autocracy or closed autocracy. Turkey's and Hungary's pre-2026 coding do not qualify.
- **Single US political-violence attack killing ten or more people** — A single attack on US soil kills at least 10 people (excluding perpetrators) and is officially determined by federal law enforcement, or coded by START/GTD, as politically, religiously, racially or ideologically motivated. Ordinary criminal and non-ideological mass shootings excluded.
- **Democrats control at least one chamber of Congress from January 2027** — Following the 3 November 2026 elections, Democrats (including caucusing independents) hold a majority of seats in the US House and/or Senate when the new Congress convenes on 3 January 2027.
- **A calendar year with three or more successful coups d'etat worldwide** — In any single calendar year from 2026 onward, at least three successful coups d'etat occur globally, where 'successful' means the coup leadership holds effective power for at least seven days, per Powell-Thyne / Cline Center coding.
- **Saudi succession from King Salman** — King Salman bin Abdulaziz (b. December 1935) ceases to be King of Saudi Arabia through death, incapacity or abdication, and a successor is proclaimed, by end-2031.
- **Vladimir Putin ceases to be Russia's paramount leader** — Putin is no longer president of Russia (or, if the office is restructured, no longer the recognized paramount decision-maker) for a continuous period exceeding 60 days, through death, incapacity, resignation, removal or coup.
- **National Rally (or RN-aligned candidate) wins the French presidency** — A candidate endorsed by, or a member of, Rassemblement National (or its formal successor) is elected President of France in the 2027 or 2032 presidential election and inaugurated.
- **Xi Jinping ceases to be CCP General Secretary** — Xi Jinping is no longer General Secretary of the Chinese Communist Party for a continuous period exceeding 60 days, for any reason.
- **The Islamic Republic of Iran ceases to exist as a governing system** — A government controls Tehran that does not derive its authority from velayat-e faqih - the office of Supreme Leader is abolished, left vacant for more than 12 months with no successor, or subordinated to a non-clerical executive - sustained for at least 90 days.
- **Criminal conviction of a major US opposition figure in a prosecution widely coded as politically motivated** — By end-2031, a sitting or former US governor, senator, House member in leadership, cabinet secretary, presidential nominee, or FBI/CIA director is convicted at trial in a federal prosecution that at least three of AP/Reuters/NYT/WSJ/WaPo characterize as politically motivated or retaliatory, or that Protect Democracy's Retaliatory Action Tracker records as such.
- **Nigerian 2027 general election breakdown** — The February 2027 Nigerian general election produces at least 500 election-related deaths within 90 days of polling per ACLED, OR the presidential result is annulled or the transfer of power prevented or delayed beyond the 29 May 2027 inauguration date, OR the military intervenes in the transfer of power.
- **Overt US military strike inside Mexican territory without Mexican consent** — The US government publicly acknowledges, or three major wire services confirm, a US military kinetic strike (manned aircraft, drone, missile or ground raid) on a target inside Mexican sovereign territory that the Mexican federal government publicly states it did not consent to.
- **Major democratic rupture or mass communal violence in India** — By end-2031, either (a) V-Dem downgrades India from electoral autocracy to closed autocracy, or (b) India records at least 1,000 deaths in communal, sectarian or state-repression political violence in a single calendar year per ACLED or UCDP coding, or (c) a national election is postponed beyond its constitutional deadline or its result is not accepted by the losing coalition.
- **US President formally invokes the Insurrection Act over a state's objection** — A presidential proclamation expressly invoking 10 U.S.C. sections 251-255 (the Insurrection Act) to deploy federal troops or federalized National Guard for domestic law enforcement inside a US state whose governor has publicly objected, confirmed by the Federal Register and major wire services.
- **Reform UK leads a UK government** — A Reform UK MP is appointed Prime Minister of the United Kingdom.
- **Contested certification of the 2028 US presidential election** — Following the 7 November 2028 election, at least one state transmits competing slates of presidential electors to Congress, OR a state fails to certify by the Electoral Count Reform Act's safe-harbour deadline and the dispute reaches Congress or the Supreme Court, OR the joint session on 6 January 2029 sustains an objection to a state's electors.
- **US executive branch openly defies a final Supreme Court order** — The executive branch publicly and knowingly fails to comply with a final, non-stayed order of the US Supreme Court for more than 30 days, and this non-compliance is (a) asserted in a filing or opinion by the Court or a lower court on remand, or (b) reported as such by at least three of AP/Reuters/NYT/WSJ/WaPo. Slow-walking with a colorable legal argument does not count.
- **Successful assassination of a sitting US President, VP, member of Congress, cabinet secretary or Supreme Court justice** — A sitting US president, vice president, member of the House or Senate, Senate-confirmed cabinet secretary, or Supreme Court justice is killed in an attack determined by federal law enforcement to be politically, ideologically or personally-grievance motivated. Natural death, accident and ordinary criminal robbery excluded.
- **Global autocratization wave inflects** — In any V-Dem Democracy Report from 2028 through 2032, either the count of countries coded as currently autocratizing falls below 35, OR the number of democratizing countries exceeds the number autocratizing; alternatively, any Freedom in the World edition through 2032 records more countries improving than declining.
- **Trump formally pursues a third presidential term** — Donald Trump files FEC paperwork as a candidate for president in 2028, is placed on a primary ballot in any state as a presidential candidate, or is formally nominated as the Republican presidential or vice-presidential candidate for 2028.
- **Armed confrontation between US state-controlled forces and federal forces** — A US governor issues an order directing state law enforcement or state-controlled National Guard to physically block or detain federal agents/troops, AND an armed confrontation occurs producing at least one death or at least one state officer detaining a federal officer (or vice versa) at gunpoint. Litigation, non-cooperation policies and protest-line scuffles do not count.
- **An EU member state initiates exit from the EU** — An EU member state's government formally notifies the European Council under Article 50 TEU, or a nationally binding referendum on EU membership is held in a member state.

</details>

### AI, compute & transformative technology

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | 7.3% | 63% | 73% | [42%–97%] | 9 | 2029Q3 |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 19% | 57% | 77% | [55%–96%] | 7 | 2029Q4 |
| Nvidia suffers a ≥50% peak-to-trough drawdown | 26% | 64% | 85% | [59%–98%] | 6 | 2029Q3 |
| US unemployment rate ≥6.0% for three consecutive months | 14% | 58% | 83% | [65%–97%] | 6 | 2030Q1 |
| A single training run of ≥1e28 FLOP is publicly reported | 7.5% | 69% | 82% | [56%–97%] | 6 | 2029Q2 |
| A top-4 US hyperscaler guides annual capex down year-over-year | 20% | 76% | 82% | [54%–98%] | 6 | 2028Q4 |
| Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt | 16% | 45% | 67% | [28%–98%] | 7 | 2030Q1 |
| A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 23% | 63% | 85% | [68%–97%] | 5 | 2029Q4 |
| A top-5 Western frontier lab exits frontier training | 11% | 46% | 69% | [38%–90%] | 6 | 2030Q3 |
| China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab | 4.2% | 29% | 58% | [16%–98%] | 7 | 2032Q1 |
| A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month | 19% | 55% | 69% | [42%–90%] | 5 | 2029Q2 |
| Frontier capability plateau: 24 months with no material aggregate benchmark advance | 7.3% | 25% | 42% | [11%–82%] | 8 | 2030Q4 |
| US driverless robotaxi services exceed 5 million paid rides per week | 6.3% | 67% | 79% | [58%–97%] | 4 | 2029Q3 |
| US licenses its current-flagship datacenter GPU for general commercial sale to China | 13% | 40% | 51% | [13%–88%] | 6 | 2029Q3 |
| Court judgment or settlement >=$5B against a frontier lab over training data, or an injunction restricting training on copyrighted corpora | 9.3% | 28% | 50% | [16%–90%] | 6 | 2031Q2 |
| Grid emergency or load-shed event officially attributed in part to datacenter demand | 12% | 38% | 58% | [16%–98%] | 5 | 2030Q2 |
| US Congress enacts broad federal preemption of state AI laws | 11% | 34% | 53% | [27%–81%] | 5 | 2030Q2 |
| Confirmed theft or leak of frontier model weights | 5.3% | 18% | 33% | [6.1%–72%] | 8 | 2031Q2 |
| US enacts binding federal pre-deployment evaluation or licensing requirements for frontier models | 5.3% | 22% | 39% | [10%–79%] | 6 | 2031Q2 |
| A top mathematics journal publishes a paper whose central theorem was found primarily by AI | 10% | 51% | 78% | [54%–96%] | 3 | 2030Q2 |
| A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections | 12% | 37% | 50% | [27%–79%] | 4 | 2030Q1 |
| Taiwan Strait event materially disrupts advanced-node or CoWoS output | 2.0% | 8.1% | 15% | [2.1%–39%] | 10 | 2031Q3 |
| Binding US-China agreement on frontier AI compute or model thresholds | 2.0% | 8.9% | 16% | [5.3%–28%] | 4 | 2031Q2 |
| AI-assisted biological attack causing ≥10 deaths, officially confirmed | 1.0% | 3.6% | 5.9% | [1.1%–21%] | 9 | 2031Q1 |
| A quantum computer publicly factors an RSA-2048 modulus | <0.5% | 1.5% | 6.5% | [2.7%–15%] | 8 | 2033Q4 |

<details><summary>Resolution criteria</summary>

- **Frontier agent reaches a 1-work-month 50%-reliability task horizon** — METR (or a successor methodology it endorses) publishes a 50%-reliability time horizon of ≥167 hours of human-expert task time for a publicly deployed or externally evaluated frontier model.
- **AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption** — A government agency, CERT, or the victim organization publicly confirms an attack in which AI agents autonomously executed the majority of intrusion steps, AND documented direct losses exceed $1B (2026 USD) or the attack disrupted power, water, telecom, or payments service for >1 million people for >6 hours.
- **Nvidia suffers a ≥50% peak-to-trough drawdown** — Nvidia's split-adjusted closing share price falls at least 50% below its all-time closing high, at any point in the window.
- **US unemployment rate ≥6.0% for three consecutive months** — BLS headline U-3 seasonally adjusted unemployment rate is at or above 6.0% in three consecutive monthly releases.
- **A single training run of ≥1e28 FLOP is publicly reported** — Epoch AI, a lab's own technical report, or two independent credible technical analyses attribute ≥1e28 FLOP of training compute to a single model training run.
- **A top-4 US hyperscaler guides annual capex down year-over-year** — Microsoft, Alphabet, Amazon, or Meta states in an official earnings release or call that its expected full-fiscal-year capital expenditures will be LOWER than the prior fiscal year's actual capex.
- **Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt** — A company or SPV whose primary business is AI/datacenter compute defaults on, or completes a distressed exchange of, >=$5B (2026 USD) of debt or lease obligations; or a rating agency downgrades >=$5B of AI-datacenter-backed debt to below investment grade.
- **A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI** — A Fortune 500 (US) or Fortune Global 500 company announces a workforce reduction of ≥10,000 positions in a single announcement, and its official communications name AI/automation as the primary stated cause (not merely one factor among several).
- **A top-5 Western frontier lab exits frontier training** — One of OpenAI, Anthropic, Google DeepMind, xAI, or Meta Superintelligence Labs is acquired, dissolved, files for bankruptcy protection, or publicly announces it will stop pretraining frontier-scale models.
- **China demonstrates a domestically built EUV lithography tool patterning wafers in a production fab** — Credible public confirmation (company announcement, government statement, or two independent major-outlet reports) that a China-built EUV scanner is exposing wafers in a commercial production fab, not merely a lab or prototype.
- **A Chinese-developed model holds #1 on a major independent aggregate leaderboard for ≥1 month** — A model developed by a China-headquartered organization holds the top overall rank on Artificial Analysis's Intelligence Index or LMArena's overall text leaderboard continuously for at least 30 days.
- **Frontier capability plateau: 24 months with no material aggregate benchmark advance** — The top score on Artificial Analysis's Intelligence Index (or an endorsed successor composite) increases by less than 5 index points over any 24-consecutive-month period beginning after 2027-01-01.
- **US driverless robotaxi services exceed 5 million paid rides per week** — Publicly reported paid rides in fully driverless (no human safety operator in vehicle) commercial services in the US total ≥5,000,000 in a single week, summed across all operators.
- **US licenses its current-flagship datacenter GPU for general commercial sale to China** — BIS policy permits general (not narrowly case-by-case) export to Chinese commercial customers of Nvidia's then-current top-of-line datacenter accelerator, within one product generation of the US-available flagship.
- **Court judgment or settlement >=$5B against a frontier lab over training data, or an injunction restricting training on copyrighted corpora** — A US or EU court enters final judgment, or a lab announces a settlement, of >=$5B (2026 USD) arising from training-data copyright/IP claims; OR a court issues an injunction (not stayed within 90 days) barring a frontier lab from training on a major copyrighted corpus.
- **Grid emergency or load-shed event officially attributed in part to datacenter demand** — A US RTO/ISO, NERC, or a state utility commission issues an official finding that a load-shed event, EEA-2/EEA-3 emergency, or rolling blackout affecting >100,000 customers was caused in part by datacenter load growth.
- **US Congress enacts broad federal preemption of state AI laws** — A bill preempting state AI regulation across a broad category (beyond a single narrow domain like deepfakes) is signed into law by the President.
- **Confirmed theft or leak of frontier model weights** — A frontier lab, a government agency, or two independent major outlets confirm that the full weights of a model within one generation of a Western frontier release were exfiltrated by an unauthorized party or publicly leaked.
- **US enacts binding federal pre-deployment evaluation or licensing requirements for frontier models** — Federal legislation or a binding rule with statutory authority is enacted requiring pre-deployment safety evaluation, reporting, or licensing for models above a compute or capability threshold, applicable to private-sector deployment (not merely federal procurement).
- **A top mathematics journal publishes a paper whose central theorem was found primarily by AI** — A paper appears in Annals of Mathematics, JAMS, Inventiones, Acta Mathematica, or Duke Mathematical Journal in which the authors explicitly state that the principal new theorem was discovered or proved primarily by an AI system rather than by the human authors.
- **A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections** — A US state enacts into law (governor's signature or veto override) a moratorium, ban, or binding numerical cap on new datacenter grid interconnections above a stated size threshold, applying statewide.
- **Taiwan Strait event materially disrupts advanced-node or CoWoS output** — TSMC publicly suspends or reduces N3/N2 or CoWoS output for >=30 consecutive days, or advanced-node/HBM/CoWoS exports from Taiwan fall >=25% month-over-month, as a direct result of military action, blockade, quarantine, or interdiction by the PRC.
- **Binding US-China agreement on frontier AI compute or model thresholds** — The US and China both sign a treaty, executive agreement, or equivalent binding instrument containing specific, verifiable commitments on frontier AI training compute limits, model capability thresholds, or mutual inspection.
- **AI-assisted biological attack causing ≥10 deaths, officially confirmed** — A national government, WHO, or equivalent official body confirms a deliberate biological release causing ≥10 human deaths, and officially states that AI tools materially assisted the design, synthesis planning, or acquisition of the agent.
- **A quantum computer publicly factors an RSA-2048 modulus** — A verifiable public demonstration in which a quantum computer factors a 2048-bit RSA modulus, with the factorization independently confirmed and the computation not reducible to classical pre-processing or special-structure moduli.

</details>

### Global macroeconomy & finance

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Japan 10-year government bond yield reaches 3.00% | 52% | 71% | 91% | [44%–99%] | 7 | 2027Q3 |
| US recession with NBER-dated peak in the window | 27% | 60% | 84% | [64%–98%] | 6 | 2029Q3 |
| China reports annual real GDP growth below 4.0% | 19% | 64% | 81% | [61%–97%] | 6 | 2029Q2 |
| Brent crude settles above $120/bbl | 38% | 61% | 75% | [45%–94%] | 6 | 2027Q4 |
| Global recession (world real GDP growth below 2.0% in a calendar year) | 11% | 36% | 63% | [43%–81%] | 7 | 2031Q2 |
| US Treasury market dysfunction requiring emergency Fed intervention | 8.9% | 30% | 51% | [17%–91%] | 8 | 2030Q4 |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 8.0% | 41% | 57% | [18%–91%] | 7 | 2030Q1 |
| Wave of emerging-market sovereign defaults or restructurings | 31% | 61% | 78% | [55%–93%] | 5 | 2028Q4 |
| S&P 500 falls 30%+ from its all-time closing high | 14% | 45% | 64% | [42%–86%] | 6 | 2030Q2 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 9.8% | 25% | 46% | [23%–68%] | 8 | 2031Q2 |
| Disorderly yen move | 10% | 34% | 55% | [17%–91%] | 6 | 2030Q4 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 16% | 36% | 55% | [30%–79%] | 6 | 2030Q1 |
| US 10-year Treasury yield closes at or above 6.00% | 5.6% | 25% | 40% | [17%–66%] | 8 | 2030Q4 |
| Formal breach of Federal Reserve independence | 8.3% | 27% | 44% | [13%–86%] | 7 | 2030Q4 |
| Disorderly broad dollar depreciation | 9.0% | 32% | 50% | [10%–92%] | 6 | 2030Q3 |
| US dollar share of allocated FX reserves falls below 50% | 2.5% | 26% | 47% | [22%–72%] | 6 | 2031Q3 |
| US CPI inflation returns to 5.0%+ year over year | 22% | 43% | 57% | [30%–84%] | 5 | 2029Q1 |
| US average effective tariff rate exceeds 15% | 17% | 41% | 51% | [24%–80%] | 5 | 2029Q2 |
| China announces a central-government property/LGFV rescue of RMB 5trn or more | 14% | 32% | 50% | [11%–90%] | 5 | 2030Q2 |
| Systemic financial market infrastructure outage | 4.9% | 17% | 31% | [6.7%–68%] | 7 | 2031Q2 |
| Sustained effective closure of the Strait of Hormuz | 17% | 25% | 26% | [11%–44%] | 8 | 2027Q2 |
| Taiwan semiconductor supply disruption with global market resolution | 2.8% | 10% | 20% | [2.3%–46%] | 9 | 2031Q4 |
| France or Italy 10-year spread over Bunds exceeds 300bp | 4.2% | 14% | 22% | [6.9%–50%] | 7 | 2030Q4 |
| Major stablecoin failure or sustained depeg | 17% | 30% | 39% | [10%–76%] | 4 | 2028Q4 |
| US inflation undershoot / deflation scare | 5.8% | 20% | 34% | [8.8%–69%] | 4 | 2031Q1 |

<details><summary>Resolution criteria</summary>

- **Japan 10-year government bond yield reaches 3.00%** — The 10-year JGB benchmark yield closes at or above 3.00% on any day in the window.
- **US recession with NBER-dated peak in the window** — NBER Business Cycle Dating Committee assigns a business-cycle peak dated between August 2026 and the end of the stated year. Later announcement is fine; the peak date is what counts.
- **China reports annual real GDP growth below 4.0%** — China's National Bureau of Statistics reports full-year real GDP growth below 4.0% for any calendar year in the window, in the initial annual release.
- **Brent crude settles above $120/bbl** — ICE Brent front-month futures settle at or above $120.00/bbl on any trading day in the window.
- **Global recession (world real GDP growth below 2.0% in a calendar year)** — IMF WEO (October vintage of the following year) reports world real GDP growth at market or PPP weights below 2.0% for any calendar year in the window. Resolves YES on the first such year.
- **US Treasury market dysfunction requiring emergency Fed intervention** — The Federal Reserve announces unscheduled purchases of Treasury securities, a new or expanded standing repo/dealer facility, or explicit market-functioning operations (not policy QE and not routine reserve management) in response to disorderly conditions in the Treasury or repo market, at any point in the window.
- **AI capex bust: aggregate hyperscaler capex falls 20%+ year over year** — Combined calendar-year capital expenditure of Microsoft, Alphabet, Amazon, Meta and Oracle, as reported in audited annual filings, comes in at least 20% below the prior calendar year's reported total, for any year in the window.
- **Wave of emerging-market sovereign defaults or restructurings** — At least three additional sovereigns, each with more than $10bn in external public debt, default on external commercial debt or formally enter a comprehensive debt restructuring or a new IMF Extended Fund Facility of at least $3bn, between August 2026 and the end of the stated year.
- **S&P 500 falls 30%+ from its all-time closing high** — S&P 500 records a daily close at least 30% below its prior all-time closing high, at any point in the window.
- **Failure or extraordinary rescue of a bank with over $250bn in assets** — A bank holding company with more than $250bn in total assets in the US, EU, UK, Switzerland, Japan or China fails, is placed into resolution, is forced into a state-brokered merger, or receives an extraordinary government capital injection or central bank emergency liquidity facility created specifically for it.
- **Disorderly yen move** — USD/JPY closes above 180, or moves more than 15 yen in either direction within any 20 trading days, in the window.
- **Large private-credit vehicle suspends redemptions or enters wind-down** — A private credit fund, BDC or interval fund with at least $20bn NAV fully suspends redemptions (beyond pro-rating within stated quarterly limits) for at least one month, or is placed into wind-down or forced sale, in the US, UK or EU.
- **US 10-year Treasury yield closes at or above 6.00%** — The constant-maturity 10-year US Treasury yield (H.15 / Treasury daily par yield curve) closes at or above 6.00% on any day in the window.
- **Formal breach of Federal Reserve independence** — A sitting US president attempts to remove or demote a Federal Reserve governor or the chair for policy reasons, issues a directive on the policy rate that the Board acts on, or legislation altering the FOMC's control of the policy rate is enacted — any one, in the window.
- **Disorderly broad dollar depreciation** — The Fed's broad nominal trade-weighted dollar index falls 20% or more from its trailing 24-month high within any 24-month period in the window.
- **US dollar share of allocated FX reserves falls below 50%** — IMF COFER reports the US dollar share of allocated global foreign exchange reserves below 50.0% for any quarter in the window.
- **US CPI inflation returns to 5.0%+ year over year** — BLS reports headline CPI-U at or above 5.0% year over year for any single month in the window.
- **US average effective tariff rate exceeds 15%** — Penn Wharton Budget Model or Yale Budget Lab reports a US average effective tariff rate on all imports above 15.0% for at least one full month in the window.
- **China announces a central-government property/LGFV rescue of RMB 5trn or more** — China's State Council, MOF or PBOC announces a single package of central-government fiscal support, debt assumption or recapitalization directed at the property sector and/or local government financing vehicles totalling at least RMB 5 trillion, announced as one program.
- **Systemic financial market infrastructure outage** — A systemically important FMI — a major CCP, CLS, DTCC, Fedwire, TARGET2, SWIFT, or a top-three custodian — suffers an outage or compromise preventing settlement for more than 24 hours, or a central bank extends emergency liquidity explicitly because of it.
- **Sustained effective closure of the Strait of Hormuz** — Seaborne crude and condensate transits through the Strait of Hormuz fall more than 50% below the 2025 monthly average for at least 14 consecutive days, per IEA, EIA, Kpler or Vortexa reporting, at any point from August 2026 onward.
- **Taiwan semiconductor supply disruption with global market resolution** — Monthly semiconductor exports from Taiwan fall more than 40% below the trailing twelve-month average for two consecutive months, for any reason (blockade, quarantine, conflict, or major natural disaster), in the window.
- **France or Italy 10-year spread over Bunds exceeds 300bp** — The 10-year OAT-Bund or BTP-Bund spread closes above 300 basis points for five consecutive trading days, or the ECB formally activates the Transmission Protection Instrument for either sovereign.
- **Major stablecoin failure or sustained depeg** — A stablecoin with at least $20bn market capitalization trades more than 5% below its peg for more than 24 consecutive hours, or its issuer suspends or fails to honor redemptions for more than 24 hours.
- **US inflation undershoot / deflation scare** — US core PCE inflation prints below 1.0% year over year for three consecutive months, or headline CPI-U prints negative year over year for any month, in the window.

</details>

### Climate & Earth systems

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | 87% | 93% | 99% | [96%–99%] | 6 | 2027Q1 |
| Global fossil CO2 emissions confirmed to have peaked | 11% | 37% | 69% | [40%–97%] | 7 | 2031Q2 |
| Disintegration of the Thwaites Eastern Ice Shelf | 13% | 39% | 60% | [21%–97%] | 8 | 2030Q2 |
| Long-term (multi-decadal) 1.5C breach formally declared | 5.6% | 42% | 84% | [57%–98%] | 5 | 2032Q1 |
| New record-low Antarctic sea ice minimum extent | 15% | 46% | 67% | [29%–98%] | 6 | 2030Q1 |
| A calendar year at or above 1.65C above pre-industrial | 62% | 90% | 97% | [85%–99%] | 4 | 2027Q2 |
| Global insured natural catastrophe losses exceed $200bn in a calendar year | 13% | 41% | 64% | [29%–98%] | 6 | 2030Q2 |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | 70% | 74% | 74% | [54%–95%] | 5 | 2027Q1 |
| FAO Food Price Index exceeds 160 in any month | 12% | 33% | 62% | [31%–88%] | 6 | 2031Q3 |
| Combined Lake Powell + Lake Mead storage falls below 20% of capacity | 19% | 44% | 64% | [31%–89%] | 5 | 2029Q4 |
| Single heat event with >= 100,000 attributed excess deaths | 9.5% | 27% | 44% | [20%–74%] | 7 | 2030Q4 |
| A new record warmest calendar year, exceeding 2024 | 78% | 94% | 99% | [97%–99%] | 3 | 2027Q2 |
| A second G20 economy formally withdraws from the Paris Agreement | 6.7% | 22% | 36% | [9.0%–75%] | 7 | 2030Q4 |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 5.4% | 19% | 35% | [13%–64%] | 6 | 2031Q3 |
| Amazon basin becomes a net annual carbon source for three consecutive years | 1.8% | 13% | 26% | [5.8%–59%] | 8 | 2032Q1 |
| Formal international SRM governance decision adopted | 13% | 32% | 40% | [13%–77%] | 4 | 2029Q2 |
| Final court judgment ordering >= $1bn in climate damages | 1.8% | 12% | 26% | [4.9%–61%] | 6 | 2032Q2 |
| Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months | 3.6% | 10% | 19% | [1.8%–47%] | 8 | 2031Q2 |
| Global mean methane annual growth rate falls to zero or below | 1.9% | 8.5% | 18% | [2.0%–49%] | 5 | 2032Q2 |
| State-backed solar radiation management deployment announced or conducted | 0.8% | 6.2% | 11% | [1.7%–30%] | 8 | 2031Q3 |
| VEI 6+ volcanic eruption with measurable global cooling | 2.5% | 10% | 17% | [1.9%–45%] | 5 | 2031Q2 |
| AMOC declared to have crossed a tipping point | <0.5% | 1.7% | 5.4% | [1.1%–17%] | 10 | 2033Q2 |
| Arctic Ocean practically ice-free (extent below 1.0 million km2) | <0.5% | 1.9% | 8.5% | [2.2%–23%] | 5 | 2033Q3 |

<details><summary>Resolution criteria</summary>

- **Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window** — NOAA Coral Reef Watch reports that Alert Level 1 or higher bleaching-level heat stress affected at least 60% of the world's coral reef area within any rolling 12-month period.
- **Global fossil CO2 emissions confirmed to have peaked** — The Global Carbon Project reports global fossil CO2 emissions below the previous all-time high in two consecutive calendar years, with the peak year identified in the published Global Carbon Budget.
- **Disintegration of the Thwaites Eastern Ice Shelf** — Satellite observation (ESA/NASA, confirmed by NSIDC or a peer-reviewed publication) shows the Thwaites Eastern Ice Shelf has lost at least 50% of its 2020 area through fracture and calving within a three-year period.
- **Long-term (multi-decadal) 1.5C breach formally declared** — The WMO, IPCC (in AR7 or a special report), or the UNFCCC Global Stocktake formally states that the long-term global mean temperature increase - defined as a 20-year mean or current human-induced warming - has exceeded 1.5C above 1850-1900.
- **New record-low Antarctic sea ice minimum extent** — NSIDC reports an Antarctic daily minimum sea ice extent below the February 2023 record of 1.79 million km2.
- **A calendar year at or above 1.65C above pre-industrial** — ERA5 annual global mean surface temperature anomaly relative to 1850-1900 is >= 1.65C for a full calendar year, as published in the Copernicus Global Climate Highlights.
- **Global insured natural catastrophe losses exceed $200bn in a calendar year** — Swiss Re sigma or Munich Re NatCatSERVICE reports global insured losses from natural catastrophes above US$200 billion (nominal) for a single calendar year.
- **The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C)** — NOAA CPC's Oceanic Nino Index (3-month running mean Nino3.4 anomaly, ERSSTv5 with the operational base period) reaches or exceeds +2.0C for at least one overlapping season during the 2026-27 event.
- **FAO Food Price Index exceeds 160 in any month** — The FAO Food Price Index (nominal, 2014-2016 = 100) records a monthly value above 160.0, exceeding the March 2022 all-time high of 160.3.
- **Combined Lake Powell + Lake Mead storage falls below 20% of capacity** — US Bureau of Reclamation end-of-month reservoir reports show combined active storage in Lake Powell and Lake Mead below 20% of combined live capacity.
- **Single heat event with >= 100,000 attributed excess deaths** — A peer-reviewed study or national statistical office attributes at least 100,000 excess deaths to a single heat wave or heat season within one country or contiguous region over a window of 90 days or less.
- **A new record warmest calendar year, exceeding 2024** — Copernicus ERA5 (with NASA GISTEMP and NOAA as corroboration) reports a calendar year with a global mean surface temperature anomaly exceeding the 2024 value (1.60C above 1850-1900) at the annual announcement in the following January.
- **A second G20 economy formally withdraws from the Paris Agreement** — A G20 member other than the United States deposits formal notification of withdrawal from the Paris Agreement with the UN Secretary-General.
- **Verified wet-bulb temperature of 35C sustained for three or more hours** — A quality-controlled surface station observation (or a national meteorological service's official record) documents a wet-bulb temperature of at least 35.0C sustained for at least three consecutive hours, confirmed in a peer-reviewed publication or by a national met service.
- **Amazon basin becomes a net annual carbon source for three consecutive years** — Peer-reviewed literature (atmospheric inversion, aircraft profile, or eddy-covariance synthesis accepted by the Global Carbon Project) establishes that the Amazon basin as a whole was a net annual source of carbon to the atmosphere in three consecutive calendar years.
- **Formal international SRM governance decision adopted** — UNEA, the UNFCCC COP, the CBD COP, or a comparable treaty body adopts a formal decision or instrument establishing an international governance framework for solar radiation modification (whether a non-use agreement, a research governance regime, or a moratorium codification), beyond the existing non-binding CBD language.
- **Final court judgment ordering >= $1bn in climate damages** — A court of final instance (highest domestic court, or a binding international tribunal) issues a non-appealable judgment ordering a state or a company to pay at least US$1 billion in damages, compensation, or a compliance fund specifically for climate change harms.
- **Observed AMOC weakening of >= 30% below the 2004-2023 mean, sustained 12 months** — The RAPID-MOCHA-WBTS array at 26N (or a successor observing system accepted as the reference by the AMOC research community) reports a 12-month running mean overturning transport at least 30% below the 2004-2023 mean, confirmed in a peer-reviewed publication.
- **Global mean methane annual growth rate falls to zero or below** — NOAA GML reports a global mean CH4 annual increase of 0.0 ppb or less for a calendar year in its published trends series.
- **State-backed solar radiation management deployment announced or conducted** — A national government formally announces a stratospheric aerosol injection deployment programme (as distinct from research), or a state or state-backed entity conducts SAI at a scale exceeding 0.1 Tg of injected aerosol precursor per year, as confirmed by independent monitoring or official statement.
- **VEI 6+ volcanic eruption with measurable global cooling** — A volcanic eruption of VEI 6 or greater (Smithsonian GVP classification) injects sufficient stratospheric sulphate that WMO, NASA GISS or Copernicus attributes at least 0.1C of global mean cooling to it in the following one to two years.
- **AMOC declared to have crossed a tipping point** — A major assessment body (IPCC, WMO, or a National Academies-equivalent) or a strong majority of the published AMOC literature states that the AMOC has crossed a critical threshold and is on an irreversible trajectory toward collapse (maximum strength below 5 Sv) under current forcing.
- **Arctic Ocean practically ice-free (extent below 1.0 million km2)** — NSIDC daily sea ice extent for the Arctic falls below 1.0 million km2 on at least one day.

</details>

### Energy systems & critical materials

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China's extraterritorial rare-earth export control regime enters into force | 46% | 77% | 84% | [58%–98%] | 7 | 2027Q4 |
| Strait of Hormuz closed again for 14+ consecutive days | 55% | 62% | 67% | [29%–92%] | 8 | 2027Q2 |
| Qatari LNG force majeure removing 15%+ of global LNG supply for 60+ days | 20% | 58% | 80% | [40%–99%] | 6 | 2029Q3 |
| Severe rare-earth supply cutoff to the US or EU | 27% | 45% | 53% | [14%–83%] | 8 | 2027Q4 |
| Major producing state imposes an export ban or nationalisation on a critical mineral | 19% | 50% | 70% | [30%–98%] | 6 | 2029Q3 |
| Loss of Russian uranium enrichment and conversion services to Western utilities | 13% | 39% | 59% | [18%–97%] | 7 | 2030Q2 |
| Grid equipment supply chain forces cancellation or multi-year deferral of major interconnection programmes | 23% | 58% | 78% | [32%–99%] | 5 | 2029Q2 |
| Brent monthly average above $120/bbl | 36% | 53% | 64% | [30%–86%] | 6 | 2027Q4 |
| China energy-related CO2 emissions decline three consecutive years | 5.2% | 46% | 70% | [29%–98%] | 5 | 2030Q2 |
| EU ETS2 delayed, price-capped or materially diluted | 24% | 63% | 83% | [49%–99%] | 4 | 2029Q2 |
| US data-center electricity demand growth collapses | 11% | 34% | 52% | [19%–90%] | 6 | 2030Q2 |
| Global oil demand declines year-on-year outside recession or supply shock | 7.1% | 35% | 61% | [22%–95%] | 5 | 2031Q1 |
| Inverter-driven systemic grid collapse in a major OECD system | 8.6% | 30% | 50% | [13%–88%] | 6 | 2030Q4 |
| LME copper exceeds $15,000/tonne | 12% | 39% | 53% | [15%–93%] | 5 | 2029Q3 |
| A Western SMR delivers first commercial grid power | 3.8% | 64% | 88% | [68%–98%] | 3 | 2030Q1 |
| Firm load shedding in a major US RTO | 17% | 47% | 62% | [33%–87%] | 4 | 2029Q2 |
| European gas price returns to crisis levels | 30% | 40% | 46% | [18%–76%] | 5 | 2027Q3 |
| Global coal demand falls 3%+ below the 2025 level | 7.2% | 47% | 73% | [47%–94%] | 3 | 2030Q3 |
| Lithium carbonate price exceeds $40,000/tonne | 14% | 36% | 44% | [9.5%–84%] | 4 | 2029Q1 |
| Cyberattack causes a major OECD power outage | 5.5% | 17% | 29% | [8.6%–57%] | 6 | 2030Q4 |
| Brent monthly average below $45/bbl | 9.6% | 34% | 41% | [20%–69%] | 4 | 2029Q1 |
| Annual global solar PV installations exceed 1,000 GW | 5.7% | 40% | 73% | [47%–97%] | 2 | 2031Q3 |
| Coordinated physical attack causes a major OECD outage | 5.1% | 15% | 24% | [2.2%–61%] | 5 | 2030Q4 |
| Nuclear accident rated INES Level 5 or above | 6.9% | 11% | 20% | [8.1%–36%] | 6 | 2030Q3 |
| Global installed water electrolysis capacity reaches 25 GW | 1.9% | 19% | 49% | [24%–78%] | 2 | 2032Q4 |

<details><summary>Resolution criteria</summary>

- **China's extraterritorial rare-earth export control regime enters into force** — The October 2025 expanded rare-earth export control measures (extraterritorial 0.1% de minimis provisions and expanded element list) are in legal force and being applied to licence applications for at least 30 consecutive days, per MOFCOM announcements, at any point before the stated year-end.
- **Strait of Hormuz closed again for 14+ consecutive days** — Commercial tanker transits through the Strait of Hormuz fall below 25% of the 2025 daily average for 14 or more consecutive days, per Lloyd's List / Kpler / IEA Oil Market Report tracking, at any point after 1 Aug 2026.
- **Qatari LNG force majeure removing 15%+ of global LNG supply for 60+ days** — QatarEnergy declares force majeure or otherwise suspends loadings such that Qatari LNG exports fall below 40% of their 2025 monthly average for 60 or more consecutive days, per Kpler/ICIS tracking, at any point after 1 Aug 2026.
- **Severe rare-earth supply cutoff to the US or EU** — Chinese exports of NdPr oxide/metal or heavy rare earths (Dy, Tb) to either the United States or the European Union fall by more than 50% year-on-year for three or more consecutive months, per China customs data.
- **Major producing state imposes an export ban or nationalisation on a critical mineral** — A country accounting for 20% or more of global mined supply of lithium, cobalt, nickel, copper or rare earths imposes an export ban, export quota cut of 30%+, or nationalisation/forced-equity measure that removes 15% or more of global supply for 3+ months.
- **Loss of Russian uranium enrichment and conversion services to Western utilities** — Rosatom/TENEX deliveries of enrichment (SWU) or conversion services to US and EU utilities fall by more than 70% year-on-year for four or more consecutive quarters, whether by sanction, counter-sanction or contract termination, per Euratom Supply Agency and US DOE/EIA reporting.
- **Grid equipment supply chain forces cancellation or multi-year deferral of major interconnection programmes** — A G7 transmission system operator or major US RTO publicly defers or cancels 10 GW or more of already-approved interconnection or transmission capacity, citing large power transformer, HVDC converter or gas turbine unavailability as the stated primary cause.
- **Brent monthly average above $120/bbl** — The calendar-month average of front-month Brent futures settlements exceeds $120.00/bbl (nominal USD) in any month after 1 Aug 2026, per ICE settlement data.
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
- **Coordinated physical attack causes a major OECD outage** — A deliberate physical attack (sabotage, arson, gunfire, explosive) causes loss of electricity supply to 500,000 or more customers for 24 or more hours in an OECD member country, confirmed as deliberate by law enforcement.
- **Nuclear accident rated INES Level 5 or above** — The IAEA International Nuclear Event Scale assigns a rating of Level 5 (accident with wider consequences) or higher to an event at a civil nuclear power reactor or spent fuel facility anywhere in the world.
- **Global installed water electrolysis capacity reaches 25 GW** — IEA Global Hydrogen Review reports cumulative installed and operating water electrolysis capacity worldwide of 25 GW or more.

</details>

### Demography & migration

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| China annual births fall below 7.0 million | 44% | 94% | 96% | [88%–99%] | 6 | 2028Q1 |
| China's officially reported population falls below 1.400 billion | 58% | 97% | 99% | [94%–99%] | 5 | 2027Q3 |
| Next UN WPP revision moves peak world population below 10.0 billion or earlier than 2070 | 23% | 63% | 85% | [47%–99%] | 5 | 2029Q2 |
| PISA 2025 shows no recovery in OECD-average mathematics | 69% | 69% | 69% | [41%–89%] | 6 | 2026Q4 |
| Best-available global TFR estimate falls below 2.1 | 2.7% | 28% | 59% | [21%–93%] | 7 | 2032Q1 |
| India publishes provisional Census 2027 population totals | 54% | 92% | 95% | [82%–99%] | 4 | 2027Q3 |
| Japan annual births (Japanese nationals) fall below 600,000 | 39% | 93% | 95% | [80%–99%] | 4 | 2028Q1 |
| US removals plus returns exceed one million in a fiscal year | 13% | 40% | 62% | [25%–98%] | 6 | 2030Q2 |
| US total fertility rate falls below 1.50 | 4.0% | 48% | 73% | [41%–95%] | 5 | 2030Q3 |
| India enacts reapportionment of Lok Sabha seats on post-2026 census population | 9.4% | 31% | 52% | [19%–93%] | 7 | 2030Q4 |
| Two million or more Ukrainian refugees return to Ukraine | 15% | 44% | 69% | [25%–98%] | 5 | 2030Q1 |
| US life expectancy at birth reaches 80.0 years | 18% | 55% | 83% | [44%–99%] | 4 | 2029Q4 |
| Global forced displacement exceeds 130 million | 11% | 32% | 54% | [27%–74%] | 6 | 2030Q4 |
| US Census Bureau officially reports negative net international migration | 22% | 43% | 52% | [16%–91%] | 6 | 2028Q3 |
| Remittances to low- and middle-income countries fall 10% or more year-on-year | 7.9% | 27% | 47% | [12%–86%] | 6 | 2031Q1 |
| A G7 country cuts permanent immigration by three quarters | 5.0% | 28% | 35% | [8.2%–67%] | 7 | 2029Q2 |
| EU return hubs operationalized at scale | 11% | 32% | 47% | [14%–89%] | 5 | 2030Q1 |
| Youth-led protests topple three or more Sub-Saharan African governments in a three-year window | 6.5% | 32% | 47% | [16%–84%] | 5 | 2030Q2 |
| Nigeria completes a national census and the result diverges more than 10% from the prior UN estimate | 7.4% | 23% | 36% | [6.0%–87%] | 6 | 2030Q3 |
| Global life expectancy falls by 0.5 years or more in a single year | 3.9% | 14% | 27% | [5.2%–66%] | 8 | 2031Q3 |
| South Korea total fertility rate reaches 1.00 or above | 2.4% | 18% | 36% | [14%–59%] | 4 | 2031Q4 |
| Gulf Cooperation Council migrant worker stock falls 15% or more from its peak | 4.0% | 14% | 24% | [2.0%–60%] | 6 | 2031Q1 |
| China's population is revised down by 15 million or more | 2.7% | 15% | 22% | [2.6%–49%] | 6 | 2030Q3 |
| China's direct birth and childcare subsidies reach 0.5% of GDP | 3.2% | 20% | 32% | [5.8%–71%] | 4 | 2030Q4 |

<details><summary>Resolution criteria</summary>

- **China annual births fall below 7.0 million** — China's National Bureau of Statistics reports annual births below 7,000,000 for any calendar year, in its regular January statistical communique or the annual Statistical Yearbook.
- **China's officially reported population falls below 1.400 billion** — NBS reports a year-end national population (mainland, excluding HK/Macau/Taiwan) below 1,400 million.
- **Next UN WPP revision moves peak world population below 10.0 billion or earlier than 2070** — A UN DESA World Population Prospects revision published after July 2026 reports a medium-variant peak world population below 10,000,000,000, or a medium-variant peak year earlier than 2070.
- **PISA 2025 shows no recovery in OECD-average mathematics** — OECD PISA 2025 results report an OECD-average mathematics score equal to or below the PISA 2022 OECD-average mathematics score (472 points).
- **Best-available global TFR estimate falls below 2.1** — A UN DESA World Population Prospects revision (or UN Population Division estimate) reports a global total fertility rate below 2.10 for the then-current year.
- **India publishes provisional Census 2027 population totals** — The Registrar General and Census Commissioner of India publishes provisional population totals from Census 2027, covering the population enumeration phase with a reference date of 1 March 2027.
- **Japan annual births (Japanese nationals) fall below 600,000** — Japan's MHLW Vital Statistics report annual births to Japanese nationals below 600,000 for any calendar year, in preliminary or final figures.
- **US removals plus returns exceed one million in a fiscal year** — DHS Office of Homeland Security Statistics (or ICE/CBP annual reporting) reports combined removals, returns, and expulsions exceeding 1,000,000 for a single fiscal year.
- **US total fertility rate falls below 1.50** — CDC/NCHS reports a US total fertility rate below 1,500 births per 1,000 women (i.e. TFR < 1.50) for any calendar year, provisional or final.
- **India enacts reapportionment of Lok Sabha seats on post-2026 census population** — India enacts a constitutional amendment or Delimitation Act fixing revised Lok Sabha seat allocations across states based on Census 2027 (or later) population figures.
- **Two million or more Ukrainian refugees return to Ukraine** — UNHCR reports cumulative refugee returns to Ukraine of 2,000,000 or more since the reporting baseline, or reports the Ukrainian refugee population in Europe falling by 2,000,000 or more from its peak.
- **US life expectancy at birth reaches 80.0 years** — NCHS reports US period life expectancy at birth of 80.0 years or more for a single calendar year, in final or provisional mortality reports.
- **Global forced displacement exceeds 130 million** — UNHCR Global Trends (or Mid-Year Trends) reports total forcibly displaced persons exceeding 130,000,000 at any reporting date.
- **US Census Bureau officially reports negative net international migration** — A Census Bureau Vintage population estimates release (or an official Census Bureau revision) reports negative net international migration for any 12-month estimating period.
- **Remittances to low- and middle-income countries fall 10% or more year-on-year** — World Bank / KNOMAD reports nominal USD remittance flows to low- and middle-income countries declining 10% or more versus the prior year.
- **A G7 country cuts permanent immigration by three quarters** — A G7 member's official annual permanent-residence/settlement admissions (e.g. US lawful permanent residents, Canada PR admissions, UK settlement grants) fall below 25% of that country's 2024 level for a full fiscal or calendar year, per the responsible national agency.
- **EU return hubs operationalized at scale** — At least three EU member states have transferred a cumulative total of 1,000 or more rejected asylum applicants or asylum seekers to designated 'return hubs' or processing centres in non-EU third countries under the Returns Regulation or bilateral arrangements, as documented by the European Commission, EUAA, or a major NGO monitor.
- **Youth-led protests topple three or more Sub-Saharan African governments in a three-year window** — In any rolling 36-month window, heads of state or heads of government in three or more Sub-Saharan African countries resign, are removed, or flee within 90 days of the onset of mass protests that contemporaneous major-outlet reporting characterizes as youth-led or 'Gen Z' protests.
- **Nigeria completes a national census and the result diverges more than 10% from the prior UN estimate** — Nigeria's National Population Commission publishes national population totals from a census conducted after 2006, and the figure differs by more than 10% from the UN WPP estimate for Nigeria published immediately prior.
- **Global life expectancy falls by 0.5 years or more in a single year** — UN WPP, IHME GBD, or WHO reports global period life expectancy at birth declining by 0.5 years or more relative to the prior year.
- **South Korea total fertility rate reaches 1.00 or above** — Statistics Korea reports an annual total fertility rate of 1.00 or higher for any calendar year.
- **Gulf Cooperation Council migrant worker stock falls 15% or more from its peak** — UN DESA International Migrant Stock estimates, or combined national labour-force statistics for Saudi Arabia, UAE, Qatar, Kuwait, Oman and Bahrain, show the foreign-born or non-national workforce at least 15% below its post-2020 peak.
- **China's population is revised down by 15 million or more** — An official Chinese government source (NBS communique, the 2030 national census, or a published statistical yearbook revision) reports a national population figure at least 15,000,000 below the previously published estimate for a comparable date.
- **China's direct birth and childcare subsidies reach 0.5% of GDP** — Combined central and local government direct cash transfers for childbirth and childcare in China exceed 0.5% of nominal GDP in a single fiscal year, per Ministry of Finance budget documents or credible reporting aggregating central and provincial outlays.

</details>

### Pandemics, biosecurity & global health

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| PEPFAR terminated, absorbed, or cut by more than half from its FY2024 level | 15% | 46% | 70% | [30%–98%] | 7 | 2030Q2 |
| Multiple US states abolish or gut school-entry vaccine mandates | 16% | 55% | 81% | [38%–99%] | 6 | 2029Q4 |
| US federal government de-recommends a core routine childhood vaccine and the change survives | 36% | 56% | 62% | [26%–94%] | 6 | 2027Q3 |
| Cholera resurgence with oral cholera vaccine stockpile failure | 18% | 51% | 74% | [36%–98%] | 5 | 2029Q4 |
| United States formally loses measles elimination status | 78% | 86% | 89% | [67%–98%] | 4 | 2026Q4 |
| A single US influenza season with at least 50,000 estimated deaths | 17% | 45% | 65% | [28%–98%] | 5 | 2029Q4 |
| Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin | 9.9% | 32% | 45% | [12%–80%] | 7 | 2030Q1 |
| Large autochthonous arbovirus transmission in continental Europe or the continental US | 20% | 55% | 78% | [36%–99%] | 4 | 2029Q3 |
| Two consecutive years of rising global new HIV infections | 1.8% | 42% | 50% | [14%–90%] | 6 | 2029Q4 |
| WHO declares at least one new PHEIC beyond polio and the current Ebola BDBV emergency | 55% | 93% | 99% | [93%–>99%] | 3 | 2027Q3 |
| Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases | 42% | 45% | 45% | [14%–82%] | 6 | 2027Q1 |
| WHO declares an influenza pandemic (any subtype) | 6.5% | 19% | 33% | [18%–50%] | 8 | 2031Q2 |
| PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly | 53% | 80% | 86% | [59%–99%] | 3 | 2027Q3 |
| A newly emerged pathogen causes at least 1 million cumulative deaths worldwide | 1.5% | 10% | 23% | [3.6%–46%] | 10 | 2032Q2 |
| WHO Pandemic Agreement enters into force | 1.9% | 51% | 75% | [44%–95%] | 3 | 2030Q3 |
| Paralytic poliomyelitis from circulating vaccine-derived poliovirus in a high-income country | 11% | 35% | 56% | [18%–93%] | 4 | 2030Q3 |
| US reports at least 5,000 confirmed measles cases in a single calendar year | 17% | 56% | 70% | [39%–91%] | 3 | 2029Q3 |
| Sustained human-to-human transmission of an H5 influenza virus | 2.5% | 8.9% | 20% | [9.2%–35%] | 9 | 2032Q3 |
| United States formally rejoins the World Health Organization | 1.2% | 28% | 40% | [13%–70%] | 4 | 2030Q2 |
| Global interruption of wild poliovirus type 1 transmission | 2.8% | 25% | 44% | [19%–74%] | 3 | 2031Q2 |
| Laboratory accident causes an outbreak of 50+ confirmed human cases with official lab attribution | 2.3% | 7.5% | 14% | [1.8%–39%] | 7 | 2031Q2 |
| Deliberate biological attack causes at least 10 confirmed human deaths | 2.2% | 4.8% | 8.9% | [1.7%–23%] | 8 | 2031Q2 |
| Ebola causes a confirmed secondary transmission chain outside Africa | 6.5% | 12% | 16% | [6.2%–36%] | 4 | 2028Q4 |
| WHO declares a global emergency over an antimicrobial-resistant pathogen | 0.9% | 3.5% | 7.0% | [3.0%–14%] | 5 | 2031Q4 |

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
- **Current DRC/Uganda Bundibugyo Ebola epidemic exceeds 10,000 confirmed cases** — WHO/AFRO situation reports for the outbreak declared 15 May 2026 (or its recognized continuation) record at least 10,000 cumulative laboratory-confirmed cases across all affected countries.
- **WHO declares an influenza pandemic (any subtype)** — WHO formally declares an influenza pandemic, or declares a PHEIC/pandemic emergency for a novel influenza A virus with confirmed sustained community-level human-to-human transmission in at least two WHO regions.
- **PABS annex to the WHO Pandemic Agreement adopted by a World Health Assembly** — A World Health Assembly (regular or special session) formally adopts the Pathogen Access and Benefit-Sharing annex to the WHO Pandemic Agreement.
- **A newly emerged pathogen causes at least 1 million cumulative deaths worldwide** — A pathogen not endemically circulating in humans as of 1 Jan 2026 is credibly estimated by WHO, IHME, or a peer-reviewed consensus source to have caused at least 1,000,000 cumulative human deaths (reported or excess) within the stated horizon.
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

### Food, water & agriculture

| Event | 2027 | 2031 | 2036 | 90% band (2036) | Impact | Median timing |
|---|---:|---:|---:|:---:|---:|---|
| New IPC/CH Famine (Phase 5) classification anywhere | 69% | 94% | 97% | [92%–99%] | 5 | 2027Q2 |
| FAO Food Price Index reaches an all-time high above 160 | 18% | 55% | 78% | [47%–97%] | 6 | 2030Q1 |
| Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously | 27% | 62% | 77% | [48%–97%] | 6 | 2029Q1 |
| GRFC reports more than 300 million people in acute food insecurity | 18% | 71% | 85% | [60%–98%] | 5 | 2029Q2 |
| New World screwworm or FMD establishes in the US or EU cattle herd | 14% | 43% | 70% | [30%–98%] | 5 | 2030Q3 |
| Thai 5% broken rice benchmark exceeds US$650/tonne | 8.4% | 26% | 49% | [21%–80%] | 7 | 2031Q3 |
| WFP annual contributions fall below US$5 billion | 37% | 59% | 68% | [44%–87%] | 5 | 2027Q4 |
| World Bank monthly urea price exceeds US$800/tonne | 29% | 48% | 63% | [37%–87%] | 5 | 2028Q2 |
| Cyberattack or physical sabotage halts a top-5 global agri-food processor or a major water utility | 20% | 54% | 78% | [40%–99%] | 4 | 2029Q4 |
| DAP/phosphate rock price exceeds US$1,000/tonne on a monthly average | 11% | 36% | 59% | [22%–98%] | 5 | 2030Q3 |
| Ukrainian seaborne grain exports fall below 1 Mt in a calendar month | 63% | 74% | 74% | [47%–93%] | 4 | 2027Q1 |
| Mississippi River or Panama Canal low-water event materially disrupts US grain exports | 33% | 79% | 96% | [76%–>99%] | 3 | 2028Q3 |
| Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months | 56% | 88% | 95% | [78%–99%] | 3 | 2027Q3 |
| World cereal production falls 4%+ year-on-year (multi-breadbasket failure) | 11% | 20% | 32% | [13%–64%] | 8 | 2030Q3 |
| World cereal stocks-to-use ratio falls below 28% | 7.8% | 23% | 37% | [16%–63%] | 7 | 2030Q4 |
| India physically curtails Indus western-river flows to Pakistan | 4.8% | 16% | 36% | [17%–59%] | 7 | 2032Q2 |
| FAO declares a desert locust upsurge or plague affecting three or more countries | 14% | 41% | 62% | [21%–98%] | 4 | 2030Q1 |
| Three or more countries/territories in confirmed IPC Famine simultaneously | 6.9% | 19% | 29% | [4.3%–69%] | 7 | 2030Q3 |
| Hormuz fertilizer flows normalise (downside-risk-off event) | 58% | 86% | 92% | [79%–98%] | 2 | 2027Q3 |
| Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab | 4.2% | 13% | 22% | [2.0%–58%] | 8 | 2031Q1 |
| Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water | 3.1% | 9.9% | 15% | [5.0%–27%] | 8 | 2030Q3 |
| Colorado River enters 2027 without an agreed post-2026 framework | 33% | 34% | 34% | [15%–61%] | 3 | 2027Q1 |

<details><summary>Resolution criteria</summary>

- **New IPC/CH Famine (Phase 5) classification anywhere** — The IPC Famine Review Committee or a CH equivalent confirms Famine (IPC Phase 5) — with reasonable evidence or higher — for at least one geographic area not already so classified as of 2026-07-29, published on ipcinfo.org.
- **FAO Food Price Index reaches an all-time high above 160** — The FAO Food Price Index (2014-2016=100, nominal) monthly value exceeds 160.0, surpassing the March 2022 record of 160.3.
- **Two or more top-10 staple exporters impose new broad export bans/quotas simultaneously** — Per the IFPRI Food and Fertilizer Export Restrictions Tracker, at least two countries each ranking in the global top 10 for wheat, maize or rice exports have in force, simultaneously and for at least 60 consecutive days, a new (post-2026-07-29) export ban or quota estimated to cut that country's exports of the staple by 25% or more.
- **GRFC reports more than 300 million people in acute food insecurity** — Any edition of the Global Report on Food Crises published in 2027-2036 reports more than 300.0 million people in IPC/CH Phase 3 or above for its reference year.
- **New World screwworm or FMD establishes in the US or EU cattle herd** — USDA APHIS, WOAH or the European Commission confirms sustained autochthonous transmission of New World screwworm (Cochliomyia hominivorax) north of the Mexico-US border, or an FMD outbreak in an FMD-free country of the G7, triggering a national movement standstill or export ban of 30+ days.
- **Thai 5% broken rice benchmark exceeds US$650/tonne** — FAO GIEWS / Thai Rice Exporters Association monthly average f.o.b. price for Thai white rice 5% broken exceeds US$650 per tonne.
- **WFP annual contributions fall below US$5 billion** — WFP's published annual contribution total for any calendar year 2026-2036 is below US$5.0 billion (nominal), per wfp.org contributions data.
- **World Bank monthly urea price exceeds US$800/tonne** — World Bank Pink Sheet monthly average urea (Middle East, bulk, f.o.b.) exceeds US$800 per tonne in any month.
- **Cyberattack or physical sabotage halts a top-5 global agri-food processor or a major water utility** — A publicly confirmed cyber or sabotage incident forces a 7+ day shutdown of national-scale operations at a top-5 global meat, grain-trading or fertilizer company, or causes a 7+ day loss of service at a water utility serving 1m+ people, per company disclosure, CISA/ENISA advisory or national regulator.
- **DAP/phosphate rock price exceeds US$1,000/tonne on a monthly average** — World Bank Pink Sheet monthly average DAP (f.o.b. US Gulf) exceeds US$1,000 per tonne in any month.
- **Ukrainian seaborne grain exports fall below 1 Mt in a calendar month** — Ukrainian Ministry of Agrarian Policy or UGA monthly data show total seaborne grain and oilseed exports below 1.0 million tonnes in any single calendar month (normal 2024-26 range ~3-5 Mt/month).
- **Mississippi River or Panama Canal low-water event materially disrupts US grain exports** — USDA Grain Transportation Report or Army Corps data show either (a) Mississippi barge freight rates above 800% of tariff benchmark, or draft/tow restrictions in force on the Lower Mississippi, for 30+ consecutive days, or (b) Panama Canal transit slots cut 30%+ below normal for 60+ consecutive days.
- **Animal-disease epizootic cuts a G20 country's poultry or pig inventory by 10%+ in 12 months** — USDA, Eurostat, WOAH or the national statistical agency of a G20 member reports a decline of 10% or more, within any rolling 12-month window, in national laying-hen inventory or national pig inventory, attributed principally to an animal disease epizootic (HPAI, ASF, FMD or successor).
- **World cereal production falls 4%+ year-on-year (multi-breadbasket failure)** — FAO's Cereal Supply and Demand Brief reports world cereal production for a calendar year at least 4.0% below the prior year's outturn (using FAO's own revised series at the time of the following year's July brief).
- **World cereal stocks-to-use ratio falls below 28%** — FAO's Cereal Supply and Demand Brief reports a world cereal stocks-to-use ratio below 28.0% for any marketing year.
- **India physically curtails Indus western-river flows to Pakistan** — Pakistan's IRSA rim-station data, corroborated by satellite/independent hydrological analysis, show a sustained reduction of 20% or more over at least four consecutive weeks in Chenab or Jhelum inflows attributable to Indian storage operations or diversion, and not to natural hydrology.
- **FAO declares a desert locust upsurge or plague affecting three or more countries** — FAO Desert Locust Watch raises the situation to 'Upsurge' or 'Plague' with swarms reported in three or more countries simultaneously for 60+ days.
- **Three or more countries/territories in confirmed IPC Famine simultaneously** — At any point in a calendar year, IPC/FRC-confirmed Famine (Phase 5) classifications are simultaneously in force for areas in three or more distinct countries or territories.
- **Hormuz fertilizer flows normalise (downside-risk-off event)** — World Bank or IFA data show Middle East seaborne urea and ammonia export volumes recovering to 90% or more of their 2024-25 monthly average for three consecutive months.
- **Highly virulent wheat rust or blast establishes in the Indian/Pakistani Punjab** — CIMMYT, BGRI, FAO or a national plant protection agency confirms establishment of a Ug99-lineage stem rust race, a novel highly virulent stripe rust race defeating deployed resistance, or wheat blast (Magnaporthe oryzae Triticum), in Indian or Pakistani Punjab or Haryana, with documented field-scale infection.
- **Armed attack on GERD or an Egypt-Ethiopia armed clash over Nile water** — ACLED or equivalent records a state-attributed kinetic attack (air, missile, drone or special-forces) on the Grand Ethiopian Renaissance Dam or associated Ethiopian water infrastructure, or a direct armed exchange between Egyptian and Ethiopian forces publicly framed by either government as arising from the Nile water dispute.
- **Colorado River enters 2027 without an agreed post-2026 framework** — On 1 January 2027, no seven-state consensus agreement and no signed federal Record of Decision governs Lake Powell/Lake Mead operations for calendar 2027, with operations instead running under an interim stopgap, unilateral federal action, or litigation.

</details>

## How bad decades begin

Among paths where at least three high-severity events fired, these are the most common opening sequences, in order of occurrence.

| Frequency | First | Then | Then |
|---:|---|---|---|
| 1.1% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics |
| 0.9% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China annual births fall below 7.0 million |
| 0.7% | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | China annual births fall below 7.0 million |
| 0.6% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | US Census Bureau officially reports negative net international migration |
| 0.6% | China annual births fall below 7.0 million | PISA 2025 shows no recovery in OECD-average mathematics | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window |
| 0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | China reports annual real GDP growth below 4.0% |
| 0.5% | Nvidia suffers a ≥50% peak-to-trough drawdown | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | New record-low Antarctic sea ice minimum extent | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | Global insured natural catastrophe losses exceed $200bn in a calendar year |
| <0.5% | A top-4 US hyperscaler guides annual capex down year-over-year | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | Nvidia suffers a ≥50% peak-to-trough drawdown |
| <0.5% | Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window | PISA 2025 shows no recovery in OECD-average mathematics | Major AI-infrastructure credit event: default or distressed restructuring of >=$5B of datacenter/neocloud debt |

The most common opening — Bleaching-level heat stress affects >= 60% of global reef area within a 12-month window → China annual births fall below 7.0 million → PISA 2025 shows no recovery in OECD-average mathematics — accounts for 1.1% of all paths. No single sequence dominates, which is itself informative: the model does not support a story in which one specific trigger reliably starts the cascade. What recurs is the *pattern* — a shock in one domain degrading the capacity to absorb the next.

## Where the correlations are

Pairs whose joint occurrence most exceeds what independence would predict. *Lift* is P(both) ÷ P(A)·P(B): a lift of 3 means these two show up together three times more often than chance. This is the part of the model that a spreadsheet of independent probabilities cannot produce, and it is where tail risk actually lives.

| Event A | Event B | P(both) | Lift | P(A given B) |
|---|---|---:|---:|---:|
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | 62% | 1.1× | 81% |
| China's extraterritorial rare-earth export control regime enters into force | Severe rare-earth supply cutoff to the US or EU | 49% | 1.1× | 92% |
| US recession with NBER-dated peak in the window | Global recession (world real GDP growth below 2.0% in a calendar year) | 58% | 1.1× | 91% |
| Nvidia suffers a ≥50% peak-to-trough drawdown | A top-4 US hyperscaler guides annual capex down year-over-year | 75% | 1.1× | 91% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 67% | 1.1× | 79% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | A single training run of ≥1e28 FLOP is publicly reported | 64% | 1.1× | 77% |
| FAO Food Price Index reaches an all-time high above 160 | GRFC reports more than 300 million people in acute food insecurity | 69% | 1.0× | 81% |
| US unemployment rate ≥6.0% for three consecutive months | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 73% | 1.0× | 86% |
| Global recession (world real GDP growth below 2.0% in a calendar year) | Severe rare-earth supply cutoff to the US or EU | 35% | 1.0× | 66% |
| Civil war onset in a country of 50 million or more that was at peace in mid-2026 | A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 54% | 1.0× | 85% |
| China reports annual real GDP growth below 4.0% | Severe rare-earth supply cutoff to the US or EU | 44% | 1.0× | 84% |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | A Fortune 500 firm announces ≥10,000 job cuts explicitly attributed primarily to AI | 67% | 1.0× | 79% |
| Nvidia suffers a ≥50% peak-to-trough drawdown | Global recession (world real GDP growth below 2.0% in a calendar year) | 55% | 1.0× | 87% |
| AI-orchestrated cyberattack causes ≥$1B damage or a national-scale critical-infrastructure disruption | A single training run of ≥1e28 FLOP is publicly reported | 65% | 1.0× | 79% |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | Severe rare-earth supply cutoff to the US or EU | 47% | 1.0× | 89% |
| Frontier agent reaches a 1-work-month 50%-reliability task horizon | US unemployment rate ≥6.0% for three consecutive months | 62% | 1.0× | 75% |
| US recession with NBER-dated peak in the window | A top-4 US hyperscaler guides annual capex down year-over-year | 71% | 1.0× | 86% |
| Disintegration of the Thwaites Eastern Ice Shelf | A second US kinetic operation to remove or kill a sitting foreign head of state or government | 39% | 1.0× | 62% |

## Continuous indicators

These evolve on a Gaussian copula driven by each path's own systemic-stress index, so the bad tails of these distributions are populated by the same paths that fired the bad events — not by independent noise.

| Indicator | Now | 2031 (p10 / p50 / p90) | 2036 (p10 / p50 / p90) |
|---|---:|:---:|:---:|
| World military expenditure as share of global GDP (percent of global GDP) | 2.5 | 2.59 / **2.89** / 3.25 | 2.71 / **3.12** / 3.6 |
| Global state-based armed conflict battle deaths per year (thousands of deaths per year) | 160 | 54 / **130** / 244 | 10.1 / **114** / 275 |
| Brent crude oil price (USD per barrel (annual average)) | 86 | 45.4 / **71.9** / 140 | 27.1 / **66.4** / 159 |
| US military expenditure as share of US GDP (percent of GDP) | 3.2 | 2.95 / **3.3** / 3.7 | 2.87 / **3.35** / 3.9 |
| European NATO members' aggregate defence spending as share of GDP (percent of GDP) | 2.65 | 3 / **3.35** / 3.74 | 3.26 / **3.73** / 4.28 |
| PLA aircraft sorties entering Taiwan's ADIZ per year (sorties per year) | 3600 | 2.46e+03 / **4.98e+03** / 7.83e+03 | 2.13e+03 / **5.77e+03** / 9.7e+03 |
| US dollar share of allocated global FX reserves (percent) | 58 | 51 / **54** / 57.1 | 47.6 / **51.8** / 56 |
| Weekly container-ship transits of the Suez Canal (transits per week) | 30 | 21.8 / **61.6** / 87.7 | 24.4 / **80.1** / 115 |
| Combined US + Russia deployed strategic nuclear warheads (warheads) | 3200 | 3.14e+03 / **3.71e+03** / 4.34e+03 | 3.21e+03 / **3.99e+03** / 4.87e+03 |
| Net monthly Russian territorial gain in Ukraine (km2 per month (negative = Ukrainian recapture)) | 104 | -29.3 / **8.86** / 178 | -96.4 / **-44.4** / 180 |
| Number of active state-based armed conflicts (>=25 battle deaths/year) (count) | 61 | 48 / **57.8** / 68.1 | 42.4 / **56.3** / 70 |
| Crude and condensate transiting the Strait of Hormuz (million barrels per day) | 8 | 5.35 / **17.9** / 21 | 5.06 / **23.4** / 27.7 |
| Annual global mean surface temperature anomaly (ERA5, vs 1850-1900) (C) | 1.47 | 1.48 / **1.62** / 1.78 | 1.51 / **1.7** / 1.92 |
| Annual mean CO2 concentration at Mauna Loa (ppm) | 429.4 | 440 / **442** / 445 | 446 / **449** / 452 |
| NOAA global mean atmospheric methane (ppb) | 1945 | 1.97e+03 / **1.98e+03** / 2e+03 | 1.98e+03 / **2e+03** / 2.02e+03 |
| Global fossil CO2 emissions (Global Carbon Project) (GtCO2/yr) | 38.1 | 35.6 / **38.3** / 40 | 34.7 / **38.3** / 41 |
| Global mean sea level (satellite altimetry, above 1993 baseline) (mm) | 112 | 132 / **138** / 144 | 144 / **152** / 160 |
| Arctic sea ice September minimum extent (NSIDC) (million km2) | 4.3 | 3.35 / **3.98** / 4.56 | 2.94 / **3.83** / 4.61 |
| Annual maximum 3-month ONI (Nino3.4) (C) | 2.4 | -0.886 / **0.43** / 1.72 | -2.48 / **-0.71** / 1.17 |
| Share of global reef area under Alert Level 1+ heat stress, rolling 12 months (% of global reef area) | 55 | 31.8 / **61.9** / 87 | 23.8 / **66.1** / 102 |
| Brazilian Legal Amazon annual deforestation (INPE PRODES) (km2/yr) | 5796 | 3.09e+03 / **4.96e+03** / 9.95e+03 | 1.85e+03 / **4.39e+03** / 1.1e+04 |
| FAO Food Price Index (nominal) (index, 2014-2016 = 100) | 130.3 | 121 / **140** / 167 | 119 / **145** / 181 |
| Annual increase in global 0-2000m ocean heat content (ZJ/yr) | 23 | 13.1 / **25** / 37.1 | 9.42 / **26.3** / 43 |
| Brent crude oil price (USD per barrel) | 84 | 41.4 / **78** / 151 | 25.5 / **75.9** / 175 |
| US 10-year Treasury yield (percent) | 4.62 | 3.1 / **4.81** / 6.36 | 2.6 / **4.95** / 7.03 |
| US CPI inflation, year over year (percent) | 3.5 | 1.21 / **2.62** / 4.95 | 0.238 / **2.1** / 5.29 |
| Federal funds target rate, upper bound (percent) | 3.75 | 1.82 / **3.53** / 5.23 | 0.874 / **3.34** / 5.81 |
| S&P 500 index level (index points) | 7412 | 6.13e+03 / **9.98e+03** / 1.61e+04 | 6.03e+03 / **1.15e+04** / 1.97e+04 |
| Global real GDP growth (percent per year) | 3 | 1.61 / **3.21** / 4.23 | 1.1 / **3.27** / 4.68 |
| China reported real GDP growth (percent per year) | 4.6 | 1.86 / **3.39** / 4.77 | 0.657 / **2.71** / 4.7 |
| US federal debt held by the public / GDP (percent) | 100 | 106 / **111** / 119 | 110 / **117** / 128 |
| USD share of allocated FX reserves (IMF COFER) (percent) | 56.5 | 46.9 / **52.1** / 57 | 42.6 / **49.5** / 56.3 |
| Gold price (USD per troy ounce) | 4040 | 3.09e+03 / **4.69e+03** / 7.24e+03 | 2.86e+03 / **5.02e+03** / 8.6e+03 |
| USD/JPY exchange rate (yen per dollar) | 163.6 | 118 / **151** / 193 | 97.4 / **145** / 201 |
| US average effective tariff rate on all imports (percent) | 6 | 2.94 / **7.95** / 18.1 | 2.05 / **9.02** / 22.9 |
| Log10 of training compute for the largest publicly-known training run (log10(FLOP)) | 26.7 | 28 / **28.8** / 29.5 | 28.8 / **30** / 30.9 |
| Global data center electricity consumption (TWh per year) | 590 | 832 / **1.03e+03** / 1.34e+03 | 999 / **1.28e+03** / 1.72e+03 |
| Combined annual capex, Microsoft + Alphabet + Amazon + Meta (USD billions per year) | 700 | 480 / **986** / 1.49e+03 | 429 / **1.14e+03** / 1.87e+03 |
| Nvidia annual data center revenue (USD billions per year) | 330 | 232 / **538** / 860 | 233 / **653** / 1.12e+03 |
| Combined annualized revenue run-rate, OpenAI + Anthropic (USD billions) | 72 | 165 / **347** / 619 | 247 / **501** / 868 |
| Log2 of METR 50%-reliability task time horizon (log2(hours of human-expert task time)) | 1.6 | 5.38 / **8.08** / 10.9 | 7.76 / **11.6** / 15.4 |
| Log10 of API price for GPT-4-class capability (log10(USD per million input tokens)) | -0.4 | -2.19 / **-1.79** / -1.4 | -3.13 / **-2.57** / -2.02 |
| Chinese open-weight models' share of OpenRouter tokens (percent) | 61 | 32.3 / **60.1** / 83.3 | 20.5 / **58.9** / 92.3 |
| Log10 of US paid fully-driverless rides per week (millions) (log10(millions of rides per week)) | -0.3 | 0.183 / **0.903** / 1.38 | 0.588 / **1.58** / 2.27 |
| US AI adoption in production, employment-weighted (Census BTOS) (percent of employment at AI-using firms) | 32 | 45 / **56.2** / 67.9 | 54.2 / **69** / 85.7 |
| Global total fertility rate (births per woman) | 2.23 | 2.03 / **2.12** / 2.21 | 1.94 / **2.06** / 2.19 |
| China annual births (million births per year) | 7.92 | 4.62 / **5.91** / 7.39 | 3.05 / **4.83** / 6.87 |
| US total fertility rate (births per woman) | 1.585 | 1.44 / **1.51** / 1.59 | 1.37 / **1.47** / 1.58 |
| Global forcibly displaced persons (million people) | 117.8 | 103 / **120** / 141 | 96.9 / **121** / 149 |
| US net international migration (thousand persons per year) | 320 | -129 / **629** / 1.41e+03 | -289 / **794** / 1.89e+03 |
| EU+ annual asylum applications (thousand applications per year) | 822 | 320 / **688** / 1.35e+03 | 113 / **645** / 1.54e+03 |
| India total fertility rate (births per woman) | 1.9 | 1.62 / **1.73** / 1.83 | 1.49 / **1.64** / 1.77 |
| World population (billion people) | 8.3 | 8.57 / **8.63** / 8.69 | 8.73 / **8.81** / 8.89 |
| China population aged 60 and over (percent of total population) | 22.9 | 27.1 / **28** / 28.8 | 29.6 / **30.8** / 31.9 |
| US annual drug overdose deaths (thousand deaths per year) | 70 | 34.7 / **55.1** / 79.8 | 18.6 / **47.7** / 82.9 |
| South Korea total fertility rate (births per woman) | 0.8 | 0.746 / **0.87** / 1 | 0.728 / **0.905** / 1.09 |
| Japan annual births (Japanese nationals) (thousand births per year) | 670 | 467 / **538** / 607 | 363 / **466** / 563 |
| Brent crude oil price (USD/bbl (nominal)) | 73 | 42.4 / **71.4** / 128 | 29.7 / **70.6** / 150 |
| Annual global solar PV capacity additions (GWdc/yr) | 650 | 642 / **882** / 1.18e+03 | 672 / **1.01e+03** / 1.42e+03 |
| Lithium-ion battery pack price (volume-weighted, all segments) (USD/kWh (nominal)) | 105 | 54.4 / **71.6** / 95.2 | 30.5 / **54.2** / 85 |
| China share of global rare-earth separation and refining (% of global refined output) | 87 | 72.1 / **79.1** / 86.9 | 65 / **74.6** / 85.8 |
| US data center electricity consumption (TWh/yr) | 225 | 326 / **470** / 687 | 399 / **600** / 890 |
| EU average wholesale electricity price (EUR/MWh (nominal)) | 80 | 40 / **66.4** / 119 | 23.2 / **59.3** / 130 |
| Global coal demand (Mt/yr) | 8800 | 7.66e+03 / **8.47e+03** / 9.05e+03 | 7.2e+03 / **8.29e+03** / 9.09e+03 |
| Uranium spot price (USD/lb U3O8) | 88 | 54.1 / **106** / 187 | 42.1 / **115** / 227 |
| Global oil (liquids) demand (million b/d) | 104.5 | 102 / **106** / 109 | 102 / **107** / 112 |
| Global LNG liquefaction nameplate capacity (Mtpa) | 510 | 655 / **712** / 754 | 743 / **822** / 883 |
| Global EV share of new light-vehicle sales (% of new sales) | 22.4 | 32.1 / **40** / 47.8 | 38.6 / **49.8** / 60.8 |
| Henry Hub natural gas price (USD/MMBtu (nominal)) | 3.7 | 2.52 / **4.29** / 6.99 | 2.07 / **4.5** / 8.38 |
| Cumulative confirmed H5N1-infected US dairy herds (herds) | 1166 | 1.3e+03 / **1.82e+03** / 2.58e+03 | 1.46e+03 / **2.19e+03** / 3.27e+03 |
| Confirmed human H5 (any NA) influenza cases reported globally per year (cases/year) | 14 | 2.98 / **16.5** / 65.8 | -0.879 / **18.4** / 85.1 |
| US confirmed measles cases per calendar year (cases/year) | 2900 | 907 / **3.78e+03** / 8.85e+03 | 167 / **4.24e+03** / 1.16e+04 |
| US kindergarten MMR vaccination coverage (% of kindergartners) | 92.5 | 89 / **90.6** / 92.2 | 87.3 / **89.5** / 91.8 |
| Global DTP3 immunization coverage (% of surviving infants) | 85 | 81.9 / **83.9** / 86 | 80.3 / **83.3** / 86.1 |
| Deaths directly attributable to bacterial AMR (million deaths/year) | 1.2 | 1.16 / **1.31** / 1.46 | 1.16 / **1.37** / 1.58 |
| International financing for HIV in low- and middle-income countries (US$ billions/year) | 7.3 | 3.16 / **5.4** / 7.87 | 1.36 / **4.39** / 7.71 |
| US adults currently using GLP-1 drugs for weight loss (% of adults) | 12.4 | 16.1 / **23.2** / 31 | 19 / **29** / 40 |
| US adult obesity prevalence (Gallup self-reported) (% of adults) | 36.4 | 31.5 / **33.4** / 35.3 | 29.2 / **31.7** / 34.3 |
| WHO approved base programme budget per biennium (US$ billions/biennium) | 4.2 | 3.42 / **4.09** / 5.09 | 3.06 / **4.04** / 5.44 |
| Global malaria deaths (thousand deaths/year) | 610 | 561 / **636** / 716 | 544 / **650** / 762 |
| CDC full-time federal workforce (thousand FTEs) | 9 | 6.62 / **8.2** / 9.85 | 5.49 / **7.72** / 10.1 |
| US presidential net approval (approve minus disapprove, aggregate) (percentage points) | -19 | -29.2 / **-9.97** / 6.14 | -30.2 / **-4.79** / 17 |
| Number of countries coded as currently autocratizing by V-Dem (countries) | 44 | 37 / **45** / 54 | 34.7 / **45.5** / 57.7 |
| Countries with net decline in Freedom House score in a given year (countries) | 54 | 39.9 / **51** / 62.8 | 34.2 / **49.4** / 65.9 |
| Share of world population living in Freedom House 'Free' countries (percent) | 21 | 15 / **20.1** / 24 | 12.6 / **19.5** / 25 |
| AfD federal voting intention (percent) | 27 | 19 / **27.9** / 36 | 15.8 / **28.6** / 39.8 |
| French RN first-round national vote share (presidential/legislative) (percent) | 35 | 27.9 / **35.9** / 44.2 | 25.1 / **36.7** / 47.9 |
| Reform UK voting intention (percent) | 26 | 14.1 / **23.9** / 34.9 | 8.93 / **23** / 38.4 |
| Successful coups d'etat worldwide per calendar year (coups) | 2 | -0.0345 / **1.96** / 4.91 | -0.784 / **2.07** / 6.15 |
| US terrorism and targeted-violence events per year (START/BDI coding) (events) | 1050 | 717 / **1.22e+03** / 1.76e+03 | 615 / **1.33e+03** / 2.08e+03 |
| Gallup average 'great deal / quite a lot' confidence across nine US institutions (percent) | 27 | 20.9 / **25.9** / 31.1 | 18.7 / **25.4** / 32.3 |
| ACLED-recorded political violence events worldwide per year (events) | 1.85e+05 | 1.51e+05 / **1.96e+05** / 2.48e+05 | 1.39e+05 / **2.03e+05** / 2.74e+05 |
| FAO Food Price Index (nominal) (index, 2014-2016=100) | 130.3 | 112 / **146** / 196 | 108 / **154** / 226 |
| World cereal stocks-to-use ratio (percent) | 32 | 27.7 / **31.1** / 34.5 | 25.9 / **30.7** / 35.4 |
| World cereal production (million tonnes per calendar year) | 2983 | 2.96e+03 / **3.13e+03** / 3.29e+03 | 2.96e+03 / **3.19e+03** / 3.43e+03 |
| Urea price (Middle East granular, f.o.b.) (USD per tonne) | 520 | 229 / **441** / 851 | 113 / **397** / 953 |
| People in acute food insecurity (IPC/CH Phase 3+, GRFC) (million people) | 266 | 226 / **291** / 357 | 213 / **303** / 395 |
| People in IPC/CH Phase 5 (Catastrophe) (million people) | 1.4 | 0.347 / **1.6** / 3.47 | -0.0683 / **1.74** / 4.33 |
| CBOT front-month wheat price (USD per bushel) | 6.9 | 5.06 / **7.68** / 12.1 | 4.65 / **8.17** / 14.3 |
| Thai white rice 5% broken, f.o.b. (USD per tonne) | 365 | 248 / **409** / 659 | 210 / **426** / 777 |
| Lake Mead elevation (feet above mean sea level) | 1053 | 991 / **1.03e+03** / 1.07e+03 | 964 / **1.02e+03** / 1.07e+03 |
| WFP annual contributions received (USD billion, nominal) | 6.5 | 3.33 / **5.53** / 7.82 | 1.98 / **4.93** / 8.13 |
| Global undernourishment headcount (PoU) (million people) | 645 | 531 / **602** / 675 | 481 / **580** / 678 |
| Share of marine fish stocks within biologically sustainable levels (percent) | 62.4 | 57.5 / **60** / 62.4 | 55.3 / **58.7** / 62.1 |

## What drives the outcome

Share of the variance in peak systemic stress attributable to each event firing at all. High-scoring nodes are the ones worth watching, because learning how they resolve collapses the most uncertainty about everything else.

*Read with one caveat:* the stress index is built from these same events, so part of any node's score is its own contribution rather than its influence on others. The ranking is still informative — it combines probability, impact rating and correlation with the rest of the system in one number — but it is not a pure causal-influence measure, and a node cannot score high here without being either likely or heavy.

| Event | Variance share | P(by 2036) | Impact |
|---|---:|---:|---:|
| Global recession (world real GDP growth below 2.0% in a calendar year) | 4.7% | 63% | 7 |
| S&P 500 falls 30%+ from its all-time closing high | 3.5% | 64% | 6 |
| Severe rare-earth supply cutoff to the US or EU | 3.4% | 53% | 8 |
| Direct US-PRC military exchange causing at least one fatality | 2.6% | 14% | 9 |
| PRC launches an amphibious or airborne assault on Taiwan's main island | 2.6% | 13% | 10 |
| PRC imposes a declared and enforced quarantine or blockade of Taiwan lasting >=7 days | 2.5% | 28% | 9 |
| US average effective tariff rate exceeds 15% | 2.2% | 51% | 5 |
| Failure or extraordinary rescue of a bank with over $250bn in assets | 1.9% | 46% | 8 |
| US 10-year Treasury yield closes at or above 6.00% | 1.7% | 40% | 8 |
| China reports annual real GDP growth below 4.0% | 1.6% | 81% | 6 |
| A NATO or EU member state currently coded as a democracy is downgraded to electoral autocracy by V-Dem | 1.6% | 63% | 8 |
| Wave of emerging-market sovereign defaults or restructurings | 1.5% | 78% | 5 |
| Strait of Hormuz crude transit below 50% of 2025 baseline for >=30 consecutive days (new episode after 1 Aug 2026) | 1.4% | 86% | 8 |
| WFP annual contributions fall below US$5 billion | 1.4% | 68% | 5 |
| AI capex bust: aggregate hyperscaler capex falls 20%+ year over year | 1.3% | 57% | 7 |
| World cereal stocks-to-use ratio falls below 28% | 1.2% | 37% | 7 |
| World cereal production falls 4%+ year-on-year (multi-breadbasket failure) | 1.2% | 32% | 8 |
| Large private-credit vehicle suspends redemptions or enters wind-down | 1.2% | 55% | 6 |

## Where the worldviews disagree most

The five parameterisations — raw analyst, audited, outside-view base rates, structural-break inside view, and prediction-market check — converge on most nodes. These are the ones where they don't, and they are exactly the forecasts you should hold most loosely.

| Event | Analyst | Audited | Outside view | Structural break | Market check | Spread |
|---|---:|---:|---:|---:|---:|---:|
| Japan 10-year government bond yield reaches 3.00% | 61% | 95% | 97% | 94% | 95% | 36pp |
| Strait of Hormuz closed again for 14+ consecutive days | 41% | 70% | 70% | 70% | 70% | 29pp |
| Brent monthly average above $120/bbl | 43% | 66% | 68% | 67% | 68% | 25pp |
| US life expectancy at birth reaches 80.0 years | 62% | 86% | 87% | 86% | 85% | 25pp |
| Severe rare-earth supply cutoff to the US or EU | 32% | 54% | 54% | 55% | 54% | 23pp |
| FAO Food Price Index reaches an all-time high above 160 | 60% | 80% | 80% | 82% | 81% | 22pp |
| Nvidia suffers a ≥50% peak-to-trough drawdown | 68% | 87% | 87% | 87% | 88% | 21pp |
| Colorado River enters 2027 without an agreed post-2026 framework | 51% | 32% | 31% | 35% | 32% | 20pp |
| China's extraterritorial rare-earth export control regime enters into force | 67% | 85% | 86% | 85% | 87% | 20pp |
| A US state enacts a statutory moratorium or hard cap on new large datacenter interconnections | 66% | 48% | 49% | 47% | 47% | 19pp |
| A G7 country cuts permanent immigration by three quarters | 19% | 36% | 35% | 37% | 37% | 19pp |
| The 2026-27 El Nino verifies as very strong (ONI peak >= +2.0C) | 89% | 73% | 71% | 73% | 72% | 18pp |
| World cereal production falls 4%+ year-on-year (multi-breadbasket failure) | 48% | 32% | 30% | 31% | 31% | 18pp |
| Officially acknowledged incident where AI materially enabled acquisition or design of a dangerous pathogen or toxin | 31% | 48% | 49% | 47% | 48% | 18pp |
| Verified wet-bulb temperature of 35C sustained for three or more hours | 51% | 34% | 36% | 34% | 35% | 17pp |
| State-attributed cyberattack causing >=24h electricity loss to >=1 million people in a NATO or OECD country | 33% | 17% | 18% | 18% | 17% | 16pp |

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
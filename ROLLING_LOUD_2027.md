# Rolling Loud 2027 — a forecast

**Information cutoff: 16 September 2026.** Produced by `predict_rolling_loud.py`
(RL-SIM), fitted to the six US flagship editions Rolling Loud has staged since
2023 and backtested leave-one-edition-out before being run forward.

---

## 1. What is actually on the calendar

This matters more than any individual name, because the honest first answer to
"what are next year's Rolling Loud lineups" is that there is now essentially
**one** of them.

| Edition | Dates | Venue | Status |
|---|---|---|---|
| Rolling Loud India 2026 | 12–13 Dec 2026 | Loud Park, Navi Mumbai | Announced, lineup TBA |
| **Rolling Loud Florida 2027** | **7–9 May 2027** | **Camping World Stadium, Orlando** | **Announced 15 Sep 2026, lineup TBA** |
| Rolling Loud California 2027 | 13–14 Mar 2027 (rumoured) | Hollywood Park | **Not announced.** A projected date on secondary listing sites only |
| Rolling Loud Europe 2027 | — | — | **Not announced.** Last European edition was Austria, July 2024 |

The brand has contracted hard, and the run of failures is the most predictive
fact in this document:

- **Miami 2025** — never staged. The annual Miami edition simply did not happen.
- **California 2026** — dropped. 2026 was the first year since 2016 with only
  one US Rolling Loud.
- **Australia 2026** — announced in November 2025 with a full lineup (Gunna, Ken
  Carson, Sexyy Red), then **cancelled outright** in the new year.

Against that, Orlando 2026 worked: roughly 65,000 a day across three sold-out
days, and the festival posted "THANK YOU ORLANDO SEE YOU IN 2027" before the
site was clear. Co-founders Tariq Cherif and Matt Zingler framed the
consolidation as deliberate — one anchor US event, lower ticket prices, room to
grow — rather than as retreat.

**P(Florida 2027 is staged as announced) ≈ 93%.** Every probability below is
conditional on that. Multiply by 0.93 for unconditional odds.

**When the lineup drops:** Rolling Loud's reveal has landed 115–130 days before
doors with unusual consistency across the last four editions. For a 7 May 2027
opening that centres the announcement on **roughly 5–12 January 2027**.

---

## 2. The bottom line

My single best guess at the three headline slots:

> ### Don Toliver · Playboi Carti · Rod Wave

That exact trio is the most likely single slate at **8.9%** — which sounds low
until you note there are over 19,000 three-name combinations in the candidate
pool, and the next-best slate is at 3.2%. Nobody should expect to name three of
three; the useful output is the per-artist column.

| Artist | P(headlines) | ±2 MC se | Why |
|---|---|---|---|
| **Don Toliver** | **68.5%** | ±0.2% | No. 2 hottest rapper as of Sep 2026; *Octane* was 2026's top-selling rap album for months. Already headlined Orlando 2026 and India 2025 |
| **Playboi Carti** | **46.8%** | ±0.2% | Five of the last six flagship headline slates, four consecutively. *Baby Boi* reported finished |
| **Rod Wave** | **42.7%** | ±0.2% | No. 3 hottest, *Don't Look Down* (Aug 2026), career-biggest arena tour, **and he is from St. Petersburg** |
| Yeat | 20.2% | ±0.2% | Top-10 heat, *ADL* double album. Has played Rolling Loud but never closed a US night — the pool's most obvious unpromoted act |
| Travis Scott | 18.0% | ±0.2% | Three of six flagships. Increasingly routes his own stadium production instead |
| Ken Carson | 12.1% | ±0.1% | Closed 2026 on a day's notice; two Rolling Loud headline bookings already banked |
| Drake | 11.5% | ±0.1% | Hottest rapper alive and has never played a Rolling Loud in eleven years. See §6 — I think this is too high |
| Gunna | 11.0% | ±0.1% | Owed a headline slot by the cancelled Australia edition; *The Last Wun* hit No. 1 |
| Lil Uzi Vert | 10.9% | ±0.1% | Booked to headline Cali 2024 and pulled out. No competing tour calendar |
| Lil Wayne | 8.0% | ±0.1% | Legacy closer, cheap relative to draw |
| YoungBoy Never Broke Again | 6.4% | ±0.1% | Booked to close 2026 and withdrew the day before |
| J. Cole | 5.9% | ±0.1% | Topped the spring-2026 heat list; runs a competing festival |
| Future | 5.5% | ±0.1% | Three of six flagships, the reliable fallback |
| Lil Baby | 4.5% | ±0.1% | Cooled from his 2022 peak |

Anyone not listed sits below 3%. **Lil Durk is the wildcard the table
understates**: acquitted on all counts on 11 September 2026 but still in custody
for a federal racketeering trial starting 5 October. He is at 22% availability
in the model, so ~1% to headline. If that trial also clears him, he walks into
winter with the best comeback narrative in rap, and a Florida festival would pay
for it. Watch that docket, not the charts.

---

## 3. The model, and why you should believe any of this

A conditional logit (Plackett-Luce) over the pool of acts who could plausibly
close a night, fitted by penalised maximum likelihood to **18 headline bookings
across six editions**, then integrated forward over coefficient uncertainty and
per-artist availability across 200,000 paths.

Feature set and ridge penalty were both chosen by **leave-one-edition-out
predictive likelihood** — never by which answer looked nicer. Each held-out
edition was predicted by a model refitted on the other five:

| | top-3 hit rate |
|---|---|
| **RL-SIM** | **66.7%** |
| Rank by popularity alone | 22.2% |
| Rebook last edition's headliners | 16.7% |
| Uniform draw from the pool | 7.0% |

Four specifications were scored. The winner adds **draw** — the size of room an
artist sells on their own name — to the obvious features:

| spec | ridge | hit | LOO log-lik |
|---|---|---|---|
| **draw** | 0.25 | 66.7% | **−38.46** ← selected |
| full (draw + back-to-back) | 0.25 | 61.1% | −39.49 |
| base (no draw) | 2.00 | 61.1% | −48.15 |
| back-to-back, no draw | 1.00 | 50.0% | −48.18 |

Without a draw term the model cheerfully promoted buzzing club acts to stadium
headliners — it had EsDeeKid at 12% to close a 65,000-capacity night. Separating
cultural heat from ticket-selling capacity fixed that and improved held-out
likelihood by ten log points.

Seventeen validation checks pass in `tests/test_rlsim.py`, including the
Plackett-Luce likelihood against its closed form, the Gumbel top-k sampler
against the softmax marginal, monotonicity in draw, and headline probabilities
summing exactly to the number of slots.

---

## 4. Three things the fit says that the conventional wisdom doesn't

**Draw beats heat, and bookability beats both.** Standardized coefficients:

```
draw          +2.580     can you sell out a stadium night on your own name
fest_avail    +2.472     do you take third-party festival bookings at all
heat          +1.482     how hot are you right now
rl_fit        -0.876     (see caution below)
hl_hist       -0.529     did you headline here recently
regional_fl   -0.029     Florida connection
```

**Rolling Loud rotates its headliners.** `hl_hist` is *negative*: conditional on
draw and heat, having headlined recently makes you **less** likely to be booked
again. The raw data agrees — only 4 of 14 headline slots went to someone who
closed the immediately preceding edition (28.6%), and "rebook last year" was the
*worst-performing* baseline at 16.7%. Playboi Carti keeps getting the slot
because his draw and heat are elite, not because incumbency helps him. It hurts
him, and he wins anyway.

**A Florida connection does nothing for headliners and a lot for the undercard.**
`regional_fl` is −0.03 at the top of the bill — headliners are national acts —
but +0.59 in the undercard model. So expect the Florida story to play out in the
mid-card (BossMan Dlow, Luh Tyler, Hurricane Wisdom, Denzel Curry, Ski Mask, JT,
Rick Ross), not in the closing slots. Rod Wave is the exception that would prove
it, and he gets there on draw and heat, not on his area code.

⚠️ **Do not read `rl_fit`'s negative sign causally.** It is collinear with draw
— underground rage acts score high on brand fit and low on draw — so the two
coefficients split one effect between them. The pair is interpretable; neither
number is on its own.

---

## 5. The undercard

A separate logistic model on edition-to-edition persistence. The same draw
control was needed here, for the opposite reason: without it the model pooled
headline-tier acts (which Rolling Loud rotates *out*) with undercard acts (which
it recycles), and the popularity and prior-appearance coefficients came out
sign-flipped. Controlling for draw separates the populations and the signs
correct themselves:

```
rl_fit        +3.191     brand fit is the dominant undercard driver
draw          -4.049     big acts headline or skip; they don't fill the mid-card
regional_fl   +0.586     Florida pays here
on_prev_bill  +0.578     last year's bill is the starting point for this year's
heat          +0.452
prior_bills   +0.010     ~zero; see caveat
```

P(appears anywhere on the announced lineup), conditional on the edition
happening:

| | |
|---|---|
| 60%+ | Don Toliver, Playboi Carti, BossMan Dlow, Molly Santana, Luh Tyler, 1900Rugrat, BabyChiefDoit, Pooh Shiesty, OsamaSon, Sorisa |
| 50–60% | EsDeeKid, Nettspend, fakemink, Homixide Gang, Skrilla, Che, xaviersobased, Rod Wave, SahBabii |
| 40–50% | SoFaygo, NoCap, skaiwater, TiaCorine, Hurricane Wisdom, Destroy Lonely, Ken Carson, Rich Amiri, Yeat, Sexyy Red |
| 25–40% | ian, Quavo, Ski Mask, Chief Keef, Travis Scott, Denzel Curry, Gunna, NBA YoungBoy |

Structurally, expect roughly what 2026 delivered: ~78 acts, a fifth of them on
the Opium/rage axis, a fifth Florida and the South, a UK contingent that is now
a fixture rather than a novelty (EsDeeKid, fakemink, Feng), and around 14% women.

---

## 6. Where I'd bet against my own model

Reporting the model faithfully and then saying where I disagree is more useful
than quietly tuning it until it agrees with me. Three places:

**Don Toliver at 68.5% is too high — call it 50–55%.** The model's own
calibration check flags this: it expects 1.34 of 3 slots to go to a 2026
headliner (44.6%) against a historical base rate of 28.6%. Toliver's September
2026 popularity rank is extreme enough to overwhelm the rotation penalty. The
sensitivity run shows how much rides on that one coefficient:

| rotation prior | resulting top of the slate |
|---|---|
| none (0.0) | Carti 79%, Toliver 72%, Rod Wave 37%, Travis 27% |
| **fitted (−0.53)** | **Toliver 71%, Carti 49%, Rod Wave 47%, Yeat 20%** |
| strong (−1.5) | Toliver 61%, Rod Wave 54%, Yeat 34%, Ken Carson 22% |

Note Toliver leads under *every* prior. The disagreement is about the margin,
not the pick.

**Drake at 11.5% is too high — call it 5%.** With 18 training observations the
model cannot learn artist-specific fixed effects; it only sees features. "Has
declined to play this festival for eleven consecutive years" is not a feature,
and it enters only through a hand-assigned `fest_avail` of 0.15. The same
caution applies to JAY-Z and Ye.

**Sexyy Red at 40% is too low — call it 55–65%.** She has been on every US
flagship bill since 2023 and was a booked Australia headliner. The feature that
should capture an unbroken streak, `prior_bills`, is fitted at +0.010 — which is
to say the two available transitions cannot identify it, so the model regresses
everyone toward the base rate. The same correction applies upward to Destroy
Lonely and Quavo.

---

## 7. What would move this forecast

- **Lil Durk's racketeering verdict (from 5 Oct 2026).** An acquittal takes him
  from ~1% to a genuine headline candidate.
- **Whether *Baby Boi* actually comes out.** A live Carti album cycle in spring
  2027 pushes him from 47% toward 60%; another year shelved pushes him down.
- **NBA YoungBoy's touring intentions.** He said he needed time away from
  performing. If he announces 2027 dates he is immediately a top-four candidate
  and Rolling Loud owes him a make-good.
- **A California 2027 announcement.** Two US editions would split the headline
  pool and lower every probability here.
- **Rod Wave's post-tour plans.** His arena run ends 19 Nov 2026. A spring 2027
  album or tour leg makes a May festival slot natural; a quiet winter makes it
  less so.

---

## 8. Honest limits

The error bars above are Monte Carlo sampling noise. They are the *least*
important source of uncertainty here.

1. **Eighteen headline bookings.** That is the entire training set. Every
   coefficient standard deviation in §4 is large relative to its estimate.
2. **The backtest is optimistic.** Popularity ranks for pre-2026 editions were
   assigned retrospectively, knowing what happened next. 66.7% is an upper bound
   on genuine out-of-sample skill, not an estimate of it. The observed ranks for
   the 2027 forecast itself are clean — they come from Complex's September 2026
   overhaul, published before any 2027 booking was known.
3. **Undercard rosters are reconstructed from trade coverage**, which prints
   maybe the top 25–30 of a 78-act bill. The 32.6% measured return rate is a
   *lower bound*, and undercard probabilities are scoped to artists prominent
   enough that a booking would be reported.
4. **Availability is elicited, not fitted.** `avail_2027` is a judgement per
   artist. It is documented in-file with reasoning, and it does real work — it is
   why Drake is not simply predicted to headline everything.

---

## 9. Sources

Dates, venues and headline slates: [Rolling Loud Florida 2027 announcement (Complex, 15 Sep 2026)](https://www.complex.com/music/a/will-lavin/rolling-loud-florida-2027-announced-pre-sale) ·
[Digital Music News](https://www.digitalmusicnews.com/2026/09/15/rolling-loud-florida-returns-may-2027/) ·
[2026 lineup (Billboard)](https://www.billboard.com/music/concerts/rolling-loud-festival-only-2026-us-date-orlando-camping-world-1236150340/) ·
[2026 lineup (BrooklynVegan)](https://www.brooklynvegan.com/rolling-loud-2026-us-lineup-playboi-carti-don-toliver-nba-youngboy-sexyy-red-chief-keef-che-more/) ·
[The FADER](https://www.thefader.com/2026/01/07/rolling-loud-2026-orlando-announce-lineup) ·
[Variety](https://variety.com/2026/music/news/rolling-loud-us-lineup-2026-playboi-carti-youngboy-don-toliver-1236631024/) ·
[NBA YoungBoy withdrawal / Ken Carson substitution (Billboard)](https://www.billboard.com/music/rb-hip-hop/nba-youngboy-cancels-rolling-loud-orlando-ken-carson-1236242344/) ·
[Pollstar](https://news.pollstar.com/2026/05/07/ken-carson-steps-in-to-headline-rolling-loud-after-nba-youngboy-backs-out/) ·
[Ken Carson set recap](https://www.billboard.com/music/rb-hip-hop/ken-carson-rolling-loud-orlando-recap-young-thug-playboi-carti-1236244021/) ·
[Cali 2025 (SoFi Stadium)](https://www.sofistadium.com/news/detail/rolling-loud-california-announces-2025-lineup-headlined-by-aap-rocky-playboi-carti-and-peso-pluma) ·
[Cali 2024 (Billboard)](https://www.billboard.com/music/concerts/rolling-loud-california-2024-lineup-nicki-minaj-post-malone-1235471476/) ·
[Miami 2024 10th anniversary](https://www.hotnewhiphop.com/833591-rolling-loud-10th-anniversary-hip-hop-news) ·
[Miami 2023 (Billboard)](https://www.billboard.com/music/rb-hip-hop/rolling-loud-miami-2023-lineup-1235301709/) ·
[Australia 2026 lineup then cancellation (Billboard)](https://www.billboard.com/music/rb-hip-hop/rolling-loud-australia-2026-lineup-1236120151/) ·
[Rolling Stone AU](https://au.rollingstone.com/music/music-news/rolling-loud-australia-promoters-cancellation-report-91632) ·
[India 2025 debut and 2026 return](https://in.eventfaqs.com/2025/11/25/rolling-loud-india-makes-historic-debut-with-65000-fans-confirms-2026-return-following-landmark-success/) ·
[Founders on the one-US-date strategy (Forbes)](https://www.forbes.com/sites/stevebaltin/2026/01/19/exclusive-rolling-loud-co-founders-on-why-orlando-is-only-us-date-in-2026/) ·
[Orlando 2026 attendance](https://mynews13.com/fl/orlando/news/2026/05/08/thousands-of-fans-in-town-for-rolling-loud-music-festival-this-weekend)

Popularity ranks: [Complex, 100 Hottest Rappers Right Now (September 2026 overhaul)](https://www.complex.com/music/a/dimassanfiorenzo/best-rappers-right-now).
Artist context: [Rod Wave, *Don't Look Down* + tour](https://consequence.net/2026/06/rod-wave-2026-fall-us-tour/) ·
[Yeat, *ADL* + LOVE/LYFE tour](https://www.jambase.com/article/yeat-tour-dates-2026) ·
[Carti, *Baby Boi* status](https://www.billboard.com/music/rb-hip-hop/playboi-carti-baby-boi-album-ready-done-swamp-izzo-1235939620/) ·
[Carti at ComplexCon 2026](https://www.complex.com/music/a/tracewilliamcowen/playboi-carti-complexcon-2026) ·
[Lil Durk acquittal and continued custody](https://www.complex.com/music/a/treyalston/lil-durk-case-behind-bars-after-trial)

---

## Reproducing

```bash
pip install numpy scipy
python predict_rolling_loud.py --paths 200000 --out results_rl
python tests/test_rlsim.py
```

Parameters, with per-artist provenance and reasoning, live in
`params/rolling_loud_editions.json` and `params/rolling_loud_artists.json`.

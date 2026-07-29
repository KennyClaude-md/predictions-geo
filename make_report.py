#!/usr/bin/env python3
"""Render REPORT.md from a completed GEO-SIM run.

Deliberately mechanical: everything here is a projection of results.json, so the
prose in the report that isn't generated is clearly separable from the numbers
that are.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent

DOMAIN_TITLES = {
    "powers": "US–China, Taiwan & the Indo-Pacific",
    "eurasia": "Russia, Ukraine, NATO & Europe",
    "mideast": "Middle East, Iran & proliferation",
    "climate": "Climate system & extreme events",
    "macro": "Global macroeconomy & financial stability",
    "ai_tech": "AI capability, diffusion & cyber/bio risk",
    "demog_health": "Demographics, pandemics & food security",
    "energy_res": "Energy transition & critical resources",
    "governance": "Political regimes, conflict & institutions",
}


def pct(x, dp=1):
    return "—" if x is None else f"{100 * x:.{dp}f}%"


def band(r, h):
    return f"{100 * r[f'ci_lo_{h}']:.1f}–{100 * r[f'ci_hi_{h}']:.1f}%"


def main() -> None:
    res = json.loads((ROOT / "results" / "results.json").read_text())
    m = res["meta"]
    events = res["events"]
    out: list[str] = []
    w = out.append

    w("# The Next Ten Years: A Probabilistic Forecast")
    w("")
    w(f"**Epoch 2026-07-29 → end-2036.** {m['paths']:,} Monte Carlo paths over "
      f"{m['quarters']} quarters, {m['n_indicators']} coupled indicators, "
      f"{m['n_events']} discrete events, {m['n_couplings']} transmission channels, "
      f"{m['n_contagion_rules']} contagion rules, {m['n_stabilizers']} stabilizing feedbacks.")
    w("")
    w("Every percentage below is a model output, not an assertion. Read "
      "[README.md](README.md) for what the model does and, more importantly, for what "
      "it cannot know. The short version: Monte Carlo error bars quantify sampling "
      "noise only, and on thin-reference-class questions the analysts' judgement is "
      "doing far more work than the sampling. The **isolated vs coupled** columns and "
      "the sensitivity table are the honest uncertainty statement.")
    w("")

    # ---- headline ----------------------------------------------------------
    w("## Headline probabilities")
    w("")
    w("`Isolated` is the probability with the domain held apart from the rest of the "
      "world; `Coupled` lets shocks propagate. `Amp` is the odds ratio between them — "
      "how much of this risk arrives through somebody else's crisis.")
    w("")

    by_domain: dict[str, list] = {}
    for e in events:
        by_domain.setdefault(e["domain"], []).append(e)

    for dom in DOMAIN_TITLES:
        rows = sorted(by_domain.get(dom, []), key=lambda r: -r["p_2036"])
        if not rows:
            continue
        w(f"### {DOMAIN_TITLES[dom]}")
        w("")
        w("| Event | by 2027 | by 2030 | by 2036 | 95% CI (2036) | Isolated | Amp |")
        w("|---|---:|---:|---:|---:|---:|---:|")
        for r in rows:
            w(f"| **{r['statement']}** | {pct(r['p_2027'])} | {pct(r['p_2030'])} | "
              f"{pct(r['p_2036'])} | {band(r, '2036')} | {pct(r['p_indep_2036'])} | "
              f"{r['amplification']:.2f}× |")
        w("")

    # ---- amplification -----------------------------------------------------
    w("## Where systemic coupling matters most")
    w("")
    w("Risks whose probability changes most when the world is allowed to interact. "
      "A high amplifier is a risk you will mis-price by thinking about its domain "
      "alone; a low one is a risk that is genuinely self-contained.")
    w("")
    amp = sorted(events, key=lambda r: -r["amplification"])
    w("| Event | Isolated | Coupled | Amp |")
    w("|---|---:|---:|---:|")
    for r in amp[:15]:
        w(f"| {r['statement']} | {pct(r['p_indep_2036'])} | {pct(r['p_2036'])} | "
          f"{r['amplification']:.2f}× |")
    w("")
    w("**Most self-contained** (coupling barely moves them, or damps them):")
    w("")
    w("| Event | Isolated | Coupled | Amp |")
    w("|---|---:|---:|---:|")
    for r in amp[-8:]:
        w(f"| {r['statement']} | {pct(r['p_indep_2036'])} | {pct(r['p_2036'])} | "
          f"{r['amplification']:.2f}× |")
    w("")

    # ---- systemic ----------------------------------------------------------
    s = res["systemic"]
    w("## How rough is the decade?")
    w("")
    w(f"Across {len(s['severe_ids'])} severe shocks — the ones that would define a decade "
      "if they happened — the model gives:")
    w("")
    w("| | Coupled model | If independent |")
    w("|---|---:|---:|")
    w(f"| Expected number by 2036 | **{s['mean_count']:.2f}** | {s['independent_mean']:.2f} |")
    w(f"| P(none at all) | {pct(s['p_zero'])} | — |")
    w(f"| P(at least 1) | **{pct(s['p_at_least_1'])}** | — |")
    w(f"| P(at least 2) | **{pct(s['p_at_least_2'])}** | {pct(s['independent_p_at_least_2'])} |")
    w(f"| P(at least 3) | **{pct(s['p_at_least_3'])}** | {pct(s['independent_p_at_least_3'])} |")
    w(f"| P(at least 4) | {pct(s['p_at_least_4'])} | — |")
    w(f"| 95th percentile count | {s['p95_count']:.0f} | — |")
    w(f"| 99th percentile count | {s['p99_count']:.0f} | — |")
    w("")
    w(f"The excess of {s['clustering_excess_3plus'] * 100:+.1f}pp in P(≥3) over the "
      "independence benchmark is the clustering the coupling produces. Crises arrive "
      "together more often than a list of separate forecasts implies — which is the "
      "single most important thing this model has to say, and the reason a portfolio of "
      "individually-reasonable risk estimates still understates the tail.")
    w("")

    # ---- regimes -----------------------------------------------------------
    w("## Regimes")
    w("")
    w("A slow Markov layer scaling volatility and crisis hazards. `Start` is the "
      "probability the world is in this regime today; `Time share` is expected "
      "occupancy over the decade.")
    w("")
    w("| Regime | Start | Time share | Hazard × | Vol × |")
    w("|---|---:|---:|---:|---:|")
    for r in res["regimes"]:
        w(f"| **{r['name']}** — {r['description']} | {pct(r['initial_probability'], 0)} | "
          f"{pct(r['expected_time_share'], 0)} | {r['hazard_multiplier']:.2f}× | "
          f"{r['vol_multiplier']:.2f}× |")
    w("")

    # ---- scenarios ---------------------------------------------------------
    w("## Emergent scenarios")
    w("")
    w("These are not scenarios anyone wrote down. They are clusters found in the "
      "simulated trajectories themselves — the world-shapes the dynamics actually "
      "produce, with the share of paths that land in each.")
    w("")
    for c in res["scenarios"]["clusters"]:
        w(f"### Cluster {c['id']} — {pct(c['probability'], 1)} of futures")
        w("")
        w(f"Mean severe events: {c['mean_severe_events']:.2f}.")
        w("")
        w("| Distinguishing event | In this world | Overall |")
        w("|---|---:|---:|")
        for e in c["distinguishing_events"][:8]:
            w(f"| {e['id']} | {pct(e['p_in_cluster'])} | {pct(e['p_overall'])} |")
        w("")
        w("| Indicator | Ends at | z |")
        w("|---|---:|---:|")
        for i in c["indicator_profile"][:8]:
            w(f"| {i['label']} | {i['value']:.2f} {i['unit']} | {i['z']:+.2f} |")
        w("")

    # ---- conditionals ------------------------------------------------------
    cm = res["conditional"]
    if cm["ids"]:
        w("## Conditional structure")
        w("")
        w("The strongest conditional dependencies in the run: pairs where one event "
          "occurring multiplies the probability of another. `Lift` is P(A|B) ÷ P(A).")
        w("")
        pairs = []
        for i, a in enumerate(cm["ids"]):
            for j, b in enumerate(cm["ids"]):
                if i == j:
                    continue
                lift = cm["lift"][i][j]
                cond = cm["conditional"][i][j]
                if lift and lift == lift and cond >= 0.02:
                    pairs.append((lift, a, b, cond, cm["marginal"][i]))
        pairs.sort(reverse=True)
        w("| If this happens… | …this becomes | vs baseline | Lift |")
        w("|---|---|---:|---:|")
        for lift, a, b, cond, marg in pairs[:20]:
            w(f"| {b} | {a} → {pct(cond)} | {pct(marg)} | {lift:.2f}× |")
        w("")

    # ---- sensitivity -------------------------------------------------------
    w("## What the answers hang on")
    w("")
    w("Rank correlation between each uncertain input and the number of severe shocks "
      "a path experiences. This is variance attribution, not causation — but it tells "
      "you which assumption to argue with first.")
    w("")
    w("| Driver | Type | Spearman ρ |")
    w("|---|---|---:|")
    for r in res["sensitivity"][:18]:
        w(f"| {r.get('label', r['driver'])} | {r['kind']} | {r['spearman']:+.3f} |")
    w("")

    # ---- indicators --------------------------------------------------------
    w("## Where the measurable quantities end up")
    w("")
    w("Terminal distributions at end-2036, from the coupled run.")
    w("")
    w("| Indicator | Today | p5 | p25 | **median** | p75 | p95 | Unit |")
    w("|---|---:|---:|---:|---:|---:|---:|---|")
    for i in res["indicators_terminal"]:
        w(f"| {i['label']} | {i['start']:.2f} | {i['p5']:.2f} | {i['p25']:.2f} | "
          f"**{i['p50']:.2f}** | {i['p75']:.2f} | {i['p95']:.2f} | {i['unit']} |")
    w("")

    # ---- calibration -------------------------------------------------------
    w("## Calibration audit")
    w("")
    w("Each event's fitted log-hazard offset — how far the engine had to move the "
      "analyst's implied hazard so that the *decoupled* marginal reproduced the "
      "elicited cumulative probability. Large offsets flag events where the analyst's "
      "annual base rate and their cumulative quotes disagreed, or where "
      "state-dependence makes a constant hazard a poor description.")
    w("")
    cal = sorted(res["calibration"], key=lambda r: -abs(r["fitted_offset_log_hazard"]))
    w("| Event | Target P(2036) | Prior hazard/yr | Effective hazard/yr | Offset |")
    w("|---|---:|---:|---:|---:|")
    for r in cal[:15]:
        w(f"| {r['id']} | {pct(r['target_p2036'])} | {r['prior_hazard_annual']:.4f} | "
          f"{r['effective_hazard_annual']:.4f} | {r['fitted_offset_log_hazard']:+.2f} |")
    w("")
    if m["dropped_references"]:
        w(f"<details><summary>{len(m['dropped_references'])} parameter references dropped "
          "as unresolved keys</summary>")
        w("")
        for d in m["dropped_references"]:
            w(f"- `{d}`")
        w("")
        w("</details>")
        w("")

    w("---")
    w("")
    w(f"Run: {m['paths']:,} paths, seed {m['seed']}, {m['runtime_seconds']}s. "
      "Reproduce with `python run_simulation.py`.")

    (ROOT / "REPORT.md").write_text("\n".join(out))
    print(f"wrote REPORT.md ({len(out)} lines)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render the RL-SIM forecast as a festival lineup poster PDF.

    python poster/make_poster.py

Nothing here is typed by hand. Which acts appear comes from the fitted model,
billing order comes from stature blended with probability, and the Friday /
Saturday / Sunday split comes from `rlsim.days` -- whose docstring is worth
reading, because the day split is by far the weakest claim on the page.

A real festival poster tiers by stature rather than by likelihood: an arena act
with a 30% chance of being booked still sits above a club act with a 60% chance.
And a real Rolling Loud bill is ~78 acts, most of them support-tier names nobody
writes headlines about, so a poster built only from famous names would not look
like a Rolling Loud poster at all.

The poster is deliberately and visibly marked as a forecast. A clean pastiche of
a real festival's announcement art is exactly the sort of thing that circulates
detached from its caption, so the disclaimer is part of the layout rather than a
footnote, and the file is handed over rather than published to a URL.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from rlsim.data import load          # noqa: E402
from rlsim.days import DAYS, assign_days   # noqa: E402

POSTER = ROOT / "poster"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

ACCENT = "#FF3B1F"
ACCENT2 = "#FFC400"

DAY_DATES = {"FRIDAY": "MAY 7", "SATURDAY": "MAY 8", "SUNDAY": "MAY 9"}

# Orlando 2026 billed 78 acts. Sizing the predicted bill to the observed bill
# size is more honest than picking a probability threshold and reporting whatever
# number falls out of it.
BILL_SIZE = 78
SUBTIER_A = 8          # names per day set at the larger of the two undercard sizes


# Acts at or above this draw headline or they are not on the bill at all. A
# stadium act does not take a second-line support slot: across every edition in
# the dataset, Travis Scott's three Rolling Loud appearances are three headline
# slots. Billing such an act beneath a smaller name is a configuration that never
# occurs, so the poster must not depict one -- their presence on the bill is
# exactly their probability of headlining it.
HEADLINE_ONLY_DRAW = 0.90


def billing_score(draw: float, p: float) -> float:
    """Stature first, likelihood second. Both are on 0-1 so the sum is commensurate."""
    return 0.65 * draw + 0.35 * p


def build_bill(res, roster):
    hl_p, bill_p = res["headline_prob"], res["bill_prob"]
    by_name = {a["name"]: k for k, a in roster.artists.items()}

    headliners = [by_name[n] for n, _ in
                  sorted(hl_p.items(), key=lambda kv: -kv[1])[:3]]

    rest = [(by_name[n], p) for n, p in bill_p.items()
            if n in by_name and by_name[n] not in headliners
            and roster.artists[by_name[n]]["draw"] < HEADLINE_ONLY_DRAW]
    # Who makes the bill is decided by probability; where they sit on it is
    # decided by stature. Conflating the two would bury the big names.
    rest.sort(key=lambda kv: -kv[1])
    rest = rest[:BILL_SIZE - len(headliners)]
    rest.sort(key=lambda kv: -billing_score(roster.artists[kv[0]]["draw"], kv[1]))
    return headliners, [k for k, _ in rest]


def sep_join(names, cls="sep"):
    """Join names with bullets, keeping real whitespace around the separator.

    Without the spaces there is no break opportunity between spans and the line
    runs straight off the edge of the poster -- names are individually nowrap so
    they never split mid-word, which leaves the gaps as the only place to wrap.
    """
    dot = f' <span class="{cls}">&#9679;</span> '
    return dot.join(f"<span class='nm'>{n.upper()}</span>" for n in names)


def day_block(roster, day, block) -> str:
    hl = roster.artists[block["headliner"]]["name"].upper()
    acts = [roster.artists[k]["name"] for k in block["acts"]]
    a, b = acts[:SUBTIER_A], acts[SUBTIER_A:]
    return f"""
    <section class="day">
      <div class="daylabel"><span>{day}</span><i>{DAY_DATES[day]}</i></div>
      <div class="hl"><div>{hl}</div></div>
      <div class="ta">{sep_join(a)}</div>
      <div class="tb">{sep_join(b)}</div>
    </section>"""


def build_html(res, roster) -> str:
    headliners, undercard = build_bill(res, roster)
    days = assign_days(roster, headliners, undercard)
    total = len(headliners) + len(undercard)

    hl_p, bill_p = res["headline_prob"], res["bill_prob"]
    p_staged = res["p_staged"]
    bt = res["backtest"]["best"]

    rows = "".join(
        f"<tr><td>{n}</td><td class='n'>{p:.0%}</td>"
        f"<td class='n'>{bill_p.get(n, 0):.0%}</td></tr>"
        for n, p in sorted(hl_p.items(), key=lambda kv: -kv[1])[:14]
    )
    bill_rows = "".join(
        f"<tr><td>{n}</td><td class='n'>{p:.0%}</td></tr>"
        for n, p in sorted(bill_p.items(), key=lambda kv: -kv[1])[:28]
    )
    blocks = "".join(day_block(roster, d, days[d]) for d in DAYS)

    return f"""<!doctype html>
<meta charset="utf-8">
<style>
  @font-face {{ font-family:'Anton';   src:url('fonts/Anton.ttf') format('truetype'); }}
  @font-face {{ font-family:'Archivo'; src:url('fonts/ArchivoBlack.ttf') format('truetype'); }}
  @font-face {{ font-family:'Oswald';  src:url('fonts/Oswald-1.ttf') format('truetype'); font-weight:500; }}
  @font-face {{ font-family:'Oswald';  src:url('fonts/Oswald-2.ttf') format('truetype'); font-weight:600; }}
  @font-face {{ font-family:'Oswald';  src:url('fonts/Oswald-3.ttf') format('truetype'); font-weight:700; }}

  @page {{ size: 12in 18in; margin: 0; }}
  * {{ box-sizing:border-box; margin:0; padding:0;
      -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
  body {{ background:#000; color:#fff; font-family:'Oswald',sans-serif; }}

  .page {{
    width:12in; height:18in; position:relative; overflow:hidden;
    display:flex; flex-direction:column; page-break-after:always;
    background:radial-gradient(125% 62% at 50% 0%, #2c0e06 0%, #0a0503 46%, #000 100%);
  }}
  .page:last-child {{ page-break-after:auto; }}
  .grain {{ position:absolute; inset:0; opacity:.05; pointer-events:none;
    background-image:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 3px),
                     repeating-linear-gradient(90deg,#fff 0 1px,transparent 1px 3px); }}

  .strip {{ background:{ACCENT}; color:#000; font-weight:700; letter-spacing:.20em;
    font-size:12.5px; text-align:center; padding:8px 0; text-transform:uppercase;
    position:relative; z-index:3; flex:none; }}
  .strip.bottom {{ background:{ACCENT2}; }}

  .head {{ flex:none; padding:14px 50px 0; position:relative; z-index:2; text-align:center; }}
  .wordmark {{ font-family:'Archivo',sans-serif; line-height:.84;
    letter-spacing:-.024em; text-transform:uppercase; }}
  .wordmark span {{ display:block; font-size:104px; transform:scaleX(1.07); }}
  .edition {{ font-family:'Anton',sans-serif; color:{ACCENT}; font-size:44px;
    letter-spacing:.07em; margin-top:6px; line-height:1; }}
  .datebar {{ margin-top:10px; font-weight:600; letter-spacing:.15em; font-size:16px;
    text-transform:uppercase; border-top:3px solid #fff; border-bottom:3px solid #fff;
    padding:8px 0; }}
  .datebar .dot {{ color:{ACCENT}; margin:0 10px; }}

  .body {{ flex:1; min-height:0; display:flex; flex-direction:column;
    justify-content:space-evenly; padding:6px 46px 0; position:relative; z-index:2;
    text-align:center; }}

  .day + .day {{ margin-top:4px; }}
  .daylabel {{ display:flex; align-items:center; justify-content:center; gap:14px;
    margin-bottom:4px; }}
  .daylabel::before, .daylabel::after {{ content:""; flex:1; height:2px; background:#3d3d3d; }}
  .daylabel span {{ font-family:'Anton',sans-serif; font-size:30px; letter-spacing:.14em;
    color:{ACCENT2}; text-transform:uppercase; }}
  .daylabel i {{ font-style:normal; font-weight:600; font-size:14px; letter-spacing:.16em;
    color:#8f8f8f; }}

  .hl {{ font-family:'Anton',sans-serif; text-transform:uppercase; font-size:80px;
    line-height:1.02; letter-spacing:.005em; }}
  .hl div {{ transform:scaleX(.95); }}

  .ta {{ font-family:'Anton',sans-serif; text-transform:uppercase; font-size:35px;
    line-height:1.22; letter-spacing:.012em; margin-top:10px; }}
  .tb {{ font-weight:600; text-transform:uppercase; font-size:17px; line-height:1.5;
    letter-spacing:.045em; margin-top:10px; color:#dcdcdc; }}

  /* names must never break across a line -- that is the tell of a fake poster */
  .nm {{ white-space:nowrap; }}
  .sep {{ color:{ACCENT}; margin:0 .40em; font-size:.55em; vertical-align:.22em; }}
  .ta .sep {{ font-size:.42em; vertical-align:.28em; }}

  .credits {{ flex:none; text-align:center; font-size:11.5px; letter-spacing:.10em;
    font-weight:500; color:#8a8a8a; text-transform:uppercase; padding:8px 50px 7px;
    line-height:1.58; position:relative; z-index:3; }}
  .credits b {{ color:#d6d6d6; font-weight:700; }}

  /* ---- page 2 ---- */
  .p2 {{ padding:60px 74px; position:relative; z-index:2; }}
  .p2 h1 {{ font-family:'Anton',sans-serif; font-size:54px; text-transform:uppercase;
    letter-spacing:.02em; line-height:1.03; }}
  .p2 h1 span {{ color:{ACCENT}; }}
  .p2 .sub {{ color:#9a9a9a; font-size:14.5px; letter-spacing:.05em; margin-top:13px;
    line-height:1.66; font-weight:500; }}
  .p2 h2 {{ font-family:'Anton',sans-serif; font-size:24px; text-transform:uppercase;
    letter-spacing:.05em; margin:32px 0 11px; color:{ACCENT2}; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; font-weight:500; }}
  th {{ text-align:left; font-size:11px; letter-spacing:.13em; color:#8a8a8a;
    text-transform:uppercase; padding:0 0 7px; border-bottom:2px solid #333; font-weight:700; }}
  td {{ padding:5.4px 0; border-bottom:1px solid #1d1d1d; }}
  td.n, th.n {{ text-align:right; font-variant-numeric:tabular-nums; }}
  .two {{ display:flex; gap:40px; }} .two > div {{ flex:1; }}
  .cap {{ font-size:11.5px; color:#8f8f8f; line-height:1.55; margin:-4px 0 11px;
    font-weight:500; }}
  .note {{ margin-top:24px; font-size:12.5px; color:#9a9a9a; line-height:1.7; font-weight:500; }}
  .note b {{ color:#e4e4e4; }}
</style>

<div class="page">
  <div class="grain"></div>
  <div class="strip">Forecast &#9679; not an official Rolling Loud announcement</div>
  <div class="head">
    <div class="wordmark"><span>Rolling</span><span>Loud</span></div>
    <div class="edition">Florida 2027</div>
    <div class="datebar">Camping World Stadium
      <span class="dot">&#9679;</span> Orlando, FL
      <span class="dot">&#9679;</span> May 7&#8211;9, 2027</div>
  </div>
  <div class="body">{blocks}</div>
  <div class="credits">
    Predicted bill &#9679; <b>{total} acts</b> &#9679; a full Rolling Loud runs ~78<br>
    Generated by <b>RL-SIM</b> from information as of <b>16 Sep 2026</b>
    &#9679; {int(round(p_staged*100))}% the edition is staged as announced<br>
    Day splits are the least certain part of this &#9679; the real lineup lands early Jan 2027
  </div>
  <div class="strip bottom">This is a statistical prediction &#9679; no affiliation with Rolling Loud</div>
</div>

<div class="page">
  <div class="grain"></div>
  <div class="p2">
    <h1>The numbers<br><span>behind the poster</span></h1>
    <div class="sub">
      A Plackett&#8211;Luce conditional logit fitted to the 18 headline bookings across the six
      US flagship editions staged since 2023, plus a logistic persistence model for the
      undercard. Feature set and regularisation chosen by held-out likelihood, then
      integrated forward over coefficient uncertainty and per-artist availability,
      200,000 paths.<br>
      Leave-one-edition-out the headline model names <b style="color:#fff">{bt['hit_rate']:.1%}</b>
      of held-out slates, against {bt['heat_only_hit_rate']:.1%} for ranking on popularity
      alone, {bt['repeat_last_hit_rate']:.1%} for rebooking the previous edition and
      {bt['random_hit_rate']:.1%} for a uniform draw from the pool.
    </div>

    <div class="two">
      <div>
        <h2>Headline slot</h2>
        <table>
          <tr><th>Artist</th><th class="n">Headline</th><th class="n">Any slot</th></tr>
          {rows}
        </table>
      </div>
      <div>
        <h2>Anywhere on the bill</h2>
        <div class="cap">Support-tier acts outrank marquee names here, and that is the
        model working rather than failing: Rolling Loud recycles its deep bill and rotates
        its top of it. The fitted undercard coefficient on draw is &#8722;4.05.</div>
        <table>
          <tr><th>Artist</th><th class="n">P</th></tr>
          {bill_rows}
        </table>
      </div>
    </div>

    <div class="note">
      <b>Read this as a forecast, not a leak.</b> All probabilities are conditional on the
      edition being staged; multiply by {p_staged:.2f} for unconditional odds. The model is
      fitted to eighteen headline bookings, so coefficient uncertainty is wide, and because
      popularity ranks for pre-2026 editions were assigned retrospectively the backtest above
      is an optimistic bound on out-of-sample skill rather than an estimate of it.<br><br>
      <b>Acts drawing at stadium scale headline or do not appear.</b> Travis Scott,
      Drake and Kendrick Lamar are all live candidates for a headline slot &#8212; Travis at
      18%, Drake at 12% &#8212; but none of them takes a second-line support billing, so
      when they miss the top three they leave the bill entirely rather than sliding down it.
      Their probability of being on this poster just is their probability of closing a
      night.<br><br>
      <b>The day splits are the weakest claim on the poster.</b> Full headline day-splits are
      recoverable for two editions and one undercard fragment, which is not enough to fit
      anything, so they follow an explicit rule: Saturday takes the biggest draw (true of
      both editions where the split is known), and each day clusters around its headliner's
      lane (visible in Orlando 2026, where NBA YoungBoy's Sunday carried Sexyy Red, OsamaSon,
      Che and Skrilla). Treat who is on the bill as the forecast and which day they play as
      an educated arrangement.<br><br>
      Where I would bet against the model: <b>Don Toliver</b> is too high (it expects 45% of
      slots to go to a 2026 headliner against a 29% historical base rate), <b>Drake</b> is too
      high (eleven years of declining this festival is not a feature the model can see), and
      <b>Sexyy Red</b> is too low (two usable transitions cannot identify an unbroken streak).
      <b>Lil Durk</b> is the wildcard: acquitted 11 Sep 2026 but held for a racketeering trial
      from 5 Oct. Full write-up in ROLLING_LOUD_2027.md.
    </div>
  </div>
</div>
"""


def main() -> None:
    res = json.loads((ROOT / "results_rl" / "rl2027.json").read_text())
    roster = load()
    html = build_html(res, roster)
    (POSTER / "poster.html").write_text(html)

    out = POSTER / "Rolling_Loud_Florida_2027_RL-SIM_forecast.pdf"
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
         "--no-pdf-header-footer", "--virtual-time-budget=10000",
         f"--print-to-pdf={out}", (POSTER / "poster.html").as_uri()],
        check=True, capture_output=True,
    )

    headliners, undercard = build_bill(res, roster)
    days = assign_days(roster, headliners, undercard)
    for d in DAYS:
        b = days[d]
        print(f"{d:9s} {roster.artists[b['headliner']]['name'].upper()}  "
              f"(+{len(b['acts'])} acts)")
    print(f"\ntotal billed: {len(headliners) + len(undercard)}")
    print(f"wrote {out}  ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()

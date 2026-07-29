#!/usr/bin/env python3
"""Render the GEO-SIM results as a self-contained HTML page.

All SVG is generated here rather than by a charting library, because the page
has to be fully self-contained (no CDN) and theme-aware in both directions.
Colours come from the validated default data-viz palette; every chart is
declared against CSS custom properties so light/dark swap in one place.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).parent

# ---- palette (validated default instance) --------------------------------- #
L = {"surface": "#fcfcfb", "page": "#f9f9f7", "ink": "#0b0b0b", "ink2": "#52514e",
     "muted": "#898781", "grid": "#e1e0d9", "axis": "#c3c2b7", "s1": "#2a78d6",
     "s2": "#eb6834", "s3": "#1baf7a", "crit": "#d03b3b", "warn": "#fab219",
     "good": "#006300", "border": "rgba(11,11,11,0.10)", "wash": "rgba(42,120,214,0.10)"}
D = {"surface": "#1a1a19", "page": "#0d0d0d", "ink": "#ffffff", "ink2": "#c3c2b7",
     "muted": "#898781", "grid": "#2c2c2a", "axis": "#383835", "s1": "#3987e5",
     "s2": "#d95926", "s3": "#199e70", "crit": "#d03b3b", "warn": "#fab219",
     "good": "#0ca30c", "border": "rgba(255,255,255,0.10)", "wash": "rgba(57,135,229,0.16)"}
SEQ = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
       "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]

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

# Indicators worth a fan chart. Missing keys are skipped silently, so this can
# stay aspirational without breaking when a domain names things differently.
FAN_KEYS = [
    "gmst_anomaly_c", "global_gdp_growth", "brent_oil_usd", "us_china_tension_index",
    "ai_capability_index", "battle_deaths_annual", "global_democracy_index",
    "co2_ppm", "us_debt_to_gdp", "russia_nato_tension_index", "food_price_index",
    "global_displacement_millions",
]

E = html.escape


def fmt_pct(x, dp=0):
    return "—" if x is None else f"{100 * x:.{dp}f}%"


def sig(x, n=3):
    if x is None:
        return "—"
    a = abs(x)
    if a >= 100:
        return f"{x:,.0f}"
    if a >= 10:
        return f"{x:.1f}"
    if a >= 1:
        return f"{x:.2f}"
    return f"{x:.3f}"


# --------------------------------------------------------------------------- #
# chart builders — each returns an <svg> string
# --------------------------------------------------------------------------- #
def bar_probabilities(rows, width=760, row_h=30, pad_l=330):
    """Horizontal bars with 95% CI whiskers. One measure, so one colour."""
    h = len(rows) * row_h + 34
    inner = width - pad_l - 60
    mx = max([r["p_2036"] for r in rows] + [0.05])
    mx = min(1.0, mx * 1.18)
    out = [f'<svg viewBox="0 0 {width} {h}" role="img" class="chart">']

    for gx in range(5):
        v = mx * gx / 4
        x = pad_l + inner * gx / 4
        out.append(f'<line x1="{x:.1f}" y1="16" x2="{x:.1f}" y2="{h - 20}" '
                   f'stroke="var(--grid)" stroke-width="1"/>')
        out.append(f'<text x="{x:.1f}" y="{h - 6}" class="tick" text-anchor="middle">'
                   f'{100 * v:.0f}%</text>')

    for i, r in enumerate(rows):
        y = 20 + i * row_h
        w = inner * r["p_2036"] / mx
        lo = inner * r["ci_lo_2036"] / mx
        hi = inner * r["ci_hi_2036"] / mx
        tip = (f"{r['statement']}&#10;&#10;by 2027: {fmt_pct(r['p_2027'], 1)}&#10;"
               f"by 2030: {fmt_pct(r['p_2030'], 1)}&#10;by 2036: {fmt_pct(r['p_2036'], 1)} "
               f"(95% CI {fmt_pct(r['ci_lo_2036'], 1)}–{fmt_pct(r['ci_hi_2036'], 1)})&#10;"
               f"isolated: {fmt_pct(r['p_indep_2036'], 1)} · amplification {r['amplification']:.2f}x")
        label = r["statement"]
        label = label if len(label) <= 52 else label[:50] + "…"
        out.append(f'<g class="hit" data-tip="{E(tip)}">')
        out.append(f'<rect x="0" y="{y - 9}" width="{width}" height="{row_h - 2}" fill="transparent"/>')
        out.append(f'<text x="{pad_l - 12}" y="{y + 5}" class="lab" text-anchor="end">{E(label)}</text>')
        out.append(f'<rect x="{pad_l}" y="{y - 5}" width="{max(w, 1.5):.1f}" height="11" rx="4" '
                   f'fill="var(--s1)"/>')
        # The whisker rides on top of the bar with end caps. Drawn as a bare
        # line at the bar's centre it would be swallowed by the fill for its
        # whole lower half and read as if the interval were one-sided.
        if hi - lo > 1.5:
            out.append(f'<g stroke="var(--ink)" stroke-width="1.4" opacity="0.5">'
                       f'<line x1="{pad_l + lo:.1f}" y1="{y + 0.5}" x2="{pad_l + hi:.1f}" '
                       f'y2="{y + 0.5}"/>'
                       f'<line x1="{pad_l + lo:.1f}" y1="{y - 4}" x2="{pad_l + lo:.1f}" '
                       f'y2="{y + 5}"/>'
                       f'<line x1="{pad_l + hi:.1f}" y1="{y - 4}" x2="{pad_l + hi:.1f}" '
                       f'y2="{y + 5}"/></g>')
        out.append(f'<text x="{pad_l + max(w, 1.5) + 8:.1f}" y="{y + 5}" class="val">'
                   f'{fmt_pct(r["p_2036"], 1)}</text>')
        out.append("</g>")
    out.append("</svg>")
    return "".join(out)


def dumbbell(rows, width=760, row_h=32, pad_l=330):
    """Isolated vs coupled probability. Two series, so legend + direct labels."""
    h = len(rows) * row_h + 34
    inner = width - pad_l - 80
    mx = max([max(r["p_2036"], r["p_indep_2036"]) for r in rows] + [0.05]) * 1.15
    mx = min(mx, 1.0)
    out = [f'<svg viewBox="0 0 {width} {h}" role="img" class="chart">']
    for gx in range(5):
        x = pad_l + inner * gx / 4
        out.append(f'<line x1="{x:.1f}" y1="14" x2="{x:.1f}" y2="{h - 20}" '
                   f'stroke="var(--grid)" stroke-width="1"/>')
        out.append(f'<text x="{x:.1f}" y="{h - 6}" class="tick" text-anchor="middle">'
                   f'{100 * mx * gx / 4:.0f}%</text>')
    for i, r in enumerate(rows):
        y = 22 + i * row_h
        xa = pad_l + inner * r["p_indep_2036"] / mx
        xb = pad_l + inner * r["p_2036"] / mx
        label = r["statement"]
        label = label if len(label) <= 52 else label[:50] + "…"
        tip = (f"{r['statement']}&#10;&#10;isolated: {fmt_pct(r['p_indep_2036'], 1)}&#10;"
               f"coupled: {fmt_pct(r['p_2036'], 1)}&#10;"
               f"amplification: {r['amplification']:.2f}x odds")
        out.append(f'<g class="hit" data-tip="{E(tip)}">')
        out.append(f'<rect x="0" y="{y - 11}" width="{width}" height="{row_h - 2}" fill="transparent"/>')
        out.append(f'<text x="{pad_l - 12}" y="{y + 4}" class="lab" text-anchor="end">{E(label)}</text>')
        out.append(f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" stroke="var(--axis)" '
                   f'stroke-width="2"/>')
        out.append(f'<circle cx="{xa:.1f}" cy="{y}" r="5" fill="var(--s2)" '
                   f'stroke="var(--surface)" stroke-width="2"/>')
        out.append(f'<circle cx="{xb:.1f}" cy="{y}" r="5" fill="var(--s1)" '
                   f'stroke="var(--surface)" stroke-width="2"/>')
        out.append(f'<text x="{max(xa, xb) + 12:.1f}" y="{y + 4}" class="val">'
                   f'{r["amplification"]:.1f}×</text>')
        out.append("</g>")
    out.append("</svg>")
    return "".join(out)


def grouped_counts(coupled, independent, width=760, height=260, cap=9):
    """Shock-count distribution: coupled model vs independence benchmark."""
    # Pad to a floor so a run where almost nothing fires does not render two
    # page-wide slabs; trim trailing empty bins so a long sparse tail does not
    # squash the occupied ones.
    occupied = max([i for i, v in enumerate(coupled) if v] or [0],
                   default=0)
    n = max(min(cap, len(coupled), occupied + 2), 5)
    c = (coupled + [0] * n)[:n]
    ind = (independent + [0] * n)[:n]
    mx = max(max(c), max(ind)) or 1
    total = sum(coupled) or 1
    pad_l, pad_b, pad_t = 44, 40, 14
    iw = width - pad_l - 16
    ih = height - pad_b - pad_t
    bw = iw / n
    out = [f'<svg viewBox="0 0 {width} {height}" role="img" class="chart">']
    for gy in range(5):
        y = pad_t + ih * gy / 4
        v = mx * (1 - gy / 4) / total
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - 16}" y2="{y:.1f}" '
                   f'stroke="var(--grid)" stroke-width="1"/>')
        out.append(f'<text x="{pad_l - 8}" y="{y + 4:.1f}" class="tick" text-anchor="end">'
                   f'{100 * v:.0f}%</text>')
    for i in range(n):
        x0 = pad_l + i * bw
        for k, (vals, col, name) in enumerate(((c, "var(--s1)", "coupled model"),
                                               (ind, "var(--s2)", "if independent"))):
            v = vals[i] / total
            bh = ih * (vals[i] / mx)
            # 2px surface gap between adjacent bars, not a stroke.
            x = x0 + 6 + k * (bw - 14) / 2
            w = (bw - 14) / 2 - 2
            tip = f"{i} severe shocks&#10;{name}: {100 * v:.1f}%"
            out.append(f'<g class="hit" data-tip="{E(tip)}">'
                       f'<rect x="{x:.1f}" y="{pad_t + ih - bh:.1f}" width="{max(w, 2):.1f}" '
                       f'height="{max(bh, 1):.1f}" rx="3" fill="{col}"/></g>')
        out.append(f'<text x="{x0 + bw / 2:.1f}" y="{height - 20}" class="tick" '
                   f'text-anchor="middle">{i}</text>')
    out.append(f'<text x="{width / 2:.0f}" y="{height - 4}" class="tick" text-anchor="middle">'
               f'number of severe shocks by 2036</text>')
    out.append("</svg>")
    return "".join(out)


def timelines(series, width=760, height=300):
    """Cumulative probability curves. Max 5 series, all direct-labelled."""
    pad_l, pad_r, pad_b, pad_t = 44, 150, 34, 14
    iw = width - pad_l - pad_r
    ih = height - pad_b - pad_t
    mx = max(max(s["values"]) for s in series) * 1.12
    mx = min(mx, 1.0)
    q = len(series[0]["values"])
    cols = ["var(--s1)", "var(--s2)", "var(--s3)", "var(--seq-yellow)", "var(--s5)"]
    out = [f'<svg viewBox="0 0 {width} {height}" role="img" class="chart">']
    for gy in range(5):
        y = pad_t + ih * gy / 4
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{pad_l + iw}" y2="{y:.1f}" '
                   f'stroke="var(--grid)" stroke-width="1"/>')
        out.append(f'<text x="{pad_l - 8}" y="{y + 4:.1f}" class="tick" text-anchor="end">'
                   f'{100 * mx * (1 - gy / 4):.0f}%</text>')
    for yr in range(2027, 2037, 2):
        qi = (yr - 2026) * 4 - 2
        if 0 <= qi < q:
            x = pad_l + iw * qi / (q - 1)
            out.append(f'<text x="{x:.1f}" y="{height - 14}" class="tick" '
                       f'text-anchor="middle">{yr}</text>')
    for i, s in enumerate(series):
        pts = " ".join(f"{pad_l + iw * k / (q - 1):.1f},{pad_t + ih * (1 - v / mx):.1f}"
                       for k, v in enumerate(s["values"]))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{cols[i]}" stroke-width="2" '
                   f'stroke-linejoin="round"/>')
        ey = pad_t + ih * (1 - s["values"][-1] / mx)
        lab = s["label"] if len(s["label"]) <= 22 else s["label"][:21] + "…"
        out.append(f'<circle cx="{pad_l + iw:.1f}" cy="{ey:.1f}" r="3.5" fill="{cols[i]}"/>')
        out.append(f'<text x="{pad_l + iw + 10:.1f}" y="{ey + 4:.1f}" class="endlab">'
                   f'{E(lab)} {fmt_pct(s["values"][-1])}</text>')
    out.append("</svg>")
    return "".join(out)


def fan(fkey, f, width=360, height=170):
    """Percentile bands for one indicator. One hue, light→dark by centrality."""
    p = f["percentiles"]
    q = len(p["50"])
    lo, hi = min(p["5"]), max(p["95"])
    span = (hi - lo) or 1
    lo -= span * 0.08
    hi += span * 0.08
    span = hi - lo
    pad_l, pad_b, pad_t, pad_r = 46, 26, 12, 10
    iw = width - pad_l - pad_r
    ih = height - pad_b - pad_t

    def X(i):
        return pad_l + iw * i / (q - 1)

    def Y(v):
        return pad_t + ih * (1 - (v - lo) / span)

    def band(a, b, fill, op):
        up = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(p[a]))
        dn = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in reversed(list(enumerate(p[b]))))
        return f'<polygon points="{up} {dn}" fill="{fill}" opacity="{op}"/>'

    out = [f'<svg viewBox="0 0 {width} {height}" role="img" class="chart">']
    for gy in range(4):
        y = pad_t + ih * gy / 3
        v = hi - span * gy / 3
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - pad_r}" y2="{y:.1f}" '
                   f'stroke="var(--grid)" stroke-width="1"/>')
        out.append(f'<text x="{pad_l - 6}" y="{y + 4:.1f}" class="tick" text-anchor="end">'
                   f'{sig(v)}</text>')
    out.append(band("5", "95", SEQ[2], 0.55))
    out.append(band("25", "75", SEQ[5], 0.65))
    med = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(p["50"]))
    out.append(f'<polyline points="{med}" fill="none" stroke="{SEQ[9]}" stroke-width="2"/>')
    for yr in (2029, 2032, 2036):
        qi = (yr - 2026) * 4 - 2
        if 0 <= qi < q:
            out.append(f'<text x="{X(qi):.1f}" y="{height - 8}" class="tick" '
                       f'text-anchor="middle">{yr}</text>')
    tip = (f"{f['label']} ({f['unit']})&#10;today: {sig(f['start'])}&#10;"
           f"2036 median: {sig(p['50'][-1])}&#10;"
           f"2036 90% range: {sig(p['5'][-1])} – {sig(p['95'][-1])}&#10;"
           f"source: {f.get('source', '')}")
    out.append(f'<rect class="hit" data-tip="{E(tip)}" x="0" y="0" width="{width}" '
               f'height="{height}" fill="transparent"/>')
    out.append("</svg>")
    return "".join(out)


def sensitivity_bars(rows, width=760, row_h=26, pad_l=300):
    """Signed rank correlations — diverging about zero."""
    h = len(rows) * row_h + 30
    inner = width - pad_l - 70
    mx = max(abs(r["spearman"]) for r in rows) * 1.15 or 0.1
    zero = pad_l + inner / 2
    out = [f'<svg viewBox="0 0 {width} {h}" role="img" class="chart">']
    out.append(f'<line x1="{zero}" y1="10" x2="{zero}" y2="{h - 22}" stroke="var(--axis)" '
               f'stroke-width="1"/>')
    for i, r in enumerate(rows):
        y = 18 + i * row_h
        v = r["spearman"]
        w = (inner / 2) * abs(v) / mx
        x = zero if v >= 0 else zero - w
        col = "var(--s1)" if v >= 0 else "var(--crit)"
        lab = r.get("label") or r["driver"]
        lab = lab if len(lab) <= 46 else lab[:45] + "…"
        tip = f"{lab}&#10;{r['kind']}&#10;Spearman rho = {v:+.3f}"
        out.append(f'<g class="hit" data-tip="{E(tip)}">')
        out.append(f'<rect x="0" y="{y - 9}" width="{width}" height="{row_h - 2}" fill="transparent"/>')
        out.append(f'<text x="{pad_l - 12}" y="{y + 4}" class="lab" text-anchor="end">{E(lab)}</text>')
        out.append(f'<rect x="{x:.1f}" y="{y - 5}" width="{max(w, 1.5):.1f}" height="10" rx="3" '
                   f'fill="{col}"/>')
        tx = (x + w + 8) if v >= 0 else (x - 8)
        anc = "start" if v >= 0 else "end"
        out.append(f'<text x="{tx:.1f}" y="{y + 4}" class="val" text-anchor="{anc}">{v:+.2f}</text>')
        out.append("</g>")
    out.append(f'<text x="{zero}" y="{h - 6}" class="tick" text-anchor="middle">'
               f'← fewer shocks   ·   more shocks →</text>')
    out.append("</svg>")
    return "".join(out)


# --------------------------------------------------------------------------- #
def build(res: dict, fans: dict) -> str:
    m = res["meta"]
    events = res["events"]
    sysm = res["systemic"]
    ev_by_id = {e["id"]: e for e in events}

    def css(v):
        return "\n".join(f"    --{k}: {val};" for k, val in v.items())

    parts = ["<title>The Next Ten Years — GEO-SIM</title>", "<style>", ":root{color-scheme:light dark}",
             ".geo{", css(L), "  --seq-yellow:#eda100;  --s5:#e87ba4;", "}",
             '@media (prefers-color-scheme: dark){:root:where(:not([data-theme="light"])) .geo{',
             css(D), "  --seq-yellow:#c98500;  --s5:#d55181;", "}}",
             ':root[data-theme="dark"] .geo{', css(D),
             "  --seq-yellow:#c98500;  --s5:#d55181;", "}"]
    parts.append("""
.geo{background:var(--page);color:var(--ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;
 line-height:1.55;margin:0;padding:0 20px 80px;-webkit-font-smoothing:antialiased}
.geo .wrap{max-width:860px;margin:0 auto}
.geo h1{font-size:clamp(28px,5vw,44px);line-height:1.1;letter-spacing:-0.02em;margin:48px 0 12px;font-weight:640}
.geo h2{font-size:clamp(20px,3vw,27px);letter-spacing:-0.01em;margin:64px 0 6px;font-weight:620}
.geo h3{font-size:16px;margin:32px 0 4px;font-weight:620}
.geo h4{font-size:13.5px;margin:20px 0 4px;font-weight:620;color:var(--ink2);
 text-transform:uppercase;letter-spacing:0.06em}
.geo p{color:var(--ink2);margin:10px 0;font-size:15.5px}
.geo .lede{font-size:18px;color:var(--ink2);margin:16px 0 8px}
.geo .meta{font-size:13px;color:var(--muted);margin:8px 0 0}
.geo .card{background:var(--surface);border:1px solid var(--border);border-radius:14px;
 padding:20px 22px;margin:18px 0}
.geo .scroll{overflow-x:auto;overflow-y:hidden}
.geo svg.chart{display:block;width:100%;height:auto;min-width:520px}
.geo .tick{font-size:11px;fill:var(--muted)}
.geo .lab{font-size:12.5px;fill:var(--ink2)}
.geo .val{font-size:12.5px;fill:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.geo .endlab{font-size:11.5px;fill:var(--ink2)}
.geo .hit{cursor:default}
.geo .hit:hover rect[fill="transparent"]{fill:var(--wash)}
.geo .tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}
.geo .tile{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 16px}
.geo .tile .n{font-size:30px;font-weight:660;letter-spacing:-0.02em;line-height:1.15}
.geo .tile .k{font-size:12px;color:var(--muted);margin-top:2px}
.geo .hero{font-size:clamp(56px,12vw,104px);font-weight:680;letter-spacing:-0.04em;line-height:1;
 margin:8px 0 2px}
.geo .legend{display:flex;flex-wrap:wrap;gap:16px;margin:12px 0 4px;font-size:12.5px;color:var(--ink2)}
.geo .legend i{width:11px;height:11px;border-radius:3px;display:inline-block;margin-right:6px;
 vertical-align:-1px}
.geo table{border-collapse:collapse;width:100%;font-size:13px;margin:12px 0}
.geo th{text-align:left;font-weight:620;color:var(--ink2);border-bottom:1px solid var(--axis);
 padding:7px 10px 7px 0;font-size:11.5px;text-transform:uppercase;letter-spacing:0.05em}
.geo td{padding:7px 10px 7px 0;border-bottom:1px solid var(--grid);color:var(--ink2);
 vertical-align:top}
.geo td.n{text-align:right;font-variant-numeric:tabular-nums;color:var(--ink);white-space:nowrap}
.geo .fans{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.geo .fan h4{margin:0 0 2px}
.geo .fan .u{font-size:11.5px;color:var(--muted);margin:0 0 6px}
.geo .sc{border-left:3px solid var(--s1);padding-left:16px;margin:22px 0}
.geo .sc .p{font-size:24px;font-weight:660;letter-spacing:-0.02em}
.geo details{margin:10px 0;font-size:14px;color:var(--ink2)}
.geo summary{cursor:pointer;font-weight:600;color:var(--ink);font-size:14px;padding:4px 0}
.geo code{font-size:12.5px;background:var(--surface);padding:1px 5px;border-radius:4px;
 border:1px solid var(--border)}
.geo .warn{border-left:3px solid var(--warn);padding:2px 0 2px 16px;margin:18px 0}
#geo-tip{position:fixed;z-index:99;pointer-events:none;opacity:0;transition:opacity .1s;
 background:var(--surface);color:var(--ink);border:1px solid var(--border);border-radius:9px;
 padding:9px 12px;font-size:12.5px;line-height:1.45;white-space:pre-line;max-width:330px;
 box-shadow:0 6px 22px rgba(0,0,0,.16);font-family:system-ui,sans-serif}
</style>""")

    parts.append('<div class="geo"><div class="wrap">')
    W = parts.append

    # ---- header ----
    W("<h1>The next ten years</h1>")
    W(f'<p class="lede">A coupled Monte Carlo simulation of {m["n_indicators"]} world indicators '
      f'and {m["n_events"]} discrete events, run {m["paths"]:,} times from today to end-2036.</p>')
    W(f'<p class="meta">Epoch 2026-07-29 · {m["quarters"]} quarterly steps · '
      f'{m["n_couplings"]} transmission channels · {m["n_contagion_rules"]} contagion rules · '
      f'{m["n_stabilizers"]} stabilizing feedbacks · seed {m["seed"]}</p>')

    W('<div class="warn"><p><strong>Read this first.</strong> Every number here is a model '
      'output, not a claim about the world. The error bars quantify Monte Carlo sampling noise '
      'only — on questions with thin historical reference classes, the analysts\' judgement is '
      'doing far more work than the sampling, and the honest uncertainty is much wider than the '
      'intervals shown. The <em>isolated vs coupled</em> comparison and the sensitivity ranking '
      'are the parts most worth trusting; any single headline percentage is the part least '
      'worth trusting.</p></div>')

    # ---- hero ----
    W("<h2>How rough is the decade?</h2>")
    W(f'<p>Across the {len(sysm["severe_ids"])} shocks severe enough to define a decade — '
      "great-power conflict, nuclear proliferation, systemic financial crisis, pandemic, "
      "state collapse — the model says at least one lands with probability</p>")
    W(f'<div class="hero">{fmt_pct(sysm["p_at_least_1"], 1)}</div>')
    W(f'<p class="meta">Expected count {sysm["mean_count"]:.2f}. '
      f'P(three or more) {fmt_pct(sysm["p_at_least_3"], 1)}, versus '
      f'{fmt_pct(sysm["independent_p_at_least_3"], 1)} if these risks were independent.</p>')

    W('<div class="tiles">')
    for n, k in ((fmt_pct(sysm["p_zero"], 1), "no severe shock at all"),
                 (fmt_pct(sysm["p_at_least_2"], 1), "two or more"),
                 (fmt_pct(sysm["p_at_least_4"], 1), "four or more"),
                 (f'{sysm["p99_count"]:.0f}', "99th-percentile count")):
        W(f'<div class="tile"><div class="n">{n}</div><div class="k">{k}</div></div>')
    W("</div>")

    W('<div class="card"><div class="legend">'
      '<span><i style="background:var(--s1)"></i>coupled model</span>'
      '<span><i style="background:var(--s2)"></i>if risks were independent</span></div>'
      '<div class="scroll">')
    W(grouped_counts(sysm["count_distribution"], sysm["count_distribution_independent"]))
    W("</div></div>")

    excess = sysm["clustering_excess_3plus"] * 100
    W(f"<p>The gap between the two distributions is the whole point of building a coupled model. "
      f"Treating each risk as its own independent forecast understates P(three or more severe "
      f"shocks) by <strong>{excess:+.1f} percentage points</strong>. Crises are not independent "
      f"draws: they share drivers, they propagate through markets and alliances, and they arrive "
      f"in clusters. A portfolio of individually-reasonable risk estimates still misprices the "
      f"tail, and it misprices it in the direction that hurts.</p>")

    # ---- headline probabilities ----
    W("<h2>Headline probabilities</h2>")
    W("<p>Probability that each event occurs at least once between now and end-2036. Bars show "
      "the coupled model; the thin whisker is the 95% Monte Carlo interval. Hover any row for "
      "the 2027 and 2030 figures and the isolated comparison.</p>")

    by_dom: dict[str, list] = {}
    for e in events:
        by_dom.setdefault(e["domain"], []).append(e)
    for dom, title in DOMAIN_TITLES.items():
        rows = sorted(by_dom.get(dom, []), key=lambda r: -r["p_2036"])
        if not rows:
            continue
        W(f"<h3>{E(title)}</h3>")
        W('<div class="card"><div class="scroll">')
        W(bar_probabilities(rows))
        W("</div></div>")

    # ---- amplification ----
    W("<h2>Which risks arrive through other people's crises</h2>")
    W("<p>Each row runs from the probability with its domain held in isolation to the probability "
      "once the world is allowed to interact. The multiplier is the odds ratio between them. A "
      "large gap means the risk is mostly imported — you will misprice it by studying its own "
      "domain alone.</p>")
    amp = sorted(events, key=lambda r: -r["amplification"])[:14]
    W('<div class="card"><div class="legend">'
      '<span><i style="background:var(--s2);border-radius:50%"></i>domain in isolation</span>'
      '<span><i style="background:var(--s1);border-radius:50%"></i>fully coupled world</span></div>'
      '<div class="scroll">')
    W(dumbbell(amp))
    W("</div></div>")

    damped = [r for r in sorted(events, key=lambda r: r["amplification"])[:6]]
    if damped:
        W("<p>At the other end, these are the risks the coupled world <em>damps</em> — where "
          "stabilizing feedbacks and stress-triggered responses outweigh contagion:</p>")
        W('<div class="card"><div class="scroll">')
        W(dumbbell(damped))
        W("</div></div>")

    # ---- timing ----
    tl = res.get("timelines")
    if tl and tl["cumulative"]:
        picks = [r["id"] for r in sorted(events, key=lambda r: -r["p_2036"])
                 if r["id"] in sysm["severe_ids"]][:5]
        if picks:
            W("<h2>Where the risk sits in time</h2>")
            W("<p>Cumulative probability by quarter. Two events can quote the same 2036 number "
              "and mean very different things for anyone deciding what to do this year: a flat "
              "hazard and a back-loaded one look identical at the horizon and nothing alike "
              "in 2028.</p>")
            W('<div class="card"><div class="scroll">')
            W(timelines([{"label": ev_by_id[p]["statement"][:24], "values": tl["cumulative"][p]}
                         for p in picks]))
            W("</div></div>")

    # ---- scenarios ----
    W("<h2>Emergent scenarios</h2>")
    W("<p>Nobody wrote these scenarios. They are clusters found in the simulated trajectories "
      "themselves — the world-shapes the coupled dynamics actually produce, with the share of "
      "futures landing in each.</p>")
    for c in res["scenarios"]["clusters"]:
        W('<div class="sc">')
        W(f'<div class="p">{fmt_pct(c["probability"], 1)} of futures</div>')
        distinct = [d for d in c["distinguishing_events"]
                    if abs(d["p_in_cluster"] - d["p_overall"]) > 0.02][:5]
        if distinct:
            W("<h4>What distinguishes it</h4><table><tr><th>Event</th><th>Here</th>"
              "<th>Overall</th></tr>")
            for d in distinct:
                st = ev_by_id.get(d["id"], {}).get("statement", d["id"])
                W(f'<tr><td>{E(st[:70])}</td><td class="n">{fmt_pct(d["p_in_cluster"])}</td>'
                  f'<td class="n">{fmt_pct(d["p_overall"])}</td></tr>')
            W("</table>")
        prof = [i for i in c["indicator_profile"] if abs(i["z"]) > 0.25][:5]
        if prof:
            W("<h4>Where it ends up</h4><table><tr><th>Indicator</th><th>2036</th>"
              "<th>vs today</th></tr>")
            for i in prof:
                W(f'<tr><td>{E(i["label"][:60])}</td><td class="n">{sig(i["value"])} '
                  f'{E(i["unit"][:16])}</td><td class="n">{i["z"]:+.2f}σ</td></tr>')
            W("</table>")
        W(f'<p class="meta">Mean severe events in this cluster: {c["mean_severe_events"]:.2f}</p>')
        W("</div>")

    # ---- regimes ----
    W("<h2>Regimes</h2>")
    W("<p>A slow Markov layer scaling volatility and crisis hazards globally — the model's way "
      "of saying that the same tension index means something different in 1995 than in 1938.</p>")
    W('<div class="card"><table><tr><th>Regime</th><th>Today</th><th>Time share</th>'
      "<th>Hazard</th><th>Vol</th></tr>")
    for r in res["regimes"]:
        W(f'<tr><td><strong style="color:var(--ink)">{E(r["name"])}</strong><br>'
          f'{E(r["description"][:150])}</td>'
          f'<td class="n">{fmt_pct(r["initial_probability"])}</td>'
          f'<td class="n">{fmt_pct(r["expected_time_share"])}</td>'
          f'<td class="n">{r["hazard_multiplier"]:.2f}×</td>'
          f'<td class="n">{r["vol_multiplier"]:.2f}×</td></tr>')
    W("</table></div>")

    # ---- fans ----
    avail = [k for k in FAN_KEYS if k in fans]
    if avail:
        W("<h2>Where the measurable quantities go</h2>")
        W("<p>Median with 50% and 90% bands. These are the continuous state variables the event "
          "hazards actually key off, so their spread is upstream of every probability above.</p>")
        W('<div class="card"><div class="legend">'
          f'<span><i style="background:{SEQ[9]}"></i>median</span>'
          f'<span><i style="background:{SEQ[5]}"></i>50% band</span>'
          f'<span><i style="background:{SEQ[2]}"></i>90% band</span></div>')
        W('<div class="fans">')
        for k in avail:
            f = fans[k]
            W(f'<div class="fan"><h4>{E(f["label"][:44])}</h4>'
              f'<div class="u">{E(f["unit"][:38])} · now {sig(f["start"])}</div>')
            W(fan(k, f))
            W("</div>")
        W("</div></div>")

    # ---- sensitivity ----
    if res["sensitivity"]:
        W("<h2>What the answers hang on</h2>")
        W("<p>Rank correlation between each uncertain input and the number of severe shocks a "
          "path experiences. This is variance attribution, not causation — but it tells you "
          "which assumption to argue with first.</p>")
        W('<div class="card"><div class="scroll">')
        W(sensitivity_bars(res["sensitivity"][:16]))
        W("</div></div>")

    # ---- full table ----
    W("<h2>Full results</h2>")
    W("<p>Every event, with its resolution criterion and the historical reference class the "
      "base rate came from. This is also the table view for the charts above.</p>")
    W('<div class="card scroll"><table><tr><th>Event</th><th>2027</th><th>2030</th>'
      "<th>2036</th><th>Isolated</th><th>Amp</th></tr>")
    for r in sorted(events, key=lambda x: (x["domain"], -x["p_2036"])):
        W(f'<tr><td><strong style="color:var(--ink)">{E(r["statement"][:110])}</strong><br>'
          f'<span style="color:var(--muted);font-size:12px">{E(r["resolution_criteria"][:190])}'
          f'</span></td>'
          f'<td class="n">{fmt_pct(r["p_2027"], 1)}</td><td class="n">{fmt_pct(r["p_2030"], 1)}</td>'
          f'<td class="n">{fmt_pct(r["p_2036"], 1)}</td>'
          f'<td class="n">{fmt_pct(r["p_indep_2036"], 1)}</td>'
          f'<td class="n">{r["amplification"]:.2f}×</td></tr>')
    W("</table></div>")

    # ---- method ----
    W("<h2>How it works, and where it breaks</h2>")
    W("<details><summary>The model</summary><p>The world is a state vector of "
      f'{m["n_indicators"]} continuous indicators plus {m["n_events"]} discrete events with '
      "state-dependent hazards, marched in quarterly steps. Each step: a Markov regime layer "
      "switches; indicators evolve by mean reversion toward a drifting attractor plus lagged "
      "cross-domain coupling plus correlated Student-t innovations (ν=5, because macro and "
      "conflict series are decisively not Gaussian) plus stabilizing feedbacks that engage only "
      "once a variable is visibly stressed; events fire against hazards modulated by indicator "
      "levels, regime, and what has already fired; and events that fire shock the indicators, "
      "closing the loop.</p></details>")
    W("<details><summary>Why the intervals are honest about parameters</summary><p>Every path "
      "draws its own hazards, volatilities, drifts and coupling strengths from priors centred on "
      "the analysts' estimates, with widths set by each analyst's own stated confidence. The "
      "hazard error is split into a shared component and an idiosyncratic one — purely "
      "independent jitter would imply the analysts are wrong about each event in unrelated "
      "directions, so their errors cancel and the <em>number</em> of shocks per decade comes out "
      "better-known than any individual shock. That is not how miscalibration works.</p></details>")
    W("<details><summary>Why there are two runs</summary><p>Hazard is exponential in indicator "
      "z-scores, so the average hazard across paths exceeds the hazard at the average state; "
      "Jensen's inequality would silently inflate every probability above what the analysts "
      "actually said. The first pass fits a per-event offset against a decoupled baseline until "
      "marginals reproduce the elicited priors. The second turns coupling, contagion and regimes "
      "on with those offsets frozen. The gap between them is the amplification reported "
      "above.</p></details>")
    W("<details><summary>Where the parameters came from</summary><p>Nine domain analysts, each "
      "required to establish its current-state numbers by live web research rather than from "
      "training data, and each then rewritten by an adversarial auditor checking for arithmetic "
      "incoherence between annual hazards and cumulative quotes, monotonicity violations, "
      "invented reference classes, recency bias extrapolating headlines into trends, aggregate "
      "over-prediction of discontinuity, and volatilities inconsistent with how the series have "
      "actually moved. A tenth agent built the transmission matrix, regimes, contagion rules and "
      "stabilizing feedbacks.</p></details>")
    W("<details><summary>What this cannot do</summary><p>It cannot know the parameters. Every "
      "number inherits the analysts' judgement, and on thin-reference-class questions — "
      "great-power war, loss-of-control incidents, AMOC collapse — that judgement is doing most "
      "of the work. The Monte Carlo error bars are the least important source of uncertainty "
      "here. The model also cannot produce a surprise that nobody parameterised: the single most "
      "likely way the 2030s actually go is through a mechanism absent from this event list "
      "entirely, and no amount of sampling fixes that.</p></details>")

    W(f'<p class="meta" style="margin-top:40px">{m["paths"]:,} paths · seed {m["seed"]} · '
      f'{m["runtime_seconds"]}s · reproduce with <code>python run_simulation.py</code></p>')
    W("</div></div>")
    W('<div id="geo-tip"></div>')
    W("""<script>
(function(){
  var tip=document.getElementById('geo-tip');
  document.addEventListener('mouseover',function(e){
    var t=e.target.closest('[data-tip]'); if(!t)return;
    tip.textContent=t.getAttribute('data-tip'); tip.style.opacity='1';
  });
  document.addEventListener('mousemove',function(e){
    if(tip.style.opacity!=='1')return;
    var w=tip.offsetWidth,h=tip.offsetHeight;
    var x=e.clientX+16,y=e.clientY+16;
    if(x+w>innerWidth-8)x=e.clientX-w-16;
    if(y+h>innerHeight-8)y=e.clientY-h-16;
    tip.style.left=x+'px'; tip.style.top=y+'px';
  });
  document.addEventListener('mouseout',function(e){
    if(e.target.closest('[data-tip]'))tip.style.opacity='0';
  });
})();
</script>""")
    return "\n".join(parts)


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(ROOT / "results"))
    a = ap.parse_args()
    d = Path(a.dir)
    res = json.loads((d / "results.json").read_text())
    fans = json.loads((d / "fans.json").read_text())
    out = d / "report.html"
    out.write_text(build(res, fans))
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()

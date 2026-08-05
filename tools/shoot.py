#!/usr/bin/env python3
"""Screenshot the built page in both themes, and report console errors.

The palette validator checks color, not layout. This is the "render it and look
at it" step: label collisions, overflow, and silent JS failures only show up in
a real browser.
"""

from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    page_path = (Path(sys.argv[1]).resolve() if len(sys.argv) > 1
                 else ROOT / "output" / "forecast.html")
    outdir = ROOT / "output" / "shots" / page_path.stem
    outdir.mkdir(parents=True, exist_ok=True)

    problems: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        for theme in ("light", "dark"):
            ctx = browser.new_context(
                viewport={"width": 1280, "height": 1000},
                device_scale_factor=2,
                color_scheme=theme,
            )
            page = ctx.new_page()
            page.on("console", lambda m: problems.append(f"[{theme} console.{m.type}] {m.text}")
                    if m.type in ("error", "warning") else None)
            page.on("pageerror", lambda e: problems.append(f"[{theme} pageerror] {e}"))
            page.goto(page_path.as_uri())
            page.wait_for_timeout(900)

            # Horizontal overflow of the page body is a hard failure.
            overflow = page.evaluate(
                "() => document.documentElement.scrollWidth - document.documentElement.clientWidth"
            )
            if overflow > 2:
                problems.append(f"[{theme}] body scrolls horizontally by {overflow}px")

            page.screenshot(path=str(outdir / f"{theme}-top.png"))
            for name, sel in [
                ("stress", "#stress"), ("headline", "#headline"),
                ("archetypes", "#archetypes"), ("pairs", "#pairs"),
                ("why", "#why"), ("map", "#map"), ("timeline", "#timeline"),
                ("topline", "#topline"),
            ]:
                loc = page.locator(sel)
                if loc.count():
                    loc.scroll_into_view_if_needed()
                    page.wait_for_timeout(200)
                    loc.screenshot(path=str(outdir / f"{theme}-{name}.png"))
            ctx.close()
        browser.close()

    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  " + p)
    else:
        print("no console errors, no horizontal overflow")
    print(f"shots in {outdir}")


if __name__ == "__main__":
    main()

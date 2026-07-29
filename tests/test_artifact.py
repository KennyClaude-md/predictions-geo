"""The artifact builder's text handling.

The report layer emits markdown; the page injects several of those strings as
HTML. That boundary is where asterisks leak into the rendered page and where
analyst-written text could inject markup, so it gets its own tests.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from build_artifact import md_inline, q_label, sig  # noqa: E402


def test_bold_and_italic_render():
    assert md_inline("**Head.** then *ital*") == "<strong>Head.</strong> then <em>ital</em>"


def test_html_is_escaped_before_markdown_runs():
    """Research text is agent-written and reaches the page as innerHTML."""
    out = md_inline('<script>alert("x")</script> & more')
    assert "<script>" not in out
    assert "&lt;script&gt;" in out and "&amp;" in out


def test_multiplication_is_not_italics():
    assert md_inline("P(A) * P(B) stays") == "P(A) * P(B) stays"


def test_asterisks_never_survive_into_output():
    for s in [
        "the variance is not *whether* they arrive",
        "*geopolitics* averages 8.1 while *climate* averages 6.1",
        "**Node** — *suppressed*: 30% vs 40%",
    ]:
        assert "*" not in md_inline(s)


def test_quarter_labels_track_the_simulation_clock():
    assert q_label(1) == "2026Q3"
    assert q_label(6) == "2027Q4"
    assert q_label(22) == "2031Q4"
    assert q_label(42) == "2036Q4"
    assert q_label(None) == "—"


def test_significant_figures_survive_small_and_large_values():
    assert sig(0.00123456) == 0.00123
    assert sig(86.4321) == 86.4
    assert sig(3615.7) == 3620
    assert sig(0.0) == 0.0

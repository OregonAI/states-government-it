"""Nebraska: a provision of a non-IT chapter, cut from the Legislature's whole-chapter page by the shared slice shape
{section_start, section_end_before} (section_end_before is the next section's number and is not in the text). The
fixtures are real bytes (page head and tail kept) of chapters 81, 84 and 49 with a few neighbouring sections."""
import re
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import nebraska

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "nebraska"
CH81 = (FIX / "ch81-cut.html").read_bytes()
CH84 = (FIX / "ch84-cut.html").read_bytes()
CH49 = (FIX / "ch49-cut.html").read_bytes()


def cut(raw, start, end_before):
    return nebraska.statute_html_to_text(raw, {"section_start": start, "section_end_before": end_before})


def heads(text):
    return re.findall(r"^(\d+-\d+(?:,\d+)?(?:\.\d+)?)\. ", text, flags=re.M)


def test_the_slice_starts_at_the_first_heading_and_stops_before_the_next_section():
    text = cut(CH81, "81-1117", "81-1117.01")
    assert text.startswith("81-1117. Information management services administrator; powers, duties, and responsibilities;")
    assert "Laws 2026, LB905, § 41.\nOperative Date: July 1, 2026" in text
    assert "81-1117.01" not in text and "Imprest Payroll" not in text and "81-1117.02" not in text


def test_a_section_range_includes_every_section_in_it():
    text = cut(CH84, "84-1204", "84-1205.01")
    assert heads(text) == ["84-1204", "84-1205"]
    assert "Repealed. Laws 2017, LB644" not in text


def test_a_section_range_that_spans_a_repealed_section_prints_it_as_the_page_does():
    text = cut(CH84, "84-1205.03", "84-1205.06")
    assert heads(text) == ["84-1205.03", "84-1205.04", "84-1205.05"]
    assert "84-1205.04. Repealed. Laws 2012, LB 719, § 33." in text


def test_the_next_section_and_the_page_furniture_are_excluded():
    text = cut(CH81, "81-1120.27", "81-1120.28")
    assert heads(text) == ["81-1120.27"]
    assert "news agency" not in text            # 81-1120.28's caption
    for leak in ("<", ">", "font-family", "printwidth", "&nbsp;", "/laws/statutes.php", "Nebraska Legislature"):
        assert leak not in text


def test_a_number_with_a_comma_and_a_decimal_part_is_one_section_number():
    text = cut(CH49, "49-14,101.01", "49-14,101.02")
    assert heads(text) == ["49-14,101.01"]
    assert "49-14,101.02" not in text and "public resources means" not in text
    assert "49-14,101.03" not in cut(CH49, "49-14,101.01", "49-14,101.03")


def test_a_boundary_the_page_does_not_hold_refuses_the_slice():
    with pytest.raises(ValueError, match="81-9999"):
        cut(CH81, "81-1117", "81-9999")
    with pytest.raises(ValueError, match="81-9998"):
        cut(CH81, "81-9998", "81-1117.01")


def test_an_end_before_the_start_or_equal_to_it_refuses_the_slice():
    with pytest.raises(ValueError, match="backwards|empty"):
        cut(CH81, "81-1120.27", "81-1117")
    with pytest.raises(ValueError, match="backwards|empty"):
        cut(CH81, "81-1117", "81-1117")


def test_a_slice_with_both_shapes_or_a_stray_key_is_refused():
    with pytest.raises(ValueError, match="slice"):
        nebraska.statute_html_to_text(CH81, {"section_start": "81-1117", "section_end_before": "81-1117.01", "part": "81-1117"})
    with pytest.raises(ValueError, match="slice"):
        nebraska.statute_html_to_text(CH81, {"section_start": "81-1117"})


SRC = {"id": "ne-rs-81-1117", "jurisdiction": "nebraska", "doc_type": "statute", "format": "html",
       "citation": "Neb. Rev. Stat. section 81-1117", "title": "x",
       "slice": {"section_start": "81-1117", "section_end_before": "81-1117.01"}}


def test_the_shared_flow_cuts_the_range_and_the_identity_check_confirms_it():
    fmt, text = ing.derive(SRC, CH81)
    assert fmt == "html" and text.startswith("81-1117. ")
    states.check_identity(SRC, text)


def test_a_range_that_is_not_the_cited_section_is_refused():
    _, text = ing.derive(SRC, CH81)
    with pytest.raises(ValueError, match="not the cited"):
        states.check_identity({**SRC, "citation": "Neb. Rev. Stat. section 81-1117.02"}, text)
    with pytest.raises(ValueError, match="not the cited|ends"):
        states.check_identity({**SRC, "citation": "Neb. Rev. Stat. sections 81-1117 to 81-1120.02"}, text)


def test_a_slice_whose_first_section_is_not_the_one_it_names_is_refused():
    _, text = ing.derive(SRC, CH81)
    with pytest.raises(ValueError, match="not the cited"):
        states.check_identity({**SRC, "slice": {"section_start": "81-1120.02", "section_end_before": "81-1120.03"}}, text)


def test_the_curator_note_names_the_range_the_way_the_slice_is_written():
    sl = nebraska.notes(SRC, "html", "text")
    assert "from section 81-1117 up to, and not including, section 81-1117.01" in sl
    inclusive = nebraska.notes({**SRC, "slice": {"article": "86-572", "part": "86-573"}}, "html", "text")
    assert "first and last inclusive" in inclusive

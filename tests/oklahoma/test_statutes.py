"""Oklahoma statutes: the Legislature serves each title as one PDF; a document is the sections from one printed
heading to the next. Fixtures are real pages of the November 2026 Title 62 and Title 74 PDFs (the first, contents
page, and the pages around the sections under test)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "oklahoma"
T62 = (FIX / "title-62-pages.pdf").read_bytes()
T74 = (FIX / "title-74-pages.pdf").read_bytes()


def cut(raw, start, end_before):
    return ing.to_text(raw, "pdf", "statute", "oklahoma",
                       {"section_start": start, "section_end_before": end_before})


def test_a_slice_runs_from_its_first_heading_to_the_heading_it_stops_before():
    text = cut(T62, "34.43", "34.44")
    lines = text.splitlines()
    assert lines[0] == "§62-34.43. Detailed information technology budgets"
    assert "§62-34.44." not in text and "§62-34.42" not in text
    assert lines[-1] == "Amended by Laws 2012, c. 304, § 373.; Laws 2026, c. 184, § 8, eff. Sept. 1, 2026."


def test_a_contents_entry_that_wraps_is_not_taken_for_the_heading():
    # The contents (page 1) prints `§62-34.11.1.2. Oklahoma Employment Security Commission Information Technology`
    # with no dot leaders on that line; the section's own heading is on page 40.
    text = cut(T62, "34.11.1.2", "34.11.1")
    assert text.splitlines()[0] == "§62-34.11.1.2. Oklahoma Employment Security Commission"
    assert "...." not in text
    assert "§62-34.11.1. " not in text


def test_the_page_footer_inside_a_section_stays():
    text = cut(T62, "34.11.1.1", "34.11.1.2")
    assert "Oklahoma Statutes - Title 62. Public Finance" in text


def test_a_section_alone_stops_before_its_next_heading():
    text = cut(T62, "36", "36.1")
    assert text.startswith("§62-36. Digital Transformation Program Revolving Fund.")
    assert "§62-36.1." not in text


def test_title_74_headings_carry_the_74_prefix():
    text = cut(T74, "3113.1", "3114")
    assert text.startswith("§74-3113.1. ")
    assert "§74-3114." not in text


def test_a_heading_the_pdf_does_not_print_refuses_the_slice():
    with pytest.raises(ValueError, match="34.999"):
        cut(T62, "34.999", "35.1")
    with pytest.raises(ValueError, match="34.99"):
        cut(T62, "34.43", "34.99")      # the end heading must be there, or the slice would be a guess


def test_an_end_heading_before_the_start_refuses_the_slice():
    with pytest.raises(ValueError):
        cut(T62, "34.44", "34.43")


def test_a_statute_pdf_with_no_slice_is_still_the_whole_pdf():
    text = ing.to_text(T62, "pdf", "statute", "oklahoma")
    assert "§62-34.43." in text and "§62-36." in text


SRC = {"id": "ok-62-os-34-43", "jurisdiction": "oklahoma", "doc_type": "statute", "format": "pdf",
       "citation": "62 O.S. 34.43", "title": "x",
       "slice": {"section_start": "34.43", "section_end_before": "34.44"}}


def test_a_slice_is_the_cited_section_when_it_opens_and_closes_on_the_cited_numbers():
    text = cut(T62, "34.43", "34.44")
    states.check_identity(SRC, text, "pdf")
    range_src = dict(SRC, citation="62 O.S. 34.11.1.1 to 34.11.1.2",
                     slice={"section_start": "34.11.1.1", "section_end_before": "34.11.1"})
    states.check_identity(range_src, cut(T62, "34.11.1.1", "34.11.1"), "pdf")


def test_a_slice_that_is_not_the_cited_section_is_refused():
    text = cut(T62, "34.43", "34.44")
    with pytest.raises(ValueError):
        states.check_identity(dict(SRC, citation="62 O.S. 34.42"), text, "pdf")
    with pytest.raises(ValueError):          # the citation promises a range the slice does not reach
        states.check_identity(dict(SRC, citation="62 O.S. 34.43 to 34.44"), text, "pdf")
    with pytest.raises(ValueError):          # the slice is of the other title
        states.check_identity(dict(SRC, citation="74 O.S. 34.43"), text, "pdf")


def test_a_statute_has_no_effective_date_and_the_notes_name_the_slice():
    text = cut(T62, "34.43", "34.44")
    assert states.effective_date(text, "statute", "oklahoma") is None
    note = states.hook("oklahoma", "extra_notes")(dict(SRC, currency_note="CN."), "pdf", text, None, "")
    assert "34.43" in note and "34.44" in note and "CN." in note


def test_a_single_section_printed_as_repealed_is_not_in_force():
    src = dict(SRC, citation="62 O.S. 34.30", slice={"section_start": "34.30", "section_end_before": "34.31"})
    with pytest.raises(ValueError, match="repealed"):
        states.check_identity(src, "§62-34.30. Repealed by Laws 2025, c. 317, § 4, eff. July 1, 2025.\n", "pdf")


def test_a_slice_that_prints_an_amendment_not_yet_in_effect_is_refused():
    # Section 34.11.1 as printed in the November 2026 PDF carries `Laws 2026, c. 445, § 131, eff. Jan. 1, 2027`:
    # the printed text is the version that takes effect then, not the law in force.
    src = dict(SRC, citation="62 O.S. 36", slice={"section_start": "36", "section_end_before": "36.1"})
    text = ("§62-36. Digital Transformation Program Revolving Fund.\nText.\nAmended by Laws 2020, c. 1, § 4, emerg. eff.\n"
            "May 22, 2020; Laws 2026, c. 445, § 143, eff. Jan.\n1, 2999.\n")
    with pytest.raises(ValueError, match="2999-01-01"):
        states.check_identity(src, text, "pdf")
    states.check_identity(src, text.replace("2999", "2026"), "pdf")

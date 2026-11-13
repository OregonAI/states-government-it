"""North Dakota statute sections: the Legislative Council serves each Century Code chapter as one PDF, and a document is the
sections from one printed heading to the next. The fixture is the real chapter 23-12 PDF served 2026-11-13 (whole file,
page footers included): section 23-12-19 wraps its heading over two lines and runs across a page break."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.ingest_common import pdf_to_text

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "north-dakota"
RAW = (FIX / "ndcc-23-12.pdf").read_bytes()


def cut(start, end_before, raw=RAW):
    return ing.to_text(raw, "pdf", "statute", "north-dakota",
                       {"section_start": start, "section_end_before": end_before})


def test_a_slice_starts_at_the_first_heading_and_reads_the_wrapped_heading_whole():
    lines = cut("23-12-19", "23-12-20").splitlines()
    assert lines[0].strip() == ("23-12-19. Voluntary participation in the health information organization - "
                                "Prohibition")
    assert lines[1].strip() == "on withholding care or benefits."


def test_a_slice_includes_every_subsection_across_the_page_break():
    text = cut("23-12-19", "23-12-20")
    for needle in ('"Health information organization" means', '"Individually identifiable health information"',
                   "An individual may opt-out", "Opting out of participating; or", "May be changed at any time",
                   "based solely on that individual's choice"):
        assert needle in text


def test_a_slice_excludes_the_next_section_and_the_one_before():
    text = cut("23-12-19", "23-12-20")
    assert "23-12-20" not in text and "COVID-19" not in text and "23-12-18" not in text
    assert "breast" not in text


def test_a_slice_excludes_page_footers_wherever_they_fall():
    text = cut("23-12-19", "23-12-20")
    assert "Page No." not in text
    assert text.endswith("health information organization.\n")


def test_a_slice_of_several_sections_keeps_the_ones_between():
    text = cut("23-12-18", "23-12-20")
    assert text.lstrip().startswith("23-12-18.") and "23-12-19." in text and "23-12-20." not in text


def test_a_slice_does_not_take_a_mention_of_a_number_for_the_heading():
    # section 23-12-19's heading is mentioned nowhere else, but a body line that begins with a number must not match
    t = pdf_to_text(RAW)
    assert sum(1 for _ in states.hook("north-dakota", "_headings")(t.splitlines()) if _[1] == "23-12-19") == 1


def test_a_heading_the_pdf_does_not_print_refuses_the_slice():
    with pytest.raises(ValueError, match="printed 0 times"):
        cut("23-12-99", "23-12-100")
    with pytest.raises(ValueError, match="does not follow"):
        cut("23-12-19", "23-12-99")


def test_a_chapter_pdf_with_no_slice_is_still_the_whole_chapter():
    assert "23-12-01." in pdf_to_text(RAW) and "CHAPTER 23-12" in pdf_to_text(RAW)


SRC = {"id": "x", "jurisdiction": "north-dakota", "doc_type": "statute", "format": "pdf", "title": "t",
       "citation": "N.D.C.C. section 23-12-19", "slice": {"section_start": "23-12-19", "section_end_before": "23-12-20"}}


def test_a_slice_is_the_cited_section_when_it_opens_and_closes_on_it():
    states.check_identity(SRC, cut("23-12-19", "23-12-20"))


def test_a_slice_that_is_not_the_cited_section_is_refused():
    with pytest.raises(ValueError):
        states.check_identity(dict(SRC, citation="N.D.C.C. section 23-12-18"), cut("23-12-19", "23-12-20"))
    with pytest.raises(ValueError):          # the slice reaches past the cited section
        states.check_identity(SRC, cut("23-12-19", "23-12-21"))
    with pytest.raises(ValueError):          # the slice starts on another section
        states.check_identity(SRC, cut("23-12-18", "23-12-20"))


def test_a_repealed_section_is_refused_as_not_in_force():
    src = dict(SRC, citation="N.D.C.C. section 23-12-01", slice={"section_start": "23-12-01",
                                                               "section_end_before": "23-12-02"})
    with pytest.raises(ValueError, match="repealed"):
        states.check_identity(src, cut("23-12-01", "23-12-02"))


def test_the_notes_name_the_slice_and_the_footer_cleanup():
    h = states.hook("north-dakota", "extra_notes")
    n = h(SRC, "pdf", cut("23-12-19", "23-12-20"), None, "")
    assert "whole of chapter 23-12" in n and "23-12-19" in n and "23-12-20" in n and "footer" in n

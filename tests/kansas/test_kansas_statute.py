"""Kansas: the Revisor of Statutes serves one section per static page (ksrevisor.gov/statutes/chapters/...).
Fixtures are whole real pages with their navigation, print and footer furniture: K.S.A. 75-7201 (a long section
with a Revisor's Note and cross references) and 75-7236 (a one-sentence section)."""
from pathlib import Path

import pytest

from src import states
from src.states import kansas

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "kansas"
S7201 = (FIX / "75-7201.html").read_bytes()
S7236 = (FIX / "75-7236.html").read_bytes()
SRC = {"id": "ks-ksa-75-7236", "jurisdiction": "kansas", "doc_type": "statute",
       "citation": "K.S.A. 75-7236", "title": "Kansas cybersecurity act"}


def test_the_state_is_found_by_name():
    assert "kansas" in states.modules(refresh=True)


def test_a_section_page_becomes_number_caption_text_and_history_one_line_per_paragraph():
    lines = kansas.section_html_to_text(S7201).splitlines()
    assert lines[0].startswith("75-7201. Definitions. As used in K.S.A. 75-7201 through 75-7212, and amendments thereto:")
    assert '(a) "Business risk" means the overall level of risk' in lines[1]
    assert "History: L. 1998, ch. 182, § 1; L. 2023, ch. 75, § 4; L. 2024, ch. 95, § 16; July 1." in lines


def test_the_revisors_note_and_cross_references_that_the_page_prints_are_kept():
    text = kansas.section_html_to_text(S7201)
    assert "Revisor's Note:\nCAUTION: Section was further amended by L. 2024, ch. 95, § 17, to be effective on July 1, 2026." in text
    assert "Cross References to Related Sections:\nSecurity conditions of employment" in text


def test_page_furniture_does_not_leak():
    for raw in (S7201, S7236):
        text = kansas.section_html_to_text(raw)
        for leak in ("<", ">", "Printable Format", "Previous", "LEGISLATIVE COORDINATING COUNCIL", "Contact Us",
                     "ksrevisor.gov 2026", "&nbsp;", "\t", "goBack"):
            assert leak not in text


def test_a_page_without_a_statute_is_refused():
    with pytest.raises(ValueError, match="no statute text"):
        kansas.section_html_to_text(b"<html><body><p>Not found</p></body></html>")


def test_identity_accepts_the_cited_section_and_refuses_another():
    text = kansas.section_html_to_text(S7236)
    assert kansas.check_identity(SRC, text, "page") is True
    with pytest.raises(ValueError, match="is not K.S.A. 75-7237"):
        kansas.check_identity({**SRC, "citation": "K.S.A. 75-7237"}, text, "page")
    # a section that merely mentions the cited number is not it
    with pytest.raises(ValueError):
        kansas.check_identity({**SRC, "citation": "K.S.A. 75-7243"}, text, "page")


def test_identity_leaves_other_states_alone():
    assert kansas.check_identity({**SRC, "jurisdiction": "texas"}, "x", "page") is False


def test_to_text_hook_takes_html_statutes_only():
    assert kansas.to_text(S7236, "html", "statute", None, "www.ksrevisor.gov").startswith("75-7236. Kansas cybersecurity act.")
    assert kansas.to_text(S7236, "html", "rule", None, "x") is None


def test_notes_describe_the_reading():
    assert "one section per page" in kansas.notes(SRC, "html", "x")


@pytest.mark.parametrize("fixture, number", [("50-7a02.html", "50-7a02"), ("74-72-123.html", "74-72,123")])
def test_section_numbers_with_a_letter_or_a_comma_are_read(fixture, number):
    text = kansas.section_html_to_text((FIX / fixture).read_bytes())
    assert text.startswith(number + ". ")
    src = {**SRC, "citation": "K.S.A. " + number}
    assert kansas.check_identity(src, text, "page") is True

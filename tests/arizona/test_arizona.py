"""Arizona: the Legislature's per-section statute pages (www.azleg.gov/ars/<title>/<nnnnn>.htm). Fixtures are the
whole bytes of three real section pages, page furniture (TITLE, comment lines, font tags) included."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import arizona

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "arizona"
S104 = (FIX / "ars-18-104.htm").read_bytes()
S102 = (FIX / "ars-18-102.htm").read_bytes()
S551 = (FIX / "ars-18-551.htm").read_bytes()
SRC = {"id": "az-ars-18-102", "jurisdiction": "arizona", "doc_type": "statute", "citation": "A.R.S. 18-102",
       "title": "18-102 - Government information technology"}


def test_the_state_is_found_by_name():
    assert "arizona" in states.modules(refresh=True)


def test_a_section_page_becomes_its_number_and_caption_then_one_line_per_paragraph():
    lines = arizona.section_html_to_text(S104).splitlines()
    assert lines[0] == "18-104. Powers and duties of the department; violation; classification"
    assert lines[1] == "A. The department shall:"
    assert lines[2].startswith("1. Develop, implement and maintain a coordinated statewide plan")
    assert lines[-1].startswith("D. The director, any member of the director's staff or any employee who knowingly")


def test_the_number_is_kept_when_the_period_sits_outside_the_font_tag():
    assert arizona.section_html_to_text(S102).splitlines()[0] == "18-102. Government information technology"


def test_entities_and_the_empty_nbsp_paragraph_are_resolved_and_no_markup_or_furniture_leaks():
    text = arizona.section_html_to_text(S551)
    assert '1. "Breach" or "security system breach":' in text.splitlines()
    for leak in ("<", ">", "&quot;", "&nbsp;", "Creation Date", "Arizona Legislative Council", "dbupdate", "\xa0"):
        assert leak not in text
    assert text.endswith("\n") and not text.endswith("\n\n")


def test_a_page_that_is_not_a_section_is_refused_not_committed():
    with pytest.raises(ValueError, match="no statute text"):
        arizona.section_html_to_text(b"<html><body><h1>Not Found</h1></body></html>")


def test_the_shared_flow_reaches_this_reader_for_html_statutes_and_no_other_combination():
    assert ing.to_text(S102, "html", "statute", "arizona").startswith("18-102. ")
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(S102, "html", "rule", "arizona")


def test_identity_accepts_the_cited_section():
    text = arizona.section_html_to_text(S102)
    states.check_identity(SRC, text)


def test_identity_refuses_another_section_or_a_changed_caption():
    text = arizona.section_html_to_text(S104)
    with pytest.raises(ValueError, match="is not A.R.S. 18-102"):
        states.check_identity(SRC, text)
    text = arizona.section_html_to_text(S102)
    with pytest.raises(ValueError, match="is not A.R.S. 18-102"):
        states.check_identity({**SRC, "title": "18-102 - Something else"}, text)


def test_a_statute_gets_no_effective_date_and_the_notes_describe_the_reading():
    text = arizona.section_html_to_text(S102)
    assert states.effective_date(text, "statute", "arizona") is None
    note = arizona.notes(SRC, "html", text)
    assert "section page" in note and "Creation Date" in note


def test_identity_goes_by_the_body_caption_not_the_title_element():
    """18-422's TITLE element prints a control character (0x1E) where the body caption prints "third-party"."""
    page = (b"<HTML><HEAD><TITLE>18-422 - State agencies; third\x1eparty electronic service provider authorization</TITLE></HEAD>"
            b"<BODY><p><font color=GREEN>18-422</font>. <font color=PURPLE><u>State agencies; third-party electronic "
            b"service provider authorization</u></font></p><p>A. Any state agency may authorize a person.</p></BODY></HTML>")
    src = {**SRC, "id": "az-ars-18-422", "citation": "A.R.S. 18-422",
           "title": "18-422 - State agencies; third-party electronic service provider authorization"}
    states.check_identity(src, arizona.section_html_to_text(page))


# ---- the Governor's order page (executive orders) ----------------------------------
EO = (FIX / "eo-2023-10.htm").read_bytes()
EO_SRC = {"id": "az-eo-2023-10", "jurisdiction": "arizona", "doc_type": "executive_order",
          "citation": "Executive Order 2023-10", "title": "Protecting the State's Cybersecurity Interests",
          "format": "html"}


def test_an_order_page_becomes_heading_title_date_then_the_order_text():
    lines = arizona.order_html_to_text(EO).splitlines()
    assert lines[:3] == ["Executive Order 2023-10", "Protecting the State’s Cybersecurity Interests",
                         "April 4, 2023"]
    assert lines[3].startswith("WHEREAS, the security and privacy of Arizonans")
    assert "NOW, THEREFORE, I, Katie Hobbs, Governor of the State of Arizona" in lines[7]


def test_list_items_are_numbered_and_the_last_section_continues_the_count_as_nine():
    text = arizona.order_html_to_text(EO)
    lines = text.splitlines()
    assert any(l.startswith("1. Within 30 days of this Order") for l in lines)
    assert any(l.startswith("2. The Arizona Department of Administration and the Arizona Department of Homeland") for l in lines)
    assert any(l.startswith("8. This Order does not confer") for l in lines)
    assert "9. This Order shall take effect immediately upon signature." in lines
    assert "1. This Order shall take effect" not in text
    assert text.count("Persona! ") == 0 and "Personal devices used for State work include" in text


def test_no_page_furniture_or_markup_leaks_into_the_order():
    text = arizona.order_html_to_text(EO)
    for leak in ("<", "Stay In Touch", "Download Executive Order", "Mailchimp", "Governor Hobbs\n", "&nbsp;", "\xa0"):
        assert leak not in text
    assert text.endswith("\n") and not text.endswith("\n\n")


def test_a_page_that_is_not_an_order_is_refused():
    with pytest.raises(ValueError, match="no order text"):
        arizona.order_html_to_text(b"<html><body><h1>Not Found</h1></body></html>")


def test_the_shared_flow_reaches_the_order_reader_for_html_orders():
    assert ing.to_text(EO, "html", "executive_order", "arizona").startswith("Executive Order 2023-10\n")


def test_order_identity_accepts_the_cited_order():
    states.check_identity(EO_SRC, arizona.order_html_to_text(EO))


def test_order_identity_wants_the_orders_own_heading_line_not_a_mention_of_its_number():
    text = arizona.order_html_to_text(EO)
    with pytest.raises(ValueError, match="is not the cited instrument"):
        states.check_identity({**EO_SRC, "citation": "Executive Order 2023-11"}, text)
    mention = "Executive Order 2024-01\nSomething else\nApril 4, 2023\nPursuant to Executive Order 2023-10, agencies shall.\n"
    with pytest.raises(ValueError, match="is not the cited instrument"):
        states.check_identity(EO_SRC, mention)
    # the heading is there but the seed title is not in the opening lines
    with pytest.raises(ValueError, match="is not the cited instrument"):
        states.check_identity({**EO_SRC, "title": "Another title"}, text)


def test_an_order_takes_the_date_its_page_prints_as_effective_and_a_statute_none():
    text = arizona.order_html_to_text(EO)
    assert states.effective_date(text, "executive_order", "arizona") == "2023-04-04"
    assert states.effective_date("Executive Order 2023-10\nT\nno date\n", "executive_order", "arizona") is None


def test_the_order_notes_describe_the_page_reading():
    note = arizona.notes(EO_SRC, "html", arizona.order_html_to_text(EO))
    assert "order page" in note and "numbering" in note

"""Alaska: the Legislature's print view for statutes and rules (akleg.gov/basis/statutes.asp and aac.asp with
media=print and a section range) and the Governor's administrative-order pages (gov.alaska.gov). Seam: the
shared flow's `ing.to_text` and `ing.check_identity`, which reach src/states/alaska.py by name. Fixtures are real
bytes: the two print pages whole; the two order pages whole except their <script> and <style> blocks (cut)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "alaska"
STATUTE = (FIX / "as-44-21-150-170-print.html").read_bytes()
RULE = (FIX / "aac-2-05-200-290-print.html").read_bytes()
AO284 = (FIX / "ao-284.html").read_bytes()
AO360 = (FIX / "ao-360.html").read_bytes()
AO314 = (FIX / "ao-314-style-mentions-content-class.html").read_bytes()


def text(raw, doc_type):
    return ing.to_text(raw, "html", doc_type, "alaska")


def test_the_state_is_found_by_name():
    assert "alaska" in states.modules(refresh=True)


def test_a_statute_range_is_one_line_per_subsection_with_a_blank_line_before_each_section():
    t = text(STATUTE, "statute")
    lines = t.splitlines()
    assert lines[0] == "Sec. 44.21.150. Declaration of purpose."
    assert lines[1].startswith("It is the purpose of AS 44.21.150 — 44.21.170 to designate")
    assert "\n\nSec. 44.21.160. Powers and duties of department." in t
    assert "(b) To carry out (a) of this section the department may, consistent with the state information systems plan adopted by the commissioner and with the departmental information systems plan," in lines
    assert "(1) maintain a central staff of systems analysts, computer programmers, and other staff members sufficient to provide systems analysis and computer programming support required by the executive branch of state government;" in lines
    assert "(h) [Repealed, § 3 ch 156 SLA 1990.]" in lines


def test_the_pages_windows_1252_punctuation_is_read_as_printed_and_no_markup_leaks():
    t = text(STATUTE, "statute")
    assert "(1) “automatic data processing” means" in t
    for leak in ("<", ">", "&nbsp;", "\xa0", "�", "\r", "\t", "  "):
        assert leak not in t


def test_a_rule_range_keeps_each_section_heading_and_its_subparagraph_lines():
    t = text(RULE, "rule")
    assert t.startswith("2 AAC 05.200. Establishment of department's electronic signature verification system.\n")
    assert "\n\n2 AAC 05.210. Verification of electronic signatures.\n" in t
    assert "(1) at least one of the parties to the transaction requiring the action is a state agency that has elected to use the department's system established in 2 AAC 05.200 - 2 AAC 05.290; and" in t.splitlines()
    assert "\t" not in t and "<" not in t


def test_an_order_page_is_its_heading_then_one_line_per_paragraph_and_list_item_without_page_furniture():
    t = text(AO284, "executive_order")
    lines = t.splitlines()
    assert lines[0] == "Administrative Order No. 284"
    assert any(l.startswith("I, Bill Walker, Governor of the State of Alaska") for l in lines)
    assert "Background and Purpose" in lines
    assert "1. Manage all information technology services and related resources within the executive branch of the State;" in lines
    assert "DATED at Juneau, Alaska, this 25th day of April, 2017" in lines
    assert lines[-1] == "Governor"
    for furniture in ("Status of the Flag", "ADMIN ORDERS BY GOVERNOR", "Meet Governor Dunleavy", "COPYRIGHT", "You are here", "Select Page"):
        assert furniture not in t


def test_unordered_lists_and_bold_headings_in_an_order_are_kept():
    t = text(AO360, "executive_order")
    assert t.splitlines()[0] == "Administrative Order No. 360"
    assert "• " in t
    assert "Leverage technology, such as artificial intelligence (“AI”), to support digitization, automation, and public access to permitting information." in t


def test_a_stylesheet_that_mentions_the_content_class_is_not_taken_for_the_order():
    t = text(AO314, "executive_order")
    assert t.startswith("Administrative Order No. 314\n\nI, Michael J. Dunleavy, Governor of the State of Alaska")
    assert "{" not in t and "@media" not in t
    assert t.splitlines()[-1].startswith("Governor") or "Dunleavy" in t.splitlines()[-1]


def test_the_next_articles_heading_the_page_prints_after_the_last_section_is_not_part_of_the_run():
    page = (b'<div class="statute"><b><a name="45.48.090"> </a>Sec. 45.48.090.   Definitions. <BR></b>In this article,<BR><BR>'
            b'&nbsp;(1) one;<BR><BR><BR><BR>Article 2. Credit Report and Credit Score Security Freeze.<BR></div>')
    t = text(page, "statute")
    assert t.splitlines()[-1] == "(1) one;"


def test_a_page_with_no_text_of_record_is_refused_not_committed():
    with pytest.raises(ValueError, match="no text"):
        text(b"<html><body><h1>Not Found</h1></body></html>", "statute")
    with pytest.raises(ValueError, match="no text"):
        text(b"<html><body><h1>Not Found</h1></body></html>", "executive_order")


def test_only_these_combinations_have_a_reader():
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(STATUTE, "json", "statute", "alaska")


S = {"id": "ak-st-44-21-150", "jurisdiction": "alaska", "doc_type": "statute",
     "citation": "AS 44.21.150 – 44.21.170", "title": "Automatic Data Processing"}


def test_a_statute_identity_needs_the_first_and_last_cited_section_as_headings():
    t = text(STATUTE, "statute")
    ing.check_identity(S, t, "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**S, "citation": "AS 44.21.350 – 44.21.390"}, t, "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**S, "citation": "AS 44.21.150 – 44.21.180"}, t, "html")
    ing.check_identity({**S, "citation": "AS 44.21.160"}, t, "html")


R = {"id": "ak-aac-2-05-200", "jurisdiction": "alaska", "doc_type": "rule",
     "citation": "2 AAC 05.200 – 2 AAC 05.290", "title": "Electronic signature verification system"}


def test_a_rule_identity_needs_the_first_and_last_cited_section():
    t = text(RULE, "rule")
    ing.check_identity(R, t, "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**R, "citation": "2 AAC 96.100 – 2 AAC 96.900"}, t, "html")


E = {"id": "ak-ao-284", "jurisdiction": "alaska", "doc_type": "executive_order",
     "citation": "Administrative Order No. 284", "title": "Reorganizing Telecommunication and Information Technology Services"}


def test_an_order_identity_is_the_orders_own_heading_not_a_mention_of_its_number():
    ing.check_identity(E, text(AO284, "executive_order"), "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**E, "citation": "Administrative Order No. 28"}, text(AO284, "executive_order"), "html")
    mention = "Administrative Order No. 360\nThe Governor rescinds Administrative Order No. 284.\n"
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(E, mention, "html")


def test_a_pdf_policy_is_left_to_the_shared_identity_check():
    from src.states import alaska
    assert alaska.check_identity({**E, "doc_type": "policy"}, "x", "PDF") is False


def test_the_conversion_notes_say_how_each_kind_of_page_was_read():
    notes = lambda s, raw, dt: ing.conversion_notes({**s, "doc_type": dt}, "html", text(raw, dt))
    assert "print view" in notes(S, STATUTE, "statute")
    assert "print view" in notes(R, RULE, "rule")
    assert "Governor's" in notes(E, AO284, "executive_order")


def test_a_one_section_print_view_is_the_section_and_passes_its_identity_check():
    raw = (FIX / "as-44-21-020-print.html").read_bytes()
    t = text(raw, "statute")
    assert t.splitlines()[0] == "Sec. 44.21.020. Duties of department."
    assert "(9) administer and supervise a statewide automatic data processing program;" in t
    assert "(10) study, design, implement, and manage the telecommunications systems and services of the state under AS 44.21.305 - 44.21.330." in t
    src = {"id": "x", "jurisdiction": "alaska", "doc_type": "statute", "citation": "AS 44.21.020"}
    ing.check_identity(src, t, "html")

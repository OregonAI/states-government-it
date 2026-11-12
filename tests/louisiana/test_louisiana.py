"""Louisiana through the shared seam (src.ingest / src.states): the Legislature's one-section law pages
(legis.la.gov Law.aspx), the Office of Technology Services' own policy pages (ots.la.gov) and the Division of
Administration's policy pages (doa.la.gov). Fixtures are real bytes fetched on 2026-11-12 through the toolkit
Fetcher, with their page furniture: R.S. 39:15.3 whole, R.S. 39:15.4 (a repealed section) whole, R.S. 39:15.12
whole, the OTS Artificial Intelligence Acceptable Use Policy and Movable Property Tagging Policy pages whole,
the OTS Information Security Policy page whole, and DOA Policy No. 3 whole."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "louisiana"
LA = "louisiana"
LAW = (FIX / "legis-rs-39-15-3.html").read_bytes()
REPEALED = (FIX / "legis-rs-39-15-4-repealed.html").read_bytes()
DEFS = (FIX / "legis-rs-39-15-12.html").read_bytes()
AI = (FIX / "ots-ai-acceptable-use.html").read_bytes()
TAG = (FIX / "ots-movable-property-tagging.html").read_bytes()
ISP = (FIX / "ots-information-security.html").read_bytes()
HR3 = (FIX / "doa-policy-3-acceptable-use.html").read_bytes()


def text(raw, doc_type, host):
    return ing.to_text(raw, "html", doc_type, LA, None, host)


def test_the_state_is_found_by_name():
    assert LA in states.modules(refresh=True)


# ---- statutes: one section per page --------------------------------------------------------

def test_a_law_page_is_its_own_label_then_one_line_per_paragraph():
    lines = text(LAW, "statute", "legis.la.gov").splitlines()
    assert lines[0] == "RS 39:15.3"
    assert lines[1] == "§15.3. Office of technology services; offices and staff; duties"
    assert lines[2].startswith("A. The office of technology services shall consist of executive offices")
    assert lines[2].endswith("operation.")          # the paragraph wrapped over three source lines is one line
    assert lines[-1].endswith("Acts 2021, No. 288, §2.")


def test_the_page_furniture_of_a_law_page_is_not_text():
    t = text(LAW, "statute", "legis.la.gov")
    for furniture in ("Sign-Up", "Scheduled Meetings", "contact the webmaster", "view next", "WebForm", "Printable"):
        assert furniture not in t


def test_a_repealed_section_keeps_its_line_as_published():
    assert text(REPEALED, "statute", "legis.la.gov").splitlines() == [
        "RS 39:15.4", "§15.4. Repealed by Acts 2013, No. 184, §8(B)."]


def test_a_page_that_is_not_a_law_page_is_refused():
    with pytest.raises(ValueError):
        text(AI, "statute", "legis.la.gov")


def test_the_citation_must_match_the_section_the_page_prints():
    src = {"id": "la-rs-39-15-3", "jurisdiction": LA, "doc_type": "statute", "citation": "R.S. 39:15.3"}
    ing.check_identity(src, text(LAW, "statute", "legis.la.gov"), "html")      # raises when it is not the section
    other = dict(src, citation="R.S. 39:15.2")
    with pytest.raises(ValueError):
        ing.check_identity(other, text(LAW, "statute", "legis.la.gov"), "html")


# ---- OTS policy pages ----------------------------------------------------------------------

def test_an_ots_policy_page_is_its_title_summary_and_body_without_menus_or_footer():
    lines = text(AI, "policy", "ots.la.gov").splitlines()
    assert lines[0] == "Artificial Intelligence Acceptable Use Policy"
    assert lines[1].startswith("Guidelines for responsible, ethical, and secure use of AI technologies")
    assert lines[2] == "Effective Date: September 29, 2025"
    assert "I. POLICY" in lines
    t = "\n".join(lines)
    for furniture in ("Skip to Main Content", "Official Banner", "How Do I?", "Privacy Policy", "Success Stories"):
        assert furniture not in t


def test_list_items_are_marked_and_nested_lists_are_indented():
    t = text(ISP, "policy", "ots.la.gov")
    assert any(l.startswith("- ") or l.startswith("1. ") for l in t.splitlines())
    assert any(l.startswith("  - ") or l.startswith("  1. ") or l.startswith("  a. ") for l in t.splitlines())


def test_a_table_is_one_line_per_row_with_cells_separated():
    t = text(TAG, "policy", "ots.la.gov")
    assert "Class Code Group | Commodity Group Name" in t.splitlines()
    assert "43211500 | Computers" in t.splitlines()


# ---- DOA policy pages ----------------------------------------------------------------------

def test_a_doa_policy_page_is_the_policy_body_only():
    lines = text(HR3, "policy", "doa.la.gov").splitlines()
    assert lines[0] == "Acceptable Use of Information Technology Systems and Networks"
    assert lines[1] == "Division of Administration Policy No. 3"
    assert lines[2] == "EFFECTIVE DATE: January 31, 1994;"
    assert "V. ACCEPTABLE/UNACCEPTABLE USE:" in lines
    t = "\n".join(lines)
    assert "Staff Directory" not in t and "Contact Us" not in t
    assert lines[-1].startswith("NOTE: This policy text is provided online")


def test_the_policy_number_a_doa_page_prints_must_match_the_citation():
    src = {"id": "la-doa-policy-3", "jurisdiction": LA, "doc_type": "policy", "citation": "DOA Policy No. 3",
           "title": "Acceptable Use of Information Technology Systems and Networks",
           "url": "https://doa.la.gov/doa/hr/policies/doa-policies/3-acceptable-use-of-information-technology-systems-and-networks/"}
    ing.check_identity(src, text(HR3, "policy", "doa.la.gov"), "html")
    with pytest.raises(ValueError):
        ing.check_identity(dict(src, citation="DOA Policy No. 4"), text(HR3, "policy", "doa.la.gov"), "html")


def test_a_chapter_heading_printed_before_the_section_stays_and_the_citation_still_matches():
    raw = (FIX / "legis-rs-39-15-7-with-heading.html").read_bytes()
    t = text(raw, "statute", "legis.la.gov")
    lines = t.splitlines()
    assert lines[0] == "RS 39:15.7"
    assert lines[1] != "" and not lines[1].startswith("§")           # the heading the page prints first
    assert any(l.startswith("§15.7. State Cybersecurity and Information Technology Fund") for l in lines)
    src = {"id": "la-rs-39-15-7", "jurisdiction": LA, "doc_type": "statute", "citation": "R.S. 39:15.7"}
    ing.check_identity(src, t, "html")


def test_a_doa_page_whose_body_has_no_title_line_is_still_identified_by_number_and_subject():
    raw = (FIX / "doa-policy-1-it-responsibilities.html").read_bytes()
    t = text(raw, "policy", "doa.la.gov")
    assert t.splitlines()[0] == "Division of Administration Policy No. 1"
    src = {"id": "la-doa-policy-1", "jurisdiction": LA, "doc_type": "policy", "citation": "DOA Policy No. 1",
           "title": "Information Technology Responsibilities",
           "url": "https://doa.la.gov/doa/hr/policies/doa-policies/1-information-technology-responsibilities/"}
    ing.check_identity(src, t, "html")
    with pytest.raises(ValueError):
        ing.check_identity(dict(src, title="Records Retention Policy"), t, "html")


def test_an_executive_order_is_identified_by_its_own_heading_line_not_by_a_mention_of_its_number():
    raw = (FIX / "jml-26-107.pdf").read_bytes()
    t = ing.to_text(raw, "pdf", "executive_order", LA, None, "gov.louisiana.gov")
    src = {"id": "la-eo-jml-26-107", "jurisdiction": LA, "doc_type": "executive_order",
           "citation": "Executive Order JML 26-107"}
    ing.check_identity(src, t, "pdf")
    with pytest.raises(ValueError):
        ing.check_identity(dict(src, citation="Executive Order JML 26-020"), t, "pdf")
    # the heading is required: the number mentioned in prose is not enough
    with pytest.raises(ValueError):
        ing.check_identity(src, "A renewal of JML 26-107 is ordered.\n", "pdf")


def test_the_longest_ots_page_is_whole_and_its_footer_is_not_text():
    assert b"</footer>" in ISP                       # the fixture keeps the page's footer
    t = text(ISP, "policy", "ots.la.gov")
    for furniture in ("Skip to Main Content", "Official Banner", "Privacy Policy", "Success Stories"):
        assert furniture not in t
    assert t.splitlines()[-1].strip()

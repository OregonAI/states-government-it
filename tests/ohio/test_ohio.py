"""Seam: src.ingest / src.states for Ohio: the Ohio Laws pages on codes.ohio.gov (a Revised Code section or
chapter, an Administrative Code chapter) and the identity check of those pages. Fixtures are the real pages
the site served on 2026-11-12, whole, with page furniture."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "ohio"
SEC = (FIX / "orc-section-125.18.html").read_bytes()
SEC_SHORT = (FIX / "orc-section-126.506.html").read_bytes()
ORC_CH = (FIX / "orc-chapter-5922.html").read_bytes()
OAC_CH = (FIX / "oac-chapter-123-4.html").read_bytes()


def text(raw, doc_type="statute"):
    return ing.to_text(raw, "html", doc_type, "ohio")


def test_section_page_opens_with_its_heading_then_effective_date_and_the_law():
    lines = text(SEC).splitlines()
    assert lines[0] == "Section 125.18 | Office of information technology - duties of director - contracts."
    assert "Effective: October 3, 2023" in lines
    assert "Latest Legislation: House Bill 33 - 135th General Assembly" in lines
    assert lines[lines.index("Latest Legislation: House Bill 33 - 135th General Assembly") + 1].startswith(
        "(A) There is hereby established the office of information technology")


def test_section_page_drops_menus_search_pdf_link_pager_and_last_updated_note():
    t = text(SEC)
    for furniture in ("Skip to main content", "Go To Section", "Download Authenticated PDF", "Related Sites",
                      "Last updated", "Expand All", "Revised Code Keywords", "Disclaimer",
                      "Legislative Service Commission staff updates"):
        assert furniture not in t
    assert "<" not in t and "&nbsp;" not in t and "\xa0" not in t


def test_section_page_keeps_version_history_lines_without_the_view_links():
    t = text(SEC_SHORT)
    assert "Available Versions of this Section" in t
    assert "October 16, 2009 \u2013 House Bill 1 - 128th General Assembly" in t
    assert "View October 16, 2009 Version" not in t


def test_section_text_collapses_the_source_double_spaces():
    t = text(SEC_SHORT)
    assert "(A) Each state agency shall participate in information technology consolidation projects" in t


def test_chapter_page_has_chapter_heading_then_each_section_heading_with_a_blank_line_before():
    lines = text(ORC_CH).splitlines()
    assert lines[0] == "Chapter 5922 | Cyber Security Reserve" or lines[0].startswith("Chapter 5922 | ")
    heads = [i for i, l in enumerate(lines) if l.startswith("Section 5922.")]
    assert len(heads) == 8
    assert all(lines[i - 1] == "" for i in heads)


def test_rule_chapter_keeps_supplemental_information_of_each_rule():
    t = text(OAC_CH, "rule")
    assert t.splitlines()[0] == "Chapter 123-4 | Accessing Confidential Personal Information"
    assert "Rule 123-4-01 | Definitions." in t
    assert "Promulgated Under: 119.03" in t
    assert "Five Year Review Date:" in t and "Prior Effective Dates:" in t
    assert t.count("Rule 123-4-0") >= 5


def test_other_formats_are_refused_by_the_module():
    with pytest.raises(ValueError):
        ing.to_text(b"x", "json", "statute", "ohio")


def test_page_without_the_laws_region_is_an_error():
    with pytest.raises(ValueError):
        text(b"<html><body><main>no laws</main></body></html>")


def seed(doc_type, citation, title, **kw):
    return {"id": "x", "jurisdiction": "ohio", "doc_type": doc_type, "citation": citation, "title": title, **kw}


def test_identity_accepts_the_cited_section_and_refuses_another():
    s = seed("statute", "R.C. 125.18", "Section 125.18")
    from src.states import check_identity
    check_identity(s, text(SEC), "html")
    with pytest.raises(ValueError, match="not R.C. 126.506"):
        check_identity(seed("statute", "R.C. 126.506", "x"), text(SEC), "html")


def test_identity_accepts_the_cited_chapter_and_refuses_a_section_page():
    from src.states import check_identity
    check_identity(seed("statute", "R.C. ch. 5922", "x"), text(ORC_CH), "html")
    with pytest.raises(ValueError):
        check_identity(seed("statute", "R.C. ch. 5922", "x"), text(SEC), "html")


def test_identity_of_a_rule_chapter():
    from src.states import check_identity
    check_identity(seed("rule", "OAC ch. 123-4", "x"), text(OAC_CH, "rule"), "html")
    with pytest.raises(ValueError):
        check_identity(seed("rule", "OAC ch. 123:3-1", "x"), text(OAC_CH, "rule"), "html")


def test_statute_and_rule_pages_print_no_document_level_effective_date():
    from src import states
    assert states.effective_date(text(OAC_CH, "rule"), "rule", "ohio") is None


# ---- DAS policy pages and Governor executive order pages (das.ohio.gov, governor.ohio.gov) ----
# Fixtures are the whole pages the sites served on 2026-11-12, with menus, scripts and footers.
POL_17 = (FIX / "das-policy-it-17.html").read_bytes()
POL_01 = (FIX / "das-policy-it-01.html").read_bytes()
POL_16 = (FIX / "das-policy-it-16.html").read_bytes()
EO_2022 = (FIX / "governor-eo-2022-07D.html").read_bytes()
EO_2019 = (FIX / "governor-eo-2019-15D.html").read_bytes()


def ptext(raw, doc_type="policy"):
    return ing.to_text(raw, "html", doc_type, "ohio")


def test_policy_page_opens_with_its_heading_and_the_issuing_block():
    lines = ptext(POL_17).splitlines()
    assert lines[0] == "IT-17 Use of Artificial Intelligence in State of Ohio Solutions"
    assert lines[1] == ""
    assert lines[2:6] == ["State of Ohio Administrative Policy", "No: IT-17 Information Technology",
                          "Effective: January 5, 2026", "Issued By: Kathleen C. Madden, Director"]


def test_policy_page_numbers_its_lists_the_way_the_page_displays_them():
    lines = ptext(POL_17).splitlines()
    assert "I. Purpose" in lines and "III. Policy" in lines
    assert "A. AI Solution Development" in lines
    assert any(l.startswith("1. Defining a formal process for identifying") for l in lines)
    assert any(l.startswith("a. Reviewing and testing any AI generated output") for l in lines)


def test_policy_page_drops_menus_styles_scripts_and_cms_comments():
    t = ptext(POL_17)
    for furniture in ("Skip to Navigation", "Web Content Viewer", "Share this", "romanH2", "IBM WebSphere",
                      "Components >", "Expand All Sections", "Ohio Checkbook", "odx-attachment"):
        assert furniture not in t
    assert "<" not in t and "&nbsp;" not in t and "\xa0" not in t and "  " not in t


def test_policy_page_keeps_the_revision_history_table_one_row_per_line():
    t = ptext(POL_17)
    assert "Date | Description of Change" in t
    assert "12/04/2023 | Original Policy" in t.splitlines()


def test_policy_page_keeps_cell_lists_on_one_line_and_the_footnotes():
    t = ptext(POL_01)
    assert "Footnotes" in t
    assert any(l.startswith("1. Back to Content [1]: A domain ID is a series of letters") for l in t.splitlines())
    row = next(l for l in t.splitlines() if l.startswith("Enterprise IT Procedures | General Assembly"))
    assert "to obtain a DAS OIT-provided service; or" in row


def test_policy_page_table_with_paragraph_cells_is_read_row_by_row():
    t = ptext(POL_16)
    assert "Document Name | Location" in t
    assert any(l.startswith("State of Ohio Procurement Manual | ") for l in t.splitlines())


def test_executive_order_page_opens_with_its_heading_then_title_and_ends_with_the_attest_block():
    lines = ptext(EO_2022, "executive_order").splitlines()
    assert lines[0] == "Executive Order 2022-07D"
    assert lines[2] == "Creation of the Cybersecurity Strategic Advisor"
    assert lines[-1] == "Frank LaRose, Secretary of State" and lines[-2] == "ATTEST:"
    t = "\n".join(lines)
    assert "Signed EO 2022-07D.pdf" not in t and "Share this" not in t and "News Releases" not in t
    assert "- Ohio Department of Higher Education, including the Ohio Technology Consortium." in t


def test_executive_order_page_numbers_its_directives():
    t = ptext(EO_2019, "executive_order")
    assert "1. The InnovateOhio Platform is hereby established" in t
    assert "a. Providing a common and standard digital platform" in t


def test_page_without_a_content_region_is_an_error_for_policies_and_orders():
    for dt in ("policy", "executive_order"):
        with pytest.raises(ValueError):
            ptext(b"<html><body><h1>x</h1></body></html>", dt)


def test_policy_identity_checks_the_heading_line_not_a_mention():
    from src.states import check_identity
    s = seed("policy", "IT-17", "Use of Artificial Intelligence in State of Ohio Solutions")
    check_identity(s, ptext(POL_17), "html")
    with pytest.raises(ValueError, match="not IT-17"):
        check_identity(s, ptext(POL_01), "html")      # IT-01's text mentions other policies, opens IT-01
    with pytest.raises(ValueError):
        check_identity(s, "IT-16 Major Project Governance Policy\nSee IT-17 for more.\n", "html")


def test_order_identity_checks_the_heading_line_not_a_mention():
    from src.states import check_identity
    s = seed("executive_order", "Executive Order 2022-07D", "x")
    check_identity(s, ptext(EO_2022, "executive_order"), "html")
    with pytest.raises(ValueError, match="not Executive Order 2022-07D"):
        check_identity(s, ptext(EO_2019, "executive_order"), "html")
    with pytest.raises(ValueError):
        check_identity(s, "Executive Order 2019-15D\nThis rescinds Executive Order 2022-07D.\n", "html")


def test_policy_effective_date_is_the_one_the_page_prints_and_an_order_has_none():
    from src import states
    assert states.effective_date(ptext(POL_17), "policy", "ohio") == "2026-01-05"
    assert states.effective_date(ptext(POL_16), "policy", "ohio") == "2026-09-01"
    assert states.effective_date(ptext(EO_2022, "executive_order"), "executive_order", "ohio") is None


def test_pdf_standard_identity_uses_its_number_in_the_text():
    from src.states import check_identity
    check_identity(seed("standard", "ITS-SEC-02", "Enterprise Security Controls Framework"),
                   "State of Ohio\nITS-SEC-02\nIT Standard\nEnterprise Security Controls Framework\n", "pdf")
    with pytest.raises(ValueError):
        check_identity(seed("standard", "ITS-SEC-02", "Enterprise Security Controls Framework"),
                       "State of Ohio\nITS-SEC-01\nIT Standard\nEnterprise Security Controls Framework\n", "pdf")


def test_conversion_notes_describe_the_site_the_page_came_from():
    from src import states
    pol = states.hook("ohio", "notes")(seed("policy", "IT-17", "x"), "html", ptext(POL_17))
    assert "das.ohio.gov" in pol and "codes.ohio.gov" not in pol and "list numbers" in pol
    eo = states.hook("ohio", "notes")(seed("executive_order", "Executive Order 2022-07D", "x"), "html",
                                      ptext(EO_2022, "executive_order"))
    assert "governor.ohio.gov" in eo and "codes.ohio.gov" not in eo and "signed PDF" in eo
    law = states.hook("ohio", "notes")(seed("statute", "R.C. 125.18", "x"), "html", text(SEC))
    assert "codes.ohio.gov" in law

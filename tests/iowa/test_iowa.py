"""Seam: src.ingest / src.states for Iowa: the policy portal's HTML policy pages (policies.iowa.gov/dom/policy/<slug>/),
and the identity and version checks of the Legislature's per-section Code PDFs, the Iowa Administrative Code chapter
PDFs and the scanned executive orders. Fixtures are real bytes served on 2026-11-11: a whole policy page with its
furniture, and the text of the real PDFs and of a real OCR reading (head and tail, cut, never re-typed)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "iowa"
POLICY = (FIX / "policy-generative-ai.html").read_bytes()
CODE = (FIX / "code-8.77.txt").read_text()
RULE = (FIX / "iac-129.8.txt").read_text()
EO87 = (FIX / "eo-87-ocr.txt").read_text()


def policy_text():
    return ing.to_text(POLICY, "html", "policy", "iowa", None, "policies.iowa.gov")


def test_policy_page_text_has_the_title_the_published_version_line_and_the_policy_body():
    lines = policy_text().splitlines()
    assert lines[0] == "Generative Artificial Intelligence (AI) Policy"
    assert lines[1] == "Published: January 14, 2026 | Updated: January 14, 2026 | Version 7"
    assert "Policy Number: ENTERPRISE PY-AI" in lines
    assert "Authority: Iowa Admin. Code r. 129-8.4." in lines
    assert "1. Purpose" in lines and "4. Policy" in lines


def test_policy_page_text_drops_the_portal_summary_menus_and_footer():
    t = policy_text()
    for furniture in ("Quick Summary", "Skip to main content", "Policy Categories", "Breadcrumb", "x-cloak",
                      "Access published policies", "hcr-enterprises"):
        assert furniture not in t
    assert "<" not in t and "&nbsp;" not in t and "\xa0" not in t and "&rsquo;" not in t
    assert "Agency’s compliance" in t        # entities decoded, apostrophe kept


def test_policy_page_without_a_policy_body_is_refused():
    with pytest.raises(ValueError, match="policy-content"):
        ing.to_text(b"<html><body><main>nothing</main></body></html>", "html", "policy", "iowa", None, "policies.iowa.gov")


def test_policy_page_effective_date_is_read_from_the_policy_body_label():
    assert states.effective_date(policy_text(), "policy", "iowa") == "2025-03-31"


def src(**kw):
    base = {"id": "x", "jurisdiction": "iowa", "doc_type": "statute", "title": "t", "citation": "Iowa Code 8.77"}
    base.update(kw)
    return base


def test_statute_section_must_print_its_own_heading_line():
    s = src(identity_text="8.77 Information technology services")
    states.check_identity(s, CODE, "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(src(identity_text="8.93 Cybersecurity"), CODE, "pdf")


def test_statute_identity_is_not_satisfied_by_a_mere_mention_of_the_section_number():
    mention = "  1. See section 8.77 Information technology services for the powers.\n"
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(src(identity_text="8.77 Information technology services"), mention, "pdf")


def test_rule_chapter_must_print_its_chapter_and_title_lines():
    s = src(doc_type="rule", identity_text="CHAPTER 8", identity_title="INFORMATION TECHNOLOGY GOVERNANCE")
    states.check_identity(s, RULE, "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(src(doc_type="rule", identity_text="CHAPTER 10",
                                  identity_title="PROCUREMENT OF INFORMATION TECHNOLOGY"), RULE, "pdf")


def test_executive_order_must_print_its_own_heading_line():
    s = src(doc_type="executive_order", identity_text="EXECUTIVE ORDER NUMBER EIGHTY-SEVEN")
    states.check_identity(s, EO87, "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(src(doc_type="executive_order", identity_text="EXECUTIVE ORDER NUMBER EIGHTY-EIGHT"),
                              EO87, "pdf")
    mention = "pursuant to EXECUTIVE ORDER NUMBER EIGHTY-SEVEN the Governor directs\n"
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(s, mention, "pdf")


def test_standard_pdf_must_print_its_own_title():
    s = src(doc_type="standard", title="Data Backup Standard", citation="State of Iowa Data Backup Operational Standard",
            identity_text="State of Iowa - Data Backup Operational Standard")
    states.check_identity(s, "State of Iowa - Data Backup Operational Standard\nSeptember 2, 2014", "pdf")
    with pytest.raises(ValueError):
        states.check_identity(s, "something else", "pdf")


def test_source_version_of_a_statute_section_is_the_code_edition_its_footer_prints():
    assert states.source_version(CODE, "statute", "iowa", "pdf") == "Iowa Code 2026"


def test_source_version_of_a_rule_chapter_is_the_iac_date_its_header_prints():
    assert states.source_version(RULE, "rule", "iowa", "pdf") == "IAC 2/5/25"


def test_source_version_of_other_documents_is_empty():
    assert states.source_version(EO87, "executive_order", "iowa", "pdf") == ""


def test_html_policy_notes_say_the_page_was_read_not_the_pdf():
    n = ing._conversion_notes({"id": "x", "jurisdiction": "iowa", "doc_type": "policy"}, "html", policy_text())
    assert "policies.iowa.gov" in n and "Quick Summary" in n and "PDF" in n


# ---- standards: the identity check matches the instrument's own heading, not a mention ----
O1033 = (FIX / "ocio-1033.txt").read_text()
O1034 = (FIX / "ocio-1034.txt").read_text()
O1053 = (FIX / "ocio-1053.txt").read_text()
O1054 = (FIX / "ocio-1054.txt").read_text()
STD1033 = "State of Iowa Enterprise Information Security Standard"
STD1053 = "Information Technology Governance Document Taxonomy"


def std(text, **kw):
    return src(doc_type="standard", identity_text=text, **kw)


def test_standard_accepts_its_own_heading_even_with_a_defined_term_after_it():
    states.check_identity(std(STD1033), O1033, "pdf")
    states.check_identity(std(STD1053), O1053, "pdf")  # 'Taxonomy ("Taxonomy")'


def test_standard_refuses_another_standards_bytes_that_only_contain_its_title_as_a_prefix():
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(std(STD1033), O1034, "pdf")  # '... Information Security Compliance Standard'


def test_standard_refuses_the_bytes_of_a_standard_that_only_cites_it():
    assert "Governance Document Taxonomy" in O1054
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(std(STD1053), O1054, "pdf")


def test_standard_title_wrapped_over_two_lines_is_still_its_heading():
    wrapped = "      State of Iowa Enterprise Email\n          Security Standard\n     December 14, 2011\n"
    states.check_identity(std("State of Iowa Enterprise Email Security Standard"), wrapped, "pdf")


# ---- the version of a policy page is read from either place the portal prints it ----
def test_policy_page_that_prints_only_a_version_name_keeps_it_on_the_second_line():
    t = ing.to_text((FIX / "policy-background-investigation.html").read_bytes(), "html", "policy", "iowa", None,
                    "policies.iowa.gov")
    assert t.splitlines()[1].endswith("| 1.0")


def test_policy_page_whose_version_name_is_the_policy_number_gets_no_version():
    t = ing.to_text((FIX / "policy-digital-accessibility.html").read_bytes(), "html", "policy", "iowa", None,
                    "policies.iowa.gov")
    assert "ADMN.303.02.E" not in t.splitlines()[1]
    assert t.splitlines()[1].count(" | ") == 1  # published | updated, no version


def test_policy_notes_do_not_claim_a_version_the_text_does_not_hold():
    s = {"id": "x", "jurisdiction": "iowa", "doc_type": "policy"}
    n = ing._conversion_notes(s, "html", "Title\nPublished: A | Updated: B\n")
    assert "its version are kept" not in n and "prints no version" in n
    n = ing._conversion_notes(s, "html", "Title\nPublished: A | Updated: B | Version 7\n")
    assert "its version are kept" in n

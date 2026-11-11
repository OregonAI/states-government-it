"""Seams: src.ingest.derive / check_identity / effective_date / source_version for Colorado's
administrative rules (the Code of Colorado Regulations, www.sos.state.co.us/CCR) and for the Office of
Information Technology's policies published as Google Drive PDFs.

www.sos.state.co.us challenges the toolkit's Python client and answers system curl, with the same
User-Agent, HTTP 200 (see docs/research/07). The rule PDFs are the official version of a rule ("The PDF
document constitutes the official version of the rule and shall govern in all cases", the CCR page says).
Fixtures are real bytes fetched 2026-11-11 through the toolkit Fetcher with curl_on_challenge=True: the
PDF of 8 CCR 1501-9 (a two-page rule in force), the PDF of 8 CCR 1501-6 (the one-page notice that the rule
was repealed effective 04/14/2026), and OIT's Vendor Selection Standard for Major IT Projects (a Google
Drive PDF linked from OIT's Technical Standards & Policies page)."""
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent / "fixtures"
RULE_PDF = (FIX / "ccr-8-1501-9.pdf").read_bytes()
REPEALED_PDF = (FIX / "ccr-8-1501-6-repealed.pdf").read_bytes()
VENDOR_PDF = (FIX / "oit-vendor-selection-standard.pdf").read_bytes()

RULE = {"id": "co-ccr-8-1501-9", "format": "pdf", "doc_type": "rule", "jurisdiction": "colorado",
        "url": "https://www.sos.state.co.us/CCR/GenerateRulePdf.do?ruleVersionId=7073&fileName=8%20CCR%201501-9",
        "citation": "8 CCR 1501-9",
        "title": "Colorado Rules Regarding Electronic Transactions by Colorado Governmental Agencies"}
VENDOR = {"id": "co-oit-vendor-selection-standard", "format": "pdf", "doc_type": "standard",
          "jurisdiction": "colorado", "url": "https://drive.google.com/file/d/1iuPwfRpcwXxHVcsSlDe1jRCe9HA4rF8T/view",
          "citation": "OIT-FinSvc-100", "title": "Vendor Selection Standard for Major IT Projects"}


def test_a_ccr_rule_pdf_is_read_as_layout_text_from_cover_to_editors_notes():
    fmt, text = ing.derive(RULE, RULE_PDF)
    assert fmt == "pdf"
    assert "8 CCR 1501-9" in text
    assert "R7      Suspension of Electronic Transactions" in text
    assert text.rstrip().splitlines()[-1].strip() == "2"
    assert "New rule eff. 03/20/2017." in text


def test_effective_date_is_the_last_eff_line_of_the_rules_history():
    _, text = ing.derive(RULE, RULE_PDF)
    assert ing.effective_date(text, "rule", "colorado") == "2017-03-20"
    history = "Editor’s Notes\n\nHistory\nNew rule eff. 04/14/2024.\nEntire rule eff. 06/30/2025.\n"
    assert ing.effective_date(history, "rule", "colorado") == "2025-06-30"
    assert ing.effective_date("no history here", "rule", "colorado") is None
    assert ing.source_version(history, "rule", "colorado") == ""


def test_a_rule_that_is_not_the_cited_one_is_refused():
    other = dict(RULE, citation="8 CCR 1501-5")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(other, RULE_PDF)
    retitled = dict(RULE, title="Rules in Support of the Colorado Information Security Act")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(retitled, RULE_PDF)


def test_a_repealed_rule_is_refused_because_it_is_not_in_force():
    src = dict(RULE, id="co-ccr-8-1501-6", citation="8 CCR 1501-6",
               title="Rules in Support of the Office of Information Technology")
    with pytest.raises(ValueError, match="repealed"):
        ing.derive(src, REPEALED_PDF)


def test_an_oit_policy_pdf_is_dated_from_its_own_header():
    fmt, text = ing.derive(VENDOR, VENDOR_PDF)
    assert fmt == "pdf"
    assert ing.effective_date(text, "standard", "colorado") == "2018-11-30"


def test_an_oit_policy_pdf_must_print_its_title_in_its_head_and_name_oit():
    nowhere = dict(VENDOR, title="Delegation of Authority Policy")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(nowhere, VENDOR_PDF)
    # a text that is not OIT's, whatever it is called
    with pytest.raises(ValueError, match="OIT"):
        ing.check_identity(VENDOR, "Vendor Selection Standard for Major IT Projects\n\nA county's standard.\n", "pdf")
    # a document that only cites the title further down is not that document
    body = "Some other policy\n" * 200 + "The Office of Information Technology: Vendor Selection Standard for Major IT Projects\n"
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(VENDOR, body, "pdf")


@pytest.mark.parametrize("printed, want", [
    ("Updated: Feb 23, 2026", "Updated: Feb 23, 2026"),
    ("Published January 2020", "Published January 2020"),
    ("nothing dated", ""),
])
def test_an_oit_policy_that_prints_no_effective_date_gives_its_updated_or_published_line(printed, want):
    assert ing.source_version(f"Title\n\n{printed}\n", "policy", "colorado") == want


def test_a_ccr_document_says_which_copy_it_is_and_where_its_date_comes_from():
    _, text = ing.derive(RULE, RULE_PDF)
    notes = ing.conversion_notes(RULE, "pdf", text)
    assert "pdftotext -layout" in notes
    assert "official version" in notes and "Secretary of State" in notes
    assert "scattered" in notes                      # the cover's logotype comes out as letter fragments
    assert "last `eff.` line" in notes
    _, vtext = ing.derive(VENDOR, VENDOR_PDF)
    assert "Secretary of State" not in ing.conversion_notes(VENDOR, "pdf", vtext)


def test_a_partial_repeal_in_the_history_does_not_become_the_effective_date():
    history = "Editor's Notes\n\nHistory\n\nEntire rule eff. 06/30/2025.\nRule 11.3 repealed eff. 01/01/2026.\n"
    assert ing._co_effective_date(history, "rule") == "2025-06-30"

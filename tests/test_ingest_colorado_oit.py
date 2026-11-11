"""Seams: src.ingest.derive / check_identity / effective_date / source_version / conversion_notes for the
Office of Information Technology's instruments as OIT's live site lists them (read 2026-11-11 through the
toolkit Fetcher, whose User-Agent is the crawler form of toolkit ADR-0019).

Fixtures are real bytes from that run. The three index pages (technical-standards, policies-governance,
standards-policies-guides) are kept whole, with their menus and footers. TS-APP-005 and TS-APP-010 are Google
Drive PDFs fetched from the download form of the file OIT links; TS-APP-010 prints its version as
'3.01 (Draft)'. The Statewide GenAI Agency Responsibilities page is a Drupal page kept whole."""
import re
from pathlib import Path

import pytest
import yaml

from src import ingest as ing

FIX = Path(__file__).resolve().parent / "fixtures"
ROOT = FIX.parent.parent
APP005_PDF = (FIX / "oit-ts-app-005.pdf").read_bytes()
APP010_PDF = (FIX / "oit-ts-app-010-draft.pdf").read_bytes()
PAGE = (FIX / "oit-genai-agency-responsibilities.html").read_bytes()

APP005 = {"id": "co-oit-ts-app-005", "format": "pdf", "doc_type": "standard", "jurisdiction": "colorado",
          "url": "https://drive.google.com/uc?export=download&id=1xt85_XMCGtAFyp4OtkIHd8GlpzsueQvv",
          "citation": "TS-APP-005", "document_id": "TS-APP-005",
          "title": "Secure Application Software Standards & Configuration Management",
          "oit_link": "https://drive.google.com/file/d/1xt85_XMCGtAFyp4OtkIHd8GlpzsueQvv/view?usp=sharing",
          "found_via": "https://oit.colorado.gov/standards-policies-guides/technical-standards"}
AGENCY = {"id": "co-oit-genai-agency-responsibilities", "format": "html", "doc_type": "policy",
          "jurisdiction": "colorado", "citation": "Statewide GenAI Agency Responsibilities",
          "url": "https://oit.colorado.gov/standards-policies-guides/guide-to-artificial-intelligence/statewide-genai-agency-responsibilities",
          "title": "Statewide GenAI Agency Responsibilities"}


# ---- a standard PDF that prints a Document ID header ------------------------------------------

def test_a_standard_pdf_is_read_and_its_header_names_its_id_and_oit():
    fmt, text = ing.derive(APP005, APP005_PDF)
    assert fmt == "pdf"
    assert "Document ID" in text and "TS-APP-005" in text


def test_the_effective_date_is_the_printed_table_row_not_the_last_updated_date():
    _, text = ing.derive(APP005, APP005_PDF)
    assert ing.effective_date(text, "standard", "colorado") == "2015-11-19"      # Last Updated is 04/02/2026
    assert ing.effective_date("  Effective Date    07-01-2026\n  Last Updated   07-01-2026\n", "standard", "colorado") == "2026-07-01"
    assert ing.effective_date("  Effective Date    N/A\n", "standard", "colorado") is None


def test_the_source_version_is_the_printed_version_and_last_updated():
    _, text = ing.derive(APP005, APP005_PDF)
    assert ing.source_version(text, "standard", "colorado") == "3.0, last updated 04/02/2026"
    assert ing.source_version("  Version     4.01\n  Last Updated   Not documented (Draft)\n",
                              "standard", "colorado") == "4.01"
    assert ing.source_version("  Version     1.0\n", "policy", "colorado") == "1.0"


def test_a_pdf_that_prints_a_different_document_id_is_refused():
    other = dict(APP005, document_id="TS-APP-009", citation="TS-APP-009")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(other, APP005_PDF)


def test_a_pdf_whose_issuing_authority_is_not_oit_is_refused():
    _, text = ing.derive(APP005, APP005_PDF)
    other = text.replace("Governor’s Office of Information Technology (OIT)", "Department of Somewhere")
    other = other.replace("OIT", "XXX").replace("Office of Information Technology", "Office")
    with pytest.raises(ValueError, match="OIT"):
        ing.check_identity(APP005, other, "pdf")
    # OIT named in the body but not as issuing authority in the header is still refused
    moved = (text.replace("Issuing Authority", "Issuing Body ")
             .replace("Governor’s Office of Information Technology (OIT)", "Department of Somewhere") + "\nOIT staff.\n")
    with pytest.raises(ValueError, match="Issuing Authority"):
        ing.check_identity(APP005, moved, "pdf")


def test_a_version_marked_draft_is_refused_as_not_in_force():
    src = dict(APP005, id="co-oit-ts-app-010", citation="TS-APP-010", document_id="TS-APP-010",
               title="Code Repositories (Repository Manager)")
    with pytest.raises(ValueError, match="Draft"):
        ing.derive(src, APP010_PDF)


def test_the_notes_give_both_the_link_oit_prints_and_the_form_fetched():
    _, text = ing.derive(APP005, APP005_PDF)
    notes = ing.conversion_notes(APP005, "pdf", text)
    assert APP005["oit_link"] in notes and "uc?export=download&id=1xt85_XMCGtAFyp4OtkIHd8GlpzsueQvv" in notes
    assert APP005["found_via"] in notes


# ---- the Statewide GenAI Agency Responsibilities page ---------------------------------------

def test_the_agency_responsibilities_page_is_its_heading_and_body_without_the_site_furniture():
    fmt, text = ing.derive(AGENCY, PAGE)
    assert fmt == "html"
    lines = text.splitlines()
    assert lines[0] == "Statewide GenAI Agency Responsibilities"
    assert "Testing must be conducted based on the risk level assigned by OIT:" in text
    assert "OIT Responsibilities" in text and "Enforce compliance." in text
    for furniture in ("Individual User Responsibilities", "Case Study", "Home", "linkedin", "oit@state.co.us",
                      "Toggle", "<", "Skip to"):
        assert furniture not in text, furniture


def test_the_agency_responsibilities_page_says_what_was_taken_and_prints_no_date():
    _, text = ing.derive(AGENCY, PAGE)
    notes = ing.conversion_notes(AGENCY, "html", text)
    assert "Office of Information Technology's web page" in notes and "language selector" in notes
    assert ing.effective_date(text, "policy", "colorado") is None
    assert ing.source_version(text, "policy", "colorado") == ""


def test_the_agency_responsibilities_page_refuses_a_layout_it_does_not_know():
    with pytest.raises(ValueError, match="layout"):
        ing.derive(AGENCY, b"<html><body><h1>Statewide GenAI Agency Responsibilities</h1><p>OIT</p></body></html>")


# ---- the seed list against OIT's live index pages ------------------------------------------

def _listed_files(page: str) -> dict[str, str]:
    """Every Google Drive file a page links: id -> the link as printed."""
    html = (FIX / page).read_text(encoding="utf-8")
    main = html[html.index("<main"):html.index("</main>")]
    return {m.group(2): m.group(1) for m in
            re.finditer(r'href="(https://drive\.google\.com/file/d/([^/"]+)/[^"]*)"', main)}


MANIFEST = (ROOT / "_meta" / "source-manifest.yml").read_text(encoding="utf-8")


@pytest.mark.parametrize("page", ["oit-technical-standards.html", "oit-policies-governance.html",
                                  "oit-standards-policies-guides.html"])
def test_every_file_oit_lists_is_in_the_seed_list_as_the_link_oit_prints_seeded_or_recorded_as_left_out(page):
    listed = _listed_files(page)
    assert listed
    missing = sorted(link for link in listed.values() if link not in MANIFEST)
    assert not missing, f"listed by OIT but neither seeded nor recorded as left out: {missing}"


def test_a_last_updated_row_that_says_draft_is_refused_even_when_the_version_does_not():
    """TS-DBS-001 prints 'Version 4.01' and 'Last Updated  Not documented (Draft)': a file that calls itself a
    draft anywhere in its header table is not shown to be in force (spec rule 6)."""
    _, text = ing.derive(APP005, APP005_PDF)
    drafted = re.sub(r"^([ \t]*Last Updated[ \t]{2,}).*$", r"\1Not documented (Draft)", text, count=1, flags=re.M)
    assert drafted != text
    with pytest.raises(ValueError, match="Last Updated"):
        ing.check_identity(APP005, drafted, "pdf")

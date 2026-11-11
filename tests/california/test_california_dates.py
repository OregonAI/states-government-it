"""Seam: src.ingest.effective_date / source_version for California instruments, read from the text
as `derive` makes it. Fixtures are real bytes (fetched 2026-11-11 through the Fetcher with its curl
transport): an ITPL PDF (ITPL 09-03: DATE ISSUED printed in capitals, in a second column), a Technology
Letter PDF (TL 21-01: DATE ISSUED prints only a month and year), a Technology Letter page (TL 26-01:
the month and year are line 2), a SIMM page (SIMM 40A: 'Revised May 2023' in the heading) and an
executive order PDF (N-5-26: 'this 30th day of March 2026')."""
from pathlib import Path

from src import ingest as ing
from src.states import california

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "california"
ITPL = ing.to_text((FIX / "cdt-itpl-09-03.pdf").read_bytes(), "pdf", "policy", "california")
TL_PDF = ing.to_text((FIX / "cdt-tl-21-01.pdf").read_bytes(), "pdf", "policy", "california")
TL_PAGE = california.cdt_html_to_text((FIX / "cdt-tl-26-01.html").read_bytes())
SIMM_PAGE = california.cdt_html_to_text((FIX / "cdt-simm-40a.html").read_bytes())
EO = ing.to_text((FIX / "eo-n-5-26.pdf").read_bytes(), "pdf", "executive_order", "california")
CA = "california"


def test_an_itpl_prints_the_day_it_was_issued():
    assert ing.effective_date(ITPL, "policy", CA) == "2009-04-15"
    assert ing.source_version(ITPL, "policy", CA) == ""


def test_a_letter_that_prints_only_month_and_year_gets_a_version_not_an_invented_day():
    assert ing.effective_date(TL_PDF, "policy", CA) is None
    assert ing.source_version(TL_PDF, "policy", CA) == "March 2021"


def test_a_technology_letter_page_prints_its_month_on_line_two():
    assert ing.effective_date(TL_PAGE, "policy", CA) is None
    assert ing.source_version(TL_PAGE, "policy", CA) == "February 2026"


def test_a_simm_page_heading_carries_its_revision_month():
    assert ing.source_version(SIMM_PAGE, "policy", CA) == "Revised May 2023"


def test_an_executive_order_is_dated_by_the_day_the_governor_signed_it():
    assert ing.effective_date(EO, "executive_order", CA) == "2026-03-30"


def test_other_states_and_undated_text_are_unchanged():
    assert ing.effective_date(ITPL, "policy") is None
    assert ing.effective_date(ITPL, "policy", "oregon") is None
    assert ing.source_version(TL_PAGE, "policy", "oregon") == ""
    assert ing.effective_date("Nothing dated here.\n", "policy", CA) is None
    assert ing.source_version("Nothing dated here.\n", "policy", CA) == ""


def test_the_conversion_notes_say_what_the_effective_date_is():
    src = {"jurisdiction": CA, "doc_type": "executive_order", "url": "https://www.gov.ca.gov/x.pdf"}
    assert "date the Governor signed" in ing.conversion_notes(src, "pdf", EO)
    src = {"jurisdiction": CA, "doc_type": "policy", "url": "https://www.cdt.ca.gov/x.pdf"}
    assert "date the letter prints as issued" in ing.conversion_notes(src, "pdf", ITPL)
    assert "date issued" not in ing.conversion_notes(src, "pdf", TL_PDF)


def test_a_simm_pdf_cover_prints_its_month_under_the_title():
    cover = ing.to_text((FIX / "cdt-simm-19e-1-pages-1-2.pdf").read_bytes(), "pdf", "policy", "california")
    assert ing.source_version(cover, "policy", CA) == "March 2023"
    assert ing.effective_date(cover, "policy", CA) is None

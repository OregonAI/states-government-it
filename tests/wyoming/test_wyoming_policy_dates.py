"""Seam: src.states.effective_date and source_version for ETS policy PDFs (Google Drive files). The 2xxx and 3023
files open with a header table (Policy Owner, Policy Contact, Policy Approver, Effective Date, Next Review Date,
Policy Version). WyIT 3023 prints that table with the Effective Date and Policy Version cells empty and a Next Review
Date of October 01, 2027, which the shared 'Effective:' label reader would take for the effective date. The 1xxx and
3xxx files (WyIT 1005 here) have no header table: their dates live in a document-history table."""
from pathlib import Path

from src import states
from src.ingest_common import pdf_to_text

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "wyoming"


def text(name):
    return pdf_to_text((FIX / name).read_bytes())


def eff(name, doc_type="standard"):
    return states.effective_date(text(name), doc_type, "wyoming")


def test_a_printed_effective_date_is_transcribed():
    assert eff("wyit-2001-s1.pdf") == "2025-09-12"


def test_an_empty_effective_date_cell_is_not_filled_from_the_next_row():
    assert "Next Review Date" in text("wyit-3023.pdf") and eff("wyit-3023.pdf", "policy") is None


def test_the_printed_policy_version_is_the_source_version():
    assert states.source_version(text("wyit-2001-s1.pdf"), "standard", "wyoming", "pdf") == "2026-09.1"


def test_an_empty_policy_version_cell_gives_no_version():
    assert states.source_version(text("wyit-3023.pdf"), "policy", "wyoming", "pdf") == ""


def test_a_file_without_the_header_table_is_left_to_the_shared_reader():
    t = text("wyit-1005.pdf")
    assert states.effective_date(t, "policy", "wyoming") == states.effective_date(t, "policy", "")
    assert states.source_version(t, "policy", "wyoming", "pdf") == ""


def test_an_abbreviated_month_is_read_and_the_next_review_date_is_not():
    # first page of the WyIT 2003 PDF as published: 'Effective Date  Nov 4, 2026', then 'Next Review Date  October 01, 2027'
    t = text("wyit-2003-p1.pdf")
    assert "Nov 4, 2026" in t and "Next Review Date" in t
    assert eff("wyit-2003-p1.pdf", "policy") == "2026-11-04"

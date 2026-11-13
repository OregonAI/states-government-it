"""Seam: src.ingest for a Wisconsin statute that is a slice of the Legislature's chapter PDF
(docs.legis.wisconsin.gov/document/statutes/16.pdf). Used where the section's own page is cut off by the end of the
Legislature's scrolling window (s. 16.61). The fixture is the real chapter's first page and pages 57 to 60 (published
11-4-26): the section starts on page 57 and ends on page 59, so the slice crosses two page breaks with their
headers, footers and running heads; the next section, s. 16.611, starts at the foot of page 59."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "wisconsin"
CHAPTER = (FIX / "statutes-16-pages-1-57-to-60.pdf").read_bytes()
SLICE = {"section_start": "16.61", "section_end_before": "16.611"}
SRC = {"id": "wi-stat-16-61", "citation": "Wis. Stat. s. 16.61", "doc_type": "statute", "jurisdiction": "wisconsin",
       "format": "pdf", "slice": SLICE, "title": "Wis. Stat. 16.61 - Records of state offices and other public records"}


def cut(start="16.61", end="16.611"):
    return ing.to_text(CHAPTER, "pdf", "statute", "wisconsin", {"section_start": start, "section_end_before": end})


def test_slice_starts_at_the_first_heading_and_includes_every_subsection_to_the_history_line():
    lines = cut().splitlines()
    assert lines[0].startswith("16.61 Records of state offices and other public")
    text = "\n".join(lines)
    for marker in ("(1) PUBLIC RECORDS BOARD.", "(2) DEFINITIONS.", "(3) POWERS AND DUTIES OF THE BOARD.",
                   "(5) TRANSFER OF PUBLIC RECORDS", "(13) HISTORICAL SOCIETY AND UNIVERSITY ARCHIVES"):
        assert marker in text, marker
    history = [l for l in lines if l.startswith("History:")]
    assert len(history) == 1 and lines.index(history[0]) > lines.index(next(l for l in lines if l.startswith("(13) ")))


def test_slice_excludes_the_next_section_and_everything_after_it():
    text = cut()
    assert "16.611 State public records" not in text
    assert "(1) In this section, “public records”" not in text
    assert "Local government records" not in text


def test_slice_excludes_page_furniture_and_running_heads():
    for line in cut().splitlines()[:-1]:
        assert not line.startswith("Updated 2023-24") and not line.startswith("Updated 23-24")
        assert line.strip() not in ("DEPARTMENT OF ADMINISTRATION", "16.61", "16.611", "57", "58", "59", "60")
        assert not line.startswith("2023-24 Wisconsin Statutes updated through")
        assert line.strip()


def test_slice_ends_with_the_legislatures_certification_line_once():
    lines = cut().splitlines()
    assert lines[-1].startswith("2023-24 Wisconsin Statutes updated through 2025 Wis. Act 247")
    assert lines[-1].endswith("(Published 11-4-26)")
    assert sum(l.startswith("2023-24 Wisconsin Statutes") for l in lines) == 1


def test_slice_reads_columns_in_order_and_joins_a_word_hyphenated_at_a_line_end():
    text = cut()
    assert "opti-" not in text and "depart-\n" not in text
    assert "optical discs" in text or "optical disc" in text


def test_slice_version_is_the_publication_date():
    assert states.source_version(cut(), "statute", "wisconsin", "pdf") == "Published 11-4-26"


def test_slice_identity_needs_the_cited_section_to_open_it():
    states.check_identity(SRC, cut(), "pdf")
    with pytest.raises(ValueError, match="not Wis. Stat. s. 16.61"):
        states.check_identity(SRC, cut("16.611", "16.612"), "pdf")


def test_a_start_heading_that_is_not_printed_or_an_end_heading_that_does_not_follow_is_refused():
    with pytest.raises(ValueError, match="16.6199"):
        cut("16.6199", "16.611")
    with pytest.raises(ValueError, match="16.99"):
        cut("16.61", "16.99")


def test_a_cross_reference_at_the_start_of_a_line_is_not_a_heading():
    # "16.611 (2)" or "16.611, stats." wrapped to a line start is a reference, not the next section's heading
    from src.states import wisconsin
    assert wisconsin.slice_headings(["16.611 (2) shall", "16.611, Stats.", "16.611 State public records; x"]) == [(2, "16.611")]


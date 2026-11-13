"""Seam: src.ingest for a Wyoming statute that is a run of sections inside a non-IT chapter, named with the shared
section-range slice `slice: {section_start, section_end_before}` (printed section numbers; the end section is not in
the slice). The fixture is real pages 292-295 of the Legislature's Title 40 PDF (re-subset with ghostscript): the end of
chapter 21 (the Uniform Electronic Transactions Act) and the start of chapter 22, so the slice has the section before
it, the chapter heading after it and the next section to be excluded."""
import json
from pathlib import Path

import pytest
from corpus_toolkit.repo import parse_frontmatter

from seedutil import make_corpus, make_fetcher
from src import ingest as ing
from src.states import wyoming

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "wyoming"
URL = "https://wyoleg.gov/statutes/compress/title40.pdf"
PDF = (FIX / "wy-title-40-pages-292-295.pdf").read_bytes()

UETA = {"id": "wy-ws-40-21-117", "url": URL + "#40-21-117", "format": "json", "doc_type": "statute",
        "jurisdiction": "wyoming", "citation": "W.S. 40-21-117 through 40-21-119",
        "title": "Electronic records of governmental agencies (Title 40, Chapter 21, sections 117 to 119)",
        "issuing_body": "Wyoming Legislature", "tags": ["data"], "why_relevant": "State agencies' electronic records.",
        "slice": {"section_start": "40-21-117", "section_end_before": "40-22-101"}}


def ingest(tmp_path, src=UETA, pdf=PDF):
    cfg = make_corpus(tmp_path, [src])
    with make_fetcher(cfg, {URL: (200, pdf)}) as f:
        out = ing.ingest(src, f, False, cfg)
    return cfg, out


def full_text(doc: Path) -> str:
    _, body = parse_frontmatter(doc)
    return body.split("## Full text\n", 1)[1].split("\n## ", 1)[0].strip("\n")


def test_the_slice_starts_at_the_first_section_heading(tmp_path):
    _, out = ingest(tmp_path)
    assert full_text(out).splitlines()[0].strip() == "40-21-117. Creation and retention of electronic records"


def test_the_slice_holds_every_section_in_range(tmp_path):
    _, out = ingest(tmp_path)
    t = full_text(out)
    for heading in ("40-21-117. Creation and retention", "40-21-118. Acceptance and distribution",
                    "40-21-119.    Interoperability."):
        assert heading in t
    assert "the department of enterprise technology\nservices shall promulgate rules" in t   # 118(b), mid-section
    assert t.rstrip().endswith("particular application.")


def test_the_slice_excludes_the_next_section_the_chapter_heading_and_the_section_before(tmp_path):
    _, out = ingest(tmp_path)
    t = full_text(out)
    assert "40-22-101" not in t and "Short title" not in t
    assert "CHAPTER 22" not in t and "MONEY TRANSMITTERS" not in t     # the heading that sits between 119 and 22-101
    assert "transferable record" not in t                               # section 116, before the slice


def test_the_bundle_records_the_slice_and_the_text_is_rederived_offline(tmp_path):
    cfg, out = ingest(tmp_path)
    bundle = json.loads((tmp_path / "_meta" / "snapshots" / "wy-ws-40-21-117.json").read_bytes())
    assert bundle["slice"] == UETA["slice"] and bundle["source"] == URL
    fm, _ = parse_frontmatter(out)
    assert fm["source_url"] == URL + "#40-21-117" and fm["effective_date"] in (None, "")
    assert "section 40-21-117" in fm["conversion_notes"] and "section 40-22-101" in fm["conversion_notes"]
    assert ing.check([UETA], cfg) == []


@pytest.mark.parametrize("start,end", [("40-21-199", "40-22-101"), ("40-21-117", "40-22-999")])
def test_a_missing_boundary_section_is_refused_and_leaves_no_snapshot(tmp_path, start, end):
    bad = {**UETA, "slice": {"section_start": start, "section_end_before": end}}
    cfg = make_corpus(tmp_path, [bad])
    with make_fetcher(cfg, {URL: (200, PDF)}) as f:
        with pytest.raises(ValueError, match=r"40-21-199|40-22-999"):
            ing.ingest(bad, f, False, cfg)
    assert not list((tmp_path / "_meta" / "snapshots").glob("wy-ws-40-21-117.*"))


def test_an_end_section_that_does_not_follow_the_start_is_refused(tmp_path):
    bad = {**UETA, "slice": {"section_start": "40-22-101", "section_end_before": "40-21-117"}}
    cfg = make_corpus(tmp_path, [bad])
    with make_fetcher(cfg, {URL: (200, PDF)}) as f:
        with pytest.raises(ValueError, match="40-21-117"):
            ing.ingest(bad, f, False, cfg)


@pytest.mark.parametrize("citation", ["W.S. 40-21-117 through 40-21-118", "W.S. 40-21-118 through 40-21-119"])
def test_the_citation_must_be_the_sections_the_slice_holds(tmp_path, citation):
    bad = {**UETA, "citation": citation}
    cfg = make_corpus(tmp_path, [bad])
    with make_fetcher(cfg, {URL: (200, PDF)}) as f:
        with pytest.raises(ValueError, match="40-21-11[789]"):
            ing.ingest(bad, f, False, cfg)


def test_a_section_printed_twice_as_a_heading_is_refused_not_guessed():
    text = "     1-2-3. A.\n\nbody\n\n     1-2-3. A again.\n\n     1-2-4. B.\n"
    with pytest.raises(ValueError, match="2 times"):
        wyoming.slice_sections(text, "1-2-3", "1-2-4")


def test_a_cross_reference_that_wraps_to_a_line_start_is_not_a_heading():
    text = ("     5-1-1. First.\n\nsee W.S. 5-1-1 through\n5-1-2.\n\n     5-1-2. Second.\n\nbody\n\n"
            "          CHAPTER 2 - NEXT\n\n     5-2-1. Next.\n")
    out = wyoming.slice_sections(text, "5-1-1", "5-2-1")
    assert out.splitlines()[0].strip() == "5-1-1. First." and out.rstrip().endswith("body")
    assert "CHAPTER 2" not in out


def test_a_repealed_section_is_not_in_force(tmp_path):
    text = "40-21-117.    Repealed by Laws 2026, ch. 1, § 1.\n"
    src = {**UETA, "citation": "W.S. 40-21-117"}
    with pytest.raises(ValueError, match="repealed"):
        wyoming.check_identity(src, text, "the slice")

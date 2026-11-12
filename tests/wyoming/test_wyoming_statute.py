"""Seam: src.ingest for Wyoming statutes: one slice (an article or a chapter) of the Legislature's
per-title PDF. The official source is one PDF per title (wyoleg.gov/statutes/compress/title09.pdf, 892
pages); a seed entry names its slice with `cut: {from: <heading line>, to: <next heading line>}`
(the shared seed check only knows Colorado's and California's `slice` keys, so Wyoming's key is `cut`, and entries of one title
are told apart by a #fragment on the url, as California's letters are). The
fixtures are real pages of that PDF (re-subset with ghostscript: the extracted text is byte-identical):
pages 264-266 and 287-298 (the end of article 25, article 29 and the start of article 30) and pages
848-855 (chapter 21 and the start of chapter 22), page headers and footers included."""
import hashlib
import json
from pathlib import Path

import pytest
from corpus_toolkit.repo import parse_frontmatter

from seedutil import make_corpus, make_fetcher
from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "wyoming"
URL = "https://wyoleg.gov/statutes/compress/title09.pdf"
ART = (FIX / "wy-title-09-pages-264-266-287-298.pdf").read_bytes()
CH21 = (FIX / "wy-title-09-pages-848-855.pdf").read_bytes()

ETS = {"id": "wy-ws-9-2-art-29", "url": URL + "#article-29", "format": "json", "doc_type": "statute",
       "jurisdiction": "wyoming", "citation": "W.S. 9-2-2901 through 9-2-2907",
       "title": "Department of Enterprise Technology Services (Title 9, Chapter 2, Article 29)",
       "issuing_body": "Wyoming Legislature", "tags": ["governance"], "why_relevant": "The enabling statute.",
       "cut": {"from": "ARTICLE 29 - DEPARTMENT OF ENTERPRISE TECHNOLOGY SERVICES",
                 "to": "ARTICLE 30 - STATE CONSTRUCTION DEPARTMENT"}}
DATA = {**ETS, "id": "wy-ws-9-21", "url": URL + "#chapter-21", "citation": "W.S. 9-21-101 through 9-21-203", "title": "Data Policies",
        "cut": {"from": "CHAPTER 21 - DATA POLICIES",
                  "to": "CHAPTER 22 - LIMITATIONS ON DELEGATES TO A CONVENTION FOR"}}


def ingest(tmp_path, src, pdf):
    cfg = make_corpus(tmp_path, [src])
    calls = []
    with make_fetcher(cfg, {URL: (200, pdf)}, calls) as f:
        out = ing.ingest(src, f, False, cfg)
    return cfg, out, calls


def full_text(doc: Path) -> str:
    _, body = parse_frontmatter(doc)
    return body.split("## Full text\n", 1)[1].split("\n## ", 1)[0].strip()


def test_article_slice_runs_from_its_heading_to_the_next_articles_heading(tmp_path):
    _, out, _ = ingest(tmp_path, ETS, ART)
    t = full_text(out)
    lines = t.splitlines()
    assert lines[0].strip() == "ARTICLE 29 - DEPARTMENT OF ENTERPRISE TECHNOLOGY SERVICES"
    assert "9-2-2906. Office of the state chief information officer" in t
    assert "9-2-2907.    Repealed by Laws 2016, ch. 30, § 1." in t
    assert "ARTICLE 30" not in t and "9-2-3001" not in t
    assert "ARTICLE 25" not in t and "9-2-2501. Director of department" not in t


def test_chapter_slice_keeps_both_articles_and_the_dated_note(tmp_path):
    _, out, _ = ingest(tmp_path, DATA, CH21)
    t = full_text(out)
    assert t.splitlines()[0].strip() == "CHAPTER 21 - DATA POLICIES"
    assert "ARTICLE 1 - DATA POLICIES-STATE AGENCIES" in t and "ARTICLE 2 - DATA PRIVACY-GOVERNMENT ENTITIES" in t
    assert "government entities. Note: this section is effective as of\n7/1/2027." in t
    assert "CHAPTER 22" not in t and "9-22-101" not in t


def test_ingest_writes_a_bundle_as_the_snapshot_and_the_document_from_it(tmp_path):
    cfg, out, _ = ingest(tmp_path, DATA, CH21)
    snap = tmp_path / "_meta" / "snapshots" / "wy-ws-9-21.json"
    bundle = json.loads(snap.read_bytes())
    assert bundle["source"] == URL and bundle["pdf_sha256"] == hashlib.sha256(CH21).hexdigest()
    assert bundle["cut"] == DATA["cut"]
    fm, _ = parse_frontmatter(out)
    assert fm["jurisdiction"] == "wyoming" and fm["source_url"] == URL + "#chapter-21" and fm["source_format"] == "json"
    assert fm["effective_date"] in (None, "")                 # a statute never gets one
    assert ing.check([DATA], cfg) == []                        # offline: re-derived from the bundle


def test_a_cached_snapshot_is_not_fetched_again(tmp_path):
    cfg, _, _ = ingest(tmp_path, DATA, CH21)
    calls = []
    with make_fetcher(cfg, {URL: (200, CH21)}, calls) as f:
        ing.ingest(DATA, f, False, cfg)
    assert calls == []


def test_a_heading_that_is_not_in_the_pdf_leaves_no_snapshot(tmp_path):
    bad = {**DATA, "cut": {"from": "CHAPTER 99 - NOTHING", "to": DATA["cut"]["to"]}}
    cfg = make_corpus(tmp_path, [bad])
    with make_fetcher(cfg, {URL: (200, CH21)}) as f:
        with pytest.raises(ValueError, match="CHAPTER 99"):
            ing.ingest(bad, f, False, cfg)
    assert not list((tmp_path / "_meta" / "snapshots").glob("wy-ws-9-21.*"))


def test_a_slice_whose_end_heading_is_missing_is_refused_not_run_to_the_end(tmp_path):
    bad = {**DATA, "cut": {"from": DATA["cut"]["from"], "to": "CHAPTER 98 - NOTHING"}}
    cfg = make_corpus(tmp_path, [bad])
    with make_fetcher(cfg, {URL: (200, CH21)}) as f:
        with pytest.raises(ValueError, match="CHAPTER 98"):
            ing.ingest(bad, f, False, cfg)


def test_the_citation_must_name_a_section_the_slice_prints(tmp_path):
    bad = {**DATA, "citation": "W.S. 9-2-2901 through 9-2-2907"}
    cfg = make_corpus(tmp_path, [bad])
    with make_fetcher(cfg, {URL: (200, CH21)}) as f:
        with pytest.raises(ValueError, match="9-2-2901"):
            ing.ingest(bad, f, False, cfg)
    assert not list((tmp_path / "_meta" / "snapshots").glob("wy-ws-9-21.*"))

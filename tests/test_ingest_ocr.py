"""Seams: src.ingest.ocr_scan / check_ocr / derive-adjacent document functions for a PDF that is a scan
(no text layer): the two-engine OCR procedure of the corpus-template AGENTS.md ("OCR" section).

Primary engine: tesseract through ocrmypdf, run here and again by `--check` in CI (both are apt packages on
Ubuntu 24.04). Cross-check engine: PaddleOCR PP-OCRv6, which CI does not have, so its text is committed beside
the snapshot (`<id>.paddle.txt`) and `--check` recomputes the agreement from the two committed texts.

Fixtures are real bytes: Oregon statewide policy 107-004-053 (a two-page scan, fetched 2026-11-11 through the
toolkit Fetcher) and the text PaddleOCR (PP-OCRv6, orientation classification on) read from it the same day.
The tests that run tesseract need ocrmypdf and skip without it on a developer machine only; in CI they fail."""
import json
import os
import shutil
from pathlib import Path

import pytest
import yaml
from corpus_toolkit import config as config_mod
from corpus_toolkit.repo import parse_frontmatter

from src import ingest as ing

ROOT = Path(__file__).resolve().parent.parent
FIX = Path(__file__).resolve().parent / "fixtures"
SCAN = (FIX / "or-das-107-004-053-scan.pdf").read_bytes()
PADDLE = (FIX / "or-das-107-004-053-scan.paddle.txt").read_text()
VOCAB = ing.ocr_vocabulary(ing.CONFIG)      # this corpus's own non-OCR text, as the ingest uses it

SRC = {"id": "or-das-107-004-053", "format": "pdf", "ocr": True, "doc_type": "policy", "jurisdiction": "oregon",
       "url": "https://www.oregon.gov/das/Policies/107-004-053.pdf", "citation": "Statewide Policy 107-004-053",
       "title": "Employee Security", "tags": ["cybersecurity"], "issuing_body": "Department of Administrative Services",
       "why_relevant": "Personnel screening, access removal and awareness training."}

needs_ocr = pytest.mark.skipif(shutil.which("ocrmypdf") is None and not os.environ.get("CI"),
                               reason="ocrmypdf not installed")


def paddle_of(text):
    return lambda pdf_path: text


def corpus(tmp_path):
    (tmp_path / "_meta").mkdir()
    shutil.copy(ROOT / "_meta" / "corpus.yml", tmp_path / "_meta" / "corpus.yml")
    (tmp_path / "_meta" / "source-manifest.yml").write_text(yaml.safe_dump({"sources": [SRC]}))
    return config_mod.load(tmp_path / "_meta" / "corpus.yml")


# ---- the agreement score ------------------------------------------------------------------

def test_agreement_is_the_word_sequence_ratio_and_figures_are_scored_apart():
    s = ing.ocr_score("the quick brown fox jumps over 12 lazy dogs 3,400",
                      "the quick brown fox jumps over 12 lazy cogs 3,400", {"the", "quick", "brown", "fox",
                                                                              "jumps", "over", "lazy", "dogs"})
    # 8 words each, 7 equal: 2*7/16
    assert s["agreement"] == pytest.approx(0.875)
    assert s["figure_agreement"] == 1.0 and s["figures"] == 2
    assert s["dict_ratio"] == 1.0
    miss = ing.ocr_score("the 12 and 99", "the 12 and 98", set())
    assert miss["figure_agreement"] == pytest.approx(0.5) and miss["dict_ratio"] == 0.0


def test_a_ratio_of_nothing_is_zero_not_a_crash():
    s = ing.ocr_score("", "", set())
    assert s["agreement"] == 0.0 and s["words"] == 0


# ---- tesseract, then the second engine -----------------------------------------------------

@needs_ocr
def test_tesseract_reads_a_scan_that_pdftotext_finds_no_words_in():
    with pytest.raises(ValueError, match="no text layer"):
        ing.pdf_to_text(SCAN)
    text = ing.ocr_tesseract(SCAN)
    assert "Employee Security" in text and "107-004-053" in text
    assert "\f" not in text and not any(l != l.rstrip() for l in text.splitlines())


@needs_ocr
def test_two_engines_that_agree_make_a_document_text_and_a_report(tmp_path):
    cfg = corpus(tmp_path)
    text, report = ing.ocr_scan(SRC, SCAN, cfg, paddle=paddle_of(PADDLE), vocab=VOCAB)
    assert "Employee Security" in text
    assert report["agreement"] >= 0.80 and report["dict_ratio"] >= 0.80
    assert report["engines"][0].startswith("tesseract") and "paddleocr" in report["engines"][1]
    assert report["pdf_sha256"] == ing.hashlib.sha256(SCAN).hexdigest()
    assert report["paddle_text"] == PADDLE


@needs_ocr
def test_engines_that_disagree_leave_no_text(tmp_path):
    cfg = corpus(tmp_path)
    with pytest.raises(ValueError, match="agree"):
        ing.ocr_scan(SRC, SCAN, cfg, paddle=paddle_of("completely different words about nothing at all " * 80),
                     vocab=VOCAB)


@needs_ocr
def test_text_that_is_mostly_not_words_is_refused_even_when_the_engines_agree(tmp_path):
    cfg = corpus(tmp_path)
    with pytest.raises(ValueError, match="dictionary"):
        ing.ocr_scan(SRC, SCAN, cfg, paddle=paddle_of(PADDLE), vocab={"zzz"})


def test_the_second_engine_missing_is_a_refusal_not_a_silent_pass(tmp_path, monkeypatch):
    monkeypatch.setenv("OCR_PADDLE_PYTHON", str(tmp_path / "no-such-python"))
    with pytest.raises(ValueError, match="PaddleOCR"):
        ing.ocr_paddle(tmp_path / "x.pdf")


# ---- the document, and --check -------------------------------------------------------------

def ingested(tmp_path):
    cfg = corpus(tmp_path)
    text, report = ing.ocr_scan(SRC, SCAN, cfg, paddle=paddle_of(PADDLE), vocab=VOCAB)
    ing.write_ocr_snapshot(cfg, SRC, SCAN, text, report)
    return cfg


@needs_ocr
def test_the_ocr_document_says_plainly_that_a_machine_read_an_image(tmp_path):
    cfg = ingested(tmp_path)
    path = ing.write_ocr_document(SRC, cfg)
    fm, body = parse_frontmatter(path)
    assert fm["text_source"] == "ocr" and fm["content_mode"] == "verbatim"
    assert fm["effective_date"] is None and fm["source_version"] == ""
    assert fm["conversion_notes"].endswith("NOT human-verified — treat every number as unchecked against the source")
    assert "tesseract" in fm["conversion_notes"] and "PP-OCRv6" in fm["conversion_notes"]
    assert "MACHINE READING OF A SCAN" in body
    assert (tmp_path / "_meta" / "snapshots" / "or-das-107-004-053.pdf").read_bytes() == SCAN


@needs_ocr
def test_check_passes_on_a_fresh_ocr_ingest(tmp_path):
    cfg = ingested(tmp_path)
    ing.write_ocr_document(SRC, cfg)
    assert ing.check([SRC], cfg) == []


@needs_ocr
def test_check_fails_when_the_committed_ocr_text_is_edited(tmp_path):
    cfg = ingested(tmp_path)
    ing.write_ocr_document(SRC, cfg)
    txt = cfg.snapshot_dir / "or-das-107-004-053.txt"
    txt.write_text(txt.read_text().replace("Employee Security", "Employee Insecurity", 1))
    assert any(".txt" in m and "or-das-107-004-053" in m for m in ing.check([SRC], cfg))


@needs_ocr
def test_check_fails_when_the_recorded_second_engine_text_is_swapped(tmp_path):
    cfg = ingested(tmp_path)
    ing.write_ocr_document(SRC, cfg)
    (cfg.snapshot_dir / "or-das-107-004-053.paddle.txt").write_text("unrelated words " * 300)
    assert any("paddle" in m for m in ing.check([SRC], cfg))


@needs_ocr
def test_check_fails_when_the_text_is_not_what_tesseract_reads_from_the_scan(tmp_path):
    """Both committed texts and the recorded hashes are consistent with each other but are not a reading of
    this PDF: only re-running tesseract on the snapshot catches it."""
    cfg = ingested(tmp_path)
    ing.write_ocr_document(SRC, cfg)
    other = "Alpha beta gamma delta epsilon. " * 200
    snap = cfg.snapshot_dir
    (snap / "or-das-107-004-053.txt").write_text(other)
    (snap / "or-das-107-004-053.paddle.txt").write_text(other)
    rep = json.loads((snap / "or-das-107-004-053.ocr.json").read_text())
    rep["text_sha256"] = ing.hashlib.sha256(other.encode()).hexdigest()
    rep["paddle_sha256"] = rep["text_sha256"]
    (snap / "or-das-107-004-053.ocr.json").write_text(json.dumps(rep))
    assert any("tesseract" in m for m in ing.check([SRC], cfg))


@needs_ocr
def test_check_fails_when_the_snapshot_pdf_is_not_the_one_that_was_read(tmp_path):
    cfg = ingested(tmp_path)
    ing.write_ocr_document(SRC, cfg)
    (cfg.snapshot_dir / "or-das-107-004-053.pdf").write_bytes(SCAN + b"\n%changed")
    assert any("pdf" in m.lower() and "sha256" in m for m in ing.check([SRC], cfg))


def test_a_scan_is_still_refused_without_the_ocr_flag():
    with pytest.raises(ValueError, match="no text layer"):
        ing.derive(dict(SRC, ocr=False), SCAN)


# ---- Oregon's executive orders print "EXECUTIVE ORDER NO. 23-26" as their heading -------------------
# (the heading lines are as tesseract read them from the Governor's scan of EO 23-26, 2026-11-11)
EO_HEAD = "Office of the Governor\n\nState of Oregon\n\nEXECUTIVE ORDER NO. 23-26\n\nESTABLISHING A STATE GOVERNMENT\n"
EO = {"id": "or-eo-23-26", "doc_type": "executive_order", "jurisdiction": "oregon", "format": "pdf",
      "citation": "Executive Order No. 23-26", "title": "Establishing a State Government Artificial Intelligence Advisory Council"}


def test_an_oregon_order_is_the_cited_one_when_its_heading_prints_its_number():
    ing.check_identity(EO, EO_HEAD, "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(dict(EO, citation="Executive Order No. 23-25"), EO_HEAD, "pdf")


def test_an_order_that_only_cites_the_number_in_passing_is_not_that_order():
    cites = "Office of the Governor\n\nEXECUTIVE ORDER NO. 24-01\n\nAs amended by Executive Order No. 23-26, the council\n"
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(EO, cites, "pdf")


# ---- a PDF with a text page and scanned pages (California's EO N-30-25) --------------------------------
# Page 1 has a text layer; pages 2-4 are scans, scanned upside down: tesseract at its default orientation
# confidence reads them as confident nonsense, so the procedure's forced-orientation retry is what makes
# the text. Fixtures are real bytes (www.gov.ca.gov, fetched 2026-11-11 with curl_on_challenge=True) and the
# text PaddleOCR read from pages 2-4 the same day.
MIXED = (FIX / "ca-eo-n-30-25-mixed.pdf").read_bytes()
MIXED_PADDLE = (FIX / "ca-eo-n-30-25-mixed.paddle.txt").read_text()
MIXED_SRC = {"id": "ca-eo-n-30-25", "format": "pdf", "ocr": [2, 3, 4], "doc_type": "executive_order",
             "jurisdiction": "california", "citation": "Executive Order N-30-25",
             "url": "https://www.gov.ca.gov/wp-content/uploads/2025/07/2025-7-15.Efficient-and-Effective-Government-EO.FINAL_.signed.pdf",
             "title": "Government Efficiency and Innovation", "tags": ["governance"],
             "issuing_body": "Office of the Governor", "why_relevant": "An order of the Governor."}


def mixed_corpus(tmp_path):
    cfg = corpus(tmp_path)
    (tmp_path / "_meta" / "source-manifest.yml").write_text(yaml.safe_dump({"sources": [MIXED_SRC]}))
    return config_mod.load(tmp_path / "_meta" / "corpus.yml")


@needs_ocr
def test_listed_scan_pages_are_read_by_ocr_and_the_text_page_keeps_its_text_layer(tmp_path):
    cfg = mixed_corpus(tmp_path)
    text, report = ing.ocr_scan(MIXED_SRC, MIXED, cfg, paddle=paddle_of(MIXED_PADDLE), vocab=VOCAB)
    assert report["forced_rotation"] is True and report["pages"] == [2, 3, 4]
    assert report["agreement"] >= 0.95
    assert " ".join(text.split()[:8]) == "EXECUTIVE DEPARTMENT STATE OF CALIFORNIA EXECUTIVE ORDER N-30-25"   # page 1: pdftotext -layout
    assert text.index("WHEREAS California is the 4th largest economy") < text.index("wildfire detection")
    assert "satellites for" in text


@needs_ocr
def test_a_listed_page_that_has_a_text_layer_is_refused(tmp_path):
    cfg = mixed_corpus(tmp_path)
    with pytest.raises(ValueError, match="page 1"):
        ing.ocr_scan(dict(MIXED_SRC, ocr=[1, 2, 3, 4]), MIXED, cfg, paddle=paddle_of(MIXED_PADDLE), vocab=VOCAB)


@needs_ocr
def test_an_unlisted_scan_page_is_refused_not_dropped(tmp_path):
    cfg = mixed_corpus(tmp_path)
    with pytest.raises(ValueError, match="page 4"):
        ing.ocr_scan(dict(MIXED_SRC, ocr=[2, 3]), MIXED, cfg, paddle=paddle_of(MIXED_PADDLE), vocab=VOCAB)


@needs_ocr
def test_check_passes_for_a_mixed_pdf_and_fails_when_the_text_layer_part_is_edited(tmp_path):
    cfg = mixed_corpus(tmp_path)
    text, report = ing.ocr_scan(MIXED_SRC, MIXED, cfg, paddle=paddle_of(MIXED_PADDLE), vocab=VOCAB)
    ing.write_ocr_snapshot(cfg, MIXED_SRC, MIXED, text, report)
    ing.write_ocr_document(MIXED_SRC, cfg)
    assert ing.check([MIXED_SRC], cfg) == []
    notes = parse_frontmatter(ing.doc_path(MIXED_SRC, cfg))[0]["conversion_notes"]
    assert "Pages 2, 3, 4" in notes and "pdftotext" in notes
    # the text-layer page is re-derived by pdftotext: an edit there, with every hash kept consistent, is caught
    snap = cfg.snapshot_dir
    edited = text.replace("4th largest economy", "5th largest economy", 1)
    (snap / "ca-eo-n-30-25.txt").write_text(edited)
    rep = json.loads((snap / "ca-eo-n-30-25.ocr.json").read_text())
    rep["text_sha256"] = ing.hashlib.sha256(edited.encode()).hexdigest()
    (snap / "ca-eo-n-30-25.ocr.json").write_text(json.dumps(rep))
    assert any("text layer" in m for m in ing.check([MIXED_SRC], cfg))

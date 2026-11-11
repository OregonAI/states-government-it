"""Seams: src.ingest.derive / docx_to_text / check for the instruments an agency publishes only as a
Word file (.docx). The text is read with pandoc (JSON syntax tree, rendered here), one line per
paragraph, heading, list item and table row, cells joined by ` | `, the same shape as the Department of
Technology pages.

Fixtures are real bytes fetched 2026-11-11 through the toolkit Fetcher: WaTech's Metadata Standard 187.10
(a standard with four tables, a revision history and a footnote part) and the Enterprise Service
Designation for Internal Identity Management (a short designation with a bulleted list and one table)."""
import shutil
from pathlib import Path

import pytest

from src import ingest as ing

FIX = Path(__file__).resolve().parent / "fixtures"
METADATA = (FIX / "wa-metadata-standard-187-10.docx").read_bytes()
DESIGNATION = (FIX / "wa-enterprise-service-185-10.docx").read_bytes()

SRC = {"id": "wa-data-01-02-s", "format": "docx", "doc_type": "standard", "jurisdiction": "washington",
       "url": "https://watech.wa.gov/sites/default/files/2023-09/187_10_MetadataStandard_Approved%252003102020.docx",
       "citation": "WaTech Standard DATA-01-02-S", "title": "Metadata Standard",
       "identity_text": "Standard 187.10 - Metadata Standard"}

needs_pandoc = pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")


@needs_pandoc
def test_a_word_file_is_read_as_one_line_per_paragraph_and_table_row():
    fmt, text = ing.derive(SRC, METADATA)
    assert fmt == "docx"
    lines = text.splitlines()
    assert lines[0] == "Standard 187.10 - Metadata Standard"
    assert "Purpose" in lines
    assert "Element | Description | Format/Example" in lines
    assert "March 10, 2020 | Approved by Technology Services Board" in lines
    assert lines[-1] == "APPROVING AUTHORITY: Jim Weaver, State CIO & Chair TSB"
    assert not any(l != l.rstrip() or "+--" in l for l in lines)


@needs_pandoc
def test_a_cell_with_several_paragraphs_stays_on_its_rows_line():
    _, text = ing.derive(SRC, METADATA)
    row = next(l for l in text.splitlines() if l.startswith("Title | A name given to the resource."))
    assert row.endswith("Format: Character Example: Water Rights Applications")


@needs_pandoc
def test_bullets_and_the_table_of_a_short_designation():
    src = dict(SRC, id="wa-ea-185-10", title="Enterprise Business Processes for Internal Identity Management",
               identity_text="Enterprise Business Processes for Internal Identity Management")
    _, text = ing.derive(src, DESIGNATION)
    lines = text.splitlines()
    assert "• Manage the State's internal identity management solution, the Enterprise Active Directory, to accomplish single sign-on." in lines
    assert "Date | Action Taken" in lines
    assert "09/06/2016 | Designated as an Enterprise Service" in lines


@needs_pandoc
def test_a_word_file_that_is_not_the_cited_instrument_is_refused():
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(dict(SRC, identity_text="Standard 162.00"), METADATA)


def test_bytes_that_are_not_a_word_file_are_refused_not_guessed():
    with pytest.raises(ValueError):
        ing.docx_to_text(b"PK\x03\x04 not really a word file")


def test_an_unknown_construct_in_the_syntax_tree_is_refused(monkeypatch):
    tree = {"pandoc-api-version": [1, 23], "meta": {}, "blocks": [{"t": "Mystery", "c": []}]}
    with pytest.raises(ValueError, match="Mystery"):
        ing.render_pandoc_ast(tree)


def test_the_rendering_of_lists_notes_and_inlines():
    s = lambda w: {"t": "Str", "c": w}
    sp = {"t": "Space"}
    para = lambda *w: {"t": "Para", "c": list(w)}
    tree = {"blocks": [
        para(s("Intro"), sp, {"t": "Note", "c": [para(s("A"), sp, s("note"))]}),
        {"t": "OrderedList", "c": [[3, {"t": "LowerAlpha"}, {"t": "OneParen"}],
                                   [[para(s("first"))], [para(s("second")), {"t": "BulletList", "c": [[para(s("inner"))]]}]]]},
        {"t": "HorizontalRule"},
        para(s("Link:"), sp, {"t": "Link", "c": [["", [], []], [s("text")], ["https://x", ""]]},
             {"t": "LineBreak"}, {"t": "Image", "c": [["", [], []], [s("logo")], ["a.png", ""]]}, s("end")),
    ]}
    assert ing.render_pandoc_ast(tree) == (
        "Intro [1]\n\nc) first\nd) second\n   • inner\n\nLink: text\nend\n\n[1] A note\n")


def test_same_words_in_a_different_layout_are_the_same_text():
    assert ing.same_words("a | b\n\nc d\n", "a  |  b c\nd")
    assert not ing.same_words("a | b c", "a | b d")
    assert not ing.same_words("a b", "a b c")


# ---- the Department of Technology's Word files --------------------------------------------
# Fixtures: SIMM 18B (the cover of the Cloud Computing Policy Exemption Form preparation instructions)
# and SIMM 5310-C (a standard whose first table names it), both fetched 2026-11-11 from www.cdt.ca.gov
# through the Fetcher with curl_on_challenge=True.
SIMM_18B = (FIX / "cdt-simm-18b.docx").read_bytes()
SIMM_5310C = (FIX / "cdt-simm-5310-c.docx").read_bytes()
CA18B = {"id": "ca-simm-18b", "format": "docx", "doc_type": "policy", "jurisdiction": "california",
         "url": "https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-18B-Cloud-Computing-Policy-Exemption-Form.docx",
         "citation": "SIMM 18B", "title": "Policy Exemption Instructions",
         "identity_text": "Cloud Computing Policy Exemption Form"}
CA5310C = {"id": "ca-simm-5310-c", "format": "docx", "doc_type": "standard", "jurisdiction": "california",
           "url": "https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5310-C-Privacy-Threshold-Assessment-and-Privacy-Impact-Assessments.docx",
           "citation": "SIMM 5310-C", "title": "Privacy Threshold Assessment and Privacy Impact Assessments",
           "identity_text": "5310-C Privacy Threshold Assessments and Privacy Impact Assessments"}


@needs_pandoc
def test_a_cdt_word_file_is_the_cited_section_when_its_cover_prints_it():
    fmt, text = ing.derive(CA18B, SIMM_18B)
    assert fmt == "docx"
    assert ing.source_version(text, "policy", "california") == "October 2023"
    _, text = ing.derive(CA5310C, SIMM_5310C)
    assert "Owner | Office of Information Security – Privacy Program" in text.splitlines()


@needs_pandoc
def test_a_cdt_word_file_under_another_sections_citation_is_refused():
    with pytest.raises(ValueError, match="Section 18B|SIMM section 18B"):
        ing.derive(dict(CA18B, citation="SIMM 18A"), SIMM_18B)
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.derive(dict(CA5310C, identity_text="5310-B Privacy Individual Access Standard"), SIMM_5310C)


# ---- ingest and --check for a Word file ---------------------------------------------------
import httpx
import yaml
from corpus_toolkit import config as config_mod
from corpus_toolkit.repo import parse_frontmatter
from corpus_toolkit.sources.fetch import Fetcher

ROOT = Path(__file__).resolve().parent.parent


def _ingested(tmp_path):
    (tmp_path / "_meta").mkdir()
    shutil.copy(ROOT / "_meta" / "corpus.yml", tmp_path / "_meta" / "corpus.yml")
    (tmp_path / "_meta" / "source-manifest.yml").write_text(yaml.safe_dump({"sources": [SRC]}))
    cfg = config_mod.load(tmp_path / "_meta" / "corpus.yml")
    handler = lambda request: httpx.Response(200, content=METADATA)
    with Fetcher(cfg, min_interval=0, transport=httpx.MockTransport(handler), sleep=lambda s: None) as f:
        ing.ingest(dict(SRC, tags=["data"], why_relevant="Metadata for open data.",
                        issuing_body="WaTech"), f, False, cfg)
    return cfg


@needs_pandoc
def test_a_word_file_is_ingested_with_the_word_file_as_snapshot_and_says_how_it_was_read(tmp_path):
    cfg = _ingested(tmp_path)
    fm, body = parse_frontmatter(ing.doc_path(SRC, cfg))
    assert fm["source_format"] == "docx" and fm["content_mode"] == "verbatim"
    assert fm["effective_date"] is None
    assert "pandoc" in fm["conversion_notes"] and "headers and footers" in fm["conversion_notes"]
    assert (cfg.snapshot_dir / "wa-data-01-02-s.docx").read_bytes() == METADATA
    assert "OCR" not in fm["conversion_notes"]


@needs_pandoc
def test_check_passes_when_another_pandoc_lays_the_same_words_out_differently(tmp_path, monkeypatch):
    cfg = _ingested(tmp_path)
    src = dict(SRC, tags=["data"], why_relevant="Metadata for open data.", issuing_body="WaTech")
    assert ing.check([src], cfg) == []
    real = ing.docx_to_text
    monkeypatch.setattr(ing, "docx_to_text", lambda raw: " ".join(real(raw).split("\n")) + "\n")
    assert ing.check([src], cfg) == []


@needs_pandoc
def test_check_fails_when_one_word_of_the_committed_text_differs(tmp_path):
    cfg = _ingested(tmp_path)
    src = dict(SRC, tags=["data"], why_relevant="Metadata for open data.", issuing_body="WaTech")
    txt = cfg.snapshot_dir / "wa-data-01-02-s.txt"
    txt.write_text(txt.read_text().replace("Approved by Technology", "Rejected by Technology", 1))
    assert any("wa-data-01-02-s" in m and ".txt" in m for m in ing.check([src], cfg))


def test_without_pandoc_the_word_file_is_refused_with_the_remedy(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(ValueError, match="pandoc is not installed"):
        ing.docx_to_text(METADATA)

"""Seam: src.ingest. The network is faked (httpx.MockTransport); fixtures are real bytes
the official sites served on 2026-11-10 (the ORS one trimmed after the first section).
Each test states one rule the ingester owes the reviewer."""
import shutil
import subprocess
import sys
from pathlib import Path

import httpx
import pytest
import yaml

from corpus_toolkit import config as config_mod
from corpus_toolkit.repo import parse_frontmatter
from corpus_toolkit.sources.fetch import FetchError, Fetcher

from src import ingest as ing

ROOT = Path(__file__).resolve().parent.parent
FIX = ROOT / "tests" / "fixtures"
ORS = (FIX / "ors-276a-excerpt.html").read_bytes()
OAR = (FIX / "oar-128-050.html").read_bytes()
PDF = (FIX / "eis-memo-cloud.pdf").read_bytes()
# A real PDF structure with one blank page: what a scan without a text layer looks like to
# pdftotext (zero words).
BLANK_PDF = (b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
             b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
             b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 200 200]>>endobj\n"
             b"trailer<</Root 1 0 R>>\n%%EOF\n")


# ---- to_text: one function per source format ------------------------------------------

def test_ors_text_is_one_paragraph_per_line_in_source_order():
    t = ing.to_text(ORS, "html", "statute")
    lines = t.splitlines()
    assert lines[0] == "Chapter 276A — Information Technology"
    assert "2025 EDITION" in lines
    # a source paragraph wrapped across several HTML lines is one line of text
    assert ("(5) Although each agency is responsible for the agency’s information resources, "
            "centralized information resource management must also exist to:") in lines
    assert lines.index("(State Chief Information Officer)") < \
        lines.index("276A.200 Legislative findings on information resources")


def test_ors_text_has_no_markup_no_page_furniture_no_blank_paragraphs():
    t = ing.to_text(ORS, "html", "statute")
    assert "<" not in t and "font-family" not in t and "MsoNormal" not in t
    assert "\xa0" not in t and "&nbsp;" not in t
    assert "\n\n" not in t                       # empty source paragraphs are dropped
    assert all(line == line.strip() for line in t.splitlines())


def test_ors_text_keeps_typography_of_the_source():
    t = ing.to_text(ORS, "html", "statute")
    assert "’" in t and "—" in t                 # decoded from windows-1252, not mangled
    assert "â€" not in t and "�" not in t


def test_oar_text_keeps_rule_number_title_body_authority_and_history():
    t = ing.to_text(OAR, "html", "rule")
    assert "Division 50" in t and "Identity Authentication/Electronic Signatures" in t
    assert "128-050-0005" in t
    assert "Statutory/Other Authority:" in t and "Statutes/Other Implemented:" in t
    assert "OSCIO 1-2026, amend filed 11/09/2026, effective 12/01/2026" in t
    assert "DAS 11-2005, f. & cert. ef. 10-21-05" in t     # entities decoded


def test_oar_text_drops_site_navigation_footer_and_scripts():
    t = ing.to_text(OAR, "html", "rule")
    for furniture in ("Search Current Rules", "Oregon State Archives", "ga('create'",
                      "Privacy Policy", "<", "Skip to main content"):
        assert furniture not in t


def test_pdf_text_is_layout_text_without_form_feeds_or_trailing_space():
    t = ing.to_text(PDF, "pdf", "policy")
    assert "Mandatory Cloud Services" in t
    assert "\f" not in t and "\n\n\n" not in t
    assert all(line == line.rstrip() for line in t.splitlines())


def test_pdf_without_a_text_layer_is_refused_not_mirrored_empty():
    with pytest.raises(ValueError, match="text layer"):
        ing.to_text(BLANK_PDF, "pdf", "policy")


def test_unknown_html_source_is_refused_rather_than_guessed():
    with pytest.raises(ValueError):
        ing.to_text(b"<html><body>x</body></html>", "html", "policy")


# ---- dates are transcribed, never guessed ----------------------------------------------

@pytest.mark.parametrize("text, want", [
    ("EFFECTIVE DATE        PAGE NUMBER\n May 1, 2025\nREVIEWED DATE\n June 2, 2026", "2025-05-01"),
    ("Effective Date: January 15, 2024", "2024-01-15"),
    ("DIVISION: Enterprise  EFFECTIVE DATE:      09-08-08", None),   # two-digit year: not guessed
    ("Date: August 12, 2022\nRe: cloud", None),                      # a memo date is not an effective date
    ("no dates here", None),
])
def test_effective_date_only_when_labelled_and_unambiguous(text, want):
    assert ing.effective_date(text) == want


# ---- ingest, with the network faked ---------------------------------------------------

def corpus(tmp_path):
    """A copy of this corpus's configuration in a temp repo, so a test never touches the real one."""
    (tmp_path / "_meta").mkdir()
    shutil.copy(ROOT / "_meta" / "corpus.yml", tmp_path / "_meta" / "corpus.yml")
    (tmp_path / "_meta" / "source-manifest.yml").write_text(
        yaml.safe_dump({"sources": [SRC_ORS, SRC_OAR, SRC_PDF]}))
    return config_mod.load(tmp_path / "_meta" / "corpus.yml")


def fetcher(cfg, routes, calls=None):
    def handler(request):
        if calls is not None:
            calls.append(str(request.url))
        status, body = routes.get(str(request.url), (404, b""))
        return httpx.Response(status, content=body)
    return Fetcher(cfg, min_interval=0, transport=httpx.MockTransport(handler),
                   sleep=lambda s: None)


SRC_ORS = {"id": "or-ors-276a", "url": "https://example.gov/ors276A.html", "format": "html",
           "citation": "ORS chapter 276A", "title": "Chapter 276A - Information Technology (2025 Edition)",
           "doc_type": "statute", "jurisdiction": "oregon",
           "issuing_body": "Oregon Legislative Assembly", "tags": ["governance", "cybersecurity"],
           "why_relevant": "The State CIO enabling statute."}
SRC_OAR = {"id": "or-oar-128-50", "url": "https://example.gov/oar.action", "format": "html",
           "citation": "OAR chapter 128, division 50",
           "title": "Identity Authentication/Electronic Signatures", "doc_type": "rule",
           "jurisdiction": "oregon", "issuing_body": "DAS, Office of the State CIO",
           "tags": ["digital-services"], "why_relevant": "E-signature guidelines."}
SRC_PDF = {"id": "or-eis-memo-20220812-cloud", "url": "https://example.gov/cloud.pdf",
           "format": "pdf", "citation": "State CIO Memo, 2022-08-12",
           "title": "Mandatory Cloud Services", "doc_type": "policy", "jurisdiction": "oregon",
           "issuing_body": "Enterprise Information Services", "tags": ["cloud-resilience"],
           "why_relevant": "Cloud strategy."}
ROUTES = {SRC_ORS["url"]: (200, ORS), SRC_OAR["url"]: (200, OAR), SRC_PDF["url"]: (200, PDF)}


def test_document_goes_to_type_state_id_with_seed_tags_and_jurisdiction(tmp_path):
    cfg = corpus(tmp_path)
    with fetcher(cfg, ROUTES) as f:
        out = ing.ingest(SRC_ORS, f, False, cfg)
        out2 = ing.ingest(SRC_OAR, f, False, cfg)
        out3 = ing.ingest(SRC_PDF, f, False, cfg)
    assert out == tmp_path / "statutes" / "oregon" / "or-ors-276a.md"
    assert out2 == tmp_path / "rules" / "oregon" / "or-oar-128-50.md"
    assert out3 == tmp_path / "policies" / "oregon" / "or-eis-memo-20220812-cloud.md"
    fm, body = parse_frontmatter(out)
    assert fm["jurisdiction"] == "oregon" and fm["doc_type"] == "statute"
    assert fm["tags"] == ["governance", "cybersecurity"]
    assert fm["citation"] == "ORS chapter 276A" and fm["source_url"] == SRC_ORS["url"]
    assert fm["source_version"] == "2025 Edition"            # printed on the page
    assert fm["last_verified"] == "" and fm["verified_by"] == ""
    assert fm["content_mode"] == "verbatim" and fm["status"] == "current"
    assert "snapshot_policy" not in fm                       # raw snapshots are committed
    assert "NON-AUTHORITATIVE" in body and "## Full text" in body


def test_full_text_is_the_committed_snapshot_text(tmp_path):
    cfg = corpus(tmp_path)
    with fetcher(cfg, ROUTES) as f:
        out = ing.ingest(SRC_OAR, f, False, cfg)
    _, body = parse_frontmatter(out)
    full = body.split("## Full text\n", 1)[1].split("\n## ", 1)[0].strip()
    assert full == (tmp_path / "_meta" / "snapshots" / "or-oar-128-50.txt").read_text().strip()


def test_written_documents_pass_the_toolkit_gates(tmp_path):
    cfg = corpus(tmp_path)
    with fetcher(cfg, ROUTES) as f:
        for s in (SRC_ORS, SRC_OAR, SRC_PDF):
            ing.ingest(s, f, False, cfg)
    for tool in ("corpus-validate-frontmatter", "corpus-verify-provenance"):
        r = subprocess.run([str(Path(sys.executable).parent / tool), "--config",
                            str(tmp_path / "_meta" / "corpus.yml")],
                           capture_output=True, text=True, cwd=tmp_path)
        assert r.returncode == 0, r.stdout + r.stderr


def test_rerun_uses_the_snapshot_and_keeps_retrieved(tmp_path):
    cfg = corpus(tmp_path)
    calls = []
    with fetcher(cfg, ROUTES, calls) as f:
        out = ing.ingest(SRC_PDF, f, False, cfg)
        first = parse_frontmatter(out)[0]["retrieved"]
        ing.ingest(SRC_PDF, f, False, cfg)
    assert len(calls) == 1
    assert parse_frontmatter(out)[0]["retrieved"] == first


def test_a_refusal_is_raised_and_writes_nothing(tmp_path):
    cfg = corpus(tmp_path)
    with fetcher(cfg, {SRC_PDF["url"]: (403, b"no")}) as f:
        with pytest.raises(FetchError):
            ing.ingest(SRC_PDF, f, False, cfg)
    assert not list(tmp_path.rglob("*.md")) and not (tmp_path / "_meta" / "snapshots").exists()


def test_a_scan_without_text_writes_no_document_and_no_snapshot(tmp_path):
    cfg = corpus(tmp_path)
    with fetcher(cfg, {SRC_PDF["url"]: (200, BLANK_PDF)}) as f:
        with pytest.raises(ValueError, match="text layer"):
            ing.ingest(SRC_PDF, f, False, cfg)
    assert not list(tmp_path.rglob("*.md"))
    assert not list((tmp_path / "_meta" / "snapshots").glob("*.txt"))


def test_a_page_that_is_not_the_cited_instrument_is_refused(tmp_path):
    cfg = corpus(tmp_path)
    wrong = dict(SRC_OAR, title="Some Other Division Title")
    with fetcher(cfg, ROUTES) as f:
        with pytest.raises(ValueError, match="title"):
            ing.ingest(wrong, f, False, cfg)


# ---- which entries are fetched --------------------------------------------------------

@pytest.mark.parametrize("extra, want", [
    ({}, True), ({"stub": True, "stub_reason": "x"}, False), ({"watch_only": True}, False),
    ({"jurisdiction": "washington"}, False)])
def test_only_non_stub_non_watch_entries_of_the_state_are_ingested(extra, want):
    assert ing.ingestable(dict(SRC_PDF, **extra), "oregon") is want


def test_run_reports_failures_and_keeps_going(tmp_path):
    cfg = corpus(tmp_path)
    srcs = [SRC_PDF, dict(SRC_OAR, url="https://example.gov/refused"), SRC_ORS]
    routes = dict(ROUTES, **{"https://example.gov/refused": (403, b"")})
    with fetcher(cfg, routes) as f:
        done, failed = ing.run(srcs, f, False, cfg)
    assert [p.name for p in done] == ["or-eis-memo-20220812-cloud.md", "or-ors-276a.md"]
    assert [i for i, _ in failed] == ["or-oar-128-50"]

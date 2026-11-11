"""Seam: src.ingest, the flow every state shares (the network is faked with httpx.MockTransport; fixtures
are real bytes the official sites served on 2026-11-10, Oregon's here). State-specific text and identity
tests are in tests/<state>/. Each test states one rule the ingester owes the reviewer."""
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

from seedutil import write_seed
from src import ingest as ing
from src import ingest_common

ROOT = Path(__file__).resolve().parent.parent
FIX = ROOT / "tests" / "fixtures" / "oregon"
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

def test_pdf_text_is_layout_text_without_form_feeds_or_trailing_space():
    t = ing.to_text(PDF, "pdf", "policy")
    assert "Mandatory Cloud Services" in t
    assert "\f" not in t and "\n\n\n" not in t
    assert all(line == line.rstrip() for line in t.splitlines())


def test_pdf_ligature_glyphs_become_letters_so_the_words_are_searchable():
    # Real PDF the EIS site serves; pdftotext emits U+FB01 for "fi" in "configured", which
    # keyword search cannot match against "configured" or "definition".
    t = ing.to_text((FIX / "ai-attachment-e-ligature.pdf").read_bytes(), "pdf", "policy")
    assert "configured AI systems" in t
    assert not any("\ufb00" <= c <= "\ufb06" for c in t)


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
    ("DIVISION: Enterprise  EFFECTIVE DATE:      01-01-2010", "2010-01-01"),   # hyphens, four-digit year
    ("Budget categories  Effective: March 12, 2026\nPage 2", "2026-03-12"),   # `Effective:` is a label
    ("The order is effective immediately. Date: March 3, 2020", None),     # prose is not a label
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
    write_seed(tmp_path, [SRC_ORS, SRC_OAR, SRC_PDF])
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


# ---- a PDF must be the instrument the seed entry cites ---------------------------------

SRC_POLICY = dict(SRC_PDF, id="or-das-107-004-190", citation="Statewide Policy 107-004-190",
                  title="Some Title Not In The Text")


@pytest.mark.parametrize("citation, title, ok", [
    ("Statewide Policy 107-004-190", "Unrelated", True),            # the policy number is in the text
    ("Statewide Procedure 107-004-190_PR", "Unrelated", True),      # _PR suffix: same number
    ("Statewide Policy 107-004-999", "Unrelated", False),           # a different number
    ("State CIO Memo, 2022-08-12", "Mandatory Cloud Services", True),   # no number: the title
    ("State CIO Memo, 2022-08-12", "A Different Memo", False),
    ("State CIO Memo, 2022-08-12", "mandatory   cloud\nservices", True),   # case and spacing
    ("State CIO Memo, 2022-08-12", "Mandatory Cloud Services\u2019", False),   # not the printed text
])
def test_pdf_identity_needs_the_policy_number_or_the_title(citation, title, ok):
    text = "Policy 107-004-190 applies.\nMandatory Cloud Services\n"
    src = dict(SRC_PDF, citation=citation, title=title)
    if ok:
        ing.check_identity(src, text)
    else:
        with pytest.raises(ValueError, match="not the cited instrument"):
            ing.check_identity(src, text)


def test_identity_text_overrides_the_title_and_the_number():
    text = "Policy 107-004-190 applies.\nPrinted Title Here\n"
    ing.check_identity(dict(SRC_PDF, citation="Memo", title="Seed Title", identity_text="printed  title here"), text)
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(dict(SRC_PDF, citation="Policy 107-004-190", title="Seed Title",
                                identity_text="absent phrase"), text)


def test_a_pdf_that_is_not_the_cited_instrument_is_refused_and_leaves_nothing(tmp_path):
    cfg = corpus(tmp_path)
    wrong = dict(SRC_PDF, citation="Statewide Policy 107-004-999", title="Nothing Like It")
    with fetcher(cfg, ROUTES) as f:
        with pytest.raises(ValueError, match="not the cited instrument"):
            ing.ingest(wrong, f, False, cfg)
    assert not list(tmp_path.rglob("*.md"))
    assert not list((tmp_path / "_meta" / "snapshots").glob("*"))


# ---- --check: the committed files are what the ingester derives ------------------------

def ingested(tmp_path):
    cfg = corpus(tmp_path)
    with fetcher(cfg, ROUTES) as f:
        done, failed = ing.run([SRC_ORS, SRC_OAR, SRC_PDF], f, False, cfg)
    assert not failed
    return cfg


def test_check_passes_on_freshly_ingested_files(tmp_path):
    cfg = ingested(tmp_path)
    assert ing.check([SRC_ORS, SRC_OAR, SRC_PDF], cfg) == []


def test_check_fails_when_the_committed_text_is_not_what_to_text_derives(tmp_path):
    cfg = ingested(tmp_path)
    txt = cfg.snapshot_dir / "or-ors-276a.txt"
    txt.write_text(txt.read_text() + "an added line\n")
    out = ing.check([SRC_ORS, SRC_OAR, SRC_PDF], cfg)
    assert len(out) >= 1 and "or-ors-276a" in out[0] and ".txt" in out[0]


def test_check_fails_when_the_document_body_drifts_from_the_text(tmp_path):
    cfg = ingested(tmp_path)
    doc = ing.doc_path(SRC_PDF, cfg)
    doc.write_text(doc.read_text().replace("## Full text\n\n", "## Full text\n\nAn edited line.\n", 1))
    out = ing.check([SRC_ORS, SRC_OAR, SRC_PDF], cfg)
    assert any("or-eis-memo-20220812-cloud" in m and "document" in m for m in out)


def test_check_fails_on_a_missing_snapshot_or_document(tmp_path):
    cfg = ingested(tmp_path)
    ing.doc_path(SRC_OAR, cfg).unlink()
    (cfg.snapshot_dir / "or-ors-276a.html").unlink()
    out = ing.check([SRC_ORS, SRC_OAR, SRC_PDF], cfg)
    assert any("or-oar-128-50" in m for m in out) and any("or-ors-276a" in m for m in out)


def test_orphans_none_when_every_document_has_an_ingestable_entry_and_no_stub_has_one(tmp_path):
    cfg = ingested(tmp_path)
    assert ing.orphans([SRC_ORS, SRC_OAR, SRC_PDF], cfg) == []


def test_orphans_fails_when_an_entry_becomes_a_stub_but_its_document_stays(tmp_path):
    cfg = ingested(tmp_path)
    out = ing.orphans([SRC_ORS, SRC_OAR, dict(SRC_PDF, stub=True, stub_reason="x")], cfg)
    assert any("or-eis-memo-20220812-cloud" in m and "stub" in m for m in out)
    assert any("policies/oregon/or-eis-memo-20220812-cloud.md" in m for m in out)


def test_orphans_fails_when_an_entry_is_removed_but_its_document_stays(tmp_path):
    cfg = ingested(tmp_path)
    out = ing.orphans([SRC_ORS, SRC_OAR], cfg)
    assert out and "or-eis-memo-20220812-cloud.md" in out[0] and "no ingestable seed entry" in out[0]


def test_orphans_ignores_watch_only_entries_with_no_document(tmp_path):
    cfg = ingested(tmp_path)
    watch = {"id": "w", "jurisdiction": "oregon", "doc_type": "policy", "watch_only": True}
    assert ing.orphans([SRC_ORS, SRC_OAR, SRC_PDF, watch], cfg) == []


def test_check_cli_runs_offline_and_passes_on_this_repo():
    r = subprocess.run([sys.executable, "-m", "src.ingest", "--check"], cwd=ROOT,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_ingestable_takes_every_state_unless_one_is_named():
    oregon = {"id": "a", "jurisdiction": "oregon"}
    wash = {"id": "b", "jurisdiction": "washington"}
    stub = {"id": "c", "jurisdiction": "washington", "stub": True}
    assert [ing.ingestable(s, None) for s in (oregon, wash, stub)] == [True, True, False]
    assert [ing.ingestable(s, "washington") for s in (oregon, wash)] == [False, True]



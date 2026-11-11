"""Seam: src.ingest, California statutes from the Legislature's official bulk download
(downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip). The site's per-section web pages
refuse the toolkit's Fetcher (a Cloudflare challenge), so the text comes from the bulk file.
tests/fixtures/pubinfo holds real rows and real section files from the 2026-11-08 download
(Government Code chapters 5.7 and 5.9, article 1 of chapter 1, and Civil Code chapter 1 of
title 1.8); the tests assemble them into a zip and serve it with the network faked."""
import io
import json
import re
import shutil
import zipfile
from pathlib import Path

import httpx
import pytest
import yaml

from corpus_toolkit import config as config_mod
from corpus_toolkit.repo import parse_frontmatter
from corpus_toolkit.sources.fetch import Fetcher

from src import check_seed_list as csl
from src import ingest as ing

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "tests" / "fixtures" / "pubinfo"
URL = "https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip"

CH59 = {"code": "GOV", "path": "3.3.1.12"}
GOV_11019_9 = {"code": "GOV", "section": "11019.9"}


def build_zip() -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for dat in sorted(PUB.glob("*.dat")):
            z.writestr(dat.name, dat.read_bytes())
        for lob in sorted((PUB / "lobs").glob("*.lob")):
            z.writestr(lob.name, lob.read_bytes())
    return buf.getvalue()


ZIP = build_zip()


def open_fixture_zip():
    return zipfile.ZipFile(io.BytesIO(ZIP))


def bundle(slice_, url=URL):
    return ing.ca_bundle(open_fixture_zip(), slice_, url, "Sun, 08 Nov 2026 21:26:00 GMT")


def text(slice_):
    return ing.to_text(bundle(slice_), "json", "statute", "california", slice_)


# ---- the bundle: the rows and section files the text is made from -------------------------

def test_bundle_holds_the_raw_rows_and_section_files_of_the_slice_only():
    b = json.loads(bundle(CH59))
    assert b["source"] == URL and b["slice"] == CH59
    assert b["zip_last_modified"] == "Sun, 08 Nov 2026 21:26:00 GMT"
    nums = [s["law_section_row"].split("\t")[2].strip("`") for s in b["sections"]]
    assert sorted(nums) == ["11549.63.", "11549.64.", "11549.65.", "11549.66."]
    # raw: the rows are the dat file's lines, tabs and backticks included, the file is its bytes
    assert all(s["law_section_row"].startswith("`GOV") and "\t" in s["law_section_row"]
               for s in b["sections"])
    first = b["sections"][0]
    assert first["lob"].encode() == (PUB / "lobs" / first["lob_member"]).read_bytes()


def test_bundle_is_deterministic_so_a_second_fetch_hashes_the_same():
    assert bundle(CH59) == bundle(CH59)


def test_unknown_node_or_section_is_refused_not_guessed():
    with pytest.raises(ValueError, match="no table of contents node"):
        bundle({"code": "GOV", "path": "9.9.9"})
    with pytest.raises(ValueError, match="no section"):
        bundle({"code": "GOV", "section": "99999"})
    with pytest.raises(ValueError, match="slice"):
        bundle({"code": "GOV"})


# ---- the text -------------------------------------------------------------------------------

def test_chapter_text_opens_with_the_headings_down_to_the_chapter_then_its_sections_in_order():
    lines = text(CH59).splitlines()
    heads = [l for l in lines if l.startswith(("TITLE ", "DIVISION ", "PART ", "CHAPTER "))]
    assert heads[0] == "TITLE 2. GOVERNMENT OF THE STATE OF CALIFORNIA [8000. - 22980.]"
    assert heads[1].startswith("DIVISION 3. EXECUTIVE DEPARTMENT")
    assert heads[2].startswith("PART 1. STATE DEPARTMENTS AND AGENCIES")
    assert heads[3] == "CHAPTER 5.9. Generative Artificial Intelligence Tools [11549.63. - 11549.66.]"
    assert lines[lines.index(heads[3]) + 1].startswith("Chapter 5.9 added by Stats.")    # the table's own note
    starts = [l.split(" ", 1)[0] for l in lines if l[:9] in ("11549.63.", "11549.64.", "11549.65.", "11549.66.")]
    assert starts == ["11549.63.", "11549.64.", "11549.65.", "11549.66."]


def test_chapter_text_leaves_out_the_neighbouring_chapter():
    t = text(CH59)
    assert "11549.4." not in t and "Office of Information Security" not in t


def test_section_text_is_number_then_paragraphs_then_the_history_line_as_the_source_prints_it():
    lines = text(CH59).splitlines()
    i = next(n for n, l in enumerate(lines) if l.startswith("11549.64. "))
    assert lines[i] == ("11549.64. As used in this chapter:")
    assert lines[i + 1].startswith("(a) “Artificial intelligence” means an engineered or machine-based system")
    j = next(n for n in range(i, len(lines)) if lines[n].startswith("Added by Stats. 2024, Ch. 928, Sec. 2."))
    assert lines[j] == "Added by Stats. 2024, Ch. 928, Sec. 2. (SB 896) Effective January 1, 2025."
    assert lines[j + 1].startswith("11549.65. ")


def test_section_text_has_no_markup_no_tabs_and_no_enspace_runs():
    t = text(CH59)
    assert "<" not in t and "\t" not in t and "caml" not in t and "EnSpace" not in t
    assert "  " not in t
    assert all(l == l.strip() for l in t.splitlines())


def test_one_section_slice_is_that_section_under_every_heading_above_it():
    lines = text(GOV_11019_9).splitlines()
    assert any(l.startswith("CHAPTER 1. State Agencies") for l in lines)
    assert any(l.startswith("ARTICLE 1. General") for l in lines)
    secs = [l.split(" ", 1)[0] for l in lines if l[:1].isdigit()]
    assert secs == ["11019.9."]
    assert "11015.5." not in "\n".join(lines)


def test_article_headings_inside_a_chapter_slice_are_printed_before_their_sections():
    lines = text({"code": "GOV", "path": "3.3.1.10"}).splitlines()
    a1 = next(i for i, l in enumerate(lines) if l.startswith("ARTICLE 1. Office of Information Security"))
    a2 = next(i for i, l in enumerate(lines) if l.startswith("ARTICLE 2. Office of Privacy Protection"))
    s1 = next(i for i, l in enumerate(lines) if l.startswith("11549.1. "))
    s5 = next(i for i, l in enumerate(lines) if l.startswith("11549.5. "))
    assert a1 < s1 < a2 < s5


def test_italics_and_the_breach_notice_table_keep_their_words_one_line_per_paragraph():
    t = text({"code": "CIV", "path": "8.4.34.1"})
    assert "NOTICE OF DATA BREACH" in t.splitlines()
    assert "What Happened?" in t.splitlines()
    assert "<i>" not in t and "<td" not in t and "<br" not in t
    assert t.splitlines()[0].startswith("DIVISION 3. OBLIGATIONS")


def test_statute_text_gets_no_effective_date_and_its_own_conversion_notes():
    t = text(CH59)
    assert ing.effective_date(t, "statute") is None
    n = ing.conversion_notes({"doc_type": "statute", "jurisdiction": "california"}, "json", t)
    assert "pubinfo" in n and "chapter" not in n.lower().split("pubinfo")[0]
    assert "pdftotext" not in n


# ---- identity ---------------------------------------------------------------------------------

SRC_59 = {"id": "ca-gov-ch-5-9", "doc_type": "statute", "jurisdiction": "california",
          "citation": "Cal. Gov. Code §§ 11549.63-11549.66",
          "title": "Generative Artificial Intelligence Tools", "slice": CH59}
SRC_1 = {"id": "ca-gov-11019-9", "doc_type": "statute", "jurisdiction": "california",
         "citation": "Cal. Gov. Code § 11019.9", "title": "Privacy policy of each state agency",
         "slice": GOV_11019_9}


def test_identity_is_the_section_range_the_citation_names():
    ing.check_identity(SRC_59, text(CH59))
    ing.check_identity(SRC_1, text(GOV_11019_9))


def test_identity_refuses_a_citation_whose_range_is_not_the_slices():
    with pytest.raises(ValueError, match="not Cal. Gov. Code"):
        ing.check_identity(dict(SRC_59, citation="Cal. Gov. Code §§ 11549.63-11549.70"), text(CH59))
    with pytest.raises(ValueError, match="not Cal. Gov. Code"):
        ing.check_identity(dict(SRC_1, citation="Cal. Gov. Code § 11015.5"), text(GOV_11019_9))


def test_identity_refuses_a_code_the_citation_does_not_name():
    with pytest.raises(ValueError, match="not Cal. Civ. Code"):
        ing.check_identity(dict(SRC_59, citation="Cal. Civ. Code §§ 11549.63-11549.66"), text(CH59))


# ---- the fetch: range requests against the bulk file -----------------------------------------

def served(calls):
    def handler(request):
        calls.append((request.method, request.headers.get("range"), request.headers.get("user-agent")))
        headers = {"Last-Modified": "Sun, 08 Nov 2026 21:26:00 GMT", "Accept-Ranges": "bytes",
                   "Content-Type": "application/zip"}
        rng = request.headers.get("range")
        if request.method == "HEAD" or not rng:
            return httpx.Response(200, headers={**headers, "Content-Length": str(len(ZIP))},
                                  content=b"" if request.method == "HEAD" else ZIP)
        spec = rng.split("=", 1)[1]
        a, b = spec.split("-")
        if a == "":
            start, end = max(len(ZIP) - int(b), 0), len(ZIP) - 1
        else:
            start, end = int(a), min(int(b) if b else len(ZIP) - 1, len(ZIP) - 1)
        return httpx.Response(206, content=ZIP[start:end + 1], headers={
            **headers, "Content-Range": f"bytes {start}-{end}/{len(ZIP)}"})
    return handler


def make_fetcher(cfg, calls):
    return Fetcher(cfg, min_interval=0, transport=httpx.MockTransport(served(calls)),
                   sleep=lambda s: None)


def corpus(tmp_path, src):
    (tmp_path / "_meta").mkdir()
    shutil.copy(ROOT / "_meta" / "corpus.yml", tmp_path / "_meta" / "corpus.yml")
    (tmp_path / "_meta" / "source-manifest.yml").write_text(yaml.safe_dump({"sources": [src]}))
    return config_mod.load(tmp_path / "_meta" / "corpus.yml")


def full_src(base, **kw):
    return {**base, "url": URL, "format": "json", "issuing_body": "California Legislature",
            "tags": ["ai", "governance"], "why_relevant": "Government use of generative AI.", **kw}


def test_the_bulk_file_is_read_by_range_never_whole(tmp_path):
    calls = []
    cfg = corpus(tmp_path, full_src(SRC_59))
    with make_fetcher(cfg, calls) as f:
        ing.ingest(full_src(SRC_59), f, False, cfg)
    assert calls and all(rng for _, rng, _ in calls)          # every GET is a range request


def test_ingest_writes_the_bundle_as_the_snapshot_and_the_document_from_it(tmp_path):
    src = full_src(SRC_59)
    cfg = corpus(tmp_path, src)
    with make_fetcher(cfg, []) as f:
        out = ing.ingest(src, f, False, cfg)
    assert out == tmp_path / "statutes" / "california" / "ca-gov-ch-5-9.md"
    snap = tmp_path / "_meta" / "snapshots" / "ca-gov-ch-5-9.json"
    assert json.loads(snap.read_bytes())["source"] == URL
    fm, body = parse_frontmatter(out)
    full = body.split("## Full text\n", 1)[1].split("\n## ", 1)[0].strip()
    assert full == text(CH59).strip()
    assert fm["jurisdiction"] == "california" and fm["source_url"] == URL
    assert fm["source_format"] == "json" and fm["effective_date"] in (None, "")
    assert ing.check([src], cfg) == []          # offline: re-derived from the committed bundle


def test_a_cached_snapshot_is_not_fetched_again(tmp_path):
    src = full_src(SRC_59)
    cfg = corpus(tmp_path, src)
    with make_fetcher(cfg, []) as f:
        ing.ingest(src, f, False, cfg)
    calls = []
    with make_fetcher(cfg, calls) as f:
        ing.ingest(src, f, False, cfg)
    assert calls == []


def test_two_entries_of_one_download_read_the_zip_directory_once(tmp_path):
    a, b = full_src(SRC_59), full_src(SRC_1, tags=["data"])
    cfg = corpus(tmp_path, a)
    calls = []
    with make_fetcher(cfg, calls) as f:
        ing.ingest(a, f, False, cfg)
        n = len(calls)
        ing.ingest(b, f, False, cfg)
    assert len(calls) - n < n


def test_a_slice_that_is_not_in_the_download_leaves_no_snapshot(tmp_path):
    src = full_src(dict(SRC_59, slice={"code": "GOV", "path": "9.9.9"}))
    cfg = corpus(tmp_path, src)
    with make_fetcher(cfg, []) as f:
        with pytest.raises(ValueError):
            ing.ingest(src, f, False, cfg)
    assert not list((tmp_path / "_meta" / "snapshots").glob("ca-gov-ch-5-9.*"))


# ---- the seed list accepts these slices -------------------------------------------------------

DOMAIN = yaml.safe_load((ROOT / "_meta" / "domain.yml").read_text())


def seed(**kw):
    e = {"id": "ca-x", "url": URL, "format": "json", "citation": "c", "title": "t", "doc_type": "statute",
         "jurisdiction": "california", "tags": ["data"], "why_relevant": "w"}
    e.update(kw)
    return {"sources": [e]}


def test_seed_check_accepts_a_pubinfo_slice_by_path_or_by_section():
    assert csl.check(seed(slice=CH59), DOMAIN) == []
    assert csl.check(seed(slice=GOV_11019_9), DOMAIN) == []


def test_seed_check_refuses_a_malformed_pubinfo_slice():
    assert csl.check(seed(slice={"code": "GOV"}), DOMAIN)
    assert csl.check(seed(slice={"path": "3.3.1.12"}), DOMAIN)
    assert csl.check(seed(slice={"code": "GOV", "path": "3.3", "section": "1"}), DOMAIN)
    assert csl.check(seed(slice={"code": "GOV", "path": 3.3}), DOMAIN)


def test_seed_check_still_treats_one_zip_with_different_slices_as_different_documents():
    two = {"sources": [seed(slice=CH59)["sources"][0],
                       dict(seed(slice=GOV_11019_9)["sources"][0], id="ca-y")]}
    assert csl.check(two, DOMAIN) == []
    same = {"sources": [seed(slice=CH59)["sources"][0], dict(seed(slice=CH59)["sources"][0], id="ca-y")]}
    assert any("duplicate url" in e for e in csl.check(same, DOMAIN))


# ---- the fetch discipline the Fetcher's own get has: refusal, challenge, 429 backoff -------------

def status_fetcher(statuses, headers=None, sleeps=None):
    """A Fetcher whose first range request (the 1-byte probe) answers per `statuses`, then 206."""
    seq = list(statuses)

    def handler(request):
        code = seq.pop(0) if seq else 206
        if code != 206:
            return httpx.Response(code, headers=headers or {})
        return httpx.Response(206, content=b"x", headers={"Content-Range": f"bytes 0-0/{len(ZIP)}"})
    return Fetcher(None, min_interval=0, transport=httpx.MockTransport(handler),
                   sleep=(sleeps.append if sleeps is not None else (lambda s: None)))


def test_a_403_on_a_range_request_is_a_refusal_not_a_generic_error():
    from corpus_toolkit.sources.fetch import Refused
    with status_fetcher([403]) as f, pytest.raises(Refused, match="403"):
        ing.CaZip(f, URL)


def test_a_cloudflare_challenge_on_a_range_request_is_a_challenge():
    from corpus_toolkit.sources.fetch import Challenge
    with status_fetcher([403], headers={"cf-mitigated": "challenge"}) as f, pytest.raises(Challenge):
        ing.CaZip(f, URL)


def test_a_429_on_a_range_request_is_waited_out_then_retried():
    sleeps = []
    with status_fetcher([429, 429], headers={"Retry-After": "7"}, sleeps=sleeps) as f:
        z = ing.CaZip(f, URL)
    assert z.size == len(ZIP) and sleeps == [7.0, 7.0]


def test_a_429_that_never_clears_is_refused_after_the_backoff_steps():
    from corpus_toolkit.sources.fetch import Refused
    with status_fetcher([429] * 20) as f, pytest.raises(Refused, match="429"):
        ing.CaZip(f, URL)


def test_a_later_block_read_gets_the_same_discipline():
    from corpus_toolkit.sources.fetch import Refused
    with status_fetcher([206, 403]) as f:
        z = ing.CaZip(f, URL)
        with pytest.raises(Refused, match="403"):
            z.read(10)

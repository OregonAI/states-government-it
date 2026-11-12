"""Seam: src.states / src.ingest for New Mexico. Seams under test: the statute slice (the Compilation
Commission's whole-chapter PDF on nmonesource.com cut to one article, by the state's `snapshot` and `to_text`),
the SRCA's Word-HTML rule page, and the identity checks, dates and versions of the DoIT PDFs.

Fixtures are cut from real bytes fetched 2026-11-12: the page text of pages 413-446 of the Chapter 9 PDF
(end of Article 26, all of Articles 27 and 27A, the heading of Article 28), the whole SRCA page of 1.12.7 NMAC,
and the first 70 lines of real DoIT PDFs, page furniture (DocuSign envelope line, Register header) included."""
import json
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "new-mexico"
PAGES = (FIX / "nmsa-chapter-9-pages-413-446.txt").read_text(encoding="utf-8").split("\f")
RULE_HTML = (FIX / "srca-1-12-7.html").read_bytes()


def head(name):
    return (FIX / name).read_text(encoding="utf-8")


NM = states.modules()["new-mexico"]


# ---- statute slices ------------------------------------------------------------------------------

def bundle(article):
    return NM.slice_bundle(PAGES, article, url="https://example.test/ch9", chapter_sha256="0" * 64)


def statute_text(article):
    return ing.to_text(bundle(article), "json", "statute", "new-mexico", {"article": article})


def test_article_27_slice_runs_from_its_heading_to_the_next_article_heading():
    lines = statute_text("27").splitlines()
    assert lines[:2] == ["ARTICLE 27", "Department of Information Technology"]
    assert any(l.startswith("9-27-1. Short title.") for l in lines)
    assert not any(l == "ARTICLE 27A" or l == "ARTICLE 26" for l in lines)
    assert "Cybersecurity Act" not in "\n".join(lines)          # 27A is not in the 27 slice


def test_article_27a_slice_stops_before_article_28():
    t = statute_text("27A")
    assert t.startswith("ARTICLE 27A\nCybersecurity\n9-27A-1. Short title.")
    assert 'may be cited as the "Cybersecurity Act"' in t
    assert "ARTICLE 28" not in t and "Homeland Security" not in t


def test_slice_keeps_the_annotations_and_history_lines_as_printed():
    t = statute_text("27A")
    assert "History: Laws 2023, ch. 115, § 1." in t
    assert "ANNOTATIONS" in t


def test_slice_text_has_no_form_feeds_or_trailing_spaces():
    t = statute_text("27")
    assert "\f" not in t and all(l == l.rstrip() for l in t.splitlines())
    assert "\n\n\n" not in t


def test_bundle_records_where_it_came_from_and_which_pages_it_holds():
    doc = json.loads(bundle("27A"))
    assert doc["format"] == "nmos-chapter-slice/1"
    assert doc["article"] == "27A" and doc["url"] == "https://example.test/ch9"
    assert len(doc["pages"]) == doc["last_page"] - doc["first_page"] + 1


def test_an_article_that_is_not_in_the_chapter_is_refused():
    with pytest.raises(ValueError, match="no heading 'ARTICLE 99'"):
        bundle("99")


def test_a_bundle_of_another_format_is_refused():
    with pytest.raises(ValueError, match="not a New Mexico slice bundle"):
        ing.to_text(b'{"format": "other"}', "json", "statute", "new-mexico", {"article": "27"})


STAT = {"id": "nm-nmsa-9-27", "jurisdiction": "new-mexico", "doc_type": "statute",
        "citation": "NMSA 1978, chapter 9, article 27", "title": "Department of Information Technology"}


def test_statute_identity_accepts_its_article_and_refuses_another():
    states.check_identity(STAT, statute_text("27"), "json")
    with pytest.raises(ValueError, match="not NMSA 1978, chapter 9, article 27A"):
        states.check_identity({**STAT, "citation": "NMSA 1978, chapter 9, article 27A"}, statute_text("27"), "json")


def test_statute_identity_refuses_a_title_that_the_heading_does_not_print():
    with pytest.raises(ValueError, match="title"):
        states.check_identity({**STAT, "title": "Cybersecurity"}, statute_text("27"), "json")


def test_snapshot_hook_builds_the_bundle_from_the_chapter_pdf_and_reuses_a_committed_one(tmp_path, monkeypatch):
    calls = []

    class Fetched:
        body = b"%PDF fake chapter"

    class Fake:
        def get(self, url):
            calls.append(url)
            return Fetched()

    monkeypatch.setattr(NM, "_pdf_pages", lambda raw: PAGES)
    src = {**STAT, "url": "https://example.test/ch9", "slice": {"article": "27"}}
    dest = tmp_path / "nm-nmsa-9-27.json"
    raw, fresh = NM.snapshot(src, Fake(), dest, False)
    assert fresh and json.loads(raw)["article"] == "27" and dest.read_bytes() == raw
    raw2, fresh2 = NM.snapshot(src, Fake(), dest, False)
    assert not fresh2 and raw2 == raw and calls == ["https://example.test/ch9"]


def test_snapshot_hook_leaves_other_entries_to_the_shared_fetch():
    assert NM.snapshot({"doc_type": "policy", "url": "x"}, None, Path("x"), False) is None


# ---- rules ---------------------------------------------------------------------------------------

RULE7 = {"id": "nm-nmac-1-12-7", "jurisdiction": "new-mexico", "doc_type": "rule",
         "citation": "1.12.7 NMAC", "title": "Digital / Electronic Signature"}


def test_srca_word_html_rule_page_becomes_one_line_per_paragraph():
    t = ing.to_text(RULE_HTML, "html", "rule", "new-mexico")
    lines = t.splitlines()
    assert lines[:3] == ["TITLE 1 GENERAL GOVERNMENT", "CHAPTER 12 INFORMATION TECHNOLOGY",
                         "PART 7 DIGITAL / ELECTRONIC SIGNATURE"]
    assert "[1.12.7.1 NMAC - Rp, NMAC 1.12.7.1, 7/1/2015]" in lines
    assert "Style Definitions" not in t and "<" not in t


def test_rule_identity_reads_the_part_heading_and_refuses_another_part():
    text = ing.to_text(RULE_HTML, "html", "rule", "new-mexico")
    states.check_identity(RULE7, text, "html")
    with pytest.raises(ValueError, match="1.12.8 NMAC"):
        states.check_identity({**RULE7, "citation": "1.12.8 NMAC"}, text, "html")
    with pytest.raises(ValueError, match="title"):
        states.check_identity({**RULE7, "title": "Electronic Authentication"}, text, "html")


def test_rule_pdf_with_a_register_header_line_is_still_identified_by_its_part_heading():
    text = head("rule-1-12-5-head.txt")
    src = {**RULE7, "citation": "1.12.5 NMAC", "title": "Oversight of Information Technology Projects"}
    states.check_identity(src, text, "PDF")
    with pytest.raises(ValueError):
        states.check_identity({**src, "citation": "1.12.9 NMAC"}, text, "PDF")


def test_rule_effective_date_is_the_one_the_rule_prints():
    text = ing.to_text(RULE_HTML, "html", "rule", "new-mexico")
    assert states.effective_date(text, "rule", "new-mexico") == "2015-07-01"


# ---- policies and standards ----------------------------------------------------------------------

def std(code, title):
    return {"id": "x", "jurisdiction": "new-mexico", "doc_type": "standard", "citation": code, "title": title}


def test_standard_identity_needs_its_printed_title_and_its_code():
    text = head("std-s-std-003-head.txt")
    states.check_identity(std("S-STD-003", "IT Risk Management Standard"), text, "PDF")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(std("S-STD-004", "IT Risk Management Standard"), text, "PDF")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(std("S-STD-003", "Firewall Functionality Standard"), text, "PDF")


def test_standard_code_is_read_through_the_file_s_own_spelling_of_it():
    # the file prints "NDT-STD008.001" for what the index calls N-STD-008
    states.check_identity(std("N-STD-008", "Wireless Access Point Hardware"), head("std-n-std-008-head.txt"), "PDF")


def test_policy_with_no_code_is_identified_by_its_identity_text_in_the_title_block():
    src = {"id": "x", "jurisdiction": "new-mexico", "doc_type": "policy", "citation": "Generative AI Use Guidelines Policy v1.0",
           "title": "Generative AI Use Guidelines Policy"}
    states.check_identity(src, head("gen-ai-policy-head.txt"), "PDF")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**src, "title": "Data Policy"}, head("gen-ai-policy-head.txt"), "PDF")


def test_ciso_order_is_identified_by_identity_text_and_dated_by_its_signature_line():
    text = head("ciso-order-2025-01-head.txt")
    src = {"id": "x", "jurisdiction": "new-mexico", "doc_type": "policy", "citation": "CISO Order No. 2025-01",
           "title": "Cybersecurity Incident Reporting", "identity_text": "ORDER NO. 2025-01"}
    states.check_identity(src, text, "PDF")
    assert "DONE AND ORDERED" not in text          # the head fixture stops before the signature
    full = text + "\n   DONE AND ORDERED THIS 30th DAY OF JUNE, 2025\n"
    assert states.effective_date(full, "policy", "new-mexico") == "2025-06-30"


def test_policy_version_is_the_one_printed_beside_the_title():
    text = head("gen-ai-policy-head.txt")
    assert states.source_version(text, "policy", "new-mexico", "pdf") == "Version 1.0 (6/2025)"
    assert states.source_version(head("std-s-std-003-head.txt"), "standard", "new-mexico", "pdf") == ""


def test_standard_effective_date_is_read_by_the_shared_label_reader():
    assert states.effective_date(head("std-s-std-003-head.txt"), "standard", "new-mexico") == "2005-04-07"


# ---- executive orders (scans, read by OCR) -------------------------------------------------------

def eo(cite):
    return {"id": "x", "jurisdiction": "new-mexico", "doc_type": "executive_order", "citation": cite,
            "title": "t"}


def test_executive_order_identity_matches_the_heading_line_not_a_mention_of_the_number():
    ocr = "State of New Mexico\nOffice of the Governor\nBill Richardson\nGovernor\n\nEXECUTIVE ORDER NO. 2008-011\n\nCLARIFYING THE CONSOLIDATION\n"
    states.check_identity(eo("Executive Order 2008-011"), ocr, "PDF")
    with pytest.raises(ValueError, match="heading line"):
        states.check_identity(eo("Executive Order 2008-01"), ocr, "PDF")
    mention = "EXECUTIVE ORDER 2024-011\nSTRENGTHENING\nwhich amends Executive Order 2008-011 in part\n"
    with pytest.raises(ValueError, match="2008-011"):
        states.check_identity(eo("Executive Order 2008-011"), mention, "PDF")


def test_executive_order_identity_refuses_an_unreadable_heading_when_the_number_is_only_in_the_body():
    ocr = ("State of New Mexico\nOffice of the Governor\n\nEXECUTIVE ORDER 2O24-O11\nCLARIFYING THE CONSOLIDATION\n\n"
           "WHEREAS Executive Order 2008-011 established the commission;\n")
    with pytest.raises(ValueError, match="heading line"):
        states.check_identity(eo("Executive Order 2008-011"), ocr, "PDF")
    twice = "EXECUTIVE ORDER 2024-011\nTITLE\nEXECUTIVE ORDER 2008-011\n"
    with pytest.raises(ValueError, match="heading line"):
        states.check_identity(eo("Executive Order 2008-011"), twice, "PDF")


# ---- notes ---------------------------------------------------------------------------------------

def test_notes_say_how_the_statute_slice_and_the_rule_page_were_read():
    n = NM.notes({"doc_type": "statute", "citation": "c"}, "json", "")
    assert "Chapter 9" in n and "annotations" in n.lower()
    r = NM.notes({"doc_type": "rule", "citation": "1.12.7 NMAC"}, "html", "")
    assert "State Records Center and Archives" in r


def test_extra_notes_warn_when_a_pdf_prints_ff_as_a_stray_letter():
    assert "Ư" in NM.extra_notes({}, "pdf", "eƯiciency", None, "")
    assert NM.extra_notes({}, "pdf", "efficiency", None, "") == ""

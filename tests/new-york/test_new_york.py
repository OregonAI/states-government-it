"""Seam: the New York state module through src.ingest (to_text, check_identity, conversion_notes) and the
`snapshot` hook the ingester calls. Fixtures are real bytes fetched on 2026-11-11: two articles of the State
Technology Law from the Senate's Open Legislation API (the key is not in them) and ITS's page for 9 NYCRR
Part 551, whole, with its navigation and footer."""
import json
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "new-york"
ART4 = (FIX / "stt-article-4.json").read_bytes()
ART5 = (FIX / "stt-article-5.json").read_bytes()
PART551 = (FIX / "its-part-551.html").read_bytes()
NY = "new-york"


def statute_text(raw, location):
    return ing.to_text(raw, "json", "statute", NY, {"article": location})


def test_the_state_is_found_by_its_hyphenated_name():
    assert NY in states.modules()


# ---- statutes: Open Legislation API JSON -------------------------------------------------

def test_statute_text_is_the_article_then_each_section_in_order_with_real_line_breaks():
    t = statute_text(ART4, "A4")
    lines = t.splitlines()
    assert lines[0].strip() == "ARTICLE IV"
    assert "\\n" not in t                      # the API stores a line break as backslash + n
    assert t.index("§ 401. Definitions.") < t.index("§ 402.") < t.index("§ 402-a.")
    assert '"Automated employment decision-making tool" shall mean any software' in t
    assert t.endswith("\n") and not t.endswith("\n\n")
    assert all(l == l.rstrip() for l in lines)


def test_statute_text_keeps_the_notes_the_source_prints():
    t = statute_text(ART5, "A5")
    assert lines_of(t)[0] == "* ARTICLE V"
    assert "NB Repealed July 1, 2028" in t


def lines_of(t):
    return [l.strip() for l in t.splitlines()]


def test_statute_to_text_refuses_json_that_is_not_the_cited_article():
    with pytest.raises(ValueError, match="not the article"):
        ing.to_text(ART4, "json", "statute", NY, {"article": "A5"})
    with pytest.raises(ValueError, match="not the article"):
        ing.to_text(ART4.replace(b'"lawId" : "STT"', b'"lawId" : "EXC"'), "json", "statute", NY, {"article": "A4"})
    with pytest.raises(ValueError, match="not a law tree"):
        ing.to_text(b'{"success": false, "message": "Invalid key"}', "json", "statute", NY,
                    {"article": "A4"})


def src_for(**kw):
    base = {"id": "ny-x", "jurisdiction": NY, "doc_type": "statute", "citation": "State Technology Law, Article 4",
            "title": "t", "url": "https://legislation.nysenate.gov/api/3/laws/STT?full=true&fromLocation=A4&toLocation=A4"}
    return {**base, **kw}


def test_statute_identity_is_the_article_numeral_the_citation_names():
    ing.check_identity(src_for(), statute_text(ART4, "A4"), "json")
    ing.check_identity(src_for(citation="State Technology Law, Article 5"), statute_text(ART5, "A5"), "json")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(src_for(), statute_text(ART5, "A5"), "json")


# ---- rules: ITS's own page of a NYCRR part ------------------------------------------------

def test_rule_text_is_the_part_without_site_navigation_or_footer():
    t = ing.to_text(PART551, "html", "rule", NY)
    lines = t.splitlines()
    assert lines[0] == "CIO/OFT Personal Privacy Protection Regulations"
    assert "PART 551." in lines and "ACCESS TO PERSONAL INFORMATION" in lines
    assert any(l.startswith("Section 551.1 Purpose and scope.") for l in lines)
    assert any(l.startswith("(a) It is the responsibility and the intent of the Office of Information") for l in lines)
    assert any(l.startswith("(c) When providing a data subject's statement of disagreement") for l in lines)
    for furniture in ("Skip to main", "Facebook", "Meet the Executive Team", "Privacy Policy", "<", "\xa0", "&nbsp;"):
        assert furniture not in t
    assert all(l == l.strip() for l in lines)


def test_rule_to_text_refuses_a_page_with_no_content_region():
    with pytest.raises(ValueError, match="layout changed"):
        ing.to_text(b"<html><body><p>Not found</p></body></html>", "html", "rule", NY)


def test_rule_identity_is_the_part_number_the_citation_names():
    src = {"id": "ny-r", "jurisdiction": NY, "doc_type": "rule", "citation": "9 NYCRR Part 551", "title": "t"}
    ing.check_identity(src, ing.to_text(PART551, "html", "rule", NY), "html")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity({**src, "citation": "9 NYCRR Part 540"}, ing.to_text(PART551, "html", "rule", NY), "html")


# ---- executive orders ----------------------------------------------------------------------

def test_executive_order_identity_is_the_number_in_the_orders_own_heading():
    src = {"id": "ny-eo", "jurisdiction": NY, "doc_type": "executive_order",
           "citation": "Executive Order No. 117", "title": "t"}
    ing.check_identity(src, "STATE OF NEW YORK\nEXECUTIVE CHAMBER\nEXECUTIVE ORDER No. 117\n\nWHEREAS", "pdf")
    ing.check_identity(src, "STATE OF NEW YORK\nE X E C U T I V E O R D E R N o. 1 1 7\nWHEREAS", "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(src, "EXECUTIVE ORDER No. 1170\n", "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(src, "The CIO was established by Executive Order No. 117, issued in 2002.\n" * 3, "pdf")


# ---- conversion notes ----------------------------------------------------------------------

def test_notes_say_how_the_statute_and_the_rule_were_read_and_that_the_key_is_not_kept():
    s = ing.conversion_notes(src_for(), "json", statute_text(ART4, "A4"))
    assert "Open Legislation API" in s and "backslash" in s and "key" in s
    r = ing.conversion_notes({"id": "r", "jurisdiction": NY, "doc_type": "rule", "citation": "c", "title": "t"},
                             "html", "x")
    assert "page-body" in r or "content region" in r


# ---- the snapshot hook: the key goes on the request and nowhere else ----------------------------

KEY = "TESTKEY0123456789abcdef"


class FakeFetcher:
    def __init__(self, body=b'{"result": {}}', exc=None):
        self.urls, self.body, self.exc = [], body, exc

    def get(self, url):
        self.urls.append(url)
        if self.exc:
            raise self.exc(f"GET {url} failed")
        return type("F", (), {"body": self.body, "status": 200})()


@pytest.fixture
def keyed(monkeypatch):
    monkeypatch.setenv("NY_OPENLEG_KEY", KEY)


def test_the_key_is_added_to_the_request_and_never_saved(tmp_path, keyed):
    f = FakeFetcher(body=('{"echo": "%s", "x": 1}' % KEY).encode())
    dest = tmp_path / "a.json"
    raw, fresh = states.hook(NY, "snapshot")(src_for(), f, dest, False)
    assert f.urls == [src_for()["url"] + "&key=" + KEY]
    assert fresh and KEY.encode() not in raw and KEY.encode() not in dest.read_bytes()
    assert json.loads(raw)["x"] == 1


def test_a_cached_snapshot_is_reused_without_a_request_or_a_key(tmp_path, monkeypatch):
    monkeypatch.delenv("NY_OPENLEG_KEY", raising=False)
    monkeypatch.setenv("NY_OPENLEG_KEY_FILE", str(tmp_path / "absent"))
    dest = tmp_path / "a.json"
    dest.write_bytes(b"cached")
    f = FakeFetcher()
    assert states.hook(NY, "snapshot")(src_for(), f, dest, False) == (b"cached", False)
    assert f.urls == []


def test_without_a_key_a_statute_is_refused_before_any_request(tmp_path, monkeypatch):
    monkeypatch.delenv("NY_OPENLEG_KEY", raising=False)
    monkeypatch.setenv("NY_OPENLEG_KEY_FILE", str(tmp_path / "absent"))
    f = FakeFetcher()
    with pytest.raises(ValueError, match="Open Legislation API key"):
        states.hook(NY, "snapshot")(src_for(), f, tmp_path / "a.json", False)
    assert f.urls == []


def test_an_error_that_quotes_the_request_url_does_not_carry_the_key(tmp_path, keyed):
    f = FakeFetcher(exc=RuntimeError)
    with pytest.raises(ValueError) as e:
        states.hook(NY, "snapshot")(src_for(), f, tmp_path / "a.json", False)
    assert KEY not in str(e.value) and "failed" in str(e.value)
    assert not (tmp_path / "a.json").exists()


def test_other_pages_are_one_plain_get(tmp_path, keyed):
    assert states.hook(NY, "snapshot")({"url": "https://its.ny.gov/x", "doc_type": "rule"},
                                       FakeFetcher(), tmp_path / "a.html", False) is None


# ---- an executive order ITS prints on its own site -------------------------------------------

EO117 = (FIX / "its-executive-order-117.html").read_bytes()


def test_executive_order_page_text_is_the_order_from_its_heading_to_the_signature_block():
    t = ing.to_text(EO117, "html", "executive_order", NY)
    lines = t.splitlines()
    assert lines[0] == "Executive Order 117"
    assert "ESTABLISHING THE POSITION OF CHIEF INFORMATION OFFICER (CIO)" in lines
    assert any(l.startswith("NOW, THEREFORE, I, GEORGE E. PATAKI, Governor of the State of New York") for l in lines)
    assert "Overseeing and supervising the management and operations of the Office for Technology;" in lines
    assert any(l.startswith("/s/ Bradford J. Race") for l in lines)
    for furniture in ("Skip to main", "Facebook", "Press Releases", "<", "\xa0"):
        assert furniture not in t
    src = {"id": "ny-eo-117", "jurisdiction": NY, "doc_type": "executive_order",
           "citation": "Executive Order No. 117", "title": "t"}
    ing.check_identity(src, t, "html")


def test_executive_order_notes_say_the_copy_is_itss_and_why_not_the_governors_scan():
    src = {"id": "ny-eo-117", "jurisdiction": NY, "doc_type": "executive_order",
           "citation": "Executive Order No. 117", "title": "t"}
    n = ing.conversion_notes(src, "html", "x")
    assert "its.ny.gov" in n and "scan" in n and "OCR" in n


# ---- policy and standard PDFs: the date the header block prints ----------------------------
# Fixtures are the first 30 lines of the pdftotext output of three real library PDFs (page furniture kept).

def header(name):
    return (FIX / f"its-header-{name}.txt").read_text(encoding="utf-8")


def version(text, doc_type="policy", fmt="pdf"):
    return ing.source_version(text, doc_type, NY, fmt)


def test_source_version_is_the_updated_date_the_header_prints():
    assert version(header("updated")) == "Updated: 12/22/2020"


def test_source_version_is_the_issued_date_when_that_is_the_label():
    assert version(header("issued")) == "Issued: 04/06/2023"       # 'Issued By:' on the next lines is not a date


def test_source_version_is_the_released_date_when_that_is_the_label():
    assert version(header("released")) == "Released: 10/27/2026"


def test_source_version_reads_the_header_block_only():
    body = header("updated") + "\n" * 40 + "Revision history\n   Updated: 01/01/1999\n"
    assert version(body) == "Updated: 12/22/2020"
    assert version("\n" * 45 + "Updated: 01/01/1999\n") == ""


def test_source_version_is_empty_when_the_header_prints_no_date_and_for_other_types():
    assert version("No: ITS-P20-001\nIssued By: NYS Office of Information\n") == ""
    assert version(header("updated"), doc_type="statute", fmt="json") == ""


def test_source_version_keeps_a_two_digit_year_as_printed():
    assert version(header("updated-two-digit-year")) == "Updated: 01/15/25"      # NYS-S16-001 prints it so

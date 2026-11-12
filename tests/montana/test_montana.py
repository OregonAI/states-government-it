"""Montana: the Legislature's Montana Code Annotated section pages (one page per section, bundled into one document by the
seed entry's `sections`) and the Governor's executive orders (PDFs). Fixtures are real bytes with their page furniture:
three whole MCA section pages (navigation bar, breadcrumb, footer disclaimer, the host's injected script) and the whole
pdftotext reading of Executive Order 3-2025 (title block, signature block)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import montana
from tests.seedutil import make_corpus, make_fetcher

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "montana"
P511 = (FIX / "mca-2-17-511.html").read_bytes()
P516 = (FIX / "mca-2-17-516.html").read_bytes()
P21_102 = (FIX / "mca-2-21-102.html").read_bytes()
P18_603 = (FIX / "mca-18-5-603.html").read_bytes()
EO_3_2025 = (FIX / "eo-3-2025.pdftotext.txt").read_text()

MITA = {"id": "mt-mca-test", "jurisdiction": "montana", "doc_type": "statute", "format": "html",
        "sections": ["2-17-511", "2-17-516"], "citation": "Mont. Code Ann. 2-17-511, 2-17-516",
        "title": "test", "url": montana.section_url("2-17-511")}


def test_the_state_is_found_by_name():
    assert "montana" in states.modules(refresh=True)


def test_a_section_url_is_built_from_its_number():
    assert montana.section_url("2-17-511") == \
        "https://mca.legmt.gov/bills/mca/title_0020/chapter_0170/part_0050/section_0110/0020-0170-0050-0110.html"
    assert montana.section_url("2-17-1101").endswith("chapter_0170/part_0110/section_0010/0020-0170-0110-0010.html")
    assert montana.section_url("2-6-1501").endswith("chapter_0060/part_0150/section_0010/0020-0060-0150-0010.html")
    assert montana.section_url("2-21-102").endswith("chapter_0210/part_0010/section_0020/0020-0210-0010-0020.html")
    assert montana.section_url("2-15-1021").endswith("chapter_0150/part_0100/section_0210/0020-0150-0100-0210.html")


def test_a_section_page_gives_its_content_and_nothing_around_it():
    frag = montana.section_fragment(P511).decode()
    assert frag.startswith('<div class="mca-content') and "carrying out all powers and duties" in frag
    assert "Previous Section" not in frag and "Disclaimer" not in frag and "APM_DO_NOT_TOUCH" not in frag
    assert montana.section_fragment(b"<html>not a section page</html>") is None


def _bundle(*pages):
    return montana.build_bundle([(montana.section_url(n), montana.section_fragment(p)) for n, p in pages])


def test_a_bundle_is_the_code_header_once_then_each_section_with_its_history():
    text = montana.statute_to_text(_bundle(("2-17-511", P511), ("2-17-516", P516)))
    lines = text.splitlines()
    assert lines[:4] == ["Montana Code Annotated 2025",
                         "TITLE 2. GOVERNMENT STRUCTURE AND ADMINISTRATION",
                         "CHAPTER 17. PROPERTY AND SYSTEMS DEVELOPMENT AND MANAGEMENT",
                         "Part 5. Information Technology -- Internet Privacy"]
    assert lines.count("Montana Code Annotated 2025") == 1
    assert "2-17-511. Chief information officer -- duties. The duties of the chief information officer include but are not limited to:" in lines
    assert "(1) carrying out all powers and duties of the department as assigned by the director of the department;" in lines
    assert "History: En. Sec. 5, Ch. 313, L. 2001." in lines
    assert text.count("\n\n2-17-516. Exemptions -- department of justice") == 1
    for leak in ("Previous Section", "Disclaimer", "<", "&#", "\t", " ", "MCA Contents"):
        assert leak not in text


def test_a_bundle_with_no_section_is_refused():
    with pytest.raises(ValueError, match="no statute text"):
        montana.statute_to_text(b"")


def test_sections_under_different_parts_are_refused_in_one_bundle():
    with pytest.raises(ValueError, match="more than one"):
        montana.statute_to_text(_bundle(("2-17-511", P511), ("2-21-102", P21_102)))


def test_the_snapshot_fetches_each_listed_section_once_and_caches_the_bundle(tmp_path):
    cfg = make_corpus(tmp_path, [])
    calls = []
    routes = {montana.section_url("2-17-511"): (200, P511), montana.section_url("2-17-516"): (200, P516)}
    dest = tmp_path / "snap.html"
    with make_fetcher(cfg, routes, calls) as f:
        raw, fresh = montana.snapshot(MITA, f, dest, False)
        again, fresh2 = montana.snapshot(MITA, f, dest, False)
    assert fresh and not fresh2 and again == raw == dest.read_bytes()
    assert calls == [montana.section_url("2-17-511"), montana.section_url("2-17-516")]
    assert raw.decode().count(montana.SECTION_MARK) == 2
    assert montana.snapshot({**MITA, "sections": None}, None, dest, False) is None      # not a statute bundle


def test_a_section_the_site_does_not_have_is_an_error_and_writes_nothing(tmp_path):
    cfg = make_corpus(tmp_path, [])
    routes = {montana.section_url("2-17-511"): (200, P511), montana.section_url("2-17-516"): (404, b"")}
    dest = tmp_path / "snap.html"
    with make_fetcher(cfg, routes) as f:
        with pytest.raises(ValueError, match="2-17-516"):
            montana.snapshot(MITA, f, dest, False)
    assert not dest.exists()


def test_a_page_that_is_not_a_section_page_is_an_error(tmp_path):
    cfg = make_corpus(tmp_path, [])
    routes = {montana.section_url("2-17-511"): (200, b"<html><body>Request unsuccessful</body></html>")}
    with make_fetcher(cfg, routes) as f:
        with pytest.raises(ValueError, match="2-17-511"):
            montana.snapshot({**MITA, "sections": ["2-17-511"]}, f, tmp_path / "s.html", False)


def test_statute_identity_needs_exactly_the_listed_sections_in_order():
    text = montana.statute_to_text(_bundle(("2-17-511", P511), ("2-17-516", P516)))
    states.check_identity(MITA, text, "html")
    with pytest.raises(ValueError, match="2-17-512 does not appear"):
        states.check_identity({**MITA, "sections": ["2-17-511", "2-17-512"]}, text, "html")
    with pytest.raises(ValueError, match="does not list"):
        states.check_identity({**MITA, "sections": ["2-17-511"]}, text, "html")
    with pytest.raises(ValueError, match="another order"):
        states.check_identity({**MITA, "sections": ["2-17-516", "2-17-511"]}, text, "html")


def test_the_shared_flow_reads_a_statute_bundle_and_prints_its_edition():
    bundle = _bundle(("2-17-511", P511))
    assert ing.to_text(bundle, "html", "statute", "montana", None, "mca.legmt.gov").startswith("Montana Code Annotated 2025")
    text = montana.statute_to_text(bundle)
    assert states.source_version(text, "statute", "montana", "html") == "Montana Code Annotated 2025"
    assert states.effective_date(text, "statute", "montana") is None


# ---- executive orders ------------------------------------------------------------------------

EO = {"id": "mt-eo-3-2025", "jurisdiction": "montana", "doc_type": "executive_order", "format": "pdf",
      "citation": "Executive Order No. 3-2025", "title": "Integrating Information Technology Resources"}


def test_an_executive_order_is_identified_by_its_own_heading_line():
    states.check_identity(EO, EO_3_2025, "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**EO, "citation": "Executive Order No. 4-2025"}, EO_3_2025, "pdf")
    # a mention of the number is not the heading
    mention = "STATE OF MONTANA\nEXECUTIVE ORDER No. 5-2025\n\nThis order amends Executive Order No. 3-2025.\n"
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity(EO, mention, "pdf")
    # a two-digit number is zero-padded by the Governor's office in some orders ("NO. 09-2016")
    scan = "STATE OF MONTANA\nOFFICE OF THE GOVERNOR\nEXECUTIVE ORDER NO. 09-2016\n"
    states.check_identity({**EO, "citation": "Executive Order No. 9-2016"}, scan, "pdf")
    with pytest.raises(ValueError, match="not the cited instrument"):
        states.check_identity({**EO, "citation": "Executive Order No. 19-2016"}, scan, "pdf")


def test_an_executive_order_prints_the_date_it_takes_effect():
    assert states.effective_date(EO_3_2025, "executive_order", "montana") == "2025-07-01"
    assert states.effective_date("EXECUTIVE ORDER NO. 1-2020\nThis Order is effective immediately.\n",
                                 "executive_order", "montana") is None


def test_a_title_18_section_page_is_addressed_and_read_like_any_other():
    assert montana.section_url("18-5-601").endswith("title_0180/chapter_0050/part_0060/section_0010/0180-0050-0060-0010.html")
    text = montana.statute_to_text(_bundle(("18-5-603", P18_603)))
    lines = text.splitlines()
    assert lines[1:4] == ["TITLE 18. PUBLIC CONTRACTS", "CHAPTER 5. SPECIAL PURCHASING CONDITIONS",
                          "Part 6. Nonvisual Access Technology Procurement"]
    assert "the state agency head shall ensure that the equipment or software:" in text
    assert "Disclaimer" not in text

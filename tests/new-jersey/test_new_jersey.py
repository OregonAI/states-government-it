"""New Jersey: the Legislature's statutes bulk file (one text file of every section) and the Governor's
infobank pages. Fixtures are cut from the bytes the sources served on 2026-11-11."""
import importlib
import json
from pathlib import Path

import pytest

FX = Path(__file__).parent.parent / "fixtures" / "new-jersey"
nj = importlib.import_module("src.states.new-jersey")

SLICE = {"sections": ["52:18A-224", "52:18A-227", "52:18A-229"]}


def statutes_txt() -> str:
    return (FX / "statutes-52-18a-220-229.txt").read_bytes().decode("latin-1")


def bundle(slice_=SLICE) -> bytes:
    return nj.statute_bundle(statutes_txt(), slice_, "https://pub.njleg.gov/statutes/STATUTES-TEXT.zip", "Wed, 11 Nov 2026")


def test_the_bundle_keeps_only_the_named_sections_and_where_they_sit():
    doc = json.loads(bundle())
    assert [s["number"] for s in doc["sections"]] == ["52:18A-224", "52:18A-227", "52:18A-229"]
    assert doc["updated_through"] == "P.L.2026, c.50, and J.R.1"
    assert doc["title_line"].startswith("TITLE 52") and "STATE GOVERNMENT" in doc["title_line"]


def test_a_section_the_file_does_not_hold_is_refused():
    with pytest.raises(ValueError, match="52:18A-228"):
        bundle({"sections": ["52:18A-224", "52:18A-228"]})


def test_the_text_is_the_banner_title_line_then_each_section_one_line_per_paragraph():
    text = nj.to_text(bundle(), "json", "statute", SLICE, "pub.njleg.gov")
    lines = text.splitlines()
    assert lines[:2] == ["NEW JERSEY GENERAL AND PERMANENT STATUTES", "(UPDATED THROUGH P.L.2026, c.50, and J.R.1)"]
    assert lines[2].startswith("TITLE 52") and lines[3] == "" and lines[4] == "52:18A-224. Short title."
    assert '6. Sections 6 through 16 of P.L.2007, c.56 (C.52:18A-224 through C.52:18A-234) shall be known and may be cited as "The Office of Information Technology Reorganization Act."' in lines
    assert "L.2007,c.56,s.6." in lines
    assert "c. The office shall be directed by the Chief Technology Officer, who shall report directly to the Governor." in text.replace("\t", " ")
    assert "52:18A-225" not in text and "Mission of the division" not in text
    assert "\t" not in text and "\r" not in text


def test_the_printed_update_line_is_the_source_version():
    text = nj.to_text(bundle(), "json", "statute", SLICE, "pub.njleg.gov")
    assert nj.source_version(text, "statute", "json") == "Updated through P.L.2026, c.50, and J.R.1"


def test_identity_wants_every_named_section_in_the_text():
    text = nj.to_text(bundle(), "json", "statute", SLICE, "")
    src = {"id": "x", "doc_type": "statute", "jurisdiction": "new-jersey", "sections": SLICE["sections"],
           "citation": "N.J.S.A. 52:18A-224"}
    assert nj.check_identity(src, text, "page") is True
    short = text.replace("52:18A-229. Administration", "52:18A-2xx. Administration")
    with pytest.raises(ValueError, match="52:18A-229"):
        nj.check_identity(src, short, "page")


def test_infobank_order_page_loses_its_furniture_and_numbers_its_list():
    text = nj.to_text((FX / "eo-corzine-42.htm").read_bytes(), "html", "executive_order", None, "www.nj.gov")
    lines = text.splitlines()
    assert lines[0] == "Executive Order #42"
    assert "Governor Jon S. Corzine" in lines[1]
    assert any(l.startswith("WHEREAS, Executive Order No. 87 (1998) established the Office of Information Technology (OIT)") for l in lines)
    assert any(l.startswith("1. ") for l in lines) and any(l.startswith("15. This Order shall take effect immediately") for l in lines)
    assert "Return to EO Index" not in text and "Incapsula" not in text and "<" not in text
    assert "/s/ Jon S. Corzine" in text


def test_order_identity_reads_the_printed_number():
    src = {"id": "e", "doc_type": "executive_order", "jurisdiction": "new-jersey", "citation": "Executive Order No. 404 (Murphy)"}
    assert nj.check_identity(src, "EXECUTIVE ORDER NO. 404\n WHEREAS", "PDF") is True
    assert nj.check_identity({**src, "citation": "Executive Order No. 42 (Corzine)"}, "Executive Order #42\nGovernor", "page") is True
    with pytest.raises(ValueError, match="Executive Order No. 405"):
        nj.check_identity({**src, "citation": "Executive Order No. 405 (Murphy)"}, "EXECUTIVE ORDER NO. 404\n", "PDF")


def test_order_identity_is_the_orders_own_heading_not_a_recital():
    root = Path(__file__).resolve().parents[2]
    e404 = (root / "_meta/snapshots/nj-eo-murphy-404.txt").read_text()
    p1703 = next((root / "_meta/snapshots").glob("nj-njoit-17-03.txt"), None)
    texts = [e404] + ([p1703.read_text()] if p1703 else [])
    for cite in ("Executive Order No. 44 (Murphy)", "Executive Order No. 178 (Christie)"):
        src = {"id": "e", "doc_type": "executive_order", "jurisdiction": "new-jersey", "citation": cite}
        for t in texts:
            with pytest.raises(ValueError):
                nj.check_identity(src, t, "PDF")
    src = {"id": "e", "doc_type": "executive_order", "jurisdiction": "new-jersey", "citation": "Executive Order No. 404 (Murphy)"}
    assert nj.check_identity(src, e404, "PDF") is True
    assert nj.check_identity(src, "\n  \n EXECUTIVE ORDER NO. 404\n", "PDF") is True


def test_a_policy_is_left_to_the_shared_identity_check():
    src = {"id": "p", "doc_type": "policy", "jurisdiction": "new-jersey", "citation": "x", "title": "x"}
    assert nj.check_identity(src, "text", "PDF") is False


SIGNED = {
    "GIVEN, under my hand and seal this\n 1st day of November,\n Two Thousand and Eighteen,\n and of the Independence": "2018-11-01",
    "GIVEN, under my hand and seal this 20th day\n of November, Two Thousand and Six, and of": "2006-11-20",
    "GIVEN, under my hand and seal this\n 10th day of October,\n Two    Thousand  and   Twenty-\n Three,      and     of": "2023-10-10",
    "GIVEN, under my hand and seal this\n 1st day of June,\n Two Thousand and Seventeen,\n and of the": "2017-06-01",
}


@pytest.mark.parametrize("printed,iso", SIGNED.items())
def test_an_order_takes_effect_on_the_day_it_prints_as_signed(printed, iso):
    text = "WHEREAS, x; and\n15. This Order shall take effect immediately.\n" + printed
    assert nj.effective_date(text, "executive_order") == iso


def test_only_orders_get_a_date_from_their_signing_line():
    assert nj.effective_date("GIVEN, under my hand and seal this 1st day of June, Two Thousand and Seventeen", "policy") is nj.UNHANDLED
    assert nj.effective_date("no signing line here", "executive_order") is nj.UNHANDLED

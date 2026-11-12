"""South Dakota: the Legislature's per-section statute pages (sdlegislature.gov/api/Statutes/<section>.html) bundled
into one document, and the identity of scanned executive orders. Fixtures are the bytes the Legislature served on
2026-11-12 (page head, style block and all)."""
import importlib
import json
from pathlib import Path

import pytest

FX = Path(__file__).parent.parent / "fixtures" / "south-dakota"
sd = importlib.import_module("src.states.south-dakota")

CHAPTER = "https://sdlegislature.gov/api/Statutes/1-33.html"


def page(name: str) -> bytes:
    return (FX / name).read_bytes()


class FakeFetcher:
    """Serves the fixture for a section URL and records the order of requests."""
    def __init__(self, pages):
        self.pages, self.asked = pages, []

    def get(self, url):
        self.asked.append(url)
        if url not in self.pages:
            raise AssertionError(f"unexpected request {url}")
        return type("Resp", (), {"body": self.pages[url]})()


def fetcher():
    base = "https://sdlegislature.gov/api/Statutes/"
    return FakeFetcher({base + "1-33-37.html": page("1-33-37.html"), base + "1-33-42.html": page("1-33-42.html"),
                        base + "1-33-43.html": page("1-33-43.html"), base + "1-33-36.html": page("1-33-36-repealed.html")})


def src(sections, **kw):
    return {"id": "sd-sdcl-test", "doc_type": "statute", "jurisdiction": "south-dakota", "format": "json",
            "url": CHAPTER + "#1-33-37", "citation": "SDCL 1-33-37, 1-33-42, 1-33-43", "title": "t",
            "sections": sections, **kw}


def test_the_snapshot_fetches_each_named_section_once_in_order_and_keeps_its_raw_page(tmp_path):
    f = fetcher()
    raw, fresh = sd.snapshot(src(["1-33-37", "1-33-43"]), f, tmp_path / "x.json", False)
    assert fresh and (tmp_path / "x.json").read_bytes() == raw
    assert f.asked == ["https://sdlegislature.gov/api/Statutes/1-33-37.html", "https://sdlegislature.gov/api/Statutes/1-33-43.html"]
    doc = json.loads(raw)
    assert [s["number"] for s in doc["sections"]] == ["1-33-37", "1-33-43"]
    assert "Functions of Bureau of Information and Technology" in doc["sections"][1]["page"]


def test_a_cached_snapshot_is_not_fetched_again(tmp_path):
    f = fetcher()
    sd.snapshot(src(["1-33-37"]), f, tmp_path / "x.json", False)
    f.asked.clear()
    raw, fresh = sd.snapshot(src(["1-33-37"]), f, tmp_path / "x.json", False)
    assert not fresh and f.asked == []


def test_a_repealed_section_is_refused_never_bundled(tmp_path):
    with pytest.raises(ValueError, match="1-33-36.*[Rr]epealed"):
        sd.snapshot(src(["1-33-36"]), fetcher(), tmp_path / "x.json", False)
    assert not (tmp_path / "x.json").exists()


def test_the_text_is_each_section_heading_paragraphs_and_history_with_a_blank_line_between():
    bundle = sd.statute_bundle({"1-33-37": page("1-33-37.html"), "1-33-43": page("1-33-43.html")}, ["1-33-37", "1-33-43"])
    text = sd.to_text(bundle, "json", "statute", None, "sdlegislature.gov")
    lines = text.splitlines()
    assert lines[0] == "1-33-37. Bureau of Information and Technology created."
    assert lines[1].startswith("There is hereby created within the Department of Executive Management")
    assert lines[2].startswith("Source: SL 1994, ch 412 (Ex. Ord. 94-4), § 17;") and lines[3] == ""
    assert lines[4] == "1-33-43. Functions of Bureau of Information and Technology."
    assert "(2) Developing and proposing operational technical standards for the state information systems" in text
    assert "<" not in text and "font-family" not in text and "SDLRC" not in text


def test_identity_needs_every_section_in_order_and_the_first_section_to_open_the_text():
    bundle = sd.statute_bundle({"1-33-37": page("1-33-37.html"), "1-33-43": page("1-33-43.html")}, ["1-33-37", "1-33-43"])
    text = sd.to_text(bundle, "json", "statute", None, "")
    assert sd.check_identity(src(["1-33-37", "1-33-43"]), text, "page") is True
    with pytest.raises(ValueError, match="1-33-42"):
        sd.check_identity(src(["1-33-37", "1-33-42", "1-33-43"]), text, "page")


def eo(number):
    return {"id": f"sd-eo-{number}", "doc_type": "executive_order", "jurisdiction": "south-dakota", "format": "pdf",
            "citation": f"Executive Order {number}", "title": "t"}


def test_an_executive_order_is_identified_by_its_own_heading_not_by_a_mention():
    # EO 2023-06 recites EO 2022-10 in its first paragraph; the heading is what identifies it
    text_2306 = ("STATE OF SOUTH DAKOTA\nOFFICE OF THE GOVERNOR\nEXECUTIVE ORDER 2023-06\n\n"
                 "Whereas, Executive Order 2022-10 acknowledged the cybersecurity risks TikTok\n")
    assert sd.check_identity(eo("2023-06"), text_2306, "PDF") is True
    with pytest.raises(ValueError, match="2022-10"):
        sd.check_identity(eo("2022-10"), text_2306, "PDF")


def test_a_reorganization_order_whose_heading_reads_executive_order_is_identified_too():
    text = "STATE OF SOUTH DAKOTA\nOFFICE OF THE GOVERNOR\nEXECUTIVE ORDER 2026-02\n\nWhereas, Article IV, Section 8"
    assert sd.check_identity(eo("2026-02"), text, "PDF") is True


def test_other_states_and_types_are_left_to_the_shared_checks():
    assert sd.check_identity({**eo("2023-06"), "jurisdiction": "oregon"}, "", "PDF") is False
    assert sd.check_identity({**eo("2023-06"), "doc_type": "policy"}, "", "PDF") is False


def test_the_real_ocr_readings_with_their_scan_noise_are_identified_by_heading():
    # the first lines of the OCR text of the two scans, copied from _meta/snapshots (stray marks around the heading)
    r2210 = (FX / "eo-2022-10-ocr-head.txt").read_text()
    r2306 = (FX / "eo-2023-06-ocr-head.txt").read_text()
    assert "b EXECUTIVE ORDER 2023-06 }" in r2306
    assert sd.check_identity(eo("2022-10"), r2210, "PDF") is True
    assert sd.check_identity(eo("2023-06"), r2306, "PDF") is True
    with pytest.raises(ValueError, match="2022-10"):
        sd.check_identity(eo("2022-10"), r2306, "PDF")


def test_a_statute_entry_that_is_not_a_json_section_bundle_is_not_the_bundlers_business(tmp_path):
    f = fetcher()
    assert sd.snapshot({**src(["1-33-37"]), "format": "pdf"}, f, tmp_path / "x.pdf", False) is None
    assert sd.snapshot({"id": "x", "doc_type": "statute", "format": "html"}, f, tmp_path / "x.html", False) is None
    assert f.asked == []


def test_a_json_statute_entry_without_sections_is_a_value_error_not_a_key_error(tmp_path):
    bad = {k: v for k, v in src(["1-33-37"]).items() if k != "sections"}
    with pytest.raises(ValueError, match="sections"):
        sd.snapshot(bad, fetcher(), tmp_path / "x.json", False)

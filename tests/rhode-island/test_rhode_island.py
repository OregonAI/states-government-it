"""Rhode Island: the Legislature's General Laws (one page per section, a chapter bundled from its index page and its
section pages), the Governor's executive order PDF, and the dates the ETSS policies print. Fixtures are real bytes, page
furniture included: chapter 11-49.3's index and seven section pages, one section of chapter 42-11, the order's PDF and
one ETSS policy PDF."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from src import states
from src.ingest_common import pdf_to_text
from src.states import UNHANDLED
ri = states.modules(refresh=True).get("rhode-island")

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "rhode-island"
CH = "https://webserver.rilegislature.gov/Statutes/TITLE11/11-49.3/INDEX.htm"
SEC = "https://webserver.rilegislature.gov/Statutes/TITLE11/11-49.3/11-49.3-{}.htm"
PAGES = {CH: (FIX / "11-49.3-chapter.html").read_bytes()}
for n in range(1, 8):
    PAGES[SEC.format(n)] = (FIX / f"11-49.3-section-{n}.html").read_bytes()
SECTION = (FIX / "42-11-2.6-section.html").read_bytes()
SRC_CH = {"id": "ri-gl-11-49-3", "jurisdiction": "rhode-island", "doc_type": "statute", "url": CH,
          "citation": "R.I. Gen. Laws ch. 11-49.3", "title": "Identity Theft Protection Act of 2015"}
SRC_SEC = {"id": "ri-gl-42-11-2-6", "jurisdiction": "rhode-island", "doc_type": "statute",
           "url": "https://webserver.rilegislature.gov/Statutes/TITLE42/42-11/42-11-2.6.htm",
           "citation": "R.I. Gen. Laws § 42-11-2.6", "title": "Office of Digital Excellence established"}
EO_SRC = {"id": "ri-eo-24-06", "jurisdiction": "rhode-island", "doc_type": "executive_order",
          "citation": "Executive Order 24-06", "title": "Artificial Intelligence and Data Centers of Excellence"}


class FakeFetcher:
    def __init__(self, pages):
        self.pages, self.asked = pages, []

    def get(self, url):
        self.asked.append(url)
        return SimpleNamespace(body=self.pages[url], status=200)


def bundle(tmp_path):
    return ri.snapshot(SRC_CH, FakeFetcher(PAGES), tmp_path / "x.html", False)


def test_the_state_is_found_by_name():
    assert ri is not None


def test_a_chapter_is_bundled_from_its_index_and_every_section_page_in_order(tmp_path):
    f = FakeFetcher(PAGES)
    raw, fresh = ri.snapshot(SRC_CH, f, tmp_path / "x.html", False)
    assert fresh and (tmp_path / "x.html").read_bytes() == raw
    assert f.asked == [CH] + [SEC.format(n) for n in range(1, 8)]


def test_a_committed_bundle_is_reused_unless_refetch(tmp_path):
    raw, _ = bundle(tmp_path)
    f = FakeFetcher({})
    again, fresh = ri.snapshot(SRC_CH, f, tmp_path / "x.html", False)
    assert again == raw and not fresh and f.asked == []


def test_a_single_section_and_other_types_are_one_plain_fetch(tmp_path):
    assert ri.snapshot(SRC_SEC, FakeFetcher({}), tmp_path / "y.html", False) is None
    assert ri.snapshot(EO_SRC, FakeFetcher({}), tmp_path / "y.pdf", False) is None


def test_a_chapter_whose_index_links_no_sections_is_refused(tmp_path):
    with pytest.raises(ValueError, match="links no sections"):
        ri.snapshot(SRC_CH, FakeFetcher({CH: b"<html><body><h2>Chapter 1</h2></body></html>"}), tmp_path / "x.html", False)


def test_chapter_text_is_the_heading_then_each_section_without_the_index_links(tmp_path):
    raw, _ = bundle(tmp_path)
    text = ri.to_text(raw, "html", "statute", None, "")
    assert text.startswith("Chapter 49.3 Identity Theft Protection Act of 2015\n")
    assert "\n§ 11-49.3-7. Notification of cybersecurity incident.\n" in text
    assert ("(a) Any municipal agency or state agency that detects a cybersecurity incident shall provide notification "
            "to the Rhode Island state police upon detection of the cybersecurity incident within twenty-four (24) hours."
            ) in " ".join(text.split())
    assert "Index of Sections" not in text and "<" not in text and "&nbsp;" not in text and "\xa0" not in text
    assert text.count("History of Section.") == 7


def test_a_section_page_keeps_its_title_chapter_and_citation_lines():
    text = ri.to_text(SECTION, "html", "statute", None, "")
    assert text.split("\n")[:4] == ["Title 42 State Affairs and Government", "Chapter 11 Department of Administration",
                                    "R.I. Gen. Laws § 42-11-2.6",
                                    "§ 42-11-2.6. Office of Digital Excellence established."]
    assert "chief digital officer" in text and text.endswith("\n")


def test_other_formats_are_not_claimed():
    assert ri.to_text(b"x", "json", "policy", None, "") is None


def test_identity_accepts_the_cited_chapter_and_section_and_refuses_the_wrong_page(tmp_path):
    raw, _ = bundle(tmp_path)
    chapter = ri.to_text(raw, "html", "statute", None, "")
    section = ri.to_text(SECTION, "html", "statute", None, "")
    assert ri.check_identity(SRC_CH, chapter, "page") is True
    assert ri.check_identity(SRC_SEC, section, "page") is True
    with pytest.raises(ValueError, match="not R.I. Gen. Laws § 42-11-2.6"):
        ri.check_identity(SRC_SEC, chapter, "page")
    with pytest.raises(ValueError, match="not R.I. Gen. Laws ch. 11-49.3"):
        ri.check_identity(SRC_CH, section, "page")


def test_identity_for_an_order_is_its_own_heading_not_a_mention_of_its_number():
    text = pdf_to_text((FIX / "eo-24-06.pdf").read_bytes(), ())
    assert ri.check_identity(EO_SRC, text, "PDF") is True
    other = dict(EO_SRC, citation="Executive Order 24-05")
    with pytest.raises(ValueError, match="24-05"):
        ri.check_identity(other, text, "PDF")
    mention = "State of Rhode Island\nEXECUTIVE ORDER\n23-01\nJanuary 1, 2023\nThis order amends Executive Order 24-06.\n"
    with pytest.raises(ValueError, match="24-06"):
        ri.check_identity(EO_SRC, mention, "PDF")


def test_other_types_are_left_to_the_shared_identity_check():
    assert ri.check_identity({"jurisdiction": "rhode-island", "doc_type": "policy", "citation": "x", "title": "y"}, "t", "PDF") is False


def test_an_etss_policy_prints_its_effective_date_day_first_and_its_last_review():
    text = pdf_to_text((FIX / "etss-300.1.pdf").read_bytes(), ())
    assert ri.effective_date(text, "policy") == "2026-06-23"
    assert ri.source_version(text, "policy", "pdf") == "Last Review: 22 June 2026"


def test_dates_the_shared_reader_handles_are_left_to_it_and_an_absent_date_is_empty():
    assert ri.effective_date("Publish Date: 7/29/2026\nEffective Date: 7/29/2026\n", "policy") is UNHANDLED
    assert ri.effective_date("Date of Last Revision 10/01/18\n", "policy") is UNHANDLED
    assert ri.source_version("Last Revision Date: 07/29/2026\n", "policy", "pdf") == "Last Revision Date: 07/29/2026"
    assert ri.source_version("Last Revision: 4/21/2025\n", "policy", "pdf") == "Last Revision: 4/21/2025"
    assert ri.source_version("Date of Last Revision 04/01/2016\n", "policy", "pdf") == "Date of Last Revision 04/01/2016"
    assert ri.source_version("  Publish Date: 23 June 2026\n  Last Review: 22 June 2026       doa.entsec@doit.ri.gov\n",
                             "policy", "pdf") == "Last Review: 22 June 2026"
    assert ri.source_version("nothing printed\n", "policy", "pdf") is None


def test_the_notes_describe_how_a_statute_page_was_read():
    note = ri.notes({"jurisdiction": "rhode-island", "doc_type": "statute"}, "html", "x")
    assert "webserver.rilegislature.gov" in note
    assert ri.notes({"jurisdiction": "rhode-island", "doc_type": "policy"}, "pdf", "x") is None

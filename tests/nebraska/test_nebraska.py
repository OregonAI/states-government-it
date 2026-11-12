"""Nebraska: the Legislature's whole-chapter pages (display-chapters.php). The fixture is real bytes: the page head
(style sheet and body wrapper) and the page tail, with sections 86-510 to 86-512, 86-572 and 86-573, 86-5,100 and
86-5,101 kept, so a slice has neighbours to be cut from."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states
from src.states import nebraska

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "nebraska"
CH86 = (FIX / "ch86-cut.html").read_bytes()
GIS = {"article": "86-572", "part": "86-573"}
SRC = {"id": "ne-ris-86-572-573", "jurisdiction": "nebraska", "doc_type": "statute", "slice": GIS,
       "citation": "Neb. Rev. Stat. sections 86-572 to 86-573", "title": "Geographic Information Systems Council: duties and report"}


def test_the_state_is_found_by_name():
    assert "nebraska" in states.modules(refresh=True)


def test_a_slice_runs_from_its_first_section_to_its_last_and_no_further():
    text = nebraska.statute_html_to_text(CH86, GIS)
    lines = text.splitlines()
    assert lines[0] == "86-572. Council; duties."
    assert lines[1] == "The Geographic Information Systems Council shall:"
    assert ("(1) Make recommendations to the Legislature and the Nebraska Information Technology Commission for "
            "program initiatives and funding. The recommendations submitted to the Legislature shall be submitted "
            "electronically;") in lines
    assert "86-573. Council; report." in lines
    assert text.rstrip().endswith("pursuant to section 86-518.\nSource: Laws 1991, LB 639, § 5; Laws 1998, LB 924, § 50; "
                                  "R.S.1943, (1999), § 81-2605; Laws 2002, LB 1105, § 343; Laws 2008, LB823, § 21.")
    assert "86-512" not in text and "86-5,100" not in text and "Network Nebraska" not in text


def test_the_source_line_and_the_operative_date_are_kept_and_sections_are_set_off():
    lines = nebraska.statute_html_to_text(CH86, GIS).splitlines()
    source = next(l for l in lines if l.startswith("Source: Laws 1991, LB 639, § 4;"))
    assert source.endswith("Laws 2026, LB905, § 65.")
    assert lines[lines.index(source) + 1] == "Operative Date: July 1, 2026"
    assert lines[lines.index("86-573. Council; report.") - 1] == ""


def test_a_repealed_section_stays_as_the_page_prints_it():
    text = nebraska.statute_html_to_text(CH86, {"article": "86-510", "part": "86-512"})
    assert "\n\n86-511. Repealed. Laws 2026, LB905, § 69.\nOperative Date: July 1, 2026\n\n86-512. Legislative intent.\n" in text


def test_a_section_number_with_a_comma_is_found_and_a_one_section_slice_works():
    text = nebraska.statute_html_to_text(CH86, {"article": "86-5,100", "part": "86-5,100"})
    assert text.startswith("86-5,100. Network Nebraska; development and maintenance; access; Chief Information Officer; "
                           "duties; cost; report.\nThe Chief Information Officer, in partnership with the University of Nebraska")
    assert "86-5,101" not in text
    assert text.rstrip().endswith("Laws 2012, LB782, § 248.")


def test_no_markup_or_css_leaks():
    text = nebraska.statute_html_to_text(CH86, GIS)
    for leak in ("<", ">", "font-family", "/laws/statutes.php", "&nbsp;", "&#167;", "\t", "printwidth"):
        assert leak not in text


def test_a_slice_the_page_does_not_hold_is_refused():
    with pytest.raises(ValueError, match="86-999"):
        nebraska.statute_html_to_text(CH86, {"article": "86-572", "part": "86-999"})
    with pytest.raises(ValueError, match="needs a slice"):
        nebraska.statute_html_to_text(CH86, None)


def test_a_page_with_no_statute_body_is_refused_not_committed():
    with pytest.raises(ValueError, match="no statute text"):
        nebraska.statute_html_to_text(b"<html><body><h1>Not Found</h1></body></html>", GIS)


def test_the_shared_flow_reaches_this_reader_and_checks_identity():
    fmt, text = ing.derive({**SRC, "format": "html"}, CH86)
    assert fmt == "html" and text.startswith("86-572. Council; duties.\n")
    with pytest.raises(ValueError, match="no to_text"):
        ing.to_text(CH86, "html", "rule", "nebraska")
    with pytest.raises(ValueError, match="not the cited"):
        # the entry cites 86-510 to 86-512 but its slice is cut elsewhere: the text does not open with 86-510
        states.check_identity({**SRC, "citation": "Neb. Rev. Stat. sections 86-510 to 86-512"}, text)


EO_TEXT = (FIX / "eo-25-04.txt").read_text()   # pdftotext -layout of the Governor's PDF, signature-block noise included
EO = {"id": "ne-eo-25-04", "jurisdiction": "nebraska", "doc_type": "executive_order", "citation": "Executive Order No. 25-04",
      "title": "Banning the Use or Download of Applications, Software, and Platforms Created or Owned by China-based Companies"}


def test_an_executive_order_is_the_cited_one_when_its_own_heading_line_says_so():
    states.check_identity(EO, EO_TEXT)       # no error


def test_a_mention_of_the_number_elsewhere_is_not_the_heading():
    other = EO_TEXT.replace("EXECUTIVE ORDER NO. 25-04", "EXECUTIVE ORDER NO. 25-05") + "\nSee Executive Order No. 25-04.\n"
    with pytest.raises(ValueError, match="not the cited"):
        states.check_identity(EO, other)


def test_the_number_must_match_exactly_not_as_a_prefix():
    with pytest.raises(ValueError, match="not the cited"):
        states.check_identity({**EO, "citation": "Executive Order No. 25-0"}, EO_TEXT)


# ---- dates ----------------------------------------------------------------------



def test_an_executive_order_is_dated_by_its_signing_day():
    assert nebraska.effective_date(EO_TEXT, "executive_order") == "2025-03-05"
    assert states.effective_date(EO_TEXT, "executive_order", "nebraska") == "2025-03-05"


def test_a_text_without_a_signing_day_is_left_to_the_shared_reader():
    assert nebraska.effective_date("Executive Order\nnothing signed here", "executive_order") is states.UNHANDLED
    assert nebraska.effective_date("History: Adopted on July 12, 2017.", "policy") is states.UNHANDLED


def test_a_nitc_section_version_is_the_latest_date_of_its_history_line():
    one = "body\n\n     History: Adopted on July 12, 2017. Amended on July 14, 2023.\n     URL: https://x\n"
    assert nebraska.source_version(one, "policy", "pdf") == "History through July 14, 2023"
    adopted = "History: Adopted on November 8, 2018.\nURL: https://x"
    assert nebraska.source_version(adopted, "standard", "pdf") == "History through November 8, 2018"


def test_a_history_line_that_wraps_and_renumbers_is_read_whole():
    wrapped = ("     History: Adopted on September 30, 2013. Renumbered on July 12, 2018 (previously was § 7-301). "
               "Amended on August 4, 2006; April 11,\n     2012; and July 12, 2018.\n     URL: https://x\n")
    assert nebraska.source_version(wrapped, "standard", "pdf") == "History through July 12, 2018"


def test_no_history_line_no_version():
    assert nebraska.source_version("no history here", "policy", "pdf") is None
    assert nebraska.source_version("History: Adopted on July 12, 2017.", "statute", "html") is None

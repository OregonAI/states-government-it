"""Kansas 2026 amendments the Revisor's section pages do not yet print: the Secretary of State's session-law pages
(sos.ks.gov/publications/sessionlaws/2026/Chapter-NN-BB-NNNN.html). Fixtures are the whole real pages, furniture included:
Chapter 53 (House Bill 2574) and Chapter 153 (House Substitute for Senate Bill 51)."""
from pathlib import Path

import pytest

from src.states import kansas

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "kansas"
HB2574 = (FIX / "Chapter-53-HB-2574.html").read_bytes()
SB51 = (FIX / "Chapter-153-SB-51.html").read_bytes()


def lines(raw, **slice_):
    return kansas.to_text(raw, "html", "statute", slice_, "www.sos.ks.gov").splitlines()


def test_an_amended_section_keeps_new_text_and_drops_struck_text():
    out = lines(HB2574, article="17")
    assert out[0].startswith("75-7246. (a) On October 1, 2028, and each year thereafter, the executive CISO shall report to the legislative budget committee and the joint committee on information technology")
    text = "\n".join(out)
    assert "director of the budget" not in text.split("\n", 1)[0]
    assert "certify an amount equal to 5%" not in text
    assert "On July October" not in text


def test_the_section_stops_at_the_next_section_and_names_its_session_law():
    out = lines(HB2574, article="4")
    assert out[0].startswith("75-413. (a) The secretary of state")
    assert not any(l.startswith("75-623.") for l in out)
    assert out[-1] == ("[2026 Session Laws of Kansas, chapter 53, House Bill No. 2574, section 4. Approved April 6, 2026.]")


def test_a_fully_struck_paragraph_leaves_no_line():
    for l in lines(HB2574, article="17"):
        assert l.strip()
        assert "<" not in l and "&" not in l


def test_a_house_substitute_page_and_a_one_paragraph_amendment():
    out = lines(SB51, article="3")
    assert out[0].startswith("75-4704. Under the supervision of the executive chief information technology officer")
    assert "cloud services for other executive branch divisions" in out[0]
    assert out[-1].startswith("[2026 Session Laws of Kansas, chapter 153, House Substitute for Senate Bill No. 51, section 3.")


def test_a_new_section_takes_its_number_from_the_seed_entry():
    out = lines(SB51, article="New Section 1", part="75-7247")
    assert out[0].startswith("75-7247. (a) The executive chief information technology officer may enter into an agreement with an entity")
    assert any(l.startswith("(b) As used in this section") for l in out)
    assert not any("46-1135" in l for l in out)


def test_identity_refuses_a_section_that_is_not_the_cited_statute():
    src = {"id": "x", "jurisdiction": "kansas", "doc_type": "statute", "citation": "K.S.A. 75-4705"}
    text = kansas.to_text(SB51, "html", "statute", {"article": "3"}, "www.sos.ks.gov")
    with pytest.raises(ValueError, match="is not K.S.A. 75-4705"):
        kansas.check_identity(src, text, "page")
    assert kansas.check_identity({**src, "citation": "K.S.A. 75-4704"}, text, "page") is True


def test_a_section_that_is_not_on_the_page_is_refused():
    with pytest.raises(ValueError, match="section 99"):
        kansas.to_text(SB51, "html", "statute", {"article": "99"}, "www.sos.ks.gov")


def test_the_notes_say_where_the_text_came_from_and_why():
    src = {"id": "ks-ksa-75-4704", "jurisdiction": "kansas", "doc_type": "statute", "citation": "K.S.A. 75-4704",
           "slice": {"article": "3"}}
    text = kansas.to_text(SB51, "html", "statute", {"article": "3"}, "www.sos.ks.gov")
    n = kansas.notes(src, "html", text)
    assert "Secretary of State" in n and "2026 Composite" in n and "struck" in n
    assert "Revisor's static section page" not in n


def test_a_curator_note_in_the_seed_entry_is_appended():
    src = {"id": "ks-ksa-75-7201", "jurisdiction": "kansas", "doc_type": "statute", "citation": "K.S.A. 75-7201",
           "curator_note": "The CAUTION line points to a repealed version."}
    n = kansas.notes(src, "html", "75-7201. x\n")
    assert n.endswith("The CAUTION line points to a repealed version.")


def test_a_new_section_note_says_the_number_is_the_composite_listings():
    src = {"id": "ks-ksa-75-7247", "jurisdiction": "kansas", "doc_type": "statute", "citation": "K.S.A. 75-7247",
           "slice": {"article": "New Section 1", "part": "75-7247"}}
    text = kansas.to_text(SB51, "html", "statute", src["slice"], "www.sos.ks.gov")
    assert text.splitlines()[-1].startswith("[2026 Session Laws of Kansas, chapter 153, House Substitute for Senate Bill No. 51, new section 1.")
    n = kansas.notes(src, "html", text)
    assert "number is the Composite Listing's" in n and "hereby amended" not in n

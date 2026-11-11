"""Seam: src.ingest for Colorado statutes: one slice (article or part) of the OLLS title file."""
from pathlib import Path

import pytest
from corpus_toolkit.repo import parse_frontmatter

from seedutil import make_corpus, make_fetcher
from src import ingest as ing

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "colorado"

# ---- Colorado statutes: one slice (article or part) of the OLLS title file ---------------
# The official source is one Word-HTML file per title (Title 24 is 22 MB). A seed entry names
# its slice with `slice: {article: "73"}` or `{article: "33.5", part: "19"}`. The fixtures are
# real bytes from crs2026-title-24.htm: the whole bodies of articles 73 to 74.1, and article
# 33.5's heading, the part 19/20 caption list and the part 19 body.

CRS_73 = (FIX / "crs-title-24-articles-73-74.html").read_bytes()
CRS_P19 = (FIX / "crs-title-24-article-33-5-part-19.html").read_bytes()
CO_73 = {"id": "co-crs-24-73", "doc_type": "statute", "jurisdiction": "colorado",
         "citation": "C.R.S. title 24, article 73",
         "title": "Security Breaches and Personal Information", "slice": {"article": "73"}}
CO_P19 = {"id": "co-crs-24-33-5-pt19", "doc_type": "statute", "jurisdiction": "colorado",
          "citation": "C.R.S. title 24, article 33.5, part 19", "title": "Colorado Cybersecurity",
          "slice": {"article": "33.5", "part": "19"}}


def crs(raw, slice_):
    return ing.to_text(raw, "html", "statute", "colorado", slice_)


def test_crs_article_slice_runs_from_its_heading_to_the_next_articles_heading():
    t = crs(CRS_73, {"article": "73"})
    lines = t.splitlines()
    assert lines[0] == "ARTICLE 73" and lines[1] == "Security Breaches and Personal Information"
    assert any(l.startswith("24-73-103. Governmental entity - notification of security breach.")
               for l in lines)
    assert "ARTICLE 74" not in lines and not any(l.startswith("24-74-10") for l in lines)


def test_crs_article_slice_keeps_source_notes_and_history_lines():
    t = crs(CRS_73, {"article": "73"})
    assert "Source: L. 2018: Entire article added, (HB 18-1128), ch. 266, p. 1639, § 4, " \
           "effective September 1." in t
    assert "<" not in t and "\xa0" not in t and "font-family" not in t and "\n\n" not in t


def test_crs_last_article_in_the_file_runs_to_the_end():
    t = crs(CRS_73, {"article": "74.1"})
    assert t.splitlines()[0] == "ARTICLE 74.1" and "24-74.1-103" in t


CRS_85 = (FIX / "crs-title-24-articles-85-90.html").read_bytes()   # contents list + arts 85, 90


def test_crs_article_slice_stops_before_the_title_level_group_heading_of_the_next_article():
    # Real bytes: the file prints the group heading LIBRARIES between article 85 and ARTICLE 90.
    # It is not text of article 85 (nor of 90): the slice must end at article 85's last line.
    lines = crs(CRS_85, {"article": "85"}).splitlines()
    assert lines[0] == "ARTICLE 85" and lines[-1].startswith("Source: L. 2000: Entire article added")
    assert "LIBRARIES" not in lines and "ARTICLE 90" not in lines
    # the group heading that sits before ARTICLE 85 is not its text either
    assert "INFORMATION TECHNOLOGY ACCESS FOR BLIND" not in lines
    # a heading word inside ordinary text is left alone
    assert any("libraries" in l.lower() for l in crs(CRS_85, {"article": "90"}).splitlines()[:3])


def test_crs_part_slice_is_the_body_of_that_part_only():
    t = crs(CRS_P19, {"article": "33.5", "part": "19"})
    lines = t.splitlines()
    assert lines[0] == "PART 19" and lines[1] == "COLORADO CYBERSECURITY"
    assert any(l.startswith("24-33.5-1902. Colorado cybersecurity council") for l in lines)
    assert "PART 20" not in lines and not any(l.startswith("24-33.5-2001") for l in lines)
    assert not any(l.startswith("PART 19 ") for l in lines)      # not the caption list


def test_crs_slice_that_is_missing_or_ambiguous_is_refused_not_guessed():
    with pytest.raises(ValueError, match="article 99"):
        crs(CRS_73, {"article": "99"})
    with pytest.raises(ValueError, match="part 3"):
        crs(CRS_P19, {"article": "33.5", "part": "3"})
    with pytest.raises(ValueError, match="needs a slice"):
        crs(CRS_73, None)
    doubled = CRS_73.replace(b"</body>", b"<p>ARTICLE 73</p></body>")
    with pytest.raises(ValueError, match="more than once"):
        crs(doubled, {"article": "73"})


def test_co_identity_is_the_heading_and_caption_of_the_slice():
    ing.check_identity(CO_73, crs(CRS_73, CO_73["slice"]))
    ing.check_identity(CO_P19, crs(CRS_P19, CO_P19["slice"]))
    with pytest.raises(ValueError, match="not C.R.S. title 24, article 74"):
        ing.check_identity(dict(CO_73, citation="C.R.S. title 24, article 74"),
                           crs(CRS_73, CO_73["slice"]))
    with pytest.raises(ValueError, match="title"):
        ing.check_identity(dict(CO_73, title="Something Else"), crs(CRS_73, CO_73["slice"]))


def test_co_statute_gets_no_effective_date_and_its_own_conversion_notes():
    text = crs(CRS_73, {"article": "73"})
    assert ing.effective_date(text, "statute") is None
    notes = ing.conversion_notes(CO_73, "html", text)
    assert "title file" in notes and "ARTICLE" in notes and "whole chapter" not in notes


def test_co_document_is_written_with_its_slice_as_full_text(tmp_path):
    src = dict(CO_73, url="https://example.gov/crs2026-title-24.htm", format="html",
               issuing_body="Office of Legislative Legal Services", tags=["data"],
               why_relevant="Governmental entity duties for personal identifying information.")
    cfg = make_corpus(tmp_path, [src])
    with make_fetcher(cfg, {src["url"]: (200, CRS_73)}) as f:
        out = ing.ingest(src, f, False, cfg)
    assert out == tmp_path / "statutes" / "colorado" / "co-crs-24-73.md"
    fm, body = parse_frontmatter(out)
    full = body.split("## Full text\n", 1)[1].split("\n## ", 1)[0].strip()
    assert full == crs(CRS_73, {"article": "73"}).strip()
    assert fm["jurisdiction"] == "colorado" and fm["effective_date"] in (None, "")
    assert ing.check([src], cfg) == []

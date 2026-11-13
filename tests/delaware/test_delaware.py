"""Seam: src.ingest / src.states for Delaware: the Delaware Code Online chapter and subchapter pages
(delcode.delaware.gov). Fixtures are the real pages the site served on 2026-11-11, whole, with page furniture.
DTI's policy and standard PDFs and the Public Archives' scanned executive orders use the shared readers."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "delaware"
SC01 = (FIX / "delcode-29-c90c-sc01.html").read_bytes()
SC03 = (FIX / "delcode-29-c90c-sc03.html").read_bytes()
SC04 = (FIX / "delcode-29-c90c-sc04.html").read_bytes()
C12B = (FIX / "delcode-6-c12b.html").read_bytes()
T19C7 = (FIX / "delcode-19-c07-sc01.html").read_bytes()      # Title 19 ch. 7 subch. I, whole page, 2026-11-13
T29C5 = (FIX / "delcode-29-c05-sc01.html").read_bytes()      # Title 29 ch. 5 subch. I, whole page, 2026-11-13


def text(raw):
    return ing.to_text(raw, "html", "statute", "delaware")


def test_text_opens_with_the_title_chapter_and_subchapter_heads_as_printed():
    lines = text(SC03).splitlines()
    assert lines[:5] == ["TITLE 29", "State Government", "Departments of Government",
                         "CHAPTER 90C. Department of Technology and Information",
                         "Subchapter III. Cyber Security"]
    assert lines[5] == ""
    assert lines[6] == "§ 9030C. Delaware Cyber Security Advisory Council"


def test_a_chapter_page_without_a_subchapter_head_keeps_its_own_heads():
    lines = text(C12B).splitlines()
    assert lines[0] == "TITLE 6"
    assert "CHAPTER 12B. Computer Security Breaches" in lines
    assert "§ 12B-100. Protection of personal information." in lines


def test_paragraphs_are_one_line_each_and_indented_by_their_level():
    lines = text(SC03).splitlines()
    assert any(l.startswith("(a) There is hereby established a Delaware Cyber Security Advisory Council") for l in lines)
    assert "  (1) State Chief Information Officer, who shall serve as chair;" in lines
    t4 = text(SC04).splitlines()
    assert "  (1) Twelve members serving by virtue of position, or their designee, as follows:" in t4
    assert "    a. The Chief Information Officer of the Department of Technology and Information." in t4
    assert "    l. The Executive Director of the Government Efficiency and Accountability Review Board." in t4


def test_each_section_ends_with_its_history_line_on_one_line():
    t = text(SC01)
    assert "73 Del. Laws, c. 86, § 1; 74 Del. Laws, c. 128, § 11; 82 Del. Laws, c. 185, § 1;" in t.splitlines()


def test_the_page_prints_the_last_sections_first_history_citation_again_after_it_and_the_repeat_is_dropped():
    t = text(SC03)
    assert t.count("81 Del. Laws, c. 373, § 1;") == 1
    assert t.rstrip().endswith("81 Del. Laws, c. 373, § 1;")


def test_a_repealed_section_keeps_its_heading_and_its_repeal_note():
    t = text(SC01).splitlines()
    assert "§ 9013C. Technology Investment Council [Repealed]." in t
    assert "repealed by 84 Del. Laws, c. 382, § 3, effective Aug. 29, 2024." in "\n".join(t)


def test_page_furniture_menus_and_the_section_index_are_not_read():
    t = text(SC03)
    for furniture in ("Authenticated PDF", "Toggle navigation", "Delaware General Assembly", "Twitter",
                      "Municipal Charters", "Return to The Delaware Code Online"):
        assert furniture not in t
    assert "<" not in t and "&amp;" not in t and "\xa0" not in t
    assert [l for l in t.splitlines() if l.strip() == "§ 9030C"] == []     # the section index at the top of the page
    t1 = text(SC01)
    assert "§ 9001C\n§ 9002C" not in t1


def test_every_section_the_page_lists_is_in_the_text():
    t = text(SC01)
    for n in ("9001C", "9004C", "9011C", "9016E", "9016G"):
        assert f"§ {n}." in t


def test_a_page_with_no_code_body_is_refused():
    with pytest.raises(ValueError, match="no code body"):
        text(b"<html><body><h1>Delaware Code Online</h1></body></html>")


def seed(citation, **kw):
    return {"id": "x", "doc_type": "statute", "jurisdiction": "delaware", "citation": citation, "title": "t", **kw}


def test_statute_identity_checks_title_chapter_and_subchapter():
    states.check_identity(seed("29 Del. C. ch. 90C, subch. III"), text(SC03), "html")
    states.check_identity(seed("29 Del. C. ch. 90C, subch. I"), text(SC01), "html")
    states.check_identity(seed("6 Del. C. ch. 12B"), text(C12B), "html")
    with pytest.raises(ValueError, match="is not 29 Del. C. ch. 90C, subch. IV"):
        states.check_identity(seed("29 Del. C. ch. 90C, subch. IV"), text(SC03), "html")
    with pytest.raises(ValueError, match="is not 29 Del. C. ch. 90D"):
        states.check_identity(seed("29 Del. C. ch. 90D"), text(SC03), "html")
    with pytest.raises(ValueError, match="is not 6 Del. C. ch. 12B"):
        states.check_identity(seed("6 Del. C. ch. 12B"), text(SC04), "html")


def test_a_statute_has_no_effective_date_and_no_version():
    t = text(SC04)
    assert states.effective_date(t, "statute", "delaware") is None
    assert states.source_version(t, "statute", "delaware", "html") == ""


def test_conversion_notes_say_what_was_read_and_what_was_dropped():
    n = states.hook("delaware", "notes")(seed("29 Del. C. ch. 90C, subch. III"), "html", text(SC03))
    assert "delcode.delaware.gov" in n and "second time" in n and "menus" in n


EO = {"id": "de-eo", "doc_type": "executive_order", "jurisdiction": "delaware",
      "citation": "Del. Governor Markell, Exec. Order No. 20", "title": "t",
      "identity_text": "MORE EFFECTIVELY UTILIZING INFORMATION TECHNOLOGY RESOURCES"}


def test_executive_order_identity_matches_the_orders_own_heading_with_the_number_in_words():
    heading = "EXECUTIVE ORDER\nNUMBER TWENTY\n\nTO:    HEADS OF ALL STATE DEPARTMENTS AND AGENCIES\n\nRE:    MORE EFFECTIVELY UTILIZING INFORMATION TECHNOLOGY RESOURCES\n"
    states.check_identity(EO, heading, "pdf")


def test_executive_order_identity_refuses_another_number_or_a_mere_mention():
    other = "EXECUTIVE ORDER\nNUMBER TWENTY-ONE\nRE: MORE EFFECTIVELY UTILIZING INFORMATION TECHNOLOGY RESOURCES\n"
    with pytest.raises(ValueError, match="Executive Order Number Twenty"):
        states.check_identity(EO, other, "pdf")
    mention = "EXECUTIVE ORDER\nNUMBER FIFTY-FIVE\nRE: X\n... pursuant to Executive Order Number Twenty dated August 27, 2010 ...\n"
    with pytest.raises(ValueError, match="Executive Order Number Twenty"):
        states.check_identity(EO, mention, "pdf")


# ---- source_version: DTI's PDFs print "Revision Number: N" and "Reviewed: M/D/YYYY" in the title block ------
# Fixtures are the text of the real PDFs (pdftotext -layout), whole, with page furniture.

def _fix(name):
    return (FIX / name).read_text()


def test_policy_pdf_version_is_the_printed_revision_and_review_date():
    assert states.source_version(_fix("dti-0042-02.txt"), "policy", "delaware", "pdf") == "Revision 13 (reviewed 7/3/2025)"


def test_revision_zero_is_a_version_not_an_absence():
    assert states.source_version(_fix("ot-ai-001.txt"), "policy", "delaware", "pdf") == "Revision 0 (reviewed 7/3/2025)"


def test_standard_pdf_version_reads_the_standard_title_block():
    assert states.source_version(_fix("se-access-001.txt"), "standard", "delaware", "pdf") == "Revision 6 (reviewed 7/20/2022)"


def test_a_page_without_the_title_block_has_no_version():
    assert states.source_version(text(SC03), "statute", "delaware", "html") == ""
    assert states.source_version("A policy with no title block.\n", "policy", "delaware", "pdf") == ""


def test_a_revision_without_a_review_date_is_still_the_revision():
    assert states.source_version("Revision Number: 4\n", "policy", "delaware", "pdf") == "Revision 4"


# ---- section-range slices of a chapter page (owner decision 2026-11-13: IT-governance sections of other law) ----

def sliced(raw, start, end):
    return ing.to_text(raw, "html", "statute", "delaware", {"section_start": start, "section_end_before": end})


def test_a_slice_starts_at_the_first_heading_and_keeps_the_page_heads():
    lines = sliced(T19C7, "705", "706").splitlines()
    assert lines[:2] == ["TITLE 19", "Labor"]
    assert "CHAPTER 7. Employment Practices" in lines
    assert lines[lines.index("") + 1].startswith("§ 705. Notice of monitoring")


def test_a_slice_includes_every_section_in_range_and_excludes_the_next_section():
    t = sliced(T29C5, "515", "518")
    heads = [l for l in t.splitlines() if l.startswith("§ ")]
    assert [h.split(".")[0] for h in heads] == ["§ 515", "§ 516", "§ 517"]
    assert "§ 518." not in t and "§ 514." not in t


def test_a_one_section_slice_holds_only_that_section_with_its_history():
    t = sliced(T19C7, "705", "706")
    heads = [l for l in t.splitlines() if l.startswith("§ ")]
    assert len(heads) == 1
    assert "(b) No employer, nor any agent or any representative of any employer, shall monitor" in t
    assert t.rstrip().endswith("73 Del. Laws, c. 148, § 1; 73 Del. Laws, c. 403, §§ 1, 2;")
    assert "Continuation of labor contracts" not in t and "Polygraph" not in t


def test_a_slice_carries_no_page_furniture():
    t = sliced(T29C5, "515", "516")
    for furniture in ("Authenticated PDF", "Toggle navigation", "Delaware General Assembly", "Twitter"):
        assert furniture not in t
    assert [l for l in t.splitlines() if l.strip() in ("§ 515", "§ 516")] == []


def test_a_slice_whose_start_or_end_is_not_on_the_page_is_refused():
    with pytest.raises(ValueError, match="section 799"):
        sliced(T19C7, "799", "800")
    with pytest.raises(ValueError, match="section 799"):
        sliced(T19C7, "705", "799")


def test_a_slice_is_not_the_whole_page():
    assert sliced(T19C7, "705", "706") != text(T19C7)
    assert len(sliced(T19C7, "705", "706")) < len(text(T19C7)) // 4


def test_slice_identity_requires_the_first_and_last_cited_sections():
    ok = seed("19 Del. C. 705")
    states.check_identity(ok, sliced(T19C7, "705", "706"), "html")
    states.check_identity(seed("29 Del. C. 515 to 517"), sliced(T29C5, "515", "518"), "html")
    with pytest.raises(ValueError, match="is not 19 Del. C. 706"):
        states.check_identity(seed("19 Del. C. 706"), sliced(T19C7, "705", "706"), "html")
    with pytest.raises(ValueError, match="is not 29 Del. C. 515 to 516"):
        states.check_identity(seed("29 Del. C. 515 to 516"), sliced(T29C5, "515", "518"), "html")


def test_slice_identity_refuses_a_repealed_section():
    t = sliced(T29C5, "523", "524")
    assert "[Repealed]" in t
    with pytest.raises(ValueError, match="repealed"):
        states.check_identity(seed("29 Del. C. 523"), t, "html")


def test_real_709c_heading_is_a_not_yet_effective_mark():
    from src.states import delaware
    heading = [l for l in text(T19C7).splitlines() if l.startswith("§ 709C.")][0]
    assert delaware._HEAD_EFFECTIVE.search(heading).groups() == ("Sep", "26", "2027")


def test_slice_identity_refuses_a_not_yet_effective_section():
    from src.states import delaware
    t = "TITLE 19\nLabor\n\n§ 709C. Pay.  [Effective Jan. 1, 2099]\n(a) text\n"
    sec = delaware._SECTIONS.fullmatch("19 Del. C. 709C")
    with pytest.raises(ValueError, match="not in force"):
        states.check_identity(seed("19 Del. C. 709C"), t, "html")
    # and the date comparison itself takes today as a parameter, so no clock change can flip it
    import datetime
    src = seed("19 Del. C. 709C")
    with pytest.raises(ValueError, match="not in force until 2027-09-26"):
        delaware._check_sections(src, "TITLE 19\nLabor\n\n§ 709C. Pay.  [Effective Sept. 26, 2027]\n(a) x\n", "html", sec,
                                 today=datetime.date(2026, 11, 13))
    assert delaware._check_sections(src, "TITLE 19\nLabor\n\n§ 709C. Pay.  [Effective Sept. 26, 2027]\n(a) x\n", "html", sec,
                                    today=datetime.date(2027, 10, 1))


def test_slice_notes_name_the_range():
    n = states.hook("delaware", "notes")(seed("19 Del. C. 705", slice={"section_start": "705", "section_end_before": "706"}),
                                         "html", sliced(T19C7, "705", "706"))
    assert "section 705" in n and "before the heading of section 706" in n

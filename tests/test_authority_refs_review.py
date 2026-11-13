"""Seam: src.authority_refs, the review pass. Each case is text copied verbatim from a committed document
(the file is named beside it; test_every_sample_is_in_its_document keeps that true) and the resolution the
documents themselves support. Written before the code that makes them pass."""
import os
from pathlib import Path

import pytest

from src import authority_refs as ar

ROOT = Path(__file__).resolve().parent.parent

# NOT PART OF THE GATE (owner decision, 2026-11-13: the authority-reference pass is not gated). Every case here
# resolves a citation against the seed lists and documents AS COMMITTED, so seeding a cited instrument, or
# rewording a left_out record, changes the right answer and fails the case. Run them when working on the tool:
#   AUTHORITY_REFS_LIVE=1 python3 -m pytest tests/test_authority_refs_review.py -q
# and expect to update the samples whose instruments have since been seeded.
pytestmark = pytest.mark.skipif(os.environ.get("AUTHORITY_REFS_LIVE") != "1",
                                reason="resolves against the live seed lists; set AUTHORITY_REFS_LIVE=1 to run")

# (state, verbatim text, document, expected [(section token, status)])
RESOLVED = [
    # Delaware: History lines are not section headings, so 29 Del. C. 502 is not held by chapter 90C
    ("delaware", "29 Delaware Code §501-\n          526), DTI makes and retains copies", "policies/delaware/de-pi-erec-001.md",
     [("29/501", "LEFT_OUT")]),
    ("delaware", "21st Century\nCommunications and Video Accessibility Act of 2010 (CVAA), and Title 6 Delaware Code\n4504.",
     "policies/delaware/de-ac-dig-001.md", [("6/4504", "NOT_HELD")]),
    ("delaware", "will be posted on the DTI website. 29 Del. C. § 9004C(10).", "policies/delaware/de-oth-psp-001.md",
     [("29/9004C", "HELD")]),
    # Iowa: chapter 8B was transferred to chapter 8; the held sections print 'C2014, §8B.21' and so on
    ("iowa", "by Iowa Code section 8B.21(​k​)-(​l​).", "standards/iowa/ia-ocio-1054.md", [("8B.21", "HELD")]),
    ("iowa", "This standard applies to all agencies as defined by Iowa Code Chapter 8A, Section 101. Non-",
     "standards/iowa/ia-ocio-1030.md", [("8A.101", "LEFT_OUT")]),
    ("iowa", "This standard applies to all participating agencies as defined by Iowa Code Chapter 8A.201. Non-participating",
     "standards/iowa/ia-ocio-1034.md", [("8A.201", "LEFT_OUT")]),
    # Maryland: every 3A-3xx section is the held 3.5-3xx
    ("maryland", "State Finance and Procurement Article, §§3A-303(a)(5), 3A-311, and 3A-312, Annotated Code of Maryland",
     "rules/maryland/md-comar-14-33.md", [("3A-303", "HELD"), ("3A-311", "HELD"), ("3A-312", "HELD")]),
    # Maine: a footnote mark glued to the section number, named by the footnote's own URL
    ("maine", "3.4.   InforME: Information Resource of Maine. Defined in 1 MRSA, Chapter 14, §533. 1",
     "policies/maine/me-oit-domain-name.md", [("1/533", "HELD")]),
    # New York: 'No. 117' and footnote mark 1
    ("new-york", "Section 1 of Executive Order No. 1171, issued January 2002, charges the State Chief",
     "policies/new-york/ny-its-p24-003.md", [("1171", "HELD")]),
    # Michigan: a compiled place of an order is not a citation of a statute
    ("michigan", "d. Executive Order 2002-14, MCL 18.62.", "executive-orders/michigan/mi-eo-2009-55.md", [("2-14", "HELD")]),
    # New Mexico
    ("new-mexico", '   Chapter 9, Article 27 NMSA 1978 may be cited as the "Department of Information',
     "statutes/new-mexico/nm-nmsa-9-27.md", [("9-27", "HELD")]),
    # Hawaii: the seed holds chapters 487N and 487R section by section
    ("hawaii", "information including information defined in HRS chapters 487N, 487R, and Acts",
     "policies/hawaii/hi-pol-ets-103-01.md", [("487N", "HELD"), ("487R", "HELD")]),
]


def full_texts():
    return ar.load_texts()


def resolved(state, text):
    rv = ar.Resolver(state, ar.load_seed(state, full_texts()))
    return [(r.cite.sec, r.status) for r in (rv.resolve(c) for c in ar.extract(state, text))]


@pytest.mark.parametrize("state,text,source,expected", RESOLVED, ids=[f"{r[0]}-{i}" for i, r in enumerate(RESOLVED)])
def test_resolution_the_documents_support(state, text, source, expected):
    assert resolved(state, text) == expected


def test_every_review_sample_is_in_its_document():
    for state, text, source, _ in RESOLVED:
        assert text.strip() in (ROOT / source).read_text(encoding="utf-8"), (source, text[:60])
        assert source.split("/")[1] == state


# ---- the section harvest ----------------------------------------------------------------------------

def test_harvest_takes_section_headings_and_never_a_history_line():
    texts = full_texts()
    code = ar.code_of("delaware", "DEL")
    got = ar.harvest_sections("delaware", code, "29", texts["de-code-29-ch-90c-subch-i"])
    toks = {t for _, t in got}
    assert "29/9001C" in toks and "29/9016C" in toks
    assert not any(t.startswith(("29/73", "29/74", "29/82", "29/84")) for t in toks)


def test_held_ranges_of_a_partly_held_chapter_are_exact():
    seed = ar.load_seed("delaware", full_texts())
    by_id = {h.seed_id: h for h in seed.holdings}
    (cid, lo, hi), = by_id["de-code-29-ch-90c-subch-i"].ranges
    assert (lo, hi) == ("29/9001C", "29/9016C")


# ---- page footers and renumbering --------------------------------------------------------------------

def test_a_page_footer_after_a_section_is_not_the_end_of_a_range():
    text = "  See MD. State Government Code Ann. § 10-1301\n\n                                                -2-\n\nnext"
    got = [(c.sec, c.end) for c in ar.extract("maryland", text)]
    assert got == [("10-1301", None)]


def test_the_history_lines_of_held_sections_give_the_old_numbers():
    rv = ar.Resolver("iowa", ar.load_seed("iowa", full_texts()))
    for old, new in (("8B.1", "8.76"), ("8B.21", "8.77"), ("8B.23", "8.84"), ("8B.24", "8.85")):
        assert rv.seed.history_map[("IC", old)] == ("IC", new), old


def test_a_chapter_cited_by_its_old_number_resolves_to_the_chapter_that_took_its_sections():
    assert [(s, st) for _, s, st, _ in [(0, r.cite.sec, r.status, 0) for r in ar.resolve_text("iowa", "Iowa Code chapter 8B")]] == [("8B", "HELD")]


def test_a_footnote_mark_run_into_a_section_number_is_named_by_the_footnotes_own_url():
    texts = full_texts()
    rv = ar.Resolver("maine", ar.load_seed("maine", texts))
    for doc, want in (("me-oit-mobile-device", "10/1347"), ("me-oit-remote-hosting", "10/1347")):
        got = [(c.sec, rv.resolve(c).status) for c in ar.extract("maine", texts[doc]) if c.sec.startswith("10/134")]
        assert got and all(g == (want, "HELD") for g in got), (doc, got)


# ---- citation forms that print no code name ----------------------------------------------------------

BARE = [
    ("arizona", "D. Monies in the state web portal fund are exempt from the provisions of section 35-190 relating to lapsing of appropriations.",
     "statutes/arizona/az-ars-18-421.md", [("ARS", "35-190")]),
    ("florida", "2. For cybersecurity breaches, state agencies shall provide notice in accordance with s. 501.171.",
     "statutes/florida/fl-st-282.md", [("FS", "501.171")]),
    ("minnesota", "(c) Subject to sections 16C.08 and 16C.09, the chief information officer may allow a state agency to obtain services",
     "statutes/minnesota/mn-stat-16e.md", [("MS", "16C.08"), ("MS", "16C.09")]),
    ("montana", "as a part of the legislative branch information technology plan, as provided for in 5-11-405, that will fulfill the intent of adequate rules for use of information technology resources for the consolidated legislative branch, as provided for in 5-2-504.",
     "statutes/montana/mt-mca-2-17-504.md", [("MCA", "5-11-405"), ("MCA", "5-2-504")]),
    ("massachusetts", "                •   Personal data as defined in Mass. Gen. Laws chapter 66A, § 1;",
     "policies/massachusetts/ma-edp-01.md", [("MGL", "66A/1")]),
    ("massachusetts", "The secretary shall, notwithstanding section 45 of chapter 30 and chapter 31, appoint a qualified individual",
     "statutes/massachusetts/ma-gl-7d.md", [("MGL", "30/45")]),
]


@pytest.mark.parametrize("state,text,source,expected", BARE, ids=[f"{b[0]}-{i}" for i, b in enumerate(BARE)])
def test_a_section_printed_with_no_code_name_is_read(state, text, source, expected):
    assert [(c.code, c.sec) for c in ar.extract(state, text)] == expected


def test_every_bare_sample_is_in_its_document():
    for state, text, source, _ in BARE:
        assert text.strip() in (ROOT / source).read_text(encoding="utf-8"), (source, text[:60])


@pytest.mark.parametrize("state,text", [
    ("minnesota", "See section 4.2 of this policy and Table 3.1 for the schedule."),
    ("montana", "The review was held on 10-12-2025 and again on 11-1-2025."),
    ("florida", "Complete section 3.5 of the form before step 2."),
])
def test_a_number_that_is_not_a_section_of_the_state_is_not_read(state, text):
    assert ar.extract(state, text) == []


def test_the_audit_does_not_depend_on_the_forms_it_audits():
    """A statute number printed after a section sign counts as a probable citation whether or not a code name
    precedes it, so a form the table cannot read shows up as missed."""
    text = "exempt from the provisions of section 35-190 relating to lapsing"
    f, ccs, _ = ar._compiled("arizona")
    n, *miss = ar.audit_text("arizona", text, [])
    assert n >= 1 and len(miss) == n
    n2, *miss2 = ar.audit_text("arizona", text, ar.extract("arizona", text))
    assert n2 == n and miss2 == []


# ---- the seed's left_out prose names instruments by bare number -----------------------------------------

LEFT_OUT = [
    ("colorado", "       (C.R.S. 24-72-501, et seq.)", "policies/colorado/co-oit-cisp-004.md", [("24-72-501", "LEFT_OUT")]),
    ("kentucky", "procedures and practices of KRS 61.931 through KRS 61.934 for notification and reporting",
     "policies/kentucky/ky-cio-090.md", [("61.931", "LEFT_OUT")]),
    ("nebraska", "    (1) Purpose. Pursuant to Neb. Rev. Stat. §§ 81-1117, 81-1120.17, and 81-1120.20, certain",
     "policies/nebraska/ne-nitc-1-204.md", [("81-1117", "LEFT_OUT"), ("81-1120.17", "LEFT_OUT"), ("81-1120.20", "LEFT_OUT")]),
    ("minnesota", "Governor’s Executive Order 19-22", "standards/minnesota/mn-mnit-it-disaster-recovery-standard.md",
     [("19-22", "LEFT_OUT")]),
    ("massachusetts", "Executive Order No. 628 is rescinded effective immediately.", "executive-orders/massachusetts/ma-eo-629.md",
     [("628", "LEFT_OUT")]),
    ("louisiana", "- Executive Order Number JML 25-103: State Government’s Use of AI.",
     "policies/louisiana/la-ots-ai-acceptable-use-policy.md", [("JML-25-103", "LEFT_OUT")]),
    ("michigan", "g. Executive Order 2002-19, MCL 38.1173.", "executive-orders/michigan/mi-eo-2009-55.md", [("2-19", "LEFT_OUT")]),
    ("maryland", "Maryland Total Human-services Integrated Network(Amends Executive Order 01.01.2021.11)",
     "executive-orders/maryland/md-eo-01-01-2022-03.md", [("01.01.2021.11", "LEFT_OUT")]),
    ("vermont", "ADS is responsible, under 22 V.S.A. § 901(a)(1), for providing direction and oversight for all",
     "policies/vermont/vt-it-procurement-guideline.md", [("22/901", "LEFT_OUT")]),
]


@pytest.mark.parametrize("state,text,source,expected", LEFT_OUT, ids=[f"{r[0]}-{i}" for i, r in enumerate(LEFT_OUT)])
def test_an_instrument_the_seed_records_as_left_out_by_bare_number_is_left_out(state, text, source, expected):
    assert resolved(state, text) == expected


def test_every_left_out_sample_is_in_its_document():
    for state, text, source, _ in LEFT_OUT:
        assert text.strip() in (ROOT / source).read_text(encoding="utf-8"), (source, text[:60])


def test_an_open_ended_left_out_range_covers_the_sections_after_it():
    # north-carolina.yml: "G.S. 147-33.72 and following (the former Article 3D ...)"
    assert resolved("north-carolina", "authority G.S. 147-33.80")[0][1] == "LEFT_OUT"
    assert resolved("north-carolina", "authority G.S. 147-64.6")[0][1] != "LEFT_OUT"


# ---- authority context: reference blocks and bracketed source notes ------------------------------------

def ctx(text, needle):
    return ar.in_authority_context(text, text.index(needle))


def test_a_related_documents_block_is_authority_context_however_long_the_list():
    text = (ROOT / "standards/nevada/nv-sec-s-4-08-02.md").read_text(encoding="utf-8")
    assert ctx(text, "NRS 281.195, Use of Computers")
    assert ctx(text, "NRS 242.181, Adherence")


def test_a_long_references_list_stays_authority_context_until_prose_resumes():
    text = (ROOT / "policies/colorado/co-oit-cisp-004.md").read_text(encoding="utf-8")
    assert ctx(text, "C.R.S. 24-72-501") and ctx(text, "C.R.S. 24-73-101")


def test_a_bracketed_source_note_is_authority_context():
    text = (ROOT / "policies/nebraska/ne-nitc-7-101.md").read_text(encoding="utf-8")
    assert ctx(text, "[Neb. Rev. Stat. § 81-1120.27(1)]") is True or ar.in_authority_context(text, text.index("Neb. Rev. Stat. § 81-1120.27(1)"))


def test_a_numbered_heading_ends_a_reference_block():
    text = "5.0   RELATED DOCUMENTS\n      NRS 242.181, Adherence\n\n6.0   STANDARD\n\n      6.1     Reporting\n      See also NRS 281.195 for the rest."
    assert ctx(text, "NRS 242.181") and not ar.in_authority_context(text, text.index("NRS 281.195"))


# ---- readings the review found wrong ----------------------------------------------------------------

READ = [
    # a code name that ends a sentence does not take the next line's heading number
    ("california", "Note: Authority cited: Section 16.5, Government Code. Reference: Section 16.5, Government Code.\n22001. Digital Signatures Must Be Created by an Acceptable Technology.",
     "rules/california/ca-ccr-2-div-7-ch-10.md", [("Gov", "16.5", None), ("Gov", "16.5", None)]),
    ("california", "section 10851, Welfare and Institutions Code.\n22620.2. Applicability of Electronic Document or Record Standards",
     "rules/california/ca-ccr-2-div-7-ch-15.md", [("WIC", "10851", None)]),
    ("new-york", "fee prescribed by Section 87 of the Public Officers Law.\nSection 551.5 Public",
     "rules/new-york/ny-nycrr-551.md", []),
    # a reversed range printed in the source is two sections, not a range
    ("california", "Government Code Sections 7923.75-7923.55, 7929.210,", "standards/california/ca-simm-5305-f.md",
     [("Gov", "7923.75", None), ("Gov", "7923.55", None), ("Gov", "7929.210", None)]),
    # a list number after a semicolon is not another section
    ("california", "or (f) of Civil Code Section 1798.24;\n            6. If the form contains open fields where the data subject may input unrestricted content, a",
     "standards/california/ca-simm-5310-a.md", [("Civ", "1798.24", None)]),
    # a new title restarts the qualifier inside one list; a hyphenated section is one section
    ("oklahoma", "Pursuant to 62 O.S. §34.11.1 and 74 O.S. §85.5, the Chief Information Officer (“CIO”) has sole",
     "policies/oklahoma/ok-pol-isd-procurement.md", [("OS", "62/34.11.1", None), ("OS", "74/85.5", None)]),
    ("oklahoma", "See 74 O.S. 85.5, 62\nO.S.34.1 et seq., and OAC 260:115-1-1", "standards/oklahoma/ok-std-use-of-ai-in-oklahoma-state-government.md",
     [("OS", "74/85.5", None), ("OS", "62/34.1", None), ("OAC", "260:115-1-1", None)]),
    ("oklahoma", "As established by 74 O.S. § 840-8.1, all state agencies should adopt a policy governing",
     "policies/oklahoma/ok-pol-social-media-guidelines.md", [("OS", "74/840-8.1", None)]),
    # a lower-case letter in a New Jersey section number
    ("new-jersey", "        N.J.S.A.52:18a-230b.", "policies/new-jersey/nj-njoit-15-06.md", [("NJSA", "52:18A-230b", None)]),
    # the old number of a rule, printed beside its new number
    ("new-mexico", "in accordance with 1 NMAC 3.3.20, Emergency Rules [now 1.24.20 NMAC].", "rules/new-mexico/nm-nmac-1-12-2.md",
     [("NMAC", "1.24.20", None)]),
    # an article is not a chapter
    ("north-carolina", "(North Carolina General Statutes Article 76, Sections 143-735 through 143-", "standards/north-carolina/nc-gis-water-sewer-data-standard.md",
     []),
]


def _read(state, text):
    return [(c.code, c.sec, c.end) for c in ar.extract(state, text)]


@pytest.mark.parametrize("state,text,source,expected", READ, ids=[f"{r[0]}-{i}" for i, r in enumerate(READ)])
def test_the_reading_the_documents_support(state, text, source, expected):
    got = _read(state, text)
    assert [g[:2] for g in got][:len(expected)] == [e[:2] for e in expected]
    assert len(got) >= len(expected)
    if not expected:
        assert got == []


def test_every_reading_sample_is_in_its_document():
    for state, text, source, _ in READ:
        assert text.strip() in (ROOT / source).read_text(encoding="utf-8"), (source, text[:60])


def test_a_citation_in_a_statutes_source_line_or_a_revision_history_row_is_not_enabling_authority():
    line = "Source: SL 1994, ch 412 (Ex. Ord. 94-4), § 17; SL 2003, ch 272 (Ex. Ord. 03-1), § 82; SL 2026, ch 1 (Ex. Ord. 26-2), § 17, eff. Apr. 13, 2026."
    assert line in (ROOT / "statutes/south-dakota/sd-sdcl-1-33-bit.md").read_text(encoding="utf-8")
    cs = [c for c in ar.extract("south-dakota", line) if c.kind == "eo"]
    assert len(cs) == 3 and all(ar.is_history_reference("statute", line, c.start) for c in cs)
    row = "03/22/2007 | Updated policy to reflect the rescission of Executive Order 2004-02T."
    assert row in (ROOT / "policies/ohio/oh-it-01.md").read_text(encoding="utf-8")
    [c] = ar.extract("ohio", row)
    assert ar.is_history_reference("policy", row, c.start)
    live = "pursuant to Executive Order 2019-15D, the Department shall"
    [c] = ar.extract("ohio", live)
    assert not ar.is_history_reference("policy", live, c.start)


def test_a_rule_history_note_with_the_old_number_is_not_a_citation():
    line = "[1.12.1.1 NMAC - Rp/E, 1 NMAC 12.1.1, 12/02/2005]"
    assert line in (ROOT / "rules/new-mexico/nm-nmac-1-12-1.md").read_text(encoding="utf-8")
    assert all(ar.is_history_reference("rule", line, c.start) for c in ar.extract("new-mexico", line))


# ---- numbers the corpus records as another number ----------------------------------------------------------

ALIAS = [
    ("texas", "1 TAC § 202.25", "standards/texas/tx-dir-security-control-standards-catalog.md", [("1/202.25", "STUB")]),
    ("washington", "RCW 52.105.450 (6, 8) Office of Cybersecurity – Higher education, Judicial, and Legislative", "policies/washington/wa-sec-01.md",
     [("52.105.450", "HELD")]),
    ("virginia", "The Code of Virginia §2-2.2009 states that \u201cthe CIO shall direct the development of policies,",
     "standards/virginia/va-sec530-01-2.md", [("2-2", "HELD")]),
    ("new-mexico", "those authorized pursuant to Section 15-5-1 NMSA 1978 [9-27-20 NMSA 1978], except", "statutes/new-mexico/nm-nmsa-9-27.md",
     [("15-5-1", "HELD"), ("9-27-20", "HELD")]),
    ("oregon", "OAR 128-030-0020, ORS 182.122, 182.124 and 184.473", "", [("182.122", "HELD"), ("182.124", "HELD"), ("184.473", "HELD")]),
]


@pytest.mark.parametrize("state,text,source,expected", ALIAS, ids=[f"{r[0]}-{i}" for i, r in enumerate(ALIAS)])
def test_a_number_the_corpus_records_as_another_number_resolves_to_it(state, text, source, expected):
    got = resolved(state, text)
    assert [g for g in got if g[0] in dict(expected)] == expected


def test_every_alias_sample_is_in_its_document():
    for state, text, source, _ in ALIAS:
        if source:
            assert text.strip().split("\n")[0] in (ROOT / source).read_text(encoding="utf-8"), (source, text[:60])


def test_a_list_closed_by_its_code_name_does_not_swallow_the_next_codes_section():
    text = "Reference: sections 25105, 26205, 26205.1, 26205.5, 26907, 27001, 27322.2, 34090.5, and 60203, Government Code; section 102235, Health and Safety Code; and section 10851, Welfare and Institutions Code."
    assert text in (ROOT / "rules/california/ca-ccr-2-div-7-ch-15.md").read_text(encoding="utf-8")
    assert [(c.code, c.sec) for c in ar.extract("california", text)] == [
        ("Gov", "25105"), ("Gov", "26205"), ("Gov", "26205.1"), ("Gov", "26205.5"), ("Gov", "26907"), ("Gov", "27001"),
        ("Gov", "27322.2"), ("Gov", "34090.5"), ("Gov", "60203"), ("HSC", "102235"), ("WIC", "10851")]


def test_a_new_mexico_article_the_seed_names_without_the_code_is_left_out():
    assert resolved("new-mexico", "Chapter 15, Article 1C NMSA 1978") == [("15-1C", "LEFT_OUT")]


@pytest.fixture(scope="module")
def report():
    return ar.build_report()


def test_one_instrument_is_one_row_however_it_is_cited(report):
    wy = [i["instrument"] for i in report["states"]["wyoming"]["not_held"] if "16-4-20" in i["instrument"]]
    assert wy == ["W.S. 16-4-201 to 16-4-205"]
    va = [i["instrument"] for i in report["states"]["virginia"]["not_held"] if i["instrument"].startswith("Executive Order 35")]
    assert va == ["Executive Order 35 (2019)"]


def test_a_statutes_own_definitions_range_is_not_a_citation_of_another_instrument(report):
    kan = {i["instrument"] for i in report["states"]["kansas"]["not_held"]}
    assert "K.S.A. 75-7212" not in kan
    assert report["states"]["kansas"]["self_range_citations_excluded"] >= 1


def test_the_report_says_how_many_chapter_citations_were_rolled_up(report):
    assert report["states"]["hawaii"]["rolled_up_chapter_citations"] == 2
    assert report["states"]["iowa"]["history_renumbered_citations"]["resolved"] > 50


def test_no_not_held_candidate_was_resolved_away_by_a_prose_number_it_does_not_match(report):
    # the bare-number reading of the seed's prose may hide an instrument only when the number is the one named there
    held_out = {i["instrument"] for i in report["states"]["oregon"]["left_out"]}
    assert not any(i["instrument"].startswith("ORS 182.122") for i in report["states"]["oregon"]["not_held"])
    assert held_out


def test_an_et_seq_left_out_range_covers_the_sections_after_it():
    # california.yml: "Civ. Code 1798.80 et seq." is left out; 1798.82 is one of those sections
    assert resolved("california", "Civil Code Section 1798.82")[0][1] == "LEFT_OUT"

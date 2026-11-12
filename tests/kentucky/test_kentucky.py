"""Kentucky through the shared seam (src.ingest / src.states): the General Assembly serves each KRS section as its
own one-page PDF and each administrative regulation as a PDF; COT's policy library is PDFs; the executive orders on
COT's page are scans. Fixtures are real bytes fetched on 2026-11-12 through the toolkit Fetcher: KRS 42.724 and
61.9307 whole, 200 KAR 1:016 whole, COT policy CIO-050 whole, and the first sixty lines of tesseract's reading of
Executive Orders 2012-880 and 2013-403 (the second repeats the first's number in a "whereas")."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "kentucky"
KRS_42_724 = (FIX / "krs-42-724.pdf").read_bytes()
KRS_61_9307 = (FIX / "krs-61-9307.pdf").read_bytes()
KAR = (FIX / "200-kar-1-016.pdf").read_bytes()
CIO_050 = (FIX / "cio-050.pdf").read_bytes()
EO_2012 = (FIX / "eo-2012-880-ocr-head.txt").read_text()
EO_2013 = (FIX / "eo-2013-403-ocr-head.txt").read_text()
KY = "kentucky"


def src(**kw):
    base = {"id": "ky-test", "jurisdiction": KY, "doc_type": "statute", "citation": "KRS 42.724",
            "title": "KRS 42.724 Commonwealth Office of Technology", "format": "pdf"}
    return {**base, **kw}


def text(raw, doc_type):
    return ing.to_text(raw, "pdf", doc_type, KY, None, "apps.legislature.ky.gov")


def test_the_state_is_found_by_name():
    assert KY in states.modules(refresh=True)


# ---- statutes: one section per PDF ---------------------------------------------------------

def test_a_section_pdf_is_the_section_number_and_catchline_then_the_text_then_the_effective_and_history_lines():
    t = text(KRS_42_724, "statute")
    assert t.startswith("42.724 Commonwealth Office of Technology.\n")
    assert "(c) Office of the Chief Information Security Officer." in t
    assert "Effective: June 29, 2021" in t
    assert t.rstrip().endswith("Formerly codified as KRS 11.505.")


def test_the_section_identity_is_the_number_the_page_opens_with():
    states.check_identity(src(), text(KRS_42_724, "statute"))
    states.check_identity(src(citation="KRS 61.9307", id="ky-t2"), text(KRS_61_9307, "statute"))


@pytest.mark.parametrize("citation", ["KRS 42.726", "KRS 42.72", "KRS 61.9307", "42.724"])
def test_another_sections_citation_is_refused(citation):
    with pytest.raises(ValueError, match="is not"):
        states.check_identity(src(citation=citation), text(KRS_42_724, "statute"))


def test_a_statute_never_gets_an_effective_date_from_its_history_line():
    assert states.effective_date(text(KRS_42_724, "statute"), "statute", KY) is None


# ---- rules: one regulation per PDF ---------------------------------------------------------

def test_a_regulation_pdf_opens_with_the_cabinet_and_carries_its_number_and_title():
    t = text(KAR, "rule")
    assert "200 KAR 1:016. Data breach notification forms." in t
    assert "(49 Ky.R. 190, 758; eff. 1-3-2023.)" in t


def test_the_regulation_identity_is_its_printed_number_and_title():
    r = src(doc_type="rule", citation="200 KAR 1:016", title="Data breach notification forms")
    states.check_identity(r, text(KAR, "rule"))
    for bad in (dict(citation="200 KAR 1:015"), dict(citation="200 KAR 1:01"), dict(title="Access to public records")):
        with pytest.raises(ValueError, match="is not"):
            states.check_identity({**r, **bad}, text(KAR, "rule"))


def test_the_regulation_effective_date_is_the_eff_date_of_its_history_line():
    assert states.effective_date(text(KAR, "rule"), "rule", KY) == "2023-01-03"


# ---- policies: the shared label reader and identity still apply -----------------------------

def test_a_policy_pdf_keeps_its_printed_en_dash_title_and_the_shared_identity_text_matches_it():
    t = text(CIO_050, "policy")
    p = src(doc_type="policy", citation="CIO-050", title="Enterprise Procurement of Information Technology Assets",
            identity_text="CIO-050: Enterprise Procurement of Information Technology")
    states.check_identity(p, t)
    assert states.effective_date(t, "policy", KY) == "2014-12-15"
    with pytest.raises(ValueError, match="is not the cited"):
        states.check_identity({**p, "identity_text": "CIO-051: Information Technology Standards"}, t)


# ---- executive orders: scans, identified by the number in the order's own heading -----------

def eo(number):
    return src(doc_type="executive_order", citation=f"Executive Order {number}", title="x")


def test_an_order_is_identified_by_the_number_printed_in_its_heading_before_the_first_whereas():
    states.check_identity(eo("2012-880"), EO_2012)
    states.check_identity(eo("2013-403"), EO_2013)


def test_a_whereas_that_names_another_order_does_not_identify_it():
    assert "Executive Order 2012-880" in EO_2013          # the 2013 order recites the 2012 one
    with pytest.raises(ValueError, match="is not the cited"):
        states.check_identity(eo("2012-880"), EO_2013)
    with pytest.raises(ValueError, match="is not the cited"):
        states.check_identity(eo("2013-403"), EO_2012)


# ---- every standard and policy in the seed list accepts only its own bytes ------------------

def test_no_policy_or_standard_identity_accepts_another_documents_bytes():
    """Policies cite the standards (CIO-072 cites ENT-201) and the KITS export names KITS, so a loose identity phrase
    would pass the wrong file. Each entry's check must accept its own committed text and every other entry's refuse it."""
    import yaml
    root = FIX.parent.parent.parent
    entries = [e for e in yaml.safe_load((root / "_meta/sources/kentucky.yml").read_text())["sources"]
               if e["doc_type"] in ("policy", "standard") and not e.get("watch_only")]
    texts = {e["id"]: (root / "_meta/snapshots" / f"{e['id']}.txt").read_text() for e in entries}
    assert len(entries) > 50
    accepted = []
    for e in entries:
        states.check_identity(e, texts[e["id"]])
        for other, t in texts.items():
            if other == e["id"]:
                continue
            try:
                states.check_identity(e, t)
            except ValueError:
                continue
            accepted.append((e["id"], other))
    assert accepted == []

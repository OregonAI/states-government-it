"""Oklahoma: OMES standards print their dates as month/day/year. Fixtures are real bytes (the whole PDF of the Use of AI in
Oklahoma State Government Standard, footer table and all)."""
from pathlib import Path

import pytest

from src import ingest as ing
from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "oklahoma"
STANDARD = (FIX / "use-of-ai-in-oklahoma-UA.pdf").read_bytes()
SRC = {"id": "ok-std-use-of-ai", "jurisdiction": "oklahoma", "doc_type": "standard", "format": "pdf",
       "citation": "OMES Use of AI in Oklahoma State Government Standard",
       "title": "Use of AI in Oklahoma State Government Standard"}


def test_the_state_is_found_by_name():
    assert "oklahoma" in states.modules(refresh=True)


def test_a_standard_prints_its_dates_as_month_day_year_and_the_shared_reader_takes_the_effective_one():
    text = ing.to_text(STANDARD, "pdf", "standard", "oklahoma")
    assert "Effective date: 03/06/2025" in text
    assert states.effective_date(text, "standard", "oklahoma") == "2025-03-06"


def test_the_last_revision_is_the_version():
    text = ing.to_text(STANDARD, "pdf", "standard", "oklahoma")
    assert states.source_version(text, "standard", "oklahoma", "pdf") == "Last revised 07/29/2026"


def test_a_document_that_prints_no_revision_has_no_version():
    assert states.source_version("Effective date: 03/06/2025\n", "standard", "oklahoma", "pdf") == ""


def test_a_standard_is_the_cited_one_when_it_prints_its_title():
    text = ing.to_text(STANDARD, "pdf", "standard", "oklahoma")
    states.check_identity(SRC, text, "pdf")
    with pytest.raises(ValueError):
        states.check_identity(dict(SRC, title="Firewall Security Standard"), text, "pdf")


AGENTS = (FIX / "ai-agent-agentic-systems-std-UA.pdf").read_bytes()
AGILE = (FIX / "agile-software-development.pdf").read_bytes()


def test_the_revision_table_is_the_effective_date_even_when_the_body_says_effective_date_earlier():
    # the body says "before the effective date of this Standard" 330 lines above the table
    text = ing.to_text(AGENTS, "pdf", "standard", "oklahoma")
    assert "before the effective date of this Standard" in text
    assert states.effective_date(text, "standard", "oklahoma") == "2026-07-30"
    assert states.source_version(text, "standard", "oklahoma", "pdf") == "Last revised 07/30/2026"


def test_a_table_that_capitalises_its_labels_is_read_the_same_way():
    text = ing.to_text(AGILE, "pdf", "standard", "oklahoma")
    assert "Last Revised: 06/11/2024" in text
    assert states.effective_date(text, "standard", "oklahoma") == "2024-06-11"
    assert states.source_version(text, "standard", "oklahoma", "pdf") == "Last revised 06/11/2024"


def test_a_document_without_the_table_leaves_the_date_to_the_shared_reader():
    assert states.effective_date("Effective: January 5, 2020\n", "policy", "oklahoma") == "2020-01-05"


def test_a_seed_entry_with_a_currency_note_gets_it_in_the_curator_notes():
    src = dict(SRC, currency_note="Currency unconfirmed: the portal refuses the Fetcher (OWNER DECISION).")
    text = ing.to_text(STANDARD, "pdf", "standard", "oklahoma")
    assert "Currency unconfirmed: the portal refuses the Fetcher (OWNER DECISION)." in ing.conversion_notes(src, "pdf", text)


def test_an_entry_without_a_currency_note_gets_no_extra_sentence():
    text = ing.to_text(STANDARD, "pdf", "standard", "oklahoma")
    assert "Currency" not in ing.conversion_notes(SRC, "pdf", text)

"""Seam: src.states.check_identity for a Wyoming executive order. The Governor's order prints its number as
'Order 2023-02' under the line 'EXECUTIVE ORDER' (never 'Executive Order 2023-02' on one line), so the shared
check, which looks for that phrase, refuses it. The fixture is the head of the scan read by tesseract."""
from pathlib import Path

import pytest

from src import states

FIX = Path(__file__).resolve().parent.parent / "fixtures" / "wyoming"
HEAD = (FIX / "eo-2023-02-page1-ocr.txt").read_text()
EO = {"id": "wy-eo-2023-02", "doc_type": "executive_order", "jurisdiction": "wyoming",
      "citation": "Executive Order 2023-02", "title": "Establishment of the Wyoming Cyber Assistance Response Effort Team"}


def test_the_heading_order_number_under_executive_order_is_the_identity():
    states.check_identity(EO, HEAD, "pdf")


def test_another_orders_number_is_refused():
    with pytest.raises(ValueError, match="2023-03"):
        states.check_identity({**EO, "citation": "Executive Order 2023-03"}, HEAD, "pdf")


def test_a_mention_of_the_number_in_the_body_is_not_the_heading():
    body = HEAD.replace("Order 2023-02", "Order 2022-09") + "\nsee Executive Order 2023-02 and Order 2023-02\n"
    with pytest.raises(ValueError):
        states.check_identity(EO, body, "pdf")


def test_other_document_types_are_left_to_the_shared_check():
    pol = {"id": "x", "doc_type": "policy", "jurisdiction": "wyoming", "citation": "WyIT 3001", "title": "General Security"}
    with pytest.raises(ValueError):
        states.check_identity(pol, "something else", "pdf")

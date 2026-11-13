# Wyoming: the authority-reference candidates, decided 2026-11-13

Owner decision 2026-11-13: a provision of a non-IT law is in scope, as a section slice, when its own focus is the
governance of state IT. Read in the Legislature's title PDFs (Fetcher, 2026-11-13).

| Candidate (held documents cite it) | Result |
|---|---|
| W.S. 40-21-101 to 40-21-119, Uniform Electronic Transactions Act (WyIT 1001) | 40-21-117 to 40-21-119 seeded (`wy-ws-40-21-117`); 40-21-101 to 40-21-116 declined, general transaction law (reasons in the left-out record) |
| W.S. 16-4-201 to 16-4-205, Public Records Act (12 documents, e.g. `wy-wyit-2001-g2`) | Declined; not done, owner question on subsection-level slices (16-4-202(d), 16-4-203(b)(xii)) |

## Public Records Act, declined

Declined, and left for an owner question: the IT-focused text is in subsections, inside general right-of-access sections.
16-4-202(d) is about electronic records alone: "If a public record exists primarily or solely in an electronic format ...
Electronic record inspection and copying shall be subject to the following". It covers costs "including the cost of
programming and computer services", alternative electronic file types, and no duty to allow inspection that "would jeopardize
or compromise the security or integrity of the original record or of any proprietary software in which it is maintained".
16-4-203(b)(xii) withholds "Information regarding the design, elements and components, and location of state information
technology security systems". Decision 1 names disclosure of the state's electronic records as IT governance, so these
subsections are of IT focus. But they sit in sections whose own focus is the general right of access: 16-4-202(a) "All public
records shall be open for inspection by any person at reasonable times, during business hours of the governmental entity", and
the article binds every governmental entity, counties and school districts included. The slice shape the seed check accepts is a
range of whole sections (section_start, section_end_before) and cannot cut a subsection, so the item is not clearly inside
decision 1. Owner question: approve subsection-level slices (16-4-202(d), 16-4-203(b)(xii)), or keep the Act out.
Its one rule-making sentence for state agencies, 16-4-204(e), has the Department of Administration and Information adopt
uniform fee and procedure rules: fees, not systems.
The records-retention half of the decision has no Wyoming section among the candidates; the one retention provision found,
40-21-112, applies to "a law [that] requires that a record be retained" and binds no agency in particular.

This reason is kept here and not in `left_out:` because `tests/test_authority_refs_review.py`
(`test_one_instrument_is_one_row_however_it_is_cited`) pins this instrument as NOT HELD for Wyoming: a left-out record that names
it makes the shared test fail. See the report's shared_changes_needed.

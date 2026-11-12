# 10 — The 20 analyst questions against four states: keyword and hybrid legs

Run 2026-11-12 on branch `eval/analyst-questions` (cut from `main` at bef1e67), issue #3 (Oregon) and issue #8 (the expected-documents check, four pilot states: Oregon, Washington, California, Colorado). Questions: `_meta/eval/questions.yml`, copied from `03-domain-taxonomy.md` section 5. Expected documents: `_meta/eval/expected/<state>.yml`, each document with a verbatim quote that `src/eval_questions.py` re-finds in the committed file. Earlier keyword-only trial for Oregon: `04-oregon-search-trial.md`. Every number below is the output of `src/eval_questions.py` (`--report --json`, and its `run_leg` at other cut-offs); none is typed from memory.

## Result

A cell is one (state, question) pair that has at least one expected document; 4 states and 20 questions give 80 pairs, of which 76 have expected documents (the other four have a `none_reason`: Colorado 10 and 20, Oregon 17, Washington 20). A cell PASSES when an expected document is in the first 5 hits of `compare` for that state, the question typed as written.

| State | Cells | Keyword leg | Hybrid leg |
|---|---|---|---|
| oregon | 19 | 1/19 (5%) | 18/19 (95%) |
| washington | 19 | 5/19 (26%) | 17/19 (89%) |
| california | 20 | 5/20 (25%) | 17/20 (85%) |
| colorado | 18 | 1/18 (6%) | 17/18 (94%) |
| **all four** | 76 | **12/76 (16%)** | **69/76 (91%)** |

Per question (cells are states with expected documents for that question):

| Question | Cells | Keyword | Hybrid |
|---|---|---|---|
| 1 | 4 | 1/4 | 4/4 |
| 2 | 4 | 0/4 | 4/4 |
| 3 | 4 | 1/4 | 4/4 |
| 4 | 4 | 1/4 | 2/4 |
| 5 | 4 | 1/4 | 4/4 |
| 6 | 4 | 1/4 | 4/4 |
| 7 | 4 | 0/4 | 3/4 |
| 8 | 4 | 0/4 | 1/4 |
| 9 | 4 | 2/4 | 3/4 |
| 10 | 3 | 1/3 | 3/3 |
| 11 | 4 | 2/4 | 4/4 |
| 12 | 4 | 0/4 | 4/4 |
| 13 | 4 | 0/4 | 4/4 |
| 14 | 4 | 2/4 | 4/4 |
| 15 | 4 | 0/4 | 4/4 |
| 16 | 4 | 0/4 | 4/4 |
| 17 | 3 | 0/3 | 3/3 |
| 18 | 4 | 0/4 | 4/4 |
| 19 | 4 | 0/4 | 4/4 |
| 20 | 2 | 0/2 | 2/2 |

**Reading it.** The keyword leg passes 12 of 76 cells. The hybrid leg passes 69 of 76. Both numbers are for the question text exactly as an analyst would type it, so the keyword figure is the honest pilot result for that leg, not a defect of the check: the check records it and fails only on a regression (see "The check" below).

Why the keyword leg is so low: the toolkit's keyword search requires every query term to match (`corpus_toolkit/mcp/backends.py`, `_fts_rows`: the terms are joined as quoted words, which SQLite FTS5 reads as all-terms AND). A 15-word question therefore returns nothing unless one document holds all 15 words. 59 of the 80 (state, question) queries returned no hit at all; 56 of those are cells with expected documents. A pass in the keyword leg is a question short enough, or worded closely enough to one document, to survive AND. The cut-off confirms this: the keyword leg barely moves from the top 1 to the top 20 (below), so ranking is not its problem, matching is.

Expected documents found in the top 5, counting each distinct (state, question, document) once: keyword 14 of 232, hybrid 138 of 232. A cell passes on one document; this counts all of them. It is capped for questions that list more than 5 documents.

### The cut-off

The check's cut-off is **5**. I measured 1, 3, 5, 10 and 20 for both legs (same tool, `run_leg(root, mode, cutoff)`):

| Cut-off (top N per state) | Keyword leg | Hybrid leg |
|---|---|---|
| 1 | 7/76 | 44/76 |
| 3 | 12/76 | 62/76 |
| 5 (the gate) | 12/76 | 69/76 |
| 10 | 13/76 | 73/76 |
| 20 | 14/76 | 75/76 |

I found no reason to move from 5. The keyword leg does not depend on it. The hybrid leg gains 4 cells from 5 to 10 and 2 more by 20; at 20 the one miss left is California question 8. A larger cut-off would raise the hybrid figure without saying the right document is near the top, so I kept it small as asked. The cut-off is an owner decision (it is `CUTOFF` in `src/eval_questions.py`; changing it makes the baseline out of date, by design).

### Hybrid cells that miss at 5

Seven cells: California 4, 7 and 8; Colorado 4; Oregon 8; Washington 8 and 9. At cut-off 10 the misses are California 4, California 8 and Washington 9; at 20, California 8 only. The per-question list below shows the top ids of each. I did not read the missing documents against the questions to judge whether the expected list or the ranking is at fault, except where the expected file's own quote answers the question (Oregon 8: the expected quote is ORS 276A.323(3), "The State Chief Information Officer shall determine and allocate the costs to state agencies associated with providing information technology services, third-party security evaluations, vulnerability assessments and remediation measures."; the hybrid top 5 holds only DAS policies, none of which is the statute).

## Oregon (issue #3)

Oregon has 49 documents on this branch (04 was run on 43). Of the 20 questions, 19 have expected documents and one (17, technology accessibility coordinator) has none: the `none_reason` records that all 49 Oregon documents were searched and no instrument answers it.

| Q | Expected (distinct ids) | Keyword top 5 | Hybrid top 5 | Keyword | Hybrid |
|---|---|---|---|---|---|
| 1 | 1 | 0 hits | 5 hits | fail | PASS |
| 2 | 6 | 0 hits | 5 hits | fail | PASS |
| 3 | 4 | 0 hits | 5 hits | fail | PASS |
| 4 | 3 | 0 hits | 5 hits | fail | PASS |
| 5 | 3 | 0 hits | 5 hits | fail | PASS |
| 6 | 6 | 1 hits | 5 hits | fail | PASS |
| 7 | 4 | 0 hits | 5 hits | fail | PASS |
| 8 | 1 | 0 hits | 5 hits | fail | fail |
| 9 | 2 | 5 hits | 5 hits | PASS | PASS |
| 10 | 2 | 0 hits | 5 hits | fail | PASS |
| 11 | 5 | 0 hits | 5 hits | fail | PASS |
| 12 | 5 | 0 hits | 5 hits | fail | PASS |
| 13 | 2 | 0 hits | 5 hits | fail | PASS |
| 14 | 5 | 0 hits | 5 hits | fail | PASS |
| 15 | 6 | 0 hits | 5 hits | fail | PASS |
| 16 | 5 | 0 hits | 5 hits | fail | PASS |
| 17 | none | 2 hits | 5 hits | no cell | no cell |
| 18 | 2 | 0 hits | 5 hits | fail | PASS |
| 19 | 3 | 0 hits | 5 hits | fail | PASS |
| 20 | 2 | 0 hits | 5 hits | fail | PASS |

Which documents each query returned, with the expected ones in bold and the ones missed, is in the per-question list below (Oregon lines). The two legs for Oregon: keyword 1 of 19, hybrid 18 of 19.

### Against the keyword-only trial in 04

04 ran `search_corpus` in keyword mode only, with two queries per question: the question reduced to its key words, and a second query worded from what the author had already read in the Oregon text. Its result: the first query returned an expected document for 4 questions (5, 6, 11, 12), no results for 13, and the informed query returned at least one expected document for 17 of 20. This run differs in four ways, so the numbers are not a like-for-like change:

1. **The query is the question as typed.** 04's first query was reduced to key words; this one is not reduced, so AND removes almost every result. Oregon keyword: 1 of 19 cells (question 9).
2. **No informed query.** 04's 17 of 20 used wording the author found in the documents; that is what the index can find, not what an analyst types. It was not repeated here.
3. **Different expected sets and one more document count.** 04 judged questions 4 and 9 as having no answering instrument in the corpus. The expected file now lists the nearest instruments (for question 4: ORS 276A.300(2), OAR 128-030-0020(1)(a)(O) and DAS policy 107-004-052; for question 9: ORS 276A.223(1)(a)(A) and the definition of "IT Investment" in 107-004-130), so those two questions are cells here. 04 used a limit of 6; this check uses 5.
4. **The semantic leg is new.** 04 could not run it (no torch in the environment, no artifact). It ran here on the machine's system Python with torch, against `_meta/embeddings` (BAAI/bge-m3, 18,044 chunks over 2,259 documents, from its `meta.json`; the artifact is not committed). Oregon hybrid: 18 of 19. 04's note that "inventory" does not find "registry" is the case the semantic leg is for: Oregon question 10 passes in the hybrid leg and fails in the keyword leg.

What carries over from 04: natural-language questions return nothing in the keyword leg (04: 13 of 20 first queries; here, Oregon cells with no keyword hit: see the per-question list), and the fix 04 asked for (a relaxed keyword fallback, or the hybrid leg) is what the hybrid column shows.

## Per question, all four states

Bold ids are expected documents. "Top" is the first 5 hits of `compare` for that state. "Missed" is the expected documents not among them.

### 1. To whom does the state CIO report: governor, agency head or board?

- **oregon**, expected: or-ors-276a. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-ors-276a**, or-open-data-standard, or-eo-23-26, or-das-107-004-130, or-das-107-004-160. Missed in the top 5: keyword or-ors-276a; hybrid none.
- **washington**, expected: wa-rcw-43-105. Keyword: PASS; top: **wa-rcw-43-105**. Hybrid: PASS; top: **wa-rcw-43-105**, wa-pol-01, wa-pol-01-02-s, wa-mgmt-03, wa-mgmt-02. Missed in the top 5: keyword none; hybrid none.
- **california**, expected: ca-gov-11545-11548. Keyword: fail; top: no hits. Hybrid: PASS; top: ca-sam-4800, ca-itpl-10-13, ca-itpl-09-05, ca-itpl-10-08, **ca-gov-11545-11548**. Missed in the top 5: keyword ca-gov-11545-11548; hybrid none.
- **colorado**, expected: co-crs-24-37-5. Keyword: fail; top: no hits. Hybrid: PASS; top: co-ccr-8-1501-5, **co-crs-24-37-5**, co-ccr-8-1501-7, co-ccr-8-1501-12, co-oit-ts-inf-003. Missed in the top 5: keyword co-crs-24-37-5; hybrid none.

### 2. Where does each state sit between decentralized and unified IT, and what has been consolidated (infrastructure, services, staff, project oversight)?

- **oregon**, expected: or-ors-276a, or-eis-memo-20220812-cloud, or-das-107-004-130, or-eis-memo-20241028-css-directive, or-das-107-004-052, or-oar-128-30. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-eis-memo-20241028-css-directive**, **or-ors-276a**, or-das-107-004-180, or-eis-it-control-standards, or-das-107-004-150. Missed in the top 5: keyword or-ors-276a, or-eis-memo-20220812-cloud, or-das-107-004-130, or-eis-memo-20241028-css-directive, or-das-107-004-052, or-oar-128-30; hybrid or-eis-memo-20220812-cloud, or-das-107-004-130, or-das-107-004-052, or-oar-128-30.
- **washington**, expected: wa-rcw-43-105, wa-ea-310, wa-ea-02. Keyword: fail; top: no hits. Hybrid: PASS; top: wa-eo-19-04, **wa-rcw-43-105**, wa-mgmt-01, wa-pol-01, wa-sec-04-03-s. Missed in the top 5: keyword wa-rcw-43-105, wa-ea-310, wa-ea-02; hybrid wa-ea-310, wa-ea-02.
- **california**, expected: ca-gov-11531-11544, ca-itpl-10-14, ca-gov-11545-11548, ca-sam-4900. Keyword: fail; top: no hits. Hybrid: PASS; top: ca-itpl-10-08, **ca-sam-4900**, ca-sam-4800, **ca-gov-11545-11548**, **ca-itpl-10-14**. Missed in the top 5: keyword ca-gov-11531-11544, ca-itpl-10-14, ca-gov-11545-11548, ca-sam-4900; hybrid ca-gov-11531-11544.
- **colorado**, expected: co-crs-24-37-5, co-ccr-8-1501-7, co-ccr-8-1501-5, co-oit-delegation-of-authority-policy. Keyword: fail; top: no hits. Hybrid: PASS; top: co-ccr-8-1501-12, **co-crs-24-37-5**, co-oit-genai-policy, co-oit-ts-ciso-012, co-oit-cisp-003. Missed in the top 5: keyword co-crs-24-37-5, co-ccr-8-1501-7, co-ccr-8-1501-5, co-oit-delegation-of-authority-policy; hybrid co-ccr-8-1501-7, co-ccr-8-1501-5, co-oit-delegation-of-authority-policy.

### 3. Is the state CISO's authority set by statute, rule, executive order, CIO directive or interagency agreement?

- **oregon**, expected: or-oar-128-30, or-ors-276a, or-oar-128-20, or-das-107-004-052. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-das-107-004-052**, **or-ors-276a**, **or-oar-128-20**, or-das-107-004-150, or-das-107-004-052-pr. Missed in the top 5: keyword or-oar-128-30, or-ors-276a, or-oar-128-20, or-das-107-004-052; hybrid or-oar-128-30.
- **washington**, expected: wa-rcw-43-105, wa-sec-01. Keyword: PASS; top: **wa-rcw-43-105**. Hybrid: PASS; top: **wa-rcw-43-105**, wa-pol-01, wa-pol-01-02-s, wa-sec-04-03-s, wa-sec-07. Missed in the top 5: keyword wa-sec-01; hybrid wa-sec-01.
- **california**, expected: ca-gov-11549-11549-10, ca-sam-5300, ca-eo-n-5-26. Keyword: fail; top: ca-sam-4800. Hybrid: PASS; top: ca-sam-4800, **ca-sam-5300**, ca-itpl-10-13, ca-simm-5330-h, ca-itpl-09-05. Missed in the top 5: keyword ca-gov-11549-11549-10, ca-sam-5300, ca-eo-n-5-26; hybrid ca-gov-11549-11549-10, ca-eo-n-5-26.
- **colorado**, expected: co-crs-24-37-5, co-ccr-8-1501-5. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-ccr-8-1501-5**, co-oit-delegation-of-authority-procedure, co-oit-ts-dbs-005, co-ccr-8-1501-7, **co-crs-24-37-5**. Missed in the top 5: keyword co-crs-24-37-5, co-ccr-8-1501-5; hybrid none.

### 4. Which states have a statute establishing the enterprise CISO role, and is it funded?

- **oregon**, expected: or-ors-276a, or-oar-128-30, or-das-107-004-052. Keyword: fail; top: no hits. Hybrid: PASS; top: or-oar-128-20, or-eis-memo-20241028-css-directive, or-das-107-004-150, **or-ors-276a**, or-das-107-004-150-pr. Missed in the top 5: keyword or-ors-276a, or-oar-128-30, or-das-107-004-052; hybrid or-oar-128-30, or-das-107-004-052.
- **washington**, expected: wa-rcw-43-105. Keyword: PASS; top: **wa-rcw-43-105**. Hybrid: PASS; top: **wa-rcw-43-105**, wa-ea-02, wa-ea-310, wa-pol-01, wa-ea-02-04-s. Missed in the top 5: keyword none; hybrid none.
- **california**, expected: ca-gov-11549-11549-10. Keyword: fail; top: ca-sam-4800. Hybrid: fail; top: ca-sam-4800, ca-sam-5300, ca-gov-11545-11548, ca-gov-8586-5, ca-tl-15-01. Missed in the top 5: keyword ca-gov-11549-11549-10; hybrid ca-gov-11549-11549-10.
- **colorado**, expected: co-crs-24-37-5. Keyword: fail; top: no hits. Hybrid: fail; top: co-ccr-8-1501-5, co-ccr-8-1501-7, co-oit-ts-dbs-014, co-oit-ts-dbs-005, co-oit-ts-inf-005. Missed in the top 5: keyword co-crs-24-37-5; hybrid co-crs-24-37-5.

### 5. Which government entities do state data-security statutes cover (executive agencies only, locals, contractors)?

- **oregon**, expected: or-ors-276a, or-oar-128-30, or-das-107-004-052. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-ors-276a**, **or-oar-128-30**, or-oar-128-20, or-das-107-004-155, or-das-107-004-110. Missed in the top 5: keyword or-ors-276a, or-oar-128-30, or-das-107-004-052; hybrid or-das-107-004-052.
- **washington**, expected: wa-rcw-43-105, wa-sec-01, wa-rcw-39-26-340, wa-rcw-42-56-590, wa-rcw-39-34-240. Keyword: fail; top: no hits. Hybrid: PASS; top: wa-ea-02-06-s, wa-ea-02-03-s, wa-data-03, wa-sec-08-01-s, **wa-rcw-43-105**. Missed in the top 5: keyword wa-rcw-43-105, wa-sec-01, wa-rcw-39-26-340, wa-rcw-42-56-590, wa-rcw-39-34-240; hybrid wa-sec-01, wa-rcw-39-26-340, wa-rcw-42-56-590, wa-rcw-39-34-240.
- **california**, expected: ca-gov-11549-11549-10, ca-gov-11545-11548, ca-sam-5300, ca-civ-1798-1798-78. Keyword: PASS; top: ca-simm-19b-1, **ca-civ-1798-1798-78**, ca-sam-4900. Hybrid: PASS; top: **ca-civ-1798-1798-78**, ca-sam-4900, ca-simm-19b-1, **ca-sam-5300**, **ca-gov-11545-11548**. Missed in the top 5: keyword ca-gov-11549-11549-10, ca-gov-11545-11548, ca-sam-5300; hybrid ca-gov-11549-11549-10.
- **colorado**, expected: co-crs-24-73, co-crs-24-74, co-crs-24-37-5, co-oit-cisp-003. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-crs-24-73**, **co-crs-24-37-5**, co-ccr-8-1501-5, co-oit-cisp-004, co-oit-ts-dbs-014. Missed in the top 5: keyword co-crs-24-73, co-crs-24-74, co-crs-24-37-5, co-oit-cisp-003; hybrid co-crs-24-74, co-oit-cisp-003.

### 6. Which states require agencies to run security training, periodic risk assessments or incident response plans?

- **oregon**, expected: or-ors-276a, or-das-107-004-120, or-das-107-004-052, or-oar-128-30, or-das-107-004-052-pr, or-eis-it-control-standards. Keyword: fail; top: or-eis-privacy-guidance. Hybrid: PASS; top: or-eis-privacy-guidance, **or-das-107-004-120**, **or-das-107-004-052**, **or-oar-128-30**, **or-das-107-004-052-pr**. Missed in the top 5: keyword or-ors-276a, or-das-107-004-120, or-das-107-004-052, or-oar-128-30, or-das-107-004-052-pr, or-eis-it-control-standards; hybrid or-ors-276a, or-eis-it-control-standards.
- **washington**, expected: wa-sec-03, wa-sec-10, wa-sec-11-01-s, wa-rcw-43-105. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-sec-11-01-s**, **wa-sec-03**, **wa-sec-10**, wa-sec-09-01-s, wa-sec-12. Missed in the top 5: keyword wa-sec-03, wa-sec-10, wa-sec-11-01-s, wa-rcw-43-105; hybrid wa-rcw-43-105.
- **california**, expected: ca-sam-5300, ca-simm-5340-a, ca-gov-11549-11549-10. Keyword: PASS; top: **ca-sam-5300**, ca-sam-4900, ca-simm-19a-1. Hybrid: PASS; top: **ca-sam-5300**, ca-sam-4900, ca-simm-19a-1, **ca-gov-11549-11549-10**, ca-tl-12-16. Missed in the top 5: keyword ca-simm-5340-a, ca-gov-11549-11549-10; hybrid ca-simm-5340-a.
- **colorado**, expected: co-crs-24-37-5, co-oit-cisp-002, co-oit-cisp-001, co-oit-cisp-003, co-ccr-8-1501-5. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-crs-24-37-5**, **co-oit-cisp-003**, co-oit-ts-ciso-002, **co-ccr-8-1501-5**, **co-oit-cisp-001**. Missed in the top 5: keyword co-crs-24-37-5, co-oit-cisp-002, co-oit-cisp-001, co-oit-cisp-003, co-ccr-8-1501-5; hybrid co-oit-cisp-002.

### 7. Must the CIO approve agency cloud acquisitions, and is a pre-acquisition security review required?

- **oregon**, expected: or-das-107-004-150, or-das-107-004-150-pr, or-das-107-004-130, or-eis-memo-20220812-cloud. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-das-107-004-150**, **or-das-107-004-150-pr**, or-oar-128-20, **or-eis-memo-20220812-cloud**, or-eis-memo-20241028-css-directive. Missed in the top 5: keyword or-das-107-004-150, or-das-107-004-150-pr, or-das-107-004-130, or-eis-memo-20220812-cloud; hybrid or-das-107-004-130.
- **washington**, expected: wa-rcw-43-105, wa-sec-02, wa-sec-11-01-s. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-sec-11-01-s**, wa-ea-310, **wa-sec-02**, wa-ea-122, wa-sec-09. Missed in the top 5: keyword wa-rcw-43-105, wa-sec-02, wa-sec-11-01-s; hybrid wa-rcw-43-105.
- **california**, expected: ca-tl-23-03, ca-sam-4900, ca-simm-141. Keyword: fail; top: no hits. Hybrid: fail; top: ca-simm-71a, ca-sam-5200, ca-simm-22a, ca-simm-18b, ca-sam-4800. Missed in the top 5: keyword ca-tl-23-03, ca-sam-4900, ca-simm-141; hybrid ca-tl-23-03, ca-sam-4900, ca-simm-141.
- **colorado**, expected: co-crs-24-37-5, co-oit-cisp-003. Keyword: fail; top: no hits. Hybrid: PASS; top: co-oit-ts-dbs-014, co-oit-ts-dat-001, co-oit-ts-ciso-012, co-ccr-8-1501-12, **co-crs-24-37-5**. Missed in the top 5: keyword co-crs-24-37-5, co-oit-cisp-003; hybrid co-oit-cisp-003.

### 8. How is the central IT organization funded: chargeback, general fund, assessment or hybrid?

- **oregon**, expected: or-ors-276a. Keyword: fail; top: no hits. Hybrid: fail; top: or-das-107-004-130-pr, or-das-107-004-010, or-das-107-004-150, or-das-107-004-180, or-das-107-004-130. Missed in the top 5: keyword or-ors-276a; hybrid or-ors-276a.
- **washington**, expected: wa-rcw-43-105. Keyword: fail; top: no hits. Hybrid: fail; top: wa-mgmt-01, wa-mgmt-02, wa-mgmt-01-03-s, wa-pm-01-05-s, wa-mgmt-02-01-s. Missed in the top 5: keyword wa-rcw-43-105; hybrid wa-rcw-43-105.
- **california**, expected: ca-gov-11531-11544. Keyword: fail; top: no hits. Hybrid: fail; top: ca-simm-19a-1, ca-sam-4900, ca-simm-55a, ca-itpl-11-03, ca-simm-55d. Missed in the top 5: keyword ca-gov-11531-11544; hybrid ca-gov-11531-11544.
- **colorado**, expected: co-crs-24-37-5, co-oit-real-time-billing-dispute-policy. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-crs-24-37-5**, co-ccr-8-1501-12, co-oit-change-management-policy, co-oit-real-time-billing-dispute-procedure, co-oit-ts-ciso-012. Missed in the top 5: keyword co-crs-24-37-5, co-oit-real-time-billing-dispute-policy; hybrid co-oit-real-time-billing-dispute-policy.

### 9. How does each state define an "information technology procurement"?

- **oregon**, expected: or-ors-276a, or-das-107-004-130. Keyword: PASS; top: or-das-107-004-150, or-eis-privacy-guidance, **or-ors-276a**, or-das-107-004-130-pr, or-open-data-standard. Hybrid: PASS; top: **or-ors-276a**, or-das-107-004-130-pr, or-eis-it-control-standards, or-das-107-004-150, or-eis-privacy-guidance. Missed in the top 5: keyword or-das-107-004-130; hybrid or-das-107-004-130.
- **washington**, expected: wa-pm-01. Keyword: fail; top: wa-watech-ads-procurement-guidance, wa-watech-genai-procurement-guidelines, wa-watech-genai-deployment-guidelines, wa-sec-11-01-g, wa-ea-01-03-s. Hybrid: fail; top: wa-rcw-43-105, wa-watech-genai-procurement-guidelines, wa-sec-11-01-g, wa-pm-01-02-s, wa-watech-ads-procurement-guidance. Missed in the top 5: keyword wa-pm-01; hybrid wa-pm-01.
- **california**, expected: ca-sam-4800, ca-pcc-12100-12113. Keyword: fail; top: ca-simm-180, ca-simm-19b-1, ca-simm-19d-1, ca-simm-120, ca-simm-19e-1. Hybrid: PASS; top: ca-simm-71a, **ca-sam-4800**, ca-sam-4900, ca-simm-19e-1, ca-gov-11545-11548. Missed in the top 5: keyword ca-sam-4800, ca-pcc-12100-12113; hybrid ca-pcc-12100-12113.
- **colorado**, expected: co-crs-24-37-5. Keyword: PASS; top: co-ccr-8-1501-11, co-ccr-8-1501-7, **co-crs-24-37-5**. Hybrid: PASS; top: **co-crs-24-37-5**, co-ccr-8-1501-11, co-ccr-8-1501-7, co-ccr-8-1501-12, co-crs-24-85. Missed in the top 5: keyword none; hybrid none.

### 10. Which states require an inventory of agency AI systems; all uses or high-risk only; how often updated; published?

- **oregon**, expected: or-das-107-004-190, or-eis-ai-attachment-a. Keyword: fail; top: no hits. Hybrid: PASS; top: or-eis-ai-attachment-g, **or-das-107-004-190**, or-eis-ai-attachment-b, or-eis-ai-attachment-d, **or-eis-ai-attachment-a**. Missed in the top 5: keyword or-das-107-004-190, or-eis-ai-attachment-a; hybrid none.
- **washington**, expected: wa-data-04, wa-watech-ads-procurement-guidance, wa-mgmt-01. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-data-04**, wa-watech-ai-risk-assessments, wa-eo-24-01, wa-sec-04, wa-watech-ai-risk-level-guidance. Missed in the top 5: keyword wa-data-04, wa-watech-ads-procurement-guidance, wa-mgmt-01; hybrid wa-watech-ads-procurement-guidance, wa-mgmt-01.
- **california**, expected: ca-sam-4900, ca-tl-25-01, ca-eo-n-12-23, ca-tl-24-01, ca-genai-guidelines, ca-gov-11545-11548. Keyword: PASS; top: **ca-sam-4900**. Hybrid: PASS; top: **ca-sam-4900**, **ca-tl-24-01**, **ca-eo-n-12-23**, ca-simm-5305-f, ca-sam-5300. Missed in the top 5: keyword ca-tl-25-01, ca-eo-n-12-23, ca-tl-24-01, ca-genai-guidelines, ca-gov-11545-11548; hybrid ca-tl-25-01, ca-genai-guidelines, ca-gov-11545-11548.
- **colorado**, expected: none (a `none_reason` in `_meta/eval/expected/colorado.yml`; no cell). Keyword top: no hits. Hybrid top: co-ccr-8-1501-12, co-oit-genai-policy, co-oit-cisp-001, co-ccr-8-1501-5, co-crs-24-37-5.

### 11. Which states require impact assessments before agencies deploy AI, and who reviews them?

- **oregon**, expected: or-das-107-004-190-pr, or-eis-ai-attachment-b, or-eis-ai-attachment-g, or-eis-ai-attachment-a, or-das-107-004-190. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-eis-ai-attachment-b**, **or-das-107-004-190**, **or-eis-ai-attachment-a**, **or-eis-ai-attachment-g**, or-eo-26-26. Missed in the top 5: keyword or-das-107-004-190-pr, or-eis-ai-attachment-b, or-eis-ai-attachment-g, or-eis-ai-attachment-a, or-das-107-004-190; hybrid or-das-107-004-190-pr.
- **washington**, expected: wa-data-04, wa-eo-24-01, wa-watech-ai-risk-assessments, wa-watech-genai-procurement-guidelines. Keyword: PASS; top: wa-watech-genai-deployment-guidelines, **wa-watech-genai-procurement-guidelines**, **wa-watech-ai-risk-assessments**, wa-watech-ads-procurement-guidance, wa-rcw-43-105. Hybrid: PASS; top: **wa-watech-ai-risk-assessments**, **wa-watech-genai-procurement-guidelines**, wa-watech-genai-deployment-guidelines, wa-watech-ads-procurement-guidance, wa-rcw-43-105. Missed in the top 5: keyword wa-data-04, wa-eo-24-01; hybrid wa-data-04, wa-eo-24-01.
- **california**, expected: ca-sam-4900, ca-simm-5305-f, ca-tl-24-01, ca-eo-n-12-23, ca-simm-5310-c, ca-simm-150, ca-tl-24-03. Keyword: PASS; top: ca-genai-guidelines, **ca-simm-5305-f**, ca-gov-11545-11548, **ca-sam-4900**, ca-sam-4800. Hybrid: PASS; top: **ca-simm-5305-f**, **ca-sam-4900**, ca-gov-11545-11548, ca-genai-guidelines, ca-sam-4800. Missed in the top 5: keyword ca-tl-24-01, ca-eo-n-12-23, ca-simm-5310-c, ca-simm-150, ca-tl-24-03; hybrid ca-tl-24-01, ca-eo-n-12-23, ca-simm-5310-c, ca-simm-150, ca-tl-24-03.
- **colorado**, expected: co-oit-genai-policy. Keyword: fail; top: no hits. Hybrid: PASS; top: co-crs-2-3-pt17, **co-oit-genai-policy**, co-crs-24-37-5, co-oit-delegation-of-authority-procedure, co-oit-cisp-001. Missed in the top 5: keyword co-oit-genai-policy; hybrid none.

### 12. How does each state's instrument define "artificial intelligence", and does it borrow the federal definition?

- **oregon**, expected: or-ors-276a, or-oar-128-20, or-das-107-004-190, or-das-107-004-155, or-das-107-004-200. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-das-107-004-190**, **or-ors-276a**, or-eo-26-26, or-eis-ai-attachment-b, or-eo-23-26. Missed in the top 5: keyword or-ors-276a, or-oar-128-20, or-das-107-004-190, or-das-107-004-155, or-das-107-004-200; hybrid or-oar-128-20, or-das-107-004-155, or-das-107-004-200.
- **washington**, expected: wa-data-04, wa-eo-24-01, wa-watech-ai-risk-level-guidance, wa-watech-ads-procurement-guidance. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-data-04**, **wa-eo-24-01**, wa-watech-genai-procurement-guidelines, wa-watech-genai-accountability-framework, wa-watech-ai-risk-assessments. Missed in the top 5: keyword wa-data-04, wa-eo-24-01, wa-watech-ai-risk-level-guidance, wa-watech-ads-procurement-guidance; hybrid wa-watech-ai-risk-level-guidance, wa-watech-ads-procurement-guidance.
- **california**, expected: ca-gov-11549-63-11549-66, ca-sam-4800, ca-genai-guidelines, ca-gov-11545-11548. Keyword: fail; top: no hits. Hybrid: PASS; top: ca-sam-4900, **ca-gov-11549-63-11549-66**, ca-simm-150, **ca-sam-4800**, ca-eo-n-5-26. Missed in the top 5: keyword ca-gov-11549-63-11549-66, ca-sam-4800, ca-genai-guidelines, ca-gov-11545-11548; hybrid ca-genai-guidelines, ca-gov-11545-11548.
- **colorado**, expected: co-crs-2-3-pt17, co-oit-genai-policy. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-crs-2-3-pt17**, **co-oit-genai-policy**, co-ccr-8-1501-12, co-oit-ts-oea-001, co-crs-24-37-5. Missed in the top 5: keyword co-crs-2-3-pt17, co-oit-genai-policy; hybrid none.

### 13. What body governs state AI use (task force, council, office, chief AI officer), who sits on it, and is it advisory or binding?

- **oregon**, expected: or-das-107-004-190, or-eo-23-26. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-eo-23-26**, or-eis-ai-attachment-a, **or-das-107-004-190**, or-eis-ai-attachment-b, or-eo-26-26. Missed in the top 5: keyword or-das-107-004-190, or-eo-23-26; hybrid none.
- **washington**, expected: wa-data-04, wa-watech-ai-risk-assessments, wa-eo-24-01. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-data-04**, **wa-eo-24-01**, wa-watech-genai-accountability-framework, wa-pol-01, wa-watech-genai-procurement-guidelines. Missed in the top 5: keyword wa-data-04, wa-watech-ai-risk-assessments, wa-eo-24-01; hybrid wa-watech-ai-risk-assessments.
- **california**, expected: ca-gov-11549-63-11549-66, ca-sam-4900, ca-eo-n-12-23, ca-genai-guidelines, ca-eo-n-5-26. Keyword: fail; top: no hits. Hybrid: PASS; top: **ca-sam-4900**, **ca-eo-n-12-23**, **ca-eo-n-5-26**, **ca-gov-11549-63-11549-66**, ca-gov-11545-11548. Missed in the top 5: keyword ca-gov-11549-63-11549-66, ca-sam-4900, ca-eo-n-12-23, ca-genai-guidelines, ca-eo-n-5-26; hybrid ca-genai-guidelines.
- **colorado**, expected: co-oit-genai-policy, co-crs-2-3-pt17. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-crs-2-3-pt17**, **co-oit-genai-policy**, co-crs-24-37-5, co-oit-delegation-of-authority-policy, co-oit-delegation-of-authority-procedure. Missed in the top 5: keyword co-oit-genai-policy, co-crs-2-3-pt17; hybrid none.

### 14. Is the state's AI policy set by statute, executive order, rule or CIO guideline?

- **oregon**, expected: or-das-107-004-190, or-eo-26-26, or-eo-23-26, or-ors-276a, or-oar-128-20. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-eo-26-26**, **or-das-107-004-190**, **or-eo-23-26**, or-das-107-004-200, or-eis-ai-attachment-a. Missed in the top 5: keyword or-das-107-004-190, or-eo-26-26, or-eo-23-26, or-ors-276a, or-oar-128-20; hybrid or-ors-276a, or-oar-128-20.
- **washington**, expected: wa-eo-24-01, wa-data-04, wa-rcw-43-105. Keyword: PASS; top: **wa-rcw-43-105**. Hybrid: PASS; top: **wa-rcw-43-105**, wa-pol-01, **wa-data-04**, **wa-eo-24-01**, wa-pol-01-02-s. Missed in the top 5: keyword wa-eo-24-01, wa-data-04; hybrid none.
- **california**, expected: ca-gov-11549-63-11549-66, ca-eo-n-12-23, ca-sam-4900, ca-tl-25-01. Keyword: PASS; top: **ca-sam-4900**, ca-sam-4800, ca-gov-11545-11548. Hybrid: PASS; top: **ca-sam-4900**, ca-sam-4800, ca-gov-11545-11548, **ca-tl-25-01**, ca-sam-5300. Missed in the top 5: keyword ca-gov-11549-63-11549-66, ca-eo-n-12-23, ca-tl-25-01; hybrid ca-gov-11549-63-11549-66, ca-eo-n-12-23.
- **colorado**, expected: co-oit-genai-policy, co-crs-2-3-pt17. Keyword: fail; top: no hits. Hybrid: PASS; top: co-oit-ts-dbs-014, **co-oit-genai-policy**, co-ccr-8-1501-7, co-ccr-8-1501-5, co-ccr-8-1501-12. Missed in the top 5: keyword co-oit-genai-policy, co-crs-2-3-pt17; hybrid co-crs-2-3-pt17.

### 15. Which states impose AI-specific procurement terms or vendor disclosure duties?

- **oregon**, expected: or-eis-ai-attachment-g, or-eo-26-26, or-eis-ai-attachment-b, or-ors-276a, or-oar-128-20, or-das-107-004-155. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-eo-26-26**, **or-eis-ai-attachment-b**, or-eis-ai-attachment-d, **or-eis-ai-attachment-g**, or-das-107-004-190. Missed in the top 5: keyword or-eis-ai-attachment-g, or-eo-26-26, or-eis-ai-attachment-b, or-ors-276a, or-oar-128-20, or-das-107-004-155; hybrid or-ors-276a, or-oar-128-20, or-das-107-004-155.
- **washington**, expected: wa-data-04, wa-des-genai-contract-clauses, wa-eo-24-01, wa-watech-genai-procurement-guidelines. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-watech-genai-procurement-guidelines**, **wa-data-04**, **wa-des-genai-contract-clauses**, **wa-eo-24-01**, wa-watech-ai-risk-assessments. Missed in the top 5: keyword wa-data-04, wa-des-genai-contract-clauses, wa-eo-24-01, wa-watech-genai-procurement-guidelines; hybrid none.
- **california**, expected: ca-sam-4900, ca-genai-guidelines, ca-tl-24-01, ca-eo-n-5-26, ca-gov-8586-5. Keyword: fail; top: no hits. Hybrid: PASS; top: **ca-eo-n-5-26**, **ca-sam-4900**, ca-simm-71a, **ca-genai-guidelines**, **ca-tl-24-01**. Missed in the top 5: keyword ca-sam-4900, ca-genai-guidelines, ca-tl-24-01, ca-eo-n-5-26, ca-gov-8586-5; hybrid ca-gov-8586-5.
- **colorado**, expected: co-oit-genai-policy. Keyword: fail; top: no hits. Hybrid: PASS; top: co-crs-24-85, **co-oit-genai-policy**, co-oit-ts-dbs-014, co-crs-2-3-pt17, co-crs-24-37-5. Missed in the top 5: keyword co-oit-genai-policy; hybrid none.

### 16. Which states restrict AI-only adverse decisions (for example benefit cuts or fraud findings) or require public disclosure of AI use?

- **oregon**, expected: or-eis-ai-attachment-b, or-eis-ai-attachment-d, or-das-107-004-190, or-eis-ai-attachment-g, or-eis-ai-attachment-f. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-das-107-004-190**, **or-eis-ai-attachment-g**, **or-eis-ai-attachment-b**, **or-eis-ai-attachment-d**, or-eis-memo-20250212-deepseek. Missed in the top 5: keyword or-eis-ai-attachment-b, or-eis-ai-attachment-d, or-das-107-004-190, or-eis-ai-attachment-g, or-eis-ai-attachment-f; hybrid or-eis-ai-attachment-f.
- **washington**, expected: wa-data-04, wa-watech-genai-procurement-guidelines, wa-watech-ads-procurement-guidance. Keyword: fail; top: no hits. Hybrid: PASS; top: wa-watech-ai-risk-assessments, **wa-watech-genai-procurement-guidelines**, wa-watech-genai-accountability-framework, **wa-data-04**, wa-watech-genai-deployment-guidelines. Missed in the top 5: keyword wa-data-04, wa-watech-genai-procurement-guidelines, wa-watech-ads-procurement-guidance; hybrid wa-watech-ads-procurement-guidance.
- **california**, expected: ca-gov-11549-63-11549-66, ca-sam-4900, ca-simm-5305-f. Keyword: fail; top: no hits. Hybrid: PASS; top: **ca-gov-11549-63-11549-66**, **ca-simm-5305-f**, ca-eo-n-6-26, **ca-sam-4900**, ca-eo-n-5-26. Missed in the top 5: keyword ca-gov-11549-63-11549-66, ca-sam-4900, ca-simm-5305-f; hybrid none.
- **colorado**, expected: co-oit-genai-policy. Keyword: fail; top: no hits. Hybrid: PASS; top: co-oit-cisp-001, co-crs-2-3-pt17, **co-oit-genai-policy**, co-crs-24-74, co-crs-24-37-5. Missed in the top 5: keyword co-oit-genai-policy; hybrid none.

### 17. Which states have a technology accessibility coordinator and how do they verify vendor compliance?

- **oregon**, expected: none (a `none_reason` in `_meta/eval/expected/oregon.yml`; no cell). Keyword top: or-eis-privacy-guidance, or-eis-it-control-standards. Hybrid top: or-eis-it-control-standards, or-eis-privacy-guidance, or-oar-128-20, or-eo-26-26, or-das-107-004-155.
- **washington**, expected: wa-user-01, wa-user-01-01-s. Keyword: fail; top: wa-sec-11-01-g. Hybrid: PASS; top: wa-sec-11-01-g, **wa-user-01-01-s**, **wa-user-01**, wa-ea-02-07-s, wa-pol-01-02-s. Missed in the top 5: keyword wa-user-01, wa-user-01-01-s; hybrid none.
- **california**, expected: ca-simm-25a, ca-gov-7405, ca-sam-4800, ca-itpl-10-10, ca-gov-11545-11548, ca-tl-18-05. Keyword: fail; top: ca-simm-170b, ca-simm-5305-f, ca-simm-170a, ca-simm-5310-c, ca-simm-120. Hybrid: PASS; top: **ca-sam-4800**, ca-sam-4900, ca-simm-120, ca-simm-170b, ca-simm-5340-c. Missed in the top 5: keyword ca-simm-25a, ca-gov-7405, ca-sam-4800, ca-itpl-10-10, ca-gov-11545-11548, ca-tl-18-05; hybrid ca-simm-25a, ca-gov-7405, ca-itpl-10-10, ca-gov-11545-11548, ca-tl-18-05.
- **colorado**, expected: co-crs-24-85, co-oit-ts-oea-001, co-ccr-8-1501-11. Keyword: fail; top: no hits. Hybrid: PASS; top: **co-ccr-8-1501-11**, **co-oit-ts-oea-001**, **co-crs-24-85**, co-oit-ts-inf-003, co-crs-2-3-pt17. Missed in the top 5: keyword co-crs-24-85, co-oit-ts-oea-001, co-ccr-8-1501-11; hybrid none.

### 18. Is disaster recovery centralized, federated or left to agencies?

- **oregon**, expected: or-das-107-004-150, or-eis-it-control-standards. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-das-107-004-150**, **or-eis-it-control-standards**, or-das-107-004-160, or-das-107-004-120, or-ors-276a. Missed in the top 5: keyword or-das-107-004-150, or-eis-it-control-standards; hybrid none.
- **washington**, expected: wa-sec-12, wa-sec-04-01-s, wa-rcw-43-105. Keyword: fail; top: no hits. Hybrid: PASS; top: wa-mgmt-01-01-s, **wa-sec-04-01-s**, **wa-sec-12**, **wa-rcw-43-105**, wa-sec-10. Missed in the top 5: keyword wa-sec-12, wa-sec-04-01-s, wa-rcw-43-105; hybrid none.
- **california**, expected: ca-sam-5300, ca-gov-11549-11549-10, ca-tl-18-03, ca-gov-8592-30-8592-50, ca-simm-5325-a. Keyword: fail; top: ca-simm-19a-1, ca-sam-4800. Hybrid: PASS; top: ca-simm-19a-1, ca-sam-4800, ca-itpl-10-14, **ca-simm-5325-a**, ca-tl-12-04. Missed in the top 5: keyword ca-sam-5300, ca-gov-11549-11549-10, ca-tl-18-03, ca-gov-8592-30-8592-50, ca-simm-5325-a; hybrid ca-sam-5300, ca-gov-11549-11549-10, ca-tl-18-03, ca-gov-8592-30-8592-50.
- **colorado**, expected: co-ccr-8-1501-5, co-crs-24-37-5, co-oit-cisp-002. Keyword: fail; top: no hits. Hybrid: PASS; top: co-oit-genai-policy, co-ccr-8-1501-12, **co-ccr-8-1501-5**, co-oit-ts-dbs-005, co-oit-ts-dbs-014. Missed in the top 5: keyword co-ccr-8-1501-5, co-crs-24-37-5, co-oit-cisp-002; hybrid co-crs-24-37-5, co-oit-cisp-002.

### 19. What cybersecurity or IT services does the state provide to local governments (whole-of-state)?

- **oregon**, expected: or-ors-276a, or-oar-128-30, or-das-107-004-120. Keyword: fail; top: no hits. Hybrid: PASS; top: **or-ors-276a**, or-das-107-004-052, **or-oar-128-30**, or-eis-it-control-standards, or-eis-memo-20241028-css-directive. Missed in the top 5: keyword or-ors-276a, or-oar-128-30, or-das-107-004-120; hybrid or-das-107-004-120.
- **washington**, expected: wa-rcw-43-105. Keyword: fail; top: no hits. Hybrid: PASS; top: **wa-rcw-43-105**, wa-sec-01, wa-ea-02-03-s, wa-eo-19-04, wa-pol-01. Missed in the top 5: keyword wa-rcw-43-105; hybrid none.
- **california**, expected: ca-gov-8586-5, ca-gov-11549-11549-10, ca-gov-11531-11544, ca-gov-8592-30-8592-50, ca-eo-b-34-15, ca-pcc-12100-12113. Keyword: fail; top: no hits. Hybrid: PASS; top: **ca-gov-8586-5**, **ca-gov-8592-30-8592-50**, ca-sam-5300, **ca-eo-b-34-15**, ca-gov-11545-11548. Missed in the top 5: keyword ca-gov-8586-5, ca-gov-11549-11549-10, ca-gov-11531-11544, ca-gov-8592-30-8592-50, ca-eo-b-34-15, ca-pcc-12100-12113; hybrid ca-gov-11549-11549-10, ca-gov-11531-11544, ca-pcc-12100-12113.
- **colorado**, expected: co-crs-24-33-5-pt19, co-crs-24-37-5, co-crs-24-37-7. Keyword: fail; top: no hits. Hybrid: PASS; top: co-ccr-8-1501-5, co-oit-cisp-003, **co-crs-24-33-5-pt19**, **co-crs-24-37-5**, co-ccr-8-1501-12. Missed in the top 5: keyword co-crs-24-33-5-pt19, co-crs-24-37-5, co-crs-24-37-7; hybrid co-crs-24-37-7.

### 20. Which states require or accept GovRAMP authorization for cloud purchases?

- **oregon**, expected: or-das-107-004-150, or-eis-ai-attachment-g. Keyword: fail; top: no hits. Hybrid: PASS; top: or-eis-memo-20220812-cloud, or-das-107-004-150-pr, or-eis-it-control-standards, or-eo-26-26, **or-das-107-004-150**. Missed in the top 5: keyword or-das-107-004-150, or-eis-ai-attachment-g; hybrid or-eis-ai-attachment-g.
- **washington**, expected: none (a `none_reason` in `_meta/eval/expected/washington.yml`; no cell). Keyword top: no hits. Hybrid top: wa-rcw-43-105, wa-ea-310, wa-data-01-03-g, wa-ea-122, wa-ea-03-01-s.
- **california**, expected: ca-sam-4900. Keyword: fail; top: no hits. Hybrid: PASS; top: ca-sam-4800, ca-simm-5315-b, ca-sam-5200, **ca-sam-4900**, ca-simm-18b. Missed in the top 5: keyword ca-sam-4900; hybrid none.
- **colorado**, expected: none (a `none_reason` in `_meta/eval/expected/colorado.yml`; no cell). Keyword top: no hits. Hybrid top: co-ccr-8-1501-9, co-oit-cisp-001, co-oit-ts-dat-001, co-crs-24-37-5, co-ccr-8-1501-5.


## The check

`src/eval_questions.py` (tests in `tests/test_eval_questions.py`; 35 tests, each failure mode proved by a test: a broken quote, an unknown id, a stub id, a missing question, a regressed cell, a stale baseline, and a low pass rate that must NOT fail).

- `--check` (in `scripts/gates.sh` and the `generated` job of `ci.yml`): validates the expected files, requires `_meta/eval/baseline.json` to match the questions and the expected document ids, runs the keyword leg with the pinned toolkit (no embedder), and fails if a cell that passes in the baseline no longer does.
- `--write-baseline`: writes the baseline from the tool's own keyword run. It is not part of `scripts/regen.sh` on purpose: a regenerated baseline would accept a regression silently. A deliberate change to the expected files or questions is followed by `--write-baseline`, and the diff of `baseline.json` is the review.
- `--report [--json FILE]`: both legs, with the hybrid leg only when `_meta/embeddings` is present and the embedder loads. Run it as `PYTHONPATH=<toolkit v1.37.1 source> /usr/bin/python3 src/eval_questions.py --report` where torch is installed.

The pilot's recorded rate (spec "Done" 1) is therefore: keyword leg **12/76 (16%)** in `_meta/eval/baseline.json`, hybrid leg **69/76 (91%)** in this write-up (not gated).

## Seed-list gaps the lists revealed

Two kinds, both from the `none_reason` entries and the seed files (`_meta/sources/<state>.yml`), not from a search for new instruments. I fetched nothing from any state site, so "absent at the source" is not established for any item.

**A question with no answering instrument among the documents held (the expected file's `none_reason`):**

1. **Oregon question 17** (technology accessibility coordinator, vendor verification): `none_reason` says no Oregon instrument names a coordinator or a vendor verification process, and "Oregon seeds no accessibility instrument". Whether Oregon has one is not known; 04 reached the same point and did not research it either.
2. **Colorado question 10** (AI system inventory): the `none_reason` finds only inventories of IT assets and contracts, none of AI systems; the generative AI policy requires OIT intake but sets no inventory, update frequency or publication.
3. **Colorado question 20** (GovRAMP or FedRAMP authorization for cloud purchases): none of the cloud provisions read requires or accepts either; the corpus holds no Colorado executive order and no cloud security policy.
4. **Washington question 20**: no match for GovRAMP, StateRAMP or FedRAMP in any Washington document; the cloud provisions read name no authorization program.

For 2 to 4, "no provision" may be the true answer for that state rather than a gap; the corpus cannot tell the two apart without the official sources being checked.

**A question whose candidate answering instrument is a stub (a seed entry with no text; relevance is judged from the seed entry's title and `why_relevant`, which is UNVERIFIED because the text is not held):**

- **Oregon `or-eo-16-13`** (Executive Order 16-13, Unifying Cyber Security in Oregon): the seed entry says it "Directs the transfer of executive department IT security functions to the Office of the State CIO". Questions 2 and 3 ask about consolidation and the basis of the CISO's authority. It is a stub because a scan's two-engine OCR did not reach the 90% bar on figures (its `stub_reason`). It is Oregon's only stub.
- **Washington `wa-law-2026-c167`** (Laws of 2026, ch. 167, section 6, enacted but not in force until 2027-02-01) and **`wa-rcw-43-386`** (facial recognition; borderline for scope, owner decision): candidates for question 16 (public disclosure of AI use; human review). The Washington question 16 cell lists other documents (`wa-data-04`, two WaTech procurement guidelines).
- **Colorado `co-crs-24-18-pt3`** (state agency use of facial recognition; borderline for scope, owner decision): a candidate for question 16; the expected document is the generative AI policy.
- **Washington `wa-watech-genai-interim-guidelines`**: the published link returns 404; a candidate for the AI-policy questions. Not shown as withdrawn.
- **California**: 67 of 246 seed entries are stubs, most with reasons that name forms, templates, spreadsheets or sample exhibits (17 read "form or template: a fill-in document, not an instrument's text"), 7 "no official text could be fetched" and 1 "not public" (e.g. SIMM 25B Website Accessibility Certificate Template for question 17; SIMM 5325-B Technology Recovery Program Certification for question 18; SIMM 22B COTS/SaaS Acquisition Information Form for question 7). For the forms, these are what the instruments call for rather than the instruments, so I count them as a coverage fact, not a gap in the answers; every California question has expected documents.

No seed-list entry was changed. Whether the borderline-scope stubs (Washington and Colorado facial recognition) become documents, and whether to seed accessibility instruments for Oregon, are the owner's calls; question 16 has an expected document in each state, so the check does not wait on them.

## What was not measured

- **Whether the expected lists are complete.** A pass means an expected document came back; it does not show that the best answering document is expected, or that no other instrument answers the question. The lists were written by agents from the committed documents and each quote re-found by the tool, which proves the quote is in the document, not that the list is exhaustive.
- **Passage quality.** The cell is document-level. It does not check that the returned passage is the quoted one (hybrid hits carry a chunk heading and preview; the check ignores them).
- **The informed-query ceiling.** No reworded or reduced queries were run, so this write-up does not show what a careful keyword user would get.
- **Other states.** Only the four pilot states are in the check. The other states in `_meta/sources/` have no expected lists.
- **Stability of the hybrid leg.** One run of one embedding model (BAAI/bge-m3), no repeat, no other model; and whether `_meta/embeddings` was built from the current text of every document was not checked (its `meta.json` count of 2,259 documents equals the number of document files, which is all that was compared).
- **Vaquill outside baseline** (spec "Done" 2) and **`coverage`'s stub share** (spec "Done" 3) are not part of this work.
- **Whether the corpus ships the hybrid configuration.** It does not. The hybrid leg turns the semantic module on in code (`src/eval_questions.py` sets `semantic_search_module` to `corpus_toolkit.semantic.search`); `_meta/corpus.yml` configures none, so the served `compare` tool, whose default mode is hybrid, falls back to keyword search today and an analyst would get the keyword-leg result, not the hybrid one. Turning it on needs a `corpus.yml` setting and a deployed index (owner decision).
- **The hybrid leg in the gate.** It is not gated: CI has no torch and no embeddings. A gate for it would have to run on the deploy box or the GPU machine (owner decision).

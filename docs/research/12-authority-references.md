# 12. Authority references: what the documents we hold say enables them

Status: 2026-11-12, branch `research/authority-references`. **Every instrument named below as missing is UNVERIFIED**: this pass fetched nothing, read no cited instrument, and changed no document, snapshot or seed file. Each line is a candidate for the owner to approve or decline before any fetch. Generated figures come from `_meta/eval/authority-refs.json` (`python3 src/authority_refs.py`; `--table` prints the per-state table).

**Update, same day, after rebasing onto `main`:** the figures and lists in this note were computed at 2,259 documents. PR #65 then turned seven Oklahoma statute stubs into documents (2,266 documents), and `_meta/eval/authority-refs.json` was regenerated for that. The note was not recomputed. The only entry it changes is Oklahoma's "new evidence" item: 62 O.S. 34.11.2 to 34.31.2, 35.1 to 35.8 and 74 O.S. 3113.1 are now held; 34.11.1, 34.32, 35.9 and 36 are still not held because the only official text is not in force until 2027-01-01.

## The idea and the method

Policies and standards cite the rules and statutes that enable them, and rules cite statutes. Reading every document we hold for the instruments it cites, and comparing them with what we hold, finds missing material without any search. Before this pass `_meta/graph.json` had 2,259 nodes and no edges: nobody had read the documents for what they cite.

`src/authority_refs.py` reads the "Full text" of all 2,259 documents from 42 states and extracts the citations each makes to **its own state's** statutes, administrative rules and executive orders, in the forms that state's documents print (`src/authority_forms.py`, one table per state). Each citation is resolved against the state's seed file (`_meta/sources/<state>.yml`):

- **HELD**: a held document's own citation, its section headings, a renumbering the held documents themselves print, or a chapter held section by section covers it.
- **STUB**: a seed entry with `stub: true` covers it (no document yet).
- **LEFT OUT**: the seed's `left_out` record names it; the recorded reason is kept.
- **NOT HELD**: none of the above. These are the candidates.

Federal citations (U.S.C., C.F.R., NIST, FIPS, FedRAMP, Pub. L.) are counted and never candidates. A citation inside a history note (a statute's "Source:" line, "Formerly ...", a revision-history row, a rule's bracketed history line) is counted separately and is not read as enabling authority. A statute that cites a range containing its own section ("As used in K.S.A. 75-7201 through 75-7212") is not a citation of another instrument.

### What this pass changed in the tool, after an independent review

An independent review of the first version read documents in every state against the tool's output and found false HELDs, wrong NOT HELDs and whole forms the table could not see. Each confirmed finding was fixed test-first (`tests/test_authority_refs_review.py`, every sample a verbatim line of a committed document) and the JSON regenerated:

- Delaware: a History line ("73 Del. Laws, c. 86") was read as a section heading, so the held 29 Del. C. chapter 90C covered every Title 29 section from 74 to 9047C. Headings now come from lines that open with the section sign and are kept to the held chapter. 29 Del. C. 502 is NOT HELD.
- Renumbering is read from the held documents' own history lines (Iowa "C2014, §8B.21" is held 8.77; Oregon "[Formerly 182.122]" is held 276A.300) and from three recorded tables (Maryland 3A-3nn is held 3.5-3nn; Texas 1 TAC 202 is the stub 477; four printed misprints with their evidence).
- A chapter cited as a whole is HELD where the corpus holds the code section by section (Hawaii 487N and 487R, Missouri chapter 37, West Virginia article 5A-6).
- Bare-number readers: a section printed with no code name is read for Arizona ("section 35-190"), Florida ("s. 501.171"), Minnesota ("sections 16C.08 and 16C.09"), Montana ("5-11-405") and Massachusetts ("Mass. Gen. Laws chapter 66A", "section 45 of chapter 30").
- The seed's own prose names instruments by bare number ("24-72 (Colorado Open Records Act)", "Left out: 61.934", "JML 25-103", "19-22", "147-33.72 and following", "1798.80 et seq."); these now resolve LEFT OUT with the recorded reason.
- Not citations: a page-footer line ("-2-") run onto a range, an order's compilation reference ("Executive Order 2002-14, MCL 18.62"), a section heading on the line after a sentence that ends in a code name ("Government Code." then "22001."), a list number ("; 6. If the form"), a footnote mark glued to a section ("10 MRSA § 13471") or to an order ("No. 1171"), "[now 1.24.20 NMAC]" beside the old number, and an order named in a statute's "Source:" line or in a revision-history row.
- The authority-context flag now treats a "References" or "Related Documents" block of any length, a bracketed source note ("[Neb. Rev. Stat. § 81-1120.27(1)]") and a numbered heading as authority context; a numbered heading or a prose paragraph ends the block.
- The extraction audit no longer depends on the forms it audits: a statute number printed after a section sign counts as a probable citation whether or not a code name precedes it.
- One instrument is one row: a section named inside a range cited in the same chapter, and an order cited with and without its year, are merged.

### What the tool still cannot read, and the measured miss rate

The audit before this pass (anchored on each state's own code names) reported 139 of 6,583 probable citations missed (2.1 percent). The new audit, which also counts every statute number printed after a section sign, reports **2,931 of 11,528 missed (25.4 percent)**. By document type the misses are: statutes 1,965 of 5,403 (36.4 percent; Texas statutes alone 751), policies and standards 871 of 4,822 (18.1 percent), rules 69 of 1,000 (6.9 percent), orders 26 of 303 (8.6 percent). The policy-and-standard misses are concentrated in California (378, mostly State Administrative Manual section numbers, which are policies in this corpus) and Nevada (268, a standard's own section numbers); the other 40 states together have 225, and those are real: a policy that names its state once and then cites "§ 143B-1342", "sections 86-512 to 86-524" or "section 27-43, Hawai'i Revised Statutes (HRS)" by number. A miss here is a number printed after a section sign that no extracted citation covers; some are not citations at all (a policy's own section numbers), so the rates are an upper bound on what the tool fails to read. Most of the difference from the old audit is the half it could not see: a statute citing its sibling sections by bare number. That is now read for Arizona, Florida, Minnesota and Montana (Utah and Virginia already read it); for the other states it is **not read**, so statute-to-statute citations understate what is missing there, and the policy-and-standard misses above are the figure that bears on the owner's idea.

Also unread, found by the review and not fixed: two-column PDF layouts that interleave a code name from one column with a number from the other (California SIMM 5305-F, SIMM 19B-4); session-law citations ("Public Law 2023, Chapter 681"); a Title-and-Part form ("Louisiana Administrative Code Title 34.VII"); Maryland "Title 10, Subtitle 13" with no section number; a hyphenated Kentucky section ("KRS 154.15-020"); the Florida list shorthand ("§§ 501.171, 812.081, 815.04, .045"); an Idaho suffix in brackets ("67-5745 [A]"); Montana "part 1 other than 2-15-114" in the seed's prose; a policy cited by another policy (Missouri C-5); a statute cited by article only (New York "art. 6-A"). 

The extraction cannot say what a cited section **says**: no cited instrument was fetched or read, so a candidate's scope (IT or not) is judged from the citing line only. The in-force status of every cited order and statute is unknown from our documents; spec rule 6 ("In force only") must be checked before any seed entry.

## Totals per state

Citations are to the state's own statutes, rules and executive orders; "instruments" are distinct instruments at the grain the corpus holds that state (a chapter, an article, a section or an order; one instrument can be counted under two resolutions, so the columns need not add to "cited"). "Not held" includes the instruments of a kind the audit marks unreliable (New York orders). Out-of-scope items are counted among not held.

| state | documents read | citing documents | citations found | instruments cited | held | stub | left out | not held |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| alaska | 13 | 12 | 76 | 47 | 23 | 0 | 1 | 23 |
| arizona | 30 | 20 | 46 | 35 | 6 | 0 | 8 | 21 |
| california | 171 | 122 | 689 | 141 | 43 | 1 | 15 | 82 |
| colorado | 62 | 45 | 259 | 26 | 12 | 1 | 4 | 9 |
| delaware | 36 | 29 | 46 | 7 | 2 | 0 | 3 | 2 |
| florida | 5 | 5 | 108 | 21 | 1 | 2 | 5 | 15 |
| hawaii | 47 | 10 | 35 | 10 | 5 | 0 | 0 | 5 |
| idaho | 136 | 58 | 115 | 28 | 12 | 0 | 1 | 15 |
| iowa | 49 | 49 | 177 | 36 | 18 | 1 | 6 | 11 |
| kansas | 56 | 37 | 72 | 39 | 16 | 0 | 3 | 20 |
| kentucky | 82 | 40 | 142 | 52 | 18 | 0 | 17 | 18 |
| louisiana | 63 | 21 | 76 | 40 | 10 | 0 | 1 | 29 |
| maine | 81 | 18 | 19 | 12 | 7 | 0 | 1 | 4 |
| maryland | 77 | 51 | 174 | 48 | 28 | 0 | 1 | 19 |
| massachusetts | 56 | 51 | 295 | 37 | 13 | 0 | 6 | 19 |
| michigan | 12 | 10 | 213 | 72 | 14 | 0 | 7 | 55 |
| minnesota | 30 | 11 | 1298 | 254 | 3 | 0 | 7 | 244 |
| missouri | 120 | 5 | 11 | 8 | 2 | 0 | 0 | 6 |
| montana | 13 | 12 | 128 | 66 | 46 | 0 | 0 | 20 |
| nebraska | 108 | 15 | 40 | 24 | 14 | 0 | 6 | 4 |
| nevada | 45 | 17 | 496 | 37 | 5 | 0 | 3 | 29 |
| new-hampshire | 4 | 3 | 19 | 7 | 3 | 0 | 1 | 3 |
| new-jersey | 45 | 17 | 49 | 22 | 10 | 0 | 2 | 10 |
| new-mexico | 39 | 35 | 176 | 34 | 17 | 0 | 2 | 15 |
| new-york | 64 | 58 | 373 | 22 | 4 | 1 | 0 | 17 |
| north-carolina | 69 | 54 | 781 | 42 | 5 | 1 | 8 | 34 |
| north-dakota | 9 | 3 | 51 | 6 | 1 | 0 | 2 | 3 |
| ohio | 43 | 40 | 188 | 77 | 15 | 0 | 3 | 59 |
| oklahoma | 143 | 141 | 461 | 39 | 1 | 11 | 6 | 21 |
| oregon | 49 | 37 | 474 | 47 | 4 | 0 | 3 | 43 |
| pennsylvania | 53 | 48 | 91 | 25 | 7 | 0 | 3 | 15 |
| rhode-island | 28 | 6 | 8 | 6 | 4 | 0 | 0 | 2 |
| south-carolina | 16 | 3 | 16 | 5 | 3 | 0 | 0 | 2 |
| south-dakota | 3 | 2 | 2 | 1 | 1 | 0 | 0 | 0 |
| texas | 19 | 17 | 286 | 36 | 6 | 3 | 1 | 26 |
| utah | 10 | 9 | 218 | 53 | 4 | 1 | 4 | 44 |
| vermont | 15 | 12 | 40 | 28 | 5 | 0 | 4 | 19 |
| virginia | 68 | 66 | 815 | 202 | 61 | 1 | 2 | 138 |
| washington | 124 | 105 | 697 | 42 | 7 | 1 | 6 | 31 |
| west-virginia | 82 | 39 | 106 | 25 | 14 | 0 | 6 | 5 |
| wisconsin | 17 | 3 | 30 | 12 | 4 | 2 | 3 | 3 |
| wyoming | 67 | 23 | 90 | 22 | 8 | 0 | 3 | 11 |
| **total** | **2,259** | **1,359** | **9,486** | **1,793** | **482** | **26** | **154** | **1,151** |

### Extraction recall by state

"Before" is the audit committed with the first version (anchored on code names); "now" is the independent audit. A low share means statute cross-references by bare number are not read for that state.

| state | citations before | citations now | probable now | missed now | share read now | share read before |
|---|---:|---:|---:|---:|---:|---:|
| alaska | 109 | 76 | 137 | 29 | 0.788 | 1.000 |
| arizona | 1 | 46 | 38 | 0 | 1.000 | 1.000 |
| california | 670 | 689 | 978 | 493 | 0.496 | 0.928 |
| colorado | 259 | 259 | 419 | 170 | 0.594 | 0.984 |
| delaware | 47 | 46 | 56 | 11 | 0.804 | 0.978 |
| florida | 47 | 108 | 82 | 3 | 0.963 | 0.765 |
| hawaii | 35 | 35 | 83 | 50 | 0.398 | 0.964 |
| idaho | 116 | 115 | 118 | 2 | 0.983 | 1.000 |
| iowa | 190 | 177 | 298 | 106 | 0.644 | 0.959 |
| kansas | 76 | 72 | 75 | 0 | 1.000 | 1.000 |
| kentucky | 165 | 142 | 137 | 1 | 0.993 | 0.993 |
| louisiana | 76 | 76 | 54 | 2 | 0.963 | 0.963 |
| maine | 22 | 19 | 24 | 6 | 0.750 | 1.000 |
| maryland | 174 | 174 | 294 | 128 | 0.565 | 0.854 |
| massachusetts | 262 | 295 | 173 | 0 | 1.000 | 1.000 |
| michigan | 230 | 213 | 261 | 37 | 0.858 | 1.000 |
| minnesota | 102 | 1298 | 1217 | 0 | 1.000 | 1.000 |
| missouri | 11 | 11 | 42 | 31 | 0.262 | 1.000 |
| montana | 10 | 128 | 14 | 1 | 0.929 | 0.909 |
| nebraska | 40 | 40 | 142 | 105 | 0.261 | 1.000 |
| nevada | 494 | 496 | 743 | 268 | 0.639 | 0.996 |
| new-hampshire | 19 | 19 | 21 | 2 | 0.905 | 0.905 |
| new-jersey | 49 | 49 | 47 | 2 | 0.957 | 0.978 |
| new-mexico | 371 | 176 | 180 | 47 | 0.739 | 0.957 |
| new-york | 374 | 373 | 393 | 29 | 0.926 | 0.986 |
| north-carolina | 783 | 781 | 877 | 128 | 0.854 | 0.975 |
| north-dakota | 51 | 51 | 43 | 22 | 0.488 | 1.000 |
| ohio | 189 | 188 | 205 | 39 | 0.810 | 0.994 |
| oklahoma | 461 | 461 | 358 | 30 | 0.916 | 1.000 |
| oregon | 474 | 474 | 363 | 0 | 1.000 | 1.000 |
| pennsylvania | 91 | 91 | 87 | 3 | 0.966 | 1.000 |
| rhode-island | 8 | 8 | 46 | 38 | 0.174 | 0.889 |
| south-carolina | 16 | 16 | 202 | 188 | 0.069 | 0.778 |
| south-dakota | 46 | 2 | 76 | 11 | 0.855 | 0.970 |
| texas | 285 | 286 | 1038 | 755 | 0.273 | 0.996 |
| utah | 218 | 218 | 213 | 1 | 0.995 | 0.957 |
| vermont | 40 | 40 | 36 | 0 | 1.000 | 1.000 |
| virginia | 815 | 815 | 833 | 5 | 0.994 | 0.986 |
| washington | 698 | 697 | 723 | 8 | 0.989 | 0.989 |
| west-virginia | 106 | 106 | 201 | 98 | 0.512 | 0.980 |
| wisconsin | 30 | 30 | 105 | 77 | 0.267 | 1.000 |
| wyoming | 90 | 90 | 96 | 5 | 0.948 | 1.000 |

## Candidates by state

Classes: **seed whole** (an IT instrument, or a whole chapter of IT law, the seed does not hold); **section slice of a non-IT chapter** (one or a few sections of a chapter that is otherwise out of scope); **owner scope decision** (whether a kind of law belongs at all); **owner scope decision (new evidence)** (the seed already records an open owner decision or a left-out reason for it, and these citing documents are new evidence for that decision, not a new finding). The tool resolves 40 of the 149 candidates below as LEFT OUT, and those are always the last class. Counts are citing documents. Each quoted line is verbatim from the named committed document. An instrument marked "not in the tool's output" was found by searching the documents for the citation; the tool does not read that form.

### alaska

**Owner scope decision**

- AS 09.80.190 (Uniform Electronic Transactions Act; definitions the held rule 2 AAC 05.200-290 adopts): 1 citing document. `ak-aac-2-05-200`: "(6) "electronic signature" has the meaning given in AS 09.80.190;"
- AS 44.17.020, 44.17.060 (reorganization authority of Administrative Order 284): 1 citing document. `ak-ao-284`: "under the authority of Article III, Sections 1, 23, and 24, Constitution of the State of Alaska, and in accordance with AS 44.17.020, 44.17.060, and 41.17.070, order the following reorganization of telecommunication and information technology services within the executive branch."

Out of scope or not worth a seed entry: 17 instruments; most cited: AS chapter 44.62 (2 documents); AS 45.50.471 to 45.50.561 (1 document); AS 11.46.550 (1 document).

### arizona

**Owner scope decision**

- A.R.S. 44-7012 (Uniform Electronic Transactions Act): 1 citing document. `az-ars-44-7042`: "A. Except as otherwise provided in section 44-7012, subsection D, and this subsection, each governmental agency, except state agencies, shall determine if, and the extent to which, the governmental agency will send and accept electronic records and electronic signatures to"

**Owner scope decision (new evidence)**

- A.R.S. 41-151 and 41-151.12 to 41-151.19 (state records management, cited by the electronic-records statute): 1 citing document. `az-ars-44-7041`: "subject to the management, preservation, determination of value and disposition of records requirements prescribed in sections 41-151, 41-151.12, 41-151.13, 41-151.14, 41-151.15, 41-151.16, 41-151.17 and 41-151.19 and the permanent public records requirements prescribed in section 39-101 shall comply with those requirements."

Out of scope or not worth a seed entry: 18 instruments; most cited: A.R.S. 35-190 (5 documents); A.R.S. 38-211 (2 documents); A.R.S. 13-2001 (1 document).

### california

**Seed whole**

- Gov. Code 11549.82: 1 citing document. `ca-eo-n-9-26`: "shall complete the requirements of subdivision (a) of Section 11549.82 of"
- Executive Order B-1-11: 1 citing document. `ca-tl-17-02`: "Mobile Phone & Mobile Computing Device Requests              Government Code Sections 11545, 11546                                                              Executive Order B-1-11"
- Executive Order D-3-99: 2 citing documents. `ca-civ-1798-1798-78`: "2001, unless otherwise authorized by the Department of Information Technology pursuant to Executive Order D-3-99, whenever an agency electronically collects personal information, as defined by Section 11015.5 of the Government Code, the agency shall retain the source or sources or"
- Executive Order S-03-10 (already a stub): 2 citing documents. `ca-itpl-10-08`: "this responsibility is implementation of EO S-03-10 issued February 9,"

**Section slice of a non-IT chapter**

- Gov. Code 14613.7 (California Highway Patrol incident reporting): 2 citing documents. `ca-simm-5340-a`: "•   California Highway Patrol Reporting Requirements (Government Code 14613.7):"
- Gov. Code 19130, 19131 (personal services contracts): 3 citing documents. `ca-sam-5200`: "• If the acquisition is for a personal services contract pursuant to Government Code §19130(a), the acquiring department must notify the State Personnel Board pursuant to Government Code §19131 prior to contract execution."
- Gov. Code 11145: 1 citing document. `ca-tl-18-06`: "IT PROJECT PROCUREMENT AUTHORITY                       Government Code Sections § 11145, 11546;"

**Owner scope decision**

- Gov. Code 8898.1 (independent verification organizations, EO N-9-26): 1 citing document. `ca-eo-n-9-26`: "complete the requirements of Section 8898.1 of the Government Code"
- Civ. Code 1633.1 et seq. (California UETA): 2 citing documents. `ca-simm-5330-d`: "• The California Uniform Electronic Transactions Act, California Civil Code"
- Gov. Code 11000 (definition of state agency): 2 citing documents. `ca-sam-4900`: "Government Code (GC): 11000, 11545, 11546, 11546.1(e), 11546.7, 11549.63, 11549.63(g), 11549.64, 11549.65, 11549.65(c), 11549.66"
- Pub. Contract Code 1102 (definition of emergency): 2 citing documents. `ca-itpl-10-14`: "Chapter 404, Statutes of 2010 Public Contract Code Section 1102"

**Owner scope decision (new evidence)**

- Pub. Contract Code 6611 (Innovation Procurement Sprints): 3 citing documents. `ca-eo-n-04-19`: "pursuant to Public Contract Code section 6611."
- Gov. Code 11135 (nondiscrimination; electronic and information technology accessibility): 7 citing documents. `ca-itpl-10-10`: "Government Code Sections 11135 and 11545                                            OFFICE OF THE STATE CHIEF"
- Executive Order S-09-09 (state contract expenditures): 2 citing documents. `ca-simm-18`: "SIMM 18A: IT Contract Exemptions Executive Order S-09-09"
- Civ. Code 3111 (AI training-data documentation): 1 citing document. `ca-sam-4900`: "References: GC 11546.7; Civil Code 3111"
- Executive Order S-04-06 (continuity planning): 1 citing document. `ca-sam-5300`: "NIST SP 800-34; NIST SP 800-53: Contingency Planning (CP), NIST IR 8286D; NIST CSF 2.0 IDENTIFY (ID), PROTECT (PR), RESPOND (RS), RECOVER (RC); SAM 5325; SIMM 5325-A; SIMM 5325-B; SIMM 5300-C; SAM 5300.4; SIMM 5330-C; Executive Order S-04-06"
- Civ. Code 1798.82 (breach notice; the seed leaves 1798.80 et seq. out as businesses): 3 citing documents. `ca-tl-16-03`: "NOTIFICATION REQUIREMENTS                                  Civil Code Section 1798.29, 1798.82"

Out of scope or not worth a seed entry: 70 instruments; most cited: Penal Code 502 (3 documents); Gov. Code 15275 to 15277 (3 documents); Health & Safety Code 102235 (2 documents).

### colorado

**Section slice of a non-IT chapter**

- C.R.S. article 24-34 (24-34-802 and 24-34-301(18), accessibility standards bind public entities): 1 citing document. `co-ccr-8-1501-11`: "Section 24-34-802(1)(c), C.R.S. specifies that the accessibility standards for individuals with a disability"

**Owner scope decision**

- 1 CCR 101-9 (State Procurement Rules): 1 citing document. `co-oit-genai-policy`: "●   1 CCR 101-9 Procurement Rules"
- 1 CCR 101-1 (interagency agreements, rule 3-5): 2 citing documents. `co-oit-delegation-of-authority-policy`: "●   1 CCR 101-1-3-5 - Interagency Agreements"
- C.R.S. article 24-50, part 10 (federal tax information background checks): 1 citing document. `co-oit-cisp-004`: "Tax Information (C.R.S. 24-50-1001, et seq.)"

**Owner scope decision (new evidence)**

- C.R.S. article 24-72 (Colorado Open Records Act; 24-72-202(6)(b)(X), (XII), 24-72-204, 24-72-501): 6 citing documents. `co-ccr-8-1501-12`: "contrary to the public interest, including requests related to security under C.R.S. section 24-72-"
- C.R.S. articles 24-71.3 and 24-71 (electronic transactions and signatures): 1 citing document. `co-ccr-8-1501-9`: "governmental agencies in accordance with CRS 24-71.3-101 et seq. These rules identify the covered"

Out of scope or not worth a seed entry: 5 instruments; most cited: C.R.S. article 24-4 (4 documents); C.R.S. article 11-56 (1 document); C.R.S. article 15-1 (1 document).

### delaware

**Owner scope decision**

- 19 Del. C. chapter 7 (employee privacy and monitoring): 2 citing documents. `de-dti-0042-02`: "in regard to use of these services. This is in accordance with 19 Del. C. chapter 7."
- 6 Del. C. chapter 45 (section 4504, cited beside ADA and Section 508): 1 citing document. `de-ac-dig-001`: "Communications and Video Accessibility Act of 2010 (CVAA), and Title 6 Delaware Code"

**Owner scope decision (new evidence)**

- 29 Del. C. 501 to 526 (Delaware Public Records Law; the seed's left_out names it as an owner decision): 2 citing documents. `de-pi-erec-001`: "3. In order to comply with the Delaware Public Records Law (29 Delaware Code §501-"

Out of scope: none.

### florida

**Seed whole**

- F.A.C. 60GG-1 (already a stub): 2 citing documents. `fl-fds-60gg-1-faq`: "Agencies”) regarding the requirements established in Rule Chapter 60GG-1, Florida Administrative"

**Owner scope decision (new evidence)**

- F.S. 501.171 (security of confidential personal information; breach notice): 2 citing documents. `fl-st-282`: "2. For cybersecurity breaches, state agencies shall provide notice in accordance with s. 501.171."
- F.S. 287.057(11), (26) and 287.042 (IT provisions inside the procurement chapter): 3 citing documents. `fl-fds-60gg-1-faq`: "•   Continuing oversight meetings pursuant to s. 287.057(26), F.S."
- F.S. 112.22 (prohibited applications on government devices): 2 citing documents. `fl-fds-prohibited-applications-list`: "meet the criteria for prohibited applications established in section 112.22(1)(f), Florida Statutes. For waiver requests,"
- F.S. 216.023(4)(a)10 (budget request for IT projects over $10 million): 1 citing document. `fl-fds-npv-guide`: "Section 216.023 and section 282.0051, Florida Statutes; Rule Chapter 60GG-1, Florida"

Out of scope or not worth a seed entry: 13 instruments; most cited: F.S. chapter 120 (2 documents); F.S. chapter 20 (1 document); F.S. chapter 119 (1 document).

### hawaii

**Section slice of a non-IT chapter**

- HRS 103D-310(c) and HAR 3-122-112 (cooperative purchasing compliance): 1 citing document. `hi-pol-spo-2017-06`: "COMPLIANCE PURSUANT TO HRS §103D-310(c). Use of GSA Schedule 70 is for the"

**Owner scope decision**

- HRS chapter 103D (Hawaii Procurement Code): 2 citing documents. `hi-pol-spo-2017-06`: "procurement process pursuant to HRS 103D shall be used, unless granted express approval by"
- HRS 94-1.1 (public archives; records): 1 citing document. `hi-pol-cdo-005`: "4     HRS § 94-1.1 https://www.capitol.hawaii.gov/hrscurrent/Vol02_Ch0046-0115/HRS0094/HRS_0094-0001_0001.htm."

Out of scope or not worth a seed entry: 1 instrument; most cited: HRS chapter 91 (1 document).

### idaho

**Owner scope decision**

- Idaho Code 55-1705 (Idaho coordinate system): 2 citing documents. `id-ita-s4233`: "IDTM83: The Idaho coordinate system of 1983, single zone as described in 55-1705 (4) Idaho"

**Not in force (spec rule 6): no seed**

- Executive Orders 2005-22, 2006-05 and 2001-07 (issued before 2019; the seed records that none is in force): 5 citing documents. `id-ita-p1040`: "11/15/06 – Updated Authority section to reference Executive Order 2005-22."
- **Open question for the owner, separate from any seed entry:** the held ITA documents that cite Executive Order 2005-22 (`id-ita-p1040`, `id-ita-p1050`, `id-ita-p1060`) rest on an order the seed records as lapsed. Are they still in force?

Out of scope or not worth a seed entry: 8 instruments; most cited: Idaho Code 74-101 to 74-126 (3 documents); Idaho Code 74-101 to 74-127 (1 document); Idaho Code 58-330 (1 document).

### iowa

**Owner scope decision**

- IAC 11-25 (the rule 19 standards name as their enforcement; agency [11] Title II chapters 20 to 34 are reserved): 19 citing documents. `ia-ocio-1028`: "are identified, the agency will receive written notification pursuant to IAC 11--25.11(8A)."

**Owner scope decision (new evidence)**

- Iowa Code 8A.101 (who a standard binds): 16 citing documents. `ia-ocio-1027`: "This standard applies to all participating agencies as defined by Iowa Code 8A.101 and in support of SF396"
- Iowa Code 8A.201 (IT consolidation exemptions; common web content management system): 3 citing documents. `ia-ocio-1047`: "under Iowa Code 8A.201 (4}, to use a common website content management system."

**Not in force (spec rule 6): no seed**

- Iowa Code 8A.204 and the Technology Governance Board (the seed records the current Code no longer provides for them): 1 citing documents. `ia-ocio-1034`: "As provided for under Iowa Code section 8A.204, the Technology Governance Board, in conjunction with the"

Out of scope or not worth a seed entry: 10 instruments; most cited: Iowa Code 679A.19 (3 documents); Iowa Code 17A.7 (2 documents); Iowa Code 602.1102 (2 documents).

### kansas

No candidates.
Out of scope or not worth a seed entry: 20 instruments; most cited: K.S.A. 45-215 (9 documents); K.S.A. 45-229 (6 documents); K.S.A. 22-4714 (2 documents).

### kentucky

**Section slice of a non-IT chapter**

- KRS 186A.040 and 186A.285 (named in COT's own implementing list): 3 citing documents. `ky-krs-42-726`: "with KRS 42.720 to 42.742, 45.253, 171.420, 186A.040, and 186A.285;"

**Owner scope decision**

- KRS 11.080 and 11.090 to 11.110 (scope-defining definitions of agency): 2 citing documents. `ky-cio-076`: "office, or agency of the state as defined in KRS 11.080 and as the term agency is used"

**Owner scope decision (new evidence)**

- KRS 45.253 (named in COT's own implementing list): 3 citing documents. `ky-krs-42-720`: "of powers and authority conferred by KRS 42.720 to 42.742, 45.253, 171.420,"
- KRS 171.420 (State Archives retention period): 6 citing documents. `ky-krs-42-720`: "of powers and authority conferred by KRS 42.720 to 42.742, 45.253, 171.420,"

Out of scope or not worth a seed entry: 11 instruments; most cited: KRS 164.001 (2 documents); KRS chapter 13A (2 documents); KRS 189.292 (1 document).

### louisiana

**Section slice of a non-IT chapter**

- R.S. 39:1594, 39:1595, 39:1600.2 (methods of source selection the IT procurement part works through): 5 citing documents. `la-rs-39-198`: "contracts and consulting services contracts related to information technology are defined in this Part, and the provisions of this Part supersede, with respect to such procurements, any existing conflicting statutory provisions and supplement the provisions of R.S. 39:1551 through 1736."
- R.S. 39:1556 (definitions of procure and consulting service) (not in the tool's output): 2 citing documents. `la-rs-39-1753-1`: "(3) "Procure" and "procurement" shall have the same meaning as provided in R.S. 39:1556."

**Owner scope decision**

- R.S. 39:1551 to 39:1736 (the Louisiana Procurement Code): 1 citing document. `la-rs-39-200`: "this Part do not relate to the procurement of services covered by R.S. 39:1481 through 1526 except as provided in R.S. 39:198. The Louisiana Lease of Movables Act, R.S. 9:3301 through 3342, shall not apply to the provisions of this"
- R.S. 36:3 and 39:2 (scope-defining definitions): 4 citing documents. `la-rs-39-196`: "applicable to all state agencies in the executive branch, as defined in R.S. 36:3(1), except for any agency of a statewide elected official, with respect to the purchase, lease, and rental of all information technology equipment, related services, and software."
- LAC 34:VII (property control): 1 citing document. `la-ots-movable-property-tagging-policy`: "of OTS and the customer agency to follow all guidelines of the Louisiana Administrative Code Title 34, Part VII as it pertains to Property Control. The respective customer agency will be responsible for tagging all movable IT equipment excluding leased"
- Executive Order MJF 96-50 (Year 2000 compliance): 1 citing document. `la-doa-policy-7`: "It is the policy of the Division of Administration, as required by Executive Orders MJF 96-50 as amended, that all software and equipment procured by the Division must be Year 2000 compliant. The systems must not produce incorrect results prior"

Out of scope or not worth a seed entry: 16 instruments; most cited: R.S. 47:1508 (2 documents); R.S. 15:587.5 (1 document); R.S. 15:587.6 (1 document).

### maine

No candidates.
Out of scope or not worth a seed entry: 4 instruments; most cited: 1 M.R.S. 400 (1 document); 1 M.R.S. 401 to 410 (1 document); 25 M.R.S. 4501 (1 document).

### maryland

**Seed whole**

- State Gov't 10-1501 to 10-1504 (Maryland Open Data Act): 1 citing document. `md-doit-data-classification-policy`: "Source: Md. State Government Article, § 10-1501"

**Section slice of a non-IT chapter**

- State Gov't 2-1224, 2-1226 (cybersecurity information held by the Office of Legislative Audits): 1 citing document. `md-doit-incident-reporting-state-government`: "Consistent with the requirements established in (Md. Code, State Gov't § 2-1226), information obtained by the Office of Legislative Audits (OLA) is generally protected from disclosure. Additionally, if the information obtained will be included in a public audit report, per"
- COMAR 21.05 (21.05.08.05, the nonvisual access clause in procurement): 1 citing document. `md-doit-nonvisual-access-regulatory-standards`: "Applicable Law & Other Policy • COMAR 21.05.08.05"

**Owner scope decision**

- Executive Order 01.01.2017.22 (listed in the IT Security Manual's Authority section): 1 citing document. `md-doit-it-security-manual-v1-2`: "●   Manual (FISCAM)     ●   Maryland Executive Order 01.01.2017.22"

Out of scope or not worth a seed entry: 14 instruments; most cited: State Gov't 8-201 (1 document); COMAR 13A.06 (1 document); COMAR 13A.08 (1 document).

### massachusetts

**Section slice of a non-IT chapter**

- M.G.L. c. 30, section 63 (notice of personal data systems): 8 citing documents. `ma-801-cmr-3`: "required by M.G.L. c. 30, § 63 and c. 66A, § 2(e)."
- M.G.L. c. 36, section 40 (authority line of 950 CMR 120.00): 1 citing document. `ma-950-cmr-120`: "Indexes required by M.G.L. c. 36. Unless otherwise noted, all Indexes created by Massachusetts"

**Owner scope decision**

- M.G.L. c. 214, sections 3B and 1B (remedies under the fair information practices law): 1 citing document. `ma-950-cmr-33`: "general, it is an invasion of personal privacy under M.G.L. c. 214, § 1B, as appearing in St. 1973, c. 1114, § 62, to"

**Owner scope decision (new evidence)**

- M.G.L. c. 6A, sections 7A and 109 (EOTSS's own authority): 8 citing documents. `ma-801-cmr-3`: "M.G.L. c. 6A, § 5, or to the Office of the Governor in accordance with M.G.L. c. 66A, and each"

Out of scope or not worth a seed entry: 15 instruments; most cited: M.G.L. c. 6 (5 documents); M.G.L. c. 4 (4 documents); M.G.L. c. 66 (2 documents).

### michigan

**Seed whole**

- Executive Order 1994-13 (compiled at MCL 18.32) (not in the tool's output): 1 citing document. `mi-eo-2001-3`: "3. Executive Order 1994-13, as amended, being Section 18.32 of the Michigan Compiled Laws (transfer of certain computer program analysis and programming responsibilities to the Michigan Administrative Information Network);"

**Section slice of a non-IT chapter**

- MCL 24.401 to 24.404 (Records Media Act): 3 citing documents. `mi-eo-2009-55`: "e. Section 4 of the Records Reproduction Act, 1992 PA 116, MCL 24.404."

**Owner scope decision**

- MCL 333.2503, 333.2505, 333.20173a (Public Health Code, Health Information Technology Commission): 4 citing documents. `mi-eo-2009-55`: "Health Information Technology Commission created under Section 2503 of the Public Health Code, 1978 PA 368, MCL 333.2503, is transferred to the Director of the Department of Technology, Management, and Budget, or his or her designee from within the Department."

Out of scope or not worth a seed entry: 53 instruments; most cited: MCL chapter 15 (3 documents); MCL chapter 16 (3 documents); MCL chapter 722 (3 documents).

### minnesota

**Section slice of a non-IT chapter**

- Minn. Stat. chapter 16A (16A.11, 16A.1285, 16A.28, 16A.671; IT funding): 2 citing documents. `mn-stat-13`: "(c) Register of ownership of bonds or certificates. Information in a register of ownership of state bonds or certificates is classified under section 16A.672, subdivision 11."

**Owner scope decision**

- Minn. Stat. 138.17 (Records Management Act): 2 citing documents. `mn-stat-13`: "this section may be construed to require retention of government data, including private data on decedents or confidential data on decedents, for periods of time other than those established by the procedures provided in section 138.17, or any other statute."

**Owner scope decision (new evidence)**

- Minn. Stat. chapter 16C (16C.02 to 16C.09; procurement): 3 citing documents. `mn-mnit-supply-chain-risk-policy`: "c. Minnesota Statutes Chapter 16C: State Procurement (2024) – Key sections: § 16C.03"

Out of scope or not worth a seed entry: 242 instruments; most cited: Minn. Stat. chapter 15 (3 documents); Minn. Stat. chapter 144 (2 documents); Minn. Stat. chapter 3 (2 documents).

### missouri

No candidates.
Out of scope or not worth a seed entry: 6 instruments; most cited: Executive Order 05-05 (1 document); Executive Order 92-04 (1 document); RSMo 432.230 (1 document).

### montana

No candidates.
Out of scope or not worth a seed entry: 20 instruments; most cited: MCA 2-15-1001 (2 documents); MCA 2-15-102 (2 documents); MCA 2-15-124 (2 documents).

### nebraska

**Owner scope decision**

- Neb. Rev. Stat. 49-14,101.01, 49-14,101.02 (prohibited uses of public resources): 2 citing documents. `ne-nitc-7-101`: "passage, or defeat of a ballot question; these uses are prohibited. [Neb. Rev. Stat. § 49-"

**Owner scope decision (new evidence)**

- Neb. Rev. Stat. 81-1117, 81-1120.17, 81-1120.20 (procurement review by the Office of the CIO): 2 citing documents. `ne-nitc-1-204`: "(1) Purpose. Pursuant to Neb. Rev. Stat. §§ 81-1117, 81-1120.17, and 81-1120.20, certain"
- Neb. Rev. Stat. 81-1120.02, 81-1120.27 (communications system; personal use): 2 citing documents. `ne-nitc-1-101`: "electromagnetic systems. [Source: Neb. Rev. Stat. § 81-1120.02(4)]"
- Neb. Rev. Stat. 84-1201 to 84-1228 (Records Management Act): 1 citing document. `ne-nitc-1-101`: "codified at Neb. Rev. Stat. §§ 84-1201 to 84-1228."

Out of scope or not worth a seed entry: 2 instruments; most cited: Neb. Rev. Stat. 76-2502 (2 documents); Neb. Rev. Stat. 81-2402 (1 document).

### nevada

**Section slice of a non-IT chapter**

- NRS 281.195 (Use of Computers): 2 citing documents. `nv-sec-s-4-08-02`: "of certain incidents;       NRS 281.195, Use of Computers"

Out of scope or not worth a seed entry: 28 instruments; most cited: NRS chapter 205 (4 documents); NRS chapter 463 (2 documents); NRS chapter 439 (2 documents).

### new-hampshire

**Section slice of a non-IT chapter**

- RSA 21-I:11, I(a)(8) and 21-I:14, XII (DAS purchasing subsections tied to IT contract terms) (not in the tool's output): 1 citing document. `nh-st-21-r`: "IV. For purposes of this section, "agency" shall have the meaning defined in RSA 21-I:11, II(b), but shall not include those agencies exempt under RSA 21-I:18 from the provisions of RSA 21-I."

Out of scope or not worth a seed entry: 3 instruments; most cited: RSA chapter 94 (1 document); RSA chapter 14 (1 document); RSA chapter 21-G (1 document).

### new-jersey

**Owner scope decision**

- Executive Orders 87 (1998) and 84 (1984) (founding orders of the Office of Information Technology): 3 citing documents. `nj-eo-christie-225`: "established by, and granted powers through, Executive Order No. 84"
- N.J.S.A. 52:25-23 (anti-splitting of purchases): 1 citing document. `nj-treasury-circular-24-04`: "NOTE: Pursuant to N.J.S.A. 52:25-23(a), agencies shall not divide purchases exceeding the"

Out of scope or not worth a seed entry: 5 instruments; most cited: N.J.S.A. 11A:1-1 (1 document); N.J.S.A. 52:14D-1 (1 document); Executive Order 1 (2006) (1 document).

### new-mexico

**Section slice of a non-IT chapter**

- NMSA 14-3-15.2 (Public Records Act, electronic signature authority) (not in the tool's output): 1 citing document. `nm-nmac-1-12-7`: "1.12.7.2 SCOPE: To implement the electronic signature authority pursuant to the Public Records Act, Section 14-3-15.2 NMSA 1978 and the New Mexico Uniform Electronic Transactions Act, Section 14-16-1 et seq NMSA 1978."
- NMSA 14-16 and 14-15 (Uniform Electronic Transactions Act; Electronic Authentication of Documents Act) (not in the tool's output): 1 citing document. `nm-nmac-1-12-7`: "1.12.7.2 SCOPE: To implement the electronic signature authority pursuant to the Public Records Act, Section 14-3-15.2 NMSA 1978 and the New Mexico Uniform Electronic Transactions Act, Section 14-16-1 et seq NMSA 1978."

Out of scope or not worth a seed entry: 15 instruments; most cited: NMSA 1978 article 10-9 (2 documents); NMSA 1978 article 14-16 (1 document); NMSA 1978 article 14-15 (1 document).

### new-york

**Section slice of a non-IT chapter**

- Public Officers Law article 6-A (Personal Privacy Protection Law), sections 91 to 99 (not in the tool's output): 1 citing document. `ny-nycrr-551`: "(Statutory authority: Public Officers Law, art. 6-A, §94[2]; Executive Law, §206-a[11])"
- Executive Law 170-f (IT accessibility) and 206-a(11) (not in the tool's output): 2 citing documents. `ny-nycrr-551`: "(Statutory authority: Public Officers Law, art. 6-A, §94[2]; Executive Law, §206-a[11])"
- State Finance Law 163 (and 163-e, 165) (not in the tool's output): 1 citing document. `ny-its-p20-004`: "ascertaining whether State Finance Law Section 163 applies."

**Owner scope decision**

- Arts and Cultural Affairs Law 57.05 with 8 NYCRR 188 (not in the tool's output): 1 citing document. `ny-nys-p11-001`: "57.05 of the Arts and Cultural Affairs Law and 8 NYCRR Part 188."
- Governors' continuing orders for Executive Order 117 (Executive Orders 5, 9, 2 and 6): 51 citing documents. `ny-its-g26-002`: "Pataki on January 28, 2002 and continued by Executive Order 5 issued by Governor Eliot Spitzer on"

Out of scope or not worth a seed entry: 11 instruments; most cited: Executive Law (1 document); 8 NYCRR 188 (1 document); Executive Law (1 document).

Also 6 instruments of a kind the audit marks unreliable for this state (see extraction notes in the JSON); none is a candidate until a person reads the quotes.

### north-carolina

**Seed whole**

- Executive Order 276 (stub; high-risk applications): 1 citing document. `nc-high-risk-applications-policy`: "privacy of North Carolinians, Executive Order No. 276 directs NCDIT and the State CIO to develop a"

**Section slice of a non-IT chapter**

- G.S. 143-135.9, 143-52.1, 143-48(b), 143-48.3, 143-53.1 (procurement sections the State CIO's IT purchasing runs on) (not in the tool's output): 4 citing documents. `nc-gs-143b-art-15`: "(b) The Department shall review all procurements to ensure they meet current technology standards, are not duplicative, meet business objectives, are cost-effective, and are adequately funded. G.S. 143-135.9 shall apply to information technology procurements."
- G.S. 66-58.5, 66-325 (electronic offers and transactions) (not in the tool's output): 1 citing document. `nc-9-ncac-06b`: "History Note: Authority G.S. 66-58.5; 66-325; 147-33.95;"
- G.S. 143B-10(j)(3) (internal policy authority of the Department) (not in the tool's output): 1 citing document. `nc-clean-desk-procedure`: "Pursuant to N.C.G.S. § 143B-10(j)(3) and the Statewide Information Security Manual (SISM) the N.C."

**Owner scope decision**

- G.S. 132-6.1, 132-1.10 (public records: electronic data-processing databases) (not in the tool's output): 7 citing documents. `nc-gs-143b-art-15`: "(c) Such information technology information protected from public disclosure under G.S. 132-6.1(c), including, but not limited to, security features of critical infrastructure, information technology systems, telecommunications networks, or electronic security systems, including hardware or software security, passwords, or security standards,"
- G.S. chapter 116E (Education Longitudinal Data System) (not in the tool's output): 2 citing documents. `nc-9-ncac-06a`: "History Note: Authority G.S. 143B-1321(a)(16); 116E-4(b);"
- Executive Orders 16 (1993), 12 (2013) and 18 (2009) (not in the tool's output): 2 citing documents. `nc-former-email-mailbox-policy`: "•    Executive Order 18 – Email Retention and Archiving Policy (July 7, 2009)"

Out of scope or not worth a seed entry: 34 instruments; most cited: G.S. chapter 14 (7 documents); G.S. chapter 75 (7 documents); G.S. chapter 132 (6 documents).

### north-dakota

**Section slice of a non-IT chapter**

- NDCC 23-12-19 (health information network, law implemented by rule 113-02-01) (not in the tool's output): 1 citing document. `nd-nac-113-02-01`: "Law Implemented: NDCC 23-12-19, 54-59-25, 54-59-26, 54-59-28, 54-59-29"

**Owner scope decision**

- NDCC 6-09-43 (health information technology planning loans) (not in the tool's output): 1 citing document. `nd-ndcc-54-59`: "health information technology infrastructure under section 6-09-43."

Out of scope or not worth a seed entry: 3 instruments; most cited: N.D.C.C. chapter 23-12 (1 document); N.D.C.C. chapter 28-32 (1 document); N.D.C.C. chapter 47-25.1 (1 document).

### ohio

**Seed whole**

- R.C. 1306.20 (definition of state agency for the electronic transaction sections) (not in the tool's output): 2 citing documents. `oh-orc-1306-21`: "(D) For purposes of this section, "state agency" has the same meaning as in section 1306.20 of the Revised Code."

**Section slice of a non-IT chapter**

- R.C. 126.08 (authority line of IT-16) (not in the tool's output): 1 citing document. `oh-it-16`: "V. Authority ORC 125.18, 126.08"
- R.C. 125.02, 125.04 (DAS Director sections; authority line of IT-06) (not in the tool's output): 1 citing document. `oh-it-06`: "V. Authority ORC 125.02, 125.04, 125.18"

**Owner scope decision**

- R.C. 149.34, 149.11 (records management) (not in the tool's output): 2 citing documents. `oh-it-07`: "1. In accordance with ORC 149.34 (A), the "head of each state agency, office, institution, board, or commission shall...establish, maintain, and direct an active continuing program for the effective management of the Records of the state agency..."."

Out of scope or not worth a seed entry: 54 instruments; most cited: R.C. 149.43 (5 documents); R.C. 111.15 (2 documents); Executive Order 2004-02T (2 documents).

### oklahoma

**Section slice of a non-IT chapter**

- 74 O.S. 85.5 (CIO's IT purchasing authority in the Central Purchasing Act): 2 citing documents. `ok-pol-isd-procurement`: "Pursuant to 62 O.S. §34.11.1 and 74 O.S. §85.5, the Chief Information Officer (“CIO”) has sole"

**Owner scope decision**

- 51 O.S. 151 to 172 (cited by nine OMES standards; subject not stated): 9 citing documents. `ok-std-agency-electronic-information-request`: "This standard shall take effect upon publication and is made pursuant to Title 51 O.S. §§ 151-172."
- 67 O.S. 206, 305 and OAC 60:10 (Archives and Records Commission): 2 citing documents. `ok-std-data-classification-security`: "and have their programs approved by the Archives and Records Commission (67 O.S. Sec 206,"
- OAC 580:16 (central purchasing rules): 1 citing document. `ok-pol-isd-procurement`: "Statutory Reference: Titles 62 and 74 of the Oklahoma Statutes and OAC Section 580:16"

**Owner scope decision (new evidence)**

- 62 O.S. 34.11.1 to 34.33 and 35.1 to 35.9; 74 O.S. 3113.1 (already stubs): 133 citing documents. `ok-pol-information-security-ppg`: "Chief Information Officer in accordance with Title 62 O.S. §§ 34.11.1 and 34.12 and Title 62 O.S."
- 62 O.S. 34.3 (creation of OMES): 1 citing document. `ok-pol-hipaa-hitech`: "The Information Services Division (“ISD”) was created pursuant to 62 O.S. § 34.3 (Supp. 2010) as a"

Out of scope or not worth a seed entry: 14 instruments; most cited: 74 O.S. 150.9 (1 document); 10 O.S. 7505-1.1 (1 document); 10 O.S. 7510-1.5 (1 document).

### oregon

**Section slice of a non-IT chapter**

- ORS 184.305, 184.340 (DAS Director's powers): 3 citing documents. `or-das-107-004-110`: "AUTHORITY:         ORS 184.305, ORS 184.340, ORS 291.015, ORS 291.016, ORS 291.018, ORS"

**Owner scope decision**

- ORS 646A.600 to 646A.628 (Oregon Consumer Information Protection Act): 4 citing documents. `or-das-107-004-120`: "under the Oregon Consumer Information Protection Act (ORS 646A.600 et seq.). Depending upon the"
- ORS 219.110: 1 citing document. `or-das-107-004-160`: "•   ORS 162.305, 192.660, 219.110, 276A.206, 276A.300,"

**Owner scope decision (new evidence)**

- ORS 291.015, 291.016, 291.018, 291.026, 291.034, 291.047 (budget and state administration; authority of the mobile-device and acceptable-use policies): 5 citing documents. `or-das-107-004-110`: "AUTHORITY:         ORS 184.305, ORS 184.340, ORS 291.015, ORS 291.016, ORS 291.018, ORS"
- ORS 279B.030 (cost analysis for IT services): 3 citing documents. `or-das-107-004-130`: "Enterprise Information Services                                                      ORS 276A.200-236; and 279B.030"

Out of scope or not worth a seed entry: 38 instruments; most cited: ORS chapter 174 (15 documents); ORS chapter 352 (9 documents); ORS chapter 192 (6 documents).

### pennsylvania

**Seed whole**

- Executive Orders 2011-05 and 2004-8 (enterprise IT governance): 2 citing documents. `pa-md-245-13`: "in Executive Order 2004-8 As Amended, Enterprise Information Technology Governance Board.                 •"

**Section slice of a non-IT chapter**

- 4 Pa. Code 3.21 (continuity of government data processing plan): 1 citing document. `pa-itp-business-continuity-policy`: "Agencies are required by 4 Pa. Code, Section 3.21 of the provisions of the Pennsylvania"

**Owner scope decision (new evidence)**

- 71 P.S. 181, 182 (Administrative Code of 1929, sections 501 and 502): 3 citing documents. `pa-eo-2016-06`: "WHEREAS,     Sections 501 and 502 of the Administrative Code of 1929, 71 P.S. §§ 181,"

Out of scope or not worth a seed entry: 12 instruments; most cited: 65 P.S. 67.101 (2 documents); 73 P.S. 2301 to 2330 (2 documents); 65 P.S. 67.101 to 67.3104 (1 document).

### rhode-island

No candidates.
Out of scope or not worth a seed entry: 2 instruments; most cited: R.I. Gen. Laws 28-42-38 (1 document); R.I. Gen. Laws 38-2-2 (1 document).

### south-carolina

**Owner scope decision**

- General Appropriations Act provisos 93.9, 117.96, 117.102, 117.107 and others (not in the tool's output): 1 citing document. `sc-admin-statewide-infosec-program-policy`: "legislative authorities established by the South Carolina General Assembly in Provisos"

Out of scope or not worth a seed entry: 2 instruments; most cited: S.C. Code chapter 1-3 (1 document); S.C. Code chapter 1-1 (1 document).

### south-dakota

No candidates.
Out of scope: none.

### texas

**Seed whole**

- 1 TAC chapter 201 (DIR rule on IRM duties, section 201.4) (not in the tool's output): 1 citing document. `tx-dir-irm-continuing-education-guide`: "requirements for an agency under 1 Texas Administrative Code § 201.4. A request for a waiver"
- 1 TAC chapter 206 (already a stub) (not in the tool's output): 1 citing document. `tx-dir-internet-email-domain-name-policy`: "• Texas Administrative Code, Title 1, Chapter 206 (State Web Sites)"

**Section slice of a non-IT chapter**

- Gov't Code 551.127 (videoconference standards in the Open Meetings Act chapter) (not in the tool's output): 1 citing document. `tx-dir-videoconferencing-standards`: "The Department of Information Resources (DIR) is required by Texas Government Code §"
- Gov't Code 572.070 (foreign-adversary awareness training) (not in the tool's output): 2 citing documents. `tx-gv-2063`: "(5) reporting to the Texas Ethics Commission as required by Section 572.070 and to law enforcement agencies suspected foreign influence operations and other interactions with persons acting on behalf of a foreign adversary."

**Owner scope decision**

- 1 TAC chapter 203 (not in the tool's output): 1 citing document. `tx-dir-security-control-standards-catalog`: "1 TAC Chapter 203"
- Gov't Code 441.185 and 13 TAC chapter 6 (records retention) (not in the tool's output): 2 citing documents. `tx-gv-2054`: "development project and any information resources projects described in this subchapter, a state agency shall classify the data produced from or used in the project and determine appropriate data security and applicable retention requirements under Section 441.185 for each classification."

**Owner scope decision (new evidence)**

- Bus. & Com. Code 521 (521.002, 521.053; the seed leaves it out as businesses): 3 citing documents. `tx-dir-state-website-linking-privacy-policy`: "Texas Business & Commerce Code, Section 521.053"

Out of scope or not worth a seed entry: 26 instruments; most cited: Education Code chapter 61 (6 documents); Education Code chapter 5 (2 documents); Gov't Code chapter 552 (2 documents).

### utah

**Seed whole**

- Utah Admin. Code R895-7 (stub; Acceptable Use of IT Resources) (not in the tool's output): 2 citing documents. `ut-dts-1000-0003`: "Authority: Utah Administrative Code, R895-7. Acceptable Use of Information Technology Resources; Utah Administrative Code, R477-11. Discipline. DTS Policy 5000-0002 Enterprise Security Policy"

**Section slice of a non-IT chapter**

- Utah Code 63J-1-201, 63J-1-410 (budgetary procedures): 3 citing documents. `ut-code-63a-16`: "(2) The division has authority to operate as an internal service fund agency as provided in Section 63J-1-410."

**Owner scope decision (new evidence)**

- Utah Code 63G-2-206 (GRAMA; shared records of the Cyber Center): 2 citing documents. `ut-code-63a-16`: "(a) A governmental entity that is required to submit information under Section 63A-19-405 shall provide records to the Cyber Center as a shared record in accordance with Section 63G-2-206."

Out of scope or not worth a seed entry: 43 instruments; most cited: Utah Admin. Code R477-11 (3 documents); Utah Code chapter 63E-1 (3 documents); Utah Code chapter 63A-3 (2 documents).

### vermont

**Owner scope decision (new evidence)**

- 3 V.S.A. 2222 and 2283 (chapter 45, Administration): 3 citing documents. `vt-ads-cybersecurity-standard-2023-01`: "a)   3 V.S.A. § 2283(b)            b)   3 V.S.A. § 2222(a)"

Out of scope or not worth a seed entry: 18 instruments; most cited: 1 V.S.A. 317 (2 documents); 2 V.S.A. 20 (2 documents); 32 V.S.A. 1010 (2 documents).

### virginia

**Section slice of a non-IT chapter**

- Va. Code 2.2-603 (agency heads: IT security incident reporting): 8 citing documents. `va-ea200`: "Code of Virginia, §2.2-603(F)"
- Va. Code 2.2-225 (Secretary of Technology): 4 citing documents. `va-cpm110-05`: "Code of Virginia, §2.2-225 (Powers and duties of the"
- Va. Code 2.2-4303.01 (high-risk contracts): 4 citing documents. `va-buy-it-manual`: "as approvals by the OAG and VITA, in accordance with § 2.2-4303.01. If the procurement is a Cloud"
- Va. Code 2.2-203.2:5 (Secretary of Administration): 1 citing document. `va-cpm112-04-8`: "Code of Virginia § 2.2-203.2:5 (Powers and duties of the"

**Owner scope decision**

- Va. Code 2.2-4300 to 2.2-4304 (Virginia Public Procurement Act core): 12 citing documents. `va-buy-it-manual`: "institution of the Commonwealth (Virginia Code §2.2-4304(C))."
- Va. Code 2.2-4310, 2.2-4343.1, 2.2-2001, 2.2-2000.1 (SWaM preferences): 2 citing documents. `va-buy-it-manual`: "• Any executive branch agency’s goals under § 2.2-4310 of the Code of Virginia for"
- Va. Code 2.2-1115(D): 2 citing documents. `va-ea300-01`: "Code of Virginia, § 2.2-1115 (D) (Procurement                 Executive Branch Agencies"
- Va. Code 2.2-2458 (Information Technology Investment Board): 2 citing documents. `va-gov102-02`: "Code of Virginia, §2.2-2457; §2.2-2458                                     technology plans and technology-related budget"
- Va. Code 2.2-2026, 2.2-2027, 2.2-2423 (VGIN): 2 citing documents. `va-oth702-00`: "Services Program (ISP). Pursuant to § 2.2-2026, Code of Virginia, the VGIN Coordinator"
- Executive Order 19 (2018, cloud) and Executive Order 35 (2019, SWaM): 6 citing documents. `va-buy-it-manual`: "internal procedures consistent with the provisions of the VPPA, Executive Order 35 (2019) and DSBSD"

Out of scope or not worth a seed entry: 112 instruments; most cited: Va. Code 2.2-3700 (6 documents); Va. Code 23.1-1000 (3 documents); Va. Code 8.01-324 (2 documents).

### washington

**Seed whole**

- RCW chapter 19.360 (electronic signatures, governmental affairs): 1 citing document. `wa-sec-11-01-g`: "In accordance with RCW 19.360.020(4), the Washington          Agencies should first determine whether a signature is"

**Section slice of a non-IT chapter**

- WAC 292-110 (292-110-010, use of state resources): 1 citing document. `wa-user-02`: "2.   WAC 292-110-010 - Use of State Resources (Section 4)."
- RCW 38.52.040(4), 38.52.030 (emergency management): 2 citing documents. `wa-rcw-43-105`: "(7) In fulfilling its duties under this section, the agency and the technology services board security subcommittee shall collaborate with the military department and the cybersecurity advisory committee created in RCW 38.52.040(4)."

**Owner scope decision**

- RCW chapter 43.386 (facial recognition; stub): 1 citing document. `wa-data-03`: "16. Chapter 43.386 RCW: Facial Recognition."

**Owner scope decision (new evidence)**

- RCW 43.88.092 (information technology budget detail): 2 citing documents. `wa-rcw-43-105`: "of other institutions of higher education. Institutions of higher education shall provide to the director sufficient data and information on proposed expenditures on business and administrative applications to permit the director to evaluate the proposed expenditures pursuant to RCW 43.88.092(3)."
- Executive Order 25-06 (Transforming Customer Experience): 2 citing documents. `wa-ea-02-07-s`: "Executive Order 25-06 establishes a comprehensive approach to improve customer"
- WAC 434-615, 434-660, 434-662 (Secretary of State records rules): 3 citing documents. `wa-data-01-03-g`: "demonstrate the authenticity, maintain the chain of custody, and help protect the evidentiary value of the record (WAC 434-662-060)."
- RCW chapter 39.26 (state procurement): 4 citing documents. `wa-ea-03`: "2. If granted, an Innovation exemption exempts a state agency, from adherence to public procurement requirements for the purchase of goods and services under chapter 39.26 RCW."

Out of scope or not worth a seed entry: 26 instruments; most cited: RCW chapter 42.56 (9 documents); RCW chapter 43.09 (3 documents); RCW chapter 43.41 (3 documents).

### west-virginia

**Owner scope decision (new evidence)**

- Executive Orders 7-03, 6-06 and 3-17: 23 citing documents. `wv-wveb-p101-2`: "Title XIII, § 13001; W. Va. Code §§ 5A-8-21,22 and 24; Executive Order No. 6-06"
- W. Va. Code 5A-8-21, 5A-8-22, 5A-8-24 (limits on release of personal information): 1 citing document. `wv-wveb-p101-2`: "Title XIII, § 13001; W. Va. Code §§ 5A-8-21,22 and 24; Executive Order No. 6-06"

Out of scope or not worth a seed entry: 4 instruments; most cited: W. Va. Code 14-2-1 (1 document); W. Va. Code 29-6-1 (1 document); W. Va. Code 5A-8-1 (1 document).

### wisconsin

**Seed whole**

- Executive Order 184 (stub) (not in the tool's output): 1 citing document. `wi-det-it-security-standards-handbook`: "Pursuant to Governor Evers’ Executive Order #184, the Removal of Prohibited Foreign Products"

**Section slice of a non-IT chapter**

- Wis. Stat. 16.705, 16.71 (purchasing subchapter; read in the held IT statutes) (not in the tool's output): 2 citing documents. `wi-stat-16-973`: "greater than $1,000,000, and require each executive branch agency authorized under s. 16.71 (1m) to enter into a contract for materials, supplies, equipment, or contractual services relating to information technology to include in each contract with a vendor of information"
- Wis. Stat. 16.61 (stub; records retention): 2 citing documents. `wi-det-it-security-policy-handbook`: "• Records retention obligations of state agencies Wis. Stat. § 16.61 defined in Wis. Stat. § 16.61(2)(b)."

**Owner scope decision (new evidence)**

- Wis. Stat. 16.754, 16.70 (purchasing subchapter): 2 citing documents. `wi-det-it-security-policy-handbook`: "Compliance References    • Wis. Stat. § 16.754"
- Wis. Stat. 19.62 and chapter 19 subchapter IV (personal information practices): 2 citing documents. `wi-det-it-security-policy-handbook`: "• PII (Personally Identifiable Information): Wis. Stat. § 19.62(5) defines personally identifiable"

Out of scope or not worth a seed entry: 3 instruments; most cited: Wis. Stat. chapter 19 (1 document); Wis. Stat. 146.816 (1 document); Wis. Stat. 19.32 (1 document).

### wyoming

**Section slice of a non-IT chapter**

- W.S. 40-21-101 to 40-21-119 (Uniform Electronic Transactions Act) (not in the tool's output): 4 citing documents. `wy-wyit-1001`: "● Wyoming §§ 40-21-101 — 40-21-119"

**Owner scope decision**

- W.S. 16-4-201 to 16-4-205 (Public Records Act): 12 citing documents. `wy-wyit-2001-g2`: "1.3.7.​   Public disclosure requirements under W.S. §16-4-201 through §16-4-205);"

Out of scope or not worth a seed entry: 7 instruments; most cited: W.S. 9-2-1013 (1 document); W.S. 1-39-101 (1 document); W.S. 7-19-106 (1 document).

## Cross-state patterns

Counts below are over the 147 candidates listed above (not-in-force items excluded); one candidate may group several sections of one law, and "citing documents" is summed over candidates.

| kind of non-IT law | candidates | states | citing documents |
|---|---:|---:|---:|
| procurement | 32 | 18 | 77 |
| records and public records | 18 | 18 | 56 |
| organization | 11 | 9 | 30 |
| budget | 9 | 9 | 19 |
| e-signature | 9 | 9 | 14 |
| privacy | 9 | 8 | 25 |
| personnel | 7 | 6 | 12 |
| accessibility | 5 | 5 | 12 |
| definition | 4 | 4 | 24 |
| emergency | 3 | 3 | 4 |

Candidates that are IT instruments or IT-adjacent rather than a non-IT chapter: IT order (16 in 13 states), IT rule (6 in 4 states), AI (4 in 2 states), other (4 in 4 states), security (3 in 3 states), data (2 in 2 states), geospatial (2 in 2 states), health (2 in 2 states), IT statute (1 in 1 states).

By class: seed whole 15 candidates in 11 states; section slice 42 in 25; owner scope decision 51 in 27; owner scope decision (new evidence) 39 in 19. 32 candidates are not in the tool's output at all (found by searching the documents for forms the tool does not read).

What the counts support:

- **Procurement law is the most-cited non-IT chapter**: 32 candidates in 18 states. The IT statutes and policies in those states run their purchasing through a few named sections of the general procurement code (for example Louisiana 39:1594, 1595 and 1600.2; Nebraska 81-1117 and 81-1120.17 and .20; Oklahoma 74 O.S. 85.5; Virginia 2.2-4303.01). One rule for slicing procurement law would settle 32 candidates.
- **Records management and public records come next**: 18 candidates in 18 states (for example Arizona 41-151, Delaware 29 Del. C. 501 to 526, Minnesota 138.17, Nebraska 84-1201 to 84-1228, Texas 441.185, Wyoming 16-4-201 to 205). It is one decision, not 18.
- **Electronic-transactions law** (the Uniform Electronic Transactions Act and its neighbours) is cited by held IT documents in 9 states; the seed has already left it out of Colorado as general public-records, records and e-signature law.
- **Orders are the clearest gap among the IT instruments themselves**: orders the held documents say they implement (California B-1-11 and D-3-99, Maryland 01.01.2017.22, Michigan 1994-13, Pennsylvania 2011-05 and 2004-8, West Virginia 7-03, 6-06 and 3-17) are not held; for each, an in-force check comes before any seed entry.
- **A policy library built on a lapsed order** is a finding of its own, not a missing instrument: Idaho (below).
- **The statute-to-statute half is mostly noise where it is read**: Minnesota alone has 955 not-held statute citations, 949 of them one statute citing another by bare number (mostly in a definition or a data classification). They are counted, and only the few that name an IT funding or procurement rule are listed.

## What the owner must decide

1. **Section slicing of non-IT chapters.** One decision for procurement law (32 candidates, 18 states) and one for records and public records (18 candidates, 18 states) settle most of this document. Until they are made, the "section slice" candidates stay unseeded.
2. **The 39 "new evidence" items.** The seed already holds an owner decision or a left-out reason for each; held documents (often several) are built on them. Reverse the reasons or confirm them.
3. **The 15 "seed whole" candidates.** Approve or decline each seed entry. Nothing was fetched or read, so none is verified, and each order needs an in-force check first.
4. **Idaho: are the ITA policies that rest on a lapsed order still in force?** Orders issued before 2019 lapsed by 2022 (the seed records this), and id-ita-p1040, id-ita-p1050 and id-ita-p1060 print Executive Order 2005-22 in their Authority sections or revision history. This is a spec rule 6 question about held documents, not a missing-material question.
5. **Scope-defining definition sections** (Iowa 8A.101, Kentucky 11.080, Louisiana 36:3 and 39:2, California Gov. Code 11000): whether a one-section definition of "agency" in a non-IT chapter is ever mirrored. One rule for all.
6. **Whether to extend the bare-number reader** to the states where it is not read (recall table above). It costs a per-state review of false positives and surfaces statute cross-references, most of them out of scope.
7. **Not-in-force citations** (Idaho 2005-22, 2006-05 and 2001-07, Iowa 8A.204): no seed entry; whether the documents that still cite them should be flagged is the owner's call.

## Owner decisions, 2026-11-13

1. **Procurement provisions and records-retention provisions tied to state IT are in scope.** IT provisions inside procurement law and records-retention law may be seeded as section slices. Widened the same day: "I approve the other adjacent subjects as long as its focus is regarding the governance of IT". So a provision in any non-IT chapter (budget, organization, records, e-signature, privacy, accessibility and the like) may be seeded as a section slice when the provision's own focus is the governance of state IT; a general provision that merely also applies to IT is not approved.
2. **The 15 "seed whole" candidates are approved** for verification against the official source and ingest.
3. **Idaho:** the three ITA policies that rest on the lapsed Executive Order 2005-22 (`id-ita-p1040`, `id-ita-p1050`, `id-ita-p1060`) are treated as not in force.
4. **No gate.** `src/authority_refs.py --check` is not run by `scripts/gates.sh` or CI, and `scripts/regen.sh` does not rebuild `_meta/eval/authority-refs.json`. The JSON is a dated result; re-run the tool to refresh it.

The other items under "What the owner must decide" are still open. Nothing in this PR acts on decisions 1 to 3; that work follows in its own PR.

## Reproduce

```
python3 src/authority_refs.py --table      # the per-state table
python3 src/authority_refs.py --check      # the committed JSON is what the documents give
python3 -m pytest tests/test_authority_refs.py tests/test_authority_refs_review.py -q
```

The candidate lists were built from the JSON (`not_held`, `stub` and `left_out` items, each with its citing documents and verbatim quotes) and, where the tool does not read the form, from a search of the documents. The class of each was judged from the citing line alone and is UNVERIFIED.
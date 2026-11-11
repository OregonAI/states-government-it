# 04 — Oregon search trial against the 20 analyst questions

Run 2026-11-10 against the 43 Oregon documents committed on branch `night/pilot-states` (issue #3). Questions: `03-domain-taxonomy.md` section 5.

## Read this first: the trial was KEYWORD-ONLY

No semantic search was run. The toolkit (`corpus_toolkit.semantic`) builds an embeddings artifact with `sentence-transformers` (BAAI/bge-m3), `model2vec` or a remote embedder service. In this environment `.venv` has none of `torch`, `sentence_transformers` or `model2vec`, and nothing may be installed. Model files exist in `~/.cache/huggingface` but cannot be loaded without those packages. The toolkit's only dependency-free embedder is a character n-gram hasher that its own docstring says is "NOT semantic", so building it would not test semantic search. `_meta/corpus.yml` has no `semantic_search_module` either, so `mode="hybrid"` returns exactly the keyword result. I confirmed this: every hybrid probe returned the identical list.

Method: `CorpusFramework(config).search_corpus(query, limit=6, mode="keyword")`, called directly (no network server). For each question I ran two queries: the analyst's question reduced to its key words, and a second query using the wording I found in the Oregon text. The second query is an informed query: I read the corpus first, so it shows what the index can find, not what an analyst would type cold. Expected documents were found by reading the corpus (regex over the document files), with the passage quoted or located. Document ids are the `or-...` ids; `ors-276a` is `or-ors-276a`, `oar-128-30` is `or-oar-128-30`, `107-004-nnn` is `or-das-107-004-nnn`.

How the keyword search behaves, which drives most results below:

- **All terms must match (AND), after stemming.** Any query of more than about three words that is not a phrase in one document returns nothing. "GovRAMP FedRAMP StateRAMP" returns nothing, while each word alone returns the right document (`GovRAMP` -> attachment-g, `FedRAMP` -> 107-004-150, `StateRAMP` -> it-control-standards).
- **Stemming over-matches.** "accessibility" returns documents that only say "access" (107-004-140, 107-004-110, ...).
- **No synonyms.** "inventory of AI systems" misses the "Statewide AI Registry"; "chargeback" matches nothing.

Result: of 20 questions, a first-attempt analyst-style query returned an expected document for 4 (questions 5, 6, 11, 12) and no results at all for 13; the informed second query returned at least one expected document for 17. Questions 4 and 9 have no instrument in the corpus that answers them as asked, and question 17 has none at all.

## Per question

Verdicts: **Yes** = every expected document in the corpus returned; **Partial** = some did; **No** = none, or no expected document exists in the corpus.

### 1. To whom does the state CIO report?
- Query 1 `state CIO reports to governor board agency head`: no results. Query 2 `Governor shall appoint the State Chief Information Officer`: `ors-276a`.
- Expected: `ors-276a`, 276A.203(2): "The Governor shall appoint the State Chief Information Officer, who serves at the pleasure of the Governor." Also 276A.203(4)(a)(A): "Serve as the Governor's chief advisor concerning information resources...".
- **Yes** with the informed query; the analyst-style query failed (AND).

### 2. Decentralized vs unified IT; what is consolidated?
- Q1 `decentralized unified IT consolidation infrastructure services staff`: none. Q2 `consolidation of agency information technology security functions`: `ors-276a`.
- Expected: `ors-276a` 276A.323(2)(b) ("the unification of agency information technology security functions"); `107-004-052` ("a unified and coherent statewide cyber and information security program"); `eis-memo-20241028-css-directive`; `eis-memo-20220812-cloud` (cloud brokering, "consolidation"); and EO 16-13 "Unifying Cyber Security in Oregon" (stub, no text).
- **Partial.** Only the statute came back. The single word `unified` returns the css directive and 107-004-052, so recall depends on guessing the document's word.

### 3. Is the CISO's authority set by statute, rule, EO, directive or agreement?
- Q1 `CISO authority statute rule executive order directive`: none. Q2 `State Chief Information Security Officer`: `ors-276a, oar-128-20, 107-004-155, oar-128-30, 107-004-052, eis-memo-20241028-css-directive`.
- Expected: `oar-128-30` ("The Department will designate a State Chief Information Security Officer to manage and promote information security across the agencies of state government"); `ors-276a` 276A.300(2) (security authority is the State CIO's, and the statute never names a CISO); `107-004-052` and `107-004-120` (policy; CISO receives non-compliance transmittals and develops partnerships); the CSS directive memo (signed by the CISO). EO 16-13 is a stub.
- **Yes** for the informed query (`107-004-120` is lower than rank 6 but matches the same phrase). The question is answerable from the corpus only by reading: rule and policy name the CISO, the statute vests authority in the CIO.

### 4. Statute establishing the enterprise CISO role; funded?
- Q1 `statute establishing enterprise CISO role funded`: none. Q2 `Chief Information Security Officer`: `oar-128-20, ors-276a, 107-004-155, oar-128-30, 107-004-052, css-directive`.
- Correct answer from the corpus: no statute. `ors-276a` contains the phrase "Chief Information Security Officer" zero times; the role is created by OAR 128-030 (passage above). Funding is not stated in any document held; 276A.209 funds the State CIO's office generally.
- **No expected statute exists; the right documents (`oar-128-30`, `107-004-052`) came back.** A reader still has to infer "no statute" from absence.

### 5. Which entities do the data-security statutes cover?
- Q1 `data security statutes cover executive agencies local governments contractors`: `ors-276a, it-control-standards`. Q2 `executive department information systems security`: `oar-128-30, ors-276a, 107-004-190, 107-004-052, 107-004-180, 107-004-120`.
- Expected: `ors-276a` 276A.300(1)(a) ("Executive department" per ORS 174.112), 276A.303 (Secretary of State, Treasurer, Attorney General), 276A.323(1)(a) (excludes SoS, Treasurer, AG, Lottery, public universities). `107-004-052` covers contractors as "users".
- **Yes.**

### 6. Training, risk assessments, incident response plans required?
- Q1 `agencies must security awareness training risk assessment incident response plan`: `107-004-052, privacy-guidance, it-control-standards, oar-128-30, 107-004-120, 107-004-190`. Q2 `annual information technology security awareness training`: `it-control-standards, 107-004-052, privacy-guidance, 107-004-190, ors-276a`.
- Expected: `ors-276a` 276A.323(2)(c) ("Conduct and document the completion of annual information technology security awareness training for all agency employees") and 276A.306 (assessments); `107-004-052` and `-052-pr` ("Complete annual cybersecurity training by December 31 of each year"); `107-004-120` (agency incident response plan).
- **Yes** (statute lands at rank 5 in Q2 and is missed by Q1; `107-004-052-pr` missed).

### 7. Must the CIO approve agency cloud acquisitions; security review?
- Q1 `CIO approve agency cloud acquisition pre-acquisition security review`: none. Q2 `cloud services exception authorized by the State CIO`: `eis-memo-20220812-cloud, 107-004-150, 107-004-130, it-control-standards, ors-276a`.
- Expected: `eis-memo-20220812-cloud` ("any current and future needs and use of public cloud services must utilize the EIS Cloud Service unless an exception has been authorized by the State CIO"); `107-004-150` and `-150-pr` (Cloud and Hosted Systems Workbook, submitted to the State CIO, with a Section B security review for significant-risk investments).
- **Partial** (`107-004-150-pr` missed by Q2; Q1 failed).

### 8. How is central IT funded?
- Q1 `central IT funding chargeback general fund assessment`: none. Q2 `allocate costs to state agencies information technology services`: `ors-276a, 107-004-150`.
- Expected: `ors-276a` 276A.323(3) ("The State Chief Information Officer shall determine and allocate the costs to state agencies associated with providing information technology services, third-party security evaluations...") and 276A.209 (State IT Operating Fund: appropriations, continuously appropriated). Neither says "chargeback".
- **Yes** with the informed query. The word `chargeback` appears in no document, so an analyst using the question's vocabulary finds nothing. A fuller answer (rates) would need DAS rate publications, not in the seed list.

### 9. Definition of an "information technology procurement"
- Q1 `definition information technology procurement`: `107-004-150-pr, 107-004-030, oar-128-30, 107-004-030-pr, 107-004-150, 107-004-130-pr`. Q2 `information technology includes hardware software services data processing`: `oar-128-20, 107-004-155, 107-004-130, 107-004-110, ors-276a, budget-categories`.
- Expected: no Oregon instrument held defines the term. The nearest is `ors-276a` 276A.230(2): "Information technology includes, but is not limited to, all present and future forms of hardware, software and services for data processing, office automation and telecommunications" (a definition of IT, not of procurement). The procurement statutes (ORS 279A.050, 279B.030, 291.047) were left out of the seed list as an owner decision.
- **No.** The statute definition is retrievable (rank 5) but the question's real answer sits in instruments not seeded. Seed-list gap.

### 10. AI system inventories: scope, frequency, published?
- Q1 `inventory of agency AI systems high-risk published`: none. Q2 `statewide registry AI-using applications`: `107-004-190`.
- Expected: `107-004-190`, "Statewide AI Registry": "The State CIO or their designee will oversee the creation and maintenance of a statewide registry of all AI-using applications in use or development by state agencies, including details on their uses, as part of an enterprise application portfolio management system." Covers all uses; the passage states no update frequency and no publication.
- **Yes** only for the informed wording. "inventory" does not find "registry" (no synonyms); a semantic index would be expected to.

### 11. Impact assessments before deploying AI; who reviews?
- Q1 `impact assessment before deploying AI who reviews`: `attachment-b, ors-276a`. Q2 `AI Use Form risk evaluation higher-risk`: `107-004-190-pr, attachment-b`.
- Expected: `107-004-190-pr` (agency applies the AI Risk Management Framework, submits the AI Use Form with the IT investment intake; "EIS Initial review by EIS"; EIS prescribes extra requirements for higher-risk uses); `attachment-b` ("Initial Risk Evaluation: Completion of the AI Use Form"); `107-004-190`; `attachment-g` (higher-risk requirements). The Use Form itself (Attachment C, docx) is not held.
- **Partial** (`107-004-190`, `attachment-g` not returned).

### 12. Definition of "artificial intelligence"; federal borrowing?
- Q1 `definition of artificial intelligence federal definition`: `107-004-155, oar-128-20, ors-276a, privacy-guidance`. Q2 `artificial intelligence means a machine-based system`: `oar-128-20, 107-004-200, 107-004-190, ors-276a`.
- Expected: `ors-276a` 276A.340(1) ("a machine-based system that is capable, for a given set of human-defined objectives, of making predictions, recommendations or decisions influencing real or virtual environments and uses machine- or human-based inputs to..."), and the same wording in `107-004-155`, `-190`, `-200`. Whether it is the federal definition cannot be shown from the corpus: none of these texts cites a federal statute. UNVERIFIED (not checked at a federal source tonight).
- **Yes.**

### 13. What body governs state AI use?
- Q1 `body governing state AI use council task force chief AI officer`: none. Q2 `Enterprise AI Advisory Committee`: `107-004-190, ors-276a`.
- Expected: `107-004-190`: "The State CIO will establish an Enterprise AI Advisory Committee comprised of representatives from EIS and executive branch agencies and chaired by the State CIO or designee. The committee will serve as advisory to EIS and the State CIO." Also EO 23-26 (State Government AI Advisory Council) which is a **stub with no text**; `attachment-b` cites the Council's recommendations.
- **Partial.** The EO that created the earlier Council cannot be searched.

### 14. Is AI policy set by statute, EO, rule or CIO guideline?
- Q1 `AI policy set by statute executive order rule guideline`: none. Q2 `Responsible Artificial Intelligence Usage policy`: `107-004-190-pr, 107-004-190, 107-004-200-pr, 107-004-200, attachment-b, attachment-e`.
- Expected: all four layers exist: CIO policy (`107-004-190`, `-200`), statute (`ors-276a` 276A.340-.348, covered AI products), rule (`oar-128-20`), and EOs 23-26 and 26-26 (stubs).
- **Partial.** Policy returned; statute and rule not surfaced by this query; both EOs absent (stubs).

### 15. AI procurement terms and vendor disclosure
- Q1 `AI procurement terms vendor disclosure`: `ors-276a` (noise). Q2 `vendor zero data retention attestation third-party certification AI`: `attachment-g`.
- Expected: `attachment-g`, section 5 "Vendor Compliance": "Vendors must agree to Zero Data Retention (ZDR) on AI processing and provide third-party attestation/certification (e.g. GovRAMP)... require breach notification within 24 hours... grant audit rights"; EO 26-26 "Responsible Artificial Intelligence Procurement Standards" (stub).
- **Partial.** Found only by guessing the document's terms; the EO is missing.

### 16. AI-only adverse decisions; public disclosure of AI use
- Q1 `restrict AI-only adverse decisions public disclosure of AI use`: none. Q2 `human in the loop user disclosure mechanism`: `107-004-190-pr, 107-004-190, attachment-b`.
- Expected: `107-004-190` principle "Human Oversight and Review... AI must not replace subject matter expertise"; and the "Exclusions" passage (non-GenAI automated decision systems are outside the policy); `107-004-190-pr` requires a "User disclosure mechanism"; `attachment-d` (User disclosure mechanism) and `attachment-f` (Human in the loop documentation). No instrument held restricts AI-only adverse decisions in terms.
- **Partial.** `attachment-d` and `attachment-f`, whose titles are exactly these phrases, were not returned (the query's other words were not all present in them).

### 17. Technology accessibility coordinator; vendor verification
- Q1 `technology accessibility coordinator vendor accessibility compliance`: `107-004-015-pr, oar-128-30, ors-276a, 107-004-052, open-data-standard, it-control-standards`. Q2 `accessibility information technology`: `ors-276a, 107-004-155, 107-004-052, oar-128-20, zscaler memo, deepseek memo`.
- Expected: none in the corpus. Every hit is stemming noise ("access", "coordinator" of unrelated things); the only on-topic words are a risk line in `attachment-b` ("Ensure AI systems comply with applicable accessibility standards").
- **No.** Seed-list gap: no accessibility instrument was seeded. I did not research whether Oregon has one tonight.

### 18. Disaster recovery: centralized, federated or agency?
- Q1 `disaster recovery centralized federated agencies`: none. Q2 `business continuity disaster recovery plan agency`: `107-004-150, it-control-standards`.
- Expected: `107-004-150`: "Business continuity and disaster recovery: Agencies must document their business continuity (BC) and disaster recovery (DR) needs, and must develop plans and Service Contract terms to meet those needs" (agency-level for cloud services); `it-control-standards` (contingency planning controls). No statewide DR instrument is held.
- **Yes**, but the corpus answers only the cloud-service slice. Whether the State Data Center provides central DR is not in any seeded document.

### 19. Services to local governments (whole-of-state)
- Q1 `services to local governments whole-of-state cybersecurity`: none. Q2 `Oregon Cybersecurity Center of Excellence public bodies local governments`: `ors-276a`.
- Expected: `ors-276a` 276A.555(2)(e): the center coordinates, funds or provides "Cybersecurity-related goods and services to Oregon public bodies, with priority given to local governments, regional governments, special districts, education service districts, school districts and libraries"; 276A.560 (Advisory Council); `107-004-120` (the CISO "develops partnerships and engages with the Oregon Cybersecurity Advisory Council, regional and local governments").
- **Partial.** `107-004-120` was not returned.

### 20. GovRAMP for cloud purchases
- Q1 `GovRAMP authorization cloud purchases`: none. Q2 `GovRAMP FedRAMP StateRAMP`: none.
- Expected: `attachment-g` (GovRAMP attestation, vendor compliance); `107-004-150` ("the state frequently accepts a SOC2 Type 2 audit... Other types of audits or certifications, such as FedRAMP, may also be acceptable"); `it-control-standards` (cites StateRAMP baselines as a reference). Each term alone finds one document: `GovRAMP` -> attachment-g, `FedRAMP` -> 107-004-150, `StateRAMP` -> it-control-standards.
- **No** for both multi-word queries; the documents exist. This is the clearest AND-search failure.

## What the trial revealed

### Seed-list gaps (not fixed tonight; each needs an owner decision or discovery)
1. **Three executive orders are stubs (EO 16-13, 23-26, 26-26).** They are the expected answers for questions 2, 3, 13, 14, 15. They are scans with no text layer; OCR tools (`tesseract`, `ocrmypdf`) are on this machine but the ingester has no OCR step and the seed list says the two-engine OCR procedure has not been run. Four policies are stubs for the same reason (107-004-051, -053, -100 and the 2026-04-20 107-004-052 update memo).
2. **Procurement statutes left out** (ORS 279A.050, 279B.030(4), 291.047, ...) by owner decision: they are the answer source for question 9 and part of 7 and 15.
3. **Attachment C (AI Use Form) and A (AI adoption template), docx**: left out; relevant to questions 10 and 11.
4. **No accessibility instrument** (question 17) and **no statewide disaster-recovery or State Data Center service instrument** (question 18). Not researched tonight.
5. **No funding or rates instrument** (question 8): only the statute's allocation clause is held.
6. **No Oregon legislation or session-law instrument on AI** beyond ORS 276A.340-.348; none was looked for tonight.

### Ingest defects
1. **Fixed: PDF ligature glyphs.** `pdftotext` wrote U+FB01 and its relatives into 7 documents (173 occurrences in `or-eis-privacy-guidance`, 29 in `attachment-b`, 22 in `attachment-g`), so `definition`/`configured`/`findings` were unsearchable in them (a search for `deﬁnition` found them and `definition` did not). `pdf_to_text` now writes the letters, with a test on a real PDF fixture. Documents re-derived offline from the committed snapshots; the PDF `conversion_notes` sentence now says so (a one-line change in every PDF document). Gates pass.
2. **Not fixed: the document body for PDFs keeps layout columns and page furniture** (by design, "removing furniture would be editing the instrument"). Search snippets from policy tables are hard to read as a result. No defect, noted only.

### Toolkit behaviour the owner should know (file in `OregonAI/corpus-toolkit`; not filed tonight)
1. Keyword mode is all-terms-AND with no fallback, so natural-language questions return nothing (13 of 20 first queries returned nothing). A relaxed fallback (OR with ranking) is needed before analysts can use it unaided.
2. `mode="hybrid"` silently equals keyword when no semantic module is configured, and the hit carries no field saying so; a caller cannot tell.
3. Stemming is aggressive enough to equate "accessibility" with "access".
4. `corpus.yml` has no `semantic_search_module` and no embeddings artifact exists; the semantic half of the trial is still to do on the GPU machine.

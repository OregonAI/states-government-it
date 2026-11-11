# Colorado: OIT's live pages against the August archive copy (2026-11-11)

Measured 2026-11-11 with the toolkit `Fetcher` at toolkit v1.37.0 (through PYTHONPATH; the gate and CI stay on the v1.36.4 pin and
read committed snapshots only). v1.37.0's default User-Agent is `Mozilla/5.0 (compatible; OregonAI-CivicCorpus/<version>;
+https://github.com/OregonAI/<repo>)` (toolkit ADR-0019). No other identity, client or endpoint was used. It supersedes the
Colorado OIT section of `07-colorado-ccr-and-oit.md`, which says the site answered HTTP 403; leave `07` as written.

## What changed

The version token in that string is read from the installed package metadata, so under PYTHONPATH=toolkit v1.37.0 the
live requests sent `OregonAI-CivicCorpus/1.36.4` while running v1.37.0 code (measured 2026-11-11); the firewall accepts it, and
`tests/test_fetch_identity.py` checks the identity through `src.ingest.make_fetcher` at both versions.

colorado.gov's shared firewall answered the old default User-Agent with HTTP 403 and answers the crawler-form one with 200.
`https://oit.colorado.gov/robots.txt` answered 200 (text/plain, 2,027 bytes) to the first Fetcher request. Every page below
answered 200 to the Fetcher, as did `www.colorado.gov/governor` and its year pages. `governor.colorado.gov` did not answer
(ConnectTimeout, one request).

## The live pages against the August copy (Wayback 20260822055824)

- The old index was ONE page ("Technical Standards & Policies") that listed everything and linked 54 ServiceHub articles (ServiceNow,
  script-rendered). The live site splits it: `/standards-policies-guides` (section front), `/standards-policies-guides/technical-standards`
  (the older address `.../technical-standards-policies` serves the same page, byte for byte), `/policies-governance`, and
  `/standards-policies-guides/general-oit-rules-information`. **None of them links a ServiceHub article for a policy, standard or
  procedure.** Each listed instrument is a Google Drive PDF (`drive.google.com/file/d/<id>/view?usp=sharing`).
- Counts on the live pages: 41 technical standards, 10 policies, 3 procedures (54 Drive files; coincidentally the number of lead-stubs).
  Fetched through Drive's download form (`drive.google.com/uc?export=download&id=<id>`, which redirects to
  `drive.usercontent.google.com`) all 54 are text PDFs, and every one opens with a header table (Document ID, Title, Issuing Authority,
  Version, Effective Date, Last Updated), except the eSignature guidelines and POL 100-51.
- Of the 54 earlier lead-stubs, 49 are on the live pages. Five are not: TS-APP-003, TS-APP-004, TS-APP-006, TS-INF-004, TS-OIT-006. The
  live page says its standards supersede "any standards posted prior" and lists only TS-APP-005, -009, -010, -011.
- The old stubs' titles were wrong in places: nine differ from the PDF's own Title (e.g. the stub for TS-CISO-004 was titled "Patch
  Management Standard v2026"; TS-CISO-004 is the OIT Firewall Design Standard, and the patch standard is TS-CISO-005).
- New on the live pages and not in the August stub list: TS-CISO-005 Patch Management, TS-CISO-007 Server Hardening, the Enterprise IT
  Change Management Policy (POL-OIT-001) and POL 100-51 (OIT Internal Policies).
- Gone from the live pages although in the August copy: the OIT Authority & Governance Operations Memorandum and the Vendor Selection
  Standard for Major IT Projects (OIT-FinSvc-100); the "Archived" CISP sets and POL 200-01 / 200-02 sections. The two Drive files still
  download and their text is unchanged (compared with the committed snapshots), so the pages dropped them without any statement that they
  were withdrawn. They are removed from the corpus (in force only) and recorded in the seed list's left-out record; restoring them is a revert.
- The eSignature guidelines are still listed, under Current Statewide Policies, Enterprise Governance, as "eSignature Guidelines for State
  Agencies" (same Drive id as before). The PDF is unchanged in text and prints no Issuing Authority; it names OIT once. OIT lists it as a
  current statewide policy, so it stays, with the issuing body the PDF prints.
- The Statewide GenAI Policy is now the Drive PDF POL-AI-001 (version 2.0, effective 09/17/2024, last updated 04/01/2026) on the Policies page.
  The Guide to Artificial Intelligence pages (including the Strategic Approach page) still link a ServiceHub article, KB0012606; the
  Statewide GenAI Agency Responsibilities page is a readable web page (it was a 403). It is a sub-page of the Guide, which the section page
  calls "Practical Help", with must-directives like its siblings; all the Guide's sub-pages are treated alike and left out (OWNER DECISION).
- Three PDFs call themselves a draft on their own header table while the page lists them as issued: TS-APP-010 and TS-INF-010 print version
  "3.01 (Draft)", and TS-DBS-001 prints version 4.01 with Last Updated "Not documented (Draft)". All three are stubs (OWNER DECISION): the
  ingester refuses a Draft on the Version row or the Last Updated row alike (in force only, spec rule 6).
- The Drive PDFs are re-rendered by Google Docs on each download: the byte hash changes while the text does not (the three files held
  before had new hashes and identical text). Hash-only drift checks will report them changed every time.
- The rules page lists the same five OIT rules (8 CCR 1501-5, -7, -9, -11, -12) as the seed list. The Secretary of State's page for 1501-5 shows
  06/30/2026 as the current version, the one held.

## Executive orders

`www.colorado.gov/governor/executive-orders` links one page per year, 2019 to 2026; each row is an order number, date, title and a Google
Drive PDF. 869 rows were read by title. Candidates on state IT, cybersecurity, data or AI: B 2019 013 (Colorado Digital ID; in scope, in force
by the record; its PDF's text layer holds every word twice, so it is a stub: the two-engine OCR run on 2026-11-11 reached 94% word agreement but
only 85% figure agreement of 46 against a bar of 90%, 87% with tesseract mode 4 and 82% with mode 6, so it stays a stub), D 2026 022 (a cybersecurity education pathway; left out, owner
decision), the broadband orders (out of scope) and fifteen election-cybersecurity National Guard activations (out of scope). No order on state
AI or data governance was found. `spl.cde.state.co.us` was not retried.

## Left for the owner

The seed list's comments carry each case: the Glossary of Terms (incorporated by reference into every instrument; fetched, no ingester),
the guide pages with directives (Individual User Responsibilities; Approved & Prohibited GenAI Tools; Statewide GenAI Agency Responsibilities), D 2026 022, TS-DBS-001, and the removal of
the two documents the live pages no longer list.

# Changelog — State Government IT Governance

Keep a Changelog format; ISO dates. Change types: Added, Source-Updated,
Superseded, Repealed, Removed, Verified, Fixed, Security.
Repo-curation dates only — official effective dates live in frontmatter.

## [Unreleased]

### Source-Updated
- Colorado OIT rebuilt from OIT's live pages (they answer the Fetcher under toolkit v1.37.0's User-Agent): the 54 ServiceHub lead-stubs are replaced by the 54 Google Drive PDFs the live pages list (51 documents, among them the eSignature guidelines kept from before; 2 stubs for versions the files call Draft; 1 left out as not IT); the OIT Authority & Governance Memorandum and the Vendor Selection Standard are no longer listed and are removed; the Statewide GenAI Agency Responsibilities page is a document; Colorado executive order B 2019 013 is a stub; four watch entries for OIT's index pages and two for the Governor's order lists; research note 09. The Fetcher-identity test accepts the v1.36.4 and v1.37.0 User-Agents.

### Fixed
- OCR gates: figure agreement between the engines must be 0.90 (Oregon EO 16-13 read 0.75 with its paragraph numbers dropped and is a stub again); `--check` requires the re-run's words and figures to equal the committed text's (an edited figure no longer passes with its hash updated); every position where the engines disagree is recorded in `<id>.ocr.json` and the curator notes; DAS policies are read by rows (`ocr_psm: 4`) and signature glyphs are not committed.
- Word files print their review date, cover date or revision history as `source_version` (DES clauses, SIMM 5310-C, Oregon Attachment A); Attachment A's title is the one its cover prints; CDT form stubs say what each holds; the WA EA-01-01-S stub reason no longer claims curl.

### Added
- 14 documents from Word files (WaTech x10, DES, CDT SIMM 18B and 5310-C, Oregon AI Attachment A) and 7 from scanned PDFs read by the two-engine OCR procedure (Oregon EO 23-26, 26-26, DAS 107-004-051, -053, -100; California EO N-04-19, N-30-25). OCR documents carry `text_source: ocr`. See `docs/research/08-word-files-and-scans.md`.

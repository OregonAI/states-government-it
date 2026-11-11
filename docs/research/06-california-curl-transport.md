# California: the refusal was the client, not the identity (2026-11-11)

Dated 2026-11-11, after `05-california-time-and-difficulty.md`. Everything below was measured with the
toolkit's `Fetcher` (shipped User-Agent, per-host rate limit) on 2026-11-11 unless marked UNVERIFIED.

## Finding

`www.cdt.ca.gov` and `www.gov.ca.gov` answer the toolkit's httpx client with HTTP 403 and
`cf-mitigated: challenge`, and answer system curl 8.5, sending the same User-Agent, with HTTP 200 (pages and PDFs).
`www.genai.ca.gov`, `www.govops.ca.gov` and `oal.ca.gov` answer the same way. So the refusal is scored on the
Python client's connection, not on the declared identity, and `05` was wrong to call these hosts refused. Still
refused, also to curl: `leginfo.legislature.ca.gov` (challenge), `www.sco.ca.gov` (challenge), `www.library.ca.gov`
(HTTP 403, no challenge header).

## What changed

- The ingester asks the Fetcher for its curl transport (`curl_on_challenge=True`, toolkit ADR-0018) when the
  pinned toolkit has it (`make_fetcher`: the signature is read first, so v1.36.4 still imports and runs and a
  challenged host stays a refusal there). Live fetching on this branch used the toolkit branch through PYTHONPATH;
  CI and the gate run at the pin, offline.
- `cdt_html_to_text`: the CDT's Technology Letters from 2021 on and several SIMM sections are web pages (the page is the
  instrument). `check_identity` no longer treats every California policy as a SAM chapter; an executive order PDF is
  identified by its printed heading.
- The seed list was rebuilt from the CDT index pages as fetched: 29 SIMM rows, 84 Technology Letter rows, 31
  Information Technology Policy Letter rows, 20 executive orders. Every title, number, url and status was copied from
  those bytes. Corrections to the first pass, which read them through a summarising tool: Technology Letter 25-06
  (listed, out of scope), 22-01 and 24-02 (no own link on the index; their pages are listed in the CDT's sitemap,
  https://www.cdt.ca.gov/sitemap_index.xml (fetched 2026-11-11), and print the letter number), the SIMM 5300 page's per-standard addresses, SIMM 10, 18, 40A/B, 55A/D, 5305-B, the
  5305-B/C FAQs, 5355-B and 5360-A (web pages), SIMM 150's real title, TL 26-02's date (not a typo).
- Result (after review fixes): 167 California documents (142 new), 71 stubs, 8 watch pages. Stubs by reason: 19 spreadsheets
  (3 of them macro-enabled .xlsm), 16 Word files, 17 forms or templates, 19 other (SIMM 5300-A is not public; the PDFs of N-04-19
  and N-30-25 are scans, N-30-25 from page 2 on; the seven older IT executive orders have no reachable official text; SIMM 17
  is the separate multi-page site https://capmf.cdt.ca.gov/, not one document; SIMM 158 is a page with no instrument text; the
  SIMM 170 exhibits are samples; SIMM 19H's framework PDF is a diagram).
- Executive orders: N-12-23, N-5-26, N-6-26 and N-9-26 are documents (PDFs from www.gov.ca.gov; N-9-26, a
  September 2026 AI oversight order, is not on the CDT list and is seeded because it is an AI instrument); N-04-19 and
  N-30-25 are stubs (scanned PDFs; N-30-25's page 1 has a text layer, pages 2-4 do not, and it was first committed as a
  complete document because the provenance gate compares the text only with what pdftotext produces). The attested copies of N-5-26 and N-9-26 are scans; the signed copies carry a text layer.
  The seven older orders on the CDT list (S-03-10, S-16-04, S-13-04, D-59-02, D-57-02, D-17-00, D-10-99) are stubs: they have no
  reachable official text (the State Library's list answers 403 and loads its table by script).

## Review fixes (2026-11-11)

- `pdf_to_text` refuses a PDF with a page that has no words, unless the seed entry lists the page in `no_text_pages`
  (a figure, a blank page or a scanned form it has looked at); a listed page that has text is refused too. Two older
  documents needed the list: Oregon 107-004-140 (pages 4-7 are scanned attachment forms: still needs OCR) and Washington
  SEC-11-01-G (page 2 blank, page 4 empty).
- Identity: a CDT page is its own first line, a CDT letter PDF carries the number in its header block, any other CDT PDF
  carries its title on the cover and the SIMM section number the cover prints, and an executive order is its heading before
  the first WHEREAS. Checked against every other California CDT/Governor entry's text: 55 of 144 entries used to pass on some
  other document's text; none of the 142 does now (the ITPL 10-09 letter and its FAQs, and five SIMM entries, got a more specific
  identity_text).
- Dates: `effective_date` is the day a letter prints as issued or the day the Governor signed; a month with no day is a
  `source_version`. SIMM PDFs that print their revision history as a table are not read (the cells wrap); their cover month is.

## Still open

- N-04-19 and the attested copies need the two-engine OCR procedure.
- The drift detector has its own transport; it will probably report the CDT and Governor pages as access failures
  until the toolkit gives it the same fallback (UNVERIFIED: drift was not run).
- Time: the ingest of 168 documents ran in about 4 minutes of fetching at the toolkit's rate limit.

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
  (listed, out of scope), 22-01 and 24-02 (no own link on the index; their pages answer at guessed addresses that print
  the letter number), the SIMM 5300 page's per-standard addresses, SIMM 10, 18, 40A/B, 55A/D, 5305-B, the
  5305-B/C FAQs, 5355-B and 5360-A (web pages), SIMM 150's real title, TL 26-02's date (not a typo).
- Result: 168 California documents (143 new), 63 stubs, 8 watch pages. Stubs by reason: 19 spreadsheets, 16 Word
  files, 17 forms or templates, 11 other (SIMM 5300-A is not public; N-04-19's PDF is a scan; SIMM 17 and 158 are pages
  with no instrument text; the SIMM 170 exhibits are samples; SIMM 19H's framework PDF is a diagram).
- Executive orders: N-12-23, N-5-26, N-6-26, N-30-25 and N-9-26 are documents (PDFs from www.gov.ca.gov; N-9-26, a
  September 2026 AI oversight order, is not on the CDT list and is seeded because it is an AI instrument); N-04-19 is a
  stub (a scanned PDF). The attested copies of N-5-26 and N-9-26 are scans; the signed copies carry a text layer.
  The seven older orders on the CDT list (S-03-10, S-16-04, S-13-04, D-59-02, D-57-02, D-17-00, D-10-99) have no
  reachable official text: the State Library's list answers 403 and loads its table by script.

## Still open

- N-04-19 and the attested copies need the two-engine OCR procedure.
- The drift detector has its own transport; it will probably report the CDT and Governor pages as access failures
  until the toolkit gives it the same fallback (UNVERIFIED: drift was not run).
- Time: the ingest of 168 documents ran in about 4 minutes of fetching at the toolkit's rate limit.

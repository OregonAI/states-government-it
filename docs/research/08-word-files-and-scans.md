# Word files and scanned PDFs (2026-11-11)

Measured 2026-11-11 with the toolkit `Fetcher` (shipped User-Agent, rate limit, `curl_on_challenge=True` from the toolkit
branch through PYTHONPATH; the gate and CI run at the v1.36.4 pin). Nothing here was read through WebFetch or a search.

## Word files (.docx)

- `src/ingest.py` reads a `.docx` with pandoc's docx reader into its JSON syntax tree and renders the tree itself: one
  line per paragraph, heading, list item and table row (cells joined by ` | `, as the CDT pages are), footnotes after the
  text. Pandoc's own plain-text writer was not used: its tables are wide grids and its layout changes between releases.
  Headers, footers, pictures and text boxes are not read (Oregon's Attachment A has its cover title in a text box, so the
  title is not in the text; the seed entry carries it).
- **Versions.** The committed text was made with pandoc 3.11 (the maintainer's copy). Ubuntu 24.04, which CI is pinned to,
  packages pandoc 3.1.3+ds-2. I unpacked that package (`apt-get download` and `dpkg -x`, not installed) and re-derived all 14
  Word files with it: the text is byte-identical to 3.11's for every one. `--check` does not rely on that staying true: for
  a Word file it requires the same words in the same order as the committed text (layout may differ), so a changed or
  dropped word fails it and a different line break does not. pandoc missing is a failure, not a pass.
- **Ingested (14):** the DES Generative AI Contract Clauses; ten WaTech library items (EA-01-03-S, EA-03, EA-03-01-S,
  EA 185.10, SEC-04-01-G, DATA-01-02-S, DATA-01-04-G, DATA-02-01-PR, DATA-02-03-S, DATA-02-07-S); CDT SIMM 18B (the
  preparation instructions for the cloud policy exemption request) and SIMM 5310-C (a standard that holds the PTA/PIA
  requirements before its form); Oregon's Attachment A (Agency AI Adoption Strategy Template and Instructions: guidance
  and ten required components, not a blank form).
- **Judged forms or templates and left as stubs (14 California items):** SIMM 15B, 19A.2, 19A.3, 19B.2, 19B.5, 19C.2,
  19D.2, 19E.2, 30B, 45A (an SOW with `<placeholders>`), 45E, 45G, 45H, 50 PIER template. Each is a document an entity
  fills in (entry fields, placeholders, blank outlines). Oregon's Attachment C (AI Use Form: required questions with check
  boxes, submitted to EIS) is a form and is left out; whether forms enter the corpus is the owner's decision.
- **Legacy `.doc` (1):** WaTech EA-01-01-S is a Word 97-2003 binary. pandoc has no reader for it and nothing else is
  installed (no antiword, catdoc or LibreOffice). It stays a stub.

## Scanned PDFs: the two-engine procedure (corpus-template AGENTS.md, "OCR")

- tesseract 5.3.4 through ocrmypdf 15.2.0 (both the Ubuntu 24.04 packages) is the primary engine; PaddleOCR 3.7.0 with
  PP-OCRv6 (orientation classification on) is the cross-check and reads the original scan. docTR, the tiebreaker, was
  not needed. The bars are the platform's: 0.80 word-sequence agreement, 0.80 dictionary ratio (from this corpus's non-OCR
  text), 100 words. A page that tesseract reads as nonsense at its default orientation confidence is read again with
  `--rotate-pages-threshold 0`: EO N-30-25's scanned pages 2-4 are upside down and needed it (agreement 0.995 after).
- **Ingested (8):** Oregon EO 16-13, 23-26, 26-26; DAS 107-004-051, -053, -100; California EO N-04-19 (all four pages
  scanned) and N-30-25 (page 1 has a text layer, pages 2-4 are scans: `ocr: [2, 3, 4]`). Word agreement 0.976-0.998;
  figure agreement 0.75 (EO 16-13) to 1.0, reported in each document's conversion notes.
- **What CI can check.** CI has no PaddleOCR. The second engine's text is committed (`<id>.paddle.txt`) with a report
  (`<id>.ocr.json`: tool versions, the PDF's and both texts' sha256, the scores). `--check` recomputes the agreement from
  the two committed texts, and re-runs tesseract on the committed scan, requiring 0.95 agreement with the committed text.
  An edited text, a swapped second reading, a different PDF, or a text that is not a reading of this scan each fail
  (tests/test_ingest_ocr.py proves each). It does not re-derive the dictionary ratio, which depends on the rest of the
  corpus. It cannot show the text is right: both engines can misread a digit alike, so every document says
  `NOT human-verified`, carries `text_source: ocr`, and leaves `effective_date` and `source_version` empty.
- **Left as stubs or left out:** the 2026-04-20 State CIO memo (read by OCR; overtaken, see the seed list); the 107-004-140
  attachments, pages 4-7 (a blank request form and an agreement with signature blocks); SIMM 19H's one-page diagram (OCR
  gives box labels only).

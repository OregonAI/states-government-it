# src: this domain's ingester and checks

- **Test first.** Write the failing test in `tests/`, watch it fail, then write the code.
  Tests fake the network; the first test file also adds a `unit-tests` job to
  `.github/workflows/ci.yml`.
- **Use the toolkit's primitives:** `Fetcher` for fetching, `record_snapshot` for
  snapshots and hashes, `write_document` for documents. `ingest.py` shows the shared flow.
- **One module per state: `src/states/<state>.py`**, found by name (no registry to edit). It
  defines only the hooks the state needs (`to_text`, `check_identity`, `effective_date`,
  `source_version`, `notes`, `extra_notes`, `snapshot`; the contract is in `src/states/__init__.py`).
  It imports from `ingest_common`, `ingest_docx`, `ingest_ocr`, never from another state or
  `ingest.py`; cleanup two states need moves to `ingest_common.py`. PDFs, Word files and scans are shared.
- **Fetch honestly:** the toolkit's User-Agent and per-host rate limit, as shipped. A
  refusal is an error to report, and the entry becomes a stub.
- **Per-source cleanup lives in the state's `to_text` hook**, one function per source format,
  each with a test built from a real snapshot in `tests/<state>/` (fixtures in `tests/fixtures/<state>/`;
  tests of the shared flow stay in `tests/`). `tests/seedutil.py` writes a temp seed directory.
- **Every generated file has a `--check` mode** and a step in both `scripts/gates.sh` and
  the `generated` job in `ci.yml`, and is rebuilt by `scripts/regen.sh`.
- **`eval_questions.py --check` is the one generated-file check not rebuilt by `regen.sh`:** its baseline is a
  ratchet (a cell that passes may not stop passing), so it is rewritten only by `--write-baseline`, on purpose.
- **A check must be able to fail.** Prove it by running it once against a broken input.
- **Pin every dependency exactly** in `requirements.txt`, with the reason.
- Search, filters, `compare` and `coverage` are toolkit features: build them in
  `OregonAI/corpus-toolkit` and move this repo's pin.

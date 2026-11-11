# src: this domain's ingester and checks

- **Test first.** Write the failing test in `tests/`, watch it fail, then write the code.
  Tests fake the network; the first test file also adds a `unit-tests` job to
  `.github/workflows/ci.yml`.
- **Use the toolkit's primitives:** `Fetcher` for fetching, `record_snapshot` for
  snapshots and hashes, `write_document` for documents. `ingest.py` (built from the toolkit example) shows the
  shape; start from it.
- **Fetch honestly:** the toolkit's User-Agent and per-host rate limit, as shipped. A
  refusal is an error to report, and the entry becomes a stub.
- **Per-source cleanup lives in `to_text`**, one function per source format, each with a
  test built from a real snapshot.
- **Every generated file has a `--check` mode** and a step in both `scripts/gates.sh` and
  the `generated` job in `ci.yml`.
- **A check must be able to fail.** Prove it by running it once against a broken input.
- **Pin every dependency exactly** in `requirements.txt`, with the reason.
- Search, filters, `compare` and `coverage` are toolkit features: build them in
  `OregonAI/corpus-toolkit` and move this repo's pin.

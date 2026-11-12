type: Added

Outside baseline for the 20 analyst questions (issue #9): `docs/research/11-vaquill-baseline.md` runs each question once, as typed, through Vaquill's hosted `search_us_statutes` for Oregon, Washington, California and Colorado (80 calls, 320 credits) and scores it against the same expected documents, with `src/vaquill_baseline.py` (the explicit citation-to-document mapping and the scorer, tested in `tests/test_vaquill_baseline.py`) and the result in `_meta/eval/vaquill-baseline.json` (citations, ranks and scoring only; Vaquill's raw responses are not committed).

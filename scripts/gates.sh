#!/usr/bin/env bash
# The gates CI runs, locally, in one command. Run before every commit.
# A generated file that fails its check here: run scripts/regen.sh.
# NOT run here: the link check (lychee, CI only) and the CODEOWNERS owner lookup.
# Setup once: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
set -uo pipefail
cd "$(dirname "$0")/.."
[ -x .venv/bin/python ] || { echo "no .venv -- see the setup line at the top of this file"; exit 2; }
export PATH="$PWD/.venv/bin:$PATH"

fail=0
run() { echo "== $1"; shift; "$@" || { echo "FAILED: $*"; fail=1; }; }

run "placeholders"   bash -c '! grep -rnoE "\{\{[A-Z_]+\}\}" . --exclude-dir=.git --exclude-dir=.venv --exclude-dir=docs --exclude=corpus.yml --exclude=gates.sh'
run "llms.txt"       bash -c '! grep -q "One annotated link per" llms.txt'
run "llms.txt current"   python3 src/build_llms.py --check
run "changelog current"  python3 src/build_changelog.py --check
run "frontmatter"    corpus-validate-frontmatter --config _meta/corpus.yml
run "provenance"     corpus-verify-provenance --config _meta/corpus.yml
run "graph current"  python3 src/build_graph.py --check
run "status current" corpus-generate-status --config _meta/corpus.yml --output STATUS.md --check
run "seed list"      python3 src/check_seed_list.py --check
run "analyst questions" python3 src/eval_questions.py --check
run "ingest current" python3 src/ingest.py --check
run "codeowners"     python3 .github/scripts/check-codeowners-paths.py
run "ingester loads" python3 -c "import src.ingest, src.states; src.states.modules()"
if ls tests/test_*.py >/dev/null 2>&1; then run "unit tests" python3 -m pytest tests/ -q; fi

[ $fail -eq 0 ] && echo "ALL GATES PASSED" || echo "GATES FAILED"
exit $fail

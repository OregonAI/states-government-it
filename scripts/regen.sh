#!/usr/bin/env bash
# Rebuilds every generated file from what is committed, in one command:
#   _meta/graph.json  STATUS.md  llms.txt  CHANGELOG.md  _meta/eval/authority-refs.json
# Run it after adding or changing documents, and to resolve a rebase conflict in any of those files
# (take either side, run this, `git add -A`, `git rebase --continue`). scripts/gates.sh checks each one.
set -euo pipefail
cd "$(dirname "$0")/.."
[ -x .venv/bin/python ] || { echo "no .venv -- see the setup line at the top of scripts/gates.sh"; exit 2; }
export PATH="$PWD/.venv/bin:$PATH"

python3 src/build_graph.py
corpus-generate-status --config _meta/corpus.yml --output STATUS.md
python3 src/build_llms.py
python3 src/build_changelog.py
python3 src/authority_refs.py

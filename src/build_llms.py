#!/usr/bin/env python3
"""Build llms.txt from _meta/templates/llms.txt, naming the states that are files in _meta/sources/.

  python3 src/build_llms.py           # write llms.txt
  python3 src/build_llms.py --check   # exit 1 if llms.txt is stale
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = "@@STATES@@"


def state_names(seed_dir: Path) -> list[str]:
    """Display names of the states, in name order: `new-york.yml` is New York."""
    return [p.stem.replace("-", " ").title() for p in sorted(Path(seed_dir).glob("*.yml"))]


def render(template: str, seed_dir: Path) -> str:
    if TOKEN not in template:
        raise ValueError(f"the llms.txt template has no {TOKEN}: nothing would be generated")
    return template.replace(TOKEN, ", ".join(state_names(seed_dir)))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if llms.txt is stale")
    ap.add_argument("--template", default=str(ROOT / "_meta" / "templates" / "llms.txt"))
    ap.add_argument("--seed-dir", default=str(ROOT / "_meta" / "sources"))
    ap.add_argument("--output", default=str(ROOT / "llms.txt"))
    a = ap.parse_args()
    out = Path(a.output)
    try:
        text = render(Path(a.template).read_text(encoding="utf-8"), Path(a.seed_dir))
    except ValueError as e:
        print(e)
        return 1
    if a.check:
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            print(f"{out.name} is stale: run scripts/regen.sh")
            return 1
        print(f"{out.name} is current.")
        return 0
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

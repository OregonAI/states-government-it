#!/usr/bin/env python3
"""Check the seed list (_meta/sources/<state>.yml, one file per state) against the domain pack
(_meta/domain.yml).

  python3 src/check_seed_list.py --check     # exit 1 and list every problem

The states are the files in the seed directory (domain.yml does not list them). A state file
holds only that state's entries and a non-empty `left_out` record (a list of `text:` items: what
was found on an official page and not seeded, and why). An instrument's url may not be both seeded
and left out, and left-out prose may not begin a line with `id:` or `sha256:` (corpus-toolkit
edits those lines by regex when it records a baseline).

Rules: a key written twice anywhere in the file (e.g. two `sources:` blocks) fails; every entry has the required fields, non-empty; `jurisdiction`, `doc_type` and
`tags` take only values from domain.yml; `format` is declared from a known set; ids and
urls are unique; a stub carries `stub_reason`; `stub` and `watch_only` are true booleans
and never both. An empty list fails: a missing or emptied manifest must not pass.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("id", "url", "format", "citation", "title", "doc_type", "jurisdiction", "tags",
            "why_relevant")
CA_SLICE_CODES = {"GOV", "CIV", "PCC"}   # the codes src/ingest.py's CA_CODES maps to (a test keeps them equal)
# states whose only slice shape is the section range (their hook reads no other)
ARTICLE_REFUSED = {"oklahoma"}
FORMATS = {"html", "pdf", "doc", "docx", "xlsx", "json", "xml", "txt"}


class DuplicateKeyError(ValueError):
    """A mapping key written twice. PyYAML keeps the last one silently, which drops every
    entry under an earlier `sources:` block while the check still passes."""


class _UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=True)
            if key in seen:
                raise DuplicateKeyError(
                    f"duplicate key {key!r} at line {key_node.start_mark.line + 1}")
            seen.add(key)
        return super().construct_mapping(node, deep)


def load_yaml_text(text: str):
    """yaml.safe_load, except that a duplicate mapping key at any level raises."""
    return yaml.load(text, Loader=_UniqueKeyLoader)  # noqa: S506 -- SafeLoader subclass


def _blank(v) -> bool:
    return v is None or (isinstance(v, (str, list)) and not (v.strip() if isinstance(v, str) else v))


def check(manifest: dict, domain: dict) -> list[str]:
    sources = (manifest or {}).get("sources") or []
    if not sources:
        return ["no entries in sources: an empty seed list cannot pass"]
    states, types = set(domain["states"]), set(domain["instrument_types"])
    tags = set(domain["tags"])
    errors: list[str] = []
    ids: set = set()
    urls: set = set()   # (url, slice) pairs
    for i, e in enumerate(sources):
        if not isinstance(e, dict):
            errors.append(f"entry #{i}: not a mapping")
            continue
        eid = e.get("id") or f"#{i}"
        bad = lambda msg: errors.append(f"{eid}: {msg}")  # noqa: E731
        for f in REQUIRED:
            if _blank(e.get(f)):
                bad(f"missing or empty required field {f}")
        if e.get("id") in ids:
            bad("duplicate id")
        ids.add(e.get("id"))
        # Several documents may be slices of one source file (a Colorado title file): the unit
        # that must be unique is the url plus the slice, and a url shared with an unsliced entry
        # is still a duplicate.
        sl = e.get("slice")
        key = (e.get("url"), tuple(sorted(sl.items())) if isinstance(sl, dict) else None)
        if key in urls or (e.get("url"), None) in urls or (key[1] is None and any(
                u == e.get("url") for u, _ in urls)):
            bad("duplicate url")
        urls.add(key)
        if "slice" in e and e["slice"] is not None:
            ok_strings = isinstance(sl, dict) and all(isinstance(v, str) and v for v in sl.values())
            juris = e.get("jurisdiction")
            is_ca = juris == "california"
            # a section range of one file (a title PDF, a chapter page): the printed number of the first
            # section and of the section whose heading ends the slice (that section is not in it); a state's
            # to_text hook cuts it, and the ingester refuses a state whose hook does not (src/states)
            section_range = (not is_ca and ok_strings and set(sl) == {"section_start", "section_end_before"})
            # a Colorado-style article (and optionally part) of a title file; Oklahoma's hook reads only
            # the section range, so an article slice there would pass this check and crash the ingester
            colorado = (not is_ca and juris not in ARTICLE_REFUSED and ok_strings
                        and not _blank(sl.get("article")) and not set(sl) - {"article", "part"})
            # a California slice of the Legislature's bulk download: a code the ingester knows and
            # exactly one of a table-of-contents path or a section number; only California entries
            california = (is_ca and ok_strings and sl.get("code") in CA_SLICE_CODES
                          and set(sl) <= {"code", "path", "section"}
                          and len(set(sl) & {"path", "section"}) == 1)
            if not (colorado or california or section_range):
                bad("slice must be a mapping with section_start and section_end_before, as strings, "
                    "or with article (and optionally part), as strings (not on a california or oklahoma entry), or, "
                    f"on a california entry, with code (one of {sorted(CA_SLICE_CODES)}) and exactly one of path "
                    "or section, as strings")
        url = e.get("url")
        if isinstance(url, str) and not url.startswith(("http://", "https://")):
            bad(f"url is not http(s): {url}")
        if e.get("format") and e["format"] not in FORMATS:
            bad(f"format {e['format']!r} not one of {sorted(FORMATS)}")
        if e.get("jurisdiction") and e["jurisdiction"] not in states:
            bad(f"jurisdiction {e['jurisdiction']!r} not in domain.yml states")
        if e.get("doc_type") and e["doc_type"] not in types:
            bad(f"doc_type {e['doc_type']!r} not in domain.yml instrument_types")
        t = e.get("tags")
        if isinstance(t, list):
            for x in t:
                if x not in tags:
                    bad(f"tags: {x!r} not in domain.yml tags")
        elif t is not None:
            bad("tags must be a list")
        for flag in ("stub", "watch_only"):
            if flag in e and e[flag] is not True:
                bad(f"{flag} must be true when present (omit it otherwise)")
        if e.get("stub") is True and _blank(e.get("stub_reason")):
            bad("stub: true requires stub_reason")
        if e.get("stub") is True and e.get("watch_only") is True:
            bad("stub and watch_only are exclusive")
    return errors


_URL = re.compile(r"https?://[^\s)'\",;>]+")
_TOOLKIT_KEY = re.compile(r"^[ \t]*(?:-[ \t]+)?(id|sha256):")


def check_left_out(name: str, left_out, seeded_urls: set) -> list[str]:
    """The left-out record of one state file: a non-empty list of `{text: <non-empty string>}`."""
    if not isinstance(left_out, list) or not left_out:
        return [f"{name}: left_out is missing or empty: record what was found and left out, with the reason"]
    errors: list[str] = []
    for i, item in enumerate(left_out):
        text = item.get("text") if isinstance(item, dict) else None
        if not isinstance(text, str) or not text.strip():
            errors.append(f"{name}: left_out item #{i} must be a mapping with a non-empty text")
            continue
        for line in text.splitlines():
            if _TOOLKIT_KEY.match(line):
                errors.append(f"{name}: left_out item #{i} has a line starting {line.strip()[:30]!r}: "
                              f"the toolkit's baseline editor reads lines beginning id: or sha256: as an "
                              f"entry's keys; reword it")
        for url in _URL.findall(text):
            url = url.rstrip(".:")
            if url in seeded_urls:
                errors.append(f"{name}: {url} is seeded and also left out (left_out item #{i})")
    return errors


def check_seed_dir(seed_dir, domain: dict) -> tuple[dict, list[str]]:
    """(the combined manifest `{"sources": [...]}`, problems) for a directory of per-state seed files."""
    seed_dir = Path(seed_dir)
    files = sorted(seed_dir.glob("*.yml")) if seed_dir.is_dir() else []
    if not files:
        return {"sources": []}, [f"no *.yml state files in {seed_dir}: an empty seed list cannot pass"]
    errors: list[str] = []
    sources: list = []
    left: list[tuple[Path, list, object]] = []
    for f in files:
        try:
            doc = load_yaml_text(f.read_text()) or {}
        except (DuplicateKeyError, yaml.YAMLError) as e:
            errors.append(f"{f.name}: cannot be loaded: {e}")
            continue
        entries = doc.get("sources") or []
        if not entries:
            errors.append(f"{f.name}: no entries in sources")
        for e in entries:
            if isinstance(e, dict) and e.get("jurisdiction") != f.stem:
                errors.append(f"{f.name}: entry {e.get('id')!r} has jurisdiction {e.get('jurisdiction')!r}: "
                              f"a state file holds only {f.stem!r} entries")
        sources += entries
        left.append((f, entries, doc.get("left_out")))
    errors += check({"sources": sources}, {**domain, "states": [f.stem for f in files]}) if sources else []
    for f, entries, left_out in left:
        # an index page to watch may be cited in the left-out prose ("watched below"): it is not an instrument
        urls = {e.get("url") for e in entries if isinstance(e, dict) and not e.get("watch_only")}
        errors += check_left_out(f.name, left_out, urls)
    return {"sources": sources}, errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="the default; accepted for gates")
    ap.add_argument("--seed-dir", default=str(ROOT / "_meta" / "sources"))
    ap.add_argument("--domain", default=str(ROOT / "_meta" / "domain.yml"))
    a = ap.parse_args()
    try:
        domain = load_yaml_text(Path(a.domain).read_text())
    except (DuplicateKeyError, yaml.YAMLError) as e:
        print(f"seed list cannot be loaded: {e}")
        return 1
    manifest, errors = check_seed_dir(a.seed_dir, domain)
    for m in errors:
        print(m)
    if errors:
        print(f"{len(errors)} seed-list problem(s)")
        return 1
    print(f"seed list ok: {len(manifest['sources'])} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())

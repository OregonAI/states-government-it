"""Seam: src.check_seed_list.check(manifest, domain) -> list of error strings, and main().
Each test states one rule the seed list owes the owner who approves it."""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from src import check_seed_list as c

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = {
    "states": ["oregon", "washington"],
    "instrument_types": ["statute", "rule"],
    "tags": {"governance": "x", "ai": "y"},
}


def entry(**kw):
    base = {
        "id": "or-ors-276a", "url": "https://example.gov/x", "format": "html",
        "citation": "ORS ch. 276A", "title": "Information Technology",
        "doc_type": "statute", "jurisdiction": "oregon", "tags": ["governance"],
        "why_relevant": "CIO statute.",
    }
    base.update(kw)
    return base


def errs(*entries):
    return c.check({"sources": list(entries)}, DOMAIN)


def test_valid_entry_passes():
    assert errs(entry()) == []


def test_missing_required_field_is_named():
    e = entry()
    del e["citation"]
    out = errs(e)
    assert len(out) == 1 and "or-ors-276a" in out[0] and "citation" in out[0]


def test_empty_required_field_fails():
    assert errs(entry(why_relevant=" "))


def test_jurisdiction_outside_domain_fails():
    assert any("jurisdiction" in m for m in errs(entry(jurisdiction="texas")))


def test_doc_type_outside_domain_fails():
    assert any("doc_type" in m for m in errs(entry(doc_type="memo")))


def test_unknown_tag_fails_and_empty_tags_fail():
    assert any("tags" in m for m in errs(entry(tags=["governance", "vibes"])))
    assert any("tags" in m for m in errs(entry(tags=[])))


def test_duplicate_id_and_duplicate_url_fail():
    assert any("duplicate id" in m for m in errs(entry(), entry(url="https://example.gov/y")))
    assert any("duplicate url" in m for m in errs(entry(), entry(id="other")))


def test_stub_needs_reason_and_watch_only_needs_flag_true():
    assert any("stub_reason" in m for m in errs(entry(stub=True)))
    assert errs(entry(stub=True, stub_reason="refused")) == []
    assert any("watch_only" in m for m in errs(entry(watch_only="yes")))


def test_stub_and_watch_only_are_exclusive():
    assert errs(entry(stub=True, stub_reason="r", watch_only=True))


def test_bad_url_and_undeclared_format_fail():
    assert errs(entry(url="ftp://x"))
    assert errs(entry(format="doc"))


def test_empty_list_fails_so_a_missing_manifest_cannot_pass():
    assert c.check({"sources": []}, DOMAIN)


def test_cli_fails_on_broken_manifest(tmp_path):
    m = tmp_path / "m.yml"
    m.write_text(yaml.safe_dump({"sources": [entry(tags=["nope"])]}))
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--manifest", str(m)],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 1 and "nope" in r.stdout


def test_cli_passes_on_repo_manifest():
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--check"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


# ---- a duplicate key must not silently drop approved entries -----------------------------

TWO_SOURCES_BLOCKS = """\
sources:
  - id: a
    url: https://example.gov/a
sources:
  - id: b
    url: https://example.gov/b
"""


def test_loader_rejects_a_second_sources_block():
    with pytest.raises(c.DuplicateKeyError, match="sources"):
        c.load_yaml_text(TWO_SOURCES_BLOCKS)


def test_loader_rejects_duplicate_keys_at_any_level():
    with pytest.raises(c.DuplicateKeyError, match="url"):
        c.load_yaml_text("sources:\n  - id: a\n    url: x\n    url: y\n")


def test_cli_fails_on_two_sources_blocks(tmp_path):
    m = tmp_path / "m.yml"
    m.write_text(TWO_SOURCES_BLOCKS)
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--manifest", str(m)],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 1 and "sources" in r.stdout

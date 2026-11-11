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


def test_entries_sharing_one_source_file_need_different_slices():
    a = entry(url="https://example.gov/title-24.htm", slice={"article": "73"})
    b = entry(id="other", url="https://example.gov/title-24.htm", slice={"article": "74"})
    assert errs(a, b) == []
    assert any("duplicate url" in m for m in errs(a, dict(b, slice={"article": "73"})))
    assert any("duplicate url" in m for m in errs(a, dict(b, slice=None)))
    assert any("duplicate url" in m for m in errs(dict(a, slice=None), dict(b, slice=None)))
    parts = [dict(a, slice={"article": "33.5", "part": "19"}),
             dict(b, slice={"article": "33.5", "part": "20"})]
    assert errs(*parts) == []


def test_slice_must_name_an_article_and_may_name_a_part():
    assert any("slice" in m for m in errs(entry(slice="article 73")))
    assert any("slice" in m for m in errs(entry(slice={"part": "19"})))
    assert any("slice" in m for m in errs(entry(slice={"article": "73", "chapter": "x"})))
    assert errs(entry(slice={"article": "73"})) == []


def test_stub_needs_reason_and_watch_only_needs_flag_true():
    assert any("stub_reason" in m for m in errs(entry(stub=True)))
    assert errs(entry(stub=True, stub_reason="refused")) == []
    assert any("watch_only" in m for m in errs(entry(watch_only="yes")))


def test_stub_and_watch_only_are_exclusive():
    assert errs(entry(stub=True, stub_reason="r", watch_only=True))


def test_bad_url_and_undeclared_format_fail():
    assert errs(entry(url="ftp://x"))
    assert errs(entry(format="rtf"))


def test_legacy_word_doc_is_a_declarable_format_for_a_stub():
    # Washington publishes a policy only as a .doc; the toolkit's sniffer names the format "doc",
    # so a stub for it must be able to declare it.
    assert errs(entry(format="doc", stub=True, stub_reason="Word-only source")) == []


def test_empty_list_fails_so_a_missing_manifest_cannot_pass():
    assert c.check({"sources": []}, DOMAIN)


def test_cli_fails_on_broken_manifest(tmp_path):
    m = tmp_path / "oregon.yml"
    m.write_text(yaml.safe_dump({"sources": [entry(tags=["nope"])]}))
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--seed-dir", str(tmp_path)],
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
    m = tmp_path / "oregon.yml"
    m.write_text(TWO_SOURCES_BLOCKS)
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--seed-dir", str(tmp_path)],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 1 and "sources" in r.stdout


# ---- California slices: the code is one the ingester knows, and only California entries carry one ----

CA_DOMAIN = {**DOMAIN, "states": ["oregon", "california"]}


def ca_errs(*entries):
    return c.check({"sources": list(entries)}, CA_DOMAIN)


def ca_entry(**kw):
    return entry(**{"jurisdiction": "california", "slice": {"code": "GOV", "path": "3.3.1.8"}, **kw})


def test_california_slice_code_must_be_one_the_ingester_knows():
    assert ca_errs(ca_entry()) == []
    assert any("slice" in m for m in ca_errs(ca_entry(slice={"code": "XYZ", "path": "3.3.1.8"})))
    assert any("slice" in m for m in ca_errs(ca_entry(slice={"code": "gov", "section": "7405"})))
    for code in ("GOV", "CIV", "PCC"):
        assert ca_errs(ca_entry(slice={"code": code, "section": "1"})) == []


def test_california_slice_codes_are_the_ingesters_codes():
    from src.states import california
    assert c.CA_SLICE_CODES == set(california.CA_CODES.values())


def test_a_code_slice_belongs_only_on_a_california_entry():
    assert any("slice" in m for m in errs(entry(slice={"code": "GOV", "section": "7405"})))


def test_a_california_entry_cannot_carry_an_article_slice():
    assert any("slice" in m for m in ca_errs(ca_entry(slice={"article": "73"})))


# ---- One seed file per state: _meta/sources/<state>.yml holds that state's entries and its left-out record ----

LEFT = [{"text": "Something seen and not seeded (https://example.gov/other): the reason."}]


def write_state(d, state, entries, left_out=LEFT, **extra):
    doc = {"sources": entries, **extra}
    if left_out is not None:
        doc["left_out"] = left_out
    (d / f"{state}.yml").write_text(yaml.safe_dump(doc))


def seed_errs(tmp_path, domain=DOMAIN):
    manifest, errors = c.check_seed_dir(tmp_path, domain)
    return manifest, errors


def test_the_states_are_the_files_in_the_seed_directory(tmp_path):
    write_state(tmp_path, "oregon", [entry()])
    write_state(tmp_path, "washington", [entry(id="wa-rcw-43-105", url="https://example.gov/w",
                                               jurisdiction="washington")])
    manifest, errors = seed_errs(tmp_path, {k: v for k, v in DOMAIN.items() if k != "states"})
    assert errors == []
    assert [e["id"] for e in manifest["sources"]] == ["or-ors-276a", "wa-rcw-43-105"]


def test_a_state_file_holds_only_its_own_states_entries(tmp_path):
    write_state(tmp_path, "oregon", [entry(jurisdiction="washington")])
    _, errors = seed_errs(tmp_path)
    assert any("oregon.yml" in m and "washington" in m for m in errors)


def test_an_id_or_url_may_not_repeat_across_state_files(tmp_path):
    write_state(tmp_path, "oregon", [entry()])
    write_state(tmp_path, "washington", [entry(jurisdiction="washington")])
    _, errors = seed_errs(tmp_path)
    assert any("duplicate id" in m for m in errors) and any("duplicate url" in m for m in errors)


def test_a_state_file_must_record_what_it_left_out(tmp_path):
    write_state(tmp_path, "oregon", [entry()], left_out=None)
    assert any("left_out" in m for m in seed_errs(tmp_path)[1])
    write_state(tmp_path, "oregon", [entry()], left_out=[])
    assert any("left_out" in m for m in seed_errs(tmp_path)[1])
    write_state(tmp_path, "oregon", [entry()], left_out=[{"text": " "}])
    assert any("left_out" in m for m in seed_errs(tmp_path)[1])
    write_state(tmp_path, "oregon", [entry()], left_out=["a bare string"])
    assert any("left_out" in m for m in seed_errs(tmp_path)[1])


def test_an_instrument_cannot_be_both_seeded_and_left_out(tmp_path):
    write_state(tmp_path, "oregon", [entry()],
                left_out=[{"text": "Seen at https://example.gov/x and left out."}])
    assert any("https://example.gov/x" in m and "left out" in m for m in seed_errs(tmp_path)[1])


def test_left_out_text_may_not_look_like_a_key_the_toolkit_rewrites(tmp_path):
    # corpus_toolkit.sources.manifest edits `id:` and `sha256:` lines by regex; prose that begins a
    # line that way would be taken for an entry's key
    for bad in ("id: or-ors-276a\nmore", "note\n- sha256: abc"):
        write_state(tmp_path, "oregon", [entry()], left_out=[{"text": bad}])
        assert any("id:" in m or "sha256:" in m for m in seed_errs(tmp_path)[1]), bad


def test_an_empty_or_missing_seed_directory_fails(tmp_path):
    _, errors = seed_errs(tmp_path)
    assert errors


def test_main_checks_the_directory(tmp_path):
    write_state(tmp_path, "oregon", [entry()])
    dom = tmp_path / "domain.yml"
    dom.write_text(yaml.safe_dump({k: v for k, v in DOMAIN.items() if k != "states"}))
    sd = tmp_path / "seed"
    sd.mkdir()
    (tmp_path / "oregon.yml").rename(sd / "oregon.yml")
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--seed-dir", str(sd),
                        "--domain", str(dom)], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0 and "seed list ok: 1 entries" in r.stdout, r.stdout
    (sd / "oregon.yml").write_text(yaml.safe_dump({"sources": [entry()]}))
    r = subprocess.run([sys.executable, "-m", "src.check_seed_list", "--seed-dir", str(sd),
                        "--domain", str(dom)], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 1 and "left_out" in r.stdout


def test_a_watched_index_page_may_be_cited_in_the_left_out_prose(tmp_path):
    write_state(tmp_path, "oregon", [entry(watch_only=True)],
                left_out=[{"text": "No rules: see the index page https://example.gov/x, watched."}])
    assert seed_errs(tmp_path)[1] == []

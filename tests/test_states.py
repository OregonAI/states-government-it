"""Seam: src.states, the per-state hook dispatch. A state is a module `src/states/<state>.py`, found by
name; adding one edits no shared file."""
import textwrap

import pytest

from src import ingest as ing
from src import states

DUMMY = textwrap.dedent('''
    from src.states import UNHANDLED

    def to_text(raw, fmt, doc_type, slice_, host):
        return raw.decode().upper() if fmt == "html" and doc_type == "statute" else None

    def check_identity(src, text, what_is):
        if src["doc_type"] == "statute":
            if "NEVERLAND" not in text:
                raise ValueError(f"{src['id']}: not the cited instrument")
            return True
        return False

    def effective_date(text, doc_type):
        return "2001-02-03" if text.startswith("DATED") else UNHANDLED

    def notes(src, fmt, text):
        return "Neverland notes." if src["doc_type"] == "statute" else None
''')


@pytest.fixture
def neverland(tmp_path, monkeypatch):
    """A state added the way a real one is: one new file, in a directory the package searches."""
    (tmp_path / "neverland.py").write_text(DUMMY)
    monkeypatch.setattr(states, "__path__", [*states.__path__, str(tmp_path)])
    monkeypatch.setattr(states, "_modules", None)
    yield "neverland"
    monkeypatch.setattr(states, "_modules", None)


def test_the_four_pilot_states_are_found_by_name_with_no_registry():
    assert {"oregon", "washington", "california", "colorado"} <= set(states.modules())


def test_a_new_state_file_is_discovered_and_its_hooks_are_used(neverland):
    assert neverland in states.modules(refresh=True)
    assert ing.to_text(b"neverland act", "html", "statute", neverland) == "NEVERLAND ACT"
    src = {"id": "nv-1", "jurisdiction": neverland, "doc_type": "statute", "citation": "NV 1", "title": "t"}
    ing.check_identity(src, "NEVERLAND ACT")
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(src, "SOMEWHERE ELSE")
    assert ing.conversion_notes(src, "html", "x") == "Neverland notes."


def test_an_effective_date_hook_can_decline_and_the_shared_label_reader_answers(neverland):
    assert ing.effective_date("DATED x", "policy", neverland) == "2001-02-03"
    assert ing.effective_date("Effective Date: March 5, 2020\n", "policy", neverland) == "2020-03-05"
    assert ing.effective_date("DATED x", "statute", neverland) is None     # a statute never has one


def test_a_state_with_no_module_gets_the_shared_checks_and_no_html_cleanup():
    assert "nowhere" not in states.modules()
    with pytest.raises(ValueError, match="'nowhere' has no module in src/states/"):
        ing.to_text(b"<p>x</p>", "html", "statute", "nowhere")
    pdf_policy = {"id": "x", "jurisdiction": "nowhere", "doc_type": "policy",
                  "citation": "Policy 107-004-190", "title": "t"}
    ing.check_identity(pdf_policy, "Policy 107-004-190 text")                 # the shared policy-number check
    with pytest.raises(ValueError, match="not the cited instrument"):
        ing.check_identity(pdf_policy, "something else", "pdf")


def test_a_state_module_imports_no_other_state_and_not_the_ingest_flow():
    import ast
    import pathlib
    for p in pathlib.Path(states.__file__).parent.glob("*.py"):
        if p.name == "__init__.py":
            continue
        for node in ast.walk(ast.parse(p.read_text())):
            mod = node.module if isinstance(node, ast.ImportFrom) else None
            names = [a.name for a in node.names] if isinstance(node, (ast.Import, ast.ImportFrom)) else []
            bad = [m for m in ([mod] if mod else []) + names
                   if m in ("src.ingest", "src.states.oregon", "src.states.washington", "src.states.california",
                            "src.states.colorado") or m == "src.ingest_ocr"]
            assert not bad, f"{p.name} imports {bad}"

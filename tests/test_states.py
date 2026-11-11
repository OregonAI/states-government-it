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


def forbidden_imports(source: str, own: str, all_states: set) -> list:
    """Full module names a state module imports that it may not: the ingest flow and any other state.
    `src.ingest_common`, `src.ingest_docx` and `src.ingest_ocr` are allowed."""
    import ast
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            found += [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:                     # relative: resolve against src.states
                pkg = ["src", "states"][:max(0, 2 - (node.level - 1))]
                base = ".".join(pkg + ([base] if base else []))
            found.append(base)
            found += [f"{base}.{a.name}" for a in node.names]
    banned = {"src.ingest"} | {f"src.states.{n}" for n in all_states if n != own}
    return sorted({m for m in found if m in banned})


@pytest.mark.parametrize("line", [
    "from src import ingest",
    "import src.ingest",
    "from src.ingest import x",
    "from src.states import washington",
    "from src.states.washington import x",
    "from . import washington",
    "from .washington import x",
    "from .. import ingest",
    "import src.states.washington as w",
])
def test_the_import_rule_catches_every_way_to_import_the_ingest_flow_or_another_state(line):
    assert forbidden_imports(line, "oregon", {"oregon", "washington"}), line


@pytest.mark.parametrize("line", [
    "from src.ingest_common import _squash",
    "from src.ingest_ocr import ocr",
    "from src import ingest_docx",
    "from src.states import UNHANDLED",
    "from src.states.oregon import x",        # itself
    "import re",
])
def test_the_import_rule_allows_the_shared_helpers_and_the_package(line):
    assert forbidden_imports(line, "oregon", {"oregon", "washington"}) == [], line


def test_a_state_module_imports_no_other_state_and_not_the_ingest_flow():
    import pathlib
    names = set(states.modules())
    for p in pathlib.Path(states.__file__).parent.glob("*.py"):
        if p.name == "__init__.py":
            continue
        bad = forbidden_imports(p.read_text(), p.stem, names)
        assert not bad, f"{p.name} imports {bad}"


def _loads_command() -> str:
    import pathlib
    import re
    gates = (pathlib.Path(states.__file__).parents[2] / "scripts" / "gates.sh").read_text()
    return re.search(r'run "ingester loads" python3 -c "([^"]+)"', gates).group(1)


def test_the_ingester_loads_gate_fails_on_a_state_module_that_cannot_be_imported(tmp_path):
    import pathlib
    import shutil
    import subprocess
    import sys
    src = pathlib.Path(states.__file__).parents[1]
    shutil.copytree(src, tmp_path / "src", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(src.parent / "_meta", tmp_path / "_meta", ignore=shutil.ignore_patterns("snapshots"))
    cmd = [sys.executable, "-c", _loads_command()]
    assert subprocess.run(cmd, cwd=tmp_path, capture_output=True).returncode == 0
    (tmp_path / "src" / "states" / "zbroken.py").write_text("def (:\n")
    assert subprocess.run(cmd, cwd=tmp_path, capture_output=True).returncode != 0


def test_ci_runs_the_same_loads_command_as_the_gate():
    import pathlib
    ci = (pathlib.Path(states.__file__).parents[2] / ".github" / "workflows" / "ci.yml").read_text()
    assert f'- run: python3 -c "{_loads_command()}"' in ci

"""Utah: the Legislature's per-chapter XML of the Utah Code. Everything else Utah seeds is a PDF or a
Word file, which the shared readers handle. Hooks are described in src/states/__init__.py."""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

_KNOWN = {"chapter", "effdate", "sunset", "catchline", "part", "section", "histories", "history",
          "modchap", "modyear", "subsection", "tab", "xref"}
_INLINE = {"xref", "modchap", "tab"}
_LABEL = re.compile(r"(\([A-Za-z0-9]+\))$")


def _squeeze(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _flat(el: ET.Element) -> str:
    """An element's text with every inline child (cross-reference, chapter number) read as text."""
    return "".join(el.itertext())


def _block(el: ET.Element, depth: int, out: list[str], label: str = "") -> None:
    """A section or subsection: its own words (text before and between its children), then each
    subsection one level deeper, then (sections only) the amendment history."""
    indent = "  " * depth
    buf = [el.text or ""]
    first = True
    history: list[str] = []

    def flush():
        nonlocal first
        words = _squeeze("".join(buf))
        buf.clear()
        if words or (label and first):
            out.append(f"{indent}{label + ' ' if label and first else ''}{words}".rstrip())
            first = False

    for child in el:
        if child.tag in _INLINE:
            buf.append(_flat(child))
        elif child.tag == "subsection":
            flush()
            number = _LABEL.search(child.get("number", ""))
            _block(child, depth + 1, out, number.group(1) if number else "")
        elif child.tag == "histories":
            history = [_squeeze(_flat(h)) for h in child.findall("history")]
        elif child.tag == "catchline":
            pass
        elif child.tag == "effdate" and el.tag == "section":
            pass                                  # printed under the heading by code_xml_to_text
        elif child.tag == "sunset" and el.tag == "section":
            pass
        else:
            raise ValueError(f"Utah Code XML: unexpected <{child.tag}> inside <{el.tag}>")
        buf.append(child.tail or "")
    flush()
    out.extend(history)


def code_xml_to_text(raw: bytes) -> str:
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        raise ValueError(f"not Utah Code chapter XML: {e}") from None
    if root.tag != "chapter":
        raise ValueError(f"not Utah Code chapter XML: root element is <{root.tag}>")
    unknown = {el.tag for el in root.iter()} - _KNOWN
    if unknown:
        raise ValueError(f"Utah Code XML has markup this reader does not know: {sorted(unknown)}: the format changed")
    title = _squeeze(root.findtext("catchline") or "")
    out = [f"Chapter {root.get('number')} {title}"]
    if (eff := root.findtext("effdate")):
        out.append(f"Effective {_squeeze(eff)}")
    if (sun := root.find("sunset")) is not None:
        out.append(f"Repeal date {sun.get('repdate')} (Section {sun.get('repsec')})")
    rendered = 0

    def section_lines(section: ET.Element) -> None:
        out.extend(["", f"{section.get('number')} {_squeeze(section.findtext('catchline') or '')}"])
        if (eff := section.findtext("effdate")):
            out.append(f"Effective {_squeeze(eff)}")
        if (sun := section.find("sunset")) is not None:
            out.append(f"Repeal date {sun.get('repdate')} (Section {sun.get('repsec')})")
        _block(section, 0, out)

    for child in root:                            # parts, or sections sitting directly in the chapter
        if child.tag == "part":
            out += ["", f"Part {child.get('number')} {_squeeze(child.findtext('catchline') or '')}"]
            for section in child.findall("section"):
                section_lines(section)
                rendered += 1
        elif child.tag == "section":
            section_lines(child)
            rendered += 1
    total = len(list(root.iter("section")))
    if rendered == 0:
        raise ValueError(f"Utah Code XML: chapter {root.get('number')} renders no section: not a chapter file")
    if rendered != total:
        raise ValueError(f"Utah Code XML: {total - rendered} of {total} sections are in a place this reader does not render")
    return "\n".join(out) + "\n"


# ---- hooks (see src/states/__init__.py) ----------------------------------------

def to_text(raw, fmt, doc_type, slice_, host):
    if fmt == "xml" and doc_type == "statute":
        return code_xml_to_text(raw)
    return None


def check_identity(src, text, what_is):
    if src["doc_type"] == "statute":
        number = re.search(r"(\d+[A-Za-z]?-\d+[a-z]?)$", src["citation"])
        first = text.splitlines()[0] if text.strip() else ""
        if not number or not first.startswith(f"Chapter {number.group(1)} "):
            raise ValueError(f"{src['id']}: file is not {src['citation']} (chapter mismatch)")
        return True
    return False


def notes(src, fmt, text):
    if fmt == "xml":
        return ("Text rendered from the Legislature's per-chapter XML download of the Utah Code (the file the "
                "chapter page's Download Options link to): the chapter line, its effective date and any repeal "
                "date the file carries (a section that takes effect later carries its own, printed under its heading), each part and section heading, each subsection on its own "
                "line indented by depth with its own label, cross-references as their text, and each section's "
                "amendment history after it. The file is a versioned URL: when the chapter is amended the "
                "Legislature publishes a new file name.")
    return None

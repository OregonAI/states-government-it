"""Scanned PDFs read by two OCR engines, and the record of that reading, shared by every state's ingester."""
from __future__ import annotations

import difflib
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

from corpus_toolkit.sources.snapshots import record_snapshot

from src.ingest_common import ROOT, _LIGATURES
from src.states import check_identity


# ---- scanned PDFs: the two-engine OCR procedure ---------------------------------------------
#
# corpus-template AGENTS.md, "OCR": tesseract (through ocrmypdf) is the primary engine and PaddleOCR
# PP-OCRv6 reads the ORIGINAL scan as the cross-check; a single engine's output is never promoted. The
# seed entry says `ocr: true` for a PDF known to be a scan. What is committed:
#   <id>.pdf         the scan as the source served it (source_sha256 never hashes a derived copy)
#   <id>.txt         the tesseract text: this is the document's text and what the provenance gate reads
#   <id>.paddle.txt  the second engine's text. CI has no PaddleOCR, so its text is kept and the agreement
#                    is recomputed from the two committed texts
#   <id>.ocr.json    the report: tools, the PDF's and both texts' sha256, agreement, figure agreement,
#                    dictionary ratio
# `--check` re-derives what CI can: it re-runs tesseract on the committed PDF and requires the committed
# text to agree with that reading (OCR_RECHECK), and it recomputes the two-engine agreement from the
# committed texts. The dictionary ratio is a gate at ingest only: it is judged against the rest of the
# corpus's non-OCR text, which changes as the corpus grows, so the recorded value is not re-derived.
#
# What `--check` can and cannot catch. CI installs the same Ubuntu 24.04 apt packages (tesseract 5.3.4,
# ocrmypdf 15.2.0) that made the text, and their re-run is byte-identical (measured for all eight scans), so
# while the installed tools are the recorded ones the re-run must give the committed text's word sequence
# and figure sequence EXACTLY: an edited number or word fails even when text_sha256 is updated beside it.
# When the apt packages move (recorded tool versions differ from the installed ones) a reading may shift by
# a word, so the bar relaxes to OCR_RECHECK on words with the figure sequence still exact, and the message
# says so. The remedy is to re-ingest the scan (`python3 src/ingest.py --refetch`) so the record is renewed
# under the new tools; never to relax the bar. Figure agreement between the engines is a gate at ingest
# (OCR_MIN_FIGURES) and again here, because the word score cannot see digits.

OCR_WORD = re.compile(r"[a-z]{2,}")


OCR_FIGURE = re.compile(r"\$?-?\d[\d,]*(?:\.\d+)?%?")


OCR_TOKEN = re.compile(r"[A-Za-z]+|\$?\d[\d,]*(?:\.\d+)?%?")   # words and figures, for listing disagreements


OCR_MIN_AGREEMENT = 0.80    # the platform's bar for two engines on the word sequence


OCR_MIN_DICT = 0.80


OCR_MIN_WORDS = 100


OCR_MIN_FIGURES = 0.90      # figure agreement between the engines (Oregon EO 16-13 read 0.75 and was wrong)


OCR_RECHECK = 0.995         # word bar of the re-run when the installed tools are not the recorded ones


OCR_ENGINES = ("tesseract (ocrmypdf)", "paddleocr PP-OCRv6")


OCR_CAVEAT = ("NOT human-verified \u2014 treat every number as unchecked against the source")


def ocr_score(primary: str, cross: str, vocab: set) -> dict:
    """Word-sequence agreement of two engines, figure agreement scored separately (digits are where
    engines diverge and the word score hides it), and the share of the primary text's words the corpus's
    own non-OCR vocabulary knows."""
    wa, wb = OCR_WORD.findall(primary.lower()), OCR_WORD.findall(cross.lower())
    fa, fb = OCR_FIGURE.findall(primary.lower()), OCR_FIGURE.findall(cross.lower())
    ratio = lambda a, b: difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else 0.0
    return {"words": len(wa), "agreement": ratio(wa, wb), "figures": len(fa),
            "figure_agreement": 1.0 if not fa and not fb else ratio(fa, fb),
            "dict_ratio": sum(1 for w in wa if w in vocab) / len(wa) if wa else 0.0,
            "glued": len(re.findall(r"\b[A-Za-z]{18,}\b", primary))}


def ocr_vocabulary(config) -> set:
    """Words of this corpus's own text that was NOT produced by OCR, sampled evenly: the reference a
    reading is judged against. Text read by OCR is excluded, or its misreadings would become vocabulary."""
    ocr_ids = {p.name[:-len(".ocr.json")] for p in config.snapshot_dir.glob("*.ocr.json")}
    files = sorted(p for p in config.snapshot_dir.glob("*.txt")
                   if p.stem not in ocr_ids and not p.name.endswith(".paddle.txt"))
    vocab: set = set()
    for p in files[::max(1, len(files) // 400)]:
        vocab |= set(OCR_WORD.findall(p.read_text(encoding="utf-8", errors="replace").lower()))
    return vocab


def ocr_disagreements(primary: str, cross: str) -> list[dict]:
    """Every position where the two engines read a different token (word or figure): what tesseract (the
    committed reading) and paddle read there, and the four tesseract tokens before it. A reader can see
    where the committed reading is contested."""
    a, b = OCR_TOKEN.findall(primary), OCR_TOKEN.findall(cross)
    ops = difflib.SequenceMatcher(None, [t.casefold() for t in a], [t.casefold() for t in b], autojunk=False)
    return [{"tesseract": " ".join(a[i1:i2]), "paddle": " ".join(b[j1:j2]), "before": a[max(0, i1 - 4):i1]}
            for tag, i1, i2, j1, j2 in ops.get_opcodes() if tag != "equal"]


_SIGNATURE_FIELD = re.compile(r"^APPROVED:(.*)$")


def _drop_signature_glyphs(page: str) -> str:
    """The DAS policies' `APPROVED:` field holds a handwritten signature. What an engine reads from it
    (`A, Bath`, `Yun |`, `fh eat M`) is glyph noise that looks like a name, so it is not committed: the
    label stays, the reading after it (on the line, or on the next non-blank line when that holds no word of
    four letters) goes."""
    lines = page.split("\n")
    out, i = [], 0
    while i < len(lines):
        m = _SIGNATURE_FIELD.match(lines[i])
        out.append("APPROVED:" if m else lines[i])
        i += 1
        if m:
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and len(lines[j].split()) <= 4 and not re.search(r"[A-Za-z]{4,}", lines[j]):
                i = j + 1
    return "\n".join(out)


def _tool_version(cmd: list) -> str:
    try:
        out = subprocess.run(cmd, capture_output=True, check=False)
    except FileNotFoundError:
        return "not installed"
    return (out.stdout or out.stderr).decode("utf-8", "replace").strip().splitlines()[0]


def _clean_pages(pages: list[str]) -> list[str]:
    return ["\n".join(l.rstrip() for l in page.splitlines()).strip("\n") for page in pages]


def ocr_tesseract(raw: bytes, force_rotate: bool = False, psm: int | None = None) -> str:
    """The text tesseract reads from a scan, one text block per page (see `ocr_tesseract_pages`)."""
    text = "\n\n".join(ocr_tesseract_pages(raw, force_rotate, psm))
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"


def ocr_tesseract_pages(raw: bytes, force_rotate: bool = False, psm: int | None = None) -> list[str]:
    """What tesseract reads from each page of a scan, through ocrmypdf on a COPY. `force_rotate` applies
    tesseract's orientation call even where it is unsure (a page scanned upside down is otherwise read as
    confident nonsense). `psm` is tesseract's page-segmentation mode, the seed entry's `ocr_psm`: 4 reads a
    two-column layout by rows, so a label column stays beside its text (the default, 3, sets the label
    column apart as a block). Signature-field glyphs are not kept (`_drop_signature_glyphs`)."""
    with tempfile.TemporaryDirectory() as tmp:
        src, out, side = Path(tmp, "in.pdf"), Path(tmp, "out.pdf"), Path(tmp, "side.txt")
        src.write_bytes(raw)
        cmd = ["ocrmypdf", "-l", "eng", "--optimize", "0", "--output-type", "pdf", "--rotate-pages",
               "--deskew", "--sidecar", str(side)] + (["--rotate-pages-threshold", "0"] if force_rotate else []) \
            + (["--tesseract-pagesegmode", str(psm)] if psm else [])
        try:
            proc = subprocess.run(cmd + [str(src), str(out)], capture_output=True, check=False, timeout=1800)
        except FileNotFoundError:
            raise ValueError("ocrmypdf is not installed: it runs tesseract on the scans "
                             "(apt-get install ocrmypdf tesseract-ocr)") from None
        if proc.returncode != 0 or not side.is_file():
            raise ValueError("tesseract could not read the PDF (ocrmypdf exit "
                             f"{proc.returncode}): {proc.stderr.decode('utf-8', 'replace').strip()[-200:]}")
        pages = side.read_text(encoding="utf-8").split("\f")
    if len(pages) > 1 and not pages[-1].strip():
        pages.pop()
    return [_drop_signature_glyphs(p) for p in _clean_pages(pages)]


def _pdf_pages(raw: bytes) -> int:
    out = subprocess.run(["pdfinfo", "-"], input=raw, capture_output=True, check=True).stdout.decode("utf-8", "replace")
    return int(re.search(r"^Pages:\s+(\d+)", out, flags=re.M).group(1))


def _layer_page(raw: bytes, n: int) -> str:
    """Page n's text layer as `pdf_to_text` reads it (pdftotext -layout, ligatures written as letters)."""
    text = subprocess.run(["pdftotext", "-layout", "-f", str(n), "-l", str(n), "-", "-"], input=raw,
                          capture_output=True, check=True).stdout.decode("utf-8", "replace")
    text = text.translate(str.maketrans(_LIGATURES)).replace("\f", "")
    return "\n".join(l.rstrip() for l in text.split("\n")).strip("\n")


def _subset_pdf(raw: bytes, pages: list[int]) -> bytes:
    """A PDF of just these pages, in order (poppler's pdfseparate and pdfunite)."""
    with tempfile.TemporaryDirectory() as tmp:
        whole = Path(tmp, "whole.pdf")
        whole.write_bytes(raw)
        parts = []
        for n in pages:
            part = Path(tmp, f"p-{n}.pdf")
            subprocess.run(["pdfseparate", "-f", str(n), "-l", str(n), str(whole), str(part)], check=True,
                           capture_output=True)
            parts.append(str(part))
        out = Path(tmp, "subset.pdf")
        subprocess.run(["pdfunite", *parts, str(out)], check=True, capture_output=True)
        return out.read_bytes()


def _compose(raw: bytes, pages: list[int], ocr_pages: list[str]) -> str:
    """The text of a PDF with some scanned pages: each page in order, the text layer's where the page has
    one and the OCR reading's where it is listed in `pages`."""
    by_page = dict(zip(pages, ocr_pages))
    blocks = [by_page[n] if n in by_page else _layer_page(raw, n) for n in range(1, _pdf_pages(raw) + 1)]
    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(blocks)).strip("\n") + "\n"


def ocr_paddle(pdf_path: Path) -> str:
    """The cross-check engine's text, by `src/ocr_paddle.py` under a Python that has PaddleOCR
    (`OCR_PADDLE_PYTHON`, default /usr/bin/python3: the repo's .venv has none). Refused, never skipped,
    when it is not there: unchecked OCR is not promotable."""
    python = os.environ.get("OCR_PADDLE_PYTHON", "/usr/bin/python3")
    env = dict(os.environ, PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK="True")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([python, str(ROOT / "src" / "ocr_paddle.py"), str(pdf_path)], cwd=tmp,
                                  capture_output=True, check=False, timeout=3600, env=env)
    except FileNotFoundError:
        raise ValueError(f"PaddleOCR (the second OCR engine) is not available: {python} does not exist "
                         f"(set OCR_PADDLE_PYTHON to a Python with paddleocr)") from None
    if proc.returncode != 0:
        raise ValueError("PaddleOCR (the second OCR engine) failed: "
                         + proc.stderr.decode("utf-8", "replace").strip()[-300:])
    return proc.stdout.decode("utf-8", "replace")


def ocr_scan(src: dict, raw: bytes, config, paddle=None, vocab: set | None = None) -> tuple[str, dict]:
    """(text, report) for a scanned PDF, or ValueError. `ocr: true` in the seed entry says every page is a
    scan; `ocr: [2, 3, 4]` lists the scanned pages of a PDF whose other pages have a text layer (their text
    is pdftotext's). Both engines read the scan; the text is tesseract's, promoted only when the engines
    agree on at least OCR_MIN_AGREEMENT of the word sequence, at least OCR_MIN_DICT of the words are known
    words, there are OCR_MIN_WORDS words, and the text is the cited instrument. A page scanned upside down
    is read again with orientation forced when the first reading fails."""
    vocab = ocr_vocabulary(config) if vocab is None else vocab
    paddle = paddle or ocr_paddle
    pages = sorted(set(src["ocr"])) if isinstance(src.get("ocr"), list) else None
    psm = src.get("ocr_psm")
    scan = raw
    if pages:
        for n in range(1, _pdf_pages(raw) + 1):
            has_layer = bool(_layer_page(raw, n).split())
            if n in pages and has_layer:
                raise ValueError(f"{src['id']}: PDF page {n} has a text layer but the seed entry lists it in ocr")
            if n not in pages and not has_layer:
                raise ValueError(f"{src['id']}: PDF page {n} has no text layer (a scan) and the seed entry's "
                                 f"ocr list does not name it")
        scan = _subset_pdf(raw, pages)
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp, "scan.pdf")
        pdf.write_bytes(scan)
        cross = paddle(pdf)
    why, ocr_pages, score, forced = "", [], {}, False
    for forced in (False, True):
        ocr_pages = ocr_tesseract_pages(scan, force_rotate=forced, psm=psm)
        score = ocr_score("\n\n".join(ocr_pages), cross, vocab)
        if score["words"] < OCR_MIN_WORDS:
            why = f"tesseract read only {score['words']} words (needs {OCR_MIN_WORDS})"
        elif score["agreement"] < OCR_MIN_AGREEMENT:
            why = (f"the two OCR engines agree on only {score['agreement']:.0%} of the word sequence "
                   f"(needs {OCR_MIN_AGREEMENT:.0%})")
        elif score["figure_agreement"] < OCR_MIN_FIGURES:
            why = (f"the two OCR engines agree on only {score['figure_agreement']:.0%} of the "
                   f"{score['figures']} figures (needs {OCR_MIN_FIGURES:.0%}): the words agree but the numbers "
                   f"(section numbers, dates, citations) are contested")
        elif score["dict_ratio"] < OCR_MIN_DICT:
            why = (f"only {score['dict_ratio']:.0%} of the words are in the corpus's non-OCR dictionary "
                   f"(needs {OCR_MIN_DICT:.0%})")
        else:
            why = ""
            break
    if why:
        raise ValueError(f"{src['id']}: OCR is not promotable: {why}")
    if pages:
        text = _compose(raw, pages, ocr_pages)
    else:
        text = re.sub(r"\n{3,}", "\n\n", "\n\n".join(ocr_pages)).strip("\n") + "\n"
    check_identity(src, text, "pdf")
    contested = ocr_disagreements("\n\n".join(ocr_pages), cross)
    report = dict({k: (round(v, 4) if isinstance(v, float) else v) for k, v in score.items()},
                  engines=list(OCR_ENGINES), forced_rotation=forced, psm=psm, disagreements=contested,
                  tools={"tesseract": _tool_version(["tesseract", "--version"]),
                         "ocrmypdf": _tool_version(["ocrmypdf", "--version"])},
                  pdf_sha256=hashlib.sha256(raw).hexdigest(),
                  text_sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
                  paddle_sha256=hashlib.sha256(cross.encode("utf-8")).hexdigest())
    if pages:
        report.update(pages=pages, ocr_page_texts=ocr_pages)
    return text, dict(report, paddle_text=cross)


def _page_list(pages: list) -> str:
    return ", ".join(str(n) for n in pages)


def ocr_notes(report: dict) -> str:
    """`conversion_notes` for text read by OCR: wording of the reference implementation (oregon-kpm)."""
    glued = (f"; {report['glued']} heading/letterhead token(s) lost their word spacing and are left as-is "
             f"rather than reconstructed" if report.get("glued") else "")
    pages = report.get("pages")
    head = (f"Pages {_page_list(pages)} of the PDF have no text layer (they are scans) and their text was "
            f"recovered by OCR; the other pages' text is the text layer, extracted with pdftotext -layout "
            f"(trailing spaces and form feeds removed, ligature glyphs written as their letters)."
            if pages else "no text layer in the source PDF; text recovered by OCR.")
    return (f"{head} Two independent engines "
            f"({' + '.join(report['engines'])}) agree on {report['agreement']:.0%} of the word sequence and "
            f"{report['figure_agreement']:.0%} of the {report['figures']} figures"
            f"{' of the scanned pages' if pages else ''}, "
            f"{report['dict_ratio']:.0%} dictionary-recognizable{glued}.{_contested(report)} "
            f"Reading order of labelled or two-column layouts, bullet glyphs (read as 'e' or 'o'), letterhead logos, handwriting "
            f"and signatures are not reliably read or placed; the glyphs read from a signature field are "
            f"not committed. effective_date and source_version are "
            f"left empty: a date read from a scan is not transcribed from the source. {OCR_CAVEAT}")


def _contested(report: dict) -> str:
    """Where the committed reading is contested: the count, every figure the engines read differently
    (up to 12) and where the rest are."""
    found = report.get("disagreements")
    if found is None:
        return ""
    figures = [d for d in found if any(t[0].isdigit() or t[0] == "$" for t in (d["tesseract"] + " " + d["paddle"]).split())]
    shown = "; ".join(f"tesseract read {d['tesseract'] or 'nothing'} where paddle read {d['paddle'] or 'nothing'} "
                      f"(after \"{' '.join(d['before'])}\")" for d in figures[:12])
    more = f" and {len(figures) - 12} more" if len(figures) > 12 else ""
    return (f" {len(found)} position(s) where the two engines read a different word or figure are listed in the "
            f"scan's ocr.json report (disagreements): the committed reading is tesseract's and is contested "
            f"there." + (f" Figures read differently: {shown}{more}." if figures else
                         " The engines read every figure alike."))


def _ocr_paths(config, sid: str) -> tuple[Path, Path, Path]:
    d = config.snapshot_dir
    return d / f"{sid}.txt", d / f"{sid}.paddle.txt", d / f"{sid}.ocr.json"


def load_ocr_report(config, sid: str) -> dict | None:
    _, _, side = _ocr_paths(config, sid)
    return json.loads(side.read_text(encoding="utf-8")) if side.is_file() else None


def write_ocr_snapshot(config, src: dict, raw: bytes, text: str, report: dict):
    """Record the scan, its OCR text (the toolkit writes `<id>.pdf`, `<id>.txt`, both hashes and the drift
    baseline), then the second engine's text and the report beside them."""
    snap = record_snapshot(config, src["id"], raw, "pdf", text)
    txt, paddle, side = _ocr_paths(config, src["id"])
    if snap.fresh or not side.is_file():
        txt.write_text(text, encoding="utf-8")
        paddle.write_text(report["paddle_text"], encoding="utf-8")
        side.write_text(json.dumps({k: v for k, v in report.items() if k != "paddle_text"},
                                   indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return snap


def _recheck(sid: str, committed: str, again: str, recorded: dict) -> list[str]:
    """Compare tesseract's re-run on the snapshot with the committed reading. With the recorded tools
    installed the word and figure sequences must be equal; with other versions the figures must still be
    equal and the words agree at OCR_RECHECK (see the section note)."""
    same_tools = (recorded.get("tesseract") == _tool_version(["tesseract", "--version"])
                  and recorded.get("ocrmypdf") == _tool_version(["ocrmypdf", "--version"]))
    words = lambda t: OCR_WORD.findall(t.lower())
    figures = lambda t: OCR_FIGURE.findall(t.lower())
    problems = []
    if figures(committed) != figures(again):
        problems.append(f"{sid}: the figures of the committed text are not the figures tesseract reads from the "
                        f"snapshot PDF (committed {len(figures(committed))}, re-read {len(figures(again))}): "
                        f"a number was edited or the text is not a reading of this PDF")
    if same_tools:
        if words(committed) != words(again):
            ratio = difflib.SequenceMatcher(None, words(committed), words(again), autojunk=False).ratio()
            problems.append(f"{sid}: with the recorded tools installed, tesseract re-reading the snapshot PDF gives a "
                            f"different word sequence from the committed text (agreement {ratio:.4f}, needs exact): "
                            f"the words were edited, or the text is not a reading of this PDF")
    else:
        ratio = difflib.SequenceMatcher(None, words(committed), words(again), autojunk=False).ratio()
        if ratio < OCR_RECHECK:
            problems.append(f"{sid}: the installed tesseract/ocrmypdf are not the recorded ones; its re-reading of the "
                            f"snapshot PDF agrees with the committed words on only {ratio:.3f} (needs "
                            f"{OCR_RECHECK}): re-ingest this scan to renew the record, or the text is not a reading "
                            f"of this PDF")
    return problems


def check_ocr(src: dict, raw: bytes, config) -> tuple[str | None, list[str]]:
    """Offline re-derivation of a scan's document text: (committed text, problems). See the section note."""
    sid = src["id"]
    txt, paddle, side = _ocr_paths(config, sid)
    report = load_ocr_report(config, sid)
    if report is None or not txt.is_file() or not paddle.is_file():
        return None, [f"{sid}: OCR record missing ({sid}.ocr.json, {sid}.txt and {sid}.paddle.txt are all required)"]
    text, cross = txt.read_text(encoding="utf-8"), paddle.read_text(encoding="utf-8")
    sha = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()
    problems = []
    if report["pdf_sha256"] != hashlib.sha256(raw).hexdigest():
        problems.append(f"{sid}: the snapshot PDF's sha256 is not the one the OCR report was made from")
    if report["text_sha256"] != sha(text):
        problems.append(f"{sid}: {sid}.txt differs from the OCR text recorded in {sid}.ocr.json (text_sha256)")
    if report["paddle_sha256"] != sha(cross):
        problems.append(f"{sid}: {sid}.paddle.txt (second engine) differs from the text recorded in {sid}.ocr.json")
    pages = report.get("pages")
    ocr_text = "\n\n".join(report["ocr_page_texts"]) if pages else text
    if pages:
        try:
            if _compose(raw, pages, report["ocr_page_texts"]) != text:
                problems.append(f"{sid}: {sid}.txt is not the text layer of the snapshot PDF's other pages (pdftotext) "
                                f"with the recorded OCR reading of pages {_page_list(pages)}")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            problems.append(f"{sid}: cannot read the snapshot PDF's text layer with pdftotext: {e}")
    score = ocr_score(ocr_text, cross, set())
    if score["agreement"] < OCR_MIN_AGREEMENT or abs(score["agreement"] - report["agreement"]) > 0.005:
        problems.append(f"{sid}: tesseract text and paddle text agree on {score['agreement']:.3f}, the report "
                        f"says {report['agreement']:.3f} (bar {OCR_MIN_AGREEMENT})")
    if score["figure_agreement"] < OCR_MIN_FIGURES:
        problems.append(f"{sid}: the two engines agree on only {score['figure_agreement']:.3f} of the figures "
                        f"(bar {OCR_MIN_FIGURES})")
    if report["dict_ratio"] < OCR_MIN_DICT or score["words"] < OCR_MIN_WORDS:
        problems.append(f"{sid}: the recorded OCR quality is below the gate")
    try:
        scan = _subset_pdf(raw, pages) if pages else raw
        again = ocr_tesseract(scan, force_rotate=report.get("forced_rotation", False), psm=report.get("psm"))
        problems += _recheck(sid, ocr_text, again, report.get("tools") or {})
    except ValueError as e:
        problems.append(f"{sid}: cannot re-run tesseract on the snapshot: {e}")
    try:
        check_identity(src, text, "pdf")
    except ValueError as e:
        problems.append(str(e))
    return text, problems


def with_ocr(src: dict, config) -> dict:
    """The seed entry with its OCR report attached (`_ocr`) when it is a scan read by OCR."""
    report = load_ocr_report(config, src["id"]) if src.get("ocr") else None
    return dict(src, _ocr=report) if report else src


def _ocr_warning(report: dict) -> str:
    pages = report.get("pages")
    what = (f"Pages {_page_list(pages)} of the source PDF are images with no text layer; their text below"
            if pages else "The source PDF has no text layer: it is an image. The full text below")
    return (f"> **MACHINE READING OF A SCAN.** {what} was read from the image by OCR (two engines, see the "
            f"curator notes) and is not the document's own text. Expect character-level errors in words and "
            f"figures, and treat every number as unchecked against the source. `source_sha256` hashes this "
            f"transcription; the scan is the snapshot.\n\n")

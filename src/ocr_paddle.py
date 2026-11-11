#!/usr/bin/env python3
"""The second OCR engine: PaddleOCR (PP-OCRv6) over the ORIGINAL scan, text to stdout.

Run by `src/ingest.py` as a subprocess under a Python that has paddleocr (the repo's .venv does
not, and CI does not: the second engine runs once, when a scan is ingested, and its text is
committed beside the snapshot, see `ocr_scan` in ingest.py).

  python3 src/ocr_paddle.py scan.pdf [page ...]      # one line per recognised text line

It reads the original, never tesseract's output, so the two engines share only the pixels.
Orientation classification is ON: without it a rotated scan reads as fluent nonsense that
scores about 0.05 against the other engine (corpus-template AGENTS.md, OCR section).
"""
import subprocess
import sys
import tempfile
from pathlib import Path


def main(argv: list[str]) -> int:
    from paddleocr import PaddleOCR
    pdf, pages = argv[1], [int(p) for p in argv[2:]]
    with tempfile.TemporaryDirectory() as tmp:
        cmd = ["pdftoppm", "-r", "200", "-png"]
        if len(pages) == 1:
            cmd += ["-f", str(pages[0]), "-l", str(pages[0])]
        subprocess.run(cmd + [pdf, f"{tmp}/p"], check=True, capture_output=True)
        ocr = PaddleOCR(lang="en", use_doc_orientation_classify=True,
                        use_doc_unwarping=False, use_textline_orientation=True)
        for img in sorted(Path(tmp).glob("p-*.png")):
            number = int(img.stem.split("-")[-1])
            if pages and number not in pages:
                continue
            for d in ocr.predict(str(img)):
                for line in d.get("rec_texts") or []:
                    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

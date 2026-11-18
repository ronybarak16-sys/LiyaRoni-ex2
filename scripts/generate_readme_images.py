"""Render README screenshots from the ACTUAL compiled PDF (output/final_book.pdf) with PyMuPDF.

Pages are located by searching their text (not hard-coded numbers), so the screenshots stay
correct after the layout changes.
    python scripts/generate_readme_images.py             # README previews -> assets/readme/
    python scripts/generate_readme_images.py --all --out Detector/reports/pages_R1   # every page
"""
import argparse
import sys
from pathlib import Path

import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output" / "final_book.pdf"

# name -> text that identifies the page (first page containing it is used)
TARGETS = {
    "cover_preview": None,                      # page 1
    "chapter_preview": "הפסיכולוגיה של הכלב העירוני",
    "graph_preview": "חלוקת זמן הטיולים",
    "diagram_preview": "תרשים זרימה בן שמונה",
    "table_preview": "השוואה בין סביבות הליכה",
}


def find_page(doc, needle):
    if needle is None:
        return 0
    for pno, page in enumerate(doc):
        if needle in page.get_text() and pno > 3:   # skip cover/abstract/TOC/intro matches
            return pno
    raise SystemExit(f"text not found in PDF: {needle}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="render every page")
    ap.add_argument("--out", default=str(ROOT / "assets" / "readme"))
    ap.add_argument("--dpi", type=int, default=110)
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    if args.all:
        for pno, page in enumerate(doc, start=1):
            page.get_pixmap(dpi=args.dpi).save(out / f"page_{pno:02d}.png")
        print(f"rendered {doc.page_count} pages -> {out}")
        return
    for name, needle in TARGETS.items():
        pno = find_page(doc, needle)
        doc[pno].get_pixmap(dpi=args.dpi).save(out / f"{name}.png")
        print(f"{name}.png  <- PDF page {pno + 1}")


if __name__ == "__main__":
    main()

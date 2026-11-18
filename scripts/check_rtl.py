"""Objective RTL probe for the compiled PDF.

Why: visual inspection of Hebrew word order in rasterised pages proved unreliable during
development (see docs/PROCESS_LOG.md). This script measures word positions instead.

For each probe (word A, word B) where A precedes B in the Hebrew source, it finds the two
words on the same text line and checks that A is to the RIGHT of B (x(A) > x(B)).
Usage: python scripts/check_rtl.py [pdf]   -> exit 1 if any probe fails.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]

# (description, first word, second word) — words exactly as PyMuPDF extracts them
PROBES = [
    # (description, first word, second word, chapter-file hint used only for the report)
    ("cover label", "מדריך", "מאויר"),
    ("cover subtitle", "בין", "פחמימות"),
    ("cover subtitle line 2", "השלם", "לבעלי"),
    ("cover authors", "ליה", "פורת"),
    ("cover authors", "מגישות", "ליה"),
    ("cover group code label", "קוד", "קבוצה"),
    ("cover group code after label", "קבוצה", "liyaroni-ex2"),
    ("p.9 checklist callout title", "רשימת", "ציוד"),
    ("p.9 checklist callout title", "קבועה", "ליד"),
    ("warning box title (p.4)", "הבהרה", "חשובה"),
    ("warning box title", "שימו", "לב"),
    ("abstract body (control)", "כלב", "בעיר"),
    ("diagram block 1", "הכלב", "הרים"),
    ("diagram block 3", "נסו", "לזהות"),
    ("diagram block 6", "פנו", "מיד"),
    ("diagram block 7", "פעלו", "בדיוק"),
    ("diagram block 8", "תעדו", "את"),
    ("diagram block 5", "עקבו", "אחר"),
    ("diagram label", "הופיע", "סימן"),
    ("diagram label", "הכול", "תקין"),
    ("FAQ heading", "התחמם", "מאוד"),
    ("FAQ heading", "הכלב", "מסרב"),
    ("elevator speech bubble", "זאת", "הייתה"),
    ("graph caption", "חלוקת", "זמן"),
    ("table header", "מתי", "כדאי"),
]


def check(pdf_path: Path) -> int:
    doc = pymupdf.open(pdf_path)
    failures = 0
    for desc, first, second in PROBES:
        found = None
        for pno, page in enumerate(doc, start=1):
            words = page.get_text("words")
            for a in (w for w in words if w[4] == first):
                same_line = [b for b in words if b[4] == second and abs(b[3] - a[3]) < 2.5
                             and abs(b[0] - a[0]) < 120]
                if same_line:
                    b = min(same_line, key=lambda w: abs(w[0] - a[0]))
                    found = (pno, a[0] > b[0])
                    break
            if found:
                break
        if found is None:
            print(f"NOT FOUND  {desc}: '{first}' + '{second}'")
            failures += 1
        else:
            pno, ok = found
            print(f"{'PASS' if ok else 'FAIL'}       p.{pno:<3} {desc}: '{first}' -> '{second}'")
            failures += 0 if ok else 1
    print(f"\n{len(PROBES) - failures}/{len(PROBES)} RTL probes passed")
    return failures


if __name__ == "__main__":
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "output" / "final_book.pdf"
    sys.exit(1 if check(pdf) else 0)

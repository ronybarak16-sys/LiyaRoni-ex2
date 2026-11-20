"""Whole-book RTL word-order audit (complements the targeted probes in check_rtl.py).

Method
1. Collect every pair of consecutive Hebrew words ("bigrams") from the LaTeX sources
   (book/**/*.tex and figures/tikz/*.tex), after stripping comments and commands.
2. Rebuild every text line of the PDF in *visual right-to-left order* (words sorted by
   x descending) and collect the Hebrew bigrams that appear there.
3. A source bigram "A B" that appears in the PDF only as "B A" (reversed) is reported as
   a probable RTL defect, with page number and line text.
Text extraction is used only to read word *positions*; the final judgement remains a
visual inspection of the rendered pages.

Usage: python scripts/audit_rtl_full.py [pdf]  -> exit 1 if suspected reversals are found
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
HEB = re.compile(r"[\u0590-\u05FF]")
STRIP = re.compile(r"[^\u0590-\u05FF\-]")  # keep Hebrew letters (incl. geresh/gershayim) and hyphen


def norm(word):
    return STRIP.sub("", word).strip("-")


def source_bigrams():
    files = list((ROOT / "book").rglob("*.tex")) + list((ROOT / "figures" / "tikz").glob("*.tex"))
    bigrams = defaultdict(set)
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            line = re.sub(r"(?<!\\)%.*", "", line)                 # comments
            line = line.replace("}{", " | ")                       # separate macro arguments
            line = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", line)  # commands (keep their {text})
            line = re.sub(r"[{}$\\&]", " ", line)
            toks = line.split()
            for t1, t2 in zip(toks, toks[1:]):
                if re.search(r"[,.:;?!)(\]\[]$", t1) or re.match(r"[(\[]", t2):
                    continue                                       # never pair across punctuation
                a, b = norm(t1), norm(t2)
                if a and b and HEB.search(a) and HEB.search(b):
                    bigrams[(a, b)].add(f.relative_to(ROOT).as_posix())
    return bigrams


def pdf_lines(pdf):
    doc = pymupdf.open(pdf)
    for pno, page in enumerate(doc, start=1):
        rows = defaultdict(list)
        for w in page.get_text("words"):
            rows[(w[5], w[6])].append(w)                         # (block, line)
        for ws in rows.values():
            ws.sort(key=lambda w: -w[0])                          # visual RTL order
            yield pno, [norm(w[4]) for w in ws], " ".join(w[4] for w in ws)


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "output" / "final_book.pdf"
    src = source_bigrams()
    seen_ok, seen_rev = set(), defaultdict(list)
    for pno, words, raw in pdf_lines(pdf):
        for a, b in zip(words, words[1:]):
            if not (a and b):
                continue
            if (a, b) in src:
                seen_ok.add((a, b))
            if (b, a) in src and a != b:
                seen_rev[(b, a)].append((pno, raw))
    suspects = {k: v for k, v in seen_rev.items() if k not in seen_ok}
    checked = len(seen_ok) + len(suspects)
    print(f"source Hebrew bigrams: {len(src)} | matched in PDF: {checked} | "
          f"correct order: {len(seen_ok)} | reversed only: {len(suspects)}")
    for (a, b), hits in sorted(suspects.items(), key=lambda kv: kv[1][0][0]):
        pno, raw = hits[0]
        print(f"  REVERSED p.{pno:<3} '{a} {b}'  ({', '.join(sorted(src[(a, b)]))})")
        print(f"             visual line (right->left): {raw[:110]}")
    return 1 if suspects else 0


if __name__ == "__main__":
    sys.exit(main())

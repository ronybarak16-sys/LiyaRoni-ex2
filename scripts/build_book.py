"""Reproducible build: figures -> XeLaTeX -> Biber -> XeLaTeX x2 -> output/final_book.pdf.

Usage (Windows PowerShell or any shell):
    python scripts/build_book.py            # full build
    python scripts/build_book.py --no-figs  # skip Python figure generation
Exit code is non-zero on any failure. Build intermediates go to build/ (git-ignored).
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
BUILD = ROOT / "build"
OUTPUT = ROOT / "output" / "final_book.pdf"
MAX_PAGES = 20
RERUN_RE = re.compile(r"Rerun to get|Please rerun LaTeX|Please \(re\)run Biber")


def run(cmd, cwd):
    print("$", " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode != 0:
        print(result.stdout[-4000:])
        print(result.stderr[-2000:])
        raise SystemExit(f"FAILED: {' '.join(cmd)} (exit {result.returncode})")
    return result.stdout


def check_tools():
    for tool in ("xelatex", "biber"):
        if shutil.which(tool) is None:
            raise SystemExit(f"Missing tool on PATH: {tool} (install MiKTeX or TeX Live)")


def build_figures():
    for script in ("create_graph.py", "create_illustration.py"):
        run([sys.executable, str(ROOT / "figures" / "python" / script)], ROOT)


def build_pdf():
    BUILD.mkdir(exist_ok=True)
    latex = ["xelatex", "-interaction=nonstopmode", "-halt-on-error",
             f"-output-directory={BUILD}", "main.tex"]
    run(latex, BOOK)
    run(["biber", f"--input-directory={BUILD}", f"--output-directory={BUILD}", "main"], BOOK)
    # DET-1-11: rerun until labels/TOC are stable (max 5 passes), never ship "Rerun to get ..."
    for _ in range(5):
        run(latex, BOOK)
        log = (BUILD / "main.log").read_text(encoding="utf-8", errors="replace")
        if not RERUN_RE.search(log):
            break
    else:
        raise SystemExit("FAILED: LaTeX still asks for a rerun after 5 passes")


def report():
    import fitz  # PyMuPDF

    pdf = BUILD / "main.pdf"
    OUTPUT.parent.mkdir(exist_ok=True)
    shutil.copyfile(pdf, OUTPUT)
    pages = fitz.open(OUTPUT).page_count
    log = (BUILD / "main.log").read_text(encoding="utf-8", errors="replace")
    overfull = len(re.findall(r"^Overfull \\hbox", log, re.M))
    undefined = len(re.findall(r"undefined", log, re.I))
    missing = len(re.findall(r"Missing character", log))
    print(f"\nPDF: {OUTPUT.relative_to(ROOT)}  pages={pages} (max {MAX_PAGES})")
    rerun = len(RERUN_RE.findall(log))
    print(f"log: overfull hbox={overfull}  'undefined' mentions={undefined}  missing glyphs={missing}"
          f"  rerun warnings={rerun}")
    if pages > MAX_PAGES:
        raise SystemExit(f"FAIL: {pages} pages > {MAX_PAGES}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-figs", action="store_true")
    args = parser.parse_args()
    check_tools()
    if not args.no_figs:
        build_figures()
    build_pdf()
    report()


if __name__ == "__main__":
    main()

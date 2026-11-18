"""Automated project validation -> console + docs/VALIDATION_RESULTS.md

Statuses: PASS | FAIL | MANUAL REVIEW REQUIRED | NOT VERIFIED
A file-existence PASS does not prove semantic correctness; items that need human/agent
judgement are reported as MANUAL REVIEW REQUIRED.
"""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
results = []


def rec(req, status, evidence=""):
    results.append((req, status, evidence))


def exists(req, rel):
    p = ROOT / rel
    rec(req, "PASS" if p.exists() and p.stat().st_size > 0 else "FAIL", rel)


def main():
    pdf = ROOT / "output" / "final_book.pdf"
    # ---- PDF ----
    try:
        import pymupdf
        doc = pymupdf.open(pdf)
        n = doc.page_count
        rec("PDF exists and opens", "PASS", f"{pdf.relative_to(ROOT)}")
        rec("Page count 1..20", "PASS" if 1 <= n <= 20 else "FAIL", f"{n} pages")
        text = "\n".join(p.get_text() for p in doc)
        for title in ["לחיים עם כלב בעיר הגדולה", "בין פחמימות לטיולי לילה", "תקציר", "תוכן עניינים",
                      "הפסיכולוגיה של הכלב העירוני", "מיפוי שטח", "לוגיסטיקה ואופרציות",
                      "מדריך הישרדות", "מקורות"]:
            # whitespace-insensitive: large display fonts can merge words in extraction
            squash = re.sub(r"\s+", "", text)
            ok = re.sub(r"\s+", "", title) in squash
            rec(f"PDF text contains '{title}'", "PASS" if ok else "FAIL", "text extraction (spaces ignored)")
        cover_words = doc[0].get_text()
        rec("Cover on page 1 (title words present)", "PASS" if "רשמי" in cover_words else "FAIL", "p.1")
    except Exception as exc:  # noqa: BLE001
        rec("PDF exists and opens", "FAIL", str(exc))

    # ---- sources ----
    for rel in ["book/main.tex", "book/preamble.tex", "book/references.bib",
                "book/frontmatter/cover.tex", "book/frontmatter/abstract.tex",
                "book/frontmatter/introduction.tex",
                "book/chapters/chapter01_psychology.tex", "book/chapters/chapter02_city_mapping.tex",
                "book/chapters/chapter03_logistics.tex", "book/chapters/chapter04_survival.tex",
                "book/backmatter/acknowledgments.tex"]:
        exists(f"LaTeX source: {rel}", rel)
    main_tex = (ROOT / "book/main.tex").read_text(encoding="utf-8")
    rec("main.tex \\input's the 4 chapters",
        "PASS" if len(re.findall(r"\\input\{chapters/chapter0[1-4]", main_tex)) == 4 else "FAIL")
    rec("TOC generated automatically", "PASS" if "\\tableofcontents" in main_tex else "FAIL")

    # ---- figures ----
    for rel in ["figures/python/create_graph.py", "figures/generated/activity_graph.pdf",
                "figures/python/create_illustration.py",
                "figures/generated/original_neighborhood_map.png",
                "figures/tikz/dog_illustration.tex", "figures/tikz/eight_block_diagram.tex"]:
        exists(f"Figure asset: {rel}", rel)
    diag = (ROOT / "figures/tikz/eight_block_diagram.tex").read_text(encoding="utf-8")
    blocks = re.findall(r"\\node\[(?:startblk|blk|endblk|urgent|decision)\]\s*\((B\d)\)", diag)
    rec("Diagram has exactly 8 blocks", "PASS" if len(set(blocks)) == 8 else "FAIL",
        f"{len(set(blocks))} block nodes: {sorted(set(blocks))}")
    graph_src = (ROOT / "figures/python/create_graph.py").read_text(encoding="utf-8")
    data = [int(x) for x in re.findall(r'\("[^"]+", "\d\d:\d\d", (\d+)\)', graph_src)]
    ch3 = (ROOT / "book/chapters/chapter03_logistics.tex").read_text(encoding="utf-8")
    rec("Graph data match formula example (20+15+35+10=80)",
        "PASS" if data == [20, 15, 35, 10] and "20 + 15 + 35 + 10 = 80" in ch3 else "FAIL", f"data={data}")
    rec("Formula present (\\sum in chapter 3)", "PASS" if "\\sum_{i=1}^{n}" in ch3 else "FAIL")
    ch2 = (ROOT / "book/chapters/chapter02_city_mapping.tex").read_text(encoding="utf-8")
    rec("Table present (booktabs in chapter 2)", "PASS" if "\\toprule" in ch2 else "FAIL")

    # ---- RTL probes ----
    r = subprocess.run([sys.executable, str(ROOT / "scripts/check_rtl.py")], capture_output=True,
                       text=True, encoding="utf-8")
    last = (r.stdout.strip().splitlines() or ["no output"])[-1]
    rec("RTL word-order probes", "PASS" if r.returncode == 0 else "FAIL", last)

    # ---- project docs / skills ----
    for rel in ["README.md", "docs/PRD.md", "docs/PROMPT_HISTORY.md", "docs/AGENT_COMMUNICATION.md",
                "docs/PROCESS_LOG.md", "docs/SOURCE_AUDIT.md", "docs/QA_REPORT.md",
                "docs/ISSUE_TRACKER.md", "docs/REQUIREMENTS_MATRIX.md", "docs/PROJECT_PLAN.md",
                "docs/ARCHITECTURE.md", "docs/SELF_ASSESSMENT.md", "docs/FINAL_CHECKLIST.md",
                ".claude/skills/book-master/SKILL.md", ".claude/skills/book-detector/SKILL.md",
                ".claude/skills/book-fixer/SKILL.md", "requirements.txt", "CLAUDE.md"]:
        exists(f"File: {rel}", rel)
    for skill in ["book-master", "book-detector", "book-fixer"]:
        s = (ROOT / f".claude/skills/{skill}/SKILL.md").read_text(encoding="utf-8")
        ok = s.startswith("---") and f"name: {skill}" in s and "description:" in s
        rec(f"Skill frontmatter valid: {skill}", "PASS" if ok else "FAIL")
    for img in ["cover_preview", "chapter_preview", "graph_preview", "diagram_preview"]:
        p = ROOT / "assets/readme" / f"{img}.png"
        fresh = p.exists() and pdf.exists() and p.stat().st_mtime >= pdf.stat().st_mtime - 1
        rec(f"README screenshot {img}.png newer than PDF", "PASS" if fresh else "FAIL",
            "generated by scripts/generate_readme_images.py")
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    rec("README documents build commands", "PASS" if "build_book.py" in readme else "FAIL")

    # ---- judgement items ----
    for item in ["Hebrew language quality", "Visual design quality", "Source accuracy (FIXER audit)",
                 "Live 3-agent communication (Gate D)", "Independent QA + retest cycle"]:
        rec(item, "MANUAL REVIEW REQUIRED", "see docs/QA_REPORT.md / docs/AGENT_COMMUNICATION.md")

    # ---- output ----
    width = max(len(r[0]) for r in results)
    for req, status, ev in results:
        print(f"{status:<24} {req:<{width}}  {ev}")
    fails = sum(1 for r in results if r[1] == "FAIL")
    lines = ["# Validation results", "",
             f"Generated by `scripts/validate_project.py` on {datetime.now():%Y-%m-%d %H:%M}.", "",
             "| Status | Requirement | Evidence |", "|---|---|---|"]
    lines += [f"| {s} | {q} | {e} |" for q, s, e in results]
    lines += ["", f"**FAIL count: {fails}**"]
    (ROOT / "docs/VALIDATION_RESULTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nFAIL: {fails}   (written to docs/VALIDATION_RESULTS.md)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

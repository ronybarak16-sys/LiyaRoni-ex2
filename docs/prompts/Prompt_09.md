# Prompt 09 of 17

Type: **LLM guidance** · Kind: agent task · Source record: `60890c88` 2026-11-20T11:12:26.497Z (UTC)

## 1. Date and time
2026-11-20 13:12:26 IST (Asia/Jerusalem) · 2026-11-20 11:12:26 UTC

## 2. Agent responsible
DETECTOR (agent `a60444777a0353b60`, subagent transcript `60890c88-7e1f-4edc-b638-7fd79a4a4ada/subagents/agent-a60444777a0353b60.jsonl`); task issued by MASTER in session `60890c88-7e1f-4edc-b638-7fd79a4a4ada` via Agent tool call from MASTER (launch; description: Detector QA round R1).

**Submitted by (team member):** Requires Team Member Action — to be filled by ליה פורת / רוני ברק. Issued by MASTER (Claude) during the orchestration of a human prompt.

## 3. Exact prompt
```text
You are DETECTOR, the independent QA / red-team agent of a three-agent Claude Code project (MASTER, DETECTOR, FIXER). MASTER (the session that launched you) wrote the book; you must review it independently and critically. You do NOT fix or rewrite the book.

FIRST read your role definition and follow it: C:\VibeCoding\LiyaRoni-ex2\.claude\skills\book-detector\SKILL.md (also skim C:\VibeCoding\LiyaRoni-ex2\CLAUDE.md).

## Project
Repository: C:\VibeCoding\LiyaRoni-ex2 (Windows; Bash tool is Git Bash; Python 3.11 with PyMuPDF (`import pymupdf`), Pillow).
Book: Hebrew RTL illustrated guide "המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה", XeLaTeX + polyglossia. Compiled PDF: output/final_book.pdf (must be EXACTLY 20 pages — students' requirement). Sources: book/main.tex, book/preamble.tex, book/frontmatter/*.tex, book/chapters/*.tex, book/backmatter/*.tex, book/references.bib, figures/tikz/*.tex, figures/python/*.py. Authors: ליה פורת ורוני ברק; group code liyaroni-ex2.

Useful tools already in the repo:
- `python scripts/generate_readme_images.py --all --out Detector/reports/pages_R1 --dpi 110` renders every page to PNG — LOOK at the pages with the Read tool (it shows images). Zoom on regions with PyMuPDF `page.get_pixmap(dpi=180, clip=pymupdf.Rect(...))`.
- `python scripts/audit_rtl_full.py` (word-order audit source vs PDF), `python scripts/check_rtl.py`, `python scripts/validate_project.py`.
- Text layer: `pdftotext -enc UTF-8 -f N -l N output/final_book.pdf -` and PyMuPDF `page.get_text("words")` (gives x positions; in RTL the first word of a phrase must have the LARGER x).
IMPORTANT known pitfall: Hebrew word order judged by eye from images is unreliable — use word x-positions to decide order, and images for layout/clipping/overlap/glyph appearance.

## Input A — the students' defect list (from their own reading of the PDF; their tool may OCR, so some items may be OCR artefacts — VERIFY each one, do not assume either way)
1. p.1 cover: shows `liyaroni-ex2 קוד קבוצת` — should be `קוד קבוצה: liyaroni-ex2`.
2. p.3 TOC: entries and page numbers not cleanly on one line; detached number lines, `|` characters, or a lone dot on its own line after "מעלית: שלושה כלבים...".
3. pp.4, 6, 11, 12, 17: `טיפ מהשטת` / `טיפ מהשטת:` should be `טיפ מהשטח:`. p.6: ensure the colon in heading `מעלית: שלושה כלבים...`.
4. p.8 figure 2.1 (Python map): "כביש ראשי סואן" appears duplicated; check the label is not clipped at the top edge.
5. p.10 table 2.2: `בלה 2.2:` should be `טבלה 2.2:`; `בכל יציאה []6` citation placement.
6. p.11 "המתמטיקה של יום עירוני": symbols `n` (after "האות") and `i` (after "שמספרו") reportedly missing.
7. p.12 table 3.1: `אי:` and `בי:` should be `א':` and `ב':`; Friday/Saturday rows layout.
8. p.14: `"תוכנית בי"` should be `"תוכנית ב'"`.
9. p.17 appendix A: `(פרק .(2` should be `(פרק 2).`; the "ריחרוח" entry looks split rather than one continuous entry.
10. p.19: `(Source Audit` missing closing parenthesis.
11. p.20: `3.1: גרף...` missing `איור`; RTL of the sentence with TikZ and Python — period should be at the end, words in order.
Context from MASTER (hypotheses you should confirm or refute, not trust): the body font David draws `'`, `"`, and a tightly-kerned `ח:`/`ה:` in shapes that OCR may read as `י`, `יי`, `ת` — if so, the defect is a glyph-readability problem worth reporting as REAL-VISUAL even if the text layer is correct.

## Input B — your own full review
Then do your own complete review of all 20 pages per the skill's categories A–P, prioritising: Hebrew spelling/grammar/agreement, RTL/LTR order (punctuation, parentheses, numbers, English terms, math), quotes/gershayim, bullets, formulas, tables, figures/diagram (8 blocks, readable, no overflow), captions/numbering, bibliography formatting, headers/footers, clipping/overlap/whitespace, page count = 20. Do not invent problems; every issue needs evidence (page image path or zoom crop path, text-layer excerpt, or log line).

## Output
Write C:\VibeCoding\LiyaRoni-ex2\Detector\reports\QA-R1.md with:
- a header (date, PDF page count, tools used),
- section 1 "Students' list": one row per item 1–11 with verdict REAL (wrong characters/order in the PDF), REAL-VISUAL (characters correct but glyphs/spacing visibly misleading), or NOT REPRODUCED (renders correctly; explain), plus evidence,
- section 2 "Detector findings": issues in the format from the skill (ID DET-1-nn, Severity CRITICAL/MAJOR/MINOR/SUGGESTION, File, Page, Problem, Evidence, Proposed correction, Status OPEN),
- a summary count per severity.
Keep crops/images you cite under Detector/reports/R1_evidence/. Do NOT edit anything outside Detector/reports/. Do NOT run git commit/push.

Your final message back to MASTER: use the protocol header (MESSAGE_ID, TIMESTAMP, SENDER: detector, RECIPIENT: master, TASK_ID: T-005, MESSAGE_TYPE: ISSUE_REPORT, SUBJECT, FILE_REFERENCES, REQUEST, EXPECTED_OUTPUT, STATUS) followed by a concise list of all REAL/REAL-VISUAL items and DET findings with severity and one-line proposed fix each.
```

## 4. Purpose
Independent QA of output/final_book.pdf and all sources; classify each of the students' 11 items as REAL / REAL-VISUAL / NOT REPRODUCED with evidence.

## 5. Actual result
Detector/reports/QA-R1.md: 26 findings (0 CRITICAL, 2 MAJOR, 12 MINOR, 12 SUGGESTION); students' list: 1 real, 5 real-visual, 6 not reproduced. Hand-back received 13:22 local.

## 6. Files affected
Detector/reports/QA-R1.md, Detector/reports/R1_evidence/*, Detector/reports/pages_R1/*.

## 7. Follow-up corrections
- Retest requested in Prompt_13 (QA-R2).

---
Generated by `scripts/export_prompts.py` from the Claude Code transcripts; fields 4-7 from the project records named in the script header. Do not edit by hand; re-run the script.

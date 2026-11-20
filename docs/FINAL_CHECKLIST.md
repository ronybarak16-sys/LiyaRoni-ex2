# Final checklist (acceptance gates)

Status as of 2026-11-20 (after P-004). **The project is NOT finished.**

| Gate | Item | Status | Evidence |
|---|---|---|---|
| A | Hebrew book compiles | PASS | scripts/build_book.py |
| A | ≤ 20 pages | PASS | exactly 20 pages (P-004) |
| A | Cover, abstract, TOC, 4 chapters, bibliography | PASS | pp. 1, 2, 3, 5–16, 19 |
| B | Python graph / table / formula | PASS | pp. 12 / 9, 10, 12 / 11 |
| B | Original + object-based illustrations | PASS | pp. 1, 6, 7, 8 |
| B | Exactly 8 blocks in diagram | PASS | validate_project.py, p. 15 |
| B | Colors, backgrounds, callouts | PASS (master) — DETECTOR review pending | |
| C | Separate chapter files, reproducible build, scripts, dependencies | PASS | book/, scripts/, requirements.txt |
| D | 3 Skills exist and are discovered | PASS | harness listing |
| D | Three agents actually ran | **FAIL (pending)** | detector/fixer not started |
| D | Real communication, QA findings, fixes, retest | **FAIL (pending)** | AGENT_COMMUNICATION.md |
| E | PRD | PASS (v0.3) — review pending | docs/PRD.md |
| E | README with real screenshots | PASS | assets/readme/ |
| E | Prompt history, communication log, source audit, QA, matrix | PARTIAL | docs/ |
| F | Final PDF, LaTeX sources, Git | PASS | output/, book/, GitHub |
| F | Assignment report per template | **BLOCKED** | template not provided |
| F | No unsupported claims of completion | PASS | this file |
| P-003 | Cover: ליה פורת, רוני ברק, liyaroni-ex2; no placeholders | PASS | validate_project.py, p.1 render |
| P-003 | "!" correctly positioned (no leading "!" in titles) | PASS (master) | pp. 4, 9 renders (20-page edition) |
| P-003 | p.9 title "רשימת ציוד קבועה ליד הדלת" correct + right-aligned | PASS (master) | now p.11 render, audit |
| P-003 | Hebrew word order across the PDF | PASS (automated + visual) | audit_rtl_full.py 0 reversed |
| P-003 | Detector independent QA | **NOT PERFORMED** | detector session not running |
| P-004 | Book exactly 20 pages, substantive content, TOC on one page, RTL audit 0 reversed | PASS (master) | build log, audit_rtl_full.py, visual pass of all pages |

## Remaining blockers → smallest next action
1. Start `detector` and `fixer` sessions (CLAUDE.md → *Launching the agents*), then tell master "agents are up".
2. ~~Provide author names + group code~~ — done (P-003). Note: the code supplied, `liyaroni-ex2`, has 12 characters; confirm it matches the instructor's required format.
3. Provide the instructor's report template (and the verbatim P-001 prompt text for `docs/prompts/`).

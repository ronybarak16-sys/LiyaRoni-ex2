# Requirements matrix

PDF pages refer to `output/final_book.pdf` (13 pages, build of 2026-11-18).
Result: PASS (verified with evidence) · PENDING (needs another agent) · MANUAL (human/agent judgement) · FAIL · BLOCKED.

## Book
| Requirement | File | PDF page | Method | Result |
|---|---|---|---|---|
| Hebrew title + subtitle exact | frontmatter/cover.tex | 1 | text extraction + RTL probe | PASS |
| ≤ 20 pages | output/final_book.pdf | 13 total | PyMuPDF page_count | PASS |
| Cover page with original illustration | frontmatter/cover.tex, figures/tikz/dog_illustration.tex | 1 | visual | PASS (master) / PENDING detector |
| Abstract (תקציר) 150–220 words | frontmatter/abstract.tex | 2 | word count + visual | PENDING detector |
| Auto TOC | main.tex `\tableofcontents` | 3 | source + visual | PASS |
| 4 chapters, separate files | book/chapters/*.tex | 5–12 | validate_project.py | PASS |
| Python graph | figures/python/create_graph.py | 10 | script + data check | PASS |
| Table | chapter02 (tab:areas) | 8 | visual | PASS |
| Formula | chapter03 eq. (3.1) | 9 | visual | PASS |
| Original illustration | TikZ city scene, elevator scene; Python map | 1, 6, 7 | source present | PASS |
| Object-based illustration | dog_illustration.tex (pics from ellipses/paths), create_illustration.py (patches) | 1, 6, 7 | source inspection | PASS |
| 8-block diagram | figures/tikz/eight_block_diagram.tex | 12 | regex count = 8 + visual | PASS |
| Callout boxes (≥ 4 distinct) | preamble.tex: tipbox, knowbox, mistakebox, notebox, fieldbox, emergencybox | 2–12 | visual | PASS |
| Real, verified bibliography | references.bib | 13 | FIXER audit | **PENDING (fixer not started)** |
| Captions + visual credits | all figures; backmatter | 6–13 | visual | PASS |
| Page numbers + running headers | preamble.tex (fancyhdr) | all | visual | PASS |
| Correct RTL | all | all | check_rtl.py 18/18 + visual | PASS (automated) / PENDING detector |
| Hebrew language quality | all | all | DETECTOR review | PENDING |

## Project deliverables
| Requirement | Evidence | Result |
|---|---|---|
| LaTeX sources, separate chapters | book/ | PASS |
| Final PDF in output/ | output/final_book.pdf | PASS |
| Python + TikZ graphics sources | figures/ | PASS |
| README with real PDF screenshots | README.md, assets/readme/*.png (scripts/generate_readme_images.py) | PASS |
| PRD | docs/PRD.md v0.1 | PASS (draft) / review PENDING |
| Three Skills | .claude/skills/book-*/SKILL.md (harness discovered them) | PASS |
| Multi-agent architecture doc | docs/ARCHITECTURE.md | PASS |
| **Real communication between 3 agents** | docs/AGENT_COMMUNICATION.md | **BLOCKED – detector/fixer not started** |
| Prompt history | docs/PROMPT_HISTORY.md | PASS (P-001 verbatim text to be attached) |
| QA reports, issue resolution | docs/QA_REPORT.md, docs/ISSUE_TRACKER.md | PENDING (no detector round yet) |
| Source audit | docs/SOURCE_AUDIT.md | PENDING |
| Build instructions | README.md, CLAUDE.md, scripts/build_book.py | PASS |
| Git repository | GitHub origin/main | PASS |
| Assignment report PDF (instructor template) | — | **BLOCKED – template not in repository** |
| Final checklist | docs/FINAL_CHECKLIST.md | PASS (reflects current state) |

# Requirements matrix

PDF pages refer to `output/final_book.pdf` (**20 pages**, build of 2026-11-20, expanded at the students' request — prompt P-004).
Result: PASS (verified with evidence) · PENDING (needs another agent) · MANUAL (human/agent judgement) · FAIL · BLOCKED.

## Book
| Requirement | File | PDF page | Method | Result |
|---|---|---|---|---|
| Hebrew title + subtitle exact | frontmatter/cover.tex | 1 | text extraction + RTL probe | PASS |
| ≤ 20 pages (students asked for exactly 20) | output/final_book.pdf | 20 total | PyMuPDF page_count | PASS |
| Cover page with original illustration | frontmatter/cover.tex, figures/tikz/dog_illustration.tex | 1 | visual | PASS (master) / PENDING detector |
| Cover authors + group code | frontmatter/cover.tex | 1 | text + position check | PASS |
| Abstract (תקציר) 150–220 words | frontmatter/abstract.tex | 2 | word count + visual | PENDING detector |
| Auto TOC on one page | main.tex `\tableofcontents` | 3 | source + visual | PASS |
| 4 chapters, separate files | book/chapters/*.tex | 5–16 | validate_project.py | PASS |
| Python graph | figures/python/create_graph.py | 12 | script + data check | PASS |
| Tables | ch.2 tab:areas, tab:seasons; ch.3 tab:week | 9, 10, 12 | visual | PASS |
| Formula | chapter03 eq. (3.1) | 11 | visual | PASS |
| Original illustrations | TikZ city scene, elevator scene, exposure ladder; Python map | 1, 6, 7, 8 | source present | PASS |
| Object-based illustration | dog_illustration.tex (pics from ellipses/paths), create_illustration.py (patches) | 1, 6, 8 | source inspection | PASS |
| 8-block diagram | figures/tikz/eight_block_diagram.tex | 15 | regex count = 8 + visual | PASS |
| Callout boxes (≥ 4 distinct) | preamble.tex: tipbox, knowbox, mistakebox, notebox, fieldbox, emergencybox | 2–20 | visual | PASS |
| Appendices: glossary, fridge sheet | backmatter/appendix.tex | 17, 18 | visual | PASS |
| Real, verified bibliography | references.bib (10 entries) | 19 | FIXER audit | **PENDING (fixer not started)** |
| Captions + visual credits, production note | all figures; backmatter/acknowledgments.tex | 6–20 | visual | PASS |
| Page numbers + running headers | preamble.tex (fancyhdr) | all | visual | PASS |
| Correct RTL | all | all | audit_rtl_full.py 0/2,652 reversed, check_rtl.py 25/25, visual pass of all 20 pages | PASS (master) / PENDING detector |
| No leading "!" in headings | preamble.tex (icons) | 4, 9 | grep + render | PASS (master) |
| Ch.3 checklist title correct + right-aligned | preamble.tex (`before title`) | 11 | bigram audit + render | PASS (master) |
| Hebrew language quality | all | all | DETECTOR review | PENDING |

## Project deliverables
| Requirement | Evidence | Result |
|---|---|---|
| LaTeX sources, separate chapters | book/ | PASS |
| Final PDF in output/ | output/final_book.pdf | PASS |
| Python + TikZ graphics sources | figures/ | PASS |
| README with real PDF screenshots | README.md, assets/readme/*.png (scripts/generate_readme_images.py) | PASS |
| PRD | docs/PRD.md v0.3 | PASS (draft) / review PENDING |
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

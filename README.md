# המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה
**בין פחמימות לטיולי לילה: המדריך השלם לבעלי כלבים עירוניים**

A 20-page illustrated Hebrew handbook for city dog owners, typeset in XeLaTeX, with every graphic
generated from code. A three-agent Claude Code team (MASTER, DETECTOR, FIXER) produced it as a
Vibe Coding academic project.

📕 **Final book:** [`output/final_book.pdf`](output/final_book.pdf)

<p align="center">
  <img src="assets/readme/cover_preview.png" width="31%" alt="Cover">
  <img src="assets/readme/chapter_preview.png" width="31%" alt="Chapter 1 opening">
  <img src="assets/readme/table_preview.png" width="31%" alt="Chapter 2 with map and table">
</p>

> All screenshots are rendered from the actual `output/final_book.pdf` by
> `scripts/generate_readme_images.py` (PyMuPDF). They are not mock-ups.

## Project status
| | |
|---|---|
| Book | ✅ compiles, exactly 20 / 20 pages, all mandatory elements present; 0 overfull boxes, 0 undefined refs, 0 rerun warnings |
| RTL check | ✅ whole-book audit: 2,643 / 2,643 word pairs in correct order, 0 mostly-reversed lines (`scripts/audit_rtl_full.py`) + 25/25 targeted probes |
| Source audit (FIXER) | ✅ 16 bibliography entries opened and checked; claims: 18 VERIFIED, 4 PARTIALLY VERIFIED (hedged wording), 1 REMOVED, 1 N/A ([SOURCE_AUDIT](docs/SOURCE_AUDIT.md)) |
| Independent QA (DETECTOR) | ✅ round R1: 26 findings → all fixed by FIXER → round R2 retest **QA_APPROVED**, 0 open issues ([QA-R1](Detector/reports/QA-R1.md), [QA-R2](Detector/reports/QA-R2.md)) |
| 3-agent collaboration | ✅ Detector and Fixer ran as independent Claude Code agents launched by Master (own context + own Skill), with real task/report messages — see [AGENT_COMMUNICATION](docs/AGENT_COMMUNICATION.md). Separate interactive terminal sessions were never started. |
| Report PDF (instructor template) | ⛔ template not provided |

Details are in [`docs/FINAL_CHECKLIST.md`](docs/FINAL_CHECKLIST.md).

## The book
| # | Chapter | Highlights |
|---|---|---|
| 1 | הפסיכולוגיה של הכלב העירוני: *איך לשרוד מעלית עם שלושה כלבים וחתול* | body-language panel, elevator scene (TikZ), elevator etiquette, puppy exposure ladder (TikZ), home alone |
| 2 | מיפוי שטח: *הגאוגרפיה של גינות כלבים ופינות הצל הנכונות* | Python-drawn neighborhood map, walking-environments table, seasons table, dog-park etiquette |
| 3 | לוגיסטיקה ואופרציות: *איך לארגן את התיק לטיול של חמש דקות שנגמר בשעה* | gear checklist, formula $T_{daily}=\sum t_i$, matplotlib graph, example week table, emergency bag |
| 4 | מדריך הישרדות: *שאלות נפוצות ותקלות נפוצות* | 11 FAQs, 8-block decision flowchart, emergency box, fill-in emergency card |

The book also contains a cover, an abstract (תקציר), an automatic TOC, an introduction, two appendices (a short glossary and a one-page fridge cheat sheet), a bibliography (biblatex/biber), and an "About the book" page with visual credits, a production note and the three-agent workflow diagram.

<p align="center">
  <img src="assets/readme/graph_preview.png" width="45%" alt="Page with the Python graph and formula">
  <img src="assets/readme/diagram_preview.png" width="45%" alt="Page with the 8-block diagram">
</p>

### Code-generated graphics
| Graphic | Source | Technique |
|---|---|---|
| Cover city scene + elevator scene | `figures/tikz/dog_illustration.tex` | TikZ `pics` built from ellipses, circles, Bézier paths |
| Puppy exposure ladder | `figures/tikz/exposure_ladder.tex` | TikZ shapes with a computed colour gradient |
| Neighborhood planning map | `figures/python/create_illustration.py` | matplotlib patches (Rectangle, Circle, Polygon…) |
| Walk-time graph (illustrative data) | `figures/python/create_graph.py` | matplotlib, vector PDF |
| 8-block flowchart | `figures/tikz/eight_block_diagram.tex` | TikZ nodes + arrows |

## The three agents
| Agent | Skill | Responsibility |
|---|---|---|
| **MASTER** | [`/book-master`](.claude/skills/book-master/SKILL.md) | PRD, writing, LaTeX, graphics, build, triage, final acceptance |
| **DETECTOR** | [`/book-detector`](.claude/skills/book-detector/SKILL.md) | independent QA / red team on sources + rendered PDF; only it marks issues VERIFIED |
| **FIXER** | [`/book-fixer`](.claude/skills/book-fixer/SKILL.md) | source verification; implements approved fixes; requests retest |

```
student prompts ─► MASTER ──QA_REQUEST──► DETECTOR ──ISSUE_REPORT──► MASTER (triage)
                     │                        ▲                          │
                     └──FIX_REQUEST──► FIXER ─┴──RETEST_REQUEST          │
                                                   shared Git repository = source of truth
```
Architecture: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) · protocol and log: [`docs/AGENT_COMMUNICATION.md`](docs/AGENT_COMMUNICATION.md)

## Vibe Coding process
Natural-language prompts → generated code → **run** → **inspect output** → refine. Real examples
from this project, each found by running and inspecting the output:
- The LaTeX prototype exposed a package-order error (biblatex before polyglossia) before the full book was written.
- A hand-written RTL helper double-reversed matplotlib's Hebrew text. matplotlib 3.11 already handles bidi, so the helper was removed.
- TikZ node text proved to be LTR under bidi. Visual checking was unreliable, so the project gained an automated position-based RTL probe, later extended to a whole-book, line-by-line audit.
- Student reviewers saw `"ייזה…"` and `קבוצת`: the text layer was correct, but the David font draws `״`, `"` and `'` like yods, and a colon kern merged `ה:` into `ת`. The fix: upright Gisha glyphs for quotes and geresh, and font-aware colon spacing.

### Final QA cycle (Detector ↔ Fixer)
| Step | Agent | Output |
|---|---|---|
| Full review + verification of the students' 11-item list | DETECTOR | [`Detector/reports/QA-R1.md`](Detector/reports/QA-R1.md): 0 CRITICAL, 2 MAJOR, 12 MINOR, 12 SUGGESTION; of the students' items, 1 real, 5 real-visual, 6 not reproduced |
| Source audit of every reference and claim | FIXER | [`Fixer/reports/SOURCE-AUDIT-R1.md`](Fixer/reports/SOURCE-AUDIT-R1.md): an unreadable AVMA page and misattributed heat-stroke signs were replaced with verified sources |
| Triage | MASTER | [`Master/work/TRIAGE-R1.md`](Master/work/TRIAGE-R1.md) |
| Fixes | FIXER | [`Fixer/reports/FIX-R1.md`](Fixer/reports/FIX-R1.md): all approved items fixed, still 20 pages |
| Independent retest | DETECTOR | [`Detector/reports/QA-R2.md`](Detector/reports/QA-R2.md): all R1 issues VERIFIED, no regressions → **QA_APPROVED** |

See [`docs/PROMPT_HISTORY.md`](docs/PROMPT_HISTORY.md) and [`docs/PROCESS_LOG.md`](docs/PROCESS_LOG.md).

## AI process documentation, Git history and collaboration
Added in response to the previous assignment's feedback (prompt [P-007](docs/prompts/Prompt_14.md)):
- **Every AI prompt in its own numbered file:** [`docs/prompts/`](docs/prompts/README.md) — 20 prompts (9 human, 11 Master→agent), exact text exported from the Claude Code transcripts by `scripts/export_prompts.py`, each with date/time, agent, purpose, result, files and follow-ups.
- **Central chronology:** [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md) — sessions, prompts, agent tasks, system events, builds, commits and pushes with exact times.
- **Git activity:** [`docs/GIT_LOG.md`](docs/GIT_LOG.md) — every commit (what/why), push and milestone tag; commit conventions `type(scope): summary` + why-body + `Refs:`.
- **Collaboration:** [`docs/COLLABORATION.md`](docs/COLLABORATION.md) — current evidence (one Git identity so far, no pulls yet) and the actions each team member must perform. Summary with statuses: [`docs/P007_FINAL_SUMMARY.md`](docs/P007_FINAL_SUMMARY.md).

## Build
Prerequisites: Python ≥ 3.11, a TeX distribution with XeLaTeX + biber (developed on MiKTeX 25.12),
and the Windows fonts David, Gisha, Arial and Courier New.
```powershell
pip install -r requirements.txt
python scripts/build_book.py          # figures → xelatex → biber → xelatex (until stable) → output/final_book.pdf
python scripts/check_rtl.py           # targeted RTL word-order probes
python scripts/audit_rtl_full.py      # whole-book RTL audit (source word pairs vs PDF)
python scripts/validate_project.py    # requirement checks → docs/VALIDATION_RESULTS.md
python scripts/generate_readme_images.py
```

## Repository
```
Master/ Detector/ Fixer/        agent role cards + work/ and reports/
.claude/skills/book-*/          the three Claude Code Skills
book/                           main.tex, preamble.tex, references.bib, frontmatter/, chapters/, backmatter/
figures/python | tikz | generated
scripts/                        build, validation, RTL probe, screenshots
docs/                           PRD, plan, architecture, logs, audit, QA, matrix, checklist
assets/readme/                  screenshots rendered from the PDF
output/final_book.pdf
```

## Documentation
[PRD](docs/PRD.md) · [Project plan](docs/PROJECT_PLAN.md) · [Requirements matrix](docs/REQUIREMENTS_MATRIX.md) ·
[Source audit](docs/SOURCE_AUDIT.md) · [QA report](docs/QA_REPORT.md) · [Issue tracker](docs/ISSUE_TRACKER.md) ·
[Self-assessment](docs/SELF_ASSESSMENT.md)

## Contributors
**ליה פורת ורוני ברק** · group code `liyaroni-ex2`. The content is informational and does not replace a veterinarian.

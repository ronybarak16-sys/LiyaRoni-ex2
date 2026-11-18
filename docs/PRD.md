# PRD — המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה

| Field | Value |
|---|---|
| Version | **v0.2 (Master, 2026-11-18)** — awaiting DETECTOR + FIXER review |
| Authors | ליה פורת ורוני ברק |
| Group code | liyaroni-ex2 |
| Owner | MASTER agent |
| Reviewers | DETECTOR (critical review), FIXER (feasibility, sources, risk) |
| Status | DRAFT |

Version history: see §20. Versions are bumped only when a real revision happens.

---

## 1. Product name
**המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה**
Subtitle: *בין פחמימות לטיולי לילה: המדריך השלם לבעלי כלבים עירוניים*

## 2. Overview
A short (≤ 20 pages) illustrated Hebrew handbook for urban dog owners, typeset in LaTeX,
with code-generated graphics, produced by a three-agent Claude Code workflow (Vibe Coding).
The deliverable is both a **book** (PDF) and a **document-engineering repository**.

## 3. Problem statement
Urban dog owners juggle small apartments, elevators, traffic, heat, and tight schedules.
Practical advice is scattered, often unsourced, and either too dry or too anecdotal.

## 4. Vision
A warm, funny, *accurate* guide that a first-time city dog owner reads in one evening and
keeps on the shelf. Humor carries the reader; sources carry the claims.

## 5. Target readers
First-time urban owners; apartment residents; owners of small/medium/large dogs; busy
professionals. Assumption: no professional background. Dogs differ by age, health,
temperament — the book never prescribes one-size-fits-all rules.

## 6. User needs
| ID | Need |
|---|---|
| UN-1 | Understand why the city can be stressful for some dogs and read body language |
| UN-2 | Choose good walking routes (shade, water, surface heat, traffic) |
| UN-3 | Organize gear and time for daily walks |
| UN-4 | Know what to do (and what *not* to do) in common incidents, incl. when to call a vet |

## 7. Scope
In: cover, abstract, TOC, introduction, 4 chapters, bibliography, production note; Python
graph; TikZ illustration; TikZ 8-block diagram; table; formula; callout boxes; README;
docs; validation scripts; Skills; agent collaboration evidence.

## 8. Out of scope
Veterinary diagnosis or treatment; breed-specific medical advice; named municipal rules
not verified by FIXER; nutrition plans; printed publication; English edition.

## 9. Functional requirements
| ID | Requirement | Acceptance |
|---|---|---|
| FR-1 | Title + subtitle exactly as specified | text extraction from p.1 |
| FR-2 | Cover page with original illustration | visual |
| FR-3 | Hebrew abstract (תקציר), ~150–220 words | word count + visual |
| FR-4 | Auto-generated Hebrew TOC (`\tableofcontents`) | no manual TOC in source |
| FR-5 | 4 chapters, one `.tex` file each, `\input` from `main.tex` | file check |
| FR-6 | Python (matplotlib) graph, vector PDF, values = script data | DETECTOR compares |
| FR-7 | ≥ 1 booktabs table (Chapter 2 environments comparison) | visual |
| FR-8 | ≥ 1 formula, LTR math inside RTL text (Chapter 3) | visual |
| FR-9 | Original object-based illustration from TikZ primitives | source in `figures/tikz/` |
| FR-10 | Flowchart with **exactly 8** blocks (Chapter 4) | count `\node[block` = 8 |
| FR-11 | ≥ 4 visually distinct callout box types (tcolorbox) | visual |
| FR-12 | Bibliography via biblatex/biber; only real, audited sources | SOURCE_AUDIT |
| FR-13 | Captions + source acknowledgments for every figure | visual |
| FR-14 | Page numbers + running headers | visual |
| FR-15 | Production note on Claude Code / Python / LaTeX / TikZ | back matter |

## 10. Non-functional requirements
- **≤ 20 physical pages** (target 16–19). Body font ≥ 10.5pt equivalent.
- Correct RTL everywhere; LTR only for math, URLs, English terms.
- Reproducible on Windows: one command `python scripts/build_book.py`.
- Deterministic figures (no randomness).
- No fabricated sources, data, communications or screenshots.

## 11. Content architecture & page budget
| Part | File | Pages (budget) |
|---|---|---|
| Cover | `book/frontmatter/cover.tex` | 1 |
| Abstract | `book/frontmatter/abstract.tex` | 1 |
| TOC | `main.tex` | 1 |
| Introduction | `book/frontmatter/introduction.tex` | 1 |
| Ch.1 Psychology of the urban dog | `book/chapters/chapter01_psychology.tex` | 3 |
| Ch.2 Mapping the terrain | `book/chapters/chapter02_city_mapping.tex` | 3 |
| Ch.3 Logistics & operations (graph, formula) | `book/chapters/chapter03_logistics.tex` | 3 |
| Ch.4 Survival guide FAQ (8-block diagram) | `book/chapters/chapter04_survival.tex` | 3 |
| Bibliography + production note | `book/backmatter/acknowledgments.tex` | 1–2 |
| **Total** | | **15–17** |

## 12. Design principles
Modern urban lifestyle guide. Palette: navy `#183153`, cream `#FFF8ED`, sage `#87A98C`,
coral `#E98B73`, gold `#D8B56A`, charcoal `#333333`. Designed chapter openers (colored band
+ chapter number + subtitle), cream page tint, rounded callouts, booktabs tables,
consistent captions. Decoration only where it aids reading.

## 13. LaTeX technical architecture
XeLaTeX + polyglossia (`hebrew` main, `english` other) + fontspec. Fonts: David (serif body),
Arial (sans headings/captions) — verified installed on the build machine (Phase 0).
Packages: geometry, xcolor, tcolorbox, tikz, titlesec, fancyhdr, booktabs, tabularx,
enumitem, graphicx, biblatex(biber), hyperref. `preamble.tex` holds all styles/macros.
Risk-sensitive combos (bidi + tikz, bidi + tcolorbox, biblatex in RTL) are prototyped first.

## 14. Python graphics requirements
`figures/python/create_graph.py`: explicit dataset dict, matplotlib, palette constants,
vector PDF to `figures/generated/activity_graph.pdf`. Hebrew labels are not rendered by
matplotlib (no bidi shaping) — axis labels use numbers/English short labels and the
Hebrew explanation lives in the LaTeX caption *(design decision, open for review)*.
Illustrative data flagged in caption.

## 15. Multi-agent architecture
Three live Claude Code sessions on the same machine and folder — `master`, `detector`,
`fixer` — each running its Skill. Communication with `ListAgents` + `SendMessage`.
Shared repository is the source of truth; messages carry file references only.

## 16. Responsibilities & permissions
| Agent | Writes | Approves |
|---|---|---|
| MASTER | book, figures, scripts, docs, README | triage, final acceptance |
| DETECTOR | `Detector/reports/`, QA_REPORT, tracker status | issue VERIFIED |
| FIXER | approved fixes, `Fixer/reports/`, SOURCE_AUDIT, references.bib | source VERIFIED |

## 17. Communication protocol
Structured message (MESSAGE_ID, TIMESTAMP, SENDER, RECIPIENT, TASK_ID, MESSAGE_TYPE,
SUBJECT, FILE_REFERENCES, REQUEST, EXPECTED_OUTPUT, STATUS). See `book-master` Skill.
Required start-up test: 6 directed links (M→D, M→F, D→M, D→F, F→M, F→D).

## 18. Source verification rules & QA process
Sources: veterinary associations, welfare organizations, government, peer-reviewed.
Statuses: VERIFIED / PARTIALLY VERIFIED / UNSUPPORTED / NEEDS CLARIFICATION / REMOVED.
QA: Draft → DETECTOR round 1 → MASTER triage → FIXER fixes → DETECTOR retest → repeat
until 0 open CRITICAL/MAJOR.

## 19. Acceptance criteria / deliverables / risks
**Acceptance**: gates A–F in `docs/FINAL_CHECKLIST.md`.
**Deliverables**: see `docs/REQUIREMENTS_MATRIX.md`.

| Risk | Impact | Mitigation |
|---|---|---|
| RTL breaks in TikZ/tcolorbox | broken diagrams | prototype first; `\begin{english}`/`\setLR` where needed |
| Hebrew in matplotlib renders reversed | wrong graph labels | keep Hebrew in LaTeX caption |
| Page count > 20 | fail | budget + measure each build |
| Fabricated/unsupported claims | academic integrity | FIXER audit before release |
| Detector/Fixer sessions not launched | Gate D fails | explicit launch instructions; no simulation |
| Instructor report template absent | missing deliverable | documented as blocker |

**Dependencies**: MiKTeX (XeLaTeX, biber), Python 3.11 + matplotlib/numpy/Pillow/PyMuPDF,
Windows fonts David/Arial.
**Assumptions**: none outstanding for metadata — authors ליה פורת ורוני ברק, group code liyaroni-ex2 (P-003).
**Constraints**: ≤ 20 pages; Hebrew; no remote push without approval.

**Milestones**: M0 inspection · M1 skills+PRD v0.1 · M2 LaTeX prototype · M3 first full draft
· M4 PRD review → v1.0 · M5 source audit · M6 QA round 1 + fixes · M7 retest · M8 docs/README · M9 release.

## 20. Version history
| Version | Date | Change | Trigger |
|---|---|---|---|
| v0.1 | 2026-11-18 | Initial definition | Master, from assignment brief |
| v0.2 | 2026-11-18 | Authors and group code added; NFR: RTL correctness verified by automated whole-book audit (`audit_rtl_full.py`) + visual check; callout titles use drawn icons, not punctuation glyphs | user prompt P-003 |

## 21. Traceability
Every assignment requirement → `docs/REQUIREMENTS_MATRIX.md` (file, page, method, result).

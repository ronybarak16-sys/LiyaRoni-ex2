# QA report

## Automated checks (master, reproducible by anyone)
| Check | Command | Latest result |
|---|---|---|
| Build | `python scripts/build_book.py` | success, 13 pages, 0 overfull hbox, 0 missing glyphs |
| RTL word order | `python scripts/check_rtl.py` | 18/18 probes PASS |
| Project validation | `python scripts/validate_project.py` | see `docs/VALIDATION_RESULTS.md` |

| Whole-book RTL audit | `python scripts/audit_rtl_full.py` | 1,830 source word pairs matched in PDF, 0 reversed |
| RTL probes (after C1) | `python scripts/check_rtl.py` | 25/25 PASS |

## Correction round C1 — user prompt P-003 (performed by MASTER; FIXER/DETECTOR sessions unavailable)

| ID | Original issue | Root cause | Modified files | Corrective action | Validation | Result |
|---|---|---|---|---|---|---|
| USR-01 | Cover showed placeholders for authors and group code | not yet supplied | `book/frontmatter/cover.tex`, `book/main.tex` (pdfauthor), README, PRD, CLAUDE.md | "מגישות: ליה פורת ורוני ברק", "קוד קבוצה: liyaroni-ex2"; code isolated as LTR run with `\textenglish{}` | word x-positions p.1 (מגישות→ליה→פורת→ורוני→ברק; קוד→קבוצה→:→liyaroni-ex2→·→2026) + render | PASS (master) |
| USR-02 | "!" at the start of warning-box titles (pp. 4, 8) | decorative glyphs `\textbf{!}`, `\textbf{i}`, `$\times$`, `+` placed as the first character of the RTL title | `book/preamble.tex` | replaced by drawn TikZ icons `\warnicon`, `\infoicon`, `\crossicon`, `\medicon` (baseline-aligned, cap height); full "!" audit: only one real "!" in the book (״הוא ידידותי!״, ch.1) — renders at the logical end | grep of all sources + render of pp. 4, 6, 8 | PASS (master) |
| USR-03 | p.9 checklist title displayed "הדלת ליד קבועה ציוד רשימת", left-aligned | tcolorbox title is set in vertical mode; its first item was a TikZ picture (`\paw`), so the paragraph began LTR under bidi → words reversed and line left-aligned. Same mechanism as the earlier FAQ-heading defect. | `book/preamble.tex` | global `\tcbset{before title={\leavevmode}}` (applies to every box, incl. inline ones); FAQ macro starts with `\leavevmode` (replaces earlier ad-hoc `\setRL`) | isolated 5-variant test (order + right edge x), bigram audit, render p.9 | PASS (master) — title right-aligned, correct order |
| USR-04 | `(ראו פרק 2 ו[5])` — vav prefix glued to a citation | prefix letter attached to an LTR/neutral bracket run | `book/chapters/chapter03_logistics.tex` | rephrased "(ראו פרק 2 ומקור [5])" | render p.10 | PASS (master) |
| USR-05 | Bibliography item 7 showed literal `--` | English font family loaded without TeX ligatures | `book/references.bib` | `{\textendash}` | render p.13 | PASS (master) |
| USR-06 | Regression during C1: page count 13 → 14 | new icons 2 pt taller than the glyphs they replaced | `book/preamble.tex` | icons scaled to cap height, explicit bounding box with no depth | per-line y diff vs. pre-fix PDF; 13 pages | PASS (master) |

Visual inspection: all 13 pages rendered (3-up sheets) and inspected after C1; pages 1, 4, 8, 9
additionally at 95–140 dpi. Mandatory elements (graph, table, formula, illustrations, 8-block diagram,
bibliography, TOC) unchanged and present.
**Independent verification by DETECTOR: NOT PERFORMED (session not running).**

## Independent QA rounds (DETECTOR)
| Round | Date | Scope | CRIT | MAJ | MIN | SUG | Report | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | — | full review A–P | — | — | — | — | `Detector/reports/QA-R1.md` | **NOT STARTED – detector session not running** |

Master's own pre-QA self-inspection findings are in `docs/ISSUE_TRACKER.md` (M-01…M-11). They are
not a substitute for independent review.

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

## Expansion round E1 — user prompt P-004 (performed by MASTER)
| Check | Result |
|---|---|
| Page count | **20** (build log + PyMuPDF) |
| TOC | one page (p.3), 4 minor sections intentionally excluded via `\secnotoc` |
| RTL | `audit_rtl_full.py`: 2,652 matched word pairs, 0 reversed; `check_rtl.py` 25/25 |
| Layout | 0 overfull boxes, 0 missing glyphs; all 20 pages visually inspected; fixes: emergency-card label column, cheat-sheet spacing/bullet colour, orphan last page removed |
| Content integrity | bibliography internal note removed (USR-07); production note no longer claims unperformed reviews (USR-08) |
| Validation | `validate_project.py` 0 FAIL |

**Independent verification by DETECTOR: NOT PERFORMED (session not running).**

## Correction round C2 — Hebrew review P-005 (performed by MASTER)
| ID | Reported | Root cause | Fix | Validation |
|---|---|---|---|---|
| USR-09 | `"ייזה…שלייי"`, `ייאף מול אףיי`, `ובלתיימים`, etc. (≈25 spots) | David's ״ glyph (and its `"`) look like two yods; text layer was correct | ״→`"`, ׳→`'` everywhere; `"` drawn with Gisha's upright glyph | 0 U+05F4 left; zoom renders |
| USR-10 | bullets shown as `.` | `\small` coral `$\bullet$` too small | `\textbullet` full size (lists + fridge sheet) | renders pp. 4, 13, 18 |
| USR-11 | `בבלגן :` | wide side bearing of David's `:`/`;` | XeTeX inter-char kern Hebrew letter → `:`/`;`; colons moved inside bold labels | renders p. 6, 16 (no collision with `)`) |
| USR-12 | reversed fridge-page footer | paragraph starting with TikZ `\paw` → LTR | `\leavevmode` inside `\paw`; audit gained per-line check (catches it on the old PDF) | audit: 0 bad lines |
| USR-13 | `Python,LaTeX` order, sentence ending in `Claude Code` | comma-separated English run inside RTL | sentence rewritten with Hebrew between the English terms | render p. 4 |
| USR-14 | ch.3 formula sentence unclear | sentence ended with inline math | rewritten so it ends in Hebrew | render p. 11 |
| USR-15 | graph labels `'20 דק` | abbreviation with geresh in matplotlib bidi | "20 דקות", `סה"כ` | render p. 12 |
| USR-16 | missing `:` after "טיפ מהשטח" | — | `fieldbox` title gets `:` | text layer |
| USR-17 | (found while checking) first table column lower than its row | `p{}` vs X top alignment | `m{}` columns for all tables | renders pp. 9, 10, 12, 16 |
| — | `בלה 2.2`, `[]6`, `$:24/7$`, `+` in emergency title | reviewer's OCR/text artefacts; page renders are correct | none | zoom renders |
| — | "גליות" → "רגליות" | "גליות" (wavy movement) is the intended word | none | — |

Result: 20 pages, 0 overfull boxes, `audit_rtl_full.py` 0 reversed / 0 bad lines, `check_rtl.py` 25/25,
`validate_project.py` 0 FAIL. **DETECTOR verification: NOT PERFORMED (session not running).**

## Independent QA rounds (DETECTOR)
| Round | Date | Scope | CRIT | MAJ | MIN | SUG | Report | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | — | full review A–P | — | — | — | — | `Detector/reports/QA-R1.md` | **NOT STARTED – detector session not running** |

Master's own pre-QA self-inspection findings are in `docs/ISSUE_TRACKER.md` (M-01…M-11). They are
not a substitute for independent review.

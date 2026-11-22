# Issue tracker

Prefixes: `M-` found by MASTER during self-inspection (Phase 7, before QA) · `DET-<round>-` found by
DETECTOR · `SRC-` found by FIXER's source audit.
Closing rule: an issue is **CLOSED** only after DETECTOR marks it VERIFIED.

| ID | Sev. | File | Problem | Owner | Status |
|---|---|---|---|---|---|
| M-01 | CRITICAL | book/preamble.tex | biblatex loaded before polyglossia → compile error | master | FIXED – awaiting DETECTOR verification |
| M-02 | MAJOR | book/preamble.tex | monospace font lacks Hebrew script → polyglossia error | master | FIXED – awaiting verification |
| M-03 | MAJOR | figures/python/create_graph.py | Hebrew labels double-reversed | master | FIXED – awaiting verification |
| M-04 | CRITICAL | book/frontmatter/cover.tex | cover TikZ nodes LTR: colon/brackets misplaced | master | FIXED – awaiting verification (`check_rtl.py` PASS) |
| M-05 | CRITICAL | figures/tikz/eight_block_diagram.tex | arrow labels reversed, then invisible after first fix | master | FIXED – awaiting verification |
| M-06 | MAJOR | book/frontmatter/introduction.tex | time `06:52` displayed `52:06` | master | FIXED – awaiting verification |
| M-07 | MAJOR | ch3, ch4, backmatter | maqaf before English/digits/math detached (`ב־Python`, `ו־10`) | master | FIXED by rephrasing – awaiting verification |
| M-08 | MINOR | book/references.bib | quotes shown as `?`; Hebrew note in law entry garbled | master | FIXED – awaiting verification |
| M-09 | MINOR | backmatter | URLs/paths overflow margin (4 overfull hboxes) | master | FIXED (0 overfull) – awaiting verification |
| M-10 | MINOR | figures/tikz/eight_block_diagram.tex | label "כן / לא בטוח" overlapped block 6 → shortened to "כן" (block 4 asks "is it *possible*") | master | FIXED – DETECTOR to judge safety wording |
| M-11 | SUGGESTION | whole book | 13 pages vs. 16–19 target in brief (max 20 respected) | master | RESOLVED by P-004: expanded to 20 pages with substantive content – awaiting DETECTOR review |
| USR-01 | MAJOR | cover.tex | author/group placeholders on cover | master (P-003) | FIXED – awaiting DETECTOR verification |
| USR-02 | MAJOR | preamble.tex | leading "!" (and i/×/+ glyphs) in callout titles, pp. 4, 8 | master (assigned to FIXER; session unavailable) | FIXED – awaiting verification |
| USR-03 | CRITICAL | preamble.tex (box titles) | p.9 checklist title reversed + left-aligned | master (assigned to FIXER; session unavailable) | FIXED (root cause) – awaiting verification |
| USR-04 | MINOR | chapter03_logistics.tex | vav prefix glued to citation | master | FIXED – awaiting verification |
| USR-05 | MINOR | references.bib | literal `--` in bibliography | master | FIXED – awaiting verification |
| USR-06 | MAJOR | preamble.tex | regression 13→14 pages during USR-02/03 fix | master | FIXED – awaiting verification |
| USR-07 | MINOR | references.bib | internal note "PENDING FIXER VERIFICATION" printed in the bibliography | master | FIXED (note removed; status tracked in SOURCE_AUDIT) – awaiting verification |
| USR-08 | MAJOR | backmatter/acknowledgments.tex | production note claimed Detector/Fixer reviews that have not happened | master | FIXED (describes the designed workflow; status in repo) – awaiting verification |

| USR-09…USR-17 | MAJOR/MINOR | see QA_REPORT round C2 | P-005 review: quote glyphs, bullets, colon spacing, reversed footer, mixed EN/HE sentence, formula sentence, graph labels, field-tip colon, table alignment | master | FIXED – awaiting DETECTOR verification |

Prefix `USR-` = reported by the students (prompt P-003) or found while fixing them.
DETECTOR and FIXER issues: none yet — sessions not started.

## DETECTOR round R1 issues (QA-R1 → retest QA-R2, 2026-11-22)
Status column maintained by DETECTOR. Evidence: `Detector/reports/QA-R1.md`, `Detector/reports/QA-R2.md`.

| ID | Sev. | File | Problem | Owner | Status |
|---|---|---|---|---|---|
| DET-1-01 | MAJOR | book/preamble.tex | colon fused into ה/ח/ת in Gisha / David Bold | fixer | VERIFIED (R2) |
| DET-1-02 | MAJOR | preamble + ch1/3/4, intro, appendix | David `'` reads as yod | fixer | VERIFIED (R2) |
| DET-1-03 | MINOR | preamble, ch1, acknowledgments | detached colon after `"`, `'`, digits, `}` | fixer | VERIFIED (R2) |
| DET-1-04 | MINOR | all chapters | `(פרק 2)` / refs split across lines | fixer | VERIFIED (R2) |
| DET-1-05 | MINOR | preamble (TOC) | leader dot glued to titles | fixer | VERIFIED (R2) |
| DET-1-06 | MINOR | preamble | `\emph` / `\itshape` invisible | fixer | VERIFIED (R2) |
| DET-1-07 | MINOR | figures/tikz/eight_block_diagram.tex | badge 4 hid arrowhead; label crowded badge 5 | fixer | VERIFIED (R2) |
| DET-1-08 | MINOR | ch1, ch2 | justified narrow cells, big word gaps | fixer | VERIFIED (R2) |
| DET-1-09 | MINOR | ch4 | emergency-card labels flush left | fixer | VERIFIED (R2) |
| DET-1-10 | MINOR | ch3 | `ראשון–רביעי` wrapped | fixer | VERIFIED (R2) |
| DET-1-11 | MINOR | preamble, scripts/build_book.py | "Rerun" warning in final log | fixer | VERIFIED (R2) |
| DET-1-12 | MINOR | references.bib | biblatex no driver for `legislation` | fixer | VERIFIED (R2) |
| DET-1-13 | MINOR | ch3, ch4 | "ערכת הכפילות" undefined | fixer | VERIFIED (R2) |
| DET-1-14 | MINOR | intro, ch2 | spelling חציה → חצייה | fixer | VERIFIED (R2) |
| DET-1-15 | SUGGESTION | ch2 | הגיאוגרפיה → הגאוגרפיה | fixer | VERIFIED (R2) |
| DET-1-16 | SUGGESTION | ch1 | repeated "לא מתוחה" | fixer | VERIFIED (R2) |
| DET-1-17 | SUGGESTION | ch3 | א'/ב' not introduced | fixer | VERIFIED (R2) |
| DET-1-18 | SUGGESTION | ch1 | "שש קומות" vs floors 3→7 | fixer | VERIFIED (R2) |
| DET-1-19 | SUGGESTION | ch3 | mixed numerals / English unit | fixer | VERIFIED (R2) |
| DET-1-20 | SUGGESTION | acknowledgments | sentences ending with English word | fixer | VERIFIED (R2) |
| DET-1-21 | SUGGESTION | preamble, references.bib | US dates; undated web sources | fixer | VERIFIED (R2) |
| DET-1-22 | SUGGESTION | build-wide | mirrored parens in text layer (info only) | master | CLOSED – NO ACTION per MASTER triage (informational) |
| DET-1-23 | SUGGESTION | preamble | cramped callout title tab | fixer | VERIFIED (R2) |
| DET-1-24 | SUGGESTION | acknowledgments | ו\en{Fixer} → ו-\en{Fixer} | fixer | VERIFIED (R2) |
| DET-1-25 | SUGGESTION | appendix | glossary not alphabetical | fixer | VERIFIED (R2) |
| DET-1-26 | SUGGESTION | introduction / bidi | `\endL/\endR` log warning | — | VERIFIED (R2) – accepted as known harmless bidi list warning (127, same as HEAD) |

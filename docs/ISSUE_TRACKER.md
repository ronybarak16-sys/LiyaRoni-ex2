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

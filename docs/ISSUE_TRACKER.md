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
| M-11 | SUGGESTION | whole book | 13 pages vs. 16–19 target in brief (max 20 respected) | master | OPEN – for PRD review; do not pad artificially |

DETECTOR and FIXER issues: none yet — sessions not started.

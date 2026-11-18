# Architecture

## 1. Build pipeline
```
figures/python/create_graph.py ───────► figures/generated/activity_graph.pdf ─────────┐
figures/python/create_illustration.py ─► figures/generated/original_neighborhood_map.pdf┤
figures/tikz/dog_illustration.tex  (\cityScene, \elevatorScene, pics) ─────────────────┤ \input
figures/tikz/eight_block_diagram.tex ──────────────────────────────────────────────────┤
book/preamble.tex (fonts, colors, boxes, headers, RTL helpers) ────────────────────────┤
book/frontmatter/*.tex  book/chapters/*.tex  book/backmatter/*.tex ────────────────────┤
book/references.bib ─────────────────────────── biber ─────────────────────────────────┤
                                                                                       ▼
                     book/main.tex ── xelatex → biber → xelatex → xelatex ──► build/main.pdf
                                                                                       │ copy
                                                                                       ▼
                                                                         output/final_book.pdf
                                                                                       │
              scripts/check_rtl.py · scripts/validate_project.py · scripts/generate_readme_images.py
```
One command: `python scripts/build_book.py` (fails if pages > 20).

## 2. LaTeX design decisions
| Decision | Reason |
|---|---|
| XeLaTeX + polyglossia (bidi) | stable Hebrew RTL; LuaLaTeX also installed but untested |
| David (body, scaled 1.12) + Gisha (headings) | installed Windows fonts with Hebrew script; Gisha = modern sans |
| `report` class, `secnumdepth=0` | numbered chapters in banner; clean unnumbered sections |
| tcolorbox callouts (6 styles) | breakable, RTL-safe |
| TikZ text: `rtlpar` style / `\RLE{}` | TikZ nodes are LTR under bidi (measured, see PROCESS_LOG #11) |
| biblatex numeric + biber, bibliography in `english` env | English sources typeset LTR |

## 3. Agent system
```
        ┌──────────── student (human prompts) ────────────┐
        ▼                                                 │
   ┌─────────┐  QA_REQUEST / RETEST_REQUEST   ┌──────────┐ │
   │ MASTER  │ ─────────────────────────────► │ DETECTOR │ │
   │ author  │ ◄───────────────────────────── │ QA / red │ │
   │ + PM    │   ISSUE_REPORT / QA_APPROVED   │  team    │ │
   └─────────┘                                └──────────┘ │
     │   ▲  FIX_REQUEST / SOURCE_AUDIT              ▲      │
     ▼   │  FIX_COMPLETED                RETEST_REQUEST    │
   ┌─────────┐ ─────────────────────────────────────┘      │
   │  FIXER  │  sources + approved fixes                    │
   └─────────┘                                              │
   Shared repository = source of truth (files referenced in every message)
```
Transport: Claude Code `ListAgents` + `SendMessage` between three local interactive sessions.
Skills: `.claude/skills/book-{master,detector,fixer}/SKILL.md`.

## 4. QA workflow
draft → DETECTOR round (A–P, page renders, log grep, RTL probes) → MASTER triage (approve/reject)
→ FIXER fix + rebuild → DETECTOR retest → VERIFIED / REOPENED → repeat until 0 open CRITICAL/MAJOR.

# Process log (chronological, real events only)

Times are local (2026-11-18), taken from file-system / git timestamps where available.
Agent = the Claude Code session that performed the action.

| # | Time | Agent | Activity | Result / evidence |
|---|---|---|---|---|
| 1 | ~20:53 | master | Phase 0 inspection: folder had only empty `Master/`, `Detector/`, `Fixer/` (capitalized); no git, no README, no Skills, no report template (also none in sibling `LiyaRoni-ex1`). | Environment: Python 3.11.9 (matplotlib 3.11.2, numpy 2.4.6, Pillow 13.0, PyMuPDF), MiKTeX 25.12 (XeLaTeX, LuaLaTeX, biber, latexmk), Windows fonts David, Gisha, Arial, Frank Ruehl, Tahoma, Courier New. |
| 2 | ~20:55 | master | `ListAgents` | "No reachable agents — no other Claude session is running on this machine" (peer messaging available). **detector / fixer not running.** |
| 3 | ~21:00 | master | `git init -b main`, `.gitignore`, folder skeleton, 3 Skills, CLAUDE.md, role cards, PRD v0.1 | Claude Code harness immediately listed `book-master`, `book-detector`, `book-fixer` as available skills (discovery confirmed). |
| 4 | 21:10 | master | Commit `cc384df`; user prompt P-002 authorised pushing to `github.com/ronybarak16-sys/LiyaRoni-ex2` | `git push -u origin main` → `* [new branch] main -> main` |
| 5 | 21:11 | master | Phase 4 LaTeX prototype (`Master/work/prototype/`) | Found 3 real defects: biblatex loaded before polyglossia (error), monospace font without Hebrew (error), ✗ glyph missing in Gisha. Fixed in preamble; prototype then compiled cleanly. Table `\midrule` printed as text in prototype (heredoc escaping) — not reproduced in the book. |
| 6 | 21:14 | master | Graph v1 with a manual string-reversal RTL helper | Rendered **double-reversed** Hebrew: matplotlib 3.11 already does bidi layout. Helper deleted; `matplotlib>=3.11` pinned. |
| 7 | 21:18 | master | TikZ dog/city illustration, elevator scene, 8-block diagram, Python neighborhood map | Map inspected visually — OK. |
| 8 | 21:16–21:25 | master | Wrote cover, abstract, introduction, chapters 1–4, back matter, bibliography (9 entries, **unaudited**) | — |
| 9 | ~21:26 | master | First full build (`scripts/build_book.py`) | Failed: `\square` undefined (needs amssymb), headheight too small. Fixed → 13 pages. |
| 10 | ~21:27 | master | Self-inspection of rendered pages (contact sheets) | Issues M-01…M-08 in `docs/ISSUE_TRACKER.md` (cover RTL, reversed time, maqaf before English, bibliography quotes, …). |
| 11 | ~21:28 | master | RTL investigation | Visual reading of Hebrew word order in rasters proved **unreliable**; wrote `scripts/check_rtl.py` that measures word x-positions. Minimal test showed TikZ node text is LTR by default and `\setRL` has no effect inside nodes; `\begin{RTL}` (wrapped) and `\RLE{}` (single line) work; `\beginR…\endR` made filled labels disappear. Final: 18/18 probes PASS. |
| 12 | ~21:29 | master | Bibliography font `\small`, URL breaking | 13 pages, 0 overfull boxes, 0 missing glyphs. |
| 13 | ~21:30 | master | Scripts `validate_project.py`, `generate_readme_images.py`; README screenshots rendered from the PDF | — |

## Pending (requires human action)
- Start the **detector** and **fixer** sessions (see `CLAUDE.md` → *Launching the agents*). Until then:
  PRD review, source audit, QA round 1, fixes and retest have **not** happened.

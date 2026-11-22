# Project: המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה

Authors: ליה פורת ורוני ברק · Group code: liyaroni-ex2

Hebrew illustrated LaTeX book (≤ 20 PDF pages) produced by three cooperating Claude Code
sessions: **master**, **detector**, **fixer**. Shared repository = single source of truth.

## Assignment (summary — full text in docs/PRD.md §Traceability)
Cover · Hebrew abstract · auto TOC · 4 chapters in separate files · Python graph · table ·
formula · original object-based illustration (TikZ) · 8-block diagram · callout boxes ·
real bibliography · README with real PDF screenshots · PRD · 3 Skills · real agent
communication · prompt history · QA reports · source audit · reproducible build.

## Agents
| Session name | Skill | Folder | Role |
|---|---|---|---|
| master   | `/book-master`   | `Master/`   | author, orchestrator, final acceptance |
| detector | `/book-detector` | `Detector/` | independent QA / red team, retests |
| fixer    | `/book-fixer`    | `Fixer/`    | source audit + approved fixes |

Note: the pre-existing agent folders are capitalized (`Master/`, `Detector/`, `Fixer/`);
they are kept as-is (Windows is case-insensitive; the brief's lowercase names map to them).

## Launching the agents
Mode actually used (2026-11-20 →): MASTER launches DETECTOR and FIXER as independent Claude Code
agents (Agent tool, own context, own Skill) and continues them with `SendMessage`; reports are files
in `Detector/reports/` and `Fixer/reports/`. Alternative (never used so far): separate terminals —
open two additional terminals in this folder and in each run `claude`, then:
- terminal 2: `/rename detector` then `/book-detector` — then: "wait for messages from master"
- terminal 3: `/rename fixer` then `/book-fixer` — then: "wait for messages from master"
The master session runs `ListAgents` to discover them and uses `SendMessage`.

## Build
```
pip install -r requirements.txt
python scripts/build_book.py        # figures + xelatex + biber + xelatex x2 -> output/final_book.pdf
python scripts/validate_project.py  # automated checks -> docs/VALIDATION_RESULTS.md
python scripts/generate_readme_images.py
```
Engine: XeLaTeX + polyglossia (Hebrew) + biblatex/biber. Fonts: David (body), Gisha (sans) — Windows system fonts.
RTL rules: TikZ wrapped nodes use style `rtlpar`, single-line nodes `\RLE{}`; never start a
paragraph/box title with a TikZ picture without `\leavevmode` (global for tcolorbox titles).
Check with `python scripts/audit_rtl_full.py` after every change.
Typography rules: use ASCII `"` and `'` (not ״ ׳) — `"` is drawn with Gisha automatically; never
end a Hebrew sentence with inline math or an English word if it can be avoided.

## Rules for every agent
- Never fabricate sources, messages, screenshots, test results or prompt history.
- Log real events: `docs/PROCESS_LOG.md`, `docs/AGENT_COMMUNICATION.md`, `docs/PROMPT_HISTORY.md`.
- Issues live in `docs/ISSUE_TRACKER.md`; only detector marks VERIFIED; only fixer marks sources VERIFIED.
- Do not push to any remote without explicit user approval.

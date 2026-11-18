# Prompt history (Vibe Coding record)

Only prompts that actually occurred are listed. Earlier history: none — the project started in
this session from three empty agent folders.

---
### P-001 — Master project prompt
- **Date/time:** 2026-11-18, ~20:53 · **Agent:** master (session `liyaroni-ex2-7f`) · **Phase:** all
- **Prompt (exact text):** the "MASTER PROJECT PROMPT — COMPLETE MULTI-AGENT LATEX BOOK PRODUCTION"
  (Parts 1–25: book specification, repo structure, three-agent architecture, Skills, real
  communication, Vibe Coding, PRD, chapter contents, LaTeX/RTL engineering, design system,
  Python, sources, README, QA, page budget, validation, Git, documentation, phases, gates).
  The full verbatim text is held by the students; *attach it as `docs/prompts/P-001.md`* —
  it is not reproduced here to avoid an unverifiable re-typing.
- **Purpose:** define the entire project.
- **Result:** Phases 0–7 executed by master (see `PROCESS_LOG.md` rows 1–13).
- **Problems discovered:** detector/fixer sessions not running → Gate D blocked.
- **Status:** in progress.

### P-002 — "uplod to git https://github.com/ronybarak16-sys/LiyaRoni-ex2.git"
- **Date/time:** 2026-11-18, ~21:10 · **Agent:** master
- **Purpose:** authorise publishing the repository to GitHub.
- **Result:** remote `origin` added; `git push -u origin main` succeeded (commit `cc384df`).
  Subsequent milestone commits are pushed to the same remote.
- **Status:** done.

---
## Internal refinement iterations (master, driven by P-001)
These are not new user prompts; they are the natural-language-guided iterations Claude made
after inspecting real output.

| ID | Trigger (observed output) | Refinement | Verification |
|---|---|---|---|
| R-01 | Prototype log: `biblatex Error: 'polyglossia' loaded after biblatex` | load order hyperref → polyglossia → biblatex | prototype recompiled, 0 errors |
| R-02 | Graph Hebrew double-reversed | removed manual reversal; rely on matplotlib ≥ 3.11 | rendered test string correct |
| R-03 | Cover subtitle colon/brackets misplaced | RTL inside TikZ overlay nodes | `check_rtl.py` cover probes PASS |
| R-04 | Flowchart labels in wrong order, then invisible | `\RLE{}` for single-line nodes, `RTL` env for wrapped nodes | 18/18 probes PASS + visual check |
| R-05 | Last page with 5 lines only | bibliography `\small` | 13 pages |

# Prompt history (Vibe Coding record)

> **Superseded (2026-11-22, P-007):** the authoritative record is now one file per prompt in
> [`docs/prompts/`](prompts/README.md) (exact text from the transcripts) and the central
> [`docs/DEVELOPMENT_HISTORY.md`](DEVELOPMENT_HISTORY.md). Correction (PROC-1-01): an **earlier session**
> (2026-11-18 20:13–20:52, two prompts, abandoned draft) preceded P-001 — the sentence below was wrong.

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

### P-003 — "MASTER PROMPT — FINAL CORRECTIONS, HEBREW RTL AUDIT, AND GIT SYNCHRONIZATION"
- **Date:** 2026-11-18 (after P-002) · **Agent:** master
- **Prompt (summary of its 9 tasks; full text held by the students):** (1) cover authors
  "מגישות: ליה פורת ורוני ברק" and group code "liyaroni-ex2"; (2) audit every "!" — leading
  exclamation marks in warning-box titles on pp. 4 and 8; (3) page 9 checklist title rendered
  reversed ("הדלת ליד קבועה ציוד רשימת") and mis-aligned; (4) RTL audit of all pages;
  (5) rebuild + visual validation; (6) FIXER fixes / DETECTOR final QA; (7) docs; (8) commit and
  push; (9) acceptance criteria.
- **Result:** see QA_REPORT "Correction round C1". Root cause of (3) found in the reusable box
  title mechanism and fixed globally; decorative "!"/"i"/"×"/"+" glyphs replaced by drawn icons;
  new whole-book audit `scripts/audit_rtl_full.py` (0 reversed of 1,830 matched word pairs).
- **Problem discovered:** P-001 RTL probes were hand-picked and missed the p.9 title → replaced by
  an exhaustive source-vs-PDF bigram audit.
- **Agents:** detector/fixer sessions still not running → fixes done by master; independent QA pending.
- **Status:** done except DETECTOR verification.

### P-004 — "add more pages to the book, i need that will be 20 pages at total"
- **Date:** 2026-11-20 · **Agent:** master
- **Purpose:** expand the book from 13 to exactly 20 PDF pages.
- **Decision:** add substantive content rather than padding (whitespace/font tricks), consistent
  with the brief's rule "never artificially expand".
- **Result:** new sections — ch.1 puppy exposure ladder (new TikZ figure) and home-alone; ch.2
  seasons table and dog-park etiquette; ch.3 example-week table and emergency bag; ch.4 five FAQs
  and a fill-in emergency card; appendices A (glossary) and B (fridge cheat sheet); an "About the
  book" page with credits, production note and agent-workflow diagram. 1 new reference (avsab-puppy).
- **Problems discovered and fixed:** first build 21 pp. (TOC spilled to 2 pages; 6-line orphan
  page) → compact TOC spacing, minor sections excluded from TOC (`\secnotoc`), back matter split
  into two balanced pages; TikZ style name `step` clashed with a built-in key; an internal
  "PENDING FIXER VERIFICATION" note was printed in the bibliography; the production note claimed
  Detector/Fixer reviews that had not happened (rewritten to describe the designed workflow).
- **Status:** done (20 pages); DETECTOR review and FIXER audit of the new claims C-19…C-24 pending.

### P-005 — Hebrew review of the 20-page PDF (quotes, bullets, punctuation, RTL, formula, tables)
- **Date:** 2026-11-20 · **Agent:** master
- **Prompt:** a Hebrew item-by-item review (sections 1 and 2; the pasted text was cut off mid-way
  through section 2). Reported e.g. `"ייזה הרגע…שלייי"`, bullets shown as `.`, `בבלגן :`, reversed
  fridge-page footer, `Python,LaTeX` ordering, graph labels `'20 דק`, `ובלתיימים` in the TOC.
- **Diagnosis:** the PDF text layer already contained correct ״/•, but the David font draws the
  gershayim (and even the ASCII `"`) as two slanted strokes that read as "יי"; the small coral
  bullet read as a period; David's colon/semicolon carry a wide side bearing; the footer was a real
  RTL defect (paragraph starting with a TikZ picture) that the audit missed because the same words
  appear correctly in every running header.
- **Fixes:** ״→`"` and ׳→`'` in all sources (76 + 16); `"` typeset with Gisha's upright glyph
  (active char, text layer keeps U+0022); full-size bullets; Hebrew-letter→colon/semicolon kern;
  colons moved inside bold labels (16); `\paw` starts with `\leavevmode` (root cause of the footer);
  audit now also flags individual mostly-reversed lines; intro English list and ch.3 formula sentence
  rewritten; field-tip label gets a colon; graph unit written in full ("20 דקות"); table cells
  vertically centred.
- **Not changed (already correct on the page, explained to the students):** `טבלה 2.2`, `[6]`,
  `24/7:` and the emergency-box title (the "+" is a drawn medical-cross icon); "גליות" (wavy) is the
  intended word, not "רגליות".
- **Status:** done; 20 pages; DETECTOR review still not possible (no session).

### P-006 — "הפעל את Detector ו-Fixer כדי לסגור את כל הליקויים…"
- **Date:** 2026-11-20 → 2026-11-22 · **Agent:** master (orchestrating detector + fixer)
- **Prompt (summary):** 11 remaining defects seen by the students (cover `קבוצת`, TOC, `מהשטת`, map
  label, `בלה 2.2`, missing n/i, `אי:/בי:`, `תוכנית בי`, `(פרק .(2`, `(Source Audit`, `3.1:` without
  איור); run a full Detector review, let Fixer fix every finding, retest until no open errors; update
  README; commit and push.
- **Execution:** no separate sessions existed, so MASTER launched DETECTOR and FIXER as independent
  Claude Code agents with their Skills. Real cycle: QA-R1 → SOURCE-AUDIT-R1 → TRIAGE-R1 → FIX-R1
  (interrupted by a usage limit, resumed) → MASTER independent re-check → QA-R2 = QA_APPROVED.
- **Key findings:** of the students' 11 items, 1 real, 5 real-visual (David's `'` looks like a yod; the
  P-005 colon kern made `ה:`/`ח:` look like `ת` in Gisha/David Bold), 6 not reproduced. Detector also
  found 20 further issues (spelling חצייה, "שש קומות" vs floors 3→7, TOC leaders, rerun warning…).
  Fixer's audit replaced an unreadable AVMA source and a misattributed heat-stroke list.
- **Status:** done — 0 open issues, 20 pages.

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
| R-06 | p.9 callout title reversed (P-003) | `\leavevmode` in `\paw` → fixed order but pushed a section to the next page (14 pp.) | page diff vs. saved pre-fix PDF |
| R-07 | regression from R-06 | moved fix to global `\tcbset{before title={\leavevmode}}` + FAQ macro; still 14 pp. | per-line y-position diff showed +2 pt in icon titles |
| R-08 | icon titles 2 pt taller | icons scaled to cap height with a baseline-aligned bounding box | 13 pages, identical line positions |

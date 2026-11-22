# P-007 — Process improvements after previous-assignment feedback: task assignment (MASTER)

Date: 2026-11-22 · Trigger: students' prompt "Additional Project Requirements – Previous Assignment Feedback".
Goal: fix the three weaknesses from the previous assignment —
(1) unstructured prompt documentation, (2) generic Git messages / undocumented VCS activity,
(3) no evidence of collaboration between the two team members.
Agents: the SAME existing DETECTOR and FIXER agents (resumed via SendMessage); no new agents, no role changes.
Statuses: Pending · In Progress · Completed · Requires Team Member Action.

## Facts established by MASTER before assigning (verified 2026-11-22)
- Session transcripts (Claude Code, local): `~/.claude/projects/C--VibeCoding-LiyaRoni-ex2/`
  - `03e07aff-….jsonl` — an EARLIER session, 2026-11-18 20:13–20:52 (local), 2 substantive prompts
    + "stop"/"resume" controls; not documented anywhere yet.
  - `60890c88-….jsonl` — this session (2026-11-18 → 2026-11-22), 7 human prompts incl. the mid-turn
    "uplod to git …" (stored as a `queue-operation` record).
  - `60890c88-…/subagents/agent-*.jsonl` — DETECTOR and FIXER transcripts.
- Git: 6 commits (cc384df … 5b39519), **all by one identity `ronybarak16-sys`**; pushes to
  `origin/main` after each commit; **no pull ever**; no second team-member identity.

## Assignment
| ID | Task | Agent | Files (write access) | Status |
|---|---|---|---|---|
| T-701 | Review existing prompt documentation; find missing/unnumbered/undocumented AI sessions (both transcripts, agent tasks) | DETECTOR | `Detector/reports/PROCESS-R1.md` (read-only elsewhere) | Completed |
| T-702 | Review Git history: message quality, pushes/pulls evidence (`git log`, `git reflog`, remote refs), identities, collaboration evidence | DETECTOR | same report | Completed |
| T-703 | Export every real prompt into separate numbered files `docs/prompts/Prompt_NN.md` (exact text from transcripts; 7 required fields) via a reproducible script `scripts/export_prompts.py` | FIXER | `docs/prompts/**`, `scripts/export_prompts.py` | Completed |
| T-704 | Central chronological development history `docs/DEVELOPMENT_HISTORY.md` (sessions, prompts, agent tasks, builds, commits/pushes) | FIXER | `docs/DEVELOPMENT_HISTORY.md` | Completed |
| T-705 | Git activity log `docs/GIT_LOG.md` (every commit/push with what & why; conventions for future commits) | FIXER | `docs/GIT_LOG.md` | Completed |
| T-706 | Apply MASTER-approved Detector recommendations (docs only) | FIXER | as approved | Completed |
| T-707 | Collaboration plan + exact actions for each team member | MASTER | `docs/COLLABORATION.md` | Completed |
| T-708 | Commit each real milestone with descriptive conventional messages; push; document | MASTER | git | Completed |
| T-709 | Final verification (9 checks) | DETECTOR → MASTER | `Detector/reports/PROCESS-R2.md` | Completed |
| T-710 | Team-member actions (own Git identities, commits, pulls, pushes) | **Students** | — | Requires Team Member Action |

## Rules given to the agents
- Never invent prompts, sessions, results, Git operations, identities or collaboration.
- Privacy: strip `<system-reminder>` blocks and any e-mail address from exported text; harness
  messages (e.g. "usage limit has reset") are recorded as system events, not human prompts.
- History is not rewritten (no amend/rebase/force-push); old commits are documented, not renamed.
- Agents do not run `git commit`/`push`; MASTER does, after reviewing.

_Status updated 2026-11-22 at P-007 closure: T-701…T-709 Completed (DETECTOR QA_APPROVED DET-T709b-001); T-710 Requires Team Member Action. Summary: `docs/P007_FINAL_SUMMARY.md`._

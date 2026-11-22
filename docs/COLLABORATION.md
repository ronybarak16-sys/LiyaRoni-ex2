# Team collaboration plan — ליה פורת & רוני ברק (group liyaroni-ex2)

Purpose: address the previous-assignment feedback "most of the work was performed under one account,
insufficient evidence of collaboration". This file states what the Git history shows **today** and the
concrete actions that **only the team members** can perform. No agent may simulate identities, commits,
pulls or pushes on a member's behalf.

## 1. Current evidence (verified by MASTER, 2026-11-22)
| Evidence | Status |
|---|---|
| Commits | 6 commits, **all by the Git identity `ronybarak16-sys`** |
| Pushes | after every commit, to `origin/main` (see `docs/GIT_LOG.md`) |
| Pulls / merges | **none** — the repository was only ever pushed from one clone |
| Second identity in history | **none** |
| Who typed each AI prompt | **not recorded** — transcripts do not identify the human; to be filled by the team in `docs/prompts/Prompt_NN.md` ("Submitted by") |

## 2. Proposed division of responsibilities (proposal — the team decides and edits this table)
| Area | ליה פורת | רוני ברק |
|---|---|---|
| Hebrew content and proofreading of the book | lead | review |
| Review of AI findings (Detector/Fixer reports) and approval decisions | shared | shared |
| Repository owner, build & figures (`scripts/`, `figures/`) | review | lead |
| Prompt documentation: confirm "Submitted by" in each `Prompt_NN.md` | own prompts | own prompts |
| Final submission checks | shared | shared |

## 3. Actions that require a team member — status: **Requires Team Member Action**
### רוני ברק (repository owner, Git identity `ronybarak16-sys`)
| # | Action | How |
|---|---|---|
| R-1 | Give Liya write access | GitHub → `ronybarak16-sys/LiyaRoni-ex2` → Settings → Collaborators → *Add people* → Liya's GitHub username |
| R-2 | After Liya's first push: **pull** her work | `git pull origin main` in your clone; check `git log --format="%h %an %s" -5` shows her commit |
| R-3 | Make your own reviewed contribution as a commit | e.g. review Liya's change or a doc you own; `git commit` with a conventional message (see `docs/GIT_LOG.md`) and `git push` |
| R-4 | Fill "Submitted by" in the prompt files you typed | edit `docs/prompts/Prompt_NN.md`, commit `docs: record prompt authorship (Rony)` |

### ליה פורת (needs her own GitHub account and Git identity)
| # | Action | How |
|---|---|---|
| L-1 | Use your own GitHub account; accept Rony's invitation | GitHub notification / e-mail |
| L-2 | Clone the repository with **your** identity | `git clone https://github.com/ronybarak16-sys/LiyaRoni-ex2.git` · `cd LiyaRoni-ex2` · `git config user.name "<your GitHub username>"` · `git config user.email "<your GitHub e-mail>"` (repository-local; if you work on the shared computer, use a separate clone folder so Rony's identity is not used) |
| L-3 | Make a real contribution | e.g. your Hebrew proofreading pass of a chapter (`book/chapters/…`) or the "Submitted by" fields of the prompts you typed; rebuild with `python scripts/build_book.py` if book sources change |
| L-4 | Commit and push under your name | `git add <files>` · `git commit -m "content: …"` (descriptive body) · `git pull --rebase origin main` · `git push origin main` |
| L-5 | Pull Rony's later changes | `git pull origin main` before each work session |

### Both
| # | Action |
|---|---|
| B-1 | Alternate work sessions with **pull → work → commit → push**, so the history shows both identities and real integration |
| B-2 | Record each joint milestone (who did what, which commits) in `docs/DEVELOPMENT_HISTORY.md` |
| B-3 | Tell MASTER when B-1…B-2 happened; DETECTOR will verify the identities and pulls in the Git history (final check T-709) |

## 4. What the AI agents will and will not do
- MASTER commits only the AI-session work it actually performed, under the identity configured on this computer.
- No agent will create commits under Liya's name, fake pulls/merges, or edit authorship metadata.
- DETECTOR verifies the evidence after the team acts; missing evidence stays marked **Requires Team Member Action**.

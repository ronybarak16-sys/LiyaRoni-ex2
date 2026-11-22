"""Export every real prompt of the project into numbered files docs/prompts/Prompt_NN.md.

Reproducible: re-run at any time; the files are regenerated from the Claude Code transcripts.

    python scripts/export_prompts.py [--transcripts DIR] [--out docs/prompts]

Sources (read-only):
  * main session transcripts   <DIR>/*.jsonl          (one per Claude Code session)
  * agent metadata             <DIR>/<session>/subagents/agent-*.meta.json  (agent id -> role)
  DIR defaults to ~/.claude/projects/C--VibeCoding-LiyaRoni-ex2

What counts as a prompt (numbered chronologically across all sessions):
  (a) HUMAN prompts: non-meta `user` records of the main thread whose text is not a control input
      or a harness event, plus `queued_command` attachments typed by a human mid-turn
      (e.g. "uplod to git ...", recorded as a queue-operation / attachment, not as a user record).
  (b) AGENT TASK prompts: the `prompt` of `Agent` tool calls and the `message` of `SendMessage`
      calls made by MASTER in a main transcript. The receiving agent (DETECTOR / FIXER) is taken
      from the agent's .meta.json (description) and the agent id.
NOT separate prompts (recorded under "Follow-up" of the latest prompt of the same session):
  control inputs ("stop", "resume", "continue"), harness events ("usage limit has reset",
  /rate-limit-options and its output, failed agent task-notifications).

Exact text: <pasted_content ...> wrapper tags are removed, the content is kept verbatim;
<system-reminder>...</system-reminder> blocks are removed (privacy).
Fields 4-7 (purpose, result, files, follow-up) are not in the transcripts. They come from the
ANNOTATIONS table below, which was compiled from docs/PROMPT_HISTORY.md, docs/PROCESS_LOG.md,
docs/AGENT_COMMUNICATION.md, the agent reports, `git show --stat`, `git reflog show origin/main`,
and (for session 03e07aff) that transcript's own tool calls. A prompt without an annotation gets
"Not recorded" - nothing is guessed.

Privacy gate: the script FAILS (exit 2, nothing written) if any e-mail address would be written.
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = Path.home() / ".claude" / "projects" / "C--VibeCoding-LiyaRoni-ex2"
TZ = ZoneInfo("Asia/Jerusalem")

CONTROL_INPUTS = {"stop", "resume", "continue"}
HARNESS_PREFIXES = ("<task-notification>", "<command-name>", "<local-command-stdout>",
                    "<local-command-caveat>", "Another Claude session sent a message")
HARNESS_PATTERNS = [re.compile(r"usage limit has reset", re.I)]
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SYSREM_RE = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
PASTED_RE = re.compile(r"</?pasted_content[^>]*>")

# --------------------------------------------------------------------------------------------
# Annotations (fields 4-7). Key = "<session id prefix 8>|<UTC timestamp to the second>".
# type: addition | correction | improvement | error fix | LLM guidance
# --------------------------------------------------------------------------------------------
NR = "Not recorded"
ANNOTATIONS = {
    "03e07aff|2026-11-18T18:13:07": dict(
        type="addition",
        summary="Earlier session: generic 'multi-agent LaTeX book swarm' prompt (Assignment 02)",
        purpose="Build a complete LaTeX book with a Master/Detector/Fixer multi-agent loop: custom class "
                "`book_style.cls`, Python charts, TikZ diagrams, Hebrew/English text, README, incident log. "
                "No book topic was given.",
        result="From this session's own tool calls: Claude chose the topic 'multi-agent AI systems', installed "
               "Python packages, downloaded the Heebo font into `fonts/`, wrote the class, chart scripts, "
               "`Master/build.py`, `Detector/audit.py`, `main.tex`, front matter and chapters 1-4. The turn was "
               "stopped by the user at 20:26 before the first compile (Claude's stop summary: \"The book is "
               "about half done, and I haven't compiled main.tex yet\").",
        abandoned=True,
        files="Written in this session (NOT persisted, see follow-up): book_style.cls, main.tex, "
              "frontmatter/{titlepage,colophon,preface}.tex, chapters/01-04, python/{palette,fig_reliability,"
              "fig_audit}.py, Master/build.py, Detector/audit.py, fonts/ (Heebo).",
        followup="None of these files survived: when session 60890c88 started (21:05) its first `ls` showed only "
                 "the three empty folders Master/, Detector/, Fixer/ (modified 20:53) and no git repository. "
                 "Who removed the files: Not recorded. This session is not mentioned in docs/PROMPT_HISTORY.md "
                 "(which says the project started from empty folders; PROC-1-01).",
    ),
    "03e07aff|2026-11-18T18:29:03": dict(
        type="addition",
        summary="Earlier session: continuation directive (chapters 5-7, quadratic formula, AAA.style.pdf)",
        purpose="Resume the paused build: write chapters 5-7 (final chapter must explain the quadratic formula), "
                "compile to `AAA.style.pdf`, run the Detector/Fixer loop, write README and logs.",
        result="Claude's final summary of the session (20:52): `AAA.style.pdf` 39 pages; 14 build+audit rounds, "
               "findings 115 -> 63 -> 10 -> 4 -> 1 -> 0; `incident_log.md` with 22 incidents; README with "
               "screenshots; one known overlap left in the topologies figure (the fixing edit was declined).",
        abandoned=True,
        files="Written (NOT persisted): chapters/05_red_team, 06_case_study, 07_principles.tex, "
              "frontmatter/glossary.tex, Master/{PRD,AGENT,ARCHITECTURE}.md, Detector/{AGENT,CHECKLIST}.md, "
              "Detector/{render_pages,test_rules}.py, Fixer/{AGENT,patch_log}.md, Fixer/verify.py, "
              "incident_log.md, README.md, plus edits to the class and chapters 1-4.",
        followup="All of this output was gone at 20:53 (see Prompt_01); who removed it: Not recorded. The "
                 "project actually submitted was started from scratch by Prompt_03 in session 60890c88.",
    ),
    "60890c88|2026-11-18T19:04:58": dict(
        type="addition",
        summary="MASTER PROJECT PROMPT: the dog-in-the-city Hebrew book, 3 agents, PRD, Skills, Git",
        purpose="Define the whole project: Hebrew book 'המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה' "
                "(<=20 pages), repository structure, three agents with Skills, real communication, PRD, "
                "chapter contents, LaTeX/RTL rules, Python figures, sources, README, QA, validation, Git, "
                "documentation, phases and gates (Parts 1-25).",
        result="MASTER phases 0-7: git repository, 3 Skills, role cards, CLAUDE.md, PRD v0.1, LaTeX preamble "
               "(commit cc384df 21:10:27), then the first complete 13-page draft with figures, build/"
               "validation/RTL scripts, docs and README (commit b1cec22 21:32:29, pushed 21:32:39). "
               "`ListAgents` found no detector/fixer session, so no agent work happened in this turn.",
        files="See `git show --stat cc384df` (11 files) and `git show --stat b1cec22` (48 files): "
              ".claude/skills/*, CLAUDE.md, */ROLE.md, docs/*, book/**, figures/**, scripts/*, README.md, "
              "assets/readme/*, output/final_book.pdf.",
        followup="docs/PROMPT_HISTORY.md (P-001) and docs/PROCESS_LOG.md give ~20:53 for the start; the "
                 "transcript timestamp of this prompt is 21:04:58 local. Gate D (agent communication) stayed "
                 "blocked until Prompt_08.",
    ),
    "60890c88|2026-11-18T19:10:14": dict(
        type="LLM guidance",
        summary="'uplod to git <repo URL>' typed mid-turn: publish the repository to GitHub",
        purpose="Authorise and request publishing the repository to the students' GitHub remote.",
        result="Delivered mid-turn (queue-operation 'absorbed_mid_turn'). Remote `origin` added and "
               "`git push -u origin main`: reflog shows origin/main = cc384df at 21:10:35. Every later "
               "milestone commit was pushed to the same remote.",
        files="No working-tree files (git remote configuration only).",
        followup="Typed with a typo ('uplod'); understood correctly. Recorded as P-002 in PROMPT_HISTORY.md.",
    ),
    "60890c88|2026-11-18T19:46:00": dict(
        type="error fix",
        summary="FINAL CORRECTIONS: cover authors/group code, '!' audit, reversed p.9 title, full RTL audit, push",
        purpose="Fix the cover credits (מגישות: ליה פורת ורוני ברק, קוד קבוצה liyaroni-ex2), remove leading "
                "'!' in box titles, fix the reversed/misaligned p.9 checklist title, audit RTL on every page, "
                "rebuild, document, commit and push.",
        result="Root cause of the reversed title found (tcolorbox titles starting with a TikZ picture began LTR); "
               "fixed globally; drawn icons instead of '!'/'i'/'x'/'+' glyphs; new scripts/audit_rtl_full.py "
               "(0 reversed of 1,830 word pairs); 13 pages. Commit 82e8261 21:56:27, pushed 21:56:30. "
               "DETECTOR/FIXER sessions still absent, so MASTER did FIXER's part.",
        files="`git show --stat 82e8261` (25 files): book/preamble.tex, book/frontmatter/cover.tex, "
              "scripts/audit_rtl_full.py, scripts/check_rtl.py, scripts/validate_project.py, docs/*, README.md, "
              "assets/readme/*, output/final_book.pdf.",
        followup="PROCESS_LOG.md row 14 says '~21:40'; transcript timestamp is 21:46:00. "
                 "Independent DETECTOR QA was left pending.",
    ),
    "60890c88|2026-11-20T10:29:25": dict(
        type="addition",
        summary="'add more pages to the book, i need that will be 20 pages at total'",
        purpose="Expand the book from 13 to exactly 20 PDF pages.",
        result="Substantive new content (no padding): puppy exposure ladder + home-alone (ch.1), seasons table "
               "and dog-park etiquette (ch.2), example week and emergency bag (ch.3), five FAQs and emergency "
               "card (ch.4), appendices A/B, 'About the book' page; one new reference (avsab-puppy). First build "
               "was 21 pages -> compact TOC, `\\secnotoc`. 20 pages. Commit cefcbb7 12:43:05, pushed 12:43:10.",
        files="`git show --stat cefcbb7` (28 files): book/chapters/*, book/backmatter/{appendix,acknowledgments}.tex, "
              "figures/tikz/exposure_ladder.tex, book/preamble.tex, book/references.bib, docs/*, README.md.",
        followup="New factual claims C-19...C-24 were left for the FIXER audit (done in Prompt_10).",
    ),
    "60890c88|2026-11-20T10:51:34": dict(
        type="correction",
        summary="Hebrew item-by-item review of the 20-page PDF (quotes, bullets, colons, RTL, graph, tables)",
        purpose="Correct the defects the students found in the PDF: quote marks read as 'יי', bullets read as "
                "periods, space before colons, reversed footer, graph labels, table/formula issues.",
        result="Diagnosis: the PDF text layer was correct; David's glyphs for \" and the small bullet were "
               "misread. Fixes: ASCII quotes drawn with Gisha's upright glyph, full-size bullets, Hebrew "
               "letter->colon kern, `\\paw` starts with `\\leavevmode` (footer root cause), per-line audit. "
               "20 pages. Commit 06ae08e 13:01:16, pushed 13:01:21.",
        files="`git show --stat 06ae08e` (25 files): book/preamble.tex, all chapters, introduction, appendix, "
              "figures/python/create_graph.py, scripts/audit_rtl_full.py, docs/*, CLAUDE.md, assets/readme/*.",
        followup="The pasted text was cut off in section 2 (recorded in PROMPT_HISTORY P-005). The colon kern "
                 "introduced here later made 'ה:'/'ח:' look like 'ת' in Gisha/David Bold (found by DETECTOR "
                 "in Prompt_09, fixed in Prompt_11).",
    ),
    "60890c88|2026-11-20T11:11:21": dict(
        type="error fix",
        summary="'Run Detector and Fixer': close the 11 remaining PDF defects, retest until clean, README, push",
        purpose="Have DETECTOR review the whole PDF (and the students' 11-item list), let FIXER fix every "
                "finding, retest until no open errors, update README, commit and push.",
        result="MASTER launched DETECTOR and FIXER as independent Claude Code agents (Prompt_09, Prompt_10), "
               "triaged their reports (Master/work/TRIAGE-R1.md), sent FIX_REQUEST (Prompt_11), resumed FIXER "
               "after a usage limit (Prompt_12), and requested a retest (Prompt_13) -> QA-R2 QA_APPROVED, "
               "0 open issues, 20 pages. Commit 5b39519 2026-11-22 22:02:59, pushed 22:03:05.",
        files="`git show --stat 5b39519` (163 files incl. evidence images): Detector/reports/*, Fixer/reports/*, "
              "Master/work/TRIAGE-R1.md, book/**, figures/tikz/eight_block_diagram.tex, scripts/build_book.py, "
              "scripts/validate_project.py, docs/*, README.md.",
        followup="Of the students' 11 items DETECTOR classified 1 real, 5 real-visual and 6 not reproduced "
                 "(QA-R1). The work was paused about 56 h by the account usage limit (see Prompt_11).",
    ),
    "60890c88|2026-11-20T11:12:26": dict(
        type="LLM guidance",
        summary="MASTER -> DETECTOR: QA round R1 (T-005), full review A-P + students' 11-item list",
        purpose="Independent QA of output/final_book.pdf and all sources; classify each of the students' "
                "11 items as REAL / REAL-VISUAL / NOT REPRODUCED with evidence.",
        result="Detector/reports/QA-R1.md: 26 findings (0 CRITICAL, 2 MAJOR, 12 MINOR, 12 SUGGESTION); "
               "students' list: 1 real, 5 real-visual, 6 not reproduced. Hand-back received 13:22 local.",
        files="Detector/reports/QA-R1.md, Detector/reports/R1_evidence/*, Detector/reports/pages_R1/*.",
        followup="Retest requested in Prompt_13 (QA-R2).",
    ),
    "60890c88|2026-11-20T11:12:40": dict(
        type="LLM guidance",
        summary="MASTER -> FIXER: source audit (T-004) of 10 bib entries and claims C-01...C-24",
        purpose="Verify every bibliography entry and factual claim against the real source (WebFetch/WebSearch); "
                "propose rewordings for unsupported claims; may correct bib metadata.",
        result="Fixer/reports/SOURCE-AUDIT-R1.md (message M-f-001): 7 VERIFIED, 11 PARTIALLY VERIFIED, "
               "3 NEEDS CLARIFICATION (AVMA page blocked by bot protection), 2 UNSUPPORTED; heat-stroke sign "
               "list found to match Humane World, not AVMA; references.bib metadata corrected; 20 pages. "
               "Hand-back received 13:27 local.",
        files="Fixer/reports/SOURCE-AUDIT-R1.md, docs/SOURCE_AUDIT.md, book/references.bib.",
        followup="MASTER approved the proposed changes in Master/work/TRIAGE-R1.md; applied in Prompt_11.",
    ),
    "60890c88|2026-11-20T11:27:38": dict(
        type="error fix",
        summary="MASTER -> FIXER: FIX_REQUEST R1 (T-006), fix approved DET-1-xx + apply source decisions",
        purpose="Implement every APPROVED item of TRIAGE-R1 (DET-1-01...25, source rewordings/citations) "
                "under hard constraints: 20 pages, 0 overfull, audits clean, validate 0 FAIL.",
        result="Edits applied, then the agent stopped: task-notification 13:52 local 'failed ... weekly limit'. "
               "Finished after the resume (Prompt_12): Fixer/reports/FIX-R1.md, 24 items fixed (DET-1-26 left, "
               "DET-1-22 no action), 16 verified bib entries, 20 pages, rerun warnings 0.",
        files="book/preamble.tex, book/references.bib, all chapters, introduction, appendix, acknowledgments, "
              "figures/tikz/eight_block_diagram.tex, scripts/build_book.py, scripts/validate_project.py, "
              "docs/SOURCE_AUDIT.md, Fixer/reports/FIX-R1.md, Fixer/reports/FIX-R1_evidence/*.",
        followup="The harness events above (failure, /rate-limit-options, reset) are SYSTEM EVENTS, not prompts; the work resumed with Prompt_12.",
    ),
    "60890c88|2026-11-22T19:53:59": dict(
        type="LLM guidance",
        summary="MASTER -> FIXER: resume T-006 after the usage-limit interruption",
        purpose="Continue FIX_REQUEST T-006 without redoing finished edits; run the full verification chain; "
                "write FIX-R1.md; reply FIX_COMPLETED + RETEST_REQUEST.",
        result="FIX_COMPLETED M-f-002 + RETEST_REQUEST M-f-003 received 21:56 local: build 20 pages, 0 overfull/"
               "undefined/rerun, RTL audit 2643/2643, 25/25 probes, validate 0 FAIL.",
        files="Fixer/reports/FIX-R1.md (written in this run); verification outputs (output/final_book.pdf, "
              "assets/readme/*, docs/VALIDATION_RESULTS.md).",
        followup="MASTER re-ran build/audits independently before forwarding the retest (AGENT_COMMUNICATION.md).",
    ),
    "60890c88|2026-11-22T19:56:57": dict(
        type="LLM guidance",
        summary="MASTER -> DETECTOR: RETEST_REQUEST round R2 (T-007) + regression scan",
        purpose="Independently retest every R1 issue and scan for regressions.",
        result="Detector/reports/QA-R2.md: all 26 R1 issues VERIFIED (DET-1-26 accepted, DET-1-22 no action), "
               "no new issues -> QA_APPROVED, 20 pages. Hand-back 22:01 local; commit 5b39519 at 22:02:59.",
        files="Detector/reports/QA-R2.md, Detector/reports/R2_evidence/*, Detector/reports/pages_R2/*.",
        followup="None recorded.",
    ),
    "60890c88|2026-11-22T20:10:54": dict(
        type="improvement",
        summary="Additional requirements from previous-assignment feedback: prompt docs, Git quality, collaboration",
        purpose="Without changing agents or architecture: numbered prompt documentation and a central work log, "
                "meaningful Git history with documented pushes/pulls, and genuine collaboration evidence for "
                "both team members.",
        result="T-701...T-710, see Master/work/TASKS-P007.md. "
               "MASTER split the work (Master/work/TASKS-P007.md: T-701...T-710), wrote docs/COLLABORATION.md and "
               "committed both (98eae31 22:13:09, pushed 22:13:12), then assigned T-701/702 to DETECTOR "
               "(Prompt_15) and T-703/704/705 to FIXER (Prompt_16). Remaining items in progress at export time.",
        files="Master/work/TASKS-P007.md, docs/COLLABORATION.md (commit 98eae31); later docs/prompts/*, "
              "docs/DEVELOPMENT_HISTORY.md, docs/GIT_LOG.md, scripts/export_prompts.py.",
        followup="T-710 (own Git identities, pulls, pushes by both students) is marked 'Requires Team Member Action'.",
    ),
    "60890c88|2026-11-22T20:12:23": dict(
        type="LLM guidance",
        summary="MASTER -> DETECTOR: T-701/T-702 independent review of prompt documentation and Git history",
        purpose="Read-only review: missing/unnumbered prompts and sessions, commit-message quality, push/pull "
                "evidence, identities and collaboration evidence.",
        result="Detector/reports/PROCESS-R1.md: 15 findings (0 CRITICAL, 6 MAJOR, 8 MINOR, 1 SUGGESTION); "
               "5 need team-member action (TM-1...TM-8). MASTER approved PROC-1-01...07, -13, -14 for FIXER (T-706, "
               "Prompt_17). @@STATUS:Detector/reports/PROCESS-R1.md@@",
        files="Detector/reports/PROCESS-R1.md.",
        followup="Approved recommendations go to FIXER as T-706.",
    ),
    "60890c88|2026-11-22T20:12:37": dict(
        type="improvement",
        summary="MASTER -> FIXER: T-703/704/705 numbered prompt files, development history, Git log",
        purpose="Export every real prompt into docs/prompts/Prompt_NN.md with a reproducible script; write "
                "docs/DEVELOPMENT_HISTORY.md and docs/GIT_LOG.md from real records only.",
        result="This export (scripts/export_prompts.py) plus docs/DEVELOPMENT_HISTORY.md and docs/GIT_LOG.md; "
               "not committed by FIXER (MASTER commits after review).",
        files="scripts/export_prompts.py, docs/prompts/Prompt_NN.md, docs/prompts/README.md, "
              "docs/DEVELOPMENT_HISTORY.md, docs/GIT_LOG.md.",
        followup="Extended by T-706 (Prompt_17) with the MASTER-approved DETECTOR findings.",
    ),
    "60890c88|2026-11-22T20:16:57": dict(
        type="correction",
        summary="MASTER -> FIXER: FIX_REQUEST T-706, fold approved DETECTOR findings (PROCESS-R1) into T-703..705",
        purpose="Apply PROC-1-01...07, -13, -14 as approved by MASTER: abandoned earlier session documented, one "
                "file per prompt incl. all MASTER->agent prompts, exact local+UTC times, harness events as SYSTEM "
                "EVENT rows, 'Submitted by (team member)' field, one GIT_LOG row per commit and per push, commit "
                "conventions.",
        result="Folded into this export, docs/DEVELOPMENT_HISTORY.md and docs/GIT_LOG.md (not committed by FIXER).",
        files="scripts/export_prompts.py, docs/prompts/*, docs/DEVELOPMENT_HISTORY.md, docs/GIT_LOG.md.",
        followup="PROC-1-08 and PROC-1-15 and COLLABORATION.md are handled by MASTER, not FIXER.",
    ),
}
TEAM_FIELD = "Requires Team Member Action — to be filled by ליה פורת / רוני ברק"


def local(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(TZ)


def clean(text: str) -> str:
    text = SYSREM_RE.sub("", text)
    text = PASTED_RE.sub("", text)
    return text.strip("\n").strip()


def user_text(rec):
    c = rec["message"]["content"]
    if isinstance(c, str):
        return c
    return "\n".join(p.get("text", "") for p in c if p.get("type") == "text")


def is_tool_result(rec):
    c = rec["message"]["content"]
    return isinstance(c, list) and any(p.get("type") == "tool_result" for p in c)


def load_roles(tdir: Path):
    """agent id -> role, toolUseId -> agent id (from subagents/*.meta.json)."""
    roles, by_tool = {}, {}
    for meta in tdir.glob("*/subagents/agent-*.meta.json"):
        aid = meta.name[len("agent-"):-len(".meta.json")]
        m = json.loads(meta.read_text(encoding="utf-8"))
        d = (m.get("description") or "").lower()
        roles[aid] = "DETECTOR" if "detector" in d else "FIXER" if "fixer" in d else NR
        if m.get("toolUseId"):
            by_tool[m["toolUseId"]] = aid
    return roles, by_tool


def scan(tdir: Path):
    roles, by_tool = load_roles(tdir)
    prompts, events = [], []
    for f in sorted(tdir.glob("*.jsonl")):
        sid = f.stem
        user_texts = []
        for line in f.open(encoding="utf-8"):
            r = json.loads(line)
            t = r.get("type")
            ts = r.get("timestamp", "")
            if r.get("isSidechain"):
                continue
            if t == "user" and not r.get("isMeta") and not is_tool_result(r):
                raw = user_text(r)
                txt = clean(raw)
                if not txt:
                    continue
                low = txt.lower()
                if low in CONTROL_INPUTS:
                    events.append(dict(session=sid, ts=ts, kind="control input", text=txt))
                elif txt.startswith(HARNESS_PREFIXES) or any(p.search(txt) for p in HARNESS_PATTERNS):
                    if txt.startswith("<task-notification>") and "<status>failed</status>" in txt:
                        summ = re.search(r"<summary>(.*?)</summary>", txt, re.S)
                        tool = re.search(r"<tool-use-id>(.*?)</tool-use-id>", txt)
                        events.append(dict(session=sid, ts=ts, kind="harness: agent run failed",
                                           text=summ.group(1) if summ else txt[:300],
                                           tool=tool.group(1) if tool else None))
                    elif txt.startswith("<task-notification>") or txt.startswith("Another Claude"):
                        continue  # routine agent hand-back notifications (results are in the reports)
                    elif txt.startswith("<local-command-caveat>"):
                        continue
                    else:
                        events.append(dict(session=sid, ts=ts, kind="harness event",
                                           text=re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", txt)).strip()))
                else:
                    user_texts.append((ts, txt))
                    prompts.append(dict(session=sid, ts=ts, kind="human", agent="MASTER", text=txt,
                                        how="user message"))
            elif t == "attachment":
                a = r.get("attachment", {})
                if a.get("type") == "queued_command" and (a.get("origin") or {}).get("kind") == "human":
                    txt = clean(str(a.get("prompt", "")))
                    if txt.lower() in CONTROL_INPUTS:
                        continue
                    prompts.append(dict(session=sid, ts=a.get("timestamp", ts), kind="human", agent="MASTER",
                                        text=txt, how="typed while MASTER was working; delivered mid-turn (queue-operation reason 'absorbed_mid_turn')"))
            elif t == "assistant":
                for p in r["message"].get("content", []):
                    if p.get("type") != "tool_use" or p["name"] not in ("Agent", "Task", "SendMessage"):
                        continue
                    inp = p["input"]
                    if p["name"] == "SendMessage":
                        aid = inp.get("to")
                        txt = inp.get("message", "")
                        how = "SendMessage from MASTER"
                    else:
                        aid = by_tool.get(p["id"])
                        txt = inp.get("prompt", "")
                        how = f"Agent tool call from MASTER (launch; description: {inp.get('description')})"
                    prompts.append(dict(session=sid, ts=ts, kind="agent task", agent=roles.get(aid, NR),
                                        agent_id=aid, tool_id=p["id"], text=clean(str(txt)), how=how))
    # de-duplicate a queued human prompt that also appears as a user record
    seen, uniq = set(), []
    for pr in sorted(prompts, key=lambda x: x["ts"]):
        k = (pr["session"], pr["text"], pr["ts"][:16])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(pr)
    for pr in uniq:
        pr["followups"] = []
    for ev in sorted(events, key=lambda x: x["ts"]):
        target = None
        if ev.get("tool"):
            target = next((p for p in uniq if p.get("tool_id") == ev["tool"]), None)
        if target is None:
            before = [p for p in uniq if p["session"] == ev["session"] and p["ts"] <= ev["ts"]]
            target = before[-1] if before else None
        if target is not None:
            target["followups"].append(ev)
    return uniq


def fence(text: str) -> str:
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def resolve(value: str) -> str:
    m = re.search(r"@@STATUS:(.+?)@@", value)
    if not m:
        return value
    path = ROOT / m.group(1)
    if path.exists():
        status = f"(Report present at export time: `{m.group(1)}`.)"
    else:
        status = f"(In progress at export time: `{m.group(1)}` does not exist yet.)"
    return value.replace(m.group(0), status)


def render(n, pr, total):
    key = f"{pr['session'][:8]}|{pr['ts'][:19]}"
    ann = ANNOTATIONS.get(key, {})
    dt = local(pr["ts"])
    if pr["kind"] == "human":
        who = (f"MASTER (main Claude Code session `{pr['session']}`); prompt typed by a team member "
               f"({pr['how']}).")
        submitted = (f"**Submitted by (team member):** {TEAM_FIELD} (the transcript does not identify "
                     "which team member typed it).")
        if ann.get("abandoned"):
            submitted += ("\n\n**Session status:** abandoned attempt; its output did not persist. "
                          f"**Why it was abandoned:** {TEAM_FIELD}.")
    else:
        who = (f"{pr['agent']} (agent `{pr.get('agent_id')}`, subagent transcript "
               f"`{pr['session']}/subagents/agent-{pr.get('agent_id')}.jsonl`); task issued by MASTER in "
               f"session `{pr['session']}` via {pr['how']}.")
        submitted = (f"**Submitted by (team member):** {TEAM_FIELD}. Issued by MASTER (Claude) during the "
                     "orchestration of a human prompt.")
    fu = []
    for ev in pr["followups"]:
        fu.append(f"- {local(ev['ts']):%Y-%m-%d %H:%M:%S} ({ev['kind']}): {ev['text']}")
    if ann.get("followup"):
        fu.append(f"- {ann['followup']}")
    if not fu:
        fu.append(f"- {NR}")
    f = fence(pr["text"])
    lines = [
        f"# Prompt {n:02d} of {total}",
        "",
        f"Type: **{ann.get('type', NR)}** · Kind: {pr['kind']} · "
        f"Source record: `{pr['session'][:8]}` {pr['ts']} (UTC)",
        "",
        "## 1. Date and time",
        f"{dt:%Y-%m-%d %H:%M:%S} {dt.tzname()} (Asia/Jerusalem) · {pr['ts'][:19].replace('T', ' ')} UTC",
        "",
        "## 2. Agent responsible",
        who,
        "",
        submitted,
        "",
        "## 3. Exact prompt",
        f"{f}text",
        pr["text"],
        f,
        "",
        "## 4. Purpose",
        ann.get("purpose", NR),
        "",
        "## 5. Actual result",
        resolve(ann.get("result", NR)),
        "",
        "## 6. Files affected",
        ann.get("files", NR),
        "",
        "## 7. Follow-up corrections",
        *fu,
        "",
        "---",
        "Generated by `scripts/export_prompts.py` from the Claude Code transcripts; fields 4-7 from the "
        "project records named in the script header. Do not edit by hand; re-run the script.",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcripts", type=Path, default=DEFAULT_DIR)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "prompts")
    args = ap.parse_args()
    prompts = scan(args.transcripts)
    total = len(prompts)
    files = {}
    for n, pr in enumerate(prompts, 1):
        files[f"Prompt_{n:02d}.md"] = render(n, pr, total)
    # index
    rows = ["| No. | Date (Asia/Jerusalem) | Session | Agent | Kind | Type | Summary |",
            "|---|---|---|---|---|---|---|"]
    counts = {}
    for n, pr in enumerate(prompts, 1):
        ann = ANNOTATIONS.get(f"{pr['session'][:8]}|{pr['ts'][:19]}", {})
        typ = ann.get("type", NR)
        counts[(pr["session"][:8], pr["kind"], typ)] = counts.get((pr["session"][:8], pr["kind"], typ), 0) + 1
        rows.append(f"| [{n:02d}](Prompt_{n:02d}.md) | {local(pr['ts']):%Y-%m-%d %H:%M} | `{pr['session'][:8]}` | "
                    f"{pr['agent']} | {pr['kind']} | {typ} | {ann.get('summary', NR)} |")
    crow = ["| Session | Kind | Type | Count |", "|---|---|---|---|"]
    for (s, k, t), c in sorted(counts.items()):
        crow.append(f"| `{s}` | {k} | {t} | {c} |")
    readme = "\n".join([
        "# Prompt documentation (numbered)",
        "",
        "One file per real prompt, numbered chronologically across all Claude Code sessions of the project.",
        "Generated by `python scripts/export_prompts.py` (re-run to refresh; do not edit the Prompt files by hand).",
        "",
        "- **Human prompts**: messages typed by the team in the main session (MASTER), including messages typed",
        "  mid-turn that Claude Code stores as queue operations.",
        "- **Agent task prompts**: tasks MASTER sent to DETECTOR or FIXER (`Agent` launch prompt or `SendMessage`).",
        "- **Not separate prompts**: control inputs (`stop`, `resume`) and harness events (usage-limit messages,",
        "  `/rate-limit-options`, failed-agent notifications). They are listed under *Follow-up corrections* of the",
        "  prompt they belong to.",
        "- Privacy: `<system-reminder>` blocks are removed and the export fails if any e-mail address would be",
        "  written. Times are local (Asia/Jerusalem) converted from the transcript UTC timestamps.",
        "",
        "## Sessions",
        "| Session | Period (local) | Note |",
        "|---|---|---|",
        "| `03e07aff` | 2026-11-18 20:13-20:52 | Earlier attempt (generic multi-agent book, `AAA.style.pdf`). Its files did not persist: the folder held only empty `Master/`, `Detector/`, `Fixer/` at 20:53. Not in PROMPT_HISTORY.md. |",
        "| `60890c88` | 2026-11-18 21:04 onward | The submitted project (MASTER); DETECTOR and FIXER run as agents of this session from 2026-11-20. |",
        "",
        "## Index",
        *rows,
        "",
        "## Counts",
        *crow,
        "",
    ])
    files["README.md"] = readme
    # privacy gate
    bad = [(name, m.group(0)) for name, txt in files.items() for m in EMAIL_RE.finditer(txt)]
    if bad:
        for name, addr in bad:
            print(f"PRIVACY FAIL: e-mail-like string in {name}: {addr[:3]}...")
        sys.exit(2)
    args.out.mkdir(parents=True, exist_ok=True)
    for old in args.out.glob("Prompt_*.md"):
        if old.name not in files:
            old.unlink()
    for name, txt in files.items():
        (args.out / name).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{total} prompt files written to {args.out}")
    for (s, k, t), c in sorted(counts.items()):
        print(f"  {s}  {k:<10} {t:<13} {c}")
    print("privacy scan: 0 e-mail addresses")


if __name__ == "__main__":
    main()

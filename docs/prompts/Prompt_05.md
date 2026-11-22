# Prompt 05 of 19

Type: **error fix** · Kind: human · Source record: `60890c88` 2026-11-18T19:46:00.300Z (UTC)

## 1. Date and time
2026-11-18 21:46:00 IST (Asia/Jerusalem) · 2026-11-18 19:46:00 UTC

## 2. Agent responsible
MASTER (main Claude Code session `60890c88-7e1f-4edc-b638-7fd79a4a4ada`); prompt typed by a team member (user message).

**Submitted by (team member):** Requires Team Member Action — to be filled by ליה פורת / רוני ברק (the transcript does not identify which team member typed it).

## 3. Exact prompt
```text
MASTER PROMPT — FINAL CORRECTIONS, HEBREW RTL AUDIT, AND GIT SYNCHRONIZATION

You are the MASTER agent responsible for the existing Hebrew LaTeX book project:

"המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה"

The book has already been created and compiled successfully. This is a targeted final correction and quality assurance task.

Do not recreate the book from scratch. Do not redesign the entire project. Preserve the existing content, illustrations, colors, typography, chapter structure, and overall visual appearance unless a specific correction is necessary.

Your mission is to implement the following corrections, coordinate verification with the existing Detector and Fixer agents, rebuild the PDF, thoroughly inspect Hebrew right-to-left rendering, update project documentation, and commit and push all approved changes to the existing Git repository.

TASK 1 — Update the cover page with the correct authors and group code

Locate the LaTeX source responsible for the first page (cover page).

Replace the existing author placeholders with the following exact information:

Authors: ליה פורת ורוני ברק

Group code: liyaroni-ex2

The cover should display the information in Hebrew as:

מגישות: ליה פורת ורוני ברק

קוד קבוצה: liyaroni-ex2

Requirements:

Replace all placeholders such as [שמות המחברים — יושלם] and [XXXXXXXX] where they refer to these exact details.
Ensure that the names are written in the correct order: ליה פורת first, followed by רוני ברק.
Do not translate or transliterate the Hebrew names into English.
Preserve the exact spelling and capitalization of liyaroni-ex2.
Ensure that the author names and group code are properly aligned within the existing cover layout.
Apply correct right-to-left direction to the Hebrew text.
Isolate the Latin group code as a left-to-right segment within the RTL line, so its characters and hyphen appear in the correct order.
Maintain adequate contrast and readability against the dark cover background.
Make sure there is no overlapping text, clipping, or unexpected line break.
Update any relevant project metadata, README, PRD, submission documentation, and report placeholders to use these same details.

If a metadata file already contains the correct information, preserve it and avoid duplicating conflicting values.

TASK 2 — Correct exclamation mark positioning throughout the entire book

There are existing punctuation problems in the Hebrew PDF, particularly involving exclamation marks (!) that appear in unnatural positions at the beginning of certain headings or labels.

For example, inspect the warning and informational callout boxes, including the callout headings on PDF pages 4 and 8.

Perform a complete audit of all exclamation marks throughout the entire book.

Requirements:

Identify every occurrence of the exclamation mark in LaTeX source files, reusable macros, TikZ labels, custom boxes, chapter headings, captions, and other rendered text.
Distinguish between an actual sentence-ending exclamation mark and a decorative warning symbol.
For genuine exclamatory sentences, place the punctuation logically after the final word, and verify that it is visually displayed at the correct end of the RTL sentence.
Do not leave a punctuation mark at the beginning of a Hebrew heading merely because a LaTeX command, LTR container, or bidirectional rendering issue moved it there.
For informational or warning boxes such as "שימו לב" and "הבהרה חשובה", preferably replace decorative leading exclamation marks with a properly positioned separate icon or graphic, or remove the unnecessary punctuation.
If a warning icon is retained, ensure it does not disrupt Hebrew text direction.
Do not add unnecessary exclamation marks simply to make headings more expressive.
Pay particular attention to text combining Hebrew, English, numbers, parentheses, and punctuation.
Verify that question marks, colons, periods, quotation marks, and parentheses are also correctly positioned.
Correct the underlying LaTeX formatting rather than manually inserting reversed strings or fragile visual workarounds.

Important: Hebrew is written right to left. Therefore, validate punctuation according to the actual logical end of each Hebrew sentence, not according to English left-to-right assumptions.

The final output must contain natural and professionally typeset Hebrew punctuation.

TASK 3 — Fix the reversed callout heading on PDF page 9

There is a specific RTL rendering problem on physical PDF page 9, in Chapter 3, under the section:

"הערכה הבסיסית"

The dark-blue checklist callout contains a heading that is rendered in reversed word order and is incorrectly positioned.

The intended heading is:

רשימת ציוד קבועה ליד הדלת

However, it currently appears in reversed order as:

"הדלת ליד קבועה ציוד רשימת"

This is unacceptable.

Correct both the text rendering and its alignment.

Requirements:

Locate the source code that generates this callout.
Identify whether the problem comes from the callout title macro, tcolorbox, a TikZ node, an explicit LTR direction, or another bidirectional text mechanism.
Preserve the exact intended Hebrew phrase: "רשימת ציוד קבועה ליד הדלת"
Ensure the heading is rendered in natural Hebrew reading order.
Align the title to the RIGHT side of the dark-blue callout header.
Ensure the title begins visually at the right side and flows toward the left, according to Hebrew RTL conventions.
Maintain the paw icon or existing decorative icon without disturbing the text direction.
If necessary, explicitly set the title content to RTL using a solution compatible with the existing XeLaTeX/polyglossia configuration.
Do not reverse the Hebrew words manually as a workaround.
Do not use \reflectbox or other transformations that visually mirror the text.
Do not alter the meaning of the title.
Preserve the existing callout colors, border, shape, and overall visual style.
Recompile the PDF and visually inspect the corrected page.

This issue may indicate a reusable macro problem rather than an isolated typo. Investigate the root cause carefully.

TASK 4 — Perform a comprehensive RTL audit across ALL pages

The page 9 error suggests that other Hebrew text elements may suffer from similar bidirectional rendering problems.

Perform a systematic RTL audit of the entire book, not just page 9.

Inspect:

Cover page.
Abstract.
Table of contents.
Chapter titles.
Section headings.
Subsection headings.
Informational callout boxes.
Callout title banners.
Numbered lists.
Bullet lists.
Checklists.
Table headers and table cells.
Figure captions.
Mathematical explanations.
Graph titles and labels.
TikZ illustrations.
The eight-block flowchart.
Bibliography headings and Hebrew descriptions.
Headers and footers.
Mixed Hebrew-English expressions.
Numbers, dates, and citations.

For every element, verify:

A. Correct Hebrew word order

Words must appear in their natural reading order, not reversed.

B. Correct text direction

Hebrew text must flow from right to left.

C. Correct horizontal alignment

Hebrew headings and relevant labels should be properly right-aligned unless the design intentionally uses centered alignment.

D. Correct punctuation

Punctuation must appear in a natural and typographically correct position.

E. Correct handling of English

Technical terms such as Python, LaTeX, TikZ, Claude Code, and mathematical notation must retain their proper left-to-right order when embedded in Hebrew sentences.

F. Correct handling of numbers and mathematical notation

Numbers, formulas, figure numbering, page numbering, and mathematical symbols must remain readable and logically ordered.

G. Correct handling of parentheses and quotation marks

Avoid mirrored or misplaced parentheses caused by bidirectional text problems.

H. Correct rendering in custom boxes

Special attention must be paid to reusable box macros, as these may inherit incorrect text direction.

Technical implementation requirements

Inspect the existing XeLaTeX and polyglossia configuration.

Identify the actual source of any RTL defects.

Use robust, maintainable LaTeX solutions.

Where appropriate, explicitly control Hebrew direction in custom components and their title fields.

Avoid arbitrary manual word reversal.

Avoid introducing Unicode directional control characters unnecessarily.

Do not solve one formatting problem by breaking another.

Make changes to reusable macros when a shared formatting issue is identified.

Preserve the existing typography, design system, font sizes, and spacing as much as possible.

TASK 5 — Recompile and visually validate the corrected PDF

After implementing the corrections:

Regenerate any affected figures if necessary.
Recompile the entire book using the existing build workflow.
Ensure bibliography and table of contents references are updated.
Confirm that the LaTeX build completes successfully.
Verify the exact PDF page count.
Ensure that the document still contains no more than 20 pages.
Render ALL PDF pages into images for visual inspection.
Inspect every page individually for RTL errors, clipping, overlapping text, or shifted objects.
Compare the corrected PDF against the previous version to identify unintended visual regressions.
Specifically verify physical pages 1, 4, 8, and 9.
Mandatory page-specific checks

Page 1 — Cover

Verify that the cover correctly displays:

ליה פורת
רוני ברק
liyaroni-ex2

Remove all previous placeholders related to these fields.

Page 4 — Warning box

Verify that the warning title and any exclamation icon are correctly positioned and that Hebrew punctuation is natural.

Page 8 — Warning box

Verify the same punctuation and RTL corrections.

Page 9 — Checklist box

Verify that the dark-blue callout title displays exactly:

"רשימת ציוד קבועה ליד הדלת"

Confirm the title is correctly right-aligned and is not visually reversed.

Additional checks

Search the PDF's extracted text for the intended phrases, but do not rely exclusively on text extraction to assess visual RTL rendering.

Use actual page renderings as the final visual reference.

Preserve all mandatory book elements, including the Python graph, table, mathematical formula, original illustrations, eight-block diagram, bibliography, and table of contents.

Do not accept the revised version until the targeted defects have been visually verified as corrected.

TASK 6 — Coordinate final review with Detector and Fixer

Use the existing multi-agent architecture.

Do not create fictional agent responses.

Assign the required work as follows:

MASTER

Coordinates all changes.
Updates author and group details.
Maintains project consistency.
Integrates changes.
Rebuilds the final PDF.
Performs final acceptance.
Manages Git synchronization.

FIXER

Investigates and corrects the exclamation mark issues.
Fixes the page 9 reversed callout title.
Repairs any additional RTL defects.
Reports modified files and explanations.

DETECTOR

Independently reviews the updated PDF.
Checks all pages for remaining RTL errors.
Verifies the cover information.
Confirms the specific issues on pages 4, 8, and 9 are resolved.
Checks for layout regressions.
Produces a final QA report.

Use genuine Claude Code inter-agent messages if the corresponding independent sessions are available.

If the sessions are unavailable, report the blocker accurately rather than fabricating collaboration.

The Master must approve the final result only after real verification.

TASK 7 — Update all project files and documentation

Once the PDF is correct, update all relevant project files.

This includes, where applicable:

Cover page LaTeX source.
Any affected chapter files.
Reusable callout macros.
Main LaTeX configuration.
Final PDF.
README.
PRD.
Group metadata.
Requirement verification matrix.
QA report.
Issue tracker.
Prompt history.
Process documentation.
Final checklist.

Add an authentic entry to the prompt history documenting this correction request.

Update the QA report with:

Original issue.
Root cause.
Modified source files.
Corrective action.
Validation method.
Final verification result.

Regenerate README screenshots from the NEW final PDF if the existing screenshots contain any changed pages.

Do not keep outdated screenshots in the README.

Do not overwrite unrelated project content.

TASK 8 — Update Git and GitHub

After all corrections have been implemented and verified, synchronize the project with the existing Git repository.

This is a mandatory final step.

Git procedure
Inspect the repository status using git status.
Check the current branch.
Inspect the existing remote configuration using git remote -v.
Review the changed files.
Ensure no credentials, secrets, temporary build artifacts, or unrelated personal files are staged.
Stage all relevant, approved project changes.
Create a descriptive Git commit.

Suggested commit message:

Fix Hebrew RTL layout, update authors and group metadata, and finalize PDF

Push the commit to the existing configured remote branch if available and authorized.
Confirm the push result.
Verify the final repository status and commit hash.

Important Git safety rules:

Do not delete existing Git history.
Do not force-push.
Do not change the existing remote URL unnecessarily.
Do not create a new repository when an appropriate repository already exists.
Do not overwrite unrelated work.
Do not claim a successful push if authentication or network access prevented it.
If pushing fails, report the exact reason and the command required to finish synchronization.
If no remote repository is configured, complete the local commit and report that a remote is required.

The final PDF and all necessary source files must be included in the Git changes.

TASK 9 — Final acceptance criteria

Do not declare the task complete until the following conditions are verified:

Cover includes ליה פורת.
Cover includes רוני ברק.
Cover includes the exact code liyaroni-ex2.
All relevant placeholders have been replaced.
Exclamation marks are correctly positioned.
Page 9 callout title is correctly displayed.
Page 9 callout title is right-aligned.
Hebrew word order is correct throughout the PDF.
Mixed Hebrew-English text is readable.
Tables, figures, labels, captions, and diagrams display correctly.
Final PDF compiles successfully.
PDF does not exceed 20 pages.
No new layout problems were introduced.
Documentation is updated.
Final PDF screenshots are current.
Detector has completed independent QA, if its live session is available.
Relevant corrections have been committed to Git.
Changes have been pushed to the existing GitHub remote, if configured and authorized.
FINAL OUTPUT REPORT

At the end, provide a concise but accurate report containing:

List of changes made.
Files modified.
Confirmation of corrected author names and group code.
Explanation of the original RTL problem and how it was resolved.
Confirmation of the page 9 callout correction.
Final PDF path.
Final PDF page count.
QA verification results.
Git commit hash.
Current branch.
GitHub push status.
Any remaining issues or actions that require user intervention.

BEGIN NOW. Inspect the existing files, apply the required corrections, rebuild the PDF, perform the final RTL audit, and synchronize the approved project changes with Git. Do not stop after merely explaining what should be done.
```

## 4. Purpose
Fix the cover credits (מגישות: ליה פורת ורוני ברק, קוד קבוצה liyaroni-ex2), remove leading '!' in box titles, fix the reversed/misaligned p.9 checklist title, audit RTL on every page, rebuild, document, commit and push.

## 5. Actual result
Root cause of the reversed title found (tcolorbox titles starting with a TikZ picture began LTR); fixed globally; drawn icons instead of '!'/'i'/'x'/'+' glyphs; new scripts/audit_rtl_full.py (0 reversed of 1,830 word pairs); 13 pages. Commit 82e8261 21:56:27, pushed 21:56:30. DETECTOR/FIXER sessions still absent, so MASTER did FIXER's part.

## 6. Files affected
`git show --stat 82e8261` (25 files): book/preamble.tex, book/frontmatter/cover.tex, scripts/audit_rtl_full.py, scripts/check_rtl.py, scripts/validate_project.py, docs/*, README.md, assets/readme/*, output/final_book.pdf.

## 7. Follow-up corrections
- PROCESS_LOG.md row 14 says '~21:40'; transcript timestamp is 21:46:00. Independent DETECTOR QA was left pending.

---
Generated by `scripts/export_prompts.py` from the Claude Code transcripts; fields 4-7 from the project records named in the script header. Do not edit by hand; re-run the script.

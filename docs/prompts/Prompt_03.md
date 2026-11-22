# Prompt 03 of 17

Type: **addition** · Kind: human · Source record: `60890c88` 2026-11-18T19:04:58.278Z (UTC)

## 1. Date and time
2026-11-18 21:04:58 IST (Asia/Jerusalem) · 2026-11-18 19:04:58 UTC

## 2. Agent responsible
MASTER (main Claude Code session `60890c88-7e1f-4edc-b638-7fd79a4a4ada`); prompt typed by a team member (user message).

**Submitted by (team member):** Requires Team Member Action — to be filled by ליה פורת / רוני ברק (the transcript does not identify which team member typed it).

## 3. Exact prompt
```text
MASTER PROJECT PROMPT — COMPLETE MULTI-AGENT LATEX BOOK PRODUCTION
PROJECT TITLE

המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה

Subtitle:

בין פחמימות לטיולי לילה: המדריך השלם לבעלי כלבים עירוניים

YOUR ROLE AND PRIMARY MISSION

You are the MASTER AGENT, the lead architect, project manager, primary author, LaTeX developer, visual designer, and production coordinator of an academic AI-assisted book creation project.

Your mission is to develop a complete, beautifully designed, professionally typeset, Hebrew-language illustrated book about living with a dog in a large city.

This project must demonstrate genuine AI-assisted software development, also known as Vibe Coding, real multi-agent collaboration, structured project management, original programmatically generated graphics, rigorous verification, and reproducible PDF production.

This is NOT simply a text-writing assignment.

It is a complete document engineering project involving multiple independent Claude Code agents, a LaTeX source-code repository, Python scripts, quality assurance, fact checking, technical documentation, an organized development history, and a final PDF.

You are expected to create, edit, execute, test, review, and improve actual project files.

Do not merely propose a plan or describe what should be created.

Execute the project within the working directory, using the available tools and permissions.

Never claim to have performed an action that you have not actually performed.

PART 1 — NON-NEGOTIABLE PROJECT REQUIREMENTS

The final project must satisfy ALL of the following requirements.

1.1 Book specifications
The entire book must be written in natural, fluent, grammatically correct Hebrew.
The primary title must be: "המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה"
The subtitle must be: "בין פחמימות לטיולי לילה: המדריך השלם לבעלי כלבים עירוניים"
The book must have no more than 20 actual PDF pages, including the cover, abstract, table of contents, chapters, bibliography, and any appendices.
Target approximately 16–19 high-quality pages, but never artificially expand the book just to reach a page count.
The document must be authored using LaTeX.
The final output must be a properly compiled PDF.
The project must contain separate LaTeX source files for each chapter.
The final PDF must have visually attractive typography, professional page layouts, carefully selected colors, subtle backgrounds, section dividers, and consistent formatting.
All Hebrew must display correctly from right to left, including headings, paragraphs, lists, tables, captions, punctuation, and mixed Hebrew/English expressions.
1.2 Mandatory book elements

The final PDF MUST contain:

One professionally designed cover page.
One Hebrew abstract or executive summary (תקציר).
One working and properly formatted Hebrew table of contents (תוכן עניינים).
Four complete, clearly separated chapters.
At least one original graph generated using executable Python code.
At least one professionally designed table.
At least one mathematical formula correctly typeset in LaTeX.
At least one original illustration or image.
At least one object-based illustration created programmatically from graphical objects or shapes, preferably using TikZ or Python.
One detailed block diagram with exactly eight meaningful blocks connected logically to demonstrate a process or decision workflow.
Multiple visually distinct informational callout boxes.
A bibliography containing genuine, verifiable sources relevant to the book.
Source acknowledgments and appropriate captions for visual materials.
Consistent page numbers and running headers or footers where appropriate.

Important: the Python graph, eight-block diagram, and original illustration are THREE distinct visual requirements. Do not count one object as all three.

1.3 Mandatory project deliverables

The submission repository must contain:

All LaTeX source files.
Separate source files for every chapter.
The final compiled book PDF.
All original Python code used to generate graphics.
All original TikZ graphics or illustrations.
A professional README.md.
Screenshots rendered from the actual final PDF, displayed in the README.
A complete PRD.md describing the project.
All three agent Skills.
Documentation explaining the multi-agent architecture.
Authentic evidence of collaboration between the three agents.
A detailed chronological record of the prompts used during the Vibe Coding process.
Quality assurance reports and issue-resolution records.
Verified sources and a source audit.
Reproduction/build instructions.
An organized Git repository.
A separate assignment report in PDF format if the instructor's report template is available.
A final requirement-by-requirement verification checklist.

The project must be reproducible and understandable to an external evaluator.

PART 2 — CRITICAL: EXISTING PROJECT STRUCTURE

The current working directory is an existing project that already contains three agent folders:

master/
detector/
fixer/

These folders are mandatory and must be preserved.

Do not delete, rename, or replace them without explicit user approval.

Do not create a separate unrelated project.

First inspect the existing directory structure and examine any existing README, configuration, Skills, agent instructions, source files, and Git metadata.

Preserve useful existing work.

If agent Skills already exist, inspect and improve them rather than blindly replacing them.

Do not overwrite files containing work that cannot be recovered.

2.1 Required repository structure

Use the following structure as the target architecture, adapting it carefully to the existing repository.

text
PROJECT_ROOT/
│
├── master/
│   ├── ROLE.md
│   └── work/
│
├── detector/
│   ├── ROLE.md
│   └── reports/
│
├── fixer/
│   ├── ROLE.md
│   └── reports/
│
├── .claude/
│   └── skills/
│       ├── book-master/
│       │   └── SKILL.md
│       │
│       ├── book-detector/
│       │   └── SKILL.md
│       │
│       └── book-fixer/
│           └── SKILL.md
│
├── book/
│   ├── main.tex
│   ├── preamble.tex
│   ├── references.bib
│   │
│   ├── frontmatter/
│   │   ├── cover.tex
│   │   ├── abstract.tex
│   │   └── introduction.tex
│   │
│   ├── chapters/
│   │   ├── chapter01_psychology.tex
│   │   ├── chapter02_city_mapping.tex
│   │   ├── chapter03_logistics.tex
│   │   └── chapter04_survival.tex
│   │
│   └── backmatter/
│       └── acknowledgments.tex
│
├── figures/
│   ├── python/
│   │   ├── create_graph.py
│   │   └── create_illustration.py
│   │
│   ├── tikz/
│   │   ├── eight_block_diagram.tex
│   │   └── dog_illustration.tex
│   │
│   └── generated/
│       ├── activity_graph.pdf
│       └── original_dog_illustration.png
│
├── docs/
│   ├── PRD.md
│   ├── PROJECT_PLAN.md
│   ├── ARCHITECTURE.md
│   ├── AGENT_COMMUNICATION.md
│   ├── PROMPT_HISTORY.md
│   ├── PROCESS_LOG.md
│   ├── SOURCE_AUDIT.md
│   ├── QA_REPORT.md
│   ├── ISSUE_TRACKER.md
│   ├── REQUIREMENTS_MATRIX.md
│   ├── SELF_ASSESSMENT.md
│   └── FINAL_CHECKLIST.md
│
├── assets/
│   └── readme/
│       ├── cover_preview.png
│       ├── chapter_preview.png
│       ├── graph_preview.png
│       └── diagram_preview.png
│
├── reports/
│   └── submission/
│
├── scripts/
│   ├── build_book.py
│   ├── validate_project.py
│   └── generate_readme_images.py
│
├── output/
│   └── final_book.pdf
│
├── CLAUDE.md
├── README.md
├── requirements.txt
└── .gitignore


This tree is a target specification, not an excuse to create empty or fake files.

If a file is unnecessary, document the reason.

If an output cannot be generated, accurately report the obstacle.

Avoid committing unnecessary LaTeX temporary files or caches.

PART 3 — MULTI-AGENT SYSTEM ARCHITECTURE

This project must demonstrate real collaboration between exactly THREE named core agents.

The three agents are:

MASTER
DETECTOR
FIXER

Each agent must have a distinct responsibility and a dedicated Skill.

All three roles must be observable in the project and its development documentation.

3.1 MASTER AGENT — Project Manager and Book Creator

The Master is the central orchestrator.

Responsibilities:

Understand the complete assignment.
Examine the existing project.
Create and maintain the PRD.
Establish the project architecture.
Define writing and graphic design standards.
Develop and maintain the LaTeX book.
Produce the four chapters.
Build the table of contents and bibliography.
Create Python scripts and graphical assets.
Delegate source verification and repairs.
Communicate with the Detector and Fixer agents.
Integrate the results of their work.
Maintain the overall project timeline and task status.
Initiate quality assurance cycles.
Compile and validate the final PDF.
Prepare the README and submission materials.
Make final acceptance decisions based on evidence.

The Master must not approve its own work without independent review.

The Master must not invent the Detector's or Fixer's findings.

The Master remains responsible for the book and final acceptance.

3.2 DETECTOR AGENT — Independent Quality Assurance and Red Team

The Detector is an independent critical reviewer.

Its purpose is to discover weaknesses, inconsistencies, technical errors, and unmet requirements.

It must inspect:

Language quality
Hebrew spelling.
Grammar.
Natural wording.
Punctuation.
Clarity.
Repetition.
Consistency of tone.
Correct gender and number agreement.
Proper Hebrew and English mixing.
Editorial quality
Chapter structure.
Information accuracy.
Logical flow.
Missing explanations.
Redundant content.
Unclear recommendations.
Reader usefulness.
Humor that interferes with meaning.
Poor transitions between chapters.
LaTeX quality
Compilation errors.
Missing packages.
Undefined commands.
Broken references.
Incorrect table of contents entries.
Overfull and underfull boxes.
RTL direction errors.
Reversed punctuation.
Unexpected font substitutions.
Broken equations.
Tables extending beyond margins.
Image scaling problems.
Captions appearing in wrong locations.
Excessive blank space.
Orphan headings.
Layout inconsistencies.
Incorrect total page count.
Visual quality
Color consistency.
Typography.
Readability.
Contrast.
Balanced page composition.
Image resolution.
Callout box appearance.
Background placement.
Consistency of graphics.
Diagram readability.
Proper figure numbering.
Compliance
All required sections exist.
The graph is actually generated by Python.
The original illustration has available source code.
The eight-block diagram contains exactly eight blocks.
The bibliography exists and is valid.
The README contains authentic PDF screenshots.
The PRD exists.
Prompt history is documented.
Agent collaboration is evidenced.
The final PDF contains at most 20 pages.

The Detector must produce structured issue reports.

Each issue must contain:

Issue ID.
Severity: CRITICAL, MAJOR, MINOR, or SUGGESTION.
Relevant file.
Relevant page or section.
Exact problem.
Evidence.
Proposed correction.
Current status.

The Detector must never report imaginary problems just to appear useful.

The Detector must not silently rewrite the book.

It should primarily detect and report problems, independently recheck fixes, and confirm whether issues are resolved.

3.3 FIXER AGENT — Source Verification and Corrective Engineering

The Fixer has TWO connected responsibilities.

Responsibility A — Source verification

Act as an independent fact-checking and bibliography specialist.

Verify the credibility of all factual claims concerning:

Dog behavior.
Urban canine stress and environmental stimulation.
Dog welfare.
Socialization.
Heat exposure.
Hydration.
Safe walking practices.
Dangerous objects or food encountered outdoors.
Emergency response principles.
Public-space etiquette.
Any legal or municipal rule included in the book.

Prefer trustworthy veterinary, animal welfare, academic, governmental, and professional sources.

Where appropriate, investigate sources such as recognized veterinary associations, reputable animal welfare organizations, government animal welfare services, and peer-reviewed research.

Never assume a source is reliable simply because its name appears in a draft.

Never fabricate publications, authors, dates, quotations, URLs, statistics, or DOI identifiers.

For every important claim, maintain a traceable mapping between the claim and the supporting source.

If a claim cannot be verified, flag it and either recommend removal or a clearly labeled qualification.

Responsibility B — Technical and editorial correction

Fix problems reported by the Detector and approved by the Master.

Examples:

Repair broken LaTeX.
Correct bibliography entries.
Fix inaccurate claims.
Improve problematic phrasing.
Repair graphics.
Correct incorrect formulas.
Improve accessibility.
Fix RTL layout problems.
Adjust page layout to comply with the 20-page limit.
Repair broken build scripts.

Every correction must be documented.

After completing a correction, send a message to the Detector requesting independent reinspection.

Never mark an issue as verified simply because you changed its code.

The Detector must verify the outcome.

3.4 Strict separation of responsibilities

The Master creates and coordinates.

The Detector identifies and validates problems.

The Fixer verifies sources and implements approved corrections.

The three roles must not become three fictional personalities simulated inside a single answer.

PART 4 — CLAUDE CODE SKILLS SETUP

Create or validate three genuine Claude Code project Skills using the documented project-level format:

text
.claude/skills/book-master/SKILL.md
.claude/skills/book-detector/SKILL.md
.claude/skills/book-fixer/SKILL.md


Each file must contain valid YAML frontmatter and detailed Markdown instructions.

Each Skill should use:

A unique name.
An accurate description.
Clear role boundaries.
Responsibilities.
Input expectations.
Output expectations.
Standard operating procedures.
Allowed files and editing boundaries.
Quality requirements.
Communication responsibilities.
Completion criteria.

Use valid Claude Code Skill conventions.

Do not assume that merely writing a SKILL.md file automatically creates a running independent agent.

A Skill is a reusable instruction set. A live Claude Code session or teammate is needed to execute it.

Required Skill behavior

book-master

Must coordinate the complete project, delegate verification and QA, create the book, and approve final deliverables.

book-detector

Must execute detailed independent document inspections and generate actionable issue reports without claiming ownership of the final product.

book-fixer

Must audit sources, repair approved defects, document changes, and request independent retesting.

Skill verification

After creation:

Confirm that all three SKILL.md files exist.
Confirm that their YAML frontmatter is valid.
Confirm that their names do not conflict with existing commands.
Confirm that Claude Code can discover the Skills.
Verify invocation using the supported command syntax.
Preserve the actual role instructions in the repository.

The expected invocations are:

text
/book-master
/book-detector
/book-fixer


If a Skill is not recognized, diagnose the actual discovery problem rather than claiming successful registration.

PART 5 — REAL COMMUNICATION BETWEEN AGENTS

This is a critical graded requirement.

The three agents must genuinely communicate.

The system must use real Claude Code agent communication capabilities, not simulated dialogue.

5.1 Preferred execution approach

Prefer three independent local interactive Claude Code sessions:

Session named master
Session named detector
Session named fixer

Use ListAgents and SendMessage when these features are available.

Use /list-agents to verify session discovery.

Do not present a text file containing imaginary conversations as proof of communication.

Do not claim that a message was delivered unless the messaging tool confirms it.

Do not fabricate replies from sessions that are not running.

If separate sessions have not been started, prepare their Skills and exact launch instructions, but report that the live communication requirement is still pending.

Do not hide this limitation.

5.2 Initial communication test

Before beginning collaborative production:

Identify the running sessions.
Confirm the Master can see the Detector.
Confirm the Master can see the Fixer.
Ask the Master to send a PING to Detector.
Ask the Master to send a PING to Fixer.
Require each recipient to respond with PONG and its own session name.
Ask the Detector to send a direct message to Fixer.
Ask the Fixer to acknowledge that message.
Record the observed results.

If the environment supports it, perform a complete pairwise communication check between all three agents.

For three agents, a complete directed network has six links.

Verify each link independently.

If the network is not fully available, record exactly which links work and which do not.

Do not mark failed or untested links as successful.

5.3 Communication protocol

All meaningful inter-agent communication should use a structured format containing:

text
MESSAGE_ID:
TIMESTAMP:
SENDER:
RECIPIENT:
TASK_ID:
MESSAGE_TYPE:
SUBJECT:
FILE_REFERENCES:
REQUEST:
EXPECTED_OUTPUT:
STATUS:


Message types may include:

TASK_ASSIGNMENT
RESEARCH_REQUEST
SOURCE_AUDIT
QA_REQUEST
ISSUE_REPORT
FIX_REQUEST
FIX_COMPLETED
RETEST_REQUEST
QA_APPROVED
STATUS_UPDATE
BLOCKER
FINAL_ACCEPTANCE

Send concise messages containing references to actual project files.

Avoid transmitting unnecessarily large file contents.

Use the shared repository as the source of truth.

5.4 Required real collaboration workflow

At least the following complete cycle must happen:

Master creates a draft.
Master requests a Detector review.
Detector reviews the actual files.
Detector sends a genuine defect report.
Master assigns the necessary corrections to Fixer.
Fixer performs the actual fixes.
Fixer reports the changed files.
Master requests a new Detector inspection.
Detector independently verifies the corrected files.
Detector approves or rejects the result.
Master records the final status.

Repeat the cycle if significant problems remain.

The process should demonstrate authentic iterative engineering, not artificial compliance.

5.5 Communication evidence

Maintain docs/AGENT_COMMUNICATION.md.

Record real communication milestones, task IDs, message timestamps when available, file references, and outcomes.

Where supported, preserve relevant transcript excerpts or terminal screenshots.

Distinguish clearly between:

Actual inter-session tool messages.
Human prompts.
Files used to coordinate work.
Planned but unexecuted communication.

Never invent evidence.

PART 6 — VIBE CODING DEVELOPMENT METHODOLOGY

The development process must demonstrate Vibe Coding.

This means using natural-language instructions to guide an AI-assisted development process while continuously inspecting, testing, and refining the generated code and outputs.

The project should not consist of one massive unverified generation step.

Instead, use iterative development.

6.1 Required development approach

Follow these principles:

Describe requirements in natural language.
Let Claude propose and generate implementation code.
Run the resulting code.
Inspect the output.
Identify actual shortcomings.
Refine the instructions.
Apply revisions.
Rebuild.
Independently validate.
Document the evolution.

Every meaningful iteration must have a clear reason and outcome.

6.2 Prompt documentation

Create docs/PROMPT_HISTORY.md.

For each significant prompt, record:

Prompt number.
Date and time, if known.
Agent receiving the prompt.
Exact prompt text when available.
Purpose.
Relevant files.
Actual result.
Discovered problem.
Subsequent refinement.
Final status.

A typical entry:

text
Prompt ID: P-007
Agent: Master
Phase: Graphic design

Goal:
Improve the chapter-opening layout.

Prompt:
[The exact natural-language prompt used]

Result:
The chapter-opening design was updated.

Files:
book/preamble.tex

Verification:
The PDF was recompiled and inspected.

Follow-up:
Adjusted spacing after detecting a crowded heading.


This is a FORMAT EXAMPLE only.

Do not record it as a real historical event unless it actually occurred.

6.3 Preserve real development history

Do not reconstruct fictional historical prompts.

Do not falsely claim that an instruction was issued earlier.

If previous history is unavailable, document what is known and label earlier stages as unavailable.

From the current point onward, record actual prompts and genuine development decisions.

6.4 Version management

Maintain meaningful revisions of the PRD and development plan.

For example:

PRD v0.1 — initial definition.
PRD v0.2 — changes following agent review.
PRD v1.0 — approved production specification.

Use versions only when corresponding revisions truly exist.

Maintain a project change log.

When practical, create Git commits at significant verified milestones.

Do not push to a remote repository without permission.

PART 7 — PRODUCT REQUIREMENTS DOCUMENT (PRD)

Create a detailed and professional docs/PRD.md.

The PRD must be written before major production decisions are finalized.

It should include:

Product name.
Project overview.
Problem statement.
Product vision.
Target readers.
User needs.
Scope.
Out-of-scope items.
Functional requirements.
Non-functional requirements.
Content architecture.
Design principles.
LaTeX technical architecture.
Python graphics requirements.
Multi-agent architecture.
Responsibilities and permissions.
Agent communication protocol.
Source verification rules.
Quality assurance process.
Acceptance criteria.
Deliverables.
Risks.
Dependencies.
Assumptions.
Constraints.
Development milestones.
Traceability to assignment requirements.
7.1 Expert review of PRD

Before approving the PRD:

Master creates the initial PRD.
Detector reviews it critically.
Fixer reviews technical feasibility, source requirements, and operational risks.
Master evaluates all feedback.
Accepted and rejected suggestions are documented with reasons.
The revised PRD is reviewed again if substantial changes were introduced.

Document the actual discussion.

The PRD must remain aligned with the book and repository.

PART 8 — BOOK CONTENT AND EDITORIAL DIRECTION
8.1 Overall concept

Create a humorous, practical, visually engaging guide for people raising dogs in urban environments.

The book should feel like a charming modern illustrated handbook, not a dry academic essay.

It should combine:

Everyday situations.
Useful advice.
Evidence-based explanations.
Urban-life humor.
Practical tips.
Short examples.
Attractive visual organization.
Realistic situations familiar to dog owners.

The reader should enjoy the text and finish each chapter with useful knowledge.

Writing tone

Use:

Natural modern Hebrew.
Warm, intelligent humor.
Short and medium-length paragraphs.
Clear explanations.
Memorable examples.
Practical recommendations.
Conversational phrasing when appropriate.

Avoid:

Robotic writing.
Excessively formal academic Hebrew.
Repetitive AI-style phrases.
Forced jokes.
Exaggerated claims.
Excessive slang.
Unverified scientific statements.
Unnecessarily long paragraphs.
Repeated introductory explanations.

Humor must never replace factual accuracy.

8.2 Target audience

The book is intended for:

First-time urban dog owners.
Apartment residents.
People living in busy cities.
Owners of small, medium, and large dogs.
People balancing work, social life, and dog care.
Readers who want a practical, entertaining introduction to city dog ownership.

Do not assume every dog has identical needs.

Recognize differences in age, health, temperament, environment, and individual behavior.

PART 9 — REQUIRED BOOK STRUCTURE

The book must contain the following four chapters.

CHAPTER 1
הפסיכולוגיה של הכלב העירוני

Suggested subtitle:

"איך לשרוד מעלית עם שלושה כלבים וחתול"

Purpose:

Explain how an urban environment affects dogs and how owners can better understand canine behavior.

Required topics:

A dog's perspective on urban life.
Common environmental stimulation: cars, horns, elevators, strangers, bicycles, and unfamiliar smells.
How sensory overload may affect some dogs.
Recognizing signs of comfort and discomfort.
Body language and canine communication.
The difference between excitement, fear, stress, and curiosity.
Positive reinforcement and predictable routines.
Elevator etiquette.
Encounters with other dogs.
Respecting personal space.
Practical ways to make everyday city experiences easier.

Include a short humorous scenario about an elevator encounter involving several dogs and a cat.

Make the example entertaining while maintaining practical, safe recommendations.

Include at least one designed callout box summarizing useful behavioral tips.

Do not make unsupported behavioral generalizations.

CHAPTER 2
מיפוי שטח — הגיאוגרפיה של גינות כלבים ופינות הצל הנכונות

Purpose:

Help urban dog owners think strategically about walking routes and their neighborhood environment.

Required topics:

Choosing suitable walking routes.
Dog parks versus ordinary public spaces.
Factors to consider when evaluating dog parks.
Availability of shade.
Water access.
Ground temperature and hot surfaces.
Traffic and road safety.
Choosing quieter routes.
Planning walking routes based on weather and conditions.
Respect for local regulations and other public-space users.

Do not invent actual municipal regulations, locations, or facility availability.

If using a named city or municipality, verify relevant claims first.

A conceptual city map or illustrated neighborhood planning diagram is acceptable.

Include a meaningful table comparing different urban walking environments.

Suggested table columns:

סוג אזור
יתרונות
אתגרים
מתי כדאי לבחור בו

Examples of rows:

פארק עירוני
רחוב שקט
גינת כלבים
טיילת
אזור מסחרי

Use clear, concise Hebrew inside the table.

CHAPTER 3
לוגיסטיקה ואופרציות — איך לארגן את התיק לטיול של חמש דקות שנגמר בשעה

Purpose:

Teach the practical organization and planning behind daily dog ownership in a large city.

Required topics:

Preparing for a walk.
Essential items to carry.
Water and appropriate containers.
Waste bags.
A suitable leash and identification.
Weather-related preparation.
Time planning.
Managing unexpected delays.
Organizing daily routines.
Planning around work and personal commitments.
Keeping basic supplies accessible.
Creating a reusable preparation checklist.

This chapter must contain a mathematical formula.

Suggested formula:

T_daily = Σ t_i

Where:

T_daily represents the total daily walking time.
t_i represents the duration of walk i.

Explain the formula in Hebrew.

Provide one clearly hypothetical numerical example.

Make clear that the mathematical example is illustrative and not a universal veterinary recommendation.

The mathematical notation must display left to right, while the explanatory Hebrew remains correctly right to left.

Mandatory Python graph

Create a meaningful graph illustrating an aspect of urban dog ownership.

A suitable example is:

חלוקת זמן הטיולים לאורך יום עירוני לדוגמה

Use an explicitly illustrative fictional daily schedule, such as:

Morning walk: 20 minutes.
Midday walk: 15 minutes.
Evening walk: 35 minutes.
Night walk: 10 minutes.

These are example data only, not evidence-based prescriptions.

The graph must be generated using actual Python code, preferably with Matplotlib.

Requirements:

Reproducible from the included Python script.
Professionally styled.
Readable at the printed book size.
Appropriate color palette.
Clear axis labels.
Accurate values.
Hebrew-compatible labels where technically practical.
A Hebrew caption in LaTeX.
An explicit note that values are illustrative if using fictional data.

Prefer vector output such as PDF where supported.

Keep the original Python source code.

The Detector must verify that the graphic really originates from Python and that the chart values match the source data.

CHAPTER 4
מדריך הישרדות — שאלות נפוצות ותקלות נפוצות

Purpose:

Create a practical FAQ and troubleshooting chapter about common unexpected situations in urban dog ownership.

Required situations:

The dog picked up or swallowed something from the street.
The dog refuses to enter an elevator.
The dog becomes nervous near traffic.
The dog reacts strongly to unfamiliar dogs.
The weather becomes unusually hot.
The walking schedule is disrupted.
The dog becomes overwhelmed in a busy environment.
The owner forgets a necessary walking item.

Use clear FAQ formatting.

Separate ordinary practical situations from possible emergencies.

For medical or poisoning concerns:

Avoid making remote diagnoses.
Avoid invented first-aid instructions.
Do not recommend inducing vomiting.
Do not prescribe medication.
Clearly recommend contacting a veterinarian promptly when ingestion of a potentially harmful substance is suspected.
Explain urgent warning signs only when they can be supported by reliable veterinary sources.
Never present uncertain information as established fact.

Include a clearly distinguishable emergency-information box.

Mandatory eight-block diagram

This chapter must include a flowchart with exactly eight meaningful blocks.

Suggested subject:

מה עושים כשהכלב מרים משהו חשוד מהרצפה?

The diagram should present an educational response workflow without attempting to replace veterinary advice.

The eight blocks should form a logical decision-support process.

Proposed concepts:

Detect the event.
Move the dog away from further exposure if safe.
Determine what was encountered, if possible.
Consider whether ingestion may have occurred.
Check for immediate warning signs.
Contact a veterinarian for guidance when ingestion or danger is possible.
Follow professional instructions.
Document the event and improve prevention.

Adapt branching and arrow directions to create a valid and readable process.

Use TikZ or another code-based graphical method.

Mandatory technical requirements:

Exactly eight primary labeled blocks.
Every block visible.
Every label readable.
Logical connecting arrows.
Clear start and end.
No unexplained disconnected blocks.
No text overflowing outside shapes.
RTL-compatible Hebrew labels.
Consistent geometry, spacing, and colors.
Source code included in the repository.

The diagram must not contain misleading advice that encourages delaying urgent veterinary care.

PART 10 — COVER, ABSTRACT, CONTENTS, AND BIBLIOGRAPHY
10.1 Cover design

Create a premium, modern, visually memorable cover.

The cover must contain:

Main Hebrew title.
Subtitle.
Original graphic or illustration.
Attractive composition.
Harmonious colors.
Group or author information when supplied.
Appropriate whitespace.

Suggested visual direction:

An elegant illustrated cityscape with a dog, buildings, walking paths, trees, and subtle playful elements.

Prefer original code-generated vector graphics.

The cover should resemble a polished commercial illustrated guide.

Avoid a default academic report appearance.

Do not invent author names or group identifiers.

Use explicit placeholders for missing details.

10.2 Abstract

Create a Hebrew abstract summarizing:

The book's purpose.
The challenges of urban dog ownership.
The four main themes.
The practical benefits for readers.
The book's approachable educational style.

Target approximately 150–220 Hebrew words, adjusted for the final layout.

The abstract should be useful and not repetitive.

10.3 Table of contents

Generate the table of contents automatically from LaTeX sectioning commands.

Requirements:

Proper Hebrew heading.
Correct chapter titles.
Correct page numbers.
RTL-compatible layout.
Consistent typography.
No missing or duplicated entries.

Recompile as needed to resolve references and page numbers.

Do not manually type a fake table of contents.

10.4 Bibliography

Create a properly formatted bibliography.

Use real, verifiable sources relevant to the actual statements in the book.

Preferred sources include:

Veterinary professional associations.
Reputable animal welfare organizations.
Government or municipal public guidance.
Peer-reviewed research when relevant.
Official safety recommendations.

Use BibLaTeX/Biber or another stable citation solution compatible with the selected LaTeX engine and Hebrew typesetting.

Requirements:

Every cited work must exist.
Every URL must be authentic.
Every bibliographic item must be relevant.
Source metadata must be accurate.
Do not fabricate publication details.
Cite important factual claims appropriately.
Ensure the bibliography compiles and displays correctly.

Additionally, provide a short methodology or production note explaining the use of Claude Code, Python, LaTeX, TikZ, and AI-assisted workflows.

A tool-use statement is not a substitute for a bibliography of factual sources.

PART 11 — PROFESSIONAL LATEX ENGINEERING
11.1 Compilation strategy

Use XeLaTeX or LuaLaTeX, selecting whichever offers reliable Hebrew and RTL support in the available environment.

Inspect installed tools first.

Use an appropriate Unicode-aware Hebrew typesetting solution, such as polyglossia with a compatible LaTeX engine.

Do not use a fragile configuration that reverses Hebrew punctuation or breaks math.

Check which Hebrew fonts are actually installed.

Possible fonts include:

Noto Sans Hebrew.
Noto Serif Hebrew.
David.
Arial.

Use only available fonts, and provide sensible fallbacks.

Do not assume a font exists.

Avoid mixing font packages that conflict with XeLaTeX or LuaLaTeX.

11.2 Right-to-left support

The entire reading experience must be correctly RTL.

Verify:

Paragraph direction.
Chapter headings.
Section headings.
Table cells.
Captions.
Page numbers.
Running headers.
Bullet and numbered lists.
Bibliography.
URLs.
English technical terms.
Mathematical formulas.
TikZ diagrams.

Avoid reversed parentheses and punctuation.

For mathematical notation, maintain proper mathematical left-to-right ordering.

Do not solve RTL issues by rasterizing all Hebrew text into images.

11.3 Document architecture

Use main.tex as the master entry point.

Separate visual configuration and reusable commands into preamble.tex.

Keep the chapters in separate files.

Use \input or an equivalent LaTeX mechanism to assemble the book.

Do not place the entire book in one giant source file.

Avoid unnecessary package complexity.

Write reusable commands for repeated graphic elements and callout boxes.

Maintain clear, understandable source code.

11.4 Layout quality

Use consistent margins and type sizes.

Apply carefully chosen spacing between paragraphs and sections.

Avoid excessively wide text columns.

Avoid crowded pages.

Avoid orphan headings and awkward page breaks.

Make chapter openings visually distinct.

Keep graphics and captions together when possible.

Keep tables within page boundaries.

Use professional page numbering and headers.

The final document should look intentional and professionally art-directed.

PART 12 — VISUAL DESIGN SYSTEM

Use a consistent editorial design language.

Suggested aesthetic:

Modern urban lifestyle guide with subtle playful dog-related illustrations.

Suggested color palette:

Deep navy: #183153
Warm cream: #FFF8ED
Sage green: #87A98C
Warm coral: #E98B73
Muted gold: #D8B56A
Soft charcoal: #333333

These colors are creative recommendations, not rigid restrictions.

Adjust the palette if the PDF requires better contrast or visual balance.

12.1 Design principles

The book should feel:

Elegant.
Warm.
Modern.
Friendly.
Playful without appearing childish.
Readable.
Consistent.
Professionally finished.
12.2 Required visual elements

Use several of the following:

Designed chapter-opening pages.
Subtle colored backgrounds.
Section accent bars.
Rounded informational boxes.
Highlighted quotations.
Tip boxes.
Checklists.
Compact icons.
Small thematic illustrations.
Elegant tables.
Clear graph styling.
Consistent figure captions.

Avoid placing decorative elements everywhere.

Maintain sufficient whitespace.

Every visual must either improve readability, communicate information, or support the book's theme.

12.3 Reusable callout boxes

Create reusable LaTeX styles for:

טיפ חשוב
כדאי לדעת
טעות נפוצה
שימו לב
טיפ מהשטח

Use tcolorbox or an equivalent robust implementation.

Ensure these styles work correctly with Hebrew text and page breaks.

12.4 Original object-based illustration

Produce at least one attractive original illustration built from graphical primitives.

Acceptable tools include:

TikZ drawing objects.
Python Pillow drawing shapes.
Matplotlib artists.
Programmatic SVG generation.

An example is a small dog or a dog walking through a city created from circles, paths, curves, polygons, and other reusable objects.

Keep the editable source code.

Do not substitute a randomly downloaded image.

Do not present an AI image as if it were drawn programmatically.

The implementation should visibly demonstrate code-based graphical construction.

PART 13 — PYTHON REQUIREMENTS

Use Python for at least one meaningful graph.

Prefer Matplotlib.

Recommended dependencies may include:

text
matplotlib
numpy
Pillow
PyMuPDF


Install only what is required.

Check the environment before suggesting package installation.

Do not overwrite system-wide configurations unnecessarily.

13.1 Python graph requirements

The graph source must:

Be readable.
Contain clear variable names.
Use explicit input data.
Produce the same graphic when rerun.
Save output to the expected project path.
Include comments.
Avoid unexplained hardcoded values.
Be version-controlled.
Match the graphic used in the final PDF.
13.2 Original illustration script

If Python is used for the illustration:

Draw with actual graphical objects.
Use deterministic dimensions.
Save a high-resolution output.
Prefer transparency where appropriate.
Make the result suitable for PDF placement.
Document how to regenerate it.
13.3 Reproducibility

Create a build script capable of:

Generating Python graphics.
Compiling the LaTeX project.
Running bibliography processing if required.
Resolving cross-references.
Copying the final PDF to output/.
Performing basic output checks.

When applicable, support Windows PowerShell users.

Document prerequisites and exact commands.

PART 14 — SOURCES, FACT CHECKING, AND SAFETY

This book contains practical animal-care information.

Accuracy is essential.

The Fixer must audit factual information before the content is approved.

14.1 Source quality rules

Prioritize sources that are:

Identifiable.
Credible.
Relevant.
Verifiable.
Scientifically or professionally grounded when appropriate.

Prefer original guidance and primary sources over anonymous websites.

Avoid relying on unsupported blogs for medical or behavioral recommendations.

14.2 Claim verification

Create a source audit table with:

Claim ID.
Chapter.
Statement.
Source.
URL or reference.
Verification status.
Notes.
Required correction.

Use the following statuses:

VERIFIED
PARTIALLY VERIFIED
UNSUPPORTED
NEEDS CLARIFICATION
REMOVED

Do not label a source VERIFIED without actually checking it.

14.3 Medical safety

The book must not pretend to replace a veterinarian.

Use appropriately cautious language.

Avoid universal recommendations about walking duration, nutrition, health, and behavioral treatment.

When discussing emergencies, provide general informational guidance supported by reputable sources and direct the reader to appropriate veterinary care.

14.4 Data integrity

If using illustrative data:

Label it explicitly.
Never disguise it as research.
Never invent statistics and cite them to unrelated sources.
Ensure graphs accurately reflect their declared datasets.
PART 15 — README REQUIREMENTS

Create a visually polished and informative README.md in the repository root.

The README must allow a lecturer or evaluator to understand the project without opening every file.

It must include:

Project name.
Brief description.
Book cover preview.
Explanation of the educational project.
Overview of the four chapters.
Highlights of the final book.
Actual screenshots from the compiled PDF.
Python-generated graph preview.
Eight-block diagram preview.
Explanation of the three agents.
An architecture diagram of the workflow.
Explanation of the Vibe Coding process.
Tools and technologies used.
Repository structure.
Instructions for installing dependencies.
Instructions for compiling the PDF.
Quality assurance overview.
Links to the PRD and process documentation.
A link to the final PDF.
Information about contributors when provided.
15.1 PDF screenshots

Screenshots must come from the actual final PDF.

Use a genuine PDF-rendering process, such as PyMuPDF or an equivalent installed tool.

Create previews of:

Cover.
Representative chapter page.
Page containing the Python graph.
Page containing the eight-block diagram.

Save the screenshots under assets/readme/.

Embed them in the README using working relative Markdown paths.

Do not create unrelated mockup images and label them as final PDF screenshots.

Do not reuse screenshots from an outdated PDF after the book changes.

15.2 Presentation quality

The README should feel like documentation of a polished technical and creative project.

Use meaningful headings, embedded images, concise explanations, and useful relative links.

Avoid exaggerated marketing language.

PART 16 — QUALITY ASSURANCE AND RED TEAM

Implement a structured quality assurance process.

The Detector must inspect both the source files and the rendered PDF.

Do not rely only on whether the LaTeX compiler returns success.

A technically valid PDF can still contain unacceptable layout problems.

16.1 Required inspection categories

The Detector must evaluate:

A. Requirement completeness.

B. Hebrew writing quality.

C. Correct RTL rendering.

D. Citation and bibliography quality.

E. Technical LaTeX validity.

F. Visual consistency.

G. Graphic readability.

H. Table correctness.

I. Formula correctness.

J. Eight-block diagram correctness.

K. Page count.

L. README accuracy.

M. PRD consistency.

N. Prompt history authenticity.

O. Evidence of multi-agent communication.

P. Repository reproducibility.

16.2 PDF visual inspection

Render all pages of the PDF into image previews using an available local tool.

Inspect every page for:

Clipped text.
Incorrect line directions.
Overlapping elements.
Poor spacing.
Unreadable graphics.
Cut-off tables.
Broken borders.
Excessive whitespace.
Incorrect page breaks.
Empty pages.
Broken references.
Visual inconsistencies.

Provide page-specific defect reports.

Use automated layout checks where possible, but do not equate automated success with visual quality.

16.3 Fixing protocol

The Fixer must work from a specific issue ID.

For every fix:

Read the original issue.
Inspect the relevant source.
Determine the cause.
Propose a correction.
Apply the correction.
Rebuild if needed.
Record the changed files.
Report the correction to Master.
Request Detector retesting.
Wait for independent confirmation.

Do not close the issue without verification.

16.4 Iterative review cycles

Perform an initial review after the first complete book draft.

Perform another review after integrating fixes.

Continue targeted correction cycles while important issues remain.

The final release must have:

Zero known unresolved CRITICAL issues.
Zero known unresolved MAJOR issues.
A reproducible PDF build.
A passing requirements audit.
Source verification completed for material factual claims.
An actual page count at or below 20.

Document remaining minor limitations honestly.

PART 17 — PAGE COUNT MANAGEMENT

The maximum page count is strict.

Count the actual physical pages of the compiled PDF.

The cover, abstract, table of contents, chapters, and bibliography all count toward the 20-page limit.

Create a balanced page budget.

Suggested initial budget:

text
Cover:                    1 page
Abstract:                 1 page
Table of contents:        1 page
Introduction:             1 page
Chapter 1:                3 pages
Chapter 2:                3 pages
Chapter 3:                3 pages
Chapter 4:                3 pages
Bibliography/credits:     1–2 pages
--------------------------------
Target:                  17–18 pages
Maximum:                 20 pages


This is an initial layout target, not a guaranteed page count.

Adjust after actual compilation.

Do not exceed 20 pages.

If the document is too long:

Remove repetition.
Shorten unnecessary explanations.
Improve layout efficiency.
Resize graphics carefully.
Optimize whitespace.
Adjust section breaks.
Simplify redundant callouts.

Do not make the font unreasonably small.

Do not sacrifice readability merely to satisfy the page limit.

PART 18 — VALIDATION AUTOMATION

Create scripts/validate_project.py.

It should check as many requirements as can be reliably verified programmatically.

The script should verify:

The final PDF exists.
The PDF can be opened.
The page count is between 1 and 20.
The expected chapter source files exist.
The main LaTeX file exists.
The PRD exists.
The README exists.
The three Skill files exist.
Python graph source exists.
Generated graph exists.
Original illustration source exists.
Eight-block diagram source exists.
The bibliography file exists.
Prompt history documentation exists.
Agent communication documentation exists.
Required screenshots exist.
The final PDF contains expected chapter titles, where reliable text extraction is possible.
All required dependencies and build instructions are documented.

Do not claim that a simple file-existence check proves semantic correctness.

For requirements that require manual or visual verification, print:

MANUAL REVIEW REQUIRED

Create a machine-readable or Markdown summary of validation results.

The final checklist must clearly distinguish:

PASS
FAIL
MANUAL REVIEW REQUIRED
NOT VERIFIED
PART 19 — GITHUB AND SUBMISSION REQUIREMENTS

The project must be organized as a clean Git repository suitable for academic submission.

19.1 Git repository

If Git is not initialized, prepare the repository and request approval for operations that affect existing configuration.

Do not erase an existing Git history.

Create a sensible .gitignore.

Exclude disposable build products where appropriate.

Preserve all source files necessary for reproduction.

Include the final PDF intentionally, despite excluding unnecessary temporary output files.

19.2 Repository quality

The repository should contain:

Logical file organization.
Descriptive filenames.
Human-readable documentation.
No unnecessary duplicates.
No broken relative links.
No passwords or API tokens.
No unrelated personal files.
No fake screenshots.
No fabricated communication logs.
19.3 Submission documents

The assignment requires a separate report PDF prepared according to the instructor's dedicated report template.

If the report template is available in the project, inspect it and complete it accurately.

If the template is missing, document the missing dependency and do not invent the template's contents.

The report PDF must not be confused with the book PDF.

If the instructor requires a filename based on an eight-character group code, use the actual group code provided by the students.

Do not invent the group code.

The report must be exported to PDF rather than submitted as a Word file when the instructor requires PDF-only submission.

The book itself must remain a separate final PDF in output/final_book.pdf.

19.4 Final repository access

Prepare the project for GitHub submission.

Do not publish or push the repository without the user's approval.

Document the exact steps required for GitHub upload if automatic publishing is not authorized.

Do not claim that a GitHub submission occurred unless it actually occurred.

PART 20 — REQUIRED PROJECT DOCUMENTATION

In addition to the README and PRD, produce the following useful documents.

docs/PROJECT_PLAN.md

Include:

Development phases.
Task dependencies.
Milestones.
Assigned agents.
Acceptance criteria.
Actual status.
docs/ARCHITECTURE.md

Explain:

Source structure.
LaTeX assembly process.
Python figure generation.
Build dependencies.
Agent system.
Quality assurance workflow.

Include an architecture diagram where useful.

docs/AGENT_COMMUNICATION.md

Document genuine inter-agent communication, including task handoffs and actual message outcomes.

docs/PROMPT_HISTORY.md

Document actual significant natural-language prompts used during development and subsequent improvements.

docs/PROCESS_LOG.md

Maintain a chronological summary of implementation activities and results.

docs/SOURCE_AUDIT.md

Record claims, sources, verification results, and corrections.

docs/QA_REPORT.md

Record QA rounds, findings, and final verification results.

docs/ISSUE_TRACKER.md

Maintain issue IDs, severity, ownership, status, and resolution.

docs/REQUIREMENTS_MATRIX.md

Map every assignment requirement to:

Relevant file.
Relevant PDF page if applicable.
Verification method.
Verification result.
Supporting evidence.
docs/SELF_ASSESSMENT.md

Provide a transparent project self-assessment.

Describe strengths, weaknesses, and known limitations.

Do not fabricate a lecturer's grade.

docs/FINAL_CHECKLIST.md

Summarize final acceptance results and pending issues.

PART 21 — DEVELOPMENT PHASES AND ORDER OF EXECUTION

Execute the work in the following order.

PHASE 0 — Initial inspection

Inspect the current environment.

Determine:

Current working directory.
Existing folders and files.
Existing Git state.
Claude Code capabilities.
Installed Python version.
Available LaTeX engines.
Available packages.
Available fonts.
Existing instructions and Skills.
Existing assignment attachments.

Produce a short factual environment report.

Do not pretend that unavailable software is installed.

PHASE 1 — Requirements analysis

Translate the assignment into an explicit requirements matrix.

Identify mandatory and optional requirements.

Preserve the instructor's exact requirements where provided.

Identify missing metadata such as author names and group code.

Use clearly marked placeholders for missing administrative details without blocking technical development.

PHASE 2 — Agent configuration

Create and validate the three Skills.

Prepare role instructions.

Verify that each agent has a distinct scope.

Check actual inter-session communication availability.

If the Detector and Fixer sessions are not running, provide the exact commands and instructions needed for the students to open them.

Do not simulate their responses.

PHASE 3 — PRD development

Create the initial PRD.

Ask the other agents for actual review when available.

Record their real feedback.

Revise the PRD.

Approve the implementation plan.

PHASE 4 — LaTeX prototype

Create a small working Hebrew LaTeX document.

Test:

Unicode.
Hebrew RTL.
Fonts.
Section headings.
Tables.
Formulas.
Captions.
Colored boxes.
TikZ graphics.

Compile the prototype.

Fix technical issues before generating the entire book.

PHASE 5 — Book content development

Write the cover, abstract, introduction, and four chapters.

Maintain a consistent style.

Separate chapters into their designated files.

Use real source citations.

Avoid unverified claims.

PHASE 6 — Graphics production

Create:

Python graph.
Original code-generated illustration.
Eight-block TikZ flowchart.
Professional table.
Mathematical formula.
Relevant callout boxes.

Compile and visually inspect each component.

PHASE 7 — First complete PDF

Assemble the document.

Generate the complete PDF.

Verify its page count.

Inspect all pages.

Correct obvious production defects.

PHASE 8 — Independent source audit

Ask Fixer to review factual claims and bibliography.

Resolve unsupported or inaccurate information.

Record verification results.

PHASE 9 — Red Team review

Ask Detector to perform a complete review.

Require a detailed issue report.

Classify issues by severity.

PHASE 10 — Correction cycle

Assign approved fixes to Fixer.

Recompile.

Ask Detector to independently retest.

Repeat as necessary.

PHASE 11 — Documentation and README

Create actual screenshots from the approved PDF.

Finish:

README.
PRD.
Architecture documentation.
Prompt history.
Communication log.
Source audit.
QA reports.
Requirements matrix.
Submission documentation.
PHASE 12 — Final verification

Run all available automated checks.

Perform visual validation.

Verify every mandatory requirement.

Ensure the final PDF does not exceed 20 pages.

Ensure all source files needed to reproduce the PDF are present.

PHASE 13 — Delivery preparation

Prepare the final repository.

Provide a final summary containing:

Final PDF path.
Page count.
Chapter list.
Graphics created.
Skills created.
Agents actually used.
Communication evidence.
QA results.
Documentation status.
Remaining blockers.
Exact steps required for submission.
PART 22 — IMPORTANT FAILURE AND RECOVERY RULES

Never conceal failures.

If compilation fails:

Read the actual error.
Identify its cause.
Fix the relevant source.
Recompile.
Verify the result.

If fonts are missing:

Inspect available fonts.
Select an appropriate installed alternative.
Document the change.
Recompile and inspect Hebrew rendering.

If Python packages are missing:

Identify the missing dependency.
Check whether installation is allowed.
Use an appropriate environment.
Document installation requirements.
Avoid unnecessary system modifications.

If an agent cannot be reached:

Verify the session exists.
Check /list-agents.
Check whether messaging is supported.
Check inbound message settings.
Verify the sessions run in compatible environments.
Report the real blocker.
Request only the necessary human action.

Do not substitute imaginary agent conversations.

If internet access is unavailable:

Use only sources that can be genuinely verified from available materials.
Mark unverified references clearly.
Avoid inventing citations.
Keep source verification pending where necessary.

If the final PDF exceeds 20 pages:

Revise content and layout.
Recompile.
Recount.
Repeat until compliant.

If the PDF looks unattractive:

Improve the actual layout.
Do not simply claim that the design is professional.
PART 23 — FINAL ACCEPTANCE GATES

The project is complete only if all mandatory gates are satisfied.

GATE A — Book
Hebrew book compiled successfully.
Maximum 20 actual pages.
Four chapters.
Cover.
Abstract.
Table of contents.
Bibliography.
GATE B — Mandatory visual elements
Real Python-generated graph.
At least one table.
At least one formula.
At least one original illustration.
At least one object-based graphical illustration.
Exactly eight blocks in the required process diagram.
Attractive colors, backgrounds, and callouts.
GATE C — Technical project
Separate LaTeX chapter files.
Reproducible build.
Working graphic-generation scripts.
Documented dependencies.
Clean repository structure.
GATE D — Multi-agent collaboration
Master Skill exists and is functional.
Detector Skill exists and is functional.
Fixer Skill exists and is functional.
Three distinct agents have actually run.
Actual communication occurred.
Actual QA findings were created.
Actual corrections were performed.
Independent retesting occurred.
Evidence is preserved.

If the three live agents were not actually activated, this gate FAILS even if their Skill files exist.

GATE E — Documentation
PRD completed.
README completed.
Authentic final-PDF screenshots embedded.
Prompt history documented.
Agent communication documented.
Source audit completed.
QA reports completed.
Requirements matrix completed.
Final checklist completed.
GATE F — Submission readiness
Final book PDF available.
LaTeX source project complete.
Git repository prepared.
Separate assignment report handled according to the actual template requirements.
No mandatory requirement knowingly missing.
No unsupported claims of successful completion.

Do not declare the project finished while a mandatory gate remains failed or unverified.

PART 24 — AUTONOMY, ACCOUNTABILITY, AND QUALITY EXPECTATIONS

You are expected to act as a capable technical project manager and book-production lead.

Make reasonable creative decisions independently.

Do not ask for approval for every minor formatting choice.

Do not repeatedly ask for information already available in the repository or conversation.

Prefer actual working implementations to speculative descriptions.

Prioritize:

Assignment compliance.
Authentic multi-agent execution.
Correct Hebrew typesetting.
Technical reproducibility.
Factual accuracy.
Beautiful visual design.
Useful, engaging content.
Professional documentation.

Use critical judgment.

Do not accept inferior or obviously broken outputs simply because they compile.

Avoid unnecessary complexity.

Maintain compatibility with the users' Windows development environment where possible.

Never execute destructive, external publishing, payment, or credential-related actions without the required permission.

PART 25 — IMMEDIATE ACTIONS

BEGIN EXECUTION NOW.

Your first actions must be:

ACTION 1

Inspect the current project directory and identify the existing master, detector, and fixer folders.

ACTION 2

Read existing project instructions, Skills, and configuration files.

ACTION 3

Create a concise requirements matrix covering every mandatory deliverable listed above.

ACTION 4

Prepare and validate the three Claude Code Skills without destroying any existing work.

ACTION 5

Determine whether three independent Claude Code sessions are currently running and accessible.

If they are running, attempt real session discovery and messaging.

If they are not, provide exact instructions for starting the missing sessions and activating the correct Skills.

The students may need to launch additional interactive Claude Code terminals themselves. Do not pretend that writing Skill files launches those terminals.

ACTION 6

Create the initial PRD, project plan, and LaTeX technical prototype.

ACTION 7

As soon as real communication is available, ask Detector and Fixer to review the PRD and relevant requirements.

ACTION 8

Proceed through the full development lifecycle while maintaining genuine process documentation.

ACTION 9

Compile, inspect, and improve the final book until all technically achievable requirements pass.

ACTION 10

Prepare the final submission package and explain any genuinely unresolved dependency.

Final instruction

DO NOT STOP AT PLANNING.

Write actual project files, execute actual code, produce an actual Hebrew LaTeX book, generate the required graphics, test the output, and prepare the repository for submission.

However, do not fabricate collaboration, sources, tests, screenshots, or successful execution.

If a real agent session, human permission, software dependency, or instructor document is missing, clearly identify the specific blocker and provide the smallest necessary next action.

The final objective is a complete, visually impressive, accurate, professionally produced Hebrew illustrated book, supported by a genuine three-agent Claude Code workflow and a fully documented Vibe Coding development process.

START WITH PROJECT INSPECTION AND AGENT CONFIGURATION.
```

## 4. Purpose
Define the whole project: Hebrew book 'המדריך הלא-רשמי לחיים עם כלב בעיר הגדולה' (<=20 pages), repository structure, three agents with Skills, real communication, PRD, chapter contents, LaTeX/RTL rules, Python figures, sources, README, QA, validation, Git, documentation, phases and gates (Parts 1-25).

## 5. Actual result
MASTER phases 0-7: git repository, 3 Skills, role cards, CLAUDE.md, PRD v0.1, LaTeX preamble (commit cc384df 21:10:27), then the first complete 13-page draft with figures, build/validation/RTL scripts, docs and README (commit b1cec22 21:32:29, pushed 21:32:39). `ListAgents` found no detector/fixer session, so no agent work happened in this turn.

## 6. Files affected
See `git show --stat cc384df` (11 files) and `git show --stat b1cec22` (48 files): .claude/skills/*, CLAUDE.md, */ROLE.md, docs/*, book/**, figures/**, scripts/*, README.md, assets/readme/*, output/final_book.pdf.

## 7. Follow-up corrections
- docs/PROMPT_HISTORY.md (P-001) and docs/PROCESS_LOG.md give ~20:53 for the start; the transcript timestamp of this prompt is 21:04:58 local. Gate D (agent communication) stayed blocked until Prompt_08.

---
Generated by `scripts/export_prompts.py` from the Claude Code transcripts; fields 4-7 from the project records named in the script header. Do not edit by hand; re-run the script.

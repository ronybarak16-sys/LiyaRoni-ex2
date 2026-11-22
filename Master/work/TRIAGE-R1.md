# MASTER triage of DETECTOR round R1 (`Detector/reports/QA-R1.md`) — 2026-11-20

Input: DETECTOR message DET-T005-R1-001 (0 CRITICAL, 2 MAJOR, 12 MINOR, 12 SUGGESTION).
Hard constraints for every fix: book stays **exactly 20 pages**, 0 overfull boxes,
`audit_rtl_full.py` 0 reversed / 0 bad lines, `check_rtl.py` all PASS, `validate_project.py` 0 FAIL.

| ID | Sev. | Decision | Note for FIXER |
|---|---|---|---|
| DET-1-01 | MAJOR | APPROVED | letter→colon kern must not make `ה:`/`ח:` read as `ת` in any font (Gisha, David Bold); keep David Regular free of a visible gap. Students' items 1, 3. |
| DET-1-02 | MAJOR | APPROVED | `'` must not read as yod (א'/ב', פיג'מה, צ'יוואווה). Robust, maintainable method; mind bibliography names like O'Neill. Students' items 7, 8. |
| DET-1-03 | MINOR | APPROVED | colon after `"`, `'`, digits, `}` |
| DET-1-04 | MINOR | APPROVED | `פרק~N` and `~` before `\ref`/`\cite`. Students' item 9. |
| DET-1-05 | MINOR | APPROVED | TOC leader spacing. Students' item 2. |
| DET-1-06 | MINOR | APPROVED | `\emph` → bold/colour; drop `\itshape` (fixes DET-1-26 too) |
| DET-1-07 | MINOR | APPROVED | badge 4 / label "לא, בוודאות" in diagram |
| DET-1-08 | MINOR | APPROVED | ragged cells where gaps are large; verify visually |
| DET-1-09 | MINOR | APPROVED | emergency-card label alignment |
| DET-1-10 | MINOR | APPROVED | "ראשון–רביעי" no wrap |
| DET-1-11 | MINOR | APPROVED | build loops until no "Rerun" warning; validator fails on it |
| DET-1-12 | MINOR | APPROVED | `@legislation` → supported type, with the URL FIXER verified in the source audit |
| DET-1-13 | MINOR | APPROVED | name "ערכת הכפילות" in ch.3 (the duplicate-kit tip) |
| DET-1-14 | MINOR | APPROVED | חצייה |
| DET-1-15 | SUG | APPROVED | הגאוגרפיה (consistent with גאומטריות) |
| DET-1-16 | SUG | APPROVED | second "לא מתוחה" → "רפויה" |
| DET-1-17 | SUG | APPROVED | introduce א' and ב' as the two adults |
| DET-1-18 | SUG | APPROVED | heading → "ארבע קומות של מתח" (3→7) |
| DET-1-19 | SUG | APPROVED (modified) | "ועשר" → "ו-10"; do NOT put Hebrew inside math — drop "min" from the display equation and state "כלומר 80 דקות" in the text |
| DET-1-20 | SUG | APPROVED | p.20 sentences end in Hebrew |
| DET-1-21 | SUG | APPROVED | `urldate=iso`; undated web sources: year only if verified, else "n.d." |
| DET-1-22 | info | NO ACTION | known; the project audits by word positions, not copy-paste |
| DET-1-23 | SUG | APPROVED if 20 pages hold | callout title tab spacing |
| DET-1-24 | SUG | APPROVED | "ו-\en{Fixer}" |
| DET-1-25 | SUG | APPROVED | glossary in alphabetical order |
| DET-1-26 | SUG | covered by DET-1-06 | |

Students' items NOT REPRODUCED by DETECTOR (4 map label, 5 טבלה 2.2/[6], 6 n/i, 10 Source Audit, 11 איור 3.1):
no change — verified correct on the rendered page; explained to the students.

## Source-audit decisions (FIXER report M-f-001, `Fixer/reports/SOURCE-AUDIT-R1.md`)
| Claim | Decision |
|---|---|
| avma-warm | REPLACE everywhere by `humane-heat` (+ `rkc-pavements` for pavement temperature); AVMA page unreadable → not cited unverified |
| C-02 | APPROVED: add `aspcapro-body` |
| C-03 | APPROVED: "מסתייג" → "מתנגד" |
| C-04 | APPROVED wording (review + survey) |
| C-05, C-07 | APPROVED wording with `rkc-pavements`, `humane-heat` |
| C-06 | APPROVED: `hall2020exertional` for the exercise trigger |
| C-09 | APPROVED wording (local authority may set off-leash areas, §law) |
| C-11, C-12 | APPROVED: cite `humane-heat`; heatstroke signs attributed to animal-welfare organisations, not AVMA |
| C-14 | APPROVED: replace `aspca-apcc` by `aspca-poisoned` (keeps entry count) |
| C-15 | APPROVED: add `banfield-poison` (safety-critical sentence stays) |
| C-16 | APPROVED both rewordings (ch.4 + glossary) |
| C-20 | APPROVED wording + `rspca-separation` |
| C-23 | APPROVED: add `rspca-fireworks` |
| C-24 | APPROVED wording + `avsab-puppy` |
| C-10, C-17, C-22 | no change (optional cites skipped for page budget) |
Page budget: the book must stay 20 pages; if the larger bibliography overflows p.19, reduce the
bibliography font to `\footnotesize` rather than cutting content.

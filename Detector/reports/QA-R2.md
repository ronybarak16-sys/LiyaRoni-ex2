# QA-R2 — DETECTOR retest of R1 fixes (task T-007, RETEST_REQUEST M-m-011)

- Date: 2026-11-22
- PDF: `output/final_book.pdf` (rebuilt 2026-11-22 21:56), **20 pages** (PyMuPDF `page_count`)
- I verified each issue myself. FIXER's descriptions were not taken as evidence.
- Tools:
  - Re-rendered all 20 pages to `Detector/reports/pages_R2/` (110 dpi) and looked at every page.
  - 250–400 dpi crops in `Detector/reports/R2_evidence/`.
  - Read word and character x-positions with PyMuPDF `words`/`rawdict`.
  - Saved a `pdftotext` dump of each page as `R2_evidence/text_pNN.txt`.
  - Ran a scripted scan of every page for lines that begin or end inside a citation or reference.
  - Grepped `build/main.log` and the source files.
  - Re-ran `audit_rtl_full.py`: 2643/2643 bigrams in correct order, 0 reversed.
  - Re-ran `check_rtl.py`: 25/25 PASS.
- Log state:
  - `Rerun to get` / `Please rerun`: 0
  - Overfull boxes: 0
  - Missing characters: 0
  - `Font shape ... undefined`: 0
  - biblatex "No driver": 0
  - Remaining warnings: biblatex "Language 'hebrew' not supported" (expected), 2× "`h` float specifier changed to `ht`", and 127× `\endL or \endR problem` (see DET-1-26).

## Retest results

| ID | Sev. | Result | Evidence |
|---|---|---|---|
| DET-1-01 | MAJOR | **VERIFIED** | The colon is now clear of ה/ח/ת in every font. Gisha: cover `מגישות:` / `קוד קבוצה:` (`R2_evidence/p01_cover_credits.png`), heading `מעלית:` (`p06_elevator_heading.png`), card labels `שבב:`, `חיים:`, `ואלרגיות:` (`p16_card.png`), diagram node `היה:` (`p15_diagram.png`). David Bold: legend `מהשטח:`, `נפוצה:` (`p04_legend_list.png`), `הדרגתית:` (`p07_emph_colon.png`). David Regular is unchanged and correct. None of the colons reads as ת. In David Bold the colon keeps a small gap, which is legible and acceptable. |
| DET-1-02 | MAJOR | **VERIFIED** | The geresh is now upright and clearly not a yod: table 3.1 `א':`/`ב':` (`p12_table31.png`), `(א' ו-ב')` (`p12_intro_AB.png`), `תוכנית ב'` (`p12_bullets.png`, `p14_planB.png`). `פיג'מה` (p.4), `צ'יוואווה` (p.6), the glossary on p.17, the headings on pp.17–18 and the TOC were checked in the page renders. A source scan finds no Hebrew letter followed by a bare ASCII `'` outside preamble comments. The text layer still has U+0027. |
| DET-1-03 | MINOR | **VERIFIED** | The colon now sits tight after these characters: `"שיטת הקשת":` (`p07_tip_quote_colon.png`), `"ערכת הכפילות":` (p.11), `"מקדם עיכוב":` (`p12_bullets.png`), `מפרק 3:` (`p14_planB.png`), `איור 1.1:` … `4.1:` (`p20_credits.png`), and `הדרגתית:`. |
| DET-1-04 | MINOR | **VERIFIED** | `(פרק 2).` on p.17 now moves to the next line as a whole (`p17_perek2.png`). A scripted scan of all 20 pages found no line that ends in `(פרק`/`איור`/`טבלה`/`ומקור`/`[` and no line that starts with `2).` or `]`. The only hit is the rotated y-axis label inside the graph image on p.12, which is not body text. |
| DET-1-05 | MINOR | **VERIFIED** | Every TOC entry now has a gap before its first leader dot (`p03_toc_dots.png`). I spot-checked the TOC page numbers against the headings (5, 6 ×3, 7 ×2, 9, 10, 12, 13, 15, 16) and they are correct. `חיזוק חיובי` moved to p.6 and the TOC shows 6. |
| DET-1-06 | MINOR | **VERIFIED** | Emphasis is now bold: `למה` (p.4); `שלנו`, `כל` (p.5); `לא`, `שלכם` (p.6); `הדרגתית:` (p.7); `מבעוד מועד` (p.15). The font-shape warnings are gone. The bibliography keeps real italics (p.19). |
| DET-1-07 | MINOR | **VERIFIED** | Badge 4 is now on the west vertex, and the 3→4 arrowhead is visible. `לא, בוודאות` is to the left of the arrow, clear of badge 5 and of the `הופיע סימן חריג` connector (`p15_diagram.png`). There are still exactly 8 blocks, and the advice is unchanged and safe. |
| DET-1-08 | MINOR | **VERIFIED** | Tables 2.1 and 2.2 and the three body-language boxes are now flush right with no stretched word gaps (`pages_R2/page_05.png`, `page_09.png`, `page_10.png`). |
| DET-1-09 | MINOR | **VERIFIED** | The emergency-card labels are flush right, and their colons line up (`p16_card.png`). |
| DET-1-10 | MINOR | **VERIFIED** | `ראשון–רביעי` now fits on one line (`p12_table31.png`). |
| DET-1-11 | MINOR | **VERIFIED** | `grep -c "Rerun to get\|Please rerun" build/main.log` returns 0. |
| DET-1-12 | MINOR | **VERIFIED** | Reference [12] prints with its source, URL and access date (`pages_R2/page_19.png`). The log has no "No driver" warning. |
| DET-1-13 | MINOR | **VERIFIED** | The term is defined in the ch.3 tip, `"ערכת הכפילות": קנו שני עותקים…` (p.11), and ch.4 refers back to it (p.14). |
| DET-1-14 | MINOR | **VERIFIED** | Pages 4 and 8 now read `מעבר חצייה` / `מעברי חצייה`. Grep finds no `חציה` left. |
| DET-1-15 | SUG | **VERIFIED** | The p.8 subtitle reads `הגאוגרפיה`. |
| DET-1-16 | SUG | **VERIFIED** | p.6 now reads `והרצועה רפויה ולא נכרכת`. |
| DET-1-17 | SUG | **VERIFIED** | p.12 now reads `שני אנשים עובדים (א' ו-ב')`, and the pair stays on one line. |
| DET-1-18 | SUG | **VERIFIED** | The heading reads `…וארבע קומות של מתח` on p.6, and the TOC matches. |
| DET-1-19 | SUG | **VERIFIED** | The text reads `ו-10 דקות`, the equation is `= 80` with no unit, and the next sentence says `כלומר 80 דקות`. The graph and formula values are unchanged and consistent. |
| DET-1-20 | SUG | **VERIFIED** | All 5 credit items and the "איך נבנה הספר" sentences now end in Hebrew (`p20_credits.png`, `pages_R2/page_20.png`). |
| DET-1-21 | SUG | **VERIFIED** | Access dates appear as `visited on 2026-11-20`, and undated pages show `N.d.` (p.19). |
| DET-1-22 | info | **CLOSED – no action** | MASTER's triage said NO ACTION. This was information only. |
| DET-1-23 | SUG | **VERIFIED** | Callout tabs now have clear space above the first line (pp. 2, 4, 5, 6, 7). The book is still 20 pages. |
| DET-1-24 | SUG | **VERIFIED** | Word x-positions on p.20 (y≈534): `ו` x=439, `-` between, `Fixer` x=411–435. This renders as `ו-Fixer` in the correct RTL order. |
| DET-1-25 | SUG | **VERIFIED** | The glossary is alphabetical, from ברכיצפלי to תוכנית ב' (`pages_R2/page_17.png`). |
| DET-1-26 | SUG | **VERIFIED – accepted as known** | FIXER's statement is correct. The remaining 127 `\endL or \endR problem` lines are bidi's generic itemize warning, and every list renders correctly. The specific trigger in R1 (`\emph` at introduction.tex:23) is gone. I accept this as a known, harmless log warning. |

## FIXER's notes — DETECTOR judgement
1. **`[3, 7]` reads right-to-left inside the brackets: not a defect.** On p.6, `rawdict` shows `[` at x=359, `5` at 362, `,` at 370.5, `4` at 373.6 and `]` at 379. A Hebrew reader therefore meets 4, then the comma, then 5, which is the natural RTL order (`R2_evidence/p06_cite45.png`). It is consistent across the whole book, and the brackets are balanced. No action.
2. **The C-24 item on p.10 is not a defect.** The second line of item 6 (`הווטרינר [6].`) starts under the item text, not under the `6.` label, so the hanging indent is there (`R2_evidence/p10_item6_wrap.png`). FIXER's concern does not reproduce.

## Reworded text (pp. 5–17): Hebrew, RTL and citations
I re-read every changed passage on pp. 5, 6, 7, 9, 10, 11, 14, 15, 16 and 17. The grammar and agreement are correct, for example `סקירת מחקר וסקר … מצאו`, `ארגוני רווחת בעלי חיים ממליצים/מונים`, and `ראש הרשות המקומית רשאי`. Each citation follows the word it supports, and the period comes after the bracket. The numbering runs in order of first appearance, [1] to [16], and every number has a bibliography entry. RTL order is confirmed by `audit_rtl_full.py` (0 reversed).

## Fresh regression scan (all 20 pages)
I found no new defects. Cover, TOC, headers and footers, the 4 chapter banners, the figures (1.1, 1.2, 2.1, 3.1, 4.1), the tables (2.1, 2.2, 3.1), the formula, the callouts, the fridge page, the 16-entry bibliography (it fits p.19 without overflow; the last line is at about 765 pt, inside the 774 pt text area) and the about page all render correctly. There is no clipping or overlap. The p.13 whitespace after "תיק חירום קטן" is unchanged from R1 and comes from the chapter 4 page break.
**New issues: none (no DET-2-nn).**

## Summary
| Severity | Open after R2 |
|---|---|
| CRITICAL | 0 |
| MAJOR | 0 (DET-1-01 and DET-1-02 VERIFIED) |
| MINOR | 0 (DET-1-03 to DET-1-14 VERIFIED) |
| SUGGESTION | 0 (DET-1-15 to 21 and 23 to 25 VERIFIED; DET-1-26 accepted as known; DET-1-22 closed with no action) |

I updated the status column of `docs/ISSUE_TRACKER.md` by adding a "DETECTOR round R1 issues" section with rows for DET-1-01 to DET-1-26. **Verdict: QA_APPROVED.**

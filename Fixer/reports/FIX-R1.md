# FIX-R1 — FIXER corrective engineering (task T-006, FIX_REQUEST M-m-010)

- Input: `Master/work/TRIAGE-R1.md` (MASTER decisions), `Detector/reports/QA-R1.md`, `Fixer/reports/SOURCE-AUDIT-R1.md`
- Dates: work 2026-11-20 to 2026-11-22. No git commit or push. No DET issue was marked VERIFIED; DETECTOR does that.
- Evidence: `Fixer/reports/FIX-R1_evidence/` contains:
  - `colons_geresh_400dpi.png`: 400-dpi crops of every colon and geresh case.
  - `colon_gaps.txt`: the measured gap between each colon and the glyph before it, with the font of each, for the whole PDF.
  - `page_3/12/15/16/17/19.png`: renders of the TOC, table 3.1, the diagram, the emergency card, the glossary and the sources page.

## Final verification (after the last change, in the requested order)
| Check | Result |
|---|---|
| `python scripts/build_book.py` | `pages=20`; `overfull hbox=0`; `'undefined' mentions=0` (was 2: the italic font-shape warnings are gone); `missing glyphs=0`; `rerun warnings=0` |
| `python scripts/audit_rtl_full.py` | 2643/2643 matched bigrams in correct order; reversed 0; mostly-reversed lines 0 |
| `python scripts/check_rtl.py` | 25/25 PASS. No probe was changed. |
| `python scripts/generate_readme_images.py` | run; screenshots are newer than the PDF |
| `python scripts/validate_project.py` | **FAIL: 0**. New row "Build log has no 'Rerun' warning" = PASS. 5 MANUAL REVIEW rows, same as before. |
| Visual review | Pages 1, 3–7, 9–17, 19 and 20 rendered at 85–110 dpi, plus 400-dpi crops of colons and geresh. Findings are per issue below. |

## Per issue

| ID | Root cause | Change | Files | Verification |
|---|---|---|---|---|
| DET-1-01 | The letter→colon kern `-0.14em` applied in every font. It is right only for David Regular; in David Bold and Gisha it pushed the colon into ה/ח, which then read as ת. | The kern now depends on the font. `\hc@colonkern{David-Regular}{David-Bold}{Gisha}` reads `\f@family`/`\f@series` when the colon is set. Letter→colon: −0.14em / 0 / +0.04em. | `book/preamble.tex` | `colon_gaps.txt`: Gisha ה/ח→colon gap +0.39 to +0.57 pt, David Bold 0.00 pt, David Regular −1.70 pt (unchanged). 400-dpi crops: `קבוצה:` and `מגישות:` on the cover, `טיפ מהשטח:` (Gisha Bold and David Bold), `ואלרגיות:` on the card and `היה:` in the diagram are all clearly separate. No ה:/ח: reads as ת. |
| DET-1-02 | ASCII `'` in David is a slanted stroke that looks like a yod. | New `\gr` macro: Gisha's upright glyph. The text layer keeps U+0027, and `'` is **not** made active, so math primes, TikZ and bibliography names such as O'Neill are unaffected. `\pdfstringdefDisableCommands` keeps bookmarks correct. Applied to: א\gr/ב\gr in table 3.1 and its intro, תוכנית ב\gr (ch. 3, ch. 4, glossary), פיג\gr מה, צ\gr יוואווה, and נספח א\gr/ב\gr (title and TOC). | preamble, ch1, ch3, ch4, introduction, appendix | Crops and page renders: `א':`, `ב':`, `פיג'מה`, `צ'יוואווה` all show an upright apostrophe, clearly not a yod. Text layer: `פיג'מה`, `נספח א'`. |
| DET-1-03 | David's colon has a wide side bearing, and the kern fired only after Hebrew letters. | (a) Digit→colon uses bidi's own digit class, so it does not break bidi's "3.1" handling. (b) After `"` and `\gr`, a `\futurelet` look-ahead tightens a following colon: −0.20em in David Regular, −0.14em in Bold. It does not consume spaces. A font switch resets XeTeX's inter-character state, which is why the look-ahead is needed. (c) `}:` cases: the colon moved inside the bold group (`\emph{הדרגתית:}`, `\textbf{איור~\ref{…}:}`). | preamble, ch1, acknowledgments | `colon_gaps.txt`: `3:` −1.70 pt; `":` −2.38 pt; `':` −2.2 pt; bold `":` −1.71 pt. The 330-dpi value test (−0.14/−0.22/−0.30em) showed that −0.30em collides in `א':`, so −0.20em was chosen. |
| DET-1-04 | Breakable space in `(פרק 2)` and before citations/refs. | Ties: `פרק~N`, `איור~\ref`, and `~\cite` on every \cite and \ref in book/**. | all chapter, front and back files | p.17 `(פרק 2)` no longer breaks; nothing in the book wraps at a citation. |
| DET-1-05 | Leader dots started flush against the title. | `\hspace{0.8em}` before `\titlerule*` (chapter and section). | preamble | p.3 render: every entry has a visible gap before the first dot. |
| DET-1-06 (+26) | David and Gisha have no italic, so `\emph` and fieldbox `\itshape` were invisible. | `\emph` → bold. `fontupper=\itshape` removed. The English bibliography keeps real italics (`\AtBeginBibliography{\renewcommand*\mkbibemph…}`). | preamble | `שלנו`, `לא`, `שלכם`, `הדרגתית:`, `מבעוד מועד` render bold. The log no longer has "Font shape … undefined". **DET-1-26 is NOT fully resolved:** its `\endL or \endR` warning is the generic itemize/bidi warning that every list item produces. There are 127 such warnings, the same count as a build of HEAD that I made for comparison, and the rendering is correct. I left this as is. |
| DET-1-07 | Badge 4 sat on the diamond's top vertex, over the arrowhead from block 3. The label crowded badge 5. | Badge 4 moved to the west vertex. The `לא, בוודאות` label moved to the left side of the arrow. | `figures/tikz/eight_block_diagram.tex` | p.15 render: the 3→4 arrowhead is visible, and the label is clear of badge 5 and of the `הופיע סימן חריג` connector. validate_project still finds 8 blocks (PASS). |
| DET-1-08 | Narrow justified cells left large word gaps. | Tables 2.1 and 2.2 use `>{\raggedright\arraybackslash}X` (under bidi this is ragged on the left, flush right). The three body-language boxes use `before upper=\raggedright`. | ch2, ch1 | p.5, 9, 10 renders: the cells are flush right and the large gaps are gone. |
| DET-1-09 | `\raggedleft` under bidi = flush **left**. | Card label column → `\raggedright`. | ch4 | p.16 render: the labels are flush right and the colons line up at the right edge. |
| DET-1-10 | `ראשון–רביעי` wrapped. | `\mbox{ראשון–רביעי}`, column 1.9 → 2.05cm. At 2.0cm there was a 1.2 pt overfull box. | ch3 | p.12: one line; overfull 0. |
| DET-1-11 | **Root cause found:** `"` became active only in `\AtBeginDocument`, which runs *after* main.aux is read. Labels whose caption contains `"` (fig. 1.1 "מעלית לקומה 7") were read with catcode 12 and re-checked at the end with the active catcode, so they "changed" on every run. That is why HEAD still had the warning after 3 passes. | (a) `"` is activated in the `begindocument/before` hook, before the aux is read. (b) build_book.py loops xelatex until there is no `Rerun to get`/`Please rerun` message (max 5 passes, otherwise FAIL) and prints `rerun warnings=`. (c) validate_project.py FAILs if the log has a rerun warning. | preamble, `scripts/build_book.py`, `scripts/validate_project.py` | The build now settles in 1 pass after biber; `grep -c "Rerun to get" build/main.log` = 0; the validator row is PASS. |
| DET-1-12 | `@legislation` has no biblatex driver. | `@misc` with title, note, howpublished and the verified gov.il/Nevo URL. | references.bib | The biblatex "No driver" warning is gone; [12] shows the URL and access date. |
| DET-1-13 | The term "ערכת הכפילות" did not exist in ch. 3. | The ch. 3 tip now starts `"ערכת הכפילות": קנו שני עותקים…`. | ch3 | p.11 render. |
| DET-1-14 | Spelling. | `מעבר חצייה`, `מעברי חצייה`. | introduction, ch2 | grep: no `חציה` left. |
| DET-1-15 | Spelling consistency. | `הגאוגרפיה`. | ch2 | p.8 subtitle. |
| DET-1-16 | The phrase was repeated. | The second `לא מתוחה` → `רפויה`. | ch1 | p.6. |
| DET-1-17 | א'/ב' were not introduced. | `…שני אנשים עובדים (א\gr{}~ו-ב\gr) וכלב בוגר ובריא`. A tie keeps the pair together. | ch3 | p.12. |
| DET-1-18 | Floors 3→7 is four floors, not six. | The heading now reads `…חתול אחד וארבע קומות של מתח`. The TOC follows. | ch1 | p.3 TOC, p.6. |
| DET-1-19 (modified) | Mixed number styles, and an English unit at the end of a sentence. | `ו-10 דקות`. The display equation is `T_daily = 20 + 15 + 35 + 10 = 80`, with no Hebrew in math, and the text continues `כלומר 80 דקות, …`. | ch3 | p.11. The validator's string `20 + 15 + 35 + 10 = 80` is still present (PASS). |
| DET-1-20 | Sentences ended with an English word. | The 5 credit items and both "איך נבנה הספר" sentences now end in Hebrew (`…בקוד TikZ במיוחד לספר.`, `…Python מצורות גאומטריות.`, `…TikZ בתוך מסמך הספר.`, `הספר נכתב ונבנה בעזרת Claude Code כפרויקט Vibe Coding, כלומר פיתוח בהנחיה בשפה טבעית.`). | acknowledgments | p.20. |
| DET-1-21 | US date format; undated sources showed no date. | biblatex `date=iso,urldate=iso` (`seconds=true` is required by biblatex for urldate=iso; no time is printed). The `date` bibmacro prints "n.d." when there is no year. Only verified dates are given: aspca-poisoned 2019-03-20, avsab2021 2021, avsab-puppy 2008, and the articles. | preamble, references.bib | p.19: `visited on 2026-11-20`, `N.d.` on undated pages. No "Conflicting options" warning. |
| DET-1-22 | Information only. | No action (per triage). | — | — |
| DET-1-23 | The title tab was cramped. | callout `top=5pt` → `8pt`. | preamble | Still 20 pages, and every page starts at the same content as before (checked page by page). |
| DET-1-24 | Hebrew prefix joined directly to a Latin word. | `ו-\en{Fixer}`. | acknowledgments | p.20. |
| DET-1-25 | Glossary was not alphabetical. | Sorted: ברכיצפלי, חיזוק חיובי, מכת חום, מרחק נוח, עומס חושי, קסיליטול, ריחרוח, שבב אלקטרוני, שער כפול, תוכנית ב'. | appendix | p.17. |

## Source-audit decisions applied (from the TRIAGE table)
- `avma-warm` is removed everywhere: 2 uses in ch2 (text and seasons table), 2 in ch3 and 1 in ch4. The replacements are `humane-heat`, plus `rkc-pavements` for pavement temperature. `aspca-apcc` is replaced by `aspca-poisoned`. Both old entries are deleted from references.bib.
- Added, using the BibTeX verified in SOURCE-AUDIT-R1 Part 3: `aspcapro-body`, `hall2020exertional`, `banfield-poison`, `rspca-separation`, `rspca-fireworks`, `rkc-pavements`, `humane-heat`, `aspca-poisoned`.
- Rewordings applied: C-02 (cite), C-03 (`מתנגד לשימוש בשיטות ענישה`), C-04, C-05, C-06, C-07, C-09, C-11, C-12, C-14, C-15, C-16 (ch. 4 and glossary), C-20 (text and knowbox cite), C-23 and C-24.
- The bibliography now has 16 entries and fits on p.19 at the existing `\small` size, so `\footnotesize` was not needed.
- `docs/SOURCE_AUDIT.md` is updated: 18 VERIFIED, 4 PARTIALLY VERIFIED (C-09, C-17, C-20, C-22), 1 REMOVED (C-16), 1 N/A.

## Notes for DETECTOR / MASTER
- Multi-citations such as `[3, 7]` display right-to-left inside the brackets. This is the existing behaviour (already true of `[4, 5]` in HEAD) and was not part of R1.
- p.10, nimusei-gina item 6: the longer approved C-24 sentence wraps to a second line, and that line starts at the label position because the existing `leftmargin=*` gives no hanging indent. It is legible; I did not change the list layout because it was outside the request.
- Bash note: one helper script briefly wrote `~\1{` instead of `~\cite{`/`~\ref{`. A second script repaired it, choosing `\ref` for `fig:/tab:/eq:` keys and `\cite` for all others. A grep confirms no `\1{` remains, and the build has 0 undefined references or citations.

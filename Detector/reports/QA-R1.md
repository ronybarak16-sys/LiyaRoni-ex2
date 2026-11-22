# QA-R1 — DETECTOR independent review (task T-005)

- Date: 2026-11-20
- PDF: `output/final_book.pdf` (build 2026-11-20 12:59), **20 pages** (PyMuPDF `page_count` = 20; `build/main.log`: "Output written ... (20 pages)")
- Tools: `scripts/generate_readme_images.py --all --dpi 110` → `Detector/reports/pages_R1/page_NN.png` (all 20 pages looked at);
  PyMuPDF zoom crops (200–500 dpi) → `Detector/reports/R1_evidence/*.png`; PyMuPDF `get_text("words")` / `rawdict` (x positions; for RTL
  the earlier word must have the larger x); `pdftotext -enc UTF-8` per page → `R1_evidence/text_pNN.txt`; `scripts/audit_rtl_full.py`
  (2614/2614 bigrams in correct order, 0 reversed); `scripts/check_rtl.py` (25/25 PASS); `scripts/validate_project.py` (FAIL 0);
  grep of `build/main.log`; reading of all `book/**/*.tex`, `book/preamble.tex`, `figures/python/create_graph.py`.
- Side effect to note: running `validate_project.py` rewrote the timestamp line of `docs/VALIDATION_RESULTS.md` (1-line diff, no content change). Nothing else outside `Detector/reports/` was touched.

---

## 1. Students' list

| # | Students' item | Verdict | Evidence / explanation |
|---|---|---|---|
| 1 | p.1 cover `liyaroni-ex2 קוד קבוצת` | **REAL-VISUAL** | Text layer is correct: `קוד קבוצה‪: liyaroni-ex2` and `מגישות‪: ליה פורת...` (`R1_evidence/text_p01.txt`); visual order is also correct. But the colon is pulled *into* the preceding letter: `קבוצה:` renders like `קבוצת` and `מגישות:` shows no visible colon (`R1_evidence/p01_cover_credits.png`). Root cause = DET-1-01 (negative kern `-0.14em` letter→colon, `book/preamble.tex:70`, collides in Gisha / David Bold). |
| 2 | p.3 TOC: detached numbers, `\|`, lone dot after "מעלית..." | **REAL-VISUAL (partial)** | No `\|` characters, no detached page-number lines, every entry and its number are on one line (`pages_R1/page_03.png`); the line-merging/`\|` come from text extraction. Real part: the dot leader starts flush against some titles, so the first leader dot reads as a sentence period — `העירונית.`, `להגיד.`, `של מתח.`, `הציבורי.`, `אישי.` (`R1_evidence/p03_toc_dots.png`). → DET-1-05. |
| 3 | pp.4,6,11,12,17 `טיפ מהשטת`; p.6 colon in heading `מעלית:` | **REAL-VISUAL** | Text layer: `טיפ מהשטח‪:` and `מעלית‪:` are correct. Visually the colon fuses with ח so it reads `מהשטת` (`R1_evidence/p04_legend_list.png`, `p04_tipbox_label.png`, `p06_tip_quote_colon.png`), and in the p.6 heading the colon overlaps ת (`p06_elevator_heading.png`). Same in other sans-bold headings: `שפת הגוף:` (`p05_heading_colon.png`), `לבד בבית:` (`p07_heading_colon.png`), diagram node 3 `היה:` reads `הית` (`p15_diagram.png`), emergency card `שבב:`, `חיים:`, `ואלרגיות:` (`p16_card_colons.png`). → DET-1-01 (MAJOR). |
| 4 | p.8 map: "כביש ראשי סואן" duplicated / clipped | **NOT REPRODUCED** | The label appears once in the text layer (one occurrence, 2 words at y=331) and once in the image. It sits fully inside the figure with margin above it (`R1_evidence/p08_map_label.png`). |
| 5 | p.10 `בלה 2.2:`; `בכל יציאה []6` | **NOT REPRODUCED** | Caption is `טבלה 2.2:` in both the text layer (`text_p10.txt`) and the image (`pages_R1/page_10.png`). Word positions: `[6]` x=207 is left of `יציאה` x=220, so it comes at the end of the sentence in RTL. Rendered `בכל יציאה [6]` is correct. `[]6` comes from the text layer splitting brackets and digits. |
| 6 | p.11 `n` after "האות", `i` after "שמספרו" missing | **NOT REPRODUCED** | rawdict: CMMI10 `n` at x=208.3, between `האות` (x≈217) and `מציינת` (x≤199). CMMI10 `i` at x=342.2, between `שמספרו` (x≥348) and `,` (x=339). `t_i` at x=484–488. All are present and in the right order (`pages_R1/page_11.png`). The `:i` "word" that PyMuPDF reports is a word-grouping artefact. |
| 7 | p.12 table 3.1 `אי:`/`בי:`; Fri/Sat rows | **REAL-VISUAL** | The text layer has ASCII `'` (`א':`). In David the `'` glyph is a slanted stroke that looks almost the same as yod, so `א'` reads as `אי` (`R1_evidence/p12_geresh_vs_yod.png`, 500 dpi, next to the `י` of `טיול`). The colon after `'` also stands detached (`א׳ :`, DET-1-03). The Friday/Saturday rows are fine. The only layout flaw is that `ראשון–רביעי` wraps onto 2 lines in the first column (`p12_table31.png`, DET-1-10). → DET-1-02. |
| 8 | p.14 `"תוכנית בי"` | **REAL-VISUAL** | Same David `'` glyph as in item 7 (`R1_evidence/p14_planB.png`). It also shows `מפרק 3 :` with a detached colon (DET-1-03). The same applies on p.12 bullet `תוכנית ב' לצהריים` (`p12_bullets.png`). → DET-1-02. |
| 9 | p.17 `(פרק .(2`; "ריחרוח" split | **REAL** (first part) / **NOT REPRODUCED** (second) | The line breaks inside the parenthesis: `...למכת חום (פרק` ⏎ `2).` (`R1_evidence/p17_perek2_break.png`; `appendix.tex:19-20` has an ordinary breakable space). → DET-1-04. The "ריחרוח" entry is one continuous paragraph that wraps normally (`pages_R1/page_17.png`). The "split" is pdftotext merging entries. |
| 10 | p.19 `(Source Audit` missing `)` | **NOT REPRODUCED** (visual) | Both parentheses are drawn: `במסמך ביקורת המקורות (Source Audit) שבמאגר הפרויקט.` (`pages_R1/page_19.png`). rawdict shows XeTeX stores *mirrored* paren characters in the text layer (`(` at x=349 left of `Source`, `)` at x=412 right of `Audit`), so copy-paste/OCR of the text layer yields odd parentheses. This is an accessibility-only artefact (DET-1-22). |
| 11 | p.20 `3.1: גרף...` missing `איור`; TikZ/Python sentence order | **NOT REPRODUCED** | Text layer `• איור ‪ :3.1‬גרף שנוצר בקוד ‪ Python‬מנתוני המחשה.` and image (`R1_evidence/p20_credits.png`): `איור 3.1` is present, the period is at the sentence end (far left), and word order is correct (`audit_rtl_full.py` 0 reversed). Related real points: the colon after `3.1` / `1.1` is detached (`איור 1.1 :`, DET-1-03), and several credit items end with an English word against the CLAUDE.md typography rule (DET-1-20). |

**Summary of students' list:** REAL 1 (item 9a) · REAL-VISUAL 5 (items 1, 2-partial, 3, 7, 8) · NOT REPRODUCED 6 (4, 5, 6, 9b, 10, 11).
MASTER's hypothesis is **confirmed for `'` and for `ח:`/`ה:`/`ת:`**. Precise cause of the colon problem: the inter-character kern `\XeTeXinterchartoks \hebletterclass \colonclass = {\kern-0.14em}` (`book/preamble.tex:70`) was tuned for David *Regular*, where it looks fine (`R1_evidence/p02_body_colon.png`). It is applied to **every** font, and in David Bold and Gisha/Gisha Bold it pushes the colon into the letter. The `"` → `יי` hypothesis is **not** reproduced: `"` is already drawn upright with Gisha (`preamble.tex:73-74`) and reads correctly on every page checked.

---

## 2. Detector findings

### DET-1-01
- Severity: MAJOR
- File: `book/preamble.tex` (line 70)            - Page/Section: 1 (cover credits), 4 (legend list + tip box label), 5/6/7/14 (sans-bold section headings with colon), 6/9/11/12/17 (all "טיפ מהשטח:" box labels), 15 (diagram node 3 `היה:`, node 5 `דבר:`), 16 (emergency card labels)
- Problem: Letter→colon kern `-0.14em` is applied in all fonts. In Gisha (sf, used for headings, box titles, the cover, TikZ nodes) and David Bold, the colon collides with the preceding letter. `ה:` reads as `ת`, `ח:` reads as `ת`, and `ב:`/`ם:` swallow the colon. Readers and OCR see `קבוצת`, `מהשטת`, `הית`, and missing colons.
- Evidence: `R1_evidence/p01_cover_credits.png`, `p04_legend_list.png`, `p04_tipbox_label.png`, `p05_heading_colon.png`, `p06_elevator_heading.png`, `p07_heading_colon.png`, `p15_diagram.png`, `p16_card_colons.png`. Regular David is fine: `p02_body_colon.png`, `p20_group_code.png`. Text layer is correct everywhere.
- Proposed correction: Make the kern font-dependent. Either (a) apply it only in the upright-medium serif family, e.g. `\XeTeXinterchartoks\hebletterclass\colonclass={\ifx\f@family\rmdefault\ifx\f@series\mddefault\kern-0.14em\fi\fi}` (inside `\makeatletter`), or (b) set the kern to `0` for sf/bold, possibly with a small positive kern (`+0.05em`) for Gisha. Re-render pp.1, 4, 6, 15, 16 at 300 dpi to confirm the colon is clear of ה/ח/ת.
- Status: OPEN

### DET-1-02
- Severity: MAJOR
- File: `book/preamble.tex` (quote handling, l.71-74); occurrences in `chapters/chapter03_logistics.tex` (table 3.1, `תוכנית ב'`), `chapters/chapter04_survival.tex:28`, `frontmatter/introduction.tex` (`פיג'מה`), `chapters/chapter01_psychology.tex` (`צ'יוואווה`)            - Page/Section: 4, 6, 12, 14
- Problem: In the David body font, ASCII `'` is a slanted stroke at yod height and looks like `י`. `א'`/`ב'` read as `אי`/`בי`, as in students' items 7 and 8. In Gisha (headings `נספח א'`, glossary term `תוכנית ב'`) it is upright and fine.
- Evidence: `R1_evidence/p12_geresh_vs_yod.png` (500 dpi, `א'` next to the `י` of `טיול`), `p12_table31.png`, `p12_bullets.png`, `p14_planB.png`.
- Proposed correction: Treat `'` the same way as `"`, so it is drawn with Gisha's upright glyph, without making `'` active globally (math primes and TikZ use it). Add `\newcommand{\gr}{{\hebrewfontsf\char39}}` and write `א\gr`, `ב\gr`, `תוכנית ב\gr`, `פיג\gr מה`, `צ\gr יוואווה`. Alternatively use U+05F3 (׳) from Gisha. The text layer stays ASCII `'`.
- Status: OPEN

### DET-1-03
- Severity: MINOR
- File: `book/preamble.tex:63-70`; occurrences in `chapter01_psychology.tex:107` (`\emph{הדרגתית}:`), ch.1 fieldbox (`"שיטת הקשת":`), `chapter02_city_mapping.tex` (`מכבדים "לא":`), `chapter03_logistics.tex` (`"מקדם עיכוב":`, `א':`, `ב':`), `chapter04_survival.tex:28` (`מפרק 3:`), `backmatter/acknowledgments.tex:27-31` (`\ref{...}}:`)            - Page/Section: 6, 7, 10, 12, 14, 20
- Problem: This is the reverse of DET-1-01. David's colon has a wide side bearing, and the compensating kern only fires after a Hebrew letter. After `"`, `'`, a digit, or a closing group `}`, the colon stands detached, as if `word :`.
- Evidence: `R1_evidence/p06_tip_quote_colon.png` (`"שיטת הקשת" :`), `p12_table31.png` (`א׳ :`), `p12_bullets.png` (`"מקדם עיכוב" :`), `p14_planB.png` (`מפרק 3 :`), `p20_credits.png` (`איור 1.1 :`, `איור 3.1 :`), `pages_R1/page_07.png` (`הדרגתית :`).
- Proposed correction: When fixing DET-1-01, add the other left-hand classes (digits 0-9, `"` (active → Gisha), `'`, `)`) to the kern rule for David Regular only. For `}:` cases, move the colon inside the group or use a bare `\kern-0.14em` macro (`\colon`-like `\hcolon`).
- Status: OPEN

### DET-1-04
- Severity: MINOR
- File: `book/backmatter/appendix.tex:19-20` (also every `פרק N` / `איור N` reference)            - Page/Section: 17 (glossary "ברכיצפלי")
- Problem: The line breaks between `(פרק` and `2).`, leaving `2).` alone on a line (students' item 9).
- Evidence: `R1_evidence/p17_perek2_break.png`; text layer `(פרק` / `.(2`.
- Proposed correction: Use a tie: `(פרק~2)`. Apply it globally to `פרק~N`, `איור~\ref`, `טבלה~\ref`, `ומקור~\cite`.
- Status: OPEN

### DET-1-05
- Severity: MINOR
- File: `book/preamble.tex:150-153` (`\titlecontents`)            - Page/Section: 3 (TOC)
- Problem: For some entries the first leader dot touches the title, so it reads as a trailing period (`העירונית.`, `להגיד.`, `של מתח.`, `הציבורי.`, `אישי.`). Other entries have a gap. This is the "lone dot" in students' item 2.
- Evidence: `R1_evidence/p03_toc_dots.png`, `pages_R1/page_03.png`.
- Proposed correction: Put a fixed gap before the leaders: `{\hspace{0.8em}\titlerule*[0.6pc]{.}\contentspage}` for both chapter and section.
- Status: OPEN

### DET-1-06
- Severity: MINOR
- File: `book/preamble.tex:207` (`fontupper=\itshape`), 7× `\emph{...}` (ch.1 l.14, 28, 74, 94, 107; ch.4 l.51; introduction l.23)            - Page/Section: 4, 5, 6, 7, 15 (+ all field boxes)
- Problem: David and Gisha have no italic. `build/main.log:2047,2093`: "Font shape `TU/David(1)/m/it' undefined ... using m/n". So every `\emph` (e.g. `הכלב *שלנו*`, `*לא* נגמר`, `*מבעוד מועד*`) has no visible emphasis, and `\itshape` in fieldbox does nothing.
- Evidence: log lines above; `pages_R1/page_05.png` (`הכלב שלנו` plain), `page_06.png` (`זה לא נגמר` plain).
- Proposed correction: `\renewcommand{\emph}[1]{\textbf{#1}}` (or a colour such as `\textcolor{coraldark}{#1}`). Remove `fontupper=\itshape` from fieldbox.
- Status: OPEN

### DET-1-07
- Severity: MINOR
- File: `figures/tikz/eight_block_diagram.tex`            - Page/Section: 15, figure 4.1
- Problem: (a) Number badge 4 sits on the top vertex of the diamond, exactly where the arrow from block 3 ends, so the arrowhead is hidden. (b) The edge label `לא, בוודאות` touches or overlaps badge 5 and crowds the vertical `הופיע סימן חריג` connector. The diagram does have exactly 8 blocks, the logic is sound, and the advice is safe (do not induce vomiting).
- Evidence: `R1_evidence/p15_diagram.png`.
- Proposed correction: Move badge 4 to the diamond's right or left vertex, or shorten the 3→4 arrow by `shorten >=` so the head is visible. Shift the `לא, בוודאות` label left (`left=4pt` / `pos=0.4`), clear of badge 5.
- Status: OPEN

### DET-1-08
- Severity: MINOR
- File: `book/chapters/chapter02_city_mapping.tex` (tables 2.1, 2.2), `chapter01_psychology.tex` (tcbraster boxes)            - Page/Section: 5, 9, 10
- Problem: Narrow justified `X` columns and boxes leave large word gaps: `רוכבי    אופניים,    פיקניקים`, `טיול ארוך בבוקר או   לפני`, `מסלולים    חלופיים    בשעות`, `יכולה   להיראות   כמו   קפיצות`.
- Evidence: `pages_R1/page_09.png`, `page_10.png`, `page_05.png`, `R1_evidence/p09_table21_justify.png`.
- Proposed correction: Make the cells ragged on the end (left) side. Under bidi RTL that is `>{\raggedright\arraybackslash}X` (verify by render, see DET-1-09). For the three body-language boxes add `halign=flush right` / `before upper=\raggedright`.
- Status: OPEN

### DET-1-09
- Severity: MINOR
- File: `book/chapters/chapter04_survival.tex` (emergency card, `>{\sffamily\bfseries\raggedleft}m{5.4cm}`)            - Page/Section: 16
- Problem: The card labels are flush **left** (all colons align at the left edge of the column), and their right edges are ragged. In RTL, labels should be flush right. Under bidi, `\raggedleft` gives end-side alignment.
- Evidence: `R1_evidence/p16_card_colons.png` (label right edges vary from x≈1120 to 1250 px; left edges constant).
- Proposed correction: Use `\raggedright` (or nothing) in that column spec, then re-render.
- Status: OPEN

### DET-1-10
- Severity: MINOR
- File: `book/chapters/chapter03_logistics.tex` (table 3.1 first column `m{1.9cm}`)            - Page/Section: 12
- Problem: `ראשון–רביעי` breaks after the en-dash onto two lines, making the first row taller and the day column uneven. This is the "rows layout" complaint in students' item 7.
- Evidence: `R1_evidence/p12_table31.png`.
- Proposed correction: Widen the column to about 2.3cm or write `\mbox{ראשון–רביעי}`.
- Status: OPEN

### DET-1-11
- Severity: MINOR
- File: `scripts/build_book.py:44-51`, `build/main.log:2801`            - Page/Section: build
- Problem: The final XeLaTeX pass still reports `LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.` The PDF can be shipped with unsettled references. TOC page numbers and figure refs were spot-checked and are currently correct.
- Evidence: `build/main.log` line 2801.
- Proposed correction: Loop xelatex (max 5) until the log no longer contains "Rerun to get", and have `validate_project.py` FAIL if it does.
- Status: OPEN

### DET-1-12
- Severity: MINOR
- File: `book/references.bib` (entry `il-doglaw2002`, type `@legislation`)            - Page/Section: 19, ref [8]
- Problem: `build/main.log:2727`: `Package biblatex Warning: No driver for 'legislation'`. The entry is printed through the fallback driver: `Dog Supervision Regulation Law, 5763–2002 (Israel). Hebrew title: ... 2002.` with no publisher/source. It is the only reference without a URL.
- Evidence: log line; `pages_R1/page_19.png`.
- Proposed correction: Change it to `@misc` (or `@legal` with a driver alias) with `howpublished`/`url` pointing to the official text (Nevo / Knesset / gov.il), and let FIXER verify it.
- Status: OPEN

### DET-1-13
- Severity: MINOR
- File: `book/chapters/chapter04_survival.tex:37`            - Page/Section: 14
- Problem: `בפעם הבאה תעזור "ערכת הכפילות" מפרק 3` refers to a term that does not exist in chapter 3. The ch.3 tip only says `קנו שני עותקים מכל דבר קטן`. A reader cannot find the reference.
- Evidence: `grep "כפילות" book/` → only ch4:37.
- Proposed correction: Either name the idea in ch.3 (e.g. `טיפ מהשטח` starts with `"ערכת כפילות": קנו שני עותקים...`) or rephrase ch.4: `בפעם הבאה יעזור הסט הכפול של ציוד (פרק~3).`
- Status: OPEN

### DET-1-14
- Severity: MINOR
- File: `book/frontmatter/introduction.tex:14`, `book/chapters/chapter02_city_mapping.tex:26`            - Page/Section: 4, 8
- Problem: Spelling `מעבר חציה` / `מעברי חציה`. In the book's full spelling (it writes `ברזייה`, `טעייה`, `שנייה`, `פנייה`) the correct form is `חצייה`.
- Evidence: source lines; `pages_R1/page_04.png`, `page_08.png`.
- Proposed correction: `מעבר חצייה`, `מעברי חצייה`.
- Status: OPEN

### DET-1-15
- Severity: SUGGESTION
- File: `book/chapters/chapter02_city_mapping.tex:5`            - Page/Section: 8 (chapter subtitle)
- Problem: `הגיאוגרפיה` is inconsistent with `גאומטריות` used three times (Academy spelling `גאוגרפיה`).
- Evidence: grep (see DET-1-14 command).
- Proposed correction: `הגאוגרפיה של גינות כלבים...`.
- Status: OPEN

### DET-1-16
- Severity: SUGGESTION
- File: `book/chapters/chapter01_psychology.tex` (tipbox "כללי המעלית", item 2)            - Page/Section: 6
- Problem: Repetition: `רצועה קצרה, לא מתוחה. הכלב צמוד אליכם, והרצועה לא מתוחה ולא נכרכת...`.
- Evidence: `pages_R1/page_06.png`.
- Proposed correction: `...הכלב צמוד אליכם, והרצועה רפויה ולא נכרכת סביב רגליים.`
- Status: OPEN

### DET-1-17
- Severity: SUGGESTION
- File: `book/chapters/chapter03_logistics.tex` ("שבוע לדוגמה" paragraph)            - Page/Section: 12
- Problem: The table uses `א'`/`ב'` for the two adults, but the text never says so.
- Evidence: `pages_R1/page_12.png`.
- Proposed correction: `...למשק בית עם שני אנשים עובדים (א' ו-ב') וכלב בוגר ובריא.`
- Status: OPEN

### DET-1-18
- Severity: SUGGESTION
- File: `book/chapters/chapter01_psychology.tex` (section "מעלית: ... ושש קומות של מתח")            - Page/Section: 6
- Problem: The narrative gets on at `קומה 3` and the figure is `מעלית לקומה 7`, which is four floors, not "שש קומות". Readers may notice.
- Evidence: `pages_R1/page_06.png`.
- Proposed correction: Change to `ארבע קומות של מתח` (and the TOC follows), or board at floor 1.
- Status: OPEN

### DET-1-19
- Severity: SUGGESTION
- File: `book/chapters/chapter03_logistics.tex` (example under eq. 3.1)            - Page/Section: 11
- Problem: Numbers are mixed: `20 דקות ... 15 ... 35 ... ועשר דקות`, then `= 80 min.` uses an English unit in a Hebrew sentence, which also ends the sentence with an English word.
- Evidence: `pages_R1/page_11.png`.
- Proposed correction: `ו-10 דקות לפני השינה` and `= 80\ \text{דקות}` (or drop the unit and say `כלומר 80 דקות` in the text).
- Status: OPEN

### DET-1-20
- Severity: SUGGESTION
- File: `book/backmatter/acknowledgments.tex:27-36`            - Page/Section: 20
- Problem: Against the CLAUDE.md rule "never end a Hebrew sentence with ... an English word if it can be avoided", 4 of 5 credit items and the "איך נבנה הספר" sentence end with `TikZ.`/`Python.`. Rendering is correct, but this is what students' OCR mis-read in item 11.
- Evidence: `R1_evidence/p20_credits.png`; `text_p20.txt`.
- Proposed correction: E.g. `סולם החשיפה, תרשים שנבנה בקוד \en{TikZ} במיוחד לספר.`, `מפה קונספטואלית שנוצרה בקוד \en{Python} מצורות גאומטריות.`, `...בקוד \en{Python} ובשפת השרטוט \en{TikZ} בתוך מסמך הספר.`
- Status: OPEN

### DET-1-21
- Severity: SUGGESTION
- File: `book/preamble.tex:30` (biblatex options), `book/references.bib`            - Page/Section: 19
- Problem: Access dates are in US format `visited on 11/18/2026`, which is ambiguous for Israeli readers. Web sources [1], [6], [9], [10] have no date at all.
- Evidence: `pages_R1/page_19.png`.
- Proposed correction: Add `urldate=iso` (or `urldate=long`) to the biblatex options. Add `year`/`date` where the page states one, or `n.d.`.
- Status: OPEN

### DET-1-22
- Severity: SUGGESTION
- File: build-wide (XeTeX/bidi)            - Page/Section: all pages with parentheses in Hebrew text (e.g. 19)
- Problem: The text layer stores mirrored parenthesis characters, so copy-paste or OCR of `(Source Audit)` / `(פרק 1)` returns reversed or unbalanced brackets. Visually everything is correct. This explains students' items 5/9/10 artefacts.
- Evidence: rawdict p.19: `(` at x=349 (left of `Source`), `)` at x=412 (right of `Audit`); `text_p19.txt`.
- Proposed correction: Informational only. Optionally mention in README that text extraction from the PDF is not a reliable proofreading source.
- Status: OPEN

### DET-1-23
- Severity: SUGGESTION
- File: `book/preamble.tex:187-191` (`calloutbase`: `top=5pt`, title `yshift=-8pt`)            - Page/Section: 2, 5, 6, 7, 9, 10, 12, 13, 20
- Problem: The boxed title tab ends about 1 pt above the ascenders of the first body line. There is no overlap, but it looks cramped.
- Evidence: `R1_evidence/p02_box_title.png`, `p05_box_tab.png`, `p06_mistake_tab.png`.
- Proposed correction: `top=8pt` (check that the page count stays 20).
- Status: OPEN

### DET-1-24
- Severity: SUGGESTION
- File: `book/backmatter/acknowledgments.tex` (last paragraph), `introduction.tex` (`ו\textbf{פרק 4}` is fine)            - Page/Section: 20
- Problem: `ו\en{Fixer}` attaches the Hebrew prefix directly to a Latin word (`וFixer`). Order is correct (ו x=438 is right of Fixer x=415), but Hebrew convention is `ו-Fixer`.
- Evidence: word positions p.20 y=533/534; `pages_R1/page_20.png`.
- Proposed correction: `ו-\en{Fixer}`.
- Status: OPEN

### DET-1-25
- Severity: SUGGESTION
- File: `book/backmatter/appendix.tex`            - Page/Section: 17
- Problem: The glossary is called "מילון" but is not alphabetical (ח, ע, מ, ב, מ, ק, ש, ש, ר, ת).
- Evidence: `pages_R1/page_17.png`.
- Proposed correction: Sort alphabetically (ברכיצפלי, חיזוק חיובי, מכת חום, מרחק נוח, עומס חושי, קסיליטול, ריחרוח, שבב אלקטרוני, שער כפול, תוכנית ב'), or rename it to "מונחים לפי סדר הופעה".
- Status: OPEN

### DET-1-26
- Severity: SUGGESTION
- File: `book/frontmatter/introduction.tex:23`            - Page/Section: 4
- Problem: `build/main.log:~2040`: `\endL or \endR problem (0 missing, 2 extra) detected at line 23` (the `\emph{למה}` legend item). The rendering looks right, but it is a bidi warning.
- Evidence: log excerpt.
- Proposed correction: This disappears if `\emph` is redefined (DET-1-06). Otherwise wrap it as `{\bfseries למה}`.
- Status: OPEN

---

## Checks passed (no issue)
- Page count 20 (K). All 4 chapters plus abstract, intro, TOC, 2 appendices, bibliography and about-page are present (A).
- Graph values in `figures/python/create_graph.py` (20/15/35/10, total 80) match figure 3.1, the formula example and the caption "להמחשה בלבד". Bars read right-to-left, and the rotated y-label order is correct (`R1_evidence/p12_graph_ylabel.png`).
- The 8-block diagram has exactly 8 numbered blocks, logical branches (כן → vet; לא בוודאות → monitor; new sign → vet), and safe advice (J).
- The map figure is legible and not clipped, and its Hebrew labels are in correct order.
- TOC page numbers match the actual pages for all entries checked (מעלית 6, גור בעיר 7, נימוסי גינה 10, שבוע לדוגמה 12, תיק חירום 13, כשזה כבר לא יומיומי 15, כרטיס חירום 16).
- Figure/table numbering is sequential (1.1, 1.2, 2.1, 3.1, 4.1; tables 2.1, 2.2, 3.1). Running headers show the correct chapter.
- No Overfull boxes and no Missing characters in the log. `audit_rtl_full.py` 2614/2614 bigrams in correct order; `check_rtl.py` 25/25.

## Severity summary
| Severity | Count | IDs |
|---|---|---|
| CRITICAL | 0 | — |
| MAJOR | 2 | DET-1-01, DET-1-02 |
| MINOR | 12 | DET-1-03 … DET-1-14 |
| SUGGESTION | 12 | DET-1-15 … DET-1-26 |
| **Total** | **26** | |

Students' list: REAL 1 · REAL-VISUAL 5 · NOT REPRODUCED 6 (11 items; items 2 and 9 split).

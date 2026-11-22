# SOURCE-AUDIT-R1 — FIXER source verification (task T-004)

- **Agent:** FIXER (`/book-fixer`, Responsibility A)
- **Date checked:** 2026-11-20 (all checks below were run on this date)
- **Scope:** all 10 entries of `book/references.bib` and claims C-01…C-24 in `docs/SOURCE_AUDIT.md`
- **Method:** WebFetch / WebSearch, plus the Crossref API (metadata), PubMed / PMC E-utilities (abstracts and full text)
  and Semantic Scholar (abstract). Downloaded PDFs were read page by page.
  No chapter text was edited. Only `book/references.bib` (metadata), `docs/SOURCE_AUDIT.md` and this report were changed.

## Summary

| Result | Count | Claims |
|---|---|---|
| VERIFIED | 7 | C-01, C-03, C-08, C-10, C-13, C-19, C-21 |
| PARTIALLY VERIFIED | 11 | C-02, C-04, C-06, C-07, C-09, C-14, C-17, C-20, C-22, C-23, C-24 |
| NEEDS CLARIFICATION | 3 | C-05, C-11, C-12 (the AVMA page could not be read) |
| UNSUPPORTED | 2 | C-15, C-16 |
| N/A | 1 | C-18 (illustrative data, unchanged) |

**Most important findings**
1. **AVMA page (`avma-warm`) could not be read.** `www.avma.org` returned an Incapsula bot-protection page (HTTP 200 with
   "Request unsuccessful") to WebFetch and curl, both at the bib URL and at the `/resources-tools/` URL that search engines now
   list. I did not try to get around the bot protection. Search-engine excerpts suggest the page exists and mentions hot
   asphalt burning paws. However, **the heatstroke sign list in the book (C-12) does not match the AVMA excerpts I saw**. It matches,
   almost item for item, the list on the Humane World for Animals page (HSVMA-derived), which I read in full. So C-12 is probably
   attributed to the wrong organisation.
2. **`hall2020` covers the risk factors but not "exercise is a common trigger".** That finding comes from a companion paper by the
   same authors: Hall, Carter & O'Neill 2020, *Animals* 10(8):1324, doi 10.3390/ani10081324. Exertional HRI made up 74.2% of events.
3. **`il-doglaw2002`: the leash rule, licensing, microchip marking and the rabies-vaccination condition are all in this law.**
   §11(א) covers the leash, §2(א) the licence for dogs over 3 months, and §3(ב)(2) + §4 the electronic-chip marking.
   §3(ב)(3) makes a licence valid only if the dog is vaccinated **"לפי הוראות פקודת הכלבת"**. The rabies obligation itself is
   therefore in the Rabies Ordinance, 1934, and the 2002 law makes it a condition for the licence. Citing this law for C-10 is correct.
4. **`avsab-puppy`:** the statement is dated **© 2008**. The direct PDF linked from the AVSAB index is now in the bib.
5. **`hiby2004` is a questionnaire study, not a review.** The book's wording "סקירות מחקר" (C-04) needs a small fix.
6. **The emergency instruction "do not induce vomiting" (C-15) is not on the ASPCA page.** Banfield Pet Hospital states it explicitly.
7. Several uncited general-advice claims are supported by sources I read: Royal Kennel Club (pavement test), RSPCA
   (separation anxiety, fireworks), and the Israeli Dog Supervision Regulations 2005 (chip readers). Ready-to-paste BibTeX is below.
   **Page-budget warning:** each new bib entry adds about 2–3 lines to the bibliography. The book is exactly 20 pages now.

## Part 1 — Bibliography entries

| Key | Opened (2026-11-20) | Verdict | What I saw / changes |
|---|---|---|---|
| `avma-warm` | `https://www.avma.org/resources/pet-owners/petcare/warm-weather-pet-safety` (WebFetch: empty; curl: Incapsula block page); `https://www.avma.org/resources-tools/pet-owners/petcare/warm-weather-pet-safety` (WebFetch: empty) | **NEEDS CLARIFICATION** | Content could not be read. Search results list a page titled "Warm weather pet safety" at both `avma.org/resources/…` and `www.avma.org/resources-tools/…`, so the URL may have moved. Not changed, because I could not verify it. MASTER or a human should open it in a normal browser, or the citations should be replaced (see C-05, C-11, C-12). |
| `aspca-apcc` | `https://www.aspca.org/pet-care/animal-poison-control` | **VERIFIED** (title corrected) | HTML title "ASPCA Poison Control \| (888) 426-4435 \| ASPCA". Text: "If you think your pet may have ingested a potentially poisonous substance, call (888) 426-4435." **Changed** the title from "Animal Poison Control" to "{ASPCA} Poison Control" and urldate to 2026-11-20. |
| `aspca-foods` | `https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets` | **VERIFIED** | Title "People Foods to Avoid Feeding Your Pets". Covers chocolate, grapes/raisins and xylitol ("…including gum, candy, baked goods and toothpaste"). No change. |
| `hall2020` | Crossref `api.crossref.org/works/10.1038/s41598-020-66015-8`; PubMed 32555323; PMC7303136 full text | **VERIFIED** | Title, authors (Emily J. Hall, Anne J. Carter, Dan G. O'Neill), *Scientific Reports* 10, article 9128, 2020 (issue 1, published 18 Jun 2020): all match. No change. |
| `avsab2021` | `https://avsab.org/wp-content/uploads/2021/08/AVSAB-Humane-Dog-Training-Position-Statement-2021.pdf` (PDF read, 4 pp.); index page `https://avsab.org/resources/position-statements/` | **VERIFIED** | "Position Statement on Humane Dog Training", footer "© 2021 American Veterinary Society of Animal Behavior". The URL resolves. The AVSAB index now links an identical copy at `…/uploads/2024/12/AVSAB-Humane-Dog-Training-Position-Statement-2021.pdf` (same content, checked p. 4). Bib left unchanged. |
| `avsab-puppy` | `https://avsab.org/wp-content/uploads/2024/12/Puppy-Socialization-Position-Statement-FINAL.pdf` (linked from the AVSAB index; PDF read); also the older copy `…/uploads/2018/03/Puppy_Socialization_Position_Statement_Download_-_10-3-14.pdf` | **VERIFIED** (URL corrected) | Title "AVSAB Position Statement On Puppy Socialization", footer "© 2008 AVSAB". The year 2008 is correct. **Changed** the URL from the index page to the direct PDF. |
| `ziv2017` | Crossref `10.1016/j.jveb.2017.02.004`; doi.org (redirects to Elsevier, 403); Purdue Canine Welfare Science summary page | **VERIFIED** | Gal Ziv, "The effects of using aversive training methods in dogs—A review", *J. Vet. Behav.* 19, 50–60, 2017 (May): all match. No change. |
| `hiby2004` | Crossref search (gives DOI 10.1017/S0962728600026683); Semantic Scholar abstract | **VERIFIED** (DOI added) | Hiby, Rooney, Bradshaw, *Animal Welfare* 13(1):63–69, 2004 (Feb): all match. **Added** `doi = {10.1017/S0962728600026683}`. Note: this is a questionnaire study of 364 owners, not a review. |
| `rspca-behaviour` | `https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour` and `…/behaviour/understanding` | **VERIFIED** (URL + title corrected) | The original URL resolves, but its title is "Understanding Your Dog's Behaviour" (heading "How to help your dog behave well") and it has **no body-language content**. The body-language guide is at `…/behaviour/understanding`, title "Understanding Your Dog's Body Language". **Changed** the URL and title to that page, and urldate to 2026-11-20. |
| `il-doglaw2002` | `https://he.wikisource.org/wiki/חוק_להסדרת_הפיקוח_על_כלבים`; `https://www.gov.il/BlobFolder/legalinfo/law-dog-supervision-2002/he/regulation_law-regulating-supervision%20of%20dogs.pdf` (official gov.il copy of the updated Nevo text, read pp. 1–5) | **VERIFIED** (URL added) | Title "חוק להסדרת הפיקוח על כלבים, תשס"ג-2002", published in ס"ח 1884 on 29.12.2002. **Added** the gov.il URL, urldate and a note. The English title is kept as a descriptive translation. |

`python scripts/build_book.py --no-figs` was run after the bib changes, with this output:
`PDF: output\final_book.pdf  pages=20 (max 20)` · `overfull hbox=0  'undefined' mentions=2  missing glyphs=0`. The two "undefined"
mentions are the existing italic font-shape warnings for David/Gisha (`main.log` lines 2047/2093), not undefined
citations. `main.blg` has 0 warnings. The bibliography renders on p. 19.

## Part 2 — Claims

**C-01** (ch. 1, `rspca-behaviour`): welfare organisations recommend learning body language to spot stress early. **VERIFIED.**
After the URL fix, the RSPCA page says: "Use this guide to help you recognise important body language signals and get to know how
your dog is feeling" and lists "worried" signals. ASPCApro ("Canine Body Language Tips") adds that "Yawning and lip licking
may be early signs of stress". The plural "ארגונים" would be fully covered if `aspcapro-body` is also cited (optional).

**C-02** (ch. 1, `rspca-behaviour`): stress/fear signs. **PARTIALLY VERIFIED.** RSPCA lists "Tail is tucked under", "ears are
back", "they're yawning", "They're licking their lips". It does **not** list the visible eye white, freezing or escape attempts.
ASPCApro "Canine Body Language Tips" (https://www.aspcapro.org/resource/canine-body-language-tips) lists all seven signs:
whale eye ("lots of white showing"), "freeze completely", "frantically try to escape", tucked tail, ears "pinned … back", yawning
and lip licking. *Proposal:* keep the text and add `aspcapro-body` to the "לחוץ או מפחד" box:
`… קפיאה או ניסיון לברוח \cite{rspca-behaviour,aspcapro-body}.`

**C-03** (ch. 1, `avsab2021`): AVSAB recommends reward-based training and opposes punishment. **VERIFIED.** "AVSAB recommends that
only reward-based training methods are used for all dog training… AVSAB therefore advises that aversive methods should not
be used". *Optional precision:* "מסתייג" understates the source, so "ומתנגד לשימוש בשיטות ענישה" is closer. Note also that AVSAB is a
*Society of Animal Behavior*, so "האגודה הווטרינרית האמריקאית להתנהגות בעלי חיים" is a more exact rendering than "איגוד
הווטרינרים האמריקאי לרפואה התנהגותית" (minor; MASTER's call).

**C-04** (ch. 1, `ziv2017`, `hiby2004`): "reviews found" that pain/fear-based methods carry higher risk. **PARTIALLY VERIFIED.** Ziv
2017 is a review: aversive methods "can jeopardize both the physical and mental health of dogs" (Purdue summary of the abstract;
the publisher page returned 403). Hiby 2004 is **not a review**. It is a questionnaire study in which punishment was associated with more problem behaviours
("we conclude that it may represent a welfare concern"). *Proposed rewording:*
`וסקירת מחקר וסקר בקרב בעלי כלבים מצאו ששיטות אימון מבוססות ענישה או הפחדה קשורות לסיכון גבוה יותר לבעיות התנהגות ולפגיעה ברווחה \cite{ziv2017,hiby2004}.`

**C-05** (ch. 2, `avma-warm`): asphalt is much hotter than air, burns paws; AVMA advises limiting activity, shade and water.
**NEEDS CLARIFICATION.** The AVMA page could not be read (see Part 1). Search excerpts attribute "Avoid hot surfaces, such as asphalt,
that can burn your pet's paws" to it, but I have not read it. Other sources I did read:
Royal Kennel Club "The danger of hot pavements": pavements "will usually be much warmer than the air outside".
Humane World for Animals "How to Keep Pets Safe in High Temperatures": "Asphalt gets very hot and can burn your pet's paws, so walk
your dog on the grass if possible"; "On very hot days, limit exercise to early morning or evening hours"; "plenty of fresh, cold
water"; shade. *Proposed rewording (if AVMA cannot be confirmed):*
`בימים חמים המדרכה יכולה להתחמם הרבה יותר מהאוויר \cite{rkc-pavements}, ואספלט לוהט עלול לגרום לכוויות בכפות. ארגוני רווחת בעלי חיים ממליצים להגביל פעילות בימים חמים לשעות הבוקר המוקדמות והערב, לדאוג לצל ולמים וללכת על דשא כשאפשר \cite{humane-heat}.`

**C-06** (ch. 2 & 4, `hall2020`): exercise is a common trigger; higher risk in brachycephalic, heavier and older dogs. **PARTIALLY
VERIFIED.** Hall 2020 *Sci Rep* (PubMed abstract and PMC full text) supports the risk factors. It reports "Dogs with a brachycephalic skull shape
and dogs weighing over 50 kg were also at greater risk", bodyweight at or above the breed/sex mean (OR 1.42), and "dogs ≥12 years had the
greatest odds of HRI (OR 1.75)". It does **not** report triggers. Hall, Carter & O'Neill 2020, *Animals* 10(8):1324 (PubMed 32751913)
reports: "Exertional heat-related illness was the predominant trigger (74.2% of events)". Ch. 4 line 62 cites only the risk factors,
so that part is fine. *Proposal for ch. 2:*
`מחקר על כלבים בבריטניה מצא שפעילות גופנית היא הגורם השכיח ביותר למכת חום \cite{hall2020exertional}, ושהסיכון גבוה יותר בכלבים ברכיצפליים (בעלי אף קצר), בכלבים כבדים ובכלבים מבוגרים \cite{hall2020}.`

**C-07** (ch. 2, no cite): back-of-hand pavement test. **PARTIALLY VERIFIED** (supported, but not cited). Royal Kennel Club: "place
the back of your hand on the pavement for seven seconds" (https://www.royalkennelclub.com/hotpavements). A PDSA vet nurse quoted in
Countryfile uses 5 seconds (search excerpt only). The text already hedges ("בדיקה גסה"). *Proposal:* `…הניחו את גב כף היד על המדרכה לכמה שניות \cite{rkc-pavements}.`

**C-08** (ch. 2, `il-doglaw2002`): the law sets public-space rules including a leash. **VERIFIED.** §11(א): "המחזיק בכלב לא יאפשר
את יציאתו מתחומי חצריו … אלא אם כן הכלב מוחזק בידי אדם המסוגל לשלוט בו, באמצעות רצועה שאת אורכה וטיבה יקבע השר"
(gov.il / Nevo text, p. 5).

**C-09** (ch. 2, no cite): local authorities have bylaws (waste pick-up, off-leash areas). **PARTIALLY VERIFIED.** Off-leash areas:
§11(ב) of the 2002 law lets **the head of the local authority** set areas and times where the leash duty does not apply (verified).
Waste pick-up: municipal bylaws exist, for example the Tel Aviv-Yafo (שמירת הסדר והניקיון) bylaw and its DNA amendment, but I saw this only in a
news search result (ice.co.il) and did not open the official bylaw text. The sentence is generic and already says "check your city website".
*Proposed rewording:*
`בנוסף, ראש הרשות המקומית רשאי לקבוע אזורים ושעות שבהם מותר לשחרר כלבים בלי רצועה \cite{il-doglaw2002}, ולרשויות רבות יש חוקי עזר משלהן, למשל לגבי איסוף צואה.`

**C-10** (ch. 3, `il-doglaw2002`): microchip, licensing and rabies vaccination are mandatory. **VERIFIED.** §2(א): no keeping a dog
older than 3 months without a valid licence. §3(ב): the licence is valid only if (2) "הכלב מסומן לפי הוראות חוק זה" and (3) "הכלב מחוסן
לפי הוראות פקודת הכלבת". §4(א): marking "באמצעות סימון תת עורי בשבב אלקטרוני". The vaccination duty itself comes from the Rabies Ordinance
1934, and this law makes it a licence condition. *Optional precision:* `…סימון בשבב אלקטרוני ורישוי, ותנאי לרישיון הוא חיסון נגד כלבת \cite{il-doglaw2002}.`

**C-11** (ch. 3, `avma-warm`): carry water, especially on hot days. **NEEDS CLARIFICATION** (AVMA unreadable). Humane World
supports it: "make sure they have protection from heat and sun and plenty of fresh, cold water". *Proposal:* change the cite to `\cite{humane-heat}`
(ch. 3 lines 20 and 69, and the ch. 2 season table line 95) unless AVMA is confirmed.

**C-12** (ch. 4, `avma-warm`): "AVMA lists heatstroke signs: heavy panting, profuse drooling, weakness/incoordination, vomiting,
very dark tongue, seizures, unconsciousness". **NEEDS CLARIFICATION, probably attributed to the wrong organisation.** I could not read the AVMA page.
The AVMA-related excerpts I saw (search results) give a different list (anxiousness, excessive panting, restlessness, excessive drooling; the AVMA
first-aid page: heavy panting, excessive drooling, weakness, confusion, vomiting, gum colour). Humane World for Animals lists:
"heavy panting, glazed eyes, a rapid heartbeat, difficulty breathing, excessive thirst, lethargy, fever, dizziness, lack of coordination,
profuse salivation, vomiting, a deep red or purple tongue, seizure and unconsciousness". That matches the book's list. *Proposed rewording:*
`ארגוני רווחת בעלי חיים מונים בין סימני מכת החום התנשפות חזקה, ריור מרובה, חוסר יציבות, הקאה, לשון אדומה-כהה או סגולה, פרכוסים ואובדן הכרה \cite{humane-heat}.`

**C-13** (ch. 4, `aspca-foods`): chocolate, grapes/raisins and xylitol products are dangerous. **VERIFIED.** All three are on the page.
Xylitol is "used as a sweetener in many products, including gum…", and the page also covers grapes/raisins and kidney damage.

**C-14** (ch. 4, `aspca-apcc`): ASPCA says contact a vet or animal poison control immediately. **PARTIALLY VERIFIED.** The cited
landing page only says "call (888) 426-4435". The ASPCA article "What to Do if Your Pet Is Poisoned" (20 Mar 2019,
https://www.aspca.org/news/what-do-if-your-pet-poisoned) says: "Call APCC at (888) 426-4435 or Your Local Veterinarian Immediately". *Proposal:*
keep the sentence and change the cite to `\cite{aspca-poisoned}` (or `\cite{aspca-apcc,aspca-poisoned}`).

**C-15** (ch. 4 emergency box; listed as `aspca-apcc`): do not induce vomiting or give remedies without explicit vet instruction. **UNSUPPORTED by
the listed source.** The ASPCA pages do not mention vomiting. The 2019 article only says to consult a professional before "giving your pet
anything after a possible poisoning". Banfield Pet Hospital, "Help for pet poisoning: what to do right now"
(https://www.banfield.com/Wellness-at-banfield/First-aid/Poisonings), says: "Do not induce vomiting or give your pet a home remedy unless a
veterinarian" directs you to, and "Do not give your pet anything by mouth or attempt to treat the poisoning yourself". *Proposal:* keep the text,
because it is correct and safety-critical, and add `\cite{banfield-poison}` at the end of the first bullet.

**C-16** (ch. 4, no cite): "sniffing calms many dogs". **UNSUPPORTED.** The only evidence I found is a non-peer-reviewed citizen-science
field study (pulse drop while sniffing, reported via animalhealthdigest.com / Tufts *Your Dog*, search excerpts only). I found no
authoritative source. *Proposed rewording (ch. 4):*
`יוצאים מהסביבה העמוסה לפינה שקטה, נותנים לכלב לרחרח בקצב שלו ומסיימים את הטיול מוקדם.`
The same claim appears in the appendix glossary ("וגם דרך להירגע"). Suggest
`טיול עם הרבה ריחרוח הוא גם העשרה חשובה.`

**C-17** (ch. 4, no cite): a sudden refusal may indicate pain, so consult a vet. **PARTIALLY VERIFIED.** RSPCA dog-behaviour page: "If you notice a
change, ask your vet for advice". It says a changed dog "could be distressed, bored, ill or injured". AVSAB 2021: the vet evaluates "if there are
medical factors contributing to the behavior concern". The text is already hedged ("כדאי לחשוב גם על…"). *Proposal:* keep it as a recommendation.
Optionally cite `\cite{avsab2021}`, which is already in the bib.

**C-18:** N/A. Explicitly illustrative data, not audited.

**C-19** (ch. 1, `avsab-puppy`): early, controlled, positive socialisation, coordinated with the vet regarding vaccination. **VERIFIED.** AVSAB:
puppies "should be exposed to as many new people, animals, stimuli and environments as can be achieved safely and without causing
over-stimulation"; "it should be the standard of care for puppies to receive such socialization before they are fully vaccinated";
"a minimum of one set of vaccines at least 7 days prior to the first class"; training "based on positive reinforcement". The vet-coordination
clause is a fair practical gloss, since the vaccination conditions are veterinary matters and the statement says fearful puppies "should seek veterinary guidance".

**C-20** (ch. 1, `avsab2021`): home-alone distress is not "revenge", it is treatable, and the owner should see a vet and then a reward-based trainer. **PARTIALLY VERIFIED.**
AVSAB 2021 supports "separation anxiety… should always be evaluated by a veterinarian" and reward-based methods only. It does not mention "revenge" or
list the signs. RSPCA "Separation Anxiety in Dogs" (https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour/separationrelatedbehaviour)
lists "Destructive behaviour", "Howling, barking, whining", "Toileting", says SRB "is preventable and treatable", advises talking "to a vet… who should
then refer you to a clinical animal behaviourist", and says "Never punish your dog". It explains that an apparently guilty look is misread by owners, but it does
not use the word "revenge". *Proposed rewording:*
`חשוב לזכור שזו לא "נקמה": התנהגויות כאלה הן לרוב סימן למצוקה כשהכלב נשאר לבד, ואפשר למנוע אותן ולטפל בהן \cite{rspca-separation}.`
In the knowbox, use `\cite{avsab2021,rspca-separation}`.

**C-21** (ch. 4, `avsab2021`): avoid equipment that works through pain or pressure on the neck. **VERIFIED.** AVSAB FAQ: "An appropriate trainer should avoid
any use of training tools that involve pain (choke chains, prong collars, or electronic shock collars)… physical correction techniques (leash jerking…)".
Choke and prong collars act on the neck.

**C-22** (ch. 4 and appendix, no cite): a vet or the municipal veterinary service can scan the microchip of a stray dog. **PARTIALLY VERIFIED.** Dog Supervision Regulations
5765-2005 (gov.il / Nevo PDF `pets_999_388.pdf`) §8(ב)(1): an authorised marking vet must have a "קורא שבבים". Law §9(ב): the registry notifies the owner about a found
marked dog, and §13(ב) does the same for a dog seized by the municipal service. This supports the mechanism. I found no official "found a dog" procedure page.
*Proposal:* keep the text and add `\cite{il-dogregs2005}` (new entry), or keep it uncited as practical advice.

**C-23** (ch. 4, no cite): for noise-phobic dogs, see the vet in advance of fireworks. **PARTIALLY VERIFIED** (supported, not cited). RSPCA "Keeping dogs, cats and other
small pets safe during fireworks" (https://www.rspca.org.uk/adviceandwelfare/fireworks/pets) says: "prepare well in advance", "Ask your vet about pheromone diffusers",
"Walk your dog during daylight hours", "Close windows and curtains", "Create a safe space", and "Don't try to coax them out". This matches the whole paragraph.
*Proposal:* add `\cite{rspca-fireworks}` at the end of the paragraph.

**C-24** (ch. 2 line 113, **no cite in text**): puppies should see the vet before a first dog-park visit. **PARTIALLY VERIFIED.** AVSAB puppy statement:
"Visits to dog parks or other areas that are not sanitized and/or highly trafficked by dogs of unknown vaccination or disease status should be avoided."
The book's advice is consistent but softer. *Proposed rewording:*
`\item \textbf{גורים:} עד להשלמת החיסונים עדיף להימנע מגינות כלבים עמוסות, ואת הביקור הראשון מתאמים עם הווטרינר \cite{avsab-puppy}.`

## Part 3 — Proposed new BibTeX entries (verified 2026-11-20, NOT yet added)

These are not in `references.bib`, because adding them only matters together with the text changes MASTER chooses. All values
were read on the source itself, except where marked.

```bibtex
@article{hall2020exertional,
  author  = {Hall, Emily J. and Carter, Anne J. and O'Neill, Dan G.},
  title   = {Dogs Don't Die Just in Hot Cars{\textemdash}Exertional Heat-Related Illness (Heatstroke) Is a Greater Threat to {UK} Dogs},
  journal = {Animals},
  volume  = {10},
  number  = {8},
  pages   = {1324},
  year    = {2020},
  doi     = {10.3390/ani10081324}
}
@online{humane-heat,
  author  = {{Humane World for Animals}},
  title   = {How to Keep Pets Safe in High Temperatures},
  url     = {https://www.humaneworld.org/en/resources/keep-pets-safe-temperature-gets},
  urldate = {2026-11-20}
}
@online{rkc-pavements,
  author  = {{The Royal Kennel Club}},
  title   = {The danger of hot pavements},
  url     = {https://www.royalkennelclub.com/hotpavements},
  urldate = {2026-11-20}
}
@online{aspcapro-body,
  author  = {{ASPCA}},
  title   = {Canine Body Language Tips},
  url     = {https://www.aspcapro.org/resource/canine-body-language-tips},
  urldate = {2026-11-20}
}
@online{aspca-poisoned,
  author  = {{ASPCA}},
  title   = {What to Do if Your Pet Is Poisoned},
  date    = {2019-03-20},
  url     = {https://www.aspca.org/news/what-do-if-your-pet-poisoned},
  urldate = {2026-11-20}
}
@online{banfield-poison,
  author  = {{Banfield Pet Hospital}},
  title   = {Help for pet poisoning: what to do right now},
  url     = {https://www.banfield.com/Wellness-at-banfield/First-aid/Poisonings},
  urldate = {2026-11-20}
}
@online{rspca-separation,
  author  = {{RSPCA}},
  title   = {Separation anxiety in dogs},
  url     = {https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour/separationrelatedbehaviour},
  urldate = {2026-11-20}
}
@online{rspca-fireworks,
  author  = {{RSPCA}},
  title   = {Keeping dogs, cats and other small pets safe during fireworks},
  url     = {https://www.rspca.org.uk/adviceandwelfare/fireworks/pets},
  urldate = {2026-11-20}
}
@legislation{il-dogregs2005,
  title   = {Dog Supervision Regulation Regulations, 5765{\textendash}2005 (Israel)},
  note    = {Hebrew title: Takanot le-Hasdarat ha-Pikuah al Klavim. Full updated text (Nevo) hosted by gov.il},
  year    = {2005},
  url     = {https://www.gov.il/BlobFolder/generalpage/national-database-for-dog-registration-and-obligation-to-subscribe-general-information/he/pets_999_388.pdf},
  urldate = {2026-11-20}
}
```

Page budget: the book is exactly 20 pages, with the bibliography on p. 19. If MASTER adopts several of these, rebuild and check the page count.
A space-saving option is to *replace* `avma-warm` with `humane-heat`, which is a net zero entries.

## Part 4 — URLs actually opened (2026-11-20)
- avma.org warm-weather page (both `/resources/` and `/resources-tools/` paths): blocked (Incapsula); AVMA `/walking-your-pet` and `/first-aid-tips-pet-owners`: blocked
- https://www.aspca.org/pet-care/animal-poison-control · https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets · https://www.aspca.org/news/what-do-if-your-pet-poisoned
- https://api.crossref.org/works/10.1038/s41598-020-66015-8 · https://api.crossref.org/works/10.1016/j.jveb.2017.02.004 · Crossref bibliographic query for Hiby 2004
- PubMed E-utilities: PMID 32555323, PMID 32751913; PMC E-utilities: PMC7303136 (full text)
- https://www.nature.com/articles/s41598-020-66015-8 (redirects to a login page) · https://doi.org/10.1016/j.jveb.2017.02.004 (redirects to Elsevier, 403)
- https://api.semanticscholar.org (Ziv 2017: abstract withheld; Hiby 2004: abstract) · https://caninewelfare.centers.purdue.edu/resource/the-effects-of-using-aversive-training-methods-in-dogs-a-review
- https://avsab.org/wp-content/uploads/2021/08/AVSAB-Humane-Dog-Training-Position-Statement-2021.pdf · https://avsab.org/wp-content/uploads/2024/12/AVSAB-Humane-Dog-Training-Position-Statement-2021.pdf · https://avsab.org/resources/position-statements/
- https://avsab.org/wp-content/uploads/2018/03/Puppy_Socialization_Position_Statement_Download_-_10-3-14.pdf · https://avsab.org/wp-content/uploads/2024/12/Puppy-Socialization-Position-Statement-FINAL.pdf
- https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour · …/behaviour/understanding · …/behaviour/separationrelatedbehaviour · https://www.rspca.org.uk/adviceandwelfare/fireworks/pets
- https://www.aspcapro.org/resource/canine-body-language-tips
- https://www.humaneworld.org/en/resources/keep-pets-safe-temperature-gets
- https://www.royalkennelclub.com/hotpavements (redirected from thekennelclub.org.uk/hotpavements)
- https://www.banfield.com/Wellness-at-banfield/First-aid/Poisonings
- https://he.wikisource.org/wiki/חוק_להסדרת_הפיקוח_על_כלבים · gov.il law PDF (above) · gov.il regulations PDF `pets_999_388.pdf`

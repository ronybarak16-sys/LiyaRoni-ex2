# QA report

## Automated checks (master, reproducible by anyone)
| Check | Command | Latest result |
|---|---|---|
| Build | `python scripts/build_book.py` | success, 13 pages, 0 overfull hbox, 0 missing glyphs |
| RTL word order | `python scripts/check_rtl.py` | 18/18 probes PASS |
| Project validation | `python scripts/validate_project.py` | see `docs/VALIDATION_RESULTS.md` |

## Independent QA rounds (DETECTOR)
| Round | Date | Scope | CRIT | MAJ | MIN | SUG | Report | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | — | full review A–P | — | — | — | — | `Detector/reports/QA-R1.md` | **NOT STARTED – detector session not running** |

Master's own pre-QA self-inspection findings are in `docs/ISSUE_TRACKER.md` (M-01…M-11). They are
not a substitute for independent review.

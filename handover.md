# Handover

**Last Updated:** 2026-08-02
**Session:** Philips Feedback + Evaluations (360, HeartStyles, Anytime 2020-2025, 18 PPMs)

---

## Last Completed Action

- Ingested Philips 360 Leadership Feedback (DDI, Dec 2020) — 14 raters, all competencies above company avg
- Ingested HeartStyles 360 (Dec 2025) — Encouraging 93%, 4 respondents, Ergos Mind program
- Ingested Philips Anytime Feedback 2020-2025 (6 files, 177 total entries)
- Processed 18 career evaluation/PPM files (2013-2025) — 17 already ingested, 1 new (2025)
- Previous: Amazon profile + reviews + 48 appreciation emails

## Current State

| Aspect | Status |
|--------|--------|
| Phase | 7 — Cloud Deployment (only remaining) |
| Tests | 227 passing, 2 skipped |
| Knowledge Graph | 884 artifacts, 2,038 nodes, 7,648 edges |
| Embeddings | 21,346 chunks in ChromaDB |
| Git Remote | `git@github.com:dsvellal/dsvellal-career-catalogue.git` (main) |

### Node Breakdown
| Type | Count |
|------|-------|
| skill | 685 |
| time_range | 390 |
| achievement | 380 |
| project | 268 |
| person | 245 |
| organization | 70 |

## Philips Feedback Summary (This Session)

| File | Year | Entries | Key Rating |
|------|------|---------|------------|
| 360 Leadership (DDI) | 2020 | 14 raters | All 5 behaviors above company avg (+0.24 to +0.39) |
| HeartStyles 360 | 2025 | 4 raters | Encouraging 93%, Developing 82%, Transforming 80% |
| Anytime Feedback | 2020 | 57 entries | Engagement 9.5/10, Recommend 9.5/10 |
| Anytime Feedback | 2021 | 28 entries | Work-again 9.4/10, Recommend 9.6/10, Mentoring 9.3/10 |
| Anytime Feedback | 2022 | 17 entries | "Level-headed, calm, T-shaped knowledge" |
| Anytime Feedback | 2023 | 25 entries | Global scope (4 locations), "strategic thinking" |
| Anytime Feedback | 2024 | 28 entries | Directors praise, 6 locations, Developer Days India |
| Anytime Feedback | 2025 | 22 entries | 9.6/10 overall, €350K AI funding, "force multiplier" |

## Career Evaluation Arc (PPM files 2013-2025)

- **Exeter 2013-2015:** "Thought leader of OneGate and Exeter" — consistently exceeds
- **Amazon 2016-2018:** Ownership LP 16/16 unanimous; peers recommended TPM path
- **Philips 2018-2021:** Meets → Top Score → Role Model in ALL behaviors + US relocation
- **Philips NA 2021-2025:** EXCELLING; "yet to meet anybody who doesn't regard you as role model"; primary GenAI driver (€61K revenue, 73% of total)

## In-Progress Work

None.

## Next Steps

1. **Commit & push** — done
2. **More Philips data** — if user provides more files
3. **Wishlist feature #1: OKF Conversion** — when user requests
4. **Skill deduplication** — 685 skills likely have semantic duplicates

## Blockers

None.

## Key Context

- Graph now has comprehensive coverage: IBM (via career batch), Exeter (97 files), Amazon (profile + 2 reviews + 48 emails), Philips (feedback 2019-2025 + evaluations)
- 245 people in the graph across all organizations
- Anytime Feedback scores consistently 9.3-9.6/10 across 5 years
- 2025 marks AI pivot: GenAI driver, €350K funding secured, 100 NPS, "force multiplier"

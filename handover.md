# Handover

**Last Updated:** 2026-08-05T23:15:00Z
**Session:** Data representation architecture — full implementation

---

## Last Completed Action

Fully implemented the data representation architecture from the brainstorm session:

1. **Philips timeline split** — "Philips USA" (34 items, Cambridge MA, 2021-12-06+) and "Philips India" (75 items, Bangalore, 2018-09-18 to 2021-12-04)
2. **Three-level drill-down** on all three content views:
   - **Timeline**: Level 1 (row) → Level 2 (rich summary card with evidence ref) → Level 3 (full artifact modal)
   - **Impact Wall**: Level 1 (stat card) → Level 2 (expanded detail with evidence) → Level 3 (full artifact modal)
   - **Voices**: Level 1 (quote card) → Level 2 (detail card with evidence) → Level 3 (full artifact modal)
3. **Evidence index in DuckDB** — 562 files indexed, queryable by era, year, NPS, people, programs, category
4. **`twin publish --viz-only`** command generates split timeline + evidence-enriched data
5. **`twin index-evidence`** command rebuilds the evidence_index table
6. **Evidence file serving** via symlink for full artifact rendering
7. **Improved evidence matching** — uses DuckDB evidence_index for better file matching (43 items matched so far)

---

## Current State

| Aspect | Status |
|--------|--------|
| Phase | Data representation architecture (COMPLETE) |
| Knowledge graph | 3,471 nodes, 17,190 edges, 25,767 chunks |
| Evidence index | 562 files indexed in DuckDB (349 Philips India, 213 Philips USA) |
| Evidence files | 600+ markdown files in data/evidence/ |
| Viz tabs | 8 live at http://localhost:5174 |
| Timeline | 6 eras, 353 items, 43 with evidence links (12%) |
| Three-level drill-down | Working on Timeline, Impact, and Voices |
| Tests | 227 pass, 2 skipped |
| Build | TypeScript clean (pre-existing CareerArc warning only) |
| Git | Uncommitted changes |

### Files Changed This Session

| File | Change |
|------|--------|
| `scripts/publish_viz_data.py` | NEW — generates split timeline + evidence-enriched JSON |
| `src/twin/ingestion/evidence_index.py` | NEW — parses/indexes evidence markdown into DuckDB |
| `src/twin/db.py` | Updated — creates evidence_index table on init |
| `src/twin/cli.py` | Updated — `publish` runs viz data gen, new `index-evidence` cmd |
| `viz/src/Timeline.tsx` | Rewritten — split eras, three-level drill-down, artifact viewer |
| `viz/src/ImpactWall.tsx` | Rewritten — three-level drill-down with evidence |
| `viz/src/Voices.tsx` | Rewritten — three-level drill-down with evidence |
| `viz/src/Hero.tsx` | Updated — split era colors, tagline |
| `viz/src/styles.css` | Added — artifact overlay, evidence indicators, voices detail, impact evidence |
| `viz/src/data/timeline_full.json` | Regenerated — 6 split eras with evidence refs |
| `viz/vite.config.ts` | Updated — fs.allow for parent dir |
| `viz/public/data/evidence` | NEW — symlink to `../../../data/evidence` |
| `tests/test_db.py` | Updated — added evidence_index to expected tables |
| `decisions.md` | 4 new decisions (Philips split, data arch, drill-down UX, reverse chrono) |
| `prompts.md` | Prompt 039 logged |
| `DESIGN.md` | Replaced — comprehensive UI screen design doc with ASCII mockups |

---

## In-Progress Work

None — all planned items from this session are complete.

---

## Next Steps

1. **Improve evidence matching** — currently 12% of timeline items have evidence links; could increase with better fuzzy matching or manual annotation
2. **Enrich timeline item summaries** — pull richer narratives from evidence markdown during publish
3. **Split graph JSON** per sub-view (5 files instead of 1 monolithic graph.json)
4. **API endpoints** — build FastAPI view-specific endpoints (`/api/viz/timeline`, `/api/viz/impact`, etc.)
5. **LLM query planner** — implement the unified search interface for chat twin
6. **Phase 7: Cloud Deployment** — static viz + FastAPI backend

---

## Blockers

None.

---

## Key Context

- **Architecture decisions:** Live API for chat/generators, static publish for viz, view-specific endpoints, LLM query planner, evidence in DuckDB, curated highlights + drill-down
- **Split date:** 2021-12-05 (India before, USA after)
- **Evidence symlink:** `viz/public/data/evidence → ../../../data/evidence`
- **Dev server:** `cd viz && npm run dev` (runs on 5174 if 5173 taken)
- **Publish:** `uv run twin publish --viz-only` regenerates all viz JSON
- **Index:** `uv run twin index-evidence` rebuilds evidence_index (562 files)
- **Tests:** `uv run python3 -m pytest tests/` (227 pass)
- **Three-level UX:** Summary → Rich Summary → "Explore the full story" (full markdown)
- Claude IS the LLM for classification (no Gemini dependency)
- CLAUDE.md mandates Evidence Generation Protocol for every ingestion

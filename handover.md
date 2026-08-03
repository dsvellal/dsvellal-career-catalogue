# Handover

**Last Updated:** 2026-08-02T23:50:00Z
**Session:** Full interactive portfolio — 8 tabs, Knowledge Graph, quality fixes

---

## Last Completed Action

Built and polished the full interactive career portfolio. Fixed Hero counter (7,000+ was showing 7+) and rebuilt voices.json with 220 clean, human-readable quotes (previously 60, many raw filenames). Committed and pushed all changes.

---

## Current State

| Aspect | Status |
|--------|--------|
| Phase | 7 — Cloud Deployment (only remaining) |
| Viz tabs | **8 live** at `http://localhost:5173` |
| Build | Clean (`npm run build ✓`, no TS errors in new files) |
| Data files | `graph.json` (1MB) + `voices.json` (220 quotes) + `talks.json` + `impact.json` + `timeline.json` |
| DB | 913 artifacts, 2,169 nodes, 13,514 edges |
| Git | Committed and pushed to main |

### Tab inventory

| Tab | Component | Data source |
|-----|-----------|-------------|
| Overview | `Hero.tsx` | Static KPIs (animated count-up) |
| Professional Identity | `Constellation.tsx` | `constellation.json` |
| Career Arc | `CareerArc.tsx` | `career_arc.json` |
| Impact | `ImpactWall.tsx` | `impact.json` (8 cards) |
| Timeline | `Timeline.tsx` | `timeline.json` (4 eras, 23 milestones) |
| Voices | `Voices.tsx` | `voices.json` (220 quotes) |
| Talks & Givebacks | `TalksGivebacks.tsx` | `talks.json` (43 entries) |
| Knowledge Graph | `KnowledgeGraph.tsx` | `graph.json` (5 sub-views) |

### Knowledge Graph sub-views

| Sub-view | What it shows |
|----------|---------------|
| Force Graph | D3 force-directed, 148 nodes / 1,619 edges, zoom/pan/click |
| Org Subgraph | Bipartite project→skill per company (IBM/Exeter/Amazon/Philips) |
| Skill Heatmap | 20×20 co-occurrence matrix, hover tooltips |
| Timeline Radial | Polar chart, 913 artifacts · 20 years arc bands |
| Ego Explorer | Search any node, traverse 1-hop graph, breadcrumb trail |

---

## In-Progress Work

None.

---

## Next Steps

1. **Phase 7: Cloud Deployment** — deploy FastAPI backend + viz frontend; see `plan.md`
2. **Optional viz improvements:**
   - graph.json is 1MB static import — consider `React.lazy` + `import()` for production bundle splitting
   - Org Subgraph bipartite layout could use stronger x-force pins to separate columns more clearly
   - Timeline Radial project dots cluster together at same year — add orbit radius variation

---

## Blockers

None.

---

## Key Context

- Dev server: `cd viz && npm run dev` → `http://localhost:5173`
- All data is static JSON in `viz/src/data/` — no API server needed
- Pre-existing TS errors in `CareerArc.tsx` and `Constellation.tsx` are pre-existing, not new
- voices.json is regenerated from DuckDB with quality filter (strips filename-style entries, requires ≥35 chars, no date slugs)
- Era colors (consistent across all components): IBM=#3987e5 / Exeter=#d95926 / Amazon=#199e70 / Philips=#c98500

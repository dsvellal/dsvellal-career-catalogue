# Handover

**Last Updated:** 2026-08-03T03:45:00Z
**Session:** Remove em/en-dashes, humanize all content across components and data files

---

## Last Completed Action

Removed all em-dashes and en-dashes from every authored component and data file. Rewrote affected copy as natural, flowing prose:

- `Hero.tsx` — bio rewritten as plain prose; snazzy tagline uses a comma instead of an em-dash; aria-labels cleaned
- `Voices.tsx`, `TalksGivebacks.tsx`, `Timeline.tsx` — section subtitles and date ranges humanized
- `impact.json` — all detail fields rewritten as conversational sentences; "86–89%" stat fixed
- `timeline.json` — roles and milestone details cleaned ("to" replaces arrows and dashes in prose)

CSS comments with dashes intentionally left (not user-visible). Pre-existing files not touched.

---

## Current State

| Aspect | Status |
|--------|--------|
| Phase | 7 — Cloud Deployment (only remaining) |
| Viz tabs | **8 live** at `http://localhost:5173` |
| Build | Clean (`npm run build ✓`) |
| Git | Committed and pushed to `main` |

### Hero overview (Overview tab)

| Element | Value |
|---------|-------|
| Full name | DATTATREYA SUBRAMANYA VELLAL (small caps above display name) |
| Display name | Datta Vellal |
| Tagline | *"Turning regulated complexity into engineering excellence — one org, one standard, one team at a time."* |
| Sub-tagline | GLOBAL DIGITAL TRANSFORMATION LEADER · IBM → EXETER → AMAZON → PHILIPS |
| Bio | Global Digital Transformation Leader... IEC 62304, ISO 13485, ISO 14971, FDA guidances, INCOSE/EARS... $3M+ savings... 7,000+ engineers |
| Photo | `viz/public/photo.jpg` — professional headshot, navy blazer |
| Logo | `viz/public/logo.jpg` — दत्ta011ya logotype, CSS-inverted white on dark nav |

### KPI tiles (clickable, shining on hover)

| Tile | Value | Navigates to |
|------|-------|-------------|
| Career savings delivered | $3M+ | Impact tab |
| Industry depth | 20 yrs | Timeline tab |
| Engineers reached | 7,000+ | Voices tab |
| Recognitions & quotes | 220+ | Knowledge Graph tab |

### All 8 tabs

| Tab | Component | Data source |
|-----|-----------|-------------|
| Overview | `Hero.tsx` | Static + `impact.json` |
| Professional Identity | `Constellation.tsx` | `constellation.json` |
| Career Arc | `CareerArc.tsx` | `career_arc.json` |
| Impact | `ImpactWall.tsx` | `impact.json` (8 cards) |
| Timeline | `Timeline.tsx` | `timeline.json` (4 eras, 23 milestones) |
| Voices | `Voices.tsx` | `voices.json` (220 quotes) |
| Talks & Givebacks | `TalksGivebacks.tsx` | `talks.json` (43 entries) |
| Knowledge Graph | `KnowledgeGraph.tsx` | `graph.json` (5 sub-views) |

---

## Next Steps

1. **Phase 7: Cloud Deployment** — deploy FastAPI backend + viz frontend; see `plan.md`
2. **Optional** — `graph.json` is 1MB static import; `React.lazy` + dynamic `import()` would improve initial bundle size

---

## Blockers

None.

---

## Key Context

- Dev server: `cd viz && npm run dev` → `http://localhost:5173`
- All data is static JSON in `viz/src/data/` — no API server needed
- Pre-existing TS errors in `CareerArc.tsx` and `Constellation.tsx` are untouched
- Era colors (consistent across all components): IBM=#3987e5 / Exeter=#d95926 / Amazon=#199e70 / Philips=#c98500
- `photo.jpg` and `logo.jpg` are both in `viz/public/` and served as static assets by Vite

# Handover

**Last Updated:** 2026-08-03T03:20:00Z
**Session:** Hero polish — photo, logo, title rebrand, scroll fix

---

## Last Completed Action

Polished the Hero/Overview tab with five changes:
1. **Photo** — profile photo placed in right column of two-column hero layout (loaded from Google Sites URL; add `viz/public/photo.jpg` if offline access needed)
2. **Logo** — "दत्ta011ya" logotype placed in nav, replacing plain text brand; stored at `viz/public/logo.jpg`
3. **Title rebrand** — removed all "principal engineer" references; now reads "Global Digital Transformation Leader leveraging data, AI & Software Craftsmanship principles to transform medical device software"
4. **Stats** — replaced "Service uptime / 99.999%" with "Knowledge artifacts / 913" (service uptime was context-less to an outsider)
5. **Scroll arrow** — wired as a `<button>` that `scrollIntoView` to the Career Highlights below-fold section

---

## Current State

| Aspect | Status |
|--------|--------|
| Phase | 7 — Cloud Deployment (only remaining) |
| Viz tabs | **8 live** at `http://localhost:5173` |
| Build | Clean (`npm run build ✓`) |
| Git | Committed and pushed to main |

### Hero layout

- Two-column: text + KPI tiles left, photo right
- Below-fold section (revealed by ↓ scroll button): 4 career highlight cards — Medical Device / AI Pioneer / Org Transformer / Full Human
- Photo: loaded from Google Sites URL; falls back to "DV" initials placeholder if URL fails
- Logo: `viz/public/logo.jpg` — inverted white on dark nav

### Photo note

The Google Sites image URL is session-authenticated — it will work when the browser is logged in to Google, but may show the initials placeholder in a cold browser session. To guarantee it always shows:
1. Save your photo as `viz/public/photo.jpg`
2. Change `PHOTO_URL` in `Hero.tsx` to `'/photo.jpg'`

---

## Next Steps

1. **Phase 7: Cloud Deployment** — deploy FastAPI backend + viz frontend
2. **Photo permanence** — add `viz/public/photo.jpg` and update `PHOTO_URL` in `Hero.tsx`
3. **Optional** — graph.json is 1MB static import; consider `React.lazy` + `import()` for production

---

## Blockers

None.

---

## Key Context

- Dev server: `cd viz && npm run dev` → `http://localhost:5173`
- All data is static JSON in `viz/src/data/` — no API server needed
- Era colors: IBM=#3987e5 / Exeter=#d95926 / Amazon=#199e70 / Philips=#c98500
- Logo is a JPEG with black background — `filter: invert(1)` applied in CSS makes it white on dark nav

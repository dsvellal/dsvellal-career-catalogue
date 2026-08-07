# Handover

**Last Updated:** 2026-08-06T23:00:00Z
**Session:** Resume collection ingestion (7 PDFs + 1 DOCX)

---

## Last Completed Action

Ingested 8 resume/career files from `/Downloads/Career/Resume/`:
- 6 PDF resume versions (2012, 2020, 2021, 2022, 2023, 2025, 2026) — each as individual evidence file
- 1 DOCX Amazon Work Examples document — structured LP-format work examples
- 1 thematic summary (career progression arc across all versions)

Updated INDEX.md (root + year-specific), updated README.md total count (1,154 → 1,162).

---

## Current State

| Aspect | Status |
|--------|--------|
| Phase | Data architecture enhancement (DESIGN COMPLETE, IMPLEMENTATION PENDING) |
| Knowledge graph | 3,471 nodes, 17,190 edges, 25,767 chunks (in DuckDB/ChromaDB) |
| Evidence files (total) | 1,162 files in data/evidence/ |
| Evidence markdown | 877 markdown files |
| Evidence images | 236 files |
| Evidence certificates | 14 files |
| Evidence sessions | 20 files |
| Evidence snapshots | 4 files |
| Batch JSON | 32 files in data/ (ingestion source data) |
| Enrich JSON | 11 files in data/ (enrichment outputs) |
| Viz tabs | 8 live at http://localhost:5174 |
| Timeline | 6 eras, 353 items, 43 with evidence links (12%) |
| Tests | 227 pass, 2 skipped |
| Build | TypeScript clean |
| Exeter evidence | 98 artifacts (2013: 17, 2014: 54, 2015: 34, 2017: 2) |
| Amazon evidence | 53 artifacts (2016: 13, 2017: 28, 2018: 17) — includes Work Examples doc |
| Resume collection | 8 artifacts (2012, 2020, 2021, 2022, 2023, 2025, 2026 + Amazon Work Examples) |
| Git | Uncommitted changes (resume ingestion) |

---

## In-Progress Work

### Re-Ingestion with Enhanced Schema (NOT YET STARTED)

The user wants to re-ingest Amazon, Exeter, and IBM content by **enhancing existing evidence files in-place** with YAML frontmatter. This remains pending.

---

## Next Steps

### Step 0: Continue ingesting remaining files from /Downloads/Career/

Check if there are other subdirectories in `/Downloads/Career/` not yet ingested.

### Step 1: Update `evidence_index.py` to parse YAML frontmatter

The DuckDB index builder needs YAML frontmatter support (see Decision 028-031).

### Step 2: Enhance existing evidence files in-place

Prepend YAML frontmatter to all existing evidence markdown files.

### Step 3: Rebuild DuckDB index

Run `twin index-evidence` after enhancement.

---

## Blockers

None.

---

## Key Context

### Architecture Decisions (current)

| Decision | Choice |
|----------|--------|
| 028: Storage layer | Markdown-first, DuckDB as derived index |
| 029: Frontmatter schema | Flat + comprehensive (18 fields) |
| 030: Recurring artifacts | Same format, `recurring: true` + `period: YYYY-MM` |
| 031: Re-ingestion strategy | Enhance in-place (prepend frontmatter, body unchanged) |

### Resume Collection Key Insight

Datta maintains **two parallel resume formats**:
1. **Impact format** (2023, 2025): Modern two-column, $3M+ headline, domain-specific skills — for external positioning
2. **Comprehensive format** (2021, 2022, 2026): Traditional layout, full detail — for internal/immigration processes

Career arc: Java dev (IBM) → worldwide component lead → org transformer (Philips India) → global Principal (Philips NA)

### Key conventions preserved

- File numbering: sequential within year (`<NNN>-<slug>.md`)
- Slugs: kebab-case from subject, truncated
- "Role at time" uses actual title at that period
- Claude performs all classification (no external API)
- Every artifact gets an evidence file
- Evidence files are git-tracked
- Internal URLs get HTML/PDF snapshots; external URLs referenced only

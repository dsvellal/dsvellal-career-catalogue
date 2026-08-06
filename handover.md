# Handover

**Last Updated:** 2026-08-06T00:30:00Z
**Session:** Data architecture enhancement — YAML frontmatter schema design

---

## Last Completed Action

Designed and documented the enhanced data architecture for the master dataset. Four architecture decisions made via structured interview (Decisions 028-031). No code changes yet — design phase only.

---

## Current State

| Aspect | Status |
|--------|--------|
| Phase | Data architecture enhancement (DESIGN COMPLETE, IMPLEMENTATION PENDING) |
| Knowledge graph | 3,471 nodes, 17,190 edges, 25,767 chunks |
| Evidence index | 562 files indexed in DuckDB (349 Philips India, 213 Philips USA) |
| Evidence files | 600+ markdown files in data/evidence/ (NO frontmatter yet) |
| Viz tabs | 8 live at http://localhost:5174 |
| Timeline | 6 eras, 353 items, 43 with evidence links (12%) |
| Tests | 227 pass, 2 skipped |
| Build | TypeScript clean |
| Git | Uncommitted changes (decisions.md, prompts.md, handover.md) |

---

## In-Progress Work

### Re-Ingestion with Enhanced Schema (NOT YET STARTED)

The user wants to re-ingest Amazon, Exeter, and IBM content by **enhancing existing evidence files in-place** with YAML frontmatter. This is the immediate next action.

---

## Next Steps

### Step 1: Update `evidence_index.py` to parse YAML frontmatter

The DuckDB index builder (`src/twin/ingestion/evidence_index.py`) currently parses evidence files using regex on the markdown body. It needs to:
1. Check for YAML frontmatter (between `---` markers) first
2. If present, use frontmatter values directly (fast path)
3. If absent, fall back to current regex parsing (backward compat)
4. Add new columns to evidence_index table: `organization`, `tags`, `sentiment`, `impact_type`, `recurring`, `period`

### Step 2: Enhance existing evidence files in-place

For each file in `data/evidence/<year>/individual/*.md`:
1. Read the file
2. Extract/infer all 18 frontmatter fields from the body content
3. Prepend YAML frontmatter block
4. Write back (body unchanged)

Priority order:
- Amazon files (in `data/evidence/` — check what exists)
- Exeter files
- IBM files
- Then all Philips files (2018-2026)

### Step 3: Rebuild DuckDB index

Run `twin index-evidence` after enhancement to verify all frontmatter parses correctly.

### Step 4: Begin new content ingestion

User will provide new Amazon/Exeter/IBM content for re-ingestion with the enhanced schema.

---

## Blockers

None.

---

## Key Context

### Architecture Decisions (this session)

| Decision | Choice |
|----------|--------|
| 028: Storage layer | Markdown-first, DuckDB as derived index |
| 029: Frontmatter schema | Flat + comprehensive (18 fields) |
| 030: Recurring artifacts | Same format, `recurring: true` + `period: YYYY-MM` |
| 031: Re-ingestion strategy | Enhance in-place (prepend frontmatter, body unchanged) |

### YAML Frontmatter Schema (canonical)

```yaml
---
title: <string>
date: <ISO date or original date string>
year: <int>
era: <Amazon | Exeter | IBM | Philips India | Philips USA | Independent>
organization: <Philips | Amazon | Exeter | IBM | Independent>
category: <string>
source_type: <email | calendar | image | pdf | presentation | spreadsheet | document | social_post | github | certificate>
channel: <email_archive | outlook_calendar | viva_engage | linkedin | github | internal_screenshot | ...>
involvement: <author | direct_recipient | cc_mentioned | participant | mentioned_by_name | part_of_distribution>
role: <role title at time>
people: [list of names]
skills: [list of skills demonstrated/exercised]
programs: [list of programs referenced]
tags: [flexible multi-label tags]
nps: <float or null>
sentiment: <positive | neutral | negative>
impact_type: <award | recognition | delivery | operational | leadership | technical | mentoring | null>
recurring: <true | false>
period: <YYYY-MM, only if recurring>
---
```

### Existing infrastructure

- `src/twin/ingestion/evidence_index.py` — current regex-based parser (needs frontmatter-first upgrade)
- `src/twin/db.py` — DuckDB schema (evidence_index table needs new columns)
- `data/evidence/INDEX.md` — master index of all evidence files
- `twin index-evidence` CLI command — rebuilds evidence_index table
- Evidence files exist for: 2018 (3), 2019 (155+19), 2020 (67+64), 2021 (3+19), 2022 (7), 2023 (15), 2024 (5), 2025 (56), 2026 (98)
- Amazon/Exeter/IBM files were ingested via `scripts/ingest_career.py` into the knowledge graph (nodes/edges/chunks) but evidence markdown files for those eras may be minimal or absent — verify what exists in `data/evidence/`

### Key conventions preserved

- File numbering: sequential within year (`<NNN>-<slug>.md`)
- Slugs: kebab-case from subject, truncated
- "Role at time" uses actual title at that period
- Claude performs all classification (no external API)
- Every artifact gets an evidence file
- Evidence files are git-tracked

### Era/role mapping for frontmatter inference

| Era | Years | Organization | Role(s) |
|-----|-------|--------------|---------|
| IBM | 2007-2014 | IBM | Application Developer, Senior Application Developer |
| Exeter | 2014-2017 | Exeter (Edifecs) | Software Engineer, Technical Lead |
| Amazon | 2017-2018 | Amazon | SDE-2 |
| Philips India | 2018-2021 | Philips | SWCoE Competency Specialist |
| Philips USA | 2021-present | Philips | Software Competency Lead, Innovation Engineering |
| Independent | various | Independent | Community contributor, Yoga instructor |

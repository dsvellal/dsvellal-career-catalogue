# Feature Wishlist

Features to build, ordered by priority. Pick the top one, interview to flush out requirements, then implement.

---

## 1. OKF Conversion — Dual Knowledge Representation

**Priority:** High
**Added:** 2026-08-02
**Decisions:** #029, #030, #031, #032, #033
**Reference Spec:** `/Users/dsvellal/Code/knowledge-catalog/okf/SPEC.md` (OKF v0.2)

### Summary

Convert the in-memory knowledge graph (DuckDB nodes/edges) into Open Knowledge Format — a bundle of markdown files with YAML frontmatter that is human-readable, git-versioned, and agent-consumable. Maintain dual existence: OKF files are the source of truth for knowledge; DuckDB/ChromaDB/NetworkX are derived in-memory views rebuilt via incremental sync.

### Design Decisions (Already Made)

| Decision | Choice |
|----------|--------|
| Ownership split | OKF owns knowledge (nodes, edges). DuckDB owns operational data (artifacts, logs, chunks, sync state, voice profiles). |
| Bundle structure | One subdirectory per node type: `projects/`, `skills/`, `people/`, `organizations/`, `achievements/`, `outcomes/`, `time-ranges/` |
| Edge representation | Conventional body section headings map to edge types (e.g., `# Skills` = `USED_SKILL` edges) |
| Sync mechanism | Incremental content-hash diffing. `twin sync` command + sync-on-startup. |
| Ingestion promotion | Auto-write OKF files with `status: draft`. User flips to `stable` after review. |

### Section-to-Edge Mapping

| Section Heading | Edge Type | Direction |
|----------------|-----------|-----------|
| `# Skills` | `USED_SKILL` | concept -> skill |
| `# Outcomes` | `PRODUCED` | concept -> outcome |
| `# Recognition` | `RECOGNIZED_FOR` | achievement -> concept |
| `# Organization` | `AT_ORG` | concept -> org |
| `# Time Period` | `DURING` | concept -> time_range |
| `# Collaborators` | `COLLABORATED_WITH` | concept -> person |
| `# Projects` | `WORKED_ON` | person -> project |
| `# Parent Skills` | `SKILL_PARENT` | skill -> skill |

### Implementation Scope (To Be Flushed Out)

1. **Export**: `twin export-okf` — dump current DuckDB nodes/edges into OKF bundle
2. **Sync**: `twin sync` — read OKF bundle, diff against DuckDB, update in-memory stores
3. **Promote**: Modify ingestion pipeline to auto-write `.md` files with `status: draft`
4. **Index generation**: Auto-generate `index.md` per directory
5. **CLI integration**: Wire into existing `twin` CLI
6. **OKF frontmatter**: Map node properties to OKF frontmatter fields (`type`, `title`, `description`, `tags`, `generated`, `status`, `sources`)
7. **Concept ID**: Use slugified node name as filename (e.g., `projects/bar-raiser-program.md`)

### Open Questions (For Implementation Interview)

- Where should the OKF bundle directory live? (`./knowledge/`, `./okf/`, configurable?)
- Should `time-ranges/` be individual files or just date metadata on other concepts?
- How to handle the ~500 skill nodes — one file each, or group low-signal skills?
- Should the initial export require manual review before becoming source of truth?
- What OKF frontmatter extensions (beyond spec) are needed for twin-specific data?

---

## 2. Skill Deduplication (Semantic)

**Priority:** Medium
**Added:** 2026-08-02

### Summary

Semantic duplicates exist in the skill graph (e.g., "Leadership" vs "Technical Leadership" vs "Influence-based Leadership" are intentionally separate, but "Active Listening" vs "Listening" could merge). Need a dedup pass that presents candidates for merge and lets user decide.

### Open Questions

- Threshold for similarity (embedding distance? LLM judgment?)
- Interactive merge or batch with confirmation?
- Should merged skills retain both original names as aliases?

---

## 3. Voice Profile Regeneration

**Priority:** Medium
**Added:** 2026-08-02

### Summary

Regenerate the voice profile from the now much richer corpus (16 LinkedIn recommendations + 167 enriched artifacts + workshop letters). Current profile is a placeholder default. Should analyze writing samples, recommendation language, and self-descriptions to build an authentic voice.

---

## 4. Phase 7: Cloud Deployment

**Priority:** Medium
**Added:** 2026-08-02

### Summary

Deploy the twin publicly. Decisions 008 and 015 define the hybrid model (local source of truth, cloud read-only projection) with domain-agnostic configuration. Includes curated publish snapshot, API hosting, and portfolio serving.

---

## 5. Interactive Knowledge Graph Visualization

**Priority:** Low
**Added:** 2026-08-02

### Summary

The OKF bundle in knowledge-catalog has a Cytoscape.js-powered `viz.html` generator. Adapt or build similar for the twin's knowledge graph — force-directed graph, node filtering by type, detail panel, search. Could reuse the viewer from knowledge-catalog or build a custom one integrated with the FastAPI server.

---

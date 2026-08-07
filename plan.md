# Execution Plan

**Project:** dsvellal-personal-knowledge-context
**Last Updated:** 2026-08-07
**Current Phase:** 7 (Cloud Deployment); Phase 5d complete

---

## Phase 0: Design (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 0.1 | Define system intent and scope | Done | See prompts.md #001 |
| 0.2 | Architecture decisions | Done | See decisions.md #001-#015 |
| 0.3 | Write architecture document | Done | architecture.md |
| 0.4 | Write high-level design | Done | high-level-design.md |
| 0.5 | Write low-level design (schemas, APIs) | Done | low-level-design.md |
| 0.6 | Define user flows | Done | user-flows.md (7 flows) |
| 0.7 | Define test cases | Done | test-cases.md (6 sections + integration + edge cases) |
| 0.8 | Setup project scaffolding | Done | pyproject.toml, src/twin/, CLI working |

---

## Phase 1: Core Ingestion + Graph (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1.1 | Project scaffolding (pyproject.toml, deps) | Done | Completed in Phase 0 |
| 1.2 | DuckDB schema initialization | Done | src/twin/db.py — 9 tables, 10 indexes |
| 1.3 | CLI framework (Typer) | Done | `twin init`, `twin status` wired to real DB |
| 1.4 | Format extractors (PDF, DOCX, email, markdown, JSON) | Done | src/twin/ingestion/extractors.py |
| 1.5 | Gemini classification integration | Done | google-genai SDK, src/twin/ingestion/classifier.py |
| 1.6 | Entity resolution logic | Done | src/twin/ingestion/resolver.py — idempotent insert (try/except) |
| 1.7 | Graph edge creation | Done | src/twin/ingestion/edges.py |
| 1.8 | `twin ingest <file>` command | Done | Full pipeline: extract→dedup→classify→resolve→link→log |
| 1.9 | `twin status` command | Done | Node type breakdown + last ingestion time |
| 1.10 | Dedup via SHA-256 content hash | Done | In pipeline, skips duplicates |
| 1.11 | Ingestion audit logging | Done | ingestion_log table, per-ingest records |

---

## Phase 2: Retrieval + Synthesis (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 2.1 | ChromaDB integration (embedding storage) | Done | src/twin/retrieval/embeddings.py |
| 2.2 | Chunking strategy implementation | Done | src/twin/retrieval/chunker.py — section-aware, sentence-boundary split |
| 2.3 | Vector search | Done | search_vectors() in embeddings.py |
| 2.4 | Full-text search (DuckDB FTS) | Done | src/twin/retrieval/fts.py — BM25 scoring |
| 2.5 | Graph traversal (NetworkX from DuckDB) | Done | src/twin/retrieval/graph.py — neighbors, paths, subgraphs |
| 2.6 | Reciprocal Rank Fusion | Done | src/twin/retrieval/fusion.py — weighted RRF |
| 2.7 | Voice profile creation | Done | src/twin/synthesis/voice.py — versioned profiles |
| 2.8 | Context assembly pipeline | Done | src/twin/synthesis/context.py — hybrid search + fusion + prompt |
| 2.9 | `POST /api/ask` endpoint | Done | src/twin/api/app.py + /api/health |
| 2.10 | LLM provider abstraction (Gemini + Ollama) | Done | src/twin/providers/llm.py — router with fallback |

---

## Phase 3: Generators (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 3.1 | Resume generator (markdown output) | Done | src/twin/generators/resume.py |
| 3.2 | ATS PDF renderer (WeasyPrint) | Done | src/twin/generators/pdf_ats.py (needs pango system dep) |
| 3.3 | Designed PDF renderer (Typst) | Done | src/twin/generators/pdf_typst.py |
| 3.4 | Cover letter generator | Done | src/twin/generators/cover_letter.py |
| 3.5 | Weekly/monthly summary generator | Done | src/twin/generators/summary.py |
| 3.6 | `POST /api/generate` endpoint | Done | Resume + cover letter via /api/generate |
| 3.7 | `POST /api/summary` endpoint | Done | /api/summary with time range |

---

## Phase 6: Cloud Sync (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 6.1 | Google Drive API OAuth2 setup | Done | src/twin/sync/gdrive.py (class-based, credentials path) |
| 6.2 | Change detection (changes.list + page tokens) | Done | Page token storage + detect_changes() |
| 6.3 | Watch folder (fswatch/watchdog) | Done | src/twin/sync/watcher.py — ~/twin-inbox |
| 6.4 | Sync state table management | Done | gdrive_sync table with upsert logic |
| 6.5 | Handle: new, modified, deleted, moved | Done | process_change() dispatches by action |

---

## Phase 4: Chat Interface (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 4.1 | Frontend framework selection | Done | FastAPI + vanilla HTML/JS/CSS (no Node.js needed) |
| 4.2 | Chat UI with streaming | Done | templates/chat.html with fetch API |
| 4.3 | Citation display | Done | Citations shown below each answer |
| 4.4 | Conversation context management | Done | Client-side context array |

---

## Phase 5: Portfolio Site (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 5.1 | Static site generation from graph snapshot | Done | src/twin/generators/portfolio.py |
| 5.2 | Sections: About, Projects, Skills, Timeline, Recognition | Done | Stats + Skills + Projects + Achievements |
| 5.3 | Graph/skill visualization | Done | Stats bar with counts (viz deferred to Phase 7) |
| 5.4 | Publish workflow | Done | `twin publish` CLI command |

---

## Phase 5b: Data Representation Architecture (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 5b.1 | Split Philips timeline into India/USA eras | Done | 2021-12-05 split date, 6 eras total |
| 5b.2 | Three-level drill-down (Timeline) | Done | Summary → Rich Summary → Full Artifact |
| 5b.3 | Three-level drill-down (Impact Wall) | Done | Same pattern as Timeline |
| 5b.4 | Three-level drill-down (Voices) | Done | Same pattern as Timeline |
| 5b.5 | Evidence index in DuckDB | Done | 562 files indexed, src/twin/ingestion/evidence_index.py |
| 5b.6 | `twin publish --viz-only` command | Done | Generates split, evidence-enriched JSON |
| 5b.7 | `twin index-evidence` CLI command | Done | Rebuilds evidence_index table |
| 5b.8 | Legacy evidence file serving (symlink) | Superseded | Symlink remains local but is inert because the current Vite build disables `publicDir` |
| 5b.9 | Reverse chronological order everywhere | Done | Philips USA → India → Amazon → Exeter → IBM |
| 5b.10 | Evidence matching in publish | Done | 43/353 items linked (12%), DuckDB-backed |

---

## Phase 5c: Journey Analysis and Visualization (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 5c.1 | Export all canonical relationship stores | Done | Deterministic private DuckDB, ChromaDB, and exact NetworkX snapshot under `data/exports/relationships/` |
| 5c.2 | Validate export completeness and failure safety | Done | Manifest/hashes/consistency report; 4 focused tests passing |
| 5c.3 | Document the longitudinal journey model | Done | `data/journey-analysis.md` records the thesis, view rationale, evidence picture, and confidence boundaries |
| 5c.4 | Build evidence-tiered public journey dataset | Done | Deterministic builder, exact schema, privacy/provenance validation, and 5 focused tests |
| 5c.5 | Implement exact eight-view Journey Atlas | Done | UI, data binding, hash navigation, responsive shell, production build, and TypeScript check complete |
| 5c.6 | Enforce raw-evidence/public-build boundary | Done | `publicDir` disabled; local filenames replaced by opaque source IDs; 1.2 MB build contains only HTML, CSS, JS, logo, and photo—no evidence directory |
| 5c.7 | Browser, responsive, accessibility, build, and type verification | Done | Eight desktop/mobile deep links, keyboard navigation, zero page overflow at 390 px, zero automated WCAG A/AA violations, production build, and static typing verified |

---

## Phase 5d: Executive Portfolio Observatory (Complete)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 5d.1 | Audit public metrics, attribution, privacy, and data quality | Done | Corrected mixed session/survey populations, heterogeneous rating interpretation, service-growth wording, XITE/Sutra attribution, and other claim boundaries |
| 5d.2 | Identify defensible longitudinal and cross-domain relationships | Done | Development-to-later-observation, assessed-to-observed strengths, quality-enables-speed, title-independent leadership, capability multiplication, topic-frontier shift, demand-led influence, and service continuity |
| 5d.3 | Define claim/source/support/method/conflict schema | Done | Provenance, support directness, and claim state are orthogonal; stable human-readable IDs and privacy-aware access states |
| 5d.4 | Build deterministic `portfolio.json` public projection | Done | 9 routes, 55 claims, 82 supports, 36 sources, 18 methods, 11 explicit relationships, 30 caveats, and 8 conflicts |
| 5d.5 | Replace Journey Atlas with nine-route executive observatory | Done | Three progressive depth levels, global evidence lens, claim/source/method routes, Data Room, documentary media, and responsive interactions |
| 5d.6 | Correct committed professional-session aggregate evidence | Done | Separates 88 post-event datasets / 1,050 rows from two pre-event surveys / 133 rows; unsupported global satisfaction and JSCPD causality claims removed |
| 5d.7 | Run deterministic data, privacy, frontend, accessibility, and browser verification | Done | All 7 repository gates pass; 269 tests pass / 2 skip; 9 routes pass at 1440 and 390 px; zero automated WCAG A/AA violations and no browser errors |
| 5d.8 | Complete documentation and publish directly to `main` | Done | System/product/design/user-flow/test/setup/handover records reconciled; direct-main publication with no new pull request per owner instruction |

---

## Phase 7: Cloud Deployment

| # | Task | Status | Notes |
|---|------|--------|-------|
| 7.1 | Deployment target selection | Pending | |
| 7.2 | Published snapshot format | Done | `twin publish --viz-only` generates static JSON |
| 7.3 | Cloud API (read-only) | Pending | View-specific endpoints planned |
| 7.4 | Domain configuration | Pending | |
| 7.5 | Split graph JSON per sub-view | Pending | 5 files instead of monolithic graph.json |
| 7.6 | LLM query planner for /api/ask | Pending | Multi-mode retrieval orchestration |

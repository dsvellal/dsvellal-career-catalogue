# Architecture

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.2.0
**Status:** Active

---

## 1. System Overview

A personal knowledge system that ingests all professional artifacts (documents, achievements, code, recognition), builds a multi-dimensional knowledge graph, and serves multiple consumers through a unified API. The system's primary persona is a first-person digital twin that can explain Datta's work, generate tailored resumes, produce weekly summaries, and power a dynamic portfolio.

---

## 2. Component Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           CONSUMERS                                      │
│                                                                          │
│  ┌──────────┐  ┌──────────────┐  ┌────────────┐  ┌──────────────────┐  │
│  │ Chat Twin │  │ Portfolio    │  │ Generators │  │ Weekly Summary   │  │
│  │ (Web UI)  │  │ (Public Site)│  │ (Resume,   │  │ (Scheduled)      │  │
│  │           │  │              │  │  Cover Ltr)│  │                  │  │
│  └─────┬─────┘  └──────┬──────┘  └─────┬──────┘  └────────┬─────────┘  │
│        │                │               │                   │            │
└────────┼────────────────┼───────────────┼───────────────────┼────────────┘
         │                │               │                   │
         ▼                ▼               ▼                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         API LAYER                                         │
│                                                                          │
│  /api/ask          - conversational Q&A (first-person synthesis)         │
│  /api/search       - hybrid retrieval across knowledge graph             │
│  /api/generate     - structured output generation (resume, cover, etc.)  │
│  /api/summary      - time-bounded work summaries                         │
│  /api/graph        - graph traversal and exploration                     │
│  /api/ingest       - document/artifact ingestion                         │
│  /api/publish      - curate and push to public deployment                │
│  /api/health       - system status                                       │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────┐
│                      SYNTHESIS LAYER                                      │
│                                                                          │
│  ┌────────────────┐  ┌────────────────┐  ┌─────────────────────────┐   │
│  │ Voice Engine   │  │ Context        │  │ Output Formatters       │   │
│  │                │  │ Assembly       │  │                         │   │
│  │ - Voice profile│  │ - Query decomp │  │ - Resume (ATS/design)  │   │
│  │ - Tone control │  │ - Chunk select │  │ - Cover letter         │   │
│  │ - 1st person   │  │ - Relevance    │  │ - Summary (weekly/     │   │
│  │   enforcement  │  │   scoring      │  │   monthly)             │   │
│  │ - Confidence   │  │ - Citation     │  │ - Portfolio section    │   │
│  │   calibration  │  │   tracking     │  │ - LinkedIn post        │   │
│  └────────────────┘  └────────────────┘  └─────────────────────────┘   │
│                                                                          │
│  LLM Provider Abstraction:                                               │
│    Primary: Gemini (gemini-2.5-pro / gemini-2.5-flash)                  │
│    Fallback: Ollama (gemma4 / llama3.3)                                  │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────┐
│                      RETRIEVAL LAYER                                      │
│                                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  │
│  │ Vector      │  │ Graph       │  │ Full-Text   │  │ Temporal     │  │
│  │ Search      │  │ Traversal   │  │ Search      │  │ Filter       │  │
│  │             │  │             │  │             │  │              │  │
│  │ Semantic    │  │ Relationship│  │ Keyword     │  │ Date-range   │  │
│  │ similarity  │  │ walks (BFS/ │  │ matching    │  │ queries,     │  │
│  │ over        │  │ DFS), path  │  │ with FTS5   │  │ recency      │  │
│  │ embeddings  │  │ finding     │  │ ranking     │  │ weighting    │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └──────────────┘  │
│                                                                          │
│  Fusion: Reciprocal Rank Fusion (RRF) with configurable weights          │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────┐
│                      KNOWLEDGE GRAPH                                      │
│                                                                          │
│  Store: DuckDB (structured) + ChromaDB (vectors)                         │
│  Graph Engine: NetworkX (in-memory, built from DuckDB edges)             │
│                                                                          │
│  Node Types:         Edge Types:                                         │
│  ─────────────       ───────────────────────                             │
│  Project             WORKED_ON (person->project)                         │
│  Skill               USED_SKILL (project->skill)                         │
│  Person              PRODUCED (project->outcome)                         │
│  Organization        RECOGNIZED_FOR (achievement->project|skill)         │
│  Achievement         AT_ORG (project->org, person->org)                  │
│  Outcome             DURING (any->time_range)                            │
│  TimeRange           COLLABORATED_WITH (person->person)                  │
│  Artifact            EVIDENCED_BY (any->artifact)                        │
│                      SUPERVISED_BY (person->person)                       │
│                      SKILL_PARENT (skill->skill)                         │
│                      ORG_PARENT (org->org)                                │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────┐
│                      INGESTION LAYER                                      │
│                                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ CLI      │  │ Web      │  │ Watch Folder │  │ Google Drive Sync │  │
│  │ (twin    │  │ Upload   │  │ ~/twin-inbox │  │ Drive API v3      │  │
│  │  ingest) │  │          │  │              │  │ changes.list      │  │
│  └──────────┘  └──────────┘  └──────────────┘  └───────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Canonical relationship export lane

The operational stores remain canonical: DuckDB owns structured records, ChromaDB owns vector records, and NetworkX is rebuilt in memory from DuckDB nodes and edges. `scripts/export_relationships.py` creates a portable, deterministic private snapshot without introducing another source of truth.

```
data/knowledge.duckdb ──┐
                        ├──> validated staging ──> atomic install
data/chroma/ ─────────┘      data/exports/relationships/
          │                         ├─ DuckDB tables + relationship projections
          └─ NetworkX rebuild      ├─ Chroma documents, metadata, vectors
                                    ├─ exact node-link graph + metrics
                                    └─ manifest, hashes, inventories, checks
```

The exporter opens DuckDB read-only, verifies Chroma IDs before and after streaming, compares overlapping Chroma documents and metadata with DuckDB chunks, validates graph counts and endpoints, hashes every output, and replaces the previous export only after validation. `viz/data/knowledge.duckdb` and `viz/data/chroma` are noncanonical and excluded.

The generated export is private: it contains raw artifact text, people, metadata, and full embedding vectors. It is versioned only in the access-controlled private repository by explicit owner decision and never crosses the public deployment boundary. Oversized vector streams are deterministically split below 48 MiB per file so the complete snapshot remains Git-hostable without Git LFS.

---

### Curated Journey Atlas projection

The public portfolio does not query the private export. `scripts/build_journey_data.py` is a deliberate editorial boundary that selects reviewed, public-safe evidence into one versioned static contract:

```
reviewed evidence files + longitudinal analysis
                    │
                    ▼
        validate schema, provenance,
        chronology, metrics, and privacy
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
viz/src/data/journey.json   data/journey-analysis.md
          │
          ▼
eight-view React Journey Atlas ──> Vite static build
```

The builder validates private references containing local evidence paths, then removes those paths at the publication boundary. Public references contain only an opaque `source_id`, `tier`, `supports`, and optional source year. Evidence tiers distinguish corroborated, documented, self-reported, and derived material; `caveat_labels` resolve through a shared glossary. The browser receives neither artifact bodies nor local filenames.

The Vite build sets `publicDir: false`. Only explicitly imported presentation assets can enter the module graph, which prevents the local raw-evidence symlink from being copied into `dist`.

---

## 3. Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Backend | Python 3.12+ / FastAPI | Proven in Chitta, strong async, good LLM library support |
| Database | DuckDB | Embedded analytical DB, larger-than-memory, columnar, FTS extension, better for graph-shaped queries than SQLite |
| Vectors | ChromaDB (embedded) | Proven in Chitta, works well for <1M vectors |
| Graph | NetworkX (in-memory from DuckDB) | Fast traversal, no infra dependency. Rebuild from edges table at startup. |
| LLM (classification) | Claude (interactive session) | Superior classification quality, no external API needed (Decision 028) |
| LLM (synthesis) | Google Gemini API (2.5-pro / 2.5-flash) | User's existing subscription, strong synthesis |
| LLM (fallback) | Ollama (gemma4, BGE-m3) | Offline capability, free |
| Frontend | React + TypeScript + Vite + D3 | SPA with hash-addressable view navigation and static JSON data |
| Journey Data | `scripts/build_journey_data.py` → `viz/src/data/journey.json` | Curated, evidence-tiered, public-safe projection for exactly eight views |
| Legacy Viz Data | `twin publish` static JSON generation | Pre-shaped files retained for archived view components |
| Relationship Export | Deterministic JSON/JSONL/YAML + SHA-256 manifest | Portable inspection of DuckDB, ChromaDB, and the exact runtime NetworkX projection without changing canonical stores |
| Evidence Index | DuckDB evidence_index table | 562 indexed Markdown records; coverage gap is reported rather than hidden |
| CLI | Python (Typer) | Consistent with backend, rich terminal output, modern Click alternative |
| Drive Sync | Google Drive API v3 | Official API, change tracking with page tokens |
| Deployment (cloud) | Domain-agnostic, configurable | Vercel/Cloud Run or equivalent. Decided at Phase 7. |
| PDF (ATS) | WeasyPrint | Simple, standards-compliant HTML-to-PDF |
| PDF (Designed) | Typst | Modern typesetting, programmable templates, beautiful output |

---

## 4. Deployment Model

### Hybrid: Local + Cloud

- **Local:** Development, ingestion, private data management. All source material stays on local machine.
- **Cloud:** Read-only public projection. Portfolio site, chat twin, API for consumers. Deployed data is a curated subset.
- **Private export:** `data/exports/relationships/` stays local and is never consumed by the public build.

### Data Flow

```
Local Machine (source of truth)
    │
    │ curated builder + explicit publish action
    ▼
Validated public projection (no raw evidence)
    │
    ▼
Cloud (read-only static build)
    │
    │ serves
    ▼
Public consumers (portfolio, chat, API)
```

### Privacy Boundaries

| Level | Description | Example | Handling |
|-------|-------------|---------|----------|
| Public | Safe to publish | Project names, public skills, cert names | Published to cloud |
| Internal | Professional but private | Performance review content, salary info | Local only, never published |
| Confidential | Sensitive | NDA-covered project details, personal emails | Local only, redacted in outputs |

The private relationship export is always Local regardless of individual source-row visibility. The Journey Atlas receives only reviewed aggregates and attributed public recommendations after validation.

---

## 5. Phase Plan

| Phase | Scope | Deliverable | Dependencies |
|-------|-------|-------------|--------------|
| 0 | Design | Design docs, decisions.md, prompts.md | None |
| 1 | Core Ingestion + Graph | DuckDB schema, extractors, CLI (`twin ingest`, `twin status`), Gemini classification | Gemini API key |
| 2 | Retrieval + Synthesis | Vector store, hybrid search, Ask endpoint, voice profile | Phase 1 |
| 3 | Generators | Resume, cover letter, summary generators via API | Phase 2 |
| 4 | Chat Interface | Web UI for conversational twin | Phase 2 |
| 5 | Portfolio Site | Public-facing dynamic portfolio, static generation | Phase 3 |
| 6 | Cloud Sync | Google Drive monitoring, watch folder | Phase 1 |
| 7 | Cloud Deployment | Published snapshot to Vercel + Cloud Run | Phase 5 |

**Recommended execution order:** 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 7

Rationale: Move Cloud Sync (6) earlier because low-friction ingestion determines whether the system stays populated. The twin is useless if it has no knowledge.

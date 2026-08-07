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

### Schema-v3 Executive Portfolio Observatory projection (current)

The publication compiler now emits two orthogonal layers in the same privacy-safe contract:

```text
55 canonical claims + supports + sources + methods + relationships
                              │
                    exact ownership validation
                              │
          ┌───────────────────┴───────────────────┐
          ▼                                       ▼
23 curated story blocks                    4 audit-only claims
51 claims owned exactly once               retained outside the public story
          │
          ▼
8 primary routes → Inspect Claim → source/method records
```

`story_blocks` is a presentation layer rather than a second factual store. Each block references one primary claim and any folded supporting claims, adds concise executive `title`, `meaning`, and `proof` copy, and may reference one allowlisted documentary source. Build validation requires every featured claim to have exactly one owner and limits narrative pages to no more than four blocks. The generic Impact route was removed because it had no unique ownership boundary; the route parser maps legacy `impact` hashes to Innovation & Value.

The React shell renders the same portrait-bearing page hero on all eight routes. Public pages do not render a global evidence lens, Gaps mode, confidence badges, claim counts, or support counts. `DetailPages.tsx` resolves a story block's primary and folded claims into four compact disclosures: meaning, deduplicated evidence, derivation method, and scope/evidence context. The data is still complete—confidence, caveats, conflicts, attribution, and relationship reasoning remain part of the audit model—but presentation concerns no longer dominate the executive reading path.

The Data Room searches the 23 curated conclusions and a 34-source publication closure instead of rendering all 55 raw claims by default. That closure includes direct claim supports, documentary sources, inputs to the 16 story-linked methods, and sources used to reconcile story claims; ten story-linked longitudinal relationships remain available behind collapsed native disclosures. The same publication sets guard direct claim/source/method hashes: audit-only records remain in the deterministic contract but reveal only a generic evidence invitation in the public UI. The `#/impact` compatibility redirect and stable story-linked record hashes preserve traceability.

### Claim-centric Executive Portfolio Observatory projection (archived schema v2)

The public portfolio does not query the private export. `scripts/build_portfolio_data.py` is the publication compiler: it reads reviewed evidence and committed aggregates, computes bounded metrics, records editorial relationships, validates every reference, and emits one public-safe contract.

```
reviewed evidence + committed aggregates + editorial relationship definitions
                              │
                              ▼
                  deterministic claim compiler
       ┌──────────────────────┼──────────────────────┐
       │ validate IDs/support │ compute methods      │ privacy allowlist
       │ attribution/conflicts│ formulas/rounding    │ excerpts/media/URLs
       └──────────────────────┴──────────────────────┘
                              │
                              ▼
                 viz/src/data/portfolio.json
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
        nine executive-question       Level 3 resolvers
        Level 1/2 experiences         claim/source/method
                  └───────────┬───────────┘
                              ▼
                      Vite static build
```

The contract is claim-centric. Source provenance (`corroborated`, `documented`, or `self_reported`), support directness, and claim state (`observed`, `calculated`, or `interpreted`) are independent fields. Calculations and interpretations resolve to versioned method records with explicit inputs, formula or rubric, inclusion/exclusion and deduplication rules, rounding, result, and caveats. Conflicts remain visible instead of being silently overwritten.

Sources use stable editorial IDs rather than path hashes. A public source capsule contains reviewed metadata, a verbatim or explicitly labelled editorial-summary excerpt, held-artifact SHA-256 plus its scope/note, access state, and optional allowlisted public URL. Exact verbatim excerpts are validated against the canonical source. A public link remains independently openable, while the checksum is explicitly scoped to the held publication artifact rather than the mutable live page. Private originals remain locally verifiable and are described as withheld; local paths, internal URLs, participant identity, and raw artifact bodies are excluded from the browser contract.

Longitudinal links are an explicit editorial dataset, not a rendering of graph co-occurrence. Every relationship names its endpoint claims, relation type, reasoning or method, confidence, and limitation. The prior `journey.json`/eight-view builder remains a legacy compatibility artifact but is not the active portfolio input.

The Vite build sets `publicDir: false`. Only explicitly imported presentation assets and individually reviewed documentary evidence can enter the module graph, which prevents the local raw-evidence symlink from being copied into `dist`.

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
| Portfolio Data | `scripts/build_portfolio_data.py` → `viz/src/data/portfolio.json` | Schema-v3 story layer over claim-centric, method-bearing, privacy-safe evidence for eight routes and stable detail records |
| Legacy Journey Data | `scripts/build_journey_data.py` → `viz/src/data/journey.json` | Superseded eight-view compatibility projection; retained for regression history |
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

The private relationship export is always Local regardless of individual source-row visibility. The Executive Portfolio Observatory receives only reviewed claims, bounded aggregates, approved excerpts, and allowlisted documentary media after validation.

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
| 5d | Executive Portfolio Observatory | Claim/source/method compiler, eight-route story UI, Data Room, folded traceability, explicit longitudinal analysis | Phase 5 + reviewed evidence |
| 6 | Cloud Sync | Google Drive monitoring, watch folder | Phase 1 |
| 7 | Cloud Deployment | Published snapshot to Vercel + Cloud Run | Phase 5 |

**Recommended execution order:** 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 7

Rationale: Move Cloud Sync (6) earlier because low-friction ingestion determines whether the system stays populated. The twin is useless if it has no knowledge.

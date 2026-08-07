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
| Frontend | React + TypeScript + Vite + D3 | SPA with tab navigation, static JSON data |
| Viz Data | `twin publish` static JSON generation | Pre-shaped per view, evidence-enriched |
| Evidence Index | DuckDB evidence_index table | 982 files (790 markdown, 160 images, 14 certs, 20 sessions) |
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

### Data Flow

```
Local Machine (source of truth)
    │
    │ explicit publish action
    ▼
Cloud (read-only projection)
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

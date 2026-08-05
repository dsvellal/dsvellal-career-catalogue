# Decisions Log

Structured record of all architectural and design decisions for the Personal Knowledge Context system.
Format designed to be machine-readable for AI reconstruction and improvement.

---

## Decision 001: Greenfield in Peer Directory

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Project Structure

**Question:** What is the relationship between the existing Chitta PLM knowledge system and this new personal knowledge system?

**Decision:** Create a new greenfield project at `../dsvellal-personal-knowledge-context`, peer to the Chitta repo. Build from scratch with purpose-designed architecture.

**Rationale:** The personal knowledge system has fundamentally different data semantics (identity, career, achievements) vs. engineering documents (FMEAs, requirements). A clean slate allows designing the graph schema, ingestion pipeline, and synthesis layer specifically for personal context without carrying PLM-specific assumptions.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Pivot Chitta codebase | Loses the working PLM system. The PLM system itself is portfolio evidence. |
| Fork as sibling | Inherits PLM-specific schema assumptions (chunks, documents, FTS5 indexing tuned for technical docs). Would spend more time stripping than building. |
| Multi-tenant namespace | Excessive complexity. Two fundamentally different domains sharing infrastructure creates coupling that constrains both. |

---

## Decision 002: Input Scope

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Data Model

**Question:** What types of source material will the system ingest?

**Decision:** Three input categories for initial scope:
1. Documents & text (PDFs, Word docs, emails, Slack messages, meeting notes, project plans, design docs)
2. Structured achievements (certificates, awards, appreciation emails, performance reviews, recommendations)
3. Code & projects (Git repos as evidence: commit history, PRs, architecture decisions, what was built)

Media/recordings excluded from initial scope.

**Rationale:** These three categories cover the full career narrative without requiring transcription infrastructure. Media can be added later as an extension.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Include media/recordings | Requires transcription pipeline (Whisper or cloud ASR). Adds significant complexity. Can be added as Phase N+1 without architectural changes. |
| Text-only | Misses the structured achievement data that's highest-signal for resume generation. |

---

## Decision 003: Full-Stack Output Architecture

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Architecture

**Question:** What's the primary output/interface for the digital twin?

**Decision:** Full stack: knowledge API at the core, with multiple consumers:
- Conversational chat interface (the "digital twin")
- Dynamic portfolio website
- Resume/cover letter generators
- Weekly summary generator

**Rationale:** All consumers need the same underlying retrieval and synthesis capabilities. API-first design means each consumer is a thin client over the same knowledge core.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Chat-only | Misses the resume/portfolio use cases which are arguably the highest immediate value. |
| Portfolio-only | Static output. The conversational aspect is what makes it a "digital twin" vs. a fancy website. |
| API-only (headless) | Correct architecturally but delays demonstrable value. Need at least one consumer to validate the API design. |

---

## Decision 004: Cloud-First LLM Strategy

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Infrastructure

**Question:** Where should LLM inference run?

**Decision:** Gemini Cloud as primary (user has existing subscription). Ollama as local fallback. Provider-agnostic abstraction layer to allow switching.

**Rationale:** Gemini provides superior synthesis quality for nuanced personal narrative compared to local models. Existing subscription eliminates cost concern. Local fallback ensures system works offline and for development.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Local only (Ollama) | Quality ceiling too low for first-person voice synthesis. Gemma4/Llama can retrieve but struggle with nuanced career narrative. |
| Cloud only (no fallback) | Breaks offline dev workflow. Network dependency for every operation is fragile. |
| Claude/GPT instead of Gemini | User has Gemini subscription. No reason to add another provider cost. Can be added to the abstraction layer later if needed. |

---

## Decision 005: First-Person Voice Identity

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** UX / Identity

**Question:** How should the digital twin represent the user?

**Decision:** First-person voice. The system speaks as Datta: "I built...", "My experience in...", "I led the..."

**Rationale:** More engaging and personal than third-person. Creates the "digital twin" feeling rather than a "well-informed recruiter" feeling. Requires a voice profile document to calibrate tone, vocabulary, and self-presentation style.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Third-person factual | Professional but impersonal. Reads like a Wikipedia entry. Doesn't create the twin effect. |
| Adaptive (context-dependent) | Adds complexity in prompting. First-person can still be formal in formal contexts without switching to third-person. |

**Implementation Notes:**
- Requires a "voice profile" document: writing samples, tone preferences, how user describes their own work
- System prompt must enforce first-person consistently
- Generated outputs (resumes) may use third-person as a format convention (this is output formatting, not identity)

---

## Decision 006: Multi-Dimensional Graph Schema

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Data Model

**Question:** What relationships matter most between artifacts in the knowledge graph?

**Decision:** Multi-dimensional graph with all first-class node types:
- Time (anchoring events to periods)
- Skills (competency mapping)
- Projects (work units)
- People (collaborators)
- Organizations (employers, clients)
- Outcomes (measurable results)
- Achievements (recognition, certifications)
- Artifacts (source evidence files)

Typed edges connect across dimensions.

**Rationale:** Each consumer needs different traversal patterns. Resume generator needs skill-centric. Portfolio needs project-centric. Weekly summary needs time-centric. Multi-dimensional enables all without restructuring.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Timeline-centric | Great for summaries but weak for skill-matching against job descriptions. |
| Skill-centric | Great for resumes but loses narrative flow for portfolio/chat. |
| Project-centric | Good for storytelling but makes cross-project skill aggregation expensive. |

---

## Decision 007: Omni-Channel Ingestion with Cloud Sync

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Infrastructure

**Question:** How should new material enter the system?

**Decision:** Four ingestion channels:
1. CLI tool (scripted/bulk operations)
2. Web upload UI (manual with context)
3. Watch folder (passive local collection)
4. Google Drive sync (cloud monitoring for add/modify/delete)

**Rationale:** The system is only valuable if kept fed. Multiple channels reduce friction for different contexts. Google Drive sync is particularly important because it enables "set and forget" ingestion from an existing workflow.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| CLI only | High friction for non-technical moments. You won't always be in a terminal when you receive an appreciation email. |
| Web only | Misses bulk import and scripted workflows. |
| Watch folder only | No cloud sync means you have to manually move files from cloud to local. Breaks "set and forget." |

**Implementation Notes:**
- Google Drive sync uses the Drive API with change detection (changes.list endpoint with page tokens)
- Must handle: new files, modified files, deleted files, moved files
- Deduplication by content hash (same as Chitta's approach)

---

## Decision 008: Hybrid Deployment Model

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Infrastructure

**Question:** Where should the digital twin live when deployed?

**Decision:** Hybrid model:
- **Local:** Development, ingestion, private data management. All source material stays on local machine.
- **Cloud:** Read-only public projection. Portfolio site, chat twin, API for consumers. Deployed data is a curated subset.

**Rationale:** Privacy-first for ingestion (performance reviews, salary info, private emails should never leave the machine). Public-facing for the twin's purpose (being discoverable, shareable). The "curated subset" concept means you control exactly what the public twin knows.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Local only | Defeats the "digital twin that represents me to others" purpose. Can't share a localhost URL. |
| Full cloud | Privacy risk. Not all source material should be uploadable to a server. |
| Serverless | Vendor coupling. Cold starts hurt chat UX. State management is complex. |

**Implementation Notes:**
- Local system is the "source of truth" with full graph
- Cloud deployment receives a "published" snapshot: curated nodes, embeddings, and a synthesized voice profile
- Publishing is an explicit action, not automatic

---

## Decision 009: Design-Doc-First Methodology

**Date:** 2026-07-27
**Phase:** Discovery
**Category:** Process

**Question:** How should the system be built?

**Decision:** Write a full design document first (data model, API contracts, component diagram, worked example), then build against the spec.

**Rationale:** Multi-consumer architecture with a graph schema needs upfront alignment. Building without a spec risks rework when the second consumer reveals schema assumptions from the first. The design doc itself becomes part of the project's AI-readable context.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| MVP in a weekend | Would optimize for one consumer (probably chat) and bake in assumptions that break the others. |
| Incremental delivery | Good for execution phase, but premature without knowing the full shape. Incremental delivery is the execution strategy once the design is agreed. |
| Solid foundation | Indistinguishable from "design doc first" in practice. The distinction was about timeline, not approach. |

---

## Decision 010: Structured AI-Readable Documentation

**Date:** 2026-07-27
**Phase:** Design
**Category:** Process / Meta

**Question:** How should project documentation be formatted?

**Decision:** All project documents use structured formats (markdown with consistent headings, tables, frontmatter-style metadata) designed to be parsed by AI systems for reconstruction or improvement.

Key files:
- `DESIGN.md` - Architecture specification
- `decisions.md` - This file. Decision log with alternatives.
- `prompts.md` - Complete prompt history with timestamps and outcomes.

**Rationale:** The project itself is about AI-readable knowledge. Its own documentation should demonstrate the principle. Any AI given these files should be able to understand the full context, continue the work, or suggest improvements.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Informal notes | Not reconstructable. Loses the "why" behind decisions. |
| Jira/Linear tickets | External system dependency. Not colocated with code. Not AI-readable without API access. |
| Wiki | Same external dependency issue. Also tends toward prose over structure. |

---

## Decision 011: DuckDB as Primary Store

**Date:** 2026-07-27
**Phase:** Design (Open Questions)
**Category:** Infrastructure

**Question:** If the graph exceeds NetworkX's in-memory comfort zone, what's the migration plan?

**Decision:** Use DuckDB from the start instead of SQLite. NetworkX remains for in-memory graph traversal, backed by DuckDB edges table.

**Rationale:** DuckDB handles analytical queries over graph-shaped data well (multi-hop joins, aggregations over node/edge properties). Supports larger-than-memory datasets. Embedded (no server process). Columnar storage is efficient for the read-heavy, write-light pattern of a personal knowledge graph. Better JSON support than SQLite for the properties columns.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Stay with NetworkX + SQLite, cap git detail | Works for now but creates a scaling cliff. SQLite's row-oriented storage is inefficient for the analytical queries this system needs (aggregating skills across projects, time-range filtering). |
| Plan for Neo4j migration | Adds operational complexity (server process, JVM). Overkill for personal-scale data. Migration is never free even with compatible schemas. |
| SQLite with careful indexing | Would work but DuckDB gives better analytical query performance with less effort. No downside at this scale. |

---

## Decision 012: Dual-Layer Confidential Handling

**Date:** 2026-07-27
**Phase:** Design (Open Questions)
**Category:** Privacy / Data Model

**Question:** How should the system handle NDA-covered or confidential projects?

**Decision:** Store full detail locally with visibility=confidential. At publish time, auto-generate anonymized versions via Gemini. Human review required before deployment. An `anonymization_map` table tracks the mapping.

**Rationale:** The digital twin should have no gaps in its narrative. A public twin that says "I can't talk about 3 years of my career" undermines credibility. Anonymized versions preserve the skill/impact story while protecting confidential details.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Anonymized versions only | Loses the full-detail local context. When generating outputs privately (e.g., a resume for a specific company that's not under NDA), you want the real details. |
| Exclude from publish entirely | Creates visible gaps. "Why is there nothing between 2022-2025?" raises questions. |
| Manual anonymization | Doesn't scale. Tedious. Inconsistent. AI-assisted with human review is the right balance. |

---

## Decision 013: English Only

**Date:** 2026-07-27
**Phase:** Design (Open Questions)
**Category:** Scope

**Question:** Are there artifacts in languages other than English?

**Decision:** English only. No multilingual support needed.

**Rationale:** All professional artifacts are in English. Simplifies embedding model choice (no need for multilingual models like BGE-m3) and synthesis prompts. Can always add multilingual later without breaking changes.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Multilingual input | Adds complexity with no current need. |
| Multilingual input and output | Significantly increases synthesis prompt complexity and testing surface. |

---

## Decision 014: Triple Output Format for Resumes

**Date:** 2026-07-27
**Phase:** Design (Open Questions)
**Category:** Output / UX

**Question:** What format should generated resumes be in?

**Decision:** All three outputs from a single generation:
1. Markdown source (editable, version-controllable)
2. ATS-friendly PDF (WeasyPrint, simple HTML template, standard fonts)
3. Designed PDF (Typst, polished typography and layout)

**Rationale:** Different submission channels need different formats. ATS systems need parseable plain formats. Human reviewers appreciate design. Markdown gives you an editable master to tweak. One generation pass, three renderers.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Markdown only | Shifts conversion burden to user. Friction leads to skipping. |
| ATS PDF only | Looks generic. Doesn't stand out for direct applications. |
| Designed PDF only | Gets mangled by ATS parsers. Many large companies require ATS-friendly format. |

---

## Decision 015: Domain-Agnostic Deployment

**Date:** 2026-07-27
**Phase:** Design (Open Questions)
**Category:** Infrastructure

**Question:** Should the system assume a specific domain for the public-facing twin?

**Decision:** No domain assumption baked in. Fully configurable at deployment time via environment variables.

**Rationale:** Domain registration is a separate concern from system architecture. Making it configurable means no rework when a domain is eventually chosen, and allows testing with platform subdomains (*.vercel.app, *.fly.dev) before committing to a purchase.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Register domain now | Premature. System needs to be working before it needs to be public. |
| Platform subdomain | Fine for initial deployment but shouldn't be an assumption either. |

---

## Decision 016: uv for Dependency Management

**Date:** 2026-07-27
**Phase:** Design (Project Setup)
**Category:** Tooling

**Question:** Which Python dependency/environment management tool should the project use?

**Decision:** Use `uv` (by Astral) for virtual environment creation and package installation. Standard `pyproject.toml` with hatchling build backend.

**Rationale:** Fast, modern, lockfile-capable. Replaces pip + venv with a single tool. Deterministic builds. Significantly faster install times than pip.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| pip + venv (traditional) | Works but slower installs, no built-in lockfile, separate tools for env + install. |
| poetry | Mature but heavier. Custom lock format. Slower resolution. |

---

## Decision 017: Scaffolding with Stub CLI

**Date:** 2026-07-27
**Phase:** Design (Project Setup)
**Category:** Architecture

**Question:** Should Phase 0 include a working CLI or just documentation?

**Decision:** Create full project scaffolding with a working CLI (`twin --help`, `twin status`). All Phase 1+ commands exist as stubs that print "not yet implemented."

**Rationale:** Proves the CLI framework end-to-end before Phase 1 implementation begins. Developers can immediately run `twin status` and see output. Test infrastructure is validated. Reduces Phase 1 scope to "fill in the stubs."

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Docs only, scaffold later | Delays validation of the build chain. Phase 1 would start with both scaffolding and feature work. |
| Full CLI with init | Scope creep. Phase 0 is design; Phase 1 is implementation. Stub commands are the clean boundary. |

---

## Decision 018: Migrate to google-genai SDK

**Date:** 2026-07-27
**Phase:** Implementation (Phase 1)
**Category:** Dependencies

**Question:** Which Google AI SDK to use for Gemini classification?

**Decision:** Use `google-genai` (v2.14+) instead of `google-generativeai` (v0.8.x). The old package emits a FutureWarning stating all support has ended.

**Rationale:** Building on an officially deprecated, unsupported package creates unnecessary tech debt. The new SDK has a cleaner API (Client pattern vs global configure).

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Keep google-generativeai | Deprecated, no future bug fixes. Would need migration eventually anyway. |
| Use raw REST API | More boilerplate, no structured output helpers, lose SDK benefits. |

---

## Decision 019: No EVIDENCED_BY Edges

**Date:** 2026-07-27
**Phase:** Implementation (Phase 1)
**Category:** Data Model

**Question:** How to link artifacts to nodes as evidence?

**Decision:** Do not create EVIDENCED_BY edges. Instead, use `source_artifact_id` field on all edges to track provenance. The `edges` table has FK constraints requiring both `source_id` and `target_id` to reference `nodes(id)`, and artifacts are not nodes.

**Rationale:** The FK constraint is valuable for graph integrity. Rather than remove it or promote artifacts to nodes (conflating two concepts), we use the existing `source_artifact_id` field which already provides the artifact→edge provenance link.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Remove FK constraint on edges | Weakens data integrity. Graph queries would need to handle dangling references. |
| Insert artifacts as nodes | Conflates document storage with knowledge graph entities. Inflates node count. |
| Add separate evidence table | Over-engineering. source_artifact_id already provides the link. |

---

## Decision 020: ChromaDB Default Embeddings

**Date:** 2026-07-27
**Phase:** Implementation (Phase 2)
**Category:** Retrieval

**Question:** Which embedding model to use for vector search?

**Decision:** Use ChromaDB's built-in default embedding function (all-MiniLM-L6-v2) rather than calling Gemini's text-embedding-004 API.

**Rationale:** Keeps vector search fully local and free — no API call per chunk. all-MiniLM-L6-v2 is good enough for personal-scale retrieval. Can upgrade to Gemini embeddings later when API budget allows or when retrieval quality needs improvement.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Gemini text-embedding-004 | Adds API cost per chunk. Slower ingest. Overkill for personal-scale data. |
| BGE-m3 via Ollama | Requires Ollama running. Adds deployment dependency. |

---

## Decision 021: Paragraph-First Chunking Strategy

**Date:** 2026-07-27
**Phase:** Implementation (Phase 2)
**Category:** Retrieval

**Question:** How to chunk documents for embedding?

**Decision:** Section-aware chunking: split by markdown headers first, then by paragraph boundaries within each section. Long single paragraphs are further split at sentence boundaries. Configurable chunk_size (default 512 chars) with overlap (default 64 chars).

**Rationale:** Preserves semantic coherence — a paragraph about one topic stays together. Section awareness means chunks carry their heading context. Sentence-boundary splitting for long paragraphs avoids mid-word cuts.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Fixed-size character splitting | Breaks mid-sentence/word. Loses semantic coherence. |
| Recursive character splitter (LangChain-style) | Over-engineered for this use case. Adds dependency. |
| LLM-based semantic chunking | Too expensive per document. Adds API cost and latency to ingestion. |

---

## Decision 025: Explicit Organization Extraction in Classifier

**Date:** 2026-07-28
**Phase:** Implementation (Gap Fix)
**Category:** Ingestion

**Question:** How should the pipeline resolve organizations for AT_ORG edges — add to the Gemini classification prompt, or infer from other fields?

**Decision:** Add an explicit `organizations` field to the classification prompt, asking Gemini to extract organizations with their role (employer, issuer, client, partner, education).

**Rationale:** Explicit extraction is more reliable than inference. Organizations appear in many forms (letterhead, "Offered by", email domains) that aren't easily parsed from other fields. The marginal token cost per classification call is negligible.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Infer from people roles / metadata | Unreliable for certificates, awards, standalone org mentions. Would miss "IBM" on a cert that names no people. |
| Post-processing NER | Adds another dependency. Gemini already does NER implicitly — just needs the schema. |

---

## Decision 026: Media Storage in Local Managed Directory with Cloud URL Fallback

**Date:** 2026-07-28
**Phase:** Implementation (Media Recall)
**Category:** Storage

**Question:** How to store original binary files (images, PDFs) so they can be recalled on-demand?

**Decision:** Copy source files into `data/media/<content_hash>.<ext>` at ingest time. Also store an optional `media_url` for cloud-hosted originals (e.g., Google Photos links). Serve via `GET /api/media/<artifact_id>` — returns the local file if available, otherwise redirects to the cloud URL.

**Rationale:** Content-addressable storage via the SHA-256 hash we already compute. Self-contained, works offline, dedup built-in. Cloud URL fallback means images that live in Google Photos don't need to be downloaded at ingest time.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| DuckDB BLOB column | Bloats the database. Makes backups heavier. Slower for large files. |
| git-annex style CAS (hash[0:2]/hash[2:4]/...) | Over-engineered for expected volume (<10K files). Adds path resolution complexity. |
| Cloud-only (no local copy) | Breaks offline access. Depends on external service availability. |

---

## Decision 026: Filename-Based Classification for Batch Ingestion

**Date:** 2026-07-28
**Phase:** Data Population
**Category:** Ingestion Strategy

**Question:** How to classify 679 career files for bulk ingestion without exhausting LLM API quota?

**Decision:** Use rule-based classification derived from filename + folder context. The Career folder has extremely descriptive naming conventions (dates, topics, people, organizations encoded in filenames). Use `ingest_pre_classified()` to bypass the Gemini classifier.

**Rationale:** The filenames in ~/Downloads/Career are semantically rich — e.g., `DoTheRightThing_CodingRevampForLongterm_September13th2013.pdf` contains the appreciation category, topic, and date. This makes LLM classification unnecessary for bulk ingestion. Saves API quota, runs instantly, and produces accurate classifications.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Gemini API for each file | 679 API calls, rate limiting, cost, and slower. Content-based classification adds marginal value when filenames already encode the semantics. |
| Claude interactive (read each file) | 679 files × read + classify would exceed session context. Not practical for bulk. |
| Hybrid (filename + Gemini for ambiguous) | Over-engineered. Filename classification achieved 0 errors on 679 files. |

---

## Decision 027: Skip Sensitive Files Entirely

**Date:** 2026-07-28
**Phase:** Data Population
**Category:** Privacy

**Question:** How to handle compensation, salary, tax, and financial documents during ingestion?

**Decision:** Skip sensitive files entirely (not ingested at all). Applied regex patterns to 40+ sensitive filename indicators. 42 files skipped.

**Rationale:** User preference. These files don't add meaningful career knowledge (the employment relationship is already captured via offer letters, experience letters, and appreciation emails). Financial details have no value in a digital twin's knowledge graph.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Ingest with visibility='internal' | User explicitly chose "skip sensitive files" |
| Selective ingestion (keep employment dates) | Dates already captured from non-sensitive docs |

---

## Decision 028: Claude as Sole AI (Classifier, Resolver, Enricher)

**Date:** 2026-07-31
**Phase:** Data Population / Operations
**Category:** LLM Provider

**Question:** Which LLM should power classification, entity resolution, and enrichment going forward?

**Decision:** Claude (the interactive session) replaces Gemini and Ollama as the sole AI. During ingestion sessions, Claude reads content directly and generates structured classifications inline — no external API calls needed.

**Rationale:** Claude already demonstrated superior classification quality on Fernando's recommendation (Gemini returned `"type": "other"` with zero entities; Claude extracted 7 claims, 6 skills, 1 person, 1 org). The interactive model has full project context, understands the graph schema, and can make nuanced judgments about claims and skill extraction. No API key management, no rate limits, no cost per call.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Keep Gemini as classifier | Produced poor results on recommendations (type: "other", 0 entities). Requires API key and costs per call. |
| Ollama local fallback | Not installed, adds operational complexity for marginal benefit |
| Multi-model ensemble | Over-engineered for a personal project. One high-quality model is sufficient. |

---

## Decision 029: OKF as Human-Readable Knowledge Layer (Split Ownership)

**Date:** 2026-08-02
**Phase:** Design (Knowledge Representation)
**Category:** Architecture / Data Model

**Question:** How should the knowledge graph be stored in a human-readable, portable format alongside the existing in-memory stores?

**Decision:** Adopt Open Knowledge Format (OKF v0.2) with split ownership:
- **OKF owns knowledge** — nodes (Projects, Skills, People, Organizations, Achievements, Outcomes, TimeRanges) and their relationships live as `.md` files with YAML frontmatter in a bundle directory.
- **DuckDB owns operational data** — artifacts (raw text, content hashes), ingestion logs, chunks, gdrive sync state, voice profiles remain in DuckDB only.
- The in-memory stores (DuckDB nodes/edges, ChromaDB vectors, NetworkX graph) become **derived views** rebuilt from the OKF bundle via incremental sync.

**Rationale:** Not everything in DuckDB should be human-readable files. Raw text blobs, content hashes, sync tokens, and ingestion logs are operational plumbing — they'd be noise as markdown. But the knowledge graph (who you are, what you did, what skills you used, what you achieved) maps perfectly to OKF concepts. Each node becomes a concept file; edges become markdown links between concepts. The OKF bundle becomes the human-browsable, git-versioned, agent-readable knowledge base.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| OKF is source of truth for everything | Operational data (chunks, logs, sync tokens) has no business being markdown files. Would be noise. |
| DuckDB stays as source of truth, OKF is export only | OKF becomes read-only — hand edits get overwritten. Loses the editability benefit. |
| Bidirectional sync on both sides | Complex conflict resolution. Two writable truths is a recipe for data loss. |

---

## Decision 030: One Directory Per Node Type (Bundle Structure)

**Date:** 2026-08-02
**Phase:** Design (Knowledge Representation)
**Category:** Data Model / File Layout

**Question:** How should node types map to the OKF bundle directory structure?

**Decision:** One subdirectory per node type: `projects/`, `skills/`, `people/`, `organizations/`, `achievements/`, `outcomes/`, `time-ranges/`. Each node becomes one `.md` file in its type directory.

**Rationale:** Simplest, most faithful to OKF philosophy — every concept is its own addressable file. One node = one file makes the bidirectional sync with DuckDB trivial. `index.md` files can provide project-centric or timeline views as navigational aids without changing the underlying structure.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Project-centric hierarchy | Shared nodes (skills, orgs) need canonical location decisions. Complicated. |
| Career-period hierarchy (by org/time) | Skills span multiple periods. Cross-cutting queries require full traversal. |
| Hybrid: type dirs but projects contain inline sub-concepts | Outcomes/achievements aren't individually addressable. Harder to query programmatically. |

---

## Decision 031: Conventional Body Sections for Edge Types

**Date:** 2026-08-02
**Phase:** Design (Knowledge Representation)
**Category:** Data Model / Relationships

**Question:** How should typed, weighted edges be represented in OKF markdown files?

**Decision:** Use conventional body section headings per edge type. A project file has `# Skills`, `# Outcomes`, `# Recognition` sections. Links under each heading are implicitly that edge type (e.g., links under `# Skills` = `USED_SKILL` edges).

**Rationale:** Human-readable AND machine-parseable via heading convention. No frontmatter bloat, no NLP guessing. The rebuild script deterministically maps `# Skills` → `USED_SKILL`, `# Outcomes` → `PRODUCED`, etc. Weight and confidence can be derived during build (e.g., from `verified` status, or explicit annotations like `(primary)` next to a link).

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Plain markdown links, edge type inferred from prose | Requires NLP or heuristics. Non-deterministic rebuild. |
| Structured `relationships` field in frontmatter | Verbose, duplicates body links, not how OKF intends relationships to work. |
| Hybrid: frontmatter for high-signal, body for narrative | Two places to look for edges. Complicated boundary definition. |

**Section-to-Edge Mapping:**

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

---

## Decision 032: Incremental Hash-Based Sync

**Date:** 2026-08-02
**Phase:** Design (Knowledge Representation)
**Category:** Infrastructure / Sync

**Question:** When and how should OKF files be hydrated into the in-memory stores?

**Decision:** Incremental content-hash sync on startup + explicit `twin sync` command. On first run, full build. On subsequent runs, compare each OKF file's hash against what's stored in DuckDB — only re-process changed/new/deleted files. ChromaDB re-embeds only changed chunks.

**Rationale:** Fast after first build. No always-on watcher complexity. Clear command (`twin sync`) for after manual edits. Composes with existing ingestion — `twin ingest` writes to DuckDB then "promotes" to OKF; `twin sync` goes the other direction (OKF -> in-memory).

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Full rebuild on every startup | Slow for large bundles. Re-embeds everything unnecessarily. |
| File watcher (continuous hot reload) | Always-on process. Race conditions. Over-engineered for this use case. |
| Explicit `twin build` only | Manual step, easy to forget. Queries return stale results. |

---

## Decision 034: Idempotent Node Insertion via try/except

**Date:** 2026-08-02
**Phase:** Implementation (Ingestion Bug Fix)
**Category:** Data Model / Reliability

**Question:** What should happen when `_resolve_node` tries to INSERT a node that already exists (due to concurrent ingestion or a prior partial run)?

**Decision:** Wrap the INSERT in a try/except. On failure, fall back to SELECT by `id` and return the existing node as `is_new=False`.

**Rationale:** Without this, any duplicate node_id collision throws an unhandled exception and aborts ingestion mid-run. The race can happen during parallel ingestion scripts or when a script crashes after partial inserts and is re-run. The SELECT-first check (by `type + LOWER(name)`) can miss cases where the same logical entity is inserted under a slightly different name, yet generate the same deterministic id hash. The try/except makes the insert idempotent at the ID level.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| INSERT OR IGNORE | Silently swallows all errors including genuine schema violations. Hard to debug. |
| Unique constraint + SELECT-then-INSERT transaction | DuckDB embedded doesn't have the same transaction isolation as Postgres. The race is still possible within a single connection under certain usage patterns. |
| Pre-check by id before insert | Still racey; two checks still lose to a concurrent insert between check and write. |

---

## Decision 033: Auto-Promote with status=draft

**Date:** 2026-08-02
**Phase:** Design (Knowledge Representation)
**Category:** Ingestion / Lifecycle

**Question:** How does the ingestion pipeline "promote" knowledge to OKF?

**Decision:** Ingestion writes OKF files immediately with `status: draft` in frontmatter. User reviews and flips to `status: stable` when satisfied. `twin sync` treats both equally for in-memory build, but generators and public outputs only use `stable` concepts.

**Rationale:** Leverages OKF's built-in lifecycle field exactly as designed. Everything lands in the bundle immediately (human-readable, git-trackable from day one). The `status: draft` signal lets generators and public outputs filter to `stable` only. Avoids separate staging mechanism. Single source of truth from moment of ingestion.

**Alternatives Considered:**

| Option | Why It Lost |
|--------|-------------|
| Immediate write-through (always stable) | LLM-classified entities go straight to stable. Bundle fills with unreviewed noise. |
| Staging + explicit `twin promote` | Extra step. Knowledge isn't in OKF until promoted — loses immediate visibility. |
| Confidence-gated auto-promote | Threshold is arbitrary. Important knowledge may be low-confidence initially. |

---

## Decision 020: Evidence Generation Protocol

**Timestamp:** 2026-08-04
**Context:** Need traceable evidence for every ingested artifact, ready for UI demonstration.

**Decision:** Made evidence generation MANDATORY in CLAUDE.md. Every artifact produces: (a) individual evidence markdown, (b) knowledge graph enrichment (nodes, edges, chunks).

**Alternatives:**
1. Store raw text only in DB — rejected (not UI-ready, not traceable)
2. Generate evidence on-demand when UI requests — rejected (too slow, context lost)
3. **Generate at ingestion time and commit to git** — chosen (persistent, traceable, UI-ready)

---

## Decision 021: Remove Gemini Dependency

**Timestamp:** 2026-08-04
**Context:** Classifier required GEMINI_API_KEY which was never set, resulting in empty classifications.

**Decision:** Claude IS the LLM. Local rule-based classifier extracts entities from structured email metadata. No external API needed.

**Alternatives:**
1. Set up Gemini API key — rejected (unnecessary dependency)
2. Use OpenAI — rejected (same problem, external dependency)
3. **Local classifier + Claude enrichment** — chosen (zero dependencies, always works)

---

## Decision 022: URL Handling Protocol

**Timestamp:** 2026-08-05
**Context:** Internal Philips URLs will die when employee leaves. Need to preserve content.

**Decision:** Internal URLs get HTML snapshots saved to data/evidence/snapshots/. External URLs referenced only.

**Alternatives:**
1. Snapshot everything — rejected (external URLs are persistent, wastes space)
2. Reference everything — rejected (internal content will be lost forever)
3. **Internal=snapshot, External=reference** — chosen (preserves what will die, references what won't)

---

## Decision 023: Image Storage for Evidence

**Timestamp:** 2026-08-05
**Context:** Awards, certificates, Viva Engage screenshots need to be stored and demonstrated in UI.

**Decision:** Compress to fit 1024x768 display, save as JPEG (quality 85), store in data/evidence/images/<year>/. Committed to git.

**Alternatives:**
1. Store full resolution — rejected (too large for git, unnecessary)
2. Store only references — rejected (screenshots of internal content will disappear)
3. **Compressed JPEG at display quality** — chosen (good quality, reasonable size, git-friendly)

# Personal Knowledge Context System

A personal knowledge system that ingests professional artifacts (documents, achievements, code, recognition), builds a multi-dimensional knowledge graph, and serves multiple consumers through a unified API.

The system's primary persona is a first-person digital twin that can explain Datta's work, generate tailored resumes, produce weekly summaries, and power a dynamic portfolio.

---

## What It Does

- **Ingests** documents, achievements, code artifacts, and recognition into a knowledge graph
- **Retrieves** via hybrid search (vector, graph, full-text, temporal)
- **Synthesizes** first-person responses using a calibrated voice profile
- **Generates** tailored resumes, cover letters, and summaries from evidence
- **Audits** the complete DuckDB, ChromaDB, and runtime NetworkX relationship layer through a deterministic private export

---

## Consumers

| Consumer | Description |
|----------|-------------|
| Chat Twin | Conversational Q&A about Datta's work (first-person) |
| Portfolio | Dynamic public-facing professional site |
| Resume Generator | JD-tailored resume with gap analysis |
| Weekly Summary | Time-bounded work summaries |

---

## Project Structure

| File | Purpose |
|------|---------|
| `CLAUDE.md` | AI assistant instructions for this project |
| `.gitignore` | Files excluded from git |
| `README.md` | This file |
| `architecture.md` | System architecture and component interactions |
| `high-level-design.md` | Consumer specs, synthesis layer, security model |
| `low-level-design.md` | Data model, API contracts, ingestion pipeline |
| `plan.md` | Execution plan with task tracking |
| `decisions.md` | Decision log with alternatives considered |
| `prompts.md` | Prompt history with timestamps |
| `user-flows.md` | How users derive value from the system |
| `test-cases.md` | Golden tests and integration test specs |
| `SETUP.md` | Local development setup instructions |
| `scripts/export_relationships.py` | Export and validate the canonical private relationship stores |
| `scripts/build_journey_data.py` | Build the curated public Journey Atlas dataset and analysis report |

---

## Tech Stack

- **Backend:** Python 3.12+ / FastAPI
- **Database:** DuckDB (structured) + ChromaDB (vectors)
- **Graph:** NetworkX (in-memory, rebuilt from DuckDB edges)
- **LLM:** Gemini (primary) / Ollama (fallback)
- **CLI:** Typer
- **PDF:** WeasyPrint (ATS) + Typst (designed)

---

## Current Status

**Phases 0-6: Complete.** Full pipeline operational: ingestion, retrieval, synthesis, generators, chat, portfolio, cloud sync.

**Phase 7: Cloud Deployment** — Pending. Static publish (`twin publish --viz-only`) works; cloud endpoints not yet deployed.

**Journey Atlas:** Data builder, eight views, production build, static typing, public-bundle isolation, and interactive desktop/mobile review are complete.

**Data:**
- 1,498 evidence files in `data/evidence/`, including 1,086 Markdown files; 277 Markdown files currently carry YAML frontmatter
- 32 batch ingestion source files + 11 enrichment outputs
- Knowledge graph: 3,471 nodes, 17,190 edges, 25,767 chunks
- Portable private relationship export: all 10 DuckDB tables, full Chroma documents/metadata/embeddings, exact NetworkX node-link graph, hashes, and consistency checks under `data/exports/relationships/`
- Viz app: eight-view Journey Atlas at `viz/` (Executive Portrait, Twenty-Year Journey, Capability Compounder, Outcome Ledger, Trust & Respect, Influence Web, Teaching & Service Ripple, Momentum & Next Horizon)
- Evidence spans 2007-2026 across 6 eras (IBM, Exeter, Amazon, Philips India, Philips USA, Independent)
- Awards & citations: 16 awards, 12 recognitions, 2 USPTO patents (27+ citations), ~20 public references

**Next:** Close embedding and evidence-index coverage gaps, continue applying the YAML frontmatter schema, and complete the reviewed public deployment boundary.

See `plan.md` for full execution plan.

### Build the curated Journey Atlas data

```bash
.venv/bin/python scripts/build_journey_data.py
```

This validates every private evidence path and displayed metric, then replaces local paths with opaque public source IDs before writing the public-safe `viz/src/data/journey.json` and the editorial rationale in `data/journey-analysis.md`. The public dataset contains curated aggregates and attributed recommendations—not raw artifacts, internal filenames, internal links, email addresses, donor identities, account details, or full relationship records.

### Private relationship export

Run the export only on a trusted local machine:

```bash
.venv/bin/python scripts/export_relationships.py
```

The generated `data/exports/relationships/` directory is a complete portable snapshot, not public portfolio data. By explicit owner decision it is versioned only in this access-controlled private repository. Its manifest records hashes and source inventories; its consistency report currently records 4,411 DuckDB chunks without Chroma vectors and 13 soft edge-to-artifact provenance references whose artifacts are absent. Full embedding vectors are emitted in deterministic parts below 48 MiB. Do not deploy, mirror publicly, or share this directory without another deliberate privacy review.

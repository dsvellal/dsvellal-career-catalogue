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
| `scripts/build_portfolio_data.py` | Compile and validate the claim-centric public executive portfolio dataset |
| `scripts/check_public_bundle.py` | Independently reject private paths, identifiers, raw evidence, or unapproved assets in the production bundle |
| `scripts/build_journey_data.py` | Build the superseded eight-view Journey Atlas compatibility dataset |

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

**Executive Portfolio Observatory:** Nine executive-question routes, three progressive evidence levels, global Narrative/Proof/Method/Gaps lenses, claim/source/method records, explicit longitudinal relationships, documentary evidence, and a searchable Data Room are compiled from a deterministic public projection. The previous Journey Atlas remains as regression history, not the active UI.

**Data:**
- 1,498 evidence files in `data/evidence/`, including 1,086 Markdown files; 277 Markdown files currently carry YAML frontmatter
- 32 batch ingestion source files + 11 enrichment outputs
- Knowledge graph: 3,471 nodes, 17,190 edges, 25,767 chunks
- Portable private relationship export: all 10 DuckDB tables, full Chroma documents/metadata/embeddings, exact NetworkX node-link graph, hashes, and consistency checks under `data/exports/relationships/`
- Viz app: nine-route Executive Portfolio Observatory at `viz/` (Brief, Leadership System, Journey, Impact, Trust, Innovation, Learning & Multiplication, Community & Service, Data Room)
- Public evidence contract: 55 claims, 82 support edges, 36 source capsules, 18 methods, 11 explicit relationships, 30 caveats, and 8 retained conflicts across 9 routes
- Evidence spans 2007-2026 across 6 eras (IBM, Exeter, Amazon, Philips India, Philips USA, Independent)
- Professional feedback accounting: 88 post-event/interaction datasets and 1,050 response rows; two pre-event audience surveys and 133 rows are reported separately
- Community learning: 50 recorded deliveries, 3,732 participant instances, and 13 student-feedback forms with 494 response rows; presenter ratings remain separate at 4.58/5 (`n=149`) and 9.12/10 (`n=128`), while 8.87/10 (`n=98`) is recommendation likelihood—not NPS

**Next:** Close embedding and evidence-index coverage gaps, continue applying the YAML frontmatter schema, and complete the reviewed public deployment boundary.

See `plan.md` for full execution plan.

### Build the public Executive Portfolio Observatory data

```bash
.venv/bin/python scripts/build_portfolio_data.py
```

The builder validates stable IDs and references, computes bounded metrics from committed records, attaches claims to supports and versioned methods, checks explicit longitudinal relationships, restricts external URLs to an allowlist, and writes `viz/src/data/portfolio.json`. Verbatim excerpts must occur exactly in their held canonical source. Published SHA-256 values cover that held artifact; for an external public record they explicitly do **not** claim to checksum the live web page. The browser projection contains approved excerpts and scoped source checksums—not local paths, raw artifacts, internal links, participant/donor identities, account details, or the private relationship export.

The current public contract keeps three independent credibility dimensions: source provenance, support directness, and claim state. Calculated or interpreted claims disclose inputs, formula or rubric, inclusion/exclusion and deduplication rules, rounding, caveats, confidence, and conflicts. An interpreted relationship never becomes causal merely because its endpoints occur in sequence.

### Private relationship export

Run the export only on a trusted local machine:

```bash
.venv/bin/python scripts/export_relationships.py
```

The generated `data/exports/relationships/` directory is a complete portable snapshot, not public portfolio data. By explicit owner decision it is versioned only in this access-controlled private repository. Its manifest records hashes and source inventories; its consistency report currently records 4,411 DuckDB chunks without Chroma vectors and 13 soft edge-to-artifact provenance references whose artifacts are absent. Full embedding vectors are emitted in deterministic parts below 48 MiB. Do not deploy, mirror publicly, or share this directory without another deliberate privacy review.

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

**Executive Portfolio Observatory:** Eight impact-led routes present a concise story layer over the full evidence model. Twenty-three curated story blocks each communicate one executive conclusion; 51 claims are owned exactly once by those blocks and four technical/privacy-sensitive claims remain audit-only. Narrative, evidence, method, and scope now live together behind **Inspect claim** instead of competing as global lenses. The previous nine-route observatory and Journey Atlas remain as regression history, not the active UI.

**Data:**
- 1,498 evidence files in `data/evidence/`, including 1,086 Markdown files; 277 Markdown files currently carry YAML frontmatter
- 32 batch ingestion source files + 11 enrichment outputs
- Knowledge graph: 3,471 nodes, 17,190 edges, 25,767 chunks
- Portable private relationship export: all 10 DuckDB tables, full Chroma documents/metadata/embeddings, exact NetworkX node-link graph, hashes, and consistency checks under `data/exports/relationships/`
- Viz app: eight-route Executive Portfolio Observatory at `viz/` (Brief, Leadership, Career Journey, Trust, Innovation & Value, Learning, Community & Service, Data Room); legacy `#/impact` resolves to Innovation & Value
- Public evidence contract: schema v3 with 23 story blocks, exact ownership of 55 claims (51 story-owned and 4 audit-only), 82 support edges, 36 source capsules, 18 methods, 11 explicit relationships, 30 caveats, and 8 retained conflicts
- Evidence spans 2007-2026 across 6 eras (IBM, Exeter, Amazon, Philips India, Philips USA, Independent)
- Professional feedback accounting: 88 post-event/interaction datasets and 1,050 response rows; two pre-event audience surveys and 133 rows are reported separately
- Community learning: 50 recorded deliveries, 3,732 participant instances, and 13 student-feedback forms with 494 response rows; presenter ratings remain separate at 4.58/5 (`n=149`) and 9.12/10 (`n=128`), while recommendation likelihood retains its source scale at 8.87/10 (`n=98`)

**Next:** Close embedding and evidence-index coverage gaps, continue applying the YAML frontmatter schema, and complete the reviewed public deployment boundary.

See `plan.md` for full execution plan.

### Build the public Executive Portfolio Observatory data

```bash
.venv/bin/python scripts/build_portfolio_data.py
```

The builder validates stable IDs and references, computes bounded metrics from committed records, attaches claims to supports and versioned methods, checks explicit longitudinal relationships, restricts external URLs to an allowlist, and writes `viz/src/data/portfolio.json`. Verbatim excerpts must occur exactly in their held canonical source. Published SHA-256 values cover that held artifact; for an external public record they explicitly do **not** claim to checksum the live web page. The browser projection contains approved excerpts and scoped source checksums—not local paths, raw artifacts, internal links, participant/donor identities, account details, or the private relationship export.

The current public contract keeps three independent credibility dimensions: source provenance, support directness, and claim state. Calculated or interpreted claims disclose inputs, formula or rubric, inclusion/exclusion and deduplication rules, rounding, caveats, confidence, and conflicts. An interpreted relationship never becomes causal merely because its endpoints occur in sequence.

The public pages intentionally do not display global confidence labels, caveat banners, claim inventory counts, or a Gaps lens. Those fields remain in the audit contract. Each primary route carries Datta's portrait, each story block contains one positive impact statement and one bounded evidence signal, and **Inspect claim** reveals meaning, evidence, derivation, scope, and the complete folded-claim trail. The Data Room searches 23 curated conclusions and a 34-source closure spanning direct support, method inputs, documentary records, and reconciliation sources; 16 story-linked methods and 10 story-linked relationships begin collapsed. Audit-only claims and their exclusive records remain in the deterministic contract but resolve to the generic Data Room invitation instead of a public detail page.

Final verification on 2026-08-07 passed all seven repository gates: Ruff, formatting, mypy, 274 tests passed with 2 skipped, TypeScript, the Vite production build, and the independent public-bundle privacy scan. All eight routes were checked at a 390 px viewport without page overflow; mobile places the executive answer before a compact portrait; Data Room clear resets in one action; audit-only deep links reveal no audit copy; and desktop/mobile screenshots were reviewed. Automated WCAG A/AA audits of the Brief and Inspect Claim returned zero violations, with gradient-background contrast retained as a manual review item.

### Private relationship export

Run the export only on a trusted local machine:

```bash
.venv/bin/python scripts/export_relationships.py
```

The generated `data/exports/relationships/` directory is a complete portable snapshot, not public portfolio data. By explicit owner decision it is versioned only in this access-controlled private repository. Its manifest records hashes and source inventories; its consistency report currently records 4,411 DuckDB chunks without Chroma vectors and 13 soft edge-to-artifact provenance references whose artifacts are absent. Full embedding vectors are emitted in deterministic parts below 48 MiB. Do not deploy, mirror publicly, or share this directory without another deliberate privacy review.

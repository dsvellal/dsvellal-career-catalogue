# Setup Instructions

**Project:** dsvellal-personal-knowledge-context
**Status:** Phases 0-6 and Executive Portfolio Observatory complete; Phase 7 cloud deployment pending

---

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager)
- Git
- Node.js 20+ and npm (portfolio development and verification)
- (Phase 1+) Google Gemini API key
- (Phase 6+) Google Drive API OAuth2 credentials
- (Phase 3+) Typst (for designed PDF output)
- (Phase 2+) Ollama (optional, for local LLM fallback)

---

## Initial Setup

```bash
# Clone
git clone <repo-url>
cd dsvellal-personal-knowledge-context

# Create virtual environment and install
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# Configure environment
cp .env.example .env
# Edit .env with your Gemini API key

# Verify CLI works
twin --help
twin status
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Phase 1+ | Google Gemini API key |
| `GOOGLE_DRIVE_CREDENTIALS` | Phase 6+ | Path to OAuth2 credentials JSON |
| `OLLAMA_BASE_URL` | Optional | Ollama server URL (default: http://localhost:11434) |
| `TWIN_DB_PATH` | Optional | DuckDB file path (default: ./data/knowledge.duckdb) |
| `TWIN_CHROMA_PATH` | Optional | ChromaDB persistence path (default: ./data/chroma) |

---

## Development Workflow

```bash
# Run tests
pytest

# Run linting
ruff check .

# Run type checking
mypy src/

# Start API server (Phase 2+)
twin serve

# Start with hot reload (development)
twin serve --reload
```

### Export the private relationship stores

The canonical stores are `data/knowledge.duckdb` and `data/chroma`. Export them, plus the exact NetworkX graph rebuilt from DuckDB, with:

```bash
.venv/bin/python scripts/export_relationships.py
```

The command writes an atomic snapshot to `data/exports/relationships/`:

- `duckdb/tables/`: every table as deterministic JSONL, with parsed JSON columns
- `duckdb/relationships/`: enriched edges and explicit artifact, evidence, person, skill, and program relationships
- `chromadb/`: readable records and complete embedding vectors split into deterministic JSONL parts below 48 MiB
- `networkx/`: node-link graph, per-node metrics, and graph summary
- `inventory/`, `manifest.json`, and `quality/consistency-report.md`: source identity, SHA-256 hashes, counts, and cross-store checks

This directory contains raw/private material. By explicit owner decision it is tracked only in the access-controlled private repository; it is not an input to the public portfolio and must not be deployed or mirrored publicly. The exporter reads only the canonical root-level stores; accidental stores under `viz/data/` are explicitly excluded.

Verify the exporter with:

```bash
.venv/bin/python -m pytest tests/test_export_relationships.py -q
```

### Build and run the Executive Portfolio Observatory

Regenerate and validate the claim-centric public projection:

```bash
.venv/bin/python scripts/build_portfolio_data.py
```

The builder reads committed source records, recomputes bounded metrics, and validates:

- exactly nine primary page records and stable human-readable claim/source/method IDs;
- a support edge and source record for every public claim;
- method records for calculated and interpreted claims;
- explicit endpoint claims, support, confidence, method/reasoning, and limitation for every longitudinal relationship;
- reference integrity across claims, supports, sources, methods, caveats, and conflicts;
- an allowlist for external public links and a deny-list for local paths, internal URLs, emails, account/PAN language, and similar private payloads;
- deterministic equality with `viz/src/data/portfolio.json`.

The prior `scripts/build_journey_data.py` and `journey.json` remain for regression history but are not the active UI contract.

Run and verify the portfolio:

```bash
cd viz
npm ci
npm run dev
npm run build
npx tsc --noEmit
```

The default development URL is `http://localhost:5173/#/brief`. Page routes and Level 3 records use stable hashes such as `#/trust`, `#/claim/<id>`, `#/source/<id>`, and `#/method/<id>`. `publicDir` is disabled, so production builds must import approved assets explicitly. The output must not contain raw `data/evidence/`, `data/exports/relationships/`, local paths, or internal URLs.

Verify both derived-data pipelines with:

```bash
.venv/bin/python -m pytest \
  tests/test_build_portfolio_data.py \
  tests/test_process_feedback.py \
  tests/test_build_journey_data.py \
  tests/test_export_relationships.py -q
```

---

## Project Layout

```
dsvellal-personal-knowledge-context/
├── src/
│   └── twin/
│       ├── __init__.py
│       ├── cli.py              # Typer CLI commands
│       ├── api/                # FastAPI endpoints
│       ├── ingestion/          # Format extractors, pipeline
│       ├── graph/              # DuckDB + NetworkX operations
│       ├── retrieval/          # Hybrid search, RRF
│       ├── synthesis/          # Voice engine, context assembly
│       ├── generators/         # Resume, cover letter, summary
│       └── providers/          # LLM provider abstraction
├── data/                       # DuckDB + ChromaDB (gitignored)
│   └── exports/relationships/  # Generated portable export, private-repository only
├── scripts/                    # Export and derived-data builders
│   ├── export_relationships.py
│   ├── build_portfolio_data.py
│   └── build_journey_data.py   # Superseded compatibility projection
├── tests/
├── viz/                        # React/Vite Executive Portfolio Observatory
├── templates/                  # Resume/PDF templates
├── pyproject.toml
├── .env.example
└── docs/                       # Architecture markdown files
```

---

## CLI Commands (current)

| Command | Status | Description |
|---------|--------|-------------|
| `twin --help` | Working | Show available commands |
| `twin status` | Working | Show system status (node type breakdown, last ingestion) |
| `twin init` | Working | Initialize knowledge graph database |
| `twin ingest <path>` | Working | Ingest a file or directory (full pipeline) |
| `twin serve` | Working | Start the FastAPI server (chat, ask, generate, summary) |
| `twin publish` | Working | Generate static portfolio (JSON + HTML) |
| `twin publish --viz-only` | Working | Generate viz-specific JSON data files |
| `twin index-evidence` | Working | Rebuild DuckDB evidence_index from evidence markdown |

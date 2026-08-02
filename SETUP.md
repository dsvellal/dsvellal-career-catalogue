# Setup Instructions

**Project:** dsvellal-personal-knowledge-context
**Status:** Phase 1 (Core Ingestion + Graph)

---

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager)
- Git
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
├── tests/
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
| `twin status` | Working | Show system status |
| `twin init` | Stub (Phase 1) | Initialize knowledge graph database |
| `twin ingest <path>` | Stub (Phase 1) | Ingest a file or directory |
| `twin serve` | Stub (Phase 2) | Start the API server |

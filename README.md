# Personal Knowledge Context System

A personal knowledge system that ingests professional artifacts (documents, achievements, code, recognition), builds a multi-dimensional knowledge graph, and serves multiple consumers through a unified API.

The system's primary persona is a first-person digital twin that can explain Datta's work, generate tailored resumes, produce weekly summaries, and power a dynamic portfolio.

---

## What It Does

- **Ingests** documents, achievements, code artifacts, and recognition into a knowledge graph
- **Retrieves** via hybrid search (vector, graph, full-text, temporal)
- **Synthesizes** first-person responses using a calibrated voice profile
- **Generates** tailored resumes, cover letters, and summaries from evidence

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

**Phase 0: Design** — Complete. All architecture docs, user flows, test cases, and project scaffolding are done.

**Phase 1: Core Ingestion + Graph** — Ready to begin. CLI framework is operational (`twin --help`).

See `plan.md` for full execution plan.

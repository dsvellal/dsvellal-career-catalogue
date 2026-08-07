# High-Level Design

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.1.0
**Status:** Draft

---

## 1. Consumer Specifications

### 1.1 Chat Twin (Web UI)

**Purpose:** Interactive conversational interface. Users ask questions about Datta, get first-person answers with evidence.

**Behavior:**
- Always responds in first person
- Cites evidence (links to artifacts)
- Gracefully handles questions outside knowledge ("I don't have records of that specific thing, but...")
- Adjusts depth based on detected audience
- Maintains conversation context within a session

**Tech:** Next.js or SvelteKit frontend, WebSocket for streaming responses.

### 1.2 Portfolio Site (Public)

**Purpose:** Dynamic, always-current professional portfolio.

**Journey Atlas views (curated from evidence):**

1. Executive Portrait — concise identity, operating modes, and strongest proof points
2. Twenty-Year Journey — braided professional, service, and capability timelines
3. Capability Compounder — how technical depth became broader organizational leverage
4. Outcome Ledger — quantified contribution grouped by scale, with attribution caveats
5. Trust & Respect — selected person-attributed recommendations and recognition
6. Influence Web — credibility → reusable mechanism → expanded reach, not a causal social graph
7. Teaching & Service Ripple — sustained teaching and service as a parallel career lane
8. Momentum & Next Horizon — recent evidence signals and explicitly aspirational directions

**Tech:** Static React/Vite site built from one curated, evidence-tiered JSON projection. Every view has a stable hash deep link. The raw relationship export and evidence archive are local-only inputs and are not copied into the build.

**Presentation rule:** The sequence is intentional: orient the visitor, establish chronology, demonstrate compounding capability and measurable value, then let other people's words validate trust before showing influence, service, and future momentum. This projects confidence without converting co-occurrence or self-authored claims into false authority.

### 1.3 Resume Generator

**Purpose:** Given a job description, produce a tailored resume highlighting relevant experience.

**Process:**
1. Parse JD: extract required skills, experience, keywords
2. Query graph: find matching nodes (skills, projects, outcomes)
3. Score coverage: what % of JD requirements have evidence?
4. Select & rank: choose most relevant items per section
5. Generate: format as resume (ATS-friendly or designed PDF)
6. Report gaps: what's in the JD that you can't evidence?

### 1.4 Weekly Summary Generator

**Purpose:** Produce a summary of work done in a time range.

**Process:**
1. Query artifacts ingested in time range
2. Query nodes modified/created in time range
3. Identify follow-ups from previous summaries
4. Synthesize into structured summary (completed, in-progress, follow-ups)

---

## 2. Synthesis Layer

### 2.1 LLM Provider Abstraction

```python
class LLMProvider(Protocol):
    async def generate(self, prompt: str, system: str, temperature: float = 0.7) -> str: ...
    async def embed(self, text: str) -> list[float]: ...
    async def classify(self, text: str, categories: list[str]) -> dict: ...

class GeminiProvider(LLMProvider):
    # Primary: gemini-2.5-pro for synthesis, gemini-2.5-flash for classification
    # Embedding: text-embedding-004

class OllamaProvider(LLMProvider):
    # Fallback: gemma4 for synthesis, BGE-m3 for embedding

class ProviderRouter:
    # Tries primary, falls back to secondary on failure/timeout
    # Logs which provider handled each request
```

### 2.2 Voice Engine

The voice engine ensures all outputs sound like Datta speaking in first person.

**Components:**
1. **Voice Profile** - A calibration document derived from writing samples
2. **System Prompt Template** - Enforces first-person, injects profile
3. **Tone Adapter** - Adjusts formality/technicality based on audience
4. **Confidence Gate** - Refuses to claim things not in the knowledge graph

**Voice Profile Structure:**
```yaml
identity:
  name: "Datta Vellal"
  current_role: "..."
  key_themes: ["...", "..."]

voice_characteristics:
  perspective: first_person
  tone: professional_but_approachable
  technical_depth: high
  self_presentation: confident_not_boastful
  signature_phrases: ["...", "..."]

boundaries:
  never_claim: ["things not evidenced", "exact dates if uncertain"]
  always_cite: true
  uncertainty_handling: "acknowledge gaps directly"

audience_adaptations:
  technical_recruiter:
    emphasis: skills, metrics, scale
    depth: medium
    jargon: use_freely
  hiring_manager:
    emphasis: impact, leadership, decision_making
    depth: high
    jargon: moderate
  peer_engineer:
    emphasis: technical_choices, tradeoffs, learnings
    depth: deep
    jargon: full
  non_technical:
    emphasis: outcomes, analogies, impact
    depth: low
    jargon: avoid
```

### 2.3 Context Assembly

For any synthesis request:
1. Decompose the query into sub-questions
2. Retrieve relevant nodes and chunks via hybrid search
3. Score relevance and select top-K context chunks
4. Assemble a context window with:
   - Voice profile (always present)
   - Relevant graph neighborhood (nodes + edges)
   - Supporting artifact excerpts (with citation markers)
   - Audience/format parameters
5. Generate with citation tracking
6. Post-process: verify claims against graph, flag unsupported statements

---

## 3. Retrieval Layer

### 3.1 Hybrid Search

Four retrieval strategies fused via Reciprocal Rank Fusion (RRF):

| Strategy | Source | Strength |
|----------|--------|----------|
| Vector Search | ChromaDB embeddings | Semantic similarity, finds conceptually related content |
| Graph Traversal | NetworkX (from DuckDB) | Relationship walks, path finding, neighborhood exploration |
| Full-Text Search | DuckDB FTS extension | Keyword matching, exact phrase lookup |
| Temporal Filter | DuckDB date queries | Time-bounded queries, recency weighting |

### 3.2 Fusion

Configurable weights per consumer:
- Resume generator: high vector weight (semantic matching to JD)
- Weekly summary: high temporal weight
- Chat twin: balanced across all four
- Legacy graph portfolio views: high graph weight
- Current Journey Atlas: no runtime fusion; it consumes the reviewed static journey projection

---

## 4. Security & Privacy

### 4.1 Privacy Controls

- `published` flag on every node: explicit opt-in for public visibility
- `visibility` property on projects: public/internal/confidential
- Publication step requires explicit confirmation
- Cloud deployment receives ONLY published nodes
- No raw artifact text in cloud, only synthesized outputs and embeddings
- Voice profile and system prompts stay local (cloud uses a published voice summary)
- The Journey Atlas consumes `viz/src/data/journey.json`, never `data/exports/relationships/` or raw evidence bodies
- Journey claims retain an evidence tier, opaque source ID, and caveat labels; private evidence paths are validated locally and removed before the browser bundle
- Vite `publicDir` is disabled so `viz/public/data/evidence` cannot be copied into a production bundle

### 4.2 Confidential Project Handling

Dual-layer approach:
- Store full detail locally with `visibility=confidential`
- At publish time, auto-generate anonymized versions via Gemini
- Human review required before deployment
- `anonymization_map` table tracks original-to-anonymized mapping

### 4.3 API Keys & Credentials

- Gemini API key in `.env` (never committed)
- Google Drive OAuth2 credentials in local secure storage
- Cloud deployment uses service account with read-only access to published snapshot

---

## 5. API Surface (Overview)

| Endpoint | Purpose | Primary Consumer |
|----------|---------|-----------------|
| `POST /api/ask` | Conversational Q&A | Chat Twin |
| `GET /api/search` | Hybrid retrieval | All |
| `POST /api/generate` | Structured output (resume, cover letter, etc.) | Generators |
| `POST /api/summary` | Time-bounded summaries | Weekly Summary |
| `GET /api/graph/*` | Graph traversal and exploration | Portfolio, Chat |
| `POST /api/ingest` | Document ingestion | CLI, Web Upload |
| `POST /api/publish` | Push curated subset to cloud | Admin |
| `GET /api/health` | System status | Monitoring |

See `low-level-design.md` for full API contracts and request/response schemas.

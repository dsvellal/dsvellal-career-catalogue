# Low-Level Design

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.1.0
**Status:** Draft

---

## 1. Data Model (DuckDB Schema)

### 1.1 Core Tables

```sql
-- Core identity nodes
CREATE TABLE nodes (
    id VARCHAR PRIMARY KEY,
    type VARCHAR NOT NULL,         -- project|skill|person|organization|achievement|outcome|time_range
    name VARCHAR NOT NULL,
    description VARCHAR,
    properties JSON NOT NULL DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_artifacts VARCHAR[] DEFAULT [],
    confidence DOUBLE DEFAULT 1.0,
    published BOOLEAN DEFAULT FALSE,
    visibility VARCHAR DEFAULT 'public'  -- public|internal|confidential
);

-- Typed relationships
CREATE TABLE edges (
    id VARCHAR PRIMARY KEY,
    source_id VARCHAR NOT NULL REFERENCES nodes(id),
    target_id VARCHAR NOT NULL REFERENCES nodes(id),
    type VARCHAR NOT NULL,         -- WORKED_ON|USED_SKILL|PRODUCED|RECOGNIZED_FOR|AT_ORG|DURING|COLLABORATED_WITH|EVIDENCED_BY|SUPERVISED_BY|SKILL_PARENT|ORG_PARENT
    properties JSON NOT NULL DEFAULT '{}',
    weight DOUBLE DEFAULT 1.0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_artifact_id VARCHAR,
    confidence DOUBLE DEFAULT 1.0
);

-- Source artifacts (raw ingested material)
CREATE TABLE artifacts (
    id VARCHAR PRIMARY KEY,
    file_path VARCHAR,
    file_name VARCHAR NOT NULL,
    file_type VARCHAR NOT NULL,    -- pdf|docx|email|git|json|md|txt
    content_hash VARCHAR NOT NULL, -- SHA-256 for dedup
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_channel VARCHAR NOT NULL,  -- cli|web|watch|gdrive
    status VARCHAR DEFAULT 'processed',  -- pending|processing|processed|failed
    metadata JSON DEFAULT '{}',
    classification JSON DEFAULT '{}',
    raw_text VARCHAR,
    chunk_count INTEGER DEFAULT 0
);

-- Content chunks (for embedding and retrieval)
CREATE TABLE chunks (
    id VARCHAR PRIMARY KEY,
    artifact_id VARCHAR NOT NULL REFERENCES artifacts(id),
    sequence INTEGER NOT NULL,
    content VARCHAR NOT NULL,
    section VARCHAR,
    embedding_id VARCHAR,          -- Reference to ChromaDB vector
    metadata JSON DEFAULT '{}'
);

-- Ingestion audit trail
CREATE TABLE ingestion_log (
    id VARCHAR PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action VARCHAR NOT NULL,       -- ingest|update|delete|classify|embed|link
    artifact_id VARCHAR,
    details JSON DEFAULT '{}',
    channel VARCHAR
);

-- Google Drive sync state
CREATE TABLE gdrive_sync (
    id VARCHAR PRIMARY KEY,
    drive_file_id VARCHAR NOT NULL UNIQUE,
    drive_name VARCHAR NOT NULL,
    drive_modified_time TIMESTAMP,
    local_artifact_id VARCHAR REFERENCES artifacts(id),
    sync_status VARCHAR DEFAULT 'synced',  -- synced|modified|deleted|new
    last_synced_at TIMESTAMP,
    page_token VARCHAR
);

-- Voice profile (versioned)
CREATE TABLE voice_profile (
    id VARCHAR PRIMARY KEY,
    version INTEGER NOT NULL,
    profile_text VARCHAR NOT NULL,
    writing_samples JSON DEFAULT '[]',
    tone_parameters JSON DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

-- Publication state
CREATE TABLE publications (
    id VARCHAR PRIMARY KEY,
    published_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    snapshot_hash VARCHAR NOT NULL,
    node_count INTEGER,
    config JSON DEFAULT '{}'
);

-- Anonymization mappings
CREATE TABLE anonymization_map (
    id VARCHAR PRIMARY KEY,
    original_node_id VARCHAR NOT NULL REFERENCES nodes(id),
    anonymized_name VARCHAR NOT NULL,
    anonymized_description VARCHAR,
    anonymized_properties JSON DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reviewed BOOLEAN DEFAULT FALSE,
    reviewer_notes VARCHAR
);
```

### 1.2 Indexes

```sql
CREATE INDEX idx_nodes_type ON nodes(type);
CREATE INDEX idx_nodes_visibility ON nodes(visibility);
CREATE INDEX idx_nodes_published ON nodes(published);
CREATE INDEX idx_edges_source ON edges(source_id);
CREATE INDEX idx_edges_target ON edges(target_id);
CREATE INDEX idx_edges_type ON edges(type);
CREATE INDEX idx_artifacts_hash ON artifacts(content_hash);
CREATE INDEX idx_artifacts_status ON artifacts(status);
CREATE INDEX idx_chunks_artifact ON chunks(artifact_id);
CREATE INDEX idx_gdrive_file_id ON gdrive_sync(drive_file_id);
```

---

## 2. Node Type Properties

Each node type has specific fields stored in `properties` JSON:

```yaml
Project:
  status: active|completed|paused|archived
  role: owner|lead|contributor|advisor
  org_id: reference to Organization node
  start_date: ISO 8601
  end_date: ISO 8601 | null
  impact_summary: one-line outcome
  tech_stack: [string]
  team_size: integer
  visibility: public|internal|confidential

Skill:
  category: technical|leadership|domain|tool|methodology
  proficiency: learning|competent|proficient|expert
  years_experience: number
  last_used: ISO 8601
  evidence_count: number (computed)

Person:
  relationship: manager|report|peer|collaborator|mentor|client
  org_id: reference
  interaction_period: {start, end}
  context: how you know them

Organization:
  type: employer|client|community|education
  role_held: job title / role
  department: string
  start_date: ISO 8601
  end_date: ISO 8601 | null
  location: string

Achievement:
  type: certification|award|recognition|publication|talk|patent
  issuer: who gave it
  date: ISO 8601
  expiry: ISO 8601 | null
  credential_id: string | null
  url: verification link | null

Outcome:
  type: metric|delivery|impact|efficiency
  value: the measurable result (e.g., "reduced build time by 40%")
  context: what made this significant
  project_id: reference

TimeRange:
  start: ISO 8601
  end: ISO 8601
  label: "Q3 2024" | "2022-2025" | "Sprint 47"
  type: quarter|year|sprint|custom
```

---

## 3. Edge Type Properties

```yaml
WORKED_ON:
  role: owner|lead|contributor|advisor|reviewer
  timeframe: {start, end}
  contribution_summary: what specifically you did

USED_SKILL:
  depth: primary|supporting|incidental
  context: how the skill was applied

PRODUCED:
  type: direct|contributed|influenced
  description: what was produced

RECOGNIZED_FOR:
  recognition_type: award|praise|promotion|certification
  recognizer: who recognized

AT_ORG:
  role: job title
  department: string
  timeframe: {start, end}

DURING:
  (no extra properties, just links any node to a TimeRange)

COLLABORATED_WITH:
  context: project/initiative name
  dynamic: peer|reported_to|managed

EVIDENCED_BY:
  claim: what specific claim this artifact supports
  strength: strong|moderate|weak

SUPERVISED_BY:
  timeframe: {start, end}

SKILL_PARENT:
  (hierarchy: Python -> Programming -> Technical Skills)

ORG_PARENT:
  (hierarchy: Team -> Department -> Company)
```

---

## 4. API Contracts

### 4.1 Ask (Conversational Twin)

```
POST /api/ask
{
  "question": "What experience do you have with knowledge graphs?",
  "context": {
    "audience": "technical_recruiter",
    "formality": "professional",
    "depth": "detailed"
  }
}

Response:
{
  "answer": "I've built two production knowledge graph systems...",
  "citations": [
    {"artifact_id": "...", "chunk_id": "...", "relevance": 0.92, "excerpt": "..."}
  ],
  "related_nodes": [
    {"id": "...", "type": "project", "name": "Chitta", "relevance": 0.95}
  ],
  "confidence": 0.88
}
```

### 4.2 Generate (Structured Output)

```
POST /api/generate
{
  "type": "resume",
  "parameters": {
    "job_description": "...",
    "target_role": "Senior ML Engineer",
    "time_range": {
      "start": "2026-07-21",
      "end": "2026-07-27"
    },
    "format": "pdf|markdown|json",
    "max_length": null,
    "emphasis": ["knowledge_graphs", "llm_applications"]
  }
}

Response:
{
  "content": "...",
  "format": "markdown",
  "metadata": {
    "skills_matched": ["Python", "Knowledge Graphs", "LLM"],
    "evidence_used": 12,
    "coverage_score": 0.78,
    "gaps": ["No evidence for Kubernetes experience"]
  }
}
```

### 4.3 Search (Hybrid Retrieval)

```
GET /api/search?q=machine+learning+projects&type=project&time_after=2024-01-01

Response:
{
  "results": [
    {
      "node": {"id": "...", "type": "project", "name": "...", "properties": {...}},
      "score": 0.94,
      "match_sources": ["vector", "graph", "fts"],
      "connected": {
        "skills": [...],
        "outcomes": [...],
        "achievements": [...]
      }
    }
  ],
  "total": 5,
  "facets": {
    "skills": [{"name": "Python", "count": 4}, ...],
    "orgs": [{"name": "Philips", "count": 3}, ...]
  }
}
```

### 4.4 Summary (Time-Bounded)

```
POST /api/summary
{
  "time_range": {
    "start": "2026-07-21",
    "end": "2026-07-27"
  },
  "format": "weekly_standup",
  "include_followups": true
}

Response:
{
  "summary": "This week I focused on...",
  "sections": {
    "completed": [...],
    "in_progress": [...],
    "follow_ups": [...],
    "blockers": [...]
  },
  "artifacts_referenced": 8,
  "time_range_label": "Week of July 21, 2026"
}
```

### 4.5 Graph (Exploration)

```
GET /api/graph/neighbors/{node_id}?depth=2&edge_types=WORKED_ON,USED_SKILL
GET /api/graph/path?from={node_id}&to={node_id}
GET /api/graph/cluster?center_type=skill&name=Python
GET /api/graph/timeline?start=2024-01-01&end=2026-07-27&node_types=project,achievement
```

### 4.6 Ingest

```
POST /api/ingest
Content-Type: multipart/form-data

file: <binary>
metadata: {
  "context": "Appreciation email from VP Engineering for Chitta demo",
  "project": "Chitta",
  "date": "2026-07-15",
  "type": "achievement"
}

Response:
{
  "artifact_id": "...",
  "status": "processed",
  "extracted": {
    "nodes_created": 2,
    "edges_created": 5,
    "chunks": 3
  },
  "classification": {
    "type": "recognition",
    "confidence": 0.94,
    "related_projects": ["Chitta"],
    "skills_mentioned": ["knowledge_graphs", "nlp"]
  }
}
```

### 4.7 Publish

```
POST /api/publish
{
  "include": {
    "node_types": ["project", "skill", "achievement", "outcome", "organization"],
    "published_flag": true,
    "min_confidence": 0.7
  },
  "exclude": {
    "node_ids": ["..."],
    "properties": {
      "visibility": "confidential"
    }
  },
  "target": "cloud",
  "format": "snapshot"
}

Response:
{
  "publication_id": "...",
  "published_at": "2026-07-27T...",
  "stats": {
    "nodes": 145,
    "edges": 312,
    "artifacts_referenced": 89,
    "excluded": 23
  },
  "deployment_url": "https://..."
}
```

---

## 5. Ingestion Pipeline

### 5.1 Processing Flow

```
Input (file + optional metadata)
    │
    ▼
┌─────────────────┐
│ Dedup Check     │──── duplicate ──── Skip (log)
│ (SHA-256 hash)  │
└────────┬────────┘
         │ new/modified
         ▼
┌─────────────────┐
│ Format Detection│
│ & Extraction    │
└────────┬────────┘
         │ raw text + structure
         ▼
┌─────────────────┐
│ AI Classification│
│ (Gemini)         │
│                  │
│ - Artifact type  │
│ - Time period    │
│ - Related nodes  │
│ - Key claims     │
│ - Confidence     │
└────────┬────────┘
         │ classification result
         ▼
┌─────────────────┐
│ Entity Resolution│
│                  │
│ - Match to       │
│   existing nodes │
│ - Create new     │
│   nodes if needed│
│ - Create edges   │
└────────┬────────┘
         │ graph updates
         ▼
┌─────────────────┐
│ Chunking &      │
│ Embedding       │
│                 │
│ - Semantic chunk│
│ - Embed each    │
│ - Store vectors │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Audit Log       │
│ (who/what/when) │
└─────────────────┘
```

### 5.2 AI Classification Prompt Pattern

```
You are classifying a document for a personal knowledge system.

Given this extracted text from a {file_type} file:
---
{extracted_text_preview}
---

Classify this artifact:
1. What type is this? (email_appreciation|certificate|project_doc|meeting_notes|code_readme|performance_review|recommendation|presentation|other)
2. What time period does it reference? (extract dates)
3. What projects are mentioned or implied?
4. What skills/technologies are demonstrated?
5. What people are mentioned and in what capacity?
6. What specific claims or achievements can be extracted?
7. Confidence (0.0-1.0) in your classification.

Respond as JSON matching this schema: {...}
```

### 5.3 Google Drive Sync

```
Sync Loop (scheduled, every 15 minutes):

1. Call Drive API changes.list with stored page_token
2. For each change:
   - NEW file: download, run through ingestion pipeline
   - MODIFIED file: download, re-extract, diff against stored version, update graph
   - DELETED file: mark artifact as deleted, soft-remove edges (keep audit trail)
   - MOVED file: update file_path metadata only
3. Store new page_token
4. Log sync activity
```

### 5.4 Supported Formats

| Format | Extraction Method |
|--------|------------------|
| PDF | pdfplumber |
| DOCX | python-docx |
| Email (.eml/.msg) | email parser |
| Git repo | gitpython (commits, PRs, READMEs) |
| Structured JSON | certificates, awards schema |
| Plain text / Markdown | direct read |

---

## 6. Worked Example

**Scenario:** Ingesting an appreciation email and later generating a resume.

### Step 1: Ingest

```bash
twin ingest ~/emails/vp-feedback-chitta-demo.eml --context "VP Engineering feedback after Chitta demo to leadership"
```

**Pipeline executes:**
1. Hash: `sha256:abc123...` (new, not duplicate)
2. Extract: email text, sender, date, subject
3. Classify (Gemini):
   ```json
   {
     "type": "email_appreciation",
     "date": "2026-07-15",
     "projects": ["Chitta"],
     "skills": ["knowledge_graphs", "nlp", "demo_presentation", "product_thinking"],
     "people": [{"name": "Sarah Chen", "role": "VP Engineering"}],
     "claims": [
       "Successfully demonstrated Chitta to senior leadership",
       "System described as 'game-changing for compliance workflow'",
       "Reduced document search time from hours to seconds"
     ],
     "confidence": 0.92
   }
   ```
4. Entity resolution:
   - Match "Chitta" to existing Project node
   - Match "Sarah Chen" to existing Person node (or create)
   - Create Achievement node: "VP Recognition for Chitta Demo"
   - Create Outcome node: "Reduced document search time from hours to seconds"
   - Create edges: RECOGNIZED_FOR(achievement->project), PRODUCED(project->outcome), etc.
5. Embed: 3 chunks stored in ChromaDB
6. Log: ingestion record created

### Step 2: Resume Generation (weeks later)

```bash
twin generate resume --jd ./senior-ml-engineer-jd.txt --format pdf
```

**Pipeline executes:**
1. Parse JD: extracts "knowledge graphs", "NLP", "Python", "production ML systems", "leadership"
2. Graph query: finds Chitta project (USED_SKILL: knowledge_graphs, nlp, python), finds Achievement (VP recognition), finds Outcome (hours to seconds)
3. Coverage: 4/5 JD requirements have evidence (gap: "leadership" needs more signal)
4. Generate resume with:
   - Chitta project prominently featured
   - Outcome "Reduced compliance document search from hours to seconds" as bullet
   - VP recognition as evidence of impact
   - Tailored skill section emphasizing JD keywords
5. Output: `./output/resume-senior-ml-engineer-2026-07-27.pdf`

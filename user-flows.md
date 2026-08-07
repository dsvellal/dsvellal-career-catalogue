# User Flows

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.2.0

---

## Flow 1: Ingest a New Artifact

**Actor:** Datta (system owner)
**Goal:** Add a new piece of evidence to the knowledge graph

### Via CLI

```
1. User runs: twin ingest ~/path/to/file.pdf --context "optional context"
2. System checks SHA-256 hash for duplicates
3. System extracts text based on file type
4. System classifies artifact via Gemini (type, time, projects, skills, claims)
5. System resolves entities (match/create nodes)
6. System creates typed edges between nodes
7. System chunks content and generates embeddings
8. System logs the ingestion event
9. User sees: summary of what was extracted (nodes created, edges, classification)
```

### Via Watch Folder

```
1. User drops file into ~/twin-inbox/
2. System detects new file (fswatch/watchdog)
3. System runs ingestion pipeline (same as CLI steps 2-8)
4. File is moved to ~/twin-inbox/processed/
```

### Via Google Drive

```
1. User saves file to synced Drive folder
2. System detects change on next sync cycle (every 15 min)
3. System downloads new/modified file
4. System runs ingestion pipeline
5. System updates gdrive_sync table with new state
```

---

## Flow 2: Ask a Question (Chat Twin)

**Actor:** Visitor (recruiter, hiring manager, colleague)
**Goal:** Learn about Datta's experience in a specific area

```
1. Visitor opens chat interface
2. Visitor types: "What experience do you have with knowledge graphs?"
3. System decomposes query into sub-questions
4. System runs hybrid search (vector + graph + FTS + temporal)
5. System fuses results via RRF
6. System assembles context (voice profile + relevant nodes + artifact excerpts)
7. System generates first-person response via Gemini
8. System verifies claims against graph (confidence gate)
9. Visitor sees: answer with citations and related nodes
10. Visitor can follow up within the same session context
```

---

## Flow 3: Generate a Tailored Resume

**Actor:** Datta
**Goal:** Produce a resume optimized for a specific job description

```
1. User runs: twin generate resume --jd ./job-description.txt
2. System parses JD: extracts required skills, experience, keywords
3. System queries graph for matching nodes (skills, projects, outcomes)
4. System scores coverage (% of JD requirements evidenced)
5. System selects and ranks most relevant items per resume section
6. System generates resume content with voice engine
7. System renders three outputs:
   - Markdown source (editable)
   - ATS-friendly PDF (WeasyPrint)
   - Designed PDF (Typst)
8. System reports gaps: JD requirements without evidence
9. User reviews and optionally edits markdown, re-renders
```

---

## Flow 4: Generate Weekly Summary

**Actor:** Datta
**Goal:** Get a structured summary of work done this week

```
1. User runs: twin summary --week (or scheduled automatically)
2. System queries artifacts ingested in the time range
3. System queries nodes modified/created in the time range
4. System identifies follow-ups from previous summaries
5. System synthesizes into sections: completed, in-progress, follow-ups, blockers
6. User sees: formatted summary ready for standup or manager update
```

---

## Flow 5: Publish to Cloud

**Actor:** Datta
**Goal:** Update the public digital twin with latest curated content

```
1. User runs: twin publish
2. System selects nodes where published=true AND visibility!=confidential
3. System runs anonymization on confidential nodes (Gemini)
4. System presents anonymized versions for human review
5. User approves/edits anonymized content
6. System generates published snapshot (nodes, edges, embeddings)
7. System deploys snapshot to cloud endpoint
8. Public consumers (portfolio, chat twin) now serve updated content
```

---

## Flow 6: Explore the Knowledge Graph

**Actor:** Datta or Visitor
**Goal:** Navigate relationships between skills, projects, and achievements

```
1. User navigates to graph view (portfolio or admin UI)
2. User selects a starting node (e.g., "Python" skill)
3. System returns 2-hop neighborhood (projects using Python, outcomes from those projects)
4. User clicks on a project node
5. System shows: connected skills, outcomes, achievements, time range, team
6. User can find paths between nodes ("how does X connect to Y?")
```

---

## Flow 7: Bulk Import (Initial Population)

**Actor:** Datta
**Goal:** Bootstrap the knowledge graph with existing career history

```
1. User organizes files by category in a staging directory
2. User runs: twin ingest --dir ./staging/ --recursive
3. System processes each file through the pipeline
4. System deduplicates across files (same content hash = skip)
5. System resolves entities across files (same project name = same node)
6. User runs: twin status
7. User sees: graph statistics (node count by type, edge count, coverage timeline)
8. User reviews and manually marks nodes as published/confidential
```

---

## Flow 8: Audit All Relationship Stores Locally

**Actor:** Datta or a trusted local analyst
**Goal:** Inspect every structured and vector relationship in portable formats without changing the source stores

```
1. User runs: .venv/bin/python scripts/export_relationships.py
2. Exporter opens data/knowledge.duckdb read-only and connects to canonical data/chroma
3. System stages every DuckDB table, enriched relationship projections, Chroma records/full vectors, and the exact rebuilt NetworkX graph
4. System checks referential integrity, Chroma/DuckDB alignment, graph counts, and output hashes
5. On success, system atomically installs data/exports/relationships/
6. User reviews manifest.json and quality/consistency-report.md before querying the JSON/JSONL/YAML files
7. If validation fails, the prior valid snapshot remains untouched
8. The private export remains local and never enters the portfolio build
```

---

## Archived Schema-v2 Portfolio Flows

Flows 9–13 document the prior nine-route observatory and global evidence-lens interaction. They remain for product history but are superseded by the schema-v3 flows that follow.

### Flow 9: Read the Executive Brief, Then Choose Depth (Archived)

**Actor:** Executive recruiter, hiring leader, board or transformation sponsor
**Goal:** Decide quickly whether Datta merits deeper evaluation, then verify the strongest claims

```
1. Visitor opens #/brief and receives a concise leadership thesis plus a small set of bounded proof points
2. Every proof point shows scope, unit, period, attribution, confidence, source count, and one material caveat
3. Visitor opens a claim dossier to understand why the claim matters and how it connects to other evidence
4. Visitor follows support links to source capsules or a method link to inspect inputs, formula/rubric, exclusions, and rounding
5. Browser Back returns to the same executive-question context without losing the evidence lens
6. No raw private artifact or local path is served at any depth
```

---

### Flow 10: Inspect a Hidden Longitudinal Relationship (Archived)

**Actor:** Leadership evaluator, organizational-development partner, or skeptical peer
**Goal:** Determine whether a cross-year leadership pattern is evidence or storytelling

```
1. Visitor opens Leadership System or Trust and enters the Relationship Lab
2. Visitor selects an explicit relationship such as 2020 development edge → 2025 independent corroborating observation
3. The interface shows both endpoint claims, their dates and claim states, and the relationship statement
4. Solid/dashed treatment distinguishes direct or calculated structure from interpretation
5. Visitor opens the relationship method/reasoning and sees confidence plus the explicit non-causal limitation
6. Visitor resolves each endpoint to its sources and can compare supporting, qualifying, or conflicting records
7. The interface never invents an edge from graph proximity, shared keywords, or visual layout
```

---

### Flow 11: Explore Participant Voice and Adaptation (Archived)

**Actor:** Conference organizer, learning leader, prospective mentee, or community participant
**Goal:** Understand what people actually learned, what they criticized, and how the teaching practice evolved

```
1. Visitor opens Learning & Multiplication
2. The summary separates delivery counts, participant instances, feedback datasets, response rows, qualitative entries, and rating observations
3. Visitor reads approved excerpts grouped by explicit participant-takeaway claim categories
4. Visitor compares those takeaways with approved excerpts explicitly classified as requested improvements
5. Visitor follows an adaptation relationship to later evidence while seeing that chronology does not prove causation
6. Source links resolve to sanitized aggregates or approved excerpts; participant identity remains withheld unless explicitly public
```

---

### Flow 12: Audit Claims in the Data Room (Archived)

**Actor:** Diligent evaluator, journalist, data-minded peer, or Datta
**Goal:** Search the complete public claim inventory and understand quality gaps and corrections

```
1. Visitor opens #/data-room and searches claim/source text, then filters by source access state or evidence grade
2. Results expose claims, supporting/qualifying links, methods, source capsules, and conflict records
3. Visitor opens a correction such as 90 mixed datasets → 88 post-event datasets + two pre-event surveys
4. The record shows the prior interpretation, corrected population, exact units, resolution, and affected claims
5. Visitor reviews corpus coverage gaps such as incomplete frontmatter/indexing, missing embeddings, orphan provenance, and curation bias
6. Private-source records state why originals are withheld and still expose a held-artifact checksum with its scope/note, an approved verbatim excerpt or labelled editorial summary, and what was supported; public external records clarify that the checksum is not of the mutable live page
```

---

### Flow 13: Change the Evidence Lens (Archived)

**Actor:** Any portfolio visitor
**Goal:** Read the same evidence according to the visitor's immediate question

```
1. Visitor selects Narrative, Proof, Method, or Gaps from the global lens control
2. Narrative foregrounds the executive explanation; Proof foregrounds source and support paths
3. Method foregrounds formulas, rubrics, denominators, and attribution; Gaps foregrounds caveats, conflicts, privacy boundaries, and missing coverage
4. The lens changes emphasis only—it does not create different facts or remove contradictory records
5. The choice remains keyboard operable and understandable on desktop and mobile
```

---

## Current Schema-v3 Portfolio Flows

### Flow 14: Read an Impact-First Executive Story

**Actor:** Executive recruiter, hiring leader, board member, or transformation sponsor
**Goal:** Understand Datta's leadership case without being asked to parse the evidence inventory first

```
1. Visitor opens #/brief and sees Datta's portrait, one concise thesis, and four executive signals
2. Visitor chooses Leadership, Career Journey, Trust, Innovation & Value, Learning, or Community & Service
3. The selected route retains the portrait identity anchor and shows two to four non-repeating impact blocks
4. Each block presents one heading, one meaning statement, one bounded evidence signal, and one evidence action
5. The same raw claim is never repeated as a second story card on another page
6. A legacy #/impact link resolves to Innovation & Value rather than failing or reopening a duplicate ledger
```

### Flow 15: Inspect a Curated Conclusion

**Actor:** Evidence-minded evaluator or skeptical peer
**Goal:** Move from executive meaning to complete traceability without switching global display modes

```
1. Visitor chooses Explore evidence / Inspect claim from a story block
2. The record opens with the block's positive conclusion and bounded evidence signal
3. Why this matters explains the leadership or organizational significance
4. Evidence combines the primary claim and every folded supporting conclusion, deduplicating shared sources
5. How this was derived exposes formulas, rubrics, inputs, inclusion rules, exclusions, and rounding where applicable
6. Scope & definitions explains scope, attribution, reconciliation, and interpretation boundaries in neutral language
7. Visitor can open source and method records, including the reviewed excerpt, locator, access state, and held-artifact checksum scope
8. Browser Back returns to the owning story page; no global Narrative/Proof/Method/Gaps state must be restored
```

### Flow 16: Search the Curated Data Room

**Actor:** Diligent evaluator, journalist, data-minded peer, or Datta
**Goal:** Find a conclusion or source without encountering a wall of raw audit records

```
1. Visitor opens #/data-room and sees the portrait-led page thesis plus an empty search invitation
2. Visitor searches a topic, refines by evidence access/basis, or explicitly chooses Browse all records
3. Results contain matching curated conclusions and source records; folded claims contribute to matching without becoming duplicate cards
4. For example, an AI search returns five curated conclusions and three source records
5. Visitor opens a conclusion through Inspect claim or opens a source capsule directly
6. Calculation methods and cross-record relationships remain available in collapsed disclosures below search
7. Four audit-only claims and their exclusive records stay out of search, browse, and direct public detail views while remaining represented by the audit contract
8. Clear results returns to the empty search invitation in one action
```

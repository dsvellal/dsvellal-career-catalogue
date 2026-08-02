# User Flows

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.1.0

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

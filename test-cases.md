# Test Cases

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.1.0

---

## 1. Ingestion Pipeline

### 1.1 Deduplication

| # | Test | Input | Expected |
|---|------|-------|----------|
| T1.1.1 | Reject duplicate file | Same file ingested twice | Second ingest returns "duplicate", no new nodes/edges |
| T1.1.2 | Accept modified file | Same filename, different content | New artifact created, existing nodes updated |
| T1.1.3 | Hash is content-based | Identical content, different filename | Detected as duplicate |

### 1.2 Format Extraction

| # | Test | Input | Expected |
|---|------|-------|----------|
| T1.2.1 | PDF extraction | Multi-page PDF with headers | Full text extracted, structure preserved |
| T1.2.2 | DOCX extraction | Word doc with formatting | Plain text extracted, tables preserved |
| T1.2.3 | Email extraction (.eml) | Email with sender, subject, body | Sender, date, subject, body all captured |
| T1.2.4 | Markdown passthrough | .md file | Content used directly |
| T1.2.5 | Unsupported format | .mp4 video file | Graceful rejection with clear error |

### 1.3 AI Classification

| # | Test | Input | Expected |
|---|------|-------|----------|
| T1.3.1 | Appreciation email | "Great work on the demo..." | type=email_appreciation, projects detected, skills extracted |
| T1.3.2 | Certificate | PDF certificate image | type=certification, issuer and date extracted |
| T1.3.3 | Project README | GitHub README.md | type=code_readme, tech_stack extracted |
| T1.3.4 | Low confidence | Ambiguous document | confidence < 0.5, flagged for review |

### 1.4 Entity Resolution

| # | Test | Input | Expected |
|---|------|-------|----------|
| T1.4.1 | Match existing project | Doc mentions "Chitta" when Chitta node exists | Links to existing node, no duplicate |
| T1.4.2 | Create new project | Doc mentions unknown project name | New Project node created |
| T1.4.3 | Skill hierarchy | "Python" mentioned | Links to existing Python skill node, not duplicate |
| T1.4.4 | Person resolution | "Sarah Chen, VP Engineering" | Matches existing person or creates with role |

---

## 2. Retrieval & Search

### 2.1 Vector Search

| # | Test | Input | Expected |
|---|------|-------|----------|
| T2.1.1 | Semantic match | "machine learning projects" | Returns ML-related projects even if "machine learning" not in text |
| T2.1.2 | No results | Query with zero semantic overlap | Empty results, not an error |

### 2.2 Graph Traversal

| # | Test | Input | Expected |
|---|------|-------|----------|
| T2.2.1 | 1-hop neighbors | Node ID + depth=1 | Returns directly connected nodes only |
| T2.2.2 | Path finding | Two connected nodes | Returns shortest path with edge types |
| T2.2.3 | Disconnected nodes | Two unconnected nodes | Returns empty path, not error |

### 2.3 Hybrid Fusion (RRF)

| # | Test | Input | Expected |
|---|------|-------|----------|
| T2.3.1 | Multi-source hit | Query matching vector + FTS | Higher score than single-source match |
| T2.3.2 | Weight configuration | Custom weights per consumer | Results order changes based on weights |

---

## 3. Synthesis & Voice

### 3.1 Voice Consistency

| # | Test | Input | Expected |
|---|------|-------|----------|
| T3.1.1 | First-person enforcement | Any question | Response uses "I", "my", "I've" — never "Datta" in third person |
| T3.1.2 | Confidence gate | Question about unrecorded topic | Response acknowledges gap: "I don't have records of..." |
| T3.1.3 | Citation tracking | Question with graph evidence | Response includes citations with artifact references |

### 3.2 Audience Adaptation

| # | Test | Input | Expected |
|---|------|-------|----------|
| T3.2.1 | Technical recruiter | audience=technical_recruiter | Emphasizes skills, metrics, scale |
| T3.2.2 | Non-technical | audience=non_technical | Avoids jargon, uses analogies |

---

## 4. Generators

### 4.1 Resume

| # | Test | Input | Expected |
|---|------|-------|----------|
| T4.1.1 | JD matching | JD with 5 required skills | Resume emphasizes matching skills, reports gaps |
| T4.1.2 | Triple output | Generate command | Produces markdown + ATS PDF + designed PDF |
| T4.1.3 | Gap reporting | JD with skill not in graph | Gap clearly reported in metadata |
| T4.1.4 | Empty graph | Generate with no ingested data | Graceful error, not a crash |

### 4.2 Summary

| # | Test | Input | Expected |
|---|------|-------|----------|
| T4.2.1 | Weekly summary | time_range = last 7 days | Sections: completed, in-progress, follow-ups |
| T4.2.2 | Empty week | time_range with no activity | Returns "no activity recorded" message |
| T4.2.3 | Follow-up tracking | Previous summary had follow-ups | Current summary references them |

---

## 5. Privacy & Publishing

### 5.1 Visibility

| # | Test | Input | Expected |
|---|------|-------|----------|
| T5.1.1 | Confidential excluded | Publish with confidential nodes | Confidential nodes absent from snapshot |
| T5.1.2 | Anonymization | Confidential node at publish | Anonymized version created, original preserved locally |
| T5.1.3 | Published flag | Node with published=false | Excluded from cloud deployment |

### 5.2 Data Isolation

| # | Test | Input | Expected |
|---|------|-------|----------|
| T5.2.1 | No raw text in cloud | Published snapshot | Contains embeddings and synthesis, not raw artifact text |
| T5.2.2 | API key isolation | Cloud deployment | No local API keys exposed in cloud config |

---

## 6. Integration Tests

### 6.1 End-to-End: Ingest → Ask

```
Given: Empty database
When: Ingest an appreciation email mentioning "Chitta" and "knowledge graphs"
Then: Ask "What experience do you have with knowledge graphs?"
Expected: Response mentions Chitta project with citation to the email
```

### 6.2 End-to-End: Ingest → Generate Resume

```
Given: 5 artifacts ingested covering 3 projects
When: Generate resume with JD requiring Python, ML, leadership
Then: Resume includes relevant projects, reports "leadership" as gap if no evidence
Expected: All three output formats produced without error
```

### 6.3 End-to-End: Drive Sync → Graph Update

```
Given: Existing synced file with known content
When: File modified in Google Drive
Then: Next sync cycle detects change, re-extracts, updates graph
Expected: Node properties reflect new content, audit trail records update
```

---

## 7. Edge Cases & Error Handling

| # | Test | Scenario | Expected |
|---|------|----------|----------|
| T7.1 | Gemini rate limit | Classification during rate limit | Falls back to Ollama or queues for retry |
| T7.2 | Corrupted file | Binary garbage as input | Graceful error, logged, pipeline continues |
| T7.3 | Massive file | 100MB PDF | Chunked processing, doesn't OOM |
| T7.4 | Concurrent ingestion | 10 files simultaneously | No race conditions on entity resolution |
| T7.5 | Network offline | Gemini unreachable | Falls back to Ollama, logs degradation |
| T7.6 | Empty artifact | File with no extractable text | Logged as failed, no phantom nodes created |

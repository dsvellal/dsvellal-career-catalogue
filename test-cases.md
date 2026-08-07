# Test Cases

**Project:** dsvellal-personal-knowledge-context
**Version:** 0.2.0

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

---

## 8. Relationship Export and Public Portfolio Projection

### 8.1 Portable relationship export

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.1.1 | Complete deterministic serialization | Fixture DuckDB, Chroma collection, and derived viz files | Every table, relationship projection, Chroma record/vector part, NetworkX graph, inventory, report, and manifest is written in stable order |
| T8.1.2 | Parsed data types | JSON-valued DuckDB fields and Unicode/newline text | JSON is emitted as objects/lists and text round-trips without loss |
| T8.1.3 | Cross-store alignment | Matching DuckDB and Chroma chunks | IDs, documents, metadata, and artifact links agree; counts appear in the report |
| T8.1.4 | Exact runtime graph | Connected and isolated fixture nodes | Node-link graph and per-node degree/component metrics match the production `DiGraph` projection |
| T8.1.5 | Atomic replacement | Existing output plus a valid new snapshot | Old output is replaced only after all hashes and validations pass; no staging directories remain |
| T8.1.6 | Failure preservation | Chroma record with a missing artifact reference | Export fails and preserves the prior snapshot unchanged |
| T8.1.7 | Missing canonical source | Absent DuckDB or Chroma path | Clear failure without creating a phantom database or output |
| T8.1.8 | Git-hostable vector partitioning | Embedding JSONL larger than the configured part limit | Complete ordered record stream is split into deterministic parts, each at or below the byte limit |

Automated coverage: `tests/test_export_relationships.py` (5 tests, passing on 2026-08-07).

### 8.2 Curated journey dataset (legacy regression)

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.2.1 | Committed output is reproducible | `build_journey_data()` and committed `journey.json` | Parsed objects match exactly and both pass validation |
| T8.2.2 | Exact view contract | Generated `meta.views` | Exactly eight IDs in narrative order; every declared `data_key` exists |
| T8.2.3 | Public payload boundary | Serialized journey object | No local evidence path/filename, email domain, HTTP(S) URL, PAN-card phrase, account-number phrase, or raw artifact body |
| T8.2.4 | Evidence vocabulary | Private source model and nested public references | Private paths exist before stripping; public refs have opaque stable IDs and support text; all four evidence tiers are represented |
| T8.2.5 | Claim boundaries | Eras, metrics, and caveat glossary | Canonical chronology is exact; every displayed metric has evidence; team, self-reported, co-occurrence, and future-direction caveats exist |
| T8.2.6 | Writer outputs | Temporary output/report paths | Valid schema-versioned JSON and analysis explaining the eight-view rationale are written |

Automated coverage: `tests/test_build_journey_data.py` (5 tests, passing on 2026-08-07). Together with the export suite, 10 focused tests pass.

### 8.3 Journey Atlas UI and public build (archived verification)

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.3.1 | Hash normalization | Empty, invalid, and valid view hashes | Empty/invalid hashes resolve to `#portrait`; valid hashes render the named view |
| T8.3.2 | Keyboard navigation | Desktop nav focus plus Left/Right/Home/End | Focus wraps or moves to the first/last view without changing semantic link behavior |
| T8.3.3 | Mobile navigation | Viewport ≤900 px | Desktop tabs hide; labeled native selector remains available |
| T8.3.4 | Chart accessibility | Braided and momentum SVGs, influence links, scroll regions | Informative charts have names/descriptions, decoration is hidden, dense regions are keyboard focusable |
| T8.3.5 | Motion preference | `prefers-reduced-motion: reduce` | Page animation and smooth scrolling are disabled |
| T8.3.6 | Public bundle isolation | Production Vite build | Build succeeds, all eight views render, approved logo/photo assets load, and `dist/data/evidence` is absent |
| T8.3.7 | Static typing | `npx tsc --noEmit` | No TypeScript errors in current or archived components |

Verification on 2026-08-06: `npm run build` and `npx tsc --noEmit` pass; the production artifact is 1.2 MB with five files (HTML, CSS, JS, logo, photo), and `dist/data/evidence` is absent. All eight desktop and 390 px mobile deep links were reviewed, the mobile document width stayed equal to the viewport, arrow-key navigation was exercised, and automated WCAG A/AA checks reported zero violations. Gradient contrast remains a manual visual check and was reviewed in settled screenshots.

### 8.4 Corrected professional-feedback aggregate

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.4.1 | Mutually exclusive populations | Duplicate, pre-survey, and post-event fixtures | Duplicate files are excluded first; pre-surveys and post-event records have no overlap |
| T8.4.2 | Transparent units | Files with multiple text and rating fields | File count, response rows, qualitative entries, rating-question aggregates, and rating observations remain separate |
| T8.4.3 | Correct committed totals | `all_sessions_data.json` | 88 post-event/interaction datasets and 1,050 rows; two pre-surveys and 133 rows; category counts match the reviewed table |
| T8.4.4 | No heterogeneous satisfaction score | Mixed 5/10-point questions and constructs | Rating inventory is reported, but no global average/satisfaction claim is emitted |
| T8.4.5 | JSCPD interpretation boundary | Before file plus post-exercise ratings | Post ratings can be reported; unmatched files do not establish code improvement or causality |
| T8.4.6 | Deterministic regeneration | Committed JSON extract and temporary output | Repeated `--from-json` generation is byte stable and matches committed `summary_stats.json` |

Automated coverage: `tests/test_process_feedback.py`.

### 8.5 Claim-centric portfolio dataset (archived schema-v2 contract)

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.5.1 | Deterministic committed projection | `build_portfolio_data()` and `portfolio.json` | Parsed objects match exactly and validation succeeds |
| T8.5.2 | Exact route contract | Generated `pages` | Nine ordered routes: Brief through Data Room; every page claim ID resolves |
| T8.5.3 | Stable reference integrity | Claims, supports, sources, methods, relationships, caveats, conflicts | IDs are unique and every cross-reference resolves |
| T8.5.4 | Claim support and method coverage | All public claims | Every claim has support; calculated/interpreted claims have versioned methods with inputs/rules/result |
| T8.5.5 | Explicit relationship integrity | All longitudinal relationships | Endpoint and relationship claims, supports, state, reasoning/method, confidence, caveats, and limitation are present |
| T8.5.6 | Correct metric derivations | Session, connect, 360, service, career, and inventory records | Values, formula inputs, unit, scope, attribution, rounding, and caveats match source records |
| T8.5.7 | Privacy boundary | Serialized projection | No local path, internal domain, email, account/PAN language, raw export payload, or placeholder evidence; external URL hosts are allowlisted |
| T8.5.8 | Source publication record | Every source capsule | Stable human ID, held-artifact checksum scope/note, access state, locator through support, and approved excerpt are present; exact verbatim excerpts occur in their canonical source and an external-page checksum is never implied |
| T8.5.9 | Conflict transparency | Superseded mixed-population and attribution claims | Conflict remains visible and affected claims point to the corrected resolution |

Automated coverage: `tests/test_build_portfolio_data.py`.

### 8.6 Executive Portfolio Observatory UI and public build (archived schema-v2 contract)

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.6.1 | Primary and detail routing | Empty/invalid hash; nine page hashes; claim/source/method hashes | Default and invalid routes resolve safely; every valid route renders a focused heading and browser-history entry |
| T8.6.2 | Global evidence lens | Narrative, Proof, Method, Gaps controls | Same claim set remains; selected layer becomes visible; state is keyboard operable and persisted as a nonessential enhancement |
| T8.6.3 | Claim-to-source traversal | A summary claim with method/support | Visitor can reach claim dossier, support/source record, and method record, then navigate back without a dead end |
| T8.6.4 | Relationship Lab semantics | Observed and interpreted records | Only declared records render; line style and text communicate state; endpoints/method/caveat are navigable |
| T8.6.5 | Participant transparency | Learning route | Positive takeaways and constructive criticism use explicit data groupings; no unversioned browser-side sentiment/theme inference |
| T8.6.6 | Data Room discovery | Search and access/grade/state filters | Claims and sources are discoverable; result count updates accessibly; methodology exposes conflicts, caveats, and quality gaps |
| T8.6.7 | Media safety | Production asset graph | Only allowlisted reviewed images are bundled; no third-party faces/names, internal comments/URLs, or identifiable children |
| T8.6.8 | Responsive layout | Desktop and compact viewport | Primary navigation adapts, cards remain readable, detail routes preserve depth, and page width does not overflow viewport |
| T8.6.9 | Accessibility and motion | Keyboard, focus, semantic landmarks, reduced-motion preference | Skip link, route focus, controls, tabs, links, and focus indicators work without pointer/color dependence; nonessential motion is disabled |
| T8.6.10 | Type/build/privacy gates | TypeScript, Vite build, serialized bundle scan | `tsc --noEmit` and production build pass; bundle has no forbidden private token or raw evidence/export directory |

### 8.7 Final verification record — 2026-08-07

- `./scripts/check.sh lint types test frontend`: all 7 gates passed.
- Python: Ruff lint and format passed; mypy passed across 35 source files; pytest reported 269 passed, 2 skipped, and 3 dependency deprecation warnings.
- Portfolio: deterministic builder check passed for 9 routes, 55 claims, 82 supports, 36 sources, 18 methods, 11 relationships, 30 caveats, and 8 conflicts.
- Frontend: TypeScript passed; Vite built 41 modules; independent `scripts/check_public_bundle.py` accepted `viz/dist` with only four reviewed documentary images.
- Browser: all 9 primary routes rendered the expected heading at 1440×1000 and 390×844; document width equalled viewport width on every route; claim → source and claim → method traversal, Data Room search, filters, and Relationship Lab state filters passed.
- Accessibility: axe-core WCAG A/AA reported zero violations on the Brief, Data Room Methodology, and Trust Relationship Lab. Gradient backgrounds made automated contrast computation inconclusive, so settled desktop/mobile screenshots were reviewed manually. Console contained only Vite/React development notices; page errors were empty.

### 8.8 Schema-v3 executive story layer

| # | Test | Input | Expected |
|---|------|-------|----------|
| T8.8.1 | Exact route contract | Generated `pages` | Eight ordered routes: Brief, Leadership, Journey, Trust, Innovation, Learning, Community, Data Room; no Impact page |
| T8.8.2 | Legacy route compatibility | `#/impact` | Router resolves to the Innovation & Value page and its focused heading |
| T8.8.3 | Story-block count and density | Generated `story_blocks` | Exactly 23 blocks; two to four blocks per narrative page; zero blocks in Data Room |
| T8.8.4 | Exact claim ownership | Primary, folded, and audit-only IDs | All 55 claims occur exactly once: 51 story-owned and 4 audit-only |
| T8.8.5 | Story reference integrity | Every story block | Page, primary claim, folded claims, optional image source, and source support all resolve |
| T8.8.6 | One-impact language contract | Story titles and proof copy | No duplicate initiative-card headings or audit-first title vocabulary; each block has title, meaning, proof, and one evidence route |
| T8.8.7 | Folded traceability | Inspect Claim for a multi-claim block | Primary and folded conclusions appear together; sources are deduplicated; evidence, method, and scope remain openable |
| T8.8.8 | No global evidence mode | Application shell and detail route | No Narrative/Proof/Method/Gaps control or persisted lens state; claim details contain the relevant disclosures |
| T8.8.9 | Executive-surface semantics | Story pages | No public confidence/state badges, caveat banner, claim/source/method counts, or raw audit wall |
| T8.8.10 | Portrait coverage | Eight primary routes | Each route renders one primary portrait plus the compact global-header thumbnail |
| T8.8.11 | Curated Data Room | Empty, `AI`, browse, and clear states | Empty state shows no wall; `AI` returns 5 conclusions and 3 sources; browse/search operates on 23 conclusions and the 34-source publication closure; Clear results resets in one action |
| T8.8.12 | Collapsed audit depth | Data Room | Calculation methods and evidence relationships begin closed and remain keyboard operable |
| T8.8.13 | Responsive geometry | Every route at 390 px | `scrollWidth <= innerWidth`; content, disclosures, and navigation remain usable |
| T8.8.14 | Accessibility | Brief and Inspect Claim | Axe WCAG A/AA returns zero violations; gradient contrast remains documented for manual review |
| T8.8.15 | Public-bundle privacy | Production `dist` | Only reviewed assets are present; forbidden private paths, identifiers, raw evidence, and exports are absent |
| T8.8.16 | Audit publication guard | Audit-only claim, exclusive source, and exclusive method hashes | Generic evidence invitation appears; document title and rendered page reveal no audit identifier or audit copy |
| T8.8.17 | Story-linked disclosures | Browse all Data Room state | Exactly 34 story-relevant sources, 16 story-linked methods, and 10 story-linked relationships are available; method-input and reconciliation sources remain traceable; audit-only records are absent |
| T8.8.18 | Mobile answer-first hierarchy | Brief at 390 px | Executive copy appears before a compact portrait; portrait remains present; redundant portrait caption is hidden |
| T8.8.19 | Bidirectional source lineage | Method-input and reconciliation-only source records | Method/reconciliation links reach the source; source detail reports and links back to its method or reconciled conclusion |

Automated story-layer coverage is in `tests/test_build_portfolio_data.py`; browser assertions cover routes, portrait count, Data Room search, responsive width, and axe checks.

### 8.9 Schema-v3 final verification record — 2026-08-07

- `./scripts/check.sh lint types test frontend`: all seven checks passed.
- Python: Ruff lint/format and mypy passed; pytest reported 274 passed and 2 skipped.
- Data: schema v3 regenerated deterministically with 8 pages, 23 story blocks, exact 55-claim ownership, 82 supports, 36 sources, 18 methods, and 11 relationships.
- Frontend: TypeScript, Vite production build, and independent public-bundle privacy validation passed.
- Browser: all eight routes rendered the expected page at desktop and 390 px mobile widths; every route had one primary portrait plus the global-header thumbnail; every mobile route satisfied `scrollWidth <= innerWidth`; desktop and mobile screenshots were visually reviewed.
- Data Room: `AI` search returned 5 curated conclusions and 3 source records rather than a raw claim wall; Browse all returned 23 conclusions and the 34-source publication closure; 16 methods and 10 relationships were story-linked and collapsed initially; Clear results reset in one action.
- Publication guards: direct hashes for an audit-only claim, source, and method returned the generic evidence invitation without rendering the raw identifier, audit copy, or unsafe document title.
- Accessibility: Brief and Inspect Claim axe WCAG A/AA audits each returned zero violations. Gradient-background contrast items were automated-incomplete and manually reviewed.

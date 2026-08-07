# Relationship export consistency report

The export preserves the canonical DuckDB tables, Chroma records and embeddings, and the exact NetworkX runtime graph. Personal data in this directory is private and must not be committed or published without review.

## DuckDB tables

| Table | Rows |
|---|---:|
| `anonymization_map` | 0 |
| `artifacts` | 1,364 |
| `chunks` | 25,767 |
| `edges` | 17,190 |
| `evidence_index` | 562 |
| `gdrive_sync` | 0 |
| `ingestion_log` | 1,259 |
| `nodes` | 3,471 |
| `publications` | 0 |
| `voice_profile` | 1 |

## Referential and graph checks

| Check | Count |
|---|---:|
| `duplicate_ordered_edge_pairs` | 0 |
| `orphan_chunk_artifacts` | 0 |
| `orphan_edge_artifact_provenance` | 13 |
| `orphan_edge_sources` | 0 |
| `orphan_edge_targets` | 0 |
| `orphan_ingestion_artifacts` | 0 |
| `self_loops` | 0 |

`orphan_edge_artifact_provenance` and `orphan_ingestion_artifacts` are soft, non-foreign-key provenance links and are reported rather than hidden.

## ChromaDB alignment

| Check | Count |
|---|---:|
| `duckdb_chunk_ids` | 25,767 |
| `chroma_ids` | 21,356 |
| `overlap` | 21,356 |
| `missing_in_chroma` | 4,411 |
| `extra_in_chroma` | 0 |
| `orphan_artifact_links` | 0 |
| `document_mismatches` | 0 |
| `metadata_mismatches` | 0 |

## Runtime NetworkX graph

- Nodes: 3,471
- Edges: 17,190
- Isolates: 244
- Weak components: 247
- Largest weak component: 3,223

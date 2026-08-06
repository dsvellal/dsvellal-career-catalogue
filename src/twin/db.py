"""DuckDB schema initialization and connection management."""

from pathlib import Path

import duckdb

DEFAULT_DB_PATH = Path("./data/knowledge.duckdb")

SCHEMA_SQL = """
-- Core identity nodes
CREATE TABLE IF NOT EXISTS nodes (
    id VARCHAR PRIMARY KEY,
    type VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    description VARCHAR,
    properties JSON NOT NULL DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_artifacts VARCHAR[] DEFAULT [],
    confidence DOUBLE DEFAULT 1.0,
    published BOOLEAN DEFAULT FALSE,
    visibility VARCHAR DEFAULT 'public'
);

-- Typed relationships
CREATE TABLE IF NOT EXISTS edges (
    id VARCHAR PRIMARY KEY,
    source_id VARCHAR NOT NULL REFERENCES nodes(id),
    target_id VARCHAR NOT NULL REFERENCES nodes(id),
    type VARCHAR NOT NULL,
    properties JSON NOT NULL DEFAULT '{}',
    weight DOUBLE DEFAULT 1.0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_artifact_id VARCHAR,
    confidence DOUBLE DEFAULT 1.0
);

-- Source artifacts (raw ingested material)
CREATE TABLE IF NOT EXISTS artifacts (
    id VARCHAR PRIMARY KEY,
    file_path VARCHAR,
    file_name VARCHAR NOT NULL,
    file_type VARCHAR NOT NULL,
    content_hash VARCHAR NOT NULL,
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    source_channel VARCHAR NOT NULL,
    status VARCHAR DEFAULT 'processed',
    metadata JSON DEFAULT '{}',
    classification JSON DEFAULT '{}',
    raw_text VARCHAR,
    chunk_count INTEGER DEFAULT 0,
    media_path VARCHAR,
    media_url VARCHAR
);

-- Content chunks (for embedding and retrieval)
CREATE TABLE IF NOT EXISTS chunks (
    id VARCHAR PRIMARY KEY,
    artifact_id VARCHAR NOT NULL REFERENCES artifacts(id),
    sequence INTEGER NOT NULL,
    content VARCHAR NOT NULL,
    section VARCHAR,
    embedding_id VARCHAR,
    metadata JSON DEFAULT '{}'
);

-- Ingestion audit trail
CREATE TABLE IF NOT EXISTS ingestion_log (
    id VARCHAR PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action VARCHAR NOT NULL,
    artifact_id VARCHAR,
    details JSON DEFAULT '{}',
    channel VARCHAR
);

-- Google Drive sync state
CREATE TABLE IF NOT EXISTS gdrive_sync (
    id VARCHAR PRIMARY KEY,
    drive_file_id VARCHAR NOT NULL UNIQUE,
    drive_name VARCHAR NOT NULL,
    drive_modified_time TIMESTAMP,
    local_artifact_id VARCHAR REFERENCES artifacts(id),
    sync_status VARCHAR DEFAULT 'synced',
    last_synced_at TIMESTAMP,
    page_token VARCHAR
);

-- Voice profile (versioned)
CREATE TABLE IF NOT EXISTS voice_profile (
    id VARCHAR PRIMARY KEY,
    version INTEGER NOT NULL,
    profile_text VARCHAR NOT NULL,
    writing_samples JSON DEFAULT '[]',
    tone_parameters JSON DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

-- Publication state
CREATE TABLE IF NOT EXISTS publications (
    id VARCHAR PRIMARY KEY,
    published_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    snapshot_hash VARCHAR NOT NULL,
    node_count INTEGER,
    config JSON DEFAULT '{}'
);

-- Anonymization mappings
CREATE TABLE IF NOT EXISTS anonymization_map (
    id VARCHAR PRIMARY KEY,
    original_node_id VARCHAR NOT NULL REFERENCES nodes(id),
    anonymized_name VARCHAR NOT NULL,
    anonymized_description VARCHAR,
    anonymized_properties JSON DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reviewed BOOLEAN DEFAULT FALSE,
    reviewer_notes VARCHAR
);
"""

INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(type);
CREATE INDEX IF NOT EXISTS idx_nodes_visibility ON nodes(visibility);
CREATE INDEX IF NOT EXISTS idx_nodes_published ON nodes(published);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_id);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_id);
CREATE INDEX IF NOT EXISTS idx_edges_type ON edges(type);
CREATE INDEX IF NOT EXISTS idx_artifacts_hash ON artifacts(content_hash);
CREATE INDEX IF NOT EXISTS idx_artifacts_status ON artifacts(status);
CREATE INDEX IF NOT EXISTS idx_chunks_artifact ON chunks(artifact_id);
CREATE INDEX IF NOT EXISTS idx_gdrive_file_id ON gdrive_sync(drive_file_id);
"""


def get_connection(db_path: Path = DEFAULT_DB_PATH) -> duckdb.DuckDBPyConnection:
    """Open a connection to the DuckDB database."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))


def init_schema(db_path: Path = DEFAULT_DB_PATH) -> Path:
    """Create all tables and indexes. Returns the database path."""
    from twin.ingestion.evidence_index import create_evidence_index_table

    conn = get_connection(db_path)
    try:
        conn.execute(SCHEMA_SQL)
        conn.execute(INDEX_SQL)
        create_evidence_index_table(conn)
    finally:
        conn.close()
    return db_path


def is_initialized(db_path: Path = DEFAULT_DB_PATH) -> bool:
    """Check whether the database exists and has the schema."""
    if not db_path.exists():
        return False
    conn = get_connection(db_path)
    try:
        tables = conn.execute("SHOW TABLES").fetchall()
        return len(tables) > 0
    finally:
        conn.close()

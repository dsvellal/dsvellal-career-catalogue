#!/usr/bin/env python3
"""Batch ingest pre-classified artifacts from a JSON manifest.

Usage:
    python scripts/ingest_batch.py data/batch.json

Manifest format:
[
  {
    "file_name": "ibm-bravo-award-2008.jpg",
    "file_type": "image",
    "media_url": "https://...",
    "context": "IBM Bravo Award, June 2008",
    "raw_text": "...",
    "classification": {
      "type": "certificate",
      "dates": [{"date": "2008-06-01", "context": "award date"}],
      "projects": [...],
      "skills": [...],
      "people": [...],
      "organizations": [...],
      "claims": [...],
      "confidence": 0.96
    }
  }
]
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from twin.db import DEFAULT_DB_PATH, get_connection, init_schema
from twin.ingestion.pipeline import ingest_pre_classified


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/ingest_batch.py <manifest.json>")
        sys.exit(1)

    manifest_path = Path(sys.argv[1])
    if not manifest_path.exists():
        print(f"Error: {manifest_path} not found")
        sys.exit(1)

    items = json.loads(manifest_path.read_text())

    if not DEFAULT_DB_PATH.exists():
        init_schema(DEFAULT_DB_PATH)

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        for i, item in enumerate(items, 1):
            result = ingest_pre_classified(
                classification_data=item["classification"],
                conn=conn,
                file_name=item.get("file_name", f"item_{i}"),
                file_type=item.get("file_type", "image"),
                raw_text=item.get("raw_text", ""),
                media_url=item.get("media_url", ""),
                context=item.get("context", ""),
                channel="batch",
            )
            status_icon = "+" if result.status == "processed" else "="
            print(
                f"  {status_icon} [{result.status}] {result.file_name} "
                f"— {result.nodes_created} nodes, {result.edges_created} edges"
            )

        total = conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0]
        nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
        edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        print(f"\nDB totals: {total} artifacts, {nodes} nodes, {edges} edges")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

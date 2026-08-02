#!/usr/bin/env python3
"""Enrich existing graph nodes with additional properties.

Usage:
    python scripts/enrich_nodes.py data/enrich_<name>.json

Manifest format:
[
  {
    "type": "skill",
    "name": "Java",
    "properties": {
      "category": "programming_language",
      "first_seen": "2007-07-01"
    }
  },
  ...
]

Each entry finds the node by (type, name) case-insensitively and merges
the given properties into the existing ones. Unknown nodes are skipped
with a warning.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from twin.db import DEFAULT_DB_PATH, get_connection, init_schema


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/enrich_nodes.py <manifest.json>")
        sys.exit(1)

    manifest_path = Path(sys.argv[1])
    if not manifest_path.exists():
        print(f"Error: {manifest_path} not found")
        sys.exit(1)

    items = json.loads(manifest_path.read_text())

    if not DEFAULT_DB_PATH.exists():
        init_schema(DEFAULT_DB_PATH)

    conn = get_connection(DEFAULT_DB_PATH)
    updated = skipped = 0

    try:
        for item in items:
            node_type = item["type"]
            name = item["name"]
            new_props = item.get("properties", {})

            row = conn.execute(
                "SELECT id, properties FROM nodes WHERE type = ? AND LOWER(name) = ?",
                [node_type, name.strip().lower()],
            ).fetchone()

            if not row:
                print(f"  ? [skip]    {node_type}:{name} — not found")
                skipped += 1
                continue

            node_id, existing_raw = row
            existing = json.loads(existing_raw) if existing_raw else {}
            existing.update({k: v for k, v in new_props.items() if v is not None})
            conn.execute(
                "UPDATE nodes SET properties = ? WHERE id = ?",
                [json.dumps(existing), node_id],
            )
            print(f"  + [enriched] {node_type}:{name}")
            updated += 1

        print(f"\nDone: {updated} enriched, {skipped} skipped")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

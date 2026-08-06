"""Generate static JSON data files for the viz frontend from DuckDB.

This script is invoked by `twin publish` to produce pre-shaped,
view-specific JSON files that the viz frontend imports directly.

Key changes from the previous manual export:
- Philips era split into "Philips USA" (2021-12-06+) and "Philips India" (2018-09-18 to 2021-12-04)
- Reverse chronological order everywhere
- Evidence file references included for drill-down
- Three-level data: summary, rich_summary, evidence_file
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

SPLIT_DATE = "2021-12-05"
EVIDENCE_BASE = Path("data/evidence")
VIZ_DATA_DIR = Path("viz/src/data")
DB_PATH = Path("data/knowledge.duckdb")

ERA_ORDER = [
    "Philips USA",
    "Philips India",
    "Amazon",
    "Exeter",
    "IBM",
    "Independent",
]

ERA_COLORS = {
    "Philips USA": "#c98500",
    "Philips India": "#e6a817",
    "Amazon": "#199e70",
    "Exeter": "#d95926",
    "IBM": "#3987e5",
    "Independent": "#9085e9",
}


def _build_evidence_lookup() -> dict[str, list[dict]]:
    """Build a year→files lookup from the evidence_index table if available."""
    try:
        from twin.db import get_connection

        if not DB_PATH.exists():
            return {}
        conn = get_connection(DB_PATH)
        rows = conn.execute(
            "SELECT file_path, file_name, title, year, date FROM evidence_index"
        ).fetchall()
        conn.close()

        lookup: dict[str, list[dict]] = {}
        for fp, fn, title, year, date in rows:
            key = str(year) if year else "unknown"
            lookup.setdefault(key, []).append({
                "file_path": fp,
                "file_name": fn,
                "title": title or "",
                "date": date or "",
            })
        return lookup
    except Exception:
        return {}


_EVIDENCE_LOOKUP: dict[str, list[dict]] | None = None


def find_evidence_file(title: str, date: str, era: str) -> str | None:
    """Attempt to find a matching evidence file for a timeline item."""
    global _EVIDENCE_LOOKUP
    if _EVIDENCE_LOOKUP is None:
        _EVIDENCE_LOOKUP = _build_evidence_lookup()

    year = date[:4] if len(date) >= 4 else None
    if not year:
        return None

    # Try evidence_index lookup first (DuckDB-backed)
    candidates = _EVIDENCE_LOOKUP.get(year, [])
    if candidates:
        slug_words = [w for w in re.sub(r"[^a-z0-9]+", " ", title.lower()).split() if len(w) > 3]
        best_match = None
        best_score = 0
        for c in candidates:
            c_text = (c["title"] + " " + c["file_name"]).lower()
            score = sum(1 for w in slug_words if w in c_text)
            if score > best_score and score >= 2:
                best_score = score
                best_match = c["file_path"]
        if best_match:
            p = Path(best_match)
            try:
                return str(p.relative_to(Path.cwd()))
            except ValueError:
                return str(p)

    # Fallback: scan filesystem
    evidence_dir = EVIDENCE_BASE / year / "individual"
    if not evidence_dir.exists():
        return None

    slug = re.sub(r"[^a-z0-9]+", "-", title.lower().strip())[:40].rstrip("-")

    for f in evidence_dir.iterdir():
        if not f.suffix == ".md":
            continue
        fname_lower = f.stem.lower()
        words = [w for w in slug.split("-") if len(w) > 3]
        matches = sum(1 for w in words if w in fname_lower)
        if matches >= 2:
            return str(f.relative_to(Path(".")))

    return None


def split_philips_era(philips_era: dict) -> tuple[dict, dict]:
    """Split single Philips era into India and USA based on dates."""
    india_years = []
    usa_years = []

    for yr_group in philips_era["years"]:
        year = yr_group["year"]
        india_months = []
        usa_months = []

        for month_group in yr_group["months"]:
            india_items = []
            usa_items = []

            for item in month_group["items"]:
                date = item.get("date", str(year))
                if len(date) >= 10:
                    is_usa = date > SPLIT_DATE
                elif len(date) == 7:
                    is_usa = date > "2021-12"
                else:
                    if "Moved to North America" in item.get("title", ""):
                        is_usa = True
                    elif "Promoted to Principal" in item.get("title", ""):
                        is_usa = True
                    elif year <= 2021:
                        is_usa = False
                    else:
                        is_usa = True

                if is_usa:
                    usa_items.append(item)
                else:
                    india_items.append(item)

            if india_items:
                india_months.append({**month_group, "items": india_items})
            if usa_items:
                usa_months.append({**month_group, "items": usa_items})

        if india_months:
            india_years.append({
                "year": year,
                "total": sum(len(m["items"]) for m in india_months),
                "months": india_months,
            })
        if usa_months:
            usa_years.append({
                "year": year,
                "total": sum(len(m["items"]) for m in usa_months),
                "months": usa_months,
            })

    india_era = {
        "era": "Philips India",
        "org": "Philips India",
        "role": "Software Competency Lead → Engineering Manager",
        "start": 2018,
        "end": 2021,
        "start_date": "2018-09-18",
        "end_date": "2021-12-04",
        "location": "Bangalore, India",
        "color_slot": 1,
        "years": india_years,
        "total": sum(y["total"] for y in india_years),
    }

    usa_era = {
        "era": "Philips USA",
        "org": "Philips North America",
        "role": "Principal Engineer, Medical Device Software",
        "start": 2021,
        "end": 2026,
        "start_date": "2021-12-06",
        "end_date": "present",
        "location": "Cambridge, MA",
        "color_slot": 0,
        "years": usa_years,
        "total": sum(y["total"] for y in usa_years),
    }

    return usa_era, india_era


def enrich_timeline_items(eras: list[dict]) -> list[dict]:
    """Add evidence_file references to timeline items where possible."""
    for era in eras:
        for yr_group in era.get("years", []):
            for month_group in yr_group.get("months", []):
                for item in month_group.get("items", []):
                    if "evidence_file" not in item:
                        ef = find_evidence_file(
                            item.get("title", ""),
                            item.get("date", str(yr_group["year"])),
                            era["era"],
                        )
                        if ef:
                            item["evidence_file"] = ef
    return eras


def generate_timeline(input_path: Path, output_path: Path) -> dict:
    """Generate the split, enriched timeline_full.json."""
    with open(input_path) as f:
        raw_data = json.load(f)

    new_eras = []

    for era in raw_data:
        if era["era"] == "Philips":
            usa, india = split_philips_era(era)
            new_eras.append(usa)
            new_eras.append(india)
        else:
            new_eras.append(era)

    ordered = []
    for era_name in ERA_ORDER:
        match = next((e for e in new_eras if e["era"] == era_name), None)
        if match:
            ordered.append(match)

    ordered = enrich_timeline_items(ordered)

    with open(output_path, "w") as f:
        json.dump(ordered, f, indent=2)

    total_items = sum(e.get("total", 0) for e in ordered)
    return {"eras": len(ordered), "total_items": total_items}


def generate_impact(input_path: Path, output_path: Path) -> dict:
    """Copy impact data, adding evidence file references where possible."""
    with open(input_path) as f:
        data = json.load(f)

    for item in data:
        if "evidence_file" not in item:
            ef = find_evidence_file(
                item.get("label", ""),
                "",
                item.get("era", ""),
            )
            if ef:
                item["evidence_file"] = ef

    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    return {"items": len(data)}


def generate_voices(input_path: Path, output_path: Path) -> dict:
    """Enrich voices data with evidence references."""
    with open(input_path) as f:
        data = json.load(f)

    for item in data:
        if "evidence_file" not in item:
            ef = find_evidence_file(
                item.get("quote", "")[:40],
                item.get("date", ""),
                item.get("company", ""),
            )
            if ef:
                item["evidence_file"] = ef

    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    return {"voices": len(data)}


def main():
    """Run all data generators."""
    print("Publishing viz data...")
    print(f"  Output: {VIZ_DATA_DIR}")
    print()

    VIZ_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Timeline
    timeline_in = VIZ_DATA_DIR / "timeline_full.json"
    if timeline_in.exists():
        stats = generate_timeline(timeline_in, timeline_in)
        print(f"  ✓ timeline_full.json — {stats['eras']} eras, {stats['total_items']} items")

    # Impact
    impact_in = VIZ_DATA_DIR / "impact.json"
    if impact_in.exists():
        stats = generate_impact(impact_in, impact_in)
        print(f"  ✓ impact.json — {stats['items']} items")

    # Voices
    voices_in = VIZ_DATA_DIR / "voices.json"
    if voices_in.exists():
        stats = generate_voices(voices_in, voices_in)
        print(f"  ✓ voices.json — {stats['voices']} voices")

    print()
    print("Done. Viz data updated.")


if __name__ == "__main__":
    main()

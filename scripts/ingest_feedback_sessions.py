#!/usr/bin/env python3
"""Ingest feedback survey files from Philips internal sessions and university talks.

Reads Excel (.xlsx) and CSV files, extracts responses, computes ratings,
builds raw_text narratives, classifies, and ingests into DuckDB + ChromaDB.
"""

import csv
import os
import sys
from pathlib import Path
from datetime import datetime

import openpyxl

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from twin.db import DEFAULT_DB_PATH, get_connection, init_schema
from twin.ingestion.pipeline import ingest_pre_classified
from twin.retrieval.chunker import chunk_text, store_chunks
from twin.retrieval.embeddings import embed_chunks

BASE_DIR = "/Users/dsvellal/Downloads/dsvellal-data-catalogue/Website/Students feedbacks/"


def read_xlsx(filepath):
    """Read an Excel file and return headers + data rows."""
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active
    rows = []
    for row in ws.iter_rows(values_only=True):
        rows.append(list(row))
    wb.close()
    if not rows:
        return [], []
    return rows[0], rows[1:]


def read_csv_file(filepath):
    """Read a CSV file and return headers + data rows."""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return [], []
    return rows[0], rows[1:]


def find_rating_columns(headers):
    """Find columns that look like rating/scale questions (1-10 or 1-5)."""
    rating_cols = []
    for i, h in enumerate(headers):
        if h is None:
            continue
        h_lower = h.lower()
        if any(kw in h_lower for kw in [
            "scale of 1", "how likely", "rate", "rating",
            "capturing attention", "audience engagement", "knowledge on topic",
            "how relevant", "recommend"
        ]):
            rating_cols.append((i, h))
    return rating_cols


def find_text_columns(headers):
    """Find columns that contain textual feedback."""
    text_cols = []
    skip_keywords = ["id", "start time", "completion time", "email", "name",
                     "timestamp", "username", "last modified"]
    for i, h in enumerate(headers):
        if h is None:
            continue
        h_lower = h.lower().strip()
        if any(h_lower.startswith(kw) or h_lower == kw for kw in skip_keywords):
            continue
        text_cols.append((i, h))
    return text_cols


def compute_ratings(data_rows, rating_cols):
    """Compute average ratings for each rating column."""
    results = {}
    for col_idx, col_name in rating_cols:
        values = []
        for row in data_rows:
            if col_idx < len(row) and row[col_idx] is not None:
                try:
                    v = float(str(row[col_idx]).strip())
                    if 0 < v <= 10:
                        values.append(v)
                except (ValueError, TypeError):
                    pass
        if values:
            results[col_name] = {
                "avg": round(sum(values) / len(values), 2),
                "count": len(values),
                "min": min(values),
                "max": max(values),
            }
    return results


def extract_text_responses(data_rows, text_cols, max_per_col=20):
    """Extract notable text responses from feedback columns."""
    responses = {}
    for col_idx, col_name in text_cols:
        col_responses = []
        for row in data_rows:
            if col_idx < len(row) and row[col_idx] is not None:
                val = str(row[col_idx]).strip()
                if val and val.lower() not in ("none", "n/a", "na", "-", "nil", "no"):
                    col_responses.append(val)
        if col_responses:
            responses[col_name] = col_responses[:max_per_col]
    return responses


def build_raw_text(event_name, date_str, num_responses, ratings, text_responses, org):
    """Build a narrative raw_text for the artifact."""
    lines = []
    lines.append(f"# Feedback Survey: {event_name}")
    lines.append(f"Date: {date_str}")
    lines.append(f"Organization: {org}")
    lines.append(f"Total Responses: {num_responses}")
    lines.append("")

    if ratings:
        lines.append("## Ratings Summary")
        for col_name, stats in ratings.items():
            short_name = col_name.split("\n")[0][:80]
            lines.append(f"- {short_name}: {stats['avg']}/10 (n={stats['count']}, range {stats['min']}-{stats['max']})")
        lines.append("")

    if text_responses:
        lines.append("## Qualitative Feedback")
        for col_name, responses in text_responses.items():
            short_name = col_name.split("\n")[0][:100]
            lines.append(f"\n### {short_name}")
            for r in responses[:10]:
                # Truncate very long responses
                display = r[:300] + "..." if len(r) > 300 else r
                lines.append(f'- "{display}"')
        lines.append("")

    return "\n".join(lines)


def get_skills_from_event(event_name):
    """Derive skills from the event name."""
    event_lower = event_name.lower()
    skills = ["technical training", "knowledge sharing", "presentation"]

    skill_map = {
        "unit testing": ["unit testing", "software testing", "test automation"],
        "tdd": ["test-driven development", "TDD", "software testing"],
        "test driven": ["test-driven development", "TDD", "software testing"],
        "clean code": ["clean code", "code quality", "software craftsmanship"],
        "clean-code": ["clean code", "code quality", "software craftsmanship"],
        "interview": ["interviewing", "hiring", "talent acquisition"],
        "tech debt": ["technical debt", "code quality", "refactoring"],
        "code duplication": ["code duplication", "refactoring", "DRY principle"],
        "jscpd": ["code duplication detection", "JSCPD", "static analysis"],
        "mutation testing": ["mutation testing", "test quality"],
        "pair programming": ["pair programming", "collaborative development"],
        "microservices": ["microservices", "software architecture"],
        "mentoring": ["mentoring", "coaching"],
        "code dojo": ["code dojo", "coding kata", "collaborative learning"],
        "program behavior": ["program behavior metrics", "software metrics"],
        "crafting code quality": ["code quality", "software tooling", "static analysis"],
        "swcoe": ["software engineering", "center of excellence"],
        "i will code": ["coding practice", "hands-on coding", "learning program"],
        "shift left": ["shift-left testing", "quality at desk", "DevOps"],
        "hiring culture": ["hiring culture", "recruitment transformation"],
        "bar raiser": ["bar raiser", "interview training", "hiring standards"],
        "skill raiser": ["bar raiser", "interview training", "hiring standards"],
        "solid": ["SOLID principles", "object-oriented design"],
        "github": ["GitHub", "version control", "DevOps"],
        "copilot": ["GitHub Copilot", "AI-assisted coding", "developer productivity"],
        "back to basics": ["software fundamentals", "coding basics"],
        "new hire": ["onboarding", "new hire training"],
        "design-thinking": ["design thinking", "reliability engineering"],
    }

    for keyword, mapped_skills in skill_map.items():
        if keyword in event_lower:
            skills.extend(mapped_skills)

    return list(set(skills))


def get_claims_from_ratings(event_name, ratings, num_responses):
    """Generate claims based on ratings."""
    claims = []
    for col_name, stats in ratings.items():
        if stats["avg"] >= 8.0:
            short_name = col_name.split("\n")[0][:60]
            claims.append(f"Received average rating of {stats['avg']}/10 for '{short_name}' across {stats['count']} responses")
        elif stats["avg"] >= 7.0:
            short_name = col_name.split("\n")[0][:60]
            claims.append(f"Received average rating of {stats['avg']}/10 for '{short_name}' across {stats['count']} responses")

    claims.append(f"Delivered '{event_name}' session with {num_responses} attendees providing feedback")
    return claims


# ============ FILE DEFINITIONS ============

FILES_TO_PROCESS = [
    # (filename, event_name, date, org)
    ("20190407 - Unit Testing Workshop Feedback(1-20).xlsx",
     "Unit Testing Workshop", "2019-04-07", "Philips India"),
    ("20190415 - Conducting interviews - knowledge sharing session(1-8).xlsx",
     "Conducting Interviews - Knowledge Sharing Session", "2019-04-15", "Philips India"),
    ("20190708 - Test driven development & clean-code practices(1-16).xlsx",
     "Test Driven Development & Clean-Code Practices", "2019-07-08", "Philips India"),
    ("20190808 - Tech Debt - What does that mean_(1-4).xlsx",
     "Tech Debt - What Does That Mean?", "2019-08-08", "Philips India"),
    ("20190819 - New Hire - Feedback on clean code environment setup(1-24).xlsx",
     "New Hire - Clean Code Environment Setup", "2019-08-19", "Philips India"),
    ("20190826 - New Hire Mentoring - Feedback to your mentor_ Dattatreya S Vellal (dsvellal@philips.com)(1-6).xlsx",
     "New Hire Mentoring - Feedback for Datta", "2019-08-26", "Philips India"),
    ("20190909 - Code duplication elimination workshop feedback(1-17).xlsx",
     "Code Duplication Elimination Workshop", "2019-09-09", "Philips India"),
    ("20190911 - Program Behavior Metrics - Feedback(1-4).xlsx",
     "Program Behavior Metrics", "2019-09-11", "Philips India"),
    ("20190913 - Code dojo session with Simao(1-2).xlsx",
     "Code Dojo Session with Simao", "2019-09-13", "Philips India"),
    ("20190923 - JSCPD Tool - Introduction to EOI Team(1-12).xlsx",
     "JSCPD Tool - Introduction to EOI Team", "2019-09-23", "Philips India"),
    ("20190925 - .clean code initiatives feedback form(1-65).xlsx",
     "Clean Code Initiatives Feedback Form", "2019-09-25", "Philips India"),
    ("20191004 - Feedback to Dattaterya S Vellal (dsvellal@philips.com)(1-3).xlsx",
     "General Feedback for Datta", "2019-10-04", "Philips India"),
    ("20191014 - Mutation testing session(1-1).xlsx",
     "Mutation Testing Session", "2019-10-14", "Philips India"),
    ("20191015 - JSCPD After Elimination(1-6).xlsx",
     "JSCPD After Elimination", "2019-10-15", "Philips India"),
    ("20191015 - JSCPD Before Elimination(1-16).xlsx",
     "JSCPD Before Elimination", "2019-10-15", "Philips India"),
    ("20191107 - Crafting Code Quality - Tooling, Feedback(1-14).xlsx",
     "Crafting Code Quality - Tooling", "2019-11-07", "Philips India"),
    ("20191111 - Feedback about the SWCoE training(1-14).xlsx",
     "Software CoE Training Feedback", "2019-11-11", "Philips India"),
    ("20191111 - Feedback about Datta's interaction with you in Shanghai(1-4).xlsx",
     "Datta's Interaction in Shanghai", "2019-11-11", "Philips India"),
    ("20200131 - Initiative_ I will code!(1-85).xlsx",
     "Initiative: I Will Code!", "2020-01-31", "Philips India"),
    ("20200218 - Pair programming - feedback(1-8).xlsx",
     "Pair Programming Session", "2020-02-18", "Philips India"),
    ("20200302 - Feedback about Datta, wrt pair-programming(1-4).xlsx",
     "Feedback About Datta - Pair Programming", "2020-03-02", "Philips India"),
    ("20200304 - Software CoE - Interaction experience(1-14).xlsx",
     "Software CoE - Interaction Experience", "2020-03-04", "Philips India"),
    ("20200604 - Relooking at interviews - things we already know(1-3).xlsx",
     "Relooking at Interviews - Things We Already Know", "2020-06-04", "Philips India"),
    ("20200716 - Feedback on Microservices & associated reliability_design-thinking(1-7).xlsx",
     "Microservices & Reliability/Design-Thinking", "2020-07-16", "Philips India"),
    ("20200813 - [Anonymous] Feedback about the _Bar_Skill raiser training_ session(1-19).xlsx",
     "Bar/Skill Raiser Training Session", "2020-08-13", "Philips India"),
    ("20200909 - [Anonymous Feedback] Interview upskilling(1-4).xlsx",
     "Interview Upskilling", "2020-09-09", "Philips India"),
    ("20201011 - Changing the hiring culture - feedback(1-11).xlsx",
     "Changing the Hiring Culture", "2020-10-11", "Philips India"),
    ("20201016 - End of _I Will Code_ Survey(1-5).xlsx",
     "End of 'I Will Code' Survey", "2020-10-16", "Philips India"),
    ("20210210 - Shift left quality (quality-at-desk) - feedback(1-5).xlsx",
     "Shift Left Quality (Quality-at-Desk)", "2021-02-10", "Philips North America"),
    ("20210226 - Interviewing tips - an interactive session with Datta(1-6).xlsx",
     "Interviewing Tips - Interactive Session", "2021-02-26", "Philips North America"),
    ("20210319 - Feedback about today's conversation(1-4).xlsx",
     "Feedback About Today's Conversation", "2021-03-19", "Philips North America"),
    ("20210405 - Feedback for Datta(1-3).xlsx",
     "Feedback for Datta", "2021-04-05", "Philips North America"),
    ("20230515 - Feedback for _Back to basics_ workshop(1-10).xlsx",
     "Back to Basics Workshop", "2023-05-15", "Philips North America"),
    # Note: filename has non-breaking spaces (0xc2a0)
    ("20240627 - SOLID  - Feedback Talk D.xlsx",
     "SOLID Principles - Feedback Talk", "2024-06-27", "Philips North America"),
    ("20240927 - [Feedback] GitHub foundational training course - OHC(1-5).xlsx",
     "GitHub Foundational Training Course - OHC", "2024-09-27", "Philips North America"),
    ("20250227 - Coding with GitHub CoPilot - Session Feedback(1-17).xlsx",
     "Coding with GitHub CoPilot", "2025-02-27", "Philips North America"),
]

CSV_FILES = [
    ("Social Media & The World Of Microservices.csv",
     "Social Media & The World of Microservices", "2019-05-18", "SIT Tumkur"),
    ("How was today's session - SOLID Principles of OO design & programming.csv",
     "SOLID Principles of OO Design & Programming", "2018-09-18", "RVCE Bangalore"),
    ("Feedback for today's session.csv",
     "University Guest Lectures - Consolidated Feedback", "2020-03-07", "AIT/SIT"),
]


def process_file(filepath, event_name, date_str, org, conn, file_type="xlsx"):
    """Process a single feedback file and ingest it."""
    if file_type == "xlsx":
        headers, data_rows = read_xlsx(filepath)
    else:
        headers, data_rows = read_csv_file(filepath)

    if not headers or not data_rows:
        return None, "No data found"

    num_responses = len(data_rows)
    rating_cols = find_rating_columns(headers)
    text_cols = find_text_columns(headers)
    ratings = compute_ratings(data_rows, rating_cols)
    text_responses = extract_text_responses(data_rows, text_cols)

    raw_text = build_raw_text(event_name, date_str, num_responses, ratings, text_responses, org)

    # Build classification
    skills = get_skills_from_event(event_name)
    claims = get_claims_from_ratings(event_name, ratings, num_responses)

    # Determine projects
    projects = ["Software Center of Excellence"]
    event_lower = event_name.lower()
    if "i will code" in event_lower:
        projects.append("I Will Code Initiative")
    if "jscpd" in event_lower:
        projects.append("JSCPD Code Duplication Detection")
    if "clean code" in event_lower:
        projects.append("Clean Code Initiative")
    if "bar" in event_lower or "skill raiser" in event_lower:
        projects.append("Bar Raiser Program")
    if "hiring" in event_lower or "interview" in event_lower:
        projects.append("Hiring Culture Transformation")
    if "github" in event_lower or "copilot" in event_lower:
        projects.append("Developer Tooling Training")

    # People mentioned
    people = [{"name": "Dattatreya S Vellal", "role": "presenter/facilitator"}]
    if "simao" in event_lower:
        people.append({"name": "Simao", "role": "co-facilitator"})

    classification = {
        "type": "feedback_survey",
        "dates": [{"date": date_str, "context": f"Session date for '{event_name}'"}],
        "projects": projects,
        "skills": skills,
        "people": people,
        "organizations": [{"name": org, "role": "employer" if "Philips" in org else "educational institution"}],
        "claims": claims,
        "confidence": 0.95,
    }

    filename = os.path.basename(filepath)
    context = f"Feedback survey for '{event_name}' delivered at {org} on {date_str}. {num_responses} responses collected."

    result = ingest_pre_classified(
        classification_data=classification,
        conn=conn,
        file_name=filename,
        file_type=file_type,
        raw_text=raw_text,
        context=context,
        channel="cli",
    )

    # Chunk and embed
    chunks_created = 0
    if result.status == "processed":
        row = conn.execute(
            f"SELECT id, raw_text FROM artifacts WHERE id = ?", [result.artifact_id]
        ).fetchone()
        if row:
            chunks = chunk_text(row[1], row[0])
            store_chunks(chunks, conn)
            embed_chunks(chunks)
            chunks_created = len(chunks)

    # Compute key rating
    key_rating = ""
    if ratings:
        first_key = list(ratings.keys())[0]
        key_rating = f"{ratings[first_key]['avg']}/10"

    return result, {
        "num_responses": num_responses,
        "key_rating": key_rating,
        "chunks": chunks_created,
        "ratings": ratings,
    }


def main():
    init_schema(DEFAULT_DB_PATH)
    conn = get_connection(DEFAULT_DB_PATH)

    results_table = []
    total_nodes_created = 0
    total_nodes_matched = 0
    total_edges = 0
    total_chunks = 0

    print("=" * 100)
    print("PROCESSING PHILIPS INTERNAL SESSION FEEDBACK FILES")
    print("=" * 100)

    for filename, event_name, date_str, org in FILES_TO_PROCESS:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            # Try to find by date prefix (handles non-breaking space issues)
            date_prefix = filename[:8]
            found = False
            for f in os.listdir(BASE_DIR):
                if f.startswith(date_prefix) and f.endswith(".xlsx") and event_name.split()[0].lower() in f.lower():
                    filepath = os.path.join(BASE_DIR, f)
                    filename = f
                    found = True
                    break
            if not found:
                # Try just by date prefix
                for f in os.listdir(BASE_DIR):
                    if f.startswith(date_prefix) and f.endswith(".xlsx"):
                        filepath = os.path.join(BASE_DIR, f)
                        filename = f
                        found = True
                        break
            if not found:
                print(f"  MISSING: {filename}")
                results_table.append({
                    "file": filename[:50],
                    "event": event_name[:40],
                    "date": date_str,
                    "responses": 0,
                    "rating": "N/A",
                    "status": "MISSING",
                    "nodes_created": 0,
                    "nodes_matched": 0,
                    "edges": 0,
                })
                continue

        print(f"\nProcessing: {filename}")
        result, info = process_file(filepath, event_name, date_str, org, conn, "xlsx")

        if result is None:
            print(f"  FAILED: {info}")
            results_table.append({
                "file": filename[:50],
                "event": event_name[:40],
                "date": date_str,
                "responses": 0,
                "rating": "N/A",
                "status": "FAILED",
                "nodes_created": 0,
                "nodes_matched": 0,
                "edges": 0,
            })
        else:
            status = result.status.upper()
            nc = result.nodes_created
            nm = result.nodes_matched
            ec = result.edges_created
            total_nodes_created += nc
            total_nodes_matched += nm
            total_edges += ec
            total_chunks += info.get("chunks", 0)
            print(f"  Status: {status} | Responses: {info['num_responses']} | Rating: {info['key_rating']} | Nodes: +{nc}/~{nm} | Edges: {ec} | Chunks: {info['chunks']}")
            results_table.append({
                "file": filename[:50],
                "event": event_name[:40],
                "date": date_str,
                "responses": info["num_responses"],
                "rating": info["key_rating"],
                "status": status,
                "nodes_created": nc,
                "nodes_matched": nm,
                "edges": ec,
            })

    print("\n" + "=" * 100)
    print("PROCESSING CSV FILES (checking for duplicates)")
    print("=" * 100)

    # Check for duplicates - look for existing artifacts with similar content
    for filename, event_name, date_str, org in CSV_FILES:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  MISSING: {filename}")
            results_table.append({
                "file": filename[:50],
                "event": event_name[:40],
                "date": date_str,
                "responses": 0,
                "rating": "N/A",
                "status": "MISSING",
                "nodes_created": 0,
                "nodes_matched": 0,
                "edges": 0,
            })
            continue

        # Check if xlsx version exists (possible duplicate)
        xlsx_check = conn.execute(
            "SELECT id, file_name FROM artifacts WHERE file_name LIKE ? OR file_name LIKE ?",
            [f"%{date_str.replace('-', '')}%{event_name[:15]}%", f"%{date_str.replace('-', '')}%"]
        ).fetchall()

        if xlsx_check:
            print(f"\n  POTENTIAL DUPLICATE: {filename}")
            print(f"    Existing: {[r[1] for r in xlsx_check]}")
            print(f"    Ingesting anyway (different format/source)")

        print(f"\nProcessing: {filename}")
        result, info = process_file(filepath, event_name, date_str, org, conn, "csv")

        if result is None:
            print(f"  FAILED: {info}")
            results_table.append({
                "file": filename[:50],
                "event": event_name[:40],
                "date": date_str,
                "responses": 0,
                "rating": "N/A",
                "status": "FAILED",
                "nodes_created": 0,
                "nodes_matched": 0,
                "edges": 0,
            })
        else:
            status = result.status.upper()
            nc = result.nodes_created
            nm = result.nodes_matched
            ec = result.edges_created
            total_nodes_created += nc
            total_nodes_matched += nm
            total_edges += ec
            total_chunks += info.get("chunks", 0)
            print(f"  Status: {status} | Responses: {info['num_responses']} | Rating: {info['key_rating']} | Nodes: +{nc}/~{nm} | Edges: {ec} | Chunks: {info['chunks']}")
            results_table.append({
                "file": filename[:50],
                "event": event_name[:40],
                "date": date_str,
                "responses": info["num_responses"],
                "rating": info["key_rating"],
                "status": status,
                "nodes_created": nc,
                "nodes_matched": nm,
                "edges": ec,
            })

    conn.close()

    # Print summary table
    print("\n\n" + "=" * 140)
    print("SUMMARY TABLE")
    print("=" * 140)
    print(f"{'#':<3} {'File':<52} {'Event':<42} {'Date':<12} {'Resp':<5} {'Rating':<8} {'Status':<10} {'N+':<4} {'N~':<4} {'E':<4}")
    print("-" * 140)
    for i, r in enumerate(results_table, 1):
        print(f"{i:<3} {r['file']:<52} {r['event']:<42} {r['date']:<12} {r['responses']:<5} {r['rating']:<8} {r['status']:<10} {r['nodes_created']:<4} {r['nodes_matched']:<4} {r['edges']:<4}")
    print("-" * 140)
    print(f"TOTALS: {len(results_table)} files | Nodes created: {total_nodes_created} | Nodes matched: {total_nodes_matched} | Edges: {total_edges} | Chunks: {total_chunks}")
    print("=" * 140)


if __name__ == "__main__":
    main()

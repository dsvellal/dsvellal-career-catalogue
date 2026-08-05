#!/usr/bin/env python3
"""
Process 92 Philips session feedback Excel files into structured JSON.
Extracts ratings, text feedback, dates, and categorizes each session.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from statistics import mean

import openpyxl

FEEDBACK_DIR = "/Users/dsvellal/Downloads/Website/Philips-Sessions-Feedback"
OUTPUT_DIR = "/Users/dsvellal/Code/dsvellal-personal-knowledge-context/data/evidence/sessions"

# Month name to number mapping
MONTH_MAP = {
    'jan': 1, 'january': 1, 'feb': 2, 'february': 2, 'mar': 3, 'march': 3,
    'apr': 4, 'april': 4, 'may': 5, 'jun': 6, 'june': 6,
    'jul': 7, 'july': 7, 'aug': 8, 'august': 8, 'sep': 9, 'sept': 9, 'september': 9,
    'oct': 10, 'october': 10, 'nov': 11, 'november': 11, 'dec': 12, 'december': 12
}


def extract_date_from_filename(filename):
    """Extract date from filename using various patterns."""
    name = filename.replace('.xlsx', '')

    # Pattern: YYYYMMDD at start like 20190415
    m = re.search(r'(\d{4})(\d{2})(\d{2})', name)
    if m and int(m.group(1)) >= 2018 and int(m.group(1)) <= 2026:
        year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year}-{month:02d}-{day:02d}"

    # Pattern: [Feedback] 20250312 ...
    m = re.match(r'\[Feedback\]\s*(\d{4})(\d{2})(\d{2})', name)
    if m:
        year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f"{year}-{month:02d}-{day:02d}"

    # Pattern: DDth Month YYYY or DDth Month Year
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{4})', name, re.IGNORECASE)
    if m:
        day = int(m.group(1))
        month = MONTH_MAP.get(m.group(2).lower()[:3], 0)
        year = int(m.group(3))
        if month and 1 <= day <= 31:
            return f"{year}-{month:02d}-{day:02d}"

    # Pattern: Dec-16-Workshop, Dec-17-Workshop, Dec-18
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(\d{1,2})', name, re.IGNORECASE)
    if m:
        month = MONTH_MAP.get(m.group(1).lower()[:3], 0)
        day = int(m.group(2))
        # Guess year from context - these Dec workshops are from 2024
        if 'Workshop' in name or 'Feedback' in name:
            return f"2024-{month:02d}-{day:02d}"

    # Pattern: just a year like "2018 -" or "2019 " or "2020 -"
    m = re.match(r'(\d{4})\s*[-.]', name)
    if m:
        year = int(m.group(1))
        if 2018 <= year <= 2026:
            return str(year)

    # Pattern: year somewhere in the name for older files
    m = re.search(r'20(18|19|20|21|22|23|24|25|26)', name)
    if m:
        year = int("20" + m.group(1))
        # Only return year if we can't get more specific
        return str(year)

    return "unknown"


def categorize_session(filename, questions=None):
    """Categorize session based on filename and content."""
    name = filename.lower()

    # Before-after comparison
    if 'jscpd before' in name or 'jscpd after' in name:
        return "before-after"

    # Connects / personal feedback about Datta
    if '.connects' in name or 'connects' in name:
        return "connects"
    if 'feedback about datta' in name or 'feedback for datta' in name or 'feedback to datta' in name:
        return "feedback-about-datta"
    if 'new hire mentoring' in name:
        return "feedback-about-datta"
    if 'pair.?programming.*feedback' in name or 'pair programming' in name:
        return "feedback-about-datta"
    if "feedback to dattaterya" in name or "feedback about the swcoe" in name:
        return "feedback-about-datta"
    if "tune observation" in name:
        return "feedback-about-datta"

    # Interview sessions
    if 'interview' in name or 'hiring' in name or 'panelist' in name:
        return "interview"

    # CoPilot / AI / GenAI
    if 'copilot' in name or 'co-pilot' in name or 'ai ' in name or 'ai-' in name or 'genai' in name:
        return "ai-genai"
    if 'context engineering' in name or 'agents' in name or 'elevate' in name:
        return "ai-genai"
    if 'prompt engineering' in name:
        return "ai-genai"

    # DORA
    if 'dora' in name or 'continuous value delivery' in name:
        return "dora"

    # CodeScene / Tech Debt
    if 'codescene' in name or 'tech debt' in name or 'tech-debt' in name:
        return "tech-debt"

    # Code quality sessions
    if 'code quality' in name or 'clean.?code' in name or 'code dojo' in name:
        return "code-quality"
    if 'code duplication' in name or 'jscpd' in name:
        return "code-quality"
    if 'unit test' in name or 'mutation test' in name or 'bdd' in name:
        return "code-quality"
    if 'behavior-driven' in name or 'best practices' in name:
        return "code-quality"
    if 'code review' in name or 'shift left' in name or 'back to basics' in name:
        return "code-quality"
    if 'i will code' in name or 'crafting code' in name:
        return "code-quality"

    # DORA / metrics
    if 'program behavior metrics' in name or 'observability' in name:
        return "dora"

    # Surveys / audience understanding (pre-session)
    if 'understanding' in name and 'audience' in name:
        return "other"
    if 'survey' in name and 'requirement' in name:
        return "other"

    # Other specific categories
    if 'microservices' in name or 'reliability' in name:
        return "code-quality"
    if 'traceability' in name:
        return "code-quality"
    if 'bar_skill raiser' in name or 'bar raiser' in name:
        return "interview"
    if 'github foundational' in name:
        return "ai-genai"
    if '62304' in name:
        return "code-quality"
    if 'analytics community' in name:
        return "ai-genai"
    if 'gdp engagement' in name or 'software excellence' in name or 'business interaction' in name:
        return "other"
    if 'grow' in name:
        return "ai-genai"

    return "other"


def is_numeric_rating(value, max_scale=10):
    """Check if a value is a numeric rating."""
    if value is None:
        return False
    try:
        v = float(value)
        return 1 <= v <= max_scale
    except (ValueError, TypeError):
        return False


def detect_rating_scale(values):
    """Detect whether ratings are on 1-5 or 1-10 scale."""
    numeric_vals = []
    for v in values:
        try:
            n = float(v)
            if 1 <= n <= 10:
                numeric_vals.append(n)
        except (ValueError, TypeError):
            continue

    if not numeric_vals:
        return None

    max_val = max(numeric_vals)
    if max_val <= 5:
        return 5
    return 10


def is_rating_column(header, values):
    """Determine if a column contains numeric ratings."""
    if header is None:
        return False

    header_str = str(header).lower()
    # Skip timestamp/ID columns
    skip_keywords = ['timestamp', 'id', 'email', 'name', 'date', 'time']
    for kw in skip_keywords:
        if kw in header_str:
            return False

    # Count numeric values in range
    numeric_count = 0
    total_non_empty = 0
    for v in values:
        if v is not None and str(v).strip():
            total_non_empty += 1
            try:
                n = float(v)
                if 1 <= n <= 10:
                    numeric_count += 1
            except (ValueError, TypeError):
                pass

    # If majority are numeric ratings
    if total_non_empty > 0 and numeric_count / total_non_empty >= 0.5:
        return True
    return False


def is_text_column(header, values):
    """Determine if a column contains meaningful text feedback."""
    if header is None:
        return False

    header_str = str(header).lower()
    # Skip timestamp/ID/metadata columns
    skip_keywords = ['timestamp', 'id', 'email address', 'start time', 'completion time',
                     'last modified', 'email id', 'repository link', 'what is your philips email',
                     'what is your code repository', 'command run']
    for kw in skip_keywords:
        if kw in header_str:
            return False

    # Check if values have meaningful text (not just numbers or short answers)
    text_count = 0
    for v in values:
        if v is not None:
            s = str(v).strip()
            if len(s) > 10 and not is_numeric_rating(v):
                text_count += 1

    return text_count > 0


def is_meaningful_feedback(text):
    """Filter out email content, metadata, and non-feedback text."""
    if not text or len(text) < 15:
        return False
    lower = text.lower()
    # Skip email-like content
    if '@philips.com' in lower and ('adding' in lower or 'cc' in lower or 'from:' in lower):
        return False
    # Skip URLs only
    if text.startswith('http') and ' ' not in text:
        return False
    # Skip entries that are just names/emails
    if '@' in text and len(text.split()) <= 5:
        return False
    return True


def extract_session_name(filename):
    """Extract a clean session name from the filename."""
    name = filename.replace('.xlsx', '')

    # Remove response count notation like (1-65)
    name = re.sub(r'\(\d+-\d+\)', '', name)

    # Remove [Feedback] prefix
    name = re.sub(r'\[.*?\]\s*', '', name)

    # Remove date prefixes like "DDth Month YYYY - "
    name = re.sub(r'\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4}\s*-\s*', '', name)

    # Remove YYYYMMDD prefix
    name = re.sub(r'^\d{8}\s*-?\s*', '', name)

    # Remove " (1)" duplicate suffix
    name = re.sub(r'\s*\(\d+\)\s*$', '', name)

    # Remove trailing " - Feedback" or "- Session Feedback"
    name = re.sub(r'\s*-?\s*(?:Session\s+)?Feedback\s*$', '', name, flags=re.IGNORECASE)

    # Remove leading/trailing whitespace and dashes
    name = name.strip(' -_')

    return name if name else filename.replace('.xlsx', '')


def process_file(filepath):
    """Process a single Excel file and extract all data."""
    filename = os.path.basename(filepath)
    result = {
        "filename": filename,
        "session_name": extract_session_name(filename),
        "date": extract_date_from_filename(filename),
        "response_count": 0,
        "questions": [],
        "ratings": {},
        "text_feedback": [],
        "category": "",
        "is_pre_session_survey": False,
        "is_duplicate": False,
        "raw_data_sample": []
    }

    # Mark duplicates
    if filename.endswith(' (1).xlsx'):
        result["is_duplicate"] = True

    # Mark pre-session surveys
    if 'understanding' in filename.lower() and 'audience' in filename.lower():
        result["is_pre_session_survey"] = True

    try:
        wb = openpyxl.load_workbook(filepath, data_only=True)
        ws = wb.active

        # Read all rows using max_row/max_column for reliable reading
        rows = []
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column, values_only=True):
            rows.append(row)
        wb.close()

        if not rows:
            return result

        # First row is headers
        headers = list(rows[0])
        data_rows = rows[1:]

        result["questions"] = [str(h) if h is not None else "" for h in headers]
        result["response_count"] = len(data_rows)

        # Extract date from data if not found in filename
        if result["date"] == "unknown" and data_rows:
            # Look for timestamp columns
            for col_idx, header in enumerate(headers):
                if header and any(kw in str(header).lower() for kw in ['start time', 'completion time', 'timestamp']):
                    for row in data_rows:
                        if col_idx < len(row) and row[col_idx] is not None:
                            val = row[col_idx]
                            if hasattr(val, 'strftime'):
                                # It's a datetime object
                                result["date"] = val.strftime("%Y-%m-%d")
                                break
                            elif isinstance(val, str):
                                # Try parsing string date
                                for fmt in ["%Y-%m-%d %H:%M:%S", "%m/%d/%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S"]:
                                    try:
                                        dt = datetime.strptime(val.split('.')[0], fmt)
                                        result["date"] = dt.strftime("%Y-%m-%d")
                                        break
                                    except ValueError:
                                        pass
                    if result["date"] != "unknown":
                        break

        # Process each column
        for col_idx, header in enumerate(headers):
            if header is None:
                continue

            # Get all values for this column
            col_values = [row[col_idx] if col_idx < len(row) else None for row in data_rows]

            # Check if it's a rating column
            if is_rating_column(header, col_values):
                numeric_vals = []
                for v in col_values:
                    try:
                        n = float(v)
                        if 1 <= n <= 10:
                            numeric_vals.append(n)
                    except (ValueError, TypeError):
                        pass

                if numeric_vals:
                    scale = detect_rating_scale(col_values)
                    result["ratings"][str(header)] = {
                        "avg": round(mean(numeric_vals), 2),
                        "min": min(numeric_vals),
                        "max": max(numeric_vals),
                        "count": len(numeric_vals),
                        "scale": scale
                    }

            # Check if it's a text feedback column
            elif is_text_column(header, col_values):
                for v in col_values:
                    if v is not None:
                        s = str(v).strip()
                        if is_meaningful_feedback(s):
                            result["text_feedback"].append({
                                "question": str(header),
                                "response": s
                            })

        # Store a sample of raw data (first 3 rows)
        for row in data_rows[:3]:
            sample = {}
            for idx, h in enumerate(headers):
                if h and idx < len(row) and row[idx] is not None:
                    sample[str(h)] = str(row[idx])
            if sample:
                result["raw_data_sample"].append(sample)

    except Exception as e:
        result["error"] = str(e)

    # Categorize
    result["category"] = categorize_session(filename)

    return result


def compute_summary(all_sessions):
    """Compute summary statistics across all sessions."""
    summary = {
        "total_files": len(all_sessions),
        "total_sessions_excluding_duplicates_and_surveys": 0,
        "total_responses": 0,
        "sessions_by_year": {},
        "sessions_by_category": {},
        "overall_ratings": {
            "all_averages": [],
            "normalized_to_5_scale": []
        },
        "top_quotes": [],
        "before_after_comparison": {},
        "sessions_with_errors": [],
        "pre_session_surveys": [],
        "duplicates": []
    }

    all_text_feedback = []
    all_rating_avgs = []

    for session in all_sessions:
        if session.get("is_duplicate"):
            summary["duplicates"].append(session["filename"])
            continue
        if session.get("is_pre_session_survey"):
            summary["pre_session_surveys"].append(session["filename"])

        summary["total_sessions_excluding_duplicates_and_surveys"] += 1
        summary["total_responses"] += session["response_count"]

        if session.get("error"):
            summary["sessions_with_errors"].append({
                "filename": session["filename"],
                "error": session["error"]
            })

        # Year breakdown
        date_str = session["date"]
        year = "unknown"
        if date_str and date_str != "unknown":
            year = date_str[:4]
        summary["sessions_by_year"][year] = summary["sessions_by_year"].get(year, 0) + 1

        # Category breakdown
        cat = session["category"]
        summary["sessions_by_category"][cat] = summary["sessions_by_category"].get(cat, 0) + 1

        # Collect ratings
        for q, rating_data in session["ratings"].items():
            avg = rating_data["avg"]
            scale = rating_data.get("scale", 5)
            all_rating_avgs.append(avg)
            # Normalize to 5-point scale
            if scale == 10:
                normalized = avg / 2
            else:
                normalized = avg
            summary["overall_ratings"]["normalized_to_5_scale"].append(normalized)

        # Collect text feedback
        for fb in session["text_feedback"]:
            all_text_feedback.append({
                "session": session["session_name"],
                "date": session["date"],
                "question": fb["question"],
                "response": fb["response"]
            })

    # Calculate overall rating stats
    if summary["overall_ratings"]["normalized_to_5_scale"]:
        norm_ratings = summary["overall_ratings"]["normalized_to_5_scale"]
        summary["overall_ratings"]["grand_average_normalized_5_scale"] = round(mean(norm_ratings), 2)
        summary["overall_ratings"]["total_rating_data_points"] = len(norm_ratings)
        summary["overall_ratings"]["min_normalized"] = round(min(norm_ratings), 2)
        summary["overall_ratings"]["max_normalized"] = round(max(norm_ratings), 2)

    if all_rating_avgs:
        summary["overall_ratings"]["grand_average_raw"] = round(mean(all_rating_avgs), 2)

    # Remove the raw lists from final output
    del summary["overall_ratings"]["all_averages"]
    del summary["overall_ratings"]["normalized_to_5_scale"]

    # Select top quotes (longer, more substantive feedback)
    # Filter out trivial responses and email-like content
    substantive_quotes = []
    for fb in all_text_feedback:
        resp = fb["response"]
        lower_resp = resp.lower().strip()
        # Skip trivial or non-feedback text
        if len(resp) < 30:
            continue
        if lower_resp.startswith(('yes', 'no', 'na', 'n/a', 'none', 'nothing', 'good', 'ok', 'nil')):
            continue
        # Skip email-like content (contains multiple @philips.com references)
        if resp.count('@philips.com') > 1:
            continue
        # Skip content that looks like meeting notes / forwards
        if 'from:' in lower_resp and 'sent:' in lower_resp:
            continue
        substantive_quotes.append(fb)

    # Sort by a quality heuristic: prefer medium-length, diverse sessions
    # Longer is not always better (email chains are long); prefer 30-300 char range
    def quote_quality(fb):
        length = len(fb["response"])
        # Sweet spot is 50-300 characters
        if 50 <= length <= 300:
            return 3
        elif 30 <= length <= 500:
            return 2
        else:
            return 1

    substantive_quotes.sort(key=lambda x: (-quote_quality(x), -len(x["response"])))

    # Pick diverse quotes across sessions (max 3 per session)
    selected_quotes = []
    session_counts = {}
    for fb in substantive_quotes:
        session_key = fb["session"]
        if session_counts.get(session_key, 0) >= 3:
            continue
        selected_quotes.append(fb)
        session_counts[session_key] = session_counts.get(session_key, 0) + 1
        if len(selected_quotes) >= 50:
            break

    summary["top_quotes"] = selected_quotes

    # Before/After comparison
    before_session = None
    after_session = None
    for session in all_sessions:
        if 'before elimination' in session["filename"].lower():
            before_session = session
        elif 'after elimination' in session["filename"].lower():
            after_session = session

    if before_session and after_session:
        summary["before_after_comparison"] = {
            "before": {
                "filename": before_session["filename"],
                "response_count": before_session["response_count"],
                "ratings": before_session["ratings"],
                "text_feedback_sample": before_session["text_feedback"][:5]
            },
            "after": {
                "filename": after_session["filename"],
                "response_count": after_session["response_count"],
                "ratings": after_session["ratings"],
                "text_feedback_sample": after_session["text_feedback"][:5]
            },
            "interpretation": "JSCPD code duplication - feedback collected before elimination (baseline metrics) and after elimination (effectiveness ratings). The 'before' file captures baseline duplication data while 'after' captures session effectiveness ratings."
        }

    return summary


def main():
    feedback_dir = Path(FEEDBACK_DIR)
    output_dir = Path(OUTPUT_DIR)

    # Get all xlsx files
    xlsx_files = sorted(feedback_dir.glob("*.xlsx"))
    print(f"Found {len(xlsx_files)} Excel files to process")

    all_sessions = []
    for i, filepath in enumerate(xlsx_files):
        print(f"Processing [{i+1}/{len(xlsx_files)}]: {filepath.name}")
        session_data = process_file(str(filepath))
        all_sessions.append(session_data)

    # Write all sessions data
    output_file = output_dir / "all_sessions_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_sessions, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nWritten all sessions data to: {output_file}")

    # Compute and write summary
    summary = compute_summary(all_sessions)
    summary_file = output_dir / "summary_stats.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False, default=str)
    print(f"Written summary stats to: {summary_file}")

    # Print key stats
    print(f"\n{'='*60}")
    print(f"PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"Total files processed: {summary['total_files']}")
    print(f"Sessions (excl duplicates/surveys): {summary['total_sessions_excluding_duplicates_and_surveys']}")
    print(f"Total responses: {summary['total_responses']}")
    print(f"Sessions by year: {json.dumps(summary['sessions_by_year'], indent=2)}")
    print(f"Sessions by category: {json.dumps(summary['sessions_by_category'], indent=2)}")
    if 'grand_average_normalized_5_scale' in summary['overall_ratings']:
        print(f"Grand average rating (normalized to 5-point): {summary['overall_ratings']['grand_average_normalized_5_scale']}")
    print(f"Duplicates found: {len(summary['duplicates'])}")
    print(f"Pre-session surveys: {len(summary['pre_session_surveys'])}")
    if summary['sessions_with_errors']:
        print(f"Files with errors: {len(summary['sessions_with_errors'])}")
        for err in summary['sessions_with_errors']:
            print(f"  - {err['filename']}: {err['error']}")


if __name__ == "__main__":
    main()

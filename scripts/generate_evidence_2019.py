"""Generate individual evidence files for all 2019 emails."""

import re
from pathlib import Path

from twin.ingestion.extractors import extract


def slugify(text: str) -> str:
    """Create a filesystem-safe slug from text."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def extract_sender_name(from_field: str) -> str:
    """Extract clean name from email From field."""
    match = re.match(r'"?([^"<]+)"?\s*<?', from_field)
    if match:
        name = match.group(1).strip().rstrip(";").strip()
        return name
    return from_field.strip()


def identify_datta_role(text: str, date: str) -> str:
    """Identify Datta's role based on email content and date."""
    if "Competency Specialist" in text or "Software Center of Excellence" in text:
        return "Competency Specialist – Software Excellence, Software Center of Excellence"
    if "Senior Architect" in text and "IDM" in text:
        return "Senior Architect, IDM"
    if "Project Architect" in text:
        return "Project Architect, IDM"
    # Date-based fallback
    if date and date[:7] >= "2019-07":
        return "Competency Specialist – Software Excellence, Software Center of Excellence"
    return "Project Architect, IDM"


def categorize_email(subject: str, text: str) -> str:
    """Categorize the email by theme."""
    subject_lower = subject.lower()
    text_lower = text.lower()

    if "jscpd" in subject_lower or "duplication" in subject_lower or "duplicate" in subject_lower:
        return "Code Duplication / JSCPD"
    if "interview" in subject_lower or "hiring" in subject_lower or "f2f" in subject_lower or "campus" in subject_lower:
        return "Interview Process & Hiring"
    if "recognition" in subject_lower or "praise" in subject_lower or "kudos" in subject_lower or "thank" in subject_lower:
        return "Recognition & Appreciation"
    if "workshop" in subject_lower or "session" in subject_lower or "bootcamp" in subject_lower:
        return "Workshops & Technical Sessions"
    if "code quality" in subject_lower or "clean code" in subject_lower or "code live" in subject_lower:
        return "Code Quality"
    if "devops" in subject_lower or "jenkins" in subject_lower or "ci" in subject_lower or "pipeline" in subject_lower:
        return "CI/CD & DevOps"
    if "sig" in subject_lower or "tech debt" in subject_lower or "technical debt" in subject_lower or "tics" in subject_lower:
        return "Technical Debt"
    if "beqr" in subject_lower or "best practices" in subject_lower or "excellence" in subject_lower:
        return "BEQR & Best Practices"
    if "announcement" in subject_lower or "swcoe" in subject_lower:
        return "Role & Organization"
    if "agile" in subject_lower or "transformation" in subject_lower:
        return "Agile Transformation"
    if "connect" in subject_lower or "introducing" in subject_lower or "engagement" in subject_lower:
        return "Cross-BU Engagement"
    if "feedback" in subject_lower or "culture" in subject_lower:
        return "Feedback & Culture"
    if "workday" in subject_lower:
        return "HR / Administrative"
    if "story" in subject_lower and "noreply" in text_lower:
        return "Project Tracking (TFS)"
    return "General / Other"


def determine_datta_involvement(from_field: str, to_field: str, cc_field: str, text: str) -> str:
    """Determine how Datta is involved in this email."""
    datta_patterns = ["dsvellal", "Vellal, Dattatreya", "Vellal; Dattatreya", "Subramanya Vellal"]

    is_sender = any(p.lower() in from_field.lower() for p in datta_patterns)
    is_direct_recipient = any(p.lower() in to_field.lower() for p in datta_patterns)
    is_cc = any(p.lower() in cc_field.lower() for p in datta_patterns)
    mentions_datta = "datta" in text.lower() and not is_sender

    if is_sender:
        return "Author"
    if is_direct_recipient and mentions_datta:
        return "Direct recipient — explicitly mentioned/praised"
    if is_direct_recipient:
        return "Direct recipient"
    if is_cc and mentions_datta:
        return "CC'd — explicitly mentioned"
    if is_cc:
        return "CC'd for visibility"
    if mentions_datta:
        return "Mentioned by name"
    return "Part of distribution list"


def extract_key_quotes(text: str) -> list[str]:
    """Extract notable quotes that mention Datta or show appreciation."""
    quotes = []
    lines = text.split("\n")
    datta_keywords = ["datta", "dattatreya", "vellal", "thank", "kudos", "great", "appreciate",
                      "excellent", "amazing", "impressed", "wonderful", "good job", "well done",
                      "backbone", "immense", "brilliant"]

    for i, line in enumerate(lines):
        line_lower = line.lower().strip()
        if not line_lower or line_lower.startswith("---") or line_lower.startswith("subject:"):
            continue
        if any(kw in line_lower for kw in datta_keywords):
            clean_line = line.strip()
            if 10 < len(clean_line) < 500 and clean_line not in quotes:
                quotes.append(clean_line)
                if len(quotes) >= 5:
                    break
    return quotes


def generate_evidence(path: Path, output_dir: Path, index: int) -> dict | None:
    """Generate an evidence markdown file for a single email."""
    try:
        result = extract(path)
    except Exception as e:
        return {"file": path.name, "error": str(e)}

    meta = result.metadata
    subject = meta.get("subject", path.stem)
    from_field = meta.get("from", "")
    to_field = meta.get("to", "")
    cc_field = meta.get("cc", "")
    date = meta.get("date", "")
    date_short = date[:10] if date else "unknown"

    slug = slugify(subject) or slugify(path.stem)
    filename = f"{index:03d}-{slug}.md"
    output_path = output_dir / filename

    sender_name = extract_sender_name(from_field)
    category = categorize_email(subject, result.text)
    datta_role = identify_datta_role(result.text, date)
    involvement = determine_datta_involvement(from_field, to_field, cc_field, result.text)
    key_quotes = extract_key_quotes(result.text)

    thread_depth = meta.get("thread_depth", 1)
    is_reply = meta.get("is_reply", False)
    attachments = meta.get("attachments", [])

    # Build markdown
    lines = []
    lines.append(f"# Evidence: {subject}")
    lines.append("")
    lines.append("## Source")
    lines.append(f"- **File:** `{path.name}`")
    lines.append(f"- **Date:** {date_short}")
    lines.append(f"- **Ingested:** 2026-08-04")
    lines.append(f"- **Channel:** email_archive")
    lines.append(f"- **Category:** {category}")
    lines.append("")
    lines.append("## Email Metadata")
    lines.append(f"- **From:** {from_field}")
    lines.append(f"- **To:** {to_field}")
    if cc_field:
        lines.append(f"- **CC:** {cc_field}")
    lines.append(f"- **Date:** {date}")
    lines.append(f"- **Thread depth:** {thread_depth}")
    lines.append(f"- **Is reply:** {is_reply}")
    if attachments:
        lines.append(f"- **Attachments:** {len(attachments)}")
        for att in attachments:
            lines.append(f"  - `{att['filename']}` ({att['content_type']}, {att['size_bytes']} bytes)")
    lines.append("")
    lines.append("## Datta's Involvement")
    lines.append(f"- **Role at time:** {datta_role}")
    lines.append(f"- **Involvement type:** {involvement}")
    lines.append("")

    if key_quotes:
        lines.append("## Key Quotes")
        for q in key_quotes:
            lines.append(f"> {q}")
            lines.append("")

    lines.append("## Full Email Content")
    lines.append("")
    lines.append("```")
    # Truncate very long emails but keep meaningful content
    content = result.text
    if len(content) > 5000:
        content = content[:5000] + "\n\n[... truncated, full content in database ...]"
    lines.append(content)
    lines.append("```")

    output_path.write_text("\n".join(lines), encoding="utf-8")

    return {
        "file": path.name,
        "evidence_file": filename,
        "subject": subject,
        "date": date_short,
        "category": category,
        "involvement": involvement,
    }


def main():
    base = Path("/Users/dsvellal/Downloads/Website/Appreciation Emails/2019")
    output_dir = Path("data/evidence/2019/individual")
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(base.glob("*.msg"))
    print(f"Processing {len(files)} emails...\n")

    results = []
    errors = []

    for i, f in enumerate(files, 1):
        info = generate_evidence(f, output_dir, i)
        if info and "error" in info:
            errors.append(info)
            print(f"  [{i:3d}] ERROR: {info['file'][:60]} -> {info['error']}")
        elif info:
            results.append(info)
            print(f"  [{i:3d}] {info['category']:<30} | {info['involvement']:<35} | {info['subject'][:50]}")

    print(f"\n{'='*80}")
    print(f"Generated: {len(results)} evidence files")
    print(f"Errors: {len(errors)}")
    print(f"Output: {output_dir}/")

    # Category breakdown
    categories = {}
    for r in results:
        cat = r["category"]
        categories[cat] = categories.get(cat, 0) + 1

    print(f"\nCategory breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")

    # Generate category index
    index_path = output_dir / "_INDEX.md"
    index_lines = ["# 2019 Individual Evidence Files\n"]
    index_lines.append(f"**Total:** {len(results)} evidence files from {len(files)} source emails\n")

    current_cat = ""
    for r in sorted(results, key=lambda x: (x["category"], x["date"])):
        if r["category"] != current_cat:
            current_cat = r["category"]
            index_lines.append(f"\n## {current_cat}\n")
            index_lines.append("| # | Date | Subject | Datta's Role | Evidence File |")
            index_lines.append("|---|------|---------|--------------|---------------|")
        index_lines.append(
            f"| | {r['date']} | {r['subject'][:60]} | {r['involvement'][:30]} | [{r['evidence_file']}]({r['evidence_file']}) |"
        )

    index_path.write_text("\n".join(index_lines), encoding="utf-8")
    print(f"\nIndex written: {index_path}")


if __name__ == "__main__":
    main()

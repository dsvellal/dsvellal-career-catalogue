"""Enrich email artifacts with classification, chunks, nodes, and edges.

Uses rule-based entity extraction from structured email metadata and content,
eliminating the need for an external LLM API call.
"""

import json
import re
import uuid
from pathlib import Path

import duckdb

from twin.db import get_connection
from twin.ingestion.classifier import ClassificationResult
from twin.ingestion.edges import create_edges
from twin.ingestion.resolver import resolve
from twin.retrieval.chunker import chunk_text, store_chunks


def extract_people_from_email(metadata: dict, text: str) -> list[dict]:
    """Extract people and their roles from email fields and content."""
    people = []
    seen_names = set()

    def add_person(name: str, role: str):
        clean = name.strip().strip('"').strip()
        clean = re.sub(r"\s*<[^>]+>", "", clean)
        clean = re.sub(r"\s*\([^)]*\)", "", clean)
        clean = clean.replace(";", ",").strip().strip(",").strip()
        if not clean or len(clean) < 3 or "@" in clean or clean.lower() in seen_names:
            return
        if "philips" in clean.lower() or "noreply" in clean.lower():
            return
        seen_names.add(clean.lower())
        people.append({"name": clean, "role": role})

    from_field = metadata.get("from", "")
    to_field = metadata.get("to", "")
    cc_field = metadata.get("cc", "")

    for match in re.finditer(r'"([^"]+)"', from_field):
        add_person(match.group(1), "sender")

    for match in re.finditer(r'"([^"]+)"', to_field):
        name = match.group(1)
        if "vellal" not in name.lower() and "dsvellal" not in name.lower():
            add_person(name, "recipient")

    for match in re.finditer(r'"([^"]+)"', cc_field):
        name = match.group(1)
        if "vellal" not in name.lower() and "dsvellal" not in name.lower():
            add_person(name, "cc")

    return people


def extract_skills_from_text(text: str) -> list[str]:
    """Extract skills/technologies mentioned in email content."""
    skill_patterns = {
        "CI/CD": r"\bci[/-]?cd\b",
        "Jenkins": r"\bjenkins\b",
        "GitHub Actions": r"\bgithub actions?\b",
        "GitHub Copilot": r"\b(?:github )?copilot\b",
        "DevOps": r"\bdevops\b",
        "Docker": r"\bdocker\b",
        "Kubernetes": r"\bkubernetes\b|k8s",
        "Java": r"\bjava\b",
        "Python": r"\bpython\b",
        "Kotlin": r"\bkotlin\b",
        "JavaScript": r"\bjavascript\b|node\.?js",
        "Unit Testing": r"\bunit test",
        "Test Automation": r"\btest automation\b",
        "SonarQube": r"\bsonarqube\b|sonarlint",
        "CodeScene": r"\bcodescene\b",
        "JSCPD": r"\bjscpd\b",
        "Code Review": r"\bcode review\b|pair review",
        "Pair Programming": r"\bpair program",
        "TDD": r"\btdd\b|test.driven",
        "Agile": r"\bagile\b|scrum|kanban",
        "Microservices": r"\bmicro.?service",
        "Architecture": r"\barchitect",
        "Technical Debt": r"\btech.?debt|technical debt",
        "SBOM": r"\bsbom\b",
        "BlackDuck": r"\bblack\s?duck\b",
        "Coverity": r"\bcoverity\b",
        "TICS": r"\btics\b",
        "ELK": r"\belk\b|elasticsearch",
        "Static Analysis": r"\bstatic.?(?:code )?analysis\b",
        "Dynamic Analysis": r"\bdynamic analysis\b",
        "Mutation Testing": r"\bmutation test",
        "InnerSource": r"\binner.?source\b",
        "Open Source": r"\bopen.?source\b",
        "IEC 62304": r"\b62304\b|iec.?62304",
        "DORA Metrics": r"\bdora\b",
        "AI/GenAI": r"\bgen.?ai\b|generative ai|\bartificial intelligence\b",
        "LLM": r"\bllm\b|large language model",
        "Prompt Engineering": r"\bprompt engineer",
        "Machine Learning": r"\bmachine learning\b|\bml\b",
        "Workshop Facilitation": r"\bworkshop\b",
        "Technical Leadership": r"\btechnical lead",
        "Mentoring": r"\bmentor",
        "Interview Design": r"\binterview\b.*\b(?:process|standard|design)\b",
    }

    text_lower = text.lower()
    found = []
    for skill, pattern in skill_patterns.items():
        if re.search(pattern, text_lower):
            found.append(skill)
    return found


def extract_projects_from_text(text: str) -> list[str]:
    """Extract project names from email content."""
    project_patterns = {
        "IDM": r"\bidm\b",
        "HSOP": r"\bhsop\b",
        "HSDP": r"\bhsdp\b",
        "IGT": r"\bigt\b",
        "SaaS DevOps Pipeline": r"\bsaas\b.*\bpipeline\b|\bdevops pipeline\b",
        "JSCPD Initiative": r"\bjscpd\b.*\b(?:workshop|session|initiative)\b",
        "Bar Raiser Program": r"\bbar.?raiser\b",
        "Quality@Desk": r"\bquality.?@.?desk\b|qad\b",
        "Software Excellence Conference": r"\bsw(?:coe)?\s*(?:excellence)?\s*conference\b",
        "BEQR": r"\bbeqr\b",
        "Bootcamp": r"\bbootcamp\b",
        "Clean Code": r"\bclean code\b",
        "Back2Basics": r"\bback.?2.?basics\b",
        "CodeScene Adoption": r"\bcodescene\b.*\b(?:adopt|integrat)\b",
        "SonarQube Integration": r"\bsonarqube\b.*\bintegrat",
        "Sutra": r"\bsutra\b",
        "Kairos": r"\bkairos\b",
        "ReqSpec": r"\breqspec\b",
        "XITE": r"\bxite\b",
        "Developer Days": r"\bdeveloper days\b",
        "GROW 3.0": r"\bgrow\s*3\.?0\b",
        "EPS-AD": r"\beps.?ad\b",
        "Ultrasound": r"\bultrasound\b",
        "MR": r"\bmagnetic resonance\b|\b(?:^|\s)mr\s",
        "GDP Software Track": r"\bgdp\b.*\bsoftware\b",
    }

    text_lower = text.lower()
    found = []
    for project, pattern in project_patterns.items():
        if re.search(pattern, text_lower):
            found.append(project)
    return found


def classify_email_type(subject: str, text: str, metadata: dict) -> str:
    """Determine email type from content."""
    subject_lower = subject.lower()
    text_lower = text.lower()

    if any(kw in subject_lower for kw in ["recognition", "kudos", "thank", "praise", "appreciate", "congrat"]):
        return "email_appreciation"
    if any(kw in subject_lower for kw in ["certificate", "milestone", "award"]):
        return "certificate"
    if any(kw in subject_lower for kw in ["announcement", "announce"]):
        return "email_appreciation"
    if "nps" in subject_lower and ("10" in subject_lower or "9" in subject_lower):
        return "email_appreciation"
    if any(kw in text_lower[:500] for kw in ["thank you", "great work", "well done", "kudos", "bulls eye"]):
        return "email_appreciation"
    if any(kw in subject_lower for kw in ["workshop", "session", "training"]):
        return "presentation"
    if any(kw in subject_lower for kw in ["meeting", "mom", "minutes", "standup"]):
        return "meeting_notes"
    if "story " in subject_lower or "noreply-tfs" in metadata.get("from", "").lower():
        return "project_doc"
    return "other"


def extract_claims(text: str, subject: str, metadata: dict) -> list[str]:
    """Extract specific claims/achievements from text."""
    claims = []
    text_lower = text.lower()

    praise_patterns = [
        r"(?:thank|thanks)\s+(?:you\s+)?(?:for|to)\s+(.{20,100}?)(?:\.|!|$)",
        r"(?:great|excellent|wonderful|fantastic|impressive)\s+(.{10,80}?)(?:\.|!|$)",
        r"(?:kudos|appreciation)\s+(?:for|to|on)\s+(.{10,100}?)(?:\.|!|$)",
        r"(?:congratulations?)\s+(?:for|on|to)\s+(.{10,100}?)(?:\.|!|$)",
    ]

    for pattern in praise_patterns:
        matches = re.findall(pattern, text_lower[:3000])
        for m in matches[:2]:
            clean = m.strip()
            if len(clean) > 15:
                claims.append(clean)

    if "nps" in subject.lower() and ("10" in subject or "9" in subject):
        claims.append(f"Achieved {subject}")

    return claims[:5]


def extract_dates(metadata: dict) -> list[dict]:
    """Extract dates from email metadata."""
    dates = []
    date_str = metadata.get("date", "")
    if date_str:
        iso_match = re.search(r"(\d{4}-\d{2}-\d{2})", date_str)
        if iso_match:
            dates.append({"date": iso_match.group(1), "context": "email date"})
        else:
            date_match = re.search(
                r"(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s+(\d{1,2}\s+\w+\s+\d{4})", date_str
            )
            if date_match:
                dates.append({"date": date_match.group(0), "context": "email date"})
    return dates


def enrich_artifact(artifact_id: str, conn: duckdb.DuckDBPyConnection) -> dict:
    """Classify, resolve, chunk, and link a single artifact."""
    row = conn.execute(
        "SELECT raw_text, metadata, file_name, file_type FROM artifacts WHERE id = ?",
        [artifact_id],
    ).fetchone()

    if not row:
        return {"status": "not_found"}

    text, metadata_json, file_name, file_type = row
    metadata = json.loads(metadata_json) if metadata_json else {}
    subject = metadata.get("subject", file_name)

    # Classify
    people = extract_people_from_email(metadata, text)
    skills = extract_skills_from_text(text)
    projects = extract_projects_from_text(text)
    doc_type = classify_email_type(subject, text, metadata)
    claims = extract_claims(text, subject, metadata)
    dates = extract_dates(metadata)

    classification = ClassificationResult(
        type=doc_type,
        dates=dates,
        projects=projects,
        skills=skills,
        people=people,
        organizations=[{"name": "Philips", "role": "employer"}],
        claims=claims,
        confidence=0.85,
    )

    # Resolve entities → create nodes
    resolution = resolve(classification, conn)

    # Create edges
    edges_created = create_edges(resolution, classification, artifact_id, conn)

    # Chunk text
    chunks = chunk_text(text, artifact_id)
    chunks_stored = store_chunks(chunks, conn) if chunks else 0

    # Update classification in artifacts table
    classification_dict = {
        "type": classification.type,
        "dates": classification.dates,
        "projects": classification.projects,
        "skills": classification.skills,
        "people": classification.people,
        "organizations": classification.organizations,
        "claims": classification.claims,
        "confidence": classification.confidence,
    }
    conn.execute(
        "UPDATE artifacts SET classification = ? WHERE id = ?",
        [json.dumps(classification_dict), artifact_id],
    )

    return {
        "status": "enriched",
        "nodes_created": len(resolution.nodes_created),
        "nodes_matched": len(resolution.nodes_matched),
        "edges_created": edges_created,
        "chunks_stored": chunks_stored,
        "type": doc_type,
        "people": len(people),
        "skills": len(skills),
        "projects": len(projects),
        "claims": len(claims),
    }


def main():
    conn = get_connection()

    # Get all email artifacts that need enrichment
    artifacts = conn.execute("""
        SELECT id, file_name FROM artifacts
        WHERE source_channel = 'email_archive'
        ORDER BY file_name
    """).fetchall()

    print(f"Enriching {len(artifacts)} email artifacts...\n")

    totals = {
        "enriched": 0,
        "nodes_created": 0,
        "nodes_matched": 0,
        "edges_created": 0,
        "chunks_stored": 0,
    }

    for i, (artifact_id, file_name) in enumerate(artifacts, 1):
        result = enrich_artifact(artifact_id, conn)
        if result["status"] == "enriched":
            totals["enriched"] += 1
            totals["nodes_created"] += result["nodes_created"]
            totals["nodes_matched"] += result["nodes_matched"]
            totals["edges_created"] += result["edges_created"]
            totals["chunks_stored"] += result["chunks_stored"]

            if i % 50 == 0 or i <= 5:
                print(
                    f"  [{i:3d}] {file_name[:50]:<50} "
                    f"nodes:{result['nodes_created']}+{result['nodes_matched']} "
                    f"edges:{result['edges_created']} chunks:{result['chunks_stored']} "
                    f"type:{result['type']}"
                )

    print(f"\n{'='*60}")
    print(f"ENRICHMENT COMPLETE")
    print(f"{'='*60}")
    print(f"  Artifacts enriched: {totals['enriched']}")
    print(f"  Nodes created: {totals['nodes_created']}")
    print(f"  Nodes matched: {totals['nodes_matched']}")
    print(f"  Edges created: {totals['edges_created']}")
    print(f"  Chunks stored: {totals['chunks_stored']}")

    # Final stats
    total_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
    total_edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    total_chunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    print(f"\n  Total nodes in graph: {total_nodes}")
    print(f"  Total edges in graph: {total_edges}")
    print(f"  Total chunks in DB: {total_chunks}")


if __name__ == "__main__":
    main()

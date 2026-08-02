"""Portfolio site generator: static HTML from knowledge graph snapshot."""

import json
from dataclasses import dataclass, field
from pathlib import Path

import duckdb

from twin.retrieval.graph import build_graph, search_by_type


@dataclass
class PortfolioData:
    projects: list[dict] = field(default_factory=list)
    skills: list[dict] = field(default_factory=list)
    achievements: list[dict] = field(default_factory=list)
    organizations: list[dict] = field(default_factory=list)
    stats: dict = field(default_factory=dict)


def extract_portfolio_data(conn: duckdb.DuckDBPyConnection) -> PortfolioData:
    """Extract published data from the knowledge graph for portfolio generation."""
    graph = build_graph(conn)

    projects = []
    for node in search_by_type(graph, "project"):
        row = conn.execute(
            "SELECT properties, description FROM nodes WHERE id = ?", [node["id"]]
        ).fetchone()
        props = json.loads(row[0]) if row and row[0] else {}
        projects.append(
            {
                **node,
                "description": row[1] if row else "",
                "status": props.get("status", ""),
                "tech_stack": props.get("tech_stack", []),
            }
        )

    skills = []
    for node in search_by_type(graph, "skill"):
        row = conn.execute("SELECT properties FROM nodes WHERE id = ?", [node["id"]]).fetchone()
        props = json.loads(row[0]) if row and row[0] else {}
        skills.append(
            {
                **node,
                "category": props.get("category", "technical"),
                "proficiency": props.get("proficiency", "competent"),
            }
        )

    achievements = [n for n in search_by_type(graph, "achievement")]
    organizations = [n for n in search_by_type(graph, "organization")]

    stats = {
        "total_nodes": graph.number_of_nodes(),
        "total_edges": graph.number_of_edges(),
        "projects": len(projects),
        "skills": len(skills),
        "achievements": len(achievements),
    }

    return PortfolioData(
        projects=projects,
        skills=skills,
        achievements=achievements,
        organizations=organizations,
        stats=stats,
    )


def generate_portfolio_html(data: PortfolioData, output_dir: Path) -> Path:
    """Generate a static portfolio site from extracted data."""
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "index.html"

    skills_html = "".join(f'<span class="skill-tag">{s["name"]}</span>' for s in data.skills)
    projects_html = "".join(
        f'<div class="project-card"><h3>{p["name"]}</h3><p>{p.get("description", "")}</p></div>'
        for p in data.projects
    )
    achievements_html = "".join(f"<li>{a['name']}</li>" for a in data.achievements)

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Datta Vellal — Portfolio</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
               line-height: 1.6; color: #1a1a1a; max-width: 900px; margin: 0 auto; padding: 2rem; }}
        header {{ text-align: center; padding: 3rem 0; border-bottom: 1px solid #eee; }}
        header h1 {{ font-size: 2.5rem; color: #2c3e50; }}
        header p {{ color: #6c757d; font-size: 1.125rem; margin-top: 0.5rem; }}
        section {{ padding: 2rem 0; }}
        h2 {{ color: #2c3e50; margin-bottom: 1rem; font-size: 1.5rem; }}
        .skill-tag {{ display: inline-block; background: #e8f4f8; color: #2c3e50;
                     padding: 0.3rem 0.8rem; border-radius: 15px; margin: 0.25rem;
                     font-size: 0.875rem; }}
        .project-card {{ background: #f8f9fa; border-radius: 8px; padding: 1.25rem;
                        margin-bottom: 1rem; border-left: 3px solid #2c3e50; }}
        .project-card h3 {{ margin-bottom: 0.5rem; }}
        .stats {{ display: flex; gap: 2rem; justify-content: center; padding: 1.5rem;
                 background: #f8f9fa; border-radius: 8px; margin: 1rem 0; }}
        .stat {{ text-align: center; }}
        .stat .num {{ font-size: 1.75rem; font-weight: 700; color: #2c3e50; }}
        .stat .label {{ font-size: 0.8rem; color: #6c757d; text-transform: uppercase; }}
        footer {{ text-align: center; padding: 2rem 0; color: #6c757d; font-size: 0.85rem;
                 border-top: 1px solid #eee; margin-top: 2rem; }}
    </style>
</head>
<body>
    <header>
        <h1>Datta Vellal</h1>
        <p>Software Engineer &bull; Knowledge Systems &bull; ML Engineering</p>
    </header>

    <div class="stats">
        <div class="stat"><div class="num">{data.stats.get("projects", 0)}</div>\
<div class="label">Projects</div></div>
        <div class="stat"><div class="num">{data.stats.get("skills", 0)}</div>\
<div class="label">Skills</div></div>
        <div class="stat"><div class="num">{data.stats.get("achievements", 0)}</div>\
<div class="label">Achievements</div></div>
    </div>

    <section id="skills">
        <h2>Skills</h2>
        <div>{skills_html or "<p>No skills indexed yet.</p>"}</div>
    </section>

    <section id="projects">
        <h2>Projects</h2>
        {projects_html or "<p>No projects indexed yet.</p>"}
    </section>

    <section id="achievements">
        <h2>Achievements</h2>
        <ul>{achievements_html or "<li>No achievements indexed yet.</li>"}</ul>
    </section>

    <footer>
        Generated by Twin &mdash; Personal Knowledge Context System
    </footer>
</body>
</html>"""

    index_path.write_text(html)
    return index_path

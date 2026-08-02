"""CLI entry point for the twin knowledge system."""

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from twin.db import DEFAULT_DB_PATH, get_connection, init_schema, is_initialized

app = typer.Typer(
    name="twin",
    help="Personal knowledge context system — a first-person digital twin.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def status(
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", help="Path to database file"),
) -> None:
    """Show system status and knowledge graph statistics."""
    if not is_initialized(db_path):
        console.print(
            Panel(
                "[dim]No database initialized yet.[/dim]\n"
                "Run [bold]twin init[/bold] to create the knowledge graph.",
                title="Twin Status",
                border_style="blue",
            )
        )
        return

    conn = get_connection(db_path)
    try:
        counts = {}
        for tbl in ("nodes", "edges", "artifacts", "chunks"):
            row = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()  # noqa: S608
            counts[tbl] = row[0] if row else 0

        tbl_status = Table(title="Twin Status", border_style="blue")
        tbl_status.add_column("Metric", style="bold")
        tbl_status.add_column("Value", justify="right")
        tbl_status.add_row("Database", str(db_path))
        tbl_status.add_row("Nodes", str(counts["nodes"]))
        tbl_status.add_row("Edges", str(counts["edges"]))
        tbl_status.add_row("Artifacts", str(counts["artifacts"]))
        tbl_status.add_row("Chunks", str(counts["chunks"]))

        type_rows = conn.execute(
            "SELECT type, COUNT(*) FROM nodes GROUP BY type ORDER BY COUNT(*) DESC"
        ).fetchall()
        if type_rows:
            tbl_status.add_section()
            for node_type, count in type_rows:
                tbl_status.add_row(f"  {node_type}", str(count))

        last_ingest = conn.execute(
            "SELECT timestamp FROM ingestion_log ORDER BY timestamp DESC LIMIT 1"
        ).fetchone()
        if last_ingest:
            tbl_status.add_section()
            tbl_status.add_row("Last ingestion", str(last_ingest[0]))

        console.print(tbl_status)
    finally:
        conn.close()


@app.command()
def init(
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", help="Path to database file"),
) -> None:
    """Initialize the knowledge graph database."""
    if is_initialized(db_path):
        console.print(f"[dim]Database already initialized at[/dim] {db_path}")
        return

    init_schema(db_path)
    console.print(f"[green]✓[/green] Knowledge graph initialized at [bold]{db_path}[/bold]")


@app.command()
def ingest(
    path: str = typer.Argument(help="Path to file or directory to ingest"),
    context: str = typer.Option("", "--context", "-c", help="Optional context"),
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Recurse into dirs"),
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", help="Path to database file"),
) -> None:
    """Ingest a file or directory into the knowledge graph."""
    from twin.ingestion.pipeline import ingest_file

    if not is_initialized(db_path):
        console.print("[red]Error:[/red] Not initialized. Run [bold]twin init[/bold] first.")
        raise typer.Exit(1)

    target = Path(path).expanduser()
    if not target.exists():
        console.print(f"[red]Error:[/red] Path not found: {target}")
        raise typer.Exit(1)

    files: list[Path] = []
    if target.is_file():
        files.append(target)
    elif target.is_dir():
        pattern = "**/*" if recursive else "*"
        files = [f for f in target.glob(pattern) if f.is_file()]
    else:
        console.print(f"[red]Error:[/red] Unsupported path type: {target}")
        raise typer.Exit(1)

    if not files:
        console.print("[dim]No files found to ingest.[/dim]")
        return

    conn = get_connection(db_path)
    try:
        for file in files:
            result = ingest_file(file, conn, context=context, channel="cli")
            if result.status == "processed":
                console.print(
                    f"[green]✓[/green] {result.file_name} — "
                    f"{result.nodes_created} new nodes, "
                    f"{result.nodes_matched} matched, "
                    f"{result.edges_created} edges"
                )
            elif result.status == "skipped":
                console.print(f"[dim]⊘ {result.file_name} — {result.skipped_reason}[/dim]")
            else:
                console.print(f"[red]✗ {result.file_name} — {result.skipped_reason}[/red]")
    finally:
        conn.close()


@app.command()
def serve(
    port: int = typer.Option(8000, "--port", "-p", help="Port to serve on"),
    host: str = typer.Option("127.0.0.1", "--host", help="Host to bind to"),
    reload: bool = typer.Option(False, "--reload", help="Enable hot reload"),
) -> None:
    """Start the API server."""
    import uvicorn

    console.print(f"[green]✓[/green] Starting Twin API on [bold]{host}:{port}[/bold]")
    uvicorn.run("twin.api.app:app", host=host, port=port, reload=reload)


@app.command()
def publish(
    output: Path = typer.Option(Path("./output/portfolio"), "--output", "-o", help="Output dir"),
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", help="Path to database file"),
) -> None:
    """Generate the static portfolio site from the knowledge graph."""
    from twin.generators.portfolio import extract_portfolio_data, generate_portfolio_html

    if not is_initialized(db_path):
        console.print("[red]Error:[/red] Not initialized. Run [bold]twin init[/bold] first.")
        raise typer.Exit(1)

    conn = get_connection(db_path)
    try:
        data = extract_portfolio_data(conn)
        index = generate_portfolio_html(data, output)
        console.print(
            f"[green]✓[/green] Portfolio generated at [bold]{index}[/bold]\n"
            f"  {data.stats.get('projects', 0)} projects, "
            f"{data.stats.get('skills', 0)} skills, "
            f"{data.stats.get('achievements', 0)} achievements"
        )
    finally:
        conn.close()


@app.callback()
def main() -> None:
    """Personal knowledge context system — a first-person digital twin."""


if __name__ == "__main__":
    app()

"""Tests for chat UI and portfolio generation."""

import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from twin.api.app import app
from twin.db import get_connection, init_schema
from twin.generators.portfolio import extract_portfolio_data, generate_portfolio_html

client = TestClient(app)


class TestChatUI:
    def test_serves_chat_page(self):
        response = client.get("/")
        assert response.status_code == 200
        assert "Twin" in response.text
        assert "chat" in response.text.lower()

    def test_chat_has_input_form(self):
        response = client.get("/")
        assert 'id="ask-form"' in response.text
        assert 'id="question"' in response.text

    def test_chat_has_javascript(self):
        response = client.get("/")
        assert "/api/ask" in response.text
        assert "fetch" in response.text


class TestPortfolioGenerator:
    @pytest.fixture
    def db(self, tmp_path: Path):
        db_path = tmp_path / "test.duckdb"
        init_schema(db_path)
        conn = get_connection(db_path)
        conn.execute(
            "INSERT INTO nodes (id, type, name, description, properties) VALUES "
            "('p1', 'project', 'Chitta', 'Knowledge graph system', "
            '\'{"status": "active", "tech_stack": ["Python", "DuckDB"]}\'), '
            "('s1', 'skill', 'Python', NULL, '{\"category\": \"technical\"}'), "
            "('s2', 'skill', 'NLP', NULL, '{\"category\": \"technical\"}'), "
            "('a1', 'achievement', 'VP Recognition', NULL, '{}'), "
            "('o1', 'organization', 'Philips', NULL, '{}')"
        )
        conn.execute(
            "INSERT INTO edges (id, source_id, target_id, type) VALUES "
            "('e1', 'p1', 's1', 'USED_SKILL')"
        )
        yield conn
        conn.close()

    def test_extracts_portfolio_data(self, db):
        data = extract_portfolio_data(db)
        assert len(data.projects) == 1
        assert data.projects[0]["name"] == "Chitta"
        assert len(data.skills) == 2
        assert len(data.achievements) == 1
        assert data.stats["projects"] == 1

    def test_generates_html(self, db, tmp_path):
        data = extract_portfolio_data(db)
        output_dir = tmp_path / "portfolio"
        index = generate_portfolio_html(data, output_dir)
        assert index.exists()
        content = index.read_text()
        assert "Datta Vellal" in content
        assert "Chitta" in content
        assert "Python" in content
        assert "VP Recognition" in content

    def test_empty_graph_generates_valid_html(self, tmp_path):
        db_path = tmp_path / "empty.duckdb"
        init_schema(db_path)
        conn = get_connection(db_path)
        data = extract_portfolio_data(conn)
        output_dir = tmp_path / "empty_portfolio"
        index = generate_portfolio_html(data, output_dir)
        assert index.exists()
        assert "No projects indexed" in index.read_text()
        conn.close()


class TestPublishCLI:
    def test_publish_command(self):
        from typer.testing import CliRunner

        from twin.cli import app as cli_app

        runner = CliRunner()
        with tempfile.TemporaryDirectory() as tmp:
            db = str(Path(tmp) / "test.duckdb")
            out = str(Path(tmp) / "portfolio")
            runner.invoke(cli_app, ["init", "--db", db])
            result = runner.invoke(cli_app, ["publish", "--db", db, "--output", out])
            assert result.exit_code == 0
            assert "Portfolio generated" in result.output

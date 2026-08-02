"""Tests for graph traversal."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.retrieval.graph import (
    build_graph,
    find_path,
    get_neighbors,
    get_subgraph,
    search_by_type,
)


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    conn.execute(
        "INSERT INTO nodes (id, type, name) VALUES "
        "('p1', 'project', 'Chitta'), "
        "('p2', 'project', 'Twin'), "
        "('s1', 'skill', 'Python'), "
        "('s2', 'skill', 'NLP'), "
        "('s3', 'skill', 'GraphDB'), "
        "('per1', 'person', 'Alice')"
    )
    conn.execute(
        "INSERT INTO edges (id, source_id, target_id, type, weight, confidence) VALUES "
        "('e1', 'p1', 's1', 'USED_SKILL', 1.0, 0.9), "
        "('e2', 'p1', 's2', 'USED_SKILL', 1.0, 0.9), "
        "('e3', 'p2', 's1', 'USED_SKILL', 1.0, 0.8), "
        "('e4', 'p2', 's3', 'USED_SKILL', 1.0, 0.8), "
        "('e5', 'per1', 'p1', 'COLLABORATED_WITH', 1.0, 0.85)"
    )
    yield conn
    conn.close()


class TestBuildGraph:
    def test_builds_from_db(self, db):
        g = build_graph(db)
        assert g.number_of_nodes() == 6
        assert g.number_of_edges() == 5

    def test_node_attributes(self, db):
        g = build_graph(db)
        assert g.nodes["p1"]["type"] == "project"
        assert g.nodes["p1"]["name"] == "Chitta"

    def test_edge_attributes(self, db):
        g = build_graph(db)
        edge_data = g.edges["p1", "s1"]
        assert edge_data["type"] == "USED_SKILL"
        assert edge_data["weight"] == 1.0


class TestGetNeighbors:
    def test_depth_1(self, db):
        g = build_graph(db)
        neighbors = get_neighbors(g, "p1", depth=1)
        ids = {n["id"] for n in neighbors}
        assert "s1" in ids
        assert "s2" in ids
        assert "per1" in ids  # incoming edge

    def test_depth_2(self, db):
        g = build_graph(db)
        neighbors = get_neighbors(g, "per1", depth=2)
        ids = {n["id"] for n in neighbors}
        assert "p1" in ids  # depth 1
        assert "s1" in ids  # depth 2

    def test_filter_by_edge_type(self, db):
        g = build_graph(db)
        neighbors = get_neighbors(g, "p1", depth=1, edge_types=["USED_SKILL"])
        ids = {n["id"] for n in neighbors}
        assert "s1" in ids
        assert "per1" not in ids  # COLLABORATED_WITH excluded

    def test_nonexistent_node(self, db):
        g = build_graph(db)
        assert get_neighbors(g, "nope") == []


class TestFindPath:
    def test_finds_path(self, db):
        g = build_graph(db)
        path = find_path(g, "per1", "s2")
        assert "per1" in path
        assert "s2" in path
        assert "p1" in path

    def test_no_path(self, db):
        g = build_graph(db)
        # Add an isolated node
        g.add_node("isolated", type="skill", name="Isolated")
        assert find_path(g, "per1", "isolated") == []

    def test_nonexistent_node(self, db):
        g = build_graph(db)
        assert find_path(g, "nope", "s1") == []


class TestGetSubgraph:
    def test_extracts_subgraph(self, db):
        g = build_graph(db)
        sub = get_subgraph(g, "p1", depth=1)
        assert "p1" in sub.nodes
        assert "s1" in sub.nodes
        assert "per1" in sub.nodes
        # p2 is 2 hops from p1 via s1
        assert "p2" not in sub.nodes

    def test_depth_2_includes_more(self, db):
        g = build_graph(db)
        sub = get_subgraph(g, "p1", depth=2)
        assert "p2" in sub.nodes  # via s1

    def test_nonexistent_center(self, db):
        g = build_graph(db)
        sub = get_subgraph(g, "nope")
        assert sub.number_of_nodes() == 0


class TestSearchByType:
    def test_finds_all_of_type(self, db):
        g = build_graph(db)
        projects = search_by_type(g, "project")
        assert len(projects) == 2
        names = {p["name"] for p in projects}
        assert names == {"Chitta", "Twin"}

    def test_empty_for_unknown_type(self, db):
        g = build_graph(db)
        assert search_by_type(g, "nonexistent") == []

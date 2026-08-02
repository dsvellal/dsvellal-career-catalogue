"""Graph traversal using NetworkX, rebuilt from DuckDB edges."""

import duckdb
import networkx as nx


def build_graph(conn: duckdb.DuckDBPyConnection) -> nx.DiGraph:
    """Build a NetworkX directed graph from DuckDB nodes and edges."""
    g = nx.DiGraph()

    nodes = conn.execute("SELECT id, type, name FROM nodes").fetchall()
    for node_id, node_type, name in nodes:
        g.add_node(node_id, type=node_type, name=name)

    edges = conn.execute(
        "SELECT source_id, target_id, type, weight, confidence FROM edges"
    ).fetchall()
    for source, target, edge_type, weight, confidence in edges:
        g.add_edge(source, target, type=edge_type, weight=weight, confidence=confidence)

    return g


def get_neighbors(
    graph: nx.DiGraph,
    node_id: str,
    depth: int = 1,
    edge_types: list[str] | None = None,
) -> list[dict]:
    """Get neighbors of a node up to a given depth. Returns node info dicts."""
    if node_id not in graph:
        return []

    visited = set()
    frontier = {node_id}
    results = []

    for _ in range(depth):
        next_frontier = set()
        for nid in frontier:
            for neighbor in _get_adjacent(graph, nid, edge_types):
                if neighbor not in visited and neighbor != node_id:
                    visited.add(neighbor)
                    next_frontier.add(neighbor)
                    data = graph.nodes[neighbor]
                    results.append(
                        {
                            "id": neighbor,
                            "type": data.get("type", ""),
                            "name": data.get("name", ""),
                            "depth": _ + 1,
                        }
                    )
        frontier = next_frontier

    return results


def find_path(graph: nx.DiGraph, source_id: str, target_id: str) -> list[str]:
    """Find shortest path between two nodes. Returns list of node IDs."""
    if source_id not in graph or target_id not in graph:
        return []
    try:
        return list(nx.shortest_path(graph.to_undirected(), source_id, target_id))
    except nx.NetworkXNoPath:
        return []


def get_subgraph(
    graph: nx.DiGraph,
    center_id: str,
    depth: int = 2,
) -> nx.DiGraph:
    """Extract a subgraph around a center node."""
    if center_id not in graph:
        return nx.DiGraph()

    nodes = {center_id}
    frontier = {center_id}
    for _ in range(depth):
        next_frontier = set()
        for nid in frontier:
            next_frontier.update(graph.successors(nid))
            next_frontier.update(graph.predecessors(nid))
        nodes.update(next_frontier)
        frontier = next_frontier

    return graph.subgraph(nodes).copy()


def search_by_type(graph: nx.DiGraph, node_type: str) -> list[dict]:
    """Find all nodes of a given type."""
    results = []
    for node_id, data in graph.nodes(data=True):
        if data.get("type") == node_type:
            results.append({"id": node_id, "type": node_type, "name": data.get("name", "")})
    return results


def _get_adjacent(graph: nx.DiGraph, node_id: str, edge_types: list[str] | None) -> set[str]:
    """Get adjacent nodes, optionally filtered by edge type."""
    neighbors = set()
    for _, target, data in graph.out_edges(node_id, data=True):
        if edge_types is None or data.get("type") in edge_types:
            neighbors.add(target)
    for source, _, data in graph.in_edges(node_id, data=True):
        if edge_types is None or data.get("type") in edge_types:
            neighbors.add(source)
    return neighbors

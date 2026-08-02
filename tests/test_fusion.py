"""Tests for Reciprocal Rank Fusion."""

from twin.retrieval.fusion import SearchResult, reciprocal_rank_fusion


class TestRRF:
    def test_single_list(self):
        results = [
            SearchResult(id="a", content="A", source="vector"),
            SearchResult(id="b", content="B", source="vector"),
        ]
        fused = reciprocal_rank_fusion({"vector": results})
        assert len(fused) == 2
        assert fused[0].id == "a"
        assert fused[0].score > fused[1].score

    def test_fuses_multiple_lists(self):
        vector = [
            SearchResult(id="a", content="A", source="vector"),
            SearchResult(id="b", content="B", source="vector"),
        ]
        fts = [
            SearchResult(id="b", content="B", source="fts"),
            SearchResult(id="c", content="C", source="fts"),
        ]
        fused = reciprocal_rank_fusion({"vector": vector, "fts": fts})
        # "b" appears in both lists, should rank highest
        assert fused[0].id == "b"

    def test_respects_weights(self):
        vector = [SearchResult(id="a", source="vector")]
        fts = [SearchResult(id="b", source="fts")]
        # Give FTS 10x weight
        fused = reciprocal_rank_fusion(
            {"vector": vector, "fts": fts},
            weights={"vector": 1.0, "fts": 10.0},
        )
        assert fused[0].id == "b"

    def test_top_n_limits_output(self):
        results = [SearchResult(id=f"r{i}", source="v") for i in range(20)]
        fused = reciprocal_rank_fusion({"v": results}, top_n=5)
        assert len(fused) == 5

    def test_empty_input(self):
        assert reciprocal_rank_fusion({}) == []

    def test_empty_lists(self):
        fused = reciprocal_rank_fusion({"v": [], "f": []})
        assert fused == []

    def test_deduplication(self):
        # Same ID in multiple lists should appear once
        vector = [SearchResult(id="a", content="A full", source="vector")]
        fts = [SearchResult(id="a", content="A", source="fts")]
        fused = reciprocal_rank_fusion({"vector": vector, "fts": fts})
        assert len(fused) == 1
        # Should keep the one with more content
        assert fused[0].content == "A full"

    def test_score_is_combined(self):
        vector = [SearchResult(id="a", source="vector")]
        fts = [SearchResult(id="a", source="fts")]
        fused = reciprocal_rank_fusion({"vector": vector, "fts": fts}, k=60)
        # Score should be 1/(60+1) + 1/(60+1) = 2/61
        expected = 2.0 / 61.0
        assert abs(fused[0].score - expected) < 0.001

    def test_preserves_metadata(self):
        results = [SearchResult(id="a", metadata={"artifact_id": "art_1"})]
        fused = reciprocal_rank_fusion({"v": results})
        assert fused[0].metadata == {"artifact_id": "art_1"}

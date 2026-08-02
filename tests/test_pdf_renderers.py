"""Tests for PDF renderers (WeasyPrint ATS + Typst designed). Skipped if system deps missing."""

import pytest

try:
    from weasyprint import HTML  # noqa: F401

    WEASYPRINT_AVAILABLE = True
except (ImportError, OSError):
    WEASYPRINT_AVAILABLE = False


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint system deps not available")
class TestATSPdf:
    def test_renders_pdf(self, tmp_path):
        from twin.generators.pdf_ats import render_ats_pdf

        md = "# Datta Vellal\n\n## Summary\n\nSenior engineer.\n\n## Skills\n\n- Python\n- ML"
        out = tmp_path / "resume.pdf"
        result = render_ats_pdf(md, out)
        assert result.exists()
        assert result.stat().st_size > 0

    def test_markdown_to_plain_text(self):
        from twin.generators.pdf_ats import markdown_to_plain_text

        md = "# Name\n\n**Bold** and *italic*\n\n- Bullet point"
        text = markdown_to_plain_text(md)
        assert "Bold" in text
        assert "#" not in text
        assert "**" not in text


class TestTypstPdf:
    def test_markdown_to_typst_conversion(self):
        from twin.generators.pdf_typst import _markdown_to_typst

        md = "# Name\n\n## Section\n\n- **Bold** item\n- Normal item"
        typst = _markdown_to_typst(md)
        assert "= Name" in typst
        assert "== Section" in typst
        assert "- *Bold* item" in typst

    def test_renders_pdf(self, tmp_path):
        from twin.generators.pdf_typst import render_typst_pdf

        md = "# Datta Vellal\n\n## Summary\n\nSenior engineer.\n\n## Skills\n\n- Python"
        out = tmp_path / "resume_designed.pdf"
        result = render_typst_pdf(md, out)
        assert result.exists()
        assert result.stat().st_size > 0

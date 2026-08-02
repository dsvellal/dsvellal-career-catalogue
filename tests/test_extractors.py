"""Tests for format-specific text extraction."""

import json
from email.mime.text import MIMEText
from pathlib import Path

import pytest

from twin.ingestion.extractors import ExtractionResult, detect_file_type, extract


@pytest.fixture
def fixtures(tmp_path: Path) -> Path:
    return tmp_path


def test_detect_file_type():
    assert detect_file_type(Path("doc.pdf")) == "pdf"
    assert detect_file_type(Path("doc.docx")) == "docx"
    assert detect_file_type(Path("msg.eml")) == "email"
    assert detect_file_type(Path("notes.md")) == "md"
    assert detect_file_type(Path("data.json")) == "json"
    assert detect_file_type(Path("readme.txt")) == "txt"
    assert detect_file_type(Path("unknown.xyz")) == "txt"


def test_extract_plaintext(tmp_path: Path):
    f = tmp_path / "note.md"
    f.write_text("# Hello\n\nThis is a test.", encoding="utf-8")
    result = extract(f)
    assert result.file_type == "md"
    assert "Hello" in result.text
    assert "This is a test" in result.text


def test_extract_txt(tmp_path: Path):
    f = tmp_path / "plain.txt"
    f.write_text("Just plain text.", encoding="utf-8")
    result = extract(f)
    assert result.file_type == "txt"
    assert result.text == "Just plain text."


def test_extract_json(tmp_path: Path):
    data = {"name": "Project X", "status": "active", "score": 42}
    f = tmp_path / "data.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    result = extract(f)
    assert result.file_type == "json"
    assert result.metadata["name"] == "Project X"
    assert result.metadata["score"] == 42
    assert json.loads(result.text) == data


def test_extract_json_array(tmp_path: Path):
    data = [{"item": 1}, {"item": 2}]
    f = tmp_path / "list.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    result = extract(f)
    assert result.file_type == "json"
    assert result.metadata == {}


def test_extract_email(tmp_path: Path):
    msg = MIMEText("Great work on the demo!")
    msg["Subject"] = "Kudos"
    msg["From"] = "boss@example.com"
    msg["To"] = "datta@example.com"
    msg["Date"] = "Mon, 15 Jul 2026 10:00:00 +0000"
    f = tmp_path / "feedback.eml"
    f.write_bytes(msg.as_bytes())
    result = extract(f)
    assert result.file_type == "email"
    assert "Great work on the demo!" in result.text
    assert result.metadata["subject"] == "Kudos"
    assert result.metadata["from"] == "boss@example.com"


def test_extract_docx(tmp_path: Path):
    from docx import Document

    doc = Document()
    doc.core_properties.author = "Datta"
    doc.core_properties.title = "Test Doc"
    doc.add_paragraph("First paragraph.")
    doc.add_paragraph("Second paragraph.")
    f = tmp_path / "report.docx"
    doc.save(f)
    result = extract(f)
    assert result.file_type == "docx"
    assert "First paragraph" in result.text
    assert "Second paragraph" in result.text
    assert result.metadata["author"] == "Datta"
    assert result.metadata["title"] == "Test Doc"


def test_extract_pdf(tmp_path: Path):
    # Create a minimal PDF using pdfplumber's test support isn't easy,
    # so we use fpdf2 if available, otherwise skip
    pytest.importorskip("fpdf")
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(text="Hello from PDF")
    f = tmp_path / "sample.pdf"
    pdf.output(str(f))

    result = extract(f)
    assert result.file_type == "pdf"
    assert "Hello from PDF" in result.text
    assert result.metadata["page_count"] == 1


def test_extraction_result_defaults():
    r = ExtractionResult(text="hello")
    assert r.metadata == {}
    assert r.file_type == ""

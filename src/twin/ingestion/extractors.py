"""Format-specific text extraction from source files."""

import csv
import email
import json
from dataclasses import dataclass, field
from email import policy
from pathlib import Path

import docx
import pdfplumber


@dataclass
class ExtractionResult:
    text: str
    metadata: dict = field(default_factory=dict)
    file_type: str = ""


def detect_file_type(path: Path) -> str:
    suffix = path.suffix.lower()
    type_map = {
        ".pdf": "pdf",
        ".docx": "docx",
        ".doc": "doc",
        ".eml": "email",
        ".msg": "email",
        ".md": "md",
        ".markdown": "md",
        ".txt": "txt",
        ".json": "json",
        ".xlsx": "xlsx",
        ".xls": "xlsx",
        ".pptx": "pptx",
        ".ppt": "ppt",
        ".csv": "csv",
        ".png": "image",
        ".jpg": "image",
        ".jpeg": "image",
    }
    return type_map.get(suffix, "txt")


def extract(path: Path) -> ExtractionResult:
    """Extract text from a file, dispatching by format."""
    file_type = detect_file_type(path)
    extractors = {
        "pdf": _extract_pdf,
        "docx": _extract_docx,
        "doc": _extract_doc,
        "email": _extract_email,
        "md": _extract_plaintext,
        "txt": _extract_plaintext,
        "json": _extract_json,
        "xlsx": _extract_xlsx,
        "pptx": _extract_pptx,
        "ppt": _extract_ppt,
        "csv": _extract_csv,
        "image": _extract_image,
    }
    extractor = extractors.get(file_type, _extract_plaintext)
    result = extractor(path)
    result.file_type = file_type
    return result


def _extract_pdf(path: Path) -> ExtractionResult:
    pages = []
    metadata = {}
    with pdfplumber.open(path) as pdf:
        metadata["page_count"] = len(pdf.pages)
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
    return ExtractionResult(text="\n\n".join(pages), metadata=metadata)


def _extract_docx(path: Path) -> ExtractionResult:
    doc = docx.Document(str(path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    metadata = {}
    core = doc.core_properties
    if core.author:
        metadata["author"] = core.author
    if core.title:
        metadata["title"] = core.title
    if core.created:
        metadata["created"] = core.created.isoformat()
    return ExtractionResult(text="\n\n".join(paragraphs), metadata=metadata)


def _extract_email(path: Path) -> ExtractionResult:
    raw = path.read_bytes()
    msg = email.message_from_bytes(raw, policy=policy.default)
    metadata = {
        "subject": msg["subject"] or "",
        "from": msg["from"] or "",
        "to": msg["to"] or "",
        "date": msg["date"] or "",
    }
    body = msg.get_body(preferencelist=("plain", "html"))
    text = body.get_content() if body else ""
    return ExtractionResult(text=text.strip(), metadata=metadata)


def _extract_plaintext(path: Path) -> ExtractionResult:
    try:
        text = path.read_text(encoding="utf-8").strip()
    except UnicodeDecodeError:
        text = path.read_text(encoding="latin-1").strip()
    return ExtractionResult(text=text)


def _extract_json(path: Path) -> ExtractionResult:
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    metadata = {}
    if isinstance(data, dict):
        metadata = {k: v for k, v in data.items() if isinstance(v, str | int | float | bool)}
    return ExtractionResult(text=raw, metadata=metadata)


def _extract_xlsx(path: Path) -> ExtractionResult:
    import openpyxl

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    sheets_text = []
    metadata = {"sheet_count": len(wb.sheetnames), "sheets": wb.sheetnames}
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        rows = []
        for row in ws.iter_rows(values_only=True):
            cells = [str(c) if c is not None else "" for c in row]
            if any(cells):
                rows.append("\t".join(cells))
        if rows:
            sheets_text.append(f"[Sheet: {sheet_name}]\n" + "\n".join(rows))
    wb.close()
    return ExtractionResult(text="\n\n".join(sheets_text), metadata=metadata)


def _extract_pptx(path: Path) -> ExtractionResult:
    from pptx import Presentation

    prs = Presentation(str(path))
    slides_text = []
    for i, slide in enumerate(prs.slides, 1):
        texts = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    text = paragraph.text.strip()
                    if text:
                        texts.append(text)
        if texts:
            slides_text.append(f"[Slide {i}]\n" + "\n".join(texts))
    metadata = {"slide_count": len(prs.slides)}
    return ExtractionResult(text="\n\n".join(slides_text), metadata=metadata)


def _extract_ppt(path: Path) -> ExtractionResult:
    """Extract text from legacy .ppt files using filename context as fallback."""
    # python-pptx doesn't support .ppt (legacy binary format)
    # Use the filename as the extracted content for classification
    return ExtractionResult(
        text=f"[Legacy PPT file: {path.name}]",
        metadata={"format": "legacy_ppt", "note": "Binary format, text from filename only"},
    )


def _extract_doc(path: Path) -> ExtractionResult:
    """Extract text from legacy .doc files using filename context as fallback."""
    # python-docx doesn't support .doc (legacy binary format)
    return ExtractionResult(
        text=f"[Legacy DOC file: {path.name}]",
        metadata={"format": "legacy_doc", "note": "Binary format, text from filename only"},
    )


def _extract_csv(path: Path) -> ExtractionResult:
    rows_text = []
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        for row in reader:
            if any(cell.strip() for cell in row):
                rows_text.append("\t".join(row))
    return ExtractionResult(text="\n".join(rows_text), metadata={"row_count": len(rows_text)})


def _extract_image(path: Path) -> ExtractionResult:
    """Extract text from images using Tesseract OCR."""
    try:
        import pytesseract
        from PIL import Image

        img = Image.open(path)
        text = pytesseract.image_to_string(img).strip()
        if text:
            return ExtractionResult(
                text=text, metadata={"ocr": True, "dimensions": f"{img.width}x{img.height}"}
            )
    except Exception:
        pass
    return ExtractionResult(
        text=f"[Image file: {path.name}]",
        metadata={"ocr": False, "note": "OCR failed or no text detected"},
    )

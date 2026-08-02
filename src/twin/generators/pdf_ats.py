"""ATS-friendly PDF rendering via WeasyPrint (machine-readable, simple layout)."""

import re
from pathlib import Path

import markdown
from weasyprint import HTML

ATS_CSS = """\
@page {
    size: letter;
    margin: 1in 0.75in;
}
body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.4;
    color: #1a1a1a;
}
h1 {
    font-size: 18pt;
    margin-bottom: 4pt;
    border-bottom: 1px solid #333;
    padding-bottom: 4pt;
}
h2 {
    font-size: 13pt;
    margin-top: 14pt;
    margin-bottom: 6pt;
    color: #2c3e50;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
}
h3 {
    font-size: 11pt;
    font-weight: bold;
    margin-top: 8pt;
    margin-bottom: 2pt;
}
ul {
    margin: 4pt 0;
    padding-left: 18pt;
}
li {
    margin-bottom: 3pt;
}
p {
    margin: 4pt 0;
}
"""


def render_ats_pdf(markdown_content: str, output_path: Path) -> Path:
    """Render markdown resume to ATS-friendly PDF via WeasyPrint."""
    html_body = markdown.markdown(markdown_content, extensions=["tables", "fenced_code"])
    html_doc = f"""\
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{ATS_CSS}</style></head>
<body>{html_body}</body>
</html>"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_doc).write_pdf(str(output_path))
    return output_path


def markdown_to_plain_text(md: str) -> str:
    """Strip markdown formatting for ATS text extraction testing."""
    text = re.sub(r"#{1,6}\s+", "", md)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"^[-*]\s+", "", text, flags=re.MULTILINE)
    return text.strip()

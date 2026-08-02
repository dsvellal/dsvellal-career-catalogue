"""Designed PDF rendering via Typst (visually polished resume)."""

import re
import subprocess
import tempfile
from pathlib import Path

TYPST_TEMPLATE = """\
#set page(margin: (x: 1.2cm, y: 1.5cm))
#set text(font: "New Computer Modern", size: 10pt)
#set par(justify: true)

#show heading.where(level: 1): it => [
  #set text(size: 16pt, weight: "bold")
  #it.body
  #v(-4pt)
  #line(length: 100%, stroke: 0.5pt + rgb("#2c3e50"))
  #v(4pt)
]

#show heading.where(level: 2): it => [
  #v(8pt)
  #set text(size: 11pt, weight: "bold", fill: rgb("#2c3e50"))
  #upper(it.body)
  #v(2pt)
]

#show heading.where(level: 3): it => [
  #v(4pt)
  #set text(size: 10pt, weight: "bold")
  #it.body
]

{content}
"""


def render_typst_pdf(markdown_content: str, output_path: Path) -> Path:
    """Render markdown resume to designed PDF via Typst."""
    typst_content = _markdown_to_typst(markdown_content)
    typst_doc = TYPST_TEMPLATE.format(content=typst_content)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".typ", delete=False) as f:
        f.write(typst_doc)
        typ_path = Path(f.name)

    try:
        result = subprocess.run(
            ["typst", "compile", str(typ_path), str(output_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Typst compilation failed: {result.stderr}")
    finally:
        typ_path.unlink(missing_ok=True)

    return output_path


def _markdown_to_typst(md: str) -> str:
    """Convert markdown to Typst markup."""
    lines = md.split("\n")
    output = []

    for line in lines:
        if line.startswith("# "):
            output.append(f"= {line[2:]}")
        elif line.startswith("## "):
            output.append(f"== {line[3:]}")
        elif line.startswith("### "):
            output.append(f"=== {line[4:]}")
        elif line.startswith("- ") or line.startswith("* "):
            bullet_text = line[2:]
            bullet_text = _convert_inline_formatting(bullet_text)
            output.append(f"- {bullet_text}")
        elif line.strip() == "":
            output.append("")
        else:
            output.append(_convert_inline_formatting(line))

    return "\n".join(output)


def _convert_inline_formatting(text: str) -> str:
    """Convert markdown inline formatting to Typst.

    Typst: *bold*, _italic_, #raw("code")
    Markdown: **bold**, *italic*, `code`
    """
    # Use placeholders to avoid double-matching
    bold_matches = []

    def _capture_bold(m: re.Match[str]) -> str:
        bold_matches.append(m.group(1))
        return f"\x00B{len(bold_matches) - 1}\x00"

    text = re.sub(r"\*\*(.+?)\*\*", _capture_bold, text)
    text = re.sub(r"\*(.+?)\*", lambda m: f"_{m.group(1)}_", text)
    text = re.sub(r"`(.+?)`", lambda m: f'#raw("{m.group(1)}")', text)

    for i, content in enumerate(bold_matches):
        text = text.replace(f"\x00B{i}\x00", f"*{content}*")

    return text

#!/usr/bin/env python3
"""Convert GitHub-style Markdown file to standalone styled HTML for Playwright PDF export."""
import re
import sys
from pathlib import Path
import markdown


def normalize_gfm_lists_and_blocks(md_text: str) -> str:
    """Normalize 2-space nested lists and cuddled lists outside fenced code blocks for python-markdown."""
    lines = md_text.splitlines()
    out = []
    in_fence = False
    fence_marker = ""
    list_re = re.compile(r"^( +)([-*+] |\d+\. )")
    top_list_re = re.compile(r"^([-*+] |\d+\. )")

    for line in lines:
        stripped = line.lstrip()
        if not in_fence:
            m_fence = re.match(r"^(`{3,}|~{3,})", stripped)
            if m_fence:
                in_fence = True
                fence_marker = m_fence.group(1)[0] * len(m_fence.group(1))
                out.append(line)
                continue
        else:
            if stripped.startswith(fence_marker) and re.match(rf"^{re.escape(fence_marker[0])}+\s*$", stripped):
                in_fence = False
                fence_marker = ""
            out.append(line)
            continue

        # Ensure blank line before top-level list if preceded by normal paragraph/bold label line
        if top_list_re.match(line) and out:
            prev = out[-1].strip()
            if prev and not top_list_re.match(out[-1]) and not list_re.match(out[-1]) and not prev.startswith(">"):
                out.append("")

        m_indent = list_re.match(line)
        if m_indent:
            spaces = len(m_indent.group(1))
            # Convert 2-space indent levels to 4-space indent levels for python-markdown
            level = max(1, (spaces + 1) // 2)
            line = ("    " * level) + line[spaces:]

        out.append(line)

    return "\n".join(out)


CSS = """
@page {
  size: A4 portrait;
  margin: 15mm 13mm 16mm 13mm;
}
* {
  box-sizing: border-box;
}
html, body {
  margin: 0;
  padding: 0;
  font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Arial, sans-serif;
  font-size: 9.5pt;
  line-height: 1.48;
  color: #1f2328;
  background: #ffffff;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
h1, h2, h3, h4 {
  color: #0f172a;
  font-weight: 700;
  line-height: 1.28;
  page-break-after: avoid;
  break-after: avoid;
}
h1 {
  font-size: 16.5pt;
  margin: 0 0 10px 0;
  padding-bottom: 8px;
  border-bottom: 2px solid #1d4ed8;
}
h2 {
  font-size: 12.8pt;
  margin: 18px 0 8px 0;
  padding-bottom: 4px;
  border-bottom: 1px solid #cbd5e1;
}
h3 {
  font-size: 10.8pt;
  margin: 14px 0 6px 0;
  color: #1e3a8a;
}
h4 {
  font-size: 9.8pt;
  margin: 10px 0 4px 0;
  color: #334155;
}
p {
  margin: 5px 0 8px 0;
  text-align: left;
  overflow-wrap: anywhere;
}
ul, ol {
  margin: 4px 0 8px 0;
  padding-left: 20px;
}
li {
  margin: 2.5px 0;
  overflow-wrap: anywhere;
}
hr {
  border: 0;
  border-top: 1px solid #e2e8f0;
  margin: 12px 0;
}
a {
  color: #1d4ed8;
  text-decoration: none;
}
code {
  font-family: Consolas, "Cascadia Mono", "Courier New", monospace;
  font-size: 8.2pt;
  background: #f1f5f9;
  color: #0f172a;
  padding: 1px 4px;
  border-radius: 3px;
  border: 1px solid #e2e8f0;
  overflow-wrap: break-word;
}
pre {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 5px;
  padding: 8px 10px;
  margin: 6px 0 10px 0;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow-wrap: anywhere;
  font-size: 8.1pt;
  line-height: 1.4;
}
pre code {
  background: transparent;
  border: none;
  padding: 0;
  font-size: inherit;
}
blockquote {
  margin: 8px 0;
  padding: 7px 12px;
  border-left: 3.5px solid #2563eb;
  background: #f8fafc;
  color: #334155;
  border-radius: 0 4px 4px 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0 12px 0;
  font-size: 7.8pt;
  line-height: 1.35;
}
table.wide-table {
  font-size: 6.7pt;
  line-height: 1.3;
}
table.wide-table th, table.wide-table td {
  padding: 3px 3.5px;
}
table.wide-table code {
  font-size: 6.3pt;
  padding: 0 2px;
}
table.ultra-wide-table {
  font-size: 5.9pt;
  line-height: 1.25;
}
table.ultra-wide-table th, table.ultra-wide-table td {
  padding: 2px 2.5px;
}
table.ultra-wide-table code {
  font-size: 5.6pt;
  padding: 0 1.5px;
}
thead {
  display: table-header-group;
}
tr {
  page-break-inside: avoid;
  break-inside: avoid;
}
th, td {
  border: 1px solid #cbd5e1;
  padding: 4px 5px;
  vertical-align: top;
  overflow-wrap: anywhere;
  word-break: normal;
}
td.nowrap, th.nowrap {
  white-space: nowrap;
}
th {
  background: #eff6ff;
  color: #0f172a;
  font-weight: 700;
}
tbody tr:nth-child(even) {
  background: #f8fafc;
}
img {
  max-width: 92%;
  max-height: 420px;
  height: auto;
  display: block;
  margin: 6px auto 10px auto;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  page-break-inside: avoid;
  break-inside: avoid;
}
"""


def _embed_pdf_images(body: str, base_dir: Path) -> str:
    """Convert local <img src="..."> into optimized JPEG data-URIs (max 1200px wide, q=82) for compact A4 PDFs."""
    import base64
    import io
    from PIL import Image

    def _repl(m: re.Match) -> str:
        prefix, raw_src, suffix = m.group(1), m.group(2), m.group(3)
        if raw_src.startswith(("http://", "https://", "data:", "file:")):
            return m.group(0)
        img_path = (base_dir / raw_src).resolve()
        if not img_path.is_file():
            return m.group(0)
        with Image.open(img_path) as im:
            im_rgb = im.convert("RGB")
            w, h = im_rgb.size
            if w > 880:
                new_h = int(round(h * 880 / w))
                im_rgb = im_rgb.resize((880, new_h), Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            im_rgb.save(buf, format="JPEG", quality=70, optimize=True)
            b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f'{prefix}data:image/jpeg;base64,{b64}{suffix}'

    return re.sub(r'(<img\b[^>]*?\bsrc=")(.*?)(")', _repl, body)


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--pdf-opt"]
    pdf_opt = "--pdf-opt" in sys.argv[1:]
    if len(args) < 2:
        print("Usage: md_to_html.py <input.md> <output.html> [--pdf-opt]", file=sys.stderr)
        sys.exit(1)
    src = Path(args[0]).resolve()
    dst = Path(args[1]).resolve()
    md_raw = src.read_text(encoding="utf-8")
    md_norm = normalize_gfm_lists_and_blocks(md_raw)
    body = markdown.markdown(
        md_norm,
        extensions=["extra", "sane_lists", "toc"],
    )
    # Allow long paths/identifiers inside inline <code> (outside <pre>) to wrap cleanly at '/' and '_'
    def _wrap_inline_code(block_html: str) -> str:
        parts = re.split(r"(<pre>.*?</pre>)", block_html, flags=re.DOTALL)
        for i in range(0, len(parts), 2):
            parts[i] = re.sub(
                r"<code>(.*?)</code>",
                lambda m: "<code>" + m.group(1).replace("/", "/<wbr>").replace("_", "_<wbr>") + "</code>",
                parts[i],
                flags=re.DOTALL,
            )
        return "".join(parts)

    body = _wrap_inline_code(body)

    compact_id_re = re.compile(
        r"^(Entry\s+\d+|CL-\d+|SV-\d+|IA-\d+|BUG-\d+|UF-\d+|P0?\d|S0\d|Passed|Failed|N/A|ĐẠT|VALID|INCOMPLETE|INVALID|#[0-9]+)$"
    )

    def _process_table(t_match: re.Match) -> str:
        t_inner = t_match.group(1)
        first_tr = re.search(r"<tr[^>]*>(.*?)</tr>", t_inner, flags=re.DOTALL)
        cols = len(re.findall(r"<(?:th|td)\b", first_tr.group(1))) if first_tr else 0
        t_class = ""
        if cols >= 11:
            t_class = ' class="ultra-wide-table"'
        elif cols >= 7:
            t_class = ' class="wide-table"'

        def _tag_cell(c_match: re.Match) -> str:
            tag, attrs, inner = c_match.group(1), c_match.group(2), c_match.group(3)
            plain = re.sub(r"<[^>]+>", "", inner).strip()
            if "\n" not in plain and "<br" not in inner.lower():
                if compact_id_re.match(plain) or (cols <= 6 and 0 < len(plain) <= 10 and "/" not in plain):
                    return f'<{tag}{attrs} class="nowrap">{inner}</{tag}>'
            return c_match.group(0)

        t_inner = re.sub(r"<(td|th)([^>]*)>(.*?)</\1>", _tag_cell, t_inner, flags=re.DOTALL)
        return f"<table{t_class}>{t_inner}</table>"

    body = re.sub(r"<table>(.*?)</table>", _process_table, body, flags=re.DOTALL)
    if pdf_opt:
        body = _embed_pdf_images(body, src.parent)
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>{src.stem}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""
    dst.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()

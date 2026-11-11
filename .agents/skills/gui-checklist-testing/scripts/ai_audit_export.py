#!/usr/bin/env python3
"""Gom các entry AI log (từ một file gộp nối tiếp như ai_log/AI_Log.md hoặc nhiều file *.md) thành AI Audit Report (Markdown).

Usage: python ai_audit_export.py <ai_log_dir_or_file> -o AI_Critique_and_Audit_Report.md [--student "Họ tên - MSSV"]
           [--critique critique.md] [--no-ai]

Hỗ trợ cả 2 chế độ lưu nhật ký:
1. Một file gộp nối tiếp duy nhất (ví dụ `ai_log/AI_Log.md`), trong đó mỗi lượt tương tác mới được append vào cuối file dưới tiêu đề `## Entry NN — ...` (hoặc `# ...`).
2. Nhiều file `*.md` rời trong thư mục `ai_log/`.

Mỗi entry gồm các nhãn in đậm:
**Tool:**, **Date and time:**, **Task / Step:**, **Prompt:**, **AI output:**, **Kept:**, **Changed:**, **Rejected:**, **By hand:**
(giá trị có thể nhiều dòng, kéo dài tới nhãn kế tiếp hoặc đường phân cách `---`).
Bỏ qua file bắt đầu bằng "_" hoặc README. --no-ai ghi khai báo "I do not use any AI help in this exercise."
--critique nối thêm nội dung AI Critique (do SV tự viết) vào cuối báo cáo.
"""
import argparse, re, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

LABELS = ["Tool", "Date and time", "Task / Step", "Prompt", "AI output", "Kept", "Changed", "Rejected", "By hand"]
LABEL_RE = re.compile(r"^\*\*(" + "|".join(re.escape(l) for l in LABELS) + r"):\*\*[ \t]*(.*)$")
HEADING_RE = re.compile(r"^#{1,2}\s+(?:Entry\s+\d+\s*[—–-]\s*)?(.+)$")


def parse_block(title: str, lines: list[str]) -> tuple[str, dict[str, str]]:
    fields, cur = {}, None
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        if not in_fence and stripped == "---":
            continue
        lm = None if in_fence else LABEL_RE.match(line)
        if lm:
            cur = lm.group(1)
            fields[cur] = [lm.group(2)] if lm.group(2) else []
        elif cur is not None:
            fields[cur].append(line)
    return title, {k: "\n".join(v).strip() for k, v in fields.items()}


def parse_entries_from_text(text: str, fallback_stem: str = "") -> list[tuple[str, dict[str, str]]]:
    """Tách văn bản thành danh sách (title, fields) cho từng entry hợp lệ."""
    blocks: list[tuple[str, list[str]]] = []
    cur_title = fallback_stem
    cur_lines: list[str] = []
    in_fence = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        hm = None if in_fence else HEADING_RE.match(line)
        if hm:
            if cur_lines:
                blocks.append((cur_title, cur_lines))
            cur_title = hm.group(1).strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_lines:
        blocks.append((cur_title, cur_lines))

    entries = []
    for title, blines in blocks:
        t, f = parse_block(title, blines)
        if f.get("Tool") or f.get("Prompt"):
            entries.append((t, f))
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", help="Thư mục chứa AI_Log.md / *.md hoặc đường dẫn trực tiếp tới file AI_Log.md")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--student", default="")
    ap.add_argument("--critique")
    ap.add_argument("--no-ai", action="store_true")
    a = ap.parse_args()

    out = ["# AI Audit Report", ""]
    if a.student:
        out += [f"- Sinh viên: {a.student}", ""]
    if a.no_ai:
        out += ["I do not use any AI help in this exercise.", ""]
    else:
        target = Path(a.dir)
        if target.is_file():
            files = [target]
        else:
            files = sorted(
                p for p in target.glob("*.md")
                if not p.name.startswith("_") and p.name.lower() != "readme.md"
            )
        parsed = []
        for p in files:
            for title, f in parse_entries_from_text(p.read_text(encoding="utf-8"), p.stem):
                parsed.append((len(parsed) + 1, p, title, f))

        if not parsed:
            sys.exit(f"Không có entry nào trong {a.dir}. Dùng --no-ai nếu không dùng AI.")

        out += ["I use AI tools for the following tasks:", ""]
        tools = sorted({f.get("Tool", "?") for _, _, _, f in parsed})
        out += [f"Công cụ đã dùng: {', '.join(tools)}", f"Số tương tác: {len(parsed)}", ""]
        out += ["| # | Tool | Ngày giờ | Việc |", "|---|---|---|---|"]
        for i, p, title, f in parsed:
            out.append(f"| {i} | {f.get('Tool', '')} | {f.get('Date and time', '')} | {f.get('Task / Step', '') or title} |")
        out.append("")
        for i, p, title, f in parsed:
            out += [f"## {i}. {title or p.stem}", ""]
            for lab in LABELS:
                val = f.get(lab, "")
                if lab in ("Prompt", "AI output"):
                    out += [f"**{lab}:**", "", "~~~text", val or "(chưa ghi)", "~~~", ""]
                else:
                    out.append(f"**{lab}:** {val or '(chưa ghi)'}")
                    out.append("")
            out.append("---")
            out.append("")
    if a.critique:
        crit = Path(a.critique).read_text(encoding="utf-8").strip()
        crit = re.sub(r"^#+\s*AI Critique[^\n]*\n+", "", crit, flags=re.I)
        out += ["# AI Critique", "", crit.strip(), ""]
    Path(a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Đã ghi {a.out}")


if __name__ == "__main__":
    main()

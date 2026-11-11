#!/usr/bin/env python3
"""Gom các entry AI log thành AI Audit Report (Markdown).

Usage: python ai_audit_export.py <ai_log_dir> -o AI_Critique_and_Audit_Report.md [--student "Họ tên - MSSV"]
           [--critique critique.md] [--no-ai]

Mỗi file *.md trong ai_log_dir là một entry theo assets/ai_log_template.md với các nhãn in đậm:
**Tool:**, **Date and time:**, **Task / Step:**, **Prompt:**, **AI output:**, **Kept:**, **Changed:**, **Rejected:**, **By hand:**
(giá trị có thể nhiều dòng, kéo dài tới nhãn kế tiếp).
Bỏ qua file bắt đầu bằng "_" hoặc README. --no-ai ghi khai báo "I do not use any AI help in this exercise."
--critique nối thêm nội dung AI Critique (do SV tự viết) vào cuối báo cáo.
Không sửa nội dung entry; chỉ gom và sắp xếp theo tên file.
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


def parse(text):
    title = ""
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
    fields, cur = {}, None
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
        lm = None if in_fence else LABEL_RE.match(line)
        if lm:
            cur = lm.group(1)
            fields[cur] = [lm.group(2)] if lm.group(2) else []
        elif cur and not (line.startswith("# ") and not in_fence):
            fields[cur].append(line)
    return title, {k: "\n".join(v).strip() for k, v in fields.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
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
        files = sorted(p for p in Path(a.dir).glob("*.md") if not p.name.startswith("_") and p.name.lower() != "readme.md")
        if not files:
            sys.exit(f"Không có entry nào trong {a.dir}. Dùng --no-ai nếu không dùng AI.")
        out += ["I use AI tools for the following tasks:", ""]
        tools = sorted({parse(p.read_text(encoding='utf-8'))[1].get("Tool", "?") for p in files})
        out += [f"Công cụ đã dùng: {', '.join(tools)}", f"Số tương tác: {len(files)}", ""]
        out += ["| # | Tool | Ngày giờ | Việc |", "|---|---|---|---|"]
        parsed = []
        for i, p in enumerate(files, 1):
            title, f = parse(p.read_text(encoding="utf-8"))
            parsed.append((i, p, title, f))
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
        # bỏ tiêu đề đầu file critique nếu SV đã tự đặt "# AI Critique" để không bị lặp tiêu đề
        crit = re.sub(r"^#+\s*AI Critique[^\n]*\n+", "", crit, flags=re.I)
        out += ["# AI Critique", "", crit.strip(), ""]
    Path(a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Đã ghi {a.out}")


if __name__ == "__main__":
    main()

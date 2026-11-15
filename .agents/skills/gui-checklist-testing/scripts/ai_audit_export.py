#!/usr/bin/env python3
"""Gom các entry AI log (từ một file gộp nối tiếp như ai_log/AI_Log.md hoặc nhiều file *.md) thành AI Audit Report (Markdown).

Usage: python ai_audit_export.py <ai_log_dir_or_file> -o AI_Critique_and_Audit_Report.md [--student "Họ tên - MSSV"]
           [--critique critique.md] [--summary audit_summary.md] [--no-ai]

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


def _parse_student_info(raw: str) -> tuple[str, str, str]:
    """Tách chuỗi 'Họ tên - MSSV (email)' nếu có, ngược lại trả (raw, '', '')."""
    m = re.match(r"^\s*(.+?)\s*[-–—]\s*(\d{6,12})\s*(?:\(([^)]+)\))?\s*$", raw or "")
    if m:
        return m.group(1).strip(), m.group(2).strip(), (m.group(3) or "").strip()
    return (raw or "").strip(), "", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", help="Thư mục chứa AI_Log.md / *.md hoặc đường dẫn trực tiếp tới file AI_Log.md")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--student", default="")
    ap.add_argument(
        "--scope",
        default="`M1` — Xác thực & Hồ sơ cá nhân (`Register`, `Login`, `ForgotPassword` 2 bước, `Profile`, `Header/Navbar`)",
    )
    ap.add_argument(
        "--flow",
        default="`F1` — Đăng ký -> Đăng nhập -> Cập nhật hồ sơ (`FR-01` -> `FR-02` -> `FR-04`)",
    )
    ap.add_argument("--sut", default="EShop Web & API (`./eshop-sut`, commit gốc `1a9304a`)")
    ap.add_argument("--critique")
    ap.add_argument("--summary")
    ap.add_argument("--no-ai", action="store_true")
    a = ap.parse_args()

    out = [
        "# Báo Cáo Phê Bình & Nhật Ký Kiểm Toán AI (AI Audit Report) — HW03-AI (Phạm Vi M1)",
        "",
    ]
    if a.student:
        name, sid, email = _parse_student_info(a.student)
        if sid and email:
            out += [
                f"- **Sinh viên thực hiện:** {name}",
                f"- **Mã số sinh viên (MSSV):** `{sid}`",
                f"- **Email sinh viên:** `{email}`",
            ]
        elif sid:
            out += [
                f"- **Sinh viên thực hiện:** {name}",
                f"- **Mã số sinh viên (MSSV):** `{sid}`",
            ]
        else:
            out.append(f"- **Sinh viên thực hiện:** {a.student}")
    out += [
        "- **Môn học:** Kiểm chứng Phần mềm (Software Testing)",
        "- **Bài tập:** `HW03-AI` — GUI & Usability Testing (Individual Assignment)",
        f"- **Phạm vi phân công nhóm (Task 1 & Task 3):** {a.scope}",
        f"- **Luồng đánh giá Usability (Task 2):** {a.flow}",
        "- **Mức độ năng lực Bloom-AI:** `G9.3 (Analyse)` & `G9.4 (Collaborate with AI for exploratory testing)`",
        "",
        "---",
        "",
    ]

    if a.no_ai:
        out += [
            "## 1. Tuyên Bố Bắt Buộc Về Sử Dụng AI (Mandatory Disclosure)",
            "",
            '*"I do not use any AI help in this exercise."*',
            "",
        ]
    else:
        target = Path(a.dir)
        skip_names = {"readme.md", "critique.md", "audit_summary.md"}
        if a.critique:
            skip_names.add(Path(a.critique).name.lower())
        if a.summary:
            skip_names.add(Path(a.summary).name.lower())
        if target.is_file():
            files = [target]
        else:
            files = sorted(
                p for p in target.glob("*.md")
                if not p.name.startswith("_") and p.name.lower() not in skip_names
            )
        parsed = []
        for p in files:
            for title, f in parse_entries_from_text(p.read_text(encoding="utf-8"), p.stem):
                parsed.append((len(parsed) + 1, p, title, f))

        if not parsed:
            sys.exit(f"Không có entry nào trong {a.dir}. Dùng --no-ai nếu không dùng AI.")

        tools = sorted({f.get("Tool", "?") for _, _, _, f in parsed})
        tools_str = ", ".join(f"`{t}`" for t in tools)
        total_n = len(parsed)

        out += [
            "## 1. Thông Tin Tổng Quan & Tuyên Bố Bắt Buộc Về Sử Dụng AI (Mandatory Disclosure)",
            "",
            '*"I use AI tools for the following tasks:"*',
            "",
            "| Hạng mục | Nội dung chi tiết |",
            "| :--- | :--- |",
        ]
        if a.student:
            name, sid, email = _parse_student_info(a.student)
            stu_cell = f"{name} (`{sid}` — `{email}`)" if (sid and email) else a.student
            out.append(f"| **Sinh viên thực hiện** | {stu_cell} |")
        src_refs = "[`ai_log/AI_Log.md`](ai_log/AI_Log.md) & [`ai_log/critique.md`](ai_log/critique.md)"
        if a.summary:
            src_refs = "[`ai_log/AI_Log.md`](ai_log/AI_Log.md), [`ai_log/critique.md`](ai_log/critique.md) & [`ai_log/audit_summary.md`](ai_log/audit_summary.md)"
        out += [
            f"| **Hệ thống kiểm thử (SUT)** | {a.sut} |",
            f"| **Phạm vi kiểm thử (Task 1 & Task 3)** | {a.scope} |",
            f"| **Luồng đánh giá Usability (Task 2)** | {a.flow} |",
            f"| **Công cụ AI đã sử dụng** | {tools_str} (kết hợp các mô hình ngôn ngữ `Gemini` & `Claude`) |",
            "| **Chính sách AI & Cấp độ Bloom-AI** | `Open` (bắt buộc khai báo & đính kèm AI Audit Report) · `G9.3` & `G9.4` |",
            f"| **Tổng số lượt tương tác đã ghi nhận** | **`{total_n}` lượt tương tác (`Entry 01` .. `Entry {total_n:02d}`)** theo trình tự thời gian thực hiện |",
            f"| **Nguồn nhật ký gốc đối chiếu** | {src_refs} |",
            "",
            "---",
            "",
        ]

        sec_idx = 2
        if a.critique:
            crit = Path(a.critique).read_text(encoding="utf-8").strip()
            crit = re.sub(r"^#+\s*AI Critique[^\n]*\n+", "", crit, flags=re.I)
            out += [
                f"## {sec_idx}. AI Critique (200–300 từ)",
                "",
                crit.strip(),
                "",
                "---",
                "",
            ]
            sec_idx += 1

        if a.summary:
            summ = Path(a.summary).read_text(encoding="utf-8").strip()
            summ = re.sub(r"^#+\s+[^\n]*\n+", "", summ)
            out += [
                f"## {sec_idx}. Tổng Hợp Kết Quả Kiểm Toán Đầu Ra AI (Audit Verdict Summary)",
                "",
                summ.strip(),
                "",
                "---",
                "",
            ]
            sec_idx += 1

        out += [
            f"## {sec_idx}. Bảng Danh Mục Tổng Hợp {total_n} Lượt Tương Tác AI (Interaction Summary)",
            "",
            "| STT | Công cụ AI | Ngày giờ thực hiện | Hạng mục / Bước công việc (`Task / Step`) |",
            "| :---: | :---: | :--- | :--- |",
        ]
        for i, p, title, f in parsed:
            step_txt = (f.get("Task / Step", "") or title).replace("|", "\\|")
            out.append(f"| `Entry {i:02d}` | `{f.get('Tool', '')}` | `{f.get('Date and time', '')}` | {step_txt} |")
        out += ["", "---", ""]
        sec_idx += 1

        out += [
            f"## {sec_idx}. Nhật Ký Kiểm Toán Chi Tiết Từng Lượt Tương Tác (`Entry 01` .. `Entry {total_n:02d}`)",
            "",
        ]
        for i, p, title, f in parsed:
            out += [
                f"### Entry {i:02d} — {title or p.stem}",
                "",
                f"- **Tool:** `{f.get('Tool', '') or '(chưa ghi)'}`",
                f"- **Date and time:** `{f.get('Date and time', '') or '(chưa ghi)'}`",
                f"- **Task / Step:** {f.get('Task / Step', '') or '(chưa ghi)'}",
                "",
                "**Prompt:**",
                "",
                "~~~text",
                f.get("Prompt", "") or "(chưa ghi)",
                "~~~",
                "",
                "**AI output:**",
                "",
                "~~~text",
                f.get("AI output", "") or "(chưa ghi)",
                "~~~",
                "",
            ]
            for key, label_vi in [
                ("Kept", "Kept (Giữ nguyên)"),
                ("Changed", "Changed (Chỉnh sửa)"),
                ("Rejected", "Rejected (Bác bỏ)"),
                ("By hand", "By hand (Tự thực hiện thủ công)"),
            ]:
                val = (f.get(key, "") or "(chưa ghi)").strip()
                if val.startswith("- ") or "\n- " in val:
                    indented = "\n".join(f"  {ln}" if ln.strip() else "" for ln in val.splitlines())
                    out += [f"- **{label_vi}:**", indented]
                else:
                    out.append(f"- **{label_vi}:** {val}")
            out += [
                "",
                "---",
                "",
            ]
    if a.critique and a.no_ai:
        crit = Path(a.critique).read_text(encoding="utf-8").strip()
        crit = re.sub(r"^#+\s*AI Critique[^\n]*\n+", "", crit, flags=re.I)
        out += ["## 2. AI Critique (200–300 từ)", "", crit.strip(), ""]
    Path(a.out).write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Đã ghi {a.out}")


if __name__ == "__main__":
    main()

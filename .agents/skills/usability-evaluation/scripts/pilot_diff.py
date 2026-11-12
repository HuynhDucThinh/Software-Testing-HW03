#!/usr/bin/env python3
"""Trích xuất bảng thay đổi bộ công cụ trước và sau phiên chạy thử Pilot (S00).

Sinh viên tự điền cột 'Lý do tinh chỉnh sau Pilot S00' dựa trên quan sát thực tế.
Không tự ý ghi đè nếu tệp đầu ra đã có lý do do sinh viên điền (trừ khi truyền --force).
"""
import argparse
import difflib
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PLACEHOLDER_REASON = "(SV điền lý do từ quan sát phiên Pilot S00)"


def format_snippet(lines: list[str]) -> str:
    joined = " / ".join(ln.strip() for ln in lines if ln.strip())
    if not joined:
        return "—"
    return joined.replace("|", "\\|")


def main():
    parser = argparse.ArgumentParser(description="So sánh công cụ trước và sau phiên Pilot S00.")
    parser.add_argument("before", type=Path, help="Bản đóng băng trước Pilot")
    parser.add_argument("after", type=Path, help="Bản đã tinh chỉnh sau Pilot")
    parser.add_argument("-o", "--out", type=Path, required=True, help="Đường dẫn tệp Markdown đầu ra")
    parser.add_argument("--title", default="Bộ công cụ khảo sát (Participant Kit)", help="Tên tài liệu đối chiếu")
    parser.add_argument("--force", action="store_true", help="Ghi đè kể cả khi đã có lý do SV điền")
    args = parser.parse_args()

    if not args.before.is_file() or not args.after.is_file():
        sys.exit("[ERROR] Không tìm thấy tệp trước hoặc sau Pilot để so sánh.")

    if args.out.exists() and not args.force:
        existing = args.out.read_text(encoding="utf-8")
        row_count = existing.count("\n| `C")
        todo_count = existing.count(PLACEHOLDER_REASON)
        if row_count > 0 and todo_count < row_count:
            sys.exit(f"[ERROR] '{args.out}' đã có lý do do SV điền — từ chối ghi đè (dùng --force nếu muốn tạo lại).")

    old_lines = args.before.read_text(encoding="utf-8").splitlines()
    new_lines = args.after.read_text(encoding="utf-8").splitlines()

    matcher = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    diff_rows = []
    op_map = {"replace": "Hiệu chỉnh", "delete": "Lược bỏ", "insert": "Bổ sung"}

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        old_range = f"{i1 + 1}–{i2}" if i2 > i1 else "—"
        new_range = f"{j1 + 1}–{j2}" if j2 > j1 else "—"
        diff_rows.append(
            (op_map[tag], old_range, new_range, format_snippet(old_lines[i1:i2]), format_snippet(new_lines[j1:j2]))
        )

    md = [
        f"# Biên Bản Tinh Chỉnh Công Cụ Sau Phiên Chạy Thử Pilot (`S00`) — {args.title}",
        "",
        f"- **Bản trước Pilot:** `{args.before.as_posix()}`",
        f"- **Bản chính thức sau Pilot:** `{args.after.as_posix()}`",
        "",
        "| Mã thay đổi | Loại | Dòng cũ | Dòng mới | Nội dung trước Pilot | Nội dung sau Pilot | Lý do tinh chỉnh từ quan sát `S00` |",
        "| :---: | :---: | :---: | :---: | :--- | :--- | :--- |",
    ]
    if diff_rows:
        for idx, (kind, r_old, r_new, s_old, s_new) in enumerate(diff_rows, start=1):
            md.append(f"| `C{idx:02d}` | {kind} | {r_old} | {r_new} | {s_old} | {s_new} | {PLACEHOLDER_REASON} |")
    else:
        md.append(
            "| `C00` | Giữ nguyên | — | — | Không thay đổi câu chữ | Không thay đổi câu chữ | Kịch bản và thang đo trong phiên Pilot `S00` đã rõ ràng, thời lượng hợp lý nên giữ nguyên cho 7 phiên chính thức. |"
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Đã xuất biên bản đối chiếu Pilot tại '{args.out}' ({len(diff_rows)} thay đổi).")


if __name__ == "__main__":
    main()

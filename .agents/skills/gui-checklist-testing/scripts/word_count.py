#!/usr/bin/env python3
"""Đếm từ của AI Critique (mục 10 của đề: 200 đến 300 từ).

Usage: python word_count.py <file.md> [--min 200] [--max 300] [--section "AI Critique"]

Đếm từ (chuỗi ký tự chữ/số tách bởi khoảng trắng) trong file, hoặc chỉ phần dưới tiêu đề --section
(tới tiêu đề cùng cấp kế tiếp). Bỏ dấu đánh dấu Markdown (#, *, -, >, `, bảng) khi đếm.
Mã thoát 1 nếu ngoài khoảng.
"""
import argparse, re, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def section(text, title):
    lines = text.splitlines()
    heads = []
    for i, l in enumerate(lines):
        m = re.match(r"^(#+)\s+(.*)$", l)
        if m and title.lower() in m.group(2).lower():
            heads.append((i + 1, len(m.group(1))))
    if not heads:
        sys.exit(f"Không thấy tiêu đề chứa '{title}'")
    # lấy tiêu đề đầu tiên có nội dung (bỏ qua tiêu đề trùng liên tiếp không có thân bài)
    for start, level in heads:
        body = []
        for l in lines[start:]:
            m = re.match(r"^(#+)\s", l)
            if m and len(m.group(1)) <= level:
                break
            body.append(l)
        if "".join(body).strip():
            return "\n".join(body)
    return ""


def count(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"[#*>`|_~\-]+", " ", text)
    return len([w for w in re.split(r"\s+", text) if re.search(r"\w", w)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--min", type=int, default=200)
    ap.add_argument("--max", type=int, default=300)
    ap.add_argument("--section")
    a = ap.parse_args()
    text = Path(a.file).read_text(encoding="utf-8")
    if a.section:
        text = section(text, a.section)
    n = count(text)
    ok = a.min <= n <= a.max
    print(f"{a.file}: {n} từ (yêu cầu {a.min}-{a.max}) -> {'ĐẠT' if ok else 'KHÔNG ĐẠT'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""In ma trận độ phủ của checklist.json: IA x loại nguồn, IA x màn hình, IA x nhóm checkpoint slide.

Usage: python coverage_matrix.py <checklist.json>

Chỉ ĐẾM và IN SỐ LƯỢNG. Không đề xuất item hay khía cạnh nào cần thêm (quy tắc 8: ở Bước 2 AI không gợi ý).
Nhóm checkpoint slide được suy từ cột `can_cu`/`muc_kiem_tra` bằng từ khoá (heuristic đơn giản);
SV tự đọc kết quả và quyết định.
"""
import json, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

IAS = ["IA-01", "IA-02", "IA-03", "IA-04"]
SOURCES = ["SRS", "Control", "Heuristic"]
GROUPS = {
    "Visual Consistency": ["căn", "alignment", "màu", "color", "font", "chữ", "chính tả", "định dạng", "nhất quán", "ngôn ngữ"],
    "Controls and Inputs": ["độ dài", "maxlength", "disabled", "vô hiệu", "placeholder", "gợi ý", "type", "bắt buộc", "ký hiệu *", "nhãn"],
    "Navigation and Usability": ["tab", "enter", "phím", "keyboard", "focus", "hover", "link", "điều hướng", "chuyển trang", "quay lại"],
    "Feedback and Safety": ["thông báo", "lỗi", "loading", "đang xử lý", "xác nhận", "toast", "alert", "phản hồi"],
    "Responsive Display": ["responsive", "viewport", "375", "768", "1440", "cuộn", "che", "tràn", "overlap"],
}


def has(text, kws):
    t = unicodedata.normalize("NFC", text.lower())
    return any(k in t for k in kws)


def table(title, rows, cols):
    print(f"\n{title}")
    print("| | " + " | ".join(cols) + " | Tổng |")
    print("|---|" + "---|" * (len(cols) + 1))
    for r, counts in rows:
        print(f"| {r} | " + " | ".join(str(counts.get(c, 0)) for c in cols) + f" | {sum(counts.values())} |")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    items = doc.get("items", [])
    print(f"Tổng {len(items)} item. Ma trận chỉ đếm số lượng, không gợi ý item.")

    by = defaultdict(Counter)
    for it in items:
        by[it["ia"]][it.get("loai_nguon", "")] += 1
    table("1. IA x loại nguồn", [(ia, by[ia]) for ia in IAS], SOURCES)

    screens = sorted({i["man_hinh"] for i in items})
    by = defaultdict(Counter)
    for it in items:
        by[it["ia"]][it["man_hinh"]] += 1
    table("2. IA x màn hình", [(ia, by[ia]) for ia in IAS], screens)

    by = defaultdict(Counter)
    for it in items:
        blob = f"{it.get('muc_kiem_tra', '')} {it.get('can_cu', '')} {it.get('expected', '')}"
        for g, kws in GROUPS.items():
            if has(blob, kws):
                by[it["ia"]][g] += 1
    table("3. IA x nhóm checkpoint slide (suy từ từ khoá, một item có thể thuộc nhiều nhóm)", [(ia, by[ia]) for ia in IAS], list(GROUPS))

    by_origin = Counter(i.get("nguon", "") for i in items)
    print("\n4. Nguồn item: " + ", ".join(f"{k} {v}" for k, v in sorted(by_origin.items())))
    by_plat = Counter(p for i in items for p in i.get("nen_tang", []))
    print("5. Item áp dụng theo nền tảng: " + ", ".join(f"{k} {v}" for k, v in sorted(by_plat.items())))


if __name__ == "__main__":
    main()


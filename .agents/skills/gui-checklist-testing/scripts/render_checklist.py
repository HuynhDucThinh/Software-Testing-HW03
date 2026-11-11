"""Render checklist.json thành bảng Markdown (skill gui-checklist-testing).

    python .agents/skills/gui-checklist-testing/scripts/render_checklist.py checklist/checklist.json -o checklist/M1_GUI_Checklist.md

Cột kết quả P1/P2/P3 lấy từ item["ket_qua"][Px] nếu có; nền tảng không áp dụng ghi "N/A".
"""
import argparse, json, re
from collections import Counter
from pathlib import Path

IA_NAMES = {
    "IA-01": "General UI standards",
    "IA-02": "Forms",
    "IA-03": "Navigation",
    "IA-04": "Feedback / state",
}


def escape_outside_code(text):
    parts = re.split(r"(`[^`]*`)", str(text))
    out = []
    for p in parts:
        if p.startswith("`") and p.endswith("`"):
            out.append(p)
        else:
            p = re.sub(r"<(?!(?:br\s*/?)>)(?=[A-Za-z/!?])", "&lt;", p, flags=re.I)
            out.append(p)
    return "".join(out)


def cell(s):
    return escape_outside_code(s).replace("|", "\\|").replace("\n", "<br>")


def result(it, p):
    if p not in it.get("nen_tang", []):
        return "N/A"
    return it.get("ket_qua", {}).get(p, "")


def render(doc):
    meta, items = doc["meta"], doc["items"]
    plats = list(meta.get("platforms", {}))
    out = [f"# Checklist GUI - {meta.get('scope', '')}", ""]
    out.append(f"> Sinh tự động từ `checklist.json` bằng `render_checklist.py` (skill gui-checklist-testing) - không sửa tay. Phiên bản: {meta.get('version', '')}.")
    out.append("")
    out.append(f"- SUT: {meta.get('sut_version', '')}")
    out.append(f"- Căn cứ: {meta.get('test_basis', '')}")
    out.append("- Nền tảng: " + "; ".join(f"{k} = {v}" for k, v in meta.get("platforms", {}).items()))
    out.append("")

    by_ia = Counter(i["ia"] for i in items)
    by_src = Counter(i.get("loai_nguon", "") for i in items)
    by_origin = Counter(i.get("nguon", "") for i in items)
    out += ["## Thống kê", "",
            "| IA | Số item |", "|---|---|"]
    out += [f"| {ia} {IA_NAMES.get(ia, '')} | {by_ia[ia]} |" for ia in sorted(by_ia)]
    out.append(f"| **Tổng** | **{len(items)}** |")
    out.append("")
    out.append("Loại căn cứ: " + ", ".join(f"{k} {v}" for k, v in sorted(by_src.items())) +
               " | Nguồn item: " + ", ".join(f"{k} {v}" for k, v in sorted(by_origin.items())) +
               " | Ưu tiên: " + ", ".join(f"{k} {v}" for k, v in sorted(Counter(i['uu_tien'] for i in items).items())))
    out.append("")

    if doc.get("assumptions"):
        out += ["## Giả định", "", "| Mã | Nội dung |", "|---|---|"]
        out += [f"| {k} | {cell(v)} |" for k, v in doc["assumptions"].items()]
        out.append("")

    for ia in sorted(by_ia):
        out += [f"## {ia} - {IA_NAMES.get(ia, '')}", ""]
        head = ["ID", "Màn hình", "Mục kiểm tra", "Căn cứ", "Expected (ngưỡng Pass/Fail)", "Ưu tiên", "Nguồn"] + plats + ["Notes"]
        out.append("| " + " | ".join(head) + " |")
        out.append("|" + "---|" * len(head))
        for it in items:
            if it["ia"] != ia:
                continue
            exp = cell(it["expected"])
            if it.get("tien_dieu_kien"):
                exp = f"*Tiền điều kiện:* {cell(it['tien_dieu_kien'])}<br>{exp}"
            notes = []
            if it.get("gia_dinh"):
                notes.append(cell(it["gia_dinh"]))
            for p, why in it.get("na", {}).items():
                notes.append(f"{p} N/A - {cell(why)}")
            for p, n in it.get("notes_nt", {}).items():
                notes.append(f"{p}: {cell(n)}")
            for p, ev in it.get("evidence", {}).items():
                notes.append(f"{p} ảnh: " + ", ".join(f"`{e}`" for e in ev))
            ly = it.get("ly_do_ai_bo_sot")
            if isinstance(ly, dict):
                notes.append(f"Vì sao AI bỏ sót ({cell(ly.get('loai', ''))}): {cell(ly.get('giai_thich', ''))}")
            elif ly:
                notes.append(f"Vì sao AI bỏ sót: {cell(ly)}")
            if it.get("luc_them"):
                notes.append(f"Lúc thêm: {cell(it['luc_them'])}")
            if it.get("notes"):
                notes.append(cell(it["notes"]))
            row = [
                cell(it["id"]),
                cell(it["man_hinh"]),
                cell(it["muc_kiem_tra"]),
                f"{cell(it['can_cu'])} ({cell(it.get('loai_nguon', ''))})",
                exp,
                cell(it["uu_tien"]),
                cell(it.get("nguon", "")),
            ] + [cell(result(it, p)) for p in plats] + ["<br>".join(notes)]
            out.append("| " + " | ".join(row) + " |")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    doc = json.loads(Path(a.json).read_text(encoding="utf-8"))
    ids = [i["id"] for i in doc["items"]]
    assert len(ids) == len(set(ids)), "trùng id"
    md = render(doc)
    out = Path(a.out) if a.out else Path(a.json).with_suffix(".md")
    out.write_text(md + "\n", encoding="utf-8", newline="\n")
    print(f"Đã ghi {out} ({len(ids)} item)")


if __name__ == "__main__":
    main()

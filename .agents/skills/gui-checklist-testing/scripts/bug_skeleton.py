#!/usr/bin/env python3
"""Gom dữ kiện bug từ checklist.json và sinh khung BUG-<n>.md chỉ chứa dữ kiện chép lại.

Usage:
  python bug_skeleton.py <checklist.json> --out bugs/            # in danh sách Failed + nhóm đề xuất, sinh khung
  python bug_skeleton.py <checklist.json> --list-only            # chỉ in danh sách, không ghi file
  python bug_skeleton.py <checklist.json> --out bugs/ --start 1  # số BUG bắt đầu (mặc định 1)

Quy tắc (SKILL.md quy tắc 12): KHÔNG viết tiêu đề, mô tả, steps, severity, priority. Các mục đó để trống cho SV.
Nhóm = các item Failed có cùng (màn hình, notes Actual đã chuẩn hoá) -> chỉ là gợi ý gom; SV tách/gộp trước khi chốt.
Không ghi đè file BUG-<n>.md đã tồn tại.
"""
import argparse, json, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def norm(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def failed_cells(doc):
    rows = []
    for it in doc["items"]:
        for p, r in it.get("ket_qua", {}).items():
            if r == "Failed" and it.get("lap_bug", {}).get(p, True) is not False:
                rows.append((it, p))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--out")
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--list-only", action="store_true")
    a = ap.parse_args()
    doc = json.loads(Path(a.json).read_text(encoding="utf-8"))
    plats = doc["meta"].get("platforms", {})
    rows = failed_cells(doc)

    print(f"Failed x nền tảng: {len(rows)} ô, {len({it['id'] for it, _ in rows})} item\n")
    print("| Item | IA | Màn hình | Nền tảng | Notes (Actual) | Ảnh |")
    print("|---|---|---|---|---|---|")
    for it, p in rows:
        notes = it.get("notes_nt", {}).get(p, "").replace("|", "\\|")
        ev = ", ".join(it.get("evidence", {}).get(p, []))
        print(f"| {it['id']} | {it['ia']} | {it['man_hinh']} | {p} | {notes} | {ev} |")

    groups = defaultdict(list)
    for it, p in rows:
        key = (norm(it["man_hinh"]), norm(it.get("notes_nt", {}).get(p, ""))[:80], it["id"])
        groups[it["id"]].append((it, p))
    # nhóm theo item (mặc định); SV tự gộp item có cùng hành vi khi chốt
    print(f"\nĐề xuất: {len(groups)} nhóm (mỗi nhóm = 1 item Failed trên một hoặc nhiều nền tảng). SV tách/gộp trước khi chốt.")

    if a.list_only or not a.out:
        return
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    n = a.start
    for iid, cells in groups.items():
        path = out / f"BUG-{n}.md"
        if path.exists():
            print(f"Bỏ qua {path} (đã tồn tại)")
            n += 1
            continue
        it = cells[0][0]
        ps = [p for _, p in cells]
        env = "; ".join(f"{p}: {plats.get(p, '')}" for p in ps)
        notes = "\n".join(f"- {p}: {it.get('notes_nt', {}).get(p, '')}" for p in ps)
        evid = "\n".join(f"- {p}: " + ", ".join(it.get('evidence', {}).get(p, [])) for p in ps)
        md = f"""# BUG-{n} - (SV viết tiêu đề)

> Khung chỉ chứa dữ kiện chép lại từ checklist.json. SV tự viết Tiêu đề, Summary, Steps, Impact, Severity, Priority.

## Summary
(SV viết)

- Bug ID: BUG-{n}
- Checklist item: {it['id']}
- Requirement: {it.get('can_cu', '')}
- Interface aspect: {it['ia']}
- Màn hình: {it['man_hinh']}
- Loại lỗi: {it.get('loai_loi', '(SV chọn)')}
- Severity: (SV)
- Priority: (SV)

## Environment
- SUT: {doc['meta'].get('sut_version', '')}
- Nền tảng: {env}

## Preconditions
{it.get('tien_dieu_kien', '(SV ghi)')}

## Steps to reproduce
(SV viết)

## Expected result
{it.get('expected', '')}

## Actual result
{notes}

## Evidence
{evid}
"""
        path.write_text(md, encoding="utf-8")
        print(f"Đã ghi {path} ({it['id']}; {', '.join(ps)})")
        n += 1


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""tests/compose_t1_p3_from_raw.py
P3 (Chrome Android 156 trên OPPO Reno10 5G) không thể chụp lại khi thiết bị không kết nối.
Script dựng lại ảnh minh chứng P3 TỪ ẢNH GỐC page.screenshot đã chụp trên điện thoại thật ngày 11/11 (evidence_raw/P3/F*.png),
bỏ hoàn toàn thanh địa chỉ vẽ giả và hộp thoại vẽ giả của bản cũ, rồi gắn chú thích riêng theo từng mục
(Actual lấy nguyên văn từ checklist.json - notes_nt.P3 của lượt chạy P3 ngày 11/11).
"""
import json, os
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("c", ROOT / "tests" / "compose_t1_evidence.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

SCENE = {
    "F01.png": ("/register", ["CL-03", "CL-07", "CL-11", "CL-12", "CL-13", "CL-16", "CL-19", "CL-23", "CL-24", "SV-04", "SV-08", "SV-09", "SV-14", "SV-16", "SV-19"]),
    "F02.png": ("/login", ["CL-32"]),
    "F03.png": ("/profile", ["CL-30"]),
    "F04.png": ("/login", ["CL-01", "CL-04", "CL-14", "CL-15", "CL-28", "SV-03"]),
    "F05.png": ("/forgot-password", ["CL-05", "CL-26", "CL-35"]),
    "F06.png": ("/forgot-password", ["CL-08", "CL-17", "CL-18", "CL-20", "SV-12", "SV-13"]),
    "F07.png": ("/profile", ["CL-06", "CL-22", "CL-25"]),
    "F08.png": ("/profile", ["SV-10", "CL-36"]),
    "F09.png": ("/profile", ["SV-11"]),
    "F10.png": ("/profile", ["SV-06"]),
    "F11.png": ("/profile", ["SV-05"]),
    "F12.png": ("/login", ["CL-33"]),
}
ck = {i["id"]: i for i in json.loads((ROOT / "checklist/checklist.json").read_text("utf-8"))["items"]}
out_raw = ROOT / "evidence_raw" / "v2" / "P3"
out_raw.mkdir(parents=True, exist_ok=True)

# SV-20: ảnh cũ có ô DOM-probe chèn trong trang; chỉ cắt bỏ dải 108px thanh địa chỉ vẽ giả phía trên
sv20_src = ROOT / "screenshots/task1_failed/P3_SV-20.png"
sv20_raw = out_raw / "SV-20_page.png"
if not sv20_raw.exists():
    im = Image.open(sv20_src); im.crop((0, 108, im.width, im.height)).save(sv20_raw)
items = []


def short_expected(it):
    return it["expected"].split(" Fail nếu")[0].replace("*Expected:* ", "")[:230]


def add(item_id, raw_path, route, scene_note, time_src=None):
    it = ck[item_id]
    mt = datetime.fromtimestamp(os.path.getmtime(time_src or raw_path), tz=timezone.utc).isoformat()
    note = it["notes_nt"]["P3"].replace("Actual: ", "")
    items.append({
        "id": item_id, "platform": "P3", "browser": "Chrome Android 156.0.8078.79", "os": "Android 15 - OPPO Reno10 5G (CPH2531), thiết bị thật qua adb",
        "viewport_text": "màn hình thật 1080x2412 (ảnh thu nhỏ)", "url": f"http://localhost:5173{route}", "title": "frontend-web",
        "captured_at": mt, "file": str(raw_path.relative_to(ROOT)).replace("\\", "/"),
        "expected": short_expected(it),
        "actual": [note, scene_note],
        "source_note": "Ảnh trang gốc chụp trên điện thoại thật ngày 11/11 (page.screenshot qua Playwright _android); số liệu Actual là kết quả đo DOM của lượt chạy P3 11/11.",
    })


for scene, (route, ids) in SCENE.items():
    src = ROOT / "evidence_raw" / "P3" / scene
    # Bản lưu trong evidence_raw/P3 đã bị ghép dải thanh địa chỉ vẽ giả (108px trên), lớp phủ email (đáy) và với F05/F07 là hộp thoại vẽ giả.
    # Chỉ CẮT BỎ các phần vẽ thêm đó, không chỉnh sửa điểm ảnh nào của trang web.
    im = Image.open(src)
    bottom = 1480 if scene in ("F05.png", "F07.png") else im.height - 80
    raw = out_raw / f"{scene[:-4]}_page.png"
    im.crop((0, 108, im.width, bottom)).save(raw)
    for i in ids:
        share = f"Ảnh cảnh {route} dùng chung cho {len(ids)} mục P3 ({', '.join(ids)}); xem chú thích riêng của mục này." if len(ids) > 1 else "Ảnh chụp riêng cho mục này."
        if scene in ("F05.png", "F07.png"):
            share += " Hộp thoại window.alert() không chụp được bằng page.screenshot nên nội dung được ghi trong dòng Actual."
        add(i, raw, route, share, time_src=src)
add("SV-20", sv20_raw, "/profile", "Ô tối màu là hộp DOM-probe do script chèn vào trang lúc chụp; bàn phím ảo hệ thống không xuất hiện trong page.screenshot.")
items[-1]["captured_at"] = "2026-11-11T19:42:04+07:00"  # thời điểm commit a11ec87 của ảnh SV-20 gốc

(out_raw / "meta.json").write_text(json.dumps({"platform": "P3", "items": items}, ensure_ascii=False, indent=2), "utf-8")
for it in items:
    c.compose(it, ROOT / "screenshots" / "task1_failed" / f"P3_{it['id']}.png")
print("P3 composed", len(items))

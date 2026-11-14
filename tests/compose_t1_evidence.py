#!/usr/bin/env python3
"""tests/compose_t1_evidence.py
Ghép khung chú thích minh bạch cho ảnh minh chứng Task 1 (không vẽ giả thanh địa chỉ hay hộp thoại):
  - Dải trên: nền tảng thật (tên + phiên bản trình duyệt do Playwright báo), hệ điều hành, URL thực tế page.url(),
    document.title và thời điểm chụp; ghi rõ "Ảnh chụp tự động bằng Playwright".
  - Ảnh trang web nguyên vẹn ở giữa (khung đỏ = phần tử liên quan, chỉ thêm CSS outline).
  - Dải dưới: mã mục, Expected rút gọn, Actual đo trực tiếp lúc chụp, kèm lớp phủ email sinh viên.
Cách chạy: python tests/compose_t1_evidence.py P1 [P2 ...]
"""
import json, sys, textwrap
from datetime import datetime, timezone, timedelta
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
EMAIL = "23120199@student.hcmus.edu.vn"
TZ = timezone(timedelta(hours=7))


def font(size, bold=False):
    for fp in ([r"C:\Windows\Fonts\segoeuib.ttf"] if bold else [r"C:\Windows\Fonts\segoeui.ttf"]) + [r"C:\Windows\Fonts\arial.ttf"]:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    out = []
    for para in text.split("\n"):
        words, cur = para.split(" "), ""
        for w in words:
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=fnt) <= width:
                cur = t
            else:
                if cur:
                    out.append(cur)
                cur = w
        out.append(cur)
    return out


def compose(item, dst):
    page = Image.open(ROOT / item["file"]).convert("RGB")
    pw, ph = page.size
    scale = 1.0 if pw >= 900 else 0.8
    f_b, f_r, f_s = font(int(17 * scale), True), font(int(15 * scale)), font(int(14 * scale))
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    pad = 16
    ts = datetime.fromisoformat(item["captured_at"].replace("Z", "+00:00")).astimezone(TZ).strftime("%Y-%m-%d %H:%M:%S")
    vp = item.get("viewport_text") or f"viewport {item['viewport']['width']}x{item['viewport']['height']}"
    src = item.get("source_note") or f"Ảnh chụp tự động bằng Playwright lúc {ts} (UTC+7); khung đỏ = phần tử liên quan (chỉ thêm CSS outline)"
    top_lines = [
        (f"{item['platform']} - {item['browser']} - {item['os']} - {vp}", f_b),
        (f"URL: {item['url']}   |   document.title: \"{item['title']}\"", f_r),
        (src, f_s),
    ]
    tl = []
    for t, f in top_lines:
        for ln in wrap(probe, t, f, pw - 2 * pad):
            tl.append((ln, f))
    top_h = pad + sum(int(f.size * 1.45) for _, f in tl) + pad // 2
    bottom = [(f"{item['id']} - Expected: {item['expected']}", f_b)] + [("Actual (đo lúc chụp): " + a if i == 0 else "  " + a, f_r) for i, a in enumerate(item["actual"])]
    bl = []
    for t, f in bottom:
        for ln in wrap(probe, t, f, pw - 2 * pad):
            bl.append((ln, f))
    wm_f = font(int(18 * scale), True)
    bot_h = pad + sum(int(f.size * 1.45) for _, f in bl) + int(wm_f.size * 2.4) + pad
    canvas = Image.new("RGB", (pw, top_h + ph + bot_h), (30, 41, 59))
    d = ImageDraw.Draw(canvas)
    y = pad
    for ln, f in tl:
        d.text((pad, y), ln, font=f, fill=(248, 250, 252) if f is f_b else (186, 230, 253))
        y += int(f.size * 1.45)
    canvas.paste(page, (0, top_h))
    d.rectangle([0, top_h + ph, pw, top_h + ph + bot_h], fill=(15, 23, 42))
    y = top_h + ph + pad
    for ln, f in bl:
        d.text((pad, y), ln, font=f, fill=(254, 202, 202) if f is f_b else (226, 232, 240))
        y += int(f.size * 1.45)
    tw = d.textlength(EMAIL, font=wm_f)
    x1, y1 = pw - tw - 2 * 14 - pad, top_h + ph + bot_h - int(wm_f.size * 1.9) - pad // 2
    d.rounded_rectangle([x1, y1, pw - pad, y1 + int(wm_f.size * 1.7)], radius=8, fill=(255, 249, 196), outline=(217, 119, 6), width=2)
    d.text((x1 + 14, y1 + 3), EMAIL, font=wm_f, fill=(185, 28, 28))
    dst.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dst, "PNG", optimize=True)


if __name__ == "__main__":
    for P in sys.argv[1:]:
        meta = json.loads((ROOT / "evidence_raw" / "v2" / P / "meta.json").read_text("utf-8"))
        for it in meta["items"]:
            compose(it, ROOT / "screenshots" / "task1_failed" / f"{P}_{it['id']}.png")
        print(P, "composed", len(meta["items"]))

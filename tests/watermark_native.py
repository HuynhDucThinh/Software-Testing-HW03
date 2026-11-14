import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def load_font(size: int, bold: bool = True):
    candidates = (
        [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"]
        if bold
        else [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"]
    )
    for fp in candidates:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def apply_watermark(raw_path: Path, out_path: Path, bottom_offset: int = 84):
    base = Image.open(raw_path).convert("RGBA")
    pw, ph = base.size

    wm_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    wd = ImageDraw.Draw(wm_layer)

    # Scale font nicely for 1080x2412 mobile vs 1920x1080 desktop
    is_portrait_mobile = ph > pw
    font_size = 28 if is_portrait_mobile else 22
    f_wm = load_font(font_size, bold=True)
    email_txt = "23120199@student.hcmus.edu.vn"

    bbox = wd.textbbox((0, 0), email_txt, font=f_wm)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    px, py = (20, 12) if is_portrait_mobile else (16, 10)
    mx = 28 if is_portrait_mobile else 24
    my = bottom_offset

    wx1 = pw - tw - px * 2 - mx
    wy1 = ph - th - py * 2 - my
    wx2 = pw - mx
    wy2 = ph - my

    wd.rounded_rectangle(
        [wx1, wy1, wx2, wy2],
        radius=10,
        fill=(255, 249, 196, 242),
        outline=(217, 119, 6, 255),
        width=3,
    )
    wd.text((wx1 + px, wy1 + py - bbox[1]), email_txt, font=f_wm, fill=(185, 28, 28, 255))

    final_img = Image.alpha_composite(base, wm_layer).convert("RGB")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    final_img.save(out_path, format="PNG", optimize=True)
    print(f"WATERMARKED: {out_path} ({final_img.size[0]}x{final_img.size[1]})")


if __name__ == "__main__":
    raw = Path(sys.argv[1])
    out = Path(sys.argv[2])
    offset = int(sys.argv[3]) if len(sys.argv) > 3 else 84
    apply_watermark(raw, out, offset)

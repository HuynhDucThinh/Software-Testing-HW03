import ctypes
from ctypes import wintypes
import sys
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageGrab

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

user32 = ctypes.windll.user32


def find_browser_hwnd(browser_kind: str):
    cls_key = "Chrome_WidgetWin_1" if browser_kind == "chrome" else "MozillaWindowClass"
    candidates = []

    @ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    def enum_cb(hwnd, lparam):
        if not user32.IsWindowVisible(hwnd):
            return True
        length = user32.GetWindowTextLengthW(hwnd)
        if length <= 0:
            return True
        tbuf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, tbuf, length + 1)
        cbuf = ctypes.create_unicode_buffer(256)
        user32.GetClassNameW(hwnd, cbuf, 256)
        title = tbuf.value
        cls = cbuf.value
        if cls_key.lower() in cls.lower():
            tl = title.lower()
            if (
                "frontend-web" in tl
                or "localhost:5173" in tl
                or "version" in tl
                or "phiên bản" in tl
                or "troubleshooting" in tl
                or "gỡ rối" in tl
                or "support" in tl
            ):
                candidates.append((hwnd, title))
        return True

    user32.EnumWindows(enum_cb, 0)
    return candidates[0][0] if candidates else None


def maximize_and_focus(browser_kind: str):
    hwnd = find_browser_hwnd(browser_kind)
    if not hwnd:
        return None
    SW_MAXIMIZE = 3
    HWND_TOPMOST = -1
    SWP_NOMOVE = 0x0002
    SWP_NOSIZE = 0x0001
    SWP_SHOWWINDOW = 0x0040
    user32.ShowWindow(hwnd, SW_MAXIMIZE)
    user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW)
    user32.SetForegroundWindow(hwnd)
    return hwnd


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


def snap_and_watermark(browser_kind: str, out_path: Path):
    maximize_and_focus(browser_kind)
    time.sleep(0.5)

    screen = ImageGrab.grab().convert("RGBA")
    pw, ph = screen.size

    wm_layer = Image.new("RGBA", screen.size, (0, 0, 0, 0))
    wd = ImageDraw.Draw(wm_layer)

    f_wm = load_font(22, bold=True)
    email_txt = "23120199@student.hcmus.edu.vn"
    bbox = wd.textbbox((0, 0), email_txt, font=f_wm)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    px, py = 16, 10
    mx, my = 24, 72  # sits cleanly right above the Windows 11 Taskbar

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

    final_img = Image.alpha_composite(screen, wm_layer).convert("RGB")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    final_img.save(out_path, format="PNG", optimize=True)
    print(f"CAPTURED MAXIMIZED DESKTOP -> {out_path.name} ({final_img.size[0]}x{final_img.size[1]})")


if __name__ == "__main__":
    kind = sys.argv[1]
    target = Path(sys.argv[2])
    snap_and_watermark(kind, target)

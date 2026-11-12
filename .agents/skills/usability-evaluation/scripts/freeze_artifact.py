#!/usr/bin/env python3
"""Đóng băng bất biến đầu ra nháp của AI theo từng bước kèm dấu thời gian và mã băm SHA-256.

Ví dụ:
  python freeze_artifact.py usability/plan.md --step 0 --out usability/frozen --prefix T2 --note "AI draft plan F1"
"""
import argparse
import datetime as dt
import hashlib
import shutil
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description="Đóng băng tệp nháp AI phục vụ đối chiếu Human Review.")
    parser.add_argument("files", nargs="+", type=Path, help="Danh sách tệp cần đóng băng")
    parser.add_argument("--step", required=True, help="Mã bước thực hiện (ví dụ: 0, 1, 2)")
    parser.add_argument("--out", type=Path, required=True, help="Thư mục lưu bản đóng băng (ví dụ: usability/frozen)")
    parser.add_argument("--prefix", default="T2", help="Tiền tố đặt tên bản chụp")
    parser.add_argument("--note", default="", help="Ghi chú ngắn gọn cho INDEX.md")
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now()
    stamp = now.strftime("%Y%m%d-%H%M%S")
    index_entries = []

    for src in args.files:
        if not src.is_file():
            sys.exit(f"[ERROR] Không tìm thấy tệp nguồn cần đóng băng: {src}")
        dst = args.out / f"{args.prefix}_{src.stem}_step{args.step}_{stamp}{src.suffix}"
        if dst.exists():
            sys.exit(f"[ERROR] Bản đóng băng đã tồn tại, từ chối ghi đè: {dst}")
        shutil.copy2(src, dst)
        digest = hashlib.sha256(dst.read_bytes()).hexdigest()[:12]
        note_part = f" · {args.note}" if args.note else ""
        index_entries.append(
            f"- `{now:%Y-%m-%d %H:%M:%S}` · `{dst.name}` · Bước `{args.step}`{note_part} · `sha256:{digest}`\n"
        )
        print(f"Đã đóng băng: {dst} (sha256:{digest})")

    index_file = args.out / "INDEX.md"
    if not index_file.exists():
        index_file.write_text("# Danh Mục Các Bản Đóng Băng Đầu Ra AI (Frozen Snapshots)\n\n", encoding="utf-8")
    with open(index_file, "a", encoding="utf-8") as fh:
        fh.writelines(index_entries)


if __name__ == "__main__":
    main()

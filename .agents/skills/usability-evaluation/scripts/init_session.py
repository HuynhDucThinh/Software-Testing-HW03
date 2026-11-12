#!/usr/bin/env python3
"""Khởi tạo các khung phiếu phiên JSON trống (S00 cho Pilot, S01..S07 cho 7 phiên chính thức).

Tuyệt đối không điền sẵn dữ liệu giả lập: mọi kết quả đo lường, SUS, SEQ và câu hỏi mở đều là null.
Ví dụ:
  python init_session.py usability/sessions S00 --pilot
  python init_session.py usability/sessions S01 S02 S03 S04 S05 S06 S07 --platform "P1 - Chrome 157 / Windows 11"
"""
import argparse
import json
import re
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

TEMPLATE_PATH = Path(__file__).resolve().parents[1] / "assets" / "session_template.json"


def main():
    parser = argparse.ArgumentParser(description="Khởi tạo khung JSON rỗng cho các phiên Usability.")
    parser.add_argument("sessions_dir", type=Path, help="Thư mục lưu các phiếu phiên (ví dụ: usability/sessions)")
    parser.add_argument("session_ids", nargs="+", help="Một hoặc nhiều mã phiên dạng S00, S01..S07")
    parser.add_argument("--pilot", action="store_true", help="Đánh dấu phiên chạy thử Pilot")
    parser.add_argument("--participant", help="Ghi đè mã ẩn danh người tham gia (mặc định S0k -> P0k)")
    parser.add_argument("--platform", help="Chuỗi mô tả nền tảng thực thi mặc định (nếu cố định)")
    parser.add_argument("--milestones", nargs="*", default=[], help="Danh sách tên khóa mốc chặng rỗng cần khởi tạo")
    args = parser.parse_args()

    if not TEMPLATE_PATH.is_file():
        sys.exit(f"[ERROR] Không tìm thấy tệp mẫu: {TEMPLATE_PATH}")

    base_template = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
    args.sessions_dir.mkdir(parents=True, exist_ok=True)

    for sid in args.session_ids:
        m = re.fullmatch(r"S(\d{2})", sid)
        if not m:
            sys.exit(f"[ERROR] Mã phiên '{sid}' không hợp lệ (bắt buộc dạng S00, S01..S99).")
        num_str = m.group(1)
        out_file = args.sessions_dir / f"{sid}.json"
        if out_file.exists():
            print(f"[SKIP] Đã tồn tại '{out_file}', bỏ qua không ghi đè.")
            continue

        doc = json.loads(json.dumps(base_template))
        doc["session_id"] = sid
        doc["is_pilot"] = bool(args.pilot or sid == "S00")
        doc["participant_code"] = args.participant if (args.participant and len(args.session_ids) == 1) else f"P{num_str}"
        if args.platform:
            doc["platform"] = args.platform
        if args.milestones:
            doc["task_execution"]["milestones"] = {k: None for k in args.milestones}

        out_file.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        role_lbl = "Pilot" if doc["is_pilot"] else "Chính thức"
        print(f"Đã tạo khung rỗng: {out_file} ({role_lbl}, mã ẩn danh {doc['participant_code']})")


if __name__ == "__main__":
    main()

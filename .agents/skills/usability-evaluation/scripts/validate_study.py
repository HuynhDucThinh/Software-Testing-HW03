#!/usr/bin/env python3
"""Kiểm định tự động cấu trúc và ràng buộc chống gian lận cho nghiên cứu Usability Evaluation.

Hỗ trợ kiểm tra độc lập hoặc kết hợp:
  - Kế hoạch 9 phần (--plan plan.md)
  - Phiếu hướng dẫn & công cụ người tham gia (--kit participant_kit.md)
  - Danh sách 1 Pilot + 7 người tham gia ngoài lớp che 4 số giữa (--participants participants.md)

Sử dụng cờ --allow-pending ở Bước 0 / Bước 1 khi bảng người tham gia còn để khung mẫu chưa điền tên thật.
Trả về mã thoát 1 nếu có bất kỳ ERROR nào; mã thoát 0 nếu đạt chuẩn.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PLAN_SECTIONS = [
    ("Purpose", ["muc dich", "purpose"]),
    ("Problem Statement & Research Questions", ["cau hoi", "problem", "research"]),
    ("Test Objectives & Task Design", ["muc tieu", "nhiem vu", "objective", "task"]),
    ("User Profile & Recruitment", ["ho so", "nguoi tham gia", "user profile", "recruit"]),
    ("Method & Test Design", ["phuong phap", "method", "thiet ke phien"]),
    ("Environment & Clean State", ["moi truong", "thiet bi", "environment", "clean state"]),
    ("Test-Monitor Role & Rescue Protocol", ["dieu phoi", "can thiep", "monitor", "moderator", "rescue"]),
    ("Evaluation Measures & Instruments", ["chi so", "do luong", "measure", "instrument"]),
    ("Report Contents & Deliverables", ["noi dung bao cao", "report", "deliverable"]),
]

SCENARIO_FORBIDDEN_PATTERNS = [
    (r"\bbước\s*\d+\b", "cụm 'bước 1/2/...' (chỉ dẫn từng bước)"),
    (r"\b(bấm|nhấn|click|chọn)\s+(vào\s+)?(nút|menu|liên kết|link|ô|tab)\b", "động từ chỉ dẫn thao tác trên control"),
    (r"\bgõ\s+vào\s+ô\b", "chỉ dẫn gõ vào ô cụ thể"),
    (r"(->|→)", "ký hiệu mũi tên nối bước thao tác"),
    (r"/(register|login|forgot-password|profile|cart|checkout|admin)\b", "đường dẫn URL kỹ thuật của route"),
    (r"\b(sign\s*in|username|forgot\s*password|submit)\b", "nhãn kỹ thuật tiếng Anh trên giao diện"),
]

RAW_PHONE_RE = re.compile(r"(?<!\w)(?:0\d{8,10}|\+?84\d{8,10})(?!\w)")
MASKED_PHONE_RE = re.compile(r"\b(?:0\d{2}|\+84\d{1,2})\*{4}\d{3,4}\b")


def strip_accents(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn").replace("đ", "d")


def parse_h2_sections(md_text: str):
    sections = []
    current = None
    for line in md_text.splitlines():
        if line.startswith("## "):
            current = [line[3:].strip(), []]
            sections.append(current)
        elif current is not None:
            current[1].append(line)
    return [(heading, "\n".join(body).strip()) for heading, body in sections]


def validate_plan(path: Path, allow_pending: bool, errors: list, warnings: list):
    if not path.is_file():
        errors.append(f"plan: không tìm thấy tệp '{path}'")
        return
    raw = path.read_text(encoding="utf-8")
    norm_all = strip_accents(raw)
    secs = parse_h2_sections(raw)

    numbered = []
    for h, body in secs:
        m = re.match(r"^(\d+)\.\s*(.+)$", h)
        if m:
            numbered.append((int(m.group(1)), h, body))

    found_nums = [n for n, _, _ in numbered]
    if found_nums != list(range(1, 10)):
        errors.append(f"plan: bắt buộc có đủ 9 mục đánh số '## 1.' .. '## 9.' đúng thứ tự (hiện có: {found_nums})")

    for (num, heading, body), (expected_name, keywords) in zip(numbered, PLAN_SECTIONS):
        nh = strip_accents(heading)
        if not any(kw in nh for kw in keywords):
            warnings.append(f"plan: mục '## {heading}' chưa khớp từ khóa nhận diện của phần '{expected_name}'")
        compact_len = len(re.sub(r"\s+", "", body))
        if compact_len < 50:
            errors.append(f"plan: nội dung mục '## {heading}' quá ngắn (< 50 ký tự thực)")
        if not allow_pending and re.search(r"<[A-Z0-9_]+>|<[^>]{10,}>", body):
            errors.append(f"plan: mục '## {heading}' vẫn còn thẻ giữ chỗ '<...>' chưa điền")

    required_concepts = [
        (["sus", "ueq"], "thang đo chuẩn SUS / UEQ-S"),
        (["pilot", "chay thu"], "phiên chạy thử Pilot"),
        (["ngoai lop", "outside"], "điều kiện 7 người ngoài lớp học"),
        (["4 chu so", "4 so giua", "****", "middle four"], "quy tắc che 4 chữ số giữa của SĐT/Zalo"),
        (["thanh cong", "success"], "tiêu chí hoàn thành nhiệm vụ đo được"),
        (["benchmark", "ky vong"], "mốc thời gian kỳ vọng (benchmark)"),
    ]
    for keys, label in required_concepts:
        if not any(k in norm_all for k in keys):
            warnings.append(f"plan: chưa nêu rõ {label}")


def validate_kit(path: Path, allow_pending: bool, max_nonempty_lines: int, errors: list, warnings: list):
    if not path.is_file():
        errors.append(f"kit: không tìm thấy tệp '{path}'")
        return
    raw = path.read_text(encoding="utf-8")
    norm_all = strip_accents(raw)

    intro_checks = [
        (["khong kiem tra", "not testing you"], "lời trấn an 'kiểm tra sản phẩm, không kiểm tra bạn'"),
        (["noi to", "think aloud", "think-aloud"], "hướng dẫn nói to suy nghĩ (Think-Aloud)"),
        (["dong y", "consent"], "mục xác nhận đồng ý quay màn hình / ghi âm"),
        (["xac nhan", "tro giang", "lien he"], "thông báo trợ giảng có thể liên hệ xác minh"),
    ]
    for keys, label in intro_checks:
        if not any(k in norm_all for k in keys):
            warnings.append(f"kit: thiếu {label}")

    secs = parse_h2_sections(raw)
    task_body = None
    sus_body = None
    probe_body = None
    for h, body in secs:
        nh = strip_accents(h)
        if task_body is None and any(k in nh for k in ["nhiem vu", "task", "scenario"]) and "seq" not in nh and "do de" not in nh:
            task_body = body
        elif sus_body is None and "sus" in nh:
            sus_body = body
        elif probe_body is None and any(k in nh for k in ["hoi mo", "trao doi mo", "probe", "open"]):
            probe_body = body

    if not task_body:
        errors.append("kit: thiếu mục '## ... Nhiệm vụ ...'")
    else:
        quote_lines = [ln.lstrip("> ").strip() for ln in task_body.splitlines() if ln.strip().startswith(">")]
        scenario_text = " ".join(quote_lines)
        if not scenario_text:
            errors.append("kit: kịch bản nhiệm vụ cần đặt trong khối trích dẫn '>' để điều phối viên đọc nguyên văn")
        else:
            if not allow_pending and ("<" in scenario_text and ">" in scenario_text):
                errors.append("kit: kịch bản nhiệm vụ vẫn còn thẻ mẫu '<...>' chưa điền")
            for pat, reason in SCENARIO_FORBIDDEN_PATTERNS:
                m = re.search(pat, scenario_text, flags=re.I)
                if m:
                    errors.append(
                        f"kit: kịch bản nhiệm vụ chứa '{m.group(0)}' ({reason}) — bắt buộc viết định hướng mục tiêu, không chỉ dẫn bước/control"
                    )

    if not re.search(r"1\s*[—–-]\s*2\s*[—–-]\s*3\s*[—–-]\s*4\s*[—–-]\s*5\s*[—–-]\s*6\s*[—–-]\s*7", raw):
        warnings.append("kit: chưa có câu hỏi bổ trợ SEQ thang 1–7 (khuyến khích giữ để tăng chiều sâu phân tích)")

    if not sus_body:
        errors.append("kit: thiếu mục thang đo '## ... SUS ...'")
    else:
        item_nums = [int(x) for x in re.findall(r"^\|\s*(\d+)\s*\|", sus_body, flags=re.M)]
        if item_nums != list(range(1, 11)):
            errors.append(f"kit: bảng SUS bắt buộc có đúng 10 câu đánh số 1..10 theo thứ tự (hiện có: {item_nums})")
        if not re.search(r"\|\s*1\s*\|\s*2\s*\|\s*3\s*\|\s*4\s*\|\s*5\s*\|", sus_body):
            warnings.append("kit: tiêu đề bảng SUS nên có đủ 5 cột mức điểm 1 | 2 | 3 | 4 | 5")

    if not probe_body:
        errors.append("kit: thiếu mục câu hỏi phỏng vấn mở (Open-ended Probe Questions)")
    else:
        numbered_probes = re.findall(r"^\s*\d+\.\s+.+", probe_body, flags=re.M)
        if len(numbered_probes) < 4:
            errors.append(f"kit: bắt buộc có tối thiểu 4 câu hỏi mở, hiện có {len(numbered_probes)}")
        probe_norm = strip_accents(probe_body)
        probe_dims = [
            (["ro rang", "clarity"], "Clarity (Độ rõ ràng)"),
            (["phuc hoi", "khoi phuc", "error recovery"], "Error recovery (Phục hồi sau lỗi)"),
            (["toc do", "speed"], "Speed (Tốc độ)"),
            (["tin cay", "trust"], "Trust (Độ tin cậy)"),
        ]
        for keys, dim_label in probe_dims:
            if not any(k in probe_norm for k in keys):
                errors.append(f"kit: bộ câu hỏi mở thiếu chiều bắt buộc '{dim_label}'")

    nonempty_count = sum(1 for ln in raw.splitlines() if ln.strip())
    if nonempty_count > max_nonempty_lines:
        warnings.append(f"kit: có {nonempty_count} dòng khác rỗng (> {max_nonempty_lines}), lưu ý căn gọn khi in phát tay")


def validate_participants(path: Path, allow_pending: bool, errors: list, warnings: list):
    if not path.is_file():
        errors.append(f"participants: không tìm thấy tệp '{path}'")
        return
    raw = path.read_text(encoding="utf-8")

    # 1. Hard PII gate: never allow unmasked 9-11 digit phone numbers anywhere in the file
    raw_phones = RAW_PHONE_RE.findall(raw)
    if raw_phones:
        errors.append(
            f"participants: phát hiện số điện thoại chưa che 4 chữ số giữa ({raw_phones[0][:4]}...) — bắt buộc che dạng 090****123"
        )

    # 2. Parse markdown rows for P00 and P01..P07
    row_re = re.compile(r"^\|\s*`?(P\d{2})`?\s*\|\s*`?(S\d{2})`?\s*\|(.+)\|\s*$", flags=re.M)
    records = {}
    for m in row_re.finditer(raw):
        p_code, s_code, rest = m.group(1), m.group(2), m.group(3)
        cols = [c.strip().strip("`") for c in rest.split("|")]
        if len(cols) < 6:
            errors.append(f"participants: dòng {p_code} thiếu cột thông tin (cần đủ Họ tên, Nghề nghiệp, Nhóm, Zalo/SĐT, Ngoài lớp, Đồng ý)")
            continue
        if p_code in records:
            errors.append(f"participants: mã {p_code} bị lặp lại nhiều lần")
        records[p_code] = {
            "session": s_code,
            "name": cols[0],
            "occupation": cols[1],
            "group": cols[2],
            "contact": cols[3],
            "outside_class": cols[4],
            "consent": cols[5],
        }

    expected_codes = [f"P0{i}" for i in range(0, 8)]
    missing_codes = [c for c in expected_codes if c not in records]
    if missing_codes:
        errors.append(f"participants: thiếu các dòng mã người tham gia bắt buộc: {missing_codes} (cần P00 cho Pilot và P01..P07 cho 7 phiên chính)")
        return

    for idx in range(0, 8):
        p_code = f"P0{idx}"
        s_expected = f"S0{idx}"
        rec = records[p_code]
        if rec["session"] != s_expected:
            errors.append(f"participants: {p_code} phải ánh xạ đúng phiên {s_expected} (hiện ghi {rec['session']})")

    if allow_pending:
        return

    seen_names = set()
    seen_contacts = set()
    non_it_count = 0

    for idx in range(0, 8):
        p_code = f"P0{idx}"
        rec = records[p_code]
        for field_key, label in [("name", "Họ tên"), ("occupation", "Nghề nghiệp"), ("group", "Nhóm"), ("contact", "Liên hệ")]:
            val = rec[field_key]
            norm_v = strip_accents(val)
            if not val or any(tok in norm_v for tok in ["sv dien", "vd:", "tbd", "todo", "<"]):
                errors.append(f"participants: dòng {p_code} cột '{label}' chưa điền thông tin thật ('{val}')")

        masked_hit = MASKED_PHONE_RE.search(rec["contact"])
        if not masked_hit:
            errors.append(
                f"participants: dòng {p_code} cột Liên hệ ('{rec['contact']}') chưa đúng chuẩn SĐT/Zalo che 4 chữ số giữa (ví dụ: 090****123)"
            )
        else:
            phone_tok = masked_hit.group(0)
            if phone_tok in seen_contacts:
                errors.append(f"participants: SĐT/Zalo đã che '{phone_tok}' ở {p_code} bị trùng với người tham gia khác")
            seen_contacts.add(phone_tok)

        clean_name = strip_accents(rec["name"]).strip()
        if clean_name in seen_names:
            errors.append(f"participants: Họ tên '{rec['name']}' ở {p_code} bị trùng lặp (Pilot và 7 người chính phải là 8 người độc lập)")
        seen_names.add(clean_name)

        if strip_accents(rec["outside_class"]) not in ("co", "yes", "true"):
            errors.append(f"participants: {p_code} bắt buộc là người ngoài lớp học HW03 (cột Ngoài lớp phải là 'Có')")
        if strip_accents(rec["consent"]) not in ("co", "yes", "true"):
            errors.append(f"participants: {p_code} cần xác nhận đồng ý để trợ giảng liên hệ xác minh ('Có')")

        if idx >= 1 and "non-it" in rec["group"].lower():
            non_it_count += 1

    if non_it_count == 0:
        warnings.append("participants: chưa ghi nhận người tham gia thuộc nhóm non-IT (đề bài khuyến khích ưu tiên người dùng phổ thông không chuyên CNTT)")


def main():
    parser = argparse.ArgumentParser(description="Kiểm định kế hoạch, phiếu khảo sát và bảng người tham gia Usability.")
    parser.add_argument("--plan", type=Path, help="Đường dẫn tới plan.md")
    parser.add_argument("--kit", type=Path, help="Đường dẫn tới participant_kit.md")
    parser.add_argument("--participants", type=Path, help="Đường dẫn tới participants.md")
    parser.add_argument("--allow-pending", action="store_true", help="Cho phép ô giữ chỗ ở Bước 0 / Bước 1 trước khi thu dữ liệu thật")
    parser.add_argument("--max-kit-lines", type=int, default=85, help="Ngưỡng dòng cảnh báo độ dài phiếu phát tay")
    args = parser.parse_args()

    if not (args.plan or args.kit or args.participants):
        parser.error("Cần truyền ít nhất một trong các tham số: --plan, --kit, --participants")

    errors, warnings = [], []
    if args.plan:
        validate_plan(args.plan, args.allow_pending, errors, warnings)
    if args.kit:
        validate_kit(args.kit, args.allow_pending, args.max_kit_lines, errors, warnings)
    if args.participants:
        validate_participants(args.participants, args.allow_pending, errors, warnings)

    for e in errors:
        print(f"[ERROR] {e}")
    for w in warnings:
        print(f"[WARN]  {w}")
    print(f"Kết quả kiểm định: {len(errors)} lỗi, {len(warnings)} cảnh báo.")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

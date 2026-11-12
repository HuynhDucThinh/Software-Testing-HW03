#!/usr/bin/env python3
"""Kiểm định tính toàn vẹn dữ liệu phiên thử nghiệm & Tính toán thống kê SUS + Hiệu năng (Task 2 HW03).

Chức năng:
  1. --check: Kiểm tra nghiêm ngặt toàn bộ phiếu S*.json (chống rò rỉ SĐT/email cá nhân, cấm thiếu câu SUS,
     kiểm tra logic trạng thái hoàn thành vs sự kiện cứu hộ, kiểm đủ số phiên chính thức --expect 7).
  2. Chế độ tính toán đầy đủ:
     - Tính điểm SUS chuẩn Brooke (1996): câu lẻ (x - 1), câu chẵn (5 - x), tổng * 2.5 -> thang 0.0..100.0.
     - Xuất ma trận chi tiết từng câu Q1..Q10 của cả 7 người tham gia chính thức (tách riêng phiên Pilot S00).
     - Tính Mean, SD mẫu (n - 1), Median, Min-Max, đối chiếu mốc chuẩn 68.0, mức chấp nhận Bangor và hạng chữ Sauro-Lewis.
     - Tính tỷ lệ hoàn thành (độc lập / có cứu hộ lỗi chặn / không hoàn thành), thống kê thời gian và tần suất lỗi/do dự.
     - Trích xuất nguyên văn danh mục sự kiện lỗi (is_bug: true) hỗ trợ đối chiếu GitHub Issues ở Bước 5.
"""
import argparse
import json
import re
import statistics as st
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

VALID_COMPLETION = ("khong_tro_giup", "co_tro_giup", "khong_hoan_thanh")
COMPLETION_LABELS = {
    "khong_tro_giup": "Hoàn thành độc lập",
    "co_tro_giup": "Hoàn thành (có cứu hộ lỗi chặn)",
    "khong_hoan_thanh": "Không hoàn thành",
}
PROBE_KEYS = ("clarity", "error_recovery", "speed", "trust")
MMSS_RE = re.compile(r"^(\d{1,3}):([0-5]\d)$")
RAW_PHONE_RE = re.compile(r"(?<!\w)(?:0\d{8,10}|\+?84\d{8,10})(?!\w)")
EMAIL_RE = re.compile(r"[\w.+-]+@([\w-]+\.[\w.-]+)")
SAFE_TEST_DOMAINS = {"example.com", "eshop.com", "test.local", "localhost"}


def parse_mmss(val) -> int | None:
    if not isinstance(val, str):
        return None
    m = MMSS_RE.match(val.strip())
    if not m:
        return None
    return int(m.group(1)) * 60 + int(m.group(2))


def format_mmss(seconds: float) -> str:
    sec_int = int(round(seconds))
    return f"{sec_int // 60:02d}:{sec_int % 60:02d}"


def compute_sus_contributions(answers: list[int]) -> list[int]:
    return [(val - 1) if idx % 2 == 0 else (5 - val) for idx, val in enumerate(answers)]


def compute_sus_total(answers: list[int]) -> float:
    return 2.5 * sum(compute_sus_contributions(answers))


def classify_sus(score: float) -> tuple[str, str, str]:
    """Trả về (Bangor Acceptability, Adjective Rating, Sauro-Lewis Grade)."""
    if score >= 84.1:
        grade = "A+"
    elif score >= 80.8:
        grade = "A"
    elif score >= 78.9:
        grade = "A-"
    elif score >= 77.2:
        grade = "B+"
    elif score >= 74.1:
        grade = "B"
    elif score >= 72.6:
        grade = "B-"
    elif score >= 71.1:
        grade = "C+"
    elif score >= 65.0:
        grade = "C"
    elif score >= 62.7:
        grade = "C-"
    elif score >= 51.7:
        grade = "D"
    else:
        grade = "F"

    if score >= 68.0:
        acceptability = "Acceptable (Đạt chuẩn >= 68.0)"
    elif score >= 51.7:
        acceptability = "Marginal (Cận biên — Cần cải thiện)"
    else:
        acceptability = "Not Acceptable (Kém — Dưới ngưỡng chấp nhận)"

    if score >= 85.0:
        adj = "Excellent"
    elif score >= 72.6:
        adj = "Good"
    elif score >= 51.7:
        adj = "OK / Fair"
    elif score >= 38.0:
        adj = "Poor"
    else:
        adj = "Worst Imaginable"

    return acceptability, adj, grade


def count_events(doc: dict, ev_type: str) -> int:
    return sum(1 for e in (doc.get("events") or []) if e.get("type") == ev_type)


def count_assists(doc: dict) -> int:
    return max(count_events(doc, "A"), len(doc.get("assists") or []))


def validate_session(path: Path, doc: dict, allowed_emails: set[str]) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    raw_text = path.read_text(encoding="utf-8")

    # PII checks inside anonymous session JSON
    for pm in RAW_PHONE_RE.finditer(raw_text):
        errors.append(
            f"Phát hiện chuỗi số giống SĐT cá nhân ({pm.group(0)[:4]}...) — tuyệt đối không lưu SĐT thật vào JSON (chỉ lưu ở participants.md đã che 4 số giữa)"
        )
        break
    for em in EMAIL_RE.finditer(raw_text):
        full_mail = em.group(0).lower()
        domain = em.group(1).lower()
        if full_mail not in allowed_emails and domain not in SAFE_TEST_DOMAINS:
            errors.append(
                f"Phát hiện địa chỉ email ngoài tên miền test ({full_mail[:3]}...@{domain}) — ẩn danh hóa hoặc thêm --allow-email nếu là dữ liệu kiểm thử"
            )
            break

    if doc.get("session_id") != path.stem:
        errors.append(f"session_id={doc.get('session_id')!r} không khớp tên tệp '{path.stem}'")

    is_pilot = doc.get("is_pilot")
    if path.stem == "S00" and is_pilot is not True:
        errors.append("Phiên S00 bắt buộc đặt 'is_pilot': true")
    if path.stem != "S00" and is_pilot is not False:
        errors.append(f"Phiên chính thức {path.stem} bắt buộc đặt 'is_pilot': false")

    p_code = str(doc.get("participant_code") or "")
    if not re.fullmatch(r"P\d{2}", p_code):
        errors.append(f"participant_code={p_code!r} không hợp lệ (cần mã ẩn danh P00, P01..P07)")

    if not doc.get("date"):
        warnings.append("Chưa ghi ngày thực hiện ('date')")
    if doc.get("clean_state_reset") is not True:
        errors.append("clean_state_reset phải là true (xác nhận đã khởi tạo lại CSDL sạch trước phiên)")

    consent = doc.get("consent") or {}
    if consent.get("ta_verification_contact") is not True:
        warnings.append("consent.ta_verification_contact chưa đặt true")

    te = doc.get("task_execution") or {}
    comp = te.get("completion_status")
    if comp not in VALID_COMPLETION:
        errors.append(f"task_execution.completion_status phải thuộc {VALID_COMPLETION} (hiện tại: {comp!r})")
    if parse_mmss(te.get("total_duration")) is None:
        errors.append(f"task_execution.total_duration={te.get('total_duration')!r} thiếu hoặc sai định dạng mm:ss")

    for mk, mv in (te.get("milestones") or {}).items():
        if mv not in (None, "") and parse_mmss(mv) is None:
            errors.append(f"Mốc thời gian milestones.{mk}={mv!r} sai định dạng mm:ss")

    n_assist = count_assists(doc)
    if comp == "khong_tro_giup" and n_assist > 0:
        errors.append("Có ghi nhận can thiệp/cứu hộ (assists > 0) nhưng completion_status lại để 'khong_tro_giup'")
    if comp == "co_tro_giup" and n_assist == 0:
        warnings.append("completion_status là 'co_tro_giup' nhưng mảng 'assists' đang rỗng")

    seq = doc.get("seq")
    if seq is not None and not (isinstance(seq, int) and not isinstance(seq, bool) and 1 <= seq <= 7):
        errors.append(f"seq={seq!r} không hợp lệ (phải là số nguyên 1..7 hoặc null)")

    sus = doc.get("sus")
    if not (isinstance(sus, list) and len(sus) == 10):
        errors.append("Trường 'sus' bắt buộc là mảng gồm đúng 10 câu trả lời")
    else:
        invalid_q = [
            idx + 1
            for idx, v in enumerate(sus)
            if not (isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 5)
        ]
        if invalid_q:
            errors.append(f"Các câu SUS {invalid_q} đang trống (null) hoặc ngoài thang 1..5 — không được bỏ trống hay ước lượng")

    probes = doc.get("open_probes") or {}
    missing_probes = [k for k in PROBE_KEYS if not str(probes.get(k) or "").strip()]
    if missing_probes:
        errors.append(f"Thiếu nội dung trả lời phỏng vấn mở ở các chiều: {missing_probes}")

    for idx, ev in enumerate(doc.get("events") or []):
        if ev.get("type") not in ("E", "H", "Q", "A"):
            errors.append(f"events[{idx}].type={ev.get('type')!r} không thuộc ('E', 'H', 'Q', 'A')")
        if parse_mmss(ev.get("t")) is None:
            warnings.append(f"events[{idx}].t={ev.get('t')!r} không đúng định dạng mm:ss")

    return errors, warnings


def describe_numeric(values: list[float]) -> dict | None:
    if not values:
        return None
    return {
        "n": len(values),
        "mean": st.mean(values),
        "sd": st.stdev(values) if len(values) > 1 else 0.0,
        "median": st.median(values),
        "min": min(values),
        "max": max(values),
    }


def build_markdown_report(pilot_rows: list[dict], official_rows: list[dict], benchmark_sec: int | None, expected_n: int | None) -> str:
    lines = [
        "# Báo Cáo Tính Toán Điểm SUS & Thống Kê Hiệu Năng Thực Nghiệm (Sinh Tự Động)",
        "",
        "> Công thức chuẩn System Usability Scale (Brooke, 1996): câu lẻ `(x - 1)`, câu chẵn `(5 - x)`, tổng điểm quy đổi `= tổng đóng góp * 2.5` (thang `0.0 .. 100.0`). Phiên chạy thử Pilot (`S00`) được tách riêng, không gộp vào thống kê của 7 phiên chính thức.",
        "",
    ]

    # 1. Pilot summary
    if pilot_rows:
        lines += [
            "## 1. Tóm tắt Phiên Chạy Thử Nghiệm Pilot (`S00`)",
            "",
            "| Mã phiên | Mã người TG | Nhóm | Nền tảng | Kết quả hoàn thành | Thời gian | Lỗi (`E`) | Do dự (`H`) | Cứu hộ (`A`) | SEQ (`1–7`) | SUS (`0–100`) |",
            "| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        for r in pilot_rows:
            seq_str = str(r["seq"]) if r["seq"] is not None else "—"
            lines.append(
                f"| `{r['sid']}` | `{r['p_code']}` | `{r['group']}` | {r['platform']} | {COMPLETION_LABELS[r['comp']]} | `{format_mmss(r['sec'])}` | {r['E']} | {r['H']} | {r['A']} | {seq_str} | **{r['sus_total']:.1f}** |"
            )
        lines.append("")

    # 2. Official sessions performance table
    lines += [
        "## 2. Tổng Hợp Kết Quả Thực Thi 7 Phiên Chính Thức (`S01` .. `S07`)",
        "",
        "| Mã phiên | Mã người TG | Nhóm | Kết quả hoàn thành | Thời gian | Lỗi (`E`) | Do dự (`H`) | Cứu hộ (`A`) | SEQ (`1–7`) | SUS (`0–100`) | Xếp hạng SUS |",
        "| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]
    for r in official_rows:
        _, adj, grade = classify_sus(r["sus_total"])
        seq_str = str(r["seq"]) if r["seq"] is not None else "—"
        lines.append(
            f"| `{r['sid']}` | `{r['p_code']}` | `{r['group']}` | {COMPLETION_LABELS[r['comp']]} | `{format_mmss(r['sec'])}` | {r['E']} | {r['H']} | {r['A']} | {seq_str} | **{r['sus_total']:.1f}** | `{grade}` ({adj}) |"
        )
    lines.append("")

    # 3. Item-by-item Q1..Q10 SUS matrix
    lines += [
        "## 3. Ma Trận Điểm Gốc (`1..5`) & Điểm Quy Đổi Chi Tiết Từng Câu `SUS` (`Q1` .. `Q10`)",
        "",
        "| Phiên (`Người TG`) | Q1 (+) | Q2 (-) | Q3 (+) | Q4 (-) | Q5 (+) | Q6 (-) | Q7 (+) | Q8 (-) | Q9 (+) | Q10 (-) | Tổng quy đổi (`0–40`) | Điểm `SUS` (`x 2.5`) |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for r in official_rows:
        raw_q = r["sus_raw"]
        contrib = compute_sus_contributions(raw_q)
        cells = " | ".join(f"{raw_q[i]} (`{contrib[i]}`)" for i in range(10))
        lines.append(f"| `{r['sid']}` (`{r['p_code']}`) | {cells} | `{sum(contrib)}` | **{r['sus_total']:.1f}** |")

    if official_rows:
        avg_raw = [st.mean(r["sus_raw"][i] for r in official_rows) for i in range(10)]
        avg_con = [st.mean(compute_sus_contributions(r["sus_raw"])[i] for r in official_rows) for i in range(10)]
        avg_cells = " | ".join(f"{avg_raw[i]:.2f} (`{avg_con[i]:.2f}`)" for i in range(10))
        mean_sum_con = sum(avg_con)
        lines.append(f"| **Trung bình câu** | {avg_cells} | `{mean_sum_con:.2f}` | **{mean_sum_con * 2.5:.1f}** |")
    lines.append("")

    # 4. Aggregate statistical summary
    n = len(official_rows)
    sus_stats = describe_numeric([r["sus_total"] for r in official_rows])
    seq_vals = [r["seq"] for r in official_rows if r["seq"] is not None]
    seq_stats = describe_numeric(seq_vals)
    completed_rows = [r for r in official_rows if r["comp"] != "khong_hoan_thanh"]
    dur_stats = describe_numeric([r["sec"] for r in completed_rows])

    def fmt_ratio(cnt: int) -> str:
        return f"{cnt}/{n} ({100.0 * cnt / n:.1f}%)" if n else "—"

    lines += [
        "## 4. Bảng Thống Kê Tổng Hợp Khả Năng Sử Dụng & Hiệu Năng",
        "",
        "| Chỉ số đo lường (Metric) | Giá trị thống kê | Đối chiếu chuẩn / Ghi chú |",
        "| :--- | :---: | :--- |",
        f"| **Số phiên chính thức hợp lệ (`n`)** | `{n}`" + (f" / `{expected_n}`" if expected_n else "") + " | Tách biệt hoàn toàn khỏi phiên Pilot `S00` |",
    ]
    if sus_stats:
        acc, adj, grade = classify_sus(sus_stats["mean"])
        diff_68 = sus_stats["mean"] - 68.0
        sign_str = f"+{diff_68:.1f}" if diff_68 >= 0 else f"{diff_68:.1f}"
        lines += [
            f"| **Điểm `SUS` trung bình ± Độ lệch chuẩn (`Mean ± SD`)** | **`{sus_stats['mean']:.1f} ± {sus_stats['sd']:.1f}`** | Lệch `{sign_str}` điểm so với mốc trung bình lịch sử `68.0` |",
            f"| **Điểm `SUS` trung vị & Khoảng biến thiên (`Median · Min–Max`)** | `{sus_stats['median']:.1f}` (`{sus_stats['min']:.1f} – {sus_stats['max']:.1f}`) | Hạng **`{grade}`** · `{adj}` · {acc} |",
        ]
    if seq_stats:
        lines.append(
            f"| **Độ dễ sau nhiệm vụ `SEQ` (`Mean ± SD` · `Median`)** | `{seq_stats['mean']:.2f} ± {seq_stats['sd']:.2f}` (`Median: {seq_stats['median']:.1f}`) | Thang `1..7` (mốc trung bình tham chiếu `~5.5`) |"
        )
    if n:
        c_indep = sum(1 for r in official_rows if r["comp"] == "khong_tro_giup")
        c_assist = sum(1 for r in official_rows if r["comp"] == "co_tro_giup")
        c_fail = sum(1 for r in official_rows if r["comp"] == "khong_hoan_thanh")
        lines += [
            f"| **Hoàn thành độc lập (không cần cứu hộ)** | `{fmt_ratio(c_indep)}` | Người dùng tự hoàn tất toàn bộ luồng |",
            f"| **Hoàn thành có cứu hộ tại điểm lỗi chặn SUT** | `{fmt_ratio(c_assist)}` | Áp dụng *System-Bug Rescue Protocol* sau `>= 90s` |",
            f"| **Không hoàn thành nhiệm vụ** | `{fmt_ratio(c_fail)}` | Dừng phiên hoặc vượt thời gian tối đa |",
            f"| **Tổng tỷ lệ đi tới đích cuối luồng** | `{fmt_ratio(len(completed_rows))}` | Tính chung cả độc lập và có cứu hộ kỹ thuật |",
        ]
        if benchmark_sec is not None:
            within_bm = sum(1 for r in completed_rows if r["sec"] <= benchmark_sec)
            lines.append(
                f"| **Hoàn thành trong mốc Benchmark (`<= {format_mmss(benchmark_sec)}`)** | `{fmt_ratio(within_bm)}` | So với ngưỡng mục tiêu trong `plan.md` |"
            )
    if dur_stats:
        lines.append(
            f"| **Thời gian thực hiện (`Mean ± SD` · `Median` · `Min–Max`)** | `{format_mmss(dur_stats['mean'])} ± {format_mmss(dur_stats['sd'])}` (`Med: {format_mmss(dur_stats['median'])}`, `{format_mmss(dur_stats['min'])}–{format_mmss(dur_stats['max'])}`) | Tính trên các phiên đi hết luồng |"
        )
    if n:
        mean_e = st.mean(r["E"] for r in official_rows)
        mean_h = st.mean(r["H"] for r in official_rows)
        mean_a = st.mean(r["A"] for r in official_rows)
        lines.append(
            f"| **Trung bình Lỗi (`E`) / Do dự (`H`) / Cứu hộ (`A`) mỗi phiên** | `{mean_e:.2f}` / `{mean_h:.2f}` / `{mean_a:.2f}` | Đo mật độ ma sát tương tác trung bình |"
        )
    lines.append("")

    # 5. Extracted bug events across sessions
    bug_events = []
    for r in pilot_rows + official_rows:
        tag = f"{r['sid']} (Pilot)" if r["is_pilot"] else r["sid"]
        for ev in r["events"]:
            if ev.get("is_bug") is True:
                bug_events.append(
                    (
                        tag,
                        ev.get("t") or "—",
                        ev.get("screen") or "—",
                        ev.get("type") or "—",
                        (ev.get("description") or "").replace("|", "\\|"),
                        ev.get("known_bug_id") or "Cần kiểm tra / Bug mới",
                    )
                )

    lines += [
        "## 5. Danh Mục Sự Kiện Lỗi Kỹ Thuật Ghi Nhận Từ Các Phiên (`is_bug: true`)",
        "",
        "| Phiên | Mốc `mm:ss` | Màn hình | Loại | Ghi nhận nguyên văn tại hiện trường | Mã Bug đối chiếu |",
        "| :---: | :---: | :--- | :---: | :--- | :---: |",
    ]
    if bug_events:
        for b_sid, b_t, b_scr, b_type, b_desc, b_id in bug_events:
            lines.append(f"| `{b_sid}` | `{b_t}` | {b_scr} | `{b_type}` | {b_desc} | `{b_id}` |")
    else:
        lines.append("| — | — | — | — | Không có sự kiện nào gắn cờ `is_bug: true` | — |")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Kiểm định phiếu JSON và tính thống kê SUS cho Task 2.")
    parser.add_argument("sessions_dir", type=Path, help="Thư mục chứa các tệp S00.json, S01.json..S07.json")
    parser.add_argument("--check", action="store_true", help="Chỉ chạy kiểm tra tính hợp lệ, không xuất bảng thống kê")
    parser.add_argument("--expect", type=int, help="Số lượng phiên chính thức bắt buộc (ví dụ: 7)")
    parser.add_argument("--benchmark", help="Mốc thời gian kỳ vọng dạng mm:ss (ví dụ: 05:00)")
    parser.add_argument("--allow-email", action="append", default=[], help="Email kiểm thử cụ thể được phép xuất hiện trong JSON")
    parser.add_argument("-o", "--out", type=Path, help="Tệp Markdown lưu bảng kết quả tính toán")
    args = parser.parse_args()

    session_files = sorted(args.sessions_dir.glob("S*.json"))
    if not session_files:
        sys.exit(f"[ERROR] Không tìm thấy bất kỳ tệp S*.json nào trong '{args.sessions_dir}'.")

    allowed_emails = {e.lower() for e in args.allow_email}
    total_errors = 0
    pilot_rows = []
    official_rows = []
    seen_participants = set()

    for sf in session_files:
        try:
            doc = json.loads(sf.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"[ERROR] {sf.name}: Cú pháp JSON không hợp lệ — {exc}")
            total_errors += 1
            continue

        errs, warns = validate_session(sf, doc, allowed_emails)
        p_code = doc.get("participant_code")
        if p_code in seen_participants:
            errs.append(f"Mã người tham gia '{p_code}' bị trùng lặp với một phiếu phiên khác")
        if p_code:
            seen_participants.add(p_code)

        role_note = " (Pilot)" if doc.get("is_pilot") else ""
        for e in errs:
            print(f"[ERROR] {sf.name}{role_note}: {e}")
        for w in warns:
            print(f"[WARN]  {sf.name}{role_note}: {w}")
        total_errors += len(errs)

        if errs:
            continue

        row = {
            "sid": doc["session_id"],
            "is_pilot": bool(doc.get("is_pilot")),
            "p_code": doc["participant_code"],
            "group": doc.get("user_group") or "—",
            "platform": doc.get("platform") or "—",
            "comp": doc["task_execution"]["completion_status"],
            "sec": parse_mmss(doc["task_execution"]["total_duration"]),
            "E": count_events(doc, "E"),
            "H": count_events(doc, "H"),
            "A": count_assists(doc),
            "seq": doc.get("seq"),
            "sus_raw": doc["sus"],
            "sus_total": compute_sus_total(doc["sus"]),
            "events": doc.get("events") or [],
        }
        if row["is_pilot"]:
            pilot_rows.append(row)
        else:
            official_rows.append(row)

    if args.expect is not None and len(official_rows) != args.expect:
        print(
            f"[ERROR] Số phiên chính thức hợp lệ hiện có là {len(official_rows)}, không khớp mức yêu cầu --expect {args.expect}."
        )
        total_errors += 1

    print(
        f"Tổng kết kiểm tra: {len(session_files)} tệp đọc ({len(pilot_rows)} Pilot, {len(official_rows)} phiên chính hợp lệ), {total_errors} lỗi."
    )

    if args.check or total_errors > 0:
        sys.exit(1 if total_errors > 0 else 0)

    bm_sec = parse_mmss(args.benchmark) if args.benchmark else None
    if args.benchmark and bm_sec is None:
        sys.exit(f"[ERROR] Giá trị --benchmark '{args.benchmark}' không đúng định dạng mm:ss.")

    report_md = build_markdown_report(pilot_rows, official_rows, bm_sec, args.expect)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report_md, encoding="utf-8")
        print(f"Đã xuất báo cáo thống kê SUS & hiệu năng tại: {args.out}")
    else:
        print("\n" + report_md)


if __name__ == "__main__":
    main()

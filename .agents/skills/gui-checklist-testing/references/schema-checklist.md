# Schema `checklist.json`

Một file cho một phạm vi (nhóm màn hình). UTF-8, `ensure_ascii=False`, thụt 2. Đường dẫn: `checklist/checklist.json`.

```jsonc
{
  "meta": {
    "hw": "HW03",
    "task": "T1 - GUI Checklist",
    "scope": "M1 - Auth & Profile (Register, Login, ForgotPassword, Profile, Header)",
    "sut_version": "eshop-sut @ <commit>",
    "test_basis": "eshop-sut/README.md (SRS v2.0) FR-01..04, FR-21..24; slide Nhom05",
    "platforms": {"P1": "Chrome trên Windows", "P2": "Firefox trên Windows", "P3": "Safari/Android Chrome/Expo Go"},
    "result_values": ["Passed", "Failed", "N/A", "Blocked"],
    "inventory": "checklist/m1_inventory.md",
    "version": "v1 - AI nháp (T1 bước 1)",
    "step": 1                       // tuỳ chọn: bước đã xong
  },
  "assumptions": {                  // mã -> nội dung; GAx = quyết định Expected, NAx = nền tảng không áp dụng
    "GA1": "...", "NA1": "..."
  },
  "items": [ { /* item */ } ]
}
```

## Item

| Trường | Bắt buộc | Kiểu | Ghi chú |
|---|---|---|---|
| `id` | có | `CL-01`... hoặc `SV-01`... | duy nhất, không đánh lại số khi xoá |
| `ia` | có | `IA-01`...`IA-04` | IA-01 chuẩn chung, IA-02 form, IA-03 điều hướng, IA-04 phản hồi/trạng thái |
| `man_hinh` | có | chuỗi | màn hình / vùng |
| `muc_kiem_tra` | có | chuỗi | ngắn, một ý, viết trung lập |
| `can_cu` | có | chuỗi | mã điều khoản + `file:dòng`, hoặc tên heuristic/checklist |
| `loai_nguon` | có | `SRS` / `Control` / `Heuristic` | 3 nguồn checklist của bài giảng |
| `expected` | có | chuỗi | công thức slide 12 + câu "Fail nếu ..." |
| `uu_tien` | có | `Mandatory` / `Optional` | |
| `nen_tang` | có | mảng mã nền tảng | nền tảng áp dụng |
| `nguon` | có | `AI` / `SV` / `Both` | AI đề xuất / SV thêm / SV sửa đáng kể |
| `na` | khi thiếu nền tảng | `{Px: "Giả định NAx: ..."}` | mỗi nền tảng bị bỏ một lý do |
| `loai_loi` | | `Visual-Layout` / `State` / `Responsive` / `Typo-Localization` | nhóm lỗi nếu item Failed (slide 9) |
| `du_lieu` | | mảng `{gia_tri, ket_qua_mong_doi}` | bảng data-driven (slide 18), vd email hợp lệ / sai định dạng / rỗng |
| `viewport` | | `375` / `768` / `1440` hoặc mảng | khi item phụ thuộc kích thước màn hình |
| `tien_dieu_kien` | | chuỗi | dữ liệu cần dựng, trạng thái đăng nhập, công cụ |
| `gia_dinh` | | chuỗi chứa mã `GAx` | khi Expected dựa vào giả định |
| `ly_do_ai_bo_sot` | item `SV` | chuỗi hoặc `{loai, giai_thich}` | SV viết; `loai` thuộc `prompt` / `giới hạn model` / `đặc điểm giao diện` / `khác` |
| `luc_them` | | chuỗi | thêm trước khi chạy / trong lúc chạy Px (ghi trung thực) |
| `ket_qua` | sau bước 4 | `{Px: "Passed"/"Failed"/"N/A"/"Blocked"}` | |
| `notes_nt` | Failed/Blocked | `{Px: "..."}` | Actual nguyên văn + lý do; Blocked ghi item gốc |
| `evidence` | Failed | `{Px: ["screenshots/task1_failed/P1_CL-05.png"]}` | ảnh có overlay |
| `run` | sau bước 4 | `{Px: "checklist/runs/P1_20261112-0930.csv"}` | lượt đã gộp |
| `notes` | | chuỗi | ghi chú chung |
| `che_do` | bước 3 | `auto` / `manual` / `mixed` | cách chạy |
| `che_do_ghi_chu` | mixed/manual | chuỗi | phần chạy tay / lý do cần mắt người |
| `auto_status`, `auto_notes`, `auto_evidence`, `auto_run` | sau lượt auto | `{Px: ...}` | kết quả Playwright, không phải verdict |

## Ví dụ item (minh hoạ định dạng, không phải nội dung chính thức)

```json
{
  "id": "CL-01", "ia": "IA-02", "man_hinh": "Register",
  "muc_kiem_tra": "Kiểu dữ liệu của ô Email",
  "can_cu": "FR-22 (README.md:253)", "loai_nguon": "SRS",
  "expected": "Ô Email trên /register có type=\"email\" (DevTools > Elements). Fail nếu type khác \"email\".",
  "uu_tien": "Mandatory", "nen_tang": ["P1", "P2", "P3"], "nguon": "AI"
}
```

## File lượt chạy (đầu vào `merge_platform.py`)

CSV UTF-8, có header: `id,status,notes,evidence` (evidence nhiều ảnh cách nhau bởi `;`). Hoặc JSON:

```json
{"platform": "P1", "run_at": "2026-11-12 09:30", "env": "Chrome 142 / Windows 11",
 "results": {"CL-01": {"status": "Failed", "notes": "...", "evidence": ["...png"]}}}
```

## Quy tắc tên ảnh

- Item Failed: `P<n>_<id>.png` trong `screenshots/task1_failed/` (nhiều ảnh: `P<n>_<id>_<k>.png`).
- Ảnh tổng quan cross-platform: `P<n>_<màn hình>_1.png` trong `screenshots/task3_cross_platform/`.
- Bản gốc chưa nén để trong `evidence_raw/` (đã gitignore).

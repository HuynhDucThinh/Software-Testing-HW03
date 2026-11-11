# 2026-11-11 - Task 1 Bước 2: Kiểm cấu trúc, gộp mục bổ sung của sinh viên và xuất ma trận độ phủ

**Tool:** Antigravity
**Date and time:** 2026-11-11 15:25 +07:00
**Task / Step:** Task 1, Bước 2 (Gộp mục bổ sung `SV-01`..`SV-20` và kiểm chuẩn ma trận độ phủ)
**Prompt:**
Đã review sv_items.md, gộp bước 2

**AI output:**
Đã kiểm tra cấu trúc `checklist/sv_items.md`, chép nguyên văn 20 mục `SV-01`..`SV-20` cùng 4 giả định bổ sung (`GA6`, `GA7`, `GA8`, `NA2`) vào `checklist/checklist.json` (`step: 2`), xuất lại `checklist/M1_GUI_Checklist.md`, đóng băng bản chuẩn Bước 2 bằng `freeze.py --step 2`, chạy kiểm tra schema bằng `check_checklist.py --min 41 --min-per-ia 8` và in ma trận độ phủ bằng `coverage_matrix.py`:
- Tổng số mục thiết kế: 59 mục (`AI`: 37, `Both`: 2, `SV`: 20), vượt ngưỡng tối thiểu `> 40` mục.
- Phân bổ theo nhóm IA: `IA-01`: 14, `IA-02`: 23, `IA-03`: 12, `IA-04`: 10 (mọi IA đều đạt tối thiểu 8 mục).
- Phân bổ theo loại nguồn: `SRS`: 37, `Control`: 10, `Heuristic`: 12.
- Số mục áp dụng theo nền tảng: `P1`: 58, `P2`: 58, `P3`: 52 (các mục `N/A` đều gắn mã giả định hợp lệ `NA1` hoặc `NA2`).
- Kết quả `check_checklist.py`: `0 lỗi, 0 cảnh báo`, toàn bộ 20 mục `SV` đều có đủ trường `ly_do_ai_bo_sot` và ngưỡng `Fail nếu`.

**Kept:** Giữ nguyên kết quả gộp nguyên văn 20 mục `SV-01`..`SV-20`, các giả định `GA6`..`GA8`, `NA2`, file `checklist/M1_GUI_Checklist.md` (59 mục) và ma trận độ phủ để chuyển sang Bước 3 chuẩn bị thực thi.
**Changed:** Không chỉnh sửa nội dung các mục `CL-01`..`CL-39` hay `SV-01`..`SV-20` trong quá trình gộp tự động.
**Rejected:** Không loại bỏ mục nào.
**By hand:** Sinh viên rà soát toàn bộ `checklist/sv_items.md` (bao gồm 20 mục bổ sung, ngưỡng `Fail nếu`, giả định `GA6`..`GA8`, `NA2` và phân tích `ly_do_ai_bo_sot` cho từng mục) trước khi yêu cầu gộp vào `checklist/checklist.json`.

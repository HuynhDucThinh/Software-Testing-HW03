# 2026-11-11 - Task 1 Bước 1 (Lượt 1/4): AI nháp checklist cho IA-01 (General UI Standards)

**Tool:** Antigravity
**Date and time:** 2026-11-11 14:16 +07:00
**Task / Step:** Task 1, Bước 1, Lượt IA-01 (General UI Standards)
**Prompt:**
Dùng skill gui-checklist-testing, bước 1 - lượt IA-01. Làm xong báo cáo kết quả thực hiện yêu cầu nào? làm những gì? tôi cần check các nội dung nào?

**AI output:**
Đã đọc `references/slide-checklist.md`, `checklist/m1_inventory.md` và `checklist/m1_test_basis.md`, sinh 11 mục checklist nháp đầu tiên (`CL-01` .. `CL-11`) cho nhóm `IA-01` trong `checklist/checklist.json` (kèm 2 giả định `GA1`, `GA2`), xuất bảng Markdown `checklist/M1_GUI_Checklist.md` và đóng băng bản nháp lượt IA-01 vào `checklist/ai-outputs/`:
- Nguồn SRS (8 mục): `CL-01`, `CL-02` (nhất quán ngôn ngữ tiếng Việt - FR-21:244), `CL-03`..`CL-06` (đúng 1 thẻ `<h1>` và nội dung tiêu đề khớp chức năng cho Register, Login, ForgotPassword, Profile - FR-21:247 & FR-05:81), `CL-07`, `CL-08` (nhất quán màu xanh dương nút tích cực, nút phụ và màu đỏ nút đăng xuất - FR-21:245).
- Nguồn Control (2 mục): `CL-09` (căn lề thẳng hàng theo lưới - Slide 10 #1), `CL-10` (responsive không tràn ngang / không đè chồng ở 375px, 768px, 1440px - Slide 10 #17, #18, #19 & Slide 31).
- Nguồn Heuristic (1 mục): `CL-11` (độ tương phản màu chữ/nền tối thiểu 4.5:1 theo WCAG 2.2 SC 1.4.3).

**Kept:** Giữ nguyên 9/11 mục (`CL-01`..`CL-08`, `CL-11`) cùng 2 giả định `GA1` (thuật ngữ quốc tế được phép giữ nguyên) và `GA2` (dải màu xanh dương cho nút tích cực, đỏ cho nút nguy hiểm/đăng xuất).
**Changed:**
- Sinh viên xác nhận nền tảng `P3` là `Safari trên iPhone (iOS)` thay vì Safari chung chung; bổ sung giả định `NA1` cho thiết bị di động màn hình cố định.
- Điều chỉnh `CL-09` (`nguon: "Both"`): bỏ giới hạn chỉ kiểm trên `1440px` để kiểm tra căn lề dọc khung form trên cả khung nhìn thực tế của `P3` (iPhone).
- Điều chỉnh `CL-10` (`nguon: "Both"`): chỉ áp dụng kiểm thử chuyển đổi 3 mốc viewport `375px / 768px / 1440px` trên `P1, P2` và đánh dấu `P3` là `N/A` theo `NA1` (vì iPhone thật có khung nhìn cố định).
- Sửa định dạng bọc thẻ HTML bằng backticks trong `CL-03`..`CL-06` và cập nhật `render_checklist.py` để không bị vỡ cỡ chữ khi xem bảng Markdown.
**Rejected:** Không loại bỏ mục nào trong 11 mục `IA-01`.
**By hand:** Sinh viên kiểm tra bảng `checklist/M1_GUI_Checklist.md`, phát hiện lỗi hiển thị thẻ HTML trần làm vỡ font trong bảng Markdown, duyệt từng câu hỏi xác nhận `GA1`, `GA2`, mức ưu tiên và chốt môi trường thực thi `P3` là Safari trên iPhone.


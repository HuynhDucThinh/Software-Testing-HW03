# 2026-11-11 - Task 1 Bước 1 (Lượt 4/4): AI nháp checklist cho IA-04 (Feedback and State)

**Tool:** Antigravity
**Date and time:** 2026-11-11 15:08 +07:00
**Task / Step:** Task 1, Bước 1, Lượt IA-04 (Feedback and State)
**Prompt:**
Đồng ý và thực hiện lượt cuối cùng

**AI output:**
Đã chốt phần review của sinh viên cho lượt `IA-03` vào `ai_log/04_step1_ia03_navigation.md` và sinh tiếp 8 mục checklist nháp cuối cùng (`CL-32` .. `CL-39`) cho nhóm `IA-04` trong `checklist/checklist.json` (kèm 2 giả định `GA4`, `GA5`), hoàn tất trọn bộ nháp AI Bước 1 gồm 39 mục phủ đủ `IA-01`..`IA-04`, xuất `checklist/M1_GUI_Checklist.md`, đóng băng bằng `freeze.py --step 1` và kiểm chuẩn bằng `check_checklist.py`:
- Nguồn SRS (5 mục): `CL-32` (thông báo tiếng Việt thân thiện khi trùng Email đăng ký, không lộ lỗi SQLite thô - FR-01:33, FR-21:244), `CL-33` (khóa tạm 30 giây kèm thông báo sau đúng 3 lần đăng nhập sai liên tiếp - FR-02:41-42), `CL-34` (không lộ nguyên nhân chi tiết khi sai Email so với sai Mật khẩu - FR-02:42), `CL-36` (đồng bộ tên trên Header và giữ dữ liệu sau khi cập nhật Profile - FR-04:64), `CL-38` (vô hiệu hóa OTP sau khi dùng và báo lỗi khi nhập sai/dùng lại OTP cũ - FR-03:60, SEC-07:284).
- Nguồn Control (2 mục): `CL-35` (hiển thị phản hồi nội trang/toast nhất quán thay vì `window.alert()` trên ForgotPassword & Profile - Slide 10 #15, #16, giả định `GA4`), `CL-37` (chỉ báo loading và khóa nút Submit chống bấm đúp khi chờ API trên P1, P2; N/A trên P3 theo `NA1` - Slide 10 #13, giả định `GA5`).
- Nguồn Heuristic (1 mục): `CL-39` (giữ nguyên dữ liệu đã gõ khi gửi form báo lỗi và xóa lỗi cũ khi gửi lại thành công - Nielsen #5, #9).

**Kept:** Giữ nguyên toàn bộ 8 mục `CL-32`..`CL-39`, hai giả định `GA4` (không dùng `window.alert()` thay cho thông báo nội trang/toast nhất quán) và `GA5` (thời gian phản hồi 0,1-1 giây và đồng bộ ngay trạng thái tên trên Header), cùng cấu hình `P3 = N/A` theo `NA1` cho `CL-37`.
**Changed:** Không chỉnh sửa câu chữ hay mức ưu tiên sau khi sinh viên kiểm tra bảng `IA-04`.
**Rejected:** Không loại bỏ mục nào trong 8 mục `IA-04`.
**By hand:** Sinh viên kiểm tra bảng `IA-04` trên `checklist/M1_GUI_Checklist.md`, xác nhận `GA4`, `GA5`, cấu hình `P3 = N/A` của `CL-37` và chốt toàn bộ 39 mục nháp Bước 1 để chuyển sang Bước 2.


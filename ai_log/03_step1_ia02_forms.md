# 2026-11-11 - Task 1 Bước 1 (Lượt 2/4): AI nháp checklist cho IA-02 (Forms and Validation)

**Tool:** Antigravity
**Date and time:** 2026-11-11 14:39 +07:00
**Task / Step:** Task 1, Bước 1, Lượt IA-02 (Forms and Validation)
**Prompt:**
Tôi đồng ý toàn bộ nội dung bạn nói, tui dùng safari trên iPhone. Bạn hoàn thiện nội dung verify human và chuyển sang IA-02 nhé

**AI output:**
Đã chốt phần review của sinh viên cho lượt `IA-01` (cập nhật `P3 = Safari trên iPhone (iOS)`, thêm `NA1`, cập nhật `CL-09` và `CL-10` sang `nguon: "Both"`) và sinh tiếp 12 mục checklist nháp (`CL-12` .. `CL-23`) cho nhóm `IA-02` trong `checklist/checklist.json` (kèm giả định `GA3`), xuất lại `checklist/M1_GUI_Checklist.md` và đóng băng bản nháp lượt `IA-02` vào `checklist/ai-outputs/`:
- Nguồn SRS (10 mục): `CL-12` (dấu `*` trường bắt buộc - FR-22:252), `CL-13` & `CL-14` (`type="email"` và kiểm định dạng email - FR-01:33, FR-02:44, FR-22:253), `CL-15` (`type="password"` che ký tự mật khẩu - FR-22:254), `CL-16` (trường Xác nhận mật khẩu trên Register - FR-01:35), `CL-17` (Step Indicator trên ForgotPassword 2 bước - FR-03:52, FR-22:256), `CL-18` (trường Xác nhận mật khẩu mới ở Bước 2 ForgotPassword - FR-03:57-59), `CL-19` (quy tắc mật khẩu mạnh - FR-01:34, FR-03:58), `CL-20` (mã OTP 6 chữ số - FR-03:51, SEC-07:284), `CL-22` (định dạng SĐT bắt đầu bằng `0`, 10-11 số - FR-04:65).
- Nguồn Control (1 mục): `CL-21` (trạng thái `disabled` và nền xám phân biệt của ô Email trên Profile - FR-04:66 & Slide 10 #6).
- Nguồn Heuristic (1 mục): `CL-23` (gắn kết `<label for>` với ô nhập và gợi ý hướng dẫn - WCAG 2.2 SC 1.3.1, SC 3.3.2 & Slide 10 #7).

**Kept:** Giữ nguyên toàn bộ 12 mục `CL-12`..`CL-23`, giả định `GA3` (chỉ báo bước cho form 2 bước) và bộ dữ liệu kiểm thử mẫu (`du_lieu`) cho `CL-13` (Email), `CL-19` (Mật khẩu mạnh), `CL-22` (Số điện thoại).
**Changed:** Không chỉnh sửa câu chữ hay mức ưu tiên sau khi sinh viên đối chiếu với yêu cầu trong `eshop-sut/README.md`.
**Rejected:** Không loại bỏ mục nào trong 12 mục `IA-02`.
**By hand:** Sinh viên kiểm tra bảng `IA-02` trên `checklist/M1_GUI_Checklist.md`, xác nhận giả định `GA3`, cách tách mục màn hình chính/phụ và bộ giá trị kiểm thử mẫu trước khi yêu cầu chạy lượt `IA-03`.


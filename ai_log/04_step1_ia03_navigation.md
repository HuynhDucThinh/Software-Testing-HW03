# 2026-11-11 - Task 1 Bước 1 (Lượt 3/4): AI nháp checklist cho IA-03 (Navigation)

**Tool:** Antigravity
**Date and time:** 2026-11-11 15:01 +07:00
**Task / Step:** Task 1, Bước 1, Lượt IA-03 (Navigation)
**Prompt:**
Oke tôi xác nhận yêu cầu, bạn cứ làm theo nội dung yêu cầu trong README.md nhé. Lượt 3 bắt đầu

**AI output:**
Đã chốt phần review của sinh viên cho lượt `IA-02` vào `ai_log/03_step1_ia02_forms.md` và sinh tiếp 8 mục checklist nháp (`CL-24` .. `CL-31`) cho nhóm `IA-03` trong `checklist/checklist.json`, xuất lại `checklist/M1_GUI_Checklist.md` và đóng băng bản nháp lượt `IA-03` vào `checklist/ai-outputs/`:
- Nguồn SRS (4 mục): `CL-24` (Navbar highlight trang đang mở - FR-23:260), `CL-25` (nhãn chuẩn 'Đăng xuất' và thoát phiên trên Header - FR-23:262), `CL-26` (nút 'Quay lại đăng nhập' ở Bước 1 ForgotPassword - FR-03:53), `CL-27` (liên kết sang Login và tự chuyển hướng sau khi đăng ký thành công - FR-01:36).
- Nguồn Control (2 mục): `CL-28` (điều hướng SPA không reload toàn trang cho các link trên Login & Header - Slide 31 Link Checker), `CL-31` (hiệu ứng hover chuột trên nút/link và phím Enter gửi form mặc định trên P1, P2; N/A trên P3 theo NA1 - Slide 10 #10, #12).
- Nguồn Heuristic (2 mục): `CL-29` (nút 'Quay lại' từ Bước 2 về Bước 1 trên ForgotPassword - Nielsen #3), `CL-30` (điều hướng khi khách chưa đăng nhập truy cập thẳng `/profile` - FR-04:64 & Nielsen #3).

**Kept:** Giữ nguyên toàn bộ 8 mục `CL-24`..`CL-31`, bao gồm cấu hình `P3 = N/A` theo `NA1` cho `CL-31` (hover chuột & phím Enter vật lý) và phân bổ mức ưu tiên `Mandatory`/`Optional`.
**Changed:** Không chỉnh sửa câu chữ hay mức ưu tiên sau khi sinh viên kiểm tra bảng `IA-03`.
**Rejected:** Không loại bỏ mục nào trong 8 mục `IA-03`.
**By hand:** Sinh viên rà soát 8 mục `CL-24`..`CL-31` trên `checklist/M1_GUI_Checklist.md`, xác nhận xử lý `N/A` trên iPhone Safari và mức ưu tiên trước khi yêu cầu chạy lượt cuối `IA-04`.


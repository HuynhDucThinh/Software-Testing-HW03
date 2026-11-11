# 2026-11-11 - Task 1 Bước 0: Khảo sát control và cơ sở đặc tả phạm vi M1

**Tool:** Antigravity
**Date and time:** 2026-11-11 13:50 +07:00
**Task / Step:** Task 1, Bước 0 (Khảo sát phạm vi M1)
**Prompt:**
Thực hiện Bước 0 của skill gui-checklist-testing cho phạm vi M1 (Sinh viên: Huỳnh Đức Thịnh, MSSV: 23120199, Email: 23120199@student.hcmus.edu.vn): đọc đặc tả eshop-sut/README.md và mã nguồn giao diện M1 trong eshop-sut/frontend-web/src để tạo checklist/m1_inventory.md, checklist/m1_test_basis.md và khởi tạo khung rỗng checklist/checklist.json (step 0).

**AI output:**
Đã sinh 3 file khảo sát nền tảng tại bước 0:
- checklist/m1_inventory.md (danh mục 5 vùng giao diện M1: Register, Login, ForgotPassword 2 bước, Profile khối hồ sơ cá nhân, Header/Navbar kèm thẻ HTML, thuộc tính, thông báo và vị trí dòng mã nguồn).
- checklist/m1_test_basis.md (trích nguyên văn điều khoản FR-01..04, FR-05:81, FR-21..24, SEC-04, SEC-07 kèm số dòng trong eshop-sut/README.md và bảng phân định ranh giới phạm vi M1).
- checklist/checklist.json (khởi tạo meta cho M1 của SV Huỳnh Đức Thịnh - 23120199, 3 nền tảng P1..P3, assumptions rỗng, items rỗng, step = 0).

**Kept:** Giữ nguyên cấu trúc danh mục 5 vùng giao diện M1 trong `checklist/m1_inventory.md` và toàn bộ trích dẫn điều khoản SRS kèm số dòng trong `checklist/m1_test_basis.md` (tạm giữ ranh giới chuẩn M1/M3 trên trang `/profile`, sẽ nhắc kiểm tra lại nếu nhóm điều chỉnh).
**Changed:**
- Chốt nền tảng `P3` trong `checklist/checklist.json` thành `Safari (macOS/iOS hoặc qua BrowserStack / LambdaTest)` (bản gốc AI trước khi sửa đã đóng băng tại `checklist/ai-outputs/M1_checklist_step0_20261111-135503.json`).
- Bổ sung xác nhận thực tế vào `checklist/m1_inventory.md` cho cả 5 màn hình, bao gồm ghi nhận hành vi trình duyệt tự động điền nhầm (autofill) email/mật khẩu đã lưu vào ô `Mã OTP (4 số)` và `Mật khẩu mới` ở Bước 2 trang `/forgot-password` do thiếu thuộc tính định danh `name`/`autoComplete`.
**Rejected:** Không sử dụng hành vi hiện tại trong mã nguồn làm Expected (tuân thủ Quy tắc 2: chỉ lấy đặc tả và heuristic làm oracle).
**By hand:** Sinh viên tự xử lý lỗi đường dẫn chứa ký tự `&` khi cài đặt `sqlite3`, khởi chạy Backend (`localhost:3000`) và Frontend Web (`localhost:5173`), trực tiếp mở kiểm chứng cả 5 màn hình (`/register`, `/login`, `/forgot-password` Bước 1 & Bước 2, `/profile`, `Header`) và chụp đối chiếu thực tế.


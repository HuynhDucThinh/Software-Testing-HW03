# 2026-11-11 - Task 1 Bước 6: Gom nhóm dữ kiện lỗi (45 mục Failed -> 27 Bugs) và đồng bộ GitHub Issues

**Tool:** Antigravity
**Date and time:** 2026-11-11 17:45 +07:00
**Task / Step:** Task 1, Bước 6 (Trích xuất danh sách `Failed`, gom nhóm chống trùng lặp `bugs/bug_groups.md`, lập `bugs/BUG-01.md`..`BUG-27.md`, đăng GitHub Issues `#1`..`#27` và tổng hợp `Bug_Report.md`)
**Prompt:**
Bước 6. Dùng github của tôi có sẵn để đăng issue luôn nhe

**AI output:**
Đã thực hiện quy trình Bước 6 từ nguồn dữ liệu `checklist/checklist.json`:
- Chạy `bug_skeleton.py checklist/checklist.json --list-only` trích xuất toàn bộ `130` ô `Failed` trên 3 nền tảng (`P1`: 44, `P2`: 44, `P3`: 42) tương ứng `45 / 59` mục kiểm tra độc lập bị `Failed`.
- Gom nhóm các mục `Failed` có cùng nguyên nhân gốc hoặc cùng hiện tượng trên thành phần giao diện thành **27 báo cáo lỗi không trùng lặp (`BUG-01` .. `BUG-27`)**, đảm bảo ánh xạ song ánh 100% cả 45 mục `Failed` (`5 Critical`, `10 Major`, `11 Minor`, `1 Cosmetic`) trong `bugs/bug_groups.md` và `bugs/BUG-01.md`..`BUG-27.md`.
- Tạo nhãn phân loại (`severity: critical/major/minor/cosmetic`, `IA-01..IA-04`, `M1`) và đăng trực tiếp **27 GitHub Issues (`#1` .. `#27`)** kèm ảnh chụp minh chứng hiển thị nội dòng lên repository `https://github.com/HuynhDucThinh/Software-Testing-HW03/issues`.
- Lưu bộ ảnh chụp trang tổng quan và từng trang chi tiết GitHub Issue vào `screenshots/github_issues/` (`GitHub_Issues_Overview_Page1.png`, `GitHub_Issues_Overview_Page2.png`, `ISSUE-01_BUG-01.png` .. `ISSUE-27_BUG-27.png`), xuất `Bug_Report.md` ở thư mục gốc và kết xuất đầy đủ các bảng dữ liệu chi tiết sang tài liệu trung tâm `Main_Report.md` (Mục 1..4, Mục 6, Mục 8), `README.md` (Mục 3) và `checklist/checklist.json` (`step: 6`, `version: v6`).

**Kept:** Giữ nguyên cấu trúc gom 27 nhóm lỗi (`G-01`..`G-27` -> `BUG-01`..`BUG-27`), toàn bộ 27 GitHub Issues `#1`..`#27`, file `Bug_Report.md` và bảng tổng hợp trong `Main_Report.md`, `README.md`.
**Changed:** Tách riêng nhóm lỗi màu sắc ngữ nghĩa nút bấm (`BUG-19`: `CL-07, CL-08`) khỏi lỗi độ tương phản văn bản (`BUG-20`: `CL-11`), và tách lỗi thiếu dấu sao/liên kết `<label>` (`BUG-23`: `CL-12, CL-23`) khỏi lỗi thiếu `autocomplete`/`type="tel"` (`BUG-24`: `SV-12, SV-20`) để mỗi GitHub Issue có một nguyên nhân kỹ thuật rõ ràng, dễ khắc phục.
**Rejected:** Loại bỏ phương án tạo rời rạc 45 GitHub Issues theo từng mục đơn lẻ vì sẽ gây trùng lặp báo cáo lỗi (ví dụ 3 mục `CL-19`, `SV-08`, `SV-09` đều bắt cùng một biểu thức chính quy mật khẩu sai trong `Register.jsx:15`).
**By hand:** Sinh viên kiểm tra đối chiếu các GitHub Issues `#1`..`#27` trên tài khoản `HuynhDucThinh/Software-Testing-HW03` (mở chế độ Public trước thời điểm nộp bài chấm điểm để trợ giảng truy cập trực tiếp liên kết).


# 2026-11-11 - Task 1 Bước 3: Chuẩn bị hướng dẫn thực thi RUN.md, dom_probe.js và khung ghi kết quả

**Tool:** Antigravity
**Date and time:** 2026-11-11 15:35 +07:00
**Task / Step:** Task 1, Bước 3 (Chuẩn bị `RUN.md`, `dom_probe.js`, phân loại `che_do` và khung CSV lượt chạy)
**Prompt:**
Thực hiện bước 3. Bạn quét thử xem cần thông tin gì từ tôi thì đề xuất tôi cung cấp

**AI output:**
Đã hoàn thành Bước 3 chuẩn bị thực thi cho toàn bộ 59 mục checklist M1 mà không thay đổi bất kỳ nội dung `expected` nào:
- Chép `checklist/dom_probe.js` từ `.agents/skills/gui-checklist-testing/assets/dom_probe.js` (script chỉ đọc DOM, xuất JSON thông số tiêu đề `h1`, thuộc tính `input`, màu và độ tương phản nút, thứ tự `Tab`, vị trí khối lỗi, tràn ngang để sinh viên tự đối chiếu).
- Cập nhật `checklist/checklist.json` (`step: 3`): gán `che_do: "manual"` kèm `che_do_ghi_chu` cụ thể cho từng mục trong 59 mục, xuất lại `checklist/M1_GUI_Checklist.md`, đóng băng bằng `freeze.py --step 3` và kiểm chuẩn `check_checklist.py --min 41 --min-per-ia 8` (`0 lỗi, 0 cảnh báo`).
- Soạn `checklist/RUN.md` gồm: lệnh khởi động và reset SQLite qua đường dẫn `D:\KCPM\GUI_Usability_Testing`, lưu ý kỹ thuật kết nối `localhost:5173` và `localhost:3000` qua BrowserStack/LambdaTest Local Tunnel cho `P3` (`Safari trên iPhone`), quy tắc chống gian lận ảnh chụp (overlay `23120199@student.hcmus.edu.vn`, điền `23120199 - Huỳnh Đức Thịnh` vào form, hiện rõ trình duyệt/OS và URL `localhost`), gom 59 mục vào 7 nhóm tiền điều kiện (`G1`..`G7`) đẩy các mục đổi tên cực trị (`SV-06`, `SV-05`) và khóa tài khoản (`CL-33`) xuống cuối lượt, bảng ánh xạ dữ liệu `dom_probe.js` và quy trình gộp CSV.
- Tạo sẵn khung `checklist/runs/P1_template.csv`, `P2_template.csv`, `P3_template.csv` (điền sẵn `N/A` cho các mục không áp dụng theo thiết kế) và các thư mục đích trong `screenshots/`.
- Đồng thời rà soát mã nguồn SUT và đề xuất 5 nhóm thông tin cần sinh viên xác nhận trước khi bước vào Bước 4 (phương thức chạy `P3` để giữ URL `localhost` và gọi được cổng `3000`, phiên bản cụ thể của `P1`/`P2`/`P3`, công cụ chèn watermark email, ranh giới nhóm ở `/profile` + repo đăng GitHub Issues, và cách phối hợp điền CSV).

**Kept:** Giữ nguyên `checklist/RUN.md`, `checklist/dom_probe.js`, phân loại `che_do` trong `checklist/checklist.json` và 3 file khung CSV trong `checklist/runs/` để rà soát thông tin môi trường trước khi chạy Bước 4.
**Changed:** Chờ sinh viên cung cấp phiên bản trình duyệt/OS/thiết bị thực tế và xác nhận phương thức tunnel cho `P3` để điền hoàn chỉnh mục 1.3 của `checklist/RUN.md` trước lượt chạy đầu tiên.
**Rejected:** Không loại bỏ mục nào.
**By hand:** Sinh viên rà soát quy trình trong `checklist/RUN.md`, chuẩn bị công cụ chụp ảnh kèm overlay email cá nhân và cung cấp thông số phiên bản môi trường thực tế của 3 nền tảng trước khi thực thi Bước 4.

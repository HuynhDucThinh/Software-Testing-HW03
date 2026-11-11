# Nhật Ký Tương Tác AI (Append-Only AI Log) — HW03-AI

- **Sinh viên:** Huỳnh Đức Thịnh — MSSV: `23120199` (`23120199@student.hcmus.edu.vn`)
- **Quy ước ghi nhật ký:** Toàn bộ các lượt tương tác với AI được gom chung trong file duy nhất này theo trình tự thời gian; mỗi lượt tương tác mới được nối tiếp (`append`) vào cuối file dưới dạng một mục `## Entry NN — ...` đầy đủ các trường chuẩn để `ai_audit_export.py` trích xuất tự động.

---

## Entry 01 — 2026-11-11 - Task 1 Bước 0: Khảo sát control và cơ sở đặc tả phạm vi M1

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

---

## Entry 02 — 2026-11-11 - Task 1 Bước 1 (Lượt 1/4): AI nháp checklist cho IA-01 (General UI Standards)

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

---

## Entry 03 — 2026-11-11 - Task 1 Bước 1 (Lượt 2/4): AI nháp checklist cho IA-02 (Forms and Validation)

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

---

## Entry 04 — 2026-11-11 - Task 1 Bước 1 (Lượt 3/4): AI nháp checklist cho IA-03 (Navigation)

**Tool:** Antigravity
**Date and time:** 2026-11-11 15:01 +07:00
**Task / Step:** Task 1, Bước 1, Lượt IA-03 (Navigation)
**Prompt:**
Oke tôi xác nhận yêu cầu, bạn cứ làm theo nội dung yêu cầu trong README.md nhé. Lượt 3 bắt đầu

**AI output:**
Đã chốt phần review của sinh viên cho lượt `IA-02` vào `ai_log/AI_Log.md` (`Entry 03`) và sinh tiếp 8 mục checklist nháp (`CL-24` .. `CL-31`) cho nhóm `IA-03` trong `checklist/checklist.json`, xuất lại `checklist/M1_GUI_Checklist.md` và đóng băng bản nháp lượt `IA-03` vào `checklist/ai-outputs/`:
- Nguồn SRS (4 mục): `CL-24` (Navbar highlight trang đang mở - FR-23:260), `CL-25` (nhãn chuẩn 'Đăng xuất' và thoát phiên trên Header - FR-23:262), `CL-26` (nút 'Quay lại đăng nhập' ở Bước 1 ForgotPassword - FR-03:53), `CL-27` (liên kết sang Login và tự chuyển hướng sau khi đăng ký thành công - FR-01:36).
- Nguồn Control (2 mục): `CL-28` (điều hướng SPA không reload toàn trang cho các link trên Login & Header - Slide 31 Link Checker), `CL-31` (hiệu ứng hover chuột trên nút/link và phím Enter gửi form mặc định trên P1, P2; N/A trên P3 theo NA1 - Slide 10 #10, #12).
- Nguồn Heuristic (2 mục): `CL-29` (nút 'Quay lại' từ Bước 2 về Bước 1 trên ForgotPassword - Nielsen #3), `CL-30` (điều hướng khi khách chưa đăng nhập truy cập thẳng `/profile` - FR-04:64 & Nielsen #3).

**Kept:** Giữ nguyên toàn bộ 8 mục `CL-24`..`CL-31`, bao gồm cấu hình `P3 = N/A` theo `NA1` cho `CL-31` (hover chuột & phím Enter vật lý) và phân bổ mức ưu tiên `Mandatory`/`Optional`.
**Changed:** Không chỉnh sửa câu chữ hay mức ưu tiên sau khi sinh viên kiểm tra bảng `IA-03`.
**Rejected:** Không loại bỏ mục nào trong 8 mục `IA-03`.
**By hand:** Sinh viên rà soát 8 mục `CL-24`..`CL-31` trên `checklist/M1_GUI_Checklist.md`, xác nhận xử lý `N/A` trên iPhone Safari và mức ưu tiên trước khi yêu cầu chạy lượt cuối `IA-04`.

---

## Entry 05 — 2026-11-11 - Task 1 Bước 1 (Lượt 4/4): AI nháp checklist cho IA-04 (Feedback and State)

**Tool:** Antigravity
**Date and time:** 2026-11-11 15:08 +07:00
**Task / Step:** Task 1, Bước 1, Lượt IA-04 (Feedback and State)
**Prompt:**
Đồng ý và thực hiện lượt cuối cùng

**AI output:**
Đã chốt phần review của sinh viên cho lượt `IA-03` vào `ai_log/AI_Log.md` (`Entry 04`) và sinh tiếp 8 mục checklist nháp cuối cùng (`CL-32` .. `CL-39`) cho nhóm `IA-04` trong `checklist/checklist.json` (kèm 2 giả định `GA4`, `GA5`), hoàn tất trọn bộ nháp AI Bước 1 gồm 39 mục phủ đủ `IA-01`..`IA-04`, xuất `checklist/M1_GUI_Checklist.md`, đóng băng bằng `freeze.py --step 1` và kiểm chuẩn bằng `check_checklist.py`:
- Nguồn SRS (5 mục): `CL-32` (thông báo tiếng Việt thân thiện khi trùng Email đăng ký, không lộ lỗi SQLite thô - FR-01:33, FR-21:244), `CL-33` (khóa tạm 30 giây kèm thông báo sau đúng 3 lần đăng nhập sai liên tiếp - FR-02:41-42), `CL-34` (không lộ nguyên nhân chi tiết khi sai Email so với sai Mật khẩu - FR-02:42), `CL-36` (đồng bộ tên trên Header và giữ dữ liệu sau khi cập nhật Profile - FR-04:64), `CL-38` (vô hiệu hóa OTP sau khi dùng và báo lỗi khi nhập sai/dùng lại OTP cũ - FR-03:60, SEC-07:284).
- Nguồn Control (2 mục): `CL-35` (hiển thị phản hồi nội trang/toast nhất quán thay vì `window.alert()` trên ForgotPassword & Profile - Slide 10 #15, #16, giả định `GA4`), `CL-37` (chỉ báo loading và khóa nút Submit chống bấm đúp khi chờ API trên P1, P2; N/A trên P3 theo `NA1` - Slide 10 #13, giả định `GA5`).
- Nguồn Heuristic (1 mục): `CL-39` (giữ nguyên dữ liệu đã gõ khi gửi form báo lỗi và xóa lỗi cũ khi gửi lại thành công - Nielsen #5, #9).

**Kept:** Giữ nguyên toàn bộ 8 mục `CL-32`..`CL-39`, hai giả định `GA4` (không dùng `window.alert()` thay cho thông báo nội trang/toast nhất quán) và `GA5` (thời gian phản hồi 0,1-1 giây và đồng bộ ngay trạng thái tên trên Header), cùng cấu hình `P3 = N/A` theo `NA1` cho `CL-37`.
**Changed:** Không chỉnh sửa câu chữ hay mức ưu tiên sau khi sinh viên kiểm tra bảng `IA-04`.
**Rejected:** Không loại bỏ mục nào trong 8 mục `IA-04`.
**By hand:** Sinh viên kiểm tra bảng `IA-04` trên `checklist/M1_GUI_Checklist.md`, xác nhận `GA4`, `GA5`, cấu hình `P3 = N/A` của `CL-37` và chốt toàn bộ 39 mục nháp Bước 1 để chuyển sang Bước 2.

---

## Entry 06 — 2026-11-11 - Task 1 Bước 2: Kiểm cấu trúc, gộp mục bổ sung của sinh viên và xuất ma trận độ phủ

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

---

## Entry 07 — 2026-11-11 - Task 1 Bước 3: Chuẩn bị hướng dẫn thực thi RUN.md, dom_probe.js và khung ghi kết quả

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
**Changed:** Sau khi rà soát giới hạn kết nối `localhost:3000` trên iPhone vật lý và thời lượng phiên dùng thử Cloud ngắn, sinh viên quyết định chuyển `P3` sang thiết bị thật `Chrome Android 156.0.8078.79 trên OPPO Reno10 5G (Android 15, adb reverse)` (hợp lệ theo Mục 6 của đề bài), cài đặt bổ sung `Mozilla Firefox 137.0.1` cho `P2`, cập nhật đồng bộ thông số phiên bản thực tế của cả 3 nền tảng (`P1`, `P2`, `P3`) vào `checklist/checklist.json`, `checklist/sv_items.md`, `checklist/M1_GUI_Checklist.md`, `checklist/RUN.md` và đóng băng lại bản `--step 3b` trước khi bắt đầu Bước 4.
**Rejected:** Loại bỏ phương án dùng Safari trên iPhone rời / Cloud Trial và không dùng Microsoft Edge thay cho Firefox (do trùng nhân Chromium với Chrome).
**By hand:** Sinh viên kết nối cáp USB điện thoại `OPPO Reno10 5G`, bật chế độ nhà phát triển và cấp quyền khóa RSA cho `adb`, đồng ý cài đặt Firefox `137.0.1` và chốt cấu hình 3 nền tảng thực thi trước khi bước sang Bước 4.

---

## Entry 08 — 2026-11-11 - Task 1 Bước 5: Xuất sổ làm việc Excel 3 sheet và tổng hợp Test Summary Report

**Tool:** Antigravity
**Date and time:** 2026-11-11 17:20 +07:00
**Task / Step:** Task 1, Bước 5 (Xuất `checklist/M1_GUI_Checklist_And_Summary.xlsx`, cập nhật `M1_GUI_Checklist.md`, `README.md` và `Main_Report.md`)
**Prompt:**
Tiếp tục thực hiện bước 5 giúp tôi nhé.

**AI output:**
Đã hoàn thành Bước 5 của quy trình GUI Checklist cho phạm vi M1:
- Cập nhật `checklist/checklist.json` (`step: 5`, phiên bản `v5`) và chạy `build_excel.py` sinh sổ làm việc `checklist/M1_GUI_Checklist_And_Summary.xlsx` gồm đủ 3 sheet chuẩn:
  1. `Test Cases`: 59 dòng kiểm thử kèm đầy đủ `TC ID`, `Objective`, `IA`, `Màn hình`, `Precondition`, `Căn cứ`, `Expected`, kết quả và `Notes` thực tế trên `P1`/`P2`/`P3`, `Ưu tiên`, `Nguồn`, `Loại lỗi` và cột giải thích `Vì sao AI bỏ sót` cho toàn bộ 20 mục `SV`.
  2. `Checklist`: bảng thực thi rút gọn có Data Validation dropdown (`Passed,Failed,N/A,Blocked`) trên cả 3 cột `P1`, `P2`, `P3`.
  3. `Test Summary Report`: bảng tổng hợp dùng công thức động (`ROWS`, `COUNTA-COUNTIF`, `COUNTIF`, `COUNTBLANK` với `fullCalcOnLoad=True`) đối chiếu trực tiếp sang vùng `Checklist!G5:I63`, kèm thống kê theo `IA-01..IA-04`, loại căn cứ (`SRS`, `Control`, `Heuristic`) và nguồn thiết kế (`AI`, `Both`, `SV`).
- Chạy lại `render_checklist.py` đồng bộ `checklist/M1_GUI_Checklist.md` và kiểm tra bằng `coverage_matrix.py` + `check_checklist.py --min 41 --min-per-ia 8` (`0 lỗi, 0 cảnh báo`).
- Tổng hợp đầy đủ các bảng số liệu Test Summary (`59` mục thiết kế; `168/177` lượt thực thi trên 3 nền tảng; `38 Passed / 130 Failed / 9 N/A / 0 Blocked`, trong đó `P1`: `14P/44F/1NA`, `P2`: `14P/44F/1NA`, `P3`: `10P/42F/7NA`; `45/59` mục độc lập phát hiện lỗi và `15/20` mục do SV bổ sung bắt được lỗi thật) sang `README.md` và khởi tạo báo cáo chính `Main_Report.md` (hoàn chỉnh phần Task 1 & Task 3).

**Kept:** Giữ nguyên file `checklist/M1_GUI_Checklist_And_Summary.xlsx`, `checklist/M1_GUI_Checklist.md`, các bảng thống kê trong `README.md` và nội dung phần Task 1, Task 3 trong `Main_Report.md`.
**Changed:** Chưa cần chỉnh sửa; các mục chờ số liệu của Bước 6 (số lượng GitHub Issues) và Task 2 (7 phiên Usability & SUS) đã được đánh dấu rõ để điền tiếp ở các bước kế tiếp.
**Rejected:** Không có.
**By hand:** Sinh viên kiểm tra đối chiếu số liệu thống kê giữa file Excel, `README.md` và `Main_Report.md` trước khi chuyển sang Bước 6 (gom dữ kiện bug và tạo GitHub Issues).

---

## Entry 09 — 2026-11-11 - Task 1 Bước 6: Gom nhóm dữ kiện lỗi (45 mục Failed -> 27 Bugs) và đồng bộ GitHub Issues

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

---

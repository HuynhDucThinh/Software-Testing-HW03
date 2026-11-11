# RUN - Hướng dẫn thực thi Checklist GUI phạm vi M1

Bước 3 của skill `gui-checklist-testing`. Tài liệu này quy định quy trình khởi chạy SUT, thứ tự thực thi 59 mục checklist (`CL-01`..`CL-39` và `SV-01`..`SV-20`) trên 3 nền tảng, quy tắc chụp ảnh chống gian lận, cách thu thập dữ kiện bằng `dom_probe.js` và cách gộp kết quả vào `checklist.json`.

> **Nguyên tắc đóng băng:** Kiểm tra và chốt thông tin môi trường trong file này **trước** khi bắt đầu chạy chính thức ở Bước 4. Nếu thay đổi quy trình chạy, cần chạy lại `freeze.py`; tuyệt đối không sửa nội dung `expected` sau khi đã xem kết quả thực tế (`Actual`).

---

## 1. Chuẩn bị môi trường (trước mỗi nền tảng)

### 1.1. Khởi động và đặt lại SUT về trạng thái gốc (Seed)
Do đường dẫn gốc có ký tự `&`, luôn chạy lệnh qua thư mục liên kết `D:\KCPM\GUI_Usability_Testing`:

- **Cửa sổ Terminal 1 - Backend (cổng `3000`, reset CSDL SQLite trước mỗi nền tảng):**
  ```powershell
  cd D:\KCPM\GUI_Usability_Testing\eshop-sut\backend
  node database.js
  node server.js
  ```
  *(Lưu ý: Nếu `node server.js` đang chạy từ nền tảng trước, nhấn `Ctrl + C` dừng server rồi chạy lại `node database.js` và `node server.js` để đưa tài khoản, mật khẩu và bộ đếm khóa đăng nhập về trạng thái ban đầu).*

- **Cửa sổ Terminal 2 - Web Frontend (cổng `5173`):**
  ```powershell
  cd D:\KCPM\GUI_Usability_Testing\eshop-sut\frontend-web
  npm run dev
  ```
  - Địa chỉ kiểm thử bắt buộc: `http://localhost:5173`

### 1.2. Tài khoản và dữ liệu kiểm thử chuẩn
- **Tài khoản khách mặc định (seed):** `test@eshop.com` / `Test1234!`
- **Tài khoản đăng ký mới trong lượt chạy:** dùng định dạng `m1+<nhãn>@example.com` (ví dụ `m1+ok@example.com`, `m1+1@example.com` .. `m1+7@example.com`) để không đụng tài khoản seed.
- **Chuỗi nhận diện sinh viên trên form:**
  - Họ Tên nhận diện: `23120199 - Huỳnh Đức Thịnh`
  - Email sinh viên (dùng làm lớp phủ overlay trên mọi ảnh chụp): `23120199@student.hcmus.edu.vn`

### 1.3. Cấu hình 3 nền tảng thực thi (cần điền đủ phiên bản thực tế trước khi chạy)

| Mã | Nền tảng | Trình duyệt & Phiên bản | Hệ điều hành & Thiết bị | Độ phân giải / Viewport mặc định | Cách kết nối `localhost` |
|---|---|---|---|---|---|
| `P1` | Chrome trên Windows | `Chrome <điền phiên bản>` | `Windows <10/11, bản build>` - Desktop PC | `<ví dụ 1920x1080>` | Trực tiếp `http://localhost:5173` |
| `P2` | Firefox trên Windows | `Firefox <điền phiên bản>` | `Windows <10/11, bản build>` - Desktop PC | `<ví dụ 1920x1080>` | Trực tiếp `http://localhost:5173` |
| `P3` | Safari trên iPhone (iOS) | `Mobile Safari <điền phiên bản>` | `iPhone <dòng máy> - iOS <phiên bản>` | `<đọc từ dom_probe.viewport>` | Qua **BrowserStack Local** hoặc **LambdaTest Tunnel** (xem mục 1.4) |

### 1.4. Lưu ý kỹ thuật bắt buộc cho `P3` (`Safari trên iPhone`)
- Các trang frontend của SUT gọi trực tiếp `http://localhost:3000/api/...`, đồng thời Mục 6 của đề yêu cầu ảnh chụp phải hiển thị rõ **tên trình duyệt / OS / thiết bị cùng URL `localhost`**.
- **Không mở qua IP Wi-Fi LAN (`192.168.x.x:5173`) trên iPhone rời**, vì thanh địa chỉ sẽ mất chữ `localhost` và mọi lệnh gọi `http://localhost:3000` trên iPhone sẽ lỗi kết nối (trỏ nhầm vào chính điện thoại).
- **Cách chạy chuẩn qua BrowserStack Live / LambdaTest Real-Time:**
  1. Đảm bảo Backend (`localhost:3000`) và Frontend (`localhost:5173`) đang chạy trên máy Windows.
  2. Chạy công cụ đường hầm trên máy Windows:
     - Với BrowserStack: `BrowserStackLocal.exe --key <ACCESS_KEY>` (hoặc bật ứng dụng BrowserStack Local).
     - Với LambdaTest: `LT.exe --user <EMAIL> --key <ACCESS_KEY>`.
  3. Mở phiên **Real Device -> iOS -> iPhone -> Safari**, gõ `http://localhost:5173/register`.
  4. Mở **DevTools / Web Inspector** tích hợp sẵn trên thanh công cụ BrowserStack/LambdaTest để dán `dom_probe.js` khi cần lấy thông số DOM.

---

## 2. Quy tắc ảnh chụp và Chống gian lận (Mục 6 & Mục 11 của đề)

1. **Lớp phủ (Overlay) bắt buộc trên MỌI ảnh chụp:**
   - Mọi ảnh trong `screenshots/task1_failed/` và `screenshots/task3_cross_platform/` phải có lớp phủ chữ **`23120199@student.hcmus.edu.vn`** rõ nét, không che khuất vùng lỗi cần minh chứng.
   - Sinh viên tự chèn overlay (ví dụ cấu hình Watermark tự động trong ShareX hoặc chèn chữ bằng Snipping Tool / Paint); **AI tuyệt đối không tạo, chỉnh sửa hay ghép ảnh**.
2. **Thông tin trong form trên ảnh tổng quan đa nền tảng (`Task 3`):**
   - Trước khi chụp ảnh tổng quan ở từng nền tảng (`P1`, `P2`, `P3`), nhập trực tiếp **`23120199 - Huỳnh Đức Thịnh`** vào ô nhập trên form (`Họ Tên` tại `/register` hoặc `/profile`; ô tài khoản tại `/login`) mà chưa cần bấm gửi.
3. **Khung chụp màn hình:**
   - Phải chụp thấy rõ **thanh địa chỉ chứa `localhost:5173/...`** và **dấu hiệu nhận biết trình duyệt / hệ điều hành / thiết bị** (thanh tiêu đề trình duyệt + taskbar hệ điều hành trên Desktop, hoặc thanh thông tin thiết bị iPhone/iOS của BrowserStack/LambdaTest trên `P3`).
4. **Quy ước đường dẫn và đặt tên file ảnh:**
   - **Ảnh minh chứng mục `Failed` (chỉ chụp khi kết quả là `Failed`):**
     `screenshots/task1_failed/P<n>_<ID>.png` (ví dụ: `screenshots/task1_failed/P1_CL-01.png`; nếu 1 mục cần 2 ảnh: `P1_CL-05_1.png`, `P1_CL-05_2.png`).
   - **Ảnh tổng quan đa nền tảng (`Task 3`, tối thiểu bộ ảnh cho mỗi nền tảng `P1`, `P2`, `P3`):**
     - `screenshots/task3_cross_platform/P<n>_Register_1.png`
     - `screenshots/task3_cross_platform/P<n>_Login_1.png`
     - `screenshots/task3_cross_platform/P<n>_ForgotPassword_1.png`
     - `screenshots/task3_cross_platform/P<n>_Profile_1.png`
   - Ảnh thô chưa đóng dấu (nếu có lưu tạm) đặt trong thư mục `evidence_raw/` (đã được `.gitignore` loại khỏi Git).

---

## 3. Danh sách kiểm nhanh trước khi lưu mỗi bức ảnh

- [ ] Nhìn thấy rõ tên trình duyệt / hệ điều hành / khung thiết bị (`Chrome`, `Firefox`, `iPhone Safari`).
- [ ] Thanh URL hiển thị rõ `localhost:5173/...`.
- [ ] Đã có lớp phủ (overlay) email sinh viên `23120199@student.hcmus.edu.vn`.
- [ ] Ô nhập trên form có chuỗi `23120199 - Huỳnh Đức Thịnh` (bắt buộc với mọi ảnh `task3_cross_platform`, khuyến khích giữ cả khi chụp form lỗi nếu không ảnh hưởng kịch bản test).
- [ ] Đúng thư mục và đúng tên file chuẩn `P<n>_<ID>.png` hoặc `P<n>_<Screen>_1.png`.

---

## 4. Thứ tự thực thi 59 mục theo 7 nhóm tiền điều kiện (`G1` -> `G7`)

Sắp xếp dưới đây gom toàn bộ **59 mục** theo luồng trạng thái tăng dần mức tác động dữ liệu, giúp mỗi nền tảng chỉ cần **reset backend đúng 1 lần ở đầu lượt chạy**:

| Nhóm | Tiền điều kiện & Thao tác mở đầu | Mục chốt kết quả ngay tại nhóm (59 mục) | Mục đa màn hình cần ghi nhận dữ kiện trung gian | Lưu ý điều hành & tránh bị `Blocked` dây chuyền |
|---|---|---|---|---|
| **G1** | **Khách (chưa đăng nhập)**, mở `/register`. Dán `dom_probe.js`. Nhập `23120199 - Huỳnh Đức Thịnh` chụp `P<n>_Register_1.png` trước khi test. | **9 mục:** `CL-03`, `CL-13`, `CL-16`, `SV-14`, `SV-04`, `SV-08`, `SV-09`, `CL-32`, `CL-27` | Ghi nhận phần `/register` cho: `CL-02`, `CL-07`, `CL-09`, `CL-11`, `CL-12`, `CL-15`, `CL-19`, `CL-23`, `CL-24`, `CL-31` *(P1,P2)*, `CL-39`, `SV-02` *(P1,P2)*, `SV-11`, `SV-16`, `SV-17` *(P1,P2)*, `SV-19` | Dùng email mới `m1+1@example.com`..`m1+7@example.com` khi thử mật khẩu. Nếu mật khẩu chuẩn `Abcd123!` bị form từ chối ở `CL-19`/`SV-08`, ghi nhận kết quả cho mục đó; để dựng tài khoản `m1+ok@example.com` phục vụ test gửi lên server (`CL-32`, `CL-27`), thử chuỗi mật khẩu thoả điều kiện client hiện hành hoặc đánh dấu `Blocked (bị chặn bởi CL-19)` nếu không thể gửi form. |
| **G2** | **Khách**, gõ thẳng URL `/profile` để chấm `CL-30`; sau đó mở `/login`, dán `dom_probe.js`, chụp `P<n>_Login_1.png`. | **7 mục:** `CL-30`, `CL-01`, `CL-04`, `SV-01` *(P1,P2)*, `SV-03`, `CL-34`, `CL-39` | Ghi nhận phần `/login` cho: `CL-07`, `CL-09`, `CL-11`, `CL-12`, `CL-14`, `CL-15`, `CL-23`, `CL-24`, `CL-28`, `CL-31` *(P1,P2)*, `SV-12`, `SV-16`, `SV-17` *(P1,P2)*, `SV-19` | **Quan trọng:** Khi kích hoạt lỗi cho `SV-03` và `CL-34`, ưu tiên dùng `khongtontai@eshop.com` và tài khoản phụ `m1+ok@example.com` (hoặc tối đa **1 lần** sai trên `test@eshop.com`) để **không** làm khóa sớm `test@eshop.com` trước khi sang G3-G6. |
| **G3** | **Khách** (đã lưu sẵn 1 cặp tài khoản trong trình duyệt cho `SV-12`), mở `/forgot-password` Bước 1 -> dán `dom_probe.js` -> lấy OTP vào Bước 2 -> dán lại `dom_probe.js`, chụp `P<n>_ForgotPassword_1.png`. | **13 mục:** `CL-05`, `CL-14`, `CL-15`, `CL-17`, `CL-18`, `CL-19`, `CL-20`, `CL-26`, `CL-29`, `SV-02` *(P1,P2)*, `SV-12`, `SV-13`, `CL-38` | Ghi nhận phần `/forgot-password` cho: `CL-02`, `CL-08`, `CL-09`, `CL-11`, `CL-12`, `CL-23`, `CL-31` *(P1,P2)*, `CL-35`, `SV-16`, `SV-17` *(P1,P2)*, `SV-19` | Ở `CL-38`, thực hiện đổi mật khẩu trên tài khoản phụ `m1+ok@example.com` (hoặc đặt lại `test@eshop.com` về đúng `Test1234!`) để G4 vẫn đăng nhập được bằng `test@eshop.com` / `Test1234!`. |
| **G4** | **Đã đăng nhập** (`test@eshop.com` / `Test1234!`), mở `/profile`, dán `dom_probe.js`. Nhập `23120199 - Huỳnh Đức Thịnh` chụp `P<n>_Profile_1.png`. Cuối G4 bấm nút thoát trên Header (`CL-25`). | **24 mục:** `CL-06`, `CL-21`, `SV-20` *(chỉ P3)*, `CL-22`, `SV-10`, `SV-11`, `CL-35`, `CL-36`, `SV-07`, `SV-15`, `CL-02`, `CL-07`, `CL-08`, `CL-09`, `CL-11`, `CL-12`, `CL-23`, `CL-24`, `CL-28`, `CL-31` *(P1,P2)*, `SV-16`, `SV-17` *(P1,P2)*, `SV-19`, `CL-25` | Đã đi đủ cả 5 vùng giao diện -> chốt dứt điểm toàn bộ các mục đa màn hình thông thường tại cuối G4. | Nếu SĐT bắt đầu bằng `0` (`0912345678`) bị chặn ở `CL-22`, sau khi chấm xong `CL-22` và `SV-10`, hãy nhập một chuỗi số qua được kiểm tra client (ví dụ `912345678`) khi cần bấm `Cập nhật` lưu `Họ Tên`/`Địa chỉ` cho `SV-11`, `CL-36`, `SV-07`, `SV-06`, `SV-05` để tránh bị `Blocked` dây chuyền. |
| **G5** | **Chế độ hiển thị & Mạng trên Desktop** *(chỉ chạy trên `P1, P2`; `P3 = N/A`)*. Kiểm cả trạng thái khách và đã đăng nhập. | **3 mục:** `CL-10` *(375/768/1440px)*, `SV-18` *(zoom 200% ở 1440px)*, `CL-37` *(DevTools Network Slow 3G)* | Không | Sau khi xong G5, trả trình duyệt về Zoom `100%`, tắt Device Toolbar và trả Network về `No throttling` trước khi sang G6. |
| **G6** | **Đã đăng nhập**, tại `/profile` ghi dữ liệu đặc biệt vào `Họ Tên` rồi đăng xuất & đăng nhập lại kiểm tra `Header`. | **2 mục:** `SV-06` *(chuỗi 100 ký tự liền nhau)*, `SV-05` *(`<b>Test</b><i>User</i>`)* | Không | Thực hiện `SV-06` trước, `SV-05` sau. Sau khi kiểm xong `SV-05`, có thể đổi lại `Họ Tên` bình thường hoặc giữ nguyên để sang G7. |
| **G7** | **Cuối lượt chạy:** Đảm bảo `test@eshop.com` có bộ đếm sai = 0 (đăng nhập đúng 1 lần rồi đăng xuất), mở `/login`. | **1 mục:** `CL-33` *(nhập sai mật khẩu liên tiếp lần 1, 2, 3 và bấm đồng hồ đo thời gian khóa)* | Không | Chạy cuối cùng vì tài khoản `test@eshop.com` sẽ bị khóa sau khi kích hoạt. |

---

## 5. Cách thu thập dữ kiện bằng `checklist/dom_probe.js`

Trên từng trang (`/register`, `/login`, `/forgot-password` Bước 1, `/forgot-password` Bước 2, `/profile`), mở **DevTools -> Console**, dán toàn bộ nội dung file `checklist/dom_probe.js` và nhấn `Enter`. Script chỉ đọc DOM và in JSON dữ kiện khách quan (sinh viên tự đối chiếu Expected để kết luận `Passed`/`Failed`):

| Trường trong JSON của `dom_probe.js` | Phục vụ đối chiếu các mục checklist |
|---|---|
| `url`, `ua`, `viewport`, `title` | Ghi thông số môi trường lượt chạy; kiểm `SV-16` (`document.title`). |
| `h1`, `headings` | Kiểm số lượng và nội dung thẻ `<h1>` cấp trang: `CL-03`, `CL-04`, `CL-05`, `CL-06`. |
| `horizontal_scroll`, `text_overflow_candidates` | Kiểm tràn ngang khung nhìn: `CL-09`, `CL-10`, `SV-06`, `SV-18`. |
| `fields[]` (`type`, `required`, `disabled`, `readonly`, `label`, `label_linked`, `label_has_asterisk`, `autocomplete`) | Kiểm `CL-12` (dấu `*`), `CL-13` & `CL-14` (`type="email"`), `CL-15` (`type="password"`), `CL-16` & `CL-18` (trường xác nhận), `CL-21` (`Email` disabled), `CL-23` (`label_linked`), `SV-12` (`autocomplete`), `SV-20` (`type`/`inputmode`). |
| `buttons[]` (`text`, `bg`, `color`, `contrast`, `x`, `y`, `w`, `h`, `disabled`) | Kiểm `CL-01` & `CL-02` (nhãn nút), `CL-07` & `CL-08` (màu RGB nền nút), `CL-09` (căn lề `x`, `w`), `CL-11` (tương phản `contrast`), `CL-37` (`disabled`), `SV-19` (`w >= 24`, `h >= 24`). |
| `tab_order[]` (`tag`, `text`, `tabindex`, `y`) | Hỗ trợ kiểm thứ tự `Tab`: `SV-01`, `SV-02` (kết hợp bấm phím `Tab` thực tế để kiểm cả `SV-17`). |
| `messages[]` (`text`, `y`, `above_submit`) | Chạy lại sau khi kích hoạt lỗi form để lấy toạ độ dọc của khối lỗi so với nút Submit: `SV-03`, `SV-04`, `CL-32`, `CL-34`. |
| `nav_links[]` (`text`, `href`, `aria_current`, `cls`) | Kiểm `CL-24` (highlight trang đang mở), `CL-25` (nhãn `Đăng xuất`), `CL-28` (liên kết điều hướng). |
| `innerhtml_risk` | Hỗ trợ phát hiện dấu hiệu thẻ HTML chưa escape hoặc lọt vào Header: `SV-05`. |

---

## 6. Quy trình ghi kết quả CSV và Gộp từng nền tảng (Bước 4)

1. Nhân bản file khung tương ứng trong `checklist/runs/` thành file lượt chạy có gắn dấu thời gian:
   - `checklist/runs/P1_template.csv` -> `checklist/runs/P1_<YYYYMMDD-HHMM>.csv`
   - `checklist/runs/P2_template.csv` -> `checklist/runs/P2_<YYYYMMDD-HHMM>.csv`
   - `checklist/runs/P3_template.csv` -> `checklist/runs/P3_<YYYYMMDD-HHMM>.csv`
2. Điền 4 cột chuẩn `id,status,notes,evidence`:
   - `status`: chỉ nhận một trong 4 giá trị `Passed`, `Failed`, `N/A`, `Blocked` (các mục không áp dụng theo thiết kế đã được điền sẵn `N/A`).
   - `notes`:
     - Bắt buộc ghi **Actual nguyên văn + lý do lệch Expected** đối với mọi mục `Failed`.
     - Bắt buộc ghi **mã mục gây chặn** (ví dụ `Bị chặn bởi CL-19: ...`) đối với mọi mục `Blocked`.
   - `evidence`: đường dẫn tương đối từ gốc repo tới ảnh minh chứng cho mọi mục `Failed` (ví dụ `screenshots/task1_failed/P1_CL-01.png`; nhiều ảnh phân tách bằng dấu `;`). Để trống nếu `Passed` hoặc `N/A`.
3. Chạy lệnh kiểm thử gộp (`--dry-run` trước, gộp thật sau, rồi kiểm tra ràng buộc):
   ```powershell
   python ".agents/skills/gui-checklist-testing/scripts/merge_platform.py" checklist/checklist.json checklist/runs/<file>.csv --platform <Px> --dry-run
   python ".agents/skills/gui-checklist-testing/scripts/merge_platform.py" checklist/checklist.json checklist/runs/<file>.csv --platform <Px>
   python ".agents/skills/gui-checklist-testing/scripts/render_checklist.py" checklist/checklist.json -o checklist/M1_GUI_Checklist.md
   python ".agents/skills/gui-checklist-testing/scripts/check_checklist.py" checklist/checklist.json --min 41 --min-per-ia 8
   ```
4. Tạo **1 Git commit riêng cho mỗi nền tảng** ngay sau khi `check_checklist.py` báo `0 lỗi`:
   - `test(task1): execute checklist on P1 (Chrome Windows)`
   - `test(task1): execute checklist on P2 (Firefox Windows)`
   - `test(task1): execute checklist on P3 (Safari iPhone)`

---

## 7. Nhật ký các lượt chạy thực tế (Cập nhật trong Bước 4)

| Lượt | Nền tảng | Thời gian (Bắt đầu - Kết thúc) | Môi trường chi tiết | File CSV kết quả | Chính thức? | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | `P1` | `(chờ chạy Bước 4)` | `(điền trước/khi chạy)` | `checklist/runs/P1_...csv` | Có | Reset CSDL trước khi chạy G1..G7 |
| 2 | `P2` | `(chờ chạy Bước 4)` | `(điền trước/khi chạy)` | `checklist/runs/P2_...csv` | Có | Reset CSDL trước khi chạy G1..G7 |
| 3 | `P3` | `(chờ chạy Bước 4)` | `(điền trước/khi chạy)` | `checklist/runs/P3_...csv` | Có | Reset CSDL + bật Local Tunnel trước khi chạy |

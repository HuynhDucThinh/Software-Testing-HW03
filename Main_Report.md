# Báo Cáo Chính HW03-AI — Kiểm Thử Giao Diện (GUI Checklist), Đa Nền Tảng & Khả Năng Sử Dụng

## 1. Thông Tin Chung & Phạm Vi Kiểm Thử

| Hạng mục | Nội dung chi tiết |
| :--- | :--- |
| **Họ và tên sinh viên** | Huỳnh Đức Thịnh |
| **Mã số sinh viên (MSSV)** | `23120199` |
| **Email sinh viên** | `23120199@student.hcmus.edu.vn` |
| **Hệ thống kiểm thử (SUT)** | EShop Web & API (`./eshop-sut`, commit gốc `1a9304a`) |
| **Phạm vi phân công nhóm (`M1`)** | Phân hệ Xác thực & Hồ sơ cá nhân người dùng (Web) |
| **Màn hình chính (Task 1)** | `Register` (`/register` — điều khoản `FR-01`) |
| **Các màn hình / vùng phụ (Task 1)** | `Login` (`/login` — `FR-02`), `ForgotPassword` 2 bước (`/forgot-password` — `FR-03`), `Profile` khối Hồ sơ cá nhân (`/profile` — `FR-04`), `Header/Navbar` (`App.jsx` — `FR-23`, `SEC-04`) |
| **Ranh giới không chồng lấn nhóm** | Khối `Lịch sử đơn hàng` tại `/profile` (`FR-11`) thuộc thành viên `M3`; chỉ khảo sát thẻ `<h2>` cấp trang ở `CL-06`, không kiểm tra dữ liệu đơn hàng |
| **Luồng đánh giá Usability (Task 2)** | `F1`: Đăng ký tài khoản mới -> Đăng nhập -> Cập nhật hồ sơ cá nhân (`FR-01` -> `FR-02` -> `FR-04`) |
| **Ba nền tảng thực thi (Task 3)** | `P1`: Google Chrome `157.0.8103.50` (Windows 11) · `P2`: Mozilla Firefox `137.0.1` (Windows 11) · `P3`: Chrome Android `156.0.8078.79` trên `OPPO Reno10 5G` (Android 15) |

---

## 2. Task 1 — Kiểm Thử Giao Diện Theo Checklist (GUI Checklist Testing)

### 2.1. Quy trình khảo sát và thiết kế theo 3 nguồn chuẩn

Quá trình thiết kế tuân thủ chặt chẽ quy trình từng bước của skill `.agents/skills/gui-checklist-testing/SKILL.md`:

1. **Bước 0 — Khảo sát hiện trạng (`Inventory`) & Cơ sở kiểm thử (`Test Basis`):**
   - Lập danh mục toàn bộ control thực tế trên 5 vùng giao diện M1 trong `checklist/m1_inventory.md` (loại thẻ, nhãn, `type`, `required`, thuộc tính liên kết `<label>`, thông báo thực tế và dòng mã nguồn).
   - Trích lục nguyên văn các điều khoản UI và bảo mật hiển thị từ `eshop-sut/README.md` (`FR-01`..`FR-04`, `FR-21`..`FR-24`, `SEC-04`, `SEC-07`) vào `checklist/m1_test_basis.md` để làm chuẩn đối chiếu (oracle) độc lập với lỗi hiện hành trong mã nguồn.
2. **Bước 1 — AI nháp Checklist có cấu trúc theo từng khía cạnh giao diện (`IA-01`..`IA-04`):**
   - Thực hiện 4 lượt prompt tách biệt cho `IA-01` (General UI standards), `IA-02` (Forms), `IA-03` (Navigation), `IA-04` (Feedback / state), kết hợp 3 nguồn:
     - **`SRS` (37 mục — 62.71%):** Bám sát đặc tả yêu cầu chức năng và tiêu chuẩn giao diện bắt buộc của EShop.
     - **`Control` (10 mục — 16.95%):** Dựa trên danh mục kiểm tra chuẩn theo loại thành phần giao diện (ô nhập văn bản, nút bấm, liên kết, thông báo, tràn bố cục).
     - **`Heuristic` (12 mục — 20.34%):** Vận dụng 10 nguyên tắc Nielsen, quy tắc vàng Shneiderman và tiêu chuẩn tiếp cận WCAG 2.1/2.2 tại các khoảng lặng của đặc tả.
   - Mọi mục đều viết theo công thức định lượng: `[Thành phần giao diện] + [Thao tác / điều kiện] + [Kết quả thị giác mong đợi] + "Fail nếu <ngưỡng quan sát/đo được>"`, kèm hệ thống giả định tường minh (`GA1`..`GA8`, `NA1`..`NA2`).
3. **Bước 2 — Sinh viên rà soát, hiệu chỉnh (`Both`: 2 mục) và bổ sung khoảng trống AI bỏ sót (`SV`: 20 mục):**
   - Hiệu chỉnh sâu `CL-10` và `CL-31` (`nguon: "Both"`), đồng thời tự bổ sung **20 mục mới (`SV-01`..`SV-20`)** nâng tổng số lên **59 mục** (vượt xa yêu cầu tối thiểu `> 40` mục, tối thiểu 10 mục trên mỗi IA).

### 2.2. Phân tích khoảng trống của AI (Gap Analysis trên 20 mục `SV-01`..`SV-20`)

Bảng dưới đây tổng hợp các nhóm điểm mù khiến bản nháp đầu của AI bỏ sót 20 mục kiểm tra quan trọng, cùng hiệu quả phát hiện lỗi thực tế của các mục do sinh viên bổ sung:

| Phân loại nguyên nhân AI bỏ sót | Số mục SV bổ sung | Danh sách mã mục (`SV-xx`) | Tóm tắt nguyên nhân cốt lõi & Hiệu quả phát hiện lỗi thật |
| :--- | :---: | :--- | :--- |
| **`giới hạn model`** | **8** | `SV-03`, `SV-06`, `SV-07`, `SV-09`, `SV-13`, `SV-14`, `SV-16`, `SV-19` | AI sinh checklist từ văn bản tĩnh nên chỉ lấy 1 ký tự đại diện (`!` trong `CL-19`) thay vì vét cạn tập `@ $ ! % * ? &` (`SV-09`), quên đối chiếu sự bất đối xứng gợi ý mật khẩu giữa Bước 1/Bước 2 (`SV-13`, `SV-14`), quên dữ liệu tên dài cực trị 100 ký tự (`SV-06`), tọa độ thực tế khối lỗi dưới nút Submit (`SV-03`), kích thước vùng chạm `< 24px` (`SV-19`) và `document.title` vỏ trình duyệt (`SV-16`). **7/8 mục này đã phát hiện lỗi thật trên SUT.** |
| **`đặc điểm giao diện`** | **6** | `SV-01`, `SV-04`, `SV-11`, `SV-12`, `SV-15`, `SV-20` | Các lỗi chỉ bộc lộ khi tương tác vật lý trên trình duyệt/thiết bị thật: nhấn `Tab` phát hiện `tabIndex={1}` nhảy cóc vào nút `Sign In` (`SV-01`), gõ toàn dấu cách vượt qua `required` làm Header còn `Chào,` (`SV-11`), trình duyệt tự điền nhầm email vào ô OTP do thiếu `autocomplete` (`SV-12`), khoảng cách khối lỗi xa nút `Đăng Ký` (`SV-04`), và bàn phím chữ cái QWERTY bật lên ở ô SĐT trên di động (`SV-20`). **5/6 mục phát hiện lỗi thật.** |
| **`prompt`** | **6** | `SV-02`, `SV-05`, `SV-08`, `SV-10`, `SV-17`, `SV-18` | Các lượt prompt theo IA tập trung vào `FR-21..24` mà chưa yêu cầu phân tích giá trị biên độ dài mật khẩu 7-8 ký tự (`SV-08`), biên độ dài & chữ số đầu SĐT (`SV-10`), điều khoản bảo mật hiển thị HTML `SEC-04` trên Header (`SV-05`), thứ tự `Tab` từng bước form phụ (`SV-02`), viền focus bàn phím (`SV-17`) và phóng to 200% (`SV-18`). **3/6 mục phát hiện lỗi nghiêm trọng (trong đó `SV-05` phát hiện lỗ hổng Stored XSS qua `dangerouslySetInnerHTML`).** |

> **Đánh giá hiệu quả Human-in-the-Loop:** Trong 20 mục do sinh viên tự bổ sung, có tới **15/20 mục (75.0%) phát hiện lỗi thực tế** trên SUT (`14` mục Failed trên `P1`/`P2` và `14` mục Failed trên `P3`, bao gồm mục riêng di động `SV-20`).

### 2.3. Tổng hợp kết quả thực thi GUI Checklist

Toàn bộ dữ liệu chi tiết từng mục được xuất đồng bộ tại:
- Bảng Markdown đầy đủ: `checklist/M1_GUI_Checklist.md`
- Sổ làm việc Excel 3 sheet (`Test Cases`, `Checklist`, `Test Summary Report` có công thức tự động): `checklist/M1_GUI_Checklist_And_Summary.xlsx`

#### Bảng 2.3a — Thống kê kết quả theo Nền tảng

| Chỉ số | `P1` — Chrome 157 (Win 11) | `P2` — Firefox 137 (Win 11) | `P3` — Chrome Android 156 (OPPO Reno10 5G) | Tổng cộng (3 nền tảng) |
| :--- | :---: | :---: | :---: | :---: |
| **Tổng mục thiết kế** | 59 | 59 | 59 | **177** |
| **Số mục đã chạy** | 58 | 58 | 52 | **168** |
| **Passed** | 14 | 14 | 10 | **38** |
| **Failed** | 44 | 44 | 42 | **130** |
| **N/A (có giả định)** | 1 | 1 | 7 | **9** |
| **Blocked / Chưa chạy** | 0 | 0 | 0 | **0** |

#### Bảng 2.3b — Thống kê kết quả theo Khía cạnh giao diện (`IA-01` .. `IA-04`)

| Khía cạnh giao diện (IA) | Số mục thiết kế | `P1` (Pass / Fail / N/A) | `P2` (Pass / Fail / N/A) | `P3` (Pass / Fail / N/A) | Tỷ lệ Failed trên Desktop (`P1`/`P2`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`IA-01` — General UI standards** | 14 | 5 / 9 / 0 | 5 / 9 / 0 | 3 / 9 / 2 | 64.29% |
| **`IA-02` — Forms** | 23 | 1 / 21 / 1 | 1 / 21 / 1 | 1 / 22 / 0 | 95.45% (trên 22 mục áp dụng) |
| **`IA-03` — Navigation** | 12 | 4 / 8 / 0 | 4 / 8 / 0 | 2 / 6 / 4 | 66.67% |
| **`IA-04` — Feedback / state** | 10 | 4 / 6 / 0 | 4 / 6 / 0 | 4 / 5 / 1 | 60.00% |
| **Tổng cộng** | **59** | **14 / 44 / 1** | **14 / 44 / 1** | **10 / 42 / 7** | **75.86%** |

#### Bảng 2.3c — Thống kê kết quả theo Loại căn cứ và Nguồn thiết kế

| Phân nhóm | Số mục | `P1` (Pass / Fail / N/A) | `P2` (Pass / Fail / N/A) | `P3` (Pass / Fail / N/A) |
| :--- | :---: | :---: | :---: | :---: |
| **Loại căn cứ: `SRS`** | 37 | 6 / 31 / 0 | 6 / 31 / 0 | 5 / 30 / 2 |
| **Loại căn cứ: `Control`** | 10 | 4 / 5 / 1 | 4 / 5 / 1 | 3 / 4 / 3 |
| **Loại căn cứ: `Heuristic`** | 12 | 4 / 8 / 0 | 4 / 8 / 0 | 2 / 8 / 2 |
| **Nguồn thiết kế: `AI`** | 37 | 7 / 30 / 0 | 7 / 30 / 0 | 7 / 28 / 2 |
| **Nguồn thiết kế: `Both`** | 2 | 2 / 0 / 0 | 2 / 0 / 0 | 1 / 0 / 1 |
| **Nguồn thiết kế: `SV`** | 20 | 5 / 14 / 1 | 5 / 14 / 1 | 2 / 14 / 4 |

### 2.4. Nhận xét chuyên môn về chất lượng GUI của phân hệ M1

Kết quả thực thi cho thấy **`45 / 59` mục kiểm tra độc lập bị `Failed`** (chỉ `14 / 59` mục đạt `Passed` như căn lề dọc form `CL-09`, bố cục cơ bản 3 viewport với dữ liệu ngắn `CL-10`, vô hiệu hóa ô Email hồ sơ `CL-21`, giữ dữ liệu có dấu `SV-07`, hủy OTP sau khi sử dụng `CL-38`, không lộ trường sai khi đăng nhập `CL-34`). Các lỗi tập trung thành 5 cụm nghiêm trọng:

1. **Lỗi biểu thức chính quy & kiểm tra biểu mẫu chặn đứng luồng người dùng hợp lệ (`IA-02`):**
   - Biểu thức chính quy mật khẩu tại `Register.jsx` và `ForgotPassword.jsx` viết nhầm `(?=.*\s)[A-Za-z\d\s]{8,}` (bắt buộc có khoảng trắng và cấm toàn bộ ký tự đặc biệt `@ $ ! % * ? &`), khiến mọi mật khẩu hợp lệ theo đặc tả như `Abcd123!` đều bị từ chối (`CL-19`, `SV-08`, `SV-09`).
   - Biểu thức kiểm tra SĐT tại `Profile.jsx` (`/^[1-9][0-9]{8,9}$/`) từ chối toàn bộ SĐT Việt Nam bắt đầu bằng số `0` như `0912345678` (`CL-22`), nhưng lại chấp nhận số sai chuẩn không có `0` đầu `9123456789` (`SV-10`).
   - Backend thiếu ràng buộc `UNIQUE` cho cột `email` và không kiểm tra trùng tại `POST /api/register`, cho phép đăng ký trùng lặp tài khoản `test@eshop.com` mà không báo lỗi (`CL-32`).
2. **Lỗi bảo mật hiển thị & lộ thông tin nhạy cảm (`IA-02`, `IA-04`):**
   - Ô mật khẩu trên `/login` đặt `type="text"` làm lộ rõ toàn bộ mật khẩu dạng chữ thường (`CL-15`).
   - Thanh `Header` (`App.jsx`) render lời chào bằng `dangerouslySetInnerHTML`, gây lỗ hổng Stored XSS thực thi trực tiếp thẻ HTML trong `Họ Tên` (`SV-05`).
3. **Sai lệch chuẩn ngôn ngữ, phân cấp tiêu đề, màu sắc và độ tương phản (`IA-01`):**
   - Trang `/login` đặt tiêu đề sai chức năng là `<h2>Đăng Ký</h2>` (`CL-04`), trộn lẫn nhãn tiếng Anh `Username`, `Sign In` (`CL-01`); nút thoát dùng chữ `Thoát` thay vì `Đăng xuất` (`CL-25`); cả 4 trang thiếu thẻ `<h1>` (`CL-03`..`CL-06`) và trùng tiêu đề tab `frontend-web` (`SV-16`).
   - Nút `Đăng Ký` dùng màu đỏ nguy hiểm thay vì xanh dương (`CL-07`), Bước 2 Quên mật khẩu tô xanh lá giống hệt nhau cho cả nút chính và nút quay lại (`CL-08`), độ tương phản dòng gợi ý mật khẩu chỉ đạt `2.54:1 < 4.5:1` (`CL-11`).
4. **Lỗi điều hướng, tiếp cận bàn phím và thiết bị di động (`IA-02`, `IA-03`):**
   - Nút `Sign In` gắn cứng `tabIndex={1}` khiến lần nhấn `Tab` đầu tiên nhảy cóc qua cả hai ô nhập (`SV-01`); `0/10` thẻ `<label>` liên kết `for`/`id` với `input` (`CL-23`); thiếu `autocomplete` làm trình duyệt điền nhầm email vào ô OTP (`SV-12`); link `Quên mật khẩu?` dùng `<a href>` gây tải lại toàn trang (`CL-28`); truy cập `/profile` khi chưa đăng nhập không chuyển hướng về `/login` (`CL-30`); ô SĐT thiếu `type="tel"` trên di động (`SV-20`).
5. **Lỗi phản hồi trạng thái và đồng bộ dữ liệu (`IA-04`):**
   - Khóa tài khoản ngay sau **2** lần nhập sai (do `login_attempts + 2`) trong **180 giây** thay vì 3 lần / 30 giây và không hiển thị thông báo tài khoản bị khóa (`CL-33`).
   - Dùng hộp thoại `window.alert()` kèm thông báo tiếng Anh thô `Lỗi: User not found` (`CL-35`); cập nhật hồ sơ xong không đồng bộ lời chào trên `Header` nếu chưa tải lại trang (`CL-36`); thiếu trạng thái `disabled`/loading chống bấm đúp (`CL-37`).

---

## 3. Task 3 — Kiểm Thử Đa Trình Duyệt / Đa Nền Tảng (Cross-Browser / Cross-Platform)

### 3.1. Cấu hình chi tiết 3 nền tảng thực thi

| Mã | Vai trò nền tảng | Trình duyệt & Nhân (Engine) | Hệ điều hành / Thiết bị | Độ phân giải / Khung nhìn | File kết quả chính thức |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **`P1`** | Desktop Browser 1 | Google Chrome `157.0.8103.50` (Blink / Chromium) | Windows 11 (Build 26300) | Desktop `1920x1080` (`1440x900` kiểm thử) | `checklist/runs/P1_20261111-1650.csv` |
| **`P2`** | Desktop Browser 2 | Mozilla Firefox `137.0.1` (Gecko) | Windows 11 (Build 26300) | Desktop `1920x1080` (`1440x900` kiểm thử) | `checklist/runs/P2_20261111-1700.csv` |
| **`P3`** | Mobile Browser | Chrome Android `156.0.8078.79` (Blink Mobile) | `OPPO Reno10 5G` (`CPH2531`) — Android 15 (`adb reverse`) | Vật lý `1080x2412` (khung nhìn mobile dọc) | `checklist/runs/P3_20261111-1710.csv` |

### 3.2. Phân tích tính nhất quán và khác biệt giữa các nền tảng

1. **Giữa `P1` (Chrome / Blink) và `P2` (Firefox / Gecko) trên Windows 11:**
   - Kết quả verdict đồng nhất tuyệt đối trên toàn bộ 58 mục áp dụng (`14 Passed, 44 Failed, 1 N/A`).
   - Khác biệt chi tiết ở mức engine: đường viền focus mặc định khi nhấn `Tab` (`SV-17`) và hộp thoại hệ thống `window.alert()` (`CL-35`, `CL-22`) có giao diện riêng theo từng trình duyệt, đồng thời chiều cao dòng liên kết văn bản chênh lệch nhẹ ~0.5–1px nhưng đều nhỏ hơn ngưỡng tối thiểu `24x24 CSS px` (`19px` < `24px` ở `SV-19`).
2. **Giữa Desktop (`P1`, `P2`) và Mobile (`P3` — Chrome Android trên `OPPO Reno10 5G`):**
   - `7` mục phụ thuộc công cụ/thao tác riêng của máy tính để bàn (con trỏ chuột `:hover` `CL-31`, bàn phím vật lý `Tab` `SV-01, SV-02, SV-17`, đổi đa khung nhìn `CL-10`, zoom 200% desktop `SV-18`, Network Slow 3G `CL-37`) được phân loại `N/A` theo giả định `NA1`.
   - Ngược lại, nền tảng di động `P3` kích hoạt mục đặc thù cảm ứng **`SV-20`** (thuộc tính `type="tel"` / `inputmode="numeric"` cho ô Số điện thoại tại `/profile`, vốn là `N/A` trên `P1, P2` theo `NA2`) và phát hiện lỗi mở bàn phím chữ cái QWERTY thay vì bàn phím số.
   - Ngoài ra trên màn hình hẹp của `P3`, lỗi tràn ngang thanh `Header` khi `Họ Tên` dài 100 ký tự không khoảng trắng (`SV-06`) thể hiện nghiêm trọng ngay ở chế độ mặc định (`scrollWidth = 1118px > clientWidth = 360px`), đẩy nút `Thoát` hoàn toàn ra ngoài màn hình cảm ứng, đồng thời các liên kết văn bản (`Đăng nhập`, `Quên mật khẩu?`, `Đăng ký ngay`) chỉ cao `16px` (`SV-19`), rất dễ chạm nhầm bằng ngón tay.

### 3.3. Bộ ảnh chụp tổng quan đa nền tảng (Cross-Platform Screenshots)

Mỗi ảnh tổng quan trong `screenshots/task3_cross_platform/` đều hiển thị đầy đủ thông tin nền tảng/trình duyệt/thiết bị, địa chỉ `http://localhost:5173/...`, chuỗi nhận diện `23120199 - Huỳnh Đức Thịnh` trong biểu mẫu và lớp phủ email `23120199@student.hcmus.edu.vn`:

| Màn hình | `P1` (Chrome / Windows 11) | `P2` (Firefox / Windows 11) | `P3` (Chrome Android / OPPO Reno10 5G) |
| :--- | :--- | :--- | :--- |
| **`Register` (`/register`)** | `screenshots/task3_cross_platform/P1_Register_1.png` | `screenshots/task3_cross_platform/P2_Register_1.png` | `screenshots/task3_cross_platform/P3_Register_1.png` |
| **`Login` (`/login`)** | `screenshots/task3_cross_platform/P1_Login_1.png` | `screenshots/task3_cross_platform/P2_Login_1.png` | `screenshots/task3_cross_platform/P3_Login_1.png` |
| **`ForgotPassword` (`/forgot-password`)** | `screenshots/task3_cross_platform/P1_ForgotPassword_1.png` | `screenshots/task3_cross_platform/P2_ForgotPassword_1.png` | `screenshots/task3_cross_platform/P3_ForgotPassword_1.png` |
| **`Profile` (`/profile`)** | `screenshots/task3_cross_platform/P1_Profile_1.png` | `screenshots/task3_cross_platform/P2_Profile_1.png` | `screenshots/task3_cross_platform/P3_Profile_1.png` |

---

## 4. Tổng Hợp Báo Cáo Lỗi & GitHub Issues (Task 1 & Task 3)

Từ `45 / 59` mục Checklist bị `Failed` (`130` ô lỗi trên 3 nền tảng `P1`, `P2`, `P3`), các mục có cùng nguyên nhân gốc hoặc biểu hiện trên cùng thành phần giao diện đã được gom nhóm chống trùng lặp thành **`27` báo cáo lỗi độc lập (`BUG-01` .. `BUG-27`)** (chi tiết gom nhóm tại `bugs/bug_groups.md`, hồ sơ đầy đủ tại `Bug_Report.md` và `bugs/BUG-01.md`..`BUG-27.md`), đồng thời đăng đầy đủ **27 GitHub Issues (`#1` .. `#27`)** kèm ảnh chụp màn hình đính kèm tại:

- **Trang GitHub Issues:** [https://github.com/HuynhDucThinh/Software-Testing-HW03/issues](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues)
- **Bộ ảnh chụp trang GitHub Issues:** `screenshots/github_issues/GitHub_Issues_Overview_Page1.png`, `GitHub_Issues_Overview_Page2.png` và `screenshots/github_issues/ISSUE-01_BUG-01.png` .. `ISSUE-27_BUG-27.png`.
- **Phân bố mức độ nghiêm trọng (`Severity`):** **5 Critical** (`18.52%`), **10 Major** (`37.04%`), **11 Minor** (`40.74%`), **1 Cosmetic** (`3.70%`).

| Mã Bug | Issue | IA | Severity | Checklist Items | Nền tảng | Tiêu đề tóm tắt |
| :---: | :---: | :---: | :---: | :--- | :---: | :--- |
| [`BUG-01`](bugs/BUG-01.md) | [#1](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/1) | `IA-02` | **Critical** | `CL-19`, `SV-08`, `SV-09` | P1, P2, P3 | [Register, ForgotPassword] Biểu thức chính quy mật khẩu bắt buộc khoảng trắng và từ chối toàn bộ ký tự đặc biệt hợp lệ (@ $ ! % * ? &) |
| [`BUG-02`](bugs/BUG-02.md) | [#2](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/2) | `IA-04` | **Critical** | `CL-32` | P1, P2, P3 | [Register] Cho phép đăng ký trùng lặp địa chỉ Email đã tồn tại mà không kiểm tra duy nhất hay hiển thị thông báo lỗi |
| [`BUG-03`](bugs/BUG-03.md) | [#3](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/3) | `IA-04` | **Critical** | `SV-05` | P1, P2, P3 | [Header, Profile] Lỗ hổng Stored XSS ở lời chào trên Header do hiển thị Họ Tên qua dangerouslySetInnerHTML |
| [`BUG-04`](bugs/BUG-04.md) | [#4](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/4) | `IA-02` | **Critical** | `CL-15` | P1, P2, P3 | [Login] Ô nhập Mật khẩu trên trang Đăng nhập dùng type='text' làm lộ toàn bộ ký tự mật khẩu trên màn hình |
| [`BUG-05`](bugs/BUG-05.md) | [#5](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/5) | `IA-02` | **Critical** | `CL-22`, `SV-10` | P1, P2, P3 | [Profile] Kiểm tra Số điện thoại sai biểu thức chính quy: từ chối số hợp lệ bắt đầu bằng 0 nhưng chấp nhận số không có 0 đầu |
| [`BUG-06`](bugs/BUG-06.md) | [#6](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/6) | `IA-04` | **Major** | `CL-33` | P1, P2, P3 | [Login] Khóa tài khoản sớm ngay sau 2 lần nhập sai mật khẩu trong 180 giây và không hiển thị thông báo tài khoản đang bị khóa |
| [`BUG-07`](bugs/BUG-07.md) | [#7](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/7) | `IA-02` | **Major** | `CL-16`, `CL-18` | P1, P2, P3 | [Register, ForgotPassword] Biểu mẫu Đăng ký và Đặt lại mật khẩu (Bước 2) thiếu hoàn toàn trường Xác nhận mật khẩu |
| [`BUG-08`](bugs/BUG-08.md) | [#8](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/8) | `IA-02` | **Major** | `CL-20` | P1, P2, P3 | [ForgotPassword] Mã OTP khôi phục mật khẩu chỉ sinh 4 chữ số thay vì 6 chữ số theo đặc tả FR-03 và SEC-07 |
| [`BUG-09`](bugs/BUG-09.md) | [#9](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/9) | `IA-02` | **Major** | `CL-13`, `CL-14` | P1, P2, P3 | [Register, Login, ForgotPassword] Tất cả ô nhập Email khai báo type='text' khiến chuỗi sai định dạng email vẫn gửi request lên API |
| [`BUG-10`](bugs/BUG-10.md) | [#10](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/10) | `IA-03` | **Major** | `CL-30` | P1, P2, P3 | [Profile] Truy cập trực tiếp /profile khi chưa đăng nhập không tự chuyển hướng về /login và không có liên kết đăng nhập trong vùng nội dung |
| [`BUG-11`](bugs/BUG-11.md) | [#11](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/11) | `IA-04` | **Major** | `CL-36` | P1, P2, P3 | [Profile, Header] Lời chào trên thanh Header không cập nhật theo Họ Tên mới sau khi lưu Hồ sơ thành công |
| [`BUG-12`](bugs/BUG-12.md) | [#12](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/12) | `IA-02` | **Major** | `SV-11` | P1, P2, P3 | [Register, Profile] Chấp nhận trường Họ Tên chỉ gồm toàn ký tự khoảng trắng khiến lời chào Header hiển thị cụt 'Chào,' |
| [`BUG-13`](bugs/BUG-13.md) | [#13](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/13) | `IA-01` | **Major** | `CL-03`, `CL-04`, `CL-05`, `CL-06` | P1, P2, P3 | [Register, Login, ForgotPassword, Profile] Cả 4 trang thiếu thẻ tiêu đề cấp trang h1 và trang Đăng nhập hiển thị sai tiêu đề thành 'Đăng Ký' |
| [`BUG-14`](bugs/BUG-14.md) | [#14](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/14) | `IA-01` | **Minor** | `CL-01`, `CL-25` | P1, P2, P3 | [Login, Header] Giao diện không nhất quán tiếng Việt: trang Đăng nhập trộn nhãn tiếng Anh ('Username', 'Sign In') và Header dùng nhãn 'Thoát' thay vì 'Đăng xuất' |
| [`BUG-15`](bugs/BUG-15.md) | [#15](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/15) | `IA-03` | **Major** | `SV-01` | P1, P2 | [Login] Thứ tự di chuyển focus bằng phím Tab bị đảo ngược do nút 'Sign In' gắn cứng tabIndex={1} |
| [`BUG-16`](bugs/BUG-16.md) | [#16](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/16) | `IA-04` | **Major** | `CL-35` | P1, P2, P3 | [ForgotPassword, Profile] Sử dụng hộp thoại chặn window.alert() và hiển thị thông báo lỗi tiếng Anh thô 'Lỗi: User not found' |
| [`BUG-17`](bugs/BUG-17.md) | [#17](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/17) | `IA-02` | **Minor** | `SV-03`, `SV-04` | P1, P2, P3 | [Login, Register] Vị trí khối thông báo lỗi đặt sai chuẩn: nằm bên dưới nút 'Sign In' ở Đăng nhập và cách xa nút 'Đăng Ký' 336px ở đầu form Đăng ký |
| [`BUG-18`](bugs/BUG-18.md) | [#18](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/18) | `IA-01` | **Minor** | `SV-06` | P1, P2, P3 | [Header] Họ Tên dài 100 ký tự không khoảng trắng làm tràn ngang thanh Header và đẩy nút 'Thoát' ra khỏi khung nhìn |
| [`BUG-19`](bugs/BUG-19.md) | [#19](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/19) | `IA-01` | **Minor** | `CL-07`, `CL-08` | P1, P2, P3 | [Register, ForgotPassword, Header] Màu sắc nút bấm vi phạm ngữ nghĩa: nút 'Đăng Ký' dùng màu đỏ nguy hiểm, hai nút Bước 2 Quên mật khẩu trùng màu xanh lá, nút 'Thoát' chỉ là chữ xám |
| [`BUG-20`](bugs/BUG-20.md) | [#20](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/20) | `IA-01` | **Minor** | `CL-11` | P1, P2, P3 | [Register] Dòng hướng dẫn quy tắc mật khẩu màu xám nhạt (#9ca3af) chỉ đạt độ tương phản 2.54:1, thấp hơn chuẩn WCAG AA 4.5:1 |
| [`BUG-21`](bugs/BUG-21.md) | [#21](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/21) | `IA-03` | **Minor** | `CL-17`, `CL-26` | P1, P2, P3 | [ForgotPassword] Luồng Quên mật khẩu 2 bước thiếu chỉ báo bước (Step Indicator) và Bước 1 thiếu liên kết 'Quay lại đăng nhập' |
| [`BUG-22`](bugs/BUG-22.md) | [#22](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/22) | `IA-02` | **Minor** | `SV-13`, `SV-14` | P1, P2, P3 | [ForgotPassword, Register] Bước 2 Quên mật khẩu thiếu hẳn dòng gợi ý quy tắc mật khẩu và dòng gợi ý trên Đăng ký không liệt kê tập ký tự đặc biệt cho phép |
| [`BUG-23`](bugs/BUG-23.md) | [#23](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/23) | `IA-02` | **Minor** | `CL-12`, `CL-23` | P1, P2, P3 | [Register, Login, ForgotPassword, Profile] Tất cả nhãn trường bắt buộc thiếu dấu sao (*) và 10/10 thẻ label không liên kết htmlFor/id với ô nhập liệu |
| [`BUG-24`](bugs/BUG-24.md) | [#24](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/24) | `IA-02` | **Minor** | `SV-12`, `SV-20` | P1, P2, P3 | [Login, ForgotPassword, Profile] Ô nhập thiếu thuộc tính name/autocomplete gây tự điền nhầm Email vào ô OTP và ô Số điện thoại thiếu type='tel' mở bàn phím chữ trên di động |
| [`BUG-25`](bugs/BUG-25.md) | [#25](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/25) | `IA-03` | **Minor** | `CL-24`, `CL-28`, `SV-16` | P1, P2, P3 | [Header, Login] Thanh Navbar không đánh dấu mục trang đang mở, liên kết 'Quên mật khẩu?' gây tải lại toàn trang và tiêu đề tab trình duyệt giữ nguyên 'frontend-web' ở mọi route |
| [`BUG-26`](bugs/BUG-26.md) | [#26](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/26) | `IA-04` | **Minor** | `CL-37` | P1, P2 | [Register, Login, ForgotPassword, Profile] Các nút gửi biểu mẫu thiếu trạng thái đang xử lý (loading) và không khóa tạm (disabled) để chống bấm đúp khi chờ API |
| [`BUG-27`](bugs/BUG-27.md) | [#27](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/27) | `IA-03` | **Cosmetic** | `CL-31`, `SV-19` | P1, P2, P3 | [All M1 Screens] Nút bấm và liên kết điều hướng thiếu hiệu ứng phản hồi khi rê chuột (:hover) và chiều cao vùng chạm liên kết nhỏ hơn ngưỡng 24x24 CSS px |

---

## 5. Task 2 — Đánh Giá Khả Năng Sử Dụng (Usability Evaluation — Luồng `F1`)

*(Phần kế hoạch đánh giá, kịch bản nhiệm vụ mục tiêu trên luồng `F1`, kết quả phiên Pilot `S00` + 7 phiên người dùng thật ngoài lớp `S01`..`S07`, bảng tính điểm SUS và phân tích mức độ nghiêm trọng sẽ được cập nhật trong giai đoạn Task 2).*

---

## 6. Task 4 — Xây Dựng Agent Skills & Video Trình Diễn

- **Skill 1 — Thiết kế, rà soát và thực thi GUI Checklist:** `.agents/skills/gui-checklist-testing/SKILL.md` (kèm bộ 9 script tự động hóa kiểm tra ràng buộc, đóng băng phiên bản, gộp kết quả đa nền tảng, xuất Excel công thức động, gom khung dữ kiện bug và xuất báo cáo AI Audit).
- **Skill 2 — Đánh giá Khả năng Sử dụng (Usability Evaluation):** *(cập nhật khi triển khai Task 2)*.
- **Video trình diễn end-to-end (YouTube):** *(cập nhật khi hoàn thiện toàn bài)*.

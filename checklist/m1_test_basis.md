# M1 Test Basis - Cơ sở đặc tả kiểm thử giao diện

Nguồn đặc tả gốc: `eshop-sut/README.md` (System Requirements Specification - Phiên bản 2.0, cập nhật 2026-05-14).
Theo Quy tắc 2 của skill `gui-checklist-testing`, tài liệu đặc tả này là **oracle duy nhất** cho các yêu cầu từ SRS. Số dòng dưới đây được trích xuất chính xác từ `eshop-sut/README.md` tại commit `368cd04`.

---

## 1. Điều khoản nghiệp vụ thuộc phạm vi M1 (`FR-01` .. `FR-04` và `FR-05`)

### `FR-01`: Đăng ký tài khoản (`eshop-sut/README.md:30-36`)
Trích nguyên văn:
- Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**. (dòng 32)
- Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống. (dòng 33)
- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`). (dòng 34)
- Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp. (dòng 35)
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập. (dòng 36)

### `FR-02`: Đăng nhập & Khóa tài khoản (`eshop-sut/README.md:38-45`)
Trích nguyên văn:
- Người dùng nhập Email và Mật khẩu. (dòng 40)
- Sau mỗi lần đăng nhập sai, hệ thống tăng bộ đếm lên **đúng 1 đơn vị**. (dòng 41)
- Nếu đăng nhập sai từ **3 lần trở lên** liên tiếp, tài khoản bị tạm khóa **30 giây** (môi trường demo). Hệ thống trả về thông báo lỗi phù hợp; không để lộ chi tiết nguyên nhân. (dòng 42)
- Đăng nhập thành công trả về JWT Token. Token được lưu phía client và gửi kèm tất cả các yêu cầu có xác thực qua header `Authorization: Bearer <token>`. (dòng 43)
- Trường email phải dùng `type="email"` (có validate HTML5 format). (dòng 44)

### `FR-03`: Quên mật khẩu & Đặt lại mật khẩu (2 bước) (`eshop-sut/README.md:46-61`)
Trích nguyên văn:
- **Bước 1 — Lấy mã OTP:** (dòng 48)
  - Người dùng nhập địa chỉ Email đã đăng ký. (dòng 50)
  - Hệ thống sinh mã OTP **6 chữ số ngẫu nhiên** và gửi qua Email (trong môi trường demo: hiển thị trực tiếp trên màn hình). (dòng 51)
  - Giao diện phải hiển thị **chỉ báo bước (Step Indicator)** — ví dụ: "Bước 1 / 2". (dòng 52)
  - Có nút **Quay lại đăng nhập**. (dòng 53)
- **Bước 2 — Đặt lại mật khẩu:** (dòng 55)
  - Người dùng nhập OTP, Mật khẩu mới, và **Xác nhận mật khẩu mới**. (dòng 57)
  - Mật khẩu mới phải tuân thủ điều kiện như FR-01. (dòng 58)
  - Hai trường mật khẩu phải khớp nhau. (dòng 59)
  - OTP chỉ hợp lệ cho email đã yêu cầu, không thể dùng cho email khác. (dòng 60)

### `FR-04`: Quản lý hồ sơ cá nhân (`eshop-sut/README.md:62-68`)
Trích nguyên văn:
- Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**. (dòng 64)
- **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số. (dòng 65)
- Email không được phép thay đổi qua giao diện. (dòng 66)
- Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`. (dòng 67)

### `FR-05` (điều khoản tiêu đề dùng chung toàn hệ thống - `eshop-sut/README.md:81`)
Trích nguyên văn:
- Mỗi trang chỉ có 1 `<h1>` duy nhất. (dòng 81)

---

## 2. Điều khoản giao diện chung (`FR-21` .. `FR-24`) ánh xạ vào `IA-01` .. `IA-04`

### `FR-21`: Tiêu chuẩn Giao diện Chung -> `IA-01` (`eshop-sut/README.md:242-249`)
Trích nguyên văn:
- **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn). (dòng 244)
- **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ. (dòng 245)
- **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn. (dòng 246 - *thuộc các màn hình hiển thị giá/đơn hàng của M2, M3*)
- **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang. (dòng 247)
- **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải. (dòng 248)

### `FR-22`: Form Requirements -> `IA-02` (`eshop-sut/README.md:250-257`)
Trích nguyên văn:
- Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn. (dòng 252)
- Trường Email phải dùng `type="email"`. (dòng 253)
- Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ). (dòng 254)
- Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới. (dòng 255)
- Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng. (dòng 256)

### `FR-23`: Navigation Requirements -> `IA-03` (`eshop-sut/README.md:258-264`)
Trích nguyên văn:
- Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn. (dòng 260)
- Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ. (dòng 261 - *thuộc phạm vi Giỏ hàng M3, chỉ kiểm phần Navbar liên quan M1*)
- Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát"). (dòng 262)
- Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm). (dòng 263 - *thuộc phạm vi M2, M3*)

### `FR-24`: Feedback & State Requirements -> `IA-04` (`eshop-sut/README.md:265-271`)
Trích nguyên văn:
- Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge). (dòng 267 - *thuộc phạm vi M2*)
- Khi xóa item khỏi giỏ phải có dialog xác nhận. (dòng 268 - *thuộc phạm vi M3*)
- Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện. (dòng 269 - *thuộc phạm vi M2, M3*)
- Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng). (dòng 270 - *thuộc phạm vi M2*)

> Ghi chú cho `IA-04` trong phạm vi M1: Ngoài các phản hồi trạng thái quy định trực tiếp tại `FR-01` (chuyển hướng sau đăng ký, báo lỗi trùng email/mật khẩu yếu), `FR-02` (thông báo khóa tạm 30 giây sau 3 lần sai, không lộ chi tiết nguyên nhân), `FR-03` (hiển thị OTP 6 chữ số, phản hồi đặt lại mật khẩu), `FR-04` (phản hồi cập nhật hồ sơ, cập nhật hiển thị lời chào trên Header) và `SEC-04` (hiển thị an toàn dữ liệu tên người dùng), các mục kiểm tra `IA-04` còn lại sẽ dựa trên nguồn **Control checklist** và **Heuristic** (Nielsen #1 Visibility of system status, Nielsen #5 Error prevention, Nielsen #9 Help users recognize, diagnose, and recover from errors) theo `docs/Nhom05_GUI_Testing_Slides.md`.

---

## 3. Điều khoản bảo mật liên quan trực tiếp đến hiển thị GUI phạm vi M1 (`SEC-04`, `SEC-07`)

| Mã | Dòng (`README.md`) | Nội dung trích nguyên văn | Phạm vi áp dụng trong Task 1 (GUI) |
| :---: | :---: | :--- | :--- |
| `SEC-04` | 281 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. | Kiểm tra hiển thị tên người dùng `Chào, <tên>` trên Header (`App.jsx:27`) khi cập nhật Họ Tên chứa thẻ HTML/ký tự đặc biệt. |
| `SEC-07` | 284 | OTP đặt lại mật khẩu phải đủ entropy (tối thiểu 6 chữ số), có thời hạn và vô hiệu hóa sau khi dùng. | Kết hợp với `FR-03` kiểm tra độ dài mã OTP hiển thị trên giao diện và nhãn trường OTP ở Bước 2 màn hình `ForgotPassword`. |

*(Các yêu cầu thuần API/CSDL như `SEC-01`, `SEC-02`, `SEC-03`, `SEC-05`, `SEC-06` không phải kiểm thử GUI nên không đưa vào checklist Task 1).*

---

## 4. Phân định ranh giới phạm vi M1 để tránh trùng lặp nhóm

| Thuộc phạm vi M1 (Đưa vào Checklist) | Ngoài phạm vi M1 (Không đưa vào Checklist) |
| :--- | :--- |
| Toàn bộ màn hình `Register` (`/register`) | Danh sách sản phẩm, tìm kiếm, thẻ giá `₫`, `alt` ảnh trên `Home` & `ProductDetail` (M2) |
| Toàn bộ màn hình `Login` (`/login`) | Thêm vào giỏ, xóa giỏ hàng, badge số lượng giỏ, mã giảm giá trên `Cart` & `Checkout` (M3) |
| Toàn bộ màn hình `ForgotPassword` 2 bước (`/forgot-password`) | Bảng `Lịch sử đơn hàng` và nút `Hủy đơn` bên cột phải trang `/profile` (M3) |
| Khối `Hồ sơ của bạn` và cấu trúc tiêu đề cấp trang trên `/profile` | Toàn bộ phân hệ `Web Admin` tại cổng `5174` (M4) |
| `Header/Navbar` cho các liên kết Auth (`/login`, `/register`, `/profile`), lời chào `Chào, <tên>`, nút `Đăng xuất`, highlight route M1 | Breadcrumb của các trang `Giỏ hàng`, `Thanh toán`, `Chi tiết sản phẩm` (M2, M3) |


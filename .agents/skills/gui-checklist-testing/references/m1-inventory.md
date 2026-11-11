# M1 inventory - control từng màn hình

Khung điền ở Bước 0. Dữ liệu dưới đây ghi lại **control nào tồn tại** (loại, nhãn, `type`, file:dòng) từ `eshop-sut/frontend-web/src`. Đây chỉ là danh mục để biết cần kiểm gì. **Không dùng nó làm Expected** (quy tắc 2). SV phải đối chiếu từng dòng với giao diện thật trên trình duyệt và sửa nếu khác.

Cập nhật commit SUT: ghi `git rev-parse --short HEAD` của `eshop-sut` (hoặc commit gốc của repo) vào `meta.sut_version`.

## Register - `/register` (`pages/Register.jsx`)

| Control | Loại / thuộc tính | Nhãn / văn bản | Dòng |
|---|---|---|---|
| Tiêu đề trang | `h2` | "Đăng Ký Tài Khoản" | 32 |
| Vùng báo lỗi | `div` đỏ, render trước `form` | nội dung lỗi (state `error`) | 33 |
| Họ Tên | `input type=text`, `required` | "Họ Tên" | 36-43 |
| Email | `input type=text`, `required` | "Email" | 46-53 |
| Mật khẩu | `input type=password`, `required` | "Mật khẩu" | 56-63 |
| Gợi ý mật khẩu | `p` | "Yêu cầu: Tối thiểu 8 ký tự, ..." | 64-66 |
| Nút gửi | `button type=submit` | "Đăng Ký" | 70-75 |
| Link sang Login | `Link` | "Đăng nhập" | 78 |
| Kiểm tra mật khẩu phía client | regex | thông báo "Mật khẩu quá yếu!..." | 15-20 |

Không thấy trường "Xác nhận mật khẩu" trong mã. SV xác nhận trên giao diện.

## Login - `/login` (`pages/Login.jsx`)

| Control | Loại / thuộc tính | Nhãn / văn bản | Dòng |
|---|---|---|---|
| Tiêu đề trang | `h2` | (đọc nguyên văn trên giao diện) | 24 |
| Ô tài khoản | `input type=text`, `required` | "Username" | 27-36 |
| Ô mật khẩu | `input type=text`, `required` | "Mật khẩu" | 37-46 |
| Link quên mật khẩu | `a href="/forgot-password"` | "Quên mật khẩu?" | 49-51 |
| Nút gửi | `button type=submit`, `tabIndex={1}` | "Sign In" | 53-59 |
| Link sang Register | `Link` | "Đăng ký ngay" | 61-63 |
| Vùng báo lỗi | `div` đỏ, render sau `form` | "Đăng nhập thất bại. Vui lòng kiểm tra lại." | 66 |

## ForgotPassword - `/forgot-password` (`pages/ForgotPassword.jsx`)

| Control | Loại / thuộc tính | Nhãn / văn bản | Dòng |
|---|---|---|---|
| Tiêu đề trang | `h2` | "Quên Mật Khẩu" | 43 |
| Bước 1: Email | `input type=text`, `required` | "Nhập Email của bạn" | 46-56 |
| Bước 1: nút | `button type=submit` | "Lấy mã OTP" | 57-59 |
| Bước 2: khối thông báo OTP | `div` xanh | "Mã OTP của bạn là: ..." | 65-67 |
| Bước 2: OTP | `input type=text`, `required` | "Mã OTP (4 số)" | 68-77 |
| Bước 2: mật khẩu mới | `input type=password`, `required` | "Mật khẩu mới" | 78-87 |
| Bước 2: nút gửi | `button type=submit` | "Đặt lại mật khẩu" | 90-92 |
| Bước 2: nút quay lại | `button type=button` (`setStep(1)`) | "← Quay lại" | 93-95 |
| Lỗi / thành công | `alert()` | nhiều thông báo | 20, 28, 34, 37 |

Không thấy chỉ báo bước, nút "Quay lại đăng nhập", hay trường "Xác nhận mật khẩu mới" trong mã. SV xác nhận trên giao diện.

## Profile - `/profile` (`pages/Profile.jsx`)

| Control | Loại / thuộc tính | Nhãn / văn bản | Dòng |
|---|---|---|---|
| Tiêu đề khối hồ sơ | `h2` | "Hồ sơ của bạn" | 113 |
| Tiêu đề khối đơn hàng | `h2` | "Lịch sử đơn hàng" | 167 |
| Email | `input type=text`, `disabled` | "Email (Không đổi)" | 115-125 |
| Họ Tên | `input type=text`, `required` | "Họ Tên" | 126-135 |
| Số điện thoại | `input type=text`, `placeholder="VD: 0912345678"` | "Số điện thoại" | 136-145 |
| Địa chỉ giao hàng | `textarea` | "Địa chỉ giao hàng" | 146-156 |
| Nút cập nhật | `button type=submit` | "Cập nhật" | 157-162 |
| Kiểm tra SĐT phía client | regex | alert "Số điện thoại không hợp lệ..." | 43-46 |
| Phản hồi | `alert()` | "Cập nhật thành công!", "Lỗi cập nhật" | 60, 62 |

Phần "Lịch sử đơn hàng" thuộc phạm vi M3. M1 chỉ kiểm khối hồ sơ và tiêu đề trang.

## Header / Navbar - toàn cục (`App.jsx`)

| Control | Loại / thuộc tính | Nhãn / văn bản | Dòng |
|---|---|---|---|
| Logo | `Link` | "EShop" | 21 |
| Link giỏ hàng | `Link` | "Giỏ hàng" | 23 |
| Lời chào (đã đăng nhập) | `Link` chứa `span` dùng `dangerouslySetInnerHTML` | "Chào, <tên>" | 26-28 |
| Nút thoát | `button` | "Thoát" | 29 |
| Link đăng nhập / đăng ký (khách) | `Link` | "Đăng nhập", "Đăng ký" | 33-34 |

## Màn hình ngoài phạm vi (không kiểm trong Task 1 của M1)

Home, ProductDetail (M2); Cart, Checkout, Order history (M3); Admin (M4); Mobile (M5). Login chỉ dùng để thiết lập trạng thái đã đăng nhập khi cần.


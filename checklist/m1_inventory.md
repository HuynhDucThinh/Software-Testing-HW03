# M1 Inventory - Danh mục control theo từng màn hình

Tài liệu khảo sát Bước 0 cho phạm vi **M1 (Authentication & Profile - Web)**.
Dữ liệu dưới đây ghi lại **control nào đang tồn tại thực tế trong mã nguồn** (`eshop-sut/frontend-web/src` và thông báo trả về từ `eshop-sut/backend/server.js`) để xác định danh mục đối tượng cần kiểm thử.

> Quy tắc bắt buộc (Quy tắc 2): Danh mục này **không phải là Expected**. Expected chỉ được lấy từ đặc tả `eshop-sut/README.md` (xem `checklist/m1_test_basis.md`), checklist theo loại control, hoặc heuristic chuẩn. Sinh viên cần mở trình duyệt (`http://localhost:5173`) đối chiếu từng dòng dưới đây với giao diện thực tế và hiệu chỉnh nếu có khác biệt.

- **Phiên bản SUT khảo sát:** `eshop-sut @ 1a9304a` (repo HEAD `368cd04`)
- **Trạng thái đối chiếu giao diện thật:** Đã xác nhận trực tiếp trên trình duyệt (`http://localhost:5173`, backend `http://localhost:3000`) ngày `2026-11-11` bởi SV Huỳnh Đức Thịnh (`23120199`).
- **Frontend Web URL:** `http://localhost:5173`
- **Backend API URL:** `http://localhost:3000`
- **Tài khoản seed sẵn (`eshop-sut/README.md:23-24`):**
  - User: `test@eshop.com` / `Test1234!`
  - Admin: `admin@eshop.com` / `Admin123!`

---

## 1. Màn hình chính: Register - `/register` (`eshop-sut/frontend-web/src/pages/Register.jsx`)

| STT | Control / Thành phần | Thẻ HTML & Thuộc tính chính | Nhãn / Văn bản hiển thị | Hành vi / Thông báo trong mã | Vị trí mã nguồn |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Khung chứa form | `div` (`max-w-md mx-auto mt-10 bg-white p-8 border rounded shadow-sm`) | - | Khung căn giữa trang | `Register.jsx:31` |
| 2 | Tiêu đề trang | `h2` (`text-2xl font-bold mb-6 text-center`) | `"Đăng Ký Tài Khoản"` | Không có thẻ `h1` trên trang | `Register.jsx:32` |
| 3 | Vùng thông báo lỗi | `div` (`bg-red-100 text-red-700 p-3 mb-4 rounded`) | Nội dung biến `error` | Render phía **trên** thẻ `form` khi `error` khác rỗng | `Register.jsx:33` |
| 4 | Nhãn Họ Tên | `label` (`block text-gray-700 mb-2`) | `"Họ Tên"` | Không có dấu `*` báo trường bắt buộc | `Register.jsx:36` |
| 5 | Ô nhập Họ Tên | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Ràng buộc HTML5 `required` | `Register.jsx:37-43` |
| 6 | Nhãn Email | `label` (`block text-gray-700 mb-2`) | `"Email"` | Không có dấu `*` báo trường bắt buộc | `Register.jsx:46` |
| 7 | Ô nhập Email | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Dùng `type="text"`, không validate HTML5 email | `Register.jsx:47-53` |
| 8 | Nhãn Mật khẩu | `label` (`block text-gray-700 mb-2`) | `"Mật khẩu"` | Không có dấu `*` báo trường bắt buộc | `Register.jsx:56` |
| 9 | Ô nhập Mật khẩu | `input` (`type="password"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Ẩn ký tự nhập; kiểm tra bằng regex khi submit | `Register.jsx:57-63` |
| 10 | Dòng gợi ý mật khẩu | `p` (`text-xs text-gray-400 mt-1`) | `"Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt."` | Hiển thị tĩnh ngay dưới ô Mật khẩu | `Register.jsx:64-66` |
| 11 | Nút gửi form | `button` (`type="submit"`, `w-full bg-red-500 text-white py-2 rounded hover:bg-red-600`) | `"Đăng Ký"` | Nút nền màu đỏ (`bg-red-500`) | `Register.jsx:70-75` |
| 12 | Khối chuyển trang Login | `div` chứa văn bản + `Link to="/login"` (`text-blue-600 hover:underline`) | `"Đã có tài khoản? "` + `"Đăng nhập"` | Điều hướng sang `/login` | `Register.jsx:77-79` |
| 13 | Logic kiểm tra mật khẩu client | Regex `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/` | `"Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."` | Gán vào state `error` nếu không khớp regex | `Register.jsx:15-20` |
| 14 | Phản hồi API `/api/register` | `axios.post('http://localhost:3000/api/register')` | Thành công: `navigate('/login')`; Lỗi: `err.response?.data?.error \|\| 'Đăng ký thất bại.'` | Khi trùng email, SQLite trả lỗi thô `SQLITE_CONSTRAINT: UNIQUE constraint failed: users.email` | `Register.jsx:22-27`, `server.js:20-30` |

**Thành phần đặc tả nêu nhưng không có trên giao diện thực tế `/register` (đã xác nhận trên trình duyệt):**
- Trường **Xác nhận mật khẩu** (`FR-01`).

---

## 2. Màn hình bổ trợ: Login - `/login` (`eshop-sut/frontend-web/src/pages/Login.jsx`)

| STT | Control / Thành phần | Thẻ HTML & Thuộc tính chính | Nhãn / Văn bản hiển thị | Hành vi / Thông báo trong mã | Vị trí mã nguồn |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Khung chứa form | `div` (`max-w-md mx-auto mt-10 bg-white p-8 border rounded shadow-sm`) | - | Khung căn giữa trang | `Login.jsx:23` |
| 2 | Tiêu đề trang | `h2` (`text-2xl font-bold mb-6 text-center`) | `"Đăng Ký"` | Không có thẻ `h1`; văn bản đang ghi `"Đăng Ký"` | `Login.jsx:24` |
| 3 | Nhãn tài khoản | `label` (`block text-gray-700 mb-2`) | `"Username"` | Nhãn tiếng Anh, không có dấu `*` | `Login.jsx:28` |
| 4 | Ô nhập tài khoản | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Lưu vào state `email`, dùng `type="text"` | `Login.jsx:29-35` |
| 5 | Nhãn mật khẩu | `label` (`block text-gray-700 mb-2`) | `"Mật khẩu"` | Không có dấu `*` | `Login.jsx:38` |
| 6 | Ô nhập mật khẩu | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Dùng `type="text"` (hiển thị rõ mật khẩu) | `Login.jsx:39-45` |
| 7 | Liên kết quên mật khẩu | `a` (`href="/forgot-password"`, `text-blue-500 hover:underline`) | `"Quên mật khẩu?"` | Dùng thẻ `<a>` tải lại trang thay vì `Link` SPA | `Login.jsx:49-51` |
| 8 | Nút gửi form | `button` (`type="submit"`, `tabIndex={1}`, `w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700`) | `"Sign In"` | Nhãn tiếng Anh; gán cứng `tabIndex={1}` | `Login.jsx:53-59` |
| 9 | Khối chuyển trang Register | `div` chứa văn bản + `Link to="/register"` (`text-blue-600 hover:underline`) | `"Chưa có tài khoản? "` + `"Đăng ký ngay"` | Điều hướng sang `/register` | `Login.jsx:61-63` |
| 10 | Vùng thông báo lỗi | `div` (`bg-red-100 text-red-700 p-3 mt-4 rounded`) | `"Đăng nhập thất bại. Vui lòng kiểm tra lại."` | Render phía **dưới** `form` (dưới nút submit); ghi đè cả thông báo khóa tài khoản từ backend | `Login.jsx:17-19`, `Login.jsx:66`, `server.js:40-64` |

---

## 3. Màn hình bổ trợ: ForgotPassword (2 bước) - `/forgot-password` (`eshop-sut/frontend-web/src/pages/ForgotPassword.jsx`)

| STT | Control / Thành phần | Thẻ HTML & Thuộc tính chính | Nhãn / Văn bản hiển thị | Hành vi / Thông báo trong mã | Vị trí mã nguồn |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Khung chứa form | `div` (`max-w-md mx-auto mt-10 bg-white p-8 border rounded shadow-sm`) | - | Khung căn giữa trang | `ForgotPassword.jsx:42` |
| 2 | Tiêu đề trang | `h2` (`text-2xl font-bold mb-6 text-center`) | `"Quên Mật Khẩu"` | Không có thẻ `h1` trên trang | `ForgotPassword.jsx:43` |
| 3 | [Bước 1] Nhãn Email | `label` (`block text-gray-700 mb-2`) | `"Nhập Email của bạn"` | Hiển thị khi `step === 1`; không có dấu `*` | `ForgotPassword.jsx:48` |
| 4 | [Bước 1] Ô nhập Email | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Dùng `type="text"` | `ForgotPassword.jsx:49-55` |
| 5 | [Bước 1] Nút lấy OTP | `button` (`type="submit"`, `w-full bg-blue-600 text-white py-2 rounded`) | `"Lấy mã OTP"` | Gọi `POST /api/forgot-password`; lỗi bật `alert("Lỗi: " + ...)` | `ForgotPassword.jsx:16-21`, `ForgotPassword.jsx:57-59` |
| 6 | [Bước 2] Khối hiển thị OTP demo | `div` (`bg-green-100 text-green-800 p-3 rounded text-sm mb-4`) | `"Mã OTP của bạn là: <resetToken>"` | Backend sinh số ngẫu nhiên 4 chữ số (`1000..9999`) | `ForgotPassword.jsx:17`, `ForgotPassword.jsx:65-67`, `server.js:72` |
| 7 | [Bước 2] Nhãn OTP | `label` (`block text-gray-700 mb-2`) | `"Mã OTP (4 số)"` | Hiển thị khi `step === 2`; không có dấu `*` | `ForgotPassword.jsx:69` |
| 8 | [Bước 2] Ô nhập OTP | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Nhập chuỗi `resetToken`; không có `name`/`autoComplete` nên trình duyệt tự điền nhầm (autofill) email đã lưu vào ô OTP khi đi kèm ô `password` bên dưới | `ForgotPassword.jsx:70-76` |
| 9 | [Bước 2] Nhãn Mật khẩu mới | `label` (`block text-gray-700 mb-2`) | `"Mật khẩu mới"` | Không có dấu `*` | `ForgotPassword.jsx:79` |
| 10 | [Bước 2] Ô nhập Mật khẩu mới | `input` (`type="password"`, `required`, `w-full border p-2 rounded`) | Không có `placeholder` | Kiểm tra cùng regex chứa `\s` như `Register.jsx` | `ForgotPassword.jsx:26-30`, `ForgotPassword.jsx:80-86` |
| 11 | [Bước 2] Nút Đặt lại mật khẩu | `button` (`type="submit"`, `w-full bg-green-600 text-white py-2 rounded`) | `"Đặt lại mật khẩu"` | Nút nền xanh lá (`bg-green-600`) | `ForgotPassword.jsx:90-92` |
| 12 | [Bước 2] Nút Quay lại bước 1 | `button` (`type="button"`, `w-full bg-green-600 text-white py-2 rounded`) | `"← Quay lại"` | Nút nền xanh lá (`bg-green-600`), gọi `setStep(1)` | `ForgotPassword.jsx:93-95` |
| 13 | Hộp thoại thông báo (`window.alert`) | Native JS `alert()` | `"Lỗi: User not found"`, `"Mật khẩu quá yếu!..."`, `"Đổi mật khẩu thành công!"`, `"Mã OTP không đúng hoặc có lỗi xảy ra."` | Dùng `alert()` thay vì thông báo inline trên form | `ForgotPassword.jsx:20,28,34,37` |

**Thành phần đặc tả nêu nhưng không có trên giao diện thực tế `/forgot-password` (đã xác nhận trên trình duyệt):**
- Chỉ báo bước (**Step Indicator**, ví dụ `"Bước 1 / 2"`) (`FR-03`, `FR-22`).
- Nút **Quay lại đăng nhập** ở Bước 1 (`FR-03`).
- Trường **Xác nhận mật khẩu mới** ở Bước 2 (`FR-03`).

---

## 4. Màn hình bổ trợ: Profile - `/profile` (`eshop-sut/frontend-web/src/pages/Profile.jsx`)

> Lưu ý phạm vi: M1 chỉ kiểm tra trạng thái truy cập `/profile`, tiêu đề trang và **khối Hồ sơ cá nhân** (`Profile.jsx:108-164`). Khối **Lịch sử đơn hàng** (`Profile.jsx:166-214`) thuộc phạm vi của thành viên M3 (chỉ ghi nhận sự tồn tại của thẻ `<h2>` thứ hai khi đếm số lượng thẻ tiêu đề cấp trang).

| STT | Control / Thành phần | Thẻ HTML & Thuộc tính chính | Nhãn / Văn bản hiển thị | Hành vi / Thông báo trong mã | Vị trí mã nguồn |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Trạng thái chưa đăng nhập | `div` (`text-center mt-10`) | `"Vui lòng đăng nhập"` | Render khi `user` là `null` | `Profile.jsx:108` |
| 2 | Bố cục 2 cột khi đã đăng nhập | `div` (`flex flex-col md:flex-row gap-8`) | - | Cột trái `md:w-1/3` (Hồ sơ), cột phải `md:w-2/3` (Đơn hàng) | `Profile.jsx:111-112, 166` |
| 3 | Tiêu đề khối hồ sơ | `h2` (`text-2xl font-bold mb-4`) | `"Hồ sơ của bạn"` | Không có thẻ `h1` trên trang (trang có 2 thẻ `h2`) | `Profile.jsx:113, 167` |
| 4 | Nhãn Email | `label` (`block text-gray-700 mb-1`) | `"Email (Không đổi)"` | Trường chỉ đọc | `Profile.jsx:116-118` |
| 5 | Ô hiển thị Email | `input` (`type="text"`, `disabled`, `w-full border p-2 rounded bg-gray-100`) | Giá trị `user.email` | Vô hiệu hóa chỉnh sửa (`disabled`) | `Profile.jsx:119-124` |
| 6 | Nhãn Họ Tên | `label` (`block text-gray-700 mb-1`) | `"Họ Tên"` | Không có dấu `*` dù input có `required` | `Profile.jsx:127` |
| 7 | Ô nhập Họ Tên | `input` (`type="text"`, `required`, `w-full border p-2 rounded`) | Giá trị `name` | Bắt buộc nhập (`required`) | `Profile.jsx:128-134` |
| 8 | Nhãn Số điện thoại | `label` (`block text-gray-700 mb-1`) | `"Số điện thoại"` | Không có `required` | `Profile.jsx:137` |
| 9 | Ô nhập Số điện thoại | `input` (`type="text"`, `placeholder="VD: 0912345678"`, `w-full border p-2 rounded`) | Placeholder `"VD: 0912345678"` | Kiểm tra regex `/^[1-9][0-9]{8,9}$/` khi submit (kể cả khi để trống) | `Profile.jsx:43-46`, `Profile.jsx:138-144` |
| 10 | Nhãn Địa chỉ giao hàng | `label` (`block text-gray-700 mb-1`) | `"Địa chỉ giao hàng"` | Không có `required` | `Profile.jsx:147-149` |
| 11 | Ô nhập Địa chỉ giao hàng | `textarea` (`placeholder="Nhập địa chỉ của bạn"`, `w-full border p-2 rounded h-24`) | Placeholder `"Nhập địa chỉ của bạn"` | Cho phép nhập nhiều dòng | `Profile.jsx:150-155` |
| 12 | Nút Cập nhật | `button` (`type="submit"`, `w-full bg-blue-600 text-white py-2 rounded`) | `"Cập nhật"` | Nút nền xanh dương (`bg-blue-600`) | `Profile.jsx:157-162` |
| 13 | Hộp thoại thông báo (`window.alert`) | Native JS `alert()` | `"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."`, `"Cập nhật thành công!"`, `"Lỗi cập nhật"` | Dùng `alert()` thay vì thông báo inline trên form; `AuthContext.user` không tự cập nhật tên mới nếu chưa đăng nhập lại/reload | `Profile.jsx:44, 60, 62` |

---

## 5. Thành phần toàn cục: Header / Navbar & Footer (`eshop-sut/frontend-web/src/App.jsx`)

| STT | Control / Thành phần | Thẻ HTML & Thuộc tính chính | Nhãn / Văn bản hiển thị | Hành vi / Thông báo trong mã | Vị trí mã nguồn |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Thanh Header | `header` (`bg-blue-600 text-white p-4 flex justify-between items-center`) | - | Hiển thị cố định đầu trang trên mọi route | `App.jsx:20` |
| 2 | Logo thương hiệu | `Link` (`to="/"`, `text-2xl font-bold`) | `"EShop"` | Điều hướng về trang chủ `/` | `App.jsx:21` |
| 3 | Thanh điều hướng (`nav`) | `nav` (`flex gap-4 items-center`) | - | Không dùng `NavLink`, không có class highlight trang đang chọn | `App.jsx:22-37` |
| 4 | Liên kết Giỏ hàng | `Link` (`to="/cart"`, `hover:underline`) | `"Giỏ hàng"` | Biến `cart` đã lấy ở dòng 17 nhưng không render badge số lượng | `App.jsx:17, 23` |
| 5 | Liên kết Hồ sơ / Lời chào (khi đã đăng nhập) | `Link` (`to="/profile"`, `hover:underline text-yellow-300`) bọc `span` có `dangerouslySetInnerHTML` | `` `Chào, ${user.name}` `` | Render trực tiếp chuỗi HTML từ `user.name` không escape | `App.jsx:26-28` |
| 6 | Nút đăng xuất (khi đã đăng nhập) | `button` (`onClick={logout}`, `bg-red-500 px-3 py-1 rounded`) | `"Thoát"` | Nhãn đang là `"Thoát"` thay vì `"Đăng xuất"` | `App.jsx:29` |
| 7 | Liên kết Đăng nhập (khi chưa đăng nhập) | `Link` (`to="/login"`, `hover:underline`) | `"Đăng nhập"` | Điều hướng sang `/login` | `App.jsx:33` |
| 8 | Liên kết Đăng ký (khi chưa đăng nhập) | `Link` (`to="/register"`, `hover:underline`) | `"Đăng ký"` | Điều hướng sang `/register` | `App.jsx:34` |
| 9 | Chân trang (Footer) | `footer` (`bg-gray-800 text-white text-center p-4 mt-8`) | `"© 2026 EShop SUT. Dành cho mục đích kiểm thử."` | Hiển thị cuối mọi trang | `App.jsx:61-63` |

---

## 6. Màn hình ngoài phạm vi Task 1 của M1

- `Home` (`/`), `ProductDetail` (`/product/:id`): thuộc phạm vi M2.
- `Cart` (`/cart`), `Checkout` (`/checkout`), phần bảng `Lịch sử đơn hàng` trong `/profile`: thuộc phạm vi M3.
- `frontend-admin` (`http://localhost:5174`): thuộc phạm vi M4.
- `frontend-mobile` (React Native / Expo): thuộc phạm vi M5 (trừ trường hợp sinh viên chọn Mobile làm nền tảng thứ 3 cho Task 3 Cross-Platform trên đúng các màn hình Auth & Profile của M1).


# M1 test basis - điều khoản đặc tả UI

Nguồn: `eshop-sut/README.md` (SRS v2.0). Số dòng tính theo file hiện tại. SV kiểm lại số dòng nếu README đổi. Đặc tả là **oracle** của Expected (quy tắc 2).

## Điều khoản nghiệp vụ liên quan M1

| Mã | Dòng | Nội dung (trích) |
|---|---|---|
| FR-01 | 30-36 | Cung cấp Họ Tên, Email, Mật khẩu. Email đúng định dạng và duy nhất. Mật khẩu tối thiểu 8 ký tự, có chữ hoa, chữ thường, chữ số, ký tự đặc biệt (`@ $ ! % * ? &`). Có trường **Xác nhận mật khẩu**, từ chối nếu không khớp. Đăng ký xong chuyển tới Đăng nhập. |
| FR-02 | 38-44 | Nhập Email và Mật khẩu. Sai từ 3 lần liên tiếp thì khóa tạm 30 giây, thông báo phù hợp, không lộ nguyên nhân. Trường email dùng `type="email"`. |
| FR-03 | 46-60 | Bước 1: nhập email, sinh OTP 6 chữ số, **chỉ báo bước** (vd "Bước 1 / 2"), có nút **Quay lại đăng nhập**. Bước 2: OTP, mật khẩu mới, **xác nhận mật khẩu mới**; mật khẩu mới theo FR-01; hai trường khớp nhau. |
| FR-04 | 62-67 | Cập nhật Họ Tên, Số điện thoại, Địa chỉ. SĐT hợp lệ bắt đầu bằng `0`, 10 đến 11 chữ số. Email không đổi được qua giao diện. Không tự đổi `role`. |

## Điều khoản giao diện (nguồn chính của Task 1)

| Mã | Dòng | Nội dung (trích) | IA |
|---|---|---|---|
| FR-21 | 242-248 | Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ chuẩn). Nút tích cực (Submit, Mua hàng) màu xanh dương; nút nguy hiểm/hủy màu đỏ. Tiền dùng `₫` có phân cách hàng nghìn. Mỗi trang có **đúng 1** `<h1>` mô tả nội dung trang. Thứ tự Tab từ trên xuống dưới, trái sang phải. | IA-01 |
| FR-22 | 250-256 | Trường bắt buộc có ký hiệu `*` bên cạnh nhãn. Email dùng `type="email"`. Mật khẩu dùng `type="password"`. Thông báo lỗi xuất hiện **trên** nút submit, không phải bên dưới. Form từ 2 bước trở lên có Step Indicator rõ ràng. | IA-02 |
| FR-23 | 258-263 | Navbar highlight trang đang chọn. Link Giỏ hàng có badge số lượng. Nút đăng xuất có nhãn "Đăng xuất" (không phải "Thoát"). Breadcrumb ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm). | IA-03 |
| FR-24 | 265-270 | Phản hồi trực quan sau "Thêm vào giỏ". Xác nhận khi xóa khỏi giỏ. Empty State có icon và message thân thiện. Ảnh sản phẩm có `alt` mô tả. | IA-04 |

Với M1: FR-23 áp dụng cho Navbar (nhãn đăng xuất, highlight); breadcrumb, badge giỏ, thêm giỏ, xóa khỏi giỏ, alt ảnh thuộc màn hình của thành viên khác nên không đưa vào phạm vi M1 (ghi giả định phạm vi `GAx` nếu cần).

## Điều khoản bảo mật liên quan hiển thị an toàn

| Mã | Dòng | Nội dung |
|---|---|---|
| SEC-04 | 281 | Dữ liệu người dùng khi hiển thị phải được escape, không dùng `innerHTML` trực tiếp. |
| SEC-06 | 283 | API cập nhật hồ sơ không cho đổi `role` từ client. |
| SEC-07 | 284 | OTP đặt lại mật khẩu tối thiểu 6 chữ số, có thời hạn, vô hiệu sau khi dùng. |

Chỉ dùng SEC-04 cho item về cách giao diện hiển thị tên người dùng ở Header. Các mục bảo mật API không thuộc Task 1 (GUI).

## Giả định mẫu (ghi vào `assumptions` khi cần)

- `GA1`: Đặc tả chỉ định "tiếng Việt nhất quán" nhưng cho phép thuật ngữ kỹ thuật chuẩn; item kiểm nhãn "Username", "Sign In" lấy ngưỡng "nhãn không phải tiếng Việt thông dụng".
- `GA2`: Đặc tả không quy định định dạng chỉ báo bước; chấp nhận mọi dạng thể hiện rõ "bước hiện tại / tổng số bước".
- `GA3`: Đặc tả không quy định thời gian phản hồi; dùng ngưỡng của slide: phản hồi thị giác trong 0,1 đến 1 giây.
- `NA1`: Nền tảng điện thoại cảm ứng (Android Chrome, Expo Go) không có bàn phím vật lý; item về thứ tự phím Tab ghi N/A cho nền tảng này.

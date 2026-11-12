# Biên Bản Tinh Chỉnh Công Cụ Sau Phiên Chạy Thử Pilot (`S00`) — Bộ Công Cụ & Kịch Bản Điều Phối

- **Phiên Pilot thực hiện:** `S00` (`P00` — nhóm `non-IT`, ngày `2026-11-12`, thời gian hoàn thành `01:02`, `SEQ = 5/7`, `SUS = 47.5/100`, hoàn thành có cứu hộ kỹ thuật ở 2 lỗi chặn `BUG-01` và `BUG-05`).
- **Bản đóng băng trước Pilot:** `usability/frozen/T2_participant_kit_step1_20261112-113805.md` & `usability/frozen/T2_moderator_script_step1_20261112-113805.md`
- **Bản chính thức sau Pilot:** `usability/participant_kit.md`, `usability/moderator_script.md`, `usability/session_helper.html`

## 1. Đối Chiếu Thay Đổi Trên Phiếu Người Tham Gia (`participant_kit.md`)

| Mã thay đổi | Loại | Dòng cũ | Dòng mới | Nội dung trước Pilot | Nội dung sau Pilot | Lý do tinh chỉnh từ quan sát thực tế tại `S00` |
| :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| `C01` | Hiệu chỉnh | 25–25 | 25–25 | *(Lưu ý: Bạn có thể tự chọn tên gọi, đặt một địa chỉ email đuôi `@eshop.com`, tự đặt mật khẩu cá nhân, số điện thoại di động quen thuộc và một địa chỉ nhận hàng bất kỳ...)* | *(Lưu ý bảo mật thông tin cá nhân trên video quay màn hình: Vui lòng **không nhập họ tên hay số điện thoại thật của bạn** lên trang web; thay vào đó hãy dùng bộ dữ liệu giả lập mẫu gồm Họ tên `Trần Minh Khôi`, email `khoitran@eshop.com`, số điện thoại 10 chữ số mẫu `0912 345 678` và địa chỉ mẫu `123 Nguyễn Văn Cừ, Quận 5, TP.HCM`...)* | Trong phiên `S00`, cụm từ *"số điện thoại di động quen thuộc"* khiến người tham gia `P00` gõ họ tên và số điện thoại cá nhân thật lên biểu mẫu đang quay màn hình. Cung cấp sẵn bộ thông tin giả lập 10 chữ số đầu `0` vừa bảo vệ tuyệt đối PII trên video của 7 phiên `S01..S07`, vừa giữ nguyên tính chân thực khi chạm lỗi regex `BUG-05`. |

## 2. Tinh Chỉnh Quy Trình Điều Phối & Công Cụ Ghi Nhận (`moderator_script.md` & `session_helper.html`)

| Mã thay đổi | Tệp cập nhật | Vấn đề bộc lộ qua phiên Pilot `S00` | Biện pháp tinh chỉnh áp dụng cho 7 phiên chính thức `S01..S07` |
| :---: | :--- | :--- | :--- |
| `M01` | `usability/moderator_script.md` (Mục 1 — Bước 4 & 5) | Ở phiên `S00`, điều phối viên bật `Win + Alt + R` hơi trễ (từ đầu màn hình `/login` ở giây `00:25`, video thu được `41 giây` chặng `Login -> Profile`), làm thiếu hình ảnh trực quan của chặng 1 (`/register`). | Đưa thao tác nhấn **`Win + Alt + R` ngay tại Trang chủ `http://localhost:5173/` trước khi giao chuột cho người tham gia** thành mục kiểm tra bắt buộc trước khi bấm đồng hồ `00:00`, đồng thời bổ sung bước nhắc miệng không gõ SĐT thật lên web. |
| `M02` | `usability/session_helper.html` (Tab 1 & Tab 2) | Khi tốc ký nhanh các nhận xét của `P00` bằng ô nhập tay, điều phối viên chưa kịp đổi ô chọn `Màn hình` (mặc định đang ở `Register`) và `Loại sự kiện` (mặc định `E`), đồng thời phát hiện nhận xét phổ biến về việc chuyển từ Đăng ký sang Đăng nhập không báo thành công / không giữ sẵn email. | Đóng khung vàng bộ dữ liệu giả lập ngay trên Tab 1 và bổ sung nút bấm nhanh 1-click `+ Q: ĐK xong không báo / không giữ email` gắn sẵn đúng màn hình `Login` & loại `Q` trên Tab 2. |

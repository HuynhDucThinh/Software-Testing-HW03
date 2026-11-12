# Kịch Bản Điều Phối Viên & Phiếu Quan Sát Hiện Trường (Moderator Script & Observation Sheet)

Tài liệu nội bộ dành riêng cho người điều phối (`Moderator`) — **không phát tờ này cho người tham gia**.

---

## 1. Danh sách kiểm tra bắt buộc trước mỗi phiên (`Clean State Checklist`)

- [ ] **Bước 1:** Dừng tiến trình Backend cũ (nếu đang chạy), chạy `node database.js` và `node server.js` tại `eshop-sut/backend` để đưa toàn bộ bảng `users` về đúng trạng thái gốc ban đầu.
- [ ] **Bước 2:** Đảm bảo Web Frontend đang chạy tại `http://localhost:5173`.
- [ ] **Bước 3:** Mở cửa sổ trình duyệt mới sạch dữ liệu (`Incognito / Private` hoặc chạy `localStorage.clear()`), đặt sẵn tại trang xuất phát `http://localhost:5173`.
- [ ] **Bước 4:** Bật sẵn phần mềm quay màn hình & kiểm tra micro thu âm (chỉ bấm `Record` sau khi người tham gia xác nhận đồng ý).
- [ ] **Bước 5:** Chuẩn bị đồng hồ bấm giờ (`00:00` tính từ lúc người tham gia đọc xong nhiệm vụ và bắt đầu chạm chuột/bàn phím).

---

## 2. Quy tắc giữ thái độ trung lập & Câu nhắc chuẩn

- **Không bao giờ** chỉ tay lên màn hình, không đọc tên nút bấm, không gật/lắc đầu khi người tham gia hỏi *"Bấm vào đây đúng không?"*.
- **Các câu phản hồi trung lập duy nhất được phép dùng:**
  - Khi người tham gia im lặng quá 15 giây: *"Bạn đang nghĩ gì hoặc đang tìm thông tin gì trên màn hình lúc này vậy?"*
  - Khi người tham gia hỏi cách làm: *"Theo bạn, ở tình huống thực tế bình thường bạn sẽ thử làm gì tiếp theo?"*
  - Khi người tham gia tự trách mình làm sai: *"Không sao đâu bạn, mục tiêu hôm nay là tìm ra chỗ phần mềm thiết kế chưa rõ cho người dùng mà."*

---

## 3. Giao thức Cứu hộ khi gặp Lỗi Chặn Kỹ thuật của SUT (`System-Bug Rescue Protocol`)

Áp dụng thống nhất để vừa thu thập đầy đủ bằng chứng lỗi nghiêm trọng, vừa không làm đứt gãy hoàn toàn các màn hình kế tiếp của luồng:

| Điểm chặn tiềm ẩn trên SUT | Điều kiện bắt buộc trước khi can thiệp | Lời thoại cứu hộ chuẩn hóa (cấp gợi ý tối thiểu) | Cách ghi nhận vào JSON |
| :--- | :--- | :--- | :--- |
| `<Mô tả điểm chặn kỹ thuật #1 nếu có>` | Người tham gia đã tự thử `>= 3 lần` dữ liệu hợp lệ bị từ chối VÀ bị kẹt quá `90 giây` (hoặc xin bỏ cuộc) | *"Ở ô này hệ thống hiện đang có một lỗi kiểm tra dữ liệu nội bộ. Để bạn đi tiếp trải nghiệm phần sau, bạn thử nhập theo mẫu `<giá_trị_mẫu>` này nhé."* | Ghi vào `events` (`type: "E"`, `is_bug: true`), ghi vào `assists`, và đặt `completion_status = "co_tro_giup"` |
| `<Mô tả điểm chặn kỹ thuật #2 nếu có>` | Người tham gia đã tự thử `>= 3 lần` dữ liệu hợp lệ bị từ chối VÀ bị kẹt quá `90 giây` (hoặc xin bỏ cuộc) | *"Trường này hệ thống đang bị lỗi định dạng kiểm tra. Bạn thử nhập `<giá_trị_mẫu>` để xem hệ thống phản hồi tiếp thế nào nhé."* | Ghi vào `events` (`type: "E"`, `is_bug: true`), ghi vào `assists`, và đặt `completion_status = "co_tro_giup"` |

---

## 4. Bảng ghi chép nhanh tại hiện trường (Chuyển nguyên văn vào `sessions/S0x.json`)

- **Mã phiên:** `S0_` · **Mã người tham gia:** `P0_` · **Nhóm:** `non-IT / IT` · **Nền tảng:** `______`
- **Mốc thời gian chuyển chặng (`mm:ss`):** Chặng 1: `____` · Chặng 2: `____` · Chặng 3: `____` · **Kết thúc (`total_duration`):** `____`
- **Kết quả hoàn thành:** `[ ] khong_tro_giup` · `[ ] co_tro_giup` · `[ ] khong_hoan_thanh`

| Mốc `mm:ss` | Màn hình | Loại (`E` Lỗi / `H` Do dự / `Q` Câu nói / `A` Trợ giúp) | Ghi chép hành vi & lời nói nguyên văn của người tham gia | Lỗi SUT? (`BUG-xx` / Mới) |
| :---: | :--- | :---: | :--- | :---: |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |

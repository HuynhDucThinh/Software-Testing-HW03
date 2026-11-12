# Kịch Bản Điều Phối Viên & Phiếu Quan Sát Hiện Trường — Luồng `F1`

> **Tài liệu nội bộ dành riêng cho Người điều phối (`Huỳnh Đức Thịnh — 23120199`)** — Tuyệt đối **không** mở tài liệu này cho người tham gia xem trước hoặc trong lúc thực hiện nhiệm vụ.

---

## 1. Danh sách kiểm tra bắt buộc trước MỖI phiên (`Clean State Checklist` — 30 giây)

Thực hiện đầy đủ cho phiên chạy thử Pilot (`S00`) và từng phiên chính thức (`S01` .. `S07`):

- [ ] **Bước 1 (Làm sạch CSDL & Mở trạm thử nghiệm 1-click):** Mở PowerShell tại thư mục gốc dự án và chạy:
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\usability\start_session.ps1 -Session S0x
  ```
  *(Script tự động dừng Backend cũ, xóa `database.sqlite`, chạy lại `node database.js` + `node server.js`, đảm bảo Frontend `:5173` sẵn sàng, mở trang điều phối `usability/session_helper.html?session=S0x` cho bạn và mở sẵn **1 cửa sổ Chrome Ẩn danh mới tinh** tại `http://localhost:5173/` cho người tham gia).*
- [ ] **Bước 2:** Sắp xếp cửa sổ `session_helper.html` sang màn hình phụ hoặc thu gọn (chỉ mở lại phần khảo sát khi người tham gia làm xong nhiệm vụ); để cửa sổ Chrome Ẩn danh `http://localhost:5173/` phóng toàn màn hình.
- [ ] **Bước 3:** Tắt thông báo Zalo / Messenger trên máy tính để không làm gián đoạn phiên thử nghiệm.
- [ ] **Bước 4:** Chuẩn bị tổ hợp phím **Xbox Game Bar (`Win + Alt + R`)** để quay riêng cửa sổ Chrome (tắt Webcam; bật/tắt Micro bằng `Win + Alt + M` đúng theo lựa chọn đồng ý của người tham gia).

---

## 2. Kịch bản lời thoại điều phối từng phút (~12–15 phút/phiên)

### Giai đoạn A — Mở đầu & Xin xác nhận đồng ý (`2 phút`)
1. **Đón tiếp & Trấn an tâm lý:**
   > *"Cảm ơn anh/chị/cô/chú/bạn đã giúp mình buổi thử nghiệm hôm nay. Mình đang làm bài tập đánh giá xem trang web bán hàng EShop này thiết kế dễ hay khó dùng đối với người mới — tức là mình **kiểm tra trang web chứ hoàn toàn không kiểm tra kỹ năng của bạn**. Chỗ nào bạn thấy rối hay bị báo lỗi chính là chỗ quý giá để mình phát hiện điểm yếu của phần mềm."*
2. **Hướng dẫn nói to suy nghĩ (`Concurrent Think-Aloud`):**
   > *"Trong lúc cầm chuột thao tác, bạn giúp mình **nghĩ gì trong đầu thì nói thành tiếng ra ngoài** nhé: ví dụ bạn đang tìm mục nào, nhìn chữ trên màn hình thấy gì lạ, hoặc sao bấm mà chưa được. Mình sẽ ngồi cạnh ghi chép và xin phép không chỉ cách làm trong lúc bạn thực hiện."*
3. **Xin đồng ý quay cửa sổ trình duyệt & Xác minh trợ giảng:**
   > *"Mình xin phép quay lại riêng cửa sổ trang web (không quay camera mặt) để đối chiếu thời gian làm bài, và xin lưu Họ tên + SĐT đã che số giữa để nếu trợ giảng môn học kiểm tra ngẫu nhiên thì xác nhận bạn có tham gia thật. Bạn có đồng ý quay màn hình và có đồng ý thu âm giọng nói không?"*
   - Tích ngay 3 ô `Consent` tương ứng trên `session_helper.html`.
   - Nếu đồng ý quay màn hình: nhấp chuột vào cửa sổ Chrome Ẩn danh `http://localhost:5173/`, bấm **`Win + Alt + R`** (kiểm tra trạng thái Micro khớp với đồng ý ghi âm).

### Giai đoạn B — Giao nhiệm vụ & Quan sát trung lập (`4–8 phút`, tối đa `10 phút`)
1. Đưa Mục 2 của `participant_kit.md` cho người tham gia đọc kỹ (chỉ giải thích lại mục tiêu nếu họ hỏi, **tuyệt đối không dùng các từ**: *bấm nút Đăng ký, nhập Username, bấm vào chữ Chào trên góc phải, vào /profile*).
2. Ngay khi người tham gia đặt tay lên chuột bắt đầu tìm kiếm trên trang chủ `http://localhost:5173/`, bấm nút **`Bắt đầu (00:00)`** trên `session_helper.html`.
3. **Các câu nhắc trung lập duy nhất được phép dùng trong phiên:**
   - Khi người tham gia im lặng quá `15–20 giây`: *"Lúc này bạn đang tìm gì hoặc đang phân vân điều gì trên màn hình vậy?"*
   - Khi người tham gia hỏi *"Bấm nút này phải không?"* / *"Nhập gì vào đây?"*: *"Nếu đang ở nhà tự dùng trang web này một mình thì bạn sẽ thử làm thế nào?"*
   - Khi vừa qua từng chặng, bấm nút mốc tương ứng trên `session_helper.html`:
     - `m1_register_done`: Ngay khi đăng ký xong và chuyển sang màn hình đăng nhập.
     - `m2_login_done`: Ngay khi đăng nhập thành công và vào giao diện đã đăng nhập.
     - `m3_profile_opened`: Ngay khi bấm vào lời chào `Chào, <Tên>` mở ra trang thông tin cá nhân.
     - `m4_profile_saved`: Ngay khi lưu thông tin cá nhân thành công (cũng là lúc dừng đồng hồ).

---

## 3. Giao thức Cứu hộ khi gặp Lỗi Chặn Kỹ thuật của SUT (`System-Bug Rescue Protocol`)

Áp dụng **nhất quán như nhau cho mọi phiên** để vừa thu được trọn vẹn bằng chứng bức xúc/thử sai thực tế, vừa giúp người tham gia không bị kẹt chết ở chặng đầu mà bỏ lỡ các màn hình phía sau:

| Điểm chặn mã nguồn trên luồng `F1` | Hiện tượng người tham gia sẽ gặp | Ngưỡng bắt buộc chờ TRƯỚC khi cứu hộ | Lời thoại cứu hộ chuẩn hóa (cấp gợi ý tối thiểu) | Thao tác ghi nhận bắt buộc |
| :--- | :--- | :--- | :--- | :--- |
| **Điểm A — Mật khẩu tại `/register`** (`BUG-01`, `Register.jsx:15`) | Dòng chữ nhỏ bảo cần *chữ hoa, thường, số và ký tự đặc biệt*, nhưng regex thực tế lại **cấm `@ $ ! % * ? &` và bắt buộc phải có dấu cách (`\s`)** -> báo đỏ *"Mật khẩu quá yếu!..."* liên tục | Người tham gia đã tự sửa & bấm gửi thất bại **`>= 3 lần`** HOẶC bị kẹt tại ô mật khẩu **`>= 90 giây`** (hoặc tự xin bỏ cuộc) | *"Ở ô mật khẩu này bộ lọc của trang web hiện đang có một lỗi lập trình nội bộ là bắt buộc có dấu cách và không nhận ký tự đặc biệt. Để bạn đi tiếp sang phần sau, bạn thử đặt mật khẩu dạng `Matkhau 123` (có 1 dấu cách ở giữa) nhé."* | 1. Đã ghi các lần lỗi `E` (`is_bug: true`, `BUG-01`)<br>2. Bấm nút **`+ Cứu hộ A (BUG-01)`** -> tự động thêm vào `assists` và chuyển `completion_status` sang **`co_tro_giup`** |
| **Điểm B — Số điện thoại tại `/profile`** (`BUG-05`, `Profile.jsx:43`) | Placeholder gợi ý `VD: 0912345678`, nhưng regex `/^[1-9][0-9]{8,9}$/` **từ chối mọi SĐT bắt đầu bằng số `0`**, bật hộp thoại `alert()` báo lỗi | Người tham gia đã nhập SĐT hợp lệ đầu `0` bị `alert()` từ chối **`>= 3 lần`** HOẶC kẹt **`>= 90 giây`** | *"Ô số điện thoại này trang web đang có lỗi kỹ thuật từ chối chữ số 0 ở đầu. Để hoàn tất lưu thông tin, bạn thử bỏ số 0 đầu tiên đi (ví dụ nhập 9 chữ số từ số thứ hai như `912345678`) xem sao nhé."* | 1. Đã ghi các lần lỗi `E` (`is_bug: true`, `BUG-05`)<br>2. Bấm nút **`+ Cứu hộ A (BUG-05)`** -> ghi vào `assists` và đặt `completion_status = "co_tro_giup"` |
| **Rủi ro phụ C — Khóa ngầm tại `/login`** (`BUG-03`, `server.js:54`) | Gõ sai mật khẩu vừa tạo `2 lần` làm `login_attempts` nhảy lên `4` -> khóa ngầm `3 phút` nhưng UI chỉ báo chung *"Đăng nhập thất bại"* | Chỉ khi bạn thấy rõ họ đã gõ lại đúng mật khẩu vừa đăng ký nhưng vẫn bị từ chối liên tiếp do dính khóa `3 phút` | *"Hệ thống vừa tạm khóa tài khoản 3 phút do 2 lần gõ nhầm trước đó mà không hiện thông báo khóa. Bạn có thể tạo nhanh một email mới hoặc chờ hết khóa nhé."* | Ghi sự kiện `E` (`BUG-03`) và nếu hỗ trợ mở khóa/tạo lại thì ghi vào `assists` (`co_tro_giup`) |

> **Lưu ý quan trọng các điểm KHÔNG ĐƯỢC cứu hộ sớm (vì người dùng có thể tự vượt qua):**
> - Tiêu đề trang `/login` ghi nhầm chữ **"Đăng Ký"** (`BUG-07`), nhãn **"Username"** (`BUG-11`), ô mật khẩu `/login` **hiện rõ chữ thường** (`BUG-08`), hay việc tìm đường vào Hồ sơ qua chữ vàng **`Chào, <Tên>`** trên thanh Header (`App.jsx:26`): để người tham gia tự tìm tòi (chỉ can thiệp gợi ý vùng thanh trên cùng nếu sau `90 giây` họ hoàn toàn bế tắc không tìm thấy lối vào trang cá nhân, và vẫn phải tính là `co_tro_giup`).

---

## 4. Đóng phiên, Thu phiếu `SUS` & Lưu trữ (`3–4 phút`)

1. Ngay khi người tham gia lưu xong thông tin cá nhân (hoặc hết `10:00`), bấm **`Dừng kết thúc`** trên đồng hồ và nhấn **`Win + Alt + R`** tắt quay màn hình.
2. Trên `session_helper.html`, chuyển sang thẻ **`Chế độ Người tham gia điền phiếu`** và mời người tham gia tự chọn:
   - Điểm **`SEQ` (`1–7`)**,
   - Đủ **10 câu `SUS` (`1–5`)**,
   - Và cùng trao đổi / nhập câu trả lời cho **4 câu hỏi mở** (`Clarity`, `Error recovery`, `Speed`, `Trust`).
3. Bấm nút **`Tải xuống S0x.json`** -> lưu tệp vào `usability/sessions/S0x.json`.
4. Vào thư mục `C:\Users\DUC THINH\Videos\Captures\`, đổi tên video vừa quay thành `S0x.mp4` và cất vào thư mục lưu trữ riêng ngoài Git (cập nhật tham chiếu trong `usability/recordings/LINKS.md`).
5. Cập nhật dòng thông tin của `P0x` vào `usability/participants.md` (**bắt buộc che 4 chữ số giữa của SĐT/Zalo**, ví dụ `090****123`, trước khi lưu vào repo!).

---

## 5. Khung bảng ghi chép giấy dự phòng (Dùng nếu muốn tốc ký tay song song)

- **Mã phiên:** `S0_` · **Mã người TG:** `P0_` · **Nhóm:** `non-IT / IT` · **Reset DB sạch:** `[ ] Có`
- **Mốc chặng (`mm:ss`):** `m1_register`: `____` · `m2_login`: `____` · `m3_open_profile`: `____` · `m4_saved / Tổng`: `____`
- **Trạng thái hoàn thành:** `[ ] khong_tro_giup` · `[ ] co_tro_giup` · `[ ] khong_hoan_thanh`

| Mốc `mm:ss` | Màn hình (`Home` / `Register` / `Login` / `Header` / `Profile`) | Loại (`E` / `H` / `Q` / `A`) | Hành vi quan sát & Câu nói `Think-Aloud` nguyên văn | Mã Bug liên quan (`BUG-xx` / Mới) |
| :---: | :--- | :---: | :--- | :---: |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |
| `  :  ` | | | | |

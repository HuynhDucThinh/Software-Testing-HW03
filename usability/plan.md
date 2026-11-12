# Kế Hoạch Đánh Giá Khả Năng Sử Dụng (Usability Evaluation Plan) — Luồng `F1`

| Hạng mục | Nội dung chi tiết |
| :--- | :--- |
| **Hệ thống kiểm thử (SUT)** | EShop — Ứng dụng thương mại điện tử tiếng Việt (`./eshop-sut` @ `1a9304a`, giữ nguyên mã nguồn gốc) |
| **Phân công phạm vi nhóm** | Thành viên **M1** (Authentication & Personal Profile — Web) · Luồng đầu-cuối không trùng lặp **`F1`** |
| **Luồng nghiệp vụ mục tiêu (`F1`)** | Đăng ký tài khoản mới -> Đăng nhập hệ thống -> Cập nhật thông tin hồ sơ cá nhân (`FR-01`, `FR-02`, `FR-04`) |
| **Người điều phối (Moderator)** | Huỳnh Đức Thịnh — MSSV: `23120199` (`23120199@student.hcmus.edu.vn`) |
| **Hình thức thực hiện** | Điều phối trực tiếp tại chỗ (`In-person Moderated Usability Testing`) trên máy tính của điều phối viên |
| **Quy mô mẫu khảo sát** | **1 phiên chạy thử Pilot (`S00` — `P00`)** + **7 phiên chính thức (`S01..S07` — `P01..P07`)** ngoài lớp học |

---

## 1. Mục đích đánh giá (Purpose)

Đợt đánh giá khả năng sử dụng có điều phối này nhằm đo lường mức độ dễ hiểu, hiệu quả thao tác, khả năng tự chẩn đoán — phục hồi sau lỗi và mức độ tin cậy cảm nhận của **người dùng thật phổ thông** trong lần đầu tiên tiếp cận hệ thống EShop để hoàn tất chu trình khởi tạo và thiết lập thông tin tài khoản cá nhân (luồng `F1`: từ lúc chưa có tài khoản đến khi đăng ký thành công, đăng nhập và lưu đầy đủ họ tên, số điện thoại liên lạc, địa chỉ nhận hàng mặc định).

Khác với kiểm thử danh mục giao diện ở Task 1 vốn đối chiếu từng thuộc tính DOM/CSS tĩnh với đặc tả, đợt đánh giá Task 2 tập trung phát hiện các điểm đứt gãy trong mô hình tư duy người dùng (`User Mental Model`), định lượng mức độ cản trở thực tế của các lỗi logic/biểu mẫu đối với tiến trình hoàn thành nhiệm vụ, và cung cấp cơ sở thực nghiệm để phân tách rõ **lỗi cài đặt phần mềm đơn lẻ (`Isolated Bugs`)** với **vấn đề thiết kế hệ thống (`Systemic Design Issues`)**, từ đó xếp hạng ưu tiên cải tiến trải nghiệm đăng ký và quản lý hồ sơ trên EShop.

## 2. Câu hỏi nghiên cứu cụ thể (Problem Statement & Research Questions)

Nghiên cứu được thiết kế nhằm trả lời 5 câu hỏi định lượng và định tính cụ thể sau:

- **RQ1 — Khả năng hoàn thành & Tác động của lỗi chặn biểu mẫu:** Có bao nhiêu trên 7 người tham gia chính thức tự hoàn thành trọn vẹn luồng `F1`, và bao nhiêu người bị chặn đứng bắt buộc phải kích hoạt cơ chế cứu hộ tại khâu đặt mật khẩu đăng ký (`FR-01`) hoặc khâu nhập số điện thoại hồ sơ (`FR-04`)?
- **RQ2 — Khả năng định vị điều hướng (`Navigation Discoverability`):** Khi bắt đầu từ trang chủ chưa đăng nhập và sau khi đăng nhập quay về trang chủ, người dùng mất bao lâu để nhận ra lối vào phần tạo tài khoản mới và đặc biệt là lối vào trang quản lý thông tin cá nhân (khi thanh điều hướng trên cùng chỉ hiển thị lời chào tên người dùng mà không có nhãn menu *"Hồ sơ"* hay *"Tài khoản"*)?
- **RQ3 — Nhận thức trạng thái & Sự bối rối khi chuyển trang:** Việc hệ thống chuyển trang tức thời sau khi tạo tài khoản mà không có thông báo xác nhận, cộng với tiêu đề trang đăng nhập hiển thị sai ngữ cảnh và nhãn trường pha trộn tiếng Anh, gây ra bao nhiêu lần ngập ngừng hoặc thao tác nhầm cho người dùng lần đầu?
- **RQ4 — Khả năng tự phục hồi sau thông báo lỗi (`Error Recovery`):** Khi hệ thống từ chối dữ liệu đầu vào bằng cảnh báo nội dòng hoặc hộp thoại trình duyệt (`alert`), nội dung thông báo có giúp người dùng hiểu đúng nguyên nhân để tự điều chỉnh hay dẫn họ vào vòng lặp thử sai thất bại?
- **RQ5 — Cảm nhận chủ quan về Độ dễ, Tốc độ và Độ tin cậy (`SEQ`, `SUS` & `Trust`):** Điểm độ dễ `SEQ` (`1–7`) và điểm khả năng sử dụng chuẩn **`SUS` (`0–100`)** trung bình của luồng `F1` đạt mức nào so với mốc chuẩn lịch sử `68.0`, đồng thời các khiếm khuyết hiển thị (như lộ ký tự mật khẩu khi đăng nhập hoặc thông tin quay về giá trị cũ khi tải lại trang) ảnh hưởng ra sao đến lòng tin bảo mật của người dùng?

## 3. Mục tiêu kiểm thử & Thiết kế nhiệm vụ (Test Objectives & Task Design)

- **Trạng thái khởi đầu (`Initial State`):** Cơ sở dữ liệu SQLite của EShop vừa được khởi tạo lại về trạng thái gốc sạch (`Clean State`), trình duyệt mở cửa sổ ẩn danh mới tại trang chủ `http://localhost:5173/` ở trạng thái **chưa đăng nhập**.
- **Kịch bản nhiệm vụ định hướng mục tiêu (`Goal-oriented Task Scenario` — giao nguyên văn cho người tham gia):**
  > Bạn vừa biết đến cửa hàng trực tuyến EShop và muốn tạo một tài khoản cá nhân mới để chuẩn bị mua sắm. Sau khi tạo tài khoản xong, bạn hãy truy cập vào tài khoản vừa tạo của mình trên trang web và bổ sung đầy đủ họ tên, số điện thoại liên lạc cùng địa chỉ nhận hàng mặc định để sẵn sàng cho các lần đặt hàng sau.
- **Quy tắc dữ liệu đầu vào:** Người tham gia tự do sử dụng tên gọi, địa chỉ email kiểm thử (ví dụ `nguoimua@eshop.com`), mật khẩu cá nhân tự đặt, số điện thoại di động quen thuộc và một địa chỉ nhận hàng giả định tại Việt Nam — điều phối viên tuyệt đối không áp đặt sẵn mật khẩu hay định dạng số điện thoại lách lỗi trước khi bắt đầu.
- **Các mốc chặng đo thời gian (`Task Milestones`):**
  1. `m1_register_done`: Hoàn tất gửi biểu mẫu tạo tài khoản mới thành công.
  2. `m2_login_done`: Xác thực đăng nhập thành công vào hệ thống và chuyển vào giao diện đã đăng nhập.
  3. `m3_profile_opened`: Định vị và mở được trang quản lý thông tin cá nhân từ thanh điều hướng.
  4. `m4_profile_saved`: Lưu thành công thông tin Họ tên, Số điện thoại và Địa chỉ nhận hàng mặc định.
- **Tiêu chí hoàn thành thành công (`Success Criteria`):** Tài khoản mới được ghi nhận trong hệ thống, người tham gia đăng nhập hợp lệ vào đúng tài khoản đó và nhận được xác nhận cập nhật thành công bộ ba thông tin (Họ tên, Số điện thoại, Địa chỉ nhận hàng) trên trang thông tin cá nhân.
- **Mốc thời gian kỳ vọng (`Benchmark Time`):** **`05:00`** (`300 giây`) cho toàn bộ 3 chặng đối với người dùng lần đầu; ngưỡng thời gian tối đa cho phần thao tác nhiệm vụ là **`10:00`** (`600 giây`) trước khi kết thúc phiên để chuyển sang phần khảo sát.

## 4. Hồ sơ người tham gia mục tiêu (User Profile & Recruitment Criteria)

- **Quy mô mẫu bắt buộc:** Tổng cộng **8 người thật độc lập** (không trùng lặp giữa phiên chạy thử và phiên chính thức):
  - **1 người tham gia phiên chạy thử Pilot (`P00` — phiên `S00`):** Dùng để kiểm tra độ dễ hiểu của câu chữ kịch bản, kiểm chứng quy trình bấm giờ — quay màn hình và chốt ngưỡng cứu hộ; dữ liệu của `S00` được báo cáo riêng, **không gộp vào thống kê của 7 phiên chính thức**.
  - **7 người tham gia chính thức (`P01` .. `P07` — phiên `S01` .. `S07`):** Mỗi người thực hiện 1 phiên độc lập.
- **Tiêu chí tuyển chọn (`Inclusion & Exclusion Criteria`):**
  - **Bắt buộc 100% là người ngoài lớp học Kiểm thử phần mềm HW03** (người thân, bạn bè khác ngành/khác khóa).
  - Đã từng sử dụng trình duyệt web hoặc mua sắm trực tuyến cơ bản nhưng **chưa từng tiếp xúc với hệ thống EShop** và không ngồi xem trước phiên thử nghiệm của người khác.
  - **Ưu tiên nhóm người dùng phổ thông không chuyên CNTT / không làm kiểm thử phần mềm (`non-IT`)** (mục tiêu tối thiểu `>= 5/7` người thuộc nhóm `non-IT`, đa dạng độ tuổi sinh viên, nhân viên văn phòng, kinh doanh/nội trợ) để thu nhận phản ứng tự nhiên nhất.
- **Xác thực chống gian lận & Bảo mật thông tin cá nhân (`Anti-AI-Cheat & PII Masking`):**
  - Sinh viên thu thập Họ tên và số điện thoại / Zalo thật có sự đồng ý trước của cả 8 người để sẵn sàng xác nhận nếu trợ giảng gọi điện kiểm tra ngẫu nhiên (giả mạo người tham gia sẽ nhận `0 điểm` Task 2).
  - Trong tệp công khai `usability/participants.md` và báo cáo nộp bài, toàn bộ số điện thoại / Zalo bắt buộc **che đúng 4 chữ số ở giữa** theo định dạng chuẩn `09x****xxx` (ví dụ: `090****123`); trong các tệp dữ liệu phiên `usability/sessions/S0x.json` chỉ lưu mã ẩn danh (`P00`, `P01..P07`), tuyệt đối không lưu SĐT hay email thật.

## 5. Phương pháp & Thiết kế phiên thử nghiệm (Method & Test Design)

- **Phương pháp điều phối:** Kiểm thử khả dụng có điều phối trực tiếp tại chỗ (**In-person Moderated Usability Testing**) kết hợp kỹ thuật **nói to suy nghĩ đồng thời (`Concurrent Think-Aloud`)**. Mỗi phiên diễn ra riêng biệt 1-kèm-1 ngay tại máy tính của điều phối viên để loại bỏ hoàn toàn biến nhiễu do độ trễ mạng từ xa hoặc khác biệt cấu hình thiết bị.
- **Cấu trúc chuẩn của 1 phiên thử nghiệm (~12–15 phút/người):**
  1. **Mở đầu & Thiết lập tâm lý (`2 phút`):** Giải thích rõ mục tiêu buổi thử nghiệm là kiểm tra chất lượng trang web chứ không đánh giá kỹ năng người dùng; hướng dẫn cách nói to suy nghĩ (`Think-Aloud`); xin xác nhận đồng ý quay màn hình cửa sổ trình duyệt và đồng ý để trợ giảng liên hệ xác minh; bật quay cửa sổ trình duyệt.
  2. **Thực hiện kịch bản nhiệm vụ luồng `F1` (`4–8 phút`, tối đa `10 phút`):** Giao phiếu nhiệm vụ, bấm đồng hồ `00:00`, quan sát trung lập và ghi nhận theo thời gian thực các mốc hoàn thành chặng (`m1..m4`), lỗi thao tác (`E`), điểm ngập ngừng `>= 5 giây` (`H`), phát ngôn nguyên văn (`Q`) và sự kiện cứu hộ kỹ thuật (`A`).
  3. **Chấm thang đo định lượng sau nhiệm vụ (`2 phút`):** Ngay khi dừng đồng hồ và tắt quay màn hình, người tham gia tự đánh giá độ dễ tổng thể qua câu hỏi **Single Ease Question (`SEQ`, thang `1–7`)** và hoàn thành bảng **10 câu chuẩn `SUS` (thang Likert `1–5`)** trên biểu mẫu thu phiếu tại chỗ (kiểm tra bắt buộc không bỏ trống câu nào).
  4. **Phỏng vấn sâu bằng 4 câu hỏi mở (`2–3 phút`):** Trao đổi ngắn gọn theo 4 chiều bắt buộc — **Độ rõ ràng (`Clarity`)**, **Khả năng phục hồi sau lỗi (`Error recovery`)**, **Tốc độ thao tác (`Speed`)**, và **Độ tin cậy (`Trust`)** — kết hợp hỏi làm rõ các thời điểm người tham gia khựng lại trong phiên.
- **Quy trình chạy thử Pilot (`S00`) & Tinh chỉnh:** Thực hiện trọn vẹn quy trình trên với `P00` trước tiên; mọi chỉnh sửa về diễn đạt kịch bản hoặc phiếu khảo sát sau `S00` đều được trích xuất tự động bằng `pilot_diff.py` vào `usability/pilot_refinements.md` kèm lý do thực tế trước khi khóa bộ công cụ cho `S01..S07`.

## 6. Môi trường, Thiết bị & Khởi tạo trạng thái sạch (Environment & Clean State)

- **Cấu hình trạm thử nghiệm cố định:**
  - **Thiết bị & Hệ điều hành:** Máy tính cá nhân chạy Windows 11 Build 26300, độ phân giải màn hình `1920x1080`, chuột và bàn phím vật lý tiêu chuẩn.
  - **Trình duyệt thực thi:** Google Chrome `157.0.8103.x` (64-bit) mở ở chế độ **Cửa sổ Ẩn danh mới (`Incognito`)** nhằm loại bỏ hoàn toàn lịch sử tự động điền (`Autofill`), trình quản lý mật khẩu lưu sẵn và bộ nhớ đệm cũ.
  - **Hệ thống SUT:** Giữ nguyên **100% mã nguồn gốc** tại `./eshop-sut` (không tạo nhánh sửa mã nguồn); Backend Express + SQLite chạy tại `http://localhost:3000` và Frontend React/Vite chạy tại `http://localhost:5173`.
- **Quy trình khởi tạo trạng thái sạch bắt buộc trước MỖI phiên (`Clean State Protocol`):**
  1. Dừng tiến trình Backend hiện tại, xóa tệp `eshop-sut/backend/database.sqlite`, chạy lại `node database.js` và `node server.js` để đưa bảng `users` về đúng trạng thái hạt giống ban đầu (tránh xung đột email hoặc bộ đếm khóa tài khoản từ phiên trước).
  2. Đóng toàn bộ cửa sổ ẩn danh cũ, mở cửa sổ Chrome ẩn danh mới truy cập sẵn `http://localhost:5173/` và kiểm tra `localStorage` rỗng trước khi mời người tham gia ngồi vào máy.
  3. Xác nhận cờ `"clean_state_reset": true` trong tệp JSON của từng phiên (`S00..S07`).
- **Công cụ ghi nhận bằng chứng:**
  - **Quay video màn hình cửa sổ trình duyệt:** Sử dụng công cụ tích hợp **Xbox Game Bar (`Win + Alt + R`)** trên Windows 11 chỉ quay riêng cửa sổ trình duyệt EShop (**không bật Webcam quay mặt**; bật hoặc tắt thu âm Micro tùy sự đồng ý của từng người tham gia). Tệp video `S00.mp4..S07.mp4` được lưu trữ ngoài Git repository công khai (đặt trong thư mục lưu trữ bảo mật phục vụ chấm bài trên Moodle và đối chiếu vấn đáp, dẫn chiếu qua `usability/recordings/LINKS.md`).
  - **Công cụ bấm giờ & thu phiếu tại chỗ (`session_helper.html`):** Ghi dấu thời gian thực `mm:ss` cho từng chặng và sự kiện, kiểm tra đủ 10 câu `SUS` và xuất trực tiếp tệp cấu trúc chuẩn `usability/sessions/S0x.json`.

## 7. Vai trò người điều phối & Quy tắc can thiệp (Test-Monitor Role & Rescue Protocol)

- **Nguyên tắc quan sát trung lập:**
  - Điều phối viên ngồi lệch phía sau/bên cạnh để quan sát màn hình mà không gây áp lực tâm lý; tuyệt đối không chỉ tay lên màn hình, không gợi ý vị trí nút bấm, không giải thích thuật ngữ tiếng Anh hay thông báo lỗi thay cho hệ thống.
  - Khi người tham gia im lặng quá `20 giây` hoặc quay sang hỏi *"Bấm chỗ nào?"*, chỉ sử dụng các câu nhắc trung lập: *"Bạn cứ thử làm giống như khi đang ở nhà một mình nhé"*, *"Lúc này bạn đang tìm thông tin gì trên màn hình?"*, hoặc *"Theo bạn thông báo đó đang muốn nói điều gì?"*.
- **Giao thức cứu hộ minh bạch khi gặp lỗi chặn kỹ thuật của SUT (`System-Bug Rescue Protocol`):**
  Qua khảo sát mã nguồn thực tế ở Task 1, luồng `F1` tồn tại **2 lỗi mã nguồn mức chặn luồng** và **1 rủi ro khóa tài khoản sớm** có khả năng làm người dùng thật bị kẹt vĩnh viễn nếu không có quy tắc xử lý thống nhất:
  1. **Điểm chặn A tại trang tạo tài khoản (`BUG-01` — `Register.jsx:15`):** Giao diện hướng dẫn mật khẩu cần chữ hoa, chữ thường, số và ký tự đặc biệt, nhưng biểu thức chính quy thực tế lại **bắt buộc có khoảng trắng (`\s`) và từ chối mọi ký tự đặc biệt (`@ $ ! % * ? &`)**.
  2. **Điểm chặn B tại trang thông tin cá nhân (`BUG-05` — `Profile.jsx:43`):** Ô số điện thoại hiển thị gợi ý `VD: 0912345678`, nhưng mã kiểm tra lại **từ chối mọi chuỗi bắt đầu bằng chữ số `0`**.
  3. **Rủi ro phụ C tại trang đăng nhập (`BUG-03` — `server.js:54-57`):** Gõ sai mật khẩu chỉ `2 lần` sẽ làm bộ đếm tăng `+4 >= 3` và khóa tài khoản ngầm trong `3 phút` mà giao diện không báo rõ trạng thái khóa.

  **Quy tắc 3 bước bắt buộc khi kích hoạt cứu hộ:**
  - **Bước 1 — Chờ tự xoay xở để thu bằng chứng thật:** Điều phối viên bắt buộc giữ im lặng quan sát tối thiểu **`90 giây` liên tục tại điểm kẹt HOẶC tối thiểu `>= 3 lần` người tham gia tự sửa và gửi biểu mẫu hợp lệ nhưng vẫn bị từ chối** (ghi nhận đầy đủ số lần lỗi `E`, thời gian bối rối và câu nói bức xúc).
  - **Bước 2 — Cấp dữ liệu mẫu vượt chốt tối thiểu:** Chỉ khi đã đủ ngưỡng trên (hoặc khi người tham gia tuyên bố bỏ cuộc), điều phối viên thông báo trung lập: *"Chỗ này bộ lọc hiện tại của trang web đang có một lỗi kỹ thuật nội bộ. Để bạn có thể tiếp tục trải nghiệm nốt phần còn lại, bạn thử nhập định dạng mẫu này nhé"* (cấp mật khẩu có khoảng trắng như `Matkhau 123` cho Điểm A; gợi ý lược bỏ chữ số `0` đầu tiên như `901234567` cho Điểm B; hoặc thông báo chờ mở khóa/tạo lại nếu dính Điểm C).
  - **Bước 3 — Ghi nhận minh bạch trạng thái cứu hộ:** Mọi phiên có sử dụng gợi ý vượt chốt đều bắt buộc ghi bản ghi chi tiết vào mảng `assists` + sự kiện loại `A` theo đúng mốc `mm:ss`, và **bắt buộc xếp loại trạng thái hoàn thành của phiên là `co_tro_giup` (`Completed with Rescue Assist`)**, tuyệt đối không tính vào tỷ lệ hoàn thành độc lập `khong_tro_giup`.

## 8. Chỉ số đo lường & Dữ liệu thu thập (Evaluation Measures & Instruments)

| Nhóm đo lường | Chỉ số cụ thể (Metric) | Đơn vị / Thang đo | Nguồn & Công cụ xử lý |
| :--- | :--- | :--- | :--- |
| **Hiệu năng khách quan (`Performance`)** | **Tỷ lệ hoàn thành nhiệm vụ (`Completion Rate`)** tách rõ 3 mức: Hoàn thành độc lập (`khong_tro_giup`), Hoàn thành có cứu hộ lỗi chặn (`co_tro_giup`), Không hoàn thành (`khong_hoan_thanh`) | Tỷ lệ `x/7` (`%`) | `S01..S07.json` -> `analyze_usability.py` |
| **Hiệu năng khách quan (`Performance`)** | **Thời gian thực hiện (`Time on Task`)** theo từng chặng (`m1..m4`) và tổng thời gian toàn luồng (`Mean ± SD`, `Median`, `Min–Max`, tỷ lệ đạt mốc Benchmark tối đa `05:00`) | `mm:ss` (giây) | Đồng hồ bấm giờ phiên -> `analyze_usability.py` |
| **Hiệu năng khách quan (`Performance`)** | **Mật độ ma sát tương tác:** Số lỗi thao tác/bị từ chối (`E`), số lần ngập ngừng từ `5 giây` trở lên (`H`), và số lần điều phối viên cứu hộ (`A`) trung bình mỗi phiên | Số lần / phiên | Nhật ký sự kiện `events` & `assists` |
| **Cảm nhận định lượng (`Preference`)** | **Độ dễ sau nhiệm vụ (`Single Ease Question — SEQ`)** đánh giá ngay khi kết thúc thao tác | Số nguyên `1` (Rất khó) .. `7` (Rất dễ) | `participant_kit.md` -> `S01..S07.json` |
| **Cảm nhận định lượng (`Preference`)** | **Thang đo chuẩn `System Usability Scale (SUS — Brooke, 1996)`** gồm 10 câu phát biểu xen kẽ tích cực (câu lẻ `1,3,5,7,9` tính `x - 1`) và tiêu cực (câu chẵn `2,4,6,8,10` tính `5 - x`), nhân hệ số `2.5` | Thang `0.0 .. 100.0` (`Mean ± SD`, `Median`, hạng chữ Sauro–Lewis `A+..F` & mức chấp nhận Bangor so với mốc `68.0`) | `participant_kit.md` -> `analyze_usability.py` |
| **Định tính chiều sâu (`Qualitative`)** | **Phát ngôn `Think-Aloud` nguyên văn** trong lúc làm và câu trả lời cho **4 câu hỏi phỏng vấn mở**: `Clarity` (Độ rõ ràng), `Error recovery` (Phục hồi lỗi), `Speed` (Tốc độ), `Trust` (Độ tin cậy) | Trích dẫn nguyên văn theo mã `P01..P07` | `events` (`type: "Q"`) & `open_probes` |

## 9. Cấu trúc nội dung báo cáo (Report Contents & Deliverables)

Toàn bộ kết quả thực hiện Task 2 sẽ được đóng gói thành bộ hiện vật hoàn chỉnh và đồng bộ trực tiếp vào Mục 5 & Mục 8 của `Main_Report.md`:

1. **Hồ sơ kế hoạch & công cụ chuẩn bị (`usability/`):** Kế hoạch 9 phần `plan.md`, phiếu hướng dẫn & thang đo `participant_kit.md`, kịch bản điều phối `moderator_script.md`, công cụ hỗ trợ chạy phiên `start_session.ps1` / `session_helper.html` và thư mục đóng băng bản nháp AI `usability/frozen/` kèm mã băm `SHA-256`.
2. **Danh sách người tham gia xác thực (`usability/participants.md`):** Bảng thông tin 1 người chạy thử Pilot (`P00`) và 7 người tham gia chính thức ngoài lớp học (`P01..P07`) có SĐT/Zalo che đúng 4 chữ số giữa (`09x****xxx`) và xác nhận đồng ý kiểm chứng.
3. **Biên bản chạy thử Pilot & Tinh chỉnh (`usability/sessions/S00.json`, `usability/pilot_refinements.md`):** Kết quả phiên `S00` tách riêng và bảng đối chiếu các điều chỉnh trước khi tiến hành 7 phiên chính thức.
4. **Dữ liệu gốc 7 phiên chính thức & Bằng chứng quay màn hình (`usability/sessions/S01.json..S07.json`, `usability/recordings/LINKS.md`):** Từng phiên có lịch sử Git commit độc lập theo đúng Mục 12 của đề bài.
5. **Báo cáo tính toán thống kê `SUS` & Hiệu năng (`usability/sus_and_metrics_summary.md`):** Bảng kết quả từng phiên, ma trận điểm gốc và điểm quy đổi chi tiết từng câu `Q1..Q10` của cả 7 người tham gia, các chỉ số `Mean ± SD`, `Median`, `Min–Max`, đối chiếu chuẩn `68.0` và danh mục sự kiện lỗi trích xuất tự động.
6. **Phân tích tổng hợp & Xếp hạng mức độ nghiêm trọng (`usability/findings.md` & `Main_Report.md` §5.8–§5.9):** Gom nhóm các điểm nghẽn trải nghiệm, phân tách rạch ròi giữa **Lỗi phần mềm đơn lẻ (`Isolated Bugs`)** (ánh xạ đầy đủ sang hệ thống GitHub Issues `#1..#27` hoặc lập thêm Issue mới kèm ảnh nếu phát sinh lỗi mới) và **Vấn đề thiết kế hệ thống (`Systemic Design Issues`)**, xếp hạng theo 4 mức `Severity` (`Critical`, `Major`, `Minor`, `Cosmetic`) kèm đề xuất cải tiến cụ thể và thảo luận giới hạn của nghiên cứu.

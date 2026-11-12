# Phương Pháp Luận Lập Kế Hoạch & Điều Phối Kiểm Thử Khả Dụng (Evaluation Methodology)

Tài liệu tham chiếu nền tảng cho Bước 0, Bước 1 và Bước 2 của skill `usability-evaluation`.

---

## 1. Phân định ranh giới GUI Testing, Functional Testing và Usability Evaluation

Tổng hợp từ tài liệu lý thuyết kiểm thử giao diện (Seminar GUI Testing — Slide 4, 6–8, 10, 16) và phương pháp kiểm thử khả dụng có điều phối (Rubin & Chisnell, *Handbook of Usability Testing*):

| Khía cạnh | GUI Checklist Testing (Task 1) | Functional Testing | Moderated Usability Evaluation (Task 2) |
| :--- | :--- | :--- | :--- |
| **Trọng tâm kiểm chứng** | Thuộc tính thị giác, bố cục, chuẩn điều khiển, điều hướng bàn phím, phản hồi trạng thái khớp đặc tả UI (`IA-01..04`) | Logic xử lý dữ liệu đầu vào/đầu ra, công thức tính toán, lưu trữ CSDL | Mức độ dễ hiểu, hiệu quả thao tác, khả năng tự phục hồi lỗi và cảm nhận tâm lý của **người dùng thật** trên một luồng đầu-cuối |
| **Người thực hiện** | Kiểm thử viên đối chiếu từng mục checklist với ngưỡng oracle | Kiểm thử viên hoặc kịch bản kiểm thử tự động | **7 người tham gia thật ngoài lớp học** thực hiện kịch bản mục tiêu dưới sự quan sát trung lập của điều phối viên |
| **Khả năng tự động hóa** | Tự động hóa một phần (đo DOM/CSS, kiểm tra liên kết), kết hợp mắt người | Mức độ tự động hóa cao | **Không thể tự động hóa thay con người** (Slide 16): hành vi ngập ngừng, mô hình tư duy và đánh giá chủ quan bắt buộc đến từ người thật |

---

## 2. Cấu trúc Kế hoạch Kiểm thử Khả dụng 9 phần (`plan.md`)

Kế hoạch đóng vai trò bản thiết kế nghiên cứu cố định trước khi tuyển người tham gia. Tệp `plan.md` bắt buộc có đủ 9 mục cấp hai (`## 1.` .. `## 9.`) theo đúng trình tự sau:

1. **Mục đích đánh giá (`Purpose`):** Nêu lý do thực hiện đợt đánh giá trên luồng nghiệp vụ đã chọn và các quyết định cải tiến sản phẩm sẽ dựa vào kết quả nghiên cứu.
2. **Câu hỏi nghiên cứu cụ thể (`Problem Statement & Research Questions`):** Danh sách các câu hỏi định lượng và định tính cụ thể (`RQ1..RQn`) có thể trả lời trực tiếp bằng dữ liệu quan sát phiên thử nghiệm (ví dụ: tỷ lệ người dùng tự vượt qua biểu mẫu đăng ký không cần trợ giúp, vị trí gây ngập ngừng lâu nhất, mức độ tin cậy sau khi lưu hồ sơ).
3. **Mục tiêu kiểm thử & Thiết kế nhiệm vụ (`Test Objectives & Task Design`):**
   - Phát biểu kịch bản nhiệm vụ theo **mô hình tư duy người dùng (`User Mental Model`)**, không viết theo cấu trúc mã nguồn.
   - Quy định rõ: trạng thái khởi đầu của hệ thống, dữ liệu nền cung cấp cho người tham gia (nếu cần), **tiêu chí hoàn thành nhiệm vụ đo lường được (`Success Criteria`)**, và **mốc thời gian kỳ vọng (`Benchmark Time`, ví dụ `05:00`)** kèm ngưỡng thời gian tối đa của phiên.
4. **Hồ sơ người tham gia mục tiêu (`User Profile & Recruitment Criteria`):**
   - Quy mô mẫu: **1 người chạy thử Pilot (`P00` / `S00`)** + **7 người tham gia chính thức (`P01..P07` / `S01..S07`)**.
   - Điều kiện bắt buộc: **100% người ngoài lớp học HW03**, có thông tin liên hệ xác thực (SĐT/Zalo che 4 chữ số giữa trong báo cáo), ưu tiên người dùng phổ thông không chuyên CNTT / không làm kiểm thử phần mềm để phản ánh trải nghiệm tự nhiên nhất.
5. **Phương pháp & Thiết kế phiên thử nghiệm (`Method & Test Design`):**
   - Hình thức: Kiểm thử khả dụng có điều phối (`Moderated Usability Testing` — trực tiếp trên máy điều phối hoặc từ xa đồng bộ qua chia sẻ màn hình có tương tác trực tiếp, mỗi phiên 1 người độc lập).
   - Kỹ thuật thu thập nhận thức: **Concurrent Think-Aloud** (người tham gia vừa thao tác vừa nói thành tiếng suy nghĩ, kỳ vọng và bối rối của mình).
   - Trình tự chuẩn của 1 phiên (khoảng 15–20 phút): Mở đầu & xin đồng ý (`2–3 phút`) -> Thực hiện nhiệm vụ trên SUT (`5–10 phút`) -> Chấm điểm `SEQ` & `SUS` (`2–3 phút`) -> Phỏng vấn sâu 4 câu hỏi mở (`3–4 phút`).
6. **Môi trường, Thiết bị & Khởi tạo trạng thái sạch (`Environment & Clean State`):**
   - Thông số trình duyệt, độ phân giải, URL `http://localhost:5173`, công cụ quay màn hình và thu âm (OBS Studio / Xbox Game Bar / Snipping Tool Video).
   - **Quy tắc trạng thái sạch (`Clean State`):** Trước mỗi phiên (`S00..S07`), khởi tạo lại cơ sở dữ liệu SQLite gốc và xóa sạch `localStorage`/`sessionStorage` của trình duyệt để không phiên nào bị nhiễu bởi dữ liệu của người trước, đồng thời **không chỉnh sửa mã nguồn gốc của SUT**.
7. **Vai trò người điều phối & Giao thức cứu hộ lỗi chặn (`Test-Monitor Role & Rescue Protocol`):**
   - Nguyên tắc quan sát trung lập, danh mục các câu nhắc `Think-Aloud` không gợi ý đáp án, và quy tắc xử lý minh bạch khi người tham gia chạm phải lỗi chặn kỹ thuật của SUT (xem chi tiết Mục 4 bên dưới).
8. **Chỉ số đo lường & Dữ liệu thu thập (`Evaluation Measures & Instruments`):**
   - **Nhóm chỉ số hiệu năng (`Performance Metrics`):** Tỷ lệ hoàn thành (`khong_tro_giup` / `co_tro_giup` / `khong_hoan_thanh`), thời gian hoàn thành từng chặng và toàn luồng (`mm:ss`), số lỗi thao tác (`E`), số điểm ngập ngừng `>= 5 giây` (`H`), số lần điều phối viên can thiệp (`A`).
   - **Nhóm chỉ số cảm nhận chủ quan (`Preference & Attitude Metrics`):** Điểm độ dễ sau nhiệm vụ `SEQ` (`1..7`), thang đo chuẩn 10 câu **`SUS`** (`0..100`), và 4 câu hỏi mở bắt buộc (`Clarity`, `Error recovery`, `Speed`, `Trust`).
9. **Cấu trúc nội dung báo cáo (`Report Contents & Deliverables`):**
   - Danh mục hiện vật đầu ra: bảng 7 người tham gia đã che 4 số giữa SĐT, biên bản Pilot `S00`, 7 phiếu phiên `S01..S07` kèm video minh chứng, bảng thống kê `SUS`, phân tích tách biệt `Isolated Bugs` và `Systemic Design Issues`, xếp hạng `Severity` và liên kết GitHub Issues.

---

## 3. Quy tắc viết Kịch bản Nhiệm vụ Định hướng Mục tiêu (`Goal-oriented Task Scenario`)

1. **Đặt bối cảnh thực tế đời thường:** Cho người tham gia một vai trò và mục đích tự nhiên (ví dụ: khách hàng mới muốn tạo tài khoản mua sắm cá nhân trên cửa hàng trực tuyến EShop, sau đó kiểm tra việc đăng nhập lại và bổ sung thông tin liên lạc nhận hàng vào hồ sơ).
2. **Tuyệt đối không lộ bước dẫn hay tên thành phần UI:**
   - **Cấm dùng động từ chỉ dẫn thao tác cơ học:** *bấm nút, nhấn vào, click, chọn menu, gõ vào ô, cuộn xuống, mở đường dẫn...*
   - **Cấm gọi nguyên văn nhãn nút / tên route kỹ thuật trên giao diện:** *`Đăng Ký`, `Sign In`, `Username`, `Cập nhật`, `Thoát`, `/register`, `/login`, `/profile`...*
3. **Cung cấp linh hoạt dữ liệu đầu vào:** Cho phép người tham gia tự chọn thông tin quen thuộc hoặc cung cấp một phiếu thông tin nhân vật giả định tự nhiên (như địa chỉ giao hàng mẫu, số điện thoại liên lạc mẫu đúng chuẩn Việt Nam `09...`) mà không ép cú pháp kỹ thuật như *"nhập mật khẩu có dấu cách"*.

---

## 4. Giao thức Cứu hộ Minh bạch khi gặp Lỗi Chặn Kỹ thuật (`System-Bug Rescue Protocol`)

Trong các hệ thống kiểm thử thực hành có cài sẵn khiếm khuyết nghiêm trọng (chẳng hạn biểu thức chính quy kiểm tra mật khẩu hoặc số điện thoại bị lập trình ngược với đặc tả và ngược với dòng hướng dẫn trên màn hình), nếu điều phối viên hoàn toàn im lặng đến hết giờ, người dùng sẽ kẹt vĩnh viễn ở màn hình đầu tiên và buổi thử nghiệm mất trắng dữ liệu ở các màn hình phía sau. Ngược lại, nếu gợi ý quá sớm sẽ làm sai lệch kết quả kiểm thử khả dụng.

Do đó, mọi buổi điều phối phải tuân thủ nghiêm ngặt **Giao thức 3 bước**:

1. **Giai đoạn Tự xoay xở bắt buộc (`00:00` đến tối thiểu `90 giây` tại điểm kẹt hoặc `>= 3` lần gửi biểu mẫu thất bại liên tiếp):**
   - Điều phối viên tuyệt đối giữ im lặng, chỉ ghi chép đầy đủ các chuỗi người dùng đã thử, thời gian khựng lại, biểu cảm và lời nói `Think-Aloud`, chỉ dùng câu nhắc trung tính: *"Bạn cứ thử theo cách bạn nghĩ, và nói to giúp mình điều gì trên màn hình đang làm bạn phân vân nhé."*
2. **Điều kiện kích hoạt cứu hộ (`Rescue Trigger`):**
   - Chỉ can thiệp khi người tham gia **(a)** tuyên bố bỏ cuộc, hoặc **(b)** đã thử tối thiểu 3 giá trị hợp lệ theo hiểu biết thông thường / theo hướng dẫn trên màn hình mà vẫn bị hệ thống từ chối do lỗi mã nguồn trong hơn `90 giây` khiến luồng bị chặn đứng hoàn toàn.
3. **Cách thức can thiệp & Ghi nhận trung thực:**
   - Điều phối viên thông báo ngắn gọn: *"Chỗ này hệ thống đang có một lỗi kỹ thuật nội bộ ở bộ lọc dữ liệu. Để bạn có thể tiếp tục trải nghiệm các phần còn lại của trang web, bạn thử dùng giá trị mẫu `<giá_trị_vượt_chốt>` này nhé."*
   - **Bắt buộc ghi nhận vào phiếu phiên:**
     - Tạo một bản ghi trong mảng `assists` (mốc thời gian `t`, màn hình, lý do lỗi chặn, nội dung hỗ trợ đã cung cấp).
     - Tạo sự kiện loại `E` kèm cờ `"is_bug": true` tại điểm người dùng bị chặn.
     - Chuyển trường `completion_status` của cả phiên từ `khong_tro_giup` sang **`co_tro_giup`** (không bao giờ được chấm là hoàn thành độc lập nếu đã nhận cứu hộ!).

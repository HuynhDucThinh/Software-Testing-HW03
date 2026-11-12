# Kế Hoạch Đánh Giá Khả Năng Sử Dụng (Usability Evaluation Plan) — Luồng `<FLOW_ID>`

**Hệ thống kiểm thử (SUT):** `<SUT_NAME>`  
**Luồng nghiệp vụ đầu-cuối được chọn:** `<FLOW_NAME>`  
**Người điều phối (Moderator):** `<STUDENT_NAME>` (`<STUDENT_ID>`)  
**Quy mô mẫu:** 1 phiên Pilot (`S00`) + 7 phiên chính thức (`S01..S07`)

---

## 1. Mục đích đánh giá (Purpose)

<Nêu rõ lý do tổ chức đợt đánh giá khả năng sử dụng trên luồng nghiệp vụ này và những quyết định cải tiến giao diện/sản phẩm sẽ dựa trên kết quả thu được.>

## 2. Câu hỏi nghiên cứu cụ thể (Problem Statement & Research Questions)

- **RQ1:** <Câu hỏi định lượng/định tính số 1 về tỷ lệ hoàn thành hoặc điểm nghẽn chuyển bước>
- **RQ2:** <Câu hỏi số 2 về khả năng hiểu hướng dẫn và tự phục hồi khi gặp thông báo lỗi>
- **RQ3:** <Câu hỏi số 3 về nhận thức trạng thái hệ thống và mức độ tin cậy của người dùng>
- **RQ4:** <Câu hỏi số 4 về cảm nhận tốc độ thao tác và điểm số SUS tổng thể so với mốc chuẩn 68.0>

## 3. Mục tiêu kiểm thử & Thiết kế nhiệm vụ (Test Objectives & Task Design)

- **Trạng thái khởi đầu:** Cơ sở dữ liệu ở trạng thái gốc vừa khởi tạo lại (`Clean State`), trình duyệt chưa đăng nhập, mở tại trang chủ hoặc trang bắt đầu của luồng.
- **Kịch bản nhiệm vụ định hướng mục tiêu (Goal-oriented Scenario):**
  > <Phát biểu mục tiêu bằng ngôn ngữ đời thường tự nhiên, không nêu các bước bấm, không nhắc tên nút hay đường dẫn URL.>
- **Tiêu chí hoàn thành thành công (`Success Criteria`):** <Điều kiện trạng thái cuối cùng đo lường được xác nhận người dùng đã đạt mục tiêu>.
- **Mốc thời gian kỳ vọng (`Benchmark Time`):** `<MM:SS>` (thời gian tối đa cho phép trước khi kết thúc nhiệm vụ: `<MAX_MM:SS>`).

## 4. Hồ sơ người tham gia mục tiêu (User Profile & Recruitment Criteria)

- **Số lượng:** 1 người tham gia chạy thử Pilot (`P00`) và **7 người tham gia chính thức (`P01..P07`)**.
- **Điều kiện bắt buộc:** 100% là người thật **không thuộc lớp học HW03**, có khả năng sử dụng trình duyệt web cơ bản để mua sắm trực tuyến, ưu tiên nhóm không chuyên CNTT / không làm kiểm thử phần mềm (`non-IT`).
- **Xác thực & Bảo mật:** Lưu họ tên và SĐT/Zalo có **che 4 chữ số ở giữa** (`09x****xxx`) tại `participants.md`, sẵn sàng xác nhận nếu trợ giảng liên hệ ngẫu nhiên.

## 5. Phương pháp & Thiết kế phiên thử nghiệm (Method & Test Design)

- **Phương pháp:** Kiểm thử khả dụng có điều phối (`Moderated Usability Testing`) kết hợp kỹ thuật nói to suy nghĩ đồng thời (**Concurrent Think-Aloud**), mỗi phiên thực hiện riêng rẽ từng người một.
- **Cấu trúc thời lượng 1 phiên (~15–20 phút):**
  1. Thiết lập tâm lý, hướng dẫn `Think-Aloud` & xin phép quay màn hình / ghi âm (`2–3 phút`).
  2. Thực hiện kịch bản nhiệm vụ đầu-cuối trên SUT (`5–10 phút`).
  3. Đánh giá nhanh độ dễ `SEQ` (1–7) và điền phiếu **10 câu chuẩn `SUS`** (1–5) (`2–3 phút`).
  4. Phỏng vấn sâu bằng **4 câu hỏi mở** (`Clarity`, `Error recovery`, `Speed`, `Trust`) (`3–4 phút`).
- **Phiên chạy thử (`Pilot Session — S00`):** Thực hiện trước với `P00` để rà soát độ rõ ràng của kịch bản, kiểm tra công cụ ghi hình và chốt ngưỡng can thiệp trước khi chạy 7 phiên chính thức.

## 6. Môi trường, Thiết bị & Khởi tạo trạng thái sạch (Environment & Clean State)

- **Môi trường chạy SUT:** Backend (`http://localhost:3000`) và Web Frontend (`http://localhost:5173`) giữ nguyên mã nguồn gốc không chỉnh sửa.
- **Quy trình làm sạch trước mỗi phiên (`Clean State`):** Khởi tạo lại cơ sở dữ liệu SQLite (`node database.js && node server.js`), mở cửa sổ trình duyệt ẩn danh / hồ sơ mới sạch bộ nhớ cục bộ (`localStorage.clear()`).
- **Công cụ ghi nhận bằng chứng:** Quay video màn hình kèm âm thanh (khi người tham gia đồng ý) và ghi chú có cấu trúc theo mốc thời gian `mm:ss`.

## 7. Vai trò người điều phối & Quy tắc can thiệp (Test-Monitor Role & Rescue Protocol)

- **Quan sát trung lập:** Không gợi ý vị trí nút bấm, không giải thích giao diện thay hệ thống; chỉ dùng câu nhắc trung lập khi người tham gia quên nói to suy nghĩ.
- **Giao thức cứu hộ lỗi chặn kỹ thuật (`System-Bug Rescue Protocol`):** Nếu người tham gia bị kẹt cứng tại một lỗi mã nguồn nghiêm trọng của SUT sau tối thiểu `90 giây` hoặc `>= 3 lần` nhập dữ liệu hợp lệ bị từ chối vô lý, điều phối viên ghi nhận đầy đủ lỗi chặn, cấp dữ liệu mẫu vượt chốt để người tham gia tiếp tục đánh giá các màn hình sau, và bắt buộc đánh dấu phiên là **`co_tro_giup`**.

## 8. Chỉ số đo lường & Dữ liệu thu thập (Evaluation Measures & Instruments)

- **Đo lường hiệu năng (`Performance`):** Trạng thái hoàn thành (`khong_tro_giup` / `co_tro_giup` / `khong_hoan_thanh`), thời gian hoàn thành từng chặng và tổng thời gian (`mm:ss`), số lỗi thao tác (`E`), số lần ngập ngừng `>= 5s` (`H`), số lần trợ giúp (`A`).
- **Đo lường cảm nhận (`Preference`):** Điểm `SEQ` (`1..7`), điểm **System Usability Scale (`SUS`, thang `0..100`)** gồm 10 câu Likert 1–5, và câu trả lời nguyên văn cho 4 câu hỏi mở (`Clarity`, `Error recovery`, `Speed`, `Trust`).

## 9. Cấu trúc nội dung báo cáo (Report Contents & Deliverables)

1. Mục tiêu, kịch bản nhiệm vụ định hướng mục tiêu và bộ công cụ đo lường (`SUS` + 4 Probes).
2. Bảng danh sách 7 người tham gia thật ngoài lớp học (che 4 chữ số giữa SĐT/Zalo) và tóm tắt tinh chỉnh sau phiên Pilot `S00`.
3. Bảng dữ liệu thực thi 7 phiên `S01..S07`, ma trận tính điểm `SUS` chi tiết (`Mean`, `SD`, `Median`, đối chiếu mốc `68.0` và hạng Bangor/Sauro).
4. Phân tích tổng hợp điểm nghẽn: tách biệt **Lỗi phần mềm đơn lẻ (`Isolated Bugs`)** và **Vấn đề thiết kế hệ thống (`Systemic Design Issues`)**, xếp hạng theo mức độ nghiêm trọng (`Severity`), đề xuất cải tiến và liên kết GitHub Issues kèm ảnh minh chứng.

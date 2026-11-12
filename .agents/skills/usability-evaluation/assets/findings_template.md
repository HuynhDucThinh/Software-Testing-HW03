# Báo Cáo Tổng Hợp & Phân Tích Đánh Giá Khả Năng Sử Dụng (Usability Findings) — Luồng `<FLOW_ID>`

Tài liệu phân tích Giai đoạn 3 (Bước 5 của skill `usability-evaluation`), tổng hợp trực tiếp từ dữ liệu thực nghiệm của 7 phiên chính thức (`S01..S07`) và kết quả tính toán từ `analyze_usability.py`.

---

## 1. Tổng hợp Điểm nghẽn Trải nghiệm & Phân tách Bản chất Vấn đề (`Isolated Bugs` vs `Systemic Design Issues`)

| Mã Finding | Màn hình / Chặng | Mô tả điểm nghẽn trải nghiệm | Các phiên gặp (`k / 7`) | Bằng chứng quan sát & trích dẫn `Think-Aloud` | Phân loại bản chất (`Isolated Bug` / `Systemic Design Issue`) | Severity (`Critical` / `Major` / `Minor` / `Cosmetic`) | Điểm ưu tiên (`Severity x k/7`) | Tham chiếu Bug / GitHub Issue |
| :---: | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| `UF-01` | | | | | | | | |

---

## 2. Phân tích Chuyên sâu hai Nhóm Vấn đề

### 2.1. Nhóm Lỗi phần mềm đơn lẻ (`Isolated Bugs`) phát hiện qua tương tác người dùng thật
- <Phân tích các lỗi lập trình/đặc tả cụ thể khiến người dùng thất bại hoặc mất niềm tin; đối chiếu mã `BUG-xx` / GitHub Issue `#xx` đã đăng hoặc liên kết tới Issue mới vừa tạo.>

### 2.2. Nhóm Vấn đề thiết kế hệ thống (`Systemic Design Issues`) xuyên suốt luồng nghiệp vụ
- <Phân tích các bất cập về mô hình luồng tương tác, cơ chế phản hồi không đồng nhất, thiếu phòng ngừa lỗi (`Error Prevention`) và tải nhận thức cao lặp lại qua nhiều màn hình.>

---

## 3. Xếp hạng Ưu tiên & Khuyến nghị Cải tiến Thiết kế (`Prioritised Recommendations`)

1. **Ưu tiên 1 (`Critical / Blocker`):** <Giải pháp kỹ thuật & UX cụ thể>
2. **Ưu tiên 2 (`Major`):** <Giải pháp kỹ thuật & UX cụ thể>
3. **Ưu tiên 3 (`Minor / Cosmetic`):** <Giải pháp kỹ thuật & UX cụ thể>

---

## 4. Tổng hợp Định tính từ 4 Câu hỏi Phỏng vấn Sâu (`Open-ended Probes`)

| Chiều đánh giá | Xu hướng nhận xét chính của 7 người tham gia | Phiên tiêu biểu | Trích dẫn tiêu biểu |
| :--- | :--- | :---: | :--- |
| **1. Độ rõ ràng (`Clarity`)** | | | |
| **2. Phục hồi sau lỗi (`Error recovery`)** | | | |
| **3. Tốc độ thao tác (`Speed`)** | | | |
| **4. Độ tin cậy (`Trust`)** | | | |

---

## 5. Giới hạn của Nghiên cứu (`Study Limitations`)

- <Nêu rõ giới hạn cỡ mẫu `n = 7`, môi trường kiểm thử cục bộ, ảnh hưởng của giao thức cứu hộ tại điểm lỗi chặn, v.v.>

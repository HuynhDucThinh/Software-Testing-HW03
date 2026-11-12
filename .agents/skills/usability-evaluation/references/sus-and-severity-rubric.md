# Thang Đo Chuẩn SUS, Câu Hỏi Phỏng Vấn Sâu & Khung Phân Loại Mức Độ Nghiêm Trọng

Tài liệu tham chiếu phương pháp chấm điểm và phân tích kết quả cho Bước 1, Bước 4 và Bước 5 của skill `usability-evaluation`.

---

## 1. Thang đo chuẩn System Usability Scale (`SUS` — Brooke, 1996)

### 1.1. Cấu trúc 10 câu hỏi đan xen
Thang đo `SUS` gồm đúng **10 phát biểu** chấm trên thang Likert 5 mức (`1 = Hoàn toàn không đồng ý` đến `5 = Hoàn toàn đồng ý`), xen kẽ:
- **Các câu số lẻ (`Q1, Q3, Q5, Q7, Q9`):** Mang sắc thái khẳng định tích cực về tính dễ dùng, tính gắn kết và sự tự tin.
- **Các câu số chẵn (`Q2, Q4, Q6, Q8, Q10`):** Mang sắc thái phủ định tiêu cực về sự rườm rà, thiếu nhất quán và gánh nặng học cách sử dụng.

Cấu trúc đan xen âm–dương giúp phát hiện và hạn chế thiên lệch gật đầu (*acquiescence bias*) hoặc khoanh bừa một cột của người trả lời.

### 1.2. Công thức quy đổi điểm `SUS` (`0.0` .. `100.0`)
Với mảng 10 câu trả lời nguyên $x_1, x_2, \dots, x_{10} \in \{1, 2, 3, 4, 5\}$ của một người tham gia:
- Điểm đóng góp của câu lẻ ($i \in \{1, 3, 5, 7, 9\}$): $c_i = x_i - 1 \in [0, 4]$
- Điểm đóng góp của câu chẵn ($i \in \{2, 4, 6, 8, 10\}$): $c_i = 5 - x_i \in [0, 4]$
- Tổng điểm `SUS` của phiên (thang `0..100`, không phải tỷ lệ phần trăm):
  $$\text{SUS} = 2.5 \times \sum_{i=1}^{10} c_i$$

### 1.3. Ngưỡng tham chiếu chuẩn quốc tế (Bangor, Kortum & Miller, 2009; Sauro & Lewis, 2016)
Mốc trung bình lịch sử của `SUS` trên hàng nghìn hệ thống phần mềm là **`68.0` điểm**:

| Khoảng điểm `SUS` | Mức độ chấp nhận (Bangor Acceptability) | Hạng tính từ (Adjective Rating) | Thang chữ (Sauro–Lewis Grade) | Diễn giải thực tiễn |
| :---: | :--- | :--- | :---: | :--- |
| `84.1 – 100.0` | `Acceptable` (Chấp nhận tốt) | `Best Imaginable / Excellent` | `A+` / `A` | Trải nghiệm xuất sắc, người dùng sẵn sàng giới thiệu |
| `72.6 – 84.0` | `Acceptable` (Chấp nhận được) | `Good` | `B+` / `B` | Khả năng sử dụng tốt, vượt mức trung bình ngành |
| `68.0 – 72.5` | `Acceptable` (Đạt ngưỡng chuẩn) | `OK / Above Average` | `C+` / `C` | Đạt ngưỡng trung bình (`68.0`), còn một số ma sát nhỏ |
| `51.7 – 67.9` | `Marginal` (Cận biên — Cần cải thiện) | `OK / Fair` | `C-` / `D` | Dưới trung bình; tồn tại điểm nghẽn làm giảm hiệu quả |
| `0.0 – 51.6` | `Not Acceptable` (Không chấp nhận được) | `Poor / Worst Imaginable` | `F` | Khả năng sử dụng kém nghiêm trọng; người dùng bị chặn hoặc bối rối nặng |

> *Lưu ý cỡ mẫu nhỏ (`n = 7`):* Với 7 người tham gia, báo cáo bắt buộc trình bày đồng thời **Trung bình (`Mean`), Độ lệch chuẩn mẫu (`SD`, chia cho `n - 1`), Trung vị (`Median`) và Khoảng biến thiên (`Min – Max`)** để tránh bị kéo lệch bởi một phiên cá biệt.

---

## 2. Thang đo độ dễ sau nhiệm vụ (`SEQ`) và 4 Câu hỏi Phỏng vấn Sâu (`Open Probes`)

1. **Single Ease Question (`SEQ`, thang `1..7` — khuyến khích thu thập ngay khi vừa kết thúc nhiệm vụ):**
   - Hỏi ngay sau khi người tham gia hoàn thành hoặc dừng nhiệm vụ (*"Nhìn chung, việc thực hiện yêu cầu vừa rồi đối với bạn khó hay dễ?"*, `1 = Rất khó` .. `7 = Rất dễ`; mốc trung bình tham chiếu của `SEQ` là `~5.5`). Giúp đo trực tiếp độ khó của riêng luồng nhiệm vụ trước khi chấm `SUS` toàn cục.
2. **4 chiều phỏng vấn mở bắt buộc theo đề bài (`Clarity`, `Error recovery`, `Speed`, `Trust`):**
   - **`Clarity` (Độ rõ ràng):** Các tiêu đề, nhãn ô nhập, hướng dẫn quy tắc dữ liệu và trạng thái trên màn hình có dễ hiểu ngay từ lần đọc đầu tiên không? Chỗ nào gây hiểu lầm?
   - **`Error recovery` (Khả năng phục hồi sau lỗi):** Khi hệ thống từ chối dữ liệu hoặc báo lỗi, thông báo hiển thị có giúp bạn nhận biết ngay nguyên nhân và cách tự sửa không?
   - **`Speed` (Tốc độ & Sự trôi chảy):** Bạn cảm nhận thời gian và số thao tác để đi hết luồng vừa rồi nhanh gọn hay rườm rà so với mong đợi? Khâu nào làm bạn mất nhiều thời gian nhất?
   - **`Trust` (Mức độ tin cậy & An tâm):** Bạn có cảm thấy yên tâm khi cung cấp thông tin cá nhân/mật khẩu và tin tưởng rằng hệ thống đã lưu đúng dữ liệu của bạn không? Vì sao?

---

## 3. Quy tắc phân tách `Isolated Bugs` và `Systemic Design Issues`

Yêu cầu trọng tâm ở Phase 3 của đề bài là không trộn lẫn mọi phàn nàn vào một danh sách phẳng mà phải **phân tách rạch ròi 2 bản chất vấn đề**:

| Tiêu chí đối chiếu | Lỗi phần mềm đơn lẻ (`Isolated Bugs`) | Vấn đề thiết kế hệ thống (`Systemic Design Issues`) |
| :--- | :--- | :--- |
| **Bản chất gốc rễ** | Lỗi lập trình cục bộ tại một thành phần hoặc một API làm hệ thống chạy **sai khác trực tiếp so với đặc tả chức năng/bảo mật** hoặc gây hỏng trạng thái cụ thể | Khiếm khuyết mang tính **kiến trúc tương tác, luồng thông tin hoặc quy ước giao diện lặp lại xuyên suốt nhiều màn hình**, làm tăng tải nhận thức dù chức năng không crash |
| **Khả năng tái hiện** | Tái hiện xác định 100% bằng các bước cố định (`Steps to Reproduce`), có ngưỡng `Expected` vs `Actual` rõ ràng | Bộc lộ qua hành vi ngập ngừng, hiểu nhầm mô hình hoạt động, phải mò mẫm hoặc cảm giác thiếu tin cậy ở nhiều người tham gia |
| **Ví dụ điển hình trên EShop** | Regex mật khẩu đòi khoảng trắng (`BUG-01`); ô mật khẩu `/login` để `type="text"` lộ ký tự (`BUG-04`); tiêu đề trang `/login` hiện chữ `Đăng Ký` (`BUG-13`); Header không cập nhật tên sau khi lưu Hồ sơ (`BUG-11`) | Thiếu đồng nhất cơ chế thông báo phản hồi giữa các màn hình (lúc chữ đỏ đầu form, lúc dưới nút, lúc bật hộp thoại chặn `window.alert()`); không tự động đăng nhập sau khi vừa tạo tài khoản mới khiến người dùng phải gõ lại toàn bộ thông tin vừa đăng ký; thiếu gợi ý định dạng cụ thể ngay tại ô nhập |
| **Hướng xử lý & Liên kết** | Bắt buộc lập **Bug Report** và đăng **GitHub Issue** kèm ảnh chụp màn hình (hoặc tham chiếu chéo mã `BUG-xx` / Issue `#xx` nếu đã đăng ở Task 1) | Đề xuất giải pháp tái thiết kế trải nghiệm (`UX Redesign Recommendation`) ở cấp toàn hệ thống |

---

## 4. Khung xếp hạng mức độ nghiêm trọng (`Severity & Priority Matrix`)

Mỗi phát hiện (`Finding`) được đánh giá kết hợp giữa **Mức độ tác động (`Severity`, 1..4)** và **Tần suất bắt gặp trên 7 phiên (`Frequency = k / 7`)**, tính điểm ưu tiên **`Impact Score = Severity x (k / 7)`** (thang `0.14 .. 4.00`):

| Mức `Severity` | Trọng số | Tiêu chí phân loại trong kiểm thử khả dụng |
| :--- | :---: | :--- |
| **`Critical` (Blocker)** | `4` | Ngăn chặn người dùng hoàn thành nhiệm vụ nếu không có trợ giúp từ bên ngoài, làm mất dữ liệu hoặc làm lộ thông tin nhạy cảm nghiêm trọng (như lộ mật khẩu rõ trên màn hình) gây sụp đổ niềm tin. |
| **`Major` (High Friction)** | `3` | Gây nhầm lẫn đáng kể, dẫn tới thao tác sai lặp lại hoặc kéo dài thời gian đáng kể, nhưng người dùng cuối cùng vẫn có thể tự tìm đường vượt qua được. |
| **`Minor` (Moderate Friction)** | `2` | Gây khựng nhẹ (vài giây ngập ngừng) hoặc bất tiện nhỏ khi nhập liệu/điều hướng, không đe dọa kết quả hoàn thành nhiệm vụ. |
| **`Cosmetic` (Low)** | `1` | Điểm chưa chỉn chu về thẩm mỹ, câu chữ hoặc bố cục mà người dùng chỉ nhận xét thêm chứ không làm chậm thao tác. |

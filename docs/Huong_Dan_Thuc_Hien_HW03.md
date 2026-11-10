# Hướng Dẫn Chi Tiết Thực Hiện Bài Tập HW03 – GUI & Usability Testing

Tài liệu này tổng hợp và hướng dẫn từng bước cách thực hiện bài tập **HW03 – GUI & Usability (HW03-AI)** dựa trên đề bài gốc [`2026.HW03.GUI Usability_En.md`](./2026.HW03.GUI%20Usability_En.md).

---

## 1. Tổng Quan & Quy Tắc Cốt Lõi (Bắt Buộc Nắm Rõ)

### Thông tin chung
- **Mã bài tập:** HW03-AI (Làm cá nhân, nhưng **không được trùng lặp phạm vi** với các thành viên khác trong cùng nhóm).
- **Hệ thống kiểm thử (SUT):** EShop (`https://github.com/ttbhanh/eshop-sut`).
- **Mức độ Bloom-AI yêu cầu:** `G9.3 (Analyse)` và `G9.4 (Collaborate with AI for exploratory testing)`.
- **Cấu trúc điểm (Tổng 100 điểm):**
  1. **Task 1 — GUI Checklist** (Thiết kế + Thực thi + Báo cáo lỗi): **30 điểm**
  2. **Task 2 — Usability Evaluation** (Kịch bản + 7 phiên thử nghiệm + Phân tích): **40 điểm**
  3. **Task 3 — Cross-Browser / Cross-Platform** ($\ge 3$ nền tảng): **20 điểm**
  4. **Agent Skills** (Xây dựng skill + Video demo): **10 điểm**

### Các quy định "Sống Còn" (Tránh bị 0 điểm)
1. **Không nộp trễ & Không thiếu file:** Thiếu bất kỳ tài liệu bắt buộc nào trong file `.zip` = **0 điểm**.
2. **Không đạo văn (kể cả Prompt):** Sao chép bài làm hoặc sao chép prompt giữa các sinh viên = **0 điểm cả hai**.
3. **Không bịa đặt người tham gia (Task 2):** Phải có 7 người thật ngoài lớp học. Trợ giảng (TA) sẽ gọi điện/Zalo xác minh ngẫu nhiên **2 người**. Nếu giả mạo = **0 điểm Task 2**.
4. **Chống gian lận ảnh chụp màn hình (Task 3):** Ảnh chụp đa nền tảng phải hiển thị rõ thông tin của bạn (**Email sinh viên**, **MSSV và Họ tên** điền vào form trên giao diện SUT) cùng với tên trình duyệt/thiết bị/OS và URL `localhost`.
5. **AI-First nhưng có kiểm duyệt (Human Review):** Không dùng 1 câu prompt chung chung. Phải dẫn dắt AI từng bước, review kết quả, sửa lỗi và bổ sung những gì AI bỏ sót.
6. **Git Commit theo từng bước:** Mỗi giai đoạn làm bài phải có Git commit riêng biệt (thiết kế checklist, chạy test, log bug, từng phiên usability, phân tích...).

---

## 2. Chuẩn Bị Môi Trường & Chọn Phạm Vi (Scope Selection)

### Bước 2.1: Cài đặt và chạy SUT (EShop)
1. Clone repository `https://github.com/ttbhanh/eshop-sut` về máy.
2. Đọc `README.md` của repo để khởi chạy Backend, Web Frontend (và Mobile App qua Expo Go nếu chọn).
3. Khởi tạo Git repository cho thư mục làm bài tập của bạn (hoặc fork repo SUT để vừa quản lý bài vừa tạo **GitHub Issues** cho việc báo cáo bug).

### Bước 2.2: Chọn phạm vi (Thống nhất với nhóm để KHÔNG TRÙNG LẶP)
Mỗi thành viên trong nhóm phải chọn **màn hình chính (Task 1)** và **luồng nghiệp vụ (Task 2)** khác nhau:

- **Các phân hệ của SUT:**
  - **Pool A (Auth, Categories, Products):** FR-01 (Đăng ký), FR-02 (Đăng nhập & khóa tài khoản), FR-03 (Quên/Đặt lại mật khẩu 2 bước), FR-04 (Hồ sơ cá nhân), FR-05 (Danh sách & tìm kiếm SP), FR-06 (Chi tiết SP).
  - **Pool B (Cart & Checkout):** FR-07 (Giỏ hàng), FR-08 (Thanh toán), FR-09 (Mã giảm giá), FR-10 (Trạng thái đơn hàng), FR-11 (Lịch sử đơn hàng).
  - **Pool C (Web Admin):** FR-12 (Phân quyền), FR-13 (Dashboard), FR-14 (CRUD Danh mục), FR-15 (CRUD Sản phẩm), FR-16 (Import SP từ CSV), FR-17 (CRUD Mã giảm giá), FR-18 (Quản lý đơn hàng), FR-19 (Quản lý người dùng).
  - **Pool D (Mobile App):** Các màn hình trên ứng dụng di động.

- **Chọn cho Task 1 (GUI Checklist):** Chọn **nhiều màn hình liên quan** (tối thiểu 1 màn hình nhưng đề bài khuyến nghị chọn từ 2–4 màn hình để tạo được **> 40 mục kiểm tra** sâu sắc, không trùng lặp).
- **Chọn cho Task 2 (Usability Evaluation):** Chọn **1 luồng đầu-cuối (end-to-end flow)** duy nhất (Ví dụ: *Đăng ký tài khoản $\rightarrow$ Tìm kiếm sản phẩm $\rightarrow$ Thêm vào giỏ $\rightarrow$ Áp mã giảm giá & Thanh toán*).

> **Lưu ý Git:** Sau khi chọn xong phạm vi và tạo khung thư mục báo cáo, hãy tạo commit đầu tiên: `docs: initialize project structure and scope selection`.

---

## 3. Hướng Dẫn Chi Tiết Từng Task

### TASK 1: Thiết Kế & Thực Thi GUI Checklist (30 Điểm)

#### Bước 1: Thiết kế Checklist (> 40 items) bao phủ 4 khía cạnh giao diện (IA)
Checklist của bạn phải có **hơn 40 mục (khuyến nghị 45–60 mục)** và bao phủ đủ 4 mã khía cạnh giao diện sau:
1. **IA-01: General UI standards (Tiêu chuẩn UI chung):** Bố cục (layout), căn lề (alignment), khoảng cách (spacing), font chữ, màu sắc, độ tương phản, tính nhất quán của icon/button, responsive khi thu phóng màn hình...
2. **IA-02: Forms (Biểu mẫu):** Nhãn (labels), placeholder, trường bắt buộc (`*`), kiểm tra dữ liệu đầu vào (validation), định dạng ngày/số/tiền tệ, giới hạn ký tự, trạng thái nút Submit (disabled/enabled), tự động focus...
3. **IA-03: Navigation (Điều hướng):** Thanh menu, breadcrumbs, liên kết (links), điều hướng bằng bàn phím (`Tab`, `Enter`, `Esc`), thứ tự Tab (tab order), nút Back/Forward của trình duyệt, phân trang (pagination)...
4. **IA-04: Feedback / state (Phản hồi & Trạng thái):** Thông báo lỗi/thành công (toast/inline message), trạng thái đang tải (loading spinner/skeleton), trạng thái rỗng (empty state), hộp thoại xác nhận (confirmation modal) khi xóa/hủy, giữ trạng thái khi tải lại trang...

#### Bước 2: Quy trình cộng tác với AI & Bổ sung mục AI bỏ sót (Rất quan trọng)
1. **Dùng AI tạo bản nháp:** Viết prompt có cấu trúc (cung cấp ngữ cảnh màn hình EShop, yêu cầu phân loại theo `IA-01` đến `IA-04`). Lưu lại toàn bộ câu prompt và kết quả vào **AI Audit Report**.
2. **Review và tự bổ sung (Human Review):** Đọc kỹ danh sách AI sinh ra, chỉnh sửa các mục chung chung và **tự thêm vào các mục mà AI đã bỏ sót**.
3. **Giải thích lý do AI bỏ sót:** Đối với **mỗi mục bạn tự thêm vào**, phải giải thích rõ trong báo cáo *tại sao AI lại bỏ sót nó* (Ví dụ: do prompt chưa mô tả đặc thù tiếng Việt/tiền tệ VNĐ, do giới hạn của mô hình AI chỉ tập trung vào happy-path UI mà quên Accessibility/ARIA, quên kiểm thử tràn văn bản dài tiếng Việt có dấu, chế độ Dark Mode, RTL layout, hoặc hành vi cắt chữ khi zoom 200%...).

#### Bước 3: Thực thi Checklist (Test Execution) & Ghi nhận kết quả
Tạo bảng Checklist trên cả **File Excel (`.xlsx`)** và trong **Báo cáo chính (`.md`)** với các cột gợi ý sau:

| ID | Screen | Aspect (IA-01..04) | Checklist Item (Test Condition) | Source (AI / Human Added) | Result (Chrome) | Result (Platform 2) | Result (Platform 3) | Notes (Lý do nếu Failed / Lý do AI bỏ sót) | Screenshot / Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

- Đánh dấu từng mục là **Passed** hoặc **Failed**.
- Cột **Notes**: Bắt buộc ghi rõ lý do thất bại đối với các mục **Failed**.
- **Ảnh chụp màn hình (Screenshots):** Đính kèm ảnh chụp cho các mục **Failed**.

#### Bước 4: Báo cáo lỗi (Bug Reporting)
- Với mỗi lỗi tìm được, viết Bug Report chi tiết trong file Markdown báo cáo **VÀ** tạo Issue trên trang **GitHub Issues** của bạn.
- Mỗi GitHub Issue phải có: Tiêu đề rõ ràng, Các bước tái hiện (Steps to reproduce), Kết quả mong đợi (Expected), Kết quả thực tế (Actual), Môi trường, Mức độ nghiêm trọng (Severity), và **Ảnh chụp màn hình đính kèm**.

> **Lưu ý Git:** Tạo các commit riêng cho bước thiết kế checklist (`feat(task1): design GUI checklist with AI and human review`), bước thực thi (`test(task1): execute GUI checklist on SUT`), và bước báo cáo lỗi (`docs(task1): add bug reports and screenshots`).

---

### TASK 2: Đánh Giá Khả Năng Sử Dụng – Usability Evaluation (40 Điểm)

Thực hiện đánh giá khả năng sử dụng có điều phối (moderated usability testing) trên **1 luồng end-to-end** đã chọn với **7 người tham gia thật**.

#### Giai đoạn 1: Lập kế hoạch & Chuẩn bị (Plan & Prepare)
1. **Xác định mục tiêu (Objectives):** Nêu rõ bạn muốn tìm hiểu điều gì (VD: *Người dùng có gặp khó khăn khi tìm kiếm sản phẩm và áp dụng mã giảm giá không? Thông báo lỗi ở trang thanh toán có dễ hiểu để họ tự sửa lỗi không? Mức độ tự tin của họ khi hoàn tất đơn hàng?*).
2. **Viết kịch bản nhiệm vụ (Task Scenario):**
   - Biến luồng đã chọn thành một kịch bản mang tính mục tiêu thực tế (Goal-oriented), **KHÔNG viết hướng dẫn từng bước bấm nút nào**.
   - *Ví dụ tốt:* "Bạn đang muốn mua một chiếc áo khoác mùa đông có giá dưới 500.000 ₫ để tặng bạn bè. Hãy sử dụng trang web EShop để tìm một sản phẩm phù hợp, áp dụng mã giảm giá hiện có để được ưu đãi và hoàn tất đặt hàng."
   - *Ví dụ sai (cấm dùng):* "Bước 1 bấm vào ô tìm kiếm, gõ áo khoác. Bước 2 bấm nút lọc giá < 500k. Bước 3 bấm Thêm vào giỏ..."
3. **Chuẩn bị công cụ đo lường (Instruments):**
   - **Thang đo chuẩn:** Chọn **SUS** (System Usability Scale - 10 câu hỏi thang điểm 1–5) hoặc **UEQ-S** (User Experience Questionnaire Short - 8 mục thang điểm -3 đến +3). Chuẩn bị sẵn Google Form hoặc phiếu đánh giá.
   - **Câu hỏi phỏng vấn mở (Probe Questions):** Chuẩn bị ít nhất 4 câu hỏi bao quát 4 khía cạnh bắt buộc:
     1. *Clarity (Độ rõ ràng):* Giao diện và thông tin hiển thị có chỗ nào làm bạn bối rối không?
     2. *Error recovery (Khả năng phục hồi sau lỗi):* Khi gặp lỗi (hoặc nếu gặp lỗi), bạn có dễ dàng biết cách sửa không?
     3. *Speed (Tốc độ):* Bạn cảm thấy thời gian để hoàn thành thao tác vừa rồi nhanh hay chậm so với kỳ vọng?
     4. *Trust (Độ tin cậy):* Bạn có cảm thấy yên tâm/tin tưởng khi nhập thông tin cá nhân và đặt hàng trên trang này không? Vì sao?
4. **Tuyển 7 người tham gia thật (Recruit 7 participants):**
   - **Điều kiện bắt buộc:** Phải là người **ngoài lớp học** (sinh viên đang học môn này không hợp lệ). Ưu tiên người không học CNTT / không phải Tester.
   - Lưu thông tin liên hệ xác thực vào bảng: Họ tên, Độ tuổi/Nghề nghiệp, SĐT/Zalo/Email (**che 4 chữ số ở giữa của SĐT**, ví dụ: `090****123`).
5. **Chạy phiên thử nghiệm (Pilot Session):**
   - Thử nghiệm trước với **1 người (ngoài 7 người chính thức)** để kiểm tra kịch bản có dễ hiểu không, luồng web có bị lỗi chặn đứng không, thời gian có hợp lý không. Ghi nhận lại kết quả Pilot và những tinh chỉnh trước khi chạy thật.

> **Lưu ý Git:** Commit tài liệu kế hoạch và kịch bản (`docs(task2): complete usability evaluation plan and pilot refinement`).

#### Giai đoạn 2: Tiến hành 7 phiên thử nghiệm (Conduct the Sessions)
Thực hiện lần lượt từng phiên (1 người/phiên):
1. **Thiết lập tâm lý (Set the stage):** Giải thích rằng bạn đang kiểm thử *sản phẩm* chứ không phải kiểm tra trình độ của họ. Hướng dẫn họ phương pháp **Think Aloud** (vừa thao tác vừa nói suy nghĩ trong đầu ra thành tiếng). Xin phép quay màn hình và ghi âm.
2. **Quan sát trung lập (Observe neutrally):** Không gợi ý, không chỉ chỗ bấm. Chỉ can thiệp nếu người dùng bị kẹt hoàn toàn không thể đi tiếp.
3. **Thu thập bằng chứng (Capture evidence):**
   - Quay video màn hình (và âm thanh).
   - Ghi chép có cấu trúc (Structured notes): Thời gian hoàn thành, các điểm khựng lại (hesitations), bấm nhầm (errors), điểm gây khó chịu (friction points) và câu nói thể hiện sự bối rối của người dùng.
4. **Kết thúc phiên (Close the session):**
   - Cho người tham gia điền phiếu **SUS / UEQ-S** ngay lập tức.
   - Hỏi các câu hỏi mở (Probe questions) để đào sâu vào những chỗ bạn thấy họ ngập ngừng.

> **Lưu ý Git:** Khuyến khích commit ghi chú sau các phiên thử nghiệm (hoặc từng phiên) theo đúng yêu cầu Mục 12 (`data(task2): add session notes and SUS responses for participants 1-7`).

#### Giai đoạn 3: Phân tích & Báo cáo (Analyse & Report)
1. **Tính điểm SUS / UEQ-S:**
   - Lập bảng điểm chi tiết từng câu hỏi của cả 7 người và tính điểm trung bình chung.
   - *Cách tính SUS:* Với câu lẻ (1, 3, 5, 7, 9) lấy $(\text{Điểm} - 1)$; với câu chẵn (2, 4, 6, 8, 10) lấy $(5 - \text{Điểm})$. Cộng tổng điểm của 10 câu rồi nhân với $2.5$ để ra thang điểm $100$. Đối chiếu với chuẩn (VD: $> 68$ là trên trung bình).
2. **Tổng hợp (Synthesise):** Gom nhóm các vấn đề tương tự nhau của 7 người dùng. Phân biệt rõ đâu là **lỗi phần mềm đơn lẻ (isolated bugs)** và đâu là **vấn đề thiết kế hệ thống (systemic design issues)**.
3. **Phân loại mức độ nghiêm trọng (Prioritise by severity):** Xếp hạng các vấn đề tìm được (ví dụ: *Critical/Blocker* ngăn hoàn thành nhiệm vụ, *Major* gây khó khăn lớn, *Minor/Cosmetic* bất tiện nhỏ về thị giác).
4. **Báo cáo lỗi (Report bugs):** Đưa các lỗi thực sự phát hiện được vào Báo cáo chính **VÀ** tạo **GitHub Issues** kèm ảnh chụp màn hình.

---

### TASK 3: Kiểm Thử Đa Trình Duyệt / Đa Nền Tảng – Cross-Browser / Cross-Platform (20 Điểm)

Thực thi lại Checklist của Task 1 trên **ít nhất 3 nền tảng (platforms)** khác nhau.

1. **Lựa chọn nền tảng (Tối thiểu 3):**
   - Tổ hợp chuẩn trên Web: **Chrome**, **Firefox**, và **Safari** (hoặc **Android Chrome**).
   - Thay thế hợp lệ: Bạn có thể test **Mobile App của SUT qua Expo Go trên điện thoại thật** để tính là 1 trong 3 nền tảng bắt buộc (ví dụ: Chrome + Firefox + Expo Go Mobile).
2. **Công cụ thực hiện:**
   - Ưu tiên dùng tài khoản dùng thử (Trial) của **BrowserStack** hoặc **LambdaTest** (kết nối Local Testing tới `localhost` của bạn).
   - Nếu hết hạn trial, có thể dùng Sauce Labs, CrossBrowserTesting, hoặc thiết bị vật lý thật.
3. **Quy tắc chụp ảnh màn hình (CỰC KỲ QUAN TRỌNG - Chống gian lận Mục 6 & Mục 11):**
   - Ảnh chụp màn hình phải thấy rõ: **Tên Trình duyệt / Hệ điều hành / Thiết bị** + **URL `localhost` của SUT**.
   - **Trên biểu mẫu (form) của giao diện SUT hoặc lớp phủ (overlay):** Phải hiển thị rõ **Email sinh viên**, **Mã số sinh viên (Student ID) và Họ tên đầy đủ** của bạn (hãy nhập trực tiếp chuỗi `MSSV - Họ Tên - Email sinh viên` vào ô input trên form của SUT khi chụp ảnh, đồng thời chèn watermark/overlay email sinh viên lên ảnh theo đúng yêu cầu Mục 6 & Mục 11).

> **Lưu ý Git:** Commit kết quả và hình ảnh kiểm thử đa nền tảng (`test(task3): add cross-browser execution results and screenshots`).

---

### TASK 4 (Mục 7): Xây Dựng Agent Skill & Video Demo (10 Điểm)

1. **Xây dựng Agent Skills:**
   - Tạo các Agent Skill (ví dụ: thư mục `.agent/skills/` hoặc `.claude/skills/` chứa file `SKILL.md` kèm hướng dẫn, template, quy trình từng bước) cho 2 hoạt động:
     1. Skill thiết kế và rà soát **GUI Checklist** (`gui-checklist-skill`).
     2. Skill lập kế hoạch và phân tích **Usability Evaluation** (`usability-evaluation-skill`).
   - (Khuyến khích thêm): Tạo thêm 1 skill hoặc rule tự động trích xuất lịch sử hội thoại AI ra định dạng **AI Audit Report** (`ai-audit-extractor`).
2. **Quay Video Demo (YouTube Link):**
   - Quay video màn hình (có thuyết minh hoặc phụ đề rõ ràng) trình diễn từ đầu đến cuối (end-to-end) cách bạn gọi và sử dụng các Agent Skills này trên một màn hình hoặc luồng hoàn chỉnh của SUT.
   - Upload lên YouTube (để chế độ **Public** hoặc **Unlisted / Không công khai** — tuyệt đối không để Private) và dán link vào `README.md` cũng như báo cáo chính.

---

## 4. Các Báo Cáo Bắt Buộc Về AI (Mục 9 & Mục 10)

### 4.1. AI Audit Report (Phụ lục bắt buộc)
- Bắt đầu bằng câu tuyên bố: `"I use AI tools for the following tasks:"`
- Liệt kê **mọi tương tác với AI** theo đúng cấu trúc:
  - **Name of the AI tool:** (VD: Gemini, Claude, ChatGPT, Cursor...)
  - **Date and time:** Ngày giờ thực hiện.
  - **Your prompt:** Toàn bộ câu lệnh bạn đã nhập.
  - **The AI output:** Kết quả AI trả về (và ghi chú những gì bạn đã chỉnh sửa/chọn lọc).

### 4.2. AI Critique (Đoạn văn 200–300 từ, bắt buộc)
- Viết một đoạn văn **từ 200 đến 300 từ** (kiểm tra kỹ số từ!) trả lời đủ 3 câu hỏi:
  1. AI đã làm sai, thiên vị (biased), hoặc thiếu sót ở điểm nào trong quá trình làm bài?
  2. Tại sao AI lại không phát hiện ra vấn đề đó? (Phân tích nguyên nhân kỹ thuật/ngữ cảnh).
  3. Bạn rút ra được nguyên tắc gì khi cộng tác với AI qua bài tập này?
- Xuất cả phần **AI Critique và AI Audit Report** ra định dạng **Markdown (`.md`) VÀ PDF (`.pdf`)**.

---

## 5. Cấu Trúc Thư Mục & Danh Sách Kiểm Tra Trước Khi Nộp Bài (Submission Checklist)

### Định dạng tên file nén nộp lên Moodle
```text
<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip
```
- Ví dụ: `25127001_HW03_AI_GUIUsability_095.zip` (Điểm tự đánh giá gồm 3 chữ số từ `000` đến `100`).

### Cấu trúc thư mục gợi ý bên trong file `.zip`
```text
<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>/
├── README.md                                  # Bảng tự đánh giá + Báo cáo tóm tắt kiểm thử + Link YouTube demo
├── Main_Report.md                             # Báo cáo chính (Task 1 + Task 2 + Task 3 + Link GitHub Issues)
├── Main_Report.pdf                            # Bản xuất PDF của Báo cáo chính
├── Bug_Report.md                              # Danh sách chi tiết các Bug + Link & ảnh chụp trên GitHub Issues
├── AI_Critique_and_Audit_Report.md            # AI Critique (200-300 từ) + Nhật ký AI Audit đầy đủ
├── AI_Critique_and_Audit_Report.pdf           # Bản xuất PDF của AI Critique & AI Audit Report
├── git_commit_log.txt                         # Lịch sử Git commit (chạy lệnh: git log --stat > git_commit_log.txt)
├── checklist/
│   └── GUI_Checklist_And_Summary.xlsx         # File Excel (> 40 items, kết quả chạy đa nền tảng + Test Summary)
├── usability_evidence/
│   ├── Participant_List.md                    # Bảng 7 người tham gia (che 4 số giữa SĐT/Zalo)
│   ├── Session_Notes_And_SUS_Responses.xlsx   # Ghi chú quan sát 7 phiên + Điểm SUS/UEQ-S chi tiết
│   └── recordings/                            # Video quay màn hình các phiên (hoặc file chứa link Google Drive/YouTube)
├── screenshots/
│   ├── failed_items/                          # Ảnh chụp các mục Failed trong Task 1
│   ├── github_issues/                         # Ảnh chụp các Bug đã tạo trên GitHub Issues
│   └── cross_platform/                        # Ảnh chụp Task 3 (>= 3 nền tảng, có MSSV, Họ tên, Email SV, localhost)
└── skills/
    ├── gui-checklist-skill/
    │   └── SKILL.md
    └── usability-evaluation-skill/
        └── SKILL.md
```

### Checklist rà soát lần cuối trước khi nén `.zip`
- [ ] **README.md** đã có bảng tự đánh giá điểm (Assessment Template Mục 15) và thống kê tổng hợp (số màn hình/luồng, số checklist thiết kế/thực thi/pass/fail, số bug, số người tham gia, link video demo Agent Skill).
- [ ] **Main Report** và **AI Critique & Audit Report** đều có đủ **2 định dạng `.md` và `.pdf`**.
- [ ] **Excel Checklist** có **> 40 mục**, phủ đủ `IA-01`, `IA-02`, `IA-03`, `IA-04`, có giải thích lý do AI bỏ sót cho các mục tự thêm, có ghi chú lý do cho các mục `Failed`.
- [ ] Mọi lỗi phát hiện đều đã được đưa lên **GitHub Issues** kèm ảnh chụp màn hình.
- [ ] **7 người tham gia Usability** đều là người ngoài lớp học, thông tin SĐT/Zalo đã che 4 số giữa, sẵn sàng xác nhận nếu TA gọi.
- [ ] **Ảnh chụp Cross-Platform ($\ge 3$ nền tảng)** hiển thị rõ tên trình duyệt/thiết bị, URL `localhost`, Email sinh viên, MSSV và Họ tên trong form.
- [ ] **AI Critique** nằm đúng trong khoảng **200–300 từ**.
- [ ] Đã xuất file **`git_commit_log.txt`** thể hiện lịch sử làm việc từng bước.


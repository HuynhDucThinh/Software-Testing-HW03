**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS)**

**CS423 / CSC13003 – Kiểm chứng Phần mềm (Software Testing · AI-augmented · 2026)**

**AI POLICY · TEMPLATES — 2026 v1.0 (`[AI-05]`)**

# Bảng Kiểm Quyền Riêng Tư & Sử Dụng AI Có Trách Nhiệm (Privacy & Responsible AI Use Checklist)

*Rà soát đầy đủ danh mục kiểm tra dưới đây trước khi nộp bất kỳ bài tập nào có sự hỗ trợ của AI.*

*Chuyển ngữ và điền đầy đủ theo biểu mẫu chuẩn `[AI-05] - FIT@HCMUS - AI Privacy Checklist` (chuyển thể từ Med Kharbach, PhD, 2026 — CC BY-NC-SA 4.0 cho học phần CS423 / CSC13003).*

---

## 1. Trước Khi Sử Dụng AI (`Before I use AI`)

- `[x]` **Tôi đã xác nhận Cấp độ sử dụng AI được quy định cho bài tập này** (*I confirmed the AI Use Category assigned to this assignment*).
  - *Đối chiếu minh chứng:* Mục 1 đề bài `HW03-AI` quy định `AI Policy: Open` kèm khai báo bắt buộc và `AI Audit Report` (`Category 4` theo thang AIAS; cấp độ Bloom-AI `G9.3 Analyse` & `G9.4 Collaborate` — xem [`Main_Report.md`](../Main_Report.md) phần đầu trang và [`AI-03_Disclosure_Form_23120199.md`](AI-03_Disclosure_Form_23120199.md) Mục 1).
- `[x]` **Tôi đã khai báo rõ công cụ AI sử dụng trong nhật ký câu lệnh** (*I have declared which AI tool(s) I will use in my prompt log*).
  - *Đối chiếu minh chứng:* Khai báo công cụ `Antigravity` (kết hợp `Gemini` & `Claude`) ngay từ `Entry 01` đến `Entry 25` trong [`ai_log/AI_Log.md`](../ai_log/AI_Log.md) và Bảng 1 của [`AI_Critique_and_Audit_Report.md`](../AI_Critique_and_Audit_Report.md).
- `[x]` **Tôi đã đọc và nắm vững Quy định / Thỏa thuận sử dụng AI của môn học** (*I have read the AI Use Agreement for this course*).
  - *Đối chiếu minh chứng:* Đã rà soát toàn bộ nguyên tắc tại Mục 2 (*AI-First strategy*, *Human review*, *AI Audit Report*), Mục 9, Mục 10, Mục 11 và Mục 17 của đề bài cùng bộ biểu mẫu chính sách AI `2026 v1.0` của Khoa CNTT.
- `[x]` **Tôi hiểu rõ những hiện vật nào TUYỆT ĐỐI KHÔNG ĐƯỢC dùng AI sinh ra** (*I understand which artifacts MUST NOT be AI-generated*).
  - *Đối chiếu minh chứng:* Mục 11 đề bài (*Anti-AI-Cheat Constraints*) nghiêm cấm bịa đặt hoặc dùng AI sinh giả danh sách 7 người tham gia thật ngoài lớp học (cùng dữ liệu khảo sát thực nghiệm của họ) và bộ ảnh chụp đa nền tảng; đã tuân thủ nghiêm tại [`usability/participants.md`](../usability/participants.md), `usability/sessions/S00..S07.json`, `usability/recordings/LINKS.md` và `screenshots/task3_cross_platform/`.

---

## 2. Trong Quá Trình Sử Dụng AI (`While I am using AI`)

- `[x]` **Tôi bảo vệ dữ liệu cá nhân của người tham gia khảo sát, bạn học và bên thứ ba** (*I did not enter personal data of classmates, customers, or patients — with full privacy safeguards disclosed below*).
  - *Đối chiếu minh chứng & Công khai minh bạch:*
    1. Ngay sau phiên chạy thử Pilot `S00` (`Entry 13`), phát hiện rủi ro người tham gia có thói quen gõ SĐT/Email cá nhân thật lên biểu mẫu EShop khi đang quay màn hình, tôi đã bổ sung hộp **`Persona mẫu`** vào [`usability/participant_kit.md`](../usability/participant_kit.md), [`usability/moderator_script.md`](../usability/moderator_script.md) và `usability/session_helper.html` (xem [`usability/pilot_refinements.md`](../usability/pilot_refinements.md)) nên cả 7 video `S01.mp4..S07.mp4` không lộ SĐT/Email cá nhân thật trên giao diện web.
    2. Tất cả các phiên thử nghiệm đều có sự đồng thuận tự nguyện (`consent_given: true`, không ghi âm giọng nói `audio_recording: false` để bảo vệ quyền riêng tư).
    3. *Ghi chú minh bạch:* Ở bước lập bảng [`usability/participants.md`](../usability/participants.md) (`Entry 14`), tôi có cung cấp danh sách tên và SĐT liên hệ của `P00..P07` trong phiên làm việc cục bộ để định dạng che đúng 4 chữ số giữa (`084****047` .. `035****706`) theo Mục 11 đề bài; toàn bộ tệp lưu trong Git repository, nhật ký [`ai_log/AI_Log.md`](../ai_log/AI_Log.md) (`Entry 23`) và gói nộp bài đều **chỉ chứa SĐT đã che 4 số giữa**, còn bản đối chiếu đầy đủ phục vụ trợ giảng gọi xác minh ngẫu nhiên được lưu riêng trong thư mục cục bộ `.local/` nằm trong `.gitignore`.
- `[x]` **Tôi không dán nguyên văn trái phép các tài liệu đọc có bản quyền thương mại vào AI** (*I did not paste copyrighted reading materials wholesale into the AI*).
  - *Đối chiếu minh chứng:* Chỉ tham chiếu các nguyên lý kiểm thử tiêu chuẩn phục vụ học tập (ISTQB FL Syllabus, Slide bài giảng học phần, Nielsen Heuristics, WCAG 2.2, công thức chuẩn SUS của Brooke 1996).
- `[x]` **Tôi không đưa mã nguồn nội bộ doanh nghiệp hay mã nguồn vi phạm giấy phép vào AI** (*I did not paste proprietary employer or open-source license-restricted code*).
  - *Đối chiếu minh chứng:* Toàn bộ quá trình chỉ làm việc trên kho mã nguồn thực hành công khai của môn học là `eshop-sut` (`https://github.com/ttbhanh/eshop-sut`, commit `1a9304a`) và mã kiểm thử do chính bài làm xây dựng.
- `[x]` **Tôi đã ghi nhận đầy đủ từng câu lệnh Prompt và phản hồi AI kèm mốc thời gian vào nhật ký** (*I logged each prompt + AI response into prompt_log.md with timestamp*).
  - *Đối chiếu minh chứng:* Đã ghi nối tiếp đủ **25 lượt tương tác (`Entry 01` .. `Entry 25`)** kèm mốc ngày giờ (`+07:00`), câu lệnh `Prompt` nguyên văn, `AI output` và quyết định `Kept / Changed / Rejected / By hand` trong [`ai_log/AI_Log.md`](../ai_log/AI_Log.md).

---

## 3. Trước Khi Nộp Bài (`Before I submit my work`)

- `[x]` **Mọi hiện vật có sự tham gia của AI đều đã được gắn nhãn kiểm toán trong AI Audit Report** (*All AI-generated artifacts are tagged in the AI Audit Report*).
  - *Đối chiếu minh chứng:* Toàn bộ 25 lượt hiện vật được gắn nhãn phán quyết `VALID` (`7/25 = 28.0%`), `INCOMPLETE` (`18/25 = 72.0%`), `INVALID` (`0/25 = 0.0%`) tại [`ai-forms/AI-02_Audit_Report_23120199.md`](AI-02_Audit_Report_23120199.md) Mục 3–4, [`ai_log/audit_summary.md`](../ai_log/audit_summary.md) và [`AI_Critique_and_Audit_Report.md`](../AI_Critique_and_Audit_Report.md) Mục 3.
- `[x]` **Mọi trích dẫn điều khoản và tài liệu tham khảo từ AI đều đã được xác minh tồn tại thật** (*All citations from AI have been verified — sources actually exist*).
  - *Đối chiếu minh chứng:* Toàn bộ số dòng điều khoản `FR-01..05, FR-21..24, SEC-04, SEC-07` đã được đối chiếu khớp trực tiếp với [`eshop-sut/README.md`](../eshop-sut/README.md) trong [`checklist/m1_test_basis.md`](../checklist/m1_test_basis.md); các chuẩn ISTQB FL v4.0, WCAG 2.2, Nielsen (1994), Brooke (1996) và Rubin & Chisnell (2008) đều là tài liệu chuẩn xác thực.
- `[x]` **Mọi đoạn mã và script do AI hỗ trợ viết đều đã được chạy thực thi và kiểm thử thực tế** (*All AI-generated code has been executed and tested*).
  - *Đối chiếu minh chứng:* Đã thực thi và kiểm chứng đầu ra của toàn bộ 9 script Python trong `.agents/skills/gui-checklist-testing/scripts/`, 3 script Python trong `.agents/skills/usability-evaluation/scripts/`, `checklist/dom_probe.js`, `tests/capture_t1_evidence.mjs`, `tests/capture_t3_native_p1_p2.mjs`, `usability/start_session.ps1`, `usability/session_helper.html` và `tests/export_pdfs.mjs` (`0` lỗi thực thi).
- `[x]` **Đoạn văn Phê bình AI (`AI Critique`) dài 200–300 từ đã được đưa vào báo cáo** (*My 200–300-word AI Critique is included in the report*).
  - *Đối chiếu minh chứng:* Đạt **`271` từ** (kiểm đếm tự động bằng `word_count.py` đạt `ĐẠT` trong ngưỡng `200–300` từ), do sinh viên trực tiếp biên tập tại [`ai_log/critique.md`](../ai_log/critique.md), Mục 10 [`Main_Report.md`](../Main_Report.md) và Mục 2 [`AI_Critique_and_Audit_Report.md`](../AI_Critique_and_Audit_Report.md).
- `[x]` **Đoạn Tuyên bố Bắt buộc về Sử dụng AI (`Mandatory Disclosure`) đã có ở cuối báo cáo** (*The Mandatory Disclosure paragraph is at the end of my report*).
  - *Đối chiếu minh chứng:* Trình bày đầy đủ tại Mục 11 của [`Main_Report.md`](../Main_Report.md), Mục 1 của [`AI_Critique_and_Audit_Report.md`](../AI_Critique_and_Audit_Report.md) và Mục 6 của [`AI-02_Audit_Report_23120199.md`](AI-02_Audit_Report_23120199.md).
- `[x]` **Tôi đã đính kèm Biểu mẫu Khai báo Sử dụng AI (`AI Use Disclosure Form`)** (*I attached the AI Use Disclosure Form*).
  - *Đối chiếu minh chứng:* Đính kèm tại [`ai-forms/AI-03_Disclosure_Form_23120199.md`](AI-03_Disclosure_Form_23120199.md).
- `[x]` **Tôi sẵn sàng tham gia buổi vấn đáp ngẫu nhiên 5–7 phút vào tuần kế tiếp sau hạn nộp bài** (*I am ready for a 5–7-min random oral defense the week after submission*).
  - *Đối chiếu minh chứng:* Nắm vững toàn bộ quy trình thiết kế 59 mục checklist (`CL-01..39`, `SV-01..20`), nguyên nhân gốc mã nguồn của 28 Bugs (`#1..#28`), diễn biến thực tế của 8 phiên người dùng `P00..P07`, thiết lập `adb`/CDP trên `OPPO Reno10 5G` và kiến trúc 2 Agent Skills.

---

## 4. Cam Đoan Cuối Cùng (Final Statement)

*Trách nhiệm cuối cùng về tính chính xác, tính nguyên bản và sự liêm chính học thuật của toàn bộ hồ sơ bài nộp này thuộc về cá nhân tôi. Tôi hiểu rõ mọi hành vi sử dụng AI không khai báo hoặc gian lận dữ liệu thực nghiệm đều bị xử lý như hành vi vi phạm quy chế học vụ.*

---

## Chữ Ký Xác Nhận (Signature)

| Hạng mục | Thông tin xác nhận |
| :--- | :--- |
| **Họ tên sinh viên in hoa (`Student name - printed`):** | **HUỲNH ĐỨC THỊNH** |
| **Mã số sinh viên (`Student ID`):** | `23120199` |
| **Lớp / Khóa (`Class / Cohort`):** | `CSC13003 – 23_3 (Khóa K2023)` |
| **Môn học (`Course`):** | `CS423 / CSC13003 – Software Testing (Kiểm chứng Phần mềm)` |
| **Giảng viên & Trợ giảng (`Instructors`):** | TS. Lâm Quang Vũ, TS. Trần Duy Hoàng, ThS. Trần Thị Bích Hạnh, ThS. Trương Phước Lộc, ThS. Hồ Tuấn Thanh |
| **Ngày ký (`Date`):** | `16/11/2026` |
| **Chữ ký (`Signature`):** | *Huỳnh Đức Thịnh (Đã ký xác nhận điện tử — `23120199`)* |

---

## Tài Liệu Tham Khảo (References)

- Kharbach, M. (2026). *AI Use Policy Templates for Higher Education*. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (v4.0 / latest version).
- Hardman, P. (2025). *A Post-AI Learning Taxonomy*.
- Fuster Rabella, M. (2025). *OECD Education Working Paper No. 338*.
- Perkins, M., Roe, J., & Furze, L. (2025). *AI Assessment Scale*.
- Anthropic (2025). *Building reliable AI test agents* — engineering blog.
- DeepEval & Promptfoo documentation — testing frameworks for LLM systems.

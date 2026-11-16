**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS)**

**CS423 / CSC13003 – Kiểm chứng Phần mềm (Software Testing · AI-augmented · 2026)**

**AI POLICY · TEMPLATES — 2026 v1.0 (`[AI-03]`)**

# Biểu Mẫu Khai Báo Sử Dụng AI (AI Use Disclosure Form)

*Đính kèm bắt buộc cho mọi bài tập có sử dụng AI ở bất kỳ mức độ được phép nào.*

*Chuyển ngữ và điền đầy đủ theo biểu mẫu chuẩn `[AI-03] - FIT@HCMUS - AI Disclosure Form` (chuyển thể từ Med Kharbach, PhD, 2026 — CC BY-NC-SA 4.0 cho học phần CS423 / CSC13003).*

---

## 1. Thông Tin Môn Học & Sinh Viên (Course & Student Info)

| Trường thông tin (`Field`) | Nội dung (`Value`) |
| :--- | :--- |
| **Môn học (`Course`):** | `CS423 / CSC13003 – Software Testing (Kiểm chứng Phần mềm)` |
| **Mã bài tập (`Assignment ID`):** | `HW03-AI` |
| **Tên bài tập (`Assignment Title`):** | `GUI & Usability Testing on EShop` (Phạm vi `M1: Register, Login, ForgotPassword, Profile, Header` & Luồng `F1: Đăng ký -> Đăng nhập -> Cập nhật hồ sơ`) |
| **Cấp độ sử dụng AI (`AI Use Category 1–5`):** | `Category 4` — *AI-Assisted Generation with Mandatory Human Review & Audit* (`AI Policy: Open` · Năng lực Bloom-AI `G9.3 Analyse` & `G9.4 Collaborate`) |
| **Ngày hoàn thành (`Date`):** | `16/11/2026` |
| **Họ tên sinh viên (`Student name`):** | Huỳnh Đức Thịnh |
| **Mã số sinh viên (`Student ID`):** | `23120199` (`23120199@student.hcmus.edu.vn`) |

---

## 2. Các Câu Hỏi Khai Báo Chi Tiết (Disclosure Questions)

### 1. Công cụ AI đã sử dụng (`AI tool(s) used`)

- **`Google Antigravity IDE`** — môi trường tác nhân kiểm thử & lập trình tích hợp các mô hình ngôn ngữ lớn **`Google Gemini`** và **`Anthropic Claude`**.
- **Tổng số lượt tương tác có kiểm toán:** **`25` lượt tương tác theo từng bước kỷ luật (`Entry 01` .. `Entry 25`)**, được ghi nhận đầy đủ tên công cụ, ngày giờ, câu lệnh `Prompt` nguyên văn, đầu ra `AI output` và quyết định `Kept / Changed / Rejected / By hand` tại [`ai_log/AI_Log.md`](../ai_log/AI_Log.md) và [`AI_Critique_and_Audit_Report.md`](../AI_Critique_and_Audit_Report.md).
- Không sử dụng công cụ AI sinh ảnh/vẽ giả giao diện hay giả lập dữ liệu người tham gia khảo sát.

### 2. Các giai đoạn sử dụng AI trong bài tập (`Stage(s) of the assignment where AI was used`)

- `[x]` **brainstorming** *(khảo sát danh mục control giao diện `m1_inventory.md` và ánh xạ điều khoản đặc tả `m1_test_basis.md`)*
- `[x]` **outlining** *(dựng cấu trúc kế hoạch đánh giá khả năng sử dụng 9 phần `usability/plan.md`, phân cụm thực thi `G1..G7` trong `RUN.md` và khung báo cáo)*
- `[x]` **drafting** *(sinh bản nháp đầu tiên 39 mục checklist theo 4 lượt `IA-01..IA-04`, bộ phiếu khảo sát `participant_kit.md`, `moderator_script.md`, khung mô tả Bug và đặc tả `SKILL.md`)*
- `[x]` **feedback** *(rà soát chéo theo Rubric đề bài ở vai trò trợ giảng tại `Entry 10, 18, 19, 20, 23, 25` để phát hiện điểm mâu thuẫn hoặc suy diễn quá dữ liệu)*
- `[x]` **revision** *(đồng bộ số liệu, hiệu đính câu chữ báo cáo và chuẩn hóa quy tắc trong Agent Skills sau khi sinh viên kiểm chứng)*
- `[x]` **coding** *(viết script đọc DOM khách quan `dom_probe.js`, script Playwright hỗ trợ đo kiểm/chụp minh chứng `capture_t1_evidence.mjs`, trạm bấm giờ — thu phiếu offline `session_helper.html`, các script kiểm định Python trong `.agents/skills/` và công cụ xuất PDF `md_to_html.py` / `export_pdfs.mjs`)*
- `[x]` **data analysis** *(chạy công thức tổng hợp sổ làm việc Excel 3 sheet, tính toán ma trận điểm `SUS` `Q1..Q10` và thống kê `SEQ`/thời gian thực thi qua `analyze_usability.py`)*
- `[ ]` **visual design** *(KHÔNG sử dụng AI để thiết kế hay vẽ giả giao diện SUT; toàn bộ `130` ảnh Task 1, `15` ảnh Task 3 và `2` ảnh trích video Task 2 đều chụp trực tiếp từ trình duyệt/thiết bị thật)*
- `[x]` **other (specify):** *Đồng bộ 28 GitHub Issues (`#1..#28`) qua `gh` CLI, dựng ảnh trang GitHub Issues từ dữ liệu REST API thật khi repo đang ở chế độ `Private`, và tải lưu trữ 8 tệp video thực nghiệm `.mp4` lên Google Drive.*

### 3. Các câu lệnh Prompt tiêu biểu nhất đã giao cho AI (`Main prompts or tasks given to the AI`)

Toàn bộ 25 câu lệnh `Prompt` nguyên văn được đính kèm tại Phụ lục A ([`AI_Critique_and_Audit_Report.md`](../AI_Critique_and_Audit_Report.md) và [`ai_log/AI_Log.md`](../ai_log/AI_Log.md)). Ba câu lệnh tiêu biểu phản ánh rõ cách dẫn dắt AI từng bước và kiểm toán chất lượng gồm:

1. **Prompt khởi tạo khảo sát nền tảng phạm vi `M1` (`Entry 01` — Task 1 Bước 0):**
   ```text
   Thực hiện Bước 0 của skill gui-checklist-testing cho phạm vi M1 (Sinh viên: Huỳnh Đức Thịnh, MSSV: 23120199, Email: 23120199@student.hcmus.edu.vn): đọc đặc tả eshop-sut/README.md và mã nguồn giao diện M1 trong eshop-sut/frontend-web/src để tạo checklist/m1_inventory.md, checklist/m1_test_basis.md và khởi tạo khung rỗng checklist/checklist.json (step 0).
   ```
2. **Prompt kiểm toán nghiêm ngặt theo vai trò trợ giảng chấm bài (`Entry 18` — Task 1 & Task 3):**
   ```text
   Oke bây giờ tiến hành review nội dung đã làm được trước nhé. Đóng vai trò TA dùng claude để chấm bài, bạn hãy quét toàn bộ nội dung bài nộp. KHÔNG ĐỌC CÁC NỘI DUNG TRONG @[d:\KCPM\GUI & Usability Testing\docs\temp] @[d:\KCPM\GUI & Usability Testing\eshop-sut] vì không liên quan bài nộp => Đánh giá mức độ hoàn thiện cho task 1 phải có minh chứng kèm theo đạt bao nhiêu điểm và gợi ý chỉnh sửa để bài làm đạt điểm tối đa giúp tôi
   ```
3. **Prompt kết nối điện thoại vật lý thật chụp mới toàn bộ 42 ảnh `P3` và tổng hợp thực nghiệm Task 2 (`Entry 22` & `Entry 16`):**
   ```text
   Bây giờ, bạn sẽ thực hiện việc cắm điện thoại OPPO Reno10 5G để bạn chạy chụp luôn 42 ảnh P3 nhé. Tui đã cắm thiết bị vào rồi
   ---
   Thực hiện Bước 5 và tổng hợp hoàn thiện task 2 giúp tôi. Làm xong báo cáo kết quả các nội dung đã thực hiện và đạt được bao nhiêu điểm cho phần này theo rubric @[d:\KCPM\GUI & Usability Testing\docs\2026.HW03.GUI Usability_En.md] Tất cả đều phải có minh chứng
   ```

### 4. Phân định cụ thể phần AI đóng góp và phần Sinh viên tự thực hiện (`Specific parts of the work AI contributed to`)

- **Phần AI khởi tạo và đóng góp công cụ hỗ trợ:**
  - Bản nháp 39 mục checklist đầu tiên `CL-01..CL-39` (`37` mục giữ nguyên `nguon: "AI"`, đóng băng tại `checklist/ai-outputs/`), script đọc DOM `checklist/dom_probe.js`, script xuất sổ làm việc `checklist/M1_GUI_Checklist_And_Summary.xlsx`, script chụp minh chứng `tests/capture_t1_evidence.mjs` và khung mô tả dữ kiện `bugs/BUG-01..28.md`.
  - Bản nháp kế hoạch 9 phần `usability/plan.md`, phiếu khảo sát `participant_kit.md`, kịch bản điều phối `moderator_script.md` (đóng băng mã băm `SHA-256` tại `usability/frozen/`), trạm thu phiếu ngoại tuyến `usability/session_helper.html`, script tính điểm `analyze_usability.py` và khung tổng hợp `Main_Report.md`, `Bug_Report.md`.
  - Hai bộ Agent Skills tái sử dụng tại `.agents/skills/gui-checklist-testing/` và `.agents/skills/usability-evaluation/` cùng công cụ xuất PDF chuẩn A4 (`tests/md_to_html.py`, `tests/export_pdfs.mjs`).
- **Phần Sinh viên trực tiếp hiệu chỉnh và bổ sung chuyên môn:**
  - Hiệu chỉnh đáng kể `CL-09` và `CL-10` (`nguon: "Both"`, bổ sung giả định `NA1`), **tự phát hiện điểm mù của AI và biên soạn mới 20 mục `SV-01..SV-20`** tại [`checklist/sv_items.md`](../checklist/sv_items.md) (bắt được `15/20` lỗi thật như Stored XSS `BUG-03`, đảo thứ tự `Tab` `BUG-15`, tràn ngang Header `BUG-18`, bàn phím chữ `QWERTY` ở ô SĐT Android `BUG-24`).
  - Phát hiện và yêu cầu sửa mô tả sai ở 4 Bug (`BUG-06, 08, 19, 27`), loại bỏ cách dùng chung 37 ảnh có vẽ giả khung trình duyệt của đợt chạy đầu (`Entry 17–18`), xóa bỏ nhận định suy diễn quá dữ liệu ở câu hỏi phỏng vấn mở để thay bằng phân tích *Say–Do Gap* (`Entry 20`), chuẩn hóa quy tắc Skill (`Entry 24`) và **trực tiếp tự biên tập đoạn văn phản biện cá nhân `AI Critique` (`271` từ)** tại [`ai_log/critique.md`](../ai_log/critique.md).
- **Phần `100%` do Sinh viên tự thực hiện — AI tuyệt đối KHÔNG tham gia (Danh mục cấm theo Mục 11 Anti-AI-Cheat):**
  - Tự tuyển chọn, liên hệ và trực tiếp điều phối tại chỗ **1 phiên chạy thử Pilot (`P00`) + 7 phiên chính thức với 7 người tham gia thật ngoài lớp học (`P01..P07`, `100% non-IT`)**; trực tiếp quay màn hình toàn bộ 8 video thực tế `S00.mp4..S07.mp4` ([Google Drive](https://drive.google.com/drive/folders/1IB2Zh8lavgSNagaKdTyaWhBYH24_f8OL)).
  - Từng người tham gia tự tay thao tác trên trình duyệt, tự chấm điểm `SEQ (1–7)`, `10 câu SUS (1–5)` và gõ câu trả lời cho `4 câu hỏi phỏng vấn mở` (bảo toàn nguyên văn trong `usability/sessions/S00..S07.json`); danh sách SĐT/Zalo thật đã che 4 số giữa tại [`usability/participants.md`](../usability/participants.md).
  - Tự kết nối cáp USB điện thoại thật `OPPO Reno10 5G` (Android 15), cài đặt trình duyệt và kiểm chứng trực tiếp giao diện SUT trên cả 3 nền tảng `P1, P2, P3`; tự thực hiện và ghi âm Video Demo 2 Agent Skills ở Task 4.

### 5. Phương pháp kiểm duyệt, hiệu đính và xác minh đầu ra AI (`How I reviewed, revised, or verified the AI output`)

1. **Cơ chế đóng băng bất biến trước khi chỉnh sửa (`Freeze-Before-Edit`):** Mọi bản nháp đầu tiên của AI ở Task 1 (`checklist/ai-outputs/`) và Task 2 (`usability/frozen/` kèm mã băm `SHA-256`) đều được lưu cố định để đối chiếu minh bạch những gì con người đã sửa hoặc bổ sung.
2. **Đối chiếu Cơ sở kiểm thử & Chuẩn học thuật:** Kiểm tra từng điều kiện `Expected` và nhận định phân tích với số dòng cụ thể trong `eshop-sut/README.md`, giáo trình ISTQB FL v4.0, Slide bài giảng tuần GUI & Usability, Nielsen 10 Heuristics, WCAG 2.2 và Rubin & Chisnell (2008); bác bỏ việc đưa `RTL` và `Dark mode` vào checklist sau khi đo thực tế thấy SUT có `0` quy tắc CSS tối và chỉ hỗ trợ tiếng Việt.
3. **Thực thi & Đo kiểm trực tiếp trên 3 nền tảng thật:** Chạy đối chiếu trên Google Chrome `157` (`P1`), Mozilla Firefox `137.0.1` / `159.0` (`P2`) và điện thoại thật `OPPO Reno10 5G` (`P3`), kiểm tra từng ảnh bằng chứng đảm bảo `130/130` tệp `.png` trong `screenshots/task1_failed/` có mã băm `MD5` duy nhất và chụp nguyên màn hình `adb screencap` cho lỗi bàn phím ảo `SV-20` & tràn ngang `SV-06`.
4. **Hậu kiểm từng giây trên Video thực nghiệm:** Đối chiếu chéo 8 tệp video `.mp4` với biên bản `S00..S07.json`, qua đó phát hiện lỗi mới [`BUG-28`](../bugs/BUG-28.md) ([Issue #28](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/28) — mất sạch SĐT & Địa chỉ khi chuyển trang SPA không nhấn `F5` ở `S05 @ 01:48`, đối chứng với `S07 @ 01:02`).
5. **Chạy bộ công cụ kiểm định tự động độc lập:** Kiểm tra bằng `check_checklist.py` (`59` mục, `0` lỗi), `validate_study.py` (`0` lỗi), `analyze_usability.py --check --expect 7` (`0` lỗi), `word_count.py` (`271` từ -> `ĐẠT`) và kiểm tra bố cục in A4 (`docOverflow = 0px`, `brokenImgs = 0`) trên cả 3 báo cáo PDF.

### 6. Trích dẫn công cụ AI theo chuẩn IEEE (`Citation — IEEE style`)

- [1] Google DeepMind, *Google Antigravity IDE* [AI-powered agentic development environment], Mountain View, CA, USA: Google LLC, 2026. [Online]. Available: https://idx.google.com
- [2] Google DeepMind, *Gemini* [Large language model], Mountain View, CA, USA: Google LLC, 2026. [Online]. Available: https://gemini.google.com
- [3] Anthropic, *Claude* [Large language model], San Francisco, CA, USA: Anthropic PBC, 2026. [Online]. Available: https://claude.ai

---

## 3. Cam Đoan Trung Thực Học Thuật (Statement of Honesty)

*Bằng việc ký tên dưới đây, tôi xác nhận toàn bộ nội dung khai báo trên là chính xác và đầy đủ. Tôi hiểu rõ việc không khai báo hoặc khai báo sai sự thật về việc sử dụng AI bị xem là vi phạm liêm chính học thuật và có thể dẫn đến điểm `0` cho toàn bộ bài tập cùng hình thức xử lý kỷ luật theo quy định của Khoa và Nhà trường.*

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

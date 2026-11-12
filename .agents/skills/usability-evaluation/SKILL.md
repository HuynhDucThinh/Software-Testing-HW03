---
name: usability-evaluation
description: Lập kế hoạch, thiết kế bộ công cụ khảo sát, điều phối phiên chạy thử Pilot, kiểm định dữ liệu 7 người tham gia thật ngoài lớp học, chấm điểm thang đo chuẩn SUS và phân tích tổng hợp đánh giá khả năng sử dụng có điều phối (Moderated Usability Evaluation — Task 2 HW03). Dẫn dắt AI qua từng bước kỷ luật có điểm dừng để sinh viên rà soát và tạo Git commit riêng; tái sử dụng linh hoạt cho mọi luồng nghiệp vụ đầu-cuối trên Web hoặc Mobile. Dùng khi người dùng nói "usability evaluation", "đánh giá khả năng sử dụng", "Task 2", "kịch bản người dùng", "SUS", "pilot S00", "7 người tham gia", hoặc gọi skill kèm số bước.
---

# Đánh giá khả năng sử dụng có điều phối theo từng bước (Moderated Usability Evaluation)

Skill này hướng dẫn AI cộng tác với sinh viên thực hiện trọn vẹn một nghiên cứu **Moderated Usability Evaluation** bám sát lý thuyết lập kế hoạch kiểm thử khả dụng 9 phần (Rubin & Chisnell), nguyên lý giao diện người dùng (Consistency, Error Prevention, System Feedback) và chuẩn đo lường **System Usability Scale (SUS — Brooke, 1996)** kết hợp bộ câu hỏi phỏng vấn sâu 4 chiều (`Clarity`, `Error recovery`, `Speed`, `Trust`).

**Nguyên tắc cốt lõi:** Mỗi lần kích hoạt skill chỉ thực hiện **đúng một bước (`Bước 0` .. `Bước 5`) rồi dừng lại** để sinh viên kiểm duyệt, hiệu chỉnh và tạo Git commit độc lập. Tuyệt đối không dùng một câu lệnh gộp để sinh toàn bộ bài làm.

---

## Quy tắc bắt buộc & Cổng chống gian lận (Anti-AI-Cheat Hard Gates)

1. **Cấm tuyệt đối bịa đặt người tham gia (`Participant Impersonation = 0 điểm`):**
   - AI **không bao giờ** tự sinh họ tên, số điện thoại, Zalo, email hay hồ sơ của người tham gia thử nghiệm (`P00` Pilot và `P01..P07` chính thức).
   - Toàn bộ 7 người tham gia chính thức phải là **người thật ngoài lớp học HW03** (ưu tiên người dùng phổ thông không chuyên CNTT / không phải Tester).
   - Trong bảng `participants.md`, thông tin SĐT/Zalo bắt buộc **che đúng 4 chữ số ở giữa** (ví dụ: `090****123`), còn trong các phiếu phiên `sessions/S0x.json` chỉ lưu mã ẩn danh (`P00`, `P01..P07`), không lưu SĐT hay email cá nhân.
2. **Cấm tuyệt đối sinh giả lập dữ liệu phiên thử nghiệm:**
   - AI **không bao giờ** tự viết ghi chú quan sát, mốc thời gian, câu nói `Think-Aloud`, điểm `SUS` (`1..5`), điểm `SEQ` hay câu trả lời phỏng vấn mở.
   - Script `init_session.py` chỉ tạo khung JSON rỗng (`null`). Nếu thiếu bất kỳ câu trả lời `SUS` nào trong 10 câu, `analyze_usability.py` báo lỗi mã thoát `1` để sinh viên hỏi lại người tham gia, tuyệt đối không nội suy hay điền thay.
3. **Giữ nguyên 100% mã nguồn gốc của SUT:**
   - Không tạo nhánh sửa mã nguồn `eshop-sut/` khi tổ chức phiên thử nghiệm. Trước mỗi phiên (`S00` và `S01..S07`), khởi tạo lại cơ sở dữ liệu sạch (`node database.js && node server.js`) để đảm bảo tính độc lập trạng thái (`Clean State`).
4. **Kịch bản nhiệm vụ định hướng mục tiêu (`Goal-oriented Scenario`):**
   - Kịch bản giao cho người tham gia phải xuất phát từ nhu cầu thực tế đời thường, nêu rõ mục tiêu cần đạt nhưng **không nêu hướng dẫn từng bước** và **không tiết lộ tên nút bấm, nhãn trường hay đường dẫn URL** trên giao diện. Kiểm định tự động bằng `scripts/validate_study.py --kit`.
5. **Giao thức cứu hộ minh bạch khi đụng lỗi chặn của SUT (`System-Bug Rescue Protocol`):**
   - Nếu luồng kiểm thử chứa các lỗi mã nguồn mức `Critical` đã biết hoặc mới phát sinh làm chặn cứng bước đầu (ví dụ: biểu thức chính quy từ chối đầu vào hợp lệ theo đặc tả), điều phối viên phải để người tham gia tự xoay xở tối thiểu theo ngưỡng quy định trong `moderator_script.md` để ghi nhận trọn vẹn bằng chứng điểm nghẽn thực tế, sau đó mới cấp gợi ý trung lập theo chuẩn và bắt buộc đánh dấu trạng thái hoàn thành là `co_tro_giup` (`Assisted`) để người tham gia đi tiếp các màn hình kế tiếp trong luồng.
6. **Đóng băng bản nháp AI & Ghi nhật ký AI nối tiếp:**
   - Mọi bản nháp kế hoạch hoặc bộ công cụ do AI khởi tạo ở Bước 0 và Bước 1 phải được đóng băng bằng `scripts/freeze_artifact.py` vào `<dir>/frozen/` trước khi sinh viên chỉnh sửa.
   - Mọi tương tác có sử dụng AI hỗ trợ phân tích/soạn thảo đều phải ghi nối tiếp (`append-only`) vào cuối tệp `ai_log/AI_Log.md` theo đúng định dạng `## Entry NN`.

---

## Cấu trúc thư mục làm việc chuẩn (`<dir>`, mặc định: `usability/`)

| Đường dẫn tệp | Bước sinh | Vai trò & Trách nhiệm |
| :--- | :---: | :--- |
| `<dir>/plan.md` | Bước 0 | Kế hoạch đánh giá 9 phần (AI nháp từ đặc tả luồng -> đóng băng -> SV rà soát & chốt) |
| `<dir>/participant_kit.md` | Bước 1 | Phiếu giao cho người tham gia: Consent + Kịch bản mục tiêu + SEQ + 10 câu SUS + 4 Probes |
| `<dir>/moderator_script.md` | Bước 1 | Kịch bản điều phối viên, quy tắc Think-Aloud, giao thức cứu hộ lỗi chặn & khung ghi chép nhanh |
| `<dir>/participants.md` | Bước 1 -> 3 | Khung trống ở Bước 1; **SV tự điền** danh sách 1 Pilot (`P00`) + 7 người ngoài lớp (`P01..P07`) che 4 số giữa ở Bước 3 |
| `<dir>/frozen/` | Bước 0, 1 | Lưu trữ bất biến các bản nháp AI kèm mã băm `SHA-256` và `INDEX.md` |
| `<dir>/sessions/S00.json` | Bước 2 | Khung rỗng từ `init_session.py`; **SV nhập** dữ liệu phiên chạy thử Pilot (`is_pilot: true`) |
| `<dir>/pilot_refinements.md` | Bước 2 | Bảng đối chiếu thay đổi công cụ trước và sau Pilot (`pilot_diff.py` sinh diff, **SV ghi lý do**) |
| `<dir>/sessions/S01.json..S07.json` | Bước 3 | Khung rỗng từ `init_session.py`; **SV nhập** dữ liệu thực tế của 7 phiên chính thức |
| `<dir>/recordings/` | Bước 3 | Thư mục lưu video quay màn hình / ghi âm các phiên (hoặc tệp `LINKS.md` trỏ tới thư mục lưu trữ được cấp quyền) |
| `<dir>/sus_and_metrics_summary.md` | Bước 4 | Bảng ma trận điểm `SUS` chi tiết từng câu `Q1..Q10`, thống kê `Mean/SD/Median` & hiệu năng thực thi (`analyze_usability.py`) |
| `<dir>/findings.md` | Bước 5 | Báo cáo tổng hợp Pain Points, tách `Isolated Bugs` vs `Systemic Design Issues`, xếp hạng `Severity` & đồng bộ `Main_Report.md` |

---

## Quy trình thực hiện 6 bước (Mỗi lần gọi chỉ làm 1 bước rồi dừng)

Cách gọi chuẩn: `Dùng skill usability-evaluation cho thư mục <dir> (luồng <mã_luồng>), thực hiện Bước <k>`. Nếu người dùng chưa nêu số bước, kiểm tra các tệp hiện có trong `<dir>` để xác định bước kế tiếp và hỏi xác nhận trước khi làm.

### Bước 0 — Khảo sát luồng nghiệp vụ & Lập Kế hoạch 9 phần (`plan.md`)
1. Đọc tài liệu đặc tả của luồng được chọn (ví dụ với luồng `F1`: `FR-01`, `FR-02`, `FR-04` trong `eshop-sut/README.md` và mã nguồn giao diện thực tế để nắm chính xác các route, trường nhập, thông báo và lỗi chặn đã biết), kết hợp đọc `references/evaluation-methodology.md`.
2. Khởi tạo `<dir>/plan.md` theo khung `assets/plan_template.md` gồm đủ **9 mục đánh số `## 1.` đến `## 9.` đúng thứ tự**:
   - `1. Mục đích đánh giá (Purpose)`
   - `2. Câu hỏi nghiên cứu cụ thể (Problem Statement & Research Questions)`
   - `3. Mục tiêu kiểm thử & Thiết kế nhiệm vụ (Test Objectives & Task Design)`
   - `4. Hồ sơ người tham gia mục tiêu (User Profile & Recruitment Criteria)`
   - `5. Phương pháp & Thiết kế phiên thử nghiệm (Method & Test Design)`
   - `6. Môi trường, Thiết bị & Khởi tạo trạng thái sạch (Environment & Clean State)`
   - `7. Vai trò người điều phối & Quy tắc can thiệp (Test-Monitor Role & Rescue Protocol)`
   - `8. Chỉ số đo lường & Dữ liệu thu thập (Evaluation Measures & Instruments)`
   - `9. Cấu trúc nội dung báo cáo (Report Contents & Deliverables)`
3. Chạy kiểm định cấu trúc và đóng băng bản nháp AI:
   ```powershell
   python .agents/skills/usability-evaluation/scripts/validate_study.py --plan <dir>/plan.md
   python .agents/skills/usability-evaluation/scripts/freeze_artifact.py <dir>/plan.md --step 0 --out <dir>/frozen --prefix T2
   ```
4. Ghi nhật ký tương tác vào `ai_log/AI_Log.md`, báo cáo kết quả để sinh viên rà soát `plan.md` và **DỪNG**.

### Bước 1 — Thiết kế Bộ công cụ khảo sát (`participant_kit.md`, `moderator_script.md`, khung `participants.md`)
1. Đọc `references/sus-and-severity-rubric.md` và `plan.md` đã được sinh viên duyệt.
2. Tạo 3 tài liệu công cụ từ `assets/`:
   - `<dir>/participant_kit.md`: Gồm lời giới thiệu thiết lập tâm lý (*kiểm thử sản phẩm, không kiểm thử con người*), hướng dẫn nói to suy nghĩ (`Think-Aloud`), mục xác nhận đồng ý quay màn hình/ghi âm và xác minh của trợ giảng, khối **Nhiệm vụ định hướng mục tiêu** (`>` blockquote không lộ bước dẫn/tên control), câu hỏi độ dễ `SEQ` (`1..7`), bảng **10 câu chuẩn `SUS`** thang `1..5`, và **4 câu hỏi phỏng vấn mở** (`Clarity`, `Error recovery`, `Speed`, `Trust`).
   - `<dir>/moderator_script.md`: Danh sách kiểm trước phiên (reset CSDL SQLite, bật công cụ quay màn hình), kịch bản lời thoại trung lập, bảng giao thức xử lý khi người dùng bị kẹt bởi lỗi hệ thống, và mẫu bảng ghi nhận sự kiện theo mốc thời gian `mm:ss`.
   - `<dir>/participants.md`: Khung bảng trống cho 1 Pilot (`P00`) và 7 người tham gia chính thức (`P01..P07`) kèm hướng dẫn che 4 chữ số giữa của SĐT/Zalo (tuyệt đối không điền dữ liệu giả).
3. Kiểm định tự động toàn bộ bộ công cụ và đóng băng:
   ```powershell
   python .agents/skills/usability-evaluation/scripts/validate_study.py --plan <dir>/plan.md --kit <dir>/participant_kit.md --participants <dir>/participants.md --allow-pending
   python .agents/skills/usability-evaluation/scripts/freeze_artifact.py <dir>/participant_kit.md <dir>/moderator_script.md --step 1 --out <dir>/frozen --prefix T2
   ```
4. Ghi nhật ký vào `ai_log/AI_Log.md`, hướng dẫn sinh viên tạo Git commit Giai đoạn 1 và **DỪNG**.

### Bước 2 — Khởi tạo & Ghi nhận phiên chạy thử Pilot (`S00`) + Tinh chỉnh công cụ
1. Khởi tạo phiếu rỗng cho phiên Pilot `S00`:
   ```powershell
   python .agents/skills/usability-evaluation/scripts/init_session.py <dir>/sessions S00 --pilot --participant P00
   ```
2. **Sinh viên trực tiếp thực hiện phiên Pilot `S00` với 1 người thật ngoài nhóm 7 người chính thức**, ghi nhận dữ liệu thực tế vào `<dir>/sessions/S00.json` và thông tin liên hệ đã che 4 số giữa của `P00` vào `<dir>/participants.md`.
3. Nếu phát hiện câu chữ kịch bản gây hiểu nhầm, lỗi chặn luồng hoặc bất cập thời gian, cập nhật lại `participant_kit.md` / `moderator_script.md` và chạy `pilot_diff.py` để xuất bảng đối chiếu thay đổi vào `<dir>/pilot_refinements.md` (sinh viên ghi rõ lý do từng thay đổi):
   ```powershell
   python .agents/skills/usability-evaluation/scripts/pilot_diff.py <bản_đóng_băng_step1> <dir>/participant_kit.md -o <dir>/pilot_refinements.md
   python .agents/skills/usability-evaluation/scripts/validate_study.py --kit <dir>/participant_kit.md
   python .agents/skills/usability-evaluation/scripts/analyze_usability.py <dir>/sessions --check
   ```
4. Nhắc sinh viên commit kết quả Pilot và **DỪNG**.

### Bước 3 — Khởi tạo khung 7 phiên chính thức (`S01..S07`) & Kiểm định dữ liệu thực nghiệm
1. Tạo 7 khung JSON rỗng `S01.json` .. `S07.json` (tuyệt đối không điền sẵn bất kỳ con số hay nhận xét nào):
   ```powershell
   python .agents/skills/usability-evaluation/scripts/init_session.py <dir>/sessions S01 S02 S03 S04 S05 S06 S07
   ```
2. **Sinh viên trực tiếp điều phối 7 phiên thử nghiệm độc lập với 7 người thật ngoài lớp học** (reset CSDL sạch trước mỗi phiên, quay màn hình + ghi âm khi được đồng ý), sau đó điền bảng `participants.md` và dữ liệu 7 phiên vào `S01.json..S07.json` (hoặc cung cấp biên bản thô từng phiên để chuyển đúng nguyên văn vào cấu trúc JSON mà không thêm bớt).
3. Chạy kiểm định nghiêm ngặt tính hợp lệ và quy tắc bảo mật thông tin cá nhân:
   ```powershell
   python .agents/skills/usability-evaluation/scripts/validate_study.py --participants <dir>/participants.md
   python .agents/skills/usability-evaluation/scripts/analyze_usability.py <dir>/sessions --check --expect 7
   ```
4. Chỉ khi đạt `0 lỗi`, nhắc sinh viên tạo Git commit lưu trữ dữ liệu 7 phiên và **DỪNG**.

### Bước 4 — Tính toán điểm `SUS`, Hiệu năng thực thi & Xuất bảng dữ kiện lỗi
1. Chạy công cụ thống kê tự động `analyze_usability.py` trên dữ liệu thật của `S00..S07`:
   ```powershell
   python .agents/skills/usability-evaluation/scripts/analyze_usability.py <dir>/sessions --expect 7 --benchmark 05:00 --out <dir>/sus_and_metrics_summary.md
   ```
2. Kiểm tra đầu ra tại `<dir>/sus_and_metrics_summary.md`, bao gồm:
   - Tóm tắt riêng phiên Pilot `S00` (không gộp vào thống kê 7 phiên chính thức).
   - Bảng tổng hợp hiệu năng 7 phiên chính thức `S01..S07` (trạng thái hoàn thành, thời gian, số lỗi thao tác `E`, số lần ngập ngừng `H`, số lần trợ giúp `A`, điểm `SEQ`, tổng điểm `SUS`).
   - **Ma trận điểm chi tiết từng câu `SUS` (`Q1..Q10`) của cả 7 người tham gia** kèm điểm quy đổi và trung bình từng câu.
   - Bảng chỉ số thống kê tổng hợp (`Mean`, `SD` mẫu `n - 1`, `Median`, `Min–Max`, đối chiếu mốc chuẩn `68.0`, xếp hạng mức chấp nhận Bangor và thang điểm chữ Sauro–Lewis).
   - Danh mục toàn bộ sự kiện lỗi kỹ thuật ghi nhận trong các phiên để chuẩn bị đối chiếu ở Bước 5.
3. Khởi tạo khung `<dir>/findings.md` từ `assets/findings_template.md` và **DỪNG** để sinh viên rà soát số liệu.

### Bước 5 — Phân tích tổng hợp Findings, Báo cáo Bug mới (nếu có) & Đồng bộ `Main_Report.md`
1. Trên cơ sở dữ liệu thật của 7 phiên và bảng thống kê Bước 4, hoàn thiện `<dir>/findings.md`:
   - Gom nhóm các điểm nghẽn trải nghiệm tương đồng xuất hiện qua nhiều người dùng.
   - **Phân tách rạch ròi** giữa **Lỗi phần mềm đơn lẻ (`Isolated Bugs`)** và **Vấn đề thiết kế hệ thống (`Systemic Design Issues`)** dựa trên tiêu chí tại `references/sus-and-severity-rubric.md`.
   - **Xếp hạng mức độ nghiêm trọng (`Severity Ranking`)** theo ma trận tác động x tần suất (`Critical / Blocker`, `Major`, `Minor`, `Cosmetic`) kèm đề xuất cải tiến cụ thể.
   - Đối chiếu các `Isolated Bugs` với danh sách GitHub Issues hiện có: nếu phát hiện lỗi thực sự mới chưa có trên GitHub Issues, lập hồ sơ Bug mới kèm ảnh chụp màn hình và đăng lên GitHub Issues đúng quy định đề bài.
2. Đồng bộ đầy đủ toàn bộ nội dung Task 2 vào **Mục `5.1..5.9`**, bảng tổng kết **Mục `8`** của `Main_Report.md` và bảng chỉ số trong `README.md`.
3. Ghi nhật ký tương tác vào `ai_log/AI_Log.md`, kiểm tra lại toàn bộ liên kết nội bộ và hướng dẫn sinh viên tạo Git commit hoàn tất Task 2.

---

## Bảng tra cứu nhanh các Script tự động của Skill

| Script | Chức năng chính |
| :--- | :--- |
| `scripts/validate_study.py` | Kiểm định cấu trúc `plan.md` (9 phần), `participant_kit.md` (không lộ bước/control, đủ 10 SUS + 4 probes) và `participants.md` (1 Pilot + 7 người ngoài lớp, SĐT/Zalo che đúng 4 số giữa `09x****xxx`, không trùng lặp) |
| `scripts/freeze_artifact.py` | Đóng băng bản nháp AI kèm dấu thời gian + mã băm `SHA-256` vào `<dir>/frozen/` và ghi `INDEX.md` |
| `scripts/pilot_diff.py` | Sinh bảng đối chiếu thay đổi công cụ trước và sau phiên Pilot `S00` ra `<dir>/pilot_refinements.md` |
| `scripts/init_session.py` | Tạo khung JSON rỗng (`S00.json`, `S01.json..S07.json`) từ `assets/session_template.json` |
| `scripts/analyze_usability.py` | Kiểm tra toàn vẹn dữ liệu 7 phiên, chống rò rỉ SĐT/email cá nhân, tính chi tiết `SUS` (`Q1..Q10`, `Mean`, `SD`, `Median`, hạng Bangor/Sauro), tỷ lệ hoàn thành, thời gian và gom sự kiện lỗi |

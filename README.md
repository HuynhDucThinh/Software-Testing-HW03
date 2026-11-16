# Software-Testing-HW03 — GUI & Usability Testing (M1)

## 1. Thông Tin Chung (General Information)

| Hạng mục | Nội dung |
| :--- | :--- |
| **Sinh viên thực hiện** | Huỳnh Đức Thịnh |
| **Mã số sinh viên (MSSV)** | `23120199` |
| **Email sinh viên** | `23120199@student.hcmus.edu.vn` |
| **Bài tập** | HW03-AI — GUI & Usability Testing (Individual Assignment) |
| **Hệ thống kiểm thử (SUT)** | EShop (`./eshop-sut`) |
| **Phân công trong nhóm** | **M1** — Authentication & Profile (Web) |
| **Màn hình chính (Task 1)** | `Register` (`/register` — `FR-01`) |
| **Màn hình bổ trợ (Task 1)** | `Login` (`FR-02`), `Forgot Password 2 bước` (`FR-03`), `Profile` (`FR-04`), `Header/Navbar` khi đăng nhập |
| **Luồng Usability (Task 2)** | `F1`: Đăng ký -> Đăng nhập -> Cập nhật hồ sơ (`FR-01` / `FR-02` / `FR-04`) |
| **Mức độ Bloom-AI** | `G9.3 (Analyse)` & `G9.4 (Collaborate with AI for exploratory testing)` |

---

## 2. Cấu Trúc Thư Mục Dự Án (Repository Structure)

```text
Software-Testing-HW03/
├── README.md                              # Tổng quan, Test Summary, Bảng tự đánh giá & Link Video Demo
├── Main_Report.md                         # Báo cáo chính (Task 1, Task 2, Task 3, Task 4 — kèm bản .pdf)
├── Bug_Report.md                          # Danh sách 28 Bug phát hiện & liên kết GitHub Issues (kèm bản .pdf)
├── AI_Critique_and_Audit_Report.md        # Phê bình AI (271 từ) & Nhật ký AI Audit Report (kèm bản .pdf)
├── git_commit_log.txt                     # Lịch sử Git commit theo từng bước thực hiện
├── ai-forms/                              # Bộ 3 biểu mẫu Chính sách AI chuẩn FIT@HCMUS 2026 v1.0 (.md & .pdf)
│   ├── AI-02_Audit_Report_23120199.md     # Biểu mẫu kiểm toán 5 phần theo hiện vật
│   ├── AI-03_Disclosure_Form_23120199.md  # Biểu mẫu khai báo sử dụng AI & trích dẫn IEEE
│   └── AI-05_Privacy_Checklist_23120199.md# Bảng kiểm quyền riêng tư & sử dụng AI có trách nhiệm
├── eshop-sut/                             # Mã nguồn hệ thống EShop (System Under Test @ commit 1a9304a)
├── checklist/                             # Thiết kế & Kết quả thực thi GUI Checklist (59 items)
│   ├── checklist.json                     # Nguồn dữ liệu chuẩn cho Markdown, Excel, Bug skeleton
│   ├── M1_GUI_Checklist.md                # Bảng Checklist chi tiết theo 4 IA & 3 nền tảng
│   ├── M1_GUI_Checklist_And_Summary.xlsx  # File Excel 3 sheet (Test Cases, Checklist, Test Summary Report)
│   ├── m1_inventory.md                    # Khảo sát thành phần giao diện thực tế phạm vi M1
│   ├── m1_test_basis.md                   # Trích lục điều khoản đặc tả UI (FR-01..04, FR-21..24, SEC-04/07)
│   ├── sv_items.md                        # 20 mục do SV bổ sung kèm giải thích lý do AI bỏ sót
│   ├── RUN.md                             # Quy trình thực thi G1..G7, quy tắc ảnh & nhật ký chạy
│   ├── dom_probe.js                       # Script đọc DOM khách quan trên DevTools Console
│   └── runs/                              # Các file CSV/JSON kết quả từng lượt chạy P1, P2, P3
├── usability/                             # Bộ hồ sơ thực nghiệm Đánh giá Khả năng Sử dụng (Task 2 — Luồng F1)
│   ├── plan.md                            # Kế hoạch đánh giá 9 phần (Rubin & Chisnell)
│   ├── participant_kit.md                 # Phiếu Consent, Kịch bản mục tiêu, SEQ, 10 câu SUS & 4 Probes
│   ├── moderator_script.md                # Kịch bản điều phối trung lập & System-Bug Rescue Protocol
│   ├── participants.md                    # Danh sách 1 Pilot (P00) + 7 người thật ngoài lớp (P01..P07, che 4 số giữa)
│   ├── pilot_refinements.md               # Đối chiếu tinh chỉnh công cụ sau phiên Pilot S00
│   ├── sessions/                          # Dữ liệu gốc 8 phiên (S00.json Pilot + S01..S07.json chính thức)
│   ├── recordings/LINKS.md                # Liên kết xem trực tiếp 8 video .mp4 trên Google Drive
│   ├── sus_and_metrics_summary.md         # Ma trận điểm SUS từng câu Q1..Q10 & thống kê hiệu năng
│   ├── findings.md                        # Phân tách Isolated Bugs vs Systemic Design Issues & xếp hạng Severity
│   └── frozen/                            # Bản đóng băng đầu ra AI Bước 0 & Bước 1 kèm mã băm SHA-256
├── screenshots/                           # Ảnh chụp minh chứng (Task 1, Task 2 Usability, Task 3, GitHub Issues)
│   ├── task1_failed/                      # 130 ảnh minh chứng mục Failed trên P1 (44), P2 (44), P3 (42)
│   ├── usability/                         # Minh chứng thực nghiệm trích xuất từ video phiên thật (BUG-28 S05, BUG-18 S06)
│   ├── task3_cross_platform/              # 15 ảnh đa nền tảng cấp OS/Thiết bị thật (12 ảnh giao diện + 3 ảnh xác thực phiên bản)
│   └── github_issues/                     # 28 ảnh trang GitHub Issues (#1..#28) + 2 ảnh danh sách tổng quan
├── tests/                                 # Script kiểm tra dò tự động hỗ trợ đối chiếu trên 3 nền tảng
├── ai_log/
│   ├── AI_Log.md                          # Nhật ký tương tác AI gộp chung nối tiếp (Entry 01..25)
│   ├── critique.md                        # Bài phản biện AI cá nhân (200-300 từ)
│   └── audit_summary.md                   # Tổng hợp phân loại kiểm toán đầu ra AI (VALID / INCOMPLETE / INVALID)
├── bugs/                                  # Khung dữ kiện và chi tiết từng Bug
└── .agents/skills/                        # Agent Skills tái sử dụng cho GUI Checklist & Usability Evaluation
```

---

## 3. Báo Cáo Tóm Tắt Kiểm Thử (Test Summary Report)

### 3.1. Chỉ số tổng quan toàn bài

| Chỉ số (Metric) | Kết quả (Value) | Ghi chú |
| :--- | :---: | :--- |
| **Số màn hình / vùng giao diện kiểm thử (Screens tested)** | **5** | `Register` (chính), `Login`, `ForgotPassword` (2 bước), `Profile`, `Header/Navbar` |
| **Số luồng Usability (Flows tested)** | **1** | `F1`: Đăng ký -> Đăng nhập -> Cập nhật hồ sơ (`FR-01` / `FR-02` / `FR-04`) |
| **Số mục Checklist thiết kế (Designed items)** | **59** | Vượt ngưỡng `> 40` mục; phủ đủ 4 IA (`IA-01`: 14, `IA-02`: 23, `IA-03`: 12, `IA-04`: 10) |
| **Số nền tảng thực thi (Platforms tested)** | **3** | `P1` Chrome 157 (Win 11), `P2` Firefox (Win 11; 137.0.1 cài đặt cho ảnh Task 3, 159.0 Playwright cho đo Task 1), `P3` Chrome Android 156/157 (OPPO Reno10 5G) |
| **Tổng số lượt kiểm tra đã thực thi (Executed checks)** | **168 / 177** | `P1`: 58/59, `P2`: 58/59, `P3`: 52/59 (9 lượt `N/A` có giả định `NA1`, `NA2`) |
| **Tổng kết quả lượt chạy (Passed / Failed / N/A / Blocked)** | **38 Passed / 130 Failed / 9 N/A / 0 Blocked** | `45 / 59` mục độc lập phát hiện lỗi (`Failed`) trên ít nhất 1 nền tảng (`14 / 59` mục `Passed` hoàn toàn) |
| **Tổng số Bugs đã báo cáo (GitHub Issues)** | **28 Bugs (`#1`..`#28`)** | `5 Critical`, `11 Major`, `11 Minor`, `1 Cosmetic` (`27` Task 1 + `1` mới `BUG-28` Task 2) — [GitHub Issues](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues) & [`Bug_Report.md`](Bug_Report.md) |
| **Số người tham gia Usability (Participants)** | **7 người thật ngoài lớp học (`P01..P07`) + 1 Pilot (`P00`)** | `100% non-IT`, SĐT che 4 số giữa; **`SUS = 48.6 ± 11.3` (`Hạng F — Poor`)**, `8` video quay màn hình trên [Google Drive](https://drive.google.com/drive/folders/1IB2Zh8lavgSNagaKdTyaWhBYH24_f8OL) |
| **Video Demo Agent Skills (YouTube)** | **[Xem trên YouTube](https://www.youtube.com/watch?v=3AzhYuL9wxg)** | `https://www.youtube.com/watch?v=3AzhYuL9wxg` (trình diễn kiến trúc & quy trình từng bước của 2 Agent Skills) |

### 3.2. Kết quả thực thi Checklist theo từng nền tảng (Task 1 & Task 3)

| Chỉ số | `P1` — Chrome 157 (Windows 11) | `P2` — Firefox 137/159 (Windows 11) | `P3` — Chrome Android 156/157 (OPPO Reno10 5G) | Tổng lượt (3 nền tảng) |
| :--- | :---: | :---: | :---: | :---: |
| **Item thiết kế** | 59 | 59 | 59 | **177** |
| **Đã chạy (Executed)** | 58 | 58 | 52 | **168** |
| **Passed** | 14 (24.14%) | 14 (24.14%) | 10 (19.23%) | **38** |
| **Failed** | 44 (75.86%) | 44 (75.86%) | 42 (80.77%) | **130** |
| **N/A (theo thiết kế `NA1`, `NA2`)** | 1 (`SV-20`) | 1 (`SV-20`) | 7 (`CL-10,31,37`, `SV-01,02,17,18`) | **9** |
| **Blocked** | 0 | 0 | 0 | **0** |
| **Chưa chạy** | 0 | 0 | 0 | **0** |

### 3.3. Phân bố thiết kế và kết quả theo Khía cạnh giao diện (`IA-01` .. `IA-04`)

| Mã IA | Khía cạnh giao diện | Số mục | `P1` (Pass / Fail / N/A) | `P2` (Pass / Fail / N/A) | `P3` (Pass / Fail / N/A) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`IA-01`** | General UI standards (Chuẩn giao diện chung) | **14** | 5 / 9 / 0 | 5 / 9 / 0 | 3 / 9 / 2 |
| **`IA-02`** | Forms (Biểu mẫu & Kiểm tra đầu vào) | **23** | 1 / 21 / 1 | 1 / 21 / 1 | 1 / 22 / 0 |
| **`IA-03`** | Navigation (Điều hướng & Bàn phím) | **12** | 4 / 8 / 0 | 4 / 8 / 0 | 2 / 6 / 4 |
| **`IA-04`** | Feedback / state (Phản hồi & Trạng thái) | **10** | 4 / 6 / 0 | 4 / 6 / 0 | 4 / 5 / 1 |
| **Tổng** | **Toàn bộ phạm vi M1** | **59** | **14 / 44 / 1** | **14 / 44 / 1** | **10 / 42 / 7** |

### 3.4. Phân bố theo Loại căn cứ (Test Basis) và Nguồn thiết kế (`AI` / `Both` / `SV`)

| Nhóm phân loại | Số mục | Tỷ lệ | `P1` (Pass / Fail / N/A) | `P2` (Pass / Fail / N/A) | `P3` (Pass / Fail / N/A) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Căn cứ `SRS`** (Đặc tả `FR-01..04`, `FR-21..24`, `SEC-04/07`) | 37 | 62.71% | 6 / 31 / 0 | 6 / 31 / 0 | 5 / 30 / 2 |
| **Căn cứ `Control`** (Checklist theo thành phần giao diện) | 10 | 16.95% | 4 / 5 / 1 | 4 / 5 / 1 | 3 / 4 / 3 |
| **Căn cứ `Heuristic`** (Nielsen, Shneiderman, WCAG 2.x) | 12 | 20.34% | 4 / 8 / 0 | 4 / 8 / 0 | 2 / 8 / 2 |
| **Nguồn `AI`** (AI đề xuất đạt chuẩn giữ lại) | 37 | 62.71% | 7 / 30 / 0 | 7 / 30 / 0 | 7 / 28 / 2 |
| **Nguồn `Both`** (AI đề xuất, SV hiệu chỉnh đáng kể) | 2 | 3.39% | 2 / 0 / 0 | 2 / 0 / 0 | 1 / 0 / 1 |
| **Nguồn `SV`** (SV tự phát hiện khoảng trống & bổ sung) | 20 | 33.90% | 5 / 14 / 1 | 5 / 14 / 1 | 2 / 14 / 4 |

### 3.5. Kết quả Đánh giá Khả năng Sử dụng (Task 2 — Luồng `F1`)

| Chỉ số đo lường (`n = 7` phiên chính thức `S01..S07`, tách riêng Pilot `S00`) | Giá trị thống kê | Tham chiếu hiện vật |
| :--- | :---: | :--- |
| **Điểm `SUS` trung bình ± Độ lệch chuẩn (`Mean ± SD`)** | **`48.6 ± 11.3`** (`Med: 47.5`, `30.0 – 67.5`) | Hạng **`F`** (`Poor` / `Not Acceptable`, lệch `-19.4` so với mốc `68.0`) — [`sus_and_metrics_summary.md`](usability/sus_and_metrics_summary.md) |
| **Độ dễ sau nhiệm vụ `SEQ` (`1..7`)** | **`3.43 ± 0.98`** (`Median: 3.0`) | Thấp hơn mốc chuẩn `~5.5` — [`participant_kit.md`](usability/participant_kit.md) |
| **Tỷ lệ hoàn thành độc lập vs Có cứu hộ lỗi chặn SUT** | **`3/7` (`42.9%`)** độc lập · **`4/7` (`57.1%`)** cứu hộ | Tổng `7/7 (100%)` đạt đích trong mốc `<= 05:00` (`Mean: 01:32 ± 00:36`) |
| **Mật độ ma sát trung bình (`E / H / A` mỗi phiên)** | **`4.57` lỗi / `0.57` do dự / `0.86` cứu hộ** | Tổng hợp `11` Findings (`7 Isolated Bugs` + `4 Systemic Design Issues`) — [`findings.md`](usability/findings.md) |
| **Lỗi mới phát hiện riêng nhờ hành vi người dùng thật** | **[`BUG-28`](bugs/BUG-28.md) ([GitHub Issue #28](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/28))** | Mất sạch SĐT & Địa chỉ trên `/profile` khi điều hướng SPA không nhấn `F5` (`S05` đối chứng `S07`) |

---

## 4. Bảng Tự Đánh Giá Điểm (Self-Assessment Table)

| No. | Criteria | Max Grade | Self-Assessed Grade | Notes / Evidence |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Task 1 — GUI Checklist** (design + execution + bug report) | **30** | **`30`** | [`checklist/M1_GUI_Checklist_And_Summary.xlsx`](checklist/M1_GUI_Checklist_And_Summary.xlsx), [`Bug_Report.md`](Bug_Report.md), `28` [GitHub Issues](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues) |
| **2** | **Task 2 — Usability Evaluation** (task scenario + 7 sessions + analysis) | **40** | **`40`** | [`usability/plan.md`](usability/plan.md), [`usability/participants.md`](usability/participants.md), [`usability/sessions/`](usability/sessions/), [`usability/recordings/LINKS.md`](usability/recordings/LINKS.md), [`usability/sus_and_metrics_summary.md`](usability/sus_and_metrics_summary.md), [`usability/findings.md`](usability/findings.md), [`Main_Report.md`](Main_Report.md) (§5) |
| **3** | **Task 3 — Cross-Browser / Cross-Platform** (>= 3 platforms) | **20** | **`20`** | [`screenshots/task3_cross_platform/`](screenshots/task3_cross_platform/) (`15` ảnh), [`checklist/runs/`](checklist/runs/), [`Main_Report.md`](Main_Report.md) (§4) |
| **4** | **Agent Skills** (skills + YouTube demo video) | **10** | **`10`** | [`.agents/skills/gui-checklist-testing/`](.agents/skills/gui-checklist-testing/), [`.agents/skills/usability-evaluation/`](.agents/skills/usability-evaluation/), [Video Demo YouTube](https://www.youtube.com/watch?v=3AzhYuL9wxg) |
| | **Total** | **100** | **`100`** | Đủ hiện vật bắt buộc theo Mục 14 đề bài (`23120199_HW03_AI_GUIUsability_100.zip`) |

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
├── Main_Report.md                         # Báo cáo chính (Task 1, Task 2, Task 3)
├── Bug_Report.md                          # Danh sách Bug phát hiện & liên kết GitHub Issues
├── AI_Critique_and_Audit_Report.md        # Phê bình AI (200-300 từ) & Nhật ký AI Audit Report
├── git_commit_log.txt                     # Lịch sử Git commit theo từng bước thực hiện
├── eshop-sut/                             # Mã nguồn hệ thống EShop (System Under Test)
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
├── usability/                             # Kế hoạch, Kịch bản, Danh sách 7 người tham gia & Phân tích SUS
├── screenshots/                           # Ảnh chụp minh chứng (Task 1 Failed, GitHub Issues, Task 3 Cross-Platform)
│   ├── task1_failed/                      # 130 ảnh minh chứng mục Failed trên P1 (44), P2 (44), P3 (42)
│   ├── task3_cross_platform/              # 12 ảnh tổng quan đa nền tảng trên P1, P2, P3
│   └── github_issues/                     # Ảnh chụp các trang GitHub Issues đã đăng
├── tests/                                 # Script kiểm tra dò tự động hỗ trợ đối chiếu trên 3 nền tảng
├── ai_log/
│   └── AI_Log.md                          # Nhật ký tương tác AI gộp chung nối tiếp (Entry 01..NN)
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
| **Số nền tảng thực thi (Platforms tested)** | **3** | `P1` Chrome 157 (Win 11), `P2` Firefox 137 (Win 11), `P3` Chrome Android 156 (OPPO Reno10 5G) |
| **Tổng số lượt kiểm tra đã thực thi (Executed checks)** | **168 / 177** | `P1`: 58/59, `P2`: 58/59, `P3`: 52/59 (9 lượt `N/A` có giả định `NA1`, `NA2`) |
| **Tổng kết quả lượt chạy (Passed / Failed / N/A / Blocked)** | **38 Passed / 130 Failed / 9 N/A / 0 Blocked** | `45 / 59` mục độc lập phát hiện lỗi (`Failed`) trên ít nhất 1 nền tảng (`14 / 59` mục `Passed` hoàn toàn) |
| **Tổng số Bugs đã báo cáo (GitHub Issues)** | **27 Bugs (`#1`..`#27`)** | `5 Critical`, `10 Major`, `11 Minor`, `1 Cosmetic` — [GitHub Issues](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues) & [`Bug_Report.md`](Bug_Report.md) |
| **Số người tham gia Usability (Participants)** | *Đang cập nhật (Task 2)* | 7 người thật ngoài lớp học (+ 1 phiên Pilot) |
| **Video Demo Agent Skills (YouTube)** | *Đang cập nhật (Task 4)* | Link video trình diễn end-to-end |

### 3.2. Kết quả thực thi Checklist theo từng nền tảng (Task 1 & Task 3)

| Chỉ số | `P1` — Chrome 157 (Windows 11) | `P2` — Firefox 137 (Windows 11) | `P3` — Chrome Android 156 (OPPO Reno10 5G) | Tổng lượt (3 nền tảng) |
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

---

## 4. Bảng Tự Đánh Giá Điểm (Self-Assessment Table)

| No. | Criteria | Max Grade | Self-Assessed Grade | Notes / Evidence |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Task 1 — GUI Checklist** (design + execution + bug report) | **30** | *TBD* | `./checklist/M1_GUI_Checklist_And_Summary.xlsx`, `./Bug_Report.md`, GitHub Issues |
| **2** | **Task 2 — Usability Evaluation** (task scenario + 7 sessions + analysis) | **40** | *TBD* | `./usability/` |
| **3** | **Task 3 — Cross-Browser / Cross-Platform** (>= 3 platforms) | **20** | *TBD* | `./screenshots/task3_cross_platform/`, `./checklist/runs/` |
| **4** | **Agent Skills** (skills + YouTube demo video) | **10** | *TBD* | `./.agents/skills/` |
| | **Total** | **100** | *TBD* | |

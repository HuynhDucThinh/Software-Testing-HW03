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
| **Màn hình bổ trợ (Task 1)** | `Login` (`FR-02`), `Forgot Password 2 bước` (`FR-03`), `Profile` (`FR-04`), Navbar khi đăng nhập |
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
├── checklist/                             # Thiết kế & Kết quả thực thi GUI Checklist (> 40 items)
├── usability/                             # Kế hoạch, Kịch bản, Danh sách 7 người tham gia & Phân tích SUS
├── screenshots/                           # Ảnh chụp minh chứng (Task 1 Failed, GitHub Issues, Task 3 Cross-Platform)
├── scripts/                               # Script hỗ trợ kiểm thử tự động
├── ai_log/                                # Nhật ký tương tác AI theo từng bước
├── bugs/                                  # Khung dữ kiện và chi tiết từng Bug
└── .agents/skills/                        # Agent Skills tái sử dụng cho GUI Checklist & Usability Evaluation
```

---

## 3. Báo Cáo Tóm Tắt Kiểm Thử (Test Summary Report)

| Chỉ số (Metric) | Kết quả (Value) | Ghi chú |
| :--- | :---: | :--- |
| **Số màn hình kiểm thử (Screens tested)** | *Đang cập nhật* | `Register`, `Login`, `ForgotPassword`, `Profile` (+ Navbar) |
| **Số luồng Usability (Flows tested)** | 1 | `F1`: Đăng ký $\rightarrow$ Đăng nhập $\rightarrow$ Cập nhật hồ sơ |
| **Số mục Checklist thiết kế (Designed items)** | *Đang cập nhật* | Mục tiêu $> 40$ items phủ đủ `IA-01`, `IA-02`, `IA-03`, `IA-04` |
| **Số mục đã thực thi (Executed items)** | *Đang cập nhật* | Thực thi trên $\ge 3$ nền tảng |
| **Số mục Passed / Failed** | *Đang cập nhật* | — |
| **Tổng số Bugs đã báo cáo (GitHub Issues)** | *Đang cập nhật* | Kèm ảnh chụp màn hình trên từng Issue |
| **Số người tham gia Usability (Participants)** | *Đang cập nhật* | 7 người thật ngoài lớp học (+ 1 phiên Pilot) |
| **Video Demo Agent Skills (YouTube)** | *Đang cập nhật* | Link video trình diễn end-to-end |

---

## 4. Bảng Tự Đánh Giá Điểm (Self-Assessment Table)

| No. | Criteria | Max Grade | Self-Assessed Grade | Notes / Evidence |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Task 1 — GUI Checklist** (design + execution + bug report) | **30** | *TBD* | `./checklist/`, `./Bug_Report.md`, GitHub Issues |
| **2** | **Task 2 — Usability Evaluation** (task scenario + 7 sessions + analysis) | **40** | *TBD* | `./usability/` |
| **3** | **Task 3 — Cross-Browser / Cross-Platform** ($\ge 3$ platforms) | **20** | *TBD* | `./screenshots/task3_cross_platform/` |
| **4** | **Agent Skills** (skills + YouTube demo video) | **10** | *TBD* | `./.agents/skills/` |
| | **Total** | **100** | *TBD* | |


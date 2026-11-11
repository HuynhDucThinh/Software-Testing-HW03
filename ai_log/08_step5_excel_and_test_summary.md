# 2026-11-11 - Task 1 Bước 5: Xuất sổ làm việc Excel 3 sheet và tổng hợp Test Summary Report

**Tool:** Antigravity
**Date and time:** 2026-11-11 17:20 +07:00
**Task / Step:** Task 1, Bước 5 (Xuất `checklist/M1_GUI_Checklist_And_Summary.xlsx`, cập nhật `M1_GUI_Checklist.md`, `README.md` và `Main_Report.md`)
**Prompt:**
Tiếp tục thực hiện bước 5 giúp tôi nhé.

**AI output:**
Đã hoàn thành Bước 5 của quy trình GUI Checklist cho phạm vi M1:
- Cập nhật `checklist/checklist.json` (`step: 5`, phiên bản `v5`) và chạy `build_excel.py` sinh sổ làm việc `checklist/M1_GUI_Checklist_And_Summary.xlsx` gồm đủ 3 sheet chuẩn:
  1. `Test Cases`: 59 dòng kiểm thử kèm đầy đủ `TC ID`, `Objective`, `IA`, `Màn hình`, `Precondition`, `Căn cứ`, `Expected`, kết quả và `Notes` thực tế trên `P1`/`P2`/`P3`, `Ưu tiên`, `Nguồn`, `Loại lỗi` và cột giải thích `Vì sao AI bỏ sót` cho toàn bộ 20 mục `SV`.
  2. `Checklist`: bảng thực thi rút gọn có Data Validation dropdown (`Passed,Failed,N/A,Blocked`) trên cả 3 cột `P1`, `P2`, `P3`.
  3. `Test Summary Report`: bảng tổng hợp dùng công thức động (`ROWS`, `COUNTA-COUNTIF`, `COUNTIF`, `COUNTBLANK` với `fullCalcOnLoad=True`) đối chiếu trực tiếp sang vùng `Checklist!G5:I63`, kèm thống kê theo `IA-01..IA-04`, loại căn cứ (`SRS`, `Control`, `Heuristic`) và nguồn thiết kế (`AI`, `Both`, `SV`).
- Chạy lại `render_checklist.py` đồng bộ `checklist/M1_GUI_Checklist.md` và kiểm tra bằng `coverage_matrix.py` + `check_checklist.py --min 41 --min-per-ia 8` (`0 lỗi, 0 cảnh báo`).
- Tổng hợp đầy đủ các bảng số liệu Test Summary (`59` mục thiết kế; `168/177` lượt thực thi trên 3 nền tảng; `38 Passed / 130 Failed / 9 N/A / 0 Blocked`, trong đó `P1`: `14P/44F/1NA`, `P2`: `14P/44F/1NA`, `P3`: `10P/42F/7NA`; `45/59` mục độc lập phát hiện lỗi và `15/20` mục do SV bổ sung bắt được lỗi thật) sang `README.md` và khởi tạo báo cáo chính `Main_Report.md` (hoàn chỉnh phần Task 1 & Task 3).

**Kept:** Giữ nguyên file `checklist/M1_GUI_Checklist_And_Summary.xlsx`, `checklist/M1_GUI_Checklist.md`, các bảng thống kê trong `README.md` và nội dung phần Task 1, Task 3 trong `Main_Report.md`.
**Changed:** Chưa cần chỉnh sửa; các mục chờ số liệu của Bước 6 (số lượng GitHub Issues) và Task 2 (7 phiên Usability & SUS) đã được đánh dấu rõ để điền tiếp ở các bước kế tiếp.
**Rejected:** Không có.
**By hand:** Sinh viên kiểm tra đối chiếu số liệu thống kê giữa file Excel, `README.md` và `Main_Report.md` trước khi chuyển sang Bước 6 (gom dữ kiện bug và tạo GitHub Issues).

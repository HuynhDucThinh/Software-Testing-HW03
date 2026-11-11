---
name: gui-checklist-testing
description: Thiết kế, review, thực thi GUI checklist (Task 1 HW03) cho phạm vi M1 của EShop (Register, Login, Forgot Password, Profile, Header). Dẫn AI qua từng bước theo bài giảng GUI checklist (3 nguồn - đặc tả UI, checklist theo control, heuristic), mỗi item có ngưỡng Pass/Fail quan sát được, chạy trên ít nhất 3 nền tảng, xuất Excel + Test Summary, gom dữ kiện bug và ghi AI Audit. Mỗi lần gọi chỉ làm một bước rồi dừng. Dùng khi người dùng nói "GUI checklist", "checklist giao diện", "kiểm thử giao diện", "cross-browser", "IA-01...IA-04", hoặc gọi skill kèm số bước.
---

# GUI checklist theo từng bước (HW03 - Task 1)

Skill dẫn AI đi qua kỹ thuật **checklist testing** của bài giảng. **Mỗi lần gọi chỉ làm một bước rồi dừng** để sinh viên (SV) review và commit. Không gộp cả kỹ thuật vào một lượt: đề chấm việc dẫn AI từng bước và việc SV review.

Toàn bộ dữ liệu của phạm vi nằm trong **một file** `checklist/checklist.json` (schema: `references/schema-checklist.md`). Bảng Markdown, Excel, Test Summary, khung bug đều sinh từ file này nên số liệu luôn khớp.

Phạm vi M1: màn hình chính `Register`; màn phụ `Login`, `ForgotPassword` (2 bước), `Profile`, `Header/Navbar` khi đã đăng nhập. SUT: `eshop-sut/` (web `http://localhost:5173`, API `http://localhost:3000`).

## Quy tắc bắt buộc

1. **Đọc test basis thật trước khi viết.** Đặc tả UI nằm ở `eshop-sut/README.md` (FR-01..04, FR-21..24). Mã UI nằm ở `eshop-sut/frontend-web/src/pages/*.jsx`. Không bịa control, nhãn, route.
2. **Đặc tả là oracle. Mã chỉ để biết control nào tồn tại.** Expected lấy từ đặc tả, heuristic hoặc checklist bài giảng, không lấy từ hành vi hiện tại của mã. Không chạy SUT để chỉnh Expected theo cái quan sát được. Chỗ đặc tả im lặng thì ghi giả định `GAx` trong `assumptions`.
3. **Expected theo công thức của slide:** `[Thành phần giao diện] + [Thao tác / điều kiện] + [Kết quả thị giác mong đợi]`, kết thúc bằng một câu `Fail nếu ...` có ngưỡng đo được (DevTools, mắt thường, px, giây).
4. **Không trùng.** Mỗi thuộc tính chung (màu nút, ký hiệu tiền...) khẳng định ở một item.
5. **N/A phải có giả định.** Nền tảng không áp dụng thì bỏ khỏi `nen_tang` và ghi lý do trong `na` (mã `NAx` trong `assumptions`).
6. **Đóng băng output AI** sau mỗi bước AI (`scripts/freeze.py`) trước khi SV sửa. Không sửa file đã đóng băng.
7. **Nguồn từng item:** `nguon` = `AI` / `SV` / `Both` (AI đề xuất, SV sửa đáng kể).
8. **Bước 2: AI không gợi ý** item hay khía cạnh nào. Chỉ giải thích "vì sao AI bỏ sót" sau khi SV đã commit item của mình, nếu SV hỏi.
9. **Verdict chính thức = lượt SV chạy tay** trên trình duyệt/thiết bị thật. Lượt Playwright (nếu dùng) chỉ ghi `auto_status`. Mục thuần thị giác (màu, bố cục, cảm nhận) do SV chấm bằng mắt. AI chỉ chạy `dom_probe.js`, đọc DOM, gộp kết quả.
10. **Assertion phải kiểm tra phần tử đang hiển thị** (không chỉ có trong DOM) để tránh false positive (slide 19). Mỗi lượt bắt đầu từ trạng thái sạch (restart backend, seed lại).
11. **Ảnh chỉ cho item Failed** (mục Passed/N/A không chụp). Cross-platform: thêm 1 ảnh tổng quan mỗi màn hình mỗi nền tảng. Mọi ảnh phải thấy tên trình duyệt/thiết bị, URL `localhost`, overlay email sinh viên, và form hiển thị **MSSV + họ tên** (mục 6 và 11 của đề). **AI không tạo hay ghép overlay**, chỉ kiểm tra, đổi tên, nén.
12. **Bug report do SV viết.** AI chỉ gom dữ kiện (`scripts/bug_skeleton.py`). Không viết mô tả bug thay SV.
13. **Ghi AI Audit mỗi lần dùng AI** (`assets/ai_log_template.md`): công cụ, ngày giờ, prompt nguyên văn, output. Không dùng prompt kiểu "làm toàn bộ cho tôi"; mỗi prompt nêu rõ bước và IA.
14. **Mỗi bước một Git commit** (quy ước ở cuối file). Quy định khoá học và `CLAUDE.md`/`AGENTS.md` thắng skill này khi mâu thuẫn.

## Các bước

Gọi: `Dùng skill gui-checklist-testing, bước <n>` (thư mục làm việc `checklist/`). Thiếu số bước thì đọc `meta.step` trong `checklist.json` để biết bước kế và hỏi lại.

### Bước 0 - Khảo sát
- Điền `checklist/m1_inventory.md` (khung: `references/m1-inventory.md`): với mỗi màn hình liệt kê control (loại, nhãn, `type`, `required`, thông báo thật, file:dòng).
- Điền `checklist/m1_test_basis.md` (khung: `references/m1-test-basis.md`): trích nguyên văn điều khoản UI của FR-01..04, FR-21..24 kèm số dòng `eshop-sut/README.md`.
- Tạo `checklist/checklist.json` với `meta` (scope, sut_version, test_basis, platforms, inventory, version, step), `assumptions` và `items` rỗng. Dừng.

### Bước 1 - AI nháp checklist theo 3 nguồn
- **Đọc `references/slide-checklist.md` trước khi sinh item**, không sinh từ trí nhớ về heuristic.
- Chạy **4 lượt riêng**, mỗi lượt một IA (IA-01, IA-02, IA-03, IA-04), mỗi lượt một prompt ghi vào AI log.
- Nguồn item: (a) điều khoản đặc tả (`loai_nguon: SRS`), (b) checklist theo control (`Control`), (c) heuristic Nielsen/Norman/Shneiderman và WCAG khi đặc tả im lặng (`Heuristic`).
- Mỗi item: `id` CL-xx, `ia`, `man_hinh`, `muc_kiem_tra`, `can_cu`, `loai_nguon`, `expected` (công thức + "Fail nếu"), `uu_tien`, `nen_tang`, `nguon: "AI"`; tuỳ chọn `loai_loi`, `du_lieu`, `tien_dieu_kien`, `gia_dinh`, `na`.
- Mục tiêu nháp AI: 30 đến 40 item, đủ 4 IA.
- `render_checklist.py` -> `freeze.py --step 1` -> `check_checklist.py`. Dừng.

### Bước 2 - SV bổ sung + gap analysis
- SV tự mở `checklist/sv_items.md` (khung `assets/sv_items_template.md`) và tự viết item còn thiếu. **AI không gợi ý.**
- Nhóm điểm mù AI thường bỏ sót (slide 12) mà SV nên tự rà: accessibility bằng bàn phím, dark mode, RTL, đa ngôn ngữ; cùng các điểm riêng của M1 (giá trị biên SĐT và mật khẩu, thứ tự Tab, vị trí thông báo lỗi, HTML trong tên ở Header). Danh sách này chỉ nhắc SV, AI không điền item.
- Mỗi item SV có `ly_do_ai_bo_sot` (loai: prompt / giới hạn model / đặc điểm giao diện / khác, kèm 1 đến 3 câu giải thích do SV viết).
- Sau khi SV commit: AI kiểm cấu trúc (chỉ đọc), chép nguyên văn vào JSON (id `SV-xx`); trường trống thì ghi `(SV chưa ghi)` và `check_checklist.py` báo lỗi tới khi SV điền.
- `scripts/coverage_matrix.py` in ma trận độ phủ (IA x nhóm slide x loại nguồn). Chỉ in số lượng, không đề xuất item.
- Tổng số item phải **lớn hơn 40**, mục tiêu 55 đến 65.
- `render_checklist.py` + `check_checklist.py --min 41 --min-per-ia 8`. Dừng.

### Bước 3 - Chuẩn bị chạy (RUN.md + dom_probe.js)
- Điền `checklist/RUN.md` từ `assets/RUN_template.md`: lệnh khởi động SUT, tài khoản, thứ tự nhóm item (gom theo tiền điều kiện để ít restart), quy tắc ảnh, danh sách kiểm trước khi chụp, cách ghi kết quả vào `runs/<Px>_<YYYYMMDD-HHMM>.csv`.
- Phân loại cách chạy (`che_do`): `auto` / `manual` / `mixed`. Mặc định M1 chạy `manual` kèm `dom_probe.js`.
- Chép `assets/dom_probe.js` vào `checklist/`, dán vào DevTools Console từng trang. Script chỉ đọc DOM, in JSON dữ kiện, không kết luận Pass/Fail.
- Procedure phải khớp cách chạy thật trước khi chạy. Sửa thì freeze lại, Expected không đổi. Dừng.

### Bước 4 - Chạy từng nền tảng + gộp
- SV chạy tay ít nhất **3 nền tảng**: P1 Chrome, P2 Firefox, P3 một trong Safari (BrowserStack/LambdaTest), Android Chrome, hoặc Expo Go trên điện thoại thật.
- Mỗi nền tảng: restart backend, chạy toàn bộ item áp dụng, ghi `runs/<Px>_<ts>.csv` với header `id,status,notes,evidence`. Item Failed ghi Actual nguyên văn trong `notes` và ảnh `P<n>_<id>.png` có overlay.
- Gộp: `merge_platform.py checklist/checklist.json checklist/runs/<file>.csv --platform Px --dry-run`, kiểm tra rồi chạy lại không có `--dry-run`.
- `check_checklist.py`: mọi item Failed có notes và ảnh. Một nền tảng một commit. Dừng.

### Bước 5 - Excel + Test Summary
- `build_excel.py checklist/checklist.json -o checklist/M1_GUI_Checklist_And_Summary.xlsx --tester "<họ tên - MSSV>"`: 3 sheet Test Cases / Checklist / Test Summary Report, cột theo nền tảng, cột Notes, cột lý do AI bỏ sót, công thức đếm.
- `render_checklist.py` sinh `checklist/M1_GUI_Checklist.md`.
- Chép bảng tổng (thiết kế / đã chạy / Passed / Failed theo nền tảng, theo IA, theo nguồn) sang `README.md` và báo cáo chính. Dừng.

### Bước 6 - Gom dữ kiện bug
- `bug_skeleton.py checklist/checklist.json --out bugs/` liệt kê item x nền tảng Failed, gom theo dữ kiện giống nhau (cùng phần tử, cùng hành vi) và sinh khung `BUG-<n>.md` chỉ chứa dữ kiện chép lại (item, nền tảng, môi trường, Expected, Actual, ảnh). Tiêu đề, mô tả, steps, severity để trống cho SV.
- SV viết bug (mẫu `assets/bug_template.md`), đăng GitHub Issues (đính ảnh), chụp trang issue vào `screenshots/github_issues/`, ghi vào `Bug_Report.md`. Dừng.

### Bước 7 - Phụ lục AI và nộp
- `ai_audit_export.py ai_log/ -o AI_Critique_and_Audit_Report.md`: gom các entry AI log thành AI Audit Report (công cụ, ngày giờ, prompt, output, phần giữ / sửa / loại).
- SV tự viết AI Critique rồi chạy `word_count.py <file> --min 200 --max 300`.
- Xuất PDF cho báo cáo chính và phụ lục AI, xuất `git log --date=iso-strict --pretty=fuller > git_commit_log.txt`. Dừng.

## Script

| Script | Việc |
|---|---|
| `scripts/check_checklist.py <json> [--min 41] [--min-per-ia 8]` | Kiểm schema, id, đủ 4 IA, số item, 3 nguồn, N/A có giả định, trùng mục, ngưỡng "Fail nếu", item SV có lý do AI bỏ sót, Failed có notes và ảnh. Mã thoát khác 0 khi có lỗi |
| `scripts/freeze.py <json> --step k --out <dir>` | Đóng băng json và md, có timestamp, không ghi đè, ghi `INDEX.md` |
| `scripts/render_checklist.py <json> -o <md>` | Bảng theo IA, thống kê, giả định, cột kết quả từng nền tảng |
| `scripts/merge_platform.py <json> <lượt.csv/json> --platform Px [--dry-run] [--force]` | Gộp một lượt chạy |
| `scripts/build_excel.py <json> -o <xlsx> [--tester ...]` | Excel 3 sheet (cần `openpyxl`) |
| `scripts/coverage_matrix.py <json>` | Ma trận độ phủ, chỉ in số lượng |
| `scripts/bug_skeleton.py <json> --out <dir>` | Danh sách Failed, gom nhóm, khung bug chỉ dữ kiện |
| `scripts/ai_audit_export.py <dir> -o <md>` | Gom AI log thành AI Audit Report |
| `scripts/word_count.py <file> --min --max` | Đếm từ AI Critique |

## Quy ước verdict

- Lệch Expected -> **Failed** (notes ghi Actual nguyên văn + lý do). Bị lỗi khác chặn thì **Blocked** + item gốc trong notes.
- Nền tảng không áp dụng (theo `na`) -> **N/A**. N/A không có giả định là lỗi check.
- Expected sai phát hiện sau khi có Actual -> không sửa Expected; ghi "Failed do lỗi thiết kế item, không lập bug".
- Lượt chính thức = chạy toàn bộ trên một nền tảng sau khi reset dữ liệu; ghi nhật ký trong `RUN.md`.

## Quy ước Git commit

| Bước | Thông điệp commit |
|---|---|
| 0 | `docs(task1): M1 inventory and test basis` |
| 1 | `feat(task1): AI draft GUI checklist` |
| 2 | `feat(task1): SV items and AI gap reasons` |
| 3 | `docs(task1): run guide and DOM probe` |
| 4 | `test(task1): execute checklist on <nền tảng>` (mỗi nền tảng một commit) |
| 5 | `test(task1): Excel checklist and test summary` |
| 6 | `docs(task1): bug reports and GitHub issues` |
| 7 | `docs: AI audit, critique and git log` |


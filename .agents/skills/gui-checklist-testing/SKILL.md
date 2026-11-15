---
name: gui-checklist-testing
description: Thiết kế, review, thực thi GUI checklist và kiểm thử đa nền tảng (Task 1 & Task 3 HW03) tái sử dụng linh hoạt cho mọi nhóm màn hình Web/Mobile (kèm mẫu tham chiếu đầy đủ cho phạm vi M1 của EShop: Register, Login, Forgot Password, Profile, Header). Dẫn dắt AI qua từng bước kỷ luật theo bài giảng GUI checklist (3 nguồn - đặc tả UI, checklist theo control, heuristic), mỗi item có ngưỡng Pass/Fail quan sát được, chạy trên ít nhất 3 nền tảng, xuất Excel + Test Summary, gom dữ kiện bug và ghi AI Audit. Mỗi lần gọi chỉ làm một bước rồi dừng. Dùng khi người dùng nói "GUI checklist", "checklist giao diện", "kiểm thử giao diện", "cross-browser", "IA-01...IA-04", hoặc gọi skill kèm số bước.
---

# GUI checklist theo từng bước (HW03 - Task 1 & Task 3)

Skill dẫn AI đi qua kỹ thuật **checklist testing** và **cross-platform testing** của bài giảng. **Mỗi lần gọi chỉ làm một bước rồi dừng** để sinh viên (SV) review và tạo Git commit riêng. Không gộp cả kỹ thuật vào một lượt: đề chấm việc dẫn AI từng bước có kỷ luật và việc SV trực tiếp kiểm duyệt (`Human review`).

Toàn bộ dữ liệu của một phạm vi kiểm thử nằm trong **một nguồn chân lý duy nhất** `checklist/checklist.json` (schema tổng quát cho mọi nhóm màn hình tại `references/schema-checklist.md`). Bảng Markdown, sổ làm việc Excel 3 sheet, Test Summary, khung gom nhóm bug đều sinh tự động từ file này nên số liệu luôn khớp tuyệt đối.

**Khả năng tái sử dụng đa màn hình (`Reusable across screens`):** Tham số hóa cho bất kỳ nhóm màn hình nào (`<scope>`: ví dụ `M1` Auth & Profile, `M2` Home & ProductDetail, `M3` Cart & Checkout, `M4` Web Admin, `M5` Mobile App). Trong `references/m1-inventory.md` và `references/m1-test-basis.md` đính kèm sẵn mẫu khảo sát thực tế của phạm vi `M1` trên SUT `eshop-sut/` (web `http://localhost:5173`, API `http://localhost:3000`).

## Quy tắc bắt buộc

1. **Đọc test basis thật trước khi viết.** Đặc tả UI nằm ở `eshop-sut/README.md` (FR-01..04, FR-21..24). Mã UI nằm ở `eshop-sut/frontend-web/src/pages/*.jsx`. Không bịa control, nhãn, route.
2. **Đặc tả là oracle. Mã chỉ để biết control nào tồn tại.** Expected lấy từ đặc tả, heuristic hoặc checklist bài giảng, không lấy từ hành vi hiện tại của mã. Không chạy SUT để chỉnh Expected theo cái quan sát được. Chỗ đặc tả im lặng thì ghi giả định `GAx` trong `assumptions`.
3. **Expected theo công thức của slide:** `[Thành phần giao diện] + [Thao tác / điều kiện] + [Kết quả thị giác mong đợi]`, kết thúc bằng một câu `Fail nếu ...` có ngưỡng đo được (DevTools, mắt thường, px, giây).
4. **Không trùng.** Mỗi thuộc tính chung (màu nút, ký hiệu tiền...) khẳng định ở một item.
5. **N/A phải có giả định.** Nền tảng không áp dụng thì bỏ khỏi `nen_tang` và ghi lý do trong `na` (mã `NAx` trong `assumptions`).
6. **Đóng băng output AI** sau mỗi bước AI (`scripts/freeze.py`) trước khi SV sửa. Không sửa file đã đóng băng.
7. **Nguồn từng item:** `nguon` = `AI` / `SV` / `Both` (AI đề xuất, SV sửa đáng kể).
8. **Bước 2: AI không gợi ý** item hay khía cạnh nào. Chỉ giải thích "vì sao AI bỏ sót" sau khi SV đã commit item của mình, nếu SV hỏi.
9. **Chế độ thực thi minh bạch (`manual` hoặc `mixed`) & Kiểm duyệt của SV:** Cho phép chạy thủ công kết hợp `dom_probe.js` (`che_do: "manual"`) hoặc kết hợp Playwright / CDP trên trình duyệt và thiết bị vật lý thật để đo khách quan DOM/CSS/Network ở `auto_status` (`che_do: "mixed"`). Trong mọi trường hợp, SV phải trực tiếp chuẩn bị môi trường sạch, quan sát các mục phụ thuộc phần cứng/thị giác (ví dụ bàn phím cảm ứng di động, bố cục tràn ngang) và rà soát đối chiếu số đo cùng ảnh minh chứng trước khi chốt `ket_qua` chính thức.
10. **Assertion phải kiểm tra phần tử đang hiển thị** (không chỉ có trong DOM) để tránh false positive (slide 19). Mỗi lượt bắt đầu từ trạng thái sạch (restart backend, seed lại).
11. **Ảnh minh chứng thật & Quy tắc chống gian lận (Mục 6 & Mục 11):** Ảnh `task1_failed/` **chỉ chụp cho item `Failed`** (mỗi mục trên mỗi nền tảng một ảnh riêng có mã băm `MD5` duy nhất; mục `Passed`/`N/A` không chụp). Ảnh `task3_cross_platform/` chụp nguyên màn hình cấp hệ điều hành / thiết bị thật cho mỗi màn hình trên mỗi nền tảng, hiển thị rõ trình duyệt/OS/thiết bị, URL `localhost` và chuỗi **MSSV + họ tên** điền trên biểu mẫu. Tuyệt đối **không vẽ giả giao diện, thanh địa chỉ hay hộp thoại `window.alert()`**; được phép dùng công cụ/script đóng dấu lớp phủ email sinh viên đồng bộ trên ảnh chụp thật và ghép dải chú thích thông số bên ngoài vùng ảnh trang.
12. **Gom nhóm chống trùng lặp & Kiểm duyệt Bug Report:** Chạy `scripts/bug_skeleton.py` để gom các mục `Failed` có cùng nguyên nhân gốc thành bộ Bug không trùng lặp. Dưới chính sách `AI Policy: Open`, AI được hỗ trợ soạn nháp hồ sơ Bug từ dữ kiện `Expected`/`Actual` thực tế và hỗ trợ đồng bộ GitHub Issues, nhưng **SV bắt buộc rà soát, hiệu đính chính xác từng thông số kỹ thuật, mức `Severity` và kiểm chứng trực tiếp trên trang GitHub Issues** (tuân thủ Mục 2 `Human review`).
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
- Phân loại cách chạy (`che_do`): `manual` / `mixed` / `auto` kèm `che_do_ghi_chu` nêu rõ phần đo tự động và phần SV kiểm chứng trực tiếp.
- Chép `assets/dom_probe.js` vào `checklist/`, dán vào DevTools Console từng trang. Script chỉ đọc DOM, in JSON dữ kiện, không kết luận Pass/Fail.
- Procedure phải khớp cách chạy thật trước khi chạy. Sửa thì freeze lại, Expected không đổi. Dừng.

### Bước 4 - Chạy từng nền tảng + gộp
- Thực thi trên ít nhất **3 nền tảng** (`P1` Chrome, `P2` Firefox, `P3` một trong Safari trên BrowserStack/LambdaTest, Android Chrome, hoặc Expo Go trên điện thoại thật) theo chế độ `manual` hoặc `mixed` đã công khai.
- Mỗi nền tảng: restart backend về trạng thái seed sạch, thực thi toàn bộ item áp dụng, ghi `runs/<Px>_<ts>.csv` với header `id,status,notes,evidence`. Item `Failed` ghi `Actual` nguyên văn trong `notes` và đính kèm ảnh chụp riêng từng mục `P<n>_<id>.png` có lớp phủ email sinh viên.
- Gộp: `merge_platform.py checklist/checklist.json checklist/runs/<file>.csv --platform Px --dry-run`, SV rà soát kết quả rồi chạy lại không có `--dry-run`.
- `check_checklist.py`: mọi item `Failed` có `notes` và ảnh tồn tại trên ổ đĩa. Một nền tảng một commit. Dừng.

### Bước 5 - Excel + Test Summary
- `build_excel.py checklist/checklist.json -o checklist/<Scope>_GUI_Checklist_And_Summary.xlsx --tester "<họ tên - MSSV>"`: 3 sheet `Test Cases` / `Checklist` / `Test Summary Report`, cột theo nền tảng, cột `Notes`, cột lý do AI bỏ sót, hyperlink ảnh minh chứng và công thức đếm tự động.
- `render_checklist.py` sinh `checklist/<Scope>_GUI_Checklist.md`.
- Chép bảng tổng (thiết kế / đã chạy / Passed / Failed theo nền tảng, theo IA, theo nguồn) sang `README.md` và báo cáo chính. Dừng.

### Bước 6 - Gom dữ kiện & Lập báo cáo Bug
- `bug_skeleton.py checklist/checklist.json --out bugs/` liệt kê item x nền tảng `Failed`, gom theo nguyên nhân gốc chống trùng lặp và sinh khung dữ kiện `BUG-<n>.md` (item, nền tảng, môi trường, Expected, Actual, ảnh).
- Hoàn thiện hồ sơ chi tiết từng Bug (`assets/bug_template.md`), SV kiểm duyệt toàn bộ nội dung kỹ thuật và mức `Severity`, đăng lên GitHub Issues kèm ảnh minh chứng, chụp trang issue vào `screenshots/github_issues/` và đồng bộ `Bug_Report.md`. Dừng.

### Bước 7 - Phụ lục AI và nộp
- Ghi nhận đầy đủ nhật ký tương tác AI nối tiếp tại `ai_log/AI_Log.md`.
- SV tự viết hoặc trực tiếp biên tập, hiệu đính đoạn `AI Critique` (`ai_log/critique.md`) phản ánh trải nghiệm thực tế, kiểm đếm bằng `word_count.py <file> --section "AI Critique" --min 200 --max 300`.
- `ai_audit_export.py ai_log -o AI_Critique_and_Audit_Report.md --student "<họ tên - MSSV (email)>" --critique ai_log/critique.md`: kết xuất báo cáo Phê bình & Kiểm toán AI hoàn chỉnh.
- Xuất PDF cho báo cáo chính và phụ lục AI, xuất `git log --date=iso-strict --stat --pretty=fuller > git_commit_log.txt`. Dừng.

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


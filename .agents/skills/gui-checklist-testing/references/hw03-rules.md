# Quy định HW03 áp dụng cho Task 1, Task 3 và phụ lục

Nguồn: `docs/2026.HW03.GUI Usability_En.md`. Dùng để AI tự đối chiếu trước khi báo hoàn thành mỗi bước.

## Nguyên tắc (mục 2)

| Quy định | Cách tuân thủ trong skill |
|---|---|
| AI-First nhưng không dùng một prompt chung chung | Bước 1 chạy 4 lượt riêng theo IA; mỗi lượt một prompt ghi vào AI log |
| Human review: sửa và bổ sung, không nộp output thô | Bước 2 do SV tự viết; output AI được đóng băng trước khi sửa |
| AI Audit Report ghi toàn bộ quá trình dùng AI | `assets/ai_log_template.md` + `scripts/ai_audit_export.py` |
| Tài liệu hóa bằng Markdown | Mọi sản phẩm là `.md`, `.json`, `.csv`; Excel và PDF xuất từ chúng |
| Chất lượng hơn hoàn thành: số lượng và chất lượng checklist, bug, ảnh | Cổng `check_checklist.py`; ảnh theo quy tắc; bug có steps, expected, actual |

## Task 1 (mục 6)

- Checklist **lớn hơn 40 item** bao phủ đủ IA-01, IA-02, IA-03, IA-04.
- Dùng AI tạo bộ ban đầu, sau đó review và **bổ sung item AI bỏ sót**; mỗi item bổ sung **giải thích vì sao AI bỏ sót** (chất lượng prompt, giới hạn mô hình, đặc điểm giao diện).
- Thực thi: Passed hoặc Failed; cột **Notes** ghi lý do cho item Failed; **ảnh chỉ cho item Failed**.
- Báo lỗi ở **cả** Markdown và GitHub Issues; mỗi issue có ảnh.

## Task 3 (mục 6)

- Thực hiện Task 1 trên **ít nhất 3 nền tảng**: Chrome, Firefox, Safari (hoặc Android Chrome). Expo Go trên điện thoại thật thay được một nền tảng.
- Ưu tiên BrowserStack hoặc LambdaTest. Nếu hết trial: Sauce Labs, CrossBrowserTesting hoặc thiết bị thật, ảnh phải thấy tên trình duyệt/OS/thiết bị và URL `localhost`.
- Mỗi ảnh có overlay **email sinh viên**. Ảnh cross-platform phải có **MSSV và họ tên trong form** (mục 11).

## Nộp bài (mục 12, 14)

- Mỗi bước kiểm thử một Git commit; xuất commit log dạng text.
- Gói nộp: báo cáo chính (Markdown + PDF), bug report có ảnh GitHub Issues, AI Critique + AI Audit Report (Markdown + PDF), `git_commit_log.txt`, Excel checklist (hơn 40 item) và test summary, bằng chứng usability, ảnh cross-platform, `README.md` có bảng tự đánh giá và test summary.
- Thiếu tài liệu bắt buộc: 0 điểm. Sao chép giữa sinh viên, kể cả prompt: 0 điểm cả hai.

## AI Critique (mục 10)

- 200 đến 300 từ. Trả lời: AI sai, thiên lệch hoặc thiếu ở đâu; vì sao không phát hiện; nguyên tắc cộng tác rút ra. Kiểm bằng `scripts/word_count.py`.

## Không được AI làm hoặc bịa (mục 11)

- Danh sách 7 người tham gia usability; ảnh cross-platform có MSSV, họ tên, email. AI không tạo, ghép hay chỉnh các thông tin này.


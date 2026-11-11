# Nguồn checklist từ bài giảng (slide Nhóm 05) và ánh xạ vào IA

Đọc toàn bộ file này **trước khi sinh item ở Bước 1**. Nguồn: `docs/Nhom05_GUI_Testing_Slides.md` (Slide 9 đến 12, 15, 18 đến 20, 31). Phần heuristic ở mục 6 là kiến thức chung; SV đối chiếu với bài giảng "Where checklists come from" của lớp và sửa nếu khác.

## 1. Công thức viết item (Slide 12)

`[Thành phần thị giác] + [Thao tác / điều kiện] + [Kết quả thị giác mong đợi] -> đo lường PASS / FAIL`

Ví dụ khuôn: "Ô Email trên `/register` + quan sát thuộc tính `type` trong DevTools + `type="email"`. Fail nếu `type` khác `email`."

## 2. 19 checkpoint của checklist mẫu (Slide 10) và IA tương ứng

| # | Nhóm | Checkpoint | Tiêu chí | IA gợi ý |
|---|---|---|---|---|
| 1 | Visual Consistency | Alignment | Nhãn, ô nhập, tiêu đề, nút căn thẳng theo lưới | IA-01 |
| 2 | Visual Consistency | Color and Palette | Màu chữ, nền, giao diện nhất quán giữa các màn hình | IA-01 |
| 3 | Visual Consistency | Typography and Content | Chữ và thông báo hệ thống không lỗi chính tả, ngữ pháp | IA-01 |
| 4 | Visual Consistency | Data Formatting | Định dạng ngày, giờ, số nhất quán | IA-01 |
| 5 | Controls and Inputs | Field Limits | Ô nhập giới hạn độ dài và chuỗi hợp lệ | IA-02 |
| 6 | Controls and Inputs | Disabled States | Ô chỉ đọc, bị vô hiệu hóa khác biệt thị giác (xám) | IA-02 |
| 7 | Controls and Inputs | Assistive Hints | Placeholder, tooltip hữu ích, rõ nghĩa | IA-02 |
| 8 | Controls and Inputs | Selection Controls | Checkbox, radio, dropdown có trạng thái mặc định rõ | IA-02 |
| 9 | Navigation and Usability | Tab Order | Tab và Shift+Tab đi theo thứ tự hợp lý | IA-03 |
| 10 | Navigation and Usability | Default Actions | Form có nút mặc định phù hợp (Enter) | IA-03 |
| 11 | Navigation and Usability | Keyboard Support | Phím tắt và thao tác bàn phím nhất quán | IA-03 |
| 12 | Navigation and Usability | Hover and Focus | Link, nút có phản hồi thị giác khi hover/focus | IA-03 |
| 13 | Feedback and Safety | Processing States | Chỉ báo đang xử lý, trở lại bình thường khi xong | IA-04 |
| 14 | Feedback and Safety | Destructive Safeguards | Xác nhận trước khi thay đổi vĩnh viễn | IA-04 |
| 15 | Feedback and Safety | Error Messages | Lỗi rõ ràng, không thuật ngữ kỹ thuật, không đổ lỗi người dùng | IA-04 |
| 16 | Feedback and Safety | Input Validation | Nhập sai có dấu hiệu cục bộ (viền đỏ, nhãn lỗi) | IA-02/IA-04 |
| 17 | Responsive Display | Breakpoint Layout | Bố cục co giãn đúng ở các độ phân giải | IA-01 |
| 18 | Responsive Display | Element Overlap | Bảng nổi, ảnh không che nút hay nhãn | IA-01 |
| 19 | Responsive Display | Scroll Boundaries | Không có thanh cuộn ngang ngoài ý muốn | IA-01 |

Dùng làm nguồn `loai_nguon: Control` khi control có thật trong inventory.

## 3. Bốn interface aspect của đề (Slide 11)

- IA-01 General UI standards: căn hàng, màu sắc, hiển thị trên mobile và desktop.
- IA-02 Forms and controls: ô nhập, nút kiểm soát điều kiện, báo lỗi rõ khi nhập sai.
- IA-03 Navigation: menu, đường dẫn trang, phân trang, phím Tab đi đúng luồng.
- IA-04 Feedback and state: loading, nút disabled chống bấm đúp, hộp thoại xác nhận, toast.

## 4. Bốn nhóm lỗi GUI (Slide 9) - dùng cho trường `loai_loi`

| Giá trị `loai_loi` | Ý nghĩa |
|---|---|
| `Visual-Layout` | Sắp xếp, kích thước, hiển thị thành phần |
| `State` | Trạng thái thành phần khi tương tác, cập nhật dữ liệu |
| `Responsive` | Bố cục và hiển thị trên kích thước màn hình khác nhau |
| `Typo-Localization` | Chính tả, nội dung, ngôn ngữ hiển thị |

## 5. Nguyên tắc thiết kế (Slide 6 đến 8)

- Consistency: bộ màu, phông chữ đồng nhất mọi màn hình.
- Error prevention: chốt chặn trên giao diện (giới hạn ký tự, bắt buộc định dạng).
- System feedback: phản hồi thị giác ngay lập tức, trong khoảng 0,1 đến 1 giây (đã dùng làm giả định `GA3`).

## 6. Heuristic dùng khi đặc tả im lặng (`loai_nguon: Heuristic`)

- Nielsen (10): visibility of system status; match between system and real world; user control and freedom; consistency and standards; error prevention; recognition rather than recall; flexibility and efficiency of use; aesthetic and minimalist design; help users recognize, diagnose and recover from errors; help and documentation.
- Norman (6): visibility; feedback; constraints; mapping; consistency; affordance/signifiers.
- Shneiderman (8): consistency; universal usability; informative feedback; dialogs yield closure; error prevention; easy reversal of actions; internal locus of control; reduce short-term memory load.
- WCAG 2.2 (tham khảo cho accessibility): SC 1.3.1 (info and relationships, nhãn gắn với ô nhập), SC 2.4.3 (focus order), SC 3.3.1 (error identification), SC 3.3.2 (labels or instructions), SC 4.1.2 (name, role, value).

## 7. Điểm mù AI thường gặp (Slide 12)

Accessibility chỉ dùng bàn phím, dark mode, bố cục phải sang trái (RTL), đa ngôn ngữ. Danh sách này nhắc SV tự rà ở Bước 2; AI không điền item thay SV.

## 8. Kỹ thuật tự động (Slide 16 đến 20) - dùng khi viết kiểm thử tự động

- Nên tự động: luồng lặp, trạng thái có kết quả rõ, nhiều bộ dữ liệu, hồi quy. Không tự động hoàn toàn: đánh giá đẹp/xấu, trải nghiệm.
- Data-driven (Slide 18): tách dữ liệu khỏi bước. Dùng trường `du_lieu` của item cho bảng giá trị (hợp lệ, sai định dạng, rỗng, vượt độ dài) và expected tương ứng.
- Assertion (Slide 19): kiểm kết quả người dùng thật sự nhìn thấy; tránh false positive (chữ có trong HTML nhưng bị ẩn).
- Ổn định (Slide 20): locator theo role/label/test id, auto-wait thay vì chờ cố định, mỗi test bắt đầu từ trạng thái sạch.

## 9. Công cụ thủ công (Slide 31)

- Link checker: phát hiện liên kết hỏng (hỗ trợ item điều hướng IA-03).
- Responsive testing: kiểm 3 viewport mobile 375px, tablet 768px, desktop 1440px.
- BrowserStack: kiểm đa trình duyệt (Safari, Chrome, Firefox) và thiết bị thật.


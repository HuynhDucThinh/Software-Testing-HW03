# [IA-04] [Register, Login, ForgotPassword, Profile] Các nút gửi biểu mẫu thiếu trạng thái đang xử lý (loading) và không khóa tạm (disabled) để chống bấm đúp khi chờ API

## Summary
Trên cả 4 biểu mẫu Đăng ký, Đăng nhập, Quên mật khẩu và Hồ sơ cá nhân, khi người dùng bấm nút gửi trong điều kiện mạng chậm, nút Submit không chuyển sang trạng thái `disabled` và không hiển thị chỉ báo đang xử lý, cho phép bấm đúp phát sinh nhiều request trùng lặp lên server.

- **Bug ID:** `BUG-26`
- **Checklist item:** `CL-37`
- **Interface aspect:** `IA-04` — Feedback / state
- **Màn hình:** Register (`/register`), Login (`/login`), ForgotPassword (`/forgot-password`), Profile (`/profile`)
- **Requirement:** Slide 10 #13 Processing States; Slide 11 IA-04
- **Loại lỗi:** `State`
- **Severity:** **Minor**
- **Priority:** **Medium**

## Environment
- **SUT:** `eshop-sut @ 1a9304a (repo HEAD 6b6a7a9)` (Web `http://localhost:5173`, Backend API `http://localhost:3000`)
- **P1:** Google Chrome 157.0.8103.50 trên Windows 11
- **P2:** Mozilla Firefox trên Windows 11 (bản cài đặt `137.0.1` dùng để quan sát trực tiếp; nhân Gecko `159.0` bản Playwright dùng để đo DOM và chụp ảnh minh chứng)
- **URL kiểm thử:** `http://localhost:5173/register`
- **Viewport:** Desktop `1440x900` (`P1`, `P2`)

## Preconditions
Mở DevTools -> Network -> chọn chế độ giả lập mạng chậm (`Slow 3G`) trên `P1`/`P2`.

## Steps to reproduce
1. Bật chế độ mạng chậm trong DevTools trên trang `/register` (và tương tự trên `/login`, `/forgot-password`, `/profile`).
2. Điền thông tin hợp lệ rồi bấm liên tiếp 2 lần nhanh vào nút Submit trong lúc request đầu tiên đang ở trạng thái `pending`.
3. Quan sát trạng thái thuộc tính `disabled`/nhãn nút Submit và số lượng request gửi đi trong tab Network.

## Expected result
Theo Slide 10 #13 (Processing States) và Slide 11 (`IA-04`), ngay khi gửi biểu mẫu chờ phản hồi mạng, nút Submit phải khóa tạm thời (`disabled`) kèm chỉ báo đang tải (spinner hoặc đổi nhãn `Đang xử lý...`) để ngăn gửi trùng request.

- **`CL-37`** (*Chỉ báo đang xử lý (loading) và khóa tạm nút Submit chống bấm đúp khi chờ API* — căn cứ: `Slide 10 #13 Processing States; Slide 11 IA-04`): Trong vòng 0,1 giây sau khi bấm gửi form và trong suốt lúc chờ API phản hồi, nút Submit hiển thị trạng thái đang xử lý (đổi nhãn hoặc hiện biểu tượng xoay) và có thuộc tính `disabled` ngăn bấm lặp lại nhiều lần, sau đó trở về bình thường khi hoàn tất. Fail nếu nút Submit vẫn cho phép nhấp liên tiếp phát sinh nhiều request API trùng nhau trong lúc đang chờ phản hồi.

## Actual result
Cả 4 component không quản lý biến state `isSubmitting`; trong lúc chờ API phản hồi, nút bấm vẫn giữ `disabled=false` và nhãn cũ, bấm đúp phát sinh `>= 2` request `POST`/`PUT` liên tiếp (ví dụ sinh 2 mã OTP liên tiếp hoặc cộng dồn số lần sai mật khẩu).

**Dữ kiện `Actual` nguyên văn theo từng mục và nền tảng:**
- **`CL-37` trên `P1`:** Actual: Trong lúc chờ API phản hồi chậm, nút Submit vẫn có disabled=false, giữ nguyên nhãn "Sign In" (không có chỉ báo loading) và cho phép bấm đúp phát sinh 2 request API trùng lặp.
- **`CL-37` trên `P2`:** Actual: Trong lúc chờ API phản hồi chậm, nút Submit vẫn có disabled=false, giữ nguyên nhãn "Sign In" (không có chỉ báo loading) và cho phép bấm đúp phát sinh 2 request API trùng lặp.

## Impact
Trên kết nối mạng di động hoặc mạng chập chờn, người dùng bấm lại nút gửi sẽ vô tình tạo bản ghi trùng, làm mất hiệu lực mã OTP đầu tiên hoặc làm tăng gấp đôi bộ đếm khóa tài khoản.

## Reproducibility
Luôn luôn (100%) trên các nền tảng áp dụng: `P1`, `P2`.

## Evidence
![BUG-26 — P1_CL-37](../screenshots/task1_failed/P1_CL-37.png)

**Danh sách đầy đủ ảnh minh chứng theo nền tảng:**
- `CL-37` (`P1`): [`screenshots/task1_failed/P1_CL-37.png`](../screenshots/task1_failed/P1_CL-37.png)
- `CL-37` (`P2`): [`screenshots/task1_failed/P2_CL-37.png`](../screenshots/task1_failed/P2_CL-37.png)

## GitHub Issue
- **Issue:** [#26 — [HW03-M1] [BUG-26] [IA-04] [Register, Login, ForgotPassword, Profile] Các nút gửi biểu mẫu thiếu trạng thái đang xử lý (loading) và không khóa tạm (disabled) để chống bấm đúp khi chờ API](https://github.com/HuynhDucThinh/Software-Testing-HW03/issues/26)
- **Ảnh chụp trang GitHub Issue:** [`screenshots/github_issues/ISSUE-26_BUG-26.png`](../screenshots/github_issues/ISSUE-26_BUG-26.png)

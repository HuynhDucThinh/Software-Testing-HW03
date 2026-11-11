# RUN - chạy checklist M1

Bước 3 của skill `gui-checklist-testing`. AI điền khung, SV sửa cho khớp cách chạy thật **trước** khi chạy. Sửa sau đó thì freeze lại, Expected không đổi.

## 1. Chuẩn bị (mỗi nền tảng)

- Khởi động SUT:
  - `cd eshop-sut/backend; node database.js; node server.js` (cổng 3000).
  - `cd eshop-sut/frontend-web; npm run dev` (cổng 5173).
- Restart backend (chạy lại `node database.js`) trước lượt chính thức để CSDL về trạng thái seed.
- Tài khoản: `test@eshop.com` / `Test1234!`. Tài khoản đăng ký mới dùng email dạng `m1+<mã>@example.com`.
- Nền tảng di động: ghi cách truy cập (`adb reverse tcp:5173 tcp:5173` và `tcp:3000`, hoặc IP LAN, hoặc tunnel BrowserStack Local).
- Ghi phiên bản: trình duyệt `<...>`, OS `<...>`, thiết bị `<...>`, độ phân giải `<...>`.

## 2. Thông tin nhận diện (mục 6 và 11 của đề)

- Overlay trên mọi ảnh: **email sinh viên** của bạn. Bạn tự làm overlay; AI không tạo hay ghép.
- Ảnh cross-platform: nhập **MSSV và họ tên** vào form `Register` hoặc `Profile` trước khi chụp (không bấm gửi nếu không cần).
- Ảnh phải thấy: tên trình duyệt/thiết bị, hệ điều hành, URL `localhost`.

## 3. Danh sách kiểm trước mỗi ảnh

- [ ] Thấy tên trình duyệt hoặc thiết bị
- [ ] Thấy URL `localhost`
- [ ] Có overlay email sinh viên
- [ ] Form có MSSV và họ tên (ảnh cross-platform)
- [ ] Đúng tên file: `P<n>_<id>.png` (Failed) hoặc `P<n>_<màn hình>_1.png` (tổng quan)

## 4. Thứ tự nhóm item

| Nhóm | Tiền điều kiện chung | Item | Ghi chú |
|---|---|---|---|
| G1 | Khách, trang `/register` mới tải | CL-xx, ... | |
| G2 | Khách, trang `/login` | CL-xx, ... | restart backend trước nhóm khóa tài khoản |
| G3 | Khách, `/forgot-password` | CL-xx, ... | |
| G4 | Đã đăng nhập, `/profile` | CL-xx, ... | |
| G5 | Đã đăng nhập, Header | CL-xx, ... | |

## 5. Dữ kiện từ `dom_probe.js`

Dán `dom_probe.js` vào DevTools Console từng trang, chép JSON vào ghi chú lượt chạy. Script chỉ cung cấp dữ kiện (số `h1`, `type`, nhãn có `*`, thứ tự Tab, vị trí lỗi so với nút gửi). SV tự kết luận Passed/Failed.

## 6. Ghi kết quả

File lượt `checklist/runs/<Px>_<YYYYMMDD-HHMM>.csv`, header `id,status,notes,evidence`. `status` thuộc Passed / Failed / N/A / Blocked. Failed ghi Actual nguyên văn trong `notes`. Blocked ghi item gốc. Gộp:

```powershell
python .agents/skills/gui-checklist-testing/scripts/merge_platform.py checklist/checklist.json checklist/runs/<file>.csv --platform <Px> --dry-run
python .agents/skills/gui-checklist-testing/scripts/merge_platform.py checklist/checklist.json checklist/runs/<file>.csv --platform <Px>
python .agents/skills/gui-checklist-testing/scripts/check_checklist.py checklist/checklist.json
```

## 7. Nhật ký lượt chạy

| Lượt | Nền tảng | Bắt đầu - kết thúc | Chính thức? | Ghi chú |
|---|---|---|---|---|


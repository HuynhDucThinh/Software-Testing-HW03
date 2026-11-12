# Đặc Tả Cấu Trúc Dữ Liệu Phiên Thử Nghiệm (`sessions/S0x.json`) & Bảng Người Tham Gia (`participants.md`)

Tài liệu quy định cấu trúc dữ liệu chuẩn cho `init_session.py`, `validate_study.py` và `analyze_usability.py`.

---

## 1. Cấu trúc tệp JSON từng phiên (`<dir>/sessions/S00.json` .. `S07.json`)

- Mỗi phiên lưu trong **một tệp JSON độc lập**:
  - `S00.json`: Phiên chạy thử Pilot (`"is_pilot": true`) — được kiểm tra tính hợp lệ và xuất tóm tắt riêng, **không gộp** vào trung bình của 7 phiên chính thức.
  - `S01.json` .. `S07.json`: 7 phiên chính thức với 7 người thật ngoài lớp (`"is_pilot": false`).
- **Quy tắc ẩn danh trong JSON:** Trường `participant_code` chỉ lưu mã `P00`, `P01..P07`. Tuyệt đối không đưa số điện thoại hay email cá nhân của người tham gia vào tệp JSON (email tài khoản thử nghiệm trên SUT nếu xuất hiện trong ghi chú phải thuộc tên miền giả định như `@example.com` hoặc `@eshop.com`).

### Ví dụ cấu trúc hợp lệ đã điền đầy đủ

```json
{
  "session_id": "S01",
  "is_pilot": false,
  "date": "2026-11-12",
  "participant_code": "P01",
  "user_group": "non-IT",
  "platform": "P1 - Chrome 157 / Windows 11",
  "clean_state_reset": true,
  "consent": {
    "screen_recording": true,
    "audio_recording": true,
    "ta_verification_contact": true
  },
  "recording_ref": "recordings/S01_P01.mp4",
  "task_execution": {
    "milestones": {
      "register_done": "02:15",
      "login_done": "03:05",
      "profile_updated": "04:30"
    },
    "total_duration": "04:30",
    "completion_status": "co_tro_giup",
    "goal_achieved": true
  },
  "events": [
    {
      "t": "01:10",
      "screen": "Register",
      "type": "E",
      "description": "Nhập mật khẩu hợp lệ có dấu @ 3 lần liên tiếp đều bị báo mật khẩu quá yếu.",
      "is_bug": true,
      "known_bug_id": "BUG-01"
    },
    {
      "t": "02:30",
      "screen": "Login",
      "type": "H",
      "description": "Khựng lại 6 giây nhìn tiêu đề trang Đăng nhập vì đang hiển thị chữ Đăng Ký.",
      "is_bug": true,
      "known_bug_id": "BUG-13"
    },
    {
      "t": "02:45",
      "screen": "Login",
      "type": "Q",
      "description": "Ủa sao gõ mật khẩu mà nó hiện nguyên chữ ra thế này, lộ hết rồi!",
      "is_bug": true,
      "known_bug_id": "BUG-04"
    }
  ],
  "assists": [
    {
      "t": "01:55",
      "screen": "Register",
      "reason": "Kẹt cứng quá 90 giây và 3 lần thử mật khẩu hợp lệ do lỗi regex BUG-01 của SUT.",
      "intervention": "Cung cấp mật khẩu mẫu có khoảng trắng để người dùng đi tiếp sang bước Đăng nhập."
    }
  ],
  "seq": 3,
  "sus": [3, 4, 2, 3, 3, 4, 3, 4, 2, 3],
  "open_probes": {
    "clarity": "Tiêu đề trang đăng nhập ghi nhầm thành Đăng Ký và quy tắc mật khẩu không nói rõ ký tự nào hợp lệ.",
    "error_recovery": "Thông báo lỗi chung chung hoặc bật hộp thoại bất ngờ nên không biết tự sửa số điện thoại thế nào.",
    "speed": "Mất nhiều thời gian thử đi thử lại mật khẩu và số điện thoại, lẽ ra chỉ mất chưa tới 2 phút.",
    "trust": "Không yên tâm vì ô mật khẩu lúc đăng nhập hiện rõ toàn bộ ký tự và cập nhật tên xong góc trên vẫn hiện tên cũ."
  },
  "moderator_notes": ""
}
```

### Quy tắc các trường bắt buộc

| Trường | Kiểu & Giá trị hợp lệ | Ràng buộc kiểm định tự động |
| :--- | :--- | :--- |
| `session_id` | Chuỗi `"S00"` .. `"S99"` | Phải trùng khớp hoàn toàn với tên tệp `S0x.json` |
| `is_pilot` | `true` / `false` | `S00` bắt buộc là `true`; `S01..S07` bắt buộc là `false` |
| `participant_code` | Chuỗi `"P00"` .. `"P99"` | Mã ẩn danh duy nhất, khớp với bảng `participants.md` |
| `clean_state_reset` | `true` | Phải đặt `true` xác nhận đã reset CSDL trước phiên |
| `task_execution.total_duration` | Chuỗi `"mm:ss"` | Thời lượng thực hiện nhiệm vụ hợp lệ (ví dụ `"04:30"`) |
| `task_execution.completion_status` | `"khong_tro_giup"` \| `"co_tro_giup"` \| `"khong_hoan_thanh"` | Nếu mảng `assists` không rỗng hoặc có sự kiện loại `"A"`, **cấm** để `"khong_tro_giup"` |
| `events[].type` | `"E"` (Lỗi/sai) \| `"H"` (Do dự/ngập ngừng) \| `"Q"` (Câu nói nguyên văn) \| `"A"` (Trợ giúp) | Phân loại chuẩn hóa để đếm tự động tần suất ma sát |
| `seq` | Số nguyên `1..7` hoặc `null` | Điểm câu hỏi độ dễ sau nhiệm vụ (`1 = Rất khó`, `7 = Rất dễ`) |
| `sus` | Mảng **đúng 10 số nguyên `1..5`** | Bắt buộc đủ 10 phần tử nguyên từ `1` đến `5`; thiếu hoặc ngoài khoảng sẽ báo `ERROR` |
| `open_probes` | Object đủ 4 khóa `clarity`, `error_recovery`, `speed`, `trust` | Không được bỏ trống bất kỳ khóa nào trong 4 chiều bắt buộc |

---

## 2. Quy chuẩn Bảng Danh Sách Người Tham Gia (`<dir>/participants.md`)

Theo Mục 6, Mục 11 và Mục 14 của đề bài:
1. Tệp `participants.md` tách rõ **Bảng 1 (Phiên Pilot — `P00`)** và **Bảng 2 (7 Người tham gia chính thức — `P01..P07`)**.
2. Mỗi dòng của Bảng 2 phải có: `Mã P0x`, `Mã phiên S0x`, `Họ và tên thật`, `Độ tuổi / Nghề nghiệp`, `Nhóm (non-IT / IT)`, `Liên hệ Zalo / SĐT (đã che 4 chữ số giữa)`, `Xác nhận ngoài lớp HW03`, và `Đồng ý xác minh`.
3. **Định dạng che 4 chữ số giữa bắt buộc:**
   - Với SĐT/Zalo 10 số Việt Nam (`0901234567`): che đúng 4 chữ số ở vị trí thứ 4–7 thành **`090****567`** (3 chữ số đầu + `****` + 3 chữ số cuối).
   - Nếu kèm email cá nhân dự phòng, che phần giữa tên hộp thư (ví dụ `ng****an@gmail.com`), ưu tiên dùng SĐT/Zalo che 4 số giữa để trợ giảng thuận tiện gọi xác minh theo đúng yêu cầu *"name plus Zalo / phone, middle four digits masked"*.

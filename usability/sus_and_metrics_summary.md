# Báo Cáo Tính Toán Điểm SUS & Thống Kê Hiệu Năng Thực Nghiệm (Sinh Tự Động)

> Công thức chuẩn System Usability Scale (Brooke, 1996): câu lẻ `(x - 1)`, câu chẵn `(5 - x)`, tổng điểm quy đổi `= tổng đóng góp * 2.5` (thang `0.0 .. 100.0`). Phiên chạy thử Pilot (`S00`) được tách riêng, không gộp vào thống kê của 7 phiên chính thức.

## 1. Tóm tắt Phiên Chạy Thử Nghiệm Pilot (`S00`)

| Mã phiên | Mã người TG | Nhóm | Nền tảng | Kết quả hoàn thành | Thời gian | Lỗi (`E`) | Do dự (`H`) | Cứu hộ (`A`) | SEQ (`1–7`) | SUS (`0–100`) |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `S00` | `P00` | `non-IT` | P1 - Google Chrome 157 (Incognito) / Windows 11 | Hoàn thành (có cứu hộ lỗi chặn) | `01:02` | 2 | 1 | 2 | 5 | **47.5** |

## 2. Tổng Hợp Kết Quả Thực Thi 7 Phiên Chính Thức (`S01` .. `S07`)

| Mã phiên | Mã người TG | Nhóm | Kết quả hoàn thành | Thời gian | Lỗi (`E`) | Do dự (`H`) | Cứu hộ (`A`) | SEQ (`1–7`) | SUS (`0–100`) | Xếp hạng SUS |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `S01` | `P01` | `non-IT` | Hoàn thành (có cứu hộ lỗi chặn) | `02:40` | 6 | 2 | 2 | 4 | **30.0** | `F` (Worst Imaginable) |
| `S02` | `P02` | `non-IT` | Hoàn thành độc lập | `01:44` | 3 | 1 | 0 | 5 | **47.5** | `F` (Poor) |
| `S03` | `P03` | `non-IT` | Hoàn thành (có cứu hộ lỗi chặn) | `00:48` | 4 | 0 | 1 | 2 | **52.5** | `D` (OK / Fair) |
| `S04` | `P04` | `non-IT` | Hoàn thành (có cứu hộ lỗi chặn) | `01:17` | 4 | 0 | 1 | 3 | **45.0** | `F` (Poor) |
| `S05` | `P05` | `non-IT` | Hoàn thành (có cứu hộ lỗi chặn) | `01:44` | 5 | 1 | 2 | 3 | **67.5** | `C` (OK / Fair) |
| `S06` | `P06` | `non-IT` | Hoàn thành độc lập | `01:18` | 6 | 0 | 0 | 3 | **52.5** | `D` (OK / Fair) |
| `S07` | `P07` | `non-IT` | Hoàn thành độc lập | `01:10` | 4 | 0 | 0 | 4 | **45.0** | `F` (Poor) |

## 3. Ma Trận Điểm Gốc (`1..5`) & Điểm Quy Đổi Chi Tiết Từng Câu `SUS` (`Q1` .. `Q10`)

| Phiên (`Người TG`) | Q1 (+) | Q2 (-) | Q3 (+) | Q4 (-) | Q5 (+) | Q6 (-) | Q7 (+) | Q8 (-) | Q9 (+) | Q10 (-) | Tổng quy đổi (`0–40`) | Điểm `SUS` (`x 2.5`) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `S01` (`P01`) | 2 (`1`) | 5 (`0`) | 1 (`0`) | 5 (`0`) | 2 (`1`) | 3 (`2`) | 2 (`1`) | 4 (`1`) | 3 (`2`) | 1 (`4`) | `12` | **30.0** |
| `S02` (`P02`) | 3 (`2`) | 2 (`3`) | 3 (`2`) | 3 (`2`) | 4 (`3`) | 3 (`2`) | 1 (`0`) | 5 (`0`) | 4 (`3`) | 3 (`2`) | `19` | **47.5** |
| `S03` (`P03`) | 2 (`1`) | 1 (`4`) | 2 (`1`) | 3 (`2`) | 4 (`3`) | 3 (`2`) | 2 (`1`) | 2 (`3`) | 2 (`1`) | 2 (`3`) | `21` | **52.5** |
| `S04` (`P04`) | 2 (`1`) | 3 (`2`) | 3 (`2`) | 4 (`1`) | 3 (`2`) | 2 (`3`) | 2 (`1`) | 3 (`2`) | 3 (`2`) | 3 (`2`) | `18` | **45.0** |
| `S05` (`P05`) | 2 (`1`) | 3 (`2`) | 3 (`2`) | 2 (`3`) | 3 (`2`) | 2 (`3`) | 4 (`3`) | 1 (`4`) | 4 (`3`) | 1 (`4`) | `27` | **67.5** |
| `S06` (`P06`) | 2 (`1`) | 3 (`2`) | 3 (`2`) | 2 (`3`) | 2 (`1`) | 2 (`3`) | 3 (`2`) | 2 (`3`) | 2 (`1`) | 2 (`3`) | `21` | **52.5** |
| `S07` (`P07`) | 2 (`1`) | 3 (`2`) | 2 (`1`) | 2 (`3`) | 2 (`1`) | 3 (`2`) | 2 (`1`) | 2 (`3`) | 2 (`1`) | 2 (`3`) | `18` | **45.0** |
| **Trung bình câu** | 2.14 (`1.14`) | 2.86 (`2.14`) | 2.43 (`1.43`) | 3.00 (`2.00`) | 2.86 (`1.86`) | 2.57 (`2.43`) | 2.29 (`1.29`) | 2.71 (`2.29`) | 2.86 (`1.86`) | 2.00 (`3.00`) | `19.43` | **48.6** |

## 4. Bảng Thống Kê Tổng Hợp Khả Năng Sử Dụng & Hiệu Năng

| Chỉ số đo lường (Metric) | Giá trị thống kê | Đối chiếu chuẩn / Ghi chú |
| :--- | :---: | :--- |
| **Số phiên chính thức hợp lệ (`n`)** | `7` / `7` | Tách biệt hoàn toàn khỏi phiên Pilot `S00` |
| **Điểm `SUS` trung bình ± Độ lệch chuẩn (`Mean ± SD`)** | **`48.6 ± 11.3`** | Lệch `-19.4` điểm so với mốc trung bình lịch sử `68.0` |
| **Điểm `SUS` trung vị & Khoảng biến thiên (`Median · Min–Max`)** | `47.5` (`30.0 – 67.5`) | Hạng **`F`** · `Poor` · Not Acceptable (Kém — Dưới ngưỡng chấp nhận) |
| **Độ dễ sau nhiệm vụ `SEQ` (`Mean ± SD` · `Median`)** | `3.43 ± 0.98` (`Median: 3.0`) | Thang `1..7` (mốc trung bình tham chiếu `~5.5`) |
| **Hoàn thành độc lập (không cần cứu hộ)** | `3/7 (42.9%)` | Người dùng tự hoàn tất toàn bộ luồng |
| **Hoàn thành có cứu hộ tại điểm lỗi chặn SUT** | `4/7 (57.1%)` | Áp dụng *System-Bug Rescue Protocol* sau `>= 90s` |
| **Không hoàn thành nhiệm vụ** | `0/7 (0.0%)` | Dừng phiên hoặc vượt thời gian tối đa |
| **Tổng tỷ lệ đi tới đích cuối luồng** | `7/7 (100.0%)` | Tính chung cả độc lập và có cứu hộ kỹ thuật |
| **Hoàn thành trong mốc Benchmark (`<= 05:00`)** | `7/7 (100.0%)` | So với ngưỡng mục tiêu trong `plan.md` |
| **Thời gian thực hiện (`Mean ± SD` · `Median` · `Min–Max`)** | `01:32 ± 00:36` (`Med: 01:18`, `00:48–02:40`) | Tính trên các phiên đi hết luồng |
| **Trung bình Lỗi (`E`) / Do dự (`H`) / Cứu hộ (`A`) mỗi phiên** | `4.57` / `0.57` / `0.86` | Đo mật độ ma sát tương tác trung bình |

## 5. Danh Mục Sự Kiện Lỗi Kỹ Thuật Ghi Nhận Từ Các Phiên (`is_bug: true`)

| Phiên | Mốc `mm:ss` | Màn hình | Loại | Ghi nhận nguyên văn tại hiện trường | Mã Bug đối chiếu |
| :---: | :---: | :--- | :---: | :--- | :---: |
| `S00 (Pilot)` | `00:11` | Register | `E` | Nhập mật khẩu hợp lệ có ký tự đặc biệt nhưng bị báo Mật khẩu quá yếu do regex đòi khoảng trắng. | `BUG-01` |
| `S00 (Pilot)` | `00:29` | Login | `H` | Trang đăng nhập mà ghi tên trang Đăng Ký, nút đăng nhập lại ghi Sign In (chưa thống nhất cách trình bày và ngôn ngữ). | `BUG-13` |
| `S00 (Pilot)` | `00:36` | Login | `Q` | Ô mật khẩu tại màn hình đăng nhập hiển thị rõ nguyên chữ 'Matkhau 123' không được che dấu chấm. | `BUG-04` |
| `S00 (Pilot)` | `00:56` | Profile | `E` | Nhập số điện thoại 10 chữ số bắt đầu bằng số 0 bị hộp thoại alert báo không hợp lệ (người dùng nhận xét SĐT không cho nhập đủ 10 số). | `BUG-05` |
| `S01` | `00:12` | Register | `E` | Gõ nhầm nhiều khoảng trắng bên trong địa chỉ email ('lva@...   com') nhưng ô Email không kiểm tra định dạng hợp lệ và vẫn cho gửi tạo tài khoản. | `BUG-09` |
| `S01` | `00:21` | Register | `E` | Nhập mật khẩu đúng yêu cầu hiển thị trên màn hình nhưng vẫn bị báo đỏ 'Mật khẩu quá yếu!' do bộ lọc ngầm bắt buộc khoảng trắng và cấm ký tự đặc biệt. | `BUG-01` |
| `S01` | `00:27` | Register | `Q` | Phản ánh ô mật khẩu không có nút ẩn/hiện mật khẩu và không có ô xác nhận lại nên khó nhìn biết mình vừa gõ ký tự gì. | `BUG-07` |
| `S01` | `00:34` | Login | `H` | Ngập ngừng khi thấy trang đăng nhập lại ghi tiêu đề là 'Đăng Ký', nhãn ô là 'Username' và nút bấm ghi 'Sign In' trộn lẫn tiếng Anh với tiếng Việt. | `BUG-13` |
| `S01` | `00:48` | Login | `E` | Đăng nhập thất bại ở lượt tạo tài khoản đầu tiên do trước đó gõ nhầm mật khẩu bị che dấu chấm trên trang Đăng ký (ô mật khẩu trang Đăng nhập lại hiện rõ nguyên chữ thường); phải bấm 'Đăng ký ngay' quay lại tạo tài khoản lần 2. | `BUG-04` |
| `S01` | `01:09` | Register | `E` | Ở lượt đăng ký lại lần 2 vẫn tiếp tục bị chặn bởi lỗi 'Mật khẩu quá yếu!' dù đã nhập đủ chữ hoa, chữ thường, số và ký tự đặc biệt. | `BUG-01` |
| `S01` | `01:57` | Profile | `E` | Liên tiếp 5 lần tự thử nhập số điện thoại Việt Nam (bắt đầu bằng số 0, thêm khoảng trắng theo mẫu, đổi đầu +84) đều bị hộp thoại alert chặn báo 'Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.' | `BUG-05` |
| `S01` | `02:42` | Profile | `E` | Cập nhật Họ tên từ 'Lê Văn A' sang 'Lê Văn An' báo thành công nhưng dòng chào trên góc phải thanh Header vẫn giữ nguyên tên cũ 'Chào, Lê Văn A' kể cả khi quay ra Trang chủ. | `BUG-11` |
| `S02` | `00:21` | Login | `H` | Sau khi bấm Đăng Ký lần đầu, trang chuyển sang màn hình đăng nhập nhưng không có thông báo thành công, không điền sẵn tài khoản vừa tạo và tiêu đề vẫn ghi 'Đăng Ký' khiến người dùng tưởng chưa lưu được nên bấm 'Đăng ký ngay' để tạo lại. | `BUG-13` |
| `S02` | `00:47` | Register | `E` | Xóa phần đuôi tên miền email chỉ để lại chuỗi 'nguyenvanc' (không có ký tự @) rồi bấm Đăng Ký thì biểu mẫu không kiểm tra định dạng email và vẫn tạo tài khoản thành công. | `BUG-09` |
| `S02` | `00:54` | Login | `Q` | Khi chuyển từ Đăng ký sang Đăng nhập phải gõ lại toàn bộ tài khoản từ đầu, đồng thời ô Mật khẩu hiển thị lộ rõ chuỗi ký tự thường trên màn hình. | `BUG-04` |
| `S02` | `01:13` | Profile | `Q` | Bỏ trống hoàn toàn ô 'Địa chỉ giao hàng' rồi bấm Cập nhật nhưng hệ thống vẫn cho lưu bình thường qua hộp thoại window.alert('Cập nhật thành công!') kiểu cũ. | `BUG-16` |
| `S02` | `01:46` | Profile | `E` | Đổi Họ tên trong Hồ sơ sang 'Nguyễn Văn C2' và bấm Cập nhật báo thành công nhưng dòng chào trên góc phải thanh Header vẫn giữ tên cũ 'Chào, Nguyễn C2', gây cảm giác quay về Trang chủ không lưu đúng tên mới. | `BUG-11` |
| `S02` | `01:51` | Profile | `E` | Bấm nút 'Thoát' ngay khi đang đứng ở trang Hồ sơ thì giao diện không chuyển về Trang chủ hay trang Đăng nhập mà đứng yên ở màn hình trắng chỉ hiện dòng chữ tĩnh 'Vui lòng đăng nhập'. | `BUG-10` |
| `S03` | `00:06` | Register | `E` | Nhập chuỗi 'levanb' không có ký tự '@' vào ô Email trên trang Đăng ký nhưng hệ thống không kiểm tra định dạng hợp lệ và vẫn tạo tài khoản. | `BUG-09` |
| `S03` | `00:09` | Register | `Q` | Nhận xét quy tắc mật khẩu bất thường khi bắt buộc mật khẩu phải chứa ký tự dấu cách ('Matkhau 123') mới cho đăng ký. | `BUG-01` |
| `S03` | `00:12` | Login | `Q` | Chuyển từ trang Đăng ký sang Đăng nhập không tự lưu giữ thông tin tài khoản người dùng vừa tạo, đồng thời tiêu đề trang vẫn ghi 'Đăng Ký'. | `BUG-13` |
| `S03` | `00:21` | Login | `E` | Do trang Đăng ký ghi nhãn 'Email' nhưng trang Đăng nhập lại đổi nhãn thành 'Username', người dùng gõ Họ tên ('lê văn b') vào ô Username và bị báo lỗi 'Đăng nhập thất bại. Vui lòng kiểm tra lại.' (mật khẩu cũng bị lộ chữ thường). | `BUG-14` |
| `S03` | `00:36` | Profile | `E` | Nhập số điện thoại mẫu 10 chữ số bắt đầu bằng số 0 đúng như gợi ý trên ô nhập nhưng bị hộp thoại alert chặn báo 'Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.' | `BUG-05` |
| `S04` | `00:06` | Register | `E` | Chỉ gõ duy nhất 1 chữ cái 'd' vào ô Email nhưng biểu mẫu Đăng ký không hề báo lỗi định dạng email và vẫn cho phép tạo tài khoản. | `BUG-09` |
| `S04` | `00:14` | Login | `Q` | Phản ánh hệ thống không tự lưu giữ thông tin tài khoản giữa màn hình Đăng ký và màn hình Đăng nhập; gõ lệch mật khẩu lúc đăng ký (do thiếu ô xác nhận lại) nên đăng nhập thất bại và phải bấm vào 'Quên mật khẩu?'. | `BUG-07` |
| `S04` | `00:34` | ForgotPassword | `E` | Tại Bước 2 Quên mật khẩu (không có dòng hướng dẫn quy tắc mật khẩu, mã OTP chỉ 4 chữ số), người dùng nhập mật khẩu mới 2 lần đều bị hộp thoại window.alert chặn báo 'Mật khẩu quá yếu!' do lỗi biểu thức kiểm tra bắt buộc khoảng trắng. | `BUG-01` |
| `S04` | `00:38` | ForgotPassword | `Q` | Nhận xét cơ chế bật hộp thoại thông báo alert mặc định của trình duyệt có trải nghiệm UI/UX chưa tốt và gây ngắt quãng thao tác. | `BUG-16` |
| `S05` | `00:36` | Register | `H` | Các ô nhập trên biểu mẫu Đăng ký thiếu thuộc tính name/autocomplete chuẩn nên trình duyệt tự động điền sẵn tài khoản cũ không liên quan, người dùng phải xóa đi gõ lại. | `BUG-24` |
| `S05` | `00:41` | Register | `E` | Nhập chuỗi 'lethie' không có ký tự '@' vào ô Email nhưng biểu mẫu Đăng ký vẫn chấp nhận không báo lỗi định dạng. | `BUG-09` |
| `S05` | `00:44` | Register | `E` | Nhập mật khẩu bị báo đỏ 'Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.' do lỗi biểu thức chính quy bắt buộc khoảng trắng. | `BUG-01` |
| `S05` | `00:52` | Login | `Q` | Màn hình Đăng nhập hiển thị sai tiêu đề thành 'Đăng Ký', trộn lẫn nhãn tiếng Anh ('Username', 'Sign In'), không giữ sẵn tài khoản vừa tạo và làm lộ mật khẩu dạng chữ thường. | `BUG-13` |
| `S05` | `01:18` | Profile | `E` | Nhập số điện thoại 10 chữ số bắt đầu bằng số 0 rồi thử thêm khoảng trắng đều bị hộp thoại alert chặn báo 'Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.' ở 2 lần liên tiếp (01:18 và 01:26). | `BUG-05` |
| `S05` | `01:44` | Profile | `E` | Thử xóa chữ trong ô 'Họ Tên' và chỉ gõ khoảng trắng nhưng biểu mẫu không cắt khoảng trắng mà vẫn báo 'Cập nhật thành công!'. | `BUG-12` |
| `S05` | `01:48` | Profile | `E` | Sau khi lưu thành công Số điện thoại và Địa chỉ giao hàng ('Hà Nội'), người dùng bấm logo EShop ra Trang chủ rồi bấm lại 'Chào, lethie' vào Hồ sơ thì toàn bộ Số điện thoại và Địa chỉ giao hàng vừa lưu biến mất sạch trên giao diện (quay về ô trống do Profile.jsx đọc lại state cũ chưa đồng bộ trong AuthContext). | `BUG-28` |
| `S06` | `00:08` | Register | `E` | Gõ chuỗi ký tự rất dài ('lê văn ffffffffffffffffffffffff...') vào ô 'Họ Tên' nhưng biểu mẫu hoàn toàn không kiểm tra giới hạn độ dài tối đa (maxLength). | `BUG-18` |
| `S06` | `00:14` | Register | `E` | Nhập 'levanf' không có ký tự '@' vào ô Email nhưng biểu mẫu Đăng ký vẫn cho phép gửi đi không báo lỗi định dạng. | `BUG-09` |
| `S06` | `00:16` | Register | `Q` | Nhận xét quy tắc kiểm tra mật khẩu hơi kỳ lạ (bắt buộc khoảng trắng thay vì ký tự đặc biệt thông thường) và không có nút ẩn/hiện mật khẩu. | `BUG-01` |
| `S06` | `00:19` | Login | `Q` | Nhận xét giữa các màn hình chuyển tiếp từ Đăng ký sang Đăng nhập không lưu giữ thông tin tài khoản tạm thời để điền sẵn, đồng thời tiêu đề trang lại ghi 'Đăng Ký'. | `BUG-13` |
| `S06` | `00:24` | Login | `E` | Mật khẩu ('Matkhau 123') hiển thị lộ nguyên văn dạng chữ thường trên trình duyệt và không có nút ẩn/hiện mật khẩu. | `BUG-04` |
| `S06` | `00:44` | Profile | `E` | Bấm 'Cập nhật' khi chưa nhập Số điện thoại bị hộp thoại hệ thống window.alert chặn cứng báo 'Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.'. | `BUG-16` |
| `S06` | `00:52` | Profile | `E` | Nhập 9 chữ số '912345678' (không bắt đầu bằng số 0) vào ô Số điện thoại và để trống hoàn toàn ô 'Địa chỉ giao hàng' nhưng hệ thống vẫn chấp nhận báo 'Cập nhật thành công!'. | `BUG-05` |
| `S06` | `00:58` | Header | `E` | Sau khi nối thêm chuỗi dài ký tự 'f' vào 'Họ Tên' và tải lại trang (lặp lại ở 01:18..01:26), dòng 'Chào, lê văn fff...' làm vỡ bố cục thanh Header theo chiều ngang, ép chữ 'Giỏ hàng' gãy dòng và đẩy nút 'Thoát' văng xa khỏi khung nhìn bên phải khiến người dùng phải kéo thanh cuộn ngang qua khoảng trắng lớn mới bấm 'Thoát' được ở 01:26. | `BUG-18` |
| `S07` | `00:09` | Register | `E` | Nhập chuỗi 'hhhhhh' không có ký tự '@' vào ô Email nhưng biểu mẫu không kiểm tra định dạng Gmail/Username hợp lệ, đồng thời trình duyệt tự động xổ danh sách tài khoản gợi ý che khuất màn hình. | `BUG-09` |
| `S07` | `00:18` | Register | `E` | Nhập mật khẩu bị báo đỏ 'Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.' do quy tắc kiểm tra khoảng trắng lỗi; người dùng nhận xét biểu mẫu cần nâng cấp thêm ô 'Nhập lại mật khẩu'. | `BUG-01` |
| `S07` | `00:32` | Login | `Q` | Sau khi đăng ký xong, trang nhảy thẳng sang màn hình Đăng nhập không có thông báo xác nhận hay hiệu ứng chuyển đổi trạng thái, bố cục sơ sài và tiêu đề trang bị ghi nhầm thành 'Đăng Ký'. | `BUG-13` |
| `S07` | `00:40` | Login | `E` | Gõ nhầm Username thiếu ký tự ('hhhh' thay vì 'hhhhhh') trong khi mật khẩu hiển thị lộ nguyên văn dạng chữ thường; hệ thống báo chung 'Đăng nhập thất bại. Vui lòng kiểm tra lại.'. | `BUG-04` |
| `S07` | `00:47` | ForgotPassword | `E` | Bấm sang 'Quên mật khẩu?' và nhập 'hhhh' lấy mã OTP thì bị hộp thoại window.alert mặc định chặn màn hình báo 'Lỗi: User not found'; người dùng nhận xét kiểu hộp thoại alert quá cũ kỹ. | `BUG-16` |
| `S07` | `01:01` | Profile | `Q` | Quay lại sửa đúng Username 'hhhhhh' để đăng nhập, điền Số điện thoại '912345678' cùng Địa chỉ giao hàng 'Không có.' rồi bấm 'Cập nhật' (lặp lại ở 01:10): tiếp tục hiện hộp thoại window.alert('Cập nhật thành công!') đơn điệu, giao diện web sơ sài làm trải nghiệm chưa tốt. | `BUG-16` |
| `S07` | `01:20` | Login | `Q` | Khi thoát ra kiểm tra lại màn hình Đăng nhập/Đăng ký cuối phiên, người dùng góp ý cơ chế tài khoản mất cân đối: lúc tạo mới thiếu ô nhập lại mật khẩu, nhưng khi nhập đúng email mà gõ sai mật khẩu vài lần thì bị khóa cứng ngay mà không báo rõ số lần thử còn lại. | `BUG-06` |

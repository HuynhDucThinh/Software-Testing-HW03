# Item SV tự bổ sung (bước 2)

## Giả định mới (bắt đầu từ GA6 / NA2)

| Mã | Nội dung | Loại (quyết định Expected / N/A) | Lý do SV chốt |
|---|---|---|---|
| GA6 | Đặc tả FR-22 yêu cầu thông báo lỗi nằm "trên nút submit"; hiểu là khối lỗi nằm trong form, liền kề phía trên nút Submit (không nằm ở đầu trang phía trên tiêu đề và cũng không nằm dưới nút Submit). | Quyết định Expected | Đặc tả không nói rõ khoảng cách; chọn cách hiểu đo được bằng toạ độ `getBoundingClientRect()`. |
| GA7 | Đặc tả không nói về Họ Tên chỉ gồm khoảng trắng; áp dụng Nielsen #5 (Error prevention): giá trị chỉ gồm khoảng trắng không được xem là Họ Tên hợp lệ. | Quyết định Expected | Trường Họ Tên là bắt buộc (FR-01:32) nên giá trị rỗng về mặt nội dung phải bị từ chối. |
| GA8 | Đặc tả không quy định `document.title`; áp dụng WCAG 2.4.2: mỗi trang có tiêu đề tab mô tả riêng, khác nhau giữa các trang. | Quyết định Expected | Giúp người dùng phân biệt tab và công cụ đọc màn hình xác định trang. |
| NA2 | P3 là Chrome trên điện thoại Android có bàn phím ảo trên màn hình, còn P1 và P2 là máy tính để bàn không có bàn phím ảo; mục kiểm tra loại bàn phím ảo hiển thị khi chạm vào ô nhập chỉ áp dụng cho P3. | N/A nền tảng | Máy tính để bàn không có bàn phím ảo để quan sát. |

## Item

### SV-01
- ia: IA-03
- man_hinh: Login
- muc_kiem_tra: Thứ tự di chuyển focus bằng phím Tab trên form Đăng nhập
- can_cu: FR-21 (eshop-sut/README.md:248); Slide 10 #9 Tab Order
- loai_nguon: SRS
- tien_dieu_kien: Mở /login, click vào vùng trống rồi nhấn Tab liên tiếp, quan sát thứ tự focus.
- expected: Khi nhấn Tab liên tiếp trên /login, focus đi lần lượt từ trên xuống dưới, trái sang phải qua các thành phần của form theo thứ tự hiển thị (ô tài khoản, ô mật khẩu, liên kết `Quên mật khẩu?`, nút gửi form, liên kết `Đăng ký ngay`) và không nhảy cóc. Fail nếu nút gửi form nhận focus trước ô tài khoản hoặc trước ô mật khẩu, hoặc thứ tự focus khác thứ tự hiển thị từ trên xuống dưới.
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: Lỗi thứ tự Tab chỉ lộ khi đi bằng bàn phím thật, nhìn ảnh chụp hay đọc mã giao diện bằng mắt thường không thấy; AI sinh checklist chủ yếu từ mô tả nhãn và màu nên không nghĩ tới việc duyệt focus từng bước.

### SV-02
- ia: IA-03
- man_hinh: Register, ForgotPassword
- muc_kiem_tra: Thứ tự di chuyển focus bằng phím Tab trên form Đăng ký và form Quên mật khẩu ở cả 2 bước
- can_cu: FR-21 (eshop-sut/README.md:248); Slide 10 #9 Tab Order, #11 Keyboard Support
- loai_nguon: SRS
- tien_dieu_kien: Mở /register; sau đó mở /forgot-password, nhập `test@eshop.com`, bấm `Lấy mã OTP` để sang Bước 2 rồi kiểm tra lại.
- expected: Trên /register và ở cả Bước 1 lẫn Bước 2 của /forgot-password, nhấn Tab liên tiếp di chuyển focus qua mọi ô nhập, nút và liên kết theo đúng thứ tự hiển thị từ trên xuống dưới, mỗi phần tử tương tác nhận focus đúng một lần. Fail nếu có phần tử tương tác bị bỏ qua, nhận focus hai lần, hoặc thứ tự focus khác thứ tự hiển thị.
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: Prompt lượt IA-03 yêu cầu chung về điều hướng nên AI gom vào điều hướng giữa các trang; tôi không yêu cầu riêng "thứ tự Tab từng form" nên AI không tách thành mục kiểm tra cụ thể cho từng màn hình.

### SV-03
- ia: IA-02
- man_hinh: Login
- muc_kiem_tra: Vị trí khối thông báo lỗi so với nút gửi form trên trang Đăng nhập
- can_cu: FR-22 (eshop-sut/README.md:255)
- loai_nguon: SRS
- tien_dieu_kien: Tại /login, nhập Email đúng định dạng nhưng sai mật khẩu rồi bấm nút gửi form để hiện thông báo lỗi.
- expected: Khối thông báo lỗi đăng nhập hiển thị phía trên nút gửi form (toạ độ `bottom` của khối lỗi nhỏ hơn hoặc bằng toạ độ `top` của nút gửi, đo bằng `getBoundingClientRect()`). Fail nếu khối thông báo lỗi nằm bên dưới nút gửi form.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI chỉ kiểm tra nội dung thông báo lỗi (CL-32, CL-34) mà không để ý vị trí khối lỗi so với nút; vị trí chỉ phát hiện được khi thật sự kích hoạt lỗi và nhìn bố cục, AI không chạy giao diện.

### SV-04
- ia: IA-02
- man_hinh: Register
- muc_kiem_tra: Vị trí khối thông báo lỗi so với nút Đăng Ký trên trang Đăng ký
- can_cu: FR-22 (eshop-sut/README.md:255); Giả định GA6
- loai_nguon: SRS
- tien_dieu_kien: Tại /register, nhập mật khẩu không đạt quy tắc (ví dụ `abc`) rồi bấm `Đăng Ký` để hiện khối thông báo lỗi.
- expected: Khối thông báo lỗi hiển thị trong form, liền kề phía trên nút `Đăng Ký` (khoảng cách dọc giữa mép dưới khối lỗi và mép trên nút nhỏ hơn khoảng cách tới tiêu đề trang, đo bằng `getBoundingClientRect()`). Fail nếu khối lỗi nằm phía trên tiêu đề trang hoặc phía trên tất cả các ô nhập, xa nút `Đăng Ký` đến mức người dùng phải cuộn mới thấy khi form dài.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: Quy tắc "lỗi nằm trên nút submit" chỉ có ý nghĩa khi so toạ độ thực tế trên giao diện; AI coi mọi khối lỗi hiển thị phía trên nút là đạt nên không tách riêng kiểm tra khoảng cách và vị trí so với tiêu đề.

### SV-05
- ia: IA-04
- man_hinh: Profile, Header
- muc_kiem_tra: Hiển thị an toàn ký tự HTML trong Họ Tên ở lời chào trên Header
- can_cu: SEC-04 (eshop-sut/README.md:281)
- loai_nguon: SRS
- tien_dieu_kien: Đăng nhập `test@eshop.com`, tại /profile đổi Họ Tên thành `<b>Test</b><i>User</i>` kèm SĐT hợp lệ, bấm `Cập nhật`, rồi đăng xuất và đăng nhập lại.
- expected: Lời chào trên Header hiển thị nguyên văn chuỗi `Chào, <b>Test</b><i>User</i>` dưới dạng văn bản thường (nhìn thấy cả các ký tự `<b>`), không in đậm hoặc in nghiêng phần tên. Fail nếu phần tên được trình duyệt dựng thành định dạng (in đậm, in nghiêng) hoặc thẻ HTML nhập vào bị thực thi.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: Prompt các lượt IA chỉ nhắm vào yêu cầu giao diện FR-21..24 nên AI bỏ qua điều khoản bảo mật SEC-04 dù nó có trong m1_test_basis; việc hiển thị tên người dùng chỉ lộ lỗi khi nhập thẻ HTML thật.

### SV-06
- ia: IA-01
- man_hinh: Header, Profile
- muc_kiem_tra: Bố cục Header khi Họ Tên người dùng rất dài và không có khoảng trắng
- can_cu: Slide 10 #5 Field Limits, #18 Element Overlap, #19 Scroll Boundaries
- loai_nguon: Control
- tien_dieu_kien: Đăng nhập, đổi Họ Tên tại /profile thành chuỗi 100 ký tự liên tục không có khoảng trắng (ví dụ lặp `Nguyen`), SĐT hợp lệ, bấm `Cập nhật`, đăng nhập lại; kiểm tra ở viewport 375px và 1440px.
- expected: Thanh Header với lời chào dài vẫn nằm gọn trong chiều rộng khung nhìn, không che nút `Đăng xuất` hay liên kết khác và không sinh thanh cuộn ngang (`document.documentElement.scrollWidth <= document.documentElement.clientWidth`); tên dài được cắt bớt, xuống dòng hoặc rút gọn. Fail nếu lời chào đẩy nút `Đăng xuất` ra ngoài màn hình, chồng lên phần tử khác hoặc tạo thanh cuộn ngang.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI chỉ nghĩ đến bố cục với dữ liệu mẫu ngắn như "Test User" (CL-10) mà không thử dữ liệu cực trị; không có số liệu thật về độ dài tên nên AI khó đoán rủi ro tràn bố cục.

### SV-07
- ia: IA-01
- man_hinh: Header, Profile
- muc_kiem_tra: Hiển thị đúng chữ tiếng Việt có dấu trong Họ Tên và Địa chỉ giao hàng
- can_cu: Slide 10 #3 Typography and Content; FR-21 (eshop-sut/README.md:244)
- loai_nguon: Control
- tien_dieu_kien: Tại /profile nhập Họ Tên `Nguyễn Văn Ánh` và Địa chỉ `12 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh`, SĐT hợp lệ, bấm `Cập nhật`, tải lại trang.
- expected: Sau khi lưu và tải lại, lời chào trên Header và các ô Họ Tên, Địa chỉ giao hàng trên /profile hiển thị đúng và đủ mọi dấu tiếng Việt như đã nhập (`Nguyễn Văn Ánh`, `Đường Lê Lợi`), không có ký tự lỗi `?`, `�` hoặc mất dấu. Fail nếu có ký tự dấu bị mất, bị thay bằng ký tự lạ hoặc hiển thị khác giá trị đã nhập.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI sinh mục kiểm tra chính tả của nhãn tĩnh (CL-02) nhưng không nghĩ tới dữ liệu động có dấu do người dùng nhập và vòng lưu-đọc qua máy chủ; điều này cần dữ liệu thật mới kiểm được.

### SV-08
- ia: IA-02
- man_hinh: Register
- muc_kiem_tra: Giá trị biên độ dài tối thiểu 8 ký tự của mật khẩu trên trang Đăng ký
- can_cu: FR-01 (eshop-sut/README.md:34); Slide 10 #5 Field Limits
- loai_nguon: SRS
- tien_dieu_kien: Tại /register nhập Họ Tên, Email mới hợp lệ; thử lần lượt từng mật khẩu bên dưới.
- expected: Mật khẩu `Abc12!x` (7 ký tự, đủ các nhóm) bị từ chối kèm thông báo lỗi; mật khẩu `Abc123!x` (8 ký tự, đủ các nhóm chữ hoa, chữ thường, số, ký tự đặc biệt) được chấp nhận và chuyển tới /login. Fail nếu mật khẩu 7 ký tự được chấp nhận hoặc mật khẩu 8 ký tự đạt đủ nhóm bị từ chối.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: CL-19 của AI dùng ví dụ thiếu nhóm ký tự chứ không kiểm giá trị biên độ dài vì prompt không nhắc phân tích giá trị biên; mục này tách riêng ranh giới 7 và 8 ký tự.

### SV-09
- ia: IA-02
- man_hinh: Register
- muc_kiem_tra: Từng ký tự đặc biệt trong tập cho phép (@ $ ! % * ? &) được chấp nhận trong mật khẩu
- can_cu: FR-01 (eshop-sut/README.md:34)
- loai_nguon: SRS
- tien_dieu_kien: Tại /register dùng Email mới cho mỗi lần thử, Họ Tên bất kỳ; thử lần lượt các mật khẩu `Abcd123@`, `Abcd123$`, `Abcd123!`, `Abcd123%`, `Abcd123*`, `Abcd123?`, `Abcd123&`.
- expected: Cả 7 mật khẩu đều được chấp nhận (mỗi mật khẩu chứa đúng một ký tự đặc biệt thuộc tập `@ $ ! % * ? &`) và đăng ký thành công chuyển tới /login. Fail nếu bất kỳ mật khẩu nào trong 7 mật khẩu trên bị báo "quá yếu" hoặc bị từ chối dù thoả đủ điều kiện của đặc tả.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI chỉ lấy một ký tự đại diện là `!` trong CL-19 thay vì kiểm từng ký tự trong tập; lỗi bộ lọc ký tự chỉ lộ khi thử nhiều giá trị khác nhau, AI không thực thi nên không thấy.

### SV-10
- ia: IA-02
- man_hinh: Profile
- muc_kiem_tra: Giá trị biên độ dài và chữ số đầu của Số điện thoại trên trang Hồ sơ
- can_cu: FR-04 (eshop-sut/README.md:65); Slide 10 #5 Field Limits
- loai_nguon: SRS
- tien_dieu_kien: Đăng nhập `test@eshop.com`, mở /profile; thử lần lượt từng giá trị SĐT bên dưới rồi bấm `Cập nhật`.
- expected: SĐT `091234567` (9 chữ số), `091234567890` (12 chữ số) và `9123456789` (10 chữ số nhưng không bắt đầu bằng 0) bị từ chối kèm thông báo lỗi; hệ thống chỉ chấp nhận SĐT bắt đầu bằng `0` và có 10 hoặc 11 chữ số. Fail nếu bất kỳ giá trị nào trong ba giá trị trên được lưu thành công.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: CL-22 của AI chỉ nêu các giá trị hợp lệ và một giá trị có chữ cái; phần giá trị biên không hợp lệ (9, 12 chữ số, số đầu khác 0) cần prompt yêu cầu phân tích biên, mà prompt của tôi chưa yêu cầu.

### SV-11
- ia: IA-02
- man_hinh: Register, Profile
- muc_kiem_tra: Từ chối Họ Tên chỉ chứa khoảng trắng
- can_cu: Nielsen #5 Error prevention; FR-01 (eshop-sut/README.md:32); Giả định GA7
- loai_nguon: Heuristic
- tien_dieu_kien: Tại /register nhập Họ Tên là 3 dấu cách, Email và mật khẩu hợp lệ; tại /profile xoá Họ Tên và nhập 3 dấu cách rồi bấm `Cập nhật`.
- expected: Cả /register và /profile đều từ chối Họ Tên chỉ gồm khoảng trắng và hiển thị thông báo yêu cầu nhập Họ Tên, không lưu giá trị rỗng về nội dung. Fail nếu hệ thống chấp nhận đăng ký hoặc cập nhật với Họ Tên chỉ gồm khoảng trắng, khiến lời chào trên Header chỉ còn `Chào,`.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: Thuộc tính `required` của trình duyệt chặn ô rỗng nên AI mặc định ô bắt buộc đã được bảo vệ; lỗ hổng chỉ xuất hiện với chuỗi toàn dấu cách mà AI không nghĩ tới.

### SV-12
- ia: IA-02
- man_hinh: Login, ForgotPassword
- muc_kiem_tra: Thuộc tính autocomplete và hành vi tự điền của trình duyệt trên ô OTP, ô Email và ô mật khẩu
- can_cu: WCAG 2.2 SC 1.3.5 Identify Input Purpose; Slide 10 #7 Assistive Hints
- loai_nguon: Heuristic
- tien_dieu_kien: Trình duyệt đã lưu một cặp tài khoản/mật khẩu cho localhost; mở /forgot-password, nhập email để sang Bước 2.
- expected: Ô OTP ở Bước 2 không bị trình duyệt tự điền email hay mật khẩu đã lưu (ô OTP không nhận giá trị trùng email) và các ô email, mật khẩu có thuộc tính `autocomplete` phù hợp (ví dụ `email`, `current-password`, `new-password`, `one-time-code`). Fail nếu ô OTP tự động hiện email đã lưu hoặc các ô trên không khai báo thuộc tính `autocomplete` phù hợp mục đích nhập.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: Lỗi này tôi quan sát được khi đối chiếu giao diện thật ở Bước 0 (ảnh chụp ô OTP tự điền email); AI chỉ đọc mô tả control nên không biết hành vi tự điền của trình duyệt.

### SV-13
- ia: IA-02
- man_hinh: ForgotPassword
- muc_kiem_tra: Hiển thị quy tắc mật khẩu mạnh cho ô Mật khẩu mới ở Bước 2
- can_cu: FR-03 (eshop-sut/README.md:58); Nielsen #6 Recognition rather than recall
- loai_nguon: Heuristic
- tien_dieu_kien: Đang ở Bước 2 trang /forgot-password sau khi lấy OTP.
- expected: Ở Bước 2, gần ô `Mật khẩu mới` hiển thị dòng gợi ý nêu đủ quy tắc mật khẩu (tối thiểu 8 ký tự, chữ hoa, chữ thường, số, ký tự đặc biệt) giống gợi ý trên /register để người dùng không phải nhớ. Fail nếu Bước 2 không có bất kỳ dòng gợi ý quy tắc mật khẩu nào gần ô `Mật khẩu mới`.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI chú ý tới quy tắc mật khẩu ở Register (CL-19) nhưng không đối chiếu chéo để thấy form Bước 2 thiếu gợi ý tương ứng; việc so sánh nhất quán giữa hai màn hình cần nhìn cả hai giao diện.

### SV-14
- ia: IA-02
- man_hinh: Register
- muc_kiem_tra: Dòng gợi ý mật khẩu liệt kê các ký tự đặc biệt được chấp nhận
- can_cu: FR-01 (eshop-sut/README.md:34); Slide 10 #7 Assistive Hints
- loai_nguon: SRS
- tien_dieu_kien: Mở /register và quan sát dòng gợi ý bên dưới ô Mật khẩu.
- expected: Dòng gợi ý dưới ô `Mật khẩu` nêu cụ thể các ký tự đặc biệt hợp lệ `@ $ ! % * ? &` để người dùng biết nên dùng ký tự nào. Fail nếu dòng gợi ý chỉ ghi chung chung "ký tự đặc biệt" mà không liệt kê tập ký tự được chấp nhận.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: Prompt chỉ yêu cầu kiểm tra có gợi ý hay không (CL-23) chứ không yêu cầu soát mức độ cụ thể của nội dung gợi ý so với đặc tả nên AI không tách mục này.

### SV-15
- ia: IA-04
- man_hinh: Profile, Header
- muc_kiem_tra: Duy trì trạng thái đăng nhập sau khi tải lại trang
- can_cu: FR-02 (eshop-sut/README.md:43); Nielsen #1 Visibility of system status
- loai_nguon: SRS
- tien_dieu_kien: Đăng nhập `test@eshop.com` / `Test1234!`, mở /profile rồi nhấn F5 (tải lại trang).
- expected: Sau khi tải lại /profile, Header vẫn hiển thị `Chào, <tên>` kèm nút `Đăng xuất` và khối Hồ sơ vẫn hiển thị đủ thông tin tài khoản, không bị đẩy về trạng thái khách. Fail nếu sau khi tải lại Header quay về `Đăng nhập`/`Đăng ký` hoặc trang hiển thị `Vui lòng đăng nhập` dù token đã được lưu phía client.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI chỉ nhìn từng màn hình tại một thời điểm và không mô phỏng thao tác tải lại trang; trạng thái phiên sau F5 phụ thuộc cách lưu token phía client nên AI không thể suy ra từ mô tả điều khoản.

### SV-16
- ia: IA-03
- man_hinh: Register, Login, ForgotPassword, Profile
- muc_kiem_tra: Tiêu đề tab trình duyệt mô tả riêng cho từng trang
- can_cu: WCAG 2.2 SC 2.4.2 Page Titled; Giả định GA8
- loai_nguon: Heuristic
- tien_dieu_kien: Mở lần lượt /register, /login, /forgot-password, /profile (đã đăng nhập) và đọc tiêu đề tab.
- expected: Mỗi trang trong 4 trang trên có tiêu đề tab (`document.title`) mô tả đúng chức năng và khác nhau giữa các trang (ví dụ phân biệt được trang đăng ký và đăng nhập). Fail nếu hai trang bất kỳ có cùng `document.title` hoặc tiêu đề tab không liên quan chức năng trang.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: Tiêu đề tab nằm ngoài vùng hiển thị của trang web nên AI khi liệt kê control từ nội dung trang không đưa vào; đây là điểm AI thường bỏ qua khi chỉ nhìn phần thân trang.

### SV-17
- ia: IA-03
- man_hinh: Register, Login, ForgotPassword, Profile, Header
- muc_kiem_tra: Hiển thị khung focus nhìn thấy được khi di chuyển bằng bàn phím
- can_cu: WCAG 2.2 SC 2.4.7 Focus Visible; Slide 10 #12 Hover and Focus
- loai_nguon: Heuristic
- tien_dieu_kien: Dùng phím Tab đi qua mọi ô nhập, nút và liên kết trên 5 vùng giao diện (đã đăng nhập khi kiểm Profile/Header).
- expected: Mỗi phần tử tương tác khi nhận focus bằng Tab có khung hoặc đổi màu nhìn rõ so với trạng thái không focus (đường viền, vòng sáng hoặc nền khác biệt). Fail nếu có ít nhất một phần tử tương tác nhận focus mà không có bất kỳ dấu hiệu thị giác nào cho biết đang focus.
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: Slide 12 nêu khả năng dùng chỉ bàn phím là điểm mù của AI; trạng thái focus chỉ thấy khi thao tác bàn phím thật và AI không có trải nghiệm đó.

### SV-18
- ia: IA-01
- man_hinh: Register, Login, ForgotPassword, Profile, Header
- muc_kiem_tra: Bố cục khi phóng to trình duyệt đến 200%
- can_cu: WCAG 2.2 SC 1.4.4 Resize Text, SC 1.4.10 Reflow; Slide 10 #17 Breakpoint Layout
- loai_nguon: Heuristic
- tien_dieu_kien: Ở viewport 1440px bấm Ctrl và dấu cộng đến mức phóng to 200%, mở lần lượt 5 vùng giao diện.
- expected: Ở mức phóng to 200% mọi nhãn, ô nhập, nút trên 5 vùng giao diện vẫn đọc được, không bị cắt hay chồng lên nhau và có thể thao tác mà không cần cuộn ngang. Fail nếu xuất hiện thanh cuộn ngang, hoặc nhãn, ô nhập, nút bị che hay chồng lên nhau ở mức 200%.
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: CL-10 của AI chỉ nêu 3 viewport cố định; prompt của tôi không nhắc tới người dùng phóng to chữ nên AI không thêm kịch bản phóng to trình duyệt.

### SV-19
- ia: IA-02
- man_hinh: Register, Login, ForgotPassword, Profile, Header
- muc_kiem_tra: Kích thước vùng chạm của nút và liên kết
- can_cu: WCAG 2.2 SC 2.5.8 Target Size (Minimum); Slide 10 #18 Element Overlap
- loai_nguon: Heuristic
- tien_dieu_kien: Mở DevTools đo kích thước các nút và liên kết (`Đăng nhập`, `Đăng ký`, `Quên mật khẩu?`, `Đăng ký ngay`, `Đăng nhập`, `Đăng xuất`); trên P3 thử chạm bằng ngón tay.
- expected: Mọi nút và liên kết dạng chữ trên 5 vùng giao diện có vùng chạm tối thiểu 24 x 24 CSS px (đo bằng `getBoundingClientRect()`), và trên điện thoại Android chạm đúng một lần vào phần tử cần chọn mà không bấm nhầm phần tử kề bên. Fail nếu có nút hoặc liên kết có chiều cao hoặc chiều rộng nhỏ hơn 24 CSS px, hoặc chạm một lần trên điện thoại Android kích hoạt nhầm phần tử kề bên.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: Kích thước vùng chạm chỉ cảm nhận được khi chạm thật trên điện thoại; AI không có thiết bị và khi đánh giá bố cục chỉ nhìn kiểu máy tính để bàn.

### SV-20
- ia: IA-02
- man_hinh: Profile
- muc_kiem_tra: Loại bàn phím ảo hiển thị khi chạm vào ô Số điện thoại
- can_cu: Slide 10 #5 Field Limits; WCAG 2.2 SC 1.3.5 Identify Input Purpose; Giả định NA2
- loai_nguon: Control
- tien_dieu_kien: Trên điện thoại Android (Chrome), đăng nhập và mở /profile, chạm vào ô `Số điện thoại`.
- expected: Khi chạm vào ô `Số điện thoại` trên điện thoại Android, bàn phím ảo hiển thị dạng bàn phím số hoặc bàn phím điện thoại (ô khai báo `type="tel"` hoặc `inputmode="numeric"`) để nhập chữ số nhanh. Fail nếu bàn phím chữ cái thông thường hiện ra và người dùng phải chuyển sang bàn phím số thủ công.
- nen_tang: P3 (P1, P2 N/A theo NA2)
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: Hành vi bàn phím ảo chỉ quan sát được trên thiết bị cảm ứng thật; AI không có điện thoại thật nên không đưa mục phụ thuộc thiết bị di động vào checklist.


## Ghi chú về các khía cạnh đề bài gợi ý nhưng không đưa thành mục kiểm tra (bổ sung 14/11/2026)

Đề bài (Mục 6, Task 1) nêu ví dụ các khía cạnh AI hay bỏ sót gồm **accessibility, RTL và dark mode**. Accessibility đã được phủ bằng các mục `CL-11` (tương phản), `CL-23` (label), `SV-01`/`SV-02`/`SV-17` (bàn phím, focus), `SV-18` (zoom 200%), `SV-19` (vùng chạm), `SV-12`/`SV-20` (mục đích ô nhập). Hai khía cạnh còn lại được SV khảo sát và quyết định **không lập mục kiểm tra**, với số liệu đo trên `P1` (Google Chrome 157, Playwright `emulateMedia`) như sau:

| Khía cạnh | Số liệu đo trên SUT | Quyết định của SV | Lý do |
|---|---|---|---|
| **Dark mode** | Với `colorScheme: 'light'` và `'dark'`, nền khung form `/register` đều là `rgb(255, 255, 255)`; số quy tắc CSS chứa `prefers-color-scheme` hoặc lớp `.dark` = `0`. | Không lập mục | Đặc tả `eshop-sut/README.md` không yêu cầu giao diện tối và SUT không cài đặt chế độ này; một mục "phải có dark mode" sẽ không có căn cứ đặc tả (oracle). Kết quả đo được ghi lại để chứng minh đã kiểm tra. |
| **RTL (right-to-left)** | `<html lang="en">`, không có thuộc tính `dir`; toàn bộ nội dung là tiếng Việt (viết trái sang phải). | Không lập mục | SUT chỉ có một ngôn ngữ tiếng Việt, không hỗ trợ ngôn ngữ viết phải sang trái, nên bố cục RTL không thể kích hoạt. |

> Quan sát phụ khi khảo sát: thuộc tính `<html lang="en">` không khớp nội dung tiếng Việt (WCAG 2.2 SC 3.1.1 Language of Page). Đây là phát hiện ngoài phạm vi 59 mục đã chạy nên chỉ ghi nhận tại đây, chưa lập Bug.

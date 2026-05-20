**RoomBooking**

**Software Requirements Specification**

Phiên bản Draft 1.0.0 · 19/05/2026

| **Dự án** |   |
|---|---|
| **Loại tài liệu** | Software Requirements Specification (SRS) |
| **Trạng thái** | Draft – Phiên bản 1.0.0 |
| **Được chuẩn bị bởi** | Đội kỹ thuật Slitigenz |
| **Ngày** | 19/05/2026 |

**Mục lục**

# Lịch sử Phiên bản

| **Phiên bản** | **Ngày** | **Mô tả** | **Tác giả** |
|---|---|---|---|
| 1.0.0 | 19/05/2026 | Bản SRS mẫu sinh thử để kiểm tra template <br> Đặc tả module Quản lý đặt phòng họp | Claude |

# Giới thiệu

- **Mục đích:** Xác định các yêu cầu chức năng và phi chức năng cho hệ thống RoomBooking — quản lý đặt phòng họp nội bộ. Tài liệu là hợp đồng chính thức giữa các bên liên quan và đội phát triển.
- **Phạm vi:** Bao gồm module Quản lý đặt phòng họp. Không bao gồm tích hợp lịch ngoài (Google Calendar, Outlook) và quản lý thiết bị phòng họp.
- **Đối tượng:** Quản lý sản phẩm, kỹ sư backend, kỹ sư QA, kiến trúc sư và các bên liên quan nghiệp vụ.

## Định nghĩa, Từ viết tắt và Ký hiệu

| **Thuật ngữ / Từ viết tắt** | **Định nghĩa** |
|---|---|
| SRS | Software Requirements Specification |
| FR | Functional Requirement — Yêu cầu chức năng |
| NFR | Non-Functional Requirement — Yêu cầu phi chức năng |
| Booking | Một lượt đặt phòng họp gắn với khung giờ cụ thể |
| Slot | Khung thời gian đặt phòng, đơn vị 30 phút |

## Tổng quan Tài liệu

Phần còn lại của tài liệu được tổ chức như sau:

- Mục 2 — Mô tả Tổng quan: bối cảnh hệ thống, phân loại người dùng và yêu cầu hành vi chung
- Mục 3 — Yêu cầu Cụ thể: yêu cầu chức năng và đặc tả chi tiết từng tính năng
- Mục 4 — Yêu cầu Phi chức năng: hiệu năng, bảo mật, độ tin cậy và khả năng mở rộng

# Mô tả Tổng quan

## Bối cảnh Sản phẩm

RoomBooking là một sản phẩm độc lập mới phục vụ đặt phòng họp trong nội bộ tổ chức. Nó hoạt động trong bối cảnh sau:

- Xác thực người dùng qua hệ thống SSO nội bộ của tổ chức.
- Lưu trữ dữ liệu booking trong cơ sở dữ liệu quan hệ.
- Gửi email xác nhận qua dịch vụ SMTP nội bộ.

## Chức năng Sản phẩm

| **Lĩnh vực Tính năng** | **Tóm tắt** |
|---|---|
| Quản lý đặt phòng họp | Xem lịch phòng, tạo booking, hủy booking theo khung giờ |

## Phân loại Người dùng và Đặc điểm

| **Phân loại Người dùng** | **Mô tả** | **Trình độ Kỹ thuật** | **Tần suất Sử dụng** |
|---|---|---|---|
| Nhân viên | Người đặt và quản lý booking của chính mình | Thấp – Trung bình | Hàng ngày |
| Quản trị viên (Admin) | Quản lý danh mục phòng, xem và hủy mọi booking | Trung bình | Hàng tuần |

## Yêu cầu Hành vi Chung

Các quy tắc sau áp dụng toàn cục cho tất cả tính năng, trừ khi có quy định riêng tại từng tính năng.

### Quy tắc Validation Đầu vào

| Tình huống | Hành vi Hệ thống | Ghi chú |
|---|---|---|
| Trường bắt buộc để trống | Chặn submit, highlight đỏ, hiển thị lỗi inline "Trường này không được để trống". | Áp dụng cho mọi form. |
| Khung giờ không hợp lệ | Giờ kết thúc phải sau giờ bắt đầu; chặn submit nếu vi phạm. | Đơn vị slot tối thiểu 30 phút. |

### Quy tắc Xử lý Lỗi & Phản hồi Hệ thống

| Tình huống | Hành vi Hệ thống | Ghi chú |
|---|---|---|
| Lỗi server | Trả HTTP 500, hiển thị toast lỗi + nút Thử lại. | Không mất dữ liệu form đang nhập. |
| Xung đột booking | Trả HTTP 409, hiển thị "Khung giờ đã được đặt". | Xem BR tại FEAT-002. |

### Quy tắc Tìm kiếm, Lọc & Sắp xếp

| Tình huống | Hành vi Hệ thống | Ghi chú |
|---|---|---|
| Lọc lịch phòng | Lọc theo ngày và theo phòng; áp dụng ngay khi đổi giá trị (onChange). | Mặc định: ngày hiện tại. |
| Sắp xếp danh sách booking | Mặc định theo giờ bắt đầu tăng dần `[Mặc định]`. | |

### Chú giải Loại & Thuộc tính thành phần

Bảng chú giải dưới đây định nghĩa các giá trị **Loại** và **Thuộc tính** dùng trong toàn bộ đặc tả thành phần. Khi viết đặc tả tính năng, **tái sử dụng** các giá trị này, không tự định nghĩa giá trị mới.

{{LEGEND}}

# Yêu cầu Cụ thể

Mỗi lĩnh vực tính năng gồm: bảng yêu cầu chức năng (FR), đặc tả use case chi tiết, màn hình wireframe và đặc tả component.

## Quản lý đặt phòng họp

### Danh sách Yêu cầu Chức năng

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| FEAT-001 | Xem lịch phòng họp theo ngày | Very High |
| FEAT-002 | Tạo booking mới | Very High |
| FEAT-003 | Hủy booking | High |

### Đặc tả Chi tiết — Xem lịch phòng họp (FEAT-001)

| **Đặc tả Use Case** | **Đặc tả Use Case** |
|---|---|
| **Mã tính năng (Use case / Feature)** | FEAT-001 |
| **Tác nhân** | Nhân viên, Admin |
| **Mô tả** | Người dùng xem lịch các phòng họp theo ngày, nhận biết slot trống và slot đã được đặt. |
| **Sự kiện kích hoạt** | Người dùng truy cập màn hình Lịch phòng họp. |
| **Tiền điều kiện** | Người dùng đã đăng nhập. Hệ thống đã có danh mục phòng họp. |
| **Luồng chính** | Hệ thống tải danh sách phòng và booking của ngày hiện tại. <br> Hiển thị lưới lịch: hàng = phòng, cột = slot 30 phút. <br> Người dùng đổi ngày hoặc lọc theo phòng. <br> Hệ thống cập nhật lưới theo bộ lọc. |
| **Luồng ngoại lệ / Xử lý lỗi** | Không có phòng nào: Hiển thị empty state. <br> Lỗi tải dữ liệu: Hiển thị thông báo lỗi và nút Thử lại theo Mục 2.4.2. |
| **Hậu điều kiện** | Lưới lịch hiển thị đúng theo ngày và bộ lọc đang áp dụng. |

#### Sơ đồ luồng

| [ Sơ đồ luồng — sẽ được bổ sung ] |
|---|

#### Giao diện / Wireframe

Hình 1. Màn hình lưới lịch phòng họp theo ngày

#### Đặc tả các thành phần

##### Thanh điều khiển

| STT / ID | Tên / Label | Loại | Thuộc tính | Mô tả |
|---|---|---|---|---|
|   | Chọn ngày | Date Picker | Required | Chọn ngày xem lịch. Mặc định: ngày hiện tại. |
|   | Lọc theo phòng | Select (Multi) |   | Lọc lưới theo một hoặc nhiều phòng. Mặc định: hiển thị tất cả. |
|   | Tạo booking | Button (Primary) |   | Mở pop-up Tạo booking mới (FEAT-002). |

##### Lưới lịch

| STT / ID | Tên / Label | Loại | Thuộc tính | Mô tả |
|---|---|---|---|---|
|   | Ô slot trống | Cell |   | Slot chưa có booking. Click để mở pop-up Tạo booking với giờ tương ứng. |
|   | Ô slot đã đặt | Cell + Tag |   | Slot đã có booking. Hiển thị tên người đặt + tiêu đề cuộc họp. |

### Đặc tả Chi tiết — Tạo booking mới (FEAT-002)

| **Đặc tả Use Case** | **Đặc tả Use Case** |
|---|---|
| **Mã tính năng (Use case / Feature)** | FEAT-002 |
| **Tác nhân** | Nhân viên, Admin |
| **Mô tả** | Người dùng tạo một booking cho phòng họp ở khung giờ mong muốn. |
| **Sự kiện kích hoạt** | Người dùng nhấn "Tạo booking" hoặc click vào một ô slot trống. |
| **Tiền điều kiện** | Người dùng đã đăng nhập. Có ít nhất một phòng họp khả dụng. |
| **Luồng chính** | Hệ thống hiển thị pop-up Tạo booking. <br> Người dùng nhập tiêu đề, chọn phòng, ngày, giờ bắt đầu và kết thúc. <br> Hệ thống validate theo Mục 2.4.1. <br> Người dùng nhấn "Xác nhận". <br> Hệ thống tạo booking, gửi email xác nhận và hiển thị toast thành công. |
| **Luồng ngoại lệ / Xử lý lỗi** | Khung giờ đã được đặt: Hiển thị lỗi inline "Khung giờ đã được đặt". <br> Validation thất bại: Highlight trường lỗi theo Mục 2.4.1. <br> Người dùng hủy: Đóng pop-up, không lưu dữ liệu. |
| **Hậu điều kiện** | Booking mới được tạo và hiển thị trên lưới lịch. <br> Email xác nhận được gửi cho người đặt. |

#### Sơ đồ luồng

| [ Sơ đồ luồng — sẽ được bổ sung ] |
|---|

#### Giao diện / Wireframe

Hình 2. Pop-up tạo booking mới

#### Đặc tả các thành phần

##### Pop-up Tạo booking

| STT / ID | Tên / Label | Loại | Thuộc tính | Mô tả |
|---|---|---|---|---|
| Thông tin booking | Thông tin booking | Thông tin booking | Thông tin booking | Thông tin booking |
|   | Tiêu đề cuộc họp | Input (Text) | Required <br> Max_150_char | Tiêu đề mô tả cuộc họp. |
|   | Phòng họp | Select (Single) | Required | Chọn từ danh sách phòng họp khả dụng. |
|   | Ngày | Date Picker | Required | Ngày diễn ra cuộc họp. Không nhận ngày quá khứ. |
|   | Giờ bắt đầu | Time Picker | Required | Đơn vị slot 30 phút. |
|   | Giờ kết thúc | Time Picker | Required | Phải sau giờ bắt đầu. |
|   | Ghi chú | Textarea | Max_500_char | Ghi chú tùy chọn cho cuộc họp. |
| Hành động | Hành động | Hành động | Hành động | Hành động |
|   | Hủy | Button |   | Đóng pop-up, không lưu dữ liệu. |
|   | Xác nhận | Button (Primary) |   | Ấn để tạo booking. |

#### Business Rules / System Behavior

| Mã BR | Mô tả |
|---|---|
|   | Hệ thống phải **chặn tạo booking trùng khung giờ** trên cùng một phòng. Nếu khung giờ giao với một booking đã tồn tại, hệ thống từ chối với phản hồi HTTP 409. |
|   | Không cho phép tạo booking cho **khung giờ trong quá khứ**. |
|   | Sau khi tạo thành công, hệ thống phải gửi **email xác nhận** đến địa chỉ của người đặt. |
|   | Mỗi booking phải được ghi vào **audit log** kèm người tạo và thời điểm tạo. |

### Đặc tả Chi tiết — Hủy booking (FEAT-003)

| **Đặc tả Use Case** | **Đặc tả Use Case** |
|---|---|
| **Mã tính năng (Use case / Feature)** | FEAT-003 |
| **Tác nhân** | Nhân viên (booking của mình), Admin (mọi booking) |
| **Mô tả** | Người dùng hủy một booking không còn nhu cầu sử dụng. |
| **Sự kiện kích hoạt** | Người dùng nhấn "Hủy" trên chi tiết một booking. |
| **Tiền điều kiện** | Người dùng đã đăng nhập. Booking tồn tại và chưa diễn ra. |
| **Luồng chính** | Người dùng nhấn "Hủy booking". <br> Hệ thống hiển thị confirmation dialog. <br> Người dùng xác nhận. <br> Hệ thống hủy booking, giải phóng slot và gửi email thông báo hủy. |
| **Luồng ngoại lệ / Xử lý lỗi** | Booking đã bắt đầu/đã qua: Ẩn nút Hủy. <br> Không có quyền: Nút Hủy ẩn theo RBAC. <br> Người dùng hủy thao tác: Đóng dialog, không thay đổi. |
| **Hậu điều kiện** | Booking chuyển sang trạng thái Đã hủy. <br> Slot được giải phóng trên lưới lịch. |

#### Sơ đồ luồng

| [ Sơ đồ luồng — sẽ được bổ sung ] |
|---|

#### Giao diện / Wireframe

Hình 3. Confirmation dialog hủy booking

#### Đặc tả các thành phần — Confirmation Dialog

| STT / ID | Tên / Label | Loại | Mô tả |
|---|---|---|---|
|   | Tiêu đề | Text (Bold) | "Hủy booking?" |
|   | Mô tả | Text | "Booking [Tiêu đề] sẽ bị hủy và slot được giải phóng. Hành động không thể hoàn tác." |
|   | Hủy | Button | Đóng dialog, không thực hiện hành động. |
|   | Xác nhận | Button (Danger) | Thực hiện hủy booking. |

#### Business Rules / System Behavior

| Mã BR | Mô tả |
|---|---|
|   | Nhân viên chỉ được hủy **booking do chính mình tạo**. Admin được hủy mọi booking. |
|   | Không cho phép hủy booking **đã bắt đầu hoặc đã kết thúc**. |
|   | Sau khi hủy thành công, hệ thống gửi **email thông báo hủy** cho người đặt. |

# Yêu cầu Phi chức năng

## Hiệu năng

- Lưới lịch phải tải xong trong vòng 2 giây với tối đa 50 phòng × 48 slot/ngày.
- Thao tác tạo/hủy booking phản hồi trong vòng 1 giây (p95).

## Độ tin cậy và Tính sẵn sàng

- Hệ thống đạt uptime tối thiểu 99,5% trong giờ làm việc.
- Dữ liệu booking được sao lưu hằng ngày.

## Bảo mật

- Mọi phiên xác thực qua SSO nội bộ, token có thời hạn.
- Phân quyền theo vai trò: Nhân viên chỉ thao tác booking của mình; Admin toàn quyền.

## Khả năng Bảo trì

- Mã nguồn tuân theo coding convention của tổ chức, có unit test cho logic chống trùng booking.

## Khả năng Mở rộng

- Kiến trúc cho phép bổ sung tích hợp lịch ngoài (Google Calendar, Outlook) ở phiên bản sau mà không phá vỡ module hiện tại.

## Khả năng Sử dụng

- Giao diện hỗ trợ tiếng Việt, thao tác tạo booking không quá 4 bước.

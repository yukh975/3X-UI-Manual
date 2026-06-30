# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 Tiếng Việt · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Hướng dẫn sử dụng cho bảng điều khiển [3x-ui](https://github.com/MHSanaei/3x-ui) — tài liệu hướng dẫn toàn diện được viết cho bảng điều khiển phiên bản **v3.4.2**.

> **Bản sao chỉ đọc.** Kho lưu trữ GitHub này là bản sao một chiều — nguồn của tài liệu nằm trên GitLab riêng tư và được đẩy lên đây tự động, vì vậy luôn được cập nhật. Phát hiện lỗi hoặc thiếu chính xác? Vui lòng [mở Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull request không được chấp nhận** (chúng sẽ bị đóng tự động) — các sửa đổi được thực hiện tại nguồn.

## Mục lục

| Tệp | Ngôn ngữ | Định dạng |
| --- | --- | --- |
| **[3X-UI-MANUAL.ar.md](3X-UI-MANUAL.ar.md)** · [PDF](pdf/3X-UI-MANUAL.ar.pdf) | 🇸🇦 العربية | Markdown + PDF |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.es.md](3X-UI-MANUAL.es.md)** · [PDF](pdf/3X-UI-MANUAL.es.pdf) | 🇪🇸 Español | Markdown + PDF |
| **[3X-UI-MANUAL.fa.md](3X-UI-MANUAL.fa.md)** · [PDF](pdf/3X-UI-MANUAL.fa.pdf) | 🇮🇷 فارسی | Markdown + PDF |
| **[3X-UI-MANUAL.id.md](3X-UI-MANUAL.id.md)** · [PDF](pdf/3X-UI-MANUAL.id.pdf) | 🇮🇩 Bahasa Indonesia | Markdown + PDF |
| **[3X-UI-MANUAL.ja.md](3X-UI-MANUAL.ja.md)** · [PDF](pdf/3X-UI-MANUAL.ja.pdf) | 🇯🇵 日本語 | Markdown + PDF |
| **[3X-UI-MANUAL.pt.md](3X-UI-MANUAL.pt.md)** · [PDF](pdf/3X-UI-MANUAL.pt.pdf) | 🇧🇷 Português | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |
| **[3X-UI-MANUAL.tr.md](3X-UI-MANUAL.tr.md)** · [PDF](pdf/3X-UI-MANUAL.tr.pdf) | 🇹🇷 Türkçe | Markdown + PDF |
| **[3X-UI-MANUAL.uk.md](3X-UI-MANUAL.uk.md)** · [PDF](pdf/3X-UI-MANUAL.uk.pdf) | 🇺🇦 Українська | Markdown + PDF |
| **[3X-UI-MANUAL.vi.md](3X-UI-MANUAL.vi.md)** · [PDF](pdf/3X-UI-MANUAL.vi.pdf) | 🇻🇳 Tiếng Việt | Markdown + PDF |
| **[3X-UI-MANUAL.zh-CN.md](3X-UI-MANUAL.zh-CN.md)** · [PDF](pdf/3X-UI-MANUAL.zh-CN.pdf) | 🇨🇳 简体中文 | Markdown + PDF |
| **[3X-UI-MANUAL.zh-TW.md](3X-UI-MANUAL.zh-TW.md)** · [PDF](pdf/3X-UI-MANUAL.zh-TW.pdf) | 🇹🇼 繁體中文 | Markdown + PDF |

## Có gì mới trong 3.4.2

Phiên bản 3.4.2 là một bản cập nhật lớn: WireGuard chuyển sang mô hình đa khách hàng, REALITY có thêm trình quét đích trực tiếp, các bộ cân bằng tải nhận được các tab Observatory/Burst Observatory, và đã thêm xác nhận các cài đặt nhạy cảm bằng mã 2FA. Dưới đây là các thay đổi so với 3.4.1, được nhóm theo các mục của hướng dẫn.

### Thay đổi ở phần 1 — Giới thiệu, yêu cầu và cài đặt

- Trong menu bên (và trong ngăn kéo trên di động) xuất hiện nút **«Tài liệu»** (biểu tượng quyển sách) — mở tài liệu chính thức `https://docs.sanaei.dev/`.
- Phiên bản Xray tối thiểu mà bảng điều khiển cập nhật lên được nâng lên **26.6.27** (đi kèm — lõi Xray 26.6.27).

### Thay đổi ở phần 2 — Đăng nhập bảng điều khiển và bảo mật truy cập

- Khi bật 2FA, việc thay đổi tên đăng nhập/mật khẩu quản trị và việc tắt 2FA nay yêu cầu **nhập mã hiện tại** từ ứng dụng xác thực (xác nhận các thay đổi nhạy cảm).
- LDAP: công tắc mới **«Bỏ qua kiểm tra chứng chỉ TLS»** (`ldapInsecureSkipVerify`) — tắt việc kiểm tra chứng chỉ khi dùng LDAPS; chỉ khả dụng khi đã bật «Sử dụng TLS (LDAPS)».

### Thay đổi ở phần 3 — Tổng quan / Bảng điều khiển chính

- Nút phiên bản bảng điều khiển nay luôn mở cửa sổ cập nhật (xem phần 16 — kênh dev).
- Cải tiến **khả năng truy cập** xuyên suốt: nhãn aria cho các biểu tượng và kích hoạt phần tử bằng Enter/Space (cho trình đọc màn hình và điều hướng bằng bàn phím).

### Thay đổi ở phần 4 — Inbound: tạo và các tham số chung

- Thao tác **«Xuất tất cả liên kết»** nay tạo liên kết qua engine đăng ký — áp dụng mẫu nhận xét cho từng khách hàng và ưu tiên các endpoint Host được quản lý (trước đây có nhận xét cố định `inbound-email`).

### Thay đổi ở phần 5 — Giao thức

- **WireGuard chuyển sang mô hình đa khách hàng.** Các peer nay là khách hàng thông thường (với việc tự động cấp địa chỉ trong tunnel, hỗ trợ đăng ký, giới hạn lưu lượng/thời hạn và nhóm); danh sách «Peer» inline trong biểu mẫu inbound đã bị xóa.
- Với WireGuard-inbound đã thêm trường **DNS** có thể cấu hình (mặc định `1.1.1.1, 1.0.0.1`) và **thẻ cấu hình khách hàng** — sao chép/tải xuống/QR của `.conf` đầy đủ và liên kết `wireguard://`/`wg://`.

### Thay đổi ở phần 6 — Transport (Stream Settings)

- Với XHTTP, đối với các inbound mới, tham số `maxConnections` trong **xmux** nay mặc định là **6** (trước đây `0` — không giới hạn). Các inbound hiện có giữ nguyên giá trị của mình.

### Thay đổi ở phần 7 — Bảo mật kết nối: TLS, XTLS và REALITY

- Đã thêm **trình quét đích REALITY trực tiếp**: các nút **«Quét»** (kiểm tra đích hiện tại «trực tiếp») và **«Tìm đích»** (quét một tên miền hoặc dải **IP/CIDR** và chọn các đích phù hợp theo chứng chỉ của chúng). Các trường «Đích» và SNI nay để trống khi lần đầu chọn REALITY.

### Thay đổi ở phần 8 — Khách hàng

- Việc gia hạn thời hạn/hạn mức qua `bulkAdjust` nay **tự động bật lại** khách hàng đã bị tắt chỉ vì hết hạn mức (hết hạn hoặc vượt quá hạn mức), nếu việc gia hạn đưa họ trở lại trong giới hạn. Những khách hàng bị tắt thủ công hoặc vẫn còn hết hạn mức vẫn bị tắt.

### Thay đổi ở phần 9 — Nhóm khách hàng

- **«Đặt lại lưu lượng»** của nhóm nay chỉ đặt về 0 **bộ đếm của chính nhóm**; các bộ đếm, hạn mức và trạng thái của từng khách hàng không bị ảnh hưởng, không cần khởi động lại Xray. Đây là thay đổi so với hành vi trước đây (trước đây lưu lượng của tất cả khách hàng trong nhóm bị đặt lại).

### Thay đổi ở phần 10 — Đăng ký (Subscription)

- Trong các **host được quản lý**, trường **VLESS route** đã được định nghĩa lại: nay là một giá trị duy nhất `0-65535` (chứ không phải danh sách cổng), và nó thực sự được «nhúng» vào UUID của mỗi đăng ký (raw/JSON/Clash).
- Biến `{{EMAIL}}` (và đồng nghĩa `{{USERNAME}}`) trong mẫu nhận xét nay chỉ hiển thị trên **liên kết đầu tiên** của khách hàng — giống như khối lưu lượng/thời hạn.

### Thay đổi ở phần 11 — Xray: định tuyến, outbounds, DNS và tiện ích mở rộng

- **Bộ cân bằng tải**: trang được chia thành các tab **«Cài đặt bộ cân bằng tải»** và **«Observatory»**; thay vì JSON thô — các biểu mẫu Observatory và Burst Observatory (với Burst đã thêm trường **«Phương thức HTTP»**). Bộ cân bằng tải Random/Round-robin với `fallbackTag` nay tự động tạo Burst Observatory.
- Khi xóa outbound hoặc bộ cân bằng tải, bảng điều khiển tự dọn sạch các tham chiếu liên quan trong định tuyến và hiển thị **xem trước hậu quả** trong hộp thoại xác nhận.
- Trong các quy tắc định tuyến, tiêu chí mạng **L4** được ghi vào cấu hình bằng chữ thường (`tcp`/`udp`), còn trong bảng hiển thị bằng chữ hoa.
- Các lỗi trong biểu mẫu thêm/sửa bộ cân bằng tải nay được trì hoãn cho đến khi chạm vào trường lần đầu hoặc khi thử lưu.

### Thay đổi ở phần 12 — Node (đa bảng điều khiển, master/slave)

- Thông báo «đã lưu cục bộ, node ngoại tuyến — sẽ đồng bộ sau» nay chỉ hiển thị khi node thực sự ngoại tuyến hoặc đã tắt (trước đây — mỗi khi lưu trên node trực tuyến).

### Thay đổi ở phần 16 — Vận hành: sao lưu, log, cập nhật, CLI

- Tên các tệp sao lưu nay chứa địa chỉ máy chủ và **ngày-giờ**: `{host}_YYYY-MM-DD_HHMMSS.db` (`.dump` cho PostgreSQL), ví dụ `panel.example.com_2026-06-27_000000.db` — cả khi tải xuống từ bảng điều khiển lẫn trong các bản sao lưu do bot Telegram gửi.
- Có thể bật **kênh dev** của bản cập nhật từ bản dựng ổn định: nút phiên bản luôn mở cửa sổ cập nhật, xuất hiện công tắc **«Kênh dev»** với cảnh báo về tính không ổn định và việc không có rollback tự động.

---

Được tạo từ việc phân tích các tệp nguồn của bảng điều khiển. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

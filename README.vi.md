# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 Tiếng Việt · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Hướng dẫn sử dụng cho bảng điều khiển [3x-ui](https://github.com/MHSanaei/3x-ui) — tài liệu hướng dẫn toàn diện được viết cho bảng điều khiển phiên bản **v3.5.0**.

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

## Có gì mới trong 3.5.0

Phiên bản 3.5.0 là một bản phát hành lớn: MTProto chuyển sang mô hình đa khách hàng (engine mtg-multi, secret cá nhân, hạn mức và ad-tag), Hosts được quản lý trở thành host nhóm (nhiều inbound và nhiều địa chỉ trong một bản ghi), khôi phục trên panel PostgreSQL chấp nhận bản sao lưu SQLite, outbound có thêm «Target Strategy», chế độ kiểm tra «Real delay» và các cột Egress/Country, bộ cân bằng tải có thể dùng một bộ cân bằng tải khác làm fallback. Đi kèm là lõi Xray 26.7.11. Dưới đây là các thay đổi so với 3.4.2, được nhóm theo các mục của hướng dẫn.

### Thay đổi ở phần 1 — Giới thiệu, yêu cầu và cài đặt

- Lõi Xray được cập nhật lên **26.7.11**. Các di chuyển tự động đi kèm: các phương thức mã hóa Shadowsocks `none`/`plain` và VMess `none`/`zero` đã bị xóa khỏi lõi (các cấu hình đã lưu được ghi lại tự động), còn VLESS/Trojan-outbound không mã hóa đến địa chỉ công khai bị từ chối khi lưu.
- Lệnh mới **`x-ui pgclient [phiên bản]`** và mục **10. Install/Upgrade client tools (pg_dump/pg_restore)** trong menu PostgreSQL — cài đặt/cập nhật các công cụ client PostgreSQL.
- Sửa lỗi script: cài đặt PostgreSQL và fail2ban trên họ RHEL (EPEL), Arch không còn chạy `pacman -Syu` đầy đủ, tên nhị phân Xray chính xác trên ARM 32-bit (`xray-linux-arm32`), xác nhận IPv4 được tự phát hiện trước khi phát hành chứng chỉ IP, đã sửa thông báo sai «Your input is invalid» khi chọn cổng ACME mặc định.

### Thay đổi ở phần 2 — Đăng nhập bảng điều khiển và bảo mật truy cập

- Giới hạn IP: kết nối «chết» nay chỉ bị chặn **một lần**, chứ không phải ở mỗi lần quét 10 giây — bộ đếm fail2ban không còn bị tăng ảo, không cần nâng cao `maxretry` nữa.

### Thay đổi ở phần 4 — Inbounds: tạo mới và các tham số chung

- Danh sách inbound có thêm **tìm kiếm** (theo ghi chú, cổng và giao thức), còn các danh sách thả xuống chọn node («Развернуть на», bộ lọc «Node») nay hỗ trợ tìm kiếm khi nhập.

### Thay đổi ở phần 5 — Giao thức

- **MTProto chuyển sang mô hình đa khách hàng** (engine mtg-multi): người dùng MTProto nay là các client thông thường với secret, hạn mức, thời hạn, ad-tag riêng và liên kết `tg://proxy` cá nhân. Trường «Secret» ở cấp inbound đã bị bỏ (các inbound hiện có được chuyển đổi tự động), «FakeTLS domain» trở thành domain mặc định cho các secret mới. Các trường inbound mới: **Max connections** (giới hạn kết nối), **Public IPv4/IPv6** (cho ad-tag middle proxy). Các thay đổi của client được áp dụng «ngay lập tức», không làm rơi các phiên Telegram của người khác.
- WireGuard: menu inbound nhận được bộ thao tác client đầy đủ (Export All URLs, liên kết/hủy liên kết, nhóm), phần xuất được chia thành các tab **Config** và **Links**, trường **«IP được phép WireGuard» nay có thể chỉnh sửa** (nhiều mục nhập cách nhau bằng dấu phẩy), còn trong cấu hình client của inbound trên node, `Endpoint` nay trỏ đến địa chỉ của node.

### Thay đổi ở phần 7 — Bảo mật kết nối: TLS, XTLS và REALITY

- Tổ hợp **Finalmask + REALITY bị từ chối** khi lưu (nó từng làm Xray-core sập ở kết nối đầu tiên); placeholder minClientVer được cập nhật lên 26.3.27.
- Loại mặt nạ TCP Finalmask mới — **XMC (Minecraft)**: ngụy trang luồng thành lưu lượng Minecraft (Hostname, Usernames, Password bắt buộc với tự động tạo).

### Thay đổi ở phần 8 — Clients

- Cột mới **«Tốc độ»** — tốc độ trực tiếp của từng client (↑/↓, trung bình trượt ~5 giây).
- Tìm kiếm client lại tìm được theo **Telegram ID**; trong biểu mẫu client, các inbound đã tắt bị ẩn khỏi danh sách liên kết; đã sửa việc tích lũy bản ghi trùng lặp trong cửa sổ «Hủy liên kết».
- Client MTProto có các trường riêng: **«MTProto secret»** (với nút tạo lại) và **«Ad-tag (kênh tài trợ)»** (32 ký tự hex); hạn mức và thời hạn nay thực sự được áp dụng cho MTProto.

### Thay đổi ở phần 9 — Nhóm khách hàng

- Cửa sổ thông tin client nay hiển thị **nhóm** của client.

### Thay đổi ở phần 10 — Đăng ký (Subscription)

- **Hosts được quản lý trở thành host nhóm**: một bản ghi bao phủ **nhiều inbound** (chọn nhiều) và **nhiều địa chỉ** (nhập dạng thẻ, mỗi mục có thể có `:cổng` riêng; tự động gợi ý địa chỉ; để trống — kế thừa địa chỉ của inbound). Các cột của danh sách hiển thị chip địa chỉ và inbound (với «+N»), các thao tác và API làm việc với nhóm (`groupId`), xuất hiện endpoint hàng loạt `POST /panel/api/hosts/bulk/add`. Việc sắp xếp host nay là toàn cục (theo thứ tự, sau đó theo remark).
- Nội dung **thông báo** (`subAnnounce`) nay được hiển thị dưới dạng banner trên trang thông tin đăng ký; các mẫu tùy chỉnh có sẵn biến `announce`.
- Trang thông tin trong trình duyệt nay cũng mở được qua **liên kết JSON/Clash** (không chỉ qua liên kết chính).
- Các cài đặt host **Final Mask** và **Allow insecure** nay cũng có hiệu lực tương ứng trong các liên kết raw (`fm=`) và cho **Hysteria2** (`insecure=1` / `skip-cert-verify: true`).
- Phạm vi «Khoảng thời gian cập nhật đăng ký» (`subUpdates`) được sửa thành **0–525600** (giới hạn UI cũ 168 từng chặn việc lưu cài đặt sau khi nâng cấp từ 2.x).
- Các client **WireGuard gốc nay được đưa vào đăng ký Clash và JSON** (trước đây — chỉ vào raw).

### Thay đổi ở phần 11 — Xray: định tuyến, outbounds, DNS và phần mở rộng

- Trình chỉnh sửa outbound: trường mới **«Target Strategy»** (11 giá trị từ `AsIs` đến `ForceIPv4`), chế độ kiểm tra **«Real delay»** (toàn bộ thời gian bao gồm cả thiết lập tunnel; chế độ HTTP nay được đo trên kết nối «ấm»), các cột **Egress** (IP đầu ra ẩn sau biểu tượng «con mắt») và **Country** (cờ + quốc gia, nhãn WARP) sau bài kiểm tra HTTP/Real.
- **Fallback của bộ cân bằng tải có thể trỏ đến một bộ cân bằng tải khác**: bảng điều khiển tự xây dựng đối tượng loopback ẩn (`_bl_…`), bảo vệ khỏi vòng lặp và khỏi việc xóa bộ cân bằng tải đang được sử dụng; tiền tố `_bl_` được dành riêng.
- Tab «Định tuyến cơ bản» nhận được bộ chọn **«Default Outbound»** — outbound nào xử lý lưu lượng không khớp với bất kỳ quy tắc nào (outbound được chọn sẽ được chuyển lên vị trí đầu tiên).
- Các máy chủ DNS trên IP riêng tư không còn bị quy tắc `geoip:private` chặn — bảng điều khiển tự duy trì một quy tắc allow được quản lý.
- Happy Eyeballs trong cài đặt dial (sockopt) nay thực sự được bật; «Try delay» mặc định 250 ms, giá trị `0` đặt rõ ràng được giữ nguyên.
- Nhập đăng ký outbound: các liên kết `ss://` có `?plugin=`/dấu `/` ở cuối nay được phân tích cổng chính xác.

### Thay đổi ở phần 12 — Nút (đa bảng điều khiển, master/slave)

- Gói các bản sửa lỗi: lưu client không thay đổi không còn phá vỡ lưu lượng đang chạy của các inbound trên nút; các ghi đè Host của nút được nhận vào master ở lần chấp nhận đầu tiên; tự động gia hạn mở cửa sổ hạn mức mới; xóa client trên master xóa hoàn toàn client đó trên các nút; các inbound của nút không bị quét sạch trước lần chấp nhận đầu tiên; một inbound không hợp lệ không dừng việc đồng bộ lưu lượng của nút; kiểm tra xung đột cổng được giới hạn trong nút của chính nó.

### Thay đổi ở phần 14 — Telegram Bot

- Menu lệnh của bot được bổ sung **`/usage`**, **`/inbound`**, **`/restart`** và lệnh quản trị mới **`/clearall`** (đặt lại lưu lượng của tất cả client, có xác nhận).
- Danh sách client trực tuyến được ghi nhãn dạng `email - remark inbound`; các tin nhắn sao lưu và nhật ký chặn chứa tên host; tìm kiếm theo Telegram ID hoạt động bất kể định dạng của cài đặt.

### Thay đổi ở phần 16 — Vận hành: sao lưu, nhật ký, cập nhật, CLI

- **Khôi phục trên panel PostgreSQL chấp nhận tệp SQLite**: bản sao lưu `.db` thông thường hoặc `.dump` di chuyển được nhập thẳng vào PostgreSQL (trong một giao dịch duy nhất, với các kiểm tra trước khi dừng Xray). Hộp thoại chọn tệp chấp nhận `.dump,.db` trên cả hai DBMS; «Tải xuống tệp di chuyển» chỉ còn trên các panel PostgreSQL.
- Trước khi khôi phục tệp lưu trữ `pg_dump`, bảng điều khiển kiểm tra khả năng đọc của dump và khi phiên bản không khớp sẽ gợi ý lệnh chính xác `x-ui pgclient <phiên bản>`.
- Tự động sửa chữa khi khởi động: các bộ đếm lưu lượng bị tràn được kẹp lại và khôi phục; gỡ bỏ ràng buộc UNIQUE lỗi thời trên cổng inbound (từng cản trở multi-node).
- Nhật ký Xray: tác vụ mới mỗi 10 phút cắt bớt access-log và error-log khi vượt quá **64 MiB**; việc dọn dẹp hàng ngày nay làm sạch cả hai.
- Docker: tự động gia hạn chứng chỉ đã được sửa (crond được khởi chạy, trạng thái acme.sh được lưu trong volume).

---

Được tạo từ việc phân tích các tệp nguồn của bảng điều khiển. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

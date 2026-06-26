# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 Tiếng Việt · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Hướng dẫn sử dụng cho bảng điều khiển [3x-ui](https://github.com/MHSanaei/3x-ui) — tài liệu hướng dẫn toàn diện được viết cho bảng điều khiển phiên bản **v3.4.1**.

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

## Có gì mới trong 3.4.1

Mục này liệt kê ngắn gọn các thay đổi của phiên bản **3.4.1** so với 3.4.0 mà người dùng bảng điều khiển có thể thấy, được nhóm theo các mục của hướng dẫn. Chi tiết về từng tính năng — trong mục tương ứng bên dưới.

### Thay đổi ở phần 1 — Giới thiệu, yêu cầu và cài đặt
- **Cài đặt bản dev và cài đặt phiên bản cụ thể qua install.sh** — Script cài đặt install.sh nay hỗ trợ đối số để chọn phiên bản: chỉ định tag (ví dụ v3.4.0) để cài phiên bản cụ thể, hoặc 'dev-latest' (bí danh 'dev') để cài bản rolling dev theo commit mới nhất của nhánh main, bỏ qua kiểm tra phiên bản tối thiểu. Không có đối số thì cài bản ổn định mới nhất.

### Thay đổi ở phần 3 — Tổng quan / Bảng điều khiển chính
- **Bảng điều khiển chính: cải tiến lựa chọn khoảng thời gian trong biểu đồ lịch sử hệ thống và số liệu Xray** — Trong các cửa sổ lịch sử trên bảng điều khiển chính, lựa chọn khoảng thời gian đã được cập nhật. Đối với biểu đồ số liệu hệ thống, các khoảng 2m, 1h, 3h, 6h, 12h, 24h, 2d và 7d có sẵn (lịch sử nay lưu đến 7 ngày thay vì 48 giờ trước đây), và trên khoảng 2 và 7 ngày, nhãn thời gian được bổ sung thêm ngày tháng. Đối với biểu đồ số liệu Xray, các khoảng 2m, 1h, 3h, 6h và 12h có sẵn. Các giá trị không đều 30m, 2h và 5h đã bị xóa.
- **Bảng điều khiển chính: thẻ sử dụng bộ nhớ hiển thị RSS thực của tiến trình** — Chỉ số sử dụng RAM của bảng điều khiển trên trang tổng quan nay phản ánh RSS thực của tiến trình và khớp với giá trị mà hệ điều hành hiển thị. Trước đây hiển thị bộ đếm nội bộ Go, thường phóng đại mức sử dụng bộ nhớ và không bao giờ giảm. Nay con số giảm khi bộ nhớ được giải phóng.

### Thay đổi ở phần 5 — Giao thức
- **VLESS encryption: các chế độ tạo khóa mới (native / xorpub / random)** — Trong inbound với giao thức VLESS, khối tạo khóa mã hóa nay có cấu trúc khác. Thay vì hai nút riêng biệt (X25519 và ML-KEM-768) dưới các trường «Giải mã» và «Mã hóa», xuất hiện danh sách thả xuống «Tạo khóa» với sáu lựa chọn: X25519 và ML-KEM-768, mỗi loại trong ba chế độ — native, xorpub và random. Chọn chế độ cần thiết và nhấn «Tạo»: bảng điều khiển sẽ điền các trường decryption và encryption bằng cặp khóa đã tạo. Nút «Xóa» loại bỏ các giá trị đã tạo, và dòng «Đã chọn» hiển thị loại và chế độ khóa hiện tại.
- **Xóa trường Rewrite port trong cài đặt tunnel-inbound không còn làm hỏng việc lưu** — Đã sửa lỗi: trong inbound với giao thức tunnel, việc xóa trường «Cổng ghi đè» (Rewrite port) không còn gây lỗi khi lưu. Trước đây giá trị rỗng gây thông báo lỗi xác thực; nay trường này đơn giản bị loại khỏi cài đặt khi trống.

### Thay đổi ở phần 7 — Bảo mật kết nối: TLS, XTLS và REALITY
- **Khôi phục flow XTLS Vision khi bật mã hóa trên inbound hiện có** — Nếu bật mã hóa (decryption/encryption) trên inbound VLESS/XHTTP hiện có sau khi đã thêm khách hàng, bảng điều khiển nay tự động khôi phục flow=xtls-rprx-vision cho những khách hàng cần có nó. Trước đây flow trong trường hợp này âm thầm biến mất khỏi cấu hình, liên kết và đăng ký (đặc biệt trên inbound của node). Không cần thao tác thủ công — sửa được áp dụng tự động khi chỉnh sửa inbound và một lần khi cập nhật bảng điều khiển.

### Thay đổi ở phần 8 — Khách hàng
- **Bật và tắt hàng loạt các khách hàng đã chọn** — Khi chọn nhiều khách hàng trên trang Clients, trong menu More (Thêm) có sẵn các thao tác hàng loạt Enable (Bật) và Disable (Tắt). Bật sẽ kích hoạt từng khách hàng đã chọn trên tất cả inbounds được liên kết; khách hàng đã hết hạn mức lưu lượng hoặc thời hạn sẽ tự động bị tắt trở lại. Tắt sẽ lập tức thu hồi quyền truy cập của khách hàng, nhưng bản ghi và lưu lượng tích lũy của họ được giữ lại. Trước khi thực hiện, bảng điều khiển yêu cầu xác nhận, và sau thao tác hiển thị thông báo với số lượng khách hàng đã xử lý và, nếu có, số lượng thao tác thất bại.
- **Đặt XTLS flow hàng loạt trong hộp thoại Adjust** — Trong hộp thoại điều chỉnh hàng loạt Adjust xuất hiện trường Set flow để đặt hoặc xóa XTLS flow cho tất cả khách hàng đã chọn cùng lúc. Mặc định chọn No change (không thay đổi). Tùy chọn Disable (clear flow) xóa flow, còn các giá trị xtls-rprx-vision và xtls-rprx-vision-udp443 đặt vision-flow tương ứng. Đặt vision-flow chỉ áp dụng cho inbounds hỗ trợ flow; các inbounds không phù hợp được giữ nguyên và đánh dấu là đã bỏ qua, trong khi xóa flow luôn được phép. Nay để áp dụng hộp thoại, chỉ cần đặt ngày, lưu lượng hoặc flow.
- **Đổi tên khách hàng không còn làm hỏng liên kết và đã xóa toast lưu trùng lặp** — Đã sửa hành vi khi chỉnh sửa khách hàng: đổi tên khách hàng (thay đổi email của họ) không còn gây lỗi khi lưu liên kết inbounds và các liên kết bên ngoài — các thao tác này nay sử dụng email mới. Ngoài ra, khi lưu khách hàng, thông báo cập nhật thành công không còn xuất hiện nhiều lần.

### Thay đổi ở phần 10 — Đăng ký (Subscription)
- **Nhóm biến Remark Template «Connection» mới: {{PROTOCOL}}, {{TRANSPORT}}, {{SECURITY}}** — Vào tập biến mẫu nhận xét (Remark Template) đã thêm nhóm «Kết nối» (Connection) với ba biến mô tả cấu hình inbound: {{PROTOCOL}} — giao thức (VLESS, VMess, Trojan, v.v.), {{TRANSPORT}} — mạng truyền tải (tcp, ws, grpc, v.v.) và {{SECURITY}} — bảo mật truyền tải (TLS, REALITY, NONE; hiển thị bằng chữ hoa). Giống như các biến mức sử dụng và thời hạn, ba biến này chỉ hoạt động trong nội dung đăng ký và tự động bị loại khỏi nhận xét trên các liên kết hiển thị trong bảng điều khiển và trên trang thông tin đăng ký.
- **Mẫu nhận xét mặc định nay bao gồm {{EMAIL}}; email khách hàng đã trở lại trong nhận xét liên kết bảng điều khiển** — Mẫu nhận xét mặc định đã thay đổi: nay bao gồm email khách hàng — {{INBOUND}}-{{EMAIL}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D (trước đây không có email). Ngoài ra, đã sửa hành vi của phiên bản 3.4.0: trên các liên kết hiển thị trong bảng điều khiển (QR-code và các cửa sổ «Thông tin» trên trang «Khách hàng») và trên trang thông tin đăng ký, email khách hàng lại xuất hiện trong tên hồ sơ — «inbound-host-email» khi có host hoặc «inbound-email» không có host. Thông tin lưu lượng và thời hạn không được chèn vào các tên hiển thị này.
- **Tích hợp ứng dụng Incy: nút nhập nhanh và tab Incy với định tuyến** — Trên trang thông tin đăng ký trong menu ứng dụng (Android và iOS) xuất hiện mục «Incy» — mở deep-link incy://add/<liên-kết-đăng-ký> để nhập nhanh đăng ký vào ứng dụng. Trong cài đặt đăng ký đã thêm tab «Incy» với công tắc «Bật định tuyến» (Enable routing) và trường «Quy tắc định tuyến» (Routing rules) theo định dạng incy://routing/onadd/<base64>. Khi định tuyến được bật và trường đã điền, chuỗi này được thêm vào một dòng riêng trong nội dung đăng ký (định dạng raw), cung cấp hồ sơ định tuyến cho ứng dụng Incy. Cài đặt chỉ áp dụng cho ứng dụng Incy.
- **Khôi phục {{TRAFFIC_USED}} cho khách hàng có dòng lưu lượng mồ côi** — Đã sửa việc tính toán biến {{TRAFFIC_USED}} (và các chỉ số sử dụng khác) trong nhận xét cho khách hàng có dòng thống kê lưu lượng «mồ côi» sau khi xóa và tạo lại inbound. Trước đây ở những khách hàng đó {{TRAFFIC_USED}} hiển thị 0.00B, mặc dù tiêu đề trang thông tin đăng ký hiển thị mức sử dụng đúng. Nay bảng điều khiển cũng tìm thống kê theo email khách hàng, và biến lại hiển thị lưu lượng đã sử dụng chính xác.
- **Tiêu đề tab chính xác trên trang Hosts** — Trên trang Hosts nay hiển thị đúng tiêu đề tab trình duyệt thay vì '3X-UI' chung. Thay đổi chỉ thuần mỹ quan và chỉ ảnh hưởng đến nhãn tab.

### Thay đổi ở phần 11 — Xray: định tuyến, outbounds, DNS và tiện ích mở rộng
- **Danh sách thả xuống Dialer Proxy nay liệt kê outbounds từ đăng ký** — Trong phần Sockopt của biểu mẫu outbound, danh sách thả xuống «Dialer Proxy» (chuỗi proxy: chuyển outbound này qua outbound khác theo tag) nay hiển thị không chỉ outbounds cục bộ mà còn cả tag của outbounds từ đăng ký. Blackhole-outbound và chính outbound đang chỉnh sửa vẫn bị loại khỏi danh sách. Để trống trường để kết nối trực tiếp.
- **HTTP outbound: custom request headers được giữ lại (và có thể chỉnh sửa)** — Trong biểu mẫu outbound với giao thức HTTP đã thêm trường «Headers» (Tiêu đề) — trình chỉnh sửa cặp khóa/giá trị cho các CONNECT-tiêu đề gửi đến HTTP-proxy thượng nguồn. Trước đây các tiêu đề này bị mất khi lưu lại outbound; nay chúng được giữ lại. Lưu ý: chỉ các tiêu đề ở cấp cài đặt mới được áp dụng, xray-core bỏ qua các tiêu đề ở cấp máy chủ riêng lẻ.

### Thay đổi ở phần 12 — Node (đa bảng điều khiển, master/slave)
- **Kênh Dev khi cập nhật node** — Trong hộp thoại xác nhận cập nhật node xuất hiện hộp kiểm 'Cập nhật lên kênh phát triển (commit mới nhất)'. Nếu đánh dấu, các node đã chọn sẽ cài bản rolling dev-latest thay vì bản ổn định; khi bỏ đánh dấu, node cập nhật theo kênh thông thường của mình. Dưới hộp kiểm có cảnh báo rằng bản dev không ổn định.
- **Nhập lịch sử lưu lượng khách hàng khi đồng bộ inbound từ node lần đầu** — Đã sửa việc tính toán lưu lượng khi thêm node đã có lưu lượng tích lũy. Trước đây khi đồng bộ inbound từ node lần đầu, bộ đếm tổng của inbound được chuyển đúng, còn bộ đếm riêng lẻ của khách hàng bị xóa về 0, và master đánh giá thấp mức sử dụng của khách hàng cho toàn bộ lịch sử trước khi kết nối node. Nay khi nhập inbound cùng với node, bộ đếm khách hàng kế thừa giá trị thực từ node.

### Thay đổi ở phần 14 — Telegram-bot
- **Khởi động lại Telegram-bot khi lưu cài đặt** — Các thay đổi cài đặt Telegram-bot nay được áp dụng ngay khi lưu, không cần khởi động lại bảng điều khiển. Nếu bạn thay đổi token, chat ID, địa chỉ API-server hoặc bật/tắt bot, bảng điều khiển tự động khởi động lại bot với các tham số mới. Quy tắc cũ về việc phải khởi động lại bảng điều khiển sau khi thay đổi token không còn hiệu lực.
- **Tên tệp sao lưu từ Telegram-bot — theo webDomain/IP** — Các tệp sao lưu cơ sở dữ liệu do Telegram-bot gửi nay được đặt tên theo địa chỉ máy chủ: theo webDomain, và nếu không được đặt — theo IP công cộng. Trước đây khi webDomain không được đặt, những bản sao lưu đó nhận tên chung x-ui, khó nhận biết tệp đến từ máy chủ nào.

### Thay đổi ở phần 16 — Vận hành: sao lưu, log, cập nhật, CLI
- **Màn hình theo dõi sức khỏe tunnel (tự động khởi động lại xray theo biến môi trường)** — Trong 3.4.1 xuất hiện màn hình theo dõi sức khỏe tunnel tùy chọn. Nếu được bật, bảng điều khiển định kỳ kiểm tra tính khả dụng của URL đã chỉ định và, sau một số lần kiểm tra thất bại liên tiếp, tự động khởi động lại lõi xray — điều này giúp khôi phục tunnel đã ngừng truyền tải lưu lượng. Màn hình chỉ được cấu hình thông qua các biến môi trường của dịch vụ (không có cài đặt trong giao diện web) và mặc định bị tắt. Biến chính XUI_TUNNEL_HEALTH_MONITOR=true bật nó; XUI_TUNNEL_HEALTH_PROXY nên trỏ đến inbound xray cục bộ (ví dụ socks5://127.0.0.1:1080), nếu không chỉ kiểm tra kết nối của chính máy chủ, chứ không phải tunnel. Các biến khác đặt URL kiểm tra (XUI_TUNNEL_HEALTH_URL), khoảng thời gian (XUI_TUNNEL_HEALTH_INTERVAL, 30s), timeout (XUI_TUNNEL_HEALTH_TIMEOUT, 10s), số lần thất bại trước khi khởi động lại (XUI_TUNNEL_HEALTH_FAILURES, 3) và khoảng dừng tối thiểu giữa các lần khởi động lại (XUI_TUNNEL_HEALTH_COOLDOWN, 5m). Lưu ý: việc khởi động lại xray sẽ ngắt kết nối của tất cả khách hàng đang kết nối.
- **Tự động cập nhật trong trình xem log** — Trong các cửa sổ xem log (cả 'Log truy cập' Xray và 'Log' chung của bảng điều khiển) xuất hiện hộp kiểm 'Tự động cập nhật'. Nếu bật, log tự động được đọc lại mỗi 5 giây với việc giữ nguyên số dòng, cấp độ và bộ lọc đã chọn. Việc truy vấn dừng lại ngay khi cửa sổ đóng hoặc hộp kiểm bị bỏ chọn.
- **Kênh cập nhật Dev cho bảng điều khiển (bản rolling theo commit)** — Công tắc chỉ hiển thị trong cửa sổ cập nhật bảng điều khiển trên bản dev (bản CI theo từng commit riêng lẻ). Khi bật, bảng điều khiển sẽ cập nhật lên bản rolling dev-latest theo dõi mỗi commit của nhánh main và không phải bản ổn định; không có tự động quay lại. Ở chế độ dev, cửa sổ hiển thị commit hiện tại và mới nhất thay vì số phiên bản. Tính năng chỉ có sẵn trên Linux với systemd.
- **Cập nhật lên kênh Dev trong menu x-ui và lệnh x-ui update-dev** — Trong menu quản lý script x-ui đã thêm mục cập nhật lên kênh phát triển ('Update to Dev Channel (latest commit)'), cài bản rolling dev-latest sau khi xác nhận, cũng như lệnh 'x-ui update-dev'. Do đó các mục menu đã được đánh số lại: tổng cộng có 28 mục, nhập lựa chọn — trong khoảng 0-28. Nếu hướng dẫn có đánh số các mục menu, cần đối chiếu lại.
- **Xóa PostgreSQL khi gỡ cài đặt bảng điều khiển** — Khi xóa bảng điều khiển, nếu nó sử dụng PostgreSQL, script nay hỏi thêm xem có cần xóa cả máy chủ PostgreSQL cùng với tất cả cơ sở dữ liệu của nó hay không. Yêu cầu xác nhận rõ ràng (mặc định — từ chối) và đi kèm cảnh báo: việc xóa sẽ ảnh hưởng đến TẤT CẢ cơ sở dữ liệu PostgreSQL trên máy, kể cả của các ứng dụng khác, và không thể hoàn tác. Khi từ chối, PostgreSQL và dữ liệu của nó được giữ lại.
- **Trình xem log truy cập Xray được đổi tên thành 'Log truy cập'** — Trình xem access-log Xray và nút gọi nó trên thẻ trạng thái Xray nay có tên 'Log truy cập' (trước đây — đơn giản là 'Log'). Điều này được thực hiện để không nhầm lẫn với trình xem log chung của bảng điều khiển.
- **Chọn số dòng log: đã thêm 1000, bỏ 10** — Trong cả hai cửa sổ log, danh sách chọn số dòng đã thay đổi: giá trị 10 bị xóa, thêm 1000. Nay có thể chọn 20, 50, 100, 500 hoặc 1000 dòng.
- **Định danh bản dev (dev+<commit>) trong giao diện, bot và CLI** — Trên bản dev, bảng điều khiển hiển thị phiên bản của mình dưới dạng 'dev+<commit>' thay vì số phiên bản ổn định — trong badge thanh bên, trên bảng điều khiển chính, trong cửa sổ cập nhật, trong báo cáo Telegram-bot và trong đầu ra 'x-ui -v'. Trên các bản ổn định, dạng hiển thị phiên bản không thay đổi.
- **Trình xem log: các thông báo đơn giản hiển thị nguyên vẹn, không bị biến dạng theo định dạng ngày** — Trình xem log bảng điều khiển nay hiển thị đúng các thông báo đơn giản không có dấu thời gian và cấp độ (ví dụ thông báo hệ thống 'Syslog is not supported') — toàn bộ, không cắt bớt văn bản. Trước đây những dòng như vậy bị phân tích sai như bản ghi log có ngày và cấp độ, và một phần văn bản bị mất.

---

Được tạo từ việc phân tích các tệp nguồn của bảng điều khiển. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 简体中文 · 🇹🇼 [繁體中文](README.zh-TW.md)

用于 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板的用户手册 — 一份为面板 **v3.4.1** 编写的综合使用指南。

> **只读镜像。** 此 GitHub 仓库为单向镜像 — 手册源文件存放于私有 GitLab，并自动推送至此，因此始终保持最新。发现错误或不准确之处？请[提交 Issue](https://github.com/yukh975/3X-UI-Manual/issues)。**不接受 Pull Request**（将自动关闭） — 修改须在源端进行。

## 目录

| 文件 | 语言 | 格式 |
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

## 3.4.1 新特性

本节简要列出 **3.4.1** 相较于 3.4.0 对面板用户可见的变更，按手册章节分组。每项功能的详细说明请参见对应章节。

### 第 1 节的更改 — 简介、系统要求与安装
- **通过 install.sh 安装 dev 版本或指定版本** — 安装脚本 install.sh 现已支持版本选择参数：指定标签（如 v3.4.0）可安装特定版本，或使用 'dev-latest'（别名 'dev'）安装跟随 main 分支最新提交的 rolling dev 版本（跳过最低版本检查）。不带参数时默认安装最新稳定版。

### 第 3 节的更改 — 概览 / 仪表盘
- **仪表盘：系统历史图表与 Xray 指标图表的时间范围选择已重新设计** — 仪表盘历史窗口中的时间范围选择已更新。系统指标图表可选范围为 2m、1h、3h、6h、12h、24h、2d 和 7d（历史数据现最多保存 7 天，原为 48 小时），其中 2 天和 7 天范围的时间标签会附加日期。Xray 指标图表可选范围为 2m、1h、3h、6h 和 12h。不规则的 30m、2h 和 5h 已移除。
- **仪表盘：内存使用卡片显示进程真实 RSS** — 仪表盘中面板的内存使用量现在反映进程的实际 RSS，与操作系统显示的数值一致。此前显示的是 Go 内部计数器，会高估内存使用量且从不减少。现在内存释放后数值会相应降低。

### 第 5 节的更改 — 协议
- **VLESS 加密：新的密钥生成模式（native / xorpub / random）** — 在使用 VLESS 协议的 inbound 中，加密密钥生成模块已重新设计。原来在「解密」和「加密」字段下方各有两个独立按钮（X25519 和 ML-KEM-768），现改为「密钥生成」下拉列表，包含六个选项：X25519 和 ML-KEM-768，各有三种模式——native、xorpub 和 random。选择所需模式后点击「生成」，面板将自动填写 decryption 和 encryption 字段的密钥对。「清除」按钮用于删除已生成的值，「已选」行显示当前密钥类型和模式。
- **清空 tunnel inbound 设置中的 Rewrite port 字段不再导致保存失败** — 修复了一个问题：在使用 tunnel 协议的 inbound 中，清空「端口重写」（Rewrite port）字段不再引发保存错误。此前空值会触发验证错误提示；现在清空该字段时，它将被直接从配置中移除。

### 第 7 节的更改 — 连接安全：TLS、XTLS 与 REALITY
- **在现有 inbound 上启用加密后，XTLS Vision flow 自动恢复** — 如果在已添加客户端的 VLESS/XHTTP inbound 上启用加密（decryption/encryption），面板现在会自动为符合条件的客户端恢复 flow=xtls-rprx-vision。此前在这种情况下，flow 会在配置、链接和订阅中静默丢失（在节点 inbound 上尤为明显）。无需任何手动操作——修复会在编辑 inbound 时自动应用，并在面板更新后执行一次补全。

### 第 8 节的更改 — 客户端
- **批量启用与禁用选定客户端** — 在 Clients 页面选中多个客户端后，More（更多）菜单中提供 Enable（启用）和 Disable（禁用）批量操作。启用操作会在所有绑定的 inbound 上激活每个选定客户端；流量配额已耗尽或已过期的客户端将被自动再次禁用。禁用操作会立即撤销客户端访问权限，但其记录和累计流量数据将保留。执行前面板会要求确认，操作完成后会显示已处理客户端数量的通知，如有失败也会一并显示。
- **在 Adjust 对话框中批量设置 XTLS flow** — 批量调整对话框 Adjust 新增了 Set flow 字段，可为所有选定客户端统一设置或清除 XTLS flow。默认选项为 No change（不更改）。Disable（clear flow）用于清除 flow，xtls-rprx-vision 和 xtls-rprx-vision-udp443 则设置对应的 vision-flow。vision-flow 仅应用于支持 flow 的 inbound；不适用的 inbound 保持不变并标记为已跳过，而清除 flow 则始终允许。现在只需设置天数、流量或 flow 之一即可应用对话框。
- **重命名客户端不再破坏绑定关系，并移除了重复的保存提示** — 修复了客户端编辑行为：重命名客户端（修改其 email）不再导致保存 inbound 绑定和外部引用时出错——这些操作现在使用更新后的 email。此外，保存客户端时成功更新的通知不再多次弹出。

### 第 10 节的更改 — 订阅（Subscription）
- **Remark Template 新增「Connection」变量组：{{PROTOCOL}}、{{TRANSPORT}}、{{SECURITY}}** — 备注模板（Remark Template）变量集中新增了「连接」（Connection）组，包含三个描述 inbound 配置的变量：{{PROTOCOL}}——协议（VLESS、VMess、Trojan 等），{{TRANSPORT}}——传输网络（tcp、ws、grpc 等），{{SECURITY}}——传输安全（TLS、REALITY、NONE；以大写形式输出）。与流量和有效期变量一样，这三个变量仅在订阅正文中生效，并会自动从面板上显示的链接以及订阅信息页的备注中移除。
- **默认备注模板现已包含 {{EMAIL}}；客户端 email 重新出现在面板链接备注中** — 默认备注模板已更改：现在包含客户端 email——{{INBOUND}}-{{EMAIL}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D（此前不含 email）。此外，3.4.0 版本中的一个问题已修复：在面板显示的链接（Clients 页面的 QR 码和「信息」窗口）以及订阅信息页上，客户端 email 重新出现在配置文件名中——设置了 host 时为「inbound-host-email」，未设置时为「inbound-email」。流量和有效期信息不会填入这些显示名称。
- **Incy 客户端集成：快速导入按钮及带路由功能的 Incy 标签页** — 订阅信息页的应用菜单（Android 和 iOS）中新增了「Incy」入口——点击可打开 deep-link incy://add/<订阅链接> 以快速将订阅导入 Incy 客户端。订阅设置中新增了「Incy」标签页，包含「启用路由」（Enable routing）开关和「路由规则」（Routing rules）字段，格式为 incy://routing/onadd/<base64>。当路由已启用且字段已填写时，该字符串将作为独立行附加到订阅正文（raw 格式），将路由配置文件传递给 Incy 客户端。这些设置仅对 Incy 客户端生效。
- **为孤立流量记录的客户端恢复 {{TRAFFIC_USED}}** — 修复了因删除并重新创建 inbound 后流量统计行变为「孤立」的客户端在备注中 {{TRAFFIC_USED}}（及其他流量统计变量）的计算问题。此前此类客户端的 {{TRAFFIC_USED}} 显示为 0.00B，但订阅信息页标题中的使用量显示正确。现在面板会额外按客户端 email 查找统计数据，该变量将再次显示正确的已用流量。
- **Hosts 页面标签页标题正确显示** — Hosts 页面的浏览器标签页标题现在能正确显示，而非通用的「3X-UI」。此更改为纯外观改动，仅影响标签页标签文字。

### 第 11 节的更改 — Xray：路由、outbounds、DNS 与扩展
- **Dialer Proxy 下拉列表现在列出订阅 outbounds** — 在 outbound 表单的 Sockopt 部分，「Dialer Proxy」（代理链：通过另一个 outbound 的标签路由本 outbound 流量）下拉列表现在不仅显示本地 outbounds，还显示来自订阅的 outbound 标签。列表中仍然排除 blackhole outbound 和当前编辑的 outbound 本身。留空表示直接连接。
- **HTTP outbound：自定义请求头已保留（且可编辑）** — 使用 HTTP 协议的 outbound 表单中新增了「Headers」（请求头）字段——用于编辑发送给上游 HTTP 代理的 CONNECT 请求头的键值对。此前这些请求头在重新保存 outbound 时会丢失；现在它们将被保留。注意：仅应用设置层级的请求头，xray-core 会忽略单个服务器层级的请求头。

### 第 12 节的更改 — 节点（多面板，master/slave）
- **更新节点时的 Dev 渠道选项** — 节点更新确认对话框中新增了「更新至开发渠道（最新提交）」复选框。勾选后，选定节点将安装 rolling 版本 dev-latest 而非稳定版；不勾选时节点按其常规渠道更新。复选框下方显示 dev 版本不稳定的警告。
- **首次同步 inbound 时导入客户端历史流量数据** — 修复了在已累积流量的节点上添加节点时的流量计算问题。此前首次从节点同步 inbound 时，inbound 的总计数器能正确迁移，但客户端的单独计数器会被清零，导致主面板少算连接节点之前的所有历史流量。现在随节点导入 inbound 时，客户端计数器会继承节点上的真实值。

### 第 14 节的更改 — Telegram 机器人
- **保存设置时重新加载 Telegram 机器人** — Telegram 机器人的设置更改现在在保存时立即生效，无需重启面板。如果更改了 token、chat ID、API 服务器地址，或启用/禁用了机器人，面板将自动以新参数重启机器人。此前关于更换 token 后需重启面板的规则不再适用。
- **Telegram 机器人备份文件名改为 webDomain/IP** — Telegram 机器人发送的数据库备份文件现以服务器地址命名：使用 webDomain，若未设置则使用公网 IP。此前未设置 webDomain 时，备份文件名为通用的 x-ui，难以区分来源服务器。

### 第 16 节的更改 — 运维：备份、日志、更新、CLI
- **隧道健康监测器（通过环境变量自动重启 xray）** — 3.4.1 新增了可选的隧道健康监测器。启用后，面板会定期检测指定 URL 的可达性，若连续多次检测失败，则自动重启 xray 核心——有助于恢复停止转发流量的隧道。监测器仅通过服务环境变量配置（网页界面中无相关设置），默认关闭。关键变量 XUI_TUNNEL_HEALTH_MONITOR=true 用于启用；XUI_TUNNEL_HEALTH_PROXY 应指向本地 xray inbound（例如 socks5://127.0.0.1:1080），否则仅检测服务器本身的网络连通性而非隧道。其他变量设置检测 URL（XUI_TUNNEL_HEALTH_URL）、检测间隔（XUI_TUNNEL_HEALTH_INTERVAL，30s）、超时（XUI_TUNNEL_HEALTH_TIMEOUT，10s）、触发重启前的连续失败次数（XUI_TUNNEL_HEALTH_FAILURES，3）以及两次重启之间的最短间隔（XUI_TUNNEL_HEALTH_COOLDOWN，5m）。注意：重启 xray 会断开所有已连接客户端的连接。
- **日志查看器中的自动刷新** — 日志查看窗口（Xray 「访问日志」和面板「日志」）中新增了「自动刷新」复选框。启用后，日志每 5 秒自动重新读取一次，同时保留已选的行数、级别和过滤器设置。关闭窗口或取消勾选后轮询停止。
- **面板的 Dev 更新渠道（按提交的 rolling 版本）** — 该开关仅在 dev 版本（按单个提交构建的 CI 版本）的面板更新窗口中显示。启用后，面板将更新至 rolling 版本 dev-latest，该版本跟随 main 分支的每次提交，不是稳定版；不提供自动回滚。Dev 模式下更新窗口显示当前提交和最新提交而非版本号。此功能仅在带有 systemd 的 Linux 上可用。
- **x-ui 菜单中的 Dev 渠道更新选项及 x-ui update-dev 命令** — x-ui 管理脚本菜单中新增了更新至开发渠道的条目（「Update to Dev Channel (latest commit)」），确认后安装 rolling 版本 dev-latest，同时新增命令 'x-ui update-dev'。因此菜单条目已重新编号：共 28 个条目，选择输入范围为 0-28。如果手册中引用了菜单条目编号，需重新核对。
- **卸载面板时可选删除 PostgreSQL** — 卸载面板时，如果面板使用了 PostgreSQL，脚本现在会额外询问是否同时删除 PostgreSQL 服务器及其所有数据库。此操作需要明确确认（默认为否），并附有警告：删除将影响该机器上的所有 PostgreSQL 数据库，包括其他应用的数据库，且不可逆。选择否时 PostgreSQL 及其数据将保留。
- **Xray 访问日志查看器重命名为「访问日志」** — Xray access 日志查看器及 Xray 状态卡片上的调用按钮现更名为「访问日志」（原名为「日志」）。此更改旨在与面板通用日志查看器加以区分。
- **日志行数选择：新增 1000，移除 10** — 两个日志窗口中的行数选择列表已更新：移除了 10，新增了 1000。现可选择 20、50、100、500 或 1000 行。
- **dev 版本标识符（dev+<提交哈希>）在界面、机器人和 CLI 中显示** — 在 dev 版本上，面板以「dev+<提交哈希>」的形式显示版本号，而非稳定版本号——体现在侧边栏标识、仪表盘、更新窗口、Telegram 机器人报告及 'x-ui -v' 输出中。稳定版的版本显示方式不变。
- **日志查看器：纯通知消息原样显示，不再错误套用日期格式** — 面板日志查看器现在能正确显示不带时间戳和级别的纯通知消息（例如系统消息「Syslog is not supported」）——完整显示，不再截断。此前此类行被错误地解析为带日期和级别的日志条目，导致部分文本丢失。

---

根据面板源文件分析整理。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

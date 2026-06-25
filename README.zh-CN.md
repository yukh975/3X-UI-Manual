# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 简体中文 · 🇹🇼 [繁體中文](README.zh-TW.md)

用于 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板的用户手册 — 一份为面板 **v3.4.0** 编写的综合使用指南。

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

## 3.4.0 新增内容

本节简要列出 **3.4.0** 版本相对于 3.3.1 的、对面板用户可见的变更，按手册章节分组。各项功能的详细说明见下文相应章节。

### 3. 概览 / 仪表盘
- **系统指标历史：新增聚合区间 12h/24h/48h** — 在系统指标历史窗口中，平均区间新增了 12h、24h 和 48h 三个值——现在图表（CPU、RAM、流量、数据包、连接、磁盘、在线、负载）可以查看长达两天的周期。

### 4. Inbounds：创建与通用参数
- **Inbound：与 Xray API 保留端口冲突的警告** — 在创建或修改 inbound 时，面板现在不允许占用内部 Xray API 的保留端口（默认在 127.0.0.1 上为 62789）：loopback 上该端口的本地 TCP-inbound 会被以端口冲突错误拒绝。在节点（nodes）上此限制不生效——它们有自己的 Xray。
- **Tunnel/TProxy：接受不含 security 键的 streamSettings** — tunnel/TProxy 类型的 inbound，其 streamSettings 不含 security 块时，现在可以正常打开并保存，不再报校验错误。
- **Inbounds：列表中新增 Speed 列（实时速度）** — inbounds 列表中出现了 Speed 列，显示每个 inbound 当前的流量速度（上行/下行）。

### 5. 协议
- **Shadowsocks-2022：切换为不同密钥长度的方法时重新生成客户端 PSK** — 对于 Shadowsocks-2022：当加密方法切换为密钥长度不同的方法时（例如在 aes-256 和 aes-128 之间），保存 inbound 时客户端 PSK 现在会自动按新长度重新生成。后果：受影响的客户端需要重新获取订阅（旧链接将失效）。
- **WireGuard：移除了 workers 字段** — 从 WireGuard 表单（inbound 和 outbound）中移除了 workers 字段：xray-core v26.6.22 不再使用它。先前已保存的配置照常工作——该字段只是被忽略。
- **VLESS+XHTTP：链接和订阅中的 xtls-rprx-vision 流控** — 对于 XHTTP 之上的 VLESS，xtls-rprx-vision 流控现在能正确进入链接和订阅（包括 XHTTP+REALITY 以及 Clash/Mihomo 格式）。此前面板会保存 flow，但客户端拿到的配置不含 vision。

### 6. 传输（Stream Settings）
- **XHTTP：sessionID 字段重命名 + Session ID Table / Length** — 在 XHTTP 传输中，会话字段被重命名：Session ID Placement 和 Session ID Key（此前为 Session Placement / Session Key）。新增了两个参数。Session ID Table——用于生成会话标识符的字符集：可以选择预定义集合（ALPHABET、Base62、hex、number 等）或输入任意 ASCII 字符串；留空——使用 xray-core 的默认值。Session ID Length——生成标识符的长度或范围（例如 8-16）；仅在设置了 Session ID Table 时生效，最小值必须大于 0。旧的已保存 inbound 会自动迁移。
- **Inbound：用于识别 CDN/中继后真实 IP 的 Real client IP 预设** — 在 inbound 的套接字设置（sockopt）中出现了 Real client IP 选项——一个用于在流量经由 CDN 或中继到达时识别访客真实 IP 的预设（否则记录的是中间方的地址）。提供三种选项：Off / direct（不处理）、Cloudflare CDN（信任 X-Forwarded-For）和 L4 relay / Spectrum (PROXY)（接受 PROXY 协议头）。各预设互斥，并会在所选传输不支持时给出警告。这些字段从不在订阅中发送给客户端。
- **gRPC：现在会处理 Trusted X-Forwarded-For 头** — Trusted X-Forwarded-For 头现在在 gRPC 传输上也会被处理（此前——仅 WebSocket、HTTPUpgrade 和 XHTTP）。对于 gRPC-inbound，面板不再显示该头不受支持的警告。

### 7. 连接安全：TLS、XTLS 与 REALITY
- **TLS：新增字段 Verify Peer Cert By Name、Curve Preferences、Master Key Log、ECH Sockopt** — Verify Peer Cert By Name——客户端用以校验服务器证书的名称（逗号分隔），代替 SNI；是已移除的 allowInsecure 的现代替代，会在链接和订阅中传递，不写入服务器。Curve Preferences——TLS 密钥交换曲线的限制及顺序（例如 X25519MLKEM768、X25519）；留空——使用默认值。Master Key Log——用于记录 TLS 密钥的路径（SSLKEYLOGFILE 格式），供 Wireshark 调试；生产环境应留空。ECH Sockopt——用于获取 ECH 配置的套接字参数（dialerProxy、Domain Strategy、TCP Fast Open、Multipath TCP）。
- **REALITY：fallback 限速（Limit Fallback）和 Master Key Log** — 对每个方向（Upload 和 Download）设置：After Bytes——在开始限速前以全速放行多少字节（0——从第一个字节起就限速）；Bytes Per Sec——fallback 流量的速度上限，以防探针把服务器当作免费通道使用（0——不限速，禁用该方向）；Burst Bytes Per Sec——短时突发的余量。同时新增了 Master Key Log 字段（用于调试的 SSLKEYLOGFILE 文件路径）。
- **TLS：从 inbound 证书和按 SNI 填充 Pinned Peer Cert SHA-256 的按钮** — 在 Pinned Peer Cert SHA-256 字段旁边，现在有两个自动填充按钮，取代了原先的随机哈希按钮。第一个填入 inbound 自身证书的 SHA-256。第二个通过按指定 SNI 建立 TLS 连接获取服务器实时证书的哈希（serverName 必须填写）。获取到的哈希会添加到字段中（逗号分隔），并进入链接，供客户端固定证书。
- **TLS：新建 inbound 证书默认关闭 OCSP-stapling** — 对于新的 inbound，OCSP stapling 默认关闭（间隔 0）。这消除了对没有 OCSP 响应方的证书（例如 Let's Encrypt）在 xray 日志中产生的错误。该字段仍保留——可为支持 stapling 的证书将其开启。
- **REALITY：与 dest 字段兼容（target 的别名）** — 如果 REALITY-inbound 是用 dest 字段创建的（由旧版本面板、通过 API 或外部工具），现在能正确加载：dest 的值会填入 Target 字段。此前 Target 会为空，重新保存会破坏 REALITY。

### 8. 客户端
- **客户端编辑器中的「Links」选项卡（外部链接与订阅）** — 在其中用 **Add External Link** 按钮添加第三方分享链接（`vless://`、`vmess://`、`trojan://`、`ss://`、`hysteria2://`、`wireguard://`），用 **Add External Subscription** 按钮添加远程订阅的 URL。上述所有内容都会混入该客户端的订阅输出（raw、JSON 和 Clash 格式）：链接按原样添加，而远程订阅由面板定期下载并将其配置与自身配置合并。
- **「IP 限制」字段现在在没有 Fail2ban 时会被禁用** — **IP 限制** 字段现在只有在已安装并启用 Fail2ban 时才生效。如果未安装 Fail2ban（或系统是 Windows，或该功能在服务器上被关闭），客户端编辑器的此字段会被禁用，悬停时显示提示，建议从 `x-ui` 的 bash 菜单安装 Fail2ban。面板更新时，对于没有 Fail2ban 的服务器上的客户端，已保存的 IP 限制会被清零，因为它在那里本就不生效。
- **删除未绑定的客户端、导出与导入客户端** — 在 **客户端** 页面的 **更多** 菜单中新增了三项操作。**导出客户端** 显示所有客户端的 JSON 列表（格式为 `{client, inboundIds}`），并带有复制和下载（`clients-export.json`）按钮。**导入客户端** 接受同样的 JSON：带绑定的客户端会被重建并绑定到 inbound，无绑定的客户端恢复为独立记录，而已存在的 email 不会被覆盖（它们会被标记为已跳过）。**删除未绑定的客户端** 会删除所有未绑定到任何 inbound 的客户端，连同其流量、IP 日志和外部链接；此操作不可逆。
- **客户端 IP 日志：连接时间与节点名** — 在客户端 IP 日志中（位于「IP 限制」字段旁的查看按钮以及「客户端信息」卡片中），每条记录现在除了 IP 本身外，还包含最后一次访问的时间以及记录该连接所经由的节点标签（`@ 节点名`）——在多面板配置中可以看到客户端是经由哪个节点连接的。
- **在单个客户端编辑器中清除组标签** — 现在如果在单个客户端的编辑器中清空 **组** 字段并保存，组标签会被正确移除——此前客户端可能会继续显示在原组下，直到再次保存。
- **客户端列表自动刷新（后台轮询）** — 客户端列表现在会自动刷新：面板每隔几秒拉取一次最新页面，因此新连接的客户端和变化的排序顺序无需手动刷新即可出现。

### 10. 订阅（Subscription）
- **托管 Hosts：按主机覆盖订阅链接** — 在 3.4.0 版本中新增了 Hosts 板块（侧边菜单项）。可为每个 inbound 设置一个或多个 Host 端点，它们会替代 inbound 自身的地址、端口和 TLS 参数填入订阅链接——这便于通过 CDN 或中继分发流量。主机可设置 Remark 和描述、绑定到 inbound、Address（留空——继承 inbound 的地址）和 Port（0——继承 inbound 的端口）、Security 参数（same/tls/none/reality），以及 Host header、Path、Mux、Sockopt、Final Mask、从订阅格式中排除（raw/json/clash）和 Clash/mihomo 参数。主机在 inbound 内可排序，并支持批量操作。
- **Remark Template 取代了 ремарка 模型构造器；变量 {{VAR}}** — 原先的配置名构造器（选择 Inbound/Email/External Proxy 和分隔符）被「Remark Template」字段取代。在其中你可以编写任意的名称格式，通过按钮插入变量：客户端标识（{{EMAIL}}、{{INBOUND}}、{{HOST}}、{{ID}}、{{SUB_ID}}、{{COMMENT}}、{{TELEGRAM_ID}}）、流量（{{TRAFFIC_USED}}、{{TRAFFIC_LEFT}}、{{TRAFFIC_TOTAL}}、{{UP}}、{{DOWN}}、{{USAGE_PERCENTAGE}}）以及期限/状态（{{DAYS_LEFT}}、{{TIME_LEFT}}、{{EXPIRE_DATE}}、{{JALALI_EXPIRE_DATE}}、{{STATUS}}、{{STATUS_EMOJI}}）。生成订阅时变量会为每个客户端单独替换，并提供预览。以「|」符号分隔的、带无限值的片段会被自动隐藏，而用量和期限信息只显示在客户端的第一条链接上。如果该字段留空，则使用原先的 ремарка 模型。
- **Per-client 外部链接与远程订阅（Links 选项卡）** — 在这里可以为单个客户端附加第三方分享链接（Add External Link）和外部订阅地址（Add External Subscription）——它们会被包含进其自身的订阅（RAW、JSON 和 Clash 格式）。外部订阅由面板下载并与客户端的配置合并。这便于在你的 inbound 之上为客户端额外提供一些服务器。
- **Happ：在客户端中隐藏服务器设置（Hide server settings）** — 在订阅设置的 Happ 选项卡中新增了「Hide server settings」开关。开启后，Happ 客户端中查看和修改服务器参数的功能会被隐藏。该选项仅对 Happ 客户端生效。
- **节点名不再追加到订阅中的配置名后** — 节点名（Node）不再添加到订阅中的配置名后。客户端应用中只显示管理员设置的 inbound ремарка，不带形如「@节点名」的内部后缀。
- **ремарка 模型标签重命名 Other → External Proxy（随后被模板取代）** — 无需单独记录：ремарка 模型项「Other」更名为「External Proxy」一事，已被迁移到新的 Remark Template 字段所吸收，那里已从 UI 中移除了模型构造器。
- **订阅链接的正确性：SS2022、Shadowrocket、SIP002 obfs、Clash 中的 XHTTP** — 改进了生成的订阅链接的兼容性：修正了 SS2022 的编码、Shadowrocket 的 deep-link、Shadowsocks+obfs 以 SIP002 格式（obfs-local 插件）的输出，以及 Clash/Mihomo 订阅中完整的 XHTTP 字段集。无需单独设置——链接只是能被客户端更正确地识别。
- **订阅 ремарка 模型：项「Other」更名为「External Proxy」** — 在订阅设置的 ремарка 模型中，**「Other」** 项更名为 **「External Proxy」**（来源——外部代理的 ремарка）。行为未变，现有设置保持兼容。
- **订阅：通过点击芯片选择 ремарка 变量（Remark variable picker）** — 在 Remark Template 字段旁有一组分好类的变量芯片：点击变量 {{VAR}} 会将其插入模板，悬停时显示描述。在 ремарка 和主机名字段中，也允许使用单括号的简化写法——{DATA_LEFT}、{EXPIRE_DATE}、{PROTOCOL}、{TRANSPORT} 等；面板会自动将其转换为内部格式 {{...}}。

### 11. Xray：路由、outbounds、DNS 与扩展
- **路由和 Outbounds 拆分为独立的侧边菜单项** — 从此版本起，**「出站」（Outbounds）** 和 **「路由」（Routing）** 被拆分为独立的侧边菜单项（紧挨在「Hosts」之下），各有自己的地址——`/outbound` 和 `/routing`。此前路由在「Xray 配置」子菜单内打开，而 outbounds 作为 Xray 页面的一个选项卡。「Xray 配置」子菜单现在只保留：Основное、Балансировщик、DNS 和 Расширенный шаблон。指向 `/outbound` 和 `/routing` 的直接链接以及页面刷新都能按预期工作。
- **路由规则可用开关启用和禁用** — 单条路由规则现在可以用开关临时 **禁用**，而无需删除它。规则表中有一列 **「启用」** 带开关，规则表单中的「启用」字段——同样是开关。被禁用的规则不会进入最终的 Xray 配置。统计用的服务规则（`api`）不能禁用——其开关被锁定。
- **路由规则和 outbounds 的导出在预览模态窗口中打开** — 路由规则和出站的 **「导出」** 按钮现在不再立即下载文件，而是打开一个带 JSON 预览以及 **「复制」** 和 **「下载」** 按钮的模态窗口。在「路由」选项卡上，「导入」和「导出」被收进 **「更多」** 下拉菜单（与 Outbounds 选项卡一样）。
- **测试所有出站现在也检查来自订阅的 outbounds；direct/dns 不再被测试** — 「出站」页面上的 **「全部测试」** 按钮现在也检查从订阅获取的 outbounds（「来自订阅」表）——它们的行也会用结果高亮。同时 `freedom`（「direct」）和 `dns` outbounds 在任何模式下都不再被测试（它们不是代理）：它们的测试按钮不可用，「全部测试」会跳过它们。
- **FinalMask：分段数组 Lengths/Delays 取代单个 Length/Delay** — 在 fragment 掩码（FinalMask）中，单个的 Length 和 Delay 字段被列表 Lengths 和 Delays 取代：可为每个分段单独设置长度范围（例如 100-200）和以毫秒计的延迟（例如 10-20 或 0）。行可以添加和删除；先前已保存的值会自动迁移。
- **Loopback outbound：新增 Sniffing 块** — loopback 类型的 outbound 出现了 Sniffing 块，参数与 inbound 相同：启用、destOverride、Metadata Only、Route Only 以及排除域名列表。
- **Hysteria2 / Salamander：Gecko 模式（packetSize）和 Realm 掩码的 TLS** — 在 Hysteria2 的 UDP 掩码（FinalMask）中扩展了功能。Salamander 掩码新增了 Mode 选择器：Gecko 模式为数据包添加随机填充，带 Min/Max 大小字段（从 1 到 2048，默认 512-1200），以防范数据包长度分析。Realm 掩码出现了可选的 TLS Config 块：Server Name (SNI)、ALPN（h3/h2/http/1.1）、Fingerprint 和 Allow Insecure。
- **导入到 outbound 的分享链接会保留 xmux 设置** — 从分享链接导入 outbound 时，现在会保留多路复用器 **xmux**（XHTTP）的设置：此前它们会被悄悄丢失。导入后这些值会填入 XMUX 子表单。
- **来自订阅的 outbounds 的标签保留非 ASCII 字符（西里尔字母）** — 从订阅获取的 outbounds 的标签现在会保留非 ASCII 字符（例如西里尔字母）并保持可读，而不会被简化为只剩数字。

### 12. 节点（多面板，master/slave）
- **节点：新的 TLS 校验模式——Mutual TLS（客户端证书）** — 在节点表单中，TLS 校验模式现在有四个选项：Verify（系统 CA）、Pin（按 SHA-256 固定证书）、Skip（不校验）和新的 Mutual TLS（客户端证书）。在 Mutual TLS 模式下，面板会用其自身 CA 签发的客户端证书额外向节点证明自己；此类节点的 API 令牌变为可选。要启用 mTLS：在节点上设置 Mutual TLS 模式，从 Node mTLS 板块复制管理面板的 CA，在节点上将其登记为受信任的父级 CA，并重启节点。
- **节点：「Node mTLS」板块——复制面板 CA 与受信任的父级 CA** — 在节点页面新增了 Node mTLS 板块，用于配置面板之间的双向 TLS 认证。「复制此面板的 CA」按钮会将面板的根证书复制到剪贴板——需要把它交给将校验面板客户端证书的受管节点。「受信任的父级 CA」字段在面板自身作为节点时使用：把管理面板的 CA 粘贴到这里，以要求其客户端证书，然后重启面板。双向 TLS 按需开启；如果字段为空，节点按原方案工作——仅使用 API 令牌。
- **面板到节点的出站连接路由（Connection outbound）** — 节点表单中出现了 **「Connection outbound」**（出站连接）字段。如果在其中选择某个 Xray-outbound 标签，面板到该节点 API 的流量将经由指定的 outbound（面板会自行在工作配置中添加一个 loopback 上的桥接 inbound，并在不重启的情况下应用它）。空值 = 直接连接。列表中标签被分为「出站」和「负载均衡器」两组，blackhole 出站被隐藏。
- **节点：经由所选 outbound 路由面板→节点流量（「Connection outbound」）** — 节点表单中出现了「Connection outbound」字段：它允许将面板访问节点的流量经由所选的 Xray outbound 转发（可选普通 outbounds 和负载均衡器）。面板会自动在工作配置中添加 loopback-bridge inbound，并在不重启的情况下应用变更。留空表示直接连接。
- **节点：在仍有 inbounds 绑定到节点时阻止删除节点** — 只有在从节点上移除了所有 inbounds 之后才能删除节点。如果节点上仍绑定有至少一个 inbound，面板会以错误拒绝删除——请先解绑或删除这些 inbounds，然后再删除节点。
- **节点：节点页面显示部署在节点上的 inbound 的实时速度** — 在节点页面，对于部署在节点上的 inbound，现在会显示在线客户端、计数器和当前传输速度。「已结束」（ended）芯片只计入已到期和已耗尽流量的客户端（被禁用的客户端不再计入其中）。

### 14. Telegram 机器人
- **通知：带 Telegram 和 Email（SMTP）通道的新事件总线** — 新增了一套事件通知系统，带两个投递通道——Telegram 和 Email。在通知选项卡中，事件以卡片分组：Outbound（中断/恢复）、Xray Core（异常退出）、Nodes（节点不可用/已恢复）、System（CPU 和内存高负载，带可配置的 % 阈值）、Security（登录尝试）。每个分组都有一个主开关和已选事件计数器。已启用事件集可为 Telegram 和 Email 分别配置；默认启用「登录尝试」和「CPU 高负载」。
- **通知：新的 Email/SMTP 通道及 SMTP 服务器设置** — 新增了通过 SMTP 的电子邮件通知通道。在 SMTP 设置选项卡中设置：启用 email 通知、SMTP 主机和端口（默认 587）、用户名、密码（隐藏存储）、收件人列表（逗号分隔）以及加密类型——none、STARTTLS（默认）或 TLS。「发送测试邮件」按钮会检查连接并显示在哪一步（连接、认证、发送）出现了错误。在第二个选项卡中选择将就哪些事件发送邮件。
- **通知：内存高负载告警（RAM 阈值）** — 在 CPU 高负载告警之外，新增了内存高负载告警。在「System」事件分组中出现了「Memory high (%)」，带自己的阈值字段（默认 80%）；面板每分钟检查一次 RAM 负载，超过阈值时向所选通道发送通知。

### 15. 地理库（geoip / geosite 及自定义）
- **地理库更新：逐文件状态以及无变化时跳过重启** — 地理库更新（geoip/geosite，包括 IR 和 RU 套件）现在会显示逐个文件的状态：已更新、已是最新或下载错误。只有在至少一个文件确实被更新时，才会重启 Xray（也就意味着断开活动连接）；无变化时面板不会重启。x-ui update-all-geofiles 命令也有相同的行为。

### 16. 运维：备份、日志、更新、CLI
- **客户端 IP 限制仅在已安装 fail2ban 时生效；否则字段被禁用** — 客户端的 IP 数量限制现在只有在服务器上已安装 fail2ban 时才生效。如果没有，客户端表单中以及批量添加时的「IP Limit」字段会变为不可用并附带说明提示（在 Windows 上——以单独的消息），而此类服务器上先前设置的限制会自动清零，因为它们本就不生效。fail2ban 的封禁现在同时覆盖 TCP 和 UDP。
- **安装和更新面板时自动安装 fail2ban** — 在普通服务器上安装和更新面板时，现在会自动安装并配置 fail2ban（此前仅在 Docker 中如此），以便 IP 限制功能开箱即用。此行为由环境变量 XUI_ENABLE_FAIL2BAN 控制：当变量未设置或等于 true 时执行配置。手动执行可用命令 x-ui setup-fail2ban；fail2ban 出错不会中断安装或更新。
- **通过 XUI_PORT 变量覆盖面板端口** — 新增了环境变量 XUI_PORT，它仅在当前进程运行期间设置 Web 面板端口，而不修改数据库中保存的 webPort 值。允许的值为 1 到 65535；空值、无效值或超出范围的值会被忽略（使用 webPort），并在日志中给出警告。在使用 bridge 网络的 Docker 时，容器发布的端口必须与 XUI_PORT 一致，例如 XUI_PORT=8080 且 ports：「8080:8080」。
- **CLI：-webCert/-webCertKey 标志现在在 setting 子命令中生效** — 在 CLI 中，-webCert 和 -webCertKey 标志现在在 x-ui setting 子命令中也生效了（此前它们会被悄悄忽略，面板仍然没有 HTTPS）。指定它们后，可以直接设置 Web 面板的证书和密钥路径，而无需调用单独的 cert 子命令。
- **数据库备份文件名按服务器地址生成** — 数据库备份文件现在按服务器地址命名，而不是固定的 x-ui.db / x-ui.dump。从浏览器下载时，名称取自地址栏中的面板地址，否则——取自配置的 Web 域名，若没有——取自公网 IP（先 IPv4，后 IPv6）。这样来自不同服务器的备份很容易区分。扩展名对 SQLite 仍为 .db，对 PostgreSQL 为 .dump。
- **支持在仅 IPv6 的主机上安装和更新** — 安装和更新脚本现在能在仅 IPv6 的服务器上正常工作：下载发行版和辅助文件不再强制使用 IPv4，因此可以在没有 IPv4 地址的主机上安装和更新面板。

---

根据面板源文件分析整理。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

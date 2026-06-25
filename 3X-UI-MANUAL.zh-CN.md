# 3X-UI 面板用户手册

🇸🇦 [العربية](3X-UI-MANUAL.ar.md) · 🇬🇧 [English](3X-UI-MANUAL.en.md) · 🇪🇸 [Español](3X-UI-MANUAL.es.md) · 🇮🇷 [فارسی](3X-UI-MANUAL.fa.md) · 🇮🇩 [Bahasa Indonesia](3X-UI-MANUAL.id.md) · 🇯🇵 [日本語](3X-UI-MANUAL.ja.md) · 🇷🇺 [Русский](3X-UI-MANUAL.ru.md) · 🇺🇦 [Українська](3X-UI-MANUAL.uk.md) · 🇨🇳 简体中文 · 🇹🇼 [繁體中文](3X-UI-MANUAL.zh-TW.md)

**3X-UI 版本：3.4.0。** 本手册依据此版本编写，并适用于该版本。3.4.0 相对于 3.3.1 的变更汇总见[「3.4.0 新增内容」](#340-新增内容)一节。

> 关于 **3X-UI** Web 面板（管理 Xray-core）的详细中文手册：功能、配置与运维，逐一讲解界面中的每个字段和
> 开关。
>
> 名称与标签与面板界面保持一致；中文术语按其在界面中显示的样子给出。词语 *inbound* / *outbound* 不
> 翻译。

## 目录

- [3.4.0 新增内容](#340-新增内容)
- [1. 简介、要求与安装](#1-简介要求与安装)
  - [1.1. 什么是 3X-UI](#11-什么是-3x-ui)
  - [1.2. 支持的操作系统与架构](#12-支持的操作系统与架构)
  - [1.3. 安装方式](#13-安装方式)
  - [1.4. 首次启动与默认凭据](#14-首次启动与默认凭据)
  - [1.5. 文件位置](#15-文件位置)
  - [1.6. 管理命令 `x-ui`（脚本菜单）](#16-管理命令-x-ui脚本菜单)
  - [1.7. `x-ui` 子命令（无交互菜单）](#17-x-ui-子命令无交互菜单)
  - [1.8. SQLite → PostgreSQL 迁移](#18-sqlite--postgresql-迁移)
- [2. 登录面板与访问安全](#2-登录面板与访问安全)
  - [2.1. 登录表单](#21-登录表单)
  - [2.2. 双因素认证（2FA / TOTP）](#22-双因素认证2fa--totp)
  - [2.3. 登录尝试限制（login limiter / 防暴力破解）](#23-登录尝试限制login-limiter--防暴力破解)
  - [2.4. 修改管理员登录名和密码](#24-修改管理员登录名和密码)
  - [2.5. 密钥路径（URI 路径 / webBasePath）和面板端口](#25-密钥路径uri-路径--webbasepath和面板端口)
  - [2.6. 会话生存时间（超时）](#26-会话生存时间超时)
  - [2.7. LDAP（同步与认证）](#27-ldap同步与认证)
- [3. 概览 / 仪表盘](#3-概览--仪表盘)
  - [3.1. 数据采集的通用原则](#31-数据采集的通用原则)
  - [3.2. CPU（ЦП）](#32-cpuцп)
  - [3.3. 内存（RAM）](#33-内存ram)
  - [3.4. 交换空间（Swap）](#34-交换空间swap)
  - [3.5. 磁盘（Storage）](#35-磁盘storage)
  - [3.6. 系统运行时间（Uptime）](#36-系统运行时间uptime)
  - [3.7. 系统负载（Load average）](#37-系统负载load-average)
  - [3.8. 网络：速度与总流量](#38-网络速度与总流量)
  - [3.9. 服务器 IP 地址](#39-服务器-ip-地址)
  - [3.10. TCP/UDP 连接](#310-tcpudp-连接)
  - [3.11. Xray 状态与进程管理](#311-xray-状态与进程管理)
  - [3.12. 面板更新（3X-UI）](#312-面板更新3x-ui)
  - [3.13. 地理文件更新（GeoIP / GeoSite）](#313-地理文件更新geoip--geosite)
  - [3.14. 数据库的备份与恢复](#314-数据库的备份与恢复)
  - [3.15. 其他界面元素](#315-其他界面元素)
- [4. Inbounds：创建与通用参数](#4-inbounds创建与通用参数)
  - [4.1. 表单通用字段](#41-表单通用字段)
  - [4.2. Sniffing（嗅探）](#42-sniffing嗅探)
  - [4.3. Allocate（端口分配策略）](#43-allocate端口分配策略)
  - [4.4. External Proxy（外部代理）](#44-external-proxy外部代理)
  - [4.5. Fallbacks（Fallback 项）](#45-fallbacksfallback-项)
  - [4.6. 定期流量重置](#46-定期流量重置)
  - [4.7. inbound 的 JSON（advanced）](#47-inbound-的-jsonadvanced)
  - [4.8. inbound 的操作：QR / Edit / Reset / Delete 与统计](#48-inbound-的操作qr--edit--reset--delete-与统计)
- [5. 协议](#5-协议)
  - [5.1. 支持的协议列表](#51-支持的协议列表)
  - [5.2. 哪些协议支持 TLS / REALITY / 传输](#52-哪些协议支持-tls--reality--传输)
  - [5.3. VLESS](#53-vless)
  - [5.4. VMess](#54-vmess)
  - [5.5. Trojan](#55-trojan)
  - [5.6. Shadowsocks](#56-shadowsocks)
  - [5.7. Dokodemo-door / Tunnel（透明转发器）](#57-dokodemo-door--tunnel透明转发器)
  - [5.8. SOCKS / HTTP（`mixed` 协议）](#58-socks--httpmixed-协议)
  - [5.9. WireGuard（inbound）](#59-wireguardinbound)
  - [5.10. Hysteria（默认 v2）](#510-hysteria默认-v2)
  - [5.11. MTProto（Telegram 代理）](#511-mtprototelegram-代理)
  - [5.12. 协议选择简明速查表](#512-协议选择简明速查表)
- [6. 传输（Stream Settings）](#6-传输stream-settings)
  - [6.1. 选择传输网络](#61-选择传输网络)
  - [6.2. RAW / TCP（`tcpSettings`）](#62-raw--tcptcpsettings)
  - [6.3. mKCP（`kcpSettings`）](#63-mkcpkcpsettings)
  - [6.4. WebSocket（`wsSettings`）](#64-websocketwssettings)
  - [6.5. gRPC（`grpcSettings`）](#65-grpcgrpcsettings)
  - [6.6. HTTPUpgrade（`httpupgradeSettings`）](#66-httpupgradehttpupgradesettings)
  - [6.7. XHTTP / SplitHTTP（`xhttpSettings`）](#67-xhttp--splithttpxhttpsettings)
  - [6.8. Hysteria 传输（`hysteriaSettings`）](#68-hysteria-传输hysteriasettings)
  - [6.9. 相关参数](#69-相关参数)
- [7. 连接安全：TLS、XTLS 与 REALITY](#7-连接安全tlsxtls-与-reality)
  - [7.1. 有何区别：TLS vs XTLS vs REALITY](#71-有何区别tls-vs-xtls-vs-reality)
  - [7.2. 「无」模式（`none`）](#72-无模式none)
  - [7.3. TLS 模式](#73-tls-模式)
  - [7.4. REALITY 模式](#74-reality-模式)
  - [7.5. 配置实践建议](#75-配置实践建议)
- [8. 客户端](#8-客户端)
  - [8.1. 客户端字段](#81-客户端字段)
  - [8.2. 绑定到 inbound](#82-绑定到-inbound)
  - [8.3. 客户端操作](#83-客户端操作)
  - [8.4. 批量操作](#84-批量操作)
  - [8.5. 搜索、过滤与排序](#85-搜索过滤与排序)
  - [8.6. 图标与状态](#86-图标与状态)
- [9. 客户端组](#9-客户端组)
  - [9.1. 什么是客户端组以及为何需要它](#91-什么是客户端组以及为何需要它)
  - [9.2. 组与客户端、inbound、节点和协议的关系](#92-组与客户端inbound节点和协议的关系)
  - [9.3. 组目录与「空」组](#93-组目录与空组)
  - [9.4. 组的字段与列](#94-组的字段与列)
  - [9.5. 创建组](#95-创建组)
  - [9.6. 重命名组](#96-重命名组)
  - [9.7. 向组添加客户端](#97-向组添加客户端)
  - [9.8. 从组中移除客户端（不删除客户端本身）](#98-从组中移除客户端不删除客户端本身)
  - [9.9. 重置组流量](#99-重置组流量)
  - [9.10. 删除组与删除组内客户端](#910-删除组与删除组内客户端)
  - [9.11. 与「客户端」页的关联](#911-与客户端页的关联)
  - [9.12. API 端点汇总](#912-api-端点汇总)
  - [9.13. 按组统计流量](#913-按组统计流量)
- [10. 订阅（Subscription）](#10-订阅subscription)
  - [10.1. 什么是 subId 以及链接如何生成](#101-什么是-subid-以及链接如何生成)
  - [10.2. 订阅服务器设置](#102-订阅服务器设置)
  - [10.3. 输出格式](#103-输出格式)
  - [10.4. 订阅信息页面与二维码](#104-订阅信息页面与二维码)
  - [10.5. 自定义订阅页面模板](#105-自定义订阅页面模板)
- [11. Xray：路由、outbounds、DNS 与扩展](#11-xray路由outboundsdns-与扩展)
  - [11.1. 编辑器结构：选项卡/模式](#111-编辑器结构选项卡模式)
  - [11.2. 基本设置（General）](#112-基本设置general)
  - [11.3. 路由规则（routing）](#113-路由规则routing)
  - [11.4. Outbounds（出站连接）](#114-outbounds出站连接)
  - [11.5. 负载均衡器（Balancers）](#115-负载均衡器balancers)
  - [11.6. DNS](#116-dns)
  - [11.7. Fake DNS](#117-fake-dns)
  - [11.8. WireGuard / WARP / NordVPN](#118-wireguard--warp--nordvpn)
  - [11.9. Reverse 代理与 TUN](#119-reverse-代理与-tun)
  - [11.10. 日志与统计（Stats、metrics）](#1110-日志与统计statsmetrics)
  - [11.11. 保存、重启与自动转换](#1111-保存重启与自动转换)
  - [11.12. 来自订阅的 outbound（带自动更新）](#1112-来自订阅的-outbound带自动更新)
  - [11.13. WARP 中的 IP 轮换](#1113-warp-中的-ip-轮换)
- [12. 节点（多面板，master/slave）](#12-节点多面板masterslave)
  - [12.1. 列表顶部的汇总](#121-列表顶部的汇总)
  - [12.2. 添加与编辑节点](#122-添加与编辑节点)
  - [12.3. TLS 校验（针对 https 节点）](#123-tls-校验针对-https-节点)
  - [12.4. 每个节点显示的内容](#124-每个节点显示的内容)
  - [12.5. 节点操作](#125-节点操作)
  - [12.6. 指标历史](#126-指标历史)
  - [12.7. inbounds 和客户端如何同步](#127-inbounds-和客户端如何同步)
  - [12.8. 节点链（子节点 / 传递节点）](#128-节点链子节点--传递节点)
  - [12.9. 节点：3.3.0 新增](#129-节点330-新增)
- [13. 面板设置](#13-面板设置)
  - [13.1. 保存与重启面板](#131-保存与重启面板)
  - [13.2. 常规设置（「面板」选项卡 / *General*）](#132-常规设置面板选项卡--general)
  - [13.3. 面板访问：IP、端口、路径、域名、证书](#133-面板访问ip端口路径域名证书)
  - [13.4. 会话、面板代理与受信任代理（「代理与服务器」选项卡 / *Proxy and Server*）](#134-会话面板代理与受信任代理代理与服务器选项卡--proxy-and-server)
  - [13.5. Telegram 机器人（「Telegram 机器人」选项卡 / *Telegram Bot*）](#135-telegram-机器人telegram-机器人选项卡--telegram-bot)
  - [13.6. 日期与时间（「日期与时间」选项卡 / *Date and Time*）](#136-日期与时间日期与时间选项卡--date-and-time)
  - [13.7. 外部流量与 Xray 行为（「外部流量」选项卡 / *External Traffic*）](#137-外部流量与-xray-行为外部流量选项卡--external-traffic)
  - [13.8. 其他：Xray 配置模板与校验 URL](#138-其他xray-配置模板与校验-url)
  - [13.9. 管理员账户与 API 令牌](#139-管理员账户与-api-令牌)
  - [13.10. 3.3.0 中的 API 变更（对集成很重要）](#1310-330-中的-api-变更对集成很重要)
- [14. Telegram 机器人](#14-telegram-机器人)
  - [14.1. 启用与配置机器人](#141-启用与配置机器人)
  - [14.2. 主菜单与按钮](#142-主菜单与按钮)
  - [14.3. 机器人命令](#143-机器人命令)
  - [14.4. 客户端管理（仅管理员）](#144-客户端管理仅管理员)
  - [14.5. 通知与报告](#145-通知与报告)
  - [14.6. 备份与日志](#146-备份与日志)
  - [14.7. 运行特性](#147-运行特性)
- [15. 地理库（geoip / geosite 及自定义）](#15-地理库geoip--geosite-及自定义)
  - [15.1. 什么是 geoip.dat 和 geosite.dat](#151-什么是-geoipdat-和-geositedat)
  - [15.2. 标准地理文件及其更新](#152-标准地理文件及其更新)
  - [15.3. 自定义地理资源（Custom GeoSite / GeoIP）](#153-自定义地理资源custom-geosite--geoip)
  - [15.4. 校验与限制](#154-校验与限制)
  - [15.5. 面板启动时的自动检查](#155-面板启动时的自动检查)
  - [15.6. 在路由规则中使用地理库](#156-在路由规则中使用地理库)
- [16. 运维：备份、日志、更新、CLI](#16-运维备份日志更新cli)
  - [16.1. 数据库的备份与恢复](#161-数据库的备份与恢复)
  - [16.2. 查看日志](#162-查看日志)
  - [16.3. Xray 日志级别与配置](#163-xray-日志级别与配置)
  - [16.4. Xray 管理：停止与重启](#164-xray-管理停止与重启)
  - [16.5. 重启与更新面板](#165-重启与更新面板)
  - [16.6. 定期任务（cron）](#166-定期任务cron)
  - [16.7. 控制台菜单与 CLI（`x-ui`）](#167-控制台菜单与-clix-ui)
  - [16.8. 卸载面板](#168-卸载面板)
  - [16.9. 命令 `x-ui migrateDB`](#169-命令-x-ui-migratedb)

---

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

## 1. 简介、要求与安装

### 1.1. 什么是 3X-UI

**3X-UI** 是一款用于 [Xray-core](https://github.com/XTLS/Xray-core) 服务器的开源 Web 管理面板。该面板提供统一的多语言 Web 界面，用于部署、配置和监控种类广泛的代理与 VPN 协议：从单台 VPS 到由多个节点组成的分布式配置。

3X-UI 是原始项目 X-UI 的增强分支。与之相比，它增加了对更多协议的支持，提升了稳定性，加入了逐客户端的流量统计以及大量便捷功能。

主要功能：

- **多种协议的 inbound** —— VLESS、VMess、Trojan、Shadowsocks、WireGuard、Hysteria2、HTTP、SOCKS（Mixed）、Dokodemo-door / Tunnel、TUN 以及 **MTProto**（Telegram 代理，于 3.3.0 加入）。
- **现代化的传输方式与加密** —— TCP (Raw)、mKCP、WebSocket、gRPC、HTTPUpgrade 和 XHTTP，可由 TLS、XTLS 和 REALITY 进行保护。
- **Fallback** —— 通过 Xray 的 fallback 机制在同一端口上提供多种协议（例如在 443 上同时提供 VLESS 和 Trojan）。
- **逐客户端管理** —— 流量配额、到期日期、IP 数量限制、显示「在线」状态、一键邀请链接、二维码和订阅。
- **流量统计** —— 针对每个 inbound、客户端和 outbound，并支持重置。
- **支持多节点** —— 在单个面板中管理并扩展至多台服务器。
- **outbound 与路由** —— WARP、NordVPN、自定义路由规则、负载均衡器、代理链。
- **内置订阅服务器**，支持多种输出格式。
- **Telegram 机器人**，用于远程监控和管理。
- **REST API**，附带内置的 Swagger 文档。
- **灵活的存储** —— SQLite（默认）或 PostgreSQL。
- **13 种界面语言**，深色和浅色主题。
- **与 Fail2ban 集成**，用于应用逐客户端的 IP 限制。

> 重要提示：本项目仅供个人使用。不建议将其用于非法目的或生产环境。

### 1.2. 支持的操作系统与架构

#### 操作系统

安装脚本根据 `/etc/os-release`（或 `/usr/lib/os-release`）中的 `ID` 字段来识别发行版。官方支持：

Ubuntu、Debian、Armbian、Fedora、CentOS、RHEL、AlmaLinux、Rocky Linux、Oracle Linux、Amazon Linux、Virtuozzo、Arch、Manjaro、Parch、openSUSE（Tumbleweed / Leap）、Alpine，以及 Windows。

在 Alpine 系列系统上使用 OpenRC 服务（`rc-service` / `rc-update`），其余系统则使用 systemd。对于 CentOS 7，软件包通过 `yum` 安装；对于更新的版本，则通过 `dnf` 安装。如果未能识别发行版，脚本默认会尝试使用 `apt-get` 包管理器。

#### 处理器架构

架构通过 `uname -m` 的输出来确定，并归一化为以下受支持的某个值：

| `uname -m` 的值 | 3X-UI 架构 |
| --- | --- |
| `x86_64`, `x64`, `amd64` | `amd64` |
| `i*86`, `x86` | `386` |
| `armv8*`, `arm64`, `aarch64` | `arm64` |
| `armv7*`, `arm` | `armv7` |
| `armv6*` | `armv6` |
| `armv5*` | `armv5` |
| `s390x` | `s390x` |

如果架构不在此列表中，脚本会输出「Unsupported CPU architecture!」消息并终止安装。

#### 基础依赖

在安装面板之前，脚本会自动安装一组基础软件包（其名称因发行版而异）：`cron`/`cronie`/`dcron`、`curl`、`tar`、`tzdata`/`timezone`、`socat`、`ca-certificates`、`openssl`。

### 1.3. 安装方式

#### 方式 1。安装脚本（推荐）

以 root 身份用一条命令完成安装：

```bash
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)
```

脚本必须要求 root 权限：以非 root 身份运行时会输出「Please run this script with root privilege」并以错误退出。

安装程序逐步执行的操作：

1. 识别操作系统和架构。
2. 安装基础依赖。
3. 下载发布版归档 `x-ui-linux-<arch>.tar.gz` 并将其解压到目录 `/usr/local/x-ui`。
4. 下载管理脚本 `x-ui.sh` 并将其安装为命令 `/usr/bin/x-ui`。
5. 创建日志目录 `/var/log/x-ui`。
6. 启动初始配置：选择数据库、生成凭据、选择端口、可选的 SSL 配置。
7. 安装并启动自启动服务（systemd 单元 `x-ui.service`，或用于 Alpine 的 OpenRC init 脚本）。

**安装时选择数据库。** 安装程序提供：

- `1) SQLite`（默认，在客户端数量 < 500 时推荐）—— 单个文件 `/etc/x-ui/x-ui.db`，无需配置。
- `2) PostgreSQL`（在客户端数量较多或存在多个节点时推荐）。PostgreSQL 可以在本地安装（会创建一个专用用户和名为 `xui` 的数据库），也可以指定指向现有服务器的 DSN。连接参数会以 `XUI_DB_TYPE` 和 `XUI_DB_DSN` 变量的形式写入服务的环境文件（根据发行版不同，为 `/etc/default/x-ui`、`/etc/conf.d/x-ui` 或 `/etc/sysconfig/x-ui`）。

**示例：将 PostgreSQL 参数写入服务环境文件。** 在选择 PostgreSQL 并指定 DSN 后，安装程序会向环境文件中添加大致如下的几行：

```bash
XUI_DB_TYPE=postgres
XUI_DB_DSN=postgres://xui:S3cretPass@127.0.0.1:5432/xui?sslmode=disable
```

这里 `xui` 是用户名和数据库名，`127.0.0.1:5432` 是服务器的地址和端口，`sslmode=disable` 适用于本地连接（对于远程服务器通常使用 `require`）。

**安装指定的（旧）版本。** 可以显式指定版本标签 —— 安装程序会下载相应的发布版：

```bash
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/v2.4.0/install.sh) v2.4.0
```

此类安装允许的最低版本是 `v2.3.5`；指定更旧的版本时会输出「Please use a newer version (at least v2.3.5)」。

#### 方式 2。Docker

以默认的 SQLite 数据库启动：

```bash
docker compose up -d
```

若要以内置的 PostgreSQL 服务启动，需要取消 `docker-compose.yml` 中 `XUI_DB_*` 行的注释，并使用 profile 启动：

```bash
docker compose --profile postgres up -d
```

镜像包含 Fail2ban（默认启用），用于应用逐客户端的 IP 限制。Fail2ban 通过 `iptables` 封禁违规者，这需要 `NET_ADMIN` 能力。在 `docker-compose.yml` 中该能力已通过 `cap_add` 授予。通过 `docker run` 手动启动时需要自行添加这些能力，否则封禁只会被记录到日志，而不会实际应用：

**示例：完整的 `docker run` 命令。** 包含面板端口转发、网络能力以及用于数据库的持久卷的最小化版本：

```bash
docker run -d \
  --name 3x-ui \
  --restart unless-stopped \
  --cap-add=NET_ADMIN --cap-add=NET_RAW \
  -v $PWD/db:/etc/x-ui \
  -v $PWD/cert:/root/cert \
  -p 2053:2053 \
  ghcr.io/mhsanaei/3x-ui:latest
```

卷 `/etc/x-ui` 会在容器重启之间保存 `x-ui.db` 文件，否则设置和账户都将丢失。

```bash
docker run -d --cap-add=NET_ADMIN --cap-add=NET_RAW ... ghcr.io/mhsanaei/3x-ui
```

在 Docker 中，面板是容器的主进程：自启动由容器的重启策略（例如 `restart: unless-stopped`）控制，而不是由容器内部的某个服务控制。

### 1.4. 首次启动与默认凭据

首次安装时（此时仍使用默认凭据），安装程序会**为用户名、密码、Web 路径以及端口生成随机值**：

| 参数 | 安装时如何生成 | 备注 |
| --- | --- | --- |
| 用户名（Username） | 由 10 个字符组成的随机字符串 | 自动生成 |
| 密码（Password） | 由 10 个字符组成的随机字符串 | 自动生成 |
| 面板 Web 路径（WebBasePath） | 由 18 个字符组成的随机字符串 | 保护面板不被通过根 URL 发现 |
| 面板端口（Port） | 默认为 1024–62000 范围内的随机端口；如有需要可手动设置 | `webPort` 的「出厂」值为 `2053`，但安装程序会覆盖它 |

安装结束时，脚本会输出最终的汇总信息：用户名、密码、端口、Web 路径、API 令牌以及一个可直接使用的登录链接（Access URL），形式如下：

```
https://<域名或IP>:<端口>/<web路径>
```

如果未配置 SSL 证书，该链接将为 `http://`，并且脚本会输出关于需要配置 SSL 的警告（菜单项 19）。

> 必须更改凭据。由于登录名和密码是随机生成的，应在**安装后立即保存**。可以随时通过菜单项「Reset Username & Password」（见下文）或从 Web 界面的面板设置中更改它们。重置后，脚本会提醒：「Please use the new login username and password to access the X-UI panel. Also remember them!」。

安装完成后，使用命令 `x-ui` 打开管理菜单（见 1.6 节）。

### 1.5. 文件位置

| 路径 | 用途 |
| --- | --- |
| `/usr/local/x-ui/` | 面板安装目录（二进制文件 `x-ui`、脚本 `x-ui.sh`） |
| `/usr/local/x-ui/bin/xray-linux-<arch>` | Xray-core 二进制文件（在 armv5/armv6/armv7 上重命名为 `xray-linux-arm`） |
| `/usr/bin/x-ui` | 管理脚本（命令 `x-ui`） |
| `/etc/x-ui/x-ui.db` | SQLite 数据库文件（默认） |
| `/var/log/x-ui/` | 面板日志目录 |
| `/etc/systemd/system/x-ui.service` | 服务的 systemd 单元（非 Alpine） |
| `/etc/init.d/x-ui` | OpenRC init 脚本（仅 Alpine） |
| `/etc/default/x-ui` · `/etc/conf.d/x-ui` · `/etc/sysconfig/x-ui` | 服务环境变量文件（路径取决于发行版）；`XUI_DB_TYPE`/`XUI_DB_DSN` 写入此处 |

数据库目录可以通过环境变量 `XUI_DB_FOLDER` 覆盖（默认 `/etc/x-ui`），Xray 二进制文件目录可以通过变量 `XUI_BIN_FOLDER` 覆盖（默认为相对面板目录的 `bin`）。数据库文件名为 `x-ui.db`。

**示例：将数据库移到单独的磁盘。** 若要将 `x-ui.db` 存放在 `/etc/x-ui` 以外的位置（例如挂载的磁盘 `/data`），请在服务环境文件中设置该变量并重启面板：

```bash
echo 'XUI_DB_FOLDER=/data/x-ui' >> /etc/default/x-ui
mkdir -p /data/x-ui
systemctl restart x-ui
```

数据库的完整路径将变为 `/data/x-ui/x-ui.db`。

#### 主要环境变量

| 变量 | 用途 | 默认值 |
| --- | --- | --- |
| `XUI_DB_TYPE` | 数据库后端：`sqlite` 或 `postgres` | `sqlite` |
| `XUI_DB_DSN` | PostgreSQL 连接字符串（当 `XUI_DB_TYPE=postgres` 时） | — |
| `XUI_DB_FOLDER` | SQLite 数据库文件目录 | `/etc/x-ui` |
| `XUI_INIT_WEB_BASE_PATH` | Web 面板的初始 URI 路径（仅在首次初始化时） | `/` |
| `XUI_DB_MAX_OPEN_CONNS` | 最大打开连接数（PostgreSQL 连接池） | — |
| `XUI_DB_MAX_IDLE_CONNS` | 最大空闲连接数（PostgreSQL 连接池） | — |
| `XUI_ENABLE_FAIL2BAN` | 通过 Fail2ban 启用 IP 限制 | `true` |
| `XUI_LOG_LEVEL` | 日志级别（`debug`、`info`、`warning`、`error`） | `info` |
| `XUI_DEBUG` | 调试模式 | `false` |

**示例：临时启用详细日志。** 为诊断问题，将日志级别提升到 `debug` 并重启服务：

```bash
echo 'XUI_LOG_LEVEL=debug' >> /etc/default/x-ui
systemctl restart x-ui
x-ui log    # 查看调试日志
```

诊断完成后，将值改回 `info`，以免日志过度增长。

**通过环境设置 Web 面板的初始路径。** 变量 `XUI_INIT_WEB_BASE_PATH` 在首次初始化设置时设定 Web 面板的 URI 路径（`webBasePath`）。这在通过 Docker 或 systemd 部署时很方便，可以立即固定面板的登录路径。该值会自动归一化 —— 必要时会添加前导和结尾斜杠，而空值或仅由空格组成的值会被忽略（此时会应用默认路径 `/`）。该变量**仅影响首次初始化**：如果设置已创建，则需在 Web 界面或通过菜单项「Reset Web Base Path」更改路径。

### 1.6. 管理命令 `x-ui`（脚本菜单）

安装完成后，命令 `x-ui`（以 root 身份运行）会打开交互式菜单「3X-UI Panel Management Script」。通过输入菜单项编号来选择（范围 0–27）。许多菜单项也可作为子命令在脚本中使用（见 1.7 节）。

菜单按主题分块。

#### 安装与更新

- **1. Install** —— 安装面板（运行 `install.sh`）。安装前会检查面板是否尚未安装。
- **2. Update** —— 将 x-ui 的所有组件更新到最新版本。此过程不会丢失数据；更新后面板会自动重启。需要确认。
- **3. Update Menu** —— 仅将管理脚本（`x-ui.sh` / 命令 `x-ui`）更新到最新版本，而不重新安装面板。
- **4. Legacy Version** —— 安装指定的（旧）面板版本。脚本会询问版本号（例如 `2.4.0`）并下载相应的发布版。
- **5. Uninstall** —— 完全卸载面板**连同 Xray**。会停止并禁用服务，删除目录 `/etc/x-ui/` 和 `/usr/local/x-ui/`、服务环境文件以及管理脚本本身。需要确认（默认为「否」）。

#### 凭据与设置

- **6. Reset Username & Password** —— 重置面板的用户名和密码。可以输入自定义值，或留空以随机生成（随机用户名为 10 个字符，随机密码为 18 个字符）。此外还会提示是否关闭双因素认证（2FA），如果已配置的话。重置后面板会重启。
- **7. Reset Web Base Path** —— 重置面板的 Web 路径：生成一个新的随机路径（18 个字符），面板会重启。在原路径被泄露或遗忘时使用。
- **8. Reset Settings** —— 将面板的所有设置重置为默认值。**此过程不会丢失凭据（用户名和密码）和账户数据。** 需要确认；重置后面板会重启。
- **9. Change Port** —— 更改 Web 面板端口。会询问端口号（1–65535）；设置后需要重启，端口才会生效。
- **10. View Current Settings** —— 查看当前设置（`x-ui setting -show`）。其中会显示所使用的数据库后端（SQLite，或 DSN 中密码被掩码的 PostgreSQL）以及可直接使用的访问链接（Access URL）。如果未配置 SSL，会提示为 IP 地址签发 Let's Encrypt 证书。

#### 服务管理

- **11. Start** —— 启动面板服务。如果面板已在运行，会输出无需重复启动的消息。
- **12. Stop** —— 停止面板服务。
- **13. Restart** —— 重启面板服务。
- **14. Restart Xray** —— 仅重启 Xray-core 内核，而不重启面板本身（通过 `systemctl reload x-ui`，在 Docker 中则向面板进程发送 `USR1` 信号）。
- **15. Check Status** —— 检查服务状态（`systemctl status x-ui` 或 `rc-service x-ui status`）。
- **16. Logs Management** —— 日志管理：查看调试日志（Debug Log，通过 `journalctl`），以及（Alpine 除外）清除所有日志（Clear All logs）。

#### 自启动

- **17. Enable Autostart** —— 启用面板在操作系统启动时自启动（`systemctl enable x-ui` 或 `rc-update add`）。
- **18. Disable Autostart** —— 禁用操作系统启动时的自启动。

在 Docker 中，自启动由容器的重启策略控制，因此这些菜单项只会输出相应的提示。

#### 安全与网络

- **19. SSL Certificate Management** —— 通过 acme.sh 管理 SSL 证书：为域名签发证书、吊销、强制续期、查看现有域名、为面板指定证书路径，以及为 IP 地址签发短期（约 6 天，带自动续期）证书。
- **20. Cloudflare SSL Certificate** —— 通过 Cloudflare 的 DNS 验证签发 SSL 证书。
- **21. IP Limit Management** —— 管理逐客户端的 IP 数量限制（基于 Fail2ban）：查看和解除封禁等。
- **22. Firewall Management** —— 管理防火墙（打开/关闭端口以及查看规则）。
- **23. SSH Port Forwarding Management** —— 配置 SSH 端口转发，以便通过 SSH 隧道从本地机器打开面板。

#### 性能与维护

- **24. Enable BBR** —— 启用/禁用 TCP BBR 拥塞控制算法（带 Enable BBR / Disable BBR 项的子菜单）。
- **25. Update Geo Files** —— 更新 geo 数据库（`.dat` 文件），可选择来源：Loyalsoldier（`geoip.dat`、`geosite.dat`）、chocolate4u（`geoip_IR.dat`、`geosite_IR.dat`）、runetfreedom（`geoip_RU.dat`、`geosite_RU.dat`）或 All（一次性全部）。更新后面板会重启。
- **26. Speedtest by Ookla** —— 通过 Speedtest by Ookla 运行网络速度测试。
- **27. PostgreSQL Management** —— 管理内置/关联的 PostgreSQL 实例（启用及相关操作）。
- **0. Exit Script** —— 退出菜单。

### 1.7. `x-ui` 子命令（无交互式菜单）

为了在脚本中使用，命令 `x-ui` 支持直接子命令（不带参数运行 `x-ui` 会打开菜单）：

| 命令 | 操作 |
| --- | --- |
| `x-ui` | 打开管理菜单 |
| `x-ui start` | 启动面板 |
| `x-ui stop` | 停止面板 |
| `x-ui restart` | 重启面板 |
| `x-ui restart-xray` | 重启 Xray |
| `x-ui status` | 当前服务状态 |
| `x-ui settings` | 当前设置 |
| `x-ui enable` | 启用操作系统启动时的自启动 |
| `x-ui disable` | 禁用自启动 |
| `x-ui log` | 查看日志 |
| `x-ui banlog` | 查看 Fail2ban 封禁日志 |
| `x-ui update` | 更新面板 |
| `x-ui update-all-geofiles` | 更新所有 geo 文件 |
| `x-ui migrateDB [file]` | `.db` ↔ `.dump` 转换（SQLite） |
| `x-ui legacy` | 安装旧版本 |
| `x-ui install` | 安装面板 |
| `x-ui uninstall` | 卸载面板 |

### 1.8. 从 SQLite 迁移到 PostgreSQL

现有的 SQLite 安装可以迁移到 PostgreSQL：

```bash
x-ui migrate-db --dsn "postgres://xui:password@127.0.0.1:5432/xui?sslmode=disable"
# 然后在 /etc/default/x-ui 中设置 XUI_DB_TYPE 和 XUI_DB_DSN 并重启：
systemctl restart x-ui
```

原始的 SQLite 文件保持原样不动 —— 只在验证新后端工作正常后再手动删除它。

**示例：验证已切换到 PostgreSQL。** 迁移后，用查看设置的命令确认面板确实运行在新后端上 —— 输出中应显示 PostgreSQL（DSN 中的密码会被掩码）：

```bash
x-ui settings | grep -i -E 'db|dsn'
```

如果面板能够打开且账户仍在，就可以删除原始的 `x-ui.db`。

---

## 2. 登录面板与访问安全

本节介绍与 3X-UI 面板管理员认证相关的所有内容：登录表单、双因素认证（TOTP）、密码暴力破解防护、修改账户凭据、修改面板的密钥路径和端口、会话生存时间，以及通过 LDAP 进行同步/认证。

### 2.1. 登录表单

登录页面通过面板密钥路径（`webBasePath`）的根路径提供。如果用户已经授权，会自动重定向到 `…/panel/`。页面上有主题切换、界面语言选择以及登录表单本身。

表单字段：

| 字段 | 提示/标题（RU） | 必填 | 说明 |
|------|--------------------------|-------------|----------|
| 用户名 | «Имя пользователя» | 是 | 管理员登录名。空值会在客户端被拒绝，在服务器端则以消息「请输入用户名」拒绝。 |
| 密码 | «Пароль» | 是 | 管理员密码。空值会以消息「请输入密码」拒绝。 |
| 2FA 代码 | «Код 2FA» | 仅在启用 2FA 时 | 该字段**仅**在面板启用双因素认证时出现。来自认证应用的 6 位代码。 |

按钮 **«Войти»**（登录）将表单提交至 `POST /login`。

行为与消息：

- 登录成功时显示「登录成功」并跳转至 `…/panel/`。
- 当账户凭据有任何错误或 2FA 代码不正确时，服务器返回**统一**消息：「账户数据错误。」（英文：*Invalid username or password or two-factor code.*）。这是有意为之——面板不会提示具体哪一项错误（登录名、密码还是代码），以免为暴力破解提供便利。
- 面板根据 `POST /getTwoFactorEnable` 请求来显示或隐藏「2FA 代码」字段，该请求在授权之前就返回当前的 2FA 状态。
- 如果服务器会话已过期，则在下一次请求时显示「会话已过期。请重新登录」，并将用户重定向到登录页面。

> 关于 CSRF 的说明：客户端在提交表单之前会获取一个 CSRF 令牌（`GET /csrf-token`）；`/login` 和 `/logout` 请求受 CSRF 校验保护。

**示例：通过 API 登录。** 当 2FA 关闭时，只需登录名和密码即可；启用 2FA 时会增加 `twoFactorCode` 字段：

```bash
# Без 2FA
curl -i -X POST https://panel.example.com:2053/мой-секрет/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'username=admin&password=ВашПароль'

# С включённой 2FA — добавляется 6-значный код
curl -i -X POST https://panel.example.com:2053/мой-секрет/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'username=admin&password=ВашПароль&twoFactorCode=123456'
```

成功时服务器会返回带有会话 cookie 的 `Set-Cookie`——正是它需要在后续对 `/panel/api/…` 的请求中传递。

### 2.2. 双因素认证（2FA / TOTP）

3X-UI 中的 2FA 按照 **TOTP** 标准实现，并兼容任何认证应用（Google Authenticator、Aegis、FreeOTP 等）。参数被固定写死：算法 **SHA1**、**6** 位数字、周期 **30** 秒、发行方（issuer）`3x-ui`、标签 `Administrator`。

**示例：编码到 QR 码中的 otpauth-URI。** 如果认证应用无法用相机扫描，可以通过以下链接手动添加令牌（用你自己的 Base32 密钥替换 `JBSWY3DPEHPK3PXP`）：

```
otpauth://totp/3x-ui:Administrator?secret=JBSWY3DPEHPK3PXP&issuer=3x-ui&algorithm=SHA1&digits=6&period=30
```

参数 `algorithm=SHA1`、`digits=6`、`period=30` 与面板写死的值一致——无需更改。

设置位于 **Настройки → Учетная запись** 部分的 **«Двухфакторная аутентификация»** 选项卡中。

| 元素 | 文本（RU） | 说明 |
|---------|------------|----------|
| 开关 | «Включить 2FA» | 启用/关闭双因素认证。 |
| 说明 | «Добавляет дополнительный уровень аутентификации для повышения безопасности.» | 开关下方的提示。 |

#### 如何启用 2FA

启用开关时，面板会**在本地生成一个新密钥**——一个 Base32 编码的随机字符串（字母表为 `A–Z` 和 `2–7`）。随后会打开「启用双因素认证」窗口，并附带分步说明：

1. **«Отсканируйте этот QR-код в приложении для аутентификации или скопируйте токен рядом с QR-кодом и вставьте его в приложение»**。QR 码下方以文本形式显示密钥本身——点击 QR 码即可将密钥复制到剪贴板（弹出「已复制」）。
2. **«Введите код из приложения»** ——需要输入应用生成的 6 位代码。代码**在浏览器端**校验：面板会根据刚刚生成的密钥自行计算当前的 TOTP，并与输入值比较。如果代码不正确——「代码错误」；该字段只接受恰好 6 位数字。

只有在成功确认之后，密钥和启用标志才会被保存。保存时显示「双因素认证已成功设置」。

重要：设置部分的更改需通过通用按钮 **«Сохранить»** 应用，之后通常需要重启面板（「保存更改并重启面板以使其生效」）。首次启用 2FA 时，服务器还会额外**使所有活动会话失效**（递增「login epoch」），因此应用设置后需要重新登录——这次要带上 2FA 代码。

#### 如何关闭 2FA

再次点击开关会打开「关闭双因素认证」窗口，并附带提示「输入应用中的代码以关闭双因素认证。」。输入正确代码后，标志和密钥会被清除，并显示「双因素认证已成功删除」。

#### 登录时的代码校验

登录时，服务器取出已保存的密钥，并将当前的 TOTP 与传入的 2FA 代码比较。不匹配会被视为登录失败，但向用户显示的是同一条统一消息「账户数据错误。」。

#### 恢复访问（recovery）

3X-UI 中**没有**单独的「恢复代码」机制。如果丢失了对认证应用的访问，无法通过面板界面恢复登录。唯一的办法是直接在服务器的数据库中关闭 2FA：将设置表中的 `twoFactorEnable` 键重置为 `false`（必要时清空 `twoFactorToken`），之后重启面板。因此建议在启用 2FA 时把密钥（Base32 令牌）保存在安全的地方。

**示例：在服务器上紧急关闭 2FA。** 通过 SSH 获取服务器访问权限后，停止面板，重置设置表中的键，然后再次启动面板：

```bash
x-ui stop
sqlite3 /etc/x-ui/x-ui.db "UPDATE settings SET value='false' WHERE key='twoFactorEnable';"
sqlite3 /etc/x-ui/x-ui.db "UPDATE settings SET value='' WHERE key='twoFactorToken';"
x-ui start
```

此后只需用登录名和密码即可登录，如有需要可重新配置 2FA。

> 与修改凭据的关联：修改登录名/密码时（见 2.4），服务器上的 2FA 会**自动关闭**，以免旧密钥阻挡新账户下的访问。

### 2.3. 登录尝试限制（login limiter / 暴力破解防护）

面板内置了失败登录限制器（相当于应用层面的 fail2ban）。参数在代码中设定，**无法**通过界面配置：

| 参数 | 值 | 用途 |
|----------|----------|------------|
| 最大失败次数 | **5** | 在窗口期内允许多少次失败尝试。 |
| 计数窗口 | **5 分钟** | 累计失败次数的滑动窗口（更早的会被丢弃）。 |
| 封锁（cooldown） | **15 分钟** | 超过阈值后该键被封锁多长时间。 |

工作原理：

- 封锁键由 **「IP + 登录名」组合**构成（登录名转为小写，去除空格）。也就是说，封锁针对具体的「地址 + 用户名」一对，而非整个面板。
- 每次失败尝试（登录名/密码错误或 2FA 代码错误）都会使计数器增长。在 **5 分钟**内达到 **5** 次失败后，该键被封锁 **15 分钟**。封锁期间，该对的任何尝试都会被以同样的消息「账户数据错误。」立即拒绝，即使数据正确。
- **成功登录会立即重置**计数器并解除该对的封锁。
- 客户端 IP 地址在考虑可信代理（见 `trustedProxyCIDRs`）的情况下确定：仅当请求来自可信地址时才接受 `X-Real-IP` 和 `X-Forwarded-For` 头。否则使用连接的真实地址，若无法获取则使用字符串 `unknown`。

所有尝试都会被记录。对于失败的尝试，会在服务器日志中写入一条警告，包含用户名、IP、原因，以及封锁时的 `blocked_until` 时间。如果启用了通过 Telegram 机器人的登录通知（`tgNotifyLogin` ——「登录通知」），管理员还会额外收到成功、失败和被封锁尝试的用户名、IP 和时间。

**示例：Telegram 登录通知。** 启用 `tgNotifyLogin` 后，每次尝试之后管理员会收到大致如下的消息：

```
Уведомление о входе
Пользователь: admin
IP: 203.0.113.45
Время: 2026-06-10 14:32:07
Статус: успешно
```

对于被封锁的「IP + 登录名」对，状态中会指明该尝试已被限制器拒绝。

### 2.4. 修改管理员登录名和密码

**Настройки → Учетная запись** 部分的 **«Учетные данные администратора»** 选项卡。字段：

| 字段 | 文本（RU） | 说明 |
|------|------------|----------|
| 当前登录名 | «Текущий логин» | 现行用户名。必须与当前登录名一致，否则更改会被拒绝。 |
| 当前密码 | «Текущий пароль» | 用于确认身份的现行密码。 |
| 新登录名 | «Новый логин» | 新用户名。不能为空。 |
| 新密码 | «Новый пароль» | 新密码。不能为空。 |

更改通过按钮 **«Подтвердить»** 应用，并提交至 `POST /panel/setting/updateUser`。

服务器逻辑与消息：

- 如果「当前登录名」与实际不符或「当前密码」错误——「修改管理员凭据时发生错误。」并附说明「用户名或密码错误」。
- 如果新登录名或新密码为空——说明「新用户名和新密码必须填写」。
- 成功时——「您已成功修改管理员凭据。」。密码以 bcrypt 哈希形式存储。

**示例：通过 API 修改凭据。** 该请求需要有效的会话 cookie（登录时获得）以及对当前登录名/密码的确认：

```bash
curl -X POST https://panel.example.com:2053/мой-секрет/panel/setting/updateUser \
  -b 'session=ВАША_СЕССИОННАЯ_COOKIE' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'oldUsername=admin&oldPassword=СтарыйПароль&newUsername=root&newPassword=НовыйСложныйПароль'
```

成功后当前会话会失效——需要用新数据重新登录。

修改凭据的重要影响：

- **所有现有会话都会失效**（用户的 `login_epoch` 计数器递增），因此修改后面板会自动退出登录并重定向到登录页面——需要重新登录。
- 如果修改时启用了 **2FA，它会自动关闭**（标志和密钥被重置）。修改登录名/密码后需要重新配置双因素认证。

如果启用了 2FA，在提交表单之前会打开「修改凭据」窗口，并附带提示「输入应用中的代码以修改管理员凭据。」——只有确认当前 2FA 代码后才能修改凭据。

### 2.5. 密钥路径（URI 路径 / webBasePath）和面板端口

这些参数位于 **Настройки → Панель** 部分，直接影响面板的「隐蔽性」和可达性。在保存并**重启面板**后生效。

| 字段 | 文本（RU） | 默认值 | 说明 |
|------|------------|-----------------------|----------|
| 面板端口 | «Порт панели»（`panelPort`），提示「面板运行的端口」 | **2053** | Web 界面的 TCP 端口。 |
| URI 路径 | «URI-путь»（`panelUrlPath`），提示「必须以 '/' 开头并以 '/' 结尾」 | **/** | 密钥基础路径（`webBasePath`）。面板只能通过它访问（例如 `/мой-секрет/`）。 |
| 面板管理 IP 地址 | «IP-адрес для управления панелью»（`panelListeningIP`），提示「留空以允许任意 IP 连接」 | 空 | 面板监听的地址。空 = 所有接口。 |
| 面板域名 | «Домен панели»（`panelListeningDomain`），提示「留空以允许任意域名和 IP 连接。」 | 空 | 按域名（Host）限制访问。 |
| 面板证书公钥路径 | `publicKeyPath`，提示「输入以 '/' 开头的完整路径」 | 空 | 用于 HTTPS 访问面板的 TLS 证书。 |
| 面板证书私钥路径 | `privateKeyPath`，相同提示 | 空 | TLS 私钥。 |

基础路径（`webBasePath`）的行为：

- 该值会被自动规范化：如果不以 `/` 开头，则在开头添加该字符；如果不以 `/` 结尾，则在末尾添加。也就是说路径实际上总是 `/…/` 形式。
- 基础路径应用于面板本身、资源以及会话 cookie（cookie 仅针对该路径下发）。

> 安全建议（「安全警告」部分）：如果配置「过于公开」，面板会自行显示警告：
> - 「面板通过普通 HTTP 运行——请为生产环境配置 TLS。」
> - 「标准端口 2053 广为人知——请改为一个随机端口。」
> - 「默认基础路径 "/" 广为人知——请改为一个随机路径。」
>
> 换言之，对于生产服务器应当设置**非标准端口**、**非平凡的 URI 路径**以及 **TLS 证书**。

**示例：生产环境的「隐蔽」面板配置。** 在 **Настройки → Панель** 部分设置大致如下的值：

| 字段 | 值 |
|------|----------|
| 面板端口 | `34571`（随机，替代 2053） |
| URI 路径 | `/aXf9Qm2/`（非平凡，以 `/` 开头和结尾） |
| 面板证书公钥路径 | `/etc/letsencrypt/live/panel.example.com/fullchain.pem` |
| 面板证书私钥路径 | `/etc/letsencrypt/live/panel.example.com/privkey.pem` |

保存并重启后，面板将只能通过 `https://panel.example.com:34571/aXf9Qm2/` 访问，而安全警告会消失。

### 2.6. 会话生存时间（超时）

字段 **«Продолжительность сессии»**（`sessionMaxAge`）位于面板/间隔设置之中。

| 字段 | 文本（RU） | 默认值 | 单位 | 说明 |
|------|------------|-----------------------|---------|----------|
| 会话时长 | «Продолжительность сессии»，提示「系统中的会话时长（值：分钟）」 | **360** | 分钟 | 管理员会话 cookie 的生存时间。 |

行为：

- 该值以**分钟**为单位设定（默认 360 分钟 = 6 小时），在设置 cookie 时换算为秒。
- 如果该值**大于 0**，会话 cookie 会被设置相应的 `MaxAge`。超过该期限后 cookie 失效，下一次请求时用户会收到「会话已过期。请重新登录」。
- 会话也会在修改凭据或首次启用 2FA 时提前失效（通过 `login_epoch` 机制，见 2.4 和 2.2），以及在显式退出（`POST /logout`）时失效。
- 会话 cookie 标记为 `HttpOnly`，策略为 `SameSite=Lax`；在直接通过 HTTPS 访问面板时会设置 `Secure` 标志。

除超时本身外，还有一个相关通知：**«Задержка уведомления об истечении сессии»**（`expireTimeDiff`，提示「在达到阈值之前收到会话过期通知（值：天）」，默认 `0`）——可以提前收到警告。

### 2.7. LDAP（同步与认证）

LDAP 部分提供两项功能：(1) 当本地密码不匹配时通过 LDAP 认证管理员登录；(2) 定期从目录同步客户端状态（VLESS 标志的启用/禁用）。

登录时如何使用：服务器先校验本地的 bcrypt 密码哈希。如果它**不匹配**且 LDAP 已启用，面板会尝试在目录中认证用户：在设定了 `Bind DN` 的情况下执行一次服务性 bind，然后按过滤器和属性查找用户记录，并尝试用输入的密码以找到的 DN 进行 bind。成功即表示登录。（LDAP 认证成功后，如果启用了 2FA，仍会校验 TOTP 代码。）

部分字段：

| 字段 | 文本（RU） | 默认值 | 说明 |
|------|------------|-----------------------|----------|
| 启用 LDAP 同步 | «Включить LDAP-синхронизацию»（`enable`） | **false** | LDAP 集成的主开关。 |
| LDAP 主机 | «LDAP-хост»（`host`） | 空 | LDAP 服务器地址。 |
| LDAP 端口 | «Порт LDAP»（`port`） | **389** | 端口。LDAPS 通常为 636。 |
| 使用 TLS（LDAPS） | «Использовать TLS (LDAPS)»（`useTls`） | **false** | 启用后使用 `ldaps://` 方案并校验服务器证书（不跳过校验）。 |
| Bind DN | «Bind DN»（`bindDn`） | 空 | 用于首次 bind/查找的服务账户 DN。若为空——不执行 bind（匿名查找）。 |
| Bind 密码 | 提示：「已配置；留空以保留当前密码。」/「未配置。」/「已配置——输入新值以替换」 | 空 | `Bind DN` 的密码。单独存储；如需保留原值，将该字段留空。 |
| Base DN | «Base DN»（`baseDn`） | 空 | 进行查找的子树根（递归查找，遍历整个子树）。 |
| 用户过滤器 | «Фильтр пользователя»（`userFilter`） | `(objectClass=person)` | 选取账户的 LDAP 过滤器。认证时登录名会经转义后代入过滤器。 |
| 用户属性（username/email） | «Атрибут пользователя (username/email)»（`userAttr`） | `mail` | 与客户端的登录名/标识符相匹配的属性（例如 `mail` 或 `uid`）。 |
| VLESS 标志属性 | «Атрибут VLESS-флага»（`vlessField`） | `vless_enabled` | 决定客户端 VLESS 访问是否应启用的属性。 |
| 通用标志属性（可选） | «Общий атрибут флага (опц.)»（`flagField`），提示「若设置，将覆盖 VLESS 标志——例如 shadowInactive。」 | 空 | 若设置，则代替 `vless_enabled` 使用。 |
| Truthy 值 | «Truthy-значения»（`truthyValues`），提示「以逗号分隔；默认：true,1,yes,on」 | `true,1,yes,on` | 标志属性中被视为「已启用」的值列表。 |
| 反转标志 | «Инвертировать флаг»（`invertFlag`），提示「当属性表示『已禁用』时启用（例如 shadowInactive）。」 | **false** | 反转标志的含义。 |
| 同步计划 | «Расписание синхронизации»（`syncSchedule`），提示「类 cron 字符串，例如 @every 1m」 | `@every 1m` | 以类 cron 格式表示的同步周期。 |
| inbound 标签 | «Теги входящих»（`inboundTags`），提示「LDAP 同步可在其上自动创建或自动删除客户端的 inbound。」 | 空 | 限定在哪些 inbound 上允许自动操作。如果没有 inbound：「未找到 inbound。请先创建一个 inbound。」 |
| 自动创建客户端 | «Авто-создание клиентов»（`autoCreate`） | **false** | 当客户端出现在目录中时，在指定的 inbound 中创建该客户端。 |
| 自动删除客户端 | «Авто-удаление клиентов»（`autoDelete`） | **false** | 当客户端从目录中消失时删除该客户端。 |
| 默认流量（GB） | «Объём по умолчанию (ГБ)»（`defaultTotalGb`） | **0** | 自动创建客户端的流量限制（0 = 无限制）。 |
| 默认期限（天） | «Срок по умолчанию (дни)»（`defaultExpiryDays`） | **0** | 自动创建客户端的有效期（0 = 永久）。 |
| 默认 IP 限制 | «Лимит IP по умолчанию»（`defaultIpLimit`） | **0** | 同时在线 IP 数量限制（0 = 无限制）。 |

同步标志逻辑的特点：读取标志属性（`flagField`，默认 `vless_enabled`）时，若其值在 truthy 值列表中则视为「已启用」；启用反转后结果取反。用户属性（`userAttr`）用作匹配键（email/名称）——没有该属性值的记录会被跳过。

> 安全：建议启用 **TLS（LDAPS）**，以免 bind 密码和被校验的密码以明文传输；并为 `Bind DN` 使用一个仅具备最低必要读取权限的账户。

**示例：典型的 LDAP 同步配置（Active Directory）。** 针对某个目录填写本部分字段，该目录的访问状态保存在一个类似 `userAccountControl` 的标志属性中，匹配按邮箱进行：

| 字段 | 值 |
|------|----------|
| LDAP 主机 | `ldap.example.com` |
| LDAP 端口 | `636` |
| 使用 TLS（LDAPS） | 已启用 |
| Bind DN | `CN=svc-3xui,OU=Service,DC=example,DC=com` |
| Base DN | `OU=Users,DC=example,DC=com` |
| 用户过滤器 | `(objectClass=person)` |
| 用户属性（username/email） | `mail` |
| VLESS 标志属性 | `vless_enabled` |
| Truthy 值 | `true,1,yes,on` |
| 同步计划 | `@every 5m` |

在这种配置下，面板每 5 分钟遍历一次 `OU=Users` 子树，按 `mail` 匹配客户端，并根据 `vless_enabled` 的值启用/关闭 VLESS 访问。

---

## 3. 概览 / 仪表盘

仪表盘（「仪表盘」，英文界面中为 *Overview*）是面板的起始页面。它实时显示服务器和 Xray 进程的状态。所有指标均来自服务器端。后台调度器**每 2 秒**重新生成一次快照，并通过 WebSocket 将其推送到所有打开的标签页；每分钟一次，累积的指标序列会落盘到磁盘。HTTP 端点 `GET /status` 返回最近一次缓存的快照。

下面将逐一说明页面上的每一项指标和每一个控件。

### 3.1. 数据采集的总体原则

- 快照由 `gopsutil` 库采集。如果某项具体采集失败，对应字段保持为零，并在日志中写入一条警告（`get cpu percent failed`、`get uptime failed` 等等）——这不会导致整个仪表盘失效，只是相应的方块会显示 0/N-A。
- 「瞬时」速率（CPU %、网络、磁盘 I/O）是按当前快照与前一快照之差除以以秒为单位的间隔计算得出的。因此在页面首次加载时，速率值可能为零，直到累积出第二次采集。
- 历史数据可在「系统历史」（*System History*）部分查看——图表依据的正是下文所述的那些数据序列（见 3.12 节）。

### 3.2. CPU（CPU）

「CPU」（*CPU*）方块以百分比显示当前处理器的负载，以及处理器本身的参数。

| 指标 | 说明 |
|---|---|
| CPU 负载，% | 最近一个间隔内处理器忙碌时间所占的比例。通过指数移动平均（EMA，系数 `alpha = 0.3`）进行平滑，以免突发波动使指示器抖动。该值始终被钳制在 0–100 % 区间内。在最初的第一次采集时返回 0（基准点初始化）。 |
| 逻辑处理器 | 逻辑核心的数量——即计入了 Hyper-Threading。 |
| 物理核心 | 物理核心的数量。 |
| 频率 | 处理器的基准频率，单位 MHz。该值采用惰性请求并缓存：首次成功采集会被保存下来，重试不会比每 5 分钟一次更频繁，且请求本身受 1.5 秒超时限制（在某些系统上频率查询响应较慢）。 |

CPU 负载在算法上的计算方式如下：如果存在原生的平台实现，则使用它，否则按处理器时间计数器的增量（busy / total）计算。Guest 时间和 GuestNice 时间被排除在外，以免重复计入。

### 3.3. 内存（RAM）

「内存」（*RAM*）方块显示已用和总量。以「已用 / 总量」和/或填充百分比的形式显示。历史中记录的是百分比。

### 3.4. 交换分区（Swap）

「交换分区」（*Swap*）方块显示已用和总量。如果未配置交换文件/分区（总量 = 0），则该指标为零；在没有 swap 时，历史序列中写入 0。

### 3.5. 磁盘（Storage）

「磁盘」（*Storage*）方块显示已用和总量，其中**仅统计根分区 `/`**。「磁盘使用率」（*Disk Usage*）历史中写入填充百分比。磁盘输入输出（读取 / 写入，字节/秒）作为计数器在该间隔内的增量单独采集——它显示在历史的「磁盘 I/O」标签页上。

### 3.6. 系统运行时间（Uptime）

「系统运行时间」（*Uptime*）指标。这是自**整个服务器**启动以来的时间（以秒为单位），而不是面板或 Xray 的运行时间。Xray 进程的运行时间单独保存（见 3.9 节），此外还有面板的线程数（译为「线程」/ *Threads*）。

### 3.7. 系统负载（Load average）

「系统负载」（*System Load*）块——由三个数字组成的数组 `[Load1, Load5, Load15]`。提示文字：「系统在过去 1、5 和 15 分钟内的平均负载」（*System load average for the past 1, 5, and 15 minutes*）。历史图表名为「系统平均负载（1 / 5 / 15 分钟）」。在历史序列中各值分别写入：`load1`、`load5`、`load15`。

这是标准的 Unix 指标：处于执行队列中的进程的平均数量。参考标准——与核心数相比较：负载若持续超过物理核心数，则表明过载。

### 3.8. 网络：速率和总流量

**仅统计物理接口**。虚拟接口和隧道接口被排除在外：包括 `lo`/`lo0`，以及所有以 `loopback`、`docker`、`br-`、`veth`、`virbr`、`tun`、`tap`、`wg`、`tailscale`、`zt` 开头的接口。各值在所有剩余接口上求和。

**总速率**（*Overall Speed*）——瞬时速率，即计数器在该间隔内的增量：

| 指标 | 说明 |
|---|---|
| 上传 / 发送（标注为「上传」/ *Upload*） | 出站速率，字节/秒。 |
| 下载 / 接收（标注为「下载」/ *Download*） | 入站速率，字节/秒。 |

**总流量**（*Total Data*）——自系统启动以来累积的计数器：

| 指标 | 说明 |
|---|---|
| 已发送（标注为「已发送」/ *Sent*） | 已发送的字节总量。 |
| 已接收（标注为「已接收」/ *Received*） | 已接收的字节总量。 |

此外还会采集数据包速率（包/秒）和数据包总计数器——它们显示在历史的「网络数据包」（*Network Packets*）标签页上。网络的历史序列：`netUp`、`netDown`、`pktUp`、`pktDown`。

### 3.9. 服务器 IP 地址

「服务器 IP 地址」（*IP Addresses*）块显示 `IPv4` 和 `IPv6`。外部地址通过第三方服务确定（IPv4 用 `api4.ipify.org`、`ipv4.icanhazip.com`、`v4.api.ipinfo.io/ip`、`ipv4.myexternalip.com/raw`、`4.ident.me`、`check-host.net/ip`，IPv6 用类似的服务）。列表会逐个尝试，直到收到第一个成功的响应；每个请求的超时为 3 秒。

特性：
- 结果在进程生命周期内**被缓存**：已成功确定的地址不会被重复请求。
- 如果没有任何服务作出响应，字段中保留 `N/A`。对于 IPv6，在首次出现 `N/A` 时会完全禁用 IPv6 请求，以免在没有 IPv6 的网络上浪费时间。
- 旁边有一个「眼睛」按钮用于隐藏/显示地址——提示为「隐藏或显示服务器 IP 地址」（*Toggle visibility of the IP*）。这只是界面中的视觉隐藏（例如用于截图），不会影响地址本身。

### 3.10. TCP/UDP 连接

「连接数」（*Connection Stats*）块显示服务器上活跃的 TCP 和 UDP 连接总数（针对整个系统，而不仅是 Xray）。历史图表为「活跃连接（TCP / UDP）」（*Active Connections*），序列为 `tcpCount`、`udpCount`。

### 3.11. Xray 状态与进程管理

「Xray」卡片显示 Xray-core 进程的状态，并允许对其进行管理。

#### 状态

| 值 | 标注 | 译文 | 何时设置 |
|---|---|---|---|
| `running` | 「已启动」 | *Running* | Xray 进程已启动。 |
| `stop` | 「已停止」 | *Stopped* | 进程未启动，且没有记录到启动错误。 |
| `error` | 「错误」 | *Error* | 进程未启动，但记录到了启动错误。错误文本显示在标题为「运行 Xray 时发生错误」（*An error occurred while running Xray*）的弹窗中。 |
| — | 「未知」 | *Unknown* | 在尚未获取到状态时显示。 |

状态旁边会显示 **Xray 版本**。

#### 控制按钮

- **停止**（*Stop*）。调用 `POST /stopXrayService`。成功时面板会通过 WebSocket 推送新状态 `stop` 以及通知「Xray 已成功停止」（*Xray service has been stopped*），失败时——推送带文本的 `error` 状态。注意：如果面板是*通过* Xray 本身访问的，停止 Xray 可能会中断与面板的连接——直接连接面板则不存在该问题。
- **重启**（*Restart*）。调用 `POST /restartXrayService`。操作前会显示确认「重启 xray？」并附说明「以已保存的配置重新加载 xray 服务」。成功时——`running` 状态以及通知「Xray 已成功重启」（*Xray service has been restarted successfully*）。重启会应用当前已保存的配置——请在更改设置后使用它。

> 注意。在本分支中，仪表盘为所有授权类型添加了完整的 Start / Stop / Restart 管理；在 3x-ui 的原始 UI 中没有单独的「启动」按钮——启动是通过重启来执行的。

#### 查看 Xray 日志按钮

Xray 卡片上有一个查看 Xray 日志的按钮（*Logs*）。它只在 Xray 配置中设置了 access 日志时才会出现：内置查看器读取的正是该文件，因此没有 access 日志时按钮会被隐藏。按钮的可见性绑定到独立的标志 `accessLogEnable`，不再依赖于 IP 限制——在线列表和 IP 地址限制即使在没有 access 日志的情况下也能继续工作（见 8 节）。

#### Xray 版本选择

「版本选择」（*Version*）部分允许将 Xray-core 切换到另一个发行版。版本列表通过 `GET /getXrayVersion` 加载：

- 来源是 `XTLS/Xray-core` 仓库的 GitHub API（`/releases`）。请求会缓存 **15 分钟**；当 GitHub 出现故障时会返回最近一次成功获取的列表，以免选择器变空。
- 列表中只会包含形如 `X.Y.Z` 且**不早于 26.4.25** 的发行版。

提示：「选择您想要切换到的版本」（*Choose the version you want to switch to.*）以及警告「重要：旧版本可能不支持当前设置」（*Choose carefully, as older versions may not be compatible with current configurations.*）。

切换：`POST /installXray/:version`。流程：

**示例。** 切换到 Xray-core 的特定版本（会话 cookie 必须已通过授权获取）：

```bash
curl -X POST 'https://panel.example.com:2053/xpanel/installXray/v25.6.8' \
  -b cookie.txt
```

这里的 `v25.6.8` 是 `GET /getXrayVersion` 返回的列表中的一个标签。版本必须存在于该列表中，否则面板会返回拒绝。
1. 所选版本会校验是否存在于最新的发行版列表中（否则——拒绝）。
2. Xray 被停止。
3. 针对当前操作系统和架构，从 GitHub 下载压缩包 `Xray-<os>-<arch>.zip`（支持 amd64/64、arm64-v8a、arm32-v7a/v6/v5、386/32、s390x；对于 Windows 为 `xray.exe`）。压缩包和二进制文件的大小限制为 200 MB。
4. 二进制文件以原子方式替换（通过临时文件 + 重命名）并被标记为可执行。
5. Xray 重新启动。

切换前会显示对话框「切换 Xray 版本」（*Do you really want to change the Xray version?*），附说明「这将把 Xray 版本更改为 #version#」。成功时——通知「Xray 已成功更新」（*Xray updated successfully*）。

### 3.12. 面板更新（3X-UI）

面板更新检查块。数据通过 `GET /getPanelUpdateInfo` 获取：

| 字段 | 说明 |
|---|---|
| 当前面板版本 | 已安装面板的版本。 |
| 最新面板版本 | 从 GitHub 获取的 3x-ui 的最新发行版。 |
| 有可用更新 | 表示最新版本比当前版本更新的标志。如果不需要更新——则显示「面板已是最新」/「已是最新」。 |

**「更新面板」**（*Update Panel*）按钮会启动 `POST /updatePanel`。提示：「这将把 3X-UI 更新到最新发行版并重启面板服务」。启动前——确认「您确定要更新面板吗？」并附文本「这将把 3X-UI 更新到版本 #version# 并重启面板服务」。

特性和限制：
- 自更新**仅在 Linux 上**受支持（在其他操作系统上会返回错误）。
- 更新脚本从官方仓库下载（`raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh`，限制 2 MB）并通过 `bash` 运行，尽可能通过 `systemd-run` 隔离执行。
- 成功启动时显示「面板更新已开始」（*Panel update started*）；如果更新检查失败——「面板更新检查失败」。安装期间会显示警告「正在安装。请勿刷新页面」。

### 3.13. 地理文件更新（GeoIP / GeoSite）

地理库更新按钮/对话框会调用 `POST /updateGeofile`（所有文件）或 `POST /updateGeofile/:fileName`（单个文件）。更新依据严格的名称和来源白名单工作：

| 文件 | 来源 |
|---|---|
| `geoip.dat`、`geosite.dat` | `Loyalsoldier/v2ray-rules-dat`（latest） |
| `geoip_IR.dat`、`geosite_IR.dat` | `chocolate4u/Iran-v2ray-rules`（latest） |
| `geoip_RU.dat`、`geosite_RU.dat` | `runetfreedom/russia-v2ray-rules-dat`（latest） |

行为：
- 文件名会被校验：禁止 `..`、斜杠、绝对路径；只允许 `[a-zA-Z0-9._-]+.dat`。白名单之外的文件不会被下载。
- 使用条件请求 `If-Modified-Since`：如果源服务器上的文件未发生变化（HTTP 304），则不会重新下载，仅更新时间戳。
- 下载完成后 Xray **会重启**（以便加载新的库）。

**示例。** 仅更新俄罗斯的地理库，不触碰其他文件：

```bash
curl -X POST 'https://panel.example.com:2053/xpanel/updateGeofile/geoip_RU.dat' -b cookie.txt
curl -X POST 'https://panel.example.com:2053/xpanel/updateGeofile/geosite_RU.dat' -b cookie.txt
```

要一次性更新白名单中的所有文件——请调用不带文件名的 `POST /updateGeofile`。
- 对话框：单个文件为「您确定要更新地理文件吗？」附「这将更新文件 #filename#」，「更新全部」按钮为「这将更新所有地理文件」。成功——「地理文件已成功更新」。

### 3.14. 数据库备份与恢复

「备份与恢复」（*Backup & Restore*）块。其行为取决于所使用的数据库管理系统（默认 SQLite 或 PostgreSQL）。

#### 导出数据库（备份）

「导出数据库」/「备份」（*Back Up*）按钮会调用 `GET /getDb`。文件以附件形式返回：
- **SQLite**：先执行 checkpoint（刷新 WAL），然后下载文件 `x-ui.db`。提示：「点击以下载包含您当前数据库备份的 .db 文件……」。
- **PostgreSQL**：以自定义格式下载转储 `x-ui.dump`（`pg_dump --format=custom --no-owner --no-privileges`）。服务器上必须安装 PostgreSQL 客户端工具；否则——会报缺少 `pg_dump` 的错误。

#### 导入数据库（恢复）

「导入数据库」/「恢复」（*Restore*）按钮通过 `POST /importDB`（表单字段 `db`）上传文件。提示：「点击以选择并上传 .db 文件……，以从备份恢复数据库」。

**SQLite** 的流程是安全的，带有回滚：
1. 文件会被校验是否为 SQLite 格式并保存到临时文件，然后校验完整性。
2. Xray 被停止，当前数据库被关闭并重命名为 `*.backup`（回退）。
3. 新文件就位为工作数据库，执行初始化和迁移。如果出现问题——则恢复回退文件。
4. Xray 重新启动。

对于 **PostgreSQL**，上传 `.dump`（校验签名 `PGDMP`）并通过 `pg_restore --clean --if-exists --single-transaction …` 应用。提示直接警告：「这将替换所有当前数据」。

消息：「数据库已成功导入」、「导入数据库时发生错误」、「……在读取数据库时」、「……在获取数据库时」。

#### 迁移文件（SQLite 与 PostgreSQL 之间）

「下载迁移文件」（*Download Migration*）按钮会调用 `GET /getMigration`，并生成可移植的导出，用于在另一种数据库管理系统上运行面板：
- 在 **SQLite** 上下载 `x-ui.dump`（文本 SQL 转储）。
- 在 **PostgreSQL** 上下载 `x-ui.db`——一个由 PostgreSQL 数据汇集而成的现成 SQLite 数据库。

### 3.15. 其他界面元素

- **在线客户端指示器。** 仪表盘维护一个 `online` 序列（*Online Clients* /「客户端在线」）——具有活跃连接的客户端数量。在 Xray 运行时计算（否则为 0），并以相同的 2 秒节拍记入历史。图表——「在线」标签页。
- **系统历史（图表）。** 「图表」按钮/部分 →「系统历史」，包含以下标签页：「带宽」、「数据包」、「磁盘 I/O」、「在线」、「负载」、「连接」、「磁盘使用率」。数据通过 `GET /history/:metric/:bucket` 拉取；允许的聚合间隔（bucket，秒）：**2、30、60、120、180、300、720、1440、2880**（后三个对应间隔选择器中的 **12h**、**24h** 和 **48h** 预设），每个标签页最多接收 60 个数据点。指标环形缓冲区保存最长 **48 小时**的数据，因此图表（CPU、RAM、流量、数据包、连接、磁盘、在线、负载）可查看长达两昼夜的时段。允许的指标：`cpu, mem, swap, netUp, netDown, pktUp, pktDown, diskRead, diskWrite, diskUsage, tcpCount, udpCount, online, load1, load5, load15`。标注「最近 2 分钟」对应 bucket = 2（实时模式）。

**示例。** 获取最近约 2 分钟的 CPU 负载序列（bucket = 2 秒，最多 60 个数据点）以及按 5 分钟聚合的同一序列（bucket = 300 秒）：

  ```bash
  curl 'https://panel.example.com:2053/xpanel/history/cpu/2' -b cookie.txt
  curl 'https://panel.example.com:2053/xpanel/history/cpu/300' -b cookie.txt
  ```

  指标可替换为任何允许的值（`mem`、`netUp`、`tcpCount`、`load1` 等等）。不在列表 `2, 30, 60, 120, 180, 300, 720, 1440, 2880` 之内的 bucket 将被拒绝。
- **Xray 指标**——一个单独的块，展示 Xray 的内存消耗和垃圾回收（序列 `xrAlloc, xrSys, xrHeapObjects, xrNumGC, xrPauseNs`）以及「观察台」（出站连接的状态）。仅当 Xray 配置中设置了 `metrics` 块（`listen 127.0.0.1:11111`，标签 `metrics_out`）时才工作；否则会显示「Xray 指标端点未配置」。

**示例**：用于启用 Xray 指标方块的块。在 Xray 设置部分必须同时存在 `metrics`（带标签）和一个监听该标签的 inbound：

  ```json
  {
    "metrics": {
      "tag": "metrics_out"
    },
    "inbounds": [
      {
        "listen": "127.0.0.1",
        "port": 11111,
        "protocol": "dokodemo-door",
        "settings": { "address": "127.0.0.1" },
        "tag": "metrics_out"
      }
    ]
  }
  ```

  地址 `127.0.0.1:11111` 是有意不对外暴露的——面板在本地对其进行轮询。
- **深色主题切换器。** 位于通用菜单/页头中，而不是在仪表盘本身。选项：「主题」（*Theme*），可选「深色」和「极深色」（*Ultra Dark*）。这纯粹是外观显示设置，不影响面板的工作。
- **其他链接**，位于仪表盘周围（来自菜单/底部栏）：「日志」、「配置」——查看 Xray 的最终 JSON（`GET /getConfigJson`）、「文档」。

---

## 4. Inbounds：创建与通用参数

**「入站」**（英文 *Inbounds*）一节是 Xray 所有入口点的列表，客户端通过这些入口点进行连接。每个 inbound 既保存「面板」字段（备注、流量限额、重置计划），也保存 Xray 配置的原始 JSON 块（`settings`、`streamSettings`、`sniffing`）。

创建通过**「创建连接」**（*Add Inbound*）按钮完成，编辑通过**「修改连接」**（*Modify Inbound*）按钮完成。两个操作分别发送到 API 端点 `POST /add` 和 `POST /update/:id`。

下面讲解表单中**不**属于具体协议设置（客户端、加密、REALITY/TLS）、也**不**属于传输/流（**「流」**、**「安全」**选项卡）的所有字段——这些是其他章节的主题。

### 4.1. 表单通用字段

#### Remark（备注）

| 参数 | 值 |
|---|---|
| 字段 | `remark` |
| 类型 | 字符串 |
| 默认 | 空 |

inbound 的可读名称，显示在列表中和对话框标题里（「删除连接 "{remark}"？」等）。字段标签为**「备注」**。它不影响 Xray 的运行，仅用于方便管理；建议设置唯一且有意义的名称，因为它们会被填入导出文件的名称以及批量操作的确认信息中。

#### Protocol（协议）

| 参数 | 值 |
|---|---|
| 字段 | `protocol` |
| 标签 | **「协议」** |
| 校验 | `required,oneof=vmess vless trojan shadowsocks wireguard hysteria http mixed tunnel tun` |

inbound 协议的下拉列表。允许的值：

| 值 | 备注 |
|---|---|
| `vmess` | |
| `vless` | |
| `trojan` | |
| `shadowsocks` | |
| `wireguard` | |
| `hysteria` | Hysteria v2 即带 `streamSettings.version = 2` 的 `hysteria`，没有单独的协议 |
| `http` | |
| `mixed` | 同一端口上的 socks/http |
| `tunnel` | |
| `tun` | 校验器接受，但没有单独的协议常量 |

该字段为必填（`required`）。协议的选择决定了哪些客户端设置字段以及哪种传输可用（见各协议专属章节）。

> 重要：保存时服务会对 `streamSettings` 进行规范化。传输设置仅对 `vmess`、`vless`、`trojan`、`shadowsocks`、`hysteria` 协议保留；对其余协议（`http`、`mixed`、`tunnel`、`wireguard`、`tun`），`streamSettings` 字段会被**强制清空**。

对于 `tunnel`/TProxy 类型的 inbound，如果其 `streamSettings` 块不含 `security` 键（无传输变体），表单可以正常打开和保存，不会出现 `streamSettings.security Invalid input` 校验错误。

#### Listen IP（监听 IP）

| 参数 | 值 |
|---|---|
| 字段 | `listen` |
| 类型 | 字符串 |
| 默认 | 空 → Xray 监听 `0.0.0.0`（所有 IP） |

inbound 接收连接的 IP 地址。字段提示：

> 「留空以监听所有 IP 地址」。

在生成 Xray 配置时，空值会被替换为 `0.0.0.0`。除 IP 外，该字段还接受 **Unix 套接字路径**——提示：

> 「也可以指定 Unix 套接字路径（例如 /run/xray/in.sock）或带 @ 前缀的抽象套接字名称（例如 @xray/in.sock），以监听套接字而非 TCP 端口——这种情况下请将端口设为 0」。

因此该字段接受两种 Unix 套接字形式：文件系统中的路径（`/run/xray/in.sock`）和带 `@` 前缀的抽象套接字名称（`@xray/in.sock`）。两种情况下都要把 `Port` 设为 `0`。

当需要把 inbound 限制在单个接口上时（例如把仅作为 Nginx 后端 fallback 目标的 inbound 设为 `127.0.0.1`），或当 inbound 监听 Unix 套接字时，才会修改此字段。

**示例。** 仅监听本地接口（典型的 Nginx 后端 fallback 目标）和 Unix 套接字的 inbound：

```
listen = 127.0.0.1   порт = 8443
listen = /run/xray/in.sock   порт = 0
```

#### Port（端口）

| 参数 | 值 |
|---|---|
| 字段 | `port` |
| 标签 | **「端口」** |
| 校验 | `gte=0,lte=65535` |
| 默认 | —（由用户设置） |

TCP/UDP 监听端口。允许的值从 `0` 到 `65535`。值 `0` 仅在配合监听 Unix 套接字时使用（见上文）。

保存时服务会检查端口冲突：两个 inbound 不能同时占用同一传输（TCP/UDP）上相互重叠的 `listen:port`。传输由协议和 `streamSettings`/`settings` 推算：例如 `hysteria` 和 `wireguard` 始终占用 UDP，`kcp`/`quic` 占用 UDP，而其余大多数占用 TCP。发生冲突时保存会被拒绝并报错。

此外，面板不允许占用**内部 Xray API 的保留端口**（标签 `api`，默认 `127.0.0.1` 上的 `62789`）：本地 TCP inbound 若其监听地址在 loopback 上与该端口重叠，会以同样的端口冲突错误被拒绝。API 的真实端口从 Xray 配置模板中读取（回退值为 `62789`）。在节点（nodes）上此限制不生效——它们有自己的 Xray。

> Xray 标签（`Tag`，唯一）会从端口和传输自动生成，格式为 `in-<端口>-<tcp|udp|tcpudp|any>`；对于部署在节点上的 inbound，会加上 `n<nodeId>-` 前缀。发生冲突时会向标签追加 `-2`、`-3` 等。用户通常不编辑标签。

#### Total traffic（总流量，GB）

| 参数 | 值 |
|---|---|
| 字段 | `total`（以**字节**计） |
| 标签 | **「总用量」** |
| 默认 | `0` |

inbound 的总流量限额。表单中以吉字节输入，数据库中以字节存储。字段提示：

> 「= 无限制。（单位：GB）」。

也就是说，**`0` 表示无限制**。这是整个 inbound 层级（而非单个客户端）的限额；实际已用流量保存在 `up`（已发送）和 `down`（已接收）字段中，并与 `total` 比较。

#### Expiry date / Duration（到期日期 / 时长）

| 参数 | 值 |
|---|---|
| 字段 | `expiryTime`（Unix 时间戳） |
| 标签 | **「到期日期」**（英文 *Duration*） |
| 默认 | 空 / `0` |

inbound 的有效期。提示：

> 「留空表示永久有效」。

空值（`0`）表示无期限的 inbound。该值以 Unix 时间戳存储；表单既允许设置具体日期，也允许设置以天为单位的时长（从当前时刻相对计算——英文字段标签 *Duration*）。

#### Enabled（启用）

| 参数 | 值 |
|---|---|
| 字段 | `enable` |
| 标签 | **「启用」**（英文 *Enabled*） |
| 默认 | 创建时设置 |

inbound 的活动状态标志。在列表中切换此标志由专门的「轻量」端点 `POST /setEnable/:id` 处理，而非完整更新——这样设计是为了避免在每次点击拥有上千客户端的 inbound 开关时都重新序列化整个 `settings` 块（所有客户端）。关闭 inbound 时会将其从运行中的 Xray 移除，启用时则重新加入。

#### Node / Deploy to（节点 / 部署到）

| 参数 | 值 |
|---|---|
| 字段 | `nodeId` |
| 标签 | **「部署到」**、**「本地面板」** |
| 默认 | 空（本地面板） |

选择 inbound 实际运行的位置：本地面板或某个已注册的节点。实现上的特点：`nodeId = 0` 会被规范化为 `nil`，因为 `0` 不是有效的节点 id，而是表单绑定的产物；`nil`/`0` 表示本地面板。在离线节点上保存 inbound 时可能出现提示「更改将在节点重新连接时同步」。

#### 分享链接的地址策略（Share address strategy）

| 参数 | 值 |
|---|---|
| 字段 | 策略 +（可选）自定义地址 |
| 标签 | **「分享链接的地址策略」**（英文 *Share address strategy*） |
| 默认 | **「inbound 监听地址」**（*Inbound listen*） |

下拉列表决定将哪个地址填入该 inbound 的**导出分享链接和二维码**。可选值：

| 值 | 标签 | 填入的内容 |
|---|---|---|
| `node` | **「节点地址」**（*Node address*） | inbound 所运行节点的地址 |
| `listen` | **「inbound 监听地址」**（*Inbound listen*） | inbound 自身的监听地址 |
| `custom` | **「自定义」**（*Custom*） | 来自**「分享链接自定义地址」**（*Custom share address*）字段的自定义地址 |

选择**「自定义」**时会出现**「分享链接自定义地址」**字段；在其中输入主机或 IP，**不含协议和端口**（该值会被校验）。**「节点地址」**选项仅当存在可运行该 inbound 的已启用节点时才显示在列表中；否则它会被隐藏，且取值回退为**「inbound 监听地址」**。

此策略**仅**影响直接的分享链接和二维码，**不**影响订阅的输出——那里的地址仍由面板的常规逻辑决定。

### 4.2. Sniffing（嗅探）

**「嗅探」**选项卡编辑 Xray 配置的 `sniffing` 块，该块以原始 JSON 存储。Sniffing 允许 Xray「窥探」连接内部的真实域名/协议，用于路由目的。

| 子字段 | 标签 | 用途 |
|---|---|---|
| `enabled` | （选项卡开关） | 为 inbound 开启/关闭嗅探 |
| `destOverride` | — | 要拦截目标地址的协议列表：`http`、`tls`、`quic`、`fakedns` |
| `metadataOnly` | **「仅元数据」** | 仅使用连接元数据，不读取有效负载 |
| `routeOnly` | **「仅路由」** | 嗅探结果仅用于路由，不重写目标地址 |
| `domainsExcluded` | **「排除的域名」** | 从嗅探中排除的域名 |
| （排除的 IP） | **「排除的 IP」** | 从嗅探中排除的 IP 地址 |

- **`destOverride`** —— 嗅探器集合：`http`（从 HTTP Host 头识别域名）、`tls`（从 SNI 识别）、`quic`（从 QUIC ClientHello 识别）、`fakedns`（与 FakeDNS 池匹配）。通常为识别域名会开启 `http` 和 `tls`。

**`sniffing` 块示例**（通过 HTTP 和 TLS 识别域名，结果仅用于路由，不触碰本地网络）：

```json
{
  "enabled": true,
  "destOverride": ["http", "tls"],
  "routeOnly": true,
  "domainsExcluded": ["courier.push.apple.com"]
}
```
- **`metadataOnly`** —— 开启时，Xray 不读取首个数据包的内容，仅依赖元数据；这有助于不破坏那些不能「窥探」数据的协议。
- **`routeOnly`** —— 嗅探结果仅供路由规则使用；此时 outbound 中的连接地址不会被重写为识别出的域名。

> 注意：面板将 `sniffing` 作为不透明的 JSON 块存储，保存时不向其添加任何内容——这些复选框的所有默认值都由客户端应用一侧生成。原始块可通过「入站 JSON」一节编辑（见下文）。

### 4.3. Allocate（端口分配策略）

`streamSettings` 中的 `allocate` 块控制 Xray 如何分配监听端口。这是 Xray 配置的一部分；面板将其作为 `streamSettings`/inbound JSON 的一部分存储和传递。参数（按 Xray-core 术语）：

| 子字段 | 用途 | 值 / 默认 |
|---|---|---|
| `strategy` | 端口分配策略 | `always` —— 始终监听指定端口（默认）；`random` —— 周期性在范围内变更监听端口 |
| `refresh` | `random` 时端口变更间隔（分钟） | 整数分钟（建议 5；最小为 2） |
| `concurrency` | `random` 时同时保持开放的端口数 | 整数（默认 3；不超过端口范围宽度的三分之一） |

`strategy: always` 让 inbound 固定在单个端口上（标准模式）。`strategy: random` 用于反封锁场景，此时 inbound 周期性在端口范围内「跳动」；这种情况下 `refresh` 和 `concurrency` 才有意义。只有在有意使用随机端口模式时才需要修改这些值。

**`streamSettings` 中的 `allocate` 块示例**（随机端口模式：保持 3 个端口开放，每 5 分钟变更一次）：

```json
{
  "allocate": {
    "strategy": "random",
    "refresh": 5,
    "concurrency": 3
  }
}
```

要使其生效，inbound 的 `port` 需设为一个范围（例如 `20000-20100`）。

### 4.4. External Proxy（外部代理）

**「External Proxy」**字段属于邀请链接生成的设置，存储在 inbound 的 `streamSettings` 中。它设置一组备用外部地址（主机/端口，必要时带强制 TLS——**「强制 TLS」**），这些地址会被填入客户端链接，替代 inbound 真实的 `listen:port`。

当客户端不应直接连接服务器、而要经由外部代理/反代/CDN 连接时使用：此时分享链接中填的是该前端的公网地址。这不影响 Xray 接收连接的过程——它只是生成链接的「外观修饰」。相关表单字段：**「强制 TLS」**、**「Fingerprint」**、每条记录的标签。

### 4.5. Fallbacks（Fallback）

**「Fallback」**一节设置对未匹配 inbound 任何客户端的连接进行转发的规则。仅对 TLS 传输上的主 inbound（VLESS/Trojan TCP-TLS）可用。通过端点 `GET /:id/fallbacks` / `POST /:id/fallbacks` 管理。

该节提示：

> 「当此入站上的连接未匹配任何客户端时，会被转发到别处。在下方选择一个子入站，路由字段（SNI / ALPN / Path / xver）将自动从其传输填入；或将选择留空并直接指定 Dest（例如 8080 或 127.0.0.1:8080），以转发到外部服务器，如 Nginx。每个子入站都应在 127.0.0.1 上以 security=none 监听」。

fallback 一节仅对基于 RAW（TCP）且安全为 TLS 或 REALITY 的 VLESS/Trojan inbound 显示。新建的 inbound 以 `security=none` 启动，因此该节起初可能看起来不存在。在此状态下（VLESS/Trojan、RAW/TCP、安全尚未配置），会显示一段内嵌提示代替该节：在**「安全」**选项卡选择 TLS 或 Reality 后，fallback 才会可用。

#### fallback 行的字段

| 字段 | 默认 | 描述 |
|---|---|---|
| （子 inbound） | — | 选择子 inbound（标签**「选择入站」**）。若已选择，Name/Alpn/Path/Dest 字段可从其传输自动填入 |
| Name | 空（= 任意） | 按名称（SNI/名称）的匹配条件。「任意」标签为**「任意」** |
| Alpn | 空 | 按 ALPN 的匹配条件 |
| Path | 空 | 按路径的匹配条件（用于子 inbound 的 WS/HTTP 传输） |
| Dest | 自动 | 转发目标。占位符**「自动（子项的 listen:端口）」**。可指定端口（`8080`）或 `host:port`（`127.0.0.1:8080`） |
| Xver | `0` | PROXY 协议版本（**「Xver」**）：`0` —— 关闭，`1` 或 `2` —— 对应的 PROXY protocol 版本 |
| （顺序） | 按位置 | 规则的应用顺序；通过**「上移」**/**「下移」**按钮设置 |

保存逻辑：主 inbound 的整个 fallback 列表被原子替换。既没有选择子 inbound（`childId <= 0`）、也没有指定 `Dest` 的行会被**跳过**。若所选子 inbound 等于主 inbound 自身的 id，则将其清零。生成最终 JSON 时：若 `Dest` 为空，则从子 inbound 计算为 `listen:port`，其中 `0.0.0.0`/`::`/`::0` 被替换为 `127.0.0.1`；`name`/`alpn`/`path` 为空的字段不会进入输出 JSON；`xver` 仅在大于 0 时才添加。

**最终 `settings.fallbacks` 示例**（带 `alpn=h2` 的流量经路径 `/ws` 转发到 WS 目标，其余全部转发到端口 8080 上的本地 Nginx）：

```json
{
  "fallbacks": [
    { "alpn": "h2", "path": "/ws", "dest": "127.0.0.1:2001", "xver": 1 },
    { "dest": 8080 }
  ]
}
```

最后一行不含 `name`/`alpn`/`path`，是捕获其余所有流量的「默认」规则。

#### fallback 一节的按钮和提示

- **「添加 fallback」** —— 添加一行；**「暂无 fallback」** —— 空状态。
- **「快速添加所有合适项」** / **「全部添加」** —— 为每个尚未连接的合适 inbound 添加一行 fallback。结果：「已添加 {n} 个 fallback」或「没有新的合适入站」。
- **「从子项填充」** —— 从所选子 inbound 的传输重新拉取路由字段（SNI/ALPN/Path/xver）；执行后显示「已从子项填充」。
- **「修改路由字段」** / **「隐藏高级项」** —— 显示/隐藏行的细节字段。
- **「路由条件」** 和 **「默认 —— 捕获其余所有流量」** 标签说明了每行的触发条件。

保存 fallback 后，服务器会触发 Xray 重启，使新的 `settings.fallbacks` 生效。

### 4.6. 周期性流量重置

**「流量重置」**块按计划配置 inbound 流量计数器的自动重置。描述：

> 「按指定间隔自动重置流量计数器」。

| 参数 | 值 |
|---|---|
| 字段 | `trafficReset` |
| 校验 | `omitempty,oneof=never hourly daily weekly monthly` |
| 默认 | `never` |
| 关联字段 | `lastTrafficResetTime` —— 上次重置的时间戳（标签**「上次重置」**） |

下拉列表：

| 值 | 标签 |
|---|---|
| `never` | **「从不」** |
| `hourly` | **「每小时」** |
| `daily` | **「每天」** |
| `weekly` | **「每周」** |
| `monthly` | **「每月」** |

每个周期都注册了一个 cron 作业，按相应计划运行（`@hourly`、`@daily`、`@weekly`、`@monthly`）。作业会选出所有设置了对应 `trafficReset` 的 inbound，并对每个 inbound 重置其自身的计数器（`up=0`、`down=0`）**以及**其所有客户端的流量。也就是说，周期性重置同时影响 inbound 及其客户端。

**字段值示例。** 要让计数器在每月一号清零，表单中选择**「每月」**，保存为：

```json
{ "trafficReset": "monthly" }
```

值 `never`（默认）完全关闭自动重置。

### 4.7. 入站 JSON（高级）

**「入站 JSON 分区」**一节提供对 inbound 原始 JSON 块的直接访问。描述：

> 「完整的入站 JSON 以及针对 settings、sniffing 和 streamSettings 的独立编辑器」。

可用的编辑器：

| 选项卡 | 标签 | 编辑内容 |
|---|---|---|
| **全部** | 「在一个编辑器中包含所有字段的完整入站对象」 | 整个 Inbound 对象 |
| **设置** | 「Xray settings 块的封装」 | `settings` 字段 |
| **Sniffing** | 「Xray sniffing 块的封装」 | `sniffing` 字段 |
| **Stream** | 「Xray stream 块的封装」 | `streamSettings` 字段 |

这些字段被序列化为嵌套的 JSON 对象：空块以 `null` 返回，而非有效 JSON 的文本会被包装成字符串，以免数据丢失。保存时的解析错误会带**「高级 JSON」**前缀显示。

「入站 JSON」查看窗口和 inbound 导入窗口一样，使用带 JSON 语法高亮的完整代码编辑器（而非普通文本框）：查看配置时为高亮的只读模式，导入时为可编辑模式，从而便于阅读和修改。

### 4.8. inbound 操作：QR / Edit / Reset / Delete 及统计

在列表和 inbound 卡片中可执行以下操作（**「菜单」**菜单）：

#### 流量统计

显示 inbound 的汇总流量：**「已发送/已接收」**（`up`/`down` 字段）、**「总流量」**、**「总连接数」**。卡片中还有**「创建于」**、**「更新于」**、**「到期日期」**。

inbounds 列表中有一个 **Speed** 列，显示每个 inbound 当前的流量速度（上传/下载），它由两次轮询间计数器的增量计算得出；同样的实时速度也显示在 inbound 统计窗口中。当某次轮询没有增量时，速度值会被重置。

在 inbounds 页面的客户端汇总中，状态按「已耗尽/已结束」优先级判定：到期或流量耗尽（并被自动任务取消了 `enable`）的客户端归入**「已耗尽/已结束」**（*Depleted/Ended*）状态，而非灰色的**「已禁用」**（*Disabled*），且不会被重复计数。该分类与客户端自身卡片中显示的一致，并正确处理绑定到多个 inbound 的客户端。

#### 二维码与复制链接

- **「详情」** —— 展开连接和订阅链接。
- 客户端二维码：提示**「点击二维码即可复制」**。
- **「复制链接」**（英文 *Copy URL*）、**「导出链接」**。

#### Edit（修改）

**「修改连接」** —— 打开编辑表单（`POST /update/:id`）。更新时服务会重新读取现有行，迁移已变更的字段，必要时重新生成标签（若旧标签是自动生成的），并同步 Xray 运行时。成功时显示提示**「连接更新成功」**。

#### Reset Traffic（重置流量）

**「重置流量」** —— 将此 inbound 的 `up`/`down` 计数器清零（`POST /:id/resetTraffic`，设为 `up=0, down=0`）。确认：

> 「重置 "{remark}" 的流量？」 / 「将此连接的发送/接收计数器重置为 0」。

重置 inbound 流量**不**触动其客户端的计数器（客户端有单独的「重置客户端流量」操作）。重置后会触发 Xray 重启。成功时显示提示**「入站流量已重置」**。还有批量版本——**「重置所有连接的流量」**（`POST /resetAllTraffics`）。

#### Delete（删除）

**「删除连接」**（`POST /del/:id`）。确认：

> 「删除连接 "{remark}"？」 / 「该连接及其所有客户端都将被删除。此操作无法撤销」。

删除会将 inbound 从运行中的 Xray 移除（必要时伴随重启）。成功时显示提示**「连接删除成功」**。批量删除为 `POST /bulkDel`，带逐项报告，且最多只重启一次 Xray。

#### inbound 客户端的其他操作

菜单中还提供：**「克隆」**（带新端口和空客户端列表的 inbound 副本）、**「删除所有客户端」**（`POST /:id/delAllClients` —— 删除所有客户端，inbound 本身保留）、**「删除已禁用的客户端」**、**「绑定/解绑客户端」**、**「导入」**/**「导出连接」**（`POST /import`）。客户端操作的细节属于客户端章节。

---

## 5. 协议

在创建入站连接（inbound）时，首先要选择的是**协议**（「Protocol」）。协议决定了 Xray-core 对该 inbound 采用哪种流量认证与加密方式、`settings` 中需要填写哪一组字段，以及该 inbound 可用哪些传输方式（`network`）和安全类型（TLS / REALITY）。

协议字段在创建 inbound 时设定一次，**编辑时不可更改**（编辑表单中的下拉列表处于锁定状态）。若要更换协议，需要新建一个 inbound。

### 5.1. 受支持协议列表

服务端接受 `Protocol` 字段的以下取值：

```
oneof=vmess vless trojan shadowsocks wireguard hysteria http mixed tunnel tun mtproto
```

> 从版本 **3.3.0** 起，列表中新增了 `mtproto`（Telegram 代理）。

| 配置中的取值 | 用途 | 客户端模型 |
|---|---|---|
| `vless` | 主力代理协议（创建 inbound 时的默认值） | 使用 UUID 的客户端，支持 flow 和后量子加密 |
| `vmess` | 经典的 Xray 代理协议 | 使用 UUID 和 `security` 参数的客户端 |
| `trojan` | 伪装成普通 HTTPS 的代理 | 使用密码的客户端 |
| `shadowsocks` | Shadowsocks 代理（含 SIP022 / 2022-blake3） | 单用户或多用户（2022） |
| `wireguard` | WireGuard inbound | Peer（而非客户端） |
| `hysteria` | Hysteria inbound（默认版本 2） | 使用 `auth` 令牌的客户端 |
| `http` | 经典 HTTP 代理（forward proxy） | user/pass 账户，不计流量 |
| `mixed` | 合并的 SOCKS + HTTP 代理 | user/pass 账户 |
| `tunnel` | 透明转发器（xray `dokodemo-door`） | 无客户端 |
| `tun` | TUN 接口（仅用于渲染现有项） | 无客户端 |
| `mtproto` | Telegram 代理（MTProto），于 3.3.0 加入；由独立进程 `mtg` 提供服务，而非 Xray | 无客户端（凭密钥访问） |

> 关于 `tun` 的说明：该取值保留在列表中只是为了兼容并**显示**此前已保存的 inbound，但在当前版本中 backend 不建议创建此类型——该支持已被视为过时。创建此类型的新 inbound 没有意义。

> 关于 Hysteria 2 的说明：不存在名为「hysteria2」的独立协议。它就是带有 `streamSettings.version = 2` 字段的 `hysteria` 协议。在生成分享链接时，当流版本等于 2，`hysteria2://` 的链接格式会被自动选用。

并非所有协议都支持分发到节点（nodes）。可部署到节点的只有：`vless`、`vmess`、`trojan`、`shadowsocks`、`hysteria`、`wireguard`。协议 `http`、`mixed`、`tunnel`、`tun`、`mtproto` 仅在本地面板上运行。

### 5.2. 哪些协议支持 TLS / REALITY / 传输

能否启用某一层安全和传输取决于协议以及所选网络（`streamSettings.network`）：

| 功能 | 适用的协议 | 允许的网络（`network`） |
|---|---|---|
| **TLS** | `vmess`、`vless`、`trojan`、`shadowsocks`（对 `hysteria` 则始终可用） | `tcp`、`ws`、`http`、`grpc`、`httpupgrade`、`xhttp` |
| **REALITY** | `vless`、`trojan` | `tcp`、`http`、`grpc`、`xhttp` |
| **flow（`xtls-rprx-vision`）** | 仅 `vless` | 仅 `tcp`，且 `security = tls` 或 `reality` |
| **Stream / 传输**（「传输」标签页） | `vmess`、`vless`、`trojan`、`shadowsocks`、`hysteria` | — |

对于协议 `http`、`mixed`、`tunnel`、`tun`、`wireguard`，传输标签页不可用——它们没有 Xray 的 stream 设置。

---

### 5.3. VLESS

用途：主力现代代理协议。支持 XTLS-Vision（`flow`）、REALITY，以及 VLESS 本身层面的后量子加密（字段 `decryption` / `encryption`）。新建 inbound 时默认采用该协议。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `clients` | `[]` | 客户端列表。每个客户端包含：`id`（UUID）、`email`（必填）、`flow`、限额（`limitIp`、`totalGB`、`expiryTime`）、`enable`、`tgId`、`subId`、`comment`、`reset` |
| `decryption` | `none` | 服务端侧的解密参数。UI 中的标签：「解密」（英文「Decryption」） |
| `encryption` | `none` | 配对的加密参数（会写入客户端链接）。标签：「加密」（英文「Encryption」） |
| `fallbacks` | `[]` | fallback 列表（参见 fallback 一节）；当 `network = tcp` 且 `security` 为 TLS 或 REALITY 时可用 |
| `testseed` | （4 个数字：900、500、900、256） | 「Vision testseed」——用于 XTLS-Vision padding 的 4 个正整数。仅对带 `xtls-rprx-vision` flow 的客户端生效，否则被忽略 |

#### flow（`xtls-rprx-vision`）

`flow` 设定在**客户端**上，而非 inbound 上，可取以下三种值之一：

| 取值 | 含义 |
|---|---|
| `` （空） | 不使用 XTLS-flow（默认） |
| `xtls-rprx-vision` | XTLS-Vision——VLESS over TCP+TLS/REALITY 的推荐模式 |
| `xtls-rprx-vision-udp443` | 同样的 Vision，但带 UDP/443（QUIC）处理 |

只有在满足全部条件时 `flow` 字段才可选：协议为 `vless`、`network = tcp` 且 `security` 为 `tls` 或 `reality`。**Vision testseed** 字段也只在相同条件下才显示在表单中。

> XHTTP 的例外：当 VLESS over `network = xhttp` 并启用了 VLESS 后量子认证（`encryption`/`decryption`，vlessenc）时，`xtls-rprx-vision` flow 同样允许——无论安全层如何，包括与 REALITY 搭配。此时面板会正确地将 `xtls-rprx-vision` 写入分享链接和订阅中（含 Clash/Mihomo 格式），因此客户端拿到的正是带 Vision 的配置。

#### 解密 / 加密（VLESS 后量子认证）

字段 `decryption` 和 `encryption` 是 VLESS 本身层面的认证（独立于传输层的 TLS/REALITY）。两者默认均为 `none`。表单中其旁边有三个按钮：

- **X25519 认证**（英文「X25519 auth」）——基于 X25519 生成一对 `decryption`/`encryption`。
- **ML-KEM-768 认证**（英文「ML-KEM-768 auth」）——后量子（Post-Quantum）变体。
- **清除**——将两个字段重置回 `none`。

按钮下方会显示一行状态「已选择：{auth}」，其值根据 `encryption` 字符串的最后一段判定：空/`none` → 「None」，超长密钥（>300 个字符）→ ML-KEM-768，较短 → X25519，否则为「自定义」。

技术上，这些按钮会调用 `GET /panel/api/server/getNewVlessEnc`（通过 `xray vlessenc` 生成密钥），并以形如 `mlkem768x25519plus.native.<rtt>.<role>` 的配对值填充**两个**字段（例如 `decryption = mlkem768x25519plus.native.600s.server-x25519`、`encryption = mlkem768x25519plus.native.0rtt.client-x25519`）。参数 `decryption` 留在服务端，`encryption` 写入客户端链接。

> 重要：在为 Xray 生成 inbound 配置时，面板会删除多余内容：如果 `settings` 中残留 `encryption`（它属于客户端侧），则会被从服务端配置中**剔除**。服务端上只保留 `decryption`。

何时选用 VLESS：这是新 inbound 的推荐默认选项，尤其是搭配 REALITY（无需自有证书）或 TLS + XTLS-Vision 时。

**示例：带一个客户端和 XTLS-Vision 的 VLESS inbound 的 `settings` 块。** `flow` 字段位于客户端上，`decryption` 留在服务端：

```json
{
  "clients": [
    {
      "id": "d342d11e-d424-4583-b36e-524ab1f0afa4",
      "email": "user1",
      "flow": "xtls-rprx-vision",
      "limitIp": 2,
      "totalGB": 0,
      "expiryTime": 0,
      "enable": true
    }
  ],
  "decryption": "none"
}
```

对于 REALITY 搭配，对应的 `streamSettings` 块（「Transport」标签页 → Security: REALITY）如下：

```json
{
  "network": "tcp",
  "security": "reality",
  "realitySettings": {
    "dest": "www.microsoft.com:443",
    "serverNames": ["www.microsoft.com"],
    "privateKey": "<приватный ключ X25519>",
    "shortIds": ["", "6ba85179e30d4fc2"]
  }
}
```

---

### 5.4. VMess

用途：经典的 Xray 代理协议。按 UUID 认证，客户端上还可额外配置有效载荷的加密方法（`security`）。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `clients` | `[]` | 客户端列表 |

每个 VMess 客户端（除了通用字段 `email`、限额、`enable`、`tgId`、`subId`、`comment`、`reset` 之外）：

| 客户端字段 | 默认值 | 说明 |
|---|---|---|
| `id` | — | 客户端 UUID |
| `security` | `auto` | VMess 有效载荷的加密方法。允许取值：`aes-128-gcm`、`chacha20-poly1305`、`auto`、`none`、`zero` |

`security` 取值含义：
- `auto` —— Xray 根据平台自行选择密码（推荐）；
- `aes-128-gcm`、`chacha20-poly1305` —— 固定的 AEAD 密码；
- `none` —— 不加密有效载荷（仅在 TLS 之上才有意义）；
- `zero` —— 既不加密也不认证有效载荷。

> 历史兼容性：旧记录可能存有 `security: ""` —— 读取时空字符串会被归并为 `auto`。在生成服务端配置时，VMess 客户端的 `security` 字段会从 `settings` 中**删除**，因为 inbound 不需要它。

何时选用 VMess：为了兼容旧客户端或现有配置。对于新部署，通常更推荐 VLESS。

---

### 5.5. Trojan

用途：模仿普通 HTTPS 流量的代理。按密码认证。与 VLESS 一样，支持 fallback，并（在 `network = tcp` 时）支持 REALITY/TLS。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `clients` | `[]` | 客户端列表 |
| `fallbacks` | `[]` | fallback 列表（在 `network = tcp` 且 TLS/REALITY 时可用） |

每个 Trojan 客户端的关键字段：

| 客户端字段 | 默认值 | 说明 |
|---|---|---|
| `password` | — | 客户端密码（必填，至少 1 个字符） |
| `email` | — | 客户端的唯一标识符 |

客户端的其余字段为通用字段（`limitIp`、`totalGB`、`expiryTime`、`enable`、`tgId`、`subId`、`comment`、`reset`）。

何时选用 Trojan：当需要在 443 端口上伪装成 HTTPS 时，包括对未授权连接 fallback 到 Web 服务器（Nginx）的情形。

**示例：带 fallback 到本地 Web 服务器的 Trojan `settings` 块。** 未授权连接（无有效密码）被转发到监听 `127.0.0.1:8080` 的 Nginx：

```json
{
  "clients": [
    { "password": "S3cret-Pass-1", "email": "user1" }
  ],
  "fallbacks": [
    { "dest": "127.0.0.1:8080" }
  ]
}
```

fallback 需要 `network = tcp` 且 Security 为 TLS 或 REALITY；否则 fallbacks 字段不可用。

---

### 5.6. Shadowsocks

用途：轻量的 Shadowsocks 代理。既支持过时的 AEAD 密码，也支持新的 SIP022 方法（`2022-blake3-*`）。可在单用户或多用户模式下运行。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `method` | `2022-blake3-aes-256-gcm` | inbound 的加密方法。UI 中的标签：「加密方法」（英文「Encryption method」） |
| `password` | `` | inbound 的密码（对于 2022 方法会按所选方法自动生成） |
| `network` | `tcp,udp` | 传输方式。标签：「网络」（英文「Network」）。可选项：`tcp,udp`（TCP、UDP）、`tcp`、`udp` |
| `clients` | `[]` | 客户端列表 |
| `ivCheck` | `false`（关闭） | 「ivCheck」开关——防止 IV 重复使用的保护 |

#### 加密方法（`method`）

允许的集合：

| 方法 | 类别 |
|---|---|
| `aes-256-gcm` | 过时的 AEAD |
| `chacha20-poly1305` | 过时的 AEAD |
| `chacha20-ietf-poly1305` | 过时的 AEAD |
| `xchacha20-ietf-poly1305` | 过时的 AEAD |
| `2022-blake3-aes-128-gcm` | SS 2022（推荐） |
| `2022-blake3-aes-256-gcm` | SS 2022（默认） |
| `2022-blake3-chacha20-poly1305` | SS 2022，单用户 |

面板按方法的处理逻辑：
- **2022 方法**（`2022-blake3-*`）被视为「SS 2022」。方法 `2022-blake3-chacha20-poly1305` 为**单用户**（不支持 multi-user）；其余 2022 方法允许多个客户端。带生成按钮（按方法匹配密钥长度）的密码字段正是针对 2022 方法显示在表单中。
- **过时密码**（`aes-*`、`chacha20-*`）按经典方案「一个方法 + 一个密码」工作。

> 启动 Xray 前的规范化：对于过时密码，每个客户端必须携带与 inbound 方法相同的 `method`（否则 Xray 会因「unsupported cipher method:」而崩溃）。对于 2022 方法则相反——客户端的 `method` 字段必须**为空**（否则 Xray 会因「users must have empty method」而拒绝该 inbound）。面板在切换方法时会自动整理数据。

> 更改密钥大小时重新生成客户端密钥：对于 Shadowsocks-2022，当加密方法切换为密钥大小不同的方法（例如在 `2022-blake3-aes-256-gcm` 与 `2022-blake3-aes-128-gcm` 之间）时，面板会在保存 inbound 时自动按新长度重新生成客户端 PSK。否则旧密钥仍保持原长度，Xray 会拒绝它们。后果：受影响的客户端需要重新获取订阅——此前的链接将无法连接。

何时选用 Shadowsocks：用于无需 TLS 伪装的简单部署；现代选择是 2022-blake3 方法。

**示例：使用 2022-blake3 方法（多用户模式）的 Shadowsocks `settings` 块。** inbound 有自己的密码（所需长度的 base64 密钥），每个客户端有自己的密码，客户端的 `method` 字段**为空**：

```json
{
  "method": "2022-blake3-aes-256-gcm",
  "password": "d2hhdGV2ZXItMzItYnl0ZS1iYXNlNjQta2V5LWhlcmU=",
  "network": "tcp,udp",
  "clients": [
    {
      "email": "user1",
      "password": "Y2xpZW50LWtleS0zMi1ieXRlcy1iYXNlNjQtaGVyZQ==",
      "method": ""
    }
  ]
}
```

对于 legacy 密码（`aes-256-gcm` 等）则相反：inbound 上只有一个密码，而客户端的 `method` 必须与 inbound 的方法一致。

---

### 5.7. Dokodemo-door / Tunnel（透明转发器）

用途：透明转发器（在面板中为协议 `tunnel`，实现 `dokodemo-door` 的行为）。接收流量并将其重定向到指定的地址/端口，无需认证，也没有客户端。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `rewriteAddress` | （无） | 「重写地址」（英文「Rewrite address」）——流量被重定向到的目标地址 |
| `rewritePort` | （无） | 「重写端口」（英文「Rewrite port」）——目标端口（0–65535） |
| `allowedNetwork` | `tcp,udp` | 「允许的网络」（英文「Allowed network」）。可选项：`tcp,udp`、`tcp`、`udp` |
| `portMap` | `{}` | 「端口映射」——端口→端口的映射表（Record<string,string>） |
| `followRedirect` | `false`（关闭） | 「跟随 redirect」（英文「Follow redirect」）——使用被拦截连接的原始目标地址 |

> Tunnel 的「Transport」标签页：此类型的 inbound 有一个**「Transport」**标签页，但仅限于 `sockopt` 设置——这足以支持 **TProxy** 模式（通过 `sockopt.tproxy` 进行透明代理/重定向）。Tunnel 的传输选择下拉列表（`network`）和「Security」标签页被隐藏，因为该类型不支持 TLS/REALITY。

何时选用：用于对内部服务进行透明代理/端口转发。

---

### 5.8. SOCKS / HTTP（协议 `mixed`）

在此构建中没有独立的 `socks` 协议——SOCKS 和 HTTP 代理被合并到协议 **`mixed`**（合并的 SOCKS + HTTP）中。此外，还有一个独立的纯 `http` 代理。

#### 5.8.1. Mixed（SOCKS + HTTP）

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `auth` | `password` | 「Auth」——认证模式。可选项：`password`（按用户名/密码）或 `noauth`（无需授权） |
| `accounts` | （可选） | 「账户」——user/pass 对的列表。当 `auth = noauth` 时，该字段不写入配置 |
| `udp` | `false`（关闭） | 「UDP」开关——通过 SOCKS 支持 UDP |
| `ip` | `127.0.0.1` | 「UDP IP」——UDP 关联的本地地址。该字段仅在启用 `udp` 时显示 |

账户通过「添加」按钮添加；添加时会生成随机的登录名（8 个字符）和密码（12 个字符），可以编辑。

#### 5.8.2. HTTP（纯代理）

用途：经典的 HTTP forward 代理。在 Xray 层面不把客户端作为「计费」对象跟踪（没有 email/限额）——只有一个账户列表。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `accounts` | `[]` | 「账户」——user/pass 对的列表（两个字段均必填） |
| `allowTransparent` | `false`（关闭） | 「允许透明」（英文「Allow transparent」）——以原始 Host 头转发请求 |

何时选用 SOCKS/HTTP：用于无需复杂伪装的本地或内部代理访问。`mixed` 的方便之处在于一个端口同时为 SOCKS 和 HTTP 客户端提供服务。

---

### 5.9. WireGuard（inbound）

用途：WireGuard inbound。与代理协议不同，它不操作「客户端」——取而代之的是配置 **peer**（服务端接受的设备）。传输和 TLS/REALITY 对它不适用。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `secretKey` | — | 服务端私钥（必填）。旁边有生成按钮；公钥自动推导显示（只读字段） |
| `mtu` | （可选） | 接口的 MTU |
| `noKernelTun` | `false`（关闭） | 「无 kernel 的 TUN」（英文「No-kernel TUN」）——使用 userspace-TUN 而非内核 TUN |
| `domainStrategy` | （可选） | 「Domain Strategy」——域名解析策略：`ForceIP`、`ForceIPv4`、`ForceIPv4v6`、`ForceIPv6`、`ForceIPv6v4` |
| `peers` | `[]` | peer 列表 |

每个 peer 的字段：

| peer 字段 | 默认值 | 说明 |
|---|---|---|
| `privateKey` | （可选） | 客户端私钥——保存它是为了让面板能为用户渲染配置（仅在 inbound-peer 上） |
| `publicKey` | — | peer 的公钥（必填） |
| `preSharedKey`（PSK） | （可选） | 额外的共享密钥 |
| `allowedIPs` | `[]` | 允许的 IP。添加新 peer 时，面板会自动建议下一个空闲地址（默认 `10.0.0.2/32`） |
| `keepAlive` | （可选） | 「Keep-alive」——连接保持间隔 |
| `comment` | （可选） | 「Comment」——peer 的任意标签；显示在「Peer N」标题旁，并会带入分享链接和 `.conf` 文件的 `remark` 中 |

「添加 peer」按钮会生成一对新密钥并填入下一个 `allowedIPs`。每个 peer 都可以删除（仅剩一个时不允许删除）。

peer 的「Comment」字段有助于区分设备：其文本显示在表单中「Peer N」标题旁，同时也会进入分享链接和所生成 `.conf` 文件的 `remark` 中，因此在客户端应用里很容易认出设备。这是一个面板字段——xray-core 会忽略 peer 的未知字段。

#### Domain Strategy 与 Transport 标签页

除了 peer 之外，WireGuard inbound 还有一个 **Domain Strategy** 字段（域名解析策略：`ForceIP`、`ForceIPv4`、`ForceIPv4v6`、`ForceIPv6`、`ForceIPv6v4`）。该字段可选，只有在设定时才写入配置。

> **Workers** 字段（`workers`，工作线程数）已从 WireGuard 表单（inbound 和 outbound 均如此）中移除：从 xray-core v26.6.22 起，引擎不再使用它，而依赖 wireguard-go 的内部机制。此前已保存的配置无需改动即可工作——解析时该字段会被直接丢弃，无需迁移。

> WireGuard 也有一个 **「Transport」** 标签页——但是精简版：其上只能配置 `sockopt` 和 **Finalmask** 混淆。传输选择下拉列表（`network`）被隐藏，因为 WireGuard 始终通过 UDP 监听。在噪声记录（noise）中，Finalmask 以单独字段设定 **Rand Range**（0–255 的字节范围，带校验），而 WireGuard 和 Hysteria 可用的混淆方法是 **Salamander**。

何时选用 WireGuard：当你需要的正是 WireGuard VPN 隧道，而非可伪装的代理时。

---

### 5.10. Hysteria（默认 v2）

用途：基于 QUIC 的 Hysteria inbound。面板默认使用版本 2。每个客户端用 `auth` 令牌认证，而非 UUID/密码。Hysteria 的 TLS 始终可用（参见 5.2 的功能表）。

`settings` 块的字段：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `version` | `2` | 协议版本（最低 1；面板默认 2） |
| `clients` | `[]` | 客户端列表 |

每个客户端的关键字段是 `auth`（令牌，必填），外加通用字段（`email`、限额、`enable`、`tgId`、`subId`、`comment`、`reset`）。

附加参数在 `streamSettings.hysteriaSettings` 中设定：

| 字段 | 值 / 可选项 | 说明 |
|---|---|---|
| `version` | 固定为 2（字段锁定） | 「版本」（英文「Version」） |
| `udpIdleTimeout` | （整数 ≥ 1，秒） | 「UDP idle timeout（秒）」——UDP 空闲超时 |
| `masquerade` | 默认关闭 | 「Masquerade」——在「未授权」请求时伪装成普通 Web 服务器 |

启用 `masquerade` 时可选择类型（`type`）：
- `` —— default（404 页面）；
- `proxy` —— 反向代理（字段「Upstream URL」、「重写 Host」、「跳过 TLS verify」）；
- `file` —— 目录分发（字段「目录」，例如 `/var/www/html`）；
- `string` —— 固定响应（字段「状态码」、「Body」、「头部」）。

何时选用 Hysteria：当需要 QUIC 传输以及在不稳定/移动网络上的鲁棒性时；伪装可提升入口点的隐蔽性。

---

### 5.11. MTProto（Telegram 代理）

> 于版本 **3.3.0** 加入。协议取值为 `mtproto`。

MTProto 是 Telegram 自有代理的协议。在 3X-UI 中，此类 inbound **不由 Xray 而由独立进程 `mtg` 提供服务**，由面板自身管理。面板会定期将已启用的 MTProto inbound 与正在运行的 `mtg` 进程进行核对：启动缺失的、停止多余的，并从 `mtg` 的指标中采集流量计数。因此该 inbound 的**流量统计**与普通协议一样工作。

表单中的官方提示：

> 「MTProto 由独立进程 mtg 提供服务，而非 Xray。这里的传输设置和客户端不适用——请在 Telegram 中分享下方链接。」

由此带来：

- **「传输」（Stream Settings）和「客户端」标签页对该 inbound 不适用**——访问通过单个密钥设定，而非客户端列表。
- MTProto inbound **仅在主面板上启动**；不会部署到子节点（nodes）上（带有指定 `NodeID` 的 inbound 会被跳过）。

- MTProto 的 **「Sniffing」** 标签页被隐藏——该协议由进程 `mtg` 而非 Xray 提供服务，因此 sniffing 对它不适用。

**字段。** 保存在 inbound 的 `settings` 中：

| UI 中的字段 | 键 | 说明 |
|---|---|---|
| Remark | `remark` | inbound 标签。 |
| Listen IP | `listen` | 监听的 IP（空 = 所有接口）。 |
| Port | `port` | 代理端口。 |
| 密钥 | `settings.secret` | **FakeTLS** 格式的访问密钥。 |
| 掩护域名（FakeTLS） | `settings.fakeTlsDomain` | 代理将其 HTTPS 流量伪装成访问的那个域名。 |

**密钥格式（FakeTLS）。** 面板会自动将密钥规整为正确形式：结果 = `ee` + 32 个 hex 字符 + 掩护域名的 hex 编码，即 `ee<hex32><hex(fakeTlsDomain)>`。前缀 `ee` 启用 FakeTLS 模式，而域名（例如某知名网站）用于将流量伪装成普通 HTTPS。只需指定域名即可——其余部分由面板自动补全。

#### Domain-fronting 与 mtg 的扩展选项

MTProto inbound 还有 `mtg` 进程的附加参数。字段 **Domain fronting IP**、**Domain fronting port** 和 **Domain fronting PROXY protocol** 设定 `mtg` 将非 Telegram 流量发送到何处（例如发往一个假的 NGINX 站点）：如果 IP 留空，则通过 DNS 使用 FakeTLS 域名，默认端口为 `443`。此外还有 **Accept PROXY protocol**（用于监听器）、**IP preference**（`prefer-ipv6` / `prefer-ipv4` / `only-ipv6` / `only-ipv4`）和 **Debug logging**。每个值仅在设定时才写入文件 `mtg-<id>.toml`。

#### 通过 Xray 路由 Telegram 流量

开关 **「Route through Xray」**（默认关闭）和可选字段 **Outbound** 让你能把 Telegram 的 egress 交给 Xray 路由器管理。启用后，面板会在 Xray 配置中嵌入一个带有该 inbound 自身 tag 的本地 SOCKS 桥，`mtg` 通过它发送 Telegram 流量。此后即可在「Routing」标签页上用规则对该流量进行匹配，或通过 **Outbound** 字段将其强制导向所选 outbound 或负载均衡器（若该字段为空，则由路由规则决定）。

**如何分发给用户。** 对于 MTProto inbound，面板会生成一条邀请链接：

**示例：FakeTLS 密钥与生成的链接。** 如果掩护域名为 `www.cloudflare.com`，密钥按 `ee` + 32 个 hex 字符 + 域名的 hex 编码组装，例如：

```
secret = ee1a2b3c4d5e6f70819293a4b5c6d7e8f7777772e636c6f7564666c6172652e636f6d
```

生成的邀请链接（连同 QR 码一起在 Telegram 中发给用户）：

```
tg://proxy?server=203.0.113.10&port=443&secret=ee1a2b3c4d5e6f70819293a4b5c6d7e8f7777772e636c6f7564666c6172652e636f6d
```

```
tg://proxy?server=<адрес>&port=<порт>&secret=<секрет>
```

（等价形式——`https://t.me/proxy?server=…&port=…&secret=…`）。需要把这条链接和 QR 码发给 Telegram 用户——打开后代理会立即添加到应用中。该链接也会通过订阅服务器分发。

**何时使用。** 绕过 Telegram 封锁的常规方式；FakeTLS 伪装（掩护域名）让流量看起来像在普通访问所指定的网站。

### 5.12. 协议选择速查表

- **VLESS** —— 默认选择；搭配 REALITY 或 TLS + XTLS-Vision 时为最佳方案，支持后量子认证。
- **Trojan** —— 伪装成 HTTPS，可 fallback 到 Web 服务器。
- **VMess** —— 兼容旧客户端。
- **Shadowsocks** —— 不带 TLS 的简单代理；现代选择是 `2022-blake3-*` 方法。
- **Hysteria** —— QUIC，在劣质网络上的鲁棒性。
- **mixed / http** —— 内部用 SOCKS/HTTP 代理。
- **WireGuard** —— 完整的 VPN 隧道。
- **tunnel** —— 透明的端口转发。
- **MTProto** —— 绕过 Telegram 封锁的代理（FakeTLS）；独立进程 `mtg`。

---

## 6. 传输层（Stream Settings）

传输层（在面板界面中为 **「Транспорт」** 字段，英文 *Transmission*）决定了 Xray-core 在 inbound 内部传输数据的方式：在 TLS/Reality 之上使用何种网络协议，以及流量具体如何成帧。这些参数会保存到 Xray 配置的 `streamSettings` 对象中，并在 inbound 编辑器的传输层选项卡中设置。加密（TLS / Reality）在单独的章节中讨论——此处仅描述网络的选择及其参数。

### 6.1. 选择传输网络

网络在 **「Транспорт」** 下拉列表（`streamSettings.network`）中选择。默认值为 `tcp`（在列表中显示为 **RAW**）。可用的选项如下：

| 列表中的值 | `network` 字段 | 传输层 |
| --- | --- | --- |
| RAW | `tcp` | 普通 TCP（在新版 Xray 中已重命名为 RAW），可选 HTTP 混淆 |
| mKCP | `kcp` | 可靠的 UDP 传输 mKCP |
| WebSocket | `ws` | 基于 HTTP(S) 的 WebSocket |
| gRPC | `grpc` | gRPC 隧道（HTTP/2） |
| HTTPUpgrade | `httpupgrade` | HTTP Upgrade |
| XHTTP | `xhttp` | XHTTP / SplitHTTP——现代的可复用多路传输 |

切换该值时，面板会清空上一个网络的设置块，并用其结构定义中的默认值填充新网络的设置块，因此子表单中的每个字段始终都有合理的初始值。

> **重要。** 在本版面板中，**列表里没有 HTTP/2（`h2`）传输**——它已从网络集合中移除；如需双向的类 HTTP/2 隧道，请使用 gRPC，而现代的 HTTP 伪装传输请使用 XHTTP。**Hysteria** 传输（`hysteria`）不通过此列表选择：它与 Hysteria 协议硬绑定，当 inbound 本身以 Hysteria 协议创建时会自动出现（见第 6.8 节）。

下面分别解析每种网络及其每个字段。

---

### 6.2. RAW / TCP（`tcpSettings`）

基础 TCP 传输。默认情况下流量按「原样」传输；可选地将其伪装成普通的 HTTP/1.1 交互。

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| Proxy Protocol（`acceptProxyProtocol`） | `false`（关闭） | 接收来自上游负载均衡器/代理的 PROXY protocol 头 |
| HTTP 混淆（`header.type`） | `none`（关闭） | 启用将流量伪装为 HTTP/1.1 |

#### Proxy Protocol

**「Proxy Protocol」** 开关（`acceptProxyProtocol`）。启用后，Xray 会在入站连接上预期收到 PROXY protocol 头，并从中提取客户端的真实 IP。仅当面板前面有添加该头的反向代理/负载均衡器（例如 HAProxy 或带 `send-proxy` 的 nginx）时才启用。默认关闭。

#### HTTP 混淆（camouflage）

**「HTTP Обфускация」** 开关。控制 `header` 字段：

- **关闭** → `header.type = "none"`（在传输线路上 `header` 字段直接不存在）。纯 TCP。
- **开启** → `header.type = "http"`。流量按 HTTP/1.1 请求和响应的样式成帧。启用时，面板会立即用默认值填充 `request` 和 `response` 子对象。

启用 HTTP 混淆后，会出现用于配置模拟请求和响应的字段。

**请求头（`header.request`）：**

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| 请求版本 | `request.version` | `1.1` | 请求起始行中的 HTTP 版本 |
| 请求方法 | `request.method` | `GET` | 模拟请求的 HTTP 方法 |
| 请求路径 | `request.path` | `/` | 路径（可多个）。以逗号分隔的值列表输入；在传输线路上是字符串数组。若留空，则填入 `/` |
| 请求头 | `request.headers` | `{}`（空） | HTTP 头的「名称/值」表。存储为映射 `名称 → [值]`（一个名称可对应多个值） |

**响应头（`header.response`）：**

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| 响应版本 | `response.version` | `1.1` | 响应起始行中的 HTTP 版本 |
| 响应状态 | `response.status` | `200` | 模拟响应的 HTTP 状态码 |
| 响应原因 | `response.reason` | `OK` | 状态的文本描述（reason-phrase） |
| 响应头 | `response.headers` | `{}`（空） | 响应头的「名称/值」表（映射 `名称 → [值]`） |

头部字段按行编辑——每一行设置头名称（`Имя`）及其值（`Значение`）。这些参数仅用于伪装流量的外观；它们不影响加密。默认值（`GET / HTTP/1.1`，响应 `200 OK`）适用于大多数场景——只有在需要模拟特定网站/服务时才值得修改。

**RAW 带 HTTP 混淆的 `streamSettings` 示例：**

```json
{
  "network": "tcp",
  "tcpSettings": {
    "acceptProxyProtocol": false,
    "header": {
      "type": "http",
      "request": {
        "version": "1.1",
        "method": "GET",
        "path": ["/"],
        "headers": {
          "Host": ["www.example.com"]
        }
      },
      "response": {
        "version": "1.1",
        "status": "200",
        "reason": "OK"
      }
    }
  }
}
```

请注意：在传输线路上 `path` 是字符串数组，每个头都是值的数组（`Host → ["www.example.com"]`）。

---

### 6.3. mKCP（`kcpSettings`）

mKCP 是基于 UDP 的可靠传输。在丢包率高、延迟大的链路上很有用，但会产生更高的额外开销流量。所有默认值都与 xray-core 中推荐的值一致。

| 字段 | 键 | 默认值 | 允许范围 | 说明 |
| --- | --- | --- | --- | --- |
| MTU | `mtu` | `1350` | 576–1460 | 最大数据包大小（字节）。出现分片问题时调小 |
| TTI（毫秒） | `tti` | `20` | 10–100 | 传输间隔（ms）。越小延迟越低，但额外开销越高 |
| Uplink（МБ/с） | `uplinkCapacity` | `5` | ≥ 0 | 上行的估算吞吐能力（МБ/с） |
| Downlink（МБ/с） | `downlinkCapacity` | `20` | ≥ 0 | 下行的估算吞吐能力（МБ/с） |
| CWND 乘数 | `cwndMultiplier` | `1` | ≥ 1 | 拥塞窗口（congestion window）乘数 |
| 最大发送窗口 | `maxSendingWindow` | `2097152` | ≥ 0 | 发送窗口的最大大小 |

字段说明：
- **Uplink / Downlink capacity** 决定 mKCP 占用链路的激进程度。应按实际链路带宽设置：值过高会导致多余流量，值过低则导致链路未被充分利用。
- **TTI** 直接影响「延迟 ↔ 额外开销」的权衡：较小的值会降低延迟，但会增加额外开销数据包的数量。
- **MTU** 限制单个 mKCP 数据包的大小；调低有助于在大型 UDP 包被截断或丢弃的链路上工作。

> 在本版中，mKCP 子表单内的「seed」字段（mKCP 混淆密码）和**头部类型/混淆**下拉列表（`none`、`srtp`、`utp`、`wechat-video`、`dtls`、`wireguard`）**未作为单独字段提供**——传输层混淆已整合进通用的「FinalMask」机制（包括 `mkcp-legacy` 模式），在相应章节中描述。作为单独复选框的「congestion」参数也未提供；拥塞控制通过 `cwndMultiplier` 和 `maxSendingWindow` 设置。

---

### 6.4. WebSocket（`wsSettings`）

基于 HTTP(S) 的 WebSocket 传输。能很好地穿越 CDN 和反向代理，伪装成普通的 Web 流量。

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Proxy Protocol | `acceptProxyProtocol` | `false` | 接收来自上游代理的 PROXY protocol 头（见第 6.2 节） |
| Хост | `host` | `""`（空） | HTTP 头 `Host` 的值。通过 CDN/域前置工作时指定 |
| Путь | `path` | `/` | WebSocket 握手请求行中的路径 |
| heartbeat 周期 | `heartbeatPeriod` | `0` | 发送 heartbeat 帧的间隔（秒）。`0` 表示禁用 heartbeat |
| Заголовки | `headers` | `{}`（空） | 握手的附加 HTTP 头。映射「名称 → 值」（仅字符串值，无数组） |

说明：
- **Путь** 必须在服务端（inbound）和客户端一致。通常会在 Web 服务器一侧用该路径来伪装入口点。
- **Хост** 在 inbound 位于 CDN 之后或使用域前置时才有意义；否则可以留空。
- **heartbeat 周期** 使连接在穿越会积极断开非活动会话的代理/CDN 时保持「存活」。默认（`0`）禁用 heartbeat。
- 与 RAW 不同，WebSocket 的头部表使用「扁平」格式 `名称 → 值`（每个头一行值）。

**WebSocket 位于 CDN 之后的 `streamSettings` 示例：**

```json
{
  "network": "ws",
  "wsSettings": {
    "acceptProxyProtocol": false,
    "host": "cdn.example.com",
    "path": "/ray",
    "heartbeatPeriod": 0,
    "headers": {
      "User-Agent": "Mozilla/5.0"
    }
  }
}
```

`host` 和 `path` 的值必须与客户端一致；与 RAW 不同，这里头的值是普通字符串，而非数组。

---

### 6.5. gRPC（`grpcSettings`）

参数数量最「精简」的传输。在 gRPC 调用内部（基于 HTTP/2）隧道化流量；与支持 gRPC 的 CDN 兼容性良好。没有头部混淆。

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| 服务名（`Service Name`） | `serviceName` | `""`（空） | gRPC 服务名（实际上是隧道的「路径」）。服务端和客户端必须一致 |
| Authority | `authority` | `""`（空） | 伪头 `:authority` 的值（HTTP/2 中相当于 `Host`）。通过 CDN/域工作时指定 |
| Multi Mode | `multiMode` | `false`（关闭） | 启用在单个连接内多路复用多个并行 gRPC 流 |

说明：
- **Service Name**——gRPC 通道的主要标识符；它在两端必须相同。空值是允许的，但通常会设置一个不明显的字符串用于伪装。
- **Authority** 影响 HTTP/2 帧中发送的 `:authority`；首先在通过 CDN 代理时需要。
- **Multi Mode** 允许多个逻辑流通过单个物理连接；在服务端和客户端都支持时启用以提升性能。

**gRPC 的 `streamSettings` 示例：**

```json
{
  "network": "grpc",
  "grpcSettings": {
    "serviceName": "GunService",
    "authority": "grpc.example.com",
    "multiMode": false
  }
}
```

`serviceName`（此处为 `GunService`）扮演隧道「路径」的角色，必须在服务端和客户端一致。

---

### 6.6. HTTPUpgrade（`httpupgradeSettings`）

基于 HTTP `Upgrade` 机制的传输（与 WebSocket 类似，但不含 WebSocket 协议本身）。同样能很好地穿越代理和 CDN。字段集与 WebSocket 相同，但**不含** heartbeat 周期。

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Proxy Protocol | `acceptProxyProtocol` | `false` | 接收来自上游代理的 PROXY protocol 头 |
| Хост | `host` | `""`（空） | HTTP 头 `Host` 的值 |
| Путь | `path` | `/` | 带 `Upgrade` 头的 HTTP 请求路径 |
| Заголовки | `headers` | `{}`（空） | 附加 HTTP 头。「扁平」映射 `名称 → 值`（与 WebSocket 相同） |

**Хост**、**Путь** 和 **Заголовки** 字段的用途与 WebSocket（第 6.4 节）相同。HTTPUpgrade 没有 heartbeat——这是 WebSocket 特有的。

---

### 6.7. XHTTP / SplitHTTP（`xhttpSettings`）

XHTTP（又称 SplitHTTP）是 xray-core 的现代可复用多路 HTTP 传输。它将上行流和下行流拆分成单独的 HTTP 请求，非常适合 CDN 以及对连接持续时间有限制的环境。编辑器中并非所有字段都会同时显示：其中一部分会根据所选模式（`mode`）和启用的开关而出现。

#### 基础字段（始终可见）

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Хост | `host` | `""`（空） | HTTP 头 `Host` 的值 |
| Путь | `path` | `/` | HTTP 请求的基础路径 |
| 模式（`Mode`） | `mode` | `auto` | 传输模式（见下文） |
| Server Max Header Bytes | `serverMaxHeaderBytes` | `0` | 服务端请求头大小限制（字节）。`0` 为 xray-core 的默认值 |
| Padding Bytes | `xPaddingBytes` | `100-1000` | 随机「填充」padding 的范围（字节，格式 `最小-最大`），用于干扰大小分析 |
| Заголовки | `headers` | `{}`（空） | 附加 HTTP 头。「扁平」映射 `名称 → 值` |
| Uplink 的 HTTP 方法 | `uplinkHTTPMethod` | `""`（Default = POST） | 上行请求的 HTTP 方法。可选：空（默认为 POST）、`POST`、`PUT`、`GET`（最后一项仅在 `packet-up` 模式下可用） |
| Padding Obfs Mode | `xPaddingObfsMode` | `false`（关闭） | 启用增强的 padding 混淆并展开附加字段（见下文） |
| No SSE Header | `noSSEHeader` | `false`（关闭） | 不发送 `Content-Type: text/event-stream`（SSE）头。当它妨碍穿越中间节点时启用 |

#### 「模式」字段（`mode`）

下拉列表，取值：

| 值 | 说明 |
| --- | --- |
| `auto` | 自动选择模式（默认） |
| `packet-up` | 上行流被拆分成单独的 HTTP 请求（每个请求一个数据包） |
| `stream-up` | 上行流通过一个长时持续的流式请求传输 |
| `stream-one` | 一个共用的双向流式请求 |

模式的选择决定了哪些附加字段会变为可见。

**仅在 `mode = packet-up` 时可见的字段：**

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| 最大缓冲上传数 | `scMaxBufferedPosts` | `30` | 上行流同时缓冲的 POST 请求的最大数量 |
| 最大上传大小（字节） | `scMaxEachPostBytes` | `1000000` | 单个上行 POST 请求的最大大小（字节） |
| Uplink Data Placement | `uplinkDataPlacement` | `""`（Default = body） | 上行流数据的放置位置：`body`、`header`、`cookie`、`query` |
| Uplink Data Key | `uplinkDataKey` | `""` | uplink 数据的键名/头名。仅当 `uplinkDataPlacement` 已设置且不等于 `body` 时出现 |

**仅在 `mode = stream-up` 时可见的字段：**

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Stream-Up Server | `scStreamUpServerSecs` | `20-80` | 服务端流式连接的保持时间范围（秒，格式 `最小-最大`） |

#### Padding 混淆字段（在 `xPaddingObfsMode = 开启` 时可见）

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Padding Key | `xPaddingKey` | `""`（占位符 `x_padding`） | padding 的键名 |
| Padding Header | `xPaddingHeader` | `""`（占位符 `X-Padding`） | 传递 padding 所用的 HTTP 头名称 |
| Padding Placement | `xPaddingPlacement` | `""`（Default = queryInHeader） | padding 的放置位置：`queryInHeader`、`header`、`cookie`、`query` |
| Padding Method | `xPaddingMethod` | `""`（Default = repeat-x） | padding 的生成方法：`repeat-x` 或 `tokenish` |

#### 会话与序列的放置（始终可见）

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Session ID Placement | `sessionIDPlacement` | `""`（Default = path） | 传递会话标识符的位置：`path`、`header`、`cookie`、`query` |
| Session ID Key | `sessionIDKey` | `""`（占位符 `x_session`） | 会话键名。仅当 `sessionIDPlacement` 已设置且不等于 `path` 时出现 |
| Session ID Table | `sessionIDTable` | `""`（占位符 `Base62`） | 用于生成会话标识符的字符集。可从自动补全下拉列表中选择预定义值（`ALPHABET`、`Alphabet`、`BASE36`、`Base62`、`HEX`、`alphabet`、`base36`、`hex`、`number`），或输入任意 ASCII 字符串。空——xray-core 的默认值 |
| Session ID Length | `sessionIDLength` | `""`（空） | 所生成标识符的长度或范围（例如 `8-16`）。仅在已设置 `Session ID Table` 时显示；最小值必须大于 0 |
| Sequence Placement | `seqPlacement` | `""`（Default = path） | 传递数据包序号的位置：`path`、`header`、`cookie`、`query` |
| Sequence Key | `seqKey` | `""`（占位符 `x_seq`） | 序列键名。仅当 `seqPlacement` 已设置且不等于 `path` 时出现 |

会话字段在 xray-core v26.6.22 中已重命名：之前称为 **Session Placement** / **Session Key**（`sessionPlacement` / `sessionKey`）——现在是 **Session ID Placement** / **Session ID Key**（`sessionIDPlacement` / `sessionIDKey`）；内核已不再识别旧名称。更新前保存的 inbound 会自动迁移到新键——无需重新保存。

建议：
- 对于大多数安装，只需保持 **模式 = `auto`**，设置 **Путь**/**Хост**，并（在通过 CDN 工作时）与客户端协调一致即可。
- 放置字段（`*Placement`/`*Key`）和 padding 混淆仅在针对特定反 DPI/CDN 场景进行精细调整时才需要；当值为空时，使用括号中标注的 xray-core 默认值。
- 与客户端/outbound 一侧相关的参数（例如重复 POST 的间隔、分块大小）不会出现在 inbound 表单中——监听服务器会忽略它们。相反，XMUX 多路复用器在 inbound 表单中是可用的（见下文）。

- **不会写入额外开销的默认值。** 面板不再向 XHTTP 配置写入额外开销默认值 `scMaxEachPostBytes` 和 `scMinPostsIntervalMs`——会应用 xray-core 的内部值。这消除了一个固定的 DPI 特征（字面量 `scMinPostsIntervalMs=30`），此前流量可能因此被封锁。对于已保存的 inbound，与 xray-core 默认值相同的值不会出现在链接和订阅中（无需重新保存 inbound）；手动设置的值会被保留。

**XHTTP（`auto` 模式）的 `streamSettings` 示例：**

```json
{
  "network": "xhttp",
  "xhttpSettings": {
    "host": "xhttp.example.com",
    "path": "/yourpath",
    "mode": "auto",
    "xPaddingBytes": "100-1000"
  }
}
```

对于大多数安装，这四个字段就足够了；会话/序列放置字段和 padding 混淆字段留空即可——这样会使用 xray-core 的默认值。

#### XMUX（连接多路复用）

**XMUX** 开关（`enableXmux`）启用多路复用层，它将并行请求分配到一个小的物理连接池上。启用后会展开六个可配置字段（保存在 `xhttpSettings.xmux` 中）：

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| Max Concurrency | `maxConcurrency` | `16-32` | 单个连接上的最大并发请求数（范围 `最小-最大`） |
| Max Connections | `maxConnections` | `0` | 物理连接的最大数量（`0` 表示无限制） |
| Max Reuse Times | `cMaxReuseTimes` | `""`（空） | 连接可重复使用的次数 |
| Max Request Times | `hMaxRequestTimes` | `600-900` | 单个连接上的最大请求数（范围） |
| Max Reusable Secs | `hMaxReusableSecs` | `1800-3000` | 连接可用于重复使用的时长（秒，范围） |
| Keep Alive Period | `hKeepAlivePeriod` | `""`（空） | 用于保持连接的 keep-alive 周期 |

> **重要。** 不能同时设置 **Max Connections** 和 **Max Concurrency**——xray-core 会拒绝这样的配置。默认情况下，启用 XMUX 时面板会设置 `Max Concurrency = 16-32`；如果你设置了 **Max Connections**（值大于 `0`），面板会移除默认的 **Max Concurrency** 值以避免冲突。

---

### 6.8. Hysteria 传输（`hysteriaSettings`）

**Hysteria** 传输不在「Транспорт」列表中选择：当 inbound 以 Hysteria 协议创建时它会自动激活，而对其他协议则隐藏（离开 Hysteria 协议时，网络会被强制重置为 `tcp`）。参数：

| 字段 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| 版本 | `version` | `2`（已固定，字段被锁定） | Hysteria 版本。仅支持 Hysteria 2 |
| UDP idle timeout（秒） | `udpIdleTimeout` | `60` | UDP 会话空闲超时（秒）。允许范围为 2–600；xray-core 在启动时会拒绝该区间之外的值 |
| Masquerade | `masquerade` | 关闭（不存在） | 在被探测时启用将监听器伪装成 HTTP/3 服务器 |

启用 **Masquerade** 后会出现类型（`type`）选择以及依赖于它的字段：

- **`""` — default (404 page)**：返回标准的 404 页面（无需额外字段）。
- **`proxy` (reverse proxy)**：反向代理到外部网站。
  - `url`（**Upstream URL**，占位符 `https://www.example.com`）——目标地址；
  - `rewriteHost`（**Переписать Host**，默认 `false`）——替换 `Host` 头；
  - `insecure`（**Пропустить TLS verify**，默认 `false`）——不校验上游的 TLS 证书。
- **`file` (serve directory)**：从目录提供文件。
  - `dir`（**Директория**，占位符 `/var/www/html`）。
- **`string` (fixed body)**：固定的 HTTP 响应。
  - `statusCode`（**Код статуса**，默认 `0`，范围 0–599）；
  - `content`（**Body**）——响应体；
  - `headers`（**Заголовки**）——映射 `名称 → 值`。

Masquerade 让基于 Hysteria 的 inbound 在主动探测中看起来像普通的 HTTP/3 服务器，从而提高隐蔽性。默认情况下伪装是关闭的。

**带反向代理（`masquerade` → `proxy`）的 `hysteriaSettings` 示例：**

```json
{
  "version": 2,
  "udpIdleTimeout": 60,
  "masquerade": {
    "type": "proxy",
    "url": "https://www.example.com",
    "rewriteHost": true,
    "insecure": false
  }
}
```

此处在被探测时，监听器会返回来自 `https://www.example.com` 的响应，将自己伪装成普通的 HTTP/3 网站。

---

### 6.9. 相关参数

除了选择网络之外，同一选项卡上还有两个不依赖于具体传输的通用块（详见相应章节）：

- **External Proxy**（`externalProxy`）——一组外部地址/端口，会在订阅链接中替换面板自身的地址。
- **Sockopt**（`sockopt`）——底层套接字选项（TCP Fast Open、mark、域策略、透明代理等）。

#### Real client IP（识别 CDN/中继后的真实 IP）

当 inbound 位于中间方（如 Cloudflare 这样的 CDN、L4 隧道/中继或另一个面板）之后时，Xray 看到的是中间方的地址，而非真实访问者的地址。该地址会进入在线客户端列表，并据此计算每客户端的 IP 限制，这导致两者在代理之后都失去意义。为了恢复真实 IP，inbound 表单的 **Sockopt** 区块中有一个 **Real client IP** 预设选择，它整合了 `acceptProxyProtocol` 和 `trustedXForwardedFor` 的设置：

| 预设 | 作用 | 何时使用 |
| --- | --- | --- |
| **Off / direct** | 清空两个字段。 | inbound 对客户端直接可达 |
| **Cloudflare CDN** | 设置 `sockopt.trustedXForwardedFor = ["CF-Connecting-IP"]`。 | 位于 Cloudflare CDN（橙色云朵）之后的 WebSocket / HTTPUpgrade / XHTTP / gRPC |
| **L4 relay / Spectrum (PROXY)** | 启用 `acceptProxyProtocol = true`。 | inbound 前面有 L4 隧道/中继或 Cloudflare **Spectrum** |

各预设相互排斥：选择其中一个会清空另一个的字段，因此过时的 `trustedXForwardedFor` 不会覆盖通过 PROXY 协议恢复的 IP。预设下方仍可见「原始」的 **Proxy Protocol** 开关和 **Trusted X-Forwarded-For** 列表——预设只是替你填写它们，必要时可手动修改。如果所选预设不被当前传输支持（例如在 mKCP 上使用 PROXY 协议），表单会显示警告。这些字段仅与服务端相关，并且**绝不会在订阅中发送给客户端**。

> **只用其中一个。** `acceptProxyProtocol` 从 L4 的 PROXY 协议头中读取真实 IP，而 `trustedXForwardedFor` 从 HTTP 请求头中读取；只有当你的中间方链路有此要求时，才值得手动将两者混用。
- **FinalMask**（`finalmask`）——通用的传输层混淆机制（包括 mKCP 的 legacy 混淆），它取代了各网络子表单内单独的「seed」/「header type」字段。

---

## 7. 连接安全：TLS、XTLS 与 REALITY

每个支持通过 transport 流传输的 inbound（VMess、VLESS、Trojan、Shadowsocks、Hysteria），在编辑器中都有一个 **「安全」** 选项卡。在这里可以设置传输通道究竟如何加密和伪装。共有三种模式，通过单选按钮切换：

| 模式 | UI 中的标签 | 何时可用 |
|-------|--------------|----------------|
| `none` | **无** | 始终可用（Hysteria 除外，因其强制要求 TLS） |
| `tls` | **TLS** | 对于网络为 `tcp`、`ws`、`http`、`grpc`、`httpupgrade`、`xhttp` 的 VMess/VLESS/Trojan/Shadowsocks；对于 Hysteria — 始终可用 |
| `reality` | **Reality** | 仅对网络为 `tcp`、`http`、`grpc`、`xhttp` 的 VLESS/Trojan 可用 |

如果协议是 Hysteria，则不显示 **无** 按钮（它强制要求 TLS）。**Reality** 按钮仅在协议与网络的组合允许时才出现（见上表）。

切换模式时，面板会完全重建 `streamSettings` 块：删除上一模式遗留的 `tlsSettings` 和 `realitySettings`，并填入所选模式的默认值。具体而言，选择 **Reality** 时面板会立即自动：从内置的热门域名列表中填入一对随机的 `target` + `serverNames`（SNI），生成随机的 `shortIds`，并向服务器请求一对新的 X25519 密钥（privateKey/publicKey）。

### 7.1. 区别何在：TLS vs XTLS vs REALITY

- **TLS** — 基于 TLS 1.2/1.3 协议的经典传输加密。服务器上必须存放有效证书（自己的域名 + 证书链）。流量看上去像普通 HTTPS，但对于主动审查者而言，到你域名的 TLS 握手具有可识别特征；当按 SNI 进行「狙杀」或缺少受信任证书时，连接会被阻断/报错。

- **XTLS (Vision)** — 它不是「安全」列表中的独立模式，而是叠加在 TLS **或** Reality 之上的 *flow* 机制。通过 inbound 客户端侧的 **Flow** 字段 = `xtls-rprx-vision`（或 `xtls-rprx-vision-udp443`）来启用。在 `security = tls` 或 `security = reality` 的情况下，Vision 可用于网络为 `tcp` 的 VLESS；此外，在启用了 VLESS 加密（vlessenc / ML-KEM）时，Vision 也可用于叠加在 `xhttp` 传输之上的 VLESS — 此时 **Flow** 字段同样可以设为 `xtls-rprx-vision`，且该值会正确写入 `vless://` 链接（`flow=xtls-rprx-vision`）。Vision 减少了「双重加密」（TLS-in-TLS），在握手后直接传递有效负载，从而加快传输速度并改善伪装。因此 **VLESS + Reality + Flow `xtls-rprx-vision`** 这一组合被认为是推荐的现代配置。

- **REALITY** — 一种无需自有证书的伪装机制。服务器「借用」真实第三方网站的 TLS 握手（`target`/`serverNames`），因此对于观察者而言，该连接与访问该网站毫无区别，且完全不需要证书。身份验证建立在一对 X25519 密钥和一组 `shortIds` 之上。REALITY 能抵御主动探测（`active probing`）和按 SNI 阻断，因为 SNI 指向的是真实的外部域名。代价是对配置有更严格的要求（带端口的正确 `target`、与客户端的密钥同步）。

简短的选择规则：
- 有自己的域名和有效证书，需要简单的 HTTPS 外观 → **TLS**（尽可能配合 Vision）；
- 没有域名/证书，或需要对 DPI 实现最大隐蔽性 → **REALITY**（VLESS/TCP 配合 Vision）。

### 7.2. 「无」模式（`none`）

传输不带 TLS 封装：`streamSettings` 中的 `tlsSettings` 和 `realitySettings` 块被剔除。该模式没有额外字段。适用于以下情形：
- inbound 只监听 `127.0.0.1` 并作为 fallback 目标（按面板规则，用于 fallback 的子 inbound 应当以 `security=none` 监听 `127.0.0.1`）；
- 由外层提供加密/伪装（例如面板前置的 Nginx 反向代理）；
- 在内部网络中使用带有自身加密的协议（Shadowsocks）。

对于可从外部访问的 inbound，不建议使用「无」模式。

**示例：网络为 `tcp` 的 TLS 的 `streamSettings` 块**（VLESS/Trojan/VMess）。选择 **TLS** 模式并填写 SNI 和证书路径后，结果如下所示：

```json
"streamSettings": {
  "network": "tcp",
  "security": "tls",
  "tlsSettings": {
    "serverName": "vpn.example.com",
    "minVersion": "1.2",
    "maxVersion": "1.3",
    "alpn": ["h2", "http/1.1"],
    "settings": { "fingerprint": "chrome" },
    "certificates": [
      {
        "certificateFile": "/root/cert/vpn.example.com.crt",
        "keyFile": "/root/cert/vpn.example.com.key",
        "ocspStapling": 3600,
        "usage": "encipherment"
      }
    ]
  }
}
```

### 7.3. TLS 模式

`tlsSettings` 块的字段。默认值取自面板的模式定义。

#### 主要参数

| 字段（标签） | 默认值 | 说明 |
|----------------|----------------------|----------|
| **SNI** (`serverName`) | `""`（空） | Server Name Indication — 在 TLS 握手中出示的域名。必须与证书的域名一致。英文占位提示：「Server Name Indication」。 |
| **Cipher Suites** (`cipherSuites`) | `""` → **自动** | 允许的密码套件列表。默认为空 — 由 Xray/Go 自行选择（**自动** 选项）。仅在需要明确限制密码套件时才更改。 |
| **最小/最大版本** (`minMaxVersion`) | min = `1.2`, max = `1.3` | TLS 的最小和最大版本。可选值：`1.0`、`1.1`、`1.2`、`1.3`。建议保留 `1.2`–`1.3`；不宜将最小值降到 1.0/1.1（过时且不安全的版本）。 |
| **uTLS** (`settings.fingerprint`) | `chrome`（表单中提供 **None** = `""` 选项） | 模仿的客户端 hello 的 TLS 指纹（uTLS fingerprint），使握手看起来像流行浏览器。见下方列表。在 TLS 中，列表的第一项是 **None**（`""`），用于关闭模仿。 |
| **ALPN** (`alpn`) | `["h2", "http/1.1"]` | 在 TLS 中协商的应用层协议列表（多选）。允许的值：`h3`、`h2`、`http/1.1`。默认提供 `h2` 和 `http/1.1`。 |

可选的 **uTLS fingerprint** 值（TLS 与 REALITY 相同）：`chrome`、`firefox`、`safari`、`ios`、`android`、`edge`、`360`、`qq`、`random`、`randomized`、`randomizednoalpn`、`unsafe`。在 TLS 表单中另有一个空值 **None**（不应用指纹模仿）。

可用的 **Cipher Suites** 值（TLS 1.3 和 ECDHE 套件）：`TLS_AES_128_GCM_SHA256`、`TLS_AES_256_GCM_SHA384`、`TLS_CHACHA20_POLY1305_SHA256`、`TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`、`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`、`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`、`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`、`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`、`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`、`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`、`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`、`TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`、`TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`。

#### TLS 开关

| 开关 | 默认值 | 说明 |
|---------------|--------------|----------|
| **拒绝未知 SNI** (`rejectUnknownSni`) | 关（`false`） | 若启用，当客户端出示的 SNI 与证书中的名称不一致时，服务器断开连接。可提升隐蔽性（服务器不响应「陌生」请求），但要求客户端的 SNI 精确匹配。 |
| **禁用 System Root** (`disableSystemRoot`) | 关（`false`） | 关闭对系统受信任根证书存储的使用。 |
| **会话恢复** (`enableSessionResumption`) | 关（`false`） | 启用 TLS 会话恢复（session resumption / session tickets）。 |

#### TLS 附加参数（vcn、曲线、密钥日志、ECH Sockopt）

在 TLS 主要设置下方可使用附加字段。

| 字段（标签） | 默认值 | 说明 |
|----------------|--------------|----------|
| **Verify Peer Cert By Name** (`settings.verifyPeerCertByName`) | `""` | 一组名称（以逗号分隔），客户端按这些名称而非 SNI 来校验服务器证书。这是 2026-06-01 之后从 Xray 移除的 `allowInsecure` 字段的现代替代品。该值仅用于面板：不会写入服务器的 xray 配置，但会传入邀请链接和订阅（`vcn=…`），以便客户端自行应用。占位提示：`example.com`。 |
| **Curve Preferences** (`curvePreferences`) | `""` | 限制并按偏好排序 TLS 密钥交换曲线（例如 `X25519MLKEM768`、`X25519`）。为空时 — 采用 Xray-core 的默认值。 |
| **Master Key Log** (`masterKeyLog`) | `""` | 以 `SSLKEYLOGFILE` 格式写入 TLS master key 的路径（用于调试时在 Wireshark 中解密流量）。占位提示：`/path/to/sslkeylog.txt`。生产环境应留空 — 该文件可解密全部流量。 |
| **ECH Sockopt** (`echSockopt`) | 关 | 一个开关，用于设置 Xray 请求 ECH config list 所用连接的套接字参数。启用后可用：**Dialer Proxy** (`dialerProxy` — 将请求经指定 tag 的 outbound 转发)、**Domain Strategy** (`domainStrategy`)、**TCP Fast Open** (`tcpFastOpen`)、**Multipath TCP** (`tcpMptcp`)。无必要时保持关闭。 |

字段 `verifyPeerCertByName`、`curvePreferences`、`masterKeyLog` 和 `echSockopt` 位于 `tlsSettings` 的顶层，并在保存配置时不会被面板字段的「裁剪」过程剔除。

#### 证书

**SSL 证书** 部分（UI 中标题为「SSL 证书」）以列表形式设置：用 **+** 按钮添加一条新的证书记录，用 **− 删除** 按钮移除（删除按钮仅在记录多于一条时可用）。默认在启用 TLS 时会创建一条空记录。

每条记录都有一个输入模式切换开关（`useFile`）：

- **证书路径**（值 `useFile = true`，默认）— 指定服务器上文件的路径：
  - **公钥** (`certificateFile`) — 证书文件（`.crt`/`.pem`）的路径；
  - **私钥** (`keyFile`) — 私钥文件（`.key`）的路径。
- **证书内容**（值 `useFile = false`）— 内容直接粘贴到字段中（多行文本区域）：
  - **公钥** (`certificate`) — 证书的 PEM 内容；
  - **私钥** (`key`) — 密钥的 PEM 内容。

在「证书路径」模式的字段下方有两个按钮：
- **设置面板证书** — 将面板自有 SSL 证书的路径填入字段。对于中央面板上的 inbound，取其证书（`POST /panel/setting/all` → `webCertFile`/`webKeyFile`）；对于指派到某节点的 inbound，取该节点自身的证书（`GET /panel/api/nodes/webCert/{nodeId}`），因为中央面板的路径在节点上并不存在。若未配置证书，则显示警告：「*面板未配置证书。请先在「设置」中安装。*」（面板证书本身在「设置 → 安全」部分设置）。
- **清除** — 清空两个路径。

每条证书记录的附加字段：

| 字段 | 默认值 | 说明 |
|------|--------------|----------|
| **OCSP Stapling** (`ocspStapling`) | `0`（关） | OCSP stapling 的刷新间隔（秒，最小为 `0`）。对于新建 inbound，默认关闭（`0`）：这可消除 xray 日志中针对无 OCSP 响应方的证书所产生的错误（例如已放弃 OCSP 的 Let's Encrypt）。仅对支持 stapling 的证书启用。 |
| **一次性加载** (`oneTimeLoading`) | 关（`false`） | 若启用，证书在启动时从磁盘读取一次，文件变更时不会重新读取。 |
| **使用选项** (`usage`) | `encipherment` | 证书的用途。允许值：`encipherment`（加密 — 普通服务器证书）、`verify`（校验）、`issue`（签发 — 服务器自行签名/签发证书）。 |
| **Build Chain** (`buildChain`) | 关（`false`） | **仅** 在 `usage = issue` 时显示。补全证书链。 |

> inbound 编辑器中没有「自签名证书」这样的单独按钮：面板不会为 inbound 即时生成自签名证书。证书要么通过路径/内容指定，要么用「设置面板证书」按钮从面板设置中拉取。面板自身 SSL 证书的签发/获取（包括文件上传和域名绑定）在 **设置 → 安全** 部分完成；这里没有面向 inbound 的 ACME/Let's Encrypt 端点。

#### ECH 与证书固定（TLS 扩展字段）

| 字段 | 默认值 | 说明 |
|------|--------------|----------|
| **ECH key** (`echServerKeys`) | `""` | Encrypted Client Hello 的服务器密钥。 |
| **ECH config** (`settings.echConfigList`) | `""` | ECH config list（客户端部分，会写入链接）。 |
| **对端证书 SHA-256** (`settings.pinnedPeerCertSha256`) | `[]` | 对端证书的 SHA-256 哈希（hex 字符串，逗号分隔）。原文提示：「*对端证书的 SHA-256 哈希，以十六进制字符串形式（如 e8e2d3…），以逗号分隔。仅用于面板 — 不写入服务器的 xray 配置，但会包含在邀请链接中，以便客户端固定证书。*」 |

按钮：
在 **对端证书 SHA-256** 字段旁有两个自动填充按钮：
- **Fill from this inbound's certificate**（盾牌图标）— 填入该 inbound 自身证书的 SHA-256 哈希（通过 `getCertHash` 端点本地获取）。
- **Fetch the hash by pinging the SNI (xray tls ping)**（下载图标）— 通过按指定 SNI 进行 TLS 连接来获取服务器实时证书的哈希（服务器上调用 `getRemoteCertHash`）。**SNI** (`serverName`) 字段必须已填写 — 否则显示提示「*Set the SNI (serverName) first to ping the remote certificate.*」

获取到的哈希会添加到字段中（逗号分隔）并写入邀请链接，以便客户端固定证书。
- **获取新的 ECH 证书** — 向服务器请求一对针对当前 SNI 的新 ECH 密钥（`POST /panel/api/server/getNewEchCert`，服务器上执行 `xray tls ech --serverName <SNI>`）；填入 **ECH key** 和 **ECH config** 字段。
- **清除** — 清空两个 ECH 字段。

### 7.4. REALITY 模式

`realitySettings` 块的字段。REALITY 不使用 SSL 证书：取而代之的是借用的外部域名 TLS 握手以及一对 X25519 密钥。

#### 伪装参数

| 字段（标签） | 默认值 | 说明 |
|----------------|----------------------|----------|
| **显示** (`show`) | 关（`false`） | 在 Xray 日志中输出 REALITY 调试信息。通常保持关闭。 |
| **Xver** (`xver`) | `0` | 传递给后端的 PROXY 协议版本（`0` — 关闭）。最小为 `0`。 |
| **uTLS** (`settings.fingerprint`) | `chrome` | 模仿的 TLS 指纹（与 TLS 中相同的列表，但没有空值 None）。 |
| **目标** (`target`) | `""`（启用时面板填入随机值） | **必填字段。** REALITY 借用其 TLS 握手的真实域名。原文提示：「*必填。必须包含端口（例如 example.com:443）。无端口时 Xray-core 不会启动。*」面板的校验会检查端口是否存在且正确；否则给出错误「REALITY 目标必填」/「REALITY 目标必须包含端口…」/「REALITY 目标的端口无效」。旁边的刷新按钮会从内置列表填入一对随机值。 |
| **SNI** (`serverNames`) | `[]`（与目标一同填入） | 允许的 SNI 列表（以标签形式多值输入）。必须与 **目标** 中的域名相符。刷新按钮会连同随机目标一起填入 SNI。 |
| **最大时间差（毫秒）** (`maxTimediff`) | `0` | 客户端与服务器时钟允许的最大偏差（毫秒，`0` — 无限制）。最小为 `0`。 |
| **最低客户端版本** (`minClientVer`) | `""` | Xray 客户端的最低版本（占位提示 `25.9.11`）。为空 — 无限制。 |
| **最高客户端版本** (`maxClientVer`) | `""` | Xray 客户端的最高版本。为空 — 无限制。 |
| **Short IDs** (`shortIds`) | `[]`（启用时生成） | 区分客户端的短标识符（hex）列表。以标签形式多值输入；刷新按钮生成一组随机值。 |
| **SpiderX** (`settings.spiderX`) | `/` | 「蜘蛛」路径（REALITY 的客户端部分），在模仿访问外部网站时使用。会写入邀请链接。 |

启用 REALITY 时以及点击刷新按钮时，**目标** (`target`) 和 **SNI** (`serverNames`) 会从面板的内置列表中填入一对随机值：`www.amazon.com`、`aws.amazon.com`、`www.oracle.com`、`www.nvidia.com`、`www.amd.com`、`www.intel.com`、`www.sony.com`（每个都带端口 `:443`）。请选择一个「重量级」、稳定且不在你自己服务器之后的第三方 HTTPS 网站。

**示例：网络为 `tcp` 的 REALITY 的 `streamSettings` 块**（VLESS）。不需要证书 — 取而代之的是借用的域名和一对 X25519 密钥：

```json
"streamSettings": {
  "network": "tcp",
  "security": "reality",
  "realitySettings": {
    "show": false,
    "xver": 0,
    "dest": "www.nvidia.com:443",
    "serverNames": ["www.nvidia.com"],
    "privateKey": "YOUR_X25519_PRIVATE_KEY",
    "shortIds": ["", "6ba85179e30d4fc2"],
    "settings": {
      "publicKey": "YOUR_X25519_PUBLIC_KEY",
      "fingerprint": "chrome",
      "spiderX": "/"
    }
  }
}
```

这里面板的 **目标** (`target`) 字段对应最终 Xray 配置中的 `dest`。如果某个 REALITY inbound 是以 `dest` 键中的 destination 创建的（由旧版面板、通过 API 或外部工具创建），面板在解析时会在 `target` 为空时将 `dest` → `target` 归一化 — 因此此类 inbound 能正确加载，**目标** 字段不会为空，重新保存也不会破坏正常工作的 REALITY。

#### REALITY 密钥（X25519）

| 字段 | 默认值 | 说明 |
|------|--------------|----------|
| **公钥** (`settings.publicKey`) | `""` | X25519 公钥（客户端将其放入自己的配置/链接中）。 |
| **私钥** (`privateKey`) | `""` | X25519 私钥（仅存于服务器）。 |

密钥下方的按钮：
- **获取新证书** — 向服务器请求一对新密钥（`GET /panel/api/server/getNewX25519Cert`；服务器上执行 `xray x25519`），填入 **私钥** 和 **公钥**。首次启用 REALITY 模式时也会自动生成这同一对密钥。

**示例：通过 API 获取一对 X25519 密钥**（在表单之外，例如供脚本使用）。该请求返回私钥和公钥：

```bash
curl -s -b cookie.txt https://your-panel:2053/panel/api/server/getNewX25519Cert
# Ответ:
# {"success":true,"obj":{"privateKey":"...","publicKey":"..."}}
```

`cookie.txt` — 通过 `POST /login` 登录后获得的会话 cookie 文件。
- **清除** — 清空两个密钥。

#### 后量子签名 ML-DSA-65（mldsa65）

REALITY 的附加（可选）后量子认证层：

| 字段 | 默认值 | 说明 |
|------|--------------|----------|
| **mldsa65 Seed** (`mldsa65Seed`) | `""` | ML-DSA-65 密钥的服务器 seed。 |
| **mldsa65 Verify** (`settings.mldsa65Verify`) | `""` | 校验值（客户端部分，会写入链接）。 |

按钮：
- **获取新的 Seed** — 请求一对新值（`GET /panel/api/server/getNewmldsa65`；服务器上执行 `xray mldsa65`），填入 **mldsa65 Seed** 和 **mldsa65 Verify**。
- **清除** — 清空两个字段。

#### fallback 限速与 REALITY 密钥日志

REALITY 设置中提供 fallback 流量限速 — 它可防止主动探测者将服务器当作通向借用域名的免费通道。该设置对两个方向分别配置 — **Limit Fallback Upload** 和 **Limit Fallback Download**（`limitFallbackUpload` / `limitFallbackDownload`），每个都有相同的一组字段：

| 字段（标签） | 默认值 | 说明 |
|----------------|--------------|----------|
| **After Bytes** (`afterBytes`) | `0` | 在开始限速之前以全速放行多少字节。`0` — 从第一个字节起就限速。 |
| **Bytes Per Sec** (`bytesPerSec`) | `0` | 达到阈值后 fallback 流量速度的上限（字节/秒）。`0` — 无限制（关闭该方向）。 |
| **Burst Bytes Per Sec** (`burstBytesPerSec`) | `0` | 在恒定速率之上用于短时突发的余量（token-bucket 的大小）。若小于 **Bytes Per Sec**，则上调至其值。 |

同处还增加了 **Master Key Log** (`masterKeyLog`) 字段 — 以 `SSLKEYLOGFILE` 格式写入 TLS master key 的路径，供在 Wireshark 中调试；生产环境应留空。

### 7.5. 实用配置建议

1. **VLESS + Reality（推荐）：** 创建一个网络为 `tcp` 的 VLESS inbound，在「安全」选项卡中选择 **Reality** — 面板会自行填入随机的 `target`/SNI、`shortIds` 并生成 X25519 密钥。如有需要，点击「获取新证书」获取你自己的一对密钥。对于 VLESS 客户端，启用 **Flow** = `xtls-rprx-vision`（XTLS Vision）— 这能带来最高的性能和隐蔽性。

**示例：最终的客户端链接 VLESS + Reality + Vision。** 面板为这样的 inbound 输出的邀请链接如下所示（密钥/ID 的值仅作示意）：

```text
vless://uuid-клиента@1.2.3.4:443?type=tcp&security=reality&pbk=ПУБЛИЧНЫЙ_КЛЮЧ&fp=chrome&sni=www.nvidia.com&sid=6ba85179e30d4fc2&spx=%2F&flow=xtls-rprx-vision#my-reality
```

这里 `pbk` — X25519 公钥，`sni` — 来自 **目标** 的借用域名，`sid` — **Short IDs** 之一，`flow=xtls-rprx-vision` — 已启用的 XTLS Vision。
2. **使用自有域名的 TLS：** 选择 **TLS**，在 **SNI** 中填写域名，添加证书（通过文件路径或内容），或者如果域名和证书已在「设置 → 安全」中配置，则点击「设置面板证书」。保留 **最小/最大版本** = `1.2`–`1.3`，**uTLS** = `chrome`，以伪装成普通浏览器。
3. 不要对向外开放的 inbound 保留 **无** 模式 — 只在本地 fallback 目标（`127.0.0.1`）或由外部代理提供 TLS 时才使用它。
4. 来自界面的提示：对大多数高级字段都有提示「*建议保留默认设置*」 — 仅在理解后果时才更改它们。

---

## 8. 客户端

客户端就是一个 VPN 用户账户：一组凭据（UUID 或密码），绑定到一个或多个 inbound，拥有自己的流量配额、有效期和并发连接限制。在本分支中，客户端是一个独立的实体（`clients` 表）：同一个客户端可以同时绑定到多个 inbound，并共享同一个 UUID/密码以及共享的流量计数器。**客户端** 部分会显示面板中的所有账户，不受 inbound 限制，并支持搜索、筛选、排序和批量操作。

### 8.1. 客户端字段

下面逐一说明 **添加客户端** / **修改客户端** 编辑器中的每个字段。

客户端表单分为两个选项卡：**基本**（email、绑定到 inbound、限额、有效期、组、注释、反向标签）和 **凭据**（UUID/密码/auth、Flow、VMess Security）。在字段标签中，配额标注为 **流量限额（GB）**，有效期标注为 **时长（天）** 和 **自动续期（天）**；**流量限额（GB）** 和 **IP 限制** 字段带有提示，说明 `0` 表示「无限制」。在编辑已有客户端时，生成随机 email 的按钮会被隐藏，而 IP 日志按钮则直接放到 **IP 限制** 字段旁边，并显示已记录的地址数量。

| 字段 | JSON 键 | 默认值 | 描述 |
|------|-----------|--------------|----------|
| Email | `email` | —（必填） | 客户端的唯一标识符 |
| UUID | `id` | 自动生成 | VMess/VLESS 的标识符 |
| 密码 | `password` | 自动生成 | Trojan/Shadowsocks 的密码 |
| 授权 | `auth` | 自动生成 | Hysteria 的密码 |
| Flow | `flow` | 空 | Flow control（XTLS），仅 VLESS |
| VMess Security | `security` | `auto` | VMess 加密方法 |
| IP 限制 | `limitIp` | `0`（无限制） | 最大并发 IP 数 |
| 已发送/接收总计（GB） | `totalGB` | `0`（无限制） | 流量配额 |
| 有效期 | `expiryTime` | `0`（永久） | 到期日期 |
| 自动续期 | `reset` | `0`（关闭） | 流量重置周期，天 |
| Telegram 用户 ID | `tgId` | `0`（无） | 数字 Telegram ID |
| 订阅 ID | `subId` | 自动生成 | 订阅标识符 |
| 组 | `group` | 空 | 逻辑分组标签 |
| 注释 | `comment` | 空 | 任意备注 |
| 已启用 | `enable` | `true` | 账户是否处于激活状态 |

#### Email（标识符）

**Email** 字段是客户端的主要且必填的标识符。尽管名为 email，但它不一定是邮件地址：任何文本标签（用户名、编号）都可以。该值在面板范围内必须 **唯一**；尝试创建第二个使用已占用 email 的客户端会被拒绝（`email already in use`），除非 `subId` 也相同（此时会被视为同一客户端的绑定）。

Email **不能留空**（`client email is required`），并且 **不能包含空格、字符 `/`、`\` 和控制字符**（「Email 不能包含空格、'/'、'\' 或控制字符」）。Email 参与流量统计、IP 日志、在线列表以及操作名称——不建议事后更改它。

#### UUID / 密码 / 授权（凭据）

具体使用哪个凭据字段取决于客户端所绑定 inbound 的协议。如果字段留空，值会自动填充：

- **UUID**（`id` 字段）——用于 **VMess** 和 **VLESS** 协议。如果未设置，则生成一个随机 UUID v4。
- **密码**（`password` 字段）——用于 **Trojan** 和 **Shadowsocks**。对于 Trojan，默认生成一个去掉连字符的 UUID。对于 Shadowsocks，会根据 inbound 的加密方法生成对应长度的 Base64 密钥：`2022-blake3-aes-128-gcm` 为 16 字节，`2022-blake3-aes-256-gcm` 和 `2022-blake3-chacha20-poly1305` 为 32 字节；其他方法则为去掉连字符的 UUID。如果手动输入的密钥不符合 2022-blake3 方法，它会被生成的密钥替换。
- **授权**（`auth` 字段）——**Hysteria** 的密码。默认为去掉连字符的 UUID。

由于一个客户端可以绑定到不同协议的 inbound，因此客户端记录中可能同时存在 UUID、密码和 auth——每种协议使用各自的字段。

**示例：客户端凭据在不同 inbound 的 `settings` 中的样子。** 同一个客户端在 VLESS inbound 中通过 `id` 标识，在 Trojan 中通过 `password` 标识，在 Shadowsocks 中通过 `password`（Base64 密钥）标识：

```json
// VLESS inbound 的 settings.clients 片段
{ "id": "b831381d-6324-4d53-ad4f-8cda48b30811", "email": "user-a", "flow": "xtls-rprx-vision" }

// 同一客户端在 Trojan inbound 中
{ "password": "b831381d63244d53ad4f8cda48b30811", "email": "user-a" }

// 同一客户端在 Shadowsocks inbound 中（方法 2022-blake3-aes-256-gcm）
{ "password": "GPyOaA3f7CO0az53eaQ8eqMfRDjmBlOh7v1u3+Z+pHk=", "email": "user-a" }
```

#### Flow

**Flow**（`flow` 字段）——XTLS 流控。**仅适用于 VLESS**，且仅当 inbound 配置为 XTLS Vision 时：VLESS 基于 **TCP** 传输，security 为 **`tls`** 或 **`reality`**。允许的值是 `xtls-rprx-vision`（以及历史值 `xtls-rprx-vision-udp443`）；空值表示无 flow。

如果 inbound 不支持 XTLS-flow，所设置的 flow 在保存客户端时会被 **静默清空**：对于绑定到多个 inbound 的同一客户端，flow 仅在允许的地方应用。仅当你专门使用 VLESS-Vision 时才需要更改它。

#### VMess Security

**VMess Security**（`security` 字段）——VMess 载荷的加密方法。默认值是 `auto`（由 Xray 自行选择加密算法）。允许的值是 VMess 标准值：`auto`、`aes-128-gcm`、`chacha20-poly1305`、`none`、`zero`。其他协议不使用该字段。

#### IP 限制（并发连接）

**IP 限制**（`limitIp` 字段）——客户端可同时连接的 **不同 IP 地址** 的最大数量。默认值是 `0`，表示 **无限制**。当值为正数时，面板会跟踪客户端的活跃 IP，并在超出限制时通过后台任务禁用该账户。（从 **3.3.1** 起，IP 计数通过 Xray 内核的 online-stats API 进行，**不再需要** 访问日志；在旧版内核上，面板会退回到读取访问日志，此时必须启用访问日志。）使用它可以禁止将一个订阅分享到多台设备：例如 `2` 表示允许两台设备。

IP 限制通过 **Fail2ban** 实现，因此只有在安装并正常运行 Fail2ban 时 **IP 限制** 字段才可用（面板通过 `GET /panel/api/server/fail2banStatus` 检查其状态）。如果未安装 Fail2ban，客户端编辑器（以及批量添加表单）中的该字段会被禁用，将鼠标悬停时会显示提示，建议从 `x-ui` 的 bash 菜单安装 Fail2ban（「Fail2ban is not installed, so the IP limit cannot be enforced. Install Fail2ban from the x-ui bash menu to enable this option.」）；在 Windows 上提示会说明那里无法使用 Fail2ban（「Fail2ban is not available on Windows, so the IP limit cannot be enforced.」），如果该功能在服务器上被禁用——则显示「The IP limit feature is disabled on this server.」。在更新面板时，对于没有 Fail2ban 的服务器上的客户端，已保存的 IP 限制会被一次性迁移清零，因为它在那里本来就不会生效。

**值示例。** `limitIp: 0`——无限制；`limitIp: 1`——严格地同时仅一台设备；`limitIp: 3`——最多三个不同 IP。当出现第四个活跃 IP 时，后台任务会禁用该客户端（`enable = false`），直到你执行 **重置 IP 限制**。

相关操作：**IP 日志** 显示客户端已记录的 IP 列表；每条记录除 IP 本身外，还包含最后一次访问的时间以及连接所记录到的节点标签（`@ 节点名`）——在多面板配置中，可以看到客户端是通过哪个节点连接的。**重置 IP 限制** 会清空累积的 IP 日志，使客户端无需等待记录自然过期即可再次连接。

#### 已发送/接收总计（GB）——流量配额

**已发送/接收总计（GB）**（`totalGB` 字段）——总流量配额（发送 + 接收）。默认值 `0` 表示 **无限制**。当达到配额（`up + down >= total`）时，客户端被视为 **已耗尽**（depleted）并被禁用。在 UI 中通常以吉字节为单位输入；在数据库中以字节存储。

在客户端列表中，**流量** 列显示一条彩色的使用进度条：已消耗的流量、限额标记（无限制时显示 ∞ 符号）以及悬停时显示的提示，其中细分了已发送/已接收和剩余量。手机上的客户端卡片中也会显示相同的紧凑指示器。

#### 有效期（Expiry）

**有效期**（`expiryTime` 字段）设置账户的到期时刻。该字段有三种模式：

- **永久**——`0`。客户端永远不会因时间而到期。
- **具体日期**——正的 Unix 时间戳（单位毫秒）。到期时（`expiryTime <= 现在`），客户端被视为已过期（expired）并被禁用。在 UI 中通常通过选择日期或以天数（**时长**，单位 **天**）设置。
- **首次使用后开始**——**负值**，编码了一段时长。在客户端尚未传输任何字节之前，有效期保持为负数（「延迟开始」）。在流量统计的第一个时间点上，面板会将其转换为绝对日期：`现在 + |时长|`。这样就可以销售例如「自首次连接起 30 天」的套餐，而无需提前知道客户端何时激活。转换按 email 只执行一次，以便所有绑定的 inbound 都获得相同的有效期。

**有效期编码示例。** 固定日期 2026 年 3 月 1 日 00:00 UTC → `expiryTime: 1772323200000`（正的毫秒时间戳）。「自首次连接起 30 天」→ `expiryTime: -2592000000`（负值，`30 × 24 × 60 × 60 × 1000`）；在第一个字节流量时，面板会将其替换为 `现在 + 2592000000`。永久 → `expiryTime: 0`。

#### 自动续期（客户端流量重置周期）

**自动续期** 字段（`reset` 字段）是以天为单位的自动续期/重置周期。提示：「到期后自动续期。（0 = 关闭）（单位：天）」。

- `0`——自动续期 **关闭**（默认值）。有效期到期后，客户端只是变为已耗尽。
- `> 0`——后台任务在有效期到期时 **将流量计数器重置为零**（`up = down = 0`），**将有效期向前推移** `reset` 天（如有需要，可推移多个周期，直到新的有效期落在未来），并在必要时再次 **启用** 客户端。这实现了周期性订阅（例如按月）。自动续期 **不适用于节点上的 inbound**（`node_id IS NOT NULL`）。

一个重要的结果：在批量删除操作中，`reset > 0` 的客户端会被 **排除** 在「已耗尽」概念之外——它们的流量/有效期理应由自动续期清零，而不应使账户成为删除候选。

#### Telegram 用户 ID

**Telegram 用户 ID**（`tgId` 字段）——用户的数字 Telegram 标识符，用于绑定到面板内置的 Telegram 机器人（通知、自行查看统计信息）。提示：「数字 Telegram 用户 ID（0 = 无）」。默认值 `0` 表示未绑定。可以按该字段筛选（**有** / **无**）。

#### 订阅 ID（subId）

**订阅 ID**（`subId` 字段）——客户端被纳入 **订阅**（subscription）时所使用的标识符。所有具有相同 `subId` 的客户端都通过同一个订阅链接提供。如果创建时该字段留空，面板会 **自动生成一个随机的** `subId`（UUID）。该值在使用其他 email 的客户端之间必须 **唯一**（`subId already in use`），并遵循与 email 相同的字符限制（「订阅 ID 不能包含空格、'/'、'\' 或控制字符」）。

没有 `subId`，客户端就无法使用订阅链接（「该客户端没有 subId，无法使用共享链接。」）。

#### Links 选项卡（外部链接和订阅）

除了 **基本** 和 **凭据** 选项卡，客户端编辑器中还有第三个选项卡 **Links**（提示：「Add third-party share links and remote subscription URLs to include in this client's subscription.」）。在其中通过 **Add External Link** 按钮添加第三方分享链接（`vless://`、`vmess://`、`trojan://`、`ss://`、`hysteria2://`、`wireguard://`），通过 **Add External Subscription** 按钮添加远程订阅的 URL（例如 `https://provider.example/sub/…`）。

上述所有内容都会被混入该客户端的订阅输出中（raw、JSON 和 Clash 格式）：链接按原样添加，而远程订阅则由面板定期下载（带缓存和短超时）并将其配置与自身配置合并。这样，在一条客户端订阅链接中，就可以连同自己的服务器一起提供外部配置。

#### 组

**组**（`group` 字段）——用于将相关客户端归并在一起的逻辑标签。提示：「用于对相关客户端进行分组的逻辑标签（例如团队、客户、地区）。可从工具栏筛选。」，占位符为「例如 customer-a」。该字段为可选（默认为空）。可以按组筛选列表并执行批量操作；要清除客户端的标签，请使用 **取消分组** 操作。

也可以直接在单个客户端的编辑器中取消组：如果清空 **组** 字段并保存，标签会被正确移除，客户端不再显示在之前的组下。

#### 注释

**注释**（`comment` 字段）——供管理员使用的任意文本备注（默认为空）。内容会进入搜索，并可用于筛选（**有** / **无** 注释）。

#### 已启用

**已启用**（`enable` 字段）——账户激活状态标志。默认 **已启用**（`true`）；创建时即使未传递该标志，面板也会强制设为 `true`。被禁用的客户端（`enable = false`）无法连接，在汇总中归入 **未激活**（deactive）类别。面板会自动禁用那些已耗尽配额、已过期或超出 IP 限制的客户端。

#### 只读字段

客户端卡片中还会显示一些服务性字段：**创建时间**（`created_at`）和 **更新时间**（`updated_at`）——创建和最后修改的时间戳，自动填充且不可编辑。**反向标签** 字段（`reverse`）——用于简单 VLESS 反向代理的可选 Reverse tag（「可选的 Reverse tag」）。

### 8.2. 绑定到 inbound

每个客户端必须至少绑定到一个 inbound——创建时至少需要一个（`at least one inbound is required`）。在编辑器中，这是 **绑定的入站** 字段，提示为 **选择一个或多个入站**。

- **绑定**——将客户端添加到选定的 inbound（相同的 UUID/密码和共享流量）。现有绑定会保留。
- **解绑**——将客户端从选定的 inbound 中移除。客户端记录本身会保留（如需彻底删除，请使用 **删除**）。客户端未绑定的组合会被静默跳过。

在保存绑定到多个 inbound 的客户端时，与具体协议/传输不兼容的字段（例如 VLESS-Vision 之外的 Flow）会自动针对每个 inbound 调整为允许的值。

在 inbound 选择列表上方（在客户端表单中、批量添加客户端时以及批量绑定/解绑窗口中）有 **全选** 和 **清空** 按钮。在这些列表中，每个 inbound 如果设置了备注（remark）就用备注标注，否则用 inbound 的标签标注。

### 8.3. 对客户端的操作

对于单个客户端（通过 **客户端信息** 卡片或 **操作** 上下文菜单），可执行以下操作：

#### 查看信息、二维码和链接

- **客户端信息**——包含所有字段、已用/剩余流量（**剩余**）、有效期和绑定的 inbound 的卡片。

通过 API 查询客户端（`GET /panel/api/clients/get/:email`）时，除 `client` 和 `inboundIds` 字段外，还会额外返回 `usedTraffic`——实际消耗的流量（发送 + 接收，已计入节点数据），这便于将消耗量与配额 `totalGB` 进行对照。
- **二维码** 和 **链接**——用于导入到客户端应用的客户端配置链接。基于所有绑定的、支持该协议的 inbound 生成（`GET /links/:email`）。如果没有合适的链接：「没有可共享的链接——请先将客户端绑定到一个支持协议的入站。」。
- **订阅链接**——基于 `subId` 的订阅 URL（`GET /subLinks/:subId`）。仅当客户端有 `subId` 且订阅服务在 **面板设置 → 订阅** 中已启用时可用（否则显示「订阅服务已禁用。」）。此外还会提供 **JSON 订阅 URL**。

#### 重置流量

**重置流量**（`POST /resetTraffic/:email`）将指定客户端的发送/接收计数器（`up`、`down`）清零。配额（`totalGB`）和有效期 **不受影响**——仅清零已使用的量。提示框：「流量已重置」。如果客户端未绑定到任何 inbound：「请先将该客户端绑定到一个入站。」。

**重置流量** 按钮也可从客户端编辑表单中使用——位于底部面板，**取消** / **保存** 旁边（重置前会请求确认）。如果客户端因流量耗尽而被禁用，重置（无论单个还是批量）都会自动再次 **启用** 它（`enable = true`），并立即将此更改下发到节点——不再需要在主控和节点上手动重新启用客户端。

#### 重置 IP 限制

清空客户端累积的 IP 日志（`POST /clearIps/:email`），以解除因超出并发连接限制而产生的临时封禁。提示框：「日志已清空」。

#### 删除

**删除**（`POST /del/:email`）——彻底删除客户端。确认对话框：标题「删除客户端 {email}？」，正文「客户端将从所有绑定的入站中删除，其流量记录将被销毁。此操作无法撤销。」。删除会将客户端从 **所有** inbound 中移除并销毁其流量记录。提示框：「客户端已删除」。

### 8.4. 批量操作

在客户端列表中可以勾选多条记录（**全选**、**全部清空**）；计数器显示「已选 {count}」。对于选定的记录可执行：

- **删除 ({count})**（`POST /bulkDel`）——批量删除。确认：「删除 {count} 个客户端？」、「每个被选中的客户端都将从所有绑定的入站中删除，其流量记录将被销毁。此操作无法撤销。」。提示框：「已删除客户端：{count}」，部分失败时显示「已删除：{ok}，失败：{failed}」。
- **修改 ({count})** / **调整**（`POST /bulkAdjust`）——批量修改有效期和/或配额。对话框「修改 {count} 个客户端」，提示「正值表示增加，负值表示减少。具有无限期或无限流量的客户端会在相应字段上被跳过。」。字段：**增加天数** 和 **增加流量（GB）**。逻辑：
  - **有效期：** 永久有效期（`expiryTime == 0`）的客户端会被跳过（「unlimited expiry」）；对于有日期的客户端，有效期按指定天数推移；对于处于「首次使用后开始」模式（负有效期）的客户端，调整其等待时长。超出剩余量的减少操作会被跳过（「reduction exceeds remaining time/delay window」）。
  - **流量：** 无限流量（`totalGB == 0`）的客户端会被跳过（「unlimited traffic」）；否则配额按指定量调整，且不低于零。
  - 如果天数和流量都未指定：「请在应用前指定天数或流量。」。提示框：「已修改：{count}」 / 「已修改：{ok}，已跳过：{skipped}」。

**示例：将选定客户端延长 30 天并增加 50 GB。** 在 **修改** 对话框中填写 **增加天数** = `30`，**增加流量（GB）** = `50`。反之，要减少一周并削减 10 GB 配额，请输入负值：**增加天数** = `-7`，**增加流量（GB）** = `-10`（在相应字段上为永久有效期或无限流量的客户端会被跳过）。
- **绑定 ({count})** / **解绑 ({count})**（`POST /bulkAttach` / `bulkDetach`）——将选定客户端批量绑定/解绑到选定的 inbound。目标仅限多用户 inbound。解绑结果：「已解绑 {detached}，已跳过 {skipped}。」。
- **Sub 链接 ({count})**——选定客户端的订阅 URL 和 JSON 订阅的汇总表格，带 **全部复制** 按钮。如果都没有 subId：「所选客户端中没有任何一个具有订阅 ID。」。
- **添加到组** 和 **取消分组**——设置和移除组标签。

#### 按状态重置流量和删除

- **重置所有客户端流量**（`POST /resetAllTraffics`）——将面板中 **所有** 客户端的 `up`/`down` 计数器清零。确认：「重置所有客户端的流量？」 和 「所有客户端的发送/接收计数器都将重置为零。配额和有效期不受影响。此操作无法撤销。」。提示框：「所有客户端流量已重置」。
- **删除已耗尽的**（`POST /delDepleted`）——删除所有 **配额已耗尽**（`total > 0 and up + down >= total`）**或有效期已过**（`expiry_time > 0 and expiry_time <= 现在`）的客户端，前提是 `reset = 0`（带自动续期的客户端不会被触碰）。确认：「删除已耗尽的客户端？」、「将删除所有配额流量已耗尽或有效期已过的客户端。此操作无法撤销。」。提示框：「已删除已耗尽客户端：{count}」。

#### 导出、导入和删除未绑定客户端

当未选中任何项时，在 **客户端** 页面的 **更多** 菜单中提供三个操作。

**导出客户端**（`GET /clients/export`）会打开一个查看器，显示所有客户端的 JSON 列表，格式为 `{client, inboundIds}`，带复制和下载按钮（文件 `clients-export.json`）。**导入客户端**（`POST /clients/import`）会打开一个编辑器，将相同格式的 JSON 粘贴进去并点击 **Import**：带 `inboundIds` 的客户端会被创建并绑定到 inbound，无绑定的客户端会作为独立的「裸」记录恢复，而已存在的 email **永远不会被覆盖**——它们会被列入跳过列表。提示框：「{count} clients imported」、「{ok} imported, {failed} skipped」。

**删除未绑定客户端**（`POST /clients/delOrphans`）——一项危险操作：删除所有未绑定到任何 inbound 的客户端，连同其流量记录、IP 日志和外部链接一并删除。确认：「Delete clients without an inbound?」、「Removes every client that is not attached to any inbound, along with its traffic record. This cannot be undone.」。提示框：「{count} unattached clients deleted」。该操作不可逆。

### 8.5. 搜索、筛选和排序

列表上方有一个搜索框（「搜索 email、注释、sub ID、UUID、密码、auth…」）——它会按 email、注释、subId、UUID、密码和 auth 搜索。结果计数器：「显示 {total} 中的 {shown} 个」。

客户端列表会自动刷新：面板每隔几秒拉取一次当前页的最新数据，因此新连接的客户端和变化的排序顺序无需手动刷新即可出现（后台轮询时加载指示器不会闪烁）。

**客户端筛选** 面板允许按状态（类别）、协议、绑定的 inbound、有效期范围、已用流量范围、是否有自动续期（**有/无**）、是否有 Telegram ID 和注释，以及按组进行筛选。在带节点的面板上会出现 **节点** 多选框：可以将列表限制为选定节点的客户端；单独的 **本地面板** 选项筛选未绑定到节点的 inbound 的客户端（该筛选器仅在存在节点时可见）。排序：**最旧/最新优先**、**最近更新**、**最近在线**、**Email A→Z / Z→A**、**流量较多**、**剩余较多**、**即将到期**。

### 8.6. 图标和状态

状态优先级：已耗尽/已过期 → 未激活 → 即将到期 → 激活。

- **在线** / **离线**——具有活跃连接（出现在当前在线列表中）且 **已启用** 的客户端。在线列表通过单独的请求更新（`/onlines`、`/onlinesByGuid`）。
- **已耗尽**（depleted）——配额已用完（`up + down >= totalGB`）**或** 有效期已过（`expiryTime <= 现在`）。此类客户端会自动被禁用，并受 **删除已耗尽的** 操作影响。
- **即将到期 / 即将结束**（expiring）——已启用的客户端，其距离到期不足阈值间隔 **或** 距离配额耗尽不足阈值量（阈值在面板设置中设定）。如果客户端已耗尽/已禁用，则不计入。
- **未激活**（deactive）——`enable = false` 的客户端（被手动或后台任务禁用）。
- **激活**（active）——已启用、未耗尽、有效期未过且距离阈值尚远。

---

## 9. 客户端分组

> 这是本 3X-UI 分支的一项功能。在原版 3x-ui（MHSanaei）项目中并没有「客户端分组」这一概念——这里新增了独立的分组表、面板菜单中的**分组**页面以及相应的 API 方法。如果你将配置迁移到原版 3x-ui，分组标签将不会在任何地方被处理。

### 9.1. 什么是客户端分组以及为什么需要它

**分组**是一个具名的逻辑标签（label），可以贴到一个或多个客户端上。它不会创建新的连接方式，也既不是 inbound 也不是节点——它纯粹是一个组织性的标记，便于按它来筛选客户端并进行批量处理。

本分支客户端模型的核心思想是：**客户端是一个顶层实体，通过 email 标识**（`clients` 表中的 `email` 字段拥有唯一索引）。同一个客户端（拥有相同凭据的同一个 email）可以同时属于多个 inbound，甚至同时存在于多个节点上，包括使用不同协议。分组标签**每个客户端只存储一次**，因此它会自动应用到该客户端在所有 inbound 中的全部绑定上。

分组标签是用于分组的逻辑标记：

| 层级 | 存储位置 | 字段 |
|------|--------------|------|
| 客户端记录（数据库） | `clients` 表 | `group_name`（默认为空字符串 `''`） |
| 分组字典（数据库） | `client_groups` 表 | `name`（唯一索引，非空） |
| inbound 设置（Xray） | JSON `settings.clients[].group` | 在该客户端所属的每个 inbound 的每个客户端对象中重复存放 |

实际中为什么需要它：

- **一个客户端跨多个 inbound/节点。** 如果一个客户端被「售卖」为同时访问多个 inbound（例如不同协议或不同节点），分组就能把它作为一个整体来管理：重置流量、删除、重命名标签——通过一次操作就能作用于它的所有 inbound。
- **批量操作与筛选。** 在**客户端**页面上，列表可以按分组筛选；在**分组**页面上，可对分组的全部成员执行批量操作。
- **管理大量客户端。** 像 `vip`、`trial`、`team-A` 这样的标签有助于把成千上万的客户端归入逻辑上的「篮子」，而无需为此增设单独的 inbound。

### 9.2. 分组与客户端、inbound、节点和协议的关系

这是理解上最重要的一个小节，因为标签的同步并不简单。

**分组描述的是客户端，而不是 inbound。** 标签存在于客户端记录中（`clients.group_name`）。当客户端被绑定到多个 inbound 时，任何一次分组变更，面板都会遍历该客户端所属的**所有** inbound，并在它们的 Xray 设置（`settings.clients[]`）中设置/移除 `group` 字段。技术上的实现方式是：通过客户端的 email 找到它所属的所有 inbound，然后在每个这样的 inbound 的 JSON 设置中修改对应该 email 的客户端对象。因此：

- 分组**与协议无关。** 同一个 email 可以在一个 inbound 中是 VLESS 客户端，在另一个 inbound 中是 Hysteria 客户端——它的分组标签仍然只有一个，并会应用到两者上（同时每个协议各自的凭据是独立的，分别保存）。
- 分组**覆盖节点。** 属于节点的 inbound 与主面板的 inbound 区别在于 `nodeId` 字段（主面板 inbound 的该字段为 `null`/`0`）。分组标签会应用到 inbound 中的客户端对象，无论它是主面板 inbound 还是节点 inbound——只要其中存在使用该 email 的客户端即可。

**分组标签对来自节点的同步以及对设置重建都具有稳定性。** 这一行为是特意设计的：

- 当节点发送流量快照时，它的数据**不会覆盖**面板数据库中客户端的本地 `group_name` 和 `comment`。分组和备注被视为「面板本地」字段——节点不管理它们。
- 在重建 inbound 设置时，传入数据中 `group` 的空值**不会重置**已保存的标签。分组正是通过**分组**页面来管理（而不是通过编辑 inbound 的 Xray 设置），因此在普通的设置重建中，「空分组」被解释为「不动它」，而不是「清空」。

实践结论：唯一会**有意清空**标签的操作是删除分组以及将客户端显式移出分组（见下文）。普通的 inbound 编辑或与节点的后台同步都不会丢失分组。

### 9.3. 分组字典与「空」分组

页面上的分组列表由两个来源合并而成：

1. **派生分组（derived）**——客户端身上实际出现的所有非空 `group_name` 值，并附带客户端数量统计。
2. **已保存分组（stored）**——来自 `client_groups` 表的记录。

这种合并带来一个重要效果：分组可以**在没有任何客户端的情况下**存在。这样的分组通过显式的「添加分组」按钮创建（在 `client_groups` 中写入记录），并在列表中以计数 `0` 显示。这些记录被视为**空分组**。列表始终按名称不区分大小写排序。

页面上的汇总计数：

| 字段（RU） | 显示内容 |
|-----------|----------------|
| Всего групп | 分组总数（已保存和派生的合计）。 |
| Клиенты с группой | 有非空分组标签的客户端数量。 |
| Пустые группы | 没有客户端的分组数量（计数为 `0`）。 |
| Клиентов в группе | 某个具体分组中的客户端数量（表格列）。 |

### 9.4. 分组的字段与列

`client_groups` 表中的一条分组记录包含：

| 字段 | 类型 | 默认值 | 描述 |
|------|-----|--------------|----------|
| `Id` | int | 自增 | 分组记录的主键。 |
| `Name` | string | —（必填） | 分组名称。唯一索引，不能为空。在 UI 中为**名称**列。 |
| `CreatedAt` | int64（毫秒） | 创建时间 | 分组记录的创建时刻。 |
| `UpdatedAt` | int64（毫秒） | 修改时间 | 最后一次修改的时刻。 |

页面表格中至少显示**名称**和**分组内客户端数**两列，以及操作按钮（见下文）。

### 9.5. 创建分组

按钮**添加分组**。

步骤：
1. 点击**添加分组**。
2. 输入分组名称。
3. 确认。

后端行为（`POST /panel/api/clients/groups/create`，请求体 `{"name": "..."}`）：
- 名称会去除两侧空白。空名称会被拒绝并报错「group name is required」。
- 如果已存在同名分组——报错「group already exists」。
- 成功时在 `client_groups` 中创建一条记录（最初没有客户端——即空分组）。

成功消息：**「分组「{name}」已创建。」**

**示例：通过 API 创建空分组。** 在客户端填充之前先准备好一套标签：

```bash
curl -s 'https://panel.example.com:2053/panel/api/clients/groups/create' \
  -H 'Content-Type: application/json' \
  -b cookie.txt \
  -d '{"name": "vip"}'
```

成功时的响应：

```json
{ "success": true, "msg": "Группа «vip» создана.", "obj": null }
```

用同一名称再次调用将返回 `"success": false` 和消息 `group already exists`。

> 提前创建空分组很方便，当你想先准备好一套标签，然后通过「添加客户端…」往里填充客户端时尤其如此。

### 9.6. 重命名分组

按钮**重命名**，对话框标题为**「重命名 {name}」**。

行为（`POST /panel/api/clients/groups/rename`，请求体 `{"oldName": "...", "newName": "..."}`）：
- 两个名称都会去除两侧空白。旧名称为空——报错「old group name is required」，新名称为空——报错「new group name is required」。
- 如果新名称与旧名称相同——不做任何操作（影响 `0` 个客户端）。
- 否则原子地执行重命名：
  - 重命名 `client_groups` 中的记录；
  - 所有 `group_name = oldName` 的客户端，其字段更新为 `newName`；
  - 在受影响客户端所属的**所有 inbound**（包括节点上的）中，Xray 设置里的 `group` 值由旧值改为新值。
- 重命名后，面板将 Xray 标记为需要重启，并发出客户端变更通知。

消息：
- 成功：**「已为 {count} 个客户端重命名分组。」**
- UI 中的名称冲突：**「名为「{name}」的分组已存在。」**

### 9.7. 向分组添加客户端

按钮**添加客户端…**，标题为**「向分组「{name}」添加客户端」**。

对话框中的逐字提示：

> 「选择要添加到此分组的客户端。现有的 inbound 绑定会保留；只更改分组标签。已属于此分组的客户端不会显示。」

如果没有可添加的对象，会显示**「没有其他可添加的客户端。」**

行为（`POST /panel/api/clients/groups/bulkAdd`，请求体 `{"emails": [...], "group": "..."}`）：
- 分组名称必填（否则报错「group name is required」）；空的 email 列表——操作不做任何事。
- 如果该分组在 `client_groups` 和派生分组中都尚不存在——它将被自动创建。
- 对所选 email 的客户端设置 `group_name = group`；**客户端与 inbound 的绑定不变**——只影响标签。然后在这些客户端的所有 inbound 中设置 `group` 字段。
- 返回受影响的客户端记录数量；Xray 被标记为需要重启。

成功消息：**「已向 {name} 添加 {count} 个客户端。」**

**示例：用一个请求给多个客户端打上分组标签。** 客户端通过 email 指定，与 inbound 的绑定不会因此改变：

```bash
curl -s 'https://panel.example.com:2053/panel/api/clients/groups/bulkAdd' \
  -H 'Content-Type: application/json' \
  -b cookie.txt \
  -d '{"emails": ["alice@example.com", "bob@example.com"], "group": "vip"}'
```

如果分组 `vip` 尚不存在，它将被自动创建。请求之后，这些客户端的记录中会被设置 `group_name = "vip"`，而它们每个 inbound 的 Xray 设置中，对应的客户端对象会获得 `"group": "vip"` 字段：

```json
{ "id": "6f1b...", "email": "alice@example.com", "group": "vip", "enable": true }
```

### 9.8. 将客户端移出分组（不删除客户端本身）

按钮**移除客户端…**，标题为**「将客户端移出分组「{name}」」**。

逐字提示：

> 「选择要从此分组移除的成员。客户端本身会保留（如需彻底删除，请使用「删除分组客户端」）。」

行为（`POST /panel/api/clients/groups/bulkRemove`，请求体 `{"emails": [...]}`）：技术上这等同于以空分组执行「添加到分组」。所选客户端的 `group_name` 被清空，其 inbound 的 Xray 设置中的 `group` 字段被删除。客户端本身及其与 inbound 的绑定保持不变。

成功消息：**「已将 {count} 个客户端从 {name} 移除。」**

### 9.9. 重置分组流量

按钮**重置流量**。

确认对话框：
- 标题：**「重置分组 {name} 的流量？」**
- 文本：**「这将把此分组中全部 {count} 个客户端的 up/down 清零。」**

行为：对分组所有成员的 email，在流量表中将 `up` 和 `down` 清零，并将 `enable` 字段设为 `true`（客户端被启用）。该操作在一个事务中分批执行。

成功消息：**「已重置 {count} 个客户端的流量。」**

### 9.10. 删除分组与删除分组客户端

页面上有**两个本质上不同的删除操作**——它们很容易混淆，因此区分至关重要。

#### 9.10.1. 删除分组（保留客户端）

按钮**「删除分组（保留客户端）」**。

对话框：
- 标题：**「删除分组 {name}？」**
- 文本：**「这将删除分组并清除 {count} 个客户端身上的分组标签。客户端本身不会被删除。」**

行为（`POST /panel/api/clients/groups/delete`，请求体 `{"name": "..."}`）：从 `client_groups` 中删除分组记录，清空其所有客户端的 `group_name`，并从它们的 inbound 中移除 `group` 字段。**客户端、其连接和流量都会保留。** Xray 被标记为需要重启。

成功消息：**「已清除 {count} 个客户端的分组。」**

#### 9.10.2. 删除分组客户端（彻底删除）

按钮**「删除分组客户端」**。

对话框：
- 标题：**「删除 {name} 中的所有客户端？」**
- 文本：**「这将连同流量记录一起不可逆地删除 {count} 个客户端。分组标签也会被清除。此操作无法撤销。」**

这是一项破坏性操作：它会删除客户端本身（通过按 email 批量删除，端点 `POST /panel/api/clients/bulkDel`），包括它们的流量记录，从而将它们从所有 inbound 中移除。

消息：
- 成功：**「已删除 {count} 个客户端。」**
- 部分结果：**「{ok} 已删除，{failed} 已跳过」**

> 如果分组为空，则无法对其成员执行操作——会显示**「此分组中暂无客户端。」**

### 9.11. 与「客户端」页面的关联

分组标签在**分组**页面之外也可见并被使用：

- 在客户端的精简记录中有 `group` 字段，因此客户端列表中会显示其所属分组。
- 客户端列表（`/panel/api/clients/list/paged`）接受筛选参数 `group`：可以传入一个名称，或用逗号分隔多个名称。匹配在该字段内按「或」的原则进行，不区分大小写。特殊情况：筛选分组列表中的空元素表示「无分组的客户端」（其 `group` 为空）。
- 在客户端页面的响应中会返回 `groups` 数组——现有分组名称的完整清单，以便 UI 构建筛选下拉列表。

**示例：按分组筛选客户端。** 该请求只返回带有 `vip` 或 `trial` 标签的客户端（多个名称——用逗号分隔，「或」）：

```
GET /panel/api/clients/list/paged?group=vip,trial
```

要获取**没有**分组的客户端，请在列表中传入一个空元素——例如筛选值 `group=`（空字符串）或 `group=vip,`（标签 `vip` 加上无分组的客户端）。

### 9.12. API 端点汇总

所有分组路由都挂载在 `/panel/api/clients` 下：

| 方法与路径 | 用途 | 请求体 |
|--------------|-----------|--------------|
| `GET /panel/api/clients/groups` | 列出分组及客户端计数 | — |
| `GET /panel/api/clients/groups/:name/emails` | 分组所有成员的 email（按 email 排序） | — |
| `POST /panel/api/clients/groups/create` | 创建空分组 | `{"name"}` |
| `POST /panel/api/clients/groups/rename` | 重命名分组 | `{"oldName","newName"}` |
| `POST /panel/api/clients/groups/delete` | 删除分组，保留客户端（清除标签） | `{"name"}` |
| `POST /panel/api/clients/groups/bulkAdd` | 向分组添加客户端（按 email） | `{"emails":[...],"group"}` |
| `POST /panel/api/clients/groups/bulkRemove` | 将客户端移出分组（清除标签） | `{"emails":[...]}` |
| `POST /panel/api/clients/bulkDel` | 彻底删除客户端（由「删除分组客户端」使用） | `{"emails":[...],"keepTraffic"}` |

**示例：通过 API 演示分组生命周期的典型场景。**

```bash
# 1. 创建标签 trial
curl -s .../panel/api/clients/groups/create   -d '{"name":"trial"}'

# 2. 把它贴到两个客户端上
curl -s .../panel/api/clients/groups/bulkAdd  -d '{"emails":["u1@example.com","u2@example.com"],"group":"trial"}'

# 3. 将所有成员的流量清零（email 取自 /groups/trial/emails）
curl -s .../panel/api/clients/groups/bulkRemove -d '{"emails":["u2@example.com"]}'

# 4. 删除分组但保留客户端（仅清除标签）
curl -s .../panel/api/clients/groups/delete   -d '{"name":"trial"}'
```

第 4 步会删除分组记录并清空其客户端的 `group_name`，但客户端本身、它们的连接和流量都会保留。要不可逆地删除客户端本身，则应改用 `bulkDel`。

会更改客户端标签的操作（`rename`、`delete`、`bulkAdd`、`bulkRemove`）会将 Xray 标记为需要重启，并发出客户端变更通知。

### 9.13. 按分组统计的流量

3.3.0 版本的新功能：在**分组**部分（「客户端」页面的分组管理选项卡），分组表格现在不仅显示每个分组中的客户端数量，还显示该分组的累计已用流量。该列标题为**「已用流量」**。

#### 该列显示的内容

对于每一行分组，会显示属于该分组的所有客户端的流量总和——即所有成员的 `up + down`（发出 + 接收的流量）相加。这能快速回答「整个分组总共下载/上传了多少」的问题，而无需逐个打开客户端并手动累加。

分组表格中并排显示的还有：

| 列 | 含义 |
|---|---|
| Имя | 分组名称 |
| Клиенты | 该分组标记了多少客户端（此列以前叫「分组内客户端数」） |
| Отправлено | 分组所有客户端的 `up` 总和（发出的流量） |
| Получено | 分组所有客户端的 `down` 总和（接收的流量） |
| Использованный трафик | 分组所有客户端的 `up + down` 总和 |

发出和接收的流量以独立的**已发送**和**已接收**两列显示，而**已用流量**列显示它们的总和。客户端数量这一列就叫**客户端**。

表格上方的汇总还会额外显示所有分组的聚合值——**「分组总数」**和**「有分组的客户端」**，并将总流量拆分为两张卡片：**「总发送 / 接收」**（带上/下箭头——分别为所有分组发出和接收的流量）和**「总流量」**（带图表图标——两者的合计）。

#### 如何计算

计算通过对客户端表的一条 SQL 查询完成，并连接（`LEFT JOIN`）流量统计表：

- 按分组标签字段（`group_name`）对客户端进行分组并统计其数量——这就是「分组内客户端数」；
- 流量取自连接表 `client_traffics` 中 `up + down` 的总和。也就是说，对每个客户端的发出字节（`up`）和接收字节（`down`）都进行累加；
- 由于 email 在客户端表和流量表中都是唯一的，连接不会重复计算同一客户端的流量。

数值的特点：

- **没有流量记录的客户端**会被计入成员计数，但对总和的贡献为 0，因此刚创建的分组显示流量为 `0`。
- **空分组**（已创建但没有客户端）也会出现在列表中，计数为零、流量为零：除了从客户端标签「派生」出的分组外，结果中还会掺入显式保存的分组，之后列表会按名称不区分大小写排序。
- 没有分组标签的客户端（`group_name` 为空）不计入统计。

#### 相关操作

从分组表格中仍然可以执行针对整个分组的操作，其中包括**「重置流量」**——将所选分组所有客户端的 `up`/`down` 清零。这样重置之后，该分组的「已用流量」列将显示为 `0`。

---

## 10. 订阅（Subscription）

订阅（subscription）是一种机制，它允许向客户端下发一个固定的链接（URL），VPN 客户端通过该链接自行下载并定期更新完整的配置集合。无需手动向用户逐个转发每个 inbound 的单独链接，而是给他一个统一地址，形如 `https://域名:端口/sub/<subId>`。面板会通过该地址实时汇集与该客户端关联的所有配置，并以客户端所需的格式返回。当服务器上的设置发生变化时（新地址、Reality 密钥轮换、新增 inbound），客户端会在下一次自动更新时获得最新配置，无需用户进行任何操作。

订阅由面板内部一个独立的 HTTP/HTTPS 服务器提供，它独立于 Web 面板启动，并监听自己的端口。这样做是出于安全考虑：可以对外开放订阅端口，而无需开放面板本身的端口。

### 10.1. 什么是 subId 以及链接如何生成

inbound 中的每个客户端都有 `subId` 字段（界面中为「订阅 ID」）。正是这个值充当订阅的键：面板会在所有 inbound 中查找 `subId` 与请求值相符的客户端，并把它们的配置合并为一个响应。

- 如果多个客户端（在同一个或不同的 inbound 中）设置了相同的 `subId`，它们的配置会汇入同一个订阅。这是把多台服务器/协议通过一个链接一次性下发给同一用户的常规方式。

**示例：一个用户——一个链接两台服务器。** 假设有两个 inbound（服务器 A 上的 VLESS 和服务器 B 上的 Trojan）。要用一个链接向用户下发两份配置，请给他的两个客户端设置相同的 `subId`：

```
Inbound 1 (VLESS):  email = ivan@vpn,  subId = ivan2025
Inbound 2 (Trojan): email = ivan@vpn,  subId = ivan2025
```

这样，通过地址 `https://sub.example.com:2096/sub/ivan2025`，面板会同时返回两份配置。之后再添加一个使用相同 `subId` 的第三个 inbound，它会在订阅的下一次自动更新时出现在用户处，无需转发新链接。
- 如果客户端的 `subId` 字段为空，则无法分享用于公共访问的链接。界面中会有提示指出这一点：「该客户端没有 subId，无法使用公共访问链接。」

#### 客户端的外部链接与订阅（「Links」选项卡）

客户端表单中有一个 **「Links」** 选项卡，可以为单个客户端附加额外的配置来源，这些来源会被混入它的订阅中（格式为 RAW、JSON 和 Clash）：

- **Add External Link** —— 第三方分享链接（`vless://`、`trojan://`、`ss://` 等）。原样添加到输出中，对于 JSON/Clash 还会额外解析为配置。
- **Add External Subscription** —— 外部订阅地址。面板会自行下载它（带缓存和较短的超时），并把获取到的配置并入客户端的总列表。

这便于在你的 inbound 之上，通过同一个统一链接向客户端下发额外的服务器。如果远端订阅的响应过大，它不再被静默截断：面板会返回错误，并继续使用上一次成功缓存的值。
- `subId` 的值不能任意设置：保存时会校验其中不含空格、`/`、`\` 字符和控制字符。对应的校验提示为：「订阅 ID 不能包含空格、'/'、'\' 或控制字符」。

最终链接构造为 `<base>/<subPath>/<subId>`（参见订阅服务器设置一节及「反向代理 URI」字段）。如果按 `subId` 找不到任何客户端（客户端已删除、`subId` 不存在），服务器返回不带正文的 HTTP 404。发生内部错误时——HTTP 500。VPN 客户端只依据响应码判断，因此错误正文是有意留空的。

#### 订阅中 inbound 链接的顺序

每个 inbound 都有 **「订阅中的顺序」** 字段（`subSortIndex`）——一个从 1 起的数字，用于指定该 inbound 的链接在订阅输出中的位置。较小的值排在前面；值相等时保持原始创建顺序（按 id）。该顺序应用于所有输出格式——纯文本、订阅页面、JSON 和 Clash。此字段不影响面板内 inbounds 本身的顺序。

该字段在 inbound 表单中分享地址（share address）设置旁边编辑，并按常规规则同步到节点。如果至少有一个 inbound 的顺序不为 1，Inbounds 列表中就会出现一个紧凑的 **「顺序」** 列。

### 10.2. 订阅服务器设置

所有订阅参数都位于面板设置的 **「订阅」** 选项卡中。下面逐一解析每个参数；括号中标注了内部设置键和默认值。

该部分本身又分为若干选项卡：**「面板设置」**、**「信息」**、**「配置文件」**、**「证书」**、**「Happ」** 和 **「Clash / Mihomo」**。订阅标题、支持 URL、配置文件页、公告和主题目录字段位于「配置文件」选项卡；Happ 和 Clash/Mihomo 的路由规则位于同名选项卡；订阅更新间隔位于「信息」选项卡。

#### 基本参数

| 字段（UI） | 键 | 默认值 | 说明 |
|---|---|---|---|
| 启用订阅 | `subEnable` | `true`（已启用） | 启动独立的订阅服务器。提示：「带独立配置的订阅功能」。如果关闭——订阅服务器不会启动，所有链接都无法工作。 |
| 监听 IP | `subListen` | 空 | 订阅服务器接受连接所用的 IP 地址。提示：「默认留空以监听所有 IP 地址」。 |
| 订阅端口 | `subPort` | `2096` | 订阅服务器的 TCP 端口。提示：「为订阅服务提供服务的端口号不应在服务器上被占用」——该端口必须空闲，且不与面板或 Xray 冲突。 |
| URI 路径 | `subPath` | `/sub/` | 提供普通订阅的路径。提示：「必须以 '/' 开头并以 '/' 结尾」。 |
| 监听域名 | `subDomain` | 空 | 允许访问订阅的域名（Host 校验）。提示：「默认留空以监听所有域名和 IP 地址」。如果设置了——则拒绝来自其他 Host 的请求。 |

**安全须知：** 默认路径 `/sub/`（以及 JSON 的 `/json/`）广为人知且容易被猜到。面板会显示警告：「默认订阅路径 "/sub/" 广为人知——请修改它。」JSON 也有类似提示。建议设置一个自定义的、不易被猜到的路径。

#### TLS / 证书

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| 订阅证书公钥文件路径 | `subCertFile` | 空 | 证书文件（`.crt`/`fullchain`）的完整路径。提示：「请输入以 '/' 开头的完整路径」。 |
| 订阅证书私钥文件路径 | `subKeyFile` | 空 | 私钥文件的完整路径。提示：「请输入以 '/' 开头的完整路径」。 |

如果两个路径都已设置且证书成功加载，订阅服务器会以 **HTTPS** 工作。如果字段为空或证书无法读取——服务器会回退到 **HTTP**（错误会写入日志）。是否存在有效的 TLS 也会影响基础 URL 的生成：当端口为 443 且带 TLS、或端口为 80 且不带 TLS 时，链接中会省略端口号。

#### 更新间隔

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| 订阅更新间隔 | `subUpdates` | `12` | 客户端应用重新请求订阅的频率（单位：小时）。提示：「客户端应用更新之间的间隔（单位：小时）」。 |

该值通过 HTTP 头 `Profile-Update-Interval` 传递给客户端；现代客户端将其作为配置自动更新的周期。

#### 响应中的格式与信息

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| 编码 | `subEncrypt` | `true` | 提示：「加密订阅中返回的配置」。从技术上讲这并非加密，而是对整个普通订阅正文进行 **Base64 编码**（大多数客户端期望的格式）。关闭时，链接以纯文本返回，每行一个。 |
| 显示使用信息 | `subShowInfo` | `true` | 提示：「在配置名称后显示剩余流量和到期日期」。启用时，会在每个配置的名称（remark）后追加剩余流量标记（📊）和有效期标记（例如 `5D,3H⏳`）；客户端已到期/不可用时显示 `⛔️N/A`。 |
| 在名称中包含 Email | `subEmailInRemark` | `true` | 提示：「在订阅配置名称中包含客户端的 email。」。把客户端的 email 加入配置的 remark 中。 |

#### 备注模板（Remark Template）

订阅中每个配置的显示名称（remark）按 **备注模板** 生成——位于订阅设置 **「信息」** 选项卡中的 **「备注模板」** 字段（`remarkTemplate`）。旧的备注模型构造器（单独选择 inbound/email/external proxy 各部分和分隔符）已从界面移除；现在你可以编写任意的名称格式并在其中插入变量。默认值为 `{{INBOUND}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D`。如果该字段留空，则采用旧的（无法通过界面配置的）备注模型。

变量按 **Client**、**Traffic** 和 **Time & status** 分组，并以可点击的 `{{VAR}}` 芯片形式显示在字段旁边，悬停时带提示；点击会把标记插入模板，并提供实时预览。每个变量都会在生成订阅时针对具体客户端单独替换。也允许使用单层括号的简化写法（`{DATA_LEFT}`、`{EXPIRE_DATE}`、`{PROTOCOL}`、`{TRANSPORT}` 等）——面板会自动把它转换为内部格式 `{{...}}`。

可用变量：

- **客户端标识：** `{{EMAIL}}`、`{{INBOUND}}`（inbound 自身的备注）、`{{HOST}}`（主机的备注）、`{{ID}}`（UUID）、`{{SHORT_ID}}`（UUID 的前 8 个字符）、`{{SUB_ID}}`、`{{COMMENT}}`、`{{TELEGRAM_ID}}`、`{{PROTOCOL}}`、`{{TRANSPORT}}`。
- **流量：** `{{TRAFFIC_USED}}`、`{{TRAFFIC_LEFT}}`、`{{TRAFFIC_TOTAL}}`（及其以精确字节计的 `*_BYTES` 变体）、`{{UP}}`、`{{DOWN}}`、`{{USAGE_PERCENTAGE}}`。
- **有效期与状态：** `{{DAYS_LEFT}}`、`{{TIME_LEFT}}`、`{{EXPIRE_DATE}}`（`YYYY-MM-DD`）、`{{JALALI_EXPIRE_DATE}}`（贾拉里历日期）、`{{EXPIRE_UNIX}}`、`{{CREATED_UNIX}}`、`{{RESET_DAYS}}`、`{{STATUS}}`（active / expired / disabled / depleted）、`{{STATUS_EMOJI}}`。

模板可以用竖线 `|` 分成若干段。某段中变量给出「无限」值（`∞`）时——例如无限制客户端的 `{{TRAFFIC_LEFT}}` 或 `{{DAYS_LEFT}}`——该段会被自动隐藏。此外，流量消耗和有效期的区块只显示一次，在客户端的第一个链接上，以免在每个配置中重复。

**示例。** 模板 `{{EMAIL}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D` 对于剩余 42 GB、还有 7 天的客户端，会生成形如 `ivan@vpn 📊42.00GB ⏳7D` 的名称，而对于无限制客户端——只是 `ivan@vpn`（带 `∞` 的段被省略）。
| 备注模板 | `remarkTemplate` | `{{INBOUND}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D` | 每个配置显示名称（remark）的自由模板，带 `{{VAR}}` 变量替换。生成订阅时针对每个客户端单独替换。旧的「备注模型」构造器（选择 inbound/email/external proxy 和分隔符）已从界面移除，仅在该字段留空时作为后备方案使用。详情——参见下文「备注模板（Remark Template）」。 |

#### 配置文件元数据（响应头）

这些字符串通过响应的 HTTP 头传递给客户端，并在 VPN 客户端中作为配置文件元数据显示。它们默认都为空。

| 字段（UI） | 键 | 头 | 说明 |
|---|---|---|---|
| 订阅标题 | `subTitle` | `Profile-Title`（以 Base64） | 「客户端在 VPN 客户端中看到的订阅名称」。对于 Clash 还通过 `Content-Disposition` 用作导入配置文件的名称。 |
| 支持 URL | `subSupportUrl` | `Support-Url` | 「在 VPN 客户端中显示的技术支持链接」。 |
| 配置文件 URL | `subProfileUrl` | `Profile-Web-Page-Url` | 「在 VPN 客户端中显示的你的网站链接」。如果未设置，则填入实际的订阅请求 URL。 |
| 公告 | `subAnnounce` | `Announce`（以 Base64） | 「在 VPN 客户端中显示的公告文本」。 |

此外，每个响应都会传递 `Subscription-Userinfo` 头，其中包含客户端的聚合流量数据：`upload`、`download`、`total` 和 `expire`（到期时刻，单位秒）。客户端据此显示剩余流量和有效期。

#### 路由（仅适用于 Happ 客户端）

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| 启用路由 | `subEnableRouting` | `false` | 「在 VPN 客户端中启用路由的全局设置。（仅适用于 Happ）」。通过 `Routing-Enable` 头传递。 |
| 路由规则 | `subRoutingRules` | 空 | 「VPN 客户端的全局路由规则。（仅适用于 Happ）」。通过 `Routing` 头传递。 |

| 隐藏服务器设置 | `subHideSettings` | `false` | 「在订阅中隐藏服务器设置（仅适用于 Happ）」。启用时，在 Happ 客户端中隐藏查看和修改服务器参数的功能。该选项仅对 Happ 客户端生效。 |

#### 反向代理 URI

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| 反向代理 URI | `subURI` | 空 | 「修改订阅 URL 地址的基础 URI，以便在代理服务器后使用」。 |

如果该字段为空，面板会从订阅的域名和端口（并考虑 TLS）自行构造链接的基础地址。但如果订阅是通过外部反向代理/CDN 在其他域名或路径下分发的，则在此字段中设置最终的基础 URI，所有链接都会基于它构造。JSON（`subJsonURI`）和 Clash（`subClashURI`）也有类似的独立字段。

如果只设置了通用的 `subURI`，而 JSON 和 Clash 的独立字段留空，则订阅页面上这些格式的链接会继承 `subURI` 的方案和主机（而不是 sub 服务器的端口和 `http`）——这样它们就与反向代理的地址一致。

**示例：反向代理后的订阅。** 订阅本身监听 `2096`，但对外通过 nginx/CDN 在 `https://cfg.example.com/u/` 上可用。为了让响应中的链接基于外部地址而非内部的 `域名:2096` 构造，在「Reverse proxy URI」字段中设置最终的基础 URI：

```
Reverse proxy URI: https://cfg.example.com/u
```

这样，最终链接会呈现为 `https://cfg.example.com/u/ivan2025`。对于 JSON 和 Clash 格式，如有需要，用同样的方式填写独立字段 `subJsonURI` 和 `subClashURI`。

### 10.3. 输出格式

订阅可以以三种独立格式提供，每种格式都有自己的端点，可以分别启用/禁用。

#### 输出中的服务器地址与节点

订阅链接中的服务器地址按照与面板中普通链接和二维码相同的分享地址策略填入：「listen」——可路由的绑定地址，「custom」——用户设置的自定义地址（`shareAddr`），「node」（默认）——节点地址。对于未明确设置策略的 inbound，订阅输出不变。这使得绑定到特定公网 IP 的节点 inbound 能向客户端提供可达的地址。该策略应用于原始、JSON 和 Clash 格式。

节点名称（Node）不会被添加到订阅中配置文件的名称（remark）中：客户端应用中只显示管理员设置的 inbound 备注，不带形如 `@节点名` 的内部后缀。要在多节点订阅中区分同名条目，请手动为它们设置不同的备注，或使用带自有 Remark 的受管主机（Hosts）。

如果由于节点间不同步，同一个客户端两次进入了服务用 JSON inbound，订阅输出会在所有三种格式中按 email 自动去除此类重复，因此输出中不会出现重复的配置文件。

#### 受管主机（Hosts）

**Hosts** 部分（侧边菜单项；带 Total/Enabled/Disabled 数量及列表的汇总页）设置订阅链接的地址覆盖。可以为每个 inbound 添加一个或多个 **主机** ——这些端点会被填入下发给客户端的 subscription 链接中，**取代 inbound 本身的地址、端口和 TLS 参数**。这便于通过 CDN 或中继分发流量，而无需更改 inbound 本身。

每个主机都设置有：

- **Remark** 和描述（Description）、与具体 **Inbound** 的绑定、**Enable** 开关以及对节点的分配（**Nodes**）。
- **Address**（空——继承 inbound 的地址）和 **Port**（`0`——继承 inbound 的端口）；**Tags**（仅在 RAW 订阅中生效）。
- **Security** 选项卡——`same` / `tls` / `none` / `reality`，带 SNI、指纹（fingerprint）、ALPN、证书绑定（pinned-cert）、`allowInsecure` 和 ECH。
- **Advanced** 选项卡——Host header、Path、VLESS 路由、Mux、Sockopt、Final Mask 以及把主机从个别订阅格式（raw / json / clash）中排除。
- **Clash (mihomo)** 选项卡——IP 版本、Mihomo X25519、主机混洗（Shuffle host）。

主机在其所属 inbound 范围内排序，并支持批量启用、禁用和删除。受管主机取代了旧的 External Proxy 数组。

#### 普通链接（SUB）—— Base64 / 纯文本

基础格式，端点为 `subPath`（默认 `/sub/`）。始终启用（在订阅整体启用的前提下）。返回 Xray 链接列表（`vless://`、`vmess://`、`trojan://`、`ss://` 等）——每行一个。启用「编码」选项（`subEncrypt`）时，整个列表会编码为 Base64；关闭时——以纯文本返回。几乎所有客户端都能理解这种格式（v2rayNG、V2RayTun、Sing-box、NekoBox、Streisand、Shadowrocket、Happ 等）。

**示例：关闭「编码」时的响应正文。** 当 `subEncrypt = false` 时，端点 `/sub/` 返回纯文本——每行一个链接：

```
vless://3c8f...@a.example.com:443?security=reality&...#srvA-ivan
trojan://p4ss@b.example.com:443?security=tls&...#srvB-ivan
```

当 `subEncrypt = true`（默认）时，同一列表整体编码为 Base64 并以一行返回——这正是大多数客户端期望的形式。

#### JSON 订阅（sing-box 及兼容客户端）

端点 `subJsonPath`（默认 `/json/`），通过单独的复选框启用。

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| JSON 订阅 | `subJsonEnable` | `false` | 「独立启用/禁用 JSON 订阅端点。」。 |

返回完整的 JSON 配置（sing-box 及衍生客户端——Podkop、OpenWRT sing-box、Karing、NekoBox——可识别的格式）。该格式有额外的可用参数（`subFormats` 选项卡）：

- **Mux**（`subJsonMux`，默认为空）—— JSON 多路复用（Mux）设置，会被注入到每个 JSON 订阅流的 outbound 中。「在一个连接中传输多个独立的数据流。」。
- **Final Mask**（`subJsonFinalMask`，默认为空）——「xray 的 finalmask 掩码（TCP/UDP）和 QUIC 设置，添加到每个 JSON 订阅流中。需要客户端上的较新版本 xray。」。通过子字段配置：「数据包」（`packets`）、「长度」（`length`）、「间隔」（`interval`）、「最大分割」（`maxSplit`）、「噪声」（`noises`：「类型」/`type`、「数据包」/`packet`、「延迟（毫秒）」/`delayMs`、「应用到」/`applyTo`、「+ 噪声」按钮），以及「并发数」（`concurrency`）、「xudp 并发数」（`xudpConcurrency`）和「xudp UDP 443」（`xudpUdp443`）。
- **路由规则**（`subJsonRules`，默认为空）——添加到 JSON 配置中的全局规则。

#### Clash / Mihomo 订阅（YAML）

端点 `subClashPath`（默认 `/clash/`），通过单独的复选框启用。

| 字段（UI） | 键 | 默认 | 说明 |
|---|---|---|---|
| Clash / Mihomo 订阅 | `subClashEnable` | `false` | 启用为 Clash 和 Mihomo 客户端生成 YAML 配置。 |
| 启用路由 | `subClashEnableRouting` | `false` | 「将 Clash/Mihomo 的全局路由规则添加到生成的 YAML 订阅中。」。 |
| 全局路由规则 | `subClashRules` | 空 | 「在 MATCH,PROXY 之前添加到每个 YAML 订阅开头的 Clash/Mihomo 规则。」。 |

响应以 `application/yaml; charset=utf-8` 类型返回。如果设置了「订阅标题」（`subTitle`），它还会通过 `Content-Disposition` 头（`attachment; filename*=UTF-8''<title>`）传递，以便 Clash 客户端用该名称命名导入的配置文件。

生成的链接格式和 YAML 会针对现代客户端保持最新状态：Shadowsocks-2022（SS2022）不再把 userinfo 编码为 Base64；带 http 混淆的 Shadowsocks 链接以 SIP002 格式、配合 `obfs-local` 插件输出；为 Clash/Mihomo 订阅实现了完整的 XHTTP 字段集合。这无需单独设置——链接只是被客户端更准确地识别。

> 注意：本构建恰好支持三种格式——普通链接（Base64/文本）、JSON（sing-box 兼容）和 Clash/Mihomo（YAML）。订阅服务器中没有单独的 Outline 格式。

### 10.4. 订阅信息页面与二维码

如果在浏览器中打开订阅链接（或显式地在 URL 后添加参数 `?html=1` 或 `?view=html`，或发送头 `Accept: text/html`），服务器会返回可视化的 **订阅信息页面**（「订阅信息」），而不是「原始」响应。VPN 客户端仍会得到机器响应，因为它们不请求 HTML。

该页面（由 Vite 构建的单页应用）显示：

- **订阅信息**（Descriptions 区块）：
  - 「订阅 ID」——`subId` 的值；
  - 「状态」——「活跃」、「未激活」或「无限制」。当客户端被禁用、耗尽流量限额或有效期已过时，会标为「未激活」状态；
  - 「已下载」和「已上传」——流量量；
  - 「总限额」——流量限额，未限制时为 `∞`；
  - 「有效期」——到期日期或「永久」；
  - 剩余流量和最后在线时间。
  - 日期根据面板的「Calendar Type」设置（`datepicker`，默认 `gregorian`）以公历或贾拉里历显示。
- **订阅链接**：对每个已启用的格式——一行单独的内容，带彩色标签（绿色 **SUB**、紫色 **JSON**、金色 **CLASH**）、复制按钮和 **二维码** 按钮（弹出窗口，尺寸 240 px）。只有当对应格式在设置中启用时，JSON 和 CLASH 的行才会出现。
- **单独链接**（「复制链接」）：订阅中包含的各个独立配置的完整列表，每个都带自己的协议标签、复制按钮和二维码（post-quantum 链接不生成二维码）。

- **「复制所有配置」按钮**（位于单独链接列表上方）：一键把所有配置链接（每个换行）一次性复制到剪贴板，无需逐个复制；完成后显示通知「已复制所有配置」。
- **快速导入到应用的按钮**（按平台分的下拉菜单）：Android——v2box、v2rayNG（深链 `v2rayng://install-config?url=…`）、Sing-box、V2RayTun、NPV Tunnel、Happ（`happ://add/…`）；iOS——Shadowrocket（通过参数 `flag=shadowrocket`）、v2box（`v2box://install-sub?url=…&name=…`）、Streisand（`streisand://import/…`）、V2RayTun、NPV Tunnel、Happ。这些按钮要么打开相应应用的深链并已填入订阅地址，要么把链接复制到剪贴板。

信息页面以禁止缓存的头（`Cache-Control: no-cache`）返回，以便客户端始终看到关于流量和有效期的最新数据。

### 10.5. 订阅页面的自定义模板

从 3.3.0 起，可以用自己的 HTML 模板替换标准的订阅落地页。默认情况下，订阅地址会返回内置页面，但如果指定了带有自己模板的目录，面板会渲染它并向其中填入客户端的最新数据（流量、有效期、链接等）。

重要：面板 **不提供** 现成的模板。仓库中只包含一个带说明文件 `sub_templates/README.md` 的 `sub_templates/` 目录；你需要自行创建自己的主题。

#### 在哪里启用

主题目录在面板设置中设置：

**设置 → 订阅 → 「订阅信息」部分**，**「订阅主题目录」** 字段（`subThemeDir`）。

界面中的字段说明：
「指向带有订阅页面自定义模板（index.html/sub.html）的文件夹的绝对路径（例如 /etc/3x-ui/sub_templates/my-theme/）。留空以使用默认页面。」

同一部分旁边还有相邻的设置，它们的值可在模板中使用：

「订阅主题目录」字段的说明中有一个 **「模板指南 ↗」** 链接，指向有关创建订阅页面自定义外观模板的文档。
- **「订阅标题」**（`subTitle`）——客户端可见的名称；
- **「支持 URL」**（`subSupportUrl`）——技术支持链接。

#### 设置参数

| 参数 | 默认值 | 用途 |
|---|---|---|
| `subThemeDir` | `""`（空） | 指向带有你的 HTML 模板的目录的绝对路径。空 = 内置的默认页面。 |

#### 如何填入自己的模板

1. 在服务器上为主题创建一个文件夹（任意位置），例如 `/etc/3x-ui/sub_templates/my-theme/`。
2. 在其中放入一个名为 `index.html` 或 `sub.html` 的 HTML 文件。

**示例：主题路径。** 服务器上的最终布局和设置中字段的值：

```
/etc/3x-ui/sub_templates/my-theme/
└── index.html        (或 sub.html——它优先)
```

```
设置 → 订阅 → 「订阅主题目录」:
/etc/3x-ui/sub_templates/my-theme/
```

路径必须是 **绝对** 的（以 `/` 开头）。如果文件夹中既没有 `index.html` 也没有 `sub.html`，面板会返回内置页面。
3. 在面板中打开 **设置 → 订阅**，在「订阅主题目录」字段中填入该文件夹的 **绝对** 路径。
4. 保存设置。

文件选择和渲染的行为：
- 如果目录中有 `sub.html`，则使用它；否则采用 `index.html`。也就是说 `sub.html` 优先于 `index.html`。
- 模板由标准的 Go `html/template` 引擎渲染。
- 解析后的模板会被 **缓存**，仅在文件的修改时间变化时才从磁盘重新读取。因此模板的修改无需重启面板即可生效，同时又不会在每次请求时产生读取/解析的开销。
- 响应会先整体生成到缓冲区，然后才返回给客户端：如果模板在执行过程中失败，部分生成的（损坏的）页面不会发送给用户。

#### 默认行为与回退（fallback）

- 字段为空 → 返回内置的 SPA 页面（数据注入到 `window.__SUB_PAGE_DATA__` 中）。
- 路径不存在或不是目录 → 使用默认页面。
- 目录中既没有 `index.html` 也没有 `sub.html` → 日志中写入警告「subThemeDir set but no usable template found」，返回默认页面。
- 模板文件存在但无法解析 → 日志中写入错误「custom template parse failed」，返回默认页面。
- 模板执行出错 → 日志中写入「custom template execution failed」，返回默认页面。

也就是说，自定义模板的任何问题都不会「破坏」订阅——面板总是降级到内置页面。所有订阅页面（自定义的和标准的）都以禁止缓存的头（`Cache-Control: no-cache, no-store, must-revalidate`）返回，以便客户端始终获得关于流量和有效期的最新数据。

#### 可用的模板变量

模板上下文中会传入一组订阅客户端的数据。通过 `{{ .名称 }}` 引用：

| 变量 | 类型 | 说明 |
|---|---|---|
| `{{ .sId }}` | string | 订阅 ID（UUID）。 |
| `{{ .enabled }}` | bool | 客户端/订阅是否启用。 |
| `{{ .download }}` | string | 格式化的下载量（如「2.5 GB」）。 |
| `{{ .upload }}` | string | 格式化的上传量。 |
| `{{ .total }}` | string | 格式化的总流量限额。 |
| `{{ .used }}` | string | 格式化的已用流量（download + upload）。 |
| `{{ .remained }}` | string | 格式化的剩余流量。 |
| `{{ .expire }}` | int64 | 有效期——Unix 时间，单位 **秒**（`0` = 永久）。用于 JS `Date` 时请乘以 1000。 |
| `{{ .lastOnline }}` | int64 | 最后在线时间——Unix 时间，单位 **毫秒**（`0` = 从未）。 |
| `{{ .downloadByte }}` | int64 | 以精确字节计的下载量。 |
| `{{ .uploadByte }}` | int64 | 以精确字节计的上传量。 |
| `{{ .totalByte }}` | int64 | 以精确字节计的总限额。 |
| `{{ .subUrl }}` | string | 订阅页面的 URL。 |
| `{{ .subJsonUrl }}` | string | 订阅 JSON 配置的 URL。 |
| `{{ .subClashUrl }}` | string | Clash/Mihomo 配置的 URL。 |
| `{{ .subTitle }}` | string | 来自设置的订阅标题（可能为空）。 |
| `{{ .subSupportUrl }}` | string | 来自设置的支持 URL（可能为空）。 |
| `{{ .links }}` | []string | 配置字符串列表（VMess、VLESS 等）。遍历：`{{ range .links }} … {{ end }}`。 |
| `{{ .emails }}` | []string | 与订阅相关的 email 列表。 |
| `{{ .datepicker }}` | string | 面板当前的日历格式：`gregorian` 或 `jalali`（取自「日历类型」设置；若为空——`gregorian`）。 |

使用部分变量的最简模板正文示例：

```html
<h1>{{ .subTitle }}</h1>
<p>已使用：{{ .used }} / {{ .total }}（剩余 {{ .remained }}）</p>
{{ range .links }}<div>{{ . }}</div>{{ end }}

**示例：从 `expire` 得出到期日期。** 字段 `{{ .expire }}` 是 Unix 时间，单位 **秒**，因此用于 JavaScript 时要乘以 1000；值 `0` 表示「无期限」：

```html
<script>
  var exp = {{ .expire }};
  document.write(exp === 0
    ? 'Без срока'
    : 'До ' + new Date(exp * 1000).toLocaleDateString());
</script>
```

请注意：`{{ .lastOnline }}` 已经以 **毫秒** 给出——无需乘以 1000。
```

---

## 11. Xray：路由、outbounds、DNS 与扩展

**「Xray 设置」** 部分是 Xray-core 配置模板的编辑器，面板基于它生成用于启动内核的最终 `config.json`。模板部分的提示：*「Xray 配置文件根据模板创建。」* 与 inbounds（它们单独存储在数据库中，并在组装配置时填入模板）不同，其余的一切——日志、路由、outbounds、DNS、策略、统计——都正是在这里设定的。

> 重要：模板的值以键 `xrayTemplateConfig` 存储在数据库中。保存时，面板会让它经过一系列自动转换（见 [11.10](#1110-保存重启与自动转换)）。任何语法不正确的 JSON 都会被拒绝并报错 *「xray template config invalid」*。

#### 菜单中的位置：「出站」与「路由」

**「出站」（Outbounds）** 和 **「路由」（Routing）** 是侧边菜单中的独立条目（紧挨在「主机」下方，「面板设置」上方），各有自己的地址：`/outbound` 和 `/routing`。指向这些页面的直接链接以及页面刷新都按预期工作。与此同时，**「Xray 配置」** 子菜单中只保留：基本、负载均衡器、DNS 和高级模板。在下面的说明中，[11.3](#113-路由规则routing) 和 [11.4](#114-outbounds出站连接) 两节分别对应「路由」和「出站」页面。

### 11.1. 编辑器结构：选项卡/模式

编辑器提供了几种模板显示模式（按 JSON 部分过滤）：

| 模式 | 显示内容 |
|---|---|
| **基本** | 基础部分（日志、基础路由、主要设置） |
| **高级模板** | 完整的 Xray JSON 模板 |
| **全部** | 同时显示所有部分 |

编辑器内部设置的逻辑分组：

- **主要设置**（提示：*「这些参数描述通用设置」*）。
- **日志**（见 [11.9](#119-日志与统计stats-metrics)）。
- **基础连接**：阻断与直连路由。
- **入站**（提示：*「修改配置模板以连接特定客户端」*）。
- **出站**（见 [11.4](#114-outbounds出站连接)）。
- **负载均衡器**（见 [11.5](#115-负载均衡器balancers)）。
- **路由**（提示：*「每条规则的优先级都很重要！」*，见 [11.3](#113-路由规则routing)）。
- **DNS / Fake DNS**（见 [11.6](#116-dns)）。

### 11.2. 主要设置（General）

#### Freedom Protocol Strategy

| 字段 | 标签 | 描述 | 默认值 |
|---|---|---|---|
| `FreedomStrategy` | **Freedom 协议策略设置** | 直连（freedom）outbound 的网络出口策略。提示：*「设置 Freedom 协议中的网络出口策略」*。控制协议为 `freedom` 的 outbound 中 `settings` 内的 `domainStrategy` 字段。 | 在标准模板中，freedom-outbound `direct` 的 `domainStrategy` 为 **`AsIs`**（地址不解析，按原样传递）。 |

freedom 的 `domainStrategy`（Xray-core 取值）：`AsIs`（不在服务端解析域名），以及 `UseIP` / `UseIPv4` / `UseIPv6` 系列及其「强制」变体 `ForceIP*`，后者迫使出口服务器解析域名并按解析到的 IP 连接。如果出口服务器没有 IPv6，或需要强制只走 IPv4，请改为 `UseIPv4`。

#### Freedom Happy Eyeballs (IPv4/IPv6)

| 字段 | 标签 | 描述 |
|---|---|---|
| `FreedomHappyEyeballs` | **Freedom Happy Eyeballs (IPv4/IPv6)** | 提示：*「用于直连（freedom）出站的双栈组合——在同时具有 IPv4 和 IPv6 的出口服务器上很有用。」* 为 freedom-outbound 启用 Happy Eyeballs 算法（同时尝试两个地址族）。 |
| try delay | （提示） | *「切换到另一个地址族之前等待的毫秒数。150–250 毫秒是一个不错的起点。」* 切换到备用地址族之前的延迟。推荐范围为 150–250 毫秒。 |

#### Overall Routing Strategy

| 字段 | 标签 | 描述 | 默认值 |
|---|---|---|---|
| `RoutingStrategy` | **域名路由设置** | 路由的整体 DNS 解析策略。提示：*「设置整体的 DNS 解析路由策略」*。控制 `routing.domainStrategy` 字段。 | 在标准模板中 `routing.domainStrategy` = **`AsIs`**。 |

`routing.domainStrategy` 决定 IP 路由规则如何与域名请求匹配：`AsIs`（只用域名规则，不解析）、`IPIfNonMatch`（如果域名未匹配规则——则解析并检查 IP 规则）、`IPOnDemand`（遇到 IP 规则时立即解析）。要让 IP 规则（例如 `geoip:*`）在域名请求时生效，通常需要 `IPIfNonMatch`。

#### Outbound Test URL

| 字段 | 标签 | 描述 | 默认值 |
|---|---|---|---|
| `outboundTestUrl` | **出站测试 URL** | 测试 outbound 时用于检查连通性的 URL。提示：*「检查出站连接的 URL」*。与模板分开存储，存于键 `xrayOutboundTestUrl` 下。 | **`https://www.google.com/generate_204`** |

该值会经过清洗。在实际测试 outbound 时，它会被额外校验为公共 URL——这是为防止 SSRF：用户无法通过客户端塞入任意（包括内部）URL，测试 URL 始终取自服务端设置。保存/测试时为空值会被替换为默认的 `generate_204`。

#### Block BitTorrent

| 字段 | 标签 | 描述 |
|---|---|---|
| `Torrent` | **阻止 BitTorrent** | 在 `routing.rules` 中添加一条规则，将带 `protocol: ["bittorrent"]` 的流量发送到 outbound `blocked`。在标准模板中此规则默认存在。 |

#### 连接限制（Connection Limits）

提示：*「等级 0 用户的连接级策略。留空则使用 Xray 默认值。」* 这些参数写入 `policy.levels.0`。

| 字段 | 标签 | 描述 | 默认值 |
|---|---|---|---|
| `connIdle` | **空闲超时**（秒） | *「在空闲指定秒数后关闭连接。减小该值可在高负载服务器上更快释放内存和文件描述符（Xray 默认：300）。」* | 空 → Xray 默认 **300** |
| `bufferSize` | **缓冲区大小**（KB） | *「每个连接的内部缓冲区大小，单位 KB。设为 0 可在小内存服务器上最大限度减少内存占用（Xray 默认值取决于平台）。」* 占位符：**「自动」**。 | 空 → 取决于平台；`0` — 最小化 |

**示例（`policy.levels.0`）。** 该分组中的字段写入等级 0 策略。在小内存的高负载服务器上，可以这样加快资源释放：

```json
"policy": {
  "levels": {
    "0": {
      "connIdle": 120,
      "bufferSize": 0
    }
  }
}
```

这里连接在空闲 120 秒后即关闭（而非默认的 300），`bufferSize: 0` 最大限度减少缓冲区内存占用。表单中留空的字段不会进入 JSON——于是 Xray 会应用自己的默认值。

### 11.3. 路由规则（routing）

`routing.rules` 规则列表。**顺序至关重要**（*「每条规则的优先级都很重要！」*）：规则自上而下评估，命中第一条匹配的规则。提示：*「拖动以更改顺序」*。顺序管理按钮：**置顶**、**置底**、**上移**、**下移**。

每条规则都有 `type: "field"`。按钮：**创建规则**、**编辑规则**。列表字段提示：*「以逗号分隔的元素」*。

在「路由」页面，**「导入规则」** 和 **「导出规则」** 按钮被收纳到 **「更多」**（more）下拉菜单中——与「出站」页面一样。**「导出规则」** 按钮不会立即下载文件，而是打开一个带 JSON 预览以及 **「复制」** 和 **「下载」** 按钮的模态窗口：内容可在保存前查看。「出站」页面的出站导出也以相同方式工作。

#### Route Tester（路由测试器）

在 Routing 选项卡中有一个 **Route Tester** 子选项卡——它会询问正在运行的 Xray：某个具体连接会由哪个 outbound 处理，而不发送任何真实流量。指定域名或 IP、端口、网络（TCP/UDP），并在需要时指定 inbound 和嗅探到的协议（`http`/`tls`/`quic`/`bittorrent`），然后点击 **Test Route**。决策直接取自实时路由引擎。

响应中会显示选中的 outbound，使用负载均衡器时——还会显示负载均衡器的标签。如果没有任何规则匹配，测试器会提示流量走默认 outbound（`outbounds` 列表中的第一个）。这便于在依赖规则顺序之前先验证它。

#### 启用与禁用单条规则

单条路由规则可以用开关临时**禁用**，而无需删除。规则表中有一列 **「启用」** 带开关（Switch），规则表单中也有一个 **「启用」** 字段——同样是开关。被禁用的规则不会进入最终的 Xray 配置，但会保留在模板中，随时可以重新启用。

统计服务规则（`inboundTag: ["api"] → outboundTag: "api"`）无法禁用——它的开关被锁定，以免破坏面板的流量计量（见 [11.10](#1110-保存重启与自动转换)）。

#### 规则表单字段

| 表单字段 | 标签 | JSON 字段 | 描述 |
|---|---|---|---|
| 源 | **源** | `source` | 源 IP 地址/子网。逗号分隔列表。 |
| 源端口 | **源端口** | `sourcePort` | 源端口。 |
| 目标 | **目标** | `domain` + `ip` + `port` | 目标域名、IP 和端口。域名支持前缀 `domain:`、`full:`、`regexp:`、`keyword:`，以及 `geosite:*`；IP 支持 `geoip:*` 和 CIDR。 |
| 网络 | — | `network` | `tcp`、`udp` 或 `tcp,udp`。 |
| 协议 | — | `protocol` | `http`、`tls`、`bittorrent`（通过 sniffing 识别）。 |
| 用户 | **用户** | `user` | 按用户 e-mail/标识过滤。 |
| 属性 / 值 | **属性** / **值** | `attrs` | 用于匹配的 HTTP 头属性。 |
| VLESS route | **VLESS route** | — | 按 VLESS 的 route 字段路由。 |
| 入站标签 | **入站标签** | `inboundTag` | 规则适用的一个或多个 inbound 标签（包括内置的 `api`，以及来自 DNS 设置的 DNS 标签）。在 inbound 列表中，如果某 inbound 设置了单独的备注，则显示为「tag (remark)」，否则——只显示标签；保存的规则中依然只存储标签。 |
| 出站标签 | **出站标签** / **出站连接** | `outboundTag` | 将匹配的流量发往何处。 |
| 负载均衡器标签 | **负载均衡器标签** / **负载均衡器** | `balancerTag` | 提示：*「通过其中一个已配置的负载均衡器引导流量」*。 |

> `outboundTag` 与 `balancerTag` 互斥：*「无法同时使用 balancerTag 和 outboundTag。同时使用时只有 outboundTag 生效。」* 在同一条规则中，请只设置出站标签或负载均衡器标签之一。

#### 标准模板的内置规则

在标准 `config.json` 中，`routing` 部分包含三条规则（按此顺序）：

1. `inboundTag: ["api"] → outboundTag: "api"` — 面板统计 gRPC-API 的服务规则。
2. `ip: ["geoip:private"] → outboundTag: "blocked"` — 阻断私有地址段。
3. `protocol: ["bittorrent"] → outboundTag: "blocked"` — 阻断 BitTorrent。

> 规则 `api → api` 在保存时始终自动提升到位置 0（见 [11.10](#1110-保存重启与自动转换)），以免统计请求被上方的 catch-all 规则「吃掉」。

**规则示例。** 将所有发往俄罗斯网站和私有网络的流量直连发送（绕过代理），其余的——发往负载均衡器。顺序很重要：「直连」规则必须位于 catch-all 之上。在 `routing.rules` 中：

```json
{
  "type": "field",
  "domain": ["geosite:category-ru", "domain:example.ru"],
  "ip": ["geoip:ru", "geoip:private"],
  "outboundTag": "direct"
}
```

要让 IP 规则（`geoip:ru`）对域名请求也生效，通常需要在路由顶层设置 `routing.domainStrategy: "IPIfNonMatch"`（见 [11.2](#112-主要设置general)）。

#### 预置路由分组（基础连接）

在「基础连接」模式中，面板帮助你从现成列表组装典型规则：

| 分组 | 字段 | 提示 |
|---|---|---|
| 按协议/网站阻断 | — | *「配置以阻止客户端访问特定协议」* |
| 按国家阻断 | **被阻断的 IP 地址**、**被阻断的域名** | *「这些参数将根据目标国家阻断流量。」* |
| 直连 | **直连 IP 地址**、**直连域名** | *「直连意味着特定流量不会经由其他服务器转发。」* |
| IPv4 规则 | — | *「这些参数将允许客户端只通过 IPv4 路由到目标域名」* |
| WARP 规则 | — | *「这些选项将根据具体目标通过 WARP 引导流量。」* |
| NordVPN 路由 | — | *「这些选项将根据具体目标通过 NordVPN 引导流量。」* |

#### MTProto-inbound：通过 Xray 路由 Telegram 流量

MTProto-inbound 有一个 **「Route through Xray」** 开关（默认关闭）以及可选的 **Outbound** 选择。启用时，面板会在 Xray 配置中添加一个标签与该 inbound 本身相同的环回 SOCKS 桥接，mtg 通过它引导 Telegram 流量。此后出站的 Telegram 流量由路由器管理：可以在 Routing 选项卡上按 inbound 标签用普通规则匹配它，或通过 **Outbound** 字段将其强制导向选定的 outbound 或负载均衡器。将 **Outbound** 留空，则由路由规则做决策。

### 11.4. Outbounds（出站连接）

`outbounds` 列表。按钮：**创建出站连接**、**修改出站连接**。提示：*「修改配置模板，为此服务器定义出站连接」*。

标准模板中有两个必备的 outbound：

- `protocol: "freedom"`，`tag: "direct"` — 直接出口到互联网（带 `domainStrategy: "AsIs"` 和 `finalRules: [{action: "allow"}]`）；
- `protocol: "blackhole"`，`tag: "blocked"` — 用于被阻断流量的「黑洞」。

#### outbound 表单的通用字段

| 字段 | 标签 | 描述 |
|---|---|---|
| 标签 | **标签**（提示：*「唯一标签」*） | outbound 的唯一标识符。占位符：*「唯一标签」*。校验：*「标签为必填」*、*「标签已被另一个出站使用」*。 |
| 协议 | — | 出站类型（见下文）。 |
| 地址 / 端口 | **地址** / 端口 | 连接目标。地址和端口为必填。 |
| 通过…发送 | **通过…发送** | 出站接口的本地 IP 地址（`sendThrough`）。占位符：*「本地 IP」*。 |
| Dialer proxy（链式） | — | 提示：*「将此出站通过另一个出站（按标签）连接，以构建代理链。留空则直接连接。」* 占位符：*「选择用于链式的出站」*。通过 `streamSettings.sockopt.dialerProxy` 实现。 |

#### 支持的 outbound 协议

表单支持的协议：

- **`freedom`** — 直接出口。字段 `settings.domainStrategy`、`finalRules`（见下文）、Happy Eyeballs。不可测试（*「Outbound has no testable endpoint」*）。
- **`blackhole`** — 丢弃流量。字段 **响应类型**。不可测试。
- **`socks`**、**`http`** — 带 `address`/`port` 的 `settings.servers[]` 列表；字段 **授权密码**。
- **`vmess`** — `settings.vnext[]`（`address`/`port`）。
- **`vless`** — `settings.address`/`settings.port`。
- **`trojan`**、**`shadowsocks`** — `settings.servers[]`。
- **`wireguard`** — 带 `endpoint` 的 `settings.peers[]`，外加密钥（见 [11.7](#117-wireguard--warp--nordvpn)）。
- **`hysteria`** — `settings.address`/`settings.port`（UDP 传输）。

对于 **loopback** 类型的 outbound，提供 **Sniffing** 块，参数与 inbound 相同：开关、**destOverride**、**Metadata Only**、**Route Only** 以及 **排除域名** 列表。

在 **Hysteria2** 的 **UDP** 掩码（FinalMask）中，提供了额外的模式。**Salamander** 掩码有一个 **Mode** 选择器，取值为 **Salamander** 和 **Gecko**：Gecko 模式会为数据包添加随机填充，带有大小的 **Min**/**Max** 字段（`packetSize`，范围 1–2048，默认 512–1200）——这可防止按包长进行指纹识别。**Realm** 掩码（UDP hole-punching）新增了可选的 **TLS Config** 块，包含 **Server Name**（SNI）、**ALPN**（`h3`/`h2`/`http/1.1`）、**Fingerprint**（uTLS）字段以及 **Allow Insecure** 开关。

**示例：通过上游 SOCKS 的链式连接。** outbound `upstream` 连接外部 SOCKS5 代理，而 `chained` 通过它（`dialerProxy`）发送自己的流量，从而形成链。在 `outbounds` 中：

```json
[
  {
    "tag": "upstream",
    "protocol": "socks",
    "settings": {
      "servers": [{ "address": "203.0.113.10", "port": 1080 }]
    }
  },
  {
    "tag": "chained",
    "protocol": "freedom",
    "streamSettings": {
      "sockopt": { "dialerProxy": "upstream" }
    }
  }
]
```

现在带 `outboundTag: "chained"` 的路由规则会通过 `upstream` 将流量送出到互联网。

#### 从分享链接导入 outbound

outbound 可以从分享链接（`vless://`、`vmess://` 等）导入。导入时，链接 `extra=` 块中传递的多路复用器 **xmux**（XHTTP）设置也会被保留：导入后，它们的值会填入所创建 outbound 的 **XMUX** 子表单。

#### Mux 字段（多路复用）

**最大并发**、**最大连接数**、**最大复用次数**、**最大请求数**、**最大复用秒数**、**keep alive 周期**。这些参数配置出站的 mux/XUDP 行为。

#### Sockopts（套接字设置）

**Sockopts** 分组：**keep alive 间隔**、**Mark (fwmark)**、**接口**、**仅 IPv6**、**接受 proxy protocol**、**Proxy protocol**、**TCP user timeout（毫秒）**、**TCP keep-alive idle（秒）**。链式的 dialer-proxy 也在此处设置。

#### Freedom finalRules（覆盖私有 IP 阻断）

对于 freedom-outbound，提供 **最终规则** 分组：

| 字段 | 标签 | 描述 |
|---|---|---|
| `overrideXrayPrivateIp` | **覆盖 Xray 中默认的私有 IP 阻断** | 解除 Xray 内置的对发往私有 IP 的出站禁令。 |
| `action` | **动作** | `allow`（如标准模板中：`finalRules: [{action: "allow"}]`）、`redirect`（**Redirect**）或其他。 |
| `blockDelay` | **阻断延迟（毫秒）** | 丢弃连接前的延迟。 |
| `redirect` / `fragment` | **Redirect** / **Fragment** | 流量重定向和分片动作。 |

#### fragment 掩码：逐片的 Lengths 与 Delays

在 **fragment** 掩码（FinalMask 中的 fragment 类型，用于 TCP）中，单个 Length 和 Delay 字段被替换为列表 **Lengths** 和 **Delays**：可为每个分段单独设置长度范围（例如 `100-200`）和延迟毫秒数（例如 `10-20` 或 `0`）。列表行可以添加和删除；先前保存的单个值会自动迁移为单元素数组。

#### 表单的其他字段

- **UDP over TCP** 和 **UoT 版本** — 用于 shadowsocks 类协议。
- **无 gRPC 头**、**Uplink chunk 大小** — gRPC 传输参数。
- TLS/uTLS 字段：**校验 peer 名称**、**Pinned SHA256**、**Short ID**、**Vision testpre**，占位符「服务器名称」。

#### 出站测试

按钮：**测试**、**测试全部**。状态：**正在测试连接...**、**测试成功**、**测试失败**、**无法测试出站连接**。结果：**测试结果**，延迟（毫秒）。

两种模式（提示：*「TCP：快速的仅拨号探测。HTTP：通过 xray 的完整请求。」*）：

- **TCP**（`mode=tcp`）— 对 `host:port` 的简单拨号，对所有端点并行执行，超时约 5 秒。只检查 TCP 可达性，不验证代理协议。对 `freedom`/`blackhole`/标签 `blocked` 会返回 *「Outbound has no testable endpoint」*。
- **HTTP**（`mode=http` 或为空）— 启动一个临时的 Xray 实例，运行一次真实的 HTTP 请求（探测 URL = 服务端的 `outboundTestUrl`），测量真实延迟。权威但代价高的模式：由全局锁序列化（*「Another outbound test is already running, please wait」*）。单次尝试超时 10 秒，等待结果窗口 15 秒（已加大，以免在慢速或隧道化链路上的健康 outbounds 被标记为「Failed」）。失败时，真实原因（DNS 错误、connection refused、超过截止时间、TLS 错误等）会写入面板/Xray 日志，通用的超时消息会指向该日志。

> UDP 协议（`wireguard`、`hysteria`）和 UDP 传输（`kcp`、`quic`、`hysteria`）**始终**以 HTTP 模式测试，即使请求了 TCP——裸 UDP 拨号无法区分「活的」端点和「死的」端点。对于 wireguard，测试配置中会强制设置 `noKernelTun: true`。

#### 批量检查与分阶段拆解

**测试** 和 **测试全部** 在 HTTP 模式下，会为一批 outbounds 启动一个共享的临时 Xray 实例，为每个创建一个带规则的环回 SOCKS-inbound，并通过它并行发送一次真实的 HTTP 请求；**测试全部** 分批检查 outbounds。**测试全部** 也会检查来自订阅的 outbounds（「来自订阅」只读表格）——它们的行同样会以测试结果高亮。同时，`freedom`（「direct」）和 `dns` 的 outbounds 在任何模式下都不会被测试（它们不是代理）：其测试按钮不可用，**测试全部** 会跳过它们，服务端防护即使在直接调用 API 时也禁止对其进行 HTTP 测试。除成功/失败外，弹出的结果还会显示响应的 HTTP 状态码以及按阶段的耗时拆解：**Proxy connect**（连接到代理）、**TLS via outbound**（通过 outbound 的 TLS）和 **First byte**（首字节时间）——这有助于了解延迟或故障出现在哪一步。

#### outbounds 流量统计

面板按标签统计流量（`up`/`down`/`total`）。重置按钮可重置某个具体标签或全部标签的计数（`tag = "-alltags-"`）。**账户信息** 和 **出站连接状态** 字段显示汇总。

### 11.5. 负载均衡器（Balancers）

`routing.balancers` 列表。按钮：**创建负载均衡器**、**编辑负载均衡器**。

在 Balancers 选项卡中有实时状态列：**Live Target** 显示运行中 Xray 里负载均衡器当前激活的目标，而 **Override** 允许手动覆盖目标选择（值 **Auto (strategy)** 恢复按策略选择）。状态通过单独的按钮刷新。如果负载均衡器在运行中的 Xray 里尚未激活，面板会先提示保存更改或启动 Xray。

| 字段 | 标签 | 描述 |
|---|---|---|
| 标签 | **标签**（提示：*「唯一标签」*） | 唯一标识符。占位符：*「唯一的负载均衡器标签」*。校验：*「标签为必填」*、*「标签已被另一个负载均衡器使用」*。 |
| 选择器 | **选择器** | outbound 标签列表（按子串），负载均衡器从中选择出口。必须至少选择一个：*「请至少选择一个出站」*。 |
| Fallback | **Fallback** | 若无任何选择器匹配时的后备 outbound 标签。 |
| 策略 | **策略** | 选择算法（见下文）。 |

#### 策略与观测参数

策略（`strategy.type`）决定负载均衡器如何从选择器中挑选 outbound。Xray-core 取值：`random`（随机）、`roundRobin`（轮询）、`leastPing`（按 observatory 结果取最小延迟）、`leastLoad`（最小负载）。`leastLoad`/`leastPing` 使用来自 `strategy.settings` 的参数：

| 字段 | 标签 | 描述 |
|---|---|---|
| `expected` | **期望值** | 占位符：*「最优节点数」* — 目标的存活节点数。 |
| `maxRtt` | **最大 RTT** | 筛选候选时允许的 RTT 上限。 |
| `tolerance` | **容差** | 比较延迟/负载时的容差（tolerance）。 |
| `baselines` | **Baselines** | 用于对节点分组的延迟阈值。 |
| `costs` | **Costs** | 针对各标签的权重系数（cost）。 |

**策略示例。** `strategy` 块位于负载均衡器内部（在 JSON 中——与 `tag` 和 `selector` 相邻）：

```json
"strategy": { "type": "random" }      // 从选择器中随机选择
"strategy": { "type": "roundRobin" }  // 轮流，逐个
"strategy": { "type": "leastPing" }   // 最小延迟（需要观测器）
```

对于 `leastLoad`，参数在 `settings` 中设置：

```json
"strategy": {
  "type": "leastLoad",
  "settings": {
    "expected": 2,
    "maxRTT": "1s",
    "tolerance": 0.05,
    "baselines": ["500ms", "1s", "2s"],
    "costs": [
      { "regexp": false, "match": "proxy-premium",   "value": 0.1 },
      { "regexp": true,  "match": "^proxy-cheap-.+$", "value": 5 }
    ]
  }
}
```

**它如何运作（举例说明）。** 设观测器测得各出口的延迟为：`A = 250 毫秒`、`B = 280 毫秒`、`C = 700 毫秒`、`D = 1500 毫秒`。在上述设置下，选择过程如下：

1. **`maxRTT: "1s"`** — 延迟高于 1 秒的出口被剔除：`D`（1500 毫秒）出局。剩下 `A`、`B`、`C`。
2. **`baselines` + `expected`** — 出口按延迟阈值分组，取落入其中的出口数不少于 `expected` 的**最小**阈值。阈值 `500ms` 已包含 `A` 和 `B`——即 2（= `expected`），因此选中分组 {`A`、`B`}。只要快速出口足够，`C`（700 毫秒）就不会被选中（它是「热备」）。
3. **`tolerance: 0.05`** — 在选定分组内，延迟相差不超过 5% 的出口被视为等价，负载在它们之间均分。`A`（250）和 `B`（280）相差约 12%（> 5%），因此在其他条件相同时优先选更快的 `A`；若差异在 5% 以内——流量会同时经过 `A` 和 `B`。
4. **`costs`** — 在比较前对各出口的「成本」进行修正：`value` 越小，出口越有吸引力，越大则相反。在示例中，`proxy-premium` 得到 `0.1`（变得更「便宜」，被选中的意愿更高），而所有 `proxy-cheap-*`（按正则表达式，`regexp: true`）得到 `5`（变得更「贵」，最后才使用）。这样可以柔性地优先某些出口，而不必硬性排除它们。

结果：流量将主要经过 `A`（在延迟接近时——与 `B` 均分），`C` 保持为备用，`D` 在其 RTT 降到 `maxRTT` 以下之前被排除。

#### 观测器：`observatory` 与 `burstObservatory`（为 `leastPing` / `leastLoad` 测量）

`leastPing` 和 `leastLoad` 策略本身不进行任何测量——它们需要每个 outbound 的延迟和可用性数据。这些由**观测器**（observatory）收集：它周期性地「ping」每个被跟踪的 outbound，并记录响应时间和可用性。同样的数据会显示在 **「观测器」** 选项卡中（状态 **活跃 / 不可用**、**「最后活动」**、**「最后尝试」**）。

面板中没有观测器的专门表单——该块需在 Xray 配置编辑器中**手动**添加，位于配置顶层（与 `routing` 和 `outbounds` 相邻），之后需要**重启 Xray**。

提供两种变体：

- **`observatory`** — 简单版：`subjectSelector` + `probeURL` + `probeInterval`。
- **`burstObservatory`** — 增强版，可通过 `pingConfig` 精细配置 ping；适合多个出口。

`burstObservatory` 块示例：

```json
{
  "subjectSelector": ["WS-SE", "WS-FR", "WS-PL"],
  "pingConfig": {
    "destination": "https://www.google.com/generate_204",
    "interval": "1m",
    "connectivity": "http://connectivitycheck.platform.hicloud.com/generate_204",
    "timeout": "5s",
    "sampling": 2
  }
}
```

字段含义：

| 字段 | 设定内容 |
|---|---|
| `subjectSelector` | 要观测的 outbound **标签前缀** 列表。Xray 取所有标签以指定字符串开头的 outbound。在示例中观测出口 `WS-SE…`、`WS-FR…`、`WS-PL…`。这些标签应与负载均衡器 **选择器** 中所选的一致。 |
| `pingConfig.destination` | **通过每个 outbound** 请求的 URL，用于测量延迟。取一个返回 `204` 且无主体的「轻量」页面——例如 `https://www.google.com/generate_204`。到响应的时间即测得的延迟。 |
| `pingConfig.interval` | 多久 ping 一次每个 outbound。时长字符串：`"1m"` — 每分钟一次，也可用 `"30s"`、`"5m"` 等。越频繁数据越新鲜，但后台流量越多。 |
| `pingConfig.connectivity` | （可选）检查服务器**自身基础连通性**的 URL。如果它不可达——说明问题出在服务器网络，观测器**不会**把 outbound 标记为不可用（防止本地故障导致的误报）。通常也是一个返回 `204` 的 endpoint。 |
| `pingConfig.timeout` | 在判定一次尝试失败前，等待一次 ping 响应的时长（例如 `"5s"`）。 |
| `pingConfig.sampling` | 为每个 outbound 保留并取平均的最近测量数。`2` — 计入最近两次 ping（平滑随机抖动）。 |

如何把一切串起来：

1. 在 Xray 编辑器中添加带所需 `subjectSelector` 的 `burstObservatory` 块。
2. 创建负载均衡器：**策略** = `leastPing`，在 **选择器** 中填入相同的 outbound 标签（`WS-SE`、`WS-FR`、`WS-PL`）。
3. 用路由规则把流量导向它（字段 **负载均衡器标签**，见 [11.3](#113-路由规则routing)）。
4. 重启 Xray。在 **「观测器」** 选项卡中会出现出口的状态，负载均衡器将开始从存活的出口中选择最快的。

> 同一条规则中不能同时设置 `balancerTag` 和 `outboundTag`——只有 `outboundTag` 会生效。

### 11.6. DNS

`dns` 部分。开关：**启用 DNS**（提示：*「启用内置 DNS 服务器」*）。

#### DNS 通用参数

| 字段 | 标签 | JSON | 描述 / 提示 |
|---|---|---|---|
| `tag` | **DNS 标签名称** | `dns.tag` | *「此标签将在路由规则中作为入站标签可用。」* 允许通过 `inboundTag` 路由 DNS 请求本身。 |
| `clientIp` | **客户端 IP** | `dns.clientIp` | *「用于在 DNS 查询期间向服务器告知指定的 IP 位置」*（EDNS Client Subnet）。 |
| `strategy` | **查询策略** | `dns.queryStrategy` | *「整体的域名解析策略」*。取值：`UseIP`、`UseIPv4`、`UseIPv6`。 |
| `disableCache` | **禁用缓存** | `dns.disableCache` | *「禁用 DNS 缓存」*。 |
| `disableFallback` | **禁用后备 DNS** | `dns.disableFallback` | *「禁用后备 DNS 查询」*。 |
| `disableFallbackIfMatch` | **匹配时禁用后备 DNS** | `dns.disableFallbackIfMatch` | *「当匹配到 DNS 服务器的域名列表时禁用后备 DNS 查询」*。 |
| `enableParallelQuery` | **启用并行查询** | — | *「启用向多个服务器的并行 DNS 查询以加快解析」*。 |
| `useSystemHosts` | **使用系统 Hosts** | `dns.useSystemHosts` | *「使用已安装系统的 hosts 文件」*。 |

**`dns` 块示例。** 对 Google 域名的查询经 Cloudflare 的 DoH 服务器解析，其余的——经 `1.1.1.1`；对 Google 的查询只接受非私有 IP。在配置顶层：

```json
"dns": {
  "tag": "dns-inbound",
  "queryStrategy": "UseIPv4",
  "servers": [
    {
      "address": "https://cloudflare-dns.com/dns-query",
      "domains": ["geosite:google"],
      "expectIPs": ["geoip:!private"]
    },
    "1.1.1.1"
  ]
}
```

字符串形式的服务器（`"1.1.1.1"`）没有字段——它是其余所有域名的默认服务器。标签 `dns-inbound` 之后可在路由规则中用作 `inboundTag`，以便将 DNS 请求本身引导到所需的 outbound。

#### 过期记录缓存

| 字段 | 标签 | 描述 |
|---|---|---|
| `serveStale` | **使用过期记录** | *「在后台刷新期间返回缓存中的过期结果」*。 |
| `serveExpiredTTL` | **过期记录 TTL** | *「过期缓存记录的有效期（秒）；0 = 无限」*。 |

#### DNS 服务器（`dns.servers` 列表）

按钮：**创建 DNS**、**编辑 DNS**、**删除全部**（确认：*「列表中所有 DNS 服务器将被删除。此操作无法撤销。」*）。模板：**使用模板**，窗口 **DNS 模板**，包括 **家庭** 预设。

在 DNS 服务器记录上点击 **编辑 DNS** 时（与 Fake DNS 记录一样），编辑窗口会填入服务器已保存的值，而不是默认值。

DNS 服务器字段：

| 字段 | 标签 | 描述 |
|---|---|---|
| address | — | DNS 地址（IP、DoH-URL、`localhost`、`fakedns` 等）。 |
| `domains` | **域名** | 使用此服务器的域名列表。 |
| `expectIPs` | **期望 IP** | 仅当 IP 落入列表时才接受响应。 |
| `unexpectIPs` | **非期望 IP** | 丢弃带指定 IP 的响应。 |
| `skipFallback` | **跳过 Fallback** | 不将此服务器用作 fallback。 |
| `finalQuery` | **最终查询** | 将服务器标记为链中的最终服务器。 |
| `timeoutMs` | **超时（毫秒）** | 对服务器的查询超时。 |

#### Hosts（静态记录）

**Hosts** 分组（`dns.hosts`）。按钮 **添加 Host**；空状态 **未定义 Host**。字段：域名（占位符：*「域名（例如 domain:example.com）」*）和值（占位符：*「IP 或域名——输入后按 Enter」*）。

#### DNS 日志

见 [11.9](#119-日志与统计stats-metrics)：日志部分中的 **DNS 日志** 标志（`dnsLog`）。

### 11.7. Fake DNS

`fakedns` 部分。按钮：**创建 Fake DNS**、**编辑 Fake DNS**。

| 字段 | 标签 | 描述 |
|---|---|---|
| `ipPool` | **IP 池子网** | 用于发放虚拟 IP 的 CIDR 范围（例如 `198.18.0.0/15`）。 |
| `poolSize` | **池大小** | 在环形池中保留多少个地址。 |

Fake DNS 与 inbound 上的 sniffing 配合使用：内核给客户端发放一个虚拟 IP，记住域名↔IP 的对应关系，并在路由时还原域名。要让 Fake DNS 工作，必须将地址为 `fakedns` 的 DNS 服务器添加到 DNS 服务器列表中。

**示例：Fake DNS + DNS 服务器的组合。** 先设定虚拟地址池，再添加 `fakedns` DNS 服务器，使域名查询从该池获得 IP：

```json
"fakedns": [
  { "ipPool": "198.18.0.0/15", "poolSize": 65535 }
],
"dns": {
  "servers": [
    { "address": "fakedns", "domains": ["geosite:geolocation-!cn"] },
    "1.1.1.1"
  ]
}
```

此外，还需在 inbound 上启用带 `destOverride: ["fakedns"]` 的 sniffing，否则内核无从取得用于还原的真实域名。

### 11.8. WireGuard / WARP / NordVPN

#### WireGuard 字段（`wireguard`）

| 字段 | 标签 | 描述 |
|---|---|---|
| `secretKey` | **私钥** | 本地接口的私钥。 |
| `publicKey` | **公钥** | peer 的公钥。 |
| `psk` | **共享密钥** | PreShared Key（可选）。 |
| `allowedIPs` | **允许的 IP 地址** | 路由进隧道的地址范围。 |
| `endpoint` | **端点** | peer 的 `host:port`。 |
| `domainStrategy` | **域名策略** | WireGuard-outbound 的解析策略。 |

#### Cloudflare WARP（`warp`）

该集成使用 API `https://api.cloudflareclient.com/v0a4005`（client-version `a-6.30-3596`）。控制器动作（`/xray/warp/:action`）：`config`、`reg`、`license`、`data`、`del`。

分步：

1. **创建 WARP 账户** → `reg`：面板生成/接受私钥（`privateKey`）和公钥（`publicKey`），在 Cloudflare 注册设备，并在 `warp` 设置中保存 `access_token`、`device_id`、`license_key`、`private_key`（以及 `client_id`）。
2. **WARP / WARP+ 许可密钥** → `license`：设置 26 字符的 WARP+ 密钥（占位符：*「26 字符的 WARP+ 密钥」*）。出错时：*「无法设置 WARP 许可。」* 如果尚未获取配置：*「请先获取 WARP 配置。」*
3. **账户信息**：**设备名称**、**设备型号**、**设备已启用**、**账户类型**、**角色**、**WARP+ data**、**配额**、**用量**。
4. **添加出站** — 使用获取到的密钥和 Cloudflare 端点创建 WireGuard-outbound。
5. **删除账户** → `del`：清除已保存的 WARP 数据。

#### NordVPN（`nord` / `nordvpn`）

该集成使用 NordLynx（= WireGuard）。控制器动作（`/xray/nord/:action`）：`countries`、`servers`、`reg`、`setKey`、`data`、`del`。

分步：

1. **访问令牌** → `reg`：面板向 `api.nordvpn.com` 请求 NordLynx 凭据并提取 `nordlynx_private_key`。在 `nord` 设置中保存 `private_key` 和 `token`。替代方式——`setKey`：直接输入 **私钥**（不能为空）。
2. **国家** → `countries` 加载国家列表；**城市**（或 **所有城市**）。
3. **服务器** → `servers` 加载所选国家的服务器（`countryId` 被校验为数字——防注入）。过滤：只显示 **负载** > 7% 的服务器。如果没有服务器：*「未找到所选国家的服务器」*。如果服务器未提供 NordLynx 公钥：*「所选服务器未提供 NordLynx 公钥。」*
4. 创建/更新出站：提示 *「已添加 NordVPN 出站」* / *「已更新 NordVPN 出站」*。

#### IPv4 优先与 userspace TUN

WARP 和 NordVPN 向导生成的 WireGuard-outbounds 使用 `domainStrategy: "ForceIPv4v6"`（IPv4 优先，在仅 v6 的主机上回退到 IPv6），而非 `ForceIP`——这消除了在 IPv6 配置不完整的主机上、当选中 Cloudflare 端点的 AAAA 记录时握手「卡住」的问题。此外，为它们启用了 userspace TUN（`noKernelTun: true`），而非 kernel TUN：后者需要权限和 fwmark 路由，并在许多 VPS 上静默失败，而面板内置的连接检查始终通过 userspace TUN 测试——现在真实流量和检查走的是同一条路径。该变更仅作用于新添加或重置的 outbounds；已保存的模板保留各自的设置。

### 11.9. Reverse 代理与 TUN

#### Reverse（反向代理）

Xray 配置的 `reverse` 部分。在 outbound 表单中有一个切换到 **反向代理** 类型的开关。按钮：**创建反向代理**、**编辑反向代理**。

| 字段 | 标签 | 描述 |
|---|---|---|
| 类型 | **类型** | **Bridge** 或 **Portal** — Xray 反向代理的两种角色。 |
| 域名 | **域名** | bridge↔portal 配对的服务标记域名。 |
| 标签 / 连接 | **标签** / **连接** | 用于关联 bridge 和 portal 的标签。 |
| Reverse Tag | **反向代理标签** | 提示：*「用于简单 VLESS 反向代理的出站连接标签。留空以禁用。」* 占位符：*「出站标签（空 = 禁用）」*。实现简化的 VLESS reverse。 |

outbound 表单中还包含反向流字段：**反向 sniffing**、**Workers**、**Reserved**、**最小上传间隔（毫秒）**、**最大上传大小（字节）**。

#### TUN（`tun`）

| 字段 | 标签 | 描述 | 默认值 |
|---|---|---|---|
| name | — | *「TUN 接口的名称。」* | **`xray0`** |
| mtu | — | *「最大传输单元。数据包的最大大小。」* | **1500** |
| `userLevel` | **用户等级** | *「通过此入站流建立的所有连接都将使用此用户等级。」* | **0** |

### 11.10. 日志与统计（Stats, metrics）

#### 日志（`log`）

提示：*「日志可能拖慢服务器运行。仅在需要时启用你所需要的日志类型！」* 标准模板的 `log` 部分：`access: "none"`、`error: ""`、`loglevel: "warning"`、`dnsLog: false`、`maskAddress: ""`。

| 字段 | 标签 | JSON | 描述 | 默认值 |
|---|---|---|---|---|
| `logLevel` | **日志等级** | `loglevel` | *「错误日志的日志等级…」* 取值：`debug`、`info`、`warning`、`error`、`none`。 | **`warning`** |
| `accessLog` | **访问日志** | `access` | *「访问日志文件的路径。特殊值「none」禁用访问日志。」* | **`none`** |
| `errorLog` | **错误日志** | `error` | *「错误日志文件的路径。特殊值「none」禁用错误日志。」* | **`""`**（默认） |
| `dnsLog` | **DNS 日志** | `dnsLog` | *「启用 DNS 查询日志」* | **false** |
| `maskAddress` | **地址掩码** | `maskAddress` | *「启用后，日志中的真实 IP 地址将被替换为掩码地址。」* | **`""`**（关闭） |

#### 统计（`stats` / `policy`）

**统计** 分组。在 `policy.system` 和 `policy.levels` 中启用计数器。在标准模板中：`statsInboundUplink: true`、`statsInboundDownlink: true`、`statsOutboundUplink: false`、`statsOutboundDownlink: false`；对于等级 `0` — `statsUserUplink: true`、`statsUserDownlink: true`。

| 字段 | 标签 | 描述 | 默认值 |
|---|---|---|---|
| `statsInboundUplink` | **入站上行统计** | *「为所有入站代理的出站流量启用统计采集。」* | **true** |
| `statsInboundDownlink` | **入站下行统计** | *「为所有入站代理的入站流量启用统计采集。」* | **true** |
| `statsOutboundUplink` | **出站上行统计** | *「为所有出站代理的出站流量启用统计采集。」* | **false** |
| `statsOutboundDownlink` | **出站下行统计** | *「为所有出站代理的入站流量启用统计采集。」* | **false** |

> 按客户端和 inbounds 的统计（uplink/downlink）是仪表盘和客户端流量显示的基础；不建议关闭。outbound 统计默认关闭，仅当你按出站标签跟踪流量时才需要。

#### Metrics

标准模板中存在 `metrics` 部分（`listen: "127.0.0.1:11111"`、`tag: "metrics_out"`）以及相应的 API `metrics_out`。面板用此监听器收集指标和 observatory 快照：它从模板解析 `metrics.listen`，轮询 `/debug/vars` 并按标签聚合延迟历史。如果你更改 `metrics.listen` 的地址/端口，面板会访问新地址；删除 `metrics` 部分将关闭 observatory 图表的采集。

> 以 HTTP 模式测试 outbound 会启动一个**独立的临时** Xray 实例，带有运行在随机端口上自己的 `metrics`-listener——这与主配置中的 listener 不是同一个。

### 11.11. 保存、重启与自动转换

#### 按钮

| 按钮 | 动作 |
|---|---|
| **保存** | `POST /xray/update`：校验并保存模板 + `outboundTestUrl`。 |
| **重启 Xray** | 以已保存的配置重新加载服务。确认：*「重启 xray？」* / *「以已保存的配置重新加载 xray 服务。」* |

提示：成功 — *「Xray 重启成功」*、*「Xray 停止成功」*；错误 — *「重启 Xray 时发生错误。」*、*「停止 Xray 时发生错误。」* 窗口 **Xray 重启输出** 显示内核的诊断输出。

#### 热应用更改（无需完整重启）

inbounds、outbounds 和路由规则的更改会「实时」应用：点击 **保存** 时，面板计算新旧配置之间的差异，并仅通过 Xray 的 gRPC-API（HandlerService/RoutingService）应用变化的部分，而不重启进程。仅当更改了没有热重载 API 的部分（`log`、`dns`、`policy`、`observatory` 等）时，才会自动执行完整重启。因此 Xray 页面无需单独的「重启」按钮——**保存** 本身就会应用更改。必要时内核仍会自动重启（另见订阅更新和 WARP 轮换时的自动重载）。

#### 恢复默认模板

端点 `GET /xray/getDefaultJsonConfig` 返回标准模板（内置于二进制中的 `config.json`）。可用它把配置重置为出厂状态。

#### 保存时的自动转换

保存 Xray 设置时，面板会执行（按此顺序）：

1. **剥离封装** — 如果形如 `{ "xraySetting": <配置>, "inboundTags": …, "outboundTestUrl": … }` 的封装意外进入了值中，则将其剥除（否则每次保存都会层层累积）。最多剥离 8 层。
2. **配置校验** — JSON 被解析为 Xray 配置结构；出错时——拒绝并报 *「xray template config invalid」*。
3. **确保统计规则** — 规则 `inboundTag: ["api"] → outboundTag: "api"` 被强制提升到 `routing.rules` 的位置 0（若不存在则添加）。这保证面板的 gRPC 统计请求不会被上方的 catch-all 规则拦截（否则在代理正常工作时，客户端可能显示为离线且零流量）。

> 由于第 3 点，请不要尝试删除或移动 `api → api` 规则——面板在下次保存时仍会把它放回原位。这是统计基础设施的一部分，而非用户的路由。

### 11.12. 来自订阅的 outbound（带自动更新）

从 3.3.0 版起，面板可直接从订阅 URL 导入 `outbound`——与 VPN 提供商发给客户端应用的格式相同。订阅会在后台定期重读，因此服务器上的 `outbound` 集合无需手动编辑配置模板即可保持最新。

在中文界面中，该部分名为 **「出站订阅」**，描述：「从远程订阅 URL 导入出站（vmess/vless/trojan/ss/...）。标签保持不变，以便在负载均衡器和路由规则中使用。更新自动执行。」该部分位于 Xray 页面，`outbound` 配置面板之上。

#### 它的工作方式

订阅与 Xray 配置模板分开存储。模板**永不被改写**：从订阅获取的 `outbound` 在每次生成 Xray 配置时动态加入最终配置。

#### 添加订阅

在「添加订阅」表单中提供以下字段：

| 字段 | 键 | 默认值 | 用途 |
|------|------|--------------|------|
| 订阅 URL | `url` | —（必填） | 订阅地址。占位符：「https://...（base64 链接列表）」。仅接受 HTTP(S)；地址会做安全检查。 |
| 备注 | `remark` | 空 | 任意标记（占位符「例如 HK 节点」）。 |
| 标签前缀 | `tagPrefix` | `subN-` | 导入的 `outbound` 标签的起始前缀。如果留空，面板会自动选取形如 `sub1-`、`sub2-` 等的最小空闲编号。 |
| 更新间隔 | `updateInterval` | 600 秒（10 分钟） | 多久重读一次订阅。UI 中以小时/分钟设定。 |
| 已启用 | `enabled` | 是（`true`） | 只有已启用的订阅才进入配置并自动更新。 |
| 允许私有地址 | `allowPrivate` | 否（`false`） | 允许 localhost、LAN 和私有 IP 的 URL。出于防 SSRF 默认关闭——仅对受信任的本地源启用。 |
| 在手动出站之前 | `prepend` | 否（`false`） | 启用时，该订阅的 `outbound` 排在模板的手动 `outbound` **之前**，其中之一可能成为默认 `outbound`。否则它们排在**之后**。 |

**「预览」** 按钮（`POST /outbound-subs/parse`）可在保存前下载并解析 URL，看会得到哪些 `outbound` 和标签；此过程不向数据库写入任何内容。如果该 URL 未识别出任何内容，会显示「此 URL 未找到出站。」

多个订阅在 `outbound` 总列表中的顺序由优先级（`priority`）决定，并通过上/下箭头更改（`POST /outbound-subs/:id/move`）。

#### 接受哪些订阅格式

按 URL 取回的响应体处理方式如下：

- 内容首先尝试作为 **base64**（标准和 URL-safe 两种变体，自动补全填充并去除空格/换行）。如果是 base64——则解码；否则按原样使用。
- 然后将内容体按行拆分。每个非空且不以 `#` 开头的行被解析为链接。无法识别的行（注释、不支持的协议）被静默跳过。
- 支持的链接方案：`vmess://`、`vless://`、`trojan://`、`ss://`（Shadowsocks）、`hysteria2://` / `hy2://`、`wireguard://` / `wg://`。

也就是说，与大多数提供商一样的普通「base64 编码链接列表」订阅即可适用。

#### 稳定标签

为每个链接计算一个稳定的「身份」（去掉备注片段的 URI 核心；对于 vmess——是去掉 `ps` 字段的内部 JSON）。「身份 → 标签」的对应关系会被保存，在下次更新时同一服务器获得同一标签，即使备注或次要参数发生了变化。这是特意设计的，以便负载均衡器和路由规则在更新后继续工作：

- 负载均衡器/规则中的精确标签会继续指向同一服务器。
- 前缀/通配选择器（例如 `hk-*`）会自动接纳订阅之后返回的新服务器——这是「订阅一个池」的推荐方式。
- 如果某服务器从订阅中消失，它的标签就从最终的 `outbound` 数组中消失；若负载均衡器设置了 `fallbackTag`，Xray 会使用它。
- 如果提供商更改了服务器的 UUID/主机/凭据，身份就会改变——这会被视为带有新标签的新 `outbound`。

在同一次抓取内部，标签通过后缀 `-N` 去重。来自订阅的标签保留非 ASCII 字符（例如西里尔字母）并保持可读：Unicode 字母和数字在 slug 中保留，标点替换为连字符——来自西里尔名称的标签不再被缩减为纯数字。

#### 自动更新如何工作

- 订阅更新的后台任务按计划**每 5 分钟**运行一次。
- 每次运行时，它会遍历所有已启用的订阅，仅更新自身间隔已到期的那些：如果订阅从未更新过，或自上次更新以来过去的时间不少于其 `updateInterval`，则更新它。这样任务会频繁检查订阅，但每个具体订阅的重读不会快于其 `updateInterval`（默认 10 分钟）。UI 中以相应提示反映了这一点。
- 更新：URL 会重新作为公共地址做安全检查（若订阅未设置 `allowPrivate`，则私有地址被阻断），请求通过面板的代理客户端发出，带头 `User-Agent: 3x-ui-outbound-sub/1.0`。重定向链被限制为 10 跳，且每一跳同样会做私有性检查（防 SSRF）。期望返回 HTTP 200；否则记录错误。
- 解析成功后保存结果，记录最后更新时间，清除错误。出错时其文本会在 UI 中显示为「最后错误」，而先前获取的 `outbound` 仍然有效。
- 如果至少有一个订阅确实更新了，任务会标记 Xray 需要重启，并发出 UI 失效以让界面拉取新的 `outbound`。Xray 的实际重载发生在管理器最近的 30 秒周期内。

手动更新单个订阅——按钮 **「立即更新」**（`POST /outbound-subs/:id/refresh`）；它也会标记 Xray 需要重启。添加、修改、删除订阅同样会置位 Xray 重启标志（删除时其 `outbound` 会在下次重载时从配置中移除）。UI 提示：「添加或更新后请重启 Xray（或等待下次自动重载），以使出站生效。」

#### 它如何进入 Xray 配置

每次生成 Xray 配置时，激活的订阅 `outbound` 被分为两组——`prepend`（「在手动出站之前」标志）和其余的——并与模板拼接：`[订阅的 prepend] + [模板的 outbound] + [其余订阅]`。每组内部，订阅按优先级排列。模板中的手动 `outbound` 不受影响；如果模板的 `outbound` 数组因某种原因解析失败，则不向其中混入订阅的 `outbound`（以免丢失手动的）。

导入的 `outbound` 还会在 `outbound` 面板本身中以单独的 **「来自出站订阅（只读）」** 块显示——在那里无法编辑它们，管理只能通过「出站订阅」部分进行。

### 11.13. WARP 中的 IP 轮换

在 3X-UI 中可以建立 WARP-outbound——一个到 Cloudflare WARP 的出站 WireGuard 连接（Xray 配置中标签为 `warp`）。面板会自行在 Cloudflare 服务器上注册一个设备账户，获取 WireGuard 密钥和地址，并将它们填入标签为 `warp` 的 outbound。流量经由这样的 outbound 以 Cloudflare WARP 的 IP 地址出口到互联网。3.3.0 版的新功能——可以手动或按计划更换该出站 IP，而无需手动重建 WARP 账户。

管理位于 **Xray** 部分的 WARP 卡片中（在点击「创建 WARP 账户」并获取配置之后；在此之前操作不可用——面板会提示「请先获取 WARP 配置」）。

#### 更换 IP 时会发生什么

按钮 **「更换 IP」** 启动 IP 更换。逻辑：

1. 生成一对新的 WireGuard 密钥。
2. 用新密钥在 Cloudflare 服务器上重新注册 WARP 设备（新的 `device_id`、`access_token`、地址和 peer 数据）。
3. 新数据写入 Xray 配置的 WARP-outbound：更新 `secretKey`、`address`（v4 `/32` 和 v6 `/128`）、`reserved`（来自 `client_id`），以及 peer 的 `publicKey` 和 `endpoint`。
4. 如果先前设置了 WARP+ 许可密钥（长度不少于 26 字符），它会自动重新安装到新账户上。若失败，这只是日志中的一条警告——IP 更换不会取消。
5. 成功更换后，Xray 被标记为需要重启，以使新 outbound 生效。

成功时界面显示「WARP IP 地址更换成功！」。

#### 按计划自动轮换

WARP 卡片中有一个 **「自动更新 IP 地址」** 开关和一个 **「间隔（天）」** 字段。提示：「0 — 关闭。自动更换 IP 地址。」

| 参数 | 值 |
|---|---|
| 数据库中的设置 | `warpUpdateInterval`（整数，≥ 0） |
| 默认值 | `0`（自动轮换关闭） |
| 单位 | 天 |
| `0` | 关闭自动更换 |
| `> 0` | 每 N 天更换一次 IP |

写入间隔会保存 `warpUpdateInterval`，且当值大于 0 时，将「最后更新时间」重置为当前时刻——否则调度器会在最近一个 tick 上就更换 IP。

计划由一个每小时运行一次的后台任务执行——也就是说面板每小时检查一次是否到了轮换的时候。检查算法：

- 如果间隔 ≤ 0 — 什么都不做；
- 如果「最后更新时间」为 0（例如间隔是通过直接编辑数据库设置的）— 这是首次运行：任务仅记录一个基准时间戳，并**不**立即更换 IP；
- 如果自最后更新以来过去的时间不少于 `间隔 × 24 × 3600` 秒 — 执行同样的 IP 更换，更新时间戳并计划 Xray 重启。

一个重要细节：通过「更换 IP」按钮的手动更换也会重置最后更新时间戳。因此手动轮换之后，自动间隔的计时会重新开始，计划更换不会紧随其后立即触发。

#### 「通过面板代理」

> **3.3.1 中已更改。** 单独的「面板网络代理」设置（`panelProxy`）已被移除。面板自身的出站流量（包括对 WARP API 的请求）现在通过选定的 **面板流量 outbound** 引导——Xray-outbound 或负载均衡器（见 [13](#13-面板设置) 部分）。下面的说明适用于 3.3.1 之前的版本。

所有对 Cloudflare WARP API 的请求（注册、获取配置、设置许可、更换 IP）都不直接发出，而是通过面板的 HTTP 客户端进行，超时 15 秒。该客户端尊重面板设置中的 **「面板网络代理」**（`panelProxy`）设置。

来自该设置的说明：代理会路由面板自身的出站请求（geo 数据库更新、Xray/面板版本检查、Telegram，以及现在对 WARP 的访问）——以绕过服务端过滤。接受形如 `socks5://` 或 `http(s)://` 的地址，例如 Xray 自身的本地 SOCKS-inbound。如果该字段为空或代理设置不正确——则使用直连（行为不会被破坏）。

对 WARP 的好处：如果服务器无法直接访问 `api.cloudflareclient.com`，注册和轮换以前会失败。现在，在 `panelProxy` 中指定一个可用的代理（包括 Xray 自己的 inbound），就能保证 WARP API 的可达性，以及手动按钮和计划轮换都能正常工作。

#### 何时有用

- 为经由 WARP 的 outbound 定期更换出站 IP——降低因单一地址而被封锁和追踪的风险。
- 当当前 Cloudflare 地址进入黑名单或运行缓慢时，手动「刷新」IP。
- 对于无法直接访问 Cloudflare WARP API 的服务器：通过 `panelProxy` 路由请求可使注册和轮换正常工作。

---

## 12. 节点（多面板，master/slave）

**节点** 一节可将普通的 3X-UI 安装变成 **中央（主，master）面板**，由它远程监视并管理其他（子）3X-UI 面板。每个节点都是部署在各自服务器上的独立 3X-UI 安装；主面板通过节点自身的 HTTP API 与其通信，轮询其状态，并把分配给它的 inbound 和客户端同步到节点上。这正是 **多面板** 能力：你不必逐一登录每个面板，而是在同一个列表中看到所有服务器并集中管理它们。

一个重要原则：**节点不是代理（agent），而是一个完整的 3X-UI 面板。** 主面板不会在节点上「安装」任何东西，它只是凭令牌连接到节点的 API。把节点从列表中删除只会停止监控；远端面板本身不受影响（提示：「这将停止对该节点的监控。远端面板本身不会受到影响」）。

### 12.1. 列表顶部的汇总

节点表格上方会显示聚合计数：

| 字段 | 说明 |
|---|---|
| 节点总数 | 列表中节点的总数。 |
| 在线 | 有多少节点处于 `online` 状态。 |
| 不在线 | 有多少节点处于 `offline` 状态。 |
| 平均延迟 | 到各节点的平均延迟（ping），单位毫秒。 |

### 12.2. 添加与编辑节点

**添加节点** 和 **修改节点** 按钮会打开包含节点字段的表单。

**名称**、**地址**、**端口** 和 **API Токен** 为必填字段（提示：「名称、地址、端口和 API 令牌为必填项」）。

点击「保存」时（无论是添加还是修改），面板都会 **先检查节点的可达性**，超时为 6 秒。如果节点没有响应，记录将不会保存并显示错误。也就是说，无法添加一个明显不可达的节点。

#### 表单字段

| 字段（RU） | 默认值 | 允许的取值 | 说明 |
|---|---|---|---|
| 名称 | —（必填） | 非空字符串，**唯一** | 节点的内部名称。名称列具有唯一性约束——不能创建两个同名节点。占位提示：`napr. de-frankfurt-1`。保存时会去掉两端空白。 |
| 备注 | 空 | 任意字符串 | 节点的可选备注/描述。不影响工作。 |
| 方案 | `https` | `http` / `https` | 连接到远端面板所用的协议。如果留空或填写了不允许的值，归一化会将其设为 `https`。如果节点以普通 HTTP 响应而方案设为 `https`，面板会返回清晰的提示：「the server speaks HTTP, not HTTPS; set the node scheme to http」。 |
| 地址 | —（必填） | 主机名或 IP | 远端面板的地址。占位提示：`panel.example.com или 1.2.3.4`。地址会被归一化；默认禁止私有/本地地址以防 SSRF——参见「允许私有地址」。 |
| 端口 | —（必填） | 整数 **1–65535** | 远端节点 Web 面板的端口。超出范围的值会被拒绝（「node port must be 1-65535」）。 |
| 基础路径 | `/` | 路径字符串 | 远端面板的基础路径（web base path），如果设置了的话。会被归一化：保证以 `/` 开头和结尾（空值 → `/`）。轮询时面板会在其后追加 `panel/api/server/status`。 |
| API Токен | —（必填） | 远端面板的令牌 | 访问节点 API 的 Bearer 令牌。通过 `Authorization: Bearer <token>` 头传递。占位提示：「来自远端面板设置页的令牌」。提示：「远端面板在 设置 → API 令牌 一节中显示其 API 令牌」。也就是说令牌要 **在节点本身上** 创建（设置 → API 令牌），再粘贴到这里。 |
| 已启用 | `true` | 是/否 | 启用节点的监控与同步。被禁用的节点 **不会被** 后台任务轮询（heartbeat 和 traffic-sync 会跳过它们），也不参与面板的批量更新。 |
| 允许私有地址 | `false` | 是/否 | 解除 SSRF 防护，允许通过私有/本地地址连接节点。提示：「仅对私有网络或 VPN 中的节点启用」。仅当节点确实位于私有网络中或可通过 VPN 访问时才启用。 |

#### 在节点侧获取与重新生成令牌

令牌在远端面板的 **设置 → API 令牌** 一节中获取。同一处也可以重新签发：**重新生成令牌** 按钮，并带有警告：「重新生成将使当前令牌作废。任何使用它的中央面板在更新前都会失去访问权限。是否继续？」。重新生成后，主面板中的旧令牌将不再有效——需要在节点表单中更新它。

#### 出站连接（Connection outbound）

**Connection outbound**（出站连接，`outboundTag`）字段设定主面板对该节点 API 的请求流量如何离开服务器。如果在其中选择某个 Xray outbound 标签，面板对节点的请求将不会直连，而是经由指定的 outbound；面板会自行在运行中的配置里添加一个 loopback 上的桥接 inbound，并实时生效，无需重启。提示：「Route this node's panel API traffic through the selected Xray outbound. A loopback bridge inbound is added to the running config automatically and applied live. Leave empty for a direct connection」。

该选择器的结构与面板中的 outbound 选择一致：标签分组为 **Outbounds**（普通出站）和 **Balancers**（负载均衡器），blackhole 出站从列表中隐藏。空值（占位提示「Direct connection」）= 直连到节点。

#### 导入 inbound（选择要同步的 inbound）

节点表单中有一个 **导入 inbound**（`inboundSyncMode`）设置，具有两种模式：**所有 inbound**（`all`，默认）和 **已选择**（`selected`）。默认情况下，主面板会把所有选中了该节点的 inbound 同步到节点上；现有节点继续以「所有 inbound」模式工作。

在 **已选择** 模式下，该字段下方会出现 inbound 标签的多选。点击 **加载 inbound**——主面板会根据已输入（尚未保存）的连接参数向节点请求其 inbound 列表（端点 `POST /panel/api/nodes/inbounds`）并显示它们的标签；勾选所需的即可。面板只会把勾选的标签同步并部署到节点上，而节点上直接存在的其余 inbound 将保持不变——主面板既不会删除它们，也不会管理它们。

**示例：为选择性导入请求节点的 inbound 列表。** 请求体中传入尚未保存的连接参数；响应中是节点上可用的 inbound 的标签：

```
POST /panel/api/nodes/inbounds
Content-Type: application/json

{ "name": "de-fra-1", "scheme": "https", "address": "node1.example.com",
  "port": 2053, "basePath": "/", "apiToken": "abcdef..." }
```

### 12.3. TLS 校验（用于 https 节点）

这组字段设定主面板如何校验节点的 HTTPS 证书。这些设置 **仅在 `https` 方案下有效**；对 `http` 节点会被忽略。

**TLS 校验**——下拉列表，提示：「面板如何校验节点的 HTTPS 证书。固定（pin）或跳过——用于自签名证书（仅限 https 节点）」。

| 模式（RU） | 取值 | 默认值 | 说明 |
|---|---|---|---|
| 校验（标准 CA） | `verify` | 是（default） | 由受信任 CA 进行常规的证书链校验。适用于持有公共/Let's Encrypt 证书的节点。所有 `http` 节点也使用此模式。 |
| 固定证书（SHA-256） | `pin` | — | 不校验 CA 链，但会将节点叶证书的 SHA-256 与保存的指纹比对（常量时间比较）。为 **自签名** 证书保留 MITM 防护。需要填写指纹字段。 |
| 跳过校验 | `skip` | — | 完全关闭证书校验。警告：「跳过校验会去除对「中间人」攻击的防护——API 令牌可能被截获。最好固定证书」。 |

在以上三种模式之外，3.4.0 又增加了第四种——**Mutual TLS (client certificate)**（`mtls`），与其余模式一样，仅在 `https` 方案下可用。

| 模式（RU） | 取值 | 默认值 | 说明 |
|---|---|---|---|
| Mutual TLS（客户端证书） | `mtls` | — | 除校验节点证书之外，主面板还额外用 **客户端证书**（由其自身的 CA 签发）向节点证明自己的身份。对于处于此模式的节点，**API 令牌变为可选**——节点凭证书识别主面板。选择该模式时会显示提示：「This node authenticates the panel with a client certificate. Copy this panel's CA from the Node mTLS section onto the node, set its Trusted parent CA, then restart it」。 |

要为某个节点启用双向 TLS：在节点侧设置 **Mutual TLS** 模式，从 **Node mTLS** 一节（见下文）复制管理面板的 CA，在节点上把它配置为 **可信父级 CA**，并重启该节点。

如果选择了除 `skip`、`pin` 或 `mtls` 之外的任何值，归一化会强制设为 `verify`。

#### 固定证书

选择 **固定证书** 时会出现：

- **固定证书的 SHA-256**——输入字段。接受 **base64** 格式的指纹（Xray 的 `pinnedPeerCertSha256` 格式）或带冒号或不带冒号的 **hex**（`openssl -fingerprint` 风格）。提示：「节点证书的 SHA-256，base64 或 hex 格式。点击「获取」可立即从节点读取它」。占位提示：「base64 或 hex 格式的 SHA-256」。选择 `pin` 时，保存时空的或不正确的指纹会触发校验错误。

**示例：同一个指纹的两种格式。** 该字段接受任意一种写法——两者表示同一张证书：

```
# base64 (формат pinnedPeerCertSha256 из Xray)
6O7TNg3l2k0pq8R1sT2uV3wX4yZ5a6B7c8D9e0F1g2=

# hex с двоеточиями (стиль openssl x509 -fingerprint -sha256)
E8:E2:D3:60:DE:5D:9A:4D:29:AB:CF:11:B2:7C:34:...
```

如果指纹尚未知晓，点击 **获取**——主面板会自行通过 HTTPS 从节点读取并填入字段。
- **获取** 按钮——以不校验证书的方式通过 HTTPS 连接节点，读取当前叶证书的 SHA-256（端点 `POST /certFingerprint`），并填入字段。成功后——「已获取节点当前证书」；失败时——「无法获取证书」。仅对 https 节点可用。

#### Node mTLS（面板之间的双向 TLS 认证）

在 **节点** 页面上有一个单独的 **Node mTLS** 一节——配置双向 TLS 认证，在 API 令牌之外为「面板 → 节点」调用增加第二个因素（客户端证书）。双向 TLS 是按需启用的；如果该节的字段为空，节点将沿用原有方案——**仅使用 API 令牌**（提示：「Mutual TLS adds a client-certificate factor on top of the API token for node-to-node calls. It is opt-in: leave it empty to keep token-only auth」）。该节有两个操作：

- **复制本面板的 CA**（`POST /panel/api/nodes/mtls/ca`）——把本面板的根证书（CA）复制到剪贴板。需要把该 CA 分发给受管节点，使它们信任本面板的客户端证书；之后在各节点上把 TLS 校验模式设为 **Mutual TLS**（提示：「Hand this CA to the nodes this panel manages, then set their TLS verification to Mutual TLS」）。复制后——「CA certificate copied to clipboard」。
- **可信父级 CA**（`Trusted parent CA`，`POST /panel/api/nodes/mtls/trustCA`）——当本面板自身作为上级（管理）面板的节点时使用的字段。把管理面板的 CA 粘贴到这里，以要求它出示客户端证书，然后点击 **Save trust CA**。此更改需要 **重启面板**（提示：「When this panel is itself a node, paste the managing panel's CA here to require its client certificate. Restart the panel to apply」）。

### 12.4. 每个节点显示的内容

节点表格的列与节点卡片的字段（观测到的状态，每次 heartbeat 轮询时填充）：

| 字段（RU） | 说明 |
|---|---|
| 状态 | `online` / `offline` / `unknown`——见下文。 |
| CPU | 远端服务器的处理器占用百分比。 |
| 内存 | 内存（RAM）使用百分比（按 `current/total*100` 计算）。 |
| 运行时长 | 服务器连续运行的时间（秒）。 |
| 延迟 | 节点对上一次轮询的响应时间（毫秒）。 |
| 上次 ping | 上次成功 heartbeat 的时间（unix 秒；`0` =「从未」；近期的值显示为「刚刚」）。 |
| Xray 版本 | 节点上运行的 Xray-core 版本。 |
| 面板版本 | 节点上 3X-UI 的版本——与当前版本比对以提供更新指示。 |
| (inbounds) | 该节点上实际部署了多少 inbound。 |
| (客户端) | 节点 inbound 上的客户端数量。 |
| (在线) | 节点上当前在线的客户端数量。 |
| (已耗尽) | 节点上有多少客户端 **已到期或耗尽流量限额**。手动禁用的客户端不计入此计数。 |
| (速度) | 节点上部署的 inbound 上的当前（实时）传输速度。 |

inbound/客户端/在线计数通过节点稳定的 GUID（`panelGuid`）而非本地 id 与节点关联——这样子节点上的客户端就会被计在子节点名下，而不是计在它经由其同步的中间节点名下。

对于部署在节点上的 inbound，页面会显示在线客户端、计数器以及 **当前传输速度**。基于稳定 GUID 的关联还能正确区分具有相同 `panelGuid` 的「克隆」节点。

#### 节点状态

| 状态 | RU | 何时设置 |
|---|---|---|
| `online` | 在线 | 节点对 `panel/api/server/status` 轮询返回了 `success=true`。 |
| `offline` | 不在线 | 节点没有响应、返回 HTTP 错误、`success=false`，或返回无法识别的响应。 |
| `unknown` | 未知 | 初始值，节点尚未被轮询过。 |

轮询失败时，错误文本会被保存并以清晰的措辞显示，有助于诊断「offline」的原因。

### 12.5. 对节点的操作

- **测试连接**（`POST /test`）——在节点表单中根据已输入（尚未保存）的参数测试连通性，超时 6 秒。结果：「连接正常（{ms} 毫秒）」或「无法连接」。便于在保存前调试地址/端口/令牌/TLS。
- **立即检查**（「立即检查」按钮，`POST /probe/:id`）——对已保存节点的计划外轮询；立即更新状态与指标（CPU/内存/运行时长/延迟/版本）并记录 heartbeat。失败时——「检查失败」。

**示例：通过主面板 API 测试并轮询节点。** 「测试连接」对表单中尚未保存的参数进行测试：

```
POST /panel/api/nodes/test
Content-Type: application/json

{ "scheme": "https", "address": "de-frankfurt-1.example.com", "port": 2053,
  "basePath": "/", "apiToken": "eyJhbGci...", "tlsMode": "verify" }
```

对 id 为 7 的已保存节点进行计划外轮询：

```
POST /panel/api/nodes/probe/7
```
- **更新面板**（`POST /updatePanel`，请求体 `{ids:[…]}`）——在节点上启动其内置的自更新器：节点下载最新的 3X-UI 发行版并在其上重启。**更新选中的（{count}）** 按钮可一次性对多个勾选的节点执行此操作。每个节点旁会显示指示：**有可用更新** 或 **已是最新**，依据节点面板版本与最新版本的比较得出。

**示例：用一个请求更新多个节点。** 请求体中传入勾选节点的 id；只有已启用且 `online` 的节点会被更新，其余的会作为已跳过返回。

```
POST /panel/api/nodes/updatePanel
Content-Type: application/json

{ "ids": [3, 7, 12] }
```

形如「已在 2 个节点上启动更新，1 个失败」的响应：例如节点 12 可能处于 offline 因而被跳过。
  - 确认：「将 {count} 个节点更新到最新版本？每个选中的节点都会下载最新发行版并重启。只有处于在线的已启用节点会被更新」。
  - **只有处于 `online` 状态的已启用节点会被更新。** 被禁用的节点在结果中标记为「node is disabled」，offline 的标记为「node is offline」。汇总：「已在 {ok} 个节点上启动更新，{failed} 个失败」。如果没有选中任何合适的节点——「请至少选择一个在线的已启用节点」。
- **Set Cert from Panel**（辅助操作，`GET /webCert/:id`）——在节点上创建 inbound 时，允许填入节点 **自身** Web-TLS 证书的路径（而非中央面板的），以保证文件确实存在于该节点上。要求节点已启用且可达。
- **删除节点**（`POST /del/:id`）——确认：「删除节点 "{name}"？这将停止对该节点的监控。远端面板本身不会受到影响」。删除节点记录及其累积的流量统计；远端面板照常继续运行。**只有在节点上的所有 inbound 都已移除之后，才能删除该节点。** 如果仍有至少一个 inbound 绑定到该节点（通过 `node_id`），面板会拒绝删除并报出形如「cannot delete node: N inbound(s) still attached to it; detach or delete them first」的错误——请先解绑或删除这些 inbound，然后再删除节点。这避免了出现仍带有指向已删除节点的悬空引用的「孤立」inbound。

### 12.6. 指标历史

历史按钮/图表会请求 `GET /history/:id/:metric/:bucket`。可用的指标：**`cpu`** 和 **`mem`**——它们在每次成功的 heartbeat 时累积。聚合区间大小（`bucket`，单位秒）受白名单限制：

**示例：请求历史。** 节点 7 的 CPU 占用图表，按 60 秒区间聚合（返回最多 60 个数据点）：

```
GET /panel/api/nodes/history/7/cpu/60
```

对于内存和「实时」模式（2 秒）——分别为 `…/7/mem/60` 和 `…/7/cpu/2`。白名单之外的值会被拒绝（「invalid metric」/「invalid bucket」）。

| Bucket（秒） | 用途 |
|---|---|
| 2 | 实时模式 |
| 30 | 30 秒区间 |
| 60 | 1 分钟区间 |
| 120 | 2 分钟区间 |
| 180 | 3 分钟区间 |
| 300 | 5 分钟区间 |

返回最多 60 个数据点。不允许的指标或 bucket 会被拒绝（「invalid metric」/「invalid bucket」）。

### 12.7. inbound 与客户端如何同步

inbound 通过 `node_id` 字段「归属于」节点（在 inbound 编辑器中选择节点）：

**示例：节点表单中的令牌。** 令牌在子面板上获取（设置 → API Токен）并粘贴到主面板的 **API Токен** 字段。每次轮询时主面板都会在请求头中发送它：

```
GET https://panel.example.com:2053/panel/api/server/status
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abc123...
```

如果子面板设置了 **基础路径**（web base path），例如 `/secret/`，主面板会自行把它放在 `panel/api/server/status` 之前 → `https://panel.example.com:2053/secret/panel/api/server/status`。

1. **配置部署（reconcile）。** 当与某节点关联的任何 inbound/客户端发生变更时，该节点会被标记为「脏」。后台任务会为每个处于 `online` 状态的已启用节点，在存在变更时把其 inbound（按 `node_id`）部署到节点上，然后清除「脏」标志。被禁用、offline 或「脏」的节点被视为「待处理」——对它的部署会推迟到连接恢复之后。
2. **流量采集。** 同一任务会向节点请求一份流量快照并合并进本地统计。基于合并后的流量执行限额/期限耗尽检查，并在必要时禁用客户端；该节点的「已耗尽」计数正反映这一点。如果节点不可达，则其在线客户端会被清空。

   对于同时绑定到多个面板的客户端，master 在同一任务中还会向各节点额外下发该客户端 **跨所有面板汇总** 的流量消耗（在节点上以单独一张表存储，键为主面板的 GUID；每次下发都会覆写，因此主面板侧的重置也会随之传播）。在节点上，客户端流量显示两个值中较大者——本地值或下发值——而当超过总配额时，客户端会 **在节点本地** 被禁用（通过自动禁用时同样的 Xray 重启机制，从而断开已建立的连接）。这消除了以下情形：节点只看到自己那部分流量，少算了消耗，从而继续为已耗尽总限额的客户端提供服务。当客户端被重置流量、自动续期或删除时，下发的计数会被清空。
3. **Heartbeat。** 一个独立的后台任务会定期（带并发限制）通过 `panel/api/server/status` 轮询所有 **已启用** 的节点，更新状态/指标/版本，并在有 Web 客户端时通过 WebSocket 推送更新后的节点树。

### 12.8. 节点链（子节点 / 传递节点）

拓扑不一定是扁平的：一个节点本身也可以是其自身节点的主面板。这类下级面板会在你这里显示为 **子节点**——它们是从直接节点获取的 **「只读」投影**。

- 提示：「只读：可通过 {parent} 访问的下属节点。请从它自己的面板 {parent} 中管理它」。也就是说，子节点不能在这里编辑、删除或更新——对它的所有操作都在它直接父级的面板中执行。
- 子节点的身份由其 GUID 确定；因此在线客户端和 inbound 会被准确地计在实际承载它们的物理节点名下，即使在 `Node1 → Node2 → Node3` 这样的链中也是如此（主面板每次经由一个直接节点「向内深入」一层）。
- 如果直接节点变得不可达，它的子节点缓存会被清空，子节点会从树中消失，直到连接恢复。

### 12.9. 节点：3.3.0 中的新内容

在 3.3.0 版本中，**节点** 一节获得了三项显著改进：在多级（multi-hop）拓扑中正确归因流量与在线客户端、节点之间的 client-IP 同步，以及在节点面板存活但其上 Xray 核心已崩溃的情况下单独的状态指示。后文中 inbound/outbound 一词不再翻译。

#### 1. Multi-hop：沿子节点链正确归因流量

以前计数（inbound 数量、在线客户端、已耗尽）是在「直接」节点这一层级统计的。如果你有一条形如 `主面板 → 节点1 → 节点2 → 节点3` 的链，所有物理上存在于 `节点2`/`节点3` 上的东西都会被错误地算到 `节点1` 头上——因为它们是经由 `节点1` 到达主面板的。在 3.3.0 中，归因按照真实来源进行。

其工作方式：

- **子节点会作为单独的行显示。** 每个面板都会发布自己的直接节点列表；只有具有已知 `Guid` 的节点才会被纳入——需要稳定的身份才能把节点归到上方一个「跳」处。主面板会定期（从 heartbeat 任务中）拉取并缓存这些列表，然后把「传递」子节点添加到直接节点之下。
- **传递节点为只读。** 在 UI 中它们被标记为 **「子节点」**，并带提示：*「只读：可通过 {родитель} 访问的下属节点。请从它自己的面板 {родитель} 中管理它。」* 这种行没有管理按钮——节点由其直接父级的面板管理。
- **通过 GUID 形成层级。** 对于直接节点，`ParentGuid` 就是主面板自身的 GUID；对于传递节点，则是其父节点的 GUID。树就是这样构建的。
- **计数的真实来源是 inbound 上的 `origin_node_guid`。** 这是物理上持有该 inbound 的节点的 `panelGuid`。它在从节点同步 inbound 时被写入，并在后续各跳中 **原样保留**，因此深度嵌套的 inbound 会被归到真实节点上，而不是中间节点上。计数（inbound 数量、在线客户端、已耗尽客户端）会按此 GUID 重新计算。选键逻辑：

  | inbound 状态 | 归因到 |
  |---|---|
  | 设置了 `origin_node_guid` | 该 GUID（真实的来源节点） |
  | 为空，但设置了 `node_id` | 节点的合成 GUID（旧版本，尚未上报自己的 `panelGuid`） |
  | 为空且 `node_id` 为空 | 主面板自身的 GUID（本地 Xray 上的 inbound） |

  在线客户端同样按 GUID 分组，因此每个节点行只显示真正连接到它本身的客户端。

**用户所见：** 在扁平拓扑中（节点直接位于主面板之下）不会有任何变化——按 GUID 和按 `id` 的计数一致。但一旦出现节点链，列表中就会出现「子节点」行，且每个节点的 inbound/在线/已耗尽数量现在反映的正是它自身的负载，而不是所有经它中转的东西的总和。

#### 2. 节点之间从 access.log 同步 client-IP

按 IP 限制（客户端的 `limitIp`）依赖于 Xray 写入其 access.log 的地址。以前每个节点只能看到对自己的连接，因此「每个客户端不超过 N 个 IP」的限制在集群中不起作用：客户端可以连到不同的节点从而绕过限制。在 3.3.0 中，观测到的 IP 会在整个集群范围内同步。

其工作方式：

- 在每个节点上，后台任务会解析 access.log，从每一行中提取 IP、客户端 email 和时间戳，并存入本地表（每个 email 一条记录，IP 以 JSON 数组 `{ip, timestamp}` 形式存储）。本地地址 `127.0.0.1` 和 `::1` 会被丢弃。
- 同步 **每 10 秒** 对每个在线的已启用节点执行一次双向交换：从节点拉取 IP 并合并进本地表，然后把主面板的汇总视图回传给节点。
- 合并会把旧的与传入的观测结合起来，**不会重复计算** 在多个节点上看到的同一个 IP，也 **不会复活已过期的** 记录：采用与本地任务相同的陈旧阈值——**30 分钟**。对每个 IP 保留最新的时间戳。来自其他节点的记录会获得新的本地 id（各节点的 id 空间相互独立）；对同一 email 的并发插入受到去重保护。
- 在统计限额时，「活跃」的 IP 是指要么在当前本地扫描中被发现、要么在同步库中具有非常新的时间戳（**2 分钟以内**）的 IP。正是这一点让限额能在整个集群范围内生效，即使该地址是在另一个节点上被发现的。超过限额时，最旧的「活跃」IP 会被送入 fail2ban 日志，连接被强制断开（通过 Xray API 对客户端 remove/re-add）。

**用户所见：** 按 IP 数量的限制现在作用于整个集群，而不再是各节点各自为政；面板中按客户端可看到在任意节点上发现的 IP（在 30 分钟窗口内）。对此没有单独的按钮/设置——只要节点的 access.log 已启用且可访问，同步就会在后台自动进行（限额本身还需要节点上有 Fail2Ban）。

#### 3. 单独的状态指示：节点面板在线，但 Xray 已崩溃

以前节点状态本质上就是「在线 / 不在线」。如果节点面板有响应，节点就被算作在线——即便其上的 Xray 核心已不工作、客户端实际上无法连接。在 3.3.0 中，面板健康与 Xray 核心健康被区分开来。

其工作方式：

- 轮询节点时，主面板会从远端 `/panel/api/server/status` 的响应中取出 `xray.state` 和 `xray.errorMsg` 字段并保存在节点上。即使面板 ping 成功而核心不健康，这些字段也会被填充——正是为了把面板的可达性与 Xray 的状态区分开来。
- `xray.state` 的取值：`"running"`（运行中）、`"stop"`（已停止）、`"error"`（错误）。
- 这些取值被转换为节点状态。在原有状态之上新增了：

  | 状态键 | 中文标签 | 何时显示 |
  |---|---|---|
  | `online` | 「在线」 | 面板有响应，Xray 运行中（`running`） |
  | `offline` | 「不在线」 | 面板不可达 / ping 未通过 |
  | `unknown` | 「未知」 | 状态尚未确定 |
  | `xrayError` | 「Xray 错误」 | 面板在线，但 Xray 核心处于 `error` 状态（有 `errorMsg`） |
  | `xrayStopped` | 「已停止」 | 面板在线，但 Xray 已停止（`stop`） |

- 对于这类状态，UI 中使用 **单独的紫色指示**（区别于绿色「在线」和红色「不在线」的颜色）。紫色直白地表明：节点是能联系上的，问题出在 Xray 核心本身，而不是网络或面板本身。

**用户所见：** 在核心崩溃时，节点不再误导性地显示「绿色」，而是高亮为 **紫色**，状态为 **「Xray 错误」** 或 **「已停止」**。这能立即表明需要修的是节点上的 Xray（重启核心、查看 `errorMsg`），而不是去排查节点本身的可达性。同样的 `xrayState`/`xrayError` 也会透传到传递子节点（见第 1 点），因此核心的异常状态在整条链上都可见。

---

## 13. 面板设置

「设置」区域（页面标题为 **设置**，英文 *Panel Settings*）用于管理 3X-UI Web 面板本身的行为：它监听哪个地址和端口、如何受保护、如何与 Telegram 机器人及外部服务交互、在哪个时区执行计划任务。每个参数都以「键 — 值」对的形式存储在数据库的 `settings` 表中；如果数据库中没有相应的值，则应用默认值。

> **重要 — 应用更改。** 本页面上的任何更改都需要用 **保存**（*Save*）按钮保存，然后重启面板才能使更改生效。原文提示：「保存更改并重启面板以使其生效。」保存时会显示通知「设置已更改」。

### 13.1. 保存与重启面板

| 元素 | 用途 |
| --- | --- |
| **保存**（*Save*） | 将表单的所有字段写入数据库（`POST /panel/setting/update`）。写入前，值会经过校验——不正确的地址、端口或路径将被拒绝，面板会返回错误。 |
| **重启面板**（*Restart Panel*） | 重启面板的 Web 服务器（`POST /panel/setting/restartPanel`）。重启会延迟 3 秒进行。提示：「您确定要重启面板吗？确认后，重启将在 3 秒后进行。如果面板不可用，请检查服务器日志」。成功时显示「面板已成功重启」。 |
| **恢复默认设置**（*Reset to Default*） | 删除数据库中所有已保存的设置，之后面板使用默认值。此操作不会重置管理员凭据。 |

重启是通过向面板进程发送 `SIGHUP` 信号（或通过已注册的重启钩子）来执行的。在 Windows 上不支持通过信号自动重启。**监听参数（IP、端口、路径、域名、证书、时区）的更改只有在重启面板后才会生效。**

### 13.2. 通用设置（「面板」选项卡 / *General*）

#### 界面语言（*Language*）

面板 Web 界面的语言。可用语言：`en-US`（英语）、`ru-RU`（俄语）、`zh-CN`、`zh-TW`、`fa-IR`、`ar-EG`、`es-ES`、`id-ID`、`ja-JP`、`pt-BR`、`tr-TR`、`uk-UA`、`vi-VN`。这是显示设置，不影响 Xray 的工作。

#### 日历类型（*Calendar Type*）

- **键：** `datepicker`
- **默认值：** `gregorian`（公历）。
- **用途：** 日期选择中使用的日历类型（例如，在设置客户端有效期时）。提示：「计划任务将根据此日历执行。」备选值为波斯（贾拉里）历，这对面板的伊朗用户群体很有需求。

#### 分页大小（*Pagination Size*）

- **键：** `pageSize`
- **默认值：** `25`
- **允许值：** 从 `0` 到 `1000` 的整数。
- **用途：** 表格（连接/inbound 列表）中每页的行数。提示：「确定连接表格的页面大小。设为 0 可禁用」——当为 `0` 时，分页显示被禁用，所有记录以单一列表显示。
- **无需重启面板**（显示设置）。

#### 自动停用后重启 Xray（*Restart Xray After Auto Disable*）

- **键：** `restartXrayOnClientDisable`
- **默认值：** `true`
- **用途：** 当客户端被自动停用时（因有效期到期或达到流量上限），重启 Xray，以断开该客户端已建立的连接。提示：「当客户端因有效期结束或流量上限而被自动停用时，重启 Xray。」该功能本身没有变化——只是开关位于「面板」（*General*）选项卡上，与其他通用设置并列。

#### 备注模型与分隔符（*Remark Model & Separation Character*）

- **键：** `remarkModel`
- **默认值：** `-ieo`
- **用途：** 设定订阅中配置名称（remark）的生成方式。该字符串由**第一个字符**——分隔符，以及随后的**顺序字母序列**组成：
  - `i` — inbound 备注（*inbound remark*）；
  - `e` — 客户端 email；
  - `o` — 附加标记（*extra*）。
  
  默认值 `-ieo` 中分隔符为 `-`，各部分顺序为：inbound → email → extra（例如 `MyInbound-user@mail-extra`）。空的部分会被跳过。界面中的「示例备注」（*Sample Remark*）字段显示所生成名称的预览。是否将 email 纳入名称还取决于订阅设置中的「在名称中包含 Email」参数（参见订阅章节）。

**示例：`remarkModel` 的值如何影响配置名称。** 假设 inbound 名为 `VLESS-Reality`，客户端 email 为 `alex@vpn`，附加标记为 `RU`。那么：

| 字段值 | 最终名称（remark） |
| --- | --- |
| `-ieo`（默认） | `VLESS-Reality-alex@vpn-RU` |
| `_ie` | `VLESS-Reality_alex@vpn` |
| `-ei` | `alex@vpn-VLESS-Reality` |
| ` o`（空格分隔符，仅标记） | `RU` |

字符串的第一个字符始终是分隔符；其余字母决定哪些部分以何种顺序进入名称。

### 13.3. 面板访问：IP、端口、路径、域名、证书

这一组参数定义面板的网络入口点。**此处的所有更改只有在重启面板后才会生效。**

| 字段 | 键 | 默认值 | 描述 |
| --- | --- | --- | --- |
| 面板管理 IP 地址（*Listen IP*） | `webListen` | `""`（空） | Web 面板监听的 IP。空 = 在所有 IP 上监听。提示：「留空以允许从任意 IP 连接」。如果设置，则必须是正确的 IP 地址（否则保存会被拒绝）。 |
| 面板域名（*Listen Domain*） | `webDomain` | `""`（空） | 用于按域名校验请求的面板域名。空 = 接受来自任意域名和 IP 的连接。提示：「留空以允许从任意域名和 IP 连接。」 |
| 面板端口（*Listen Port*） | `webPort` | `2053` | 面板运行的端口。提示：「面板运行的端口」。允许 `1–65535`。端口必须空闲；面板与订阅服务不能同时使用相同的 `IP:端口` 组合。 |
| URI 路径（*URI Path*） | `webBasePath` | `/` | 面板 URL 的基础路径（basePath）。提示：「必须以 '/' 开头并以 '/' 结尾」。保存时，如果缺少前导和结尾的 `/`，面板会自动添加。路径中的非法字符会被拒绝。 |

##### 面板证书（TLS / HTTPS）

| 字段 | 键 | 默认值 | 描述 |
| --- | --- | --- | --- |
| 面板证书公钥文件路径（*Public Key Path*） | `webCertFile` | `""` | 证书（链）文件的完整路径。提示：「输入以 '/' 开头的完整路径」。 |
| 面板证书私钥文件路径（*Private Key Path*） | `webKeyFile` | `""` | 私钥文件的完整路径。提示：「输入以 '/' 开头的完整路径」。 |

如果设置了证书/密钥路径中的**至少一个**，面板在保存时会尝试加载「证书 + 密钥」对；如果出错（文件不存在、密钥与证书不匹配），保存会被拒绝。当两个正确的路径都已设置时，面板切换到 HTTPS。两个字段都为空 = 面板按普通 HTTP 工作。

> **安全警告**（*Security warnings*）。如果面板检测到不安全的配置，会显示「您的面板可能处于暴露状态：」警告块：
> - 按普通 HTTP 工作 —「请为生产环境配置 TLS」；
> - 标准端口 2053 —「将其改为随机端口」；
> - 默认基础路径 `/` —「将其改为随机路径」；
> - 标准订阅路径 `/sub/` 和 JSON 订阅 `/json/` —「请更改它」。
> 这些是建议，而非强制限制。

### 13.4. 会话、面板代理与受信任代理（「代理与服务器」选项卡 / *Proxy and Server*）

#### 会话时长（*Session Duration*）

- **键：** `sessionMaxAge`
- **默认值：** `360`（分钟，即 6 小时）。
- **允许值：** 从 `1` 到 `525600` 分钟（1 年）。
- **用途：** 管理员在无需重新登录的情况下保持登录状态的时长。单位为**分钟**。提示：「系统中的会话时长（单位：分钟）」。

#### 面板流量 Outbound（*Panel Traffic Outbound*）

- **键：** `panelOutbound`
- **默认值：** `""`（空 = 直连）。
- **用途：** 设定面板通过其发送**自身请求**的 Xray **outbound**——版本检查和面板/Xray 下载、对 Telegram 的访问、常规的 geo 文件更新——以绕过服务器端对 GitHub/Telegram 的过滤。该字段为**下拉列表**：其中列出了 Xray 配置模板中的 outbound、outbound 订阅中的 outbound，以及路由**负载均衡器**（单独分组）。列表中排除了 `blackhole` 类型的 outbound——把下载路由到「黑洞」毫无意义。原文提示：「将面板自身的请求——版本检查和面板/Xray 下载、Telegram 以及常规的 geo 文件更新——通过此 Xray 出站路由，以绕过服务器端对 GitHub/Telegram 的过滤。本地桥接入站会自动添加到运行中的配置并即时生效。Xray 内置的 Geodata 自动更新不受影响；它有自己用于下载的出站。留空以使用直连。」

> **工作原理。** 选择 outbound 后，面板会自动向运行中的配置添加一个服务用的回环 inbound（带标签 `panel-egress` 的 SOCKS 桥接）和一条路由规则，该规则将面板自身的 HTTP 流量转发到所选 outbound。如果选择了负载均衡器，规则中会代入 `balancerTag`，面板流量将在其成员之间分配。桥接和规则会**即时**生效，无需完全重启面板。留空字段以使用直连。Xray 内置的 geo 数据自动更新**不受**此设置影响——它在 Xray 路由内部有自己的 outbound。
- **格式：** `socks5://`（或 `socks5h://`）或 `http(s)://`，必要时带形如 `socks5://user:pass@host:port` 的认证。严格支持的协议为：`socks5`、`socks5h`、`http`、`https`——其他协议视为非法，此时面板会回退到直连。典型示例是 Xray 自身的本地 SOCKS 入站。
- 原文提示：「将面板自身的出站请求（geo 更新、Xray/面板版本检查、Telegram）通过此代理路由，以绕过服务器端对 GitHub/Telegram 的过滤。接受 socks5:// 或 http(s)://，例如 Xray 的本地 SOCKS 入站。留空以使用直连。」
- 无效的代理不会导致保存出错——面板只是使用直连并在日志中写入警告。

**字段值示例。** 如果服务器上已经在端口 `10808` 上运行了 Xray 的本地 SOCKS 入站，可将面板的自身请求通过它转发：

```
socks5://127.0.0.1:10808
```

对于带认证的外部 HTTP 代理：

```
http://user:pass@proxy.example.com:8080
```

保存并重启后，面板将通过指定的代理拉取 geo 数据库更新、检查版本并访问 Telegram。

#### 受信任代理 CIDR（*Trusted proxy CIDRs*）

- **键：** `trustedProxyCIDRs`
- **默认值：** `127.0.0.1/32,::1/128`（仅本地主机）。
- **格式：** 以逗号分隔的 IP 地址或 CIDR 子网列表（例如 `10.0.0.0/8, 192.168.1.5`）。每个元素都会作为 IP 或 CIDR 校验——不正确的值在保存时会被拒绝。
- **用途：** 列出允许设置 `X-Forwarded-Host`、`X-Forwarded-Proto` 标头和真实客户端 IP 标头的来源。原文提示：「以逗号分隔的 IP/CIDR，允许其设置 forwarded host、proto 和 client IP 标头。」如果面板工作在反向代理（nginx、Caddy 等）之后，需要配置此项，以便正确识别客户端 IP 和协议。

**示例：面板位于反向代理之后。** 如果 nginx 与面板位于同一主机并将请求代理到面板，则仅信任本地主机（默认值）即可：

```
127.0.0.1/32,::1/128
```

如果代理位于内部网络 `10.0.0.0/8` 中的单独服务器上，请添加其子网，否则面板会忽略它传递的标头，并看到代理的 IP 而非真实客户端的 IP：

```
127.0.0.1/32,::1/128,10.0.0.0/8
```

传递真实 IP 和协议的相应 nginx 块示例：

```nginx
proxy_set_header X-Real-IP        $remote_addr;
proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
```

### 13.5. Telegram 机器人（「Telegram 机器人」选项卡 / *Telegram Bot*）

#### 启用 Telegram 机器人（*Enable Telegram Bot*）

- **键：** `tgBotEnable`
- **类型/默认值：** 布尔型，`false`。
- **用途：** 启用 Telegram 机器人的工作。提示：「通过 Telegram 机器人访问面板功能」。

#### Telegram 令牌（*Telegram Token*）

- **键：** `tgBotToken`
- **默认值：** `""`。
- **用途：** 机器人令牌。提示：「需要从 Telegram 机器人管理器 @botfather 获取令牌」。
- **安全特性：** 令牌属于机密值。在面板读取设置的响应中不会返回它（字段被清空，仅返回「已配置/未配置」标志）。如果保存时将字段留空，则之前保存的令牌将**被保留**（不会被覆盖）。

#### Telegram 机器人语言（*Telegram Bot Language*）

- **键：** `tgLang`
- **默认值：** `en-US`。
- **用途：** 机器人消息的语言（独立于 Web 界面的语言）。可用语言列表与面板语言相同。

#### 机器人管理员 User ID（*Admin Chat ID*）

- **键：** `tgBotChatId`
- **默认值：** `""`。
- **格式：** 一个或多个数字 Telegram User ID，**以逗号分隔**。
- **用途：** 通知接收者和被允许通过机器人管理面板的管理员。提示：「Telegram 机器人管理员的一个或多个 User ID。要获取 User ID，请使用 @userinfobot 或在机器人中使用 '/id' 命令。」

#### 通知频率（*Notification Time*）

- **键：** `tgRunTime`
- **默认值：** `@daily`（每日一次）。
- **格式：** **Crontab** 格式的字符串（支持标准 cron 表达式，以及 `@daily`、`@hourly`、`@every 1h` 之类的缩写）。提示：「以 Crontab 格式指定通知间隔」。控制机器人的周期性报告。

**字段值示例。**

| 值 | 机器人何时发送报告 |
| --- | --- |
| `@daily` | 每日午夜一次（默认） |
| `@hourly` | 每小时 |
| `@every 6h` | 每 6 小时 |
| `0 9 * * *` | 每天 09:00 |
| `30 8 * * 1` | 每周一 08:30 |

时间按「时区」设置（第 13.6 节）中的时区计算。

#### SOCKS 代理（*SOCKS Proxy*）

- **键：** `tgBotProxy`
- **默认值：** `""`。
- **用途：** 专门用于机器人连接 Telegram 的 SOCKS5 代理。提示：「如果连接 Telegram 需要 Socks5 代理，请按照指南配置其参数。」它专门作用于机器人的流量（不同于第 13.4 节的通用「面板网络代理」）。

#### Telegram API Server（*Telegram API Server*）

- **键：** `tgBotAPIServer`
- **默认值：** `""`（使用标准服务器 `api.telegram.org`）。
- **格式：** URL `http(s)://…`；保存时会通过 URL 正确性校验——无效的地址会被拒绝。提示：「使用的 Telegram API 服务器。留空以使用默认服务器。」用于自行部署的 Telegram Bot API server。

#### 机器人通知（「通知」组 / *Notifications*）

| 字段 | 键 | 默认值 | 描述 |
| --- | --- | --- | --- |
| 数据库备份（*Database Backup*） | `tgBotBackup` | `false` | 将数据库备份文件连同报告一起发送到 Telegram。提示：「发送带有数据库备份文件的通知」。 |
| 登录通知（*Login Notification*） | `tgBotLoginNotify` | `true` | 在尝试登录面板时进行通知。提示：「显示有人尝试登录您的面板时的用户名、IP 地址和时间。」 |
| 会话到期通知延迟（*Expiration Date Notification*） | `expireDiff` | `0` | 在客户端有效期到期前多少**天**发送通知。`0` — 禁用。允许 `>= 0`。提示：「在达到阈值前接收会话有效期到期通知（单位：天）」。 |
| 通知的流量阈值（*Traffic Cap Notification*） | `trafficDiff` | `0` | 用于通知的剩余流量阈值。提示：「在达到阈值前接收流量耗尽通知（单位：GB）」。允许 `0–100`。 |
| CPU 负载阈值（*CPU Load Notification*） | `tgCpu` | `80` | 如果 CPU 负载超过阈值（以 **%** 计），通知管理员。允许 `0–100`。提示：「如果 CPU 负载超过此阈值，在 Telegram 中通知管理员（单位：%）」。 |

### 13.6. 日期与时间（「日期与时间」选项卡 / *Date and Time*）

#### 时区（*Time Zone*）

- **键：** `timeLocation`
- **默认值：** `Local`（服务器的系统时区）。
- **格式：** IANA tz 数据库中的时区名称（例如 `Europe/Moscow`、`UTC`、`Asia/Tehran`）。
- **用途：** 面板执行计划任务（机器人报告、流量重置/检查、有效期到期）所依据的时区。提示：「计划任务根据此时区的时间执行」。
- **校验：** 保存时会校验时区——不存在的时区会被拒绝。如果之后数据库中出现不正确的值，面板会在运行时回退到 `Local`，而如果它也不可用，则回退到 `UTC`。

### 13.7. 外部流量与 Xray 行为（「外部流量」选项卡 / *External Traffic*）

| 字段 | 键 | 默认值 | 描述 |
| --- | --- | --- | --- |
| 外部流量通知（*External Traffic Inform*） | `externalTrafficInformEnable` | `false` | 在每次流量更新时通知外部 API。提示：「在每次流量更新时通知外部 API。」 |
| 外部流量通知 URI（*External Traffic Inform URI*） | `externalTrafficInformURI` | `""` | 面板向其发送流量更新的 URL。保存时会通过 URL 正确性校验。提示：「流量更新发送到此 URI」。 |
| 自动停用后重启 Xray（*Restart Xray After Auto Disable*） | `restartXrayOnClientDisable` | `true` | 当客户端因有效期到期或超过流量上限而被自动停用时，重启 Xray。提示：「当客户端因有效期结束或流量上限而被自动停用时，重启 Xray。」**该开关位于「面板」（*General*）选项卡** — 参见第 13.2 节；此处列出是为了完整性。 |

### 13.8. 其他：Xray 配置模板与测试 URL

#### Xray 配置模板（*xrayTemplateConfig*）

- **键：** `xrayTemplateConfig`
- **默认值：** 随构建提供的内置（embedded）JSON 模板。
- **用途：** Xray-core 配置的基础 JSON 模板，面板在其之上构建 inbound/outbound。此值在所有设置的常规输出中**不会返回**，且在单独的 Xray 配置页面而非面板设置字段的通用列表中编辑。默认的标准模板可通过 `GET /panel/setting/getDefaultJsonConfig` 获取。

#### 出站测试 URL（*xrayOutboundTestUrl*）

- **键：** `xrayOutboundTestUrl`
- **默认值：** `https://www.google.com/generate_204`
- **用途：** 在检查出站（outbound）连接可用性时使用的 URL。设置时会作为 HTTP(S) URL 进行净化处理。

### 13.9. 管理员账户与 API 令牌

这些参数位于相邻的选项卡（「账户」 / *Authentication*）上，并在安全章节中详细介绍；此处为键的简要汇总。

- **更改凭据**（「当前登录名」、「当前密码」、「新登录名」、「新密码」字段）通过单独的请求 `POST /panel/setting/updateUser` 保存。需要正确的当前登录名和密码；新的登录名和密码不能为空。消息：「您已成功更改管理员凭据。」/「用户名或密码不正确」。
- **双因素认证（2FA）** — 键 `twoFactorEnable`（默认 `false`）和机密 `twoFactorToken`。令牌是机密：在启用 2FA 的情况下，保存时空字段不会覆盖现有令牌。在**首次**启用 2FA 时，面板会使当前会话失效（提升「登录纪元」）。
- **API 令牌**由单独的端点（`/panel/setting/apiTokens…`）管理：列表、创建（`apiTokens/create`）、删除、启用/禁用。令牌本身**仅在创建时显示一次**，且不以可读形式存储：「立即复制此令牌。出于安全考虑，它不以可读形式存储，且不会再次显示。」

有关 2FA、密码、LDAP 同步以及订阅格式（JSON/Clash、fragmentation、noises、mux）的详情，已归入手册相应的单独章节。

### 13.10. 3.3.0 中的 API 变更（对集成很重要）

在 3.3.0 版本中，服务器 API 的路径结构发生了变化。如果您有通过 HTTP 访问面板的外部集成（脚本、机器人、中央面板、CI 任务），则**需要修正它们**，否则它们将停止工作。

#### ⚠️ BREAKING CHANGE：`/panel/setting/*` 和 `/panel/xray/*` 端点已迁移到 `/panel/api` 下

以前，面板设置管理和 Xray 配置分别位于路径 `/panel/setting/*` 和 `/panel/xray/*` 下。现在两组都注册在通用 API 组 `/panel/api` 内部。旧路径**已完全删除**——对它们的请求将返回 404。

为什么这样做：整个 `/panel/api` 组都经过统一的访问检查，也就是说这些端点现在接受与其余 API 相同的 `Authorization: Bearer <token>` 标头。API 令牌是完整的管理员访问权限，由此整个 API 面变得统一。

**未发生变化的内容：** Web 界面页面（SPA 路由）`/panel/settings` 和 `/panel/xray` 保持原位——只涉及服务器 API 端点。

#### 路径对应表（旧 → 新）

以下所有路径的前缀变化——仅仅是在 `/panel/` 之后添加了 `api/`。

| 之前（≤ 3.2.x） | 之后（3.3.0） | 方法 |
|---|---|---|
| `/panel/setting/all` | `/panel/api/setting/all` | POST |
| `/panel/setting/defaultSettings` | `/panel/api/setting/defaultSettings` | POST |
| `/panel/setting/update` | `/panel/api/setting/update` | POST |
| `/panel/setting/updateUser` | `/panel/api/setting/updateUser` | POST |
| `/panel/setting/restartPanel` | `/panel/api/setting/restartPanel` | POST |
| `/panel/setting/getDefaultJsonConfig` | `/panel/api/setting/getDefaultJsonConfig` | GET |
| `/panel/setting/apiTokens` | `/panel/api/setting/apiTokens` | GET |
| `/panel/setting/apiTokens/create` | `/panel/api/setting/apiTokens/create` | POST |
| `/panel/setting/apiTokens/delete/:id` | `/panel/api/setting/apiTokens/delete/:id` | POST |
| `/panel/setting/apiTokens/setEnabled/:id` | `/panel/api/setting/apiTokens/setEnabled/:id` | POST |
| `/panel/xray/` | `/panel/api/xray/` | POST |
| `/panel/xray/update` | `/panel/api/xray/update` | POST |
| `/panel/xray/getDefaultJsonConfig` | `/panel/api/xray/getDefaultJsonConfig` | GET |
| `/panel/xray/getXrayResult` | `/panel/api/xray/getXrayResult` | GET |
| `/panel/xray/getOutboundsTraffic` | `/panel/api/xray/getOutboundsTraffic` | GET |
| `/panel/xray/resetOutboundsTraffic` | `/panel/api/xray/resetOutboundsTraffic` | POST |
| `/panel/xray/testOutbound` | `/panel/api/xray/testOutbound` | POST |
| `/panel/xray/warp/:action` | `/panel/api/xray/warp/:action` | POST |
| `/panel/xray/nord/:action` | `/panel/api/xray/nord/:action` | POST |
| `/panel/xray/outbound-subs`（及 `/outbound-subs/*`） | `/panel/api/xray/outbound-subs`（及 `/outbound-subs/*`） | GET/POST/DELETE |

子路径名称、请求体和响应格式本身没有改变——改变的**仅是前缀**。

#### 如何修复现有集成

1. 在您的脚本/配置中找到所有出现的 `/panel/setting/` 和 `/panel/xray/`。
2. 替换前缀：在 `/panel/` 之后紧接着添加 `api/`（例如 `/panel/setting/all` → `/panel/api/setting/all`）。
3. 请求体、参数和响应格式无需修改——只更改 URL。
4. 由于设置和 Xray 配置现在位于 `/panel/api` 下，可以（并且应当）使用与 `/panel/api/inbounds/*` 及其他端点相同的 API 令牌 `Authorization: Bearer <token>` 访问它们。不要忘记对整个 `/panel/api` 组启用的 CSRF 中间件。

**示例：通过 API 读取所有设置。** 以前（≤ 3.2.x）：

```bash
curl -sk -X POST "https://panel.example.com:2053/MyPath/panel/setting/all" \
  -H "Authorization: Bearer <token>"
```

现在（3.3.0）——在 `/panel/` 之后添加了 `api/`：

```bash
curl -sk -X POST "https://panel.example.com:2053/MyPath/panel/api/setting/all" \
  -H "Authorization: Bearer <token>"
```

重启面板同理：`POST /panel/api/setting/restartPanel`。旧路径 `/panel/setting/restartPanel` 现在将返回 404。

#### 类型化 API：模式与文档（Swagger / OpenAPI）

在 3.3.0 中，OpenAPI 规范变得完全类型化。以前类型化响应用空对象 `{}` 描述；现在组件和模式（`components.schemas`）直接从数据模型生成。由此：

- Swagger UI 显示真实的数据模型，而非空洞的占位符。
- 外部生成器（`openapi-generator` 等）可以根据规范构建出所需语言的现成客户端。
- 每个类型化响应都附有指向具体模型的 `$ref`，并附带了响应示例。

在哪里查看 API 文档：

- **内置 Swagger 页面。** 在面板菜单中——**「API 文档」**项（SPA 路由 `/panel/api-docs`）。这里交互式地列出了所有端点，附带描述、请求体和响应示例。
- **原始 OpenAPI 3.0 规范**在地址 `/panel/api/openapi.json` 提供。此 URL 可以直接喂给 Postman、Insomnia 或 `openapi-generator`。该规范在构建阶段嵌入到二进制文件中；当面板在非标准 `webBasePath` 下工作时，规范中的 `servers` 字段会自动重写为当前的基础路径，以便「Try it out」按钮和外部生成器命中正确的前缀。

---

## 14. Telegram 机器人

3X-UI 面板内置了一个 Telegram 机器人，通过它可以接收服务器和客户端状态的通知，并直接在即时通讯软件中管理单个客户端。机器人采用 long polling 技术（持续轮询 Telegram）工作，因此不需要外部域名或开放端口——只需具备访问 Telegram 服务器的出站连接即可。

机器人区分两类对话对象：

- **管理员**——其 Telegram User ID 填写在机器人设置中的用户（「机器人管理员的 User ID」字段）。可访问所有功能：服务器统计、备份、客户端管理、重启 Xray。
- **客户端**——任何其他用户，其 Telegram User ID 绑定到某个入站连接的具体客户端（客户端的 `tgId` 字段）。仅可查看自己订阅的相关信息。

**示例：将客户端绑定到 Telegram。** 为了让用户接收其订阅的统计信息，需将其数字形式的 Telegram User ID 写入客户端的 `tgId` 字段。在客户端的 JSON 设置中如下所示：

```json
{
  "email": "ivan",
  "id": "6f1e6b1a-0c3d-4f2a-9b7e-1a2b3c4d5e6f",
  "tgId": "123456789",
  "enable": true,
  "limitIp": 2,
  "totalGB": 53687091200,
  "expiryTime": 0
}
```

此后，User ID 为 `123456789` 的用户即可向机器人发送 `/usage ivan` 并查看自己的统计信息。同样的 ID，管理员也可以通过客户端卡片中的「👤 设置 Telegram 用户」按钮填写——不必手动编辑 JSON。

### 14.1. 启用和配置机器人

机器人的所有参数都在面板的 **设置 → Telegram 机器人** 部分设置。修改设置后需要保存并重启面板——机器人会在 Web 服务器启动时初始化。

| 字段 (UI) | 设置键 | 默认值 | 说明 |
|---|---|---|---|
| 启用 Telegram 机器人 | `tgBotEnable` | `false` | 主开关。提示：「通过 Telegram 机器人访问面板功能」。在关闭状态下，机器人不会启动，通知任务也不会被调度。 |
| Telegram 令牌 | `tgBotToken` | （空） | 机器人令牌。提示：「需要从 Telegram 机器人管理器 @botfather 获取令牌」。令牌为空时机器人不会启动。 |
| SOCKS 代理 | `tgBotProxy` | （空） | 用于连接 Telegram 的代理。提示（RU）：「如果连接 Telegram 需要 Socks5 代理，请按照指南配置其参数」。 |
| Telegram API Server | `tgBotAPIServer` | （空） | 备用的 Telegram API 服务器。提示：「使用的 Telegram API 服务器。留空则使用默认服务器」。 |
| 机器人管理员的 User ID | `tgBotChatId` | （空） | 一个或多个管理员的 Telegram User ID，以逗号分隔。提示：「要获取 User ID，请使用 @userinfobot 或在机器人中使用 `/id` 命令」。 |
| 机器人向管理员发送通知的频率 | `tgRunTime` | `@daily` | crontab 格式的周期性报告计划。提示：「以 Crontab 格式指定通知间隔」。 |
| 数据库备份 | `tgBotBackup` | `false` | 提示：「随通知一起发送数据库备份文件」。将备份附加到周期性报告中。 |
| 登录通知 | `tgBotLoginNotify` | `true` | 提示：「当有人尝试登录您的面板时，显示用户名、IP 地址和时间」。 |
| 触发通知的 CPU 负载阈值 | `tgCpu` | `80` | CPU 负载阈值（百分比，校验范围 0–100）。提示：「当 CPU 负载超过此阈值时，在 Telegram 中通知管理员（数值：%）」。值为 0 时禁用 CPU 检查。 |
| Telegram 机器人语言 | — | — | 机器人生成所有消息所使用的语言。 |

#### 通过 @BotFather 获取令牌

1. 在 Telegram 中打开与 **@BotFather** 的对话。
2. 发送 `/newbot` 命令并按照说明操作（机器人名称和以 `bot` 结尾的唯一 `username`）。
3. BotFather 会发放形如 `123456789:AA...` 的令牌。将其复制到 **Telegram 令牌** 字段中。

#### 获取管理员 User ID

User ID 是账户的数字标识符（不是 username）。可以通过两种方式获取：

- 给 **@userinfobot** 发消息。
- 启动已配置好的机器人并向其发送 **`/id`** 命令——它会返回你的 ID。

将获取到的数字填入 **机器人管理员的 User ID** 字段。要指定多个管理员，请以逗号分隔列出他们的 ID（例如 `11111111,22222222`）。每个 ID 都会被作为整数校验；不正确的值会导致机器人启动失败。

**示例：「机器人管理员的 User ID」字段的值。** 单个管理员——只需一个数字：

```
123456789
```

两个管理员以逗号分隔（可以不加空格）：

```
123456789,987654321
```

每个值都必须是整数。形如 `@username` 或 `123 456`（数字中间带空格）的写法不可用——机器人将无法启动。

#### 代理

支持 `socks5://`、`http://` 和 `https://` 方案。如果代理字段留空，机器人会尝试使用面板的通用代理（如果已设置且其方案受支持）。方案不受支持或语法不正确的 URL 会被忽略——机器人将直接连接。当从服务器直接访问 Telegram API 被封锁时，代理会很有用。

#### 电子邮件通知 (SMTP)

除 Telegram 外，相同的事件也可以通过邮件接收。该通道在 **设置 → Email** 部分的 **SMTP Settings** 选项卡中配置：

| 字段 (UI) | 设置键 | 默认值 | 说明 |
|---|---|---|---|
| Enable Email Notifications | `smtpEnable` | `false` | 通过 SMTP 发送邮件通知的主开关。 |
| SMTP Host | `smtpHost` | （空） | SMTP 服务器主机（例如 `smtp.gmail.com`）。 |
| SMTP Port | `smtpPort` | `587` | SMTP 服务器端口。 |
| SMTP Username | `smtpUsername` | （空） | 用于 SMTP 认证的用户名。同时用作发件人地址 (From)。 |
| SMTP Password | `smtpPassword` | （空） | 用于 SMTP 认证的密码。隐藏存储；如果密码已设置，字段会显示「已配置」标记，可以留空以保留当前密码。 |
| Recipients | `smtpTo` | （空） | 以逗号分隔的收件人列表（例如 `admin@example.com, ops@example.com`）。 |
| Encryption | `smtpEncryptionType` | `starttls` | 连接加密类型：`none`（不加密）、`starttls`（STARTTLS）或 `tls`（隐式 TLS）。 |

**Send Test Email** 按钮会发送一封测试邮件并按阶段显示结果：**Connection**（连接）、**Authentication**（认证）和 **Send**（发送）。如果出现问题，诊断会指出错误发生在哪个阶段（例如「Authentication failed — check username and password」或「Server requires STARTTLS — change encryption type」），从而简化参数的调整。

在第二个选项卡（**Notifications**）中可以选择将通过邮件发送通知的事件——使用与 Telegram 相同的分组卡片（参见 14.5 节中的「事件总线与通知选择」）。

#### Telegram API 服务器

默认情况下，机器人访问 Telegram 的官方 API。在 **Telegram API Server** 字段中可以指定自己的 Bot API 服务器地址（`telegram-bot-api`）。该 URL 会进行安全性检查；被封锁或不正确的地址会被舍弃，转而使用默认服务器。

### 14.2. 主菜单与按钮

菜单通过 **`/start`** 命令调出。按钮是附加在消息上的 inline 键盘；按钮集取决于你是管理员还是客户端。

#### 管理员菜单

| 按钮 | 操作 |
|---|---|
| 📊 排序后的流量使用报告 | 列出所有客户端，按流量排序，并显示每个客户端的消耗量；没有数据的「多余」email 会标记为「❗ 无结果」。 |
| 💻 服务器状态 | 服务器概览（参见 14.5 节）。「🔄 刷新」按钮会重新绘制数据。 |
| 重置所有流量 | 重置**所有**客户端的流量计数器。会请求确认（「您确定吗？🤔」），然后对每个客户端输出「✅ 成功」或「❌ 失败」，最后显示「🔚 已为所有客户端完成流量重置」。 |
| 📂 数据库备份 | 发送数据库文件和 `config.json`（参见 14.6 节）。 |
| 📄 封禁日志 | 发送因 IP 限制而被封禁地址的日志文件。 |
| 🔌 入站连接 | 所有 inbound 的概览：Remark、端口、流量、客户端数量、到期日期。 |
| ⚠️ 即将到期 | 流量或期限即将耗尽的 inbound 和客户端列表（参见 14.5 节）。 |
| 🖱️ 命令 | 显示管理员命令的帮助。 |
| 🟢 在线 | 当前在线客户端的数量和列表；点击 email 会打开客户端卡片。「🔄 刷新」按钮。 |
| 👥 所有客户端 | 打开 inbound 选择，然后显示其客户端列表——用于查看/管理。 |
| ➕ 新建客户端 | 启动客户端添加向导（选择 inbound → 草稿 → 确认）。 |
| 订阅设置 / 单独链接 / 二维码 | 选择 inbound 和客户端，以获取订阅链接、单独链接或二维码。 |

#### 客户端菜单

客户端可使用的按钮集有限：

| 按钮 | 操作 |
|---|---|
| 客户端统计 | 显示绑定到该客户端 Telegram User ID 的所有订阅的数据。 |
| 🖱️ 命令 | 显示客户端命令的帮助。 |
| 订阅设置 | 选择自己的客户端 → 订阅链接。 |
| 单独链接 | 选择自己的客户端 → 单独链接。 |
| 二维码 | 选择自己的客户端 → 二维码。 |

如果用户没有任何客户端绑定了他的 Telegram User ID，机器人会回复：「❌ 未找到您的配置！💭 请让管理员在配置中使用您的 Telegram User ID。🆔 您的 User ID：…」。需要将此 ID 转交给管理员，以便其填入客户端字段中。

### 14.3. 机器人命令

机器人注册了四条命令，可在 Telegram 的「/」菜单中看到：

| 命令 | 说明（来自菜单） | 访问权限 | 功能 |
|---|---|---|---|
| `/start` | 显示主菜单 | 所有人 | 欢迎语；对管理员额外显示「🤖 欢迎使用 <Host> 管理机器人！」和主菜单。 |
| `/help` | 机器人帮助 | 所有人 | 显示通用欢迎语和选择菜单项的提示。 |
| `/status` | 检查机器人状态 | 所有人 | 回复「✅ 机器人运行正常」。 |
| `/id` | 显示您的 Telegram ID | 所有人 | 返回「🆔 您的 User ID：<code>…</code>」。便于获取自己的 User ID。 |

除已注册的命令外，还会处理另外三条带参数的命令（它们不在「/」菜单中显示，但可正常工作）：

- **`/usage [Email]`**——按 email 查找客户端。
  - 对**管理员**显示完整的客户端卡片（带管理按钮）。
  - 对**客户端**仅显示其自己名下指定 email 的订阅（通过 Telegram User ID 绑定）。不带参数时，机器人会要求指定 email：「❗ 请指定要查找的 email」。
- **`/inbound [连接名称]`**——仅限管理员。按 Remark 查找 inbound 并输出其参数及所有客户端的统计信息。不带参数（或对客户端）时——「❗ 未知命令」。
- **`/restart`**——仅限管理员。重启 Xray Core。可能的回复：「✅ Xray 核心重启成功」、「❗ Xray Core 未运行」（如果核心未在运行）、「❗ 重启 Xray-core 时出错。<错误>」。`/restart` 后带任何参数都会导致出现未知命令消息并附带 `/restart` 提示。

在群聊中，形如 `/命令@botusername` 的命令仅在 username 与当前机器人名称匹配时才会被处理。

管理员帮助（「命令」按钮）：

```
🔃 Для перезапуска Xray Core: /restart
🔎 Для поиска клиента по email: /usage [Email]
📊 Для поиска входящих подключений (со статистикой клиентов): /inbound [имя подключения]
🆔 Ваш Telegram User ID: /id
```

客户端帮助：

```
💲 Для просмотра информации о вашей подписке: /usage [Email]
🆔 Ваш Telegram User ID: /id
```

### 14.4. 客户端管理（仅限管理员）

打开客户端卡片后（通过「所有客户端」、「在线」、「即将到期」或 `/usage`），管理员会看到客户端的相关信息（email、绑定的 inbound、「已激活」状态、连接状态、到期日期、流量消耗）以及管理用的 inline 按钮：

| 按钮 | 用途 |
|---|---|
| 🔄 刷新 | 重新读取客户端卡片。 |
| 📈 重置流量 | 将客户端的流量计数器清零。需要确认「✅ 确认重置流量？」。 |
| 🚧 流量限额 | 设置流量限额。预设值：♾ 无限（0）、1/5/10/20/30/40/50/60/80/100/150/200 GB 或「🔢 自定义」——在内置数字键盘上输入数字（按钮 0–9、「🔄」——重置为 0、「⬅️」——删除最后一位数字、「✅ 确认：N」）。数值以 GB 为单位设置。 |
| 📅 修改到期日期 | 预设选项：♾ 无限、「🔢 自定义」、增加 7/10/14/20 天、1/3/6/12 个月。正数会延长期限（在当前到期日期上加天数，如果期限已过则在「现在」基础上加）；0 会取消期限限制。 |
| 🔢 IP 日志 | 显示客户端记录的 IP 地址（如有时间戳则一并显示）。在日志中可使用「🔄 刷新」和「❌ 清除 IP」（带确认「✅ 确认清除 IP？」）。 |
| 🔢 IP 限额 | 同时连接的 IP 限制。选项：♾ 无限（0）、1–10 或「🔢 自定义」（数字键盘）。 |
| 👤 设置 Telegram 用户 | 显示客户端当前绑定的 Telegram User ID；可清除绑定（「❌ 删除 Telegram 用户」，带确认）。绑定新用户通过 Telegram 系统的联系人选择完成。 |
| 🔘 启用/禁用 | 启用或禁用客户端。需要确认「✅ 确认启用/禁用用户？」。 |

所有修改配置的操作（流量/IP 限额、到期日期、Telegram 用户的绑定/解绑、启用/禁用），如有必要会将 Xray 标记为需重启，以使更改生效。操作成功后，机器人会输出形如「✅ <email>：…」的确认信息并重新显示卡片。

向导中任何数字输入都被限制为小于 999999 的值。

### 14.5. 通知与报告

通知会发送给所有管理员（`tgBotChatId` 中的所有 User ID）。

#### 事件总线与通知选择

通知基于统一的事件总线构建，投递通道有两个——**Telegram** 和 **电子邮件 (SMTP)**。可为每个通道分别选择对哪些事件发出提醒。在 **设置 → Telegram** 中，这是在 **Notifications** 选项卡中完成；在 **设置 → Email** 中，则在同名选项卡中完成。

事件以卡片分组；每个分组都有一个主开关，带有已启用事件的计数器（n/总数）以及当仅选中部分事件时的中间状态。可用的分组有：

- **Outbound**——「Down」(`outbound.down`) 和「Up」(`outbound.up`)：outbound 的中断和恢复。
- **Xray Core**——「Crash」(`xray.crash`)：Xray 核心的异常终止。
- **Nodes**——「Down」(`node.down`) 和「Up」(`node.up`)：节点变为不可用或已恢复。
- **System**——「CPU high (%)」(`cpu.high`) 和「Memory high (%)」(`memory.high`)：处理器和内存的高负载。这两个事件旁边都有一个以百分比表示阈值的内联字段。
- **Security**——「Login attempt」(`login.attempt`)：尝试登录面板。

已启用事件集分别存储：Telegram 存于 `tgEnabledEvents`，Email 存于 `smtpEnabledEvents`。默认情况下两个通道都启用了「Login attempt」和「CPU high」（值为 `login.attempt,cpu.high`）。

#### 面板登录通知

由 **登录通知** 复选框控制（`tgBotLoginNotify`，默认启用）。每次尝试登录 Web 面板时，管理员都会收到消息：

- 成功时：「✅ 成功登录面板。」+ 主机、用户名、IP、时间。
- 失败时：「❗️ 面板登录失败。」+ 主机、**原因**（例如第二因素不正确时显示「2FA 错误」）、用户名、IP、时间。

#### CPU 和内存负载超限

面板每分钟检查一次处理器和内存的负载。如果阈值 **`tgCpu`** > 0 且 CPU 一分钟内的平均负载超过该阈值，管理员就会收到：「🔴 处理器负载为 N%，超过阈值 M%」。内存负载同样会与阈值 **`tgMemory`**（默认 80%）对比检查——对应「Memory high (%)」事件。

两个阈值都通过 Notifications 选项卡 **System** 分组中「CPU high (%)」和「Memory high (%)」事件旁的内联字段设置（参见下文「事件总线与通知选择」）。Email 通道使用单独的键 `smtpCpu` 和 `smtpMemory`。阈值为 0 时，相应的检查被禁用。

#### 周期性报告（按计划）

根据 **通知频率** 字段中的 cron 表达式调度（`tgRunTime`，默认 `@daily`）。如果值为空或不正确，则使用 `@daily`。报告包含：

#### 计划构造器

**机器人向管理员发送通知的频率** 字段不是手动输入字符串，而是通过计划构造器设置。首先在下拉列表中选择模式：

- **`@every` — 按间隔重复**——会出现数字字段和单位选择（**秒** / **分钟** / **小时**）；结果汇集成形如 `@every 6h` 的表达式。
- **`@hourly` — 每小时**、**`@daily` — 每天 00:00**、**`@weekly` — 每周**、**`@monthly` — 每月**——现成的预设，保存为对应的宏（`@hourly`、`@daily`、`@weekly`、`@monthly`）。
- **自定义 (crontab)**——用于填写自己的 crontab 表达式的字段。面板调度器启用了秒级，因此自定义表达式由 **6 个字段** 组成：秒、分、时、日、月、星期（例如 `0 30 8 * * *`——每天 08:30:00）。切换到此模式时，字段会填入当前选择的 crontab 等价值，以便有所参照。

**示例：「通知频率」字段（`tgRunTime`）的值。** 既支持现成的简写，也支持完整的 crontab 格式：

| 值 | 触发时机 |
|---|---|
| `@daily` | 每天午夜一次（默认值） |
| `@hourly` | 每小时 |
| `@every 6h` | 每 6 小时 |
| `0 9 * * *` | 每天 09:00 |
| `0 9 * * 1` | 每周一 09:00 |
| `0 */12 * * *` | 每 12 小时（在 00:00 和 12:00） |

crontab 中字段的顺序：分、时、日、月、星期。

1. 「🕰 已计划的报告：<计划>」一行以及当前日期/时间。
2. **服务器状态**（见下文）。
3. 按 inbound 和客户端列出的「即将到期」区块。
4. 向绑定了 Telegram User ID 的客户端发送个人通知——每个非管理员客户端都会收到其流量/期限即将耗尽的订阅列表（包括已禁用的）。
5. 如果启用了 **数据库备份**（`tgBotBackup`）——向管理员发送数据库备份。

**服务器状态** 包含：主机、3X-UI 和 Xray 版本、IPv4/IPv6、运行时间（天数）、平均负载 (Load1/2/3)、RAM（当前/总计）、在线客户端数量、TCP/UDP 连接计数器、网络总流量 (↑/↓) 以及 Xray 状态。

**「即将到期」** 显示：

- 按 inbound：已禁用的数量和「即将耗尽」的数量，然后列举这些 inbound（Remark、端口、流量、到期日期）；
- 按客户端：同上，外加客户端卡片和带其 email 的按钮（点击会打开客户端卡片）。

「即将耗尽」的阈值取自面板的通用设置：流量余量（GB）和期限余量（天）。当某 inbound/客户端距流量限额剩余小于阈值 **或** 距到期日期剩余小于阈值时，即被视为「即将耗尽」。

### 14.6. 备份与日志

- **数据库备份**（「📂 数据库备份」按钮或周期性报告中的复选框）：机器人会发送备份时间、数据库文件（`x-ui.db`，PostgreSQL 则为 `x-ui.dump`）以及 Xray 配置文件 `config.json`。
- **封禁日志**（「📄 封禁日志」按钮）：发送因超出 IP 限额而被封禁的 IP 地址日志的当前和上一个文件。空文件不会被发送。

### 14.7. 工作特性

- **长消息** 会被拆分成多部分（阈值约 2000 字符），inline 键盘附加在最后一部分上。
- **并发**：命令和按钮点击会被并发处理（最多 10 个同时处理的处理器池）。
- **发送可靠性**：连接出错时，消息会以指数退避方式重新发送（1秒/2秒/4秒，最多 3 次尝试）。
- **缓存**：「服务器状态」数据会被缓存，以免频繁点击「刷新」给系统带来负担。
- **机器人重启**：在保存设置并重启面板时，上一轮轮询循环会正确停止，并启动新的循环——同一时间只有一个接收更新的实例在运行。

---

## 15. 地理数据库（geoip / geosite 及自定义）

地理数据库是一些二进制 `.dat` 文件，Xray-core 用它们按国家归属（IP 段）或域名类别对流量进行路由和过滤。面板既能加载和更新标准的地理文件集合，也能加载按 URL 指定的任意用户自定义来源。所有文件都存放在 Xray 二进制文件旁边的 `bin` 目录中（默认路径为 `bin`，可通过环境变量 `XUI_BIN_FOLDER` 覆盖）。

### 15.1. 什么是 geoip.dat 和 geosite.dat

- **geoip.dat** — “IP 地址 → 国家/地区代码”的对应数据库。在路由规则中以 `geoip:<代码>` 形式使用，例如 `geoip:ru`、`geoip:cn`，以及特殊标记 `geoip:private`（私有/本地网络）。本质上它回答的是“这个 IP 位于哪个国家”这一问题。
- **geosite.dat** — “域名 → 类别/列表”的对应数据库。以 `geosite:<类别>` 形式使用，例如 `geosite:category-ads-all`（广告域名）、`geosite:google`、`geosite:ru`。本质上它是按组分类的域名列表。

这些文件用于构建诸如“所有发往俄罗斯 IP/域名的流量走直连，其余走 outbound”之类的规则。规则本身在 Xray 的路由部分定义；地理数据库只是为它们提供数据。如果没有最新的地理文件，引用 `geoip:`/`geosite:` 的规则将不会生效，或者会依据过时的列表运行。

**示例：“俄罗斯域名和 IP 走直连”规则。** 在路由部分中，这样的规则会把所有发往俄罗斯资源的流量导向带 `direct` 标签的 outbound：

```json
{
  "type": "field",
  "domain": ["geosite:category-ru"],
  "ip": ["geoip:ru"],
  "outboundTag": "direct"
}
```

### 15.2. 标准地理文件及其更新

面板内置了一个固定的“白名单”（allowlist），包含六个标准文件，且其下载来源已硬编码。更新通过 `POST /panel/api/server/updateGeofile/:fileName` 执行（或不带文件名——用于一次性更新全部）。

**示例：通过 API 更新单个文件和一次性更新全部。** 仅更新 `geoip_RU.dat`：

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/updateGeofile/geoip_RU.dat' \
  -H 'Cookie: 3x-ui=<session-cookie>'
```

用一个请求更新全部六个标准文件（不指定文件名）：

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/updateGeofile' \
  -H 'Cookie: 3x-ui=<session-cookie>'
```

成功响应：

```json
{ "success": true, "msg": "Geofile updated successfully", "obj": null }
```

| 文件名 | 来源（发布仓库） |
|---|---|
| `geoip.dat` | `github.com/Loyalsoldier/v2ray-rules-dat` (geoip.dat) |
| `geosite.dat` | `github.com/Loyalsoldier/v2ray-rules-dat` (geosite.dat) |
| `geoip_IR.dat` | `github.com/chocolate4u/Iran-v2ray-rules` (geoip.dat) |
| `geosite_IR.dat` | `github.com/chocolate4u/Iran-v2ray-rules` (geosite.dat) |
| `geoip_RU.dat` | `github.com/runetfreedom/russia-v2ray-rules-dat` (geoip.dat) |
| `geosite_RU.dat` | `github.com/runetfreedom/russia-v2ray-rules-dat` (geosite.dat) |

更新标准文件的特点：

- **更新单个文件的按钮。** 下载前会弹出确认：“您确定要更新地理文件吗？”，并说明“这将更新文件 #filename#。”（英文 *Do you really want to update the geofile? This will update the #filename# file.*）。成功后会弹出通知“地理文件已成功更新”（英文 *Geofile updated successfully*）。
- **“Обновить все”按钮**（英文 *Update all*）会下载全部六个文件。确认提示：“这将更新所有地理文件。”（英文 *This will update all geofiles.*）。
- **条件下载。** 如果本地已存在该文件，请求中会带上 `If-Modified-Since` 头，其值为文件的修改时间。服务器返回 `304 Not Modified` 表示文件未变更——不会重复下载，只更新文件的时间戳。
- **文件名安全性。** 仅接受白名单中的名称；名称会被检查是否不含 `..`、路径分隔符 `/` 和 `\`、绝对路径，并且必须匹配模式 `^[a-zA-Z0-9._-]+\.dat$`。任何不在列表中的名称都会以错误“Invalid geofile name”被拒绝。
- **重启 Xray。** 下载地理文件后，Xray-core 会重启，以便重新读取更新后的数据库。如果重启失败，错误消息中会附加相应的说明行。

#### 从命令行更新地理数据库（x-ui）

地理数据库也可以不通过面板更新——使用 `x-ui` 的交互式菜单（更新地理文件的菜单项），或非交互式命令 `x-ui update-all-geofiles`。对集合中的每个文件（geoip/geosite，包括 IR 和 RU 集合）都会输出单独的状态：“已更新”、“已是最新”或“下载错误”。下载失败时不会打印虚假的成功消息。只有当至少有一个文件确实被更新时，才会重启 Xray（也即断开活动连接）；如果没有任何文件发生变更（全部返回 `304 Not Modified`），面板和 Xray 都不会重启。

### 15.3. 通过 Xray 自动更新地理数据（Geodata Auto-Update）

按任意 URL 添加额外的 `.dat` 来源不是用面板自身的功能，而是通过 Xray-core 原生的 `geodata` 段实现。对应部分被放在 Xray 更新的模态窗口中（仪表盘 → Xray 更新，`xrayUpdates`）——即“Geodata 自动更新”选项卡（英文 *Geodata Auto-Update*）。面板在这里只是编辑 Xray 配置模板中的 `geodata` 键；文件的下载、校验和热重载由 Xray 内核本身负责。

该部分顶部显示一条提示：“Xray 会按计划下载这些文件并在不重启的情况下热重载它们。URL 必须是 HTTPS。在 Xray 能更新某个文件之前，该文件必须已存在于 bin 文件夹中。”（英文 *Xray downloads these files on schedule and hot-reloads them without a restart. URLs must be HTTPS. Each file must already exist in the bin folder once before Xray can update it.*）。

#### 该部分的字段

- **计划（cron）**（英文 *Schedule (cron)*）— 由 5 个字段组成的 cron 字符串；默认值为 `0 4 * * *`（每天 04:00）。保存时会校验该字符串恰好包含 5 个字段，否则会输出错误“Cron 必须包含 5 个字段，例如 0 4 * * *”。
- **通过 outbound 下载（可选）**（英文 *Download through outbound (optional)*）— 一个下拉列表，包含可用 outbound 的标签（外加订阅 outbound），Xray 将通过它下载文件；协议为 `blackhole` 的 outbound 不会出现在列表中。该字段可留空——此时使用直接连接。这个选择与面板自身请求所用的 outbound（见 §11）无关：geodata 自动更新有自己独立的下载用 outbound。
- **文件列表** — 每一行指定一对“URL + 文件名”（英文 *File name*）。URL 必须以 `https://` 开头（否则“每个文件都需要 HTTPS URL。”）。文件名应填写简单形式，不含路径和分隔符——只能是字符 `^[A-Za-z0-9._-]+$`（否则“文件名必须是简单形式，例如 geosite_custom.dat（不含路径）。”）。输入 URL 时，面板会尝试根据路径的最后一段自动填入文件名。“Добавить файл”按钮（英文 *Add file*）会添加一行，垃圾桶按钮会删除该行。

如果列表为空，会显示提示：“尚未配置文件。在路由规则中将文件引用为 ext:geosite_custom.dat:category。”（英文 *No files configured. Reference files in routing rules as ext:geosite_custom.dat:category.*）。

#### 保存

“保存并重启 Xray”按钮（英文 *Save & Restart Xray*）会弹出确认“保存 geodata 设置？”，并说明“Xray 配置模板将被更新，且 Xray 将被重启。”（英文 *Save geodata settings? This updates the Xray config template and restarts Xray.*）。保存后，`geodata` 键会写入配置模板（`POST /panel/api/xray/update`），并重启 Xray（`POST /panel/api/server/restartXrayService`）。如果文件列表为空，会从模板中删除 `geodata` 键。

重要特点：

- **文件必须已存在于 `bin` 中。** Xray 只更新启动时已存在于 `bin` 文件夹中的那些 `.dat` 文件。因此，新的自定义文件要先手动放入 `bin`（或至少在那里以所需名称创建一个空的/过时的版本），之后 Xray 才会按计划将其保持为最新状态。
- **热重载。** 在计划下载之后，Xray 会重新读取更新后的数据库，而无需完全重启进程。
- **兼容性。** 之前已下载的地理文件（无论是标准还是自定义）在路由规则中以 `ext:` 语法继续工作，无需更改。

如果列表为空，会显示提示：“暂无自定义 geo 来源——点击“添加”以创建”（英文 *No custom geo sources yet — click Add to create one*）。

#### 表格列与来源字段

| 字段（UI） | JSON | 默认值 | 描述 |
|---|---|---|---|
| 类型（*Type*） | `type` | —（必填） | 资源类型：仅 `geosite` 或 `geoip`。决定最终文件的名称。 |
| 别名（*Alias*） | `alias` | —（必填） | 来源的简短标识符。由它和类型构成文件名。 |
| URL（*URL*） | `url` | —（必填） | `.dat` 文件的直接链接（http/https）。 |
| 已启用（*Enabled*） | — | — | 来源在列表中是否处于活动状态的标志。 |
| 已更新（*Last updated*） | `lastUpdatedAt` | `0` | 上次成功更新的时间（Unix 时间；`0` 表示尚未更新过）。 |
| 路由（ext:…）（*Routing (ext:…)*） | — | — | 用于路由规则的现成字符串：`ext:<文件.dat>:tag`。 |
| 操作（*Actions*） | — | — | “修改”、“删除”、“立即更新”按钮。 |

此外，数据库中还存储一些辅助字段：`localPath`（文件在 `bin` 目录中的实际路径）、`lastModified`（服务器返回的 `Last-Modified` 头的值，用于条件下载）、`createdAt` 和 `updatedAt`。

#### 文件命名

最终文件的名称由类型和别名自动生成：

- 类型 `geoip` → `geoip_<alias>.dat`；
- 类型 `geosite` → `geosite_<alias>.dat`。

例如，类型为 `geosite`、别名为 `myads` 的来源会创建文件 `geosite_myads.dat`。

**示例：通过 API 添加来源。** 将你自己的广告域名列表添加为别名为 `myads` 的 `geosite` 资源：

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/customGeo/add' \
  -H 'Cookie: 3x-ui=<session-cookie>' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "geosite",
    "alias": "myads",
    "url": "https://example.com/lists/myads.dat"
  }'
```

面板会把文件下载到 `bin` 目录并命名为 `geosite_myads.dat`，保存记录并重启 Xray。

#### 按钮和操作

- **添加**（英文 *Add*）— 打开“添加来源”表单（英文 *Add custom geo*）。保存按钮为“保存”（英文 *Save*）。API：`POST /add`。
- **修改**（英文 *Edit*）— “修改来源”表单（英文 *Edit custom geo*）。API：`POST /update/:id`。更改类型或别名时，旧文件会被删除，新文件会被重新下载。
- **删除**（英文 *Delete*）— 确认提示“删除此自定义 geo 来源？”（英文 *Delete this custom geo source?*）。删除数据库中的记录以及 `.dat` 文件本身。API：`POST /delete/:id`。成功时：“自定义 geo 文件「<名称>」已删除”。
- **立即更新**（英文 *Update now*）— 重新下载特定来源并更新时间戳。API：`POST /download/:id`。成功时：“地理文件「<名称>」已更新”。
- **更新全部** — 一次性更新所有自定义来源。API：`POST /update-all`。全部成功时：“所有自定义 geo 来源已更新”（英文 *All custom geo sources updated*）。如果至少有一个来源未更新成功，则该操作被视为部分失败，提示“一个或多个自定义 geo 来源更新失败”（英文 *One or more custom geo sources failed to update*），且响应中会列出成功和失败的来源。

在执行上述任一操作（添加、修改、删除、更新、在有成功项时的更新全部）之后，Xray-core 都会重启。

#### 分步：添加来源

1. 点击“添加”。
2. 在“类型”字段中选择 `geosite` 或 `geoip`。
3. 在“别名”字段中输入标识符（仅限小写拉丁字母、数字、`-` 和 `_`；占位提示：`a-z 0-9 _ -`）。
4. 在“URL”字段中填写 `.dat` 文件的直接链接（必须以 `http://` 或 `https://` 开头）。
5. 点击“保存”。面板会立即把文件下载到 `bin` 目录，保存记录并重启 Xray。

### 15.4. 校验和限制

在创建和修改来源时会执行严格的检查。错误消息：

| 条件 | 消息（RU） | 消息（EN） |
|---|---|---|
| 类型不是 `geosite`/`geoip` | Тип должен быть geosite или geoip | *Type must be geosite or geoip* |
| 别名为空 | Укажите псевдоним | *Alias is required* |
| 别名包含不允许的字符（不匹配 `^[a-z0-9_-]+$`） | Псевдоним содержит недопустимые символы | *Alias must match allowed characters* |
| 别名被保留 | Этот псевдоним зарезервирован | *This alias is reserved* |
| URL 为空 | Укажите URL | *URL is required* |
| URL 无法解析 | Некорректный URL | *URL is invalid* |
| 协议不是 http/https | URL должен использовать http или https | *URL must use http or https* |
| 主机为空/无效，或被 SSRF 防护阻止 | Некорректный хост URL | *URL host is invalid* |
| “类型 + 别名”重复 | Такой псевдоним уже используется для этого типа | *This alias is already used for this type* |
| 来源未找到 | Источник не найден | *Custom geo source not found* |
| 下载错误 | Ошибка загрузки | *Download failed* |

表单中的提示（客户端校验）：“别名：仅 a-z、数字、- 和 _”（*Alias may only contain lowercase letters, digits, - and _*）以及“URL 必须以 http:// 或 https:// 开头”（*URL must start with http:// or https://*）。

额外的技术限制：

- **保留别名。** 不能使用与标准文件冲突的别名。被保留的有（比较时不区分大小写，连字符等同于下划线）：`geoip`、`geosite`、`geoip_ir`、`geosite_ir`、`geoip_ru`、`geosite_ru`。例如，`geosite-ru` 会被当作 `geosite_ru` 而被拒绝。
- **SSRF 防护。** URL 的主机会被解析为 IP，如果它指向私有/内部地址，下载会被阻止（用户会看到“Некорректный хост URL”）。这可以防止利用面板访问内部服务。
- **路径穿越防护。** 文件的最终路径必须位于 `bin` 目录内部（含符号链接解析）；尝试越出其范围会被拒绝。
- **文件最小大小。** 下载的文件只有不小于 64 字节才被视为有效；过小的文件会以下载错误被拒绝。
- **代理与条件下载。** 如果面板设置中指定了代理，下载会通过它进行；其余情况下使用具备 SSRF 安全性传输的直接连接。与标准文件一样，会应用 `If-Modified-Since`/`304 Not Modified`（未变更的文件不会重复下载）。下载超时为 10 分钟，URL 可用性探测（HEAD，必要时为部分 GET）为 12 秒。

### 15.5. 面板启动时的自动检查

面板启动时会遍历所有自定义来源，并为每个来源检查本地文件的存在性和完整性（文件缺失、是目录或小于 64 字节）。如果文件缺失或损坏，会对来源进行探测并尝试重新下载。这保证了在重新安装或丢失 `bin` 目录后，自定义地理文件会被自动恢复。

### 15.6. 在路由规则中使用地理数据库

在 Xray 的路由规则中，地理数据库通过前缀在 `domain`/`ip` 之类的字段中使用：

- **geoip:** 用于 IP 数据库——`geoip:<代码>`。示例：`geoip:ru`、`geoip:cn`、`geoip:private`。取自 `geoip.dat`（如果规则指向具体文件，则取自 `geoip_RU.dat` 等）。
- **geosite:** 用于域名数据库——`geosite:<类别>`。示例：`geosite:category-ads-all`、`geosite:google`、`geosite:ru`。取自 `geosite.dat`。

**示例：通过 geosite 屏蔽广告。** 把所有广告域名发往“黑洞”的规则（假设有一个带 `blocked` 标签、协议为 `blackhole` 的 outbound）：

```json
{
  "type": "field",
  "domain": ["geosite:category-ads-all"],
  "outboundTag": "blocked"
}
```

对于**用户自定义**文件，使用外部文件语法 `ext:`。UI 中的提示：“在路由规则中将该值用作 ext:文件.dat:tag（替换 tag）。”（英文 *In routing rules use the value column as ext:file.dat:tag (replace tag).*）。格式：

```
ext:<文件名.dat>:<标签>
```

其中 `<文件名.dat>` 为 `geoip_<alias>.dat` 或 `geosite_<alias>.dat`，而 `<标签>` 为文件内部的具体列表/类别。面板在“路由（ext:…）”列中提示一个现成模板，形如 `ext:geosite_myads.dat:tag`——只需把 `tag` 替换为所需的标签。这样的文件名在“Geodata 自动更新”部分（见 §15.3）的“文件名”字段中指定——例如 `geosite_custom.dat`；在规则中以 `ext:geosite_custom.dat:category` 引用它。

**示例：基于自定义文件的规则。** 如果添加了类型为 `geosite`、别名为 `myads` 的来源，且 `.dat` 文件内部的列表标记为 `ads` 标签，那么路由规则如下：

```json
{
  "type": "field",
  "domain": ["ext:geosite_myads.dat:ads"],
  "outboundTag": "blocked"
}
```

对于 IP 来源（类型 `geoip`、别名 `mycorp`、标签 `office`），字段为 `"ip": ["ext:geoip_mycorp.dat:office"]`。

---

## 16. 运维：备份、日志、更新、CLI

本节涵盖面板的日常维护：创建和恢复数据库备份、查看面板和 Xray 的日志、重启和停止服务、更新 Xray 及面板本身、定期任务（cron）以及卸载面板。部分操作通过 Web 界面完成（「仪表盘」和「面板设置」页面上的标签页），部分操作通过服务器上的 `x-ui` 控制台菜单完成。

### 16.1. 数据库备份与恢复

面板的所有数据（入站/inbound、客户端、分组、节点、设置）都存储在同一个数据库中。备份管理位于 **「仪表盘」** 页面的 **「备份」** 标签页，区块标题为 **「备份与恢复」**。

面板支持两种数据库引擎，备份行为也因此而异：

- **SQLite**（默认方案）——数据存放在文件 `x-ui.db` 中。
- **PostgreSQL**——如果面板配置为使用 PostgreSQL，区块中会显示提示：
  > 「本面板运行在 PostgreSQL 上。『备份』会下载一个 pg_dump 归档（.dump），『恢复』会通过 pg_restore 将其载入回去。服务器上必须安装 PostgreSQL 客户端工具（pg_dump 和 pg_restore）。」

#### 导出（创建副本）

**「导出数据库」** 按钮（英文 `Back Up`）会将备份文件下载到您的设备。

| 数据库引擎 | 文件名 | 服务器上发生的操作 |
|-----------|-----------|----------------------------|
| SQLite | `x-ui.db` | 先执行 WAL checkpoint，以确保文件包含最新写入，然后整个文件被读取并提供下载 |
| PostgreSQL | `x-ui.dump` | 运行 `pg_dump`，归档被提供下载 |

界面中的提示：
- SQLite：「点击以将包含您当前数据库备份的 .db 文件下载到您的设备。」
- PostgreSQL：「点击以将当前数据库的 PostgreSQL 转储（.dump）下载到您的设备。」

从技术上讲，导出就是一个 `GET /panel/api/server/getDb` 请求。附件名由服务器根据引擎生成（`Content-Disposition`）。

备份文件名按服务器地址生成，而非固定的 `x-ui.db` / `x-ui.dump`。从浏览器下载时，文件名取自地址栏中的面板地址（请求主机名）；否则取自配置的 Web 域名，若没有则取自服务器的公网 IP（先 IPv4，再 IPv6），最后回退为 `x-ui`。这样就便于区分来自不同服务器的备份。扩展名对 SQLite 保持为 `.db`，对 PostgreSQL 保持为 `.dump`；通过 Telegram 发送的备份也按同样的域名/IP 命名。

**示例：通过 API 下载备份。** 同样的导出也可以通过控制台请求获取——例如用于自动备份脚本。需要一个已授权的会话（登录 cookie）：

```bash
# 1) 登录并保存会话 cookie
curl -s -c cookies.txt \
     -d 'username=admin&password=admin' \
     https://panel.example.com:2053/panel/login

# 2) 下载数据库文件（文件名由服务器指定：x-ui.db 或 x-ui.dump）
curl -s -b cookies.txt -OJ \
     https://panel.example.com:2053/panel/api/server/getDb
```

如果面板通过基础路径（Web Base Path）打开，需要将其加入 URL：`…:2053/<base_path>/panel/api/server/getDb`。

#### 导入（恢复）

**「导入数据库」** 按钮（英文 `Restore`）会打开文件选择并将文件上传到服务器以进行恢复（`POST /panel/api/server/importDB`，表单字段 `db`）。

界面中的提示：
- SQLite：「点击以从您的设备选择并上传一个 .db 文件，从备份恢复数据库。」
- PostgreSQL：「点击以选择并上传一个 .dump 文件来恢复 PostgreSQL 数据库。这将替换所有当前数据。」

**SQLite 的导入过程（重点在于它是原子性的，且支持回滚）：**
1. 检查上传文件的格式——必须是有效的 SQLite 数据库；否则返回错误「Invalid db file format」。
2. 文件被保存为临时文件 `x-ui.db.temp` 并进行完整性检查。
3. 在替换数据库前 **停止 Xray**。
4. 当前数据库被重命名为备份 `x-ui.db.backup`（fallback）。
5. 临时文件被移动到工作数据库的位置，执行架构初始化与迁移，然后进行 inbound 迁移。
6. **如果任一步骤出错** ——执行回滚：从 `x-ui.db.backup` 恢复先前的数据库，并在旧数据上重启 Xray。
7. 成功时删除 fallback 文件，**Xray 自动重启** 并使用已恢复的数据。

操作结束后的界面消息：

| 结果 | 文本 |
|-----------|-------|
| 成功 | 「数据库导入成功」 |
| 导入错误 | 「导入数据库时发生错误」 |
| 文件读取错误 | 「读取数据库时发生错误」 |

> 恢复会完全替换当前数据。由于 Xray 在此过程中会短暂停止，导入期间现有的客户端连接会被中断。

#### 引擎间迁移文件（SQLite ⇄ PostgreSQL）

除了普通备份之外，还有一个 **「下载迁移文件」** 功能（`Download Migration`，请求 `GET /panel/api/server/getMigration`）。它会生成一个可移植的文件，用于切换到另一个数据库引擎：

| 当前引擎 | 下载的内容 | 文件名 | 用途 |
|----------------|-----------------|-----------|------------|
| SQLite | 可移植的 SQL 转储（文本） | `x-ui.dump` | 用您的数据填充 PostgreSQL |
| PostgreSQL | 由 PostgreSQL 数据组装而成的 SQLite 数据库 | `x-ui.db` | 将面板切换回 SQLite |

提示：
- 在 SQLite 上：「点击以下载您的 SQLite 数据库的可移植 .dump 导出（SQL 文本）。」
- 在 PostgreSQL 上：「点击以下载由您的 PostgreSQL 数据组装而成、可用于在 SQLite 上运行面板的 SQLite 数据库（.db）。」

SQLite 的 `.db ⇄ .dump` 转换也可以通过 CLI 命令 `x-ui migrateDB [file]` 完成（见 16.7 节）。

#### 通过 Telegram 机器人备份

如果配置了 Telegram 机器人（见关于通知的章节），它可以将备份直接发送到管理员聊天中。通过 Telegram 备份包括 **两个文件**：数据库本身（`x-ui.db`，在 PostgreSQL 上为 `x-ui.dump`）和 Xray 配置 `config.json`。消息前会有一行「🗄 备份时间：…」。

在 Telegram 中获取备份有两种方式：

1. **按需获取。** 机器人菜单中的 **「📂 数据库备份」** 按钮——机器人会立即将文件发送到当前聊天。
2. **随报告自动发送。** 机器人设置中有一个开关 **「数据库备份」**（`Database Backup`），描述为「发送带有数据库备份文件的通知」。开启后，每次定期发送报告时，机器人会在报告之后向所有管理员发送备份。报告的发送周期由机器人的 cron 计划设定（见 16.6 节）。机器人会在文件之间以及管理员之间稍作停顿，以免超出 Telegram 的限制。

> 通过机器人的备份只有在机器人运行时才会发送；在 PostgreSQL 上还要求服务器上安装有 `pg_dump`。

### 16.2. 查看日志

面板中有两个独立的日志查看工具，都从「仪表盘」上的 **「日志」** 标签页打开。每个窗口都能刷新（标题中的「刷新」图标）并将所显示的内容下载为文件 `x-ui.log`（带下载图标的按钮）。

#### 面板日志（应用程序 / syslog）

面板日志窗口（`POST /panel/api/server/logs/{count}`）。控件：

| 控件 | 默认值 | 说明 |
|---------|------------------------|----------|
| 行数 | `20` | 下拉列表：10 / 20 / 50 / 100 / 500 |
| 级别 | `Info` | 最低级别：Debug / Info / Notice / Warning / Error |
| SysLog（复选框） | 关闭 | 从何处获取日志：从应用程序缓冲区还是从系统日志 |

行为取决于 **SysLog** 复选框：

- **关闭（默认）：** 日志取自面板内部的环形缓冲区，并按所选级别过滤。记录会显示级别（DEBUG / INFO / NOTICE / WARNING / ERROR）和来源：`X-UI:` ——面板本身的消息，`XRAY:` ——转发过来的 Xray 消息。
- **开启：** 面板在服务器上执行 `journalctl -u x-ui --no-pager -n <count> -p <level>`，即显示 `x-ui` 服务的系统日志。允许的行数为 1 到 10000；级别接受 syslog 取值（`emerg/0`、`alert/1`、`crit/2`、`err/3`、`warning/4`、`notice/5`、`info/6`、`debug/7`）。在 Windows 上不支持 SysLog 模式——会显示一条警告，提示需要取消勾选并使用应用程序日志。如果 `systemd`/服务不可用，会出现 `journalctl` 启动错误的消息。

**示例：从服务器控制台获取同一份日志。** 当面板不可用时（例如无法启动），可以直接读取系统日志——这正是面板在 SysLog 模式下执行的命令：

```bash
# warning 级别及以上的最后 100 行
journalctl -u x-ui --no-pager -n 100 -p warning

# 实时跟踪日志
journalctl -u x-ui -f
```

> 此窗口中的级别过滤的是 **输出**。究竟有哪些最低级别会被写入控制台/syslog，由面板的日志级别决定（环境变量，默认为 `Info`；写入文件时面板始终以 `DEBUG` 级别记录）。

#### Xray 日志（访问日志）

这是 Xray 访问日志的独立窗口（`POST /panel/api/server/xraylogs/{count}`）。它会解析 Xray 访问日志中的行并以表格形式显示：**Date、From、To、Inbound、Outbound、Email**。

| 控件 | 默认值 | 说明 |
|---------|------------------------|----------|
| 行数 | `20` | 10 / 20 / 50 / 100 / 500 |
| **过滤** | 空 | 按子字符串进行文本搜索（按 Enter 应用） |
| **Direct**（复选框） | 开启 | 显示直连（通过 freedom-outbound 的流量） |
| **Blocked**（复选框） | 开启 | 显示被阻止的连接（流向 blackhole-outbound 的流量） |
| **Proxy**（复选框） | 开启 | 显示被代理的流量 |

事件类型会根据日志行中出站连接的标签自动判定：匹配 freedom 标签 →「DIRECT」（绿色），blackhole →「BLOCKED」（红色），其余一切 →「PROXY」（蓝色）。`api -> api` 行和空行会被跳过。

> 为了让此窗口显示记录，Xray 必须启用带文件路径（而非 `none`）的 **访问日志** ——见下文。如果访问日志被禁用或文件不可用，窗口将为空（「No Record...」）。

### 16.3. Xray 日志级别与日志设置

Xray 自身的日志记录参数在 **「Xray 配置」** 页面的 **「日志」**（`Log`）区块中设置，带有警告：
> 「日志可能会拖慢服务器运行。仅在需要时开启您所需的日志类型！」

| 字段 | 译名 | 默认值 | 说明 |
|------|---------|------------------------|----------|
| **日志级别**（`logLevel`） | Log Level | `warning` | Xray 错误日志的详细程度。允许的取值：`debug`、`info`、`notice`、`warning`、`error`。提示：「错误日志的日志级别，指明需要记录的信息。」 |
| **访问日志**（`accessLog`） | Access Log | `none` | 访问日志文件的路径。特殊值 `none` 会禁用访问日志。提示：「访问日志文件的路径。特殊值『none』会禁用访问日志。」 |
| **错误日志**（`errorLog`） | Error Log | 空（默认路径） | 错误日志文件的路径；`none` 会禁用它们。提示：「错误日志文件的路径。特殊值『none』会禁用错误日志。」 |
| **DNS 日志**（`dnsLog`） | DNS Log | `false`（关闭） | 启用 DNS 查询的日志记录。提示：「启用 DNS 查询日志」。 |
| **地址掩码**（`maskAddress`） | Mask Address | 空（关闭） | 启用后，日志中真实 IP 地址会被自动替换为掩码地址。提示：「启用后，日志中真实 IP 地址会被替换为掩码地址。」 |

> 由于默认情况下 **「访问日志」= `none`**，「Xray 日志」窗口（16.2 节）一开始是空的。要让它工作，请在此处设置访问日志的路径并重启 Xray。

> 请注意：空的访问日志只影响这个窗口。「仪表盘」上的在线客户端列表以及客户端表单中的 IP 数量限制 **不依赖** 访问日志——面板通过 Xray 核心的 online-stats API（连接统计）来判定在线客户端并统计其 IP 地址。在没有该 API 的旧版核心上，面板会自动回退到旧的方式（读取访问日志），这时为了 IP 限制功能，这里的访问日志路径仍然是必需的。

> **IP 数量限制与 fail2ban。** 客户端的 IP 数量限制本身（客户端表单及批量添加中的「IP Limit」字段）只有在服务器上安装了 **fail2ban** 时才会在服务器上生效——正是它来封禁超出限制的地址。面板会检查 fail2ban 是否存在（`GET /panel/api/server/fail2banStatus`）；如果没有，「IP Limit」字段会变为不可用并附带说明提示（在 Windows 上为单独的消息），而此前在这类服务器上设置的限制会被自动清零，因为它们本来也不生效。fail2ban 的封禁同时作用于 TCP 和 UDP。在普通服务器上，现在安装和更新面板时会自动安装 fail2ban（见 16.5 节）。

**示例：让「Xray 日志」窗口开始显示记录的 `log` 区块。** 在 Xray 的 JSON 配置中是这样的：

```json
{
  "log": {
    "loglevel": "warning",
    "access": "./access.log",
    "error": "",
    "dnsLog": false,
    "maskAddress": ""
  }
}
```

关键是把 `"access": "none"` 替换为文件路径（例如 `"./access.log"`）。保存后重启 Xray，「Xray 日志」窗口中的表格就会填满记录行。

### 16.4. Xray 管理：停止与重启

Xray 的状态从「仪表盘」上的 Xray 卡片进行管理。当前状态显示为以下取值之一：**运行中**（`Running`）、**已停止**（`Stopped`）、**未知**（`Unknown`）、**错误**（`Error`）。出错时可看到悬浮提示「启动 Xray 时出错」。

| 按钮 | 译名 | 端点 | 操作 |
|--------|---------|----------|----------|
| **停止** | `Stop` | `POST /panel/api/server/stopXrayService` | 停止 Xray 进程。成功时——警告通知「Xray service has been stopped」。 |
| **重启** | `Restart` | `POST /panel/api/server/restartXrayService` | 应用当前配置重启（或启动）Xray。成功时——通知「Xray service has been restarted successfully」。 |

任一操作之后，面板会通过 WebSocket 广播新状态，因此「仪表盘」上的状态无需刷新页面即可更新。如果操作以错误结束，Xray 状态会变为「错误」，错误文本会出现在通知中。

> 除了手动重启之外，面板自身还会检查是否需要重启 Xray（每 30 秒一次的后台任务）以及进程是否已崩溃（每秒检查一次）——见 16.6 节。

### 16.5. 面板的重启与更新

#### 重启面板

在 **「面板设置」** 页面有一个 **「重启面板」** 操作（`Restart Panel`，`POST /panel/api/setting/restartPanel`）。确认后，面板会 **在 3 秒后** 重启。

消息：
- 确认：「您确定要重启面板吗？请确认，重启将在 3 秒后进行。如果面板不可用，请检查服务器日志。」
- 成功：「面板重启成功」。

从技术上讲，在 Linux 上重启是通过向面板进程发送 `SIGHUP` 信号（或通过已注册的钩子）来完成的。在 Windows 上不支持发送 `SIGHUP`。

#### 面板自我更新（Update Panel）

在「仪表盘」上可使用 **「更新面板」** 功能（`Update Panel`）——直接从 Web 界面将 3X-UI 更新到最新版本。

更新前，面板会比对版本（`GET /panel/api/server/getPanelUpdateInfo`），向 GitHub 请求 3x-ui 的最新版本：

| 字段 | 译名 |
|------|---------|
| **当前面板版本** | Current panel version |
| **最新面板版本** | Latest panel version |
| **面板已是最新** /「已是最新」 | Panel is up to date / Up to date——在没有新版本时显示 |

启动更新——`POST /panel/api/server/updatePanel`。确认对话框：
- 「您确定要更新面板吗？」
- 「这会将 3X-UI 更新到版本 #version# 并重启面板服务。」

启动后——弹出消息「面板更新已开始」（`Panel update started`）；版本检查失败时——「面板更新检查失败」（`Panel update check failed`）。

**服务器上发生的操作：** 自我更新 **仅在 Linux 上** 受支持（在其他操作系统上会返回错误「panel web update is supported only on Linux installations」）。面板从 GitHub（`raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh`）下载官方脚本 `update.sh` 并在单独的进程中运行它：优先通过 `systemd-run` 在单独的单元中运行（`x-ui-web-update-<timestamp>`），在没有 systemd 时——作为单独的分离进程运行。运行结束后，脚本会更新各组件并重启面板服务。运行需要 `bash`。

如果在更新过程中脚本生成了新的随机 Web 面板基础路径（Web Base Path），`x-ui` 服务会自动重启，以便新路径立即生效。（不重启的话，服务器会继续提供旧路径，而界面会显示新路径，新地址在手动重启之前都将不可访问。）

> 在节点上，同一个 3x-ui 面板会通过 `POST /panel/api/nodes/updatePanel` 集中更新——见关于节点的章节。

#### 自动安装 fail2ban

为了让客户端的 IP 数量限制（16.3 节）开箱即用，现在在普通服务器上安装和更新面板时会自动安装并配置 `fail2ban`（以前这只在 Docker 镜像中发生）。其行为由环境变量 `XUI_ENABLE_FAIL2BAN` 控制：当该变量未设置或等于 `true` 时执行配置。手动运行可用命令 `x-ui setup-fail2ban`。fail2ban 配置失败不会中断面板的安装或更新。

#### 在纯 IPv6 主机上的安装与更新

脚本 `install.sh` 和 `update.sh` 现在能在仅有 IPv6 的服务器上正常工作：下载版本、`x-ui.sh` 脚本和服务文件不再强制使用 IPv4（`curl -4`），而是使用可用的协议。因此即便在没有 IPv4 地址的主机上也能安装和更新面板。

#### 通过 `XUI_PORT` 变量覆盖面板端口

Web 面板的监听端口可以通过环境变量 `XUI_PORT` 覆盖——它仅在当前进程运行期间生效，**不会改变** 数据库中保存的 `webPort` 值。允许的取值为 `1` 到 `65535`；空值、无效值或超出范围的值会被忽略（改用 `webPort`）并在日志中给出警告。这在部署时很方便，首先是在 Docker 中：使用 bridge 网络时，容器发布的端口应与 `XUI_PORT` 一致——例如 `XUI_PORT=8080` 和 `ports: "8080:8080"`。

#### 更新和切换 Xray-core 版本

在同一个「仪表盘」上，可以独立于面板来管理 Xray-core 的版本。

- **Xray 更新**（`Xray Updates`）/ **版本选择**（`Version`）——可用版本的下拉列表。提示：「选择所需版本」以及警告「重要：旧版本可能不支持当前设置」。
- 安装/切换版本——`POST /panel/api/server/installXray/{version}`。对话框：「切换 Xray 版本」/「您确定要更换 Xray 版本吗？」。成功时——「Xray 更新成功」。

**示例：通过 API 请求更换 Xray-core 版本。** 版本以 XTLS/Xray-core 的发布标签指定（带 `v` 前缀）。例如，切换到 `v1.8.24`：

```bash
curl -s -b cookies.txt -X POST \
     https://panel.example.com:2053/panel/api/server/installXray/v1.8.24
```

（`cookies.txt` 是 16.1 节示例中的 cookie 文件。）安装后，Xray 会自动以所选版本重启。

在服务器上更换版本时，Xray 先停止，从 GitHub（XTLS/Xray-core）下载所需版本的归档，解压并替换二进制文件，然后在校验归档/二进制文件的校验大小后重启 Xray。

### 16.6. 定期任务（cron）

面板在启动时注册了一系列后台任务。它们的计划是固定的（不在 UI 中配置，Telegram 报告计划和 LDAP 同步除外）。以下是与运维相关的任务。

| 任务 | 计划 | 用途 |
|--------|-----------|------------|
| 检查 Xray 是否运行 | 每 1 秒 | 监控 Xray 进程是否在运行 |
| 检查是否需要重启 Xray | 每 30 秒 | 当配置被标记为已更改时重启 |
| 采集 Xray 流量 | 每 5 秒（启动后 5 秒开始） | 统计 inbound/客户端的流量 |
| 检查客户端 IP | 每 10 秒 | 按日志监控 IP 限制 |
| 节点的心跳与流量同步 | 每 5 秒 | 与节点交换数据 |
| **清理日志** | **每天**（`@daily`） | 清理 IP-limit 日志和持久化访问日志，将当前日志轮转为 `*.prev.log` |
| **按周期重置流量** | `@hourly`、`@daily`、`@weekly`、`@monthly` | 重置那些设置了相应自动重置周期的 inbound（及其客户端）的流量计数器 |
| Telegram 报告 | 在机器人设置中设定（默认 `@daily`） | 向管理员发送报告；启用该选项时——附带数据库备份（16.1 节） |
| 重置 Telegram hash 存储 | 每 2 分钟 | 仅在机器人启用时 |
| 为 Telegram 监控 CPU 负载 | 每 10 秒 | 仅当设置了 CPU 阈值 > 0 时 |

此外：

- **周期性重置流量** 只对那些选择了相应自动重置模式（每小时/每天/每周/每月）的 inbound 触发。该任务会重置 inbound 本身及其所有客户端的流量。
- **到期与耗尽检查。** 客户端因到期及因流量限额耗尽而被禁用，是在流量统计的框架内进行的：`expiry_time` 已到期或流量额度已耗尽的客户端会被标记并禁用，必要时会计算下一个期限（用于循环限额和「首次使用起计」模式）。在「仪表盘」及各列表中，这会通过「已过期」/「已耗尽」/「即将到期」等状态体现。
- **自动备份到 Telegram** 是报告任务的副作用，并没有专门只用于备份的独立 cron 计划。因此自动备份的频率等于机器人报告的频率。

### 16.7. 控制台菜单与 CLI（`x-ui`）

在服务器上，面板通过 `x-ui` 命令管理。不带参数时会打开交互式菜单「3X-UI Panel Management Script」；带参数时会执行具体的子命令。与运维相关的菜单项：

| 菜单序号 | 菜单项 | 操作 |
|----------|-------|----------|
| 1 | Install | 安装面板（下载并运行 `install.sh`） |
| 2 | Update | 将所有 x-ui 组件更新到最新版本而不丢失数据；之后——自动重启 |
| 3 | Update Menu | 仅更新 `x-ui` 菜单脚本本身 |
| 4 | Legacy Version | 按输入的版本号安装指定的（旧）版本面板（例如 `2.4.0`） |
| 5 | Uninstall | 完全卸载面板和 Xray（见 16.8） |
| 6 | Reset Username & Password | 重置管理员的登录名/密码 |
| 7 | Reset Web Base Path | 重置 Web 面板的基础路径 |
| 8 | Reset Settings | 将设置重置为默认值 |
| 9 | Change Port | 更换面板端口 |
| 10 | View Current Settings | 查看当前设置 |
| 11–13 | Start / Stop / Restart | 启动、停止、重启面板服务 |
| 14 | Restart Xray | 仅重启 Xray |
| 15 | Check Status | 服务的当前状态 |
| 16 | Logs Management | 查看和清理日志（见下文） |
| 17–18 | Enable / Disable Autostart | 开启/关闭操作系统启动时服务的自动启动 |
| 25 | Update Geo Files | 更新地理文件（GeoIP/GeoSite） |
| 27 | PostgreSQL Management | 管理 PostgreSQL |

#### CLI 中的日志管理（第 16 项）

在「Logs Management」子菜单中：
- **Debug Log** ——流式查看服务日志：`journalctl -u x-ui -e --no-pager -f -p debug`（在 Alpine 上——对 `/var/log/messages` 执行 `grep`）。
- **Clear All logs** ——清理系统日志：`journalctl --rotate` + `journalctl --vacuum-time=1s`，之后服务会重启。（在 Alpine 上不可用。）

#### `x-ui` 的直接子命令

所有可用的子命令：

| 命令 | 说明 |
|---------|----------|
| `x-ui` | 打开管理菜单 |
| `x-ui start` | 启动面板 |
| `x-ui stop` | 停止面板 |
| `x-ui restart` | 重启面板 |
| `x-ui restart-xray` | 重启 Xray |
| `x-ui status` | 当前状态 |
| `x-ui settings` | 显示当前设置 |
| `x-ui enable` | 开启操作系统启动时的自动启动 |
| `x-ui disable` | 关闭自动启动 |
| `x-ui log` | 查看日志 |
| `x-ui banlog` | 查看 Fail2ban 封禁日志 |
| `x-ui setup-fail2ban` | 为 IP 限制安装并配置 fail2ban（见 16.5） |
| `x-ui update` | 更新面板 |
| `x-ui update-all-geofiles` | 更新所有地理文件（之后会重启） |
| `x-ui migrateDB [file]` | 转换数据库 `.db ⇄ .dump`（SQLite） |
| `x-ui legacy` | 安装旧版本 |
| `x-ui install` | 安装面板 |
| `x-ui uninstall` | 卸载面板 |

> `x-ui update` 命令会下载并运行官方的 `update.sh`（与 16.5 节的 Web 更新相同），并请求确认：「This function will update all x-ui components to the latest version, and the data will not be lost.」运行结束后，面板会自动重启。

> **`setting` 子命令中的 `-webCert` / `-webCertKey` 标志。** Web 面板的证书和私钥路径可以直接在子命令 `x-ui setting -webCert <路径> -webCertKey <路径>` 中设置——指定这两个标志中的任意一个都会保存相应路径（与单独的 `cert` 子命令一样），面板会立即切换到 HTTPS。

#### 通过 CLI 获取 API 令牌

通过 CLI 获取 API 令牌的命令（菜单项/命令 `x-ui`）不会显示先前发放的令牌。API 令牌仅以哈希形式存储，因此无法以明文形式获取已有令牌。如果令牌已配置，命令会告知其数量，建议在面板中管理令牌（**Settings → API Tokens**，见关于 API 令牌的章节），并立即生成一个名称形如 `cli-fallback-<timestamp>` 的 **新备用令牌** 并将其输出，以便 CLI 无需进入界面也能保持可用。

### 16.8. 卸载面板

卸载从 CLI 进行——菜单项 **5（Uninstall）** 或命令 `x-ui uninstall`。卸载前会请求确认（默认为「否」）：「Are you sure you want to uninstall the panel? xray will also uninstalled!」。

确认后，脚本会：
1. 停止服务并关闭其自动启动（`systemctl stop/disable x-ui`，在 Alpine 上为 `rc-service`/`rc-update`），删除服务的 unit 文件并重新加载 systemd 配置。
2. 删除数据和应用目录（`/etc/x-ui/`、安装目录）以及服务的 env 文件（`/etc/default/x-ui`、`/etc/conf.d/x-ui` 或 `/etc/sysconfig/x-ui` ——取决于发行版）。
3. 删除 `x-ui` 脚本本身，并输出消息「Uninstalled Successfully.」以及重新安装的命令。

> 卸载不可逆：面板连同 Xray 及所有数据（包括数据库）都会被删除。如果数据可能还有用，请提前导出数据库（16.1 节）。

### 16.9. `x-ui migrateDB` 命令

从 3.3.0 版本起，管理脚本 `x-ui.sh` 增加了 `migrateDB` 子命令——它是对内置二进制文件 `x-ui`（`x-ui migrate-db`）的封装，用于在两种格式之间转换面板的 SQLite 数据库：二进制的 `.db` 和可移植的文本转储 `.dump`（普通 SQL 文本）。

#### 命令的作用

该命令可双向工作，且方向会 **自动** 根据输入文件确定：

| 方向 | 名称 | 发生的操作 |
|---|---|---|
| `.db → .dump` | dump（导出） | 二进制 SQLite 数据库导出为文本 SQL 文件 |
| `.dump → .db` | restore（恢复） | 从文本 SQL 文件重新组装出二进制 SQLite 数据库 |

在底层，脚本会调用面板的二进制文件：
- 导出：`x-ui migrate-db --src <输入> --dump <输出>`
- 恢复：`x-ui migrate-db --restore <输入> --out <输出>`

#### 调用语法

```
x-ui migrateDB [file.db|file.dump] [output]
```

- **`[file.db|file.dump]`** ——输入文件（第一个参数）。如果不指定，则取面板已安装的默认数据库：`/etc/x-ui/x-ui.db`。
- **`[output]`** ——输出文件的路径（第二个参数）。可选：不指定时，会在输入文件旁边自动选取名称（见下文）。

示例：

```
x-ui migrateDB                              # 导出 /etc/x-ui/x-ui.db -> /etc/x-ui/x-ui.dump
x-ui migrateDB /etc/x-ui/x-ui.db backup.dump
x-ui migrateDB backup.dump restored.db      # 从转储组装 .db
```

#### 方向是如何确定的

脚本会查看输入文件的扩展名：
- `*.db`、`*.sqlite`、`*.sqlite3` → **dump** 模式（导出为文本）；
- `*.dump`、`*.sql` → **restore** 模式（组装数据库）。

如果扩展名无法识别，脚本会读取文件的前 16 个字节：签名 `SQLite format 3` 表示二进制数据库（dump 模式），否则文件被视为转储（restore 模式）。

未指定第二个参数时的输出文件名：
- 导出时——与输入相同的名称，扩展名为 `.dump`；
- 恢复时——相同的名称，扩展名为 `.db`。

#### 保护性检查与行为

- **二进制文件是否存在。** 如果找不到 `x-ui` 二进制文件或其不可执行——会输出错误「x-ui binary not found … Is the panel installed?」。
- **构建是否支持该功能。** 脚本会检查二进制文件是否支持 `migrate-db --dump/--restore`（通过 `x-ui migrate-db -h`）。如果不支持——会建议先用命令 `x-ui update` 更新面板。
- **输入文件是否存在。** 如果输入文件不存在，会打印错误以及调用语法行。
- **覆盖输出。** 如果输出文件已存在，会请求确认（默认为「否」）；未确认则操作取消。恢复时会先删除旧的输出文件。
- **保护「活动」数据库。** 当面板正在运行、且要恢复到默认数据库 `/etc/x-ui/x-ui.db` 时，操作会被拒绝，并要求先停止面板（`x-ui stop`）或选择其他输出路径。这可防止覆盖正在运行的服务的工作数据库。
- 如果数据库组装失败，未写完的输出文件会被删除。

#### 为什么需要它

- **备份。** 文本 `.dump` 是人类可读的，便于存放在版本控制系统中，也便于对数据库内容做差异查看。
- **迁移。** 转储在不同机器之间可移植，且对 SQLite 文件格式版本差异具有鲁棒性——在新服务器上可由它组装出可用的 `.db`。
- **诊断。** 即使手边没有 SQLite 工具，也可以从 `.dump` 中用肉眼查看面板的结构和数据。

#### 交互式模式

除了直接调用，转换也可以从交互式菜单进行。在 PostgreSQL 子菜单（`x-ui` → PostgreSQL 操作部分）中有一项 **9. Convert SQLite `.db <-> .dump`**：它会询问输入文件的路径（默认 `/etc/x-ui/x-ui.db`）和输出文件的路径（可留空以自动命名），而方向与 CLI 模式一样会自动确定。

---

*本文档依据 3X-UI 源代码编写。如果某项界面在您的版本中有所不同，
以面板的行为和 UI 中的提示为准。*

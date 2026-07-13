# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 简体中文 · 🇹🇼 [繁體中文](README.zh-TW.md)

用于 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板的用户手册 — 一份为面板 **v3.5.0** 编写的综合使用指南。

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

## 3.5.0 新特性

3.5.0 是一次重大发布：MTProto 改用多客户端模型（mtg-multi 引擎、每客户端独立密钥、配额与 ad-tag），托管主机改为分组式（一条记录内含多个 inbound 和多个地址），PostgreSQL 面板的恢复功能可接受 SQLite 备份，outbound 新增「Target Strategy」、「Real delay」测试以及 Egress/Country 列，负载均衡器可将另一个负载均衡器用作 fallback。随附 Xray 核心 26.7.11。以下列出相对于 3.4.2 的变更，按手册章节分组。

### 第 1 节的更改 — 简介、系统要求与安装

- Xray 核心已更新至 **26.7.11**。随之而来的自动迁移：Shadowsocks 的 `none`/`plain` 与 VMess 的 `none`/`zero` 加密方式已从核心中移除（已保存的配置会自动改写），指向公网地址的未加密 VLESS/Trojan outbound 在保存时会被拒绝。
- 新增 **`x-ui pgclient [版本]`** 命令和 PostgreSQL 菜单中的 **10. Install/Upgrade client tools (pg_dump/pg_restore)** 菜单项——用于安装/升级 PostgreSQL 客户端工具。
- 脚本修复：RHEL 系（EPEL）上的 PostgreSQL 与 fail2ban 安装、Arch 不再执行完整的 `pacman -Syu`、32 位 ARM 上 Xray 二进制文件名已修正（`xray-linux-arm32`）、签发 IP 证书前确认自动检测到的 IPv4，并修复了选择默认 ACME 端口时误报的「Your input is invalid」。

### 第 2 节的更改 — 登录面板与访问安全

- IP 限制：「死」连接现在只封禁**一次**，而不是在每次 10 秒扫描时重复封禁——fail2ban 计数器不再虚增，无需再调高 `maxretry`。

### 第 4 节的更改 — Inbounds：创建与通用参数

- inbound 列表新增**搜索**（按备注、端口和协议），节点下拉列表（「部署到」、「节点」筛选器）也支持搜索。

### 第 5 节的更改 — 协议

- **MTProto 改用多客户端模型**（mtg-multi 引擎）：MTProto 用户现在是普通客户端，拥有自己的密钥、配额、有效期、ad-tag 和专属 `tg://proxy` 链接。inbound 级别的「Secret」字段已移除（现有 inbound 会自动转换），「FakeTLS domain」成为新密钥的默认域名。新的 inbound 字段：**Max connections**（连接数限制）、**Public IPv4/IPv6**（用于 ad-tag middle proxy）。客户端更改「热」应用，不会中断其他用户的 Telegram 会话。
- WireGuard：inbound 菜单获得完整的客户端操作集（Export All URLs、绑定/解绑、分组），导出拆分为 **Config** 和 **Links** 两个选项卡，**「WireGuard 允许的 IP」字段变为可编辑**（多个条目以逗号分隔），节点 inbound 的客户端配置中 `Endpoint` 现在指向节点地址。

### 第 7 节的更改 — 连接安全：TLS、XTLS 与 REALITY

- **Finalmask + REALITY 组合在保存时会被拒绝**（该组合会导致 Xray-core 在首次连接时崩溃）；minClientVer 占位符已更新为 26.3.27。
- Finalmask 新增 TCP 掩码类型——**XMC（Minecraft）**：将流量伪装成 Minecraft 流量（Hostname、Usernames，以及必填、可自动生成的 Password）。

### 第 8 节的更改 — 客户端

- 新增**「速度」**列——每个客户端的实时速度（↑/↓，约 5 秒滑动平均值）。
- 客户端搜索恢复支持按 **Telegram ID** 查找；客户端表单的绑定列表中隐藏已禁用的 inbound；修复了「解绑」窗口中重复条目累积的问题。
- MTProto 客户端拥有专属字段：**「MTProto secret」**（可重新生成）和**「Ad-tag（赞助频道）」**（32 个十六进制字符）；配额和有效期现在对 MTProto 真正生效。

### 第 9 节的更改 — 客户端分组

- 客户端信息窗口现在会显示其所属**分组**。

### 第 10 节的更改 — 订阅（Subscription）

- **托管主机改为分组式**：一条记录可覆盖**多个 inbound**（多选）和**多个地址**（标签式输入，每个条目可带自己的 `:端口`；地址自动补全；留空则继承 inbound 地址）。列表的列以芯片形式显示地址和 inbound（带「+N」），操作和 API 均以分组（`groupId`）为单位，并新增了批量端点 `POST /panel/api/hosts/bulk/add`。主机排序现在是全局的（先按排序序号，再按备注）。
- **公告**文本（`subAnnounce`）现在会以横幅形式显示在订阅信息页面上；自定义模板中可使用 `announce` 变量。
- 现在通过 **JSON/Clash 链接**（而不仅是主链接）也能在浏览器中打开信息页面。
- 主机设置 **Final Mask** 与 **Allow insecure** 现在分别也作用于 raw 链接（`fm=`）和 **Hysteria2**（`insecure=1` / `skip-cert-verify: true`）。
- 「订阅更新间隔」（`subUpdates`）的取值范围修正为 **0–525600**（此前界面上限 168 会在从 2.x 升级后阻止保存设置）。
- 原生 **WireGuard 客户端现在会进入 Clash 和 JSON 订阅**（此前仅进入 raw）。

### 第 11 节的更改 — Xray：路由、outbounds、DNS 与扩展

- Outbound 编辑器：新增**「Target Strategy」**字段（从 `AsIs` 到 `ForceIPv4` 共 11 个值）、**「Real delay」**测试模式（包含隧道建立在内的完整耗时；HTTP 模式现在按「热」连接测量），以及 HTTP/Real 测试后的 **Egress** 列（出口 IP，藏在「眼睛」图标后）和 **Country** 列（旗帜 + 国家名称，WARP 标记）。
- **负载均衡器的 Fallback 可以指向另一个负载均衡器**：面板会自动构建隐藏的 loopback 对象（`_bl_…`），并防止循环依赖及删除正在使用的负载均衡器；`_bl_` 前缀已被保留。
- 「基本路由」选项卡新增**「Default Outbound」**选择器——决定由哪个 outbound 处理未命中任何规则的流量（所选 outbound 会移至首位）。
- 私有 IP 上的 DNS 服务器不再被 `geoip:private` 规则拦截——面板会自行维护一条受管的放行规则。
- dial 设置（sockopt）中的 Happy Eyeballs 现在能真正启用；「Try delay」默认 250 毫秒，显式设置的 0 会被保留。
- outbound 订阅导入：带 `?plugin=`/结尾 `/` 的 `ss://` 链接现在能正确解析端口。

### 第 12 节的更改 — 节点（多面板，master/slave）

- 一组修复：未做修改地保存客户端不再中断节点 inbound 的实时流量；节点的 Host 覆盖会在首次接受时导入主面板；自动续期会开启新的配额窗口；在主面板删除客户端会将其从节点上完全删除；节点的 inbound 在首次接受前不会被清除；单个异常 inbound 不再阻断节点流量同步；端口冲突检查仅限于所在节点。

### 第 14 节的更改 — Telegram 机器人

- 机器人命令菜单新增 **`/usage`**、**`/inbound`**、**`/restart`**，以及新的管理员命令 **`/clearall`**（重置所有客户端流量，需确认）。
- 在线客户端列表以 `email - inbound 备注` 标注；备份和封禁日志消息包含主机名；按 Telegram ID 搜索不受设置格式化方式影响。

### 第 16 节的更改 — 日常运维：备份、日志、更新、CLI

- **PostgreSQL 面板的恢复功能可接受 SQLite 文件**：普通 `.db` 备份或迁移 `.dump` 可直接导入 PostgreSQL（单个事务，并在停止 Xray 前完成检查）。两种数据库引擎的文件选择对话框均接受 `.dump,.db`；「下载迁移文件」仅保留在 PostgreSQL 面板上。
- 恢复 `pg_dump` 归档前，面板会检查转储文件的可读性，版本不匹配时会提示准确的 `x-ui pgclient <版本>` 命令。
- 启动时自动修复：溢出的流量计数器会被钳制并恢复；移除 inbound 端口上过时的 UNIQUE 约束（它曾妨碍 multi-node）。
- Xray 日志：新的定时任务每 10 分钟运行一次，在 access 或 error 日志超过 **64 MiB** 时进行截断；每日清理现在两者都会清理。
- Docker：证书自动续期已修复（crond 会启动，acme.sh 状态保存在卷中）。

---

根据面板源文件分析整理。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

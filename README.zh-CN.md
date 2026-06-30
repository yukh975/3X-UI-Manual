# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 简体中文 · 🇹🇼 [繁體中文](README.zh-TW.md)

用于 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板的用户手册 — 一份为面板 **v3.4.2** 编写的综合使用指南。

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

## 3.4.2 新特性

3.4.2 是一次重大更新：WireGuard 改用多客户端模型，REALITY 新增了实时目标扫描器，负载均衡器获得了 Observatory / Burst Observatory 选项卡，并新增了对敏感设置以 2FA 代码进行确认。以下列出相对于 3.4.1 的变更，按手册章节分组。

### 第 1 节的更改 — 简介、系统要求与安装

- 侧边菜单（以及移动端抽屉）中新增了**「文档」**按钮（书本图标）——打开官方文档 `https://docs.sanaei.dev/`。
- 面板更新所允许的最低 Xray 版本已提升至 **26.6.27**（随附 Xray 核心 26.6.27）。

### 第 2 节的更改 — 登录面板与访问安全

- 启用 2FA 后，修改管理员登录名/密码以及关闭 2FA，现在都需要**输入身份验证器应用中的当前代码**（对敏感修改进行确认）。
- LDAP：新增**「跳过 TLS 证书校验」**开关（`ldapInsecureSkipVerify`）——在 LDAPS 下禁用证书校验；仅在启用「使用 TLS（LDAPS）」时可用。

### 第 3 节的更改 — 概览 / 仪表盘

- 面板版本按钮现在始终打开更新窗口（参见第 16 节——dev 渠道）。
- 全面的**可访问性**改进：图标按钮的 aria 标签，以及通过 Enter/Space 激活元素（面向屏幕阅读器和键盘导航）。

### 第 4 节的更改 — Inbounds：创建与通用参数

- **「导出所有链接」**操作现在通过订阅引擎生成链接——为每个客户端套用备注模板，并优先使用受管 Host 端点（此前为固定备注 `inbound-email`）。

### 第 5 节的更改 — 协议

- **WireGuard 改用多客户端模型。** peer 现在是普通客户端（隧道内地址自动分配，支持订阅、流量/有效期限制和分组）；inbound 表单中内联的「Peer」列表已移除。
- WireGuard inbound 新增可配置的 **DNS** 字段（默认 `1.1.1.1, 1.0.0.1`）以及**客户端配置卡片**——可复制/下载/扫码完整的 `.conf` 以及 `wireguard://`/`wg://` 链接。

### 第 6 节的更改 — 传输（Stream Settings）

- 对于新建的 XHTTP inbound，**xmux** 中的 `maxConnections` 参数默认值现为 **6**（原为 `0`——不限制）。已有 inbound 保留其原值。

### 第 7 节的更改 — 连接安全：TLS、XTLS 与 REALITY

- 新增 **REALITY 实时目标扫描器**：**「扫描」**按钮（「实时」检查当前目标）和**「查找目标」**按钮（扫描某个域名或 **IP/CIDR** 范围，并根据证书挑选可用目标）。首次选择 REALITY 时，「目标」和 SNI 字段现在为空。

### 第 8 节的更改 — 客户端

- 通过 `bulkAdjust` 续期有效期/配额现在会**自动启用**仅因耗尽（有效期到期或配额超限）而被禁用的客户端——前提是续期使其重新回到限制范围内。手动禁用或仍处于耗尽状态的客户端保持禁用。

### 第 9 节的更改 — 客户端分组

- 分组的**「重置流量」**现在仅清零**分组自身的计数器**；各个客户端的计数器、配额和状态均不受影响，无需重启 Xray。这是相对于以往行为的变更（此前会重置分组内所有客户端的流量）。

### 第 10 节的更改 — 订阅（Subscription）

- 在**受管主机**中，**VLESS route** 字段已重新定义：现为单个值 `0-65535`（而非端口列表），并会真正「嵌入」到每个订阅 UUID 中（raw/JSON/Clash）。
- 备注模板中的 `{{EMAIL}}` 变量（及其同义词 `{{USERNAME}}`）现在仅在客户端的**第一条链接**上输出——与流量/有效期块一样。

### 第 11 节的更改 — Xray：路由、outbounds、DNS 与扩展

- **负载均衡器**：页面拆分为**「均衡器设置」**和**「Observatory」**两个选项卡；以 Observatory 和 Burst Observatory 表单取代原始 JSON（Burst 新增**「HTTP 方法」**字段）。带 `fallbackTag` 的 Random/Round-robin 均衡器现在会自动创建 Burst Observatory。
- 删除 outbound 或负载均衡器时，面板会自动清理路由中的相关引用，并在确认对话框中显示**影响预览**。
- 路由规则中的网络条件 **L4** 在配置中以小写写入（`tcp`/`udp`），而在表格中以大写显示。
- 负载均衡器添加/编辑表单中的错误现在会延迟到首次触碰字段或尝试保存时才提示。

### 第 12 节的更改 — 节点（多面板，master/slave）

- 「已本地保存，节点离线——稍后同步」提示现在仅在节点确实离线或已关闭时显示（此前在每次保存到在线节点时都会出现）。

### 第 16 节的更改 — 运维：备份、日志、更新、CLI

- 备份文件名现在包含服务器地址和**日期时间**：`{host}_YYYY-MM-DD_HHMMSS.db`（PostgreSQL 为 `.dump`），例如 `panel.example.com_2026-06-27_000000.db`——无论是从面板下载，还是 Telegram 机器人发送的备份都是如此。
- 现在可以从稳定版构建启用**dev 渠道**更新：版本按钮始终打开更新窗口，新增**「Dev 渠道」**开关，并附有关于不稳定和无自动回滚的警告。

---

根据面板源文件分析整理。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

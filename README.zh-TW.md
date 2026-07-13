# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 繁體中文

使用者手冊，適用於 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板——為面板 **v3.5.0** 撰寫的完整使用指南。

> **唯讀鏡像。** 此 GitHub 儲存庫為單向鏡像——手冊原始檔存放於私有 GitLab，並自動推送至此，因此內容始終保持最新。發現錯誤或不準確之處？請[提交 Issue](https://github.com/yukh975/3X-UI-Manual/issues)。**不接受 Pull Request**（將自動關閉）——修正須在原始來源處進行。

## 目錄

| 檔案 | 語言 | 格式 |
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

## 3.5.0 新功能

3.5.0 是一次重大更新：MTProto 改採多客戶端模式（mtg-multi 引擎、個人 secret、配額與 ad-tag），受管主機改為群組式（一筆記錄可含多個 inbound 與多個地址），PostgreSQL 面板的還原功能可接受 SQLite 備份，outbound 新增「Target Strategy」、「Real delay」測試與 Egress/Country 欄位，負載均衡器可將另一個負載均衡器用作 fallback。隨附 Xray 核心 26.7.11。以下列出相對於 3.4.2 的變更，依手冊章節分組整理。

### 第 1 節的變更 — 簡介、需求與安裝

- Xray 核心更新至 **26.7.11**。隨附的自動遷移：Shadowsocks 的 `none`/`plain` 與 VMess 的 `none`/`zero` 加密方式已從核心移除（已儲存的設定會自動改寫），指向公網地址的未加密 VLESS/Trojan outbound 在儲存時會被拒絕。
- 新增 **`x-ui pgclient [版本]`** 指令與 PostgreSQL 選單中的 **10. Install/Upgrade client tools (pg_dump/pg_restore)** 項目——安裝／更新 PostgreSQL 客戶端工具。
- 腳本修正：RHEL 系上的 PostgreSQL 與 fail2ban 安裝（EPEL）、Arch 不再執行完整的 `pacman -Syu`、32 位元 ARM 上 Xray 二進位檔名稱正確（`xray-linux-arm32`）、簽發 IP 憑證前確認自動偵測的 IPv4、修正選擇預設 ACME 連接埠時誤報「Your input is invalid」的問題。

### 第 2 節的變更 — 登入面板與存取安全

- IP 限制：「死」連線現在只會被封鎖**一次**，而非每次 10 秒掃描都觸發——fail2ban 計數器不再虛增，也無需調高 `maxretry`。

### 第 4 節的變更 — Inbounds：建立與通用參數

- Inbound 清單新增**搜尋**功能（依備註、連接埠與協定），節點下拉選單（「Deploy to」、「節點」篩選器）也支援輸入搜尋。

### 第 5 節的變更 — 協議

- **MTProto 改採多客戶端模式**（mtg-multi 引擎）：MTProto 使用者現在是一般客戶端，擁有自己的 secret、配額、有效期、ad-tag 和個人 `tg://proxy` 連結。inbound 層級的「Secret」欄位已移除（既有 inbound 會自動轉換），「FakeTLS domain」成為新 secret 的預設域名。新的 inbound 欄位：**Max connections**（連線數限制）、**Public IPv4/IPv6**（用於 ad-tag middle proxy）。客戶端變更「即時」套用，不會中斷其他人的 Telegram 工作階段。
- WireGuard：inbound 選單獲得完整的客戶端操作集（Export All URLs、繫結/解除繫結、群組），匯出視窗拆分為 **Config** 與 **Links** 兩個分頁，**「WireGuard 允許的 IP」欄位改為可編輯**（多筆記錄以逗號分隔），節點 inbound 的客戶端設定中 `Endpoint` 現在指向節點地址。

### 第 7 節的變更 — 連線安全性：TLS、XTLS 與 REALITY

- **Finalmask + REALITY 組合在儲存時會被拒絕**（它會導致 Xray-core 在首次連線時崩潰）；minClientVer 的輸入提示更新為 26.3.27。
- 新的 Finalmask TCP 遮罩類型——**XMC（Minecraft）**：將流量偽裝成 Minecraft 流量（Hostname、Usernames、必填的 Password 且支援自動生成）。

### 第 8 節的變更 — 客戶端

- 新增**「速度」**欄位——每個客戶端的即時速度（↑/↓，約 5 秒滑動平均）。
- 客戶端搜尋再次支援 **Telegram ID**；客戶端表單中已停用的 inbound 從綁定清單中隱藏；修正「解綁」視窗中重複項目累積的問題。
- MTProto 客戶端擁有專屬欄位：**「MTProto secret」**（可重新生成）與 **「Ad-tag（贊助頻道）」**（32 個 hex 字元）；配額與有效期現在對 MTProto 實際生效。

### 第 9 節的變更 — 客戶端群組

- 客戶端資訊視窗現在會顯示其**群組**。

### 第 10 節的變更 — 訂閱（Subscription）

- **受管主機改為群組式**：一筆記錄可涵蓋**多個 inbound**（多重選取）與**多個地址**（標籤式輸入，每筆記錄可帶自己的 `:連接埠`；地址自動完成；空白——繼承 inbound 地址）。清單欄位以標籤顯示地址與 inbound（帶「+N」），操作與 API 以群組（`groupId`）為單位運作，並新增批量端點 `POST /panel/api/hosts/bulk/add`。主機排序現在是全域的（先依順序，再依備註）。
- **公告**文字（`subAnnounce`）現在會以橫幅顯示在訂閱資訊頁面上；自訂範本可使用 `announce` 變數。
- 資訊頁面現在也可透過 **JSON/Clash 連結**在瀏覽器中開啟（不再僅限主連結）。
- 主機設定 **Final Mask** 與 **Allow insecure** 現在分別也對 raw 連結（`fm=`）和 **Hysteria2**（`insecure=1` / `skip-cert-verify: true`）生效。
- 「訂閱更新間隔」（`subUpdates`）範圍修正為 **0–525600**（先前的介面上限 168 會在從 2.x 升級後阻擋設定儲存）。
- 原生 **WireGuard 客戶端現在會納入 Clash 與 JSON 訂閱**（先前僅 raw）。

### 第 11 節的變更 — Xray：路由、outbounds、DNS 與擴充功能

- Outbound 編輯器：新增 **「Target Strategy」** 欄位（從 `AsIs` 到 `ForceIPv4` 共 11 個值）、**「Real delay」** 測試模式（含隧道建立的完整時間；HTTP 模式現在以「暖」連線測量），以及 HTTP/Real 測試後的 **Egress**（出口 IP，隱藏於「眼睛」圖示後）與 **Country**（旗幟 + 國家，WARP 標記）欄位。
- **負載均衡器的 Fallback 可指向另一個負載均衡器**：面板會自行建立隱藏的 loopback 物件（`_bl_…`），並防範循環依賴與刪除使用中的負載均衡器；`_bl_` 前綴為保留字。
- 「基本路由」分頁新增 **「Default Outbound」** 選擇器——決定未匹配任何規則的流量由哪個 outbound 處理（所選項目會移至首位）。
- 私有 IP 上的 DNS 伺服器不再被 `geoip:private` 規則封鎖——面板會自行維護受管的放行規則。
- Dial 設定（sockopt）中的 Happy Eyeballs 現在會確實啟用；「Try delay」預設為 250 毫秒，明確設定的 0 會被保留。
- Outbound 訂閱匯入：帶 `?plugin=`／結尾 `/` 的 `ss://` 連結現在能正確解析連接埠。

### 第 12 節的變更 — 節點（多面板，master/slave）

- 修正合集：未變更的客戶端儲存不再中斷節點 inbound 的即時流量；節點的 Host 覆寫在首次接受時會匯入主面板；自動續期會開啟新的配額週期；在主面板刪除客戶端會在節點上完整刪除；節點的 inbound 在首次接受前不會被清除；單一異常 inbound 不會中止節點流量同步；連接埠衝突檢查僅限於自身節點。

### 第 14 節的變更 — Telegram 機器人

- 機器人指令選單新增 **`/usage`**、**`/inbound`**、**`/restart`**，以及新的管理員指令 **`/clearall`**（重設所有客戶端的流量，需確認）。
- 線上客戶端清單以 `email - inbound 備註` 標示；備份與封鎖日誌訊息包含主機名稱；依 Telegram ID 搜尋不受設定格式影響。

### 第 16 節的變更 — 日常運維：備份、日誌、更新、CLI

- **PostgreSQL 面板的還原功能可接受 SQLite 檔案**：一般 `.db` 備份或遷移用 `.dump` 可直接匯入 PostgreSQL（單一交易，並在停止 Xray 前先行檢查）。檔案選擇對話框在兩種資料庫上均接受 `.dump,.db`；「下載遷移檔案」僅保留於 PostgreSQL 面板。
- 還原 `pg_dump` 封存檔前，面板會檢查轉儲的可讀性，版本不符時會提示確切的 `x-ui pgclient <版本>` 指令。
- 啟動時自動修復：溢位的流量計數器會被箝制並復原；移除 inbound 連接埠上過時的 UNIQUE 限制（它妨礙 multi-node）。
- Xray 日誌：新的任務每 10 分鐘檢查一次，當 access 或 error 日誌超過 **64 MiB** 時將其截斷；每日清理現在會同時清理兩者。
- Docker：憑證自動續期已修復（crond 會啟動，acme.sh 狀態保存在磁碟區中）。

---

根據面板原始檔分析整理而成。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

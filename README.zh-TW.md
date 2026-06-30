# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 繁體中文

使用者手冊，適用於 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板——為面板 **v3.4.2** 撰寫的完整使用指南。

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

## 3.4.2 新功能

3.4.2 是一次重大更新：WireGuard 改採多用戶端模式，REALITY 新增即時目標掃描器，負載均衡器新增 Observatory／Burst Observatory 分頁，並為敏感設定加入 2FA 代碼確認。以下列出相對於 3.4.1 的變更，依手冊章節分組整理。

### 第 1 節的變更 — 簡介、需求與安裝

- 側邊選單（以及行動版抽屜）新增了 **「文件」** 按鈕（書本圖示）——開啟官方文件 `https://docs.sanaei.dev/`。
- 面板更新時可升級的最低 Xray 版本提升至 **26.6.27**（隨附 Xray 核心 26.6.27）。

### 第 2 節的變更 — 登入面板與存取安全

- 啟用 2FA 時，變更管理員登入名稱／密碼以及停用 2FA，現在都需要**輸入當前代碼**（驗證器應用程式中的代碼），以確認敏感變更。
- LDAP：新增 **「略過 TLS 憑證驗證」** 切換開關（`ldapInsecureSkipVerify`）——在 LDAPS 時停用憑證驗證；僅在已啟用「使用 TLS（LDAPS）」時可用。

### 第 3 節的變更 — 概覽 / 儀表板

- 面板版本按鈕現在永遠開啟更新視窗（詳見第 16 節——dev 頻道）。
- 全面提升**無障礙性**：圖示加上 aria 標籤，並可透過 Enter/Space 啟用元素（供螢幕報讀器與鍵盤導覽使用）。

### 第 4 節的變更 — Inbounds：建立與通用參數

- **「匯出所有連結」** 動作現在透過訂閱引擎生成連結——對每個用戶端套用備註範本，並優先使用受管的 Host 端點（先前使用固定備註 `inbound-email`）。

### 第 5 節的變更 — 協定

- **WireGuard 改採多用戶端模式。** Peer 現在是一般用戶端（在隧道中自動配發地址，支援訂閱、流量／時限限制與群組）；inbound 表單中內嵌的「Peer」清單已移除。
- WireGuard inbound 新增可設定的 **DNS** 欄位（預設 `1.1.1.1, 1.0.0.1`），以及**用戶端設定卡片**——可複製／下載／QR 完整 `.conf` 與 `wireguard://`／`wg://` 連結。

### 第 6 節的變更 — 傳輸（Stream Settings）

- XHTTP 新建 inbound 的 **xmux** 中 `maxConnections` 參數現在預設為 **6**（先前為 `0`——無限制）。既有 inbound 保留其原值。

### 第 7 節的變更 — 連線安全：TLS、XTLS 與 REALITY

- 新增 **REALITY 即時目標掃描器**：**「掃描」** 按鈕（「即時」驗證當前目標）與 **「尋找目標」** 按鈕（掃描網域或 **IP/CIDR** 範圍，並依其憑證挑選合適的目標）。首次選擇 REALITY 時，「目標」與 SNI 欄位現在為空。

### 第 8 節的變更 — 用戶端

- 透過 `bulkAdjust` 延長時限／配額時，現在會**自動啟用**僅因耗盡（已過期或超出配額）而被停用的用戶端，前提是延長後使其回到限制範圍內。手動停用或仍處於耗盡狀態的用戶端維持停用。

### 第 9 節的變更 — 用戶端群組

- 群組的 **「重設流量」** 現在僅將**群組本身的計數器**歸零；個別用戶端的計數器、配額與狀態不受影響，也無需重啟 Xray。此為相對於先前行為的變更（先前會重設群組中所有用戶端的流量）。

### 第 10 節的變更 — 訂閱（Subscription）

- **受管主機**中的 **VLESS route** 欄位已重新定義：現在是單一數值 `0-65535`（不再是連接埠清單），且會實際「嵌入」每份訂閱的 UUID 中（raw／JSON／Clash）。
- 備註範本中的 `{{EMAIL}}` 變數（及其同義詞 `{{USERNAME}}`）現在僅在用戶端的**第一個連結**上輸出——與流量／時限區塊相同。

### 第 11 節的變更 — Xray：路由、outbounds、DNS 與擴充功能

- **負載均衡器**：頁面拆分為 **「負載均衡器設定」** 與 **「Observatory」** 分頁；以 Observatory 和 Burst Observatory 表單取代原始 JSON（Burst 新增 **「HTTP 方法」** 欄位）。帶 `fallbackTag` 的 Random/Round-robin 負載均衡器現在會自動建立 Burst Observatory。
- 刪除 outbound 或負載均衡器時，面板會自動清除路由中相關的引用，並在確認對話框中顯示**影響預覽**。
- 路由規則中的網路條件 **L4** 在設定中以小寫寫入（`tcp`/`udp`），在表格中以大寫顯示。
- 新增/編輯負載均衡器表單中的錯誤現在會延後至首次接觸欄位或嘗試儲存時才顯示。

### 第 12 節的變更 — 節點（多面板，master/slave）

- 「已在本機儲存，節點離線——稍後同步」的通知現在僅在節點確實離線或關閉時才顯示（先前每次在線上節點儲存時都會出現）。

### 第 16 節的變更 — 日常維運：備份、日誌、更新、CLI

- 備份檔案名稱現在包含伺服器位址與**日期時間**：`{host}_YYYY-MM-DD_HHMMSS.db`（PostgreSQL 為 `.dump`），例如 `panel.example.com_2026-06-27_000000.db`——從面板下載時與 Telegram 機器人傳送的備份皆是如此。
- 現在可從穩定版本啟用更新的 **dev 頻道**：版本按鈕永遠開啟更新視窗，並新增 **「Dev 頻道」** 切換開關，附有不穩定且無自動回退的警告。

---

根據面板原始檔分析整理而成。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

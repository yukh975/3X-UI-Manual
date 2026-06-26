# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 繁體中文

使用者手冊，適用於 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板——為面板 **v3.4.1** 撰寫的完整使用指南。

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

## 3.4.1 新功能

本節簡要列出 **3.4.1** 相對於 3.4.0 中使用者可見的變更，依手冊章節分組整理。各功能的詳細說明請見下方對應章節。

### 第 1 節的變更 — 簡介、需求與安裝
- **透過 install.sh 安裝 dev 版本與指定版本** — 安裝腳本 install.sh 現在支援指定版本引數：填入標籤（例如 v3.4.0）可安裝特定版本，或填入 'dev-latest'（別名 'dev'）以略過最低版本檢查，安裝追蹤 main 分支最新提交的滾動 dev 版本。不填引數則安裝最新穩定版本。

### 第 3 節的變更 — 概覽 / 儀表板
- **儀表板：重新設計系統歷史圖表與 Xray 指標圖表的時間範圍選擇** — 儀表板歷史視窗的時間範圍選擇器已更新。系統指標圖表可選範圍為 2m、1h、3h、6h、12h、24h、2d 及 7d（歷史資料現可保存最多 7 天，取代先前的 48 小時），在 2 天和 7 天的範圍下，時間標籤會額外顯示日期。Xray 指標圖表可選範圍為 2m、1h、3h、6h 及 12h。不規則的 30m、2h、5h 選項已移除。
- **儀表板：記憶體使用卡片顯示程序真實 RSS** — 儀表板上面板的記憶體使用量指標現在反映程序的真實 RSS，與作業系統顯示的數值一致。先前顯示的是 Go 內部計數器，其數值會偏高且從不下降。現在記憶體釋放後數值也會隨之降低。

### 第 5 節的變更 — 協定
- **VLESS 加密：新的金鑰生成模式（native / xorpub / random）** — 在 VLESS 協定的 inbound 中，加密金鑰生成區塊已重新設計。原本在「解密」和「加密」欄位下方的兩個獨立按鈕（X25519 和 ML-KEM-768）已被一個「金鑰生成」下拉選單取代，提供六個選項：X25519 和 ML-KEM-768，每種各有 native、xorpub 和 random 三種模式。選擇所需模式後點擊「生成」，面板將自動填入 decryption 和 encryption 欄位的金鑰對。「清除」按鈕可移除已生成的值，「已選」行顯示目前的金鑰類型與模式。
- **清空 tunnel inbound 設定中的 Rewrite port 欄位不再導致儲存失敗** — 已修復一個錯誤：在 tunnel 協定的 inbound 中清空「Rewrite port」（重寫埠號）欄位不再導致儲存錯誤。先前空值會觸發驗證錯誤訊息；現在清空後該欄位會直接從設定中排除。

### 第 7 節的變更 — 連線安全：TLS、XTLS 與 REALITY
- **在現有 inbound 上啟用加密時恢復 XTLS Vision flow** — 若在已有用戶端的 VLESS/XHTTP inbound 上啟用加密（decryption/encryption），面板現在會自動為符合條件的用戶端恢復 flow=xtls-rprx-vision。先前在此情況下，flow 會在設定、連結和訂閱中靜默消失（尤其是在節點 inbound 上）。無需任何手動操作——修復在編輯 inbound 時自動套用，並在面板更新時執行一次。

### 第 8 節的變更 — 用戶端
- **批次啟用與停用選定用戶端** — 在「Clients」頁面選取多個用戶端後，「More（更多）」選單中提供批次 Enable（啟用）和 Disable（停用）操作。啟用會在所有綁定的 inbounds 上啟用每個選定的用戶端；流量配額耗盡或已過期的用戶端將自動再次停用。停用會立即撤銷用戶端的存取權限，但記錄和累計流量資料會保留。執行前面板會要求確認，操作完成後顯示已處理用戶端數量的通知，若有失敗也會顯示相應數量。
- **在 Adjust 對話框中批次設定 XTLS flow** — 批次調整對話框 Adjust 新增了「Set flow」欄位，可一次為所有選定的用戶端設定或清除 XTLS flow。預設選項為 No change（不變更）。Disable（clear flow）選項會清除 flow；xtls-rprx-vision 和 xtls-rprx-vision-udp443 則設定對應的 vision-flow。設定 vision-flow 僅套用於支援 flow 的 inbounds；不符合的 inbounds 保持不變並標記為已跳過，而清除 flow 則始終允許。現在只需設定天數、流量或 flow 三項之一即可套用對話框。
- **重新命名用戶端不再破壞綁定關係，並移除重複的儲存提示** — 已修復編輯用戶端時的行為：重新命名用戶端（變更其 email）不再在儲存 inbounds 綁定和外部連結時造成錯誤——這些操作現在會使用新的 email。此外，儲存用戶端時成功更新的通知不再重複顯示。

### 第 10 節的變更 — 訂閱（Subscription）
- **Remark Template 新增「Connection」變數群組：{{PROTOCOL}}、{{TRANSPORT}}、{{SECURITY}}** — 備註範本（Remark Template）的變數集新增了「Connection（連線）」群組，包含三個描述 inbound 設定的變數：{{PROTOCOL}} — 協定（VLESS、VMess、Trojan 等），{{TRANSPORT}} — 傳輸網路（tcp、ws、grpc 等），以及 {{SECURITY}} — 傳輸安全（TLS、REALITY、NONE，以大寫顯示）。與流量和時限變數一樣，這三個變數僅在訂閱正文中有效，在面板顯示的連結和訂閱資訊頁面的備註中會自動移除。
- **預設備註範本現在包含 {{EMAIL}}；用戶端 email 重新出現在面板連結備註中** — 預設備註範本已更改，現在包含用戶端 email——{{INBOUND}}-{{EMAIL}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D（先前不含 email）。此外，已修復 3.4.0 版本的行為：在面板顯示的連結（「Clients」頁面的 QR 碼和「Info」視窗）及訂閱資訊頁面上，用戶端 email 再次出現在設定檔名稱中——有設定主機時為「inbound-host-email」，無主機時為「inbound-email」。流量和時限資訊不會填入這些顯示名稱。
- **Incy 用戶端整合：快速匯入按鈕與含路由設定的 Incy 分頁** — 訂閱資訊頁面的應用程式選單（Android 和 iOS）新增了「Incy」項目——點擊後會開啟 deep-link incy://add/<訂閱連結> 以快速將訂閱匯入 Incy 用戶端。訂閱設定中新增了「Incy」分頁，包含「Enable routing（啟用路由）」開關和格式為 incy://routing/onadd/<base64> 的「Routing rules（路由規則）」欄位。啟用路由且欄位已填寫時，此字串會作為獨立一行附加至訂閱正文（raw 格式），將路由設定檔傳遞給 Incy 用戶端。這些設定僅對 Incy 用戶端有效。
- **修復孤立流量記錄用戶端的 {{TRAFFIC_USED}} 計算** — 修復了 {{TRAFFIC_USED}}（及其他流量統計變數）在備註中的計算問題，適用於刪除並重新建立 inbound 後流量記錄「孤立」的用戶端。先前此類用戶端的 {{TRAFFIC_USED}} 顯示 0.00B，而訂閱資訊頁面的標題中流量卻顯示正確。現在面板會額外依用戶端 email 搜尋統計資料，變數再次顯示正確的已用流量。
- **「Hosts」頁面的瀏覽器分頁標題現在正確顯示** — Hosts 頁面現在正確顯示瀏覽器分頁標題，不再顯示通用的「3X-UI」。此為純外觀變更，僅影響分頁標籤。

### 第 11 節的變更 — Xray：路由、outbounds、DNS 與擴充功能
- **Dialer Proxy 下拉選單現在列出訂閱 outbounds** — outbound 表單 Sockopt 區段的「Dialer Proxy」下拉選單（代理鏈：透過另一個 outbound 的標籤路由此 outbound）現在不僅顯示本地 outbounds，還顯示來自訂閱的 outbound 標籤。blackhole outbound 和正在編輯的 outbound 本身仍從清單中排除。留空則為直接連線。
- **HTTP outbound：自訂請求標頭已保留（且可編輯）** — HTTP 協定的 outbound 表單新增了「Headers（標頭）」欄位——用於編輯發送至上游 HTTP 代理的 CONNECT 請求標頭鍵值對。先前這些標頭在重新儲存 outbound 時會遺失；現在已能正確保存。注意：僅套用設定層級的標頭，xray-core 會忽略個別伺服器層級的標頭。

### 第 12 節的變更 — 節點（多面板，master/slave）
- **更新節點時的 Dev 頻道選項** — 節點更新確認對話框新增了「更新至開發頻道（最新提交）」核取方塊。勾選後，選定節點將安裝 dev-latest 滾動版本而非穩定版本；未勾選時節點按其正常頻道更新。核取方塊下方顯示 dev 版本不穩定的警告。
- **首次從節點同步 inbound 時匯入用戶端流量歷史** — 修復了新增已累計流量的節點時的流量計算問題。先前首次從節點同步 inbound 時，inbound 的總計數器會正確轉移，但個別用戶端的計數器會歸零，導致主節點低估連接節點前的用戶端使用量。現在匯入 inbound 連同節點時，用戶端計數器會繼承節點上的實際數值。

### 第 14 節的變更 — Telegram 機器人
- **儲存設定時重新載入 Telegram 機器人** — Telegram 機器人的設定變更現在會在儲存時立即生效，無需重啟面板。如果您變更了令牌、chat ID、API 伺服器地址，或啟用/停用機器人，面板會自動以新參數重啟機器人。先前關於變更令牌後需重啟面板的規定已不再適用。
- **Telegram 機器人備份檔案名稱依 webDomain/IP 命名** — Telegram 機器人發送的資料庫備份檔案現在以伺服器地址命名：優先使用 webDomain，若未設定則使用公共 IP。先前未設定 webDomain 時，此類備份會使用通用名稱 x-ui，難以辨識備份來自哪台伺服器。

### 第 16 節的變更 — 日常維運：備份、日誌、更新、CLI
- **隧道健康監控器（透過環境變數自動重啟 xray）** — 3.4.1 新增了可選的隧道健康監控器。啟用後，面板會定期檢查指定 URL 的可達性，在連續多次檢查失敗後自動重啟 xray 核心——有助於恢復停止通行流量的隧道。監控器僅透過服務環境變數設定（網頁介面中無設定選項），預設停用。關鍵變數 XUI_TUNNEL_HEALTH_MONITOR=true 可啟用監控器；XUI_TUNNEL_HEALTH_PROXY 應指向本地 xray inbound（例如 socks5://127.0.0.1:1080），否則只會檢查伺服器本身的網路連通性而非隧道。其他變數可設定檢查 URL（XUI_TUNNEL_HEALTH_URL）、間隔（XUI_TUNNEL_HEALTH_INTERVAL，30s）、逾時（XUI_TUNNEL_HEALTH_TIMEOUT，10s）、重啟前的失敗次數（XUI_TUNNEL_HEALTH_FAILURES，3）以及重啟之間的最短間隔（XUI_TUNNEL_HEALTH_COOLDOWN，5m）。注意：重啟 xray 會中斷所有已連線用戶端的連線。
- **日誌檢視器中的自動更新** — 日誌檢視視窗（Xray 的「存取日誌」和面板的一般「日誌」）新增了「自動更新」核取方塊。啟用後，日誌每 5 秒自動重新讀取，並保留所選的行數、級別和篩選條件。視窗關閉或核取方塊取消勾選時，輪詢即停止。
- **面板的 Dev 更新頻道（依提交的滾動版本）** — 此切換開關僅在 dev 版本（依個別提交的 CI 版本）上顯示於面板更新視窗中。啟用後，面板將更新至 dev-latest 滾動版本，該版本追蹤 main 分支的每次提交且非穩定版本；無自動回退。在 dev 模式下，更新視窗顯示當前和最新提交而非版本號。此功能僅在使用 systemd 的 Linux 上可用。
- **x-ui 選單中的 Dev 頻道更新選項與 x-ui update-dev 指令** — x-ui 管理腳本選單新增了「更新至開發頻道（最新提交）」項目，確認後安裝 dev-latest 滾動版本；同時新增了 'x-ui update-dev' 指令。因此選單項目已重新編號：共計 28 個項目，選項輸入範圍為 0-28。若手冊中提及選單項目編號，請重新核對。
- **解除安裝面板時刪除 PostgreSQL** — 解除安裝面板時，若面板使用 PostgreSQL，腳本現在會額外詢問是否一併刪除 PostgreSQL 伺服器及其所有資料庫。此請求需要明確確認（預設為拒絕），並附有警告：刪除將影響機器上的所有 PostgreSQL 資料庫，包括其他應用程式的資料庫，且操作不可逆。拒絕時 PostgreSQL 及其資料將保留。
- **Xray 存取日誌檢視器重新命名為「存取日誌」** — Xray 存取日誌檢視器及 Xray 狀態卡片上的呼叫按鈕現在命名為「存取日誌」（先前僅稱「日誌」）。此更改是為了避免與面板的一般日誌檢視器混淆。
- **日誌行數選擇：新增 1000，移除 10** — 兩個日誌視窗中的行數選擇清單已更改：移除了 10，新增了 1000。現在可選擇 20、50、100、500 或 1000 行。
- **介面、機器人和 CLI 中的 dev 版本識別符（dev+<提交>）** — 在 dev 版本上，面板以「dev+<提交>」格式顯示其版本，取代穩定版本號——出現在側邊欄徽章、儀表板、更新視窗、Telegram 機器人報告以及「x-ui -v」的輸出中。穩定版本的版本顯示格式不變。
- **日誌檢視器：簡單通知完整顯示，不再被誤解析為日期格式** — 面板日誌檢視器現在能正確顯示不含時間戳和級別的簡單通知（例如系統訊息「Syslog is not supported」）——完整呈現文字，不再截斷。先前此類行會被錯誤解析為含日期和級別的日誌記錄，導致部分文字遺失。

---

根據面板原始檔分析整理而成。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

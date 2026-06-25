# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 繁體中文

使用者手冊，適用於 [3x-ui](https://github.com/MHSanaei/3x-ui) 面板——為面板 **v3.4.0** 撰寫的完整使用指南。

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

## 3.4.0 的新功能

本節簡要列舉 **3.4.0** 版本相對於 3.3.1 對面板使用者可見的變更，並依手冊各章節分組。每項功能的細節請見下方對應章節。

### 3. 概覽 / 儀表板
- **系統指標歷史：新增聚合間隔 12h/24h/48h** — 在系統指標歷史視窗中，平均間隔新增了 12h、24h 與 48h 三個值——現在圖表（CPU、RAM、流量、封包、連線、磁碟、在線、負載）可檢視長達兩天的期間。

### 4. Inbounds：建立與通用參數
- **Inbound：與保留的 Xray API 埠號衝突的警告** — 在建立或修改 inbound 時，面板現在不允許佔用內部 Xray API 的保留埠號（在 127.0.0.1 上預設為 62789）：在 loopback 上該埠號的本機 TCP inbound 會以埠號衝突錯誤被拒絕。在節點（nodes）上此限制不生效——它們有自己的 Xray。
- **Tunnel/TProxy：接受不含 security 鍵的 streamSettings** — streamSettings 中不含 security 區塊的 tunnel/TProxy 類型 inbound，現在可在不出現驗證錯誤的情況下開啟並儲存。
- **Inbounds：清單中新增 Speed（即時速度）欄** — inbounds 清單中出現了 Speed 欄，顯示每個 inbound 目前的流量速度（上行/下行）。

### 5. 協定
- **Shadowsocks-2022：在切換為金鑰大小不同的方法時重新產生客戶端 PSK** — 對於 Shadowsocks-2022：當將加密方法切換為金鑰大小不同的方法（例如在 aes-256 與 aes-128 之間）時，儲存 inbound 時客戶端 PSK 現在會自動依新長度重新產生。後果：受影響的客戶端需要重新取得訂閱（舊連結將失效）。
- **WireGuard：移除 workers 欄位** — 從 WireGuard 表單（inbound 與 outbound）中移除了 workers 欄位：xray-core v26.6.22 不再使用它。先前儲存的設定無需變更即可運作——該欄位只是被忽略。
- **VLESS+XHTTP：連結與訂閱中的 xtls-rprx-vision 流控** — 對於 XHTTP 之上的 VLESS，xtls-rprx-vision 流控現在能正確進入連結與訂閱（包含 XHTTP+REALITY 以及 Clash/Mihomo 格式）。先前面板會儲存 flow，但客戶端取得的設定不含 vision。

### 6. 傳輸（Stream Settings）
- **XHTTP：sessionID 欄位重新命名 + Session ID Table / Length** — 在 XHTTP 傳輸中，工作階段欄位已重新命名：Session ID Placement 與 Session ID Key（先前為 Session Placement / Session Key）。新增了兩個參數。Session ID Table——用於產生工作階段識別碼的字元集：可選擇預先定義的（ALPHABET、Base62、hex、number 等）或輸入任意 ASCII 字串；留空則為 xray-core 的預設值。Session ID Length——所產生識別碼的長度或範圍（例如 8-16）；僅在設定了 Session ID Table 時才生效，最小值必須大於 0。舊的已儲存 inbound 會自動遷移。
- **Inbound：用於辨識 CDN/中繼後方真實 IP 的 Real client IP 預設組合** — 在 inbound 的通訊端設定（sockopt）中出現了 Real client IP 選項——當流量經由 CDN 或中繼到達時（否則記錄的是中介者位址），用於辨識訪客真實 IP 的預設組合。提供三個選項：Off / direct（不處理）、Cloudflare CDN（信任 X-Forwarded-For）與 L4 relay / Spectrum (PROXY)（接受 PROXY 協定標頭）。各預設組合互斥，並會在所選傳輸不支援時提出警告。這些欄位絕不會在訂閱中發送給客戶端。
- **gRPC：現在會採用 Trusted X-Forwarded-For 標頭** — Trusted X-Forwarded-For 標頭現在在 gRPC 傳輸上也會被採用（先前——僅 WebSocket、HTTPUpgrade 與 XHTTP）。對於 gRPC inbound，面板不再顯示標頭不受支援的警告。

### 7. 連線安全：TLS、XTLS 與 REALITY
- **TLS：新欄位 Verify Peer Cert By Name、Curve Preferences、Master Key Log、ECH Sockopt** — Verify Peer Cert By Name——客戶端據以驗證伺服器憑證的名稱（以逗號分隔），用於取代 SNI；是已移除的 allowInsecure 的現代替代方案，會在連結與訂閱中傳遞，但不寫入伺服器。Curve Preferences——限制並排序 TLS 金鑰交換曲線（例如 X25519MLKEM768、X25519）；留空則為預設值。Master Key Log——寫入 TLS 金鑰的路徑（SSLKEYLOGFILE 格式），用於在 Wireshark 中除錯；正式環境請留空。ECH Sockopt——用於取得 ECH 設定的通訊端參數（dialerProxy、Domain Strategy、TCP Fast Open、Multipath TCP）。
- **REALITY：fallback 速率限制（Limit Fallback）與 Master Key Log** — 針對每個方向（Upload 與 Download）可設定：After Bytes——在開始限制前以全速放行多少位元組（0——從第一個位元組起即限制）；Bytes Per Sec——fallback 流量的速度上限，以防探針把伺服器當作免費通道使用（0——不限制，停用該方向）；Burst Bytes Per Sec——用於短暫突發的餘量。此外還新增了 Master Key Log 欄位（SSLKEYLOGFILE 檔案路徑，用於除錯）。
- **TLS：從 inbound 憑證及依 SNI 填入 Pinned Peer Cert SHA-256 的按鈕** — Pinned Peer Cert SHA-256 欄位旁現在有兩個自動填入按鈕，取代了先前的隨機雜湊按鈕。第一個填入 inbound 本身憑證的 SHA-256。第二個透過依指定 SNI 進行 TLS 連線取得伺服器即時憑證的雜湊（serverName 必須已填寫）。所取得的雜湊會加入該欄位（以逗號分隔），並進入連結，供客戶端釘選憑證。
- **TLS：新 inbound 憑證的 OCSP-stapling 預設關閉** — 對於新的 inbound，OCSP stapling 預設關閉（間隔為 0）。這可消除沒有 OCSP 回應者的憑證（例如 Let's Encrypt）在 xray 日誌中的錯誤。該欄位仍保留——可為支援 stapling 的憑證啟用它。
- **REALITY：相容 dest 欄位（target 的別名）** — 如果 REALITY inbound 是以 dest 欄位建立的（由舊版面板、透過 API 或外部工具），現在它能正確載入：dest 的值會填入 Target 欄位。先前 Target 會是空的，重新儲存會破壞 REALITY。

### 8. 客戶端
- **客戶端編輯器中的「Links」分頁（外部連結與訂閱）** — 在此分頁中，可用 **Add External Link** 按鈕新增第三方分享連結（`vless://`、`vmess://`、`trojan://`、`ss://`、`hysteria2://`、`wireguard://`），用 **Add External Subscription** 按鈕新增遠端訂閱的 URL。以上所有內容都會併入該客戶端的訂閱輸出（raw、JSON 與 Clash 格式）：連結原樣加入，遠端訂閱則由面板定期下載並將其設定與自身設定合併。
- **「IP 限制」欄位現在在無 Fail2ban 時會停用** — **IP 限制**欄位現在僅在已安裝且啟用 Fail2ban 時才有效。如果未安裝 Fail2ban（或系統為 Windows，或在伺服器上停用了該功能），客戶端編輯器的此欄位會被封鎖，將游標懸停時會顯示提示，建議從 `x-ui` 的 bash 選單安裝 Fail2ban。在面板更新時，對於未安裝 Fail2ban 的伺服器上的客戶端，已儲存的 IP 限制會歸零，因為它在那裡本來就不會套用。
- **刪除未繫結客戶端、匯出與匯入客戶端** — **客戶端**頁面的**更多**選單中新增了三個操作。**匯出客戶端**會顯示所有客戶端的 JSON 清單（格式為 `{client, inboundIds}`），並附有複製與下載（`clients-export.json`）按鈕。**匯入客戶端**接受相同的 JSON：有繫結的客戶端會被重建並繫結到 inbound，無繫結的客戶端會以獨立記錄還原，而已存在的 email 不會被覆寫（它們會被標記為已略過）。**刪除未繫結客戶端**會刪除所有未繫結到任何 inbound 的客戶端，連同其流量、IP 記錄與外部連結一併刪除；此操作不可復原。
- **客戶端 IP 記錄：連線時間與節點名稱** — 在客戶端 IP 記錄中（「IP 限制」欄位旁的檢視按鈕，以及「客戶端資訊」卡片中），每筆記錄現在除了 IP 本身外，還包含最後存取時間與用於記錄該連線的節點標籤（`@ 節點名稱`）——在多面板設定中可看出客戶端是透過哪個節點連線的。
- **在單一編輯器中重設客戶端的群組標籤** — 現在如果在單一客戶端編輯器中清空**群組**欄位並儲存，群組標籤會正確被移除——先前客戶端可能在重新儲存之前繼續顯示在原群組下。
- **客戶端清單自動更新（背景輪詢）** — 客戶端清單現在會自動更新：面板每隔幾秒拉取最新頁面，因此新連線的客戶端與變更後的排序順序無需手動重新整理即會出現。

### 10. 訂閱（Subscription）
- **託管的 Hosts：按主機覆寫 subscription 連結** — 在 3.4.0 版本中新增了 Hosts 區段（側邊選單項目）。可為每個 inbound 設定一個或多個 Host 端點，它們會取代 inbound 本身的位址、埠號與 TLS 參數，填入 subscription 連結——這便於透過 CDN 或中繼分發流量。主機可設定 Remark 與描述、與 inbound 的繫結、Address（留空——繼承 inbound 位址）與 Port（0——繼承 inbound 埠號）、Security 參數（same/tls/none/reality），以及 Host header、Path、Mux、Sockopt、Final Mask、從訂閱格式中排除（raw/json/clash）與 Clash/mihomo 參數。主機在 inbound 內可排序並支援批次操作。
- **Remark Template 取代了 remark 模型建構器；變數 {{VAR}}** — 先前的設定檔名稱建構器（選擇 Inbound/Email/External Proxy 與分隔符號）已被「Remark Template」欄位取代。在其中您可寫入任意名稱格式，並用按鈕插入變數：客戶端識別（{{EMAIL}}、{{INBOUND}}、{{HOST}}、{{ID}}、{{SUB_ID}}、{{COMMENT}}、{{TELEGRAM_ID}}）、流量（{{TRAFFIC_USED}}、{{TRAFFIC_LEFT}}、{{TRAFFIC_TOTAL}}、{{UP}}、{{DOWN}}、{{USAGE_PERCENTAGE}}）與期限/狀態（{{DAYS_LEFT}}、{{TIME_LEFT}}、{{EXPIRE_DATE}}、{{JALALI_EXPIRE_DATE}}、{{STATUS}}、{{STATUS_EMOJI}}）。在產生訂閱時，變數會針對每個客戶端個別代入，並提供預覽。以「|」符號分隔的區段，若其值為無限制則會自動隱藏，而用量與期限資訊僅顯示在客戶端的第一個連結上。如果該欄位留空，則使用先前的 remark 模型。
- **每客戶端外部連結與遠端訂閱（Links 分頁）** — 在此可為個別客戶端附加第三方分享連結（Add External Link）與外部訂閱位址（Add External Subscription）——它們將被納入其自身訂閱（RAW、JSON 與 Clash 格式）。外部訂閱由面板下載並與客戶端設定合併。這便於在您的 inbound 之上為客戶端額外提供伺服器。
- **Happ：在客戶端中隱藏伺服器設定（Hide server settings）** — 在訂閱設定的 Happ 分頁中新增了「Hide server settings」開關。當它啟用時，Happ 客戶端中會隱藏檢視與變更伺服器參數的功能。此選項僅對 Happ 客戶端生效。
- **節點名稱不再附加到訂閱中的設定檔名稱** — 節點名稱（Node）不再加到訂閱中的設定檔名稱。在客戶端應用程式中只顯示管理員設定的 inbound remark，不含形如「@節點名稱」的內部後綴。
- **remark 模型標籤重新命名 Other → External Proxy（隨後被範本取代）** — 無需單獨記錄：remark 模型項目「Other」重新命名為「External Proxy」一事，已被改用新的 Remark Template 欄位所取代，其中 UI 的模型建構器已被移除。
- **訂閱連結正確性：SS2022、Shadowrocket、SIP002 obfs、Clash 中的 XHTTP** — 改善了所產生訂閱連結的相容性：修正了 SS2022 的編碼、Shadowrocket 的 deep-link、Shadowsocks+obfs 以 SIP002 格式（obfs-local 外掛）的輸出，以及 Clash/Mihomo 訂閱中完整的 XHTTP 欄位集。無需個別設定——連結只是能被客戶端更正確地辨識。
- **訂閱 remark 模型：項目「Other」重新命名為「External Proxy」** — 在訂閱設定的 remark 模型中，**「Other」**項目重新命名為**「External Proxy」**（來源——外部代理的 remark）。行為未變，現有設定仍相容。
- **訂閱：透過點擊晶片選擇 remark 變數（Remark variable picker）** — Remark Template 欄位旁提供了一組分組的變數晶片：點擊變數 {{VAR}} 會將其插入範本，懸停時會顯示描述。在 remark 與主機名稱欄位中也允許使用單花括號的簡寫——{DATA_LEFT}、{EXPIRE_DATE}、{PROTOCOL}、{TRANSPORT} 等；面板會自動將其轉換為內部格式 {{...}}。

### 11. Xray：路由、outbounds、DNS 與擴充功能
- **路由與 Outbounds 移至獨立的側邊選單項目** — 從此版本起，**「外送」（Outbounds）**與**「路由」（Routing）**移至獨立的側邊選單項目（緊接在「Hosts」下方），各有自己的位址——`/outbound` 與 `/routing`。先前路由是在「Xray 設定」子選單內開啟，而 outbounds 則作為 Xray 頁面的分頁。在「Xray 設定」子選單中現在只剩下：基本、負載平衡器、DNS 與進階範本。直接連到 `/outbound` 與 `/routing` 以及重新整理頁面均如預期運作。
- **路由規則可透過開關啟用與停用** — 個別路由規則現在可透過開關暫時**停用**，而不必刪除它。在規則表中有一個帶開關的**「啟用」**欄，規則表單中的「啟用」欄位也是開關。已停用的規則不會進入最終的 Xray 設定。統計用的服務規則（`api`）無法停用——其開關被封鎖。
- **路由規則與 outbounds 的匯出會在預覽的模態視窗中開啟** — 路由規則與外送的**「匯出」**按鈕現在不再立即下載檔案，而是開啟一個帶 JSON 預覽以及**「複製」**和**「下載」**按鈕的模態視窗。在「路由」分頁中，「匯入」與「匯出」收進了**「更多」**下拉選單（如同 Outbounds 分頁）。
- **測試所有外送現在也會檢查來自訂閱的 outbounds；direct/dns 不再被測試** — 「外送」頁面上的**「測試全部」**按鈕現在也會檢查從訂閱取得的 outbounds（「來自訂閱」表）——它們的列也會以結果高亮顯示。同時，`freedom`（「direct」）與 `dns` 兩種 outbounds 在任何模式下都不再被測試（它們不是代理）：它們的測試按鈕不可用，而「測試全部」會略過它們。
- **FinalMask：逐片段的 Lengths/Delays 陣列取代單一 Length/Delay** — 在 fragment 遮罩（FinalMask）中，單一的 Length 與 Delay 欄位被 Lengths 與 Delays 清單取代：可為每個片段分別設定長度範圍（例如 100-200）與以毫秒計的延遲（例如 10-20 或 0）。可新增與刪除列；先前儲存的值會自動轉移。
- **Loopback outbound：新增 Sniffing 區塊** — loopback 類型的 outbound 出現了 Sniffing 區塊，其參數與 inbound 相同：啟用、destOverride、Metadata Only、Route Only 與排除網域清單。
- **Hysteria2 / Salamander：Gecko 模式（packetSize）與 Realm 遮罩的 TLS** — 在 Hysteria2 的 UDP 遮罩（FinalMask）中擴充了功能。Salamander 遮罩新增了 Mode 選擇器：Gecko 模式會為封包加上隨機填充，並有 Min/Max 大小欄位（從 1 到 2048，預設 512-1200），以防範封包長度分析。Realm 遮罩出現了可選的 TLS Config 區塊：Server Name (SNI)、ALPN（h3/h2/http/1.1）、Fingerprint 與 Allow Insecure。
- **將分享連結匯入 outbound 時會保留 xmux 設定** — 從分享連結匯入 outbound 時，現在會保留多工器 **xmux**（XHTTP）的設定：先前它們會被無聲丟失。匯入後，這些值會填入 XMUX 子表單。
- **來自訂閱的 outbounds 標籤保留非 ASCII 字元（西里爾文）** — 從訂閱取得的 outbounds 標籤現在會保留非 ASCII 字元（例如西里爾文）並保持可讀，而不會被縮減為純數字。

### 12. 節點（多面板，master/slave）
- **節點：新的 TLS 檢查模式——Mutual TLS（客戶端憑證）** — 在節點表單中，TLS 檢查模式現在有四個選項：Verify（系統 CA）、Pin（依 SHA-256 釘選憑證）、Skip（不檢查）與新的 Mutual TLS（客戶端憑證）。在 Mutual TLS 模式下，面板會以由其自身 CA 簽發的客戶端憑證額外向節點證明自己；對於這類節點，API 權杖變為可選。要啟用 mTLS：在節點上設定 Mutual TLS 模式，從 Node mTLS 區段複製管理面板的 CA，在節點上將其設定為信任的上層 CA，並重新啟動節點。
- **節點：「Node mTLS」區段——複製面板 CA 與信任的上層 CA** — 在「節點」頁面新增了 Node mTLS 區段，用於設定面板之間的相互 TLS 驗證。「複製此面板的 CA」按鈕會將面板的根憑證複製到剪貼簿——需要將其傳給受管節點，這些節點將驗證面板的客戶端憑證。「信任的上層 CA」欄位用於面板本身即為節點的情況：在此貼上管理面板的 CA，以要求其客戶端憑證，並重新啟動面板。相互 TLS 可按需啟用；如果欄位為空，節點按先前的方案運作——僅使用 API 權杖。
- **路由面板對節點的外送連線（Connection outbound）** — 在節點表單中出現了**「Connection outbound」**（外送連線）欄位。如果在其中選擇一個 Xray outbound 標籤，面板對該節點 API 的流量會經由指定的 outbound（面板會自行在工作設定中加入 loopback 上的橋接 inbound 並在不重新啟動的情況下套用它）。空值 = 直接連線。在清單中，標籤分組為「外送」與「負載平衡器」，blackhole 外送被隱藏。
- **節點：將面板→節點的流量經由所選 outbound 路由（「Connection outbound」）** — 在節點表單中出現了「Connection outbound」欄位：它讓面板對節點的存取流量得以經由所選的 Xray outbound 進行路由（可用一般 outbounds 與負載平衡器）。面板會自動在工作設定中加入 loopback-bridge inbound 並在不重新啟動的情況下套用變更。若要直接連線，請將此欄位留空。
- **節點：在仍有 inbounds 繫結到節點時，刪除節點會被封鎖** — 只有在節點上的所有 inbounds 都已移除後，才能刪除該節點。如果仍有至少一個 inbound 繫結到節點，面板會以錯誤拒絕刪除——請先解除繫結或刪除這些 inbounds，然後再刪除節點。
- **節點：節點頁面顯示放置於節點上的 inbound 的即時速度** — 在「節點」頁面中，對於放置於節點上的 inbound，現在會顯示在線客戶端、計數器與目前的傳輸速度。「已結束」（ended）晶片只計算已過期與已用盡流量的客戶端（已停用的客戶端不再計入其中）。

### 14. Telegram 機器人
- **通知：帶 Telegram 與 Email (SMTP) 通道的新事件匯流排** — 新增了事件通知系統，具有兩個傳遞通道——Telegram 與 Email。在通知分頁中，事件以卡片分組：Outbound（失效/恢復）、Xray Core（異常終止）、Nodes（節點無法存取/已恢復）、System（CPU 與記憶體高負載，門檻可以 % 設定）、Security（登入嘗試）。每個群組都有一個主開關與已選事件的計數器。啟用的事件集合可針對 Telegram 與 Email 分別設定；預設啟用「登入嘗試」與「CPU 高負載」。
- **通知：新的 Email/SMTP 通道與 SMTP 伺服器設定** — 新增了透過 SMTP 的新電子郵件通知通道。在 SMTP 設定分頁中可設定：啟用 email 通知、SMTP 主機與埠號（預設 587）、使用者名稱、密碼（以隱藏方式儲存）、收件者清單（以逗號分隔）與加密類型——none、STARTTLS（預設）或 TLS。「傳送測試郵件」按鈕會檢查連線並顯示錯誤發生在哪個階段（連線、驗證、傳送）。在第二個分頁中選擇將收到郵件的事件。
- **通知：記憶體高負載警示（RAM 門檻）** — 在 CPU 高負載警示之外，新增了記憶體高負載警示。在「System」事件群組中出現了「Memory high (%)」，帶有自己的門檻欄位（預設 80%）；面板每分鐘檢查一次 RAM 負載，當超過門檻時會向所選通道發送通知。

### 15. 地理資料庫（geoip / geosite 與自訂）
- **地理資料庫更新：每個檔案的狀態以及無變更時略過重新啟動** — 地理資料庫更新（geoip/geosite，包含 IR 與 RU 組合）現在會顯示每個檔案的狀態：已更新、已是最新或下載錯誤。只有在至少一個檔案確實被更新時，才會重新啟動 Xray（也就是中斷使用中的連線）；若無變更，面板不會重新啟動。x-ui update-all-geofiles 指令也是相同的行為。

### 16. 運維：備份、日誌、更新、CLI
- **客戶端 IP 限制僅在已安裝 fail2ban 時運作；否則欄位被封鎖** — 客戶端的 IP 數量限制現在僅在伺服器上已安裝 fail2ban 時才有效。如果未安裝，客戶端表單與批次新增時的「IP Limit」欄位會變為不可用並附有說明提示（在 Windows 上——以另一則訊息），而這類伺服器上先前設定的限制會自動歸零，因為它們本來就不會套用。fail2ban 封鎖現在同時涵蓋 TCP 與 UDP。
- **在安裝與更新面板時自動安裝 fail2ban** — 在一般伺服器上安裝與更新面板時，fail2ban 現在會自動安裝並設定（先前只在 Docker 中發生），以便 IP 限制功能開箱即用。此行為由環境變數 XUI_ENABLE_FAIL2BAN 控制：當該變數未設定或等於 true 時會執行設定。可用 x-ui setup-fail2ban 指令手動執行；fail2ban 的錯誤不會中斷安裝或更新。
- **透過 XUI_PORT 變數覆寫面板埠號** — 新增了環境變數 XUI_PORT，它只在目前行程運作期間設定網頁面板的埠號，不會變更資料庫中儲存的 webPort 值。允許的值為 1 到 65535；空值、不正確或超出範圍的值會被忽略（改用 webPort），並在日誌中記錄警告。使用 bridge 網路的 Docker 時，容器的發布埠號必須與 XUI_PORT 一致，例如 XUI_PORT=8080 與 ports：「8080:8080」。
- **CLI：旗標 -webCert/-webCertKey 現在在 setting 子指令中生效** — 在 CLI 中，旗標 -webCert 與 -webCertKey 現在在 x-ui setting 子指令中也能運作（先前它們會被無聲忽略，面板仍維持無 HTTPS）。指定它們後，即可立即設定網頁面板憑證與金鑰的路徑，而不必另外呼叫 cert 子指令。
- **資料庫備份檔案名稱依伺服器位址產生** — 資料庫備份檔案現在依伺服器位址命名，而非固定的 x-ui.db / x-ui.dump。從瀏覽器下載時，名稱取自網址列中的面板位址，否則——取自設定的網頁網域，若無則——取自公開 IP（先 IPv4，後 IPv6）。如此一來，來自不同伺服器的備份就容易區分。副檔名仍為 SQLite 的 .db 與 PostgreSQL 的 .dump。
- **支援在僅有 IPv6 的主機上安裝與更新** — 安裝與更新腳本現在在僅有 IPv6 的伺服器上能正確運作：下載發行版與輔助檔案不再強制使用 IPv4，因此可在沒有 IPv4 位址的主機上安裝與更新面板。

---

根據面板原始檔分析整理而成。Yuriy Khachaturian（[yukh.net](https://yukh.net)）

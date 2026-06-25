# 3X-UI 面板使用手冊

🇸🇦 [العربية](3X-UI-MANUAL.ar.md) · 🇬🇧 [English](3X-UI-MANUAL.en.md) · 🇪🇸 [Español](3X-UI-MANUAL.es.md) · 🇮🇷 [فارسی](3X-UI-MANUAL.fa.md) · 🇮🇩 [Bahasa Indonesia](3X-UI-MANUAL.id.md) · 🇯🇵 [日本語](3X-UI-MANUAL.ja.md) · 🇧🇷 [Português](3X-UI-MANUAL.pt.md) · 🇷🇺 [Русский](3X-UI-MANUAL.ru.md) · 🇹🇷 [Türkçe](3X-UI-MANUAL.tr.md) · 🇺🇦 [Українська](3X-UI-MANUAL.uk.md) · 🇻🇳 [Tiếng Việt](3X-UI-MANUAL.vi.md) · 🇨🇳 [简体中文](3X-UI-MANUAL.zh-CN.md) · 🇹🇼 繁體中文

**3X-UI 版本：3.4.0。** 本手冊依據此版本編寫並針對該版本保持最新。3.4.0 相對於 3.3.1 的變更摘要請見[「3.4.0 的新功能」](#340-的新功能)一節。

> 詳盡的 **3X-UI** 網頁面板（管理 Xray-core）中文使用手冊：功能、設定與運維，並逐一說明介面中的每個欄位與
> 開關。
>
> 名稱與標籤與面板介面一致；中文術語按其在介面中的顯示方式列出。*inbound* / *outbound* 兩詞
> 不予翻譯。

## 目錄

- [3.4.0 的新功能](#340-的新功能)
- [1. 簡介、需求與安裝](#1-簡介需求與安裝)
  - [1.1. 什麼是 3X-UI](#11-什麼是-3x-ui)
  - [1.2. 支援的作業系統與架構](#12-支援的作業系統與架構)
  - [1.3. 安裝方式](#13-安裝方式)
  - [1.4. 首次啟動與預設憑證](#14-首次啟動與預設憑證)
  - [1.5. 檔案位置](#15-檔案位置)
  - [1.6. 管理指令 `x-ui`（腳本選單）](#16-管理指令-x-ui腳本選單)
  - [1.7. `x-ui` 子指令（無互動式選單）](#17-x-ui-子指令無互動式選單)
  - [1.8. SQLite → PostgreSQL 遷移](#18-sqlite--postgresql-遷移)
- [2. 登入面板與存取安全](#2-登入面板與存取安全)
  - [2.1. 登入表單](#21-登入表單)
  - [2.2. 雙重身分驗證（2FA / TOTP）](#22-雙重身分驗證2fa--totp)
  - [2.3. 登入嘗試限制（login limiter / 防暴力破解）](#23-登入嘗試限制login-limiter--防暴力破解)
  - [2.4. 變更管理員帳號與密碼](#24-變更管理員帳號與密碼)
  - [2.5. 祕密路徑（URI 路徑 / webBasePath）與面板埠號](#25-祕密路徑uri-路徑--webbasepath與面板埠號)
  - [2.6. 工作階段存活時間（逾時）](#26-工作階段存活時間逾時)
  - [2.7. LDAP（同步與驗證）](#27-ldap同步與驗證)
- [3. 概覽 / 儀表板](#3-概覽--儀表板)
  - [3.1. 資料收集的一般原則](#31-資料收集的一般原則)
  - [3.2. 處理器（CPU）](#32-處理器cpu)
  - [3.3. 記憶體（RAM）](#33-記憶體ram)
  - [3.4. 置換空間（Swap）](#34-置換空間swap)
  - [3.5. 磁碟（Storage）](#35-磁碟storage)
  - [3.6. 系統運作時間（Uptime）](#36-系統運作時間uptime)
  - [3.7. 系統負載（Load average）](#37-系統負載load-average)
  - [3.8. 網路：速度與總流量](#38-網路速度與總流量)
  - [3.9. 伺服器 IP 位址](#39-伺服器-ip-位址)
  - [3.10. TCP/UDP 連線](#310-tcpudp-連線)
  - [3.11. Xray 狀態與行程管理](#311-xray-狀態與行程管理)
  - [3.12. 面板更新（3X-UI）](#312-面板更新3x-ui)
  - [3.13. 地理檔案更新（GeoIP / GeoSite）](#313-地理檔案更新geoip--geosite)
  - [3.14. 資料庫備份與還原](#314-資料庫備份與還原)
  - [3.15. 其他介面元素](#315-其他介面元素)
- [4. Inbounds：建立與通用參數](#4-inbounds建立與通用參數)
  - [4.1. 表單通用欄位](#41-表單通用欄位)
  - [4.2. Sniffing（嗅探）](#42-sniffing嗅探)
  - [4.3. Allocate（埠號分配策略）](#43-allocate埠號分配策略)
  - [4.4. External Proxy（外部代理）](#44-external-proxy外部代理)
  - [4.5. Fallbacks（Fallback）](#45-fallbacksfallback)
  - [4.6. 定期重設流量](#46-定期重設流量)
  - [4.7. inbound 的 JSON（advanced）](#47-inbound-的-jsonadvanced)
  - [4.8. inbound 的操作：QR / Edit / Reset / Delete 與統計](#48-inbound-的操作qr--edit--reset--delete-與統計)
- [5. 協定](#5-協定)
  - [5.1. 支援的協定清單](#51-支援的協定清單)
  - [5.2. 哪些協定支援 TLS / REALITY / 傳輸](#52-哪些協定支援-tls--reality--傳輸)
  - [5.3. VLESS](#53-vless)
  - [5.4. VMess](#54-vmess)
  - [5.5. Trojan](#55-trojan)
  - [5.6. Shadowsocks](#56-shadowsocks)
  - [5.7. Dokodemo-door / Tunnel（透明轉發器）](#57-dokodemo-door--tunnel透明轉發器)
  - [5.8. SOCKS / HTTP（`mixed` 協定）](#58-socks--httpmixed-協定)
  - [5.9. WireGuard（inbound）](#59-wireguardinbound)
  - [5.10. Hysteria（預設 v2）](#510-hysteria預設-v2)
  - [5.11. MTProto（Telegram 代理）](#511-mtprototelegram-代理)
  - [5.12. 協定選擇速查表](#512-協定選擇速查表)
- [6. 傳輸（Stream Settings）](#6-傳輸stream-settings)
  - [6.1. 選擇傳輸網路](#61-選擇傳輸網路)
  - [6.2. RAW / TCP（`tcpSettings`）](#62-raw--tcptcpsettings)
  - [6.3. mKCP（`kcpSettings`）](#63-mkcpkcpsettings)
  - [6.4. WebSocket（`wsSettings`）](#64-websocketwssettings)
  - [6.5. gRPC（`grpcSettings`）](#65-grpcgrpcsettings)
  - [6.6. HTTPUpgrade（`httpupgradeSettings`）](#66-httpupgradehttpupgradesettings)
  - [6.7. XHTTP / SplitHTTP（`xhttpSettings`）](#67-xhttp--splithttpxhttpsettings)
  - [6.8. Hysteria 傳輸（`hysteriaSettings`）](#68-hysteria-傳輸hysteriasettings)
  - [6.9. 相關參數](#69-相關參數)
- [7. 連線安全：TLS、XTLS 與 REALITY](#7-連線安全tlsxtls-與-reality)
  - [7.1. 區別何在：TLS vs XTLS vs REALITY](#71-區別何在tls-vs-xtls-vs-reality)
  - [7.2. 「無」模式（`none`）](#72-無模式none)
  - [7.3. TLS 模式](#73-tls-模式)
  - [7.4. REALITY 模式](#74-reality-模式)
  - [7.5. 設定實務建議](#75-設定實務建議)
- [8. 客戶端](#8-客戶端)
  - [8.1. 客戶端欄位](#81-客戶端欄位)
  - [8.2. 與 inbound 的繫結](#82-與-inbound-的繫結)
  - [8.3. 對客戶端的操作](#83-對客戶端的操作)
  - [8.4. 批次操作](#84-批次操作)
  - [8.5. 搜尋、篩選與排序](#85-搜尋篩選與排序)
  - [8.6. 圖示與狀態](#86-圖示與狀態)
- [9. 客戶端群組](#9-客戶端群組)
  - [9.1. 什麼是客戶端群組以及為何需要它](#91-什麼是客戶端群組以及為何需要它)
  - [9.2. 群組與客戶端、inbound、節點及協定的關聯](#92-群組與客戶端inbound節點及協定的關聯)
  - [9.3. 群組參考與「空」群組](#93-群組參考與空群組)
  - [9.4. 群組的欄位與欄](#94-群組的欄位與欄)
  - [9.5. 建立群組](#95-建立群組)
  - [9.6. 重新命名群組](#96-重新命名群組)
  - [9.7. 將客戶端加入群組](#97-將客戶端加入群組)
  - [9.8. 從群組移除客戶端（不刪除客戶端本身）](#98-從群組移除客戶端不刪除客戶端本身)
  - [9.9. 重設群組流量](#99-重設群組流量)
  - [9.10. 刪除群組與刪除群組客戶端](#910-刪除群組與刪除群組客戶端)
  - [9.11. 與「客戶端」頁面的關聯](#911-與客戶端頁面的關聯)
  - [9.12. API 端點摘要](#912-api-端點摘要)
  - [9.13. 按群組的流量](#913-按群組的流量)
- [10. 訂閱（Subscription）](#10-訂閱subscription)
  - [10.1. 什麼是 subId 以及連結如何產生](#101-什麼是-subid-以及連結如何產生)
  - [10.2. 訂閱伺服器設定](#102-訂閱伺服器設定)
  - [10.3. 輸出格式](#103-輸出格式)
  - [10.4. 訂閱資訊頁面與 QR 碼](#104-訂閱資訊頁面與-qr-碼)
  - [10.5. 自訂訂閱頁面範本](#105-自訂訂閱頁面範本)
- [11. Xray：路由、outbounds、DNS 與擴充功能](#11-xray路由outboundsdns-與擴充功能)
  - [11.1. 編輯器結構：分頁／模式](#111-編輯器結構分頁模式)
  - [11.2. 基本設定（General）](#112-基本設定general)
  - [11.3. 路由規則（routing）](#113-路由規則routing)
  - [11.4. Outbounds（外送連線）](#114-outbounds外送連線)
  - [11.5. 負載平衡器（Balancers）](#115-負載平衡器balancers)
  - [11.6. DNS](#116-dns)
  - [11.7. Fake DNS](#117-fake-dns)
  - [11.8. WireGuard / WARP / NordVPN](#118-wireguard--warp--nordvpn)
  - [11.9. Reverse 代理與 TUN](#119-reverse-代理與-tun)
  - [11.10. 日誌與統計（Stats、metrics）](#1110-日誌與統計statsmetrics)
  - [11.11. 儲存、重新啟動與自動轉換](#1111-儲存重新啟動與自動轉換)
  - [11.12. 來自訂閱的 outbound（含自動更新）](#1112-來自訂閱的-outbound含自動更新)
  - [11.13. WARP 中的 IP 輪換](#1113-warp-中的-ip-輪換)
- [12. 節點（多面板，master/slave）](#12-節點多面板masterslave)
  - [12.1. 清單頂部的摘要](#121-清單頂部的摘要)
  - [12.2. 新增與編輯節點](#122-新增與編輯節點)
  - [12.3. TLS 檢查（針對 https 節點）](#123-tls-檢查針對-https-節點)
  - [12.4. 每個節點顯示的內容](#124-每個節點顯示的內容)
  - [12.5. 對節點的操作](#125-對節點的操作)
  - [12.6. 指標歷史](#126-指標歷史)
  - [12.7. inbounds 與客戶端如何同步](#127-inbounds-與客戶端如何同步)
  - [12.8. 節點鏈（子節點／傳遞節點）](#128-節點鏈子節點傳遞節點)
  - [12.9. 節點：3.3.0 的新功能](#129-節點330-的新功能)
- [13. 面板設定](#13-面板設定)
  - [13.1. 儲存與重新啟動面板](#131-儲存與重新啟動面板)
  - [13.2. 一般設定（「面板」分頁 / *General*）](#132-一般設定面板分頁--general)
  - [13.3. 面板存取：IP、埠號、路徑、網域、憑證](#133-面板存取ip埠號路徑網域憑證)
  - [13.4. 工作階段、面板代理與信任代理（「代理與伺服器」分頁 / *Proxy and Server*）](#134-工作階段面板代理與信任代理代理與伺服器分頁--proxy-and-server)
  - [13.5. Telegram 機器人（「Telegram 機器人」分頁 / *Telegram Bot*）](#135-telegram-機器人telegram-機器人分頁--telegram-bot)
  - [13.6. 日期與時間（「日期與時間」分頁 / *Date and Time*）](#136-日期與時間日期與時間分頁--date-and-time)
  - [13.7. 外部流量與 Xray 行為（「外部流量」分頁 / *External Traffic*）](#137-外部流量與-xray-行為外部流量分頁--external-traffic)
  - [13.8. 其他：Xray 設定範本與驗證 URL](#138-其他xray-設定範本與驗證-url)
  - [13.9. 管理員帳號與 API 權杖](#139-管理員帳號與-api-權杖)
  - [13.10. 3.3.0 的 API 變更（對整合很重要）](#1310-330-的-api-變更對整合很重要)
- [14. Telegram 機器人](#14-telegram-機器人)
  - [14.1. 啟用與設定機器人](#141-啟用與設定機器人)
  - [14.2. 主選單與按鈕](#142-主選單與按鈕)
  - [14.3. 機器人指令](#143-機器人指令)
  - [14.4. 客戶端管理（僅限管理員）](#144-客戶端管理僅限管理員)
  - [14.5. 通知與報告](#145-通知與報告)
  - [14.6. 備份與日誌](#146-備份與日誌)
  - [14.7. 運作特性](#147-運作特性)
- [15. 地理資料庫（geoip / geosite 與自訂）](#15-地理資料庫geoip--geosite-與自訂)
  - [15.1. 什麼是 geoip.dat 與 geosite.dat](#151-什麼是-geoipdat-與-geositedat)
  - [15.2. 標準地理檔案及其更新](#152-標準地理檔案及其更新)
  - [15.3. 使用者地理資源（Custom GeoSite / GeoIP）](#153-使用者地理資源custom-geosite--geoip)
  - [15.4. 驗證與限制](#154-驗證與限制)
  - [15.5. 面板啟動時的自動檢查](#155-面板啟動時的自動檢查)
  - [15.6. 在路由規則中使用地理資料庫](#156-在路由規則中使用地理資料庫)
- [16. 運維：備份、日誌、更新、CLI](#16-運維備份日誌更新cli)
  - [16.1. 資料庫備份與還原](#161-資料庫備份與還原)
  - [16.2. 檢視日誌](#162-檢視日誌)
  - [16.3. Xray 日誌記錄的等級與設定](#163-xray-日誌記錄的等級與設定)
  - [16.4. 管理 Xray：停止與重新啟動](#164-管理-xray停止與重新啟動)
  - [16.5. 重新啟動與更新面板](#165-重新啟動與更新面板)
  - [16.6. 定期任務（cron）](#166-定期任務cron)
  - [16.7. 主控台選單與 CLI（`x-ui`）](#167-主控台選單與-clix-ui)
  - [16.8. 移除面板](#168-移除面板)
  - [16.9. `x-ui migrateDB` 指令](#169-x-ui-migratedb-指令)

---

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

## 1. 簡介、需求與安裝

### 1.1. 什麼是 3X-UI

**3X-UI** 是一套開源的網頁管理面板，用於管理 [Xray-core](https://github.com/XTLS/Xray-core) 伺服器。此面板提供統一的多語言網頁介面，可部署、設定與監控種類繁多的代理與 VPN 協定：從單台 VPS 到由多個節點（node）組成的分散式組態皆可。

3X-UI 是原始 X-UI 專案的擴充分支。相較於原版，它新增了對更多協定的支援、更高的穩定性、按每個用戶端統計的流量計量，以及眾多便利功能。

主要功能：

- **多種協定的 inbound** — VLESS、VMess、Trojan、Shadowsocks、WireGuard、Hysteria2、HTTP、SOCKS (Mixed)、Dokodemo-door / Tunnel、TUN 以及 **MTProto**（Telegram 代理，於 3.3.0 加入）。
- **現代化傳輸與加密** — TCP (Raw)、mKCP、WebSocket、gRPC、HTTPUpgrade 及 XHTTP，並可由 TLS、XTLS 與 REALITY 保護。
- **Fallback** — 在同一個連接埠上提供多種協定（例如在 443 上同時提供 VLESS 與 Trojan），透過 Xray 的 fallback 機制實現。
- **按每個用戶端管理** — 流量配額、到期日期、IP 限制、顯示「線上」狀態、一鍵邀請連結、QR 碼與訂閱。
- **流量統計** — 按每個 inbound、用戶端與 outbound 統計，並可重設。
- **支援多個節點（node）** — 從單一面板管理並擴充至多台伺服器。
- **outbound 與路由** — WARP、NordVPN、自訂路由規則、負載平衡器、代理鏈。
- **內建訂閱伺服器**，支援多種輸出格式。
- **Telegram 機器人**，用於遠端監控與管理。
- **REST API**，內建 Swagger 文件。
- **彈性的儲存方式** — SQLite（預設）或 PostgreSQL。
- **13 種介面語言**，深色與淺色主題。
- **與 Fail2ban 整合**，用於按每個用戶端套用 IP 限制。

> 重要提示：本專案僅供個人使用。不建議將其用於非法目的或正式營運環境。

### 1.2. 支援的作業系統與架構

#### 作業系統

安裝腳本會根據 `/etc/os-release`（或 `/usr/lib/os-release`）中的 `ID` 欄位來判斷發行版。官方支援的有：

Ubuntu、Debian、Armbian、Fedora、CentOS、RHEL、AlmaLinux、Rocky Linux、Oracle Linux、Amazon Linux、Virtuozzo、Arch、Manjaro、Parch、openSUSE（Tumbleweed / Leap）、Alpine，以及 Windows。

在 Alpine 系列系統上使用 OpenRC 服務（`rc-service` / `rc-update`），其餘系統則使用 systemd。CentOS 7 透過 `yum` 安裝套件，較新的版本則透過 `dnf`。若無法辨識發行版，腳本預設會嘗試使用 `apt-get` 套件管理員。

#### 處理器架構

架構會根據 `uname -m` 的輸出來判斷，並對應到其中一個支援的值：

| `uname -m` 的值 | 3X-UI 架構 |
| --- | --- |
| `x86_64`、`x64`、`amd64` | `amd64` |
| `i*86`、`x86` | `386` |
| `armv8*`、`arm64`、`aarch64` | `arm64` |
| `armv7*`、`arm` | `armv7` |
| `armv6*` | `armv6` |
| `armv5*` | `armv5` |
| `s390x` | `s390x` |

若架構不在此清單中，腳本會顯示「Unsupported CPU architecture!」訊息並中止安裝。

#### 基本相依套件

在安裝面板之前，腳本會自動安裝一組基本套件（名稱因發行版而異）：`cron`/`cronie`/`dcron`、`curl`、`tar`、`tzdata`/`timezone`、`socat`、`ca-certificates`、`openssl`。

### 1.3. 安裝方式

#### 方式 1. 安裝腳本（推薦）

以 root 身分執行單一指令即可安裝：

```bash
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)
```

腳本必須具備 root 權限：若不以 root 身分執行，會顯示「Please run this script with root privilege」並以錯誤結束。

安裝程式逐步執行的內容：

1. 判斷作業系統與架構。
2. 安裝基本相依套件。
3. 下載發行版封存檔 `x-ui-linux-<arch>.tar.gz` 並解壓縮到 `/usr/local/x-ui` 目錄。
4. 下載管理腳本 `x-ui.sh` 並將其安裝為 `/usr/bin/x-ui` 指令。
5. 建立記錄檔目錄 `/var/log/x-ui`。
6. 啟動初始設定：選擇資料庫、產生帳號憑證、選擇連接埠、選擇性設定 SSL。
7. 安裝並啟動自動啟動服務（systemd 單元 `x-ui.service`，或 Alpine 上的 OpenRC init 腳本）。

**安裝時選擇資料庫。** 安裝程式提供以下選項：

- `1) SQLite`（預設，建議用於用戶端數量 < 500 的情況）— 單一檔案 `/etc/x-ui/x-ui.db`，無需設定。
- `2) PostgreSQL`（建議用於用戶端數量龐大或多節點的情況）。PostgreSQL 可在本機安裝（會建立名為 `xui` 的專用使用者與資料庫），或指定連往既有伺服器的 DSN。連線參數會以 `XUI_DB_TYPE` 與 `XUI_DB_DSN` 變數的形式寫入服務的環境檔（依發行版而定為 `/etc/default/x-ui`、`/etc/conf.d/x-ui` 或 `/etc/sysconfig/x-ui`）。

**範例：將 PostgreSQL 參數寫入服務環境檔。** 選擇 PostgreSQL 並指定 DSN 後，安裝程式會在環境檔中加入大致如下的內容：

```bash
XUI_DB_TYPE=postgres
XUI_DB_DSN=postgres://xui:S3cretPass@127.0.0.1:5432/xui?sslmode=disable
```

此處 `xui` 是使用者與資料庫的名稱，`127.0.0.1:5432` 是伺服器的位址與連接埠，`sslmode=disable` 適用於本機連線（對遠端伺服器通常使用 `require`）。

**安裝特定（舊）版本。** 可以明確指定版本標籤——安裝程式會下載對應的發行版：

```bash
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/v2.4.0/install.sh) v2.4.0
```

此種安裝方式允許的最低版本為 `v2.3.5`；若指定更舊的版本，會顯示「Please use a newer version (at least v2.3.5)」。

#### 方式 2. Docker

以預設的 SQLite 資料庫啟動：

```bash
docker compose up -d
```

若要以內建的 PostgreSQL 服務啟動，需要取消 `docker-compose.yml` 中 `XUI_DB_*` 行的註解，並使用設定檔啟動：

```bash
docker compose --profile postgres up -d
```

映像檔包含 Fail2ban（預設啟用），用於按用戶端套用 IP 限制。Fail2ban 透過 `iptables` 封鎖違規者，這需要 `NET_ADMIN` 能力。在 `docker-compose.yml` 中已透過 `cap_add` 提供此能力。若透過 `docker run` 手動啟動，則需自行加入這些能力，否則封鎖只會被記錄，而不會實際套用：

**範例：完整的 `docker run` 指令。** 最精簡的版本，包含面板連接埠的轉送、網路能力與資料庫的持久化磁碟區：

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

`/etc/x-ui` 磁碟區會在容器重新啟動之間保留 `x-ui.db` 檔案，否則設定與帳號將會遺失。

```bash
docker run -d --cap-add=NET_ADMIN --cap-add=NET_RAW ... ghcr.io/mhsanaei/3x-ui
```

在 Docker 中，面板是容器的主要程序：自動啟動由容器的重新啟動政策（例如 `restart: unless-stopped`）控制，而非由容器內的服務控制。

### 1.4. 首次啟動與預設帳號憑證

首次安裝時（仍使用預設帳號憑證的情況下），安裝程式會**產生隨機值**作為使用者名稱、密碼、網頁路徑以及連接埠：

| 參數 | 安裝時如何產生 | 備註 |
| --- | --- | --- |
| 使用者名稱（Username） | 由 10 個字元組成的隨機字串 | 自動產生 |
| 密碼（Password） | 由 10 個字元組成的隨機字串 | 自動產生 |
| 面板網頁路徑（WebBasePath） | 由 18 個字元組成的隨機字串 | 防止透過根 URL 被探測到面板 |
| 面板連接埠（Port） | 預設為 1024–62000 範圍內的隨機連接埠；如有需要可手動指定 | `webPort` 的「出廠」值為 `2053`，但安裝程式會將其覆寫 |

安裝結束時，腳本會輸出最終摘要：使用者名稱、密碼、連接埠、網頁路徑、API 權杖，以及可直接使用的登入連結（Access URL），格式如下：

```
https://<域名或IP>:<連接埠>/<網頁路徑>
```

若未設定 SSL 憑證，連結會是 `http://` 開頭，且腳本會顯示需要設定 SSL 的警告（選單項目 19）。

> 務必更改帳號憑證。由於登入名稱與密碼是隨機產生的，**應在安裝後立即將其儲存下來**。可隨時透過選單項目「Reset Username & Password」（見下文）或從網頁介面的面板設定中更改它們。重設後腳本會提醒：「Please use the new login username and password to access the X-UI panel. Also remember them!」。

安裝後，可使用 `x-ui` 指令開啟管理選單（見 1.6 節）。

### 1.5. 檔案位置

| 路徑 | 用途 |
| --- | --- |
| `/usr/local/x-ui/` | 面板安裝目錄（`x-ui` 二進位檔、`x-ui.sh` 腳本） |
| `/usr/local/x-ui/bin/xray-linux-<arch>` | Xray-core 二進位檔（在 armv5/armv6/armv7 上會更名為 `xray-linux-arm`） |
| `/usr/bin/x-ui` | 管理腳本（`x-ui` 指令） |
| `/etc/x-ui/x-ui.db` | SQLite 資料庫檔案（預設） |
| `/var/log/x-ui/` | 面板記錄檔目錄 |
| `/etc/systemd/system/x-ui.service` | systemd 服務單元（非 Alpine） |
| `/etc/init.d/x-ui` | OpenRC init 腳本（僅 Alpine） |
| `/etc/default/x-ui` · `/etc/conf.d/x-ui` · `/etc/sysconfig/x-ui` | 服務的環境變數檔（路徑依發行版而定）；`XUI_DB_TYPE`/`XUI_DB_DSN` 會寫入此處 |

資料庫目錄可透過環境變數 `XUI_DB_FOLDER`（預設為 `/etc/x-ui`）覆寫，Xray 二進位檔目錄則可透過 `XUI_BIN_FOLDER` 變數覆寫（預設為相對於面板目錄的 `bin`）。資料庫檔案名稱為 `x-ui.db`。

**範例：將資料庫移到獨立磁碟。** 若要將 `x-ui.db` 儲存在 `/etc/x-ui` 以外的地方，例如已掛載的磁碟 `/data`，請在服務環境檔中設定變數並重新啟動面板：

```bash
echo 'XUI_DB_FOLDER=/data/x-ui' >> /etc/default/x-ui
mkdir -p /data/x-ui
systemctl restart x-ui
```

資料庫的完整路徑將變為 `/data/x-ui/x-ui.db`。

#### 主要環境變數

| 變數 | 用途 | 預設值 |
| --- | --- | --- |
| `XUI_DB_TYPE` | 資料庫後端：`sqlite` 或 `postgres` | `sqlite` |
| `XUI_DB_DSN` | PostgreSQL 連線字串（當 `XUI_DB_TYPE=postgres` 時） | — |
| `XUI_DB_FOLDER` | SQLite 資料庫檔案的目錄 | `/etc/x-ui` |
| `XUI_INIT_WEB_BASE_PATH` | 網頁面板的初始 URI 路徑（僅在首次初始化時） | `/` |
| `XUI_DB_MAX_OPEN_CONNS` | 最大開啟連線數（PostgreSQL 連線池） | — |
| `XUI_DB_MAX_IDLE_CONNS` | 最大閒置連線數（PostgreSQL 連線池） | — |
| `XUI_ENABLE_FAIL2BAN` | 啟用透過 Fail2ban 套用 IP 限制 | `true` |
| `XUI_LOG_LEVEL` | 記錄等級（`debug`、`info`、`warning`、`error`） | `info` |
| `XUI_DEBUG` | 除錯模式 | `false` |

**範例：暫時啟用詳細記錄。** 為了診斷問題，將記錄等級提高到 `debug` 並重新啟動服務：

```bash
echo 'XUI_LOG_LEVEL=debug' >> /etc/default/x-ui
systemctl restart x-ui
x-ui log    # 檢視除錯記錄
```

診斷完成後，將值改回 `info`，以免記錄檔不斷膨脹。

**透過環境變數設定網頁面板的初始路徑。** `XUI_INIT_WEB_BASE_PATH` 變數會在設定首次初始化時指定網頁面板的 URI 路徑（`webBasePath`）。這在透過 Docker 或 systemd 部署時很方便，可立即固定面板的登入路徑。該值會自動正規化——必要時會在開頭與結尾加上斜線，而空白或僅由空格組成的值會被忽略（此時套用預設路徑 `/`）。此變數**僅影響首次初始化**：若設定已建立，則需在網頁介面中或透過選單項目「Reset Web Base Path」來變更路徑。

### 1.6. 管理指令 `x-ui`（腳本選單）

安裝後，`x-ui` 指令（以 root 身分執行）會開啟互動式選單「3X-UI Panel Management Script」。透過輸入項目編號（範圍 0–27）來選擇項目。許多項目也提供子指令形式以供腳本使用（見 1.7 節）。

選單分為若干主題區塊。

#### 安裝與更新

- **1. Install** — 安裝面板（執行 `install.sh`）。安裝前會檢查面板是否尚未安裝。
- **2. Update** — 將所有 x-ui 元件更新至最新版本。此過程不會遺失資料；更新後面板會自動重新啟動。需要確認。
- **3. Update Menu** — 僅將管理腳本（`x-ui.sh` / `x-ui` 指令）更新至最新版本，不重新安裝面板。
- **4. Legacy Version** — 安裝指定（舊）版本的面板。腳本會詢問版本號（例如 `2.4.0`）並下載對應的發行版。
- **5. Uninstall** — 完整移除面板**連同 Xray**。會停止並停用服務，刪除 `/etc/x-ui/` 與 `/usr/local/x-ui/` 目錄、服務環境檔以及管理腳本本身。需要確認（預設為「否」）。

#### 帳號憑證與設定

- **6. Reset Username & Password** — 重設面板的使用者名稱與密碼。可以輸入自訂值，或留空以隨機產生（隨機名稱為 10 個字元，隨機密碼為 18 個字元）。此外還會提示是否停用雙因素驗證（2FA，若已設定）。重設後面板會重新啟動。
- **7. Reset Web Base Path** — 重設面板的網頁路徑：產生新的隨機路徑（18 個字元），面板重新啟動。當先前的路徑外洩或被遺忘時使用。
- **8. Reset Settings** — 將面板的所有設定重設為預設值。**帳號憑證（使用者名稱與密碼）與帳號資料不會遺失。** 需要確認；重設後面板會重新啟動。
- **9. Change Port** — 變更網頁面板的連接埠。會詢問連接埠號（1–65535）；設定後需要重新啟動才能讓連接埠生效。
- **10. View Current Settings** — 檢視目前設定（`x-ui setting -show`）。內容也包括正在使用的資料庫後端（SQLite，或 DSN 中密碼被遮蔽的 PostgreSQL）以及可直接使用的存取連結（Access URL）。若未設定 SSL，會提示為 IP 位址簽發 Let's Encrypt 憑證。

#### 服務管理

- **11. Start** — 啟動面板服務。若面板已在執行，會顯示無需重複啟動的訊息。
- **12. Stop** — 停止面板服務。
- **13. Restart** — 重新啟動面板服務。
- **14. Restart Xray** — 僅重新啟動 Xray-core 核心，而不重新啟動面板本身（透過 `systemctl reload x-ui`，在 Docker 中則向面板程序傳送 `USR1` 訊號）。
- **15. Check Status** — 檢查服務狀態（`systemctl status x-ui` 或 `rc-service x-ui status`）。
- **16. Logs Management** — 管理記錄檔：檢視除錯記錄（Debug Log，透過 `journalctl`），以及（Alpine 以外）清除所有記錄（Clear All logs）。

#### 自動啟動

- **17. Enable Autostart** — 啟用作業系統開機時自動啟動面板（`systemctl enable x-ui` 或 `rc-update add`）。
- **18. Disable Autostart** — 停用開機時自動啟動。

在 Docker 中，自動啟動由容器的重新啟動政策控制，因此這些項目只會顯示相應的提示。

#### 安全與網路

- **19. SSL Certificate Management** — 透過 acme.sh 管理 SSL 憑證：為域名簽發憑證、撤銷、強制更新、檢視既有域名、為面板指定憑證路徑，以及為 IP 位址簽發短效（約 6 天，會自動更新）憑證。
- **20. Cloudflare SSL Certificate** — 透過 Cloudflare DNS 驗證簽發 SSL 憑證。
- **21. IP Limit Management** — 管理按用戶端的 IP 數量限制（基於 Fail2ban）：檢視與解除封鎖等。
- **22. Firewall Management** — 管理防火牆（開啟/關閉連接埠並檢視規則）。
- **23. SSH Port Forwarding Management** — 設定 SSH 連接埠轉送，以便透過 SSH 通道從本機開啟面板。

#### 效能與維護

- **24. Enable BBR** — 啟用/停用 TCP BBR 壅塞控制演算法（含 Enable BBR / Disable BBR 項目的子選單）。
- **25. Update Geo Files** — 更新 geo 資料庫（`.dat` 檔案），可選擇來源：Loyalsoldier（`geoip.dat`、`geosite.dat`）、chocolate4u（`geoip_IR.dat`、`geosite_IR.dat`）、runetfreedom（`geoip_RU.dat`、`geosite_RU.dat`）或 All（一次全部）。更新後面板會重新啟動。
- **26. Speedtest by Ookla** — 透過 Speedtest by Ookla 執行網路速度測試。
- **27. PostgreSQL Management** — 管理內建/連結的 PostgreSQL 執行個體（啟用及相關操作）。
- **0. Exit Script** — 退出選單。

### 1.7. `x-ui` 子指令（無互動式選單）

為了在腳本中使用，`x-ui` 指令支援直接的子指令（不帶引數執行 `x-ui` 會開啟選單）：

| 指令 | 動作 |
| --- | --- |
| `x-ui` | 開啟管理選單 |
| `x-ui start` | 啟動面板 |
| `x-ui stop` | 停止面板 |
| `x-ui restart` | 重新啟動面板 |
| `x-ui restart-xray` | 重新啟動 Xray |
| `x-ui status` | 服務目前狀態 |
| `x-ui settings` | 目前設定 |
| `x-ui enable` | 啟用作業系統開機時自動啟動 |
| `x-ui disable` | 停用自動啟動 |
| `x-ui log` | 檢視記錄 |
| `x-ui banlog` | 檢視 Fail2ban 封鎖記錄 |
| `x-ui update` | 更新面板 |
| `x-ui update-all-geofiles` | 更新所有 geo 檔案 |
| `x-ui migrateDB [file]` | 轉換 `.db` ↔ `.dump`（SQLite） |
| `x-ui legacy` | 安裝舊版本 |
| `x-ui install` | 安裝面板 |
| `x-ui uninstall` | 移除面板 |

### 1.8. 從 SQLite 遷移到 PostgreSQL

可以將既有的 SQLite 安裝遷移到 PostgreSQL：

```bash
x-ui migrate-db --dsn "postgres://xui:password@127.0.0.1:5432/xui?sslmode=disable"
# 接著在 /etc/default/x-ui 中設定 XUI_DB_TYPE 與 XUI_DB_DSN 並重新啟動：
systemctl restart x-ui
```

原始的 SQLite 檔案會保持不變——請在確認新後端運作正常後再手動刪除它。

**範例：驗證已切換到 PostgreSQL。** 遷移後，使用檢視設定的指令確認面板確實在新後端上運作——輸出中應顯示 PostgreSQL（DSN 中的密碼會被遮蔽）：

```bash
x-ui settings | grep -i -E 'db|dsn'
```

若面板可以開啟且帳號都在，便可刪除原始的 `x-ui.db`。

---

## 2. 登入面板與存取安全

本節說明與 3X-UI 面板管理員身分驗證相關的一切：登入表單、雙重要素驗證（TOTP）、密碼暴力破解防護、變更帳號憑證、修改面板的秘密路徑與連接埠、工作階段存活時間，以及透過 LDAP 進行同步／身分驗證。

### 2.1. 登入表單

登入頁面會在面板秘密路徑（`webBasePath`）的根路徑提供。若使用者已通過授權，會自動轉向 `…/panel/`。頁面上有主題切換、介面語言選擇，以及表單本身。

表單欄位：

| 欄位 | 提示／標題（RU） | 必填 | 說明 |
|------|--------------------------|-------------|----------|
| 使用者名稱 | 「Имя пользователя」 | 是 | 管理員登入名稱。空值在用戶端即被拒絕，在伺服器端則以「Введите имя пользователя」訊息拒絕。 |
| 密碼 | 「Пароль」 | 是 | 管理員密碼。空值會以「Введите пароль」訊息拒絕。 |
| Код 2FA | 「Код 2FA」 | 僅在啟用 2FA 時 | 此欄位**僅**在面板啟用雙重要素驗證時出現。為驗證器應用程式產生的 6 位數代碼。 |

**「Войти」**按鈕會將表單送往 `POST /login`。

行為與訊息：

- 登入成功時顯示「Вход выполнен успешно」並轉向 `…/panel/`。
- 對於任何帳號憑證錯誤或 2FA 代碼錯誤，伺服器都會回傳**統一**訊息：「Неверные данные учетной записи.」（英文：*Invalid username or password or two-factor code.*）。這是刻意設計的——面板不會提示究竟是哪一項錯誤（登入名稱、密碼或代碼），以免讓暴力破解更容易。
- 面板會根據 `POST /getTwoFactorEnable` 請求來顯示或隱藏「Код 2FA」欄位，該請求會在授權之前回傳目前的 2FA 狀態。
- 若伺服器端工作階段已過期，下次請求時會顯示「Сессия истекла. Войдите в систему снова」，並將使用者轉向登入頁面。

> 關於 CSRF 的說明：在送出表單之前，用戶端會取得 CSRF 權杖（`GET /csrf-token`）；`/login` 與 `/logout` 請求受 CSRF 檢查保護。

**範例：透過 API 登入。** 當 2FA 關閉時，只需登入名稱與密碼即可；啟用 2FA 時則加上 `twoFactorCode` 欄位：

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

成功時伺服器會回傳帶有工作階段 cookie 的 `Set-Cookie`——後續對 `/panel/api/…` 的請求都需要帶上它。

### 2.2. 雙重要素驗證（2FA / TOTP）

3X-UI 中的 2FA 依照 **TOTP** 標準實作，並相容於任何驗證器應用程式（Google Authenticator、Aegis、FreeOTP 等）。參數為硬編碼固定值：演算法 **SHA1**、**6** 位數、週期 **30** 秒、簽發者（issuer）`3x-ui`、標籤 `Administrator`。

**範例：用於編碼 QR 碼的 otpauth-URI。** 若驗證器應用程式無法掃描相機，可透過下列連結手動新增權杖（請將你自己的 Base32 秘密代入，取代 `JBSWY3DPEHPK3PXP`）：

```
otpauth://totp/3x-ui:Administrator?secret=JBSWY3DPEHPK3PXP&issuer=3x-ui&algorithm=SHA1&digits=6&period=30
```

參數 `algorithm=SHA1`、`digits=6`、`period=30` 對應面板的硬編碼固定值——無需修改。

設定位於 **Настройки → Учетная запись** 區段的**「Двухфакторная аутентификация」**分頁。

| 元素 | 文字（RU） | 說明 |
|---------|------------|----------|
| 切換開關 | 「Включить 2FA」 | 啟用／停用雙重要素驗證。 |
| 說明 | 「Добавляет дополнительный уровень аутентификации для повышения безопасности.」 | 切換開關下方的提示。 |

#### 如何啟用 2FA

啟用切換開關時，面板會**在本機產生新的秘密**——一段 Base32 編碼的隨機字串（字母表為 `A–Z` 與 `2–7`）。隨即開啟「Включить двухфакторную аутентификацию」視窗，內含逐步說明：

1. **「Отсканируйте этот QR-код в приложении для аутентификации или скопируйте токен рядом с QR-кодом и вставьте его в приложение」**。QR 碼下方會以文字形式顯示秘密本身——點選 QR 碼即可將秘密複製到剪貼簿（會彈出「Скопировано」）。
2. **「Введите код из приложения」**——需輸入應用程式產生的 6 位數代碼。代碼會**在瀏覽器端**驗證：面板自行依剛產生的秘密計算當前 TOTP，並與輸入值比對。若代碼錯誤——「Неверный код」；欄位只接受剛好 6 位數字。

只有在成功確認之後，秘密與啟用旗標才會被儲存。儲存時會顯示「Двухфакторная аутентификация была успешно установлена」。

重要：設定區段中的變更須透過共用的**「Сохранить」**按鈕套用，之後通常需要重新啟動面板（「Сохраните изменения и перезапустите панель для их применения」）。首次啟用 2FA 時，伺服器還會**讓所有作用中的工作階段失效**（遞增「login epoch」），因此套用設定後需要重新登入——此時就要帶上 2FA 代碼。

#### 如何停用 2FA

再次按下切換開關會開啟「Отключить двухфакторную аутентификацию」視窗，並提示「Введите код из приложения, чтобы отключить двухфакторную аутентификацию.」。輸入正確代碼後，旗標與秘密會被清除，並顯示「Двухфакторная аутентификация была успешно удалена」。

#### 登入時的代碼驗證

登入時，伺服器會取出已儲存的秘密，並將當前 TOTP 與送來的 2FA 代碼比對。不相符視為登入失敗，但向使用者顯示的是同一則合併訊息「Неверные данные учетной записи.」。

#### 復原存取（recovery）

3X-UI **沒有**獨立的「復原代碼」機制。若失去對驗證器應用程式的存取，就無法透過面板介面復原登入。唯一的途徑是直接在伺服器的資料庫中停用 2FA：在設定資料表中將 `twoFactorEnable` 鍵重設為 `false`（必要時清空 `twoFactorToken`），之後重新啟動面板。因此建議在啟用 2FA 時，將秘密（Base32 權杖）保存在安全的地方。

**範例：在伺服器上緊急停用 2FA。** 透過 SSH 取得伺服器存取後，停止面板、重設設定資料表中的鍵，然後再次啟動面板：

```bash
x-ui stop
sqlite3 /etc/x-ui/x-ui.db "UPDATE settings SET value='false' WHERE key='twoFactorEnable';"
sqlite3 /etc/x-ui/x-ui.db "UPDATE settings SET value='' WHERE key='twoFactorToken';"
x-ui start
```

完成後，登入只需登入名稱與密碼即可，2FA 可視需要重新設定。

> 與變更帳號憑證的關聯：變更登入名稱／密碼時（見 2.4），2FA 會在伺服器上**自動停用**，以免舊秘密阻擋以新帳號憑證登入。

### 2.3. 登入嘗試限制（login limiter／暴力破解防護）

面板內建失敗登入限制器（相當於應用層級的 fail2ban）。參數在程式碼中固定，**無法**透過介面設定：

| 參數 | 值 | 用途 |
|----------|----------|------------|
| 最大失敗次數 | **5** | 在時間視窗內允許的失敗嘗試次數。 |
| 計數視窗 | **5 分鐘** | 累計失敗的滑動視窗（較舊的會被捨棄）。 |
| 封鎖（cooldown） | **15 分鐘** | 超過門檻後該鍵被封鎖的時間長度。 |

運作方式：

- 封鎖鍵由**「IP + 登入名稱」組合**構成（登入名稱轉為小寫，並去除空白）。也就是說，封鎖只套用於特定的「位址 + 使用者名稱」組合，而非整個面板。
- 每次失敗嘗試（登入名稱／密碼錯誤或 2FA 代碼錯誤）都會使計數器增加。在 **5 分鐘**內累積達 **5** 次失敗後，該鍵會被封鎖 **15 分鐘**。封鎖期間，該組合的任何嘗試都會立即以同一則「Неверные данные учетной записи.」訊息被拒絕，即使資料正確也一樣。
- **成功登入會立即重設**計數器並解除該組合的封鎖。
- 用戶端 IP 位址的判定會考量受信任的代理（見 `trustedProxyCIDRs`）：只有當請求來自受信任位址時，才接受 `X-Real-IP` 與 `X-Forwarded-For` 標頭。否則使用實際連線位址，而當無法取得時則為字串 `unknown`。

所有嘗試都會被記錄。對於失敗的嘗試，會在伺服器日誌中寫入一則警告，包含使用者名稱、IP、原因，以及（若被封鎖）`blocked_until` 時間。若啟用了透過 Telegram 機器人的登入通知（`tgNotifyLogin`——「Уведомление о входе」），管理員還會額外收到成功、失敗與被封鎖嘗試的使用者名稱、IP 與時間。

**範例：Telegram 中的登入通知。** 啟用 `tgNotifyLogin` 後，每次嘗試後管理員都會收到大致如下的訊息：

```
Уведомление о входе
Пользователь: admin
IP: 203.0.113.45
Время: 2026-06-10 14:32:07
Статус: успешно
```

對於被封鎖的「IP + 登入名稱」組合，狀態中會註明該嘗試被限制器拒絕。

### 2.4. 變更管理員登入名稱與密碼

**Настройки → Учетная запись** 區段的**「Учетные данные администратора」**分頁。欄位：

| 欄位 | 文字（RU） | 說明 |
|------|------------|----------|
| 目前登入名稱 | 「Текущий логин」 | 現行使用者名稱。必須與目前登入名稱相符，否則變更會被拒絕。 |
| 目前密碼 | 「Текущий пароль」 | 用於確認身分的現行密碼。 |
| 新登入名稱 | 「Новый логин」 | 新的使用者名稱。不能為空。 |
| 新密碼 | 「Новый пароль」 | 新密碼。不能為空。 |

變更透過**「Подтвердить」**按鈕套用，並送往 `POST /panel/setting/updateUser`。

伺服器邏輯與訊息：

- 若「Текущий логин」與實際不符，或「Текущий пароль」錯誤——「Произошла ошибка при изменении учетных данных администратора.」並附說明「Неверное имя пользователя или пароль」。
- 若新登入名稱或新密碼為空——說明「Новое имя пользователя и новый пароль должны быть заполнены」。
- 成功時——「Вы успешно изменили учетные данные администратора.」。密碼以 bcrypt 雜湊形式儲存。

**範例：透過 API 變更帳號憑證。** 此請求需要有效的工作階段 cookie（登入時取得），並確認目前的登入名稱／密碼：

```bash
curl -X POST https://panel.example.com:2053/мой-секрет/panel/setting/updateUser \
  -b 'session=ВАША_СЕССИОННАЯ_COOKIE' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'oldUsername=admin&oldPassword=СтарыйПароль&newUsername=root&newPassword=НовыйСложныйПароль'
```

成功後，目前的工作階段會被作廢——需要以新資料重新登入。

變更帳號憑證的重要影響：

- **所有既有工作階段都會被作廢**（使用者的 `login_epoch` 計數器遞增），因此變更後面板會自動登出並轉向登入頁面——需要重新登入。
- 若變更當下已啟用 **2FA，則會自動停用**（旗標與秘密被重設）。變更登入名稱／密碼後，雙重要素驗證須重新設定。

若已啟用 2FA，在送出表單前會開啟「Изменить учетные данные」視窗，並提示「Введите код из приложения, чтобы изменить учетные данные администратора.」——只有確認目前的 2FA 代碼後才能變更帳號憑證。

### 2.5. 秘密路徑（URI 路徑／webBasePath）與面板連接埠

這些參數位於 **Настройки → Панель** 區段，直接影響面板的「隱蔽性」與可存取性。儲存並**重新啟動面板**後生效。

| 欄位 | 文字（RU） | 預設值 | 說明 |
|------|------------|-----------------------|----------|
| 面板連接埠 | 「Порт панели」（`panelPort`），提示「Порт, на котором работает панель」 | **2053** | 網頁介面的 TCP 連接埠。 |
| URI 路徑 | 「URI-путь」（`panelUrlPath`），提示「Должен начинаться с '/' и заканчиваться '/'」 | **/** | 秘密基底路徑（`webBasePath`）。面板僅能透過它存取（例如 `/мой-секрет/`）。 |
| 面板管理用 IP 位址 | 「IP-адрес для управления панелью」（`panelListeningIP`），提示「Оставьте пустым для подключения с любого IP」 | 空 | 面板監聽的位址。空 = 所有介面。 |
| 面板網域 | 「Домен панели」（`panelListeningDomain`），提示「Оставьте пустым для подключения с любых доменов и IP.」 | 空 | 依網域（Host）限制存取。 |
| 面板憑證公鑰路徑 | `publicKeyPath`，提示「Введите полный путь, начинающийся с '/'」 | 空 | 用於面板 HTTPS 存取的 TLS 憑證。 |
| 面板憑證私鑰路徑 | `privateKeyPath`，相同提示 | 空 | TLS 私鑰。 |

基底路徑（`webBasePath`）的行為：

- 值會自動正規化：若未以 `/` 開頭，會在開頭加上該字元；若未以 `/` 結尾，會在結尾加上。也就是說，路徑實際上一律為 `/…/` 形式。
- 基底路徑套用於面板本身、資源（assets）以及工作階段 cookie（cookie 僅針對此路徑發放）。

> 安全建議（「Предупреждения безопасности」區段）：若設定「過於公開」，面板會自行顯示警告：
> - 「Панель работает по обычному HTTP — настройте TLS для продакшна.」
> - 「Стандартный порт 2053 широко известен — измените его на случайный.」
> - 「Базовый путь по умолчанию "/" широко известен — измените его на случайный.」
>
> 換言之，對於正式環境的伺服器，應設定**非標準連接埠**、**非顯而易見的 URI 路徑**以及 **TLS 憑證**。

**範例：正式環境的「隱蔽」面板設定。** 在 **Настройки → Панель** 區段中設定大致如下的值：

| 欄位 | 值 |
|------|----------|
| 面板連接埠 | `34571`（隨機，取代 2053） |
| URI 路徑 | `/aXf9Qm2/`（非顯而易見，以 `/` 開頭與結尾） |
| 面板憑證公鑰路徑 | `/etc/letsencrypt/live/panel.example.com/fullchain.pem` |
| 面板憑證私鑰路徑 | `/etc/letsencrypt/live/panel.example.com/privkey.pem` |

儲存並重新啟動後，面板將僅能透過 `https://panel.example.com:34571/aXf9Qm2/` 存取，且安全警告會消失。

### 2.6. 工作階段存活時間（逾時）

**「Продолжительность сессии」**欄位（`sessionMaxAge`）位於面板／間隔設定之中。

| 欄位 | 文字（RU） | 預設值 | 單位 | 說明 |
|------|------------|-----------------------|---------|----------|
| 工作階段時長 | 「Продолжительность сессии」，提示「Продолжительность сессии в системе (значение: минута)」 | **360** | 分鐘 | 管理員工作階段 cookie 的存活期限。 |

行為：

- 值以**分鐘**指定（預設 360 分鐘 = 6 小時），在設定 cookie 時換算為秒。
- 若值**大於 0**，工作階段 cookie 會設定相應的 `MaxAge`。逾期後 cookie 失效，下次請求時使用者會收到「Сессия истекла. Войдите в систему снова」。
- 工作階段也會在變更帳號憑證或首次啟用 2FA 時提前失效（透過 `login_epoch` 機制，見 2.4 與 2.2），以及在明確登出（`POST /logout`）時失效。
- 工作階段 cookie 標記為 `HttpOnly`，採用 `SameSite=Lax` 政策；在直接以 HTTPS 存取面板時會設定 `Secure` 旗標。

除了逾時本身，還有一項相關通知：**「Задержка уведомления об истечении сессии」**（`expireTimeDiff`，提示「Получение уведомления об истечении срока действия сессии до достижения порогового значения (значение: день)」，預設 `0`）——可讓你提前收到警告。

### 2.7. LDAP（同步與身分驗證）

LDAP 區段提供兩項功能：(1) 當本機密碼不符時，透過 LDAP 驗證管理員登入；(2) 定期從目錄同步用戶端的狀態（VLESS 旗標的啟用／停用）。

登入時的使用方式：伺服器會先檢查本機 bcrypt 密碼雜湊。若**不符**且已啟用 LDAP，面板會嘗試在目錄中驗證使用者：在指定 `Bind DN` 時執行服務性 bind，接著依篩選器與屬性搜尋使用者記錄，並嘗試以找到的 DN 與輸入的密碼進行 bind。成功即表示登入。（LDAP 驗證成功後，若已啟用 2FA，仍會檢查 TOTP 代碼。）

區段欄位：

| 欄位 | 文字（RU） | 預設值 | 說明 |
|------|------------|-----------------------|----------|
| 啟用 LDAP 同步 | 「Включить LDAP-синхронизацию」（`enable`） | **false** | LDAP 整合的主開關。 |
| LDAP 主機 | 「LDAP-хост」（`host`） | 空 | LDAP 伺服器位址。 |
| LDAP 連接埠 | 「Порт LDAP」（`port`） | **389** | 連接埠。LDAPS 通常為 636。 |
| 使用 TLS（LDAPS） | 「Использовать TLS (LDAPS)」（`useTls`） | **false** | 啟用時使用 `ldaps://` 配置，並驗證伺服器憑證（不略過驗證）。 |
| Bind DN | 「Bind DN」（`bindDn`） | 空 | 用於初次 bind／搜尋的服務帳號 DN。若為空——不執行 bind（匿名搜尋）。 |
| Bind 密碼 | 提示：「Настроено; оставьте пустым, чтобы сохранить текущий пароль.」／「Не настроено.」／「Настроено — введите новое значение для замены」 | 空 | `Bind DN` 的密碼。獨立儲存；若要保留原值，將欄位留空。 |
| Base DN | 「Base DN」（`baseDn`） | 空 | 進行搜尋的子樹根（搜尋為遞迴，涵蓋整個子樹）。 |
| 使用者篩選器 | 「Фильтр пользователя」（`userFilter`） | `(objectClass=person)` | 用於選取帳號的 LDAP 篩選器。驗證時，登入名稱會經跳脫後代入篩選器。 |
| 使用者屬性（username/email） | 「Атрибут пользователя (username/email)」（`userAttr`） | `mail` | 與登入名稱／用戶端識別碼對應的屬性（例如 `mail` 或 `uid`）。 |
| VLESS 旗標屬性 | 「Атрибут VLESS-флага」（`vlessField`） | `vless_enabled` | 用於判定是否應啟用用戶端 VLESS 存取的屬性。 |
| 通用旗標屬性（選用） | 「Общий атрибут флага (опц.)」（`flagField`），提示「Если задано, переопределяет флаг VLESS — напр. shadowInactive.」 | 空 | 若指定，會用來取代 `vless_enabled`。 |
| Truthy 值 | 「Truthy-значения」（`truthyValues`），提示「Через запятую; по умолчанию: true,1,yes,on」 | `true,1,yes,on` | 視為「啟用」的旗標屬性值清單。 |
| 反轉旗標 | 「Инвертировать флаг」（`invertFlag`），提示「Включите, когда атрибут означает «отключено» (напр. shadowInactive).」 | **false** | 反轉旗標的意義。 |
| 同步排程 | 「Расписание синхронизации」（`syncSchedule`），提示「Строка типа cron, напр. @every 1m」 | `@every 1m` | 以 cron 類格式表示的同步週期。 |
| inbound 標籤 | 「Теги входящих」（`inboundTags`），提示「Входящие, на которых LDAP-синхронизация может авто-создавать или авто-удалять клиентов.」 | 空 | 限制可在哪些 inbound 上執行自動操作。若沒有 inbound：「Входящие не найдены. Сначала создайте входящий.」 |
| 自動建立用戶端 | 「Авто-создание клиентов」（`autoCreate`） | **false** | 當用戶端出現在目錄中時，在指定的 inbound 上建立用戶端。 |
| 自動刪除用戶端 | 「Авто-удаление клиентов」（`autoDelete`） | **false** | 當用戶端從目錄中消失時刪除它。 |
| 預設流量（GB） | 「Объём по умолчанию (ГБ)」（`defaultTotalGb`） | **0** | 自動建立用戶端的流量上限（0 = 無上限）。 |
| 預設期限（天） | 「Срок по умолчанию (дни)」（`defaultExpiryDays`） | **0** | 自動建立用戶端的有效期限（0 = 永久）。 |
| 預設 IP 上限 | 「Лимит IP по умолчанию」（`defaultIpLimit`） | **0** | 同時連線 IP 數量的限制（0 = 無限制）。 |

旗標同步邏輯的特點：讀取旗標屬性（`flagField`，預設 `vless_enabled`）時，若其值落在 truthy 值清單中，則視為「啟用」；若啟用反轉，結果會變為相反。使用者屬性（`userAttr`）用作對應鍵（email／名稱）——沒有此屬性值的記錄會被略過。

> 安全：建議啟用 **TLS（LDAPS）**，以免 bind 密碼與待驗證密碼以明文傳輸；並為 `Bind DN` 使用僅具最低必要讀取權限的帳號。

**範例：典型的 LDAP 同步設定（Active Directory）。** 為下列目錄填寫區段欄位：存取狀態儲存在類似 `userAccountControl` 的旗標屬性中，且依電子郵件對應：

| 欄位 | 值 |
|------|----------|
| LDAP 主機 | `ldap.example.com` |
| LDAP 連接埠 | `636` |
| 使用 TLS（LDAPS） | 啟用 |
| Bind DN | `CN=svc-3xui,OU=Service,DC=example,DC=com` |
| Base DN | `OU=Users,DC=example,DC=com` |
| 使用者篩選器 | `(objectClass=person)` |
| 使用者屬性（username/email） | `mail` |
| VLESS 旗標屬性 | `vless_enabled` |
| Truthy 值 | `true,1,yes,on` |
| 同步排程 | `@every 5m` |

採用此設定後，面板每 5 分鐘會遍歷 `OU=Users` 子樹，依 `mail` 對應用戶端，並依 `vless_enabled` 的值啟用／停用 VLESS 存取。

---

## 3. 概覽 / 儀表板

儀表板（「儀表板」，英文介面中為 *Overview*）是面板的起始頁面。它即時顯示伺服器與 Xray 程序的狀態。所有指標皆來自伺服器端。背景排程器**每 2 秒**重新組建一次快照，並透過 WebSocket 將其分發給所有已開啟的分頁；每分鐘一次，累積的指標序列會被寫入磁碟。HTTP 端點 `GET /status` 會回傳最近一次快取的快照。

下面詳細說明頁面上的每一項指標與每一個控制項。

### 3.1. 資料採集的一般原則

- 快照由 `gopsutil` 函式庫採集。如果某項具體量測失敗，該欄位保持為零，並在日誌中寫入警告（`get cpu percent failed`、`get uptime failed` 等）——這不會使整個儀表板崩潰，只是對應的方塊會顯示 0/N-A。
- 「瞬時」速率（CPU %、網路、磁碟 I/O）的計算方式為：當前快照與前一快照之差，除以以秒計的間隔。因此在頁面首次載入時，速率值可能為零，直到累積出第二次量測為止。
- 可在「系統歷史」（*System History*）區段中查看歷史記錄——圖表是根據下文所述的同一批資料序列繪製的（見 3.12 節）。

### 3.2. 處理器（CPU）

「處理器」方塊（*CPU*）以百分比顯示當前的處理器負載，並顯示處理器本身的參數。

| 指標 | 描述 |
|---|---|
| 處理器負載，% | 最近一個間隔內已佔用的處理器時間比例。透過指數平均（EMA，係數 `alpha = 0.3`）進行平滑，以免突增使指示器跳動。數值始終被限制在 0–100 % 範圍內。在第一次量測時回傳 0（基準點初始化）。 |
| 邏輯處理器 | 邏輯核心數量——即計入 Hyper-Threading 後的數量。 |
| 實體核心 | 實體核心的數量。 |
| 頻率 | 處理器的基礎頻率，單位 MHz。採用延遲查詢並快取：第一次成功的量測會被保存，重試的頻率不高於每 5 分鐘一次，且查詢本身受 1.5 秒逾時限制（在某些系統上，頻率查詢回應緩慢）。 |

CPU 負載在演算法上是這樣計算的：若有原生的平台實作則使用它，否則——透過處理器時間計數器的差量（busy / total）來計算。為避免重複計入，Guest 與 GuestNice 時間會被排除。

### 3.3. 記憶體（RAM）

「記憶體」方塊（*RAM*）顯示已使用量與總量。以「已使用 / 總量」和／或填充百分比的形式呈現。寫入歷史記錄的是百分比。

### 3.4. 置換空間（Swap）

「置換空間」方塊（*Swap*）顯示已使用量與總量。如果未設定置換檔／置換分割區（總量 = 0），該指標等於零；無 swap 時，歷史序列中寫入 0。

### 3.5. 磁碟（Storage）

「磁碟」方塊（*Storage*）顯示已使用量與總量，且**僅計入根分割區 `/`**。「磁碟使用率」（*Disk Usage*）歷史記錄中寫入填充百分比。磁碟輸入輸出（讀取 / 寫入，位元組/秒）作為間隔內的計數器差量另行採集——它顯示在歷史記錄的「磁碟 I/O」分頁中。

### 3.6. 系統運行時間（Uptime）

「系統運行時間」指標（*Uptime*）。這是自**整台伺服器**開機以來的時間（以秒計），而非面板或 Xray 的運行時間。Xray 程序的運行時間另行保存（見 3.9 節），面板的執行緒數量也是如此（譯為「執行緒」 / *Threads*）。

### 3.7. 系統負載（Load average）

「系統負載」區塊（*System Load*）——由三個數字組成的陣列 `[Load1, Load5, Load15]`。提示說明：「過去 1、5 和 15 分鐘的系統平均負載」（*System load average for the past 1, 5, and 15 minutes*）。歷史圖表名為「系統平均負載（1 / 5 / 15 分鐘）」。歷史序列中數值分別寫入：`load1`、`load5`、`load15`。

這是標準的 Unix 指標：處於執行佇列中的程序的平均數量。參考方式——與核心數比較：持續超過實體核心數量的負載表示過載。

### 3.8. 網路：速度與總流量

**僅計入實體介面**。虛擬與隧道介面被排除：即 `lo`/`lo0`，以及所有以 `loopback`、`docker`、`br-`、`veth`、`virbr`、`tun`、`tap`、`wg`、`tailscale`、`zt` 開頭的介面。數值會在所有剩餘介面上加總。

**總速度**（*Overall Speed*）——瞬時速度，間隔內的計數器差量：

| 指標 | 描述 |
|---|---|
| 上傳 / 發送（標籤「上傳」 / *Upload*） | 出站速度，位元組/秒。 |
| 下載 / 接收（標籤「下載」 / *Download*） | 入站速度，位元組/秒。 |

**總流量**（*Total Data*）——自系統啟動以來的累積計數器：

| 指標 | 描述 |
|---|---|
| 已發送（標籤「已發送」 / *Sent*） | 總共發送的位元組數。 |
| 已接收（標籤「已接收」 / *Received*） | 總共接收的位元組數。 |

此外還會採集封包速率（封包/秒）與封包總計數器——它們顯示在歷史記錄的「網路封包」（*Network Packets*）分頁中。網路相關的歷史序列：`netUp`、`netDown`、`pktUp`、`pktDown`。

### 3.9. 伺服器 IP 位址

「伺服器 IP 位址」區塊（*IP Addresses*）顯示 `IPv4` 與 `IPv6`。外部位址透過第三方服務確定（IPv4 用 `api4.ipify.org`、`ipv4.icanhazip.com`、`v4.api.ipinfo.io/ip`、`ipv4.myexternalip.com/raw`、`4.ident.me`、`check-host.net/ip`，IPv6 用類似的服務）。清單依序逐一嘗試，直到收到第一個成功的回應；每次請求的逾時為 3 秒。

特性：
- 結果在程序生命週期內**被快取**：成功確定的位址不會再次查詢。
- 如果沒有任何服務回應，欄位中保持 `N/A`。對於 IPv6，在第一次出現 `N/A` 時就會完全停用 IPv6 請求，以免在無 IPv6 的網路上浪費時間。
- 旁邊有一個「眼睛」按鈕，用於隱藏／顯示位址——提示「隱藏或顯示伺服器 IP 位址」（*Toggle visibility of the IP*）。這只是介面中的視覺隱藏（例如用於截圖），對位址本身沒有影響。

### 3.10. TCP/UDP 連線

「連線數量」區塊（*Connection Stats*）顯示伺服器上活躍的 TCP 與 UDP 連線總數（涵蓋整個系統，而非僅 Xray）。歷史圖表為「活躍連線（TCP / UDP）」（*Active Connections*），序列 `tcpCount`、`udpCount`。

### 3.11. Xray 狀態與程序管理

「Xray」卡片顯示 Xray-core 程序的狀態並提供對其的管理。

#### 狀態

| 值 | 標籤 | 翻譯 | 何時設定 |
|---|---|---|---|
| `running` | 「已啟動」 | *Running* | Xray 程序已啟動。 |
| `stop` | 「已停止」 | *Stopped* | 程序未啟動，且沒有記錄到啟動錯誤。 |
| `error` | 「錯誤」 | *Error* | 程序未啟動，但記錄到了啟動錯誤。錯誤文字會顯示在標題為「Xray 啟動時發生錯誤」（*An error occurred while running Xray*）的彈出視窗中。 |
| — | 「未知」 | *Unknown* | 在尚未取得狀態前顯示。 |

狀態旁邊會顯示 **Xray 版本**。

#### 管理按鈕

- **停止**（*Stop*）。呼叫 `POST /stopXrayService`。成功時，面板透過 WebSocket 分發新狀態 `stop` 與通知「Xray 已成功停止」（*Xray service has been stopped*）；出錯時——分發帶有文字的 `error` 狀態。重要提示：如果面板是*透過* Xray 本身存取的，停止 Xray 可能會中斷與面板的連線——直接連接到面板時則無此問題。
- **重新啟動**（*Restart*）。呼叫 `POST /restartXrayService`。執行操作前會顯示確認「重新啟動 xray？」並附說明「使用已儲存的設定重新載入 xray 服務」。成功時——狀態 `running` 與通知「Xray 已成功重新啟動」（*Xray service has been restarted successfully*）。重新啟動會套用當前已儲存的設定——請在變更設定後使用它。

> 注意。在這個分支中，為儀表板新增了適用於所有授權類型的完整 Start / Stop / Restart 管理功能；在原始的 3x-ui UI 中沒有單獨的「啟動」按鈕——啟動是透過重新啟動來執行的。

#### Xray 日誌檢視按鈕

Xray 卡片上有一個 Xray 日誌檢視按鈕（*Logs*）。只有在 Xray 設定中配置了 access 日誌時它才會出現：內建檢視器讀取的正是這個檔案，因此沒有 access 日誌時按鈕會被隱藏。按鈕的可見性綁定於獨立的 `accessLogEnable` 標誌，不再取決於 IP 限制——即使沒有 access 日誌，線上清單與 IP 位址限制仍能繼續運作（見 8 節）。

#### 選擇 Xray 版本

「選擇版本」區段（*Version*）可將 Xray-core 切換到其他發行版。版本清單透過 `GET /getXrayVersion` 載入：

- 來源——`XTLS/Xray-core` 儲存庫的 GitHub API（`/releases`）。請求會快取 **15 分鐘**；當 GitHub 發生故障時，會回傳最近一次成功取得的清單，以免選取器變空。
- 只有形如 `X.Y.Z` 且**不早於 26.4.25** 的發行版才會進入清單。

提示：「選擇您想要切換到的版本」（*Choose the version you want to switch to.*）以及警告「重要：舊版本可能不支援當前設定」（*Choose carefully, as older versions may not be compatible with current configurations.*）。

切換：`POST /installXray/:version`。流程：

**範例。** 切換到特定的 Xray-core 版本（工作階段 cookie 必須已透過授權取得）：

```bash
curl -X POST 'https://panel.example.com:2053/xpanel/installXray/v25.6.8' \
  -b cookie.txt
```

這裡的 `v25.6.8` 是 `GET /getXrayVersion` 所回傳清單中的標籤。該版本必須存在於此清單中，否則面板會回應拒絕。
1. 所選版本會檢查是否存在於當前的發行版清單中（否則——拒絕）。
2. Xray 停止。
3. 根據當前作業系統與架構，從 GitHub 下載壓縮檔 `Xray-<os>-<arch>.zip`（支援 amd64/64、arm64-v8a、arm32-v7a/v6/v5、386/32、s390x；Windows 為 `xray.exe`）。壓縮檔與二進位檔的大小限制為 200 MB。
4. 二進位檔以原子方式（透過臨時檔案 + 重新命名）替換，並標記為可執行。
5. Xray 重新啟動。

切換前會顯示對話框「切換 Xray 版本」（*Do you really want to change the Xray version?*），並附描述「這將把 Xray 版本變更為 #version#」。成功時——通知「Xray 已成功更新」（*Xray updated successfully*）。

### 3.12. 面板更新（3X-UI）

面板更新檢查區塊。資料透過 `GET /getPanelUpdateInfo` 取得：

| 欄位 | 描述 |
|---|---|
| 當前面板版本 | 已安裝面板的版本。 |
| 最新面板版本 | 自 GitHub 取得的 3x-ui 最新發行版。 |
| 有可用更新 | 表示最新版本比當前版本新的標誌。如果無需更新——則顯示「面板已是最新」 / 「已更新」。 |

**「更新面板」**按鈕（*Update Panel*）會啟動 `POST /updatePanel`。提示：「這將把 3X-UI 更新到最新發行版並重新啟動面板服務」。啟動前——確認「您確定要更新面板嗎？」並附文字「這將把 3X-UI 更新到版本 #version# 並重新啟動面板服務」。

特性與限制：
- 自我更新**僅在 Linux 上**受支援（在其他作業系統上回傳錯誤）。
- 更新腳本從官方儲存庫（`raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh`，限制 2 MB）下載，並透過 `bash` 執行，盡可能透過 `systemd-run` 進行隔離。
- 成功啟動時顯示「面板更新已開始」（*Panel update started*）；如果更新檢查失敗——「面板更新檢查失敗」。安裝過程中會顯示警告「安裝進行中。請勿重新整理頁面」。

### 3.13. 更新地理檔案（GeoIP / GeoSite）

更新地理資料庫的按鈕／對話框會呼叫 `POST /updateGeofile`（所有檔案）或 `POST /updateGeofile/:fileName`（單一檔案）。更新依據嚴格的名稱與來源白名單運作：

| 檔案 | 來源 |
|---|---|
| `geoip.dat`、`geosite.dat` | `Loyalsoldier/v2ray-rules-dat`（latest） |
| `geoip_IR.dat`、`geosite_IR.dat` | `chocolate4u/Iran-v2ray-rules`（latest） |
| `geoip_RU.dat`、`geosite_RU.dat` | `runetfreedom/russia-v2ray-rules-dat`（latest） |

行為：
- 檔案名稱會被驗證：禁止 `..`、斜線、絕對路徑；僅允許 `[a-zA-Z0-9._-]+.dat`。白名單之外的檔案不會被下載。
- 使用條件式請求 `If-Modified-Since`：如果來源伺服器上的檔案未變更（HTTP 304），則不會重新下載，只更新時間戳記。
- 下載後 Xray 會**重新啟動**（以載入新的資料庫）。

**範例。** 只更新俄羅斯地理資料庫，不動其他檔案：

```bash
curl -X POST 'https://panel.example.com:2053/xpanel/updateGeofile/geoip_RU.dat' -b cookie.txt
curl -X POST 'https://panel.example.com:2053/xpanel/updateGeofile/geosite_RU.dat' -b cookie.txt
```

若要一次更新白名單中的所有檔案——請呼叫不帶檔案名稱的 `POST /updateGeofile`。
- 對話框：「您確定要更新地理檔案嗎？」附「這將更新檔案 #filename#」（單一檔案）以及「這將更新所有地理檔案」（用於「全部更新」按鈕）。成功——「地理檔案已成功更新」。

### 3.14. 資料庫的備份與還原

「備份與還原」區塊（*Backup & Restore*）。行為取決於所使用的資料庫管理系統（預設為 SQLite 或 PostgreSQL）。

#### 匯出資料庫（備份）

「匯出資料庫」 / 「備份」按鈕（*Back Up*）會呼叫 `GET /getDb`。檔案以附件形式提供：
- **SQLite**：先執行 checkpoint（寫入 WAL），然後下載檔案 `x-ui.db`。提示：「點擊以下載包含您當前資料庫備份的 .db 檔案……」。
- **PostgreSQL**：下載自訂格式的傾印 `x-ui.dump`（`pg_dump --format=custom --no-owner --no-privileges`）。伺服器上必須安裝 PostgreSQL 用戶端工具；否則——出現關於缺少 `pg_dump` 的錯誤。

#### 匯入資料庫（還原）

「匯入資料庫」 / 「還原」按鈕（*Restore*）透過 `POST /importDB`（表單欄位 `db`）上傳檔案。提示：「點擊以選擇並上傳 .db 檔案……從備份還原資料庫」。

**SQLite** 的流程是安全的，可回滾：
1. 檔案會檢查是否為 SQLite 格式並保存到臨時檔案，然後檢查完整性。
2. Xray 停止，當前資料庫關閉並重新命名為 `*.backup`（後備）。
3. 新檔案接替工作資料庫的位置，執行初始化與遷移。如果出了問題——還原後備。
4. Xray 重新啟動。

對於 **PostgreSQL**，上傳 `.dump`（會檢查 `PGDMP` 簽章），並透過 `pg_restore --clean --if-exists --single-transaction …` 套用。提示直接警告：「這將取代所有當前資料」。

訊息：「資料庫已成功匯入」、「匯入資料庫時發生錯誤」、「……讀取資料庫時」、「……取得資料庫時」。

#### 遷移檔案（SQLite 與 PostgreSQL 之間）

「下載遷移檔案」按鈕（*Download Migration*）會呼叫 `GET /getMigration` 並產生可攜式匯出，用於在另一種資料庫管理系統上執行面板：
- 在 **SQLite** 上下載 `x-ui.dump`（文字 SQL 傾印）。
- 在 **PostgreSQL** 上下載 `x-ui.db`——由 PostgreSQL 資料組建而成的現成 SQLite 資料庫。

### 3.15. 其他介面元素

- **線上用戶端指示器。** 儀表板維護一個 `online` 序列（*Online Clients* / 「線上用戶端」）——具有活躍連線的用戶端數量。在 Xray 運行時計算（否則為 0），並以同樣的 2 秒節拍寫入歷史記錄。圖表——「線上」分頁。
- **系統歷史（圖表）。** 「圖表」按鈕／區段 →「系統歷史」，含以下分頁：「頻寬」、「封包」、「磁碟 I/O」、「線上」、「負載」、「連線」、「磁碟使用率」。資料透過 `GET /history/:metric/:bucket` 提取；允許的彙總間隔（bucket，秒）：**2、30、60、120、180、300、720、1440、2880**（最後三個對應於間隔選擇器中的 **12h**、**24h** 與 **48h** 預設值），每個分頁最多接收 60 個資料點。指標環形緩衝區保存最長 **48 小時**的資料，因此圖表（CPU、RAM、流量、封包、連線、磁碟、線上、負載）可查看最長兩天的範圍。允許的指標：`cpu, mem, swap, netUp, netDown, pktUp, pktDown, diskRead, diskWrite, diskUsage, tcpCount, udpCount, online, load1, load5, load15`。標籤「最近 2 分鐘」對應於 bucket = 2（即時模式）。

**範例。** 取得最近約 2 分鐘的 CPU 負載序列（bucket = 2 秒，最多 60 個點），以及按 5 分鐘彙總的同一序列（bucket = 300 秒）：

  ```bash
  curl 'https://panel.example.com:2053/xpanel/history/cpu/2' -b cookie.txt
  curl 'https://panel.example.com:2053/xpanel/history/cpu/300' -b cookie.txt
  ```

  指標可替換為任何允許的值（`mem`、`netUp`、`tcpCount`、`load1` 等）。不在清單 `2, 30, 60, 120, 180, 300, 720, 1440, 2880` 中的 bucket 會被拒絕。
- **Xray 指標**——獨立區塊，顯示 Xray 的記憶體消耗與垃圾回收（序列 `xrAlloc, xrSys, xrHeapObjects, xrNumGC, xrPauseNs`）以及「觀測站」（出站連線的狀態）。僅當 Xray 設定中指定了 `metrics` 區塊（`listen 127.0.0.1:11111`，標籤 `metrics_out`）時才會運作；否則顯示「Xray 指標端點未設定」。

**範例**：啟用 Xray 指標方塊的區塊。在 Xray 設定區段中，必須同時存在 `metrics`（帶標籤）以及監聽該標籤的 inbound：

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

  位址 `127.0.0.1:11111` 刻意不對外暴露——面板在本機對其進行輪詢。
- **深色主題切換。** 位於通用選單／頁首中，而非儀表板本身。選項：「主題」（*Theme*），含「深色」與「極深色」（*Ultra Dark*）選項。這純粹是視覺外觀設定，不影響面板運作。
- **其他連結**位於儀表板周邊（來自選單／底部面板）：「日誌」、「設定」——查看最終的 Xray JSON（`GET /getConfigJson`）、「文件」。

---

## 4. Inbounds：建立與通用參數

**「Inbounds」**（英文 *Inbounds*）區段是所有 Xray 入口點的清單，用戶端透過這些入口點進行連線。每個 inbound 同時保存「面板」欄位（備註、流量上限、重設排程）以及 Xray 組態的原始 JSON 區塊（`settings`、`streamSettings`、`sniffing`）。

建立透過 **「Add Inbound」**（*Add Inbound*）按鈕完成，編輯則透過 **「Modify Inbound」**（*Modify Inbound*）按鈕。兩項操作分別送往 API 端點 `POST /add` 與 `POST /update/:id`。

以下說明表單中所有**不**屬於特定協定設定（用戶端、加密、REALITY/TLS）、且**不**屬於傳輸/串流（**「Stream」**、**「Security」**分頁）的欄位 — 後者是其他章節的主題。

### 4.1. 通用表單欄位

#### Remark（備註）

| 參數 | 值 |
|---|---|
| 欄位 | `remark` |
| 類型 | 字串 |
| 預設值 | 空 |

inbound 的人類可讀名稱，會顯示在清單與對話框標題中（例如「刪除連線 "{remark}"？」等）。欄位標籤為 **「Remark」**。它不影響 Xray 的運作，僅用於管理上的便利；建議設定唯一且有意義的名稱，因為它們會被代入匯出檔案的名稱與大量操作的確認訊息中。

#### Protocol（協定）

| 參數 | 值 |
|---|---|
| 欄位 | `protocol` |
| 標籤 | **「Protocol」** |
| 驗證 | `required,oneof=vmess vless trojan shadowsocks wireguard hysteria http mixed tunnel tun` |

inbound 協定的下拉選單。允許的值：

| 值 | 備註 |
|---|---|
| `vmess` | |
| `vless` | |
| `trojan` | |
| `shadowsocks` | |
| `wireguard` | |
| `hysteria` | Hysteria v2 即 `hysteria` 搭配 `streamSettings.version = 2`，並沒有獨立的協定 |
| `http` | |
| `mixed` | 同一連接埠上的 socks/http |
| `tunnel` | |
| `tun` | 驗證器接受此值，但沒有對應的獨立協定常數 |

此欄位為必填（`required`）。所選協定決定哪些用戶端設定欄位以及哪種傳輸方式可用（見各協定專屬章節）。

> 重要：儲存時服務會將 `streamSettings` 正規化。傳輸設定只會保留給 `vmess`、`vless`、`trojan`、`shadowsocks`、`hysteria` 這幾種協定；其餘協定（`http`、`mixed`、`tunnel`、`wireguard`、`tun`）的 `streamSettings` 欄位會被**強制清空**。

對於 `tunnel`/TProxy 類型的 inbound，其 `streamSettings` 區塊不含 `security` 鍵（無傳輸變體），表單可正常開啟並儲存，不會出現 `streamSettings.security Invalid input` 驗證錯誤。

#### Listen IP（監聽 IP）

| 參數 | 值 |
|---|---|
| 欄位 | `listen` |
| 類型 | 字串 |
| 預設值 | 空 → Xray 監聽於 `0.0.0.0`（所有 IP） |

inbound 接受連線所使用的 IP 位址。欄位提示：

> 「留空以監聽所有 IP 位址」。

在產生 Xray 組態時，空值會被替換為 `0.0.0.0`。除了 IP 之外，此欄位也接受 **Unix 通訊端路徑** — 提示如下：

> 「也可以指定 Unix 通訊端路徑（例如 /run/xray/in.sock）或以 @ 為前綴的抽象通訊端名稱（例如 @xray/in.sock），以監聽通訊端而非 TCP 連接埠 — 此情況下請將連接埠設為 0」。

因此，此欄位接受兩種 Unix 通訊端形式：檔案系統中的路徑（`/run/xray/in.sock`）以及以 `@` 為前綴的抽象通訊端名稱（`@xray/in.sock`）。兩種情況下都請將 `Port` 設為 `0`。

當需要將 inbound 限制在單一介面上時（例如將只作為 Nginx 後方 fallback 目標運作的 inbound 設為 `127.0.0.1`），或當 inbound 監聽 Unix 通訊端時，才需要變更此欄位。

**範例。** 只監聽本機介面（典型的 Nginx 後方 fallback 目標）以及 Unix 通訊端的 inbound：

```
listen = 127.0.0.1   порт = 8443
listen = /run/xray/in.sock   порт = 0
```

#### Port（連接埠）

| 參數 | 值 |
|---|---|
| 欄位 | `port` |
| 標籤 | **「Port」** |
| 驗證 | `gte=0,lte=65535` |
| 預設值 | —（由使用者設定） |

監聽用的 TCP/UDP 連接埠。允許 `0` 到 `65535` 之間的值。值 `0` 僅在搭配監聽 Unix 通訊端時使用（見上文）。

儲存時服務會檢查連接埠衝突：兩個 inbound 不能同時佔用同一傳輸方式（TCP/UDP）下相互重疊的 `listen:port`。傳輸方式由協定與 `streamSettings`/`settings` 推算得出：例如 `hysteria` 與 `wireguard` 一律佔用 UDP，`kcp`/`quic` 佔用 UDP，而其餘大多數佔用 TCP。發生衝突時，儲存會被拒絕並回報錯誤。

此外，面板不允許佔用**內部 Xray API 的保留連接埠**（標籤 `api`，預設為 `127.0.0.1` 上的 `62789`）：若本機 TCP inbound 的監聽位址在 loopback 上與此連接埠重疊，會以相同的連接埠衝突錯誤被拒絕。實際的 API 連接埠是從 Xray 組態範本讀取（備援值為 `62789`）。在節點（nodes）上此限制不適用 — 它們有各自的 Xray。

> Xray 標籤（`Tag`，唯一）會自動依連接埠與傳輸方式以 `in-<連接埠>-<tcp|udp|tcpudp|any>` 格式產生；對於部署在節點上的 inbound，會加上 `n<nodeId>-` 前綴。若發生衝突，會在標籤後附加 `-2`、`-3` 等。使用者通常不需編輯標籤。

#### Total traffic（總流量，GB）

| 參數 | 值 |
|---|---|
| 欄位 | `total`（單位為**位元組**） |
| 標籤 | **「Total traffic」** |
| 預設值 | `0` |

inbound 的總流量上限。表單中以 GB 為單位輸入，資料庫中以位元組儲存。欄位提示：

> 「= 無限制。（單位：GB）」。

也就是說 **`0` 代表無限制**。這是整個 inbound 層級的上限（而非各別用戶端）；實際已用流量保存在 `up`（已傳送）與 `down`（已接收）欄位中，並與 `total` 比較。

#### Expiry date / Duration（到期日期 / 期限）

| 參數 | 值 |
|---|---|
| 欄位 | `expiryTime`（Unix 時間戳記） |
| 標籤 | **「Expiry date」**（英文 *Duration*） |
| 預設值 | 空 / `0` |

inbound 的有效期限。提示：

> 「留空以設為永久」。

空值（`0`）表示 inbound 永不過期。值以 Unix 時間戳記保存；表單既可設定明確的日期，也可設定以天數計的期限（從目前時刻起相對計算 — 英文欄位標籤為 *Duration*）。

#### Enabled（啟用）

| 參數 | 值 |
|---|---|
| 欄位 | `enable` |
| 標籤 | **「Enabled」**（英文 *Enabled*） |
| 預設值 | 於建立時設定 |

inbound 的啟用狀態標記。在清單中切換此旗標是由一個獨立的「輕量」端點 `POST /setEnable/:id` 處理，而非完整更新 — 這是為了避免在每次切換含有數千個用戶端的 inbound 的開關時，重新序列化整個 `settings` 區塊（所有用戶端）。停用 inbound 時，它會從運作中的 Xray 移除；啟用時則重新加回。

#### Node / Deploy to（節點 / 部署至）

| 參數 | 值 |
|---|---|
| 欄位 | `nodeId` |
| 標籤 | **「Deploy to」**、**「Local panel」** |
| 預設值 | 空（本機面板） |

選擇 inbound 實際運作的位置：在本機面板上，或在其中一個已註冊的節點上。實作細節：`nodeId = 0` 會被正規化為 `nil`，因為 `0` 並非有效的節點 id，而是表單繫結的產物；`nil`/`0` 代表本機面板。將 inbound 儲存到離線節點時，可能會出現「變更將在節點重新連線時同步」的提示訊息。

#### 連結用位址策略（Share address strategy）

| 參數 | 值 |
|---|---|
| 欄位 | 策略 +（選用）自訂位址 |
| 標籤 | **「Share address strategy」**（英文 *Share address strategy*） |
| 預設值 | **「Inbound listen」**（*Inbound listen*） |

此下拉選單決定該 inbound 的**匯出分享連結與 QR 碼**中要代入哪個位址。值：

| 值 | 標籤 | 代入的內容 |
|---|---|---|
| `node` | **「Node address」**（*Node address*） | inbound 所運作節點的位址 |
| `listen` | **「Inbound listen」**（*Inbound listen*） | inbound 本身的監聽位址 |
| `custom` | **「Custom」**（*Custom*） | 來自 **「Custom share address」**（*Custom share address*）欄位的自訂位址 |

選擇 **「Custom」** 時，會出現 **「Custom share address」** 欄位；在其中輸入**不含協定與連接埠**的主機名稱或 IP（值會被驗證）。**「Node address」** 選項只有在存在已啟用、且此 inbound 可在其上運作的節點時才會出現在清單中；否則會被隱藏，且值會回退為 **「Inbound listen」**。

此策略**只**影響直接分享連結與 QR 碼。它**不**影響訂閱輸出 — 訂閱中的位址仍由面板的一般邏輯決定。

### 4.2. Sniffing（嗅探）

**「Sniffing」**分頁編輯 Xray 組態的 `sniffing` 區塊，該區塊以原始 JSON 保存。Sniffing 讓 Xray 能「窺探」連線內部真正的網域名稱/協定，以供路由判斷之用。

| 子欄位 | 標籤 | 用途 |
|---|---|---|
| `enabled` | （分頁開關） | 啟用/停用 inbound 的嗅探 |
| `destOverride` | — | 要攔截目的位址的協定清單：`http`、`tls`、`quic`、`fakedns` |
| `metadataOnly` | **「Metadata only」** | 僅使用連線中繼資料，不讀取有效負載 |
| `routeOnly` | **「Route only」** | 嗅探結果僅用於路由，不改寫目的位址 |
| `domainsExcluded` | **「Excluded domains」** | 排除於嗅探之外的網域 |
| （排除的 IP） | **「Excluded IPs」** | 排除於嗅探之外的 IP 位址 |

- **`destOverride`** — 一組嗅探器：`http`（從 HTTP 標頭 Host 判斷網域）、`tls`（從 SNI 判斷）、`quic`（從 QUIC ClientHello 判斷）、`fakedns`（與 FakeDNS 池比對）。判斷網域時通常啟用 `http` 與 `tls`。

**`sniffing` 區塊範例**（依 HTTP 與 TLS 判斷網域，結果僅用於路由，不影響本地網路）：

```json
{
  "enabled": true,
  "destOverride": ["http", "tls"],
  "routeOnly": true,
  "domainsExcluded": ["courier.push.apple.com"]
}
```
- **`metadataOnly`** — 啟用時，Xray 不讀取第一個封包的內容，僅依靠中繼資料；對於不可「窺探」資料的協定，這有助於避免破壞協定。
- **`routeOnly`** — 嗅探結果僅供路由規則使用；outbound 中的連線位址不會被改寫為辨識出的網域。

> 備註：面板將 `sniffing` 當作不透明的 JSON 區塊保存，儲存時不會對其新增任何內容 — 這些核取方塊的所有預設值皆由用戶端應用程式那一側產生。原始形式的區塊可透過「Inbound 的 JSON」區段編輯（見下文）。

### 4.3. Allocate（連接埠分配策略）

`streamSettings` 中的 `allocate` 區塊控制 Xray 如何分配監聽連接埠。這是 Xray 組態的一部分；面板會將其當作 `streamSettings`/inbound JSON 的一部分保存並傳遞。參數（依 Xray-core 的術語）：

| 子欄位 | 用途 | 值 / 預設值 |
|---|---|---|
| `strategy` | 連接埠配置策略 | `always` — 一律監聽指定的連接埠（預設）；`random` — 在範圍內定期更換所監聽的連接埠 |
| `refresh` | `random` 時更換連接埠的間隔（分鐘） | 整數分鐘（建議 5；最小為 2） |
| `concurrency` | `random` 時同時保持開啟的連接埠數量 | 整數（預設 3；不超過連接埠範圍寬度的三分之一） |

`strategy: always` 讓 inbound 維持在單一連接埠上（標準模式）。`strategy: random` 用於反封鎖情境，此時 inbound 會定期在連接埠範圍內「跳動」；這種情況下 `refresh` 與 `concurrency` 才有意義。只有在刻意使用隨機連接埠模式時，才需變更這些值。

`streamSettings` 中的 **`allocate` 區塊範例**（隨機連接埠模式：保持 3 個連接埠開啟，每 5 分鐘更換一次）：

```json
{
  "allocate": {
    "strategy": "random",
    "refresh": 5,
    "concurrency": 3
  }
}
```

為使其運作，inbound 的 `port` 需設為範圍（例如 `20000-20100`）。

### 4.4. External Proxy（外部代理）

**「External Proxy」**欄位屬於邀請連結產生的設定，保存在 inbound 的 `streamSettings` 中。它設定一份替代外部位址清單（主機/連接埠，必要時可強制 TLS — **「Force TLS」**），這些位址會被代入用戶端連結，取代 inbound 真實的 `listen:port`。

當用戶端不應直接連到伺服器、而需透過外部代理/反向代理/CDN 連線時使用：此時分享連結中會填入該前端的公開位址。這不影響 Xray 接受連線的程序本身 — 它只是所產生連結的「外觀美化」。相關表單欄位：**「Force TLS」**、**「Fingerprint」**，以及各筆記錄的標籤。

### 4.5. Fallbacks（Fallback）

**「Fallbacks」**區段設定那些未匹配 inbound 任何用戶端的連線之轉送規則。此功能適用於 TLS 傳輸（VLESS/Trojan TCP-TLS）上的主 inbound。透過 `GET /:id/fallbacks` / `POST /:id/fallbacks` 端點管理。

區段提示：

> 「當此 inbound 上的連線未匹配任何用戶端時，它會被轉送到別處。在下方選擇一個子 inbound，路由欄位（SNI / ALPN / Path / xver）便會自動從其傳輸設定填入；或者保持空白並直接設定 Dest（例如 8080 或 127.0.0.1:8080），以轉送到外部伺服器（如 Nginx）。每個子 inbound 都必須監聽於 127.0.0.1 且 security=none」。

fallback 區段只會在 RAW (TCP) 上、且安全性為 TLS 或 REALITY 的 VLESS/Trojan inbound 上顯示。新的 inbound 以 `security=none` 啟動，因此該區段一開始可能看起來不存在。在此狀態下（VLESS/Trojan、RAW/TCP、尚未設定安全性），會以內嵌提示取代區段：在 **「Security」**分頁選擇 TLS 或 Reality 之後，fallback 才會可用。

#### fallback 列的欄位

| 欄位 | 預設值 | 說明 |
|---|---|---|
| （子 inbound） | — | 選擇子 inbound（標籤 **「Select inbound」**）。選定後，Name/Alpn/Path/Dest 欄位可從其傳輸設定自動填入 |
| Name | 空（= 任意） | 依名稱（SNI/名稱）匹配的條件。「任意」標籤為 **「any」** |
| Alpn | 空 | 依 ALPN 匹配的條件 |
| Path | 空 | 依路徑匹配的條件（適用於子 inbound 的 WS/HTTP 傳輸） |
| Dest | 自動 | 轉送目的地。佔位文字 **「auto (子的 listen:連接埠)」**。可指定連接埠（`8080`）或 `host:port`（`127.0.0.1:8080`） |
| Xver | `0` | PROXY 協定版本（**「Xver」**）：`0` — 關閉，`1` 或 `2` — 對應的 PROXY protocol 版本 |
| （順序） | 依位置 | 規則套用順序；以 **「上移」**/**「下移」** 按鈕設定 |

儲存邏輯：主 inbound 的整份 fallback 清單會原子性地替換。若某一列既沒有選定子 inbound（`childId <= 0`），也沒有設定 `Dest`，則會被**略過**。若選定的子 inbound 等於主 inbound 自身的 id，則會被歸零。產生最終 JSON 時：若 `Dest` 為空，會從子 inbound 算出 `listen:port`，其中 `0.0.0.0`/`::`/`::0` 會被替換為 `127.0.0.1`；空的 `name`/`alpn`/`path` 欄位不會出現在輸出 JSON 中；`xver` 只有在大於 0 時才會加入。

**最終 `settings.fallbacks` 範例**（`alpn=h2` 的流量經由路徑 `/ws` 送往 WS 目標，其餘全部送往連接埠 8080 上的本機 Nginx）：

```json
{
  "fallbacks": [
    { "alpn": "h2", "path": "/ws", "dest": "127.0.0.1:2001", "xver": 1 },
    { "dest": 8080 }
  ]
}
```

最後一列沒有 `name`/`alpn`/`path` — 這是「預設」規則，捕捉其餘所有流量。

#### fallbacks 區段的按鈕與提示

- **「Add fallback」** — 新增一列；**「尚無 fallback」** — 空狀態。
- **「快速加入所有符合的」** / **「Add all」** — 為每個符合且尚未連接的 inbound 新增一列 fallback。結果：「已新增 {n} 個 fallback」或「沒有新的符合 inbound」。
- **「從子填入」** — 從選定子 inbound 的傳輸設定重新拉取路由欄位（SNI/ALPN/Path/xver）；執行後出現「已從子填入」。
- **「編輯路由欄位」** / **「隱藏進階」** — 顯示/隱藏列的細部欄位。
- **「Routes when」** 與 **「預設 — 捕捉其餘所有」** 標籤說明每一列的觸發條件。

儲存 fallback 之後，伺服器會觸發 Xray 重新啟動，使新的 `settings.fallbacks` 生效。

### 4.6. 定期重設流量

**「重設流量」**區塊設定依排程自動重設 inbound 流量計數器。說明：

> 「依指定的間隔自動重設流量計數器」。

| 參數 | 值 |
|---|---|
| 欄位 | `trafficReset` |
| 驗證 | `omitempty,oneof=never hourly daily weekly monthly` |
| 預設值 | `never` |
| 相關欄位 | `lastTrafficResetTime` — 最後一次重設的時間戳記（標籤 **「Last reset」**） |

下拉選單：

| 值 | 標籤 |
|---|---|
| `never` | **「Never」** |
| `hourly` | **「Hourly」** |
| `daily` | **「Daily」** |
| `weekly` | **「Weekly」** |
| `monthly` | **「Monthly」** |

每個週期都註冊了一個依對應排程執行的 cron 工作（`@hourly`、`@daily`、`@weekly`、`@monthly`）。該工作會選出所有設定了相應 `trafficReset` 的 inbound，並對每一個重設 inbound 自身的計數器（`up=0`、`down=0`）**以及**其所有用戶端的流量。也就是說，定期重設會同時影響 inbound 與其用戶端。

**欄位值範例。** 若要讓計數器在每月一日歸零，在表單中選擇 **「Monthly」**，儲存為：

```json
{ "trafficReset": "monthly" }
```

值 `never`（預設）會完全關閉自動重設。

### 4.7. Inbound 的 JSON（advanced）

**「Inbound 的 JSON 區段」**區段提供對 inbound 原始 JSON 區塊的直接存取。說明：

> 「inbound 的完整 JSON，以及 settings、sniffing 與 streamSettings 的個別編輯器」。

可用的編輯器：

| 分頁 | 標籤 | 編輯內容 |
|---|---|---|
| **All** | 「在單一編輯器中呈現含所有欄位的完整 inbound 物件」 | 整個 Inbound 物件 |
| **Settings** | 「Xray settings 區塊的包裝」 | `settings` 欄位 |
| **Sniffing** | 「Xray sniffing 區塊的包裝」 | `sniffing` 欄位 |
| **Stream** | 「Xray stream 區塊的包裝」 | `streamSettings` 欄位 |

這些欄位會序列化為巢狀 JSON 物件：空區塊會以 `null` 輸出，而非有效 JSON 的文字會被包裝成字串，以免資料遺失。儲存時的解析錯誤會以 **「進階 JSON」** 前綴輸出。

「Inbound 的 JSON」檢視視窗與 inbound 匯入視窗一樣，使用具備 JSON 語法高亮的完整程式碼編輯器（而非一般文字欄位）：檢視組態時為唯讀的高亮模式，匯入時為可編輯模式，這讓閱讀與修改更為輕鬆。

### 4.8. inbound 的操作：QR / Edit / Reset / Delete 與統計

在清單與 inbound 卡片中可使用下列操作（**「選單」**選單）：

#### 流量統計

顯示 inbound 的彙總流量：**「已傳送/已接收」**（`up`/`down` 欄位）、**「總流量」**、**「總連線數」**。卡片中還有 **「建立時間」**、**「更新時間」**、**「到期日期」**。

inbounds 清單中有一個 **Speed** 欄位，顯示每個 inbound 目前的流量速率（上傳/下載），由兩次輪詢之間的計數器增量計算而得；同樣的即時速率也會顯示在 inbound 統計視窗中。當某次輪詢沒有增量時，速率值會重設。

inbounds 頁面的用戶端摘要中，狀態依「已耗盡/已結束」優先順序判定：到期或流量耗盡（且自動工作已取消其 `enable`）的用戶端歸類為 **「已耗盡/已結束」**（*Depleted/Ended*）狀態，而非灰色的 **「已停用」**（*Disabled*），且不會被重複計算。此分類與用戶端本身卡片中所顯示的一致，並正確處理繫結到多個 inbound 的用戶端。

#### QR 碼與複製連結

- **「詳情」** — 展開連線與訂閱連結。
- 用戶端 QR 碼：提示 **「點擊 QR 碼以複製」**。
- **「複製連結」**（英文 *Copy URL*）、**「匯出連結」**。

#### Edit（編輯）

**「Modify Inbound」** — 開啟編輯表單（`POST /update/:id`）。更新時服務會重新讀取既有的資料列、套用變更後的欄位、必要時重新產生標籤（若舊標籤是自動產生的），並同步 Xray 執行階段。成功時出現提示 **「連線已成功更新」**。

#### Reset Traffic（重設流量）

**「重設流量」** — 將此 inbound 的 `up`/`down` 計數器歸零（`POST /:id/resetTraffic`，設定 `up=0, down=0`）。確認訊息：

> 「重設 "{remark}" 的流量？」 / 「將此連線的傳送/接收計數器重設為 0」。

重設 inbound 流量**不會**動到其用戶端的計數器（用戶端有獨立的「重設用戶端流量」操作）。重設後會觸發 Xray 重新啟動。成功時出現提示 **「inbound 流量已重設」**。也有大量操作的版本 — **「重設所有連線的流量」**（`POST /resetAllTraffics`）。

#### Delete（刪除）

**「刪除連線」**（`POST /del/:id`）。確認訊息：

> 「刪除連線 "{remark}"？」 / 「此連線及其所有用戶端都將被刪除。此操作無法復原」。

刪除會將 inbound 從運作中的 Xray 移除（必要時伴隨重新啟動）。成功時出現提示 **「連線已成功刪除」**。大量刪除為 `POST /bulkDel`，具備逐項回報，且最多只觸發一次 Xray 重新啟動。

#### inbound 用戶端的其他操作

選單中也可使用：**「複製」**（建立 inbound 副本，使用新連接埠且用戶端清單為空）、**「刪除所有用戶端」**（`POST /:id/delAllClients` — 刪除所有用戶端，inbound 本身保留）、**「刪除已停用的用戶端」**、**「繫結/解除繫結用戶端」**、**「匯入」**/**「匯出連線」**（`POST /import`）。用戶端操作的細節屬於用戶端章節。

---

## 5. 協定

在建立傳入連線（inbound）時，首先要選擇 **Protocol**（「Protocol」）。協定決定 Xray-core 對此 inbound 採用何種流量驗證與加密方式、需要填寫 `settings` 中的哪一組欄位，以及該 inbound 可使用哪些傳輸方式（`network`）和哪些安全性類型（TLS / REALITY）。

協定欄位在建立 inbound 時設定一次，**編輯時無法變更**（編輯表單中的下拉清單已鎖定）。若要更換協定，需建立新的 inbound。

### 5.1. 支援的協定清單

伺服器接受 `Protocol` 欄位的下列取值：

```
oneof=vmess vless trojan shadowsocks wireguard hysteria http mixed tunnel tun mtproto
```

> 自 **3.3.0** 版起，清單中新增了 `mtproto` 取值（Telegram 代理）。

| 設定檔中的取值 | 用途 | 用戶端模型 |
|---|---|---|
| `vless` | 主要的代理協定（建立 inbound 時的預設值） | 使用 UUID 的用戶端，支援 flow 與後量子加密 |
| `vmess` | Xray 的經典代理協定 | 使用 UUID 與 `security` 參數的用戶端 |
| `trojan` | 偽裝成普通 HTTPS 的代理 | 使用密碼的用戶端 |
| `shadowsocks` | Shadowsocks 代理（含 SIP022 / 2022-blake3） | 單一使用者或多使用者（2022） |
| `wireguard` | WireGuard inbound | Peer（而非用戶端） |
| `hysteria` | Hysteria inbound（預設版本 2） | 使用 `auth` 權杖的用戶端 |
| `http` | 經典 HTTP 代理（forward proxy） | user/pass 帳戶，不計算流量 |
| `mixed` | 合併的 SOCKS + HTTP 代理 | user/pass 帳戶 |
| `tunnel` | 透明轉發器（xray `dokodemo-door`） | 無用戶端 |
| `tun` | TUN 介面（僅供呈現既有項目） | 無用戶端 |
| `mtproto` | Telegram 代理（MTProto），於 3.3.0 新增；由獨立的 `mtg` 程序提供服務，而非 Xray | 無用戶端（以 secret 存取） |

> 關於 `tun` 的說明：此取值保留在清單中是為了相容性以及**呈現**先前已儲存的 inbound，但在目前版本的 backend 中不建議建立此類型——其支援已被視為過時。建立此類型的新 inbound 並無意義。

> 關於 Hysteria 2 的說明：並無單獨的「hysteria2」協定。它就是設定了 `streamSettings.version = 2` 欄位的 `hysteria` 協定。在產生分享連結時，當流版本為 2，會自動選用 `hysteria2://` 連結方案。

並非所有協定都支援按節點（nodes）分發。只有下列協定可部署到節點：`vless`、`vmess`、`trojan`、`shadowsocks`、`hysteria`、`wireguard`。協定 `http`、`mixed`、`tunnel`、`tun`、`mtproto` 僅在本機面板上運作。

### 5.2. 哪些協定支援 TLS / REALITY / 傳輸

能否啟用某個安全層與傳輸，取決於協定與所選網路（`streamSettings.network`）：

| 功能 | 可用於協定 | 允許的網路（`network`） |
|---|---|---|
| **TLS** | `vmess`、`vless`、`trojan`、`shadowsocks`（以及 `hysteria` 一律可用） | `tcp`、`ws`、`http`、`grpc`、`httpupgrade`、`xhttp` |
| **REALITY** | `vless`、`trojan` | `tcp`、`http`、`grpc`、`xhttp` |
| **flow（`xtls-rprx-vision`）** | 僅 `vless` | 僅 `tcp`，且 `security = tls` 或 `reality` 時 |
| **Stream / 傳輸**（「Поток」分頁） | `vmess`、`vless`、`trojan`、`shadowsocks`、`hysteria` | — |

對於協定 `http`、`mixed`、`tunnel`、`tun`、`wireguard`，傳輸分頁不可用——它們沒有 Xray 的 stream 設定。

---

### 5.3. VLESS

用途：主要的現代代理協定。支援 XTLS-Vision（`flow`）、REALITY，以及 VLESS 自身層級的後量子加密（`decryption` / `encryption` 欄位）。新建 inbound 時為預設值。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `clients` | `[]` | 用戶端清單。每個用戶端含：`id`（UUID）、`email`（必填）、`flow`、限額（`limitIp`、`totalGB`、`expiryTime`）、`enable`、`tgId`、`subId`、`comment`、`reset` |
| `decryption` | `none` | 伺服器端的解密參數。UI 中的標籤：「Расшифрование」（英文「Decryption」） |
| `encryption` | `none` | 成對的加密參數（會放入用戶端連結）。標籤：「Шифрование」（英文「Encryption」） |
| `fallbacks` | `[]` | fallback 清單（見 fallback 章節）；當 `network = tcp` 且 `security` 為 TLS 或 REALITY 時可用 |
| `testseed` | （4 個數字：900、500、900、256） | 「Vision testseed」——用於 XTLS-Vision padding 的 4 個正整數。僅套用於使用 flow `xtls-rprx-vision` 的用戶端，否則忽略 |

#### flow（`xtls-rprx-vision`）

`flow` 設定**在用戶端上**，而非 inbound 上，並接受下列三種取值之一：

| 取值 | 含義 |
|---|---|
| `` （空） | 不使用 XTLS-flow（預設） |
| `xtls-rprx-vision` | XTLS-Vision——VLESS over TCP+TLS/REALITY 的建議模式 |
| `xtls-rprx-vision-udp443` | 同樣是 Vision，但會處理 UDP/443（QUIC） |

只有在滿足所有條件時，`flow` 欄位才可供選擇：協定 `vless`、`network = tcp`，且 `security` 為 `tls` 或 `reality`。表單中的 **Vision testseed** 欄位也僅在相同條件下顯示。

> XHTTP 的例外：當 VLESS over `network = xhttp` 並啟用 VLESS 的後量子驗證（`encryption`/`decryption`，vlessenc）時，flow `xtls-rprx-vision` 同樣可用——不論安全層為何，包括 REALITY。此時面板會正確地將 `xtls-rprx-vision` 傳入分享連結與訂閱（含 Clash/Mihomo 格式），因此用戶端取得的正是帶有 Vision 的設定。

#### 解密 / 加密（VLESS 的後量子驗證）

`decryption` 與 `encryption` 欄位屬於 VLESS 自身層級的驗證（與傳輸層的 TLS/REALITY 分開）。兩者預設皆為 `none`。表單中旁邊有三個按鈕：

- **Аутентификация X25519**（英文「X25519 auth」）——以 X25519 為基礎產生一對 `decryption`/`encryption`。
- **Аутентификация ML-KEM-768**（英文「ML-KEM-768 auth」）——後量子變體（Post-Quantum）。
- **Очистить**——將兩個欄位重設回 `none`。

按鈕下方會顯示狀態字串「Выбрано: {auth}」，其值由 `encryption` 字串的最後一段判定：空/`none` →「None」、極長的金鑰（>300 字元）→ ML-KEM-768、較短的 → X25519，否則為「Свой」（自訂）。

技術上，這些按鈕會呼叫 `GET /panel/api/server/getNewVlessEnc`（透過 `xray vlessenc` 產生金鑰）並以形如 `mlkem768x25519plus.native.<rtt>.<role>` 的成對值填入**兩個**欄位（例如 `decryption = mlkem768x25519plus.native.600s.server-x25519`、`encryption = mlkem768x25519plus.native.0rtt.client-x25519`）。`decryption` 參數留在伺服器，`encryption` 則進入用戶端連結。

> 重要：在為 Xray 產生 inbound 設定時，面板會移除多餘內容：若 `settings` 中仍留有 `encryption`（屬於用戶端那一側），它會從伺服器設定中被**剔除**。伺服器本機只保留 `decryption`。

何時選用 VLESS：這是新 inbound 的建議預設選項，尤其搭配 REALITY（無需自有憑證）或 TLS + XTLS-Vision 時。

**範例：含一個用戶端且使用 XTLS-Vision 的 VLESS inbound 的 `settings` 區塊。**`flow` 欄位位於用戶端上，`decryption` 留在伺服器：

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

對於 REALITY 組合，相應的 `streamSettings` 區塊（「Transport」分頁 → Security: REALITY）如下：

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

用途：Xray 的經典代理協定。以 UUID 驗證，用戶端另可設定酬載的加密方法（`security`）。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `clients` | `[]` | 用戶端清單 |

每個 VMess 用戶端（除了通用欄位 `email`、限額、`enable`、`tgId`、`subId`、`comment`、`reset` 之外）：

| 用戶端欄位 | 預設值 | 說明 |
|---|---|---|
| `id` | — | 用戶端 UUID |
| `security` | `auto` | VMess 酬載的加密方法。允許的取值：`aes-128-gcm`、`chacha20-poly1305`、`auto`、`none`、`zero` |

`security` 取值：
- `auto` — Xray 依平台自行選擇密碼（建議）；
- `aes-128-gcm`、`chacha20-poly1305` — 固定的 AEAD 密碼；
- `none` — 不加密酬載（僅在 TLS 之上才有意義）；
- `zero` — 不加密且不驗證酬載。

> 歷史相容性：舊紀錄可能儲存了 `security: ""`——讀取時空字串會轉為 `auto`。在產生伺服器設定時，VMess 用戶端的 `security` 欄位會從 `settings` 中**移除**，因為 inbound 不需要它。

何時選用 VMess：為了相容舊用戶端或既有設定。對於新部署，通常更建議使用 VLESS。

---

### 5.5. Trojan

用途：模擬普通 HTTPS 流量的代理。以密碼驗證。與 VLESS 一樣，支援 fallback，以及（在 `network = tcp` 時）REALITY/TLS。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `clients` | `[]` | 用戶端清單 |
| `fallbacks` | `[]` | fallback 清單（在 `network = tcp` 且 TLS/REALITY 時可用） |

每個 Trojan 用戶端的關鍵欄位：

| 用戶端欄位 | 預設值 | 說明 |
|---|---|---|
| `password` | — | 用戶端密碼（必填，至少 1 個字元） |
| `email` | — | 用戶端的唯一識別碼 |

用戶端的其餘欄位均為通用欄位（`limitIp`、`totalGB`、`expiryTime`、`enable`、`tgId`、`subId`、`comment`、`reset`）。

何時選用 Trojan：當需要在 443 連接埠上偽裝成 HTTPS 時，包括以 fallback 將未經授權的連線導向 Web 伺服器（Nginx）。

**範例：帶有 fallback 至本機 Web 伺服器的 Trojan `settings` 區塊。**未經授權的連線（無有效密碼）會被導向監聽 `127.0.0.1:8080` 的 Nginx：

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

fallback 需要 `network = tcp` 且 Security 為 TLS 或 REALITY；否則 fallbacks 欄位不可用。

---

### 5.6. Shadowsocks

用途：輕量的 Shadowsocks 代理。同時支援過時的 AEAD 密碼與新的 SIP022 方法（`2022-blake3-*`）。可在單使用者或多使用者模式下運作。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `method` | `2022-blake3-aes-256-gcm` | inbound 的加密方法。UI 中的標籤：「Метод шифрования」（英文「Encryption method」） |
| `password` | `` | inbound 的密碼（對 2022 方法會依所選方法自動產生） |
| `network` | `tcp,udp` | 傳輸。標籤：「Сеть」（英文「Network」）。選項：`tcp,udp`（TCP, UDP）、`tcp`、`udp` |
| `clients` | `[]` | 用戶端清單 |
| `ivCheck` | `false`（關閉） | 「ivCheck」開關——防止 IV 重複使用 |

#### 加密方法（`method`）

允許的集合：

| 方法 | 類別 |
|---|---|
| `aes-256-gcm` | 過時 AEAD |
| `chacha20-poly1305` | 過時 AEAD |
| `chacha20-ietf-poly1305` | 過時 AEAD |
| `xchacha20-ietf-poly1305` | 過時 AEAD |
| `2022-blake3-aes-128-gcm` | SS 2022（建議） |
| `2022-blake3-aes-256-gcm` | SS 2022（預設） |
| `2022-blake3-chacha20-poly1305` | SS 2022，單使用者 |

面板對各方法的邏輯：
- **2022 方法**（`2022-blake3-*`）視為「SS 2022」。`2022-blake3-chacha20-poly1305` 方法為**單使用者**（不支援 multi-user）；其他 2022 方法允許多個用戶端。密碼欄位（附產生按鈕，會將金鑰長度配合方法調整）正是針對 2022 方法在表單中顯示。
- **過時密碼**（`aes-*`、`chacha20-*`）採用經典的「一種方法 + 一組密碼」方案。

> 啟動 Xray 前的正規化：對於過時密碼，每個用戶端都必須帶有與 inbound 方法一致的 `method`（否則 Xray 會以「unsupported cipher method:」失敗）。對於 2022 方法則相反——用戶端的 `method` 欄位必須**為空**（否則 Xray 會以「users must have empty method」拒絕該 inbound）。面板會在切換方法時自行將資料整理妥當。

> 變更金鑰大小時重新產生用戶端金鑰：對於 Shadowsocks-2022，當加密方法變更為金鑰大小不同的方法時（例如在 `2022-blake3-aes-256-gcm` 與 `2022-blake3-aes-128-gcm` 之間），面板會在儲存 inbound 時自動依新長度重新產生用戶端 PSK。否則舊金鑰仍維持原長度，Xray 會予以拒絕。後果：受影響的用戶端需重新取得訂閱——舊連結將無法再連線。

何時選用 Shadowsocks：適用於不需 TLS 偽裝的簡單部署；現代的選擇是 2022-blake3 方法。

**範例：使用 2022-blake3 方法的 Shadowsocks `settings` 區塊（多使用者模式）。**inbound 有自己的密碼（所需長度的 base64 金鑰），每個用戶端有自己的密碼，用戶端的 `method` 欄位**為空**：

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

對於 legacy 密碼（`aes-256-gcm` 等）則相反：inbound 共用一組密碼，而用戶端的 `method` 必須與 inbound 方法一致。

---

### 5.7. Dokodemo-door / Tunnel（透明轉發器）

用途：透明轉發器（面板中為協定 `tunnel`，實作 `dokodemo-door` 行為）。接收流量並轉送至指定的位址/連接埠，無驗證、無用戶端。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `rewriteAddress` | （無） | 「Переписать адрес」（英文「Rewrite address」）——流量轉送的目標位址 |
| `rewritePort` | （無） | 「Переписать порт」（英文「Rewrite port」）——目標連接埠（0–65535） |
| `allowedNetwork` | `tcp,udp` | 「Разрешённая сеть」（英文「Allowed network」）。選項：`tcp,udp`、`tcp`、`udp` |
| `portMap` | `{}` | 「Сопоставление портов」——連接埠→連接埠的對應表（Record<string,string>） |
| `followRedirect` | `false`（關閉） | 「Следовать redirect」（英文「Follow redirect」）——使用攔截連線的原始目的位址 |

> Tunnel 的「Transport」分頁：此類型的 inbound 提供 **「Transport」** 分頁，但僅限 `sockopt` 設定——這足以滿足 **TProxy** 模式（透過 `sockopt.tproxy` 進行透明代理/redirect）。Tunnel 的傳輸選擇下拉清單（`network`）與「Security」分頁均隱藏，因為此類型不支援 TLS/REALITY。

何時選用：用於透明代理/將連接埠轉發至內部服務。

---

### 5.8. SOCKS / HTTP（協定 `mixed`）

在此版本中並無單獨的 `socks` 協定——SOCKS 與 HTTP 代理已合併為 **`mixed`** 協定（合併的 SOCKS + HTTP）。此外另有一個純粹的 `http` 代理。

#### 5.8.1. Mixed（SOCKS + HTTP）

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `auth` | `password` | 「Auth」——驗證模式。選項：`password`（以帳號/密碼）或 `noauth`（不驗證） |
| `accounts` | （選用） | 「Аккаунты」——user/pass 配對清單。當 `auth = noauth` 時，此欄位不寫入設定 |
| `udp` | `false`（關閉） | 「UDP」開關——透過 SOCKS 支援 UDP |
| `ip` | `127.0.0.1` | 「UDP IP」——UDP 關聯所用的本機位址。僅在啟用 `udp` 時顯示此欄位 |

帳戶以「Добавить」按鈕新增；新增時會產生隨機的帳號（8 字元）與密碼（12 字元），可加以編輯。

#### 5.8.2. HTTP（純代理）

用途：經典的 HTTP forward proxy。在 Xray 層級不將用戶端當作「計費」對象追蹤（沒有 email/限額）——僅有一份帳戶清單。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `accounts` | `[]` | 「Аккаунты」——user/pass 配對清單（兩個欄位皆必填） |
| `allowTransparent` | `false`（關閉） | 「Разрешить прозрачный」（英文「Allow transparent」）——以原始 Host 標頭轉送請求 |

何時選用 SOCKS/HTTP：用於不需複雜偽裝的本機或服務性代理存取。`mixed` 的便利之處在於單一連接埠可同時服務 SOCKS 與 HTTP 用戶端。

---

### 5.9. WireGuard（inbound）

用途：WireGuard inbound。與代理協定不同，它不以「用戶端」運作——取而代之設定的是 **peer**（伺服器所接受的裝置）。傳輸與 TLS/REALITY 對它不適用。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `secretKey` | — | 伺服器私鑰（必填）。旁有產生按鈕；公鑰會自動輸出（唯讀欄位） |
| `mtu` | （選用） | 介面 MTU |
| `noKernelTun` | `false`（關閉） | 「TUN без kernel」（英文「No-kernel TUN」）——使用 userspace-TUN 而非核心 TUN |
| `domainStrategy` | （選用） | 「Domain Strategy」——網域解析策略：`ForceIP`、`ForceIPv4`、`ForceIPv4v6`、`ForceIPv6`、`ForceIPv6v4` |
| `peers` | `[]` | peer 清單 |

每個 peer 的欄位：

| peer 欄位 | 預設值 | 說明 |
|---|---|---|
| `privateKey` | （選用） | 用戶端私鑰——加以儲存，以便面板能為使用者繪製設定（僅 inbound-peer 才有） |
| `publicKey` | — | peer 的公鑰（必填） |
| `preSharedKey`（PSK） | （選用） | 額外的共享金鑰 |
| `allowedIPs` | `[]` | 允許的 IP。新增 peer 時，面板會自動建議下一個可用位址（預設 `10.0.0.2/32`） |
| `keepAlive` | （選用） | 「Keep-alive」——保持連線的間隔 |
| `comment` | （選用） | 「Comment」——peer 的任意標記；顯示於「Peer N」標題旁，並會代入分享連結及 `.conf` 檔的 `remark` |

「Добавить peer」按鈕會產生新的金鑰對並代入下一個 `allowedIPs`。每個 peer 都可刪除（僅剩一個時無法刪除）。

peer 的「Comment」欄位有助於區分裝置：其文字會在表單中顯示於「Peer N」標題旁，也會進入分享連結與所產生 `.conf` 檔的 `remark`，因此在用戶端應用程式中很容易認出該裝置。此欄位屬於面板層級——xray-core 會忽略 peer 的未知欄位。

#### Domain Strategy 與 Transport 分頁

除了 peer 之外，WireGuard inbound 還有 **Domain Strategy** 欄位（網域解析策略：`ForceIP`、`ForceIPv4`、`ForceIPv4v6`、`ForceIPv6`、`ForceIPv6v4`）。此欄位非必填，僅在設定後才寫入設定。

> **Workers** 欄位（`workers`，工作執行緒數量）已自 WireGuard 表單（inbound 與 outbound 皆然）移除：自 xray-core v26.6.22 起，引擎不再使用它，而是依靠 wireguard-go 的內部機制。先前已儲存的設定無須變更即可運作——解析時此欄位會被直接捨棄，無需遷移。

> WireGuard 同樣提供 **「Transport」** 分頁——但為精簡版：其上僅可設定 `sockopt` 與 **Finalmask** 混淆。傳輸選擇下拉清單（`network`）隱藏，因為 WireGuard 一律以 UDP 監聽。在 noise（雜訊）紀錄中，Finalmask 以獨立欄位 **Rand Range** 設定（位元組範圍 0–255，附驗證），而 WireGuard 與 Hysteria 可用的混淆方法為 **Salamander**。

何時選用 WireGuard：當需要的正是 WireGuard VPN 通道，而非可偽裝的代理時。

---

### 5.10. Hysteria（預設 v2）

用途：基於 QUIC 的 Hysteria inbound。面板預設使用版本 2。每個用戶端以 `auth` 權杖驗證，而非 UUID/密碼。Hysteria 一律可用 TLS（見 5.2 的功能表）。

`settings` 區塊的欄位：

| 欄位 | 預設值 | 說明 |
|---|---|---|
| `version` | `2` | 協定版本（最低 1；面板預設 2） |
| `clients` | `[]` | 用戶端清單 |

每個用戶端的關鍵欄位為 `auth`（權杖，必填），加上通用欄位（`email`、限額、`enable`、`tgId`、`subId`、`comment`、`reset`）。

其他參數於 `streamSettings.hysteriaSettings` 中設定：

| 欄位 | 值 / 選項 | 說明 |
|---|---|---|
| `version` | 固定為 2（欄位已鎖定） | 「Версия」（英文「Version」） |
| `udpIdleTimeout` | （整數 ≥ 1，秒） | 「UDP idle timeout (с)」——UDP 閒置逾時 |
| `masquerade` | 預設關閉 | 「Masquerade」——對「未經授權」的請求偽裝成普通 Web 伺服器 |

啟用 `masquerade` 時可選擇類型（`type`）：
- `` — default（404 頁面）；
- `proxy` — 反向代理（欄位「Upstream URL」、「Переписать Host」、「Пропустить TLS verify」）；
- `file` — 目錄分享（欄位「Директория」，例如 `/var/www/html`）；
- `string` — 固定回應（欄位「Код статуса」、「Body」、「Заголовки」）。

何時選用 Hysteria：當需要 QUIC 傳輸並在不穩定/行動網路上保持穩固時；偽裝可提高入口點的隱蔽性。

---

### 5.11. MTProto（Telegram 代理）

> 於 **3.3.0** 版新增。協定取值為 `mtproto`。

MTProto 是 Telegram 自有代理的協定。在 3X-UI 中，此類 inbound **並非由 Xray 提供服務，而是由獨立的 `mtg` 程序**，並由面板本身管理。面板會定期將已啟用的 MTProto inbound 與執行中的 `mtg` 程序核對：啟動缺少的、停止多餘的，並從 `mtg` 的指標讀取流量計數。因此，此類 inbound 的**流量計算**與一般協定一樣運作。

表單中的官方提示：

> 「MTProto обслуживается отдельным процессом mtg, а не Xray. Настройки транспорта и клиенты здесь не применяются — поделитесь ссылкой ниже в Telegram.」

後果：

- **「Транспорт」（Stream Settings）與「Клиенты」分頁不適用於此 inbound**——存取以單一 secret 設定，而非用戶端清單。
- MTProto inbound **僅在主面板上啟動**；不會部署到子節點（nodes）（設定了 `NodeID` 的 inbound 會被略過）。

- MTProto 的 **「Sniffing」** 分頁隱藏——此協定由 `mtg` 程序提供服務，而非 Xray，因此 sniffing 對它不適用。

**欄位。**儲存於 inbound 的 `settings` 中：

| UI 中的欄位 | 鍵 | 說明 |
|---|---|---|
| Remark | `remark` | inbound 的標記。 |
| Listen IP | `listen` | 用於監聽的 IP（留空 = 所有介面）。 |
| Port | `port` | 代理連接埠。 |
| Секрет | `settings.secret` | **FakeTLS** 格式的存取 secret。 |
| Домен прикрытия (FakeTLS) | `settings.fakeTlsDomain` | 代理偽裝成對其發出 HTTPS 流量的網域。 |

**secret 格式（FakeTLS）。**面板會自動將 secret 整理為正確形式：結果 = `ee` + 32 個 hex 字元 + 掩護網域的 hex 編碼，亦即 `ee<hex32><hex(fakeTlsDomain)>`。前綴 `ee` 啟用 FakeTLS 模式，而網域（例如某知名網站）用於將流量偽裝成普通 HTTPS。只需指定網域——其餘部分面板會自行補齊。

#### Domain-fronting 與 mtg 進階選項

MTProto inbound 有 `mtg` 程序的額外參數。**Domain fronting IP**、**Domain fronting port** 與 **Domain fronting PROXY protocol** 欄位設定 `mtg` 將非 Telegram 流量送往何處（例如送往偽裝的 NGINX 網站）：若 IP 留空，則透過 DNS 使用 FakeTLS 網域，連接埠預設為 `443`。此外還可使用 **Accept PROXY protocol**（用於監聽器）、**IP preference**（`prefer-ipv6` / `prefer-ipv4` / `only-ipv6` / `only-ipv4`）與 **Debug logging**。每個值僅在設定後才寫入 `mtg-<id>.toml` 檔。

#### 透過 Xray 路由 Telegram 流量

**「Route through Xray」** 開關（預設關閉）與選用的 **Outbound** 欄位可讓 Telegram 的 egress 受 Xray 路由器掌控。啟用時，面板會在 Xray 設定中嵌入一個帶有該 inbound 標籤的本機 SOCKS 橋接，`mtg` 便透過它傳送 Telegram 流量。此後即可在「Routing」分頁以規則比對該流量，或透過 **Outbound** 欄位強制導向所選的 outbound 或負載平衡器（若欄位為空，則由路由規則決定）。

**如何提供給使用者。**對於 MTProto inbound，面板會產生邀請連結：

**範例：FakeTLS secret 與現成連結。**若掩護網域為 `www.cloudflare.com`，secret 組成為 `ee` + 32 個 hex 字元 + 網域的 hex 編碼，例如：

```
secret = ee1a2b3c4d5e6f70819293a4b5c6d7e8f7777772e636c6f7564666c6172652e636f6d
```

現成的邀請連結（將其與 QR 碼於 Telegram 中發送給使用者）：

```
tg://proxy?server=203.0.113.10&port=443&secret=ee1a2b3c4d5e6f70819293a4b5c6d7e8f7777772e636c6f7564666c6172652e636f6d
```

```
tg://proxy?server=<адрес>&port=<порт>&secret=<секрет>
```

（等同於 `https://t.me/proxy?server=…&port=…&secret=…`）。需將此連結與 QR 碼發送給 Telegram 使用者——開啟時代理會立即加入應用程式。此連結也會透過訂閱伺服器提供。

**何時使用。**這是繞過 Telegram 封鎖的標準方式；FakeTLS 偽裝（掩護網域）使流量看起來像對指定網站的普通造訪。

### 5.12. 協定選擇速查表

- **VLESS** — 預設選擇；搭配 REALITY 或 TLS + XTLS-Vision 時為最佳方案，支援後量子驗證。
- **Trojan** — 偽裝成 HTTPS，並可 fallback 至 Web 伺服器。
- **VMess** — 與舊用戶端相容。
- **Shadowsocks** — 不含 TLS 的簡單代理；現代的選擇是 `2022-blake3-*` 方法。
- **Hysteria** — QUIC，在惡劣網路上穩固。
- **mixed / http** — 服務性的 SOCKS/HTTP 代理。
- **WireGuard** — 完整的 VPN 通道。
- **tunnel** — 透明的連接埠轉發。
- **MTProto** — 用於繞過 Telegram 封鎖的代理（FakeTLS）；獨立的 `mtg` 程序。

---

## 6. 傳輸（Stream Settings）

傳輸（在面板介面中為 **「Транспорт」** 欄位，英文 *Transmission*）決定 Xray-core 在 inbound 內傳遞資料的方式：在 TLS/Reality 之上使用哪種網路協定，以及流量如何分幀。這些參數會儲存到 Xray 設定的 `streamSettings` 物件中，並在 inbound 編輯器的傳輸分頁中設定。加密（TLS / Reality）會在另一節中討論——這裡只描述網路的選擇及其參數。

### 6.1. 選擇傳輸網路

網路在 **「Транспорт」** 下拉選單（`streamSettings.network`）中選擇。預設值為 `tcp`（在列表中顯示為 **RAW**）。可用的選項如下：

| 列表中的值 | `network` 欄位 | 傳輸 |
| --- | --- | --- |
| RAW | `tcp` | 普通 TCP（在新版 Xray 中更名為 RAW），可選擇搭配 HTTP 混淆 |
| mKCP | `kcp` | 可靠的 UDP 傳輸 mKCP |
| WebSocket | `ws` | 基於 HTTP(S) 的 WebSocket |
| gRPC | `grpc` | gRPC 隧道（HTTP/2） |
| HTTPUpgrade | `httpupgrade` | HTTP Upgrade |
| XHTTP | `xhttp` | XHTTP / SplitHTTP——現代的可多工傳輸 |

切換值時，面板會清除前一個網路的設定區塊，並用該網路結構的預設值填充新網路的區塊，因此子表單的每個欄位始終會有合理的初始值。

> **重要。** 在此版本的面板中，**列表中沒有 HTTP/2（`h2`）傳輸**——它已從網路集合中移除；對於雙向類 HTTP/2 隧道請使用 gRPC，對於現代的 HTTP 偽裝傳輸請使用 XHTTP。**Hysteria** 傳輸（`hysteria`）不透過此列表選擇：它與 Hysteria 協定緊密綁定，並在 inbound 本身以 Hysteria 協定建立時自動出現（見第 6.8 節）。

下面分別解析每個網路及其每個欄位。

---

### 6.2. RAW / TCP（`tcpSettings`）

基礎 TCP 傳輸。預設情況下流量「按原樣」傳遞；可選擇將其偽裝成普通的 HTTP/1.1 交換。

| 欄位 | 預設值 | 描述 |
| --- | --- | --- |
| Proxy Protocol（`acceptProxyProtocol`） | `false`（關閉） | 接受來自上游負載均衡器/代理的 PROXY protocol 標頭 |
| HTTP 混淆（`header.type`） | `none`（關閉） | 開啟將流量偽裝成 HTTP/1.1 |

#### Proxy Protocol

**「Proxy Protocol」** 切換開關（`acceptProxyProtocol`）。開啟時，Xray 會在傳入連線上等待 PROXY protocol 標頭，並從中提取客戶端的真實 IP。僅當面板前面有反向代理/負載均衡器（例如帶 `send-proxy` 的 HAProxy 或 nginx）會添加此標頭時才開啟。預設為關閉。

#### HTTP 混淆（camouflage）

**「HTTP Обфускация」** 切換開關。控制 `header` 欄位：

- **關閉** → `header.type = "none"`（在傳輸線上 `header` 欄位直接不存在）。純 TCP。
- **開啟** → `header.type = "http"`。流量會以 HTTP/1.1 請求與回應的形式分幀。開啟時面板會立即用預設值填充 `request` 與 `response` 子物件。

開啟 HTTP 混淆時會出現用於設定模擬請求與回應的欄位。

**請求標頭（`header.request`）：**

| 欄位 | 鍵 | 預設值 | 描述 |
| --- | --- | --- | --- |
| 請求版本 | `request.version` | `1.1` | 請求起始行中的 HTTP 版本 |
| 請求方法 | `request.method` | `GET` | 模擬請求的 HTTP 方法 |
| 請求路徑 | `request.path` | `/` | 路徑。以逗號分隔的值列表輸入；在傳輸線上是字串陣列。若留空則填入 `/` |
| 請求標頭 | `request.headers` | `{}`（空） | HTTP 標頭的「名稱/值」表格。儲存為 `名稱 → [值]` 映射（一個名稱可對應多個值） |

**回應標頭（`header.response`）：**

| 欄位 | 鍵 | 預設值 | 描述 |
| --- | --- | --- | --- |
| 回應版本 | `response.version` | `1.1` | 回應起始行中的 HTTP 版本 |
| 回應狀態 | `response.status` | `200` | 模擬回應的 HTTP 狀態碼 |
| 回應原因 | `response.reason` | `OK` | 狀態的文字描述（reason-phrase） |
| 回應標頭 | `response.headers` | `{}`（空） | 回應標頭的「名稱/值」表格（`名稱 → [值]` 映射） |

標頭欄位逐行編輯——每行設定標頭名稱（`Имя`）及其值（`Значение`）。這些參數僅用於偽裝流量的外觀；對加密沒有影響。預設值（`GET / HTTP/1.1`，回應 `200 OK`）適用於大多數情境——只有在需要模擬特定網站/服務時才值得修改。

**帶 HTTP 混淆的 RAW 之 `streamSettings` 範例：**

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

請注意：在傳輸線上 `path` 是字串陣列，而每個標頭是值的陣列（`Host → ["www.example.com"]`）。

---

### 6.3. mKCP（`kcpSettings`）

mKCP 是基於 UDP 的可靠傳輸。在丟包率高、延遲大的通道上很有用，但會產生較高的額外流量。所有預設值都與 xray-core 中推薦的值一致。

| 欄位 | 鍵 | 預設 | 允許範圍 | 描述 |
| --- | --- | --- | --- | --- |
| MTU | `mtu` | `1350` | 576–1460 | 最大封包大小（位元組）。出現分片問題時調小 |
| TTI（毫秒） | `tti` | `20` | 10–100 | 傳輸間隔（ms）。越小延遲越低，但額外開銷越高 |
| Uplink（МБ/с） | `uplinkCapacity` | `5` | ≥ 0 | 上傳的估算吞吐量（МБ/с） |
| Downlink（МБ/с） | `downlinkCapacity` | `20` | ≥ 0 | 下載的估算吞吐量（МБ/с） |
| CWND 乘數 | `cwndMultiplier` | `1` | ≥ 1 | 壅塞視窗（congestion window）乘數 |
| 最大發送視窗 | `maxSendingWindow` | `2097152` | ≥ 0 | 最大發送視窗大小 |

欄位說明：
- **Uplink / Downlink capacity** 設定 mKCP 佔用通道的積極程度。應依照實際的通道頻寬設定：值過高會導致多餘流量，值過低則導致通道未被充分利用。
- **TTI** 直接影響「延遲 ↔ 額外開銷」的權衡：較小的值降低延遲，但增加服務性封包的數量。
- **MTU** 限制單個 mKCP 封包的大小；調低有助於在大型 UDP 封包被切割或丟失的通道上使用。

> 在此版本中，mKCP 子表單裡的「seed」欄位（mKCP 混淆密碼）以及**標頭/混淆類型**下拉選單（`none`、`srtp`、`utp`、`wechat-video`、`dtls`、`wireguard`）**不作為獨立欄位存在**——傳輸層混淆已移至通用的「FinalMask」機制（包括 `mkcp-legacy` 模式），在相應的章節中描述。「congestion」參數也未作為獨立勾選框列出；壅塞控制透過 `cwndMultiplier` 與 `maxSendingWindow` 設定。

---

### 6.4. WebSocket（`wsSettings`）

基於 HTTP(S) 的 WebSocket 傳輸。能很好地穿過 CDN 與反向代理，偽裝成普通的網頁流量。

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Proxy Protocol | `acceptProxyProtocol` | `false` | 接受來自上游代理的 PROXY protocol 標頭（見第 6.2 節） |
| Хост | `host` | `""`（空） | HTTP 標頭 `Host` 的值。在透過 CDN/域前置工作時指定 |
| Путь | `path` | `/` | WebSocket 握手請求行中的路徑 |
| heartbeat 週期 | `heartbeatPeriod` | `0` | 發送 heartbeat 幀的間隔（秒）。`0` 會停用 heartbeat |
| 標頭 | `headers` | `{}`（空） | 握手的額外 HTTP 標頭。「名稱 → 值」映射（僅字串值，無陣列） |

說明：
- **Путь** 必須在伺服器（inbound）與客戶端上一致。常常會在 web 伺服器側用此路徑來偽裝入口點。
- **Хост** 在 inbound 位於 CDN 之後或使用域前置時才有意義；否則可以留空。
- **heartbeat 週期** 在穿過會積極斷開不活躍連線的代理/CDN 時保持連線「活著」。預設（`0`）heartbeat 為關閉。
- 與 RAW 不同，WebSocket 的標頭表格使用「扁平」格式 `名稱 → 值`（每個標頭一行值）。

**位於 CDN 之後的 WebSocket 之 `streamSettings` 範例：**

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

`host` 與 `path` 的值必須與客戶端一致；與 RAW 不同，這裡的標頭值是普通字串，而非陣列。

---

### 6.5. gRPC（`grpcSettings`）

按參數數量計算最「輕量」的傳輸。在 gRPC 呼叫內部（基於 HTTP/2）對流量進行隧道封裝；與支援 gRPC 的 CDN 良好相容。沒有標頭混淆。

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| 服務名稱（`Service Name`） | `serviceName` | `""`（空） | gRPC 服務的名稱（實際上是隧道的「路徑」）。必須在伺服器與客戶端上一致 |
| Authority | `authority` | `""`（空） | 偽標頭 `:authority` 的值（HTTP/2 中相當於 `Host`）。在透過 CDN/域工作時指定 |
| Multi Mode | `multiMode` | `false`（關閉） | 開啟在單一連線內多工多個並行 gRPC 流 |

說明：
- **Service Name** 是 gRPC 通道的主要識別碼；它在兩端必須相同。空值是允許的，但通常會設定一個不明顯的字串來偽裝。
- **Authority** 影響在 HTTP/2 幀中發送哪個 `:authority`；主要在透過 CDN 代理時需要。
- **Multi Mode** 允許多個邏輯流透過單一物理連線；在伺服器與客戶端都支援時開啟以提升效能。

**gRPC 的 `streamSettings` 範例：**

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

`serviceName`（此處為 `GunService`）扮演隧道「路徑」的角色，必須在伺服器與客戶端上一致。

---

### 6.6. HTTPUpgrade（`httpupgradeSettings`）

基於 HTTP `Upgrade` 機制的傳輸（與 WebSocket 類似，但沒有 WebSocket 協定本身）。同樣能很好地穿過代理與 CDN。欄位集合與 WebSocket 相同，但**沒有** heartbeat 週期。

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Proxy Protocol | `acceptProxyProtocol` | `false` | 接受來自上游代理的 PROXY protocol 標頭 |
| Хост | `host` | `""`（空） | HTTP 標頭 `Host` 的值 |
| Путь | `path` | `/` | 帶 `Upgrade` 標頭的 HTTP 請求路徑 |
| 標頭 | `headers` | `{}`（空） | 額外的 HTTP 標頭。「扁平」映射 `名稱 → 值`（與 WebSocket 相同） |

**Хост**、**Путь** 與**標頭**欄位的用途與 WebSocket 相同（第 6.4 節）。HTTPUpgrade 未提供 heartbeat——這是 WebSocket 的特性。

---

### 6.7. XHTTP / SplitHTTP（`xhttpSettings`）

XHTTP（又稱 SplitHTTP）是 xray-core 現代的可多工 HTTP 傳輸。它將上行與下行流分成各自的 HTTP 請求，這很適合 CDN 及對連線持續時間有限制的環境。並非所有欄位都會同時顯示在編輯器中：其中一部分會依所選模式（`mode`）與已開啟的切換開關而出現。

#### 基礎欄位（始終顯示）

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Хост | `host` | `""`（空） | HTTP 標頭 `Host` 的值 |
| Путь | `path` | `/` | HTTP 請求的基礎路徑 |
| 模式（`Mode`） | `mode` | `auto` | 傳輸模式（見下文） |
| Server Max Header Bytes | `serverMaxHeaderBytes` | `0` | 伺服器上請求標頭大小的限制（位元組）。`0` 為 xray-core 的預設值 |
| Padding Bytes | `xPaddingBytes` | `100-1000` | 隨機「填充」padding 的範圍（位元組，格式為 `мин-макс`），用於阻礙大小分析 |
| 標頭 | `headers` | `{}`（空） | 額外的 HTTP 標頭。「扁平」映射 `名稱 → 值` |
| HTTP 方法 Uplink | `uplinkHTTPMethod` | `""`（Default = POST） | 上行請求的 HTTP 方法。選項：空（預設 POST）、`POST`、`PUT`、`GET`（後者僅在 `packet-up` 模式可用） |
| Padding Obfs Mode | `xPaddingObfsMode` | `false`（關閉） | 開啟進階的 padding 混淆並展開額外欄位（見下文） |
| No SSE Header | `noSSEHeader` | `false`（關閉） | 不發送 `Content-Type: text/event-stream`（SSE）標頭。若它妨礙穿過中間節點則開啟 |

#### 「模式」欄位（`mode`）

下拉選單，值如下：

| 值 | 描述 |
| --- | --- |
| `auto` | 自動選擇模式（預設） |
| `packet-up` | 上行流被拆分成各自的 HTTP 請求（每個請求一個封包） |
| `stream-up` | 上行流以單一長時間串流請求傳輸 |
| `stream-one` | 單一共用的雙向串流請求 |

模式的選擇決定哪些額外欄位會變為顯示。

**僅在 `mode = packet-up` 時顯示的欄位：**

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| 最大緩衝上傳 | `scMaxBufferedPosts` | `30` | 上行流同時緩衝的 POST 請求上限 |
| 最大上傳大小（位元組） | `scMaxEachPostBytes` | `1000000` | 單個上行 POST 請求的最大大小（位元組） |
| Uplink Data Placement | `uplinkDataPlacement` | `""`（Default = body） | 上行流資料的放置位置：`body`、`header`、`cookie`、`query` |
| Uplink Data Key | `uplinkDataKey` | `""` | uplink 資料的鍵/標頭名稱。僅在 `uplinkDataPlacement` 已設定且不等於 `body` 時出現 |

**僅在 `mode = stream-up` 時顯示的欄位：**

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Stream-Up Server | `scStreamUpServerSecs` | `20-80` | 伺服器串流連線的保持時間範圍（秒，格式為 `мин-макс`） |

#### padding 混淆欄位（在 `xPaddingObfsMode = 開啟` 時顯示）

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Padding Key | `xPaddingKey` | `""`（placeholder `x_padding`） | padding 的鍵名稱 |
| Padding Header | `xPaddingHeader` | `""`（placeholder `X-Padding`） | 傳遞 padding 的 HTTP 標頭名稱 |
| Padding Placement | `xPaddingPlacement` | `""`（Default = queryInHeader） | padding 的放置位置：`queryInHeader`、`header`、`cookie`、`query` |
| Padding Method | `xPaddingMethod` | `""`（Default = repeat-x） | padding 的產生方法：`repeat-x` 或 `tokenish` |

#### 工作階段與序列的放置（始終顯示）

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Session ID Placement | `sessionIDPlacement` | `""`（Default = path） | 傳遞工作階段識別碼的位置：`path`、`header`、`cookie`、`query` |
| Session ID Key | `sessionIDKey` | `""`（placeholder `x_session`） | 工作階段鍵名稱。僅在 `sessionIDPlacement` 已設定且不等於 `path` 時出現 |
| Session ID Table | `sessionIDTable` | `""`（placeholder `Base62`） | 用於產生工作階段識別碼的字元集。可從自動補全下拉選單中選擇預定義值（`ALPHABET`、`Alphabet`、`BASE36`、`Base62`、`HEX`、`alphabet`、`base36`、`hex`、`number`），或輸入任意 ASCII 字串。空為 xray-core 的預設值 |
| Session ID Length | `sessionIDLength` | `""`（空） | 產生的識別碼的長度或範圍（例如 `8-16`）。僅在已設定 `Session ID Table` 時顯示；最小值必須大於 0 |
| Sequence Placement | `seqPlacement` | `""`（Default = path） | 傳遞封包序號的位置：`path`、`header`、`cookie`、`query` |
| Sequence Key | `seqKey` | `""`（placeholder `x_seq`） | 序列鍵名稱。僅在 `seqPlacement` 已設定且不等於 `path` 時出現 |

工作階段欄位已依 xray-core v26.6.22 更名：以前稱為 **Session Placement** / **Session Key**（`sessionPlacement` / `sessionKey`）——現在為 **Session ID Placement** / **Session ID Key**（`sessionIDPlacement` / `sessionIDKey`）；核心已不再識別舊名稱。更新前儲存的 inbound 會自動遷移到新鍵——無需重新儲存。

建議：
- 對於大多數安裝，將**模式 = `auto`**、設定**Путь**/**Хост**，並（在透過 CDN 工作時）與客戶端協調這些值即可。
- 放置欄位（`*Placement`/`*Key`）與 padding 混淆僅在針對特定反 DPI/CDN 情境進行精細調整時才需要；當值為空時會使用括號中標示的 xray-core 預設值。
- 與客戶端/outbound 端相關的參數（例如重複 POST 的間隔、區塊大小）不會顯示在 inbound 表單中——監聽伺服器會忽略它們。相反地，XMUX 多工器在 inbound 表單中可用（見下文）。

- **不再填入服務性預設值。** 面板不再在 XHTTP 設定中寫入服務性預設值 `scMaxEachPostBytes` 與 `scMinPostsIntervalMs`——會套用 xray-core 的內部值。這消除了一個固定的 DPI 簽名（字面量 `scMinPostsIntervalMs=30`），先前流量可能因此被封鎖。對於已儲存的 inbound，與 xray-core 預設值相符的值不會輸出到連結與訂閱中（無需重新儲存 inbound）；手動設定的值會被保留。

**XHTTP（`auto` 模式）的 `streamSettings` 範例：**

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

對於大多數安裝，這四個欄位就足夠了；工作階段/序列放置與 padding 混淆欄位留空——此時會使用 xray-core 的預設值。

#### XMUX（連線多工）

**XMUX** 切換開關（`enableXmux`）會開啟多工層，將並行請求分配到一個小型物理連線池中。開啟時會展開六個可設定的欄位（儲存於 `xhttpSettings.xmux`）：

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| Max Concurrency | `maxConcurrency` | `16-32` | 單個連線的並行請求上限（範圍 `мин-макс`） |
| Max Connections | `maxConnections` | `0` | 物理連線的上限（`0` 為無限制） |
| Max Reuse Times | `cMaxReuseTimes` | `""`（空） | 連線重複使用的次數 |
| Max Request Times | `hMaxRequestTimes` | `600-900` | 單個連線的請求上限（範圍） |
| Max Reusable Secs | `hMaxReusableSecs` | `1800-3000` | 連線可供重複使用的時間（秒，範圍） |
| Keep Alive Period | `hKeepAlivePeriod` | `""`（空） | 保持連線的 keep-alive 週期 |

> **重要。** 不能同時設定 **Max Connections** 與 **Max Concurrency**——xray-core 會拒絕這樣的設定。預設情況下，開啟 XMUX 時面板會填入 `Max Concurrency = 16-32`；如果您設定了 **Max Connections**（值大於 `0`），面板會移除預設的 `Max Concurrency` 值以避免衝突。

---

### 6.8. Hysteria 傳輸（`hysteriaSettings`）

**Hysteria** 傳輸不在「Транспорт」列表中選擇：它在 inbound 以 Hysteria 協定建立時自動啟用，對其他協定則隱藏（離開 Hysteria 協定時網路會強制回到 `tcp`）。參數：

| 欄位 | 鍵 | 預設 | 描述 |
| --- | --- | --- | --- |
| 版本 | `version` | `2`（已固定，欄位鎖定） | Hysteria 版本。僅支援 Hysteria 2 |
| UDP idle timeout（秒） | `udpIdleTimeout` | `60` | UDP 工作階段的閒置逾時（秒）。允許範圍為 2–600；xray-core 在啟動時會拒絕此區間外的值 |
| Masquerade | `masquerade` | 關閉（不存在） | 開啟在探測時將監聽器偽裝成 HTTP/3 伺服器 |

開啟 **Masquerade** 時會出現類型選擇（`type`）以及依其而定的欄位：

- **`""` — default (404 page)**：傳回標準的 404 頁面（無需額外欄位）。
- **`proxy` (reverse proxy)**：反向代理到外部網站。
  - `url`（**Upstream URL**，placeholder `https://www.example.com`）——目標位址；
  - `rewriteHost`（**Переписать Host**，預設 `false`）——替換 `Host` 標頭；
  - `insecure`（**Пропустить TLS verify**，預設 `false`）——不驗證上游的 TLS 憑證。
- **`file` (serve directory)**：從目錄提供檔案。
  - `dir`（**Директория**，placeholder `/var/www/html`）。
- **`string` (fixed body)**：固定的 HTTP 回應。
  - `statusCode`（**Код статуса**，預設 `0`，範圍 0–599）；
  - `content`（**Body**）——回應主體；
  - `headers`（**Заголовки**）——`名稱 → 值` 映射。

Masquerade 讓基於 Hysteria 的 inbound 對主動探測看起來像普通的 HTTP/3 伺服器，從而提高隱蔽性。預設情況下偽裝為關閉。

**帶反向代理（`masquerade` → `proxy`）的 `hysteriaSettings` 範例：**

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

此處在探測時監聽器會傳回來自 `https://www.example.com` 的回應，偽裝成普通的 HTTP/3 網站。

---

### 6.9. 相關參數

除了選擇網路之外，同一個分頁中還有兩個不依賴於特定傳輸的通用區塊（詳見相應章節）：

- **External Proxy**（`externalProxy`）——一組外部位址/連接埠，會在訂閱連結中替換面板本身的位址。
- **Sockopt**（`sockopt`）——低階的 socket 選項（TCP Fast Open、mark、域策略、透明代理等）。

#### Real client IP（在 CDN/中繼之後判定真實 IP）

當 inbound 位於中介之後（如 Cloudflare 這類 CDN、L4 隧道/中繼或另一個面板）時，Xray 看到的是中介的位址，而非真實訪客。此位址會進入線上客戶端列表，並依它計算每個客戶端的 IP 限制，因此兩者在代理之後都變得無用。為了還原真實 IP，inbound 表單的 **Sockopt** 區段中有 **Real client IP** 預設集的選擇，它整合了 `acceptProxyProtocol` 與 `trustedXForwardedFor` 的設定：

| 預設集 | 作用 | 何時套用 |
| --- | --- | --- |
| **Off / direct** | 清除兩個欄位。 | inbound 直接對客戶端開放 |
| **Cloudflare CDN** | 設定 `sockopt.trustedXForwardedFor = ["CF-Connecting-IP"]`。 | 位於 Cloudflare CDN（橙色雲）之後的 WebSocket / HTTPUpgrade / XHTTP / gRPC |
| **L4 relay / Spectrum (PROXY)** | 開啟 `acceptProxyProtocol = true`。 | inbound 前的 L4 隧道/中繼，或 Cloudflare **Spectrum** |

各預設集互斥：選擇一個會清除另一個的欄位，因此過時的 `trustedXForwardedFor` 不會蓋過依 PROXY 協定還原的 IP。預設集下方仍會顯示「原始」的 **Proxy Protocol** 切換開關與 **Trusted X-Forwarded-For** 列表——預設集只是替您填寫它們，必要時可手動修改。如果所選預設集不被目前的傳輸支援（例如在 mKCP 上使用 PROXY 協定），表單會顯示警告。這些欄位僅與伺服器端相關，**絕不會在訂閱中發送給客戶端**。

> **只用其中一種。** `acceptProxyProtocol` 從 L4 的 PROXY 協定標頭讀取真實 IP，而 `trustedXForwardedFor` 從 HTTP 請求標頭讀取；只有在您的中介鏈確實需要時才值得手動混用它們。
- **FinalMask**（`finalmask`）——通用的傳輸層混淆機制（包括 mKCP 的 legacy 混淆），它取代了網路子表單內部的獨立「seed」/「header type」欄位。

---

## 7. 連線安全性：TLS、XTLS 與 REALITY

每一個支援透過 transport-flow 傳輸的 inbound（VMess、VLESS、Trojan、Shadowsocks、Hysteria），在編輯器中都有一個**「安全性」**分頁。在此分頁中可設定傳輸通道究竟如何加密與偽裝。共有三種模式，透過單選按鈕切換：

| 模式 | UI 中的標籤 | 何時可用 |
|-------|--------------|----------------|
| `none` | **無** | 始終可用（Hysteria 除外，它強制要求 TLS） |
| `tls` | **TLS** | 對於 `tcp`、`ws`、`http`、`grpc`、`httpupgrade`、`xhttp` 網路上的 VMess/VLESS/Trojan/Shadowsocks；對於 Hysteria 則始終可用 |
| `reality` | **Reality** | 僅限 `tcp`、`http`、`grpc`、`xhttp` 網路上的 VLESS/Trojan |

如果協定為 Hysteria（它強制要求 TLS），則不顯示**無**按鈕。**Reality** 按鈕僅在協定與網路為允許的組合時才會出現（見上表）。

切換模式時，面板會完整重建 `streamSettings` 區塊：移除前一模式的 `tlsSettings` 與 `realitySettings`，並填入所選模式的預設值。具體而言，選擇 **Reality** 時面板會立即自動：從內建的熱門網域清單中填入一組隨機的 `target` + `serverNames`（SNI），產生隨機的 `shortIds`，並向伺服器請求一組全新的 X25519 金鑰對（privateKey/publicKey）。

### 7.1. 差異何在：TLS vs XTLS vs REALITY

- **TLS** — 採用 TLS 1.2/1.3 協定的傳統傳輸加密。伺服器上必須放有有效的憑證（自有網域 + 憑證鏈）。流量看起來像普通的 HTTPS，但對於主動審查者而言，與你的網域之間可辨識的 TLS-handshake 是其特徵；當依 SNI 進行「定點封鎖」或缺少受信任憑證時，連線會被封鎖／回傳錯誤。

- **XTLS (Vision)** — 它不是「安全性」清單中的獨立模式，而是疊加於 TLS **或** Reality 之上的 *flow* 機制。在 inbound 的客戶端側透過 **Flow** = `xtls-rprx-vision`（或 `xtls-rprx-vision-udp443`）欄位啟用。當 `security = tls` 或 `security = reality` 時，Vision 可用於 `tcp` 網路上的 VLESS；此外，當啟用 VLESS 加密（vlessenc / ML-KEM）時，也可用於疊加在 `xhttp` 傳輸之上的 VLESS——這種情況下 **Flow** 欄位同樣可以設為 `xtls-rprx-vision`，且該值會正確寫入 `vless://` 連結（`flow=xtls-rprx-vision`）。Vision 降低了「雙重加密」（TLS-in-TLS），在握手之後直接傳遞有效負載，從而加快傳輸並改善偽裝。因此，**VLESS + Reality + Flow `xtls-rprx-vision`** 這套組合被視為當前推薦的現代配置。

- **REALITY** — 一種無需自有憑證的偽裝機制。伺服器「借用」一個真實第三方網站的 TLS 握手（`target`/`serverNames`），因此對觀察者而言，連線與存取該網站無法區分，且根本不需要憑證。驗證建立於 X25519 金鑰對與一組 `shortIds` 之上。REALITY 能抵禦主動探測（`active probing`）與依 SNI 的封鎖，因為 SNI 指向的是真實的外部網域。代價是對設定有更嚴格的要求（正確的帶連接埠 `target`、與客戶端的金鑰同步）。

簡短的選擇規則：
- 有自有網域與有效憑證，需要簡潔的 HTTPS 外觀 → **TLS**（盡可能搭配 Vision）；
- 沒有網域／憑證，或需要對 DPI 達到最高隱蔽性 → **REALITY**（對 VLESS/TCP 搭配 Vision）。

### 7.2. 「無」模式（`none`）

傳輸不帶 TLS 外殼進行：`streamSettings` 中的 `tlsSettings` 與 `realitySettings` 區塊會被排除。此模式沒有額外欄位。適用於以下情況：
- inbound 僅在 `127.0.0.1` 上監聽並充當 fallback 目標（依面板規則，作為 fallback 的子 inbound 應在 `127.0.0.1` 上以 `security=none` 監聽）；
- 加密／偽裝由外部層提供（例如面板前方的 Nginx 反向代理）；
- 在內部網路中使用具有自身加密的協定（Shadowsocks）。

對於可從外部存取的 inbound，不建議使用「無」模式。

**範例：`tcp` 網路上 TLS 的 `streamSettings` 區塊**（VLESS/Trojan/VMess）。選擇 **TLS** 模式並填寫 SNI 與憑證路徑後，結果如下：

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

`tlsSettings` 區塊的欄位。預設值取自面板的結構定義。

#### 主要參數

| 欄位（標籤） | 預設值 | 描述 |
|----------------|----------------------|----------|
| **SNI** (`serverName`) | `""`（空） | Server Name Indication — 在 TLS 握手中提交的網域名稱。必須與憑證的網域一致。英文提示佔位文字：「Server Name Indication」。 |
| **Cipher Suites** (`cipherSuites`) | `""` → **Auto** | 允許的加密套件清單。預設為空——選擇交由 Xray/Go 自行決定（**Auto** 選項）。僅在需要明確限制加密套件時才更改。 |
| **最小/最大版本** (`minMaxVersion`) | min = `1.2`，max = `1.3` | TLS 的最小與最大版本。可用值：`1.0`、`1.1`、`1.2`、`1.3`。建議保留 `1.2`–`1.3`；不宜將下限降至 1.0/1.1（已過時、不安全的版本）。 |
| **uTLS** (`settings.fingerprint`) | `chrome`（表單中提供 **None** = `""` 選項） | 模擬的客戶端 hello 之 TLS 指紋（uTLS fingerprint），使握手看起來像熱門瀏覽器。見下方清單。在 TLS 中清單的第一項為 **None** (`""`)，停用模擬。 |
| **ALPN** (`alpn`) | `["h2", "http/1.1"]` | 在 TLS 中協商的應用層協定清單（多選）。允許值：`h3`、`h2`、`http/1.1`。預設提供 `h2` 與 `http/1.1`。 |

**uTLS fingerprint** 的可能值（TLS 與 REALITY 相同）：`chrome`、`firefox`、`safari`、`ios`、`android`、`edge`、`360`、`qq`、`random`、`randomized`、`randomizednoalpn`、`unsafe`。在 TLS 表單中另外提供空白的 **None** 選項（不套用指紋模擬）。

**Cipher Suites** 的可用值（TLS 1.3 與 ECDHE 套件）：`TLS_AES_128_GCM_SHA256`、`TLS_AES_256_GCM_SHA384`、`TLS_CHACHA20_POLY1305_SHA256`、`TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`、`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`、`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`、`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`、`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`、`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`、`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`、`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`、`TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`、`TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`。

#### TLS 開關

| 開關 | 預設 | 描述 |
|---------------|--------------|----------|
| **拒絕未知 SNI** (`rejectUnknownSni`) | 關閉 (`false`) | 若啟用，當客戶端提交的 SNI 與憑證中的名稱不符時，伺服器將中斷連線。提升隱蔽性（伺服器不回應「外來」請求），但要求客戶端 SNI 精確一致。 |
| **停用 System Root** (`disableSystemRoot`) | 關閉 (`false`) | 停用對系統受信任根憑證儲存區的使用。 |
| **工作階段恢復** (`enableSessionResumption`) | 關閉 (`false`) | 啟用 TLS 工作階段恢復（session resumption / session tickets）。 |

#### TLS 進階參數（vcn、曲線、金鑰日誌、ECH Sockopt）

在 TLS 主要設定之下還有額外欄位可用。

| 欄位（標籤） | 預設 | 描述 |
|----------------|--------------|----------|
| **Verify Peer Cert By Name** (`settings.verifyPeerCertByName`) | `""` | 客戶端用來驗證伺服器憑證（取代 SNI）的名稱（以逗號分隔）。這是已於 2026-06-01 之後從 Xray 移除的 `allowInsecure` 欄位之現代替代品。此值僅供面板使用：不寫入伺服器上的 xray 設定，但會傳入邀請連結與訂閱（`vcn=…`），以便客戶端自行套用。佔位文字：`example.com`。 |
| **Curve Preferences** (`curvePreferences`) | `""` | 限制並依偏好順序排列 TLS 金鑰交換曲線（例如 `X25519MLKEM768`、`X25519`）。為空時——採用 Xray-core 的預設值。 |
| **Master Key Log** (`masterKeyLog`) | `""` | 以 `SSLKEYLOGFILE` 格式寫入 TLS master keys 的路徑（除錯時用於在 Wireshark 中解密流量）。佔位文字：`/path/to/sslkeylog.txt`。在正式環境中應保持為空——該檔案能解密所有流量。 |
| **ECH Sockopt** (`echSockopt`) | 關閉 | 帶有連線通訊端參數的開關，Xray 透過該連線請求 ECH config list。啟用時可用：**Dialer Proxy** (`dialerProxy` — 依標籤將請求轉送至指定的 outbound)、**Domain Strategy** (`domainStrategy`)、**TCP Fast Open** (`tcpFastOpen`)、**Multipath TCP** (`tcpMptcp`)。非必要時應保持關閉。 |

`verifyPeerCertByName`、`curvePreferences`、`masterKeyLog` 與 `echSockopt` 欄位位於 `tlsSettings` 的最上層，並能在儲存設定時面板欄位的「修剪」過程中保留下來。

#### 憑證

**SSL 憑證**區段（UI 中標題為「SSL-憑證」）以清單形式設定：用 **+** 按鈕新增一筆憑證記錄，用 **− 刪除** 按鈕移除（刪除按鈕僅在記錄多於一筆時可用）。啟用 TLS 時預設會建立一筆空白記錄。

每筆記錄都有一個輸入模式切換 (`useFile`)：

- **憑證路徑**（值 `useFile = true`，預設）——指定伺服器上的檔案路徑：
  - **公開金鑰** (`certificateFile`) — 憑證檔案的路徑（`.crt`/`.pem`）；
  - **私密金鑰** (`keyFile`) — 私密金鑰檔案的路徑（`.key`）。
- **憑證內容**（值 `useFile = false`）——內容直接貼入欄位（多行文字區域）：
  - **公開金鑰** (`certificate`) — 憑證的 PEM 內容；
  - **私密金鑰** (`key`) — 金鑰的 PEM 內容。

在「憑證路徑」模式的欄位下方有兩個按鈕：
- **安裝面板憑證** — 將面板自身的 SSL 憑證路徑填入欄位。對於中央面板上的 inbound，取用的是其憑證（`POST /panel/setting/all` → `webCertFile`/`webKeyFile`）；對於指派至節點的 inbound，取用的是節點自身的憑證（`GET /panel/api/nodes/webCert/{nodeId}`），因為中央面板的路徑在節點上並不存在。如果未設定憑證，將顯示警告：「*面板尚未設定憑證。請先在「設定」中安裝。*」（面板憑證本身在「設定 → 安全性」區段中設定）。
- **清除** — 抹除兩個路徑。

每筆憑證記錄的額外欄位：

| 欄位 | 預設 | 描述 |
|------|--------------|----------|
| **OCSP Stapling** (`ocspStapling`) | `0`（關閉） | OCSP stapling 的更新間隔（秒）（最小 `0`）。對於新的 inbound 預設為關閉（`0`）：這可消除對於沒有 OCSP responder 的憑證（例如已放棄 OCSP 的 Let's Encrypt）在 xray 日誌中的錯誤。僅對支援 stapling 的憑證啟用。 |
| **一次性載入** (`oneTimeLoading`) | 關閉 (`false`) | 若啟用，憑證在啟動時從磁碟讀取一次，當檔案變更時不會重新讀取。 |
| **使用選項** (`usage`) | `encipherment` | 憑證的用途。允許：`encipherment`（加密——一般的伺服器憑證）、`verify`（驗證）、`issue`（簽發——伺服器自行簽署／簽發憑證）。 |
| **Build Chain** (`buildChain`) | 關閉 (`false`) | **僅**在 `usage = issue` 時顯示。補全憑證鏈。 |

> inbound 編輯器中沒有自簽憑證的獨立按鈕：面板不會為 inbound 即時產生自簽憑證。憑證要麼以路徑／內容指定，要麼用「安裝面板憑證」按鈕從面板設定中拉取。面板自身 SSL 憑證的簽發／取得（包括上傳檔案與綁定網域）在 **設定 → 安全性** 區段中執行；此處沒有針對 inbound 的 ACME/Let's Encrypt 端點。

#### ECH 與憑證固定（TLS 進階欄位）

| 欄位 | 預設 | 描述 |
|------|--------------|----------|
| **ECH key** (`echServerKeys`) | `""` | Encrypted Client Hello 的伺服器金鑰。 |
| **ECH config** (`settings.echConfigList`) | `""` | ECH config list（客戶端部分，會寫入連結）。 |
| **對端憑證的 SHA-256** (`settings.pinnedPeerCertSha256`) | `[]` | 對端憑證的 SHA-256 雜湊（hex 字串，以逗號分隔）。原文提示：「*對端憑證的 SHA-256 雜湊，以十六進位字串表示（例如 e8e2d3…），以逗號分隔。僅供面板使用——不寫入 xray 伺服器設定，但會包含於邀請連結中，使客戶端能固定憑證。*」 |

按鈕：
在 **對端憑證的 SHA-256** 欄位旁有兩個自動填入按鈕：
- **Fill from this inbound's certificate**（盾牌圖示）——填入此 inbound 自身憑證的 SHA-256 雜湊（透過 `getCertHash` 端點在本機取得）。
- **Fetch the hash by pinging the SNI (xray tls ping)**（下載圖示）——透過依指定 SNI 進行 TLS 連線（在伺服器上呼叫 `getRemoteCertHash`），取得伺服器即時憑證的雜湊。**SNI** (`serverName`) 欄位必須已填寫——否則會顯示提示「*Set the SNI (serverName) first to ping the remote certificate.*」

取得的雜湊會新增至欄位（以逗號分隔）並寫入邀請連結，使客戶端能固定憑證。
- **取得新的 ECH 憑證** — 向伺服器請求一組對應當前 SNI 的新 ECH 配對（`POST /panel/api/server/getNewEchCert`，伺服器上執行 `xray tls ech --serverName <SNI>`）；填入 **ECH key** 與 **ECH config** 欄位。
- **清除** — 將兩個 ECH 欄位歸零。

### 7.4. REALITY 模式

`realitySettings` 區塊的欄位。REALITY 不使用 SSL 憑證：取而代之的是借用的外部網域 TLS 握手與一組 X25519 金鑰。

#### 偽裝參數

| 欄位（標籤） | 預設值 | 描述 |
|----------------|----------------------|----------|
| **顯示** (`show`) | 關閉 (`false`) | 將 REALITY 的除錯輸出寫入 Xray 日誌。通常保持關閉。 |
| **Xver** (`xver`) | `0` | 傳遞至後端的 PROXY 協定版本（`0` — 關閉）。最小 `0`。 |
| **uTLS** (`settings.fingerprint`) | `chrome` | 模擬的 TLS 指紋（與 TLS 中相同的清單，但不含空白的 None 選項）。 |
| **目標** (`target`) | `""`（啟用時面板會填入隨機值） | **必填欄位。** REALITY 借用其 TLS 握手的真實網域。原文提示：「*必填。必須包含連接埠（例如 example.com:443）。沒有連接埠時 Xray-core 不會啟動。*」面板的驗證會檢查連接埠是否存在且正確；否則會給出錯誤「REALITY 目標為必填」／「REALITY 目標必須包含連接埠…」／「REALITY 目標指定了無效的連接埠」。旁邊的更新按鈕會從內建清單中填入隨機配對。 |
| **SNI** (`serverNames`) | `[]`（與目標一同填入） | 允許的 SNI 清單（以標籤形式多項輸入）。必須與 **目標** 中的網域相符。更新按鈕會連同隨機目標一起填入 SNI。 |
| **最大時間差（毫秒）** (`maxTimediff`) | `0` | 客戶端與伺服器時鐘允許的最大偏差（毫秒）（`0` — 無限制）。最小 `0`。 |
| **最低客戶端版本** (`minClientVer`) | `""` | Xray 客戶端的最低版本（佔位文字 `25.9.11`）。為空——無限制。 |
| **最高客戶端版本** (`maxClientVer`) | `""` | Xray 客戶端的最高版本。為空——無限制。 |
| **Short IDs** (`shortIds`) | `[]`（啟用時產生） | 區分客戶端的短識別碼（hex）清單。以標籤形式多項輸入；更新按鈕會產生隨機的一組。 |
| **SpiderX** (`settings.spiderX`) | `/` | 「蜘蛛」路徑（REALITY 的客戶端部分），在模擬存取外部網站時使用。會寫入邀請連結。 |

啟用 REALITY 時以及按更新按鈕時，**目標** (`target`) 與 **SNI** (`serverNames`) 會從面板的內建清單中填入一組隨機配對：`www.amazon.com`、`aws.amazon.com`、`www.oracle.com`、`www.nvidia.com`、`www.amd.com`、`www.intel.com`、`www.sony.com`（每個都帶 `:443` 連接埠）。請選擇一個「分量足」、穩定的第三方 HTTPS 網站，且不位於你自己的伺服器之後。

**範例：`tcp` 網路上 REALITY 的 `streamSettings` 區塊**（VLESS）。不需要憑證——取而代之的是借用的網域與一組 X25519 金鑰：

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

此處面板的 **目標** (`target`) 欄位對應到最終 Xray 設定中的 `dest`。如果某個 REALITY inbound 是以 `dest` 鍵中的 destination 建立的（由舊版面板、透過 API 或外部工具），面板在解析時會在 `target` 為空的情況下將 `dest` → `target` 正規化——因此這類 inbound 能正確載入，**目標** 欄位不會變成空白，且重新儲存不會破壞運作中的 REALITY。

#### REALITY 金鑰（X25519）

| 欄位 | 預設 | 描述 |
|------|--------------|----------|
| **公開金鑰** (`settings.publicKey`) | `""` | X25519 公開金鑰（客戶端將其放入自己的設定／連結中）。 |
| **私密金鑰** (`privateKey`) | `""` | X25519 私密金鑰（僅保存於伺服器上）。 |

金鑰下方的按鈕：
- **取得新憑證** — 向伺服器請求一組新的金鑰對（`GET /panel/api/server/getNewX25519Cert`；伺服器上執行 `xray x25519`），填入 **私密金鑰** 與 **公開金鑰**。首次啟用 REALITY 模式時也會自動產生這同一組配對。

**範例：透過 API 取得 X25519 金鑰對**（在表單之外，例如供腳本使用）。此請求會回傳私密金鑰與公開金鑰：

```bash
curl -s -b cookie.txt https://your-panel:2053/panel/api/server/getNewX25519Cert
# Ответ:
# {"success":true,"obj":{"privateKey":"...","publicKey":"..."}}
```

`cookie.txt` — 透過 `POST /login` 登入後取得的工作階段 cookie 檔案。
- **清除** — 將兩個金鑰歸零。

#### 後量子簽章 ML-DSA-65 (mldsa65)

REALITY 的額外（非必要）後量子驗證層：

| 欄位 | 預設 | 描述 |
|------|--------------|----------|
| **mldsa65 Seed** (`mldsa65Seed`) | `""` | ML-DSA-65 金鑰的伺服器 seed。 |
| **mldsa65 Verify** (`settings.mldsa65Verify`) | `""` | 驗證值（客戶端部分，會寫入連結）。 |

按鈕：
- **取得新的 Seed** — 請求一組新配對（`GET /panel/api/server/getNewmldsa65`；伺服器上執行 `xray mldsa65`），填入 **mldsa65 Seed** 與 **mldsa65 Verify**。
- **清除** — 將兩個欄位歸零。

#### fallback 速率限制與 REALITY 金鑰日誌

在 REALITY 設定中可對 fallback 流量進行速率限制——它能阻止主動探測將伺服器當作通往借用網域的免費通道。此設定為兩個方向分別設定——**Limit Fallback Upload** 與 **Limit Fallback Download** (`limitFallbackUpload` / `limitFallbackDownload`)，每一個都有相同的一組欄位：

| 欄位（標籤） | 預設 | 描述 |
|----------------|--------------|----------|
| **After Bytes** (`afterBytes`) | `0` | 在開始限制之前以全速放行多少位元組。`0` — 從第一個位元組起就限制。 |
| **Bytes Per Sec** (`bytesPerSec`) | `0` | 超過門檻後 fallback 流量的速率上限（位元組/秒）。`0` — 無限制（停用此方向）。 |
| **Burst Bytes Per Sec** (`burstBytesPerSec`) | `0` | 用於短暫突發、超出穩定速率的餘量（token-bucket 大小）。若小於 **Bytes Per Sec**，會被提升至其值。 |

同處還新增了 **Master Key Log** (`masterKeyLog`) 欄位——以 `SSLKEYLOGFILE` 格式寫入 TLS master keys 的路徑，供在 Wireshark 中除錯；在正式環境中應保持為空。

### 7.5. 設定的實務建議

1. **VLESS + Reality（推薦）：** 在 `tcp` 網路上建立一個 VLESS inbound，在「安全性」分頁選擇 **Reality**——面板會自行填入隨機的 `target`/SNI、`shortIds` 並產生 X25519 金鑰。如有需要，按「取得新憑證」以取得你自己的金鑰對。對於 VLESS 客戶端，啟用 **Flow** = `xtls-rprx-vision`（XTLS Vision）——這將帶來最高的效能與隱蔽性。

**範例：最終的 VLESS + Reality + Vision 客戶端連結。** 面板為這類 inbound 所產出的邀請連結如下（金鑰／ID 的值為示意）：

```text
vless://uuid-клиента@1.2.3.4:443?type=tcp&security=reality&pbk=ПУБЛИЧНЫЙ_КЛЮЧ&fp=chrome&sni=www.nvidia.com&sid=6ba85179e30d4fc2&spx=%2F&flow=xtls-rprx-vision#my-reality
```

此處 `pbk` — X25519 公開金鑰，`sni` — 來自 **目標** 的借用網域，`sid` — 其中一個 **Short IDs**，`flow=xtls-rprx-vision` — 已啟用的 XTLS Vision。
2. **使用自有網域的 TLS：** 選擇 **TLS**，在 **SNI** 中填入網域名稱，新增憑證（以檔案路徑或內容），或者，如果網域與憑證已在「設定 → 安全性」中設定好，則按「安裝面板憑證」。將 **最小/最大版本** 保留為 `1.2`–`1.3`，**uTLS** 保留為 `chrome` 以偽裝成普通瀏覽器。
3. 對於對外開放的 inbound，請勿保留 **無** 模式——僅在本機 fallback 目標（`127.0.0.1`）或當 TLS 由外部代理提供時才使用它。
4. 介面中的建議：對於大多數進階欄位都有提示「*建議保留預設設定*」——僅在了解後果時才更改它們。

---

## 8. 用戶端

用戶端是 VPN 使用者的帳號：一組與一個或多個 inbound 綁定的憑證（UUID 或密碼），擁有自己的流量配額、有效期與同時連線數限制。在此分支中，用戶端是一個獨立的實體（資料表 `clients`）：同一個用戶端可以同時綁定到多個 inbound，並共用同一組 UUID/密碼與同一個流量計數器。**用戶端**區塊會顯示面板中所有的帳號（不論其所屬 inbound），並提供搜尋、篩選、排序與批次操作。

### 8.1. 用戶端欄位

下面逐一說明**新增用戶端** / **編輯用戶端**編輯器中的每個欄位。

用戶端表單分為兩個分頁：**基本**（email、inbound 綁定、限額、有效期、群組、備註、reverse tag）與**憑證**（UUID/密碼/auth、Flow、VMess Security）。在欄位標籤中，配額標示為 **流量限制 (ГБ)**，有效期則標示為 **時長 (天)** 與 **自動續期 (天)**；**流量限制 (ГБ)** 與 **IP 限制** 欄位帶有提示，說明 `0` 表示「無限制」。在編輯已存在的用戶端時，產生隨機 email 的按鈕會隱藏，而 IP 日誌按鈕則直接置於 **IP 限制** 欄位旁，並顯示已記錄的位址數量。

| 欄位 | JSON 鍵 | 預設值 | 說明 |
|------|-----------|--------------|----------|
| Email | `email` | —（必填） | 用戶端的唯一識別碼 |
| UUID | `id` | 自動產生 | VMess/VLESS 的識別碼 |
| 密碼 | `password` | 自動產生 | Trojan/Shadowsocks 的密碼 |
| 授權 | `auth` | 自動產生 | Hysteria 的密碼 |
| Flow | `flow` | 空 | Flow control（XTLS），僅限 VLESS |
| VMess Security | `security` | `auto` | VMess 加密方法 |
| IP 限制 | `limitIp` | `0`（無限制） | 同時連線的最大 IP 數 |
| 已上傳/下載合計 (ГБ) | `totalGB` | `0`（無限制） | 流量配額 |
| 有效期 | `expiryTime` | `0`（永久） | 到期日期 |
| 自動續期 | `reset` | `0`（關閉） | 流量重置週期，天 |
| Telegram 使用者 ID | `tgId` | `0`（無） | 數字型 Telegram ID |
| 訂閱 ID | `subId` | 自動產生 | 訂閱識別碼 |
| 群組 | `group` | 空 | 邏輯分組標籤 |
| 備註 | `comment` | 空 | 任意註記 |
| 已啟用 | `enable` | `true` | 帳號是否啟用 |

#### Email（識別碼）

**Email** 欄位是用戶端的主要且必填識別碼。雖然名稱如此，但它不一定是電子郵件位址：任何文字標籤皆可（使用者名稱、編號）。其值在面板範圍內必須是**唯一**的；嘗試以已被佔用的 email 建立第二個用戶端會被拒絕（`email already in use`），除非 `subId` 也相同（這會被視為對同一個用戶端的綁定）。

Email **不可留空**（`client email is required`），且**不能包含空格、`/`、`\` 字元以及控制字元**（「Email 不能包含空格、'/'、'\' 或控制字元」）。Email 會用於流量計算、IP 日誌、線上清單以及操作名稱中——不建議事後變更。

#### UUID / 密碼 / 授權（憑證）

具體使用哪個憑證欄位，取決於用戶端綁定的 inbound 所使用的協定。若欄位留空，值會自動填入：

- **UUID**（`id` 欄位）——用於 **VMess** 與 **VLESS** 協定。若未指定，會產生隨機的 UUID v4。
- **密碼**（`password` 欄位）——用於 **Trojan** 與 **Shadowsocks**。Trojan 預設產生不含連字號的 UUID。Shadowsocks 則依 inbound 的加密方法產生對應長度的 Base64 金鑰：`2022-blake3-aes-128-gcm` 為 16 位元組，`2022-blake3-aes-256-gcm` 與 `2022-blake3-chacha20-poly1305` 為 32 位元組；其他方法則為不含連字號的 UUID。若手動輸入的金鑰不符合 2022-blake3 方法，將被自動產生的金鑰取代。
- **授權**（`auth` 欄位）——**Hysteria** 的密碼。預設為不含連字號的 UUID。

由於一個用戶端可綁定到不同協定的 inbound，用戶端記錄中可能同時存在 UUID、密碼與 auth——每個協定使用各自的欄位。

**範例：用戶端的憑證在不同 inbound 的 `settings` 中的樣子。** 同一個用戶端在 VLESS inbound 中以 `id` 識別，在 Trojan 中以 `password` 識別，在 Shadowsocks 中以 `password`（Base64 金鑰）識別：

```json
// фрагмент settings.clients у VLESS-inbound
{ "id": "b831381d-6324-4d53-ad4f-8cda48b30811", "email": "user-a", "flow": "xtls-rprx-vision" }

// тот же клиент в Trojan-inbound
{ "password": "b831381d63244d53ad4f8cda48b30811", "email": "user-a" }

// тот же клиент в Shadowsocks-inbound (метод 2022-blake3-aes-256-gcm)
{ "password": "GPyOaA3f7CO0az53eaQ8eqMfRDjmBlOh7v1u3+Z+pHk=", "email": "user-a" }
```

#### Flow

**Flow**（`flow` 欄位）——XTLS 的流量控制。**僅適用於 VLESS**，且僅當 inbound 已配置為 XTLS Vision 時：VLESS 透過 **TCP** 傳輸，且 security 為 **`tls`** 或 **`reality`**。允許的值為 `xtls-rprx-vision`（以及歷史值 `xtls-rprx-vision-udp443`）；空值表示沒有 flow。

若 inbound 不支援 XTLS flow，所設定的 flow 會在儲存用戶端時**靜默清空**：對於綁定到多個 inbound 的同一個用戶端，flow 只會套用在允許的地方。只有在你刻意使用 VLESS-Vision 時才需要變更。

#### VMess Security

**VMess Security**（`security` 欄位）——VMess 酬載的加密方法。預設值為 `auto`（由 Xray 自行選擇加密器）。允許的值為 VMess 標準值：`auto`、`aes-128-gcm`、`chacha20-poly1305`、`none`、`zero`。其他協定不使用此欄位。

#### IP 限制（同時連線數）

**IP 限制**（`limitIp` 欄位）——用戶端可同時連線的**不同 IP 位址**的最大數量。預設值為 `0`，表示**無限制**。若為正值，面板會追蹤用戶端的活躍 IP，並在超過限制時透過背景任務停用該帳號。（自 **3.3.1** 起，IP 計數透過 Xray 核心的 online-stats API 進行，**不需要**存取日誌；在較舊版本的核心上，面板會退回讀取存取日誌，此時必須啟用該日誌。）可用於禁止將一個訂閱分享給多個裝置：例如 `2` 表示允許兩個裝置。

IP 限制透過 **Fail2ban** 機制實施，因此 **IP 限制** 欄位只有在 Fail2ban 已安裝且正常運作時才會啟用（面板透過 `GET /panel/api/server/fail2banStatus` 檢查其狀態）。若未安裝 Fail2ban，用戶端編輯器（以及批次新增表單）中的此欄位會被禁用，並在懸停時顯示提示，建議從 `x-ui` 的 bash 選單安裝 Fail2ban（「Fail2ban is not installed, so the IP limit cannot be enforced. Install Fail2ban from the x-ui bash menu to enable this option.」）；在 Windows 上，提示會說明 Fail2ban 在此不可用（「Fail2ban is not available on Windows, so the IP limit cannot be enforced.」），而若該功能在伺服器上被停用——「The IP limit feature is disabled on this server.」。在面板升級時，對於未安裝 Fail2ban 的伺服器上的用戶端，已儲存的 IP 限制會透過一次性遷移被清零，因為它在那裡本來就不會被套用。

**值範例。** `limitIp: 0`——無限制；`limitIp: 1`——嚴格僅允許一個裝置同時連線；`limitIp: 3`——最多三個不同 IP。當出現第四個活躍 IP 時，背景任務會停用該用戶端（`enable = false`），直到你執行 **重置 IP 限制** 為止。

相關操作：**IP 日誌** 顯示用戶端已記錄的 IP 清單；每筆記錄除了 IP 本身外，還包含最後一次存取的時間以及記錄該連線所經過的節點標記（`@ 節點名稱`）——在多面板配置中可看出用戶端是透過哪個節點連線的。**重置 IP 限制** 會清空累積的 IP 日誌，讓用戶端無需等待記錄自然過期即可再次連線。

#### 已上傳/下載合計 (ГБ) — 流量配額

**已上傳/下載合計 (ГБ)**（`totalGB` 欄位）——流量總配額（上傳 + 下載）。預設值 `0` 表示**無限制**。達到配額時（`up + down >= total`），用戶端視為**已耗盡**（depleted）並被停用。在 UI 中通常以 GB 為單位輸入；資料庫中以位元組儲存。

在用戶端清單中，**流量** 欄位會顯示彩色使用量條：已消耗的流量、限額標記（無限制時為 ∞ 符號），以及懸停時的提示（拆分為已上傳/已下載及剩餘量）。手機上的用戶端卡片也會顯示相同的精簡指示器。

#### 有效期（Expiry）

**有效期**（`expiryTime` 欄位）設定帳號的到期時刻。此欄位有三種模式：

- **永久**——`0`。用戶端永不依時間到期。
- **具體日期**——正的 Unix timestamp（以毫秒計）。到達時（`expiryTime <= 現在`），用戶端視為已過期（expired）並被停用。在 UI 中通常透過選擇日期或以天為單位的時長設定（**時長**，單位為**天**）。
- **首次使用後開始計時**——**負值**，用以編碼時長。在用戶端尚未傳輸任何位元組之前，有效期維持為負值（「延後開始」）。在第一次流量計算的 tick 時，面板會將其轉換為絕對日期：`現在 + |時長|`。這讓你可以販售例如「自首次連線起 30 天」的方案，而無需事先知道用戶端何時會啟用。轉換以 email 為單位執行一次，使所有綁定的 inbound 取得相同的有效期。

**有效期編碼範例。** 固定日期 2026 年 3 月 1 日 00:00 UTC → `expiryTime: 1772323200000`（正的毫秒 timestamp）。「自首次連線起 30 天」→ `expiryTime: -2592000000`（負值，`30 × 24 × 60 × 60 × 1000`）；在第一個流量位元組時，面板會將其替換為 `現在 + 2592000000`。永久 → `expiryTime: 0`。

#### 自動續期（用戶端流量重置週期）

**自動續期** 欄位（`reset` 欄位）是自動續期/重置的週期（以天為單位）。提示：「到期後自動續期。(0 = 關閉) (單位：天)」。

- `0`——自動續期**關閉**（預設值）。到期後用戶端就直接變為已耗盡。
- `> 0`——背景任務在到期時會**將流量計數器重置為零**（`up = down = 0`），**將有效期向前推移** `reset` 天（必要時推移多個週期，直到新的有效期落在未來），並在必要時重新**啟用**用戶端。這實現了週期性訂閱（例如按月）。自動續期**不適用於節點上的 inbound**（`node_id IS NOT NULL`）。

重要影響：帶有 `reset > 0` 的用戶端在批次刪除操作中會被**排除**於「已耗盡」概念之外——它們的流量/有效期理應由自動續期清零，而非使該帳號成為刪除候選。

#### Telegram 使用者 ID

**Telegram 使用者 ID**（`tgId` 欄位）——使用者的數字型 Telegram 識別碼，用於與面板內建的 Telegram 機器人綁定（通知、自助查看統計）。提示：「數字型 Telegram 使用者 ID (0 = 無)」。預設值 `0` 表示未綁定。此欄位可供篩選（**有** / **無**）。

#### 訂閱 ID（subId）

**訂閱 ID**（`subId` 欄位）——用戶端被納入**訂閱**（subscription）所使用的識別碼。所有具有相同 `subId` 的用戶端會透過同一條訂閱連結提供。若建立時留空，面板會**自動產生隨機**的 `subId`（UUID）。其值在不同 email 的用戶端之間必須是**唯一**的（`subId already in use`），並遵循與 email 相同的字元限制（「訂閱 ID 不能包含空格、'/'、'\' 或控制字元」）。

沒有 `subId`，用戶端的訂閱連結將無法使用（「此用戶端沒有 subId，無法提供分享連結。」）。

#### Links 分頁（外部連結與訂閱）

除了 **基本** 與 **憑證** 分頁外，用戶端編輯器還有第三個分頁 **Links**（提示：「Add third-party share links and remote subscription URLs to include in this client's subscription.」）。在此分頁中，透過 **Add External Link** 按鈕可加入第三方分享連結（`vless://`、`vmess://`、`trojan://`、`ss://`、`hysteria2://`、`wireguard://`），透過 **Add External Subscription** 按鈕則可加入遠端訂閱的 URL（例如 `https://provider.example/sub/…`）。

上述所有內容都會混入該用戶端的訂閱輸出（raw、JSON 與 Clash 格式）：連結會原樣加入，而遠端訂閱則由面板定期下載（帶快取與短逾時），並將其配置與自有配置合併。如此一來，在一條用戶端訂閱連結中，便可將自有伺服器與外部配置一併提供。

#### 群組

**群組**（`group` 欄位）——用於將相關用戶端歸類的邏輯標籤。提示：「用於分組相關用戶端的邏輯標籤（例如團隊、客戶、地區）。可從工具列篩選。」，佔位文字為「例如 customer-a」。此欄位為選填（預設為空）。可依群組篩選清單並執行批次操作；要清除用戶端的標籤，請使用 **取消分組** 動作。

也可以直接在單一用戶端編輯器中移除群組：若清空 **群組** 欄位並儲存，標籤會被正確移除，且該用戶端不再顯示在原先的群組下。

#### 備註

**備註**（`comment` 欄位）——供管理員使用的任意文字註記（預設為空）。其內容會納入搜尋，並可供篩選（**有** / **無** 備註）。

#### 已啟用

**已啟用**（`enable` 欄位）——帳號的啟用狀態旗標。預設為**已啟用**（`true`）；建立時即使未傳入此旗標，面板也會強制設為 `true`。已停用的用戶端（`enable = false`）無法連線，並在摘要中歸入**未啟用**（deactive）類別。面板會自動停用耗盡配額、已過期或超過 IP 限制的用戶端。

#### 唯讀欄位

用戶端卡片中也會顯示一些系統欄位：**建立時間**（`created_at`）與 **更新時間**（`updated_at`）——建立與最後修改的時間戳記，由系統自動填入且不可編輯。**Reverse tag** 欄位（`reverse`）為選填的 Reverse tag，用於簡易的 VLESS 反向代理（「選填的 Reverse tag」）。

### 8.2. 綁定到 inbound

每個用戶端至少必須綁定到一個 inbound——建立時至少需要一個（`at least one inbound is required`）。在編輯器中，這是 **已綁定的 inbound** 欄位，提示為 **選擇一個或多個 inbound**。

- **綁定**——將用戶端加入所選的 inbound（相同的 UUID/密碼與共用流量）。既有的綁定會保留。
- **解除綁定**——將用戶端從所選的 inbound 移除。用戶端記錄本身會保留（若要完整刪除，請使用 **刪除**）。對於用戶端未綁定的組合，會被靜默跳過。

在儲存綁定到多個 inbound 的用戶端時，與特定協定/傳輸不相容的欄位（例如 VLESS-Vision 之外的 Flow）會自動針對每個 inbound 調整為允許的值。

在 inbound 選擇清單上方（於用戶端表單、批次新增用戶端時，以及批次綁定/解除綁定的視窗中）有 **全選** 與 **清除** 按鈕。在這些清單中，每個 inbound 會以其備註（remark）標示（若有設定），否則以 inbound 的 tag 標示。

### 8.3. 用戶端操作

針對單一用戶端（透過 **用戶端資訊** 卡片或 **動作** 內容選單）可進行以下操作：

#### 查看資訊、QR 碼與連結

- **用戶端資訊**——包含所有欄位、已用/剩餘流量（**剩餘**）、有效期與已綁定 inbound 的卡片。

透過 API 查詢用戶端（`GET /panel/api/clients/get/:email`）時，除了 `client` 與 `inboundIds` 欄位外，還會額外回傳 `usedTraffic`——實際消耗的流量（上傳 + 下載，已計入節點資料），這讓消耗量與 `totalGB` 配額的比對更為簡便。
- **QR 碼** 與 **連結**——用於匯入用戶端應用程式的用戶端配置連結。依所有綁定且支援該協定的 inbound 產生（`GET /links/:email`）。若沒有合適的連結：「沒有可分享的連結——請先將用戶端綁定到支援該協定的 inbound。」。
- **訂閱連結**——依 `subId` 產生的訂閱 URL（`GET /subLinks/:subId`）。僅在用戶端具有 `subId` 且訂閱服務已在 **面板設定 → 訂閱** 中啟用時可用（否則「訂閱服務已停用。」）。此外還會提供 **JSON 訂閱 URL**。

#### 重置流量

**重置流量**（`POST /resetTraffic/:email`）會將特定用戶端的上傳/下載計數器（`up`、`down`）清零。配額（`totalGB`）與有效期**不受影響**——僅清空已使用的量。Toast：「流量已重置」。若用戶端未綁定任何 inbound：「請先將此用戶端綁定到 inbound。」。

**重置流量** 按鈕在用戶端編輯表單中也可使用——位於底部面板，與 **取消** / **儲存** 並列（重置前會要求確認）。若用戶端因流量耗盡而被停用，重置（單一與批次皆然）會自動重新**啟用**它（`enable = true`），並立即將此變更下發至節點——不再需要在主控端與節點上手動重新啟用用戶端。

#### 重置 IP 限制

清空用戶端累積的 IP 日誌（`POST /clearIps/:email`），以解除因超過同時連線數限制而造成的臨時封鎖。Toast：「日誌已清空」。

#### 刪除

**刪除**（`POST /del/:email`）——完整刪除用戶端。確認對話框：標題「刪除用戶端 {email}？」，內文「用戶端將從所有已綁定的 inbound 中移除，其流量記錄也會被銷毀。此動作無法復原。」。刪除會將用戶端從**所有** inbound 移除，並銷毀其流量記錄。Toast：「用戶端已刪除」。

### 8.4. 批次操作

在用戶端清單中可勾選多筆記錄（**全選**、**全部清除**）；計數器為「已選 {count}」。針對所選項目可進行：

- **刪除 ({count})**（`POST /bulkDel`）——批次刪除。確認：「刪除 {count} 個用戶端？」、「每個所選用戶端都會從所有已綁定的 inbound 中移除，其流量記錄也會被銷毀。此動作無法復原。」。Toast：「已刪除用戶端：{count}」，部分失敗時為「已刪除：{ok}，失敗：{failed}」。
- **修改 ({count})** / **調整**（`POST /bulkAdjust`）——批次修改有效期與/或配額。對話框「修改 {count} 個用戶端」帶有提示「正值表示增加，負值表示減少。有效期或流量無限制的用戶端會在對應欄位上被跳過。」。欄位：**增加天數** 與 **增加流量 (ГБ)**。邏輯如下：
  - **有效期：** 有效期為永久的用戶端（`expiryTime == 0`）會被跳過（「unlimited expiry」）；對於有日期的用戶端，有效期會推移指定的天數；對於「首次使用後開始計時」模式（負值有效期）的用戶端，則調整其等待時長。超出剩餘量的減少會被跳過（「reduction exceeds remaining time/delay window」）。
  - **流量：** 無限制的用戶端（`totalGB == 0`）會被跳過（「unlimited traffic」）；否則配額會變更指定的量，且不會低於零。
  - 若天數與流量皆未指定：「套用前請指定天數或流量。」。Toast：「已修改：{count}」/「已修改：{ok}，已跳過：{skipped}」。

**範例：將所選用戶端延長 30 天並增加 50 GB。** 在 **修改** 對話框中指定 **增加天數** = `30`、**增加流量 (ГБ)** = `50`。反之，若要扣除一週並削減 10 GB 配額，請輸入負值：**增加天數** = `-7`、**增加流量 (ГБ)** = `-10`（有效期為永久或流量無限制的用戶端會在對應欄位上被跳過）。
- **綁定 ({count})** / **解除綁定 ({count})**（`POST /bulkAttach` / `bulkDetach`）——將所選用戶端批次綁定/解除綁定至所選 inbound。目標僅限多使用者 inbound。解除綁定結果：「已解除綁定 {detached}，已跳過 {skipped}。」。
- **Sub 連結 ({count})**——所選用戶端訂閱 URL 與 JSON 訂閱的彙總表格，帶有 **全部複製** 按鈕。若沒有任何用戶端具有 subId：「所選用戶端中沒有任何一個具有訂閱 ID。」。
- **加入群組** 與 **取消分組**——指派與移除群組標籤。

#### 依狀態重置流量與刪除

- **重置所有用戶端流量**（`POST /resetAllTraffics`）——將面板中**所有**用戶端的 `up`/`down` 計數器清零。確認：「重置所有用戶端流量？」及「所有用戶端的上傳/下載計數器將重置為零。配額與有效期不受影響。此動作無法復原。」。Toast：「所有用戶端流量已重置」。
- **刪除已耗盡的用戶端**（`POST /delDepleted`）——刪除所有**配額已耗盡**（`total > 0 and up + down >= total`）**或已過期**（`expiry_time > 0 and expiry_time <= 現在`）的用戶端，前提是 `reset = 0`（帶自動續期的用戶端不受影響）。確認：「刪除已耗盡的用戶端？」、「所有流量配額已耗盡或有效期已過的用戶端都會被刪除。此動作無法復原。」。Toast：「已刪除已耗盡的用戶端：{count}」。

#### 匯出、匯入與刪除未綁定的用戶端

當未勾選任何項目時，在 **用戶端** 頁面的 **更多** 選單中可進行三項操作。

**匯出用戶端**（`GET /clients/export`）會開啟一個檢視器，以 `{client, inboundIds}` 格式顯示所有用戶端的 JSON 清單，並帶有複製與下載按鈕（檔案 `clients-export.json`）。**匯入用戶端**（`POST /clients/import`）會開啟一個編輯器，貼入相同的 JSON 後按 **Import**：帶有 `inboundIds` 的用戶端會被建立並綁定到 inbound，沒有綁定的用戶端則以獨立的「裸」記錄還原，而已存在的 email **絕不會被覆寫**——它們會被列入跳過清單。Toast：「{count} clients imported」、「{ok} imported, {failed} skipped」。

**刪除未綁定的用戶端**（`POST /clients/delOrphans`）——危險操作：刪除所有未綁定任何 inbound 的用戶端，連同其流量記錄、IP 日誌與外部連結。確認：「Delete clients without an inbound?」、「Removes every client that is not attached to any inbound, along with its traffic record. This cannot be undone.」。Toast：「{count} unattached clients deleted」。此動作無法復原。

### 8.5. 搜尋、篩選與排序

清單上方有一個搜尋列（「搜尋 email、備註、sub ID、UUID、密碼、auth…」）——它會依 email、備註、subId、UUID、密碼與 auth 搜尋。結果計數器：「顯示 {total} 中的 {shown} 筆」。

用戶端清單會自動更新：面板每隔幾秒重新拉取當前頁面的最新資料，因此新連線的用戶端與變更後的排序順序無需手動重新整理即會出現（背景輪詢時載入指示器不會閃爍）。

**用戶端篩選** 面板可依狀態（類別）、協定、已綁定 inbound、有效期範圍、已使用流量範圍、是否有自動續期（**有/無**）、是否有 Telegram ID 與備註，以及依群組進行篩選。在帶有節點的面板上，會出現 **節點** 多選：可將清單限定為所選節點的用戶端；另有一個單獨的 **本機面板** 項目，用以篩選未綁定節點的 inbound 的用戶端（此篩選僅在有節點時可見）。排序：**舊到新/新到舊**、**最近更新**、**最近上線**、**Email А→Я / Я→А**、**流量較多**、**剩餘較多**、**較快到期**。

### 8.6. 圖示與狀態

狀態優先順序：已耗盡/已過期 → 未啟用 → 即將到期 → 活躍。

- **在線** / **離線**——具有活躍連線（存在於當前線上清單中）且**已啟用**的用戶端。線上清單透過獨立的請求更新（`/onlines`、`/onlinesByGuid`）。
- **已耗盡**（depleted）——配額已用盡（`up + down >= totalGB`）**或**有效期已過（`expiryTime <= 現在`）。這類用戶端會自動停用，並受 **刪除已耗盡的用戶端** 動作影響。
- **即將到期 / 即將用盡**（expiring）——已啟用的用戶端，距離有效期屆滿不足門檻區間**或**距離配額耗盡不足門檻量（門檻在面板設定中設定）。若用戶端已耗盡/已停用則不計入。
- **未啟用**（deactive）——`enable = false` 的用戶端（手動或由背景任務停用）。
- **活躍**（active）——已啟用、未耗盡、有效期未過，且距離各門檻仍有餘裕。

---

## 9. 客戶端群組

> 這是本 3X-UI 分支的功能。在原始的 3x-ui 專案（MHSanaei）中並沒有「客戶端群組」的概念——這裡新增了獨立的群組資料表、面板選單中的 **Группы**（群組）頁面以及對應的 API 方法。如果您將設定遷移到原始的 3x-ui，群組標籤就不會在任何地方被納入考量。

### 9.1. 什麼是客戶端群組，以及為何需要它

**群組**是一個具名的邏輯標籤（label），可以掛到一個或多個客戶端上。它不會建立新的連線方式，也既不是 inbound、也不是節點——它純粹是一個組織用的標記，藉此可以方便地對客戶端進行篩選與批次處理。

本分支客戶端模型的核心理念：**客戶端是頂層實體，以 email 來識別**（`clients` 資料表中的 `email` 欄位帶有唯一索引）。同一個客戶端（同一個 email、同一組憑證）可以同時隸屬於多個 inbound，甚至分布在多個節點上，並且可以使用不同的協定。群組標籤**每個客戶端只儲存一次**，因此它會自動套用到該客戶端的所有 inbound 綁定上。

群組標籤是用於分組的邏輯標籤：

| 層級 | 儲存位置 | 欄位 |
|------|--------------|------|
| 客戶端記錄（資料庫） | `clients` 資料表 | `group_name`（預設為空字串 `''`） |
| 群組目錄（資料庫） | `client_groups` 資料表 | `name`（唯一索引，不可為空） |
| inbound 設定（Xray） | JSON `settings.clients[].group` | 在該客戶端所屬的每個 inbound 的每個客戶端物件中重複出現 |

實務上為何需要它：

- **一個客戶端橫跨多個 inbound/節點。** 如果某個客戶端被「售出」為同時存取多個 inbound 的權限（例如不同協定或不同節點），群組可讓您將其視為一個整體來管理：重設流量、刪除、重新命名標籤——只需對其所有 inbound 執行一次操作即可。
- **批次操作與篩選。** 在 **Клиенты**（客戶端）頁面，清單可依群組篩選；在 **Группы**（群組）頁面，可對群組所有成員執行批次動作。
- **管理大量客戶端。** 諸如 `vip`、`trial`、`team-A` 之類的標籤有助於將成千上萬的客戶端歸入邏輯分類中，而不必為此衍生出獨立的 inbound。

### 9.2. 群組與客戶端、inbound、節點及協定的關聯

這是對理解至關重要的一節，因為標籤的同步並不簡單。

**群組描述的是客戶端，而非 inbound。** 標籤存活於客戶端記錄中（`clients.group_name`）。當客戶端隸屬於多個 inbound 時，每次群組變更面板都會遍歷該客戶端所屬的**所有** inbound，並在它們的 Xray 設定（`settings.clients[]`）內設定/移除 `group` 欄位。技術上的做法是：依客戶端的 email 找出其所屬的所有 inbound，然後在每個這類 inbound 的 JSON 設定中，修改帶有該 email 的客戶端物件。因此：

- 群組**與協定無關。** 同一個 email 可以在某個 inbound 中是 VLESS 客戶端，在另一個 inbound 中是 Hysteria 客戶端——它的群組標籤仍然只有一個，並會套用到兩者（同時每個協定有各自的憑證，分別獨立儲存）。
- 群組**橫跨節點。** 隸屬於節點的 inbound 與主面板的 inbound 之間，差別在於 `nodeId` 欄位（主面板 inbound 的該欄位為 `null`/`0`）。群組標籤會套用到 inbound 中的客戶端物件，無論該 inbound 是主面板的還是節點的——只要該 email 的客戶端存在於其中即可。

**群組標籤對來自節點的同步以及設定重建具有持續性。** 這是刻意設計的行為：

- 當節點送來流量快照時，其資料**不會覆寫**面板資料庫中客戶端的本地 `group_name` 與 `comment`。群組與註解被視為「面板本地」欄位——節點不負責管理它們。
- 在重建 inbound 設定時，傳入資料中的空 `group` 值**不會重設**已儲存的標籤。群組正是透過 **Группы**（群組）頁面來管理（而非透過編輯 inbound 的 Xray 設定），因此在一般的設定重建中,「空群組」被解讀為「不要動」，而非「清空」。

實務結論：唯一會**刻意清除**標籤的操作，是刪除群組以及明確地將客戶端從群組中移除（見下文）。一般的 inbound 編輯或與節點的背景同步都不會遺失群組。

### 9.3. 群組目錄與「空」群組

頁面上的群組清單由兩個來源合併而成：

1. **衍生群組（derived）**——所有實際出現在客戶端身上的非空 `group_name` 值，並計算客戶端數量。
2. **已儲存群組（stored）**——`client_groups` 資料表中的記錄。

這種合併帶來一個重要效果：群組可以在**沒有任何客戶端**的情況下存在。這類群組是透過明確的「Добавить группу」（新增群組）按鈕建立的（在 `client_groups` 中產生一筆記錄），並在清單中以計數 `0` 顯示。這些記錄就被視為**空群組**。清單始終以不分大小寫的名稱排序。

頁面上的彙總計數：

| 欄位（RU） | 顯示內容 |
|-----------|----------------|
| Всего групп | 群組總數（已儲存的與衍生的合計）。 |
| Клиенты с группой | 有多少客戶端帶有非空群組標籤。 |
| Пустые группы | 有多少群組是沒有客戶端的（計數為 `0`）。 |
| Клиентов в группе | 特定群組中的客戶端數量（資料表的一欄）。 |

### 9.4. 群組的欄位與資料表欄位

`client_groups` 資料表中的群組記錄包含：

| 欄位 | 類型 | 預設值 | 說明 |
|------|-----|--------------|----------|
| `Id` | int | 自動遞增 | 群組記錄的主鍵。 |
| `Name` | string | —（必填） | 群組名稱。唯一索引，不可為空。在 UI 中——**Имя**（名稱）欄。 |
| `CreatedAt` | int64（毫秒） | 建立時間 | 群組記錄的建立時刻。 |
| `UpdatedAt` | int64（毫秒） | 修改時間 | 最後一次修改的時刻。 |

頁面上的資料表至少會顯示 **Имя**（名稱）與 **Клиентов в группе**（群組中的客戶端數）兩欄，以及操作按鈕（見下文）。

### 9.5. 建立群組

按鈕 **Добавить группу**（新增群組）。

步驟：
1. 點擊 **Добавить группу**。
2. 輸入群組名稱。
3. 確認。

後端行為（`POST /panel/api/clients/groups/create`，請求主體 `{"name": "..."}`）：
- 名稱會去除前後空白。空名稱會被拒絕，回傳錯誤「group name is required」。
- 如果已存在同名群組——錯誤「group already exists」。
- 成功時會在 `client_groups` 中建立一筆記錄（初始沒有任何客戶端——即空群組）。

成功訊息：**「群組「{name}」已建立。」**

**範例：透過 API 建立空群組。** 在尚未填入客戶端之前就先準備好一組標籤：

```bash
curl -s 'https://panel.example.com:2053/panel/api/clients/groups/create' \
  -H 'Content-Type: application/json' \
  -b cookie.txt \
  -d '{"name": "vip"}'
```

成功時的回應：

```json
{ "success": true, "msg": "Группа «vip» создана.", "obj": null }
```

以相同名稱再次呼叫會回傳 `"success": false` 以及訊息 `group already exists`。

> 事先建立空群組在您想要先準備好一組標籤、之後再透過「Добавить клиентов…」（新增客戶端…）將客戶端填入時很方便。

### 9.6. 重新命名群組

按鈕 **Переименовать**（重新命名），對話框標題為 **「Переименовать {name}」**。

行為（`POST /panel/api/clients/groups/rename`，請求主體 `{"oldName": "...", "newName": "..."}`）：
- 兩個名稱都會去除空白。空的舊名稱——錯誤「old group name is required」，空的新名稱——「new group name is required」。
- 如果新名稱與舊名稱相同——不做任何事（影響 `0` 個客戶端）。
- 否則會以原子方式執行重新命名：
  - `client_groups` 中的記錄被重新命名；
  - 所有 `group_name = oldName` 的客戶端，該欄位都被更新為 `newName`；
  - 在受影響客戶端所屬的**所有 inbound**（包含節點的）中，Xray 設定裡的 `group` 值由舊名改為新名。
- 重新命名後，面板會將 Xray 標記為需要重新啟動，並發送客戶端變更的通知。

訊息：
- 成功：**「已為 {count} 個客戶端重新命名群組。」**
- UI 中的名稱衝突：**「名稱為「{name}」的群組已存在。」**

### 9.7. 將客戶端新增到群組

按鈕 **Добавить клиентов…**（新增客戶端…），標題為 **「將客戶端新增到群組「{name}」」**。

對話框中的逐字提示：

> 「選擇要新增到此群組的客戶端。現有的 inbound 綁定會保留；只會變更群組標籤。已在此群組中的客戶端不會顯示。」

如果沒有可新增的對象，會顯示 **「沒有其他可新增的客戶端。」**

行為（`POST /panel/api/clients/groups/bulkAdd`，請求主體 `{"emails": [...], "group": "..."}`）：
- 群組名稱為必填（否則錯誤「group name is required」）；空的 email 清單——操作不做任何事。
- 如果該群組在 `client_groups` 中和衍生群組中都尚未存在——它會被自動建立。
- 對所選 email 的客戶端設定 `group_name = group`；**客戶端與 inbound 的綁定不變**——只影響標籤。接著在這些客戶端的所有 inbound 中設定 `group` 欄位。
- 回傳受影響的客戶端記錄數量；Xray 被標記為需重新啟動。

成功訊息：**「已將 {count} 個客戶端新增到 {name}。」**

**範例：以單一請求為多個客戶端標記群組。** 客戶端以 email 指定，而與 inbound 的綁定不會因此變更：

```bash
curl -s 'https://panel.example.com:2053/panel/api/clients/groups/bulkAdd' \
  -H 'Content-Type: application/json' \
  -b cookie.txt \
  -d '{"emails": ["alice@example.com", "bob@example.com"], "group": "vip"}'
```

如果群組 `vip` 尚不存在，它會被自動建立。請求之後，這些客戶端的記錄中會設定 `group_name = "vip"`，而其每個 inbound 的 Xray 設定中，客戶端物件會得到 `"group": "vip"` 欄位：

```json
{ "id": "6f1b...", "email": "alice@example.com", "group": "vip", "enable": true }
```

### 9.8. 將客戶端從群組移除（不刪除客戶端本身）

按鈕 **Удалить клиентов…**（移除客戶端…），標題為 **「將客戶端從群組「{name}」移除」**。

逐字提示：

> 「選擇要從此群組移除的成員。客戶端本身會保留（若要完全刪除，請使用「Удалить клиентов группы」（刪除群組客戶端））。」

行為（`POST /panel/api/clients/groups/bulkRemove`，請求主體 `{"emails": [...]}`）：技術上這與「以空群組進行新增到群組」相同。所選客戶端的 `group_name` 被清空，而其 inbound 中的 `group` 欄位會從 Xray 設定中移除。客戶端本身及其與 inbound 的綁定保持不變。

成功訊息：**「已將 {count} 個客戶端從 {name} 移除。」**

### 9.9. 重設群組流量

按鈕 **Сбросить трафик**（重設流量）。

確認對話框：
- 標題：**「重設群組 {name} 的流量？」**
- 內文：**「這會將此群組中全部 {count} 個客戶端的 up/down 歸零。」**

行為：對群組所有成員的 email，在流量資料表中將 `up` 與 `down` 歸零，並將 `enable` 欄位設為 `true`（啟用客戶端）。操作以批次方式在交易中執行。

成功訊息：**「已重設 {count} 個客戶端的流量。」**

### 9.10. 刪除群組與刪除群組客戶端

頁面上有**兩種本質上截然不同的刪除操作**——它們很容易混淆，因此區別至關重要。

#### 9.10.1. 刪除群組（保留客戶端）

按鈕 **「Удалить группу (сохранить клиентов)」**（刪除群組（保留客戶端））。

對話框：
- 標題：**「刪除群組 {name}？」**
- 內文：**「這會刪除群組並清除其在 {count} 個客戶端上的標籤。客戶端本身不會被刪除。」**

行為（`POST /panel/api/clients/groups/delete`，請求主體 `{"name": "..."}`）：群組記錄會從 `client_groups` 中刪除，其所有客戶端的 `group_name` 被清空，並從它們的 inbound 中移除 `group` 欄位。**客戶端、其連線與流量都會保留。** Xray 被標記為需重新啟動。

成功訊息：**「已清除 {count} 個客戶端的群組。」**

#### 9.10.2. 刪除群組客戶端（完全刪除）

按鈕 **「Удалить клиентов группы」**（刪除群組客戶端）。

對話框：
- 標題：**「刪除 {name} 中的所有客戶端？」**
- 內文：**「這會連同流量記錄一起不可逆地刪除 {count} 個客戶端。群組標籤也會被清除。此操作無法復原。」**

這是破壞性操作：它會刪除客戶端本身（透過依 email 批次刪除，端點 `POST /panel/api/clients/bulkDel`），包含其流量記錄，並藉此將它們從所有 inbound 中移除。

訊息：
- 成功：**「已刪除 {count} 個客戶端。」**
- 部分結果：**「{ok} 已刪除，{failed} 已跳過」**

> 如果群組是空的，則無法對其成員執行動作——會顯示 **「此群組目前還沒有客戶端。」**

### 9.11. 與「客戶端」頁面的關聯

群組標籤在 **Группы**（群組）頁面之外也可見並被使用：

- 客戶端的精簡記錄中有 `group` 欄位，因此在客戶端清單中會顯示其所屬群組。
- 客戶端清單（`/panel/api/clients/list/paged`）接受篩選參數 `group`：可以傳入單一名稱，或以逗號分隔的多個名稱。比對在該欄位內以「或」的原則進行，且不分大小寫。特殊情況：篩選的群組清單中若有空元素，表示「沒有群組的客戶端」（其 `group` 為空）。
- 在客戶端頁面的回應中會回傳一個 `groups` 陣列——所有現有群組名稱的完整清單，以便 UI 建立篩選的下拉選單。

**範例：依群組篩選客戶端。** 此請求只會回傳帶有 `vip` 或 `trial` 標籤的客戶端（多個名稱——以逗號分隔，「或」）：

```
GET /panel/api/clients/list/paged?group=vip,trial
```

若要取得**沒有**群組的客戶端，請在清單中傳入一個空元素——例如，篩選值 `group=`（空字串）或 `group=vip,`（`vip` 標籤外加沒有群組的客戶端）。

### 9.12. API 端點彙總

所有群組路由都掛載在 `/panel/api/clients` 之下：

| 方法與路徑 | 用途 | 請求主體 |
|--------------|-----------|--------------|
| `GET /panel/api/clients/groups` | 列出群組及客戶端計數 | — |
| `GET /panel/api/clients/groups/:name/emails` | 群組所有成員的 email（依 email 排序） | — |
| `POST /panel/api/clients/groups/create` | 建立空群組 | `{"name"}` |
| `POST /panel/api/clients/groups/rename` | 重新命名群組 | `{"oldName","newName"}` |
| `POST /panel/api/clients/groups/delete` | 刪除群組並保留客戶端（清除標籤） | `{"name"}` |
| `POST /panel/api/clients/groups/bulkAdd` | 將客戶端新增到群組（依 email） | `{"emails":[...],"group"}` |
| `POST /panel/api/clients/groups/bulkRemove` | 將客戶端從群組移除（清除標籤） | `{"emails":[...]}` |
| `POST /panel/api/clients/bulkDel` | 完全刪除客戶端（供「刪除群組客戶端」使用） | `{"emails":[...],"keepTraffic"}` |

**範例：透過 API 的群組典型生命週期情境。**

```bash
# 1. 建立 trial 標籤
curl -s .../panel/api/clients/groups/create   -d '{"name":"trial"}'

# 2. 將其掛到兩個客戶端上
curl -s .../panel/api/clients/groups/bulkAdd  -d '{"emails":["u1@example.com","u2@example.com"],"group":"trial"}'

# 3. 將所有成員的流量歸零（email 取自 /groups/trial/emails）
curl -s .../panel/api/clients/groups/bulkRemove -d '{"emails":["u2@example.com"]}'

# 4. 刪除群組但保留客戶端（只清除標籤）
curl -s .../panel/api/clients/groups/delete   -d '{"name":"trial"}'
```

第 4 步會刪除群組記錄並清除其客戶端的 `group_name`，但客戶端本身、其連線與流量都會保留。若要不可逆地刪除客戶端本身，則應改用 `bulkDel`。

會變更客戶端標籤的操作（`rename`、`delete`、`bulkAdd`、`bulkRemove`）會將 Xray 標記為需要重新啟動，並發送客戶端變更的通知。

### 9.13. 依群組的流量

3.3.0 版本的新功能：在 **Группы**（群組）區段（「客戶端」頁面的群組管理分頁）中，群組資料表現在不僅顯示每個群組的客戶端數量，還顯示該群組的累計已用流量。該欄位標示為 **「Использованный трафик」**（已用流量）。

#### 該欄位顯示的內容

對每一列群組，會輸出該群組所有客戶端的流量總和——也就是其所有成員的 `up + down`（送出 + 接收流量）相加。這能快速回答「整個群組總共下載/分享了多少」的問題，而不必逐一打開客戶端再手動相加。

群組資料表中相鄰會輸出：

| 欄位 | 含義 |
|---|---|
| Имя | 群組名稱 |
| Клиенты | 有多少客戶端被標記為此群組（先前該欄稱為「Клиентов в группе」（群組中的客戶端數）） |
| Отправлено | 群組所有客戶端的 `up`（送出流量）總和 |
| Получено | 群組所有客戶端的 `down`（接收流量）總和 |
| Использованный трафик | 群組所有客戶端的 `up + down` 總和 |

送出與接收流量分別以 **Отправлено**（已送出）與 **Получено**（已接收）兩欄輸出，而 **Использованный трафик**（已用流量）欄則顯示它們的總和。客戶端數量的欄位就簡單稱為 **Клиенты**（客戶端）。

資料表上方的彙總另外會顯示所有群組的聚合數值——**「Всего групп」**（群組總數）與 **「Клиенты с группой」**（有群組的客戶端），而累計流量則分為兩張卡片：**「Всего отправлено / получено」**（總計送出／接收）（帶有上/下箭頭——分別為所有群組的送出與接收流量）以及 **「Общий трафик」**（總流量）（帶有圖表圖示——它們的合計總和）。

#### 如何計算

計算透過對客戶端資料表執行一次 SQL 查詢、並聯結（`LEFT JOIN`）流量記帳資料表來完成：

- 依群組標籤欄位（`group_name`）將客戶端分組並計算其數量——這就是「群組中的客戶端數」；
- 流量取自所聯結的 `client_traffics` 資料表中 `up + down` 的總和。也就是將每個客戶端送出（`up`）與接收（`down`）的位元組相加；
- 由於 email 在客戶端資料表與流量資料表中都是唯一的，因此聯結不會使單一客戶端的流量重複計算。

數值的特性：

- **沒有流量記錄的客戶端**會被計入成員計數，但對總和貢獻 0，因此剛建立的群組顯示流量為 `0`。
- **空群組**（已建立但沒有客戶端）同樣會以零計數與零流量出現在清單中：除了由客戶端標籤「衍生」出的群組外，明確儲存的群組也會被併入結果，之後清單會以不分大小寫的名稱排序。
- 沒有群組標籤的客戶端（`group_name` 為空）不會被納入計算。

#### 相關動作

在群組資料表中，針對整個群組的動作仍然可用，包括 **「Сбросить трафик」**（重設流量）——將所選群組所有客戶端的 `up`/`down` 歸零。在這樣重設之後，該群組的「已用流量」欄會顯示 `0`。

---

## 10. 訂閱（Subscription）

訂閱（subscription）是一種機制，可讓您向用戶端發放一條固定的連結（URL），VPN 用戶端會自行透過該連結下載並定期更新整套設定。您不必再手動將每個 inbound 的個別連結逐一轉發給使用者，只需提供一個形如 `https://域名:端口/sub/<subId>` 的統一位址即可。面板會透過該位址即時彙整綁定到該用戶端的所有設定，並以用戶端所需的格式回傳。當伺服器上的設定發生變更時（新位址、Reality 金鑰輪替、新增 inbound），用戶端會在下一次自動更新時取得最新設定，無需使用者執行任何操作。

訂閱由面板內部一個獨立的 HTTP/HTTPS 伺服器負責，它獨立於 Web 面板啟動，並監聽自己的端口。這樣設計是出於安全考量：您可以對外開放訂閱端口，而無需開放面板本身的端口。

### 10.1. 什麼是 subId，以及連結如何產生

inbound 中的每個用戶端都有一個 `subId` 欄位（介面中為「訂閱 ID」）。正是這個值構成了訂閱的鍵：面板會在所有 inbound 中尋找 `subId` 與所請求值相符的用戶端，並將它們的設定合併到單一回應中。

- 如果有多個用戶端（在同一個或不同的 inbound 中）設定了相同的 `subId`，它們的設定就會被歸入同一個訂閱。這是讓單一使用者透過一條連結同時取得多個伺服器／協定的標準做法。

**範例：一個使用者，透過一條連結取得兩個伺服器。** 假設有兩個 inbound（伺服器 A 上的 VLESS 與伺服器 B 上的 Trojan）。為了透過一條連結向使用者發放這兩個設定，請為他的兩個用戶端設定相同的 `subId`：

```
Inbound 1 (VLESS):  email = ivan@vpn,  subId = ivan2025
Inbound 2 (Trojan): email = ivan@vpn,  subId = ivan2025
```

如此一來，透過 `https://sub.example.com:2096/sub/ivan2025` 位址，面板就會一次回傳這兩個設定。日後若新增第三個使用相同 `subId` 的 inbound，它會在訂閱下一次自動更新時出現在使用者那裡，無需轉發新連結。
- 如果用戶端的 `subId` 欄位為空，就無法分享供共用存取的連結。介面中會以提示指出這一點：「此用戶端沒有 subId，無法使用共用存取連結。」

#### 用戶端的外部連結與訂閱（「Links」分頁）

在用戶端表單中有一個 **「Links」** 分頁，可為個別用戶端附加額外的設定來源，這些來源會被混入該用戶端的訂閱中（支援 RAW、JSON 與 Clash 格式）：

- **Add External Link** — 第三方分享連結（`vless://`、`trojan://`、`ss://` 等）。會原樣加入回傳結果，而對於 JSON/Clash 則會額外解析為設定。
- **Add External Subscription** — 外部訂閱的位址。面板會自行下載它（具備快取與較短的逾時），並將取得的設定併入該用戶端的整體清單。

這樣可以方便地在您的 inbound 之外，透過同一條統一連結向用戶端額外發放更多伺服器。如果遠端訂閱的回應過大，不再會被靜默截斷：面板會回傳錯誤，並繼續使用上一次成功快取的值。
- `subId` 的值不能任意設定：儲存時會檢查其中是否包含空格、`/`、`\` 字元及控制字元。對應的驗證提示為：「訂閱 ID 不能包含空格、'/'、'\' 或控制字元。」

最終連結的結構為 `<基底>/<subPath>/<subId>`（請參閱關於訂閱伺服器設定與「反向代理 URI」欄位的章節）。如果依 `subId` 找不到任何用戶端（用戶端已刪除、`subId` 不存在），伺服器會回傳沒有主體的 HTTP 404。發生內部錯誤時則回傳 HTTP 500。VPN 用戶端只依據回應狀態碼運作，因此錯誤主體刻意留空。

#### 訂閱中 inbound 連結的順序

每個 inbound 都有一個 **「訂閱中順序」** 欄位（`subSortIndex`）——一個從 1 起算的數字，用來指定該 inbound 的連結在訂閱輸出中的位置。值較小者排在前面；數值相同時則保留原本的建立順序（依 id）。此順序套用於所有輸出格式——原始文字、訂閱頁面、JSON 與 Clash。此欄位不會影響面板本身中 inbounds 的順序。

此欄位在 inbound 表單中於連結內位址（share address）設定旁編輯，並依一般規則同步至節點。只要有任一 inbound 的順序不等於 1，Inbounds 清單中就會出現一個精簡的 **「順序」** 欄。

### 10.2. 訂閱伺服器設定

所有訂閱參數都位於面板設定的 **「訂閱」** 分頁中。下方逐一說明每個參數；括號中標示了該設定的內部鍵與預設值。

該區段本身又分為多個分頁：**「面板設定」**、**「資訊」**、**「設定檔」**、**「憑證」**、**「Happ」** 與 **「Clash / Mihomo」**。訂閱標題、支援 URL、設定檔頁面、公告與主題目錄等欄位位於「設定檔」分頁；Happ 與 Clash/Mihomo 的路由規則位於同名分頁；訂閱更新間隔則位於「資訊」分頁。

#### 主要參數

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| 啟用訂閱 | `subEnable` | `true`（已啟用） | 啟動獨立的訂閱伺服器。提示：「具有獨立設定的訂閱功能」。若關閉——訂閱伺服器不會啟動，所有連結都將無法運作。 |
| 監聽 IP | `subListen` | 空 | 訂閱伺服器接受連線所在的 IP 位址。提示：「保留為空（預設）以監聽所有 IP 位址」。 |
| 訂閱端口 | `subPort` | `2096` | 訂閱伺服器的 TCP 端口。提示：「用於提供訂閱服務的端口號不得在伺服器上被佔用」——該端口必須空閒，且不可與面板或 Xray 衝突。 |
| URI 路徑 | `subPath` | `/sub/` | 提供一般訂閱所使用的路徑。提示：「必須以 '/' 開頭並以 '/' 結尾」。 |
| 監聽域名 | `subDomain` | 空 | 允許存取訂閱的域名（Host 驗證）。提示：「保留為空（預設）以監聽所有域名與 IP 位址」。若已設定——使用其他 Host 的請求會被拒絕。 |

**安全重點：** 預設路徑 `/sub/`（以及 JSON 的 `/json/`）廣為人知且容易被猜中。面板會顯示警告：「預設訂閱路徑 "/sub/" 廣為人知——請更改它。」JSON 也有類似警告。建議設定一個自訂且不明顯的路徑。

#### TLS / 憑證

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| 訂閱憑證公鑰檔案路徑 | `subCertFile` | 空 | 憑證檔案（`.crt`/`fullchain`）的完整路徑。提示：「請輸入以 '/' 開頭的完整路徑」。 |
| 訂閱憑證私鑰檔案路徑 | `subKeyFile` | 空 | 私鑰檔案的完整路徑。提示：「請輸入以 '/' 開頭的完整路徑」。 |

如果兩個路徑都已設定且憑證成功載入，訂閱伺服器就會以 **HTTPS** 運作。如果欄位為空或憑證無法讀取——伺服器會回退到 **HTTP**（錯誤會寫入記錄檔）。是否具備有效的 TLS 也會影響基底 URL 的產生：在 443 端口搭配 TLS、以及 80 端口不搭配 TLS 時，連結中的端口號會被省略。

#### 更新間隔

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| 訂閱更新間隔 | `subUpdates` | `12` | 用戶端應用程式重新請求訂閱的頻率（以小時計）。提示：「用戶端應用程式中兩次更新之間的間隔（以小時計）」。 |

該值會透過 HTTP 標頭 `Profile-Update-Interval` 傳給用戶端；現代用戶端會將其作為設定自動更新的週期。

#### 回應中的格式與資訊

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| 編碼 | `subEncrypt` | `true` | 提示：「對訂閱中回傳的設定進行加密」。技術上這並非加密，而是對一般訂閱整個主體進行 **Base64 編碼**（這是大多數用戶端所預期的格式）。關閉時，連結會以明文輸出，每行一條。 |
| 顯示使用資訊 | `subShowInfo` | `true` | 提示：「在設定名稱後顯示剩餘流量與到期日」。啟用時，每個設定的名稱（remark）會加上剩餘流量（📊）與有效期（例如 `5D,3H⏳`）的標記；當用戶端已到期／不可用時則顯示 `⛔️N/A`。 |
| 在名稱中包含 Email | `subEmailInRemark` | `true` | 提示：「在訂閱設定檔名稱中包含用戶端 email。」會在設定檔 remark 中加入用戶端的 email。 |

#### 備註範本（Remark Template）

訂閱中每個設定的顯示名稱（remark）是依 **備註範本** 產生的——即訂閱設定的 **「資訊」** 分頁中的 **「備註範本」** 欄位（`remarkTemplate`）。舊版的備註模型建構器（分別選擇 inbound/email/external proxy 等部分與分隔符號）已從介面中移除；現在您可以撰寫任意的名稱格式，並在其中插入變數。預設值為 `{{INBOUND}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D`。若欄位留空，則套用舊版（無法透過介面設定的）備註模型。

變數依 **Client**、**Traffic** 與 **Time & status** 等分組顯示，並以可點擊的 `{{VAR}}` 籌碼形式出現在欄位旁，滑鼠停留時會有提示；點擊會將該標記插入範本中，並提供即時預覽。每個變數會在產生訂閱的當下，針對特定用戶端個別代入。也允許使用單花括號的簡化寫法（`{DATA_LEFT}`、`{EXPIRE_DATE}`、`{PROTOCOL}`、`{TRANSPORT}` 等）——面板會自行將其轉換為內部格式 `{{...}}`。

可用變數：

- **用戶端識別：** `{{EMAIL}}`、`{{INBOUND}}`（inbound 本身的備註）、`{{HOST}}`（主機的備註）、`{{ID}}`（UUID）、`{{SHORT_ID}}`（UUID 的前 8 個字元）、`{{SUB_ID}}`、`{{COMMENT}}`、`{{TELEGRAM_ID}}`、`{{PROTOCOL}}`、`{{TRANSPORT}}`。
- **流量：** `{{TRAFFIC_USED}}`、`{{TRAFFIC_LEFT}}`、`{{TRAFFIC_TOTAL}}`（以及它們以精確位元組表示的 `*_BYTES` 變體）、`{{UP}}`、`{{DOWN}}`、`{{USAGE_PERCENTAGE}}`。
- **有效期與狀態：** `{{DAYS_LEFT}}`、`{{TIME_LEFT}}`、`{{EXPIRE_DATE}}`（`YYYY-MM-DD`）、`{{JALALI_EXPIRE_DATE}}`（賈拉里曆日期）、`{{EXPIRE_UNIX}}`、`{{CREATED_UNIX}}`、`{{RESET_DAYS}}`、`{{STATUS}}`（active / expired / disabled / depleted）、`{{STATUS_EMOJI}}`。

範本可用直豎線 `|` 分割為多個區段。當某區段中的變數產生「無限制」值（`∞`）時——例如無限制用戶端的 `{{TRAFFIC_LEFT}}` 或 `{{DAYS_LEFT}}`——該區段會自動隱藏。此外，流量消耗與有效期區塊只會顯示一次，出現在該用戶端的第一條連結上，以免在每個設定中重複。

**範例。** 對於剩餘 42 GB、剩 7 天的用戶端，範本 `{{EMAIL}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D` 會產生形如 `ivan@vpn 📊42.00GB ⏳7D` 的名稱；而對於無限制用戶端則只有 `ivan@vpn`（含 `∞` 的區段已被省略）。
| 備註範本 | `remarkTemplate` | `{{INBOUND}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D` | 每個設定顯示名稱（remark）的自由範本，並以變數 `{{VAR}}` 代入。產生訂閱時會針對每個用戶端個別代入。舊版的「備註模型」建構器（選擇 inbound/email/external proxy 與分隔符號）已從介面中移除，僅在欄位留空時作為備援使用。詳情請參閱下方的「備註範本（Remark Template）」。 |

#### 設定檔中繼資料（回應標頭）

這些字串會透過 HTTP 回應標頭傳給用戶端，並在 VPN 用戶端中作為設定檔中繼資料顯示。它們預設皆為空。

| 欄位（UI） | 鍵 | 標頭 | 說明 |
|---|---|---|---|
| 訂閱標題 | `subTitle` | `Profile-Title`（Base64 編碼） | 「用戶端在 VPN 用戶端中看到的訂閱名稱」。對於 Clash，也會透過 `Content-Disposition` 作為匯入設定檔的名稱使用。 |
| 支援 URL | `subSupportUrl` | `Support-Url` | 「在 VPN 用戶端中顯示的技術支援連結」。 |
| 設定檔 URL | `subProfileUrl` | `Profile-Web-Page-Url` | 「在 VPN 用戶端中顯示的您的網站連結」。若未設定，則代入訂閱請求的實際 URL。 |
| 公告 | `subAnnounce` | `Announce`（Base64 編碼） | 「在 VPN 用戶端中顯示的公告文字」。 |

此外，每個回應都會傳送 `Subscription-Userinfo` 標頭，其中包含用戶端流量的彙總資料：`upload`、`download`、`total` 與 `expire`（到期時刻，以秒計）。用戶端會據此顯示剩餘流量與有效期。

#### 路由（僅適用於 Happ 用戶端）

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| 啟用路由 | `subEnableRouting` | `false` | 「在 VPN 用戶端中啟用路由的全域設定。（僅適用於 Happ）」。透過 `Routing-Enable` 標頭傳送。 |
| 路由規則 | `subRoutingRules` | 空 | 「VPN 用戶端的全域路由規則。（僅適用於 Happ）」。透過 `Routing` 標頭傳送。 |

| 隱藏伺服器設定 | `subHideSettings` | `false` | 「在訂閱中隱藏伺服器設定（僅適用於 Happ）」。啟用時，Happ 用戶端中檢視與變更伺服器參數的功能會被隱藏。此選項僅對 Happ 用戶端生效。 |

#### 反向代理 URI

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| 反向代理 URI | `subURI` | 空 | 「變更訂閱 URL 的基底 URI，以便在代理伺服器後方使用」。 |

如果欄位為空，面板會自行從訂閱的域名與端口（並考量 TLS）建構連結的基底位址。但如果訂閱是透過位於其他域名或路徑上的外部反向代理／CDN 來分發，則在此欄位中設定最終的基底 URI，所有連結都將以它為基礎建構。JSON（`subJsonURI`）與 Clash（`subClashURI`）也有類似的獨立欄位。

如果只設定了通用的 `subURI`，而 JSON 與 Clash 的獨立欄位留空，那麼訂閱頁面上這些格式的連結會繼承 `subURI` 的協定與主機（而非 sub 伺服器的端口與 `http`）——如此一來它們就會與反向代理的位址一致。

**範例：反向代理後方的訂閱。** 訂閱本身監聽於 `2096`，但對外是透過 nginx/CDN 以 `https://cfg.example.com/u/` 提供。為了讓回應中的連結以外部位址而非內部 `域名:2096` 為基礎建構，請在「Reverse proxy URI」欄位中設定最終的基底 URI：

```
Reverse proxy URI: https://cfg.example.com/u
```

如此一來，最終連結會呈現為 `https://cfg.example.com/u/ivan2025`。對於 JSON 與 Clash 格式，必要時可用相同方式填入獨立欄位 `subJsonURI` 與 `subClashURI`。

### 10.3. 輸出格式

訂閱可以三種獨立的格式輸出，每種都有自己的端點，並可分別啟用／停用。

#### 輸出中的伺服器位址與節點

訂閱連結中的伺服器位址，是依照與面板中一般連結及 QR 碼相同的「連結內位址」策略代入：「listen」——可路由的繫結位址；「custom」——使用者自訂的位址（`shareAddr`）；「node」（預設）——節點位址。對於未明確設定策略的 inbound，訂閱輸出不會改變。這讓繫結至特定公開 IP 的節點 inbound 能向用戶端提供可達的位址。此策略套用於原始、JSON 與 Clash 格式。

節點名稱（Node）不會加入訂閱中設定檔的名稱（remark）：用戶端應用程式中只會顯示管理員所設定的 inbound 備註，不含形如 `@節點名稱` 的內部後綴。若要在多節點訂閱中區分同名的條目，請手動為它們設定不同的備註，或使用具有自訂 Remark 的受管理主機（Hosts）。

如果因節點之間不同步，同一個用戶端在服務性 JSON inbound 中重複出現了兩次，訂閱輸出會在全部三種格式中自動依 email 去除這類重複項，因此輸出中不會出現重複的設定檔。

#### 受管理主機（Hosts）

**Hosts** 區段（側邊選單項目；含 Total/Enabled/Disabled 數量與清單的彙總頁面）用於設定訂閱連結的位址覆寫。可為每個 inbound 新增一個或多個 **主機**——這些端點會被代入發放給用戶端的 subscription 連結中，**取代 inbound 本身的位址、端口與 TLS 參數**。這樣可以方便地透過 CDN 或中繼分發流量，而無需更動 inbound 本身。

每個主機可設定：

- **Remark** 與描述（Description）、與特定 **Inbound** 的綁定、**Enable** 開關，以及指派至節點（**Nodes**）。
- **Address**（留空——繼承 inbound 的位址）與 **Port**（`0`——繼承 inbound 的端口）；**Tags**（僅在 RAW 訂閱中生效）。
- **Security** 分頁——`same` / `tls` / `none` / `reality`，含 SNI、指紋（fingerprint）、ALPN、憑證綁定（pinned-cert）、`allowInsecure` 與 ECH。
- **Advanced** 分頁——Host header、Path、VLESS 路由、Mux、Sockopt、Final Mask，以及將主機從個別訂閱格式（raw / json / clash）中排除。
- **Clash (mihomo)** 分頁——IP 版本、Mihomo X25519、主機洗牌（Shuffle host）。

主機在其所屬 inbound 範圍內排序，並支援批次啟用、停用與刪除。受管理主機取代了舊版的 External Proxy 陣列。

#### 一般連結（SUB）— Base64 / 純文字

基本格式，端點為 `subPath`（預設 `/sub/`）。永遠啟用（只要整體訂閱已啟用）。回傳 Xray 連結清單（`vless://`、`vmess://`、`trojan://`、`ss://` 等）——每行一條。啟用「編碼」選項（`subEncrypt`）時，整個清單會被編碼為 Base64；關閉時則以明文輸出。幾乎所有用戶端都能理解此格式（v2rayNG、V2RayTun、Sing-box、NekoBox、Streisand、Shadowrocket、Happ 等）。

**範例：關閉「編碼」時的回應主體。** 當 `subEncrypt = false` 時，端點 `/sub/` 會輸出明文——每行一條連結：

```
vless://3c8f...@a.example.com:443?security=reality&...#srvA-ivan
trojan://p4ss@b.example.com:443?security=tls&...#srvB-ivan
```

當 `subEncrypt = true`（預設）時，同一份清單會整個被編碼為 Base64 並以單行輸出——這正是大多數用戶端所預期的形式。

#### JSON 訂閱（sing-box 及相容用戶端）

端點為 `subJsonPath`（預設 `/json/`），需以獨立的核取方塊啟用。

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| JSON 訂閱 | `subJsonEnable` | `false` | 「獨立啟用／停用 JSON 訂閱端點。」 |

回傳完整的 JSON 設定（sing-box 及其衍生用戶端——Podkop、OpenWRT sing-box、Karing、NekoBox——所能理解的格式）。此格式有額外可用的參數（`subFormats` 分頁）：

- **Mux**（`subJsonMux`，預設為空）——多工（Mux）的 JSON 設定，會被注入 JSON 訂閱中每條串流的 outbound。「在單一連線中傳輸多個獨立的資料串流。」
- **Final Mask**（`subJsonFinalMask`，預設為空）——「加入 JSON 訂閱每條串流的 xray finalmask 遮罩（TCP/UDP）與 QUIC 設定。需要用戶端上的較新版本 xray。」透過子欄位設定：「封包」（`packets`）、「長度」（`length`）、「間隔」（`interval`）、「最大分割」（`maxSplit`）、「雜訊」（`noises`：「類型」/`type`、「封包」/`packet`、「延遲（ms）」/`delayMs`、「套用至」/`applyTo`，以及「+ 雜訊」按鈕），還有「平行度」（`concurrency`）、「xudp 平行度」（`xudpConcurrency`）與「xudp UDP 443」（`xudpUdp443`）。
- **路由規則**（`subJsonRules`，預設為空）——加入 JSON 設定的全域規則。

#### Clash / Mihomo 訂閱（YAML）

端點為 `subClashPath`（預設 `/clash/`），需以獨立的核取方塊啟用。

| 欄位（UI） | 鍵 | 預設值 | 說明 |
|---|---|---|---|
| Clash / Mihomo 訂閱 | `subClashEnable` | `false` | 啟用為 Clash 與 Mihomo 用戶端產生 YAML 設定。 |
| 啟用路由 | `subClashEnableRouting` | `false` | 「在所產生的 YAML 訂閱中加入 Clash/Mihomo 全域路由規則。」 |
| 全域路由規則 | `subClashRules` | 空 | 「加入每份 YAML 訂閱開頭、置於 MATCH,PROXY 之前的 Clash/Mihomo 規則。」 |

回應以 `application/yaml; charset=utf-8` 類型輸出。如果已設定「訂閱標題」（`subTitle`），它也會在 `Content-Disposition` 標頭中傳送（`attachment; filename*=UTF-8''<title>`），讓 Clash 用戶端以此名稱命名匯入的設定檔。

所產生的連結與 YAML 格式會維持在符合現代用戶端的最新狀態：Shadowsocks-2022（SS2022）不再將 userinfo 編碼為 Base64；具 http 混淆的 Shadowsocks 連結會以 SIP002 格式搭配 `obfs-local` 外掛輸出；Clash/Mihomo 訂閱已實作完整的 XHTTP 欄位集。這不需要額外設定——連結只是會被用戶端更正確地識別。

> 注意：在此版本中所支援的就是三種格式——一般連結（Base64/文字）、JSON（sing-box 相容）與 Clash/Mihomo（YAML）。訂閱伺服器中沒有獨立的 Outline 格式。

### 10.4. 訂閱資訊頁面與 QR 碼

如果在瀏覽器中開啟訂閱連結（或在 URL 中明確加上參數 `?html=1` 或 `?view=html`，又或傳送標頭 `Accept: text/html`），伺服器就不會回傳「原始」回應，而是輸出一個視覺化的 **訂閱資訊頁面**（「訂閱資訊」）。VPN 用戶端仍會收到機器可讀的回應，因為它們不會請求 HTML。

該頁面（一個由 Vite 建置的單頁應用程式）會顯示：

- **訂閱資訊**（Descriptions 區塊）：
  - 「訂閱 ID」——`subId` 的值；
  - 「狀態」——「啟用中」、「未啟用」或「無限制」。當用戶端已停用、已耗盡流量上限或已過期時，狀態會被設為「未啟用」；
  - 「已下載」與「已上傳」——流量量；
  - 「總上限」——流量上限，若不受限制則為 `∞`；
  - 「有效期」——到期日，或「永久」；
  - 剩餘流量與最後上線時間。
  - 日期依面板的「Calendar Type」設定（`datepicker`，預設 `gregorian`）以西曆或賈拉里曆顯示。
- **訂閱連結**：對每個已啟用的格式——各有一行，含彩色標籤（綠色 **SUB**、紫色 **JSON**、金色 **CLASH**）、複製按鈕與 **QR 碼** 按鈕（彈出視窗，尺寸 240 px）。只有當對應格式在設定中已啟用時，JSON 與 CLASH 的那一行才會出現。
- **個別連結**（「複製連結」）：訂閱中所含個別設定的完整清單，每條都有自己的協定標籤、複製按鈕與 QR 碼（post-quantum 連結不會產生 QR 碼）。

- **「複製所有設定」按鈕**（位於個別連結清單上方）：一鍵將所有設定連結一次複製到剪貼簿（每條換一行），無需逐一複製；完成後會顯示通知「所有設定已複製」。
- **快速匯入應用程式按鈕**（依平台分組的下拉選單）：對於 Android——v2box、v2rayNG（deep-link `v2rayng://install-config?url=…`）、Sing-box、V2RayTun、NPV Tunnel、Happ（`happ://add/…`）；對於 iOS——Shadowrocket（透過參數 `flag=shadowrocket`）、v2box（`v2box://install-sub?url=…&name=…`）、Streisand（`streisand://import/…`）、V2RayTun、NPV Tunnel、Happ。這些按鈕要嘛開啟已預先代入訂閱位址的對應應用程式 deep-link，要嘛將連結複製到剪貼簿。

資訊頁面會以禁止快取的標頭（`Cache-Control: no-cache`）輸出，讓用戶端永遠看到最新的流量與有效期資料。

### 10.5. 自訂訂閱頁面範本

自 3.3.0 起，可用自己的 HTML 範本取代標準的訂閱著陸頁面。預設情況下，訂閱位址會輸出內建頁面，但若指定一個含自訂範本的目錄，面板就會渲染它，並將用戶端的最新資料（流量、有效期、連結等）代入其中。

重要：面板 **不提供** 現成的範本。倉庫中只附帶一個含說明檔 `sub_templates/README.md` 的 `sub_templates/` 目錄；您需要自行建立自己的主題。

#### 在哪裡啟用

主題目錄在面板設定中指定：

**設定 → 訂閱 → 「訂閱資訊」區段**，欄位 **「訂閱主題目錄」**（`subThemeDir`）。

介面中該欄位的說明：
「指向含訂閱頁面自訂範本（index.html/sub.html）資料夾的絕對路徑（例如 /etc/3x-ui/sub_templates/my-theme/）。保留為空以使用預設頁面。」

在同一區段相鄰處還有一些相關設定，其值可在範本中取用：

在「訂閱主題目錄」欄位的說明中有一個 **「範本指南 ↗」** 連結，指向關於建立自訂訂閱頁面外觀範本的文件。
- **「訂閱標題」**（`subTitle`）——用戶端可見的名稱；
- **「支援 URL」**（`subSupportUrl`）——技術支援連結。

#### 設定參數

| 參數 | 預設值 | 用途 |
|---|---|---|
| `subThemeDir` | `""`（空） | 指向含您 HTML 範本之目錄的絕對路徑。空 = 內建的預設頁面。 |

#### 如何代入自己的範本

1. 在伺服器上建立一個主題資料夾（位置不限），例如 `/etc/3x-ui/sub_templates/my-theme/`。
2. 在其中放入名為 `index.html` 或 `sub.html` 的 HTML 檔案。

**範例：主題路徑。** 伺服器上的最終配置與設定中欄位的值：

```
/etc/3x-ui/sub_templates/my-theme/
└── index.html        (или sub.html — он имеет приоритет)
```

```
Настройки → Подписка → «Каталог темы подписки»:
/etc/3x-ui/sub_templates/my-theme/
```

路徑必須是 **絕對** 路徑（以 `/` 開頭）。如果資料夾中既沒有 `index.html` 也沒有 `sub.html`，面板會輸出內建頁面。
3. 在面板中開啟 **設定 → 訂閱**，並在「訂閱主題目錄」欄位中填入該資料夾的 **絕對** 路徑。
4. 儲存設定。

檔案選取與渲染的行為：
- 如果目錄中有 `sub.html`，就使用它；否則採用 `index.html`。也就是說 `sub.html` 的優先順序高於 `index.html`。
- 範本以標準的 Go `html/template` 引擎渲染。
- 已解析的範本會被 **快取**，且只有在檔案修改時間變動時才重新從磁碟讀取。因此範本的修改無需重啟面板即可生效，同時又不會在每次請求時產生讀取／解析的額外開銷。
- 回應會先整個寫入緩衝區，之後才輸出給用戶端：如果範本在執行期間失敗，部分產生的（損壞的）頁面不會送達使用者。

#### 預設行為與備援（fallback）

- 欄位為空 → 輸出內建的 SPA 頁面（資料注入 `window.__SUB_PAGE_DATA__`）。
- 路徑不存在或不是目錄 → 使用預設頁面。
- 目錄中既無 `index.html` 也無 `sub.html` → 記錄檔寫入警告「subThemeDir set but no usable template found」，並輸出預設頁面。
- 範本檔案存在但無法解析 → 記錄檔寫入錯誤「custom template parse failed」，並輸出預設頁面。
- 範本執行時發生錯誤 → 記錄檔寫入「custom template execution failed」，並輸出預設頁面。

也就是說，自訂範本的任何問題都不會「弄壞」訂閱——面板永遠會降級回內建頁面。所有訂閱頁面（無論自訂或標準）都以禁止快取的標頭（`Cache-Control: no-cache, no-store, must-revalidate`）輸出，讓用戶端永遠取得最新的流量與有效期資料。

#### 可用的範本變數

範本的上下文中會傳入一組訂閱用戶端的資料。透過 `{{ .名稱 }}` 取用：

| 變數 | 類型 | 說明 |
|---|---|---|
| `{{ .sId }}` | string | 訂閱 ID（UUID）。 |
| `{{ .enabled }}` | bool | 用戶端／訂閱是否已啟用。 |
| `{{ .download }}` | string | 格式化後的下載量（例如「2.5 GB」）。 |
| `{{ .upload }}` | string | 格式化後的上傳量。 |
| `{{ .total }}` | string | 格式化後的流量總上限。 |
| `{{ .used }}` | string | 格式化後的已用流量（download + upload）。 |
| `{{ .remained }}` | string | 格式化後的剩餘流量。 |
| `{{ .expire }}` | int64 | 有效期——Unix 時間，以 **秒** 計（`0` = 永久）。給 JS `Date` 使用時請乘以 1000。 |
| `{{ .lastOnline }}` | int64 | 最後上線時間——Unix 時間，以 **毫秒** 計（`0` = 從未上線）。 |
| `{{ .downloadByte }}` | int64 | 下載量，以精確位元組計。 |
| `{{ .uploadByte }}` | int64 | 上傳量，以精確位元組計。 |
| `{{ .totalByte }}` | int64 | 總上限，以精確位元組計。 |
| `{{ .subUrl }}` | string | 訂閱頁面的 URL。 |
| `{{ .subJsonUrl }}` | string | 訂閱 JSON 設定的 URL。 |
| `{{ .subClashUrl }}` | string | Clash/Mihomo 設定的 URL。 |
| `{{ .subTitle }}` | string | 設定中的訂閱標題（可能為空）。 |
| `{{ .subSupportUrl }}` | string | 設定中的支援 URL（可能為空）。 |
| `{{ .links }}` | []string | 設定字串清單（VMess、VLESS 等）。逐一走訪：`{{ range .links }} … {{ end }}`。 |
| `{{ .emails }}` | []string | 與訂閱相關的 email 清單。 |
| `{{ .datepicker }}` | string | 面板目前的曆法格式：`gregorian` 或 `jalali`（取自「曆法類型」設定；若為空——`gregorian`）。 |

使用其中部分變數的最小範本主體範例：

```html
<h1>{{ .subTitle }}</h1>
<p>Использовано: {{ .used }} из {{ .total }} (осталось {{ .remained }})</p>
{{ range .links }}<div>{{ . }}</div>{{ end }}

**Пример: дата окончания из `expire`.** Поле `{{ .expire }}` — это Unix-время в **секундах**, поэтому для JavaScript его умножают на 1000; значение `0` означает «без срока»:

```html
<script>
  var exp = {{ .expire }};
  document.write(exp === 0
    ? 'Без срока'
    : 'До ' + new Date(exp * 1000).toLocaleDateString());
</script>
```

Обратите внимание: `{{ .lastOnline }}` задаётся уже в **миллисекундах** — его умножать на 1000 не нужно.
```

---

## 11. Xray：路由、outbounds、DNS 與擴充功能

**「Xray 設定」**區段是 Xray-core 設定範本的編輯器，面板會以此為基礎產生用於啟動核心的最終 `config.json`。範本區段的提示文字為：*「設定檔 Xray 是依據此範本建立的。」* 與 inbounds 不同（inbounds 單獨儲存在資料庫中，並在組建設定時填入範本），其餘所有內容——日誌、路由、outbounds、DNS、政策、統計——都正是在此處設定。

> 重要：範本的值以鍵 `xrayTemplateConfig` 儲存在資料庫中。儲存時，面板會將其經過一系列自動轉換處理（見 [11.10](#1110-日誌與統計statsmetrics)）。任何語法不正確的 JSON 都會被以錯誤 *「xray template config invalid」* 拒絕。

#### 在選單中的位置：「外送」與「路由」

**「外送」(Outbounds)** 與 **「路由」(Routing)** 是側邊選單中各自獨立的項目（緊接在「主機」下方、「面板設定」上方），各有自己的位址：`/outbound` 與 `/routing`。指向這些頁面的直接連結以及重新整理頁面都能如預期運作。此時**「Xray 設定」**子選單中只剩下：基本、負載平衡器、DNS 與進階範本。下文中的 [11.3](#113-路由規則routing) 與 [11.4](#114-outbounds外送連線) 兩節分別對應「路由」與「外送」頁面。

### 11.1. 編輯器結構：分頁／模式

編輯器提供數種範本顯示模式（按 JSON 區段過濾）：

| 模式 | 顯示內容 |
|---|---|
| **基本** | 基礎區段（日誌、基礎路由、主要設定） |
| **進階範本** | 完整的 Xray JSON 範本 |
| **全部** | 同時顯示所有區段 |

編輯器內部的設定邏輯分組：

- **基本設定**（提示：*「這些參數描述一般設定」*）。
- **日誌**（見 [11.9](#119-reverse-代理與-tun)）。
- **基礎連線**：封鎖與直連路由。
- **入站**（提示：*「修改設定範本以連接特定的用戶端」*）。
- **外送**（見 [11.4](#114-outbounds外送連線)）。
- **負載平衡器**（見 [11.5](#115-負載平衡器balancers)）。
- **路由**（提示：*「每條規則的優先順序很重要！」*，見 [11.3](#113-路由規則routing)）。
- **DNS / Fake DNS**（見 [11.6](#116-dns)）。

### 11.2. 基本設定（General）

#### Freedom Protocol Strategy

| 欄位 | 標籤 | 說明 | 預設值 |
|---|---|---|---|
| `FreedomStrategy` | **Freedom 協定策略設定** | 直連（freedom）outbound 的網路輸出策略。提示：*「設定 Freedom 協定中的網路輸出策略」*。控制 `freedom` 協定 outbound 的 `settings` 內 `domainStrategy` 欄位。 | 在參考範本中，freedom-outbound `direct` 的 `domainStrategy` 為 **`AsIs`**（位址不解析，以原始形式傳遞）。 |

freedom 的 `domainStrategy`（Xray-core 的值）：`AsIs`（不在伺服器端解析網域），以及 `UseIP` / `UseIPv4` / `UseIPv6` 系列及其「強制」變體 `ForceIP*`，後者會迫使輸出伺服器解析網域並以取得的 IP 連線。若輸出伺服器沒有 IPv6 或需要強制只走 IPv4，請改為 `UseIPv4`。

#### Freedom Happy Eyeballs (IPv4/IPv6)

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `FreedomHappyEyeballs` | **Freedom Happy Eyeballs (IPv4/IPv6)** | 提示：*「給直連（freedom）outbound 的雙堆疊組合——在同時具備 IPv4 與 IPv6 的輸出伺服器上很有用。」* 為 freedom-outbound 啟用 Happy Eyeballs 演算法（同時嘗試兩種位址系列）。 |
| try delay | （提示） | *「嘗試另一個位址系列前的毫秒數。150–250 毫秒是不錯的起點。」* 切換到替代位址系列前的延遲。建議範圍為 150–250 毫秒。 |

#### Overall Routing Strategy

| 欄位 | 標籤 | 說明 | 預設值 |
|---|---|---|---|
| `RoutingStrategy` | **網域路由設定** | 路由的整體 DNS 解析策略。提示：*「設定 DNS 解析的整體路由策略」*。控制 `routing.domainStrategy` 欄位。 | 在參考範本中 `routing.domainStrategy` = **`AsIs`**。 |

`routing.domainStrategy` 決定如何將 IP 路由規則與網域請求進行比對：`AsIs`（僅網域規則，不解析）、`IPIfNonMatch`（若網域未符合任何規則——則解析並檢查 IP 規則）、`IPOnDemand`（一遇到 IP 規則就立即解析）。要讓 IP 規則（例如 `geoip:*`）對網域請求也生效，通常需要 `IPIfNonMatch`。

#### Outbound Test URL

| 欄位 | 標籤 | 說明 | 預設值 |
|---|---|---|---|
| `outboundTestUrl` | **外送測試用 URL** | 測試 outbound 時用於檢查連通性的 URL。提示：*「用於檢查外送連線的 URL」*。與範本分開儲存，以鍵 `xrayOutboundTestUrl` 保存。 | **`https://www.google.com/generate_204`** |

該值會經過清理（sanitize）。在實際測試 outbound 時，它還會額外作為公開 URL 進行驗證——這是防止 SSRF 的保護：使用者無法透過用戶端塞入任意（包括內部）URL，測試 URL 永遠取自伺服器端設定。儲存／測試時若為空值，會被替換為預設的 `generate_204`。

#### Block BitTorrent

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `Torrent` | **封鎖 BitTorrent** | 在 `routing.rules` 中加入一條規則，將帶有 `protocol: ["bittorrent"]` 的流量送往 outbound `blocked`。在參考範本中，此規則預設存在。 |

#### 連線限制（Connection Limits）

提示：*「等級 0 使用者的連線層級政策。將欄位留空以使用 Xray 的預設值。」* 這些參數寫入 `policy.levels.0`。

| 欄位 | 標籤 | 說明 | 預設值 |
|---|---|---|---|
| `connIdle` | **閒置逾時**（秒） | *「在閒置達到指定秒數後關閉連線。降低此值可在高負載伺服器上更快釋放記憶體與檔案描述符（Xray 預設值：300）。」* | 空 → Xray 預設 **300** |
| `bufferSize` | **緩衝區大小**（KB） | *「每條連線的內部緩衝區大小（KB）。在記憶體較小的伺服器上設為 0 以最小化記憶體使用（Xray 預設值依平台而定）。」* 佔位文字：**「自動」**。 | 空 → 依平台而定；`0` — 最小化 |

**範例（`policy.levels.0`）。** 此分組的欄位會寫入等級 0 的政策。在記憶體較小的高負載伺服器上，可以這樣加快資源釋放：

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

此處連線在閒置 120 秒後即關閉（而非預設的 300），而 `bufferSize: 0` 將緩衝區的記憶體耗用降到最低。表單中留空的欄位根本不會進入 JSON——Xray 會套用自己的預設值。

### 11.3. 路由規則（routing）

`routing.rules` 規則清單。**順序至關重要**（*「每條規則的優先順序很重要！」*）：規則由上而下評估，第一條符合的即生效。提示：*「拖曳以變更順序」*。順序控制按鈕：**第一**、**最後**、**上移**、**下移**。

每條規則的 `type: "field"`。按鈕：**建立規則**、**編輯規則**。清單型欄位的提示：*「以逗號分隔的項目」*。

在「路由」頁面，**「匯入規則」**與**「匯出規則」**按鈕被收進**「更多」**(more) 下拉選單——與「外送」頁面相同。**「匯出規則」**按鈕不會立即下載檔案，而是開啟一個帶有 JSON 預覽以及**「複製」**與**「下載」**按鈕的對話框：可以在儲存前先檢視內容。「外送」頁面上的外送匯出也是同樣的運作方式。

#### Route Tester（路由測試器）

Routing 分頁上有一個子分頁 **Route Tester**——它會詢問執行中的 Xray，某條特定連線會由哪個 outbound 處理，而不會真的送出流量。指定網域或 IP、連接埠、網路（TCP/UDP），必要時再加上 inbound 與嗅探到的協定（`http`/`tls`/`quic`/`bittorrent`），然後按 **Test Route**。判定直接取自運作中的路由引擎。

回應會顯示選中的 outbound，若使用了負載平衡器——還會附上負載平衡器的標籤。若沒有任何規則符合，測試器會告知流量走預設 outbound（`outbounds` 清單中的第一個）。在依賴規則之前先檢驗其順序時，這很方便。

#### 啟用與停用個別規則

可以用切換開關暫時**停用**單條路由規則，而不必刪除它。在規則表格中有一個帶切換開關 (Switch) 的**「啟用」**欄，而在規則表單中也有一個**「啟用」**欄位——同樣是切換開關。被停用的規則不會進入最終的 Xray 設定，但仍保存在範本中，隨時可以再次啟用。

統計服務專用規則（`inboundTag: ["api"] → outboundTag: "api"`）無法停用——它的切換開關被鎖定，以免破壞面板的流量計量（見 [11.10](#1110-日誌與統計statsmetrics)）。

#### 規則表單欄位

| 表單欄位 | 標籤 | JSON 欄位 | 說明 |
|---|---|---|---|
| 來源 | **來源** | `source` | 來源 IP 位址／子網。以逗號分隔的清單。 |
| 來源連接埠 | **來源連接埠** | `sourcePort` | 來源的連接埠。 |
| 目的地 | **目的地** | `domain` + `ip` + `port` | 目標網域、IP 與連接埠。網域支援前綴 `domain:`、`full:`、`regexp:`、`keyword:` 以及 `geosite:*`；IP 支援 `geoip:*` 與 CIDR。 |
| 網路 | — | `network` | `tcp`、`udp` 或 `tcp,udp`。 |
| 協定 | — | `protocol` | `http`、`tls`、`bittorrent`（由 sniffing 判定）。 |
| 使用者 | **使用者** | `user` | 按 e-mail／使用者識別碼過濾。 |
| 屬性 / 值 | **屬性** / **值** | `attrs` | 用於比對的 HTTP 標頭屬性。 |
| VLESS route | **VLESS route** | — | 按 VLESS 的 route 欄位路由。 |
| 入站標籤 | **入站標籤** | `inboundTag` | 規則所套用的一個或多個 inbound 標籤（含內建的 `api`，以及 DNS 設定中的 DNS 標籤）。在 inbound 清單中，若 inbound 設有單獨備註，會顯示為「tag (remark)」，否則僅顯示標籤；在已儲存的規則中仍只保存標籤。 |
| 外送標籤 | **外送標籤** / **外送連線** | `outboundTag` | 符合的流量送往何處。 |
| 負載平衡器標籤 | **負載平衡器標籤** / **負載平衡器** | `balancerTag` | 提示：*「透過其中一個已設定的負載平衡器導向流量」*。 |

> `outboundTag` 與 `balancerTag` 互斥：*「無法同時使用 balancerTag 與 outboundTag。若同時使用，只有 outboundTag 會生效。」* 同一條規則中只設定外送標籤或負載平衡器標籤其一。

#### 參考範本的內建規則

在標準 `config.json` 中，`routing` 區段包含三條規則（依此順序）：

1. `inboundTag: ["api"] → outboundTag: "api"` — 面板統計 gRPC-API 的服務專用規則。
2. `ip: ["geoip:private"] → outboundTag: "blocked"` — 封鎖私有位址範圍。
3. `protocol: ["bittorrent"] → outboundTag: "blocked"` — 封鎖 BitTorrent。

> `api → api` 規則在儲存時永遠會被自動提升到位置 0（見 [11.10](#1110-日誌與統計statsmetrics)），以免統計請求被上方的 catch-all 規則「吃掉」。

**規則範例。** 將前往俄羅斯網站與私有網路的所有流量直連（不經代理），其餘流量送往負載平衡器。順序很重要：「直連」規則必須排在 catch-all 之前。在 `routing.rules` 中：

```json
{
  "type": "field",
  "domain": ["geosite:category-ru", "domain:example.ru"],
  "ip": ["geoip:ru", "geoip:private"],
  "outboundTag": "direct"
}
```

要讓 IP 規則（`geoip:ru`）對網域請求也生效，通常需要在路由的頂層設定 `routing.domainStrategy: "IPIfNonMatch"`（見 [11.2](#112-基本設定general)）。

#### 預設路由分組（基礎連線）

在「基礎連線」模式下，面板會協助你從現成清單組建常見規則：

| 分組 | 欄位 | 提示 |
|---|---|---|
| 按協定／網站封鎖 | — | *「設定以使用戶端無法存取特定協定」* |
| 按國家封鎖 | **封鎖的 IP 位址**、**封鎖的網域** | *「這些參數會依目的地國家封鎖流量。」* |
| 直連 | **直連 IP 位址**、**直連網域** | *「直連表示特定流量不會經由其他伺服器轉送。」* |
| IPv4 規則 | — | *「這些參數會讓用戶端只透過 IPv4 路由到目標網域」* |
| WARP 規則 | — | *「這些選項會依特定目的地透過 WARP 導向流量。」* |
| NordVPN 路由 | — | *「這些選項會依特定目的地透過 NordVPN 導向流量。」* |

#### MTProto-inbound：透過 Xray 路由 Telegram 流量

MTProto-inbound 有一個切換開關**「Route through Xray」**（預設關閉）以及一個選填的 **Outbound** 選擇。啟用時，面板會在 Xray 設定中加入一個帶有該 inbound 標籤的迴路 SOCKS 橋接，mtg 便會透過它導向 Telegram 流量。此後，Telegram 的外送流量由路由器掌控：可以在 Routing 分頁上用一般規則按 inbound 標籤比對它，或透過 **Outbound** 欄位強制送往選定的 outbound 或負載平衡器。將 **Outbound** 留空，則由路由規則決定。

### 11.4. Outbounds（外送連線）

`outbounds` 清單。按鈕：**建立外送連線**、**修改外送連線**。提示：*「修改設定範本以定義此伺服器的外送連線」*。

在參考範本中有兩個必備的 outbound：

- `protocol: "freedom"`、`tag: "direct"` — 直接連出網際網路（帶 `domainStrategy: "AsIs"` 與 `finalRules: [{action: "allow"}]`）；
- `protocol: "blackhole"`、`tag: "blocked"` — 給被封鎖流量的「黑洞」。

#### outbound 表單的通用欄位

| 欄位 | 標籤 | 說明 |
|---|---|---|
| 標籤 | **標籤**（提示：*「唯一標籤」*） | outbound 的唯一識別碼。佔位文字：*「唯一標籤」*。驗證：*「標籤為必填」*、*「該標籤已被其他外送使用」*。 |
| 協定 | — | 外送類型（見下）。 |
| 位址 / 連接埠 | **位址** / 連接埠 | 連線目標。位址與連接埠為必填。 |
| 透過此處送出 | **透過此處送出** | 外送介面的本機 IP 位址（`sendThrough`）。佔位文字：*「本機 IP」*。 |
| Dialer proxy（鏈接） | — | 提示：*「透過另一個外送（按標籤）連接此外送，以建立代理鏈。留空則為直連。」* 佔位文字：*「選擇用於鏈接的外送」*。透過 `streamSettings.sockopt.dialerProxy` 實作。 |

#### 支援的 outbound 協定

表單支援的協定：

- **`freedom`** — 直接連出。欄位 `settings.domainStrategy`、`finalRules`（見下）、Happy Eyeballs。不可測試（*「Outbound has no testable endpoint」*）。
- **`blackhole`** — 丟棄流量。欄位 **回應類型**。不可測試。
- **`socks`**、**`http`** — 帶 `address`/`port` 的 `settings.servers[]` 清單；欄位 **授權密碼**。
- **`vmess`** — `settings.vnext[]`（`address`/`port`）。
- **`vless`** — `settings.address`/`settings.port`。
- **`trojan`**、**`shadowsocks`** — `settings.servers[]`。
- **`wireguard`** — 帶 `endpoint` 的 `settings.peers[]`，外加金鑰（見 [11.7](#117-fake-dns)）。
- **`hysteria`** — `settings.address`/`settings.port`（UDP 傳輸）。

對於 **loopback** 類型的 outbound，可用一個 **Sniffing** 區塊，其參數與 inbound 相同：啟用、**destOverride**、**Metadata Only**、**Route Only** 以及**排除網域**清單。

在 **Hysteria2** 的 **UDP** 遮罩（FinalMask）中提供額外模式。**Salamander** 遮罩有一個 **Mode** 選擇器，其值為 **Salamander** 與 **Gecko**：Gecko 模式會以 **Min**/**Max** 大小欄位（`packetSize`，範圍 1–2048，預設 512–1200）為封包加入隨機填充——這可防止依封包長度做指紋識別。**Realm** 遮罩（UDP hole-punching）新增了一個選填的 **TLS Config** 區塊，含 **Server Name** (SNI)、**ALPN**（`h3`/`h2`/`http/1.1`）、**Fingerprint** (uTLS) 與 **Allow Insecure** 切換開關等欄位。

**範例：透過上游 SOCKS 的鏈接。** outbound `upstream` 走外部 SOCKS5 代理，而 `chained` 透過它（`dialerProxy`）送出自己的流量，形成一條鏈。在 `outbounds` 中：

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

如此一來，帶 `outboundTag: "chained"` 的路由規則便會透過 `upstream` 將流量送出網際網路。

#### 從分享連結匯入 outbound

可以從分享連結（`vless://`、`vmess://` 等）匯入 outbound。匯入時也會保留以連結 `extra=` 區塊傳遞的多工器 **xmux**（XHTTP）設定：匯入後，它們的值會填入所建立 outbound 的 **XMUX** 子表單。

#### Mux 欄位（多工）

**最大平行度**、**最大連線數**、**最大重複使用次數**、**最大請求數**、**最大重複使用秒數**、**keep alive 週期**。這些參數設定外送的 mux/XUDP 行為。

#### Sockopts（通訊端設定）

**Sockopts** 分組：**keep alive 間隔**、**Mark (fwmark)**、**介面**、**僅 IPv6**、**接受 proxy protocol**、**Proxy protocol**、**TCP user timeout (毫秒)**、**TCP keep-alive idle (秒)**。鏈接的 dialer-proxy 也在此設定。

#### Freedom finalRules（覆寫私有 IP 封鎖）

對於 freedom-outbound，可用 **最終規則** 分組：

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `overrideXrayPrivateIp` | **覆寫 Xray 中私有 IP 的預設封鎖** | 解除 Xray 內建對外送至私有 IP 的禁止。 |
| `action` | **動作** | `allow`（如參考範本：`finalRules: [{action: "allow"}]`）、`redirect`（**Redirect**）或其他。 |
| `blockDelay` | **封鎖延遲 (毫秒)** | 丟棄連線前的延遲。 |
| `redirect` / `fragment` | **Redirect** / **Fragment** | 流量重新導向與分片動作。 |

#### fragment 遮罩：分段的 Lengths 與 Delays

在 **fragment** 遮罩（FinalMask 中的 fragment 類型，用於 TCP）中，單一的 Length 與 Delay 欄位已改為清單 **Lengths** 與 **Delays**：可為每個分段分別指定長度範圍（例如 `100-200`）與毫秒延遲（例如 `10-20` 或 `0`）。清單的列可以新增與刪除；先前儲存的單一值會自動轉成只含一個元素的陣列。

#### 其他表單欄位

- **UDP over TCP** 與 **UoT 版本** — 用於 shadowsocks 類協定。
- **不帶 gRPC 標頭**、**Uplink chunk 大小** — gRPC 傳輸的參數。
- TLS/uTLS 欄位：**驗證 peer 名稱**、**Pinned SHA256**、**Short ID**、**Vision testpre**，佔位文字「伺服器名稱」。

#### 測試外送

按鈕：**測試**、**測試全部**。狀態：**測試連線中…**、**測試成功**、**測試未通過**、**無法測試外送連線**。結果：**測試結果**、毫秒延遲。

兩種模式（提示：*「TCP：快速的 dial-only 探測。HTTP：透過 xray 的完整請求。」*）：

- **TCP**（`mode=tcp`）— 對 `host:port` 的簡單 dial，會對所有端點平行執行，逾時約 5 秒。只檢查 TCP 可達性，不驗證代理協定。對 `freedom`/`blackhole`/標籤 `blocked` 會回傳 *「Outbound has no testable endpoint」*。
- **HTTP**（`mode=http` 或留空）— 啟動一個臨時的 Xray 實例，跑一次真實的 HTTP 請求（探測 URL = 伺服器端的 `outboundTestUrl`），測量真實延遲。權威但昂貴的模式：以全域鎖序列化（*「Another outbound test is already running, please wait」*）。單次嘗試逾時為 10 秒，結果等待視窗為 15 秒（已調高，以免在慢速或隧道化通道上的健康 outbounds 被標記為「Failed」）。失敗時，真正的原因（DNS 錯誤、connection refused、逾時、TLS 錯誤等）會寫入面板/Xray 日誌，而通用的逾時訊息會指向該日誌。

> UDP 協定（`wireguard`、`hysteria`）與 UDP 傳輸（`kcp`、`quic`、`hysteria`）**永遠**以 HTTP 模式測試，即使要求 TCP——裸 UDP dial 無法區分端點是「活的」還是「死的」。對 wireguard，測試設定中會強制設 `noKernelTun: true`。

#### 批次測試與分階段拆解

**測試**與**測試全部**在 HTTP 模式下會為一批 outbounds 啟動一個共用的臨時 Xray 實例，為每個 outbound 建立一個帶規則的迴路 SOCKS-inbound，並透過它平行送出真實 HTTP 請求；**測試全部**會分批測試 outbounds。**測試全部**也會測試由訂閱取得的 outbounds（唯讀的「來自訂閱」表格）——它們的列也會以測試結果標示。同時，`freedom`（「direct」）與 `dns` 兩個 outbound 在任何模式下都不會被測試（它們不是代理）：其測試按鈕為不可用，**測試全部**會略過它們，而伺服器端保護即使在直接呼叫 API 時也會禁止對它們做 HTTP 測試。除了成功／失敗外，結果彈窗還會顯示回應的 HTTP 狀態以及按階段拆分的時間：**Proxy connect**（連接到代理）、**TLS via outbound**（透過 outbound 的 TLS）與 **First byte**（到第一個位元組的時間）——這有助於了解延遲或故障發生在哪一步。

#### outbounds 流量統計

面板會按標籤記錄流量計數（`up`/`down`/`total`）。重設按鈕可重設特定標籤或全部標籤的計數（`tag = "-alltags-"`）。**帳戶資訊** 與 **外送連線狀態** 欄位顯示摘要。

### 11.5. 負載平衡器（Balancers）

`routing.balancers` 清單。按鈕：**建立負載平衡器**、**編輯負載平衡器**。

Balancers 分頁有顯示即時狀態的欄位：**Live Target** 顯示負載平衡器在運作中的 Xray 內目前的活躍目標，**Override** 則可手動覆寫目標的選擇（值 **Auto (strategy)** 會回復為按策略選擇）。狀態由一個獨立按鈕更新。若負載平衡器在運作中的 Xray 內尚未啟用，面板會建議先儲存變更或啟動 Xray。

| 欄位 | 標籤 | 說明 |
|---|---|---|
| 標籤 | **標籤**（提示：*「唯一標籤」*） | 唯一識別碼。佔位文字：*「唯一的負載平衡器標籤」*。驗證：*「標籤為必填」*、*「該標籤已被其他負載平衡器使用」*。 |
| 選擇器 | **選擇器** | outbound 標籤清單（按子字串），負載平衡器從中選擇出口。至少要選一個：*「請至少選擇一個外送」*。 |
| Fallback | **Fallback** | 若沒有任何選擇器符合時的備援 outbound 標籤。 |
| 策略 | **策略** | 選擇演算法（見下）。 |

#### 策略與觀察參數

策略（`strategy.type`）決定負載平衡器如何從選擇器中挑選 outbound。Xray-core 的值：`random`（隨機）、`roundRobin`（輪流）、`leastPing`（依 observatory 結果取最小延遲）、`leastLoad`（最小負載）。`leastLoad`/`leastPing` 會使用 `strategy.settings` 中的參數：

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `expected` | **期望值** | 佔位文字：*「最佳的節點數」*——目標的活躍節點數。 |
| `maxRtt` | **最大 RTT** | 篩選候選時可接受 RTT 的上限。 |
| `tolerance` | **容差** | 比較延遲／負載時的容差 (tolerance)。 |
| `baselines` | **Baselines** | 用於將節點分組的延遲門檻值。 |
| `costs` | **Costs** | 個別標籤的權重係數 (cost)。 |

**策略範例。** `strategy` 區塊位於負載平衡器內部（在 JSON 中——與 `tag` 和 `selector` 相鄰）：

```json
"strategy": { "type": "random" }      // 從選擇器中隨機挑選
"strategy": { "type": "roundRobin" }  // 輪流，依序使用
"strategy": { "type": "leastPing" }   // 最小延遲（需要觀察器）
```

對於 `leastLoad`，參數在 `settings` 中設定：

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

**它如何運作（以範例說明）。** 假設觀察器測得各出口的延遲為：`A = 250 毫秒`、`B = 280 毫秒`、`C = 700 毫秒`、`D = 1500 毫秒`。以上述設定，選擇流程如下：

1. **`maxRTT: "1s"`** — 延遲高於 1 秒的出口被剔除：`D`（1500 毫秒）出局。剩下 `A`、`B`、`C`。
2. **`baselines` + `expected`** — 出口按延遲門檻分組，並取**最小**的、其中落入不少於 `expected` 個出口的門檻。門檻 `500ms` 已含有 `A` 與 `B`——即 2 個（= `expected`），因此選中分組 {`A`, `B`}。只要快的夠用，`C`（700 毫秒）就不進入選擇（它是「熱備援」）。
3. **`tolerance: 0.05`** — 在選中的分組內，延遲差異不超過 5% 的出口被視為等價，負載在它們之間均分。`A`（250）與 `B`（280）相差約 12%（> 5%），因此在其他條件相同時，偏好較快的 `A`；若差異在 5% 之內——流量則會同時走 `A` 與 `B`。
4. **`costs`** — 在比較之前，調整個別出口的「成本」：較小的 `value` 使出口更具吸引力，較大的則相反。範例中 `proxy-premium` 得到 `0.1`（變得「更便宜」、更易被選中），而所有 `proxy-cheap-*`（按正規表示式，`regexp: true`）得到 `5`（變得「更貴」、最後才用）。如此即可柔性地優先使用某些出口，而不必硬性排除它們。

結論：流量主要走 `A`（在延遲相近時——與 `B` 均分），`C` 留作備援，`D` 在其 RTT 未降到 `maxRTT` 以下前都被排除。

#### 觀察器：`observatory` 與 `burstObservatory`（為 `leastPing` / `leastLoad` 做的量測）

`leastPing` 與 `leastLoad` 策略本身不做任何量測——它們需要每個 outbound 的延遲與可用性資料。這些資料由**觀察器**（observatory）收集：它週期性地「ping」每個受監控的 outbound，並記下回應時間與可用性。同樣的資料也顯示在**「觀察站」**分頁（狀態 **使用中 / 無法連線**、**「最後活動」**、**「最後嘗試」**）。

面板中沒有觀察器的專屬表單——此區塊需在 Xray 設定編輯器中**手動**加入，置於設定的頂層（與 `routing` 和 `outbounds` 相鄰），之後需要**重新啟動 Xray**。

提供兩種選項：

- **`observatory`** — 簡易版：`subjectSelector` + `probeURL` + `probeInterval`。
- **`burstObservatory`** — 進階版，可透過 `pingConfig` 精細設定 ping；適合多個出口。

`burstObservatory` 區塊範例：

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

各欄位用途：

| 欄位 | 設定內容 |
|---|---|
| `subjectSelector` | 要觀察的 outbound **標籤前綴**清單。Xray 會取所有標籤以指定字串開頭的 outbound。範例中觀察的是出口 `WS-SE…`、`WS-FR…`、`WS-PL…`。這些標籤必須與負載平衡器**選擇器**中所選的一致。 |
| `pingConfig.destination` | **透過每個 outbound** 請求以量測延遲的 URL。取一個回應 `204` 且無內文的「輕量」頁面——例如 `https://www.google.com/generate_204`。到回應為止的時間即為量得的延遲。 |
| `pingConfig.interval` | 多久 ping 每個 outbound 一次。時長字串：`"1m"` — 每分鐘一次，也可 `"30s"`、`"5m"` 等。越頻繁——資料越新，但背景流量越多。 |
| `pingConfig.connectivity` | （選填）檢查伺服器本身**基本連通性**的 URL。若它無法連通——表示問題出在伺服器網路，觀察器**不會**將 outbound 標記為無法連線（防止本機故障時的誤判）。通常也是回應 `204` 的端點。 |
| `pingConfig.timeout` | 等待單次 ping 回應多久才視為失敗（例如 `"5s"`）。 |
| `pingConfig.sampling` | 為每個 outbound 保留並平均的最近量測筆數。`2` — 採計最近兩次 ping（平滑隨機跳動）。 |

如何將一切串起來：

1. 在 Xray 編輯器中加入帶有所需 `subjectSelector` 的 `burstObservatory` 區塊。
2. 建立負載平衡器：**策略** = `leastPing`，在**選擇器**中填入相同的 outbound 標籤（`WS-SE`、`WS-FR`、`WS-PL`）。
3. 用一條路由規則將流量導向它（**負載平衡器標籤**欄位，見 [11.3](#113-路由規則routing)）。
4. 重新啟動 Xray。**「觀察站」**分頁上會出現出口的狀態，負載平衡器則開始從活著的出口中挑選最快的。

> 同一條規則中不能同時設定 `balancerTag` 與 `outboundTag`——只有 `outboundTag` 會生效。

### 11.6. DNS

`dns` 區段。啟用：**啟用 DNS**（提示：*「啟用內建 DNS 伺服器」*）。

#### DNS 一般參數

| 欄位 | 標籤 | JSON | 說明 / 提示 |
|---|---|---|---|
| `tag` | **DNS 標籤名稱** | `dns.tag` | *「此標籤將可在路由規則中作為入站標籤使用。」* 允許將 DNS 請求本身透過 `inboundTag` 路由。 |
| `clientIp` | **用戶端 IP** | `dns.clientIp` | *「用於在 DNS 查詢期間向伺服器告知指定的 IP 位置」*（EDNS Client Subnet）。 |
| `strategy` | **查詢策略** | `dns.queryStrategy` | *「網域名稱解析的整體策略」*。值：`UseIP`、`UseIPv4`、`UseIPv6`。 |
| `disableCache` | **停用快取** | `dns.disableCache` | *「停用 DNS 快取」*。 |
| `disableFallback` | **停用備援 DNS** | `dns.disableFallback` | *「停用備援 DNS 查詢」*。 |
| `disableFallbackIfMatch` | **符合時停用備援 DNS** | `dns.disableFallbackIfMatch` | *「當符合 DNS 伺服器的網域清單時，停用備援 DNS 查詢」*。 |
| `enableParallelQuery` | **啟用平行查詢** | — | *「啟用向多個伺服器的平行 DNS 查詢以更快解析」*。 |
| `useSystemHosts` | **使用系統 Hosts** | `dns.useSystemHosts` | *「使用已安裝系統的 hosts 檔案」*。 |

**`dns` 區塊範例。** 對 Google 網域的請求透過 Cloudflare 的 DoH 伺服器解析，其餘一切透過 `1.1.1.1`；對 Google 的請求只接受非私有 IP。在設定的頂層：

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

字串型伺服器（`"1.1.1.1"`）不帶欄位——它是所有其他網域的預設伺服器。標籤 `dns-inbound` 之後可在路由規則中作為 `inboundTag` 使用，以將 DNS 請求本身導向所需的 outbound。

#### 過期記錄快取

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `serveStale` | **使用過期值** | *「在背景更新期間回傳快取中的過期結果」*。 |
| `serveExpiredTTL` | **過期 TTL** | *「過期快取記錄的有效期（秒）；0 = 永久」*。 |

#### DNS 伺服器（`dns.servers` 清單）

按鈕：**建立 DNS**、**編輯 DNS**、**全部刪除**（確認：*「所有 DNS 伺服器都將從清單中移除。此動作無法復原。」*）。範本：**使用範本**、**DNS 範本**對話框，含預設組 **家庭版**。

在 DNS 伺服器記錄上按 **編輯 DNS**（如同在 Fake DNS 記錄上一樣），編輯視窗會填入該伺服器已儲存的值，而非預設值。

DNS 伺服器欄位：

| 欄位 | 標籤 | 說明 |
|---|---|---|
| address | — | DNS 位址（IP、DoH-URL、`localhost`、`fakedns` 等）。 |
| `domains` | **網域** | 使用此伺服器的網域清單。 |
| `expectIPs` | **期望 IP** | 只在 IP 落入清單時才接受回應。 |
| `unexpectIPs` | **非期望 IP** | 丟棄帶有指定 IP 的回應。 |
| `skipFallback` | **略過 Fallback** | 不將此伺服器作為 fallback 使用。 |
| `finalQuery` | **最終查詢** | 將伺服器標記為鏈中的最終者。 |
| `timeoutMs` | **逾時（毫秒）** | 向伺服器查詢的逾時。 |

#### Hosts（靜態記錄）

**Hosts** 分組（`dns.hosts`）。按鈕 **新增 Host**；空狀態 **未定義 Host**。欄位：網域（佔位文字：*「網域（例如 domain:example.com）」*）與值（佔位文字：*「IP 或網域——輸入後按 Enter」*）。

#### DNS 日誌

見 [11.9](#119-reverse-代理與-tun)：日誌區段中的 **DNS 日誌** 旗標（`dnsLog`）。

### 11.7. Fake DNS

`fakedns` 區段。按鈕：**建立 Fake DNS**、**編輯 Fake DNS**。

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `ipPool` | **IP 池子網** | 用於配發虛擬 IP 的 CIDR 範圍（例如 `198.18.0.0/15`）。 |
| `poolSize` | **池大小** | 在環狀池中保留多少個位址。 |

Fake DNS 與 inbound 上的 sniffing 搭配使用：核心發給用戶端一個虛擬 IP，記住網域↔IP 的對應，並在路由時還原網域。要讓 Fake DNS 運作，必須在 DNS 伺服器清單中加入位址為 `fakedns` 的 DNS 伺服器。

**範例：Fake DNS + DNS 伺服器的搭配。** 先設定虛擬位址池，再加入 `fakedns` DNS 伺服器，讓網域請求取得此池中的 IP：

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

此外，還需在 inbound 上啟用帶 `destOverride: ["fakedns"]` 的 sniffing，否則核心無從取得真實網域以供還原。

### 11.8. WireGuard / WARP / NordVPN

#### WireGuard 欄位（`wireguard`）

| 欄位 | 標籤 | 說明 |
|---|---|---|
| `secretKey` | **祕密金鑰** | 本機介面的私鑰。 |
| `publicKey` | **公開金鑰** | peer 的公鑰。 |
| `psk` | **共用金鑰** | PreShared Key（選填）。 |
| `allowedIPs` | **允許的 IP 位址** | 路由到隧道的範圍。 |
| `endpoint` | **端點** | peer 的 `host:port`。 |
| `domainStrategy` | **網域策略** | WireGuard-outbound 的解析策略。 |

#### Cloudflare WARP（`warp`）

此整合使用 API `https://api.cloudflareclient.com/v0a4005`（client-version `a-6.30-3596`）。控制器動作（`/xray/warp/:action`）：`config`、`reg`、`license`、`data`、`del`。

逐步說明：

1. **建立 WARP 帳戶** → `reg`：面板產生／接受私鑰（`privateKey`）與公鑰（`publicKey`），在 Cloudflare 註冊裝置，並將 `access_token`、`device_id`、`license_key`、`private_key`（以及 `client_id`）儲存到設定 `warp` 中。
2. **WARP / WARP+ 授權金鑰** → `license`：設定 26 字元的 WARP+ 金鑰（佔位文字：*「26 字元的 WARP+ 金鑰」*）。錯誤時：*「無法設定 WARP 授權。」* 若尚未取得設定：*「請先取得 WARP 設定。」*
3. **帳戶資訊**：**裝置名稱**、**裝置型號**、**裝置已啟用**、**帳戶類型**、**角色**、**WARP+ data**、**配額**、**用量**。
4. **新增外送** — 以取得的金鑰與 Cloudflare 端點建立一個 WireGuard-outbound。
5. **刪除帳戶** → `del`：清除已儲存的 WARP 資料。

#### NordVPN（`nord` / `nordvpn`）

此整合使用 NordLynx（= WireGuard）。控制器動作（`/xray/nord/:action`）：`countries`、`servers`、`reg`、`setKey`、`data`、`del`。

逐步說明：

1. **存取權杖** → `reg`：面板向 `api.nordvpn.com` 請求 NordLynx 憑證並擷取 `nordlynx_private_key`。將 `private_key` 與 `token` 儲存到設定 `nord` 中。替代方式——`setKey`：直接輸入**私鑰**（不可為空）。
2. **國家** → `countries` 載入國家清單；**城市**（或**所有城市**）。
3. **伺服器** → `servers` 載入所選國家的伺服器（`countryId` 會被驗證為數字——防止注入）。過濾條件：只顯示**負載** > 7% 的伺服器。若沒有伺服器：*「找不到所選國家的伺服器」*。若伺服器未提供 NordLynx 公鑰：*「所選伺服器未回報 NordLynx 公鑰。」*
4. 建立／更新外送：提示訊息 *「已新增 NordVPN 外送」* / *「已更新 NordVPN 外送」*。

#### IPv4 優先與 userspace TUN

由 WARP 與 NordVPN 精靈產生的 WireGuard-outbounds 使用 `domainStrategy: "ForceIPv4v6"`（IPv4 優先，在 v6-only 主機上回退到 IPv6），而非 `ForceIP`——這消除了在 IPv6 設定一半的主機上、當選到 Cloudflare 端點的 AAAA 記錄時握手「卡住」的問題。此外，它們啟用了 userspace TUN（`noKernelTun: true`）而非 kernel TUN：後者需要權限與 fwmark 路由，並在許多 VPS 上靜默失敗，而面板內建的連線檢查向來透過 userspace TUN 測試——如今實際流量與檢查走的是同一條路徑。此變更只對新加入或重設的 outbounds 生效；已儲存的範本保留各自的設定。

### 11.9. Reverse 代理與 TUN

#### Reverse（反向代理）

Xray 設定的 `reverse` 區段。outbound 表單中有一個切換到 **反向代理** 類型的開關。按鈕：**建立反向代理**、**編輯反向代理**。

| 欄位 | 標籤 | 說明 |
|---|---|---|
| 類型 | **類型** | **Bridge** 或 **Portal** — Xray 反向代理的兩種角色。 |
| 網域 | **網域** | bridge↔portal 配對用的服務標籤網域。 |
| 標籤 / 連線 | **標籤** / **連線** | 串接 bridge 與 portal 的標籤。 |
| Reverse Tag | **反向代理標籤** | 提示：*「給簡易 VLESS 反向代理的外送連線標籤。留空則停用。」* 佔位文字：*「外送標籤（空 = 停用）」*。實作簡化版的 VLESS reverse。 |

outbound 表單中還有反向串流的欄位：**反向 sniffing**、**Workers**、**保留位**、**最小下載間隔 (毫秒)**、**最大下載大小 (位元組)**。

#### TUN（`tun`）

| 欄位 | 標籤 | 說明 | 預設值 |
|---|---|---|---|
| name | — | *「TUN 介面名稱。」* | **`xray0`** |
| mtu | — | *「最大傳輸單元。資料封包的最大大小。」* | **1500** |
| `userLevel` | **使用者等級** | *「透過此入站流建立的所有連線都將使用此使用者等級。」* | **0** |

### 11.10. 日誌與統計（Stats、metrics）

#### 日誌（`log`）

提示：*「日誌可能拖慢伺服器運作。請只在必要時啟用你所需的日誌種類！」* 參考範本的 `log` 區段：`access: "none"`、`error: ""`、`loglevel: "warning"`、`dnsLog: false`、`maskAddress: ""`。

| 欄位 | 標籤 | JSON | 說明 | 預設值 |
|---|---|---|---|---|
| `logLevel` | **日誌等級** | `loglevel` | *「錯誤日誌的日誌等級…」* 值：`debug`、`info`、`warning`、`error`、`none`。 | **`warning`** |
| `accessLog` | **存取日誌** | `access` | *「存取日誌檔的路徑。特殊值「none」會停用存取日誌。」* | **`none`** |
| `errorLog` | **錯誤日誌** | `error` | *「錯誤日誌檔的路徑。特殊值「none」會停用錯誤日誌。」* | **`""`**（預設） |
| `dnsLog` | **DNS 日誌** | `dnsLog` | *「啟用 DNS 查詢日誌」* | **false** |
| `maskAddress` | **位址遮罩** | `maskAddress` | *「啟用後，日誌中的真實 IP 位址會被替換為遮罩位址。」* | **`""`**（關閉） |

#### 統計（`stats` / `policy`）

**統計** 分組。在 `policy.system` 與 `policy.levels` 中啟用計數器。在參考範本中：`statsInboundUplink: true`、`statsInboundDownlink: true`、`statsOutboundUplink: false`、`statsOutboundDownlink: false`；對等級 `0`——`statsUserUplink: true`、`statsUserDownlink: true`。

| 欄位 | 標籤 | 說明 | 預設值 |
|---|---|---|---|
| `statsInboundUplink` | **入站上行統計** | *「為所有入站代理的外送流量啟用統計收集。」* | **true** |
| `statsInboundDownlink` | **入站下行統計** | *「為所有入站代理的入站流量啟用統計收集。」* | **true** |
| `statsOutboundUplink` | **外送上行統計** | *「為所有外送代理的外送流量啟用統計收集。」* | **false** |
| `statsOutboundDownlink` | **外送下行統計** | *「為所有外送代理的入站流量啟用統計收集。」* | **false** |

> 按用戶端與 inbounds 的統計（上行/下行）是儀表板與用戶端流量顯示的基礎；不建議停用。outbound 統計預設關閉，只有在你需要按外送標籤追蹤流量時才需要。

#### Metrics

參考範本中含有 `metrics` 區段（`listen: "127.0.0.1:11111"`、`tag: "metrics_out"`）以及對應的 API `metrics_out`。面板使用此 listener 收集指標與 observatory 快照：它從範本解析 `metrics.listen`、輪詢 `/debug/vars`，並按標籤彙整延遲歷史。若你變更 `metrics.listen` 的位址/連接埠，面板會改連新位址；移除 `metrics` 區段則會停用 observatory 圖表的收集。

> HTTP 模式的 outbound 測試會啟動一個**獨立的臨時** Xray 實例，帶有它自己、位於隨機連接埠的 `metrics`-listener——這與主設定中的 listener 不是同一個。

### 11.11. 儲存、重新啟動與自動轉換

#### 按鈕

| 按鈕 | 動作 |
|---|---|
| **儲存** | `POST /xray/update`：驗證並儲存範本 + `outboundTestUrl`。 |
| **重新啟動 Xray** | 以已儲存的設定重新載入服務。確認：*「重新啟動 xray？」* / *「以已儲存的設定重新載入 xray 服務。」* |

提示訊息：成功——*「Xray 已成功重新啟動」*、*「Xray 已成功停止」*；錯誤——*「重新啟動 Xray 時發生錯誤。」*、*「停止 Xray 時發生錯誤。」* **Xray 重新啟動輸出** 視窗會顯示核心的診斷輸出。

#### 熱套用變更（不需完整重啟）

inbounds、outbounds 與路由規則的變更會「即時」套用：按下**儲存**時，面板會計算新舊設定之間的差異，並透過 Xray 的 gRPC-API（HandlerService/RoutingService）只套用變動的部分，而不重啟程序。只有在變更沒有熱重載 API 的區段（`log`、`dns`、`policy`、`observatory` 等）時，才會自動執行完整重啟。因此在 Xray 頁面不需要獨立的「重新啟動」按鈕——**儲存** 本身就會套用變更。需要時，核心仍會自動重啟（另見訂閱更新與 WARP 輪換時的自動重載）。

#### 還原為預設範本

端點 `GET /xray/getDefaultJsonConfig` 會回傳參考範本（內建於二進位檔的 `config.json`）。可用它將設定重設為出廠狀態。

#### 儲存時的自動轉換

儲存 Xray 設定時，面板會執行（依此順序）：

1. **拆除包裹** — 若值中意外混入形如 `{ "xraySetting": <設定>, "inboundTags": …, "outboundTestUrl": … }` 的包裹，便將其拆除（否則每次儲存都會層層累積）。最多拆除 8 層。
2. **設定驗證** — JSON 被解析為 Xray 設定結構；出錯時——以 *「xray template config invalid」* 拒絕。
3. **保證統計規則** — `inboundTag: ["api"] → outboundTag: "api"` 規則會被強制提升到 `routing.rules` 的位置 0（若不存在則加入）。這保證面板的 gRPC-統計請求不會被上方的 catch-all 規則攔截（否則在代理運作時，用戶端可能顯示為離線且零流量）。

> 由於第 3 點，請勿試圖移除或移動 `api → api` 規則——面板在下次儲存時仍會把它放回原處。這是統計服務的基礎建設，而非使用者路由。

### 11.12. 來自訂閱的 outbound（含自動更新）

從 3.3.0 版起，面板可以直接從訂閱 URL 匯入 `outbound`——格式與 VPN 供應商提供給用戶端應用程式的相同。訂閱會在背景定期重新讀取，因此伺服器上的 `outbound` 集合無需手動編輯設定範本即可保持最新。

在中文介面中，此區段稱為**「外送訂閱」**，說明為：「從遠端訂閱 URL 匯入外送（vmess/vless/trojan/ss/...）。標籤保持不變，以便用於負載平衡器與路由規則。更新自動執行。」此區段位於 Xray 頁面、`outbound` 設定面板的上方。

#### 它如何運作

訂閱與 Xray 設定範本分開儲存。範本**永遠不會被覆寫**：每次產生 Xray 設定時，從訂閱取得的 `outbound` 會即時加入最終設定。

#### 新增訂閱

在「新增訂閱」表單中提供以下欄位：

| 欄位 | 鍵 | 預設值 | 用途 |
|------|------|--------------|------|
| 訂閱 URL | `url` | —（必填） | 訂閱位址。佔位文字：「https://...（base64 連結清單）」。只接受 HTTP(S)；位址會經過安全性檢查。 |
| 備註 | `remark` | 空 | 任意標籤（佔位文字「例如 HK 節點」）。 |
| 標籤前綴 | `tagPrefix` | `subN-` | 匯入 `outbound` 標籤的起始前綴。若留空，面板會自選最小的可用編號，形如 `sub1-`、`sub2-` 等。 |
| 更新間隔 | `updateInterval` | 600 秒（10 分鐘） | 訂閱多久重新讀取一次。在 UI 中以小時/分鐘設定。 |
| 已啟用 | `enabled` | 是（`true`） | 只有已啟用的訂閱會進入設定並自動更新。 |
| 允許私有位址 | `allowPrivate` | 否（`false`） | 允許 localhost、LAN 與私有 IP 的 URL。基於防 SSRF 預設關閉——只在可信的本機來源時才開啟。 |
| 置於手動外送之前 | `prepend` | 否（`false`） | 若啟用，此訂閱的 `outbound` 會排在範本的手動 `outbound` **之前**，其中之一可能成為預設 `outbound`。否則它們會排在**之後**。 |

**「預覽」**按鈕（`POST /outbound-subs/parse`）讓你在儲存前先下載並解析 URL，看看會得到哪些 `outbound` 與標籤；此過程不會寫入任何資料到資料庫。若該 URL 未辨識到任何內容，會顯示「此 URL 找不到外送。」

多個訂閱在 `outbound` 總清單中的順序由優先順序（`priority`）決定，並以上/下箭頭變更（`POST /outbound-subs/:id/move`）。

#### 接受哪些訂閱格式

按 URL 取得的回應主體處理方式如下：

- 內容首先嘗試作為 **base64**（標準與 URL-safe 變體，會自動補齊 padding 並移除空白/換行）。若是 base64——便解碼；否則照原樣取用。
- 接著主體會按行拆分。每一個非空、且不以 `#` 開頭的行都會被解析為一條連結。未辨識的行（註解、不支援的協定）會被靜默略過。
- 支援的連結方案：`vmess://`、`vless://`、`trojan://`、`ss://`（Shadowsocks）、`hysteria2://` / `hy2://`、`wireguard://` / `wg://`。

也就是說，像大多數供應商那樣的一般「base64 編碼的連結清單」訂閱即可。

#### 穩定標籤

每條連結都會計算出一個穩定的「身分」（不含備註片段的 URI 核心；對 vmess——不含 `ps` 欄位的內部 JSON）。「身分 → 標籤」的對應會被保存，於下次更新時同一伺服器會取得同一標籤，即使備註或次要參數有所改變。這是刻意設計的，好讓負載平衡器與路由規則在更新後仍持續運作：

- 負載平衡器/規則中的精確標籤會繼續指向同一伺服器。
- 前綴/萬用字元選擇器（例如 `hk-*`）會自動納入訂閱之後回傳的新伺服器——這是「訂閱一個池」的建議做法。
- 若某伺服器從訂閱中消失，其標籤只會從最終的 `outbound` 陣列中消失；若負載平衡器設有 `fallbackTag`，Xray 會改用它。
- 若供應商更換了伺服器的 UUID/主機/憑證，身分便改變——這會被視為帶有新標籤的新 `outbound`。

在同一次拉取內，標籤會以後綴 `-N` 去重。來自訂閱的標籤保留非 ASCII 字元（例如西里爾字母）並維持可讀：Unicode 字母與數字保留在 slug 中，標點則替換為連字號——由西里爾名稱產生的標籤不再被縮減成只剩數字。

#### 自動更新如何運作

- 訂閱更新的背景任務按排程**每 5 分鐘**執行一次。
- 每次執行時，它會遍歷所有已啟用的訂閱，只更新那些自身間隔已到期的：若訂閱從未更新過，或自上次更新以來已過去不少於其 `updateInterval`，便更新它。如此一來，任務頻繁檢查訂閱，但每個具體訂閱的重新讀取頻率不會超過其 `updateInterval`（預設 10 分鐘）。UI 中以相應的提示反映此點。
- 更新流程：URL 會重新作為公開位址檢查安全性（若訂閱未設 `allowPrivate`，私有位址會被封鎖），請求透過面板的代理用戶端發出，帶標頭 `User-Agent: 3x-ui-outbound-sub/1.0`。重新導向鏈限制為 10 次跳轉，每一跳也會檢查是否為私有位址（防 SSRF）。預期 HTTP 200；否則記為錯誤。
- 成功解析後，結果會被儲存、標記最後更新時間、清除錯誤。出錯時，其錯誤文字會在 UI 中顯示為「最後錯誤」，而先前取得的 `outbound` 仍然有效。
- 只要至少有一個訂閱實際更新了，任務便會將 Xray 標記為待重啟，並送出 UI 失效通知，讓介面拉取新的 `outbound`。Xray 實際的重新載入會在管理器最近一次的 30 秒週期上發生。

手動更新單一訂閱——**「立即更新」**按鈕（`POST /outbound-subs/:id/refresh`）；它同樣會將 Xray 標記為待重啟。新增、修改、刪除訂閱也會觸發 Xray 重啟旗標（刪除時，其 `outbound` 會在下次重新載入時從設定中消失）。UI 提示：「新增或更新後，請重新啟動 Xray（或等待下一次自動重載），以使外送生效。」

#### 它如何進入 Xray 設定

每次產生 Xray 設定時，使用中的訂閱 `outbound` 會分為兩組——`prepend`（「置於手動外送之前」旗標）與其餘——並與範本縫合：`[訂閱的 prepend] + [範本的 outbound] + [其餘訂閱]`。每組內的訂閱依優先順序排列。範本中的手動 `outbound` 不受影響；若範本的 `outbound` 陣列因某種原因無法解析，訂閱的 `outbound` 便不會被混入（以免遺失手動的）。

匯入的 `outbound` 還會在 `outbound` 面板本身以獨立區塊**「來自外送訂閱（唯讀）」**顯示——無法在那裡編輯，只能透過「外送訂閱」區段管理。

### 11.13. WARP 中的 IP 輪換

在 3X-UI 中可以建立 WARP-outbound——一個到 Cloudflare WARP 的外送 WireGuard 連線（Xray 設定中的標籤 `warp`）。面板會自行在 Cloudflare 伺服器上註冊一個裝置帳戶、取得 WireGuard 金鑰與位址，並將它們填入標籤為 `warp` 的 outbound。透過這樣的 outbound，流量會以 Cloudflare WARP 的 IP 位址連出網際網路。3.3.0 版的新功能——可以手動或按排程更換這個外送 IP，而無需手動重新建立 WARP 帳戶。

管理位於 **Xray** 區段的 WARP 卡片中（在按下「建立 WARP 帳戶」並取得設定之後；在此之前這些動作不可用——面板會提示「請先取得 WARP 設定」）。

#### 更換 IP 時會發生什麼

**「更換 IP」**按鈕會啟動 IP 更換。邏輯：

1. 產生一對新的 WireGuard 金鑰。
2. 用新金鑰在 Cloudflare 伺服器上重新註冊 WARP 裝置（新的 `device_id`、`access_token`、位址與 peer 資料）。
3. 新資料被寫入 Xray 設定的 WARP-outbound：更新 `secretKey`、`address`（v4 `/32` 與 v6 `/128`）、`reserved`（取自 `client_id`），以及 peer 的 `publicKey` 與 `endpoint`。
4. 若先前設過 WARP+ 授權金鑰（長度不少於 26 字元），它會自動被重新安裝到新帳戶。失敗時這只是日誌中的一則警告——IP 更換不會被取消。
5. 成功更換後，Xray 會被標記為需重啟，以使新 outbound 生效。

成功時，介面會顯示「WARP IP 位址已成功更換！」。

#### 按排程自動輪換

WARP 卡片中有一個切換開關**「自動更新 IP 位址」**與一個欄位**「間隔（天）」**。提示：「0 — 停用。自動更換 IP 位址。」

| 參數 | 值 |
|---|---|
| 資料庫中的設定 | `warpUpdateInterval`（整數，≥ 0） |
| 預設值 | `0`（關閉自動輪換） |
| 單位 | 天 |
| `0` | 停用自動更換 |
| `> 0` | 每 N 天更換一次 IP |

寫入間隔會保存 `warpUpdateInterval`，且當值大於 0 時，會將「最後更新時間」重設為當下——否則排程器會在最近一次 tick 就更換 IP。

排程由一個每小時執行一次的背景任務執行——也就是面板每小時檢查一次是否該輪換。檢查演算法：

- 若間隔 ≤ 0——什麼都不做；
- 若「最後更新時間」等於 0（例如間隔是直接改資料庫設定的）——這是首次執行：任務只記下基準時間戳，且**不會**立即更換 IP；
- 若距上次更新已過去不少於 `間隔 × 24 × 3600` 秒——則執行同樣的 IP 更換、更新時間戳並排定 Xray 重啟。

重要細節：用「更換 IP」按鈕手動更換時，同樣會重設最後更新的時間戳。因此手動輪換後，自動間隔的計時會重新開始，計畫中的更換不會緊接著立刻觸發。

#### 「透過面板代理」

> **3.3.1 中已變更。** 獨立設定「面板網路代理」（`panelProxy`）已移除。面板自身的外送流量（包括對 WARP API 的請求）現在會透過所選的**面板流量用 outbound**——Xray-outbound 或負載平衡器（見[第 13 節](#13-面板設定)）導向。以下說明適用於 3.3.1 之前的版本。

所有對 Cloudflare WARP API 的請求（註冊、取得設定、設定授權、更換 IP）都不是直接發出，而是透過面板帶 15 秒逾時的 HTTP 用戶端。此用戶端會遵循面板設定中的**「面板網路代理」**（`panelProxy`）設定。

依設定的說明：此代理會路由面板本身的外送請求（geo 資料庫更新、Xray/面板的版本檢查、Telegram，以及現在的 WARP 存取）——以繞過伺服器端的過濾。接受形如 `socks5://` 或 `http(s)://` 的位址，例如 Xray 自身的本機 SOCKS-inbound。若欄位為空或代理設定不正確——則使用直連（行為不會中斷）。

對 WARP 的好處：若伺服器無法直接連到 `api.cloudflareclient.com`，註冊與輪換以前會失敗。如今只要在 `panelProxy` 中指定一個可用的代理（包括自己的 Xray inbound），便能保證 WARP API 的可達性，使手動按鈕與計畫輪換都正常運作。

#### 何時有用

- 為走 WARP 的 outbound 定期更換外送 IP——降低因單一位址而被封鎖與被追蹤的風險。
- 當目前的 Cloudflare 位址被列入黑名單或運作緩慢時，手動「刷新」IP。
- 對沒有直接存取 Cloudflare WARP API 的伺服器：透過 `panelProxy` 路由請求，使註冊與輪換得以運作。

---

## 12. 節點（多面板、master/slave）

**節點**區段可將普通的 3X-UI 安裝轉變為**中央（主／master）面板**，由它遠端監控並管理其他（子／child）3X-UI 面板。每個節點都是位於各自伺服器上的獨立 3X-UI 安裝；master 透過它自身的 HTTP API 與其通訊，輪詢其狀態，並將指派給它的 inbounds 與用戶端同步到它上面。這正是**多面板**能力的體現：你不必逐一登入每個面板，而是在同一份清單中看到所有伺服器並集中管理。

重要原則：**節點不是代理（agent），而是完整的 3X-UI 面板。** master 不會在它上面「安裝」任何東西——它只是憑令牌連線到它的 API。將節點從清單中移除只會停止監控；遠端面板本身不受影響（提示：「這將停止對節點的監控。遠端面板本身不會受到影響」）。

### 12.1. 清單頂部的彙總

在節點表格上方會顯示聚合計數：

| 欄位 | 說明 |
|---|---|
| 節點總數 | 清單中的節點總數。 |
| 在線 | 有多少個節點處於 `online` 狀態。 |
| 離線 | 有多少個節點處於 `offline` 狀態。 |
| 平均延遲 | 到各節點的平均延遲（ping），以毫秒計。 |

### 12.2. 新增與編輯節點

**新增節點**與**修改節點**按鈕會開啟一個包含節點欄位的表單。

**名稱**、**位址**、**連接埠**與 **API 令牌**為必填欄位（提示：「名稱、位址、連接埠與 API 令牌為必填」）。

按下「儲存」時（無論是新增還是修改），面板會**先以 6 秒逾時檢查節點是否可達**。如果節點沒有回應，記錄不會被儲存，並顯示錯誤。也就是說，無法新增一個顯然不可達的節點。

#### 表單欄位

| 欄位 | 預設值 | 允許值 | 說明 |
|---|---|---|---|
| 名稱 | —（必填） | 非空字串，**唯一** | 節點的內部名稱。名稱欄位具有唯一性約束——無法建立兩個同名的節點。佔位提示：`napr. de-frankfurt-1`。儲存時會去除首尾空白。 |
| 備註 | 空 | 任意字串 | 節點的選填註記／說明。不影響運作。 |
| 協定 | `https` | `http` / `https` | 連線到遠端面板所用的協定。若留空或填入不允許的值，正規化會設為 `https`。如果節點以普通 HTTP 回應，而協定設為 `https`，面板會回傳清楚的提示：「the server speaks HTTP, not HTTPS; set the node scheme to http」。 |
| 位址 | —（必填） | 主機名稱或 IP | 遠端面板的位址。佔位提示：`panel.example.com или 1.2.3.4`。位址會被正規化；預設禁止私有／本機位址，以防範 SSRF——詳見「允許私有位址」。 |
| 連接埠 | —（必填） | 整數 **1–65535** | 遠端節點 Web 面板的連接埠。超出範圍的值會被拒絕（「node port must be 1-65535」）。 |
| 基礎路徑 | `/` | 路徑字串 | 遠端面板的基礎路徑（web base path），若有設定的話。會被正規化：保證以 `/` 開頭與結尾（空值 → `/`）。輪詢時面板會在其後附加 `panel/api/server/status`。 |
| API 令牌 | —（必填） | 遠端面板的令牌 | 存取節點 API 用的 Bearer 令牌。透過 `Authorization: Bearer <token>` 標頭傳遞。佔位提示：「遠端面板設定頁面上的令牌」。提示：「遠端面板在 設定 → API 令牌 區段顯示其 API 令牌」。也就是說，令牌必須**在節點本身**（設定 → API 令牌）建立，再貼到此處。 |
| 已啟用 | `true` | 是／否 | 啟用對節點的監控與同步。停用的節點**不會被輪詢**（heartbeat 與 traffic-sync 會略過它們），也不參與面板的大量更新。 |
| 允許私有位址 | `false` | 是／否 | 解除 SSRF 防護，允許以私有／本機位址連線到節點。提示：「僅對私有網路或 VPN 中的節點啟用」。只有當節點確實位於私有網路中或可透過 VPN 存取時才啟用。 |

#### 在節點端取得與重新產生令牌

令牌須在遠端面板的**設定 → API 令牌**區段取得。也可在此重新發行：**重新產生令牌**按鈕，並附有警告：「重新產生會作廢目前的令牌。任何使用它的中央面板在更新前都會失去存取權。是否繼續？」。重新產生後，主面板中的舊令牌將失效——必須在節點表單中更新它。

#### 出站連線（Connection outbound）

**Connection outbound**（出站連線，`outboundTag`）欄位用來設定 master 對此節點 API 的請求流量如何離開伺服器。若在其中選擇某個 Xray-outbound 標籤，面板對節點的請求就不會直連，而是經由指定的 outbound 通過；面板會自行在工作組態中加入一個位於 loopback 的橋接 inbound，並即時套用變更，無需重啟。提示：「Route this node's panel API traffic through the selected Xray outbound. A loopback bridge inbound is added to the running config automatically and applied live. Leave empty for a direct connection」。

此選擇器的設計與面板的 outbound 選擇相同：標籤被分組為 **Outbounds**（普通出站）與 **Balancers**（負載平衡器），blackhole 出站會從清單中隱藏。空值（佔位提示「Direct connection」）= 直連到節點。

#### 匯入 inbound（選擇要同步的 inbound）

節點表單中有一個**匯入 inbound**（`inboundSyncMode`）設定，提供兩種模式：**所有 inbound**（`all`，預設）與**已選取**（`selected`）。預設情況下，master 會把所有選擇了此節點的 inbounds 同步到節點上；既有節點仍以「所有 inbound」模式運作。

在**已選取**模式下，欄位下方會出現 inbound 標籤的多重選取。按下**載入 inbound**——master 會根據輸入的（尚未儲存的）連線參數向節點請求其 inbound 清單（端點 `POST /panel/api/nodes/inbounds`）並顯示其標籤；勾選需要的標籤即可。面板將只同步並部署勾選的標籤到節點上，而節點上直接存在的其餘 inbounds 將保持不變——master 不會刪除它們，也不管理它們。

**範例：請求節點的 inbound 清單以進行選擇性匯入。** 請求主體中傳入尚未儲存的連線參數；回應中是節點上可用 inbound 的標籤：

```
POST /panel/api/nodes/inbounds
Content-Type: application/json

{ "name": "de-fra-1", "scheme": "https", "address": "node1.example.com",
  "port": 2053, "basePath": "/", "apiToken": "abcdef..." }
```

### 12.3. TLS 驗證（針對 https 節點）

這組欄位用來設定 master 如何驗證節點的 HTTPS 憑證。這些設定**僅對 `https` 協定有意義**；對於 `http` 節點則會被忽略。

**TLS 驗證**——下拉清單，提示：「面板如何驗證節點的 HTTPS 憑證。釘選或略過——用於自簽憑證（僅限 https 節點）」。

| 模式 | 值 | 預設值 | 說明 |
|---|---|---|---|
| 驗證（標準 CA） | `verify` | 是（default） | 由受信任的 CA 對憑證鏈進行常規驗證。適用於擁有公開／Let's Encrypt 憑證的節點。也用於所有 `http` 節點。 |
| 釘選憑證（SHA-256） | `pin` | — | 不驗證 CA 鏈，但會將節點葉憑證的 SHA-256 與儲存的指紋進行比對（常數時間比較）。為**自簽**憑證保留 MITM 防護。需填寫指紋欄位。 |
| 略過驗證 | `skip` | — | 完全停用憑證驗證。警告：「略過驗證會移除對「中間人」攻擊的防護——API 令牌可能被攔截。最好改用釘選憑證」。 |

在 3.4.0 中，於上述三種模式之外新增了第四種——**Mutual TLS (client certificate)**（`mtls`），與其餘模式一樣，僅在 `https` 協定下可用。

| 模式 | 值 | 預設值 | 說明 |
|---|---|---|---|
| Mutual TLS（用戶端憑證） | `mtls` | — | 除了驗證節點憑證外，master 還會以由其自身 CA 簽發的**用戶端憑證**向節點證明自己的身分。對於此模式下的節點，**API 令牌變為非必填**——節點透過憑證辨識 master。選擇此模式時會顯示提示：「This node authenticates the panel with a client certificate. Copy this panel's CA from the Node mTLS section onto the node, set its Trusted parent CA, then restart it」。 |

若要為節點啟用相互 TLS：在節點端設定 **Mutual TLS** 模式，從 **Node mTLS** 區段（見下文）複製管理面板的 CA，在節點上將其設定為**受信任的父 CA**，然後重啟節點。

若選擇 `skip`、`pin` 或 `mtls` 以外的任何值，正規化會強制設為 `verify`。

#### 憑證釘選

選擇**釘選憑證**時，會出現：

- **釘選憑證的 SHA-256**——輸入欄位。可接受 **base64** 格式的指紋（Xray 的 `pinnedPeerCertSha256` 格式）或帶或不帶冒號的 **hex**（`openssl -fingerprint` 風格）。提示：「以 base64 或 hex 表示的節點憑證 SHA-256。按「取得」即可立即從節點讀取」。佔位提示：「base64 或 hex 的 SHA-256」。選擇 `pin` 時，若指紋為空或不正確，儲存時會引發驗證錯誤。

**範例：同一個指紋的兩種格式。** 此欄位接受任一種格式——兩者都代表同一個憑證：

```
# base64 (формат pinnedPeerCertSha256 из Xray)
6O7TNg3l2k0pq8R1sT2uV3wX4yZ5a6B7c8D9e0F1g2=

# hex с двоеточиями (стиль openssl x509 -fingerprint -sha256)
E8:E2:D3:60:DE:5D:9A:4D:29:AB:CF:11:B2:7C:34:...
```

若指紋尚不可知，請按**取得**——master 會自行透過 HTTPS 從節點讀取並填入欄位。
- **取得**按鈕——以不驗證憑證的方式透過 HTTPS 連線到節點，讀取目前葉憑證的 SHA-256（端點 `POST /certFingerprint`），並填入欄位。成功後顯示「已取得節點目前的憑證」；失敗時顯示「無法取得憑證」。僅對 https 節點可用。

#### Node mTLS（面板之間的相互 TLS 驗證）

**節點**頁面上有一個獨立的 **Node mTLS** 區段——用於設定相互 TLS 驗證，為「面板 → 節點」的呼叫在 API 令牌之上增加第二個因子（用戶端憑證）。相互 TLS 為選用功能；若該區段的欄位為空，節點仍按舊有方式運作——**僅使用 API 令牌**（提示：「Mutual TLS adds a client-certificate factor on top of the API token for node-to-node calls. It is opt-in: leave it empty to keep token-only auth」）。此區段有兩項操作：

- **複製本面板的 CA**（`POST /panel/api/nodes/mtls/ca`）——將本面板的根憑證（CA）複製到剪貼簿。此 CA 需交給受管節點，使它們信任面板的用戶端憑證；之後在節點本身將 TLS 驗證模式設為 **Mutual TLS**（提示：「Hand this CA to the nodes this panel manages, then set their TLS verification to Mutual TLS」）。複製後顯示「CA certificate copied to clipboard」。
- **受信任的父 CA**（`Trusted parent CA`，`POST /panel/api/nodes/mtls/trustCA`）——當本面板自身作為某個上層（管理）面板的節點時所使用的欄位。在此貼上管理面板的 CA，以要求它提供用戶端憑證，然後按 **Save trust CA**。此變更需要**重啟面板**（提示：「When this panel is itself a node, paste the managing panel's CA here to require its client certificate. Restart the panel to apply」）。

### 12.4. 每個節點顯示哪些資訊

節點表格的欄位與節點卡片的欄位（觀測到的狀態，在每次 heartbeat 輪詢時填入）：

| 欄位 | 說明 |
|---|---|
| 狀態 | `online` / `offline` / `unknown`——見下文。 |
| CPU | 遠端伺服器的處理器負載百分比。 |
| 記憶體 | RAM 使用率百分比（以 `current/total*100` 計算）。 |
| 運行時間 | 伺服器連續運作的時間（以秒計）。 |
| 延遲 | 節點對上次輪詢的回應時間（毫秒）。 |
| 上次 ping | 上次成功 heartbeat 的時間（unix 秒；`0` =「從未」；近期的值會顯示為「剛剛」）。 |
| Xray 版本 | 節點上運行的 Xray-core 版本。 |
| 面板版本 | 節點上的 3X-UI 版本——會與目前版本比較以顯示更新指示。 |
| (inbounds) | 此節點上實際部署了多少個 inbounds。 |
| (用戶端) | 節點 inbounds 上的用戶端數量。 |
| (在線) | 節點目前有多少用戶端在線。 |
| (已耗盡) | 節點有多少用戶端**已到期或已用盡流量限額**。手動停用的用戶端不計入此計數。 |
| (速度) | 部署在節點上的 inbounds 目前（即時）的傳輸速度。 |

inbounds／用戶端／在線計數是依節點的穩定 GUID（`panelGuid`）而非本機 id 來綁定的——這樣子節點上的用戶端才會被歸算在子節點下，而非歸算在其同步所經過的中間節點下。

對於部署在節點上的 inbounds，頁面會顯示在線用戶端、各計數以及**目前的傳輸速度**。依穩定 GUID 綁定也能正確區分具有相同 `panelGuid` 的「複製」節點。

#### 節點狀態

| 狀態 | 中文 | 何時設定 |
|---|---|---|
| `online` | 在線 | 節點對 `panel/api/server/status` 輪詢回應 `success=true`。 |
| `offline` | 離線 | 節點沒有回應、回傳了 HTTP 錯誤、`success=false` 或無法識別的回應。 |
| `unknown` | 未知 | 初始值，節點尚未被輪詢過。 |

輪詢失敗時，錯誤文字會被儲存並以清楚的措辭顯示，有助於診斷「offline」的原因。

### 12.5. 對節點的操作

- **測試連線**（`POST /test`）——在節點表單中以輸入的（尚未儲存的）參數，以 6 秒逾時檢查連線。結果：「連線正常（{ms} 毫秒）」或「無法連線」。便於在儲存前對位址／連接埠／令牌／TLS 進行除錯。
- **立即檢查**（「立即檢查」按鈕，`POST /probe/:id`）——對已儲存節點進行計畫外輪詢；立即更新狀態與指標（CPU／記憶體／運行時間／延遲／版本）並記錄 heartbeat。失敗時顯示「檢查失敗」。

**範例：透過 master 的 API 測試並輪詢節點。** 「測試連線」會嘗試表單中尚未儲存的參數：

```
POST /panel/api/nodes/test
Content-Type: application/json

{ "scheme": "https", "address": "de-frankfurt-1.example.com", "port": 2053,
  "basePath": "/", "apiToken": "eyJhbGci...", "tlsMode": "verify" }
```

對 id 為 7 的已儲存節點進行計畫外輪詢：

```
POST /panel/api/nodes/probe/7
```
- **更新面板**（`POST /updatePanel`，主體為 `{ids:[…]}`）——在節點上啟動其內建的自我更新程式：節點下載最新的 3X-UI 版本並以此重啟。**更新已選取（{count}）**按鈕會一次對多個勾選的節點執行此操作。每個節點旁會顯示一個指示：**有可用更新**或**已是最新**，依節點面板版本與最新版本的比較而定。

**範例：以單一請求更新多個節點。** 主體中傳入勾選節點的 id；只有已啟用且 `online` 的節點會被更新，其餘的會以略過回傳。

```
POST /panel/api/nodes/updatePanel
Content-Type: application/json

{ "ids": [3, 7, 12] }
```

形如「已在 2 個節點上啟動更新，1 個失敗」的回應：例如節點 12 可能處於 offline 而被略過。
  - 確認：「將 {count} 個節點更新至最新版本？每個選取的節點都會下載最新版本並重啟。只有在線且已啟用的節點會被更新」。
  - **只有狀態為 `online` 且已啟用的節點會被更新。** 停用的節點在結果中標記為「node is disabled」，offline 的標記為「node is offline」。結果：「已在 {ok} 個節點上啟動更新，{failed} 個失敗」。若未選取任何符合條件的節點——顯示「請至少選取一個在線且已啟用的節點」。
- **Set Cert from Panel**（輔助功能，`GET /webCert/:id`）——在節點上建立 inbound 時，可填入節點**自身的** web-TLS 憑證路徑（而非中央面板的），使檔案確實存在於節點上。需要節點為已啟用且可達。
- **刪除節點**（`POST /del/:id`）——確認：「刪除節點「{name}」？這將停止對節點的監控。遠端面板本身不會受到影響」。會刪除節點記錄及其累積的流量統計；遠端面板照常運作。**只有在節點上所有 inbounds 都已移除後，才能刪除節點。** 若仍有至少一個 inbound 綁定到該節點（透過 `node_id`），面板會以形如「cannot delete node: N inbound(s) still attached to it; detach or delete them first」的錯誤拒絕刪除——請先解除綁定或刪除這些 inbounds，然後再刪除節點。這可避免出現帶有指向已刪除節點之懸空引用的「孤兒」inbounds。

### 12.6. 指標歷史

歷史按鈕／圖表會請求 `GET /history/:id/:metric/:bucket`。可用的指標：**`cpu`** 與 **`mem`**——它們在每次成功的 heartbeat 時累積。聚合區間的大小（`bucket`，以秒計）受白名單限制：

**範例：請求歷史。** 節點 7 的 CPU 負載圖表，以 60 秒區間聚合（最多回傳 60 個點）：

```
GET /panel/api/nodes/history/7/cpu/60
```

對於記憶體與「即時」模式（2 秒）——分別為 `…/7/mem/60` 與 `…/7/cpu/2`。白名單之外的值會被拒絕（「invalid metric」/「invalid bucket」）。

| Bucket（秒） | 用途 |
|---|---|
| 2 | 即時模式 |
| 30 | 30 秒區間 |
| 60 | 1 分鐘區間 |
| 120 | 2 分鐘區間 |
| 180 | 3 分鐘區間 |
| 300 | 5 分鐘區間 |

最多回傳 60 個點。不允許的指標或 bucket 會被拒絕（「invalid metric」/「invalid bucket」）。

### 12.7. inbounds 與用戶端如何同步

inbound 透過 `node_id` 欄位「歸屬」於某個節點（在 inbound 編輯器中選擇節點）：

**範例：節點表單中的令牌。** 令牌須在子面板（設定 → API 令牌）取得，並貼入 master 的 **API 令牌**欄位。每次輪詢時，master 會在標頭中送出它：

```
GET https://panel.example.com:2053/panel/api/server/status
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abc123...
```

如果子面板設定了**基礎路徑**（web base path），例如 `/secret/`，master 會自行在 `panel/api/server/status` 之前補上它 → `https://panel.example.com:2053/secret/panel/api/server/status`。

1. **部署組態（reconcile）。** 每當綁定到某節點的 inbound／用戶端發生任何變更時，該節點會被標記為「髒（dirty）」。背景任務會為每個已啟用且狀態為 `online` 的節點——在有變更時——將其 inbounds（依 `node_id`）部署到節點上，然後清除「髒」標誌。已停用、offline 或「髒」的節點會被視為「等待中」——對它的部署會延後到連線恢復為止。
2. **流量收集。** 同一任務會向節點請求流量快照並將其合併到本機統計中。基於合併後的流量，會執行限額／期限耗盡檢查，並在必要時停用用戶端；節點的「已耗盡」計數正反映此點。若節點不可達，其在線用戶端會被清空。

   對於同時綁定到多個面板的用戶端，master 在同一任務中還會額外向各節點下發該用戶端**橫跨所有面板的總計**流量消耗（在節點上以獨立資料表儲存，鍵為 master 的 GUID；每次下發都會覆寫，因此 master 端的重設也會傳播過去）。在節點上，該用戶端的流量會顯示兩個值中較大者——本機的或下發的——而當總配額超出時，用戶端會**在節點本身被本機停用**（透過與自動停用時相同的 Xray 重啟機制，這會中斷已建立的連線）。這消除了以往節點只看到自己那一份流量、漏算消耗、並繼續服務已用盡總限額之用戶端的情況。在重設流量、自動續期或刪除用戶端時，下發的計數會被清空。
3. **Heartbeat。** 另一個獨立的背景任務會定期透過 `panel/api/server/status` 輪詢所有**已啟用**的節點（並限制並行度），更新狀態／指標／版本，並在有 Web 用戶端時透過 WebSocket 廣播更新後的節點樹。

### 12.8. 節點鏈（子節點／遞移節點）

拓撲不一定是扁平的：一個節點本身可以是它自己各節點的 master。這類下層面板在你這裡顯示為**子節點**——它們是從直接節點取得的**「唯讀」投影**。

- 提示：「唯讀：透過 {parent} 存取的下層節點。請從 {parent} 自身的面板管理它」。也就是說，子節點無法在此編輯、刪除或更新——對它的所有操作都要從其直接父節點的面板執行。
- 子節點的身分由其 GUID 決定；正因如此，在線用戶端與 inbounds 才會被歸算在真正託管它們的實體節點下，即使在 `Node1 → Node2 → Node3` 這樣的鏈中也是如此（master 會透過每個直接節點「向內」深入一層）。
- 若直接節點變為不可達，其子節點快取會被清空，子節點會從樹中消失，直到連線恢復。

### 12.9. 節點：3.3.0 的新功能

在 3.3.0 版中，**節點**區段獲得三項明顯的改進：在多層（multi-hop）拓撲中對流量與在線用戶端的正確歸算、節點間的 client-IP 同步，以及針對「節點面板存活、但其上的 Xray 核心已掛掉」此一情況的獨立狀態指示。以下不再翻譯 inbound/outbound 等字眼。

#### 1. Multi-hop：依子節點鏈正確歸算流量

以往各計數（inbound 數量、在線用戶端、已耗盡用戶端）是在「直接」節點的層級計算的。如果你有 `Master → Node1 → Node2 → Node3` 這樣的鏈，所有實際存在於 `Node2`／`Node3` 上的東西，都會被錯誤地歸到它經由而到達 master 的 `Node1`。在 3.3.0 中，歸算改為依真實來源進行。

其運作方式如下：

- **子節點以獨立的列顯示出來。** 每個面板都會發布其直接節點的清單；只有具備已知 `Guid` 的節點才會被納入——需要穩定的身分才能將節點向上歸算一個「跳」。master 會定期（從 heartbeat 任務中）拉取這些清單並快取，然後在直接節點之外加入「遞移」子節點。
- **遞移節點為唯讀。** 在 UI 中它們會被標記為 **「子節點」**，並附提示：*「唯讀：透過 {父節點} 存取的下層節點。請從 {父節點} 自身的面板管理它。」* 這樣的列沒有管理按鈕——該節點要從其直接父節點的面板管理。
- **透過 GUID 建立階層。** 對於直接節點，`ParentGuid` 即 master 本身的 GUID；對於遞移節點，則是其父節點的 GUID。樹狀結構就是這樣建立的。
- **計數的真實來源是 inbound 上的 `origin_node_guid`。** 這是實際持有此 inbound 之節點的 `panelGuid`。它會在 inbound 自節點同步時被設定，並**在後續各跳中按原樣保留**，因此深層巢狀的 inbound 會被歸到真實節點，而非中間節點。inbounds 數量、在線用戶端與已耗盡用戶端的計數即依此 GUID 重新計算。鍵的選擇邏輯：

  | inbound 狀態 | 歸算對象 |
  |---|---|
  | 已設定 `origin_node_guid` | 該 GUID（真實的來源節點） |
  | 為空，但已設定 `node_id` | 節點的合成 GUID（舊版本，尚未回報其 `panelGuid`） |
  | 為空且 `node_id` 也為空 | master 自身的 GUID（本機 Xray 上的 inbound） |

  在線用戶端同樣依 GUID 分組，因此每個節點列只顯示真正連線到它的那些用戶端。

**使用者所見：** 在扁平拓撲中（節點直接位於 master 之下），一切照舊——依 GUID 與依 `id` 的計數一致。但一旦出現節點鏈，清單中就會出現「子節點」列，而每個節點的 inbound／在線／已耗盡數量現在反映的正是它自己的負載，而非所有經由它遞移通過之物的總和。

#### 2. 節點間從 access.log 同步 client-IP

IP 限制（用戶端的 `limitIp`）依賴於 Xray 寫入其 access.log 的位址。以往每個節點只看到對自己的連線，因此「每個用戶端不超過 N 個 IP」的限制在叢集中無法運作：用戶端可以連到不同的節點以繞過限制。在 3.3.0 中，觀測到的 IP 會在整個叢集中同步。

其運作方式如下：

- 在每個節點上，背景任務會解析 access.log，從每一行取出 IP、用戶端 email 與時間戳，並存入本機資料表（每個 email 一筆記錄，IP 以 JSON 陣列 `{ip, timestamp}` 儲存）。本機位址 `127.0.0.1` 與 `::1` 會被捨棄。
- 同步**每 10 秒一次**，對每個在線且已啟用的節點執行雙向交換：從節點拉取 IP 並合併到本機資料表，然後將 master 的彙總視圖回傳給節點。
- 合併會把舊的與傳入的觀測整併在一起，**不會重複計算**在多個節點上看到的同一個 IP，也**不會復活過期的**記錄：套用與本機任務相同的時效閾值——**30 分鐘**。對每個 IP 保留最新的時間戳。來自其他節點的記錄會取得新的本機 id（各節點的 id 空間獨立）；同一 email 的並行插入有防重複保護。
- 在計算限制時，「存活」的 IP 是指：要麼在目前的本機掃描中被觀測到，要麼在同步資料庫中具有非常新的時間戳（**2 分鐘以內**）。正是這一點讓限制能在整個叢集的規模上運作，即使該位址是在另一個節點上被觀測到的。當超出限制時，最舊的「存活」IP 會被送入 fail2ban 日誌，連線會被強制中斷（透過 Xray API 移除／重新加入用戶端）。

**使用者所見：** IP 數量限制現在作用於整個叢集，而非各個節點各自為政；在面板中，每個用戶端會顯示在任一節點上觀測到的 IP（在 30 分鐘的時間窗內）。此功能沒有單獨的按鈕／設定——同步會在背景自動進行，前提是節點啟用了且可存取 access.log（限制本身還需要節點上有 Fail2Ban）。

#### 3. 獨立的狀態指示：節點面板在線，但 Xray 已掛掉

以往節點狀態本質上是「在線／離線」二元的。只要節點面板有回應，節點就算在線——即便其上的 Xray 核心並未運作、用戶端實際上無法連線。在 3.3.0 中，面板的健康狀態與 Xray 核心的健康狀態被區分開來。

其運作方式如下：

- 輪詢節點時，master 會從遠端 `/panel/api/server/status` 的回應中取出 `xray.state` 與 `xray.errorMsg` 欄位並儲存到節點中。即便面板 ping 成功而核心不健康時，這些欄位也會被填入——正是為了區分面板的可達性與 Xray 的狀態。
- `xray.state` 的值：`"running"`（運作中）、`"stop"`（已停止）、`"error"`（錯誤）。
- 這些值會轉譯為節點狀態。在原有狀態之外新增了：

  | 狀態鍵 | 中文標籤 | 何時顯示 |
  |---|---|---|
  | `online` | 「在線」 | 面板有回應，Xray 運作中（`running`） |
  | `offline` | 「離線」 | 面板不可達／ping 未通過 |
  | `unknown` | 「未知」 | 狀態尚未確定 |
  | `xrayError` | 「Xray 錯誤」 | 面板在線，但 Xray 核心處於 `error` 狀態（有 `errorMsg`） |
  | `xrayStopped` | 「已停止」 | 面板在線，但 Xray 已停止（`stop`） |

- 對於這類狀態，UI 中使用**獨立的紫色指示**（一種有別於綠色「在線」與紅色「離線」的顏色）。紫色直接表明：節點是聯絡得上的，問題出在 Xray 核心本身，而非網路或面板本身。

**使用者所見：** 與其在核心掛掉時誤導性地顯示「綠色」，節點會以**紫色**高亮並顯示狀態**「Xray 錯誤」**或**「已停止」**。這立刻顯示出需要修復的是節點上的 Xray（重啟核心、查看 `errorMsg`），而非去排查節點本身的可達性。同樣的 `xrayState`／`xrayError` 也會傳遞到遞移子節點（見第 1 點），因此核心的異常狀態在整條鏈上都看得到。

---

## 13. 面板設定

「設定」區段（頁面標題為 **設定**，英文 *Panel Settings*）管理 3X-UI 網頁面板本身的行為：它在哪個位址與連接埠上監聽、如何受到保護、如何與 Telegram 機器人及外部服務互動、以哪個時區執行排程任務。每個參數都以「鍵—值」配對的形式儲存在資料庫的 `settings` 表中；若資料庫中沒有相應的值，則套用預設值。

> **重要——套用變更。** 此頁面上的任何變更都需要用 **儲存**（*Save*）按鈕儲存，然後重新啟動面板，變更才會生效。原文提示為：「儲存變更並重新啟動面板以套用變更。」儲存時會顯示「設定已變更」的通知。

### 13.1. 儲存與重新啟動面板

| 元素 | 用途 |
| --- | --- |
| **儲存**（*Save*） | 將表單中所有欄位寫入資料庫（`POST /panel/setting/update`）。寫入前，值會經過驗證——不正確的位址、連接埠或路徑將被拒絕，面板會回傳錯誤。 |
| **重新啟動面板**（*Restart Panel*） | 重新啟動面板的網頁伺服器（`POST /panel/setting/restartPanel`）。重新啟動會延遲 3 秒進行。提示：「您確定要重新啟動面板嗎？確認後，將在 3 秒後重新啟動。若面板無法存取，請檢查伺服器日誌」。成功時——「面板已成功重新啟動」。 |
| **重設為預設設定**（*Reset to Default*） | 刪除資料庫中所有已儲存的設定，之後面板將使用預設值。此操作不會重設管理員的登入憑證。 |

重新啟動是透過向面板處理程序傳送 `SIGHUP` 訊號（或透過已註冊的重啟掛鉤）來執行。在 Windows 上不支援透過訊號自動重新啟動。**監聽參數（IP、連接埠、路徑、網域、憑證、時區）的變更只有在重新啟動面板後才會套用。**

### 13.2. 一般設定（「面板」分頁 / *General*）

#### 介面語言（*Language*）

面板網頁介面的語言。可用語言：`en-US`（英語）、`ru-RU`（俄語）、`zh-CN`、`zh-TW`、`fa-IR`、`ar-EG`、`es-ES`、`id-ID`、`ja-JP`、`pt-BR`、`tr-TR`、`uk-UA`、`vi-VN`。這是顯示設定，不影響 Xray 的運作。

#### 日曆類型（*Calendar Type*）

- **鍵：** `datepicker`
- **預設值：** `gregorian`（公曆）。
- **用途：** 在選擇日期時所使用的日曆類型（例如，設定客戶的有效期限時）。提示：「排程任務將依照此日曆執行。」替代值為波斯（賈拉里）曆，這在面板的伊朗使用族群中很有需求。

#### 分頁大小（*Pagination Size*）

- **鍵：** `pageSize`
- **預設值：** `25`
- **允許值：** 從 `0` 到 `1000` 的整數。
- **用途：** 表格（連線/inbound 清單）中每頁的列數。提示：「設定連線表格的分頁大小。設為 0 以停用」——當為 `0` 時，分頁輸出會被停用，所有記錄會顯示為單一清單。
- **無需重新啟動面板**（顯示設定）。

#### 自動停用後重新啟動 Xray（*Restart Xray After Auto Disable*）

- **鍵：** `restartXrayOnClientDisable`
- **預設值：** `true`
- **用途：** 當客戶被自動停用（因有效期限到期或達到流量上限）時，重新啟動 Xray，以中斷該客戶已建立的連線。提示：「當客戶因有效期限到期或流量上限而自動停用時，重新啟動 Xray。」功能本身未變更——此切換開關只是放在「面板」分頁（*General*）上，與其他一般設定並列。

#### 備註模型與分隔字元（*Remark Model & Separation Character*）

- **鍵：** `remarkModel`
- **預設值：** `-ieo`
- **用途：** 設定訂閱中組態名稱（remark）的產生方式。該字串由**第一個字元**——分隔符，以及後續的**順序字母序列**組成：
  - `i` — inbound 備註（*inbound remark*）；
  - `e` — 客戶的 email；
  - `o` — 額外標籤（*extra*）。
  
  在預設值 `-ieo` 下，分隔符為 `-`，而各部分的順序為：inbound → email → extra（例如 `MyInbound-user@mail-extra`）。空白部分會被略過。介面中的「備註範例」（*Sample Remark*）欄位會顯示所產生名稱的預覽。是否將 email 納入名稱，還取決於訂閱設定中的「在名稱中包含 Email」參數（訂閱相關區段）。

**範例：`remarkModel` 的值如何影響組態名稱。** 假設 inbound 名為 `VLESS-Reality`，客戶的 email 為 `alex@vpn`，而額外標籤為 `RU`。則：

| 欄位值 | 最終名稱（remark） |
| --- | --- |
| `-ieo`（預設） | `VLESS-Reality-alex@vpn-RU` |
| `_ie` | `VLESS-Reality_alex@vpn` |
| `-ei` | `alex@vpn-VLESS-Reality` |
| ` o`（空格分隔符，僅標籤） | `RU` |

字串的第一個字元——始終是分隔符；其餘字母決定哪些部分以何種順序納入名稱。

### 13.3. 面板存取：IP、連接埠、路徑、網域、憑證

這組設定定義了面板的網路進入點。**此處所有變更只有在重新啟動面板後才會套用。**

| 欄位 | 鍵 | 預設值 | 說明 |
| --- | --- | --- | --- |
| 面板管理用 IP 位址（*Listen IP*） | `webListen` | `""`（空） | 網頁面板監聽的 IP。空 = 在所有 IP 上監聽。提示：「留空以允許從任何 IP 連線」。若已設定，必須是有效的 IP 位址（否則儲存會被拒絕）。 |
| 面板網域（*Listen Domain*） | `webDomain` | `""`（空） | 用於依網域檢查請求的面板網域名稱。空 = 接受來自任何網域和 IP 的連線。提示：「留空以允許從任何網域和 IP 連線。」 |
| 面板連接埠（*Listen Port*） | `webPort` | `2053` | 面板運作所在的連接埠。提示：「面板運作所在的連接埠」。允許 `1–65535`。連接埠必須是空閒的；面板與訂閱服務不能同時使用相同的 `IP:連接埠` 配對。 |
| URI 路徑（*URI Path*） | `webBasePath` | `/` | 面板 URL 的基本路徑（basePath）。提示：「必須以 '/' 開頭並以 '/' 結尾」。儲存時，若缺少前導和結尾的 `/`，面板會自動加上。路徑中的禁用字元會被拒絕。 |

##### 面板憑證（TLS / HTTPS）

| 欄位 | 鍵 | 預設值 | 說明 |
| --- | --- | --- | --- |
| 面板憑證公鑰檔案路徑（*Public Key Path*） | `webCertFile` | `""` | 憑證（憑證鏈）檔案的完整路徑。提示：「輸入以 '/' 開頭的完整路徑」。 |
| 面板憑證私鑰檔案路徑（*Private Key Path*） | `webKeyFile` | `""` | 私鑰檔案的完整路徑。提示：「輸入以 '/' 開頭的完整路徑」。 |

若設定了憑證/金鑰路徑中的**至少一個**，面板在儲存時會嘗試載入「憑證 + 金鑰」配對；若發生錯誤（檔案不存在、金鑰與憑證不符），儲存會被拒絕。當兩個正確的路徑都已設定時，面板會切換為 HTTPS。兩個欄位都為空 = 面板以一般 HTTP 運作。

> **安全警告**（*Security warnings*）。若偵測到不安全的組態，面板會顯示「您的面板可能對外開放：」的區塊並附上警告：
> - 以一般 HTTP 運作——「正式環境請設定 TLS」；
> - 標準連接埠 2053——「將其改為隨機值」；
> - 預設基本路徑 `/`——「將其改為隨機值」；
> - 標準訂閱路徑 `/sub/` 與 JSON 訂閱 `/json/`——「將其變更」。
> 這些是建議，而非封鎖。

### 13.4. 工作階段、面板代理與受信任代理（「代理與伺服器」分頁 / *Proxy and Server*）

#### 工作階段持續時間（*Session Duration*）

- **鍵：** `sessionMaxAge`
- **預設值：** `360`（分鐘，即 6 小時）。
- **允許值：** 從 `1` 到 `525600` 分鐘（1 年）。
- **用途：** 管理員在不重新登入的情況下保持已授權的時間。單位為**分鐘**。提示：「系統中的工作階段持續時間（值：分鐘）」。

#### 面板流量的 outbound（*Panel Traffic Outbound*）

- **鍵：** `panelOutbound`
- **預設值：** `""`（空 = 直接連線）。
- **用途：** 設定一個 Xray **outbound**，面板透過它傳送**自身的請求**——版本檢查與面板/Xray 的下載、對 Telegram 的連線、一般的 geo 檔案更新——以繞過伺服器端對 GitHub/Telegram 的過濾。此欄位為**下拉清單**：其中列出了來自 Xray 組態範本的 outbound、來自 outbound 訂閱的 outbound，以及路由**負載平衡器**（單獨一組）。清單中已排除 `blackhole` 類型的 outbound——將下載路由到「黑洞」毫無意義。原文提示：「將面板自身的請求——版本檢查與面板/Xray 的下載、Telegram 以及一般的 geo 檔案更新——透過此 Xray outbound 路由，以繞過伺服器端對 GitHub/Telegram 的過濾。本機橋接 inbound 會自動加入運作中的組態並即時套用。Xray 內建的 Geodata 自動更新不受影響；它有自己的下載 outbound。留空以直接連線。」

> **運作方式。** 選擇某個 outbound 時，面板會自行在運作中的組態裡加入一個服務用的 loopback-inbound（標籤為 `panel-egress` 的 SOCKS 橋接）以及一條路由規則，將面板自身的 HTTP 流量導向所選的 outbound。若選擇了負載平衡器，規則中會代入 `balancerTag`，面板流量會在其成員之間分配。橋接與規則會**即時**套用，無需完整重新啟動面板。留空此欄位以直接連線。Xray 內建的 geo 資料自動更新**不受**此設定影響——它在 Xray 路由內部有自己的 outbound。
- **格式：** `socks5://`（或 `socks5h://`）或 `http(s)://`，必要時可附帶 `socks5://user:pass@host:port` 形式的授權。嚴格支援的協定為：`socks5`、`socks5h`、`http`、`https`——其他協定視為不允許，此時面板會回退至直接連線。典型範例是 Xray 自身的本機 SOCKS inbound。
- 原文提示：「將面板自身的 outbound 請求（geo 更新、Xray/面板版本檢查、Telegram）透過此代理路由，以繞過伺服器端對 GitHub/Telegram 的過濾。接受 socks5:// 或 http(s)://，例如 Xray 本機 SOCKS inbound。留空以直接連線。」
- 無效的代理不會導致儲存錯誤——面板只是改用直接連線，並在日誌中寫入警告。

**欄位值範例。** 若伺服器上已啟動了一個位於連接埠 `10808` 的本機 Xray SOCKS inbound，請將面板自身的請求透過它導向：

```
socks5://127.0.0.1:10808
```

對於帶授權的外部 HTTP 代理：

```
http://user:pass@proxy.example.com:8080
```

儲存並重新啟動後，面板將透過所指定的代理來拉取 geo 資料庫更新、檢查版本並連線 Telegram。

#### 受信任的代理 CIDR（*Trusted proxy CIDRs*）

- **鍵：** `trustedProxyCIDRs`
- **預設值：** `127.0.0.1/32,::1/128`（僅本機主機）。
- **格式：** 以逗號分隔的 IP 位址或 CIDR 子網路清單（例如 `10.0.0.0/8, 192.168.1.5`）。每個項目都會驗證為 IP 或 CIDR——不正確的值會在儲存時被拒絕。
- **用途：** 列出允許設定 `X-Forwarded-Host`、`X-Forwarded-Proto` 標頭以及真實客戶端 IP 標頭的來源。原文提示：「以逗號分隔的 IP/CIDR，允許其設定 forwarded host、proto 與 client IP 標頭。」若面板運作在反向代理（nginx、Caddy 等）之後，需要進行設定，以便正確判定客戶端 IP 與協定。

**範例：面板位於反向代理之後。** 若 nginx 位於同一主機並將請求代理至面板，請僅信任本機主機（預設值）：

```
127.0.0.1/32,::1/128
```

若代理位於內部網路 `10.0.0.0/8` 中的另一台獨立伺服器上，請加入其子網路，否則面板會忽略它所傳遞的標頭，並會看到代理的 IP 而非真實客戶端的 IP：

```
127.0.0.1/32,::1/128,10.0.0.0/8
```

傳遞真實 IP 與協定的對應 nginx 區塊範例：

```nginx
proxy_set_header X-Real-IP        $remote_addr;
proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
```

### 13.5. Telegram 機器人（「Telegram 機器人」分頁 / *Telegram Bot*）

#### 啟用 Telegram 機器人（*Enable Telegram Bot*）

- **鍵：** `tgBotEnable`
- **類型/預設：** 布林值，`false`。
- **用途：** 啟用 Telegram 機器人的運作。提示：「透過 Telegram 機器人存取面板功能」。

#### Telegram 權杖（*Telegram Token*）

- **鍵：** `tgBotToken`
- **預設：** `""`。
- **用途：** 機器人的權杖。提示：「需向 Telegram 機器人管理員 @botfather 取得權杖」。
- **安全特性：** 權杖屬於機密值。在面板讀取設定的回應中不會回傳此值（欄位會被清空，僅回傳「已設定／未設定」的旗標）。若儲存時將此欄位留空，則先前儲存的權杖會**被保留**（不被覆寫）。

#### Telegram 機器人語言（*Telegram Bot Language*）

- **鍵：** `tgLang`
- **預設：** `en-US`。
- **用途：** 機器人訊息的語言（與網頁介面語言無關）。可用語言清單與面板語言相同。

#### 機器人管理員的 User ID（*Admin Chat ID*）

- **鍵：** `tgBotChatId`
- **預設：** `""`。
- **格式：** 一個或多個數字型 Telegram User ID，**以逗號分隔**。
- **用途：** 通知的接收者，以及獲准透過機器人管理面板的管理員。提示：「一個或多個 Telegram 機器人管理員的 User ID。要取得 User ID，請使用 @userinfobot 或在機器人中使用 '/id' 指令。」

#### 通知頻率（*Notification Time*）

- **鍵：** `tgRunTime`
- **預設：** `@daily`（每天一次）。
- **格式：** **Crontab** 格式的字串（支援標準 cron 運算式，也支援 `@daily`、`@hourly`、`@every 1h` 之類的簡寫）。提示：「以 Crontab 格式指定通知間隔」。控制機器人的週期性報告。

**欄位值範例。**

| 值 | 機器人何時傳送報告 |
| --- | --- |
| `@daily` | 每天午夜一次（預設） |
| `@hourly` | 每小時 |
| `@every 6h` | 每 6 小時 |
| `0 9 * * *` | 每天 09:00 |
| `30 8 * * 1` | 每週一 08:30 |

時間以「時區」設定（第 13.6 節）中的時區計算。

#### SOCKS 代理（*SOCKS Proxy*）

- **鍵：** `tgBotProxy`
- **預設：** `""`。
- **用途：** 專供機器人連線 Telegram 使用的 SOCKS5 代理。提示：「若您需要代理 Socks5 才能連線 Telegram，請依指南設定其參數。」此設定恰好套用於機器人的流量（與第 13.4 節的一般「面板網路代理」不同）。

#### Telegram API Server（*Telegram API Server*）

- **鍵：** `tgBotAPIServer`
- **預設：** `""`（使用標準伺服器 `api.telegram.org`）。
- **格式：** URL `http(s)://…`；儲存時會通過 URL 正確性檢查——無效位址會被拒絕。提示：「所使用的 Telegram API 伺服器。留空以使用預設伺服器。」用於自行部署的 Telegram Bot API server。

#### 機器人通知（「通知」群組 / *Notifications*）

| 欄位 | 鍵 | 預設 | 說明 |
| --- | --- | --- | --- |
| 資料庫備份（*Database Backup*） | `tgBotBackup` | `false` | 將資料庫備份檔案連同報告一起傳送至 Telegram。提示：「傳送帶有資料庫備份檔案的通知」。 |
| 登入通知（*Login Notification*） | `tgBotLoginNotify` | `true` | 嘗試登入面板時發出通知。提示：「顯示有人嘗試登入您的面板時的使用者名稱、IP 位址與時間。」 |
| 工作階段到期通知延遲（*Expiration Date Notification*） | `expireDiff` | `0` | 在客戶有效期限到期前幾**天**傳送通知。`0` — 停用。允許 `>= 0`。提示：「在達到閾值前接收工作階段有效期限到期的通知（值：天）」。 |
| 通知用流量閾值（*Traffic Cap Notification*） | `trafficDiff` | `0` | 通知用的剩餘流量閾值。提示：「在達到閾值前接收流量耗盡的通知（值：GB）」。允許 `0–100`。 |
| CPU 負載閾值（*CPU Load Notification*） | `tgCpu` | `80` | 若 CPU 負載超過閾值（以**%**計），通知管理員。允許 `0–100`。提示：「若 CPU 負載超過此閾值，在 Telegram 中通知管理員（值：%）」。 |

### 13.6. 日期與時間（「日期與時間」分頁 / *Date and Time*）

#### 時區（*Time Zone*）

- **鍵：** `timeLocation`
- **預設值：** `Local`（伺服器的系統時區）。
- **格式：** IANA tz 資料庫中的時區名稱（例如 `Europe/Moscow`、`UTC`、`Asia/Tehran`）。
- **用途：** 面板執行排程任務（機器人報告、流量重設/檢查、期限到期）所依據的時區。提示：「排程任務依照此時區的時間執行」。
- **驗證：** 儲存時會檢查時區——不存在的時區會被拒絕。若之後資料庫中出現不正確的值，面板在執行階段會回退至 `Local`，若連 `Local` 也不可用——則回退至 `UTC`。

### 13.7. 外部流量與 Xray 行為（「外部流量」分頁 / *External Traffic*）

| 欄位 | 鍵 | 預設 | 說明 |
| --- | --- | --- | --- |
| 外部流量通知（*External Traffic Inform*） | `externalTrafficInformEnable` | `false` | 每次流量更新時通知外部 API。提示：「每次流量更新時通知外部 API。」 |
| 外部流量通知 URI（*External Traffic Inform URI*） | `externalTrafficInformURI` | `""` | 面板傳送流量更新的目標 URL。儲存時會通過 URL 正確性檢查。提示：「流量更新會傳送至此 URI」。 |
| 自動停用後重新啟動 Xray（*Restart Xray After Auto Disable*） | `restartXrayOnClientDisable` | `true` | 當客戶因有效期限到期或超過流量上限而自動停用時，重新啟動 Xray。提示：「當客戶因有效期限到期或流量上限而自動停用時，重新啟動 Xray。」**此切換開關位於「面板」分頁（*General*）**——見第 13.2 節；此處為求完整而列出。 |

### 13.8. 其他：Xray 組態範本與檢查 URL

#### Xray 組態範本（*xrayTemplateConfig*）

- **鍵：** `xrayTemplateConfig`
- **預設：** 內建（embedded）的 JSON 範本，隨建置一起提供。
- **用途：** Xray-core 組態的基底 JSON 範本，面板會在其之上構建 inbound/outbound。此值在一般取得所有設定的輸出中**不會回傳**，而是在獨立的 Xray 組態頁面上編輯，而非在面板設定的一般欄位清單中。預設的標準範本可透過 `GET /panel/setting/getDefaultJsonConfig` 取得。

#### outbound 檢查 URL（*xrayOutboundTestUrl*）

- **鍵：** `xrayOutboundTestUrl`
- **預設：** `https://www.google.com/generate_204`
- **用途：** 在檢查 outbound 連線可用性時所使用的 URL。設定時會作為 HTTP(S) URL 進行清理。

### 13.9. 管理員帳號與 API 權杖

這些參數位於相鄰的分頁（「帳號」 / *Authentication*）上，並在安全相關區段中有詳細說明；此處為各鍵的簡要彙總。

- **變更登入憑證**（「目前登入名稱」、「目前密碼」、「新登入名稱」、「新密碼」欄位）以單獨的請求 `POST /panel/setting/updateUser` 儲存。需要正確的目前登入名稱與密碼；新的登入名稱與密碼不得為空。訊息：「您已成功變更管理員的登入憑證。」 /「使用者名稱或密碼不正確」。
- **雙因素驗證（2FA）**——鍵 `twoFactorEnable`（預設 `false`）與機密的 `twoFactorToken`。權杖為機密：在已啟用 2FA 的情況下，儲存時的空欄位不會覆寫既有的權杖。在**首次**啟用 2FA 時，面板會使目前的工作階段失效（提升「登入紀元」）。
- **API 權杖** 由獨立的端點（`/panel/setting/apiTokens…`）管理：列出、建立（`apiTokens/create`）、刪除、啟用/停用。權杖本身**僅在建立時顯示一次**，且不會以可讀形式儲存：「請立即複製此權杖。基於安全考量，它不會以可讀形式儲存，且不會再次顯示。」

有關 2FA、密碼、LDAP 同步以及訂閱格式（JSON/Clash、fragmentation、noises、mux）的詳情，請參見手冊中相應的獨立區段。

### 13.10. 3.3.0 中的 API 變更（對整合很重要）

在 3.3.0 版本中，伺服器 API 的路徑結構發生了變更。若您有透過 HTTP 連線面板的外部整合（指令碼、機器人、中央面板、CI 任務），**需要對其進行修改**，否則它們將停止運作。

#### ⚠️ BREAKING CHANGE：`/panel/setting/*` 與 `/panel/xray/*` 端點已移至 `/panel/api` 之下

以前，面板設定管理與 Xray 組態各自獨立存放，位於 `/panel/setting/*` 與 `/panel/xray/*` 路徑下。現在兩組都已註冊在共用的 API 群組 `/panel/api` 內。舊路徑已**完全移除**——對其的請求將回傳 404。

為何如此做：整個 `/panel/api` 群組都會經過統一的存取檢查，也就是說這些端點現在接受與其餘 API 相同的 `Authorization: Bearer <token>` 標頭。API 權杖即為完整的管理員存取權限，如此一來整個 API 介面便變得一致。

**未變更的部分：** 網頁介面頁面（SPA 路由）`/panel/settings` 與 `/panel/xray` 維持原位——這只涉及伺服器 API 端點。

#### 路徑對應表（舊 → 新）

下方所有路徑的前綴變更——只是在 `/panel/` 之後加上了 `api/`。

| 原本（≤ 3.2.x） | 變更後（3.3.0） | 方法 |
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
| `/panel/xray/outbound-subs`（與 `/outbound-subs/*`） | `/panel/api/xray/outbound-subs`（與 `/outbound-subs/*`） | GET/POST/DELETE |

子路徑的名稱、請求主體與回應格式本身並未變更——只變更了**前綴**。

#### 如何修復既有的整合

1. 在您的指令碼/組態中找出所有 `/panel/setting/` 與 `/panel/xray/` 的出現之處。
2. 替換前綴：在 `/panel/` 之後立即加上 `api/`（例如 `/panel/setting/all` → `/panel/api/setting/all`）。
3. 請求主體、參數與回應格式無需修改——只變更 URL。
4. 由於設定與 Xray 組態現在位於 `/panel/api` 之下，可以（也應該）使用與 `/panel/api/inbounds/*` 等其他端點相同的 API 權杖 `Authorization: Bearer <token>` 來連線。別忘了套用在整個 `/panel/api` 群組上的 CSRF middleware。

**範例：透過 API 讀取所有設定。** 以前（≤ 3.2.x）：

```bash
curl -sk -X POST "https://panel.example.com:2053/MyPath/panel/setting/all" \
  -H "Authorization: Bearer <token>"
```

現在（3.3.0）——在 `/panel/` 之後加上了 `api/`：

```bash
curl -sk -X POST "https://panel.example.com:2053/MyPath/panel/api/setting/all" \
  -H "Authorization: Bearer <token>"
```

重新啟動面板同理：`POST /panel/api/setting/restartPanel`。舊路徑 `/panel/setting/restartPanel` 現在會回傳 404。

#### 具型別的 API：結構描述與文件（Swagger / OpenAPI）

在 3.3.0 中，OpenAPI 規格已完整具備型別。以前，具型別的回應以空物件 `{}` 描述；現在元件與結構描述（`components.schemas`）直接從資料模型產生。因此：

- Swagger UI 顯示真實的資料模型，而非空泛的佔位符。
- 外部產生器（`openapi-generator` 等）可依規格建構出所需語言的現成客戶端。
- 每個具型別的回應都附有指向具體模型的 `$ref`，並附上回應範例。

何處查看 API 文件：

- **內建的 Swagger 頁面。** 面板選單中有 **「API 文件」** 項目（SPA 路由 `/panel/api-docs`）。此處互動式地列出所有端點及其說明、請求主體與回應範例。
- **原始的 OpenAPI 3.0 規格** 由 `/panel/api/openapi.json` 位址提供。此 URL 可直接餵給 Postman、Insomnia 或 `openapi-generator`。規格在建置階段內嵌於二進位檔中；當面板在非標準的 `webBasePath` 下運作時，規格中的 `servers` 欄位會自動改寫為目前的基本路徑，以便「Try it out」按鈕與外部產生器命中正確的前綴。

---

## 14. Telegram 機器人

3X-UI 面板內建了一個 Telegram 機器人，透過它可以接收伺服器與用戶端狀態的通知，並且可以直接在通訊軟體中管理個別用戶端。機器人採用 long polling 技術（持續輪詢 Telegram）運作，因此不需要外部網域或開放連接埠 —— 只要能對外存取 Telegram 伺服器即可。

機器人區分兩種對話對象：

- **管理員** —— Telegram User ID 已填入機器人設定（「機器人管理員 User ID」欄位）的使用者。可存取所有功能：伺服器統計、備份、用戶端管理、重啟 Xray。
- **用戶端** —— 任何其他使用者，其 Telegram User ID 已綁定到某個 inbound 連線的具體用戶端（用戶端的 `tgId` 欄位）。僅能看到自己訂閱的相關資訊。

**範例：將用戶端綁定到 Telegram。** 為了讓使用者收到自己訂閱的統計，將其數字型 Telegram User ID 寫入用戶端的 `tgId` 欄位。在用戶端的 JSON 設定中看起來像這樣：

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

之後，User ID 為 `123456789` 的使用者就能向機器人發送 `/usage ivan` 並看到自己的統計。同樣的 ID，管理員也可以透過用戶端卡片中的「👤 設定 Telegram 使用者」按鈕來填入 —— 不一定要手動編輯 JSON。

### 14.1. 啟用與設定機器人

機器人的所有參數都在面板的 **設定 → Telegram-бот** 區段中設定。修改設定後需要儲存並重啟面板 —— 機器人會在 Web 伺服器啟動時初始化。

| 欄位 (UI) | 設定鍵 | 預設值 | 說明 |
|---|---|---|---|
| Включить Telegram бота | `tgBotEnable` | `false` | 主開關。提示：「透過 Telegram 機器人存取面板功能」。停用期間機器人不會啟動，通知任務也不會排程。 |
| Telegram-токен | `tgBotToken` | （空） | 機器人 Token。提示：「需要向 Telegram 機器人管理員 @botfather 取得 Token」。Token 為空時機器人不會啟動。 |
| SOCKS-прокси | `tgBotProxy` | （空） | 連線到 Telegram 用的代理。提示 (RU)：「如果連線到 Telegram 需要 Socks5 代理，請依照指南設定其參數」。 |
| Telegram API Server | `tgBotAPIServer` | （空） | 替代的 Telegram API 伺服器。提示：「使用的 Telegram API 伺服器。留空則使用預設伺服器」。 |
| User ID администратора бота | `tgBotChatId` | （空） | 一個或多個管理員的 Telegram User ID，以逗號分隔。提示：「要取得 User ID，請使用 @userinfobot 或在機器人中使用 `/id` 指令」。 |
| Частота уведомлений для администраторов от бота | `tgRunTime` | `@daily` | 週期性報告的排程，採用 crontab 格式。提示：「以 Crontab 格式指定通知間隔」。 |
| Резервное копирование базы данных | `tgBotBackup` | `false` | 提示：「發送含資料庫備份檔的通知」。會將備份附加到週期性報告中。 |
| Уведомление о входе | `tgBotLoginNotify` | `true` | 提示：「當有人嘗試登入您的面板時，顯示使用者名稱、IP 位址與時間」。 |
| Порог нагрузки на ЦП для уведомления | `tgCpu` | `80` | CPU 負載門檻（百分比，驗證範圍 0–100）。提示：「當 CPU 負載超過此門檻時通知 Telegram 管理員（數值：%）」。數值為 0 時停用 CPU 檢查。 |
| Язык Telegram-бота | — | — | 機器人產生所有訊息時所使用的語言。 |

#### 透過 @BotFather 取得 Token

1. 在 Telegram 中開啟與 **@BotFather** 的對話。
2. 發送 `/newbot` 指令並依照指示操作（機器人名稱與唯一的、以 `bot` 結尾的 `username`）。
3. BotFather 會給出形如 `123456789:AA...` 的 Token。將它複製到 **Telegram-токен** 欄位。

#### 取得管理員 User ID

User ID 是帳號的數字型識別碼（不是 username）。可以用兩種方式查得：

- 向 **@userinfobot** 發送訊息。
- 啟動已設定好的機器人並向它發送 **`/id`** 指令 —— 它會回傳您的 ID。

將取得的數字填入 **User ID администратора бота** 欄位。要指派多個管理員，將他們的 ID 以逗號分隔列出（例如 `11111111,22222222`）。每個 ID 都會被當作整數驗證；不正確的值會導致機器人啟動失敗。

**範例：「User ID администратора бота」欄位的值。** 單一管理員 —— 就是一個數字：

```
123456789
```

兩個管理員以逗號分隔（可以不加空格）：

```
123456789,987654321
```

每個值都必須是整數。形如 `@username` 或 `123 456`（數字中間有空格）的寫法不行 —— 機器人不會啟動。

#### 代理

支援 `socks5://`、`http://` 與 `https://` 協定。如果代理欄位留空，機器人會嘗試使用面板的通用代理（如果已設定且其協定受支援）。協定不受支援或語法不正確的 URL 會被忽略 —— 機器人會直接連線。當伺服器到 Telegram API 的直接存取被封鎖時，代理就很有用。

#### 電子郵件通知 (SMTP)

除了 Telegram 之外，相同的事件也可以透過郵件接收。此通道在 **設定 → Email** 區段的 **SMTP Settings** 分頁中設定：

| 欄位 (UI) | 設定鍵 | 預設值 | 說明 |
|---|---|---|---|
| Enable Email Notifications | `smtpEnable` | `false` | 透過 SMTP 發送 email 通知的主開關。 |
| SMTP Host | `smtpHost` | （空） | SMTP 伺服器主機（例如 `smtp.gmail.com`）。 |
| SMTP Port | `smtpPort` | `587` | SMTP 伺服器連接埠。 |
| SMTP Username | `smtpUsername` | （空） | SMTP 驗證用的使用者名稱。也作為寄件者位址 (From) 使用。 |
| SMTP Password | `smtpPassword` | （空） | SMTP 驗證用的密碼。隱藏儲存；如果密碼已設定，欄位會顯示「已設定」標記，可以留空以保留目前的密碼。 |
| Recipients | `smtpTo` | （空） | 收件者清單，以逗號分隔（例如 `admin@example.com, ops@example.com`）。 |
| Encryption | `smtpEncryptionType` | `starttls` | 連線加密類型：`none`（不加密）、`starttls`（STARTTLS）或 `tls`（隱式 TLS）。 |

**Send Test Email** 按鈕會發送一封測試郵件，並依階段顯示結果：**Connection**（連線）、**Authentication**（驗證）與 **Send**（發送）。如果有問題，診斷會指出錯誤發生在哪個階段（例如「Authentication failed — check username and password」或「Server requires STARTTLS — change encryption type」），有助於調整參數。

在第二個分頁（**Notifications**）中選擇哪些事件會發送郵件 —— 使用與 Telegram 相同的卡片群組（見第 14.5 節的「事件匯流排與通知選擇」）。

#### Telegram API 伺服器

預設情況下機器人會連到 Telegram 官方 API。在 **Telegram API Server** 欄位中可以指定自架 Bot API 伺服器（`telegram-bot-api`）的位址。URL 會經過安全性檢查；被封鎖或不正確的位址會被捨棄，並改用預設伺服器。

### 14.2. 主選單與按鈕

選單以 **`/start`** 指令呼叫。按鈕是附加在訊息上的 inline 鍵盤；按鈕的組合取決於您是管理員還是用戶端。

#### 管理員選單

| 按鈕 | 動作 |
|---|---|
| 📊 Отсортированный отчёт об использовании трафика | 列出所有用戶端，依流量排序，並列出每個用戶端的用量；沒有資料的「多餘」email 會標記「❗ Нет результатов」。 |
| 💻 Состояние сервера | 伺服器摘要（見第 14.5 節）。「🔄 Обновить」按鈕會重新繪製資料。 |
| Сбросить весь трафик | 重置**所有**用戶端的流量計數器。會要求確認（「Вы уверены? 🤔」），然後對每個用戶端輸出「✅ Успешно」或「❌ Неудача」，最後顯示「🔚 Сброс трафика завершён для всех клиентов」。 |
| 📂 Бэкап БД | 發送資料庫檔案與 `config.json`（見第 14.6 節）。 |
| 📄 Лог банов | 發送依 IP 限制被封鎖位址的記錄檔。 |
| 🔌 Входящие подключения | 所有 inbound 的摘要：Remark、連接埠、流量、用戶端數量、到期日期。 |
| ⚠️ Скоро конец | 流量或期限即將耗盡的 inbound 與用戶端清單（見第 14.5 節）。 |
| 🖱️ Команды | 顯示管理員指令說明。 |
| 🟢 Онлайн | 線上用戶端的數量與清單；點選 email 會開啟用戶端卡片。「🔄 Обновить」按鈕。 |
| 👥 Все клиенты | 開啟 inbound 選擇，然後顯示其用戶端清單 —— 供檢視/管理。 |
| ➕ Новый клиент | 啟動新增用戶端精靈（選擇 inbound → 草稿 → 確認）。 |
| Настройки подписки / индивидуальные ссылки / QR-код | 選擇 inbound 與用戶端以取得訂閱連結、個別連結或 QR 碼。 |

#### 用戶端選單

用戶端可使用的按鈕較少：

| 按鈕 | 動作 |
|---|---|
| Статистика клиента | 顯示綁定到用戶端 Telegram User ID 的所有訂閱資料。 |
| 🖱️ Команды | 顯示用戶端指令說明。 |
| Настройки подписки | 選擇自己的用戶端 → 訂閱連結。 |
| Индивидуальные ссылки | 選擇自己的用戶端 → 個別連結。 |
| QR-код | 選擇自己的用戶端 → QR 碼。 |

如果使用者沒有任何用戶端綁定其 Telegram User ID，機器人會回覆：「❌ Ваша конфигурация не найдена! 💭 Пожалуйста, попросите администратора использовать ваш Telegram User ID в конфигурации. 🆔 Ваш User ID: …」。需要將此 ID 提供給管理員，讓他填入用戶端欄位。

### 14.3. 機器人指令

機器人註冊了四個指令，會顯示在 Telegram 的「/」選單中：

| 指令 | 說明（來自選單） | 存取權限 | 功能 |
|---|---|---|---|
| `/start` | 顯示主選單 | 所有人 | 歡迎訊息；對管理員另外顯示「🤖 Добро пожаловать в бота управления <Host>!」與主選單。 |
| `/help` | 機器人說明 | 所有人 | 顯示一般歡迎訊息與選擇選單項目的提示。 |
| `/status` | 檢查機器人狀態 | 所有人 | 回覆「✅ Бот функционирует нормально」。 |
| `/id` | 顯示您的 Telegram ID | 所有人 | 回傳「🆔 Ваш User ID: <code>…</code>」。方便取得自己的 User ID。 |

除了已註冊的指令外，還處理另外三個帶參數的指令（它們不會顯示在「/」選單中，但可以運作）：

- **`/usage [Email]`** —— 依 email 搜尋用戶端。
  - 對**管理員**顯示完整的用戶端卡片（含管理按鈕）。
  - 對**用戶端**僅顯示其本人、具有指定 email 的訂閱（依 Telegram User ID 綁定）。不帶參數時，機器人會要求指定 email：「❗ Пожалуйста, укажите email для поиска」。
- **`/inbound [имя подключения]`** —— 僅限管理員。依 Remark 搜尋 inbound 並輸出其參數及所有用戶端的統計。不帶參數（或對用戶端）時 —— 「❗ Неизвестная команда」。
- **`/restart`** —— 僅限管理員。重啟 Xray Core。可能的回應：「✅ Ядро Xray успешно перезапущено」、「❗ Xray Core не запущен」（如果核心未運作）、「❗ Ошибка при перезапуске Xray-core. <Ошибка>」。`/restart` 後帶任何參數都會導致顯示未知指令的訊息，並附上 `/restart` 提示。

在群組聊天中，形如 `/команда@botusername` 的指令僅在 username 與目前機器人名稱相符時才會處理。

管理員說明（「Команды」按鈕）：

```
🔃 Для перезапуска Xray Core: /restart
🔎 Для поиска клиента по email: /usage [Email]
📊 Для поиска входящих подключений (со статистикой клиентов): /inbound [имя подключения]
🆔 Ваш Telegram User ID: /id
```

用戶端說明：

```
💲 Для просмотра информации о вашей подписке: /usage [Email]
🆔 Ваш Telegram User ID: /id
```

### 14.4. 用戶端管理（僅限管理員）

開啟用戶端卡片後（透過「Все клиенты」、「Онлайн」、「Скоро конец」或 `/usage`），管理員會看到用戶端的資訊（email、綁定的 inbound、「Активен」狀態、連線狀態、到期日期、流量用量）與 inline 管理按鈕：

| 按鈕 | 用途 |
|---|---|
| 🔄 Обновить | 重新讀取用戶端卡片。 |
| 📈 Сбросить трафик | 將用戶端的流量計數器歸零。需要確認「✅ Подтвердить сброс трафика?」。 |
| 🚧 Лимит трафика | 設定流量上限。現成的數值：♾ Безлимит (0)、1/5/10/20/30/40/50/60/80/100/150/200 GB 或「🔢 Своё」—— 在內建的數字鍵盤上輸入數字（按鍵 0–9、「🔄」—— 重置為 0、「⬅️」—— 刪除最後一位數字、「✅ Подтвердить: N」）。數值以 GB 為單位設定。 |
| 📅 Изменить дату окончания | 現成的選項：♾ Безлимит、「🔢 Своё」、增加 7/10/14/20 天、1/3/6/12 個月。正數會延長期限（將天數加到目前的到期日期，若期限已過則加到「現在」）；0 取消期限限制。 |
| 🔢 Лог IP | 顯示用戶端記錄到的 IP 位址（如有則含時間戳記）。從記錄中可使用「🔄 Обновить」與「❌ Очистить IP」（需確認「✅ Подтвердить очистку IP?」）。 |
| 🔢 Лимит IP | 限制同時連線的 IP 數。選項：♾ Безлимит (0)、1–10 或「🔢 Своё」（數字鍵盤）。 |
| 👤 Установить пользователя Telegram | 顯示用戶端目前綁定的 Telegram User ID；可清除綁定（「❌ Удалить пользователя Telegram」，需確認）。透過 Telegram 系統的聯絡人選擇來綁定新使用者。 |
| 🔘 Вкл./Выкл. | 啟用或停用用戶端。需要確認「✅ Подтвердить вкл/выкл пользователя?」。 |

所有變更設定的操作（流量/IP 上限、到期日期、Telegram 使用者的綁定/解除綁定、啟用/停用）會在需要時將 Xray 標記為待重啟，以使變更生效。操作成功後，機器人會輸出形如「✅ <email>: …」的確認訊息，並重新顯示卡片。

精靈中任何數字輸入都限制為小於 999999 的值。

### 14.5. 通知與報告

通知會發送給所有管理員（`tgBotChatId` 中的所有 User ID）。

#### 事件匯流排與通知選擇

通知建構於單一事件匯流排之上，而傳遞通道有兩個 —— **Telegram** 與**電子郵件 (SMTP)**。對每個通道分別選擇要對哪些事件發出通知。在 **設定 → Telegram** 中這是在 **Notifications** 分頁進行，在 **設定 → Email** 中則在同名分頁進行。

事件以卡片分組；每個群組都有一個主開關，附帶已啟用事件的計數器（n/總數）以及只選了一部分時的中間狀態。可用的群組有：

- **Outbound** —— 「Down」(`outbound.down`) 與「Up」(`outbound.up`)：outbound 中斷與恢復。
- **Xray Core** —— 「Crash」(`xray.crash`)：Xray 核心異常終止。
- **Nodes** —— 「Down」(`node.down`) 與「Up」(`node.up`)：節點變得無法存取或已恢復。
- **System** —— 「CPU high (%)」(`cpu.high`) 與「Memory high (%)」(`memory.high`)：處理器與記憶體高負載。這兩個事件旁邊都有一個百分比門檻的 inline 欄位。
- **Security** —— 「Login attempt」(`login.attempt`)：嘗試登入面板。

已啟用事件的集合分開儲存：Telegram 在 `tgEnabledEvents` 中，Email 在 `smtpEnabledEvents` 中。預設情況下兩個通道都啟用「Login attempt」與「CPU high」（值為 `login.attempt,cpu.high`）。

#### 面板登入通知

由 **Уведомление о входе** 核取方塊控制（`tgBotLoginNotify`，預設啟用）。每次嘗試登入 Web 面板時，管理員都會收到訊息：

- 成功時：「✅ Успешный вход в панель.」+ 主機、使用者名稱、IP、時間。
- 失敗時：「❗️ Ошибка входа в панель.」+ 主機、**原因**（例如第二因素錯誤時的「Ошибка 2FA」）、使用者名稱、IP、時間。

#### CPU 與記憶體負載超標

面板每分鐘檢查一次處理器與記憶體的負載。如果門檻 **`tgCpu`** > 0 且該分鐘的平均 CPU 負載超過它，管理員會收到：「🔴 Загрузка процессора составляет N%, что превышает пороговое значение M%」。同樣地會以門檻 **`tgMemory`**（預設 80%）檢查 RAM 負載 —— 對應事件「Memory high (%)」。

這兩個門檻由 **Notifications** 分頁中 **System** 群組裡「CPU high (%)」與「Memory high (%)」事件旁的 inline 欄位設定（見下方「事件匯流排與通知選擇」）。對 Email 通道則有獨立的鍵 `smtpCpu` 與 `smtpMemory`。門檻值為 0 時停用對應的檢查。

#### 週期性報告（依排程）

依 **Частота уведомлений** 欄位的 cron 運算式排程（`tgRunTime`，預設 `@daily`）。如果值為空或不正確，則使用 `@daily`。報告包含：

#### 排程建構器

**Частота уведомлений для администраторов от бота** 欄位不是手動輸入字串，而是透過排程建構器設定。首先在下拉清單中選擇模式：

- **`@every` — повторять с интервалом** —— 會出現數字欄位與單位選擇（**Секунды** / **Минуты** / **Часы**）；最終會組成形如 `@every 6h` 的運算式。
- **`@hourly` — каждый час**、**`@daily` — каждый день в 00:00**、**`@weekly` — каждую неделю**、**`@monthly` — каждый месяц** —— 現成的預設值，會儲存為對應的巨集（`@hourly`、`@daily`、`@weekly`、`@monthly`）。
- **Произвольный (crontab)** —— 用於自訂 crontab 運算式的欄位。面板的排程器啟用了秒，因此自訂運算式由 **6 個欄位**組成：秒、分、時、月中日、月、星期幾（例如 `0 30 8 * * *` —— 每天 08:30:00）。切換到此模式時，欄位會填入目前選擇的 crontab 等價值，以便有個起點。

**範例：「Частота уведомлений」欄位（`tgRunTime`）的值。** 同時支援現成的縮寫與完整的 crontab 格式：

| 值 | 何時觸發 |
|---|---|
| `@daily` | 每天午夜一次（預設值） |
| `@hourly` | 每小時 |
| `@every 6h` | 每 6 小時 |
| `0 9 * * *` | 每天 09:00 |
| `0 9 * * 1` | 每週一 09:00 |
| `0 */12 * * *` | 每 12 小時（00:00 與 12:00） |

crontab 中的欄位順序：分、時、月中日、月、星期幾。

1. 「🕰 Запланированные отчёты: <расписание>」這一行與目前的日期/時間。
2. **Состояние сервера**（見下方）。
3. 依 inbound 與用戶端的「Скоро конец」區塊。
4. 給綁定了 Telegram User ID 的用戶端的個人通知 —— 每個非管理員用戶端都會收到其訂閱清單，列出流量/期限即將耗盡者（含已停用者）。
5. 如果啟用 **Резервное копирование базы данных**（`tgBotBackup`）—— 將資料庫備份發給管理員。

**Состояние сервера** 包含：主機、3X-UI 與 Xray 版本、IPv4/IPv6、運作時間（以天計）、平均負載 (Load1/2/3)、RAM（目前/總計）、線上用戶端數、TCP/UDP 連線計數器、總網路流量 (↑/↓) 與 Xray 狀態。

**「Скоро конец」** 顯示：

- 依 inbound：已停用的數量與「即將耗盡」的數量，然後列舉這些 inbound（Remark、連接埠、流量、到期日期）；
- 依用戶端：同上，再加上用戶端卡片與帶其 email 的按鈕（點選會開啟用戶端卡片）。

「即將耗盡」的門檻取自面板的通用設定：流量餘量（以 GB 計）與期限餘量（以天計）。當 inbound/用戶端距離流量上限剩餘量小於門檻，**或**距離到期日期剩餘量小於門檻時，即被視為「即將耗盡」。

### 14.6. 備份與記錄

- **Бэкап БД**（「📂 Бэкап БД」按鈕或週期性報告中的核取方塊）：機器人會發送備份時間、資料庫檔案（`x-ui.db`，或 PostgreSQL 用的 `x-ui.dump`）與 Xray 設定檔 `config.json`。
- **Лог банов**（「📄 Лог банов」按鈕）：發送因超過 IP 上限而被封鎖之 IP 位址的目前與前一個記錄檔。空檔案不會發送。

### 14.7. 運作特性

- **長訊息**會分割成多個部分（門檻約 2000 字元），inline 鍵盤會附加到最後一個部分。
- **並行性**：指令與按鈕點選會並行處理（最多 10 個同時處理器的池）。
- **發送可靠性**：連線發生錯誤時，訊息會以指數退避重試發送（1s/2s/4s，最多 3 次嘗試）。
- **快取**：「Состояние сервера」的資料會被快取，以免頻繁點選「Обновить」對系統造成負擔。
- **重啟機器人**：在儲存設定並重啟面板時，前一個輪詢循環會正確停止，並啟動新的循環 —— 同時只會運作一個接收更新的執行個體。

---

## 15. 地理資料庫（geoip / geosite 與自訂）

地理資料庫是 Xray-core 用於依國家歸屬（IP 區段）或網域類別來進行流量路由與過濾的 `.dat` 二進位檔案。面板既能下載與更新標準的地理檔案集合，也能更新以 URL 指定的任意使用者來源。所有檔案都儲存在 Xray 二進位檔旁的 `bin` 目錄（預設路徑為 `bin`，可透過環境變數 `XUI_BIN_FOLDER` 覆寫）。

### 15.1. geoip.dat 與 geosite.dat 是什麼

- **geoip.dat** — 「IP 位址 → 國家/地區代碼」的對應資料庫。在路由規則中以 `geoip:<代碼>` 的形式使用，例如 `geoip:ru`、`geoip:cn`，以及特殊標記 `geoip:private`（私有/本地網路）。本質上它回答的是「這個 IP 位於哪個國家」這個問題。
- **geosite.dat** — 「網域 → 類別/清單」的對應資料庫。以 `geosite:<類別>` 的形式使用，例如 `geosite:category-ads-all`（廣告網域）、`geosite:google`、`geosite:ru`。本質上它是分組的網域清單。

這些檔案用於建構諸如「指向俄羅斯 IP/網域的所有流量直連，其餘走 outbound」之類的規則。規則本身在 Xray 的路由區段中設定；地理資料庫只是為其提供資料。沒有最新的地理檔案，引用 `geoip:`/`geosite:` 的規則將無法生效，或會依賴過時的清單。

**範例：「俄羅斯網域與 IP 直連」規則。** 路由區段中的此規則會把指向俄羅斯資源的所有流量導向帶有 `direct` 標籤的 outbound：

```json
{
  "type": "field",
  "domain": ["geosite:category-ru"],
  "ip": ["geoip:ru"],
  "outboundTag": "direct"
}
```

### 15.2. 標準地理檔案及其更新

面板包含一份固定的「白名單」（allowlist），由六個帶有硬編碼下載來源的標準檔案組成。更新透過 `POST /panel/api/server/updateGeofile/:fileName` 執行（或不帶檔案名稱以一次更新全部）。

**範例：透過 API 更新單一檔案與一次更新全部。** 只更新 `geoip_RU.dat`：

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/updateGeofile/geoip_RU.dat' \
  -H 'Cookie: 3x-ui=<session-cookie>'
```

以一個請求更新全部六個標準檔案（不指定檔案名稱）：

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/updateGeofile' \
  -H 'Cookie: 3x-ui=<session-cookie>'
```

成功回應：

```json
{ "success": true, "msg": "Geofile updated successfully", "obj": null }
```

| 檔案名稱 | 來源（發行版儲存庫） |
|---|---|
| `geoip.dat` | `github.com/Loyalsoldier/v2ray-rules-dat` (geoip.dat) |
| `geosite.dat` | `github.com/Loyalsoldier/v2ray-rules-dat` (geosite.dat) |
| `geoip_IR.dat` | `github.com/chocolate4u/Iran-v2ray-rules` (geoip.dat) |
| `geosite_IR.dat` | `github.com/chocolate4u/Iran-v2ray-rules` (geosite.dat) |
| `geoip_RU.dat` | `github.com/runetfreedom/russia-v2ray-rules-dat` (geoip.dat) |
| `geosite_RU.dat` | `github.com/runetfreedom/russia-v2ray-rules-dat` (geosite.dat) |

標準檔案更新的特性：

- **更新單一檔案的按鈕。** 下載前會顯示確認：「您確定要更新地理檔案嗎？」並附說明「這將更新檔案 #filename#。」（英文 *Do you really want to update the geofile? This will update the #filename# file.*）。成功時會彈出通知「地理檔案更新成功」（英文 *Geofile updated successfully*）。
- **「Update all」按鈕**（英文 *Update all*）會下載全部六個檔案。確認：「這將更新所有地理檔案。」（英文 *This will update all geofiles.*）。
- **條件式下載。** 若本地檔案已存在，請求中會帶入 `If-Modified-Since` 標頭，附上檔案的修改時間。伺服器回應 `304 Not Modified` 表示檔案未變更——不會重新下載，只更新檔案的時間戳記。
- **檔案名稱安全性。** 只接受 allowlist 中的名稱；名稱會檢查是否不含 `..`、路徑分隔符 `/` 與 `\`、絕對路徑，且必須符合 `^[a-zA-Z0-9._-]+\.dat$` 樣式。任何清單外的名稱都會以錯誤「Invalid geofile name」被拒絕。
- **Xray 重啟。** 下載地理檔案後，Xray-core 會重啟以重新讀取更新後的資料庫。若重啟失敗，錯誤訊息中會附加相應的字串。

#### 從命令列更新地理資料庫（x-ui）

地理資料庫也可以不透過面板更新——透過互動式選單 `x-ui`（更新地理檔案的項目），或非互動指令 `x-ui update-all-geofiles`。集合中的每個檔案（geoip/geosite，包含 IR 與 RU 集合）都會輸出各自的狀態：「已更新」、「已是最新」或「下載錯誤」。下載失敗時不會列印虛假的成功訊息。只有在至少有一個檔案確實被更新時，才會發生 Xray 重啟（也就是中斷活躍連線）；若沒有任何檔案變更（全部回傳 `304 Not Modified`），則面板與 Xray 都不會重啟。

### 15.3. 透過 Xray 自動更新地理資料（Geodata Auto-Update）

以任意 URL 指定的額外 `.dat` 來源，並非透過面板新增，而是透過 Xray-core 原生的 `geodata` 區段。相應的章節被放置於 Xray 更新的模態視窗中（儀表板 → Xray 更新，`xrayUpdates`）——即「自動更新 Geodata」分頁（英文 *Geodata Auto-Update*）。面板在此僅編輯 Xray 設定範本中的 `geodata` 鍵；檔案的下載、驗證與熱重載由 Xray 核心自身負責。

章節上方會顯示提示：「Xray 會依排程下載這些檔案並在不重啟的情況下熱重載它們。URL 必須為 HTTPS。在 Xray 能更新某檔案之前，該檔案必須已存在於 bin 資料夾中。」（英文 *Xray downloads these files on schedule and hot-reloads them without a restart. URLs must be HTTPS. Each file must already exist in the bin folder once before Xray can update it.*）。

#### 章節欄位

- **排程（cron）**（英文 *Schedule (cron)*）— 5 個欄位的 cron 字串；預設值為 `0 4 * * *`（每天 04:00）。儲存時會檢查字串是否剛好包含 5 個欄位，否則會輸出錯誤「Cron 必須包含 5 個欄位，例如 0 4 * * *」。
- **透過 outbound 下載（選填）**（英文 *Download through outbound (optional)*）— 一個下拉清單，列出可用的 outbound 標籤（外加訂閱的 outbound），Xray 會透過它來下載檔案；協定為 `blackhole` 的 outbound 不會出現在清單中。此欄位可留空——此時將使用直接連線。此選擇與面板自身請求所用的 outbound 無關（見 §11）：geodata 自動更新有其專屬、獨立的下載用 outbound。
- **檔案清單** — 每一行設定一組「URL + 檔案名稱」（英文 *File name*）。URL 必須以 `https://` 開頭（否則顯示「每個檔案都需要 HTTPS URL。」）。檔案名稱以單純形式指定，不含路徑與分隔符——只能是 `^[A-Za-z0-9._-]+$` 字元（否則顯示「檔案名稱必須單純，例如 geosite_custom.dat（不含路徑）。」）。輸入 URL 時，面板會嘗試從路徑的最後一段自動填入檔案名稱。「Add file」按鈕（英文 *Add file*）會新增一行，垃圾桶按鈕會刪除該行。

若清單為空，會顯示提示：「尚未設定檔案。在路由規則中以 ext:geosite_custom.dat:category 形式引用檔案。」（英文 *No files configured. Reference files in routing rules as ext:geosite_custom.dat:category.*）。

#### 儲存

「儲存並重啟 Xray」按鈕（英文 *Save & Restart Xray*）會顯示確認「儲存 geodata 設定？」並附說明「Xray 設定範本將被更新，且 Xray 會被重啟。」（英文 *Save geodata settings? This updates the Xray config template and restarts Xray.*）。儲存後，`geodata` 鍵會寫入設定範本（`POST /panel/api/xray/update`），且 Xray 會重啟（`POST /panel/api/server/restartXrayService`）。若檔案清單為空，`geodata` 鍵會從範本中移除。

重要特性：

- **檔案必須已存在於 `bin`。** Xray 只更新在啟動時已存在於 `bin` 資料夾中的 `.dat` 檔案。因此新的自訂檔案要先手動放入 `bin`（或至少在那裡以所需名稱建立一個空白/過時版本），之後 Xray 才會開始依排程維持其最新狀態。
- **熱重載。** 在排程下載後，Xray 會重新讀取更新後的資料庫，而不需要完整重啟程序。
- **相容性。** 先前下載的地理檔案（無論標準或自訂）都會繼續以 `ext:` 語法在路由規則中運作，無需變更。

若清單為空，會顯示提示：「尚無自訂 geo 來源——點擊「新增」來建立一個」（英文 *No custom geo sources yet — click Add to create one*）。

#### 表格欄位與來源欄位

| 欄位（UI） | JSON | 預設值 | 說明 |
|---|---|---|---|
| 類型（*Type*） | `type` | —（必填） | 資源類型：僅 `geosite` 或 `geoip`。決定最終檔案的名稱。 |
| 別名（*Alias*） | `alias` | —（必填） | 來源的簡短識別碼。由它與類型組成檔案名稱。 |
| URL（*URL*） | `url` | —（必填） | 指向 `.dat` 檔案的直接連結（http/https）。 |
| 已啟用（*Enabled*） | — | — | 來源在清單中是否啟用的標記。 |
| 已更新（*Last updated*） | `lastUpdatedAt` | `0` | 上次成功更新的時間（Unix 時間；`0` 表示尚未更新）。 |
| 路由（ext:…）（*Routing (ext:…)*） | — | — | 路由規則的現成字串：`ext:<檔案.dat>:tag`。 |
| 動作（*Actions*） | — | — | 「編輯」、「刪除」、「立即更新」按鈕。 |

此外，資料庫中還儲存了內部欄位：`localPath`（檔案在 `bin` 目錄中的實際路徑）、`lastModified`（伺服器回傳的 `Last-Modified` 標頭值，用於條件式下載）、`createdAt` 與 `updatedAt`。

#### 檔案命名

最終檔案的名稱會自動由類型與別名組成：

- 類型 `geoip` → `geoip_<alias>.dat`；
- 類型 `geosite` → `geosite_<alias>.dat`。

例如，類型為 `geosite` 且別名為 `myads` 的來源會建立檔案 `geosite_myads.dat`。

**範例：透過 API 新增來源。** 將你自己的廣告網域清單新增為別名 `myads` 的 `geosite` 資源：

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

面板會將檔案下載到 `bin` 目錄並命名為 `geosite_myads.dat`，儲存記錄並重啟 Xray。

#### 按鈕與動作

- **新增**（英文 *Add*）— 開啟「新增來源」表單（英文 *Add custom geo*）。儲存按鈕為「儲存」（英文 *Save*）。API：`POST /add`。
- **編輯**（英文 *Edit*）— 「編輯來源」表單（英文 *Edit custom geo*）。API：`POST /update/:id`。變更類型或別名時，舊檔案會被刪除，新檔案會重新下載。
- **刪除**（英文 *Delete*）— 確認「刪除此自訂來源？」（英文 *Delete this custom geo source?*）。刪除資料庫中的記錄以及 `.dat` 檔案本身。API：`POST /delete/:id`。成功時：「自訂 geo 檔案「<名稱>」已刪除」。
- **立即更新**（英文 *Update now*）— 重新下載特定來源並更新時間戳記。API：`POST /download/:id`。成功時：「Geofile「<名稱>」已更新」。
- **更新全部** — 一次更新所有自訂來源。API：`POST /update-all`。完全成功時：「所有自訂 geo 來源已更新」（英文 *All custom geo sources updated*）。若至少有一個來源未能更新，操作視為部分失敗，訊息為「無法更新一個或多個自訂來源」（英文 *One or more custom geo sources failed to update*），且回應中會列出成功與失敗的來源。

任一動作（新增、編輯、刪除、更新、有成功項目時的更新全部）之後，Xray-core 都會重啟。

#### 逐步操作：新增來源

1. 點擊「新增」。
2. 在「類型」欄位選擇 `geosite` 或 `geoip`。
3. 在「別名」欄位輸入識別碼（只能是小寫拉丁字母、數字、`-` 與 `_`；佔位提示：`a-z 0-9 _ -`）。
4. 在「URL」欄位指定指向 `.dat` 檔案的直接連結（必須以 `http://` 或 `https://` 開頭）。
5. 點擊「儲存」。面板會立即將檔案下載到 `bin` 目錄、儲存記錄並重啟 Xray。

### 15.4. 驗證與限制

建立與編輯來源時會執行嚴格的檢查。錯誤訊息：

| 條件 | 訊息（RU） | 訊息（EN） |
|---|---|---|
| 類型不是 `geosite`/`geoip` | Тип должен быть geosite или geoip | *Type must be geosite or geoip* |
| 別名為空 | Укажите псевдоним | *Alias is required* |
| 別名含不允許字元（不符合 `^[a-z0-9_-]+$`） | Псевдоним содержит недопустимые символы | *Alias must match allowed characters* |
| 別名被保留 | Этот псевдоним зарезервирован | *This alias is reserved* |
| URL 為空 | Укажите URL | *URL is required* |
| URL 無法解析 | Некорректный URL | *URL is invalid* |
| 協定不是 http/https | URL должен использовать http или https | *URL must use http or https* |
| 主機為空/無效，或被 SSRF 防護封鎖 | Некорректный хост URL | *URL host is invalid* |
| 「類型 + 別名」重複 | Такой псевдоним уже используется для этого типа | *This alias is already used for this type* |
| 找不到來源 | Источник не найден | *Custom geo source not found* |
| 下載錯誤 | Ошибка загрузки | *Download failed* |

表單中的提示（用戶端驗證）：「別名：只能用 a-z、數字、- 與 _」（*Alias may only contain lowercase letters, digits, - and _*）以及「URL 必須以 http:// 或 https:// 開頭」（*URL must start with http:// or https://*）。

額外的技術限制：

- **保留別名。** 不能使用與標準檔案衝突的別名。已保留（比較不分大小寫，連字號等同於底線）：`geoip`、`geosite`、`geoip_ir`、`geosite_ir`、`geoip_ru`、`geosite_ru`。例如，`geosite-ru` 會被當作 `geosite_ru` 而遭拒絕。
- **SSRF 防護。** URL 的主機會被解析為 IP，若它指向私有/內部位址，下載會被封鎖（使用者會看到「Некорректный хост URL」）。這可防止利用面板存取內部服務。
- **path traversal 防護。** 最終檔案路徑必須位於 `bin` 目錄內（含符號連結解析）；嘗試越出其範圍將被拒絕。
- **最小檔案大小。** 下載的檔案只有在不小於 64 位元組時才被視為有效；過小的檔案會以下載錯誤被拒絕。
- **代理與條件式下載。** 若面板設定中指定了代理，下載會透過它進行；其餘情況則使用具 SSRF 安全傳輸的直接連線。如同標準檔案，會套用 `If-Modified-Since`/`304 Not Modified`（未變更的檔案不會重新下載）。下載逾時為 10 分鐘，URL 可用性探測（HEAD，必要時為部分 GET）為 12 秒。

### 15.5. 面板啟動時的自動檢查

面板啟動時會遍歷所有自訂來源，並對每一個檢查本地檔案是否存在與完整（檔案缺失、為目錄，或小於 64 位元組）。若檔案缺失或損毀，會對來源進行探測並嘗試重新下載。這確保在重新安裝或 `bin` 目錄遺失後，自訂地理檔案會被自動還原。

### 15.6. 在路由規則中使用地理資料庫

在 Xray 的路由規則中，地理資料庫透過前綴用於 `domain`/`ip` 之類的欄位：

- **geoip:** 用於 IP 資料庫——`geoip:<代碼>`。範例：`geoip:ru`、`geoip:cn`、`geoip:private`。取自 `geoip.dat`（若規則指向特定檔案，則取自 `geoip_RU.dat` 等）。
- **geosite:** 用於網域資料庫——`geosite:<類別>`。範例：`geosite:category-ads-all`、`geosite:google`、`geosite:ru`。取自 `geosite.dat`。

**範例：透過 geosite 封鎖廣告。** 此規則將所有廣告網域送往「黑洞」（假設有帶 `blocked` 標籤、協定為 `blackhole` 的 outbound）：

```json
{
  "type": "field",
  "domain": ["geosite:category-ads-all"],
  "outboundTag": "blocked"
}
```

對於**自訂**檔案，使用外部檔案語法 `ext:`。UI 中的提示：「在路由規則中以 ext:檔案.dat:標籤 的形式使用該值（替換標籤）。」（英文 *In routing rules use the value column as ext:file.dat:tag (replace tag).*）。格式：

```
ext:<檔案名稱.dat>:<標籤>
```

其中 `<檔案名稱.dat>` 為 `geoip_<alias>.dat` 或 `geosite_<alias>.dat`，而 `<標籤>` 為檔案內部的特定清單/類別。面板在「路由（ext:…）」欄位中會提示形如 `ext:geosite_myads.dat:tag` 的現成範本——只需把 `tag` 替換為所需的標籤。此類檔案的名稱在「自動更新 Geodata」章節（見 §15.3）的「檔案名稱」欄位中設定——例如 `geosite_custom.dat`；在規則中以 `ext:geosite_custom.dat:category` 引用它。

**範例：基於自訂檔案的規則。** 若新增了類型為 `geosite`、別名為 `myads` 的來源，而 `.dat` 檔案內部的清單以 `ads` 標籤標記，路由規則如下：

```json
{
  "type": "field",
  "domain": ["ext:geosite_myads.dat:ads"],
  "outboundTag": "blocked"
}
```

對於 IP 來源（類型 `geoip`、別名 `mycorp`、標籤 `office`），欄位會是 `"ip": ["ext:geoip_mycorp.dat:office"]`。

---

## 16. 運維：備份、日誌、更新、CLI

本章節涵蓋面板的日常維護：建立與還原資料庫備份、檢視面板與 Xray 的日誌（記錄）、重新啟動與停止服務、更新 Xray 與面板本身、週期性任務（cron）以及移除面板。部分操作在 Web 介面中執行（「儀表板」與「面板設定」頁面上的分頁），部分則透過伺服器上的 `x-ui` 主控台選單執行。

### 16.1. 資料庫的備份與還原

面板的所有資料（入站/inbound、用戶端、群組、節點、設定）都儲存在同一個資料庫中。備份管理位於 **「儀表板」** 頁面的 **「備份」** 分頁，區塊標題為 **「備份與還原」**。

面板支援兩種資料庫引擎，備份行為也會因此而不同：

- **SQLite**（預設方案）—— 資料存放於 `x-ui.db` 檔案中。
- **PostgreSQL** —— 若面板設定為使用 PostgreSQL，區塊內會顯示提示：
  > 「此面板執行於 PostgreSQL。『備份』會下載 pg_dump 封存檔（.dump），而『還原』會透過 pg_restore 將其載入回去。伺服器上必須安裝 PostgreSQL 用戶端工具（pg_dump 與 pg_restore）。」

#### 匯出（建立備份）

**「匯出資料庫」** 按鈕（英文 `Back Up`）會將備份檔案下載到您的裝置。

| 資料庫引擎 | 檔案名稱 | 伺服器上發生的動作 |
|-----------|-----------|----------------------------|
| SQLite | `x-ui.db` | 先執行 WAL checkpoint，確保檔案包含最新記錄，接著完整讀取檔案並提供下載 |
| PostgreSQL | `x-ui.dump` | 執行 `pg_dump`，封存檔提供下載 |

介面中的提示：
- SQLite：「點擊以將包含您目前資料庫備份的 .db 檔案下載到您的裝置。」
- PostgreSQL：「點擊以將目前資料庫的 PostgreSQL 傾印檔（.dump）下載到您的裝置。」

技術上，匯出就是一個 `GET /panel/api/server/getDb` 請求。附件名稱由伺服器根據引擎生成（`Content-Disposition`）。

備份檔案的名稱依伺服器位址生成，而非固定為 `x-ui.db` / `x-ui.dump`。從瀏覽器下載時，名稱取自網址列中面板的位址（請求主機名），否則取自設定的網域，若也未設定則取自伺服器的公網 IP（先 IPv4，再 IPv6），最後退回 `x-ui`。如此一來，不同伺服器的備份就很容易區分。SQLite 副檔名維持 `.db`，PostgreSQL 維持 `.dump`；透過 Telegram 的備份也依相同的網域/IP 命名。

**範例：透過 API 下載備份。** 同樣的匯出也可以透過主控台請求取得 —— 例如用於自動備份腳本。需要一個已授權的工作階段（登入 cookie）：

```bash
# 1) 登入並儲存工作階段 cookie
curl -s -c cookies.txt \
     -d 'username=admin&password=admin' \
     https://panel.example.com:2053/panel/login

# 2) 下載資料庫檔案（名稱由伺服器決定：x-ui.db 或 x-ui.dump）
curl -s -b cookies.txt -OJ \
     https://panel.example.com:2053/panel/api/server/getDb
```

若面板以基礎路徑（Web Base Path）開啟，則需將其加入 URL：`…:2053/<base_path>/panel/api/server/getDb`。

#### 匯入（還原）

**「匯入資料庫」** 按鈕（英文 `Restore`）會開啟檔案選擇，並將其上傳到伺服器以進行還原（`POST /panel/api/server/importDB`，表單欄位 `db`）。

介面中的提示：
- SQLite：「點擊以從您的裝置選擇並上傳 .db 檔案，從備份還原資料庫。」
- PostgreSQL：「點擊以選擇並上傳 .dump 檔案來還原 PostgreSQL 資料庫。這將取代所有目前的資料。」

**SQLite 的匯入流程（重要的是理解它是原子性的且具備回滾機制）：**
1. 上傳的檔案會檢查格式 —— 必須是有效的 SQLite 資料庫；否則回傳錯誤「Invalid db file format」。
2. 檔案儲存為臨時檔 `x-ui.db.temp` 並通過完整性檢查。
3. 在替換資料庫之前 **停止 Xray**。
4. 目前的資料庫被重新命名為備份檔 `x-ui.db.backup`（fallback）。
5. 臨時檔被移動到工作資料庫的位置，執行結構初始化與遷移，接著進行 inbound 遷移。
6. **若任何步驟以錯誤結束** —— 執行回滾：從 `x-ui.db.backup` 還原先前的資料庫，並在舊資料上重新啟動 Xray。
7. 成功時刪除 fallback 檔案，並在還原後的資料上 **自動重新啟動 Xray**。

依結果而定的介面訊息：

| 結果 | 文字 |
|-----------|-------|
| 成功 | 「資料庫已成功匯入」 |
| 匯入錯誤 | 「匯入資料庫時發生錯誤」 |
| 檔案讀取錯誤 | 「讀取資料庫時發生錯誤」 |

> 還原會完全取代目前的資料。由於 Xray 在過程中會短暫停止，匯入期間現有的用戶端連線會被中斷。

#### 引擎之間的遷移檔案（SQLite ⇄ PostgreSQL）

除了一般備份之外，還有 **「下載遷移檔案」** 功能（`Download Migration`，請求 `GET /panel/api/server/getMigration`）。它會生成一個可攜帶的檔案，用於轉移到另一種資料庫引擎：

| 目前引擎 | 下載的內容 | 檔案名稱 | 用途 |
|----------------|-----------------|-----------|------------|
| SQLite | 可攜帶的 SQL 傾印（文字） | `x-ui.dump` | 將您的資料植入 PostgreSQL |
| PostgreSQL | 由 PostgreSQL 資料組建的 SQLite 資料庫 | `x-ui.db` | 將面板切換回 SQLite |

提示：
- 在 SQLite 上：「點擊以下載您 SQLite 資料庫的可攜帶 .dump 匯出檔（SQL 文字）。」
- 在 PostgreSQL 上：「點擊以下載由您的 PostgreSQL 資料組建、可用於在 SQLite 上執行面板的 SQLite 資料庫（.db）。」

SQLite 的 `.db ⇄ .dump` 轉換也可從 CLI 透過 `x-ui migrateDB [file]` 命令完成（見章節 16.7）。

#### 透過 Telegram 機器人備份

若已設定 Telegram 機器人（見通知相關章節），它能將備份直接傳送到管理員的聊天中。透過 Telegram 的備份包含 **兩個檔案**：資料庫本身（`x-ui.db`，在 PostgreSQL 上則是 `x-ui.dump`）以及 Xray 的設定 `config.json`。訊息前會有一行「🗄 備份時間：…」。

在 Telegram 中取得備份有兩種方式：

1. **依請求。** 機器人選單中的 **「📂 資料庫備份」** 按鈕 —— 機器人會立即將檔案傳送到目前的聊天中。
2. **隨報告自動傳送。** 機器人設定中有一個開關 **「資料庫備份」**（`Database Backup`），說明為「傳送附帶資料庫備份檔案的通知」。啟用後，每次週期性報告發送時，機器人會在報告之後將備份傳送給所有管理員。報告發送的週期由機器人的 cron 排程決定（見章節 16.6）。在檔案之間與管理員之間，機器人會稍作暫停，以免超出 Telegram 的限制。

> 透過機器人的備份只有在機器人正在執行時才會傳送；在 PostgreSQL 上還需要伺服器上有 `pg_dump`。

### 16.2. 檢視日誌

面板有兩個獨立的日誌檢視工具，兩者都從「儀表板」上的 **「日誌」** 分頁開啟。每個視窗都能重新整理（標題列中的「重新整理」圖示）並將顯示的內容下載為 `x-ui.log` 檔案（帶下載圖示的按鈕）。

#### 面板日誌（應用程式 / syslog）

面板日誌視窗（`POST /panel/api/server/logs/{count}`）。控制項：

| 元素 | 預設值 | 說明 |
|---------|------------------------|----------|
| 行數 | `20` | 下拉清單：10 / 20 / 50 / 100 / 500 |
| 等級 | `Info` | 最低等級：Debug / Info / Notice / Warning / Error |
| SysLog（勾選框） | 關閉 | 從何處取得日誌：應用程式緩衝區或系統日誌 |

行為取決於 **SysLog** 勾選框：

- **關閉（預設）：** 日誌取自面板內部的環形緩衝區，並依所選等級過濾。記錄會顯示其等級（DEBUG / INFO / NOTICE / WARNING / ERROR）與來源：`X-UI:` —— 面板本身的訊息，`XRAY:` —— 轉發的 Xray 訊息。
- **開啟：** 面板在伺服器上執行 `journalctl -u x-ui --no-pager -n <count> -p <level>`，也就是顯示 `x-ui` 服務的系統日誌。允許的行數為 1 到 10000；等級接受 syslog 值（`emerg/0`、`alert/1`、`crit/2`、`err/3`、`warning/4`、`notice/5`、`info/6`、`debug/7`）。在 Windows 上不支援 SysLog 模式 —— 會顯示警告，提示需取消勾選並改用應用程式日誌。若 `systemd`/服務不可用，則會出現 `journalctl` 啟動錯誤的訊息。

**範例：從伺服器主控台取得同樣的日誌。** 當面板不可用時（例如無法啟動），可直接讀取系統日誌 —— 這正是面板在 SysLog 模式下執行的命令：

```bash
# warning 等級及以上的最後 100 行
journalctl -u x-ui --no-pager -n 100 -p warning

# 即時追蹤日誌
journalctl -u x-ui -f
```

> 此視窗中的等級過濾的是 **輸出**。究竟有哪個最低等級會被寫入主控台/syslog，由面板的日誌等級決定（環境變數，預設 `Info`；寫入檔案時面板一律以 `DEBUG` 等級記錄）。

#### Xray 日誌（存取記錄）

Xray 存取記錄（access log）有獨立的視窗（`POST /panel/api/server/xraylogs/{count}`）。它會解析 Xray 存取記錄的各行，並以表格顯示：**Date、From、To、Inbound、Outbound、Email**。

| 元素 | 預設值 | 說明 |
|---------|------------------------|----------|
| 行數 | `20` | 10 / 20 / 50 / 100 / 500 |
| **過濾器** | 空 | 依子字串進行文字搜尋（按 Enter 套用） |
| **Direct**（勾選框） | 開啟 | 顯示直連連線（透過 freedom-outbound 的流量） |
| **Blocked**（勾選框） | 開啟 | 顯示被封鎖的連線（流向 blackhole-outbound 的流量） |
| **Proxy**（勾選框） | 開啟 | 顯示經代理的流量 |

事件類型依日誌行中出站連線的標籤自動判定：對應到 freedom 標籤 →「DIRECT」（綠色），blackhole →「BLOCKED」（紅色），其餘一律 →「PROXY」（藍色）。`api -> api` 的行與空白行會被略過。

> 為了讓此視窗顯示記錄，Xray 必須啟用 **存取記錄** 並指定檔案路徑（非 `none`）—— 見下文。若存取記錄已停用或檔案不可用，視窗會是空的（「No Record...」）。

### 16.3. Xray 日誌的等級與設定

Xray 本身的記錄參數設定於 **「Xray 設定」** 頁面的 **「Log」**（`Log`）區塊，並附有警告：
> 「日誌可能會降低伺服器效能。請僅在需要時才啟用您需要的日誌類型！」

| 欄位 | 翻譯 | 預設值 | 說明 |
|------|---------|------------------------|----------|
| **日誌等級**（`logLevel`） | Log Level | `warning` | Xray 錯誤日誌的詳細程度等級。允許的值：`debug`、`info`、`notice`、`warning`、`error`。提示：「錯誤日誌的記錄等級，指定需要記錄的資訊。」 |
| **存取記錄**（`accessLog`） | Access Log | `none` | 存取記錄檔案的路徑。特殊值 `none` 會停用存取記錄。提示：「存取記錄檔案的路徑。特殊值『none』會停用存取記錄。」 |
| **錯誤日誌**（`errorLog`） | Error Log | 空（預設路徑） | 錯誤日誌檔案的路徑；`none` 會停用它們。提示：「錯誤日誌檔案的路徑。特殊值『none』會停用錯誤日誌。」 |
| **DNS 日誌**（`dnsLog`） | DNS Log | `false`（關閉） | 啟用 DNS 查詢的記錄。提示：「啟用 DNS 查詢日誌」。 |
| **位址遮罩**（`maskAddress`） | Mask Address | 空（關閉） | 啟用後，日誌中的真實 IP 位址會自動替換為遮罩位址。提示：「啟用後，日誌中的真實 IP 位址會被替換為遮罩位址。」 |

> 由於預設 **「存取記錄」= `none`**，因此「Xray 日誌」視窗（章節 16.2）一開始是空的。為了讓它運作，請在此處指定存取記錄的路徑並重新啟動 Xray。

> 請注意：空的存取記錄只影響此視窗。「儀表板」上的線上用戶端清單以及用戶端表單中的 IP 數量限制 **不依賴** 存取記錄 —— 面板透過 Xray 核心的 online-stats API（連線統計）判定線上用戶端並計算其 IP 位址。在沒有此 API 的舊版核心上，面板會自動退回到舊方式（讀取存取記錄），此時 IP 限制仍然需要此處的存取記錄路徑。

> **IP 數量限制與 fail2ban。** 用戶端的 IP 數量限制本身（用戶端表單以及批次新增時的「IP Limit」欄位）只有在伺服器安裝了 **fail2ban** 時才會在伺服器上套用 —— 正是它封禁超出限制的位址。面板會檢查 fail2ban 是否存在（`GET /panel/api/server/fail2banStatus`）；若不存在，「IP Limit」欄位會變為不可用並附帶說明提示（在 Windows 上 —— 以另一則訊息），而先前在這類伺服器上設定的限制會自動歸零，因為它們本來就不生效。fail2ban 的封鎖同時涵蓋 TCP 與 UDP。在一般伺服器上，fail2ban 現在會在安裝與更新面板時自動安裝（見章節 16.5）。

**範例：能讓「Xray 日誌」視窗開始顯示記錄的 `log` 區塊。** 在 Xray 的 JSON 設定中看起來如下：

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

關鍵在於將 `"access": "none"` 替換為檔案路徑（例如 `"./access.log"`）。儲存後重新啟動 Xray，「Xray 日誌」視窗中的表格便會填滿各行記錄。

### 16.4. 管理 Xray：停止與重新啟動

Xray 的狀態從「儀表板」上的 Xray 卡片進行管理。目前狀態以下列其中一個值顯示：**執行中**（`Running`）、**已停止**（`Stopped`）、**未知**（`Unknown`）、**錯誤**（`Error`）。發生錯誤時可看到彈出提示「啟動 Xray 時發生錯誤」。

| 按鈕 | 翻譯 | 端點 | 動作 |
|--------|---------|----------|------|
| **停止** | `Stop` | `POST /panel/api/server/stopXrayService` | 停止 Xray 程序。成功時 —— 顯示警告通知「Xray service has been stopped」。 |
| **重新啟動** | `Restart` | `POST /panel/api/server/restartXrayService` | 套用目前設定重新啟動（或啟動）Xray。成功時 —— 顯示通知「Xray service has been restarted successfully」。 |

任一操作之後，面板會透過 WebSocket 廣播新狀態，因此「儀表板」上的狀態無需重新載入頁面即會更新。若操作以錯誤結束，Xray 狀態會變為「錯誤」，且錯誤文字會進入通知中。

> 除了手動重新啟動之外，面板自身也會檢查是否需要重新啟動 Xray（背景任務，每 30 秒）以及程序是否當掉（每秒檢查）—— 見章節 16.6。

### 16.5. 重新啟動與更新面板

#### 重新啟動面板

在 **「面板設定」** 頁面上有 **「重新啟動面板」** 動作（`Restart Panel`，`POST /panel/api/setting/restartPanel`）。確認後面板會 **在 3 秒後** 重新啟動。

訊息：
- 確認：「您確定要重新啟動面板嗎？請確認，重新啟動將在 3 秒後進行。若面板變為不可用，請檢查伺服器日誌。」
- 成功：「面板已成功重新啟動」。

技術上，在 Linux 上的重新啟動是透過向面板程序傳送 `SIGHUP` 訊號（或透過已註冊的掛鉤）完成。在 Windows 上不支援傳送 `SIGHUP`。

#### 面板自我更新（Update Panel）

「儀表板」上有 **「更新面板」** 功能（`Update Panel`）—— 直接從 Web 介面將 3X-UI 更新到最新版本。

更新前，面板會比對版本（`GET /panel/api/server/getPanelUpdateInfo`），向 GitHub 請求最新的 3x-ui 版本：

| 欄位 | 翻譯 |
|------|---------|
| **目前面板版本** | Current panel version |
| **最新面板版本** | Latest panel version |
| **面板已是最新** /「已更新」 | Panel is up to date / Up to date —— 在沒有新版本時顯示 |

啟動更新 —— `POST /panel/api/server/updatePanel`。確認對話框：
- 「您確定要更新面板嗎？」
- 「這將把 3X-UI 更新到版本 #version# 並重新啟動面板服務。」

啟動後 —— 彈出訊息「面板更新已開始」（`Panel update started`）；版本檢查失敗時 —— 「面板更新檢查失敗」（`Panel update check failed`）。

**伺服器上發生的動作：** 自我更新 **僅在 Linux 上** 受支援（在其他作業系統上會回傳錯誤「panel web update is supported only on Linux installations」）。面板從 GitHub 下載官方腳本 `update.sh`（`raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh`）並在獨立程序中執行它：優先透過 `systemd-run` 在獨立的 unit 中（`x-ui-web-update-<timestamp>`），而在沒有 systemd 時 —— 作為獨立的分離程序。完成後腳本會更新元件並重新啟動面板服務。執行需要 `bash`。

若在更新過程中腳本生成了新的隨機 Web 面板基礎路徑（Web Base Path），`x-ui` 服務會自動重新啟動，讓新路徑立即生效。（若不重新啟動，伺服器會繼續提供舊路徑，而介面卻顯示新路徑，新位址在手動重新啟動前將不可用。）

> 在節點（nodes）上，同一個 3x-ui 的面板會透過 `POST /panel/api/nodes/updatePanel` 集中更新 —— 見節點相關章節。

#### 自動安裝 fail2ban

為了讓用戶端的 IP 數量限制（章節 16.3）開箱即用，現在在一般伺服器上安裝與更新面板時會自動安裝並設定 `fail2ban`（先前只在 Docker 映像中發生）。此行為由環境變數 `XUI_ENABLE_FAIL2BAN` 控制：若變數未設定或等於 `true`，則執行設定。手動執行可透過 `x-ui setup-fail2ban` 命令。fail2ban 設定失敗不會中斷面板的安裝或更新。

#### 在僅 IPv6 主機上的安裝與更新

`install.sh` 與 `update.sh` 腳本現在能在僅有 IPv6 的伺服器上正確運作：下載版本、`x-ui.sh` 腳本與服務檔不再強制使用 IPv4（`curl -4`），而是採用可用的協定。因此面板也可以在沒有 IPv4 位址的主機上安裝與更新。

#### 透過 `XUI_PORT` 變數覆寫面板連接埠

Web 面板的監聽連接埠可透過環境變數 `XUI_PORT` 覆寫 —— 它僅在目前程序的執行期間生效，且 **不會變更** 資料庫中儲存的 `webPort` 值。允許的值為 `1` 到 `65535`；空白、無效或超出範圍的值會被忽略（改用 `webPort`），並在日誌中產生警告。這在部署時很方便，尤其是在 Docker 中：使用 bridge 網路時，容器發布的連接埠必須與 `XUI_PORT` 一致 —— 例如 `XUI_PORT=8080` 與 `ports: "8080:8080"`。

#### 更新與切換 Xray-core 版本

同樣在「儀表板」上，可以獨立於面板來管理 Xray-core 的版本。

- **Xray 更新**（`Xray Updates`） / **版本選擇**（`Version`）—— 可用版本的下拉清單。提示：「選擇所需的版本」與警告「重要：舊版本可能不支援目前的設定」。
- 安裝/變更版本 —— `POST /panel/api/server/installXray/{version}`。對話框：「切換 Xray 版本」/「您確定要變更 Xray 版本嗎？」。成功時 —— 「Xray 已成功更新」。

**範例：透過 API 請求變更 Xray-core 版本。** 版本以 XTLS/Xray-core 的版本標籤指定（帶 `v` 前綴）。例如，切換到 `v1.8.24`：

```bash
curl -s -b cookies.txt -X POST \
     https://panel.example.com:2053/panel/api/server/installXray/v1.8.24
```

（`cookies.txt` —— 來自章節 16.1 範例的 cookie 檔案。）安裝後 Xray 會以所選版本自動重新啟動。

在伺服器上，變更版本時 Xray 會先停止，從 GitHub（XTLS/Xray-core）下載所需版本的封存檔，解壓並替換二進位檔，之後 Xray 會以封存檔/二進位檔的校驗大小檢查重新啟動。

### 16.6. 週期性任務（cron）

面板在啟動時會註冊一系列背景任務。它們的排程是固定的（在 UI 中不可設定，Telegram 報告排程與 LDAP 同步除外）。以下是與運維相關的任務。

| 任務 | 排程 | 用途 |
|--------|-----------|------------|
| 檢查 Xray 是否運作 | 每 1 秒 | 監控 Xray 程序是否在執行 |
| 檢查是否需要重新啟動 Xray | 每 30 秒 | 若設定被標記為已變更則重新啟動 |
| 收集 Xray 流量 | 每 5 秒（啟動後 5 秒開始） | 計算 inbound/用戶端的流量 |
| 檢查用戶端 IP | 每 10 秒 | 依日誌監控 IP 限制 |
| 節點的 Heartbeat 與流量同步 | 每 5 秒 | 與節點（nodes）交換資料 |
| **清理日誌** | **每日**（`@daily`） | 清理 IP-limit 日誌與持久化的 access-log，將目前日誌輪替到 `*.prev.log` |
| **依週期重設流量** | `@hourly`、`@daily`、`@weekly`、`@monthly` | 重設那些設定了對應自動重設週期的 inbound（及其用戶端）的流量計數 |
| Telegram 報告 | 在機器人設定中指定（預設 `@daily`） | 向管理員發送報告；啟用該選項時 —— 附帶資料庫備份（章節 16.1） |
| 重設 Telegram hash 儲存 | 每 2 分鐘 | 僅在啟用機器人時 |
| 為 Telegram 監控 CPU 負載 | 每 10 秒 | 僅在設定了 CPU 閾值 > 0 時 |

此外：

- **週期性流量重設** 只對那些選擇了對應自動重設模式（每小時/每日/每週/每月）的 inbound 觸發。該任務會重設 inbound 本身及其所有用戶端的流量。
- **到期與耗盡檢查。** 用戶端到期時的停用以及流量限制耗盡時的停用是在流量計算的範疇內執行的：`expiry_time` 已到期或流量已耗盡的用戶端會被標記並停用，必要時會計算下一個期限（適用於循環限制與「自首次使用起計算」模式）。在「儀表板」與各清單中，這會以「已到期」/「已耗盡」/「即將結束」等狀態反映出來。
- **自動備份到 Telegram** 是報告任務的副作用，並沒有專門僅用於備份的 cron 排程。因此自動備份的頻率等於機器人報告的頻率。

### 16.7. 主控台選單與 CLI（`x-ui`）

在伺服器上，面板透過 `x-ui` 命令管理。不帶參數時會開啟互動式選單「3X-UI Panel Management Script」；帶參數時則執行特定的子命令。與運維相關的選單項目：

| 選單編號 | 項目 | 動作 |
|----------|-------|------|
| 1 | Install | 安裝面板（下載並執行 `install.sh`） |
| 2 | Update | 將所有 x-ui 元件更新到最新版本而不遺失資料；之後 —— 自動重新啟動 |
| 3 | Update Menu | 僅更新 `x-ui` 選單腳本本身 |
| 4 | Legacy Version | 依輸入的編號安裝指定的（舊）面板版本（例如 `2.4.0`） |
| 5 | Uninstall | 完整移除面板與 Xray（見 16.8） |
| 6 | Reset Username & Password | 重設管理員的帳號/密碼 |
| 7 | Reset Web Base Path | 重設 Web 面板的基礎路徑 |
| 8 | Reset Settings | 將設定重設為預設值 |
| 9 | Change Port | 變更面板連接埠 |
| 10 | View Current Settings | 檢視目前設定 |
| 11–13 | Start / Stop / Restart | 啟動、停止、重新啟動面板服務 |
| 14 | Restart Xray | 僅重新啟動 Xray |
| 15 | Check Status | 服務的目前狀態 |
| 16 | Logs Management | 檢視與清理日誌（見下文） |
| 17–18 | Enable / Disable Autostart | 啟用/停用作業系統啟動時的服務自動啟動 |
| 25 | Update Geo Files | 更新地理檔案（GeoIP/GeoSite） |
| 27 | PostgreSQL Management | 管理 PostgreSQL |

#### CLI 中的日誌管理（項目 16）

在「Logs Management」子選單中：
- **Debug Log** —— 串流檢視服務日誌：`journalctl -u x-ui -e --no-pager -f -p debug`（在 Alpine 上 —— 以 `grep` 搜尋 `/var/log/messages`）。
- **Clear All logs** —— 清理系統日誌：`journalctl --rotate` + `journalctl --vacuum-time=1s`，之後服務會重新啟動。（在 Alpine 上不可用。）

#### `x-ui` 的直接子命令

所有可用的子命令：

| 命令 | 說明 |
|---------|----------|
| `x-ui` | 開啟管理選單 |
| `x-ui start` | 啟動面板 |
| `x-ui stop` | 停止面板 |
| `x-ui restart` | 重新啟動面板 |
| `x-ui restart-xray` | 重新啟動 Xray |
| `x-ui status` | 目前狀態 |
| `x-ui settings` | 顯示目前設定 |
| `x-ui enable` | 啟用作業系統啟動時的自動啟動 |
| `x-ui disable` | 停用自動啟動 |
| `x-ui log` | 檢視日誌 |
| `x-ui banlog` | 檢視 Fail2ban 封禁日誌 |
| `x-ui setup-fail2ban` | 安裝並設定用於 IP 限制的 fail2ban（見 16.5） |
| `x-ui update` | 更新面板 |
| `x-ui update-all-geofiles` | 更新所有地理檔案（之後重新啟動） |
| `x-ui migrateDB [file]` | 轉換資料庫 `.db ⇄ .dump`（SQLite） |
| `x-ui legacy` | 安裝舊版本 |
| `x-ui install` | 安裝面板 |
| `x-ui uninstall` | 移除面板 |

> `x-ui update` 命令會下載並執行官方的 `update.sh`（與章節 16.5 的 Web 更新相同），並請求確認：「This function will update all x-ui components to the latest version, and the data will not be lost.」完成後面板會自動重新啟動。

> **`setting` 子命令中的 `-webCert` / `-webCertKey` 旗標。** Web 面板的憑證與私鑰路徑可直接在 `x-ui setting -webCert <路徑> -webCertKey <路徑>` 子命令中指定 —— 指定其中任一旗標都會儲存對應的路徑（如同獨立的 `cert` 子命令），且面板會立即切換到 HTTPS。

#### 透過 CLI 取得 API 權杖

透過 CLI 取得 API 權杖的命令（選單項目/`x-ui` 命令）不會顯示先前發放的權杖。API 權杖只以雜湊形式儲存，因此無法取得現有權杖的明文。若已設定權杖，命令會告知其數量，建議在面板中管理權杖（**Settings → API Tokens**，見 API 權杖相關章節），並立即生成一個名稱形如 `cli-fallback-<timestamp>` 的 **新備用權杖** 並輸出它，讓 CLI 在不進入介面的情況下仍然有用。

### 16.8. 移除面板

移除從 CLI 執行 —— 選單項目 **5（Uninstall）** 或命令 `x-ui uninstall`。移除前會請求確認（預設為「否」）：「Are you sure you want to uninstall the panel? xray will also uninstalled!」。

確認後腳本會：
1. 停止服務並停用其自動啟動（`systemctl stop/disable x-ui`，在 Alpine 上 —— `rc-service`/`rc-update`），刪除服務的 unit 檔並重新載入 systemd 設定。
2. 刪除資料與應用程式目錄（`/etc/x-ui/`、安裝目錄）以及服務的 env 檔（`/etc/default/x-ui`、`/etc/conf.d/x-ui` 或 `/etc/sysconfig/x-ui` —— 視發行版而定）。
3. 刪除 `x-ui` 腳本本身，並輸出訊息「Uninstalled Successfully.」以及重新安裝的命令。

> 移除無法復原：面板連同 Xray 與所有資料（包括資料庫）一併刪除。若資料日後可能需要，請事先匯出資料庫（章節 16.1）。

### 16.9. `x-ui migrateDB` 命令

自 3.3.0 版本起，管理腳本 `x-ui.sh` 新增了 `migrateDB` 子命令 —— 它是內建二進位檔 `x-ui`（`x-ui migrate-db`）的封裝，用於在兩種格式之間轉換 SQLite 面板資料庫：二進位的 `.db` 與可攜帶的文字傾印 `.dump`（一般的 SQL 文字）。

#### 此命令的作用

該命令可在兩個方向運作，且方向由輸入檔案 **自動** 判定：

| 方向 | 名稱 | 發生的動作 |
|---|---|---|
| `.db → .dump` | dump（匯出） | 二進位的 SQLite 資料庫匯出為文字 SQL 檔 |
| `.dump → .db` | restore（還原） | 從文字 SQL 檔重新組建二進位的 SQLite 資料庫 |

在底層，腳本會呼叫面板二進位檔：
- 匯出：`x-ui migrate-db --src <輸入> --dump <輸出>`
- 還原：`x-ui migrate-db --restore <輸入> --out <輸出>`

#### 呼叫語法

```
x-ui migrateDB [file.db|file.dump] [output]
```

- **`[file.db|file.dump]`** —— 輸入檔案（第一個參數）。若未指定，則採用面板預設安裝的資料庫：`/etc/x-ui/x-ui.db`。
- **`[output]`** —— 輸出檔案的路徑（第二個參數）。可省略：未指定時會在輸入檔案旁自動選擇名稱（見下文）。

範例：

```
x-ui migrateDB                              # 匯出 /etc/x-ui/x-ui.db -> /etc/x-ui/x-ui.dump
x-ui migrateDB /etc/x-ui/x-ui.db backup.dump
x-ui migrateDB backup.dump restored.db      # 從傾印組建 .db
```

#### 方向如何判定

腳本會檢視輸入檔案的副檔名：
- `*.db`、`*.sqlite`、`*.sqlite3` → **dump** 模式（匯出為文字）；
- `*.dump`、`*.sql` → **restore** 模式（組建資料庫）。

若副檔名無法辨識，腳本會讀取檔案的前 16 個位元組：簽章 `SQLite format 3` 代表二進位資料庫（dump 模式），否則該檔案被視為傾印（restore 模式）。

未指定第二個參數時的輸出檔案名稱：
- 匯出時 —— 與輸入相同的名稱，副檔名為 `.dump`；
- 還原時 —— 相同名稱，副檔名為 `.db`。

#### 保護性檢查與行為

- **二進位檔是否存在。** 若找不到 `x-ui` 二進位檔或它不可執行 —— 會輸出錯誤「x-ui binary not found … Is the panel installed?」。
- **建置中是否支援此功能。** 腳本會檢查二進位檔是否會 `migrate-db --dump/--restore`（透過 `x-ui migrate-db -h`）。若否 —— 會建議先以 `x-ui update` 命令更新面板。
- **輸入檔案是否存在。** 輸入檔案不存在時會印出錯誤以及呼叫語法那一行。
- **覆寫輸出。** 若輸出檔案已存在，會請求確認（預設為「否」）；未確認則操作取消。還原時，舊的輸出檔案會被預先刪除。
- **保護「使用中」的資料庫。** 還原到預設資料庫 `/etc/x-ui/x-ui.db` 時，若面板正在執行，操作會被拒絕，並要求先停止面板（`x-ui stop`）或選擇其他輸出路徑。這可防止覆寫正在運作的服務的工作資料庫。
- 資料庫組建失敗時，未寫完的輸出檔案會被刪除。

#### 為什麼需要它

- **備份。** 文字 `.dump` 是人類可讀的，便於儲存在版本控制系統中，也便於差異化檢視資料庫內容。
- **轉移。** 傾印可在機器之間轉移，且對 SQLite 檔案格式版本的差異具有韌性 —— 在新伺服器上可從中組建出可運作的 `.db`。
- **診斷。** 即使手邊沒有 SQLite 工具，也能從 `.dump` 用肉眼檢視面板的結構與資料。

#### 互動模式

除了直接呼叫之外，轉換也可從互動式選單使用。在 PostgreSQL 子選單（`x-ui` → PostgreSQL 操作區段）中有一個項目 **9. Convert SQLite `.db <-> .dump`**：它會詢問輸入檔案的路徑（預設 `/etc/x-ui/x-ui.db`）與輸出檔案的路徑（可留空以自動命名），而方向如同 CLI 模式一樣自動判定。

---

*本文件依 3X-UI 原始碼編寫。若您版本中某個介面項目有所不同 —— 以面板的行為與 UI 中的提示為準。*

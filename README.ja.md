# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 日本語 · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

パネル [3x-ui](https://github.com/MHSanaei/3x-ui) のユーザーマニュアル — パネル **v3.4.0** 向けに書かれた総合ユーザーガイド。

> **読み取り専用ミラー。** この GitHub リポジトリは一方向ミラーです — マニュアルのソースはプライベート GitLab に置かれており、自動的にここへプッシュされるため、常に最新の状態です。誤りや不正確な記述を見つけた場合は、[Issue を開いてください](https://github.com/yukh975/3X-UI-Manual/issues)。**プルリクエストは受け付けていません**（自動的にクローズされます） — 修正はソース側で行われます。

## 目次

| ファイル | 言語 | 形式 |
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

## 3.4.0 の新機能

このセクションでは、パネルユーザーに見える **3.4.0** の 3.3.1 からの変更点を、マニュアルのセクションごとに簡潔にまとめています。各機能の詳細は、該当するセクションをご覧ください。

### 3. 概要 / ダッシュボード
- **システムメトリクス履歴：新しい集計間隔 12h/24h/48h** — システムメトリクス履歴ウィンドウの平均化間隔に 12h、24h、48h が追加されました。これにより、グラフ（CPU、RAM、トラフィック、パケット、接続数、ディスク、オンライン、負荷）を最大 2 日間分表示できるようになりました。

### 4. Inbounds：作成と共通パラメータ
- **Inbound：Xray API の予約済みポートとの競合警告** — inbound の作成または変更時、内部 Xray API の予約済みポート（デフォルトでは 127.0.0.1 の 62789）を使用できなくなりました。そのポートの loopback 上のローカル TCP inbound はポート競合エラーで拒否されます。ノード（nodes）にはこの制限は適用されません。ノードには独自の Xray があります。
- **Tunnel/TProxy：security キーを含まない streamSettings の受け入れ** — streamSettings に security ブロックがない tunnel/TProxy タイプの inbound が、バリデーションエラーなしで開いて保存できるようになりました。
- **Inbounds：リストに Speed（リアルタイム速度）列を追加** — inbound リストに、各 inbound の現在のトラフィック速度（送信/受信）を示す Speed 列が追加されました。

### 5. プロトコル
- **Shadowsocks-2022：キーサイズが異なるメソッドへの変更時にクライアント PSK を再生成** — Shadowsocks-2022 で、暗号化メソッドを異なるキーサイズのメソッド（たとえば aes-256 と aes-128 の間）に変更すると、inbound 保存時にクライアント PSK が新しい長さに合わせて自動的に再生成されるようになりました。結果として、影響を受けるクライアントは再度サブスクリプションを取得する必要があります（古いリンクは動作しなくなります）。
- **WireGuard：workers フィールドを削除** — WireGuard（inbound および outbound）のフォームから workers フィールドが削除されました。xray-core v26.6.22 はこのフィールドを使用しなくなりました。以前保存した設定は変更なく動作し続けます。フィールドは単に無視されます。
- **VLESS+XHTTP：リンクとサブスクリプションで xtls-rprx-vision フロー** — XHTTP 上の VLESS で、xtls-rprx-vision フローがリンクとサブスクリプション（XHTTP+REALITY や Clash/Mihomo 形式を含む）に正しく反映されるようになりました。以前はパネルがフローを保存していましたが、クライアントは vision なしの設定を受け取っていました。

### 6. トランスポート（Stream Settings）
- **XHTTP：sessionID フィールドの名称変更 + Session ID Table / Length** — XHTTP トランスポートのセッションフィールドが名称変更されました。Session ID Placement と Session ID Key（以前は Session Placement / Session Key）。2 つのパラメータが追加されました。Session ID Table はセッション識別子を生成するための文字セットです。定義済みのもの（ALPHABET、Base62、hex、number など）から選択するか、任意の ASCII 文字列を入力できます。空の場合は xray-core のデフォルト値が使用されます。Session ID Length は生成される識別子の長さまたは範囲（例：8-16）です。Session ID Table が設定されている場合にのみ有効で、最小値は 0 より大きくなければなりません。以前保存した inbound は自動的に移行されます。
- **Inbound：CDN/リレー経由の実際の IP を特定するための Real client IP プリセット** — inbound のソケット設定（sockopt）に Real client IP の選択が追加されました。トラフィックが CDN やリレーを経由する場合に実際の訪問者 IP を特定するためのプリセットです（そうしないと仲介者のアドレスが記録されます）。利用可能な 3 つのオプション：Off / direct（処理なし）、Cloudflare CDN（X-Forwarded-For を信頼）、L4 relay / Spectrum (PROXY)（PROXY プロトコルヘッダーを受け入れる）。プリセットは相互排他的で、選択したトランスポートがサポートしていない場合に警告が表示されます。これらのフィールドはサブスクリプションでクライアントに送信されることはありません。
- **gRPC：Trusted X-Forwarded-For ヘッダーが考慮されるようになった** — Trusted X-Forwarded-For ヘッダーが gRPC トランスポートでも考慮されるようになりました（以前は WebSocket、HTTPUpgrade、XHTTP のみ）。gRPC inbound では、パネルはサポートされていないヘッダーに関する警告を表示しなくなりました。

### 7. 接続セキュリティ：TLS、XTLS、REALITY
- **TLS：新しいフィールド Verify Peer Cert By Name、Curve Preferences、Master Key Log、ECH Sockopt** — Verify Peer Cert By Name は、クライアントが SNI の代わりにサーバー証明書を検証する名前（カンマ区切り）です。削除された allowInsecure の現代的な代替で、リンクとサブスクリプションに含まれますが、サーバーには書き込まれません。Curve Preferences は TLS キー交換曲線の制限と優先順位です（例：X25519MLKEM768、X25519）。空の場合はデフォルト値が使用されます。Master Key Log は TLS キーを記録するためのパスです（SSLKEYLOGFILE 形式、Wireshark でのデバッグ用）。本番環境では空のままにしてください。ECH Sockopt は ECH 設定を取得するためのソケットパラメータです（dialerProxy、Domain Strategy、TCP Fast Open、Multipath TCP）。
- **REALITY：フォールバック速度制限（Limit Fallback）と Master Key Log** — 各方向（Upload と Download）に設定できます：After Bytes — 制限を開始する前にフルスピードで通過させるバイト数（0 = 最初のバイトから制限）、Bytes Per Sec — フォールバックトラフィックの速度上限（プローブがサーバーを無料チャンネルとして使用しないように）（0 = 制限なし、この方向を無効にする）、Burst Bytes Per Sec — 一時的なスパイク用のバースト容量。また、Master Key Log フィールド（デバッグ用 SSLKEYLOGFILE ファイルへのパス）も追加されました。
- **TLS：inbound 証明書と SNI による Pinned Peer Cert SHA-256 の自動入力ボタン** — Pinned Peer Cert SHA-256 フィールドの横に、以前のランダムハッシュボタンの代わりに 2 つの自動入力ボタンが追加されました。1 つ目は inbound 自身の証明書の SHA-256 を挿入します。2 つ目は、指定された SNI への TLS 接続を実行してライブサーバー証明書のハッシュを取得します（serverName を入力する必要があります）。取得したハッシュはフィールドに追加（カンマ区切り）され、クライアントの証明書ピン留めのためにリンクに含まれます。
- **TLS：新しい inbound 証明書に対してデフォルトで OCSP ステープリングを無効化** — 新しい inbound では、OCSP ステープリングがデフォルトで無効（間隔 0）になりました。これにより、OCSP レスポンダーのない証明書（Let's Encrypt など）での xray ログのエラーが解消されます。フィールドは残っており、ステープリングをサポートする証明書に対して有効にできます。
- **REALITY：dest フィールドの互換性（target のエイリアス）** — 以前のパネルバージョン、API、または外部ツールによって dest フィールドで作成された REALITY inbound が正しく読み込まれるようになりました。dest の値が Target フィールドに設定されます。以前は Target が空になり、再保存すると REALITY が壊れていました。

### 8. クライアント
- **クライアントエディタの「Links」タブ（外部リンクとサブスクリプション）** — **Add External Link** ボタンで外部 share リンク（`vless://`、`vmess://`、`trojan://`、`ss://`、`hysteria2://`、`wireguard://`）を追加し、**Add External Subscription** ボタンでリモートサブスクリプション URL を追加できます。これらはすべて、このクライアントのサブスクリプション出力（raw、JSON、Clash 形式）に組み込まれます。リンクはそのまま追加され、リモートサブスクリプションはパネルが定期的にダウンロードして設定を統合します。
- **「IP 制限」フィールドは Fail2ban なしでは無効** — **IP 制限**フィールドは、Fail2ban がインストールされて有効な場合にのみ機能します。Fail2ban がインストールされていない場合（または Windows システムの場合、またはサーバーで機能が無効な場合）、クライアントエディタのフィールドはロックされ、ホバー時に `x-ui` bash メニューから Fail2ban をインストールするよう促すツールチップが表示されます。パネル更新時に、Fail2ban のないサーバーのクライアントの保存済み IP 制限はリセットされます（どのみち適用されていなかったため）。
- **紐付けのないクライアントの削除、クライアントのエクスポートとインポート** — **クライアント**ページの**その他**メニューに 3 つの操作が追加されました。**クライアントのエクスポート**は、すべてのクライアントの JSON リスト（`{client, inboundIds}` 形式）をコピーおよびダウンロードボタン付きで表示します（`clients-export.json`）。**クライアントのインポート**は同じ形式の JSON を受け取ります。紐付きクライアントは inbound に再作成・紐付けされ、紐付けなしクライアントは個別レコードとして復元され、既存のメールは上書きされません（スキップとしてマークされます）。**紐付けのないクライアントを削除**は、どの inbound にも紐付けられていないすべてのクライアントを、そのトラフィック、IP ログ、外部リンクとともに削除します。この操作は元に戻せません。
- **クライアントの IP ログ：接続時刻とノード名** — クライアントの IP ログ（「IP 制限」フィールド横の表示ボタンおよび「クライアント情報」カード内）の各エントリに、IP アドレスに加えて最終アクセス時刻と接続が記録されたノードのラベル（`@ ノード名`）が表示されるようになりました。マルチパネル設定では、クライアントがどのノードを通じて接続したかが確認できます。
- **単一エディタでクライアントのグループラベルをリセット** — クライアント単一エディタで**グループ**フィールドをクリアして保存すると、グループラベルが正しく削除されるようになりました。以前は、再保存するまでクライアントが以前のグループ下に表示され続けることがありました。
- **クライアントリストが自動更新（バックグラウンドポーリング）** — クライアントリストが自動的に更新されるようになりました。パネルが数秒ごとに現在のページを取得するため、新たに接続したクライアントやソート順の変更が手動更新なしで表示されます。

### 10. サブスクリプション（Subscription）
- **管理された Hosts：ホスト別にサブスクリプションリンクをオーバーライド** — バージョン 3.4.0 で Hosts セクション（サイドメニュー項目）が追加されました。各 inbound に対して 1 つ以上の Host エンドポイントを設定でき、inbound 自身のアドレス、ポート、TLS パラメータの代わりにサブスクリプションリンクに挿入されます。CDN やリレーを通じてトラフィックを配布するのに便利です。ホストには、Remark と説明、inbound への紐付け、Address（空の場合は inbound のアドレスを継承）と Port（0 の場合は inbound のポートを継承）、Security パラメータ（same/tls/none/reality）、Host ヘッダー、Path、Mux、Sockopt、Final Mask、サブスクリプション形式からの除外（raw/json/clash）、Clash/mihomo 用パラメータを設定できます。ホストは inbound 内で順序付けられ、一括操作をサポートします。
- **Remark Template が remark モデルコンストラクタを置き換え；変数 {{VAR}}** — 以前のプロフィール名コンストラクタ（Inbound/Email/External Proxy と区切り文字の選択）は「Remark Template」フィールドに置き換えられました。任意の名前形式を記述し、ボタンで変数を挿入できます：クライアント識別（{{EMAIL}}、{{INBOUND}}、{{HOST}}、{{ID}}、{{SUB_ID}}、{{COMMENT}}、{{TELEGRAM_ID}}）、トラフィック（{{TRAFFIC_USED}}、{{TRAFFIC_LEFT}}、{{TRAFFIC_TOTAL}}、{{UP}}、{{DOWN}}、{{USAGE_PERCENTAGE}}）、有効期限/ステータス（{{DAYS_LEFT}}、{{TIME_LEFT}}、{{EXPIRE_DATE}}、{{JALALI_EXPIRE_DATE}}、{{STATUS}}、{{STATUS_EMOJI}}）。変数はサブスクリプション生成時に各クライアントに個別に置換され、プレビューも利用できます。「|」で区切られたセグメントは無制限の値の場合に自動的に非表示になり、使用量と有効期限の情報はクライアントの最初のリンクにのみ表示されます。フィールドを空のままにすると、以前の remark モデルが使用されます。
- **クライアントごとの外部リンクとリモートサブスクリプション（Links タブ）** — 個々のクライアントに外部 share リンク（Add External Link）と外部サブスクリプションアドレス（Add External Subscription）を添付でき、それらがそのクライアントのサブスクリプション（RAW、JSON、Clash 形式）に含まれます。外部サブスクリプションはパネルがダウンロードしてクライアントの設定と統合します。自分の inbound に加えて追加のサーバーをクライアントに提供するのに便利です。
- **Happ：クライアントのサーバー設定を非表示にする（Hide server settings）** — サブスクリプション設定の Happ タブに「Hide server settings」トグルが追加されました。有効にすると、Happ クライアントでサーバーパラメータの表示と変更が隠されます。この設定は Happ クライアントにのみ有効です。
- **ノード名はサブスクリプションのプロフィール名に付加されなくなった** — ノード（Node）名はサブスクリプションのプロフィール名に付加されなくなりました。クライアントアプリには管理者が設定した inbound の remark のみが表示され、「@ノード名」のような内部サフィックスは付きません。
- **remark モデルのラベルが Other → External Proxy に名称変更（その後テンプレートに置き換え）** — 個別のドキュメント化は不要です：remark モデルの「Other」から「External Proxy」への名称変更は、UI からモデルコンストラクタが削除された新しい Remark Template フィールドへの移行に包含されています。
- **サブスクリプションリンクの正確性：SS2022、Shadowrocket、SIP002 obfs、Clash での XHTTP** — 生成されるサブスクリプションリンクの互換性が向上しました：SS2022 のエンコーディング、Shadowrocket のディープリンク、SIP002 形式（obfs-local プラグイン）での Shadowsocks+obfs の出力、Clash/Mihomo サブスクリプションでの XHTTP のフィールド完全性が修正されました。個別の設定は不要で、リンクがクライアントでより正しく認識されるようになります。
- **サブスクリプション remark モデル：「Other」が「External Proxy」に名称変更** — サブスクリプション設定の remark モデルで**「Other」**が**「External Proxy」**（ソース：外部プロキシの remark）に名称変更されました。動作は変わらず、既存の設定は引き続き互換性があります。
- **サブスクリプション：チップをクリックして remark 変数を選択（Remark variable picker）** — Remark Template フィールドの横に、グループ化された変数チップセットが表示されます。変数 {{VAR}} をクリックするとテンプレートに挿入され、ホバー時に説明が表示されます。remark フィールドとホスト名フィールドでは簡略記法も使用できます（シングルブラケット：{DATA_LEFT}、{EXPIRE_DATE}、{PROTOCOL}、{TRANSPORT} など）。パネルが自動的に内部形式 {{...}} に変換します。

### 11. Xray：ルーティング、outbounds、DNS、拡張機能
- **ルーティングと Outbounds がサイドメニューの独立した項目に移動** — このバージョンから、**「Outbounds」**と**「ルーティング」（Routing）**は「Hosts」の直下に独立したサイドメニュー項目として分離され、それぞれ `/outbound` と `/routing` のアドレスを持ちます。以前は、ルーティングは「Xray 設定」サブメニュー内に、outbounds は Xray ページのタブとして開いていました。「Xray 設定」サブメニューには Basic、Balancer、DNS、Advanced Template のみが残ります。`/outbound` と `/routing` への直接リンクとページの再読み込みは期待通りに動作します。
- **ルーティングルールをトグルで有効/無効に切り替え可能** — 個々のルーティングルールを削除せずにトグルで一時的に**無効化**できるようになりました。ルール一覧に**「有効」**列にトグルが、ルールフォームの「有効」フィールドもトグルになっています。無効なルールは最終的な Xray 設定に含まれません。統計サービスルール（`api`）は無効化できません。そのトグルはロックされています。
- **ルーティングルールと outbounds のエクスポートがプレビューモーダルで開く** — ルーティングルールと outbounds の**「エクスポート」**ボタンは、ファイルを直接ダウンロードする代わりに、JSON プレビューと**「コピー」**・**「ダウンロード」**ボタンを含むモーダルウィンドウを開くようになりました。「ルーティング」タブでは「インポート」と「エクスポート」が**「その他」**ドロップダウンメニューにまとめられています（Outbounds タブと同様）。
- **全 outbound テストにサブスクリプションからの outbound も含まれ、direct/dns はテストされなくなった** — 「Outbounds」ページの**「全テスト」**ボタンが、サブスクリプションから取得した outbound（「サブスクリプションから」テーブル）もテストするようになりました。それらの行もテスト結果でハイライト表示されます。一方、`freedom`（「direct」）と `dns` の outbound はどのモードでもテストされなくなりました（これらはプロキシではないため）。これらのテストボタンは利用できず、「全テスト」でもスキップされます。
- **FinalMask：単一の Length/Delay の代わりにフラグメントごとの Lengths/Delays 配列** — fragment マスク（FinalMask）の単一フィールド Length と Delay が、Lengths と Delays のリストに置き換えられました。各セグメントに個別の長さの範囲（例：100-200）とミリ秒単位の遅延（例：10-20 または 0）を設定できます。行の追加と削除が可能で、以前保存された値は自動的に移行されます。
- **loopback outbound：Sniffing ブロックを追加** — loopback タイプの outbound に、inbound と同じパラメータ（有効化、destOverride、Metadata Only、Route Only、除外ドメインリスト）を持つ Sniffing ブロックが追加されました。
- **Hysteria2 / Salamander：Gecko モード（packetSize）と Realm マスク用 TLS** — Hysteria2 の UDP マスク（FinalMask）の機能が拡張されました。Salamander マスクに Mode セレクタが追加されました：Gecko モードは、パケット長分析から保護するためにランダムなパディングを追加します（Min/Max サイズフィールド付き、1 〜 2048、デフォルト 512-1200）。Realm マスクにオプションの TLS Config ブロック（Server Name（SNI）、ALPN（h3/h2/http/1.1）、Fingerprint、Allow Insecure）が追加されました。
- **share リンクからの outbound インポートで xmux 設定を保存** — share リンクから outbound をインポートする際に、**xmux** マルチプレクサ（XHTTP）の設定が保存されるようになりました。以前は設定が無音で失われていました。インポート後、値は XMUX サブフォームに挿入されます。
- **サブスクリプションからの outbound タグが非 ASCII 文字（キリル文字）を保持** — サブスクリプションから取得した outbound のタグが、非 ASCII 文字（例：キリル文字）を保持して可読性を保つようになりました。以前は数字のみになっていました。

### 12. ノード（マルチパネル、master/slave）
- **ノード：新しい TLS 検証モード — Mutual TLS（クライアント証明書）** — ノードフォームの TLS 検証モードに 4 つのオプションが追加されました：Verify（システム CA）、Pin（SHA-256 による証明書ピン留め）、Skip（検証なし）、新しい Mutual TLS（クライアント証明書）。Mutual TLS モードでは、パネルが自身の CA によって発行されたクライアント証明書でノードに対して追加認証を行います。このタイプのノードでは API トークンがオプションになります。mTLS を有効にするには：ノードで Mutual TLS モードを設定し、Node mTLS セクションから管理パネルの CA をコピーし、ノードで信頼できる親 CA として設定してノードを再起動します。
- **ノード：「Node mTLS」セクション — パネル CA のコピーと信頼できる親 CA** — ノードページに、パネル間の相互 TLS 認証を設定するための Node mTLS セクションが追加されました。「このパネルの CA をコピー」ボタンは、パネルのルート証明書をクリップボードにコピーします。パネルのクライアント証明書を検証する管理ノードに渡す必要があります。「信頼できる親 CA」フィールドは、このパネル自体がノードである場合に使用します。管理パネルの CA をここに貼り付け、そのクライアント証明書を要求してパネルを再起動します。Mutual TLS はオプションで、フィールドが空の場合はノードが以前のスキーム（API トークンのみ）で動作します。
- **パネルからノードへの送信接続のルーティング（Connection outbound）** — ノードフォームに**「Connection outbound」**（送信接続）フィールドが追加されました。Xray outbound タグを選択すると、パネルからこのノードの API へのトラフィックが指定した outbound を経由します（パネルは loopback のブリッジ inbound を稼働設定に自動追加し、再起動なしで適用します）。空の場合は直接接続になります。リストのタグは「Outbounds」と「Balancers」にグループ化されており、blackhole outbound は非表示です。
- **ノード：選択した outbound を通じてパネル→ノード間のトラフィックをルーティング（「Connection outbound」）** — ノードフォームに「Connection outbound」フィールドが追加されました。パネルからノードへのアクセストラフィックを、選択した Xray outbound（通常の outbound とバランサーが利用可能）を通じてルーティングできます。パネルは稼働設定に loopback ブリッジ inbound を自動追加し、再起動なしで変更を適用します。直接接続の場合はフィールドを空のままにしてください。
- **ノード：inbound が紐付いている間はノードの削除がブロック** — すべての inbound がノードから外されるまでノードを削除できません。ノードに少なくとも 1 つの inbound が紐付いている場合、パネルはエラーで削除を拒否します。最初にこれらの inbound を外すか削除してから、ノードを削除してください。
- **ノード：ノードページにノードに配置された inbound のリアルタイム速度を表示** — ノードページで、ノードに配置された inbound のオンラインクライアント数、カウンター、現在の転送速度が表示されるようになりました。「終了」（ended）チップは、有効期限切れとトラフィック超過のクライアントのみをカウントします（無効化されたクライアントはカウントされなくなりました）。

### 14. Telegram ボット
- **通知：Telegram と Email（SMTP）チャンネルを使った新しいイベントバス** — 2 つの配信チャンネル（Telegram と Email）を持つイベント通知システムが追加されました。通知タブでイベントはカードにグループ化されています：Outbound（障害/復旧）、Xray Core（異常終了）、Nodes（ノード不達/復旧）、System（設定可能なしきい値%での CPU とメモリ高負荷）、Security（ログイン試行）。各グループにはマスタートグルと選択されたイベントのカウンターがあります。有効なイベントセットは Telegram と Email で個別に設定でき、デフォルトでは「ログイン試行」と「CPU 高負荷」が有効です。
- **通知：新しい Email/SMTP チャンネルと SMTP サーバー設定** — SMTP 経由のメール通知という新しい通知チャンネルが追加されました。SMTP 設定タブでは：メール通知の有効化、SMTP ホストとポート（デフォルト 587）、ユーザー名、パスワード（非表示で保存）、受信者リスト（カンマ区切り）、暗号化の種類（none、STARTTLS（デフォルト）、TLS）を設定します。「テストメールを送信」ボタンで接続を確認し、どの段階（接続、認証、送信）でエラーが発生したかを表示します。2 番目のタブで、メールを受信するイベントを選択します。
- **通知：メモリ高負荷アラート（RAM しきい値）** — CPU 高負荷通知に、メモリ（RAM）高負荷通知が追加されました。「System」イベントグループに「Memory high (%)」が独自のしきい値フィールド（デフォルト 80%）とともに追加されました。パネルは 1 分ごとに RAM 使用率を確認し、しきい値を超えると選択したチャンネルに通知を送信します。

### 15. ジオデータベース（geoip / geosite とカスタム）
- **ジオデータベースの更新：ファイルごとのステータスと変更がない場合の再起動スキップ** — ジオデータベース（geoip/geosite、IR および RU セットを含む）の更新で、ファイルごとのステータスが表示されるようになりました：更新済み、すでに最新、またはダウンロードエラー。Xray の再起動（したがってアクティブ接続の切断）は、少なくとも 1 つのファイルが実際に更新された場合にのみ発生します。変更がない場合、パネルは再起動しません。x-ui update-all-geofiles コマンドも同様の動作をします。

### 16. 運用：バックアップ、ログ、更新、CLI
- **クライアントの IP 制限は fail2ban がインストールされている場合のみ機能；そうでなければフィールドがブロック** — クライアントの IP 数制限は、サーバーに fail2ban がインストールされている場合にのみ機能します。インストールされていない場合、クライアントフォームと一括追加の「IP Limit」フィールドが、説明的なツールチップ（Windows では別のメッセージ）とともに利用できなくなります。以前に設定された制限はそのようなサーバーで自動的にリセットされます（どのみち適用されていなかったため）。fail2ban ブロックが TCP と UDP の両方に適用されるようになりました。
- **パネルのインストールと更新時に fail2ban を自動インストール** — 通常のサーバーでのパネルのインストールと更新時に、fail2ban が自動的にインストールおよび設定されるようになりました（以前は Docker のみ）。これにより、IP 制限機能がすぐに使えるようになります。環境変数 XUI_ENABLE_FAIL2BAN で動作を制御します。変数が設定されていないか true の場合、セットアップが実行されます。手動での実行は x-ui setup-fail2ban コマンドで可能です。fail2ban のエラーはインストールや更新を中断しません。
- **環境変数 XUI_PORT によるパネルポートのオーバーライド** — 現在のプロセスの実行中のみウェブパネルのポートを設定する環境変数 XUI_PORT が追加されました。データベースに保存された webPort の値は変更されません。1 〜 65535 の値が有効で、空、不正、または範囲外の値は無視されます（webPort が使用され、ログに警告が出ます）。bridge ネットワークで Docker を使用する場合、公開するコンテナポートは XUI_PORT と一致する必要があります。例：XUI_PORT=8080 と ports: 「8080:8080」。
- **CLI：-webCert/-webCertKey フラグが setting サブコマンドで機能するようになった** — CLI で -webCert と -webCertKey フラグが x-ui setting サブコマンドでも機能するようになりました（以前は無視され、パネルが HTTPS なしのままになっていました）。これらを指定することで、別の cert サブコマンドを呼び出すことなく、ウェブパネルの証明書とキーのパスを直接設定できます。
- **DB バックアップファイル名がサーバーアドレスに基づいて生成** — データベースバックアップファイルの名前が、固定の x-ui.db / x-ui.dump ではなく、サーバーアドレスに基づくようになりました。ブラウザからダウンロードする場合、名前はアドレスバーのパネルアドレスから取得されます。そうでない場合は設定されたウェブドメインから、それがない場合はパブリック IP（まず IPv4、次に IPv6）から取得されます。これにより、異なるサーバーからのバックアップを簡単に区別できます。拡張子は SQLite では .db、PostgreSQL では .dump のままです。
- **IPv6 のみのホストでのインストールと更新をサポート** — インストールおよび更新スクリプトが、IPv6 のみのサーバーで正しく動作するようになりました。リリースと補助ファイルのダウンロードが IPv4 の使用を強制しなくなったため、IPv4 アドレスのないホストでもパネルをインストールおよび更新できます。

---

パネルのソースファイルの分析をもとに作成。Yuriy Khachaturian ([yukh.net](https://yukh.net))

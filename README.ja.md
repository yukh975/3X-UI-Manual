# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 日本語 · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

パネル [3x-ui](https://github.com/MHSanaei/3x-ui) のユーザーマニュアル — パネル **v3.5.0** 向けに書かれた総合ユーザーガイド。

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

## 3.5.0の新機能

バージョン3.5.0は大規模なリリースです: MTProtoがマルチクライアントモデルに移行し（mtg-multiエンジン、クライアントごとのシークレット・クォータ・ad-tag）、管理対象ホストがグループ化され（1つのレコードに複数のinboundとアドレス）、PostgreSQLパネルの復元がSQLiteバックアップを受け付けるようになり、outboundには「Target Strategy」、「Real delay」テスト、Egress/Country列が追加され、バランサーは別のバランサーをfallbackとして使用できるようになりました。同梱のXrayコアは26.7.11です。以下では、3.4.2からの変更点をマニュアルのセクション別にまとめています。

### セクション1の変更 — はじめに、要件、インストール

- Xray コアが **26.7.11** に更新されました。付随する自動マイグレーション: Shadowsocks の暗号方式 `none`/`plain` と VMess の `none`/`zero` がコアから削除され（保存済みの設定は自動的に書き換えられます）、公開アドレスへの暗号化されていない VLESS/Trojan outbound は保存時に拒否されます。
- 新しいコマンド **`x-ui pgclient [バージョン]`** と、PostgreSQL メニューの項目 **10. Install/Upgrade client tools (pg_dump/pg_restore)** が追加されました — PostgreSQL クライアントツールのインストール/更新を行います。
- スクリプトの修正: RHEL 系での PostgreSQL と fail2ban のインストール（EPEL）、Arch では完全な `pacman -Syu` を実行しない、32 ビット ARM での Xray バイナリの正しい名前（`xray-linux-arm32`）、IP 証明書の発行前に自動検出された IPv4 を確認、デフォルトの ACME ポート選択時の誤った「Your input is invalid」を修正。

### セクション2の変更 — パネルへのログインとアクセスセキュリティ

- IP リミット: 「死んだ」接続は 10 秒ごとのスキャンのたびではなく **1 回だけ** BAN されるようになりました — fail2ban のカウンターが不要に増加しなくなり、`maxretry` を大きめに設定する必要はなくなりました。

### セクション4の変更 — Inbounds: 作成と共通パラメータ

- inbound リストに **検索**（備考・ポート・プロトコルによる）が追加され、ノードのドロップダウンリスト（「デプロイ先」、「ノード」フィルター）が検索対応になりました。

### セクション5の変更 — プロトコル

- **MTProto がマルチクライアントモデルに移行しました**（mtg-multi エンジン）: MTProto のユーザーは、独自のシークレット・クォータ・有効期限・ad-tag・パーソナルな `tg://proxy` リンクを持つ通常のクライアントになりました。inbound レベルの「Secret」フィールドは削除され（既存の inbound は自動的に変換されます）、「FakeTLS domain」は新しいシークレットのデフォルトドメインになりました。新しい inbound フィールド: **Max connections**（接続数の制限）、**Public IPv4/IPv6**（ad-tag middle proxy 用）。クライアントの変更は、他のユーザーの Telegram セッションを切断せずに「オンザフライ」で適用されます。
- WireGuard: inbound メニューにクライアント操作の完全なセット（Export All URLs、紐付け/紐付け解除、グループ）が追加され、エクスポートが **Config** と **Links** のタブに分割され、**「WireGuard 許可 IP」フィールドが編集可能** になり（カンマ区切りで複数エントリ）、ノード上の inbound のクライアント設定では `Endpoint` がノードのアドレスを指すようになりました。

### セクション7の変更 — 接続セキュリティ：TLS、XTLS、REALITY

- **Finalmask + REALITY の組み合わせは保存時に拒否** されるようになりました（初回接続時に Xray-core がクラッシュする原因になっていました）。minClientVer のプレースホルダーは 26.3.27 に更新されました。
- Finalmask の新しい TCP マスクタイプ **XMC (Minecraft)**: ストリームを Minecraft トラフィックに偽装します（Hostname、Usernames、自動生成付きの必須 Password）。

### セクション8の変更 — クライアント

- 新しい **「速度」** 列 — 各クライアントのライブ速度（↑/↓、約 5 秒間の移動平均）。
- クライアント検索が再び **Telegram ID** で検索できるようになりました。クライアントフォームでは無効化された inbound が紐付けリストに表示されなくなり、「紐付け解除」ウィンドウでの重複エントリの蓄積が修正されました。
- MTProto クライアントには専用フィールドがあります: **「MTProto secret」**（再生成付き）と **「Ad-tag（スポンサーチャンネル）」**（32 の hex 文字）。クォータと有効期限が MTProto にも実際に適用されるようになりました。

### セクション9の変更 — クライアントグループ

- クライアント情報ウィンドウにクライアントの **グループ** が表示されるようになりました。

### セクション10の変更 — サブスクリプション (Subscription)

- **管理対象ホストがグループ化されました**: 1 つのレコードが **複数の inbound**（マルチ選択）と **複数のアドレス**（タグ入力、各エントリに独自の `:ポート` を指定可能; アドレスの自動補完; 空の場合は inbound のアドレスを継承）をカバーします。リストの列はアドレスと inbound のチップ（「+N」付き）を表示し、操作と API はグループ（`groupId`）単位で動作し、一括の `POST /panel/api/hosts/bulk/add` が追加されました。ホストの並び順はグローバルになりました（並び順、次に備考順）。
- **お知らせ**（`subAnnounce`）のテキストがサブスクリプション情報ページにバナーとして表示されるようになり、カスタムテンプレートで変数 `announce` が利用可能になりました。
- ブラウザでの情報ページが **JSON/Clash リンク** でも開くようになりました（メインリンクだけではなくなりました）。
- ホスト設定の **Final Mask** と **Allow insecure** が、それぞれ raw リンク（`fm=`）と **Hysteria2**（`insecure=1` / `skip-cert-verify: true`）にも適用されるようになりました。
- 「更新間隔」（`subUpdates`）の範囲が **0–525600** に修正されました（従来の UI 上限 168 は 2.x からのアップグレード後に設定の保存をブロックしていました）。
- ネイティブ **WireGuard クライアントが Clash および JSON サブスクリプションに含まれる** ようになりました（以前は raw のみ）。

### セクション11の変更 — Xray: ルーティング、outbounds、DNS、および拡張機能

- outbound エディター: 新しい **「Target Strategy」** フィールド（`AsIs` から `ForceIPv4` まで 11 の値）、テストモード **「Real delay」**（トンネル確立を含む合計時間; HTTP モードは「ウォーム」接続で測定されるようになりました）、HTTP/Real テスト後の **Egress** 列（「目」アイコンの背後の出口 IP）と **Country** 列（国旗 + 国名、WARP ラベル）。
- **バランサーの Fallback に別のバランサーを指定できる** ようになりました: パネルは非表示の loopback オブジェクト（`_bl_…`）を自動的に構築し、循環参照や使用中のバランサーの削除から保護します。プレフィックス `_bl_` は予約されています。
- 「基本ルーティング」タブに **「Default Outbound」** セレクターが追加されました — どのルールにもマッチしなかったトラフィックを処理する outbound です（選択したものが先頭に移動されます）。
- プライベート IP 上の DNS サーバーが `geoip:private` ルールでブロックされなくなりました — パネルが管理された許可ルールを自動的に維持します。
- dial 設定（sockopt）の Happy Eyeballs が実際に有効化されるようになりました。「Try delay」のデフォルトは 250 ms になり、明示的な 0 は保持されます。
- outbound サブスクリプションのインポート: `?plugin=` や末尾の `/` を持つ `ss://` リンクのポートが正しく解析されるようになりました。

### セクション12の変更 — ノード（マルチパネル、マスター/スレーブ）

- 修正パッケージ: 変更なしのクライアント保存がノード inbound の稼働中トラフィックを壊さなくなりました。ノードの Host オーバーライドが初回承認時にマスターへ取り込まれます。自動更新が新しいクォータウィンドウを開きます。マスターでのクライアント削除がノード上でも完全に削除するようになりました。ノードの inbound は初回承認前に一掃されなくなりました。1 つの不正な inbound がノードのトラフィック同期を止めなくなりました。ポート競合チェックは自分のノードに限定されました。

### セクション14の変更 — Telegramボット

- ボットのコマンドメニューに **`/usage`**、**`/inbound`**、**`/restart`** と、新しい管理者コマンド **`/clearall`**（全クライアントのトラフィックリセット、確認付き）が追加されました。
- オンラインクライアントのリストは `email - inbound の備考` としてラベル付けされます。バックアップと BAN ログのメッセージにホスト名が含まれます。Telegram ID による検索は設定のフォーマットに依存せず機能します。

### セクション16の変更 — 運用：バックアップ、ログ、更新、CLI

- **PostgreSQL パネルの復元が SQLite ファイルを受け付ける** ようになりました: 通常の `.db` バックアップまたはマイグレーション用 `.dump` が直接 PostgreSQL にインポートされます（単一トランザクション、Xray 停止前のチェック付き）。ファイル選択ダイアログは両方の DBMS で `.dump,.db` を受け付けます。「マイグレーションファイルをダウンロード」は PostgreSQL パネルにのみ残りました。
- `pg_dump` アーカイブの復元前に、パネルはダンプの読み取り可能性を確認し、バージョン不一致の場合は正確なコマンド `x-ui pgclient <バージョン>` を提示します。
- 起動時の自動修復: オーバーフローしたトラフィックカウンターがクランプされて復元されます。inbound ポートの古い UNIQUE 制約が削除されます（multi-node の妨げになっていました）。
- Xray ログ: 新しいジョブが 10 分ごとに、access ログと error ログが **64 MiB** を超えた場合に切り詰めます。毎日のクリーンアップは両方をクリアするようになりました。
- Docker: 証明書の自動更新が修正されました（crond が起動し、acme.sh の状態がボリュームに保存されます）。

---

パネルのソースファイルの分析をもとに作成。Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

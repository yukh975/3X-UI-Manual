# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 日本語 · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

パネル [3x-ui](https://github.com/MHSanaei/3x-ui) のユーザーマニュアル — パネル **v3.4.2** 向けに書かれた総合ユーザーガイド。

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

## 3.4.2の新機能

バージョン3.4.2は大規模なアップデートです: WireGuardがマルチクライアントモデルに移行し、REALITYにライブのターゲットスキャナーが追加され、バランサーに「Observatory」/「Burst Observatory」タブが設けられ、機微な設定変更に2FAコードによる確認が導入されました。以下では、3.4.1からの変更点をマニュアルのセクション別にまとめています。

### セクション1の変更 — 概要・要件・インストール

- サイドメニュー（およびモバイルのドロワー）に **「ドキュメント」** ボタン（本のアイコン）が追加され、公式ドキュメント `https://docs.sanaei.dev/` を開きます。
- パネルが更新する Xray の最小バージョンが **26.6.27** に引き上げられました（同梱の Xray コアも 26.6.27）。

### セクション2の変更 — パネルへのログインとアクセスセキュリティ

- 2FA が有効な場合、管理者のログイン名/パスワードの変更および 2FA の無効化に、認証アプリの **現在のコードの入力** が必要になりました（機微な変更の確認）。
- LDAP: 新しいトグル **「TLS 証明書の検証をスキップする」**（`ldapInsecureSkipVerify`）が追加されました。LDAPS 時に証明書の検証を無効にします。「TLS（LDAPS）を使用する」が有効な場合のみ利用できます。

### セクション3の変更 — 概要 / ダッシュボード

- パネルバージョンボタンが常に更新ウィンドウを開くようになりました（セクション16 — dev チャンネル参照）。
- 全面的な **アクセシビリティ** の改善: アイコンに aria ラベルを付与し、Enter/Space で要素を操作できるようにしました（スクリーンリーダーおよびキーボードナビゲーション向け）。

### セクション4の変更 — Inbounds: 作成と共通パラメータ

- **「すべてのリンクをエクスポート」** アクションがサブスクリプションエンジン経由でリンクを生成するようになりました。各クライアントにリマークテンプレートを適用し、管理対象の Host エンドポイントを優先します（以前は固定のリマーク `inbound-email` でした）。

### セクション5の変更 — プロトコル

- **WireGuard がマルチクライアントモデルに移行しました。** peer は通常のクライアントになりました（トンネル内アドレスの自動割り当て、サブスクリプション対応、トラフィック/期限の制限、グループに対応）。inbound フォームのインライン「peer」リストは削除されました。
- WireGuard inbound に設定可能な **DNS** フィールド（デフォルト `1.1.1.1, 1.0.0.1`）と **クライアント設定カード**（完全な `.conf` および `wireguard://`/`wg://` リンクのコピー/ダウンロード/QR）が追加されました。

### セクション6の変更 — トランスポート（Stream Settings）

- XHTTP の新規 inbound では、**xmux** の `maxConnections` パラメーターのデフォルトが **6** になりました（以前は `0` — 無制限）。既存の inbound は自身の値を保持します。

### セクション7の変更 — 接続セキュリティ: TLS、XTLS、REALITY

- **REALITY のライブターゲットスキャナー** が追加されました: **「スキャン」** ボタン（現在のターゲットを「ライブで」チェック）と **「ターゲットを検索」** ボタン（ドメインまたは **IP/CIDR** 範囲をスキャンし、証明書から適切なターゲットを選定）。REALITY を初めて選択したとき、「ターゲット」フィールドと SNI は空になりました。

### セクション8の変更 — クライアント

- `bulkAdjust` による期限/クォータの延長が、**枯渇のみが原因で**無効化されていたクライアント（期限切れまたはクォータ超過）を、延長によって制限内に戻る場合に **自動的に有効化** するようになりました。手動で無効化されたクライアントや、まだ枯渇しているクライアントは無効のままです。

### セクション9の変更 — クライアントグループ

- グループの **「トラフィックをリセット」** が、**グループ自体のカウンターのみ** をゼロにするようになりました。個々のクライアントのカウンター・クォータ・状態には影響せず、Xray の再起動も不要です。これは従来の動作からの変更です（以前はグループのすべてのクライアントのトラフィックがリセットされていました）。

### セクション10の変更 — サブスクリプション（Subscription）

- **管理対象ホスト** の **VLESS route** フィールドが再定義されました: 1 つの値 `0-65535`（ポートのリストではなくなりました）になり、生成される各サブスクリプションの UUID に実際に「埋め込まれる」ようになりました（raw/JSON/Clash）。
- リマークテンプレートの変数 `{{EMAIL}}`（およびその同義語 `{{USERNAME}}`）が、クライアントの **最初のリンク** にのみ出力されるようになりました — トラフィック/期限ブロックと同様です。

### セクション11の変更 — Xray: ルーティング・outbound・DNS・拡張機能

- **バランサー**: ページが **「バランサー設定」** タブと **「Observatory」** タブに分割されました。生の JSON の代わりに Observatory および Burst Observatory のフォームが用意されました（Burst には **「HTTP メソッド」** フィールドが追加されました）。`fallbackTag` を持つ Random/Round-robin バランサーは、Burst Observatory を自動的に作成するようになりました。
- outbound またはバランサーを削除すると、パネルがルーティング内の関連参照を自動的にクリーンアップし、確認ダイアログに **影響のプレビュー** を表示します。
- ルーティングルールのネットワーク条件 **L4** は、設定では小文字（`tcp`/`udp`）で書き込まれ、テーブルでは大文字で表示されます。
- バランサーの追加/編集フォームのエラーは、フィールドに初めて触れるか保存を試みるまで遅延表示されるようになりました。

### セクション12の変更 — ノード（マルチパネル、master/slave）

- 「ローカルに保存しました、ノードはオフラインです — 後で同期されます」という通知が、ノードが実際にオフラインまたは無効の場合にのみ表示されるようになりました（以前はオンラインのノードに保存するたびに表示されていました）。

### セクション16の変更 — 運用: バックアップ・ログ・更新・CLI

- バックアップファイル名にサーバーアドレスと **日時** が含まれるようになりました: `{host}_YYYY-MM-DD_HHMMSS.db`（PostgreSQL は `.dump`）、例 `panel.example.com_2026-06-27_000000.db` — パネルからのダウンロード時、および Telegram ボットが送信するバックアップの両方に適用されます。
- 安定版ビルドからでも更新の **dev チャンネル** を有効にできるようになりました: バージョンボタンが常に更新ウィンドウを開き、不安定性および自動ロールバックがないことの警告を伴う **「Dev チャンネル」** トグルが追加されました。

---

パネルのソースファイルの分析をもとに作成。Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

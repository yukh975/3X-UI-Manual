# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.6.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.6.0

Version 3.6.0 updates the core to **Xray 26.7.28** and noticeably reworks the interface. Highlights: the Overview page became a command deck (CPU/RAM/Swap/Storage tiles with sparklines, a new TCP/UDP connections chart, and a sidebar that is now a hover-to-expand icon rail); the **XMC (Minecraft)** TCP mask now requires full Mojang profiles (a breaking change); subscriptions can now **auto-detect the client by User-Agent** and serve live status via `?format=info`; **node API tokens are now write-only**; panel emails gained sender **From/name** fields; and SQLite runs in **WAL** mode by default. Below are the changes relative to 3.5.0, grouped by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- The **Xray core is updated to 26.7.28** (the panel and its child binary are kept in lockstep). An unencrypted outbound (no TLS or other encryption) to a public address is still rejected, but that check is now **skipped when the running core is older than 26.7.11** — so it no longer blocks a config your core would actually accept.

### Changes in section 2 — Panel login and access security

- **`GET /panel/api/openapi.json` now requires authentication.** Previously the full admin-API map plus the build version were served anonymously (HTTP 200); the endpoint now sits behind the shared `checkAPIAuth` (a session, a Bearer token, or mTLS) and returns 404 without credentials. Token-authenticated clients are unaffected.

### Changes in section 3 — Overview / Dashboard

- The **Overview page was reworked into a command deck**: a top action bar (Xray state with its version and the error text in a tooltip, the panel version/Update control, and grouped Restart/Stop, Logs/Config/Backup, and System History / Xray Metrics buttons), plus a warning banner under load (80% / 90%).
- The circular gauges are gone; in their place are **four tiles** — CPU/RAM/Swap/Storage — each with a large percentage, detail, average/peak, and a filled **sparkline**. Sparklines use a 72-sample window, are seeded on load from `GET /panel/api/server/history/<metric>/2`, and are appended every 2 s; the tooltip shows clock time.
- Two wide trend charts: **Overall Speed** (↑/↓) and a **new TCP/UDP Connection Stats chart** (open sockets).
- Removed: the gauges, the Telegram @XrayUI card, and Load average (moved to System History). The System strip is now grouped (Xray | OS uptime, panel RAM | threads, IP addresses with a show/hide toggle).
- The **sidebar** is now a 72 px icon rail that expands on hover; the manual collapse toggle is gone.

### Changes in section 4 — Inbounds: creation and common parameters

- Monthly traffic reset gained a **"Reset day" (1–31)** field — pick the day of the month the counter resets, instead of a fixed day.

### Changes in section 5 — Protocols

- **Hysteria is version 2 only.** The inbound schema pins `version` to `2` (a value from the API or older panels is healed automatically), and the dead `hysteria://` link scheme is removed — the link is always `hysteria2://`. "Hysteria2" is not a separate protocol; it is `hysteria` with `version = 2`.
- Shadowsocks reliability: a client whose cipher is stored under the `method` key (not `cipher`), and `aead_*` aliases, no longer crash the core — the cipher name is matched against the core's own table case-insensitively, and an unrecognized value is an error rather than a guess.

### Changes in section 6 — Transport (Stream Settings)

- XHTTP, the **`uplinkDataPlacement`** field: the invalid `query` option was removed and `auto` was added; the default label is now **"Default (auto)"**.
- When XMUX is first enabled, the default **`maxConnections` is lowered from 6 to 3** (tracking core 26.7.28); already-saved values are untouched.

### Changes in section 7 — Connection Security: TLS, XTLS, and REALITY

- **The Finalmask XMC (Minecraft) mask changed — a breaking change.** Instead of a `usernames` list, a **profiles** array is now required, each with `username` (3–16 of `A-Za-z0-9_`), `uuid` (dashed or 32 hex characters), `texturesValue`, and `texturesSignature` (signed values from Mojang's session server). The old "default to Dream" fallback is gone. The panel **rejects an incomplete XMC mask on save**; rows from older panels / the API / a backup **lose only that one mask** at config generation (the whole config no longer goes down, and a warning names the inbound); in the form, old `usernames` are carried into profile stubs. Rebuild the profiles with data from Mojang's session server, or the obfuscation won't work.
- The **Min/Max Client Ver** (REALITY) fields gained tooltips and save-time format/range validation; the placeholder is now `x.y.z`. **Important:** empty Min/Max no longer means "no restriction" — the check has a built-in minimum client version.
- Fixed: switching a Finalmask item to the array (`rand`) kind no longer writes an empty `packet: []` that used to bring the whole config down (the residue is also stripped from already-saved rows).

### Changes in section 8 — Clients

- New REST endpoint **`GET /panel/api/clients/get/tgId/:tgId`** — look up clients by Telegram ID (returns an array, since the ID isn't unique; accepts a positive ID only). A DB index backs it.

### Changes in section 10 — Subscriptions (Subscription)

- **Format auto-detection by User-Agent** (a new "Subscription formats" tab): `subClashAutoDetect` + `subClashUserAgentRegex` (default `(?i)(clash|mihomo)`) serve Clash YAML to Clash/Mihomo clients; `subJsonAutoDetect` + `subJsonUserAgentRegex` (empty by default, so off) serve a JSON array; `subJsonAlwaysArray` returns an array even for one profile on the explicit `/json/` endpoint. The regexes are Go RE2, validated on save; a panel restart is required to apply them.
- The **"Show identity on every link"** toggle (`subShowIdentityOnAllLinks`): `{{EMAIL}}` / `{{USERNAME}}` stay on every link's remark (usage tokens still appear on the first link only).
- A new **`?format=info`** query parameter — the subscription's live status as JSON (without the links, with a new **`isOnline`** field and deduplicated emails); templates and the subscription page now get the `{{ .isOnline }}` variable. The **`?view=raw`** parameter and **Download** buttons save the JSON/Clash subscription as a file.
- Output correctness: a WireGuard client now exports **all** Allowed IPs (raw link and `.conf`), not just the first; Clash YAML quotes "numeric-looking" short-ids / passwords / PSKs (otherwise one proxy zeroed out the whole provider); VLESS `flow` is now gated in JSON too; empty remark variables no longer leave a dangling hyphen; Hysteria2 drops the non-standard `fm=`; external link names are preserved in Clash/JSON; the Happ `Routing-Enable` header is sent only when enabled; XHTTP emits the legacy session-field aliases; a managed host's `hostHeader` / `path` apply to ws/httpupgrade/xhttp; Clash emits `pin-sha256`; and the raw generators are hardened against 500s.

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **The default (freedom) outbound now blocks egress to private ranges** (`geoip:private`): a `block` rule was added to the front of its `finalRules`, closing an SSRF path to the local gRPC / metrics listeners via the AsIs domain strategy. On upgrade a one-time seeder rewrites **only stock** `finalRules`; your customizations are kept. If you need LAN / loopback access through the direct outbound, add an explicit allow rule ahead of the block.
- The route tester (**Route test**) rejects an out-of-range port instead of wrapping it.
- An inbound whose clients are all filtered out now serializes as `"clients": []` instead of `null` in the config (a debugging cosmetic).

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **A node's API token is now write-only.** Reading a node no longer returns the token itself — only a `hasApiToken` flag. On edit: a blank field **keeps the current token**, a non-empty value replaces it, and `clearApiToken` removes it (only for a disabled or mTLS node). The field hint reads "Leave blank to keep the current token."
- Reliability: a departed master's frozen traffic no longer disables a client that is actually within quota (only fresh rows are counted); inbound fallback edits now reach the nodes; and the MTProto sidecar (`mtg-multi`) lifecycle is hardened.

### Changes in section 13 — Panel Settings

- Email (SMTP): new **"SMTP From Address"** (`smtpFrom`) and **"SMTP Sender Name"** (`smtpFromName`) fields. The message is now assembled per RFC 5322 (a proper name-addr `From`, a `Date`, a `Message-ID`, and a UTF-8 Subject) — strict receivers like Gmail stop rejecting it. An empty `smtpFrom` = use the SMTP username (existing setups are unchanged); an invalid address is rejected on save.
- Notifications: a new **`outboundDownThreshold`** (default 3, range 1–100) next to the "outbound down" event in both channels — Email and Telegram: the alert fires only after N consecutive failed probes; `1` reproduces the old notify-on-first-failure behavior.
- Many numeric fields gained a grey **"Default"** tag; clearing a port field no longer saves port `1` (it reverts to the stored value — no lockout); the expiry date-picker commits on click (no OK button, and it no longer silently saves `0`).
- Build: production sourcemaps are no longer bundled in the binary (`dist` dropped from ~25 MB to ~6.7 MB); rebuild with `XUI_SOURCEMAP=true` to debug.

### Changes in section 14 — Telegram Bot

- **Privileged bot callbacks now require admin rights** (backup export, mass traffic reset, client creation, ban logs, and so on) — relevant if the bot is in a shared / group chat.
- A transient auto-deleted bot message no longer resets the in-progress wizard state.

### Changes in section 16 — Operations: backups, logs, updating, CLI

- SQLite runs in **WAL** mode by default — the end of the "database is locked" storm under normal load (applied automatically on upgrade).
- SQLite backups are taken as an **online snapshot** (a consistent copy while writes continue) — for downloads, migration, and the scheduled Telegram backup; interrupted snapshots are swept at startup.
- PostgreSQL: the panel survives a database outage without a runaway instant-restart loop (reconnect with backoff, ~70 s total).
- The external traffic-notify webhook is now bounded by a timeout (~3 s) — a stalled receiver no longer wedges the 5-second traffic tick and quota enforcement.
- Startup self-repair: legacy string `tgId` values in inbound settings are repaired (numeric string ids are preserved) — the end of the `cannot unmarshal string into ... tgId` error.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

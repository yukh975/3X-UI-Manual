# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.9.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.9.0

Version 3.9.0 is a feature release. The headline: the **TUIC v5** protocol now runs natively inside the 3x-ui process — a separate `tuic-server` sidecar is no longer needed (#6577), and its traffic goes through Xray routing and chains, honors per-client quotas, and survives client edits without dropping connections. **AmneziaWG, TUIC, and MTProto** inbounds can now be deployed on nodes. The Happ client gained a **routing-rule editor, a separate ad-blocking toggle, and a "local network direct" preset** (#6545); the Happ settings are folded into four tabs. The Telegram bot got **access levels, account linking via `/start` and an invite link** (#6518) and a **`/broadcast`** command to message every client (#6510). A new **"Exclude from subscriptions"** inbound toggle hides the links without disabling the inbound itself (#6463). Clients gained **weekday calendar renewal with a schedule preview** (#6524), and **traffic counters are preserved during a portable export/import** (#6469). **Two inbounds — IPv4 and IPv6 — can share one port** (#6603). A **custom User-Agent** can be set for downloading a client's external subscriptions (#6613), and the `x-ui setting -getApiToken` command gained a **`-tokenScope`** flag (#6700). The core is updated to **Xray-core v26.9.30**: on the first start the saved configurations are rewritten once to match its keys (XDNS masks and the WireGuard outbound). Build requirements: Go 1.27.1, Xray-core v26.9.30. Below are the changes relative to 3.8.5, by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- **Bundled with Xray-core 26.9.30** (instead of 26.9.9). Building from source still requires Go 1.27.1; installing from packages and the script is unaffected.
- **The `tuic-server` sidecar is no longer downloaded or needed:** TUIC v5 is implemented natively inside the panel (#6577). `install.sh`, the Docker image, and the release archives no longer contain it, and on reinstall/upgrade the old binary (`bin/tuic-server*`) and the `bin/tuic` directory are removed automatically.
- **One-time template migrations on the first start of 3.9.0:** the XDNS masks (Final Mask) are rewritten into the new object format (`XdnsFinalmaskObjectsFix`), and for the WireGuard outbound the `settings.domainStrategy` key and the `"local"` remoteDNS mode are moved into `sockopt.domainStrategy`/`targetStrategy` (`WireguardDomainStrategyFix`). **Back up the database before upgrading** — an unmigrated XDNS mask or a leftover `"local"` remoteDNS will keep the core from starting, and after the mask format changes old clients need a new client Xray.

### Changes in section 4 — Inbounds: creation and common parameters

- **An IPv4 and an IPv6 inbound can listen on the same port** (#6603): if the IPv6 inbound listens on `::` with `v6only` enabled in sockopt, it no longer conflicts with an IPv4 inbound on the same port. A bare `0.0.0.0` or `::` without `v6only` still takes the whole port.
- **The "Exclude from subscriptions" toggle** (`excludeFromSub`, #6463): hides the inbound's links from every subscription output format while leaving the inbound itself enabled and working (unlike disabling it).
- **Saving an inbound no longer touches its clients:** the inbound edit form does not load or send the client list, and the "Enable" toggle is shown only when adding. A client added, deleted, renewed, or reset in parallel (by the bot, the API, or another admin) is no longer rolled back by saving the inbound. Importing an inbound from a 2.x panel now accepts the old client field format (string `tgId`) (#6663).

### Changes in section 5 — Protocols

- **TUIC v5 runs natively inside the 3x-ui process** ([5.13](#513-tuic-v5), #6577), without the `tuic-server` sidecar. The decrypted traffic goes into the Xray core over a local SOCKS5 bridge, so **routing, geo-rules, and chains** of Xray now apply to TUIC; **a client's personal traffic quota (`totalGB`) is now supported and enforced**; adding/editing/disabling a client is **applied live, without dropping the connections** of the others; the online status no longer depends on the logging level. The `cubic` algorithm is served as `new_reno` on the server. A TUIC inbound can now be **deployed on a node** (node v3.8.0 or newer).
- **AmneziaWG:** the signature fields **I2–I5** are exposed in the outbound form (#6611). Inbound validation is tightened: **S1 ≤ 1552, S2 ≤ 1608, S3 ≤ 1636** (so the handshake fits into the receive buffer of iOS peers), and overlapping **H1–H4** ranges **are now rejected** (#6642). AmneziaWG client connectivity is fixed (relay sniffing with `routeOnly`) (#6654).
- **Hysteria2:** client edits are applied live (AddUser/RemoveUser) without recreating the UDP listener — neighboring connections are no longer dropped when a single client changes (#6606).
- **WireGuard, AmneziaWG, and TUIC configs advertise the addresses from the bound hosts** (Hosts), not the panel's own address; with several hosts one config per host is issued.

### Changes in section 7 — Connection Security: TLS, XTLS, and REALITY

- **The hint for an empty "Min client version" is clarified by core version** (#6568): an empty field means "no lower bound" only on Xray-core v26.9.8+; on cores v26.7.11–v26.9.7 an empty field still yields the built-in minimum 26.3.27 (to accept such clients, set `1.0.0`).
- **The "Cipher suites" field** became a multi-select with tag input — you can set several suites or a name not in the list; the same setting was added to managed hosts (see [10.4](#104-output-formats)).

### Changes in section 8 — Clients

- **Auto-renewal is set with a single mode selector** (#6524): "Disabled", "At a fixed interval (days)", **"Calendar — by weekday"**, and "Calendar — by day of month". For the weekly mode a **"Renewal weekday"** field appeared (`resetWeekday`, 1=Mon…7=Sun). Next to it is a **renewal schedule preview** (renewal date, validity, the number of periods to be charged).
- **Traffic counters are preserved during a portable client export/import** (#6469): the export carries `up`/`down`/`resetCount`/`lastOnline`, and the import restores them only for newly created clients (existing ones are not overwritten).
- **The HWID device list is populated for clients without a limit too** (limit 0): devices are recorded but block nothing.
- **Overlapping `allowedIPs` of WireGuard/AmneziaWG clients are rejected** (#6623): masked ranges are compared, not exact strings — a client with `…/24` no longer "captures" other clients' addresses.

### Changes in section 9 — Client groups

- **The group filter and client search work with non-ASCII uppercase** (Cyrillic, Farsi, etc.): case is now folded for non-Latin text too (#6685).

### Changes in section 10 — Subscriptions (Subscription)

- **A custom User-Agent for downloading a client's external subscriptions** (#6613): a new field on the "Subscription" settings tab (`externalSubUserAgent`, `v2rayNG/1.8.5` by default). It is a global setting; it is unrelated to the per-outbound User-Agent from [11.12](#1112-subscription-outbounds-with-auto-update).
- **Happ: a routing-rule editor, ad blocking, and a "local network direct" preset** ([10.7](#107-happ-client-integration), #6545). Ad blocking is now a separate toggle, presets are applied with an "Apply template" button, and an "Everything through the proxy, local network direct" preset is added. The Happ settings are folded into four tabs; **Happ local-proxy authentication** was added (#6628).
- **Incy app-management parameters** ([10.2](#102-subscription-server-settings), #6650): a dedicated "Incy" tab with auto-detection and field groups (app, banners, privacy, network, routing).
- **When downloading external subscriptions the panel sends a stable `X-HWID`** (#6567, #6579), so providers with a per-device limit do not reject the request; no settings required.
- **Behind a reverse proxy `X-Real-IP` is no longer used as the server address** in links (#6608).
- **A client on several tunnel inbounds gets the correct keys and the address of its own node in each subscription** (#6653).

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **One-time template migrations for Xray-core 26.9.30:** the XDNS masks (Final Mask) are converted into the new object format, and for the WireGuard outbound the domain strategy is moved into `sockopt.domainStrategy`/`targetStrategy` (the `"local"` remoteDNS mode is dropped). The `domainStrategy` selector is removed from the WireGuard/WARP outbound form.
- **A `remoteDNS` that does not parse as an IP is rejected** on saving the template and for subscription outbounds.
- **The REALITY ML-KEM hint** (`support-x25519mlkem768`) is now carried into raw `vless://` links too, for Xray 26.9.8+ clients (#6712).

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **AmneziaWG, TUIC, and MTProto inbounds can now be deployed on nodes** (#6306). The protocol is run by the node's own panel, so a node version threshold applies: MTProto — v3.5.0+, AmneziaWG — v3.7.0+, TUIC — v3.8.0+; a node below the threshold (or one that has not yet reported its version) rejects the save.

### Changes in section 14 — Telegram Bot

- **Access levels** (#6518): "unlinked" (only `/start` and `/id`), "user" (own `/usage`, `/status`, `/help`), and "administrator" (everything). New commands get administrator rights until explicitly allowed.
- **Account linking via `/start`:** the bot's client card gained an **"Invite link"** button — the first person to open the link is bound to this client (the previous manual linking via `/id` is kept). There is a rate limit (5 attempts per hour).
- **The `/broadcast` command** (#6510, admin only): sends a message (text, media, album) to every client with a linked Telegram ID, with a preview, confirmation, and progress; the admin is not disclosed to the recipients.
- The "New client" wizard is now split by admin, not by chat (#6604); WireGuard and AmneziaWG are available in the inbound picker (#6621); links and QR codes are built in-process (#6597); the QR caption is localized (#6562).

### Changes in section 16 — Operations: backups, logs, updating, CLI

- **The `-tokenScope` flag for `x-ui setting -getApiToken`** (#6700): the token scope — `admin`, `monitor`, or `node-sync`. On reissue the token **keeps its previous scope and expiry** (it used to silently become `admin`); an unknown value is rejected before the token is deleted.
- **Viewing the system log is capped by a 15-second `journalctl` timeout** (#6689); the `x-ui` menu reads the service state without scanning the journal (#6629) — no more delays on hosts with large logs.
- **On EL7/CentOS 7 `x-ui.sh` keeps firewalld, pulled in by fail2ban, from blocking the panel ports** (#6688).
- **A restore from an SQL dump is isolated to its own database file** — a malicious dump cannot open or create an outside file.
- **Back up the database before upgrading** — the first start runs one-time template migrations (see sections 1 and 11).

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

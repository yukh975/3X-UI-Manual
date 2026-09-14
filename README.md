# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.8.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.8.0

Version 3.8.0 adds **a new protocol, TUIC v5** — it runs as a separate `tuic-server` process managed by the panel, like MTProto — along with **AmneziaWG as an outbound** and a **Discord bot** for notifications, reports and commands. The rest of the headline: **Happ client integration** (app-management headers, routing presets, encrypted links); the subscription can now serve **a separate info config with status**, **a routing profile and DNS servers for JSON**, **balancer member weights** and **a counter of free HWID slots**; WireGuard/AmneziaWG clients gained **Keepalive**; the interface gained a **"Command Palette" on Ctrl+K**. The core is updated to **Xray-core v26.9.9**: on the first start, saved configurations are rewritten to its keys, and an empty **"Min Client Ver"** in REALITY now means "no lower bound". Below are the changes relative to 3.7.0, by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- **Xray-core 26.9.9 and the `tuic-server` 1.0.0 binary are bundled**, the latter for the new TUIC protocol: `install.sh` and `update.sh` install it into the panel's `bin/`, and it ships in the release archives and the Docker image (in Docker, publish the TUIC port as UDP). There are no prebuilt binaries for armv5/armv6/s390x — TUIC is unavailable there. Building from source requires Go 1.27.1.
- **Installation and updates verify the archive's SHA-256** against the published `.sha256` file, and `x-ui.sh`, `x-ui.rc` and the service unit files are taken from the same release's tag rather than from `main`.
- **One-time migrations on the first start:** the Xray template is rewritten to the new core's keys, the MTProto link address moves into a host, `subSortIndex` 0 → 1. **Back up the database before upgrading.**
- **The SQLite database is owner-only:** the `x-ui.db*` files are `0600` and the `/etc/x-ui` directory is `0700`. A new database (and a settings reset) gets random subscription paths.

### Changes in section 2 — Panel login and access security

- An invalid, disabled or expired **Bearer token gets HTTP 401** instead of 404 — the authentication failure is now visible. A request without the header and a request to a wrong base path still get 404.
- Login and logout lines in the log now follow a single format and contain the real username; a successful login is no longer logged twice.

### Changes in section 3 — Overview / Dashboard

- **"Command Palette" — Ctrl+K or ⌘K** ([3.17](#317-command-palette-ctrlk)): search for clients, inbounds, pages and settings tabs, copy a subscription, restart Xray (without confirmation) and switch the theme.
- **After a database import the panel restarts itself** — the subscription paths from the backup start working immediately.
- Updating geo files from the dashboard verifies SHA-256 and does not restart Xray if nothing has changed.

### Changes in section 4 — Inbounds: creation and common parameters

- **The inbound list shows the remarks of attached host groups** — multiple entry points (IPv4, IPv6, CDN) are visible without opening the inbound. Only enabled groups are taken into account, and search finds an inbound by them too.
- **"Subscription sort order"** accepts **negative values**: `-1` is enough to put an inbound first. `0` and an empty value are normalized to `1`, including in data saved earlier.

### Changes in section 5 — Protocols

- **A new protocol: TUIC v5** ([5.13](#513-tuic-v5)). The inbound is served by a separate `tuic-server` process behind the panel's UDP relay; the certificate is set right in the form, clients get a UUID and a password, and there are `tuic://` links and a Clash config. Limitations: traffic and limits are inbound-level only, it works on the local panel only, and any client change restarts the process and drops connections.
- **MTProto:** all links are built from managed hosts, so behind a reverse proxy clients get the correct external address and port. The former custom link address is moved into a host on upgrade.
- **AmneziaWG:** the default MTU is 1420 minus `S4`; the UDP socket binds to the listen IP; "Regenerate" sets single values for H1–H4; obfuscation parameters are validated against the bounds of `amneziawg-go`; clearing the header protection key applies to the running interface.
- **Hysteria2:** the link carries the standard obfs parameters (salamander/gecko) and `mport`; in xray-core 26.9.9 port hopping is performed by the client-side `udphop` mask.

### Changes in section 6 — Transport (Stream Settings)

- Hysteria's `proxy` masquerade mode gained an **"X-Forwarded headers"** field: `X-Forwarded-For`, `X-Forwarded-Host` and `X-Forwarded-Proto` are added to the proxied request.

### Changes in section 7 — Connection Security: TLS, XTLS, and REALITY

- **An empty "Min Client Ver" no longer means the built-in minimum.** In Xray-core v26.9.8 and newer (3.8.0 ships with v26.9.9) an empty field means "no lower bound": third-party cores such as Mihomo and sing-box connect without the `1.0.0` workaround. Explicitly set values work as before.
- **A TLS inbound cannot be saved without a certificate or key.** Every entry needs a certificate (a path or the content) and a private key, and at least one entry must be a server certificate. The check runs both in the form and on the server; incomplete entries saved earlier can still be edited.
- **The REALITY target scanner** shows the certificate chain size and warns when, with ML-DSA-65 enabled, the chain is shorter than 3500 bytes. "Find Targets" with an empty field checks the list from the new **"Reality scan candidates"** setting.
- A selected uTLS fingerprint of **None** is now kept — on save it used to silently revert to `chrome`. The Clash/Mihomo subscription enables ML-KEM support for REALITY (`support-x25519mlkem768`).

### Changes in section 8 — Clients

- **Keepalive for WireGuard/AmneziaWG clients** — the "Keepalive (seconds)" field: `25` in a new client's form, `0` disables it. A button that generates a **pre-shared key** (PresharedKey) now sits next to it.
- **Happ Encrypted Link** in the QR code window: the `happ://crypt5/…` link is generated locally on the panel server, with no external services. The option becomes available once **"Encrypted subscription links"** is enabled in the subscription settings (Happ → Subscription Links).
- **Bulk adjust** now also sets the **HWID Limit** (lowering it removes the excess devices) and the **MTProto ad-tag**.
- The HWID device list shows a **short fingerprint** — the first 12 characters of the identifier's hash.
- **TUIC** clients: a UUID and a password, and the QR code window offers **"TUIC config (Clash)"**; a per-client traffic quota is not supported for TUIC.
- A client on several tunnel inbounds keeps its keys and peer address on each of them, and its config is shown separately for each inbound.
- Fixes: auto-renew applies to all of a client's inbounds; an expiry at 23:59:59 on the day before the renewal day is moved to midnight without spending a renewal; an explicit `enable: false` is preserved on creation and import; a partially applied client operation marks Xray for a restart; a client's external links respect its expiry.

### Changes in section 9 — Client groups

- **"Adjust ({count})"** on the groups page applies every bulk-adjust field — Flow, the HWID limit and the MTProto ad-tag. Previously only days and traffic were applied, and the selected Flow was silently discarded.

### Changes in section 10 — Subscriptions (Subscription)

- **Happ client integration** ([10.7](#107-happ-client-integration)): with auto-detection enabled, the panel recognizes Happ by its User-Agent and sends it app-management headers — banners, migration to a new or fallback URL, TUN mode and engine, auto-connect, per-app proxy on Android, enforced HWID. Routing presets and a visual rule generator are included too.
- **A separate info config:** traffic and expiry are shown as a separate "dummy" config at the top of the list, and an expired or depleted subscription serves only the status config, built from configurable templates.
- **JSON subscription:** an embedded routing profile (JSON, a `happ://`/`incy://` deeplink or an HTTPS URL), custom **DNS servers**, a **"Block Connection"** tab; the client's local inbounds listen on `127.0.0.1`, and mux is off for Vision.
- **Clash/Mihomo:** AmneziaWG and TUIC proxies, ML-KEM for REALITY, extra `/mihomo/` and `/clash-legacy/` endpoints.
- **New installations get random subscription paths** (`subPath`, `subJsonPath`, `subClashPath`); an upgrade keeps the paths, and a settings reset creates new ones.
- The **`…/hwid-status`** endpoint reports how many device slots are taken and how many are left, without using up a slot; the device limit also applies to `?view=raw`.
- **Member weights** in leastLoad balancers: a member with a lower weight is picked more often.
- **Hosts:** MTProto links are built from hosts; REALITY parameters are dropped when a host forces TLS; a host's "Description" is passed to Happ as the server caption.
- The **"Month-end subscription expiry display"** option shows the end of a monthly subscription as the last second of the previous month; links of disabled and expired clients are left out of the output.

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **A new outbound protocol: AmneziaWG** ([details](#amneziawg-outbound)): the tunnel is brought up by the panel's embedded engine, and Xray sees such an outbound as a local SOCKS gateway at `127.0.0.1:64900` (the port is reserved). The obfuscation parameters must exactly match the server's.
- **One-time template conversions for xray-core 26.9.9** ([details](#one-time-template-conversions-on-upgrade-to-380)): `proxySettings` → `sockopt.dialerProxy`, the freedom strategy → `sockopt.domainStrategy`, a DNS outbound's `nonIPQuery`/`blockTypes` → `rules`.
- **Hysteria2 port hopping** is now set by the `udphop` UDP mask. Hysteria2 outbounds imported before 3.8.0 no longer hop ports — import the link again (ones from subscriptions update on their own).
- **NordVPN:** multiple NordLynx servers — one `nord-<hostname>` outbound per server; the load is shown in the list, **"Reset"** refreshes the key, and **"Log Out"** no longer deletes the added outbounds.
- Routing rules gained a **"Comment"** field — for the panel only; it is not passed to the core.
- **Subscription outbounds:** a custom **User-Agent** for providers that serve links only to "their own" clients; a server inserted in the middle of a subscription no longer takes over its neighbor's tag.
- Blackhole gained a `custom` response type with a **"Custom response (base64)"** field, and WireGuard a **"Remote DNS"** field; the useless port field is hidden for DoH servers; protocols in the template are read case-insensitively; VLESS with `vnext` can be tested; blackhole is no longer offered in MTProto's outbound picker.

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **Client changes go out to all nodes in parallel** — both single edits and bulk operations. A slow or unreachable node no longer holds up the request: anything that did not make it in time is applied by the background sync.
- **A node snapshot does not resurrect deleted clients** and cannot claim a client of another inbound.
- **Widening a node's inbound selection imports those inbounds instead of deleting them:** removal from a node waits one sync cycle.

### Changes in section 13 — Panel Settings

- A new **"Discord Bot"** tab ([13.11](#1311-discord-bot-discord-bot-tab--discord-bot)): token, channel, admin IDs, language, report schedule, events and CPU/RAM thresholds, a test notification button.
- **"Reality scan candidates"** on the "General" tab sets the list of targets that "Find Targets" checks when the search is empty.
- A settings reset generates new random subscription paths. The "Notification Time" field (Telegram and Discord) offers preset intervals or a custom cron expression.

### Changes in section 14 — Telegram Bot

- **A new Discord bot** ([14.8](#148-discord-bot)): notifications about panel events, a scheduled report with a database backup, and the `!status`, `!report`, `!backup`, `!usage`, `!inbounds`, `!restart` commands for the admins on the list.
- **Telegram bot:** a regular user's link buttons work only for that user's own clients; traffic reports arrive as a single message; each chat has its own new-client draft; the bot answers every button press.
- The bot shows an "after first use" expiry in days.

### Changes in section 15 — Geo databases (geoip / geosite and custom)

- **Standard geo files are checked against the published SHA-256** and installed all-or-nothing within a source. If the files have not changed, Xray is not restarted and connections are not dropped.
- The geodata auto-update editor has a **"Use standard sources"** button: it adds the missing standard files without touching your own rows.

### Changes in section 16 — Operations: backups, logs, updating, CLI

- **Back up the database before upgrading to 3.8.0** — the first start runs one-time migrations (see sections 1 and 11).
- `update.sh` verifies the archive checksum and takes the scripts from the release tag; **"Update Menu"** updates `x-ui.sh` from the installed version's tag.
- `/usr/local/x-ui/x-ui setting -getApiToken` accepts **`-tokenName <name>`** (default `cli-fallback`): the command reissues the token with exactly that name and leaves the others untouched.
- **Backups via the Discord bot:** the `!backup` command and scheduled reports with the database attached (`discordBotBackup`).
- The fail2ban backend setting is written to `jail.d`, and the `migrateDB` dump is created with `0600` permissions.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

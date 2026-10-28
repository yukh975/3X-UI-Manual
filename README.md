# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.11.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.11.0

Version 3.11.0 is a major release after 3.10.2. Highlights: the **Telegram bot has been rewritten** — one "live" screen instead of a stream of messages, a four-section menu, lists opened through inline search, notification cards, forum topics ([section 14](#14-telegram-bot)); **AmneziaWG** gained a kernel mode and a keepalive range; **subscription hosts** gained an SNI pool, random IPs from a CIDR, manual ordering and binding a client to its own hosts; **FinalMask** gained the Filter mask, a Lua script for Noise, DoH for xDNS and tlshello fragmentation presets; **TLS** gained cipher suite presets and a dynamic ECH helper; **XDRIVE** is now VLESS with encryption only; there is a new API token scope, **`node-admin`**, and a threshold for node-down notifications. The Xray core is **26.10.21**, and the interface is in 14 languages (Slovak added). Below are the changes relative to 3.10.2, by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- **First user with random credentials** ([1.4](#14-first-launch-and-default-credentials)): on a new database (Docker, manual start) the login and password are created at server start and printed once to the log; the fixed `admin`/`admin` is gone. `x-ui setting -show` shows `hasDefaultCredential: true` while there is no user.
- **Docker images for ARM and 386** ([1.3](#13-installation-methods)): the image gets the correct Xray and `mtg` binaries — ARMv6 gets the ARMv6 build, 386 gets the 32-bit one; an unknown architecture stops the build.
- **Xray core 26.10.21** ([1.3](#13-installation-methods)): 26.10.10 was withdrawn upstream.
- **Slovak interface** ([1.1](#11-what-is-3x-ui)): the panel is available in 14 languages, with `sk-SK` added.

### Changes in section 2 — Panel login and access security

- **Client address behind a proxy** ([2.3](#23-login-attempt-limiting-login-limiter--brute-force-protection)): `X-Forwarded-For` is read right to left, skipping trusted proxies, and `X-Real-IP` is accepted only when it matches; the proxy must overwrite `X-Real-IP` (for Caddy — `header_up X-Real-IP {remote_host}`). Otherwise, on a mismatch, the proxy's address becomes the login block key.
- **CSRF rejection is visible in the log** ([2.1](#21-login-form)): a request with a wrong token gets 403 and leaves a warning with the method, path and client address (#6692).

### Changes in section 3 — Overview / Dashboard

- **LXC container metrics** ([3.1](#31-general-data-collection-principles)): in LXC with LXCFS, CPU, swap and uptime are taken from the container rather than the host; unmeasurable values are shown as a dash instead of zero (#6920).
- **Public IPs are refreshed** ([3.9](#39-server-ip-addresses)): addresses are rechecked every 5 minutes, failed requests are retried with a growing delay, and a temporary failure does not erase the last known address (#6933).
- **Panel update via the API** ([3.12](#312-panel-update-3x-ui)): `POST /panel/api/server/updatePanel` is available to `admin` tokens and the new `node-admin` scope.
- **Accessibility** ([3.15](#315-additional-interface-elements)): the panel was checked for screen reader support (#6907).

### Changes in section 4 — Inbounds: creation and common parameters

- **Fallback: the PROXY protocol header is taken from the child inbound** (#6835, #6880; [4.5](#45-fallbacks)): if a fallback row has a child inbound selected, an empty **Dest** and no **Xver**, and the child inbound accepts PROXY protocol (`sockopt` or a RAW/WebSocket/HTTPUpgrade transport), `xver` `1` is written to the config. Previously, enabling Proxy Protocol on the child inbound broke the fallback: the master did not send the header and the child rejected every connection. Editing the child inbound's address, port or PROXY flag rebuilds the masters that depend on it.
- **Periodic reset re-enables clients disabled by quota** (#6833, #6834; [4.6](#46-periodic-traffic-reset)): after a reset, the inbound's clients that were disabled by an exhausted quota, and the inbound itself if it was turned off by its own traffic limit, are brought back into service. Previously the client showed zero usage but stayed out of the running core, and the inbound stayed disabled forever. An inbound disabled manually or by expiry stays disabled; an inbound on a node is not re-enabled automatically.
- **The advanced JSON editor preserves formatting** (#6857; [4.7](#47-inbound-json-advanced)): a line break or spaces in the **All** editor are no longer replaced with the panel's own formatting and no longer shift the cursor.
- **Deleting an inbound and clearing depleted clients go through the shared traffic-write queue** (#6912; [4.8](#48-inbound-actions-qr--edit--reset--delete-and-statistics)): on PostgreSQL the deadlock with the traffic poll is gone, and an inbound deleted while being edited no longer "resurrects".

### Changes in section 5 — Protocols

- **AmneziaWG: optional kernel mode** (#6877; [5.10](#kernel-mode)): the **Kernel mode** switch moves an individual inbound from the built-in engine to the Linux kernel module (`xui-awg<id>`, NAT in nftables, traffic bypasses Xray). Requires root, the `amneziawg` module, `awg`, `ip`, `nft`; the panel shows the reasons a host is not ready and the install command `x-ui install-awg-kernel`. Not supported: Xray routing and sniffing, peer IPv6, port forwarding and a pinned listen IP; the mode is unavailable in Docker. Traffic and quotas are accounted for as for other protocols; on a clean panel stop the interfaces are removed, after a crash they are picked up.
- **AmneziaWG: persistent keepalive range** (#6881; [5.10](#510-amneziawg)): in a client's **Keepalive (seconds)** you can enter a range such as `15-25` (0–65535). `.conf` and `vpn://` carry the range, Clash/Mihomo gets the lower bound, and plain WireGuard stays on a single number. Do not send ranges to older nodes.
- **AmneziaWG: faster client download through the built-in engine and a safe fallback bridge port** ([5.10](#510-amneziawg)): the receive TCP buffer scales up to 8 MB (at 50 ms RTT a single stream rose from about 310 to 500 Mbit/s), and if port `64900` of the local SOCKS5 bridge is taken, the fallback port is chosen below 62789 and does not take the panel's own ports.
- **WireGuard/AmneziaWG configs are validated line by line** ([5.9](#59-wireguard-inbound)): a value with a control character makes the `.conf` empty, a `vpn://` profile with wg-quick hooks is rejected, and the inbound form validates clients' **Allowed IPs** on create and edit.
- **TUIC: Xray routing by user** (#6875; [5.13](#513-tuic-v5)): the SOCKS5 bridge tells clients apart by email, so `user` rules work for TCP and UDP. Adding, deleting and renaming a client replaces only that inbound's bridge, without restarting Xray.

### Changes in section 6 — Transport (Stream Settings)

- **XDRIVE: VLESS with encryption only, service name `google-drive`** (Xray-core#7182; [6.10](#610-xdrive-xdrivesettings)): to meet xray-core 26.10.17's requirements, XDRIVE is offered only for VLESS, saving without **Decryption** is rejected, a client flow is not issued on XDRIVE (and is unavailable in the form, [5.3](#53-vless)), and selecting XDRIVE in an outbound turns on **Mux**. Previously saved inbounds and outbounds that the core now rejects are left out of the config (with a warning in the log) and do not stop the rest. The `Google Drive` service is now called `google-drive` (the old name is read as an alias).
- **Client XMUX for XDRIVE and MASQUE** ([6.10](#610-xdrive-xdrivesettings), [6.11](#611-masque-transport-masquesettings)): the panel no longer drops the optional `xmux` object when saving an inbound, and the JSON subscription passes it to clients; the form has no field for it — set it in the advanced JSON.
- **FinalMask: Filter mask (source IPs)** (Xray-core#7206; [6.12](#612-finalmask-transport-level-obfuscation)): in the inbound editor (TCP and UDP), the **Allowed Source IPs** and **Blocked Source IPs** lists cut off connections by source IP; links and the JSON subscription do not carry this mask.
- **FinalMask: tlshello fragmentation presets** ([6.12](#612-finalmask-transport-level-obfuscation)): in the client editors (outbound, hosts, the subscription's Final Mask JSON) the **Presets** list replaces the TCP masks with the ready-made `tlshello-0-len` or `tlshello-6-98`; the Fragment length check allows zero in `lengths` elements except the last.
- **FinalMask: Lua script for Noise and DoH for xDNS** (Xray-core#7124, Xray-core#7140; [6.12](#612-finalmask-transport-level-obfuscation)): the **Script** field replaces the noise list, and the xDNS resolver accepts `https://` addresses with the **Workers**, **DoH TLS** and **DoH QUIC** fields — previously saving lost everything except `addrs`.

### Changes in section 7 — Connection Security: TLS, XTLS, and REALITY

- **Cipher suites: presets and a fingerprint warning** ([7.3](#73-tls-mode)): the Cipher Suites field gained a Presets group (`semi-python`, `real-firefox`) — ready-made ordered lists of client suites; a preset replaces the list entirely. If suites are set with a uTLS fingerprint other than `unsafe`, the form warns that clients apply the suites only with `unsafe` and ignore them under any other fingerprint.
- **Dynamic ECH helper** (#6869, [7.3](#dynamic-ech-behind-cdn)): under the ECH config list field (formerly "ECH config") it builds a `domain+DoH URL` value from ready-made combinations or from your own domain and resolver, accepts only the `https`, `h2c` and `udp` schemes, and asks for confirmation before replacing a locally generated ECH key. The form also explains that local ECH keys do not work behind a CDN (Cloudflare behind the orange cloud) — the dynamic form is needed there. The same helper exists in hosts ([10.4](#104-output-formats)).
- **Fixed the description of the ML-KEM hint in REALITY links** ([7.4](#74-reality-mode)): a `vless://` link carries `support-x25519mlkem768=true` (the section previously claimed the parameter is absent from the link); for a host with the "Mihomo X25519" switch the hint is removed.

### Changes in section 8 — Clients

- **A client is bound to its own hosts** ([8.1](#host-rule-override)): the **Host Rule Override** field on the **Basic** tab restricts the client's subscriptions to the selected managed hosts. If no bound hosts remain, the client gets no links in that format but stays in traffic accounting (#6620).
- **AmneziaWG: keepalive range** ([8.1](#81-client-fields)): **Keepalive (seconds)** accepts `15-25`; `.conf` and `vpn://` carry the range, Clash/Mihomo gets the lower bound (#6881).
- **Client IPs are recorded even without Fail2ban** ([8.1](#81-client-fields)): with `XUI_ENABLE_FAIL2BAN=false` only the limit-based blocking is turned off, and the **IP Log** stays current (#6830).
- **Looking up a client by subscription ID via the API** ([8.3](#83-per-client-operations)): `GET /panel/api/clients/get/subId/:subId` (#6908).
- **Traffic reset returns clients to service** ([8.3](#83-per-client-operations)): an inbound's periodic reset and **Reset all client traffic** re-enable clients disabled by quota; an inbound turned off by its own limit is re-enabled by the periodic reset (#6833, #6834).

### Changes in section 10 — Subscriptions (Subscription)

- **Host: SNI pool** (#6923, [10.4](#104-output-formats)): a host's SNI field can hold several values — each config gets a random SNI from the pool, and the "Same random SNI for all configs" switch picks one SNI for the whole host in each subscription request. No separate host per domain is needed; a host with a single SNI is served as before.
- **Host: random IPs from a CIDR range** (#6784, [10.4](#104-output-formats)): a host's address can be a CIDR (IPv4 or IPv6), and the "Random IP count" field (1–100, default 1) sets how many unique addresses from the range each subscription request gets. The range is expanded in all formats, in both subscription orders, in QR codes and in tunnel config exports.
- **Host order in the subscription and drag-and-drop** (#6894, #6895, [10.2](#102-subscription-server-settings)): the new "Subscription Node Ordering" setting (`subHostSortMode`) with the "Hosts order" mode lines up raw, JSON and Clash subscriptions in the order of the Hosts page across all inbounds (by default the order is as before — within each inbound). Rows of the hosts table can be dragged, not just moved with the Up/Down buttons.
- **Binding a client to hosts** (#6620, [10.4](#104-output-formats)): a client gets in subscriptions only the hosts bound to it (the "Host Rule Override" field in the client form, API: `clientHostRuleIds`). The binding fails closed — a client with no matching hosts gets no links but stays in traffic accounting. Deleting a host closes the binding only on its inbound, not on all of the client's inbounds.
- **An inbound's external proxy carries over to imported hosts** (#6831, [10.4](#104-output-formats)): an `externalProxy` edit made while updating an inbound now reaches the subscription — previously the update returned 200 but subscriptions kept serving the old address, port and security. Hosts that the administrator changed, disabled, deleted or made shared are not affected.
- **Cipher suites in links: `cs` and `fp=unsafe`** (#6825, [10.4](#104-output-formats)): share links of a host or TLS inbound carry the `cs` parameter, and with an empty fingerprint `fp=unsafe` is added — otherwise the suites do not take effect in v2rayN and other Xray-based clients. Previously the cipher suites reached only the JSON and Clash subscriptions.
- **The host's "Mihomo X25519" switch removes ML-KEM** (#6803, [10.4](#104-output-formats)): for a REALITY host, the Clash proxy gets `support-x25519mlkem768: false` and the `vless://` link is without the hint. Previously the switch was saved but had no effect, and all REALITY proxies carried `true`; the stored values were reset once on update so that subscriptions do not change silently. A REALITY host's fingerprint now reaches Clash and JSON, and an empty SNI, fingerprint, Host and path of one host are not inherited from another.
- **Shadowsocks with a TCP HTTP header in Clash/Mihomo** (#6838, [10.4](#104-output-formats)): such a node is emitted with `plugin: obfs` (`mode: http` and the Host header) if the header accepts the path `/`; previously it was skipped.
- **XMUX numbers in Clash** (#6843, [10.4](#104-output-formats)): an inbound's numeric XMUX parameters, for example `maxConnections` (default `3` in the panel), now reach `reuse-settings` — previously only string values were passed.
- **DNS from remote Clash rules** (#6868, [10.4](#104-output-formats)): the new "Use DNS from remote rules" switch (`subClashRemoteDNS`, off by default) carries the `dns` and `sniffer` sections of the template that the global rules link points to into the profile; enable it only for a template you trust.
- **No caching on all subscription routes** (#6862, [10.4](#104-output-formats)): raw, JSON, Clash, `/mihomo/` and `/clash-legacy/` responses are served with `Cache-Control: no-cache, no-store, must-revalidate`, so a CDN or proxy in front of the subscription server does not serve stale traffic, expiry and rules. In addition, inbound settings without the client list are cached for 10 s, and on installations with 100 thousand clients a subscription request reads them dozens of times faster (#6758).

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **Lua scripts: what the panel saves** ([11.14](#1114-lua-scripts-for-routing-and-dns)): a template with `routing.script` and `dns.script` together with fallback/parallel switches or servers with domains is rejected on save; such scripts in old templates are dropped with a warning when the config is built (xray-core v26.10.21; Xray-core#7124, Xray-core#7136).
- **XDRIVE in an outbound — VLESS only** ([11.4](#114-outbounds-outgoing-connections)): selecting XDRIVE turns on Mux, `flow` is not written, outbounds the core does not accept are skipped with a warning; the storage service is called `google-drive` (Xray-core#7182).
- **A private DoH server works** ([11.6](#116-dns)): the auto-rule for a private DNS server opens the port from the URL (443 by default) for `https://` and `h2c://`, not 53 (#6918).
- **The TCP check understands IPv6** ([11.4](#114-outbounds-outgoing-connections)): an outbound with an IPv6 address without brackets is no longer marked unavailable (#6850).

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **The "Node administrator" token** ([12.2](#122-adding-and-editing-a-node)): the `node-admin` scope includes the `node-sync` permissions and lets the master update the node's panel; `node-sync` does not allow updating (#6666).
- **Threshold for node-down notifications** ([12.7](#127-how-inbounds-and-clients-are-synchronized)): `node.down` is sent after the set number of consecutive failed checks, by default after one (#6768).
- **A node's disable does not stick** ([12.7](#127-how-inbounds-and-clients-are-synchronized)): if the master allows a client, an accidental "disabled" from the node does not flip the client between states (#6870).
- **A recreated client does not vanish from the node** ([12.7](#127-how-inbounds-and-clients-are-synchronized)): re-adding a node inbound with a just-deleted email clears the deletion mark.

### Changes in section 13 — Panel Settings

- **Proxy and client address** ([13.4](#134-session-panel-proxy-and-trusted-proxies-proxy-and-server-tab--proxy-and-server)): describes how the panel chooses the client address from `X-Forwarded-For` and `X-Real-IP`, and adds a Caddy example with `header_up X-Real-IP {remote_host}`.
- **Forum topic for bot notifications** ([13.5](#135-telegram-bot-telegram-bot-tab--telegram-bot)): in "Admin Chat ID" you can specify `chatId:topicId`, and notifications go to the given topic of a forum supergroup.
- **Bot setup warnings** ([13.5](#135-telegram-bot-telegram-bot-tab--telegram-bot)): the test message checks the bot's capabilities and warns if inline mode is off or privacy mode is on.
- **Node notification threshold** ([13.5](#135-telegram-bot-telegram-bot-tab--telegram-bot)): `nodeDownThreshold` (default 1) delays `node.down` until the set number of consecutive failed checks (#6768).
- **The `node-admin` token scope** ([13.9](#139-administrator-account-and-api-tokens)): a node token that is additionally allowed to update the node's panel; token lookup by index reduces load (#6666, #6915).

### Changes in section 14 — Telegram Bot

- **The bot is rebuilt around one "live" screen** ([14.2](#142-main-menu-and-buttons)): taps edit a single message with a picture and a keyboard, the path "Panel › …" sits above the text, every screen has "⬅️ Back", and long text is paged ("Page X of Y", caption limit 1024 characters). The administrator's main menu is four sections (🖥 Server, 👥 Clients, 🚦 Traffic, ⚙️ Maintenance) and "🔄 Refresh" (#6760).
- **Inbound and client lists open through inline search** ([14.2](#142-main-menu-and-buttons)): the "🔍 Find inbound…" / "🔍 Find client…" buttons. Inline mode must be enabled once in @BotFather with `/setinline` ([14.1](#141-enabling-and-configuring-the-bot)); while it is off, the bot shows "⚠️ Inline mode is off" with instructions and a "Check again" button, and panel settings show the warning "Inline mode is disabled" after the "Send Test Message" button (request `POST /panel/api/setting/tgBotCapabilities`) (#6760).
- **The bot works in private chats only** ([14.1](#141-enabling-and-configuring-the-bot)): in groups and channels it replies "🤖 This bot works in private chat only…", and group Privacy mode is now just an informational warning "Group Privacy is on" (#6760).
- **The "/" menu contains only `/start`; the "Commands" button is removed** ([14.3](#143-bot-commands)): the other commands work if typed manually. Actions are grouped by section, and ♻️ Restart Xray and 📢 Broadcast buttons are added (#6760).
- **Notifications are live cards** ([14.5](#145-notifications-and-reports)): a repeat of an event within 30 minutes edits the same message and counts "🔁 repeated N× · last HH:MM:SS", every message has "🙈 Hide"; the separate rate limiter is removed; successful and failed logins are different cards. A periodic report replaces the previous one instead of piling up (#6760).
- **The "➕ New client" wizard starts with a draft** ([14.4](#144-client-management-administrator-only)): inbounds are chosen with the "Attach inbound (N)" button with a checklist and "✅ Done", so a client can be attached to several inbounds at once; after creation the client card opens (#6760).
- **QR codes are one sheet image** with a numbered legend "🔳 QR codes:" instead of several messages ([14.2](#142-main-menu-and-buttons)); the DB backup arrives as one message with a caption and `config.json` ([14.6](#146-backup-and-logs)) (#6760).
- **Administrator notifications can be directed to a forum topic** ([14.1](#141-enabling-and-configuring-the-bot)): in the "Admin Chat ID" field, `:topicId` is appended to the chat ID, for example `-1001234567890:42`. Topic 1 equals General; two different topics of one chat is an error (#6879).
- **Client lookup by Telegram ID uses the indexed clients table** ([14.3](#143-bot-commands)): the bot determines the access level faster on panels with many clients (#6887).
- **3.11.0 limitations** ([14.4](#144-client-management-administrator-only), [14.6](#146-backup-and-logs)): the bot no longer gives an administrator other clients' links and QR codes (the admin links menu is removed, the client card has no such buttons) — take them from the panel; "📄 Get Ban Logs" sends only the previous journal `3xipl-banned.prev.log` (#6984, #6990).

### Changes in section 16 — Operations: backups, logs, updating, CLI

- **Clean service stop** ([16.5](#165-restarting-and-updating-the-panel)): the units use `KillMode=mixed`, the panel itself stops Xray and the helper processes, and no false termination error is written to the journal (#6884).
- **Client IPs with fail2ban off** ([16.3](#163-xray-logging-level-and-configuration)): the panel keeps recording addresses; limit-based blocking still requires fail2ban (#6830).
- **The `node-admin` scope in the CLI** ([16.7](#167-console-menu-and-cli-x-ui)): `x-ui setting -getApiToken -tokenScope node-admin`.
- **AmneziaWG kernel module** ([16.7](#167-console-menu-and-cli-x-ui)): the `x-ui install-awg-kernel` command builds and installs the module via DKMS for AmneziaWG kernel mode.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.10.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.10.0

Version 3.10.0 is a feature release. The headline: a new **MASQUE** protocol — an IP tunnel over HTTP/3 or HTTP/2 ([5.15](#515-masque)) — and with it **WARP over MASQUE**, straight from the WARP window; a new **XDRIVE** transport that carries the stream as files through Google Drive, a local folder, or any HTTP storage ([6.10](#610-xdrive-xdrivesettings)); and **Lua scripts for routing and DNS** ([11.14](#1114-lua-scripts-for-routing-and-dns)). Client-side port hopping is now configured with the **UDP Hop** UDP mask, and Final Mask gained Header Custom variables, Sudoku for UDP, and a Reset range for Noise. The systemd service **runs in a sandbox** (#6718), the installer sets up **PostgreSQL 18 from PGDG**, and node sync is more robust: an empty node snapshot no longer deletes clients (#6734), and client edits are applied on the node without dropping connections. The core is updated to **Xray-core v26.10.10**: it verifies TLS certificates against built-in root certificates (for your own CA there is a "Use system CA" toggle), and on the first start the configuration is rewritten once to match its keys. ⚠️ **Shadowsocks-2022 inbounds using the `2022-blake3-chacha20-poly1305` method are switched to `aes-256-gcm` — their clients' links change.** Build requirements: Go 1.27.2, Xray-core v26.10.10. Below are the changes relative to 3.9.0, by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- **Bundled with Xray-core 26.10.10** (instead of 26.9.30); building from source requires Go 1.27.2, while installing from packages and the script is unaffected. The new core verifies the TLS certificates of outbound servers against Mozilla's built-in root certificates rather than the system store; for a server with a private CA, the outbound's TLS settings have a "Use system CA" toggle (`useSystemCA`).
- **One-time migrations on the first start of 3.10.0:** the XDNS masks are converted to the new core's `names`/`addrs` format (`XdnsFinalmaskNamesAddrsFix`), the legacy `quicParams.udpHop` in client-side masks is replaced by the `udphop` mask (`UDPHopClientMaskFix`), and on hosts the leftover checkbox-era values `0`/`1`/`false`/`true` of the "Verify peer cert by name" field are cleared (`HostVerifyPeerCertByNameBoolFix`). Shadowsocks inbounds using `2022-blake3-chacha20-poly1305` are switched to `2022-blake3-aes-256-gcm`, and an SS-2022 server key of the wrong length is replaced — **the links of these inbounds change**. **Back up the database before upgrading.**
- **The local PostgreSQL is now installed as version 18 from the official PGDG repository** (apt on Debian/Ubuntu, dnf on the RHEL family 8+). Where PGDG has no build, the distribution package is installed as before; an existing cluster is left untouched.
- **A WireGuard outbound in Docker no longer crashes Xray** (#6796): where a kernel TUN cannot be created (in a container with `NET_ADMIN` but without `/dev/net/tun` and with a read-only `/proc/sys`), the panel switches WireGuard outbounds to the userspace TUN (`noKernelTun`) on its own.

### Changes in section 2 — Panel login and access security

- **The LDAP sync schedule accepts a standard five-field crontab** (for example, `30 8 * * *`) alongside the six-field form, `@every`, and `@daily`/`@hourly`/…: previously such a value was saved, but the sync silently never ran. An unrecognized schedule is now rejected on save, and one saved earlier is replaced at startup with the default `@every 1m`, with a warning in the log.

### Changes in section 3 — Overview / Dashboard

- **The panel update confirmation dialog closes immediately** after clicking "Confirm" (#6766): from then on only the "Installation is in progress, please do not refresh this page" indicator is shown, instead of a confirmation that hangs until the update finishes.

### Changes in section 5 — Protocols

- **New MASQUE protocol** ([5.15](#515-masque)): a CONNECT-IP tunnel over HTTP/3 or HTTP/2 with mandatory TLS (xray-core v26.10.10). Clients sign in with an email and password (HTTP Basic); the inbound has an "Address pool" (`10.14.0.1/24`, `fd14::1/64` by default), an MTU, and a request path. Quotas, expiry, "IP Limit", and live client edits work as with other Xray protocols; depending on the ALPN, the inbound takes UDP (`h3`), TCP (`h2`), or both. There is no share link — the client gets its configuration from the JSON subscription. It can be deployed on a node (node panel v3.9.1+, i.e. 3.10.0). The email of a MASQUE inbound's client cannot contain ":".
- **VLESS: Vision inside VLESS encryption on any transport** ([5.3](#53-vless)): with `encryption`/`decryption` enabled, the `xtls-rprx-vision` flow is available on any network, not only XHTTP. If the transport cannot carry Vision, the panel strips the clients' flow from the server config — previously a leftover flow made the server reject every client.
- **Shadowsocks: the `2022-blake3-chacha20-poly1305` method is removed from inbounds** ([5.6](#56-shadowsocks)): the core cannot bring up a multi-user inbound with it, which kept the whole of Xray from starting. On the first start of 3.10.0 such inbounds are switched to `2022-blake3-aes-256-gcm` (the keys are kept, but the clients' links change — refresh the subscriptions); the method remains available for outbounds. A Shadowsocks inbound is now always multi-user — the single-user QR code in the inbound row and the link block in the info window are removed.
- **Shadowsocks-2022: the server key length is validated** ([5.6](#56-shadowsocks)): 16 bytes for `aes-128-gcm`, 32 for `aes-256-gcm`. A key of the wrong length (for example, one sent via the API) is no longer saved and no longer crashes Xray; an invalid key that is already saved is replaced with a new one at startup.
- **TUN: "Adapter type", "System DNS to gateway", and "Block leaks (WFP)"** ([5.1](#51-list-of-supported-protocols)): the xray-core 26.9 parameters `desc` (Windows), `autoSystemDnsToGateway` (Linux), and `autoSystemWfpBlockLeak` (Windows: `dns`, `misconfigtun`) can now be set in the TUN inbound form.
- **TUIC:** sniffing on the bridge into Xray no longer overrides the destination IP requested by the client — the domain is used for routing only (`routeOnly`) (#6753); the speed of TUIC clients is shown on the clients page again, and the certificate buttons no longer overflow the form (#6723) ([5.13](#513-tuic-v5)).
- **AmneziaWG:** UDP replies to a peer respect the tunnel MTU — large datagrams are fragmented instead of being sent over the MTU (#6780) ([5.10](#510-amneziawg)).
- **WireGuard + AmneziaWG on the same client:** the WireGuard peer now gets the public key and keepalive of its own WireGuard inbound rather than the AmneziaWG tunnel's, so such a WireGuard tunnel connects again (#6751) ([5.9](#59-wireguard-inbound)).

### Changes in section 6 — Transport (Stream Settings)

- **New XDRIVE transport** ([6.10](#610-xdrive-xdrivesettings)): the stream is carried as files in a shared storage folder — Google Drive, a local folder, or any HTTP API described by a template — with an optional fronting address and core tuning parameters. There are no links, QR codes, or Clash output for it: clients get the configuration, together with the storage secrets, from the JSON subscription; on the inbound, security is always "None".
- **An incomplete XDRIVE setup no longer crashes Xray** ([6.10](#610-xdrive-xdrivesettings)): the folder, the three Google Drive secrets, and the template operations (`put`/`get`/`list`/`delete` with `url`, `namesRegex` with a capture group) are validated when the inbound and the Xray template are saved, not when the listener starts.
- **MASQUE transport** ([6.11](#611-masque-transport-masquesettings)) for the new MASQUE protocol ([5.15](#515-masque)): it is set automatically, and on the server only the **Path** is configured (`/.well-known/masque/ip/*/*/` by default); TLS is mandatory, and the ALPN selects the listeners — `h3` (HTTP/3 over UDP, the default) and/or `h2` (HTTP/2 over TCP).
- **The client-side UDP Hop UDP mask** ([6.12](#612-finalmask-transport-level-obfuscation)): since xray-core 26.9.9, port hopping works only through the `udphop` mask (modes, interval, the server's ports and IPs); the panel converts the legacy client-side `quicParams.udpHop` into it (the `UDPHopClientMaskFix` migration) and keeps a single `udphop` at the end of the UDP mask list — otherwise the client could not connect. On an inbound, the **UDP Hop** toggle merely advertises the range to clients.
- **FinalMask: variables and Errors in Header Custom, Sudoku for UDP, a Reset range for Noise** ([6.12](#612-finalmask-transport-level-obfuscation)): Header Custom items can store bytes in a variable (**Capture**), repeat it (**Reuse variable**), or set an expression (**Transform**); the TCP mask has an **Errors** group, and the UDP mask a **Mode** of Prefix/Standalone; Sudoku is available as a UDP mask; Noise's **Reset** accepts a range such as `60-120`. Previously such keys from a hand-written config were lost on the next save.
- **A Salamander password shorter than 4 bytes is rejected** ([6.12](#612-finalmask-transport-level-obfuscation)): the core failed to open such a socket only after the config check had passed, and an inbound with a short password stopped the whole of Xray. The check runs in the editor and when saving the inbound, hosts, the subscription Final Mask, and the Xray template.
- **xDNS in the Xray-core 26.10.10 format** ([6.12](#612-finalmask-transport-level-obfuscation)): domains are given as a **Names** list, resolvers as a list of `udp://`/`tcp://` URLs, and **Record Types** are optional. Saved masks are rewritten by the `XdnsFinalmaskNamesAddrsFix` migration; clients on an older core cannot read the new format.

### Changes in section 7 — Connection Security: TLS, XTLS, and REALITY

- **TLS on WebSocket: the default ALPN is `http/1.1`** ([7.3](#73-tls-mode), #6787): with the previous default of `h2, http/1.1` the server negotiated h2 and the WebSocket handshake failed (#6782). The new value is set when TLS is enabled on WebSocket and when a TLS inbound is switched to WebSocket; saved inbounds are not changed.
- **Security for the new transports** ([7](#7-connection-security-tls-xtls-and-reality)): MASQUE offers only **TLS** (ALPN `h3`, uTLS **None** by default; the ALPN determines the listeners, see [6.11](#611-masque-transport-masquesettings)), and an inbound on XDRIVE offers only **None** (see [6.10](#610-xdrive-xdrivesettings)).

### Changes in section 8 — Clients

- **The auto-renewal preview is clearer** ([8.1](#81-client-fields), #6662): dates are shown as `YYYY-MM-DD HH:MM:SS UTC±HH:MM` in the panel's time zone (accounting for daylight saving time), the heading names that zone ("Server local time" when it is `Local`), and the "Estimated renewals used" counter is an estimate of how much of the limit will be used, not renewals already performed. The client preview does not renew anything; the calculation and the saved values are unchanged.
- **The auto-renewal form is rearranged** ([8.1](#81-client-fields), #6672): the mode, the day/interval field, and "Max renewals" sit in one row, the explanation depends on the selected mode (the end-of-month note appears only for the monthly one), and the outdated "0 = disabled" is gone from the hints.
- **The email of a client on a MASQUE inbound cannot contain `:`** ([8.1](#81-client-fields)): MASQUE passes the email as the Basic-auth username, and such an email brought down the whole inbound along with the Xray startup. The panel now rejects it on creation, attach, bulk operations, import, and inbound edits; nothing changes for other protocols.
- **The QR code is hidden only for links with a post-quantum key** ([8.3](#83-per-client-operations), #6730): a non-empty `pqv` or an ML-KEM-768 VLESS encryption key. REALITY links with the ML-KEM hint and VLESS encryption with an X25519 key get a QR code again — in the client windows, on the inbound, and on the subscription page.
- **The "Attach Clients To…" / "Detach Clients" windows on the Inbounds page** ([8.2](#82-inbound-binding), #6736) show the inbound's clients right on first open — previously the table stayed empty until the window was reopened.

### Changes in section 10 — Subscriptions (Subscription)

- **A host's "Description" reaches Happ in Hysteria/Hysteria2 links too** ([10.7](#107-happ-client-integration), #6740): the `?serverDescription=` server caption is appended to the name the same way as for VLESS/Trojan/Shadowsocks, instead of the standard "Hysteria | hysteria | TLS".
- **JSON subscription: host TLS verification works again** ([10.4](#104-output-formats), #6743): ECH, "Verify peer cert by name", and the host's pinned SHA-256 are emitted at the top level of `tlsSettings`, where Xray reads them; previously they were lost, and connections through such a host failed.
- **JSON subscription: a `udphop` mask for every host** ([10.4](#104-output-formats)): for a Hysteria inbound with port hopping and several hosts, only the first host used to get the hopping; now all of them do.
- **VLESS without a saved `encryption` is emitted with `none`** ([10.4](#104-output-formats), #6781): inbounds from older versions or added via the API produced `"encryption": ""` in the JSON subscription, and Xray would not load the config; the `vless://` link now carries `encryption=none` too.
- **XDRIVE and MASQUE are delivered only via the JSON subscription** ([10.4](#104-output-formats)): inbounds with the XDRIVE transport and of the MASQUE protocol have no share link (neither in the regular subscription, nor in the panel's QR codes, nor in Clash/Mihomo). ⚠️ The JSON subscription hands every client of an XDRIVE inbound the entire `xdriveSettings` block, including the storage secrets (for Google Drive — Client ID, Client Secret, Refresh Token).
- **The subscription page follows the panel theme** ([10.5](#105-subscription-info-page-and-qr-codes)): the colors of the light, dark, and ultra-dark themes and the panel's blue accent replace its own purple-and-teal palette with an animated background; the content is unchanged. The QR code for REALITY and X25519-encryption links is shown on the page again (see section 8).

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **Lua scripts for routing and DNS** ([11.14](#1114-lua-scripts-for-routing-and-dns)): new fields **"Routing Script"** (`routing.script`) in "Basics", **"Lua Script"** (`dns.script`) in DNS, and an **ID** on a DNS server — the path to a `.lua` file for Xray-core 26.10.10 scripts. A routing script replaces all rules, including the internal `api` rule (which the script itself has to route); without the file Xray will not start. Keys entered into the JSON by hand are no longer lost on save.
- **WARP over MASQUE** ([11.8](#118-wireguard--warp--nordvpn)): the **"Add WARP over MASQUE outbound"** button in the WARP window registers a separate WARP device with an ECDSA P-256 key and creates (or updates) the `warp-masque` outbound; the WireGuard WARP registration is not affected.
- **A balancer target override is no longer reset** when the Xray settings are saved or a node is tested through an outbound ([11.5](#115-balancers), #6779): the panel restores it after a hot reload of routing, rejects a target that is not in the running configuration, and clears the override when the target outbound is deleted. Restarting Xray still resets it.
- **One-time migrations for Xray-core 26.10.10** ([11.11](#1111-saving-restart-and-automatic-transformations)): the XDNS masks are converted to the `names`/`addrs` format (`XdnsFinalmaskNamesAddrsFix`, which supersedes `XdnsFinalmaskObjectsFix` from 3.9.0), and the old `quicParams.udpHop` on outbounds, hosts, and in the JSON subscription becomes the `udphop` mask (`UDPHopClientMaskFix`). Clients with a core older than 26.10.10 need a new Xray. **Back up the database before upgrading.**
- **UDP Hop on an outbound is now the `udphop` mask** ([11.4](#114-outbounds-outgoing-connections)): the toggle in the outbound's QUIC parameters is replaced by the **UDP Hop** UDP mask (modes, interval, remote ports and IPs), available for Hysteria2 and XHTTP; old settings are converted automatically, with no need to re-import links; the panel keeps a single `udphop` mask last in the list, otherwise the core cannot connect.
- **The "Use system CA" toggle** (`useSystemCA`) in the outbound's TLS ([11.4](#114-outbounds-outgoing-connections)): Xray-core 26.10.10 verifies certificates against Mozilla's built-in root certificates, so for a server with a private CA installed into the system, the system store has to be enabled explicitly.
- **MASQUE outbound** ([11.4](#114-outbounds-outgoing-connections), protocol — [5.15](#515-masque)): a new protocol in the outbound form — address, port, **Remote DNS**; the `masque` transport with TLS is set automatically.
- **TLS for XDRIVE outbounds** ([11.4](#114-outbounds-outgoing-connections)): SNI, the uTLS fingerprint, and ALPN configure the HTTPS connection to the storage API; previously TLS was not offered for XDRIVE and was silently dropped.

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **Clients attached on the master reach nodes with an `admin` token** ([12.2](#122-adding-and-editing-a-node)): the master tags its requests with the `X-3x-Master-Push` header, and the node applies the pushed clients just as with a `node-sync` token. In 3.9.0 such nodes silently kept their previous clients. The header is read by the node — **upgrade the nodes to 3.10.0**. An inbound deleted directly on the node is now recreated by the master.
- **The `node-sync` token (and mTLS) covers every call from the master** ([12.2](#122-adding-and-editing-a-node)): the inbound order in the subscription, the bulk client traffic reset, and the request for active inbounds used for online attribution reach the node again (previously HTTP 403).
- **A MASQUE inbound can be deployed on a node** ([12.7](#127-how-inbounds-and-clients-are-synchronized)): the threshold in the code is node v3.9.1+, in practice 3.10.0.
- **Client edits are applied on the node without dropping connections** ([12.7](#127-how-inbounds-and-clients-are-synchronized), #6795): if only the clients changed in the pushed inbound, the node adds and removes them one by one through the Xray API instead of recreating the inbound (`vless`, `vmess`, `trojan`, `hysteria`, `masque`; AmneziaWG — in place, like MTProto and TUIC).
- **An empty node snapshot no longer deletes clients** ([12.7](#127-how-inbounds-and-clients-are-synchronized), #6734): a snapshot without clients for an inbound that has clients on the master is not treated as authoritative — the master deletes nothing and pushes the clients to the node again.
- **Stats for detached clients from a node are ignored** ([12.7](#127-how-inbounds-and-clients-are-synchronized), #6724): the stale usage of a detached client no longer disables it on the master or restores its previous quota.
- **Traffic history is kept when a node's inbound is replaced** ([12.7](#127-how-inbounds-and-clients-are-synchronized), #6749): when an inbound is adopted under a new tag, the clients' traffic rows are carried over rather than reset to zero.
- **On PostgreSQL, node traffic sync no longer hangs the panel** (#6789): the lookup of shared emails runs inside the open transaction and does not wait for a free connection from the pool.

### Changes in section 13 — Panel Settings

- **The report and LDAP sync schedules accept a 5-field crontab and are validated on save** ([13.5](#135-telegram-bot-telegram-bot-tab--telegram-bot)): `tgRunTime`, `discordRunTime`, and `ldapSyncCron` are parsed with an optional seconds column (`30 8 * * *` and `0 30 8 * * *` are equivalent), an unrecognized value is rejected with the error `… cron schedule <…> is not valid`, and an unparseable value saved earlier is replaced with the default, with a warning in the log, instead of silently disabling the job.

### Changes in section 14 — Telegram Bot

- **A scheduled report no longer silently goes missing** ([14.5](#145-notifications-and-reports)): the "Notification Time" of the Telegram and Discord bots also accepts a standard 5-field crontab (previously it was saved, but the report was never scheduled), an invalid expression is rejected on save, and an unparseable old one is replaced with `@daily`, with a warning in the log.

### Changes in section 16 — Operations: backups, logs, updating, CLI

- **The database migration runs before the service starts** (#6729): `update.sh` runs `x-ui migrate` before starting the service, so the service no longer fails during an upgrade because of concurrent migrations (for example, "duplicate column name: exclude_from_sub" when going from 3.8.5 to 3.9.0).
- **Updating the panel leaves TLS alone:** `update.sh` no longer opens the SSL menu on a panel without a certificate (during a web update this could issue an IP certificate or delete `/root/cert/ip` and the acme.sh state) and no longer waits for an IP to be entered manually; "Access URL" shows `https://` only when a certificate is configured.
- **systemd service sandbox** (#6718): write restrictions on `/usr`, `/etc`, `/boot`, `/efi`, and home directories, reduced root capabilities, `UMask=0077`, and a system call filter on systemd 239+. Put your own settings into a separate drop-in (for example, `20-x-ui-local.conf`); `/proc/sys/net` is left writable for WireGuard with a kernel TUN. The web-update fallback path without `systemd-run` stops immediately inside the sandbox with a clear message; `x-ui uninstall` removes the whole `x-ui.service.d` directory.
- **The PostgreSQL menu installs PostgreSQL 18 from PGDG** (like the installer), manages the `postgresql-18` service on the RHEL family, and on a full PostgreSQL removal also uninstalls the PGDG packages.
- **Back up the database before upgrading** — the first start runs one-time migrations (the XDNS and `udphop` masks, the certificate verification field on hosts, the Shadowsocks-2022 method and keys; see section 1).

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

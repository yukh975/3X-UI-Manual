# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.10.2**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.10.2

Version 3.10.2 is a bug-fix release after 3.10.0 (there was no separate 3.10.1 release). Highlights: **Shadowsocks** client edits are applied on the fly and no longer drop the connections on the port ([5.6](#56-shadowsocks)); MTProto gains a **per-IP limit on pending handshakes** ([5.12](#512-mtproto-telegram-proxy)); importing **VMess links** no longer loses the XHTTP and mKCP settings ([11.4](#114-outbounds-outgoing-connections)); the Clash/Mihomo subscription exports **Hysteria2 with Gecko obfuscation** ([10.4](#104-output-formats)); Incy routing no longer mixes with the Happ headers. The core is unchanged — **Xray-core v26.10.10** — and there are no one-time database migrations. Below are the changes relative to 3.10.0, by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- **The Windows build is now named `3x-ui.exe`** (instead of `x-ui.exe`) and carries version information and an icon: a bare Go executable without them triggers more antivirus false positives.

### Changes in section 3 — Overview / Dashboard

- **The sidebar no longer has a sponsor card**, and the Sponsors page lists only real sponsors (the "Your brand here" placeholder appears only when the list is empty). The panel now fetches the sponsor data from `raw.githubusercontent.com` instead of `sponsors.sanaei.dev`: that hostname is unique to 3x-ui, travelled in plaintext SNI, and let an on-path observer identify a server running the panel (#6824).

### Changes in section 5 — Protocols

- **Shadowsocks: client changes are applied on the fly** ([5.6](#56-shadowsocks)): adding, deleting, renewing, resetting traffic for and auto-disabling a client of a multi-user Shadowsocks inbound — by an edit in the panel, by a master panel's push to a node, or by a hot config apply — no longer rebuild the inbound. Previously this closed the port and dropped every live connection on it.
- **MTProto: "Max pending handshakes per IP"** ([5.12](#512-mtproto-telegram-proxy)) — new field `settings.pendingHandshakesMaxPerIp` (default `0` — off): new connections from an IP that already has this many unfinished handshakes are closed. It protects against handshake floods; clients behind a shared IP (carrier NAT) share the limit. Requires `mtg-multi` 1.16.0 or later; changing the field restarts that inbound's `mtg` process.

### Changes in section 10 — Subscriptions (Subscription)

- **Hysteria2 with Gecko obfuscation in Clash/Mihomo** ([10.4](#104-output-formats)): a Salamander mask with a packet-size range is exported as `obfs: gecko` with `obfs-min-packet-size`/`obfs-max-packet-size`. Previously only the password reached the YAML — i.e. plain salamander — and the client could not complete the handshake with a Gecko server.
- **Incy routing is isolated from the Happ headers** (#6810, [10.2](#102-subscription-server-settings)): an Incy client that receives the Incy routing line no longer gets the Happ routing headers (`Routing-Enable`, `Routing`).

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **`vmess://` links are parsed completely** (#6808, #6809; [11.4](#114-outbounds-outgoing-connections)): when importing an outbound, in outbound subscriptions and in a client's external links, the XHTTP fields that VMess carries directly in the link's JSON (session/seq placement, padding obfuscation, xmux, etc.), the Finalmask (`fm`), the mKCP header and seed, and `mtu`/`tti` are now read. Previously such a link produced an outbound that could not connect.
- **Hot apply now covers Shadowsocks** ([11.11](#1111-saving-restart-and-automatic-transformations)): a Shadowsocks inbound's clients are changed one by one through the Xray API, like VLESS, VMess, Trojan, Hysteria and MASQUE.

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **Node traffic sync writes only what changed** ([12.7](#127-how-inbounds-and-clients-are-synchronized)): previously, every 5 seconds the records of every client a node reported were rewritten, idle ones included, and the shared record of a client on several inbounds flipped back and forth. Large installations see noticeably less database load.

### Changes in section 16 — Operations: backups, logs, updating, CLI

- **Xray core crash reports are saved in full** ([16.2](#162-viewing-logs)): the `core_crash_*.log` file in the panel's log folder holds the whole Go report — the `panic:`/`fatal error:` header and the stack trace — instead of just the first 7 bytes, "panic: ". Reports from the same second no longer overwrite each other, and ordinary log lines mentioning panic/exception are no longer mistaken for a crash and dropped from the log.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 English · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.5.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
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

## What's new in 3.5.0

Version 3.5.0 is a major release: MTProto has been moved to a multi-client model (the mtg-multi engine, personal secrets, quotas and ad-tags), managed hosts have become group-based (multiple inbounds and addresses in a single entry), restore on a PostgreSQL panel accepts SQLite backups, outbounds gained "Target Strategy", a "Real delay" test and Egress/Country columns, and a balancer can use another balancer as a fallback. The bundled core is Xray 26.7.11. Below are the changes relative to 3.4.2, grouped by manual section.

### Changes in section 1 — Introduction, requirements and installation

- The Xray core has been updated to **26.7.11**. Accompanying auto-migrations: the Shadowsocks `none`/`plain` and VMess `none`/`zero` ciphers have been removed from the core (saved configs are rewritten automatically), and an unencrypted VLESS/Trojan outbound to a public address is rejected on save.
- A new **`x-ui pgclient [version]`** command and a **10. Install/Upgrade client tools (pg_dump/pg_restore)** item in the PostgreSQL menu — installation/upgrade of the PostgreSQL client tools.
- Script fixes: PostgreSQL and fail2ban installation on the RHEL family (EPEL), Arch without a full `pacman -Syu`, the correct Xray binary name on 32-bit ARM (`xray-linux-arm32`), confirmation of the auto-detected IPv4 before issuing an IP certificate, and a fix for the false "Your input is invalid" when accepting the default ACME port.

### Changes in section 2 — Panel login and access security

- IP limit: a "dead" connection is now banned **once** rather than on every 10-second scan — fail2ban counters no longer inflate, and there is no need to raise `maxretry`.

### Changes in section 4 — Inbounds: creation and common parameters

- The inbound list gained a **search** field (by remark, port and protocol), and the node drop-downs ("Deploy to", the "Nodes" filter) are now searchable.

### Changes in section 5 — Protocols

- **MTProto has been moved to a multi-client model** (the mtg-multi engine): MTProto users are now regular clients, each with its own secret, quota, expiry, ad-tag and personal `tg://proxy` link. The inbound-level "Secret" field has been removed (existing inbounds are converted automatically), and "FakeTLS domain" became the default domain for new secrets. New inbound fields: **Max connections** (connection cap) and **Public IPv4/IPv6** (for the ad-tag middle proxy). Client changes are applied on the fly without dropping other users' Telegram sessions.
- WireGuard: the inbound menu gained the full set of client actions (Export all links, attach/detach, groups), export is split into **Config** and **Links** tabs, the **"WireGuard allowed IPs" field is now editable** (multiple comma-separated entries), and in the client config of a node-hosted inbound `Endpoint` now points to the node's address.

### Changes in section 7 — Connection security: TLS, XTLS and REALITY

- The **Finalmask + REALITY combination is rejected** on save (it caused Xray-core to crash on the first connection); the minClientVer placeholder has been updated to 26.3.27.
- A new Finalmask TCP mask type — **XMC (Minecraft)**: disguises the stream as Minecraft traffic (Hostname, Usernames, and a required Password with auto-generation).

### Changes in section 8 — Clients

- A new **"Speed"** column — each client's live speed (↑/↓, a sliding ~5-second average).
- Client search finds by **Telegram ID** again; disabled inbounds are hidden from the binding list in the client form; duplicate accumulation in the "Unbind" window has been fixed.
- MTProto clients have their own fields: **"MTProto secret"** (with regeneration) and **"Ad-tag (sponsored channel)"** (32 hex characters); quota and expiry are now actually enforced for MTProto.

### Changes in section 9 — Client groups

- The client info window now shows the client's **group**.

### Changes in section 10 — Subscriptions

- **Managed hosts have become group-based**: one entry covers **multiple inbounds** (multi-select) and **multiple addresses** (tags, each entry may carry its own `:port`; address autocompletion; empty — the inbound address is inherited). The list columns show address and inbound chips (with "+N"), actions and the API work with groups (`groupId`), and a bulk `POST /panel/api/hosts/bulk/add` has been added. Host ordering is now global (by sort order, then by remark).
- The **announcement** text (`subAnnounce`) is now shown as a banner on the subscription info page; the `announce` variable is available in custom templates.
- The info page now opens in a browser via the **JSON/Clash links** too (not only the main one).
- The host settings **Final Mask** and **Allow insecure** now also take effect in raw links (`fm=`) and for **Hysteria2** (`insecure=1` / `skip-cert-verify: true`) respectively.
- The "Subscription update intervals" range (`subUpdates`) has been fixed to **0–525600** (the previous UI limit of 168 blocked saving settings after an upgrade from 2.x).
- Native **WireGuard clients are now included in Clash and JSON subscriptions** (previously — raw only).

### Changes in section 11 — Xray: routing, outbounds, DNS and extensions

- Outbound editor: a new **"Target Strategy"** field (11 values from `AsIs` to `ForceIPv4`), a **"Real delay"** test mode (full time including tunnel establishment; the HTTP mode is now measured over a "warm" connection), and **Egress** (exit IP behind an "eye") and **Country** (flag + country, WARP badge) columns after an HTTP/Real test.
- **A balancer's fallback can point to another balancer**: the panel builds the hidden loopback object (`_bl_…`) itself and guards against cycles and against deleting a balancer that is in use; the `_bl_` prefix is reserved.
- The "Basic Routing" tab gained a **"Default Outbound"** selector — which outbound handles traffic that matched no rule (the selected one is moved to the first position).
- DNS servers on private IPs are no longer blocked by the `geoip:private` rule — the panel maintains a managed allow rule itself.
- Happy Eyeballs in dial (sockopt) settings now actually turns on; "Try delay" defaults to 250 ms, and an explicit 0 is preserved.
- Outbound subscription import: the port of `ss://` links with `?plugin=`/a trailing `/` is now parsed correctly.

### Changes in section 12 — Nodes (multi-panel, master/slave)

- A batch of fixes: saving a client without changes no longer breaks live traffic of node inbounds; a node's Host overrides are accepted into the master on first accept; auto-renewal opens a fresh quota window; deleting a client on the master fully deletes it on the nodes; a node's inbounds are not swept away before first accept; one malformed inbound no longer stops the node's traffic sync; the port-conflict check is limited to the inbound's own node.

### Changes in section 14 — Telegram bot

- **`/usage`**, **`/inbound`**, **`/restart`** and a new admin command **`/clearall`** (reset all clients' traffic, with confirmation) have been added to the bot command menu.
- Online client entries are labeled `email - inbound remark`; backup and ban-log messages include the host name; Telegram ID search works regardless of settings formatting.

### Changes in section 16 — Operations: backups, logs, updates, CLI

- **Restore on a PostgreSQL panel accepts SQLite files**: a regular `.db` backup or a migration `.dump` is imported straight into PostgreSQL (in a single transaction, with checks before Xray is stopped). The file picker accepts `.dump,.db` on both engines; "Download Migration" remains only on PostgreSQL panels.
- Before restoring a `pg_dump` archive, the panel verifies the dump is readable and, on a version mismatch, suggests the exact `x-ui pgclient <version>` command.
- Startup auto-repairs: overflowed traffic counters are clamped and recovered; the obsolete UNIQUE constraint on the inbound port is removed (it interfered with multi-node).
- Xray logs: a new job every 10 minutes trims the access and error logs when either exceeds **64 MiB**; the daily cleanup now clears both.
- Docker: certificate auto-renewal is fixed (crond starts, and acme.sh state is persisted in a volume).

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 English · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.4.2**.

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

## What's new in 3.4.2

Version 3.4.2 is a major update: WireGuard has been moved to a multi-client model, REALITY gained a live target scanner, balancers got Observatory / Burst Observatory tabs, and confirmation of sensitive settings with a 2FA code was added. Below are the changes relative to 3.4.1, grouped by manual section.

### Changes in section 1 — Introduction, requirements and installation

- A **"Documentation"** button (book icon) has appeared in the sidebar (and in the mobile drawer) — it opens the official documentation at `https://docs.sanaei.dev/`.
- The minimum Xray version the panel updates to has been raised to **26.6.27** (the bundled core is Xray 26.6.27).

### Changes in section 2 — Panel login and access security

- When 2FA is enabled, changing the administrator login/password and disabling 2FA now require **entering the current code** from the authenticator app (confirmation of sensitive changes).
- LDAP: a new **"Skip TLS certificate verification"** toggle (`ldapInsecureSkipVerify`) — disables certificate verification under LDAPS; available only when "Use TLS (LDAPS)" is enabled.

### Changes in section 3 — Overview / Dashboard

- The panel version button now always opens the update window (see section 16 — dev channel).
- A cross-cutting **accessibility** improvement: aria labels for icon buttons and activation of elements via Enter/Space (for screen readers and keyboard navigation).

### Changes in section 4 — Inbounds: creation and common parameters

- The **"Export all links"** action now builds links through the subscription engine — it applies the remark template to each client and prefers managed Host endpoints (previously a fixed `inbound-email` remark was used).

### Changes in section 5 — Protocols

- **WireGuard has been moved to a multi-client model.** Peers are now regular clients (with automatic in-tunnel address assignment, subscription support, traffic/expiry limits and groups); the inline "Peers" list has been removed from the inbound form.
- A configurable **DNS** field (default `1.1.1.1, 1.0.0.1`) and a **client configuration card** have been added to the WireGuard inbound — copy/download/QR of the full `.conf` and a `wireguard://`/`wg://` link.

### Changes in section 6 — Transport (Stream Settings)

- For new XHTTP inbounds, the `maxConnections` parameter in **xmux** now defaults to **6** (it was `0` — no limit). Existing inbounds keep their value.

### Changes in section 7 — Connection security: TLS, XTLS and REALITY

- A **live REALITY target scanner** has been added: the **"Scan"** button (check the current target "live") and the **"Find targets"** button (scan a domain or an **IP/CIDR** range and pick suitable targets by their certificates). The "Target" and SNI fields are now empty when REALITY is first selected.

### Changes in section 8 — Clients

- Extending the expiry/quota via `bulkAdjust` now **automatically enables** a client that was disabled solely because of exhaustion (expired term or exceeded quota), if the extension brings it back within the limits. Clients disabled manually or still exhausted remain disabled.

### Changes in section 9 — Client groups

- **"Reset traffic"** for a group now zeroes **only the group's own counter**; the counters, quotas and state of individual clients are not affected, and no Xray restart is required. This is a change from the previous behavior (where the traffic of all the group's clients used to be reset).

### Changes in section 10 — Subscriptions
- In **managed hosts**, the **VLESS route** field has been redefined: it is now a single value `0-65535` (rather than a port list), and it is actually "baked" into the UUID of every subscription (raw/JSON/Clash).
- The `{{EMAIL}}` variable (and its synonym `{{USERNAME}}`) in the remark template is now output only on the client's **first link** — just like the traffic/expiry block.

### Changes in section 11 — Xray: routing, outbounds, DNS and extensions
- **Balancers**: the page has been split into **"Balancer settings"** and **"Observatory"** tabs; instead of raw JSON there are now Observatory and Burst Observatory forms (Burst gains an **"HTTP method"** field). A Random/Round-robin balancer with a `fallbackTag` now automatically creates a Burst Observatory.
- When an outbound or balancer is deleted, the panel cleans up the related references in routing itself and shows a **preview of the consequences** in the confirmation dialog.
- In routing rules, the **L4** network criterion is written to the config in lowercase (`tcp`/`udp`), while the table displays it in uppercase.
- Errors in the add/edit balancer form are now deferred until the first time a field is touched or a save is attempted.

### Changes in section 12 — Nodes (multi-panel, master/slave)
- The "saved locally, node offline — will sync later" notification is now shown only when the node is actually offline or disabled (previously — on every save to an online node).

### Changes in section 16 — Operations: backups, logs, updates, CLI
- Backup file names now contain the server address and a **date-time**: `{host}_YYYY-MM-DD_HHMMSS.db` (`.dump` for PostgreSQL), for example `panel.example.com_2026-06-27_000000.db` — both when downloading from the panel and in backups sent by the Telegram bot.
- The **dev channel** of updates can now be enabled from a stable build: the version button always opens the update window, and a **"Dev channel"** toggle has appeared with a warning about instability and the absence of automatic rollback.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

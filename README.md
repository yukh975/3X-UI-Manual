# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.8.5**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.8.5

Version 3.8.5 is mostly fixes and optimization. The headline: **the subscription page has been reworked** (a usage ring, tabs, one-tap import into apps), and **the link to the built-in profile page is no longer disclosed** — the profile-page mode is now an explicit setting (`None` / `Built-in` / `Custom`, `None` by default). **The Xray core survives a broken configuration:** a config the core cannot bind is rejected with the reason shown, instead of taking down every protocol in a once-a-second loop. **AmneziaWG relay ports** are fixed (on databases with a high inbound-id counter the protocol simply did not work before), **large node-farm synchronization** is faster, and **`"qType": 0`** in a DNS outbound no longer blocks every query (a one-time migration fixes the template). Requirements are unchanged: Go 1.27.1, Xray-core v26.9.9. Below are the changes relative to 3.8.0, by manual section.

### Changes in section 2 — Panel login and access security

- **The two-factor code is accepted from adjacent TOTP windows** (#6546): with a small clock skew between the server and the authenticator app, the code is no longer rejected.

### Changes in section 4 — Inbounds: creation and common parameters

- **A port conflict is rejected on save and on enabling an inbound**, instead of silently crashing the core. The rejection message names the inbound or the AmneziaWG peer that holds the port — free it and retry.

### Changes in section 5 — Protocols

- **AmneziaWG relay ports are fixed for good:** a loopback relay slot is allocated even for a row with no peers and for a disabled row, the port number wraps around, and a row does not take up its own port. On databases with a high inbound-id counter the protocol did not work at all before.

### Changes in section 8 — Clients

- **The counter cards on the clients page are now clickable:** clicking one filters the list by that metric (total, online, etc.).

### Changes in section 10 — Subscriptions (Subscription)

- **The subscription page has been reworked:** a usage ring with the remaining quota, "Subscription / Apps / Configs" tabs, one-tap import on Android and iOS, a clear status (expired / depleted / disabled) and right-to-left rendering for Persian and Arabic.
- **The built-in profile-page mode is `None` / `Built-in` / `Custom`** (`None` by default): the subscription response no longer returns a link to the built-in profile page, which used to disclose the subscription address itself (#6538); the `Profile-Web-Page-Url` header is sent only in Built-in and Custom modes. A previously set profile address is migrated to `Custom` mode.

### Changes in section 11 — Xray: routing, outbounds, DNS, and extensions

- **`"qType": 0` in a DNS outbound no longer blocks every query:** a one-time migration rewrites the numeric `0` into the string `"0"`. Installations that reached 3.8.0 with a "block type 0" rule lost all DNS through that outbound.

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **Only the IP addresses of a node's own clients are sent to it**, not the whole farm's client table; synchronization runs in batches of up to 32 nodes, and each node has its own HTTP connection pool.

### Changes in section 13 — Panel Settings

- **A broken configuration does not crash Xray:** a config the running core cannot bind is rejected at the restart step with the reason shown — instead of a once-a-second loop that takes down every protocol.
- **"Restart Xray After Client Disable" also fires on manually disabling or deleting a client**, not only on auto-disable by expiry or quota.

### Changes in section 16 — Operations: backups, logs, updating, CLI

- **Back up the database before upgrading** — the first start runs a one-time DNS-template migration (`DNSOutboundQTypeZeroFix`, see section 11). An unparseable template is logged and skipped, and the panel still starts.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

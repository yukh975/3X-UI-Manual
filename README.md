# 3X-UI Manual

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive user guide written for panel **v3.7.0**.

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |

## What's new in 3.7.0

Version 3.7.0 adds **native AmneziaWG** — the DPI-resistant protocol now runs on an embedded engine (`amneziawg-go` over the gVisor network stack), with no kernel module, no `awg-quick` and no second panel. The rest of the headline: **API tokens gained a scope and an expiry**; a client's renewal can be pinned to a **calendar day of the month** and capped by count; a client gained its **own traffic-reset cycle**, a **device limit (HWID)** with the list of registered devices, and **external links** merged into its subscription; the subscription can carry **balancers**; importing a database **keeps this machine's settings**. Below are the changes relative to 3.6.0, by manual section.

### Changes in section 1 — Introduction, Requirements, and Installation

- **Building from source requires Go 1.27** (3.6.0 needed 1.26). The Xray core version did not change.
- The first start runs **automatic schema migrations**: the client's traffic-reset cycle and last subscription fetch, the node-sync bookkeeping columns, an index on `LOWER(email)`, the API token scope and expiry, and external-link normalization. **Back up the database before upgrading.**
- Upgrading no longer deletes **your own files in `bin/`** (a hand-added `geoip.dat`, for instance).
- `update.sh` now downloads **through the same proxy the panel is configured with**, so upgrades work on servers with no direct outbound access.

### Changes in section 2 — Panel Login and Access Security

- **An API token now carries a scope and an optional expiry.** There are three scopes: `admin` — full access, as before; `monitor` — read-only, and only over a list of status endpoints (`/server/status`, the metric histories, `/server/getXrayVersion`, `/server/getPanelUpdateInfo`, a node's metric history); `node-sync` — exactly what a central panel needs to synchronize (list/add/update/delete inbounds, client operations, restart Xray). A request outside its scope gets **HTTP 403**. Tokens created earlier stay `admin`, so nothing changes for them.
- The expiry is set at creation; past it, the token stops authenticating.
- **Replacing the stored TOTP secret now requires a 2FA code** — a stolen session can no longer quietly re-point two-factor authentication at its own secret.
- The CLI `x-ui setting -getApiToken` **no longer accumulates admin tokens**: it rotates a single `cli-fallback` token. CLI tokens printed earlier stop working once it rotates.

### Changes in section 3 — Overview / Dashboard

- **The sidebar can be pinned** ("Pin sidebar" / "Unpin sidebar") — the icon rail no longer collapses after every hover.
- The panel is now an **installable PWA** (network-only: it works only while the network is reachable).
- A new **"Uptime"** tile, and **log levels and access events are localized**: Debug/Info/Notice/Warning/Error and DIRECT/BLOCKED/PROXY render in the interface language.
- **AmneziaWG logs** are viewable (`Tools → AmneziaWG Logs`): last handshake, interface, inbound, endpoint, idle time and events.

### Changes in section 4 — Inbounds: Creation and Common Parameters

- A new **"Disable XTLS flow"** switch (`disableFlow`, VLESS only): opts this inbound out of automatic `xtls-rprx-vision` injection even when its transport allows it. Vision keeps working on your other inbounds in the same subscription.
- The **"Subscription order"** field (`subSortIndex`, present since 3.6.0) gained a narrow endpoint, `POST /panel/api/inbounds/:id/subSortIndex`. Changing the position used to go through `/update/:id`, which takes the whole inbound together with its entire client list — two people editing one inbound at once overwrote each other's work.
- A check-and-claim race on the port was closed, and **form validation errors are now shown** instead of a silent refusal to save.
- **Multi-node "online" attribution is more accurate**: a client connected to a node is no longer lost in the count.

### Changes in section 5 — Protocols

- **A new protocol: AmneziaWG.** This is WireGuard with DPI-resistant obfuscation. The panel runs it **inside its own process** (`amneziawg-go` over a gVisor netstack), so no kernel module (DKMS), no `awg-quick`, no Docker and no separate panel are needed. One enabled client = one peer. The details and every field are in the new [5.10](#510-amneziawg) subsection.
- **Hysteria:** updating an inbound whose client has an empty `auth` is now rejected (it used to silently break that client's access), and a Hysteria2 client over its limit is **force-disconnected** instead of downloading on until a restart.

### Changes in section 7 — Connection Security: TLS, XTLS and REALITY

- **A REALITY target on a local network can be checked too.** The panel's SSRF guard used to simply refuse; now the panel warns ("Target is reachable but sits on a private/local network"), asks for confirmation, and bypasses the guard **for that one probe only**. The result gained the certificate expiry and the SNI used.

### Changes in section 8 — Clients

- **Renewal on a calendar day.** The **"Renew on day"** field (`resetDay`, 1–31): the client renews on that day of every month at midnight in the panel's time zone, instead of every N days. A month too short for the chosen day renews on its last day. `0` keeps the interval mode.
- **A cap on auto-renewals** — the **"Max renewals"** field (`resetMax`): how many times auto-renew may fire before the client is left to expire. `0` means no limit. Catching up several missed periods spends one renewal per period. A **"Renewals used"** counter sits next to it.
- **A per-client traffic reset cycle** (`trafficReset` + `trafficResetDay`) — the periodic reset used to be an inbound-level setting only.
- **A device limit: "HWID Limit"** (`limitHwid`) — the maximum number of registered devices whose subscription requests are accepted; `0` means unlimited. Next to it is the **"HWID Devices"** list: device, OS and version, model, first and last seen. A device can be removed **one at a time** or the list cleared entirely — a removed device simply re-registers on its next subscription fetch.
- **A client's external links** (the "Links" tab, present since 3.6.0) gained controls: a row can be **disabled without deleting it** (`enable`), given an **expiry** and a **name prefix**, and the panel shows the **last fetch time and the error text** when an external source did not answer.
- The client table gained a **"Last Subscription Fetch"** column — when the subscription was last pulled.
- AmneziaWG clients gained key fields (**Private/Public/Pre-Shared Key**), **Allowed IPs** (empty auto-assigns) and **Forwarded Ports** — ports and ranges DNAT'd to this client, e.g. `80, 443, 8000-8100`.
- Fixes: a stale IP-log row no longer blocks saving a client; the summary badges are computed from live data rather than the `client_stats` snapshot; bulk client changes are pushed to nodes **after** the commit lands; stored IPs of offline clients expire on schedule.

### Changes in section 9 — Client Groups

- A bulk move between groups now **reports the clients that actually changed and no longer restarts Xray** when there is nothing in the config to change.

### Changes in section 10 — Subscriptions

- **The subscription page in a browser is unchanged.** During 3.7.0's development it was replaced with a neutral "this is a subscription link, copy it" page, but that was **reverted before release**: on mobile it showed a bare screen instead of traffic, expiry and links. In 3.7.0 a browser still gets the normal themed info page, and `?html=1` / `?view=html` and `?format=info` behave as before.
- **Subscription balancers** — a new "Sub Balancers" settings section. Each enabled balancer is added to the JSON subscription as **one extra profile** that automatically picks the best of the selected inbounds' endpoints (`routing.balancers` + `burstObservatory` in the client config). You configure the remark, the strategy (**Least load / Least ping / Random / Round robin**), the inbounds, and the position in the subscription list; on equal numbers the balancer comes after the inbound.
- **Client tokens now work in the subscription metadata too.** `{{EMAIL}}`, `{{ID}}`, `{{SHORT_ID}}`, `{{SUB_ID}}`, `{{TELEGRAM_ID}}` used to be substituted only in the remark template; the subscription title, support link, profile link and announcement now take them as well, so each client can get a personal title or a support link carrying their own identifier.
- **Remote routing rules by URL.** The rule fields for Happ, Incy and Clash accept not only a ready deeplink or inline rules but also **one permanent HTTPS URL**: the panel refreshes the rules in the background and keeps the last valid value, so a subscription request never waits on the external source.
- The panel **warns when salamander settings (Hysteria2) cannot reach the client**.
- Output fixes: `tlsSettings.cipherSuites` is forwarded into the JSON subscription; `mport` survives on external-proxy links; the full remark is rendered **once per subscription** rather than once per credential; `USAGE_PERCENTAGE` uses a fullwidth percent sign.

### Changes in section 11 — Xray: Routing, Outbounds, DNS and Extensions

- **PIA outbounds by login.** A new "PIA" section: enter your Private Internet Access username and password, pick a country and a server, and the panel fetches the key and adds a ready WireGuard outbound. Adding the same server again offers to renew its key instead of creating a duplicate.
- **A remote routing URL** — a rule set can live at an external address and be updated centrally.
- **A client picker inside user rules**: the `user` field is filled from the client list instead of by hand.
- **Browsing geosite/geoip categories from a routing rule** — without leaving the form you can see what is inside `geosite:category-ads-all` or `geoip:ru` and check values for typos. The panel distinguishes "no such category", "no such attribute", "wrong database kind" and "the database file is missing — add it under Geodata".
- Fixes: one poisoned DNS answer no longer blocks outbound tests; a WARP IP change **keeps the Plus license key**; allocation query failures are no longer swallowed; salamander settings import correctly from standard obfs parameters; an "unrestricted" freedom outbound stored in the database is hardened.

### Changes in section 12 — Nodes (multi-panel, master/slave)

- **Cloning inbounds to nodes** (first implementation): selected inbounds are deployed to several nodes at once, with a "{ok} cloned, {failed} failed" report.
- **A node's API token can be encrypted at rest** (opt-in) — no readable token is left in the database.
- Synchronization became more careful: a matching **already-deployed inbound is adopted rather than recreated**; disabled inbounds a node snapshot cannot report on are **kept**; a stale expiry sync **no longer undoes client extensions**; deleting clients the sync never meant to delete is fixed; the adoption timestamp is not stamped when nothing was adopted.
- **mTLS:** **every** certificate in the node trust bundle is validated; a rotated master certificate is applied **without restarting the panel** (the "Reload master mTLS credential" button, `POST /panel/api/nodes/mtls/reloadClient`); the master credential is persisted atomically and silent reissue is gone.
- Heartbeat persistence failures and the inbound a node snapshot removes are now **logged** instead of being lost.

### Changes in section 13 — Panel Settings

- **An allowlist for the IP limit** ("IP limit allowlist"): addresses and networks (comma-separated, IP or CIDR) that the IP limit **never counts and never bans**. A shared office or campus address can no longer use up a client's limit.
- **Importing a database keeps this machine's settings** — a new "Keep this machine's settings" checkbox (on by default): listen addresses and ports, the base path, certificate paths and node identity come from the current panel rather than the uploaded file. Clear it to restore the old behaviour — a whole-file clone.
- Calendar: labels are localized and a **Gregorian / Jalalian** choice was added; the clear button in the Jalali date picker actually clears the field now.
- Fixes: an inconclusive fail2ban probe **keeps the IP limits** instead of dropping them; LDAP auto-delete **no longer wipes every client** when the directory returns an empty answer; an empty database setting falls back to the default secret.

### Changes in section 14 — Telegram Bot

- Long messages are split **at line boundaries** rather than mid-character, so tables and lists no longer tear apart.

### Changes in section 15 — Geo Databases (geoip / geosite and custom)

- **The contents of a geo database can now be browsed**: the files in the Xray folder with their category count, size and update date; the list of categories; paged browsing of entries and subnets; and a check of a set of values against the database. The endpoints are `GET /panel/api/xray/geodata/files`, `/categories`, `/entries` and `POST /panel/api/xray/geodata/validate`.

### Changes in section 16 — Operations: Backups, Logs, Updates, CLI

- **Back up the database before upgrading to 3.7.0** — the first start runs schema migrations (see section 1).
- Importing a database no longer overwrites this machine's network settings by default (see section 13).
- `x-ui setting -getApiToken` rotates a single `cli-fallback` token (see section 2).
- Your own files in `bin/` survive an upgrade, and `update.sh` goes through the panel's proxy.
- A half-applied startup migration **can no longer commit silently** — the panel refuses to come up on a half-broken schema instead of pretending everything is fine.

---

Created from an analysis of the panel's source files. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._

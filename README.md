# 3X-UI Manual

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive, source-free user guide written for panel **v3.3.1**.

🇷🇺 [Russian version](README.ru.md)

> **Read-only mirror.** This GitHub repository is a one-way mirror — the manual's source lives in a private GitLab and is pushed here automatically, so it's always up to date. Found an error or inaccuracy? Please [open an Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests are not accepted** (they're closed automatically) — fixes are made at the source.

## Contents

| File | Language | Format |
| --- | --- | --- |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](3X-UI-MANUAL.ru.pdf) | 🇷🇺 Russian — **canonical** (edit this first) | Markdown + PDF |
| **[3X-UI-MANUAL.md](3X-UI-MANUAL.md)** · [PDF](3X-UI-MANUAL.pdf) | 🇬🇧 English — mirror of the Russian manual | Markdown + PDF |

16 sections covering installation, inbounds/clients, subscriptions, routing & balancers, DNS, TLS/Reality, nodes, backup, security and more — with worked examples. The manual opens with a **"What's new in 3.3.1"** section summarizing changes since 3.3.0.

## Editing

The **Russian** version is canonical: make changes in `3X-UI-MANUAL.ru.md` first, then mirror them into `3X-UI-MANUAL.md`. Keep both in sync.

## PDF

The PDFs are committed alongside the Markdown. Rebuild them after editing with:

```bash
./scripts/build-pdf.sh
```

Needs `pandoc` plus a renderer — [WeasyPrint](https://weasyprint.org/) (preferred: page numbers; `brew install pango` + `pip install weasyprint`) or Google Chrome (fallback).

---

© 2026 Yuriy Khachaturian ([yukh.net](https://yukh.net))

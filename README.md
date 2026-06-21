# 3X-UI Manual

User manual for the [3x-ui](https://github.com/MHSanaei/3x-ui) panel — a comprehensive, source-free user guide written for panel **v3.3.1**.

🇷🇺 [Версия на русском](README.ru.md)

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

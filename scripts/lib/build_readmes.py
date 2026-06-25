#!/usr/bin/env python3
"""Build per-language README files (one per manual language) from a shells JSON.

shells.json = { "<code>": {intro, mirrorNote, contents, hFile, hLang, hFormat, footer}, ... }
Each README = title + 13-language switcher (flag+native, links to README.<code>.md;
en -> README.md) + intro + read-only-mirror note + Contents table (all manuals +
PDFs) + the "What's new" summary copied verbatim from that language's manual +
attribution footer.

Usage: python3 scripts/lib/build_readmes.py shells.json
"""
import sys, json

LANGS = [
    ("ar", "🇸🇦", "العربية"), ("en", "🇬🇧", "English"), ("es", "🇪🇸", "Español"),
    ("fa", "🇮🇷", "فارسی"), ("id", "🇮🇩", "Bahasa Indonesia"), ("ja", "🇯🇵", "日本語"),
    ("pt", "🇧🇷", "Português"), ("ru", "🇷🇺", "Русский"), ("tr", "🇹🇷", "Türkçe"),
    ("uk", "🇺🇦", "Українська"), ("vi", "🇻🇳", "Tiếng Việt"),
    ("zh-CN", "🇨🇳", "简体中文"), ("zh-TW", "🇹🇼", "繁體中文"),
]

shells = json.load(open(sys.argv[1], encoding="utf-8"))


def readme_path(code):
    return "README.md" if code == "en" else f"README.{code}.md"


def switcher(cur):
    parts = []
    for code, flag, native in LANGS:
        parts.append(f"{flag} {native}" if code == cur
                     else f"{flag} [{native}]({readme_path(code)})")
    return " · ".join(parts)


def table(s):
    rows = [f"| {s['hFile']} | {s['hLang']} | {s['hFormat']} |", "| --- | --- | --- |"]
    for code, flag, native in LANGS:
        rows.append(
            f"| **[3X-UI-MANUAL.{code}.md](3X-UI-MANUAL.{code}.md)** · "
            f"[PDF](pdf/3X-UI-MANUAL.{code}.pdf) | {flag} {native} | Markdown + PDF |")
    return "\n".join(rows)


def summary(code):
    m = open(f"3X-UI-MANUAL.{code}.md", encoding="utf-8").read()
    i1 = m.index("\n## 1. ")
    prev = m.rfind("\n## ", 0, i1)          # the "## What's new" heading just before section 1
    return m[prev + 1:i1].rstrip()


for code, flag, native in LANGS:
    if code not in shells:
        continue
    s = shells[code]
    content = (f"# 3X-UI Manual\n\n{switcher(code)}\n\n{s['intro']}\n\n> {s['mirrorNote']}\n\n"
               f"## {s['contents']}\n\n{table(s)}\n\n{summary(code)}\n\n---\n\n{s['footer']}\n")
    open(readme_path(code), "w", encoding="utf-8").write(content)
    print("  ✓", readme_path(code))

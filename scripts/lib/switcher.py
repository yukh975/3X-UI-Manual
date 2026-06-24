#!/usr/bin/env python3
"""Set the language switcher line in every 3X-UI-MANUAL.<code>.md that exists.

Switcher = flag + native name, ordered alphabetically by language code (so `ru`
is mid-list, not first). The current file's own language is plain text; the
others are links to their .md file. Only languages whose file exists are listed.
Run from the repo root: python3 scripts/lib/switcher.py
"""
import glob, os, re

# ordered alphabetically by code on purpose (ru lands mid-list)
LANGS = [
    ("ar", "🇸🇦", "العربية"),
    ("en", "🇬🇧", "English"),
    ("es", "🇪🇸", "Español"),
    ("fa", "🇮🇷", "فارسی"),
    ("id", "🇮🇩", "Bahasa Indonesia"),
    ("ja", "🇯🇵", "日本語"),
    ("pt", "🇧🇷", "Português"),
    ("ru", "🇷🇺", "Русский"),
    ("tr", "🇹🇷", "Türkçe"),
    ("uk", "🇺🇦", "Українська"),
    ("vi", "🇻🇳", "Tiếng Việt"),
    ("zh-CN", "🇨🇳", "简体中文"),
    ("zh-TW", "🇹🇼", "繁體中文"),
]
FLAG_RE = re.compile(r"[\U0001F1E6-\U0001F1FF]")  # regional-indicator (flag) emoji


def present_codes():
    return {os.path.basename(f)[len("3X-UI-MANUAL."):-len(".md")]
            for f in glob.glob("3X-UI-MANUAL.*.md")}


def switcher_line(current, present):
    parts = []
    for code, flag, name in LANGS:
        if code not in present:
            continue
        if code == current:
            parts.append(f"{flag} {name}")
        else:
            parts.append(f"{flag} [{name}](3X-UI-MANUAL.{code}.md)")
    return " · ".join(parts)


def main():
    present = present_codes()
    for code, _flag, _name in LANGS:
        if code not in present:
            continue
        path = f"3X-UI-MANUAL.{code}.md"
        lines = open(path, encoding="utf-8").read().split("\n")
        # find the switcher line: first line (within the head) starting with a flag emoji
        idx = next((i for i, l in enumerate(lines[:12]) if FLAG_RE.match(l.strip())), None)
        new = switcher_line(code, present)
        if idx is None:
            # no switcher yet: insert it as the 3rd line (after title + blank)
            lines[2:2] = [new, ""]
        else:
            lines[idx] = new
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(f"  ✓ {path}")


if __name__ == "__main__":
    main()

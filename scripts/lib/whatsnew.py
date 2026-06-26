#!/usr/bin/env python3
"""Reformat the "What's new" summary item headings to read as section references.

The summary groups changes by section, so its items were headed by the section
number (`### 11. Xray…`, `### 3. Overview…`). Because only the changed sections
appear, the numbers look like a broken 1-2-3 list. Rewrite each item heading to
"<changes in section> N — <title>" (localized, from whatsnew-labels.json) so the
non-sequential numbers read as section references, not list ordinals.

Operates only on the items inside the "What's new" block (the `## …` heading just
before `## 1.`), matching `### N. Title`. Idempotent (already-reformatted headings
no longer start with a bare number). Run after the summary is written/translated,
before toc.py.

Usage: python3 scripts/lib/whatsnew.py [code ...]
"""
import sys, re, json, glob, os

LABELS = json.load(open(os.path.join(os.path.dirname(__file__), "whatsnew-labels.json"),
                       encoding="utf-8"))
ITEM = re.compile(r"^### (\d+)\.\s+(.+?)\s*$")


def reformat(path, code):
    tmpl = LABELS.get(code)
    if not tmpl:
        return f"no label for {code}"
    lines = open(path, encoding="utf-8").read().split("\n")
    try:
        sec1 = next(i for i, l in enumerate(lines) if re.match(r"^## 1\.\s", l))
    except StopIteration:
        return "no '## 1.' section found"
    summary = max(i for i in range(sec1) if lines[i].startswith("## "))
    n = 0
    for i in range(summary + 1, sec1):
        m = ITEM.match(lines[i])
        if m:
            lines[i] = "### " + tmpl.format(n=m.group(1), title=m.group(2))
            n += 1
    if n:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    return f"{n} item headings reformatted"


codes = sys.argv[1:] or [
    f.split("MANUAL.")[1][:-3] for f in sorted(glob.glob("3X-UI-MANUAL.*.md"))
]
for code in codes:
    print(f"  {code:6} {reformat(f'3X-UI-MANUAL.{code}.md', code)}")

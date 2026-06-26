#!/usr/bin/env python3
"""One-off structural repair: close the subscription-template code fence in §10.

The §10 "subscription page template" example has two ```html blocks; the first
(the `{{ .subTitle }}` body) was never closed and a stray ``` sits after the
second. Per CommonMark an info-string fence (```html) can only OPEN, so the first
block ran from its opener all the way to the stray ``` — swallowing the §10 tail
and the §11 / 11.1 / 11.2 headings into a code block (they render as code on
GitHub and get no anchor). Fix: add the missing close after the first block's
last line and drop the stray fence before the following `---`. The code lines are
identical in every language, so we anchor on them.

Usage: python3 scripts/lib/fixfence.py [code ...]   (default: all)
"""
import sys, glob, re

FENCE = "`" * 3
ANCHOR = "{{ range .links }}<div>{{ . }}</div>{{ end }}"   # last line of block 1


def fix(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    try:
        i = next(k for k, l in enumerate(lines) if l.strip() == ANCHOR)
    except StopIteration:
        return "anchor not found"
    if lines[i + 1].strip() == FENCE:
        return "already closed"
    # 1) close block 1 right after its last content line
    lines.insert(i + 1, FENCE)
    # 2) drop the stray fence: the lone ``` just before the first '---' after </script>
    try:
        s = next(k for k, l in enumerate(lines) if l.strip() == "</script>")
        sep = next(k for k in range(s, len(lines)) if lines[k].strip() == "---")
    except StopIteration:
        return "added close; </script>/--- not found for stray"
    j = sep - 1
    while j > s and lines[j].strip() == "":
        j -= 1
    if lines[j].strip() == FENCE:
        del lines[j]
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        return "fixed (added close, removed stray)"
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return "added close; no stray fence before ---"


codes = sys.argv[1:] or [
    f.split("MANUAL.")[1][:-3] for f in sorted(glob.glob("3X-UI-MANUAL.*.md"))
]
for code in codes:
    print(f"  {code:6} {fix(f'3X-UI-MANUAL.{code}.md')}")

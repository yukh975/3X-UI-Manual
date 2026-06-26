#!/usr/bin/env python3
"""Repair stale in-body cross-references after sections get renumbered.

When a subsection is inserted (e.g. a new "11.7 Fake DNS" pushes WireGuard to
11.8), prose links elsewhere that point to the OLD anchor/number go stale —
`[11.7](#117-wireguard--warp--nordvpn)` while WireGuard now lives at 11.8. The
anchor's *topic* (the slug minus its leading section number) still identifies the
target unambiguously, so we re-point each broken link to whatever heading now
carries that topic, and — when the visible text is a bare section number — update
the number too.

Only links whose topic matches exactly one heading are touched; anything
ambiguous or unmatched is left as-is and reported. Run AFTER toc.py, on every
release. Anchors keep ZWNJ/ZWJ to match GitHub (see toc.py).

Usage: python3 scripts/lib/fixlinks.py [code ...]
"""
import sys, re, glob
from toc import gh_slug, heading   # same GitHub slug + dup rules

NUM = re.compile(r"^\s*(\d+(?:\.\d+)*)\.")        # leading "11.8." in heading text
LEAD = re.compile(r"^\d+-")                        # leading "118-" in an anchor
BARE = re.compile(r"^\d+(?:\.\d+)*\.?$")           # link text that is just a number


def topic(anchor):
    return LEAD.sub("", anchor)


def fix(path):
    txt = open(path, encoding="utf-8").read()
    # heading anchors (whole-doc order for correct dup suffixes), minus code fences
    nc = re.sub(r"```.*?```", "", txt, flags=re.S)
    seen = {}
    anchors = set()
    by_topic = {}                                  # norm(topic) -> [(number, anchor)]
    by_number = {}                                 # "11.5" -> [anchor]
    norm = lambda t: t.replace("-", "")            # CJK/Latin boundary hyphens vary
    for ln in nc.split("\n"):
        lvl, text = heading(ln)
        if lvl is None:
            continue
        a = gh_slug(text, seen)
        anchors.add(a)
        m = NUM.match(text)
        num = m.group(1) if m else None
        by_topic.setdefault(norm(topic(a)), []).append((num, a))
        if num:
            by_number.setdefault(num, []).append(a)

    fixed = unresolved = 0

    def repl(m):
        nonlocal fixed, unresolved
        text, tgt = m.group(1), m.group(2)
        if tgt in anchors:
            return m.group(0)
        # 1) topic match (survives renumbering; hyphen-insensitive for CJK)
        cands = by_topic.get(norm(topic(tgt)))
        if cands and len(cands) == 1:
            num, anchor = cands[0]
            new_text = num if (num and BARE.match(text.strip())) else text
            fixed += 1
            return f"[{new_text}](#{anchor})"
        # 2) fall back to the section number in the link text (heading reworded, same number)
        if BARE.match(text.strip()):
            n = text.strip().rstrip(".")
            c2 = by_number.get(n)
            if c2 and len(c2) == 1:
                fixed += 1
                return f"[{text}](#{c2[0]})"
        unresolved += 1
        return m.group(0)

    out = re.sub(r"\[([^\]]*)\]\(#([^)]+)\)", repl, txt)
    if out != txt:
        open(path, "w", encoding="utf-8").write(out)
    return fixed, unresolved


codes = sys.argv[1:] or [
    f[len("3X-UI-MANUAL."):-3] for f in sorted(glob.glob("3X-UI-MANUAL.*.md"))
]
for code in codes:
    f, u = fix(f"3X-UI-MANUAL.{code}.md")
    print(f"  {code:6} remapped={f:3}  unresolved={u}")

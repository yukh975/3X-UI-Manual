#!/usr/bin/env python3
"""Regenerate the Table-of-Contents in every manual from its own headings.

Why: the TOC (chunk-00) and the section headings (chunk-NN) are translated by
separate agents, so a section's TOC text and its heading text can diverge — and
then the TOC's `#anchor` (derived from the TOC text) no longer matches the
heading's GitHub anchor, breaking the link on GitHub and in the PDF. Rebuilding
the TOC straight from the headings makes TOC text === heading text, so every
anchor resolves by construction. It reuses already-translated heading text (no
re-translation) and is safe to run on every release.

TOC content = the "What's new" summary heading (one top-level entry) + every
`## N.` section (top level) and `### N.M.` subsection (indented). Headings inside
the "What's new" summary (its `### k.` change items, which sit before `## 1.`)
and all `#### N.M.K.` headings are skipped — matching the existing TOC depth.

Anchors use GitHub's algorithm (lowercase; keep letters/digits/`-`/`_` and the
zero-width joiners U+200C/U+200D — GitHub preserves them, e.g. in Persian; spaces
-> `-`; drop other punctuation; never collapse repeats; duplicate slugs get
-1, -2… in document order). NB: pandoc -f gfm *strips* the zero-width joiners, so
fa PDF anchors differ — build-pdf.sh strips U+200C from link targets on its temp
copy so the PDF stays internally consistent; the committed Markdown keeps them so
GitHub (the primary surface) resolves.

Usage: python3 scripts/lib/toc.py [code ...]   (default: all 3X-UI-MANUAL.*.md)
"""
import sys, re, glob, unicodedata


KEEP = "-_‌‍"   # hyphen, underscore, ZWNJ, ZWJ (GitHub preserves the joiners)


def gh_slug(text, seen):
    # GitHub keeps \p{Word} (letters, MARKS, numbers, _) plus '-' and the joiners;
    # combining marks (e.g. Persian kasra/hamza) are KEPT, punctuation dropped.
    out = []
    for ch in text.strip().lower():
        if ch in KEEP or unicodedata.category(ch)[0] in "LMN":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
    base = "".join(out)
    n = seen.get(base, 0)
    seen[base] = n + 1
    return base if n == 0 else f"{base}-{n}"


def heading(line):
    m = re.match(r"(#{1,6})\s+(.*)", line)
    return (len(m.group(1)), m.group(2).rstrip()) if m else (None, None)


def rebuild(path):
    lines = open(path, encoding="utf-8").read().split("\n")

    # locate the TOC heading: an h2 immediately followed (after blanks) by "- ["
    toc_h = None
    for i, ln in enumerate(lines):
        lvl, _ = heading(ln)
        if lvl == 2:
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and lines[j].lstrip().startswith("- ["):
                toc_h = i
                break
    if toc_h is None:
        print(f"  !  {path}: no TOC found, skipped")
        return False

    # TOC list spans from after the heading until the next h2 (the "What's new" one)
    end = toc_h + 1
    while end < len(lines):
        lvl, _ = heading(lines[end])
        if lvl == 2:
            break
        end += 1

    # global slug counter (GitHub suffixes duplicates in whole-document order)
    seen = {}
    entries = []
    in_summary = False           # inside the "What's new" block (before "## 1.")
    started = False              # passed the "What's new" h2
    for ln in lines[end:]:
        lvl, text = heading(ln)
        if lvl is None:
            continue
        slug = gh_slug(text, seen) if lvl <= 3 else None
        if lvl == 2 and not started:
            # first h2 after the TOC = the "What's new" summary heading
            started = True
            in_summary = True
            entries.append(f"- [{text}](#{slug})")
            continue
        if lvl == 2 and re.match(r"\d+\.", text):
            in_summary = False    # reached the numbered sections
        if in_summary:
            continue              # skip the summary's ### change items
        if lvl == 2:
            entries.append(f"- [{text}](#{slug})")
        elif lvl == 3:
            entries.append(f"  - [{text}](#{slug})")
        # lvl >= 4: not in TOC

    new = lines[: toc_h + 1] + [""] + entries + [""] + lines[end:]
    out = "\n".join(new)
    old = open(path, encoding="utf-8").read()
    if out != old:
        open(path, "w", encoding="utf-8").write(out)
    return out != old


codes = sys.argv[1:] or [
    f[len("3X-UI-MANUAL."):-3] for f in sorted(glob.glob("3X-UI-MANUAL.*.md"))
]
for code in codes:
    p = f"3X-UI-MANUAL.{code}.md"
    changed = rebuild(p)
    print(f"  {'✎' if changed else '·'} {p}")

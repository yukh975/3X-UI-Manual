#!/usr/bin/env python3
"""Split a manual file into chunk-00 (header+summary+TOC) + chunk-01..16 (one
per `## N.` section) for per-section translation.
Usage: python3 scripts/lib/split.py 3X-UI-MANUAL.ru.md /tmp/src
"""
import sys, os, re
src, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
s = open(src, encoding="utf-8").read()
i1 = s.index("\n## 1. ") + 1
open(f"{outdir}/chunk-00.md", "w", encoding="utf-8").write(s[:i1])
rest = s[i1:]
idxs = [m.start() for m in re.finditer(r'(?m)^## \d+\. ', rest)] + [len(rest)]
for k in range(len(idxs) - 1):
    sec = rest[idxs[k]:idxs[k+1]]
    n = int(re.match(r'## (\d+)\. ', sec).group(1))
    open(f"{outdir}/chunk-{n:02d}.md", "w", encoding="utf-8").write(sec)
print(f"split {src} -> {outdir} ({len(idxs)} chunks)")

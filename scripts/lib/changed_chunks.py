#!/usr/bin/env python3
"""Print the chunk numbers (00..16) whose content differs between two manual
versions — i.e. the sections that must be re-translated on a version bump
(incremental translation; unchanged sections keep their existing translations).
chunk-00 = header + "What's new" summary + TOC (almost always changes).

Usage: python3 scripts/lib/changed_chunks.py OLD.md NEW.md
  e.g. OLD = `git show <vPREV-commit>:3X-UI-MANUAL.ru.md` piped to a temp file.
Prints space-separated changed chunk codes, e.g.:  00 06 08 11 16
"""
import sys, re


def chunks(path):
    s = open(path, encoding="utf-8").read()
    i1 = s.index("\n## 1. ") + 1
    out = {"00": s[:i1]}
    rest = s[i1:]
    idxs = [m.start() for m in re.finditer(r'(?m)^## \d+\. ', rest)] + [len(rest)]
    for k in range(len(idxs) - 1):
        sec = rest[idxs[k]:idxs[k + 1]]
        n = int(re.match(r'## (\d+)\. ', sec).group(1))
        out[f"{n:02d}"] = sec
    return out


old, new = chunks(sys.argv[1]), chunks(sys.argv[2])
changed = sorted(k for k in new if new[k] != old.get(k))
print(" ".join(changed))

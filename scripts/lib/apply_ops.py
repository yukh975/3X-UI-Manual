#!/usr/bin/env python3
"""Apply anchored edit ops (from the per-section integration workflow) to the
manual files. ops JSON = {"sections":[{"num","ru_ops","en_ops",...}]} (or wrapped
as {"result":{"sections":[...]}}). Each op = {"mode":"insert_after"|"replace",
"anchor","text"}; anchors must be unique in the file.
Usage: python3 scripts/lib/apply_ops.py <ops.json> <ru.md> <en.md>
"""
import json, sys

ops_path, RU, EN = sys.argv[1], sys.argv[2], sys.argv[3]
data = json.load(open(ops_path))
sections = data.get("sections") or data.get("result", {}).get("sections", [])


def apply(path, key):
    s = open(path, encoding="utf-8").read()
    applied = skipped = 0
    for sec in sorted(sections, key=lambda x: x["num"]):
        for op in sec.get(key) or []:
            a, t, m = op["anchor"], op["text"], op["mode"]
            if s.count(a) != 1:
                skipped += 1
                print(f"  SKIP §{sec['num']} {m}: anchor x{s.count(a)} :: {a[:50]!r}")
                continue
            s = s.replace(a, (a + "\n\n" + t.strip()) if m == "insert_after" else t, 1)
            applied += 1
    open(path, "w", encoding="utf-8").write(s)
    print(f"  {path}: applied {applied}, skipped {skipped}")


apply(RU, "ru_ops")
apply(EN, "en_ops")

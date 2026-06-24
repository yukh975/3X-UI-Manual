#!/usr/bin/env python3
"""Assemble translated chunks back into a manual file.
Usage: python3 scripts/lib/assemble.py <code> <chunkdir> [outfile]
"""
import sys, glob, os
code = sys.argv[1]
chunkdir = sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else f"3X-UI-MANUAL.{code}.md"
chunks = sorted(glob.glob(os.path.join(chunkdir, "chunk-*.md")))
if len(chunks) != 17:
    raise SystemExit(f"{code}: expected 17 chunks, got {len(chunks)}")
parts = [open(c, encoding="utf-8").read().strip("\n") for c in chunks]
open(out, "w", encoding="utf-8").write("\n\n".join(parts) + "\n")
print(f"assembled {out} from {len(chunks)} chunks")

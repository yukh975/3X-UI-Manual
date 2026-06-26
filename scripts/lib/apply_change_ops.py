#!/usr/bin/env python3
"""Apply change-level edits to every language in place — translate only the diff.

The cost win: instead of re-translating whole CHANGED SECTIONS (often large, mostly
unchanged), translate only the CONTENT you insert and drop it into each language at
a LANGUAGE-NEUTRAL location. Untouched text is never re-translated or even rewritten.

A change op is located by things that are identical in every language:
  - `section`: a heading number ("11.2", "11" …) — numbers are ASCII everywhere.
  - `anchor` : a VERBATIM token that isn't translated (a code span like
    `FreedomStrategy`, a field name, an API path) appearing once in that section.
and carries the translated payload per language in `text`:

  { "changes": [
      { "section": "11.2", "where": "append",  "text": {"ru":"…","en":"…", …} },
      { "section": "11.2", "where": "after",  "anchor": "`FreedomStrategy`",
        "text": {"ru":"…","en":"…", …} },
      { "section": "6.9",  "where": "replace", "anchor": "`sniffing`",
        "text": {"ru":"…", …} }
  ] }

where ∈ append | after | before | replace. `append` adds the payload at the end of
the section; the others act on the paragraph containing `anchor` (unique in-section).
Only the RU payload is authored by hand; the other 11 are produced by translating
*just that payload* (workflow), so the bytes translated ≈ the bytes that changed.

Usage:  python3 scripts/lib/apply_change_ops.py ops.json [code ...]
        python3 scripts/lib/apply_change_ops.py --selftest
"""
import sys, re, json, glob


def find_section(lines, section):
    pat = re.compile(r"^(#{2,6})\s+" + re.escape(section) + r"\.\s")
    for i, l in enumerate(lines):
        m = pat.match(l)
        if m:
            return i, len(m.group(1))
    return None, None


def section_end(lines, start, level):
    sib = re.compile(r"^#{1," + str(level) + r"}\s")   # heading of level <= this one
    for i in range(start + 1, len(lines)):
        if sib.match(lines[i]):
            return i
    return len(lines)


def para_bounds(lines, lo, hi, anchor):
    hits = [i for i in range(lo, hi) if anchor in lines[i]]
    if len(hits) != 1:
        raise ValueError(f"anchor {anchor!r} found {len(hits)}x in section (need 1)")
    a = hits[0]
    s = a
    while s > lo and lines[s - 1].strip() != "":
        s -= 1
    e = a
    while e + 1 < hi and lines[e + 1].strip() != "":
        e += 1
    return s, e                                          # inclusive paragraph span


def apply_one(lines, ch, code):
    payload = ch["text"][code].split("\n")
    h, level = find_section(lines, ch["section"])
    if h is None:
        raise ValueError(f"section {ch['section']} not found")
    end = section_end(lines, h, level)
    where = ch["where"]
    if where == "append":
        j = end
        while j > h and lines[j - 1].strip() == "":
            j -= 1
        return lines[:j] + [""] + payload + [""] + lines[j:]
    s, e = para_bounds(lines, h + 1, end, ch["anchor"])
    if where == "after":
        return lines[:e + 1] + [""] + payload + lines[e + 1:]
    if where == "before":
        return lines[:s] + payload + [""] + lines[s:]
    if where == "replace":
        return lines[:s] + payload + lines[e + 1:]
    raise ValueError(f"unknown where: {where}")


def apply_file(path, code, ops):
    lines = open(path, encoding="utf-8").read().split("\n")
    n = 0
    for ch in ops["changes"]:
        if code in ch.get("text", {}):
            lines = apply_one(lines, ch, code)
            n += 1
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return n


def selftest():
    import tempfile, os
    doc = ("# T\n\n## 11. Xray\n\nIntro.\n\n### 11.2. General\n\n"
           "A line with `FreedomStrategy` token.\n\nTail of 11.2.\n\n"
           "### 11.3. Routing\n\nOther.\n")
    ops = {"changes": [
        {"section": "11.2", "where": "after", "anchor": "`FreedomStrategy`",
         "text": {"ru": "RU added para."}},
        {"section": "11.2", "where": "append", "text": {"ru": "#### New sub\n\nbody"}},
    ]}
    f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
    f.write(doc); f.close()
    apply_file(f.name, "ru", ops)
    out = open(f.name).read(); os.unlink(f.name)
    assert "RU added para." in out
    assert out.index("RU added para.") < out.index("Tail of 11.2.")     # after anchor para
    assert out.index("#### New sub") < out.index("### 11.3. Routing")    # appended in 11.2
    assert out.index("Tail of 11.2.") < out.index("#### New sub")        # at section end
    print("selftest OK")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:
        selftest(); sys.exit(0)
    ops = json.load(open(sys.argv[1], encoding="utf-8"))
    codes = sys.argv[2:] or [
        f.split("MANUAL.")[1][:-3] for f in sorted(glob.glob("3X-UI-MANUAL.*.md"))
    ]
    for code in codes:
        print(f"  {code:6} {apply_file(f'3X-UI-MANUAL.{code}.md', code, ops)} change(s)")

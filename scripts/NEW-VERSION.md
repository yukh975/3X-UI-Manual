# Releasing a new manual version — runbook

When 3X-UI ships a new panel version `vNEW`, the manual is updated end-to-end with
the steps below. `vPREV` = the version the manual currently documents (its `main`
version note). The mechanical steps are committed scripts; three steps are
multi-agent workflows (analysis, integration, translation) authored from the
templates in this repo's history.

Repos: upstream mirror `yukh/3x-ui` (GitLab id 15, `~/git/3x-ui`) for reading
source; this manual repo (`yukh/3X-UI-Manual`, id 20). RU is the source of truth.

## 1. Sync the mirror to upstream
```bash
cd ~/git/3x-ui
git fetch upstream --prune --tags
git push origin upstream/main:refs/heads/main          # FF main
git push origin refs/tags/vNEW                         # new tag BY NAME (never --tags)
git checkout main && git pull --ff-only
git worktree add ~/git/3x-ui-vNEW vNEW                 # source tree for agents
```

## 2. Freeze the previous version as a branch (BEFORE editing main)
```bash
cd ~/git/3X-UI-Manual
git branch vPREV main && git push origin vPREV         # main still = vPREV here
```
(Its README already embeds vPREV's "What's new". Branches exist only for previous
versions; never make a branch for the new latest — main IS it.)

## 3. Analyze changes — WORKFLOW
Multi-agent over `git -C ~/git/3x-ui log vPREV..vNEW`: 5 area agents + a
completeness critic → user-facing changes mapped to the 16 sections (skip
refactors/CI/deps/internal). Output JSON of changes per section.

## 4. Edit RU (canonical) on main — as CHANGE OPS, not section rewrites
- Write the **"Что нового в vNEW"** summary (RU): one `### N. <section title>` item per
  changed section, each with the bullets of what changed. Insert after the TOC and
  **remove the old "Что нового в vPREV"** section — match the FULL heading
  `"\n## 1. <title>\n"` (a bare `## 1.` also matches a summary `### 1.` item!). Bump the
  version note + README version to vNEW. (`whatsnew.py` later reformats the item headings
  to "<changes in section> N — <title>", so the section numbers don't look out of order.)
- Integrate features into the RU body as **change ops** — WORKFLOW (one agent per changed
  section) emitting `{section, where, anchor, text:{ru:…}}` where `section` is a heading
  number and `anchor` is a VERBATIM token (code span / field / API path present once in
  that section — identical in every language). `where` ∈ append|after|before|replace.
  Apply to RU only: `python3 scripts/lib/apply_change_ops.py ops.json ru`. **Keep ops.json —
  step 5 reuses it.**

## 5. Translate ONLY the inserted changes into every language — CHANGE-LEVEL, WORKFLOW
Never re-translate whole changed sections (mostly-unchanged text — huge waste). Translate
ONLY each op's payload + the small header prose, then drop them into each language IN
PLACE via the same language-neutral anchors; untouched prose is never rewritten.
```bash
# 1) translate payloads only: workflow fills ops.json text{} for the other 11 languages
#    (ch.text.ru -> en/uk/zh-CN/zh-TW/fa/ar/tr/pt/es/ja/id/vi). Bytes translated ≈ bytes changed.
# 2) apply the SAME ops to the 12 non-RU languages in place (RU already done in step 4):
python3 scripts/lib/apply_change_ops.py ops.json en uk zh-CN zh-TW fa ar tr pt es ja id vi
# 3) per-version header bits still need translating into each chunk-00: the "What's new"
#    bullets + version-note line (small workflow). Item TITLES = the section's existing
#    translated heading (copy it — do NOT re-translate). Then:
python3 scripts/lib/whatsnew.py        # reformat summary items -> "<changes in section> N — <title>" (localized)
python3 scripts/lib/switcher.py
python3 scripts/lib/toc.py             # rebuild every TOC from its headings (anchors can't drift)
PYTHONPATH=scripts/lib python3 scripts/lib/fixlinks.py   # repair body cross-refs after renumbering
python3 scripts/lib/checklinks.py      # GATE: every #anchor must resolve — must print all OK
# READMEs (all 13): bump the version literal in readme-shells.json, then:
python3 scripts/lib/build_readmes.py scripts/lib/readme-shells.json
```
Fallback only: if a section was reworked so heavily that change ops don't fit, re-translate
that one section via the old chunk path (`changed_chunks.py` → `split.py` → translate that
chunk → `assemble.py`). Prefer ops — they keep the translated bytes ≈ the changed bytes.
**`checklinks.py` is the release gate — it must report every language OK before you build PDFs/commit.** It models GitHub exactly: CommonMark fences (an info-string fence ```lang only OPENS — only a bare ``` closes) and GitHub's slug (keeps letters/numbers/**combining marks**/`_`/`-`/ZWNJ/ZWJ, drops punctuation, dup → -1/-2). Two real-bug classes it catches: (1) **swallowed headings** — an unclosed/ info-string-only fence runs on and renders later headings *as code* (they get no anchor); a one-off `scripts/lib/fixfence.py` closed such a fence in §10 that had hidden §11/11.1/11.2. Re-run `fixfence.py` only if `checklinks` shows whole sections missing. (2) **Unicode anchors** — GitHub keeps Persian ZWNJ **and** combining diacritics (kasra/hamza) and the Turkish dotted-i mark; pandoc keeps the marks but strips ZWNJ, so the committed Markdown keeps everything (GitHub) and `build-pdf.sh` strips only ZWNJ from link targets on its temp copy (PDF). If `checklinks` is green, both surfaces resolve.
**Anchor integrity (always run `toc.py` + `fixlinks.py` after assembly; expect 0 broken links).**
The TOC (chunk-00) and section headings (chunk-NN) are translated by separate
agents, so their wording drifts apart and the TOC's `#anchor` stops matching the
heading — `toc.py` rebuilds each TOC straight from the headings so they can't.
Gotchas it accounts for: (a) the "What's new" summary's `### N.` items reuse the
section titles, so on GitHub the **section** heading's anchor gets a `-1` suffix
(the summary item grabbed the bare slug first) — which sections collide changes
per release, so the anchors are computed dynamically, never hardcoded; (b) **fa
ZWNJ** (U+200C): GitHub *keeps* the zero-width joiner in anchors, pandoc *strips*
it — the committed Markdown keeps it (GitHub is primary), and `build-pdf.sh`
strips it from link targets on its temp copy so the PDF resolves too. `fixlinks.py`
re-points body refs left stale by renumbering (e.g. WireGuard 11.7→11.8) by
matching the anchor's topic (hyphen-insensitive for CJK), falling back to the
section number in the link text. Also normalize any localized digits a translator
introduced (e.g. fa Persian-Indic ۰-۹ → ASCII) — versions/ports/section numbers
must stay ASCII.
Never note that anything is translated from Russian. `build_readmes.py` rebuilds
every `README.<code>.md` (en = README.md) with the switcher, contents table, and
each language's new "What's new" summary (pulled from its manual); the README
shell prose is stable across bumps, so it is not re-translated. (The first
multi-language set was a one-time FULL bootstrap; all later bumps are incremental.)

## 6. Build all PDFs + ship
```bash
./scripts/build-pdf.sh                 # -> pdf/3X-UI-MANUAL.<code>.pdf (RTL ar/fa, CJK fonts)
git add -A && git commit && git push origin main
```
The push-mirror auto-syncs to GitHub (throttled ~5 min; branch *deletions* don't
propagate — `git push <gh-url> --delete <branch>` directly). Verify GitHub caught
up; remove `~/git/3x-ui-vNEW` and `/tmp/src` `/tmp/tr`.

## 7. Publish to upstream — Release + per-version PR (within a day or two of vNEW)
See memory `project-upstream-manual-pr` for the full recipe. In short:
- **GitHub Release** on `yukh975/3X-UI-Manual`: tag `vNEW` (push to GitLab origin first,
  then create the release on GitHub via `~/.gh-token`); assets = 13 PDFs +
  `3X-UI-Manual-md-<vNEW>.zip` (`zip -j` of the md). PDFs live here, NOT in upstream.
- **PR to `MHSanaei/3x-ui`** (fork `yukh975/3x-ui`; never push to upstream — PR only,
  confirm first): branch `docs/manual-<vNEW>` off `main`; put 13 `manual/*.md` + `manual/LICENSE`
  (md only — **no `manual/pdf/`**); add/refresh the README `## Documentation` section
  (links `manual/` + PDFs at `…/3X-UI-Manual/releases/latest`, cadence note, CC BY 4.0).
  First PR (3.4.1): MHSanaei/3x-ui#5592.

Languages (codes = panel locales): `ar en es fa id ja pt ru tr uk vi zh-CN zh-TW`.

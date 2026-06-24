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

## 4. Edit RU (canonical) on main
- Write the **"Что нового в vNEW"** summary (RU), translate to EN, insert after the
  TOC; **remove the old "Что нового в vPREV"** section — match the FULL heading
  `"\n## 1. <title>\n"` (a bare `## 1.` also matches the summary's `### 1.`
  subsection!); fix dead `#что-нового-в-*` anchors.
- Bump the version note + README version to vNEW; **embed the full vNEW summary in
  the README** (RU+EN).
- Integrate features into the body — WORKFLOW (one agent per section → anchored
  edit ops), then `python3 scripts/lib/apply_ops.py ops.json 3X-UI-MANUAL.ru.md 3X-UI-MANUAL.en.md`.

## 5. Regenerate ALL languages from RU — WORKFLOW
```bash
python3 scripts/lib/split.py 3X-UI-MANUAL.ru.md /tmp/src   # chunk the updated RU
# translation workflow: 11 langs × 17 chunks -> /tmp/tr/<code>/chunk-NN.md
for L in uk zh-CN zh-TW fa ar tr pt es ja id vi; do
  python3 scripts/lib/assemble.py "$L" "/tmp/tr/$L"        # -> 3X-UI-MANUAL.<L>.md
done
python3 scripts/lib/switcher.py                            # flag+native-name switcher in all files
```
EN is also re-translated/updated from RU. Never note that anything is translated
from Russian. Update the README contents table to list all 13 langs + their PDFs.

## 6. Build all PDFs + ship
```bash
./scripts/build-pdf.sh                 # -> pdf/3X-UI-MANUAL.<code>.pdf (RTL ar/fa, CJK fonts)
git add -A && git commit && git push origin main
```
The push-mirror auto-syncs to GitHub (throttled ~5 min; branch *deletions* don't
propagate — `git push <gh-url> --delete <branch>` directly). Verify GitHub caught
up; remove `~/git/3x-ui-vNEW` and `/tmp/src` `/tmp/tr`.

Languages (codes = panel locales): `ar en es fa id ja pt ru tr uk vi zh-CN zh-TW`.

#!/bin/bash
# Runs when a Claude Code cloud session starts on this repo. It installs what
# build_docx.py and check_chapters.py need, then puts a reminder in front of
# the session, so a fresh session starts from the project's rules and not from
# whatever the last chapters happen to look like.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

pip install -q python-docx playwright pyyaml >/dev/null 2>&1 || true

cat <<'MSG'
Bible_bot session start. Before anything else:
1. Read CLAUDE.md in full; it outranks every prompt. Then RENDERING_SPEC.md before rendering.
2. Fixed models (RENDERING_SPEC.md, "Fixed models"): compare your work against them, not only against the latest chapters.
3. Before every commit: python3 check_chapters.py (fix every ERROR), then python3 build_site.py && python3 progress.py.
MSG

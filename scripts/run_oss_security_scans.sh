#!/usr/bin/env bash
# Optional zero-cost OSS security scanners — skip gracefully if not installed.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "=== Optional OSS security scans (zero cost) ==="
ran=0

if command -v gitleaks >/dev/null 2>&1; then
  echo "--- gitleaks ---"
  gitleaks detect --source "$ROOT" --no-git -v 2>/dev/null || gitleaks detect --source "$ROOT" -v || true
  ran=1
else
  echo "SKIP gitleaks (install: https://github.com/gitleaks/gitleaks)"
fi

if command -v bandit >/dev/null 2>&1; then
  echo "--- bandit (Python) ---"
  bandit -r "$ROOT/scripts" -q -f txt || true
  ran=1
else
  echo "SKIP bandit (pip install bandit)"
fi

if command -v semgrep >/dev/null 2>&1; then
  echo "--- semgrep (community) ---"
  semgrep scan --config auto --error --quiet "$ROOT/scripts" 2>/dev/null || semgrep scan --config auto "$ROOT/scripts" || true
  ran=1
else
  echo "SKIP semgrep (pip install semgrep)"
fi

if [[ -f "$ROOT/requirements.txt" ]] && command -v pip-audit >/dev/null 2>&1; then
  echo "--- pip-audit ---"
  pip-audit -r "$ROOT/requirements.txt" || true
  ran=1
elif [[ -f "$ROOT/requirements.txt" ]]; then
  echo "SKIP pip-audit (pip install pip-audit)"
fi

if [[ $ran -eq 0 ]]; then
  echo "No optional OSS scanners installed — SEC-002 local script still satisfies Layer B."
fi
echo "=== OSS scan pass complete ==="

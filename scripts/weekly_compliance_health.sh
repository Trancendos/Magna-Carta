#!/usr/bin/env bash
# Weekly Magna Carta compliance documentation health check (zero cloud CI cost).
# Appends results to compliance/health_check_history.yaml via --log.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 required" >&2
  exit 1
fi

if ! python3 -c "import yaml" 2>/dev/null; then
  echo "ERROR: PyYAML required — pip install pyyaml" >&2
  exit 1
fi

echo "=== Magna Carta weekly compliance health check ==="
echo "Repository: $ROOT"
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo

python3 scripts/compliance_health_check.py --report --weekly-report --log --operator "${USER:-local}"

exit_code=$?
if [[ $exit_code -eq 0 ]]; then
  echo
  echo "OK — weekly health check complete (logged)."
else
  echo
  echo "FAILED — review findings above; logged for ISMS stand-up." >&2
fi
exit "$exit_code"

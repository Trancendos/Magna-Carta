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
health_exit=$?

echo
echo "=== Layer B automation readiness ==="
python3 scripts/readiness_automation_score.py --report
readiness_exit=$?

echo
echo "=== DPA system readiness ==="
python3 scripts/dpa_readiness_check.py --report
dpa_exit=$?

echo
echo "=== Security testing (SEC-002 local scan) ==="
python3 scripts/run_security_testing.py --report
security_exit=$?

echo
echo "=== Zero-cost tooling register (ZCT-001–011) ==="
python3 scripts/zero_cost_tooling_check.py --report
zct_exit=$?

exit_code=$health_exit
if [[ $readiness_exit -ne 0 ]]; then
  exit_code=$readiness_exit
fi
if [[ $dpa_exit -ne 0 ]]; then
  exit_code=$dpa_exit
fi
if [[ $security_exit -ne 0 ]]; then
  exit_code=$security_exit
fi
if [[ $zct_exit -ne 0 ]]; then
  exit_code=$zct_exit
fi
if [[ $exit_code -eq 0 ]]; then
  echo
  echo "OK — weekly health check complete (logged)."
else
  echo
  echo "FAILED — review findings above; logged for ISMS stand-up." >&2
fi
exit "$exit_code"

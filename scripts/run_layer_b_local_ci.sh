#!/usr/bin/env bash
# Local Layer B CI — 100% free; replaces GitHub Actions for this programme.
# No cloud CI minutes, no Aikido subscription required.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PATH="$ROOT/.tools:${HOME}/.local/bin:${PATH}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 required" >&2
  exit 1
fi

if ! python3 -c "import yaml" 2>/dev/null; then
  echo "Installing PyYAML..."
  python3 -m pip install -q -r "$ROOT/requirements.txt"
fi

echo "=== Layer B local CI (zero cloud cost) ==="
echo "Repository: $ROOT"
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo

fail=0

run_step() {
  local name="$1"
  shift
  echo "--- $name ---"
  if "$@"; then
    echo "OK  $name"
  else
    echo "FAIL $name" >&2
    fail=1
  fi
  echo
}

run_step "Compliance health" python3 scripts/compliance_health_check.py --report
run_step "Automation readiness" python3 scripts/readiness_automation_score.py --report
run_step "DPA readiness" python3 scripts/dpa_readiness_check.py --report
run_step "Security testing SEC-002" python3 scripts/run_security_testing.py --report
run_step "Zero-cost tooling ZCT" python3 scripts/zero_cost_tooling_check.py --report

if [[ -x "$ROOT/scripts/run_oss_security_scans.sh" ]]; then
  echo "--- OSS security stack SEC-006 (optional tools) ---"
  if "$ROOT/scripts/run_oss_security_scans.sh"; then
    echo "OK  OSS security stack"
  else
    echo "WARN OSS scan reported issues — review above" >&2
    fail=1
  fi
  echo
fi

if [[ $fail -eq 0 ]]; then
  echo "Layer B local CI: PASSED"
  exit 0
fi

echo "Layer B local CI: FAILED" >&2
exit 1

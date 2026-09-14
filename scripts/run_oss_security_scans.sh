#!/usr/bin/env bash
# OSS security stack (SEC-006) — 100% free Aikido alternative. Skips tools not installed.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PATH="$ROOT/.tools:${HOME}/.local/bin:${PATH}"

echo "=== OSS security scans SEC-006 (zero cost, no SaaS) ==="
ran=0
fail=0

# Which scanners actually ran, and which were absent. Until 2026-09-14 this script
# tracked only a boolean: if NO scanner was installed it printed a reassuring line
# and exited 0, and if SOME were installed it reported on those and said nothing
# about the rest. Layer B CI installs only requirements.txt, so every OSS scanner
# was absent on every run -- the tier has never executed in CI, and the exit code
# said clean the whole time.
#
# That is how an unresolvable `wcmatch==11.0` reached main behind a green Layer B
# check: pip-audit resolves each requirements file in a fresh virtualenv, so it is
# exactly the check that would have refused it, and it was never installed.
#
# OSS_SCAN_REQUIRED is a comma-separated list of scanners whose absence is a
# failure rather than a skip. A caller that believes this tier ran sets it; a
# developer without the stack installed does not, and still gets skips.
SKIPPED=""
REQUIRED="${OSS_SCAN_REQUIRED:-}"

if command -v gitleaks >/dev/null 2>&1; then
  echo "--- gitleaks ---"
  if gitleaks detect --source "$ROOT" --no-banner --redact 2>/dev/null; then
    echo "OK  gitleaks"
  else
    code=$?
    if [[ $code -eq 1 ]]; then
      echo "FINDINGS in gitleaks — review above" >&2
      fail=1
    else
      echo "WARN gitleaks exited $code" >&2
    fi
  fi
  ran=1
else
  echo "SKIP gitleaks (run ./scripts/install_zero_cost_security_stack.sh)"
  SKIPPED="$SKIPPED gitleaks"
fi

if command -v bandit >/dev/null 2>&1; then
  echo "--- bandit (Python scripts/) ---"
  if bandit -r "$ROOT/scripts" -q -ll -f txt; then
    echo "OK  bandit"
  else
    echo "FINDINGS in bandit — review above" >&2
    fail=1
  fi
  ran=1
else
  echo "SKIP bandit (pip install -r requirements-oss.txt)"
  SKIPPED="$SKIPPED bandit"
fi

if command -v semgrep >/dev/null 2>&1; then
  echo "--- semgrep (community auto rules) ---"
  if semgrep scan --config auto --error --quiet "$ROOT/scripts" "$ROOT/compliance" 2>/dev/null \
    || semgrep scan --config p/default --error --quiet "$ROOT/scripts" 2>/dev/null; then
    echo "OK  semgrep"
  else
    echo "FINDINGS in semgrep — review above" >&2
    fail=1
  fi
  ran=1
else
  echo "SKIP semgrep (pip install -r requirements-oss.txt)"
  SKIPPED="$SKIPPED semgrep"
fi

if command -v pip-audit >/dev/null 2>&1; then
  for req in requirements.txt requirements-oss.txt; do
    if [[ -f "$ROOT/$req" ]]; then
      echo "--- pip-audit ($req) ---"
      # Accepted findings are suppressed HERE, next to the scan, so the acceptance
      # is real rather than a comment the scanner never reads. Each --ignore-vuln
      # must have a written disposition in the requirements file it applies to.
      #
      # There are currently NO suppressions, and the empty list is the point.
      # Until 2026-09-11 three were passed unconditionally to BOTH requirements
      # files:
      #
      #   --ignore-vuln PYSEC-2026-3481 / -3482 / -3483   (mcp 1.23.3)
      #
      # They were justified by a disposition in requirements-oss.txt recording
      # that semgrep hard-pinned `mcp==1.23.3` and that forcing >=1.28.1 broke
      # semgrep. That stopped being true: semgrep 1.173.0 onwards declares
      # `Requires-Dist: mcp==1.29.0`, and mcp 1.29.0 carries zero OSV advisories
      # against six for 1.23.3. The disposition is retired in requirements-oss.txt.
      #
      # Removing the flags with it is not tidying. A suppression outliving its
      # disposition breaks the rule stated two lines above, and it fails in the
      # dangerous direction: pip-audit would keep silencing those three ids for
      # BOTH requirements files, so if a future resolve ever pulled a vulnerable
      # mcp back in, this scan would report OK and nobody would learn anything.
      # An advisory that no longer applies needs no flag; one that applies again
      # needs a fresh written disposition, not this one restored.
      if pip-audit -r "$ROOT/$req"; then
        echo "OK  pip-audit $req"
      else
        echo "FINDINGS in pip-audit $req — review above" >&2
        fail=1
      fi
      ran=1
    fi
  done
else
  echo "SKIP pip-audit (pip install -r requirements-oss.txt)"
  SKIPPED="$SKIPPED pip-audit"
fi

# A scanner that was not installed reported nothing, which is not the same as
# reporting nothing wrong. Say which, every run, so the difference is on the record
# even when nothing is required.
if [[ -n "$SKIPPED" ]]; then
  echo "BLIND — these scanners were not installed and looked at nothing:$SKIPPED" >&2
fi

if [[ -n "$REQUIRED" ]]; then
  missing=""
  for want in ${REQUIRED//,/ }; do
    if [[ " $SKIPPED " == *" $want "* ]]; then
      missing="$missing $want"
    fi
  done
  if [[ -n "$missing" ]]; then
    echo "FAIL required scanner(s) not installed:$missing" >&2
    echo "      OSS_SCAN_REQUIRED names them, so a blind run is a failed run here." >&2
    exit 1
  fi
fi

if [[ $ran -eq 0 ]]; then
  echo "No OSS scanners installed — SEC-002 local script still satisfies Layer B."
  echo "Install free stack: ./scripts/install_zero_cost_security_stack.sh"
  exit 0
fi

echo "=== OSS scan pass complete ==="
exit "$fail"

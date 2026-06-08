#!/usr/bin/env bash
# Install a user-level cron job for weekly compliance health checks.
# Does NOT use GitHub Actions or any cloud CI — runs only on this machine.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT/scripts/weekly_compliance_health.sh"
MARKER="# magna-carta-weekly-health-check"

if [[ ! -x "$SCRIPT" ]]; then
  chmod +x "$SCRIPT"
fi

CRON_LINE="0 8 * * 1 cd $ROOT && $SCRIPT >> $ROOT/docs/evidence/weekly-health-cron.log 2>&1 $MARKER"

existing="$(crontab -l 2>/dev/null || true)"
if echo "$existing" | grep -qF "$MARKER"; then
  echo "Cron entry already installed ($MARKER)."
  echo "Current matching line:"
  echo "$existing" | grep -F "$MARKER"
  exit 0
fi

{
  echo "$existing"
  echo "$CRON_LINE"
} | crontab -

echo "Installed weekly cron (Mondays 08:00 local):"
echo "  $CRON_LINE"
echo
echo "To remove: crontab -e and delete the line containing $MARKER"

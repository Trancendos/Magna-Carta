#!/usr/bin/env bash
# Install a local git pre-commit hook — runs Layer B checks before commit.
# No GitHub Actions; hook runs only on the developer machine.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK="$ROOT/.git/hooks/pre-commit"
RUNNER="$ROOT/scripts/run_layer_b_local_ci.sh"

if [[ ! -d "$ROOT/.git" ]]; then
  echo "ERROR: not a git repository" >&2
  exit 1
fi

chmod +x "$RUNNER"

cat > "$HOOK" <<EOF
#!/usr/bin/env bash
# Magna Carta Layer B pre-commit (local only — zero cloud CI cost)
set -euo pipefail
exec "$RUNNER"
EOF

chmod +x "$HOOK"
echo "Installed pre-commit hook: $HOOK"
echo "Runs: $RUNNER"
echo "Remove with: rm $HOOK"

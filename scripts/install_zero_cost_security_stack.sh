#!/usr/bin/env bash
# Install 100% free OSS security tools (no GitHub Actions, no Aikido subscription).
# Layer B mandatory checks remain local Python scripts; this enhances SEC-006.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

TOOLS_DIR="$ROOT/.tools"
GITLEAKS_VERSION="${GITLEAKS_VERSION:-8.24.2}"

echo "=== Zero-cost OSS security stack installer ==="
echo "Repository: $ROOT"
echo

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 required" >&2
  exit 1
fi

if ! python3 -m venv /tmp/.zct_venv_probe 2>/dev/null; then
  echo "WARN: python3-venv not available — pip-audit may fail until installed"
  echo "      Debian/Ubuntu: sudo apt install python3-venv"
else
  rm -rf /tmp/.zct_venv_probe
fi

echo "--- Python OSS scanners (bandit, semgrep, pip-audit) ---"
python3 -m pip install --upgrade pip
python3 -m pip install -r "$ROOT/requirements.txt" -r "$ROOT/requirements-oss.txt"

echo
echo "--- Gitleaks (secret scanner binary) ---"
mkdir -p "$TOOLS_DIR"
ARCH="$(uname -m)"
OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
case "$ARCH" in
  x86_64|amd64) GITLEAKS_ARCH="x64" ;;
  aarch64|arm64) GITLEAKS_ARCH="arm64" ;;
  *)
    echo "WARN: unsupported arch $ARCH — skip gitleaks binary; install manually"
    GITLEAKS_ARCH=""
    ;;
esac

if [[ -n "$GITLEAKS_ARCH" && "$OS" == "linux" ]]; then
  TARBALL="gitleaks_${GITLEAKS_VERSION}_linux_${GITLEAKS_ARCH}.tar.gz"
  URL="https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/${TARBALL}"
  TMP="$(mktemp -d)"
  if curl -fsSL "$URL" -o "$TMP/gitleaks.tgz"; then
    tar -xzf "$TMP/gitleaks.tgz" -C "$TOOLS_DIR"
    chmod +x "$TOOLS_DIR/gitleaks" 2>/dev/null || true
    echo "Installed: $TOOLS_DIR/gitleaks"
  else
    echo "WARN: could not download gitleaks — skip or install from https://github.com/gitleaks/gitleaks"
  fi
  rm -rf "$TMP"
fi

echo
echo "--- Verification ---"
export PATH="$TOOLS_DIR:${HOME}/.local/bin:${PATH}"
for cmd in bandit semgrep pip-audit; do
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "  OK  $cmd ($(command -v "$cmd"))"
  else
    echo "  FAIL $cmd not on PATH (expected under ~/.local/bin after pip install)" >&2
    exit 1
  fi
done

if [[ -x "$TOOLS_DIR/gitleaks" ]]; then
  echo "  OK  gitleaks ($TOOLS_DIR/gitleaks)"
elif command -v gitleaks >/dev/null 2>&1; then
  echo "  OK  gitleaks ($(command -v gitleaks))"
else
  echo "  --  gitleaks not installed (optional; SEC-002 still satisfies Layer B)"
fi

echo
echo "Run: ./scripts/run_oss_security_scans.sh"
echo "Full Layer B (no cloud CI): ./scripts/run_layer_b_local_ci.sh"

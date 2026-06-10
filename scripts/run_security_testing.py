#!/usr/bin/env python3
"""
Local continuous security testing (SEC-002).

Complements Aikido MCP (SEC-001) when MCP is not connected. Scans repository
content for high-risk secret patterns and dangerous shell constructs.

Usage:
  python3 scripts/run_security_testing.py [--report] [--strict]
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".cursor",
}
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".woff", ".woff2"}
TEXT_SUFFIXES = {
    ".py",
    ".sh",
    ".bash",
    ".yaml",
    ".yml",
    ".json",
    ".md",
    ".toml",
    ".env",
    ".ini",
    ".txt",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".sql",
    ".cfg",
    ".conf",
}


@dataclass
class SecurityFinding:
    check: str
    severity: str
    path: str
    line: int
    message: str


PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    (
        "private_key_pem",
        "error",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
    (
        "aws_access_key",
        "error",
        re.compile(r"AKIA[0-9A-Z]{16}"),
    ),
    (
        "github_pat",
        "error",
        re.compile(r"ghp_[A-Za-z0-9]{36,}"),
    ),
    (
        "github_oauth",
        "error",
        re.compile(r"gho_[A-Za-z0-9]{36,}"),
    ),
    (
        "slack_token",
        "error",
        re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    ),
    (
        "stripe_live_key",
        "error",
        re.compile(r"sk_live_[A-Za-z0-9]{20,}"),
    ),
    (
        "jwt_like",
        "warning",
        re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    ),
    (
        "high_entropy_secret",
        "warning",
        re.compile(
            r"(?i)(api[_-]?key|secret[_-]?key|password|token|private[_-]?key)\s*[=:]\s*['\"][^'\"]{20,}['\"]"
        ),
    ),
    (
        "committed_env_file",
        "warning",
        re.compile(r"^\.env(\.|$)"),
    ),
    (
        "dangerous_shell",
        "warning",
        re.compile(r"curl\s+[^|;\n]*\|\s*(?:ba)?sh"),
    ),
]


def iter_scan_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        if path.suffix and path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            ".env",
            ".env.local",
            ".env.production",
        }:
            continue
        files.append(path)
    return files


def scan_file(path: Path) -> list[SecurityFinding]:
    findings: list[SecurityFinding] = []
    rel = str(path.relative_to(ROOT))

    for check, severity, pattern in PATTERNS:
        if check == "committed_env_file":
            if path.name.startswith(".env") and "example" not in path.name.lower():
                findings.append(
                    SecurityFinding(
                        check,
                        severity,
                        rel,
                        0,
                        "Committed environment file — use .env.example and secrets manager",
                    )
                )
            continue

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings

    for lineno, line in enumerate(text.splitlines(), start=1):
        for check, severity, pattern in PATTERNS:
            if check == "committed_env_file":
                continue
            if pattern.search(line):
                if check == "high_entropy_secret" and "example" in line.lower():
                    continue
                if check == "aws_access_key" and "AKIA" in line and "EXAMPLE" in line.upper():
                    continue
                if check == "jwt_like" and (
                    "example" in line.lower() or "placeholder" in line.lower()
                ):
                    continue
                findings.append(
                    SecurityFinding(
                        check,
                        severity,
                        rel,
                        lineno,
                        f"Pattern matched: {check}",
                    )
                )
    return findings


def run_scan() -> list[SecurityFinding]:
    all_findings: list[SecurityFinding] = []
    for path in iter_scan_files():
        all_findings.extend(scan_file(path))
    return all_findings


def print_report(findings: list[SecurityFinding]) -> None:
    if not findings:
        print("OK — no local security testing findings.")
        return
    for f in findings:
        loc = f"{f.path}:{f.line}" if f.line else f.path
        print(f"[{f.severity.upper()}] {f.check} @ {loc}: {f.message}")
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = sum(1 for f in findings if f.severity == "warning")
    print(f"\nSummary: {errors} errors, {warnings} warnings")


def main() -> int:
    parser = argparse.ArgumentParser(description="Local security testing (SEC-002)")
    parser.add_argument("--report", action="store_true", help="Print findings")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on warnings")
    args = parser.parse_args()

    findings = run_scan()
    if args.report or findings:
        print_report(findings)

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

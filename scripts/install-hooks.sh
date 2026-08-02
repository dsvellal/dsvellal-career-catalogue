#!/usr/bin/env bash
# Install git pre-commit hook that runs the check script.
# Usage: ./scripts/install-hooks.sh

set -euo pipefail

HOOK_PATH=".git/hooks/pre-commit"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cat > "$HOOK_PATH" << 'HOOK'
#!/usr/bin/env bash
# Pre-commit hook: runs lint, format, types, spelling, and security checks.
# Bypass with: git commit --no-verify

echo "Running pre-commit checks..."
./scripts/check.sh lint types spell security

if [[ $? -ne 0 ]]; then
    echo ""
    echo "Pre-commit checks failed. Fix issues or bypass with: git commit --no-verify"
    exit 1
fi
HOOK

chmod +x "$HOOK_PATH"
echo "✓ Pre-commit hook installed at $HOOK_PATH"
echo "  Runs: lint, types, spelling, security (fast checks only)"
echo "  Full suite (with tests): ./scripts/check.sh"

#!/usr/bin/env bash
# scripts/check.sh — Single source of truth for all quality checks.
# Run locally: ./scripts/check.sh
# Run in CI:   ./scripts/check.sh
# Run subset:  ./scripts/check.sh lint test
#
# Exit codes: 0 = all passed, 1 = one or more checks failed.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BOLD='\033[1m'
NC='\033[0m'

FAILED=0
CHECKS_RUN=0
CHECKS_PASSED=0

run_check() {
    local name="$1"
    shift
    CHECKS_RUN=$((CHECKS_RUN + 1))
    printf "${BOLD}▶ %s${NC}\n" "$name"
    if "$@"; then
        printf "${GREEN}  ✓ %s passed${NC}\n\n" "$name"
        CHECKS_PASSED=$((CHECKS_PASSED + 1))
    else
        printf "${RED}  ✗ %s FAILED${NC}\n\n" "$name"
        FAILED=1
    fi
}

# Determine which checks to run (all if no args)
REQUESTED="${*:-all}"

should_run() {
    [[ "$REQUESTED" == "all" ]] || [[ "$REQUESTED" == *"$1"* ]]
}

# ─── LINT ─────────────────────────────────────────────────────────────────────
if should_run "lint"; then
    run_check "Ruff lint" uv run ruff check src/ tests/
    run_check "Ruff format" uv run ruff format --check src/ tests/
fi

# ─── TYPE CHECK ───────────────────────────────────────────────────────────────
if should_run "types"; then
    run_check "Mypy type check" uv run mypy src/twin/ --ignore-missing-imports
fi

# ─── TESTS ────────────────────────────────────────────────────────────────────
if should_run "test"; then
    run_check "Pytest" uv run pytest tests/ -q --tb=short
fi

# ─── SPELLING ─────────────────────────────────────────────────────────────────
if should_run "spell"; then
    if command -v typos &>/dev/null; then
        run_check "Spelling (typos)" typos src/ tests/ --config _typos.toml
    else
        printf "${YELLOW}  ⊘ Spelling skipped (install: brew install typos-cli)${NC}\n\n"
    fi
fi

# ─── SECURITY ─────────────────────────────────────────────────────────────────
if should_run "security"; then
    run_check "Bandit (SAST)" uv run bandit -r src/twin/ -c pyproject.toml -q
    if command -v gitleaks &>/dev/null; then
        run_check "Secrets (gitleaks)" gitleaks detect --source . --no-git --no-banner
    else
        printf "${YELLOW}  ⊘ Secrets check skipped (install: brew install gitleaks)${NC}\n\n"
    fi
fi

# ─── DEPENDENCIES ─────────────────────────────────────────────────────────────
if should_run "deps"; then
    run_check "Vulnerability audit (pip-audit)" uv run pip-audit --ignore-vuln PYSEC-2026-311
    run_check "License compliance (no AGPL)" bash -c "! uv run pip-licenses --order=license | grep -qi 'AGPL'"
fi

# ─── SUMMARY ──────────────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [[ $FAILED -eq 0 ]]; then
    printf "${GREEN}${BOLD}All %d checks passed ✓${NC}\n" "$CHECKS_RUN"
else
    printf "${RED}${BOLD}%d/%d checks failed ✗${NC}\n" "$((CHECKS_RUN - CHECKS_PASSED))" "$CHECKS_RUN"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

exit $FAILED

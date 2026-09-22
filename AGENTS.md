# Repository Agent Contract

## Micro-Automations
Execute repository tasks through standard deterministic wrappers:
- **Run Verification & Compliance:** `.agents/bin/run-ci` (or `task ci`)
- **Sanitize Raw Archive:** `.agents/bin/sanitize-data` (or `task sanitize`)
- **Audit Compliance Boundary:** `.agents/bin/audit-compliance` (or `task audit`)
- **Smart Git Commit:** `.agents/bin/git-smart-commit` (or `task commit`)
- **Launch Development Server:** `task dev`

## Constraints & Boundaries
- NEVER commit raw internal files, customer names, or non-redacted metrics.
- All evidence must follow the Systemic Intervention pattern (Default Trajectory → Decision → Intervention → Observable Consequence).
- Run `.agents/bin/audit-compliance` before any commit.
- Load extended workflow skills on demand from `.agents/skills/<name>/SKILL.md`.

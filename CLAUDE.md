# Project Instructions

## Intent-First Workflow

Every prompt is an **intent**, not an instruction. Before acting:

1. Convert the intent into actionable instructions by interviewing the user.
2. Ask clarifying questions **one at a time**, only when you would otherwise need to assume something or make a decision.
3. Each question must present multiple options with rationale, pros, and cons.
4. Explicitly state your recommended choice with reasoning.
5. Do not proceed with implementation until the intent is fully clarified.

## Traceability

Every piece of work must be fully traceable — from intent through decisions to implementation. This means:

1. **Before work:** Record the prompt in `prompts.md` with a timestamp.
2. **During work:** Record any decisions in `decisions.md` with alternatives considered.
3. **After work:** Update all affected project files (see table below) and write `handover.md`.

## Project Files

The following files are maintained at the repo root. After every prompt execution, consider each file for updates:

| File | Purpose |
|------|---------|
| `handover.md` | Session continuity — current state, in-progress work, next steps, blockers. Always written last. |
| `plan.md` | Execution plan with task status tracking |
| `prompts.md` | All prompts given to Claude, time-logged |
| `decisions.md` | Structured, time-stamped decisions with alternatives considered |
| `architecture.md` | System architecture and component interactions |
| `high-level-design.md` | High-level design of the solution |
| `low-level-design.md` | Low-level design for every component |
| `user-flows.md` | How the user derives value from the product |
| `test-cases.md` | Golden tests and integration tests |
| `README.md` | Project overview, structure, and intent |
| `SETUP.md` | Instructions for local project setup |
| `.gitignore` | Files excluded from git commits |

## Handover Protocol

Every prompt execution **must** end by writing/updating `handover.md`. This file enables any future session to resume work without context loss, even after an abrupt termination. It must contain:

- **Last completed action** — what was just finished
- **Current state** — what phase/task the project is in, what's working
- **In-progress work** — anything started but not yet finished
- **Next steps** — the immediate next actions to take
- **Blockers** — anything preventing progress
- **Key context** — decisions, constraints, or facts a new session needs to know

## Code Change Protocol

With any code change, update the code **and** all project files affected by the change.

## Verification

Always verify your work. Demonstrate verification through:
- Test cases
- Examples
- Screenshots (where applicable)

## Browser Automation

Use `agent-browser` for all web automation tasks. It is installed globally (`agent-browser --version` to confirm). Chrome is pre-downloaded at `~/.agent-browser/browsers/`.

**Before running any `agent-browser` command, load the live skill content:**

```bash
agent-browser skills get core        # workflows, patterns, troubleshooting
agent-browser skills get core --full # full command reference + templates
```

**Core workflow:**

1. `agent-browser open <url>` — navigate to page
2. `agent-browser snapshot -i` — get interactive elements with refs (`@e1`, `@e2`, …)
3. `agent-browser click @e1` / `agent-browser fill @e2 "text"` — interact via refs
4. Re-snapshot after page changes

**Specialized skills** (load as needed):

```bash
agent-browser skills get electron     # Electron desktop apps (VS Code, Slack, Figma …)
agent-browser skills get slack        # Slack workspace automation
agent-browser skills get dogfood      # Exploratory testing / QA / bug hunts
```

**MCP server** (for use as a Claude Code MCP tool):

```json
{
  "mcpServers": {
    "agent-browser": { "command": "agent-browser", "args": ["mcp"] }
  }
}
```

Prefer `agent-browser` over any built-in browser automation or web-fetch tools for any task that requires navigating, interacting with, or screenshotting a real webpage.

## Model and Style

Use Claude Opus 5 for everything. If you are Claude Opus 5, start every response with a dad joke and end with a dad joke.

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

## Evidence Generation Protocol (MANDATORY)

Every piece of content ingested into this system **MUST** produce a detailed evidence file. This is non-negotiable — no ingestion is complete without evidence. The evidence enables full transparency and traceability when demonstrated in the UI.

### Structure

```
data/evidence/<year>/individual/<NNN>-<slug>.md   — one file per artifact
data/evidence/<year>/<theme>.md                    — thematic summaries (group related individual files)
data/evidence/INDEX.md                             — master index (always updated)
```

### Evidence File Format (per artifact type)

Every evidence file MUST contain:

```markdown
# Evidence: <title>

## Source
- **File:** `<filename>`
- **Date:** <ISO date>
- **Ingested:** <date of ingestion>
- **Channel:** <source channel>
- **Category:** <category>

## Metadata
<type-specific metadata — see below>

## Datta's Involvement
- **Role at time:** <role title>
- **Involvement type:** <Author | Direct recipient — praised | CC'd — mentioned | etc.>

## Key Quotes
> <notable quotes demonstrating impact>

## Full Content
```<raw content>```
```

### Type-Specific Requirements

| Artifact Type | Required Metadata | Evidence Focus |
|---------------|-------------------|----------------|
| **Email (.eml/.msg)** | From, To, CC, Date, Thread depth, Attachments | Who said what, Datta's role in thread, praise/recognition quotes |
| **PDF** | Page count, Title, Author | Key claims, certifications, scores, assessments |
| **Image** | Dimensions, OCR text (if applicable), Description | What it shows, context of why it's evidence |
| **Presentation (.pptx)** | Slide count, Title, Author | Key slides content, what was presented, audience |
| **Spreadsheet (.xlsx/.csv)** | Sheet names, Row count | Metrics, data points, quantified achievements |
| **Document (.docx/.doc)** | Author, Title, Created date | Key sections, claims, formal statements |
| **Certificate** | Issuer, Date, Title, Credential | What was certified, significance |
| **Code/Markdown** | Repository, Path | What was built, technical contribution |
| **URL (internal)** | URL, Capture date, HTML snapshot saved | Full content preserved (will die after leaving company) |
| **URL (external)** | URL, Access date, Referenced in evidence | Link referenced; content summarized in evidence markdown |

### URL Handling Protocol (MANDATORY)

When any URL/link is shared:

1. **Determine if internal or external:**
   - **Internal:** Any URL containing `philips.com`, `share.philips.com`, `intranet.philips.com`, `engage.cloud.microsoft`, `teams.microsoft.com`, `philips.service-now.com`, `sonarqube.internal.philips`, or any other corporate/intranet domain
   - **External:** Everything else (public websites, YouTube, GitHub public, conference sites, etc.)

2. **For INTERNAL links (CRITICAL — content will be lost when employee leaves):**
   - Attempt to fetch and save the full HTML/content to `data/evidence/snapshots/<year>/<slug>.html`
   - If fetch fails (auth required), document the URL, timestamp, and whatever context is available
   - Record in evidence markdown: URL, capture date, snapshot path, and content summary
   - These snapshots are committed to git — they preserve evidence that will otherwise disappear

3. **For EXTERNAL links:**
   - Fetch content if possible (WebFetch) and summarize in the evidence markdown
   - Store the URL as a reference — do NOT snapshot (the content is publicly available and persistent)
   - Record in evidence: URL, access date, content summary, relevance to Datta's work

4. **Storage structure:**
   ```
   data/evidence/snapshots/<year>/<slug>.html    — internal link HTML snapshots
   ```

5. **In the evidence markdown, always include:**
   ```markdown
   ## References
   - **URL:** <the link>
   - **Type:** Internal/External
   - **Captured:** <date> (for internal) or **Accessed:** <date> (for external)
   - **Snapshot:** <path to saved HTML> (internal only)
   - **Status:** Captured / Auth-blocked / Available externally
   ```

**Rationale:** Internal Philips links (intranet, SharePoint, Viva Engage, Teams) will become inaccessible once the employee leaves the organization. Capturing their content NOW preserves critical evidence. External links are stable and can be referenced without snapshotting.

### Enrichment (MANDATORY alongside evidence)

When ingesting ANY artifact, Claude MUST also:

1. **Classify** the artifact (type, people, skills, projects, dates, claims, organizations)
2. **Create/resolve nodes** in the knowledge graph (people, skills, projects, achievements, time_ranges, organizations)
3. **Create edges** between nodes (USED_SKILL, COLLABORATED_WITH, RECOGNIZED_FOR, AT_ORG, DURING)
4. **Chunk** the text content for searchable retrieval
5. **Update** `data/evidence/INDEX.md` with the new entry

Claude IS the LLM that performs classification — no external API (Gemini or otherwise) is required. Use `scripts/enrich_emails.py::enrich_artifact()` or the local classifier in the pipeline.

### Thematic Summaries

After processing a batch of related artifacts, create a thematic summary that:
- Cross-references individual evidence files
- Tells the narrative arc (what happened, why it matters)
- Highlights Datta's specific contributions with quotes
- Lists leadership indicators and skills demonstrated
- Quantifies impact where possible (attendees, NPS scores, budget, teams reached)

### Index Updates

After every ingestion session, update `data/evidence/INDEX.md` with:
- New year sections (if applicable)
- Category breakdown table
- Thematic summary links
- Individual file index links

### No Exceptions

- Every artifact gets an evidence file — even if it seems low-value
- Every artifact gets enriched (nodes, edges, chunks) — even if entities are sparse
- Evidence files are committed to git (not gitignored)
- Screenshots of images/attachments should be referenced when relevant

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

## Post-Ingestion Commit Protocol

After every ingestion session that produces evidence files, Claude MUST:

1. **Stage** all new/modified files: `data/evidence/`, `data/evidence/INDEX.md`, thematic summaries
2. **Commit** with a descriptive message summarizing what was ingested (count, type, year range)
3. **Push** to remote (`git push`)

This ensures evidence is never lost to a terminated session. The commit message format:

```
Evidence: <brief description> — <count> artifacts (<year range>)
```

Example: `Evidence: Appreciation letters & certificates — 35 artifacts (2008-2026)`

## Model and Style

Use Claude Opus 5 for everything. If you are Claude Opus 5, start every response with a dad joke and end with a dad joke.

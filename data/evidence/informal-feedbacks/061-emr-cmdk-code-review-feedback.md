# Evidence: EMR CMDK Code Review Working Session — CI/CD Actions Feedback

## Source
- **File:** `20240209-EMR-CMDK-Code-Review-Feedback.png`
- **Date:** 2024-02-09
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Teams — Working session - CI/CD)
- **Category:** Informal Feedback

## Metadata
- **From:** Shetty, Nishwal (and team participants)
- **To/About:** Datta Vellal (session facilitator/contributor)
- **Context:** Working session on CI/CD where Datta shared 5 actionable items for improving PR workflows, code review processes, and SonarQube integration. The session covered conversation resolution before merging, PR comment analysis, ADO-to-GitHub linking, SonarLint in IntelliJ, and smoke tests as conditional checks.
- **Platform:** Microsoft Teams (Working session - CI/CD channel, 16 participants)

## Datta's Involvement
- **Role at time:** Principal Engineer / SW CoE
- **Involvement type:** Author — shared technical recommendations; Direct recipient — thanked for the session

## Key Quotes
> Nishwal Shetty: "thanks guys great session!"

## Actions Shared by Datta
1. Analysis of PR comments to continuously improve PRs through checklists/discipline/knowledge-share/automation of tasks
2. Checklist question to link ADO task to GitHub PR that connects different steps of development to establish traceability of task completion
3. Strictness of resolution of comments before merge, and enabling checks to block merge if the comment is not resolved
4. Installing and linking SonarLint in IntelliJ and the rules of SonarQube server (profile) to enable many sonarqube issues right at the IDE, and reduce cycle time of PR resolution
5. Ability to run sanity/smoke-tests as a conditional check for merge to main

## Full Content
```
[Working session - CI/CD | Chat | Files | Recap | Recordings & Transcr... | Breakout Rooms +2 | Join | 16 participants]

[Screenshot showing: "Require conversation resolution before merging" checkbox]
When enabled, all conversations on code must be resolved before a pull request can be merged into a branch that matches this rule.

Datta: we will enable this for all repos
[thumbs up x2] [heart x1] [celebrate x1]

09:57
Datta: Some actions I have noted down worth considering:

1. Analysis of PR comments to continuously improve PRs through checklists/discipline/knowledge-share/automation of tasks.
2. Checklist question to link ADO task to GitHub PR that connects different steps of development to establish traceability of task completion.
3. Strictness of resolution of comments before merge, and enabling checks to block merge if the comment is not resolved.
4. Installing and linking Sonarlint in IntelliJ and the rules of SonarQube server (profile) to enable many sonarqube issues right at the IDE, and reduce cycle time of PR resolution.
5. Ability to run sanity/smoke-tests as a conditional check for merge to main.

[thumbs up x3]

Shetty, Nishwal 10:02
i have to drop off as well
thanks guys great session!
```

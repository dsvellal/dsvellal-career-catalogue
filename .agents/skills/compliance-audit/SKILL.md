---
name: compliance-audit
description: Verifies strict data isolation, zero-raw-files leaks, and anonymization compliance across the repository.
---

# Compliance Audit Skill

## Zero-Raw-File Rules
1. Never commit or track `.pdf`, `.docx`, `.xlsx`, `.pptx`, or raw internal evaluation directories in git.
2. Anonymize proprietary internal codenames into functional descriptions (e.g., "proprietary telemetry orchestrator", "real-time diagnostic streaming engine").
3. Abstract confidential financial numbers into growth multiples or operational efficiency percentages.
4. Ensure all published claims reference sanitized verification anchors.

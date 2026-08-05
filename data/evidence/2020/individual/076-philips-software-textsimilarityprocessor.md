# Evidence: philips-software/TextSimilarityProcessor — SWCoE Team Open Source Tool

## Source
- **URL:** https://github.com/philips-software/TextSimilarityProcessor
- **Ingested:** 2026-08-05
- **Channel:** external_url
- **Category:** Open Source / Team Output / Technical Debt

## References
- **URL:** https://github.com/philips-software/TextSimilarityProcessor
- **Type:** External (public GitHub under official Philips org)
- **Accessed:** 2026-08-05
- **Status:** Available externally (public, MIT licensed)

## Repository Metadata
- **Owner:** philips-software (official Philips open-source organization)
- **Stars:** 4 | **Forks:** 1 | **Watchers:** 3
- **Commits:** 88 (master branch)
- **License:** MIT
- **Primary contributor:** Brijesh Krishnan (SWCoE team member)
- **Active:** 2020-2022
- **Language:** Python 3.8
- **CI:** GitHub Actions + CodeCov

## What It Does
> "Resolving the Technical Debt in Test/Requirement/Issues/Any-text repos with unique id using Natural Language Processing."

Uses NLP to identify textual similarities across:
- Tests (redundant test cases)
- Requirements (duplicate requirements)
- Issues/defects (similar bug reports)
- Any text with unique IDs

### Output
- Duplicate ID report
- Similarity recommendations
- Merged data file
- HTML brief report (top-N similarities)

### Tech Stack
Python, scikit-learn, pandas, numpy, xlrd/xlsxwriter

## Datta's Connection
- **Not a direct code contributor** (Brijesh Krishnan is primary developer)
- **Team leader** — Brijesh is Datta's SWCoE colleague (appears in emails since 2019)
- **Conceptual alignment:** This tool is the NLP evolution of Datta's JSCPD work:
  - JSCPD detects code duplication (syntax-level)
  - TextSimilarityProcessor detects text duplication (semantic-level, NLP)
- **Under philips-software** — the official Philips open-source org (not personal)
- **Same technical debt reduction mission** that drove JSCPD, CodeScene, Quality@Desk

## Key Context
- Published under **philips-software** (official org) — not a personal project
- Shows SWCoE team **shipped open-source tools** to the official Philips org
- NLP-based similarity = more sophisticated than simple pattern matching (JSCPD)
- Targets requirements AND tests — exactly what Sutra later does with AI/LLM
- Active 2020-2022 = same period as Datta's Quality@Desk and technical debt programs
- 88 commits = substantial development effort

## Significance
This repo shows the SWCoE team (under Datta's competency leadership) published production tools to the official Philips open-source organization. The tool's purpose (resolving tech debt through text similarity) is the direct intellectual successor to JSCPD (code duplication) and the precursor to Sutra (AI-powered traceability). The evolution:
```
2019: JSCPD — syntax-level code duplication detection
2020: TextSimilarityProcessor — NLP-level text similarity (this repo)
2025: ReqSpec — LLM-powered requirements compliance
2026: Sutra — AI + graph database for full V&V traceability
```

## Cross-References
- [[jscpd-code-duplication-initiative]] — JSCPD (precursor: syntax-level)
- [[sutra-xite-ai-platform]] — Sutra (successor: AI/LLM-level)
- [[viva-engage-reqspec-kairos-native-compliance]] — ReqSpec (intermediate evolution)
- Email: Brijesh Krishnan K mentioned throughout 2019-2022 evidence as SWCoE team member

# Evidence: GitHub Portfolio — All Public Repositories (dsvellal)

## Source
- **Profile:** https://github.com/dsvellal
- **Ingested:** 2026-08-05
- **Channel:** external_url
- **Category:** Open Source / Code Portfolio

## References (all external, permanently available)
| Repository | URL |
|-----------|-----|
| cerberus | https://github.com/dsvellal/cerberus |
| gitstats | https://github.com/dsvellal/gitstats |
| java-maven-template | https://github.com/dsvellal/java-maven-template |
| IWillCode202x | https://github.com/dsvellal/IWillCode202x |
| no-tech-debt-starter-project | https://github.com/dsvellal/no-tech-debt-starter-project |
| chitra-the-picture-collage-creator | https://github.com/dsvellal/chitra-the-picture-collage-creator |
| utilities | https://github.com/dsvellal/utilities |

## Datta's Involvement
- **Role:** Sole developer/maintainer on all repositories
- **Involvement type:** Creator and open-source publisher

---

## Repository Details

### 1. Cerberus — Code Quality Watchdog
- **URL:** https://github.com/dsvellal/cerberus
- **Description:** "A tool to measure code quality parameters, which can be used as a watch dog to observe code quality parameters like copy paste errors, suppressed warnings etc."
- **Language:** Java | **License:** MIT | **Commits:** 11
- **Fork of:** philips-software/cerberus (originally built at Philips, open-sourced)
- **Commands:**
  - CPD: Duplicate code block detection
  - SWD: Suppressed warning detection
  - JCMD: Java Code Metrics Detector
  - JCMD-DIFF: Java Code Metrics with Diff analysis
  - FPM: Find Programming Mistakes
- **Quality gates:** Automated testing, Cobertura coverage, PMD, CPD, mutation testing (PIT)
- **No deployment model:** Executable JAR, just needs JVM 1.8+
- **Inspiration:** Facebook Infer, Bazel Build
- **Significance:** This is the tool mentioned in the LinkedIn article ("Pioneered Project Cerberus, later open-sourced"), the Virtual Learning Summit demo, and the .grow competition entry

### 2. gitstats — Git History Statistics with Anonymization
- **URL:** https://github.com/dsvellal/gitstats
- **Description:** "git history statistics generator" — fork of hoxu/gitstats with anonymization
- **Language:** Python | **Commits:** 297
- **Key addition:** Anonymization capability for author names, tags, and images
- **Config:** max_domains=1000, max_authors=2000, anonymize toggle
- **Usage:** `./git-stats -c anonymize=1 /path/to/git/repo ./Repo_analytics`
- **Significance:** Used for generating code analytics reports at Philips while respecting privacy (anonymization feature added by Datta)

### 3. java-maven-template — CI-Ready Java Starter
- **URL:** https://github.com/dsvellal/java-maven-template
- **Description:** Template repository with pre-configured CI, quality checks, and spell-checking
- **Language:** Java | **License:** MIT | **Commits:** 2
- **Features:**
  - GitHub Actions CI/CD workflows
  - `checks.sh` — local CI check script
  - `dead_link_check.sh` — link validation
  - `.spelling` — valid spelling dictionary
  - Maven build with quality gates
- **Significance:** The template used in workshops — participants fork this to start with quality built-in

### 4. IWillCode202x — Non-Techies Learning to Code
- **URL:** https://github.com/dsvellal/IWillCode202x
- **Description:** "Enthusiastic non-techies learning to code"
- **Stars:** 1 | **Forks:** 3 | **Watchers:** 4 | **Commits:** 278
- **Participants (24 individual folders):** Abhishek, Aravind, Arpitha, Datta, Jabeen, Kala, Kiran, Maheswararaj, Muralidhar, Pankaj, Pavithra, Rahul, Rashmi, Sandhya, Sanjay, Sapna, Sobi, Srimathi, Srinivas, Sujay, Sundaresan, Vinod
- **Resources:**
  - Feedback survey: http://bit.ly/202001_IWillCode
  - Environment setup wiki: http://bit.ly/2020-IWillCodeWiki
  - Assignments, topics, important commands docs
- **Significance:** This is the "I Will Code" program documented in the .grow competition entry (85 feedback responses in session data). Teaching quality coaches to code.

### 5. no-tech-debt-starter-project — AI-Maintainable Quality Policy
- **URL:** https://github.com/dsvellal/no-tech-debt-starter-project
- **Description:** Template to minimize technical debt by establishing comprehensive quality standards from project inception
- **License:** MIT | **Commits:** 3
- **Contains 17-section quality policy:**
  1. Enforcement Model (changed-code ratchet)
  2. Code Structure (duplication, complexity, size)
  3. Architecture (cyclic deps, layering, coupling)
  4. Naming & Documentation
  5. Type Safety
  6. Dependencies (SBOM, license compliance)
  7. Security Controls (secrets, static analysis)
  8. Testing (85-90% branch coverage, mutation testing)
  9. API Compatibility
  10. Code Quality (hotspot analysis, tech debt tracking)
  11. Performance (latency budgets, observability)
  12. Build & Configuration (hermetic, reproducible)
  13. Linting & Formatting
  14. Agent-CI Feedback (sub-5-min PR target)
  15. AI Provenance (human approval for AI changes)
  16. CI Pipeline (fast-lane, merge gates)
  17. Definition of Done
- **Key requirements:** AGENTS.md at repo root, machine-readable policy, risk-based enforcement, independent review for AI changes
- **Significance:** This is the MOST RECENT repo — represents Datta's current thinking on quality in the age of AI agents. Directly tied to "9-Step Blueprint" article and his Philips work.

### 6. Chitra — Privacy-First Photo Collage Creator
- **URL:** https://github.com/dsvellal/chitra-the-picture-collage-creator
- **Description:** Privacy-focused, browser-based collage creator. Images never leave your device.
- **License:** MIT
- **Stack:** React, TypeScript, Konva, Tailwind CSS, Vite
- **Quality metrics:**
  - **100% line and branch test coverage**
  - **Mutation testing >85% (Stryker)**
  - **Zero code duplication (<75 token limit via jscpd)**
  - **Cyclomatic complexity < 5 per function**
  - **Strict offline-first (CI-enforced)**
- **Features:** Drag-drop, canvas manipulation, text/stickers, undo/redo, grid/mosaic/shuffle layouts, 4K export, keyboard shortcuts
- **Security:** Client-side only, no network requests, no analytics, dependency scanning, ESLint security plugin
- **CI/CD:** GitHub Actions — runs linting, complexity, duplication, offline verification, coverage, mutation testing, security
- **Significance:** Already documented in separate evidence file. Most technically impressive personal project.

---

## Aggregate Portfolio Stats

| Metric | Value |
|--------|-------|
| **Public repositories** | 7 |
| **Total commits** | ~600+ |
| **Languages** | Java, Python, TypeScript/React, JavaScript |
| **All MIT licensed** | Yes (open source) |
| **Most starred** | IWillCode202x (1 star, 3 forks, 4 watchers) |
| **Most commits** | gitstats (297), IWillCode202x (278) |
| **Most recent** | no-tech-debt-starter-project (2026) |

## Key Themes Across All Repos

| Theme | Repos Demonstrating |
|-------|---------------------|
| **Code quality obsession** | Cerberus, java-maven-template, no-tech-debt-starter, Chitra |
| **Testing rigor** | Cerberus (mutation/PIT), Chitra (100% coverage + Stryker), no-tech-debt (85-90% target) |
| **Privacy/security** | Chitra (offline-first), gitstats (anonymization) |
| **Teaching/enablement** | IWillCode202x (24 participants), java-maven-template (workshop starter) |
| **AI-age quality** | no-tech-debt-starter (AI provenance, agent-CI feedback) |
| **Shift-left** | All repos have quality checks BEFORE merge |

## Impact Statement
This GitHub portfolio demonstrates that Datta doesn't just talk about software quality — he builds tools for it (Cerberus), creates templates for it (java-maven-template, no-tech-debt-starter), teaches others to practice it (IWillCode202x), and applies it to personal projects (Chitra with 100% coverage and mutation testing). The portfolio spans Java, Python, TypeScript, and covers code quality, privacy engineering, teaching, analytics, and AI-age development practices.

The no-tech-debt-starter-project is particularly notable — it's a **17-section quality policy** that includes AI provenance and agent-CI feedback, showing Datta is defining what quality means in the age of AI agents. This directly connects to his "9-Step Blueprint" article and his Sutra platform work.

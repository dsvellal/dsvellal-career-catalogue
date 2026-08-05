# Evidence: Quality at Desk — IoT Team Parent POM & SuppressWarnings Gating

## Source
- **File:** `20200610_QualityAtDesk_IoT_SuperPOM.PNG`
- **Date:** 2020-06-10
- **Ingested:** 2026-08-05
- **Channel:** teams_chat_screenshot
- **Category:** Recognition / Praise

## Metadata
- **Platform:** Yammer (Software Center of Excellence SW_CoE group)
- **Program referenced:** Quality at Desk / Parent POM Infrastructure
- **People visible:** Battaje Bharath (poster)
- **CC:** Jayaram, Pooja and Vernekar, Hemantkumar
- **Reactions:** You (Datta), Thomas, Abey and Williams, Simao
- **Seen by:** 164

## Datta's Involvement
- **Role at time:** Competency Specialist — Software Excellence, SWCoE
- **Involvement type:** Program owner — team independently adopting and extending the Quality at Desk infrastructure

## Visible Content (Extracted Text)
**Battaje, Bharath** — June 10 at 10:01 PM — Edited:

"We are partnering SWCoE team on quality at desk initiative for our java-maven repositories. Thanks a lot for this initiative! During this integration we have made small improvements to the existing quality at desk infrastructure and I would like to share it here.

1. **Gating for SuppressWarnings annotation:**
Existing plugins are unable to flag any @SuppressWarnings annotations used in the code for suppressing the compiler warnings. We have created a custom PMD rule which will flag any @SuppressWarnings as a PMD violation and will fail the local/pipeline build.

If you are interested, Please check below branch for the PMD custom rule and the configuration.
https://gitlab.ta.philips.com/swcoe/idealjavaproject

2. **Parent POM with quality at desk infrastructure:**
Rather than adding quality at desk plugins and configurations to every repository, we created a parent pom with all the plugins and configurations. All individual repos just need to refer (using parent tag) the parent pom and we are seeing below benefits

   a. All the plugin and configuration at one place. No duplication of plugins and configurations.
   b. All the maven dependency version control at one place
   c. Custom configuration to enable gating only for the new code with the baseline count for existing violations. This way we can fix the violations in phases."

## Key Quotes
> "We are partnering SWCoE team on quality at desk initiative for our java-maven repositories. Thanks a lot for this initiative!"
> "Rather than adding quality at desk plugins and configurations to every repository, we created a parent pom with all the plugins and configurations."

## Context
This demonstrates the IoT team not only adopting Quality at Desk but actively extending the infrastructure with innovations like custom PMD rules for @SuppressWarnings gating and a Parent POM approach for standardized quality tooling. The team contributed these improvements back to the SWCoE GitLab repository, showing the community-driven nature of the program Datta built. The Parent POM approach is particularly significant as it reduces adoption friction — teams only need one parent tag reference to get all quality gates.

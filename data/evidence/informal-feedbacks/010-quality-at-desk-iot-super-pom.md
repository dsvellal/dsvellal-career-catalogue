# Evidence: Quality at Desk — IoT Team Adopts Parent POM & SuppressWarnings Gating

## Source
- **File:** `20200610_QualityAtDesk_IoT_SuperPOM.PNG`
- **Date:** 2020-06-10
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer - Software Center of Excellence SW_CoE)
- **Category:** Informal Feedback

## Metadata
- **From:** Battaje, Bharath
- **To/About:** SWCoE team (Datta is part of SWCoE team being thanked)
- **Context:** The IoT team shared their improvements to the Quality at Desk infrastructure after partnering with SWCoE. They created a custom PMD rule to gate @SuppressWarnings annotations and implemented a Parent POM to centralize quality plugins/configurations. Seen by 164 people.
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** You (Datta), Thomas, Abey and Williams, Simao reacted
- **cc:** Jayaram, Pooja and Vernekar, Hemantkumar

## Datta's Involvement
- **Role at time:** Senior Software Engineer / SW CoE
- **Involvement type:** Team member of SWCoE — credited team for the initiative

## Key Quotes
> "We are partnering SWCoE team on quality at desk initiative for our java-maven repositories. Thanks a lot for this initiative!"

> "During this integration we have made small improvements to the existing quality at desk infrastructure and I would like to share it here."

> "All individual repos just need to refer (using parent tag) the parent pom and we are seeing below benefits:
> a. All the plugin and configuration at one place. No duplication of plugins and configurations.
> b. All the maven dependency version control at one place
> c. Custom configuration to enable gating only for the new code with the baseline count for existing violations. This way we can fix the violations in phases."

## Full Content
```
Software Center of Excellence (SW_CoE)

Battaje, Bharath — June 10 at 10:01 PM — Edited

We are partnering SWCoE team on quality at desk initiative for our java-maven repositories. Thanks a lot for this initiative! During this integration we have made small improvements to the existing quality at desk infrastructure and I would like to share it here.

1. Gating for SuppressWarnings annotation:
Existing plugins are unable to flag any @SuppressWarnings annotations used in the code for suppressing the compiler warnings. We have created a custom PMD rule which will flag any @SuppressWarnings as a PMD violation and will fail the local/pipeline build.

If you are interested, Please check below branch for the PMD custom rule and the configuration.
https://gitlab.ta.philips.com/swcoe/idealjavaproject

2. Parent POM with quality at desk infrastructure:
Rather than adding quality at desk plugins and configurations to every repository, we created a parent pom with all the plugins and configurations. All individual repos just need to refer (using parent tag) the parent pom and we are seeing below benefits

    a. All the plugin and configuration at one place. No duplication of plugins and configurations.
    b. All the maven dependency version control at one place
    c. Custom configuration to enable gating only for the new code with the baseline count for existing violations. This way we can fix the violations in phases.

cc: Jayaram, Pooja and Vernekar, Hemantkumar

You, Thomas, Abey and Williams, Simao reacted to this
Seen by 164
```

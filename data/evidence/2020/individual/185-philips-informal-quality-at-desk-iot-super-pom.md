---
title: "Quality at Desk — IoT Team Super POM Parent POM with Quality Infrastructure"
date: 2020-06-10
year: 2020
era: Philips India
organization: Philips
category: Informal Feedback
source_type: image
channel: internal_screenshot
involvement: direct_recipient
role: SWCoE Competency Specialist
people: ["Battaje, Bharath", "Jayaram, Pooja", "Vernekar, Hemantkumar", "Thomas", "Abey", "Williams, Simao"]
skills: ["maven", "parent-pom", "pmd", "code-quality", "quality-at-desk", "ci-cd", "java"]
programs: ["Quality at Desk", "SW Center of Excellence"]
tags: ["informal-feedback", "yammer", "peer-recognition", "quality-at-desk", "iot", "super-pom", "maven", "pmd"]
sentiment: positive
impact_type: recognition
recurring: false
---

# Evidence: Quality at Desk — IoT Team Super POM Parent POM with Quality Infrastructure

## Source
- **File:** `quality-at-desk-iot-super-pom-2020.png`
- **Original:** `20200610_QualityAtDesk_IoT_SuperPOM.PNG`
- **Date:** 2020-06-10
- **Ingested:** 2026-08-06
- **Channel:** Yammer — Software Center of Excellence (SW_CoE) group
- **Category:** Informal Feedback

## Context
Battaje, Bharath from the IoT team posted in the SW CoE Yammer group sharing improvements the IoT team made while partnering with the SWCoE Quality at Desk initiative for their Java-Maven repositories. The post thanks the SWCoE team (implicitly including Datta as the Quality at Desk driver) and describes two key innovations: (1) a custom PMD rule to gate SuppressWarnings annotations, and (2) a Parent POM architecture that centralizes all quality-at-desk plugins and configurations. Post was seen by 164 people.

## Content

**Battaje, Bharath — June 10 at 10:01 PM — Edited:**

We are partnering SWCoE team on quality at desk initiative for our java-maven repositories. Thanks a lot for this initiative! During this integration we have made small improvements to the existing quality at desk infrastructure and I would like to share it here.

1. Gating for SuppressWarnings annotation:
Existing plugins are unable to flag any @SuppressWarnings annotations used in the code for suppressing the compiler warnings. We have created a custom PMD rule which will flag any @SuppressWarnings as a PMD violation and will fail the local/pipeline build.

If you are interested, Please check below branch for the PMD custom rule and the configuration.
https://gitlab.ta.philips.com/swcoe/idealjavaproject

2. Parent POM with quality at desk infrastructure:
Rather than adding quality at desk infrastructure plugins and configurations to every repository, we created a parent pom with all the plugins and configurations. All individual repos just need to refer (using parent tag) the parent pom and we are seeing below benefits:

a. All the plugin and configuration at one place. No duplication of plugins and configurations.
b. All the maven dependency version control at one place.
c. Custom configuration to enable gating only for the new code with the baseline count for existing violations. This way we can fix the violations in phases.

cc: Jayaram, Pooja and Vernekar, Hemantkumar

Reactions: You, Thomas, Abey and Williams, Simao reacted to this. Seen by 164.

## Key Quotes

> "We are partnering SWCoE team on quality at desk initiative for our java-maven repositories. Thanks a lot for this initiative!"
> — Battaje, Bharath

> "Rather than adding quality at desk infrastructure plugins and configurations to every repository, we created a parent pom with all the plugins and configurations."

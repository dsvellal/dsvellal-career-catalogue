---
title: "Simao Williams Praises Datta's Role Model Behavior — Know What You Do and Why"
date: 2020-09-23
year: 2020
era: Philips India
organization: Philips
category: Informal Feedback
source_type: image
channel: internal_screenshot
involvement: direct_recipient
role: SWCoE Competency Specialist
people: ["Williams, Simao"]
skills: ["technical-analysis", "code-quality", "superlinter", "checkstyle", "maven", "github-actions", "trade-off-analysis", "role-modelling"]
programs: ["Software Center of Excellence"]
tags: ["informal-feedback", "chat", "role-modelling", "technical-excellence", "peer-recognition"]
sentiment: positive
impact_type: recognition
recurring: false
---

# Evidence: Simao Williams Praises Datta's Role Model Behavior — Know What You Do and Why

## Source
- **File:** `data/evidence/images/2020/158-simao-role-modelling-feedback.png`
- **Date:** 2020-09-23
- **Ingested:** 2026-08-06
- **Channel:** Microsoft Teams chat with Williams, Simao
- **Category:** Informal Feedback — Technical peer recognition

## Context
Datta was collaborating with Simao Williams on the interview-questions repository, specifically working out how to configure Java code linting using Superlinter and Maven/Checkstyle. Datta had independently explored four different approaches, documented the pros and cons of each, and recommended Approach 2 (disabling Superlinter's Java check and keeping it in Maven for a single source of truth). Simao's response praised Datta's analytical rigor and explicitly called out his "role model behavior" for knowing both what to do and why.

## Content

**Datta's message (12:54 PM) — technical analysis shared:**

> I tried two approaches:
> 1. Superlinter template file specifying the custom rule that we want. Here's the build that succeeded: https://github.com/dsvellal/interview-questions/runs/1153452449
> Pros: Superlinter now checks for the rules that we define in the custom file.
> Cons: Maven isn't able to pickup custom_file from the linter folder (this has something to do with classpath and how maven works on reading through classpath entries in registering files and executing them). So, we'll have two sources of truth. Also, the name has to be sun_checks.xml – any other name isn't registered and superlinter may not pick it up (see this: https://github.com/dsvellal/interview-questions/actions/runs/268245624, I have named the custom xml as checkstyle.xml instead of sun_checks.xml). Another con is, that the maven test will also execute checkstyle checks and gate for any violations. I was wondering if I'd want to remove this check from mvn, but that'll mean we'll have to install superlinter locally and run. Plus, I do really want all checkstyle checks to be done locally via maven, because java is the crux of the program for this one.
>
> 2. Disabling superlinter check for java, and running it only via maven: https://github.com/dsvellal/interview-questions/runs/1153485550. Pros: This will also ensure that we have only single source of truth for the checkstyle configuration, checkstyle check executed only once (via maven). Cons: The checkstyle checks won't get executed via superlinter.

**Datta's recommendation (Edited):**

> Atleast for this project, I'd prefer approach 2 Simao, disabling superlinter check for java and keeping it in maven.

> There's a thrid option – add additional rules (or modify rules) to sun_checks.xml and put that in the "linters" folder to reflect our custom rules that's defined in checkstyle.xml (i did not explore this path)
>
> There's a forth option – comply to sun_checks.xml everywhere – this also doesn't fit our purpose of customizing rules that we want to run for our code. So, I did not explore this one too!

**Williams, Simao — 1:51 PM:**

> Great role model behavior for "know what you do, and know why you do it" Datta 🙂 .... good analysis of the pros and cons and good recommendation of an approach. For markdownlint, html, css, yaml and shellcheck (and others that I will add that are not for Java), are you happy for me to make a PR for superlinter with Java checks switched off? Nothing improtant about this for the interview questions repo – it is more a learning experiment and a demo of one trade-off configuration of superlinter which might help to show others? If not, no issues, I will continue to add the other linters to the existing shell script.

## Key Quotes

> "Great role model behavior for 'know what you do, and know why you do it' Datta ... good analysis of the pros and cons and good recommendation of an approach."
> — Williams, Simao

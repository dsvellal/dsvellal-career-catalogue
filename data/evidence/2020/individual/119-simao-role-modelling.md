# Evidence: Simao Williams — Role Model Praise for Datta's Technical Analysis

## Source
- **File:** `20200923_Simao_RoleModelling.PNG`
- **Date:** 2020-09-23
- **Ingested:** 2026-08-05
- **Channel:** teams_chat_screenshot
- **Category:** Recognition / Praise

## Metadata
- **Platform:** Microsoft Teams (Chat with Williams, Simao)
- **Program referenced:** Open Source / Superlinter / Code Quality Tooling
- **People visible:** Williams, Simao (Datta's colleague/lead); Datta's messages (blue/right side)

## Datta's Involvement
- **Role at time:** Competency Specialist — Software Excellence, SWCoE
- **Involvement type:** Direct recipient — praised for role model behaviour by senior colleague

## Visible Content (Extracted Text)
[Datta's message at 12:54 PM:]
"I tried two approaches:
1. Superlinter template file specifying the custom rule that we want. Here's the build that succeeded: https://github.com/dsvellal/interview-questions/runs/1153452449
Pros: Superlinter now checks for the rules that we define in the custom file.
Cons: Maven isn't able to pickup custom_file from the linter folder (this has something to do with classpath and how maven works on reading through classpath entries in registering files and executing them). So, we'll have two sources of truth. Also, the name has to be sun_checks.xml - any other name isn't registered and superlinter may not pick it up (see this: https://github.com/dsvellal/interview-questions/actions/runs/268245624, I have named the custom xml as checkstyle.xml instead of sun_checks.xml). Another con is, that the maven test will also execute checkstyle checks and gate for any violations. I was wondering if I'd want to remove this check from mvn, but that'll mean we'll have to install superlinter locally and run. Plus, I do really want all checkstyle checks to be done locally via maven, because java is the crux of the program for this one.

2. Disabling superlinter check for java, and running it only via maven: https://github.com/dsvellal/interview-questions/runs/1153485550. Pros: This will also ensure that we have only single source of truth for the checkstyle configuration, checkstyle check executed only once (via maven). Cons: The checkstyle checks won't get executed via superlinter."

[Edited message:]
"Atleast for this project, I'd prefer approach 2 Simao, disabling superlinter check for java and keeping it in maven."

[Simao's messages (green):]
"There's a third option - add additional rules (or modify rules) to sun_checks.xml and put that in the 'linters' folder to reflect our custom rules that's defined in checkstyle.xml (i did not explore this path)"

"There's a forth option - comply to sun_checks.xml everywhere - this also doesn't fit our purpose of customizing rules that we want to run for our code. So, I did not explore this one too!"

---Last read---

**Williams, Simao** 1:51 PM:
"Great role model behavior for 'know what you do, and know why you do it' Datta [emoji] .... good analysis of the pros and cons and good recommendation of an approach. For markdownlint, html, css, yaml and shellcheck (and others that I will add that are not for Java), are you happy for me to make a PR for superlinter with Java checks switched off? Nothing important about this for the interview questions repo - it is more a learning experiment and a demo of one trade-off configuration of superlinter which might help to show others? If not, no issues, I will continue to add the other linters to the existing shell script."

## Key Quotes
> "Great role model behavior for 'know what you do, and know why you do it' Datta"
> "good analysis of the pros and cons and good recommendation of an approach"

## Context
This is significant praise from Simao Williams (a senior colleague and SWCoE team lead) recognizing Datta's analytical approach to technical decisions. Datta methodically investigated two approaches to integrating Superlinter with custom checkstyle rules, documented the pros/cons of each with specific build run links as evidence, and made a reasoned recommendation. Simao called this "role model behavior" — specifically the principle of "know what you do, and know why you do it." This demonstrates Datta's engineering rigor and ability to make principled technical trade-offs, and that even his peers/seniors recognize him as a role model.

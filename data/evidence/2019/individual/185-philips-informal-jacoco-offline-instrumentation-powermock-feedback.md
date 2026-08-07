---
title: "JaCoCo Offline Instrumentation with PowerMock — Unit Test Workshop Credit"
date: 2019-08-20
year: 2019
era: Philips India
organization: Philips
category: Informal Feedback
source_type: image
channel: internal_screenshot
involvement: direct_recipient
role: SWCoE Competency Specialist
people: ["H M, Meghana", "Vellal, Dattatreya", "Kumar, Nataraj", "Kumar, Prashant", "Nuji, Shivaprashanth", "S C, Shiva Kumar"]
skills: ["unit-testing", "JaCoCo", "PowerMock", "JUnit", "code-coverage", "knowledge-sharing", "teaching"]
programs: ["Unit Test Workshop", "SWCoE"]
tags: ["informal-feedback", "yammer", "peer-recognition", "unit-testing", "jacoco", "powermock"]
sentiment: positive
impact_type: recognition
recurring: false
---

# Evidence: JaCoCo Offline Instrumentation with PowerMock — Unit Test Workshop Credit

## Source
- **File:** `data/evidence/images/2019/yammer-jacoco-offline-instrumentation-powermock-feedback-2019.png`
- **Date:** 2019-08-20
- **Ingested:** 2026-08-06
- **Channel:** Yammer — Software Center of Excellence (SW_CoE) group
- **Category:** Informal Feedback

## Context

Meghana H M posted in the SW_CoE Yammer group explaining a key technical insight about using PowerMock with JaCoCo for code coverage. The post specifically credits Datta (Vellal, Dattatreya) for sharing an excellent article on JaCoCo offline instrumentation during the Unit Test Workshop conducted by the SWCoE team. This is peer recognition posted publicly to the entire SW_CoE community (seen by 184 people), spreading a technical solution that solved a real problem: code tested with PowerMock showing 0% coverage in JaCoCo when using on-the-fly instrumentation.

The problem: JaCoCo's on-the-fly instrumentation is incompatible with PowerMock. The solution — switching to JaCoCo offline instrumentation — was learned from Datta's article shared in the workshop.

## Content

**Posted by:** H M, Meghana — August 20, 2019 at 02:43 PM
**Group:** Software Center of Excellence (SW_CoE)

> We make heavy use of **PowerMock** in many of our **JUnit** tests. However, For the code that is unit tested with powermock shows 0% coverage by JaCoCo.
> JaCoCo instruments the class to collect code coverage information. JaCoCo supports two ways class instrumentation:
> - On-the-fly with using Java Agent
> - Offline when classes are prepared during build phase
>
> Right now there is **NO WAY TO USE** PowerMock with JaCoCo On-the-fly instrumentation
> JaCoCo and powermock works well with **offline instrumentation**.
>
> Thanks a lot for the excellent article on **JaCoCo offline instrumentation** shared by **Vellal, Dattatreya** in **Unit Test Workshop** conducted by SWCoE team.
>
> Please refer attached file for JaCoCo configuration and get the expected **code coverage numbers**!!

**CC'd:** Vellal, Dattatreya; Kumar, Nataraj; Kumar, Prashant; Nuji, Shivaprashanth; and S C, Shiva Kumar

**Attachment:** `pom` — Software Center of Excellence (SW_CoE) › Files (JaCoCo configuration file)

**Reactions:** You, Nuji, Shivaprashanth, Hansen, Rodolfo, and Priyanka, Palla reacted to this
**Reach:** Seen by 184

## Key Quotes

> "Thanks a lot for the excellent article on **JaCoCo offline instrumentation** shared by **Vellal, Dattatreya** in **Unit Test Workshop** conducted by SWCoE team."

> "Right now there is **NO WAY TO USE** PowerMock with JaCoCo On-the-fly instrumentation — JaCoCo and powermock works well with **offline instrumentation**."

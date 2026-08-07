---
title: "Quality at Desk — Lombok Boilerplate Reduction Session, HSDP Team Adopts It"
date: 2020-04-08
year: 2020
era: Philips India
organization: Philips
category: Informal Feedback
source_type: image
channel: internal_screenshot
involvement: direct_recipient
role: SWCoE Competency Specialist
people: ["Gaidhani, Suyog", "Vellal, Dattatreya", "Hu, Aravind", "Jagadeesan, Sundaresan", "P, Rohith Kumar", "Elapanda, Ramakrishna", "Agrawal, Praveen", "Supakar, Sitangshu", "Hristov, Zoran", "Silveira, Matheus Soares"]
skills: ["java", "lombok", "code-quality", "boilerplate-reduction", "knowledge-sharing", "mentoring"]
programs: ["Quality at Desk", "SW Center of Excellence"]
tags: ["informal-feedback", "yammer", "peer-recognition", "quality-at-desk", "lombok", "hsdp", "java"]
sentiment: positive
impact_type: recognition
recurring: false
---

# Evidence: Quality at Desk — Lombok Boilerplate Reduction Session, HSDP Team Adopts It

## Source
- **File:** `quality-at-desk-lombok-boilerplate-reduction-hsdp-2020.png`
- **Original:** `20200408_QualityAtDesk_BoilerCodeReduction_Lombok_HSDP.PNG`
- **Date:** 2020-04-08
- **Ingested:** 2026-08-06
- **Channel:** Yammer — Software Center of Excellence (SW_CoE) group
- **Category:** Informal Feedback

## Context
Following a SW CoE team discussion a couple of weeks prior, Datta (Vellal, Dattatreya) and Hu, Aravind talked about Lombok — a small Java library that reduces boilerplate code. Suyog Gaidhani shared a detailed Yammer post describing the session, his team's experience adopting Lombok in HSDP Insights services (achieving nearly 24% reduction in duplication in key modules), and how the HSDP team found this directly applicable to their recently released HSDP De-Identification service. The post was seen by 204 people and generated multiple reactions.

## Content

**Gaidhani, Suyog — April 8 at 10:38 AM — Edited:**

During a discussion with the SW CoE Team a couple of weeks back, Vellal, Dattatreya and Hu, Aravind talked about a small Java library called as Lombok and extolled its virtues in reducing the boilerplate code that inevitably makes it way into any code base. The way in which Lombok works is via annotations that can be added to the Java class for which common methods are desired. These annotations are self-descriptive in their names and a few examples of these are @Getter, @Setter, @ToString and so on. Using these annotations, reduces duplication and also saves on the developer efforts.

I was suitably impressed and went back to my team to check why we shouldn't be using such a simple technique in our HSDP Insights services. The team was happy to report that they had already been doing so since last year when the team took this up to rein in our duplicate code KPI. Given that we have a fair number of DTO and Entity classes, using Lombok helped us to reduce nearly 24% of duplication in one of our key modules. Since then the team has been a regular user of the library including using it in our recently released HSDP De-Identification service.

Here is a simple code snippet on how code with and without Lombok looks and the difference is apparent:

[Code example showing AssociatedDTO class with and without @Getter/@Setter annotations — demonstrating the dramatic reduction in code from ~20 lines to ~5 lines]

In case, anyone would like to know more about using this in their code base, please feel free to reach out to P, Rohith Kumar, Elapanda, Ramakrishna and Agrawal, Praveen.

Thank you for the session Jagadeesan, Sundaresan!

cc: Vellal, Dattatreya, Supakar, Sitangshu, Elapanda, Ramakrishna, Hu, Aravind, P, Rohith Kumar, Agrawal, Praveen, and Jagadeesan, Sundaresan

Reactions: Hristov, Zoran, Silveira, Matheus Soares, Jagadeesan, Sundaresan, and 8 others reacted to this. Seen by 204.

## Key Quotes

> "During a discussion with the SW CoE Team a couple of weeks back, Vellal, Dattatreya and Hu, Aravind talked about a small Java library called as Lombok and extolled its virtues in reducing the boilerplate code..."

> "using Lombok helped us to reduce nearly 24% of duplication in one of our key modules"

> "Thank you for the session Jagadeesan, Sundaresan!"

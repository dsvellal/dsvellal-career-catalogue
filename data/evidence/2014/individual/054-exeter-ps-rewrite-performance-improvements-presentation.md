---
title: "IF Plan Selection Rewrite - Performance Improvements Presentation"
date: 2014-12-16
year: 2014
era: Exeter
organization: Exeter (Edifecs)
category: Do The Right Thing
source_type: presentation
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Jonah Egenolf", "Anuroop V. Gaonkar"]
skills: ["Performance Optimization", "Software Architecture", "Data Layer Design", "Liferay Portal", "Java", "Refactoring", "Technical Presentation"]
programs: ["OneGate"]
tags: ["presentation", "performance", "architecture", "rewrite"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: IF Plan Selection Rewrite - Performance Improvements Presentation

## Source
- **File:** `DoTheRightThing_PSRewritePerformanceImprovements_December16th2014.pptx`
- **Date:** 2014-12-16
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Do The Right Thing

## Metadata
- **Type:** Presentation (13 slides)
- **Project:** OneGate - IF Plan Selection
- **Audience:** Exeter engineering leadership

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author (presenter)

## Presentation Summary

### Architecture (Layered Approach)
- **Data Layer:** Abstraction of Siebel Entities into OneGate Entities
- **UI Layer:** Self-painting and self-validating pages, centralized tags, configurable UI flows
- **Biz Layer:** Centralized transformations and utilities

### Key Capabilities Delivered
- Configurable UI page-order
- Breadcrumb support on Plan Selection
- Extensive logging framework
- Context-based entity/message retrieval via XPaths
- Multi-language support
- Data Layer session-context sharing across portlets
- CORE vs State vs Implementation configuration flavors

### Improvements Achieved
- Reduced lines of code (significant % reduction shown in slides)
- Improved maintainability (unit-tested methods, centralized UI model)
- Improved readability (structured and templatized coding practices)
- Improved adoptability (high degree of reusability across portlets)

### Performance Results
- Before: ~16 seconds per page load
- After: ~1.5 seconds per page load (10.7x improvement)
- Test: 1 Household-Head Member on 3.3.2.10 revamped flow

## Key Quotes
> Architecture designed for: "Easy to adopt the design into other portlets. High degree of reusability."

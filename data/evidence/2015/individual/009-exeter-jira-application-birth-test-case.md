---
title: "JIRA Analysis - Regression Issues with Initial Application Birth Test Case"
date: 2015-08-05
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Taking Things To Conclusion
source_type: image
channel: internal_screenshot
involvement: author
role: Senior Lead - Software Development
people: ["Krishnamurthy Hegde", "Alana Reid", "Audra Podany"]
skills: ["Root Cause Analysis", "Oracle Policy Automation", "Technical Communication", "Tax-Household Logic", "Healthcare Domain"]
programs: ["OneGate"]
tags: ["jira", "screenshot", "aptc", "tax-household", "technical-analysis"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: JIRA Analysis - Regression Issues with Initial Application Birth Test Case

## Source
- **File:** `TakingThingsToConclusion_ApplicationBirthTestCase_August5th2015.JPEG`
- **Date:** 2015-08-05
- **Ingested:** 2026-08-06
- **Channel:** JIRA Screenshot (Internal)
- **Category:** Taking Things To Conclusion

## Metadata
- **Type:** JIRA ticket screenshot (ONEGATECORE-27173)
- **Project:** OneGate Core - 3.3.2.10 HF3
- **Ticket:** Regression Issues with Initial Application Birth Test Case

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author (detailed technical response)

## Technical Analysis Provided

Datta provided a comprehensive technical explanation on JIRA addressing a supposed regression:

### Key Points Made
1. In 3.3.2.10 HF1, the system did not have the right effective dating or tax-household structure. Since HF2, both are now correct.
2. The benefits start date (at BLI level) indicates the start of the benefit, which plan selection respects.
3. Plan-selection slicing always respects benefit-line-item start date for APTC.
4. Even though a tax-household structure exists before a benefit line-item start date, it is not necessary to distribute the benefit to the tax-household.
5. Politely pointed out that the "regression" was actually the *correct* behavior - HF1 was wrong, not HF2.

### Conclusion (3 points)
1. Plan-selection slicing always respects benefit-line-item start date for APTC
2. Even though a tax-household structure exists before a benefit line-item start date, it is not necessary to distribute the benefit to the tax-household
3. If we want to incorporate the APTC line-item to start from date of birth, we should consider having a discussion with OPA about broader impact

## Key Quotes
> "I would want to politely point out that we were not behaving the right way in 3.3.2.10 HF1"

> "Thanks for the detailed note, Datta" - Alana Reid

## Significance
Demonstrates deep domain expertise in healthcare enrollment (APTC, tax-household logic, OPA rules), diplomatic communication when correcting US-based team members, and taking ownership of complex cross-system technical issues.

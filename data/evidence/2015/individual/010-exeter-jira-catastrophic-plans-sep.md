---
title: "JIRA Analysis - State-Specific SEP for Catastrophic Plan Exemption"
date: 2015-08-05
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Taking Things To Conclusion
source_type: image
channel: internal_screenshot
involvement: author
role: Senior Lead - Software Development
people: ["Audra Podany"]
skills: ["Root Cause Analysis", "Technical Analysis", "Healthcare Domain", "Special Enrollment Logic", "Proactive Problem Solving"]
programs: ["OneGate"]
tags: ["jira", "screenshot", "catastrophic-plans", "special-enrollment", "technical-analysis"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: JIRA Analysis - State-Specific SEP for Catastrophic Plan Exemption

## Source
- **File:** `TakingThingsToConclusion_CatastrophicPlans_August5th2015.JPEG`
- **Date:** 2015-08-05
- **Ingested:** 2026-08-06
- **Channel:** JIRA Screenshot (Internal)
- **Category:** Taking Things To Conclusion

## Metadata
- **Type:** JIRA ticket screenshot (ONEGATECORE-24434)
- **Project:** OneGate Core
- **Ticket:** RT 6124: Add State-specific SEP Question regarding Exemption to Purchase Catastrophic Plan (TID075)

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author (proactive investigation and response)

## Technical Analysis Provided

Datta proactively investigated and explained the Special Enrollment logic:

### Investigation Steps
1. Checked code-base to identify if 15/16 logic for loss/gain of hardship was respected
2. Noticed that startDate = date-of-hardship-gain because loss/gain of hardship qualifying events haven't been handled
3. Searched existing documents (Special Enrollment Dates Logic, Coverage Integration Guide) to find references
4. Created a new JIRA (ONEGATECORE-27335) to address the 15/16 logic during gain/loss of hardship special enrollment

### Context Explained
- Configuration was done as part of JIRAs ONEGATECORE-26527 and ONEGATECORE-26715
- Fix ensured Special Enrollment dates for tax-household structure respect rules during qualifying events: Exceptional Circumstances, Carrier Contract Violation, or Exchange Error
- Flagged that the code does NOT interpret the 15/16 logic rule for loss/gain or hardship

### Proactive Action
Created ONEGATECORE-27335 as an enhancement JIRA and requested PMO team to decide priority.

## Key Quotes
> "Thank you so much for explaining the issue I was seeing. I really appreciate it." - Audra Podany

> "Yes, I will be happy to make sure the documentation is updated accordingly." - Audra Podany

## Significance
Demonstrates proactive investigation, deep healthcare domain knowledge (special enrollment periods, catastrophic plans, qualifying events), cross-team communication with US-based QA team, and creating proper tracking tickets for discovered gaps.

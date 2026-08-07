---
title: "Analysis Before Code Revamp Suggestion"
date: 2014-01-01
year: 2014
era: Exeter
organization: Exeter (Edifecs)
category: Do The Right Thing
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar", "Chandrashekhar Surendranath", "Krishnamurthy Hegde", "Satheesh Kumar Raju"]
skills: ["Data Layer", "JIRA", "Java", "Problem Solving", "Refactoring", "Release Management", "Root Cause Analysis", "Technical Excellence"]
programs: ["OneGate"]
tags: ["appreciation", "do-the-right-thing"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Analysis Before Code Revamp Suggestion

## Source
- **File:** `DoTheRightThing_AnalysisBeforeCodeRevampSuggestion_February21st2014.pdf`
- **Date:** 2014-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Do The Right Thing

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 2

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> To: Dattatreya Subramanya Vellal; Chandrashekhar Surendranath

## Full Content
```
Dattatreya Subramanya Vellal
From: Anuroop V. Gaonkar
Sent: Friday, February 21, 2014 3:52 PM
To: Dattatreya Subramanya Vellal; Chandrashekhar Surendranath
Cc: Krishnamurthy Hegde; Shrinidhi Irodi
Subject: RE: Root cause analysis of ONEGATECORE-13562
Follow Up Flag: Follow up
Flag Status: Completed
1000% Yes. Redesign & Refactoring both have to happen. Redesign – based on principles. Then refactor. Don’t
refactor before redesign.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India
From: Dattatreya Subramanya Vellal
Sent: Friday, February 21, 2014 2:08 PM
To: Chandrashekhar Surendranath
Cc: Krishnamurthy Hegde; Anuroop V. Gaonkar; Shrinidhi Irodi
Subject: RE: Root cause analysis of ONEGATECORE-13562
Hello Shekhar,
The issue: http://172.10.10.57:8080/jira/browse/ONEGATECORE-13562 hit us badly – with multiple reopens. The
root-cause analysis is given in the mail below and a good fix made to make sure that this does not occur again in
3.3.2.7hf3. As an outcome of this exercise, we have noticed that in our code base, we have code which is:
- Not required, but are not removed because its legacy code
- Intertwined with lot of conditional statements performing the same set of actions
- Highly non-modular, controlled by conditional statements
- Repetitive and/or dead
The above patterns are visible in –
- HealthPlanSelectionController.java of hixHealthPlan Portlet
- EmployerPlanSelectionController.java and jsps of EmployerPlanSelection Portlet
- Controllers of MyAccount and MyAccount-SHOP portlets
- Controllers of AnonymousPlanShopping and AnonEmployerPlanShop portlets
A phase-wise clean-up will definitely help us eliminate such errors in future. I foresee the following phases:
- Phase 1: Remove dead/unused code from controllers and jsps
- Phase 2: Modularize the code base within the controllers and jsps
- Phase 3: Pull out commonly used modules, and push them into a single utility module – so that code
maintenance becomes easy
I would like to run this by you to know if and when we can start off with phase 1, as an activity during our slack time
not affecting the release, and introduce these changes into a stream at an agreed time.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Peter Alphonso Mascarenhas
Sent: Friday, February 21, 2014 12:59 PM
1
To: Dattatreya Subramanya Vellal
Cc: Shrinidhi Irodi; Krishnamurthy Hegde; Anuroop V. Gaonkar; Dharnesh Yediyurappa; Satheesh Kumar Raju; Sachin
Shivarama Nayak
Subject: Root cause analysis of ONEGATECORE-13562
Hi Datta,
ONEGATECORE-13562 was an issue with blocking EE from adding the same product type plan if one already exists in
cart.
This was not implemented for the EE flow.
Fix made :
Generic method called and in brief check made against product type of plan in cart and added plan by EE.
Variable used is “String productType” under InsurancePlan Domain class.
***
```

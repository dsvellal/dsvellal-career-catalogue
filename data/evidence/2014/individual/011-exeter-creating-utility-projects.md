---
title: "Creating Utility Projects"
date: 2014-01-01
year: 2014
era: Exeter
organization: Exeter (Edifecs)
category: Do The Right Thing
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar", "Krishnamurthy Hegde"]
skills: ["Data Layer", "JIRA", "Problem Solving", "Technical Excellence"]
programs: ["OneGate"]
tags: ["appreciation", "do-the-right-thing"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Creating Utility Projects

## Source
- **File:** `DoTheRightThing_CreatingUtilityProjects_October14th2014.pdf`
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
> To: Dattatreya Subramanya Vellal; Anuroop V. Gaonkar; Anagha Joshi; Vinay Shivanna

## Full Content
```
Dattatreya Subramanya Vellal
From: Shrinidhi Irodi
Sent: Tuesday, October 14, 2014 2:21 PM
To: Dattatreya Subramanya Vellal; Anuroop V. Gaonkar; Anagha Joshi; Vinay Shivanna
Cc: Karthikeyan Vellingiri; Manasa Swamy; Sindhu Handalagere Suresh
Subject: RE: Learnings from ONEGATECORE-14710
HI Datta,
Yes. Manasa created the utility package and they are including it in 33.2.11 code base. And we can push many such
reusable code base into this jar but with appropriate package for each reusable code.
@KV,
Once Manasa checks-in the utility you can push the reusable code and let me know .
Regards,
Shrinidhi |Mobile: +91 9686824694 |skype: shrinidhi.irodi
From: Dattatreya Subramanya Vellal
Sent: Tuesday, October 14, 2014 2:09 PM
To: Anuroop V. Gaonkar; Anagha Joshi; Vinay Shivanna
Cc: Karthikeyan Vellingiri; Shrinidhi Irodi; Manasa Swamy; Sindhu Handalagere Suresh
Subject: RE: Learnings from ONEGATECORE-14710
Anuroop – we are going to centralize the logic, but compare may become a part of our “view” and not a library with
objects (and values) coming from DL. However, for 3.3.2.11, I know that Manasa and Sindhu have created a common
utility project called og-utility used to centralize address-verification process. Perhaps we can use that?
Marking Manasa, Sindhu – pls share details.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Anuroop V. Gaonkar
Sent: Tuesday, October 14, 2014 1:23 PM
To: Anagha Joshi; Vinay Shivanna
Cc: Dattatreya Subramanya Vellal; Karthikeyan Vellingiri; Shrinidhi Irodi
Subject: FW: Learnings from ONEGATECORE-14710
Vinay,
I believe you may have need for this in the Plan Selection. Are you already centralizing this in shared util library?
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India
From: Karthikeyan Vellingiri
Sent: Tuesday, October 14, 2014 12:35 PM
To: Shrinidhi Irodi
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde
Subject: Learnings from ONEGATECORE-14710
1
Hi Shrinidhi,
ONEGATECORE-14710 is fixed finally and OPS ticket has been raised.
While fixing this JIRA, I realised that the code related to Plan Comparison should be moved to a common location or
shared library which could be shared by the four portlets namely AnonEmployerPlanShop,
AnonymousPlanShoppingPortlet, EmployerPlanSelection, hixHealthPlan.
The FOUR above mentioned portlets have the same code related to Plan Comparison. It would be good if we could
move it to a shared library. This in turn will make the code changes, enhancements and the fixes easier. Also, this
would reduce the number of lines and increase code reusability.
Even a small change requires the fix from four portlets which in turn increases the LOE and the testing effort
although the same fix is made everywhere.
Please let me know your thoughts on this.
Regards,
Karthikeyan V
Karthikeyan Vellingiri
E X E T E R
Email ID: kvellingiri@exeter.com | Mobile: +91 90
```

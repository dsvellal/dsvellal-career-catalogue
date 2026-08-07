---
title: "Fix The Right Problem"
date: 2015-01-01
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Do The Right Thing
source_type: email
channel: email_archive
involvement: direct_recipient
role: Senior Lead - Software Development
people: ["Gaurav Gupta", "Jonah Egenolf"]
skills: ["JIRA", "Problem Solving", "Technical Excellence"]
programs: ["OneGate"]
tags: ["appreciation", "do-the-right-thing"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Fix The Right Problem

## Source
- **File:** `DoTheRightThing_FixTheRightProblem_August5th2015.pdf`
- **Date:** 2015-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Do The Right Thing

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 1

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Direct Recipient

## Key Quotes
> Subject: [JIRA] Ajinth Christudas mentioned you (JIRA)

## Full Content
```
Dattatreya Subramanya Vellal
From: EG JIRA
Sent: Wednesday, August 05, 2015 8:50 PM
To: Dattatreya Subramanya Vellal
Subject: [JIRA] Ajinth Christudas mentioned you (JIRA)
Follow Up Flag: FollowUp
Flag Status: Completed
Ajinth Christudas mentioned you on ONEGATECORE-27327
Re: RT: Issues with initial plan slices with exceptional circumstance
while RENEWALS period is ON
Hi Gaurav Gupta,
Thanks for the analysis. Dattatreya Vellal, Jonah Egenolf and I tried look at this again and we were
able to replicate this issue. We should reopen this ticket.
One thing I noticed was that the Open Enrollment configs were a little different when you executed
the test case to what I set up when I ran the case.
Here is the way the Open Enrollment periods should be set up. We are trying to mimic what would be
in VT LIVE
T T V ibhmrdtpca m h e on a h he ee o o e n a v r rd l e e i d ev ni g a rl e f it e l fi y l m t e e ne i is osc n bld p d e k e c t tc k t e h , l o .d a a a f me e a i n t , y l n d ti e t a oh o ne y ne d r o . . t
Once we did that we replicated the issue again. MCN: 1-7594529
Looks like the issue is not replicable in HF2EBF2, when we followed the same steps. I am not sure if
this issue occurs in HF3, but we should test and confirm that is not the case.
For now, VT plans to use the workaround laid out in ONEGATECORE-27328 to proceed with testing.
Thanks,
Ajinth
Add Comment
This message was sent by Atlassian JIRA (v6.2.3#6260-sha1:63ef1d6)
1
```

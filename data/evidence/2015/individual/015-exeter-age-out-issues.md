---
title: "Age Out Issues"
date: 2015-01-01
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Leadership & Ownership
source_type: email
channel: email_archive
involvement: direct_recipient
role: Senior Lead - Software Development
people: ["Brett Ackerman", "Chevy Vithiananthan", "Jonah Egenolf", "Lakshmi Thanga-Raja", "Sachin Shivarama Nayak"]
skills: ["Oracle Policy Automation", "Ownership", "Technical Leadership"]
programs: ["OneGate"]
tags: ["appreciation", "leadership-&-ownership"]
sentiment: positive
impact_type: leadership
recurring: false
---

# Evidence: Age Out Issues

## Source
- **File:** `Leadership&Ownership_AgeOutIssues_April3rd2015.pdf`
- **Date:** 2015-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Leadership & Ownership

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 4

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Direct Recipient

## Key Quotes
> To: Thomas Leong; Michael Poulshock; Lakshmi Thanga-Raja; Chandrashekhar

## Full Content
```
Dattatreya Subramanya Vellal
From: Jonah Egenolf
Sent: Friday, April 03, 2015 8:36 PM
To: Thomas Leong; Michael Poulshock; Lakshmi Thanga-Raja; Chandrashekhar
Surendranath; Chevy Vithiananthan; Dattatreya Subramanya Vellal; Satheesh Kumar
Raju; Sachin Shivarama Nayak
Cc: Brett Ackerman; Audra Podany; Dinesh Surajiwale
Subject: Re: age out issue
Follow Up Flag: Follow up
Flag Status: Completed
So we have a potential plan of action here. Lemme describe the problem first:
Any time we rate a plan, we use the start date of the plan slice as the age-relative date for rate band
calculations and household composition determinations. Sometime around 3329HF4 (or sometime before
now) we also changed rating to calculate the premium for the start of each future month when we enroll
in a plan. This was apparently a request from Hawaii so we respect the premiums as they increase
throughout the year or as someone ages throughout the year.
The impact on VT, however, is not very good. VT does not change premiums throughout the year, and they
do not rate by age. So the only thing that can happen is that a family that used to qualify for a given
household composition could now fall out of that qualification and into individual pricing. So for a family of
5 with a 26 year old son, their premium would go from about 2X (the family rate) to 5X (5 X the individual
rate). Meaning a 250% jump in premium even though there was no action on the part of the customer.
Note that this rerate problem will happen ANY time a customer's plans are rerated for any reason. So the
proactive future slice insertion exacerbates the problem, but the problem is already there.
And now my understanding of the desired behavior:
VT would like a member birthday to never impact household composition unless the case the member is
on is in an enrollment window (open, special, renewal). Note this means that household composition MAY
change (example: a couple signs up, later one of the couple dies, so they will switch to individual). Also
note that anything eligibility related is still left in the hands of OPA. We're really talking about control over
premium changes here.
And the potential solution:
We will add a system parameter that, if set to true, will ensure that the start date of the plan timeline_id is
used as the relative date for age calculations (for rating and for household composition) unless they are in
the add/remove member screen and are in a special enrollment period, in which case it will take the start
of the specific slice being rated as the relative date for age calculations. (If we do add/remove member in a
special enrollment period, we probably should create a new timeline_id so we use this slice start date for
any future rating. Otherwise the age relative date will revert to the start of the timeline if we rerate the
customer later outside of add/remove member. I think we should punt on this aspect of the problem,
though. It's an edge of an edge and should never be worse for the 
```

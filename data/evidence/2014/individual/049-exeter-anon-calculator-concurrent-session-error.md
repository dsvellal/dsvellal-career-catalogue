---
title: "Anon Calculator Concurrent Session Error"
date: 2014-01-01
year: 2014
era: Exeter
organization: Exeter (Edifecs)
category: Troubleshooting & Defect Ownership
source_type: email
channel: email_archive
involvement: direct_recipient
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar", "Chandrashekhar Surendranath", "Jonah Egenolf", "Krishnamurthy Hegde", "Lakshmi Thanga-Raja", "Robert Parks", "Sachin Shivarama Nayak"]
skills: ["Release Management", "Root Cause Analysis", "Troubleshooting"]
programs: ["OneGate"]
tags: ["appreciation", "troubleshooting-&-defect-ownership"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Anon Calculator Concurrent Session Error

## Source
- **File:** `TroubleShooting&DefectOwnership_AnonCalculatorConcurrentSessionError_November7th2014.pdf`
- **Date:** 2014-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Troubleshooting & Defect Ownership

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 8

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Direct Recipient

## Key Quotes
> To: Jonah Egenolf; Dharnish Yediyurappa; Lakshmi Thanga-Raja; Jaishankar Padmanabhan

## Full Content
```
Dattatreya Subramanya Vellal
From: Anuroop V. Gaonkar
Sent: Friday, November 07, 2014 3:57 PM
To: Jonah Egenolf; Dharnish Yediyurappa; Lakshmi Thanga-Raja; Jaishankar Padmanabhan
Cc: Chandrashekhar Surendranath; Srinivas Jillella; Shrinidhi Irodi; Krishnamurthy Hegde;
Robert Parks; Dattatreya Subramanya Vellal; Sachin Shivarama Nayak; Dharnish
Yediyurappa
Subject: RE: I am running 100 Users anonymous shopping right now.
Hello Jonah & Others,
The issue was related to thread(s) trying to push the requests through the same controller instance (Thanks Sachin
for helping piece together the piece of the puzzle). This controller instance was shared across all portlet
instances/threads as we configure controllers using spring’s applicationContext configuration. So multiple threads
accessed the same controller instance. The global session object in this single instance of the controller was getting
overwritten & some of the requests were failing.
Sachin is making changes to ensure that GlobalSession is not member variable of Controller in
AnonymousPlanShopping. This should ensure that failures don’t happen when multiple threads (higher loads) start
hitting the same controller.
1. Sachin and Datta looked at if there is similar incorrect usage of GlobalSession elsewhere. They have found
some other places where fix is needed (PlanDisenrollment). Sachin will do that. These fixes are part of EBF8
as of now. Whether these should be released etc. is Lakshmi/Shekhar/… call.
We have tested these fixes and results look promising – No errors with 20 concurrent users with 5 second
think time. We are now trying with 100 users (hope our system holds up & does not start cracking
elsewhere).
2. This made us realize that in some of the other controllers also we have instance variables that may get in to
inconsistent state when multiple requests are getting pushed through that controller concurrently. To
overcome this; we can either
a. Ensure that all developers understand that they MUST NOT define instance variables in Controller
for maintaining state information & use those variables in computations
OR
b. Set the controllers as Session Scope (using spring mechanism) - Thanks Shrinidhi for this. This will
have implication that we may bump up memory foot print a bit.
We should do this cleanup in Apollo or sooner as such things may lead to very bad unintended side effects.
SalesToolByProduct serialization error may be due to the fact that they have older release (EBF4) on which load
testing was done.
SalesToolByProduct error was already resolved by replacing that with OgSalesToolByProduct (a serializable entity)
and moving the instantiation to api cache. Hence as per the check done by Datta and team needed fixes are already
present in EBF6. Hence if HI tests with the right version the Serialization error should go away.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India
1
From: Jona
```

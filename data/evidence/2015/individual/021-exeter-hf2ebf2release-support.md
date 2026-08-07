---
title: "HF2EBF2Release Support"
date: 2015-01-01
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Release Support
source_type: email
channel: email_archive
involvement: direct_recipient
role: Senior Lead - Software Development
people: ["Chandrashekhar Surendranath", "Chevy Vithiananthan", "Krishnamurthy Hegde", "Lakshmi Thanga-Raja", "Satheesh Kumar Raju"]
skills: ["Portal Development", "Release Management", "Root Cause Analysis", "SOA", "Siebel"]
programs: ["OneGate"]
tags: ["appreciation", "release-support"]
sentiment: positive
impact_type: delivery
recurring: false
---

# Evidence: HF2EBF2Release Support

## Source
- **File:** `ReleaseSupport_HF2EBF2ReleaseSupport_August4th2015.pdf`
- **Date:** 2015-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Release Support

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 1

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Direct Recipient

## Key Quotes
> Cc: Lakshmi Thanga-Raja; Krishnamurthy Hegde; Chandrashekhar Surendranath; Jonah

## Full Content
```
Dattatreya Subramanya Vellal
From: Chevy Vithiananthan
Sent: Tuesday, August 04, 2015 4:09 PM
To: Ajinth Christudas
Cc: Lakshmi Thanga-Raja; Krishnamurthy Hegde; Chandrashekhar Surendranath; Jonah
Egenolf; Dattatreya Subramanya Vellal; Christopher Simo; Satheesh Kumar Raju; Tara
Noble; Michael Poulshock; VT-HIX-Core; Darren He; Christine Lai
Subject: Re: HF2EBF2 Testing Update
I guess we are good to go
Sent from my iPhone
On Aug 4, 2015, at 1:32 AM, Ajinth Christudas <achristudas@exeter.com> wrote:
Hello All,
Datta, Shekar and I met and found the root cause of the incorrect plan slices in HF2EBF2 during our
testing earlier in the day. It came down to one of the system preference values in Siebel. The system
preference value “OneGate Respect SESD On SEPCIR” had to be set to “Y” for the system to honor
the exceptional circumstance dates. Datta had already emailed these details yesterday and looks like
we overlooked that critical piece of information during testing (cid:1)
We noticed that in the 3.3.2.10HF2EBF2ESIPR1 instance the value was set to N. Once ESI came in, we
reset that value to Y, restarted the portal server and the og-plan-service in SOA. We then executed
the four scenarios that were earlier failing and we got them all to work. We also performed a simple
COC for change in income and the plan slices looked correct.
Scenario 1: OEP Closed, Exceptional Circumstance lesser than 60 days
MCN: 1-6748369
Scenario 2: OEP Closed, Exceptional Circumstance greater than 60 days
MCN: 1-6751019
Scenario 3: OEP Active; Exceptional Circumstance lesser than 60 days
MCN: 1-6752649
Scenario 4: OEP Active; Exceptional Circumstance Greater than 60 days
MCN: 1-6754229
In addition – The other good thing is that we don’t need the backdating scripts to update the tax
household dates in EBF2 unlike EBF1
Chevy, Chris,
I will leave it up to you to decide the next steps on shipping the release out.
Thanks again Datta and Shekar for the help and working through this with me! Much appreciated!
Thanks,
Ajinth
1
```

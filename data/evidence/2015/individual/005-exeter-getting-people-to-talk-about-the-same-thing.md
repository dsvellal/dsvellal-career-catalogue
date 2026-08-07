---
title: "Getting People To Talk About The Same Thing"
date: 2015-01-01
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Collaboration
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar", "Jonah Egenolf", "Robert Parks"]
skills: ["Data Layer", "Data Layer Design", "Oracle Policy Automation", "Siebel"]
programs: ["OneGate"]
tags: ["appreciation", "collaboration"]
sentiment: positive
impact_type: operational
recurring: false
---

# Evidence: Getting People To Talk About The Same Thing

## Source
- **File:** `Collaboration_GettingPeopleToTalkAboutTheSameThing_January7th2015.pdf`
- **Date:** 2015-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Collaboration

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 27

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> Block 1: Talks about the BIG picture. Where we do the intake, do the determination and persist the results back to

## Full Content
```
Dattatreya Subramanya Vellal
From: Dattatreya Subramanya Vellal
Sent: Wednesday, January 07, 2015 6:28 PM
To: Jonah Egenolf; Anuroop V. Gaonkar
Subject: RE: OPA Data Mapping
We discussed the following things.. (image below)
Block 1: Talks about the BIG picture. Where we do the intake, do the determination and persist the results back to
Siebel. The key point to note is persist is through DL, and determination is also through DL. They need not be tied
together, and they need not be sequential. It’s a promise from DL that when it has the right data, it will persist things
back, so from an application perspective, as long as data exists in DL, we are good.
Block 2: This expands the “Determination and Persist” block from block 1, and talks a bit more about how it is
structured. The data-layer which has the context, calls a biz.layer.method (let’s call it DetermineEligibility()) and then
the results are absorbed into DL, and DL decides to persist values back to Siebel (which is why the persist is in
parenthesis)
Block 3: This expands block 2’s biz.layer.method and defines what all the biz.layer method should do. This includes:
1. Getting the in-memory DL model for the context (mcn-based)
2. Get the in-memory-OPA-data-model corresponding to this (obtained by navigating through mcn?)
3. Constructing the Req.object to be passed while doing the eligibility-determination invocation, using the
model from 2
4. Parsing the Resp.object back into model from 2
5. Obtaining/Updating the model from 1, via model from 2
6. Persisting values into Siebel.
Block 4: This is another representation of block 3, indicating the work involved in doing the eligibility-determination
piece, that includes mapping and biz.layer.method writes from our end.
Block 5: This is mostly the transformation indication.
1
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
2
From: Jonah Egenolf
Sent: Wednesday, January 07, 2015 9:22 AM
To: Anuroop V. Gaonkar
Cc: Dattatreya Subramanya Vellal
Subject: Re: OPA Data Mapping
So I didn't get a chance to respond here, but I walked through a similar thing today with Datta today and I
think it might be best if you guys work through it together in person. Can you two walk through the
OPA/DL interaction and see where that leads?
- Jonah
From: Anuroop V. Gaonkar
Sent: Tuesday, January 06, 2015 8:20 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal
Cc: Robert Parks; Sajith Sanal; Vinay Shivanna
Subject: RE: OPA Data Mapping
Hello All,
Other key item that I & Srikanth figured out that all may not be equally aware of the “basic” challenge:
1. Taking the data from Siebel & Moving that to OPA – we are in the process of solving this.
2. Next comes the challenge of pushing the data coming from OPA in to Siebel via data layer (for example: a. in
application driven by OPA or b. data returned by OPA after eligibility). Here the DL should be able to take

```

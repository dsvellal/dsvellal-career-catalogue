---
title: "Feedback From SDT On Using XML Migration SOP"
date: 2016-06-01
year: 2016
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: ["Hari", "Thiru"]
skills: ["AWS RDS", "Documentation", "XML Processing"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Feedback From SDT On Using XML Migration SOP

## Source
- **File:** `201606_Feedback_From_SDT_On_Using_XML_Migration_SOP.pdf`
- **Date:** 2016-06-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Amazon)
- **Category:** Recognition

## Metadata
- **Type:** Email
- **Organization:** Amazon (TRMS - Transaction Risk Management Services)
- **Pages:** 2

## Datta's Involvement
- **Role at time:** SDE-2 (Software Development Engineer II)
- **Involvement type:** Direct Recipient

## Key Quotes
> Friday, July 15, 2016 at 8:34:09 PM India Standard Time

## Full Content
```
Friday, July 15, 2016 at 8:34:09 PM India Standard Time
Subject: Feed Back on XML_NEW parser migra8on for
Date: Thursday, June 23, 2016 at 12:17:42 PM India Standard Time
From: Gopalan, Ramachandran
To: Vellal, DaQatreya, PoliseQy, Hari
CC: Sankaran, Thiruvenkatakrishnan, Mani, Gajendran, grcs-feeds-chennai@amazon.com
Hi DaQa/Hari,
Just sharing my experience on my first XML_NEW parser migra8on for GPIV feed standard and the break-
up of 8melines on the steps it took to complete the migra8on.
1) The wiki contains most of the steps on clear cut to complete the migra8on of a standard from old
XML to NEW parser and that helped elimina8ng the Dev hand hold on migra8on.
2) Thanks DaQa for helping in se_ng the RetailCatalogDocumentStoreService locally and adding the
step to wiki clearly & ge_ng the Odin permissions to complete the migra8on on 8meline
3) The steps for changing the madeira ion configura8ons according to new parser is also easy. May be
it varies based on different madeira configura8on with different copyFields & aspect paths
Some things to add in wiki that might be useful are:
1) The number of items or % of items that we need to submit for comparison to get full confidence
score
2) To check on the beta and prod by sample file submission aeer configura8on check-in to make sure
that configura8ons propagated through both Streaming & Doc-store service pipeline as non-sync of
them might cause madeira submission failures [Quality assurance checks/ Matching
failures/normaliza8on errors]
Timelines of the steps on high level for effort spent [No cycle 8me included] for single itera8on for each of
the step for GPIV [containing only 3 sub-vendors] .The 8me varies for other vendors based on no. of sub
vendors:
S.no MigraKon steps Effort spent
1 Se_ng up madeira/docstore & necessary environments locally 4 hr
2 Iden8fying & Submi_ng sample feed files for each vendor through old parser 0.5 hr
3 Ge_ng old Normaliza8on record through the script 0.5 hr
Changing the madeira configura8on and tes8ng for one feed to verify whether the
4 paths [ copyFields & aspect paths ]are working fine 0.5 hr
5 Submi_ng sample feed files for each vendor through New parser 0.5 hr
6 Ge_ng New Normaliza8on record through the script 0.5 hr
7 Comparison of old and new normaliza8on records 0.5 hr
8 Par8al normaliza8on pre-check in tes8ng for tes8ng through mixed aspects 3 hrs
Total: 10 hrs effort 8me on first 8me migra8on if no issue occurs in the middle.
I am working on the caffeine implementa8on of GPIV. I will let you know the feedback on how new XML
document helps in effec8ve fetching of data/reduc8ons in coding wise.
Thanks,
Page 1 of 2
Ram
Page 2 of 2
```

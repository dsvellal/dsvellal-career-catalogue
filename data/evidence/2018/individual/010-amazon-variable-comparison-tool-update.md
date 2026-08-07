---
title: "Variable Comparison Tool Update"
date: 2018-03-01
year: 2018
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: []
skills: ["AWS RDS", "Performance Optimization", "Tooling"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Variable Comparison Tool Update

## Source
- **File:** `201803_VariableComparisonToolUpdate.pdf`
- **Date:** 2018-03-01
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
> Friday, August 17, 2018 at 12:31:55 PM India Standard Time

## Full Content
```
Friday, August 17, 2018 at 12:31:55 PM India Standard Time
Subject:Re: [FYI] VariableComparisonTool updated
Date: Tuesday, 13 March 2018 at 11:45:10 India Standard Time
From: Vellal, DaHatreya
To: Kapoor, Aditya, ep-dev (ep-dev@amazon.com)
CC: trms-dev-inpay@amazon.com, Nagesh, Harsha
Hi Aditya, ep-dev team,
The tool has been generically modified & backward compaYbility has been taken care of. This will ensure
that the exisYng script opYons & DJS jobs will conYnue to run & all the opYons provided has been made
non-mandatory with appropriate defaults if not specified.
Regards,
DaHa
From: "Kapoor, Aditya" <kapoorak@amazon.com>
Date: Tuesday, 13 March 2018 at 11:13
To: "Vellal, DaHatreya" <daHatrv@amazon.com>, "ep-dev (ep-dev@amazon.com)" <ep-
dev@amazon.com>
Cc: "trms-dev-inpay@amazon.com" <trms-dev-inpay@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>, "Nagesh, Harsha" <nharsha@amazon.com>
Subject: Re: [FYI] VariableComparisonTool updated
Hi DaHa
Thanks for improving the tool. I think the changes you have made are generic to help both teams
We also came to know yesterday that there is Yger team for solving variable mismatches. If that team, is
using the same tool, we can send the mail to them as well.
Thanks
Aditya
From: DaHatreya Vellal <daHatrv@amazon.com>
Date: Tuesday, March 13, 2018 at 11:02 AM
To: "ep-dev (ep-dev@amazon.com)" <ep-dev@amazon.com>
Cc: "trms-dev-inpay@amazon.com" <trms-dev-inpay@amazon.com>
Subject: [FYI] VariableComparisonTool updated
Hello folks,
For SVA’s Pay-to-load latency reducYon project, I have enhanced the variable comparison tool with three
funcYonaliYes:
1. Added GLS filtering – this will help in fetching orders to a specific list of GLS provided via command
line. In our case, we use 610 and 644 as our GLS list, but the tool can take in any no. of GLS &
construct the correct MDS query to pull those orderIds only, belonging to the GLS list.
2. Added variable filtering – This will help in generaYng the comparison report for only the list of
variables that have been specified via this opYon, and will skip the TEC call made to fetch all the
variables specified for a country. The variables required should be specified in the file & each
variable should be line-separated.
3. Added sampleOrderIds per variable mismatch – This will help in idenYfying the orderIds for which
the variable mismatch was found. Currently this supports two use-cases: a) Variables that have
mismatched in both FRS & Fortress, and b) Variables that have defaulted in Fortress, but have not
Page 1 of 2
in FRS. The command line tool accepts max no. of orderIds that will be reported along with
“Variable Mismatch Summary” table.
The document for the same has been updated here (Offline Comparison Tool (Prod Tool) secYon):
hHps://w.amazon.com/bin/view/Variable_Comparison_tool_project_well_done/Tool_Usage/
Regards,
DaHa
DaHatreya S Vellal | TRMS | daHatrv@amazon.com | +91-9972312693
Page 2 of 2
```

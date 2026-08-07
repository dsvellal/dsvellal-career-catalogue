---
title: "Amazon Linux Migration Hari Appreciation"
date: 2016-08-01
year: 2016
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: ["Hari"]
skills: ["AWS RDS", "Amazon Linux", "Documentation", "Risk Management", "Testing"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Amazon Linux Migration Hari Appreciation

## Source
- **File:** `20160818_AmazonLinuxMigration_HariAppreciation.pdf`
- **Date:** 2016-08-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Amazon)
- **Category:** Recognition

## Metadata
- **Type:** Email
- **Organization:** Amazon (TRMS - Transaction Risk Management Services)
- **Pages:** 4

## Datta's Involvement
- **Role at time:** SDE-2 (Software Development Engineer II)
- **Involvement type:** Direct Recipient

## Key Quotes
> Thursday, August 18, 2016 at 5:09:36 PM India Standard Time

## Full Content
```
Thursday, August 18, 2016 at 5:09:36 PM India Standard Time
Subject: Re: Upgrading apollo environments to Amazon Linux
Date: Thursday, August 18, 2016 at 4:41:09 PM India Standard Time
From: PoliseGy, Hari
To: Vellal, DaGatreya, grcs-feeds-org@amazon.com
Nice. Good work DaGa.
From: DaGatreya S Vellal <daGatrv@amazon.com>
Date: Thursday, August 18, 2016 at 4:13 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
Team,
FYI, I have completed the migraZon of hosts from RHEL5 to Amazon Linux. The details are captured here:
hGps://w.amazon.com/index.php/SCP-ASP/MigraZonToAmazonLinux
Here are some stats:
- 57 hosts were replaced
- 22 environments addressed (alpha, beta, gamma and prod included)
- 9 Pipelines addressed
- 4 Zckets were resolved as a part of this migraZon (captured here)
- 2 hurdles taken care of (captured here)
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon
From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Thursday, July 21, 2016 at 6:12 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
FYI – Beta and Prod have been restored to their original capacity, with RHEL64 OS’s.
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon
From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Thursday, July 21, 2016 at 2:04 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Update: Upgrading apollo environments to Amazon Linux
Page 1 of 4
Team,
FYI. #7 in the list (hGps://w.amazon.com/index.php/SCP-
ASP/MigraZonToAmazonLinux#Apollo_environments_listed_for_migraZon) is currently stuck with beta
completely down, and 2 hosts of prod down. I am trying to restore the old RHEL OS’s back by creaZng
ASG’s and reusing the hosts that were replaced. This is to ensure that the current operaZonal capacity is
restored. Once done, I plan to check why upgrade failed, and see how it can be avoided. UnZl this happens,
no other hosts will be replaced.
Golden rules learnt (the hard way):
# Replace one host at a Zme.
# Try beta first and then prod.
# On any failure, do not conZnue further!
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon
From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Tuesday, July 19, 2016 at 12:03 AM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
Team,
FYI – the update is taking a bit longer than expected (esp. when replacing prod hosts, since I cannot replace
all of them, at the risk of losing prod availability). I plan on replacing two Apollo envt hosts a day (this will
eventually ensure that we are done with mostly all environments by this week).
I have completed #1 and #2 from this list: hGps://w.amazon.com/index.php/SCP-
ASP/MigraZonToAmazonLinux#Apollo_environments_listed_for_migraZon and I plan to take up 2
subsequent hosts every day and migrate them to Amazon linux. All progress is tracked via wiki:
hGps://w.amazon.com/index.php/SCP-ASP/MigraZonToAmazonLinux
Let me know if you have concerns.
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon
From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Monday, July 18, 2016 at 6:55 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
Page 2 of 4
Team,
Ticket hGps://G.amazon.com/0085426093 has been resolved. I have migrated
RetailCatalogServices/VendorData (beta, gamma and prod) to Amazon Linux. The migraZon is tracked via
wiki: hGps://w.amazon.com/index.php/SCP-ASP/MigraZonToAmazonLinux
General steps followed:
1. Migrate hosts to Amazon Linux
2. AcZvate the hosts
3. Run test on beta (including integraZon test if any, specified in the pipeline)
If you have any concerns let me know. I will start migraZng other hosts listed in Zck
```

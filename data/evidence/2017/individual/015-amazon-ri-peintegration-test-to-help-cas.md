---
title: "Ri PEIntegration Test To Help CAS"
date: 2017-07-01
year: 2017
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: ["Balachandra", "Raman"]
skills: ["API Design", "AWS RDS", "Risk Management", "Testing"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Ri PEIntegration Test To Help CAS

## Source
- **File:** `201707_RiPEIntegrationTest_ToHelpCAS.pdf`
- **Date:** 2017-07-01
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
> Thursday, November 9, 2017 at 3:15:44 PM India Standard Time

## Full Content
```
Thursday, November 9, 2017 at 3:15:44 PM India Standard Time
Subject:RE: TRMS RiPE Integra1on
Date: Friday, 14 July 2017 at 2:47:12 PM India Standard Time
From: D B, Naveen
To: Vellal, DaEatreya, Sharma, Raman, Singh Rana, Aniruddha
CC: Ramakrishna, Chandan, B. K., Balachandra, Ramineni, Hemachandra
Thanks DaEa..
From: Vellal, DaEatreya
Sent: Friday, July 14, 2017 2:29 PM
To: D B, Naveen <naveendb@amazon.com>; Sharma, Raman <ramanp@amazon.com>; Singh Rana,
Aniruddha <aniruddr@amazon.com>
Cc: Ramakrishna, Chandan <rchanda@amazon.com>; B. K., Balachandra <balakr@amazon.com>;
Ramineni, Hemachandra <ramineni@amazon.com>
Subject: Re: TRMS RiPE Integra1on
Hello,
I also got a ping from Prasanna & Ashish Joshi. I see that their concern is about calling the EvaluateRisk
API. Minus the coral-envelope being supported with Slapshot, we have been advoca1ng them to use the
coral-client way of calling us. I have updated the SIM: hEps://sim.amazon.com/issues/CARNAC-5435 with
the exact code that they need to write to call our client, by upda1ng an integra1on test-case that we
already had.
This should help Chun move forward and be unblocked from tes1ng. I have also responded to the email
from Prasanna and Chun.
Regards,
DaEa
DaEatreya S Vellal | TRMS | daEatrv@amazon.com | +91-9972312693
From: "D B, Naveen" <naveendb@amazon.com>
Date: Friday, 14 July 2017 at 10:31 AM
To: "Vellal, DaEatreya" <daEatrv@amazon.com>, Raman Sharma <ramanp@amazon.com>, "Singh
Rana, Aniruddha" <aniruddr@amazon.com>
Cc: "Ramakrishna, Chandan" <rchanda@amazon.com>, "Balachandra B. K."
<balakr@amazon.com>, "Ramineni, Hemachandra" <ramineni@amazon.com>
Subject: RE: TRMS RiPE Integra1on
Just for internal update:
Prasanna pinged me and DaEa to get more details on how they can test.
DaEa will help on it and update SIM with the steps required for tes1ng.
Also, updated Prasanna that the result from the API is s1ll hardcoded.
Aniruddha,
Request you to sync up with DaEa to get the details and take it further.
(taking DaEa’s help this one 1me as he has the context)
Regards,
Page 1 of 4
Naveen
From: Wang, Chun-Che
Sent: Thursday, July 13, 2017 3:57 AM
To: Ramineni, Hemachandra <ramineni@amazon.com>; Vellal, DaEatreya <daEatrv@amazon.com>;
Sharma, Raman <ramanp@amazon.com>; G, Prasanna <pgopina@amazon.com>; Lhila, Pradyumna
<prady@amazon.com>
Cc: Ramakrishna, Chandan <rchanda@amazon.com>; Sharma, Rahul <rssha@amazon.com>; Joshi, Ashish
<ashjoshi@amazon.com>; Banga, Gaurav <bangag@amazon.com>; Shao, Ivan <chenzhis@amazon.com>;
D B, Naveen <naveendb@amazon.com>; B. K., Balachandra <balakr@amazon.com>; Singh Rana,
Aniruddha <aniruddr@amazon.com>
Subject: Re: TRMS RiPE Integra1on
Replied in SIM:
hEps://sim.amazon.com/issues/CARNAC-5435
From: Ramineni, Hemachandra
Sent: Tuesday, July 11, 2017 9:35 AM
To: Vellal, DaEatreya <daEatrv@amazon.com>; Sharma, Raman <ramanp@amazon.com>; G, Prasanna
<pgopina@amazon.com>; Lhila, Pradyumna <prady@amazon.com>
Cc: Ramakrishna, Chandan <rchanda@amazon.com>; Sharma, Rahul <rssha@amazon.com>; Joshi, Ashish
<ashjoshi@amazon.com>; Banga, Gaurav <bangag@amazon.com>; Shao, Ivan <chenzhis@amazon.com>;
Wang, Chun-Che <chunchew@amazon.com>; D B, Naveen <naveendb@amazon.com>; B. K., Balachandra
<balakr@amazon.com>; Singh Rana, Aniruddha <aniruddr@amazon.com>
Subject: RE: TRMS RiPE Integra1on
+ Aniruddha
From: Vellal, Dattatreya
Sent: Tuesday, July 11, 2017 9:34 AM
To: Sharma, Raman; G, Prasanna; Ramineni, Hemachandra; Lhila, Pradyumna
Cc: Ramakrishna, Chandan; Sharma, Rahul; Joshi, Ashish; Banga, Gaurav; Shao, Ivan; Wang, Chun-Che; D B,
Naveen; B. K., Balachandra
Subject: Re: TRMS RiPE Integration
Hi Prasanna,
We have created a simple unit-test class to create coral envelope object via java, you can find the link
here: [1]. This combined with the code link that Raman has posted: [2], will help you achieve the correct
request object, which can then be used to call EvaluateRisk API of FortressSILService.
[1] - hEps://1ny.amazon.com/5daxs2az
[2] - hEps://1ny.amazon
```

# 201707 RiPEIntegrationTest ToHelpCAS

> Converted from document `201707_RiPEIntegrationTest_ToHelpCAS.pdf`

Thursday, November 9, 2017 at 3:15:44 PM India Standard Time

Subject: RE: TRMS RiPE Integra1on
Date: Friday, 14 July 2017 at 2:47:12 PM India Standard Time
From: D B, Naveen
To:
Vellal, DaEatreya, Sharma, Raman, Singh Rana, Aniruddha
CC:
Ramakrishna, Chandan, B. K., Balachandra, Ramineni, Hemachandra
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
We have created a simple unit-test class to create coral envelope object via java, you can ﬁnd the link
here: [1]. This combined with the code link that Raman has posted: [2], will help you achieve the correct
request object, which can then be used to call EvaluateRisk API of FortressSILService.
[1] - hEps://1ny.amazon.com/5daxs2az
[2] - hEps://1ny.amazon.com/14g50cqok
Regards,
DaEa
DaEatreya S Vellal | TRMS | daEatrv@amazon.com | +91-9972312693

Page 2 of 4

From: Raman Sharma <ramanp@amazon.com>
Date: Tuesday, 11 July 2017 at 9:20 AM
To: "G, Prasanna" <pgopina@amazon.com>, "Ramineni, Hemachandra" <ramineni@amazon.com>,
"Lhila, Pradyumna" <prady@amazon.com>, "Vellal, DaEatreya" <daEatrv@amazon.com>
Cc: "Ramakrishna, Chandan" <rchanda@amazon.com>, "Sharma, Rahul" <rssha@amazon.com>,
"Joshi, Ashish" <ashjoshi@amazon.com>, "Banga, Gaurav" <bangag@amazon.com>, "Shao, Ivan"
<chenzhis@amazon.com>, "Wang, Chun-Che" <chunchew@amazon.com>, "D B, Naveen"
<naveendb@amazon.com>, "Balachandra B. K." <balakr@amazon.com>
Subject: Re: TRMS RiPE Integra1on
Hi Prasanna,
It’s much easier to test integra1on by wri1ng a simple java client code. Calling using coral diver can be
very tricky because it contains envelop which is a binary blob and I don’t know easy way generate
contents of an envelop for coral diver.
You can look at this code as reference for integra1on hEps://1ny.amazon.com/14g50cqok . We haven’t
enabled AAA in FortressSIL so you can even call from desktop.
Thanks,
Raman

From: "G, Prasanna" <pgopina@amazon.com>
Date: Tuesday, July 11, 2017 at 9:06 AM
To: Hemachandra Ramineni <ramineni@amazon.com>, "Lhila, Pradyumna" <prady@amazon.com>,
Raman Sharma <ramanp@amazon.com>, DaEatreya Vellal <daEatrv@amazon.com>
Cc: Chandan Ramakrishna <rchanda@amazon.com>, "Sharma, Rahul" <rssha@amazon.com>,
"Joshi, Ashish" <ashjoshi@amazon.com>, "Banga, Gaurav" <bangag@amazon.com>, "Shao, Ivan"
<chenzhis@amazon.com>, "Wang, Chun-Che" <chunchew@amazon.com>
Subject: RE: TRMS RiPE Integra1on
Hi TRMS Team,
Gentle Reminder.. Need your support on this.
Thanks,
Prasanna
From: G, Prasanna
Sent: Monday, July 10, 2017 12:41 PM
To: Ramineni, Hemachandra <ramineni@amazon.com>; Lhila, Pradyumna <prady@amazon.com>;
Sharma, Raman <ramanp@amazon.com>; Vellal, DaEatreya <daEatrv@amazon.com>
Cc: Ramakrishna, Chandan <rchanda@amazon.com>; Sharma, Rahul <rssha@amazon.com>; Joshi, Ashish

Page 3 of 4

<ashjoshi@amazon.com>; Banga, Gaurav <bangag@amazon.com>; Shao, Ivan <chenzhis@amazon.com>;
Wang, Chun-Che <chunchew@amazon.com>
Subject: TRMS RiPE Integra1on
Hi Raman/Hemachandra,
Need support on TRMS RiPE integra1on (SIM - hEps://issues.amazon.com/CARNAC-5435).
ChunChe from Carnac working on TRMS RiPE API integra1on. It would be helpful, if you can guide him, how to
invoke the EvaluateRisk API via coral diver.
As per him, the feature of Coral Envelop seems to be missing from Slapshot and it is in their roadmap.
Regards,
Prasanna Gopinath

Sr. Technical Program Manager – CS Tech | Hyd – India Development Center | Phone Tool

Page 4 of 4


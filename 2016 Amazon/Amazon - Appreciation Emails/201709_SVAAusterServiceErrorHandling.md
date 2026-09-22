# 201709 SVAAusterServiceErrorHandling

> Converted from document `201709_SVAAusterServiceErrorHandling.pdf`

Tuesday, November 28, 2017 at 6:57:26 PM India Standard Time

Subject: Re: [Query] AusterService: UpdateAccountStatus
Date: Wednesday, 20 September 2017 at 1:31:07 PM India Standard Time
From: Sharma, Hitesh
To:
Vellal, DaJatreya
Hi,
Thanks! We’re working on ﬁxing the issue.
-Hitesh

From: "Vellal, DaJatreya" <daJatrv@amazon.com>
Date: Monday, 18 September 2017 at 3:17 PM
To: "Sharma, Hitesh" <hts@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Hi Hitesh,
I have responded back to your query via SIM.
If you need more info or context, feel free to set up a call with me. I’ll be happy to answer queries.
Regards,
DaJa

From: "Sharma, Hitesh" <hts@amazon.com>
Date: Monday, 18 September 2017 at 2:50 PM
To: "Vellal, DaJatreya" <daJatrv@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Hi DaJa,
Following up on this here - hJps://issues.amazon.com/issues/SVA-INTAKE-48. Can you please comment
on the issue linked?
Thanks,
Hitesh

From: "Shukla, Ankur" <ankshuk@amazon.com>
Date: Friday, 15 September 2017 at 1:38 PM
To: "Sharma, Hitesh" <hts@amazon.com>
Subject: FW: [Query] AusterService: UpdateAccountStatus

-Regards
Ankur Shukla

From: "Jain, Manish" <manijain@amazon.com>
Date: Friday, September 15, 2017 at 9:46 AM
Page 1 of 5

To: "Vellal, DaJatreya" <daJatrv@amazon.com>, "Chebolu, Guru Murthy Venkata Satya"
<chebolug@amazon.com>, "Walia, Amit" <amiwalia@amazon.com>, "Sankaran, Rajesh"
<rjs@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>, "Shukla, Ankur"
<ankshuk@amazon.com>, "Cholej, Vinay" <vinaych@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Thanks DaJa for bringing this to our aJenkon. RJs: Can you have Auster Service owner ﬁx this or have
secondary on-call take this over.

From: "Vellal, DaJatreya" <daJatrv@amazon.com>
Date: Thursday, 14 September 2017 at 1:04 PM
To: "Jain, Manish" <manijain@amazon.com>, "Chebolu, Guru Murthy Venkata Satya"
<chebolug@amazon.com>, "Walia, Amit" <amiwalia@amazon.com>, "Sankaran, Rajesh"
<rjs@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>, "Shukla, Ankur"
<ankshuk@amazon.com>, "Cholej, Vinay" <vinaych@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Hi,
Wanted to escalate that this issue has surfaced up again via kcket: [1]. Our Herd workﬂows are failing [2]
[3] [4], indicakng that AusterService’s updateAccountStatus method fails to update the account status.
What is happening here is that, AusterService is trying to update status of an already suspended account,
to suspended. This was already discussed more than a month ago, and an improvement was requested
via SIM: [5]
Kindly look into this.
[1] - hJps://J.amazon.com/0124335629
[2] - hJps://herdui-eu.amazon.com/ui/work.jsp?
clientId=AbuseTeam&objectId=AckonHandlerWorkﬂow%3A5171245512%3ASVAOneAccountPerCustome
rInveskgakon&instruckonId=AckonHandlerWorkﬂow&workId=bfaa2690-f4bc-4fd0-8abe-ba78b1fadbfe
[3] - hJps://herdui-eu.amazon.com/ui/work.jsp?
clientId=AbuseTeam&objectId=AckonHandlerWorkﬂow%3A6819132112%3ASVAOneAccountPerCustome
rInveskgakon&instruckonId=AckonHandlerWorkﬂow&workId=52001852-7963-4282-adb4-a9d2c963ﬀ0c
[4] - hJps://herdui-eu.amazon.com/ui/work.jsp?
clientId=AbuseTeam&objectId=AckonHandlerWorkﬂow%3A14126372325%3ASVAOneAccountPerCustom
erInveskgakon&instruckonId=AckonHandlerWorkﬂow&workId=2f468d5c-93be-4321-aed26d065c3f789c
[5] - hJps://issues.amazon.com/issues/SVA-INTAKE-48
Regards,
DaJa

From: "Jain, Manish" <manijain@amazon.com>
Date: Monday, 31 July 2017 at 12:18 PM
To: "Vellal, DaJatreya" <daJatrv@amazon.com>, "Chebolu, Guru Murthy Venkata Satya"
<chebolug@amazon.com>, "Walia, Amit" <amiwalia@amazon.com>, "Sankaran, Rajesh"
<rjs@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>, "Shukla, Ankur"
<ankshuk@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Page 2 of 5

RJS,
Please take this up as improvement for Auster.
:: MJ

From: "Vellal, DaJatreya" <daJatrv@amazon.com>
Date: Monday, 31 July 2017 at 11:23 AM
To: "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>, "Walia, Amit"
<amiwalia@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>, "Jain, Manish"
<manijain@amazon.com>, "Shukla, Ankur" <ankshuk@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Thank you very much Guru.
This is an error handling request. Can you please consider prioriksing this ASAP? I have opened a SIM
here: hJps://issues.amazon.com/issues/SVA-INTAKE-48
Regards,
DaJa
DaJatreya S Vellal | TRMS | daJatrv@amazon.com | +91-9972312693

From: "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>
Date: Monday, 31 July 2017 at 11:17 AM
To: "Vellal, DaJatreya" <daJatrv@amazon.com>, "Walia, Amit" <amiwalia@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>, "Jain, Manish"
<manijain@amazon.com>, "Shukla, Ankur" <ankshuk@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Hi DaJa,
You can create here
hJps://issues.amazon.com/issues/create?assignedFolder=171f83d8-2910-4035-81b9-f6a253ab54e4
Thanks,
Guru Murthy Chebolu,
Sr. TPM, India Payments.
M: (+91) 9880 267 457

From: "Vellal, DaJatreya" <daJatrv@amazon.com>
Date: Monday, July 31, 2017 at 10:46 AM
To: "Walia, Amit" <amiwalia@amazon.com>, Guru Chebolu <chebolug@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>, "Jain, Manish"
<manijain@amazon.com>, "Shukla, Ankur" <ankshuk@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
Hello Guru, Amit,
Page 3 of 5

Can you give me the link where I can ﬁle a SIM for the minor improvement suggested?
Regards,
DaJa
DaJatreya S Vellal | TRMS | daJatrv@amazon.com | +91-9972312693

From: "Jain, Manish" <manijain@amazon.com>
Date: Friday, 28 July 2017 at 6:57 PM
To: "Vellal, DaJatreya" <daJatrv@amazon.com>, "Shukla, Ankur" <ankshuk@amazon.com>,
"Walia, Amit" <amiwalia@amazon.com>, "Chebolu, Guru Murthy Venkata Satya"
<chebolug@amazon.com>
Cc: "trms-dev-core-inpay@amazon.com" <trms-dev-core-inpay@amazon.com>
Subject: Re: [Query] AusterService: UpdateAccountStatus
+ign Amit and Guru.
Hi! DaJa,
Please work with guru and Amit walia to ﬁle in intake request.
:: MJ

From: "Vellal, DaJatreya" <daJatrv@amazon.com>
Date: Friday, 28 July 2017 at 4:44 PM
To: "Shukla, Ankur" <ankshuk@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-devcore-inpay@amazon.com>
Subject: [Query] AusterService: UpdateAccountStatus
Hi Ankur,
I remember you sending us the allowed sva account state transikons here:
hJps://w.amazon.com/index.php?ktle=IndiaAmazonMoney/SVA/AcountStates#Account_States
With SVA going live, when HERD makes an AusterService call to updateAccountStatus for an account
whose current state is “suspended” and the new state it has to change to, is also “suspended”, an error is
thrown. However, the error isn’t too descripkve/helpful.
Here’s a case which we are inveskgakng right now, where we are ending up with quite a few such
scenarios:
1. SVA Account - SVA1, is a related customer, for two of the Accounts, SVA2 & SVA3.
2. According to our workﬂow of OneAccountPerCustomer, both SVA2 & SVA3 get queued for
inveskgakon & an inveskgator will inspect & suspend SVA1, as duplicate.
3. In doing step 2, we are ending up with a scenario where: inveskgator for SVA2, suspends SVA1 (this
ﬂow works ﬁne). Then a diﬀerent inveskgator picks up SVA3, and tries to suspend an already
suspended SVA1. This is causing errors at our HERD workﬂow, because an AusterService
updateAccountStatus query is made, to change the account status from “Suspended” (from SVA2)
to “Suspended” (from SVA3) & this is failing without friendly error messages from AusterService [1]
So, I wanted to place a request for you and your team to consider if we can either of the two solukons
that I can think of:
1. Throw a friendly message, in the error, saying you can not change the status of an account to <x> if
Page 4 of 5

it’s status is already <x>, or

2. (Our preferred method) Log such requests, but do not throw an error, when a request is made to
AusterService’s UpdateAccountStatus API, to change the account status to the same status.
Opkon 2, will help us a in avoiding a lot of open HERD work-items & I think is also logical. Can you
consider this small ﬁx/code-update? If a SIM has to be raised, let me know where to do so, and I’ll be
happy to do that.
[1] - hJps://kny.amazon.com/15abjfqvi
Regards,
DaJa
DaJatreya S Vellal | TRMS | daJatrv@amazon.com | +91-9972312693

Page 5 of 5


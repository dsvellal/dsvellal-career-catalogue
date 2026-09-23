# 201705 RiPE FortressSIL DummyAPI

> Converted from document `201705_RiPE_FortressSIL_DummyAPI.pdf`

Tuesday, October 24, 2017 at 6:12:53 PM India Standard Time

Subject: RE: RiPE API - remaining tasks and revised ETA
Date: Friday, 5 May 2017 at 1:05:40 PM India Standard Time
From: D B, Naveen
To:
Ramakrishna, Chandan, Sharma, Raman, Vellal, DaHatreya
CC:
Kapoor, Aditya, trms-ripe-dev@amazon.com
Hi Chandan,
The API integraQon tesQng is complete and is available on devo now. The API deﬁniQon is as per the Wiki.
It be called by creaQng a coral client and hiVng the FortressSILService beta environment. Wiki has the
details.
Could you get us a SDE contact from CSTech team, with whom our SDEs can work with directly for any
queries/input/output to the API?
Thanks to DaHa for compleQng the Dummy API quickly and unblock CStech, despite hurdles in integraQon
tesQng.
Regards,
Naveen
From: Ramakrishna, Chandan
Sent: Friday, May 5, 2017 10:30 AM
To: Ramakrishna, Chandan <rchanda@amazon.com>; D B, Naveen <naveendb@amazon.com>; Sharma,
Raman <ramanp@amazon.com>; Vellal, DaHatreya <daHatrv@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-ripe-dev@amazon.com
Subject: RE: RiPE API - remaining tasks and revised ETA
Please lemme know if the dummy API to return “0.1” band is on devo and the pending integraQon test is
complete. Will drop a note to CS Tech. Thanks.
From: Ramakrishna, Chandan [mailto:rchanda@amazon.com]
Sent: Tuesday, May 2, 2017 6:33 PM
To: D B, Naveen <naveendb@amazon.com>; Sharma, Raman <ramanp@amazon.com>; Vellal, DaHatreya
<daHatrv@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-ripe-dev@amazon.com
Subject: RE: RiPE API - remaining tasks and revised ETA
Thanks. Please do, will update CS Tech and set 5/25 to be the producQon date. Thanks, Chandan.
From: D B, Naveen
Sent: Tuesday, May 2, 2017 8:15 AM
To: Ramakrishna, Chandan <rchanda@amazon.com>; Sharma, Raman <ramanp@amazon.com>; Vellal,
DaHatreya <daHatrv@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-ripe-dev@amazon.com
Subject: RE: RiPE API - remaining tasks and revised ETA
Hi Chandan,
We have completed implementaQon of the dummy API in Fortress SIL.
Doing the integraQon test to ensure it is working correctly. Currently stuck in AAA authorizaQon excepQon
while calling the API.
Hopefully will be resolved by tomorrow. Will share code details, once it is veriﬁed.
Page 1 of 4

Regards,
Naveen
From: D B, Naveen [mailto:naveendb@amazon.com]
Sent: Friday, April 28, 2017 5:48 PM
To: Ramakrishna, Chandan <rchanda@amazon.com>; Sharma, Raman <ramanp@amazon.com>; Vellal,
DaHatreya <daHatrv@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-ripe-dev@amazon.com
Subject: RE: RiPE API - remaining tasks and revised ETA
Hi Chandan,
We will provide a dummy API to unblock CSTech by early next week.
The API return will be as deﬁned in the Wiki, Output secQon. As you requested, we will hardcode risk to
0.1
The schedule and task break up for the complete implementaQon is below: (ajer more discussions with
Raman and DaHa today)
By 5/16, we can share the changes in devo.
By 5/25, we can share the changes in prod.
2-May
3-May
4-May
5-May
8-May
9-May
10-May
FORTRESS code refactoring to resuse exisQng GMRA funcQonality

Raman

DaHa

Dummy API

Fortress SIL
forwarding
request to Fortress

11-May
Wiring of OTF

TEC changes for
intent
conﬁguraQons
includes devo

FORTRESS changes to understand
and open risk document

*Dependency : Datasheet setup and variable deﬁniQon on Concession MDS data
Regards,
Naveen
From: D B, Naveen [mailto:naveendb@amazon.com]
Sent: Tuesday, April 25, 2017 5:46 PM
To: Sharma, Raman <ramanp@amazon.com>; Vellal, DaHatreya <daHatrv@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-ripe-dev@amazon.com
Subject: RE: RiPE API - remaining tasks and revised ETA
Thanks Raman, DaHa and Aniruddha.
With below tasks remaining, the ETA comes to 5/12.

Raman
DaHa

26-May
1
2

27-May
1
2

28-May
1
2

29-May

30-May

31-May

1-Jun
1
3

2-Jun
4
3

3-Jun
4
5

Regards,
Naveen

Page 2 of 4

From: Sharma, Raman
Sent: Tuesday, April 25, 2017 5:06 PM
To: Vellal, DaHatreya <daHatrv@amazon.com>; D B, Naveen <naveendb@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-ripe-dev@amazon.com
Subject: Re: Draj: Risk Proﬁle EvaluaQon (RiPE) API | Week 16 status
Remaining task & esQmates:
1.
2.
3.
4.
5.
6.
7.
8.
9.

FORTRESS SIL interface changes and implementaQon. [4 days] Owner: Raman
Wiring of OTF calculator in FORTRESS [3 days] Owner: DaHa
FORTRESS changes to understand and open risk document. [2 days] Owner: DaHa, scope : CS tech
document reading only.
FORTRESS changes to dump rule execuQon result into addiQonal context and populate response.
[2 days] Owner:
Code review. [3 day for both] Owner: [Raman/ DaHa]
Setup task
a. TEC changes for intent conﬁguraQons includes devo/gamma/prod. [3 days]
b. Ruleset creaQon [1 day]
Datasheet setup and variable deﬁniQon on Concession MDS data. [Remaining: 2 days]
FORTRESS code refactoring to resuse exisQng GMRA funcQonality. [3 days]
IntegraQon tests [2 days] Scope : FortressSIL -> FORTRESS

External dependencies : Data plarorm for approvals and data sheet deployments. Analysts?
Who will write rules for CS tech? TBD
From: DaHatreya Vellal <daHatrv@amazon.com>
Date: Tuesday, April 25, 2017 at 3:55 PM
To: "D B, Naveen" <naveendb@amazon.com>
Cc: Raman Sharma <ramanp@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>
Subject: Re: Draj: Risk Proﬁle EvaluaQon (RiPE) API | Week 16 status
Hi Naveen,
Raman, Kamakhya, Vivek and I had a discussion about the remaining work that needs to be done. The
following generic high-level tasks were idenQﬁed:
1. TEC ConﬁguraQon to ensure that the right GMRA, through event, reaches Fortress – 2 to 3 days
work esQmaQon eﬀort
2. Making FORTRESS changes to that it understands both RiskDocument (RiskContext, Envelope)
and FraudDocument and works with it. This will need FORTRESS code refactoring so that we
either fork code from exisQng classes to accommodate how FORTRESS understands it or see if we
have to write separate classes to ensure that FORTRESS works with RiskDocument it receives via
RiPE API.
3. FORTRESS currently returns ENUM. For CS-Tech and other clients that are going to on-board on to
FORTRESS through RiPE, we’d need a way to return diﬀerent output types. We’ll need to think

Page 3 of 4

through what needs to be done, so that the output return type from FORTRESS can be
conﬁgurable (this was the output of our discussion with Kamakhya)
4. How do we do Rule-execuQon outcome to AcQon mapping
These tasks are speciﬁc to CS-Tech:
1. Get more clarity on the outcome states expected by CS-Tech
a. Right now, we know that they expect bands. What are the ranges of the bands, do they
expect anything else in the output, how would they interpret it / what else is needed.
2. Map risk-context to event hook for CS-Tech, to ensure that we read the RiskContext and invoke
the right event-hook, that’ll lead to the right GMRA being ﬁred, via intent.
With the above scope of work in front of us, I’d like to bring out two points:
1. 4/30 is diﬃcult because we do not understand the complete scope of the work.
2. Given that TEC conﬁguraQon is just a way for us to specify what intent to ﬁre, and uncertainity
lies in ﬁguring out how to ensure FORTRESS can be refactored to understand both FD and RD,
Raman has suggested that I take up the second task (Point 2: Making FORTRESS changes to
understand RD and FD). This is again an exploratory task. I’ll have to understand FORTRESS’s
current working and come up with interjecQon points where I’ll have to fork to see how to
accommodate both RD and FD.
We can discuss more about this in the 4pm meeQng.
Regards,
DaHa
DaHatreya S Vellal | TRMS | daHatrv@amazon.com | +91-9972312693

From: "Vellal, DaHatreya" <daHatrv@amazon.com>
Date: Tuesday, 25 April 2017 at 10:52 AM
To: "D B, Naveen" <naveendb@amazon.com>, Raman Sharma <ramanp@amazon.com>, "Singh Rana,
Aniruddha" <aniruddr@amazon.com>
Subject: Re: Draj: Risk Proﬁle EvaluaQon (RiPE) API | Week 16 status
Hi Naveen,
Raman and I discussed the work that needs to be completed and the Qmelines. I think 4/30 date is cuVng
too short. I had a quick chat with Vivek to see what eﬀorts would be needed to make TEC related
changes. His esQmate is around 3-4 days. I am doing the TEC changes for the ﬁrst Qme, I might spill over
by a day or two.
I wanted to bring this up now, and see how to miQgate this rather than bringing it up at a later point of
Qme.
Regards,
DaHa
DaHatreya S Vellal | TRMS | daHatrv@amazon.com | +91-9972312693

Page 4 of 4


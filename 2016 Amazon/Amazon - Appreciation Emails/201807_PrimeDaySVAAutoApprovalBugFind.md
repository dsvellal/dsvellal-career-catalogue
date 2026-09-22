# 201807 PrimeDaySVAAutoApprovalBugFind

> Converted from document `201807_PrimeDaySVAAutoApprovalBugFind.pdf`

Friday, August 17, 2018 at 12:37:44 PM India Standard Time

Subject: RE: Well Done Da,a in ﬁguring out the root cause of High Auto Approval Rate for HFC and SVA
load orders
Date: Tuesday, 17 July 2018 at 19:19:44 India Standard Time
From: Nagesh, Harsha
To:
Kapoor, Aditya, Vellal, Da,atreya, Kizhakkekalathil, Raj
CC:
trms-dev-inpay@amazon.com, Jones, Chris
Indeed Nice work Da,a on ﬁnding the root cause of the bug in the rule.
From: Kapoor, Aditya
Sent: Monday, July 16, 2018 10:15 PM
To: Vellal, Da,atreya <da,atrv@amazon.com>; Nagesh, Harsha <nharsha@amazon.com>;
Kizhakkekalathil, Raj <rajk@amazon.com>
Cc: Kapoor, Aditya <kapoorak@amazon.com>; trms-dev-inpay@amazon.com
Subject: Well Done Da,a in ﬁguring out the root cause of High Auto Approval Rate for HFC and SVA load
orders
Importance: High
Hi Da,a
You have shown great example of Deep Dive. Finding out exactly which rule was incorrect and also
poin`ng to exact coding error.
Thanks
Aditya

From: Da,atreya Vellal <da,atrv@amazon.com>
Date: Monday, July 16, 2018 at 3:26 PM
To: "Kumar, Akhil" <akhkum@amazon.com>, "Majidi, Keivan" <kmajidi@amazon.com>
Cc: "Shariﬀ, Mohammed Jeelan" <shariﬀm@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>, "Verma, Animesh" <vanimesh@amazon.com>, "Suresh, Nandini"
<nandinis@amazon.com>, "Kumar, Satyajeet" <satyajek@amazon.com>
Subject: Re: Weekly Connect on IN Payments Projects
Hey Guys!
We got a `cket: h,ps://,.amazon.com/0156970049 - which indicated that there were a lot of ruleset
execu`on failure, and it lead to a lot of orders gegng auto-passed. Aher deep-dive (refer `cket
correspondence) – I no`ced that the rule wri,en for SVA_HFCPass was wrong.
This is the current condi`on: h,ps://rmp-eu.amazon.com/rule_ins/show_rule_instance?class=btn+btnlink&region=GBAmazon&ruleInsId=403915355621706778&rulesetInsId=4558862135306111226&ruletyp
e=in_physical_fortress_stage2&schema=BuyerFraud
In this, you’ll no`ce that there’s an assignment instead of a comparison for $customerProﬁlePercen`le.
This changed was pushed at 04.26 UTC, and we started seeing errors of rule execu`on at the same `me:
h,ps://`ny.amazon.com/g7rj4wwv/snapshot and because of primeday order volumes this has led to a lot
of SVA orders gegng auto-passed, without fraud-check.
Can you ensure that the rule is corrected – on priority?
Page 1 of 2

Aher talking to Aditya and Animesh, we have cut a SEV-2 to the CTI of the on-call because this has
business impact. Here’s the `cket: h,ps://,.amazon.com/0157004613
Regards,

Page 2 of 2


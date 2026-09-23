# TakingThingsToConclusion MaxAPTCQuestions August8th2015

> Converted from document `TakingThingsToConclusion_MaxAPTCQuestions_August8th2015.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Michelle Prior
Thursday, August 20, 2015 7:45 PM
Dattatreya Subramanya Vellal
Chandrashekhar Surendranath
Re: another question

thank you very much

From: Dattatreya Subramanya Vellal
Sent: Thursday, August 20, 2015 3:03 AM
To: Michelle Prior
Cc: Chandrashekhar Surendranath
Subject: RE: another question
Hi Michelle,
Apologies for the late response. I have tried to answer your questions below. Kindly let me know if you have other
queries which we can help get answers to.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Michelle Prior
Sent: Tuesday, August 18, 2015 9:09 PM
Cc: Chandrashekhar Surendranath <schandrashekhar@exeter.com>; Dattatreya Subramanya Vellal
<dvellal@exeter.com>
Subject: another question

I was wrong with my "final question" before
this is another one
‘Max. APTC’ will be recalculated every time Plan Selection is started and will display APTC preferences screen if the
Max value calculated is found to be different from the previous value.
>>Datta: The scenario we are talking about is when the user selects to apply an APTC amount which is lesser than
the max-eligible APTC amount. For the reason that we are taking into account “used-aptc”, if the user does not
select the max-eligible-aptc, then every month, there will be a residue of APTC amount which will get added to his
available APTC, thereby increasing his max eligible APTC. Let’s take a scenario. The user is eligible for 100$ a month
BLI APTC amount. So, according to the formula, the eligible APTC = {100 * (0 + 12) – (0)} / 12 = 100$. The user, during
his first plan selection, selects 50$ (instead of 100$) and does a plan selection, and comes back after 6 months. Let’s
see what his max eligible APTC is – eligible APTC = {100 * (6 + 6) – (50*6)}/6 = 150$. So, in this case, when the user
revisits plan selection, because his max-eligible-APTC has changed, we will show him the APTC preferences screen
before showing him the plan-selection screen. Please note, APTC preferences screen can be reached through My
Accounts – any time. We are just showing the APTC preference screen when the max-eligible-aptc amount has
changed, so that the user can make an informed choice of utilizing or not utilizing his maximum eligible APTC
amount.

Does this mean that Max APTC value will not be displayed if the calculated value is not different?
1

>>Datta: Max APTC value is always available for the user to see, via the APTC preference screen reachable through
My Accounts. The fix talks about user making an informed choice of utilizing his maximum eligible APTC amount
whenever he revisits, and sees that his max eligible APTC amount has changed.

In that event, what value would the user see as APTC on the Plan Selection/APTC preferences screen?
>>Datta: The user will always see the maximum eligible APTC amount in the APTC preference screen.
From: Michelle Prior
Sent: Tuesday, August 18, 2015 10:18 AM
Cc: Chandrashekhar Surendranath; Dattatreya Subramanya Vellal
Subject: Re: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of circumstance

Datta and Shekar
one final question
From your last bullet - "BLI amount written at contact level will depict the OPA calculated BLI, and not the taxhousehold-level BLI. It is understood and accepted that there may be difference in these two amounts, and the one
at the tax-household-level is the correct value."
So i understand that Siebel may maintain a different amount at the contact level, is the tax HH level (the correct
value) what is used to populate the 834 transmission to the carrier? I think we can explain the different values that
the user/caseworker may see but is the HH level APTC (revised if necessary) what is sent to the carriers/issuers?
>>Datta: What is sent to the carrier via 834 is the plan-slice level applied APTC amount. This is completely plan-slice
dependent, and considers both max-eligible-APTC and selected APTC amount. This is also dependent on the no. of
enrollees uniquely enrolled into a plan. However, keeping the “how-APTC-gets-allocated” aside, the plan-slice level
applied aptc amount is the right amount, which is getting transmitted to the carriers as the used APTC, attached to
the plan’s subscriber.
Please let me know and thank you
Michelle
P.S. I know you're gone for the day and I don't expect a response right away.

From: Michelle Prior
Sent: Tuesday, August 18, 2015 9:43 AM
To: Lakshmi Thanga-Raja
Cc: Chandrashekhar Surendranath; Dattatreya Subramanya Vellal
Subject: Re: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of circumstance

Thank you all, this is helpful and I can use it to create some summary bullets. I will be in touch if i have
additional questions.
Appreciate your quick response
Michelle

From: Lakshmi Thanga-Raja
Sent: Tuesday, August 18, 2015 9:09 AM
To: Michelle Prior
Subject: FW: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of circumstance
Please include Datta if you have any follow-up questions.
2

Lakshmi

From: Krishnamurthy Hegde
Sent: Tuesday, August 18, 2015 9:08 AM
To: Chandrashekhar Surendranath <schandrashekhar@exeter.com>
Cc: Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Dattatreya Subramanya Vellal <dvellal@exeter.com>
Subject: RE: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of circumstance
Hi Lakshmi,
Please find below the summary of functional changes done in OneGate as part of the RT ticket implementation:
- Eligible APTC = (APTC BLI *(Months plans have been active up to now for the Tax Anchor + any future
months) - (total APTC used so far))/future months remaining
- Using the above formula, user can be deemed to be eligible for more APTC than that is determined by BLI
during certain period in the coverage
- A negative left-over-eligible-aptc-per-month-per-tax-household will be capped at zero
- ‘Max. APTC’ will be recalculated every time Plan Selection is started and will display APTC preferences screen
if the Max value calculated is found to be different from the previous value.
- Consumed APTC will get applied to all the tax-household structures when the tax-anchor remains the same.
This is applicable for the benefit year.
- If we have tax-household entries, with the same tax-anchor, we sum up consumed APTC while calculating
APTC for the remaining months.
- BLI amount written at contact level will depict the OPA calculated BLI, and not the tax-household-level BLI. It
is understood and accepted that there may be difference in these two amounts, and the one at the taxhousehold-level is the correct value.
Michelle can reach out to Datta (copied, who drafted the above response), if she has any quick questions.
Thanks,
Krishna
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Res: +91-80-23368241 | Off: +91-8033450029 | Skype: khegde
From: Chandrashekhar Surendranath
Sent: Tuesday, August 18, 2015 10:19 AM
To: Krishnamurthy Hegde
Subject: Fwd: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of circumstance

Sent from my iPhone
Begin forwarded message:
From: Lakshmi Thanga-Raja <Lakshmi@exeter.com>
Date: August 18, 2015 at 7:10:13 AM GMT+5:30
To: Chandrashekhar Surendranath <schandrashekhar@exeter.com>
Subject: Fwd: RT 6274 Rules are now in place to validate Recalculation of APTC after a
Change of circumstance
Can you see if this is something you can assist with?
Lakshmi
3

-------- Original message -------From: Michelle Prior <mprior@EXETER1.onmicrosoft.com>
Date: 08/17/2015 8:42 PM (GMT-05:00)
To: Lakshmi Thanga-Raja <Lakshmi@exeter.com>, Srinivas Jillella <SJillella@exeter.com>,
Tara Noble <tnoble@exeter.com>
Cc: Brett Ackerman <backerman@exeter.com>, Joey Zhou <jzhou@exeter.com>, Eric Moy
<emoy@exeter.com>
Subject: Re: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change
of circumstance
Following up on Chris' note below, can you help me understand which aspects of the
rules/functionality included in the JIRA referenced below have been included in HF3 and
what rules/functionality have not yet been included?
There is a meeting with the state of VT tomorrow afternoon - short notice I know - but I
appreciate your help.
thanks in advance
Michelle
From: Christopher Simo
Sent: Monday, August 17, 2015 8:35 PM
To: Michelle Prior; Brett Ackerman
Subject: RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of
circumstance
The project team has been asked to provide an overview of HF3 function via a walk-through of the
release notes tomorrow (Tues) at 3p.
RT 6274 Rules are now in place to validate Recalculation of APTC after a Change of
circumstance. I’ve reviewed the JIRA at some length but I am not clear on what actually has been
delivered. Can you provide a 2-3 bullets to summarize what has been delivered on the following
request:

24

Recalculate APTC to account for
previously-received APTC

Properly calculate APTC

4

Post R1

2-N


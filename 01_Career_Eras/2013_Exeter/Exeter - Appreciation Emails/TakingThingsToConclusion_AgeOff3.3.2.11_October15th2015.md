# TakingThingsToConclusion AgeOff3.3.2.11 October15th2015

> Converted from document `TakingThingsToConclusion_AgeOff3.3.2.11_October15th2015.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Eric Moy
Thursday, October 15, 2015 8:20 PM
Dattatreya Subramanya Vellal; Brett Ackerman
Satheesh Kumar Raju; Krishnamurthy Hegde; Chandrashekhar Surendranath; Lakshmi
Thanga-Raja; Jonah Egenolf
RE: [Requesting response] Age off functionality behavior in 3.3.2.11

Sounds good. I’ve added my comments to the ticket.
Thanks,
Eric

Eric Moy
Consultant | Exeter Group, Inc.
emoy@exeter.com | (240) 694-5093

From: Dattatreya Subramanya Vellal
Sent: Thursday, October 15, 2015 10:29 AM
To: Eric Moy <emoy@exeter.com>; Brett Ackerman <backerman@exeter.com>
Cc: Satheesh Kumar Raju <sraju@exeter.com>; Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar
Surendranath <schandrashekhar@exeter.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf
<jegenolf@exeter.com>
Subject: RE: [Requesting response] Age off functionality behavior in 3.3.2.11
Hi Eric,
Thank you very much. Can you please update this in the JIRA comments? If we need a granular level of control, we
can probably do it in the upcoming releases, unless we hear otherwise from Brett. Until then, the current behavior
stays.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Eric Moy
Sent: Thursday, October 15, 2015 7:45 PM
To: Dattatreya Subramanya Vellal <dvellal@exeter.com>; Brett Ackerman <backerman@exeter.com>
Cc: Satheesh Kumar Raju <sraju@exeter.com>; Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar
Surendranath <schandrashekhar@exeter.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf
<jegenolf@exeter.com>
Subject: RE: [Requesting response] Age off functionality behavior in 3.3.2.11
Hi Datta, Brett,
For age-off, I’m assuming were only dealing with three scenarios:
1. 26 y.o. QHP age-off
2. 26 y.o. Dental age-off
3. Pediatric Dental age-off
If SoV wants to control each age-off functionality individually, we can provide that level of granularity by creating
three separate flags – one to control each of the age-off scenarios. But if we’re only going to have one flag (“OG
Keep Kid On Plan – Current”), then OG should respect the flag and keep the kid on the plan for all these scenarios.
1

Eric Moy
Consultant | Exeter Group, Inc.
emoy@exeter.com | (240) 694-5093

From: Dattatreya Subramanya Vellal
Sent: Thursday, October 15, 2015 3:48 AM
To: Eric Moy <emoy@exeter.com>
Cc: Satheesh Kumar Raju <sraju@exeter.com>; Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar
Surendranath <schandrashekhar@exeter.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf
<jegenolf@exeter.com>; Brett Ackerman <backerman@exeter.com>
Subject: RE: [Requesting response] Age off functionality behavior in 3.3.2.11
Importance: High
Hi Eric, Brett,
While our QA was validating the age-off feature, we found an interesting scenario. This is jotted down in JIRA
ONEGATECORE-28402. The scenario is that of a pediatric dental age-off with “OG Keep Kid On Plan – Current” flag
set to Y. The general assumption is, whenever the “OG Keep Kid On Plan – Current” is set to Y, irrespective of the
type of age-offs (pediatric dental, dental or QHP) we do not remove the kid from an existing plan.
Can you please take a look at the JIRA and validate if the ask from our QA is what is needed? Or if the behavior that I
described above, where “OG Keep Kid On Plan – Current” set to Y, will not touch any of the age-off types on the
current policy, correct.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Friday, September 25, 2015 5:00 PM
To: Eric Moy <emoy@exeter.com>
Cc: Satheesh Kumar Raju <sraju@exeter.com>; Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar
Surendranath <schandrashekhar@exeter.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf
<jegenolf@exeter.com>; Brett Ackerman <backerman@exeter.com>
Subject: Re: [Requesting response] Age off functionality behavior in 3.3.2.10 HF3 EBF2

Hi Eric,
Please see the flags that we are using here, to control the behavior of age-off. These have been referred in the below
comments:
System Preference
Default
Name
Value
OG Keep Kid On Plan - N
Current

OG Keep Kid On Plan – N
Renewal
OG Ageoff Period - 30
Current

Meaning of each flag
If set to Y, even when the kid ages-off mid-year on current policy, the
kid will remain on parent’s plan and will get the right tier (family). If
set to N, then the kid will be removed from the parents plan, the next
time system sees this anomaly.
Same as above, but the control is on “Renewal” policy and not current
policy.
When-ever the age-off batch job is run, it will check for a date range
of “date-of-age-off-batch-job-run” + 30 days (mentioned in the value)
to see if we have any cases where individuals age off between these
2

OG Ageoff Period – 100
Renewal
OG Auto Process SR – Y
Current

OG Auto Process SR - Y
Renewal
OG Auto Enroll Kid – Y
Current
OG Auto Enroll Kid – Y
Renewal

dates. If there are then further action will be taken based on “OG Keep
Kid On Plan”, “OG Auto Process SR” and “OG Auto Enroll Kid” flags on
current policy.
Same as above, but the date range is 100 days (value can be set to
anything > 0)
When we find an age-off case, we create an SR on the current policy.
Do we auto-process it or not is controlled by this flag. Set it to “Y” and
we auto-process this SR and any other plan related discrepancies for
the current policy. Set it to “N” and we do not auto process the SR.
Same as above, but the control is on “Renewal” SR auto processing
When the kid ages off in current policy and we are processing the SR
(auto/manual) – do we auto enroll the kid into a new plan (of the
same type) or not, is controlled by this flag.
Same as above, but the control is on renewal plan enrollment for
aged-off kid.

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Eric Moy
Sent: Thursday, September 24, 2015 7:51 PM
To: Dattatreya Subramanya Vellal <dvellal@exeter.com>
Cc: Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf <jegenolf@exeter.com>; Brett Ackerman
<backerman@exeter.com>
Subject: RE: [Requesting response] Age off functionality behavior in 3.3.2.10 HF3 EBF2
Thanks Datta!
I’ve looked a little more closely into http://172.17.0.100:8080/jira/browse/ONEGATECORE-24999, which describes
the age-off functionality, and I’m wondering if (and how) the new age-off batch would handle a mid year CoC with
plan selection.
Scenario: The family does a CoC, is granted an SEP, and then goes to make changes in PS. The dependent cannot
stay on the family’s plan and must enroll in his own.
- Will the batch job check be run automatically after the family makes change to their plans?
- Datta: When a COC is submitted by the family we check for any Age off discrepancy among others. If any age
off discrepancy is found then creation of PSDR will be based on the flag (OG Auto Process SR-Current). Also,
processing the SR is based on the flags we will either remove the aged out kid from the parent plan or
remove and enroll him into the same plan. This means before the family comes to plan selection we would
have done all the check that the script also offers, for the Age off.
-

If the family submits plan selection with no changes, will the batch job know not to create a PDSR?
Datta: Again, depends on two things, a) do we want the kid to remain on the parents plan for the current
policy, and b) do we want to auto-process an SR – whenever a mid-year plan selection is done. If both of
them are Y, then the kid won’t be removed from the parents plan, and I believe an SR won’t get created.
However, if we want to remove the kid from the parents plan, then we’d need to set the appropriate flag to
N. The flags that we have created, have been listed above.

Note: if the family does a CoC, gets an SEP, but does not go to plan selection then the child stays on. Only if the
family goes to plan selection and makes edits, does the dependent need to be kicked off.
3

Eric Moy
Consultant | Exeter Group, Inc.
emoy@exeter.com | (240) 694-5093

From: Dattatreya Subramanya Vellal
Sent: Thursday, September 24, 2015 5:52 AM
To: Eric Moy <emoy@exeter.com>; Brett Ackerman <backerman@exeter.com>
Cc: Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf <jegenolf@exeter.com>
Subject: RE: [Requesting response] Age off functionality behavior in 3.3.2.10 HF3 EBF2
Hi Eric,
We have one job for age-off which can be run at any point of time. Having said that, we will include age-off check
during auto-renewals and manual renewals as well. This means, whenever we run auto-renewals or do a manual
renewals, we will call age-off checks.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Eric Moy
Sent: Thursday, September 24, 2015 6:08 AM
To: Dattatreya Subramanya Vellal <dvellal@exeter.com>; Brett Ackerman <backerman@exeter.com>
Cc: Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf <jegenolf@exeter.com>
Subject: RE: [Requesting response] Age off functionality behavior in 3.3.2.10 HF3 EBF2
Hi Datta,
Looks good to me!
Just to clarify, will the age-off batch job be separate from the renewal batch job? Or will this functionality be rolled
into the renewal batch job?
Thanks,
Eric
Eric Moy
Consultant | Exeter Group, Inc.
emoy@exeter.com | (240) 694-5093

From: Dattatreya Subramanya Vellal
Sent: Wednesday, September 23, 2015 3:20 AM
To: Brett Ackerman <backerman@exeter.com>; Eric Moy <emoy@exeter.com>
Cc: Krishnamurthy Hegde <khegde@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Jonah Egenolf <jegenolf@exeter.com>
Subject: [Requesting response] Age off functionality behavior in 3.3.2.10 HF3 EBF2
Importance: High
Hello Brett, Eric,
4

I am writing this email to let you know the age-off functionality that will be implemented in 3.3.2.10 HF3 EBF2.
Please let us know if you see anything different from your understanding of Vermont’s asks.
Functionality:
- When the age-off batch job is run, the ability to identify any of the aged-off cases, where an enrollee has aged-off
of a qhp, dental or a pediatric dental plan
- The ability to create a plan discrepancy SR on the aged-off cases and the ability to auto process it
- The ability to enroll the aged-off enrollee into a new plan
- The ability to consider a period of time within which an enrollee ages off, instead of calculating age-off cases as of
the batch-job-run-date
When the batch process is run, we will consider both current and renewals policy, and the above abilities can be
controlled via system-preferences, meaning they can be individually turned on/off for each of current or renewals
policies. The age-off check will be made for QHP plan age-off, dental plan age-off and pediatric dental plan age-off,
each of whose age-off age can be controlled through system preferences. There is one assumption that we are
making, and ie. If an enrollee ages-off from a pediatric dental plan, then that plan also has other tier’s (Individual,
family etc.), so that we can enroll him back on to the same plan.
Also, a point to note is, if we enable auto-processing a PDSR, we will also process any other pending PDSR’s present
on the case.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

5


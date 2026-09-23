# DoTheRightThing CustomerCentricSolutionManualEditBatchJob August14th2015

> Converted from document `DoTheRightThing_CustomerCentricSolutionManualEditBatchJob_August14th2015.pdf`

Dattatreya Subramanya Vellal

Subject:

Chevy Vithiananthan
Friday, August 14, 2015 8:23 PM
Dattatreya Subramanya Vellal
Jonah Egenolf; Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Krishnamurthy
Hegde
Re: EBF2 manual scenarios

Follow Up Flag:
Flag Status:

Follow Up
Completed

From:
Sent:
To:
Cc:

Batch job is fine - we can take more than a week if needed
Sent from my iPhone
On Aug 14, 2015, at 10:19 AM, Dattatreya Subramanya Vellal <dvellal@exeter.com> wrote:
Team,
Jonah and I talked about the approach mentioned below, and we think that if we are going down the
path of providing a “button” or a “batch-job that runs on a list of MCNs”, it is best if the changes are
controlled in two parts:
1. Manual update of BP’s and BLI’s to the right dates (not worrying about SEPs and all) and
save them
2. Manual update of the start and end dates of a plan, at the member coverage level and save
them
3. Once the two-part update is done, call this batch process (or click a button) that’ll do the
following:
a. Reconstruct the Tax HH structure and subsidies based on the BP and BLI start and
end
b. Recalibrate the plan slices based on the start and end dates seen on the slices
c. Redistribute subsidies based on plan-slices and Tax HH (which may end up creating a
few more slices since we are auto-correcting, but we will react to what we see at the
Tax HH)
If we are looking at doing the above proposed change, we will consider reusing our code base with
minor tweaks to do 3a, 3b and 3c. Jonah and I did discuss an LOE of about a week (Dev + Test) and
this is what I feel: 1 week may be a short duration of time for us to address this, given that we don’t
have the exact scenarios that we want to execute, and see if we are working correctly, but, if this
brings any relief to our project teams, we should definitely give it a shot.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Friday, August 14, 2015 3:52 PM
To: Jonah Egenolf <jegenolf@exeter.com>; Chevy Vithiananthan
<chevyv@EXETER1.onmicrosoft.com>
Cc: Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath
<schandrashekhar@exeter.com>; Krishnamurthy Hegde <khegde@exeter.com>
Subject: RE: EBF2 manual scenarios
Hi Chevy, Jonah,
1

Wanted to project what we understand and what we did today against this email response.

1.
2.
3.
4.

Topic 1 – No action item for the product team unless we hear back.
Topic 2 – With Jonah’s response, no action item on the product team unless we hear back.
Topic 3 – No action item for the product team unless we hear back.
“SoV request – can a script/trigger be written to update backend after manual change?” –
This goes back to the same request of continuing the way the CW’s were trained, and not
adopting the “Exceptional Circumstance” path that we suggested. However, assuming that
we may end up providing a button at the “member-coverage” applet to react to the manual
changes made, we have listed down impact areas which needs to be addressed through this
button click so that we are in sync wrt our CRM structures. The scenarios we are considering
are:
a. CW manually changes start date of a plan-slice in the member-coverage
b. CW manually changes end date of a plan-slice in the member-coverage
c. CW deletes an enrollee from a plan-slice
d. Combinations of a, b and/or c
Given these scenarios, we’d want to keep some or all of the following structures in sync,
depending on the changes made, to make sure that we react correctly to the manual edits made by
the CW at the member-coverage applet.
a. Benefit Plan, Benefit Line Item and the Hidden Benefit Line Item Date\
b. Case level (both Medicaid and QHP) “Benefit Effective Date”
c. Relevant / All Tax Household Structure start and end dates
d. Relevant / All Tax Household Subsidies, and their start and end dates
e. Subsidy distribution on the plan slices
f. Plan events and Member events
g. An indication that the “following case” was manually edited by the “following caseworker” and the “following things” changed. This can be through a DB structure to
which we write into so that we know if we ever have to revisit manually changed
cases in future, we have a way to find out what cases were changed, and what
actions were done on it.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Jonah Egenolf
Sent: Friday, August 14, 2015 2:41 AM
To: Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>; Christopher Simo
<CSimo@exeter.com>; Dattatreya Subramanya Vellal <dvellal@exeter.com>; Ajinth Christudas
<achristudas@exeter.com>; Megan Gupta <mmgupta@exeter.com>
Cc: Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath
<schandrashekhar@exeter.com>; Krishnamurthy Hegde <khegde@exeter.com>
Subject: Re: EBF2 manual scenarios

#2 was ok when they have only 1 plan on the household. If they have multiple plans and
only want to terminate 1 of them, it is a problem. I guess put another way: If they are
disenrolling all plans on the household, then we are good. So are there cases where they
want to disenroll some but not all of the plans on a household? If it's always all or nothing,
then we might be ok there.

And I'll try to answer the questions:
2

1) Please provide detail on “redistribution anomalies” - when do they happen? What tables
are impacted?
>> Basically, we don't redistribute if they just change things in Siebel. So if plan 1 used $50 in
APTC and plan 2 used $50, if we terminate plan 1 in Siebel, we would not move the APTC
across to the other plan. The anomaly is we don't redistribute.
2) Will these have an impact on subsequent transactions e.g. a subsequent CoC
>> Should not have an impact. We may or may not end up correcting any incorrectly
distributed slices when we do a CoC, but we should not get any worse.
3) Is there any way to manually fix them or does this require code – aka the ‘button’ Jonah
described this morning
>> I think you could simulate this fix by manually creating a plan discrepancy SR. Anything
that forces plan remediation should work in this case. This is basically what we'd build
with the button. A way to force creation of the missing tax household date ranges and
plan remediation.

SoV request – can a script/trigger be written to update backend after manual change?
>> Fixing them really means calling remediate via this magic button we'd have to build. There
might be some ways around the button though. For cases where we want to backdate the start
date, I think the only way you may be able to manually fix it is by first backdating the benefit plan
to the backdate point and somehow enrolling in a plan in the UI on or before the start date of the
backdated plan (to force the creation of the tax households on that date). I'm not sure how we'd
go about enrolling in a plan on that date via the UI, but it's probably doable by messing around
somehow. For pushing the start date forward or messing with the end date, then the plan
discrepancy SR creation might work. In all cases, we need to test, but it's worth a shot.

- Jonah

From: Chevy Vithiananthan
Sent: Thursday, August 13, 2015 3:41 PM
To: Christopher Simo; Dattatreya Subramanya Vellal; Ajinth Christudas; Megan Gupta
Cc: Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Jonah Egenolf; Krishnamurthy Hegde
Subject: Re: EBF2 manual scenarios

I believe #2 was considered ok as well
#3 - I believe you are updating the case with the specific scenario for what you need scripts
for right? If that is not correct let me know.

From: Christopher Simo
Sent: Thursday, August 13, 2015 3:28 PM
To: Dattatreya Subramanya Vellal; Ajinth Christudas; Megan Gupta
Cc: Chevy Vithiananthan; Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Jonah Egenolf;
Krishnamurthy Hegde
Subject: RE: EBF2 manual scenarios
All,
Here’s my take on where we are:
3

Topic 1 - “Medicaid cases that are member coverages history and we need to move it out of lapse
cancelled and into member coverages” Should be OK– recommend Optum/SoV should validate these scenarios
Topic 2 - Disenrollments that need to be backdated
>>be aware of the subsidy redistribution anomalies that may arise because of manually end-dating a
plan
Need PT team input
1) Please provide detail on “redistribution anomalies” - when do they happen? What tables
are impacted?
2) Will these have an impact on subsequent transactions e.g. a subsequent CoC
3) Is there any way to manually fix them or does this require code – aka the ‘button’ Jonah
described this morning
Topic 3 - Date flips….scenario is all that needs to change is the start date of the plan
Expect exceptional circumstance function will work in majority of scenarios.
We have requested further information from SoV on specific manual start date change scenarios
they believe they still need it.
SoV request – can a script/trigger be written to update backend after manual change?
Let me know if you want this in JIRA and which ticket (or new)
Thanks,
Chris

From: Dattatreya Subramanya Vellal
Sent: Thursday, August 13, 2015 9:06 AM
To: Ajinth Christudas; Christopher Simo; Megan Gupta
Cc: Chevy Vithiananthan; Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Jonah Egenolf;
Krishnamurthy Hegde
Subject: RE: EBF2 manual scenarios

Team - FYI..
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Thursday, August 13, 2015 4:53 PM
To: Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>; Lakshmi Thanga-Raja
<Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>; Jonah
Egenolf <jegenolf@exeter.com>
Subject: RE: EBF2 manual scenarios
Please find our responses below in green.
Regards,
Datta
4

Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chevy Vithiananthan
Sent: Thursday, August 13, 2015 4:07 AM
To: Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath
<schandrashekhar@exeter.com>; Jonah Egenolf <jegenolf@exeter.com>; Dattatreya Subramanya
Vellal <dvellal@exeter.com>
Subject: Fwd: EBF2 manual scenarios
Can we set up a call with chris to
Talk about these scenarios and what we
May be able
To do?
This is the same
Thing we talked about today and ajinth created a ticket based on some testing he had done
Lakshmi - can we set up call at 9 am eastern time?
Sent from my iPhone
Begin forwarded message:
From: Christopher Simo <CSimo@exeter.com>
Date: August 12, 2015 at 12:52:30 PM EDT
To: Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>, Jonah Egenolf
<jegenolf@exeter.com>
Cc: Ajinth Christudas <achristudas@exeter.com>, Megan Gupta
<mmgupta@exeter.com>
Subject: EBF2 manual scenarios
Chevy, Jonah,
The following are provided scenarios from SoV where they use manual intervention:
Chevy, Jonah,
The following are provided scenarios from SoV where they use manual intervention:

•

“Medicaid cases that are member coverages history and we need to move it
out of lapse cancelled and into member coverages”
o VT Team comment – This is a locally developed processs since
they have NOT been renewing Mediciad
o ESI – What do we understand: There are Medicaid (or
perhaps QHP) plan slices which are “Lapsed” or
“Terminated”, which are present in the “Member Coverage
History” tab of the BC. However these have to be brought
into the “Member Coverage” tab.
o ESI – What is our recommendation: Please note, although we
have the “Member Coverage History” tab in 3.3.2.10 HF2
EBF2 for both QHP and Medicaid policies, through an RTJIRA: 26777, and its subsequent offshoot 26952, we are
moving all plan slices which have start-date = end-date, or
“Lapsed”, or “Terminated” to the “Member Coverage
History” tab, and this is done by adding a view-filter to the
BC in 3.3.2.10 HF3 via the development ticket: 27215. We
have no recommendation here. If the “Filters” have to
change, to show “Lapsed” and “Terminated” plan slices on
5

the “Member Coverage” tab, we can acknowledge the
request. Or this can be a Siebel customization onsite.
o Conclusion: No action on product required.
•

“Disenrollments that need to be backdated. Disenrollment is automatically
based on the date of disenrollment so if we’re doing this retro from a
backlog request, we would need to manually change the disenrolled slice.”
o VT Team comment – retro termination
o ESI – What do we understand: This was brought to our notice via a comment
from Megan, through the JIRA: 27369. In this comment, the request was to
know how we can, in OneGate, change the end-date of a plan through
Exceptional Circumstances.
o ESI – What is our recommendation: The suggestion from the product team
has been provided in a following comment here. Our suggestion indicated
that Exceptional circumstance is NOT required for end-dating a plan.
Without considering the backlog for a moment, there are logical rules that
dictate end-date of a plan – Eg: APTC changes should end-date a plan based
on the 15/16 logic, Voluntary disenrollment should follow 15/16 logic etc.
Coming back to manually changing the plan, we have suggested that this
works, however, the subsidy redistribution may not take place if a direct
CRM update happens. In addition, if there are multiple plan slices for a given
plan, and we are looking at end-dating a middle slice, then we’d have to also
change the remaining slices to adjust to the changed dates, and there may
be subsidy redistribution anomalies that may not get addressed.
o Conclusion: Exceptional Circumstance does not allow controlling end-dating
of a plan. Manual end-dating of a plan may lead to subsidy redistribution
anomalies. If there exists a process like “retro termination”, followed by the
SOV, the please be aware of the subsidy redistribution anomalies that may
arise because of manually end-dating a plan.
• “Date flips….scenario is all that needs to change is the start date of the plan
– either forward or back.”
o VT Team comment – this is used for basically all different types of CoC
scenarios – income change, marriage, add HHM, etc. typically to do a change
in the past while working through their backlog
We’ve been attempting to use Exceptional Circumstance for retro per the PT’s
reccomendation and running into some defects
• http://172.17.0.100:8080/jira/browse/ONEGATECORE-27448 - ESI
Comments: A similar issue was reported internally via 25625 and we are
fixing this. The fix will be available to the project team at SOV via an EBF –
3.3.2.10 HF2 EBF3.
• http://172.17.0.100:8080/jira/browse/ONEGATECORE-27444 - ESI
Comments: There is an understanding gap, which has been pointed out by
Christine in a comment for the JIRA. This has to be talked through
completely, and the behavior has to be agreed upon, before we can
consider if this scenario needs a fix and how.
• ESI Team Comments: There were three questions from the attached
document called out for the product team:

1.

Atleast for this scenario, at a high level if we
change the start date fields directly in the Member
Coverages applet we need to sync up the dates in
the TAX HH Applet and Subsidy details applet. Is
that correct? – For the given scenario, we do not
recommend directly updating the Member
Coverage applet fields. The product team
6

recommendation is to do this by granting an
exceptional circumstance.
2.

If the answer to the above question is yes, if
SOV still wants to pursue with manually
updating plan slices, can they update the
corresponding plan slice in member
coverages applet and then come back and
update the dates in the TAX HH and Subsidy
details applet (I understand that currently
these fields are not editable, but we can
definitely get to them to be editable if need
be) – Again, the Tax HH and subsidy applets
are central to subsidy distribution and the
entries are linked. We do not recommend
manually updating any of the slices or
subsidies without understanding the
impacts.

3.

If the answer to above question is yes and feasible,
are there any other fields that are hidden in the
backend that we need to care about? I am guessing
no, but can the product team confirm –The product
team does not recommend this path. Futhermore,
the product team does not guarantee any dataerror reporting or data-error fix that’s a resultant of
this method or any missteps that were taken by the
case workers in executing this process.

Conclusion: As described earlier, the better
approach is to take the exceptional
circumstances route, which will ensure the
member coverage and the Tax HH dates in sync.
I think it would be useful to discuss these in depth in a call
Attached is a scenario Ajinth worked through on a date flip and monitoring the tax
HH tables.
For context Gov. Shumlin said today on Vermont Public Radio that VHC had
processed 4500 out of 9000 backlog cases (and touted the improvement of
automated CoC assocated with the 33210 upgrade). These transactions are key to
getting through the remaining 4500.
Thanks,
Chris

7

From: Ajinth Christudas
Sent: Wednesday, August 12, 2015 10:55 AM
To: Christopher Simo
Cc: Megan Gupta
Subject: Updating plan slices manually

Hello Chris,
Here is the first cut analysis of one use case I have tested so far. Please review this
document. It has the results of the test with screenshots and some final questions
for the product team based on our recommendation to update plan slices
We can meet later to discuss if needed. I will run another test scenario and send the
updated document
Thanks,
Ajinth

8


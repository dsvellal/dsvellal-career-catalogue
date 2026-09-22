# KeepingStakeHoldersInformed HF2EBF2EffectiveCommunication August13th2015

> Converted from document `KeepingStakeHoldersInformed_HF2EBF2EffectiveCommunication_August13th2015.pdf`

Dattatreya Subramanya Vellal
Dattatreya Subramanya Vellal
Thursday, August 13, 2015 4:53 PM
Chevy Vithiananthan; Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Jonah
Egenolf
RE: EBF2 manual scenarios

From:
Sent:
To:
Subject:

Please find our responses below in green.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chevy Vithiananthan
Sent: Thursday, August 13, 2015 4:07 AM
To: Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Jonah Egenolf <jegenolf@exeter.com>; Dattatreya Subramanya Vellal <dvellal@exeter.com>
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
Cc: Ajinth Christudas <achristudas@exeter.com>, Megan Gupta <mmgupta@exeter.com>
Subject: EBF2 manual scenarios
Chevy, Jonah,
The following are provided scenarios from SoV where they use manual intervention:
Chevy, Jonah,
The following are provided scenarios from SoV where they use manual intervention:

•

“Medicaid cases that are member coverages history and we need to move it out of lapse
cancelled and into member coverages”
o VT Team comment – This is a locally developed processs since they have
NOT been renewing Mediciad
o ESI – What do we understand: There are Medicaid (or perhaps QHP) plan
slices which are “Lapsed” or “Terminated”, which are present in the
“Member Coverage History” tab of the BC. However these have to be
brought into the “Member Coverage” tab.
1

o ESI – What is our recommendation: Please note, although we have the
“Member Coverage History” tab in 3.3.2.10 HF2 EBF2 for both QHP and
Medicaid policies, through an RT-JIRA: 26777, and its subsequent offshoot
26952, we are moving all plan slices which have start-date = end-date, or
“Lapsed”, or “Terminated” to the “Member Coverage History” tab, and this
is done by adding a view-filter to the BC in 3.3.2.10 HF3 via the development
ticket: 27215. We have no recommendation here. If the “Filters” have to
change, to show “Lapsed” and “Terminated” plan slices on the “Member
Coverage” tab, we can acknowledge the request. Or this can be a Siebel
customization onsite.
o Conclusion: No action on product required.
•

•

“Disenrollments that need to be backdated. Disenrollment is automatically based on the
date of disenrollment so if we’re doing this retro from a backlog request, we would need to
manually change the disenrolled slice.”
o VT Team comment – retro termination
o

ESI – What do we understand: This was brought to our notice via a
comment from Megan, through the JIRA: 27369. In this comment, the
request was to know how we can, in OneGate, change the end-date of a
plan through Exceptional Circumstances.

o

ESI – What is our recommendation: The suggestion from the product team
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

o

Conclusion: Exceptional Circumstance does not allow controlling end-dating
of a plan. Manual end-dating of a plan may lead to subsidy redistribution
anomalies. If there exists a process like “retro termination”, followed by the
SOV, the please be aware of the subsidy redistribution anomalies that may
arise because of manually end-dating a plan.

“Date flips….scenario is all that needs to change is the start date of the plan – either forward
or back.”
o VT Team comment – this is used for basically all different types of CoC scenarios –
income change, marriage, add HHM, etc. typically to do a change in the past while
working through their backlog
We’ve been attempting to use Exceptional Circumstance for retro per the
PT’s reccomendation and running into some defects
•

http://172.17.0.100:8080/jira/browse/ONEGATECO
RE-27448 - ESI Comments: A similar issue was
reported internally via 25625 and we are fixing this.
The fix will be available to the project team at SOV
via an EBF – 3.3.2.10 HF2 EBF3.

•

http://172.17.0.100:8080/jira/browse/ONEGATECORE-27444 - ESI
Comments: There is an understanding gap, which has been pointed
out by Christine in a comment for the JIRA. This has to be talked
through completely, and the behavior has to be agreed upon, before
we can consider if this scenario needs a fix and how.
2

•

ESI Team Comments: There were three questions from the attached document
called out for the product team:
1. Atleast for this scenario, at a high level if we change the start date fields
directly in the Member Coverages applet we need to sync up the dates in
the TAX HH Applet and Subsidy details applet. Is that correct? – For the
given scenario, we do not recommend directly updating the Member
Coverage applet fields. The product team recommendation is to do this
by granting an exceptional circumstance.
2. If the answer to the above question is yes, if SOV still wants to
pursue with manually updating plan slices, can they update the
corresponding plan slice in member coverages applet and then
come back and update the dates in the TAX HH and Subsidy
details applet (I understand that currently these fields are not
editable, but we can definitely get to them to be editable if need
be) – Again, the Tax HH and subsidy applets are central to
subsidy distribution and the entries are linked. We do not
recommend manually updating any of the slices or subsidies
without understanding the impacts.
3. If the answer to above question is yes and feasible, are there any other
fields that are hidden in the backend that we need to care about? I am
guessing no, but can the product team confirm –The product team does
not recommend this path. Futhermore, the product team does not
guarantee any data-error reporting or data-error fix that’s a resultant of
this method or any missteps that were taken by the case workers in
executing this process.
Conclusion: As described earlier, the better approach is to take the
exceptional circumstances route, which will ensure the member
coverage and the Tax HH dates in sync.

I think it would be useful to discuss these in depth in a call
Attached is a scenario Ajinth worked through on a date flip and monitoring the tax HH tables.
For context Gov. Shumlin said today on Vermont Public Radio that VHC had processed 4500 out of
9000 backlog cases (and touted the improvement of automated CoC assocated with the 33210
upgrade). These transactions are key to getting through the remaining 4500.
Thanks,
Chris

From: Ajinth Christudas
Sent: Wednesday, August 12, 2015 10:55 AM
To: Christopher Simo
Cc: Megan Gupta
Subject: Updating plan slices manually

Hello Chris,

3

Here is the first cut analysis of one use case I have tested so far. Please review this document. It has
the results of the test with screenshots and some final questions for the product team based on our
recommendation to update plan slices
We can meet later to discuss if needed. I will run another test scenario and send the updated
document
Thanks,
Ajinth

4


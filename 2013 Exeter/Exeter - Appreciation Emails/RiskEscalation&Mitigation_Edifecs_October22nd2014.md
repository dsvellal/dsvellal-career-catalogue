# RiskEscalation&Mitigation Edifecs October22nd2014

> Converted from document `RiskEscalation&Mitigation_Edifecs_October22nd2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Brett Ackerman
Wednesday, October 22, 2014 7:45 PM
Dattatreya Subramanya Vellal; Anuroop V. Gaonkar; Krishnamurthy Hegde;
Chandrashekhar Surendranath; Jonah Egenolf
RE: 22nd Oct 2014 - MoM - Edifecs

Great, work thanks Datta!
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Dattatreya Subramanya Vellal
Sent: Wednesday, October 22, 2014 10:13 AM
To: Brett Ackerman; Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath; Jonah Egenolf
Subject: RE: 22nd Oct 2014 - MoM - Edifecs

Good news is – we identified the root cause, eliminated it, triggered 834 and 834c’s through SOAP UI, and it works.
This means we have achieved the channel of Siebel-SOA-API working together. However we haven’t tested this endend via batch-process triggers for new applications and all the other different scenarios. We are going to take a stab
at them on Friday. I will keep you guys posted.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Wednesday, October 22, 2014 6:54 PM
To: Brett Ackerman; Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath; Jonah Egenolf
Subject: RE: 22nd Oct 2014 - MoM - Edifecs

Hi,
A very quick update to set the tone.
We are facing integration issues with respect to Siebel-SOA-API path. Our local JUnits work, but invoking this from
the server crossing three layers is not happening. We are trying to debug this, but please expect delays. It may get
stretched till Friday or Monday based on the complexity of the issue. FYI, Thursday is a holiday here in India.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Brett Ackerman
Sent: Wednesday, October 22, 2014 3:18 AM
To: Dattatreya Subramanya Vellal
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath; Jonah Egenolf
Subject: RE: 21st Oct 2014 - MoM - Edifecs

Datta,
My understanding is the current scope is that we update the plan event status, but not the plan status.
Per my conversation with Jonah, I think this is “OK” for now, I think we need to revisit the Plan Status/Sub Status
model in general for 834/820 etc. So let’s hold off on the plan status change for now.
1

This should allow us to focus on making sure what we have is solid for a demo to Jonathan and others.

Thanks,
Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Dattatreya Subramanya Vellal
Sent: Tuesday, October 21, 2014 12:43 PM
To: Brett Ackerman
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath; Jonah Egenolf
Subject: RE: 21st Oct 2014 - MoM - Edifecs

Update.
We have another way of achieving this for the MA Demo though (short term solution). Given that its only logical to
reflect plan-event status at the enrolled plan level, but touching the current plan-sub-status requires changes
downstream, we can consider an option of creating a new status-field at the enrolled-plan level, and that reflecting
the plan-event-status. This serves two purposes without breaking the current flow:
a. A proof that we can touch plan-level fields whenever we update plan-events
b. We provide a way to reflect plan-event-status at the plan-level
Jonah agrees with the short term solution for the demo if we want to prove that we can touch enrolled-plan-level
fields whenever plan-event-status changes via 834. . However, this also means, we have to write update-scripts to
default this new status at the enrolled plans and other Siebel related work (expose this field on the UI, update the
EAI manager to expose this field so that we can update it from the code etc.). This is considerable work – we will aim
for completion tomorrow, but expect risks. Unless I hear back otherwise, we are going ahead with this solution.
NOTE1: A long term solution is to introduce these granular statuses into plan’s status/substatus duo and have planevent-status-change update plan’s status/substatus appropriately/
NOTE2: For 999, we have to change plan-sub-status based on whatever we receive from Edifecs, but this is work-inprogress.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Tuesday, October 21, 2014 8:29 PM
To: Jonah Egenolf; Brett Ackerman
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath
Subject: RE: 21st Oct 2014 - MoM - Edifecs

Brett, Jonah,
This is our current status – we will be testing 834 XML generation and 834c XML consumption tomorrow wrt
different scenarios, and make sure that we don’t break. We will also have deployment tickets ready, just in case they
have to considered for release inclusion. I will drop a note to you by my end of day tomorrow, which indicates how
this piece can be demo-ed, and we will pursue 999 interpretation for mid-next-week.
However, judging from the conversation, I wanted to bring the following points on board:

2

1. The technical challenge to update the plan-status along with the plan-event status is virtually zero. We can
achieve this easily. It’s only a logical challenge and that being – 834c is an acknowledgement from the
integrator, and not the issuer. The acknowledgement from the issuer is 999. However, if we consider to
change the plan-sub-status along with plan-event-status, we have to maintain a mapping between what
plan-event status corresponds to what plan-sub-status. NOTE: We don’t update plan-status, that’s taken
care by a batch job from Siebel that’s run every night.
2. Agreed that it is logical that if we are changing a plan-event status, we should also have an indication of that
on the plan’s sub-status. Considering that, we are proposing the corresponding statuses for plan-event and
plan status/sub-status duo based on Onegate-events:
Plan Event Status Plan Status/Sub-status
What event leads to this change?
Scheduled
Pending/Scheduled
When we complete enrollment into a plan (or COC
or termination). Also, when we know that the
corresponding plan and plan-event have not been
processed for 834 (failure to process from the last
batch-process-run)
Submitted
Pending/Submitted
When we pick up plan-events and successfully
generate an 834 XML that will be submitted to
Edifecs for processing.
Acknowledged
Pending/Acknowledged When Edifecs sends an 834c acknowledgementresponse, accepting our XMLs after they parse it
through their 6 layer schema validation.
Approved
Pending/Approved
When Edifecs sends a 999 response to the
submitted 834 XMLs
3. This new flow of plan-sub-status may have to be validated by the functional team too, but assuming that this
gets accepted, I want to bring to the table, the following point – Most of our code works off the
status/substatus – pending/submitted. If we do any changes on the sub-status-flow to respond to plan-event
status, then we will have to make corresponding changes to OneGate code across layers to respect these
new flow of Plan-sub-status.
a. The immediate impact area is – My Accounts > My Health Plans tab. We will have to start respecting
the new sub-status flows here, if we want to see the pending plans, and make corresponding
changes in code to write sub-statuses from the backend code to follow the new sub-status-flowpath.
b. The next impact area is eligibility determination because this leads to plans being split (APTC
changed etc), and plan-split respects pending/submitted status/substatus.
c. The next impact is with COC flows, because we split plans based on any changes to APTC, CSR, Ageoff etc. and the plan-split respects pending/submitted status/substatus duo.
d. We also have to look at any SOA/Siebel calls respecting this status/substatus.
In general, we have to look at a deeper impact of changing plan-sub-status to reflect plan-events-status, if we are
touching plan-statuses too with an 834c response.
We will wait to hear back your thoughts and comments.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Jonah Egenolf
Sent: Monday, October 20, 2014 9:01 PM
To: Brett Ackerman
Cc: Dattatreya Subramanya Vellal; Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath;
Anagha Joshi; Vinay Shivanna; Manasa Swamy; Ashwini Ramesh Hegde; Kavya Ramaiah; Sachin Shivarama Nayak;
3

Satheesh Kumar Raju; Vinay Sulumane Visweswara
Subject: Re: 20th Oct 2014 - MoM - Edifecs, PS Rewrite, MA Demo

Whether our terminology is correct or not, 999 is the issuer ack. Thus the 834c is the edifecs ack. Google seems to
agree with that definition.
So it may not be correct terminology but it does match what Datta is saying. We are supporting edifecs ack this week
and issuer ack next week.
Sent from my iPhone
On Oct 20, 2014, at 10:48 AM, "Brett Ackerman" <backerman@exeter.com> wrote:
Datta,
Thanks for the update.
With regards to the Plan Status, my understanding is that the 834c (Confirmation) transaction
indicates that the 834 has been processed by the carrier whereas the 999 only acknowledges receipt
of the 834.
Thus, my expectation is that when we process the 834c the Plans Status/Sub status will be updated
to Pending/Approved to indicate the 834 transaction has been completed and plan is pending until
Effective Start Date.
Does that align with what is planned for Wednesday?

Thanks in advance,
Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell:
617.645.4570

From: Dattatreya Subramanya Vellal
Sent: Monday, October 20, 2014 10:36 AM
To: Brett Ackerman; Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath;
Jonah Egenolf
Cc: Anagha Joshi; Vinay Shivanna; Manasa Swamy; Ashwini Ramesh Hegde; Kavya Ramaiah; Sachin
Shivarama Nayak; Satheesh Kumar Raju; Vinay Sulumane Visweswara
Subject: RE: 20th Oct 2014 - MoM - Edifecs, PS Rewrite, MA Demo

Hi Brett,
Please find my updates inline.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Brett Ackerman
Sent: Monday, October 20, 2014 6:59 PM
To: Dattatreya Subramanya Vellal; Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar
Surendranath; Jonah Egenolf
Cc: Anagha Joshi; Vinay Shivanna; Manasa Swamy; Ashwini Ramesh Hegde; Kavya Ramaiah; Sachin
Shivarama Nayak; Satheesh Kumar Raju; Vinay Sulumane Visweswara
Subject: RE: 20th Oct 2014 - MoM - Edifecs, PS Rewrite, MA Demo
4

Datta,
Thanks for the update.
Can you confirm the following as part of the work to be completed 22-Oct:
1. We are updating the plan status as well as the plan event status?
[Datta]: Plan-status update is currently a part of 999, and not 834c. We have the structure
ready to update the plan-status and sub-status, but, 834c logically doesn’t update the planstatus. 834c only updates plan-event status.
2. We are doing additional testing of Initial, CoC, and Termination plan scenarios to make sure
our code works across multiple scenarios.
[Datta]: Yes these scenarios will be tested and validated.

Thanks,
Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell:
617.645.4570

From: Dattatreya Subramanya Vellal
Sent: Monday, October 20, 2014 8:27 AM
To: Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath; Brett Ackerman;
Jonah Egenolf
Cc: Anagha Joshi; Vinay Shivanna; Manasa Swamy; Ashwini Ramesh Hegde; Kavya Ramaiah; Sachin
Shivarama Nayak; Satheesh Kumar Raju; Vinay Sulumane Visweswara
Subject: RE: 20th Oct 2014 - MoM - Edifecs, PS Rewrite, MA Demo

Team,
Dates on Edifecs is as follows:
- 834 XML generation and 834c XML consumption will be demo-able by 22nd Oct 2014 end of
day IST. The end-end demo includes:
o Create an application on MA envt, complete plan-selection
o Generate 834 xmls for the plan-events created, when the batch-job from Siebel gets
triggered
Make sure that after the completion of the batch-job, the plan-event status
is changed to “Submitted”
Make sure that we have XMLs generated in a particular folder location (that
is configurable via a property)
o Assume that we have corresponding 834c XMLs in a predefined folder location of
OneGate
o Consume the XMLs from the location and change appropriate Plan-event status to
either 834-ack or 834-fail
See the plan-event status changed in Siebel
After these tasks, we also want to achieve 999 integration, that will mostly be by mid-next-week on
the same branch, and we also want to do movement of the XML generation and XML consumption
on the new data-layer, but that’s a separate activity to be tracked outside of MA Demo work.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
5

From: Dattatreya Subramanya Vellal
Sent: Monday, October 20, 2014 11:51 AM
To: Anagha Joshi; Vinay Shivanna; Manasa Swamy; Ashwini Ramesh Hegde; Dattatreya Subramanya
Vellal; Kavya Ramaiah; Sachin Shivarama Nayak; Satheesh Kumar Raju; Vinay Sulumane Visweswara
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde; Chandrashekhar Surendranath
Subject: 20th Oct 2014 - MoM - Edifecs, PS Rewrite, MA Demo

Edifecs:
- After talking to Shrinidhi, Krishna, Amit, Arun & Srini from Siebel and Suraj from SOA will
help us out with the pending pieces of Edifecs. This includes:
o Building a batch-process to look at our CRM and dump all pending 834 xmls into a
single configurable location
o Proper naming convention for the generated xmls –
OG_<batch_process_id>_<message_id>_<date_time>_<eventReason>.xml
o Building a batch process to look at a configured location and consume the 834c xmls
into OneGate
o Ability to pass messageID into 834, and read it back in 834c
o Ability to call api code from Siebel (includes PlanSelection to expose new methods –
one for 834, one for 834c)
o Ability to report success/failure of read for each of the 834c XMLs
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

6


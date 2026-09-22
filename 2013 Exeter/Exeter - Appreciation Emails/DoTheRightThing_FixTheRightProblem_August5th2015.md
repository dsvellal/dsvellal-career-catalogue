# DoTheRightThing FixTheRightProblem August5th2015

> Converted from document `DoTheRightThing_FixTheRightProblem_August5th2015.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

EG JIRA
Wednesday, August 05, 2015 8:50 PM
Dattatreya Subramanya Vellal
[JIRA] Ajinth Christudas mentioned you (JIRA)

Follow Up Flag:
Flag Status:

FollowUp
Completed

Ajinth Christudas mentioned you on

ONEGATECORE-27327

Re: RT: Issues with initial plan slices with exceptional circumstance
while RENEWALS period is ON
Hi Gaurav Gupta,
Thanks for the analysis. Dattatreya Vellal, Jonah Egenolf and I tried look at this again and we were
able to replicate this issue. We should reopen this ticket.
One thing I noticed was that the Open Enrollment configs were a little different when you executed
the test case to what I set up when I ran the case.
Here is the way the Open Enrollment periods should be set up. We are trying to mimic what would be
in VT LIVE
The link ed
image can not
be d isplay ed.
The file may
hav e been
mov ed,
ren amed, or
deleted.
Verify that
the link
points to the
correct file
and location.

Once we did that we replicated the issue again. MCN: 1-7594529
Looks like the issue is not replicable in HF2EBF2, when we followed the same steps. I am not sure if
this issue occurs in HF3, but we should test and confirm that is not the case.
For now, VT plans to use the workaround laid out in ONEGATECORE-27328 to proceed with testing.
Thanks,
Ajinth
Add Comment

This message was sent by Atlassian JIRA (v6.2.3#6260-sha1:63ef1d6)

1


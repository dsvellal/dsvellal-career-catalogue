# ClientSuccess Edifects MailFromBrett October3rd2014

> Converted from document `ClientSuccess_Edifects_MailFromBrett_October3rd2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Brett Ackerman
Friday, October 03, 2014 4:14 AM
Jonah Egenolf; Grant Spradlin; Audra Podany; Veronica Lee
Chevy Vithiananthan; Louis Gutierrez; Karen Zee; Chandrashekhar Surendranath;
Anuroop V. Gaonkar; Jonathan Kutchins; Dattatreya Subramanya Vellal
RE: Edifecs POC

All,
Yesterday morning, the team successfully generated data files from OneGate to Edifecs that allowed Edifecs to
create Initial, Change, and Termination 834s.
What that team was able to accomplish in a little less than 1.5 weeks has been fantastic. Thanks to all those involved
in helping us achieve this milestone and a special thanks to Datta and Anuroop who drove the majority of the
development effort. Great work!
Our goal next week is to fill the gaps in the areas identified during this week’s internal teams’ demo and to then
demo the end-to-end integration to the larger stakeholder group. We will also begin work on the next phase of work
middle to late next week to add the ability to consume Payer responses and Payer initiated plan updates.
ID
1
2

3
4
5
6
7
8
9
10
11
12
13
14
15

Action Item
Develop Draft System Interaction Diagram
Schedule Follow Up Meeting to review XML schema and discuss
details on the mapping from the Exeter enrollment data into the
Edifecs XML schema.
Provide Input and Output XML formats
Elaborate System Interaction Diagram
Draft Scope Document
Draft Schedule
Provide Data Dictionary for ECF format and/or functional mapping
documentation for codes and logic
Facilitate direct introductions between the development teams to
streamline work
Provide SFTP Details for environments
Create Export from OneGate into ECF Format
Create Inbound and Outbound Routes per Interaction Diagram
Internal End-to-End Demo of Initial Enrollment, Termination, and
Change
Follow Up to Gaps Found During End-to-End Demo
End-to-End Demo to Larger Stakeholder Group
Finalize Scope of Next Phase of Work

Owner
Exeter
Edifecs

Due Date
Fri - 9/19
Fri - 9/19

Status
Complete
Complete

Edifecs
Edifecs
Edifecs/Exeter
Edifecs/Exeter
Rajesh/Shane

Mon - 9/22
Mon - 9/22
Mon - 9/22
Mon - 9/22
Tue – 9/23

Complete
Complete
Complete
Complete
Complete

Shane/Brett

Tue – 9/23

Complete

Brett
Jonah
Rajesh
Exeter/Edifecs

Wed – 9/24
Fri – 9/26
Fri – 9/26
Wed – 10/1

Complete
Complete
Complete
Complete

Exeter/Edifecs
Exeter/Edifecs
Brett/Shane

Tue - 10/6
TBD
Wed – 10/7

In Progress
Planned
Planned

Thanks,
Brett

Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Brett Ackerman
Sent: Tuesday, September 23, 2014 12:46 PM
To: Jonah Egenolf; Grant Spradlin; Audra Podany; Veronica Lee
Cc: Chevy Vithiananthan; Louis Gutierrez; Karen Zee; Chandrashekhar Surendranath; Anuroop V. Gaonkar
Subject: RE: Edifecs POC
1

All,
We met with Edifecs last night to review the scope and timeline (attached).
Here are the key takeaways:
• The schedule has us complete for demo on 10/1, this is dependent on Dev being complete by end of this
week
• Edifecs won’t be able to merge the changes we send them as part of this first iteration due to the time
constraint. So we will send them changes as they come and they’ll send out individual transactions.
o We’ll resolve this as part of the next part of the integration effort (e.g. post 10/1)
• Edifecs will send us a data dictionary and/or functional mapping document for their ECF format so we can
develop the XML properly
• Scope of work includes initial enrollment, changes and disenrollment
o Essentially exchange initiated enrollment actions are in scope
• Edifecs will provide confirmation and success/error reporting, however it will not be consumed by OneGate
as part of the 10/1 effort
• Edifecs will apply 834 Baseline Biz Rules Levels 1-6 on data we send them. No carrier specific rules are
included for the 10/1 effort

Here are the current action items:
ID
1
2

3
4
5
6
7
8
9
10
11

Action Item
Develop Draft System Interaction Diagram
Schedule Follow Up Meeting to review XML schema and discuss
details on the mapping from the Exeter enrollment data into the
Edifecs XML schema.
Provide Input and Output XML formats
Elaborate System Interaction Diagram
Draft Scope Document
Draft Schedule
Provide Data Dictionary for ECF format and/or functional mapping
documentation for codes and logic
Facilitate direct introductions between the development teams to
streamline work
Provide SFTP Details for environments
Create Export from OneGate into ECF Format
Create Inbound and Outbound Routes per Interaction Diagram

Owner
Exeter
Edifecs

Due Date
Fri - 9/19
Fri - 9/19

Status
Complete
Complete

Edifecs
Edifecs
Edifecs/Exeter
Edifecs/Exeter
Rajesh/Shane

Mon - 9/22
Mon - 9/22
Mon - 9/22
Mon - 9/22
Tue – 9/23

Complete
Complete
Complete
Complete
In Progress

Shane/Brett

Tue – 9/23

In Progress

Brett
Jonah
Rajesh

Wed – 9/24
Fri – 9/26
Fri – 9/26

In Progress
In Progress
In Progress

Jonah and Grant – please feel free to add anything I may have missed.

Thanks,
Brett

Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Brett Ackerman
Sent: Tuesday, September 16, 2014 8:51 PM
To: Jonah Egenolf; Grant Spradlin; Audra Podany; Veronica Lee
Cc: Chevy Vithiananthan; Louis Gutierrez; Karen Zee; Chandrashekhar Surendranath
Subject: RE: Edifecs POC
2

All,
Thanks again to all of you who participated in today’s call with Edifecs.
The call went well from our perspective and gave us a pretty clear line of sight on what we need to do and what is
needed by Edifecs. In summary, our scope of work will be focused in generating the data in an XML format (same
used by FFM) that Edifecs will consume and then generate and send the needed 834s. This will speed up the process
and provide potential future compatibility as States roll off the FFM. We will also support responses from Edifecs to
track status of the 834 transactions. We will ignore 820s for now, though Edifecs express interest in discussing our
vision for 820s post this initiative.
Immediate Next Steps
Action Item
Provide Input and Output XML formats
Develop System Interaction Diagram
Draft Scope Document
Draft Schedule
Schedule Follow Up Call with Group for
Integration Deep Dive on Monday

Owner
Rajesh (Edifecs)
Grant
Brett/Shane, Hemanth (Edifecs)
Brett/Shane, Hemanth (Edifecs)
Shane (Edifecs)/Brett

Due Date
Friday - 9/19
Wednesday - 9/17
Friday - 9/19
Friday - 9/19
Friday - 9/19

Thanks,
Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Brett Ackerman
Sent: Monday, September 15, 2014 4:24 PM
To: Jonah Egenolf; Grant Spradlin; Audra Podany; Veronica Lee
Cc: Chevy Vithiananthan; Louis Gutierrez; Karen Zee
Subject: Edifecs POC

All,
Louis asked me to coordinate with Edifecs to push the initiative forward. Our goal is to have a POC of initial
enrollment and CoC 834s in the next few weeks.
We have a call scheduled tomorrow to review the Edifecs solution and to begin refining the scope of the POC. The
output of this call should be a better understanding of where OneGate ends and Edifecs begins, so that we can
identify what resources are needed to move this effort forward in the timeline outlined by Jonathan.

Thanks,
Brett

Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

3


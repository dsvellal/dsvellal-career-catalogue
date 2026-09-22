# Leadership&Ownership AgeOutIssues April3rd2015

> Converted from document `Leadership&Ownership_AgeOutIssues_April3rd2015.pdf`

Dattatreya Subramanya Vellal

Cc:
Subject:

Jonah Egenolf
Friday, April 03, 2015 8:36 PM
Thomas Leong; Michael Poulshock; Lakshmi Thanga-Raja; Chandrashekhar
Surendranath; Chevy Vithiananthan; Dattatreya Subramanya Vellal; Satheesh Kumar
Raju; Sachin Shivarama Nayak
Brett Ackerman; Audra Podany; Dinesh Surajiwale
Re: age out issue

Follow Up Flag:
Flag Status:

Follow up
Completed

From:
Sent:
To:

So we have a potential plan of action here. Lemme describe the problem first:
Any time we rate a plan, we use the start date of the plan slice as the age-relative date for rate band
calculations and household composition determinations. Sometime around 3329HF4 (or sometime before
now) we also changed rating to calculate the premium for the start of each future month when we enroll
in a plan. This was apparently a request from Hawaii so we respect the premiums as they increase
throughout the year or as someone ages throughout the year.
The impact on VT, however, is not very good. VT does not change premiums throughout the year, and they
do not rate by age. So the only thing that can happen is that a family that used to qualify for a given
household composition could now fall out of that qualification and into individual pricing. So for a family of
5 with a 26 year old son, their premium would go from about 2X (the family rate) to 5X (5 X the individual
rate). Meaning a 250% jump in premium even though there was no action on the part of the customer.
Note that this rerate problem will happen ANY time a customer's plans are rerated for any reason. So the
proactive future slice insertion exacerbates the problem, but the problem is already there.
And now my understanding of the desired behavior:
VT would like a member birthday to never impact household composition unless the case the member is
on is in an enrollment window (open, special, renewal). Note this means that household composition MAY
change (example: a couple signs up, later one of the couple dies, so they will switch to individual). Also
note that anything eligibility related is still left in the hands of OPA. We're really talking about control over
premium changes here.
And the potential solution:
We will add a system parameter that, if set to true, will ensure that the start date of the plan timeline_id is
used as the relative date for age calculations (for rating and for household composition) unless they are in
the add/remove member screen and are in a special enrollment period, in which case it will take the start
of the specific slice being rated as the relative date for age calculations. (If we do add/remove member in a
special enrollment period, we probably should create a new timeline_id so we use this slice start date for
any future rating. Otherwise the age relative date will revert to the start of the timeline if we rerate the
customer later outside of add/remove member. I think we should punt on this aspect of the problem,
though. It's an edge of an edge and should never be worse for the customer.)
The expectation is that this is about 1 day of work. Assuming we can get the green light, Datta, Satheesh
and Sachin can get this work done on Monday so that EG can pick it up for testing during our day Monday.

1

And I think we should get this fix in. It's pretty terrible behavior that is not really related to these age out
changes. Even if we did nothing on age out, we'd want to fix this in HF2.
- Jonah

From: Thomas Leong
Sent: Thursday, April 2, 2015 8:21 PM
To: Michael Poulshock; Lakshmi Thanga-Raja
Cc: Brett Ackerman; Audra Podany; Dinesh Surajiwale; Jonah Egenolf
Subject: Re: age out issue

Hi Michael,
The logic is built into the plan selection process (in the rating logic in og-api). The case that I mentioned
earlier is happening on initial plan enrollment.
Thanks.
-thomas
From: Michael Poulshock
Sent: Thursday, April 2, 2015 7:46 PM
To: Lakshmi Thanga-Raja
Cc: Brett Ackerman; Audra Podany; Thomas Leong; Dinesh Surajiwale; Jonah Egenolf
Subject: Re: age out issue

The rulebase logic should cover this regulatory requirement.
M
On Apr 2, 2015, at 1:58 PM, Lakshmi Thanga-Raja <Lakshmi@exeter.com> wrote:
This requirement aside what has been built should be prepped for testing.
I will follow up with Jonah and ESI on the effort and resourcing and have a decision on this
tomorrow morning.
Lakshmi

-------- Original message -------From: Brett Ackerman <backerman@exeter.com>
Date: 04/02/2015 4:51 PM (GMT-05:00)
To: Audra Podany <apodany@exeter.com>, Thomas Leong <TLeong@exeter.com>, Lakshmi
Thanga-Raja <Lakshmi@exeter.com>
Cc: Dinesh Surajiwale <dsurajiwale@exeter.com>, Jonah Egenolf <jegenolf@exeter.com>,
Michael Poulshock <mpoulshock@exeter.com>
Subject: RE: age out issue
Lakshmi and Jonah,
2

I think this will come down to what you think the LOE will be to accommodate this regulation.
If we can’t support this logic, I’m wondering whether it makes sense to even bring in the updated
functionality.
I’ll defer to you both on what is feasible for HF2 vs what gets moved to HF3.

Thanks,
Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell:
617.645.4570

From: Audra Podany
Sent: Thursday, April 02, 2015 4:01 PM
To: Brett Ackerman; Thomas Leong; Lakshmi Thanga-Raja
Cc: Dinesh Surajiwale; Jonah Egenolf
Subject: RE: age out issue
Hi all,
Just to clarify a bit more, basically the functionality described by Thomas is desired based on current
functionality. However, if we are to implement the new age-out logic requested in JIRA 24999,
current functionality will have to be altered. Essentially, the new CMS requirements state that when
an individual turns 26, they should only age-off at the next Open or Special Enrollment Period not at
end of the month in which the individual turns 26.
I would recommend viewing the summary in http://172.17.0.100:8080/jira/browse/ONEGATECORE24999.
Let me know if there are any questions.
-Audra
From: Brett Ackerman
Sent: Thursday, April 02, 2015 3:53 PM
To: Thomas Leong; Lakshmi Thanga-Raja
Cc: Dinesh Surajiwale; Audra Podany; Jonah Egenolf
Subject: RE: age out issue
+Jonah
From: Thomas Leong
Sent: Thursday, April 02, 2015 3:51 PM
To: Lakshmi Thanga-Raja
Cc: Brett Ackerman; Dinesh Surajiwale; Audra Podany
Subject: age out issue

Hi Lakshmi,
Currently, if there is a person that will age out during the year, a plan slice (member
coverage) is created starting the first of the subsequent month.
3

Example:
- 1 household, with 2 members - 1 dad, 1 son (birthday 8/5/1989 - turns 26 this year).
- in Member Coverages, there are 2 plan slices
-- one for 5/1/2015 - 8/31/2015 enrolled in Plan A, with a premium of X
-- one for 9/1/2015 - 12/31/2015 enrolled in Plan A, with a premium of Y
So, the user is still on the same plan, but the rate changes on 9/1/2015. The reason
according to ESI is that the son is falling out of the 26 rate band in the 9/1 slice. This is part
of core rating functionality, and is not an easy fix. ESI estimated a couple of days of work,
which would prob mean a little more than couple of days for me, since I am not as familiar
with the code. Since this logic is part of core rating functionality, not sure of downstream
impacts either.
Audra and I spoke earlier, and confirmed that 2 plan slices are not expected, (at least not at
initial application/plan selection). She will follow up with SME/EG VT to confirm.
Thanks.
-thomas

4


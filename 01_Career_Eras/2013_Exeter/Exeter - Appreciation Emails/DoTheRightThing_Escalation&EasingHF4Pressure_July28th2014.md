# DoTheRightThing Escalation&EasingHF4Pressure July28th2014

> Converted from document `DoTheRightThing_Escalation&EasingHF4Pressure_July28th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Chandrashekhar Surendranath
Monday, July 28, 2014 4:11 PM
Dattatreya Subramanya Vellal; Krishnamurthy Hegde; Anuroop V. Gaonkar
FW: HF4 plan changes

FYI and for your eyes.
From: Chandrashekhar Surendranath
Sent: Monday, July 28, 2014 4:12 PM
To: Jonah Egenolf; Chevy Vithiananthan; Lakshmi Thanga-Raja
Subject: RE: HF4 plan changes
Hi
We are moving forward on this based on the risk perception that you have around this.
The issue on how we avoid last mile demands (anticipated or unanticipated) on a release is still a standing debate
(because we do have other places where this happens) which needs to be had after we have cleared HF4.
In this case, Datta and his team were systematically pressurized over the last few weeks by changes coming from
various quarters which was demotivating them because they came into work every single day seeming to be the
bottleneck despite enhanced allocations.
We have had conversations with them and we also slowed down significantly over the last few days to make sure
that they got a chance to catch up with their breath (and sleep). I think we owe it to them to make sure that we
smoothen things for them.
Let’s catch up on the other side of the release.
Regards
Shekhar
From: Jonah Egenolf
Sent: Friday, July 25, 2014 10:33 PM
To: Dattatreya Subramanya Vellal; Chevy Vithiananthan; Chandrashekhar Surendranath; Anuroop V. Gaonkar;
Krishnamurthy Hegde; Lakshmi Thanga-Raja
Subject: RE: HF4 plan changes

Wanted to circle back with development here. I walked through this with Datta, and while he's not thrilled
with the changes, based on my conversations with the project teams, I think this is necessary work. The
tradeoff we're making is that we're doing some additional work to attempt to keep the states/CGI happy
with a pretty major but necessary change.
I talked through this with Chevy and he's on the same page. One of the key goals here is that we need to
make sure (or as sure as we can) delivering this hotfix does not break CGIs custom code. So we need to
make this happen for HF4.
Given that, this just comes down to a resourcing issue. Datta is thinking this represents 3 days of work for
bodies he doesn't really have since they are flat out doing bug fixes which also need to happen.

1

I just want to make sure we have a plan of attack here. I think Datta is happy to take this on, but we need
to be aware that we are squeezing here. Getting more hands on deck here would be good if we have them
available.
- Jonah

From: Jonah Egenolf
Sent: Thursday, July 24, 2014 9:11 PM
To: Ajinth Christudas; Megan Gupta; Darren He; Chwee Chua; Chevy Vithiananthan; Lakshmi Thanga-Raja; Audra
Podany; Laura Kling; Karen Zee; Brett Ackerman; Dattatreya Subramanya Vellal; Sachin Shivarama Nayak; Satheesh
Kumar Raju
Subject: HF4 plan changes

I've talked to most of you about this at one point or another, but I want to combine everything into a single
conversation and hopefully close it out. First lemme describe the fundamental change in HF4 so everyone
is on the same page:
Prior to HF4, all plan changes came from either SR processing or plan selection. This could cover many
changes, but all of them resulted in terminating the old plan and provisioning a new plan with the new
changes reflected. Additionally, multiple concurrent changes were effectuated on the date of the earliest
desired date for any included change. In practice, this meant that if you had an APTC change it happened
at the start of the next month, and if you did not it followed the 15/16 rule (I think).
In HF4 there are a couple major changes to this behavior.
First and foremost, we no longer do ANY plan changes in place. The primary example of this is APTC
distribution. Prior to HF4, Siebel did the APTC distribution via in-place updates. That means we had no date
audit trail of when the change happened and what dates it should have been active etc., nor could we
future date to the start of the next month etc.
But more generally speaking, now ANY plan change will abide by the desired effective date for the type of
change and create a new plan accordingly. The behavior is similar to the current SR processing behavior, it
just covers a broader set of plan changes. Or rather ALL plan changes.
Also new in HF4: SR processing no longer chooses a single effective date for the change. If we have an
APTC change coincident with a CSR change, the APTC change will follow the first of the next month (in
most cases) and the CSR change will follow the 15/16 rule. So if the change happened on the 17th of a
month, APTC would start the first of the next month and CSR would start the first of the following month.
Meaning we'd terminate the existing plan, add a new plan active for 1 month with just the APTC change
and add another new plan active from the end of the next month to the end of the year to cover the APTC
change and the CSR change.
So, HF4 does not introduce the concept of terminating a plan and adding a new one to effect a change, but
it does expand the volume of these new plans pretty substantially.
So what does this mean for HI and VT? I walked through this with Ajinth and Chwee and they both want
to keep the status/substatus as it currently is for SR processing and making sure the GUID/change indicator
is set any time one of these slices is created.

2

The thought is basically: the HF4 changes are simply an expansion of what SR processing is already doing,
not a fundamental change. So even if it's not functionally great, current behavior is tolerable and will make
the fewest waves and have the highest chance of just working with CGI's custom code. From a functional
perspective, I think we can look the other way a bit in an effort to keep the states content. We're not
getting worse here, and getting better seems like it'll cost us more points than it scores.
So to be explicit, that means our approach for HF4 plan changes will be:
- Any time we create a new slice, we create it as pending/submitted
- If we create multiple slices in a single execution, all will be pending submitted
- Any time we terminate a slice, we set it to Surrendered (regardless of status)
- Any time we create a slice or terminate a slice, we set the change indicator on that plan and we set the
change GUID on the master case
The only outstanding issue right now is how we handle the plans where start=end for HI. Chwee is going to
circle back on that after sitting down with the 834 devs, but other than that we should be all set.
I think this matches pretty closely with what we're already doing in HF4, and it is certainly easier than what
I thought we were going to have to do.
That's it. If anyone has issues with this approach, let's hear em.
- Jonah

3


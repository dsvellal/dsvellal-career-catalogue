# Collaboration IssueAnalysis&QuickTurnaround September13th2015

> Converted from document `Collaboration_IssueAnalysis&QuickTurnaround_September13th2015.pdf`

Dattatreya Subramanya Vellal

Subject:

Krishnamurthy Hegde
Sunday, September 13, 2015 8:04 PM
Chevy Vithiananthan
Chandrashekhar Surendranath; Lakshmi Thanga-Raja; Srinivas Jillella; Dattatreya
Subramanya Vellal
RE: Urgent Vermont HF3 EBF request

Follow Up Flag:
Flag Status:

Follow Up
Completed

From:
Sent:
To:
Cc:

+Datta – whose team helped with the quick analysis!
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Res: +91-80-23368241 | Off: +91-8033450029 | Skype: khegde
From: Krishnamurthy Hegde
Sent: Sunday, September 13, 2015 8:04 PM
To: Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>
Cc: Chandrashekhar Surendranath <schandrashekhar@exeter.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>;
Srinivas Jillella <SJillella@exeter.com>
Subject: RE: Urgent Vermont HF3 EBF request
Hi Chevy,
Here is what came out of the dev team analysis:
• 26563 – Manual Renewals Issue
o LOE is 1 day
o Impacted objects:
Siebel objects related to ‘Renewals Plan Copy’. Hence, no risk of regressing on other flows.
• 28165
o Automatic Renewals Issue. Wrong input going into the SLCSLP computation.
o LOE is 1 day
o Impacted Objects:
Data Layer jars. Hence, absolutely no impact on the non-auto-renewal flows.
• 28166 & 28167
o Automatic renewals issue. Suspected that APTC redistribution and CSR level setting is going wrong
under certain circumstances.
o LOE is 1 day
o Impacted Objects:
Data Layer jars. Hence, absolutely no impact on the non-auto-renewal flows.
I don’t believe we have a definitive way to confirm if these issues are replicable in 3.3.2.11 as well, without either (a)
a detailed code comparison or (b) retesting these issues on 3.3.2.11. Let me know if this is critical for today and we
can go with option (b) which might take a 2-3 hours of turnaround.
The overall DEV effort for all these issues, based on our current high level analysis is 1 day. But testing would take
additional day at least, is the gut feel.
Thanks,
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Res: +91-80-23368241 | Off: +91-8033450029 | Skype: khegde
From: Chevy Vithiananthan
Sent: Sunday, September 13, 2015 7:02 PM
1

To: Krishnamurthy Hegde <khegde@exeter.com>
Cc: Chandrashekhar Surendranath <schandrashekhar@exeter.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>;
Srinivas Jillella <SJillella@exeter.com>
Subject: Re: Urgent Vermont HF3 EBF request
Thanks Krishna,
I have a call with the internal team so information will be great
I would
Like to know if they are real issues
Have they been fixed in 33211
If not - just need to know level of effort and impact (such as files, modules etc)
Sent from my iPhone
On Sep 13, 2015, at 8:40 AM, Krishnamurthy Hegde <khegde@exeter.com> wrote:
We are trying to see if we can get the LOE in the next few hours. Our support has done all the
replication and analysis that it could. Trying to muster dev help now. Hopefully will have an update
by 11am. Will keep you posted.
Sent from my Windows Phone
From: Chevy Vithiananthan
Sent: 13-09-2015 17:35
To: Chandrashekhar Surendranath; Krishnamurthy Hegde
Subject: Fwd: Urgent Vermont HF3 EBF request
Is there a chance to look at this?
Sent from my iPad
Begin forwarded message:
From: Christopher Simo <CSimo@exeter.com>
Date: September 12, 2015 at 8:48:51 PM EDT
To: Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>, Brett Ackerman
<backerman@exeter.com>, Chandrashekhar Surendranath
<schandrashekhar@exeter.com>, Krishnamurthy Hegde <khegde@exeter.com>,
Srinivas Jillella <SJillella@exeter.com>
Cc: Ajinth Christudas <achristudas@exeter.com>, Megan Gupta
<mmgupta@exeter.com>, Simon Gawlik <sgawlik@exeter.com>, Jonathan Kutchins
<jkutchins@exeter.com>, Matt Cahir <mcahir@exeter.com>
Subject: Urgent Vermont HF3 EBF request
Team There was an emergency call tonight with Vermont and Optum leadership to discuss
that status of renewals testing. Vermont has identified the following issues as
critical path to generate the ‘passive’ renewals file.
Key
ONEGATECORE28167

Summary
RT: APTC allocation/CSR allocation
issues in the 2016 plan slices after
running the batch (specific test case)

2

ALM
987

ONEGATECORE28166

RT: Full APTC is not applied to 2016
QHP plan in mixed HH after renewal
batch run

985

ONEGATECORE28165

RT: APTC Eligibility (APTC Amount)
Incorrect when executing the batch
job for this specific test case

984

ONEGATECORE26563

RT: Critical Age Out Scenario (e.g.,
26 year old age out) Puts all
Applicants on Individual Plans after
Running Renewal

989

Practically – the issues impact only select populations – mixed HH, age
offs, etc. However, the carriers process the passive file all at once (and then
terminate records) thus SoV/Optum believes these issues are a blocker to testing.
This has been escalated and Vermont is pushing for the ETA ASAP asking if it could
be done as soon as tomorrow.
There is another check in call with leadership tomorrow (Sunday) and Vermont
asked for the following:
• ETA on an EBF
• Objects potentially impacted by the EBF – can they continue to seed 2015
test cases or will the objects impacted by this EBF also touch objects related
to initial applications (requiring regression testing)
Thanks,
Chris

3


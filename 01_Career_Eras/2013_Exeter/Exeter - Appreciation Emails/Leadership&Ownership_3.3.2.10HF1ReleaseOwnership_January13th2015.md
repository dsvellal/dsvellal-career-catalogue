# Leadership&Ownership 3.3.2.10HF1ReleaseOwnership January13th2015

> Converted from document `Leadership&Ownership_3.3.2.10HF1ReleaseOwnership_January13th2015.pdf`

Dattatreya Subramanya Vellal
Chandrashekhar Surendranath
Tuesday, January 13, 2015 4:40 PM
Dattatreya Subramanya Vellal
Chandrashekhar Surendranath; Anuroop V. Gaonkar; Krishnamurthy Hegde
Re: 33210 hf1 additional ticket queries

From:
Sent:
To:
Cc:
Subject:

This is good. Thanks.
Regards
Shekhar
Sent from handheld. Please excuse typos.
On Jan 13, 2015, at 4:37 PM, Dattatreya Subramanya Vellal <dvellal@exeter.com> wrote:
Hi Shekhar,
From the list, the following are the categories:
•

5 JIRAs: Needs functional teams intervention
o ONEGATECORE-17705
o ONEGATECORE-23483
o ONEGATECORE-23932
o ONEGATECORE-24250
o ONEGATECORE-24259

•

18 JIRAs: Needs QA verification as of 3.3.2.10 HF1, and if replicable, then a decision on
whether they should be fixed in 3.3.2.10 HF1 or not has to be taken by PMO
o Query: issue in (ONEGATECORE-17378,ONEGATECORE-21328,ONEGATECORE21562,ONEGATECORE-23260,ONEGATECORE-24262,ONEGATECORE24286,ONEGATECORE-24289,ONEGATECORE-24336,ONEGATECORE24369,ONEGATECORE-24374,ONEGATECORE-24375,ONEGATECORE24380,ONEGATECORE-24401,ONEGATECORE-24405,ONEGATECORE24417,ONEGATECORE-24419,ONEGATECORE-24421,ONEGATECORE-24422)

•

26 JIRAs: Needs code fix
o 14 JIRAs have low fix effort (1 to 2 PD per JIRA) can be considered for HF1: issue in
(ONEGATECORE-23723,ONEGATECORE-24187,ONEGATECORE24203,ONEGATECORE-24204,ONEGATECORE-24205,ONEGATECORE24207,ONEGATECORE-24208,ONEGATECORE-24209,ONEGATECORE24260,ONEGATECORE-24364,ONEGATECORE-24373,ONEGATECORE24382,ONEGATECORE-24424,ONEGATECORE-24425)
o 11 JIRAs have medium fix effort (3 to 5 PD per JIRA), PMO to take a call for inclusion:
issue in (ONEGATECORE-15923,ONEGATECORE-23624,ONEGATECORE23819,ONEGATECORE-23842,ONEGATECORE-24025,ONEGATECORE24291,ONEGATECORE-24315,ONEGATECORE-24367,ONEGATECORE24379,ONEGATECORE-24400,ONEGATECORE-24403)
o 1 JIRA is a high fix effort issue (>5 PD): ONEGATECORE-21025 – Part of which is being
addressed in 3.3.2.10 HF1. Everything else is APTC FSD implementation. Any further
changes in this should be considered for deferring to a future release.

•

2 JIRAs: Need Support team’s intervention and closure
o ONEGATECORE-24104
o ONEGATECORE-24261
1

•

4 JIRAs: Need LAT/Field team’s responses
o ONEGATECORE-23747
o ONEGATECORE-23748
o ONEGATECORE-23791
o ONEGATECORE-24368

•

2 JIRAs: Need PMO intervention
o ONEGATECORE-23215
o ONEGATECORE-24372

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Tuesday, January 13, 2015 2:44 PM
To: Chandrashekhar Surendranath
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde; Kavya Nagabhushan; Manasa Swamy
Subject: RE: 33210 hf1 additional ticket queries

Team,
Here’s the summary of the issue analysis. Thank you Kavya and Manasa for helping out.
Legend:
Fix Type Legend
R
F
NF
V
Func
NOP

As of 3.3.2.10 HF1
Needs Replication
Needs code fix
No fix required
Needs validation and closure
Needs functional validation
No operation. Needs PMO intervention

Summary:
Fix Type

High

Low

Medium

Grand Total

F

1

14

Func & F

1

3

4

1

1

6

8

Func & V
NOP

2

R&F

11

26

1

1

R&V

1

1

2

V

9

1

10

5

5

19

57

V&F
Grand Total

4

34

Please note, refer to “Area of fix” section in the attached spreadsheet to determine the technology
area of fix.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
2

From: Dattatreya Subramanya Vellal
Sent: Tuesday, January 13, 2015 11:49 AM
To: Chandrashekhar Surendranath
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde
Subject: RE: 33210 hf1 additional ticket queries

I have combined the two queries and there are 57 issues with the.
((status in (open, reopened, "In Progress") AND reporter in (mmgupta, achristudas, clai, sgawlik,
csimo) AND issuetype in (bug)) OR (fixversion in ("3.3.2.10 Hot Fix 1") AND status in (open,
reopened, "In Progress") AND type not in (ops-deployment, clarification))) ORDER BY fixVersion ASC
Will be taking a pass at this and send out issue/no-issue and the level of effort (high/medium/low)
for each.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chandrashekhar Surendranath
Sent: Tuesday, January 13, 2015 10:14 AM
To: Dattatreya Subramanya Vellal
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde
Subject: FW: 33210 hf1 additional ticket queries

Please check on these and let us know what the deal is.
From: Lakshmi Thanga-Raja
Sent: Monday, January 12, 2015 9:04 PM
To: Krishnamurthy Hegde; Chandrashekhar Surendranath
Subject: 33210 hf1 additional ticket queries
Please take a look and let me know what the forecast is like –
status in (open, reopened, "In Progress") AND reporter in (mmgupta, achristudas, clai, sgawlik, csimo) AND issuetype in
(bug)
fixversion in ("3.3.2.10 Hot Fix 1") and status in (open, reopened, "In Progress") and type not in (ops-deployment,
clarification)
Thanks,
Lakshmi

Lakshmi Thanga-Raja | E X E T E R | (m) 617.596.1843

3


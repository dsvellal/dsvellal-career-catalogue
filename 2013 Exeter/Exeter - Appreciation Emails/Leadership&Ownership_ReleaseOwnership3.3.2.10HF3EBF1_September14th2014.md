# Leadership&Ownership ReleaseOwnership3.3.2.10HF3EBF1 September14th2014

> Converted from document `Leadership&Ownership_ReleaseOwnership3.3.2.10HF3EBF1_September14th2014.pdf`

Dattatreya Subramanya Vellal
Dattatreya Subramanya Vellal
Monday, September 14, 2015 12:36 PM
Titoo Thambi; Kavya Nagabhushan; Harish Kumar Karnati; Kausalya Mani; Anagha Joshi;
Manohar Veeraiah; Srinivas Channakeshavala; Satheesh Kumar Raju
Amit Sharma; Krishnamurthy Hegde; Chandrashekhar Surendranath; Dharnish
Yediyurappa
3.3.2.10 HF3 EBF1 - Details

From:
Sent:
To:
Cc:
Subject:

Team,
We are focusing on getting through with the issues reported for the latest 3.3.2.10 HF3 EBF1 release. Here are all the
details that you will need. We are focusing on three main parts here:
a) Merge from 3.3.2.10 HF2 EBF3 to 3.3.2.10 HF3 EBF1 (also includes a button fix done in the current 3.3.2.11
fix via dev-jira: 28094)
b) Rob’s fixes for Renewals tracked through: 28169
c) The other bug fixes tracked via JIRA query: fixVersion = "3.3.2.10 Hot Fix 03 EBF 01" and type not in (Story,
Ops-Deployment) and status in (Open, "In Progress", Reopened)
SVN Branch: svn://172.17.10.60/onegate/branches/3.3.2.10-hotfix03-ebf-new
Envt details:
a) Dev:
I.
II.
b) Test:
I.
II.

http://ogsbl3.3.2.10hf3ebf1dev.og.devexeter.com:9280/epublicsector_enu/start.swe
http://ogapp3.3.2.10hf3ebf1dev.og.devexeter.com:7004
http://ogapp3.3.2.10hf3ebf1test.og.devexeter.com:7004
http://ogsbl3.3.2.10hf3ebf1test.og.devexeter.com:9280/epublicsector_enu/start.swe

Merge needs to happen from SVN branch: svn://172.17.10.60/onegate/tags/release-3.3.2.10-hotfix02-ebf-3. Merge
will be co-ordinated between Titoo, Kavya N, Harish, Kausalya. Merge ops-jira has been raised here: 28170
JIRA Fixes: Currently we have the following split:
JIRA
28169

Assigned to
Anagha

28165

Anagha

28167

Manohar

28166

Manohar

28168

Kausalya

Description
Rob’s fixes to
renewal code, to be
merged into the new
branch
APTC Eligibility
incorrect when
executing the batch
job
APTC/CSR allocation
for 2016 plans are
incorrect
Full APTC is not
allocated to 2016
QHP plans
BLI status issues
after renewals

Status
On Hold

Comments
Will be taken up after Anagha fixes
28165.

ETA
Today (14th
Sept 2015)

In
Progress

Will be fixed

Today (14th
Sept 2015)

In
Progress

Will be fixed

Today (14th
Sept 2015)

In
Progress

Will be fixed

Today (14th
Sept 2015)

In
Progress

This is a merge of SOA object from
deployment ticket 28093. Kausalya
will take this up after she
completes SOA merge.

Today (14th
Sept 2015)

1

26563

Srini &
Satheesh

27888

Ajinth

Age-out not working
after manual
renewals copy
Parent not eligible
for subsidy after
renewals

In
Progress

Needs Siebel Fix. Srini is helping us
do this.

Today (14th
Sept 2015)

On Hold

Needs PMO intervention. We are
waiting for Vermont to come back
on this issue, and haven’t heard
back yet.

NA

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

2


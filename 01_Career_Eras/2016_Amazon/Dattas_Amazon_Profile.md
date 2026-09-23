# Dattas Amazon Profile

> Converted from document `Dattas_Amazon_Profile.pdf`

Summary
•
•
•
•
•

Joined Amazon on 15th Feb 2016
Code Activity: 570 changes (182,992 lines added; 41,481 lines removed) on 75 packages
since about 2 years ago
Tickets resolved: 86 tickets resolved
LinkedIn Page: https://www.linkedin.com/in/dattatreyavellal
Life prior to Amazon: Dattatreya S Vellal Resume (work-ex until Feb 2016)

2018 Contributions
Major Technical Contributions
#

Contributions

Date

Brief Description

1

VariableComparisonTool
enhancements

20th
March
2018

For SVA’s Pay-to-load latency
reduction project, I have enhanced the
variable comparison tool with the
following functionalities:
1.

2.

3.

Added GLS filtering – this will
help in fetching orders to a
specific list of GLS provided
via command line.
Added variable filtering –
This will help in generating
the comparison report for
only the list of variables that
have been specified via this
option, and will skip the TEC
call made to fetch all the
variables specified for a
country.
Added sampleOrderIds per
variable mismatch – This will
help in identifying the
orderIds for which the
variable mismatch was
found. Currently this supports
two use-cases: a) Variables
that have mismatched in both
FRS & Fortress, and b)
Variables that have defaulted
in Fortress, but have not in
FRS. The command line tool
accepts max no. of orderIds
that will be reported along
with “Variable Mismatch
Summary” table. The
samples generated, as
reported, is sorted based on
descending order of absolute
difference between fortress
variable value and frs
variable value.

Impact

•
•

•

Reduced SDE efforts in figuring out
variable samples and the respective
orderId.
Daily report emailed to the ML team &
the development team, to help
collaborate & work on mismatches & fix
them faster
Generic tool enhancements to ensure
that when the S-Team goal, for which
this tool was built, is taken up again, the
enhnacements help in reducing SDE
efforts by bringing up the right kind of
samples to the ML Scientists & the
developers to dive deep & figure out the
mismatch root-cause.

4.

Decimal point precision:
Decimal point precision can
now be controlled via input
parameter to the command
line tool. This will ensure that
we don't get misled by
samples which have
difference of 1*10^-6 or so.

Other Impactful Activities that I led in 2018
#

Contributions

Date

Brief Description

1

March 2018 - APS and
AbuseCOPS IMR
Reduction

20th
March
2018

Identified opportunity to reduce the
total no of hosts, when doing 2018
Prime-day scaling. Ran FLO tests and
ensured that our hosts are
benchmarked correctly & the right no.
of hosts are used to support our
traffic.

Impact

•
•
•

AbusePreventionService: Saved
$6446.28 per year.
AbuseCOPSService: Saved $5897.88
per year.
Total cost savings of $12344.16 per
year!

2017 Contributions
Major Technical Contributions
#

Contributions

Date

Brief Description

1

Launching AmazonPay in
India, with One-accountper-customer fraud check

14th
April
2017

Project phoenix, which intended to
launch AmazonPay - Amazon's wallet
in India, with OneAccountPerCustomer
fraud check. This was handled endend by me.

•

2

Risk Document Creation

28th
April
2017

Creating a generic input document
structure that can be used by RiPE
(Risk Profile Evaluation) to handle
client specific, and Platform specific
inputs, in a generic way.

•

RiskDocument became a part of RiPE
API.

3

RiPE API - CSTech Usecase

Worked with Raman to facilitate the
initial launch of RiPE API for CS-Tech
use-case. This included presenting
RiPE to our director Anand and
developing and delivering the
components required for addressing
the CS-Tech use-case.

•

Gift Card Service calls out the CR's and
integration test written by me, to allow
them to on-board to RiPE
RiPE Integration Test and how to call it,
Appreciation for helping CAS team
members

Analysed who are our clients calling
FDPS, and created a follow-up wiki
page to help see if these clients still
have dependencies on FDPS. The

•

4

FDPS/RDPS Analysis

23rd
June
2017

Impact

•

•

API written by me evaluates about 2.5k
requests per day.
TPS supported by my API: 1150.
Requested TPS: 20.

Suggested an approach of leveraging
RDPS for fixing a known problem

intent is to see how we can support
FDPS hosting RiskDocument, instead
of FraudDocument, also to analyse if
we have a chance of gracefully
depricating FDPS and move to a new
data-store (RDPS) if there is a need.
5

Bulk API - for SVA related
actions

31st
July
2017

•

Created a generic bulk action tool for
SVA, to help take care of backlog
issues that arose due to understaffing
and underestimation during the
AmazonPay launch. This tool was
generically written to extend the right
components of TRMS to solve SVA
related problems.

•

•

5927 Investigations which had missed
SLA because of peak loads during the
PPI lauch (Amazon Wallet in IN), were
reopened and investigators were
allowed to work on the same and
complete the backlog.
This tool was reused and exnteded to
generated related-customer-ids for a
given primary customer - again an adhoc request that came from the
investigation manager to handle
investigations. Ease of extension can be
derived from the submitted CR.
Reported as a successful in-time
delivery

Other Impactful Activities that I led in 2017
#

Contributions

Date

Brief Description

1

Insist on high
standards:
Evangelised and led
interivew questions
bash

10th
Feb
2017

Identified the need to have a set of
well curated questions across DS,
Algo and PS, which'll help TRMS
interviewers in quickly picking and
choosing the right set of questions
when conducting a technical
interview. Conducted a interview
question bash, contributed the max.
no. of questions to it, and created a
question bank of 30 well curated
questions that can be used for PS,
Algo and DS problems, during
phone-screen and in-person
interviews.

2

Learn & Be Curious: IP
idea submission

28th
Feb
2017

An IP was submitted, with primary
author being Datta for a method and
approach of using social media
sentiment analysis for business
improvement.

3

Invent & Simplify

19th
May
2017

Created an idea for the Think Big
2017 contest, about how we can
integrate containers & amazon's
retail catalog. The idea also explains
how this integration can benefit
customers.

4

RiPE Poster selected
for 2017 India Tech
Conference

7th
July
2017

Submitted poster of RiPE, got
selected to present the same in 2017
India Tech Conference

Impact

•

•
•

14 weekend interview events have
happend as of Oct 2017 and in all of them,
the initial screening questions have been
asked from this list.
Many of the senior interviewers have
referred the question banks.
2 Weekend drives conducted on
HackerEarth by using the questions from
the question-bank.

Result: IP marked to be protected as trade secret.

5

Unblocked production
launch

26th
July
2017

Amazon Pay PPI general availability
launch was blocked because it was
not whitelisted as a valid payment
instrument, and I was called up on to
diagnose this and take it to
completion. I noticed that the
payment instrument type was
wrongly sent.

6

Influenced INPay Tech
team to fix their bug
the right way

20th
Sept
2017

Noticed a strange bug where our
SVA herd workflows were erroring
out because AusterService
(dependent downstream service)
was throwing an exception when an
SVA account status was being
changed from "SUSPENDED" to
"SUSPENDED". I did the dive deep
to understand why our flows were
erroring out, identifed the issue,
opened a SIM against AusterService,
and followed up to ensure that this is
fixed.

7

QMS enablement for IN
SVA

26th
Sept
2017

Enabling Queue Management
Service for IN Retail. During peak
times, like Diwali, Christmas, New
Year, Cyber Monday etc., SVA will
run promotional offers. These offers
will result in increased traffic and
there-by increased investigations
being queued. In SVA, we have
queues with very low SLA timelines
(1hr) and with high volumes, it
becomes difficult to adhere to SLAs
for all the queued investigations.

8

IN SVA - PayToLoad
latency reduction

28th
Nov
2017

Working to reducre PayToLoad
latency for SVA load and redeem
orders.

9

IN AbuseCOPS
COD_SUPPRESSION
rules movement

4th
Jan
2018

Problem given to me was to figure
out a way to minimise the leakages
happening for cash-on-delivery
payment instrument suppression,
month-on-month. I identified one of
the root-cause being our code, where
the payment-suppression rules were
executed in stage-3 of a 4-stage ruleexecution phase. I conceptualised
the solution of carving out codsuppression-rules for India business,
and move them from stage-3 to
stage-1, so that we can effectively
evalaute cod-suppressions fairly
quickly and surface that result first to
our upstream services to take
appropriate decisions.

10

AbusePreventionServi
ce optimisation using
profiler

10th
Jan
2018

I analysed Profiler
(profiler.amazon.com) data for
AbusePreventionService and was
able to identify root-causes for high
CPU consuming cycles and make
effective code changes to reduce the

I collaborated with the INPayment team and
ensured that this is solved end-end.

•
•

The technical implementation necessary
for QMS enablement in IN was complete
within a week's time. This was led by me.
The issue of making this only work for IN
SVA orders, and not for the entire IN
Retail orders was made apparent, and it
required IN SVA & ML scientists to
collaborate and write the necessary RMP
rules to do so. This task is currently
blocked.

GC CPU % consumption reduced from 23% to
under 2%.

CPU cycle usage on non-business
logic code
11

Driving IMR reduction
by h/w replacement

10th
Jan
2018

As a part of 2017 Dec, I took up the
activity of releasing un-used
hardware and optimise hard-ware
usage by potentially replacing oldgeneration hardware with new
generation hardware.

Total hardware savings of over $23K per year.

12

S-Team goal

5th
Sept
2017

As a part of S-Team goal, I
contributed towards resolving a few
major SIM's that validated mismatch
of variables evaluated by FRS and
Fortress, in Inline evaluation.

Resloved 5 SIMs that validated variable
mismatches across multiple calculators.

Other mentions
•
•
•
•
•
•
•
•
•

Insist on highest standards: Pioneering & upholding high standards for design documents within the
team.
Created an on-boarding page for TRMS-INPay team.
Created on-call helpbook for TRMS-INPay team.
Presented RiPE to Dave Rockett (TRMS Director), during the science fair:
Interviews (3 weekend events, a total of 46 interviews - 21 Phone-screen, 23 On-site interviews, 2
internship conversion)
Tech reviewer for promotions of 3 SDE-1's to SDE-2's.
Was instrumental in bringing two SDE's (SDE-2 and SDE-3) on-board to TRMS
Devised "Scaling Dev Process" to incorporate great scrum practices within the organisation of our L7
manager.
Anchored and hosted the first TRMS-SHOW-TIME, one of a kind fun activity within TRMS-Tech across
the world, and was presented in the monthly newsletter from Anand:

2016 Contributions
Major Technical Contributions
#

Contributions

Date

Brief Description

1

SDE Onboarding contents

Feb
2016

As a new member into the SCPIAN (then GRCS Feeds) family,
while I was being on-boarded
into the team, I created a
respository of contents that
would help others on-board
faster. This repository did not
exist before.

•

The MySQL DB which was
running on a host (gcsavalanche-mysql-1002.vdc) was
migrated to an RDS instance

•

2

Migrating
FeedCollectorHistoryService
MySQL DB to an RDS
instance and depricating the
old one

8th
Mar
2016

Impact

•
•

•

Created a structured approach for onboarding a new team member (with
specific sessions addressing specific
agenda).
Created a repository of high-quality
content that can be referred by anyone
(refer hyperlinked content).
Faster and a more structured on-boarding
of new joiness into the team, with all
necessary contents easily accessible.

FeedCollectionHistoryService is now
dynamically scalable.
The migration details were shared with
other teams for their use, reducing their

migration efforts from 2 weeks to a few
days.

3

Incorporating changes made
to open-source lib (Json-lib)
into Madeira

28th
Mar
2016

My first major code push to
Amazon's code base. In this, I
have modified an open-source
json-parser (Json-lib), to
generate consistent-json's and
integrated it into Madeira.

•

Enabling the team to move all XML based
feed standards to migrate to the new
parser.

4

Migrating GDSN (mergefeed) to the new XML parser

6th
April
2016

GDSN was the first of the XML
feed standard to be migrated to
the new xml parser. To migrate
GDSN to consume the new XML
parser, I enhanced the existing
DocstoreTool to incorporate a
bulk-up-converter, which would
pull all aspects of a given
standard and would bulk-up
convert an aspect from the oldinconsistent-format to the new
consistent-format

•

8% reduction in caffeine code written by
SDT teams (this is for one feed standard!
and SDT team handles about 20+ feed
standards). Assisted reduction in datareview from days to mins.

•

Came up with a strategy of migrating the
remaining XML based feed standards from
the old-xml-parser that generated
inconsistent ions to the new xml parser
that generates consistent ions, this
allowed us to come up with a generic
formula that can be handed-over to SDT's,
thereby reducing the SDE's effort involved
in migrating XML based feed.

•

Documented the most common mistakes
that may happen when migrating a mergefeed so that the lessons can be recalled
and mistakes not repeated for any future
transactions

•

Migrated the most complex XML nonmerge feed from old xml parser to the new
xml parser. Total vendors submitting feeds
in this standard were around 40
Enhanced the framework to support a
generic way of migration of non-merge
XML standard feeds to the new parser.
Wrote step-by-step SOP that our SDT's
can take up for migrating other XML feeds,
reducing the SDE involvement (hours)
On-boarded the SDT team members into
using this standard to migrate other XML
non-merge feeds
Follow-up with SDT team in ensuring that
we stick to the SOP for all migration

5

Migrating ACV (non-merge
feed) to the new XML parser

25th
May
2016

Migrating the most complex nonmerge XML feed standard (ACV)
to the new XML parser. Coming
up with a generic framework to
migrate any other non-merge
XML based feeds to the new
XML parser. Handing over the
SOP to the SDT team for
migrating any other XML nonmerge feed standard to the new
XML parser.

•
•
•
•

6

RCSQueryGeneratorTool

16th
June
2016

Wrote an RCS query generator
tool that:

•
•

Generates RCS queries
for a variety of valuemetrics queries
Downloads the RCS
response and splits it
into single json records

•
•

Automated way of querying data from
Retail Catalog Search and uploading it to
EDX for report generation.
Circumventing the disability of EDX to
accept hundreds of GB of single-line data
(as provided by RCS response) by
programatically splitting that data into
mulitple lines of single json responses,
and uploading it to EDX. Sample:
createsByDate query, which was run from

•

Uploads the split
content to EDX datawarehouse for valuemetrics downstream
operations and eventual
generation of valuemetrics reports

•

Jan 1970 to June 2016 contained 250
Million ASINs, which resulted into a single
file of about 100 GB, which was
programmatically processed and uploaded
to EDX!
Setting up a continuous data fill strategy to
pull appropriate data from RCS and
uploading it to EDX.

Assisted in backfilling the data
from RCS into EDX - there by
ensuring that when value-metrics
reports were generated, we had
the complete historic data since
Jan 1970.
Automated RCS query pulls by
creating appropriate DJS jobs.
7

GOV3 Migration to the new
xml parser

17th
Sept
2016

GOV3 is a merge feed and
requires specific steps of
migrating the old aspects into
consistent ion format.
The general steps involved are:
for every vendor aspect, get the
aspect, back it up, up-convert,
delete all historic record of the
aspect and put the up-converted
aspect back to the aspect doc
store.

•
•
•

Ensured that all code is plugged in the
right part of the platform, to ensure
configuration driven migration.
Successfully transitioned the migration
process to SDET team with minimal SDE
involvement.
Ensured migration of vendors via SDET
and recorded a live session captured.

Other impactful work
•
•

Winners of the ACSCS hackathon 2016. I wrote the SCPCatalogSearchAsinFetch package to fetch
ASINs for a catalog-search-query. Our hackathon video is uploaded here. Appreciation email is here.
I am an Amazon Agile Group recognized facilitator for - Scrum workshop and Product Ownership
workshop.

Reusable assets
•
•
•
•

Bookmarks: 794 unique visits as of 24th Oct 2017
1st week, non-tech On-boarding guide: 229 unique visits as of 24th Oct 2017
AbusePreventionService Scaling Development Process
Interviews taken for TRMS between 1st Jan 2017 and 24th Oct 2017 - 21 Phone Screen (14 Inclined, 7
Not-inclined), 23 On-site interviews (12 Inclined, 11 Not-inclined), Total of 44 interviews (26 Inclined, 18
Not-inclined).

Awards, Recognitions
•

October 2017 - TRMS Zeus Team Award for exceptional project delivery, RiPE.
Certificate: https://photos.app.goo.gl/Cd1GAgXuew0EEn2a2

•

November 2017 - TRMS Spot Award for contributing towards team process improvements.
Certificate: https://photos.app.goo.gl/v56xFvXIINeY0rjT2

Givebacks
Scrum Workshop Facilitator
Workshop details

•
•
•

10th Dec 2017: Presenter Score: 4.6, Classroom Experience: 4.2
18th Dec 2016: Presenter Score: 4.47 , Classroom Experience: 4.12
11th Nov 2016: Presenter Score: 4.12, Classroom Experience: 3.97

Agile Product Ownership Facilitator
Workshop details

•

16th Feb 2018: Presenter Score: 3.9, Classroom Experience: 4.4


# 201709 SVABulkActionTool TRMSWide Report.pdg

> Converted from document `201709_SVABulkActionTool_TRMSWide_Report.pdg.pdf`

Tuesday, November 28, 2017 at 6:50:43 PM India Standard Time

Subject: Status Report : TRMS India Payments: Sept 4th 2017
Date: Monday, 4 September 2017 at 10:21:15 AM India Standard Time
From: Kapoor, Aditya
To:
trms-phoenix-all@amazon.com
CC:
Kapoor, Aditya
Project Name
SancHon Screening from C2D Use Case
Amazon Pay: SVA Bulk AcHon Tool
Amazon Pay: Tools to Query Customer Id and Related Customer Id
Amazon Pay: Ability go to get SVA Customer Name
Amazon Pay: Enhance One Account Per Customer SoluHons
Amazon Pay: Implement SGD to allow Queue Management for Peaks
Pay to Load Latency ReducHon
High Frequency Recharges
Program
Project

India Payments
Real Time SancJon Screening for
SVA using LexisNexis for C2D use
case

Status
Date

Completed

Project Type

External

Launch Date

Goal

Launch Real Time SancHon
Screening for SVA using LexisNexis
for C2D use case

SDM

Aug 16th
Aditya Kapoor

Sept 4th

ObjecJve & Scope
Reserve Bank of India(RBI) has mandated that Amazon should not allow Denied ParHes to create and
operate Amazon Pay (SVA) accounts. SVA tech team was building soluHon using Checkpoint Service to
screen accounts denied party, however this soluHon has been put on hold Hll RFI process is ready to
be rolled out. In order to launch SVA we decided to use Lexis Nexis Bridger data for SancHon
Screening at Hme of RegistraHon. Lexis Nexis performs SancHon Screening for all Amazon.in customer
against denied party list on daily basis. The results of this screening are available via web services. We
will use exposed web services to extract the data from Lexis Nexis Bridger and build soluHon that will
allow SVA to query this data. In case of C2D, we need to prescreen the customer with COD order. This
requires a bulk API.
Accomplishments
· Completed the implementaHon for Bulk API
· Bulk API pushed to Beta for IntegraHon with C2D
SNo
Tasks
Owner
ETA
Status
th
1
Requirement DeﬁniHon (Wiki Link)
TRMS
Completed
July 11
2

Design Review

TRMS

July 15th

Completed

3

ImplementaHon Completed pushed to
Beta
Publish TPS Supported and Latency
Numbers
Push to Prod

TRMS

July 29th

Completed

TRMS

Aug 11th

Completed

TRMS

Aug 16th

Completed

5
6

Program

India Payments

Status

Green
Page 1 of 5

Project

Amazon Pay: SVA Bulk AcJon Tool

Date

Sept 4th

Project Type

External

Launch Date

Goal

Allow Re-Drive of Queued Customer
for One Account per Customer Use
Case.

SDM

Aug 25th
Aditya Kapoor

ObjecJve & Scope
Number of people registering for SVA wallet was higher than expected. At the same Hme number of
people queued for invesHgaHon and queue rate was 5%+. This resulted in large backlog for operaHon
team. Once task missed SLA, Ops team were not able to take acHon on this and these needed to be
re-driven in bulk to allow Ops team to take acHon
Accomplishments
Completed the Development of SVA Bulk AcHon Tool
SNo
Tasks
Owner
ETA
Status
st
1
Requirement DeﬁniHon (Wiki)
TRMS
Completed
Aug 1
2

OpHon and Design for the tool(Wiki)

TRMS

Aug 7th

Completed

3

ImplementaHon Completed

TRMS

Aug 25th

Completed

4

Tool used to open 5293 SLA-missed Task

TRMS

Aug 25th

Completed

Program
Project

India Payments
Amazon Pay: Tool to query SVA
customers id and Related
customerId

Status
Date

Completed
Sept 4th

Project Type

External

Launch Date

Goal

ConHnue to Support the Launch of
Amazon Pay by providing tools for
reoccurring request

SDM

Sept 1st
Aditya Kapoor

ObjecJve & Scope
Build tools which help support business by providing tools which allow us to handles reoccurring
request
SNo
Tasks
Owner
ETA
Status
1
Enhance the SVA bulk acHon tool to
TRMS
Aug 31st
Completed
allow generaHon of Primary Customer
Id and Relate Customer Id

Program
Project

India Payments
Ability to Get SVA Customer Name
in IW for Benami Account Check

Status
Date

Green

Project Type

External

Launch Date

Sept 15th
Aditya Kapoor

Sept 4th

Goal
Show SVA Customer Name in IW
SDM
ObjecJve & Scope
SVA Customer name can be diﬀerent from Amazon IdenHty Customer Name. Business team needs
SVA customer name to check for Benami Accounts
SNo
Tasks
Owner
ETA
Status
st
1
Provide a short-term mechanism to
TRMS
Completed
Aug 31
Query SVA Customer Name. Team
Page 2 of 5

2

wrote a slap shot contract to get SVA
customer name. This was
Provide SVA customer name in IW

TRMS

Sept 15th

In progress

Program
Project

India Payments
Amazon Pay: One Account Per
Customer Version 1.1

Status
Date

Green

Project Type

External

Launch Date

Goal

Enhance the one account per
customer soluHon

SDM

DFD –Sept 7th
Aditya Kapoor

Sept 4th

ObjecJve & Scope
One Account Per Customer use case was launched along with wallet. We need to add following
features to One Account Per Customer to improve the soluHon and reduce queue rate.
1) Prime account should be put in Debit Only Mode
2) Queue Rate reducHon of One Account Per Customer Use Case
3) Take Ownership of SVA Tech IntegraHon with CCS
4) Re-design SVA Tech IntegraHon with CCS to allow for modiﬁcaHon of threshold without code
change
5) NauHlus MigraHon for One Account Per Customer InvesHgaHon Widgets
S.No.
Tasks
Owner
ETA
Status
1
Requirement DeﬁniHon
TRMS
Sept 7th
In Progress
th
2
Project Plan
TRMS
In progress
Sept 7
3

Publish a Feature wise launch plan

TRMS

Sept 10th

Program
Project

India Payments
Amazon Pay: Implement SGD for
Peak Queue Management

Status
Date

Project Type
Goal

External
Implement SGD for Peak Queue
Management

Launch Date
SDM

To be Started
Sept 4th

Aditya Kapoor

ObjecJve & Scope
SGD allow to build ruleset which can be used for peak queue management. Deep dive, invesHgate
and Build SGD for India Payment Use Cases
SNo
Tasks
Owner
ETA
Status
1
Deep Dive to Understand SGD
TRMS
Sept 10th
To be Started

Program
Project

India Payments
Pay to Load Latency ReducJon

Status
Date

Yellow

Project Type

External

Launch Date

Goal

Provide Low Latency EvaluaHon for
use-cases which need instant
fulﬁllment like SVA Load. The goal is
to reduce the Hme it takes more
money to show up in wallet aker
customer see’s that thank you page.

SDM

Oct 15th 2017
Aditya Kapoor

Jul 31st 2017

Page 3 of 5

ObjecJve & Scope
Buyer Fraud Service (BFS, also referred as FRS) is used for evaluaHon in retail COW workﬂow to
evaluate risk and take acHon during Pre-Fulﬁlment Workﬂow stage. Because BFS evaluated orders in
PFW stage it does not have strict latency requirement and TP99 latency for BFS is 21 seconds. This
latency is not acceptable for use cases where fulﬁllment is needed instantly (for e.g. Digital Orders).
Amazon Pay is a payment instrument which allows user to load money to Amazon Pay account and
later redeem the balance for orders on amazon or even 3rd party. SVA Load has been conﬁgured as
retail order and hence BFS is used for evaluaHon of SVA Load and Redeem transacHons. As a product,
SVA load is very similar to Digital order and hence high latency leads to poor customer experience.
Just like SVA load and redeem, India Payments team has several use cases (Recharges, Bill payments)
in pipeline which need low latency evaluaHon. The objecHve is to provide Low Latency EvaluaHon for
use cases which need Instant fulﬁllment.
This will consist of two phases. Phase1 is the Steam schedule to roll out inline checks to IN. Phase 2:
Figuring out how to take acHon in checkout, for which we need to deﬁne requirements and ETA.
Accomplishments
ConHnue on Fixing of Variable mismatches. Team ﬁxed important issue with regards to variables that
were defaulHng. Backlog as of August 24 had 167 Variables mismatching, 24 calculators mismatching,
5 variables defaulHng and 3 calculators defaulHng. Report for Sept 3rd is being computed
S.No.
Task
Owner
ETA
Status
1
Weblab dialup to 1% in pass-through mode TRMS Dev
6/12
Completed
2

IdenHfy the list of variables for IN

TRMS Dev

6/16

Completed

3

IdenHfy the list of models and rulesets for
IN from BFS conﬁg

TRMS Dev

6/23

Completed

4

Build and Enhance automaHon to tools to
create India speciﬁc intents

TRMS Dev

6/30

Completed

5

Run SOP to create the event hook,
evaluaHon phase, outcome Scope

TRMS Dev

7/7

Completed

6

Build tools to compare evaluaHon result for
variables

TRMS Dev

7/7

Completed

7

Push the IN conﬁg to TEC

TRMS Dev

7/10

Completed

8

Weblab dialup to X% (X to be decided later)
in shadow mode

TRMS Dev

7/12

Completed

9

Generate mismatch Report for variables

TRMS Dev

7/13

Completed

10

Fix, Evaluate and retrain cycle for Variables

TRMS Dev

9/15

In Progress

11

Live Mode Readiness for Inline EvaluaHon

TRMS Dev

12

Phased Dialup

TRMS Dev

13

Deﬁne the Customer Experience for Inline
EvaluaHon
Deﬁne Task based on Customer Experience

Vinay

14

Aditya

Page 4 of 5

Program
Project
Project Type

India Payments
High Frequency Recharge
External

Status
Date
Launch Date

Goal

Prepaid recharge is the ﬁrst use
case for HFC. In case prepaid
recharges if fraud occurs, the
money is transferred to network
provided. The goal is evaluaHng
and prevent fraud for Prepaid
recharges.

SDM

On Hold
Jul 31st
Oct 30th
Aditya Kapoor

ObjecJve & Scope
Amazon India is launching High Frequency Recharges as new category. This category would include
orders which are recurring such as Bill Payments for uHliHes like DTH, Electricity, telephone, postpaid
and prepaid mobile recharges. Prepaid Mobile Recharges orders are being launched in ﬁrst phase.
The objecHve of this project is to be able to be able to Evaluate Prepaid Recharges for Fraud.
Accomplishments
On Hold Hll Fortress in available for this use case
SNo
1

Task
IdenHﬁed new variables to be built

Owner
Bilal/Akhil

ETA
6/12

Status
Completed

2

Requirement Review

TRMS Dev

6/30

Completed

3
4
5
6
7
8
9
10

Design Review
Plan for Development
Mockup for UI for InvesHgator
Fraud Document Changes: Code Review
New Variables Code Review
Wiring in Fortress
Model Building
Push to Prod

TRMS Dev
TRMS Dev
TRMS Dev
TRMS Dev
TRMS Dev
TRMS Dev
Bilal/Akhil
Team

7/7
7/28
7/14
7/21
7/21
10/07
10/21
10/30

Completed
Completed
Completed
Completed
Completed

Backlog Projects- Under Review
S
Project Name
No
1
Silent AuthenHcaHon
2
Post Dispatch Payment
3
AutomaHon of Charge Back for India

Page 5 of 5


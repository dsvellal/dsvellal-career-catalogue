# 201704 SVA OAPC Launch

> Converted from document `201704_SVA_OAPC_Launch.pdf`

Friday, October 13, 2017 at 6:59:37 PM India Standard Time

Subject: Re: TRMS Project Phoenix Status Update: Apr 17th 2014
Date: Monday, 17 April 2017 at 10:03:00 PM India Standard Time
From: Vaz, Dale
To:
Varadarajan, Anand
CC:
Kapoor, Aditya, trms-phoenix-all@amazon.com
Thank you Anand, Aditya and team for supporMng this criMcal product launch for India. ExciMng Mmes ahead.
Regards,
Dale
On 17-Apr-2017, at 5:34 PM, Varadarajan, Anand <anandva@amazon.com> wrote:

This is great work. Thanks team and looking forward to more deliveries for our payments
business inIndia.
Anand
From: Kapoor, Aditya [mailto:kapoorak@amazon.com]
Sent: Monday, April 17, 2017 1:15 AM
To: trms-phoenix-all@amazon.com
Cc: Kapoor, Aditya <kapoorak@amazon.com>
Subject: TRMS Project Phoenix Status Update: Apr 17th 2014
Importance: High
Phoenix has launched on Apr 14th. Thanks to the core TRMS India payments SDE team to
deliver on the important requirements: Da[a, Sumit, Chandrakant, Akash.
During this project we have received help, guidance and support from various teams and
individuals across the world. Thanks a lot, this was criMcal for success of this young team.
TRMS SVA account launch support
Project Name

Status

One Account Per Customer
PrevenQon of Re-entry
SancQon Screening at RegistraQon

Completed
Completed
Yellow

ConQnuous SancQon Screening

Yellow

Benami Account

Green

Program

TRMS India Payments

Project

One Account Per Customer

Project Type

External

Path to Green(if
Applicable)

Sharing Plan for
Development
Owner: Guru
SOP Agreement:
Owner: Vinay

Project
Status
Date

Completed

Launch
Date

Apr 14th

Apr 17th 2017

Page 1 of 6

Goal

One customer is allowed to create only one
SDM
Aditya Kapoor
Amazon SV account using one mobile number. But
a customer can create mulMple accounts through
mulMple mobile numbers and Amazon accounts.
Such accounts needed to be idenMﬁed and
suspended.
ObjecQve & Scope
The objecMve of OneAccountPerCustomer is to idenMfy if the customer has created mulMple SVA
accounts. If the customer has mulMple account, only one account should be in AcMve state,
remaining all SV accounts should be out in Debit Only State. The end to end scenario and scope is
described in wiki below.
h[ps://w.amazon.com/bin/view/Phoenix/TRMS/OneAccountPerCustomer/#HStage1:Reducingthemanualwork
Week Accomplishments
1) End to End IntegraMon TesMng was Completed
2) UAT Completed with OPS team
3) Code in ProducMon
4) With launch on 4/14, 6 Customers were queued for invesMgaMon and OperaMons was able
to take account level acMon on them
Path to Green
Next Steps
Code
Complete for
One Account
Per Customer.
IntegraMon
with TRMS
Orchestrator

Owner
Dev Team

ETA
Feb 15th
Feb 28th
March 17th

Status
Completed.

Balasubj/Manish Jain

Completed

UAT
Deployment
Dependencies

Aditya/ Sharrif
Aditya
Owner

Feb 22nd
Mar 3rd
March 24th
Apr 5th
Apr 11th
March 31st
Apr 11th
ETA

Risks

Owner

ETA

Status

Appendix
Use Case
DescripMon
Design

Wiki Links
h[ps://w.amazon.com/bin/view/Phoenix/TRMS/OneAccountPerCustomer/

Program

TRMS India Payments

Project

PrevenQon of Re-entry

Project Type

External

Goal

Customers whose accounts got terminated due to any of the follo
perform any transacMon related to SVA.

Completed
Completed
Status

h[ps://w.amazon.com/bin/view/Phoenix/TRMS/OneAccountPerCustomer/Design

Page 2 of 6

ObjecQve & Scope
The objecMve of PrevenMon of re-entry is to idenMfy and prevent customers from doing transacMon related to S
Scope of work:
VeriﬁcaMon that the variables regarding SVA as Payment instruments are correctly populated.
Add SVA related checks to BFS
Week Accomplishments
1. With new order’s we could see orders ﬂowing in and BFS ﬁring rules and some orders being queued for
Path to Green
Next Steps
Add SVA related checks in BFA
VeriﬁcaMon that variables are gekng
correctly populated in Prod order

Owner
Bilal
Sumit

Digital Orders VeriﬁcaMon

Anand/Ramesh

Dependencies
Prod Orders

Owner
Manish Jain

Prod Orders for Digital

Anshum@/Rameash

Risks
Digital orders have not been Tested and
any defects will not be ﬁxed prior to
release on Apr 10th
Appendix
Use Case DescripMon

Owner
Anshum@/ Ramesh

Wiki Links
h[ps://w.amazon.com/bin/view/Phoenix/TRMS/PrevenMon_of_R

Program

TRMS India Payments

Project

SancQon Screening at RegistraQon

Project Type

External

Project
Status
Date
Launch
Date

Yellow
Apr 17th
2017
Apr 30th
2017

Goal

IdenMfy customers who should not be allowed
to hold and operate SVA account by performing SDM
Aditya
SancMon Screening.
Kapoor
ObjecQve & Scope
The objecMve of SancMon Screening is to idenMfy customers who should not be allowed to
hold SVA accounts and operate them and block them. SVA account shall be screened
against Denied Party List using Checkpoint service and in case of Match(Fuzzy) shall be
queues for invesMgaMon.
During invesMgaMon, invesMgator may request informaMon from customer for
veriﬁcaMon(RFI). For 3/31 launch, we will use exisMng fax based soluMon.
Week Accomplishments
Path to Green
Page 3 of 6

1) Sharing the Development plan with SancMon Screening team on 2 Stage DPS
Check
2) Going forward this will be owned by Manish Jain Mll phase 1 is completed.
Next Steps
Owner
ETA
Status
Requirement
Aditya
Feb
Completed
DeﬁniMon
17th
Feb
28th
March
17th
Project Plan
Guru
Feb
17th
March
3rd
March
31st
Apr
20th
Design
Manish Jain
ImplementaMon Manish Jain
Dependencies
DescripQon/Owner
ETA
Status
Date of Birth
SVA Need to accept DOB as part of registraMon.
Risks
Appendix
Use Case
DescripMon

DescripQon/Owner
ETA
Status
Wiki Links
h[ps://w.amazon.com/bin/view/Phoenix/TRMS/InlineScreening

Program
Project

TRMS India Payments
ConQnuous SancQon Screening

Project Type

External

Goal

IdenMfy customers who should not be allowed to hold and o
SancMon Screening.

ObjecQve & Scope
The objecMve of SancMon Screening is to idenMfy customers who should not be allowed to hold SVA accounts an
periodically (every 24 hours) to account for changes in DPL lists and account modiﬁcaMon
Week Accomplishments
1) Just like RegistraMon Mme screening dates for ConMnuous Screening were also moved to 4/30
2) Slapshot Contract was wri[en for Get Customer Info
Path to Green
1) SOP Agreement between business and TRMS Ops team
Next Steps
Owner
Requirement DeﬁniMon
Aditya

Page 4 of 6

Project Plan

Aditya

Implement
Launch

Chandrakant
Chandrakant

Dependencies

Owner
VInay

SOP FinalizaMon
Risks
Appendix
Use Case DescripMon
Program

TRMS India Payments

Project

Benami Account

Project Type

External

DescripQon/Owner
Wiki Links
h[ps://w.amazon.com/index.php/Phoenix/TRMS/24HourSc
Project
Status
Week
ending
Launch
Date

Green
Apr 17th
2017
TBD

Goal

To idenMfy SVA Account where account name
appears to be “Benami Account” and queue them
SDM
Aditya
for invesMgaMon. If the account is Benami, such
Kapoor
account need to be reported back to RBI and
should be locked.
ObjecQve & Scope
To idenMfy SVA Account where account name appears to be “Benami Account” and queue
them for invesMgaMon. If the account is Benami, such account need to be reported back to
RBI and should be locked.
On a broad level, we would like to deﬁne “Benami” as follows: Account with
Blank name
Special characters in the name ( !@#$%^&*”:<>?,./’;~`{}|[]\-=_+() ) in the name
Xxx,yyy,zzz, xyz in the name
Names of super heroes – Superman, Batman, Antman, transformer, Avenger,
Incredibles etc. We can create a comprehensive list here.
Scope:
We would deﬁne two rulesets. One owned by compliance, one owned by fraud. One of the
ruleset owned by compliance, have staMc condiMons like names that we don't support,
frivolous names etc. For fraud evaluaMon, we would host a model, where we associate
names with fraudulent behavior. If we do this separaMon, we have separated compliance,
and model based fraud detecMon. For 3/31 release we will focus on staMc rules ruleset.
Week Accomplishments
Next Steps
Owner
ETA
Status
Requirement
Aditya
Feb 17 Completed
DeﬁniMon
th
March
17th
Project Plan
Aditya
Apr 3rd Not
Started
week
Design
Sumit
Apr
Completed
nd
2
week
Page 5 of 6

Design review
Dependencies
SOP
Risks

Sumit
Owner
Sharrif
Details

Appendix
Long Term
Requirements

Wiki Links
h[ps://w.amazon.com/bin/view/Phoenix/TRMS/BenamiAccountHandling/

ETA

Status

ETA

Status

Requirements in Backlog
C2D: Cash At Door Step enables registraMon for SVA account at Mme of delivery in case of
COD orders. The requirement is to prevent abuse in such use cases
P2B: Person to Bank enables customer to transfer SVA balance to Bank. The requirement
is to prevent fraud and abuse in this usecase.
P2P: Person to Person enables customer to transfer SVA balance to another SVA account.
The requirement is to prevent fraud and abuse in this usecase.
High Frequency Fraud and Abuse prevenMon

Page 6 of 6


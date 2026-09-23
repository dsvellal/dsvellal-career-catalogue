# BLR May Structured Architecting DAY 2

> Converted from document `BLR May Structured Architecting DAY 2.pdf`

Philips University

Structured Architecting
DAY 2 – Systems
Architecting Fundamentals
Sudeep Prasad
sudeep.prasad@philips.com
May 2019

Philips University

Recap of Day 1
Role and playing field of an architect
CAFCR+ model

2

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

The CAFCR Model
Drives, justifies, needs
What does customer need
in product and Why
Customer
What

Customer
objectives

Customer
How

Product
What

Application

Functional

Product
How

Conceptual

Enables, supports, restricts

3

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Realization

Recap Day 1

4

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Philips University

Storytelling
= Validating Assumptions
5

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Team Activity – CAFCR – Customer View
Describe the “Customer Objectives” view of your system of interest.
= WHAT the Customer wants; WHO are the customer’s customers?
What is the context in which the system has to perform?

6

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Criteria for a good story
Customer
objectives

Accessible, understandable
“do you see it in front of you?”

Application
Customer
objectives

Valuable, appealing

Attractive, important
“Are customers queuing up for this?”

Application

Conceptual

critical, challenging

“what is difficult in the realization?”
“What do you learn w.r.t. the design?”

Realization

Application

Frequent, no exceptional niche

“Does it add significantly to the bottom line?”
Application

specific

Names, ages, amounts, durations, titles, …

Functional
7

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Example Story – field upgrade
6 hours to migrate the DB
• Service engineer goes to the hospital

Needs to enter IT room

• Triggers a backup, waits for 2 hours to complete
• Triggers upgrade, waits for 1 hour
• Re-enters configuration and checks that things are working

• Restores backup, waits for 3 hours

Unpredictable! Min. 1hr

Needs to check with customer for sign-off

• Gets sign-off from HoD, returns

• Save 1 hour by backup-restore of configuration.
Avg 150 Euro per hour * #systems = xxxxxx Euro!

8

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Application View – Example: Scintimammography

In the scintimammography procedure, a woman
receives an injection of a small amount of a
radioactive substance which is taken up by
cancer cells, and a gamma camera is used to
take pictures of the breasts.

Knowing how the a customer is going to use
the delivered system is very important.
In this example, it will be difficult to know
that an arm rest my be needed sometimes.

10

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Application
View
– below
System Examples
Chose
1 or 2 items
from
government
financial dir.
Government cost of
Financial dir. Cash flow
cost of care
cash flow
care
cost of op.
cost of op.

insurance
Insurance
cost of care
cost of care

inspection
Inspection quality
quality

general
ref. physician
Ref. physician
practitioner
diagnosis
General practitioner
diagnosis treatment
patient
treatment

radiologist
nurse
Radiologist diagnosis
Nurse patient ease of
diagnosis
patient
reimburstment
work
reimburstment
ease of work

Accessory

administration
Administration patient
patient id
id invoice
invoice

fleet management
advanced vehicle control

patient
Patient
comfort
comfort health
health

IT dep.
facility man.
Facility man space
service
conformance
space
It dep. Conformance
security
securitysupp. service supp.

Cabinets
technical
room

airports
railways
console
control room

technical
room

control room

corridor
1 2 3

Functional flow

5

2D map (where)

6

7

8

Waiting room

functional flow

Call family doctor
Visit family doctor
Call neurology department
Visit neurologist
Call radiology department
Examination itself
diagnosis by radiologist

call family doctor

Report from radiologist to
neurologist

visit neurologist

visit family doctor
call neurology department
visit neurologist
call radiology department
examination itself
diagnosis by radiologist
report from radiologist to
neurologist

Visit neurologist

waiting room

days
1

4

Rest room

2D map (where)

1 meter

dressing
room
rest room

car repair
towing service

system context

patient table

console

Dressing
toll
room
tunnel

restaurants
gas stations

corridor

Stakeholders and concerns (who)
stakeholders
and concerns (who)

cabinets

bus lanes
lorry lanes

motorway
management
system

taxes
car administration
government

maintainer
cleaner
Cleaner accessibility
Maintainer
accessibility
accessibility
accessibility
safety
safety
safety
safety

accessory
cabinet

environmental monitoring

urban trafficPatient
control
magnet
table

operator
ease ofOperator
use ease
of use

magnet

1 meter

maintenance
contractors
cabinet

2

3

4

5

6

days

7

8

9

10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

work flow & time line (what, when)

corridor

Work flow & time line (what, when)

11

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Application View – Software / Service Examples
Order
entry

Field
Service

SAP

CBoM

Licensing
Upgrade
catalog

License
file

SAP

System context – data flow

Subcontractors
Field
Service

Competition
(AIAT)
Stakeholders
(add concerns)

Physicians,
Operators
Hospital IT

CSIP

Service
Marketing

12

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Hospital CxO

PRS

Team Activity – CAFCR – Application View

Describe the “Application” view of your system of interest.
Show how the customer is going to use this system in the defined context.

13

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Functional View: Top level specifications

input /
event

Interfaces / collaboration

Describe the system’s behavior

system seen as black box

Functions describe what rather
than how.

functions

output /
action

quantified characteristics

restrictions, prerequisites
boundaries, exceptions
standards, regulations

15

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Functions are verbs.

Input-Process-Output paradigm.

Team Activity – Top-down scan CAFCR – Functional View
Describe the “Functional” view of your system of interest.
Show the major functions needed to realize the customer objectives and application.

16

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Team Activity – Conceptual View
patient

work-list
attributes

attributes
examination
attributes

exam procedures
attributes

scan
attributes

scan procedures
attributes

pictorial index

precompiled

3D volume
Volume index

2D images
Volume index

data elements
additional to
the external
information model

https://www.denodo.com/en/data-virtualization/overview

Information flow

Information model

Lifecycle Decoupling
via Microservices
18

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Firmware

Ready-check

Setup

50 ms

200 ms

500 ms

Control-flow timing

Concept = Model = Analogy

Power auctioning

19

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Team Activity – Realization View
Realization View
• Describe a “realization view” of your system of interest to realize CAFC of CARCR
model
• Choose one and work it out

21

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Team Activity – Realization
Choose 1 or 2 items from below

GIVEN successful POST and velocity
WHEN it is safe to move
THEN move to end position
void moveToEndPosition(…)
{
if (safeCheck->safeToMove(…))
{
mover->movePropAng(…);
}
}

SW components & dependencies

Behavior Translation

Electrical engine

Standards and conventions:
Technology (.Net, REST, …)
Security
Coding guidelines
…

Fuel tank

transmission

Primary engine
battries

Fuel tank

2D layout of system internals
22

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

3D drawing of system internals

Report Out/
Group Discussion

“T-shaped” Presentation
Top-down presentation
Value Proposition
Why does customer want to buy?
Why do users like to use the system?

1

Business Proposition
How do we earn money?
How do we run a healthy business?

System Specification
What does customer get?
What is the system-of- interest
that we deliver?

2

Design
3
How will we realize this
specification?
How do we ensure performance,
safety, robustness, etc.?
24

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

4

Philips University

System Qualities

25

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Learning Goals
Become aware and understand how to:
• Identify system qualities related to the CAFCR+ views
• Use system qualities as a way to identify most relevant issues
• Integrate system qualities across views to identify architectural issues,
dilemmas, trade-offs, and sweet spots

26

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Quality needles as generic integrating concepts
Customer
objectives

Application

Functional

usability
safety
evolvability

27

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Conceptual

Realization

Philips University

Session Closing

28

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals

Thank you
29

Confidential

Version 1.1

DAY 2 – Systems Architecting Fundamentals


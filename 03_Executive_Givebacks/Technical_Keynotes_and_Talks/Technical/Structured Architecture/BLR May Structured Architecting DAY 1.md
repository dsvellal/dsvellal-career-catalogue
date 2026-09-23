# BLR May Structured Architecting DAY 1

> Converted from document `BLR May Structured Architecting DAY 1.pdf`

Philips University

Structured Architecting
DAY 1 – System Architecting
Fundamentals
Sudeep Prasad
sudeep.prasad@philips.com
May 2019
DAY 1 – System Architecting Fundamentals

2

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

A round of introductions
• Name
• Role in Philips
• Experience in Architecture

Expectations

4

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Rules of the game
DO’s
• Connect
• Collaborate
• Create
• Listen
• Participate
• Enjoy!

DONT’s
Say NO to interruptions:
• Emails
• Social media
• Smartphones
‘I know it all’ syndrome
‘Is this all’ syndrome

Timings: 09:30 hours to 16:30
Lunch at 12:30.

5

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Why Structured Architecting

Teaches a methodology used by system architects

Methodology based on best practices & mistakes from over 20 years

Best practices collected by Gerrit Muller, formerly at Philips and now at
TNO-ESI
The material of this training is largely stemming from his work.
Much material and background info can be found on:
http://www.gaudisite.nl/

6

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Program Objectives
Program Objectives
• Identify the Attitude and Ability of the
Architects
• Demonstrate and discuss Architecture
approach and practices
• To be aware of:
– Business context
– Role and task of the architect
– Customer value proposition
– Business proposition
– Multi-disciplinary design
– Lifecycle
– Cross-cutting concerns
– Financial considerations
– Platforms
– Need for aligned roadmaps

7

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

What now?
Day 1 – Role of a System Architect and introduction to CAFCR+ model

Day 2 – CAFCR + continued, Requirements elicitation

Day 3 – Key drivers, System partitioning, Static and dynamic behavior, Platforms

Day 4 – System lifecycle, Financial modeling, Consolidating

8

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Day 1 Objectives
1. Discuss and explain the purpose of an Architect in Philips
2. Provide an introduction to the CAFCR+ model

9

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Philips University

Learning by Reflecting

10

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Learning by Reflection – Four stage cycle of learning
Experiencing
Observing

Testing

Reflecting

Applying

Conceptualizing

Generalizing

Source: Kolb’s learning cycle
http://infed.org/mobi/david-a-kolb-on-experiential-learning/

11

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Analyzing,
Interpreting and
Explaining

Challenge: Double-loop learning
Single Loop
Reflect, Question
& Adapt
Assumptions, Governing
variables
(Why we do what we do)

Action Strategies &
Techniques
(what we do)

Observe Results &
Consequences
(What we get)

Reflect, Question
& Adapt
Double Loop

Single Loop: (most common style of learning)
• Basic problem solving: just “fix the problem” identified
Double Loop: More than “fix the problem”
• Question underlying assumptions, values and beliefs, and ways of working behind what we do
12

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Challenge: Double-loop learning
Make config:
Language
UI layout
Validation
Workflow

Single Loop

What are the
variations?

Complex
config &
Action Strategies

Assumptions, Governing
variables
(Why we do what we do)

Techniques
(what we do)

Reflect, Question
& Adapt
Observe Results & Rigid
Consequences design
(What we get)

Pre-configure

Reflect, Question
& Adapt
Double Loop

13

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Plenary – Discussion and Reflection

Use double loop learning to uncover root cause
List challenges and dilemmas in your work
Project – Product – Portfolio – Platform

14

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Business Context

16

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Learning Goals
Become aware and understand how to:
• Position ‘architecting’ in product creation context,
• Position ‘architecting’ in a broad business process context, and
• Deal with tensions between long term (strategic), mid term (tactical), and
short term (operational).

17

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Customer stakeholders
Users
user
operator
…

Brand
Functionality:

Decision makers
purchaser
owner
…

Customer
value
proposition

Society
social media
…

-

Appropriate
Efficient
RoI & Cost of ownership

Quality:
-

18

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Security, Privacy

Business stakeholders
Operational

Partnering
complementers
providers
…

server infra
data mining

…
Life cycle

Business
proposition

Marketability:
-

service
upgrades

Trust
Intended use
Tenders

…
Supply chain
procurement

Cost = Margins

manufacturing
…

IP protection & monetization

Commercial
sales

Ease of training

marketing
…

19

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Design stakeholders
Availability:
-

Technology
People

Efficiency:
-

Productivity
Outsourcing

Cost = Upfront

System
design

Others
regulations
standards
…

Technical disciplines

Application disciplines

mechanical eng.
electrical eng.
software eng.
…

domain (e.g., clinical)
human factors
…
20

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Stakeholders
Users

Operational

Partnering
user
operator
…

complementers
providers
…

server infra
data mining
…

Decision makers

purchaser
owner
…

Life cycle

Customer
value
proposition

Business
proposition

service
upgrades

Society
social media
…

…
Supply chain
System
design

Others
regulations
standards
…

procurement
manufacturing
…

Technical disciplines

Application disciplines

mechanical eng.
electrical eng.
software eng.
…

domain (e.g., clinical)
human factors
…
21

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Commercial
sales
marketing
…

Bringing innovation to the market
Users

Operational

Partnering
user
operator
…

complementers
providers
…

server infra
data mining
…

Decision makers
purchaser
owner
…

Life cycle

Customer
value
proposition

Business
proposition

service
upgrades

Society
social media
…

…
Supply chain
System
design

Others
regulations
standards
…

procurement
manufacturing
…

Technical disciplines

Application disciplines

mechanical eng.
electrical eng.
software eng.
…

domain (e.g., clinical)
human factors
…
22

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Commercial
sales
marketing
…

Team Activity – Discussion and reflection
What stakeholders do you/your architect speak to and how often?
• Reflect on current communication patterns.
• Who

• About what
• Why
• How often…

23

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Lunch

25

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Philips University

Business Context –
Process View

26

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Process model for Innovation to Market (I2M)
customer

customer viewpoint
RFD

Innovation to Market (I2M)
RI

RFA
PRC
SVAL
SVER

Time

27

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Process model for Innovation to Market (I2M)
customer

customer viewpoint
RFD

Innovation to Market (I2M)
RI

RFA
PRC
SVAL
SVER

Support, enable
component or platform creation

Support, enable
people, process and technology
28

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Process model for Innovation to Market (I2M)
customer
short-term
cashflow!
customer viewpoint
RFD

Innovation to Market (I2M)
RI

RFA
PRC
SVAL
SVER

component or platform creation

people, process and technology
29

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

long-term
assets

long-term
know how
(soft) assets

mid-term
cashflow!
Next year

Process model for Innovation to Market (I2M)
customer
short-term
cashflow!

Feedback

Strategy
customer viewpoint
RFD

Innovation to Market (I2M)
RI

RFA
PRC
SVAL
SVER

component or platform creation

people, process and technology
30

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

long-term
assets

long-term
know how
(soft) assets

mid-term
cashflow!
Next year

Architect role in the Process model
customer
short-term
cashflow!

Feedback

Strategy
customer viewpoint
RFD

Innovation to Market (I2M)
RI

RFA
PRC

Architect

SVAL
SVER

Support, enable
component or platform creation

Support, enable
people, process and technology
31

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

long-term
assets

long-term
know how
(soft) assets

mid-term
cashflow!
Next year

Architecture and Agile?
customer
short-term
cashflow!
customer viewpoint
Innovation to Market (I2M)

RFD

RI
RFA
PRC

mid-term
cashflow!
Next year

SVAL
SVER

Shorter

Replaceable
Easy

component or platform creation

people, process and technology

32

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

long-term
assets

long-term
know how
(soft) assets

Case selection

Sketch your
own case
&
Select

Divide the cases
among the groups

33

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Case will be used
for the remainder
of the training for
exercises

Team Activity – System of Interest (SoI)
Define the innovation that you will use in your case
Sketch the System-of-Interest and its immediate context
Annotate the sketch (e.g., main components, interfaces, functions, …)
Indicate related parts (products/services) with similarities
(portfolio of related products, planned product generations)

34

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Purpose of an
Architect
= Sustain Quality

36

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Viewpoint = Stakeholder + Concern
security
financial
manager

operator
ease of use

Differentiation

Cost of
ownership

sales
manager
Stake-holder

street price
concern
architect

balance
data model

integration

functions

timing
Project
leader

Fte’s

SW
engineer

problem

Adjustments

power
RF
engineer

tools

37

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

manufacturing
space

Viewpoint hopping

Cost of
ownership
Street
price

timing

functions

power

Financial
manager

sales
manager

project
leader
SW
engineer

RF
engineer

architect
integration

operator
security

operator
Ease of use

Fte’s
Sales
manager

space

Adjustments

Manufacturing

balance

Data model

SW
engineer

Differentiation

38

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

tools
Project
leader

manufac
turing

architect

Cost of
ownership

Financial
manager

RF
engineer

Architect: focus on most important issues
80%

Architecting time

20%

spent on

spent on

90%
10%
most
important
most
critical
issues

new

all other issues

solved

39

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Architect workflow
Principles

Recommendations

use feedback
work incremental
work evolutionary

translate into

time-box
iterate

make choices, be explicit
make issues tangible

quantify early
help to
achieve

measure and validate
multiple levels of abstraction

Objectives
support communication

(simple) mathematical models

facilitate reasoning

analysis of accuracy and credibility

support decision making

translate into

create understanding
maintain insight
overview

multi-view
system and its context
visualize

40

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Philips University

CAFCR+ Introduction

41

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Learning Goals
Become aware about and understand:
• How to use the CAFCR+ method as a framework for modeling
• The need for an integral and iterative approach

42

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

The CAFCR Model
Drives, justifies, needs
What does customer need
in product and Why
Customer
What

Customer
How

Product
What

Customer
objectives

Application

Functional

Product
How

Conceptual

Enables, supports, restricts

43

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Realization

The CAFCR Model: Example 1 – Car headlight cleaner
Product
How

Customer
What

Customer
How

Product
What

Customer
objectives

Application

Functional

Conceptual

Realization

With vehicle
standing still,
While driving
in traffic, on
highways,
Hot and cold
Weather.

Remove dirt
from headlight

wiper

Pump, switched
when spraying
window & light
on

Wants that more
light of the
headlights comes
on the road, no
hindrance from
dirt /clean
headlight when
dirty

Can be switched
on/off

Press button

Coating

pressure spray

44

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Tubing towards
nozzle, nozzle
hidden in
front-fender,…

The CAFCR Model: Example 2 – Underwater Photography
Product
How

Customer
What

Customer
How

Product
What

Customer
objectives

Application

Functional

Conceptual

Realization

Seal a phone in
a pouch, share
on social media

Sealed
transparent cover
with opening to
insert phone

Sealing
mechanism =
ziplock
No condensation
control
Single size

Knob for singleaction press
Start with a pipe
and seal one end

Waterproof
camera,
publish movie

Sealed camera
with buttonaccess

Sealing
mechanism =
gasket
Condensation
controlled via
temperature

Mould with
mounted PCB…
Location of
heating elements

Take photos
underwater and
publish them

45

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

The CAFCR Model: Example 3 – Radiology Search
Product
How

Customer
What

Customer
How

Product
What

Customer
objectives

Application

Functional

Conceptual

Realization

Progressive
filter-structure

Filter, code
configuration

Code-based,
synonym-assisted
algo
Multi-threaded
Standalone…

File-based
configuration
Tagged
documents in
local Solr instance
.Net GUI

Cloud-hosted, deidentified datalake
Microservices

Store word
embeddings
using Word2vec
NodeJS backend
Angular frontend

Result display
after each filter
action

Search Priors for
similar reports
Natural
language filter

Probabilistic
match and
display above a
threshold

46

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Integrating the views

What does customer need
in product and Why

Customer
What

Customer
How
Context
understanding

Customer
objectives

Product
What

Product
How

Intention

Objective
driven

Application

Functional

Conceptual

Opportunities

Constraint
awareness

47

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Knowledgebased

Realization

Recursive application of CAFCR
Know your customer and their customers, and know their objectives
Consumer

Drives

Enables

Customer’s
Customer
Business

Drives

Enables

Customer
Business

Drives

Enables

System
(producer)

Deeper into customer tree,
influence on architectural
decisions decreases

48

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

CAFCR+ Model – lifecycle view
What does customer need
in product and Why
Customer
What

Customer
How

Product
What

Customer
objectives

Application

Functional

Operations
Maintenance
Upgrades

Product
How

Conceptual

Lifecycle
Sales, service, logistics, R & D

49

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Realization
Development
Manufacturing
Installation

Exercises mapped on CAFCR+
Customer
objectives

Application

Functional

Conceptual

Realization

Life cycle

0. System-of-Interest
1. exploration of the playing field
2. SMART use cases
3. story telling
4. dynamic behavior
5. concept selection
6. customer key driver graph
7. Life Cycle
8. qualities, line of reasoning
9. Business Plan
10. Architecture Overview
50

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Philips University

CAFCR+ First Iteration – Exercises

51

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Introducing CAFCR exercises
Customer
objectives
•
•
•

Application

Functional

Conceptual

Realization

You will make a top down analysis of your product
Use time boxes of ~15 minutes per view
Show the most dominant decomposition of that view, as diagram or as a list: some more
guidance will be given per step

52

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Dos and Don’ts
Dos

Do not

Because

Start sketching/drawing as
soon as possible

Write long texts

Sketches stimulate sharing and
discussion

Use shared writing space

Immediately capture
electronic

Sharing and discussion help to
explore faster

Flow one discussion to the
next

Remembering is challenging

Annotate (add notes) during
discussion

Have nice but
volatile discussions

Information and insight are
quickly lost

Be open for ideas and
surprises

Do not stick to the
first solution

You hopefully discover a lot;
increased insight will change
problem and solution

53

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Team Activity: Customer objectives view; Value Network
CT scanner

Referring
physician
Regulatory

Hospital IS

Radiology

Insurance

Hospital
infra

Technician

Application
training

Use

Patient

Diag. Equipment

Suppliers

Components,
platforms, standards

54

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Make &
Commission

Ops & Service

Team Activity: Customer objectives view; Value Network
Radiology search

Use

CxO

Radiology
Hospital
infra

Application
training

Radiology Search
App
Platforms,
Runtime

Training,
test data

55

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Containers, Cloud

Make &
Commission

Devops

Team Activity – CAFCR – Customer View
Describe the “Customer Objectives” view of your system of interest.
= WHAT the Customer wants; WHO are the customer’s customers?
What is the context in which the system has to perform?

56

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Session Closing

58

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Review and Recap

Benefits and
Concerns

60

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals

Thank you
61

Confidential

Version 1.1

DAY 1 – System Architecting Fundamentals


# BLR May Structured Architecting DAY 3

> Converted from document `BLR May Structured Architecting DAY 3.pdf`

Philips University

Structured Architecting
DAY 3 – Systems
Architecting Fundamentals

May 2019

Philips University

Recap of day 1 and 2
•
•
•
•
•
•
•
•
•
•
•
•

Single and double loop learning model
Business context – stakeholders
Agile and Architecture
Role and task of the architect – the architect’s
profile
Defining scope – system of interest
CAFCR model
Customer view
Application view
Functional view
Qualities
Conceptual view
Realization view

2

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Security as example through all views
Trusted

Sensitive information
Selection
Classification
•
People
•
Information
Authentication
•
Badges
•
Passwords
Locks/walls

Not trusted

Customer
objectives

Guards
Administrators

Cryptography
Firewall
Security zones
Authentication
Registry
Logging

Functions for:
•
Administration
•
Authentication
•
Intrusion detection
•
Logging
Specific
•
Quantification
• Algorithms
• Interfaces

Application

Social contacts
Open passwords
blackmail
burglary
fraud
Unworkable procedures
Missing functionality
Wrong quantification

Functional

•
•
•
•

Libraries
Servers
Storage
Protocols

Conceptual

Desired
characteristics,
specifications,
and
mechanisms

Realization

Holes between concepts
Bugs
• Buffer overflow
• Non-encrypted storage
• Poor exception handling

3

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Threats

Plenary: Identify dominant qualities

http://iso25000.com/index.php/en/iso-25000-standards/iso-25010

4

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Smart Use Case
(Applied on Functional/
Black Box View)

6

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

SMART requirements

S
M
A
R
T

Specific

Quantified

Measurable

Verifiable

Achievable

t (Attainable, action-oriented, acceptable,
agreed-upon, accountable)

Realistic

(Relevant, result-oriented)

Time-bounded

(Timely, tangible, traceable)

7

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Quantified use case to define key performance
• Use case: Testing baby milk bottle teats
– For feeding teats and drinking
accessories, place the teat or
accessory on a cutting board of at
least 10 mm thickness and (70 ± 5)
Shore D hardness

Source: Child use and care articles - Drinking equipment - Part 1:
General and mechanical requirements and tests, EN 14350-1

8

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Quantified use case to define key performance
• Place the tip of the indenter centered
over, and at right angles to, the major axis
of the teat or accessory, in the region of
the waist or neck of the nipple of the teat
i.e., 15 mm to 20 mm from the tip of the
nipple or 15 mm to 20 mm from the end
of the accessory

Schematic test set up

Source: Child use and care articles - Drinking equipment - Part 1:
General and mechanical requirements and tests, EN 14350-1

9

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Quantified use case to define key performance
• PASS Criterion:
– When tested in accordance with tear
resistance test, no feeding teats which
punctures shall break, tear, or separate

Schematic Sample Indenter
Source: Child use and care articles - Drinking equipment - Part 1:
General and mechanical requirements and tests, EN 14350-1

10

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Team Activity – Smart Requirements – Functional View
Make specification overview with SMART Key Performance Parameters
(or functions or interfaces)
Determine at least one use case
interfaces

inputs

system seen as black box
functions
quantified characteristics

outputs

Restrictions, prerequisites,
boundaries, exceptions,
standards, regulations

Use case
Typical use with relevant contact data (quantified!)
11

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Customer views, and
customer key
driver graph

13

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Learning goals
Become aware and understand how to:
Apply key driver related methods and techniques to understand the customer
perspective to guide specification and design.

14

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Example Customer Key Driver Graph for Cardiac intervention

Customer key-drivers

Application key-drivers

Functionality

Focus on patient

Minimal system interface

• Predefined workflows
• Autopush to PACS

Quick response

• <1s response time
• 30o/s rotation speed

Avoid mistakes

No data entry

• WLM interface
• Sync patient across cathlab

Record decisions &
motivations

Reporting

• Derive report outline from
workflow
• Derive report content from
inventory

15

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Method to create customer key driver graph
Define the scope specification

In terms of stakeholder
or market segments

Extract facts from product specification;
Ask “why?” questions about
specifications of existing products

Acquire and analyze facts

Build a graph of relations between drivers and
requirements by brainstorming & discussions

In case requirements have multiple drivers
Discuss with customers &
Observe their reactions

Obtain feedback

Increased understanding often triggers
Moving drivers to requirements or vice
versa, and/or rephrasing

Iterate multiple times

17

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Recommendations for the definition of key drivers
Limit the number of key-drivers
Minimal 3, maximal 6
Don’t leave out the obvious key-drivers
For example, main function of the product
Use short names
Recognizable by the customer
Use market/customer-specific names,
No generic names
Do not worry about exact boundary
between customer objective and
application

18

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Create clear goal (relations)

Report Out/
Group Discussion

Philips University

Partitioning, interfacing, and
dynamic behavior

20

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Learning goals
Become aware and understand:
• design fundamentals as part of architectural reasoning
• partitioning, interface, behavior, and quantified performance design

21

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

How characteristics emerge from parts and dynamics
Characteristics
Prime system responsibility
Prime interest of customer

Results in
Dynamics
Functionality

Interact
Parts

22

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

24

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

GUI

NGUI

Application layer

FSC
Gen eral

FSC
Sys

FS
UIspecific

User
Calibration

Beam
Lim

Session
Mgt

Automation

SE
tool

Acquisitio
n

Upgrad e
tools

CWIS

QAUIGlue

FSC
Ser vAp ps

Papu

Reviewing

Application Library layer

IPISLib

XP host

FSC
UImodule

Embedded

Technical layer

Image
Detection

EPX

FSC
Generator

TSM
NT

UIDS

Collimator

Gen eration

TSM
WinCE

UICVEmb

Collimator

X-ray
Generator

Flashlite

DMT

Nicol

Velara

Flashlite

AEP
meter

Tube
cooling

FD

In general, the impact of IEC
3rd ed. must be investigated
for all Mechanical items.

Physio

Tube

chiller

Injector

VPC

LITE

Gen IO

Gen Serial

Seq uencer

MiscIO

XP Image
display
PC

XP image
IP PC

KVM
Switch

IP PC

Video
Switch

Color
monitor

Tools

Gen
Sink

Audit Trail

Infra
Field
service

Logging

PMS
Logging

ServiceFX

COM
support

UIIntLayer

Installa tion

Download

Transport
Layer

VxBasic
Mgr

PCI
driver

Infra
PCITL

BSP

CAHost

XP image
host

XDDS

Base

Database

Connecti-vity

Models &
Interfaces

FSF.NET

System
Services

FS
Abstraction

FSFW

FSMisc

HW key

FSFW
Utils

PandB
Pos

56"
Color
monitor

Scan
Converter

Geo me try

XP Ima ge
IPC

TC
AD5

TC
AD7

LCN

FSC
PLG

FSC
CLE

TC
AD5i

M
Cabinet

Patient
Support

Stand

R Cabinet

Host PC

MPDU

Ceiling
Susp. &
Monitor

Intercom

CRCB

SIBbox

Video
Wall
Con. Box

CR Video
Splitter

MCS Add
on Box

25

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

FSC
Geo CV

Gen Ca n

SIBbox

Gbe
switch

B&W
Monitor

Infra

FSC
Nt Pc

FSC
SIB

HW

Hardware
UIM

FlexVision
Switching

Infra PMS

Proscribe
XPe

Hardware
Infrastructure

FlexVision
Logging

Data
Model

EPXtool

FSC
ID

Arch
Network

Printing

Ris

FSC
IPIS

FSC
Coll

FSC
FlexVision

RealVNC

FSC
RIS

QA

FSC
EPX

Allu ra
Que stra
Age nt

Keyboard
mouse

Geo IPC,
no
SynqNet

Auxiliary
Room
Con. Box

FlexVision
PC

16x16
Matrix
Switch

MediaWall

HW tray

K/M
switch

B Cabinet

Pedestal

Infrastructure layer

User Interface
layer

TSMUI

subsystem

Legend

Partitioning guidelines
Part is cohesive
Functionality and technology belong together
Coupling with other parts is minimal

Minimize interfaces
The part is self-sustained for production
and qualification

Can be in conflict with cost/space requirements

Clear ownership of part
One department or supplier

26

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

What would you abstract?

27

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Philips University

Dynamic behavior

28

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Learning goals
Become aware and understand:
• dynamic behavior of components and their interaction
• how to use dynamic behavior as part of architectural reasoning
• the value of concept selection

29

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Dynamic behavior as a cartoon
1

2

Storage Bay

Position
the C-Arm

Get the CArm

4

3

Adjust for
Top view

Move out
of room

Button

6

7

8

Take Photo

Position for
side view

Adjust for
side view

Move out
of room

9

10

11

Photo available for
surgeon, surgery
in Progress

Move the C-Arm
to storage bay

5

Take Photo

30

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Storage Bay

12
C-Arm in
storage bay

Storage Bay

Dynamic behavior as work flow
Top View

Side view
5

1

Place patient
on table facing
up, C-Arm in
storage bay

Wheel machine from
storage bay to patient

Wheel machine into position
6

2

Place machine and do
settings (Aperture, fine
positioning)

Place machine, settings
(Aperture, fine positioning)

7

Move out of the room
8

Press Button take photo,
3

Move out of the room
4

9

Photos available for viewing
by surgeon
10

Press Button to take photo

31

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Surgery finished, wheel
machine to storage bay

Surgery
finished,
patient still on
table, wheel
C-Arm to
storage bay

Team activity – Dynamic behavior
Capture the dynamic behavior in terms of specification.
Create diagrams that capture dynamic behavior are among others:
• Functional flow of control/data
• Resource requirements & constraints

33

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Concept selection

35

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Concept selection (including flowchart)
Concept selection is picking the idea(s) which
best satisfy the needs.
In a design process, you make many
selections over time
Selection is an iterative process—
• May need new or modified concepts
• May need more info to proceed
Remember: You almost NEVER have
enough/proper information to do it...but
often you can’t wait

36

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Concept selection (including flowchart)
Collect relevant information

Number of concepts

1

Identify primary function(s)

2

Select key components for
primary function(s)

3

Select key components for
secondary functions/features

4

Create architecture scenarios

5

Ranking scenarios

6

Selection

Concept selection

37

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Example shavers - primary functions
Collect relevant information

1

Identify primary function(s)

2

Select key components for
primary function(s)

3

Select key components for
secondary functions/features

4

Create architecture scenarios

5

Ranking scenarios

6

Selection

The main function(s) of the appliance
can be derived from the commercial input.

Source: Peter Rijskamp, Senior System Architect Shaving

38

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Example shavers (contd.) – key components
Shaver example: Primary and secondary components
Collect relevant information

1

Identify primary function(s)

2

Select key components for
primary function(s)

3

Select key components for
secondary functions/features

4

Create architecture scenarios

5

Ranking scenarios

6

Primary:
Shaving system

Secondary:
Unit type

Primary:
Power-supply

Primary: Drive

Secondary:
Trimmer type,
integrated/click on

Secondary:
Integrated/
modular buildup

Secondary:
Compatibility
Secondary:
Charging interface

Selection

Not primary
function but has
effect on power
chain for
primary function
Secondary:
Trimmer element

Source: Peter Rijskamp, Senior System Architect Shaving

39

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Example shavers (contd.)
Collect relevant information

1

Identify primary function(s)

2

Select key components for
primary function(s)

3

Select key components for
secondary functions/features

4

Create architecture scenarios

5

Ranking scenarios

6

Selection
Source: Peter Rijskamp, Senior System Architect Shaving

43

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Example shavers (contd.)
Collect relevant information

1

Identify primary function(s)

2

Select key components for
primary function(s)

3

Select key components for
secondary functions/features

4

Create architecture scenarios

5

Ranking scenarios

6

Selection

FCP Lifetime Shaving Perf. Shaving minutes Design

Source: Peter Rijskamp, Senior System Architect Shaving

44

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Team activity – Concept selection
Make a decision matrix for one of the concept selected.
•
•
•
•

Define at least 2 concepts
Define criteria for selection
Eliminate / Modify
Score concepts against criteria, for
example, using a scale from 1 to 5 (1 =
very poor, 5 = very good)
• Recommend a concept with rationale

Concept 1

Concept 2

Concept 3

Criteria

1

3

5

Criteria

5

5

2
Best
because…

45

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Philips University

Platforms

47

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Learning goals
Become aware and understand about the:
• similarity across products and ways to use these similarities for overall
efficiency in development and supply chain
• ‘right level’ of reuse (component, function, module, etc.)

48

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Product in context of portfolio/generations
• Quite often, a product is part of a product family, or member of a
generation of products
• Use the same solutions for similar functionality:

Reduces
time to
quality
Saves
development
time and cost
Provides a uniform
user experience

Provides
economy
Provides a
better return on of scale
(manufacturing)
investments

49

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Provides
lower
operating cost
(e.g. SW updates,
spare parts, …)

Platform: serve single market with multiple products
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

Hair Removal

Satinelle Epilator

Conceptual

Shared Components

Epilator
Handle contains
the battery,
motor and
charging control
Shaver

SatinShave Prestige

Realization

51

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Handle +
Epilator head

Handle +
Shaver head

Platform advantages
CURRENT

ME

NEW

HE

Current Philips Ladyshave and
Epilators (Maxima, Arielle, Marlin)

Satinelle and SatinShave product lines based on
new platform

Savings versus current product line
New versus previous product line
SATINELLE (new epilator line)
SATINSHAVE (new ladyshave line)

fcp (€)
weighted average (ME, HE)
13.13
10.96

53

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Δfcp (€)
2.57
0.35

Volume (kUnits)

Saving (€)

2016

2017 -

2016

2017 -

600
380

700
470

1.5M
133k

1.8M
165k

Platform serving multiple, diverse markets
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

Music Streaming

Conceptual

Shared Components

Music
streaming

Streamium WiFi

Communication
compliant with
WiFi standard
Baby
monitoring

Baby monitor

Realization

54

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Music Device
+
WiFi
Baby
Monitor +
WiFi

Architectural approach – Platform approach

Customer requirements

Customer satisfaction
Integration and
validation

Systems

Integration and
verification

Subsystems

Modules/
Building blocks

platform

Components

Detailed design
55

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Integration and
verification
Integration and verification
Realization

Platform use and maintenance

Customer requirements

Customer satisfaction

Customer value
added diversity
dedicated people

Product development
Product creation process

Platform

Platform
Common building blocks,
technology, suppliers,
procedures, tools, …
(other) dedicated people

56

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Platform maintenance
For example:
• Include new technologies
• Decide on extensions, variation
• Processes needed to secure
cross-business decision
making in organization

Typical phases in product development
Where would platform strategy pay off (most)?

Uncertainty

Effort

Investment

Concept

Design

Engineering

• Reuse of
(Proven)
• Concepts
• Faster

• Less design
effort, risk

Industrialization

• Shorter time to
• Less
engineering, quality/yield
• Less tooling cost
existing
solutions

And how would this be for SW/Services?
57

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Ramp-up
• Faster
• Less risk

(Mass)
Production

Operation

• Less
• More
maintenance
commonality
• Less stock cost cost
• Better delivery (updates),
that is,
performance
connected
propositions

Transition from peaked design to platform
High product diversity drives consideration for platforms.

HIGH

DIVERSITY

I. Consider platform

II. Consider platform

1

LOW

4

III. Peaked design

IV. Peaked design
2

LOW

HIGH
SALES VOLUME

58

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals

Thank you
59

Confidential

Version 1.1

DAY 3 – Systems Architecting Fundamentals


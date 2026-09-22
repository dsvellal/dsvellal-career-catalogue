# BLR May Structured Architecting DAY 4

> Converted from document `BLR May Structured Architecting DAY 4.pdf`

Philips University

Structured Architecting
DAY 4 – Systems Architecting
Fundamentals

Sudeep Prasad
May 2019

Philips University

Recap of day 1, 2, and 3
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
•
•
•
•

Single and double loop learning model
Business context – stakeholders
Role and task of the architect –
the architect’s profile
Agile and conventional development
Defining scope – system of interest
CAFCR model
Qualities
T-shaped presentation
Story telling
SMART requirements
Customer view – Key driver graph
Partitioning, interfacing, and decoupling
Dynamic behavior
Concept selection
Platforms

2

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Concepts
• Apect of your system
• How have others done it?

3

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Report Out/
Group Discussion

Role of an Architect
Design gives you…

Architecture gives you…

➢

REST-API Façade for SOAP

➢

Contract-first, Communicate
E.g., use Swagger

➢

Extensible mapping rules

➢

Staging and evaluating before
deployment

➢

Monetizing the API

➢

Monitoring the API

➢

Testable interface

5

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Architect’s deliveries
Report

Specification

Report

Report

Spec

Report

Spec
Spec

6

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Design

Design
Design
Design

Architect’s Responsibilities and deliverables
Architect Responsibility:
Sustain Product Quality

Expenditure
Decomposition
Technology
Tools

Across Product variants
Across Product generations
Across the scale of usage

Communicate

₹

77
Version 1.1

$

€

Confidential

DAY 4 – Systems Architecting Fundamentals

Time

Types of Architecture Deliverables
Generating…

UML
BDD
Given the account is in credit
And the card is valid
And the dispenser has cash
When the customer requests
Then debit the account
Given secure connection
When debit request is made
Then invoke API to debit
And dispense cash
And return card

Architecture
document
Review and Approval

Request
Guard,
blogs…

88
Version 1.1

Confidential

DAY 4 – Systems Architecting Fundamentals

Enforcing…

Platforms and reuse require upfront planning
Vision on future
diversity and
flexibility
Platform

Reference
Architecture
B

Platform
Platform
C
C
’

C

A
D

Long term
roadmapping

C
C ’ ’ EE’
’C ’
A
B C ’ ’ E’E’ ’ E
BD C E ’E ’
A
A D E’ ’
D E’
B

1

E
1

C
’
’

C

Specified interface

Specified module

Interface guideline for further specification in platform

Module guideline for further specification in platform

9

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

More architecture deliverables
• Customer and lifecycle needs – what is needed
• System specification – what will be realized
• Design specification – how the system will be realized
• Verification specification – how the system will be verified
• Verification report – the result of the verification
• Feasibility report – the results of a feasibility study
• Roadmap

10

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Shared architect responsibilities
Responsibility

Primary owner

Business, plan, profit

Business manager

Schedule, resources

Project leader

Market, saleability

Marketing manager

Technology

Technology manager

Process, people

Line manager

Detailed designs

Engineers

11

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Architects are generalists with root (depth)
Breadth of knowledge

Depth of
knowledge

Specialist

Generalist

Root
knowledge

12

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Integrating many specialists…
Breadth of knowledge

Generalist

13

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Specialist

Specialist

Specialist

Specialist

Specialist

Depth of
knowledge

Specialist

Generalist

Intermediate profile eases architect role
Breadth of knowledge

All-round specialist

Depth of
knowledge

Specialist

Systems architect

Aspect architect

Root
knowledge
14

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Philips University

Life Cycle View

15

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Learning goals
Become aware and understand:
• how the lifecycle context relates to architecture reasoning
• the timing dimension of lifecycles

16

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Product related lifecycles

Individual systems
service
System
Production
System
sales
System
creation

Upgrades and options production
Upgrades and options sales

Upgrades and options creation

17

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

disposal

System lifecycle

using

local
changes, e.g.
accounts
procedures

Secondary
use

18

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

dispose

maintenance

upgrade

maintenance

using

add option

System
order

Lifecycle example: Philips 8000 series smart TV
2011

2013

Nov
2016

2017

Philips launches new Smart TV series
http://www.3dtvmagazine.nl/2011/03/philips-lanceert-nieuwe7000-8000-en-9000-3d-tv-series/

Philips sells lifestyle entertainment to Funai
http://www.philips.nl/aw/about/news/archive/standard/about/news/press/20130129persbericht-Philips-en-Funai.html

After complaints, Philips provides
Amazon Fire TV stick
https://tweakers.net/nieuws/118285/philips-geeft-klanten-die-smart-tvfuncties-verliezen-amazon-dongle.html

Still complaints, customer center does not know what to do
https://www.consumeraffairs.com/home_electronics/philips.html

19

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Now one year later: Feb 2018:
https://www.consumeraffairs.com/home_electronics/philips.html

20

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Lifecycle example
•
•

2010: Switched from ‘old’ FPGA+XP-PC-board to 3 XP-PCs
Last-time-buy of boards

•

2010 – 2014: Several SPs, PC-changes

•
•

Apr 2014: End of Win XP support
WES2009 release for main PC. But 1.5 day upgrade time
Other PCs remain on Win XP. Whitelisting for security.

•

2016: End of OEM agreement to ship Win XP →Cannot produce
No PCs available that can run Win XP →Cannot repair
Win7 release for PC-based systems. But extra RAM and license costs

•
•
•

Jan 2019: End of WES2009 support →Cannot service
Jan 2020: End of Win7 support →Cannot service, cannot sell
Win10 release for PC-based systems

21

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Plenary – Life Cycle View
Analyze the evolution during the lifecycle.
• Identify sources of change in customer context, life cycle context, and
technology.
• Determine the expected rate of change (per change) and the required
response time to change.

22

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Plenary/
Report out

Philips University

Simple financial computations for
system architects

24

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Learning goals
Become aware and understand the financial impact of specification and
design choices.

25

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Product margin: Sales price - Cost

Retailer margin
and costs
Margin per product
(The margin over the sales volume must
cover the fixed costs and generate profit)

Margin

Transportation, insurance,
royalties per product, …

Miscellaneous
Street
price

Sales
price

Labor

Material

Cost
price

Cost per product
(excluding fixed costs)
Purchase price of components may cover
development cost of supplier

26

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Cost price – Philips example
Market sales price (going price)

VAT (%)

Retail margin ( ~50 % going price)

Discounts (%)

Net-Net Sales Price

Sellex

IGM
(30 60%)

CoGS

R&D
G&A
Other Expenses
EBIT (12-15%)
Other CoGS
Import duties (%)
Freight & insurance cost
Tooling cost /depreciation
Manufacturing Overhead+ profit
Man-machine

FSP
BOM
27

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Cost of the R&D organization

EBIT = Profit or loss
Can be influenced by design

Profit as function of sales volume
$

income

profit

expenses

variable
fixed
costs
Sales volume in units

Break even point
Expected sales volume
28

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Investments, more than R&D
Financing

Business dependent:
pharmaceutics industry: Sales cost >> R&D cost

Marketing, sales
Training sales and service

NRE: outsourcing, royalties

Strategic choice: NRE or per product

Including: staff, training, tools,
housing materials, prototypes
overhead certification
Research and development

Often a standard staffing rate is used
that covers most costs above
R&D investment = effort * rate
29

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Income, more than product sales only
Other recurring
income
Services

Options, accessories

Products

License fees
pay per movie

Income service
Services

Sales priceoption * Volume option
Options

Sales priceproduct * Volume product

30

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Content, portal
updates
maintenance

Cash flow: The Time Dimension
Q1

Q2

Q3

Q4

Q1

Q2

Q3

100k$

400k$

500k$

100k$

100k$

60k$

20k$r

Sales volume (units)

-

-

2

10

20

30

30

Material & labour costs

-

-

40k$

200k$

400k$

600k$

600k$

Income

-

-

100k$

500k$

1000k$

1500k$

1500k$

Quarter profit (loss)

(100k$)

(400k$)

(440k$)

200k$

500k$

840k$

880k$

Cumulative profit

(100k$)

(500k$)

(940k$)

(740k$)

(240k$)

600k$

1480k$

Investments

Variable cost = Sales volume * Cost price / unit
Income = Sales volume * Sales price / unit
Quarter profit = Income - (Investments + Variable costs )

Cost price / unit = 20k$
Sales price / unit = 50k$

31

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

The “Hockey” Stick
Profit

1M$

0.5M$

time
(0.5M$)

(1M$)
loss
32

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

The “Hockey” Stick
What if …?
Profit

early more expensive
product + follow-on
delay of 3 months
original model

1M$

0.5M$

time
(0.5M$)
(1M$)
loss
33

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Stacking multiple developments
9

cumulative 1

8

cumulative 2

7

cumulative 3
cumulative 4

6

cumulative total

5
4
3
2
1
0
1

2

3

4

5

6

7

8

9

10

-1
-2

34

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

11

12 13

14

Fashionable financial yardsticks
Return on Investments (ROI)
Net present value

Lower investments provides higher ROI
A future value calculated back to a value today

Return on Net Assets (RONA)
Turnover/FTE

Leasing reduces assets, improves RONA

Outsourcing reduces headcount, improves
this ratio

Market ranking (share, growth)
Only numbers 1, 2, and 3 will be profitable
R&D investments/sales

In high tech segments 10% or more

Cash-flow

Combining profits with negative cash-flow,
risk of bankruptcy

35

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Net Present Value (NPV)
The value of something in the future, calculated back to a value of today.
Assume we invest 100 k€, have 10% interest per year, and re-invest the interest…
Than we have almost doubled our investment after 7 years.

Year 1

Year 4

Year 7

100

110

121

133

146

161

177

100

110

121

133

146

161

177

Time

But when we have to borrow money, our debt doubles as well

36

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

195

195

The power of NPV for architectural decisions
NPV calculation helps decide whether investing 100 k€ now to earn 150 k€ 5 years from now, is a
wise decision.
or
• Assess consequences of delayed market entry (excluding impact on sales)

150

93
77

150

Time

100

Year 0

Year 5

Year 7

• The effect of earlier return on investment.
150

113

Time
100

Year 0

Year 3

37

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Being cost efficient — Focus during development
Focus on optimal
solutions and cost
reduction

Sales volume

Focus on speed and fast
learning at minimum
investment
Focus:
Learn from 3rd
party or Q&D

Validate
requirements and
market introduction

Conquer market
and ramp up

1st

1st
gen1st
st
1
gen
gen

gen

Second
gen. own
solution

1st generation:
‘Quick & dirty’
solutions for
requirement
Exploration

Second generation: focus
on improved proposition
& low development
effort/cost/risk

Small scale trials,
E2E development

Validate requirements,
trials, be on the market,
maturing E2E proposition

Volume
production

Market size

Optimized
Optimized
solution(s)
Optimized
solution(s)
solution(s)

Ensure profitability
More focus on BoM, but incl.
development investment!

Third own
solution
Third
gen.
solution

Start making profit!
Focus on low development investment
Third generation:
incorporate
learnings,
optimize product

Focus on value
& cost down of
portfolio
Gain volume and
profitability

Conquer
market share

38

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Time

Report Out/
Group Discussion

Philips University

Roadmap

40

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

The link between product architecture and roadmapping
Architecture as a key
enabler to:
•
•
•
•

Innovation
differentiation module

Follow the market
evolution
Create diversity
Drive technology
evolution
Link innovation

B1

Optional
module

B2

Diversity module
D1 D2 D3

C*

A

B

Product
architecture

C*

D

E

F

Supplier module
F

Costs reduction module

Technology options

Technology options

41

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

E*

E**

The link between product architecture and roadmapping
A2

B3

C

D4

Product roadmap
F2
A1
/2
A1

B2

C

D1

E*

F4

B1 D1

C*

F4

Time

Building block roadmap

F1

B1

F2

F3

D1

D3

Q2

Q3

Phase out F3

F3

D4

F5 Introduction of 2 new variants F4 and F5
Same functionality / facelift version

D4 and B1 integrated

B2

Additional variant B3

C
A1

F4

Q4

Q3

Q2

Q1

Q4

B3

D4

phase out D4

B1

Same functionality / smaller and lighter version
A2

C*

A1/
Functionality A1 and A2 2
combined in one new
common building block
E*

E

Initial building blocks

D2*

D1*

D4

Q2

Same functionality /
cost reduced version
Q3
Q1
Q4
Technology roadmap

42

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

E** Same functionality /
new supplier
Q2

Q3

Q4

Time

Philips University

Consolidating the
learnings

43

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Final Team activity
For your case:
• List the business & customer drivers
• Determine key drivers for the
architecture
• Determine where the architecture is
sensitive to changes, e.g., technology,
shift of user requirements, etc.
(sensitivity points)
• Determine the trade-offs to be made
• Determine the risks (feasibility, business
case, timely-ness, etc.)

Customer Drivers

Use T-shaped presentation for
the recommendation to management.

Sensitivity
Points

44

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Business Drivers

Key Architecture Drivers

Architecture Description

Trade-off
Points

Architecture
Risks

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
45

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

4

Report Out/
Group Discussion

Philips Architecture Community (PAC)
https://share-intra.philips.com/sites/STS20130705153001/SitePages/Home.aspx

47

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals

Thank you
48

Confidential

Version 1.1

DAY 4 – Systems Architecting Fundamentals


# 2023 State of Craftsmanship

> Converted from document `2023 State of Craftsmanship.pdf`

State of Software Craftsmanship 2023
2023 State of Craftsmanship |Software Excellence

Innovation Excellence (IEX)
Software Excellence

1

Table of contents
Introduction
Executive summary
Key findings
Key recommendations

3
3
4
5

Report details

7

Maturity of Software Craftsmanship practices
1. Testing Practices
2. Unit Testing
3. Functional Testing
4. CI/CD
5. Static Analysis
6. Code Review
7. Technical Debt Management

7
8
10
11
12
14
15

Data Backed Trends in Software Development Practices
1. Market & Regulatory
2. Development Process
3. Technology
4. Databases
5. Source Code Management (SCM)
6. CI/CD
7. Operating Systems and Hardware Profile

16
16
17
18
19
19
20

Final thoughts

21

Authors & Reviewers

22

2023 State of Craftsmanship |Software Excellence

2

Introduction
Since 2017, Software Excellence has empowered development teams, maturing their software
development practices.
The Software Craftsmanship Program engaged over 80% of Philips software colleagues, driving
teams toward excellence. The facts and conclusions presented in this report are based on 2023
data gathered from leaders of 138 projects during their journey into the program through the
year.
Apart from the software practices data collected, a project information questionnaire (PIQ) was
sent to each project team to gather data for analysis. This PIQ covered market, process, and
technology information. This report incorporates data collected from 77 respondents of the PIQ.
The State of Craftsmanship in software development and delivery practices intends to guide
leaders & practitioners in prioritizing efforts to reach excellence.

Executive summary
The Software Craftsmanship Program has helped business to improve software practices and to
identify risk in assets. An analysis of software related CAPAs (Corrective and Preventive Action)
from 2021 and 2023 correlated low maturity in software practices with higher probability of
product fault occurrences.
This report summarizes data representing over 80% of Philips' software community. It shows the
program was successful in raising overall software practices maturity and obtaining significant
progress in essential practices like static code analysis, code review and continuous integration.
However, challenges remain in testing, technical debt management and automation.
The report advises strategically prioritizing actions and investments based on identified
opportunities for leaders and practitioners. The Software Excellence team has programs and
expertise to help tailor those opportunities to each business context, overcoming challenges and
optimizing outcomes.

2023 State of Craftsmanship |Software Excellence

3

Key findings
1. Testing – only the engineers of 5.9% of
projects are fully versed in testing
techniques. 37 of 127 (29.1%) projects cover
more than 75% of NFRs (Non-Functional
Requirements). 94.1% of teams still do
manual testing (at least for some
requirements).

2. Technical Debt Management – 85 of 135
(66%) projects have not defined a
process/backlog to handle their tech debt.
The average time to pay back the incurred
tech debt is over six months.
3. DevOps effectiveness – 128 of 136
projects (94.2%) have a defined continuous
integration process. However only 29.4%
have automation to deploy software in the
test environment.
4. Code Analysis – 129 of 135 projects
(95.6%) have static code analysis checks
incorporated in their code. 85 of 108
projects (78.7%) have dynamic code analysis
techniques incorporated in their software
development & deployment processes.
5. Philips is a polyglot programming
language company – C/C++, C#, Java,
Python, and JavaScript dominate the code
base.
6. There is a big internal market for software
– almost half of the teams develop software
for internal customers.

2023 State of Craftsmanship |Software Excellence

4

Key Recommendations
This section distills the key recommendations
detailed throughout the report. We hope
those recommendations can help business
leaders and practitioners while planning
invest in and prioritize areas that cultivate
code quality, accelerate delivery, and meet
exceptional customer experience. While we
list the summary of insights here, the
subsequent sections of the document bring
detailed information and insights.
1. Confidence Through Code: Crafting a
Culture of Testability and Automated
Feedback
• Investing in training engineers to write
testable code and tests; to have a holistic
view of tests leads them to optimize
software quality and to have confidence in
test stack, enabling code refactoring and
improvements.
• Prioritizing fast-feedback tests for early
and frequent validation of code
functionality. Unit tests offer bounded
context for testing, this means all flow
paths the code takes can be effectively
tested using unit-tests, which may not be
possible with functional/system testing.
Adopt a testing pyramid approach for fast
feedback on code behavior.
• While test coverage is an important
metric, focusing on the correctness and

comprehensiveness of tests yields
accurate validation that further enhances
product quality and integrity.
• Write precise and testable Non-Functional
Requirements
(NFRs)
for
your
product/solution.
• If the environments permit, automating
test execution not on a scheduled basis
(daily, weekly, fortnightly, etc.) but on
frequent triggers like commits, merges,
and pull requests provides opportunities
to identify breaking changes and fix them
early.
2. Continuous
Quality
Champions:
Monitoring, Feedback, and Optimization for
Flawless Software Development
• Define meaningful metrics and thresholds
that any team member can understand
and can be used to monitor quality
continuously.
• Prioritize early feedback to developers for
faster issue resolution (e.g., at
development time). Integrate real-time
quality
feedback
throughout
the
development cycle, making quality a
seamless part of the coding journey.
• Automate checks with thresholds at
appropriate intervals. Some phases to
consider checking for quality include

2023 State of Craftsmanship |Software Excellence

5

quality at a desk, pre-commit, commit,
pull-request,
merge,
continuous
integration,
continuous
delivery,
continuous deployment checks, postdeployment checks, and post-deployment
continuous monitoring.
• Train engineers to decipher the quality
clues hidden in code analysis data and ask
the right questions behind issues,
transforming them into software
guardians / champions.
3. Shifting Left: Empowering Developers
and Streamlining Code Reviews
• Optimizing workflows: Train developers
on best practices for effective reviews and
improve team processes to ensure timely
responses and actionable feedback.

policies, and a culture of proactive
maintenance to combat software rot and
obsolescence.
Consider
rewarding
developers that proactively pay legacy
technical debt.
• Take advantage of context-specific
workshops offered by Software Excellence
to upskill engineers and leaders in modern
methods of software development &
delivery.
• Focus on continuous deployment
processes, dependency management, pull
request management, and code merge
management to optimize development
and delivery speed.

• Shifting left: Encourage continuous
improvement by analyzing and discussing
review data (review of reviews). Identify
repetitive occurrences and automate
whenever possible, allowing developers to
focus on higher-level code concerns.
4. Build for Tomorrow: Combat Software
Rot with Continuous Maintenance and
Modern Practices
• Define a process to list, prioritize and pay
identified technical debt. Do not let
technical debt accumulate; address it as it
occurs through automation, strict team

2023 State of Craftsmanship |Software Excellence

6

Report details
We dive deep into the data and analysis in this section. This section is the basis of the Key
Recommendations section in the document. This section is divided into two types of data:
• Maturity of Software Craftsmanship practices.
• Data-backed trends in software development practices

Maturity of software craftmanship practices
The Software Craftsmanship Framework
measures the maturity of Software
Craftsmanship to encompass industry trends
and relevant practices. Products relying on
software developed with best practices are
associated with better reviews and higher
rates, mostly because the outcome tends to
present superior quality. This report
analyzes 7 core practices adopted by all
projects enrolled in the program. These are:
1. Testing practices
2. Unit testing
3. Functional testing
4. Continuous Integration (CI) & Continuous
Delivery (CD)
5. Static Code Analysis
6. Code Review
7. Technical Debt management
Let us look at each of these practices in
detail.

1. Testing practices
Mark of an excellent quality software
product/solution is guaranteeing the non-

functional requirements (NFR) of the
software.

Percentage of NFR coverage by tests
127 out of 135 projects submitted data for
testing practices from which the figure is
derived. The X-axis determines the no. of
projects, and the Y-axis defines the % of NFR
coverage they have.
As showed in the figure, we found 37% of the
teams stated that they don't measure how
many NFRs of their product/solution are
tested/checked, 27.4% of the teams
indicated that they have over 75% test
coverage on their NFRs, and 7.4% of the
teams have up to 50% NFRs covered by tests.

2023 State of Craftsmanship |Software Excellence

7

Those numbers indicate there is a big
opportunity associated with quality
attributes assurance, guaranteeing Philips
products meets what customers expect.
The Software Craftmanship program
recommends
a
fast-feedback
tests
approach. Leveraging the test pyramid is one
of the ways of doing this. The idea is to
obtain early feedback indicating that the
code written does what it intends, which can
be checked upon any changes made to the
software. We found 73.2% (93 out of 127) of
teams pursue the test pyramid strategy,
indicating there is still a relevant contingent
of projects to be trained/coached.

Recommendations
• To ensure quality with speed, the Software
Excellence team highly recommends that
leaders and practitioners focus on writing
the right NFRs for their software
product/solution
and
have
these
requirements asserted through automated
tests that can run in a suitable productionlike environment. These tests guarantee the
quality attributes of the product/solution are
met.
• Leaders and practitioners should look at
investing effort in training engineers to have
a holistic view of testing and domain testing
techniques, therefore being able to improve
testing practices in their software
development processes.

The 2023 Software Craftmanship framework
collects unit, integration, functional, and
smoke testing data. In the subsequent
sections of the document, we will analyze
unit testing and functional testing due to
their importance and prevalence in the
testing process.

2. Unit testing
135 projects made form submissions for this
practice.
When done correctly, unit testing is a costeffective and fast check against deviation
from the required behavior of the code. This
can help assert functional and nonfunctional requirements in an automated
manner that assures the quality and stability
of the tested functionality. Unit tests can
help to address the problem that the
complete behavior of a full product is
typically far too complex to exhaustively
specify or test, leading to quality issues in a
pure ‘system testing’ based approach.
However, the success of unit tests relies on
engineers' skills. From our data, we noted
that only 5.9% of teams in Philips have
engineers fully versed in unit testing
techniques.
17.2% of project engineers practice Test
Driven Development (TDD). TDD results in
better
quality.
Behavior
Driven
Development (BDD) is a team methodology
that can be considered by highly functional

2023 State of Craftsmanship |Software Excellence

8

development teams as a technique to
increase
effectiveness
of
tests.
Understanding TDD v/s BDD is important
and this article helps here. Unit testing
practices that promote quality with speed
that are still not popular in Philips projects
include mutation testing (4.4%), fuzzing
(8.1%), and property-based testing (18.5%).
Approaches to Unit Testing in Philips

Recommendation
Leaders and practitioners should focus on
training and coaching engineers in writing
code that can be easily tested and in the
different techniques of unit test case writing
to ensure that the product code is tested
appropriately for its functionality.

Recommendation
Leverage Software Excellence to conduct
context-specific workshops and bootcamps
on unit testing & refactoring the code to
make it unit-testable.

3 out of 135 projects (2.2% of respondents)
do not write unit tests, mostly developing
embedded software. We encourage
embedded software teams with low
maturity in unit testing to reach us and make
a joint improvement plan to get the best of
this valuable practice.
EMR (Electronic Medical Records) and
Cardiology business units in Brazil and India
are examples of teams that have invested
efforts into upskilling their engineers in
writing clean code and good unit tests, with
the help of the Software Excellence team.

Overall average unit testing coverage

2023 State of Craftsmanship |Software Excellence

9

gravitate towards writing functional tests
over unit tests. Common behavior noticed in
Philips’ teams is to start with manual
execution of functional tests and then
gradually progress towards automated
functional testing.

New code average unit testing coverage

Code coverage has improved over the years,
with the mean overall coverage being 69.2%,
and the average broad coverage for new
code is 79.5%.

NOTE: Leaders & practitioners must
understand that greater code coverage in
unit tests does not necessarily translate to
better code quality. Requirements
coverage AND the correctness of unit tests
are essential to assert the code's right
functional and non-functional behaviors. It
is also important to automate the execution
frequency of these unit tests based on
triggers like commit to code, merge of code,
upon pull requests, releases, and versions,
among others.

3. Functional testing
Functional testing is the most common type
of testing seen in Philips. Teams often

Percentage of functional requirements
covered by tests.

Percent of requirements covered by manual
tests.
With 126 projects answering this specific
question, 34.9% of team leaders stated that
projects cover more than 75% of functional
requirements.

2023 State of Craftsmanship |Software Excellence

10

Regarding automation, we found 103 teams
still doing manual testing and 31 relying on
manual tests to check all requirements. On
average, 58.7% of functional requirements
are
covered
by
manual
testing.

Recommendation
In functional testing and functional test
coverage, there is still a significant test
automation gap that needs attention &
work, resulting in faster feedback, and a
shorter time to market. For the practitioners
& leaders, this is a significant area of
investment and opportunity to tap into.

4. CI/CD
For this practice, form submissions were
made by 136 projects.

Recommendation
The engineering teams need to understand
why a particular process is adopted in our
team, why a specific tool is used to check the
quality, what quality parameters are
essential for our team, and how those
parameters affect the quality of our
software product/solutions. This will result
in a healthy debate about what tools to use,
what parameters to observe, and how to
protect
the
quality
of
our
products/solutions from degradation by
continuously scanning and monitoring the
parameters.
A fifth of teams do not use a version control
system (SCM) for changes in the pipelines,
and most teams do not have Continuous
Delivery (CD) to the test environment
(70.6%).

95.8% of projects have continuous
integration practices, allowing them to test
their code continuously against some
safety/quality checks. 43.1% of teams rely
on a separate DevOps team to manage the
CI/CD process.
Due to the silos of responsibility between
the development team, the testing team,
and the DevOps team, handover delays
become significant, and they affect the
delivery speed. We can break silos and
advance DevOps culture in Philips to
eliminate process handovers that delay new
releases.

Pipeline Management

Dependencies can often be the source of
software vulnerabilities. Regular updates
allow the project to use performance, bug

2023 State of Craftsmanship |Software Excellence

11

fixes, and new features. Data shows that a
third of the teams still need a strategy or
plan for updating dependencies.

Dependency Updates
Regarding merging new code and fixes in the
main software branch, 48.2% of teams take
over a day, with 21.7% taking over five days
to complete the task. 69.2% of teams spend
up to 25% of pull request time in “waiting for
rework” state (after issues being identified in
a static analysis or code review).

Recommendations
Directional areas for leaders & practitioners
to focus here include:
1. Continuous deployment process – what
steps are involved in deploying our build to a
customer environment, and how can this be
automated?
2. Dependency management – are we using
a vulnerable third-party library? Do we know
entirely what our dependencies are? Are we
keeping all our dependencies up to date?
Having systemic answers to these questions
will prove valuable in keeping the product up

to date & protecting it from third-party
vulnerabilities.
3. Pull request management – are we
effectively conducting a pull request and
review process within the team? What is the
lead time to close a pull request? How often
are changes requested in the pull request,
and how many can be statically checked?
Thinking about these questions helps
optimize the pull request and review process.
4. Code merge management – identifying
opportunities to merge code efficiently really
helps in creating faster development &
delivery of our products to our customers.

5. Static Analysis
Static analysis (SA) has received focus and
investment over the years. SonarQube,
Fortify, Black Duck, Coverity, TICS, and Code
Scene, among others, are popular static code
analyzers that are prevalent in the
organization.
Our data shows that 95.6% of teams
engaged in our programs use static code
analysis tools while checking product code.
60.7% of teams apply SA to test code, 32.6%
apply SA to infrastructure as code (IaC), and
only 8.1% use SA for documentation.
72.6% of teams answered they do some
static analysis at a desk, and 47.4% execute
the same SA checks they run in their CI
process.

2023 State of Craftsmanship |Software Excellence

12

33.3% of enrolled teams actively managed
their technical debt detected by SA.
32.6% of teams do not use gates to enforce
rules checked during SA.

Average of code base covered by static
analysis.

Recommendations
For leaders & practitioners to achieve
quality with speed, consider the following:
1. Leveraging static code analysis for its
strength: engineers need to understand
what data points can be observed by static
code analysis tools and how they help
protect the quality of their software. It is ok
to have multiple static code analysis tools
if it is relevant. Understanding what
parameters to observe and leveraging the
right tools to measure them is essential in
maintaining the quality of the product.
Automating the checks of these
parameters at appropriate intervals is also
necessary to continuously measure and
monitor these parameters.

2. Shift left checks whenever possible: the
faster feedback is given to the engineer,
the faster it can be fixed. Imagine if the
engineer is given feedback as and when
they are developing the code. Wouldn’t it
be easy for them to fix it right then? This is
part of “Developer Experience.” Enabling
appropriate feedback about code quality
as early in the development cycle as
possible is critical for maintaining excellent
software quality. There are many ways to
do this, including investing in a good
machine for the developers to work on.
Please leverage the Software Excellence
team to discuss “Developer experience”
and “Shift left” principles and their
relevance to your team.
3. Gates are our friends: often, it is not just
enough to have SA tools to observe the
code and dump results, but it is also
essential to stop the code quality from
degrading. This is where gates come into
the picture. Having the right tools to
observe the correct quality parameters and
having thresholds for these parameters
continuously monitored helps us identify
any deviation from code quality at its
earliest and empowers the engineer to
make necessary changes to uphold the
quality parameters relevant to the team.
These thresholds can often be automated
and measured, and appropriate alarms can
be raised by integrating them into the CI

2023 State of Craftsmanship |Software Excellence

13

and CD checks. Paying close attention to
our SA gates is essential.
Addressing tech debt as it occurs is
important: Just because we have tools to
measure technical debt does not mean we
should address it as we incur it. Often
because of delivery pressures, technical
debt never gets addressed, and it
accumulates over time, compromising the
quality and speed of software development
and delivery. Managing technical debt
through automation and strict team
policies and culture is essential. It is a
widespread practice that anything that can
be automated should be automated, and
manual processes and efforts must be
reserved only for activities that add value
to the team.

6. Code Review
Code review (CR) is a practice popularized in
the software industry and advocated by
Software Excellence since its inception.
We found that 92.6% of teams in our
program follow a mandatory code review
process for every change in the code. Code
reviews can be bypassed in 7.4% of the
project teams.
Having a code review checklist guarantees
consistency of code reviews. One highlight is
that most teams use checklists, but only
19.4% established them as mandatory. Nonfunctional requirements are another

relevant aspect of code review addressed by
only 54.1% of the team’s CR checklists
engaged
in
the
program.

Checklist for code review process

Despite a formal process, pair programming
is the most effective and fastest code review.
Data shows that developers are having
opportunities to work in pairs. However,
managers are vital to stimulating and
facilitating these necessary code review
awareness sessions for development
leaders.

Recommendation
To develop & deliver code with quality, it is
essential to know how teams deal with
checklists and how developers address the
main concerns during the code review.
There is an opportunity to train developers
better and to improve code review
processes in the teams, especially in related
KPIs (Key Performance Indicators), review of
review meetings, and analytics over CR

2023 State of Craftsmanship |Software Excellence

14

data. With insights extracted from those
activities, the team can act to shift left what
can be detected by automation or can be
improved with training, making room to
include in the checklist only complex and
abstract concerns that should be addressed
by engineers.
Process for managing technical debt.

7. Technical Debt Management
Technical debt refers to the consequences of
taking shortcuts or making suboptimal
decisions during development. If technical
debt accumulates over time and is
addressed, it can help the software's
performance, maintainability, and overall
quality, eventually leading to obsolescence.
Managing technical debt is essential to keep
a software asset healthy. In the Software
Craftmanship Program, we stress the formal
training process to guarantee teams can
manage tech debt over the software
lifecycle.
We found that 34.8% of teams have
implemented a complete process to deal
with technical debt. 55.3% manage findings
from Static Analysis tools; a small but
relevant percentage of 9.8% still needs an
established process.
3.7% of our projects take more than six
months to address accumulated tech debt,
and about 28.9% of projects do not measure
the time taken to repay tech debt.

Time to repay technical debt.

Recommendation
Your team needs to have a defined process
to handle technical debt once it is
identified. You can also address software
rot and obsolescence by implementing
technical debt management through
automation and tools. The key is to
measure what is important and
continuously monitor the parameters
through automation and CI processes.

2023 State of Craftsmanship |Software Excellence

15

Data-backed trends in software development practices
In this section, we cover trends of data seen
in the 69 Project Information Questionnaire
(PIQ) we received from business leaders.
This section covers the following areas:

(Food and Drug Administration (USA)) class II
and 13.8% being in FDA class I.

1. Market & Regulatory
2. Development Process
3. Technology
4. Database
5. Source Code Management
6. CICD solutions
7. Operating Systems and Hardware Profile
Let us dive deep into each of these sections.

Product target public

2. Development process
1. Market & regulatory
Almost half of the respondents (46.5%) were
working on projects aimed at the internal
market. This fact highlights the importance
of enabler teams in creating products,
precisely when complex technology is
involved. Another relevant fact about
enabler teams is the small size (6 to 20
professionals), in contrast with teams
developing for external customers, which
are usually bigger (most of them have from
21 to 50 professionals).
Of the projects targeting the open market,
almost 78.8% develop products classified as
medical devices, with 75.9% being in FDA

After the effort to adopt Scrum and Kanban
in Philips over the last years, 83.8% of teams
are now constructing software through the
agile process (Scrum or Kanban). 14.7% of
the teams use iterative/incremental or
waterfall processes.

Development process

2023 State of Craftsmanship |Software Excellence

16

3. Technology
General note about this section. In PIQ,
leaders could select multiple options for
answering these questions. The graph's
numbers reflect the choices leaders make
when answering these questions.
Philips software projects have different
architectures that involve a combination of
heterogeneous
assets.
Besides
the
traditional embedded software, there is a
growing usage of backends as part of the
primary or complementary product
functionality (data collection, for example).
Web applications are also preferred over
rich clients when no strict requirements
apply, with significant relevance in Philips
products. Mobile applications are also worth
mentioning,
primarily
to
deliver
complementary functionality for end users.

the usage of C#, Java, and JavaScript. Here, it
is important for us, as an organization, to
think about memory-safe programming
languages. Memory-safe languages avoid
whole classes of common software defects
whilst preserving the performance and
expressiveness of C and C++, therefore the
software industry is beginning to consider
alternatives to C and C++. The advantages of
considering memory-safe languages are
written well in this article. Leverage
Software Excellence to have a conversation
with us to see how you can consider memory
safe programming languages and why.

Programming language

Software profile
In terms of programming languages, C and
C++ are traditionally used in Philips products.
The prevalence of backends and the
emergence of web applications leveraged

The same variety can be found in
frameworks, building tools, and IDEs
(Integrated Development Environment),
with the Microsoft Visual Studio IDEs family
being the company's most used ones.

2023 State of Craftsmanship |Software Excellence

17

Frameworks

IDEs/editors

4. Databases
In databases, there is a diversity of types and
technologies. SQL databases are dominant,
but NoSQL options are being adopted in
different BUs (Business Units). There is also
a tendency to favor open-source options
(with support contracts) over proprietary
databases. Despite the observed tendency,
MS SQL Server and Oracle are core
components in many Philips products.
Build tools

Databases

2023 State of Craftsmanship |Software Excellence

18

5. Source Code Management (SCM)

6. CI/CD Solutions

Data shows a gradual adoption of Git-type
SCM systems in the company. Azure DevOps
and GitHub, both managed by Microsoft, are
dominant.

Azure DevOps is the most used CI/CD
platform, followed by GitHub. A positive
development highlighted in the survey
pertains to the incremental embrace of
Infrastructure as Code (IaC). Terraform
emerges as the predominant tool, aligning
with prevailing practices within the IT
(Information Technology) industry and
recommendations from the Fiesta project.

Source Code Management tools

Continuous Integration tools

Infrastructure as Code tools

2023 State of Craftsmanship |Software Excellence

19

7. Operating Systems and Hardware
Profile
Windows server is still the preferred OS
(Operating System), and the environment
Philips products rely on.
The dominant hardware profile is x86.
Virtualization is a tendency, mainly when
software is distributed and accessed through
a network. Philips also has many projects
relying on ARM and microcontrollers, which
demand specific testing environments and
strategies.

Hardware platforms

Operating Systems

2023 State of Craftsmanship |Software Excellence

20

Final thoughts
Throughout the report, we made recommendations that can guide leaders and practitioners in
the planning of actions and investments. More could be said if we had analyzed all 20 practices
currently included in the Software Craftsmanship framework.
Speed with quality can be achieved when it comes to software development. We want leaders
and practitioners to understand that when we focus on the areas listed in this report, we inch
closer to delivering quality software with less time to market. Proper outcomes are achieved
when attention is given to automation, correctness, observability, and continuous
improvements. It needs to be ingrained in our culture to look at every aspect of software
development through these measures and reserve human efforts in processes and techniques
that add value to the organization.
The Software Excellence team is happy to work with you to make this happen.

2023 State of Craftsmanship |Software Excellence

21

Authors
Dattatreya Subramanya Vellal
Fernando José Vieira
Rafael Medeiros de Farias Vaz

Reviewers
Ian Watson
Kitty Verberne
Pankaj Prasad
Rob Nicholson
Rodolfo Hansen

2023 State of Craftsmanship |Software Excellence

22

Contact Software Excellence

Send us an e-mail
software_excellence@philips.com

Join us on Viva Engage

Visit our SharePoint

Find us on GitHub*

Philips Q&A

We’re open

Book a slot

2023 State of Craftsmanship |Software Excellence

23


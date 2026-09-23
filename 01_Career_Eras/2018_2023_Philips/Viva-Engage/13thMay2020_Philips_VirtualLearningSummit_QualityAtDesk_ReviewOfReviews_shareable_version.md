# 13thMay2020 Philips VirtualLearningSummit QualityAtDesk ReviewOfReviews shareable version

> Converted from document `13thMay2020_Philips_VirtualLearningSummit_QualityAtDesk_ReviewOfReviews_shareable_version.pdf`

Quality at desk
An initiative by SWCoE

Dattatreya S Vellal
Competency Specialist, Software Excellence
Software Center of Excellence
Internal

Pipelines in Philips
Cost of fixing a failure is more, as and when we move away from the code!
On failure
Fix

Code

Pull
request
checks

Gated
Build

Deploy

Sanity

Integration
Tests

Color Legend

Other tests

Golden
Build

Cost of fix is low
Cost of fix is medium
Cost of fix is high

Thickness
Legend

No. of changes expected to be fixed is high!
No. of changes expected to be fixed is medium
No. of changes expected to be fixed is low
No. of changes expected to be fixed is very low

Internal

Avg time to turn-around a PR comments?

https://bit.ly/PR-TurnAroundTime

Internal

Do these comments look familiar to you?
Real pull request code review comments from real repositories of Philips!
Include copyright in all files
please do Formatting, indentation issue
Maintain in alphabetical order
Cognitive complexity seems to be too high, please optimize this function
This is not used anywhere.
Clear unused imports
code duplication - extract out similar to other service
Avoid hardcoding
change to CamelCase
You should assert if size is less than 1
Please update the line indentation.
This method can be removed, as there is only one line operation. Same could be done inline to return
statement.
Please maintain strings in alphabetical order. Also remove duplicate strings.
Can we decompose this class to multiple classes (Every brush head can have there own class for resources,
name etc) which helps fewer loops and better testing and organized code? Plus if in future addition of more
brush head can become easier.
Is this variable used?
what is 200? please provide the details
I see some Code related to complications in service, where is it checked in unit Testcase ?
Internal

CopyrightHeader
CodeFormatting
CodingStandards
CyclomaticComplexity
DeadCode
DependencyChecks
Duplication
HardCodedValues
NamingConvention
UnitTestCorrectness
CodeFormatting
CodeOptimisation
CodingStandards

CyclomaticComplexity
DeadCode
CodingStandards
UnitTestCorrectness

Are these common?
DeadCode
CodingStandards
CodeFormatting
UnitTestCorrectness
NamingConvention
Duplication
CyclomaticComplexity
SpellingMistake
CodeOptimisation
CopyrightHeader
DependencyChecks
HardCodedValues
HumanError
Similarity

Some more analysis
• 8 different repositories
• PR comments from 1/1 to 30/4
• 1970 pull requests in total
• 7053 comments in total
• 5% comments could be avoided!

Internal

21.30%
18.52%
12.50%
11.11%
8.80%
8.80%
4.63%
4.17%
3.70%
2.78%
1.39%
0.93%
0.92%
0.46%

What could we have avoided?
Let’s do some math!
(a) Total time to address 1 PR comments = 4 hrs -- Assumption
(b) Total pull-requests analyzed = 1970
(c) Total comments in all pull-requests = 7053
(d) Avg no. of comments per pull-request = 7053/1970 = 3.5
(e) Avg no. of comments that was avoidable = 5% of (d) = 353
(f) Effort to address 1 comment in 1 PR = (d)/(a) = 0.9 hrs = 54 mins
(g) Guesstimate of hours saved = (f) * (e) = 317 hrs in 4 months
* 79 hrs per month for 8 repositories
* ~10 hrs per repository per month
Internal

Quality at desk – program from SWCoE
On failure
Fix

Code

Pull
request
checks

Gated
Build

Deploy

Sanity

Integration
Tests

Color Legend

Other tests

Golden
Build

Cost of fix is low
Cost of fix is medium

Code with
IDE

Local build

Tools for
different
languages

Cost of fix is high
Thickness
Legend

No. of changes expected to be fixed is high!
No. of changes expected to be fixed is medium
No. of changes expected to be fixed is low
No. of changes expected to be fixed is very low

Plugins for IDEs

Components

Build controls
Internal

Quality at desk components

Quality at desk – program from SWCoE
What can Q@D check?

Advantages?

• Coding standards

• Local & immediate feedback

• Compiler warnings

• Faster correction cycles

• Unit-test case coverage

• Lesser context switches

• Cyclomatic complexity

• Greater gated build success rates

• Dead code

• Improved productivity

• Copied code

• Built for co-existence

• Programming mistakes

• Highly customizable

• Mutation testing

• Full traceability

• Other custom stuff…

• No additional infrastructure needed
Internal

Where are we now?
Quality at desk programs
• Build controls – Java (maven, gradle), Angular2+ (in-progress)
• Tools – Python, C#, Java, R, C++
• IDE plugins – C++, C#, Java, Python, AngularJS, R
• https://pypi.org/project/guardrails/
• https://gitlab.ta.philips.com/swcoe
Note: Some of the artefacts are built in house by SWCoE, some of them are re-used from other businesses from
Philips, some of them are available as open-source tools/plugins.
Internal

Demo
SWCOE project (Dog fooding):
https://gitlab.ta.philips.com/swcoe/
cerberus/blob/develop/pom.xml
Business project:
https://tfsemea1.ta.philips.com/tfs/
TPC_Region26/MR/_git/mretl/pullrequest/20709?iteration=7&
base=6&_a=files&path=%2Fmr_etl%
2FmrLogDataCollector%2Fpom.xml
Internal

PSI2M RADAR Team – Users of Quality at desk!

Do you want to engage with us?
Remember the 317 hrs saving?
Do you want to start saving now?
Drop a note to any of us indicating your interest, we will contact you:
• sundaresan.j@philips.com
• terol.david@philips.com
• dsvellal@philips.com
• rashmi.mallikarjuna@philips.com
Internal

Questions?
Most popular FAQs
• Q: Can I sync between my Sonar/TICS gating and Quality at Desk gating?
• A: Keep both! They can both co-exist! Experiment first, and then decide!
• Q: How long will it take to integrate Q@D tools?
• A: Typically, if everything goes well, 2hrs working-session with SWCoE can help
onboard Q@D on one of your projects!
• Q: Is this tool-validated?
• A: We are in the process of validating the tools written.

Internal

Quality at desk
Sudeep Prasad
Technical Consultant, Software Excellence
Software Center of Excellence
Internal

Knowledge
- Domain
- Technology

Process

Review of Reviews

- Acceptance criteria
- Readiness

Standards
- Static Analysis rules
- Gates

Internal

USPs of Code Review
• Remedy the curse of knowledge
count += 1

The software
shall validate the
input message
according to …
schema before
storing, throwing
… exception on
invalid input

• Spec-iteration
The software shall
validate the input
message before
storing

The software shall
validate the input
message according
to … schema before
storing
Internal

The software
shall validate the
input message
according to …
schema before
storing, throwing
… exception on
invalid input,
within 80 ms,
using less than
5MB working set,
etc.

Focus: Semantic Distance

Customer
Objectives

Specification
Code
Correctness
Completeness

“Keep asking for input, while the input is invalid”

Internal

Internal

Focus: Semantic Distance

Customer
Objectives

Specification
Code
Correctness
Completeness

“Ignore invalid input in the file”

Internal

Internal

Where would you do a code review?

1

2

3

4

Source

Build

Test

Deploy

Code

Compile

Smoke Test

Provision

Compile & Test

Unit Test

System Test

Stage

Git push

Integration Test

Label ‘ready’

QA / Verification

/ Pull request

Production

Internal

Review of Review of Reviews
Classification / Forecast
• …by cause

Is your classification MECI?

• Tech Awareness
• Domain

Mutually

• …by fix

Exclusive

• Design-level
• Error handling
• Readability

Collectively

Inclusive

• …by effect
• Fixing effort
• Criticality
Internal

Review of Review of Reviews
Post-mortem

• Word-counting to counter confirmation-bias

Internal

Internal

Review types
• Pair programming
• Walk-thru

• Review / on pull-request
• Inspection by review panel

Internal

Questions?

Internal

Thank you!


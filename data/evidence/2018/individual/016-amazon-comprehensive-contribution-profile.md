---
title: "Amazon Comprehensive Contribution Profile (2016-2018)"
date: 2018-08-01
year: 2018
era: Amazon
organization: Amazon
category: Performance Profile
source_type: pdf
channel: email_archive
involvement: author
role: SDE-2 (Software Development Engineer II)
people: ["Aditya Kapoor", "Harsha Nagesh", "Anand Varadarajan", "Raman"]
skills: ["AWS", "Java", "API Design", "Performance Optimization", "Fraud Detection", "Risk Management", "Technical Interviewing", "Scrum", "Migration", "Machine Learning Integration"]
programs: ["TRMS", "AmazonPay", "SVA", "RiPE", "FRS", "Fortress"]
tags: ["profile", "comprehensive", "570-code-changes", "46-interviews", "35k-savings"]
sentiment: positive
impact_type: delivery
recurring: false
---

# Evidence: Amazon Comprehensive Contribution Profile (2016-2018)

## Source
- **File:** `Dattas_Amazon_Profile.pdf`
- **Date:** 2018-08-01
- **Ingested:** 2026-08-06
- **Channel:** Internal Document (Amazon)
- **Category:** Performance Profile

## Key Metrics

| Metric | Value |
|--------|-------|
| Code Activity | 570 changes (182,992 lines added; 41,481 removed) |
| Packages touched | 75 |
| Tickets resolved | 86 |
| Cost savings | $12,344.16/year (APS + AbuseCOPS host optimization) |
| Interviews conducted | 46 (14 weekend events) |
| Scrum workshops | 3+ sessions, highest-scoring trainer |
| AmazonPay API | 2,500 requests/day, TPS 1,150 (requested: 20) |

## 2018 Major Contributions

### 1. Variable Comparison Tool Enhancements (March 2018)
- Added GLS filtering, variable filtering, sample order IDs per mismatch
- Decimal point precision control
- Daily reports emailed to ML team for collaboration on mismatches
- Built for S-Team latency reduction goal (Pay-to-Load)

### 2. APS and AbuseCOPS IMR (Host) Reduction (March 2018)
- Identified opportunity to reduce hosts during Prime Day scaling
- Ran FLO tests to benchmark correctly
- **AbusePreventionService: saved $6,446.28/year**
- **AbuseCOPSService: saved $5,897.88/year**
- **Total: $12,344.16/year savings**

## 2017 Major Contributions

### 1. AmazonPay India Launch - One-Account-Per-Customer Fraud Check (April 2017)
- Handled end-to-end by Datta
- API evaluates ~2,500 requests/day
- TPS supported: 1,150 (requested TPS was only 20 — 57x over-engineered for safety)

### 2. Risk Document Creation (April 2017)
- Generic input document structure for RiPE (Risk Profile Evaluation)
- Became part of RiPE API

### 3. RiPE API - CS-Tech Use-case
- Presented RiPE to Director Anand Varadarajan
- Developed and delivered components for CS-Tech onboarding
- Integration test written to allow Gift Card Service to call RiPE

### 4. FDPS/RDPS Analysis (June 2017)
- Analyzed all clients calling FDPS
- Suggested approach for leveraging RDPS
- Created follow-up wiki for graceful deprecation path

### 5. SVA Bulk Action Tool (July 2017)
- Generic bulk action tool for SVA backlog
- **5,927 investigations reopened** that had missed SLA during AmazonPay launch
- Reused and extended for related-customer-id generation
- Reported as successful in-time delivery

### 6. Interview Questions Evangelization (Feb 2017)
- Created question bank of 30+ curated questions across DS, Algo, PS
- Contributed maximum number of questions
- Used in 14 weekend interview events
- 2 weekend drives conducted on HackerEarth using these questions

## Full Content
```
Summary
• Joined Amazon on 15th Feb 2016
• Code Activity: 570 changes (182,992 lines added; 41,481 lines removed) on 75 packages
since about 2 years ago
• Tickets resolved: 86 tickets resolved
• LinkedIn Page: https://www.linkedin.com/in/dattatreyavellal
• Life prior to Amazon: Dattatreya S Vellal Resume (work-ex until Feb 2016)
2018 Contributions
Major Technical Contributions
# Contributions Date Brief Description Impact
1 VariableComparisonTool 20th For SVA’s Pay-to-load latency • Reduced SDE efforts in figuring out
enhancements March reduction project, I have enhanced the variable samples and the respective
2018 variable comparison tool with the orderId.
following functionalities: • Daily report emailed to the ML team &
the development team, to help
1. Added GLS filtering – this will collaborate & work on mismatches & fix
help in fetching orders to a them faster
specific list of GLS provided • Generic tool enhancements to ensure
via command line. that when the S-Team goal, for which
2. Added variable filtering – this tool was built, is taken up again, the
This will help in generating enhnacements help in reducing SDE
the comparison report for efforts by bringing up the right kind of
only the list of variables that samples to the ML Scientists & the
have been specified via this developers to dive deep & figure out the
option, and will skip the TEC mismatch root-cause.
call made to fetch all the
variables specified for a
country.
3. Added sampleOrderIds per
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
4. Decimal point precision:
Decimal point precision can
now be controlled via input
parameter to the command
line tool. This will ensure that
we don't get misled by
samples which have
difference of 1*10^-6 or so.
Other Impactful Activities that I led in 2018
# Contributions Date Brief Description Impact
1 March 2018 - APS and 20th Identified opportunity to reduce the • AbusePreventionService: Saved
AbuseCOPS IMR March total no of hosts, when doing 2018 $6446.28 per year.
Reduction 2018 Prime-day scaling. Ran FLO tests and • AbuseCOPSService: Saved $5897.88
ensured that our hosts are
per year.
benchmarked correctly & the right no.
• Total cost savings of $12344.16 per
of hosts are used to support our
year!
traffic.
2017 Contributions
Major Technical Contributions
# Contributions Date Brief Description Impact
1 Launching AmazonPay in 14th Project phoenix, which intended to • API written by me evaluates about 2.5k
India, with One-account- April launch AmazonPay - Amazon's wallet requests per day.
per-customer fraud check 2017 in India, with OneAccountPerCustomer • TPS supported by my API: 1150.
fraud check. This was handled end-
Requested TPS: 20.
end by me.
2 Risk Document Creation 28th Creating a generic input document • RiskDocument became a part of RiPE
April structure that can be used by RiPE API.
2017 (Risk Profile Evaluation) to handle
client specific, and Platform specific
inputs, in a generic way.
3 RiPE API - CSTech Use- Worked with Raman to facilitate the • Gift Card Service calls out the CR's and
case initial launch of RiPE API for CS-Tech integration test written by me, to allow
use-case. This included presenting them to on-board to RiPE
RiPE to our director Anand and • RiPE Integration Test and how to call it,
developing and delivering the
Appreciation for helping CAS team
components required for addressing
members
the CS-Tech use-case.
4 FDPS/RDPS Analysis 23rd Analysed who are our clients calling • Suggested an approach of leveraging
June FDPS, and created a follow-up wiki RDPS for fixing a known problem
2017 page to help see if these clients still
have dependencies on FDPS. The
intent is to see how we can support
FDPS hosting RiskDocument, instead
of FraudDocument, also to analyse if
we have a chance of gracefully
depricating FDPS and move to a new
data-store (RDPS) if there is a need.
5 Bulk API - for SVA related 31st Created a generic bulk action tool for • 5927 Investigations which had missed
actions July SVA, to help take care of backlog SLA because of peak loads during the
2017 issues that arose due to understaffing PPI lauch (Amazon Wallet in IN), were
and underestimation during the reopened and investigators were
AmazonPay launch. This tool was allowed to work on the same and
generically written to extend the right complete the backlog.
components of TRMS to solve SVA • This tool was reused and exnteded to
related problems.
generated related-customer-ids for a
given primary customer - again an ad-
ho
```

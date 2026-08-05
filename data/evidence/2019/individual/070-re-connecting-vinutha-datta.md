# Evidence: RE: Connecting Vinutha - Datta

## Source
- **File:** `RE  Connecting Vinutha - Datta.msg`
- **Date:** 2019-10-22
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** Cross-BU Engagement

## Email Metadata
- **From:** "Krishnappa Shapur, Nagaraj" <Nagaraj.ks@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>; "Kempanna; Vinutha"	<Vinutha.Kempanna@philips.com>; "Hariharan; Srinivas"	<Srinivas.Hariharan@philips.com>; "Singh; Vikash Kumar"	<vikash.singh@philips.com>; "Kattimani; Arun" <arun.kattimani@philips.com>;	"Rallapalli; Pragati" <pragati.rallapalli@philips.com>; "H S; Bharath"	<bharath.hs@philips.com>; "Behera; Dillip Kumar"	<dillipkumar.behera@philips.com>; "Jayan; Veena" <veena.jayan@philips.com>
- **CC:** "Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Pandit; Pattabhirama" <pattabhirama.pandit@philips.com>; "Krishnan K; Brijesh"	<brijesh.krishnank@philips.com>; "Hussong; Andreas"	<andreas.hussong@philips.com>; "Ershad; Gul" <gul.ershad@philips.com>
- **Date:** 2019-10-22T05:30:43-04:00
- **Thread depth:** 7
- **Is reply:** True

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Kempanna; Vinutha"	<Vinutha.Kempanna@philips.com>; "Hariharan; Srinivas"	<Srinivas.Hariharan@philips.com>; "Singh; Vikash Kumar"	<vikash.singh@philips.com>; "Kattimani; Arun" <arun.kattimani@philips.com>;	"Rallapalli; Pragati" <pragati.rallapalli@philips.com>; "H S; Bharath"	<bharath.hs@philips.com>; "Behera; Dillip Kumar"	<dillipkumar.behera@philips.com>; "Jayan; Veena" <veena.jayan@philips.com>

> Thank you Vinutha, Vikash, Srinivas for your time today.

> b.       Datta: Setup a meeting with the team to understand unit-tests gaps and how we can bridge them.

> c.       Datta: Setup a meeting with the team on gating practices we can introduce in the code-base.

> To: Vellal, Dattatreya

## Full Email Content

```
Subject: RE: Connecting Vinutha - Datta
From: "Krishnappa Shapur, Nagaraj" <Nagaraj.ks@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Kempanna; Vinutha"	<Vinutha.Kempanna@philips.com>; "Hariharan; Srinivas"	<Srinivas.Hariharan@philips.com>; "Singh; Vikash Kumar"	<vikash.singh@philips.com>; "Kattimani; Arun" <arun.kattimani@philips.com>;	"Rallapalli; Pragati" <pragati.rallapalli@philips.com>; "H S; Bharath"	<bharath.hs@philips.com>; "Behera; Dillip Kumar"	<dillipkumar.behera@philips.com>; "Jayan; Veena" <veena.jayan@philips.com>
CC: "Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Pandit; Pattabhirama" <pattabhirama.pandit@philips.com>; "Krishnan K; Brijesh"	<brijesh.krishnank@philips.com>; "Hussong; Andreas"	<andreas.hussong@philips.com>; "Ershad; Gul" <gul.ershad@philips.com>
Date: 2019-10-22T05:30:43-04:00

--- Latest Reply ---
All,

  This is a good summary.
The findings seem interesting

+ Adding test & Dev –ops guys
We should start off with


1.       The recommendations:

a.       We start with test duplication detection by running cosine-similarity tool with the team. This will ensure that if there are duplicates in manual tests, the problem of time-to-market can be reduced immediately and with minimal involvement of the team or disruption to schedule.

[NAGARAJ]: Bharath-Pragati: Can you explore on this



b.       We start integrating smart-test ordering that’ll look at connects between git-commits and test-files and tell us what tests have to be run in what order based on the commits made to the code base, there-by helping in identifying what tests to run to check sanity.

c.       We’ll also look at how we can introduce the right gates at developer box, at local builds and at common builds.



[NAGARAJ]: Dillip , Can you cover under your CI-CD plan



d.       We’ll target unit-test coverage for some common patterns, and how we can achieve them in the code.

e.       We’ll also look at how we can strengthen the unit-tests asserts with mutation testing.



[NAGARAJ]: Srini, Veena, Can you check on this since you are leading efforts on UNIT test


With the above ones set in place, we can look at deduplication of the codebase

Best Rgds
Nagaraj KS

--- Previous Message (1) ---
Sent: Tuesday, October 22, 2019 2:13 PM
To: Kempanna, Vinutha <Vinutha.Kempanna@philips.com>; Hariharan, Srinivas <Srinivas.Hariharan@philips.com>; Singh, Vikash Kumar <vikash.singh@philips.com>
Cc: Jagadeesan, Sundaresan <sundaresan.j@philips.com>; Pandit, Pattabhirama <pattabhirama.pandit@philips.com>; Krishnan K, Brijesh <brijesh.krishnank@philips.com>; Hussong, Andreas <andreas.hussong@philips.com>; Ershad, Gul <gul.ershad@philips.com>; Krishnappa Shapur, Nagaraj <Nagaraj.ks@philips.com>
Subject: RE: Connecting Vinutha - Datta

Thank you Vinutha, Vikash, Srinivas for your time today.

Here’s what we discussed:

1.       The data as we know:

a.       The team has approximately 400 manual tests that get executed before a release, with a code-size of ~50k lines.

b.       Currently there are sanity tests that are executed before the build, but there are opportunities to improve.

c.       By Q1 2020, there are plans of migrating all the code-bases to TFS-GIT and CICD pipelines to TFS.

d.       An audit was conducted in the past, and recommendations came out that increasing the strengths of unit-tests and coverage would help.

e.       Developers run Resharper for static code analysis at their desk, and this is on a “best effort” basis, and is not gated.

f.        Some new projects are getting initiated and/or some projects are still in its early stages, and the team is looking at ways of upholding code-quality via gating in such projects.

2.       The recommendations:

a.       We start with test duplication detection by running cosine-similarity tool with the team. This will ensure that if there are duplicates in manual tests, the problem of time-to-market can be reduced immediately and with minimal involvement of the team or disruption to schedule.

b.       We start integrating smart-test ordering that’ll look at connects between git-commits and test-files and tell us what tests have to be run in what order based on the commits made to the code base, there-by helping in identifying what tests to run to check sanity.

c.       We’ll target unit-test coverage for some common patterns, and how we can achieve them in the code.

d.       We’ll also look at how we can introduce the right gates at developer box, at local builds and at common builds.

e.       We’ll also look at how we can strengthen the unit-tests asserts with mutation testing.

f.        With the above ones set in place, we can look at deduplication of the codebase.

3.       Next actions:

a.       Pattabhi and Brijesh: Setup a meeting with the team to on-board them to similarity analysis.

b.       Datta: Setup a meeting with the team to understand unit-tes

[... truncated, full content in database ...]
```
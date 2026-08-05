# Evidence: Quality at Desk — EMR XLint Compiler Warnings Innovation

## Source
- **File:** `20200525_QualityAtDesk_EMR_XLintCompilerWarnings.png`
- **Date:** 2020-05-25
- **Ingested:** 2026-08-05
- **Channel:** teams_chat_screenshot
- **Category:** Recognition / Praise

## Metadata
- **Platform:** Yammer (Software Center of Excellence SW_CoE group)
- **Program referenced:** Quality at Desk / Compiler Warnings Gating
- **People visible:** Jaiswal Rajendra Kumar (OP), Terol David (reply), De Marco Darlan Diego (reply)
- **CC:** Patricio, Rafael, Mudiganti, Satyanarayana Reddy, Shukla, Susmita, Weiss, Joao Paulo, De Marco, Darlan Diego, Trentin, Carlos Eduardo, Shetty, Nishwal, and Singh, Himanshu
- **Reactions:** Patricio, Rafael, Terol, David, Golsteijn, Bart, and 6 others
- **Seen by:** 173

## Datta's Involvement
- **Role at time:** Competency Specialist — Software Excellence, SWCoE
- **Involvement type:** Program owner — this is a Quality at Desk initiative outcome showing teams independently innovating within the framework Datta established

## Visible Content (Extracted Text)
**Jaiswal, Rajendra Kumar** — May 25 at 11:55 AM:

"- **What is Xlint Java Compiler Warnings?** If source code is compiled with -Xlint:all, it gives you other close to 15 types of warning in the source code which is not thrown by javac.
  For Ex. cast, deprecation, divzero, empty, fallthrough, finally, overrides, path, serial, and unchecked etc.

- **How to report the -Xlint:all warning inline into code review system?** Whenever a developer makes a change in the system, developers needs to open a GitHub Pull Request. This is integrated into **Gated Pull Request CI** process to find out new Xlint compiler warning and report inline.
  How?
  1) Run a CI Build
  2) Compile the change set with -Xlint:all and capture the warnings
  3) Process the diff and pull out a list of line numbers changed/added in Pull request per file
  4) Iterate over warning log per file
     - Find an occurrence of warning
     - Pull out the line number
     - Extract log only for line number
     - Check if line number is part of changed/added list
     - If YES, post a comment with error/warning details
     - If NO, this is not a new warning"

[Screenshot showing GitHub PR with inline compiler warning comments]

**Terol, David** — May 26 at 12:40 PM:
"Thanks Jaiswal, Rajendra Kumar for sharing. Raising the bar to detect and enforce fix of Compiler Warnings at source is cheapest way to prevent potential future errors and portability issues. Extra steps could include detection of duplicated code or type refinement to guard from illegal states."

**De Marco, Darlan Diego** in reply to Terol, David — May 26 at 05:57 PM:
"Hi David, thanks for your kind words! About the extra steps over duplicated code detection, it is already in place. Not inline as compiler warning, but we are about putting this as a Link in the gated block pull request. It will lead te developer to a page with the code duplication before the commit, and after the commit. This will turn easy to the developer identify which code has been duplicated."

## Key Quotes
> "Raising the bar to detect and enforce fix of Compiler Warnings at source is cheapest way to prevent potential future errors and portability issues."

## Context
This screenshot shows a team (EMR) innovating within the Quality at Desk framework that Datta established. They integrated Xlint compiler warning detection into their PR gating process — exactly the kind of "quality at developer desk" shift the program was designed to achieve. The team independently extended the concept beyond what was originally taught, showing the program created autonomous quality champions rather than dependence on SWCoE. David Terol (Datta's manager) praised the approach publicly.

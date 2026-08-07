---
title: "Quality at Desk — EMR Team XLint Compiler Warnings Gated Pull Request Integration"
date: 2020-05-25
year: 2020
era: Philips India
organization: Philips
category: Informal Feedback
source_type: image
channel: internal_screenshot
involvement: direct_recipient
role: SWCoE Competency Specialist
people: ["Jaiswal, Rajendra Kumar", "Terol, David", "De Marco, Darlan Diego", "Patricio, Rafael", "Mudiganti", "Shukla, Susmita", "Weiss, Joao Paulo", "Trentin, Carlos Eduardo", "Shetty, Nishwal", "Singh, Himanshu"]
skills: ["xlint", "java-compiler-warnings", "ci-cd", "gated-pull-request", "code-quality", "quality-at-desk"]
programs: ["Quality at Desk", "SW Center of Excellence"]
tags: ["informal-feedback", "yammer", "peer-recognition", "quality-at-desk", "xlint", "compiler-warnings", "emr", "ci-cd"]
sentiment: positive
impact_type: recognition
recurring: false
---

# Evidence: Quality at Desk — EMR Team XLint Compiler Warnings Gated Pull Request Integration

## Source
- **File:** `quality-at-desk-emr-xlint-compiler-warnings-2020.png`
- **Original:** `20200525_QualityAtDesk_EMR_XLintCompilerWarnings.png`
- **Date:** 2020-05-25
- **Ingested:** 2026-08-06
- **Channel:** Yammer — Software Center of Excellence (SW_CoE) group
- **Category:** Informal Feedback

## Context
Jaiswal, Rajendra Kumar posted to the SW CoE Yammer group sharing how the EMR team integrated XLint Java Compiler Warnings detection into their Gated Pull Request CI process. The post described what XLint warnings are (15 types including cast, deprecation, divzero, empty, fallthrough, finally, overrides, path, serial, unchecked), and how the system works in a CI Build pipeline. The post was seen by 173 people and generated engagement from David Terol (who praised it as "cheapest way to prevent potential future errors") and Darlan Diego De Marco (who shared upcoming enhancements including code duplication detection). This is indirect evidence of Datta's Quality at Desk initiative spreading across teams.

## Content

**Jaiswal, Rajendra Kumar — May 25 at 11:55 AM:**

- What is Xlint Java Compiler Warnings? If source code is compiled with -Xlint:all, it gives you other close to 15 types of warning in the source code which is not thrown by javac. For Ex: cast, deprecation, divzero, empty, fallthrough, finally, overrides, path, serial, and unchecked etc.

- How to report the -Xlint:all warning inline into code review system? Whenever a developer makes a change in the system, developers needs to open a GitHub Pull Request. This is integrated into Gated Pull Request CI process to find out new Xlint compiler warning and report inline.

How?
1) Run a CI Build
2) Compile the change set with -Xlint:all and capture the warnings
3) Process the diff and pull out a list of line numbers changed/added in Pull request per per file
4) Iterate over warning log per file
   - Find an occurrence of warning
   - Pull out the line number
   - Extract log only for line number
   - Check if line number is part of changed/added list
   - If YES, post a comment with error/warning details
   - If NO, this is not a new warning

cc: Patricio, Rafael, Mudiganti, Satyanarayana Reddy, Shukla, Susmita, Weiss, Joao Paulo, De Marco, Darlan Diego, Trentin, Carlos Eduardo, Shetty, Nishwal and Singh, Himanshu

Reactions: Patricio, Rafael, Terol, David, Golstein, Bart, and 6 others reacted to this. Seen by 173.

**Terol, David — May 26 at 12:40 PM:**
Thanks Jaiswal, Rajendra Kumar for sharing. Raising the bar to detect and enforce fix of Compiler Warnings at source is cheapest way to prevent potential future errors and portability issues. Extra steps could include detection of duplicated code or type refinement to guard from illegal states.

cc: Jaiswal, Rajendra Kumar

De Marco, Darlan Diego reacted to this.

**De Marco, Darlan Diego in reply to Terol, David — May 26 at 05:57 PM — Edited:**
Hi David, thanks for your kind words!

About the extra steps over duplicated code detection, it is already in place. Not inline as compiler warning, but we are about putting this as a Link in the gated block pull request. It will lead developer to a page with the code duplication before the commit, and after the commit. This will turn easy to the developer identify which code has been duplicated.

We will create another post here about this subject in the next few days!

[Code duplication dashboard image attached]

## Key Quotes

> "Raising the bar to detect and enforce fix of Compiler Warnings at source is cheapest way to prevent potential future errors and portability issues."
> — Terol, David

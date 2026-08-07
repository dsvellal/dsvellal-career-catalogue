# Evidence: Quality at Desk — EMR XLint Compiler Warnings in Gated Pull Requests

## Source
- **File:** `20200525_QualityAtDesk_EMR_XLintCompilerWarnings.png`
- **Date:** 2020-05-25
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer - Software Center of Excellence SW_CoE)
- **Category:** Informal Feedback

## Metadata
- **From:** Jaiswal, Rajendra Kumar (posted); Terol, David and De Marco, Darlan Diego (engaged in thread)
- **To/About:** SW CoE team (Datta cc'd as community member)
- **Context:** The EMR team shared their implementation of XLint Java Compiler Warnings integrated inline into Gated Pull Request CI processes. This was a Quality at Desk initiative supported by SW CoE. Seen by 173 people with multiple team leads engaging in discussion about extending the practice.
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** Patricio, Rafael; Terol, David; Golsteijn, Bart; and 6 others reacted
- **cc:** Patricio, Rafael; Mudiganti, Satyanarayana Reddy; Shukla, Susmita; Weiss, Joao Paulo; De Marco, Darlan Diego; Trentin, Carlos Eduardo; Shetty, Nishwal; and Singh, Himanshu

## Datta's Involvement
- **Role at time:** Senior Software Engineer / SW CoE
- **Involvement type:** Community member — Quality at Desk initiative he helped champion

## Key Quotes
> "What is Xlint Java Compiler Warnings? If source code is compiled with -Xlintall, it gives you other close to 15 types of warning in the source code which is not thrown by javac. For Ex. cast, deprecation, divzero, empty, fallthrough, finally, overrides, path, serial, and unchecked etc."

> "How to report the -Xlint:all warning inline into code review system? Whenever a developer makes a change in the system, developers needs to open a GitHub Pull Request. This is integrated into Gated Pull Request CI process to find out new Xlint compiler warning and report inline."

> "Thanks Jaiswal, Rajendra Kumar for sharing. Raising the bar to detect and enforce fix of Compiler Warnings at source is cheapest way to prevent potential future errors and portability issues."
— Terol, David

## Full Content
```
Software Center of Excellence (SW_CoE)

Jaiswal, Rajendra Kumar — May 25 at 11:55 AM

- What is Xlint Java Compiler Warnings? If source code is compiled with -Xlintall, it gives you other close to 15 types of warning in the source code which is not thrown by javac.
  For Ex. cast, deprecation, divzero, empty, fallthrough, finally, overrides, path, serial, and unchecked etc.

- How to report the -Xlint:all warning inline into code review system? Whenever a developer makes a change in the system, developers needs to open a GitHub Pull Request. This is integrated into Gated Pull Request CI process to find out new Xlint compiler warning and report inline.
  How?
  1) Run a CI Build
  2) Compile the change set with -Xlintall and capture the warnings
  3) Process the diff and pull out a list of line numbers changed/added in Pull request per file
  4) Iterate over warning log per file
     o Find an occurrence of warning
     o Pull out the line number
     o Extract log only for line number
     o Check if line number is part of changed/added list
     o If YES, post a comment with error/warning details
     o If NO, this is not a new warning

cc: Patricio, Rafael, Mudiganti, Satyanarayana Reddy, Shukla, Susmita, Weiss, Joao Paulo, De Marco, Darlan Diego, Trentin, Carlos Eduardo, Shetty, Nishwal, and Singh, Himanshu

[Screenshot of GitHub Pull Request showing inline XLint warning comments from bot: kln-philips-emr-jenkins]

Patricio, Rafael, Terol, David, Golsteijn, Bart, and 6 others reacted to this
Seen by 173

---

Terol, David — May 26 at 12:40 PM
Thanks Jaiswal, Rajendra Kumar for sharing. Raising the bar to detect and enforce fix of Compiler Warnings at source is cheapest way to prevent potential future errors and portability issues. Extra steps could include detection of duplicated code or type refinement to guard from illegal states.

cc: Jaiswal, Rajendra Kumar
De Marco, Darlan Diego reacted to this

---

De Marco, Darlan Diego in reply to Terol, David — May 26 at 05:57 PM — Edited
Hi David, thanks for your kind words!

About the extra steps over duplicated code detection, it is already in place.

Not inline as compiler warning, but we are about putting this as a Link in the gated block pull request.

It will lead te developer to a page with the code duplication before the commit, and after the commit. This will turn easy to the developer identify which code has been duplicated.

We will create another post here about this subject in the next few days!

You can see an example in the bellow image:

[Screenshot showing code duplication detection dashboard with before/after metrics]

Terol, David and Trentin, Carlos Eduardo reacted to this
```

# 20230515 Back2Basics

> Converted from document `20230515_Back2Basics.pdf`

Back to basics
Dattatreya S Vellal (Datta)
Competency Lead
Software Center of Excellence

Your expectations from this workshop?
https://www.menti.com/alsgn98y7zpf

menti.com -> 3934 1069

Let’s get started with a sample!
You are the reviewer of this code snippet.
Here are some tips to help you review the code:
1. Do not assume anything! Everything is reviewable.
2. Please pay close attention to everything you see. You are free to question EVERYTHING.
3. Once you approve the code, it'll sit in production.
4. The code has very good unit-test coverage too!

5. If you approve the pull request, any bugs reported after the approval will be co-owned by you.

https://bit.ly/swcoe-review-me

Some anti-patterns

And how to fix them!

Disclaimer!
• We are looking at innersource data, and this is confidential.
• We are using repos as examples only.
• We intend to show patterns and not target repositories.

Oops! Password!!
• Be careful of what you commit and where
• https://github.com/search?q=org%3Aphilipsinternal+password+lang%3Ayaml&type=code

Copy paste much?
• Let’s look at this repo and see if anything is wrong with this?
• https://github.com/philips-internal/cicd-secrets-data
• What’s the purpose of the repo?
• What’s the content structure?
• Let’s look at “whispers” content…

(Is this appropriate)? Why: What could have been done better;

Keep a watch on PR comments!
Include copyright in all files
please do Formatting, indentation issue
Maintain in alphabetical order
Cognitive complexity seems to be too high, please optimize
this function
This is not used anywhere.
Clear unused imports
code duplication - extract out similar to other service
Avoid hardcoding
change to CamelCase
You should assert if size is less than 1
Please update the line indentation.
This method can be removed, as there is only one line
operation. Same could be done inline to return statement.
Please maintain strings in alphabetical order. Also remove
duplicate strings.
Is this variable used?
what is 200? please provide the details
I see some Code related to complications in service, where is
it checked in unit Testcase ?

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

8 different repositories
PR comments from 1/1 to 30/4
1970 pull requests in total
7053 comments in total
5% comments could be avoided!

Merge the pull requests
• What’s the age of your oldest pull request?
• https://github.com/philips-internal/emr-schematics/pulls
• https://github.com/philips-internal/oneapp-coreservices-ios/pulls
• https://github.com/philips-internal/tasyinterfaces/pulls?page=3&q=is%3Apr+is%3Aopen

Let’s look at issues!
• Address continuous compliance & other house-keeping issues
• https://github.com/philips-internal/psi2m-daw-nextgen/issues
• https://github.com/philips-internal/ix-component-audit/issues

Keeping our code clean!
• Stale branches
• https://github.com/philips-internal/ix-template/branches
• https://github.com/philips-internal/rocc-management-service/branches

Who has access to your code?
• For the repos you own/maintain
• Look at teams/individuals access & the level of access
• https://github.com/philips-internal/fortify-scan-action/settings/access

• Assign access to team whenever possible – instead of individuals, to
avoid single-point-of-failure.

Run what’s needed
• Remember, it’s free for you, not for Philips!
• https://github.com/philips-internal/Clinical-Platform/actions
• https://github.com/philips-internal/swcoe-data-pipe/actions
• https://github.com/philips-internal/HSP_DicomStoreCurie/actions

What is SWCoE doing?
• Developer Portal
• Philips’ stack-overflow
• Philips code hub
• Self-hosted runners
• GitHub & innersource initiatives
• Many other initiatives.

Feedback
https://bit.ly/swcoe-back2basics-feedback


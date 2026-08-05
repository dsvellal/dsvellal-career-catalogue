# Evidence: FYI: [Req Info] Code question being asked to Pradeep

## Source
- **File:** `FYI   Req Info  Code question being asked to Pradeep.msg`
- **Date:** 2019-01-14
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** Vellal, Dattatreya
- **To:** Mishra, Nitin <nitin.mishra@philips.com>
- **Date:** 2019-01-14T14:00:23.874708-05:00
- **Thread depth:** 6
- **Is reply:** False
- **Attachments:** 3
  - `BankAccountProblem.java` (application/octet-stream, 1628 bytes)
  - `CodeReview.java` (application/octet-stream, 542 bytes)
  - `n-ary zig-zag print.txt` (application/octet-stream, 364 bytes)

## Datta's Involvement
- **Role at time:** Senior Architect, IDM
- **Involvement type:** Author

## Key Quotes
> From: Vellal, Dattatreya

> Senior Architect | IDM | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

> Thanks Viswa.

> To: Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>

## Full Email Content

```
Subject: FYI: [Req Info] Code question being asked to Pradeep
From: Vellal, Dattatreya
To: Mishra, Nitin <nitin.mishra@philips.com>
Date: 2019-01-14T14:00:23.874708-05:00

--- Latest Reply ---
FYI Nitin - To give you an idea about the sort of questions I intend to ask and what data-points I am looking for.

Regards,
Datta
Senior Architect | IDM | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

--- Previous Message (1) ---
Sent: Tuesday, January 15, 2019 12:29 AM
To: Aklecha, Vishwajit <vishwajit.aklecha@philips.com>
Subject: RE: [Req Info] Code question being asked to Pradeep

Thanks Viswa.

I have two questions that I wish to cover as a part of this discussion, and one more buffer if we still have time, there’s a third question as well. I am calling all the three out in this email.

1.       I intend to start the conversation with an ice-breaker “CodeReview.java”. The intent here is to see what sort of code-review comments Pradeep provides, by looking at the code. I am specifically looking for, whether a candidate reads through the code-documentation to understand what’s expected out the class & considers the following aspects when reviewing code:

a.       Code readability (indentation)

b.       Naming convention (for variables, for the class itself)

c.       Reducing code-repeatability (8 is repeated multiple times. Extracting it into an access-modifier-appropriate property & providing necessary mechanisms to access the same via getters (and setters))

d.       The logic is wrong:

                                                               i.      The code-comment calls out that if any of the variable is less than 8, all of them have to default to 8, but the code calls out that if all of them are 8, then they are assigned.

                                                             ii.      Assignment is wrongly done. There are no braces in the if() – there are chances that irrespective of value passed b & c are always assigned to 8!

e.       Question the existence of “system.out.println” and how to convert it to logger statements if necessary.

f.        No test-code is written for this – perhaps request the reviewee to submit test-cases for this (unit/integration tests)

2.       The second one is a more intense discussion & also calls out the ability of Pradeep to showcase what he has provided in his resume. I am looking along the lines of the following points:

a.       Account class shouldn’t have public variables! They have to be private and necessary access modifiers should be provided as a part of the class.

b.       Account – shouldn’t really have those properties, it should be a part of “AccountInfo” class. Account in-itself is a transactional class, and should be considered to host only those responsibilities.

c.       In the Bank class, in both debit & credit methods, Strings are passed instead of Account (or AccountInfo) instances.

d.       Exception handling & graceful failures (what if the Account passed doesn’t exist? Or is not an account into which the intended transaction is permitted?, what if value passed in double is negative?)

e.       What if I call the debit & credit out-of-order, with multiple-threads? Thread synchronisation is important here & the mechanism used to synchronise the threads that are sending interleaved from & to accounts.

f.        Adding logs/metrics where-ever necessary.

g.       Pulling out TestMain into a separate junit-testable code

h.       Providing appropriate code-comments where-ever necessary.

i.         Single-responsibility-principle – see if debit & credit are responsibility of bank-class, or the account-class and justify the same.

3.       If time-permits, I have a third question – specified in the “n-ary zig-zag print.txt” – this is more of a discussion in terms of what data-structures can be used to solve this problem and how. Multiple methods of solving this, optimizing the solution with space/time trade-offs.

Regards,
Datta
Senior Architect | IDM | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

--- Previous Message (2) ---
Sent: Monday, January 14, 2019 4:10 PM
To: Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>
Subject: RE: [Req Info] Code question being asked to Pradeep

Hi Datta:

I already met the candidate, and discussed couple of hands-on questions. My suggestion is – you should lead the next interview, and discuss some of your favorite problem solving questions with him.

One way to discuss code is – to show some piece of existing code and ask candidate to review the code.

Best regards,

--- Previous Message (3) ---
Vishwajit Aklecha

--- Previous Message (4) ---
Sent: Monday, January 14, 2019 14:38
To: Aklecha, Vishwajit <vishwajit.aklecha@philips.com<mailto:vishwajit.aklecha@philips.com>>
Subject: [Req Info] Code question being asked to Pradeep

Hi Vishwa,
For tomorrow's interview with Pra

[... truncated, full content in database ...]
```
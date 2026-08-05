# Evidence: Re: Steps towards code-quality improvements

## Source
- **File:** `Re  Steps towards code-quality improvements.msg`
- **Date:** 2018-11-28
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "Inganti, Dheeraj" <dheeraj.inganti@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>; dl_BlrPH_HITCoE_IDM	<dl_BlrPH_HITCoE_IDM@philips.com>
- **CC:** "Kn; Pradeep" <pradeep.kn@philips.com>; "Mohan; Murali"	<murali.mohan@philips.com>; "Chourey; Pooja" <Pooja.Chourey@philips.com>
- **Date:** 2018-11-28T08:33:18-05:00
- **Thread depth:** 3
- **Is reply:** True

## Datta's Involvement
- **Role at time:** Senior Architect, IDM
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>; dl_BlrPH_HITCoE_IDM	<dl_BlrPH_HITCoE_IDM@philips.com>

> Good guidelines, Datta.

> Thanks & Regards,

> Senior Architect | IDM | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

## Full Email Content

```
Subject: Re: Steps towards code-quality improvements
From: "Inganti, Dheeraj" <dheeraj.inganti@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>; dl_BlrPH_HITCoE_IDM	<dl_BlrPH_HITCoE_IDM@philips.com>
CC: "Kn; Pradeep" <pradeep.kn@philips.com>; "Mohan; Murali"	<murali.mohan@philips.com>; "Chourey; Pooja" <Pooja.Chourey@philips.com>
Date: 2018-11-28T08:33:18-05:00

--- Latest Reply ---
Good guidelines, Datta.

All,

It is imperative for us to own up quality with goal towards 100% automation in unit tests and functional tests.


Thanks & Regards,
Dheeraj

--- Previous Message (1) ---
Date: Monday, November 26, 2018 at 1:18 PM
To: "dl_BlrPH_HITCoE_IDM@philips.com" <dl_BlrPH_HITCoE_IDM@philips.com>
Cc: "Kn, Pradeep" <pradeep.kn@philips.com>, "Mohan, Murali" <murali.mohan@philips.com>, "Chourey, Pooja" <Pooja.Chourey@philips.com>
Subject: Steps towards code-quality improvements

Hello Team,
Over a period of time, I have been reviewing and merging PR’s and this email calls out a few best-practices that we can imbibe to help us in creating a more maintainable & testable code base.

Guidelines before raising a PR:

  1.  Every git commit should have the corresponding TFS ID for which the commit is being made.
  2.  Every PR title should call out the TFS ID for which the PR has been raised.
  3.  For the new code added (changes in existing files and/or new files added) – We should have 100% test-case coverage.
  4.  Call out the test-case coverage per-file changed in the PR description (you can get the coverage % from the build logs)
  5.  Specify the build link where the changes have been built
  6.  While we don’t have automated integration tests yet, in the PR, call out what approach you took, to validate whether the changes made are working as intended.
     *   This can be as simple as: I validated this feature by deploying the changes in neb/vig and validating it via thruk. Here’s the snapshot of it <link>
  7.  While raising a PR, also include the changes required for the IDM document(s)
  8.  Ensure that appropriate log statements are added where it's necessary.
  9.  Log complete exception in case of a try-except block.
  10. Perform a git pull rebase - before submitting a developer build.
  11. Ensure appropriate code-comments are added where-ever necessary.

General guidelines:

  1.  Do not combine bug-fixes and features into a single PR.
  2.  For a feature - an approved design document has be to presented along with the PR description. The design document can be a link to the TFS ID containing the same.

Future improvements that we are thinking of:

  1.  Metrics driven code development
  2.  Integrating testing
  3.  Automating regression testing
  4.  Integrating build failures if unit-tests or coverage tests or integration tests or regression tests fail.

NOTE1: I highly encourage you guys to consider the above points before raising a PR. Starting today, I’ll be monitoring for these when I approve/merge the PRs. Our goal is to achieve a healthy regression-free build, on every build with enough automation to catch defects as soon as possible!

NOTE2: If you need any support, please feel free to reach out to me, and I’ll be happy to help.

Regards,
Datta
Senior Architect | IDM | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

--- Previous Message (2) ---
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.
```
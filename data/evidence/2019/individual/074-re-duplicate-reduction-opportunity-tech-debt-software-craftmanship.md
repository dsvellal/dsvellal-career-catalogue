# Evidence: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship

## Source
- **File:** `RE  Duplicate reduction opportunity - tech-debt & software-craftmanship.msg`
- **Date:** 2019-09-23
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** Code Duplication / JSCPD

## Email Metadata
- **From:** "Jagadeesan, Sundaresan" <sundaresan.j@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>
- **CC:** "R U; Rashmi" <rashmi.mallikarjuna@philips.com>
- **Date:** 2019-09-23T07:45:12-04:00
- **Thread depth:** 21
- **Is reply:** True

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>

> Thanks Datta!

> Thank you Bharath. Very interesting data. Thank you for sharing. An interesting observation:

> To: Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>

> Thank you for being open in sharing your code base, and results. I have accepted the invite & am looking forward to it.

## Full Email Content

```
Subject: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship
From: "Jagadeesan, Sundaresan" <sundaresan.j@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>
CC: "R U; Rashmi" <rashmi.mallikarjuna@philips.com>
Date: 2019-09-23T07:45:12-04:00

--- Latest Reply ---
Thanks Datta!
Include them as part of this week overall engagement.
We need to show some good numbers for duplication identification and (removal )

--- Previous Message (1) ---
Sent: Monday, September 23, 2019 2:31 PM
To: Battaje, Bharath <bharath.battaje@philips.com>
Cc: Krishnaraj, Hamsa <Hamsa.Krishnaraj@philips.com>; Jagadeesan, Sundaresan <sundaresan.j@philips.com>; R U, Rashmi <rashmi.mallikarjuna@philips.com>
Subject: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship


Thank you Bharath. Very interesting data. Thank you for sharing. An interesting observation:
1.      Without test: 94k lines of code, with 32.07% duplication
2.      With test: 148k lines of code, with 39.7% duplication

We can get in the session and talk about how to improve the duplication.

+Sundar, Rashmi – I have been working with Hamsa & Bharath to run JSCPD with IOT team. We are making steady progress. I will keep you posted on the results! This is an FYI to give you a trail of conversation we have been having.

--- Previous Message (2) ---
Datta

--- Previous Message (3) ---
Sent: Monday, September 23, 2019 2:07 PM
To: Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>
Cc: Krishnaraj, Hamsa <Hamsa.Krishnaraj@philips.com<mailto:Hamsa.Krishnaraj@philips.com>>
Subject: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship


Hi Datta,

Before we meet tomorrow, just wanted to share the full jscpd report for IOT hub repositories.
I was waiting for the IRB1 release to run the full report so that we can get the production ready code.
I ran two report, 1. Excluding tests 2. Including test.

 << File: jscpd-report_including_test.html >>  << File: jscpd-report_excluding_test.html >>
One of the main reason for duplicate code is the module duplication in many code base.
We already have a plan for that and I will be updating that tomorrow.

Thanks
Bharath

--- Previous Message (4) ---
Sent: Wednesday, September 18, 2019 11:33 AM
To: Battaje, Bharath <bharath.battaje@philips.com<mailto:bharath.battaje@philips.com>>
Cc: Krishnaraj, Hamsa <Hamsa.Krishnaraj@philips.com<mailto:Hamsa.Krishnaraj@philips.com>>
Subject: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship


Thank you for being open in sharing your code base, and results. I have accepted the invite & am looking forward to it.

--- Previous Message (5) ---
Datta

--- Previous Message (6) ---
Sent: Wednesday, September 18, 2019 8:45 AM
To: Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>
Cc: Krishnaraj, Hamsa <Hamsa.Krishnaraj@philips.com<mailto:Hamsa.Krishnaraj@philips.com>>
Subject: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship


I have scheduled  an hour meeting for next week. Let’s discuss these points.
Also I am working on a super POM for our project with the required plugins.
I would like to get it reviewed for any improvements.

Once again thank you for all your help and inputs.

--- Previous Message (7) ---
Sent: Tuesday, September 17, 2019 11:17 AM
To: Battaje, Bharath <bharath.battaje@philips.com<mailto:bharath.battaje@philips.com>>
Cc: Krishnaraj, Hamsa <Hamsa.Krishnaraj@philips.com<mailto:Hamsa.Krishnaraj@philips.com>>
Subject: RE: Duplicate reduction opportunity - tech-debt & software-craftmanship


Thank you Bharath for the report.

I really commend your effort of getting cpd-pmd dependency into maven. This is good! Please consider sharing your parent pom.xml, maybe we can work on it together and see how we can strengthen it.

For your question on why did TICS not pick it up, I have the answer. In short, TICS ignores imports, and any test-code! Also, TICS runs with a standard token count of 100! It’s laughably easy to break TICS’s duplication report! While it’s a data-point, I do not consider TICS’s duplication report as a strong data-point!

I went through some of these, and I am taking the liberty to share a few observations that I have made. This is only between you and me (and may be Hamsa knows because she is in cc!), but I see some very glaring programming patterns that may need to be corrected.

--- Previous Message (8) ---
Observation 1:
We can derive meaning out of import duplicates too!
Example, I see these duplication:

import com.philips.services.iothub.discoveryservice.constants.DiscoveryConstants;
import com.philips.services.iothub.discoveryservice.constants.DiscoveryLogConstants;
… and I am wondering, why are we importing all the constants? Why are we not using static imports and just getting the right constants, why pull the entire constant file? [Leads to memory inefficiency, no?

[... truncated, full content in database ...]
```
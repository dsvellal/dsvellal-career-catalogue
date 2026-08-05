# Evidence: RE: HSDP Contingency Action Clarifications 

## Source
- **File:** `RE  HSDP Contingency Action Clarifications .msg`
- **Date:** 2019-12-03
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "Orakkan, Binu" <binu.orakkan@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>; "Kannanth; Amrithraj"	<amrithraj.kannanth@philips.com>
- **CC:** "Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Supakar; Sitangshu"	<sitangshu.supakar@philips.com>
- **Date:** 2019-12-03T03:52:17-05:00
- **Thread depth:** 3
- **Is reply:** False
- **Attachments:** 1
  - `Contingent_Actions(HSDP-DP).xlsx` (application/octet-stream, 377146 bytes)

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Kannanth; Amrithraj"	<amrithraj.kannanth@philips.com>

> Thanks Datta for your suggestions and ideas to streamline this further, will definitely reach to you for further discussion.

> To: Orakkan, Binu; Vellal, Dattatreya; Kannanth, Amrithraj

## Full Email Content

```
Subject: RE: HSDP Contingency Action Clarifications 
From: "Orakkan, Binu" <binu.orakkan@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Kannanth; Amrithraj"	<amrithraj.kannanth@philips.com>
CC: "Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Supakar; Sitangshu"	<sitangshu.supakar@philips.com>
Date: 2019-12-03T03:52:17-05:00

--- Latest Reply ---
Here are the actions summary and suggestions  as per today’s discussion . Also attaching the evidences of changes already done.
Thanks Datta for your suggestions and ideas to streamline this further, will definitely reach to you for further discussion.

@Sundar – Please confirm if this is sufficient to close the contingency actions …

SL      Practice        Contingency Actions     Actual closure summary
1       Compiler Warning        Add gate to prevent warning count increasing (for example, by lowering the max each time the count falls)       Established Dynamic Compiler Warning Gate
2       Compiler Warning         Add count trending on suppressions     1) "@SuppressWarnings" Scan completed  and suppression count baselined
2) This will be monitored vis KPI dashboard & CCB
3       Compiler Warning        Add static rule (might be custom) to prevent a local warning suppression without a rationale
4       Code Duplication        Code dup: Reduce the token count and baseline from now onwards on new code  ( On the new code, the TC should be 50). Consider Relative  For Java projects default is 10 statements Non java projects this is set to 50.

Suggestions for further improvement in 2020
1)      Compiler warning :  Acknowledge all “new” suppressions in code itself. Fail the build/check-in if suppressions are not acknowledges with justification.  This is also reviewed during code review
2)      Code Duplication : Deploy JSCPD to scan JAVA code in addition to Sonar, daily reports can be stored in separate file and integrate with quality gate


Regards
Binu

--- Previous Message (1) ---
Original Appointment-----

--- Previous Message (2) ---
Sent: 2019 Nov 29 3:57 PM
To: Orakkan, Binu; Vellal, Dattatreya; Kannanth, Amrithraj
Cc: Jagadeesan, Sundaresan
Subject: HSDP Contingency Action Clarifications
When: 2019 Dec 03 12:30 PM-1:00 PM (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi.
Where: 1A-1-4


< Meeting placeholder>



  ________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.


--- Attachments ---
  [Contingent_Actions(HSDP-DP).xlsx] (application/octet-stream, 377146 bytes)
    Saved: data/email_attachments/RE  HSDP Contingency Action Clarifications /Contingent_Actions(HSDP-DP).xlsx
```
# Evidence: Lombok to boiler code elimination

## Source
- **File:** `Lombok to boiler code elimination.msg`
- **Date:** 2019-09-09
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "Vellal, Dattatreya" <dsvellal@philips.com>
- **To:** "ZHANG; Mike" <Jian.zhang@philips.com>; "Jiang; Chao"	<chao.jiang@philips.com>
- **CC:** "Williams; Simao" <simao.williams@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>; "Vellal; Dattatreya" <dsvellal@philips.com>
- **Date:** 2019-09-09T07:14:35-04:00
- **Thread depth:** 3
- **Is reply:** False

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Author

## Key Quotes
> From: "Vellal, Dattatreya" <dsvellal@philips.com>

> CC: "Williams; Simao" <simao.williams@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>; "Vellal; Dattatreya" <dsvellal@philips.com>

> Thank you for considering exploring jscpd as a tool to identify copy-paste detection.

> Dattatreya S Vellal | Competency Specialist – Software Excellence | Software Center of Excellence | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

## Full Email Content

```
Subject: Lombok to boiler code elimination
From: "Vellal, Dattatreya" <dsvellal@philips.com>
To: "ZHANG; Mike" <Jian.zhang@philips.com>; "Jiang; Chao"	<chao.jiang@philips.com>
CC: "Williams; Simao" <simao.williams@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>; "Vellal; Dattatreya" <dsvellal@philips.com>
Date: 2019-09-09T07:14:35-04:00

--- Latest Reply ---
Hello Mike,
Thank you for considering exploring jscpd as a tool to identify copy-paste detection.

While we were going through the duplicates reported by jscpd, we noticed a common pattern of duplication, which is – getters and setters. Since the codebase is in java, I would like to suggest a way of taking away the boiler plate code (getters, setters, no-constructor-arguments, all-constructor-arguments, builders, toString() etc.), that is by utilizing a jar called: Lombok: https://projectlombok.org/<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fprojectlombok.org%2F&data=02%7C01%7C%7C31f4d01d4f1a4dd1511108d73516e596%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C637036244765365554&sdata=%2BQMAFAUuwS7KzAWLCG1jrd%2FmQ%2F1ZB8rbkgB%2BWKDhsQ0%3D&reserved=0>

Lombok adds compile-time code to all the java files, via annotations. This works on all IDEs and needs to be added to your classpath (via the gradle file).

With this you can consider addressing almost all your boilerplate code, and replace them via annotations. Plus, you don’t have to write test-cases for the compiled code, jacoco automatically reports it as fully covered, if not, you can do so by adding a property into your project, defined here: https://www.rainerhahnekamp.com/en/ignoring-lombok-code-in-jacoco/<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.rainerhahnekamp.com%2Fen%2Fignoring-lombok-code-in-jacoco%2F&data=02%7C01%7C%7C31f4d01d4f1a4dd1511108d73516e596%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C637036244765375552&sdata=QAC5Vq8qe3wgIljpMeYqvTnCEkxJ%2BlOSuhgw6eD13Mw%3D&reserved=0>

Here are the more popular features of Lombok: https://projectlombok.org/features/all<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fprojectlombok.org%2Ffeatures%2Fall&data=02%7C01%7C%7C31f4d01d4f1a4dd1511108d73516e596%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C637036244765385545&sdata=MzWPpyAYy%2FnSGxcpHFDVDR89a2sGxezfhzQAIlGCUDU%3D&reserved=0>

Kindly consider using this in your projects. Let me know if you need any help, I will be happy to help.

--- Previous Message (1) ---
Datta
Dattatreya S Vellal | Competency Specialist – Software Excellence | Software Center of Excellence | dsvellal@philips.com<mailto:dsvellal@philips.com> | +919972312693

--- Previous Message (2) ---
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.
```
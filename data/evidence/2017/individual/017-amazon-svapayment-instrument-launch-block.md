---
title: "SVAPayment Instrument Launch Block"
date: 2017-07-01
year: 2017
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: ["Hari"]
skills: ["AWS", "Documentation", "Fraud Detection"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: SVAPayment Instrument Launch Block

## Source
- **File:** `201707_SVAPaymentInstrumentLaunchBlock.pdf`
- **Date:** 2017-07-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Amazon)
- **Category:** Recognition

## Metadata
- **Type:** Email
- **Organization:** Amazon (TRMS - Transaction Risk Management Services)
- **Pages:** 3

## Datta's Involvement
- **Role at time:** SDE-2 (Software Development Engineer II)
- **Involvement type:** Direct Recipient

## Key Quotes
> Thursday, November 9, 2017 at 3:46:40 PM India Standard Time

## Full Content
```
Thursday, November 9, 2017 at 3:46:40 PM India Standard Time
Subject:Ticket 0119244813 - Correspondence - Status Assigned - [AUTOCUT] [FortressBackend] High
Severity Issue in Digital Fraud System(s)
Date: Wednesday, 26 July 2017 at 10:34:26 AM India Standard Time
From: vinaych@amazon.com
To: Kumar, Rohit
CC: Kapoor, Aditya, Andersen, Kelley, Chebolu, Guru Murthy Venkata Satya, Arora, Gaurav, Chadha,
Mayank, trms-aps-primary@amazon.com, Adit, Kumar, Fadlallah, Bilal, Jones, Chris, Verma,
Animesh, Okely, Daniel, O[a, Amit, Shariff, Mohammed Jeelan, Chole], Vinay, lpa-in-dev,
Kumar, Akhil
Detailed ^cket informa^on:
h[p://[.amazon.com/0119244813
Correspondence:
Entered by vinaych at 07/25/2017 10:04:01 PM
Thanks Da[a for relentlessly pursuing this or the last 2 days and ge]ng to the root cause and the solu^on.
Entered by da[atrv at 07/25/2017 07:57:22 AM
Yes. From FDPS's end, the fix for the problem iden^fied by this ^cket is working & confirmed via FBS logs via the
paste link. This should be good to push to prod tonight.
Entered by chebolug at 07/25/2017 06:42:38 AM
Reply sent by email:
Hi Da[a, can we take this as a confirma^on that fix is working fine and good to push to prod tonight
Sent from my iPhone
Entered by da[atrv at 07/25/2017 06:23:01 AM
Please ignore my previous comment.
The persistence in FDPS is successful. Please find the logs here:
h[ps://paste.amazon.com/show/da[atrv/1500988950
Entered by da[atrv at 07/25/2017 06:18:37 AM
Our ^mber logs confirms that the order was received at FBS:
25 Jul 2017 11:55:13,885 [INFO] 3f9fd69e-64df-538b-8a14-876f573e0923 (processorScheduler--pool-41-thread-
1) com.amazon.fortressbackend.ac^vity.ProcessPYOPMessageAc^vity: ProcessPYOPMessage
received=GenericSNSMessage{message={"MWSTransac^onId":"P04-9394354-8452594-
C025043","marketplaceId":"136321","messageType":"PaymentsNo^fica^on","paymentContractId":"P04-
9394354-8452594"}, subject=PaymentCapture, signatureVersion=1, ^mestamp=2017-07-25T11:55:13.817Z,
signingCertURL=h[ps://sns.eu-west-1.amazonaws.com/SimpleNo^fica^onService-
b95095beb82e8f6a046b3aafc7f4149a.pem, topicArn=arn:aws:sns:eu-west-
1:358749047772:prod_EUAmazon_No^fica^ons, type=No^fica^on, unsubscribeURL=h[ps://sns.eu-west-
1.amazonaws.com/?Ac^on=Unsubscribe&Subscrip^onArn=arn:aws:sns:eu-west-
1:358749047772:prod_EUAmazon_No^fica^ons:b1c8883c-7c70-4418-b961-b3ad1507ff62,
subscribeURL=&lt;null&gt;, messageId=3f9fd69e-64df-538b-8a14-876f573e0923,
signature=Do7yWeTr4pZUKTfo33yDx+CNUHcssU/6BmbknFJuchT+7mKs4Qy18mfA2i8Jac3UhlMNmkpJxRHkrLBm+
dUJJ6Gt97yd9b/M2pWfpkybf0Xqwy4wP3PVhgfqE5OR5T7HUMHJ5QuBlK9Zznw0Ria4I/biLH
Page 1 of 3
dUJJ6Gt97yd9b/M2pWfpkybf0Xqwy4wP3PVhgfqE5OR5T7HUMHJ5QuBlK9Zznw0Ria4I/biLH
--------Correspondence is truncated (in email only)-----------
Short Descrip^on:
[AUTOCUT] [FortressBackend] High Severity Issue in Digital Fraud System(s)
Details:
Please click on the dependent monitor(s) of this parent monitor that are in alarm and read through the
descrip^on of the monitor for more info and the specific SOP.
The root wiki that lists all the SOPs for Digital Fraud sev-2 ^ckets is here -
h[ps://w.amazon.com/index.php/DigitalFraud/TTSOP.
***IMP NOTE***
Please DO NOT leave a sev-2 in WIP/Pending for a long ^me when not ac^vely working on the ^cket. If you are
wai^ng to verify a fix, put the ^cket in Pending but check the top-level monitor regularly (15 mins) for any new
problems. Resolve the sev-2 promptly azer the top-level goes green.
To see Carnaval monitor: h[p://carnaval.amazon.com/v1/viewObject.do?
type=monitor&name=DigitalFraud.FBS.SEV2.EU
To see Carnaval history: h[p://carnaval.amazon.com/v1/viewHistory.do?
type=monitor&name=DigitalFraud.FBS.SEV2.EU
To see Carnaval snapshot: h[p://carnaval.amazon.com/v1/viewSnapshot.do?^mestamp=2017-07-
21+07%3A35%3A57.950&name=DigitalFraud.FBS.SEV2.EU
------------------------------------------------
Monitor: DigitalFraud.FBS.SEV2.EU (17112767)
Status: ALERT
Descrip^on: High level monitor to group all Digital Fraud sev-2s.
Suppo
```

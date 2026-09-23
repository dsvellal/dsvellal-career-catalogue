# 201704 OAPCNonMandatoryFieldLaunchUnblock

> Converted from document `201704_OAPCNonMandatoryFieldLaunchUnblock.pdf`

Friday, October 13, 2017 at 5:55:33 PM India Standard Time

Subject: Re: Incomplete response from CCS
Date: Thursday, 13 April 2017 at 10:16:23 AM India Standard Time
From: CholeB, Vinay
To:
Kapoor, Aditya, Pal, Sandip Kumar, Jegannathan, Balasubramanian, Vellal, DaKatreya, Nagesh,
Harsha
CC:
Jain, Manish, Naik, Rajesh, Shukla, Ankur, Chebolu, Guru Murthy Venkata Satya, Goel, Akash
Grear stuff. Congratulations.
Thanks,
Vinay

From: "Kapoor, Aditya" <kapoorak@amazon.com>
Date: Wednesday, 12 April 2017 at 4:10 PM
To: "Pal, Sandip Kumar" <sandippa@amazon.com>, "Jegannathan, Balasubramanian"
<balasubj@amazon.com>, "Vellal, DaKatreya" <daKatrv@amazon.com>, "Nagesh, Harsha"
<nharsha@amazon.com>, "CholeB, Vinay" <vinaych@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "Chebolu, Guru Murthy Venkata Satya"
<chebolug@amazon.com>, "Goel, Akash" <goelakas@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>
Subject: Re: Incomplete response from CCS
Great news !!!. Good job Team. Smooth integra\on is tes\mony on good design.
Based on our internal tes\ng, We would be able to support upto 1000 TPS with our current infra.
Thanks
Aditya

From: "Pal, Sandip Kumar" <sandippa@amazon.com>
Date: Wednesday, April 12, 2017 at 3:49 PM
To: "Jegannathan, Balasubramanian" <balasubj@amazon.com>, DaKatreya Vellal
<daKatrv@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>, "Kapoor,
Aditya" <kapoorak@amazon.com>, "Goel, Akash" <goelakas@amazon.com>
Subject: Re: Incomplete response from CCS
Hi Bala/DaKa,
We just did a registra\on and checked the whole E2E ﬂow and it suspended 3 accounts successfully.
I checked the same in our DynamoDB table and the states of these accounts are SUSPENDED, and we
have the proper reason code and requester data.
Thanks,
Sandip

From: "Goel, Akash" <goelakas@amazon.com>
Page 1 of 8

Date: Wednesday, April 12, 2017 at 11:51 AM
To: Balasubramanian Jagannathan <balasubj@amazon.com>, "Pal, Sandip Kumar"
<sandippa@amazon.com>, "Vellal, DaKatreya" <daKatrv@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, Ankur
Shukla <ankshuk@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>, "Kapoor,
Aditya" <kapoorak@amazon.com>
Subject: Re: Incomplete response from CCS
Hi Bala,
I’ve invited Sandip and Ankur for the E2E tes\ng today at 2.30 PM.
Regards,
Akash

From: "Jegannathan, Balasubramanian" <balasubj@amazon.com>
Date: Wednesday, 12 April 2017 at 11:50
To: "Pal, Sandip Kumar" <sandippa@amazon.com>, "Vellal, DaKatreya" <daKatrv@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>, "Kapoor,
Aditya" <kapoorak@amazon.com>, "Goel, Akash" <goelakas@amazon.com>
Subject: Re: Incomplete response from CCS
Thanks for the update Sandip.
We are able to successfully make the call from SVA plaform to TRMSOrchestrator service.
DaKa/Akash,
Do let us know what \me you would be ready to con\nue the integra\on test today so that we can
conﬁrm that everything is working on your end as well.
Also, we would need to do the last integra\on test which includes calling the StateManagement API from
TRMS end. Do let us know when we can complete this leg of integra\on test.
-Bala K J

From: "Pal, Sandip Kumar" <sandippa@amazon.com>
Date: Wednesday, April 12, 2017 at 11:37 AM
To: "Vellal, DaKatreya" <daKatrv@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>,
"Jegannathan, Balasubramanian" <balasubj@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>, "Goel, Akash" <goelakas@amazon.com>
Subject: Re: Incomplete response from CCS
Hi DaKa,
Last day we did a registra\on and we were able to call TRMSOrchestrator service successfully.
A2C73OF9P3XJV0 is the customer id which we registered.

Page 2 of 8

A2C73OF9P3XJV0 is the customer id which we registered.
And below are the related customer ids which have ac\ve SVA accounts.
A2R0F9MP5XCCE2
A3TP3TMYACLWKJ
A22AUILN1VI7HG
A349928O0ISL4
A2JU8WS1DYBAQ7
A2L228NB3PN6LU
52cba406-9082-4058-a49e-f86ce2b17041 is the transac\on id we got as a response.
But Akash informed that IW was facing an issue as it expects unencrypted customer ids. He will make the
ﬁx and we will do another round of E2E today.
Thanks,
Sandip

From: "Vellal, DaKatreya" <daKatrv@amazon.com>
Date: Monday, April 10, 2017 at 7:13 PM
To: "Pal, Sandip Kumar" <sandippa@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, Ankur
Shukla <ankshuk@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>,
Balasubramanian Jagannathan <balasubj@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Goel, Akash" <goelakas@amazon.com>
Subject: Re: Incomplete response from CCS
Hi Sandip,
As I checked our pipeline, the code has gone to prod at around 7pm. I’d suggest going forward, let’s do a
co-ordinated integra\on test so that we can catch issues and mi\gate them faster. Please book some \me
on the calendar, like we did last week, and we can do the integra\on test together.
As discussed over chat, Akash (goelakash@) will be our point of contact for integra\on tes\ng. Please
keep him in loop when seBng up this \me.
Regards,
DaKa
DaKatreya S Vellal | TRMS | daKatrv@amazon.com | +91-9972312693

From: "Pal, Sandip Kumar" <sandippa@amazon.com>
Date: Monday, 10 April 2017 at 6:19 PM
To: "Vellal, DaKatreya" <daKatrv@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "trms-dev-core-inpay@amazon.com" <trms-dev-coreinpay@amazon.com>, "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>,
"Jegannathan, Balasubramanian" <balasubj@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>
Subject: Re: Incomplete response from CCS
Page 3 of 8

Hi DaKa,
Can you please conﬁrm if your changes are in prod or not? Because we tried a registra\on today and got
valida\on excep\on due to null rela\on type.
We are geBng this excep\on“com.amazon.similaritychecker.connector.TRMSOrchestratorServiceConnector: Star\ng
InvokeOneAccountPerCustomerCheck for customerId A2C73OF9P3XJV0.
10 Apr 2017 12:35:24,870 ^[[32m[INFO]^[[m (pool-6-thread-4)
com.amazon.similaritychecker.processor.AmazonKinesisCCSRecordProcessor: Event with idempotencyId
SVA_A2C73OF9P3XJV0.6024850014348253 threw an excep\on.
com.amazon.coral.validate.Valida\onExcep\on: 6 valida\on errors detected: Value null at
'relatedCustomers.1.member.rela\onType' failed to sa\sfy constraint: Member must not be null; Value
null at 'relatedCustomers.2.member.rela\onType' failed to sa\sfy constraint: Member must not be null;
Value null at 'relatedCustomers.3.member.rela\onType' failed to sa\sfy constraint: Member must not be
null; Value null at 'relatedCustomers.4.member.rela\onType' failed to sa\sfy constraint: Member must
not be null; Value null at 'relatedCustomers.5.member.rela\onType' failed to sa\sfy constraint: Member
must not be null; Value null at 'relatedCustomers.6.member.rela\onType' failed to sa\sfy constraint:
Member must not be null”
Thanks,
Sandip

From: "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>
Date: Friday, April 7, 2017 at 3:10 PM
To: "Vellal, DaKatreya" <daKatrv@amazon.com>, Balasubramanian Jagannathan
<balasubj@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, Ankur
Shukla <ankshuk@amazon.com>, "Pal, Sandip Kumar" <sandippa@amazon.com>, "trms-dev-coreinpay@amazon.com" <trms-dev-core-inpay@amazon.com>
Subject: Re: Incomplete response from CCS
Thanks DaKa.
@Bala, on our side, I think we should start making the changes to make it op\onal.
Thanks,
Guru Murthy Chebolu,
Sr. TPM, India Payments.
M: (+91) 9880 267 457

From: "Vellal, DaKatreya" <daKatrv@amazon.com>
Date: Friday, April 7, 2017 at 3:09 PM
To: Guru Chebolu <chebolug@amazon.com>, "Jegannathan, Balasubramanian"
<balasubj@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, Rajesh Naik <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "Pal, Sandip Kumar" <sandippa@amazon.com>, "trms-dev-coreinpay@amazon.com" <trms-dev-core-inpay@amazon.com>
Subject: Re: Incomplete response from CCS
Hi Guru,
Page 4 of 8

We are working towards making this non-mandatory. This means, if you have the values, pass it, and we’ll
validate them, if you don’t have the values, keep them null, and we’ll con\nue to process the request. CR:
hKps://cr.amazon.com/r/6938561/
Regards,
DaKa
DaKatreya S Vellal | TRMS | daKatrv@amazon.com | +91-9972312693

From: "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>
Date: Friday, 7 April 2017 at 3:00 PM
To: "Jegannathan, Balasubramanian" <balasubj@amazon.com>, "Vellal, DaKatreya"
<daKatrv@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>
Cc: "Jain, Manish" <manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla,
Ankur" <ankshuk@amazon.com>, "Pal, Sandip Kumar" <sandippa@amazon.com>, "trms-dev-coreinpay@amazon.com" <trms-dev-core-inpay@amazon.com>
Subject: Re: Incomplete response from CCS
Aditya,
Can you please conﬁrm whether rela\onalDataList values is a mandatory parameter for TRMS or not?
Based on this response, we will plan the next steps.
Thanks,
Guru Murthy Chebolu,
Sr. TPM, India Payments.
M: (+91) 9880 267 457

From: "Jegannathan, Balasubramanian" <balasubj@amazon.com>
Date: Thursday, April 6, 2017 at 6:38 PM
To: "Vellal, DaKatreya" <daKatrv@amazon.com>
Cc: "Kapoor, Aditya" <kapoorak@amazon.com>, "Jain, Manish" <manijain@amazon.com>, Rajesh
Naik <rajeshn@amazon.com>, "Shukla, Ankur" <ankshuk@amazon.com>, "Pal, Sandip Kumar"
<sandippa@amazon.com>, Guru Chebolu <chebolug@amazon.com>, "trms-dev-coreinpay@amazon.com" <trms-dev-core-inpay@amazon.com>
Subject: Re: Incomplete response from CCS
Hi DaKa,
The only data-setup that we are doing from our end is ensuring that there are mul\ple customers
having same address and payment instrument(CreditCard). If there was any issue with the
customer data then I don't think we would even have got the related customer list. We would have
to wait for the answer from the CCS team to understand why the rela\onDataList is 0 when there
are relevant customers.
Can you let us know why you would need the rela\onDataList as Aditya was men\oning that this
might not be necessary and can be fetched later within the TRMSOrchestrator service?
Bala K J

Page 5 of 8

Sent from my iPhone
On 06-Apr-2017, at 6:24 PM, Vellal, DaKatreya <daKatrv@amazon.com> wrote:
Sure.
When the integra\on test was done on the beta environment, we didn’t see this behaviour
(rela\onDataList being 0). So the concern is:
1. If the beta-test-data did not result in this behaviour, why is the prod-test-data
resul\ng in this behaviour?
2. Which data-set is correct, beta-test-data? Or prod-test-data?
I believe answers to the above ques\ons will ensure that we are not erring from test-datasetup perspec\ve.
Regards,
DaKa
DaKatreya S Vellal | TRMS | daKatrv@amazon.com | +91-9972312693

From: "Jegannathan, Balasubramanian" <balasubj@amazon.com>
Date: Thursday, 6 April 2017 at 6:15 PM
To: "Vellal, DaKatreya" <daKatrv@amazon.com>
Cc: "Kapoor, Aditya" <kapoorak@amazon.com>, "Jain, Manish"
<manijain@amazon.com>, "Naik, Rajesh" <rajeshn@amazon.com>, "Shukla, Ankur"
<ankshuk@amazon.com>, "Pal, Sandip Kumar" <sandippa@amazon.com>, "Chebolu,
Guru Murthy Venkata Satya" <chebolug@amazon.com>
Subject: Re: Incomplete response from CCS
Hi DaKa,
Can you clarify on what you refer to as data-setup error?
Bala K J
Sent from my iPhone
On 06-Apr-2017, at 6:03 PM, Vellal, DaKatreya <daKatrv@amazon.com> wrote:
Hi Bala,
Can you also ensure that this is not a data-setup error, since the team did not
no\ce this behaviour in beta, while doing an end-end tes\ng?
Regards,
DaKa
DaKatreya S Vellal | TRMS | daKatrv@amazon.com | +91-9972312693

From: "Chebolu, Guru Murthy Venkata Satya" <chebolug@amazon.com>
Date: Thursday, 6 April 2017 at 5:55 PM
To: "Jegannathan, Balasubramanian" <balasubj@amazon.com>
Page 6 of 8

Cc: "Kapoor, Aditya" <kapoorak@amazon.com>, "Vellal, DaKatreya"
<daKatrv@amazon.com>, "Jain, Manish" <manijain@amazon.com>,
"Naik, Rajesh" <rajeshn@amazon.com>, "Shukla, Ankur"
<ankshuk@amazon.com>, "Pal, Sandip Kumar" <sandippa@amazon.com>
Subject: Re: Incomplete response from CCS
Why we didn't open TT
Sent from my iPhone
On 06-Apr-2017, at 5:46 PM, Jegannathan, Balasubramanian
<balasubj@amazon.com> wrote:
Hi Aditya,
Here are the logs that we were able to pull from the Integra\on
test that we did on One-Customer-Per-Account project.
As you can see the “rela\onDataList” size is returned as 0 even
though we have valid related IDs for the original CustomerID.
I’ve opened an Issue SIM with them on this hKps://issuespdx.amazon.com/issues/P7157418.
The other ques\on that we were discussing is that, why would the
TRMSOrchestrator service need the Rela\onDataList. If you can
clarify this, then we would need to re-look on how we can avoid
including the Rela\onDataList parameter.
-Bala K J

From: "Pal, Sandip Kumar" <sandippa@amazon.com>
Date: Thursday, April 6, 2017 at 5:34 PM
To: "Jegannathan, Balasubramanian"
<balasubj@amazon.com>
Cc: "Shukla, Ankur" <ankshuk@amazon.com>
Subject: Incomplete response from CCS
Original custId: A2C73OF9P3XJV0
Related Id:
A2QYZCNOYOU6CK
A34UYIX6FWEQRL
A22AUILN1VI7HG
AYZGZ4HLOSLAD
A3TP3TMYACLWKJ
A3RPKJR1PYZ38X
A2R0F9MP5XCCE2
A2L228NB3PN6LU
A30IY1UYNSMD08
A1YTY4D4T4WI0B
A2JU8WS1DYBAQ7
Page 7 of 8

A2KTDPFMIN71T
A1OOYC3NVOXC5I
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A2QYZCNOYOU6CK with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A34UYIX6FWEQRL with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A22AUILN1VI7HG with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:AYZGZ4HLOSLAD with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A3TP3TMYACLWKJ with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A3RPKJR1PYZ38X with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A2R0F9MP5XCCE2 with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A2L228NB3PN6LU with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A30IY1UYNSMD08 with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A1YTY4D4T4WI0B with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A2JU8WS1DYBAQ7 with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A2KTDPFMIN71T with rela\onDataList size 0
06 Apr 2017 11:50:45,210 ^[[32m[INFO]^[[m (pool-6-thread-1)
com.amazon.similaritychecker.connector.CustomerClusteringServi
ceConnector: RC:A1OOYC3NVOXC5I with rela\onDataList size 0

Page 8 of 8


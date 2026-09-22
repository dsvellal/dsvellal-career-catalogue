# 201707 AmazonPayPPIUnblock AppreciationFromHarsha

> Converted from document `201707_AmazonPayPPIUnblock_AppreciationFromHarsha.pdf`

Thursday, November 9, 2017 at 4:06:15 PM India Standard Time

Subject: RE: Update on -: 0119244813
Date: Tuesday, 25 July 2017 at 2:33:39 PM India Standard Time
From: Nagesh, Harsha
To:
Vellal, Da-atreya, CholeL, Vinay
CC:
Chadha, Mayank, Kapoor, Aditya, B. K., Balachandra, Reddy, Rajesh Kodhihalli
Thanks Aditya and Da-a and the IN team for arriving at this resoluVon, which is simple and right.
From: Vellal, Da-atreya
Sent: Tuesday, July 25, 2017 2:32 PM
To: CholeL, Vinay <vinaych@amazon.com>; Nagesh, Harsha <nharsha@amazon.com>
Cc: Chadha, Mayank <chadham@amazon.com>; Kapoor, Aditya <kapoorak@amazon.com>; B. K.,
Balachandra <balakr@amazon.com>; Reddy, Rajesh Kodhihalli <rerajesh@amazon.com>
Subject: Re: Update on -: 0119244813
Hello Vinay, Harsha,
Aditya and I had a conversaVon with Mayank & Rakesh. From all the data points that we have
accumulated, the suggesVon given below holds. We are not making any code change at our end. Rakesh
is going to change the PaymentMethod to “Unknown” and set the RawPaymentMethod to “IndiaSVA”.
The Vcket has been assigned to LPA-IN-EPS CTI.
Regards,
Da-a
Da-atreya S Vellal | TRMS | da-atrv@amazon.com | +91-9972312693

From: "Vellal, Da-atreya" <da-atrv@amazon.com>
Date: Tuesday, 25 July 2017 at 1:22 PM
To: "CholeL, Vinay" <vinaych@amazon.com>
Cc: "Chadha, Mayank" <chadham@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>,
"Balachandra B. K." <balakr@amazon.com>, "Nagesh, Harsha" <nharsha@amazon.com>, "Reddy,
Rajesh Kodhihalli" <rerajesh@amazon.com>
Subject: Re: Update on -: 0119244813
Hi Vinay,
Quick update on the Vcket.
I have inspected a retail order with SVA as a payment instrument, and a digital order with SVA as a
payment instrument. In both of the cases, the PaymentMethod is set as “Unknown” & the
rawPaymentMethod is set as “IndiaSVA”. This is also in sync with the FraudAnalyVcs rules wri-en for
IndiaSVA, as pointed out by Akhil, in the Vcket.
The suggesVon for PyOP orders, is also to set the PaymentMethod as “Unkonwn” & rawPaymentMethod
as “IndiaSVA”. With the asserVon of both digital and retail orders following the same path (of seLng
PaymentMethod as Unknown & rawPaymentMethod as IndiaSVA), this suggesVon is not a hack, but is an
expected behaviour. Also, we really do not know why “StoredValue” was set in PyOP as the
PaymentMethod in the ﬁrst place. For PyOP orders, populaVng the PaymentMethod as Unknown &
rawPaymentMethod as IndiaSVA will keep the behaviour of all the orders ﬂowing through Fortress
(digital) and BFS (retail) in sync & will not alter any of the variable computaVon or fraud analyVcs code.

Page 1 of 4

CreaVng a new PaymentMethod for IndiaSVA, requires discussion with the plaqorm team.
I have updated the Vcket with all the details & links to FraudDocuments for Retail, Digital & PyOP orders.
Next discussion is with Mayank at 2pm, when he is done with his meeVngs.
Regards,
Da-a
Da-atreya S Vellal | TRMS | da-atrv@amazon.com | +91-9972312693

From: "Vellal, Da-atreya" <da-atrv@amazon.com>
Date: Tuesday, 25 July 2017 at 10:10 AM
To: "CholeL, Vinay" <vinaych@amazon.com>
Cc: "Chadha, Mayank" <chadham@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>,
"Balachandra B. K." <balakr@amazon.com>, "Nagesh, Harsha" <nharsha@amazon.com>, "Reddy,
Rajesh Kodhihalli" <rerajesh@amazon.com>
Subject: Re: Update on -: 0119244813
Yes. I have updated the Vcket with the next steps.
Regards,
Da-a
Da-atreya S Vellal | TRMS | da-atrv@amazon.com | +91-9972312693

From: "CholeL, Vinay" <vinaych@amazon.com>
Date: Tuesday, 25 July 2017 at 10:09 AM
To: "Vellal, Da-atreya" <da-atrv@amazon.com>
Cc: "Chadha, Mayank" <chadham@amazon.com>, "Kapoor, Aditya" <kapoorak@amazon.com>,
"Balachandra B. K." <balakr@amazon.com>, "Nagesh, Harsha" <nharsha@amazon.com>, "Reddy,
Rajesh Kodhihalli" <rerajesh@amazon.com>
Subject: Re: Update on -: 0119244813
Can you update the Vcket please?
Thanks,
Vinay
Sent from my iPhone
On 25-Jul-2017, at 10:06 AM, Vellal, Da-atreya <da-atrv@amazon.com> wrote:
Hi Vinay,
I am working on two streams
1. Check with FortressSIL team (kagupta@/ramanp@/pardeku@) to see if we have a
reason why a previous inclusion of “IndiaSVA” was reverted.
2. Follow up with Pardeep (pardeku@) to see how Fortress computes
paymenVnstrumen-ype variable and see if “PaymentMethod” is criVcal or not in this
case. This will help us ascertain the answer to Akhil’s quesVons.
I will have an answers for these by 12pm today.
Page 2 of 4

Regards,
Da-a
Da-atreya S Vellal | TRMS | da-atrv@amazon.com | +91-9972312693

From: "CholeL, Vinay" <vinaych@amazon.com>
Date: Tuesday, 25 July 2017 at 8:46 AM
To: "Vellal, Da-atreya" <da-atrv@amazon.com>
Cc: "Chadha, Mayank" <chadham@amazon.com>, "Kapoor, Aditya"
<kapoorak@amazon.com>, "Balachandra B. K." <balakr@amazon.com>, "Nagesh,
Harsha" <nharsha@amazon.com>, "Reddy, Rajesh Kodhihalli"
<rerajesh@amazon.com>
Subject: Re: Update on -: 0119244813
Da-a/Aditya,
What are the next steps in this?
Thanks,
Vinay
Sent from my iPhone
On 25-Jul-2017, at 6:15 AM, CholeL, Vinay <vinaych@amazon.com> wrote:
Thanks Da-a. When can we do this and who needs to check this possible
issue in fortress?
Also, when you menVon Fortress or BFS team, Can you pls menVon the
name of the person in brackets against that team . It helps me put a face
against that team.
Thanks,
Vinay
Sent from my iPhone
On 25-Jul-2017, at 5:20 AM, Vellal, Da-atreya <da-atrv@amazon.com>
wrote:
Hi,
I was following up with Vinay et al Vll 12.30am, must have slept
oﬀ. I noVced that BFS team responded back to the CR:
h-ps://cr.amazon.com/r/7449685/, where they have pointed out
an old CR: h-ps://cr.amazon.com/r/4996150/ which had similar
changes, but was reverted in FortressSIL. I need to talk to the
Fortress team to see if this would cause any issues. If yes, why &
then take this forward.
Ticket has been updated.
Page 3 of 4

Regards,
Da-a
Da-atreya S Vellal | TRMS | da-atrv@amazon.com | +919972312693

Page 4 of 4


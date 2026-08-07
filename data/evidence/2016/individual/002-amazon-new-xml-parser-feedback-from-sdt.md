---
title: "New XML Parser Feedback From SDT"
date: 2016-05-01
year: 2016
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: ["Hari", "Thiru"]
skills: ["Testing", "XML Processing"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: New XML Parser Feedback From SDT

## Source
- **File:** `201605_New_XML_Parser_Feedback_From_SDT.pdf`
- **Date:** 2016-05-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Amazon)
- **Category:** Recognition

## Metadata
- **Type:** Email
- **Organization:** Amazon (TRMS - Transaction Risk Management Services)
- **Pages:** 2

## Datta's Involvement
- **Role at time:** SDE-2 (Software Development Engineer II)
- **Involvement type:** Direct Recipient

## Key Quotes
> Friday, July 15, 2016 at 7:59:22 PM India Standard Time

## Full Content
```
Friday, July 15, 2016 at 7:59:22 PM India Standard Time
Subject: Re: New parser implementa0on feedback
Date: Monday, May 2, 2016 at 2:07:13 PM India Standard Time
From: PoliseDy, Hari
To: R, Hariharan, Vellal, DaDatreya, Mohan, Thanigaivel
CC: Sankaran, Thiruvenkatakrishnan, Dhanasekaran, Manivannan
Thanks for the valuable feedback Hari. We are very happy to hear that this feature has simplified the Caffeine
implementa0on.
Good work DaDa.
From: Hariharan R <rhari@amazon.com>
Date: Thursday, April 28, 2016 at 12:02 PM
To: DaDatreya S Vellal <daDatrv@amazon.com>, Hari PoliseDy <hpoliset@amazon.com>, Thanigaivel
Mohan <thanigm@amazon.com>
Cc: Hariharan R <rhari@amazon.com>, "Sankaran, Thiruvenkatakrishnan" <tsankar@amazon.com>,
Manivannan Dhanasekaran <manivand@amazon.com>
Subject: New parser implementa0on feedback
Hi Team,
TL;DR The new parser implementa0on rocks and code is more readable and easy to understand !!
The new parser implementa0on has enabled us to write code that are beDer to understand and therefore easy to
maintain. In my experience with GDSN 3.1 migra0on, we had to write lots of code for verifying whether a xml tag has
an xml aDribute or not and therefore write code accordingly. And we may never know when the vendor might send
an xml tag with an aDribute and without it. So we need to make sure we cover all the edge cases and therefore the
code complexity increases. One such complex condi0on to check is men0oned below. The below piece of code is
mandatory with the old parser, because of the complica0ons created by the json data that it output.
//code
if (attribute_value_struct instanceof Array && attribute_value_struct.length >=
2 && helper.isString(attribute_value_struct[0])) {
if (!!attribute_value_struct[1] && attribute_value_struct[1].$name ===
lookup_key && !!attribute_value_struct[0]) {
return [attribute_value_struct[0]];
}
}
//json data
"compoundStringAVP": [
[
"test",
{
"$attributeCode": "DAY",
"$attributeName": "itemPeriodSafeToUseAfterOpening",
"$codeListNameCode": "MEASUREMENT_CODE",
"$codeListVersion": "1"
}
]
Page 1 of 2
But now, with the new parser, we can write code without worrying about the xml aDribute data, as it is taken care by
the new parser. A lot of redundant code seems to have disappeared now from GDSN3.1 caffeine code because of the
new parser. The code is a lot more readable now. (Trust me, having hell a lot of 'if' condi0ons such as the above one i
n every compute func0on seems ridiculous). We now also have the ability to add more direct mappings as the need f
or the above 'if' condi0on is out of place. We are able to deal with an xml tag consistently in the same way throughou
t out our implementa0on regardless of whether it has a xml tag or not.
Special thanks to Thani who migrated the exis0ng GDSN logic saving me from addi0onal work :)
Thank you very much for your support. Looking forward to more features :)
-H
Hari | Hariharan. R | Application Engineer | GRCS Support | Amazon.com | India
rhari@amazon.com | +91-9176-9176-65
Page 2 of 2
```

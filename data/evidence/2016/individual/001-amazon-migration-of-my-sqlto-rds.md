---
title: "Migration Of My SQLTo RDS"
date: 2016-03-01
year: 2016
era: Amazon
organization: Amazon
category: Recognition
source_type: email
channel: email_archive
involvement: direct_recipient
role: SDE-2 (Software Development Engineer II)
people: ["Raman"]
skills: ["AWS RDS", "Documentation", "MySQL"]
programs: ["TRMS", "AmazonPay", "SVA"]
tags: ["amazon", "recognition"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Migration Of My SQLTo RDS

## Source
- **File:** `201603_MigrationOfMySQLToRDS.pdf`
- **Date:** 2016-03-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Amazon)
- **Category:** Recognition

## Metadata
- **Type:** Email
- **Organization:** Amazon (TRMS - Transaction Risk Management Services)
- **Pages:** 7

## Datta's Involvement
- **Role at time:** SDE-2 (Software Development Engineer II)
- **Involvement type:** Direct Recipient

## Key Quotes
> Friday, July 15, 2016 at 6:54:15 PM India Standard Time

## Full Content
```
Friday, July 15, 2016 at 6:54:15 PM India Standard Time
Subject: Re: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Date: Thursday, March 31, 2016 at 10:24:38 PM India Standard Time
From: Vellal, Da;atreya
To: Lansley, Chris, Vuppala, Lakshmi, O'Donnell, Kevin, Mani, Gajendran, Ramanarayanan, Sridhar
CC: Mohan, Thanigaivel, Wilkoszewski, Andrzej, Gorshunov, Vladimir
Hello Chris,
I have documented the steps followed I followed, in this wiki page:
h;ps://w.amazon.com/index.php/GRCS/Feeds/AvalancheDBMigra^onToRDS
The following is the opera^onal config loca^on of the FeedCollectorHistoryService, which lists the Avalanche
MySQL DB running in RDS: h;ps://apollo.amazon.com/opera^onal_configura^on.html?
environmentId=3031781&stage=Prod&opConfigAc^on=preview
Regards,
Da;a
From: "Lansley, Chris" <clansley@amazon.co.uk>
Date: Thursday, March 31, 2016 at 6:50 PM
To: Lakshmi Vuppala <lakshmiv@amazon.com>, "O'Donnell, Kevin" <kodonnel@amazon.co.uk>,
Gajendran Mani <gajendm@amazon.com>, Sridhar Ramanarayanan <rsridha@amazon.com>
Cc: Thanigaivel Mohan <thanigm@amazon.com>, "Wilkoszewski, Andrzej"
<andrzej@amazon.co.uk>, "Gorshunov, Vladimir" <vladimig@amazon.co.uk>, "Vellal, Da;atreya"
<da;atrv@amazon.com>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
I welcome informa^on from Da;a on how to perform a 1 day migra^on. I'm es^ma^ng 2 weeks work - so
clearly 1 days work is sounding very interes^ng.
As you were unware of CBM use of the avalanche db, have you checked if there are any other users / tables
on the db that will cause sev-2s when it is shut down?
From: Vuppala, Lakshmi
Sent: Thursday, March 31, 2016 5:12 AM
To: Lansley, Chris <clansley@amazon.co.uk>; O'Donnell, Kevin <kodonnel@amazon.co.uk>; Mani,
Gajendran <gajendm@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Page 1 of 6
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Gorshunov, Vladimir <vladimig@amazon.co.uk>; Vellal, Da;atreya <da;atrv@amazon.com>
Subject: Re: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Hello Chris & Kevin,
Yes, avalanche mysql database is also going away on April-26. For our feed collector history service which also uses
avalanche db and needs to con^nue even aner avalanche depreca^on, we have moved the relevant tables to RDS
instance. I have included Da;a who has done this migra^on to provide any details if you need. As per him, it
shouldn’t take more than a day to migrate from mysql to RDS.
Thanks,
Lakshmi.
From: Chris Lansley <clansley@amazon.co.uk>
Date: Wednesday, March 30, 2016 at 11:47 PM
To: "O'Donnell, Kevin" <kodonnel@amazon.co.uk>, "Mani, Gajendran" <gajendm@amazon.com>,
"Vuppala, Lakshmi" <lakshmiv@amazon.com>, "Ramanarayanan, Sridhar" <rsridha@amazon.com>
Cc: Thanigaivel Mohan <thanigm@amazon.com>, Andrzej Wilkoszewski <andrzej@amazon.co.uk>,
"Gorshunov, Vladimir" <vladimig@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
CBM stores it's state (possible CBMs) in the avalanche mysql database in a table called 'violator_work_items'.
From: O'Donnell, Kevin
Sent: Wednesday, March 30, 2016 7:09 PM
To: Lansley, Chris <clansley@amazon.co.uk>; Mani, Gajendran <gajendm@amazon.com>; Vuppala,
Lakshmi <lakshmiv@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Gorshunov, Vladimir <vladimig@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Chris has moved our builds over to hosts that do not seem to be on the Ap
```

# 201603 MigrationOfMySQLToRDS

> Converted from document `201603_MigrationOfMySQLToRDS.pdf`

Friday, July 15, 2016 at 6:54:15 PM India Standard Time

Subject: Re: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Date: Thursday, March 31, 2016 at 10:24:38 PM India Standard Time
From: Vellal, Da;atreya
To:
Lansley, Chris, Vuppala, Lakshmi, O'Donnell, Kevin, Mani, Gajendran, Ramanarayanan, Sridhar
CC:
Mohan, Thanigaivel, Wilkoszewski, Andrzej, Gorshunov, Vladimir
Hello Chris,
I have documented the steps followed I followed, in this wiki page:
h;ps://w.amazon.com/index.php/GRCS/Feeds/AvalancheDBMigra^onToRDS
The following is the opera^onal conﬁg loca^on of the FeedCollectorHistoryService, which lists the Avalanche
MySQL DB running in RDS: h;ps://apollo.amazon.com/opera^onal_conﬁgura^on.html?
environmentId=3031781&stage=Prod&opConﬁgAc^on=preview
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
Chris has moved our builds over to hosts that do not seem to be on the April deadline.
I am concerned however about a poten^al dependency on the MySQL database used by Avalanche.
Chris can you expand on that dependency with CBM and can somebody tell me whether that database is
going away and if so what the alterna^ves are?
Kevin.
From: Lansley, Chris
Sent: 24 March 2016 10:58
To: Mani, Gajendran; O'Donnell, Kevin; Vuppala, Lakshmi; Ramanarayanan, Sridhar
Cc: Mohan, Thanigaivel; Wilkoszewski, Andrzej; Gorshunov, Vladimir
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Are you aware of any exis^ng plans to get rid of the remaining 5 hosts (once the 4 of the 9 disappear)?

Page 2 of 6

From: Mani, Gajendran
Sent: Thursday, March 24, 2016 10:33 AM
To: Lansley, Chris <clansley@amazon.co.uk>; O'Donnell, Kevin <kodonnel@amazon.co.uk>; Vuppala,
Lakshmi <lakshmiv@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Gorshunov, Vladimir <vladimig@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
For Avalanche, it runs only on RHEL and moving it to Amazon linux involves lot more code changes. So, as a
part of Ava shutdown, we are also migra^ng the associated cabamula builds as well.
Am not sure about ACME builds and if you can move them to new hardware and get out of the viola^on
list, it should be ﬁne I guess. But I will let the respec^ve owners decide.
From: Lansley, Chris
Sent: Thursday, March 24, 2016 3:54 PM
To: Mani, Gajendran <gajendm@amazon.com>; O'Donnell, Kevin <kodonnel@amazon.co.uk>; Vuppala,
Lakshmi <lakshmiv@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Gorshunov, Vladimir <vladimig@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
AFAICT only 4 of the 9 hosts are disappearing [in GCS-CAT-BUILD-NODE-PRODUCTION].
I still do not know why the legacy classic hardware was not replaced with new classic hardware (non-EC2
hardware).

From: Mani, Gajendran
Sent: Wednesday, March 23, 2016 10:29 AM
To: O'Donnell, Kevin <kodonnel@amazon.co.uk>; Lansley, Chris <clansley@amazon.co.uk>; Vuppala,
Lakshmi <lakshmiv@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Gorshunov, Vladimir <vladimig@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Kevin, I don’t remember about any mail thread explicitly sta^ng about this date for Cabumala builds. Eric
might know as we took over Ava/Madeira only early this year.
We only got the ^cket men^oned in the subject that was cut last week.
From: O'Donnell, Kevin
Sent: Wednesday, March 23, 2016 3:48 PM
To: Lansley, Chris <clansley@amazon.co.uk>; Mani, Gajendran <gajendm@amazon.com>; Vuppala,
Lakshmi <lakshmiv@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>;
Gorshunov, Vladimir <vladimig@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
Page 3 of 6

Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Does anyone have the email thread around the moving of these builds oﬀ the cabumala hosts by April. I’m
trying to determine if this was something ACME commi;ed to and got missed.
Ø Lakshmi has been in touch with ACME for moving oﬀ the cabumala builds. To my knowledge, for
these hosts, we no longer have the op^on to replace and they will have to be replaced by Apr 26.
From an IM with Lakshmi:
Vuppala, Lakshmi
Actually, no.
09:50
During the avalanche/cabumala handover to our team, we were told that these hosts need to be
released by April-26 and during the handover it was men^oned that we need not worry about those 3
builds.

From: Lansley, Chris
Sent: 23 March 2016 10:01
To: Mani, Gajendran; Vuppala, Lakshmi; Ramanarayanan, Sridhar; O'Donnell, Kevin
Cc: Mohan, Thanigaivel; Wilkoszewski, Andrzej
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Thankyou. The policy isn't clear to me, can't you just replace the legacy classic hardware with new classic
hardware - was this op^on inves^gated?
From: Mani, Gajendran
Sent: Wednesday, March 23, 2016 9:48 AM
To: Lansley, Chris <clansley@amazon.co.uk>; Vuppala, Lakshmi <lakshmiv@amazon.com>;
Ramanarayanan, Sridhar <rsridha@amazon.com>; O'Donnell, Kevin <kodonnel@amazon.co.uk>
Cc: Mohan, Thanigaivel <thanigm@amazon.com>; Wilkoszewski, Andrzej <andrzej@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Access provided.
From: Lansley, Chris
Sent: Wednesday, March 23, 2016 3:12 PM

Page 4 of 6

Sent: Wednesday, March 23, 2016 3:12 PM
To: Vuppala, Lakshmi <lakshmiv@amazon.com>; Ramanarayanan, Sridhar <rsridha@amazon.com>;
O'Donnell, Kevin <kodonnel@amazon.co.uk>
Cc: Mani, Gajendran <gajendm@amazon.com>; Mohan, Thanigaivel <thanigm@amazon.com>;
Wilkoszewski, Andrzej <andrzej@amazon.co.uk>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
We can't see the policy links, it says: "401 Unauthorized. Only the management chain or permi;ed users
can view this page. Please contact gajendm@ for access."
From: Vuppala, Lakshmi
Sent: Wednesday, March 23, 2016 8:31 AM
To: Lansley, Chris <clansley@amazon.co.uk>; Ramanarayanan, Sridhar <rsridha@amazon.com>; O'Donnell,
Kevin <kodonnel@amazon.co.uk>
Cc: Mani, Gajendran <gajendm@amazon.com>; Mohan, Thanigaivel <thanigm@amazon.com>;
Wilkoszewski, Andrzej <andrzej@amazon.co.uk>
Subject: Re: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Adding Andrzej, who conﬁrmed us that these CBM related builds are owned by ACME team.
Thanks,
Lakshmi.

From: Chris Lansley <clansley@amazon.co.uk>
Date: Wednesday, March 23, 2016 at 1:58 PM
To: "Ramanarayanan, Sridhar" <rsridha@amazon.com>, "O'Donnell, Kevin" <kodonnel@amazon.co.uk>
Cc: "Mani, Gajendran" <gajendm@amazon.com>, Thanigaivel Mohan <thanigm@amazon.com>, "Vuppala,
Lakshmi" <lakshmiv@amazon.com>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Kevin - are you aware of this? (This is something arranged with Frank but never handed over?)
From: Ramanarayanan, Sridhar
Sent: Wednesday, March 23, 2016 8:26 AM
To: Lansley, Chris <clansley@amazon.co.uk>; O'Donnell, Kevin <kodonnel@amazon.co.uk>
Cc: Mani, Gajendran <gajendm@amazon.com>; Mohan, Thanigaivel <thanigm@amazon.com>; Vuppala,
Lakshmi <lakshmiv@amazon.com>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Hi Chris,
Lakshmi has been in touch with ACME for moving oﬀ the cabumala builds. To my knowledge, for these
hosts, we no longer have the op^on to replace and they will have to be replaced by Apr 26.
Regards Sridhar

Page 5 of 6

From: Lansley, Chris
Sent: Wednesday, March 23, 2016 1:54 PM
To: Ramanarayanan, Sridhar <rsridha@amazon.com>; O'Donnell, Kevin <kodonnel@amazon.co.uk>
Cc: Mani, Gajendran <gajendm@amazon.com>; Mohan, Thanigaivel <thanigm@amazon.com>
Subject: RE: The following legacy hosts will be released by April 15 (TT
h;ps://;.amazon.com/0074051147) (Drop deadline of Apr 26)
Kevin and Sridhar,
Two things:
· Does ACME have any plans during this year to move our cabumala builds?
· The Avalanche MYSQL DB is used by CBM (also owned by ACME).
Why aren't you just replacing the legacy hosts with new legacy hosts? (un^l everything is moved oﬀ the
legacy services).
Chris
From: Ramanarayanan, Sridhar [mailto:rsridha@amazon.com]
Sent: Wednesday, March 23, 2016 5:35 AM
To: gcs@amazon.com
Cc: Mani, Gajendran <gajendm@amazon.com>; Mohan, Thanigaivel <thanigm@amazon.com>
Subject: The following legacy hosts will be released by April 15 (TT h;ps://;.amazon.com/0074051147)
(Drop deadline of Apr 26)
Importance: High
Hi GCS team,
The following hosts will be released by April 15. We have a high risk policy viola^on that mandates us to
release these hosts. Request you to kindly get in touch with us, if you have any concerns :
GCS-AVALANCHE-MYSQL: https://policyengine.amazon.com/entity/1878225#hardwareMigrations2016Wave2
GCS-CAT-BUILD-NODE-PRODUCTION:
https://policyengine.amazon.com/entity/1879509#hardwareMigrations2016Wave2
GCS-CAT-BUILD-NODE-GAMMA: https://policyengine.amazon.com/entity/1880591#hardwareMigrations2016Wave2
GCS-AVALANCHE-BUILD-NODE-PRODUCTION:
https://policyengine.amazon.com/entity/1879411#hardwareMigrations2016Wave2
GCS-AVA-BUILD-NODE-GAMMA: https://policyengine.amazon.com/entity/1880352#hardwareMigrations2016Wave2
GCS-CAT-BUILD-NODE-TEST: https://policyengine.amazon.com/entity/1879468#hardwareMigrations2016Wave2
GRCS-MADEIRA-TOOLS: https://policyengine.amazon.com/entity/1880592#hardwareMigrations2016Wave2
GCS-RTIP-BUILD-NODE-PRODUCTION-LVD-P1:
https://policyengine.amazon.com/entity/1880593#hardwareMigrations2016Wave2
GCS-RTIP-BUILD-NODE-PRODUCTION-LVD-P2:
https://policyengine.amazon.com/entity/1880594#hardwareMigrations2016Wave2

Page 6 of 6

https://policyengine.amazon.com/entity/1880594#hardwareMigrations2016Wave2
Our verification shows that:
1. Avalanche will be impacted (We will take care of this).
2. Cabumala builds will be impacted (We and ACME team are coordina^ng with depreca^ng the

remaining builds - h;ps://gcs-builds.amazon.com/cgi-bin/build-status.cgi?
org_unit=US&org_unit=UK&org_unit=JP&org_unit=IT&org_unit=GLOBAL&org_unit=FR&org_unit=E
S&org_unit=DE&org_unit=CN&org_unit=CA&display_ﬁlter=all_builds)
3. The sourcedata NFS mount is impacted – Please review your dependency with this and reach out to
us for alterna^ves.
4. Avalanche’s mysql db is impacted – Please review your dependency with this and reach out to us
for alterna^ves.
5. Any thing else your team depends on that we may have missed.

Regards Sridhar

Page 7 of 6


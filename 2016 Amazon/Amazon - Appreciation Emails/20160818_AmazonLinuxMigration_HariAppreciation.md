# 20160818 AmazonLinuxMigration HariAppreciation

> Converted from document `20160818_AmazonLinuxMigration_HariAppreciation.pdf`

Thursday, August 18, 2016 at 5:09:36 PM India Standard Time

Subject: Re: Upgrading apollo environments to Amazon Linux
Date: Thursday, August 18, 2016 at 4:41:09 PM India Standard Time
From: PoliseGy, Hari
To:
Vellal, DaGatreya, grcs-feeds-org@amazon.com
Nice. Good work DaGa.

From: DaGatreya S Vellal <daGatrv@amazon.com>
Date: Thursday, August 18, 2016 at 4:13 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
Team,
FYI, I have completed the migraZon of hosts from RHEL5 to Amazon Linux. The details are captured here:
hGps://w.amazon.com/index.php/SCP-ASP/MigraZonToAmazonLinux
Here are some stats:
- 57 hosts were replaced
- 22 environments addressed (alpha, beta, gamma and prod included)
- 9 Pipelines addressed
- 4 Zckets were resolved as a part of this migraZon (captured here)
- 2 hurdles taken care of (captured here)
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon

From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Thursday, July 21, 2016 at 6:12 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
FYI – Beta and Prod have been restored to their original capacity, with RHEL64 OS’s.
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon

From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Thursday, July 21, 2016 at 2:04 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Update: Upgrading apollo environments to Amazon Linux

Page 1 of 4

Team,
FYI. #7 in the list (hGps://w.amazon.com/index.php/SCPASP/MigraZonToAmazonLinux#Apollo_environments_listed_for_migraZon) is currently stuck with beta
completely down, and 2 hosts of prod down. I am trying to restore the old RHEL OS’s back by creaZng
ASG’s and reusing the hosts that were replaced. This is to ensure that the current operaZonal capacity is
restored. Once done, I plan to check why upgrade failed, and see how it can be avoided. UnZl this happens,
no other hosts will be replaced.
Golden rules learnt (the hard way):
# Replace one host at a Zme.
# Try beta ﬁrst and then prod.
# On any failure, do not conZnue further!
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon

From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Tuesday, July 19, 2016 at 12:03 AM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux
Team,
FYI – the update is taking a bit longer than expected (esp. when replacing prod hosts, since I cannot replace
all of them, at the risk of losing prod availability). I plan on replacing two Apollo envt hosts a day (this will
eventually ensure that we are done with mostly all environments by this week).
I have completed #1 and #2 from this list: hGps://w.amazon.com/index.php/SCPASP/MigraZonToAmazonLinux#Apollo_environments_listed_for_migraZon and I plan to take up 2
subsequent hosts every day and migrate them to Amazon linux. All progress is tracked via wiki:
hGps://w.amazon.com/index.php/SCP-ASP/MigraZonToAmazonLinux
Let me know if you have concerns.
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon

From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Monday, July 18, 2016 at 6:55 PM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Re: Upgrading apollo environments to Amazon Linux

Page 2 of 4

Team,
Ticket hGps://G.amazon.com/0085426093 has been resolved. I have migrated
RetailCatalogServices/VendorData (beta, gamma and prod) to Amazon Linux. The migraZon is tracked via
wiki: hGps://w.amazon.com/index.php/SCP-ASP/MigraZonToAmazonLinux
General steps followed:
1. Migrate hosts to Amazon Linux
2. AcZvate the hosts
3. Run test on beta (including integraZon test if any, speciﬁed in the pipeline)
If you have any concerns let me know. I will start migraZng other hosts listed in Zcket:
hGps://G.amazon.com/0085425561
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon

From: "Vellal, DaGatreya" <daGatrv@amazon.com>
Date: Friday, July 15, 2016 at 9:30 AM
To: "grcs-feeds-org@amazon.com" <grcs-feeds-org@amazon.com>
Subject: Upgrading apollo environments to Amazon Linux
Team,
I have two Zckets that’s requesZng us to move from RHEL to Amazon Linux:
· hGps://G.amazon.com/0085426093
· hGps://G.amazon.com/0085425561
Between these two Zckets, the Apollo environments listed for upgrade are:

1.
2.
3.
4.
5.
6.
7.
8.
9.

RetailCatalogServices/VendorData: https://policyengine.amazon.com/entity/1479566#environmentHasRhelCapac
ity
RetailCatalogMadeira/Valet: https://policyengine.amazon.com/entity/1825568#environmentHasRhelCapacity
SecureStorageVault/GCSDatastoresAvalanche: https://policyengine.amazon.com/entity/1825576#environmentHa
sRhelCapacity
SecureStorageVault/GRCSFeeds: https://policyengine.amazon.com/entity/1876981#environmentHasRhelCapacity
GRCSFeedsCaffeineNormalizerTools: https://policyengine.amazon.com/entity/2170122#environmentHasRhelCap
acity
RetailCatalogServices/DocumentStore/NormalizedData: https://policyengine.amazon.com/entity/2171635#environ
mentHasRhelCapacity
RetailCatalogServices/MadeiraFeedListener: https://policyengine.amazon.com/entity/2171651#environmentHasR
helCapacity
RetailCatalogServices/MadeiraSupport: https://policyengine.amazon.com/entity/2171652#environmentHasRhelC
apacity
TodWorker/GRCSMadeira: https://policyengine.amazon.com/entity/2172679#environmentHasRhelCapacity

Page 3 of 4

9. TodWorker/GRCSMadeira: https://policyengine.amazon.com/entity/2172679#environmentHasRhelCapacity
10.

ElasticSearchService/NA/RetailCatalogVendorData: https://policyengine.amazon.com/entity/2240124#environme
ntHasRhelCapacity
11. RetailSystemsConfigService: https://policyengine.amazon.com/entity/2446238#environmentHasRhelCapacity

Since on Monday and Tuesday, we will be working on Hackathon (18th and 19th July), I wanted to upgrade
the environments to Amazon Linux. The intenZon is to minimize producZvity loss. Please consider raising
concerns via this thread if you are not ok with the Zmelines. Otherwise, I am going to try and upgrade
these environments between 18th and 19th of July).
Also, while I am doing this, if you have a similar Zcket, do assign it to me, I will take up the bulk
upgradaZon process.
Regards,
DaGa
daGatrv@amazon.com | SelecZon ContribuZon Pladorm – IngesZon & NormalizaZon

Page 4 of 4


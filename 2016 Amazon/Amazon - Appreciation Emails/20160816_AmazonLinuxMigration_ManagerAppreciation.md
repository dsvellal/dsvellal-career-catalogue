# 20160816 AmazonLinuxMigration ManagerAppreciation

> Converted from document `20160816_AmazonLinuxMigration_ManagerAppreciation.pdf`

Thursday, August 18, 2016 at 4:18:40 PM India Standard Time

Subject: RE: SCP - TT summary -week - 32/2016 [from 07/30 -to- 08/05]
Date: Thursday, August 18, 2016 at 4:15:21 PM India Standard Time
From: Mani, Gajendran
To:
Vellal, DaPatreya
FantasRc. Nice work. Thanks for the update.
From: Vellal, DaPatreya
Sent: Thursday, August 18, 2016 4:11 PM
To: Mani, Gajendran <gajendm@amazon.com>
Subject: Re: SCP - TT summary -week - 32/2016 [from 07/30 -to- 08/05]
Gajendran,
This is to let you know that I have completed the migraRon of hosts from RHEL5 to AmazonLinux. The
details are captured here: hPps://w.amazon.com/index.php/SCP-ASP/MigraRonToAmazonLinux
Here are some stats:
57 hosts were replaced
22 environments addressed (alpha, beta, gamma and prod included)
9 Pipelines addressed
2 Blockers taken care of (captured here)
4 Rckets were resolved as a part of this migraRon (captured here)
I stretched the weekend of 7th Aug and 14th-15th Aug to ensure that the policy engine violaRon and Rcket
SLA violaRon are taken care of.
Regards,
DaPa
daPatrv@amazon.com | SelecRon ContribuRon Plaeorm – IngesRon & NormalizaRon

From: Gajendran Mani <gajendm@amazon.com>
Date: Monday, August 8, 2016 at 12:37 PM
To: "Vellal, DaPatreya" <daPatrv@amazon.com>
Subject: RE: SCP - TT summary -week - 32/2016 [from 07/30 -to- 08/05]
DaPa, lets not change the priority of the Rcket. Let me know the ETA in geing this addressed. This Rcket
got reported already this week and I assuming, it will be reported next week as well unless we could get
this to a closure this week.
From: Vellal, DaPatreya
Sent: Monday, August 08, 2016 12:27 PM
To: Mani, Gajendran <gajendm@amazon.com>
Subject: Re: SCP - TT summary -week - 32/2016 [from 07/30 -to- 08/05]

Page 1 of 4

I am tracking this via wiki: hPps://w.amazon.com/index.php/SCP-ASP/MigraRonToAmazonLinux
As you can see from the wiki, there are 11 environments that have to be migrated and I have already
completed 6. The problem with the rest lies with the sanity-test script that we have. My plan is to compare
the sanity script with the exisRng ones which passed to see if this is any diﬀerent, if not, then to see how I
can modify the script without causing any harm to the environments. I will work with Hari/Mani to validate
the script before deploying other environments. If I migrate the environments without changing this script,
then we may lose out availability which is something that I do not intend to do.
Sev 3 going beyond 30 days – if that’s the SLA, since this doesn’t aﬀect our basic operaRons yet, I will
change the severity to Sev 5, aler consulRng with Hari.
Regards,
DaPa
daPatrv@amazon.com | SelecRon ContribuRon Plaeorm – IngesRon & NormalizaRon

From: Gajendran Mani <gajendm@amazon.com>
Date: Monday, August 8, 2016 at 12:16 PM
To: "Vellal, DaPatreya" <daPatrv@amazon.com>
Subject: FW: SCP - TT summary -week - 32/2016 [from 07/30 -to- 08/05]
Your Rcket hPps://P.amazon.com/0085425561 has failed the SLA. What is the plan to get this addressed?
From: Muthusamy, Raj
Sent: Sunday, August 07, 2016 11:45 AM
To: ascs-scp <ascs-scp@amazon.com>
Cc: PaPem, Poornanand <poornanp@amazon.com>
Subject: SCP - TT summary -week - 32/2016 [from 07/30 -to- 08/05]

Hi All,
Please see below the TT summary status for Selection Contribution Platform.

Selection Contribution Platform
SCP

2014

2015

2016 Target
=min(2014,2015)*0.9

Weekly
Target

Weekly
Actuals

High
Sev

913

544

490

9.4

12

Low
Sev

14106

14276

12695

244.1

162

Page 2 of 4

YTD Actual Total *YTD Target Total
Actual-High Sev 293

291.4

Actual-Low Sev 7029

7567.1

Week Number Weekly Actual-High Sev Weekly Actual-Low Sev
1

0

17

2

8

244

3

14

261

4

8

244

5

7

234

6

10

262

7

2

294

8

12

284

9

8

253

10

9

256

11

9

278

12

11

268

13

5

196

14

14

215

15

22

276

16

18

208

17

6

192

18

15

263

19

9

218

20

5

222

21

9

182

22

12

245

23

12

199

24

8

292

25

5

204

26

8

255

27

9

210
Page 3 of 4

28

5

176

29

3

111

30

6

143

31

12

165

32

12

162

* YTD Target Total = weekly Target X Number of weeks (I excluded 1st week since it had just one day
in 2016)
FYI: Please note that the weekly inflow total may not match with monthly inflow (for example, tickets
coming to GRCS queue sometimes get reassigned to other resolvers outside of GRCS). So these
reports numbers are just point in time.
1) Please see wiki for TT break down based on resolvers
OPSreport-week32-2016#Top_Level_Summary
2) Please see wiki for list of tickets that are failing SLA (Sev3=30 days; Sev4=60 & Sev5=90 days).
Let us go through the report during our Ops review meeting.
OPSreport-week32-2016#SLA_Failing_Report
3) Please see the wiki for list of tickets that will be SLA failing soon
OPSreport-week32-2016#SLA_Failing_Soon_Report

Please see below the overall weekly TT summary for GRCS.
a) Inflow external: 113 TTs
b) Inflow all: 174 TTs
c) Inflow all excluding projects: 174 TTs
c) Sev2: 12 TTs
Please check OPSreport-week32-2016#Sev-2_Report_-_Current_teams and update the comment
section with the Sev2 root causes.
d) Backlog external: 137 TTs
Please check OPSreport-week32-2016#Backlog_External_by_Teams
e) External TTs failing SLA: 18 TTs
f) Backlog all: 270 TTs
g) SLA failing all: 85 TTs
The overview graphs are available on the following wiki
GRCS_Remedy_Metrics_Overview
Page 4 of 4

Please let me know if you have any questions.
Regards
-Raj

Page 5 of 4


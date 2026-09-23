# TakingThingsToConclusion LiferayPerformanceImprovements March23rd2015

> Converted from document `TakingThingsToConclusion_LiferayPerformanceImprovements_March23rd2015.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Chevy Vithiananthan
Monday, March 23, 2015 7:41 PM
Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah Egenolf; Jaishankar
Padmanabhan
Aaron Kammerer; Anuroop V. Gaonkar
RE: Liferay user caching - 23rd March 2015 update

Awesome – thanks From: Dattatreya Subramanya Vellal
Sent: Monday, March 23, 2015 10:09 AM
To: Chevy Vithiananthan; Chandrashekhar Surendranath; Jonah Egenolf; Jaishankar Padmanabhan
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching - 23rd March 2015 update
Hi,

I did the exact same thing today, and have achieved consistency in getting times under 3ish seconds per page. Here
are our run details:
Run No OATS Run Name
Run Summary
Comments
Did not change any configurations aft
had published from Mar 20th Run 6. J
Perfesia04_135hhm_3000_30mins- 5404 transactions, 5 failures, Times
the DBs using scripts attached. NOTE:
30TT_32per3_Mar23_run1
= 140, 247, 324 for 1, 3, 5 HHMs
soa_purge.sh has to be run on Perf04
1
db_purge.sh has to be run on Perf01
5599 transactions, 75 failures,
Perfesia04_135hhm_3000_30minsTimes = 51, 76, 138 for 1, 3, 5
No changes, just changed the login-n
30TT_32per3_Mar23_run2
HHMs
2
the same test after purging DB tables
Perfesia04_135hhm_3000_30mins- 5528 transactions, 3 failures, Times No changes, just changed the login-n
30TT_32per3_Mar23_run3
= 69, 117, 178 for 1, 3, 5 HHMs
3
the same test after purging DB tables
5496 transactions, 17 failures,
Perfesia04_135hhm_3000_30minsTimes = 86, 149, 217 for 1, 3, 5
No Purge, but ran this as soon as the
30TT_32per3_Mar23_run4
4
HHMs
completed.
Perfesia04_135hhm_3000_30mins- 5515 transactions, 0 failures, Times No purge, but ran this as soon as the
30TT_32per3_Mar23_run5
= 71, 121, 194 for 1, 3, 5 HHMs
5
completed.
Perfesia04_135hhm_6000_120mins- <Need Jai’s help to Monitor this
Double the load, quadruple the time
30TT_64per3_Mar23_run6
run>
6
Need to watch what happens!
We should continue to load-test the environment without any DB purges, and then see if we achieve consistent
times wrt app submission or if it deteriorates. Our theory is, it should deteriorate as we put more and more data into
the system because the DB purges improved performance. Another theory is, the image of DB that we have taken on
9th march has corrupted data (may be bad indexes, dangling references etc) which is causing delayed responses, and
once we truncate those, we are seeing better times, and it remains consistent even when we load the system with
more users.
For now, I have started run6, which has a higher load, for a longer duration of time. Hopefully this should help us
prove the theory above. Handing this run off to Jai to publish the report.
Summary:
- We know that if we truncate tables, we achieve good response times and achieve them consistently
- If we let the data grow, we see deterioration of response times, but this needs proof by consistently seeing bad
response times as we increase data in our system
1

- Need to narrow down, what DB purge helps us get better performance numbers, and why!
- Need to see how to further reduce the response times if we have to!
All reports are updated here: https://exeter1microsoftonlinecom4.sharepoint.microsoftonline.com/onegate/Offshore/Shared%20Documents/Horizontal%20Foundation%20Library/3
.3.2.10%20HIX%20Performance%20Run%20-%20Change%20Tracker
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Jaishankar Padmanabhan
Sent: Saturday, March 21, 2015 5:19 AM
To: Dattatreya Subramanya Vellal; Chevy Vithiananthan; Chandrashekhar Surendranath; Jonah Egenolf
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching - 20th March 2015 update

We reverted the db, truncated all 3 db tables and also applied liferay support suggested changes–
theme.css.fast.load=true
theme.images.fast.load=true
But these had no impact as we continued to see response times > 1250s for 1HHM. The AWR for
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar20_run6 could not be saved as all instances had been shut
down.
Jai

From: Dattatreya Subramanya Vellal
Sent: Friday, March 20, 2015 11:16 AM
To: Chevy Vithiananthan; Chandrashekhar Surendranath; Jonah Egenolf
Cc: Aaron Kammerer; Jaishankar Padmanabhan; Anuroop V. Gaonkar
Subject: Liferay user caching - 20th March 2015 update
Here’s what we tried today:
1. Tried truncating a few tables from lportal and corrupted the DB machine.
2. Restored the Perf01 DB to March 9th template.
3. Ran a 3000VU test with purged SOA/APP/Siebel DBs
a. Throughput: 5256 transaction, 44 failures. Avg. Timers: 157, 332, 354 on 1, 3 and 5 HHMs – This
means that we are kind of consistent on getting our response time under 5 seconds.
4. We then tried running the same load with a few deleted lportal entries – and it got worse and we had to
stop in the middle coz there was no point in continuing the run!
5. We have initiated a run with the same configuration as 3, this will be our Run3 for the day, and would
request Jai to monitor it.
a. If we see similar numbers (as of point 2) we know we have the formula to repeat this performance
consistently!
b. Otherwise, we will have to see how to consistently hit 5k with response times under 5 seconds.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Thursday, March 19, 2015 9:08 PM
2

To: Chevy Vithiananthan; Chandrashekhar Surendranath; Jonah Egenolf
Cc: Aaron Kammerer; Jaishankar Padmanabhan; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

Team, here’s today’s update

Mar 19th Update: We have achieved configurations which has resulted in a reduced avg response time and improved
throughput. Here’s how our runs look like today:
Run No OATS Run Name
Run Summary
Comments
4062 transactions, 45 failures,
Perfesia04_135hhm_3000_30minsTimes = 502, 581, 1048 for 1, 3, 5
Configs same as 18th Mar Run which
30TT_32per3_Mar19_run1
1
HHMs
us best results (Run 5)
Our best run so far (achieved with
Perfesia04_135hhm_3000_30mins- 4380 transactions, 6 failures, Times
improved cache configs and purged S
30TT_32per3_Mar19_run2
= 327, 591, 596 for 1, 3, 5 HHMs
2
DB)
Perfesia04_135hhm_3000_30mins- Run was stopped, low CPU
30TT_32per3_Mar19_run3
utilization and high response times No results to show
3
Perfesia04_135hhm_3000_30mins- 3719 transactions, 24 errors, Times Added ehcache and buffed up config
4
30TT_32per3_Mar19_run4
= 500, 788, 754 for 1, 3, 5 HHMs
numbers, but didn't help
Perfesia04_135hhm_3000_30mins- In progress, request jai to monitor
Reverted back to Run 2's configuratio
30TT_32per3_Mar19_run5
and
publish
result
5
with purged App and SOA DB

6

Perfesia04_135hhm_3000_30mins30TT_32per3_Mar19_run6

Can be scheduled with purged
Siebel, App and SOA DBs to see if
that reduces response times

Can this be taken up by Jai? This is to
prove that purging all 3 DBs helps in
reducing response times

Run no 5 is in progress. Requesting Jai to monitor it and publish report. Can Run no 6 be taken up to prove that we
will get reduced response times if we purge DB?
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Tuesday, March 17, 2015 9:37 PM
To: Chevy Vithiananthan; Chandrashekhar Surendranath; Jonah Egenolf
Cc: Aaron Kammerer; Jaishankar Padmanabhan; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

Team,
We did lot of interesting things today with our 30 mins short runs (which ended up being 1 hour with ramp-down
times) and a lot of configuration changes (all captured in this sheet). To give you guys a contrast, we did a base run
where we applied NO CONFIGURATION CHANGES and ran the test for 30 mins, with 3000VUs, and our best run so
far has been app submission with 4135 applications submitted in 30 mins run with rampdown. Here’s how the timers
look like:

Active Virtual Users
Virtual Users with Errors
Transactions Per Second
Pages Per Second
Hits Per Second
Kilobytes Per Second

Best Run (run5)
1796.198
0
1.094
42.216
104.824
2276.949

Base Run (run6)
1706.408
0
0.961
37.407
93.151
2033.33
3

Transactions
Transactions with Errors
Pages
Hits
Kilobytes

4135
0
159575
396235
8606866

3776
0
147010
366084
7990989

Min
Best
Timings (as per OATS)
Run
IF_1HHM_Application
165.28
IF_3HHM_Application_QHP 647.59
IF_5HHM_Application_QHP 642.598

Max

Base
Run
196.9
794.727
764.651

Avg

Pass

Best
Base
Best
Base
Run
Run
Run
Run
580.815 714.693 382.198 490.587
675.138 821.654 663.329 803.164
673.15 787.801 656.51 776.537

Best
Run
3535
450
150

Fa
Base
Run
3176
450
150

Best
Run
0
0
0

We are currently running an ehcache versioned run Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run8.
Hopefully we should see better numbers after this completes execution. Requesting Jai to monitor this run and
publish report.
The performance reports and the AWR report for all of today’s runs have been uploaded in this folder.
A brief summary of our other runs:
Run
1
2
3
4
5
6
7
8

Name
Perfesia04_135hhm_3000_1hour-30TT_32per3_Mar17_run1
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run2
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run3
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run4
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run5
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run6
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run7
Perfesia04_135hhm_3000_30mins-30TT_32per3_Mar17_run8

Virtual
Users
3000 x 1
3000 x 1
3000 x 1
3000 x 1
3000 x 1
3000 x 1
3000 x 1
3000 x 1

Windows
Machines
32
32
32
32
32
32
32
32

Duration
1 hour
30 mins
30 mins
30 mins
30 mins
30 mins
30 mins
30 mins

Ramp up
32 / 3 second
32 / 3 second
32 / 3 second
32 / 3 second
32 / 3 second
32 / 3 second
32 / 3 second
32 / 3 second

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chevy Vithiananthan
Sent: Monday, March 16, 2015 9:26 PM
To: Dattatreya Subramanya Vellal
Cc: Aaron Kammerer; Jaishankar Padmanabhan; Chandrashekhar Surendranath; Jonah Egenolf; Anuroop V. Gaonkar
Subject: Re: Liferay user caching

Nice
Sent from my iPhone
On Mar 16, 2015, at 11:22 AM, "Dattatreya Subramanya Vellal" <dvellal@exeter.com> wrote:
I think we have hit something.. our latest run has an improved through-put and avg-page response
time.

Run

Virtual
Users

Name
4

Windows
Machines

Duratio

1

Perfesia04_135hhm_3000_2hours-30TT_15per5_Mar16

2

Perfesia04_135hhm_3000_1hour-30TT_32per3_Mar16_run2

3

Perfesia04_135hhm_3000_1hour-30TT_32per3_Mar16_run3

3000 x
1
3000 x
1
3000 x
1

32

2 hour

32

1 hou

32

1 hou

All data-uploaded into the folder’s XLS along with AWR reports for analysis. Handing this to Jai now
for further runs.
Jai, please update the spreadsheet with changes and details when done.

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Aaron Kammerer
Sent: Monday, March 16, 2015 7:02 PM
To: Dattatreya Subramanya Vellal; Chevy Vithiananthan; Jaishankar Padmanabhan; Chandrashekhar
Surendranath; Jonah Egenolf; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

This is roughly the page load time we saw for Datta’s last run on Friday as well. Is that correct Jai?
Thanks,
Aaron
From: Dattatreya Subramanya Vellal
Sent: Monday, March 16, 2015 8:43 AM
To: Chevy Vithiananthan; Jaishankar Padmanabhan; Chandrashekhar Surendranath; Jonah Egenolf;
Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

Our run details have been uploaded into the folder. We have done 2 runs so far.
1. Successful submission of 13k applications in 2 hours with 0 errors
2. Successful submission of 6k applications in 2 hours with 6 errors
The avg. page load time on both were close to 10+ seconds (1HHM/3HHM/5HHM), and the CPU
utilization was close to 90%. We are now trying to achieve lower load-times per page by poking
around hibernate configs and ehcache. The following two changes have already been made. All
these details have been captured in the spreadsheet here: https://exeter1microsoftonlinecom4.sharepoint.microsoftonline.com/onegate/Offshore/_layouts/15/WopiFrame.aspx?sourcedoc=%7B
A15928FA-43E9-4381-9EE2-93FB9A43A0E1%7D&file=3.3.2.10%20HIX%20Performance%20Run%20%20Change%20Tracker.xlsx&action=default

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Monday, March 16, 2015 12:35 PM
To: Chevy Vithiananthan; Jaishankar Padmanabhan; Chandrashekhar Surendranath; Jonah Egenolf;
Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching
5

Team,
All changes from now are getting tracked against this spreadsheet:
https://exeter1microsoftonlinecom4.sharepoint.microsoftonline.com/onegate/Offshore/Shared%20Documents/Horizontal%20Foundati
on%20Library/3.3.2.10%20HIX%20Performance%20Run%20-%20Change%20Tracker
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chevy Vithiananthan
Sent: Saturday, March 14, 2015 1:59 AM
To: Jaishankar Padmanabhan; Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah
Egenolf
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

Yes – this should be the one to compare against what data ran last night(this morning eastern time)
From: Jaishankar Padmanabhan
Sent: Friday, March 13, 2015 4:26 PM
To: Chevy Vithiananthan; Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah
Egenolf
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching
Btw, attached is the test we ran for Optum and that has much higher response times for each HHM
type.
From: Jaishankar Padmanabhan
Sent: Friday, March 13, 2015 4:18 PM
To: Chevy Vithiananthan; Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah
Egenolf
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

Perfesia01_135hhm_3000_25-35TT_15per5_Mar12.csv is EG’s run from March 12. The other is ESI’s
run after the fix.
Looking at the response times, it looks like the EG run was slightly better (4 -6 s per page) while the
ESI run was 8-9s. However, there were 14K+ errors reported on OATS for 1HHM in the EG run and
only 264 in the ESI run. The 3HHM case in both cases was relatively error free.
Unless ESI looked at those on app04 before running their test, we don’t know the cause.
Jai
From: Chevy Vithiananthan
Sent: Friday, March 13, 2015 3:40 PM
To: Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah Egenolf; Jaishankar
Padmanabhan
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

I understand that this run was pretty good.
6

Jai – can you attach the stats from oats (on pages) from the previous run (the one we ran for Optum
yesterday) and the run from today – so they can get a sense for what occurred.
I understand that the average page load time went down to 8 sec – from about 40s. that is good
news..
I think we are on the right track – we just need to figure out how to get this to the 2 second range –
Thanks
chevy
From: Dattatreya Subramanya Vellal
Sent: Friday, March 13, 2015 12:06 PM
To: Chandrashekhar Surendranath; Jonah Egenolf
Cc: Chevy Vithiananthan; Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching
Update:
1. We have started the run for the specific config listed in the email:
perfesia04_1hhm_IF_App_march132015_run6
2. We have consumed Rob’s logger changes portlet build:
/home/oracle/hudson_dropbox/3.3.2.10-hix-perf-fixesdev/portlet/hixHealthPlan/14_${SVN_REVISION}/hixHealthPlan.war
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Friday, March 13, 2015 9:36 PM
To: Chandrashekhar Surendranath; Jonah Egenolf
Cc: Chevy Vithiananthan; Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching

Shekhar, Jonah,
We will start off this run on the perf04 instance to establish base-numbers. Need help in monitoring
this run, because it can go up to 2 hours. Jai’s help here would be good. Once we have the
completion of this run, we can pull in numbers based on the data collected.
Then, we have identified the following changes:
• Introducing ehcache (from Aaron’s link) locally, and not at a clustered level. This requires
modification to a temporarily exploded life-ray version and inserting xmls and changing
portal-ext.properties file to point to that location. The exploded Liferay is here (I think Aaron
was looking for this, coz I see that he has created a clustered hibernate-xml:
/u01/app/oracle/mw_home_1/user_projects/domains/og_app_domain/servers/portal_serv
er1/tmp/_WL_user/liferay-ce-611/18hq0n/war/WEB-INF. Basically, we want to follow
instructions from this link: http://www.liferay.com/web/guest/community/wiki//wiki/Main/Liferay+Caching+(EhCache) that talks about /ehcache/hibernate.xml and
/ehcache/liferay-single-vm.xml which are specific to single vm life-ray instances, and not
clustered instances.
• Improving the counter increment (from this link: http://www.liferay.com/community/wiki//wiki/Main/Slimming+Liferay+Portal#section-Slimming+Liferay+PortalOptimize+Counter+Increment) to 100
• Introducing the right params for indexing via lucene index:
https://issues.liferay.com/browse/LPS-5837
7

We are going to take these changes up on Monday and get the next numbers and compare.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chandrashekhar Surendranath
Sent: Friday, March 13, 2015 9:04 PM
To: Anuroop V. Gaonkar; Dattatreya Subramanya Vellal
Cc: Jonah Egenolf; Chevy Vithiananthan; Aaron Kammerer
Subject: RE: Liferay user caching

Hi
Can we run the test specifically mentioned below that we need to demo back again to Optum? The
data that is missing in that group is a think time of 30 seconds.
Shekhar
From: Anuroop V. Gaonkar
Sent: Friday, March 13, 2015 12:12 PM
To: Jonah Egenolf; Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Chevy
Vithiananthan; Aaron Kammerer
Subject: RE: Liferay user caching
Hi,
My take here is quite different. In the thread dumps that I had collected the luence.IndexWriter
seemed to be running forever. This was locking up CPUs and subsequently led to very slow response.
When I looked at liferay site; many other people also seemed have experienced the problem of CPU
being locked when this index writing in Liferay was on.
The suggested solution was to increase the interval at which the index is rewritten/regenerated.
liiferay.lucene.index.interval or something like that. I have shared this info with Datta. He is
experimenting with the approaches suggested in the mail trail and should be able to provide his
views.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Jonah Egenolf
Sent: Friday, March 13, 2015 2:40 AM
To: Dattatreya Subramanya Vellal; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Chevy
Vithiananthan; Aaron Kammerer
Subject: Liferay user caching

Datta/Anuroop,
In our performance demo today, we ran the following test:
-

3000 users/32 agents
15users/5 seconds ramp up
8

-

1 stack
80% 1HHM, 15% 3 HHM, 5% 5 HHM
Run on stack 4

The behavior we saw was that CPU was utilized at about 25% on the app server despite plenty of
load and the APP DB was hit with hundreds of thousands of executions of something like 80 different
queries (so I think on the order of 15M query executions in a 15 minute window). Response time
goes up to 45 seconds plus for every single page. (One interesting thing is that the confirmation page
is SIGNFICANTLY slower than all the other pages. I don’t know what that means, but it might be
useful.) It also looks like perhaps a single thread on Liferay is serving all the user cache requests.
The theory is the page response slowdown is the result of a serialized (single thread not serialized to
disk) round trip to APP DB when any liferay thread asks for user permissions. We see the queries in
the AWR report on APP DB so we know something bad is happening. It might not be serialized, but
that’s what it looks like.
Ideally, liferay would be caching these permissions, but it seems that when users get to a certain
point, the cache stops working. It seems like we’re overflowing the cache, thus everything ends up
needing to go to the DB.
Anyway, that’s the background. I don’t think the specific test matters too much, but we can run that
to reproduce if we want. The key is likely volume of users on the system at once.
We tried using the portlet Datta changed to cache the portal authorization, but it doesn’t seem to
change the behavior.
Aaron and poked around a bit and found this link:
https://www.liferay.com/documentation/liferay-portal/6.0/administration/-/ai/distributed-cachi-4
Which describes how to change the liferay settings for ehcache, hibernate, etc. It looks like we do
not explicitly set any of these, but this link walks through how to do it. It doesn’t tell us exactly what
to set though.
What we’d want to do is increase the cache size, turn on flushing to disk, etc.. Whatever we can
come up with that might allow liferay’s user cache to work.
Either that or come up with a way to avoid it entirely like what Datta tried already.
I don’t have much more to go on than that. We’re hoping we can somehow turn this around and
show a working concurrency test to Optum sooner rather than later. Any help here is much
appreciated!
Thanks!
-

Jonah

9


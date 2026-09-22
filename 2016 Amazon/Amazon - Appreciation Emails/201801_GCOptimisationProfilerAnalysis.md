# 201801 GCOptimisationProfilerAnalysis

> Converted from document `201801_GCOptimisationProfilerAnalysis.pdf`

Friday, February 2, 2018 at 3:44:18 PM India Standard Time

Subject: GC $me reduced from ~17% to about 2% a5er jvm op$misa$on!
Date: Wednesday, 10 January 2018 at 9:48:24 AM India Standard Time
From: Vellal, DaNatreya
To:
trms-dev-core-inpay@amazon.com
Team,
Just wanted to let you know that a5er our JVM op$misa$on (increased heap and change in GC strategy),
our GC run $me has reduced from about 17.69% CPU u$lisa$on daily to 2.43% a5er the JVM ﬁx. Here’s
the before: [1] and a5er: [2] proﬁler charts.
What to look for:
On the very le5 of the ﬂamegraph, see that the second bar from the boNom is marked garbage
collec$on.
In the before graph here: [1], you’ll see that the daily avg from 8th to 9th jan is about 15% and
consists of Mark and Sweep consecu$ve steps.
In the a5er graph: [2], the same bar is now at 2.43%, with a single phase (because of G1GC) and
has run on young heap.
The change got deployed to onebox 14hrs ago, so this is only a 14hr run cycle numbers, but it is s$ll a
signiﬁcant reduc$on. What this means for us, is so much more CPU (about 15%) is available to perform
API level opera$ons. I’ll be op$mising loggers and paNerns soon. If we run our stress tests again, we’ll be
able to squeeze in a few extra TPS!
Regards,
DaNa
DaNatreya S Vellal | TRMS | daNatrv@amazon.com | +91-9972312693

[1] - hNps://proﬁler.amazon.com/proﬁle?
endTime=1515376799999&maxDepth=500&minimumCountsThreshold=0.00001&posi$on=01829
1802ae65c842ae65c842ae65c84&proﬁleName=AbusePreven$onService%2FEU%2FOneBox%2FPro
d&startTime=1514224800000&threadStates=BLOCKED&threadStates=RUNNABLE
[2] - hNps://proﬁler.amazon.com/proﬁle?
endTime=1515545999999&maxDepth=500&minimumCountsThreshold=0.00001&posi$on=01829
1802ae65c842ae65c842ae65c84&proﬁleName=AbusePreven$onService%2FEU%2FOneBox%2FPro
d&startTime=1515510000000&threadStates=BLOCKED&threadStates=RUNNABLE

Page 1 of 1


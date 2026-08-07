---
title: "Liferay Performance Improvements"
date: 2015-01-01
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Taking Things To Conclusion
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar", "Chandrashekhar Surendranath", "Chevy Vithiananthan", "Jonah Egenolf"]
skills: ["Delivery", "Liferay Portal", "Performance Optimization", "Persistence", "SOA"]
programs: ["OneGate"]
tags: ["appreciation", "taking-things-to-conclusion"]
sentiment: positive
impact_type: delivery
recurring: false
---

# Evidence: Liferay Performance Improvements

## Source
- **File:** `TakingThingsToConclusion_LiferayPerformanceImprovements_March23rd2015.pdf`
- **Date:** 2015-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Taking Things To Conclusion

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 9

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> To: Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah Egenolf; Jaishankar

## Full Content
```
Dattatreya Subramanya Vellal
From: Chevy Vithiananthan
Sent: Monday, March 23, 2015 7:41 PM
To: Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Jonah Egenolf; Jaishankar
Padmanabhan
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching - 23rd March 2015 update
Awesome – thanks -
From: Dattatreya Subramanya Vellal
Sent: Monday, March 23, 2015 10:09 AM
To: Chevy Vithiananthan; Chandrashekhar Surendranath; Jonah Egenolf; Jaishankar Padmanabhan
Cc: Aaron Kammerer; Anuroop V. Gaonkar
Subject: RE: Liferay user caching - 23rd March 2015 update
Hi,
I did the exact same thing today, and have achieved consistency in getting times under 3ish seconds per page. Here
are our run details:
Run No OATS Run Name Run Summary Comments
Did not change any configurations after what Jai
had published from Mar 20th Run 6. Just purged
Perfesia04_135hhm_3000_30mins- 5404 transactions, 5 failures, Times
the DBs using scripts attached. NOTE:
30TT_32per3_Mar23_run1 = 140, 247, 324 for 1, 3, 5 HHMs
soa_purge.sh has to be run on Perf04 DB, while
1 db_purge.sh has to be run on Perf01 DB.
5599 transactions, 75 failures,
Perfesia04_135hhm_3000_30mins-
Times = 51, 76, 138 for 1, 3, 5 No changes, just changed the login-nos and ran
30TT_32per3_Mar23_run2
2 HHMs the same test after purging DB tables via scripts.
Perfesia04_135hhm_3000_30mins- 5528 transactions, 3 failures, Times No changes, just changed the login-nos and ran
3 30TT_32per3_Mar23_run3 = 69, 117, 178 for 1, 3, 5 HHMs the same test after purging DB tables via scripts.
5496 transactions, 17 failures,
Perfesia04_135hhm_3000_30mins-
Times = 86, 149, 217 for 1, 3, 5 No Purge, but ran this as soon as the previous one
30TT_32per3_Mar23_run4
4 HHMs completed.
Perfesia04_135hhm_3000_30mins- 5515 transactions, 0 failures, Times No purge, but ran this as soon as the previous one
5 30TT_32per3_Mar23_run5 = 71, 121, 194 for 1, 3, 5 HHMs completed.
Perfesia04_135hhm_6000_120mins- <Need Jai’s help to Monitor this Double the load, quadruple the time of execution.
6 30TT_64per3_Mar23_run6 run> Need to watch what happens!
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
- If we let the data grow,
```

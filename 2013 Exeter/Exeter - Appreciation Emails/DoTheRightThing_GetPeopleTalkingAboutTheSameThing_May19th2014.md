# DoTheRightThing GetPeopleTalkingAboutTheSameThing May19th2014

> Converted from document `DoTheRightThing_GetPeopleTalkingAboutTheSameThing_May19th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Dharnesh Yediyurappa
Monday, May 19, 2014 11:46 AM
Anuroop V. Gaonkar; Chowlur Vijendra Nagendra Sharma; Dattatreya Subramanya Vellal;
Amit Sharma; Chandrashekhar Surendranath; Krishnamurthy Hegde; Sajith Sanal;
Shrinidhi Irodi
RE: Update: RCA for issues - 3.3.2.9 HF1

And EGQA also has a bigger hand in the contribution.
Regards,
Dharnesh Yediyurappa, +9900177558, Skype: dharnish.yediyurappa.exeter
E X E T E R | 4th floor, Nitesh Timesquare, 8 M.G. Road| Bangalore 560001 | India
From: Dharnesh Yediyurappa
Sent: Monday, May 19, 2014 11:48 AM
To: Anuroop V. Gaonkar; Chowlur Vijendra Nagendra Sharma; Dattatreya Subramanya Vellal; Amit Sharma;
Chandrashekhar Surendranath; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi
Subject: RE: Update: RCA for issues - 3.3.2.9 HF1

I will have to look back on these stats or the version and then will come back to you guys on where QA stands today
on validation and where it stands on business knowledge which might be completely different topic, but that’s also a
factor which will add to this.
Regards,
Dharnesh Yediyurappa, +9900177558, Skype: dharnish.yediyurappa.exeter
E X E T E R | 4th floor, Nitesh Timesquare, 8 M.G. Road| Bangalore 560001 | India
From: Anuroop V. Gaonkar
Sent: Monday, May 19, 2014 11:33 A
To: Chowlur Vijendra Nagendra Sharma; Dattatreya Subramanya Vellal; Amit Sharma; Chandrashekhar Surendranath;
Dharnesh Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi
Subject: RE: Update: RCA for issues - 3.3.2.9 HF1

Hi ,
After the initial analysis done by Datta, I saw response from Nagendra only about the deployment issues.
The expected behavior – 13% and validation issues 20% totally 33% need to be understood by QA team. If we can
reduce these 3 percentages – we could do significantly better in the days ahead & save most of wasted effort.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Chowlur Vijendra Nagendra Sharma
Sent: Tuesday, May 13, 2014 1:47 PM
To: Dattatreya Subramanya Vellal; Amit Sharma; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Dharnesh
Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi; Chowlur Vijendra Nagendra Sharma
Subject: RE: Update: RCA for issues - 3.3.2.9 HF1

I will check on the deployment & configuration issues. About a third of them are because of the incorrect value used
in soa deployment.properties file by the ESI Ops yesterday. We have made note of this. I will check on the rest of the
anomalies.
1

Datta, can you check SL # 53 and 59, looks like they are duplicates.

--Thanks & Regards
Nagendra Sharma
EXETER INDIA |Skype: cvnsharma |M: +919886497212
nsharma@exeter.com

From: Dattatreya Subramanya Vellal
Sent: Tuesday, May 13, 2014 1:30 PM
To: Amit Sharma; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Chowlur Vijendra Nagendra Sharma;
Dharnesh Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi; Dattatreya Subramanya Vellal
Subject: Update: RCA for issues - 3.3.2.9 HF1

Updated sheet (had missed out RCA for two cols) - % remain the same.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Tuesday, May 13, 2014 1:26 PM
To: Amit Sharma; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Chowlur Vijendra Nagendra Sharma;
Dattatreya Subramanya Vellal; Dharnesh Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi
Subject: RCA for issues - 3.3.2.9 HF1

Team,
I have consolidated the RCA for issues that we have had since 2nd of May till release (minus that of Thr and Fri). This
gives us an insight into our development, validation and deployment process. In summary, we have only fixed 47% of
issues, the rest were either deployment (13%) or validation issues (20% + 13%) or configuration (3 out of 111 issues).
We have pushed 2 issues as – will be fixed in 3.3.2.10. Perhaps we also have to focus on deployment and QA
processes along with Dev validation.

Summary of the data is here:
Row Labels
Blocker

Priority 1

Priority 2
2

Priority 3

Grand Total

Cache issue
Code Fix
Configuration
Deployment Issue
Expected Behavior
Requirements
Validation issue
Grand Total

7
2
2
1
3
15

1
41
2
18
2
1
10
75

10

3

2

1

4
16

1
5

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

3

1
61
2
20
7
2
18
111


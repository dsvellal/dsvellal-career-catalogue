# TakingThingsToConclusion ClientEscalationOnGlobalSession November12th2014

> Converted from document `TakingThingsToConclusion_ClientEscalationOnGlobalSession_November12th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Anuroop V. Gaonkar
Wednesday, November 12, 2014 7:52 PM
Sachin Shivarama Nayak; Dattatreya Subramanya Vellal; Vinay Sulumane Visweswara
Chandrashekhar Surendranath; Krishnamurthy Hegde
RE: 3.3.2.7 HF6 EBF6

Hey Sachin and Datta,
Thanks a lot for quick response.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Sachin Shivarama Nayak
Sent: Wednesday, November 12, 2014 7:22 PM
To: Dattatreya Subramanya Vellal; Vinay Sulumane Visweswara
Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde; Anuroop V. Gaonkar
Subject: RE: 3.3.2.7 HF6 EBF6

Hi All,
a) OgApiPool has been configured on the instance & code changes have been made to the respective portlets
(added OgApiPool resource-ref to each of the API Portlets & Plan Service). The flow has been tested with
App Submission (SLCSLP), Plan Selection, Enrollment & Dis-enrollment thus covering all the entire flow. OPS:
ONEGATECORE-23251
b) The fix has been ported and tested as stated above. OPS: ONEGATECORE-23252
Test data:
Login: sac1/sac1
MCN#: 1-1278725
Regards,
Sachin Nayak
EXETER

skype: sachin.nyk | mobile: +919036060177
From: Dattatreya Subramanya Vellal
Sent: Wednesday, November 12, 2014 6:51 PM
To: Vinay Sulumane Visweswara; Sachin Shivarama Nayak
Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde; Anuroop V. Gaonkar
Subject: RE: 3.3.2.7 HF6 EBF6

Udpate here:
Code fix for a and b are made. It is being tested on dev and deployment ticket being raised. Sachin is helping us here,
and will respond back to this.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

1

From: Dattatreya Subramanya Vellal
Sent: Wednesday, November 12, 2014 12:36 PM
To: Vinay Sulumane Visweswara
Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde; Anuroop V. Gaonkar
Subject: RE: 3.3.2.7 HF6 EBF6

Hi SV,
Code base is this: svn://172.17.10.60/onegate/branches/3.3.2.7-hotfix06-ebf
Dev envt. is http://ogapp3.3.2.7hf6ebf6dev.og.devexeter.com:7004/web/guest where we work, and deployment
ticket should move things to test
Test envt. is http://ogapp3.3.2.7hf6ebf6test.og.devexeter.com:7004/web/guest
Need your help in doing the following things:
a) Make sure that SiebelUtils.java from 3.3.2.9 HF code base (GetSiebelDbConnection() method, that
implements connection pooling) gets migrated to 3.3.2.7 HF6 EBF code base and gets deployed (SOA/Portal
– we will have to push it into all portlets which have og-api code, we did not have og-required-jars in 3.3.2.7
HF code base) and have a deployment ticket ready. This will take care of 1
b) For 3, Port the following commit made by Sachin to 3.3.2.7 HF6 EBF code base (same as the one shown
above) and have a deployment ticket ready (a different one!)
Revision: 44279
Author: snayak
Date: Friday, November 07, 2014 4:30:10 PM
Message:
ONEGATECORE-23108 : My guess is storing the SOA responses in globalSession is causing the serialization issue. Fingers Crossed.
Works on tomcat, not weblogic.
---Modified : /branches/3.3.2.9-hotfix03ebf1/web/portletApp/portletAppProjects/planDisenrollment/src/main/java/com/armedica/onegate/planDisenrollment/connector/s
ervice/PlanDisenrollmentIndividualServiceImpl.java
Modified : /branches/3.3.2.9-hotfix03ebf1/web/portletApp/portletAppProjects/planDisenrollment/src/main/java/com/armedica/onegate/planDisenrollment/domain/Glo
balSessionObject.java

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Anuroop V. Gaonkar
Sent: Wednesday, November 12, 2014 12:16 PM
To: Dattatreya Subramanya Vellal
Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde
Subject: FW: 3.3.2.7 HF6 EBF6

Hey Datta,
Can you please get the 1 & 3 done on 3.3.2.7 hotfix6 ebf branch?
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Tuesday, November 11, 2014 6:21 PM
To: Lakshmi Thanga-Raja
2

Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde
Subject: RE: 3.3.2.7 HF6 EBF6

Hello Lakshmi,
VT is still in 3.3.2.7 HF06 EBF4.2 and we are planning for 3.3.2.7 HF06 EBF06.
1. We should implement the connection pooling fix (og-api) – Only 1 class SiebelUtils may need to be modified
– but we need to release all portlets + plan service that depend on the og-api
2. The other fix related to AnonPlanBrowsing is not needed as the bug does not exist. Bug was introduced
later.
3. GlobalSession bug exists in planDisenrollment portlet & fix is needed there.
These are easy wins.
The others related to myAccount etc. need significant effort & I am not recommending those to be done there.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Lakshmi Thanga-Raja
Sent: Tuesday, November 11, 2014 12:27 AM
To: Anuroop V. Gaonkar
Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde
Subject: 3.3.2.7 HF6 EBF6
… for VT… on top of all the items promised, can we complete some analysis on the performance fixes that we completed for HI and if any of
those need to be moved to VT. Once you have a sense of what if anything needs to move to VT, I’d like to ask Srini to talk to VT to confirm that
it is okay to move it in.
So, at this point, I am only looking for analysis.
Thanks,
Lakshmi

Lakshmi Thanga-Raja | E X E T E R | (m) 617.596.1843

3


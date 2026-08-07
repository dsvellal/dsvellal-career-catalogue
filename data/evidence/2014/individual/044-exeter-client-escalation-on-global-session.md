---
title: "Client Escalation On Global Session"
date: 2014-01-01
year: 2014
era: Exeter
organization: Exeter (Edifecs)
category: Taking Things To Conclusion
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar", "Chandrashekhar Surendranath", "Krishnamurthy Hegde", "Sachin Shivarama Nayak", "Vinay Sulumane"]
skills: ["Delivery", "Java", "Persistence", "Portal Development", "SOA", "Siebel"]
programs: ["OneGate"]
tags: ["appreciation", "taking-things-to-conclusion"]
sentiment: positive
impact_type: delivery
recurring: false
---

# Evidence: Client Escalation On Global Session

## Source
- **File:** `TakingThingsToConclusion_ClientEscalationOnGlobalSession_November12th2014.pdf`
- **Date:** 2014-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Taking Things To Conclusion

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 3

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> To: Sachin Shivarama Nayak; Dattatreya Subramanya Vellal; Vinay Sulumane Visweswara

## Full Content
```
Dattatreya Subramanya Vellal
From: Anuroop V. Gaonkar
Sent: Wednesday, November 12, 2014 7:52 PM
To: Sachin Shivarama Nayak; Dattatreya Subramanya Vellal; Vinay Sulumane Visweswara
Cc: Chandrashekhar Surendranath; Krishnamurthy Hegde
Subject: RE: 3.3.2.7 HF6 EBF6
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
E X E T E R
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
ONEGATECORE-23108 : My guess is storing the SOA responses in gl
```

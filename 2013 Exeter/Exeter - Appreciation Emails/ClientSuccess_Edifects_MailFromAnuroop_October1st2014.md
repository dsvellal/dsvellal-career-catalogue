# ClientSuccess Edifects MailFromAnuroop October1st2014

> Converted from document `ClientSuccess_Edifects_MailFromAnuroop_October1st2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Anuroop V. Gaonkar
Wednesday, October 01, 2014 7:51 PM
Dattatreya Subramanya Vellal; Sachin Shivarama Nayak; Vinay Sulumane Visweswara;
Satheesh Kumar Raju; Kavya Ramaiah
Chandrashekhar Surendranath; Krishnamurthy Hegde
RE: Status of edifecs integration

Yes, Datta. At least from my perspective the xmls are looking good. The demo by you was also very nicely done &
very well planned.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Dattatreya Subramanya Vellal
Sent: Wednesday, October 01, 2014 7:49 PM
To: Sachin Shivarama Nayak; Vinay Sulumane Visweswara; Satheesh Kumar Raju; Kavya Ramaiah
Cc: Anuroop V. Gaonkar; Chandrashekhar Surendranath; Krishnamurthy Hegde; Brett Ackerman; Jonah Egenolf
Subject: RE: Status of edifecs integration

Not to forget – The successful working demo that pulls live data from our system and generates the xmls that we can
dump! Thank you guys for the hard-work! We will pick this up on Monday.
@PMO - FYI – all code is committed to the MADemo branch.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Sachin Shivarama Nayak
Sent: Wednesday, October 01, 2014 7:45 PM
To: Vinay Sulumane Visweswara; Jonah Egenolf; Dattatreya Subramanya Vellal
Cc: Satheesh Kumar Raju
Subject: RE: Status of edifecs integration

Here’s an update since yesterday!
Pending tasks:
•
•
•
•
•

Converting the XML tool to Maven
Deploying & stabilizing the MADEMO instance (og-api and PlanService)
Add some loggers & additional error handling
Correcting mappings, wherever wrong
Moving few hardcodings to DB

Regards,
Sachin Nayak
EXETER

skype: sachin.nyk | mobile: +919036060177
From: Vinay Sulumane Visweswara
Sent: Tuesday, September 30, 2014 7:27 PM
1

To: Jonah Egenolf; Dattatreya Subramanya Vellal
Cc: Satheesh Kumar Raju; Sachin Shivarama Nayak
Subject: Status of edifecs integration

Hi Jonah/Datta,
Please find the status of the edifecs integration below:
•
•
•

Sample XML with hardcoded OGValues is complete(File attached).
Jar has been generated and can be found under the path - svn://172.17.10.60/onegate/branches/3.3.2.9hotfix05-MADemo/lib/EdifecsXMLGenerationTool/build/jar/EdifecsXMLGenerator.jar
Placing the xml under the specified path is complete. Currently the path is hardcoded to –
“D:/Edifecs/CreatedXml/"+ masterCase + "/" + policyId + "/" + planId”

Pending tasks:
• Mapping of onegate values with the edifecs value- This will require another 3-4 hrs of effort.
• Constants values needs to be founded and populated under the DB table.
• End to end testing will start post lunch tomorrow IST.
Regards,
Vinay S V
EXETER
skype: vinay.sv2 | Mob: +919980741726

2


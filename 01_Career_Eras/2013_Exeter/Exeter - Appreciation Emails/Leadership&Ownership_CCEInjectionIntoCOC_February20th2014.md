# Leadership&Ownership CCEInjectionIntoCOC February20th2014

> Converted from document `Leadership&Ownership_CCEInjectionIntoCOC_February20th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Chevy Vithiananthan
Friday, February 21, 2014 11:11 PM
Dattatreya Subramanya Vellal; Jonah Egenolf
Chandrashekhar Surendranath; Lakshmi Thanga-Raja
RE: Integration of change engine into CoC

Follow Up Flag:
Flag Status:

FollowUp
Completed

Nice work!!
I am looking forward to all this working in the next couple of days
Now did you say the frontend is also completed?
Just kidding – but would be good to get a small POC done if possible on the frontend.
From: Dattatreya Subramanya Vellal
Sent: Friday, February 21, 2014 12:28 PM
To: Jonah Egenolf
Cc: Chandrashekhar Surendranath; Lakshmi Thanga-Raja; Chevy Vithiananthan
Subject: RE: Integration of change engine into CoC

Hi Jonah,
The integration of ChangeEngine into the COC portlets is complete. This includes self-service portlets and portaldriven portlets across IF, ER and EE COC. This can be used to now do integration testing on DEV. Code has NOT been
pushed to TEST. Let me know if any other changes are required.
Here’s the SVN commit versions
EmployeeCOC:
Revision: 25354
Author: skalita
Date: Friday, February 21, 2014 12:09:38 PM
Message:
Adding change capture engine code after COC submission
---Modified : /trunk/web/portletApp/portletAppProjects/EmployeeCOC/pom.xml
Modified :
/trunk/web/portletApp/portletAppProjects/EmployeeCOC/src/main/java/com/exeter/onegate/healthplan/web/Em
ployeeCOCController.java
Modified :
/trunk/web/portletApp/portletAppProjects/EmployeeCOC/src/main/java/com/exeter/onegate/healthplan/web/SsE
mployeeCOCController.java
IndividualFamilyCOC:
Revision: 25353
Author: skalita
Date: Friday, February 21, 2014 12:07:49 PM
Message:
Adding change capture engine code after COC submission
---Modified : /trunk/web/portletApp/portletAppProjects/IndividualFamilyCOC/pom.xml
Modified :
/trunk/web/portletApp/portletAppProjects/IndividualFamilyCOC/src/main/java/com/exeter/onegate/healthplan/we
b/IndividualFamilyCOCController.java
1

Modified :
/trunk/web/portletApp/portletAppProjects/IndividualFamilyCOC/src/main/java/com/exeter/onegate/healthplan/we
b/SsIndividualFamilyCOCController.java
EmployerApplication:
Revision: 25359
Author: skalita
Date: 2:23:57 PM, Friday, February 21, 2014
Message:
Adding change capture engine code after COC submission
---Modified : /trunk/web/portletApp/portletAppProjects/EmployerApplication/pom.xml
Modified :
/trunk/web/portletApp/portletAppProjects/EmployerApplication/src/main/java/com/armedica/onegate/employer
/web/EmployerApplicationController.java

Portlets are built and deployed on DEV2. Portlets wars are:
/home/oracle/hudson_dropbox/trunk/portlet/individualFamilyCOC/232_25353/individualFamilyCOC.war
/home/oracle/hudson_dropbox/trunk/portlet/employeeCOC/95_25354/employeeCOC.war
/home/oracle/hudson_dropbox/trunk/portlet/EmployerApplication_DRE/151_25359/employerApplication.war

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Dattatreya Subramanya Vellal
Sent: Friday, February 21, 2014 11:34 AM
To: Subhraneil Kalita
Subject: FW: Integration of change engine into CoC

FYI.. pls drop by when you complete reading this.

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Jonah Egenolf
Sent: Thursday, February 20, 2014 4:26 AM
To: Dattatreya Subramanya Vellal; Chandrashekhar Surendranath; Chevy Vithiananthan; Lakshmi Thanga-Raja;
Robert Parks
Subject: Integration of change engine into CoC

Datta and I spoke about this today in hopes of getting it done early next week, but now Chevy and Lakshmi want this
work done as soon as possible so we can start testing.
The work we need done is to call the Change Engine at the end of every CoC flow (after all data has been persisted to
Siebel). We expose a method in the change engine that takes a master case as input and returns nothing.
The main method is in ChangeCaptureEngine.java:
public void run(String masterCaseNumber, List<String> ruleSetNames) {
2

The list of ruleSetNames is optional. So we simply pass a masterCaseNumber in String format to the method.
Anywhere we can do a CoC, we need to execute this engine.
Anyway, I think Datta understands the scope here. Hopefully it’s not too much work, and all help is appreciated.
Thanks!
-

Jonah

3


# DoTheRightThing RCAAndDoingTheRightThing November18th2014

> Converted from document `DoTheRightThing_RCAAndDoingTheRightThing_November18th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Dattatreya Subramanya Vellal
Tuesday, November 18, 2014 4:35 PM
Chowlur Vijendra Nagendra Sharma; Amit Sharma; Anuroop V. Gaonkar;
Chandrashekhar Surendranath; Dharnish Yediyurappa; Krishnamurthy Hegde; Sajith
Sanal; Shrinidhi Irodi
RE: The curious case of ONEGATECORE-16759

Hi Nagendra,
The JIRA is created for updating the Apollo release document here: http://egagile:8080/jira/browse/ONEGATECORE23345
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

_____________________________________________
From: Chowlur Vijendra Nagendra Sharma
Sent: Tuesday, November 18, 2014 3:22 PM
To: Dattatreya Subramanya Vellal; Amit Sharma; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Dharnish
Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi
Cc: Chowlur Vijendra Nagendra Sharma
Subject: RE: The curious case of ONEGATECORE-16759

Hi all,
regarding the documentation error, what we have observed is as follows a) What went wrong as of 3.3.2.9 HF1 – which lead us to not capturing web.xml changes into the document
The ESI Ops team deployed the ticket 16759 to test instance and captured it in buildsheet as a special
instruction, which indicates that the release documents have to be updated with this data. However the
documentation team captured the information partially. The instructions to create the OPA data source was
captured but the steps to modify the web.xml on the OPA server were not captured in the release
documents.
b) What needs to be done to correct this in Apollo
The configuration and deployment guide for rulebase has to contain a section which explains in detail as to
how to modify this file. Since this information cannot be transmitted to the documentation team over email,
I am requesting the dev team to create a new document with this information and upload it to sharepoint.
Once that is done, please raise a deployment JIRA which will be executed by Ops team and Documentation
team will be informed about the same.
c) What checks and balances are to be added to make sure that we don’t end up with such situations going
forward
I think the Ops and documentation team has to work together to ensure there are no mismatches between
the buildsheet and release documents before sending out a release. The ops team should have the custody
of all documents pertaining to the release while doing PR dry runs and thus has to review the documents for
correctness and completeness.

Datta - As discussed, please raise a deployment with the document for modifying the web.xml and we shall capture
it in the Apollo buildsheet.

1

--Thanks & Regards
Nagendra Sharma
EXETER INDIA |Skype: cvnsharma |M: +919886497212
nsharma@exeter.com

_____________________________________________
From: Dattatreya Subramanya Vellal
Sent: Tuesday, November 18, 2014 1:06 PM
To: Amit Sharma; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Chowlur Vijendra Nagendra Sharma; Dharnish
Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi
Subject: RE: The curious case of ONEGATECORE-16759

Hi,
Nagendra and I had a discussion and Nagendra is going to take a lead in coming up with the following things.
d) What went wrong as of 3.3.2.9 HF3 – which lead us to not capturing web.xml changes into the document
e) What needs to be done to correct this in Apollo
f) What checks and balances are to be added to make sure that we don’t end up with such situations going
forward
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

-----Original Appointment----From: Dattatreya Subramanya Vellal
Sent: Monday, November 17, 2014 9:16 PM
To: Dattatreya Subramanya Vellal; Amit Sharma; Anuroop V. Gaonkar; Chandrashekhar Surendranath; Chowlur
Vijendra Nagendra Sharma; Dharnish Yediyurappa; Krishnamurthy Hegde; Sajith Sanal; Shrinidhi Irodi
Subject: The curious case of ONEGATECORE-16759
When: Tuesday, November 18, 2014 11:30 AM-12:00 PM (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi.
Where: Conf 1

Agenda:
- Need help in digging through why this configuration missed out making its way to the config document of
Rulebase: http://egagile:8080/jira/browse/ONEGATECORE-16759

2


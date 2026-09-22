# Collaboration Jonah&Rob 11thJuly2013

> Converted from document `Collaboration_Jonah&Rob_11thJuly2013.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Jonah Egenolf
Thursday, July 11, 2013 2:50 AM
Dattatreya Subramanya Vellal; Robert Parks
Sachin Shivarama Nayak
RE: Portal environment

Your help was really great today. We’ll still have questions, but we’re miles ahead of where we were. We’re
equipped to start solving problems rather than just struggling with environments.
Eventually we need to be able to spin up a clean environment from scratch, but given our timeframes this was the
perfect approach.
So thanks very much for the time and effort. It’s very appreciated.
-

Jonah

From: Dattatreya Subramanya Vellal
Sent: Wednesday, July 10, 2013 11:43 AM
To: Robert Parks; Jonah Egenolf
Cc: Sachin Shivarama Nayak
Subject: RE: Portal environment

Rob,
I guess you should be set now to debug both hix and plan-selection.
Sachin,
Thanks for helping Rob set up his environment.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Sachin Shivarama Nayak
Sent: Wednesday, July 10, 2013 8:44 PM
To: Robert Parks
Cc: Jonah Egenolf; Dattatreya Subramanya Vellal
Subject: RE: Portal environment

Hey Rob,
I’ve attached the manager again, in case you need to share it with others!
Regards,
Sachin Nayak
EXETER

skype: sachin.nyk | mobile: +919036060177
From: Robert Parks
Sent: Wednesday, July 10, 2013 5:52 PM
To: Sachin Shivarama Nayak; Jonah Egenolf; Dattatreya Subramanya Vellal
Subject: RE: Portal environment

Hi Sachin,
I think we’re connected on Skype now so whenever the upload is complete I am ready to get started.
Thanks!
1

Rob
From: Sachin Shivarama Nayak
Sent: Wednesday, July 10, 2013 7:04 AM
To: Jonah Egenolf; Robert Parks; Dattatreya Subramanya Vellal
Subject: RE: Portal environment

Hi Rob,
I’m uploading the liferay.rar to the machine 172.10.10.142 at present under \home\oracle\downloads\temp_liferay
(still going on, really slow!). I’ll send you another mail once the copy is complete. We’ll get on call once you’re in.
Some other config you may require is:
The siebel wsdl’s checked out at the location “D:\onegate\trunk\siebel\wsdl\”
I think the endpoint in the Siebel wsdl’s have the alias “ogsbl” or “ogsbldev”. So make sure you add these
lines to your system hosts file:
o ogsbl
172.10.10.141
o ogsbldev 172.10.10.141
The external environments we connect to are:
o SOA: 172.10.10.139 (Configured in pom.xml of a project)
o SBL: 172.10.10.141 (WSDL endpoints)
o OPA: 172.10.10.140
o DB: We use a local DB. So make sure you change the endpoints. You could modify it in liferay before
start up of server at: “D:\liferay-portal-6.1.1-ce-ga2\tomcat-7.0.27\conf\Catalina\localhost\*.xml”.
It is presently 10.10.20.42. Change it to the DB there.
o All the jars we use are present in artifactory. We have a local copy maintained by STS. Make sure
this is updated.
Also make sure you have liferay installed on STS to run on debug mode!
Datta could add in any points I may have missed above. ☺
Regards,
Sachin Nayak
EXETER

skype: sachin.nyk | mobile: +919036060177
From: Jonah Egenolf
Sent: Wednesday, July 10, 2013 3:08 PM
To: Robert Parks; Sachin Shivarama Nayak; Dattatreya Subramanya Vellal
Subject: Portal environment

Rob,
Just to get everyone on the same page, here's our plan for getting you a working portal environment
today:
Sachin is going to zip up his environment, put it on a local machine for us, and write up instructions for
what changes will need to be made to point the environment to EG machines instead of ESI machines. You
will probably have that email before you see this one!
Once you get in the office, get on skype with Sachin (Sachin is sachin.nyk, Rob is robertjparks) and work
through any issues you hit trying to install Sachin's environment.
Also make sure Sachin shows you how to run the portal through STS so we can debug (since at least I don't
know how to do that).

2

Unfortunately I'm going to be a little late into the office today so I want to make sure this gets going before
I get there.
Sachin/Datta, thanks a lot for the support here.
- Jonah

3


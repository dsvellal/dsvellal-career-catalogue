# DoTheRightThing ClearTextPasswordSolution October16th2015

> Converted from document `DoTheRightThing_ClearTextPasswordSolution_October16th2015.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Dattatreya Subramanya Vellal
Friday, October 16, 2015 5:35 PM
Chandrashekhar Surendranath
Amit Sharma
RE: Clear Text

Hi Shekhar,
We have come up with the following solution. The path that we are exploring right now is this:
* If siebel.properties file exists in the location $OG_HOME/config/, then:
a) Read the file, encrypt the contents, and store it within og-api as an encrypted file
b) Delete the siebel.properties file present in the location
c) When we want to get the password, decrypt the file by reading it from within og-api, obtain the key-value
pair and proceed
* If $OG_HOME/config/ does not contain siebel.properties file, then we know that it has been read and stored
within og-api, therefore, go to step c) directly.
This has to be done on load of og-api in Portal, and as a dummy service for invoking the same on SOA.
We have done, as a POC, Step1a. We are working towards achieving b and c. And once this is done, we still have to
do the following things:
1. Centralize all Header injections into one code within og-api
2. Create a utility which reads and either encrypts (and writes it within api, and deletes the original one) or
decrypts the file contents to give us key-value pairs to be used in the program.
3. Test things out completely to see if this works
We are going to go with a symmetric encryption algorithm – DES, for encryption and decryption. We will need time
till Wednesday or so to prove this end-end on a live environment.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chandrashekhar Surendranath
Sent: Friday, October 16, 2015 11:25 AM
To: Dattatreya Subramanya Vellal <dvellal@exeter.com>; Amit Sharma <amit.sharma@exeter.com>
Subject: FW: Clear Text
Some more information
From: Brett Ackerman
Sent: Friday, October 16, 2015 12:24 AM
To: Krishnamurthy Hegde <khegde@exeter.com>; Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Jonah Egenolf <jegenolf@exeter.com>; Robert Parks <rparks@exeter.com>; Amit Sharma
<amit.sharma@exeter.com>
Cc: Christopher Simo <CSimo@exeter.com>
Subject: RE: Clear Text
+ Chris
1

Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Brett Ackerman
Sent: Thursday, October 15, 2015 2:54 PM
To: Krishnamurthy Hegde <khegde@exeter.com>; Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Jonah Egenolf <jegenolf@exeter.com>; Robert Parks <rparks@exeter.com>; Amit Sharma
<amit.sharma@exeter.com>
Subject: RE: Clear Text
Krishna,
Details from Optum on how they set up their credentials for web services.

In 11g we use Oracle’s policy based authentication (OWSM) - see
https://docs.oracle.com/cd/E21764_01/web.1111/e13713/owsm_appendix.htm#WSSOV386

The policy we have applied adds envelope information. The actual TLS/SSL is configured more conventionally at the
Weblogic or OHS (httpd) layer and uses an SSL certificate owned by SoV.

-Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Brett Ackerman
Sent: Thursday, October 15, 2015 11:58 AM
To: Krishnamurthy Hegde <khegde@exeter.com>; Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Jonah Egenolf <jegenolf@exeter.com>; Robert Parks <rparks@exeter.com>; Amit Sharma
<amit.sharma@exeter.com>
Subject: RE: Clear Text
Hi Krishna,
On point 1, I will ask Ajinth to reach out to you. However, please note that hashing is not sufficient if it still sits in a
clear text file.
On point 2, there is nothing specific that VT wants us to implement beyond taking credentials out a clear text file.
However, Optum did mention that they were using role based security similar to AD to manage credentials for the
webservices. I will try and get you those details.

-Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Krishnamurthy Hegde
Sent: Thursday, October 15, 2015 10:58 AM
To: Brett Ackerman <backerman@exeter.com>; Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>; Lakshmi
Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>; Jonah
Egenolf <jegenolf@exeter.com>; Robert Parks <rparks@exeter.com>; Amit Sharma <amit.sharma@exeter.com>
Subject: RE: Clear Text
2

Hi Brett,
The team spent time working on this today. At this point, we are running in multiple directions without converging
on a single option.

In order to help speed up the conclusion of this item can you get answers to the below two questions?
1. What are the exact steps that Optum followed in order to get the DB password hashing to work? Can we get that
documentation?
2. I understand that SOV/Optum have something specific in mind, for us to implement. Can you help getting
something that's more detailed, if they've already implemented that.

We will send you updates on every day on where we stand with this item.
Thanks
Krishna
Sent from my Windows Phone
From: Brett Ackerman
Sent: 15-10-2015 02:30
To: Chevy Vithiananthan; Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Jonah Egenolf; Robert Parks
Cc: Krishnamurthy Hegde
Subject: RE: Clear Text
All,
Meeting this afternoon with VT Security went fine. Attached is the email from VT with specifications on how
passwords should be handled.
In short, the issue is that we have a number of user/pass combos in the Siebel.properities file which are clear text
and some can be hashed. This is insufficient from a VT security protocol standpoint, we should be using a separate
mechanism.
I spoke with Optum Architect and he said they were using role based TLS encryption for all web services, so that may
be something we want to look into.
I have not given any timeline on a fix here, but I think the most important next step is to internally huddle to figure
out how we plan to address this issue, then we can provide a date. Based on the conversation today, having a plan
and expected remediation timeline is the most important thing.
Please advise on next steps and timing.

Thanks,
Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Brett Ackerman
Sent: Wednesday, October 14, 2015 1:43 PM
3

To: Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>; Lakshmi Thanga-Raja <Lakshmi@exeter.com>;
Chandrashekhar Surendranath <schandrashekhar@exeter.com>; Jonah Egenolf <jegenolf@exeter.com>; Robert
Parks <rparks@exeter.com>
Subject: FW: Clear Text
Here is what I have so far on the clear text issue.
I’ll know more this afternoon to understand what is still open, and will update the group.

-Brett
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570

From: Christopher Simo
Sent: Wednesday, October 14, 2015 1:38 PM
To: Brett Ackerman <backerman@exeter.com>
Subject: FW: Clear Text

-----Original Message----From: Johnson, Rob B
Sent: Tuesday, October 13, 2015 02:52 PM Central Standard Time
To: Simo, Christopher
Subject: Clear Text
This is what I could find on this.
Topic: Exeter OneGate Siebel Code and Account Passwords Stored in Clear Text
Background:
• There is an existing finding for Exeter OneGate code (Siebel.properties HF02) storing clear text passwords
within Siebel
• The previous scope included two Siebel accounts and was mitigated to a degree by the Siebel team hashing
the passwords
Current Scope:
• The new Exeter OneGate code (Siebel.properties HF03), currently scheduled for deployment as part of the
R2 A&B release, will expand the existing finding
• The scope will increase to include a Siebel administrative account that manages all aspects of Siebel and an
Oracle account that owns the VT applications
• The new code will bypass the use of the previous mitigation process
Proposed Next Steps:
• State of Vermont Security assessment of Exeter OneGate software to determine severity of finding and to
document accordingly
• State of Vermont escalation to Exeter for code changes based on assessed severity and impact
• State of Vermont requests to Exeter and Oracle on potential mitigation options while awaiting Exeter code
changes

Password for logging in Application (EAI Object Manager) = Clear Text
Password for logging into Database Directly= Hashed Text
Example of file from DEV.
onegate.siebel.userName=EAIADMIN
onegate.siebel.password= -> Clear Text
onegate.siebel.db.userName=SADMIN
onegate.siebel.db.password=-> Hashed Text
4

onegate.siebelcustomdb.userName=ONEGATE
onegate.siebelcustomdb.password=-> Clear Text
onegate.verification.file.url=http://portaldev-app.vt.local:7003/content/docs/
onegate.siebel.db.server=dbsrd1749.uhc.com
onegate.siebel.db.port=1521
onegate.siebel.db.name=devsieb.uhc.com
onegate.individual.coc.service.url=http://soadev.hsep.in.vt.local:7777/soainfra/services/default/OneGateIndividualCoCService/OneGateIndividualCoCService
onegate.address.url=http://portaldev-app.vt.local:7003/
onegate.external.verification.url=http://soadev.hsep.in.vt.local:7777/ExternalVerifica
tionService-ExternalVerificationSimulator-context-root/VerifyHousehold_pt
onegate.siebel.gateway=apsrd4506.uhc.com
onegate.siebel.gateway.port=2320
onegate.siebel.enterprise=VTHBE_DEV
onegate.siebel.server=CRMDEV_BAT01
onegate.siebel.eim.server=apsrd4506.uhc.com
onegate.siebel.eim.server.username=oraclevt
onegate.siebel.eim.server.password=-> Clear Text
onegate.siebel.eim.server.port=22
onegate.opa.url=http://opadev-app.vt.local:8001/determinations-server/

___________________________________________________________________________
Rob Johnson l Senior Service Director Information Technology, Optum Technology Government Solutions
(office) 860.502.6048 (cell) 203.736.3799 | (email) robejohn@optum.com
400 Capital Boulevard, Rocky Hill, CT 06067

Our United Culture. The way forward.
■ Integrity ■ Compassion ■ Relationships ■ Innovation ■ Performance

This e-mail, including attachments, may include confidential and/or
proprietary information, and may be used only by the person or entity
to which it is addressed. If the reader of this e-mail is not the intended
recipient or his or her authorized agent, the reader is hereby notified
that any dissemination, distribution or copying of this e-mail is
prohibited. If you have received this e-mail in error, please notify the
sender by replying to this message and delete this e-mail immediately.

5


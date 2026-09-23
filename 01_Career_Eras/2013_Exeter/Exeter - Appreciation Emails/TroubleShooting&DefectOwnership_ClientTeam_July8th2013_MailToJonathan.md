# TroubleShooting&DefectOwnership ClientTeam July8th2013 MailToJonathan

> Converted from document `TroubleShooting&DefectOwnership_ClientTeam_July8th2013_MailToJonathan.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Lakshmi Thanga-Raja
Monday, July 08, 2013 3:12 AM
Krishnamurthy Hegde; George Mathew
Jonathan Kutchins; Chandrashekhar Surendranath; Chevy Vithiananthan; Louis Gutierrez;
Darren He; Anuroop V. Gaonkar; Jon-Paul Berexa; Peter Devlin
RE: HI HIX 3.2.4 Deployment Issues Escalation

Krishna –
First, thank you for working on this. The 3.2.4 Amazon instance has been brought up for you. The team attempted to install the
updated JAR files from ESI and it did not resolve the issue. I have asked them to proceed with a brand new portal deployment
given that we are not seeing this issue on any of our 3.2.4/3.2.4.1 instances and perhaps a fresh full install would be helpful.
Both Jon-Paul and Pete are available tonight for a collaborative session with the ESI team. Can you make sure that your team
that worked on this issue is available so that they can discuss and hopefully resolve the issue? Jon-Paul can ssh and share his
screen for your team to analyze and provide any inputs they have. I had suggested 11 EST as a possible start time. Please
follow-up with your team and can you coordinate with Pete and Jon-Paul directly.
Thank you,
Lakshmi
From: Krishnamurthy Hegde
Sent: Sunday, July 07, 2013 2:50 PM
To: George Mathew; Lakshmi Thanga-Raja
Cc: Jonathan Kutchins; Chandrashekhar Surendranath; Chevy Vithiananthan; Louis Gutierrez; Darren He; Anuroop V.
Gaonkar
Subject: RE: HI HIX 3.2.4 Deployment Issues Escalation

Hi Lakshmi,
RT 1670 has been updated with the analysis (see attached) and the next steps. Please have someone from the EG
team do the following at the end of your/Hawaii day:
a) update RT with any updates and new findings
b) provide a hand off email with the next steps to be taken up by the ESI team on Monday morning.
c) if feasible, bring up an AMZN 3.2.4 instance so that we can validate our fixes that we suggest.
Thanks,
Krishna
From: George Mathew
Sent: Sunday, July 07, 2013 7:40 PM
To: George Mathew; Lakshmi Thanga-Raja
Cc: Jonathan Kutchins; Chandrashekhar Surendranath; Lakshmi Thanga-Raja; Chevy Vithiananthan; Louis Gutierrez;
Darren He; Krishnamurthy Hegde; Anuroop V. Gaonkar
Subject: RE: HI HIX 3.2.4 Deployment Issues Escalation

Lakshmi, I am copying Anuroop, who is also coordinating with the team. He will also be available at
+919845183528.

-------- Original message -------From: George Mathew <gmathew@exeter.com>
Date:
1

To: Lakshmi Thanga-Raja <Lakshmi@exeter.com>
Cc: Jonathan Kutchins <jkutchins@exeter.com>,Chandrashekhar Surendranath
<schandrashekhar@exeter.com>,Lakshmi Thanga-Raja <Lakshmi@exeter.com>,Chevy Vithiananthan
<chevyv@exeter.com>,Louis Gutierrez <lgutierrez@exeter.com>,Darren He
<dhe@exeter.com>,Krishnamurthy Hegde <khegde@exeter.com>
Subject: RE: HI HIX 3.2.4 Deployment Issues Escalation
Lakshmi, the team has updated the RT with the current status and Pete has been reviewing this. The team
here will need another 3-4 hours to do a hand-off after analyzing the current set of logs. Krishna (copied)
will be sending an email to this group by EOD, along with next steps needed for us to fix this issue.
Both Krishna and I will be available through your day for any action.
Thanks,
George

-------- Original message -------From: Lakshmi Thanga-Raja <Lakshmi@exeter.com>
Date:
To: George Mathew <gmathew@exeter.com>
Cc: Jonathan Kutchins <jkutchins@exeter.com>,Chandrashekhar Surendranath
<schandrashekhar@exeter.com>,Lakshmi Thanga-Raja <Lakshmi@exeter.com>,Chevy Vithiananthan
<chevyv@exeter.com>,Louis Gutierrez <lgutierrez@exeter.com>,Darren He <dhe@exeter.com>
Subject: RE: HI HIX 3.2.4 Deployment Issues Escalation
George, can we have an email hand off from your team so that we can pick it up from here.
Also, who should be out point of contact for any follow-up.
Thanks,
Lakshmi
George Mathew <gmathew@exeter.com> wrote:

Jonathan, we are looking into this now.
George

-------- Original message -------From: Jonathan Kutchins <jkutchins@exeter.com>
Date:
To: George Mathew <gmathew@exeter.com>,Chandrashekhar Surendranath
<schandrashekhar@exeter.com>,Lakshmi Thanga-Raja <Lakshmi@exeter.com>
Cc: Chevy Vithiananthan <chevyv@exeter.com>,Louis Gutierrez <lgutierrez@exeter.com>,Darren He
<dhe@exeter.com>
Subject: FW: HI HIX 3.2.4 Deployment Issues Escalation
Not sure what the most expedient path forward is, but anything we can do to help accelerate a solution
would be greatly appreciated!
I think Pete Devlin is the best contact in Hawaii thru the weekend.
2

Thanks!
Jonathan
From: Peter Devlin
Sent: Saturday, July 06, 2013 8:29 PM
To: Jonathan Kutchins
Cc: Darren He; George Mathew
Subject: HI HIX 3.2.4 Deployment Issues Escalation
Hi Jonathan,
Darren is on a flight and has asked me to escalate the 3.2.4 deployment troubles on CGI’s Dev environment. There
are two issues, individual application looping and an incorrect employee eligibility summary page, but we think they
have the same source. CGI has expressed strongly that they need to have a validated Dev environment on Monday.
This past week, we had Jon Paul on-site helping troubleshoot with CGI’s deployment team. We’ve restarted all the
servers, redeployed the relevant portlets and all the wsdls, compared the rulebases, ruled out Siebel as the error
source, checked class loading, and examined the soa xsd and payloads. We first escalated to Shrikar and attempted
his suggestions. This morning Jon Paul and I had a five-hour troubleshooting call with Thomas, Raj, and Josh. By the
end of the call we hadn’t found the issue, so we increased the log level and downloaded highly detailed logs for the
test case.
Jon Paul has sent these logs to Thomas who is going to review them later this evening, but Thomas doesn’t expect
he’ll find anything. Thomas wants to also forward them to Shrinidhi and Anagha. Would ESI be able to take a look at
these logs and the relevant RT tickets (1670 and 1694) on their Sunday?
Thanks,
Pete
Peter Devlin | Exeter Group
Office 617-528-5084 | Cell 215-279-2749
pdevlin@exeter.com

3


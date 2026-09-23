# TroubleShooting&DefectOwnership AnonCalculatorConcurrentSessionError November7th2014

> Converted from document `TroubleShooting&DefectOwnership_AnonCalculatorConcurrentSessionError_November7th2014.pdf`

Dattatreya Subramanya Vellal
Anuroop V. Gaonkar
Friday, November 07, 2014 3:57 PM
Jonah Egenolf; Dharnish Yediyurappa; Lakshmi Thanga-Raja; Jaishankar Padmanabhan
Chandrashekhar Surendranath; Srinivas Jillella; Shrinidhi Irodi; Krishnamurthy Hegde;
Robert Parks; Dattatreya Subramanya Vellal; Sachin Shivarama Nayak; Dharnish
Yediyurappa
RE: I am running 100 Users anonymous shopping right now.

From:
Sent:
To:
Cc:
Subject:

Hello Jonah & Others,
The issue was related to thread(s) trying to push the requests through the same controller instance (Thanks Sachin
for helping piece together the piece of the puzzle). This controller instance was shared across all portlet
instances/threads as we configure controllers using spring’s applicationContext configuration. So multiple threads
accessed the same controller instance. The global session object in this single instance of the controller was getting
overwritten & some of the requests were failing.
Sachin is making changes to ensure that GlobalSession is not member variable of Controller in
AnonymousPlanShopping. This should ensure that failures don’t happen when multiple threads (higher loads) start
hitting the same controller.
1. Sachin and Datta looked at if there is similar incorrect usage of GlobalSession elsewhere. They have found
some other places where fix is needed (PlanDisenrollment). Sachin will do that. These fixes are part of EBF8
as of now. Whether these should be released etc. is Lakshmi/Shekhar/… call.
We have tested these fixes and results look promising – No errors with 20 concurrent users with 5 second
think time. We are now trying with 100 users (hope our system holds up & does not start cracking
elsewhere).
2. This made us realize that in some of the other controllers also we have instance variables that may get in to
inconsistent state when multiple requests are getting pushed through that controller concurrently. To
overcome this; we can either
a. Ensure that all developers understand that they MUST NOT define instance variables in Controller
for maintaining state information & use those variables in computations
OR
b. Set the controllers as Session Scope (using spring mechanism) - Thanks Shrinidhi for this. This will
have implication that we may bump up memory foot print a bit.
We should do this cleanup in Apollo or sooner as such things may lead to very bad unintended side effects.

SalesToolByProduct serialization error may be due to the fact that they have older release (EBF4) on which load
testing was done.
SalesToolByProduct error was already resolved by replacing that with OgSalesToolByProduct (a serializable entity)
and moving the instantiation to api cache. Hence as per the check done by Datta and team needed fixes are already
present in EBF6. Hence if HI tests with the right version the Serialization error should go away.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

1

From: Jonah Egenolf
Sent: Friday, November 07, 2014 12:22 AM
To: Anuroop V. Gaonkar; Dharnish Yediyurappa; Lakshmi Thanga-Raja; Jaishankar Padmanabhan
Cc: Chandrashekhar Surendranath; Srinivas Jillella; Shrinidhi Irodi; Krishnamurthy Hegde; Robert Parks
Subject: Re: I am running 100 Users anonymous shopping right now.

I think we need to refocus here a bit. Here's what we know:
- Hawaii hits the problems almost exclusively in Plan Comparison. If we saw random errors all over anon
plan selection, we would see a far less regular pattern
- Hawaii sees a deserialization error on Sales Tool By Product. We have had a problem on that previously
and we fixed it for regular plan selection. I'm guessing we never fixed it in anon plan selection.
- If a session cannot be serialized/deserialized, we will end up losing session data when the thread begins
processing again and null pointers can happen all over any time we expect global session data to exist
without being safe about it. (This isn't the problem... if we lose all the data, we're going to fail, it's just a
question of how we fail.)
So for what Hawaii is reporting, we have 2 basic approaches:
1) remove the SalesToolByProducts configured in Siebel for their plans. This could provide immediate
relief, but it is not correct. Plan comparison will no longer have links to the plan data. I don't know exactly
where this data lives, but it should be pretty easy to find in Siebel. I would try this if we want to reduce the
noise here and prove we're making headway.
2) stop putting SalesToolByProduct in the global session in the Anonymous portlet. The suggested
approach would be to simply ask the API for it every time you need it. That way it never lives in the global
session and cannot cause serialization problems. This should be a relatively trivial code change.
As to why we don't see the same behavior here: I think we don't configure the sales tool by product in our
environments. It's like the supporting PDF for the plan. If there is no such thing configured, it ends up as
NULL in the global session and does not cause a serialization problem.

Now, as to what Anuroop etc. are seeing in our environments, it looks like we start puking purely because
the system is overloaded. I don't see how else putting in a larger sleep time would cause a reduction in
failures. That said, it doesn't appear to be the same problem Hawaii is hitting. So I'm not sure what to
make of that. At a minimum, we should attack the serialization problem first.
- Jonah
From: Anuroop V. Gaonkar
Sent: Thursday, November 06, 2014 11:28 AM
To: Dharnish Yediyurappa; Lakshmi Thanga-Raja; Jaishankar Padmanabhan
Cc: Chandrashekhar Surendranath; Srinivas Jillella; Shrinidhi Irodi; Krishnamurthy Hegde; Jonah Egenolf; Robert Parks
Subject: RE: I am running 100 Users anonymous shopping right now.
Hello All,
After looking at the issue for past 3 hours – the issue appears to be code related. The primary observations are as
below:
1.

Server seems to schedule the same server thread to process the same type of requests that have arrived
at the server without much time gap from different users.
2

In the current context – the thread is thread number 13 and the request is comparePlans or
compareDentalPlans.
Please look at comparePlans request that came in around 08:02:41,286 which failed at 08:02:41,307 and
with internal session object: GlobalSessionObject@15c016ed
The portlet session for these requests becomes the same & data shared through globalsession object set in
the portlet session gets corrupted.
Why I believe 2 requests came from different virtual users?
These requests have come from different virtual users from client side as there was 25 second think time
between each operation. So 2 comparePlan requests would not have been fired by same virtual user within
micro second difference.
This kind of threading behavior may happen if we are stateless. I don’t have a reserve solution right now on how to
prevent the server from scheduling the same thread to process 2 distinct requests.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Dharnish Yediyurappa
Sent: Thursday, November 06, 2014 8:42 PM
To: Lakshmi Thanga-Raja; Jaishankar Padmanabhan
Cc: Chandrashekhar Surendranath; Srinivas Jillella; Anuroop V. Gaonkar; Shrinidhi Irodi; Krishnamurthy Hegde
Subject: RE: I am running 100 Users anonymous shopping right now.

Hi All
We tried replicating the issue in 3329HF3EBF3 & EBF6, could not get the same error (De-serialization issue) as we are
getting in production, our recommendation at this point is to add think time between the transactions and try to run
the performance test once again, Support team has asked for more details in the JIRA.
Our observations:
Observation 1: Loaded 20 concurrent users for 15mins duration with think time of 5 seconds (ramp up load, where
every single VU gets added every 5 second).
Result: 80% of the transaction failed as think time was less.
Observation 2: Loaded 20 concurrent users for 15mins duration with think time of 25 seconds (ramp up load, where
every single VU gets added every 5 second).
Result: Only 10% of Transaction failed as we increased the Think Time.
Anuroop and Team have found an issue during analysis phase which they are currently looking into it.
Regards,
Dharnesh Yediyurappa, +9900177558, Skype: dharnish.yediyurappa.exeter
E X E T E R | 4th floor, Nitesh Timesquare, 8 M.G. Road| Bangalore 560001 | India
From: Lakshmi Thanga-Raja
Sent: Thursday, November 06, 2014 5:21 PM
To: Dharnish Yediyurappa; Jaishankar Padmanabhan
3

Cc: Chandrashekhar Surendranath; Srinivas Jillella; Anuroop V. Gaonkar; Shrinidhi Irodi; Krishnamurthy Hegde
Subject: RE: I am running 100 Users anonymous shopping right now.
The question is where do we have HI production data as well. I agree we need to replicate on the HI version, but I do feel that the HI Prod data
is a critical component of our analysis,
Lakshmi

From: Dharnish Yediyurappa
Sent: Thursday, November 06, 2014 4:48 AM
To: Jaishankar Padmanabhan
Cc: Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Srinivas Jillella; Anuroop V. Gaonkar; Shrinidhi Irodi;
Krishnamurthy Hegde
Subject: RE: I am running 100 Users anonymous shopping right now.
Correction we are replicating in 3329HF3EBF3
Regards,
Dharnesh Yediyurappa, +9900177558, Skype: dharnish.yediyurappa.exeter
E X E T E R | 4th floor, Nitesh Timesquare, 8 M.G. Road| Bangalore 560001 | India
From: Dharnish Yediyurappa
Sent: Thursday, November 06, 2014 2:06 PM
To: Jaishankar Padmanabhan
Cc: Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Srinivas Jillella; Anuroop V. Gaonkar; Shrinidhi Irodi;
Krishnamurthy Hegde
Subject: RE: I am running 100 Users anonymous shopping right now.

Hi Jai
JIRA: ONEGATECORE-23108 has been raised for the same, as per the JIRA, issue has been reported in 3.3.2.9 Hot Fix
3 EBF 03, so we are trying to replicate this issue in 3329HF3EBF4 and see if its replicable or not, if replicable we need
to see which version this needs to be fixed.
I don’t think it makes sense to replicate in 33210PLNDTESTQA, will keep you all guys posted on the test results.
Regards,
Dharnesh Yediyurappa, +9900177558, Skype: dharnish.yediyurappa.exeter
E X E T E R | 4th floor, Nitesh Timesquare, 8 M.G. Road| Bangalore 560001 | India
From: Jaishankar Padmanabhan
Sent: Thursday, November 06, 2014 6:45 AM
To: Dharnish Yediyurappa
Cc: Lakshmi Thanga-Raja; Chandrashekhar Surendranath; Srinivas Jillella
Subject: RE: I am running 100 Users anonymous shopping right now.

Hi Dharnish,
The existing IF_1HHM_Anonymous script recorded by ESI QA against 3.3.2.10Perf02 failed to run against
3.3.2.10PLNLDTESTQA after I bulk replaced the url (within OpenScript). Therefore, I created
IF_1HHM_Anonymous_plnldtest script on 172.17.188.203 to run against 3.3.2.10PLNLDTESTQA
Running this script repeatedly from OpenScript (1 user) passes, while load testing with 10 users (10 iterations, think
time <= 3 sec) resulted in few errors, however with 50 users (think time <=10 sec) almost every iteration failed with
the WebHTTPException as it could not find the node to click. I did see corresponding NPE in the portal logs but not
the errors that CGI is reporting wrt user not being found.

4

Can you guys further investigate?
Thanks
Jai

From: Jaishankar Padmanabhan
Sent: Tuesday, November 04, 2014 9:15 PM
To: Dharnish Yediyurappa
Cc: Lakshmi Thanga-Raja; Chandrashekhar Surendranath
Subject: FW: I am running 100 Users anonymous shopping right now.

Hi Dharnish,
HI is seeing errors in plan comparison in the anonymous flow under load (100 users). Since this should be one of our
load scenarios anyway, can you have someone record this flow to compare health and dental plans?
33210Perf02 should be the ideal candidate to test since it has the HI production plans loaded.
Thanks
Jai
From: Eric Moy
Sent: Tuesday, November 04, 2014 4:38 PM
To: Jaishankar Padmanabhan
Subject: FW: I am running 100 Users anonymous shopping right now.

Hi Jai,
See below load testing issue and attached document.

Best,
Eric
-Eric Moy
Consultant - Exeter Group, Inc.
800 Boylston St. Suite 3500
Boston, MA 02199
emoy@exeter.com | Office: (617) 528-5151 | Cell: (240) 694-5093
From: Balasundaram, Kishore Kumar [mailto:kishorekumar.balasundaram@cgi.com]
Sent: Tuesday, November 04, 2014 10:58 AM
To: Eric Moy
Subject: FW: I am running 100 Users anonymous shopping right now.

From: Dale, Graham
Sent: Monday, November 03, 2014 2:32 PM
To: Kalu Marakkala, Peshan S; Balasundaram, Kishore Kumar; Ashok, Vasudev
Cc: sprather@adt.com
Subject: RE: I am running 100 Users anonymous shopping right now.
5

Hi guys,
Here is the default for the 100 user ‘Anonymous shopping’ test.
As I pointed out there were significant and chronic failures on comparing plans for both health and dental.
I did not note any notable response times for those transactions at all. They are sub 10 seconds across the board.
I will let you guys do what you need to do to investigate and will be here available for retest as needed.
Thanks,
Graham

From: Kalu Marakkala, Peshan S
Sent: Monday, November 03, 2014 4:12 PM
To: Dale, Graham; Balasundaram, Kishore Kumar; Ashok, Vasudev
Cc: sprather@adt.com
Subject: RE: I am running 100 Users anonymous shopping right now.

+ Vasu.
From: Kalu Marakkala, Peshan S
Sent: Monday, November 03, 2014 12:10 PM
To: Dale, Graham; Balasundaram, Kishore Kumar
Cc: sprather@adt.com
Subject: RE: I am running 100 Users anonymous shopping right now.

Let’s use this bridge –
Dial-in : 8553476250
Meeting ID : 4012137

Peshan Kalu Marakkala, OCE (SOA), OCS (Identity Management)
Executive Consultant (Technical Director), CGI
CGI Technical and Development Team Manager, HI-HIX
CGI | 720 S. Colorado Blvd Suite 1000-South Tower| Denver CO 80246
6

mobile : 612-231-9733
peshan.kalumarakkala@cgi.com | www.cgi.com

CONFIDENTIAL NOTICE: Proprietary/confidential information belonging to CGI Group Inc. may be contained in this
message. If you are not a recipient indicated or intended in this message (or responsible for delivery of this message
to such person), or you think for any reason that this message may have been addressed to you in error, you may
not use or copy or deliver this message to anyone else. In such case, you should destroy this message and are asked
to notify the sender by reply email.
From: Dale, Graham
Sent: Monday, November 03, 2014 11:58 AM
To: Balasundaram, Kishore Kumar; Kalu Marakkala, Peshan S
Cc: sprather@adt.com
Subject: RE: I am running 100 Users anonymous shopping right now.

Hi guys,

I am observing a majority of the comparison transactions failing which was something we observed with some other
States last year.
I think that we should take a look at what is going on to cause this.
I can jump on a bridge if you need me to.
Thanks,
Graham

From: Balasundaram, Kishore Kumar
Sent: Monday, November 03, 2014 3:49 PM
To: Dale, Graham
Cc: Kalu Marakkala, Peshan S
Subject: RE: I am running 100 Users anonymous shopping right now.

Thank you much!

7

From: Dale, Graham
Sent: Monday, November 03, 2014 1:48 PM
To: Balasundaram, Kishore Kumar
Cc: Kalu Marakkala, Peshan S
Subject: RE: I am running 100 Users anonymous shopping right now.

It is running again now
From: Balasundaram, Kishore Kumar
Sent: Monday, November 03, 2014 3:43 PM
To: Dale, Graham
Cc: Kalu Marakkala, Peshan S
Subject: RE: I am running 100 Users anonymous shopping right now.

Hi Graham
Can you please stop and restart 100 users anonymous shopping script. There were some errors in logs which we
found and fixed.

Thank you,
Kishore

From: Dale, Graham
Sent: Monday, November 03, 2014 12:04 PM
To: Kalu Marakkala, Peshan S; Balasundaram, Kishore Kumar
Subject: I am running 100 Users anonymous shopping right now.

Graham Dale
Consultant - BSOD
Performance Test Engineer
2100 Digby Drive | Belton, TX | 76513
Email: Graham.Dale@cgi.com
Phone: 254.316.4110
Cell: 512.299.3529
Fax: 254.774.4430

8


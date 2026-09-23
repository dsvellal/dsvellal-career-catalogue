# DoTheRightThing CreatingUtilityProjects August14th2014

> Converted from document `DoTheRightThing_CreatingUtilityProjects_August14th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Anuroop V. Gaonkar
Tuesday, October 14, 2014 2:19 PM
Dattatreya Subramanya Vellal; Anagha Joshi; Vinay Shivanna
Karthikeyan Vellingiri; Shrinidhi Irodi; Manasa Swamy; Sindhu Handalagere Suresh
RE: Learnings from ONEGATECORE-14710

Hi Datta,
Good to see one owner (Sindhu + Manasa) and one project for all utility work. Any time we need a utility function we
should first look inside this. If not present add the function to appropriate class here.
StringUtils
DateUtils
PlanUtils
ContactUtils
Etc.
Manasa & Sindhu,
You should be looking across all existing portlets and gathering all utility functions defined there & start providing
refactored implementation of those functions in appropriate utility classes in the project that you have created.
Hope you have already done that.
Key criteria for utility functions are, those need to be thread safe & those should not maintain state. If utility class
has to maintain state, then there should be forcing function to create a new instance from the class whenever any
other code wants to use that utility function.
Prime example is StringTokenizer. There are no static functions there. If I were to use StringTokenizer, then I need to
create a new instance. This is done because StringTokenizer has to remember state.
Please let me know about the progress made.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Dattatreya Subramanya Vellal
Sent: Tuesday, October 14, 2014 2:09 PM
To: Anuroop V. Gaonkar; Anagha Joshi; Vinay Shivanna
Cc: Karthikeyan Vellingiri; Shrinidhi Irodi; Manasa Swamy; Sindhu Handalagere Suresh
Subject: RE: Learnings from ONEGATECORE-14710

Anuroop – we are going to centralize the logic, but compare may become a part of our “view” and not a library with
objects (and values) coming from DL. However, for 3.3.2.11, I know that Manasa and Sindhu have created a common
utility project called og-utility used to centralize address-verification process. Perhaps we can use that?
Marking Manasa, Sindhu – pls share details.
Regards,
Datta
1

Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Anuroop V. Gaonkar
Sent: Tuesday, October 14, 2014 1:23 PM
To: Anagha Joshi; Vinay Shivanna
Cc: Dattatreya Subramanya Vellal; Karthikeyan Vellingiri; Shrinidhi Irodi
Subject: FW: Learnings from ONEGATECORE-14710

Vinay,
I believe you may have need for this in the Plan Selection. Are you already centralizing this in shared util library?
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Karthikeyan Vellingiri
Sent: Tuesday, October 14, 2014 12:35 PM
To: Shrinidhi Irodi
Cc: Anuroop V. Gaonkar; Krishnamurthy Hegde
Subject: Learnings from ONEGATECORE-14710

Hi Shrinidhi,
ONEGATECORE-14710 is fixed finally and OPS ticket has been raised.
While fixing this JIRA, I realised that the code related to Plan Comparison should be moved to a common location or
shared library which could be shared by the four portlets namely AnonEmployerPlanShop,
AnonymousPlanShoppingPortlet, EmployerPlanSelection, hixHealthPlan.
The FOUR above mentioned portlets have the same code related to Plan Comparison. It would be good if we could
move it to a shared library. This in turn will make the code changes, enhancements and the fixes easier. Also, this
would reduce the number of lines and increase code reusability.
Even a small change requires the fix from four portlets which in turn increases the LOE and the testing effort
although the same fix is made everywhere.
Please let me know your thoughts on this.
Regards,
Karthikeyan V
Karthikeyan Vellingiri
EXETER

Email ID: kvellingiri@exeter.com | Mobile: +91 9036461533 | Skype: karthik.kkn

2


# ReleaseSupport IndiaManagement July29th2013

> Converted from document `ReleaseSupport_IndiaManagement_July29th2013.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:
Attachments:

Krishnamurthy Hegde
Monday, July 29, 2013 4:29 AM
Lakshmi Thanga-Raja; Martin Schwartz; James Yoon; Laura Kling; Alana Reid; Edward
Chan; Finian O'Neill; Alice Ren; Andrew Hoffman; Matt Cha; Minhaj Chowdhury; Ryan
Leahy; Eric Moy; Richard Kang
Karen Zee; Aditya Adiga B.; OneGate-Ops; Dattatreya Subramanya Vellal; Vinay
Sulumane Visweswara; Chandrashekhar Surendranath; Anuroop V. Gaonkar
RE: QA Release 7/28 - Batch 2
Employer-Application-Plan Selection - Workaround on TEST

Thanks to Datta and Vinay SV, we have Employer Plan Selection deployed on TEST. Please refer to the attached email
for the one specific workaround in order to perform end-to-end testing (from application to plan selection). Thanks
much Thomas for helping with the configuration issues and the EG OPS team for the quick turnaround.
QA team - Please test the application and provide your feedback, once Siebel is up.
Lakshmi – we have not been able to get through the Employee plan selection flow.
Regards,
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Off: +91-80-33450029 | Skype:
khegde
From: Lakshmi Thanga-Raja
Sent: Sunday, July 28, 2013 11:46 PM
To: Martin Schwartz; James Yoon; Laura Kling; Alana Reid; Edward Chan; Finian O'Neill; Alice Ren; Andrew Hoffman;
Matt Cha; Minhaj Chowdhury; Ryan Leahy; Eric Moy; Richard Kang
Cc: Karen Zee; Aditya Adiga B.; OneGate-Ops
Subject: FW: QA Release 7/28 - Batch 2

From: Krishnamurthy Hegde
Sent: Sunday, July 28, 2013 2:14 PM
To: Martin Schwartz; Lakshmi Thanga-Raja
Cc: OneGate-Ops; Chandrashekhar Surendranath; Anuroop V. Gaonkar
Subject: RE: QA Release 7/28 - Batch 2

Hi Martin Lakshmi,
Below are the items that is available for EG QA
Employer Application
o 6039 - SHOP Employer Security Code not appearing in Siebel – Fix in progress. To be done tomorrow.
o 6109 - Advanced SHOP No groups configured. – Issue resolved on TEST.
o 6010 - Benefit Line items for employers update – Issue resolved on TEST.
o 6111/6073- Push Enrollment Dates to Group Policy – Issue resolved on TEST.
o 6114 - Large rosters crashing employer determination – No success with this. Requesting EG help in resolving
this. If there is no breakthrough tomorrow, we would resort to a ‘scripting’ solution to get it working for 3.3.
o 6122 - DRE: Group Restrictions for Optional Employees to Mandatory groups – Issue resolved on TEST
o 6123) Push OPA fields to Siebel in Employer Application – Issue resolved on TEST
o 6124) DRE: Account Object does not have an Unemployment Tax ID field to capture unemployment tax id
from the interview – Issue resolved on TEST.
o 6125 - Employer SBTC Determination Wrong – Not an issue. Assigned to Eddie for clarification and closure.
Manual BED
o 16/16 cases passed on test. Manual BED now incorporates SLCSCP as well.
1

o
o

6116 - Error message when changing benefit line item status to Approved – Issue resolved on TEST.
6117 - Error message during Manual BED – this is an issue with Vermont Rulebase. Could not verify due to
other ongoing dev/testing. Will be taken up tomorrow. It would be good if the EG QA team validates this
issue since there is no real difference in the rulebase between the Vermont and Hawaii versions.

Employee Application:
• Flow up to Application submission (summary screen) is working fine.
Nav Broker
o 5833- Nav/Broker case creation failed at Siebel end due to the mismatch in timezones of timestamps
between Siebel and SOA and occurs only at specific time range. – Here is the update from Nagendra
“Checked the time stamp on all the 4 servers (SOA,SBL,DB,APP), found no difference in time or
timezone settings. however the Timezone system preference in Siebel application was set to PST;
changed the same to EST. This change should reflect in the next Siebel restart.” EG team – can this be
tested please?

There is one update (not of consequence) from the previous Batch 1 update.
There would be no more releases today. We are facing technical (spring configuration related) issues after we
merged the Employer Application and Plan Selection code. We are seeking help from the EG team to see if it can be
resolved. Hence, Employer and Employee plan selection will not be available today.

Thanks,
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Off: +91-80-33450029 | Skype: khegde
From: Krishnamurthy Hegde
Sent: Sunday, July 28, 2013 8:14 PM
To: Martin Schwartz; Lakshmi Thanga-Raja
Cc: OneGate-Ops; Chandrashekhar Surendranath; Anuroop V. Gaonkar
Subject: QA Release 7/28 - Batch 1

Hi Martin, Lakshmi,
Here is the set of features that are stable on TEST1 and EG QA team can have a go:
IF Application
o 5955 - Copays and Deductibles for CSR = N/A – Issue under investigation. Assigned to Siebel team.
o 6072, 6079, 6082 – LOV issues - Issues resolved on TEST.
o 6077, 6080, 6084, 6086, 6087, 6093, 6095 – App submission errors – duplicate issues - Issues resolved on
TEST.
IF Plan Selection
• 5744 - Plan Selection not Working in terms of Pushing to Siebel - Issues resolved on TEST
• 5853 - Mismatch between premiums in Siebel and displayed in Portal – Need functional clarification.
Assigned to Rob.
• 5858 - Multiple Plans in Health Policy in Siebel APTC Issues - Issues resolved on TEST.
• 6104 - Select a Plan for Medicaid throws an error – Still an issue. Investigation underway. Initial sense is that
it is a portal issue and is assigned to Rob.
• 6129 - Save Advance Tax Credit via SOA to Siebel returns success but does not update the
Household.SelectedAPTC - Issues resolved on TEST
• 6130 - My Eligibility Tab not displaying Plan Selection Next Step - Issues resolved on TEST
• 6064/6069 - PS: After selecting a QHP plan and enrolling for IF, in siebel under that plan the policy coverages
and member coverages are blank - Issues resolved on TEST
2

Thanks,
Krishna
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Off: +91-80-33450029 | Skype: khegde

3


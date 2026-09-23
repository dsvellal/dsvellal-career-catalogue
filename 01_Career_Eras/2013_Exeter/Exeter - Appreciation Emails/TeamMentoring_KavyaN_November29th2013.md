# TeamMentoring KavyaN November29th2013

> Converted from document `TeamMentoring_KavyaN_November29th2013.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Kavya Nagabhushan
Friday, November 29, 2013 11:27 AM
Dattatreya Subramanya Vellal
RE: Functionality clarification for Employer Disenrollment 3.3.2.7

Thanks Datta ☺ All the credit goes to you!
I would be more than happy to take up many more such tasks ☺
Thanks,
Kavya Nagabhushan
Mobile: +91 9886 887 995 | Skype id: kavya.bhushan | Email: knagabhushan@exeter.com

From: Dattatreya Subramanya Vellal
Sent: Friday, November 29, 2013 11:24 AM
To: Kavya Nagabhushan
Subject: RE: Functionality clarification for Employer Disenrollment 3.3.2.7

Very well structured indeed. The key is to drive decisions like these and not wait for answers!
Going forward, we should start suggesting designs and get FSDs aligned to the designs. BAs should give us
requirements, we should design for it.
This however is a very solid start.. kudos to you and the team!
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chandrashekhar Surendranath
Sent: Friday, November 29, 2013 11:05 AM
To: Kavya Nagabhushan
Cc: Anuroop V. Gaonkar; Dattatreya Subramanya Vellal
Subject: Re: Functionality clarification for Employer Disenrollment 3.3.2.7

Very well structured interaction. Keep these standards.
Regards
Shekhar
Sent from handheld. Please excuse typos.
On Nov 29, 2013, at 10:17 AM, "Kavya Nagabhushan" <knagabhushan@exeter.com> wrote:
Hi Eddie,
It is possible to go ahead with a check on Employer Registration Deadline field. We can also have
the functionality of involuntary disenrollment of Employee if the Employer disenrolls from plans
before Employer Registration Deadline. These will be included for this release.
However I have another concern with this. If the Employer disenrolls from a reference plan, then all
the contributions and costs would change. In this case, the Employer contribution and Final cost for
ALL the employees who have selected plans would have to change. Please come up with a design for
1

this for the next release. For this release we will not make any changes to the premiums even if the
reference plan is disenrolled.
Also could you please update the FSD with this information after you are back next week. Enjoy your
Thanksgiving! ☺
Thanks,
Kavya Nagabhushan
Mobile: +91 9886 887 995 | Skype id: kavya.bhushan | Email: knagabhushan@exeter.com

From: Edward Chan
Sent: Friday, November 29, 2013 9:06 AM
To: Kavya Nagabhushan; Karen Zee; James Yoon
Cc: Jonah Egenolf; Chevy Vithiananthan; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar;
Krishnamurthy Hegde; Chandrashekhar Surendranath; Shrinidhi Irodi; Lakshmi Thanga-Raja
Subject: RE: Functionality clarification for Employer Disenrollment 3.3.2.7

Thanks Kavya for providing a solution. I am fine with this solution with additional comments
provided inline. I have an open item with both implementation teams waiting on use cases
and designs around possibility of "in coverage year" disenrollment by employers. Until we
receive additional requirements I don't see an issue with restricting employer disenrollment
to the employer's "open enrollment period."
From: Kavya Nagabhushan
Sent: Thursday, November 28, 2013 10:29 AM
To: Karen Zee; James Yoon; Edward Chan
Cc: Jonah Egenolf; Chevy Vithiananthan; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar;
Krishnamurthy Hegde; Chandrashekhar Surendranath; Shrinidhi Irodi; Lakshmi Thanga-Raja
Subject: Functionality clarification for Employer Disenrollment 3.3.2.7
Hi Team,
The FSD for Employer Disenrollment 3.3.2.7 can be found here. There are various scenarios that
need a functional review and hence blocking our development. Some of them are listed below,
Involuntary disenrollment of Employee when Employer disenrolls from a plan
1.

When an Employer disenrolls from a plan, all the employees and their dependents under
that plan are automatically disenrolled
2. The Employee cannot enroll into another plan if Employee Enrollment End Date in the
Group Policy is in the past
3. So this leaves with no enrolled plan for the Employee and/or dependents
Disenrollment of dependent plans/ Reference plans
1.

When a plan is dependent on other plans, all the dependent plans also must be disenrolled.
This can include the reference plan selected for a product type. A reference plan can also be
selected for disenrollment.
2. This can bring up a scenario where all the plans in a group are disenrolled leaving behind all
Employees in that group with no enrolled plan. They cannot enroll into any other plan until
the Employer enrolls into more plans and the End date has not lapsed
3. When a reference plan is disenrolled, and another reference plan is chosen, all the plan
premiums need to be recalculated. This would imply that the Plan premium, Employer
contribution and final cost for every enrolled employee needs to change. Also, all these
changes need to happen on the particular date given for disenrollment by the Employer.
Until then all costs should remain as it is
2

4.

During all the above cases, the Employee would be unaware of anything that is happening.
The monthly cost for the plan he is enrolled in can change without his notice
5. There can be many more such scenarios like this that need to be addressed
At this point of time, given the timeline restrictions, we feel the below solution would be apt
Employer can disenroll from plans ONLY before the Employee Enrollment Start Date
EC: Let's use the Employer Registration Deadline field. I want to get to a construct of
employers able to make changes prior to this deadline, then employees making changes
during employee open enrollment.
2. After the dates are open for Employees to enroll, there would be a set of plans to which the
Employer commits
EC: If we move to Employer Registration Deadline, there does exist overlapping
employer/employee open enrollment periods for VT. In this case, we would want the
employees that signed up to be involuntarily disenrolled. If we remove the plans from the
group policy, can we also just verify that the plans get dissassociated with any employees
that had gone in and selected plans? I think this is ok because that was the original point of
having an "Employer Registration Deadline"
This is not an issue for HI because they did not request rule changes for determination of
employer registration deadline and employee open enrollment dates.
3. On click of disenroll link by the Employer, a check would be made for the Employee
Enrollment Start Date and the Employer can disenroll from plans ONLY if the current date is
greater
EC: Let's use the Employer Registration Deadline field.
4. If Employee Enrollment Start Date has lapsed, then a message would be shown in a
graceful manner indicating that the Employer cannot make any changes to the set of plans
EC: Let's use the Employer Registration Deadline field.
5. In this way there would not be any involuntary disenrollment of Employee and also there
would not be any conflicts based on reference plan. The Employee would not be disenrolled
automatically from any plan.
EC: See #2
Please review this proposed change and let us know if there are any other ways of implementing the
same. Datta and I are open for any calls or clarifications regarding this.
1.

Thanks,
Kavya Nagabhushan
Mobile: +91 9886 887 995 | Skype id: kavya.bhushan | Email: knagabhushan@exeter.com

3


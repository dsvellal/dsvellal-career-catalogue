# DoTheRightThing AnalysisBeforeCodeRevampSuggestion February21st2014

> Converted from document `DoTheRightThing_AnalysisBeforeCodeRevampSuggestion_February21st2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Anuroop V. Gaonkar
Friday, February 21, 2014 3:52 PM
Dattatreya Subramanya Vellal; Chandrashekhar Surendranath
Krishnamurthy Hegde; Shrinidhi Irodi
RE: Root cause analysis of ONEGATECORE-13562

Follow Up Flag:
Flag Status:

Follow up
Completed

1000% Yes. Redesign & Refactoring both have to happen. Redesign – based on principles. Then refactor. Don’t
refactor before redesign.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Dattatreya Subramanya Vellal
Sent: Friday, February 21, 2014 2:08 PM
To: Chandrashekhar Surendranath
Cc: Krishnamurthy Hegde; Anuroop V. Gaonkar; Shrinidhi Irodi
Subject: RE: Root cause analysis of ONEGATECORE-13562

Hello Shekhar,
The issue: http://172.10.10.57:8080/jira/browse/ONEGATECORE-13562 hit us badly – with multiple reopens. The
root-cause analysis is given in the mail below and a good fix made to make sure that this does not occur again in
3.3.2.7hf3. As an outcome of this exercise, we have noticed that in our code base, we have code which is:
- Not required, but are not removed because its legacy code
- Intertwined with lot of conditional statements performing the same set of actions
- Highly non-modular, controlled by conditional statements
- Repetitive and/or dead
The above patterns are visible in –
- HealthPlanSelectionController.java of hixHealthPlan Portlet
- EmployerPlanSelectionController.java and jsps of EmployerPlanSelection Portlet
- Controllers of MyAccount and MyAccount-SHOP portlets
- Controllers of AnonymousPlanShopping and AnonEmployerPlanShop portlets
A phase-wise clean-up will definitely help us eliminate such errors in future. I foresee the following phases:
- Phase 1: Remove dead/unused code from controllers and jsps
- Phase 2: Modularize the code base within the controllers and jsps
- Phase 3: Pull out commonly used modules, and push them into a single utility module – so that code
maintenance becomes easy
I would like to run this by you to know if and when we can start off with phase 1, as an activity during our slack time
not affecting the release, and introduce these changes into a stream at an agreed time.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Peter Alphonso Mascarenhas
Sent: Friday, February 21, 2014 12:59 PM
1

To: Dattatreya Subramanya Vellal
Cc: Shrinidhi Irodi; Krishnamurthy Hegde; Anuroop V. Gaonkar; Dharnesh Yediyurappa; Satheesh Kumar Raju; Sachin
Shivarama Nayak
Subject: Root cause analysis of ONEGATECORE-13562

Hi Datta,
ONEGATECORE-13562 was an issue with blocking EE from adding the same product type plan if one already exists in
cart.
This was not implemented for the EE flow.
Fix made :
Generic method called and in brief check made against product type of plan in cart and added plan by EE.
Variable used is “String productType” under InsurancePlan Domain class.
*************************************************************************
1st failed case:
We realized that product type was being set wrongly for QHP ( set to ”SHOP” instead of “Health Insurance”)
However it worked fine for both Dental and Vision plans.
This was not the case on HFDEV as QHP plans were being blocked too.
Fix made:
QHP case was changed to make a check for “SHOP” as well as “Health Insurance”
Fix worked on HFDEV(were we never had a failed case), HFTEST but failed on ESIPR.
2nd failed case:
productType check was now failing for Dental Insurance as well. Worked for QHP. Provided logs suggested that
Product type was coming as SHOP instead of Dental Insurance.
This behavior was very erratic as seen by QA. Failed one in 3 times.
Fix:
Spoke to Sachin and was told that the productType for SHOP case is erratic and hence a correct variable was done by
him. The correct variable is AssociatedProdType under InsurancePlan domain class.
On using this variable a generic fix made across all product types although the method was duplicated as the fix was
urgent.
Fix worked on all instances.
**************************************************************************
We believe that a cleaner fix can be made and we will be looking into why productType was coming in wrong for
SHOP case in the first place .
The clean fix will be made on Trunk.

Regards,
Peter Mascarenhas
EXETER

Skype: petermasky | mobile: +919738527060

2


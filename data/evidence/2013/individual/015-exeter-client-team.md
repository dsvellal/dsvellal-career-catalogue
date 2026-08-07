---
title: "Client Team"
date: 2013-01-01
year: 2013
era: Exeter
organization: Exeter (Edifecs)
category: Troubleshooting & Defect Ownership
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Anuroop V. Gaonkar"]
skills: ["Data Layer", "Liferay Portal", "Portal Development", "Root Cause Analysis", "SOA", "Troubleshooting"]
programs: ["OneGate"]
tags: ["appreciation", "troubleshooting-&-defect-ownership"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Client Team

## Source
- **File:** `TroubleShooting&DefectOwnership_ClientTeam_July8th2013.pdf`
- **Date:** 2013-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Troubleshooting & Defect Ownership

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 2

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> To: Dattatreya Subramanya Vellal; Peter Devlin; Sajith Sanal; Shridhar Narasinha Kulkarni;

## Full Content
```
Dattatreya Subramanya Vellal
From: Jon-Paul Berexa
Sent: Monday, July 08, 2013 9:56 AM
To: Dattatreya Subramanya Vellal; Peter Devlin; Sajith Sanal; Shridhar Narasinha Kulkarni;
Anuroop V. Gaonkar
Subject: RE: HI HIX Deployment Troubleshooting
It worked!
The difference between what was done yesterday and what was done today is that the Update button was pressed
in the Admin console. Yesterday I only stopped and started the portlet, per the instructions in the email. It seems
that the new JARs did fix the problem, as you predicted. Both the individual and employee flows are working now
without looping.
Thank you for all of your help. We are going to move to the KPMG deployment issue so we may be reaching out
concerning that as well.
Thanks,
Jon-Paul
_____________________________________________
From: Dattatreya Subramanya Vellal
Sent: Sunday, July 07, 2013 6:01 PM
To: Peter Devlin; Sajith Sanal; Shridhar Narasinha Kulkarni; Anuroop V. Gaonkar; Jon-Paul Berexa
Subject: RE: HI HIX Deployment Troubleshooting
My apologies.
Please find updated steps here.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
_____________________________________________
From: Dattatreya Subramanya Vellal
Sent: Monday, July 08, 2013 9:27 AM
To: Peter Devlin; Sajith Sanal; Shridhar Narasinha Kulkarni; Anuroop V. Gaonkar; Jon-Paul Berexa
Subject: RE: HI HIX Deployment Troubleshooting
Hello Jon-Paul, Peter,
Please find the steps to set the logging level and collecting the right logs at Portal layer:
<Configure Log Levels>
1. Go to Portal Admin console, and stop the hixHealthPlan Portlet
2. Go to the portal web/guest console (<ip:port>/web/guest)
3. Login as administrator (the credentials used to add a particular portlet into a page - eg: test/test)
4. Click on "Control Panel > Server Administration" - This should take you to the server administration page
5. Now, click on "Log Levels" (direct link sample URL: 172.10.10.142:7004/group/control_panel/manage/-
/server/log-levels)
6. Change the log-level of "com.exeter to "ALL"
<Clearing the logs>
7. Winscp to the Portal Server
1
8. Navigate to the following location: /u01/app/oracle/mw_home_1/user_projects/domains/logs
9. In this folder, you will see many logs bearing the name: liferay.2013-07-07.log
10. Kindly rename the latest log file to - <logfileName>_bak.log
<Updating the portlet>
11. On the browser, go to the Portal admin console (where you start/stop a portlet)
12. Press "Lock and Edit" at the top left panel
13. Select - hixHealthPlan portlet's check box
14. Click on "Update"
15. Click "Activate Changes" if it is active
<Retake the interview>
16. Start the hixHealthPlan Portlet from the admin console
17. Retake the interview to get the new logs - stored in this location:
/u01/app/oracle/mw_home_1/user_projects/domains/logs
Please find the steps to collect the SOA EM Logs:
1. SOA url : http://SOAServerURL:port/em
2. Login to SOA server using credentials.
3. Click on default

```

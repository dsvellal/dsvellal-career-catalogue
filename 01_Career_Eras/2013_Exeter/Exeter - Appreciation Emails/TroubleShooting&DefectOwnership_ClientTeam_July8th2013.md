# TroubleShooting&DefectOwnership ClientTeam July8th2013

> Converted from document `TroubleShooting&DefectOwnership_ClientTeam_July8th2013.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Jon-Paul Berexa
Monday, July 08, 2013 9:56 AM
Dattatreya Subramanya Vellal; Peter Devlin; Sajith Sanal; Shridhar Narasinha Kulkarni;
Anuroop V. Gaonkar
RE: HI HIX Deployment Troubleshooting

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
Go to Portal Admin console, and stop the hixHealthPlan Portlet
Go to the portal web/guest console (<ip:port>/web/guest)
Login as administrator (the credentials used to add a particular portlet into a page - eg: test/test)
Click on "Control Panel > Server Administration" - This should take you to the server administration page
Now, click on "Log Levels" (direct link sample URL: 172.10.10.142:7004/group/control_panel/manage//server/log-levels)
6. Change the log-level of "com.exeter to "ALL"
<Clearing the logs>
7. Winscp to the Portal Server

1.
2.
3.
4.
5.

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
4. select "OneGateHIXInterviewService"
5. Select instanceId, this will open composite BPEL process(if instanceId is not latest press refresh button as
indicated in screenshot). Once BPEL process gets opened, verify any error you find in process. If yes, please
send across that error.
Please find attached screenshots for above mentioned SOA steps.
<< File: ScreenShot_to_collect_SOA_EM_Logs.rar >>
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal

-----Original Appointment----From: Peter Devlin
Sent: Monday, July 08, 2013 8:23 AM
To: Peter Devlin; Dattatreya Subramanya Vellal; Sajith Sanal; Shridhar Narasinha Kulkarni; Anuroop V. Gaonkar; JonPaul Berexa
Subject: HI HIX Deployment Troubleshooting
When: Monday, July 08, 2013 8:30 AM-9:00 AM (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi.
Where: 1-800-689-9374 722891#

We can use this conference line 1-800-689-9374 722891#
Here is a join me invite for screen sharing.
https://join.me/957-824-060

2


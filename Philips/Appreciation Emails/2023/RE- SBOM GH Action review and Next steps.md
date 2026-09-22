# RE: SBOM GH Action review and Next steps

**From:** "Dash, Biswo Ranjan" <bisworanjan.dash@philips.com>  
**To:** "Knoops, Jeroen" <jeroen.knoops@philips.com>, "Subramanya Vellal, Dattatreya" <dsvellal@philips.com>, "Kannanth, Amrithraj" <amrithraj.kannanth@philips.com>  
**Date:** Fri, 22 Sep 2023 12:13:23 +0000  

---

Hi Datta,

Thanks for your valuable inputs to get the action organized.

Below are Minutes of the discussion we had.


  1.  We had reviewed the NTIA conformance checker actions received the required inputs/feedbacks from Datta.

FeedBacks:


  1.  Specify the stable version of python and ntia-conformance-checker(Sandeep has to confirm the stable version of ntia-conformance-checker)
  2.  If BD version and projection is not available, it should exit with message that BD has to be configured first.
  3.  Ntia configuration check action should be independent having BD report functionality withing the same action.
  4.  Validation of SPDX report should be takencare from the workspace, if SPDX not present exit with error message.
  5.  SBOM report name should not be project independent.

We will have another meeting next week for upload action.


Regards,
Biswo

-----Original Appointment-----
From: Dash, Biswo Ranjan
Sent: Thursday, September 21, 2023 9:38 AM
To: Knoops, Jeroen; Subramanya Vellal, Dattatreya; Kannanth, Amrithraj
Cc: Patil, Sandeep; B M, Arun Kumar
Subject: SBOM GH Action review and Next steps
When: 22 September 2023 4.10 PM-4.50 PM (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi.
Where: Microsoft Teams Meeting

Hi Jeroen and Datta,

Keeping the meeting to review below two issues for SBOM and Next steps.



  1.  https://github.com/philips-internal/devops-ref-arch/issues/94<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fphilips-internal%2Fdevops-ref-arch%2Fissues%2F94&data=05%7C01%7Cdsvellal%40philips.com%7C16257ba2d95846519c1d08dbbb655191%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C638309816054438114%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=kgAXgVXIYON16cy4PIrR9kqQiv8HsxKQD9aXtSc6caA%3D&reserved=0>
  2.  https://github.com/philips-internal/devops-ref-arch/issues/95<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fphilips-internal%2Fdevops-ref-arch%2Fissues%2F95&data=05%7C01%7Cdsvellal%40philips.com%7C16257ba2d95846519c1d08dbbb655191%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C638309816054438114%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=fVk7kFNioDbm5Veo96abI0KJf5aa6MbQdHaSWoD9ZZE%3D&reserved=0>

Thanks & Regards,
Biswo


________________________________________________________________________________
Microsoft Teams meeting
Join on your computer, mobile app or room device
Click here to join the meeting<https://teams.microsoft.com/l/meetup-join/19%3ameeting_NjdhNmQyNzAtNDI3Yy00OWQxLTk2ZmEtODU3NjY2ZTNlN2M1%40thread.v2/0?context=%7b%22Tid%22%3a%221a407a2d-7675-4d17-8692-b3ac285306e4%22%2c%22Oid%22%3a%22a0380074-d37f-4b7d-9d0b-c716abd01024%22%7d>
Meeting ID: 346 486 365 255
Passcode: EV4gKL
Download Teams<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fmicrosoft-teams%2Fdownload-app&data=05%7C01%7Cdsvellal%40philips.com%7C16257ba2d95846519c1d08dbbb655191%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C638309816054438114%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=%2FnvSLTOQqbDVPUFYSu1JoRcPgyzvG0FH9dCrGwLc%2BEY%3D&reserved=0> | Join on the web<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.microsoft.com%2Fmicrosoft-teams%2Fjoin-a-meeting&data=05%7C01%7Cdsvellal%40philips.com%7C16257ba2d95846519c1d08dbbb655191%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C638309816054438114%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=hJUiERVOGv9%2FvUeEQtbCRb%2B0nKtj7bwqoXBmQQARC0A%3D&reserved=0>
Learn More<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting&data=05%7C01%7Cdsvellal%40philips.com%7C16257ba2d95846519c1d08dbbb655191%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C638309816054438114%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=F9JdZNyXeTa5aWx9O7009yn7a3JzUjbTsed9jinn9bM%3D&reserved=0> | Meeting options<https://teams.microsoft.com/meetingOptions/?organizerId=a0380074-d37f-4b7d-9d0b-c716abd01024&tenantId=1a407a2d-7675-4d17-8692-b3ac285306e4&threadId=19_meeting_NjdhNmQyNzAtNDI3Yy00OWQxLTk2ZmEtODU3NjY2ZTNlN2M1@thread.v2&messageId=0&language=en-US>
________________________________________________________________________________


________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.

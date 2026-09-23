# RE: Subramanya Vellal, Dattatreya shared "Kairos ReqSpec Demo-20260315_200040-Meeting Recording" with you

**From:** "Wiericx, Ronald" <ronald.wiericx@philips.com>  
**To:** "Subramanya Vellal, Dattatreya" <dsvellal@philips.com>, "Tekelenburg, Arjan" <Arjan.Tekelenburg@philips.com>  
**Date:** Fri, 20 Mar 2026 12:37:13 +0000  

---

Hi Datta,

I reviewed your video and uploaded a small section of our Element requirement specification. My main observation is that the user interaction with Kairos appears significantly more user-friendly. Below is an example showing a source requirement alongside the consolidated and improved version.

Looking forward to your demo next week.

Regards,
Ronald

Source Requirement (Verbatim):
When Positioning SW receives a movement request from one of the external interfaces, then it will send a brake release command to Motion Infra and use default acceleration.
Movement request with speed “0” is to be interpreted as a movement stop on which Positioning SW shall decelerate the movement and send a re-activate brake command to Motion Infra. (except for auto-centering movements and table float alternate mode).
Path deviation during programmed stops and movement stop on Positioning SW shall be below either 0.2 degrees or 2 mm as stated in SDS.POSDecoApp.Stopping.PathDeviations.PosSW.

Consolidated Improved Requirement (IEC 62304 Ed.1.1 Only):
US.PosSW.Func.BasicMovements.StartStopMovement
Safety Classification: [Class A/B/C or project-defined classification]
Category: Basic Movement Control
Parent Requirement: [System-level movement control requirement or risk control ID]

(a) When Positioning SW receives a movement request from an external interface with a speed greater than 0 mm/s, it shall:

  *   Send a brake release command to Motion Infra within [maximum latency ms].
  *   Initiate movement using the default acceleration value [default acceleration value, e.g., X mm/s²] as defined in SDS.POSDecoApp.Acceleration.PosSW.
  *   Continue movement until a stop condition is detected as defined in US.PosSW.Func.BasicMovements.RunCondition.
(b) When Positioning SW receives a movement request with speed equal to 0 mm/s, it shall:

  *   Decelerate the movement to a complete stop using the default deceleration value [default deceleration value, e.g., Y mm/s²] as defined in SDS.POSDecoApp.Deceleration.PosSW.
  *   Send a brake re-activate command to Motion Infra within [maximum latency ms].
  *   Exception: For auto-centering movements and table float alternate mode, this stop and brake re-activation sequence does not apply.
(c) During programmed stops and movement stops initiated by Positioning SW, the path deviation shall not exceed 0.2 degrees or 2 mm, measured at the relevant axis, as specified in SDS.POSDecoApp.Stopping.PathDeviations.PosSW.
(d) All actions described above shall be logged in the system event log with timestamp and movement request details for traceability.
(e) Movement requests and brake commands shall be communicated via [defined interface/protocol, e.g., iPosBehavior], specifying data type, format, and range as documented in [UID.PBPos.UI.movement_speed].


From: Subramanya Vellal, Dattatreya <dsvellal@philips.com>
Sent: Monday, March 16, 2026 4:28 AM
To: Tekelenburg, Arjan <Arjan.Tekelenburg@philips.com>; Wiericx, Ronald <ronald.wiericx@philips.com>
Subject: Subramanya Vellal, Dattatreya shared "Kairos ReqSpec Demo-20260315_200040-Meeting Recording" with you

[Share image]

Subramanya Vellal, Dattatreya invited you to view a file

Hey Ronald, Arjan,
I did a demo recording of usage of the prompt in Kiaros for one of the asset demonstrations for Kairos. Hopefully, this will be useful to you as well.

I will discuss more in our conversations this week, on how to leverage this tool to start generating BDD based scenarios as well.
[icon]<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.philips.com%2F%3Av%3A%2Fr%2Fpersonal%2Fdsvellal_philips_com%2FDocuments%2FDocuments%2FSWCoE%2F2026%2F20260314-Kairos-ReqSpec-Asset%2FKairos%2520ReqSpec%2520Demo-20260315_200040-Meeting%2520Recording.mp4%3Fe%3D4%253a932796e9535d4529a9a33c6f176b83f6%26web%3D1%26nav%3DeyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1FbWFpbCIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19%26sharingv2%3Dtrue%26fromShare%3Dtrue%26at%3D9&data=05%7C02%7Cdsvellal%40philips.com%7C12e601055d4944b1adc908de867d69b6%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639096070342096594%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=QKyaBHa1JwEzEY40MadXURu7DCdAEAYxuJB%2Ffp1hYLU%3D&reserved=0>
Kairos ReqSpec Demo-20260315_200040-Meeting Recording <https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.philips.com%2F%3Av%3A%2Fr%2Fpersonal%2Fdsvellal_philips_com%2FDocuments%2FDocuments%2FSWCoE%2F2026%2F20260314-Kairos-ReqSpec-Asset%2FKairos%2520ReqSpec%2520Demo-20260315_200040-Meeting%2520Recording.mp4%3Fe%3D4%253a932796e9535d4529a9a33c6f176b83f6%26web%3D1%26nav%3DeyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1FbWFpbCIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19%26sharingv2%3Dtrue%26fromShare%3Dtrue%26at%3D9&data=05%7C02%7Cdsvellal%40philips.com%7C12e601055d4944b1adc908de867d69b6%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639096070342119048%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=12SUbOLsOk1TkQrbTJ5pz8%2BxpqnciGRCH6FmLAMBK%2BQ%3D&reserved=0>
[permission globe icon]
This invite will only work for you and people with existing access.
[Open - Description: Rectangle: Rounded Corners: Open]<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.philips.com%2F%3Av%3A%2Fr%2Fpersonal%2Fdsvellal_philips_com%2FDocuments%2FDocuments%2FSWCoE%2F2026%2F20260314-Kairos-ReqSpec-Asset%2FKairos%2520ReqSpec%2520Demo-20260315_200040-Meeting%2520Recording.mp4%3Fe%3D4%253a932796e9535d4529a9a33c6f176b83f6%26web%3D1%26nav%3DeyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1FbWFpbCIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19%26sharingv2%3Dtrue%26fromShare%3Dtrue%26at%3D9&data=05%7C02%7Cdsvellal%40philips.com%7C12e601055d4944b1adc908de867d69b6%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639096070342135324%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=%2FeY%2Bj9kmR2PkDWnOj265qjk8s6%2B0M5hddRpv4OKVJyA%3D&reserved=0>
[Share - Description: Rectangle: Rounded Corners: Share]<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.philips.com%2F%3Av%3A%2Fr%2Fpersonal%2Fdsvellal_philips_com%2FDocuments%2FDocuments%2FSWCoE%2F2026%2F20260314-Kairos-ReqSpec-Asset%2FKairos%2520ReqSpec%2520Demo-20260315_200040-Meeting%2520Recording.mp4%3Fe%3D4%253a932796e9535d4529a9a33c6f176b83f6%26web%3D1%26nav%3DeyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1FbWFpbCIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19%26openShare%3Dtrue%26fromShare%3Dtrue%26at%3D9&data=05%7C02%7Cdsvellal%40philips.com%7C12e601055d4944b1adc908de867d69b6%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639096070342150776%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=B55JExlXLDQB7r1NMQgQtfBDwErq7mGe5xW9wDC3UGo%3D&reserved=0>
[cid:image006.png@01DCB868.C3FBA230]

This email is generated through Philips's use of Microsoft 365 and may contain content that is controlled by Philips.

________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.

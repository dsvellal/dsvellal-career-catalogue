# Re: Access to DevPortal broken

**From:** "Jha, Eeshani (Partner)" <partner.Eeshani.Jha@philips.com>  
**To:** "Subramanya Vellal, Dattatreya" <dsvellal@philips.com>, "Pichel, Stefan" <stefan.pichel@philips.com>, "Kumar, Nataraj" <nataraj.kumar@philips.com>, "Saavedra, Alexis" <alexis.saavedra@philips.com>  
**Date:** Mon, 20 Jul 2026 14:31:33 +0000  

---

Yes, I am able to access it now

Thanks a lot
________________________________
From: Subramanya Vellal, Dattatreya <dsvellal@philips.com>
Sent: Monday, July 20, 2026 7:56 PM
To: Jha, Eeshani (Partner) <partner.Eeshani.Jha@philips.com>; Pichel, Stefan <stefan.pichel@philips.com>; Kumar, Nataraj <nataraj.kumar@philips.com>; Saavedra, Alexis <alexis.saavedra@philips.com>
Cc: Terol, David <david.terol@philips.com>; Guymer, Scott <Scott.Guymer@philips.com>
Subject: Re: Access to DevPortal broken

This has been fixed for Eeshani. Alexis helped us out here. Thank you, Alexis.

@Jha, Eeshani (Partner)<mailto:partner.Eeshani.Jha@philips.com> - can you try accessing developer portal again?

We are internally tracking this issue: https://github.com/philips-internal/developer-portal/issues/4026<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fphilips-internal%2Fdeveloper-portal%2Fissues%2F4026&data=05%7C02%7Cdsvellal%40philips.com%7C0b41e8259c894028398308dee66b9907%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639201546976132107%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=xLn%2FNfY7CGnHuhmbpLNiysOFAXt2TMUsninjBMhHlvU%3D&reserved=0> to make sure we provide better UX for users facing similar issues. Please follow and update this issue if you face similar concerns.

-- Datta
Software Competency Lead
Innovation Engineering, Innovation & Design

From: Jha, Eeshani (Partner) <partner.Eeshani.Jha@philips.com>
Date: Monday, July 20, 2026 at 10:13
To: Pichel, Stefan <stefan.pichel@philips.com>; Subramanya Vellal, Dattatreya <dsvellal@philips.com>; Kumar, Nataraj <nataraj.kumar@philips.com>
Subject: Re: Access to DevPortal broken

Hello Everyone ,

@Subramanya Vellal, Dattatreya<mailto:dsvellal@philips.com> - suggested to remove my earlier personal mail linked to my personal github account and add a new personal email to EESHANI-11

So as to check if user entitlement can return null on lookup

We did this but we are still facing the same error 409 :

User lookup resulted in multiple matches

[cid:bbca56da-b5a1-492b-bbbc-219a97967ce5]

________________________________
From: Pichel, Stefan <stefan.pichel@philips.com>
Sent: Monday, July 20, 2026 4:57 PM
To: Subramanya Vellal, Dattatreya <dsvellal@philips.com>; Kumar, Nataraj <nataraj.kumar@philips.com>
Cc: Jha, Eeshani (Partner) <partner.Eeshani.Jha@philips.com>
Subject: FW: Access to DevPortal broken


Hello Dattatreya, hello Nataraj,



since both Scott and David are on vacations and David points in the OOO message to you for any engineering topics, may I ask you to have a look and delegate to the right persons that have insight into DevPortal?



Regards,



  Stefan



From: Pichel, Stefan
Sent: Montag, 20. Juli 2026 13:22
To: Guymer, Scott <Scott.Guymer@philips.com>
Cc: Terol, David <david.terol@philips.com>; Jha, Eeshani (Partner) <partner.Eeshani.Jha@philips.com>
Subject: Access to DevPortal broken



Hello Scott,



may I ask you to have a look on a case that I am not able to solve.



A user (Eeshani Jha) is complaining not being able to access the Developer Portal.





[cid:image001.png@01DD184A.B17A6D20]



I can see that the eror comes from a lookup mismatch:



{"error":{"name":"ConflictError","message":"User lookup resulted in multiple matches"},"request":{"method":"GET","url":"/awsalb/refresh"},"response":{"statusCode":409}}





That I can explain: The user has two GitHub account linked to the same email address.



[cid:image002.png@01DD184A.B17A6D20]



[cid:image003.png@01DD184A.B17A6D20]



Both were member of GitHub philips-internal, but one eeashani-11 is removed – the error keeps the same even after a waiting time of one hour and calling the DevPortal in incognito mode to be sure no caching is active.



Do you have any idea?



Regards,



  Stefan





________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.

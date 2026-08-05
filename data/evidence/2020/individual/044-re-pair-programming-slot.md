# Evidence: RE: Pair programming slot 

## Source
- **File:** `RE  Pair programming slot .msg`
- **Date:** 2020-02-18
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** Vellal, Dattatreya
- **To:** M N, Ganesh <ganesh.mn@philips.com>; Gangadharan, Nikila <nikila.gangadharan@philips.com>; D, Naveen <naveen.d@philips.com>
- **CC:** Jagadeesan, Sundaresan <sundaresan.j@philips.com>; R U, Rashmi <rashmi.mallikarjuna@philips.com>
- **Date:** 2020-02-18T02:50:02.334875-05:00
- **Thread depth:** 5
- **Is reply:** True

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Author

## Key Quotes
> From: Vellal, Dattatreya

> Thank you very much for the minutes.

> Rashmi, Sundar - the first of the pair-programming session was great, with a lot of learnings that can be incorporated.

> To: Gangadharan, Nikila <nikila.gangadharan@philips.com>; D, Naveen <naveen.d@philips.com>; Vellal, Dattatreya <dsvellal@philips.com>

> Thanks for you valuable time.

## Full Email Content

```
Subject: RE: Pair programming slot 
From: Vellal, Dattatreya
To: M N, Ganesh <ganesh.mn@philips.com>; Gangadharan, Nikila <nikila.gangadharan@philips.com>; D, Naveen <naveen.d@philips.com>
CC: Jagadeesan, Sundaresan <sundaresan.j@philips.com>; R U, Rashmi <rashmi.mallikarjuna@philips.com>
Date: 2020-02-18T02:50:02.334875-05:00

--- Latest Reply ---
Thank you very much for the minutes. 

This is what I have posted in the channel: 
Today, I pair-programmed with M N, Ganesh and @naveen.d. Lot of good learnings today. Positive ones: We were able to reduce ~20 lines of code in ScheduleWorkflow class by extracting out a common method to validate string, and also reduce memory footprint by creating a static variable of a deviceId fetched from the configuration. Also attempted to improve the readability of codebase by eliminating statement ppsObjectList.First() and encapsulating it into a method getCapturedImage(ppsObjectList). This will ensure that specific logic of how to fetch the captured image is pushed into the method, and the reader doesn't have to know about how it is done until necessary. Also it will ensure that if a change has to be made, it can be made in one place, and everywhere else, we get the change for free (unlike now, where we would have had to chagne ppsObjectList.<fetch>() everywhere the image is used!). Also noticed a generic exception being caught at SetPerformedProcedureCodeInternal() and thought of how to change it to more specific DICOM exception. Also I have to appreciate, a good practice, which is constructing the log message before logging it. Thank you for this!

Rashmi, Sundar - the first of the pair-programming session was great, with a lot of learnings that can be incorporated.

--- Previous Message (1) ---
Datta

--- Previous Message (2) ---
Sent: Tuesday, February 18, 2020 1:10 PM
To: Gangadharan, Nikila <nikila.gangadharan@philips.com>; D, Naveen <naveen.d@philips.com>; Vellal, Dattatreya <dsvellal@philips.com>
Subject: RE: Pair programming slot 


Hi Datta,

Thanks for you valuable time.

Please find the MOM for the session

1. creating a static instance of deviceId
2. encapsulating ppsObjectList.First() into a method call so that: a) readability improves, and b) abstraction helps handle changes better
3. Instead of pulling ppsObjectList.First() everything to be used, try creating a method level variable for minor improvement in performance
4. May be consider pulling out string validation into a separate method, thereby achieving ~19 reduction & improved readability: ScheduleWorkflow class. Extension to this is, if another class, has a similar pattern, please consider moving this to a utility class.
5. SetPerformedProcedureCodeInternal() in this method, please see if generic exception catch can be avoided, in favor of catching specific exceptions

Appreciate that the log messages created before logging or throwing an exception is a very good practice. This will ensure that computation doesn't happen while logging, thereby allowing us to execute the "next-line" fast! Thank you for this practice!	

Regards,
Ganesh M N

--- Previous Message (3) ---
Original Appointment-----

--- Previous Message (4) ---
Sent: 2020 Feb 18 9:18 AM
To: M N, Ganesh; D, Naveen; Vellal, Dattatreya
Subject: Pair programming slot 
When: 2020 Feb 18 12:00 PM-1:00 PM (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi.
Where: @Naveen's desk, opp 2B 4 08


Naveen – please ensure Datta is able to reach your location correctly :)

Regards,
Nikila



  ________________________________  
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.
```
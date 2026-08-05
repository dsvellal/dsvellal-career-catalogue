# Evidence: RE: Issue with JSCPD

## Source
- **File:** `RE  Issue with JSCPD.msg`
- **Date:** 2020-01-30
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** Code Duplication / JSCPD

## Email Metadata
- **From:** "Adagal, Nanda" <nanda.adagal@philips.com>
- **To:** "M.C; Venkatesh" <Venkatesh.MC@philips.com>; "Vellal; Dattatreya"	<dsvellal@philips.com>; "Hu; Aravind" <Aravind.Hu@philips.com>
- **CC:** "TK; Vivek" <vivek.tk@philips.com>; "Farook; Mohammad Fayaz"	<mohammad.fayaz@philips.com>; "Naga; Subhash" <subhash.naga@philips.com>;	"Sreenath; Revathy" <Revathy.duddisreenath@philips.com>; "P V; Vineeth"	<vineeth.p.v@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>; "R U; Rashmi" <rashmi.mallikarjuna@philips.com>
- **Date:** 2020-01-30T02:21:28-05:00
- **Thread depth:** 7
- **Is reply:** True
- **Attachments:** 3
  - `image001.jpg` (image/jpeg, 27126 bytes)
  - `image004.jpg` (image/jpeg, 8018 bytes)
  - `image005.jpg` (image/jpeg, 17125 bytes)

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "M.C; Venkatesh" <Venkatesh.MC@philips.com>; "Vellal; Dattatreya"	<dsvellal@philips.com>; "Hu; Aravind" <Aravind.Hu@philips.com>

> Hi Datta/Aravind,

> Thank you for your support in resolving the issue.

> I had discussion with Datta/Aravind and the issue got resolved.

> Thanks and regards,

## Full Email Content

```
Subject: RE: Issue with JSCPD
From: "Adagal, Nanda" <nanda.adagal@philips.com>
To: "M.C; Venkatesh" <Venkatesh.MC@philips.com>; "Vellal; Dattatreya"	<dsvellal@philips.com>; "Hu; Aravind" <Aravind.Hu@philips.com>
CC: "TK; Vivek" <vivek.tk@philips.com>; "Farook; Mohammad Fayaz"	<mohammad.fayaz@philips.com>; "Naga; Subhash" <subhash.naga@philips.com>;	"Sreenath; Revathy" <Revathy.duddisreenath@philips.com>; "P V; Vineeth"	<vineeth.p.v@philips.com>; "Jagadeesan; Sundaresan"	<sundaresan.j@philips.com>; "R U; Rashmi" <rashmi.mallikarjuna@philips.com>
Date: 2020-01-30T02:21:28-05:00

--- Latest Reply ---
Hi Datta/Aravind,

Thank you for your support in resolving the issue.

 

@ Venkatesh,

I had discussion with Datta/Aravind and the issue got resolved.

 

Details of fix:

By default JSCPD has Maximum file size (threshold) as 30KB, any file which is bigger than 30KB will be skipped from analysis.

The file being skipped in our case i.e. R4ModelInfo.cs was of size 35 KB.

 



 

To resolve the issue we can pass additional parameter –z  <New Max File Size> while running JSCPD. It will overwrite the default value 30kb.

 

e.g. 

jscpd  . --min-tokens 50 --reporters "html,verbose,console,json" --ouput "." --mode "strict" --ignoreCase true "" --ignore "obj,jscpd-*.*,References" -z 1000mb

 

Output post applying the change: 



 

Note:

The duplicate lines identified by TICS is only 4 whereas it is 22 by JSCPD it is may be due to the minimum number tokens considered by JSCPD i.e. 50.

--- Previous Message (1) ---
Thanks and regards,

Nanda

--- Previous Message (2) ---
Sent: Wednesday, January 29, 2020 3:43 PM
To: Adagal, Nanda <nanda.adagal@philips.com>; Hu, Aravind <Aravind.Hu@philips.com>
Cc: M.C, Venkatesh <Venkatesh.MC@philips.com>; TK, Vivek <vivek.tk@philips.com>; Farook, Mohammad Fayaz <mohammad.fayaz@philips.com>; Naga, Subhash <subhash.naga@philips.com>; Sreenath, Revathy <Revathy.duddisreenath@philips.com>; P V, Vineeth <vineeth.p.v@philips.com>; Jagadeesan, Sundaresan <sundaresan.j@philips.com>; R U, Rashmi <rashmi.mallikarjuna@philips.com>
Subject: RE: Issue with JSCPD

 

Hi Nanda, 

Thank you for reporting this interesting behavior. 

 

There are a couple of observations that I would like to make: 

1.      The way --ignore option is used here. What’s the intention? To avoid “folders” or “files” or both? (JSCPD documentation reference: https://www.npmjs.com/package/jscpd#ignore <https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjscpd%23ignore&data=02%7C01%7C%7C047b90db04084d391f0708d7a555061c%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C637159656895126114&sdata=LR5TVLfOZ3WU8guk%2BJVbx28U7TIjWnKQlFTggLGcMfM%3D&reserved=0> )

2.      2 seconds to run on a single file with 316 lines is a bit suspicious. 

 

Can we get into a quick call, I can also be a bit helpful here in identifying what the anomaly is and help.

--- Previous Message (3) ---
Datta

--- Previous Message (4) ---
Sent: Wednesday, January 29, 2020 3:23 PM
To: Hu, Aravind <Aravind.Hu@philips.com <mailto:Aravind.Hu@philips.com> >
Cc: Vellal, Dattatreya <dsvellal@philips.com <mailto:dsvellal@philips.com> >; M.C, Venkatesh <Venkatesh.MC@philips.com <mailto:Venkatesh.MC@philips.com> >; TK, Vivek <vivek.tk@philips.com <mailto:vivek.tk@philips.com> >; Farook, Mohammad Fayaz <mohammad.fayaz@philips.com <mailto:mohammad.fayaz@philips.com> >; Naga, Subhash <subhash.naga@philips.com <mailto:subhash.naga@philips.com> >; Sreenath, Revathy <Revathy.duddisreenath@philips.com <mailto:Revathy.duddisreenath@philips.com> >; P V, Vineeth <vineeth.p.v@philips.com <mailto:vineeth.p.v@philips.com> >
Subject: Issue with JSCPD

 

Hi Aravind,

 

We ran JSCPD on our (FDM) source code and observed a strange issue. Please see details below:

 

Issue:

There is a folder with only 2 C# files and these files have 4 lines of duplicate code.

-       Hl7.Fhir.Spec/R4ModelInfo.cs - Line 280-283

-       Hl7.Fhir.Spec/STU3ModelInfo.cs - Line 234-237

 

JSCPD is not recognizing this duplication, but TICS works . 

After investigation we found that JSCPD is not identifying existence of 1 of the file i.e. R4ModelInfo.cs. 

It is listing/analyzing only 1 file and therefore not able to find duplication.

 

Output we received:



 

We tried renaming file but still same issue. We tried copying few more C# files to this folder, then also JSCPD runs on all files except the R4ModelInfo.cs.

 

Please support us to resolve this issue.

Let us know if any more information is required.

--- Previous Message (5) ---
Thanks and regards,

Nanda

--- Previous Message (6) ---
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination,

[... truncated, full content in database ...]
```
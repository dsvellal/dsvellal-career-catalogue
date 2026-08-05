# Evidence: [FYI & Immediate Action] CCB - Defect life-cycle, fields & Owners

## Source
- **File:** `_FYI & Immediate Action  CCB - Defect life-cycle  fields & Owners.msg`
- **Date:** 2019-01-31
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "Vellal, Dattatreya" <dsvellal@philips.com>
- **To:** dl_BlrPH_HITCoE_IDM <dl_BlrPH_HITCoE_IDM@philips.com>
- **CC:** "Krishnaraj; Hamsa" <Hamsa.Krishnaraj@philips.com>; "Kn; Pradeep"	<pradeep.kn@philips.com>; "Mohan; Murali" <murali.mohan@philips.com>;	"Chourey; Pooja" <Pooja.Chourey@philips.com>; "Singh; Jayaraj"	<jayaraj.singh@philips.com>; "VellourHouse Subramani; Manikandan"	<manikandan.subramani@philips.com>; "K R; VasanthaKumar"	<VasanthaKumar.KR@philips.com>; "Kulkarni; Vasanth Kumar"	<vasanthkumar.kulkarni@philips.com>
- **Date:** 2019-01-31T06:06:26-05:00
- **Thread depth:** 2
- **Is reply:** False

## Datta's Involvement
- **Role at time:** Project Architect, IDM
- **Involvement type:** Author

## Key Quotes
> From: "Vellal, Dattatreya" <dsvellal@philips.com>

> 1.  Every defect will be vetted weekly by the CCB board (Vasanth Kulkarni – lead, Datta, Jayaraj, Vasanth, Pooja, Murali, Hamsa)

## Full Email Content

```
Subject: [FYI & Immediate Action] CCB - Defect life-cycle, fields & Owners
From: "Vellal, Dattatreya" <dsvellal@philips.com>
To: dl_BlrPH_HITCoE_IDM <dl_BlrPH_HITCoE_IDM@philips.com>
CC: "Krishnaraj; Hamsa" <Hamsa.Krishnaraj@philips.com>; "Kn; Pradeep"	<pradeep.kn@philips.com>; "Mohan; Murali" <murali.mohan@philips.com>;	"Chourey; Pooja" <Pooja.Chourey@philips.com>; "Singh; Jayaraj"	<jayaraj.singh@philips.com>; "VellourHouse Subramani; Manikandan"	<manikandan.subramani@philips.com>; "K R; VasanthaKumar"	<VasanthaKumar.KR@philips.com>; "Kulkarni; Vasanth Kumar"	<vasanthkumar.kulkarni@philips.com>
Date: 2019-01-31T06:06:26-05:00

--- Latest Reply ---
Team,
In the effort of ensuring that our defects & their life-cycle can be logically tracked, we are have come up with the following process of tracking defects in TFS:

  1.  Every defect will be vetted weekly by the CCB board (Vasanth Kulkarni – lead, Datta, Jayaraj, Vasanth, Pooja, Murali, Hamsa)
  2.  Every defect will be tracked via the following state: New -> Accepted -> Planned -> Resolved -> Verified -> Removed -> Reopened (TBD)
  3.  Every defect state will have an owner who’ll validate the content of the defect & ensure that the content present is conforming to the details that we want. (Refer the below table to see, at what state of the defect, who is the owner & what fields are mandatory in TFS when the defect is put in that state)

Starting from 19PI1, we are going to follow this process stringently. This will help us in ensuring that we are raising quality defects & are resolving them correctly, by addressing the right root-cause, while having enough data to generate required report for further dive-deep & analysis.

I look forward to each of us following through this process.

STATE
NEW
ACCEPTED
PLANNED
RESOLVED
VERIFIED
REMOVED
OWNER
Tester
Architect
PO
Developer
Tester
Architect,
SM
1
Title
Y
3
Steps to reproduce
Y
4
Description
Y
5
Impact Analysis
Y
6
System Info
 * CE Version
* Dependent Product Version
  * Env info (IP Adress, Node type, OS Version, IDM env details)
Y
7
Acceptance Criteria (What is the expected behaviour)
Y
Y
Y
8
Resolution (How the issue was fixed, PR ID link with validation proof)
Y
9
Status - How found:
* use one of the 4 values -
1. Found in Field
2. Regression Testing,
3. User Story Testing (i.e, Scrum Testing)
4. Internal Validation (Pre-Prod/Staging testing)
Y
10
Details - Size
Y
11
Details - Reference ID : use CQ/TFS/OneEMS
Y
12
Classification - Classification
1. Enhancement
2. Engineering Issue (if issue with IDM)
3. Product Defect (if issue with Product like ISPACS, UDM etc)
Y
Y
13
Classification - Rank
* used for prioritization so that it can be taken up for upcoming sprint
Y
Y
14
Classification - Severity
Y
Y
15
Classification - Reproduceability
Y
16
Classification - Component
Y
Y
17
Risk Aspects - Security
Y
18
Found in - Product (Ex: ISPACS, I4, ISEE etc)
Y
19
Found in - Project / Release (Default to IDM always)
Y
20
Found in - Version (IDM Release version Ex: 1.10.0.0)
Y
21
Found in - Found in Build (IDM Build version Ex: 1.10.0.65)
Y
22
Planned - Fixed Planned Version (Ex: upcoming IDM release version 1.11.0.0)
Y
23
Fixed in - Fixed in Version
Y
24
Fixed in - Integration Build
Y
25
Others - Generic02 - Doc update (YES or NO)
26
Others - Generic03 - Doc Location




Regards,
Datta

--- Previous Message (1) ---
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.
```
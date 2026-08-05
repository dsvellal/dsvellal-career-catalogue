# Evidence: RE: IDM for Image Capture

## Source
- **File:** `RE  IDM for Image Capture.msg`
- **Date:** 2019-02-28
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "Nolte, Kirk" <Kirk.Nolte@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>
- **Date:** 2019-02-28T12:52:00-05:00
- **Thread depth:** 5
- **Is reply:** True

## Datta's Involvement
- **Role at time:** Project Architect, IDM
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>

> Datta… Thanks for turning this around so fast, much appreciated. Enjoy your PTO tomorrow and thanks again – Kirk.

> Thank you for your time. Here’s our MoM:

> 1.       Datta to provide steps required for package registration-distribution-deployment, with IDM.

> 2.       Datta to get in touch with PCM to confirm if it supports package copy from Neb node to other linux nodes.

## Full Email Content

```
Subject: RE: IDM for Image Capture
From: "Nolte, Kirk" <Kirk.Nolte@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>
Date: 2019-02-28T12:52:00-05:00

--- Latest Reply ---
Datta… Thanks for turning this around so fast, much appreciated. Enjoy your PTO tomorrow and thanks again – Kirk.

--- Previous Message (1) ---
Sent: Thursday, February 28, 2019 9:44 AM
To: Miller, Michael <Mike.Miller@philips.com>; Mohan, Murali <murali.mohan@philips.com>; Mccready, Sean <sean.mccready@philips.com>; Nolte, Kirk <Kirk.Nolte@philips.com>; Villanueva, Victor <victor.villanueva@philips.com>; Dekkers, Jeroen <j.dekkers@philips.com>; Mendenhall, Rebecca <rebecca.mendenhall@philips.com>; K R, VasanthaKumar <VasanthaKumar.KR@philips.com>; Singh, Jayaraj <jayaraj.singh@philips.com>
Subject: RE: IDM for Image Capture

Team,
Thank you for your time. Here’s our MoM:

1.       Datta to provide steps required for package registration-distribution-deployment, with IDM.

2.       Datta to get in touch with PCM to confirm if it supports package copy from Neb node to other linux nodes.

3.       Image capture team: To close loop with the security team about:

a.       In what form will the package be distributed? Options discussed were: Zip, RPMs or any other linux supported binaries.

b.      Third-party-package distribution – wrt security scans. Suggestion: To consider scans including: Penetration testing, Fortify Scan, Nessus Scan, Blackduck scan

c.       After using IDM as a vehicle to transfer the required linux package to the Neb node – the suggested mechanism of deployment was to leverage third-party team to access the package & deploy it on the node, while they are being moderated by Philip’s support team. This process has to be vetted by the Security team.

4.       Identify an environment (Hospital site) where a sample package transfer via IDM can be initiated & tested.


Below are the steps required via IDM to perform package registration-distribution-deployment:

  1.  Software package registration process in IDM
     *   R&D / BU sends final version of Software application package (zip) to BU’s DevOps team
     *   BU DevOps packages it by adding SiteInfo.xml and creates package for IDM registration
     *   IDM team uploads the package to IDM Repo for registration (Download package from BU windows folder --> Stentor --> Repo)
     *   IDM OPS team performs checksum of the package uploaded and capture report (compare value in XML with value of checksum on package)
     *   IDM OPS team creates 2 additional files (for product package zip and xml) to support ZSYNC and copies to IDM Repo
     *   IDM Ops team creates xml file in SVN with package name for distribution only – this xml file will have package path, package zip name and package xml name.
     *   IDM Ops team creates an entry in mongo DB for the package with default countries (US and Canada) enabled and multi-site enabled. This has to done for every new package deployment request.
     *   IDM Ops team verifies package registration using SWD page & Geo Rules.
     *   Respective product manager logs into geo-rules page and sets the geo-rules according to NOR-D configuration.
  2.  Software distribution (primary user: SCS Upgrades team)
     *   SCS upgrade team shares weekly plan and is responsible for distributing software to the intended sites in preparation towards the planned upgrade
     *   SCS team submits the package for distribution via IDM Portal.
     *   After distribution request submitted, packages are copied on the NEB node.
     *   SCS team verifies the copy by visiting the IDM Portal page.
  3.  Software deployment (primary user: SCS Upgrades team)
     *   If the Deployment is for TEST Nodes, IDM Ops team adds / configures test node to support deployment (This is a onetime activity for every site)
     *   SCS team selects the package for SW deployment via IDM Portal
     *   After Deployment request is submitted it is expected for the deployment instructions to be coped on the NEB node.
     *   SCS Upgrades team will manually trigger deployment task from Thruk view.
     *   PCM takes over from here and deploys the package on the target nodes.
     *   PCM sends the deployment status to IDM portal.

--- Previous Message (2) ---
Datta

--- Previous Message (3) ---
Original Appointment-----

--- Previous Message (4) ---
Sent: Wednesday, February 27, 2019 6:16 PM
To: Miller, Michael; Mohan, Murali; Mccready, Sean; Nolte, Kirk; Villanueva, Victor; Dekkers, Jeroen; Mendenhall, Rebecca; K R, VasanthaKumar; Vellal, Dattatreya; Singh, Jayaraj
Subject: IDM for Image Capture
When: Thursday, February 28, 2019 9:00 AM-9:30 AM (UTC-06:00) Central Time (US & Canada).
Where: Skype Meeting

Image Capture is the product that will be replacing Visible Light.  If I understand Image Capture correctly, they will be deploying their own VM on our PACS platform.  We would like to understand how the SW would g

[... truncated, full content in database ...]
```
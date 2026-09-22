# Re: XITE V&V Compliance: Golden Thread Traceability - Release Notes

**From:** "Terol, David" <david.terol@philips.com>  
**To:** "Subramanya Vellal, Dattatreya" <dsvellal@philips.com>, "Ramachandra, Naveen" <Naveen.Ramachandra@philips.com>, "P, Dilip Kumar" <DilipKumar.P@philips.com>, "Hegde, Madhura" <madhura.hegde@philips.com>, "Banerjee, Amar Satyabroto" <AmarSatyabroto.Banerjee@philips.com>, "Akkottillam, Praveen" <Praveen.Akkottillam@philips.com>, "Stern, Stav" <stav.stern@philips.com>, "Nadav, Judith" <judith.nadav@philips.com>, "Yaskin, Hellen" <hellen.yaskin@philips.com>, "Weiss, Amit" <amit.weiss@philips.com>, "Eliav, Liran" <Liran.Eliav@philips.com>, "Shivashankar, Srivatsa Manu" <Manu.Srivatsa.Shivashankar@philips.com>, "Upadhyay, Hemant" <hemant.upadhyay@philips.com>, "A, Balamurugan" <Balamurugan.A@philips.com>, "Jadhav, Vikrant" <vikrant.jadhav@philips.com>, "Sheiman, Ella" <ella.sheiman@philips.com>, "Aizik, Elena" <elena.aizik@philips.com>, "KC, Jayalakshmi" <jayalakshmi.kc@philips.com>, "Mitra, Miteshkumar" <miteshkumar.mitra@philips.com>  
**Date:** Tue, 27 Jan 2026 15:28:24 +0000  

---

Thanks Datta for the detailed update on this first use case.

I know it's taken significant hard good work to get here in so short time. Good to see we enabled the three BUs and we're also taking steps on how to scale and offer this on sustainable way through the Portal integration. Great progress again.

I hope this enables our BUs to provide good feedback on this direction.

Thanks again and kudos to the team.
David.


________________________________
From: Subramanya Vellal, Dattatreya <dsvellal@philips.com>
Sent: Tuesday, January 27, 2026 7:21 AM
To: Ramachandra, Naveen <Naveen.Ramachandra@philips.com>; P, Dilip Kumar <DilipKumar.P@philips.com>; Hegde, Madhura <madhura.hegde@philips.com>; Banerjee, Amar Satyabroto <AmarSatyabroto.Banerjee@philips.com>; Akkottillam, Praveen <Praveen.Akkottillam@philips.com>; Stern, Stav <stav.stern@philips.com>; Nadav, Judith <judith.nadav@philips.com>; Yaskin, Hellen <hellen.yaskin@philips.com>; Weiss, Amit <amit.weiss@philips.com>; Eliav, Liran <Liran.Eliav@philips.com>; Shivashankar, Srivatsa Manu <Manu.Srivatsa.Shivashankar@philips.com>; Upadhyay, Hemant <hemant.upadhyay@philips.com>; A, Balamurugan <Balamurugan.A@philips.com>; Jadhav, Vikrant <vikrant.jadhav@philips.com>; Sheiman, Ella <ella.sheiman@philips.com>; Aizik, Elena <elena.aizik@philips.com>; KC, Jayalakshmi <jayalakshmi.kc@philips.com>; Mitra, Miteshkumar <miteshkumar.mitra@philips.com>
Cc: Jagadeesan, Sundaresan <sundaresan.j@philips.com>; Kuppusamy, Prasad <Prasad.Kuppusamy@philips.com>; Adebiyi, Omonigho <omo.adebiyi@philips.com>; Kumar, Nataraj <nataraj.kumar@philips.com>; Terol, David <david.terol@philips.com>; Guymer, Scott <Scott.Guymer@philips.com>; Burgers, Stefan <stefan.burgers@philips.com>; Oborzynska, Agnieszka <agnieszka.oborzynska@philips.com>; Padmanabhan, Sivaraman <sivaraman.padmanabhan@philips.com>
Subject: XITE V&V Compliance: Golden Thread Traceability - Release Notes

Dear stakeholders,
We are writing this email to keep you posted on our first XITE project deliverable - Golden Thread Traceability (GTT) use-case. As promised, this is the first use-case that establishes relationship between data ingested from your release documents, and provides a visualization for you to look around and explore.

We have ingested release documents from IGT-MoS, SRC and AV&I teams, and we appreciate the co-operation extended by your team in helping us understand the flow of documents, make available missing documents, and complete the process of data ingestion. To everyone's credit, we have received feedback from business that this use-case already found value in this process of ingestion where potential gaps were identified, and are being addressed. This uplifts our efforts and brings wings to our teams to deliver this use-case and more to delight our lead customers.

The Graph model depicting the GTT use-case, deployed on AWS, with business data is here: https://aws-neptune-avi-notebook.notebook.us-east-1.sagemaker.aws/proxy/9250/explorer/#/graph-explorer<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Faws-neptune-avi-notebook.notebook.us-east-1.sagemaker.aws%2Fproxy%2F9250%2Fexplorer%2F%23%2Fgraph-explorer&data=05%7C02%7Cdsvellal%40philips.com%7C2f95f3b375ab4a1c7fd908de5db8b60c%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639051245061579144%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=QG4gqhtPyrHbOpLHDqG1E8oIaGOXDD6heW%2FeseSnVbk%3D&reserved=0>

  *
AV&I: Refer attachment: 20260127-AV&I-Neptune-Graph-DB-Snapshot.png, which has 3927 nodes and 8800 edges
  *
IGT-MoS: Refer attachment: 20260127-IGT-MoS-Neptune-Graph-DB-Snapshot.png, which has 4150 Nodes and 3150 edges.
  *
SRC: Refer attachment: 20260127-SRC-Neptune-Graph-DB-Snapshot.png, which has 1420 nodes and 2360 edges.

These were demonstrated to you during the working sessions with you.

As requested by you in the workshop, we are in the final process of making the data available to you, on a portal that does not require GitHub specific credentials, meaning anyone in the organization can access this data, and we intend to make it available on the developer portal here: https://portal.internal.philips<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fportal.internal.philips%2F&data=05%7C02%7Cdsvellal%40philips.com%7C2f95f3b375ab4a1c7fd908de5db8b60c%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639051245061603704%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=K1sAdBWpeVBsGVtw5s8NY%2ByFWUay7SB1zvPDZaDx1ic%3D&reserved=0>. As a giant leap into making this available on the developer portal, we have it up and running on the staging instance of developer portal here: https://portal-staging.internal.philips/sutra<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fportal-staging.internal.philips%2Fsutra&data=05%7C02%7Cdsvellal%40philips.com%7C2f95f3b375ab4a1c7fd908de5db8b60c%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639051245061618582%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=1VbEuI1jO8yTdD3RUlsu7UcA1lHQjxXWlshsm69gBKA%3D&reserved=0>
We are working towards making live data pulled from Golden Thread Traceability, visible via the developer portal by end of this week.

As next steps, here's what you can expect:

  1.
Over the next few weeks, we will continue to collaborate with you to help you explore GTT use-case on your ingested documents via developer portal. Look forward to our invites, and please bring along anyone from your business who is interested in understanding and interpreting the data ingested, and visualizing it via GTT use-case.
  2.
We will call for a workshop again with you to discuss the usability and next features being made available. This will also be a demonstration workshop.
  3.
Look out for our "Impact Analysis" use-case coming on the same platform, as requested by you, in February. Here's a quick 20 minute video on proof of concept done on AV&I data:
[https://res-2.df.onecdn.static.microsoft/files/fabric-cdn-prod_20251010.003/assets/item-types/16/video.svg]20260122-Test-Impact-Analysis-Directional-Thinking-PoC.mp4<https://share.philips.com/:v:/s/SWCoECompetencies/IQAI3rY7ccGjQIXyEcd62MwvAfjcVjqOw04XTdRPUQn56ZY?e=KovpBa>

We look forward to providing value to you through this XITE journey!


-- Datta

Software Competency Lead

Innovation Engineering, Innovation & Design


________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.

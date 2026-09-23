# 201606 Feedback From SDT On Using XML Migration SOP

> Converted from document `201606_Feedback_From_SDT_On_Using_XML_Migration_SOP.pdf`

Friday, July 15, 2016 at 8:34:09 PM India Standard Time

Subject: Feed Back on XML_NEW parser migra8on for
Date: Thursday, June 23, 2016 at 12:17:42 PM India Standard Time
From: Gopalan, Ramachandran
To:
Vellal, DaQatreya, PoliseQy, Hari
CC:
Sankaran, Thiruvenkatakrishnan, Mani, Gajendran, grcs-feeds-chennai@amazon.com
Hi DaQa/Hari,
Just sharing my experience on my ﬁrst XML_NEW parser migra8on for GPIV feed standard and the breakup of 8melines on the steps it took to complete the migra8on.
1)

The wiki contains most of the steps on clear cut to complete the migra8on of a standard from old
XML to NEW parser and that helped elimina8ng the Dev hand hold on migra8on.
2) Thanks DaQa for helping in se_ng the RetailCatalogDocumentStoreService locally and adding the
step to wiki clearly & ge_ng the Odin permissions to complete the migra8on on 8meline
3) The steps for changing the madeira ion conﬁgura8ons according to new parser is also easy. May be
it varies based on diﬀerent madeira conﬁgura8on with diﬀerent copyFields & aspect paths
Some things to add in wiki that might be useful are:
1) The number of items or % of items that we need to submit for comparison to get full conﬁdence
score
2) To check on the beta and prod by sample ﬁle submission aeer conﬁgura8on check-in to make sure
that conﬁgura8ons propagated through both Streaming & Doc-store service pipeline as non-sync of
them might cause madeira submission failures [Quality assurance checks/ Matching
failures/normaliza8on errors]
Timelines of the steps on high level for eﬀort spent [No cycle 8me included] for single itera8on for each of
the step for GPIV [containing only 3 sub-vendors] .The 8me varies for other vendors based on no. of sub
vendors:
S.no

MigraKon steps

Eﬀort spent

1 Se_ng up madeira/docstore & necessary environments locally

4 hr

2 Iden8fying & Submi_ng sample feed ﬁles for each vendor through old parser

0.5 hr

3 Ge_ng old Normaliza8on record through the script
Changing the madeira conﬁgura8on and tes8ng for one feed to verify whether the
4 paths [ copyFields & aspect paths ]are working ﬁne
5 Submi_ng sample feed ﬁles for each vendor through New parser
6 Ge_ng New Normaliza8on record through the script
7 Comparison of old and new normaliza8on records
8 Par8al normaliza8on pre-check in tes8ng for tes8ng through mixed aspects

0.5 hr
0.5 hr
0.5 hr
0.5 hr
0.5 hr
3 hrs

Total: 10 hrs eﬀort 8me on ﬁrst 8me migra8on if no issue occurs in the middle.
I am working on the caﬀeine implementa8on of GPIV. I will let you know the feedback on how new XML
document helps in eﬀec8ve fetching of data/reduc8ons in coding wise.
Thanks,
Page 1 of 2

Ram

Page 2 of 2


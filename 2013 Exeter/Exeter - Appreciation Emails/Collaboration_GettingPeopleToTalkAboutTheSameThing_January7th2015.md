# Collaboration GettingPeopleToTalkAboutTheSameThing January7th2015

> Converted from document `Collaboration_GettingPeopleToTalkAboutTheSameThing_January7th2015.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Dattatreya Subramanya Vellal
Wednesday, January 07, 2015 6:28 PM
Jonah Egenolf; Anuroop V. Gaonkar
RE: OPA Data Mapping

We discussed the following things.. (image below)
Block 1: Talks about the BIG picture. Where we do the intake, do the determination and persist the results back to
Siebel. The key point to note is persist is through DL, and determination is also through DL. They need not be tied
together, and they need not be sequential. It’s a promise from DL that when it has the right data, it will persist things
back, so from an application perspective, as long as data exists in DL, we are good.
Block 2: This expands the “Determination and Persist” block from block 1, and talks a bit more about how it is
structured. The data-layer which has the context, calls a biz.layer.method (let’s call it DetermineEligibility()) and then
the results are absorbed into DL, and DL decides to persist values back to Siebel (which is why the persist is in
parenthesis)
Block 3: This expands block 2’s biz.layer.method and defines what all the biz.layer method should do. This includes:
1. Getting the in-memory DL model for the context (mcn-based)
2. Get the in-memory-OPA-data-model corresponding to this (obtained by navigating through mcn?)
3. Constructing the Req.object to be passed while doing the eligibility-determination invocation, using the
model from 2
4. Parsing the Resp.object back into model from 2
5. Obtaining/Updating the model from 1, via model from 2
6. Persisting values into Siebel.
Block 4: This is another representation of block 3, indicating the work involved in doing the eligibility-determination
piece, that includes mapping and biz.layer.method writes from our end.
Block 5: This is mostly the transformation indication.

1

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
2

From: Jonah Egenolf
Sent: Wednesday, January 07, 2015 9:22 AM
To: Anuroop V. Gaonkar
Cc: Dattatreya Subramanya Vellal
Subject: Re: OPA Data Mapping

So I didn't get a chance to respond here, but I walked through a similar thing today with Datta today and I
think it might be best if you guys work through it together in person. Can you two walk through the
OPA/DL interaction and see where that leads?
- Jonah
From: Anuroop V. Gaonkar
Sent: Tuesday, January 06, 2015 8:20 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal
Cc: Robert Parks; Sajith Sanal; Vinay Shivanna
Subject: RE: OPA Data Mapping
Hello All,
Other key item that I & Srikanth figured out that all may not be equally aware of the “basic” challenge:
1.
2.

Taking the data from Siebel & Moving that to OPA – we are in the process of solving this.
Next comes the challenge of pushing the data coming from OPA in to Siebel via data layer (for example: a. in
application driven by OPA or b. data returned by OPA after eligibility). Here the DL should be able to take
the data & build the OPA as well as DL trees because these trees need to be built based on the mapping
specified.

Challenge 2 is not solved yet. The solutions are
1.

The OPA module that Srikanth and I have built provides interfaces to traverse the OPA tree – this interface is
called by DL to build the OPA and DL tree in DL
a. Get root node
b. Get Entities
c. Get Attributes associated with entities
d. Repeat b & c recursively
e. Traverse OPA tree recursively & get relationships
We have already built this part to process results that we receive from OPA, but these interfaces need to be
used by DL

2.

Entire OPA tree is handed over to DL & DL builds the tree

I prefer option 1.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Tuesday, January 06, 2015 4:51 PM
To: Srikanth Ayanur Harirao; Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal
Cc: Robert Parks; Sajith Sanal; Vinay Shivanna
Subject: RE: OPA Data Mapping
3

Hi Jonah & Rob,
Hope you had good vacation. Srikanth, Aditya, Datta, Vinay and team have been completing on getting the mappings
working.
Srikanth and I want to complete testing the tree traversal and OPA request creation logic. Hence we would be
grateful for any assistance to move forward with that task.
We will start work on the Biz Layer piece to
a. Define interface to make eligibility determination call & expose that as web service – This should be called
by Siebel for eligibility determination
b. Implement the post processing logic in Biz Layer to archive the BLI post successful completion of eligibility
determination & before updating the new eligibility determination info.
Please let us know if you have some different thoughts / guidance.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Srikanth Ayanur Harirao
Sent: Thursday, January 01, 2015 7:19 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Robert Parks; Sajith Sanal; Vinay Shivanna
Subject: RE: OPA Data Mapping

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a.

How many OPA line items in total need to be mapped for OPA eligibility determination + application – 705
(Post-Cleanup activities)
b. How many of these have been mapped to OG Model – 447
c. How many of these mapped to OG model have been mapped to Siebel – 270
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 270
Apart from these, the OPA mapping sheet has been updated with a few changes,
Re-Introduced the Entity Implementation column to track Entity and Implementation separately
Introduced a new sheet “To Do” to keep track of design changes needed in the “Data Layer – Siebel”
mapping sheet
Please view the “To Do” sheet in the document which lists the blockers for us in mapping certain attributes.
Let me know in case of any questions.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah

4

From: Srikanth Ayanur Harirao
Sent: Wednesday, December 31, 2014 6:26 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Robert Parks; Sajith Sanal; Vinay Shivanna
Subject: RE: OPA Data Mapping

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a.

How many OPA line items in total need to be mapped for OPA eligibility determination + application – 705
(Post-Cleanup activities)
b. How many of these have been mapped to OG Model – 447
c. How many of these mapped to OG model have been mapped to Siebel – 265
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 265
Apart from these, the OPA mapping sheet has been updated with a few changes,
Re-Introduced the Entity Implementation column to track Entity and Implementation separately
Introduced a new sheet “To Do” to keep track of design changes needed in the “Data Layer – Siebel”
mapping sheet
Please view the “To Do” sheet in the document which lists the blockers for us in mapping certain attributes.
Let me know in case of any questions.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Tuesday, December 30, 2014 10:01 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Robert Parks; Sajith Sanal; Vinay Shivanna
Subject: RE: OPA Data Mapping

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a.

How many OPA line items in total need to be mapped for OPA eligibility determination + application – 705
(Post-Cleanup activities)
b. How many of these have been mapped to OG Model – 447
c. How many of these mapped to OG model have been mapped to Siebel – 239
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 239
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah

5

From: Vinay Shivanna
Sent: Monday, December 29, 2014 9:11 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Robert Parks; Sajith Sanal; Srikanth Ayanur Harirao
Subject: FW: OPA Data Mapping

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a.

How many OPA line items in total need to be mapped for OPA eligibility determination + application – 720
(Post-Cleanup activities)
b. How many of these have been mapped to OG Model – 300
c. How many of these mapped to OG model have been mapped to Siebel – 220
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 220
Regards,
Vinay S
EXETER
EmailID: vshivanna@exeter.com

skype: vinays09 | mobile: +919008891243
From: Anuroop V. Gaonkar
Sent: Monday, December 29, 2014 5:35 PM
To: Srikanth Ayanur Harirao; Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal
Cc: Vinay Shivanna; Robert Parks; Sajith Sanal
Subject: RE: OPA Data Mapping

Hello Jonah and Rob,
We are making steady progress on mapping; and completed mapping for about 180 OPA elements. Now we need
your help in
a. Getting root of the OPA tree & validating the mapping engine that we have built
b. Ensuring that Vinay and his team progresses quickly in completing the mapping & testing by providing the
appropriate “Condition” logic in the Siebel Mapping sheet to pick up the correct OneGate Entity
Implementations
c. We also noticed that there are 2 places where Relationships are specified; one in OG Entity Implementation
and other in LOV. Out of those we believe the Entity Implementation is the right way. The discrimination
between various types of relationships can be done through the value of “Name” variable present in the
Relationship Entity or by creation of specialized Relationship Entity Implementations as it is being done now.
We need to choose one way of realizing the relationships & not mix – right now there seems to be a mix. At
least we are unable to understand the reason.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Srikanth Ayanur Harirao
Sent: Wednesday, December 24, 2014 8:28 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Vinay Shivanna; Robert Parks; Sajith Sanal
Subject: RE: OPA Data Mapping
6

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
e. How many OPA line items in total need to be mapped for OPA eligibility determination + application – 720
(Post-Cleanup activities)
f. How many of these have been mapped to OG Model – 300
g. How many of these mapped to OG model have been mapped to Siebel – 157 (27 Completed today)
h. For how many items that have been mapped to Siebel have the test cases been written & verified – 157 (27
Completed today)
I’ll also be helping the team to update the conditions / implementations required for the mappings to be completed;
so the number on (b) will progress a bit slow until the issues they’re facing are resolved.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Tuesday, December 23, 2014 7:50 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Vinay Shivanna; Robert Parks; Sajith Sanal
Subject: RE: OPA Data Mapping

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a.

How many OPA line items in total need to be mapped for OPA eligibility determination + application – 757
(Post-Cleanup activities)
b. How many of these have been mapped to OG Model – 300
c. How many of these mapped to OG model have been mapped to Siebel – 130 (28 Completed today)
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 130 (28
Completed today)
I’ll also be helping the team to update the conditions / implementations required for the mappings to be completed;
so the number on (b) will progress a bit slow until the issues they’re facing are resolved.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Monday, December 22, 2014 6:49 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Vinay Shivanna; Robert Parks; Sajith Sanal
Subject: RE: OPA Data Mapping
7

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a. How many OPA line items in total need to be mapped for OPA eligibility determination + application – 788
b. How many of these have been mapped to OG Model – 300
c. How many of these mapped to OG model have been mapped to Siebel – 102
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 102
I’ll also be helping the team to update the conditions / implementations required for the mappings to be completed;
so the number on (b) will progress a bit slow until the issues they’re facing are resolved.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Friday, December 19, 2014 7:25 PM
To: Aditya Adiga B.; Jonah Egenolf; Dattatreya Subramanya Vellal; Anuroop V. Gaonkar
Cc: Vinay Shivanna; Robert Parks; Sajith Sanal
Subject: RE: OPA Data Mapping

Hi All,
Please find the status of mapping as of today.
Please note that this may not be completely accurate as we are in the process of eliminating some of the fields that
are not required.
a. How many OPA line items in total need to be mapped for OPA eligibility determination + application – 788
b. How many of these have been mapped to OG Model – 119
c. How many of these mapped to OG model have been mapped to Siebel – 87
d. For how many items that have been mapped to Siebel have the test cases been written & verified – 87
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Monday, December 15, 2014 7:13 PM
To: Aditya Adiga B.
Cc: Jonah Egenolf; Vinay Shivanna; Dattatreya Subramanya Vellal; Robert Parks; Anuroop V. Gaonkar; Sajith Sanal
Subject: RE: OPA Data Mapping

Hi Aditya,
I’ve reviewed some more fields and have updated the “Notes 2” column of the document.
Please review them too.
Thanks,
Srikanth
8

Mobile: +91 9916253960 | Skype: srikanthah
From: Aditya Adiga B.
Sent: Saturday, December 13, 2014 1:28 AM
To: Srikanth Ayanur Harirao
Cc: Jonah Egenolf; Vinay Shivanna; Dattatreya Subramanya Vellal; Robert Parks; Anuroop V. Gaonkar; Sajith Sanal
Subject: RE: OPA Data Mapping

Hi Srikanth,
I have not been able to spend much time on it today. Let us plan a Skype call on Tuesday, I’ll try to get some work
done on Monday.
Thanks,
Aditya
From: Srikanth Ayanur Harirao
Sent: Friday, December 12, 2014 8:05 AM
To: Aditya Adiga B.; Anuroop V. Gaonkar; Sajith Sanal
Cc: Jonah Egenolf; Vinay Shivanna; Dattatreya Subramanya Vellal; Robert Parks
Subject: RE: OPA Data Mapping

Hi Aditya,
I’ve update the sheet based on your comments and marked them in “Notes 2” column. Please continue reviewing
the attributes. We can discuss on Monday and identify the next steps, I’m fine with anytime.
Sajith,
I did not get a chance to review the attributes marked to be checked by the rules team. Could you please check
these and update if they are indeed needed ?
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Aditya Adiga B.
Sent: Friday, December 12, 2014 3:30 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao
Cc: Jonah Egenolf; Sajith Sanal; Vinay Shivanna; Dattatreya Subramanya Vellal; Robert Parks
Subject: RE: OPA Data Mapping

Hi Anuroop,
Thanks for the wishes.

Srikanth,
As recommended by Anuroop, I have started the review of mapping defined. In the process I have included my
findings in the Notes column and uploaded document to Sharepoint. Please let me know what time would be
convenient for you to discuss the same and define next steps. I have not updated any mapping, as some cells had
formulas and I didn’t want to break anything.
Note:
1.

I have only been able to review first 100 odd records. I’ll continue with the others tomorrow.
9

2.

I have hidden few columns to help me read data, feel free to unhide them.

Thanks,
Aditya
From: Anuroop V. Gaonkar
Sent: Thursday, December 11, 2014 7:22 AM
To: Aditya Adiga B.; Srikanth Ayanur Harirao
Cc: Jonah Egenolf; Sajith Sanal; Vinay Shivanna; Dattatreya Subramanya Vellal; Robert Parks
Subject: RE: OPA Data Mapping

Hey Aditya,
Welcome back. I wish you lots of good luck & happiness all along the new journey that you have begun in your
personal life.
Apologies for not being there at the function – I and Krishna both got caught in some release frenzy on that day.
First, thanks for providing the good foundation sheet. We have expanded that a bit – only change that has been
done is to change the “OneGate Entity Implementation” to “Condition” in order to pick up the relevant OneGate
Model Entity Implementation and the required field thereof. There are some additional columns for tracking &
notes. The Siebel fields Mapped to OPA are provided by Srikanth. He has also tried to get as many OG model
mappings completed. At least for the 50% of OPA model, OG model mappings exist.
Hence;
a.

Can you please validate the OG model mappings that we have done? Can you please indicate any of the
corrections to be made
b. As you indicated, can you please provide the OG model mappings where we have failed to find the right OG
Model placeholders
There is another team working in parallel to Siebel to OG model mapping, they can help validate the mappings as
you create & this will also help speed up the mapping & validation work.
Please let me know if we missed some piece.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Aditya Adiga B.
Sent: Thursday, December 11, 2014 2:57 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao
Cc: Jonah Egenolf; Sajith Sanal
Subject: RE: OPA Data Mapping

Hi Anuroop, Srikanth,
The OneGate Data Layer’s Data Model was constructed for an ideal Intake (outside OPA screens). However, now we
are planning to use OPA based Intake, as an interim solution while we allocate resources to develop ideal Intake. To
accommodate this change in direction, as noted by you & Srikanth, I need to include additional data elements in the
OneGate Data Layer’s Data Model. I’ll start updating the Data Model Visio tomorrow, to include OPA Intake
dependent data elements. Once, I have included these new data elements, we can update the mapping sheet to use
the same.
10

Please let me know if you have questions. I’ll try to provide detailed status on the progress each day.
Thanks,
Aditya
From: Aditya Adiga B.
Sent: Wednesday, December 10, 2014 9:28 AM
To: Anuroop V. Gaonkar
Cc: Jonah Egenolf; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: OPA Data Mapping

Hi Anuroop,
While developing OneGate entities I was in constant discussion with Julien. He confirmed that we had captured
necessary data elements required by the Rules to evaluate. Hence, I am assuming I can assist with the mapping of
most of the OPA elements. Please give me a day or two to review the current mapping. I’ll set-up meeting with
Srikanth after my ramp-up.

All,
I am planning to use this email chain to track updates and issues with mapping. Please try not to mix this with
discussion on utilization/implementation of the mapping. In this regard, I have removed Rob and Phil from the email
chain.
Thanks,
Aditya
From: Anuroop V. Gaonkar
Sent: Wednesday, December 03, 2014 6:06 AM
To: Anuroop V. Gaonkar; Jonah Egenolf; Srikanth Ayanur Harirao; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel - Determination using Data Layer

Hello Jonah,
1.

Srikanth has provided the names of Siebel entities and fields (Columns Y and Z in
OneGate_Data_Layer_External_Service_Mapping ) to which OPA elements are mapped. At the moment we
have not yet mapped 352 opa line items to OG Model. – This is tracked by column AA( Tracker 2).
2. Item 2 mentioned below is complete
3. As Srikanth was unable to come to office for some of the past days due to bereavement in his family, & as I
was focused on admin items, we have not progressed on implementing the conditional mapping mentioned
in item 3.
4. Application Context has been removed.
We still need to decide on
a.

Creation of additional fields in OG Model if no existing field can be mapped.

Mapping and validation of the mapping would require time of about 100+ person days for 700+ fields even with
Optimistic effort estimations based on experience of Plan Selection rewrite team (5 rows can be mapped and tested
per day by a person).
We have enabled 4 member dedicated team to work on mapping of the fields needed by Plan Selection Rewrite. I
need to see how the mappings needed for eligibility determination can be expedited.

11

The discussion with Shekhar has been whether we could bunch eligibility determination and application submission
in to Jan Code Drop – I believe this is the OPTION that we must pursue because
a. we would end up with mapping all most all fields required for application submission as part of eligibility
b. we would need enough time to map & test the OPA fields.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Wednesday, November 26, 2014 3:34 PM
To: Jonah Egenolf; Srikanth Ayanur Harirao; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hello Jonah,
Based on your thoughts following is what we are going to do now:
1.

Try to figure out the mapping (Siebel to OG Model) for the OG model entities that will be used in the
determination. We will try to map as many as we can. – Srikanth will add a tracking column to
OneGate_Data_Layer_External_Service_Mapping sheet to track whether the Siebel to OG model mapping
exists for the specific row or not.
2. Wherever Srikanth has indicated that new field is needed in OG Model, he will provide the Siebel field that
has to be mapped.
3. Agree that we don’t need to map OneGate Entity implementation – We are replacing that with “Condition”
– that specifies the xpath condition required to pick up the appropriate implementation
4. Will get rid of application context. The context is needed if we need to do conditional processing. This does
not come from mapping sheet; but comes from run time.
Once we have Siebel to OG model mapping for all the entities used eligibility determination and have the OPA tree,
we can run the eligibility tests. Once we have complete mapping and once we have the OPA tree, we would need
around 15 days (pessimistic view) to get everything tested ready for release. This schedule remains as per the
original plan. The delivery date will be later than 12th, but would certainly make December drop.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Jonah Egenolf
Sent: Wednesday, November 26, 2014 4:51 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

So we hit some things on the data layer we need to address here:
1) We want to normalize the config for building entities off of Siebel vs. non-Siebel entities. The structure of
the sheets will change a bit to support this normalization.
2) Defining entities off of non-Siebel entities alone does not work. This is my fault. I thought we had something
done that was not done yet.

12

Unfortunately we’re at a bad time to get work done with the holiday coming up here. We’ll try to get this done soon,
but it will push into next week due to the holidays. So the primary goal is to make sure you guys are unblocked and
are able to keep working on things.
So from looking at the sheet, it looks like there are some general Data Layer tasks/training that can be done that are
somewhat independent of the OPA mapping:
-

-

Some of the entities referenced are not fully fleshed out in the main data layer sheet. Intake was a big one
that I would be concerned about. It is likely worthwhile to get those entities ironed out from a pure OG data
layer perspective prior to trying to map the OG entity into the OPA model. This is similar to the task the data
layer testing folks are undertaking right now, but they’re focusing on the entities needed for the PS rewrite.
Many of these fields have complex logic to set them. That is all going to be done via xpath. Looking at
existing examples of field or link overrides should give an idea of what can be done. Also talking to some of
the folks that are doing the PS rewrite/data layer testing would be great here. The goal is to try to learn how
to use xpath so when you go to actually configure the xpaths you won’t be starting from scratch.

Going through these 2 exercises will help a lot when it comes to actually filling out the OPA config.
In terms of the mapping itself, the structure looks good. Comments on that:
-

-

-

You do not need to map to the OneGate Entity Implementation, but that’s easy enough to get rid of. [AG] Done (Replaced with Condition)
In cases where we say a new field is needed, we need to think about where that information comes from
Siebel right now. We have the ability to do complex transforms but we do not have the ability to make up
data from thin air. We can add fields to the OG model, but we still need to know how to populate those OG
fields from the Siebel data. If you can define how we’d set the OG field from Siebel data, we should be fine
here.[AG] - Will try to provide the Siebel field that has to be mapped (We need to figure out OG place
holder)
Can you tell me how you’re using application context? I’m hoping we don’t need to use that at all. We can
simply have a structure for individual and for employee etc. Is the goal to reduce the config here? So rather
than defining N rows for a single attribute, we define it once and it shows up on N different application
types? I don’t like seeing application context as a column either since it feels very OPA specific. But once we
understand intent we can think about how we may be able to rename it.[AG] Will get rid of application
context. The context is needed if we need to do conditional processing. This does not come from mapping
sheet; but comes from run time.
I see some weird use of the entity implementation. For example, q_hhm_caregiver_first_cousin seems to
expect the implementation to do some kind of filtering. The xpath will do that filtering not the
implementation. So anywhere you have meaning like that in the entity implementation likely has to move to
an xpath field override.[AG] This was result of 1. With usage of condition this should also go away.

Otherwise, we’re pretty close on structure and it looks like a huge chunk of the mapping is already there, which is
great. The big gap in the config looks like the xpath definition for field overrides for all those flags etc. that OPA uses.
Pretty much everything with notes will end up having an xpath field override. Step 1 is to learn how to use the xpath
field overrides, but once you are comfortable with that, that’s going to be a big chunk of work that needs to be done.
I think we’ve got enough to do in the steps above that we’re not going to hold you up over the Thanksgiving holiday,
but let’s make sure that’s true. As long as you guys are busy, I won’t feel as bad not getting this as far as I wanted to.
Let’s try to connect on Skype tomorrow to see where we stand.
-

Jonah

From: Anuroop V. Gaonkar
Sent: Tuesday, November 25, 2014 10:06 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Jonah Egenolf; Robert Parks
13

Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hello Jonah,
Following are the links to code and test data:
The OPAModelBuilder converts data that is represented as OPA tree (with embedded pointers to OG model data) in
to OPA assess request. It will also have the responsibility to map the response back to OG Model.
The simple logic is:
a. Create assess request & set the root entity (global instance). Process that root – attributes, children,
relationships
b. For each child entity of the global instance, recursively process attributes, children and relationships
c. Similarly create another root called “config” in assess request – which is place holder for response from OPA
– which also has entities
svn://172.17.10.60/onegate/branches/3.3.2.10-hix-portlet-rewrite-poc/lib/ogdetintf/poc/src/main/java/com/armedica/onegate/servintf/detintf/opa/OPAModelBuilder.java
The test data that mimics the possible OPA tree (1 HHM eligibility determination) is here:
svn://172.17.10.60/onegate/branches/3.3.2.10-hix-portlet-rewrite-poc/lib/ogdetintf/poc/src/main/resources/OPAMappingTest.csv
Many thanks to Srikanth for all his diligent work in mapping, creating test data and giving finishing touches to the
logic.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Tuesday, November 25, 2014 11:59 AM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hello Jonah,
The next steps for us are:
1.
2.

Map AssessResponse content back to OGModel – we will try to finish the code for this by end of this week
Moving away from web service call and making a local call to determination server – This will be done on
evaluation basis and may not be included in delivery as deployment configuration may need to change.

We still need guidance on:
a.

Accommodating additional fields that Srikanth has requested or if there is a mapping for those already in
OG Model
b. When can we get the OPA tree model which we can traverse and set the AssessRequest
c.

Should we start work on creating the biz layer method that can be invoked as web service from Siebel to
launch eligibility determination – this can be done quickly

Regards,
14

Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Friday, November 21, 2014 8:56 PM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hello Jonah & Rob,
Good news is that with “recursively” constructed request we have been able to hit the OPA server and getting
response back on “DATA” errors. There are no “STRUCTURAL” errors in request that we are sending.
Once we ensure that we get these data errors corrected, we will work on persisting the response back to OG model.
Hence could you please provide your guidance on
d. Accommodating additional fields that Srikanth has requested or if there is a mapping for those already in OG
Model
e. When can we get the OPA tree model which we can traverse and set the AssessRequest
f.

Should we start work on creating the biz layer method that can be invoked as web service from Siebel to
launch eligibility determination – this can be done quickly

Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Friday, November 21, 2014 4:41 PM
To: Srikanth Ayanur Harirao; Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hello Jonah and Rob,
Srikanth has published the completed mapping sheet with notes to indicate where he believes new fields are
needed. We have also created the program that can read “test OPA data” from xls sheet and build the entities,
attributes and relationships recursively to create the assessRequest required. We should be done with completing
the testing of this by Monday.
Hence could you please provide decision on:
g.

Accommodating additional fields that Srikanth has requested or if there is a mapping for those already in
OG Model
h. When can we start working with the OPA tree model
i. Should some work start on creating the biz layer method that can be invoked as web service from Siebel to
launch eligibility determination – this can be done quickly
Once the above become available; we can move ahead with additional testing work.
In the meanwhile once eligibility is successfully determined, we will work on
15

a.

Parsing the eligibility data and writing that to OG Model – will be completed as part of eligibility
determination.

b. Moving away from webservice to embedded determination server – Good to have; but will not promise that
this will be completed
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Srikanth Ayanur Harirao
Sent: Thursday, November 20, 2014 4:09 PM
To: Anuroop V. Gaonkar; Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hi Jonah & Rob,
I’ve cleaned up the document on SharePoint. The fields that need to be added have been marked as such using the
“Notes” column. Please filter using that.
Please let me know in case of any queries regarding the new additions.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Wednesday, November 19, 2014 4:17 PM
To: Anuroop V. Gaonkar; Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hi All,
I’ve cleaned up the document and uploaded it to SharePoint. I have marked the “Notes” column appropriately
wherever a new field has been identified to be created.
Also, the “Ignore Row” column has been marked with “Y” for those fields that are not part of Eligibility
Determination.
I’ll be verifying and updating the document if the fields identified for New Field creation are indeed needed. There
are a few fields that could be inferred from the context / relation between tables, these have been marked as such
using the “Notes” column.
Please let me know if you have any queries.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Anuroop V. Gaonkar
Sent: Tuesday, November 18, 2014 2:07 PM
16

To: Jonah Egenolf; Srikanth Ayanur Harirao; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hello Jonah,
Thanks for your time in explaining the answers below. Following is our understanding of how the overall solution
should work in the context of Eligibility determination for data which is already stored in OneGate system.
Please review the overall solution & the plan to execute this.
Overall Sequence in the solution:
1.
2.

3.
4.
5.
6.

7.

User initiates the operation to determine eligibility – Currently this is initiated by case worker from Siebel
The Siebel calls the Biz Layer Method exposed as web service with the MCN for which the eligibility needs to
be determined. Right now this is MCN only. In the days ahead – we will have to overload this method to
provide MCN, Programs and Program Period Corresponding to each program
Business layer can then initiate the call to the relevant rules engine module to determine eligibility giving
the MCN
Rules engine module reads data from data layer and transforms data to format needed by rules engine and
then does the eligibility determination
For all successful eligibility determinations, rules engine module parses the eligibility determination
response and sets the data in OG model in data layer
Then the call from the Biz Layer to rules engine gets completed and rules engine module returns the
eligibility determination success or failure for each instance (MCN, Program, Program Period) where
determination was requested. If failure happened failure reason is also provided
Then Biz layer persists this information to relevant store and does any post processing that is required.

The relevant plan is attached.
Pre Req Steps

Step

2

Task
1 Making the Assess call work
2 Completing the mappings for all the attributes required for eligibility determination
3 Integrating with Data layer to get the data required for Eligibility Determination from OG Data
4 Persist Eligibility Determination to OG Data Model
17

1

5 Complete Integration Testing
Pre Reqs

Task
1 Business layer method exposed as Web Service to take MCN and determine Eligibility
2 Data Layer has tree structure to represent the OPA Data Model which is mapped to OG Data M
3

Notes
Web Service
Persist
Post Process2
Web Service - Need a web service wrapper exposed in Business Layer which will be used to ca
Determination. The Web Service must accept MCN as the input.

Persist - Need a method in the Business Layer to persist the data present in OG Data Model to
Note that the persist must happen for Eligibility Related data only.

Post Processing - As per current business processes, Siebel archives the existing Benefits befo
Benefits are inserted. The same needs to happen in Business Layer. While persisting the data
the existing Benefits must be archived.

Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Jonah Egenolf
Sent: Thursday, November 13, 2014 6:09 PM
To: Anuroop V. Gaonkar; Srikanth Ayanur Harirao; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: Re: Locking Data Mapping Excel

So I think the confusion is that Application is more generic than you are taking it to mean. Application
means any intake of data changes for a program. So CoC is a form of application. And there may be N
applications for a single program. Applicants are attached to programs by applications.
So an example:
- Initial application of people A and B on program X would create 2 applicants on program X added by
application 1.
- CoC on program X would be application 2. Say this CoC adds applicant 3. Now we have a third applicant
on program X added by application 2.
- Second CoC on program X would be application 3. Say this CoC removes applicant 2. Now applicant 2 was
added by application 1 and removed by application 3.

I think application may be a confusing term here, but what is intended to mean is: a change of the
relationship between a set of people and a program. There is an initial application that establishes the
relationship and there are subsequent applications that modify that relationship in some way (it may be as
simple as an address change, but it would still be an 'application').
18

And the key point is: not all applications change the number of applicants on the program. And storing the
applicants on the application would be somewhat redundant. And even if we did, you would for SURE want
a way to see all applicants on a program without having to know which application to look at. We could
make some rule to always look at the 'latest' non-pending application, but it seems cleaner to just always
look at the program for a current view of the applicants.
Does that make more sense? I think the term applicant implies it is a child of application, but really it is a
child of program. We could call it program applicant or program member maybe?
- Jonah

From: Anuroop V. Gaonkar
Sent: Thursday, November 13, 2014 6:32 AM
To: Srikanth Ayanur Harirao; Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel
Hi Rob, Jonah
We are running in to following problems when we try to map the OG Model to OPA.
OPA does determination on Intake data. Now in OG model, the navigation path is Intake

Application ?? Aplicant?

We are unable to figure out when the Applicant gets created?
a. Will Applicant instances (rows) created every time an application instance (row) gets created?
b. If every time applicant is getting created, for each new application why do we have fields such as
“CreatedByApplication” and “RemovedByApplication” in Applicant?
c. If Applicant is not being created each time, where is the link table between the applicant and application?
d. Where is the relationship between “Applicant” and “Person” being stored? If there is no relationship
between Applicant and Person then I am finding it hard to navigate from Intake up to Person to get the data
needed to be populated in the OPA. Can you please tell us if there is a way?
e. Let’s take example of CoC application – how do we do Intake data prepopulation?

The practical problem is OG Model has MCN as root, there is no one definitive intake associated with MCN, hence
unless we have some logic to determine the relevant Intake in given MCN context would be hard to determine
eligibility. I am sharing the problem – if you have already thought, wish to hear the answer.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Srikanth Ayanur Harirao
Sent: Tuesday, November 11, 2014 5:46 PM
To: Jonah Egenolf; Robert Parks
Cc: Phil Currier; Sajith Sanal; Anuroop V. Gaonkar; Aditya Adiga B.
Subject: RE: Locking Data Mapping Excel

Hi Rob,

19

I’ve updated the latest updates on SharePoint. The latest updates contain OPA to OG Data Model mapping for some
of the fields.
Pending Tasks
Complete the remaining mapping for OPA to OG Data Model
Separate out the IFSE attributes from that of SHOP ER attributes
After the initial set of mapping, we tried to logically map the OPA attribute “q_hh_applicant_agree_3pv” which
corresponds to the “External Verification Question”, to that of a field in OG Data Model (Element –
AgreeToExternalVerification, Entity / Implementation - Intake). We had trouble mapping the path from the MCN
context to arrive at the “AgreeToExternalVerification” field.
Could you help us do the logical map ?
For Example, in order to derive the above mapping we pass the context of the MCN (and assuming the above field
will be set for the Primary Applicant) the Primary Applicant Id,

1.
2.
3.
4.
5.
6.
7.

getMCNContext(masterCaseNumber, primaryApplicantPersonId)
getProgramCase(masterCaseId)
getProgramPeriod(programCaseId)
getApplicant(programPeriodId)
getApplication(programPeriodId)
getIntake(applicationId)
getAgreeToExternalVerification(intakeId)

Note : Step 4 may not be required
Is the above correct ? What about the cardinality of these tables ?
In summary, we need to get one unique value for “AgreeToExternalVerification” in the context of given MCN. How
do we get this ?
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Srikanth Ayanur Harirao
Sent: Wednesday, November 05, 2014 6:31 PM
To: Anuroop V. Gaonkar; Aditya Adiga B.; Jonah Egenolf
Cc: Robert Parks; Phil Currier; Sajith Sanal
Subject: RE: Locking Data Mapping Excel

Hi All,
I’ve updated the document on SharePoint with the list of OPA attributes (IF, EE and ER).
I’ll be attending the “Effective Communication” training scheduled from tomorrow till Saturday, and will not have a
chance to update the excel till then.
Pending Tasks
Updating the sheet with the corresponding Data Model fields

20

-

I didn’t realize that the latest template provided separate sheets to track IFSE and ER mappings separate,
Currently, the attributes are merged into a single sheet. This needs to be separated out (as some of the
Assister and general fields are common across IFSE and ER rulebases)

Please let me know in case of any questions.
Thanks,
Srikanth
Mobile: +91 9916253960 | Skype: srikanthah
From: Anuroop V. Gaonkar
Sent: Wednesday, November 05, 2014 3:03 PM
To: Aditya Adiga B.; Jonah Egenolf
Cc: Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: Locking Data Mapping Excel

Hello Aditya,
Thanks for giving a go ahead. Will continue to work with the Jonah & team in the e-mail. Srikanth & Sajith will add
the OPA entities, attributes, relationships to the xls that we have provided. They will start with IF. Once all OPA
elements are added, we will try to map those to appropriate elements in the OG Model. There we will rely on data
dictionary. If we can’t figure out some item/ need some additions / modifications, will come back to the team here.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Aditya Adiga B.
Sent: Wednesday, November 05, 2014 12:22 AM
To: Jonah Egenolf; Anuroop V. Gaonkar
Cc: Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: Locking Data Mapping Excel

Note to the group.
Srikanth has taken the lead and is updating the mapping to include OPA Entity, Attributes and Relationships. Given
my upcoming vacation, I’ll assist him on need basis to update the Excel (available in Sharepoint). Please let me know
if there is any issue.

Anuroop,
Please feel free to update the Excel, if the template does not meet technical needs. Given my upcoming vacation, I
am hoping you will be gatekeeper on the template used for External Service (OPA) mapping.
Thanks,
Aditya
From: Anuroop V. Gaonkar
Sent: Tuesday, November 04, 2014 2:35 PM
To: Anuroop V. Gaonkar; Aditya Adiga B.
Cc: Jonah Egenolf; Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: Locking Data Mapping Excel

21

Hello All,
Yesterday there was again a small discussion around why do we need to write code to read the xlsx sheet. The
explanation is as below
There is OG Model to physical model mapping –Rob has defined – we have xls reader & converter to tree
Then we have defined generic way to map any secondary model to OG Model – This is the sheet Aditya sent across –
We don’t have reader & converter to tree. We need this now.
The basic assumptions are as below:
The DL (data layer) tree based on OG model is the primary tree. The DL Tree has Node with MCN as root.
There can be other models – which are the secondary models that we need to operate with. These secondary
models may have some other entities as roots.
The entities in DL tree (primary) need to be referenced in the tree corresponding to secondary model. This will
ensure that is only 1 copy of data corresponding to any entity even though there are multiple views.
The most natural way to build the trees from secondary models is as below:
1.

Create template mapping sheet that helps us build tree like secondary model structure (this has been done
now)
2. We need to create 1 instance of above sheet for each secondary model that we need to use – This is needed
because the elements in OPA are different than the ones that some other 3rd party such as edifecs may need.
3. Have generic xlsx reader & tree builder logic to read this template secondary model mapper sheet &
convert that in to a tree – This will lead to distinct parallel trees
4. We can use these distinct tree structures to read & write data between secondary model object &
corresponding OG model entity.
The above leads to the construct where all trees are backed by only 1 copy of data present in OG model.
We can make all the above steps generic, except the step to construct the “objects in secondary model”. We need to
have distinct sets of code to build these objects because the engines that process secondary models need to get data
in the format they understand. Thus we need separate sheets to specify these objects as well as map these objects
to onegate. Even though the mapping xlsx is read by generic reader & converted in to tree structure; we need code
to interpret that tree structure & generate the secondary model objects.
Jonah – I hope the above provides enough info on why we need one more class to read generic mapping sheet xlsx
. Each instance of this will be distinguished from the other by the name of the secondary model it is trying to map
to OG model.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Monday, November 03, 2014 4:49 PM
To: Aditya Adiga B.
Cc: Jonah Egenolf; Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: Locking Data Mapping Excel

Hello Aditya
Column “B” Entity Implementation may not be required. Similarly Column “I” Linked entity implementation is also
not required. I don’t have specific wrapper implementations in OPA for the OPA entities.
22

10 to 12 are required because, to navigate through the DLEntity and linked entity graph we should be able to provide
the specifics in the xpath for querying.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Aditya Adiga B.
Sent: Monday, November 03, 2014 12:08 PM
To: Anuroop V. Gaonkar
Cc: Jonah Egenolf; Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: Locking Data Mapping Excel

Hi Anuroop,
Do we need 10-12? That data is part of OG to SBL mapping, ideally we should not be repeating it here.
Attached is the template based on the email below. Please review and let me know if any change is required.
Thanks,
Aditya
From: Anuroop V. Gaonkar
Sent: Friday, October 31, 2014 3:26 PM
To: Anuroop V. Gaonkar; Aditya Adiga B.; Jonah Egenolf; Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur
Harirao
Subject: RE: Locking Data Mapping Excel

Hello Aditya,
Could the OPA mapping sheets have the following columns in the following order. Please decide the final names; but
this information would be needed
1.

OPA Container Entity (This should have the id associated with OPA entity – for example this can be global or
householdmember)
2. OPA Element (OPA entity, attribute or relationship id – for example this should be var_hhm_first_name or
householdmember or any relationship id)
3. OPA Element Type (Entity | Attribute | Relationship)
4. OPA Target Entity (Filled in only if the OPA Element Type value is Relationship)
5. OPA Relationship Cardinality (Filled only if the OPA Element Type value is Relationship) – This will be
One2One, or One2Many
6. OPA Attribute Data type (Filled only if the OPA Element type is Attribute)
7. OG Entity Name
(This should reference the corresponding value in Column C of Siebel Mapping
sheet – as that is our primary mapping sheet)
8. OG Entity Implementation (This should reference the corresponding value in Column D of Siebel Mapping
sheet – as that is our primary mapping sheet)
9. OG Element Name
(This should reference the corresponding value in Column E of Siebel Mapping sheet
– as that is our primary mapping sheet)
10. OG Element Type
(This should reference the corresponding value in Column F of Siebel Mapping sheet
– as that is our primary mapping sheet)
11. OG Linked Entity Name (This should reference the corresponding value in Column G of Siebel Mapping sheet
– as that is our primary mapping sheet)
12. OG Linked Entity Implementation (This should reference the corresponding value in Column H of Siebel
Mapping sheet – as that is our primary mapping sheet)
23

We will use the java mapping generated from generic – because that simplifies the processing for OPA significantly.
There is no need to build explicit tree structure for OPA, as for each entity the following recursive logic would work:
1.
2.
3.

Get entity
Find all attributes & set those by querying those from OG model
Find all child entities & for each child entity start with step 1

4.

To avoid deadlock in entity construction, process the relationships after all entities have been constructed –
This piece of logic may have to be refined.

Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Friday, October 31, 2014 2:47 PM
To: Aditya Adiga B.; Jonah Egenolf; Robert Parks; Phil Currier; Sajith Sanal; Srikanth Ayanur Harirao
Subject: RE: Locking Data Mapping Excel

Hello All,
The summary of what we discussed yesterday was:
1.
2.
3.

For each of the external models we will end up creating newer mapping to OG model
Only OG Model to Siebel layer (implementation model) should worry about read & writes
All other models will map to OG model. This means OPA model 1, model 2 / any other model OG Model
Any physical model (currently Siebel)
4. We may need to version the mapping sheets as generated code version has to refer to specific version of
mappigng sheet in order for us to easily decide on changes/corrections.
5. There will be distinct mappings to distinct rulebases resulting in more than one parallel tree
As Rob said the mapping has direction. For example if we were to traverse OG Model we would always begin by
using MCN as root; but if we were to look at OPA model, then we would use Global Instance as root & build global
instance. The Global Instance in OPA is not mapped to any entity in OG model. Thus there may be different roots in
different models. Are all relationships commutative in mapping? If not, then there may be complications. Meaning
A B, does that implay B A?
Discussed with Aditya to create separate sheets for distinct set of OPA rulebases.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Aditya Adiga B.
Sent: Friday, October 31, 2014 2:31 PM
To: Anuroop V. Gaonkar; Jonah Egenolf; Robert Parks; Phil Currier
Subject: RE: Locking Data Mapping Excel

FYI, I have unlocked the mapping Excel. As per yesterday’s discussion I’ll be creating a separate mapping Excel for
Rules.
Thanks,
Aditya
24

From: Anuroop V. Gaonkar
Sent: Wednesday, October 29, 2014 10:51 PM
To: Jonah Egenolf
Cc: Aditya Adiga B.; Robert Parks; Phil Currier
Subject: RE: Locking Data Mapping Excel

Hi Jonah,
May be I have a wrong understanding of how the object model at runtime in the data layer that has been
implemented would be structured. Yes, we can certainly discuss. My understanding is that the DL elements
etc provide XML like node structure that has meta information about entity implementation and also that
hold references to entity implementations. By adding columns we add meta info that helps us do
translations.
I shall discuss that tomorrow.
Thanks for quick feedback.
Regards,
Anuroop
On 29 Oct 2014 21:43, Jonah Egenolf <jegenolf@exeter.com> wrote:
I think we’re going down the wrong path here. I don’t know where the reuse argument is coming from, but that is off
base. No matter how many sheets we have, we’ll always be using the onegate data to map to the sheet (or vice
versa). So say we have a Siebel mapping and an OPA mapping. And we need to send a view of the world to OPA. We
will read the model, pull from Siebel (because one view has to be identified as the persistent view of Onegate),
transform the Siebel data to the Onegate model, then transform the Onegate model to the OPA model. Note there is
only 1 read from a datasource there even though we interacted with 2 external models (Siebel and OPA).
So thinking generically, what we have is:
-

A definition of the onegate model
A definition of the mapping to and from any external system to the onegate model

The confusion comes because we lumped those 2 together for the Siebel mapping, partly because Siebel is our
‘primary’ or persistent external model. But that, in some sense, is a philosophical mistake. What we COULD have
done is:
-

Define the onegate model
Define the mapping between Siebel and onegate, flag Siebel as primary
Define the mapping between OPA and onegate

What we do not want to do is add columns for every external system we need to interact with. We can add sheets
for as many external systems as we want. If, instead, we add 15 columns per external system and we have 100
systems we can talk to, we’re looking at a very crappy monolithic spreadsheet.
So I’d like to take a step back here and look at what you’re trying to do. I think there will be a different way to
achieve what we need without adding columns to the sheet. And any columns we do add would be in support of
mapping to a generic system, not anything OPA specific. If we see OPA in the column name, that’s a good indicator
that we’re doing something wrong.
Can you guys find me on Skype tomorrow morning and we can talk through this?
-

Jonah

From: Anuroop V. Gaonkar
Sent: Wednesday, October 29, 2014 3:08 AM
To: Aditya Adiga B.; Robert Parks; Phil Currier; Jonah Egenolf
Subject: RE: Locking Data Mapping Excel
25

Hello Aditya,
Thanks for the discussion. The changes would help in achieving our goal of performing OPA operations based on
information in data layer . Thanks for your insights on how the OPA names differ between the rulebases & how
relationships work in OPA.
As discussed with Jonah – the key reasons for updates to existing sheet are:
1.

Reuse – The in memory OG Model built with scaffolding of DLElement, DLAttribute, DLField should be used
to translate OG model in to any other model. If we create different mapping sheets, then we would force us
to build 2 distinct caches in memory and force us to do twice the amount IO to underlying CRM or DB. In
addition we also need to re implement the scaffolding Rob has built. With only one mapping sheet, we will
have only 1 in memory cache of values. We just need to enhance the DLField implementation to make
allowance for storage of values added in these additional columns.

2.

If we end up creating 2 distinct in memory caches then we need to start thinking about solutions to keep
these in memory caches in sync – this is a non trivial & costly problem to solve. Then we may need to build
one more layer of mapping & complicate unnecessarily.

Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Aditya Adiga B.
Sent: Wednesday, October 29, 2014 12:02 PM
To: Robert Parks; Phil Currier; Jonah Egenolf
Cc: Anuroop V. Gaonkar
Subject: Locking Data Mapping Excel
Importance: High

Hi,
Anuroop and team will be working on OneGate Data Model to OPA mapping. In this regard, it has been identified
that current Excel is most suitable to include necessary OPA mapping. In this regard, I’ll be adding 15 columns to the
existing Excel and including OPA information in those columns (one column for each Rulebase):
1. OPA <Rulebase Name> Entity
2. OPA <Rulebase Name> Element
3. OPA <Rulebase Name> Element Type
4. OPA <Rulebase Name> Data Type
5. OPA <Rulebase Name> Linked Entity

Rob, Phil,
Please let me know if there is any issue with me updating the file. Also, does the location of new columns matter?
I.e. should they be added after the ‘Ignore Row’ column OR is it acceptable to include after Siebel information
column?

Jonah,
Please let me know if you wish to discuss the changes to the Excel.
Thanks,
26

Aditya
Aditya B. Adiga
Exeter Group, Inc.
617.528.5032 office
617.899.0878 mobile
www.exeter.com

27


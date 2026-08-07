---
title: "Plan Selection Revamp"
date: 2014-01-01
year: 2014
era: Exeter
organization: Exeter (Edifecs)
category: Do The Right Thing
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Kavya Ramaiah", "Sachin Shivarama Nayak", "Vinay Sulumane"]
skills: ["Data Layer", "Data Layer Design", "Portal Development", "Problem Solving", "Technical Excellence"]
programs: ["OneGate"]
tags: ["appreciation", "do-the-right-thing"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Plan Selection Revamp

## Source
- **File:** `DoTheRightThing_PlanSelectionRevamp_December16th2014.pdf`
- **Date:** 2014-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Do The Right Thing

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 3

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> Cc: Vinay Sulumane Visweswara; Sachin Shivarama Nayak; Kavya Ramaiah; Vinay Shivanna;

## Full Content
```
Dattatreya Subramanya Vellal
From: Dattatreya Subramanya Vellal
Sent: Tuesday, December 16, 2014 5:47 PM
To: Anagha Joshi
Cc: Vinay Sulumane Visweswara; Sachin Shivarama Nayak; Kavya Ramaiah; Vinay Shivanna;
Abhishek Ramesh Babu; Ashwini Ramesh Hegde; Harish Kumar Karnati; Ariktam Kundu;
Sindhu Handalagere Suresh; Karthikeyan Vellingiri; Aravindh Pennadam Gopi
Subject: RE: Plan Selection Improvement - Code Wise
Attachments: IF Plan Selection – Rewrite and Data Later Adoption - Imovements.pptx
Thank you soo much guys. Here’s what I have come up with. Let me know if you have suggestions or improvements.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Anagha Joshi
Sent: Tuesday, December 16, 2014 1:12 PM
To: Dattatreya Subramanya Vellal
Cc: Vinay Sulumane Visweswara; Sachin Shivarama Nayak; Kavya Ramaiah; Vinay Shivanna; Abhishek Ramesh Babu;
Ashwini Ramesh Hegde; Harish Kumar Karnati; Ariktam Kundu; Sindhu Handalagere Suresh; Karthikeyan Vellingiri;
Aravindh Pennadam Gopi
Subject: Plan Selection Improvement - Code Wise
Hi Datta,
Please find the improvement of Plan Selection Rewrite code compared to the existing code as follows:
Improvement Areas Old Plan Selection New Plan Selection Comments
Lines of code in 10581 812
Controller
Lines of code to fetch 10581 2835 Old PS had the logic in
the data required to Controller itself.
paint a screen and New PS has it in the
persist data on the PlanSelectionUIServiceImpl
screen
Number of jsps 27 10 Old PS had 5 different jsps ,
one for each of the product
types - QHP, Dental, Vision,
Medicaid and CHIP for plan
selection and compare
screens.
New PS has 10 jsps in total
(excluding Tobacco ,Compare
Plans and NPI screens which
have not been coded yet)
That would make the count
13!
Spring feature Form binding concept was Extensive usage of
rarely used form binding
Tag usage Minimal Extensive New PS has reusable tags for
all the UI controls.
Basic UI controls:
1
• Button
• Checkbox
• Currency
• Dropdown
• Image
• Label
• Link
• Modal
• Radio
• Table
• Text
Plan Selection UI Controls:
• Cart Plan Tile
• Plan tile
• Plan Details
• Breadcrumbs
Modularity Basically had a single render Each screen has its
mapping and action mapping own render and action
mapping
Business logic Logic was scattered across The logic is centralized
api, controller and other in og-businesslayer
classes
Reusability of screens Not really reusable Just copy paste render
and action mapping to
the required portlet
and tweak in the
changes and you are
done!
Parameters and Messages and configurable Messages and • Makes it more secure
Messages properties were in configurable and less error prone
messages.properties , properties are in • No property files are
application.properties and database tables required
onegate-portal.properties • Entries in onegate-
portal.properties is
reduced
Session handling Portlet session(globalSession) Data layer session is
was used to dump the used
required sessi
```

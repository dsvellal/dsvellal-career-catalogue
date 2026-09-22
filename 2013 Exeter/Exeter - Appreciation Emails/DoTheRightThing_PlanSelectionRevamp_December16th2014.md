# DoTheRightThing PlanSelectionRevamp December16th2014

> Converted from document `DoTheRightThing_PlanSelectionRevamp_December16th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:
Attachments:

Dattatreya Subramanya Vellal
Tuesday, December 16, 2014 5:47 PM
Anagha Joshi
Vinay Sulumane Visweswara; Sachin Shivarama Nayak; Kavya Ramaiah; Vinay Shivanna;
Abhishek Ramesh Babu; Ashwini Ramesh Hegde; Harish Kumar Karnati; Ariktam Kundu;
Sindhu Handalagere Suresh; Karthikeyan Vellingiri; Aravindh Pennadam Gopi
RE: Plan Selection Improvement - Code Wise
IF Plan Selection – Rewrite and Data Later Adoption - Imovements.pptx

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
Improvement Areas
Lines of code in
Controller
Lines of code to fetch
the data required to
paint a screen and
persist data on the
screen
Number of jsps

Old Plan Selection
10581

New Plan Selection
812

Comments

10581

2835

Old PS had the logic in
Controller itself.
New PS has it in the
PlanSelectionUIServiceImpl

27

10

Old PS had 5 different jsps ,
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

Spring feature

Form binding concept was
rarely used

Extensive usage of
form binding

Tag usage

Minimal

Extensive

1

New PS has reusable tags for
all the UI controls.
Basic UI controls:

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
Modularity

Basically had a single render
mapping and action mapping

Business logic

Logic was scattered across
api, controller and other
classes
Not really reusable

Reusability of screens

Parameters and
Messages

Session handling

Inter portlet
communication

Usage of SOA
Unit testing per page(UI
testing)
Onegate styling

Each screen has its
own render and action
mapping
The logic is centralized
in og-businesslayer
Just copy paste render
and action mapping to
the required portlet
and tweak in the
changes and you are
done!
Messages and
configurable
properties are in
database tables

Messages and configurable
properties were in
messages.properties ,
application.properties and
onegate-portal.properties

•
•
•

Portlet session(globalSession)
was used to dump the
required session values
Http session is used

Data layer session is
used

Mostly reads and writes were
through SOA
Not possible

SOA is deprecated

Custom CSS, repeated css

Centralized style
sheets are used

Data layer session can
be used.
This is more secure

Can be done easily

Regards,
Anagha
Anagha Joshi| Senior Software Engineer | E X E T E R | 4th floor, Nitesh Timesquare
8, M.G. Road| Bangalore 560001 | India
2

Makes it more secure
and less error prone
No property files are
required
Entries in onegateportal.properties is
reduced

This is yet to be done as we
have only ported IF PS for
now

Extn:+91-80 33450011 • Mobile: +91-9738348162 • Skype ID: anagha.joshi20

3


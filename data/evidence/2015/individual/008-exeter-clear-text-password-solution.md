---
title: "Clear Text Password Solution"
date: 2015-01-01
year: 2015
era: Exeter
organization: Exeter (Edifecs)
category: Do The Right Thing
source_type: email
channel: email_archive
involvement: author
role: Senior Lead - Software Development
people: ["Brett Ackerman", "Chandrashekhar Surendranath", "Chevy Vithiananthan", "Jonah Egenolf", "Krishnamurthy Hegde", "Lakshmi Thanga-Raja", "Robert Parks"]
skills: ["Portal Development", "Problem Solving", "SOA", "Siebel", "Technical Excellence"]
programs: ["OneGate"]
tags: ["appreciation", "do-the-right-thing"]
sentiment: positive
impact_type: technical
recurring: false
---

# Evidence: Clear Text Password Solution

## Source
- **File:** `DoTheRightThing_ClearTextPasswordSolution_October16th2015.pdf`
- **Date:** 2015-01-01
- **Ingested:** 2026-08-06
- **Channel:** Email Archive (Exeter)
- **Category:** Do The Right Thing

## Metadata
- **Type:** Email
- **Project:** OneGate
- **Pages:** 5

## Datta's Involvement
- **Role at time:** Senior Lead - Software Development
- **Involvement type:** Author

## Key Quotes
> We have come up with the following solution. The path that we are exploring right now is this:

## Full Content
```
Dattatreya Subramanya Vellal
From: Dattatreya Subramanya Vellal
Sent: Friday, October 16, 2015 5:35 PM
To: Chandrashekhar Surendranath
Cc: Amit Sharma
Subject: RE: Clear Text
Hi Shekhar,
We have come up with the following solution. The path that we are exploring right now is this:
* If siebel.properties file exists in the location $OG_HOME/config/, then:
a) Read the file, encrypt the contents, and store it within og-api as an encrypted file
b) Delete the siebel.properties file present in the location
c) When we want to get the password, decrypt the file by reading it from within og-api, obtain the key-value
pair and proceed
* If $OG_HOME/config/ does not contain siebel.properties file, then we know that it has been read and stored
within og-api, therefore, go to step c) directly.
This has to be done on load of og-api in Portal, and as a dummy service for invoking the same on SOA.
We have done, as a POC, Step1a. We are working towards achieving b and c. And once this is done, we still have to
do the following things:
1. Centralize all Header injections into one code within og-api
2. Create a utility which reads and either encrypts (and writes it within api, and deletes the original one) or
decrypts the file contents to give us key-value pairs to be used in the program.
3. Test things out completely to see if this works
We are going to go with a symmetric encryption algorithm – DES, for encryption and decryption. We will need time
till Wednesday or so to prove this end-end on a live environment.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Chandrashekhar Surendranath
Sent: Friday, October 16, 2015 11:25 AM
To: Dattatreya Subramanya Vellal <dvellal@exeter.com>; Amit Sharma <amit.sharma@exeter.com>
Subject: FW: Clear Text
Some more information
From: Brett Ackerman
Sent: Friday, October 16, 2015 12:24 AM
To: Krishnamurthy Hegde <khegde@exeter.com>; Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Jonah Egenolf <jegenolf@exeter.com>; Robert Parks <rparks@exeter.com>; Amit Sharma
<amit.sharma@exeter.com>
Cc: Christopher Simo <CSimo@exeter.com>
Subject: RE: Clear Text
+ Chris
1
Brett Ackerman | E X E T E R | 800 Boylston Street, Suite 3500 Boston, MA 02199 | Office: 617.528.5138 | Cell: 617.645.4570
From: Brett Ackerman
Sent: Thursday, October 15, 2015 2:54 PM
To: Krishnamurthy Hegde <khegde@exeter.com>; Chevy Vithiananthan <chevyv@EXETER1.onmicrosoft.com>;
Lakshmi Thanga-Raja <Lakshmi@exeter.com>; Chandrashekhar Surendranath <schandrashekhar@exeter.com>;
Jonah Egenolf <jegenolf@exeter.com>; Robert Parks <rparks@exeter.com>; Amit Sharma
<amit.sharma@exeter.com>
Subject: RE: Clear Text
Krishna,
Details from Optum on how they set up their credentials for web services.
In 11g we use Oracle’s policy based authentication (OWSM) - see
https://docs.oracle.com/cd/E21764_01/web.1111/e13713/owsm_appen
```

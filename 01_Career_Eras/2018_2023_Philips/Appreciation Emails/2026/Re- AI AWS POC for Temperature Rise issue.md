# Re: AI AWS POC for Temperature Rise issue

**From:** "Subramanya Vellal, Dattatreya" <dsvellal@philips.com>  
**To:** "Rajan, Kaveri" <Kaveri.Rajan@philips.com>, "Yoo, Andrew" <andrew.yoo@philips.com>, "Brown, Cynthia" <cynthia.brown@philips.com>, "Donlon, John" <john.donlon@philips.com>, "Dianis, Scott" <scott.dianis@philips.com>, "Lee, Jewel" <Jewel.Lee@philips.com>, "Sarkar, Rupam" <rupam.sarkar@philips.com>  
**Date:** Fri, 08 May 2026 05:50:08 +0000  

---

+Nataraj, Sundar from IEN - to keep them updated about this discussion.

As a quick proof of concept, I took the documents, and then converted each of them into chunks, nodes, edges, tags, doc-labels, and given the complaint, tried to regenerate the report out of it.

Attached are a few documents for you to review:

  1.
The original document prepared by Jewel/Kaveri is here: [https://res-2.df.onecdn.static.microsoft/files/fabric-cdn-prod_20251010.003/assets/item-types/16/docx.svg] PD47114_IIA REQUEST SUBMISSION.docx<https://share.philips.com/:w:/r/sites/UltrasoundDataandResearch/Shared%20Documents/Quantitative%20Patient%20Risk/AWS%20AI%20POC/Temperature%20Rise/PD47114_IIA%20REQUEST%20SUBMISSION.docx?d=wd2b9ff8f83f54637956ba5c8a0db03e5&csf=1&web=1&e=UJb1Rh>
  2.
AI generated document is attached, named: 03_Generated_IIA_PD47114.pdf
  3.
A comparison between the original document and the generated document is attached for you to refer to as well, that is at: 02_Comparison_Report.pdf
  4.
A process report document, gives you the detailed process of how I went about doing this, is attached: 01_Process_Report.pdf

We can always argue, "are we not reverse engineering from the actual report?", however, this also serves as a proof that if we "structure" our data properly, we will be able to generate the content for the "templated IIA report", based on a compliant.

Based on the proof of concept, I am confident that this as a "data" problem and not a "reasoning problem". I used Philips enterprise approved Claude Code, and Claude Models to build the data and reports.

Happy to explain/discuss more. Let me know.

-- Datta

Software Competency Lead

Innovation Engineering, Innovation & Design


From: Rajan, Kaveri <Kaveri.Rajan@philips.com>
Date: Saturday, May 2, 2026 at 22:26
To: Yoo, Andrew <andrew.yoo@philips.com>; Brown, Cynthia <cynthia.brown@philips.com>; Donlon, John <john.donlon@philips.com>; Dianis, Scott <scott.dianis@philips.com>; Lee, Jewel <Jewel.Lee@philips.com>; Sarkar, Rupam <rupam.sarkar@philips.com>; Subramanya Vellal, Dattatreya <dsvellal@philips.com>
Cc: Karuppan Chetty, Anuradha <anuradha.chetty@philips.com>; Agarwal, Anup <anup.agarwal@philips.com>; Sarkar, Rupam <rupam.sarkar@philips.com>
Subject: RE: AI AWS POC for Temperature Rise issue

Hi Andrew,
Rupam has already created the Data Dictionary.

From: Yoo, Andrew <andrew.yoo@philips.com>
Sent: Saturday, May 2, 2026 9:40 AM
To: Brown, Cynthia <cynthia.brown@philips.com>; Rajan, Kaveri <Kaveri.Rajan@philips.com>; Donlon, John <john.donlon@philips.com>; Dianis, Scott <scott.dianis@philips.com>; Lee, Jewel <Jewel.Lee@philips.com>; Sarkar, Rupam <rupam.sarkar@philips.com>; Subramanya Vellal, Dattatreya <dsvellal@philips.com>
Cc: Karuppan Chetty, Anuradha <anuradha.chetty@philips.com>; Agarwal, Anup <anup.agarwal@philips.com>; Sarkar, Rupam <rupam.sarkar@philips.com>
Subject: Re: AI AWS POC for Temperature Rise issue


Cynthia - why don’t we loop in Rupam Sarkar for the log files?

and we can have him recreate what Scott did.. this would be his first onboarding to supporting medical informatics and epi and we can start the methods and data dictionary work..




Sent from iPhone



Andrew Yoo, MD, MS, MPH

Head of Medical and Clinical

Ultrasound

Philips



22100 Bothell Everett Highway, Bothell, WA 98021, USA

Tel 206-445-8751, Email andrew.yoo@philips.com<mailto:andrew.yoo@philips.com>



________________________________
From: Brown, Cynthia <cynthia.brown@philips.com<mailto:cynthia.brown@philips.com>>
Sent: Friday, May 1, 2026 7:18 PM
To: Rajan, Kaveri <Kaveri.Rajan@philips.com<mailto:Kaveri.Rajan@philips.com>>; Donlon, John <john.donlon@philips.com<mailto:john.donlon@philips.com>>; Dianis, Scott <scott.dianis@philips.com<mailto:scott.dianis@philips.com>>; Yoo, Andrew <andrew.yoo@philips.com<mailto:andrew.yoo@philips.com>>; Lee, Jewel <Jewel.Lee@philips.com<mailto:Jewel.Lee@philips.com>>; Sarkar, Rupam <rupam.sarkar@philips.com<mailto:rupam.sarkar@philips.com>>; Subramanya Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>
Cc: Karuppan Chetty, Anuradha <anuradha.chetty@philips.com<mailto:anuradha.chetty@philips.com>>; Agarwal, Anup <anup.agarwal@philips.com<mailto:anup.agarwal@philips.com>>; Sarkar, Rupam <rupam.sarkar@philips.com<mailto:rupam.sarkar@philips.com>>
Subject: RE: AI AWS POC for Temperature Rise issue

Hi,

I sent Datta instructions for how to get access to the Vertica database a few weeks ago. @Subramanya Vellal, Dattatreya<mailto:dsvellal@philips.com> have you been able to make progress here?
Best regards,
Cynthia

From: Rajan, Kaveri Kaveri.Rajan@philips.com<mailto:Kaveri.Rajan@philips.com>
Sent: Friday, May 1, 2026 6:58 PM
To: Donlon, John <john.donlon@philips.com<mailto:john.donlon@philips.com>>; Dianis, Scott <scott.dianis@philips.com<mailto:scott.dianis@philips.com>>; Yoo, Andrew <andrew.yoo@philips.com<mailto:andrew.yoo@philips.com>>; Lee, Jewel <Jewel.Lee@philips.com<mailto:Jewel.Lee@philips.com>>; Brown, Cynthia <cynthia.brown@philips.com<mailto:cynthia.brown@philips.com>>; Sarkar, Rupam <rupam.sarkar@philips.com<mailto:rupam.sarkar@philips.com>>; Subramanya Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>
Cc: Karuppan Chetty, Anuradha <anuradha.chetty@philips.com<mailto:anuradha.chetty@philips.com>>; Agarwal, Anup <anup.agarwal@philips.com<mailto:anup.agarwal@philips.com>>; Sarkar, Rupam <rupam.sarkar@philips.com<mailto:rupam.sarkar@philips.com>>
Subject: AI AWS POC for Temperature Rise issue

Hi team,

We are working with @Subramanya Vellal, Dattatreya<mailto:dsvellal@philips.com> to do a POC to see if AI platform can create the output for review.
We are using the recent Temperature rise issue for the POC.

We need to provide raw data for the POC. For now, we are not connecting to the actual data sources. Datt’s team is  working towards building a local RAG that can assimilate data from different documents (the ones that we upload), and we can have an AI model run through semantic questions Here is the sharepoint where we are uploading the raw data for Datta’s team to use Ultrasound Medical and Clinical - Documents - Temperature Rise - All Documents<https://share.philips.com/sites/UltrasoundDataandResearch/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FUltrasoundDataandResearch%2FShared%20Documents%2FQuantitative%20Patient%20Risk%2FAWS%20AI%20POC%2FTemperature%20Rise&viewid=4291ffa4%2D5bc1%2D4980%2Dbd1f%2D1d862fc55768>


@Donlon, John<mailto:john.donlon@philips.com> Please upload the VM13.0 SRS, RMM from VM13.0. Any other guideline like IEC used for our analysis . I have uploaded one Anup pointed me to Recommended Maximum Scanning Times for Displayed Thermal Index (TI) Values<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.aium.org%2Fresources%2Fofficial-statements%2Fview%2Frecommended-maximum-scanning-times-for-displayed-thermal-index-(ti)-values%23%3A~%3Atext%3D*Dwell%2520time%2520-%2520The%2520total%2520time%2Cbeam%2520during%2520an%2520ultrasound%2520examination.&data=05%7C02%7Cdsvellal%40philips.com%7C32796e1b65f2478aeea408dea8bb6926%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C639133720036341848%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=y7ChTQtca6uH2JPNnsaXizTwpF%2BRpagNotJILnv7SR0%3D&reserved=0>



@Lee, Jewel<mailto:Jewel.Lee@philips.com> Please provide the Complaints data in the format discussed in the call



@Yoo, Andrew<mailto:andrew.yoo@philips.com> : Any Medical Literature source? FDA benefit risk guidelines?



@Dianis, Scott<mailto:scott.dianis@philips.com> : I have uploaded the IIA Request submission document capturing the workflow. Any other raw source that we can provide Datta?



@Brown, Cynthia<mailto:cynthia.brown@philips.com> : How can we provide the Vertica Data source subset for this analysis? Export the relevant data into Excel?


We expect the AI generated output document should look like D002425196RevA, PD47114– Evaluation of X7-2 Transducer Temperature Exceeds IEC Limit.docx<https://share.philips.com/:w:/r/sites/UltrasoundDataandResearch/Shared%20Documents/Quantitative%20Patient%20Risk/AWS%20AI%20POC/Temperature%20Rise/D002425196RevA,%20PD47114%E2%80%93%20Evaluation%20of%20%20X7-2%20Transducer%20Temperature%20Exceeds%20IEC%20Limit.docx?d=w775fa7b179b444f4aac5324f927f368c&csf=1&web=1&e=ON4Shm>





Regards,

Kaveri










________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.

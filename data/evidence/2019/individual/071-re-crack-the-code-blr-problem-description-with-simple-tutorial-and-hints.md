# Evidence: RE: Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints

## Source
- **File:** `RE  Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints.msg`
- **Date:** 2019-08-21
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** General / Other

## Email Metadata
- **From:** "Benchetrit, Uri" <Uri.Benchetrit@philips.com>
- **To:** "Vellal; Dattatreya" <dsvellal@philips.com>; "Mitchell; Elaine"	<elaine.mitchell@philips.com>; "Hansen; Rodolfo"	<rodolfo.hansen@philips.com>; "Terol; David" <david.terol@philips.com>;	"Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Malli; Rani"	<rani.malli@philips.com>; "Williams; Simao" <simao.williams@philips.com>
- **Date:** 2019-08-21T01:46:07-04:00
- **Thread depth:** 7
- **Is reply:** True
- **Attachments:** 2
  - `RegEx Crossword Puzzle - Example, Problem, and Hints.pdf` (application/octet-stream, 166926 bytes)
  - `image001.png` (image/png, 34976 bytes)

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Involvement type:** Direct recipient — explicitly mentioned/praised

## Key Quotes
> To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Mitchell; Elaine"	<elaine.mitchell@philips.com>; "Hansen; Rodolfo"	<rodolfo.hansen@philips.com>; "Terol; David" <david.terol@philips.com>;	"Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Malli; Rani"	<rani.malli@philips.com>; "Williams; Simao" <simao.williams@philips.com>

> 1.      Based on the 'false positive' detected by Datta, two changes were made to the 'Problem RegEx patterns' of version 1.0 in order to block a false-positive match by the string "Add code..." (instead of the expected string "Bad code..."):

> 2.      Through this exercise Datta has learned enough about RegEx to be able to review patterns.

> Thanks Datta.

> To: Vellal, Dattatreya <dsvellal@philips.com>; Mitchell, Elaine <elaine.mitchell@philips.com>; Hansen, Rodolfo <rodolfo.hansen@philips.com>; Terol, David <david.terol@philips.com>; Jagadeesan, Sundaresan <sundaresan.j@philips.com>; Malli, Rani <rani.malli@philips.com>; Williams, Simao <simao.williams@philips.com>

## Full Email Content

```
Subject: RE: Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints
From: "Benchetrit, Uri" <Uri.Benchetrit@philips.com>
To: "Vellal; Dattatreya" <dsvellal@philips.com>; "Mitchell; Elaine"	<elaine.mitchell@philips.com>; "Hansen; Rodolfo"	<rodolfo.hansen@philips.com>; "Terol; David" <david.terol@philips.com>;	"Jagadeesan; Sundaresan" <sundaresan.j@philips.com>; "Malli; Rani"	<rani.malli@philips.com>; "Williams; Simao" <simao.williams@philips.com>
Date: 2019-08-21T01:46:07-04:00

--- Latest Reply ---
An updated subject document is attached. Please ignore previous versions.

The main changes are:

1.      Based on the 'false positive' detected by Datta, two changes were made to the 'Problem RegEx patterns' of version 1.0 in order to block a false-positive match by the string "Add code..." (instead of the expected string "Bad code..."):

a.      First raw pattern changed from `.[abcdeo\s]*` to `[^CDAQ][abcdeo\s]*`

b.      Second column pattern changed from `[a-z](.)\1o` to `[a-c](.)\1o`

2.      Removed Hint #3 about the result being a clean code quote by Robert Martin. A simple Google search with partial result will reveal the complete solution.

The first change proves two important things:

1.      It supports the claim that RegEx patterns are hard to test for “false-positives”. Meaning that it is difficult to verify that an unintended string will not be matched with a given RegEx pattern.

2.      Through this exercise Datta has learned enough about RegEx to be able to review patterns.

Thanks Datta.

- Uri.

--- Previous Message (1) ---
Sent: Tuesday, August 20, 2019 10:34 PM
To: Vellal, Dattatreya <dsvellal@philips.com>; Mitchell, Elaine <elaine.mitchell@philips.com>; Hansen, Rodolfo <rodolfo.hansen@philips.com>; Terol, David <david.terol@philips.com>; Jagadeesan, Sundaresan <sundaresan.j@philips.com>; Malli, Rani <rani.malli@philips.com>; Williams, Simao <simao.williams@philips.com>
Subject: RE: Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints

Please use the attached PDF file instead.

- Uri.

--- Previous Message (2) ---
Sent: Tuesday, August 20, 2019 2:06 PM
To: Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>; Mitchell, Elaine <elaine.mitchell@philips.com<mailto:elaine.mitchell@philips.com>>; Hansen, Rodolfo <rodolfo.hansen@philips.com<mailto:rodolfo.hansen@philips.com>>; Terol, David <david.terol@philips.com<mailto:david.terol@philips.com>>; Jagadeesan, Sundaresan <sundaresan.j@philips.com<mailto:sundaresan.j@philips.com>>; Malli, Rani <rani.malli@philips.com<mailto:rani.malli@philips.com>>; Williams, Simao <simao.williams@philips.com<mailto:simao.williams@philips.com>>
Subject: RE: Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints

Please check that the attached zipped version is working better.

--- Previous Message (3) ---
Sent: Tuesday, August 20, 2019 2:02 PM
To: Benchetrit, Uri <Uri.Benchetrit@philips.com<mailto:Uri.Benchetrit@philips.com>>; Mitchell, Elaine <elaine.mitchell@philips.com<mailto:elaine.mitchell@philips.com>>; Hansen, Rodolfo <rodolfo.hansen@philips.com<mailto:rodolfo.hansen@philips.com>>; Terol, David <david.terol@philips.com<mailto:david.terol@philips.com>>; Jagadeesan, Sundaresan <sundaresan.j@philips.com<mailto:sundaresan.j@philips.com>>; Malli, Rani <rani.malli@philips.com<mailto:rani.malli@philips.com>>; Williams, Simao <simao.williams@philips.com<mailto:simao.williams@philips.com>>
Subject: RE: Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints

Hi Uri – the images are getting omitted. Are they locally embedded into a file location of your machine?

If yes, could you please consider creating a PDF so that the images get embedded into the document?

[cid:image001.png@01D557FC.DD8E4000]

--- Previous Message (4) ---
Datta

--- Previous Message (5) ---
Sent: Tuesday, August 20, 2019 4:24 PM
To: Mitchell, Elaine <elaine.mitchell@philips.com<mailto:elaine.mitchell@philips.com>>; Vellal, Dattatreya <dsvellal@philips.com<mailto:dsvellal@philips.com>>; Hansen, Rodolfo <rodolfo.hansen@philips.com<mailto:rodolfo.hansen@philips.com>>; Terol, David <david.terol@philips.com<mailto:david.terol@philips.com>>; Jagadeesan, Sundaresan <sundaresan.j@philips.com<mailto:sundaresan.j@philips.com>>; Malli, Rani <rani.malli@philips.com<mailto:rani.malli@philips.com>>; Williams, Simao <simao.williams@philips.com<mailto:simao.williams@philips.com>>
Subject: Crack-the-Code BLR - Problem Description with Simple Tutorial and Hints

Hi all,

Please review the attached document. As per our decision it includes an example, problem with some pre-filled letters, hints, instructions for how to play, and a disclaimer on not to abuse RegEx.

@Datta Please pass it to Brijesh and ask him to allocate uninterruptable time slot and measure how long it took him to solve the puzzle. Additional comments from him are welcome.
@Elaine I will send you the source for Eng

[... truncated, full content in database ...]
```
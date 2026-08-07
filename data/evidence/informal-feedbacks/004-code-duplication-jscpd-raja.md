# Evidence: JSCPD Code Duplication Tool — Raja Rajeshwar's Experience & Appreciation

## Source
- **File:** `20191003_CodeDuplication_JSCPD_Raja.PNG`
- **Date:** 2019-10-03
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer — Software Center of Excellence group)
- **Category:** Informal Feedback

## Metadata
- **From:** Raja, Rajeshwar (primary post); Vellal, Dattatreya (reply); Jagadeesan, Sundaresan (reply)
- **To/About:** Datta Vellal — directly credited for introducing JSCPD tool, setting up CodeScene, and pair-programming to remove ~200 lines of duplicate code
- **Context:** Raja Rajeshwar shared his experience of using the JSCPD (JavaScript Copy Paste Detector) tool after Datta helped him set it up. They sat together, analyzed a 15kloc codebase, and removed ~200 lines of duplicate code in one hour.
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** You, Schroeder, Zephan, Jagadeesan, Sundaresan, and Viswanath, Sreekanth reacted
- **Seen by:** 163

## Datta's Involvement
- **Role at time:** Software Center of Excellence (SWCoE) team member / Principal Engineer
- **Involvement type:** Direct recipient — praised for hands-on mentoring; personally sat with Raja to set up and use the tool; provided the installation guide; suggested the JSCPD tool for reducing technical debt

## Key Quotes
> "I was working on setting up quality gates for a project and I approached Datta for help, he supported me in setting up CodeScene and suggested jscpd tool for reducing technical debt (code duplication)." — Raja, Rajeshwar

> "Datta and I sat together and analyzed the code base with jscpd tool. It took surprisingly less time to setup the tool, for first time use (~15min) and analysis took 10 seconds for 15kloc code base. The report is easy to ready and for the next one hour we removed code duplications." — Raja, Rajeshwar

> "I was a rewarding experience. I was able to remove ~200 lines of duplicate code in a short time. Thanks to @SW_COE and Vellal, Dattatreya." — Raja, Rajeshwar

> "Thank you Raja, Rajeshwar for piloting this. Very rewarding to see you commit the changes so fast! Very commendable!" — Vellal, Dattatreya

> "Thanks Raja and Datta. This work will motivate others to commit their code as well and help in reducing the code base Size" — Jagadeesan, Sundaresan

## Full Content
```
Software Center of Excellence (SW_CoE)

Raja, Rajeshwar – October 3, 2019 at 09:41 AM

JavaScript Copy Paste Detector Tool & My Experience

I was working on setting up quality gates for a project and I approached Datta for help, he supported me in setting up CodeScene and suggested jscpd tool for reducing technical debt (code duplication).

Datta and I sat together and analyzed the code base with jscpd tool. It took surprisingly less time to setup the tool, for first time use (~15min) and analysis took 10 seconds for 15kloc code base. The report is easy to ready and for the next one hour we removed code duplications.

The installation guide for the tool is available at
https://docs.philips.com/pp/r/personal/dsvellal_philips_com/_layouts/15/guestaccess.aspx?e=M6ZCdK&share=EeuxbFsCbgRBpZ_bYeisCm4B3nAeitq7cuTZZGq9-E4l-g

I was a rewarding experience. I was able to remove ~200 lines of duplicate code in a short time. Thanks to @SW_COE and Vellal, Dattatreya.

Source Archive: https://gitlab.ta.philips.com/Rajeshwar.Raja/simulator
Commit ID: ad22ced7

cc: Vellal, Dattatreya and Viswanath, Sreekanth

[Attached files: jscpd-report-after, jscpd-report-before - Software Center of Excellence (SW_CoE) > Files]
[Links: https://docs.philips.com/pp/r/personal/dsvellal_philips_com/_layouts/15/guestaccess.aspx?... and https://gitlab.ta.philips.com/Rajeshwar.Raja/simulator]

UNLIKE  REPLY  SHARE
You, Schroeder, Zephan, Jagadeesan, Sundaresan, and Viswanath, Sreekanth reacted to this
Seen by 163

---

Vellal, Dattatreya – October 4, 2019 at 10:22 AM from Android
Thank you Raja, Rajeshwar for piloting this. Very rewarding to see you commit the changes so fast! Very commendable!

cc: Raja, Rajeshwar

LIKE  REPLY  SHARE  EDIT

---

Jagadeesan, Sundaresan – October 4, 2019 at 04:55 PM
Thanks Raja and Datta. This work will motivate others to commit their code as well and help in reducing the code base Size

LIKE  REPLY  SHARE
```

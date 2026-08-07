# Evidence: Quality at Desk — PSI2M/ASP Team Implements Quality Gates with SWCoE

## Source
- **File:** `20200625_QualityAtDesk_PSI2M.PNG`
- **Date:** 2020-06-25
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer - Technology & Engineering)
- **Category:** Informal Feedback

## Metadata
- **From:** Satheesan, Sajith
- **To/About:** Vellal, Dattatreya and Hu, Aravind (explicitly thanked)
- **Context:** The ASP team shared their journey of implementing Quality at Desk with SWCoE support since the beginning of the year. Sajith explicitly gave "a big thanks" to Datta and Aravind for supporting the initiative. The team implemented TICS quality gates, Fortify, BlackDuck, and CI/CD code quality gates in Jenkins pipelines.
- **Platform:** Yammer (Technology & Engineering group)
- **Reactions:** Nair P, Manoj reacted
- **cc:** Vellal, Dattatreya, Hu, Aravind, and Suman, Binod

## Datta's Involvement
- **Role at time:** Senior Software Engineer / SW CoE
- **Involvement type:** Direct recipient — explicitly thanked for supporting the initiative

## Key Quotes
> "A big thanks to Vellal, Dattatreya and Hu, Aravind from SwCoE team for supporting us in this initiative."

> "The ASP team has been on a continous journey and engagement with the SwCOE team since begining of the year. The focus has been on implementation of Quality @ Desk initiative and we are begining to see a cultural change within the team and eagerness to explore more opportunities to bring in further improvements."

> "First time implemented Gates (Compiler Warning, Cyclomatic complexity and code coverage) in Jenkins Pipeline."

> "In May-June, team had two training session with SwCOE team and were able to implement Two Factory Gates. (Local machine as well in Jenkins pipeline)."

## Full Content
```
Technology & Engineering

Satheesan, Sajith — June 25 at 10:11 AM

The ASP team has been on a continous journey and engagement with the SwCOE team since begining of the year. The focus has been on implementation of Quality @ Desk initiative and we are begining to see a cultural change within the team and eagerness to explore more opportunities to bring in further improvements. Sharing below the current wow being implemented in the team, for the benefit of the whole group.

A big thanks to Vellal, Dattatreya and Hu, Aravind from SwCoE team for supporting us in this initiative.

Thanks to Suman, Binod for providing the below details:

Developer mandatory action for any code commit:
1. Installed IDE Plugin for TICS.
2. Installed local way to measure TICS score.
3. TICS score cannot be less than current score.
4. Attach TICS report during code review.
5. Implemented Local Gate that make build fail if TICS score is below the targets.
6. Developer gives equal importance for code quality.
7. Developer has fair idea about Fortify and BlacDuck.
8. Each developer gets chance to fix Fortify and Black duck issue.

Improved CI/CD for Code Quality:
1. First time implemented Gates (Compiler Warning, Cyclomatic complexity and code coverage) in Jenkins Pipeline.
2. Planning to implement Fortify also as Gate

In May-June, team had two training session with SwCOE team and were able to implement Two Factory Gates. (Local machine as well in Jenkins pipeline).

This below link is maintained by SWCoE and it is very useful to implement local build Gates. ASP team has implemented local build gate using this below link.

https://gitlab.ta.philips.com/swcoe/javagradlegating/-/tree/master

cc: Vellal, Dattatreya, Hu, Aravind, and Suman, Binod

Nair P, Manoj reacted to this
Seen by 51

---

Satheesan, Sajith — June 25 at 10:11 AM
added Vellal, Dattatreya and Hu, Aravind to the conversation.
```

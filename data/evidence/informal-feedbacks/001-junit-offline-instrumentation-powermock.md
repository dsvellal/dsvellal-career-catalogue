# Evidence: JaCoCo Offline Instrumentation with PowerMock — Appreciation from Meghana H M

## Source
- **File:** `20190820_JUnit_OfflineInstrumentation_Powermock.PNG`
- **Date:** 2019-08-20
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer — Software Center of Excellence group)
- **Category:** Informal Feedback

## Metadata
- **From:** H M, Meghana
- **To/About:** Vellal, Dattatreya (Datta)
- **Context:** Meghana shared a solution for JaCoCo + PowerMock code coverage issue, crediting Datta's article on JaCoCo offline instrumentation shared during a Unit Test Workshop conducted by the SWCoE team
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** You, Nuji, Shivaprashanth, Hansen, Rodolfo, and Priyanka, Palla reacted
- **Seen by:** 184

## Datta's Involvement
- **Role at time:** Software Center of Excellence (SWCoE) team member / Principal Engineer
- **Involvement type:** Direct recipient — praised for excellent article on JaCoCo offline instrumentation

## Key Quotes
> "Thanks a lot for the excellent article on **JaCoCo offline instrumentation** shared by Vellal, Dattatreya in **Unit Test Workshop** conducted by SWCoE team."

> "Please refer attached file for JaCoCo configuration and get the expected **code coverage numbers**!!"

## Full Content
```
Software Center of Excellence (SW_CoE)

H M, Meghana – August 20, 2019 at 02:43 PM

We make heavy use of PowerMock in many of our JUnit tests. However, For the code that is unit tested with powermock shows 0% coverage by JaCoCo.
JaCoCo instruments the class to collect code coverage information. JaCoCo supports two ways class instrumentation:
- On-the-fly with using Java Agent
- Offline when classes are prepared during build phase

Right now there is NO WAY TO USE PowerMock with JaCoCo On-the-fly instrumentation
JaCoCo and powermock works well with offline instrumentation.
Thanks a lot for the excellent article on JaCoCo offline instrumentation shared by Vellal, Dattatreya in Unit Test Workshop conducted by SWCoE team.

Please refer attached file for JaCoCo configuration and get the expected code coverage numbers!!

cc: Vellal, Dattatreya, Kumar, Nataraj, Kumar, Prashant, Nuji, Shivaprashanth, and S C, Shiva Kumar

[Attached file: pom - Software Center of Excellence (SW_CoE) > Files]

UNLIKE  REPLY  SHARE
You, Nuji, Shivaprashanth, Hansen, Rodolfo, and Priyanka, Palla reacted to this
Seen by 184
```

# Evidence: Quality at Desk — PHDSI Test Automation Code Quality Initiative

## Source
- **File:** `20200604_QualityAtDesk_PHDSI_Testing.PNG`
- **Date:** 2020-06-04
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer - Software Center of Excellence SW_CoE)
- **Category:** Informal Feedback

## Metadata
- **From:** Jagadeesan, Dinakaran
- **To/About:** Vellal, Dattatreya (credited for guidance in code quality approaches)
- **Context:** PHDSI team shared their success story of treating test automation code on par with product code. Datta was explicitly thanked for guidance in code quality approaches. The initiative yielded near zero script errors, modularity, and BDD improvements. Seen by 218 people with 14+ reactions.
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** You (Datta), T N, Guru Prakash, Potula, Anilkumar, and 14 others reacted
- **Shares:** 1 share

## Datta's Involvement
- **Role at time:** Senior Software Engineer / SW CoE
- **Involvement type:** Direct recipient — praised for guidance in code quality approaches

## Key Quotes
> "Prasad, Sudeep, Vellal, Dattatreya, Krishnan K, Brijesh for their guidance in code quality approaches"

> "We @ PHDSI took an initiative to invest in test automation code-quality, which is yielding us great results:
> - Modularity resulting in low entry barrier for test engineers
> - Automate by default attitude
> - Gating test automation quality @ developer desk - Improves efficiency in test automation
> - Achieving near zero script errors"

## Full Content
```
Software Center of Excellence (SW_CoE)

Jagadeesan, Dinakaran — June 4 at 10:59 AM

We @ PHDSI took an initiative to invest in test automation code-quality, which is yielding us great results:
- Modularity resulting in low entry barrier for test engineers
- Automate by default attitude
- Gating test automation quality @ developer desk - Improves efficiency in test automation
- Achieving near zero script errors

R.Nair, Rajeev for driving the initiative and training the team on code-quality approaches, which transformed the mindset of team members
S K, Pradeep Kumar for consistently supporting test automation initiatives and investment
Prasad, Sudeep, Vellal, Dattatreya, Krishnan K, Brijesh for their guidance in code quality approaches
Williams, Simao, Malli, Rani, Jagadeesan, Sundaresan
See Attached picture for details:

cc: Vellal, Dattatreya, R.Nair, Rajeev, S K, Pradeep Kumar, Prasad, Sudeep, Krishnan K, Brijesh, Williams, Simao, Malli, Rani, and Jagadeesan, Sundaresan

[Attached image: "Treat Test automation code on par with Product code"]

Before → After comparison table:
| Before | After |
|--------|-------|
| Mind set that Test automation is just scripting.... | Test Automation is as serious as Product code development |
| Development technical terms were considered as jargons and some thing which is very complex | Test Engineers now not afraid of technical terms like cyclomatic complexity, dead codes etc. |
| BDD single step definitions had multiple functionality asserts | BDD step definitions' complexity reduced and there by now we have the minute level of user action as single steps |
| No docstrings, large functions with multiple asserts and condition checks | Highly readable code |
| Single layer design complexity | Code modularity effectively segregated class and function [Modularized backend api's, hardware api's, framework api's and test api's] which helped us in fast debugging with minimal effort for problems analysis and fix |
| Script errors were very common during test development and provides hacks which in-turns failed other testcases | Script errors reduced and caught in earlier stages [Developer box, Pull request Lint job gate, code walkthrough meetings] |
| Empty codes were common | Dead code/empty codes are detected in Developer Box and doesn't allow developer to commit code to mainline without fixing due to coding standard gate deployment |

Tools used: Pylint, PC (PyCharm)

You, T N, Guru Prakash, Potula, Anilkumar, and 14 others reacted to this
Seen by 218
1 share

---

Veldhuijzen van Zanten, Julian — June 5 at 01:34 PM
Bedi, Shefali Interesting?
cc: Bedi, Shefali

---

Bedi, Shefali in reply to Veldhuijzen van Zanten, Julian — June 5 at 02:21 PM
Thanks for sharing, indeed i have been eyeing on test automation if we can prioritise effort in smaller chunks we can start looking at efficient option now with test factory on board. Last i checked with Microsoft, they did not offer it in the SP package we have currently.
```

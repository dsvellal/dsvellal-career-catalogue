# Evidence: Viva Engage — Community Member Credits Datta's Unit Test Workshop (Aug 2019, Seen by 184)

## Source
- **Platform:** Viva Engage (IEN Software Engineering Excellence community)
- **Date:** 2019-08-20 (original post) / 2019-08-22 (Datta's reply)
- **Ingested:** 2026-08-05
- **Channel:** internal_snapshot
- **Category:** Community Credit / Workshop Impact / Knowledge Sharing
- **Image:** [viva-engage-jacoco-unit-test-workshop-credit-2019.jpg](../../images/2019/viva-engage-jacoco-unit-test-workshop-credit-2019.jpg)

## References
- **Type:** Internal (Philips Viva Engage — requires SSO)
- **Captured:** 2026-08-05 (from authenticated full-page screenshot)
- **Status:** Captured (screenshot preserved)
- **Seen by:** 184

## Thread Details

### Original Post
- **Author:** H M, Meghana
- **Date:** Aug 20, 2019 · @5 (tagged 5 people)
- **Community:** IEN Software Engineering Excellence
- **Seen by:** 184
- **Reactions:** "You and 3 others" (4 total, Datta liked it)

### Post Content (verbatim)
> We make heavy use of **PowerMock** in many of our **JUnit** tests. However, For the code that is unit tested with powermock shows 0% coverage by JaCoCo.
> JaCoCo instruments the class to collect code coverage information. JaCoCo supports two ways class instrumentation:
> - On-the-fly with using Java Agent
> - Offline when classes are prepared during build phase
>
> Right now there is **NO WAY TO USE** PowerMock with JaCoCo On-the-fly instrumentation
> JaCoCo and powermock works well with **offline instrumentation**.
> Thanks a lot for the excellent article on **JaCoCo offline instrumentation** shared by **Subramanya Vellal, Dattatreya** in **Unit Test Workshop** conducted by **SWCoE** team.
>
> Please refer attached file for JaCoCo configuration and get the expected **code coverage** numbers!!

**Attachment:** `pom.xml` (Maven configuration for JaCoCo offline instrumentation)

### Comment: Hansen, Rodolfo (Aug 20, 2019)
> "Doing bytecode manipulation (either online or offline) for Mock Generation AND Coverage Instrumentation means you are increasingly far from the actual bytecode you want to test...
>
> Is there any particular reason you are using PowerMock?
>
> Do you now have checks in place to confirm you are not shipping instrumented binaries?"

(1 reaction)

### Comment: Subramanya Vellal, Dattatreya — **Community expert** badge (Aug 22, 2019)
> "Thank you H M, Meghana for publishing this. This is really helpful. BTW, do you know if you are shipping test-code with the build? Or is it only the source code getting bundled into binaries, in the production build?"
> cc: Hansen, Rodolfo

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Badge:** **Community expert** (official Viva Engage designation)
- **Involvement type:** Credited for workshop knowledge that solved a real team problem

## Key Context

### What This Proves
1. **Workshop content applied in practice** — Meghana took what she learned in Datta's Unit Test Workshop and applied it to solve a real problem (PowerMock + JaCoCo 0% coverage)
2. **Shared pom.xml** — the solution was actionable enough to package as a Maven config file
3. **"Community expert" badge** — Datta has official recognition on the platform
4. **Rodolfo Hansen engaged** — same person from refactoring discussion and later co-presenter
5. **Datta asks deeper questions** — "are you shipping test-code with the build?" — demonstrates production-mindedness

### Visible Sidebar Communities (from screenshot)
Shows Datta's Viva Engage profile with favorited communities:
- Innovation & Design (2)
- AI Uncovered (12)
- ChatGPT Community (20+)
- **IEN Software Engineering Excellence** (3)
- I&D Research (5)
- I&D Data and AI Engineering (2)
- Patient Safety and Quality team (20+)
- Claude Community (20+)
- Devin users (2)
- I&D Innovation Engineering (IEN) (6)
- Kairos - Philips AI Platform (3)
- Microsoft 365 Copilot (20+)
- All Things Security (15)
- Ultrasound R&D (3)

## Key Quotes

> **"Thanks a lot for the excellent article on JaCoCo offline instrumentation shared by Subramanya Vellal, Dattatreya in Unit Test Workshop conducted by SWCoE team."**

> (Datta, tagged as **Community expert**): "Thank you H M, Meghana for publishing this. This is really helpful."

## Leadership Indicators
- **"Community expert"** — official badge on the platform
- Workshop content directly solved a real engineering problem
- Content was so valuable that a participant published it as a community resource
- Engages with follow-up questions about production safety
- Member of 15+ communities spanning AI, security, R&D, and quality

## Skills Demonstrated
- JaCoCo (code coverage instrumentation)
- PowerMock (JUnit testing)
- Maven configuration (pom.xml)
- Offline vs On-the-fly instrumentation
- Unit testing best practices
- Java testing ecosystem
- Production build safety

## Impact Statement
This is **the ideal evidence of workshop impact**: a participant (Meghana) attended Datta's Unit Test Workshop, learned about JaCoCo offline instrumentation, applied it to solve a real team problem (0% code coverage with PowerMock), then published the solution back to the 184-person community — explicitly crediting Datta's workshop. The "Community expert" badge on Datta's reply confirms his recognized status in the platform.

Additionally, the sidebar showing Datta's community memberships reveals his breadth of engagement: from AI and Claude to Patient Safety, Security, and Ultrasound R&D.

## Cross-References
- [[workshops-technical-sessions]] — Unit Testing workshops documented in email evidence
- [[viva-engage-refactoring-discussion]] — Same thread participants (Rodolfo Hansen)
- [[pair-programming-quality-at-desk]] — JaCoCo as part of Quality@Desk
- Email: "1/2 day Unit testing workshop on 4th July - 9:30 to 12:30" (2019)
- Session feedback: "Unit Testing Workshop Feedback" (20 responses in data)

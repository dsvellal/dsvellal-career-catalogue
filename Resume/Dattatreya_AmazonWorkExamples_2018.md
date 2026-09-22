# Dattatreya AmazonWorkExamples 2018

> Converted from `Dattatreya_AmazonWorkExamples_2018.docx`


## Deliver results (Design & Coding)

- Successfully delivered impactful projects, in time, which required design, stake-holder management & coding – SVA OneAccountPerCustomer check, RiskProfileEvaluation (RiPE) of Fortress, XML Feed Migration & QueryGeneration & backfill tool for Automated Catalog System to name a few. While delivering these, is able to evaluate multiple options, call out pros and cons & take the path most tech-relevant & stake-holder-friendly. Proactively calls out any tech-debt incurred & articulates a step-by-step plan of mitigating it in phases. Also has a keen eye for scaling, integration, fault-tolerance, acceptance criteria as NFRs & incorporates them in design.
- On multiple occasions, has automated manual tasks & achieved results. Eg: Automated re-opening of 5297 closed herd workflows, automated ASIN pulls from RetailCatalogService and backfilled close to 1.9 billion ASINS across 12 different marketplaces and two different categories into EDX.
- Supported multiple client onboarding via clearly articulated SOPs & on-boarding docs, which resulted in 29 successful client migration for the XML Feed Migration project, and 6 successful client migration for the RiPE project, with minimal SDE efforts.

## Earn trust (Away team model projects)

- Is a part of IndiaPayments TRMS-Away team and has worked on 5 key away-team projects, significant ones being Amazon India PPI Launch (StoredValueAccount/AmazonPay), RiskDocument creation & EvaluateRisk API of RiPE, VariableComparisonTool enhancements.
- Proactively reaches out to stakeholders to understand possible paths and is meticulous in documenting requirements & scope of the projects. Maintains a wiki of MoMs had with stakeholders, follows up consistently to ensure that action items are met, maintains a task-list with start and end dates which clearly call out dependencies, order of execution, owner & completion artefacts. Is extremely transparent in keeping the stakeholders informed about the status, risks, mitigation plans and shows high ownership in taking projects to conclusion.

## Bias for action

- On a repeated basis (AbuseCOPS ruleset migration, QMS enablement for India), has shown the ability to take quick decisions & deliver in time to unblock dependencies.
- On multiple occasions (0128828360, 0121783939, 0128972298) was called to firefight critical scenarios and has successfully handled them with no intervention required.

## Dive deep

- Identifies optimization opportunities & incorporates them to ensure the best software and hardware optimisations are achieved. Eg: Reduced gc CPU consumption from 18% to 2.3% by incorporating profiler, identified hardware optimization opportunities after running FLO and saved $12k per year on APS & AbuseCOPS fleets, saved $22k in hardware by replacing legacy EC2 hosts with new generation EC2 hosts.
- Can do process dive-deeps to understand gaps and is able to come up with suggestions to improve them. Eg: Proposed scaling-for-development process to improve task completion rate in sprint, and his team has improved from 60% task completion rate to 85% task completion rate. Proposed amends to TRMS interview processes & came up with a standardized set of tech-questions that are currently being used in TRMS interviews & weekend drives.

## Hire & Develop the best

- Has created on-boarding guides (One for ACS team, One for INPayment-TRMS Away team) & on-call (INPayment-TRMS) wiki’s that’ll help the team.
- Is an active contributor towards the interview processes in his organization (68 interviews in 18 months).
- Is one among 3 scrum facilitators in India, recognized by EngineeringExcellence team & has facilitated 3 scrum workshops for different teams in India. Is also one among 3 agile product ownership workshop facilitators in India, recognized by EngineeringExcellence team & has facilitated 1 agile product ownership workshop for teams in India.
- Has mentored interns, juniors, and served as a tech-reviewer for 3 promo docs of L4 to L5 promotions in his current org.

## Vocally self-critical (sought out improvements)

- RDPS project implementation was called out as one of the projects that did not reach its completion. Multiple factors contributed towards this – Exploratory nature of the project, with no clients or end goal. The expectation was not set at the early stage of the project, which resulted in extensive dive-deep and no conclusive results. However, this does not seem to be a pattern, since there are counter examples of successful away team project deliveries. Has sought out help in clearly defining expectations on the projects being worked on, to ensure that correct success criteria are met & project gets delivered.
- Bias for action on ticket (eg: 0128263358) – This ticket has seen multiple back-and-forth, ultimately resulting in a code change done by dattatrv@. While Datta has acknowledged that this was an issue, he also confirmed that during multiple back-and-forth, he consulted senior team members about the action being taken, and they seem to agree on the approach. Also, this does not seem like a recurrent issue because after this ticket, he has independently solved 43 tickets and was also appreciated for the bias-for-action taken in solving tickets during his on-calls. Has sought out help in context setting of existing services to ensure that the right amount of dive-deep can be done to ensure correct fixes/design is addressed.

## Appendix


Deliver results (Design & Coding)

- RiskDocument for EvaluateRisk API of Fortress
- Context: Was challenged with the task of creating a generic document that would act as context & a pay-load carrier for clients who on-boarded to Fortress (platform for fraud/abuse detection), that would remain generic across multiple clients & different use-cases to be supported on Fortress.
- Delivered: Designed & implemented RiskDocument. The design was approved by our SDE-3, the principal & the samurai group.
- Artefacts: Use-case, Prototype, HLD, RiskDocumentModelCode, ClientHandlerCode, Integration test
- Impact:
- Launched the first version of RiPE API on Fortress for CS-Tech use-case using RiskDocument.
- Fortress’s EvaluateRisk API currently supports 6 clients, and the structure of RiskDocument hasn’t changed since its launch.
- Tool for taking bulk action on StoredValueAccount (SVA aka AmazonPay) Investigations
- Context: Just after the lauch of AmazonPay in India, in July 2017, TRMS investigators were understaffed to handle the total no. of AmazonPay accounts that needed to be investigated. This lead to a backlog of 5927 investigations that couldn’t be attended to & AmazonPay account creation for these accounts were blocked because the SLA for investigation had passed & investigators could not take action on them.
- Delivered: I designed & implemented a command-line tool which would take the taskId’s of such investigations & open them for investigators to take necessary actions. The implementation was done in record time to minimize the impact for the customers.
- Artefacts: Use-case & design wiki, Code
- Impact:
- The tool successfully handled the 5927 tasks were blocked & the project was reported as successfully delivered, in-time, in our weekly report.
- The tool was so generically written that it was re-used & extended to support another use-case.
- XML Feed Migration by using a consistent XML to Json Parser
- Context: The ion generated from the XML feeds are inconsistent in nature, which prevents it from indexing in Elasticsearch and writing reliable transformation code using aliasPath.
- Delivered: Designed, coded and introduced process to self-service migration of inconsistent ion generated via XML feed, to consistent ion generation for the same XML feed.
- Artefacts: XML Feed Migration Strategy, Bulk Migrator Tool Code, Self-service wiki to migrate feed without SDE involvement
- Impact: 29 feed providers were migrated using the self-service tool without SDE involvement.
- RCSQueryGeneration Tool
- Context: To generate value metrics query results across 12 market places, to identify how many of the asins created were resultant of automated feed parsing.
- Delivered: Designed & wrote a tool that would query RCS to obtain the value metrics query results, process them and upload them into EDX warehouse. Created DJS jobs that would run on a daily basis to do this, and helped in back-filling the data from 1970 till today.
- Artefacts: QueryGenerationTool, Backfill jobs, DJS Job1, DJS Job2
- Impact:
- Backfill jobs processed: 930 Million vendor contribution response, 1.1 Billion create by date responses.
- DJS job continuously processes approx: 30000 asins per day

Earn Trust (Away-team model projects)

- SVA OAOC Launch: Conceptualized and lead the OneAccountOneCustomer fraud use-case for the launch of AmazonPay in March 2017 (family & friends launch), followed by general availability in July 2017. I was handling end-end processes of the project including requirements gathering, design, stake-holder communications, coding 1 & coding 2, on-boarding. This was appreciated by directors of TRMS.
- VariableComparisonTool Enhancement: Was challenged to come up with a way to improve the reporting details of VariableComparisonTool that reported variable mismatches between FRS (legacy service) and Fortress (replacement service) for SVA use-case. I made generic code changes (GLS filtering,  variable filtering, generate sample OrderIds, control decimal point precession) to the tool to introduce options that would custom generate reports based on configurations. This resulted in SDE effort reduction by 60%.
- S-Team goal: As a part of S-Team goal, I contributed towards resolving a major SIM's that validated mismatch of variables evaluated by FRS and Fortress, in Inline evaluation. Wiki link
- RiPE API: Worked with Fortress team to facilitate the initial launch of RiPE API for CS-Tech use-case. This included presenting RiPE to our director Anand (anandva@) and developing and delivering the components required for addressing the CS-Tech use-case. RiPE Overview, Fortress SIL Code Changes 1 & 2, Fortress code changes.
- FDPS Client Analysis: Analyzed who are our clients calling FDPS and created a follow-up wiki page to help see if these clients still have dependencies on FDPS. The intent is to see how we can support FDPS hosting RiskDocument, instead of FraudDocument, also to analyze if we have a chance of gracefully deprecating FDPS and move to a new data-store (RDPS) if there is a need.

Bias-for-action

- AbuseCOPS stage-3 to stage-1 COD suppression rule migration: Identified the root cause of COD suppression slippages during flash-sales & proposed a solution to migrate suppression rules from stage-3 to stage-1 of AbuseCOPS, to ensure that evaluation results were computed within 250 milliseconds. Made necessary code changes.
- QMS enablement for IN SVA: Enabling Queue Management Service for IN Retail. During peak times, like Diwali, Christmas, New Year, Cyber Monday etc., SVA will run promotional offers. These offers will result in increased traffic and there-by increased investigations being queued. In SVA, we have queues with very low SLA timelines (1hr) and with high volumes, it becomes difficult to adhere to SLAs for all the queued investigations. Task list, MoMs.
- TT: 0128828360 - Amazon Pay PPI general availability launch was blocked because it was not whitelisted as a valid payment instrument. A ticket was cut here: https://tt.amazon.com/0128828360, and I was called up on to diagnose this and take it to completion. I noticed that the payment instrument type was wrongly sent. I collaborated with the INPayment team and ensured that this is solved end-end.
- TT: 0121783939 - BSF client migration caused a rebound effect when, after migrating to the new version, our debug-console portal started failing to show pages. Although this was an on-call task, due to him being blocked on a launch-blocker, I stepped in, identified the issue, and fixed it before it escalated. This was appreciated by the on-call during our sprint retrospective.
- TT: 0128972298 – Manual investigation load saw an increase of 6.4k investigations in 3hrs duration. A sev-2 was cut during non-office hours to mitigate this. I identified the issue, took corrective steps & ensured that such incidents never happen again.

Dive Deep

- AbusePreventionService optimizations: I analyzed Profiler (profiler.amazon.com) data for AbusePreventionService and was able to identify root-causes for high CPU consuming cycles and make effective code changes to reduce the CPU cycle usage on non-business logic code. Analysis can be found here. Code changes here & here. Impact: GC time reduced from 15% to 2.42%, improvement in supported TPS by 20%.
- IMR reductions
- As a part of 2017 Dec, I took up the activity of releasing un-used hardware and optimise hard-ware usage by potentially replacing old-generation hardware with new generation hardware. I was able to replace all the old hardware host types with the new ones & was able to save $23000 per year in hardware costs.
- APS & AbuseCOPS: Identified opportunity to reduce the total no of hosts, when doing 2018 Prime-day scaling. Ran FLO tests and ensured that our hosts are benchmarked correctly & the right no. of hosts are used to support our traffic. FLO Analysis. Impact: Saved a total of $12344.16 per year in hardware cost.

Hire & develop the best

- Created multiple SDE onboarding page
- ACSCS: Created a structured approach for on-boarding a new team member with a repository of high-quality content that can be referred by anyone for a faster and a more structured on-boarding of new joiness into the team, with all necessary contents easily accessible: here. This is still used for all SDE on-boarding into ACSCS team.
- Created a TRMS SVA specific on-boarding page to help developers onboard to new projects quickly: here
- Created a 1st week, non-tech onboarding guide based on my experiences. This reduces time required for an SDE to set things up, from 1 week, to about 2 days.
- Created TRMS-INPay On-call helpbook to refer to the most common on-call questions & solutions for the same.
- Introduced Scaling for development process within TRMS to help teams in identifying the right Scrum process & adopt them with the right context, driving results & improvement. My team personally saw task completion rate go up from 50% to 85%.
- Facilitator of Scrum Workshop & Agile Product Ownership workshop. Have delivered 3 scrum workshops, reaching out to about 90 participants & 1 agile product ownership workshop, reaching out to 10 participants. Refer Givebacks.
- Mentored interns & SDE-1’s & SDE-2’s. Continue to mentor SDE-1’s
- Hiring:
- Interviews taken for TRMS between 1st Jan 2017 and 1st May 2018 – 68.
- Created a question-bank of interview questions that have been used in 14 weekend interview events have happened as of Oct 2017. Question bank
- Created a legendary bookmark page & troubleshooting page that’s referred more than 1000 times!

Awards received

- 1st place in ACSCS 2016 Hackathon: https://w.amazon.com/bin/view/ASCS_Hackathon_July_2016/
- TRMS Zeus Team Award for exceptional project delivery, RiPE: https://photos.app.goo.gl/Cd1GAgXuew0EEn2a2
- TRMS Spot Award for contributing towards team process improvements via Scaling for development guidelines: https://photos.app.goo.gl/v56xFvXIINeY0rjT2
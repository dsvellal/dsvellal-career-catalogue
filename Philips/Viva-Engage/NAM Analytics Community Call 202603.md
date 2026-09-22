# NAM Analytics Community Call 202603

> Converted from document `NAM Analytics Community Call 202603.pdf`

NAM Analytics Community Call
Philips North America
March 2026

Agenda
Topic

Presenter
AI Prompt Engineering

2

NAM Analytics Community Call | March 2026

Dattatreya Subramanya Vellal (Datta) –
Software Excellence Competence Lead

© Koninklijke Philips N.V.

Keynote Speaker
Meet Datta:
▪ ~20 years of Software Engineering experience,
previously working at IBM and Amazon
▪ Specializes in AI-assisted digital transformation
Datta Vellal
Software Excellence Competence Lead
Software Engineering Excellence

3

NAM Analytics Community Call | March 2026

▪ 7 years of Philips experience, driving large-scale digital
transformation and elevating engineering excellence
across global teams

© Koninklijke Philips N.V.

AI in Philips
▪ GenAI Certification Programs
▪ AI Apps in Philips
▪ Philips Generative AI page
▪ Kairos: www.philips.com/kairos
▪ Microsoft 365 CoPilot: https://m365.cloud.microsoft/chat/
▪ Philips AI Chat: https://www.dex.inside.philips.com/
▪ GitHub CoPilot: Request access to GitHub CoPilot

4

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Let's do an exercise together – to learn about context!

Write your prompt to plan
a vacation for 3 days to
your favorite destination.

5

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Prompt Engineering Essentials
▪ Distinguish prompting from “context”
▪ What to do (prompt), Background/info (context)

▪ Assign a persona (and why?)
▪ Elevates tone, vocabulary, context of execution & accuracy.

▪ Tell the model what good looks like (outputs)
▪ This gives a blueprint/template to mimic/adhere to

▪ Enforce constraints
▪ Be explicit in telling the model what NOT to do.

▪ Chain your thoughts
▪ Avoid massive prompts, break complex tasks into verifiable prompts

6

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Context Engineering Essentials
▪ Curate, do not clutter
▪ Feed the most distilled information required for the immediate task.

▪ Structure information hierarchy
▪ Use tags <background>, <instructions> etc. to organize data

▪ Mix tools with AI
▪ Python scripts, shell-scripts etc. Simple tools help reduce cognitive load.

▪ Think beyond first output
▪ What information from the first interaction should be persisted in the 5th?

7

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Prompt Engineering
▪
▪
▪
▪
▪
▪
▪
▪
▪
▪

8

Ask for role-based critique: “Review this prompt as <role> and tell me what I’m doing well and what I
should improve.” Repeat across multiple rounds.
Use multiple perspectives: have the AI review the same content as a senior technologist, senior architect,
program manager, and other relevant roles.
Build prompts iteratively: state your intent, then ask the AI to review the prompt and clarify requirements
by asking one question at a time with multiple relevant options. Tell it not to assume anything.
Use pre-processing and post-processing deliberately to improve results.
Choose a structured format when helpful: YAML, JSON, Markdown, or plain text can affect output quality.
Add configurable variables or flags so outputs can adapt, such as a default number of items that can
expand when requested.
Compare prompt versions over time: ask what v2.0 would look like versus v1.0, how they differ, and why.
Ask for both strengths and improvements so you can decide what to keep and what to change.
Work in smaller, controllable batches rather than very long prompts or tasks.
Do not overuse AI: apply your own judgment and use conventional tools when they are better suited,
such as Python libraries for OCR in some cases.

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

My AI agent non-negotiable rules
▪
▪
▪
▪
▪
▪
▪

9

Analyze what I am asking you to implement. If there are multiple asks, order them based on ask
with least dependency to ask with most dependency.
DO NOT assume anything. Ask me clarifying questions. One question at a time, with multiple
choices & your recommendation.
If my answers create gaps in understanding, add to your list of questions to ask me.
Start executing after you have asked me ALL the questions clarifying my prompts intent/asks.
Explicitly tell me, your thoughts, what factors were considered, why a certain decision was taken or
an output was provided. Do this as a precursor to the actual output.
Once the output is given, review it. See if all the intents are satisfied or not. If not, re-evaluate and
start the process again.
Confirm that you have understood all these instructions before executing.

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Examples – Good & Bad
Sl No

10

Principle

The "Bad" Approach (What to Avoid)

The "Good" Approach (Best Practice)

1

Prompting vs. Context

Mixed together: "Write an email to the team about the new server
migration but first read this entire IT manual and figure out what the
migration actually is."

Separated cleanly: "Context: [Insert 1-paragraph summary of migration dates]. Instruction: Using
only the provided context, write a 3-sentence email to the team."

2

Assign a Persona

Vague & generic: "Tell me about phishing attacks."

Specific role: "Act as a senior cybersecurity analyst training non-technical staff. Explain phishing
attacks using simple analogies, keeping an encouraging and professional tone."

3

Few-Shot Prompting

Zero examples: "Classify these customer reviews as either positive or
negative: 'Great job', 'Terrible service', 'Okay I guess'."

Clear blueprint: "Classify review sentiment. Review: 'Loved the food' -> Positive. Review: 'Cold soup'
-> Negative. Review: 'Great job' ->"

4

Ruthless Constraints

Open-ended: "Give me some ideas for a social media marketing
campaign for our new shoes."

Strict boundaries: "Generate exactly 3 ideas for a shoe marketing campaign. Output the result
strictly as a JSON array of strings. Do not include any conversational filler."

5

Chain Your Prompts

The mega-prompt: "Research the history of Rome, write a 5-page essay, Step-by-step: (Prompt 1) "Provide a 5-point outline on the fall of Rome." -> (Prompt 2) "Using point
translate it to Spanish, and give me 10 tweet ideas about it."
1 from the outline above, write the first paragraph."

6

Curate, Do Not Clutter

Context overflow: "[Pasting a 500-page employee handbook] What is the Surgical precision: "[Pasting just the 3-paragraph HR section on PTO] Based on this specific excerpt,
policy on taking a sick day?"
how do I request a sick day?"

7

Structure the Hierarchy

Flat text block: "Here is the log data user logged in at 5am failed
password retry lockout please analyze why the user is locked out."

Tagged sections: "<rule> Lockout occurs after 3 failed attempts. </rule> <log> 05:00: Fail. 05:01:
Fail. 05:02: Fail. </log> <task> Explain the lockout. </task>"

8

Orchestrate Tools Wisely

Ambiguous requests: "Look up the weather and then figure out 2+2 and
then draw me a picture of it."

Targeted routing: “Use the Weather API tool to get the current temperature in London. Then, use
the Calculator tool to convert that exact number to Fahrenheit.”

9

Think Beyond the Turn

Amnesia: "What was that thing we decided on a few minutes ago?"

Stateful recall: "In step 2, we established a 'Cyberpunk' theme for the story. Keeping that
established theme in mind, generate three names for the main villain."

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Helpful prompts

11

Prompt

Intent

AI Prompt Architect

This is a meta-prompt. This prompt, when executed, asks
questions to force context, and helps create the right prompts that
can be used to instruct the AI to do exactly what you want it to do.

Requirement Analysis
Requirement Document Analysis

Use this prompt to analyze your requirements against
the expectations of IEC 62304 and FDA’s Content of
Premarket Submissions for Device Software Functions. This also
includes INCOSE guidance rules.

Feature-to-Stories

Use this prompt as a guide during your PI planning to translate
higher level features into user-stories with proper success criteria.

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Feedback

https://forms.cloud.microsoft/e/trYJnFauAY

12

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

We Want to Hear from You!
• Email me at claudia.smith@philips.com
• Ideas for topics
• Volunteers to present their impacts on Philips business

13

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Common Data Models in ADL Today
New! Order Intake (OIT): prod_wb.nam.g__sales__oit_fact__tb (SAP)

Funnel (i.e. Opportunities): prod_wb.nam.g__sales__funnel_current__tb (Salesforce)
Account/Customer: prod_wb.nam.s__customer__account_master__tb (Salesforce, SAP, Definitive, DUNS)
Service Sales Account & Assignment: prod_wb.nam.g__customer__dt_service_sales_assignments__tb (Salesforce)
Hierarchy Layers
Customer Hierarchy: (IDNs) prod_wb.nam.s__customer__idn_master__tb
Product Hierarchy: prod_gold.financebi.dim_product_hierarchy_mag

Territory Hierarchy: prod_wb.nam.s__customer__territory_and_salesperson_assignments__tb

15

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

AI User Archetypes
Use Case

License Needed

Training

• Build & Publish Agents

Copilot Studio

▪ Microsoft Training Collection

▪
▪

Use custom agents
Use AI integration with
Microsoft Products

Copilot M365

▪ M365 Copilot Masterclass
▪ Copilot Prompting Masterclass

Power BI
Developer

▪
▪
▪

Assist in DAX logic
Prepare data for AI
Enable AI Chat layer

▪ Power BI License
▪ Tenant/Workspace requirements
▪ Admin access provisioning

▪ Copilot in Microsoft Fabric

Power App
Developer

▪
▪
▪

“Do it for me” builder
Create starter apps from prompt
Enable AI Chat layer

▪ Power App Premium
▪ Copilot Studio

Agent Developer
Analyst

No License

Use free AI resources like Philips AI Chat or Copilot Chat

▪ Copilot in Microsoft Power Apps
▪ Copilot Prompting Masterclass

What training & licenses do my team and I need?
16

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Enabling Copilot in Power BI
Steps to provision Copilot in non-DS&A Power BI workspaces:

Capacity Requirements

User License Requirements

Tenant & Workspace Settings

Owner: IT/Fabric Admin

Owner: User/Workspace Admin

Owner: IT/Fabric Admin

▪

Report is in a Copilot-enabled
Premium or Fabric capacity

▪

Power BI Pro or Power BI
Premium license required

▪

Provision user-level copilot
access within the tenant.

▪

(e.g., Fabric F64+ or Power BI
Premium P1+)

▪

Member/Contributor role
within a workspace to “light
up” Copilot

▪

IT may need a use case for
user-level access requests.

Free users cannot use Power BI
Copilot feature

17

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

What does Copilot M365 Get Me?
Access to Custom Agents to Drive Efficiency:

Work Mode in Copilot
Access to internal docs, emails,
meetings, reports.

Custom Agents Available in Copilot (w M365 license)

Assists in-depth research
(internal and external sources)

Leverage AI in Microsoft Platforms:

"On-call Data Scientist", Excel
analysis, Python
•
Facilitator Available in Teams/Outlook (w M365 license)
▪
▪

18

Automate Teams meeting notes & more
Learn how to use Facilitator

NAM Analytics Community Call | March 2026

•
•

Outlook. Email drafting, summaries & inbox
management. (e.g. “Find and flag all emails from
my manager about project X”)
PPT. Presentation generation & design.
Excel. Prompt AI for trends, outliers, summaries, or
even create pivot tables.
© Koninklijke Philips N.V.

AI Communities

Join Community Now!

•
•

Join the Data & AI Community Of Practice
Access upcoming events and presentation
recordings
Stay in the know via the Microsoft 365 Copilot Viva
Engage page: Join Community Now!

19

NAM Analytics Community Call | March 2026

© Koninklijke Philips N.V.

Power App Resources
Self-Service
Training
Learn Power App
at your own pace
with these
Learner
Curriculums.
Office hours with
Jordan Young
coming soon!!
20

NAM Analytics Community Call | March 2026

•

Beginner Curriculum - ~ 7.5 hrs Start Now

•

Intermediate Curriculum - ~ 11 hrs Start Now

•

Advanced Curriculum - ~ 10 hrs Start Now

•

Interactive Workshops - ~ 9 hrs Start Now

•

Build a Mobile-Optimized App - ~ 0.5 hrs Start Now

Power Apps Home Page
For all Training and for accessing the Power Apps Home Page, log in with your
Philips email and Single-Sign-On
© Koninklijke Philips N.V.


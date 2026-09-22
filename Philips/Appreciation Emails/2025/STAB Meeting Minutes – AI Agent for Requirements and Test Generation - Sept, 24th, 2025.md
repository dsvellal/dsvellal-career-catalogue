# STAB Meeting Minutes – AI Agent for Requirements and Test Generation - Sept, 24th, 2025

**From:** "Toufaili, Feras" <Feras.Toufaili@philips.com>  
**To:** "Browning, Ted" <ted.browning@philips.com>, "Bushey, Luke" <luke.bushey@philips.com>, "Mathapati, Shreeshail" <shreeshail.mathapati@philips.com>, "Cohn, Robert" <robert.cohn@philips.com>, "Moorthy, Easwara" <easwara.moorthy@philips.com>, "George, Leeja" <leeja.george@philips.com>, "Das, Ashita Ravindra" <ashita.das_1@philips.com>, "Jaeschke, Rhyse" <rhyse.jaeschke@philips.com>, "Mohanty, Amit" <amit.mohanty@philips.com>, "Gopalarathnam, Balaji" <Balaji.Gopalarathnam@philips.com>, "Maganur, Mahantesh" <mahantesh.maganur@philips.com>, "Vadakkeveedu, Karunakaran" <karunakaran.vadakkeveedu@philips.com>, "Dutt, Karan" <Karan.Dutt@philips.com>, "Dixon, Scott" <Scott.Dixon@philips.com>, "Li, Shengqiong" <Shengqiong.Li@philips.com>, "Dwarakanath, Dheemanth" <Dheemanth.Dwarakanath@philips.com>, "Subramanya Vellal, Dattatreya" <dsvellal@philips.com>, "Peszynski, Michael" <mike.peszynski@philips.com>, "Maier, Daniel" <dan.maier@philips.com>, "Wei, Qifeng" <qifeng.wei@philips.com>, "Kumar Lakshmana, Naveen" <naveen.kumar.lakshmana@philips.com>  
**Date:** Wed, 24 Sep 2025 22:26:50 +0000  

---

Hi Team,

Thank you all for your participation and valuable insights during the meeting this morning. Below is a summary of our discussions. A big thanks to Datta for taking his time to present a demo of this powerful agent.


  *   Datta showcased an AI agent (ReqSpec) designed to generate clear, testable requirements and associated tests. This agent is trained on IEC 62304, FDA pre-market guidelines, and INCOSE standards. Philips employees with a Microsoft Office 365 Copilot license can access the agent.


  *   The agent's functionality is quite impressive. It checks for compound requirements, encourages atomicity, and prompts users to split legacy requirements if necessary. It also asks for rationale, traceability, hazard/risk mitigation, priority, responsible modules, actions, conditions, performance expectations, classification, verification/validation methods, and error handling. The agent's conversational style allows users to revise their answers, ensuring that the requirements are context-rich and standards-compliant.


  *   During the demo, Datta used a sample ultrasound requirement provided by Dan: "When color steering in trapezoid is available, the system shall display the Acquisition line as a vertical or angled line based on the steering angle while in the trapezoid imaging format." Datta demonstrated the agent’s 17 step-by-step questioning and how it generates a structured requirement and test scenarios, including positive and negative cases. The agent can be customized to output requirements in different formats to match QMS or document structures.


  *   We also discussed test case generation. The agent creates more comprehensive test scenarios when requirements are fully detailed with attributes. While users can skip requirement structuring and directly generate test cases from an existing requirement using a generic chat AI, the results may be less specific.


  *   Our team, including Dan, Ted, Qifeng, Balaji, and Ashita, had a lively discussion about the adoption and use cases of the tool. Ted noted that system-level requirements are often too vague for concrete test cases, leading to reliance on V&V interpretation. Dan highlighted that different teams have varying needs for test case detail, and the tool could help provide recommendations for all. Balaji and Ashita agreed that the tool could assist verification and feature-level testing by providing structured test case guidance. Qifeng suggested integrating the tool with CSD to help developers identify negative test cases. We also discussed capturing the agent’s output in a shared document such as the Change Proposal (CP) for use by all testing teams, rather than mandating its use immediately.


  *   Datta explained that the agent can be further customized to match business needs, streamline the number of steps, and integrate with architecture diagrams for more relevant suggestions. Dan suggested piloting the approach with a sample Change Proposal to refine the process before broader adoption. Ashita asked about generating system- or feature-level test cases, and Datta clarified the difference between Office Copilot (requirements/test scenarios) and GitHub Copilot (code/unit tests), confirming that feature-level test case generation is possible with the right training data.

Here’s a link to the recording<https://share.philips.com/:v:/r/sites/SystemTestArchitectureBoardSTAB/Shared%20Documents/Recordings/STAB-20250924_Using-AI-Agent-For-Drafting-Requirements-And-Test-Cases.mp4?csf=1&web=1&e=nwwihD>. ReqSpec<https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fm365.cloud.microsoft%2Fchat%2F%3FtitleId%3DT_54dc0f14-4257-a0e6-4fc2-4fddc74994a3%26source%3Dembedded-builder&data=05%7C02%7Cdsvellal%40philips.com%7C4f94b342969c48a7c99b08ddfbb9750f%7C1a407a2d76754d178692b3ac285306e4%7C0%7C0%7C638943496127041013%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=4%2FvrM4Nx5QFVSEcXFq6pDy7mtkXQXv26JekHtW12ioI%3D&reserved=0> agent can be accessed by members with Microsoft 365 Copilot license.

Please let me know if you have any questions or have trouble accessing the links above.

Best,
Feras


________________________________
The information contained in this message may be confidential and legally protected under applicable law. The message is intended solely for the addressee(s). If you are not the intended recipient, you are hereby notified that any use, forwarding, dissemination, or reproduction of this message is strictly prohibited and may be unlawful. If you are not the intended recipient, please contact the sender by return e-mail and destroy all copies of the original message.

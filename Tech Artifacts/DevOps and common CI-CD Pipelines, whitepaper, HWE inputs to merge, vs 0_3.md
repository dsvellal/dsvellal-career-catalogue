# DevOps and common CI-CD Pipelines, whitepaper, HWE inputs to merge, vs 0 3

> Converted from `DevOps and common CI-CD Pipelines, whitepaper, HWE inputs to merge, vs 0_3.docx`


DevOps, Hosting & Operations
 and common CI-CD pipelines


A CAO whitepaper


Bangalore, Eindhoven, November 2020


Authors:

- Herwig Wens, Fellow Architect, Chief Architect Office
- Rajesh Arasu, Principal Architect, PIC
- Dattatreya Vellal, Competency Specialist, SWCoE
- Niek Palm, Sr. Architect, SWAT EIH
- Gert Jan Kamstra, Sr. Software Architect, SWAT EIH
- Marco Franssen, Sr. Software Architect, SWAT EIH

Reviewers:

- Klaas Wijbrans, Fellow Architect, Chief Architecture Office
- Ke Ke Qi, Principal Architect, CDI
- Simao Williams, Head of Competencies

## Content


## Objective


The objective of this whitepaper is to position DevOps at Philips and propose a standardized way of working with respect to Continuous Integration (CI) and Continuous Delivery (CD) within Philips.


## Chapter 1: *** FIND A GOOD CHAPTER TITLE ***


Why, value, compelling business case, introduction, nomenclature..


Philips is transitioning into a Solutions and Software Health Tech company. Already a significant part of Philips Solutions and Products contain software. The amount of software in our Solutions and Products will grow exponentially the coming years, as Customers will be asking continuously new features from our Solutions, which largely will be delivered and fueled by Software and Data.  Not only the amount of new software-based features within our Solutions will increase exponentially, but also the Customer’s expectation that these new features will be delivered securely and instantaneously without any disruption.  Consequently, creating and delivering software in a qualitive, repeatable and productive manner is paramount.


In order to be able to deliver a consistent customer experience and bringing coherent solutions fulfilling our Customer needs, Philips is moving its existing – and developing its new –  products and solutions within a selected set of domain platforms, established on top of HealtSuite Platform.


As more individual teams will contribute and develop on top of – or on software and platforms assets on/in the platforms, Philips eventually will be able to assemble and release rapidly, meaningful solutions and meaningful new features within these solutions for our Customers.


However, how do we prevent chaos in having a lot of developers and teams contributing software to a Solution when we will do this at scale? How do we make sure that the different building blocks are easy to assemble with the right quality and speed and assets are reused? How do we make sure that things do not break in the next release or when we add a new feature? How do we make sure that we Customers have always the latest and greatest update? How do we assure that when things break, we can deliver as soon as possible a fix, preferably before the Customer notices this…?


The answer is: our software teams need to work in a DevOps way following the HealthSuite Reference Architecture (HSRA) and rigorously follow the guardrails and build solutions on our HealthSuite Platform.


In this document we explain how DevOps with a common CI/CD (Continuous Integration / Continuous Delivery Pipeline), HSRA, guardrails, HealthSuite Platforms and Hosting & Operations all come together to enable Software Developers developing software with higher quality of code combining with faster releases and stable always-on Operations.


### Our four pillars for becoming a great software company driving Digital


A lot of has changed in the world of Software Engineering in the last fifteen to twenty years. Software Engineering is actually a young craft and recognized as one of the drivers within the Third Industrial revolution where electronics combined with software lead to production automation. You could state that Software combined with more Data, remains the fuel that drives the recently Fourth Industrial (Digital) revolution. One thing is for sure: Software has moved away from only being an Art to true Science & Engineering and has matured tremendously.


### Pillar 1: HealthSuite Reference Architecture (HSRA)


Within our Philips-wide encompassing reference architecture, called HealthSuite Reference Architecture (HSRA), we define a consistent, unified and company-wide approach to software architecture and platform development. HSRA guarantees that our products and solutions can integrate with each other and with their environment in an ecosystem approach and can share meaningful data across the health continuum.


[HERE A PICTURE OF HSRA TOP]


#### Guardrails and Factory Way of working


Within HSRA, we have defined guardrails: with guardrails we want to better leverage and institutionalize HSRA assets, CAO whitelisted (controlled)assets and the Software Center of Excellence (SWCoE) best practices (the so-called .craft models).


Our guardrails are prescriptive and will be (largely) mandatory enabled and backed in, in our common CI/CD pipeline that eventually allows our developers to work in a software factory way of working.


### Pillar 2: Cloud & Platforms


Cloud has massively changed the way on how we look at software and how we can produce and use software these days. Cloud brings endless compute and (data) storage in an affordable, pay per use and shared way, which we could only dream of before: Cloud basically has democratized software.


Cloud can also bring great value to healthcare, as healthcare is also increasingly becoming Digital and is relying on software and data. Obviously, healthcare is very strict in terms of a regulatory, privacy and security perspective, therefore Philips has decided to create HealthSuite Platform (HSP) that establishes a healthcare secure and regulatory envelope within the cloud for our Customers.


Businesses, but also Customers can build solutions or their specific domain platforms on top of HealthSuite Platforms.


[HERE a PICTURE of HSP + PICTURE of STACKED SOLUTION, DOMAIN PLATFORM, HSP.]


### Pillar 3: (Biz)Dev(Sec)Ops


DevOps represents a change in culture, focusing on rapid software delivery through the adoption of agile, lean practices in the context of a system-oriented approach, hence reducing waste.


DevOps emphasizes people and culture, and seeks to improve collaboration between development and operations teams. DevOps implementations utilize technology — especially automation tools that can leverage an increasingly programmable and dynamic infrastructure from a life cycle perspective, referred to as Continuous Integrated (CI) and Continuous Delivery (CD).


DevOps is based on the following three basic principle:

- The principles of Flow: accelerating the delivery of work from Development to Operations to our customers
- The principles of Feedback: enabling us to create ever safer systems of work
- The principles of Continual Learning and Experimentation: fostering a high-trust culture and a scientific approach to organizational improvement risk-taking as part of our daily work

#### The Principle of Flow


One of the fundamental concepts in Lean is the value stream. In manufacturing operations, the value stream is often easy to see and observe, but the same principles and patterns that enable the fast flow of work in physical processes are equally applicable to technology work (and, for that matter, for all knowledge work).


In DevOps, we typically define our technology value stream as the process required to convert a business hypothesis into a technology-enabled service that delivers value to the customer.


By speeding up flow through the technology value stream, we reduce the lead time required to fulfill internal or customer requests. By doing this, we increase the quality of work as well as our throughput.


#### The Principle of Feedback


We amplify feedback to prevent problems from happening again, or enable faster detection and recovery, by enabling the fast and constant flow of feedback from right to left at all stages of our value stream.


By doing this, we create quality at the source and generate or embed knowledge where it is needed—this allows us to create ever-safer systems of work where problems are found and fixed long before a catastrophic failure occurs. By seeing problems as they occur and fencing them until effective countermeasures are in place, we continually shorten and amplify our feedback loops. 
This maximizes the opportunities to learn and improve. Creating fast feedback is critical to achieving quality, reliability, and safety in the technology value stream.


#### The Principle of Continual Learning and Experimentation


By creating faster feedback loops, we are better able to take risks and perform experiments that help us learn faster. This enables the creation of a generative, high-trust culture that supports a dynamic, disciplined, and scientific approach to experimentation and risk-taking, facilitating the creation of organizational learning, both from our successes and failures.


We also need to design our system of work so that we can multiply the effects of new knowledge, transforming local discoveries into global improvements. Regardless of where someone performs work, they do so with the cumulative and collective experience of everyone in the organization.


The SWCoE (Software Center of Excellence) plays a key role in creating this culture of learning and experimentation.


#### From DevOps to DevSecOps and BizDevOps


What’s in a name…


Lately two other acronyms popped up – which we could call extensions on top of “classic” DevOps – adding explicitly Security (Sec) and Business (Biz).


DevOps


The “classic” DevOps process is often presented in the following iconic picture:


Figure 1 The classic DevOps process representation


The picture clearly presents a continuous loop where it suggests a better collaboration (not throwing over the fence) between development and operations.


Notice that Security is not mentioned in the above picture. However, Security is an integral part of each step in the process – this is why an alternative term, DevSecOps has been introduced, to clarify this.


DevSecOps


Security is often thought of as slowing things down by adding another layer of complexity... But when done right, a modern approach to security actually empowers software developers to move faster: DevSecOps is the philosophy of integrating security practices within the DevOps process. Basically “security best practices” need to be embedded within every step of the DevOps process, e.g.  'Security as Code' can be used to create an ongoing, flexible collaboration between release engineers and security teams.


Figure 2 DevSecOp: The DevOps process, annotated with security best practices


BizDevOps


DevOps increases the ability of an organization to deliver software at a higher velocity.


But what if the same tools and practices that accelerate feature delivery can also be used to generate greater business value? That’s where BizDevOps comes in.


BizDevOps integrates feedback from the business side of an organization into its delivery cycles, effectively ensuring features released through DevOps cycles are built specifically to serve business objectives. A streamlined workflow is created from business strategy to deployment, allowing DevOps metrics to become aligned with high-level business KPIs.


As with DevOps, BizDevOps can be seen as a combination of cultural philosophies, practices, and tools that increase an organization’s ability to deliver applications and services at high velocity. When DevOps overcomes silos separating development from operations, BizDevOps overcomes silos separating DevOps from the rest of the business.


BizDevOps is accomplished by encouraging the business team to work directly with product owners, developers, and operators to set priorities for sprints and backlogs. Collaboration with the business team is encouraged throughout the entire release cycle:


Figure 3 BizDevOps (Business included as an essential partner in DevOps)


Notice


For simplicity in this document, we will further use the acronym DevOps, but in many cases, you could substitute DevOps with DevSecOps. At the end of document, we will make some suggestions on how Businesses – and how also Customers (!) can play a bigger role and better be integrated within DevSecOps.


#### Metrics


Metrics play a crucial role of to create a culture of transparency and trust.


We cannot improve our software development processes if we cannot objectively determine whether change has been successful. Software development should become metrics-driven and use metrics-gathering techniques properly to drive modern development practices.

- Metrics are a primary source of feedback, and feedback is a key objective of agile and DevOps methodologies. Development teams that collect and analyze metrics understand successes, failures and opportunities for improvement better than their peers.
- Baselines are controls that point to data from a specific time or during a specific interval. Mature development teams actively monitor metrics data and compare results with previous baselines.

To accurately understand progress, development teams should collect metrics from many aspects of the development process, including project business value, culture, processes, infrastructure, architecture, and development and test.


Through six years of research, the DevOps Research and Assessment (DORA) team has identified four key metrics that indicate the performance of a software development team:

- Deployment Frequency - How often an organization successfully releases to production
- Lead Time for Changes - The amount of time it takes a commit to get into production
- Change Failure Rate - The percentage of deployments causing a failure in production
- Time to Restore Service - How long it takes an organization to recover from a failure in production

The following benefits have been measured by using DevOps:


### Pilar 4 Hosting & Operations


Hosting & Operations is the capability that delivers, maintains and improves a platform as a service (PaaS), including the continuous integration/continuous delivery (CI/CD) toolchain, for multiple agile application teams delivering software.


The goal of Hosting & Operations in the context of DevOps is to achieve efficiencies and economies of scale in a DevOps environment, where application product delivery teams are responsible for deploying and operating their own applications. A shared consistent platform reduces duplication of technology, enables automation and focuses expertise.


The platform is itself a product used by developers. Collaboration between Hosting & Operations (also sometimes known as central or platform ops) and development teams is essential to create a software-defined platform that operates to the standard required to protect the organization while allowing the development teams to move fast.


The central ops approach is effective whether the underlying infrastructure is in a public cloud, a private cloud, or a virtualized and automated environment on-premises. The details are different, but the high-level functions are common, including security, access control, compliance, cost management and performance management leading to efficiencies, when done centrally.


Figure 6 Central Operations as a Service


The central ops team is responsible for providing a self-service development, deployment and operational platform that enables multiple software delivery teams to build and operate their own products.


## Chapter 2: Bringing it all together at Philips


### The bigger picture of End-to-End Software Development & Operations


As said before, “true BizDevOps”, means actually a culture shift towards truly collaborating across organizational boundaries with the objective to create customer value; and customer value is increasingly created thru software. Our customers are asking for high quality, flexible and integrated solutions with high availability, easy to patch and to upgrade against affordable costs.


Figure 7 End to End Software Development and Operations


In the above picture we depict our North Star, on how different parts in Philips contribute to the end-to-end software development and operations to deliver the right customer value.


Businesses and Platforms will develop in a DevOps way (Plan, Code, Build, Test, Release) with standard CI/CD pipeline tools and assets provided by the Central Hosting and Operations team.


Businesses will increasingly focus on Winning HealthSuite Solutions and bringing their domain platforms (on top of HealthSuite) to the (hybrid) Cloud in a multi-tenant way. New customer driven requirements will come in thru Integrated Value Propositions and Businesses will be able in assembling rapidly these new requirements based on secure platform assets in a DevOps way. Thru a Digital Channel, such as a Customer Portal, including an omni channel customer ticket system integrated into the solution and Customer Portal, Customers will be able to demand new features or require bug fixes. Based on proactive triage and monitoring integrated in the product and CI-CD pipeline both businesses or where needed supported by Hosting & Ops will be able to develop or unlock new features, or do bug fixing and release this rapidly to Customer(s).


Hosting and Operations will provision the standard, hardened and secured CI-CD pipeline tools and assets to the Business. They will help the business in releasing (e.g. with canary or blue-green type of deployments) products and solutions, and provide proactive monitoring & alerting, connectivity (thru Edge to the Customer on-premise), provide proactive infrastructure patching and updating, enable product upgrading thru Edge, enable/do usage metering and provide 24x7 global operational support.


Customer Services will provide Customer Insights and provide preventive maintenance information based on feedback log data coming from our modalities thru IOTHub and Edge. Customer Services will also assist Markets and Businesses with Installation, Configuration and Maintenance of on-premise devices and common infrastructure.


The Central Hardware (HW) and Operating System (OS) team


Conclusion


A consistent adoption of platforms and digital technologies combined with best-in-class software practices will enable a superior software quality, solution innovation and will get us to the North star of the Quadruple Aim.


A standard, KPI measurable CI-CD (Continuous Integration – Continuous Deployment) pipeline embedding agreed best practices, guidelines and standard tools, will make it easier for businesses to adopt platforms and create better quality software faster.


### Software Archetypes


At Philips we create different types of software. We are categorizing our broad spectrum of software flavors in 5 distinct categories:


### CI-CD Pipeline Reference Architecture


#### A DevOps process in a nutshell


The input to our DevOps process is the formulation of a business objective, concept, idea, or hypothesis, and starts when we accept the work in Development, adding it to our committed backlog of work.


From the backlog, Development teams that follow a typical Agile or iterative process will likely transform that idea into user stories and some sort of feature specification, which is then implemented in code into the application or service being built.


The code is then checked in to the version control repository, where each change is integrated and tested with the rest of the software system.


Because value is created only when our services are running in production, we must ensure that we are not only delivering fast flow, but that our deployments can also be performed without causing chaos and disruptions such as service outages, service impairments, or security or compliance failures.


#### Key Elements of a Continuous Integration and Continuous Deployment Pipeline


Guardrails


With guardrails we want to better leverage (institutionalize) HSRA assets, CAO whitelisted assets and SW CoE .craft models.


<Describe here the type of guardrails applied as a pipeline asset, step..>


Software Factory way of working


Innersource


Tech debt & waste


Central OS & central Hardware


Integration Labs – “templating” … / staging – patterns & recommendation.


Metrics and insights from pipeline


Observability and Serviceability


### Use Case: DI & Tasy


## Chapter 3: Hosting & Operations and CI-CD


H&O pipelines 2 pipelines.


## Chapter 4: Adoption styles of CI-CD


Repeatability v/s self-service mode of hosting


Migration from old to new – adoption patterns


## Conclusion


### What’s next? CustomerBizDevSecOps..?


Ecosystems, Customer Requests, Co-creation, Sensors, Data, Analysis, Feedback loops


## Internal References

- <TODO:LINK>

## External References

- https://www.weforum.org/agenda/2016/01/the-fourth-industrial-revolution-what-it-means-and-how-to-respond/
- https://www.informationweek.com/devops/8-business-benefits-of-adopting-devops/d/d-id/1328460
- The DevOps Handbook - TODO
- The Phoenix Project – TODO
- https://www.cloudops.com/blog/everything-you-need-to-know-about-bizdevops/
- https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance
- https://www.devops-research.com/research.html  (DORA)
- https://www.devops-research.com/research.html#capabilities

## Terms & Definitions


### Table 1

| Figure 4 DevOps benefits according CIO Insight | Figure 5 DevOps benefits (high performers versus low performers) from DORA |
| --- | --- |


### Table 2

| Category Type | Definition |
| --- | --- |
| Embedded Software  (Cat 1) | Real time software used for controlling devices & integrated with HW |
| Enabling Software (Cat 2) | Software to control & connect to a HW system such as the embedded PCs in modalities |
| Application Software (Cat 3) | Product specific (medical/health application) software that fulfills the overall proposition |
| Medical Middleware (Cat 4) | Software platforms needing medical domain knowledge (as in the Federated data & Interop platforms, AI platforms) |
| Infrastructure Software (Cat 5) | Generic SW platforms, IT apps, storage, cloud, Big Data and Analytics, security, privacy (as in the Hosting & Operations platforms) |


### Table 3

| Terms | Definition |
| --- | --- |
| BizDevOps | BizDevOps can be seen as a combination of cultural philosophies, practices, and tools that increase an organization’s ability to deliver applications and services at high velocity. When DevOps overcomes silos separating development from operations, BizDevOps overcomes silos separating DevOps from the rest of the business. |
| Cloud Computing | As defined by NIST: Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. |
| Continuous Integration (CI) | Continuous integration (CI) is the practice of merging all developers' working copies to a shared working copy several times a day. In this process of merging to a shared copy, server sanity checks can be performed to ensure that the quality of the shared copy is maintained. |
| Continuous Delivery (CD) | Continuous delivery is an approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time, and in releasing the software, doing so manually. The approach aims at building, testing and releasing software with speed and frequency. |
| Continuous Deployment (CD) | Continuous deployment is a step closer towards automation, where the software produced through continuous delivery can be deployed at a desired environment automatically. |
| DevOps | DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality. |
| DevSecOps | DevSecOps is the philosophy of integrating security practices within the DevOps process. DevSecOps involves creating a 'Security as Code' culture with ongoing, flexible collaboration between release engineers and security teams. |
|  |  |
|  |  |
|  |  |
|  |  |

# Evidence: SW Excellence Dashboard Presentation — Cross-Team Influence

## Source
- **File:** `20200506_SWExcellence_Dashboard_Influence.png`
- **Date:** 2020-05-06
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer - Software Center of Excellence SW_CoE)
- **Category:** Informal Feedback

## Metadata
- **From:** Tyagaraj, Anand (presenter); Wang, Hertz Hz (influenced team lead)
- **To/About:** SW CoE team / Vellal, Dattatreya (community moderator who thanked the presenter)
- **Context:** Tyagaraj, Anand presented Automation Dashboards to the SW CoE community. Datta publicly thanked the presenter and highlighted the value. The presentation then influenced Wang, Hertz Hz's China-based team to replicate the dashboard approach. Seen by 279 people.
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** Srivastava, Omkar Nath; Wang, Hertz Hz; and 2 others reacted

## Datta's Involvement
- **Role at time:** Senior Software Engineer / SW CoE
- **Involvement type:** Community facilitator — moderated discussion, publicly thanked presenter, amplified value

## Key Quotes
> "Thank you very much Tyagaraj, Anand for taking your time and presenting this to our community. This session was very helpful for us to understand how TA has helped multiple businesses in setting up live KPI dashboards. The session was practical and very insightful, and gives us examples of how to leverage data! Thank you again."
— Vellal, Dattatreya

> "@XIA, Pony, Zhang, Sunny Y, Yang, Saiqing Sq — Can we build up this kind of Dashboard?"
— Wang, Hertz Hz (demonstrating cross-team influence)

## Full Content
```
Software Center of Excellence (SW_CoE)

Tyagaraj, Anand — May 6 at 11:58 AM
Thanks for SW COE team for bringing up discussion about the below presentation and receiving it well. Attaching the slides which contains brief description about their functionality. Also each slide has URL of the dashboards for reference.

Brief what to expect in presentation:
1. Dashboards - KPI Dashboard - Real-time update of key Static Analysis metrics, Test Metrics etc. in the dashboard
    Metrics Dashboard - Custom metric dashboard created as per BIU requirement
2. Infra Analytics - Infra - VM Utilization, High level view of overall VMs, View VM's whose resource utilization is breaching the threshold, View high configuration VMs, that are rarely used, Overall VMs under a BIU
3. Build Analytics - Command Center - Self Service Analytics -
    Persona based configurable views that can be projected on a bigger screen
    Service hooks exposed APIs receives unstructured data. The data can be stored in a warehousing database.
    Provision to have free query and generate a custom dashboard could be done like below:
    Query able fields and generate reports dynamically
    Pre-built templates for visualization – that could be selected and applied for command center dashboard
    Pre-built dashboards – a readymade dashboard that could be used as-is.

cc: Mudiganti, Satyanarayana Reddy, Shamanna, Nagaraj, and Shukla, Susmita

FILES: Dashboards.pptx, image 11.png, image 12.png

Seen by 279

---

Vellal, Dattatreya — May 7 at 09:54 AM
Thank you very much Tyagaraj, Anand for taking your time and presenting this to our community. This session was very helpful for us to understand how TA has helped multiple businesses in setting up live KPI dashboards. The session was practical and very insightful, and gives us examples of how to leverage data! Thank you again.

cc: Tyagaraj, Anand

---

Shapira, Amittai — May 8 at 06:58 PM
Thank you Tyagaraj, Anand - can you please share the SW architecture and technology used to implement those dashboards other than SQL server?

cc: Tyagaraj, Anand

---

Tyagaraj, Anand in reply to Shapira, Amittai — May 8 at 07:54 PM
Hi Amittai,
The slide 2 talks about Generic Architecture, also attached below. We are following same architecture for KPI and Metrics Dashboards. However for Analytics, the data is obtained through ServiceHooks. Second image talks about pushing build logs to Elasticsearch and visualized through Kibana.

Do let me know if you need more details.

---

Wang, Hertz Hz — May 17 at 07:42 PM
@XIA, Pony, Zhang, Sunny Y, Yang, Saiqing Sq

Can we build up this kind of Dashboard?
Xu, Xuxiao X, Liu, Luke Kg

cc: XIA, Pony, Zhang, Sunny Y, Yang, Saiqing Sq, Xu, Xuxiao X, and Liu, Luke Kg
```

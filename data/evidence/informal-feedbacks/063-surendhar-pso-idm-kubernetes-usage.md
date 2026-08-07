# Evidence: Surendhar Vaithiyanathan — PSO IDM Kubernetes Advisory

## Source
- **File:** `20240228-Surendhar-PSO-IDM-Kubernets-Usage-Part-1.png`, `20240228-Surendhar-PSO-IDM-Kubernets-Usage-Part-2.png`, `20240228-Surendhar-PSO-IDM-Kubernets-Usage-Part-3.png`
- **Date:** 2024-02-28
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Teams Chat)
- **Category:** Informal Feedback

## Metadata
- **From:** Vaithiyanathan, Surendhar (PSO for ISPACS including IDM)
- **To/About:** Datta Vellal (Subramanya Vellal, Dattatreya)
- **Context:** Surendhar sought Datta's technical opinion on the IDM team's plan to upgrade IDM neb Node OS with Alma Linux and K3S (Kubernetes). Surendhar acknowledged Datta had already provided guidance to IDM team member Sijo. The conversation demonstrates Datta's role as a trusted technical advisor across Philips business units on infrastructure decisions.
- **Platform:** Microsoft Teams (1:1 Chat)

## Datta's Involvement
- **Role at time:** Principal Engineer / SW CoE
- **Involvement type:** Technical advisor — consulted on Kubernetes/infrastructure architecture decisions; already provided guidance to IDM team

## Key Quotes
> Surendhar: "I was checking with IDM team - they are planning to upgrade IDM neb Node OS with Alma & K3S"

> Surendhar: "mentioned that they even got some inputs with you"

> Surendhar: "is it the right approach"

> Surendhar (on Datta's recommendation): "yes" / "thats a good approach"

## Datta's Technical Guidance
1. Confirmed he had already talked to Sijo and showed him "paths to explore"
2. Advised that Alma Linux adoption in Philips is evident, showed which projects (including IoT Hub) have leveraged Alma Linux
3. Questioned K3S for self-hosted Kubernetes, noting CAO had not whitelisted it
4. Suggested looking at whether Fiesta offers native Kubernetes managed services via AWS
5. Recommended focusing on security risk mitigation if team chooses to self-host Kubernetes

## Full Content
```
[Chat with Vaithiyanathan, Surendhar]

Vaithiyanathan, Surendhar 28/02 10:22
Hi Datta
Good morning
How are you

28/02 10:24
Datta: Hi Surendhar.. I am good.. how are you?

Vaithiyanathan, Surendhar 28/02 10:25
I am good
One quick suggestion
I was checking with IDM team - they are planning to upgrade IDM neb Node OS with Alma & K3S
mentioned that they even got some inputs with you

28/02 10:26
Datta: yeah.. I talked to Sijo and told him on paths to explore.

Vaithiyanathan, Surendhar 28/02 10:27
is it the right approach

28/02 10:28
Datta: do you have a suggestion? I told him that I do not know which is the right OS to choose, and he'd be better of consulting PSO or OS team on this, however, I told him that the adoption of Alma Linux in Philips is evident, and showed him which projects (including IoT Hub) have leveraged Alma Linux.

Vaithiyanathan, Surendhar 28/02 10:29
I am the PSO for ISPACS (including IDM)
[thumbs up x1]
I am fine with Alma Linux but bit skeptical about K3S

28/02 10:30
Datta: talk to me about this.. what is the cause of concern?

Vaithiyanathan, Surendhar 28/02 10:31
I remember K3S was not whitelisted by CAO for various reasons..
Lifecycle management was very difficult something?

28/02 10:33
Datta: this is for self-hosted Kubernetes right?
Datta: I am unsure if CAO is actively maintaining that list of whitelisted/greylisted/blacklisted softwares.
Datta: Do you know if they are maintaining it?

Vaithiyanathan, Surendhar 28/02 10:34
[Quoting: this is for self-hosted Kubernetes right?]
yes
[Quoting: I am unsure if CAO is actively maintaining that list of whitelisted/greylisted/blacklisted softwares.]
I think SSD COE is responsible for this..but need to check if that exists and is someone maintaining this

28/02 10:39
Datta: I am not sure about Kubernetes self-hosting.. Do you want to suggest to them, Fiesta? I am sure they can look at if Fiesta offers native Kubernetes managed services via AWS?

Vaithiyanathan, Surendhar 28/02 10:53
but not sure if they will offer it as a base image

28/02 10:54
Datta: ok.. if the team choose to host their Kubernetes, then I think I would keenly look at how they plan on upgrading it to mitigate any security risks..
Datta: What do you think?

Vaithiyanathan, Surendhar 28/02 10:55
yes
thats a good approach
```

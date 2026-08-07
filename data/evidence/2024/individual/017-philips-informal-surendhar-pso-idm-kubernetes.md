---
title: "Surendhar Vaithiyanathan — PSO IDM Kubernetes Usage Advisory (3-part conversation)"
date: 2024-02-28
year: 2024
era: Philips USA
organization: Philips
category: Informal Feedback
source_type: image
channel: internal_screenshot
involvement: direct_recipient
role: Software Competency Lead
people: ["Vaithiyanathan, Surendhar", "Subramanya Vellal, Dattatreya", "Sijo"]
skills: ["kubernetes", "infrastructure-advisory", "alma-linux", "k3s", "cloud-strategy", "technical-advisory", "security"]
programs: ["PSO ISPACS", "IDM", "Fiesta"]
tags: ["informal-feedback", "chat", "kubernetes", "infrastructure", "advisory", "alma-linux"]
sentiment: positive
impact_type: recognition
recurring: false
---

# Evidence: Surendhar Vaithiyanathan — PSO IDM Kubernetes Usage Advisory (3-part conversation)

## Source
- **File (Part 1):** `data/evidence/images/2024/20240228-surendhar-pso-idm-kubernetes-part-1.png`
- **File (Part 2):** `data/evidence/images/2024/20240228-surendhar-pso-idm-kubernetes-part-2.png`
- **File (Part 3):** `data/evidence/images/2024/20240228-surendhar-pso-idm-kubernetes-part-3.png`
- **Date:** 2024-02-28
- **Ingested:** 2026-08-06
- **Channel:** Microsoft Teams chat screenshot (3 parts)
- **Category:** Informal Feedback

## Context
Surendhar Vaithiyanathan (PSO for ISPACS including IDM) reached out to Datta for advisory guidance on the IDM team's plan to upgrade their NEB Node OS with Alma Linux and K3S (a lightweight Kubernetes distribution). Surendhar mentioned that the IDM team had already gotten inputs from Datta when talking to Sijo. Datta had previously guided Sijo on paths to explore. In this follow-up conversation, Datta provided guidance on: Alma Linux adoption across Philips, skepticism around K3S (CAO whitelisting concerns), K3S lifecycle management challenges, self-hosted Kubernetes security considerations, and recommending Fiesta-managed Kubernetes over self-hosted K3S. Surendhar validated Datta's approach as "a good approach."

## Content

### Part 1

**Vaithiyanathan, Surendhar (28/02 10:22):**
> Hi Datta
> Good morning
> How are you

**Datta (28/02 10:24):**
> Hi Surendhar.. I am good.. how are you?

**Vaithiyanathan, Surendhar (28/02 10:25):**
> I am good
> One quick suggestion
> I was checking with IDM team - they are planning to upgrade IDM neb Node OS with Alma & K3S
> mentioned that they even got some inputs with you

**Datta (28/02 10:26):**
> yeah.. I talked to Sijo and told him on paths to explore.

**Vaithiyanathan, Surendhar (28/02 10:27):**
> is it the right approach

**Datta (28/02 10:28):**
> do you have a suggestion? I told him that I do not know which is the right OS to choose, and he'd be better of consulting PSO or OS team on this, however, I told him that the adoption of Alma Linux in Philips is evident, and showed him which projects (including IoT Hub) have leveraged Alma Linux.

### Part 2

**Vaithiyanathan, Surendhar (28/02 10:29):**
> I am the PSO for ISPACS (including IDM)
> I am fine with Alma Linux but bit skeptical about K3S

**Datta (28/02 10:30):**
> talk to me about this.. what is the cause of concern?

**Vaithiyanathan, Surendhar (28/02 10:31):**
> I remember K3S was not whitelisted by CAO for various reasons..
> Lifecycle management was very difficult something?

**Datta (28/02 10:33):**
> this is for self-hosted Kubernetes right?
> I am unsure if CAO is actively maintaining that list of whitelisted/greylisted/blacklisted softwares.
> Do you know if they are maintaining it?

**Vaithiyanathan, Surendhar (28/02 10:34):**
> [quoting Datta: "this is for self-hosted Kubernetes right?"]
> yes
> [quoting Datta: "I am unsure if CAO is actively maintaining that list..."]
> I think SSD COE is responsible for this..but need to check if that exists and is someone maintaining this

### Part 3

**Datta (28/02 10:39):**
> I am not sure about Kubernetes self-hosting.. Do you want to suggest to them, Fiesta? I am sure they can look at if Fiesta offers native Kubernetes managed services via AWS?

**Vaithiyanathan, Surendhar (28/02 10:53):**
> but not sure if they will offer it as a base image

**Datta (28/02 10:54):**
> ok.. if the team choose to host their Kubernetes, then I think I would keenly look at how they plan on upgrading it to mitigate any security risks..
> What do you think?

**Vaithiyanathan, Surendhar (28/02 10:55):**
> yes
> thats a good approach

## Key Quotes

> "thats a good approach" — Vaithiyanathan, Surendhar, validating Datta's security-first guidance on self-hosted Kubernetes

> "I told him that the adoption of Alma Linux in Philips is evident, and showed him which projects (including IoT Hub) have leveraged Alma Linux."

> "if the team choose to host their Kubernetes, then I think I would keenly look at how they plan on upgrading it to mitigate any security risks.."

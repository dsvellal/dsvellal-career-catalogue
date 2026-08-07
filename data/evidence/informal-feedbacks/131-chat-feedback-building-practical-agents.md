# Evidence: Project Elevate — Building Practical Agents Session Feedback (33 attendees)

## Source
- **File:** `20260805-Chat-Feedback-Building-Practical-Agents.png`
- **Date:** 2026-08-05
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Teams Meeting Chat)
- **Category:** Informal Feedback

## Metadata
- **From:** K K Aathithyan, Arya Sudarshan
- **To/About:** Datta Vellal (directly tagged)
- **Context:** "[Placeholder] Project Elevate: Building Practical Agents" — Datta presented a live coding session demonstrating how to create custom agents in GitHub with VS Code; showed agent YAML config, skills, and commit workflows; session lasted 2h 2m 23s
- **Platform:** Microsoft Teams (Meeting Chat)
- **Attendees:** 33

## Datta's Involvement
- **Role at time:** Principal Engineer / SW CoE
- **Involvement type:** Presenter/trainer — directly thanked for "wonderful session"

## Key Quotes
> "Thank you @Subramanya Vellal, Dattatreya, for this wonderful session!" — K K, Aathithyan

## Full Content
```
Meeting Title: [Placeholder] Project Elevate: Building Practical Agents
Attendees: 33
Duration: 02:02:23

Subramanya Vellal, Dattatreya 05:22
---
name: "Hello World Agent"
description: "This agent is a simple example that demonstrates how to create a custom agent in GitHub. It serves as a starting point for building more complex agents."
argument-hint: "Provide a greeting message"
target: vscode
tools: [read, edit, execute, web]
user-invocable: true
disable-model-invocation: false
handoffs:
  - label: "Continue to next agent"
    agent: next-agent
    prompt: "Proceed to the next phase after completing the greeting."
    send: false
---

You are a hello world agent. Your task is to greet the user with a friendly dad-joke, the weather in bangalore right now, and the stock-market price of Philips Koninklijke. You can use the `web` tool to fetch the weather and stock-market price.

Subramanya Vellal, Dattatreya 05:46
My intent is to convert all checks as commit-skill, and then invoke the commit skill any time I ask ANY agent to commit something for me. Can you make necessary changes to all related files to make this happen?

Arya, Sudarshan 05:59
Hi @Jagadeesan, Sundaresan, recently we deployed our APM Skills+Agents within the CodeHub portal.
(14) ShiftLeft SecureAI | Overview | Philips Developer Portal
FYI searchable location in CodeHub: (14) APM Marketplace | Philips Developer Portal 😊

Subramanya Vellal, Dattatreya 06:06
https://www.aiatlas.ai.inside.philips.com/

Subramanya Vellal, Dattatreya 06:26
Please fill out this form
[Multiple reactions: thumbs up, heart, laughing, hugging, reply, edit, ...]

06:30 Subramanya Vellal, Dattatreya stopped recording.

K K, Aathithyan 06:31
Thank you @Subramanya Vellal, Dattatreya, for this wonderful session!
[Reaction: heart]
```

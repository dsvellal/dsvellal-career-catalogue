# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

React + TypeScript + Vite + D3. Single-page application with tab-based navigation. CSS in a single styles.css file (no CSS-in-JS). Static deployment target.

## Users

Broad professional audience: hiring managers evaluating senior/principal engineering leadership roles, engineering peers and collaborators, conference organizers, community members, and anyone seeking to understand Dattatreya (Datta) Vellal's professional identity and impact. Viewed on desktop and mobile, often from a shared link or search result.

## Product Purpose

A living digital portfolio and professional identity system — not a static resume site. It makes 20 years of career depth, quantified impact, peer validation, and community contribution explorable and verifiable in one place. Backed by a structured knowledge layer that can generate tailored outputs (resumes, cover letters, weekly summaries) from rich contextual data.

## Positioning

Combines two differentiators no standard resume or LinkedIn profile offers: (1) a structured knowledge system / digital twin architecture that enables AI-powered tailored outputs, and (2) unprecedented depth of evidence — quantified impact across four organizations, 220+ peer testimonials, a full talks inventory, and a knowledge graph mapping skills across eras.

## Operating Context

Eight interactive views: Overview (hero), Professional Identity (BeTalent force graph), Career Arc (stacked bar), Impact (20 filterable cards), Timeline (vertical accordion, 343 achievements), Voices (220 rotating quotes), Talks & Givebacks (3-column + activity bar), Knowledge Graph (5 sub-views). Data sourced from JSON files extracted via DuckDB from a comprehensive personal knowledge corpus.

## Capabilities and Constraints

- Single-page app with client-side tab routing (no URL-based routes currently)
- All data is static JSON — no backend API
- D3 used for force-directed graphs and data visualizations
- Era-based color coding across all views (IBM blue, Amazon green, Philips orange, Exeter gold, Independent purple)
- Professional headshot photo and Devanagari-script logotype as brand assets
- Dark theme throughout

## Brand Commitments

Current visual identity is functional but open to evolution. No hard constraints on the dark theme, era colors, or typography — all can be refreshed if design direction warrants it. The Devanagari logotype and professional photo are retained assets.

## Evidence on Hand

- Professional headshot: `viz/public/photo.jpg`
- Logotype: `viz/public/logo.jpg`
- 343 deduplicated timeline achievements across 5 eras
- 220+ peer testimonials and recommendations
- 40+ documented talks and social contributions
- Quantified metrics: $3M+ savings, 60% delivery reduction, 99.999% uptime, 10,000+ children reached
- Full career arc data with recognition/certification/recommendation counts by year

## Product Principles

1. **Evidence over claims** — every assertion is backed by quantifiable data or verifiable testimony
2. **Whole person, not just professional** — social impact, volunteering, and community building are first-class alongside technical achievements
3. **Explorable depth** — visitors choose their own path through the material at any level of detail
4. **Living system** — the portfolio is a product of the knowledge layer, not a handcrafted static site

## Accessibility & Inclusion

No specific standard established yet. Current implementation uses semantic HTML, keyboard navigation on interactive cards, and sufficient contrast on the dark theme. WCAG 2.1 AA as a reasonable target.

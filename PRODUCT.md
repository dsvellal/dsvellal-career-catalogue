# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

React + TypeScript + Vite + D3. Single-page application with hash-addressable view navigation and namespaced CSS (no CSS-in-JS). Static deployment target.

## Users

Broad professional audience: hiring managers evaluating senior/principal engineering leadership roles, engineering peers and collaborators, conference organizers, community members, and anyone seeking to understand Dattatreya (Datta) Vellal's professional identity and impact. Viewed on desktop and mobile, often from a shared link or search result.

## Product Purpose

A living digital portfolio and professional identity system — not a static resume site. It makes 20 years of career depth, quantified impact, peer validation, and community contribution explorable and verifiable in one place. Backed by a structured knowledge layer that can generate tailored outputs (resumes, cover letters, weekly summaries) from rich contextual data.

## Positioning

Combines two differentiators no standard resume or LinkedIn profile offers: (1) a structured knowledge system / digital twin architecture that enables AI-powered tailored outputs, and (2) unusual evidence depth—quantified impact across four employers, 20 attributed public recommendations, 80+ contributors to the informal-feedback archive, a full talks inventory, and a knowledge graph mapping skills across eras.

## Operating Context

Eight evidence-led Journey Atlas views: Executive Portrait, Twenty-Year Journey, Capability Compounder, Outcome Ledger, Trust & Respect, Influence Web, Teaching & Service Ripple, and Momentum & Next Horizon. Together they move from identity and chronology through capability, outcomes, independent validation, influence, service, and future direction. The public site consumes one curated static journey dataset; the full graph and raw evidence remain private analysis sources.

## Capabilities and Constraints

- Single-page app with hash deep links (`#portrait`, `#journey`, `#capabilities`, `#outcomes`, `#respect`, `#influence`, `#service`, `#momentum`)
- All data is static JSON — no backend API
- SVG/CSS visualizations express braided timelines, capability rivers, leverage ladders, evidence timelines, structured influence flows, service ripples, and momentum signals
- Evidence tiers and caveat labels remain attached to claims; visualization geometry is explicitly bounded so it is not mistaken for causality, psychometrics, or proportional scale
- Professional headshot photo and Devanagari-script logotype as brand assets
- Warm architectural-blueprint visual language with responsive and print treatments
- Production builds disable Vite's `public/` directory; raw evidence is not copied into the deployable bundle

## Brand Commitments

The current visual identity uses warm vellum, architectural rules, restrained blueprint accents, condensed display type, and a provenance vocabulary that feels rigorous without becoming clinical. The Devanagari logotype and professional photo are retained assets.

## Evidence on Hand

- Professional headshot: `viz/public/photo.jpg`
- Logotype: `viz/public/logo.jpg`
- Career evidence spanning 2007–2026 across IBM, Exeter, Amazon, Philips India, Philips North America, and a parallel independent service lane
- 20 attributed LinkedIn recommendations, 16 formal awards, 12 public recognitions, and a larger local corpus of informal feedback
- 90 facilitated sessions with 1,183 feedback responses, plus 13 voluntary college sessions with 494 student responses
- Quantified delivery and business outcomes, with resume-originated figures labeled self-reported unless independently corroborated
- Two USPTO patents and evidence of continued AI-native, regulated-software, teaching, and community work

## Product Principles

1. **Evidence over claims** — assertions carry evidence tiers and explicit caveats; unsupported certainty is avoided
2. **Whole person, not just professional** — social impact, volunteering, and community building are first-class alongside technical achievements
3. **Focused depth** — visitors choose among eight perspectives while private raw artifacts stay outside the public experience
4. **Living system** — the portfolio is a product of the knowledge layer, not a handcrafted static site

## Accessibility & Inclusion

WCAG 2.1 AA remains the target. The current atlas provides semantic sections and labeled SVGs, visible focus treatment, `aria-current`, arrow/Home/End desktop navigation, a labeled mobile selector, horizontal-scroll labels for dense visuals, reduced-motion behavior, and single-column responsive fallbacks.

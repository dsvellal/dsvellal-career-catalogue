# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

React + TypeScript + Vite + D3. Single-page application with hash-addressable view navigation and namespaced CSS (no CSS-in-JS). Static deployment target.

## Users

Broad professional audience: hiring managers evaluating senior/principal engineering leadership roles, engineering peers and collaborators, conference organizers, community members, and anyone seeking to understand Dattatreya (Datta) Vellal's professional identity and impact. Viewed on desktop and mobile, often from a shared link or search result.

## Product Purpose

A living digital portfolio and professional identity system — not a static resume site. It makes a career spanning 20 calendar years (2007–2026), quantified impact, peer validation, learning, and community contribution explorable and verifiable in one place. Backed by a structured knowledge layer that can generate tailored outputs (resumes, cover letters, weekly summaries) from rich contextual data.

## Positioning

Combines two differentiators no standard resume or LinkedIn profile offers: (1) a structured knowledge system / digital twin architecture that enables AI-powered tailored outputs, and (2) unusual evidence depth—quantified impact across four employers, a curated 20-item recommendation archive, longitudinal assessments and reviews, participant feedback, a full talks inventory, and a knowledge graph mapping skills across eras. Selection bias, missing coverage, attribution boundaries, and superseded metrics are disclosed as part of the product rather than hidden.

## Operating Context

Eight evidence-led routes: Executive Brief, Leadership, Career Journey, Trust, Innovation & Value, Learning, Community & Service, and Data Room. The former generic Impact route is removed because it duplicated evidence owned by the thematic pages; legacy `#/impact` links resolve to Innovation & Value. Every route carries Datta's portrait; the seven narrative routes lead with two to four curated conclusions, while Data Room begins with intentional search rather than an inventory wall. On mobile, the executive answer precedes a compact portrait so identity remains present without delaying meaning.

Schema v3 adds a presentation-specific story layer: 23 impact-first blocks own 51 claims exactly once, while four corpus-quality or privacy-sensitive claims remain audit-only. The underlying projection still contains 55 claims joined to 36 source capsules by 82 first-class support records, with 18 methods, 11 reviewed relationships, 30 caveats, and 8 retained conflicts. Those records support the story; they are no longer the first thing an executive visitor must parse.

## Capabilities and Constraints

- Single-page app with stable hash routes for eight primary pages plus claim, source, and method records
- All data is static JSON — no backend API
- One impact per story block: a short heading, a human meaning statement, a bounded evidence signal, and one evidence action
- **Inspect claim** combines why the conclusion matters, its evidence, derivation method, scope, and folded supporting-claim traceability
- Explicit relationship records express only reviewed longitudinal propositions; interpreted links are visually distinct and never inferred from array order, keywords, or raw graph co-occurrence
- Source provenance, support directness, and claim state are independent; formulas, inputs, caveats, conflicts, and attribution remain attached to each claim
- A searchable Data Room exposes 23 curated conclusions, a 34-record source closure, 16 story-linked methods, and 10 story-linked relationships; the source closure includes direct support, method inputs, documentary records, and reconciliation sources, while methods and relationships begin collapsed
- Professional portrait appears once in every primary route hero, with a compact global-header thumbnail as the persistent identity anchor
- Executive data-observatory visual language: navy framing, warm reading surfaces, cobalt/teal/copper/violet signals, restrained motion, responsive and print treatments
- Production builds disable Vite's `public/` directory; raw evidence is not copied into the deployable bundle

## Brand Commitments

The visual identity combines a deep navy analytical frame with warm reading surfaces, sharp typographic hierarchy, restrained data motion, and cobalt/teal/copper/violet semantic accents. It should feel like an executive briefing room with an open audit trail—not a dashboard template or a self-promotional microsite. The Devanagari logotype and professional photo are retained assets.

## Evidence on Hand

- Professional headshot: `viz/public/photo.jpg`
- Logotype: `viz/public/logo.jpg`
- Career evidence spanning 2007–2026 across IBM, Exeter, Amazon, Philips India, Philips North America, and a parallel independent service lane
- A curated 20-item attributed recommendation archive across four employers and ten recommendation years; it is explicitly not presented as an unbiased survey
- 88 nonduplicate post-event professional feedback/interaction datasets with 1,050 response rows, plus two separately reported pre-event audience surveys with 133 rows
- 13 student-feedback forms with 494 response rows, alongside a delivery ledger of 50 talks and 3,732 participant instances; presenter ratings stay on their original 5- and 10-point scales, and recommendation likelihood is not relabelled as NPS
- Quantified delivery and business outcomes, with exact scope and attribution: Datta, team, program, or portfolio; potential value remains separate from realized value
- Patent/invention records and evidence of continued AI-native, regulated-software, teaching, and community work
- Ten annual community-service ledgers recording ₹1,972,381 distributed; donor identities and private account details remain withheld

## Product Principles

1. **Traceable claims over isolated numbers** — every factual headline resolves to support and, where applicable, a versioned method
2. **Separate fact from interpretation** — observed, calculated, and interpreted claims remain distinguishable, as do provenance and support strength
3. **Whole person, not just professional** — social impact, volunteering, learning, criticism, and community building are first-class alongside technical achievements
4. **Progressive depth** — the first read is concise; explanation and source-level detail remain one deliberate action away
5. **Transparent limits at the right depth** — the executive surface stays positive and focused; definitions, attribution, reconciliation, and non-causal boundaries remain available in Inspect Claim and source/method records
6. **Living system** — the portfolio is compiled from the knowledge layer, not maintained as free-floating factual JSX

## Accessibility & Inclusion

WCAG 2.1 AA remains the target. Primary navigation, Inspect Claim disclosures, search/filter controls, claim links, source links, and method links must be keyboard operable with visible focus and semantic labels. Motion respects reduced-motion preferences; relationship views retain a readable list representation; mobile layouts preserve the same evidence depth without horizontal page overflow.

The schema-v3 release was verified on 2026-08-07 across all eight routes at desktop and 390 px mobile widths. Every route rendered one primary portrait plus the global header thumbnail, no mobile route exceeded the viewport width, and desktop/mobile screenshots were reviewed. Public navigation and direct hashes expose only story-linked claims, sources, methods, and relationships; audit-only hashes resolve to a generic evidence invitation. Axe WCAG A/AA checks on the Brief and Inspect Claim returned zero violations; gradient-background contrast remained a manual visual check. The full repository gate passed with 274 tests, 2 skips, a successful production build, and an accepted privacy scan.

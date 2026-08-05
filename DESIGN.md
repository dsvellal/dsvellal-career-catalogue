---
name: Datta Vellal Portfolio
description: Professional identity portfolio rendered as architectural technical drawings
colors:
  vellum: "#f7f4ed"
  vellum-warm: "#f0ece3"
  ink-primary: "#1a2233"
  ink-secondary: "#3d4a5c"
  ink-muted: "#6b7280"
  construction-blue: "#a8c4d4"
  accent-vermillion: "#c44125"
  era-ibm: "#2563a8"
  era-amazon: "#0d7a52"
  era-philips: "#b84c1a"
  era-exeter: "#9a6b00"
  era-independent: "#6b46b0"
  border: "#d4cfc4"
  border-strong: "#b8b2a5"
typography:
  display:
    fontFamily: "'Barlow Condensed', sans-serif"
    fontSize: "clamp(32px, 6vw, 80px)"
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: "-0.04em"
  body:
    fontFamily: "'Barlow', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
  annotation:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "10px"
    fontWeight: 500
    letterSpacing: "0.06em"
rounded:
  none: "0"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "48px"
components:
  nav-tab:
    textColor: "{colors.ink-muted}"
    typography: "{typography.display}"
    padding: "0 16px"
  nav-tab-active:
    textColor: "{colors.ink-primary}"
  filter-button:
    backgroundColor: "{colors.vellum}"
    textColor: "{colors.ink-secondary}"
    padding: "6px 14px"
  filter-button-active:
    backgroundColor: "{colors.ink-primary}"
    textColor: "{colors.vellum}"
  impact-card:
    backgroundColor: "#ffffff"
    padding: "28px 24px"
  badge:
    textColor: "{colors.ink-muted}"
    padding: "2px 6px"
---

# Design System: Datta Vellal Portfolio

## Overview

**Creative North Star: "The Blueprint Specification"**

This portfolio is rendered as an architectural drawing sheet set — the visual language engineers use to specify designed systems. Every element inherits the precision, economy, and authority of technical documentation: thin ruled lines carry hierarchy, monospace annotations provide measurement context, and warm vellum ground establishes the physical substrate of drafting paper.

The design rejects the dark-theme SaaS portfolio default, the card-grid template, rounded corners, and decorative glass/blur. It replaces them with orthogonal composition, explicit line weights as a hierarchy system, and typography that reads as engineered signage rather than marketing.

The surface operates in **Experience** mode: the work itself leads from the first viewport. The interface recedes; the evidence system is the experience.

**Key Characteristics:**
- Warm light theme derived from physical drafting paper
- Zero border-radius throughout — all corners are right angles
- Three-tier line weight system (0.5px construction, 1px standard, 2px section)
- Monospace annotations for metadata, dates, and labels
- Condensed industrial grotesque for display headings
- Era-coded color system preserved from the data model

## Colors

A restrained palette of architectural ink on vellum, with vermillion for revision marks and active states.

### Primary
- **Blueprint Ink** (#1a2233): All primary text, display headings, and section borders. Deep blue-black that reads as technical pen ink on paper.
- **Vermillion** (#c44125): Active states, accent indicators, revision marks. The engineer's red correction pen.

### Secondary
- **Construction Blue** (#a8c4d4): Section labels, guideline annotations, ghost elements. The non-reproducing blue pencil of architectural drafting.

### Neutral
- **Vellum** (#f7f4ed): Page ground. Warm off-white that reads as drafting paper.
- **Vellum Warm** (#f0ece3): Secondary surfaces and hover states.
- **Border** (#d4cfc4): Standard rule lines.
- **Border Strong** (#b8b2a5): Emphasized rules and hover states.

### Categorical (Era Colors)
- **IBM Blue** (#2563a8): IBM era indicators
- **Amazon Green** (#0d7a52): Amazon era indicators
- **Philips Orange** (#b84c1a): Philips era indicators
- **Exeter Gold** (#9a6b00): Exeter era indicators
- **Independent Purple** (#6b46b0): Community/volunteer era indicators

## Typography

Three faces, each earned by its role:

### Display — Barlow Condensed
Industrial grotesque inspired by California highway signage. Used for all headings, stat values, and navigation labels. Weights 600–800. Always uppercase in navigation, mixed case in content headings.

### Body — Barlow
Proportional companion to the display face. All paragraph text, descriptions, and interactive content. Weights 300–600.

### Annotation — JetBrains Mono
Monospaced face used exclusively for measurements, dates, metadata labels, badge text, and dimension annotations. This is NOT decorative monospace — it is earned by its function (code, data, measurement). Weight 400–500, always uppercase with wide letter-spacing (0.04–0.1em).

## Layout

### Grid and Composition
- Max content width: 1400px, centered
- Page padding: 48px horizontal (16px on mobile)
- No rounded containers — all panels are orthogonal
- Grid gaps use 0px with borders separating cells (drawing-sheet style)
- Two-column layouts use thin vertical rules as dividers

### Spacing Rhythm
- More space above headings than below (architectural convention)
- Tight groups within components, generous separation between them
- Section headers carry a bottom border acting as a section break line

### Responsive
- Single breakpoint at 900px
- Columns collapse to single-column with horizontal borders becoming vertical stacking
- Navigation becomes horizontally scrollable
- Photo moves above text on mobile

## Elevation & Depth

Flat. No ambient shadows. The single elevation device is the **offset shadow** on the hero photo: `8px 8px 0 rgba(168, 196, 212, 0.3)` — a construction-blue offset that reads as a blueprint elevation indicator. This shadow appears nowhere else.

Tooltips use the same offset: `4px 4px 0 rgba(168, 196, 212, 0.3)`.

Depth is communicated through line weight and fill, never through blur or ambient shadow.

## Shapes

**Zero border-radius.** This is the world's defining geometric constraint. Every container, button, badge, input, card, and panel uses sharp right-angle corners. This is non-negotiable — any border-radius would break the technical drawing commitment.

Shapes are defined by their borders:
- Section boundaries: 2px solid ink-primary
- Standard containers: 1px solid border
- Construction/ghost elements: 0.5px solid construction-blue or dashed

## Components

### Navigation
Title-block strip at top. 2px bottom border (section weight). Tabs use font-display uppercase with vermillion underline on active. No background change on active — only the border indicator.

### Section Header
Functions as a drawing title block. Monospace section label in construction-blue, followed by display heading, followed by body subtitle. Bottom border separates from content.

### Filter Buttons
Rectangular (no radius). Monospace text. Active state inverts: ink-primary background with vellum text. No pill shape.

### Badges/Tags
Thin 1px border, monospace text, no background fill on default state. Category badges use border-color to indicate their category.

### Grid Cells
Items within a grid share borders (no gaps). Cells separated by 1px rules. Hover state changes background to vellum-warm. This replaces the card-grid pattern.

### Expandable Details
Triggered by click. Content animates in via max-height transition. Toggle text uses vermillion accent. No chevron icons — text indicators only ("→ read more" / "↑ collapse").

## Do's and Don'ts

### Do
- Use line weight to communicate hierarchy (2px > 1px > 0.5px)
- Keep all corners sharp (0 border-radius)
- Use monospace exclusively for measurements, dates, and metadata
- Let the grid lines do the visual work — fewer fills, more structure
- Use vermillion sparingly as the single accent color for active/revision states
- Write labels in uppercase monospace with wide letter-spacing

### Don't
- Add border-radius to any element
- Use colored backgrounds for badges (use border-color instead)
- Add ambient shadows or blur effects
- Use gradient text or decorative glass effects
- Add kickers or eyebrows above headings
- Use rounded pill shapes for buttons or filters
- Use emoji or unicode glyphs as icons
- Apply the hero-metric template (big number + small label as the page pattern)

# How Microsoft Engineers with AI

A slide deck on how Microsoft teams plan, build, test, operate and measure software as agents take on more of the work. It uses the visual template of [The Autonomous SDLC](../Pres-GHCP_AI_SDLC/) deck.

This folder hosts the presentation as a static, self-contained HTML slide deck that can be viewed directly in a browser.

## What this presentation covers

1. **Agenda / Overview**: the four questions the deck addresses:
   - Spec-driven development with product and engineering together
   - AI in testing and operations
   - Measuring productivity beyond DORA
   - How Microsoft plans and prioritizes across many teams
2. **Context: The Long View**: from AI-assisted development to AI that runs the SDLC, with agents working across every stage from intent to production.
3. **Spec-Driven Development**: product and engineering share one checkpointed spec. The flow runs requirements → specification → AI generation → validation, with clear roles for product, engineering, AI and validation, and humans owning acceptance criteria, impact metrics and the ship decision.
4. **AI in Testing & Operations**: AI across the delivery loop, not just pair programming. It covers review and test-gap analysis before merge, validation and triage at deployment, and investigation and guidance in operations. Human oversight applies at every gate, and the slide closes with five recommended practices.
5. **Measuring Productivity Beyond DORA**: DORA is necessary but not sufficient. It sets DORA, SPACE, DevEx and GitHub's [Engineering System Success Playbook (ESSP)](https://assets.ctfassets.net/wfutmusr1t3h/59IWCIRvx0KfHbh6B7bv62/d9f55b94ab43fe91e9ed183d73882954/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf) side by side, highlights PR to Customer (PR2C), and gives example Speed, Ease and Quality metrics.
6. **GitHub's framework**: the metrics GitHub tracks across developer happiness, quality and velocity, all leading to business outcomes.
7. **EngThrive**: the metrics Microsoft's DevEx initiative tracks for Satisfaction, Collaboration and Efficiency.
8. **The evidence**: why those EngThrive metrics were chosen.
9. **Planning at Scale**: aligned autonomy through a nested cadence (sprint → plan → season → strategy), small full-stack teams, the bug cap and nested OKRs, with five recommended practices.

Slides 6–8 are adapted from the [Copilot KPIs](../Pres-GHCP_KPIs/) deck and restyled for this theme.

Navigate with the arrow keys, the on-screen ‹ › buttons, or the dots in the footer.

## Viewing the presentation

The presentation is published as part of the IP-Index GitHub Pages site and automatically deployed from the `main` branch by the root `.github/workflows/deploy-pages.yml` workflow. It is linked from a tile on the site's landing page, or open `ms-engineering-practices-deck.html` directly to view it locally.

## Repository structure

- `ms-engineering-practices-deck.html`: the presentation deck (self-contained, with inline SVG icons and no external assets). Each slide is a `<section class="slide">` block; add a section to add a slide, and the navigation dots and counter update automatically.

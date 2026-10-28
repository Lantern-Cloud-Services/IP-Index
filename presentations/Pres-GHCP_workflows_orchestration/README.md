# Copilot Champions Deep Dive Session 3

A slide-deck presentation reviewing the agentic primitives, the workflows and orchestrations that make AI accurate and scalable across the SDLC, and the frontier problems we're solving next.

This folder hosts the presentation as a static, self-contained HTML slide deck that can be viewed directly in a browser.

## What this presentation covers

The deck is organized into three main sections, navigable via the on-screen agenda:

1. **Primitives Review**
   - Agent configs: persistent instructions (`copilot-instructions.md`), custom agents, skills, MCP, and subagents
   - The agentic primitives that persist context across sessions

2. **Workflows and Orchestrations**
   - Quality automation workflows (design, spec, implement, validate)
   - Deterministic controls: pairing probabilistic AI with deterministic guardrails
   - Feedback loops and the agentic flywheel
   - Orchestration patterns and examples, including lightweight orchestration and rubber-duck review agents

3. **The Frontier**
   - The SDLC agentic frontier: where things are going and the new problems we're solving

## Viewing the presentation

The presentation is published as part of the IP-Index GitHub Pages site and automatically deployed from the `main` branch by the root `.github/workflows/deploy-pages.yml` workflow. It is linked from a tile on the site's landing page, or open `ghcp_practices_3_cli.html` directly to view it locally.

## Repository structure

- `ghcp_practices_3_cli.html` — the presentation deck

# Copilot Champions Deep Dive

A slide-deck presentation exploring how to use GitHub Copilot effectively in real-world, brownfield codebases — covering context-building, agent configuration, and iteration patterns that improve day-to-day AI-assisted development.

This repository hosts the presentation as a static, self-contained HTML slide deck. It is published via GitHub Pages so it can be viewed directly in a browser and shared externally.

## What this presentation covers

The deck is organized into three main sections, navigable via the on-screen agenda:

1. **Brownfield Modernization**
   - Creating spec definitions and design documentation
   - Building context through codebase introspection (discover, document, encode, validate)
   - Safe collaboration patterns for legacy code (incremental adoption, guardrails, risk mitigation)

2. **Custom Instructions and Agent Files**
   - Agent configuration options
   - The "agentic primitives" that persist context across sessions

3. **Iteration Patterns and Best Practices**
   - The agentic flywheel and quality automation workflows
   - Spec-driven development
   - Model selection and the biggest levers for effective results
   - Designing agentic workloads (the right mode, model, and context for each stage)
   - Prompting techniques (precision, imperative goals, providing known context) and an example of prompt discipline
   - The Research → Plan → Implement workflow
   - Power-user guidance (thinking in code, CLIs vs. MCPs, shell output tips, and more)
   - Session roadmap (Sessions 0-3: org setup, foundations, agentic primitives, workflows and orchestration)

## Viewing the presentation

The presentation is published as part of the IP-Index GitHub Pages site and automatically deployed from the `main` branch by the root `.github/workflows/deploy-pages.yml` workflow. It is linked from a tile on the site's landing page, or open `ghcp_champions_cli.html` directly to view it locally.

An additional reference deck on GitHub Copilot's included models (`assets/copilot-models-cli.html`) is also included as supporting material.

## Repository structure

- `ghcp_champions_cli.html` — the main presentation deck
- `ghcp_champions_internal.html` - a six-slide internal briefing cut of the deck (Agent Configs, Flywheel, Quality Automation Workflows with multi-agent orchestration, Fabric + Foundry + GitHub value proposition with GitHub as the agentic platform for software development, Session Roadmap, "Powerpoint what now?" closer)
- `index.html` — redirects to the main presentation deck (used as the GitHub Pages entry point)
- `assets/` — supporting assets and the reference deck on Copilot models
- `ghcp_champions_internal.html` is kept in the repo but excluded from Pages by the root workflow
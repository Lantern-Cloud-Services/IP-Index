# GitHub Copilot Sandboxing and Spec Driven Development

A slide-deck presentation on safely delegating implementation work to agents with GitHub Copilot sandboxes, and on using spec driven development to keep requirements, code, and tests in sync.

This folder hosts the presentation as a static, self-contained HTML slide deck that can be viewed directly in a browser.

## What this presentation covers

The deck is organized into two main sections, navigable via the on-screen agenda:

1. **Copilot Sandbox**
   - The Coding Agent sandbox: the temporary GitHub Actions–powered environment the agent uses to clone, change, test, and commit before it is discarded
   - Local sandboxing across the Copilot CLI, the Copilot app, and cloud sessions dispatched locally

2. **Spec Driven Development**
   - Creating spec definitions and design documentation for existing codebases
   - Safe collaboration patterns for legacy code (incremental adoption, guardrails, risk mitigation)
   - What a good specification contains
   - The SDD workflow with Copilot
   - Key principles and common mistakes
   - Resources: video guides on GitHub Spec Kit

## Viewing the presentation

The presentation is published as part of the IP-Index GitHub Pages site and automatically deployed from the `main` branch by the root `.github/workflows/deploy-pages.yml` workflow. It is linked from a tile on the site's landing page, or open `ghcp_sandbox_sdd_cli.html` directly to view it locally.

## Repository structure

- `ghcp_sandbox_sdd_cli.html` — the presentation deck
- `assets/` — supporting images used by the deck

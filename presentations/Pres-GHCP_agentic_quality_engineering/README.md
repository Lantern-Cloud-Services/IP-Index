# Agentic Quality Engineering

A single-page infographic, **From Code Changes to Continuously Better Software**, describing a progressively agentic testing model that detects changes, generates and runs tests, and learns over time.

This folder hosts the infographic as a static, self-contained HTML page that can be viewed directly in a browser. It has no slides; it is one responsive page.

## What it covers

1. **Detect Feature Changes** (Change Analysis Agent): triggered by a PR or commit; analyzes code changes and their impact using repo context, docs, APIs, and past issues.
2. **Generate Tests Automatically** (Test Planning Agent): creates a semantic test plan, identifies missing scenarios, and prioritizes by risk and impact.
3. **Create Test Scripts Automatically** (Test Implementation Agent): writes unit, integration, API, or UI tests that follow project standards, adding only missing tests.
4. **Execute Tests Automatically** (CI/CD + Test Execution): runs unit, integration, E2E, security, and performance tests in GitHub Actions and diagnoses failures.
5. **Continuously Improve Testing Coverage** (Coverage Improvement Agent): analyzes coverage, defects, and production signals, finds gaps and flaky tests, and proposes new tests via PRs.

A **feedback loop** feeds failures, coverage gaps, and real-world issues back into the first step. The model is built on **GitHub Copilot**, **GitHub Actions**, and **Microsoft Foundry**, with business outcomes of higher software quality, faster delivery, lower risk, and a self-improving testing system.

## Viewing the infographic

The page is published as part of the IP-Index GitHub Pages site and automatically deployed from the `main` branch by the root `.github/workflows/deploy-pages.yml` workflow. It is linked from a tile on the site's landing page, or open `agentic_quality_engineering.html` directly to view it locally.

## Repository structure

- `agentic_quality_engineering.html` — the infographic page (all icons are inline SVG; no external assets)

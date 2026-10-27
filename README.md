# Lantern Cloud Services Presentations

A single home for Lantern Cloud Services presentation decks. Every deck lives in its own folder under
[`presentations/`](presentations/), and the site is published to GitHub Pages with a landing page that
shows one tile per presentation.

- **Live site:** http://verbose-broccoli-pj8j68q.pages.github.io/ (private Pages; requires GitHub
  sign-in with repo access. The current URL is always shown under Settings > Pages.)
- **Offline:** clone the repo and open `index.html` in a browser. All links are relative, so it works
  the same from disk as it does on Pages.

## Presentations

| Presentation | Folder | Topics |
|---|---|---|
| GitHub Copilot Sandboxing and Spec Driven Development | [`Pres-GHCP_sandbox_sdd`](presentations/Pres-GHCP_sandbox_sdd/) | Coding agent and local sandboxes, spec driven development workflow |
| Copilot KPIs: Measuring What Matters | [`Pres-GHCP_KPIs`](presentations/Pres-GHCP_KPIs/) | Outcome-based KPIs, delivery health, developer effectiveness, SPACE |
| Copilot Champions Deep Dive Session 1 | [`Pres-GHCP_champions_brownfield_primitives_iterations`](presentations/Pres-GHCP_champions_brownfield_primitives_iterations/) | Brownfield modernization, agent configuration, agentic primitives, iteration patterns |

### Not yet migrated

These decks are still hosted in their own repositories and will move here over time:

- Copilot Best Practices, Governance and GitHub Actions:
  [repo](https://github.com/Lantern-Cloud-Services/Pres-GHCP_BestPractices_Governance_Optimization_CICD),
  [live](http://www.lanterncloudservices.com/Pres-GHCP_BestPractices_Governance_Optimization_CICD/)

## Repository layout

```
index.html                           # landing page with one tile per presentation
presentations/<name>/                # one self-contained folder per deck (HTML + assets)
.github/workflows/deploy-pages.yml   # publishes index.html + presentations/ to Pages on push to main
```

There is no build step. The workflow copies `index.html` and `presentations/` into the Pages artifact,
removes `README.md` files and any internal-only decks, and deploys.

## Adding a presentation

1. Add a folder under `presentations/` containing the deck's HTML and assets. Decks should be
   self-contained and use relative links. No per-presentation `.github/` workflow is needed.
2. In `index.html`, copy an existing `<article class="tile">` block and update the title, date,
   description, tags and links (relative paths such as `presentations/<name>/deck.html`).
3. Add a row to the [Presentations](#presentations) table above.
4. Open `index.html` in a browser to check the tile and links, then push to `main` to publish.

To keep an internal-only deck in the repo but off the public site, add an `rm` line for it in the
workflow's "Prepare site" step.

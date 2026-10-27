# Engagement Index

This repository serves as a master index of customer deliveries and live content.

It is also deployed to GitHub Pages: the landing page is a tile index of every presentation in
[`presentations/`](presentations/), and each tile links to that presentation's sub-page.

## Site structure

```
index.html                           # landing page (open directly in a browser, or via GitHub Pages)
presentations/<name>/                # one folder per presentation, linked from a tile in index.html
.github/workflows/deploy-pages.yml   # publishes index.html + presentations/ to Pages on push to main
```

There is no build step: `index.html` is a plain static page with relative links, so it works the
same when opened from disk as it does on GitHub Pages.

### Adding a presentation

1. Add a folder under `presentations/` containing the deck's HTML and assets (no per-presentation
   `.github/` workflow is needed).
2. In `index.html`, copy an existing `<article class="tile">` block and update the title, date,
   description, tags and links (relative paths such as `presentations/<name>/deck.html`).
3. Open `index.html` in a browser to check it.

`README.md` files are not published. To keep an internal-only deck out of Pages, add an `rm` line
for it in the workflow's "Prepare site" step.
## Entries

### 07/02/2026 - Hannover - Copilot Best Champions

- GitHub: https://github.com/Lantern-Cloud-Services/Pres-GHCP_champions_brownfield_primitives_iterations
- Live Content: http://www.lanterncloudservices.com/Pres-GHCP_champions_brownfield_primitives_iterations/ghcp_champions_cli.html


### 06/19/2026 - WR Berkley - Copilot Best Practices and GitHub Actions

- GitHub: https://github.com/Lantern-Cloud-Services/Pres-GHCP_BestPractices_Governance_Optimization_CICD
- Live Content: http://www.lanterncloudservices.com/Pres-GHCP_BestPractices_Governance_Optimization_CICD/

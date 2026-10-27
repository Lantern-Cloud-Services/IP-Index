# Engagement Index

This repository serves as a master index of customer deliveries and live content.

It is also deployed to GitHub Pages: the landing page is a tile index of every presentation in
[`presentations/`](presentations/), and each tile links to that presentation's sub-page.

## Site structure

```
.github/workflows/deploy-pages.yml   # builds and deploys the whole site on push to main
scripts/build_site.py                # generates _site/ (landing page + copied presentations)
site/index.template.html             # landing page template ({{TILES}}, {{COUNT}})
presentations/<name>/                # one folder per presentation -> /presentations/<name>/
presentations/<name>/presentation.json  # optional tile metadata
```

### Adding a presentation

1. Add a folder under `presentations/` containing the deck's HTML and assets (no per-presentation
   `.github/` workflow is needed).
2. Add a `presentation.json` describing the tile:

   ```json
   {
     "title": "Deck title",
     "audience": "Customer / event",
     "date": "YYYY-MM-DD",
     "description": "Short summary shown on the tile",
     "tags": ["optional", "labels"],
     "decks": [{ "label": "Presentation", "path": "deck.html" }],
     "exclude": ["internal-only.html"]
   }
   ```

   The first entry in `decks` is the tile's main link; extra entries show as secondary links.
   Files in `exclude`, dot-files, `README.md` and `presentation.json` are not published.
   Without `presentation.json`, the folder name is used as the title and the tile links to `index.html`.
3. Preview locally: `python scripts/build_site.py && python -m http.server 8000 -d _site`.

Tiles are sorted newest-first by `date`. The build fails if a deck path is missing or excluded.

## Entries

### 07/02/2026 - Hannover - Copilot Best Champions

- GitHub: https://github.com/Lantern-Cloud-Services/Pres-GHCP_champions_brownfield_primitives_iterations
- Live Content: http://www.lanterncloudservices.com/Pres-GHCP_champions_brownfield_primitives_iterations/ghcp_champions_cli.html


### 06/19/2026 - WR Berkley - Copilot Best Practices and GitHub Actions

- GitHub: https://github.com/Lantern-Cloud-Services/Pres-GHCP_BestPractices_Governance_Optimization_CICD
- Live Content: http://www.lanterncloudservices.com/Pres-GHCP_BestPractices_Governance_Optimization_CICD/

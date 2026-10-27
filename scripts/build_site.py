"""Build the GitHub Pages site for the presentation index.

Scans ``presentations/<name>/`` folders, copies each into ``<out>/presentations/<name>/``
and renders a tile-based landing page at ``<out>/index.html``.

Each presentation folder may contain an optional ``presentation.json``:

    {
      "title": "Deck title",
      "audience": "Customer / event",
      "date": "YYYY-MM-DD",
      "description": "Short summary shown on the tile",
      "tags": ["optional", "labels"],
      "decks": [{"label": "Presentation", "path": "deck.html"}],
      "exclude": ["files/or/folders/not/to/publish.html"]
    }

Without it, the folder name is used as the title and the tile links to ``index.html``.
Dot-files/folders, README.md and presentation.json are never published.

Usage: python scripts/build_site.py [--out _site]
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESENTATIONS_DIR = ROOT / "presentations"
TEMPLATE = ROOT / "site" / "index.template.html"
ALWAYS_EXCLUDED = {"README.md", "presentation.json"}


def load_metadata(folder: Path) -> dict:
    meta_file = folder / "presentation.json"
    meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
    meta.setdefault("title", folder.name.replace("_", " ").replace("-", " "))
    meta.setdefault("description", "")
    meta.setdefault("audience", "")
    meta.setdefault("date", "")
    meta.setdefault("tags", [])
    meta.setdefault("exclude", [])
    if not meta.get("decks"):
        meta["decks"] = [{"label": "Open", "path": "index.html"}]
    return meta


def copy_presentation(src: Path, dest: Path, exclude: list[str]) -> None:
    excluded = {(src / e).resolve() for e in exclude}

    def ignore(directory: str, names: list[str]) -> set[str]:
        skipped = set()
        for name in names:
            path = (Path(directory) / name).resolve()
            if name.startswith(".") or path in excluded:
                skipped.add(name)
            elif Path(directory).resolve() == src.resolve() and name in ALWAYS_EXCLUDED:
                skipped.add(name)
        return skipped

    shutil.copytree(src, dest, ignore=ignore)


def validate(folder: Path, meta: dict) -> list[str]:
    errors = []
    excluded = {(folder / e).resolve() for e in meta["exclude"]}
    for deck in meta["decks"]:
        target = (folder / deck["path"]).resolve()
        if not target.is_file():
            errors.append(f"{folder.name}: deck '{deck['path']}' does not exist")
        elif target in excluded:
            errors.append(f"{folder.name}: deck '{deck['path']}' is excluded from publishing")
    return errors


def render_tile(slug: str, meta: dict) -> str:
    e = lambda s: html.escape(str(s), quote=True)
    base = f"presentations/{slug}/"
    primary, *others = meta["decks"]
    meta_line = " &middot; ".join(e(x) for x in (meta["date"], meta["audience"]) if x)
    tags = "".join(f'<span class="tag">{e(t)}</span>' for t in meta["tags"])
    extra = "".join(
        f'<a class="secondary" href="{e(base + d["path"])}">{e(d["label"])}</a>' for d in others
    )
    return f"""
      <article class="tile" data-search="{e(' '.join([meta['title'], meta['audience'], meta['description'], *meta['tags']]).lower())}">
        <a class="tile-main" href="{e(base + primary['path'])}">
          <p class="meta">{meta_line}</p>
          <h2>{e(meta['title'])}</h2>
          <p class="desc">{e(meta['description'])}</p>
          <div class="tags">{tags}</div>
          <span class="cta">{e(primary['label'])} &rarr;</span>
        </a>
        {f'<div class="links">{extra}</div>' if extra else ''}
      </article>"""


def build(out: Path) -> int:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    folders = sorted(p for p in PRESENTATIONS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))
    entries, errors = [], []
    for folder in folders:
        meta = load_metadata(folder)
        errors += validate(folder, meta)
        copy_presentation(folder, out / "presentations" / folder.name, meta["exclude"])
        entries.append((folder.name, meta))

    if errors:
        print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
        return 1

    entries.sort(key=lambda item: (item[1]["date"], item[0]), reverse=True)
    tiles = "".join(render_tile(slug, meta) for slug, meta in entries) or '<p class="empty">No presentations yet.</p>'
    page = TEMPLATE.read_text(encoding="utf-8").replace("{{TILES}}", tiles).replace("{{COUNT}}", str(len(entries)))
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / ".nojekyll").touch()

    print(f"Built {len(entries)} presentation(s) into {out}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="_site", help="output directory (default: _site)")
    args = parser.parse_args()
    out_dir = Path(args.out)
    sys.exit(build(out_dir if out_dir.is_absolute() else ROOT / out_dir))

# Source for ivonnezca.github.io

`index.html` (one folder up) is generated from these files. Folders starting with `_` are not published.

- `template.html` – page text, layout and styles
- `papers.py` – research themes and selected papers
- `img/` – photos (embedded into index.html at build time)

To rebuild: `cd _source && python3 build.py && cp index.html ../index.html`

The group site (swansea-cosmo-gravity.github.io) reuses this page's stylesheet and photos.

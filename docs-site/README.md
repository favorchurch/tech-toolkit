# HTML Documentation Edition

This folder is the build source for a static HTML website that renders **every** Markdown guide and CSV template from the same repository.

Run from the repository root:

```sh
python3 -m pip install -r docs-site/requirements.txt
python3 docs-site/build.py
```

The resulting `public/` directory can be served by any static file server. The browser experience supports desktop and mobile, inline guide search (even from local files), print layouts, original-source links, previous/next guide navigation, and downloadable blank CSV templates.

The Markdown files remain the canonical editable source; **do not edit generated HTML**. The site generator renders Mermaid diagrams as SVG where Graphviz `dot` is available, otherwise shows readable process steps and the full diagram source as a fallback. The site uses built-in system font fallbacks without redistributing Favor proprietary fonts or graphics.

For Vercel: build command `python3 -m pip install -r docs-site/requirements.txt && python3 docs-site/build.py`; output directory `public`; framework Other.

## Security

Only commit public-safe guides. Never include actual venue configurations, private repository URLs, real credentials, network maps, personal data, or confidential screenshots in the public site or search index. Public Markdown is rendered with raw HTML disabled and unsafe URL schemes blocked by MarkdownIt defaults.

## Complete offline HTML edition

[Download the full offline HTML website](favor-tech-toolkit-html.tar.xz) (compressed TAR/XZ archive).

The archive contains all 40 guide/template pages, homepage, navigation, search index, styles, diagrams, and downloads. Extract the archive into a folder, then open `index.html` in your browser. On macOS or Linux, run `tar -xf favor-tech-toolkit-html.tar.xz`. This is a snapshot; regenerate with `python3 docs-site/build.py` whenever the canonical Markdown changes.

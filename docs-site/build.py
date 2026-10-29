#!/usr/bin/env python3
"""Build the Favor Tech toolkit's entirely static, browsable HTML edition.

The repository's .md and .csv files are always canonical. This generator
performs a fresh render at build-time; it does not maintain a second copy.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from markdown_it import MarkdownIt
except ImportError:
    sys.exit('Install requirements first: python3 -m pip install -r docs-site/requirements.txt')

REPO = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve().parent
EXCLUDED_DIRS = {'.git', '.github', '.vercel', 'node_modules', 'public', 'dist', 'venv', '.venv', 'docs-site'}
TITLE_OVERRIDES = {
    'README.md': 'Toolkit overview',
    'playbooks/internet/README.md': 'Internet team',
    'playbooks/website/README.md': 'Website team',
    'playbooks/app-development/README.md': 'App development',
    'launch/README.md': 'Campus launch',
    'training/README.md': 'Training & certification',
    'templates/README.md': 'Templates & forms',
    'SECURITY.md': 'Security reporting',
    'CONTRIBUTING.md': 'Contributing',
}
GROUPS = [
    ('Start here', ['README.md','docs/START-HERE.md','docs/CHARTER.md','docs/GOVERNANCE.md','docs/SECURITY.md','docs/COVERAGE.md','docs/SOURCES.md','docs/ROADMAP.md','docs/ADOPTION-GUIDE.md','SECURITY.md','CONTRIBUTING.md']),
    ('Internet team', ['playbooks/internet/README.md','playbooks/internet/SUNDAY-SERVICE.md','playbooks/internet/INCIDENTS.md','playbooks/internet/EQUIPMENT.md']),
    ('Website team', ['playbooks/website/README.md','playbooks/website/PUBLISHING.md','playbooks/website/QA.md','playbooks/website/PLATFORM-OPS.md']),
    ('App development', ['playbooks/app-development/README.md','playbooks/app-development/DELIVERY.md','playbooks/app-development/QUALITY.md','playbooks/app-development/OPERATIONS.md']),
    ('Campus launch', ['launch/README.md','launch/CAMPUS-SURVEY.md','launch/CERTIFICATION.md']),
    ('Training', ['training/README.md']),
    ('Templates', ['templates/README.md','templates/PROJECT-BRIEF.md','templates/WEBSITE-REQUEST.md','templates/CHANGE-REQUEST.md','templates/INCIDENT-REPORT.md','templates/SERVICE-LOG.md','templates/CAMPUS-READINESS.md','templates/ACCESS-REVIEW.md','templates/TEAM-HANDOVER.md','templates/DOCUMENT-REVIEW.md','templates/ASSET-INVENTORY.csv','templates/ROLE-COMPETENCY.csv','templates/LAUNCH-BUDGET.csv']),
]
GROUP_BADGES = {'Start here': 'foundation', 'Internet team':'internet', 'Website team':'website', 'App development':'app', 'Campus launch':'launch','Training':'training','Templates':'templates'}
REPOSITORY = 'https://github.com/favorchurch/tech-toolkit'
FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#F45500"/><path d="M17 16h31v9H27v9h17v9H27v14H17z" fill="#121411"/></svg>'


def slugify(raw: str) -> str:
    norm = unicodedata.normalize('NFKD', raw).lower()
    norm = re.sub(r'[^\w\s-]', '', norm, flags=re.UNICODE)
    return re.sub(r'[-\s]+','-',norm).strip('-') or 'section'


def clean_text(markdown: str) -> str:
    markdown = re.sub(r'~~~(?:mermaid|\w+)?\n[\s\S]*?~~~', ' ', markdown)
    markdown = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', markdown)
    markdown = re.sub(r'[`*_#>\[\]|]', ' ', markdown)
    return ' '.join(markdown.split())


def htmlpath(source: str) -> str:
    return str(Path(source).with_suffix('.html'))


def relative(from_page: Path, target: Path) -> str:
    return __import__('os').path.relpath(target, from_page.parent).replace('\\', '/')


def detect_title(source: str, body: str) -> str:
    if source in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[source]
    first = re.search(r'^#\s+(.+)$', body, re.M)
    if first:
        return re.sub(r'\*|`|—', '', first.group(1)).strip()
    return Path(source).stem.replace('-', ' ').replace('_',' ').capitalize()


def iter_sources() -> dict[str,str]:
    found = {}
    for ext in ('*.md','*.csv'):
        for p in REPO.rglob(ext):
            if any(part in EXCLUDED_DIRS for part in p.relative_to(REPO).parts):
                continue
            found[str(p.relative_to(REPO)).replace('\\','/')] = p.read_text(encoding='utf-8-sig')
    return found


def parse_mermaid(source: str) -> tuple[str,list[tuple[str,str,str]],dict[str,tuple[str,bool]]]:
    lines = [l.strip() for l in source.splitlines() if l.strip() and not l.strip().startswith('%%')]
    if not lines or not lines[0].startswith('flowchart '):
        return ('TB',[],{})
    direction = 'LR' if re.search(r'\bLR\b',lines[0]) else 'TB'
    nodes: dict[str,tuple[str,bool]] = OrderedDict()
    edges: list[tuple[str,str,str]] = []
    node_rx = re.compile(r'^([A-Za-z][\w-]*)(?:\[([^\]]+)\]|\{([^}]+)\})?$')
    edge_rx = re.compile(r'^\s*(.+?)\s*(?:--\s*([^\n<>]+?)\s*-->|-->|==>)\s*(?:\|([^|]+)\|)?\s*(.+?)\s*$')
    for line in lines[1:]:
        edge = edge_rx.match(line)
        if not edge:
            lone = node_rx.match(line)
            if lone:
                k,txt,decision=lone.group(1,2,3)
                nodes.setdefault(k,(txt or decision or k,bool(decision)))
            continue
        lhs,lab1,lab2,rhs = edge.groups()
        left,right = node_rx.match(lhs.strip()),node_rx.match(rhs.strip())
        if not left or not right: continue
        for n in (left,right):
            key,rect,decision=n.group(1,2,3)
            if key not in nodes or rect or decision:
                nodes[key]=(rect or decision or key,bool(decision))
        edges.append((left.group(1),right.group(1),(lab1 or lab2 or '').strip()))
    return direction,edges,nodes


def svg_for_mermaid(source: str, svg_dir: Path, filename: str) -> str | None:
    dot = shutil.which('dot')
    if not dot: return None
    direction,edges,nodes = parse_mermaid(source)
    if not nodes or not edges: return None
    lines=['digraph guide {',f'graph [rankdir={direction}, bgcolor="transparent", pad="0.2", nodesep="0.35", ranksep="0.55", splines=polyline];',
           'node [fontname="Arial", fontsize=12, fontcolor="#121411", color="#121411", penwidth=1.25, style="filled,rounded", fillcolor="#FEF1E8", margin="0.22,0.13"];',
           'edge [fontname="Arial", fontsize=10, fontcolor="#625F59", color="#625F59", arrowsize=0.68];']
    for key,(label,decision) in nodes.items():
        safe = json.dumps(label.replace('<','').replace('>',''))
        shape='diamond' if decision else 'box'
        fill='"#FFB42A"' if decision else '"#FEF1E8"'
        lines.append(f'{json.dumps(key)} [label={safe}, shape={shape}, fillcolor={fill}];')
    for src,dst,label in edges:
        attrs = f'[label={json.dumps(label)}]' if label else ''
        lines.append(f'{json.dumps(src)} -> {json.dumps(dst)} {attrs};')
    lines.append('}')
    try:
        done = subprocess.run([dot,'-Tsvg'],input='\n'.join(lines),capture_output=True,text=True,timeout=7,check=True)
        svg=done.stdout
        if '<svg' not in svg: return None
        svg_dir.mkdir(parents=True,exist_ok=True)
        (svg_dir/filename).write_text(svg,encoding='utf-8')
        return filename
    except (OSError,subprocess.SubprocessError):
        return None


def render_document(source_path: str, body: str, out: Path, docs: dict[str,str], title: str) -> tuple[str,list[dict]]:
    md = MarkdownIt('commonmark',{'html':False,'linkify':False,'breaks':False}).enable('table').enable('strikethrough')
    toc=[]
    slugs={}
    outer=REPO/source_path
    page=out/htmlpath(source_path)
    code_index=0
    default_fence=md.renderer.rules['fence']
    default_text=md.renderer.rules['text']

    def fence_rule(tokens, idx, options, env):
        nonlocal code_index
        token=tokens[idx]
        lang=token.info.strip().split(' ')[0].lower()
        if lang=='mermaid':
            code_index+=1
            stem=slugify(Path(source_path).stem)
            asset=f'{stem}-{code_index}.svg'
            svg_path=out/'assets'/'diagrams'
            actual=svg_for_mermaid(token.content,svg_path,asset)
            code=html.escape(token.content)
            if actual:
                src=html.escape(relative(page,svg_path/actual),quote=True)
                return f'<figure class="diagram"><img src="{src}" alt="Process flow diagram; the source description is available below." loading="lazy"><details><summary>read diagram source</summary><pre><code>{code}</code></pre></details></figure>'
            direction,edges,nodes=parse_mermaid(token.content)
            node_text=''.join('<li>'+html.escape(v[0])+'</li>' for v in nodes.values())
            return f'<figure class="diagram fallback"><p class="diagram-eyebrow">process flow</p><ol class="flow-fallback">{node_text}</ol><details><summary>read complete connections</summary><pre><code>{code}</code></pre></details></figure>'
        return default_fence(tokens,idx,options,env)

    def text_rule(tokens,idx,options,env):
        raw=tokens[idx].content
        checked=None
        if raw.startswith('[ ] '):checked=False
        elif raw.lower().startswith('[x] '):checked=True
        if checked is not None:
            rest=html.escape(raw[4:])
            flag=' checked' if checked else ''
            return f'<input class="task-checkbox" type="checkbox" disabled{flag} aria-label="{("Complete" if checked else "Not complete")}"> {rest}'
        return default_text(tokens,idx,options,env)

    def heading_open(tokens,idx,options,env):
        tok=tokens[idx]
        next_tok=tokens[idx+1]
        text=next_tok.content if next_tok.type=='inline' else ''
        tag=tok.tag
        if tag in ('h2','h3','h4'):
            base=slugify(text)
            count=slugs.get(base,0)
            slugs[base]=count+1
            sid=base if not count else f'{base}-{count+1}'
            tok.attrSet('id',sid)
            if tag in ('h2','h3'):
                toc.append({'id':sid,'level':int(tag[1]),'title':text})
        return md.renderer.renderToken(tokens,idx,options,env)

    def link_open(tokens,idx,options,env):
        tok=tokens[idx]
        href=tok.attrGet('href') or ''
        if href.startswith(('http://','https://')):
            tok.attrSet('target','_blank')
            tok.attrSet('rel','noopener noreferrer')
        elif href and not href.startswith(('#','mailto:','tel:','data:')):
            u=urlsplit(href)
            target=(outer.parent/unquote(u.path)).resolve()
            try:
                rname=str(target.relative_to(REPO)).replace('\\','/')
            except ValueError:
                rname=None
            if rname in docs:
                if rname.endswith('.csv'):
                    dest=out/'downloads'/Path(rname).name
                else:
                    dest=out/htmlpath(rname)
                url=relative(page,dest)
                if u.fragment: url += '#'+u.fragment
                tok.attrSet('href',url)
        return md.renderer.renderToken(tokens,idx,options,env)

    md.renderer.rules['fence']=fence_rule
    md.renderer.rules['text']=text_rule
    md.renderer.rules['heading_open']=heading_open
    md.renderer.rules['link_open']=link_open

    # The reading page has its own H1; avoid duplicate headings.
    body = re.sub(r'^#\s+.+?\s*\n', '',body,count=1,flags=re.M)
    markup=md.render(body)
    return markup,toc


def csv_html(source: str, value: str) -> str:
    records=list(csv.reader(value.splitlines()))
    if not records:return '<p>This template has no rows yet.</p>'
    headers=records[0]
    thead=''.join(f'<th scope="col">{html.escape(h.replace("_"," "))}</th>' for h in headers)
    rows=[]
    for record in records[1:5]:
        row=''.join(f'<td>{html.escape(s)}</td>' for s in record)
        rows.append(f'<tr>{row}</tr>')
    dl='../downloads/'+Path(source).name
    return f'<div class="notice"><strong>Blank CSV template</strong><p>This is a reusable example, not a completed campus record.</p><p><a class="button button-primary" href="{html.escape(dl,quote=True)}" download>download csv ↗</a></p></div><div class="table-wrap"><table><thead><tr>{thead}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def sidebar_html(items: list[dict],current: str|None,home: bool=False) -> str:
    output=[]
    for label,paths in GROUPS:
        members=[x for x in items if x['source'] in paths]
        if not members: continue
        entries=[]
        for x in members:
            name=x['title']
            if label=='Templates' and x['source'].endswith('.csv'): name=name.replace(' CSV','')
            active=x['source']==current
            href= x['url'] if home else relative(Path('x') if current is None else Path(htmlpath(current)),Path(x['url']))
            entries.append(f'<a class="nav-link{" selected" if active else ""}" href="{html.escape(href,quote=True)}"{" aria-current=\"page\"" if active else ""}>{html.escape(name)}</a>')
        output.append(f'<div class="nav-group"><div class="nav-heading">{html.escape(label)}</div>{"".join(entries)}</div>')
    return ''.join(output)


def render_shell(*, title: str, content: str, nav: str, toc: str, path: str, active_group: str, root_href: str, asset_prefix: str, source_href: str='', page_type: str='doc',prev_html: str='',next_html: str='') -> str:
    breadcrumb=f'<a href="{html.escape(root_href,quote=True)}">all guides</a><span aria-hidden="true">/</span><span>{html.escape(active_group.lower())}</span>' if page_type=='doc' else '<span>open-source tech toolkit</span>'
    subtitle=f'<div class="page-meta"><span class="meta-dot" aria-hidden="true"></span>favor tech toolkit <span class="meta-sep">/</span> {html.escape(active_group.lower())} <span class="meta-sep">/</span> v0.1</div>'
    toolbar = f'<div class="page-actions"><a href="{html.escape(source_href,quote=True)}" target="_blank" rel="noopener noreferrer" class="page-action">view source ↗</a><button class="page-action js-print" type="button">print page</button></div>' if page_type=='doc' else ''
    toc_block= f'<aside class="toc" aria-label="On this page"><div class="toc-inner"><div class="toc-label">on this page</div>{toc}</div></aside>' if toc else ''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#FEF1E8"><meta name="description" content="Favor Tech reusable Internet, Website, and App Development playbooks and campus launch resources."><title>{html.escape(title)} · favor tech toolkit</title><link rel="icon" href="data:image/svg+xml,{__import__('urllib.parse').parse.quote(FAVICON)}"><link rel="stylesheet" href="{asset_prefix}assets/style.css"></head>
<body class="{page_type}"><a class="skip-link" href="#main">skip to content</a>
<div class="topline"></div><header class="site-top"><button id="menu-toggle" class="icon-button menu-toggle" type="button" aria-label="open navigation" aria-controls="side-nav" aria-expanded="false"><span aria-hidden="true">☰</span></button><a class="brand" href="{html.escape(root_href,quote=True)}" aria-label="Favor Tech toolkit home"><span class="brand-mark" aria-hidden="true">f<span class="brand-spark">✳</span></span><span class="brand-text"><span>favor</span><strong>tech toolkit.</strong></span></a><div class="top-center">the playbook for what’s next.</div><button type="button" id="open-search" class="search-trigger" aria-label="search all guides"><span aria-hidden="true">⌕</span><span class="search-label">search guides</span><kbd>⌘ K</kbd></button><a class="top-github" href="{REPOSITORY}" target="_blank" rel="noopener noreferrer" aria-label="GitHub source">github ↗</a></header>
<div id="nav-scrim" class="nav-scrim" hidden></div><div class="site-layout"><aside class="sidebar" id="side-nav" aria-label="Guide navigation"><div class="sidebar-head"><div class="small-label">THE SYSTEM</div><strong>all guides.</strong><span class="sidebar-count">three teams · one toolkit</span></div><nav>{nav}</nav><div class="sidebar-bottom"><span class="sidebar-foot-dot"></span><span>open-source by design.</span></div></aside>
<main id="main" tabindex="-1"><div class="breadcrumbs">{breadcrumb}</div>{content}<footer class="site-footer"><span>built to multiply good work.</span><span>favor tech · open source</span></footer></main>{toc_block}</div>
<dialog id="search-dialog" class="search-dialog" aria-labelledby="search-title"><div class="search-head"><div id="search-title" class="search-title">find your next step.</div><button type="button" id="close-search" class="icon-button" aria-label="close search">×</button></div><label class="search-input-row"><span aria-hidden="true">⌕</span><input id="search-input" type="search" placeholder="search all guides, roles, checklists..." aria-label="Search the toolkit" autocomplete="off"></label><div id="search-status" class="search-status" role="status" aria-live="polite"></div><div id="search-results" class="search-results" role="listbox" aria-label="Search results"></div><div class="search-bottom"><span><kbd>↑</kbd><kbd>↓</kbd> navigate</span><span><kbd>↵</kbd> open</span><span><kbd>esc</kbd> close</span></div></dialog>
<script defer src="{asset_prefix}assets/search-index.js"></script><script defer src="{asset_prefix}assets/app.js"></script></body></html>'''


def homepage(items:list[dict]) -> str:
    tabs=[]
    for label,paths in GROUPS:
        subset=[x for x in items if x['source'] in paths]
        if not subset:continue
        href=subset[0]['url']
        preview=''.join(f'<li><a href="{html.escape(x["url"],quote=True)}">{html.escape(x["title"])} <span aria-hidden="true">↗</span></a></li>' for x in subset[:5])
        tabs.append(f'<section class="directory-group"><div class="directory-heading"><span>{html.escape(label.lower())}</span><small>{len(subset):02d} guides</small></div><ul>{preview}</ul><a class="more-link" href="{html.escape(href,quote=True)}">browse {html.escape(label.lower())} ↗</a></section>')
    return '''<section class="hero"><div class="hero-eyebrow"><span class="pill-dot"></span> open-source operations toolkit <span class="hero-year">2026 edition</span></div><div class="hero-inner"><div class="hero-copy"><h1>good systems.<br><em>more room</em><br>to grow.</h1><p>Everything a campus needs to build, run, and grow its Tech ministry—with confidence, care, and no guesswork.</p><div class="hero-actions"><a class="button button-ink" href="docs/START-HERE.html">explore the guides <span aria-hidden="true">↗</span></a><a class="text-link" href="launch/README.html">launch a campus <span aria-hidden="true">↗</span></a></div></div><div class="hero-art" aria-hidden="true"><div class="art-ring art-ring-a"></div><div class="art-ring art-ring-b"></div><div class="art-center">+</div><span class="art-type art-type-one">BUILD</span><span class="art-type art-type-two">SERVE</span><span class="art-type art-type-three">SHARE</span></div></div><div class="hero-base"><span>one mission.</span><span>many locations.</span><span>shared excellence.</span></div></section>
<section class="intro-section"><div class="section-eyebrow">01 / the toolkit</div><div class="intro-layout"><h2>Everything<br>you need.<span class="orange-dot">.</span></h2><div><p>These aren't one-off instructions. They’re living playbooks, built from real Favor Tech workflows and designed to travel from one campus to the next.</p><div class="stat-row"><div><strong>03</strong><small>team playbooks</small></div><div><strong>03</strong><small>launch stages</small></div><div><strong>10</strong><small>toolkit categories</small></div></div></div></div></section>
<section class="tracks"><div class="section-eyebrow">02 / choose your track</div><div class="section-header"><h2>where do you<br><em>serve?</em></h2><p>Pick your lane and get straight to the work.</p></div><div class="track-grid"><a class="track-card track-internet" href="playbooks/internet/README.html"><span class="track-top"><small>01 / connect</small><span aria-hidden="true">↗</span></span><span class="track-icon" aria-hidden="true">⌁</span><strong>internet.</strong><span>Keep Sundays connected. Network setup, livestream operations, service checks, and incident recovery.</span><span class="track-bottom">open playbook <span aria-hidden="true">↗</span></span></a><a class="track-card track-website" href="playbooks/website/README.html"><span class="track-top"><small>02 / publish</small><span aria-hidden="true">↗</span></span><span class="track-icon" aria-hidden="true">◉</span><strong>website.</strong><span>Make every digital page count. Requests, design approval, content, QA, and releases.</span><span class="track-bottom">open playbook <span aria-hidden="true">↗</span></span></a><a class="track-card track-app" href="playbooks/app-development/README.html"><span class="track-top"><small>03 / build</small><span aria-hidden="true">↗</span></span><span class="track-icon" aria-hidden="true">{ }</span><strong>app dev.</strong><span>Build systems that last. Requirements, engineering, security, testing, and deployment.</span><span class="track-bottom">open playbook <span aria-hidden="true">↗</span></span></a></div></section>
<section class="launch-band"><div><div class="section-eyebrow">03 / campus multiplication</div><h2>ready, steady,<br><em>launch.</em></h2><p>Campus readiness is earned through practice, not just paperwork. Move from preparation to assisted service to demonstrated independence.</p><a class="button button-outline" href="launch/README.html">open launch pack <span aria-hidden="true">↗</span></a></div><ol class="launch-steps"><li><span>01</span><div><strong>prepare.</strong><p>Assess needs, train operators, test the essentials.</p></div></li><li><span>02</span><div><strong>assisted launch.</strong><p>Run live services with central support.</p></div></li><li><span>03</span><div><strong>certified.</strong><p>Show independent operation and safe recovery.</p></div></li></ol></section>
<section class="directory" id="guides"><div class="section-eyebrow">04 / all the guides</div><div class="directory-intro"><h2>find your<br>next step.</h2><p>Read the whole toolkit, or jump straight to the checklist you need.</p></div><div class="directory-grid">'''+''.join(tabs)+'''</div></section>
<section class="endnote"><span class="starlet" aria-hidden="true">✳</span><div><div class="small-label">SHARED KNOWLEDGE. SHARED RESPONSIBILITY.</div><h2>built to multiply<br>good work.</h2><p>Open for anyone to learn from. Maintained by the people who serve.</p><a href="docs/GOVERNANCE.html">read how we maintain it ↗</a></div></section>'''


def build(out:Path):
    docs=iter_sources()
    if 'README.md' not in docs:
        raise RuntimeError(f'Repository README not found in {REPO}')
    ordered=[]
    used=set()
    for group,paths in GROUPS:
        for p in paths:
            if p in docs:
                ordered.append({'source':p,'title':detect_title(p,docs[p]),'group':group,'badge':GROUP_BADGES[group],'url':htmlpath(p)})
                used.add(p)
    extra=sorted(set(docs)-used)
    for p in extra:
        ordered.append({'source':p,'title':detect_title(p,docs[p]),'group':'Other resources','badge':'foundation','url':htmlpath(p)})
    nav_home=sidebar_html(ordered,None,True)
    (out/'assets').mkdir(parents=True,exist_ok=True)
    (out/'downloads').mkdir(parents=True,exist_ok=True)
    for filename in ('style.css','app.js'):
        shutil.copy2(SELF/'assets'/filename,out/'assets'/filename)
    toc_count=0
    data_index=[]
    for i,doc in enumerate(ordered):
        p=doc['source'];page=out/doc['url'];page.parent.mkdir(parents=True,exist_ok=True)
        if p.endswith('.csv'):
            shutil.copy2(REPO/p,out/'downloads'/Path(p).name)
            rendered=csv_html(p,docs[p]);toc=[]
        else:
            rendered,toc=render_document(p,docs[p],out,docs,doc['title'])
        toc_count+=len(toc)
        groupsafe=html.escape(doc['group'].lower())
        eyebrow=f'<div class="doc-eyebrow"><span class="doc-type-marker"></span>{groupsafe} / field guide</div>'
        heading=f'<div class="doc-heading"><h1>{html.escape(doc["title"])}</h1><p>Reusable processes and checklists for teams who serve.</p></div>'
        source_href=REPOSITORY+'/blob/main/'+p
        source_link='<div class="page-actions"><a class="page-action" target="_blank" rel="noopener noreferrer" href="'+html.escape(source_href,quote=True)+'">view source ↗</a><button class="page-action js-print" type="button">print page</button></div>'
        prev=ordered[i-1] if i else None
        nxt=ordered[i+1] if i+1<len(ordered) else None
        prev_link=f'<a class="adjacent-card" href="{relative(page,out/prev["url"])}"><small>← previous</small><strong>{html.escape(prev["title"])}</strong></a>' if prev else '<span></span>'
        next_link=f'<a class="adjacent-card next" href="{relative(page,out/nxt["url"])}"><small>next →</small><strong>{html.escape(nxt["title"])}</strong></a>' if nxt else '<span></span>'
        content=f'<div class="document-shell"><div class="document-lead">{eyebrow}{heading}{source_link}</div><article class="prose" aria-label="{html.escape(doc["title"],quote=True)}">{rendered}</article><div class="document-feedback"><span>Spotted an outdated step?</span><a href="{REPOSITORY}/issues/new" target="_blank" rel="noopener noreferrer">propose an update ↗</a></div><nav class="adjacent" aria-label="Previous and next guides">{prev_link}{next_link}</nav></div>'
        toc_items=''.join(f'<a href="#{html.escape(t["id"],quote=True)}" class="toc-depth-{t["level"]}">{html.escape(t["title"])}</a>' for t in toc)
        roots=relative(page,out/'index.html')
        asset=relative(page,out/'index.html').replace('index.html','')
        output=render_shell(title=doc['title'],content=content,nav=sidebar_html(ordered,p),toc=toc_items,path=p,active_group=doc['group'],root_href=roots,asset_prefix=asset,source_href=source_href)
        page.write_text(output,encoding='utf-8')
        preview=clean_text(docs[p])
        data_index.append({'title':doc['title'],'group':doc['group'],'href':doc['url'],'body':preview[:16000],'excerpt':preview[:200]})
    home=render_shell(title='home',content=homepage(ordered),nav=nav_home,toc='',path='',active_group='home',root_href='index.html',asset_prefix='',page_type='home')
    (out/'index.html').write_text(home,encoding='utf-8')
    data='window.FAVOR_TECH_SEARCH_INDEX = '+json.dumps(data_index,ensure_ascii=False,separators=(',',':'))+';\n'
    (out/'assets'/'search-index.js').write_text(data,encoding='utf-8')
    (out/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8')
    (out/'404.html').write_text(home,encoding='utf-8')
    print(f'Built {len(ordered)} guide/template HTML pages + home; {toc_count} section anchors; {len(extra)} unclassified resources; outputs in {out}')
    if extra: print('Additional sources:',', '.join(extra))
    return len(ordered)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default=str(REPO/'public'))
    args=parser.parse_args()
    dest=Path(args.output).resolve()
    if dest==REPO: raise SystemExit('Refusing to overwrite repository root')
    dest.mkdir(parents=True,exist_ok=True)
    build(dest)
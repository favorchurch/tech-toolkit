/* Offline-friendly navigation and client-side search for the Favor Tech toolkit. */
(() => {
  'use strict';
  const q = (selector, root = document) => root.querySelector(selector);
  const qa = (selector, root = document) => [...root.querySelectorAll(selector)];
  const body = document.body;
  const menu = q('#menu-toggle');
  const scrim = q('#nav-scrim');
  const sidenav = q('#side-nav');
  let menuReturnFocus = null;

  const closeMenu = () => {
    body.classList.remove('nav-open');
    menu?.setAttribute('aria-expanded', 'false');
    menu?.setAttribute('aria-label', 'open navigation');
    if (scrim) scrim.hidden = true;
  };
  const toggleMenu = () => {
    if (body.classList.contains('nav-open')) {
      closeMenu();
      menu?.focus();
    } else {
      menuReturnFocus = document.activeElement;
      body.classList.add('nav-open');
      menu?.setAttribute('aria-expanded', 'true');
      menu?.setAttribute('aria-label', 'close navigation');
      if (scrim) scrim.hidden = false;
      q('.selected', sidenav)?.scrollIntoView({ block: 'nearest' });
      (q('.selected', sidenav) || q('.nav-link', sidenav))?.focus();
    }
  };
  menu?.addEventListener('click', toggleMenu);
  scrim?.addEventListener('click', () => { closeMenu(); menu?.focus(); });
  sidenav?.addEventListener('click', (e) => { if (e.target.closest('a')) closeMenu(); });
  window.addEventListener('resize', () => { if (window.innerWidth > 820) closeMenu(); }, { passive: true });

  qa('.js-print').forEach((button) => button.addEventListener('click', () => window.print()));

  const tocLinks = qa('.toc-inner a[href^="#"]');
  if ('IntersectionObserver' in window && tocLinks.length) {
    const tracked = tocLinks.map((link) => document.getElementById(decodeURIComponent(link.hash.slice(1)))).filter(Boolean);
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (!visible.length) return;
      tocLinks.forEach((link) => link.classList.toggle('current', link.hash.slice(1) === visible[0].target.id));
    }, { rootMargin: '-108px 0px -70% 0px', threshold: 0 });
    tracked.forEach((h) => observer.observe(h));
  }

  const dialog = q('#search-dialog');
  const trigger = q('#open-search');
  const closer = q('#close-search');
  const input = q('#search-input');
  const results = q('#search-results');
  const status = q('#search-status');
  const index = Array.isArray(window.FAVOR_TECH_SEARCH_INDEX) ? window.FAVOR_TECH_SEARCH_INDEX : [];
  const script = [...document.scripts].find((s) => s.src && s.src.endsWith('/assets/app.js'));
  const siteRoot = script ? new URL('../', script.src) : new URL('./', window.location.href);
  let activeIndex = 0;
  let resultLinks = [];
  let lastFocus = null;

  const isTyping = (target) => !!target?.closest?.('input, textarea, select, [contenteditable="true"]');
  const tokens = (text) => text.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean).slice(0,8);
  const highlight = (text, query) => {
    const fragment = document.createDocumentFragment();
    if (!query) { fragment.append(document.createTextNode(text)); return fragment; }
    const low = text.toLocaleLowerCase();
    const pos = low.indexOf(query.toLocaleLowerCase());
    if (pos < 0) { fragment.append(document.createTextNode(text)); return fragment; }
    fragment.append(document.createTextNode(text.slice(0,pos)));
    const marked = document.createElement('mark');
    marked.textContent = text.slice(pos,pos+query.length);
    fragment.append(marked,document.createTextNode(text.slice(pos+query.length)));
    return fragment;
  };
  const scoreItem = (item, words) => {
    const title = item.title.toLowerCase();
    const group = item.group.toLowerCase();
    const content = item.body.toLowerCase();
    let score = 0;
    for (const word of words) {
      if (title === word) score += 60;
      else if (title.includes(word)) score += 24;
      if (group.includes(word)) score += 8;
      if (content.includes(word)) score += 3;
      if (!(title.includes(word) || group.includes(word) || content.includes(word))) return 0;
    }
    return score;
  };
  const selectResult = (n) => {
    resultLinks.forEach((link,i) => link.setAttribute('aria-selected', String(i===n)));
    activeIndex = n;
    resultLinks[n]?.scrollIntoView({ block:'nearest' });
  };
  const renderSearch = () => {
    if (!results || !input) return;
    const words = tokens(input.value);
    const best = words.length
      ? index.map((item) => ({item,score:scoreItem(item,words)})).filter((entry)=>entry.score>0).sort((a,b)=>b.score-a.score).slice(0,12).map((entry)=>entry.item)
      : index.filter((item) => /^(README\.md|docs\/START-HERE\.md)$/i.test(item.href.replace(/\.html$/,'.md'))).concat(index.filter((item)=>['Internet team','Website team','App development','Campus launch'].includes(item.group) && item.href.endsWith('/README.html'))).slice(0,6);
    results.replaceChildren();
    activeIndex = 0;
    status.textContent = words.length ? `${best.length} of ${index.length} guides shown` : `start here · ${index.length} searchable guides`;
    if (!best.length) {
      const empty = document.createElement('p'); empty.className='search-empty';
      empty.textContent='No matches yet. Try a team name, action, or checklist topic.';
      results.append(empty);
      resultLinks=[];
      return;
    }
    best.forEach((item,i) => {
      const link=document.createElement('a');
      link.className='search-result';
      link.href=new URL(item.href,siteRoot).href;
      link.setAttribute('role','option');
      link.setAttribute('aria-selected',String(i===0));
      const group=document.createElement('small'); group.textContent=item.group;
      const name=document.createElement('strong'); name.append(highlight(item.title,words[0] || ''));
      const desc=document.createElement('span');
      const excerpt=item.excerpt || '';
      const firstWord=words.find(w=>excerpt.toLowerCase().includes(w));
      desc.append(highlight(excerpt.slice(0,146)+(excerpt.length>146?'…':''),firstWord||''));
      link.append(group,name,desc);
      link.addEventListener('mouseenter',()=>selectResult(i));
      results.append(link);
    });
    resultLinks=qa('.search-result',results);
  };
  const openSearch = () => {
    if (!dialog?.showModal) return;
    closeMenu();
    lastFocus=document.activeElement;
    dialog.showModal();
    input.value='';
    renderSearch();
    input.focus();
  };
  const closeSearch = () => {
    if (dialog?.open) dialog.close();
    lastFocus?.focus?.();
  };
  trigger?.addEventListener('click',openSearch);
  closer?.addEventListener('click',closeSearch);
  dialog?.addEventListener('click',(event) => { if(event.target===dialog) closeSearch(); });
  dialog?.addEventListener('close', () => lastFocus?.focus?.());
  input?.addEventListener('input',renderSearch);
  input?.addEventListener('keydown',(e) => {
    if(e.key==='ArrowDown' && resultLinks.length){e.preventDefault(); selectResult((activeIndex+1)%resultLinks.length);}
    if(e.key==='ArrowUp' && resultLinks.length){e.preventDefault(); selectResult((activeIndex-1+resultLinks.length)%resultLinks.length);}
    if(e.key==='Enter' && resultLinks.length){e.preventDefault();window.location.href=resultLinks[activeIndex].href;}
  });
  document.addEventListener('keydown',(event)=>{
    if((event.metaKey||event.ctrlKey) && event.key.toLowerCase()==='k'){
      event.preventDefault();dialog?.open ? closeSearch():openSearch();return;
    }
    if(event.key==='/'&&!event.ctrlKey&&!event.metaKey&&!event.altKey&&!isTyping(event.target)&&!dialog?.open){
      event.preventDefault();openSearch();return;
    }
    if(event.key==='Escape'&&body.classList.contains('nav-open')){closeMenu();(menuReturnFocus||menu)?.focus();}
  });
})();
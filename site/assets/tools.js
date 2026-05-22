/* DREAM MACHINE — Toolkit page logic
   Loads tools.json + categories.json, renders facets and a fast
   client-side filtered grid. URL-state-aware so deep-links work.
*/

(async () => {
  const [tools, categories] = await Promise.all([
    DM.loadJSON('tools'),
    DM.loadJSON('categories'),
  ]);

  const ALL_LAYERS = uniqueSortedBy(tools, t => t.layer);
  const ALL_DISCIPLINES = uniqueSortedBy(tools.flatMap(t => t.disciplines), x => x);

  // --- State (mirrored to URL hash for shareable links) ---
  const state = {
    q: '',
    cats: new Set(),
    layers: new Set(),
    disciplines: new Set(),
  };

  hydrateFromURL();

  // --- DOM refs ---
  const $catList   = document.getElementById('facet-cats');
  const $layerList = document.getElementById('facet-layers');
  const $discList  = document.getElementById('facet-disciplines');
  const $grid      = document.getElementById('tool-grid');
  const $count     = document.getElementById('result-count');
  const $total     = document.getElementById('total-count');
  const $totalHero = document.getElementById('t-total');
  const $catsHero  = document.getElementById('t-cats');
  const $chips     = document.getElementById('active-chips');
  const $input     = document.getElementById('search-input');
  const $empty     = document.getElementById('empty');
  const $clearAll  = document.getElementById('clear-all');

  $totalHero.textContent = tools.length.toLocaleString();
  $catsHero.textContent = categories.length;
  $total.textContent = tools.length.toLocaleString();
  $input.value = state.q;

  // --- Render facets ---
  function renderFacets() {
    $catList.innerHTML = categories.map(c => `
      <button class="facet ${state.cats.has(c.slug) ? 'is-active' : ''}"
              data-kind="cats" data-val="${DM.escapeHTML(c.slug)}">
        <span>${DM.escapeHTML(c.name)}</span>
        <span class="facet__count">${c.count}</span>
      </button>
    `).join('');

    $layerList.innerHTML = ALL_LAYERS.map(([layer, count]) => `
      <button class="facet ${state.layers.has(layer) ? 'is-active' : ''}"
              data-kind="layers" data-val="${DM.escapeHTML(layer)}">
        <span>${DM.escapeHTML(layer)}</span>
        <span class="facet__count">${count}</span>
      </button>
    `).join('');

    $discList.innerHTML = ALL_DISCIPLINES.map(([d, count]) => `
      <button class="facet ${state.disciplines.has(d) ? 'is-active' : ''}"
              data-kind="disciplines" data-val="${DM.escapeHTML(d)}">
        <span>${DM.escapeHTML(d)}</span>
        <span class="facet__count">${count}</span>
      </button>
    `).join('');
  }

  // --- Render results ---
  function applyFilters() {
    const q = state.q.trim().toLowerCase();
    const tokens = q.length ? q.split(/\s+/).filter(Boolean) : [];

    const filtered = tools.filter(t => {
      if (state.cats.size && !state.cats.has(t.category_slug)) return false;
      if (state.layers.size && !state.layers.has(t.layer)) return false;
      if (state.disciplines.size) {
        const ok = t.disciplines.some(d => state.disciplines.has(d));
        if (!ok) return false;
      }
      if (tokens.length) {
        const blob = t._s || '';
        for (const tk of tokens) {
          if (!blob.includes(tk)) return false;
        }
      }
      return true;
    });

    // Sort: exact name match first, then alpha
    filtered.sort((a, b) => {
      if (tokens.length) {
        const aHit = a.name.toLowerCase().startsWith(tokens[0]) ? 0 : 1;
        const bHit = b.name.toLowerCase().startsWith(tokens[0]) ? 0 : 1;
        if (aHit !== bHit) return aHit - bHit;
      }
      return a.name.localeCompare(b.name);
    });

    $count.textContent = filtered.length.toLocaleString();

    if (filtered.length === 0) {
      $grid.innerHTML = '';
      $empty.hidden = false;
    } else {
      $empty.hidden = true;
      // Cap render at 600 to stay snappy (we'll never exceed total anyway)
      const slice = filtered.slice(0, 600);
      $grid.innerHTML = slice.map(renderCard).join('');
    }

    renderChips();
    writeURL();
  }

  function renderCard(t) {
    const issuePills = (t.issues || []).slice(0, 6).map(n =>
      `<a class="tool-card__issue-pill" href="issue.html?n=${n}" title="Mentioned in Issue ${n}">#${n}</a>`
    ).join('');
    const moreIssues = (t.issues && t.issues.length > 6)
      ? `<span class="tool-card__issue-pill" style="background:transparent;border:none;color:var(--text-muted)">+${t.issues.length - 6}</span>`
      : '';
    const link = t.url
      ? `<a class="tool-card__link" href="${DM.escapeHTML(t.url)}" target="_blank" rel="noopener">Open ↗</a>`
      : '';
    const vendor = t.vendor
      ? `<span class="tool-card__vendor">${DM.escapeHTML(t.vendor)}</span>`
      : '';

    return `
      <article class="tool-card">
        <div class="tool-card__head">
          <h3 class="tool-card__name">${DM.escapeHTML(t.name)}</h3>
          ${vendor}
        </div>
        <p class="tool-card__blurb">${DM.escapeHTML(t.blurb)}</p>
        <div class="tool-card__meta">
          <span class="tool-card__cat">${DM.escapeHTML(t.category)}</span>
          ${link}
        </div>
        ${issuePills ? `<div class="tool-card__issues">${issuePills}${moreIssues}</div>` : ''}
      </article>
    `;
  }

  function renderChips() {
    const chips = [];
    state.cats.forEach(slug => {
      const cat = categories.find(c => c.slug === slug);
      chips.push({ kind: 'cats', val: slug, label: cat ? cat.name : slug, cls: 'chip' });
    });
    state.layers.forEach(l => chips.push({ kind: 'layers', val: l, label: l, cls: 'chip chip--pink' }));
    state.disciplines.forEach(d => chips.push({ kind: 'disciplines', val: d, label: d, cls: 'chip' }));
    $chips.innerHTML = chips.map(c =>
      `<button class="${c.cls}" data-rm-kind="${c.kind}" data-rm-val="${DM.escapeHTML(c.val)}">
        ${DM.escapeHTML(c.label)} <span class="chip__x">×</span>
      </button>`
    ).join('');
    if (chips.length > 1) {
      $chips.insertAdjacentHTML('beforeend',
        `<button class="chip chip--neutral" id="clear-inline">Clear all</button>`);
      document.getElementById('clear-inline').addEventListener('click', clearAll);
    }
  }

  // --- Event wiring ---
  document.getElementById('facets').addEventListener('click', e => {
    const b = e.target.closest('button.facet');
    if (!b) return;
    const kind = b.dataset.kind, val = b.dataset.val;
    const set = state[kind];
    if (set.has(val)) set.delete(val); else set.add(val);
    renderFacets();
    applyFilters();
  });

  $chips.addEventListener('click', e => {
    const b = e.target.closest('[data-rm-kind]');
    if (!b) return;
    state[b.dataset.rmKind].delete(b.dataset.rmVal);
    renderFacets();
    applyFilters();
  });

  $clearAll.addEventListener('click', clearAll);

  let debounce;
  $input.addEventListener('input', () => {
    clearTimeout(debounce);
    debounce = setTimeout(() => {
      state.q = $input.value;
      applyFilters();
    }, 120);
  });

  // --- Helpers ---
  function clearAll() {
    state.q = '';
    state.cats.clear();
    state.layers.clear();
    state.disciplines.clear();
    $input.value = '';
    renderFacets();
    applyFilters();
  }

  function uniqueSortedBy(arr, accessor) {
    const counts = new Map();
    for (const item of arr) {
      const v = accessor(item);
      if (Array.isArray(v)) {
        for (const x of v) counts.set(x, (counts.get(x) || 0) + 1);
      } else if (v) {
        counts.set(v, (counts.get(v) || 0) + 1);
      }
    }
    return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  }

  function writeURL() {
    const params = new URLSearchParams();
    if (state.q) params.set('q', state.q);
    if (state.cats.size) params.set('cat', [...state.cats].join(','));
    if (state.layers.size) params.set('layer', [...state.layers].join(','));
    if (state.disciplines.size) params.set('disc', [...state.disciplines].join(','));
    const qs = params.toString();
    const url = qs ? `?${qs}` : location.pathname;
    history.replaceState(null, '', url);
  }

  function hydrateFromURL() {
    const p = new URLSearchParams(location.search);
    state.q = p.get('q') || '';
    if (p.get('cat')) p.get('cat').split(',').forEach(v => state.cats.add(v));
    if (p.get('layer')) p.get('layer').split(',').forEach(v => state.layers.add(v));
    if (p.get('disc')) p.get('disc').split(',').forEach(v => state.disciplines.add(v));
  }

  // First paint
  renderFacets();
  applyFilters();
})();

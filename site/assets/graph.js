/* DREAM MACHINE — Knowledge Graph
   D3 v7 force-directed layout
   19 category nodes + 572 tool nodes
   Cross-links between tools sharing newsletter issues
   Spring physics with glow visuals
*/

(async () => {
  const [tools, categories] = await Promise.all([
    DM.loadJSON('tools'),
    DM.loadJSON('categories'),
  ]);

  /* ── Colour palette: one per layer ─────────────────────────── */
  const LAYER_COLORS = {
    'Foundation':       '#ee3ec9',  // pink
    'Modality':         '#00ffff',  // cyan
    'Agent':            '#7ed957',  // green
    'Legacy software':  '#f5a623',  // amber
    'Studios & apps':   '#a78bfa',  // lavender
    'Open source':      '#34d399',  // teal
    'Infrastructure':   '#60a5fa',  // sky blue
    'Consumer':         '#fb7185',  // rose
    'Institutions':     '#c084fc',  // purple
    'Native':           '#fbbf24',  // yellow
    'Other':            '#94a3b8',  // slate
    'Technique':        '#6ee7b7',  // mint
  };

  function catColor(cat) {
    return LAYER_COLORS[cat.layer] || '#94a3b8';
  }

  /* ── Build cross-links from shared newsletter issue appearances ─ */
  const toolIssueMap = tools.map(t => new Set(t.issues || []));

  // Group tool indices by issue number
  const byIssue = {};
  tools.forEach((t, i) => {
    (t.issues || []).forEach(n => {
      if (!byIssue[n]) byIssue[n] = [];
      byIssue[n].push(i);
    });
  });

  const crossPairs   = new Set();
  const crossPerTool = new Array(tools.length).fill(0);
  const crossLinks   = [];

  Object.values(byIssue).forEach(toolList => {
    if (toolList.length < 2) return;
    for (let i = 0; i < toolList.length; i++) {
      for (let j = i + 1; j < toolList.length; j++) {
        const a = toolList[i], b = toolList[j];
        // Cross-category links only
        if (tools[a].category_slug === tools[b].category_slug) continue;
        // Cap connections per node to avoid spaghetti
        if (crossPerTool[a] >= 5 || crossPerTool[b] >= 5) continue;
        const key = Math.min(a, b) + '-' + Math.max(a, b);
        if (crossPairs.has(key)) continue;
        // Require 2+ shared issues
        let shared = 0;
        toolIssueMap[a].forEach(n => { if (toolIssueMap[b].has(n)) shared++; });
        if (shared < 2) continue;
        crossPairs.add(key);
        crossLinks.push({
          source: `tool:${a}`,
          target: `tool:${b}`,
          type:   'cross',
          layer:  tools[a].layer,
        });
        crossPerTool[a]++;
        crossPerTool[b]++;
      }
    }
  });

  /* ── Build node + link arrays ───────────────────────────────── */
  const catById = {};
  categories.forEach((c, i) => {
    catById[c.slug] = i;
  });

  // Category nodes first, then tool nodes
  const nodes = [
    ...categories.map((c, i) => ({
      id: `cat:${c.slug}`,
      kind: 'category',
      label: c.name,
      slug: c.slug,
      layer: c.layer,
      color: catColor(c),
      r: 28,
      count: c.count,
      url: null,
    })),
    ...tools.map((t, i) => {
      const issueCount = (t.issues || []).length;
      // Bigger node = more newsletter appearances (max r 9.5)
      const r = issueCount > 0 ? Math.min(5 + issueCount * 0.8, 9.5) : 4.5;
      return {
        id: `tool:${i}`,
        kind: 'tool',
        label: t.name,
        blurb: t.blurb,
        category: t.category,
        category_slug: t.category_slug,
        layer: t.layer,
        color: LAYER_COLORS[t.layer] || '#94a3b8',
        r,
        issueCount,
        issues: t.issues || [],
        url: t.url || null,
      };
    }),
  ];

  const catLinks = tools.map((t, i) => ({
    source: `cat:${t.category_slug}`,
    target: `tool:${i}`,
    layer: t.layer,
    type: 'cat',
  }));

  const allLinks = [...catLinks, ...crossLinks];

  /* ── SVG setup ──────────────────────────────────────────────── */
  const svg = d3.select('#graph-canvas');
  const W = () => svg.node().clientWidth;
  const H = () => svg.node().clientHeight;

  // SVG filters for glow effects
  const defs = svg.append('defs');

  // Soft glow for heavily-tagged tool nodes
  const softGlow = defs.append('filter')
    .attr('id', 'glow')
    .attr('x', '-60%').attr('y', '-60%')
    .attr('width', '220%').attr('height', '220%');
  softGlow.append('feGaussianBlur').attr('stdDeviation', '2.5').attr('result', 'coloredBlur');
  const fm1 = softGlow.append('feMerge');
  fm1.append('feMergeNode').attr('in', 'coloredBlur');
  fm1.append('feMergeNode').attr('in', 'SourceGraphic');

  // Strong glow for category nodes
  const strongGlow = defs.append('filter')
    .attr('id', 'strong-glow')
    .attr('x', '-100%').attr('y', '-100%')
    .attr('width', '300%').attr('height', '300%');
  strongGlow.append('feGaussianBlur').attr('stdDeviation', '7').attr('result', 'coloredBlur');
  const fm2 = strongGlow.append('feMerge');
  fm2.append('feMergeNode').attr('in', 'coloredBlur');
  fm2.append('feMergeNode').attr('in', 'SourceGraphic');

  const g = svg.append('g').attr('class', 'graph-root');

  const zoomBehaviour = d3.zoom()
    .scaleExtent([0.06, 4])
    .on('zoom', ({ transform }) => g.attr('transform', transform));

  svg.call(zoomBehaviour);

  /* ── Force simulation — spring physics ──────────────────────── */
  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(allLinks)
      .id(d => d.id)
      .distance(d => {
        if (d.type === 'cross') return 130;
        return d.source.kind === 'category' ? 120 : 80;
      })
      .strength(d => d.type === 'cross' ? 0.04 : 0.42)
    )
    .force('charge', d3.forceManyBody()
      .strength(d => d.kind === 'category' ? -900 : -22)
    )
    .force('collide', d3.forceCollide()
      .radius(d => d.r + 3)
      .iterations(2)
    )
    .force('center', d3.forceCenter(0, 0))
    .alphaDecay(0.007)      // slow cooling → more oscillation
    .velocityDecay(0.20)    // low damping  → springy
    .alphaMin(0.001);       // never fully freezes

  /* ── Render cross-links first (behind everything) ───────────── */
  const crossLinkSel = g.append('g')
    .attr('class', 'cross-links')
    .selectAll('line')
    .data(crossLinks)
    .join('line')
    .attr('stroke', d => LAYER_COLORS[d.layer] || '#555')
    .attr('stroke-opacity', 0.13)
    .attr('stroke-width', 0.55)
    .attr('stroke-dasharray', '4,5');

  /* ── Render category→tool links ─────────────────────────────── */
  const catLinkSel = g.append('g')
    .attr('class', 'cat-links')
    .selectAll('line')
    .data(catLinks)
    .join('line')
    .attr('stroke', d => LAYER_COLORS[d.layer] || '#555')
    .attr('stroke-opacity', 0.18)
    .attr('stroke-width', 0.85);

  /* ── Render nodes ───────────────────────────────────────────── */
  const nodeSel = g.append('g')
    .attr('class', 'nodes')
    .selectAll('g')
    .data(nodes)
    .join('g')
    .attr('class', d => `node node--${d.kind}`)
    .call(drag(sim));

  // Circle
  nodeSel.append('circle')
    .attr('r', d => d.r)
    .attr('fill', d => d.kind === 'category' ? d.color : d.color)
    .attr('fill-opacity', d => d.kind === 'category' ? 0.92 : 0.72)
    .attr('stroke', d => d.kind === 'category' ? 'rgba(255,255,255,0.7)' : 'none')
    .attr('stroke-width', d => d.kind === 'category' ? 1.8 : 0)
    .attr('filter', d => {
      if (d.kind === 'category')  return 'url(#strong-glow)';
      if (d.issueCount >= 3)      return 'url(#glow)';
      return 'none';
    });

  // Category labels
  nodeSel.filter(d => d.kind === 'category')
    .append('text')
    .text(d => d.label.length > 28 ? d.label.substring(0, 26) + '…' : d.label)
    .attr('text-anchor', 'middle')
    .attr('dy', d => d.r + 14)
    .attr('fill', '#f0ecff')
    .attr('font-size', '11px')
    .attr('font-family', '"Orbitron", "Space Grotesk", Helvetica, sans-serif')
    .attr('font-weight', '700')
    .attr('letter-spacing', '0.02em')
    .style('pointer-events', 'none')
    .style('text-shadow', '0 1px 8px #000, 0 0 14px #000');

  /* ── Tick ───────────────────────────────────────────────────── */
  sim.on('tick', () => {
    catLinkSel
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    crossLinkSel
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    nodeSel.attr('transform', d => `translate(${d.x},${d.y})`);
  });

  /* ── Centre on first stable frame ──────────────────────────── */
  sim.on('end', () => {
    const cx = W() / 2, cy = H() / 2;
    svg.call(
      d3.zoom().transform,
      d3.zoomIdentity.translate(cx, cy).scale(0.65)
    );
  });

  // Initial zoom so graph appears centred
  svg.call(
    zoomBehaviour,
    d3.zoomIdentity.translate(W() / 2, H() / 2).scale(0.62)
  );

  /* ── Tooltip ────────────────────────────────────────────────── */
  const tooltip = document.getElementById('graph-tooltip');
  const ttName  = document.getElementById('tt-name');
  const ttCat   = document.getElementById('tt-cat');
  const ttBlurb = document.getElementById('tt-blurb');
  const ttUrl   = document.getElementById('tt-url');
  const ttClick = document.getElementById('tt-click');

  nodeSel
    .on('mouseenter', function(event, d) {
      if (d.kind === 'category') {
        ttName.textContent  = d.label;
        ttCat.textContent   = `${d.layer} · ${d.count} tools`;
        ttBlurb.textContent = '';
        ttUrl.textContent   = '';
        ttClick.textContent = '';
      } else {
        ttName.textContent  = d.label;
        ttCat.textContent   = d.category +
          (d.issueCount > 0 ? ` · in ${d.issueCount} issue${d.issueCount > 1 ? 's' : ''}` : '');
        ttBlurb.textContent = d.blurb || '';
        ttUrl.textContent   = d.url ? '↗ ' + d.url.replace(/^https?:\/\//, '') : '';
        ttClick.textContent = d.url ? 'Click to open →' : '';
      }
      tooltip.classList.add('visible');
      positionTooltip(event);
    })
    .on('mousemove', positionTooltip)
    .on('mouseleave', () => {
      tooltip.classList.remove('visible');
    })
    .on('click', (event, d) => {
      event.stopPropagation();
      openDetailPanel(d);
    });

  /* ── Detail panel ───────────────────────────────────────────── */
  const panel    = document.getElementById('detail-panel');
  const dpName   = document.getElementById('dp-name');
  const dpMeta   = document.getElementById('dp-meta');
  const dpBlurb  = document.getElementById('dp-blurb');
  const dpIssues = document.getElementById('dp-issues');
  const dpLink   = document.getElementById('dp-link');

  function openDetailPanel(d) {
    dpName.textContent = d.label;
    dpName.style.color = d.color;

    if (d.kind === 'category') {
      dpMeta.textContent   = d.layer;
      dpBlurb.innerHTML    = `<div class="dp-cat-count">${d.count}</div><div class="dp-cat-label">tools in this category</div>`;
      dpIssues.innerHTML   = '';
      dpLink.style.display = 'none';
    } else {
      dpMeta.textContent  = `${d.category} · ${d.layer}`;
      dpBlurb.textContent = d.blurb || '';
      dpIssues.innerHTML  = '';

      if (d.issues.length > 0) {
        const lbl = document.createElement('div');
        lbl.className   = 'dp-issues-label';
        lbl.textContent = 'Featured in newsletters';
        dpIssues.appendChild(lbl);

        const wrap = document.createElement('div');
        wrap.className = 'dp-issues-badges';
        [...d.issues].sort((a, b) => a - b).forEach(n => {
          const badge     = document.createElement('a');
          badge.href      = `issue.html?n=${n}`;
          badge.className = 'dp-issue-badge';
          badge.textContent = `#${n}`;
          wrap.appendChild(badge);
        });
        dpIssues.appendChild(wrap);
      }

      if (d.url) {
        dpLink.href          = d.url;
        dpLink.style.display = 'flex';
      } else {
        dpLink.style.display = 'none';
      }
    }
    panel.classList.add('is-open');
  }

  function closeDetailPanel() {
    panel.classList.remove('is-open');
  }

  document.getElementById('detail-close').addEventListener('click', closeDetailPanel);
  svg.on('click', closeDetailPanel);   // close when clicking canvas background
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDetailPanel(); });

  function positionTooltip(event) {
    const pad = 16;
    const tw = tooltip.offsetWidth  || 280;
    const th = tooltip.offsetHeight || 100;
    let x = event.clientX + pad;
    let y = event.clientY + pad;
    if (x + tw > window.innerWidth  - pad) x = event.clientX - tw - pad;
    if (y + th > window.innerHeight - pad) y = event.clientY - th - pad;
    tooltip.style.left = x + 'px';
    tooltip.style.top  = y + 'px';
  }

  /* ── Drag — spring bounce on release ────────────────────────── */
  function drag(simulation) {
    return d3.drag()
      .on('start', (event, d) => {
        if (!event.active) simulation.alphaTarget(0.4).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on('drag', (event, d) => {
        d.fx = event.x; d.fy = event.y;
      })
      .on('end', (event, d) => {
        d.fx = null; d.fy = null;
        // Spring bounce: briefly reheat then let cool naturally
        if (!event.active) {
          simulation.alphaTarget(0.08).restart();
          setTimeout(() => simulation.alphaTarget(0), 700);
        }
      });
  }

  /* ── Search ─────────────────────────────────────────────────── */
  const searchInput = document.getElementById('graph-search');
  let searchQuery = '';

  searchInput.addEventListener('input', () => {
    searchQuery = searchInput.value.toLowerCase().trim();
    applyFilters();
  });

  /* ── Layer filter checkboxes ────────────────────────────────── */
  const layers = [...new Set(categories.map(c => c.layer))].sort();
  const activeLayerFilters = new Set(layers); // all on by default

  const filterContainer = document.getElementById('layer-filters');
  layers.forEach(layer => {
    const label = document.createElement('label');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = true;
    checkbox.addEventListener('change', () => {
      if (checkbox.checked) activeLayerFilters.add(layer);
      else activeLayerFilters.delete(layer);
      applyFilters();
    });
    const dot = document.createElement('span');
    dot.className = 'filter-dot';
    dot.style.background = LAYER_COLORS[layer] || '#94a3b8';
    label.appendChild(checkbox);
    label.appendChild(dot);
    label.appendChild(document.createTextNode(' ' + layer));
    filterContainer.appendChild(label);
  });

  /* ── Category legend (click to isolate) ────────────────────── */
  const legendItems = document.getElementById('legend-items');
  let activeCategory = null; // null = show all

  categories.forEach(cat => {
    const item = document.createElement('div');
    item.className = 'legend-item';
    item.dataset.slug = cat.slug;

    const dot = document.createElement('span');
    dot.className = 'legend-dot';
    dot.style.background = catColor(cat);

    item.appendChild(dot);
    item.appendChild(document.createTextNode(
      cat.name.length > 26 ? cat.name.substring(0, 24) + '…' : cat.name
    ));
    item.addEventListener('click', () => {
      if (activeCategory === cat.slug) {
        activeCategory = null;
        document.querySelectorAll('.legend-item').forEach(el => el.classList.remove('dimmed'));
      } else {
        activeCategory = cat.slug;
        document.querySelectorAll('.legend-item').forEach(el => {
          el.classList.toggle('dimmed', el.dataset.slug !== cat.slug);
        });
      }
      applyFilters();
    });
    legendItems.appendChild(item);
  });

  /* ── Filter application ─────────────────────────────────────── */
  function applyFilters() {
    nodeSel.each(function(d) {
      const el = d3.select(this);
      let visible = true;

      if (d.kind === 'category') {
        visible = activeLayerFilters.has(d.layer);
        if (activeCategory && d.slug !== activeCategory) visible = false;
      } else {
        visible = activeLayerFilters.has(d.layer);
        if (activeCategory && d.category_slug !== activeCategory) visible = false;
        if (searchQuery) {
          const match = d.label.toLowerCase().includes(searchQuery) ||
                        (d.blurb || '').toLowerCase().includes(searchQuery) ||
                        d.category.toLowerCase().includes(searchQuery);
          if (!match) visible = false;
        }
      }

      el.attr('opacity', visible ? 1 : 0.05);
    });

    catLinkSel.attr('stroke-opacity', d => {
      const s = d.source, t = d.target;
      const sVis = activeLayerFilters.has(s.layer) &&
                   (!activeCategory || s.slug === activeCategory || s.category_slug === activeCategory);
      const tVis = activeLayerFilters.has(t.layer) &&
                   (!activeCategory || t.slug === activeCategory || t.category_slug === activeCategory);
      return (sVis && tVis) ? 0.18 : 0.018;
    });

    crossLinkSel.attr('stroke-opacity', d => {
      const s = d.source, t = d.target;
      const sVis = activeLayerFilters.has(s.layer) &&
                   (!activeCategory || s.category_slug === activeCategory);
      const tVis = activeLayerFilters.has(t.layer) &&
                   (!activeCategory || t.category_slug === activeCategory);
      return (sVis && tVis) ? 0.11 : 0.01;
    });
  }

  /* ── Resize ──────────────────────────────────────────────────── */
  window.addEventListener('resize', () => {
    sim.force('center', d3.forceCenter(0, 0));
  });

})();

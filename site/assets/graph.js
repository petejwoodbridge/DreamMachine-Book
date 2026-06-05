/* DREAM MACHINE — Knowledge Graph
   D3 v7 force-directed layout
   19 category nodes + 572 tool nodes, spring edges
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
      r: 22,
      count: c.count,
      url: null,
    })),
    ...tools.map((t, i) => ({
      id: `tool:${i}`,
      kind: 'tool',
      label: t.name,
      blurb: t.blurb,
      category: t.category,
      category_slug: t.category_slug,
      layer: t.layer,
      color: LAYER_COLORS[t.layer] || '#94a3b8',
      r: 4.5,
      url: t.url || null,
    })),
  ];

  const links = tools.map((t, i) => ({
    source: `cat:${t.category_slug}`,
    target: `tool:${i}`,
    layer: t.layer,
  }));

  /* ── SVG setup ──────────────────────────────────────────────── */
  const svg = d3.select('#graph-canvas');
  const W = () => svg.node().clientWidth;
  const H = () => svg.node().clientHeight;

  const g = svg.append('g').attr('class', 'graph-root');

  svg.call(
    d3.zoom()
      .scaleExtent([0.08, 4])
      .on('zoom', ({ transform }) => g.attr('transform', transform))
  );

  /* ── Force simulation ───────────────────────────────────────── */
  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links)
      .id(d => d.id)
      .distance(d => d.source.kind === 'category' ? 110 : 70)
      .strength(0.35)
    )
    .force('charge', d3.forceManyBody()
      .strength(d => d.kind === 'category' ? -600 : -18)
    )
    .force('collide', d3.forceCollide()
      .radius(d => d.r + 2.5)
      .iterations(2)
    )
    .force('center', d3.forceCenter(0, 0))
    .alphaDecay(0.015)
    .velocityDecay(0.35);

  /* ── Render links ───────────────────────────────────────────── */
  const linkSel = g.append('g')
    .attr('class', 'links')
    .selectAll('line')
    .data(links)
    .join('line')
    .attr('stroke', d => LAYER_COLORS[d.layer] || '#555')
    .attr('stroke-opacity', 0.10)
    .attr('stroke-width', 0.7);

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
    .attr('fill-opacity', d => d.kind === 'category' ? 0.85 : 0.65)
    .attr('stroke', d => d.kind === 'category' ? '#ffffff' : 'none')
    .attr('stroke-width', d => d.kind === 'category' ? 1.5 : 0)
    .style('filter', d => d.kind === 'category'
      ? `drop-shadow(0 0 8px ${d.color}aa)`
      : 'none'
    );

  // Category labels
  nodeSel.filter(d => d.kind === 'category')
    .append('text')
    .text(d => d.label.length > 28 ? d.label.substring(0, 26) + '…' : d.label)
    .attr('text-anchor', 'middle')
    .attr('dy', d => d.r + 13)
    .attr('fill', '#f5f0ff')
    .attr('font-size', '10px')
    .attr('font-family', '"Helvetica Neue", Helvetica, Arial, sans-serif')
    .attr('font-weight', '600')
    .attr('letter-spacing', '0.01em')
    .style('pointer-events', 'none')
    .style('text-shadow', '0 1px 4px #05050e, 0 0 8px #05050e');

  /* ── Tick ───────────────────────────────────────────────────── */
  sim.on('tick', () => {
    linkSel
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

  // Initial zoom offset so graph appears centred
  svg.call(
    d3.zoom()
      .scaleExtent([0.08, 4])
      .on('zoom', ({ transform }) => g.attr('transform', transform)),
    d3.zoomIdentity.translate(W() / 2, H() / 2).scale(0.65)
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
        ttCat.textContent   = d.category;
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
      if (d.url) window.open(d.url, '_blank', 'noopener');
    });

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

  /* ── Drag behaviour ─────────────────────────────────────────── */
  function drag(simulation) {
    return d3.drag()
      .on('start', (event, d) => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on('drag', (event, d) => {
        d.fx = event.x; d.fy = event.y;
      })
      .on('end', (event, d) => {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null; d.fy = null;
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

      el.attr('opacity', visible ? 1 : 0.06);
    });

    linkSel.attr('stroke-opacity', d => {
      const srcNode = d.source;
      const tgtNode = d.target;
      const srcVis = activeLayerFilters.has(srcNode.layer) &&
                     (!activeCategory || srcNode.slug === activeCategory || srcNode.category_slug === activeCategory);
      const tgtVis = activeLayerFilters.has(tgtNode.layer) &&
                     (!activeCategory || tgtNode.slug === activeCategory || tgtNode.category_slug === activeCategory);
      return (srcVis && tgtVis) ? 0.10 : 0.015;
    });
  }

  /* ── Resize ──────────────────────────────────────────────────── */
  window.addEventListener('resize', () => {
    sim.force('center', d3.forceCenter(0, 0));
  });

})();

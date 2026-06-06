/* ═══════════════════════════════════════════════════════════════════
   DREAM MACHINE — Creative Toolkit page
   Loads tools.json + categories.json, renders visual category tiles,
   enhanced tool cards, and prompting guide cards.
   ═══════════════════════════════════════════════════════════════════ */

/* ── Category visual metadata ─────────────────────────────────────── */
const CAT_META = {
  'foundation':   { emoji: '🧠', label: 'Foundation Models', accent: '#9b6dff', grad: 'linear-gradient(135deg,#667eea,#764ba2)' },
  'video':        { emoji: '🎬', label: 'Video Generation',  accent: '#f5576c', grad: 'linear-gradient(135deg,#f093fb,#f5576c)' },
  'image':        { emoji: '🎨', label: 'Image Generation',  accent: '#c471ed', grad: 'linear-gradient(135deg,#c471ed,#f64f59)' },
  'music-audio':  { emoji: '🎵', label: 'Music & Audio',     accent: '#29d8ff', grad: 'linear-gradient(135deg,#00d2ff,#3a7bd5)' },
  '3d-world':     { emoji: '🌐', label: '3D & Spatial',      accent: '#4facfe', grad: 'linear-gradient(135deg,#4facfe,#00f2fe)' },
  'voice-avatar': { emoji: '🎙️', label: 'Voice & Avatars',   accent: '#43e97b', grad: 'linear-gradient(135deg,#43e97b,#38f9d7)' },
  'agents':       { emoji: '⚡', label: 'AI Agents',         accent: '#fda085', grad: 'linear-gradient(135deg,#f6d365,#fda085)' },
  'legacy':       { emoji: '🛠️', label: 'Creative Suites',   accent: '#66a6ff', grad: 'linear-gradient(135deg,#89f7fe,#66a6ff)' },
  'studios':      { emoji: '✨', label: 'AI Studios',        accent: '#ee3ec9', grad: 'linear-gradient(135deg,#ee3ec9,#9b27af)' },
  'games':        { emoji: '🎮', label: 'Games AI',          accent: '#0fd850', grad: 'linear-gradient(135deg,#0fd850,#f9f047)' },
  'marketing':    { emoji: '📣', label: 'Marketing & Ads',   accent: '#fe5196', grad: 'linear-gradient(135deg,#f77062,#fe5196)' },
  'open-source':  { emoji: '💻', label: 'Open Source',       accent: '#38ef7d', grad: 'linear-gradient(135deg,#11998e,#38ef7d)' },
  'comfyui':      { emoji: '⚙️', label: 'ComfyUI',           accent: '#4fc3f7', grad: 'linear-gradient(135deg,#1e3c72,#2a5298)' },
  'loras':        { emoji: '🔧', label: 'LoRAs & Fine-tuning', accent: '#b721ff', grad: 'linear-gradient(135deg,#b721ff,#21d4fd)' },
  'ip-licensing-governance-and-behavioural-licence-platforms':
                  { emoji: '⚖️', label: 'IP & Licensing',    accent: '#52c234', grad: 'linear-gradient(135deg,#52c234,#2d9921)' },
  'provenance':   { emoji: '🔍', label: 'Provenance',        accent: '#90a4ae', grad: 'linear-gradient(135deg,#757f9a,#d7dde8)' },
  'consumer':     { emoji: '📱', label: 'Consumer Apps',     accent: '#fc466b', grad: 'linear-gradient(135deg,#fc466b,#3f5efb)' },
  'institutions': { emoji: '🏛️', label: 'Studios & Institutions', accent: '#4fc3f7', grad: 'linear-gradient(135deg,#1e3c72,#2a5298)' },
  'techniques':   { emoji: '📐', label: 'Techniques',        accent: '#e57373', grad: 'linear-gradient(135deg,#c94b4b,#4b134f)' },
};

/* ── Prompting guides (curated from the Dream Machine book + newsletter) ── */
const GUIDES = [
  {
    emoji: '🎨',
    title: 'Writing for Image Models',
    subtitle: 'Midjourney · FLUX · Firefly · Stable Diffusion',
    level: 'All levels',
    desc: 'Craft prompts that produce commercial-quality images — consistently.',
    tips: [
      'Lead with subject → mood → style, not just subject. "A tired archivist amid collapsing paper towers, warm chiaroscuro, Edward Hopper oil" beats "old man in a library".',
      'Aspect ratio is a creative decision: 16:9 for cinematic, 2:3 for editorial portrait, 1:1 for album art.',
      'Style references compound: chain artist × medium × era — "Yayoi Kusama × Syd Mead, 1970s sci-fi paperback".',
      'Negative space is underrated — "minimalist composition, generous breathing room" transforms a crowded image.',
    ],
    tags: ['Image', 'Design', 'All levels'],
  },
  {
    emoji: '🎬',
    title: 'Directing AI Video',
    subtitle: 'Sora · Runway Gen-4 · Veo 3 · Kling',
    level: 'Intermediate',
    desc: 'Think like a DP. Camera language, lighting, and motion vocabulary unlock cinematic AI video.',
    tips: [
      'Lead with lens + movement before your subject: "handheld 35mm, slow push in toward—" sets the feel before the content.',
      'Describe lighting quality first: "overcast afternoon, soft diffuse shadows" defines the entire aesthetic.',
      'Short, precise prompts often outperform elaborate ones. Start minimal — add texture after your first generation.',
      'For multi-shot consistency, use character reference images or style seeds and keep your system prompt constant.',
    ],
    tags: ['Video', 'Film', 'Intermediate'],
  },
  {
    emoji: '🎵',
    title: 'Generative Music & Audio',
    subtitle: 'Suno · Udio · Mureka · Stable Audio',
    level: 'All levels',
    desc: 'Stack genre, mood, era, and instrumentation to get tracks that feel intentional, not random.',
    tips: [
      'Layer genre + mood + era: "melancholic lo-fi hip hop, late-night Tokyo, 1993" beats "sad music".',
      'Name the instruments: "upright bass, brushed snare, Fender Rhodes" produces tighter results than genre tags alone.',
      'Describe song structure: mention intro, verse, chorus, breakdown to get full-track architecture.',
      'Use extend and continue features to build in sections — don\'t generate the whole track in one shot.',
    ],
    tags: ['Music', 'Audio', 'All levels'],
  },
  {
    emoji: '🎙️',
    title: 'Voice & Character Direction',
    subtitle: 'ElevenLabs · Heygen · Synthesia · Hedra',
    level: 'All levels',
    desc: 'Get AI voice and avatar performances that feel directed, not generated.',
    tips: [
      'Use emotion tags in scripts: [excited], [whispering], [pause] — tell the model where to breathe.',
      'For voice cloning: record 3–5 mins of clean mono audio at consistent volume. No background noise.',
      'Avatar direction: describe eye contact frequency, gesture pace, and posture — not just the words.',
      'Break long scripts into 20–30 second segments. Consistency degrades over long single generations.',
    ],
    tags: ['Voice', 'Film', 'Marketing'],
  },
  {
    emoji: '🌐',
    title: '3D & World Building',
    subtitle: 'Hunyuan 3D · Marble · ComfyUI · Meshy',
    level: 'Advanced',
    desc: 'Prompt spatial, not pictorial. Think in three dimensions when describing AI-generated environments.',
    tips: [
      'Work macro → micro: define sky, horizon, terrain before zooming to surface detail.',
      'Describe materials physically: "weathered concrete, exposed aggregate, rust stains from rebar" beats "industrial texture".',
      'Lighting in 3D is architecture — specify source position, quality (hard/diffuse), and colour temperature.',
      'Gaussian splatting excels at photorealism; NeRF approaches excel at editability. Know your output target.',
    ],
    tags: ['3D', 'Games', 'Spatial'],
  },
  {
    emoji: '🤖',
    title: 'Claude & ChatGPT for Creative Work',
    subtitle: 'Claude · GPT-5 · Gemini · LLMs',
    level: 'All levels',
    desc: 'LLMs are the creative collaborators you\'ve always wanted — if you know how to brief them.',
    tips: [
      'The best system prompt: "You are a [ROLE] who [SPECIALITY]. The user is [CONTEXT]." Specificity equals better output.',
      'Long context is a superpower. Paste the whole script before asking for notes. The model reads everything.',
      'Chain your prompts: Brainstorm → Evaluate → Develop are three separate prompts, not one.',
      '"Continue in the style of my last paragraph" beats "write it like me" — give examples, not abstractions.',
    ],
    tags: ['LLMs', 'Writing', 'All disciplines'],
  },
  {
    emoji: '⚙️',
    title: 'ComfyUI & Open Pipelines',
    subtitle: 'ComfyUI · Hugging Face · fal · ControlNet',
    level: 'Intermediate → Advanced',
    desc: 'Build modular, reproducible AI pipelines you can version, iterate, and share.',
    tips: [
      'One node cluster per function — prompt conditioning, sampling, VAE decode — then wire them. Modular means debuggable.',
      'Always use a preview node before your full pipeline. Understand your checkpoint\'s behaviour before a 45-minute batch.',
      'LoRA weight 0.7–0.9 is the sweet spot. Below 0.5 the style is lost; above 1.1 artifacts appear.',
      'Save the seed number. Every good output should be exactly reproducible.',
    ],
    tags: ['ComfyUI', 'Open Source', 'Advanced'],
  },
  {
    emoji: '🔧',
    title: 'Fine-tuning & LoRA Training',
    subtitle: 'FLUX LoRAs · Civitai · Krea · Hugging Face',
    level: 'Advanced',
    desc: 'Train custom style models that make your aesthetic portable, consistent, and entirely yours.',
    tips: [
      '15–30 high-quality training images outperform 200 mixed-quality ones, every time. Curation beats volume.',
      'Consistent lighting and camera angle in your training set produces cleaner output. Variation confuses the model.',
      'Trigger words must be unique: "myphotostyle2024" beats "artistic" or "professional". Avoid tokens with strong model priors.',
      'Test at every 500 steps. Overfitting arrives early — when the model only reproduces training images verbatim, stop.',
    ],
    tags: ['Fine-tuning', 'LoRAs', 'Advanced'],
  },
];

/* ── Helpers ──────────────────────────────────────────────────────── */
function esc(s) { return DM.escapeHTML(s); }

/* ── Main ─────────────────────────────────────────────────────────── */
(async () => {
  const [tools, categories] = await Promise.all([
    DM.loadJSON('tools'),
    DM.loadJSON('categories'),
  ]);

  /* ── State ──────────────────────────────────────────────────────── */
  const state = { q: '', cat: null };
  hydrateFromURL();

  /* ── DOM refs ───────────────────────────────────────────────────── */
  const $catGrid   = document.getElementById('cat-grid');
  const $toolGrid  = document.getElementById('tool-grid');
  const $empty     = document.getElementById('tk-empty');
  const $chips     = document.getElementById('active-chips');
  const $count     = document.getElementById('result-count');
  const $total     = document.getElementById('total-count');
  const $search    = document.getElementById('tk-search');
  const $clearAll  = document.getElementById('clear-all');
  const $guides    = document.getElementById('guides-grid');

  /* ── Fill static stats ──────────────────────────────────────────── */
  document.getElementById('stat-tools').textContent  = tools.length.toLocaleString();
  document.getElementById('stat-cats').textContent   = categories.length;
  document.getElementById('stat-guides').textContent = GUIDES.length;
  $total.textContent = tools.length.toLocaleString();
  $search.value = state.q;

  /* ══════════════════════════════════════════════════════════════════
     CATEGORY TILES
     ══════════════════════════════════════════════════════════════════ */
  function renderCatGrid() {
    const catTiles = categories.map(c => {
      const meta = CAT_META[c.slug] || { emoji: '🔮', label: c.name, accent: '#ee3ec9', grad: 'linear-gradient(135deg,#ee3ec9,#00ffff)' };
      const active = state.cat === c.slug;
      return `
        <button class="cat-tile${active ? ' is-active' : ''}"
                data-slug="${esc(c.slug)}"
                style="--cat-accent:${meta.accent};--cat-grad:${meta.grad};"
                aria-pressed="${active}">
          <span class="cat-tile__emoji">${meta.emoji}</span>
          <span class="cat-tile__name">${esc(meta.label)}</span>
          <span class="cat-tile__count">${c.count} tools</span>
        </button>`;
    });

    /* Special tile — Prompting Guides */
    catTiles.push(`
      <button class="cat-tile"
              data-slug="--guides--"
              style="--cat-accent:#00ffff;--cat-grad:linear-gradient(135deg,#00d2ff,#3a7bd5);"
              aria-label="Jump to Prompting Guides">
        <span class="cat-tile__emoji">📚</span>
        <span class="cat-tile__name">Prompting Guides</span>
        <span class="cat-tile__count">${GUIDES.length} guides</span>
      </button>`);

    $catGrid.innerHTML = catTiles.join('');
  }

  /* ══════════════════════════════════════════════════════════════════
     TOOL CARDS
     ══════════════════════════════════════════════════════════════════ */
  function renderToolCard(t) {
    const meta   = CAT_META[t.category_slug] || { accent: '#ee3ec9' };
    const accent = meta.accent;

    const vendor = t.vendor
      ? `<span class="tk-card__vendor">${esc(t.vendor)}</span>`
      : '';
    const link = t.url
      ? `<a class="tk-card__link" href="${esc(t.url)}" target="_blank" rel="noopener">Open ↗</a>`
      : '';
    const pills = (t.issues || []).slice(0, 5).map(n =>
      `<a class="tk-card__pill" href="issue.html?n=${n}" title="Mentioned in Issue ${n}">#${n}</a>`
    ).join('');
    const morePills = (t.issues && t.issues.length > 5)
      ? `<span class="tk-card__pill" style="border:none;background:transparent;color:var(--text-muted)">+${t.issues.length - 5}</span>`
      : '';

    return `
      <article class="tk-card" style="--cat-accent:${accent};">
        <div class="tk-card__head">
          <h3 class="tk-card__name">${esc(t.name)}</h3>
          ${vendor}
        </div>
        <p class="tk-card__blurb">${esc(t.blurb)}</p>
        <div class="tk-card__foot">
          <span class="tk-card__cat">${esc(t.category)}</span>
          ${link}
        </div>
        ${pills ? `<div class="tk-card__issues">${pills}${morePills}</div>` : ''}
      </article>`;
  }

  /* ══════════════════════════════════════════════════════════════════
     FILTER + RENDER TOOLS
     ══════════════════════════════════════════════════════════════════ */
  function applyFilters() {
    const q      = state.q.trim().toLowerCase();
    const tokens = q.length ? q.split(/\s+/).filter(Boolean) : [];

    let filtered = tools.filter(t => {
      if (state.cat && t.category_slug !== state.cat) return false;
      if (tokens.length) {
        const blob = t._s || '';
        for (const tk of tokens) {
          if (!blob.includes(tk)) return false;
        }
      }
      return true;
    });

    /* Sort: name prefix match first, then alpha */
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
      $toolGrid.innerHTML = '';
      $empty.style.display = 'block';
    } else {
      $empty.style.display = 'none';
      $toolGrid.innerHTML = filtered.slice(0, 600).map(renderToolCard).join('');
    }

    renderChips();
    writeURL();
  }

  /* ══════════════════════════════════════════════════════════════════
     ACTIVE FILTER CHIPS
     ══════════════════════════════════════════════════════════════════ */
  function renderChips() {
    const chips = [];
    if (state.cat) {
      const meta = CAT_META[state.cat];
      const label = meta ? meta.label : state.cat;
      chips.push(`
        <button class="tk-chip" data-clear-cat>
          ${esc(label)} <span class="tk-chip__x">×</span>
        </button>`);
    }
    if (state.q.trim()) {
      chips.push(`
        <button class="tk-chip" data-clear-q>
          "${esc(state.q.trim())}" <span class="tk-chip__x">×</span>
        </button>`);
    }
    if (chips.length > 1) {
      chips.push(`<button class="tk-chip tk-chip--clear" data-clear-all>Clear all</button>`);
    }
    $chips.innerHTML = chips.join('');
  }

  /* ══════════════════════════════════════════════════════════════════
     PROMPTING GUIDES
     ══════════════════════════════════════════════════════════════════ */
  function renderGuides() {
    $guides.innerHTML = GUIDES.map(g => `
      <article class="guide-card">
        <div class="guide-card__head">
          <div class="guide-card__icon">${g.emoji}</div>
          <div class="guide-card__meta">
            <h3 class="guide-card__title">${esc(g.title)}</h3>
            <div class="guide-card__subtitle">${esc(g.subtitle)}</div>
            <div class="guide-card__level">${esc(g.level)}</div>
          </div>
        </div>
        <p class="guide-card__desc">${esc(g.desc)}</p>
        <ul class="guide-card__tips">
          ${g.tips.map(tip => `<li>${esc(tip)}</li>`).join('')}
        </ul>
        <div class="guide-card__tags">
          ${g.tags.map(tag => `<span class="guide-card__tag">${esc(tag)}</span>`).join('')}
        </div>
      </article>`).join('');
  }

  /* ══════════════════════════════════════════════════════════════════
     EVENT WIRING
     ══════════════════════════════════════════════════════════════════ */

  /* Category tile clicks */
  $catGrid.addEventListener('click', e => {
    const tile = e.target.closest('.cat-tile');
    if (!tile) return;
    const slug = tile.dataset.slug;

    if (slug === '--guides--') {
      document.getElementById('guides').scrollIntoView({ behavior: 'smooth' });
      return;
    }

    state.cat = state.cat === slug ? null : slug;
    renderCatGrid();
    applyFilters();
  });

  /* Chip clicks */
  $chips.addEventListener('click', e => {
    if (e.target.closest('[data-clear-cat]'))  { state.cat = null; renderCatGrid(); applyFilters(); }
    if (e.target.closest('[data-clear-q]'))    { state.q = ''; $search.value = ''; renderCatGrid(); applyFilters(); }
    if (e.target.closest('[data-clear-all]'))  { clearAll(); }
  });

  /* Clear all button (in empty state) */
  $clearAll.addEventListener('click', clearAll);

  /* Search */
  let debounce;
  $search.addEventListener('input', () => {
    clearTimeout(debounce);
    debounce = setTimeout(() => {
      state.q = $search.value;
      applyFilters();
    }, 100);
  });

  /* ══════════════════════════════════════════════════════════════════
     HELPERS
     ══════════════════════════════════════════════════════════════════ */
  function clearAll() {
    state.q   = '';
    state.cat = null;
    $search.value = '';
    renderCatGrid();
    applyFilters();
  }

  function writeURL() {
    const p = new URLSearchParams();
    if (state.q)   p.set('q',   state.q);
    if (state.cat) p.set('cat', state.cat);
    const qs  = p.toString();
    const url = qs ? `?${qs}` : location.pathname;
    history.replaceState(null, '', url);
  }

  function hydrateFromURL() {
    const p   = new URLSearchParams(location.search);
    state.q   = p.get('q')   || '';
    state.cat = p.get('cat') || null;
  }

  /* ── First paint ────────────────────────────────────────────────── */
  renderCatGrid();
  applyFilters();
  renderGuides();

})();

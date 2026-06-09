/* DREAM MACHINE — shared client utilities */

(() => {
  // Mark the active nav link based on the current pathname
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__link').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      a.classList.add('is-active');
    }
  });

  // Nav dropdown click-toggle (keep open when moving between btn and menu)
  document.querySelectorAll('.nav__drop-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      const drop = btn.closest('.nav__drop');
      const opening = !drop.classList.contains('is-open');
      document.querySelectorAll('.nav__drop.is-open').forEach(d => d.classList.remove('is-open'));
      if (opening) drop.classList.add('is-open');
    });
  });
  document.addEventListener('click', () => {
    document.querySelectorAll('.nav__drop.is-open').forEach(d => d.classList.remove('is-open'));
  });

  // Scroll-reveal observer (graceful, optional)
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.05 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  }
})();

// JSON helpers (used by per-page scripts)
window.DM = {
  async loadJSON(name) {
    // Use pre-bundled data when available (works on file:// and static hosting)
    if (window.DM_DATA && Object.prototype.hasOwnProperty.call(window.DM_DATA, name)) {
      return window.DM_DATA[name];
    }
    const res = await fetch(`data/${name}.json`, { cache: 'no-cache' });
    if (!res.ok) throw new Error(`Failed to load data/${name}.json: ${res.status}`);
    return res.json();
  },
  fmtDate(iso) {
    if (!iso) return '';
    try {
      const d = new Date(iso + 'T00:00:00');
      return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
    } catch { return iso; }
  },
  escapeHTML(s) {
    return String(s ?? '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  },
  qs(name) {
    return new URLSearchParams(location.search).get(name);
  },
};

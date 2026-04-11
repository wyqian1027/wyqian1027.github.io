/* ======================================
   WENYANG QIAN — SITE SCRIPTS
   Handles: tab loading, lang toggle, talks filter
====================================== */

(function () {
  'use strict';

  const cache = {};

  // --- Load a tab's HTML from /tabs/<id>.html ---
  async function loadTab(id) {
    if (cache[id]) return cache[id];
    const res = await fetch(`tabs/${id}.html`);
    if (!res.ok) throw new Error(`Could not load tabs/${id}.html`);
    const html = await res.text();
    cache[id] = html;
    return html;
  }

  // --- Switch tab ---
  async function switchTab(id) {
    const buttons = document.querySelectorAll('.tab-btn');
    const panes   = document.querySelectorAll('.tab-pane');

    // Update nav
    buttons.forEach(b => b.classList.toggle('active', b.dataset.tab === id));

    // Hide all panes, show target
    panes.forEach(p => p.classList.remove('active'));
    const pane = document.getElementById(`tab-${id}`);
    if (!pane) return;
    pane.classList.add('active');

    // Already loaded?
    if (pane.dataset.loaded) return;

    // Show loading state
    pane.innerHTML = '<div class="tab-loading">Loading…</div>';

    try {
      const html = await loadTab(id);
      pane.innerHTML = html;
      pane.dataset.loaded = '1';
      // Post-load hooks
      if (id === 'talks') initTalksFilter(pane);
    } catch (e) {
      pane.innerHTML = '<p style="color:var(--muted);font-size:.85rem">Failed to load content.</p>';
    }
  }

  // --- Talks filter ---
  function initTalksFilter(pane) {
    const buttons = pane.querySelectorAll('.filter-btn');
    const items   = pane.querySelectorAll('.talk-item');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.dataset.filter;
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        items.forEach(item => {
          const show = filter === 'all' || item.dataset.type === filter;
          item.style.display = show ? '' : 'none';
        });
      });
    });
  }

  // --- Language toggle ---
  function initLangToggle() {
    const btn     = document.getElementById('lang-toggle');
    const btnText = document.getElementById('lang-btn-text');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const html = document.documentElement;
      if (html.getAttribute('lang') === 'en') {
        html.setAttribute('lang', 'zh');
        btnText.textContent = 'English';
      } else {
        html.setAttribute('lang', 'en');
        btnText.textContent = '中文';
      }
    });
  }

  // --- Wire up tab buttons ---
  function initTabs() {
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });
  }

  // --- Init ---
  document.addEventListener('DOMContentLoaded', () => {
    initLangToggle();
    initTabs();
    // Load the default tab (about) immediately
    switchTab('about');
  });

})();

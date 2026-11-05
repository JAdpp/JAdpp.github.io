// Load silent video loops only while visible. Reduced motion, Save-Data,
// slow connections, and no JavaScript retain the static title cover by default.
(() => {
  const cards = Array.from(document.querySelectorAll('[data-project-preview]'));
  if (!cards.length) return;
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  const saveData = () => Boolean(connection && (connection.saveData || /(^|-)2g$/.test(connection.effectiveType || '')));
  const automatic = () => !motion.matches && !saveData();
  const states = cards.map(card => {
    const video = card.querySelector('[data-preview-video]');
    const button = card.querySelector('[data-preview-toggle]');
    const state = { card, video, button, visible: false, userPaused: false, userPlayed: false, generation: 0 };
    video.muted = true;
    button.hidden = false;
    const updateButton = playing => {
      const label = playing ? button.dataset.pauseLabel : button.dataset.playLabel;
      button.textContent = label;
      button.setAttribute('aria-label', `${label}: ${video.getAttribute('aria-label')}`);
      button.setAttribute('aria-pressed', String(playing));
    };
    state.pause = (poster = false) => {
      // Invalidate any pending play() before pausing. Its eventual completion
      // must not change the state of a newer request.
      state.generation++;
      video.pause();
      updateButton(false);
      if (poster) card.classList.remove('is-playing');
    };
    state.sync = async () => {
      const generation = ++state.generation;
      if (!state.visible || document.hidden || state.userPaused || (!automatic() && !state.userPlayed)) {
        state.pause(!automatic() && !state.userPlayed);
        return;
      }
      if (!video.getAttribute('src')) {
        const small = window.matchMedia('(max-width: 780px)').matches;
        video.src = (small && video.dataset.srcSmall) || video.dataset.src;
        video.load();
      }
      try {
        await video.play();
        if (!state.visible || document.hidden || state.userPaused || (!automatic() && !state.userPlayed)) {
          state.pause(!automatic() && !state.userPlayed);
          return;
        }
        if (generation !== state.generation) return;
        card.classList.add('is-playing');
        updateButton(true);
      } catch (_) {
        if (generation !== state.generation) return;
        state.pause(true); // Autoplay restrictions or decoding errors keep the cover usable.
      }
    };
    button.addEventListener('click', () => {
      if (!video.paused) {
        state.userPaused = true;
        state.userPlayed = false;
        state.pause();
      } else {
        state.userPaused = false;
        state.userPlayed = true;
        state.sync();
      }
    });
    video.addEventListener('error', () => state.pause(true));
    return state;
  });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        const state = states.find(item => item.card === entry.target);
        state.visible = entry.isIntersecting && entry.intersectionRatio >= 0.25;
        state.sync();
      });
    }, { threshold: [0, 0.25], rootMargin: '0px' });
    states.forEach(state => observer.observe(state.card));
  } else {
    // Without an observer, require an explicit play rather than downloading all loops.
    states.forEach(state => { state.visible = true; state.userPaused = true; });
  }
  document.addEventListener('visibilitychange', () => states.forEach(state => state.sync()));
  const preferencesChanged = () => states.forEach(state => {
    state.userPlayed = false;
    state.sync();
  });
  motion.addEventListener?.('change', preferencesChanged);
  connection?.addEventListener?.('change', preferencesChanged);
})();

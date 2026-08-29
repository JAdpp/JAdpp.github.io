(() => {
  const root = document.documentElement;
  const themeToggle = document.querySelector(".theme-toggle");

  const updateThemeToggle = () => {
    if (!themeToggle) {
      return;
    }

    const isDark = root.dataset.theme === "dark";
    const label = isDark ? "Switch to light mode" : "Switch to dark mode";
    themeToggle.setAttribute("aria-label", label);
    themeToggle.setAttribute("aria-pressed", String(isDark));
    themeToggle.title = label;
  };

  if (themeToggle) {
    updateThemeToggle();
    themeToggle.addEventListener("click", () => {
      const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
      root.dataset.theme = nextTheme;

      try {
        localStorage.setItem("ymzhang-theme", nextTheme);
      } catch (_) {
        // Theme switching still works when storage is unavailable.
      }

      updateThemeToggle();
    });
  }

  const header = document.querySelector(".site-header");

  if (header) {
    const updateHeader = () => {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };

    updateHeader();
    window.addEventListener("scroll", updateHeader, { passive: true });
  }

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    return;
  }

  const revealTargets = document.querySelectorAll(
    ".page-shell > section:not(.hero), .page-shell > .publication-list, .page-shell > .project-list"
  );

  revealTargets.forEach((target) => target.classList.add("reveal-section"));
  document.documentElement.classList.add("motion-ready");

  if (!("IntersectionObserver" in window)) {
    revealTargets.forEach((target) => target.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      rootMargin: "0px 0px -8%",
      threshold: 0.08,
    }
  );

  revealTargets.forEach((target) => observer.observe(target));
})();

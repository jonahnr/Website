document.body.classList.add("has-js");

const canvas = document.querySelector("#constellation");
const ctx = canvas.getContext("2d");
const motionLayers = Array.from(document.querySelectorAll(".motion-layer"));
const revealCards = Array.from(document.querySelectorAll(".reveal-card"));
const dropdowns = Array.from(document.querySelectorAll(".nav-dropdown"));
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const carousels = new Map();
const insightFilterButtons = Array.from(document.querySelectorAll("[data-insight-filter]"));
const insightCards = Array.from(document.querySelectorAll(".insight-card[data-category]"));
const insightsResults = document.querySelector("[data-insights-results]");
const insightsSearch = document.querySelector("[data-insights-search]");

let width = 0;
let height = 0;
let points = [];
let pointerX = 0.5;
let pointerY = 0.5;
let frame = null;

function resizeCanvas() {
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = Math.floor(width * ratio);
  canvas.height = Math.floor(height * ratio);
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

  const count = Math.max(42, Math.min(92, Math.floor(width / 17)));
  points = Array.from({ length: count }, () => ({
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * 0.26,
    vy: (Math.random() - 0.5) * 0.26,
    r: 1 + Math.random() * 2.4,
    tone: Math.random()
  }));
}

function drawConstellation() {
  if (reduceMotion.matches) {
    return;
  }

  ctx.clearRect(0, 0, width, height);

  points.forEach((point, index) => {
    point.x += point.vx + (pointerX - 0.5) * 0.05;
    point.y += point.vy + (pointerY - 0.5) * 0.05;

    if (point.x < -32) point.x = width + 32;
    if (point.x > width + 32) point.x = -32;
    if (point.y < -32) point.y = height + 32;
    if (point.y > height + 32) point.y = -32;

    const color = point.tone > 0.74 ? "247, 185, 53" : point.tone > 0.48 ? "24, 211, 181" : "49, 168, 255";
    ctx.beginPath();
    ctx.arc(point.x, point.y, point.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(${color}, 0.56)`;
    ctx.fill();

    for (let next = index + 1; next < points.length; next += 1) {
      const other = points[next];
      const dx = point.x - other.x;
      const dy = point.y - other.y;
      const distance = Math.hypot(dx, dy);

      if (distance < 136) {
        ctx.beginPath();
        ctx.moveTo(point.x, point.y);
        ctx.lineTo(other.x, other.y);
        ctx.strokeStyle = `rgba(49, 168, 255, ${0.12 * (1 - distance / 136)})`;
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }
  });

  frame = requestAnimationFrame(drawConstellation);
}

function updateMotion() {
  if (reduceMotion.matches) {
    motionLayers.forEach((layer) => {
      layer.style.transform = "";
    });
    return;
  }

  motionLayers.forEach((layer) => {
    const depth = Number(layer.dataset.depth || 0);
    layer.style.transform = `translate3d(${(pointerX - 0.5) * depth * -28}px, ${(pointerY - 0.5) * depth * -16}px, 0)`;
  });
}


function updateParallaxScroll() {
  const scrollValue = `${window.scrollY || 0}px`;
  document.documentElement.style.setProperty("--parallax-scroll", scrollValue);
  const fractionalPage = document.querySelector(".fractional-page");
  if (fractionalPage) {
    fractionalPage.style.setProperty("--parallax-scroll", scrollValue);
  }
}

function revealOnScroll() {
  const trigger = window.innerHeight * 0.86;
  revealCards.forEach((card) => {
    card.classList.toggle("is-visible", card.getBoundingClientRect().top < trigger);
  });
}

function setupCarousel(name) {
  const items = Array.from(document.querySelectorAll(`[data-carousel-item="${name}"]`));
  const previous = document.querySelector(`[data-carousel-prev="${name}"]`);
  const next = document.querySelector(`[data-carousel-next="${name}"]`);
  const status = document.querySelector(`[data-carousel-status="${name}"]`);

  if (!items.length || !previous || !next || !status) {
    return;
  }

  const pages = Math.max(...items.map((item) => Number(item.dataset.page || 0))) + 1;
  const state = { index: 0, items, pages, previous, next, status };
  carousels.set(name, state);
  items[0].parentElement?.classList.add("is-carousel-ready");

  function render() {
    state.items.forEach((item) => {
      const isActive = Number(item.dataset.page || 0) === state.index;
      item.classList.toggle("is-hidden", !isActive);
      item.setAttribute("aria-hidden", String(!isActive));
    });

    state.status.textContent = `${state.index + 1} / ${state.pages}`;
  }

  previous.addEventListener("click", () => {
    state.index = (state.index - 1 + state.pages) % state.pages;
    render();
  });

  next.addEventListener("click", () => {
    state.index = (state.index + 1) % state.pages;
    render();
  });

  render();
}

function setupInsightFilters() {
  if (!insightFilterButtons.length || !insightCards.length) {
    return;
  }

  let activeCategory = "all";

  function renderFilter(category) {
    activeCategory = category;
    const query = (insightsSearch?.value || "").trim().toLowerCase();
    let visibleCount = 0;
    insightCards.forEach((card) => {
      const categoryMatches = category === "all" || card.dataset.category === category;
      const textMatches = !query || card.textContent.toLowerCase().includes(query);
      const isVisible = categoryMatches && textMatches;
      card.classList.toggle("is-filtered-out", !isVisible);
      card.setAttribute("aria-hidden", String(!isVisible));
      if (isVisible) {
        visibleCount += 1;
      }
    });

    const insightsPage = document.querySelector(".insights-page");
    if (insightsPage) {
      insightsPage.dataset.activeFilter = category;
    }

    if (insightsResults) {
      const categoryLabel = category === "all" ? "articles" : `${category} articles`;
      insightsResults.textContent = query ? `${visibleCount} matching ${categoryLabel}` : `${visibleCount} ${categoryLabel}`;
    }
  }

  insightFilterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      insightFilterButtons.forEach((item) => item.classList.toggle("is-active", item === button));
      renderFilter(button.dataset.insightFilter || "all");
    });
  });

  if (insightsSearch) {
    insightsSearch.addEventListener("input", () => renderFilter(activeCategory));
  }

  renderFilter("all");
}

function closeDropdowns(except = null) {
  dropdowns.forEach((dropdown) => {
    if (dropdown === except) {
      return;
    }

    dropdown.classList.remove("is-open");
    const toggle = dropdown.querySelector(".nav-dropdown-toggle");
    if (toggle) {
      toggle.setAttribute("aria-expanded", "false");
    }
  });
}

function setupDropdowns() {
  dropdowns.forEach((dropdown) => {
    if (dropdown.tagName === "DETAILS") {
      return;
    }

    const toggle = dropdown.querySelector(".nav-dropdown-toggle");
    if (!toggle) {
      return;
    }

    const isLinkToggle = toggle.tagName.toLowerCase() === "a" && toggle.getAttribute("href");
    if (isLinkToggle) {
      toggle.setAttribute("aria-haspopup", "true");
      return;
    }

    function toggleDropdown(event) {
      event.stopPropagation();
      event.preventDefault();
      const willOpen = !dropdown.classList.contains("is-open");
      closeDropdowns(dropdown);
      dropdown.classList.toggle("is-open", willOpen);
      toggle.setAttribute("aria-expanded", String(willOpen));
    }

    toggle.addEventListener("click", toggleDropdown);
  });

  document.addEventListener("click", () => closeDropdowns());
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeDropdowns();
    }
  });
}



const realParallaxItems = Array.from(document.querySelectorAll('[data-parallax-speed]'));

function updateRealParallax() {
  if (reduceMotion.matches || !realParallaxItems.length) {
    realParallaxItems.forEach((item) => item.style.setProperty('--real-parallax-y', '0px'));
    return;
  }

  const viewportCenter = height / 2;
  realParallaxItems.forEach((item) => {
    const rect = item.getBoundingClientRect();
    const elementCenter = rect.top + rect.height / 2;
    const distanceFromCenter = viewportCenter - elementCenter;
    const normalized = Math.max(-1, Math.min(1, distanceFromCenter / Math.max(height, 1)));
    const speed = Number(item.dataset.parallaxSpeed || 0);
    item.style.setProperty('--real-parallax-y', `${(normalized * speed).toFixed(2)}px`);
  });
}

function setupFractionalFlipCards() {
  const cards = Array.from(document.querySelectorAll(".fractional-flip-card, .pdl-flip-card"));
  if (!cards.length) {
    return;
  }

  cards.forEach((card) => {
    card.setAttribute("role", "button");
    card.setAttribute("aria-pressed", "false");
    card.setAttribute("aria-expanded", "false");

    function setFlipped(isFlipped) {
      card.classList.toggle("is-flipped", isFlipped);
      card.setAttribute("aria-pressed", String(isFlipped));
      card.setAttribute("aria-expanded", String(isFlipped));
    }

    card.addEventListener("click", (event) => {
      const interactive = event.target.closest("a, button, input, textarea, select");
      if (interactive) {
        return;
      }
      setFlipped(!card.classList.contains("is-flipped"));
    });

    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        setFlipped(!card.classList.contains("is-flipped"));
      }

      if (event.key === "Escape") {
        setFlipped(false);
      }
    });
  });
}

window.addEventListener("resize", () => {
  resizeCanvas();
  updateParallaxScroll();
  updateRealParallax();
  revealOnScroll();
});

window.addEventListener("scroll", () => {
  updateParallaxScroll();
  updateRealParallax();
  revealOnScroll();
}, { passive: true });

window.addEventListener("pointermove", (event) => {
  pointerX = event.clientX / Math.max(width, 1);
  pointerY = event.clientY / Math.max(height, 1);
  updateMotion();
  updateRealParallax();
}, { passive: true });

function handleMotionPreferenceChange() {
  if (reduceMotion.matches && frame) {
    cancelAnimationFrame(frame);
    frame = null;
    ctx.clearRect(0, 0, width, height);
  } else if (!frame) {
    drawConstellation();
  }
  updateMotion();
  updateRealParallax();
}

if (reduceMotion.addEventListener) {
  reduceMotion.addEventListener("change", handleMotionPreferenceChange);
} else if (reduceMotion.addListener) {
  reduceMotion.addListener(handleMotionPreferenceChange);
}


function setupFitPathFinder() {
  const finder = document.querySelector("[data-fit-path-finder]");
  if (!finder) {
    return;
  }

  const buttons = Array.from(finder.querySelectorAll("[data-fit-weights]"));
  const cards = Array.from(document.querySelectorAll("[data-offering-path]"));
  const resultTitle = finder.querySelector("[data-fit-result-title]");
  const resultCopy = finder.querySelector("[data-fit-result-copy]");
  const resultLink = finder.querySelector("[data-fit-result-link]");

  const pathDetails = {
    fit: {
      title: "Free Fit Check",
      copy: "Best when you want a no-cost starting point before deciding whether any paid work is needed.",
      href: "analytics-health-check.html#assessment-form-title",
      cta: "Start Free Fit Check"
    },
    health: {
      title: "Analytics Health Check",
      copy: "Best when dashboards exist but trust is low, definitions have drifted, or leaders need a clear current-state readout.",
      href: "analytics-health-check.html",
      cta: "Scope the health check"
    },
    reset: {
      title: "Decision System Reset",
      copy: "Best when reports no longer match how leaders make decisions and the operating model needs to be rebuilt.",
      href: "decision-system-reset.html",
      cta: "Explore the reset"
    },
    fractional: {
      title: "Fractional Analytics Consulting",
      copy: "Best when analytics needs senior ownership, recurring judgment, and standards that stay useful as priorities shift.",
      href: "fractional-analytics.html",
      cta: "Explore fractional support"
    },
    lab: {
      title: "Intelligence Lab",
      copy: "Best when the foundation is stable enough for predictive, governed, or executive intelligence products.",
      href: "intelligence-lab.html",
      cta: "Explore Intelligence Lab"
    }
  };

  const pathOrder = ["fit", "health", "reset", "fractional", "lab"];

  function parseWeights(value) {
    return value.split(",").reduce((weights, item) => {
      const [path, score] = item.split(":");
      const cleanPath = path?.trim();
      const parsedScore = Number(score);
      if (cleanPath && Number.isFinite(parsedScore)) {
        weights[cleanPath] = parsedScore;
      }
      return weights;
    }, {});
  }

  function updateRecommendation() {
    const selected = buttons.filter((button) => button.getAttribute("aria-pressed") === "true");
    const scores = Object.fromEntries(pathOrder.map((path) => [path, 0]));

    selected.forEach((button) => {
      const weights = parseWeights(button.dataset.fitWeights || "");
      Object.entries(weights).forEach(([path, score]) => {
        if (path in scores) {
          scores[path] += score;
        }
      });
    });

    if (!selected.length) {
      cards.forEach((card) => {
        card.classList.remove("is-fit-match", "is-fit-dimmed");
      });
      if (resultTitle) resultTitle.textContent = "Select your needs above";
      if (resultCopy) resultCopy.textContent = "The matching card below will light up once you choose what best describes your situation.";
      if (resultLink) {
        resultLink.href = "analytics-health-check.html#assessment-form-title";
        resultLink.textContent = "Start Free Fit Check";
      }
      return;
    }

    const bestPath = pathOrder.reduce((best, path) => {
      if (scores[path] > scores[best]) return path;
      return best;
    }, pathOrder[0]);

    cards.forEach((card) => {
      const isMatch = card.dataset.offeringPath === bestPath;
      card.classList.toggle("is-fit-match", isMatch);
      card.classList.toggle("is-fit-dimmed", !isMatch);
    });

    const detail = pathDetails[bestPath];
    if (resultTitle) resultTitle.textContent = detail.title;
    if (resultCopy) resultCopy.textContent = detail.copy;
    if (resultLink) {
      resultLink.href = detail.href;
      resultLink.textContent = detail.cta;
    }
  }

  buttons.forEach((button) => {
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => {
      const isPressed = button.getAttribute("aria-pressed") === "true";
      button.setAttribute("aria-pressed", String(!isPressed));
      updateRecommendation();
    });
  });

  updateRecommendation();
}


function setupAnalyticsEventTracking() {
  function sendAnalyticsEvent(eventName, params = {}) {
    if (typeof window.gtag !== "function") {
      return;
    }

    window.gtag("event", eventName, {
      page_path: window.location.pathname,
      page_title: document.title,
      ...params
    });
  }

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) {
      return;
    }

    const href = link.getAttribute("href") || "";
    const text = (link.textContent || "").replace(/\s+/g, " ").trim();
    const destination = link.href || href;
    const classes = link.className || "";
    const eventParams = {
      link_text: text,
      link_url: destination,
      link_classes: String(classes)
    };

    if (/calendly\.com/i.test(destination)) {
      sendAnalyticsEvent("calendly_click", eventParams);
      return;
    }

    if (/mailto:/i.test(href)) {
      sendAnalyticsEvent("email_click", eventParams);
      return;
    }

    if (/analytics-health-check\.html/i.test(destination) || /Free Fit Check|Fit Check/i.test(text)) {
      sendAnalyticsEvent("fit_check_cta_click", eventParams);
      return;
    }

    if (/our-offerings\.html#offer-chooser|Compare Engagement Paths/i.test(destination + " " + text)) {
      sendAnalyticsEvent("offering_compare_click", eventParams);
      return;
    }

    if (/enterprise-outcome-studio|Predictive-Risk-Intelligence/i.test(destination)) {
      sendAnalyticsEvent("external_demo_click", eventParams);
    }
  });

  document.addEventListener("submit", (event) => {
    const form = event.target;
    if (!(form instanceof HTMLFormElement)) {
      return;
    }

    const action = form.getAttribute("action") || "";
    if (/formsubmit\.co/i.test(action)) {
      sendAnalyticsEvent("fit_check_form_submit", {
        form_class: form.className || "",
        form_action: action
      });
    }
  }, true);

  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-fit-option]");
    if (!button) {
      return;
    }

    sendAnalyticsEvent("fit_path_finder_used", {
      option_label: (button.textContent || "").replace(/\s+/g, " ").trim(),
      option_weights: button.dataset.weights || ""
    });
  });
}

resizeCanvas();
drawConstellation();
updateMotion();
updateRealParallax();
revealOnScroll();
setupDropdowns();
setupCarousel("symptom");
setupCarousel("quote");
setupCarousel("failure");
setupCarousel("pattern");
setupCarousel("proof");
setupCarousel("healthSample");
setupFractionalFlipCards();
setupFitPathFinder();
setupAnalyticsEventTracking();






function setupMobileNavigation() {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.mobile-nav-toggle');
  const nav = document.querySelector('#primary-navigation');

  if (!header || !toggle || !nav) {
    return;
  }

  toggle.addEventListener('click', () => {
    const willOpen = !header.classList.contains('is-nav-open');
    header.classList.toggle('is-nav-open', willOpen);
    toggle.setAttribute('aria-expanded', String(willOpen));
  });

  nav.addEventListener('click', (event) => {
    const link = event.target.closest('a');
    if (!link || window.innerWidth > 760) {
      return;
    }
    header.classList.remove('is-nav-open');
    toggle.setAttribute('aria-expanded', 'false');
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 760) {
      header.classList.remove('is-nav-open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
}

setupMobileNavigation();

function getPageKey(pathname) {
  let path = (pathname || "/").split("?")[0].split("#")[0];
  path = path.replace(/\/+$/g, "");

  if (!path || path === "/" || path.toLowerCase() === "/index.html") {
    return "home";
  }

  const lastPart = path.split("/").filter(Boolean).pop() || "index";
  return lastPart.replace(/\.html$/i, "").toLowerCase();
}

function setupActiveNavigation() {
  const nav = document.querySelector("#primary-navigation");
  if (!nav) {
    return;
  }

  const page = getPageKey(window.location.pathname);
  const hash = window.location.hash || "";
  const offeringPages = new Set([
    "our-offerings",
    "analytics-health-check",
    "decision-system-reset",
    "fractional-analytics"
  ]);

  nav.querySelectorAll('a[aria-current="page"]').forEach((link) => {
    link.removeAttribute("aria-current");
    link.classList.remove("is-active");
  });

  nav.querySelectorAll("a").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) {
      return;
    }

    const target = new URL(href, window.location.href);
    const targetPage = getPageKey(target.pathname);
    const targetHash = target.hash || "";
    const isDropdownToggle = link.classList.contains("nav-dropdown-toggle");
    const isDropdownMenuItem = Boolean(link.closest(".nav-dropdown-menu"));
    let isCurrent = false;

    if (isDropdownToggle && link.closest(".nav-dropdown-offerings")) {
      isCurrent = offeringPages.has(page);
    } else if (isDropdownToggle && link.closest(".nav-dropdown-intelligence")) {
      isCurrent = page === "intelligence-lab";
    } else if (isDropdownMenuItem && targetHash) {
      isCurrent = targetPage === page && targetHash === hash;
    } else if (isDropdownMenuItem && targetPage === "intelligence-lab") {
      isCurrent = page === targetPage && !hash;
    } else if (isDropdownMenuItem && targetPage === "our-offerings") {
      isCurrent = page === targetPage;
    } else if (isDropdownMenuItem) {
      isCurrent = targetPage === page && !hash;
    } else {
      isCurrent = targetPage === page && !targetHash;
    }

    if (isCurrent) {
      link.setAttribute("aria-current", "page");
      link.classList.add("is-active");
    }
  });
}

function setupLocalFormFallbacks() {
  const isLocalHtml = window.location.protocol === "file:";
  if (!isLocalHtml) {
    return;
  }

  document.querySelectorAll("form[data-local-mail-fallback]").forEach((form) => {
    const recipient = form.dataset.localMailFallback;
    if (!recipient) {
      return;
    }

    const note = document.createElement("p");
    note.className = "local-form-note";
    note.textContent = "Local preview mode: this form will open an email draft because FormSubmit only works from the hosted site.";
    form.prepend(note);

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const subject = form.dataset.localMailSubject || "Website form request";
      const values = Array.from(form.elements)
        .filter((field) => field.name && !field.name.startsWith("_") && field.type !== "submit")
        .map((field) => `${field.name}: ${field.value || ""}`)
        .join("\n");
      const scorecardUrl = "https://parallaxdatalab.com/dashboard-trust-scorecard-download.html";
      const body = values
        ? `${values}\n\nScorecard link: ${scorecardUrl}`
        : `Please send me the Dashboard Trust & Decision Clarity Scorecard.\n\nScorecard link: ${scorecardUrl}`;
      window.location.href = `mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  });
}

setupActiveNavigation();
setupLocalFormFallbacks();
setupInsightFilters();
window.addEventListener("hashchange", setupActiveNavigation);

document.body.classList.add("has-js");

const canvas = document.querySelector("#constellation");
const ctx = canvas.getContext("2d");
const motionLayers = Array.from(document.querySelectorAll(".motion-layer"));
const revealCards = Array.from(document.querySelectorAll(".reveal-card"));
const dropdowns = Array.from(document.querySelectorAll(".nav-dropdown"));
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const carousels = new Map();

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
      title: "Free Fit Review",
      copy: "Best when you want a no-cost starting point before deciding whether any paid work is needed.",
      href: "analytics-health-check.html",
      cta: "Start with a free fit review"
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
        resultLink.href = "analytics-health-check.html";
        resultLink.textContent = "Start with a free fit review";
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
setupFitPathFinder();





document.body.classList.add("has-js");

const canvas = document.querySelector("#signal-canvas");
const ctx = canvas.getContext("2d");
const layers = Array.from(document.querySelectorAll(".parallax-layer"));
const cards = Array.from(document.querySelectorAll(".model-card, .signal-grid article, .intelligence-board article"));
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

let width = 0;
let height = 0;
let signals = [];
let pointerX = 0.5;
let pointerY = 0.5;
let animationFrame = null;

function resizeCanvas() {
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = Math.floor(width * ratio);
  canvas.height = Math.floor(height * ratio);
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

  const count = Math.max(38, Math.min(88, Math.floor(width / 18)));
  signals = Array.from({ length: count }, () => ({
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * 0.32,
    vy: (Math.random() - 0.5) * 0.32,
    r: 1.2 + Math.random() * 2.2,
    tone: Math.random()
  }));
}

function drawSignals() {
  if (reduceMotion.matches) {
    return;
  }

  ctx.clearRect(0, 0, width, height);

  signals.forEach((signal, index) => {
    signal.x += signal.vx + (pointerX - 0.5) * 0.08;
    signal.y += signal.vy + (pointerY - 0.5) * 0.08;

    if (signal.x < -30) signal.x = width + 30;
    if (signal.x > width + 30) signal.x = -30;
    if (signal.y < -30) signal.y = height + 30;
    if (signal.y > height + 30) signal.y = -30;

    const color = signal.tone > 0.72 ? "255, 211, 25" : signal.tone > 0.46 ? "24, 211, 181" : "23, 143, 255";
    ctx.beginPath();
    ctx.arc(signal.x, signal.y, signal.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(${color}, 0.55)`;
    ctx.fill();

    for (let next = index + 1; next < signals.length; next += 1) {
      const other = signals[next];
      const dx = signal.x - other.x;
      const dy = signal.y - other.y;
      const distance = Math.hypot(dx, dy);

      if (distance < 145) {
        ctx.beginPath();
        ctx.moveTo(signal.x, signal.y);
        ctx.lineTo(other.x, other.y);
        ctx.strokeStyle = `rgba(23, 143, 255, ${0.13 * (1 - distance / 145)})`;
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }
  });

  animationFrame = requestAnimationFrame(drawSignals);
}

function updateParallax() {
  if (reduceMotion.matches) {
    layers.forEach((layer) => {
      layer.style.transform = "";
    });
    return;
  }

  layers.forEach((layer) => {
    const depth = Number(layer.dataset.depth || 0);
    layer.style.transform = `translate3d(${(pointerX - 0.5) * depth * -24}px, ${(pointerY - 0.5) * depth * -14}px, 0)`;
  });
}

function revealCards() {
  const trigger = window.innerHeight * 0.86;
  cards.forEach((card) => {
    const rect = card.getBoundingClientRect();
    card.classList.toggle("is-visible", rect.top < trigger);
  });
}

window.addEventListener("resize", resizeCanvas);
window.addEventListener("scroll", () => {
  revealCards();
}, { passive: true });

window.addEventListener("pointermove", (event) => {
  pointerX = event.clientX / Math.max(width, 1);
  pointerY = event.clientY / Math.max(height, 1);
  updateParallax();
}, { passive: true });

reduceMotion.addEventListener("change", () => {
  if (reduceMotion.matches && animationFrame) {
    cancelAnimationFrame(animationFrame);
    animationFrame = null;
    ctx.clearRect(0, 0, width, height);
  } else if (!animationFrame) {
    drawSignals();
  }
  updateParallax();
});

resizeCanvas();
drawSignals();
updateParallax();
revealCards();

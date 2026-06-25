import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const stories = [
  "manufacturing-throughput",
  "utilities-reliability",
  "energy-operations",
  "logistics-service-level",
  "field-services-kpis",
  "construction-project-controls",
  "healthcare-utilization",
  "industrial-software-revenue",
  "b2b-services-scorecard",
  "retail-multi-location",
  "distribution-supply-chain",
  "facilities-maintenance"
];

function text(html, pattern, fallback = "") {
  return (html.match(pattern)?.[1] || fallback).replace(/<[^>]+>/g, "").trim();
}

function field(html, label) {
  return text(html, new RegExp(`<dt>${label}<\\/dt><dd>([\\s\\S]*?)<\\/dd>`));
}

function fixDetailPaths() {
  for (const slug of stories) {
    const file = join(root, "case-studies", slug, "index.html");
    let html = readFileSync(file, "utf8");
    const title = text(html, /<meta property="og:title" content="([^"]+)"/, text(html, /<title>([\s\S]*?) \| Parallax Data Lab<\/title>/, "Case Study"));
    const description = text(html, /<meta property="og:description" content="([^"]+)"/, "");
    html = html
      .replaceAll('href="../../../', 'href="../../')
      .replaceAll('src="../../../', 'src="../../')
      .replaceAll('href="../../../', 'href="../../')
      .replace(/home\.css\?v=\d+/g, "home.css?v=191")
      .replace(/home\.min\.js\?v=\d+/g, "home.min.js?v=185");
    if (!html.includes('name="twitter:card"')) {
      html = html.replace(
        '<meta property="og:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>',
        `<meta property="og:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="${title.replaceAll('"', "&quot;")}"/>
<meta name="twitter:description" content="${description.replaceAll('"', "&quot;")}"/>
<meta name="twitter:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>`
      );
    }
    writeFileSync(file, html);
  }
}

function summaryCard(slug, prefix) {
  const html = readFileSync(join(root, "case-studies", slug, "index.html"), "utf8");
  const title = text(html, /<h1>([\s\S]*?)<\/h1>/, "Case study");
  const kicker = text(html, /<p class="page-kicker">([\s\S]*?)<\/p>/, "Anonymized case study");
  const challenge = field(html, "Original challenge");
  const outcome = field(html, "Results and outcomes");
  const img = html.match(/<img class="case-story-image"[\s\S]*?>/)?.[0] || "";
  const src = img.match(/src="[^"]*assets\/case-studies\/([^"]+)"/)?.[1] || `${slug}.webp`;
  const alt = img.match(/alt="([^"]+)"/)?.[1] || `${kicker} image`;
  const href = prefix === "" ? `case-studies/${slug}/index.html` : `${slug}/index.html`;
  const imagePrefix = prefix === "" ? "" : "../";
  return `<article class="case-study-expanded industry-case-story case-study-index-summary reveal-card" id="${slug}">
<img class="case-story-image" src="${imagePrefix}assets/case-studies/${src}" alt="${alt}" loading="lazy" decoding="async">
<div class="case-story-copy">
<p class="page-kicker">${kicker}</p>
<h2>${title}</h2>
<dl>
<div><dt>Original challenge</dt><dd>${challenge}</dd></div>
<div><dt>Outcome signal</dt><dd>${outcome}</dd></div>
</dl>
<a class="primary-action" href="${href}">Open case study</a>
</div>
</article>`;
}

function overviewSection(prefix) {
  return `<section class="case-study-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Story details</p>
<h2>Open the case study page for the full executive proof artifact set.</h2>
<p>The overview stays scannable. Each individual case study now has its own page with the impact strip, comparison, architecture, timeline, governance, mockups, and reusable proof visuals.</p>
</div>
<div class="case-study-expanded-grid case-study-overview-grid">
${stories.map((slug) => summaryCard(slug, prefix)).join("\n")}
</div>
</section>`;
}

function fixOverview(file, prefix) {
  const path = join(root, file);
  let html = readFileSync(path, "utf8");
  for (const slug of stories) {
    const href = prefix === "" ? `case-studies/${slug}/index.html` : `${slug}/index.html`;
    html = html.replace(new RegExp(`href="#${slug}"`, "g"), `href="${href}"`);
    html = html.replace(new RegExp(`href="case-studies/${slug}/"`, "g"), `href="case-studies/${slug}/index.html"`);
    html = html.replace(new RegExp(`href="${slug}/"`, "g"), `href="${slug}/index.html"`);
  }
  const storyStart = html.indexOf('<section class="case-study-section reveal-card">\n<div class="case-study-heading">\n<p class="page-kicker">Story details</p>');
  const mainEnd = html.indexOf("</main>", storyStart);
  if (storyStart === -1 || mainEnd === -1) {
    throw new Error(`Could not find story section in ${file}`);
  }
  html = `${html.slice(0, storyStart)}${overviewSection(prefix)}\n${html.slice(mainEnd)}`
    .replace(/<section class="case-study-section proof-library-section reveal-card">[\s\S]*?<\/section>/g, "")
    .replace(/home\.css\?v=\d+/g, "home.css?v=191")
    .replace(/home\.min\.js\?v=\d+/g, "home.min.js?v=185");
  writeFileSync(path, html);
}

fixDetailPaths();
fixOverview("case-studies.html", "");
fixOverview(join("case-studies", "index.html"), "../");

console.log("Fixed case-study detail paths and compact overview output.");

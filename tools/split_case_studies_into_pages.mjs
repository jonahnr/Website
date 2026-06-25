import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));

const rootPage = join(root, "case-studies.html");
const cleanPage = join(root, "case-studies", "index.html");
const rootHtml = readFileSync(rootPage, "utf8");

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

function rewriteLocalPaths(html, prefix) {
  return html
    .replace(/\b(href|src)="(?!https?:|mailto:|tel:|#|\/)([^"]+)"/g, (_match, attr, value) => {
      if (value.startsWith(prefix)) return `${attr}="${value}"`;
      return `${attr}="${prefix}${value}"`;
    })
    .replace(/href="\.\.\/([^"]+)"/g, `href="${prefix}$1"`)
    .replace(/src="\.\.\/([^"]+)"/g, `src="${prefix}$1"`);
}

function stripProof(article) {
  return article.replace(/<div class="case-executive-proof" data-case-proof>[\s\S]*?<\/div>\s*<a class="primary-action"/, '<a class="primary-action"');
}

function getArticle(id) {
  const start = rootHtml.indexOf(`<article class="case-study-expanded industry-case-story reveal-card" id="${id}">`);
  if (start === -1) throw new Error(`Missing article ${id}`);
  const nextStarts = stories
    .map((story) => rootHtml.indexOf(`<article class="case-study-expanded industry-case-story reveal-card" id="${story}">`, start + 1))
    .filter((index) => index > start);
  const end = nextStarts.length ? Math.min(...nextStarts) : rootHtml.indexOf("</div>\n</section>", start);
  return rootHtml.slice(start, end).trim();
}

function articleField(article, label) {
  const match = article.match(new RegExp(`<dt>${label}<\\/dt><dd>([\\s\\S]*?)<\\/dd>`));
  return match ? match[1].replace(/<[^>]+>/g, "").trim() : "";
}

function articleTitle(article) {
  return (article.match(/<h2>([\s\S]*?)<\/h2>/)?.[1] || "Case study").replace(/<[^>]+>/g, "").trim();
}

function articleKicker(article) {
  return (article.match(/<p class="page-kicker">([\s\S]*?)<\/p>/)?.[1] || "Anonymized case study").replace(/<[^>]+>/g, "").trim();
}

function articleImage(article) {
  return article.match(/<img class="case-story-image"[\s\S]*?>/)?.[0] || "";
}

function articleProof(article) {
  return article.match(/<div class="case-executive-proof" data-case-proof>[\s\S]*?<\/div>\s*<a class="primary-action"/)?.[0].replace(/<a class="primary-action"$/, "").trim() || "";
}

function articleCta(article) {
  return article.match(/<a class="primary-action"[\s\S]*?<\/a>/)?.[0] || "";
}

function compactSummary(id, article, prefix) {
  const title = articleTitle(article);
  const kicker = articleKicker(article);
  const challenge = articleField(article, "Original challenge");
  const result = articleField(article, "Results and outcomes");
  const image = rewriteLocalPaths(articleImage(article), prefix);
  return `<article class="case-study-expanded industry-case-story case-study-index-summary reveal-card" id="${id}">
${image}
<div class="case-story-copy">
<p class="page-kicker">${kicker}</p>
<h2>${title}</h2>
<dl>
<div><dt>Original challenge</dt><dd>${challenge}</dd></div>
<div><dt>Outcome signal</dt><dd>${result}</dd></div>
</dl>
<a class="primary-action" href="${prefix === "" ? "case-studies/" : ""}${id}/">Open case study</a>
</div>
</article>`;
}

function buildOverview(file, prefix) {
  let html = readFileSync(join(root, file), "utf8");
  for (const id of stories) {
    const href = prefix === "" ? `case-studies/${id}/` : `${id}/`;
    html = html.replace(new RegExp(`href="#${id}"`, "g"), `href="${href}"`);
  }

  const summaries = stories.map((id) => compactSummary(id, getArticle(id), prefix)).join("\n");
  const replacement = `<section class="case-study-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Story details</p>
<h2>Open the case study page for the full executive proof artifact set.</h2>
<p>The overview stays scannable. Each individual case study now has its own page with the impact strip, comparison, architecture, timeline, governance, mockups, and reusable proof visuals.</p>
</div>
<div class="case-study-expanded-grid case-study-overview-grid">
${summaries}
</div>
</section>`;

  html = html
    .replace(/<section class="case-study-section reveal-card">\s*<div class="case-study-heading">\s*<p class="page-kicker">Story details<\/p>[\s\S]*?<\/div>\s*<\/section>/, replacement)
    .replace(/<section class="case-study-section proof-library-section reveal-card">[\s\S]*?<\/section>/, "")
    .replace(/home\.css\?v=\d+/g, "home.css?v=191")
    .replace(/home\.min\.js\?v=\d+/g, "home.min.js?v=185");
  writeFileSync(join(root, file), html);
}

function buildPage(id, article) {
  const title = articleTitle(article);
  const description = articleField(article, "Results and outcomes") || title;
  const kicker = articleKicker(article);
  const image = rewriteLocalPaths(articleImage(article), "../../");
  const proof = rewriteLocalPaths(articleProof(article), "../../");
  const cta = rewriteLocalPaths(articleCta(article), "../../");
  const details = article.match(/<dl>[\s\S]*?<\/dl>/)?.[0] || "";
  const header = rewriteLocalPaths(rootHtml.slice(rootHtml.indexOf("<header"), rootHtml.indexOf("</header>") + 9), "../../");
  const footer = rewriteLocalPaths(rootHtml.slice(rootHtml.indexOf("<footer"), rootHtml.indexOf("</body>")), "../../")
    .replace(/home\.min\.js\?v=\d+/g, "home.min.js?v=185");

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${title} | Parallax Data Lab</title>
<meta name="description" content="${description.replaceAll('"', "&quot;")}"/>
<link rel="canonical" href="https://parallaxdatalab.com/case-studies/${id}/"/>
<link href="../../home.css?v=191" rel="stylesheet"/>
<meta name="theme-color" content="#0b1745"/>
<link rel="icon" href="../../favicon.ico" sizes="any"/>
<link rel="icon" type="image/png" href="../../favicon.png"/>
<link rel="apple-touch-icon" href="../../apple-touch-icon.png"/>
<meta content="article" property="og:type"/>
<meta content="Parallax Data Lab" property="og:site_name"/>
<meta property="og:title" content="${title.replaceAll('"', "&quot;")}"/>
<meta property="og:description" content="${description.replaceAll('"', "&quot;")}"/>
<meta property="og:url" content="https://parallaxdatalab.com/case-studies/${id}/"/>
<meta property="og:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>
</head>
<body>
<canvas aria-hidden="true" id="constellation"></canvas>
${header}
<main class="case-studies-page case-study-detail-page">
<nav class="case-study-breadcrumb" aria-label="Breadcrumb"><a href="../../case-studies.html">Case Studies</a><span>${kicker}</span></nav>
<article class="case-study-expanded industry-case-story reveal-card" id="${id}">
${image}
<div class="case-story-copy case-detail-copy">
<p class="page-kicker">${kicker}</p>
<h1>${title}</h1>
${details}
${proof}
${cta}
</div>
</article>
</main>
${footer}
</body>
</html>`;
  const dir = join(root, "case-studies", id);
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, "index.html"), html);
}

for (const id of stories) {
  buildPage(id, getArticle(id));
}

buildOverview("case-studies.html", "");
buildOverview(join("case-studies", "index.html"), "../");

console.log(`Split ${stories.length} case studies into individual pages and restored overview summaries.`);

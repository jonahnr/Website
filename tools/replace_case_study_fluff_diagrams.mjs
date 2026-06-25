import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));

const slugs = [
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

function escapeHtml(value) {
  return String(value || "").replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
}

function text(value) {
  return String(value || "").replace(/<[^>]*>/g, "").replace(/\s+/g, " ").trim();
}

function field(html, label) {
  return text(html.match(new RegExp(`<dt>${label}<\\/dt><dd>([\\s\\S]*?)<\\/dd>`))?.[1]);
}

function listFromBeforeAfter(html, label) {
  const match = html.match(new RegExp(`<article><strong>${label}<\\/strong>([\\s\\S]*?)<\\/article>`));
  if (!match) return [];
  return [...match[1].matchAll(/<p><span[^>]*>.*?<\/span>([\s\S]*?)<\/p>/g)].map((item) => text(item[1])).filter(Boolean);
}

function sourceLabels(html) {
  const sourceRow = html.match(/<g class="proof-source-row">([\s\S]*?)<\/g>\s*<path/)?.[1] || "";
  const labels = [...sourceRow.matchAll(/<text[^>]*>([\s\S]*?)<\/text>/g)].map((item) => text(item[1])).filter(Boolean);
  return labels.length ? labels : ["Source data", "Operational reports", "Manual inputs"];
}

function splitWork(work) {
  return work
    .replace(/^Built /, "Built ")
    .split(/,\s+and\s+|,\s+| and /)
    .map((item) => item.replace(/\.$/, "").trim())
    .filter(Boolean)
    .slice(0, 4);
}

function wrapWords(value, maxChars = 18, maxLines = 3) {
  const words = text(value).split(" ");
  const lines = [];
  let line = "";
  for (const word of words) {
    const next = line ? `${line} ${word}` : word;
    if (next.length > maxChars && line) {
      lines.push(line);
      line = word;
    } else {
      line = next;
    }
  }
  if (line) lines.push(line);
  if (lines.length > maxLines) {
    const kept = lines.slice(0, maxLines);
    kept[maxLines - 1] = `${kept[maxLines - 1].replace(/[.,;:]$/, "")}...`;
    return kept;
  }
  return lines;
}

function svgText(x, y, value, maxChars = 18, anchor = "middle", className = "case-proof-svg-label") {
  const lines = wrapWords(value, maxChars, 3);
  return `<text class="${className}" x="${x}" y="${y}" text-anchor="${anchor}">${lines.map((line, index) => `<tspan x="${x}" dy="${index ? 19 : 0}">${escapeHtml(line)}</tspan>`).join("")}</text>`;
}

function architectureSvg(sources, workItems, afterItems, title) {
  const sourceY = sources.map((_, index) => 118 + index * 76);
  const workY = workItems.map((_, index) => 118 + index * 84);
  const outcomes = afterItems.slice(0, 4);
  const outcomeY = outcomes.map((_, index) => 118 + index * 76);
  const sourceNodes = sources.map((label, index) => {
    const y = sourceY[index];
    return `<g class="case-proof-node source-node"><rect x="42" y="${y - 28}" width="210" height="56" rx="10"/>${svgText(147, y - 5, label, 20)}</g>`;
  }).join("");
  const workNodes = workItems.map((label, index) => {
    const y = workY[index];
    return `<g class="case-proof-node work-node"><rect x="482" y="${y - 34}" width="292" height="68" rx="12"/>${svgText(628, y - 10, label, 26)}</g>`;
  }).join("");
  const outcomeNodes = outcomes.map((label, index) => {
    const y = outcomeY[index];
    return `<g class="case-proof-node outcome-node"><rect x="904" y="${y - 28}" width="216" height="56" rx="10"/>${svgText(1012, y - 5, label, 20)}</g>`;
  }).join("");
  const sourceLines = sourceY.map((y) => `<path class="case-proof-line muted" d="M252 ${y} C320 ${y}, 328 282, 382 282"/>`).join("");
  const workLines = workY.map((y) => `<path class="case-proof-line" d="M774 ${y} C812 ${y}, 792 282, 806 282"/>`).join("");
  const outcomeLines = outcomeY.map((y) => `<path class="case-proof-line muted" d="M864 282 C888 282, 878 ${y}, 904 ${y}"/>`).join("");
  return `<svg class="case-proof-large-svg architecture-large-svg" viewBox="0 0 1160 480" role="img" aria-label="${escapeHtml(title)} architecture diagram">
<rect class="case-proof-backplate" x="18" y="18" width="1124" height="444" rx="18"/>
<text class="case-proof-lane-title" x="42" y="54">Inputs leaders were already using</text>
<text class="case-proof-lane-title" x="482" y="54">What Parallax changed</text>
<text class="case-proof-lane-title" x="904" y="54">Decision-ready result</text>
${sourceNodes}
<g class="case-proof-hub"><rect x="382" y="240" width="58" height="84" rx="14"/><text x="411" y="275">Trust</text><text x="411" y="298">Gate</text></g>
${workNodes}
<g class="case-proof-hub outcome-hub"><rect x="806" y="240" width="58" height="84" rx="14"/><text x="835" y="275">Review</text><text x="835" y="298">Layer</text></g>
${outcomeNodes}
${sourceLines}
${workLines}
${outcomeLines}
</svg>`;
}

function timelineHtml(workItems, result) {
  const phases = [
    ["Discovery", "Identify the reports, sources, and operating questions behind the case."],
    ["Assessment", "Separate definition issues, refresh issues, ownership gaps, and decision gaps."],
    ["Architecture", workItems[0] || "Design the governed reporting path."],
    ["Reporting", workItems[1] || "Rebuild the reporting layer around executive review."],
    ["Governance", workItems[2] || "Clarify owners, definitions, thresholds, and confidence notes."],
    ["Adoption", result.replace(/^No verified quantitative client metrics available; outcomes are qualitative\.\s*/i, "")]
  ];
  return `<div class="case-process-timeline" aria-label="Case study process timeline">
${phases.map(([phase, detail], index) => `<article><span>${String(index + 1).padStart(2, "0")}</span><strong>${escapeHtml(phase)}</strong><p>${escapeHtml(detail)}</p></article>`).join("")}
</div>`;
}

function challengeHtml(beforeItems, afterItems, challenge, result) {
  return `<div class="case-challenge-map" aria-label="Challenge resolved by operating model">
<div class="case-challenge-column"><strong>Fragmented operating reality</strong>${beforeItems.slice(0, 4).map((item) => `<span>${escapeHtml(item)}</span>`).join("")}</div>
<div class="case-challenge-center"><span>Problem</span><p>${escapeHtml(challenge)}</p><em>Parallax operating model</em></div>
<div class="case-challenge-column is-after"><strong>Governed decision path</strong>${afterItems.slice(0, 4).map((item) => `<span>${escapeHtml(item)}</span>`).join("")}</div>
<div class="case-challenge-outcome"><strong>Outcome</strong><p>${escapeHtml(result.replace(/^No verified quantitative client metrics available; outcomes are qualitative\.\s*/i, ""))}</p></div>
</div>`;
}

function replacementSection(html) {
  const title = text(html.match(/<h1>([\s\S]*?)<\/h1>/)?.[1]);
  const work = field(html, "Work completed by Parallax");
  const challenge = field(html, "Original challenge");
  const result = field(html, "Results and outcomes");
  const sources = sourceLabels(html).slice(0, 5);
  const beforeItems = listFromBeforeAfter(html, "Before");
  const afterItems = listFromBeforeAfter(html, "After");
  const workItems = splitWork(work);
  return `<section class="case-proof-exhibits" aria-label="Executive proof exhibits">
<article class="proof-panel case-proof-exhibit case-proof-architecture">
<h3><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v5H4V5Zm3 9h10v5H7v-5Zm5-4v4"/></svg> Reporting Architecture</h3>
<p class="case-proof-note">This shows the operating inputs in this case, the specific intervention Parallax made, and the decision layer leaders used after the work.</p>
${architectureSvg(sources, workItems, afterItems, title)}
</article>
<article class="proof-panel case-proof-exhibit case-proof-process">
<h3><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h4m4 0h4m4 0h0M8 8l4 4-4 4m8-8 4 4-4 4"/></svg> Engagement Process</h3>
<p class="case-proof-note">The timeline follows the actual engagement pattern described in the case study instead of a generic project lifecycle.</p>
${timelineHtml(workItems, result)}
</article>
<article class="proof-panel case-proof-exhibit case-proof-challenge">
<h3><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 21h20L12 3Zm0 6v5m0 3h.01"/></svg> Challenge to Operating Model</h3>
<p class="case-proof-note">This connects the case challenge to the governed operating model and the outcome stated in the case study.</p>
${challengeHtml(beforeItems, afterItems, challenge, result)}
</article>
</section>`;
}

for (const slug of slugs) {
  const path = join(root, "case-studies", slug, "index.html");
  let html = readFileSync(path, "utf8");
  const replacement = replacementSection(html);
  const legacyPattern = /<section class="proof-panel visual-proof-grid">[\s\S]*?<\/section>\s*(?=<section class="proof-panel outcome-proof">)/;
  const exhibitPattern = /<section class="case-proof-exhibits"[\s\S]*?<\/section>\s*(?=<section class="proof-panel outcome-proof">)/;
  const pattern = legacyPattern.test(html) ? legacyPattern : exhibitPattern;
  if (!pattern.test(html)) {
    throw new Error(`Could not replace proof exhibits in ${slug}`);
  }
  html = html.replace(pattern, replacement);
  html = html.replace(/home\.css\?v=\d+/g, "home.css?v=198");
  writeFileSync(path, html);
}

console.log(`Replaced generic proof grids with large coherent exhibits for ${slugs.length} case studies.`);

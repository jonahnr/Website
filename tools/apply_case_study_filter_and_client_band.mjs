import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));

const cases = [
  ["manufacturing-throughput", "Manufacturing", "Power BI, Microsoft Fabric, Snowflake, dbt", "manufacturing throughput finance operations quality ERP governed model"],
  ["utilities-reliability", "Utilities", "Power BI, Azure, Microsoft Fabric, dbt", "utilities reliability exceptions owner refresh confidence asset maintenance compliance"],
  ["energy-operations", "Energy", "Power BI, Databricks, Azure, Snowflake", "energy operations field production safety risk weekly decision cadence"],
  ["logistics-service-level", "Logistics & Transportation", "Power BI, AWS, Snowflake, dbt", "logistics transportation service level bottlenecks routing customer service fleet delivery"],
  ["field-services-kpis", "Field Services", "Power BI, Power BI Embedded, Azure, dbt", "field services kpi completion backlog margin staffing regional owners"],
  ["construction-project-controls", "Construction", "Power BI, Azure, Snowflake", "construction project controls status schedule cost risk subcontractor"],
  ["healthcare-utilization", "Healthcare Operations", "Power BI, Azure, Databricks, Looker", "healthcare utilization staffing appointments service lines refresh timing"],
  ["industrial-software-revenue", "Industrial Software", "Power BI, Power BI Embedded, Snowflake, dbt", "industrial software revenue CRM finance customer billing executive dashboards"],
  ["b2b-services-scorecard", "B2B Services", "Power BI, Looker, dbt, Snowflake", "b2b services scorecard CRM finance delivery management review automation"],
  ["retail-multi-location", "Retail & Multi-Location", "Power BI, Power BI Embedded, Snowflake, AWS", "retail multi location POS labor inventory regional exceptions"],
  ["distribution-supply-chain", "Distribution & Supply Chain", "Power BI, Databricks, Snowflake, dbt", "distribution supply chain inventory orders fulfillment suppliers source path"],
  ["facilities-maintenance", "Facilities & Maintenance", "Power BI, Azure, AWS, Looker", "facilities maintenance work orders assets compliance backlog risk"]
];

const technologies = ["AWS", "Azure", "Databricks", "Power BI", "Power BI Embedded", "Looker", "dbt", "Snowflake", "Microsoft Fabric"];
const clientNames = [
  "Aster Grove", "Blue Ridge Works", "Canton Supply", "Delta Harbor", "Everline Ops", "Foundry Nine",
  "Granite Loop", "Hearthside Systems", "Ironvale", "Juniper Field", "Keystone Route", "Linden Metrics",
  "Maven Point", "Northstar Parts", "Oakline Health", "Prairie Logic", "Quarry Lake", "Redwood Service",
  "Summit Cartage", "TerraGrid", "Union Bay", "Vantage Retail", "Westport Energy", "Yardley Group"
];

function caseMap() {
  return new Map(cases.map(([slug, industry, tech, keywords]) => [slug, { industry, tech, keywords }]));
}

function controls(prefix) {
  const industryOptions = cases.map(([, industry]) => industry).filter((value, index, array) => array.indexOf(value) === index);
  return `<div class="case-study-filter-panel" data-case-study-filters>
<label class="case-filter-search"><span>Search case studies</span><input type="search" data-case-search placeholder="Search by challenge, outcome, or keyword"></label>
<label><span>Industry</span><select data-case-industry><option value="">All industries</option>${industryOptions.map((item) => `<option value="${item}">${item}</option>`).join("")}</select></label>
<label><span>Technology</span><select data-case-technology><option value="">All technologies</option>${technologies.map((item) => `<option value="${item}">${item}</option>`).join("")}</select></label>
<p data-case-filter-count>Showing 12 case studies</p>
</div>`;
}

function clientBand() {
  return `<section class="case-study-section client-proof-band reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Client proof</p>
<h2>Over 50 clients served</h2>
</div>
<img class="client-logo-sheet" src="ASSET_PREFIXassets/case-studies/client-proof-logo-cloud.webp" alt="Anonymized client logo sheet representing over 50 clients served" width="1440" height="520" loading="lazy" decoding="async">
</section>`;
}

function decorateCards(html, prefix) {
  const map = caseMap();
  for (const [slug, data] of map.entries()) {
    const rootHref = prefix === "" ? `case-studies/${slug}/index.html` : `${slug}/index.html`;
    const re = new RegExp(`<a class="industry-case-card" href="${rootHref}">`, "g");
    html = html.replace(re, `<a class="industry-case-card" href="${rootHref}" data-case-card data-industry="${data.industry}" data-technology="${data.tech}" data-keywords="${data.keywords}">`);
  }
  return html;
}

function replaceBottomSection(html) {
  const storyStart = html.indexOf('<section class="case-study-section reveal-card">\n<div class="case-study-heading">\n<p class="page-kicker">Story details</p>');
  const mainEnd = html.indexOf("</main>", storyStart);
  if (storyStart === -1 || mainEnd === -1) {
    throw new Error("Could not locate redundant story-details section.");
  }
  return `${html.slice(0, storyStart)}${clientBand()}\n${html.slice(mainEnd)}`;
}

function addControls(html, prefix) {
  if (html.includes("data-case-study-filters")) return html;
  return html.replace('<div class="industry-case-grid">', `${controls(prefix)}\n<div class="industry-case-grid">`);
}

function updateOverview(file, prefix) {
  const path = join(root, file);
  let html = readFileSync(path, "utf8");
  html = decorateCards(html, prefix);
  html = addControls(html, prefix);
  html = replaceBottomSection(html).replaceAll("ASSET_PREFIX", prefix);
  html = html.replace(/home\.css\?v=\d+/g, "home.css?v=192").replace(/home\.min\.js\?v=\d+/g, "home.min.js?v=186");
  writeFileSync(path, html);
}

updateOverview("case-studies.html", "");
updateOverview(join("case-studies", "index.html"), "../");

console.log("Added case-study filters and client proof band to overview pages.");

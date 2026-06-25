import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));

const cssMarker = "/* Case study executive proof artifact system */";
const jsMarker = "/* Case study executive proof interactions */";

const stories = {
  "manufacturing-throughput": {
    industry: "Manufacturing",
    engagement: "Analytics architecture and reporting reliability",
    timeframe: "Project-based reset",
    services: "Data integration, semantic modeling, reliability checks",
    technologies: ["ERP", "Quality", "Finance", "Operations", "Power BI"],
    impact: [["6", "Source systems"], ["1", "Governed path"], ["Daily", "Reliability checks"], ["Reusable", "Business entities"], ["Trusted", "Performance reporting"]],
    before: ["Six disconnected source systems", "Undocumented extracts", "Copied transformations", "Spreadsheet reconciliation", "No governed reporting path"],
    after: ["Systems of record mapped", "Reusable business entities", "One governed reporting path", "Daily reliability checks", "Trusted operating signal"],
    architectureSources: ["ERP", "Quality", "Finance", "Plant Ops", "Spreadsheets"],
    challengeNodes: ["Finance report", "Operations report", "Quality report", "Plant dashboard"],
    governance: [["Throughput", "Operations"], ["Quality", "Quality"], ["Finance", "Finance"], ["Reliability", "Analytics"]],
    outcome: ["Single source path", "Scalable reporting foundation", "Governed semantic model", "Trusted performance review"]
  },
  "utilities-reliability": {
    industry: "Utilities",
    engagement: "Reliability reporting and owner model",
    timeframe: "Operating review redesign",
    services: "Exception mapping, KPI ownership, refresh confidence",
    technologies: ["Asset data", "Maintenance", "Compliance", "Power BI"],
    impact: [["Current", "Exception view"], ["Named", "Owner paths"], ["Refresh", "Confidence layer"], ["Weekly", "Operating review"]],
    before: ["Reliability signals without age context", "Unclear exception ownership", "Informal escalation", "Stale report noise", "Hard-to-trust reviews"],
    after: ["Exception map", "Source reliability checklist", "KPI owner model", "Refresh-status layer", "Current reliability signals"],
    architectureSources: ["Assets", "Outages", "Maintenance", "Compliance"],
    challengeNodes: ["Asset dashboard", "Outage log", "Maintenance report", "Compliance update"],
    governance: [["Reliability", "Operations"], ["Exceptions", "Field Ops"], ["Refresh", "Analytics"], ["Escalation", "Leadership"]],
    outcome: ["Stale noise separated", "Current signals visible", "Owner response clarified", "Escalation path defined"]
  },
  "energy-operations": {
    industry: "Energy",
    engagement: "Operating-signal model",
    timeframe: "Weekly cadence reset",
    services: "Risk ranking, confidence notes, decision cadence",
    technologies: ["Field updates", "Production", "Safety", "Power BI"],
    impact: [["Several", "Field inputs"], ["Ranked", "Exceptions"], ["Weekly", "Decision cadence"], ["Clear", "Attention queue"]],
    before: ["Operational updates from several teams", "Risk context scattered", "Exceptions not ranked", "Owner response unclear", "Every signal became another dashboard"],
    after: ["Field activity connected", "Production context included", "Ranked exceptions", "Confidence notes", "Executive action path"],
    architectureSources: ["Field Ops", "Production", "Safety", "Maintenance"],
    challengeNodes: ["Field update", "Production note", "Safety context", "Leadership report"],
    governance: [["Risk", "Operations"], ["Production", "Field Ops"], ["Confidence", "Analytics"], ["Response", "Leadership"]],
    outcome: ["Clearer attention queue", "Risk-focused review", "Decision cadence created", "Dashboard sprawl reduced"]
  },
  "logistics-service-level": {
    industry: "Logistics & Transportation",
    engagement: "Service-level KPI reset",
    timeframe: "Weekly operating review",
    services: "Threshold design, routing decisions, owner response",
    technologies: ["Fleet", "Delivery", "Customer service", "Power BI"],
    impact: [["Service", "Thresholds"], ["Owner", "Response paths"], ["Earlier", "Bottleneck visibility"], ["Weekly", "Exception review"]],
    before: ["Activity volume without action priority", "Bottlenecks surfaced late", "Service exceptions mixed together", "Owner response unclear", "Review process inconsistent"],
    after: ["Service-level thresholds", "Exception owners", "Routing decisions", "Refresh confidence", "Standard weekly action path"],
    architectureSources: ["Fleet", "Delivery", "Backlog", "Customer Service"],
    challengeNodes: ["Fleet dashboard", "Delivery report", "Backlog view", "Service desk report"],
    governance: [["Service Level", "Operations"], ["Routing", "Dispatch"], ["Backlog", "Managers"], ["Refresh", "Analytics"]],
    outcome: ["Bottlenecks surfaced earlier", "Weekly path standardized", "Action thresholds clear", "Owners visible"]
  },
  "field-services-kpis": {
    industry: "Field Services",
    engagement: "KPI ownership and decision cadence",
    timeframe: "Weekly operating cadence",
    services: "KPI definitions, owners, thresholds, decisions",
    technologies: ["Regional ops", "Scheduling", "Finance", "Power BI"],
    impact: [["5", "Disputed KPIs"], ["5", "Named owners"], ["1", "Weekly action cadence"], ["Clear", "Interpretation rights"]],
    before: ["Different regional KPI definitions", "Completion-rate debates", "Backlog interpretation drift", "Margin logic inconsistent", "Delayed staffing calls"],
    after: ["Defined priority KPIs", "Named business owners", "Documented thresholds", "Metrics tied to decisions", "Weekly action cadence"],
    architectureSources: ["Regional Ops", "Scheduling", "Finance", "Service Work"],
    challengeNodes: ["Completion dashboard", "Backlog tracker", "Margin report", "Staffing view"],
    governance: [["Completion", "Operations"], ["Backlog", "Service"], ["Margin", "Finance"], ["Staffing", "Regional Lead"]],
    outcome: ["Single KPI definitions", "Owners named", "Weekly decisions tied", "Interpretation visible"]
  },
  "construction-project-controls": {
    industry: "Construction",
    engagement: "Project controls reporting workflow",
    timeframe: "Workflow standardization",
    services: "Status mapping, definition standards, executive summaries",
    technologies: ["Project status", "Schedule", "Cost", "Risk logs"],
    impact: [["Standard", "Status workflow"], ["Single", "Risk structure"], ["Cleaner", "Executive summary"], ["Consistent", "Variance review"]],
    before: ["Manual project updates", "Overlapping risk logs", "Different status versions", "Duplicated summaries", "Hard-to-scan variance"],
    after: ["Recurring reporting steps mapped", "Project definitions standardized", "Cleaner reporting workflow", "Consistent status view", "Next actions visible"],
    architectureSources: ["Schedule", "Cost", "Risk", "Subcontractor"],
    challengeNodes: ["Status deck", "Risk log", "Cost update", "Schedule report"],
    governance: [["Status", "Project Controls"], ["Variance", "Finance"], ["Risk", "PMO"], ["Next Action", "Project Lead"]],
    outcome: ["Duplicated work reduced", "Status definitions aligned", "Variance easier to review", "Next actions clearer"]
  },
  "healthcare-utilization": {
    industry: "Healthcare Operations",
    engagement: "Utilization reporting reliability",
    timeframe: "Review confidence reset",
    services: "Definition documentation, source timing, confidence notes",
    technologies: ["Utilization", "Staffing", "Appointments", "Power BI"],
    impact: [["Governed", "Definitions"], ["Source", "Timing notes"], ["Fewer", "Definition debates"], ["Clearer", "Exception context"]],
    before: ["Reports existed but trust was low", "Refresh timing unclear", "Utilization definitions drifted", "Manual adjustments hidden", "Exception context missing"],
    after: ["Definitions documented", "Source timing visible", "Manual adjustments noted", "Confidence notes added", "Exception discussion improved"],
    architectureSources: ["Utilization", "Staffing", "Appointments", "Service Lines"],
    challengeNodes: ["Utilization report", "Staffing view", "Appointment flow", "Service-line update"],
    governance: [["Utilization", "Operations"], ["Staffing", "Clinical Ops"], ["Timing", "Analytics"], ["Exceptions", "Service Line"]],
    outcome: ["Clearer utilization signal", "Fewer definition debates", "Refresh confidence improved", "Exceptions easier to discuss"]
  },
  "industrial-software-revenue": {
    industry: "Industrial Software",
    engagement: "Executive revenue dashboard consolidation",
    timeframe: "Dashboard and logic reset",
    services: "Report inventory, owner mapping, revenue definition",
    technologies: ["CRM", "Finance", "Customer data", "Power BI"],
    impact: [["14", "Reports"], ["4", "Executive views"], ["1", "Revenue definition"], ["Mapped", "Dashboard owners"]],
    before: ["Fourteen overlapping reports", "Conflicting revenue logic", "Duplicate executive dashboards", "Unclear report owners", "Revenue reconciliation meetings"],
    after: ["Four executive views", "One governed revenue definition", "Owners mapped", "Duplicate views consolidated", "Action-oriented revenue review"],
    architectureSources: ["CRM", "Finance", "Customer", "Billing"],
    challengeNodes: ["Sales dashboard", "Finance report", "Customer view", "Executive dashboard"],
    governance: [["Revenue", "Finance"], ["Pipeline", "Sales"], ["Customers", "CS"], ["Definition", "Executive Owner"]],
    outcome: ["Reports consolidated", "Revenue definition governed", "Owners visible", "Conversations moved to action"]
  },
  "b2b-services-scorecard": {
    industry: "B2B Services",
    engagement: "Management scorecard automation",
    timeframe: "Recurring report automation",
    services: "Automated refresh, definitions, scorecard rebuild",
    technologies: ["CRM", "Finance", "Delivery", "Power BI"],
    impact: [["CRM", "Source input"], ["Finance", "Source input"], ["Delivery", "Source input"], ["Automated", "Refresh path"], ["Weekly", "Management review"]],
    before: ["CRM exports copied manually", "Finance data pasted into reports", "Delivery data assembled by managers", "Recurring scorecards rebuilt", "Definitions inconsistent"],
    after: ["Automated refresh path", "Documented definitions", "Scorecard tied to decisions", "Consistent weekly review", "Manual effort reduced"],
    architectureSources: ["CRM", "Finance", "Delivery", "Status Reports"],
    challengeNodes: ["CRM export", "Finance file", "Delivery tracker", "Scorecard deck"],
    governance: [["Pipeline", "Sales"], ["Revenue", "Finance"], ["Delivery", "Operations"], ["Scorecard", "Management"]],
    outcome: ["Manual assembly reduced", "Weekly scorecard stabilized", "Definitions documented", "Review consistency improved"]
  },
  "retail-multi-location": {
    industry: "Retail & Multi-Location",
    engagement: "Location performance reporting alignment",
    timeframe: "Regional review reset",
    services: "KPI standardization, operating signal separation, owner response",
    technologies: ["POS", "Labor", "Inventory", "Power BI"],
    impact: [["Aligned", "Location metrics"], ["Separated", "Signal vs context"], ["Owner", "Follow-up"], ["Regional", "Exception review"]],
    before: ["Stores interpreted metrics differently", "Regional movement disputed", "Context metrics mixed with signals", "Exceptions scattered", "Follow-up ownership unclear"],
    after: ["Standard KPI definitions", "Operating signals separated", "Action thresholds clarified", "Owner response visible", "Regional review focused"],
    architectureSources: ["POS", "Labor", "Inventory", "Regional Ops"],
    challengeNodes: ["Store dashboard", "Labor report", "Inventory view", "Regional deck"],
    governance: [["Sales", "Store Ops"], ["Labor", "Regional Lead"], ["Inventory", "Supply Chain"], ["Exceptions", "Operations"]],
    outcome: ["Location metrics aligned", "Interpretation gaps reduced", "Thresholds clearer", "Leadership follow-up improved"]
  },
  "distribution-supply-chain": {
    industry: "Distribution & Supply Chain",
    engagement: "Governed supply-chain reporting foundation",
    timeframe: "Architecture foundation",
    services: "Source dependency mapping, entity documentation, reporting foundation",
    technologies: ["Inventory", "Orders", "Fulfillment", "Power BI"],
    impact: [["Mapped", "Source dependencies"], ["Documented", "Business entities"], ["Governed", "Reporting foundation"], ["Decision", "Ready review"]],
    before: ["Inventory signals available", "Source path ungoverned", "Business entities undocumented", "Operating review slow", "Future intelligence blocked"],
    after: ["Source dependencies mapped", "Business entities documented", "Governed reporting foundation", "Inventory exceptions visible", "Future intelligence path clearer"],
    architectureSources: ["Inventory", "Orders", "Fulfillment", "Suppliers"],
    challengeNodes: ["Inventory report", "Order tracker", "Fulfillment view", "Supplier update"],
    governance: [["Inventory", "Supply Chain"], ["Orders", "Operations"], ["Fulfillment", "Warehouse"], ["Source Path", "Analytics"]],
    outcome: ["Reliable foundation created", "Source path governed", "Inventory signals clearer", "Future intelligence enabled"]
  },
  "facilities-maintenance": {
    industry: "Facilities & Maintenance",
    engagement: "Backlog and risk decision view",
    timeframe: "Operating cadence reset",
    services: "Decision-focused backlog, thresholds, owner notes",
    technologies: ["Work orders", "Assets", "Compliance", "Power BI"],
    impact: [["Prioritized", "Backlog view"], ["Recurring", "Risk review"], ["Owner", "Response path"], ["Explicit", "Follow-up"]],
    before: ["Backlog reports existed", "Risk lists hard to prioritize", "Intervention needs unclear", "Owner notes informal", "Follow-up scattered"],
    after: ["Decision-focused backlog view", "Exception thresholds", "Owner notes", "Operating cadence", "Priority and follow-up explicit"],
    architectureSources: ["Work Orders", "Assets", "Compliance", "Backlog"],
    challengeNodes: ["Work-order list", "Backlog report", "Risk tracker", "Maintenance review"],
    governance: [["Backlog", "Maintenance"], ["Risk", "Facilities"], ["Compliance", "Operations"], ["Follow-up", "Owner"]],
    outcome: ["Priority easier to see", "Owner response path clear", "Maintenance review focused", "Follow-up explicit"]
  }
};

const library = [
  ["semantic-model", "Semantic model", ["Sources", "Business Rules", "Semantic Layer", "Executive View"]],
  ["data-governance", "Data governance", ["Definition", "Owner", "Policy", "Review"]],
  ["dashboard-standardization", "Dashboard standardization", ["Signal Row", "Trends", "Exceptions", "Actions"]],
  ["kpi-ownership", "KPI ownership", ["Metric", "Owner", "Threshold", "Decision"]],
  ["power-bi-architecture", "Power BI architecture", ["Sources", "Model", "Power BI", "Review"]],
  ["fabric-architecture", "Microsoft Fabric architecture", ["Lakehouse", "Pipelines", "Model", "Power BI"]],
  ["data-quality", "Data quality", ["Raw Data", "Validation", "Exceptions", "Confidence"]],
  ["reporting-lifecycle", "Reporting lifecycle", ["Discover", "Build", "Govern", "Adopt"]],
  ["executive-reporting", "Executive reporting", ["KPI", "Trend", "Risk", "Decision"]],
  ["analytics-operating-model", "Analytics operating model", ["Roles", "Cadence", "Backlog", "Outcomes"]],
  ["decision-framework", "Decision framework", ["Event", "Signal", "Review", "Action"]],
  ["data-lineage", "Data lineage", ["System", "Transform", "Model", "Report"]],
  ["reporting-governance", "Reporting governance", ["Inventory", "Owner", "Standard", "Audit"]],
  ["change-management", "Change management", ["Adopt", "Train", "Measure", "Improve"]],
  ["self-service-bi", "Self-service BI", ["Certified Data", "Shared Model", "Explore", "Answer"]]
];

function escapeHtml(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
}

function icon(name) {
  const paths = {
    challenge: "M12 3 2 21h20L12 3Zm0 6v5m0 3h.01",
    solution: "M4 12a8 8 0 1 1 8 8H4v-8Zm8-4v8m-4-4h8",
    result: "M4 17 10 11l4 4 6-8m0 0v6m0-6h-6",
    architecture: "M4 5h16v5H4V5Zm3 9h10v5H7v-5Zm5-4v4",
    process: "M4 12h4m4 0h4m4 0h0M8 8l4 4-4 4m8-8 4 4-4 4",
    dashboard: "M4 5h16v14H4V5Zm3 4h4v3H7V9Zm6 0h4v3h-4V9ZM7 15h10",
    governance: "M12 3 5 6v5c0 5 3.5 8 7 10 3.5-2 7-5 7-10V6l-7-3Zm-3 9 2 2 4-5",
    decision: "M5 4h14v5H5V4Zm0 11h14v5H5v-5Zm7-6v6"
  };
  return `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${paths[name] || paths.result}"/></svg>`;
}

function flowSvg(labels, className = "") {
  const width = 760;
  const gap = width / labels.length;
  const nodes = labels.map((label, index) => {
    const x = Math.round(gap * index + gap / 2);
    return `<g class="proof-svg-node" tabindex="0"><circle cx="${x}" cy="70" r="30"/><text x="${x}" y="125">${escapeHtml(label)}</text></g>`;
  }).join("");
  const lines = labels.slice(1).map((_, index) => {
    const x1 = Math.round(gap * index + gap / 2 + 31);
    const x2 = Math.round(gap * (index + 1) + gap / 2 - 31);
    return `<path class="proof-svg-path" d="M${x1} 70 H${x2}"/>`;
  }).join("");
  return `<svg class="proof-svg ${className}" viewBox="0 0 ${width} 150" role="img" aria-label="${escapeHtml(labels.join(" to "))}">${lines}${nodes}</svg>`;
}

function architectureSvg(story) {
  return `<svg class="proof-svg proof-architecture-svg" viewBox="0 0 760 360" role="img" aria-label="Executive reporting architecture">
<g class="proof-source-row">${story.architectureSources.map((label, index) => `<g class="proof-svg-node" tabindex="0"><rect x="${35 + index * 145}" y="24" width="108" height="54" rx="8"/><text x="${89 + index * 145}" y="57">${escapeHtml(label)}</text></g>`).join("")}</g>
<path class="proof-svg-path" d="M380 84v34"/>
${["Data Validation", "Business Rules", "Governed Semantic Layer", "Executive Reporting", "Trusted Decisions"].map((label, index) => {
  const y = 118 + index * 44;
  return `<g class="proof-svg-node" tabindex="0"><rect x="${index % 2 ? 410 : 210}" y="${y}" width="220" height="34" rx="8"/><text x="${index % 2 ? 520 : 320}" y="${y + 23}">${escapeHtml(label)}</text></g>${index < 4 ? `<path class="proof-svg-path" d="M380 ${y + 35}v20"/>` : ""}`;
}).join("")}
</svg>`;
}

function challengeSvg(story) {
  return `<svg class="proof-svg proof-challenge-svg" viewBox="0 0 760 340" role="img" aria-label="Reporting challenge resolved by governed model">
${story.challengeNodes.map((label, index) => `<g class="proof-svg-node challenge-before" tabindex="0"><rect x="${34 + index * 178}" y="24" width="134" height="54" rx="8"/><text x="${101 + index * 178}" y="57">${escapeHtml(label)}</text></g>`).join("")}
<path class="proof-svg-path warning" d="M380 86v44"/>
<g class="proof-svg-node warning" tabindex="0"><rect x="250" y="130" width="260" height="52" rx="8"/><text x="380" y="163">Conflicting KPIs</text></g>
<path class="proof-svg-path warning" d="M380 184v38"/>
<g class="proof-svg-node warning" tabindex="0"><rect x="250" y="222" width="260" height="52" rx="8"/><text x="380" y="255">Executive Confusion</text></g>
<path class="proof-svg-path" d="M520 248h70v-104h40"/>
<g class="proof-svg-node" tabindex="0"><rect x="630" y="118" width="104" height="52" rx="8"/><text x="682" y="150">Governed Model</text></g>
<path class="proof-svg-path" d="M682 172v38"/>
<g class="proof-svg-node" tabindex="0"><rect x="610" y="210" width="136" height="52" rx="8"/><text x="678" y="242">Trusted Decisions</text></g>
</svg>`;
}

function dashboardMockup(story) {
  return `<div class="dashboard-evolution" aria-label="Dashboard maturity comparison">
<div class="mock-dashboard mock-before"><span>Before</span><div class="mock-grid messy"><i></i><i></i><i></i><i></i><i></i><i></i></div><p>Dense visuals, inconsistent colors, limited hierarchy.</p></div>
<div class="mock-dashboard mock-after"><span>After</span><div class="mock-grid clean"><b></b><b></b><b></b><i></i><i></i><strong></strong></div><p>Executive KPI row, trend context, exception focus, clean navigation.</p></div>
</div>`;
}

function proofBanner() {
  return `<div class="proof-evidence-banner" aria-label="Evidence used"><strong>Evidence used</strong><span>Architecture</span><span>Process</span><span>Governance</span><span>Executive reporting</span><span>Operating model</span><span>Workflow improvement</span></div>`;
}

function storyProof(id, story) {
  const tech = story.technologies;
  return `<div class="case-executive-proof" data-case-proof>
<aside class="case-summary-sidebar" aria-label="Executive summary">
<h3>${icon("result")} Executive Summary</h3>
<dl>
<div><dt>Industry</dt><dd>${escapeHtml(story.industry)}</dd></div>
<div><dt>Engagement</dt><dd>${escapeHtml(story.engagement)}</dd></div>
<div><dt>Services</dt><dd>${escapeHtml(story.services)}</dd></div>
<div><dt>Technology</dt><dd>${escapeHtml(tech.join(", "))}</dd></div>
<div><dt>Timeframe</dt><dd>${escapeHtml(story.timeframe)}</dd></div>
</dl>
</aside>
<section class="impact-strip" aria-label="Executive impact strip">${story.impact.map(([metric, label]) => `<article><strong data-countup="${escapeHtml(metric)}">${escapeHtml(metric)}</strong><span>${escapeHtml(label)}</span></article>`).join("")}</section>
${proofBanner()}
<section class="proof-panel before-after-comparison"><h3>${icon("challenge")} Before vs After</h3><div><article><strong>Before</strong>${story.before.map(item => `<p><span aria-hidden="true">x</span>${escapeHtml(item)}</p>`).join("")}</article><article><strong>After</strong>${story.after.map(item => `<p><span aria-hidden="true">+</span>${escapeHtml(item)}</p>`).join("")}</article></div></section>
<section class="proof-panel visual-proof-grid">
<article><h3>${icon("architecture")} Reporting Architecture</h3>${architectureSvg(story)}</article>
<article><h3>${icon("process")} Process Timeline</h3>${flowSvg(["Discovery", "Assessment", "Architecture", "Reporting", "Governance", "Adoption"], "timeline-svg")}</article>
<article><h3>${icon("challenge")} Challenge Diagram</h3>${challengeSvg(story)}</article>
<article><h3>${icon("dashboard")} Dashboard Evolution</h3>${dashboardMockup(story)}</article>
<article><h3>${icon("architecture")} Data Flow</h3>${flowSvg(["Raw Data", "Validation", "Transform", "Logic", "Semantic Model", "Dashboard", "Decision"], "data-flow-svg")}</article>
<article><h3>${icon("governance")} KPI Governance</h3><div class="kpi-governance">${story.governance.map(([metric, owner]) => `<span><strong>${escapeHtml(metric)}</strong><em>Owner: ${escapeHtml(owner)}</em></span>`).join("")}</div></article>
<article><h3>${icon("decision")} Decision Flow</h3>${flowSvg(["Event", "Trusted Data", "Executive Review", "Decision", "Business Action"], "decision-svg")}</article>
<article><h3>${icon("architecture")} Technology Workflow</h3>${flowSvg([...tech.slice(0, 4), "Governed Model", "Executive Reporting"], "tech-svg")}</article>
</section>
<section class="proof-panel outcome-proof"><h3>${icon("result")} Outcome Cards</h3><div>${["Operational Outcome", "Leadership Outcome", "Technical Outcome", "Business Outcome"].map((label, index) => `<article><strong>${label}</strong><p>${escapeHtml(story.outcome[index] || story.outcome[0])}</p></article>`).join("")}</div></section>
<figure class="case-quote-panel"><blockquote>Observed business outcome: reporting discussions shifted from which number is correct to what decision should we make.</blockquote></figure>
${proofBanner()}
</div>`;
}

function buildLibrarySection(prefix) {
  return `<section class="case-study-section proof-library-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Reusable proof library</p>
<h2>Visual artifacts now available across future articles and service pages.</h2>
<p>These standalone SVGs use the same executive-proof language as the case studies and can be reused without client-specific claims.</p>
</div>
<div class="proof-library-grid">
${library.map(([slug, title]) => `<a href="${prefix}assets/proof-library/${slug}.svg"><img src="${prefix}assets/proof-library/${slug}.svg" alt="${escapeHtml(title)} illustration" loading="lazy" decoding="async"><span>${escapeHtml(title)}</span></a>`).join("")}
</div>
</section>`;
}

function revampHtml(file, prefix) {
  let html = readFileSync(join(root, file), "utf8");
  for (const [id, story] of Object.entries(stories)) {
    const articlePattern = new RegExp(`(<article class="case-study-expanded industry-case-story reveal-card" id="${id}">[\\s\\S]*?<\\/dl>)([\\s\\S]*?)(<a class="primary-action"[\\s\\S]*?<\\/a>\\s*<\\/div>\\s*<\\/article>)`);
    html = html.replace(articlePattern, `$1\n${storyProof(id, story)}\n$3`);
  }
  if (!html.includes("proof-library-section")) {
    html = html.replace("</main>", `${buildLibrarySection(prefix)}\n</main>`);
  }
  html = html.replace(/home\.css\?v=\d+/g, "home.css?v=190").replace(/home\.min\.js\?v=\d+/g, "home.min.js?v=184");
  writeFileSync(join(root, file), html);
}

function svgAsset(title, labels) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" role="img" aria-labelledby="title desc">
<title id="title">${escapeHtml(title)}</title>
<desc id="desc">Reusable Parallax Data Lab executive proof illustration.</desc>
<defs><linearGradient id="bg" x1="0" x2="1"><stop stop-color="#07133a"/><stop offset="1" stop-color="#102d66"/></linearGradient></defs>
<rect width="960" height="520" rx="28" fill="url(#bg)"/>
<path d="M80 404 C260 286 382 446 548 312 S730 190 880 244" fill="none" stroke="#18d3b5" stroke-width="7" stroke-linecap="round" opacity=".7"/>
${labels.map((label, index) => {
  const x = 104 + index * 200;
  const y = index % 2 ? 254 : 154;
  return `<g><rect x="${x}" y="${y}" width="154" height="88" rx="14" fill="#ffffff" opacity=".08" stroke="#7dd3fc" stroke-opacity=".45"/><circle cx="${x + 38}" cy="${y + 44}" r="19" fill="#f7b935"/><text x="${x + 78}" y="${y + 40}" fill="#f6f8ff" font-family="Inter, Arial, sans-serif" font-size="22" font-weight="800">${escapeHtml(label)}</text><text x="${x + 78}" y="${y + 66}" fill="#9fb6d9" font-family="Inter, Arial, sans-serif" font-size="15">proof layer</text></g>`;
}).join("")}
<text x="80" y="90" fill="#f6f8ff" font-family="Inter, Arial, sans-serif" font-size="42" font-weight="900">${escapeHtml(title)}</text>
<text x="80" y="452" fill="#9fb6d9" font-family="Inter, Arial, sans-serif" font-size="22">Executive-ready analytics proof artifact</text>
</svg>`;
}

function writeAssets() {
  const dir = join(root, "assets", "proof-library");
  mkdirSync(dir, { recursive: true });
  for (const [slug, title, labels] of library) {
    writeFileSync(join(dir, `${slug}.svg`), svgAsset(title, labels));
  }
}

const css = `
${cssMarker}
.case-executive-proof {
  display: grid;
  gap: clamp(18px, 3vw, 28px);
  margin: clamp(24px, 4vw, 42px) 0;
}
.case-summary-sidebar,
.proof-panel,
.proof-evidence-banner,
.impact-strip article,
.case-quote-panel {
  border: 1px solid rgba(125, 211, 252, 0.24);
  border-radius: 8px;
  background: rgba(7, 19, 58, 0.76);
  box-shadow: 0 20px 58px rgba(0, 0, 0, 0.18);
}
.case-summary-sidebar {
  padding: clamp(18px, 2.4vw, 24px);
}
.case-summary-sidebar h3,
.proof-panel h3 {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 16px;
  color: #fff;
  font-size: clamp(1.05rem, 1.8vw, 1.28rem);
}
.case-summary-sidebar svg,
.proof-panel h3 svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: var(--gold);
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
.case-summary-sidebar dl {
  margin: 0;
  display: grid;
  gap: 10px;
}
.case-summary-sidebar dl div {
  padding: 0 0 10px;
  border-bottom: 1px solid rgba(255,255,255,.09);
  display: grid;
  grid-template-columns: minmax(94px, .34fr) 1fr;
}
.case-summary-sidebar dt {
  color: var(--gold);
  font-weight: 900;
}
.case-summary-sidebar dd {
  margin: 0;
  color: rgba(246,248,255,.86);
}
.impact-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(138px, 1fr));
  gap: 12px;
}
.impact-strip article {
  min-height: 118px;
  padding: 18px;
  display: grid;
  align-content: center;
  gap: 8px;
  position: relative;
  overflow: hidden;
}
.impact-strip article::after {
  content: "";
  position: absolute;
  inset: auto 18px 14px 18px;
  height: 3px;
  background: linear-gradient(90deg, var(--gold), #18d3b5);
  border-radius: 999px;
}
.impact-strip strong {
  color: #fff;
  font-size: clamp(1.7rem, 4vw, 2.8rem);
  line-height: 1;
}
.impact-strip span {
  color: rgba(246,248,255,.82);
  font-weight: 800;
}
.proof-evidence-banner {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  padding: 14px;
}
.proof-evidence-banner strong {
  color: #fff;
  margin-right: 4px;
}
.proof-evidence-banner span {
  color: rgba(246,248,255,.84);
  border: 1px solid rgba(24,211,181,.28);
  border-radius: 999px;
  padding: 7px 10px;
  background: rgba(24,211,181,.09);
}
.proof-evidence-banner span::before {
  content: "";
  display: inline-block;
  width: 7px;
  height: 7px;
  margin-right: 7px;
  border-radius: 50%;
  background: #18d3b5;
}
.proof-panel {
  padding: clamp(18px, 2.6vw, 26px);
}
.before-after-comparison > div,
.outcome-proof > div {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}
.before-after-comparison article,
.outcome-proof article {
  border-radius: 8px;
  background: rgba(255,255,255,.055);
  padding: 16px;
}
.before-after-comparison article:first-child {
  border: 1px solid rgba(248,113,113,.34);
}
.before-after-comparison article:last-child {
  border: 1px solid rgba(24,211,181,.34);
}
.before-after-comparison strong,
.outcome-proof strong {
  display: block;
  color: #fff;
  margin-bottom: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .78rem;
}
.before-after-comparison p {
  display: flex;
  gap: 9px;
  margin: 10px 0;
  color: rgba(246,248,255,.86);
}
.before-after-comparison p span {
  width: 22px;
  height: 22px;
  flex: 0 0 22px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-weight: 900;
}
.before-after-comparison article:first-child p span {
  color: #fecaca;
  background: rgba(248,113,113,.16);
}
.before-after-comparison article:last-child p span {
  color: #bff8ee;
  background: rgba(24,211,181,.16);
}
.visual-proof-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}
.visual-proof-grid > article {
  min-width: 0;
  border-radius: 8px;
  background: rgba(255,255,255,.045);
  padding: 16px;
}
.proof-svg {
  width: 100%;
  height: auto;
  overflow: visible;
}
.proof-svg-node rect,
.proof-svg-node circle {
  fill: rgba(255,255,255,.065);
  stroke: rgba(125,211,252,.58);
  stroke-width: 2;
  transition: fill .2s ease, stroke .2s ease, transform .2s ease;
}
.proof-svg-node text {
  fill: rgba(246,248,255,.9);
  font: 800 15px Inter, Arial, sans-serif;
  text-anchor: middle;
}
.proof-svg-path {
  fill: none;
  stroke: #18d3b5;
  stroke-width: 4;
  stroke-linecap: round;
  stroke-dasharray: 420;
  stroke-dashoffset: 420;
}
.proof-svg-path.warning {
  stroke: var(--gold);
}
.case-executive-proof.is-visible .proof-svg-path {
  animation: casePathDraw 1.2s ease forwards;
}
.proof-svg-node:hover rect,
.proof-svg-node:hover circle,
.proof-svg-node:focus rect,
.proof-svg-node:focus circle {
  fill: rgba(24,211,181,.18);
  stroke: #18d3b5;
}
.dashboard-evolution {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}
.mock-dashboard {
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 8px;
  padding: 12px;
}
.mock-dashboard span {
  color: #fff;
  font-weight: 900;
  text-transform: uppercase;
  font-size: .76rem;
}
.mock-dashboard p {
  color: rgba(246,248,255,.78);
  margin: 10px 0 0;
  font-size: .9rem;
}
.mock-grid {
  margin-top: 10px;
  height: 145px;
  display: grid;
  gap: 8px;
}
.mock-grid i,
.mock-grid b,
.mock-grid strong {
  display: block;
  border-radius: 6px;
  min-width: 0;
}
.mock-grid.messy {
  grid-template-columns: 1fr .7fr 1.2fr;
  grid-auto-rows: 42px;
}
.mock-grid.messy i {
  background: rgba(248,113,113,.23);
}
.mock-grid.clean {
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 38px 72px 20px;
}
.mock-grid.clean b {
  background: rgba(24,211,181,.28);
}
.mock-grid.clean i {
  background: rgba(125,211,252,.2);
}
.mock-grid.clean strong {
  grid-column: 1 / -1;
  background: rgba(247,185,53,.28);
}
.kpi-governance {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}
.kpi-governance span {
  padding: 14px;
  border: 1px solid rgba(24,211,181,.25);
  border-radius: 8px;
  background: rgba(24,211,181,.08);
}
.kpi-governance strong,
.kpi-governance em {
  display: block;
}
.kpi-governance strong {
  color: #fff;
}
.kpi-governance em {
  color: rgba(246,248,255,.76);
  font-style: normal;
  margin-top: 6px;
}
.outcome-proof > div {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}
.outcome-proof p {
  margin: 0;
  color: rgba(246,248,255,.84);
}
.case-quote-panel {
  margin: 0;
  padding: clamp(20px, 3vw, 30px);
  border-color: rgba(247,185,53,.36);
  background: linear-gradient(135deg, rgba(247,185,53,.14), rgba(24,211,181,.08));
}
.case-quote-panel blockquote {
  margin: 0;
  color: #fff;
  font-size: clamp(1.05rem, 2vw, 1.42rem);
  font-weight: 850;
}
.proof-library-section {
  margin-top: clamp(36px, 6vw, 72px);
}
.proof-library-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 14px;
}
.proof-library-grid a {
  color: #fff;
  text-decoration: none;
  border: 1px solid rgba(125,211,252,.22);
  border-radius: 8px;
  background: rgba(7,19,58,.7);
  padding: 12px;
}
.proof-library-grid img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: 6px;
  display: block;
}
.proof-library-grid span {
  display: block;
  margin-top: 10px;
  font-weight: 900;
}
@keyframes casePathDraw {
  to { stroke-dashoffset: 0; }
}
@media (min-width: 1080px) {
  .case-executive-proof {
    grid-template-columns: minmax(0, 1fr) minmax(250px, 320px);
  }
  .case-summary-sidebar {
    grid-column: 2;
    grid-row: 1 / span 5;
    position: sticky;
    top: 102px;
  }
  .case-executive-proof > :not(.case-summary-sidebar) {
    grid-column: 1;
  }
}
@media (max-width: 900px) {
  .visual-proof-grid,
  .before-after-comparison > div,
  .dashboard-evolution,
  .outcome-proof > div {
    grid-template-columns: 1fr;
  }
}
@media (max-width: 640px) {
  .case-summary-sidebar dl div,
  .kpi-governance {
    grid-template-columns: 1fr;
  }
  .proof-svg-node text {
    font-size: 13px;
  }
}
@media (prefers-reduced-motion: reduce) {
  .case-executive-proof.is-visible .proof-svg-path {
    animation: none;
    stroke-dashoffset: 0;
  }
}
`;

const js = `
${jsMarker}
function setupCaseStudyProof() {
  const proofBlocks = Array.from(document.querySelectorAll("[data-case-proof]"));
  if (!proofBlocks.length) return;
  const observer = "IntersectionObserver" in window ? new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-visible");
      entry.target.querySelectorAll("[data-countup]").forEach((item) => {
        const value = item.dataset.countup || "";
        const number = Number(value);
        if (!Number.isFinite(number) || item.dataset.counted === "true") return;
        item.dataset.counted = "true";
        const duration = 760;
        const start = performance.now();
        function tick(now) {
          const progress = Math.min(1, (now - start) / duration);
          item.textContent = String(Math.round(number * progress));
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    });
  }, { threshold: 0.18 }) : null;
  proofBlocks.forEach((block) => {
    if (observer) observer.observe(block);
    else block.classList.add("is-visible");
  });
}
setupCaseStudyProof();
`;

function appendOnce(file, marker, content) {
  const path = join(root, file);
  const current = readFileSync(path, "utf8");
  if (current.includes(marker)) return;
  writeFileSync(path, `${current.trimEnd()}\n\n${content.trim()}\n`);
}

writeAssets();
revampHtml("case-studies.html", "");
revampHtml(join("case-studies", "index.html"), "../");
appendOnce("home.css", cssMarker, css);
appendOnce("home.js", jsMarker, js);
appendOnce("home.min.js", jsMarker, js.replace(/\n\s+/g, "\n"));

console.log("Case study proof artifacts generated for 12 stories and 15 SVG assets.");

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Missing expected block: {label}")
    return text.replace(old, new, 1)


def prefix_nested_paths(html: str) -> str:
    html = re.sub(r'(href|src)="(assets/[^"]*)"', r'\1="../\2"', html)
    html = re.sub(r'(href|src)="(home\.(?:css|js)\?v=\d+)"', r'\1="../\2"', html)
    html = re.sub(r'(href)="((?:favicon|apple-touch-icon|social-preview)[^"]*)"', r'\1="../\2"', html)
    html = re.sub(r"url\('assets/", "url('../assets/", html)

    def local_href(match: re.Match) -> str:
        target = match.group(1)
        if target.startswith(("#", "/", "../", "assets/", "http://", "https://", "mailto:", "tel:")):
            return f'href="{target}"'
        if ".html" in target or target.startswith("insights/"):
            return f'href="../{target}"'
        return f'href="{target}"'

    return re.sub(r'href="([^"]+)"', local_href, html)


def update_home() -> None:
    html = read("index.html")
    if "Analytics Foundations for AI" in html:
        return
    insert_after = """<section class="enterprise-credibility-panel reveal-card" aria-labelledby="enterprise-credibility-title">
<div>
<p class="page-kicker">Founder-led, enterprise-tested</p>
<h2 id="enterprise-credibility-title">Enterprise Analytics Experience, Delivered Through a Boutique Partnership</h2>
</div>
<div class="enterprise-credibility-grid">
<article><strong>7+ years</strong><span>delivering enterprise analytics solutions across manufacturing, healthcare, safety, operations, and SaaS</span></article>
<article><strong>100+ dashboards</strong><span>designed across executive, operational, and customer-facing use cases</span></article>
<article><strong>2 billion records +</strong><span>supported across modern cloud analytics environments</span></article>
<article><strong>Enterprise context</strong><span>supporting analytics initiatives for Fortune 500 organizations and global enterprises</span></article>
<article><strong>Hands-on depth</strong><span>Power BI, SQL, Python, cloud data warehouses, analytics governance, and AI readiness</span></article>
</div>
</section>"""
    ai_section = insert_after + """
<section class="ai-foundation-section reveal-card" aria-labelledby="ai-foundation-title">
<div class="ai-foundation-copy">
<p class="page-kicker">AI readiness starts before AI</p>
<h2 id="ai-foundation-title">Analytics Foundations for AI</h2>
<p>Most AI initiatives struggle because reporting foundations are not ready. Disconnected data sources, conflicting KPI definitions, unclear ownership, and weak governance create unreliable inputs for AI systems.</p>
<p>Parallax helps organizations establish the reporting, governance, semantic modeling, and data architecture required to support AI, automation, predictive analytics, and operational intelligence.</p>
<p>The goal is not to deploy AI faster. The goal is to deploy AI on a foundation leaders can trust.</p>
<a class="primary-action" href="data-integration-analytics-architecture.html">Explore Data Integration &amp; Analytics Architecture</a>
</div>
<div class="enterprise-architecture-flow" aria-label="Enterprise analytics architecture flow">
<span>Source Systems</span>
<span>Data Integration</span>
<span>Semantic Layer</span>
<span>Governed KPIs</span>
<span>Executive Reporting</span>
<span>Operational Intelligence</span>
<strong>AI &amp; Decision Systems</strong>
</div>
</section>"""
    html = replace_once(html, insert_after, ai_section, "home AI foundation insertion")
    write("index.html", html)


def update_reporting_automation() -> None:
    for path in ["reporting-automation-consulting.html"]:
        html = read(path)
        if "Operational improvements reporting automation can create" in html:
            continue
        target = """<p>Solutions may include automated data pipelines, cloud data platforms, Power BI refresh architecture, and streamlined report distribution processes.</p>
</section>"""
        new = target + """
<section class="expertise-use-case-section reveal-card" aria-labelledby="automation-outcomes-title">
<p class="page-kicker">Common outcomes</p>
<h2 id="automation-outcomes-title">Operational improvements reporting automation can create</h2>
<p class="expertise-delivery-intro">The specific result depends on the reporting environment, but the work is usually measured in reduced friction, clearer ownership, and more reliable recurring delivery.</p>
<div class="expertise-use-case-grid outcome-grid">
<article><h3>Less spreadsheet assembly</h3><p>Eliminate manual spreadsheet consolidation, recurring exports, copy-paste steps, and duplicate reporting processes.</p></article>
<article><h3>More reliable refresh</h3><p>Improve refresh reliability with monitored schedules, exception alerts, recovery paths, and visible data freshness checks.</p></article>
<article><h3>Lower recurring workload</h3><p>Reduce reporting preparation time, recurring analyst workload, and the review effort required to reconcile repeated reports.</p></article>
<article><h3>Standard distribution</h3><p>Standardize report distribution so the right audiences receive the right view on the right cadence.</p></article>
<article><h3>Exception monitoring</h3><p>Create automated exception monitoring for late data, failed refreshes, missing records, and threshold movement.</p></article>
<article><h3>Cleaner operating cadence</h3><p>Give teams a repeatable reporting process that supports business review instead of consuming the review.</p></article>
</div>
</section>"""
        html = replace_once(html, target, new, "reporting automation outcomes")
        write(path, html)


def update_governance_page() -> None:
    html = read("dashboard-trust-governance.html")
    if "Trusted Analytics Governance Framework" in html:
        return
    target = """</section>


<section class="expertise-delivery-section reveal-card" aria-labelledby="expertise-delivery-title">"""
    new = """</section>
<section class="governance-framework-section reveal-card" aria-labelledby="governance-framework-title">
<div>
<p class="page-kicker">Governance maturity</p>
<h2 id="governance-framework-title">Trusted Analytics Governance Framework</h2>
<p>Dashboard trust improves in stages. The framework shows how raw data becomes governed intelligence that leaders can use for action, automation, and AI-assisted decisions.</p>
</div>
<figure class="governance-framework-asset">
<img src="assets/trusted-analytics-governance-framework.webp" alt="Trusted Analytics Governance Framework showing five levels from Data Exists to Intelligence Is Operationalized" loading="lazy" decoding="async">
</figure>
</section>


<section class="expertise-delivery-section reveal-card" aria-labelledby="expertise-delivery-title">"""
    html = replace_once(html, target, new, "governance framework section")
    write("dashboard-trust-governance.html", html)


def update_architecture_page() -> None:
    html = read("data-integration-analytics-architecture.html")
    if "Modern analytics architecture should support reporting today and AI readiness tomorrow." not in html:
        target = """<article><h3>Predictive and AI readiness</h3><p>Advanced use cases need governed training data, reusable features, traceable definitions, security boundaries, monitoring, and trusted delivery into business workflows.</p></article></div>
</section>"""
        new = target + """
<section class="ai-readiness-detail-section reveal-card" aria-labelledby="ai-readiness-detail-title">
<p class="page-kicker">AI-ready architecture</p>
<h2 id="ai-readiness-detail-title">Modern analytics architecture should support reporting today and AI readiness tomorrow.</h2>
<p>AI systems require consistent business definitions, trusted retrieval paths, and enough operating context to reason across the business without amplifying noise.</p>
<div class="expertise-use-case-grid">
<article><h3>Semantic Layer</h3><p>AI systems need consistent definitions for revenue, margin, backlog, utilization, churn, and other business concepts. A governed semantic layer keeps those meanings from changing by report, user, or tool.</p></article>
<article><h3>Knowledge Architecture</h3><p>Information must be organized before AI can reason across it. Source context, metric definitions, ownership, lineage, and decision rules all need a findable structure.</p></article>
<article><h3>Retrieval-Augmented Generation</h3><p>RAG works only when retrieval paths point to trusted, governed context. Parallax helps define which sources, documents, metrics, and definitions should be available for AI-assisted answers.</p></article>
<article><h3>AI Agents</h3><p>Agents can automate actions only when systems, ownership, permissions, exception rules, and decision logic are clearly defined.</p></article>
<article><h3>Operational Intelligence</h3><p>The same architecture that improves reporting can support automated monitoring, proactive signals, and intelligence products that leaders can inspect.</p></article>
<article><h3>Future Machine Learning</h3><p>Reusable entities, quality controls, governed features, and monitored pipelines make later predictive work more credible and maintainable.</p></article>
</div>
</section>"""
        html = replace_once(html, target, new, "architecture AI readiness detail")
    modern_old = """<h2>Architecture should make trusted data products easier to build and govern.</h2>
<p>A modern platform is valuable when it reduces duplicate logic, makes lineage and quality visible, gives teams reusable governed data products, and supports Power BI, automation, predictive models, and AI agents through the same controlled foundation.</p>"""
    modern_new = """<h2>Architecture should make trusted data products easier to build and govern.</h2>
<p>Modern analytics architecture should support reporting today while creating the foundation for AI agents, operational intelligence, automation, and future machine learning initiatives. The value is not the platform alone; it is the governed path from source systems to trusted business context.</p>"""
    if modern_old in html:
        html = replace_once(html, modern_old, modern_new, "architecture modern callout")
    write("data-integration-analytics-architecture.html", html)


def update_expertise() -> None:
    html = read("expertise.html")
    if "Analytics maturity framework" in html:
        return
    after = """<section class="expertise-content-block reveal-card">
<h2>What Connects The Work</h2>
<p>The common thread is trust in the operating number. Reports earn that trust when the data path is understandable, metric definitions are owned, the reporting layer answers a real business question, and the review cadence turns the number into action. The platform still matters, but the business layer above it matters more: source logic, ownership, governance, automation readiness, and the decision rhythm leaders actually use.</p>
</section>"""
    insert = after + """
<section class="analytics-maturity-section reveal-card" aria-labelledby="analytics-maturity-title">
<p class="page-kicker">Analytics maturity framework</p>
<h2 id="analytics-maturity-title">The path from reporting visibility to AI enablement</h2>
<div class="maturity-stage-grid">
<article><span>Stage 1</span><h3>Reporting Visibility</h3><p>Power BI &amp; Microsoft Fabric make critical business activity easier to see.</p></article>
<article><span>Stage 2</span><h3>Reporting Reliability</h3><p>Data Quality &amp; Analytics Reliability make the numbers dependable enough to use.</p></article>
<article><span>Stage 3</span><h3>Governed Metrics</h3><p>KPI Strategy, Executive Reporting, and BI Governance create shared definitions and owners.</p></article>
<article><span>Stage 4</span><h3>Decision Systems</h3><p>Executive reporting connects metric movement to operating review, action paths, and accountability.</p></article>
<article><span>Stage 5</span><h3>Operational Intelligence</h3><p>Reporting Automation and Intelligence Lab turn trusted signals into repeatable monitoring and decision support.</p></article>
<article><span>Stage 6</span><h3>AI Enablement</h3><p>Data Integration &amp; Analytics Architecture prepares semantic layers, knowledge architecture, and governed context for AI.</p></article>
</div>
</section>
<section class="expertise-content-block analytics-operating-model reveal-card">
<p class="page-kicker">Analytics operating model</p>
<h2>Why These Capabilities Work Together</h2>
<p>Organizations rarely have a dashboard problem. They usually have a connected set of issues involving data quality, reporting reliability, KPI ownership, governance, automation, and decision-making. The expertise areas represent different components of the same operating system: the data path, the reporting layer, the governance model, the decision cadence, and the future intelligence layer.</p>
</section>"""
    html = replace_once(html, after, insert, "expertise maturity framework")
    write("expertise.html", html)


def update_lab() -> None:
    html = read("intelligence-lab.html")
    if "What Intelligence Lab becomes" in html:
        return
    hero_old = """<h1>Practical Analytics and Business Intelligence Insights</h1>
<p>The Intelligence Lab collects practical analytics resources, reporting ideas, dashboard guidance, and business intelligence insights for growing teams.</p>"""
    hero_new = """<h1>Where trusted reporting evolves into operational intelligence.</h1>
<p>Intelligence Lab is the advanced layer built after reporting reliability, governance, and decision context are strong enough to support predictive intelligence, monitoring, machine learning, and AI-assisted decisions.</p>"""
    html = replace_once(html, hero_old, hero_new, "lab hero")
    after_share = """</section>
<section aria-labelledby="lab-promise-title" class="lab-section lab-promise-section reveal-card">"""
    insert = """</section>
<section aria-labelledby="lab-becomes-title" class="lab-section lab-becomes-section reveal-card">
<p class="page-kicker">What Intelligence Lab becomes</p>
<h2 id="lab-becomes-title">The layer after reporting and governance foundations exist.</h2>
<p>Intelligence Lab is where trusted reporting evolves into predictive intelligence, machine learning applications, AI-assisted decision systems, operational monitoring, executive intelligence products, proactive risk detection, and workflow-triggered insights.</p>
<div class="future-state-flow" aria-label="Analytics future state progression">
<span>Reporting</span>
<span>Governance</span>
<span>Intelligence</span>
<span>Machine Learning</span>
<strong>AI-Assisted Decisions</strong>
</div>
</section>
<section aria-labelledby="lab-promise-title" class="lab-section lab-promise-section reveal-card">"""
    html = replace_once(html, after_share, insert, "lab becomes section")
    write("intelligence-lab.html", html)


CASE_VISUALS = {
    "manufacturing-throughput": ("6 source systems", "Manual extracts", "Copied transformations", "6 source systems", "Governed data path", "Reusable semantic model"),
    "utilities-reliability": ("Reliability signals", "Unclear exception age", "Informal escalation", "Reliability signals", "Owner response paths", "Refresh confidence"),
    "energy-operations": ("Field updates", "Production context", "Separate reviews", "Field and production data", "Risk-focused review", "Executive action path"),
    "logistics-service-level": ("Activity volume", "Weekly bottleneck review", "Unclear priority", "Service thresholds", "Exception owners", "Earlier bottleneck visibility"),
    "field-services-kpis": ("Regional definitions", "KPI debates", "Delayed staffing calls", "5 priority KPIs", "5 named owners", "Weekly decision cadence"),
    "construction-project-controls": ("Manual status updates", "Overlapping risk logs", "Duplicated summaries", "Standardized workflow", "Single status structure", "Cleaner executive summary"),
    "healthcare-utilization": ("Utilization reports", "Timing questions", "Definition drift", "Governed definitions", "Refresh checks", "Clearer utilization signal"),
    "industrial-software-revenue": ("14 reports", "Conflicting revenue logic", "Dashboard overlap", "4 executive views", "1 governed revenue definition", "Mapped dashboard owners"),
    "b2b-services-scorecard": ("CRM and finance exports", "Manual scorecard assembly", "Duplicate report work", "Automated refresh", "Documented definitions", "Trusted scorecard workflow"),
    "retail-multi-location": ("Store metrics", "Regional interpretation gaps", "Scattered exceptions", "Aligned location metrics", "Owner follow-up", "Leadership exception review"),
    "distribution-supply-chain": ("Inventory and order signals", "Ungoverned source path", "Slow operating review", "Governed source path", "Inventory exception signal", "Decision-ready review"),
    "facilities-maintenance": ("Work-order backlog", "Risk lists", "Manual intervention tracking", "Prioritized backlog view", "Recurring risk review", "Owner response path"),
}


def case_visual_html(values: tuple[str, ...]) -> str:
    b1, b2, b3, a1, a2, a3 = values
    return f"""<div class="case-transformation-visual" aria-label="Before and after analytics architecture">
<div><strong>Before</strong><span>{b1}</span><span>{b2}</span><span>{b3}</span></div>
<div><strong>After</strong><span>{a1}</span><span>{a2}</span><span>{a3}</span></div>
</div>"""


def update_case_studies() -> None:
    html = read("case-studies.html")
    html = html.replace(
        "Metrics are included only where they already existed in the site content. Otherwise outcomes are stated qualitatively.",
        "Metrics are included only where they already existed in the site content. Otherwise outcomes are stated through concrete operating changes such as dashboards consolidated, sources integrated, ownership mapped, workflows standardized, and refresh processes stabilized.",
    )
    outcome_updates = {
        "No verified quantitative client metrics available; outcomes are qualitative. Reliability review became easier because current exceptions, stale data, and owner follow-up were separated in the reporting view.": "No verified quantitative client metrics available; outcomes are qualitative. Reliability review became easier because current exceptions, stale data, refresh ownership, and owner follow-up were separated in the reporting view.",
        "No verified quantitative client metrics available; outcomes are qualitative. Leadership gained a tighter view of operational risk and the response owners connected to each signal.": "No verified quantitative client metrics available; outcomes are qualitative. Leadership gained a tighter view of operational risk, standardized field updates, and the response owners connected to each signal.",
        "No verified quantitative client metrics available; outcomes are qualitative. Managers gained a clearer weekly path from exception to owner to action.": "No verified quantitative client metrics available; outcomes are qualitative. Managers gained a clearer weekly path from exception to owner to action, with service-level thresholds and review workflow standardized.",
        "No verified quantitative client metrics available; outcomes are qualitative. Status review became easier because risk, schedule, and cost movement were presented in one operating structure.": "No verified quantitative client metrics available; outcomes are qualitative. Status review became easier because duplicated summaries were reduced and risk, schedule, and cost movement were presented in one operating structure.",
        "No verified quantitative client metrics available; outcomes are qualitative. Leaders could separate utilization movement from reporting timing and definition questions.": "No verified quantitative client metrics available; outcomes are qualitative. Leaders could separate utilization movement from reporting timing, refresh reliability, and definition questions.",
        "No verified quantitative client metrics available; outcomes are qualitative. Regional and store leaders gained a clearer way to compare performance movement and follow-up needs.": "No verified quantitative client metrics available; outcomes are qualitative. Regional and store leaders gained a clearer way to compare performance movement, exception ownership, and follow-up needs.",
        "No verified quantitative client metrics available; outcomes are qualitative. Leaders gained a cleaner review path for inventory exceptions, fulfillment risk, and supplier timing.": "No verified quantitative client metrics available; outcomes are qualitative. Leaders gained a cleaner governed review path for inventory exceptions, fulfillment risk, source reliability, and supplier timing.",
        "No verified quantitative client metrics available; outcomes are qualitative. The maintenance review became easier to prioritize because backlog, risk, and owner response were separated.": "No verified quantitative client metrics available; outcomes are qualitative. The maintenance review became easier to prioritize because backlog, recurring risk, refresh timing, and owner response were separated.",
    }
    for old, new in outcome_updates.items():
        html = html.replace(old, new)

    def inject(match: re.Match) -> str:
        article = match.group(0)
        case_id = match.group(1)
        if "case-transformation-visual" in article:
            return article
        visual = case_visual_html(CASE_VISUALS[case_id])
        return article.replace("</dl>", f"</dl>\n{visual}", 1)

    ids = "|".join(re.escape(key) for key in CASE_VISUALS)
    html = re.sub(rf'<article class="case-study-expanded industry-case-story reveal-card" id="({ids})">.*?</article>', inject, html, flags=re.S)
    write("case-studies.html", html)


def update_about() -> None:
    html = read("about.html")
    old_why = """<p class="page-kicker">Why Parallax exists</p>
<h2>A shift in viewpoint often reveals the real problem underneath analytics friction.</h2>
<p>Parallax Data Lab exists because analytics often grows faster than the structure supporting it. The result is familiar: more dashboards, more debates, and less confidence in what should happen next.</p>"""
    new_why = """<p class="page-kicker">The Parallax lens</p>
<h2>A shift in viewpoint often reveals the real problem underneath analytics friction.</h2>
<p>Analytics friction often grows faster than the structure supporting it. The result is familiar: more dashboards, more debates, and less confidence in what should happen next.</p>"""
    if old_why in html:
        html = replace_once(html, old_why, new_why, "about existing why retitle")
    founder_section = """</section>
<section class="about-founder-proof reveal-card" aria-labelledby="about-founder-proof-title">"""
    insert = """</section>
<section class="about-founder-story reveal-card" aria-labelledby="why-parallax-exists-title">
<p class="page-kicker">Founder story</p>
<h2 id="why-parallax-exists-title">Why Parallax Exists</h2>
<p>Throughout enterprise analytics work, a consistent pattern emerged. Organizations were not struggling because they lacked dashboards. They were struggling because reporting, governance, ownership, and decision systems had become disconnected.</p>
<p>Parallax was created to help organizations rebuild those foundations and create analytics systems leaders can trust.</p>
</section>
<section class="about-philosophy reveal-card" aria-labelledby="analytics-belief-title">
<p class="page-kicker">Personal philosophy</p>
<h2 id="analytics-belief-title">What I Believe About Analytics</h2>
<div class="about-belief-grid">
<article><strong>Trust matters more than volume</strong><span>More reports do not help when leaders cannot rely on the number.</span></article>
<article><strong>Clarity matters more than complexity</strong><span>The best analytics systems make the next decision easier to see.</span></article>
<article><strong>Ownership matters more than technology</strong><span>Tools cannot compensate for unclear definitions, decisions, and accountability.</span></article>
<article><strong>Better decisions matter more than dashboards</strong><span>The work only matters if it changes how leaders act.</span></article>
</div>
</section>
<section class="about-founder-proof reveal-card" aria-labelledby="about-founder-proof-title">"""
    if "What I Believe About Analytics" not in html:
        html = replace_once(html, founder_section, insert, "about founder story/philosophy")
    partnership_old = """<section class="about-founder-partnership reveal-card" aria-labelledby="founder-partnership-title">
<p class="page-kicker">Direct founder partnership</p>
<h2 id="founder-partnership-title">Your Analytics Partner From Strategy Through Execution</h2>
<p>Many organizations face a gap between high-level analytics strategy and the technical work required to make it successful.</p>
<p>With Parallax Data Lab, organizations work directly with founder Jonah Robinson, an analytics professional who combines strategic business understanding with hands-on expertise in data modeling, business intelligence, automation, governance, and modern cloud analytics.</p>
<p>Whether establishing executive KPI frameworks, improving trust in existing dashboards, automating reporting workflows, or preparing a foundation for AI, clients receive direct partnership from a senior analytics leader from discovery through implementation.</p>
</section>"""
    partnership_new = """<section class="about-founder-partnership reveal-card" aria-labelledby="founder-partnership-title">
<p class="page-kicker">Direct founder partnership</p>
<h2 id="founder-partnership-title">Why Clients Work Directly With Me</h2>
<p>Clients work directly with the person performing the work. No handoffs. No junior analyst layers. No sales-to-delivery transition.</p>
<p>Strategy and execution stay connected throughout the engagement, whether the work involves executive KPI frameworks, dashboard trust, reporting automation, governance, architecture, or AI readiness.</p>
</section>"""
    if partnership_old in html:
        html = replace_once(html, partnership_old, partnership_new, "about direct founder partnership")
    write("about.html", html)


def update_insights() -> None:
    html = read("insights.html")
    if "Research &amp; Perspectives" in html and "research-perspectives-section" in html:
        return
    target = """</section>
<section class="insights-filter-band" aria-label="Article categories">"""
    research = """</section>
<section class="research-perspectives-section reveal-card" aria-labelledby="research-perspectives-title">
<div class="research-perspectives-heading">
<p class="page-kicker">Research &amp; Perspectives</p>
<h2 id="research-perspectives-title">Long-form authority content for analytics, governance, and AI readiness.</h2>
<p>Research &amp; Perspectives is reserved for deeper frameworks, benchmark-style thinking, and executive-level analysis. Insights remains the home for tactical articles.</p>
</div>
<a class="research-feature-card" href="insights/ai-enablement-starts-with-trusted-business-data.html">
<img src="assets/insights/ai-enablement-trusted-business-data.webp" alt="AI enablement framework built on trusted business data" loading="lazy" decoding="async">
<div>
<span>Flagship perspective</span>
<h3>AI Enablement Starts With Trusted Business Data</h3>
<p>A deeper framework for why AI readiness depends on reporting reliability, governed definitions, ownership, semantic context, and decision paths before model selection.</p>
<em>Read the perspective</em>
</div>
</a>
</section>
<section class="insights-filter-band" aria-label="Article categories">"""
    html = replace_once(html, target, research, "insights research perspectives")
    filter_old = """<button class="is-active" type="button" data-insight-filter="all">All</button>
<button type="button" data-insight-filter="Analytics Trust">Analytics Trust</button>"""
    filter_new = """<button class="is-active" type="button" data-insight-filter="all">All</button>
<button type="button" data-insight-filter="Research &amp; Perspectives">Research &amp; Perspectives</button>
<button type="button" data-insight-filter="Analytics Trust">Analytics Trust</button>"""
    html = replace_once(html, filter_old, filter_new, "insights filter")
    card_old = """<article class="insight-card" data-category="AI Enablement">
<img src="assets/insights/ai-enablement-trusted-business-data.webp" alt="Executive team planning AI enablement around governed business data and trusted metrics" loading="lazy" decoding="async">
<div class="insight-card-body">
<span>AI Enablement</span>"""
    card_new = """<article class="insight-card" data-category="Research & Perspectives">
<img src="assets/insights/ai-enablement-trusted-business-data.webp" alt="Executive team planning AI enablement around governed business data and trusted metrics" loading="lazy" decoding="async">
<div class="insight-card-body">
<span>Research &amp; Perspectives</span>"""
    html = replace_once(html, card_old, card_new, "insights flagship category")
    write("insights.html", html)


def update_fit_check() -> None:
    html = read("free-fit-check.html")
    process = """<section aria-labelledby="fit-check-process-title" class="assessment-path-section reveal-card" id="what-you-get">
<p class="page-kicker">What happens in 15 minutes</p>
<h2 id="fit-check-process-title">The meeting is intentionally short, practical, and directional.</h2>
<div class="assessment-path-grid">
<article><span>Step 1</span><h3>You describe the friction</h3><p>Bring the messy version: dashboard distrust, reporting overload, metric disputes, slow decisions, or scattered operating signals.</p><strong>No prep deck required.</strong></article>
<article><span>Step 2</span><h3>We identify the likely path</h3><p>We separate dashboard symptoms from deeper issues in definitions, ownership, decision cadence, signal design, or analytics leadership.</p><strong>The goal is routing, not a full diagnostic.</strong></article>
<article><span>Step 3</span><h3>You get a recommended path</h3><p>The answer may be a scorecard, Analytics Health Check, Decision System Reset, Fractional Analytics, Intelligence Lab initiative, or no engagement.</p><strong>Paid work only follows if there is a clear fit.</strong></article>
</div>
</section>

"""
    process_index = html.find(process)
    form_index = html.find('<section aria-labelledby="fit-check-form-title"')
    if process_index != -1 and form_index != -1 and process_index < form_index:
        return
    html = replace_once(html, process, "", "remove process section for reorder")
    form_marker = """<section aria-labelledby="fit-check-form-title" class="assessment-form-section assessment-form-refined reveal-card">"""
    html = replace_once(html, form_marker, process + form_marker, "insert process before form")
    write("free-fit-check.html", html)


def update_css() -> None:
    css = read("home.css")
    addition = """

/* AI readiness, governance, and conversion framework additions */
.home-page .case-study-grid + .case-study-heading {
  margin-top: clamp(30px, 5vw, 56px);
}

.ai-foundation-section,
.governance-framework-section,
.ai-readiness-detail-section,
.analytics-maturity-section,
.lab-becomes-section,
.research-perspectives-section,
.about-founder-story,
.about-philosophy {
  width: min(1120px, calc(100% - 32px));
  margin: clamp(34px, 6vw, 72px) auto;
  padding: clamp(22px, 4vw, 38px);
  border: 1px solid rgba(125, 211, 252, 0.24);
  border-radius: 8px;
  background: linear-gradient(135deg, rgba(9, 26, 70, 0.9), rgba(8, 18, 50, 0.78));
  box-shadow: 0 26px 80px rgba(0, 0, 0, 0.24);
}

.ai-foundation-section,
.governance-framework-section {
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(320px, 1.05fr);
  gap: clamp(24px, 4vw, 46px);
  align-items: center;
}

.ai-foundation-copy h2,
.governance-framework-section h2,
.ai-readiness-detail-section h2,
.analytics-maturity-section h2,
.lab-becomes-section h2,
.research-perspectives-heading h2,
.about-founder-story h2,
.about-philosophy h2 {
  margin: 0 0 16px;
  color: #ffffff;
  font-size: clamp(2rem, 3.4vw, 3.35rem);
  line-height: 1.05;
}

.ai-foundation-copy p,
.governance-framework-section p,
.ai-readiness-detail-section > p:not(.page-kicker),
.analytics-maturity-section > p,
.lab-becomes-section > p,
.research-perspectives-heading p,
.about-founder-story p {
  color: rgba(246, 248, 255, 0.82);
  line-height: 1.68;
}

.enterprise-architecture-flow,
.future-state-flow {
  display: grid;
  gap: 10px;
}

.enterprise-architecture-flow span,
.enterprise-architecture-flow strong {
  position: relative;
  display: block;
  padding: 13px 16px;
  border: 1px solid rgba(125, 211, 252, 0.32);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.07);
  color: #ffffff;
  font-weight: 900;
  text-align: center;
}

.enterprise-architecture-flow span:not(:last-child)::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -10px;
  width: 1px;
  height: 10px;
  background: rgba(247, 201, 75, 0.78);
}

.enterprise-architecture-flow strong {
  background: linear-gradient(135deg, rgba(247, 201, 75, 0.24), rgba(69, 190, 255, 0.16));
  border-color: rgba(247, 201, 75, 0.55);
  color: #fff8d9;
}

.governance-framework-asset img {
  display: block;
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 22px 60px rgba(0, 0, 0, 0.28);
}

.maturity-stage-grid,
.about-belief-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  margin-top: 24px;
}

.maturity-stage-grid article,
.about-belief-grid article {
  padding: 18px;
  border: 1px solid rgba(125, 211, 252, 0.22);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.06);
}

.maturity-stage-grid span,
.research-feature-card span {
  color: #f7c94b;
  font-size: 0.76rem;
  font-weight: 900;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.maturity-stage-grid h3,
.about-belief-grid strong {
  display: block;
  margin: 8px 0;
  color: #ffffff;
  font-size: 1.05rem;
}

.maturity-stage-grid p,
.about-belief-grid span {
  color: rgba(246, 248, 255, 0.78);
  line-height: 1.55;
}

.future-state-flow {
  grid-template-columns: repeat(5, minmax(0, 1fr));
  margin-top: 24px;
}

.future-state-flow span,
.future-state-flow strong {
  position: relative;
  min-height: 74px;
  display: grid;
  place-items: center;
  padding: 12px;
  border: 1px solid rgba(125, 211, 252, 0.28);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.06);
  color: #ffffff;
  font-weight: 900;
  text-align: center;
}

.future-state-flow span:not(:last-child)::after {
  content: "->";
  position: absolute;
  right: -19px;
  color: #f7c94b;
  z-index: 1;
}

.future-state-flow strong {
  border-color: rgba(247, 201, 75, 0.52);
  color: #fff8d9;
}

.case-transformation-visual {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin: 18px 0 8px;
}

.case-transformation-visual div {
  display: grid;
  gap: 8px;
  padding: 14px;
  border: 1px solid rgba(125, 211, 252, 0.22);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.06);
}

.case-transformation-visual strong {
  color: #f7c94b;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.76rem;
}

.case-transformation-visual span {
  color: rgba(246, 248, 255, 0.9);
  font-weight: 800;
}

.research-perspectives-section {
  display: grid;
  grid-template-columns: minmax(0, 0.85fr) minmax(320px, 1.15fr);
  gap: clamp(22px, 4vw, 42px);
  align-items: center;
}

.research-feature-card {
  display: grid;
  grid-template-columns: minmax(180px, 0.72fr) minmax(0, 1fr);
  gap: 18px;
  min-height: 260px;
  padding: 16px;
  border: 1px solid rgba(247, 201, 75, 0.32);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.07);
  color: inherit;
  text-decoration: none;
}

.research-feature-card img {
  width: 100%;
  height: 100%;
  min-height: 220px;
  object-fit: cover;
  border-radius: 6px;
}

.research-feature-card h3 {
  margin: 8px 0 10px;
  color: #ffffff;
  font-size: clamp(1.35rem, 2.4vw, 2.1rem);
  line-height: 1.08;
}

.research-feature-card p {
  color: rgba(246, 248, 255, 0.8);
  line-height: 1.62;
}

.research-feature-card em {
  color: #f7c94b;
  font-style: normal;
  font-weight: 900;
}

@media (max-width: 900px) {
  .ai-foundation-section,
  .governance-framework-section,
  .research-perspectives-section,
  .research-feature-card {
    grid-template-columns: 1fr;
  }

  .maturity-stage-grid,
  .about-belief-grid,
  .future-state-flow {
    grid-template-columns: 1fr;
  }

  .future-state-flow span:not(:last-child)::after {
    content: "";
    right: auto;
    left: 50%;
    bottom: -10px;
    width: 1px;
    height: 10px;
    background: rgba(247, 201, 75, 0.78);
  }
}

@media (max-width: 640px) {
  .case-transformation-visual {
    grid-template-columns: 1fr;
  }
}
"""
    if "/* AI readiness, governance, and conversion framework additions */" not in css:
        css += addition
    write("home.css", css)


def generate_governance_webp() -> None:
    out = ROOT / "assets" / "trusted-analytics-governance-framework.webp"
    width, height = 2000, 1160
    img = Image.new("RGB", (width, height), "#081436")
    draw = ImageDraw.Draw(img)

    for y in range(height):
        r = int(8 + y / height * 6)
        g = int(20 + y / height * 14)
        b = int(54 + y / height * 28)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    font_dir = Path("C:/Windows/Fonts")
    title_font = ImageFont.truetype(str(font_dir / "arialbd.ttf"), 70)
    sub_font = ImageFont.truetype(str(font_dir / "arial.ttf"), 32)
    label_font = ImageFont.truetype(str(font_dir / "arialbd.ttf"), 30)
    stage_font = ImageFont.truetype(str(font_dir / "arialbd.ttf"), 34)
    body_font = ImageFont.truetype(str(font_dir / "arial.ttf"), 27)

    draw.text((90, 70), "Trusted Analytics Governance Framework", fill="#ffffff", font=title_font)
    draw.text((92, 154), "A practical maturity path from available data to operationalized intelligence.", fill="#cbd8f4", font=sub_font)

    stages = [
        ("Level 1", "Data Exists", "Sources are visible, but quality,\nownership, and usage are still unclear."),
        ("Level 2", "Data Is Trusted", "Refresh, lineage, quality checks,\nand source reliability are monitored."),
        ("Level 3", "KPIs Are Governed", "Definitions, owners, thresholds,\nand certified reporting paths are explicit."),
        ("Level 4", "Actions Are Connected", "Metric movement is tied to reviews,\ndecisions, owners, and follow-up."),
        ("Level 5", "Intelligence Is Operationalized", "Trusted signals support automation,\nmonitoring, AI, and decision systems."),
    ]

    def wrap_lines(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> str:
        lines = []
        for raw_line in text.split("\n"):
            words = raw_line.split()
            line = ""
            for word in words:
                candidate = f"{line} {word}".strip()
                if draw.textlength(candidate, font=font) <= max_width:
                    line = candidate
                else:
                    if line:
                        lines.append(line)
                    line = word
            if line:
                lines.append(line)
        return "\n".join(lines)

    card_w, card_h = 344, 650
    gap = 26
    start_x = 80
    y = 330
    colors = ["#1a3e79", "#1f5b8c", "#26718e", "#52836b", "#9b7a2e"]
    for i, (level, title, body) in enumerate(stages):
        x = start_x + i * (card_w + gap)
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=24, fill="#0d2457", outline="#5db9ff", width=2)
        draw.rounded_rectangle((x, y, x + card_w, y + 84), radius=24, fill=colors[i])
        draw.text((x + 28, y + 26), level, fill="#fff2bd", font=label_font)
        draw.multiline_text((x + 28, y + 140), wrap_lines(title, stage_font, card_w - 56), fill="#ffffff", font=stage_font, spacing=7)
        draw.multiline_text((x + 28, y + 300), wrap_lines(body, body_font, card_w - 56), fill="#dfe9ff", font=body_font, spacing=9)
        draw.ellipse((x + 28, y + card_h - 92, x + 88, y + card_h - 32), fill="#f7c94b")
        draw.text((x + 48, y + card_h - 84), str(i + 1), fill="#081436", font=label_font)
        if i < len(stages) - 1:
            ax = x + card_w + 4
            ay = y + card_h // 2
            draw.line((ax, ay, ax + gap - 8, ay), fill="#f7c94b", width=4)
            draw.polygon([(ax + gap - 8, ay), (ax + gap - 20, ay - 8), (ax + gap - 20, ay + 8)], fill="#f7c94b")

    draw.text((92, 1034), "Reporting reliability -> governance -> connected actions -> operational intelligence -> AI enablement", fill="#fff2bd", font=sub_font)
    img.save(out, "WEBP", quality=92, method=6)


def sync_clean_routes() -> None:
    slugs = [
        "about",
        "case-studies",
        "dashboard-trust-governance",
        "data-integration-analytics-architecture",
        "expertise",
        "free-fit-check",
        "insights",
        "intelligence-lab",
        "reporting-automation-consulting",
    ]
    for slug in slugs:
        source = ROOT / f"{slug}.html"
        target = ROOT / slug / "index.html"
        if source.exists() and target.parent.exists():
            target.write_text(prefix_nested_paths(source.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")


def main() -> None:
    update_home()
    update_reporting_automation()
    update_governance_page()
    update_architecture_page()
    update_expertise()
    update_lab()
    update_case_studies()
    update_about()
    update_insights()
    update_fit_check()
    update_css()
    generate_governance_webp()
    sync_clean_routes()
    print("Applied AI readiness and conversion updates.")


if __name__ == "__main__":
    main()

from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]

PRIMARY_CTA = "Book a 15-Minute Fit Check"

EXPERTISE = [
    ("Power BI & Microsoft Fabric", "power-bi-consultant-cincinnati.html"),
    ("KPI Strategy & Executive Reporting", "kpi-reporting-consulting.html"),
    ("Reporting Automation", "reporting-automation-consulting.html"),
    ("Data Quality & Reporting Reliability", "data-quality-review.html"),
    ("BI Governance & Dashboard Trust", "dashboard-trust-governance.html"),
    ("Data Integration & Analytics Architecture", "data-integration-analytics-architecture.html"),
]

ROOT_PAGES = [
    "index.html",
    "about.html",
    "contact.html",
    "case-studies.html",
    "analytics-health-check.html",
    "business-intelligence-consultant-cincinnati.html",
    "dashboard-trust-scorecard.html",
    "dashboard-trust-scorecard-download.html",
    "data-quality-review.html",
    "data-integration-analytics-architecture.html",
    "decision-system-reset.html",
    "decision-workspace.html",
    "expertise.html",
    "fractional-analytics.html",
    "intelligence-lab.html",
    "kpi-reporting-consulting.html",
    "our-offerings.html",
    "power-bi-consultant-cincinnati.html",
    "privacy-policy.html",
    "reporting-automation-consulting.html",
    "scorecard-thank-you.html",
    "thank-you.html",
]

SYNC_PAGES = [
    "about",
    "analytics-health-check",
    "business-intelligence-consultant-cincinnati",
    "case-studies",
    "contact",
    "dashboard-trust-scorecard",
    "dashboard-trust-scorecard-download",
    "data-quality-review",
    "data-integration-analytics-architecture",
    "decision-system-reset",
    "decision-workspace",
    "expertise",
    "fractional-analytics",
    "free-fit-check",
    "intelligence-lab",
    "dashboard-trust-governance",
    "kpi-reporting-consulting",
    "our-offerings",
    "power-bi-consultant-cincinnati",
    "privacy-policy",
    "reporting-automation-consulting",
    "scorecard-thank-you",
    "thank-you",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def meta_block(title: str, desc: str, canonical: str, image: str = "https://parallaxdatalab.com/assets/social-preview.webp") -> str:
    return f"""<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}"/>
<link rel="canonical" href="{canonical}"/>
<link href="home.css?v=171" rel="stylesheet"/>
<meta name="theme-color" content="#0b1745"/>
<link rel="icon" href="favicon.ico" sizes="any"/>
<link rel="icon" type="image/png" href="favicon.png"/>
<link rel="apple-touch-icon" href="apple-touch-icon.png"/>
<meta content="website" property="og:type"/>
<meta content="Parallax Data Lab" property="og:site_name"/>
<meta property="og:title" content="{html.escape(title)}"/>
<meta property="og:description" content="{html.escape(desc)}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{image}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{html.escape(title)}"/>
<meta name="twitter:description" content="{html.escape(desc)}"/>
<meta name="twitter:image" content="{image}"/>"""


def schema_webpage(name: str, desc: str, url: str, crumb: str) -> str:
    return f"""<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "https://parallaxdatalab.com/#organization",
      "name": "Parallax Data Lab",
      "url": "https://parallaxdatalab.com/",
      "founder": {{ "@type": "Person", "name": "Jonah Robinson" }},
      "description": "Analytics consulting for teams with too much reporting and not enough trusted signal for decisions."
    }},
    {{
      "@type": "WebPage",
      "@id": "{url}#webpage",
      "url": "{url}",
      "name": "{name}",
      "description": "{desc}",
      "isPartOf": {{ "@id": "https://parallaxdatalab.com/#website" }},
      "about": {{ "@id": "https://parallaxdatalab.com/#organization" }},
      "breadcrumb": {{ "@id": "{url}#breadcrumb" }}
    }},
    {{
      "@type": "BreadcrumbList",
      "@id": "{url}#breadcrumb",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://parallaxdatalab.com/" }},
        {{ "@type": "ListItem", "position": 2, "name": "{crumb}", "item": "{url}" }}
      ]
    }}
  ]
}}</script>"""


def extract_header(source: str) -> str:
    return re.search(r"<header[\s\S]*?</header>", source).group(0)


def extract_footer(source: str) -> str:
    return re.search(r"<footer[\s\S]*?</footer>", source).group(0)


def update_header_footer(html_text: str) -> str:
    h = html_text
    h = h.replace('<a href="how-we-help.html">How We Help</a>\n', "")
    h = h.replace('<a href="../how-we-help.html">How We Help</a>\n', "")
    h = re.sub(r'\n?<div class="site-auth-actions">[\s\S]*?</div>\n(?=</header>)', "\n", h)
    h = h.replace('<span>Power BI Consulting</span>', '<span>Power BI &amp; Microsoft Fabric</span>')
    h = h.replace('<span>KPI Reporting</span>', '<span>KPI Strategy &amp; Executive Reporting</span>')
    h = h.replace('<span>Data Quality Review</span>', '<span>Data Quality &amp; Reporting Reliability</span>')
    h = h.replace('<span>Dashboard Trust &amp; Governance</span>', '<span>BI Governance &amp; Dashboard Trust</span>')
    h = h.replace('<span>Cincinnati Analytics Consulting</span>', '<span>Local Analytics Consulting</span>')
    h = h.replace('<span>Intelligence Lab Overview</span></a>\n</details>', '<span>Intelligence Lab Overview</span></a>\n<a class="nav-menu-child" href="decision-workspace.html"><span>Interactive Decision Workspace Demo</span></a>\n</details>')
    h = h.replace('<span>About Parallax</span></a>\n<a class="nav-menu-child" href="business-intelligence-consultant-cincinnati.html"><span>Local Analytics Consulting</span></a>', '<span>About Parallax</span></a>\n<a class="nav-menu-child" href="contact.html"><span>Contact</span></a>\n<a class="nav-menu-child" href="business-intelligence-consultant-cincinnati.html"><span>Local Analytics Consulting</span></a>')
    h = h.replace('href="about.html#contact-us"', 'href="contact.html"')
    h = h.replace('href="../about.html#contact-us"', 'href="../contact.html"')
    h = h.replace('Book a Fit Check', PRIMARY_CTA)
    h = h.replace('Request the Fit Check', PRIMARY_CTA)
    h = h.replace('Request a Free Fit Check', PRIMARY_CTA)
    h = h.replace('Start With a Free Fit Check', PRIMARY_CTA)
    h = h.replace('Start with a Free Fit Check', PRIMARY_CTA)
    h = h.replace('Discuss a Power BI Project', PRIMARY_CTA)
    h = h.replace('Schedule Intro Call', PRIMARY_CTA)
    h = h.replace('<a href="how-we-help.html">How We Help</a>', '<a href="case-studies.html">Case Studies</a>')
    h = h.replace('<a href="../how-we-help.html">How We Help</a>', '<a href="../case-studies.html">Case Studies</a>')
    h = h.replace('<a href="business-intelligence-consultant-cincinnati.html">Cincinnati Analytics Consulting</a>', '<a href="business-intelligence-consultant-cincinnati.html">Local Analytics Consulting</a>')
    h = h.replace('<a href="../business-intelligence-consultant-cincinnati.html">Cincinnati Analytics Consulting</a>', '<a href="../business-intelligence-consultant-cincinnati.html">Local Analytics Consulting</a>')
    h = h.replace('<a href="power-bi-consultant-cincinnati.html">Power BI Consulting</a>', '<a href="power-bi-consultant-cincinnati.html">Power BI &amp; Microsoft Fabric</a>')
    h = h.replace('<a href="../power-bi-consultant-cincinnati.html">Power BI Consulting</a>', '<a href="../power-bi-consultant-cincinnati.html">Power BI &amp; Microsoft Fabric</a>')
    return h


def global_cleanup(text: str) -> str:
    text = text.replace("Jonah Rosenthal", "Jonah Robinson")
    text = text.replace("KPI Reporting", "KPI Strategy & Executive Reporting")
    text = text.replace("KPI reporting", "KPI strategy and executive reporting")
    text = text.replace("Data Quality Review", "Data Quality & Reporting Reliability")
    text = text.replace("data quality review", "data quality and reporting reliability")
    text = text.replace("Dashboard Trust & Governance", "BI Governance & Dashboard Trust")
    text = text.replace("Cincinnati Data Analytics Consulting", "Local Analytics Consulting")
    text = text.replace("Cincinnati Analytics Consulting", "Local Analytics Consulting")
    text = text.replace("Power BI Consulting", "Power BI & Microsoft Fabric")
    text = text.replace("Power BI consulting", "Power BI and Microsoft Fabric consulting")
    text = text.replace("Book a Fit Check", PRIMARY_CTA)
    text = text.replace("Request the Fit Check", PRIMARY_CTA)
    text = text.replace("Request a Free Fit Check", PRIMARY_CTA)
    text = text.replace("Start With a Free Fit Check", PRIMARY_CTA)
    text = text.replace("Start with a Free Fit Check", PRIMARY_CTA)
    text = text.replace("Discuss a Power BI Project", PRIMARY_CTA)
    return text


def create_about(base: str) -> str:
    header = extract_header(base)
    footer = extract_footer(base)
    title = "About Parallax Data Lab"
    desc = "Learn what Parallax Data Lab does, who founder Jonah Robinson is, and how the company helps teams build trusted analytics, BI governance, and decision-ready reporting."
    head = re.sub(r"<title>[\s\S]*?</script>", meta_block(title, desc, "https://parallaxdatalab.com/about/") + "\n" + schema_webpage(title, desc, "https://parallaxdatalab.com/about/", "About"), base.split("</head>")[0])
    head = re.sub(r"<title>[\s\S]*", meta_block(title, desc, "https://parallaxdatalab.com/about/") + "\n" + schema_webpage(title, desc, "https://parallaxdatalab.com/about/", "About"), head)
    main = """<main class="about-page about-page-modern">
<section aria-labelledby="about-hero-title" class="about-hero about-hero-modern" id="about-top">
<div class="about-hero-inner motion-layer" data-depth="0.08">
<div class="about-hero-copy">
<p class="page-kicker">About Parallax Data Lab</p>
<h1 id="about-hero-title">About Parallax Data Lab</h1>
<p>Parallax Data Lab is a founder-led analytics consulting practice for teams that already have reports, dashboards, and data tools, but need more trust, structure, and decision clarity from them.</p>
<ul class="about-check-list">
<li>BI systems that leaders can inspect and explain</li>
<li>Metrics with owners, definitions, and decision context</li>
<li>Reporting operations that are easier to govern and maintain</li>
</ul>
<div class="about-hero-actions">
<a class="primary-action" href="contact.html">Start a Conversation</a>
<a class="secondary-action" href="case-studies.html">Explore Case Studies</a>
</div>
</div>
<aside aria-label="Parallax Data Lab at a glance" class="reset-glance about-glance-panel reset-glance-refined about-glance-consistent">
<p class="page-kicker">At a glance</p>
<dl>
<div><dt>Founder</dt><dd>Jonah Robinson</dd></div>
<div><dt>Focus</dt><dd>Trust, structure, and decision clarity</dd></div>
<div><dt>Best fit</dt><dd>Teams with analytics in place, but reduced confidence in it</dd></div>
</dl>
</aside>
</div>
</section>
<section class="about-pov reveal-card" id="about-pov">
<div class="about-shell">
<p class="page-kicker">Point of view</p>
<h2>Analytics should function as a decision system, not a collection of reports.</h2>
<p class="about-section-lede">Most analytics problems are not dashboard problems first. They are clarity, ownership, governance, reliability, and decision-design problems underneath the reporting layer.</p>
<div class="about-rule-grid">
<article><img alt="Layered analytics structure supporting clean dashboard outputs" class="about-card-image" src="assets/about-pov-structure.webp" loading="lazy" decoding="async"><h3>Structure before visualization</h3><p>Dashboards should reflect a stable system, not substitute for one.</p></article>
<article><img alt="Multiple metric definitions converging into one governed analytics definition layer" class="about-card-image" src="assets/about-pov-definitions.webp" loading="lazy" decoding="async"><h3>Definitions before aggregation</h3><p>One metric should mean one thing everywhere it appears.</p></article>
<article><img alt="Central ownership hub connecting governed decision responsibilities" class="about-card-image" src="assets/about-pov-ownership.webp" loading="lazy" decoding="async"><h3>Ownership before scale</h3><p>If no one owns the truth, trust always breaks down over time.</p></article>
</div>
</div>
</section>
<section class="about-why reveal-card" id="about-story">
<div class="about-why-copy">
<p class="page-kicker">Why Parallax exists</p>
<h2>A shift in viewpoint often reveals the real problem underneath analytics friction.</h2>
<p>Parallax Data Lab exists because analytics often grows faster than the structure supporting it. The result is familiar: more dashboards, more debates, and less confidence in what should happen next.</p>
<p class="about-parallax-definition">Parallax means the same object can look different when the viewing angle changes. In analytics, that matters because a dashboard problem often reveals a deeper definition, ownership, reliability, or decision-system problem once the frame shifts.</p>
</div>
<img alt="Modern Parallax Data Lab illustration showing fragmented analytics signals becoming a clear decision system" class="about-why-art" src="assets/about-why-foundation-shift.webp" loading="lazy" decoding="async">
</section>
<section class="about-founder reveal-card" id="about-founder">
<div class="about-founder-media about-founder-media-clean">
<figure class="about-founder-portrait-card"><img alt="Portrait of Jonah Robinson, founder of Parallax Data Lab" class="about-founder-portrait" src="assets/Jonah.webp" loading="lazy" decoding="async"></figure>
<div class="about-founder-artifact-panel" aria-label="Founder credibility artifacts"><img alt="Modern glowing cube accent illustrating the Parallax perspective" class="about-founder-cube" src="assets/about-founder-cube-glow.webp" loading="lazy" decoding="async"></div>
</div>
<div class="about-founder-copy">
<p class="page-kicker">Founder</p>
<h2>Jonah Robinson</h2>
<p>Parallax Data Lab is led by Jonah Robinson, a data leader who has owned analytics end to end across complex environments, products, and business lines.</p>
<p class="about-highlight-title">Relevant experience includes:</p>
<ul class="about-arrow-list">
<li><strong>Analytics and BI:</strong> Power BI, semantic models, KPI design, executive reporting, dashboards, and reporting automation.</li>
<li><strong>Data engineering and architecture:</strong> SQL, Python, model design, source-system logic, refresh reliability, and governed data paths.</li>
<li><strong>Governance and leadership:</strong> stakeholder alignment, metric ownership, prioritization, analytics operating cadence, and decision-system cleanup.</li>
</ul>
<p class="about-founder-perspective">The work is not to produce more dashboards by default. It is to change the frame, find the structural issue, and build the decision system the business can actually run.</p>
</div>
</section>
<section class="about-proof-layer reveal-card" aria-labelledby="about-proof-layer-title">
<p class="page-kicker">Why clients trust Parallax</p>
<h2 id="about-proof-layer-title">Practical analytics experience, applied with restraint.</h2>
<p class="about-section-lede">Parallax is built for organizations where reporting complexity is creating executive friction, duplicated effort, unreliable refreshes, unclear KPI ownership, or a backlog of dashboards no one fully trusts.</p>
<div class="about-proof-grid">
<article><span>Credential</span><strong>Bachelor's in mathematics</strong><p>Useful for metric logic, model structure, analysis quality, and knowing when a number is not yet reliable enough for leadership decisions.</p></article>
<article><span>Platforms</span><strong>Power BI, Microsoft Fabric, SQL, Python, JavaScript, spreadsheets, automation workflows</strong><p>Broad enough to move across dashboards, source logic, lightweight tools, and custom workflow prototypes without treating every problem as only a BI build.</p></article>
<article><span>Organizations</span><strong>SaaS, industrial operations, B2B services, field services, manufacturing, and growing operators</strong><p>The common thread is reporting complexity, KPI disagreement, manual recurring work, and leadership teams that need clearer signal.</p></article>
<article><span>Method</span><strong>Diagnose, define, simplify, govern, then support</strong><p>The methodology starts with decision friction, not dashboard requests. That keeps the work grounded in operating improvement.</p></article>
</div>
</section>
<section class="about-systems reveal-card" id="about-systems">
<div class="about-shell">
<p class="page-kicker">How the work shows up</p>
<h2>A few examples of how the point of view turns into practical analytics work.</h2>
<div class="about-systems-grid">
<article><img alt="Manual reporting work transforming into an automated analytics pipeline" class="about-card-image" src="assets/about-systems-automate-reporting.webp" loading="lazy" decoding="async"><h3>Automate reporting that still runs manually</h3><p>Replace spreadsheet-heavy, fragile workflows with automated pipelines and governed refresh logic so results are consistent and repeatable.</p></article>
<article><img alt="Overlapping dashboards consolidating into a smaller trusted reporting set" class="about-card-image" src="assets/about-systems-dashboard-sprawl.webp" loading="lazy" decoding="async"><h3>Reduce dashboard sprawl and duplicate logic</h3><p>Audit reporting ecosystems to identify repeated metrics, redundant dashboards, and overlapping logic, then consolidate into fewer trusted assets.</p></article>
<article><img alt="Fragmented data model reorganizing into scalable governed architecture" class="about-card-image" src="assets/about-systems-data-model-scale.webp" loading="lazy" decoding="async"><h3>Fix data models that block speed and scale</h3><p>Restructure data models to improve performance, reduce load time, and eliminate brittle relationships so dashboards stay useful as usage grows.</p></article>
</div>
<p class="about-center-note strong">These are examples, not a fixed menu. The right path depends on where trust, speed, reliability, or ownership is breaking.</p>
<a class="primary-action" href="contact.html">Start a Conversation</a>
</div>
</section>
</main>"""
    return head + "\n</head>\n<body>\n<canvas aria-hidden=\"true\" id=\"constellation\"></canvas>\n" + header + "\n" + main + "\n" + footer + '<script src="home.js?v=171"></script>\n</body>\n</html>\n'


def create_contact(base: str) -> str:
    header = extract_header(base)
    footer = extract_footer(base)
    title = "Start a Conversation | Parallax Data Lab"
    desc = "Contact Parallax Data Lab about Power BI, Microsoft Fabric, KPI strategy, reporting automation, data quality, BI governance, and analytics architecture."
    head = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\"/>\n<meta content=\"width=device-width, initial-scale=1.0\" name=\"viewport\"/>\n" + meta_block(title, desc, "https://parallaxdatalab.com/contact/") + "\n" + schema_webpage(title, desc, "https://parallaxdatalab.com/contact/", "Contact") + "\n</head>"
    form_match = re.search(r"<form[\s\S]*?</form>", base)
    if form_match:
        form = form_match.group(0).replace("<h2>Start The Conversation</h2>", "<h2>Start a Conversation</h2>")
        form = form.replace(PRIMARY_CTA, "Send Inquiry")
    else:
        form = """<form action="https://formsubmit.co/" data-form-user="jonahnr" data-form-domain="gmail.com" class="about-contact-form" method="POST">
<input name="_subject" type="hidden" value="New Parallax Data Lab Contact Request"/>
<input name="_template" type="hidden" value="table"/>
<input name="_captcha" type="hidden" value="false"/>
<input name="_next" type="hidden" value="https://parallaxdatalab.com/thank-you/"/>
<h2>Start a Conversation</h2>
<label>Name<input name="name" placeholder="Enter your name" required="" type="text"/></label>
<label>Email Address<input name="email" placeholder="Enter your email" required="" type="email"/></label>
<label>Company<input name="company" placeholder="Company or organization" type="text"/></label>
<label>What do you need help with?<select name="topic" required=""><option value="">Select one</option><option>Power BI &amp; Microsoft Fabric</option><option>KPI Strategy &amp; Executive Reporting</option><option>Reporting Automation</option><option>Data Quality &amp; Reporting Reliability</option><option>BI Governance &amp; Dashboard Trust</option><option>Data Integration &amp; Analytics Architecture</option><option>Not sure yet</option></select></label>
<label>Message<textarea name="message" placeholder="Share the problem, friction, or decision area you want to improve..." required=""></textarea></label>
<button type="submit">Send Inquiry</button>
</form>"""
    main = f"""<main class="about-page about-page-modern contact-page">
<section aria-labelledby="contact-title" class="about-hero about-hero-modern contact-hero">
<div class="about-hero-inner motion-layer" data-depth="0.08">
<div class="about-hero-copy">
<p class="page-kicker">Contact Parallax Data Lab</p>
<h1 id="contact-title">Start a Conversation</h1>
<p>Reach out when reporting is too manual, dashboards are not trusted, metric definitions are drifting, Power BI or Microsoft Fabric needs stronger structure, or leadership needs a clearer analytics path.</p>
<div class="about-hero-actions">
<a class="primary-action" href="#contact-form">Send an Inquiry</a>
<a class="secondary-action" href="free-fit-check.html">Book a 15-Minute Fit Check</a>
</div>
</div>
<aside aria-label="What happens next" class="reset-glance about-glance-panel reset-glance-refined about-glance-consistent">
<p class="page-kicker">What happens next</p>
<dl>
<div><dt>1</dt><dd>Share the situation and the business question behind it.</dd></div>
<div><dt>2</dt><dd>Parallax reviews the context and replies with a sensible next step.</dd></div>
<div><dt>3</dt><dd>If there is a fit, the next conversation scopes the smallest useful engagement.</dd></div>
</dl>
</aside>
</div>
</section>
<section class="about-contact reveal-card" id="contact-form">
<div class="about-contact-intro">
<p class="page-kicker">Qualified inquiries</p>
<h2>Use the form for consulting questions, project fit, or a reporting issue you want to untangle.</h2>
<p>Useful context includes the decision being slowed down, the reports or tools involved, the teams affected, and whether the issue is trust, speed, governance, automation, or architecture.</p>
<p><a href="free-fit-check.html">The Free Fit Check</a> is the fastest route when you want a short first conversation before writing a detailed brief.</p>
</div>
{form}
<aside class="about-next-card">
<h3>Privacy and expectations</h3>
<p>Do not include passwords, credentials, protected health information, or sensitive customer data in the form. Parallax uses your submission only to respond to your inquiry and evaluate fit.</p>
<h3>Typical response</h3>
<ol>
<li>Reply within three business days</li>
<li>Clarifying questions if the issue is broad</li>
<li>A recommendation for fit check, diagnostic, project scope, or no paid engagement</li>
</ol>
<a class="about-book" href="https://calendly.com/jonahnr/parallax-data-lab-intro-call">Book a 15-Minute Fit Check</a>
<a class="about-email-link" href="#" data-mail-user="jonahnr" data-mail-domain="gmail.com" data-mail-subject="Parallax Data Lab Inquiry">Email us</a>
</aside>
</section>
</main>"""
    return head + "\n<body>\n<canvas aria-hidden=\"true\" id=\"constellation\"></canvas>\n" + header + "\n" + main + "\n" + footer + '<script src="home.js?v=171"></script>\n</body>\n</html>\n'


def create_case_studies(base: str) -> str:
    header = extract_header(base)
    footer = extract_footer(base)
    title = "Case Studies | Parallax Data Lab"
    desc = "Anonymized Parallax Data Lab case studies covering dashboard consolidation, KPI ownership, reporting automation, and analytics architecture."
    head = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\"/>\n<meta content=\"width=device-width, initial-scale=1.0\" name=\"viewport\"/>\n" + meta_block(title, desc, "https://parallaxdatalab.com/case-studies/") + "\n" + schema_webpage(title, desc, "https://parallaxdatalab.com/case-studies/", "Case Studies") + "\n</head>"
    cases = [
        ("Dashboard consolidation", "$50M-$100M industrial software company", "Industrial software and recurring revenue operations", "14 overlapping dashboards, 4 executive views, and 1 governed revenue definition", "Leadership reviewed overlapping dashboards with conflicting revenue logic.", "Revenue conversations were being spent reconciling numbers instead of deciding where to intervene.", "Duplicate report pages, unclear owners, inconsistent revenue logic, and no single governed executive view.", "Mapped report owners, inventoried revenue logic, consolidated duplicate views, and established one governed executive revenue definition.", "Power BI, semantic model review, KPI definition mapping, reporting inventory, stakeholder decision mapping.", "Report inventory, governed revenue definition, executive-ready view, ownership notes, and retirement recommendations.", "Verified figures from the existing site: 14 reports consolidated into 4 executive views, with 1 governed revenue definition.", "Fewer reconciliation loops and a clearer path from revenue movement to leadership action.", "Explore Case Studies", "power-bi-consultant-cincinnati.html"),
        ("KPI ownership and weekly cadence", "500+ employee, multi-region field services company", "Field services with regional operating variation", "5 disputed KPIs, 5 named owners, and 1 weekly action cadence", "Regional leaders used different definitions for completion rate, backlog, and margin.", "Without ownership, weekly reviews turned into debates about definitions instead of staffing, routing, and margin decisions.", "Metric definitions varied by region, thresholds were unclear, and the meeting cadence had no explicit owner for follow-up.", "Defined each KPI, named business owners, documented thresholds, and tied metrics to weekly decisions.", "KPI ownership framework, executive reporting design, decision cadence mapping, governance facilitation.", "Metric owner matrix, KPI definitions, threshold logic, and weekly action cadence.", "Verified figures from the existing site: 5 disputed KPIs mapped to 5 named owners and 1 weekly action cadence.", "Leaders could see who owned interpretation and response for each priority signal.", "View KPI Strategy & Executive Reporting", "kpi-reporting-consulting.html"),
        ("Reporting automation", "$25M-$50M B2B services company", "B2B services with CRM, finance, and delivery reporting", "Manual exports moved into automated refresh and a trusted scorecard", "Managers copied CRM, finance, and delivery data into recurring status reports.", "Manual assembly created duplicated effort, version drift, and delayed management conversations.", "Source extracts were copied into spreadsheets, definitions were undocumented, and scorecard refresh depended on manual assembly.", "Automated the refresh path, documented definitions, and rebuilt the scorecard around recurring decisions.", "Reporting automation, refresh monitoring, source review, scorecard design, KPI documentation.", "Automated workflow, scorecard rebuild, definition notes, refresh expectations, and maintenance guidance.", "No verified quantitative savings were available in project files, so results are stated qualitatively.", "Reduced manual reporting effort, improved consistency, and gave managers a scorecard they could use weekly.", "View Reporting Automation", "reporting-automation-consulting.html"),
        ("Analytics architecture foundation", "$100M+ multi-entity manufacturer", "Manufacturing operations with disconnected operating systems", "6 source systems, 1 governed data path, and daily reliability checks", "Six source systems fed finance and operations reporting through undocumented extracts and copied transformations.", "The architecture made reporting hard to trust, hard to scale, and risky to extend into operational intelligence.", "Systems of record were unclear, transformations were duplicated, and reliability checks were not visible.", "Mapped systems of record, defined reusable business entities, and established one governed path into the reporting layer.", "Data integration, analytics architecture, reliability checks, entity modeling, governance design.", "Source inventory, target architecture, governed data path, first reporting domain, and daily reliability checks.", "Verified figures from the existing site: 6 source systems organized into 1 governed data path with daily reliability checks.", "Leadership and operating teams gained a more scalable foundation for governed reporting.", "View Data Integration & Analytics Architecture", "data-integration-analytics-architecture.html"),
    ]
    articles = []
    for name, client, env, scale, challenge, mattered, issues, work, methods, deliverables, results, outcomes, cta, href in cases:
        articles.append(f"""<article class="case-study-expanded reveal-card">
<p class="page-kicker">Anonymized case study</p>
<h2>{name}</h2>
<div class="case-study-artifact" aria-label="{html.escape(name)} summary visual"><span>{html.escape(scale.split(',')[0])}</span><span>{html.escape(scale.split(',')[-1].strip())}</span><span>Governed foundation</span></div>
<dl>
<div><dt>Client or organization type</dt><dd>{client}</dd></div>
<div><dt>Industry or operating environment</dt><dd>{env}</dd></div>
<div><dt>Scale and complexity</dt><dd>{scale}</dd></div>
<div><dt>Original challenge</dt><dd>{challenge}</dd></div>
<div><dt>Why it mattered</dt><dd>{mattered}</dd></div>
<div><dt>Issues identified</dt><dd>{issues}</dd></div>
<div><dt>Work completed</dt><dd>{work}</dd></div>
<div><dt>Technology and methods</dt><dd>{methods}</dd></div>
<div><dt>Deliverables</dt><dd>{deliverables}</dd></div>
<div><dt>Measurable results</dt><dd>{results}</dd></div>
<div><dt>Qualitative outcomes</dt><dd>{outcomes}</dd></div>
<div><dt>Relevant expertise</dt><dd>{', '.join(x[0] for x in EXPERTISE[:4])}</dd></div>
</dl>
<a class="primary-action" href="{href}">{cta}</a>
</article>""")
    main = """<main class="case-studies-page">
<section class="hero-section hero-section-refined case-studies-hero">
<div class="hero-copy">
<p class="page-kicker">Case Studies</p>
<h1>Anonymized stories of reporting trust, KPI ownership, automation, and analytics architecture.</h1>
<p>These examples preserve confidentiality while retaining the verified scale, constraints, work completed, and outcomes already represented in Parallax Data Lab content.</p>
<div class="hero-actions"><a class="primary-action" href="free-fit-check.html">Book a 15-Minute Fit Check</a><a class="secondary-action" href="contact.html">Start a Conversation</a></div>
</div>
</section>
<section class="case-study-section reveal-card">
<div class="case-study-heading"><p class="page-kicker">Client work</p><h2>Representative engagements</h2><p>Company identities are protected. Metrics appear only where they already existed in project files or site content.</p></div>
<div class="case-study-expanded-grid">
""" + "\n".join(articles) + """
</div>
</section>
</main>"""
    return head + "\n<body>\n<canvas aria-hidden=\"true\" id=\"constellation\"></canvas>\n" + header + "\n" + main + "\n" + footer + '<script src="home.js?v=171"></script>\n</body>\n</html>\n'


def update_index(text: str) -> str:
    text = text.replace('alt="Jonah Robinson, founder of Parallax Data Lab"', 'alt="Jonah Robinson, founder of Parallax Data Lab"')
    text = text.replace('Book a Fit Check', PRIMARY_CTA)
    text = re.sub(r'<section aria-labelledby="case-study-title" class="case-study-section reveal-card">[\s\S]*?</section>',
                  """<section aria-labelledby="case-study-title" class="case-study-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Anonymized client work</p>
<h2 id="case-study-title">Specific operating problems. Practical analytics outcomes.</h2>
<p>Concise previews from anonymized engagements. The full Case Studies page expands the client context, work completed, verified figures, and qualitative outcomes.</p>
</div>
<div class="case-study-grid">
<article><div class="case-study-artifact" aria-label="Dashboard consolidation visual"><span>14 reports</span><span>4 executive views</span><span>1 governed revenue definition</span></div><p class="page-kicker">$50M-$100M industrial software company</p><h3>Consolidated overlapping revenue reporting into an executive view.</h3><p>Mapped dashboard owners, removed duplicate views, and established governed revenue logic so leadership could move from reconciliation to action.</p><a class="secondary-action" href="case-studies.html">Read the case study</a></article>
<article><div class="case-study-artifact case-study-artifact-alt" aria-label="Metric ownership visual"><span>5 disputed KPIs</span><span>5 named owners</span><span>1 weekly cadence</span></div><p class="page-kicker">500+ employee field services company</p><h3>Turned KPI debates into an owned weekly decision cadence.</h3><p>Defined priority KPIs, named owners, and connected thresholds to staffing, routing, and margin decisions.</p><a class="secondary-action" href="case-studies.html">Read the case study</a></article>
<article><div class="case-study-artifact case-study-artifact-third" aria-label="Automation result visual"><span>Manual exports</span><span>Automated refresh</span><span>Trusted scorecard</span></div><p class="page-kicker">$25M-$50M B2B services company</p><h3>Replaced recurring reporting assembly with a trusted scorecard workflow.</h3><p>Automated refresh, documented definitions, and reduced duplicated report development around recurring management decisions.</p><a class="secondary-action" href="case-studies.html">Read the case study</a></article>
</div>
<div class="case-study-heading"><a class="primary-action" href="case-studies.html">Explore Case Studies</a></div>
</section>""", text)
    unique = """<section class="patterns-section reveal-card" aria-labelledby="homepage-patterns-title">
<p class="page-kicker">Common reporting and analytics pain points</p>
<h2 id="homepage-patterns-title">The visible dashboard issue is often a systems issue underneath.</h2>
<div class="pattern-diagnostic-slider">
<article><h3>Slow or brittle Power BI environments</h3><p>Reports technically work, but refreshes, filters, and model changes are fragile because the model, metric layer, and reporting views are tangled together.</p></article>
<article><h3>Metrics defined differently across teams</h3><p>Teams use the same metric name with different logic, filters, or time windows, so leadership meetings drift into reconciliation.</p></article>
<article><h3>Predictive work blocked by unstable standards</h3><p>Forecasting, scoring, and AI-assisted intelligence need stable definitions and owners before advanced analytics can be trusted.</p></article>
</div>
</section>"""
    if "homepage-patterns-title" not in text:
        text = text.replace('<section class="work-section reveal-card"', unique + '\n<section class="work-section reveal-card"', 1)
    return text


def update_power_bi(text: str) -> str:
    replacement = """<section class="power-bi-project-examples reveal-card" aria-labelledby="power-bi-project-example-title"><p class="page-kicker">Anonymized project examples</p><h2 id="power-bi-project-example-title">Representative Power BI and Microsoft Fabric engagements</h2><div class="power-bi-use-case-grid"><article><h3>Multi-site operational reporting</h3><p>Consolidated fragmented reporting into a more consistent Power BI environment with shared operational definitions, governed semantic logic, role-specific views, and clearer ownership for refresh expectations.</p></article><article><h3>Executive reporting automation</h3><p>Replaced recurring spreadsheet assembly with an automated scorecard workflow, monitored refresh, documented KPI definitions, and a more reliable weekly reporting cadence.</p></article><article><h3>Secure customer analytics</h3><p>Designed customer-facing or account-team reporting with tested RLS, reusable semantic logic, access boundaries, and controlled distribution so teams could scale analytics without duplicating reports.</p></article><article><h3>Predictive operations analytics</h3><p>Combined governed historical operating data, reusable features, confidence thresholds, and intervention tracking so teams could review risk signals alongside current performance without treating AI output as a new source of truth.</p></article></div><p class="power-bi-ai-boundary"><strong>Outcome boundary:</strong> verified quantitative results were not available in the project files for these examples, so this section uses qualitative outcomes only.</p></section>"""
    text = re.sub(r'<section class="power-bi-project-examples[\s\S]*?</section>', replacement, text)
    text = text.replace('Power BI | Dashboards, DAX & KPI Strategy & Executive Reporting', 'Power BI & Microsoft Fabric | Dashboards, DAX & KPI Strategy')
    text = text.replace('Power BI & Microsoft Fabric | Dashboards, DAX & KPI Strategy & Executive Reporting', 'Power BI & Microsoft Fabric | Dashboards, DAX & KPI Strategy')
    if "case-studies.html" not in text[text.find('expertise-related-articles'):text.find('power-bi-mock-section')]:
        text = text.replace('</div>\n</section>\n<section class="local-seo-section power-bi-mock-section', '</div><a class="primary-action" href="case-studies.html">Explore Case Studies</a>\n</section>\n<section class="local-seo-section power-bi-mock-section', 1)
    return text


def update_workspace(text: str) -> str:
    text = text.replace("<title>Decision Workspace | Parallax Data Lab</title>", "<title>Interactive Decision Workspace Demo | Parallax Data Lab</title>")
    text = text.replace('content="A client workspace for turning Parallax Data Lab recommendations into owned decisions, metrics, dashboards, and action plans."', 'content="A noindex interactive prototype demonstrating how Parallax Data Lab recommendations can be organized into decisions, metrics, dashboards, and action plans."')
    text = text.replace('content="Decision Workspace | Parallax Data Lab"', 'content="Interactive Decision Workspace Demo | Parallax Data Lab"')
    text = text.replace('New client workspace', 'Interactive prototype')
    text = text.replace('Create your reporting action workspace.', 'Explore the Interactive Decision Workspace Demo.')
    text = text.replace('Start an organization account to turn recommendations into owned decisions, metrics, dashboards, and action plans.', 'This noindex prototype demonstrates decision, metric, dashboard, and action-plan workflows. Do not enter confidential production data.')
    text = text.replace('Secure client access', 'Prototype access')
    text = text.replace('Your reporting work, behind a real account.', 'A demonstration workspace, separated from production consulting delivery.')
    text = text.replace('<li>Email verification for new accounts</li>\n        <li>Secure Supabase password authentication</li>\n        <li>Self-service password recovery</li>', '<li>Demonstration workflow for account-based access</li>\n        <li>No public production security promise</li>\n        <li>No confidential or persistent client data should be entered</li>')
    text = text.replace('Need help accessing an existing workspace?', 'Want to discuss a production-ready workspace?')
    text = text.replace('Decision Workspace</p>', 'Interactive Decision Workspace Demo</p>')
    text = text.replace('Delete the active organization only after confirming twice. This removes its users, recommendations, metrics, decisions, and dashboards from the local prototype.', 'Delete the active demo organization only after confirming twice. This removes its users, recommendations, metrics, decisions, and dashboards from the prototype.')
    return text


ARTICLE_BLOCKS = {
    "why-nobody-trusts-your-dashboard": ("Trust Trace Model", "Before redesigning a dashboard, trace five links: source, transformation, metric definition, owner, and decision use. If one link is missing, the issue is not visual design yet.", "This advice applies less when the report is used for one-off exploration rather than recurring leadership decisions."),
    "why-executive-teams-argue-about-numbers": ("Decision Rights Lens", "The fastest way out of number debates is to name which leadership decision each metric governs, then assign the business owner who can accept tradeoffs in definition and timing.", "Do not force one definition to serve finance close, sales coaching, and operating triage if those decisions need different views."),
    "hidden-cost-of-reporting-misalignment": ("Misalignment Cost Map", "Look for cost in rework, delayed meetings, duplicated analysis, and quiet loss of confidence. The largest cost is usually decision delay, not dashboard labor.", "A lightweight map is enough when the business already agrees on the problem and only needs execution."),
    "single-source-of-truth-myth": ("Certified Spine, Local Views", "The useful alternative to a mythical single source of truth is a certified metric spine with explicit local views for teams that need different operating cuts.", "Do not centralize exploratory analysis too early; experimentation needs room as long as certified metrics stay protected."),
    "five-signs-your-reporting-environment-is-breaking-down": ("Reporting Breakpoint Checklist", "Five signals matter most: disputed definitions, hidden manual steps, ownerless reports, unreliable refreshes, and leadership meetings that start with reconciliation.", "A temporary spreadsheet can still be acceptable when the decision is rare, low-risk, and visibly documented."),
    "kpi-governance-explained-growing-organizations": ("Minimum Viable KPI Governance", "Start with the smallest governance layer that can hold: definition, owner, source, refresh expectation, decision cadence, and exception rule.", "Heavy councils and approval boards are usually too much for small teams unless regulatory or audit risk requires them."),
    "kpi-ownership-framework-every-leadership-team-needs": ("Metric Ownership Contract", "Every priority KPI needs an accountable owner, contributors, a definition steward, and a decision cadence. Ownership is not authorship of the report; it is accountability for interpretation and response.", "Ownership breaks when assigned to a data team that cannot make the business tradeoff."),
    "how-to-build-metrics-people-actually-use": ("Usefulness Filter", "A metric earns its place only if someone can name the decision it supports, the threshold that changes action, and the person responsible for follow-up.", "Exploratory metrics can live outside the executive scorecard until their decision role is proven."),
    "why-executive-dashboards-fail": ("Executive Dashboard Test", "A dashboard is executive-ready when it shows fewer signals, clearer confidence, named owners, and a next conversation. More visuals often make the operating model less clear.", "Deep diagnostic pages can still belong in analyst views; they should not crowd the executive surface."),
    "stop-measuring-everything-designing-executive-reporting-that-drives-action": ("Signal Budget", "Leadership attention is finite. Treat the executive report like a signal budget: only include metrics that can trigger discussion, escalation, or a change in operating rhythm.", "Broad metric libraries are useful for discovery, but they should not be mistaken for executive reporting."),
    "what-should-be-included-in-weekly-business-review": ("Weekly Review Spine", "A useful weekly business review contains priority signals, movement explanation, owner notes, decisions needed, and follow-up from the prior cadence.", "Monthly board reporting and weekly operating review need different levels of detail and different tolerance for noise."),
    "the-difference-between-reporting-and-decision-making": ("Report-to-Decision Gap", "Reporting describes what happened. Decision-making clarifies what matters, who owns it, what changed, and what action follows.", "Some compliance and audit reports only need accurate recordkeeping; forcing decision language onto them can add clutter."),
    "building-executive-dashboards-that-create-accountability": ("Accountability Layer", "Add owner, threshold, status, and follow-up fields to priority metrics. The dashboard should make accountability visible without turning into a task tracker.", "Avoid public shaming mechanics; accountability should clarify response, not create defensive behavior."),
    "when-to-hire-head-of-analytics": ("Analytics Leadership Trigger", "Hire senior analytics leadership when the bottleneck is prioritization, governance, stakeholder tradeoffs, and operating cadence rather than report production volume alone.", "If the work is mostly a short backlog of well-defined builds, a focused contractor may be enough."),
    "what-fractional-analytics-leadership-actually-means": ("Fractional Leadership Operating Model", "Fractional analytics leadership works best when it owns cadence, standards, prioritization, and decision support while internal teams retain business context.", "It is not a substitute for internal ownership when the organization needs full-time people management."),
    "building-analytics-function-without-hiring-full-team": ("Lean Analytics Function", "A lean function needs explicit intake, certified metrics, a support model, and a small number of operating rituals before it needs a large team.", "Do not underinvest when regulatory reporting, production data engineering, or 24/7 operational support is truly required."),
    "why-data-teams-struggle-to-earn-trust": ("Trust Earned Through Tradeoffs", "Data teams earn trust by making tradeoffs visible: what is certified, what is directional, what is delayed, and what should not be used yet.", "Trust is harder to rebuild if leadership continues rewarding speed over reliability."),
    "analytics-maturity-roadmap-reporting-to-decision-systems": ("Maturity Is Decision Readiness", "The roadmap is not tool maturity. It is movement from scattered reporting to governed decisions, reusable logic, and reliable operating cadence.", "Advanced tooling can be premature if basic ownership and definition standards are still unstable."),
    "ai-enablement-starts-with-trusted-business-data": ("AI Readiness Gate", "AI enablement should start with governed business questions, trusted metric definitions, access boundaries, and a human-owned response path.", "For brainstorming and drafting, AI can help earlier; for metric interpretation, the foundation matters first."),
    "prepare-reporting-environment-for-ai": ("Reporting Foundation for AI", "Prepare for AI by documenting metric meaning, lineage, security, known exclusions, and benchmark questions that can test whether answers are useful.", "Do not build AI wrappers over reports that leaders already distrust."),
    "where-ai-actually-helps-in-analytics-operations": ("Useful AI Operations Loop", "AI helps with summarization, anomaly triage, documentation, and question routing when the source signals are governed and humans own the final decision.", "It should not become an invisible decision-maker for high-impact operating calls."),
    "operations-intelligence-digest-for-leadership": ("Digest, Not Dashboard Pack", "A useful operations digest ranks attention, explains why it matters, names owners, and separates urgent exceptions from background movement.", "It is less useful when leaders still need raw exploration rather than prioritized operating signal."),
    "governance-rls-architecture-business-issue": ("Access Is a Business Rule", "RLS is not only a technical permission setting. It expresses territory, customer, role, and confidentiality rules that business leaders must own.", "Simple internal dashboards may not need elaborate RLS if audience and data sensitivity are limited."),
    "dashboards-to-predictive-risk-intelligence": ("Prediction Requires Response Design", "Risk intelligence only matters if each score has an owner, threshold, explanation, and intervention path.", "Do not score risks the organization has no capacity or authority to act on."),
    "dashboard-problem-leadership-problem": ("Leadership System Check", "When dashboards fail, inspect leadership alignment: decision rights, operating cadence, metric tradeoffs, and willingness to retire low-value reporting.", "A dashboard can still be the main issue when the business logic is sound and the usability is genuinely poor."),
}


def enhance_article(text: str, slug: str) -> str:
    if slug not in ARTICLE_BLOCKS or "Parallax field framework" in text:
        return text
    title, body, boundary = ARTICLE_BLOCKS[slug]
    block = f"""<section class="article-framework callout-section">
<h2>Parallax field framework: {title}</h2>
<p>{body}</p>
<h3>Where this advice does not apply</h3>
<p>{boundary}</p>
<h3>Practical next step</h3>
<p>Pick one recurring leadership decision and trace the source, definition, owner, refresh expectation, and action path behind it. That single trace usually reveals whether the problem is reporting, governance, architecture, or decision design.</p>
</section>
"""
    if '<section class="article-service-cta-block">' in text:
        return text.replace('<section class="article-service-cta-block">', block + '<section class="article-service-cta-block">', 1)
    return text.replace('</article>', block + '</article>', 1)


def prefix_nested_paths(text: str) -> str:
    text = re.sub(r'(href|src)="(assets/[^"]*)"', r'\1="../\2"', text)
    text = re.sub(r'(href|src)="(home\.(?:css|js)\?v=\d+)"', r'\1="../\2"', text)
    text = re.sub(r'(href|src)="(decision-workspace\.(?:css|js)\?v=\d+)"', r'\1="../\2"', text)
    text = re.sub(r'(href)="((?:favicon|apple-touch-icon|social-preview)[^"]*)"', r'\1="../\2"', text)
    text = re.sub(r"url\('assets/", "url('../assets/", text)

    def local_href(match: re.Match) -> str:
        target = match.group(1)
        if target.startswith(("#", "/", "../", "assets/", "http://", "https://", "mailto:", "tel:")):
            return f'href="{target}"'
        if ".html" in target or target.startswith("insights/"):
            return f'href="../{target}"'
        return f'href="{target}"'

    return re.sub(r'href="([^"]+)"', local_href, text)


def prefix_insight_clean_route(text: str) -> str:
    text = text.replace('href="../', 'href="../../')
    text = text.replace('src="../', 'src="../../')
    text = text.replace("url('../", "url('../../")
    text = re.sub(r'(href)="((?!https?:|mailto:|tel:|#|/|\.\./)[^"]+\.html[^"]*)"', r'\1="../\2"', text)
    return text


def update_sitemap() -> None:
    urls = [
        "",
        "about/",
        "contact/",
        "case-studies/",
        "our-offerings/",
        "expertise/",
        "power-bi-consultant-cincinnati/",
        "kpi-reporting-consulting/",
        "reporting-automation-consulting/",
        "data-quality-review/",
        "dashboard-trust-governance/",
        "data-integration-analytics-architecture/",
        "analytics-health-check/",
        "decision-system-reset/",
        "fractional-analytics/",
        "free-fit-check/",
        "dashboard-trust-scorecard/",
        "intelligence-lab/",
        "insights/",
        "business-intelligence-consultant-cincinnati/",
        "privacy-policy/",
    ]
    for article in sorted((ROOT / "insights").glob("*.html")):
        urls.append(f"insights/{article.stem}/")
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        body.append(f"  <url><loc>https://parallaxdatalab.com/{url}</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>")
    body.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(body) + "\n")


def update_redirects() -> None:
    path = ROOT / "_redirects"
    text = read(path) if path.exists() else ""
    additions = [
        "/how-we-help /our-offerings/ 301",
        "/how-we-help/ /our-offerings/ 301",
        "/how-we-help.html /our-offerings/ 301",
    ]
    lines = [line for line in text.splitlines() if "how-we-help" not in line]
    for add in additions:
        if add not in lines:
            lines.append(add)
    write(path, "\n".join(lines).strip() + "\n")


def main() -> None:
    base = global_cleanup(read(ROOT / "about.html"))
    write(ROOT / "about.html", update_header_footer(create_about(base)))
    write(ROOT / "contact.html", update_header_footer(create_contact(base)))
    write(ROOT / "case-studies.html", update_header_footer(create_case_studies(read(ROOT / "index.html"))))

    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts or path.name == "how-we-help.html" or "how-we-help" in path.parts:
            continue
        text = read(path)
        text = global_cleanup(text)
        text = update_header_footer(text)
        if path.name == "index.html" and path.parent == ROOT:
            text = update_index(text)
        if path.name == "power-bi-consultant-cincinnati.html":
            text = update_power_bi(text)
        if path.name == "decision-workspace.html":
            text = update_workspace(text)
        if path.parent.name == "insights" and path.suffix == ".html":
            text = enhance_article(text, path.stem)
            text = text.replace('href="decision-workspace.html"', 'href="../decision-workspace.html"')
        text = re.sub(r"home\.css\?v=\d+", "home.css?v=171", text)
        text = re.sub(r"home\.js\?v=\d+", "home.js?v=171", text)
        write(path, text)

    # Sync clean route copies from root pages.
    for slug in SYNC_PAGES:
        source = ROOT / f"{slug}.html"
        target = ROOT / slug / "index.html"
        if source.exists():
            write(target, prefix_nested_paths(read(source)))

    for source in sorted((ROOT / "insights").glob("*.html")):
        if source.name == "index.html":
            continue
        target = ROOT / "insights" / source.stem / "index.html"
        write(target, prefix_insight_clean_route(read(source)))

    # Keep retired How We Help files as redirect stubs for local QA.
    redirect_stub = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>How We Help Moved | Parallax Data Lab</title>
<meta name="description" content="The How We Help page has moved to the Parallax Data Lab offerings page."/>
<meta name="robots" content="noindex, follow"/>
<link rel="canonical" href="https://parallaxdatalab.com/our-offerings/"/>
<meta property="og:title" content="How We Help Moved | Parallax Data Lab"/>
<meta property="og:description" content="The How We Help page has moved to the Parallax Data Lab offerings page."/>
<meta property="og:url" content="https://parallaxdatalab.com/our-offerings/"/>
<meta property="og:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="How We Help Moved | Parallax Data Lab"/>
<meta name="twitter:description" content="The How We Help page has moved to the Parallax Data Lab offerings page."/>
<meta name="twitter:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>
<meta http-equiv="refresh" content="0; url=our-offerings.html"/>
</head>
<body><h1>How We Help has moved</h1><p>This page has moved to <a href="our-offerings.html">Our Offerings</a>.</p></body>
</html>
"""
    write(ROOT / "how-we-help.html", redirect_stub)
    write(ROOT / "how-we-help" / "index.html", redirect_stub.replace("our-offerings.html", "../our-offerings.html"))

    update_sitemap()
    update_redirects()


if __name__ == "__main__":
    main()

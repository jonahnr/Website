from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOCIAL = "https://parallaxdatalab.com/assets/social-preview.webp"
CSS = "home.css?v=125"
JS = "home.js?v=125"

META = {
    "index.html": (
        "Parallax Data Lab | Business Intelligence Consulting",
        "Business intelligence and data analytics consulting for teams that need clearer dashboards, better reporting, and trusted KPI visibility.",
        "https://parallaxdatalab.com/",
    ),
    "our-offerings.html": (
        "BI, Dashboard & Analytics Consulting | Parallax Data Lab",
        "Explore business intelligence, dashboard development, Power BI consulting, reporting automation, and analytics cleanup services.",
        "https://parallaxdatalab.com/our-offerings/",
    ),
    "our-offerings/index.html": (
        "BI, Dashboard & Analytics Consulting | Parallax Data Lab",
        "Explore business intelligence, dashboard development, Power BI consulting, reporting automation, and analytics cleanup services.",
        "https://parallaxdatalab.com/our-offerings/",
    ),
    "how-we-help.html": (
        "Analytics Reporting Help for Growing Teams | Parallax Data Lab",
        "See how Parallax Data Lab helps teams clean up reporting, define KPIs, improve dashboards, and build trusted analytics systems.",
        "https://parallaxdatalab.com/how-we-help/",
    ),
    "how-we-help/index.html": (
        "Analytics Reporting Help for Growing Teams | Parallax Data Lab",
        "See how Parallax Data Lab helps teams clean up reporting, define KPIs, improve dashboards, and build trusted analytics systems.",
        "https://parallaxdatalab.com/how-we-help/",
    ),
    "intelligence-lab.html": (
        "Analytics Intelligence Lab | Parallax Data Lab",
        "Practical analytics resources, reporting ideas, dashboard guidance, and business intelligence insights for growing teams.",
        "https://parallaxdatalab.com/intelligence-lab/",
    ),
    "intelligence-lab/index.html": (
        "Analytics Intelligence Lab | Parallax Data Lab",
        "Practical analytics resources, reporting ideas, dashboard guidance, and business intelligence insights for growing teams.",
        "https://parallaxdatalab.com/intelligence-lab/",
    ),
    "insights.html": (
        "Business Intelligence Insights | Parallax Data Lab",
        "Read business intelligence insights on dashboard trust, KPI reporting, analytics cleanup, and reporting systems for growing teams.",
        "https://parallaxdatalab.com/insights/",
    ),
    "insights/index.html": (
        "Business Intelligence Insights | Parallax Data Lab",
        "Read business intelligence insights on dashboard trust, KPI reporting, analytics cleanup, and reporting systems for growing teams.",
        "https://parallaxdatalab.com/insights/",
    ),
    "free-fit-check.html": (
        "Dashboard & Reporting Fit Check | Parallax Data Lab",
        "Take the Parallax Data Lab Fit Check to assess your dashboards, reporting gaps, KPI visibility, and analytics readiness.",
        "https://parallaxdatalab.com/free-fit-check/",
    ),
    "free-fit-check/index.html": (
        "Dashboard & Reporting Fit Check | Parallax Data Lab",
        "Take the Parallax Data Lab Fit Check to assess your dashboards, reporting gaps, KPI visibility, and analytics readiness.",
        "https://parallaxdatalab.com/free-fit-check/",
    ),
    "about.html": (
        "Contact Parallax Data Lab | Cincinnati Analytics Consulting",
        "Contact Parallax Data Lab for business intelligence consulting, dashboard development, Power BI support, and analytics reporting help.",
        "https://parallaxdatalab.com/about/",
    ),
    "about/index.html": (
        "Contact Parallax Data Lab | Cincinnati Analytics Consulting",
        "Contact Parallax Data Lab for business intelligence consulting, dashboard development, Power BI support, and analytics reporting help.",
        "https://parallaxdatalab.com/about/",
    ),
}


FOOTER = """<footer aria-label="Site footer" class="site-footer site-footer-refined">
  <div class="site-footer-inner">
    <div class="site-footer-col site-footer-about">
      <a class="site-footer-brand" href="index.html">Parallax Data Lab</a>
      <p>Parallax Data Lab provides business intelligence consulting, Power BI dashboard development, reporting automation, and analytics support for teams that need clearer data.</p>
      <p class="site-footer-location">Cincinnati, Ohio. Based in Cincinnati and serving teams across the United States.</p>
      <a class="site-footer-email" href="#" data-mail-user="jonahnr" data-mail-domain="gmail.com" data-mail-subject="Parallax Data Lab Inquiry">Email us</a>
      <a class="site-footer-contact-button" href="about.html#contact-us">Contact Parallax Data Lab</a>
    </div>
    <nav aria-label="Footer navigation" class="site-footer-col">
      <h3>Pages</h3>
      <a href="index.html">Home</a>
      <a href="our-offerings.html">Services</a>
      <a href="how-we-help.html">How We Help</a>
      <a href="free-fit-check.html">Fit Check</a>
      <a href="intelligence-lab.html">Intelligence Lab</a>
      <a href="about.html#contact-us">Contact</a>
      <a href="privacy-policy.html">Privacy Policy</a>
    </nav>
    <nav aria-label="Footer consulting services" class="site-footer-col">
      <h3>Services</h3>
      <a href="our-offerings.html">Business Intelligence Consulting</a>
      <a href="our-offerings.html#power-bi-dashboard-development">Power BI Dashboard Development</a>
      <a href="our-offerings.html#reporting-automation">Reporting Automation</a>
      <a href="free-fit-check.html">Dashboard and Reporting Fit Check</a>
      <a href="intelligence-lab.html">Analytics Reporting Resources</a>
    </nav>
    <div class="site-footer-col site-footer-contact">
      <h3>Contact</h3>
      <a class="site-footer-secondary" href="https://calendly.com/jonahnr/parallax-data-lab-intro-call">Book a Fit Check</a>
      <a class="site-footer-secondary" href="about.html#contact-us">Contact Parallax Data Lab</a>
      <a class="site-footer-secondary" href="https://www.linkedin.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    </div>
  </div>
  <div class="site-footer-bottom">
    <p>&copy; 2026 Parallax Data Lab. All rights reserved.</p>
  </div>
</footer>"""


HOME_MAIN = """<main class="home-page">
<section class="hero-section" id="top">
<a aria-label="Parallax Data Lab home" class="hero-brand motion-layer" data-depth="0.08" href="index.html">
<img alt="Parallax Data Lab logo" class="hero-logo" src="assets/parallax_data_lab_original_transparent.png"/>
</a>
<div aria-hidden="true" class="hero-rule"></div>
<div class="hero-copy motion-layer" data-depth="-0.05">
<h1>Business Intelligence Consulting for Teams That Need Clearer Data</h1>
<p>Parallax Data Lab helps companies replace messy spreadsheets, manual reporting, and unclear metrics with trusted dashboards, reporting systems, and analytics workflows.</p>
<div class="hero-proof-tags" aria-label="Business intelligence consulting proof points">
<span>Power BI dashboards</span>
<span>KPI reporting</span>
<span>analytics cleanup</span>
<span>reporting automation</span>
<span>data quality review</span>
</div>
<div class="hero-actions">
<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>
<a class="secondary-action" href="our-offerings.html">Explore Services</a>
</div>
<strong class="micro-promise">Hands-on dashboard development, reporting cleanup, and KPI visibility for growing teams.</strong>
</div>
</section>
<section class="diagnostic-section reveal-card">
<h2>When scattered business data slows decisions</h2>
<div class="diagnostic-panel">
<article>
<div>
<h3>Manual reports become the operating system.</h3>
<p>Teams copy numbers between spreadsheets, dashboards, and slide decks until no one is sure which version is current.</p>
</div>
<img alt="Business intelligence dashboard example" class="diagnostic-image" src="assets/home-generated/diagnostic-owner-drift.webp"/>
</article>
<article>
<div>
<h3>Metrics lose shared meaning.</h3>
<p>Parallax helps clean up analytics reporting, define trusted KPIs, and build dashboards that answer the questions leaders ask every week.</p>
</div>
<img alt="KPI reporting system organized into trusted metrics" class="diagnostic-image" src="assets/home-generated/diagnostic-structural-balance.webp"/>
</article>
</div>
</section>
<section class="work-section" id="services">
<div class="work-shell reveal-card">
<p class="page-kicker">Services</p>
<h2>Business intelligence, dashboard, and analytics consulting</h2>
<p class="section-lede">Use Parallax when your team needs practical help with <a href="our-offerings.html">business intelligence consulting</a>, <a href="our-offerings.html#power-bi-dashboard-development">Power BI dashboard development</a>, analytics reporting, and operational reporting cleanup.</p>
<div class="service-offer-grid">
<article><h3>Business Intelligence Consulting</h3><p>Build clearer reporting systems, define the right KPIs, and create dashboards leaders can trust.</p></article>
<article id="power-bi-dashboard-development"><h3>Power BI Dashboard Development</h3><p>Design and improve Power BI dashboards that are easier to use, easier to maintain, and tied to real business questions.</p></article>
<article id="reporting-automation"><h3>Reporting Automation</h3><p>Reduce manual spreadsheet work by streamlining recurring reports, refresh processes, and executive visibility.</p></article>
<article><h3>Analytics Foundation Review</h3><p>Assess your reporting stack, data quality, dashboard usage, and analytics gaps before investing in more tools.</p></article>
<article><h3>KPI and Metrics Design</h3><p>Clarify which metrics matter, how they should be calculated, and where teams should go to answer key business questions.</p></article>
</div>
<a class="primary-action" href="our-offerings.html">Explore Services</a>
</div>
</section>
<section class="concrete-proof-section reveal-card">
<div class="concrete-proof-heading">
<p class="page-kicker">Common problems</p>
<h2>Long-tail reporting issues Parallax helps fix</h2>
</div>
<div class="seo-intent-grid">
<article><h3>When your dashboards are not trusted</h3><p>We trace conflicting numbers back to definitions, model logic, ownership, and reporting workflow so leaders know which dashboard should guide action.</p></article>
<article><h3>When reporting still depends on spreadsheets</h3><p>We help teams move from recurring spreadsheet reporting toward automated business reporting, governed refreshes, and cleaner executive visibility.</p></article>
<article><h3>When leaders ask for numbers your team cannot easily explain</h3><p>We clarify the KPI logic, data source, filters, and owner so teams can explain what changed and why it matters.</p></article>
<article><h3>When Power BI reports exist but are hard to use</h3><p>We simplify Power BI dashboards around real business questions, reduce clutter, and make the reporting experience easier to maintain.</p></article>
<article><h3>When your metrics are inconsistent across teams</h3><p>We design shared KPI definitions and reporting standards so teams stop debating basic numbers and start improving performance.</p></article>
</div>
</section>
<section class="proof-section reveal-card">
<div class="proof-intro">
<p class="page-kicker">Dashboard and Reporting Fit Check</p>
<h2>Start with a quick dashboard and reporting Fit Check.</h2>
<p>After you submit it, you can schedule a 1:1 review to walk through your reporting gaps, dashboard opportunities, and highest-value next steps.</p>
</div>
<div class="proof-grid">
<article><strong>Data quality assessment</strong><p>Where unclear sources, manual refreshes, or duplicate spreadsheets are weakening trust.</p></article>
<article><strong>KPI dashboard consulting</strong><p>Which dashboard questions, metrics, and views matter most for leadership visibility.</p></article>
<article><strong>Analytics roadmap</strong><p>A practical recommendation for cleanup, dashboard development, reporting automation, or deeper analytics foundation work.</p></article>
</div>
<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>
</section>
<section class="lab-section lab-promise-section reveal-card">
<p class="page-kicker">Intelligence Lab</p>
<h2>Practical analytics reporting resources for teams building clearer systems.</h2>
<p>The Intelligence Lab is the supporting resource hub for reporting ideas, dashboard guidance, and business intelligence insights once the main service path is clear.</p>
<div class="lab-promise-grid lab-topic-grid">
<article><h3>What Makes a Power BI Dashboard Actually Useful?</h3><p>How to judge whether a dashboard helps leaders answer real questions.</p></article>
<article><h3>Business Intelligence Consulting: What It Is and When You Need It</h3><p>How outside BI help can clean up reporting and improve KPI visibility.</p></article>
<article><h3>How to Know Your Reporting Process Is Breaking</h3><p>Signals that spreadsheets, manual refreshes, and unclear ownership are slowing decisions.</p></article>
<article><h3>Spreadsheet Reporting vs Dashboard Reporting</h3><p>When spreadsheet workflows still make sense and when automation is overdue.</p></article>
<article><h3>How to Build KPIs Leaders Can Trust</h3><p>Why KPI design depends on definitions, ownership, and business context.</p></article>
<article><h3>Why Dashboards Fail Even When the Data Is Available</h3><p>How clutter, weak metric design, and unclear action paths undermine adoption.</p></article>
</div>
<a class="secondary-action" href="intelligence-lab.html">Explore analytics reporting resources</a>
</section>
<section class="faq-section reveal-card">
<p class="page-kicker">FAQ</p>
<h2>Business intelligence consulting questions</h2>
<div class="faq-grid">
<article><h3>What does a business intelligence consultant do?</h3><p>A BI consultant helps teams define KPIs, clean up reporting logic, build dashboards, automate recurring reports, and make business data easier to trust.</p></article>
<article><h3>Can you help improve an existing Power BI dashboard?</h3><p>Yes. Parallax can simplify Power BI reports, improve usability, clarify metrics, and connect dashboards to the business questions leaders actually ask.</p></article>
<article><h3>What if our reporting is mostly spreadsheets today?</h3><p>That is common. The work usually starts by identifying repeated manual reporting, fragile spreadsheet logic, and the best path from spreadsheet to dashboard.</p></article>
<article><h3>Do we need a data warehouse before improving dashboards?</h3><p>No. Some teams need a stronger data foundation first, but many dashboard and reporting improvements can begin with the systems already in place.</p></article>
<article><h3>How does the Fit Check work?</h3><p>You share the reporting friction, then schedule a 1:1 review to discuss dashboard gaps, KPI visibility, and the highest-value next steps.</p></article>
</div>
</section>
<section class="closing-section">
<h2>Build dashboards and reporting leaders can trust.</h2>
<p>Get a clear read on what is breaking and the best next step.</p>
<div class="hero-actions">
<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>
<a class="secondary-action" href="about.html#contact-us">Contact Parallax Data Lab</a>
</div>
</section>
</main>"""


FAQ_SCHEMA = """<script type="application/ld+json" id="homepage-faq-schema">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does a business intelligence consultant do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A BI consultant helps teams define KPIs, clean up reporting logic, build dashboards, automate recurring reports, and make business data easier to trust."
      }
    },
    {
      "@type": "Question",
      "name": "Can you help improve an existing Power BI dashboard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Parallax can simplify Power BI reports, improve usability, clarify metrics, and connect dashboards to business questions."
      }
    },
    {
      "@type": "Question",
      "name": "What if our reporting is mostly spreadsheets today?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The work can start by identifying repeated manual reporting, fragile spreadsheet logic, and the best path from spreadsheet to dashboard."
      }
    },
    {
      "@type": "Question",
      "name": "Do we need a data warehouse before improving dashboards?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Some teams need a stronger data foundation first, but many dashboard and reporting improvements can begin with existing systems."
      }
    },
    {
      "@type": "Question",
      "name": "How does the Fit Check work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You share the reporting friction, then schedule a 1:1 review to discuss dashboard gaps, KPI visibility, and highest-value next steps."
      }
    }
  ]
}
</script>"""


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def replace_or_insert_meta(text: str, title: str, desc: str, url: str, is_home: bool) -> str:
    text = re.sub(r"\s*<meta\s+name=\"keywords\"[^>]*>\s*", "\n", text, flags=re.I)
    text = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", text, count=1, flags=re.S)
    text = re.sub(r"<meta\s+[^>]*name=\"description\"[^>]*>", f'<meta name="description" content="{desc}"/>', text, count=1, flags=re.I)
    text = re.sub(r"<link\s+[^>]*rel=\"canonical\"[^>]*>", f'<link rel="canonical" href="{url}"/>', text, count=1, flags=re.I)
    text = re.sub(r"<link\s+href=\"home\.css\?v=\d+\"\s+rel=\"stylesheet\"/>", f'<link href="{CSS}" rel="stylesheet"/>', text)
    text = re.sub(r"<script src=\"home\.js\?v=\d+\"></script>", f'<script src="{JS}"></script>', text)

    favicon_block = (
        '<meta name="theme-color" content="#0b1745"/>\n'
        '<link rel="icon" href="/favicon.ico" sizes="any"/>\n'
        '<link rel="icon" type="image/png" href="/favicon.png"/>\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>'
    )
    text = re.sub(
        r"<meta name=\"theme-color\" content=\"#0b1745\"/>\s*<link.*?(?=<script type=\"application/ld\+json\"|<!-- Google tag)",
        favicon_block,
        text,
        count=1,
        flags=re.S,
    )

    og_block = (
        '<meta content="website" property="og:type"/>\n'
        '<meta content="Parallax Data Lab" property="og:site_name"/>\n'
        f'<meta property="og:title" content="{title}"/>\n'
        f'<meta property="og:description" content="{desc}"/>\n'
        f'<meta property="og:url" content="{url}"/>\n'
        f'<meta property="og:image" content="{SOCIAL}"/>\n'
        '<meta name="twitter:card" content="summary_large_image"/>\n'
        f'<meta name="twitter:title" content="{title}"/>\n'
        f'<meta name="twitter:description" content="{desc}"/>\n'
        f'<meta name="twitter:image" content="{SOCIAL}"/>'
    )
    text = re.sub(
        r"<meta content=\"website\" property=\"og:type\"/>.*?<meta content=\"[^\"]*\" name=\"twitter:image\"/>",
        og_block,
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"<meta property=\"og:title\".*?<meta name=\"twitter:image\"[^>]*>",
        og_block,
        text,
        count=1,
        flags=re.S,
    )
    if 'property="og:title"' not in text and "property='og:title'" not in text:
        if '<script type="application/ld+json">' in text:
            text = text.replace('<script type="application/ld+json">', og_block + '\n<script type="application/ld+json">', 1)
        else:
            text = text.replace("</head>", og_block + "\n</head>", 1)
    text = text.replace("https://parallaxdatalab.com/social-preview.webp", SOCIAL)
    text = re.sub(
        r"<link href=\"apple-touch-icon\.png\?v=\d+\" rel=\"apple-touch-icon\"/><link href=\"favicon\.svg\?v=\d+\" rel=\"icon\" type=\"image/svg\+xml\"/><link href=\"favicon\.ico\?v=\d+\" rel=\"icon\" sizes=\"any\"/>",
        '<link rel="icon" href="/favicon.ico" sizes="any"/>\n<link rel="icon" type="image/png" href="/favicon.png"/>\n<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>',
        text,
    )
    if is_home:
        org_schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Parallax Data Lab",
  "url": "https://parallaxdatalab.com/",
  "description": "Business intelligence and data analytics consulting for teams that need clearer dashboards, better reporting, and trusted KPI visibility.",
  "areaServed": "United States",
  "serviceType": [
    "Business Intelligence Consulting",
    "Data Analytics Consulting",
    "Power BI Consulting",
    "Dashboard Development",
    "Analytics Reporting"
  ],
  "founder": {
    "@type": "Person",
    "name": "Jonah Robinson"
  }
}
</script>
""" + FAQ_SCHEMA
        text = re.sub(r"<script type=\"application/ld\+json\">.*?</script>", org_schema, text, count=1, flags=re.S)
    return text


def replace_footer(text: str) -> str:
    return re.sub(r"<footer aria-label=\"Site footer\".*?</footer>", FOOTER, text, count=1, flags=re.S)


def update_home(text: str) -> str:
    return re.sub(r"<main class=\"home-page\">.*?</main>", HOME_MAIN, text, count=1, flags=re.S)


def update_services(text: str) -> str:
    text = text.replace(
        "<h1>Choose the right path when there is too much reporting and not enough trusted signal for decisions.</h1>",
        "<h1>Business Intelligence, Dashboard, and Analytics Consulting</h1>",
    )
    text = text.replace(
        "Use the ladder below to avoid guessing: the scorecard is optional for self-diagnosis, the Fit Check is the core free starting point, and the paid diagnostic or advanced work only follows when the evidence supports it.",
        "Parallax Data Lab helps growing teams clean up reporting, improve Power BI dashboards, automate business reporting, and create KPI visibility leaders can trust.",
    )
    text = text.replace('Request a Free Fit Check', 'Book a Fit Check')
    text = text.replace('Compare Engagement Paths', 'Explore Services')
    block = """<section class="offerings-section offer-chooser-section reveal-card" id="offer-chooser">
<p class="page-kicker">Services</p>
<h2>Practical consulting offers for clearer dashboards and reporting.</h2>
<p class="offerings-lede">Start with the service area closest to the pain: business intelligence consulting, Power BI consulting, dashboard development, analytics reporting, reporting automation, or KPI dashboard consulting.</p>
<div class="service-offer-grid service-offer-grid-page">
<article><span>01</span><h3>Business Intelligence Consulting</h3><p>Build clearer reporting systems, define the right KPIs, and create dashboards leaders can trust.</p></article>
<article id="power-bi-dashboard-development"><span>02</span><h3>Power BI Dashboard Development</h3><p>Design and improve Power BI dashboards that are easier to use, easier to maintain, and tied to real business questions.</p></article>
<article id="reporting-automation"><span>03</span><h3>Reporting Automation</h3><p>Reduce manual spreadsheet work by streamlining recurring reports, refresh processes, and executive visibility.</p></article>
<article><span>04</span><h3>Analytics Foundation Review</h3><p>Assess your reporting stack, data quality, dashboard usage, and analytics gaps before investing in more tools.</p></article>
<article><span>05</span><h3>KPI and Metrics Design</h3><p>Clarify which metrics matter, how they should be calculated, and where teams should go to answer key business questions.</p></article>
</div>
</section>"""
    text = re.sub(r"<section class=\"offerings-section offer-chooser-section.*?</section>", block, text, count=1, flags=re.S)
    return text


def update_fit_check(text: str) -> str:
    text = text.replace('Free Analytics Fit Check', 'Dashboard and Reporting Fit Check')
    text = text.replace(
        'A free 15-minute routing conversation to identify the smallest useful next step.',
        'Dashboard and Reporting Fit Check',
    )
    text = text.replace(
        'Use the Fit Check when there is too much reporting and not enough trusted signal for decisions. You can arrive directly, or bring the optional scorecard if you want to self-diagnose first. In 15 minutes, we clarify whether the issue points toward a paid diagnostic, decision-system rebuild, ongoing stewardship, intelligence work, or no engagement.',
        'Start with a quick dashboard and reporting Fit Check. After you submit it, you can schedule a 1:1 review to walk through your reporting gaps, dashboard opportunities, and highest-value next steps.',
    )
    text = text.replace('Request the 15-Minute Fit Check', 'Book a Fit Check')
    text = text.replace('Schedule Directly', 'Schedule 1:1 Review')
    text = text.replace(
        'Abstract scorecard and decision paths for the Free Fit Check',
        'Dashboard and reporting fit check',
    )
    text = text.replace(
        'Share enough context to make the 15-minute Fit Check useful.',
        'Share enough context to make the Fit Check useful.',
    )
    text = text.replace(
        'Short is fine. The goal is to understand what is breaking, what decisions are affected, and whether Parallax can point you toward a useful next step.',
        'Short is fine. The goal is to understand your dashboard gaps, KPI visibility issues, and reporting process so the 1:1 review can focus on the highest-value next steps.',
    )
    text = text.replace(
        'You will hear back with the best way to use the 15-minute meeting.',
        'Schedule the 1:1 review after you submit.',
    )
    text = text.replace(
        '<li>We review your context and confirm whether a Fit Check conversation makes sense.</li>\n<li>The meeting routes the issue toward the smallest useful next step.</li>\n<li>You leave with a recommended path, even if that path is not a paid engagement.</li>',
        '<li>Thanks for completing the Fit Check. Your responses help identify where your dashboards, reporting process, and KPI visibility may be breaking down.</li>\n<li>Schedule a 1:1 review so we can walk through the highest-value next steps.</li>\n<li>If the scheduler does not load, use the Calendly fallback link below.</li>',
    )
    return text


def update_thank_you(text: str) -> str:
    text = text.replace(
        "Thanks. We'll review your context and follow up with the clearest next step.",
        "Thanks for completing the Fit Check.",
    )
    text = text.replace(
        "You should hear back within three business days. In the meantime, you can review the engagement paths or schedule an intro call.",
        "Your responses help identify where your dashboards, reporting process, and KPI visibility may be breaking down. Schedule a 1:1 review below so we can walk through the highest-value next steps.",
    )
    text = text.replace('Compare Engagement Paths', 'Explore Services')
    text = text.replace('Schedule Intro Call', 'Schedule 1:1 Review')
    embed = """<section class="calendly-section reveal-card" aria-labelledby="calendly-title">
<p class="page-kicker">Schedule your review</p>
<h2 id="calendly-title">Choose a time for the 1:1 Fit Check review.</h2>
<div class="calendly-inline-widget" data-url="https://calendly.com/jonahnr/parallax-data-lab-intro-call" style="min-width:320px;height:700px;"></div>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
<p class="calendly-fallback">If the scheduler does not load, <a href="https://calendly.com/jonahnr/parallax-data-lab-intro-call">open the Calendly booking page</a>.</p>
</section>
"""
    text = re.sub(r'<section class="calendly-section reveal-card".*?</section>\s*', "", text, flags=re.S)
    text = text.replace("</main>", embed + "</main>", 1)
    return text


def update_how(text: str) -> str:
    text = text.replace(
        "<h1>Find the operating layer underneath messy analytics.</h1>",
        "<h1>Clearer Reporting for Teams Outgrowing Spreadsheets</h1>",
    )
    text = text.replace(
        "We help teams separate dashboard symptoms from the deeper issues in definitions, ownership, decision cadence, and operational signal quality.",
        "We help teams clean up reporting, define trusted KPIs, improve dashboards, and build analytics reporting systems that leaders can use without rechecking every number.",
    )
    text = text.replace(
        "The work turns too much reporting into a clearer system for what leaders should trust, review, and act on next.",
        "The work is practical: fewer duplicate spreadsheets, clearer Power BI reports, more consistent metrics, and a reporting process that can scale.",
    )
    text = text.replace('Request a Free Fit Check', 'Book a Fit Check')
    text = text.replace('Compare Engagement Paths', 'Explore Services')
    return text


def update_intel(text: str) -> str:
    text = text.replace(
        "Weekly operational intelligence for leaders with too much reporting and not enough trusted signal.",
        "Practical Analytics and Business Intelligence Insights",
    )
    text = text.replace(
        "The flagship Intelligence Lab offer is the Weekly Operational Intelligence Digest: a recurring signal product that turns a trusted analytics foundation into a clear leadership attention queue.",
        "The Intelligence Lab collects practical analytics resources, reporting ideas, dashboard guidance, and business intelligence insights for growing teams.",
    )
    text = text.replace('Request a Free Fit Check', 'Book a Fit Check')
    text = text.replace('Explore Intelligence Work', 'Explore Analytics Resources')
    return text


def update_about(text: str) -> str:
    text = text.replace(
        "Analytics consulting for teams that need clarity, not more dashboard volume.",
        "Contact Parallax Data Lab",
    )
    text = text.replace('Contact Us', 'Contact Parallax Data Lab')
    text = text.replace(
        "Analytics trust, decision systems, and senior data strategy",
        "Business intelligence consulting, Power BI dashboard development, reporting automation, and analytics support",
    )
    return text


def update_alt_text(text: str) -> str:
    text = text.replace('alt="Parallax Data Lab"', 'alt="Parallax Data Lab logo"')
    text = text.replace('alt="Abstract scorecard and decision paths for the Free Fit Check"', 'alt="Dashboard and reporting fit check"')
    return text


def main():
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        key = rel(path)
        title_desc_url = META.get(key)
        if title_desc_url:
            text = replace_or_insert_meta(text, *title_desc_url, is_home=(key == "index.html"))
        else:
            # Preserve unique page-level title/description but normalize modern SEO plumbing.
            title_m = re.search(r"<title>(.*?)</title>", text, flags=re.S)
            desc_m = re.search(r"<meta\s+[^>]*name=\"description\"[^>]*content=\"([^\"]*)\"[^>]*>|<meta\s+content=\"([^\"]*)\"\s+name=\"description\"[^>]*>", text, flags=re.I)
            canon_m = re.search(r"<link\s+[^>]*rel=\"canonical\"[^>]*href=\"([^\"]*)\"[^>]*>", text, flags=re.I)
            title = title_m.group(1).strip() if title_m else "Parallax Data Lab"
            desc = (desc_m.group(1) or desc_m.group(2)).strip() if desc_m else "Business intelligence and analytics consulting from Parallax Data Lab."
            url = canon_m.group(1).strip() if canon_m else "https://parallaxdatalab.com/"
            text = replace_or_insert_meta(text, title, desc, url, is_home=False)
        if key == "index.html":
            text = update_home(text)
        if key in {"our-offerings.html", "our-offerings/index.html"}:
            text = update_services(text)
        if key in {"free-fit-check.html", "free-fit-check/index.html"}:
            text = update_fit_check(text)
        if key in {"thank-you.html", "thank-you/index.html"}:
            text = update_thank_you(text)
        if key in {"how-we-help.html", "how-we-help/index.html"}:
            text = update_how(text)
        if key in {"intelligence-lab.html", "intelligence-lab/index.html", "insights.html", "insights/index.html"}:
            text = update_intel(text)
        if key in {"about.html", "about/index.html"}:
            text = update_about(text)
        text = update_alt_text(text)
        text = replace_footer(text)
        path.write_text(text, encoding="utf-8", newline="\n")

    # Keep the social preview and favicon files available at the paths used by metadata.
    assets = ROOT / "assets"
    if (ROOT / "social-preview.webp").exists() and not (assets / "social-preview.webp").exists():
        shutil.copy2(ROOT / "social-preview.webp", assets / "social-preview.webp")
    if (ROOT / "apple-touch-icon.png").exists() and not (assets / "apple-touch-icon.png").exists():
        shutil.copy2(ROOT / "apple-touch-icon.png", assets / "apple-touch-icon.png")


if __name__ == "__main__":
    main()

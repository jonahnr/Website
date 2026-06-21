from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CALENDLY = "https://calendly.com/jonahnr/parallax-data-lab-intro-call"
VERSION = "179"

CASE_STUDIES = [
    {
        "slug": "manufacturing-throughput",
        "industry": "Manufacturing",
        "title": "Manufacturing throughput reporting moved from spreadsheet reconciliation to governed operating signal.",
        "image": "assets/home-generated/failure-scale-breaks.webp",
        "type": "$100M+ multi-entity manufacturer",
        "environment": "Plant operations, finance, quality, and throughput reporting across disconnected systems.",
        "challenge": "Six source systems fed finance and operations reporting through undocumented extracts and copied transformations.",
        "work": "Mapped systems of record, defined reusable business entities, established one governed reporting path, and added daily reliability checks.",
        "outcome": "Leadership and operating teams gained a scalable foundation for trusted performance reporting.",
        "results": "Verified figures: 6 source systems organized into 1 governed data path with daily reliability checks.",
        "href": "data-integration-analytics-architecture.html",
        "cta": "View architecture work",
    },
    {
        "slug": "utilities-reliability",
        "industry": "Utilities",
        "title": "Utility reliability reporting clarified exceptions, ownership, and refresh confidence.",
        "image": "assets/home-generated/diagnostic-structural-balance.webp",
        "type": "Regional utility operations team",
        "environment": "Asset maintenance, outage review, compliance reporting, and weekly operating updates.",
        "challenge": "Reliability signals existed, but leaders could not see which exceptions were current, owned, or ready for escalation.",
        "work": "Designed an exception map, source reliability checklist, KPI owner model, and refresh-status layer for operating reviews.",
        "outcome": "Operations leaders could separate stale reporting noise from current reliability signals.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "data-quality-review.html",
        "cta": "View reliability work",
    },
    {
        "slug": "energy-operations",
        "industry": "Energy",
        "title": "Energy operations reporting connected field activity, production context, and executive review.",
        "image": "assets/home-generated/lab-operational-risk.webp",
        "type": "Energy operations group",
        "environment": "Distributed field operations, production monitoring, safety context, and leadership reporting.",
        "challenge": "Operational updates arrived from several teams, but the review process lacked a concise view of risk, exceptions, and owner response.",
        "work": "Built an operating-signal model with ranked exceptions, confidence notes, and a weekly decision cadence.",
        "outcome": "Leaders gained a clearer attention queue for operational review without turning every signal into another dashboard.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "intelligence-lab.html#predictive-risk-intelligence",
        "cta": "Explore Intelligence Lab",
    },
    {
        "slug": "logistics-service-level",
        "industry": "Logistics & Transportation",
        "title": "Logistics service-level reporting exposed bottlenecks before weekly review.",
        "image": "assets/home-generated/symptom-decisions-slow.webp",
        "type": "Multi-location logistics operator",
        "environment": "Fleet, delivery, exception, backlog, and customer service-level reporting.",
        "challenge": "Teams could see activity volume, but the reporting did not clarify which service exceptions needed action first.",
        "work": "Reframed metrics around service-level thresholds, owner response, routing decisions, and refresh confidence.",
        "outcome": "Managers gained a clearer weekly path from exception to owner to action.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "kpi-reporting-consulting.html",
        "cta": "View KPI strategy",
    },
    {
        "slug": "field-services-kpis",
        "industry": "Field Services",
        "title": "Field-service KPI debates became an owned weekly decision cadence.",
        "image": "assets/home-generated/help-situation-dashboard-trust.webp",
        "type": "500+ employee, multi-region field services company",
        "environment": "Regional operations with completion, backlog, margin, staffing, and routing metrics.",
        "challenge": "Regional leaders used different definitions for completion rate, backlog, and margin.",
        "work": "Defined each KPI, named business owners, documented thresholds, and tied metrics to weekly decisions.",
        "outcome": "Leaders could see who owned interpretation and response for each priority signal.",
        "results": "Verified figures: 5 disputed KPIs mapped to 5 named owners and 1 weekly action cadence.",
        "href": "kpi-reporting-consulting.html",
        "cta": "View KPI strategy",
    },
    {
        "slug": "construction-project-controls",
        "industry": "Construction",
        "title": "Construction project controls reporting reduced duplicated status work.",
        "image": "assets/home-generated/help-process-build-guide.webp",
        "type": "Construction project controls team",
        "environment": "Project status, schedule variance, cost updates, subcontractor status, and executive summaries.",
        "challenge": "Project updates were assembled manually, with different teams maintaining overlapping versions of status and risk.",
        "work": "Mapped recurring reporting steps, standardized project status definitions, and designed a cleaner reporting workflow.",
        "outcome": "Project leaders gained a more consistent view of status, variance, and next actions.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "reporting-automation-consulting.html",
        "cta": "View automation work",
    },
    {
        "slug": "healthcare-utilization",
        "industry": "Healthcare Operations",
        "title": "Healthcare utilization reporting separated operational signal from reporting noise.",
        "image": "assets/home-generated/assessment-trust-map.webp",
        "type": "Healthcare operations and utilization team",
        "environment": "Utilization, staffing, appointment flow, service lines, and recurring operating review.",
        "challenge": "Leaders had reports, but definitions and refresh timing made it hard to trust utilization movement.",
        "work": "Documented definitions, source timing, manual adjustments, and reporting confidence notes for review.",
        "outcome": "Operational teams could discuss exceptions with clearer context and fewer definition debates.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "data-quality-review.html",
        "cta": "View reliability work",
    },
    {
        "slug": "industrial-software-revenue",
        "industry": "Industrial Software",
        "title": "Industrial software revenue reporting consolidated overlapping executive dashboards.",
        "image": "assets/home-generated/power-bi-cincinnati-bi-model.webp",
        "type": "$50M-$100M industrial software company",
        "environment": "Recurring revenue, customer, finance, and executive dashboard reporting.",
        "challenge": "Leadership reviewed overlapping dashboards with conflicting revenue logic.",
        "work": "Mapped report owners, inventoried revenue logic, consolidated duplicate views, and established one governed executive revenue definition.",
        "outcome": "Revenue conversations could move from reconciliation to action.",
        "results": "Verified figures: 14 reports consolidated into 4 executive views, with 1 governed revenue definition.",
        "href": "power-bi-consultant-cincinnati.html",
        "cta": "View Power BI work",
    },
    {
        "slug": "b2b-services-scorecard",
        "industry": "B2B Services",
        "title": "B2B services reporting automation replaced manual scorecard assembly.",
        "image": "assets/home-generated/offerings-health-check.webp",
        "type": "$25M-$50M B2B services company",
        "environment": "CRM, finance, delivery, management scorecards, and recurring status reporting.",
        "challenge": "Managers copied CRM, finance, and delivery data into recurring status reports.",
        "work": "Automated the refresh path, documented definitions, and rebuilt the scorecard around recurring decisions.",
        "outcome": "Reduced manual reporting effort and improved consistency around weekly management review.",
        "results": "No verified quantitative savings available in project files; outcomes are qualitative.",
        "href": "reporting-automation-consulting.html",
        "cta": "View automation work",
    },
    {
        "slug": "retail-multi-location",
        "industry": "Retail & Multi-Location",
        "title": "Retail operating reporting aligned location performance, exceptions, and leadership follow-up.",
        "image": "assets/home-generated/symptom-metrics-shared-meaning.webp",
        "type": "Multi-location retail operator",
        "environment": "Location performance, labor, margin, inventory exceptions, and regional operating review.",
        "challenge": "Store and regional teams used similar metrics but interpreted performance movement differently.",
        "work": "Standardized KPI definitions, separated operating signals from context metrics, and clarified owner response.",
        "outcome": "Regional review became more focused on action thresholds and fewer competing interpretations.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "kpi-reporting-consulting.html",
        "cta": "View KPI strategy",
    },
    {
        "slug": "distribution-supply-chain",
        "industry": "Distribution & Supply Chain",
        "title": "Distribution reporting created a cleaner path from inventory signal to operating decision.",
        "image": "assets/home-generated/help-foundation-to-intelligence-advanced.webp",
        "type": "Distribution and supply-chain team",
        "environment": "Inventory, orders, fulfillment, supplier timing, service level, and exception reporting.",
        "challenge": "Operational signals were available, but teams lacked a governed path from source data to decision review.",
        "work": "Mapped source dependencies, documented business entities, and designed a governed reporting foundation.",
        "outcome": "Teams gained a clearer foundation for reliable supply-chain reporting and future intelligence work.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "data-integration-analytics-architecture.html",
        "cta": "View architecture work",
    },
    {
        "slug": "facilities-maintenance",
        "industry": "Facilities & Maintenance",
        "title": "Facilities maintenance reporting made recurring risk and backlog easier to review.",
        "image": "assets/home-generated/reset-trigger-action-v2.webp",
        "type": "Facilities and maintenance operations team",
        "environment": "Work orders, backlog, compliance checks, asset condition, and recurring management review.",
        "challenge": "Backlog and risk reporting existed, but leaders could not quickly see what required intervention.",
        "work": "Designed a decision-focused backlog view, exception thresholds, owner notes, and operating cadence.",
        "outcome": "Maintenance review became more explicit about priority, owner, and follow-up.",
        "results": "No verified quantitative client metrics available; outcomes are qualitative.",
        "href": "decision-system-reset.html",
        "cta": "View reset work",
    },
]

CASE_STUDY_GROUPS = [
    ("Industrial operations", ["Manufacturing", "Utilities", "Energy", "Construction"]),
    ("Distributed operations", ["Logistics & Transportation", "Field Services", "Retail & Multi-Location", "Facilities & Maintenance"]),
    ("Commercial and supply chain", ["Healthcare Operations", "Industrial Software", "B2B Services", "Distribution & Supply Chain"]),
]


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


def rel_for(path, asset):
    if path.parent.name == "insights" and path.suffix == ".html":
        return "../" + asset
    if path.name == "index.html" and path.parent.parent.name == "insights":
        return "../../" + asset
    if path.name == "index.html" and path.parent != ROOT:
        return "../" + asset
    return asset


def page_prefix(path):
    if path.parent.name == "insights" and path.suffix == ".html":
        return "../"
    if path.name == "index.html" and path.parent.parent.name == "insights":
        return "../../"
    if path.name == "index.html" and path.parent != ROOT:
        return "../"
    return ""


def case_dropdown(prefix=""):
    by_industry = {item["industry"]: item for item in CASE_STUDIES}
    groups = []
    for label, industries in CASE_STUDY_GROUPS:
        links = "\n".join(
            f'<a class="nav-menu-child" href="{prefix}case-studies.html#{by_industry[industry]["slug"]}"><span>{industry}</span></a>'
            for industry in industries
        )
        groups.append(f"""<details class="nav-menu-group">
<summary class="nav-menu-section-title">{label}</summary>
{links}
</details>""")
    return f"""<div class="nav-dropdown nav-dropdown-case-studies">
<a class="nav-dropdown-toggle" href="{prefix}case-studies.html">Case Studies</a>
<div aria-label="Case studies by industry" class="nav-dropdown-menu nav-menu-hierarchy nav-dropdown-menu-case-studies">
<a class="nav-menu-parent" href="{prefix}case-studies.html"><span>Case Studies Overview</span></a>
{chr(10).join(groups)}
</div>
</div>"""


def update_nav(text, prefix=""):
    case_pattern = re.compile(
        r'<div class="nav-dropdown nav-dropdown-case-studies">[\s\S]*?</details>\s*</div>\s*</div>\s*'
    )
    text = case_pattern.sub("", text)

    def update_primary(match):
        nav_html = match.group(0)
        insights_link = '<a href="' + prefix + 'insights.html">Insights</a>'
        if insights_link in nav_html:
            nav_html = nav_html.replace(insights_link, case_dropdown(prefix) + "\n" + insights_link, 1)
        return nav_html

    text = re.sub(
        r'<nav\b(?=[^>]*\bid="primary-navigation")[^>]*>[\s\S]*?</nav>',
        update_primary,
        text,
        count=1,
    )
    text = re.sub(
        r'<div aria-label="About Parallax Data Lab" class="nav-dropdown-menu nav-menu-hierarchy nav-dropdown-menu-about">[\s\S]*?</div>',
        f"""<div aria-label="About Parallax Data Lab" class="nav-dropdown-menu nav-menu-hierarchy nav-dropdown-menu-about">
<span class="nav-menu-section-title nav-menu-static-title">About</span>
<a class="nav-menu-parent" href="{prefix}about.html"><span>About Parallax</span></a>
<a class="nav-menu-child" href="{prefix}contact.html"><span>Contact</span></a>
<a class="nav-menu-child" href="{prefix}business-intelligence-consultant-cincinnati.html"><span>Local Analytics Consulting</span></a>
</div>""",
        text,
        count=1,
    )
    # Keep Intelligence Lab grouped and spacious like Offerings.
    text = text.replace('<summary class="nav-menu-section-title">Initiatives</summary>', '<summary class="nav-menu-section-title">Lab initiatives</summary>')
    return text


def case_card(item, prefix=""):
    return f"""<a class="industry-case-card" href="#{item["slug"]}">
<img src="{prefix}{item["image"]}" alt="{item["industry"]} analytics case study visual" loading="lazy" decoding="async">
<span>{item["industry"]}</span>
<strong>{item["title"]}</strong>
<em>Read story</em>
</a>"""


def case_story(item, prefix=""):
    return f"""<article class="case-study-expanded industry-case-story reveal-card" id="{item["slug"]}">
<img class="case-story-image" src="{prefix}{item["image"]}" alt="{item["industry"]} operations analytics case study image" loading="lazy" decoding="async">
<div class="case-story-copy">
<p class="page-kicker">{item["industry"]} / anonymized case study</p>
<h2>{item["title"]}</h2>
<dl>
<div><dt>Client or organization type</dt><dd>{item["type"]}</dd></div>
<div><dt>Industry or operating environment</dt><dd>{item["environment"]}</dd></div>
<div><dt>Original challenge</dt><dd>{item["challenge"]}</dd></div>
<div><dt>Work completed by Parallax</dt><dd>{item["work"]}</dd></div>
<div><dt>Results and outcomes</dt><dd>{item["results"]} {item["outcome"]}</dd></div>
<div><dt>Relevant expertise</dt><dd>Power BI &amp; Microsoft Fabric, KPI Strategy &amp; Executive Reporting, Reporting Automation, Data Quality &amp; Reporting Reliability, BI Governance &amp; Dashboard Trust, Data Integration &amp; Analytics Architecture</dd></div>
</dl>
<a class="primary-action" href="{prefix}{item["href"]}">{item["cta"]}</a>
</div>
</article>"""


def build_case_studies(prefix=""):
    cards = "\n".join(case_card(item, prefix) for item in CASE_STUDIES)
    stories = "\n".join(case_story(item, prefix) for item in CASE_STUDIES)
    return f"""<main class="case-studies-page">
<section class="hero-section hero-section-refined case-studies-hero">
<div class="hero-copy">
<p class="page-kicker">Case Studies</p>
<h1>Operations case studies across the industries Parallax supports.</h1>
<p>Explore anonymized stories across manufacturing, utilities, energy, logistics, field services, construction, healthcare operations, industrial software, B2B services, retail, distribution, and facilities maintenance.</p>
<div class="hero-actions"><a class="primary-action" href="{prefix}free-fit-check.html">Book a 15-Minute Fit Check</a><a class="secondary-action" href="{prefix}contact.html">Start a Conversation</a></div>
</div>
</section>
<section class="case-study-section industry-case-index reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Industry index</p>
<h2>Choose the operating environment closest to yours.</h2>
<p>Each card opens an anonymized story built around reporting trust, KPI ownership, automation, reliability, governance, or architecture.</p>
</div>
<div class="industry-case-grid">{cards}</div>
</section>
<section class="case-study-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Story details</p>
<h2>Representative operating analytics work</h2>
<p>Metrics are included only where they already existed in the site content. Otherwise outcomes are stated qualitatively.</p>
</div>
<div class="case-study-expanded-grid">{stories}</div>
</section>
</main>"""


def update_home_main(text):
    replacement = """<section aria-labelledby="case-study-title" class="case-study-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Anonymized client work</p>
<h2 id="case-study-title">Specific operating problems. Practical analytics outcomes.</h2>
<p>Concise previews from anonymized engagements. The full Case Studies page expands the client context, work completed, verified figures, qualitative outcomes, and industry-specific stories.</p>
</div>
<div class="case-study-grid">
<article><div class="case-study-artifact" aria-label="Dashboard consolidation visual"><span>14 reports</span><span>4 executive views</span><span>1 governed revenue definition</span></div><p class="page-kicker">$50M-$100M industrial software company</p><h3>Consolidated overlapping revenue reporting into an executive view.</h3><p>Mapped dashboard owners, removed duplicate views, and established governed revenue logic so leadership could move from reconciliation to action.</p><a class="secondary-action" href="case-studies.html#industrial-software-revenue">Read the case study</a></article>
<article><div class="case-study-artifact case-study-artifact-alt" aria-label="Metric ownership visual"><span>5 disputed KPIs</span><span>5 named owners</span><span>1 weekly cadence</span></div><p class="page-kicker">500+ employee field services company</p><h3>Turned KPI debates into an owned weekly decision cadence.</h3><p>Defined priority KPIs, named owners, and connected thresholds to staffing, routing, and margin decisions.</p><a class="secondary-action" href="case-studies.html#field-services-kpis">Read the case study</a></article>
<article><div class="case-study-artifact case-study-artifact-third" aria-label="Automation result visual"><span>Manual exports</span><span>Automated refresh</span><span>Trusted scorecard</span></div><p class="page-kicker">$25M-$50M B2B services company</p><h3>Replaced recurring reporting assembly with a trusted scorecard workflow.</h3><p>Automated refresh, documented definitions, and reduced duplicated report development around recurring management decisions.</p><a class="secondary-action" href="case-studies.html#b2b-services-scorecard">Read the case study</a></article>
<article><div class="case-study-artifact case-study-artifact-fourth" aria-label="Analytics architecture result visual"><span>6 source systems</span><span>1 governed data path</span><span>Daily reliability checks</span></div><p class="page-kicker">$100M+ multi-entity manufacturer</p><h3>Created a scalable reporting architecture across disconnected operating systems.</h3><p>Mapped systems of record, defined reusable business entities, and established one governed path into the reporting layer.</p><a class="secondary-action" href="case-studies.html#manufacturing-throughput">Read the case study</a></article>
</div>
<div class="case-study-heading"><a class="primary-action" href="case-studies.html">Explore Case Studies</a></div>
</section>"""
    return re.sub(r'<section aria-labelledby="case-study-title" class="case-study-section reveal-card">[\s\S]*?</section>', replacement, text, count=1)


def update_case_page(path, text):
    prefix = "../" if path.name == "index.html" and path.parent != ROOT else ""
    text = re.sub(r"<main class=\"case-studies-page\">[\s\S]*?</main>", build_case_studies(prefix), text, count=1)
    return text


def calendly_embed(prefix=""):
    return f"""<section class="calendly-section reveal-card" aria-labelledby="calendly-title">
<div>
<p class="page-kicker">Schedule directly</p>
<h2 id="calendly-title">Book a 15-minute Fit Check without leaving the page.</h2>
<p>Pick a time that works. If the scheduler does not load, use the fallback link below.</p>
</div>
<div class="calendly-inline-widget" data-url="{CALENDLY}" style="min-width:320px;height:700px;"></div>
<p class="calendly-fallback"><a href="{CALENDLY}">Open Calendly in a new tab</a></p>
</section>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>"""


def update_contact(text, prefix=""):
    text = re.sub(r'<h3>Privacy and expectations</h3>\s*<p>Do not include passwords[\s\S]*?</p>', '<h3>Typical response</h3>', text)
    text = text.replace('<h3>Typical response</h3>\n<h3>Typical response</h3>', '<h3>Typical response</h3>')
    if "calendly-inline-widget" not in text:
        text = text.replace("</section>\n</main>", "</section>\n" + calendly_embed(prefix) + "\n</main>", 1)
    return text


def update_fit_check(text, prefix=""):
    text = re.sub(r'<section aria-labelledby="fit-check-fit-title"[\s\S]*?</section>\s*', "", text, count=1)
    # Move form before the explanatory process section if needed.
    form = re.search(r'<section aria-labelledby="fit-check-form-title"[\s\S]*?</section>', text)
    process = re.search(r'<section aria-labelledby="fit-check-process-title"[\s\S]*?</section>', text)
    if form and process and process.start() < form.start():
        form_html = form.group(0)
        text = text[:form.start()] + text[form.end():]
        process = re.search(r'<section aria-labelledby="fit-check-process-title"[\s\S]*?</section>', text)
        text = text[:process.start()] + form_html + "\n" + text[process.start():]
    if "calendly-inline-widget" not in text:
        text = text.replace('<section aria-labelledby="fit-check-process-title"', calendly_embed(prefix) + '\n<section aria-labelledby="fit-check-process-title"', 1)
    return text


def update_article(text, path):
    prefix = page_prefix(path)
    asset = rel_for(path, "assets/jonah-founder-credibility.webp")
    text = re.sub(
        r'<div class="article-meta"><span>Written by Jonah Robinson</span>\s*<span>Published ([^<]+)</span></div>',
        f'<div class="article-meta article-meta-author"><span class="article-author-chip"><img src="{asset}" alt="Jonah Robinson" loading="lazy" decoding="async">Written by Jonah Robinson</span> <span>Published \\1</span></div>',
        text,
    )
    text = re.sub(r'<section class="article-service-cta-block">[\s\S]*?</section>\s*', "", text)
    text = hide_share_labels(text)
    return text


def hide_share_labels(text):
    share_labels = {
        "LinkedIn": "Share on LinkedIn",
        "X": "Share on X",
        "Email": "Share by email",
    }

    def replace_label(match):
        label = match.group(2)
        return f'{match.group(1)}<span class="sr-only">{share_labels[label]}</span>{match.group(3)}'

    return re.sub(
        r'(<a\b(?=[^>]*class="[^"]*\bshare-link-social\b)(?=[^>]*(?:linkedin\.com|x\.com|twitter\.com|mailto:))[^>]*>)(LinkedIn|X|Email)(</a>)',
        replace_label,
        text,
    )


def update_article_share(text):
    text = re.sub(
        r'<section class="share-link-panel share-link-compact" aria-label="Share this page">[\s\S]*?</section>\s*',
        "",
        text,
    )
    text = re.sub(
        r'<button type="button" data-copy-share="https://parallaxdatalab\.com/insights/[^"]+/">Share Link</button>\s*',
        "",
        text,
    )
    text = re.sub(r'<p class="article-share-label">Share this article</p>\s*', "", text)
    text = re.sub(
        r'<a href="([^"]*linkedin\.com[^"]*)" target="_blank" rel="noopener noreferrer"><span class="sr-only">Share on LinkedIn</span></a>',
        r'<a href="\1" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"></a>',
        text,
    )
    text = re.sub(
        r'<a href="([^"]*x\.com[^"]*)" target="_blank" rel="noopener noreferrer"><span class="sr-only">Share on X</span></a>',
        r'<a href="\1" target="_blank" rel="noopener noreferrer" aria-label="X"></a>',
        text,
    )
    text = re.sub(
        r'<a href="(mailto:[^"]*)"><span class="sr-only">Share by email</span></a>',
        r'<a href="\1" aria-label="Email"></a>',
        text,
    )
    return text


def update_footer(text, prefix=""):
    def update_footer_nav(match):
        block = match.group(0)
        if f'href="{prefix}case-studies.html">Case Studies</a>' in block:
            return block
        return block.replace(
            f'<a href="{prefix}insights.html">Insights</a>',
            f'<a href="{prefix}insights.html">Insights</a>\n      <a href="{prefix}case-studies.html">Case Studies</a>',
        )

    return re.sub(
        r'<nav aria-label="Footer navigation" class="site-footer-col">[\s\S]*?</nav>',
        update_footer_nav,
        text,
        count=1,
    )


def update_share_js(text):
    text = text.replace('visibleLabel = isArticleShare ? "LinkedIn" : label;', 'visibleLabel = "";')
    text = text.replace('visibleLabel = isArticleShare ? "X" : label;', 'visibleLabel = "";')
    text = text.replace('visibleLabel = isArticleShare ? "Email" : label;', 'visibleLabel = "";')
    text = text.replace('anchor.innerHTML = `${icon}<span>${visibleLabel || label}</span>`;', 'anchor.innerHTML = `${icon}<span class="sr-only">${label}</span>`;')
    return text


def sync_clean_routes():
    from importlib.util import spec_from_file_location, module_from_spec
    spec = spec_from_file_location("syncer", ROOT / "tools" / "apply_sitewide_revisions.py")
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    for slug in mod.SYNC_PAGES:
        src = ROOT / f"{slug}.html"
        dest = ROOT / slug / "index.html"
        if src.exists():
            write(dest, mod.prefix_nested_paths(read(src)))
    for src in sorted((ROOT / "insights").glob("*.html")):
        if src.name == "index.html":
            continue
        dest = ROOT / "insights" / src.stem / "index.html"
        write(dest, mod.prefix_insight_clean_route(read(src)))


def main():
    for path in list(ROOT.rglob("*.html")):
        if ".git" in path.parts or "tools" in path.parts:
            continue
        text = read(path)
        prefix = page_prefix(path)
        text = update_nav(text, prefix)
        if path.name == "index.html" and path.parent == ROOT:
            text = update_home_main(text)
        if path.name == "case-studies.html" or (path.name == "index.html" and path.parent.name == "case-studies"):
            text = update_case_page(path, text)
        if path.name == "contact.html" or (path.name == "index.html" and path.parent.name == "contact"):
            text = update_contact(text, prefix)
        if path.name == "free-fit-check.html" or (path.name == "index.html" and path.parent.name == "free-fit-check"):
            text = update_fit_check(text, prefix)
        if path.parent.name == "insights" or (path.name == "index.html" and path.parent.parent.name == "insights"):
            text = update_article(text, path)
            text = update_article_share(text)
        if path.name == "insights.html" or (path.name == "index.html" and path.parent.name == "insights"):
            text = update_article_share(text)
        text = update_footer(text, prefix)
        text = hide_share_labels(text)
        text = re.sub(r"home\.css\?v=\d+", f"home.css?v={VERSION}", text)
        text = re.sub(r"home\.js\?v=\d+", f"home.js?v={VERSION}", text)
        write(path, text)

    js = read(ROOT / "home.js")
    write(ROOT / "home.js", update_share_js(js))
    css = read(ROOT / "home.css")
    append = """

/* Round 2: ribbon consistency, industry case studies, author chips, and embedded scheduling. */
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  overflow: hidden !important;
  clip: rect(0 0 0 0) !important;
  white-space: nowrap !important;
}

@media (hover: hover) and (pointer: fine) and (min-width: 921px) {
  .site-header .nav-dropdown-menu.nav-dropdown-menu-intelligence,
  .site-header .nav-dropdown-menu.nav-dropdown-menu-case-studies,
  .site-header .nav-dropdown-menu.nav-dropdown-menu-about {
    width: min(760px, calc(100vw - 32px)) !important;
    max-width: min(760px, calc(100vw - 32px)) !important;
    grid-template-columns: 1fr !important;
  }

  .site-header .nav-dropdown-menu.nav-dropdown-menu-intelligence .nav-menu-group,
  .site-header .nav-dropdown-menu.nav-dropdown-menu-case-studies .nav-menu-group,
  .site-header .nav-dropdown-menu.nav-dropdown-menu-about {
    display: grid !important;
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 8px !important;
    columns: auto !important;
  }

  .site-header .nav-dropdown-menu.nav-dropdown-menu-intelligence .nav-menu-section-title,
  .site-header .nav-dropdown-menu.nav-dropdown-menu-case-studies .nav-menu-section-title,
  .site-header .nav-dropdown-menu.nav-dropdown-menu-about .nav-menu-parent {
    grid-column: 1 / -1 !important;
  }
}

.case-study-grid article,
.case-study-grid article p,
.case-study-grid article dd,
.case-study-grid article h3 {
  color: #ffffff !important;
}

.case-study-grid article .secondary-action {
  color: #071029 !important;
  background: var(--accent-primary) !important;
}

.industry-case-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
}

.industry-case-card {
  display: grid;
  grid-template-rows: 168px auto 1fr auto;
  gap: 10px;
  min-height: 360px;
  padding: 14px;
  border: 1px solid rgba(125, 211, 252, 0.24);
  border-radius: 8px;
  background: rgba(7, 19, 58, 0.78);
  color: #ffffff;
  text-decoration: none;
}

.industry-case-card img,
.case-story-image {
  width: 100%;
  height: 100%;
  min-height: 0;
  object-fit: cover;
  border-radius: 8px;
}

.industry-case-card span {
  color: var(--gold);
  font-weight: 900;
}

.industry-case-card strong {
  color: #ffffff;
  line-height: 1.25;
}

.industry-case-card em {
  color: #9bdcff;
  font-style: normal;
  font-weight: 900;
}

.industry-case-story {
  display: grid;
  grid-template-columns: minmax(260px, 0.36fr) 1fr;
  gap: 24px;
  scroll-margin-top: 110px;
}

.case-story-image {
  height: 100%;
  min-height: 320px;
}

.article-meta-author {
  align-items: center;
}

.article-author-chip {
  display: inline-flex;
  align-items: center;
  gap: 9px;
}

.article-author-chip img {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  object-fit: cover;
  border: 2px solid rgba(245, 181, 68, 0.78);
}

.share-link-social.share-icon-link span:not(.sr-only) {
  display: none !important;
}

.share-icon-link .sr-only {
  position: absolute !important;
}

.calendly-section {
  display: grid;
  grid-template-columns: minmax(260px, 0.32fr) minmax(320px, 1fr);
  gap: 22px;
}

.calendly-section .calendly-fallback {
  grid-column: 2;
}

.calendly-inline-widget {
  width: 100%;
  min-height: 680px;
  overflow: hidden;
  border: 1px solid rgba(125, 211, 252, 0.24);
  border-radius: 8px;
  background: #ffffff;
}

@media (max-width: 980px) {
  .industry-case-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .industry-case-story,
  .calendly-section {
    grid-template-columns: 1fr;
  }

  .calendly-section .calendly-fallback {
    grid-column: auto;
  }
}

@media (max-width: 640px) {
  .industry-case-grid {
    grid-template-columns: 1fr;
  }
}
"""
    if "Round 2: ribbon consistency" not in css:
        write(ROOT / "home.css", css + append)
    sync_clean_routes()


if __name__ == "__main__":
    main()

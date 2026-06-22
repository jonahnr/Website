from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
VERSION = "180"
OLD_SLUG = "data-quality-review"
NEW_SLUG = "data-quality-analytics-reliability"
OLD_FILE = ROOT / f"{OLD_SLUG}.html"
NEW_FILE = ROOT / f"{NEW_SLUG}.html"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def page_prefix(path: Path) -> str:
    if path.parent.name == "insights" and path.suffix == ".html":
        return "../"
    if path.name == "index.html" and path.parent.parent.name == "insights":
        return "../../"
    if path.name == "index.html" and path.parent != ROOT:
        return "../"
    return ""


def prefix_nested_paths(text: str) -> str:
    spec_path = ROOT / "tools" / "apply_sitewide_revisions.py"
    import importlib.util

    spec = importlib.util.spec_from_file_location("sitewide", spec_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.prefix_nested_paths(text)


def hide_share_text(text: str) -> str:
    text = re.sub(r'<button type="button" data-native-share="[^"]+" data-share-title="[^"]+">Share Link</button>\s*', "", text)
    text = re.sub(r'<button type="button" data-copy-share="[^"]+">Copy</button>\s*', "", text)
    text = text.replace('<span class="share-link-label">Share</span>\n', "")
    text = text.replace('<span class="sr-only">Share on LinkedIn</span>', "")
    text = text.replace('<span class="sr-only">Share on X</span>', "")
    text = text.replace('<span class="sr-only">Share by email</span>', "")
    return text


def standardize_reliability_refs(text: str) -> str:
    text = text.replace("data-quality-review.html", f"{NEW_SLUG}.html")
    text = text.replace("/data-quality-review/", f"/{NEW_SLUG}/")
    text = text.replace("Data Quality & Reporting Reliability Consulting", "Data Quality & Analytics Reliability Consulting")
    text = text.replace("Data Quality & Reporting Reliability", "Data Quality & Analytics Reliability")
    text = text.replace("Data Quality Review", "Data Quality & Analytics Reliability")
    text = text.replace("data reliability, BI governance", "analytics reliability, BI governance")
    text = text.replace("data reliability breaks confidence", "analytics reliability breaks confidence")
    text = text.replace("data reliability, governance", "analytics reliability, governance")
    return text


def update_nav_footer_versions(text: str) -> str:
    text = re.sub(r"home\.css\?v=\d+", f"home.css?v={VERSION}", text)
    text = re.sub(r"home\.js\?v=\d+", f"home.js?v={VERSION}", text)
    return text


def replace_first_section_after(text: str, marker: str, section: str) -> str:
    if section.splitlines()[0] in text:
        return text
    idx = text.find(marker)
    if idx == -1:
        return text
    end = text.find("</section>", idx)
    if end == -1:
        return text
    end += len("</section>")
    return text[:end] + "\n" + section + text[end:]


def home_proof_strip() -> str:
    return """<section class="engagement-proof-strip" aria-label="Example engagement outcomes">
<p class="page-kicker">Example engagement outcomes</p>
<div class="engagement-proof-grid">
<article><strong>14 reports</strong><span>to 4 executive views</span></article>
<article><strong>5 KPIs</strong><span>to 5 accountable owners</span></article>
<article><strong>6 systems</strong><span>to 1 governed data path</span></article>
</div>
</section>"""


def founder_enterprise_panel() -> str:
    return """<section class="enterprise-credibility-panel reveal-card" aria-labelledby="enterprise-credibility-title">
<div>
<p class="page-kicker">Founder-led, enterprise-tested</p>
<h2 id="enterprise-credibility-title">Enterprise Analytics Experience, Delivered Through a Boutique Partnership</h2>
</div>
<div class="enterprise-credibility-grid">
<article><strong>5+ years</strong><span>delivering enterprise analytics solutions across manufacturing, healthcare, safety, operations, and SaaS</span></article>
<article><strong>100+ dashboards</strong><span>designed across executive, operational, and customer-facing use cases</span></article>
<article><strong>Millions to billions</strong><span>of records supported across modern cloud analytics environments</span></article>
<article><strong>Enterprise context</strong><span>supporting analytics initiatives for Fortune 500 organizations and global enterprises</span></article>
<article><strong>Hands-on depth</strong><span>Power BI, SQL, Python, cloud data warehouses, analytics governance, and AI readiness</span></article>
</div>
</section>"""


def update_home(text: str) -> str:
    hero_nav_match = re.search(r'<div class="hero-expertise-nav" aria-label="Explore expertise by reporting need">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>', text)
    if hero_nav_match:
        hero_nav = re.search(r'<div class="hero-expertise-nav" aria-label="Explore expertise by reporting need">[\s\S]*?</div>\s*</div>', hero_nav_match.group(0)).group(0)
        hero_nav = hero_nav.replace('href="data-quality-review.html"', f'href="{NEW_SLUG}.html"')
        hero_nav = hero_nav.replace("<strong>Reporting Reliability</strong>", "<strong>Analytics Reliability</strong>")
        hero_nav = hero_nav.replace("</div>\n</div>", "</div>")
        text = text[:hero_nav_match.start()] + text[hero_nav_match.start():hero_nav_match.end()].replace(hero_nav_match.group(0), "</div>\n</section>") + text[hero_nav_match.end():]
        if "reporting-needs-section" not in text:
            moved = hero_nav.replace("hero-expertise-nav", "hero-expertise-nav reporting-needs-section", 1)
            moved = moved.replace("Explore by reporting need", "Explore by Reporting Need")
            text = text.replace("</section>\n<section class=\"share-link-panel", "</section>\n" + home_proof_strip() + "\n" + moved + "\n<section class=\"share-link-panel", 1)

    text = text.replace('<a class="secondary-action" href="free-fit-check.html#what-you-get">See What Youâ€™ll Get</a>', '<a class="hero-text-link" href="free-fit-check.html#what-you-get">See What Youâ€™ll Get</a>')
    text = text.replace('<a class="secondary-action" href="free-fit-check.html#what-you-get">See What You’ll Get</a>', '<a class="hero-text-link" href="free-fit-check.html#what-you-get">See What You’ll Get</a>')
    text = text.replace("hero-fit-check\" aria-label", "hero-fit-check hero-fit-check-compact\" aria-label")
    text = text.replace('href="data-quality-review.html"', f'href="{NEW_SLUG}.html"')
    text = text.replace("Data Quality &amp; Reporting Reliability", "Data Quality &amp; Analytics Reliability")

    marker = "</section>\n<section class=\"failure-section"
    if "Enterprise Analytics Experience, Delivered Through a Boutique Partnership" not in text:
        text = text.replace(marker, "</section>\n" + founder_enterprise_panel() + "\n<section class=\"failure-section", 1)
    return text


def kpi_section() -> str:
    return """<section class="expertise-strategy-section reveal-card" aria-labelledby="metrics-management-title">
<p class="page-kicker">Executive KPI systems</p>
<h2 id="metrics-management-title">From Metrics to Management Systems</h2>
<p>Many organizations have dashboards filled with metrics but lack a consistent operating model for how those metrics are reviewed, interpreted, and acted upon.</p>
<p>Effective KPI reporting is not just about tracking numbers. It requires clear ownership, standardized definitions, meaningful targets, and a process for turning insights into action.</p>
<div class="expertise-use-case-grid compact-question-grid">
<article><h3>Performance</h3><p>Which metrics truly represent organizational performance?</p></article>
<article><h3>Ownership</h3><p>Who owns each KPI and is accountable for results?</p></article>
<article><h3>Attention</h3><p>When should leadership pay attention to a changing trend?</p></article>
<article><h3>Action</h3><p>What actions should follow when performance falls outside expectations?</p></article>
</div>
</section>"""


def automation_section() -> str:
    return """<section class="expertise-strategy-section reveal-card" aria-labelledby="automation-operations-title">
<p class="page-kicker">Operating improvement</p>
<h2 id="automation-operations-title">From Manual Reporting to Scalable Analytics Operations</h2>
<p>Many organizations rely on analysts to manually export data, update spreadsheets, reconcile numbers, and distribute recurring reports. These processes consume valuable time and create unnecessary risk.</p>
<p>Parallax Data Lab helps organizations automate reporting workflows to:</p>
<ul class="about-arrow-list">
<li>Reduce time spent on repetitive reporting tasks</li>
<li>Improve confidence and consistency in recurring reports</li>
<li>Deliver faster access to reliable business insights</li>
<li>Enable analytics teams to spend more time generating recommendations rather than preparing data</li>
</ul>
<p>Solutions may include automated data pipelines, cloud data platforms, Power BI refresh architecture, and streamlined report distribution processes.</p>
</section>"""


def cincinnati_section() -> str:
    return """<section class="local-seo-section local-industry-context reveal-card" aria-labelledby="cincinnati-industries-title">
<p class="page-kicker">Cincinnati business landscape</p>
<h2 id="cincinnati-industries-title">Supporting Cincinnati's Leading Industries With Modern Analytics</h2>
<p>Cincinnati is home to some of the world's most recognized organizations across consumer products, manufacturing, logistics, healthcare, insurance, and technology.</p>
<p>From the operational complexity of manufacturers like GE Aerospace and Cintas, to the data-driven environments of organizations like Kroger, Procter &amp; Gamble, Total Quality Logistics, Fifth Third Bank, Cincinnati Children's, TriHealth, Mercy Health, Western &amp; Southern, and Great American Insurance Group, modern organizations depend on trusted analytics to make informed decisions.</p>
<p>Parallax Data Lab brings enterprise-level analytics expertise to Cincinnati organizations seeking to improve reporting, strengthen data trust, modernize business intelligence, and prepare their data foundation for AI-enabled decision making.</p>
</section>"""


def about_partner_section() -> str:
    return """<section class="about-founder-partnership reveal-card" aria-labelledby="founder-partnership-title">
<p class="page-kicker">Direct founder partnership</p>
<h2 id="founder-partnership-title">Your Analytics Partner From Strategy Through Execution</h2>
<p>Many organizations face a gap between high-level analytics strategy and the technical work required to make it successful.</p>
<p>With Parallax Data Lab, organizations work directly with founder Jonah Robinson, an analytics professional who combines strategic business understanding with hands-on expertise in data modeling, business intelligence, automation, governance, and modern cloud analytics.</p>
<p>Whether establishing executive KPI frameworks, improving trust in existing dashboards, automating reporting workflows, or preparing a foundation for AI, clients receive direct partnership from a senior analytics leader from discovery through implementation.</p>
</section>"""


def about_credibility_panel() -> str:
    return """<section class="about-founder-proof reveal-card" aria-labelledby="about-founder-proof-title">
<p class="page-kicker">Founder credibility</p>
<h2 id="about-founder-proof-title">Senior analytics experience, applied directly to the work.</h2>
<div class="enterprise-credibility-grid">
<article><strong>5+ years</strong><span>delivering enterprise analytics solutions</span></article>
<article><strong>100+ dashboards</strong><span>designed across executive, operational, and customer-facing use cases</span></article>
<article><strong>Millions to billions</strong><span>of records supported across analytics environments</span></article>
<article><strong>Domain range</strong><span>manufacturing, healthcare, safety, operations, and SaaS</span></article>
<article><strong>Hands-on tools</strong><span>Power BI, SQL, Python, cloud data platforms, governance, and AI readiness</span></article>
</div>
</section>"""


def update_about(text: str) -> str:
    if "about-founder-proof-title" not in text:
        text = text.replace("</section>\n<section class=\"about-proof-layer", "</section>\n" + about_credibility_panel() + "\n" + about_partner_section() + "\n<section class=\"about-proof-layer", 1)
    return text


def reliability_page(text: str) -> str:
    text = standardize_reliability_refs(text)
    text = text.replace("https://parallaxdatalab.com/data-quality-review/", f"https://parallaxdatalab.com/{NEW_SLUG}/")
    text = text.replace("Data quality and reporting reliability consulting for inconsistent metrics, source system issues, manual reporting patches, reconciliation work, and dashboard trust problems.", "Data quality and analytics reliability consulting for trusted reporting environments, consistent metrics, reliable refreshes, governance gaps, and dashboard confidence.")
    text = text.replace('"serviceType": "Data Quality & Analytics Reliability"', '"serviceType": "Data Quality & Analytics Reliability Consulting"')
    text = text.replace("<p class=\"page-kicker\">Data Quality & Analytics Reliability</p>\n<h1 id=\"expertise-title\">Data quality review for teams tired of reconciling conflicting numbers.</h1>\n<p>Data quality problems show up as reporting problems: dashboards do not match, leaders question the numbers, teams keep offline spreadsheets, and analysts spend too much time explaining exceptions. Parallax Data Lab reviews the path from source systems to reporting outputs so teams can find where trust is breaking and what needs to be fixed first.</p>", "<p class=\"page-kicker\">Data Quality & Analytics Reliability</p>\n<h1 id=\"expertise-title\">Data Quality & Analytics Reliability Consulting</h1>\n<p>Data quality is not just a technical issue. It is a business reliability issue. When leaders question which number is right, whether a dashboard refreshed, or whether definitions changed, analytics loses credibility.</p>\n<p>Parallax Data Lab helps organizations improve the reliability of their analytics environment by identifying reporting risks, inconsistent definitions, data quality gaps, and governance issues that reduce confidence in decision-making.</p>")
    text = text.replace("Trust Review", "Reliability Review")
    text = text.replace("Data quality review tracing conflicting source systems into trusted reporting", "Data quality and analytics reliability consulting tracing source systems into trusted reporting")
    text = text.replace("data-quality-review/", f"{NEW_SLUG}/")
    text = text.replace("data-quality-review", NEW_SLUG)
    return text


def update_sitemap(text: str) -> str:
    text = text.replace("https://parallaxdatalab.com/data-quality-review/", f"https://parallaxdatalab.com/{NEW_SLUG}/")
    text = text.replace('  <url><loc>https://parallaxdatalab.com/insights/index/</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>\n', "")
    return text


def update_redirects(text: str) -> str:
    text = text.replace("/data-quality-review /data-quality-review/ 301", f"/data-quality-review /{NEW_SLUG}/ 301")
    text = text.replace("/data-quality-review.html /data-quality-review/ 301", f"/data-quality-review.html /{NEW_SLUG}/ 301")
    if f"/{NEW_SLUG} /{NEW_SLUG}/ 301" not in text:
        text += f"\n/{NEW_SLUG} /{NEW_SLUG}/ 301\n/{NEW_SLUG}.html /{NEW_SLUG}/ 301\n"
    return text


def update_page(path: Path, text: str) -> str:
    prefix = page_prefix(path)
    text = standardize_reliability_refs(text)
    text = hide_share_text(text)
    text = update_nav_footer_versions(text)
    if path.name == "index.html" and path.parent == ROOT:
        text = update_home(text)
    if path.name == "about.html" or (path.name == "index.html" and path.parent.name == "about"):
        text = update_about(text)
    if path.name == "kpi-reporting-consulting.html" or (path.name == "index.html" and path.parent.name == "kpi-reporting-consulting"):
        text = replace_first_section_after(text, '<section class="expertise-hero"', kpi_section())
    if path.name == "reporting-automation-consulting.html" or (path.name == "index.html" and path.parent.name == "reporting-automation-consulting"):
        text = replace_first_section_after(text, '<section class="expertise-hero"', automation_section())
    if path.name == "business-intelligence-consultant-cincinnati.html" or (path.name == "index.html" and path.parent.name == "business-intelligence-consultant-cincinnati"):
        text = replace_first_section_after(text, '<section class="local-seo-hero"', cincinnati_section())
    return text


def main():
    old_text = read(OLD_FILE) if OLD_FILE.exists() else read(NEW_FILE)
    write(NEW_FILE, reliability_page(old_text))
    write(ROOT / NEW_SLUG / "index.html", prefix_nested_paths(read(NEW_FILE)))

    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts or "tools" in path.parts:
            continue
        if path == OLD_FILE or path == ROOT / OLD_SLUG / "index.html":
            continue
        text = update_page(path, read(path))
        write(path, text)

    css = read(ROOT / "home.css")
    if "Enterprise positioning revision styles" not in css:
        css += """

/* Enterprise positioning revision styles. */
.hero-fit-check-compact {
  padding: clamp(16px, 2vw, 22px) !important;
  gap: 14px !important;
}

.hero-text-link {
  color: #9bdcff;
  font-weight: 850;
  text-decoration: none;
  align-self: center;
}

.hero-text-link:hover,
.hero-text-link:focus-visible {
  color: var(--gold);
}

.engagement-proof-strip,
.reporting-needs-section,
.enterprise-credibility-panel,
.expertise-strategy-section,
.about-founder-proof,
.about-founder-partnership,
.local-industry-context {
  width: min(1120px, calc(100% - 32px));
  margin: 28px auto;
  padding: clamp(22px, 4vw, 36px);
  border: 1px solid rgba(125, 211, 252, 0.22);
  border-radius: 8px;
  background: rgba(7, 19, 58, 0.82);
  box-shadow: 0 22px 60px rgba(0, 0, 0, 0.22);
}

.reporting-needs-section {
  background: rgba(8, 28, 72, 0.94);
}

.engagement-proof-grid,
.enterprise-credibility-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.enterprise-credibility-grid {
  grid-template-columns: repeat(5, minmax(0, 1fr));
}

.engagement-proof-grid article,
.enterprise-credibility-grid article {
  padding: 16px;
  border: 1px solid rgba(69, 190, 255, 0.22);
  border-radius: 8px;
  background: rgba(5, 14, 42, 0.58);
}

.engagement-proof-grid strong,
.enterprise-credibility-grid strong {
  display: block;
  color: var(--gold);
  font-size: clamp(1.25rem, 2vw, 1.7rem);
}

.engagement-proof-grid span,
.enterprise-credibility-grid span {
  color: #d8e9ff;
}

.compact-question-grid {
  margin-top: 18px;
}

@media (max-width: 980px) {
  .engagement-proof-grid,
  .enterprise-credibility-grid {
    grid-template-columns: 1fr;
  }

  .hero-fit-check-compact .hero-actions {
    align-items: stretch;
  }
}
"""
    css = re.sub(r"home\.css\?v=\d+", f"home.css?v={VERSION}", css)
    write(ROOT / "home.css", css)

    js = read(ROOT / "home.js")
    js = js.replace('label = "Share on LinkedIn";', 'label = "LinkedIn";')
    js = js.replace('label = "Share on X";', 'label = "X";')
    js = js.replace('label = "Share by email";', 'label = "Email";')
    write(ROOT / "home.js", js)

    write(ROOT / "sitemap.xml", update_sitemap(read(ROOT / "sitemap.xml")))
    write(ROOT / "_redirects", update_redirects(read(ROOT / "_redirects")))

    if OLD_FILE.exists():
        OLD_FILE.unlink()
    old_dir = ROOT / OLD_SLUG
    if old_dir.exists():
        shutil.rmtree(old_dir)


if __name__ == "__main__":
    main()

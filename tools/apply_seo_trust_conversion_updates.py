from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "138"
SITE = "https://parallaxdatalab.com"

try:
    from apply_faq_scorecard_cleanup import deliverable_copy as DELIVERABLE_COPY
except Exception:
    DELIVERABLE_COPY = {}


SOCIAL_PAGES = {
    "index.html": ("Parallax Data Lab", "Business intelligence consulting for clearer dashboards, trusted KPIs, and decision-ready reporting.", "assets/social/home-social.jpg"),
    "our-offerings.html": ("Analytics Consulting Offerings", "Choose the right path from scorecard to diagnostic, reset, stewardship, or advanced intelligence.", "assets/social/offerings-social.jpg"),
    "expertise.html": ("Analytics Expertise", "Power BI, KPI reporting, automation, data quality, governance, and Cincinnati analytics consulting.", "assets/social/expertise-social.jpg"),
    "power-bi-consultant-cincinnati.html": ("Power BI Consulting", "Deep Power BI consulting for dashboards, DAX, semantic models, KPI reporting, RLS, and refresh reliability.", "assets/social/power-bi-social.jpg"),
    "business-intelligence-consultant-cincinnati.html": ("Data Analytics Consulting Cincinnati", "Local Cincinnati and Midwest analytics support for KPI reporting, Power BI, operations, and trusted BI systems.", "assets/social/cincinnati-social.jpg"),
    "kpi-reporting-consulting.html": ("KPI Reporting Consulting", "Metric definitions, owners, thresholds, executive cadence, and scorecards leaders can actually use.", "assets/social/kpi-social.jpg"),
    "reporting-automation-consulting.html": ("Reporting Automation Consulting", "Automate recurring reporting without scaling bad logic, hidden patches, or unclear definitions.", "assets/social/automation-social.jpg"),
    "data-quality-review.html": ("Data Quality Review", "Trace source issues, exceptions, manual patches, and metric drift so leaders can trust the number.", "assets/social/data-quality-social.jpg"),
    "dashboard-trust-governance.html": ("Dashboard Trust & BI Governance", "Certified metrics, report inventory, RLS, workspace structure, access rules, and change control.", "assets/social/governance-social.jpg"),
    "insights.html": ("Business Intelligence Insights", "Executive articles on dashboard trust, KPI governance, analytics operations, AI readiness, and decision systems.", "assets/social/insights-social.jpg"),
}

MIRRORS = {
    "index.html": [],
    **{name: [str(Path(name).with_suffix("") / "index.html")] for name in SOCIAL_PAGES if name != "index.html"},
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def href_prefix(path: Path) -> str:
    rel = Path(".") if path.parent == ROOT else path.parent.relative_to(ROOT)
    depth = 0 if str(rel) == "." else len(rel.parts)
    return "../" * depth


def page_slug(path: Path) -> str:
    if path.name == "index.html" and path.parent == ROOT:
        return ""
    if path.name == "index.html":
        return path.parent.name
    return path.stem


def canonical_for(path: Path) -> str:
    slug = page_slug(path)
    return f"{SITE}/" if not slug else f"{SITE}/{slug}/"


def social_url(asset: str) -> str:
    return f"{SITE}/{asset}"


def generate_social_images() -> None:
    from PIL import Image, ImageDraw, ImageFont

    out_dir = ROOT / "assets" / "social"
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 58)
        subtitle_font = ImageFont.truetype("arial.ttf", 30)
        small_font = ImageFont.truetype("arialbd.ttf", 24)
    except OSError:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    for _, (title, subtitle, asset) in SOCIAL_PAGES.items():
        img = Image.new("RGB", (1200, 630), "#061431")
        draw = ImageDraw.Draw(img)
        for y in range(630):
            shade = int(12 + (y / 630) * 22)
            draw.line((0, y, 1200, y), fill=(4, shade, 48))
        draw.rectangle((0, 0, 1200, 630), outline=(44, 190, 255), width=3)
        draw.line((70, 114, 1130, 114), fill=(245, 181, 68), width=4)
        draw.line((70, 516, 1130, 516), fill=(44, 190, 255), width=2)
        for x in range(80, 1120, 60):
            draw.line((x, 140, x + 120, 490), fill=(18, 84, 150), width=1)
        draw.text((78, 58), "PARALLAX DATA LAB", fill=(245, 213, 140), font=small_font)

        words = title.split()
        lines = []
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if draw.textbbox((0, 0), test, font=title_font)[2] > 940 and line:
                lines.append(line)
                line = word
            else:
                line = test
        if line:
            lines.append(line)
        y = 190
        for line in lines[:3]:
            draw.text((78, y), line, fill=(255, 255, 255), font=title_font)
            y += 70

        sub_lines = []
        line = ""
        for word in subtitle.split():
            test = f"{line} {word}".strip()
            if draw.textbbox((0, 0), test, font=subtitle_font)[2] > 980 and line:
                sub_lines.append(line)
                line = word
            else:
                line = test
        if line:
            sub_lines.append(line)
        y += 8
        for line in sub_lines[:3]:
            draw.text((82, y), line, fill=(221, 238, 255), font=subtitle_font)
            y += 42

        draw.rounded_rectangle((78, 464, 470, 516), radius=26, fill=(245, 181, 68))
        draw.text((105, 478), "parallaxdatalab.com", fill=(5, 9, 22), font=small_font)
        out = ROOT / asset
        img.save(out, "JPEG", quality=86, optimize=True, progressive=True)


def set_social_meta(text: str, asset: str) -> str:
    img = social_url(asset)
    text = re.sub(r'(<meta\s+property="og:image"\s+content=")[^"]+(")', rf"\1{img}\2", text)
    text = re.sub(r'(<meta\s+name="twitter:image"\s+content=")[^"]+(")', rf"\1{img}\2", text)
    return text


def share_block(path: Path, title: str, asset: str) -> str:
    url = canonical_for(path)
    return f'''<section class="share-link-panel reveal-card" aria-label="Share this page">
<div>
<p class="page-kicker">Shareable Link</p>
<h2>Share {title}</h2>
<p>Copy the direct link below for LinkedIn posts, email follow-ups, proposals, or internal Slack and Teams threads.</p>
</div>
<div class="share-link-control">
<input type="text" readonly value="{url}" aria-label="Direct share link for {title}"/>
<button type="button" data-copy-share="{url}">Copy Link</button>
</div>
<a class="share-link-social" href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener noreferrer">Share on LinkedIn</a>
</section>'''


def insert_after_first_section(text: str, block: str, marker: str) -> str:
    if marker in text:
        return text
    match = re.search(r"</section>", text)
    if not match:
        return text
    return text[: match.end()] + "\n" + block + text[match.end():]


def json_ld_for(path: Path, title: str, desc: str) -> str:
    slug = page_slug(path)
    payload = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "name": "Parallax Data Lab",
        "url": canonical_for(path),
        "description": desc,
        "founder": {"@type": "Person", "name": "Jonah Rosenthal"},
        "areaServed": [
            {"@type": "City", "name": "Cincinnati"},
            {"@type": "State", "name": "Ohio"},
            {"@type": "Country", "name": "United States"},
        ],
        "address": {"@type": "PostalAddress", "addressLocality": "Cincinnati", "addressRegion": "OH", "addressCountry": "US"},
        "knowsAbout": [
            "Power BI consulting",
            "Business intelligence consulting",
            "Data analytics consulting",
            "KPI reporting",
            "Reporting automation",
            "Data quality review",
            "Dashboard trust",
            "BI governance",
        ],
        "sameAs": [
            "https://www.linkedin.com/company/129543938/admin/dashboard/",
            "https://www.youtube.com/@ParallaxDataLab",
            "https://www.instagram.com/parallaxdatalab/",
            "https://x.com/parallaxdatalab",
        ],
    }
    if slug:
        payload["serviceType"] = title
    return '<script type="application/ld+json">' + json.dumps(payload, indent=2) + "</script>"


def replace_json_ld(text: str, path: Path, title: str, desc: str) -> str:
    block = json_ld_for(path, title, desc)
    if '<script type="application/ld+json">' in text:
        return re.sub(r'<script type="application/ld\+json">.*?</script>', block, text, count=1, flags=re.S)
    return text.replace("</head>", block + "\n</head>", 1)


def local_proof_section(prefix: str) -> str:
    return f'''<section class="local-trust-section reveal-card" aria-labelledby="local-proof-title">
<p class="page-kicker">Cincinnati proof and service area</p>
<h2 id="local-proof-title">Local analytics consulting for Cincinnati teams and Midwest operating environments.</h2>
<p>Parallax Data Lab is based in Cincinnati and works with teams across Ohio, Northern Kentucky, and the broader Midwest. The local advantage is practical context: how leaders review operating numbers, how manufacturing and service teams define performance, and how fast reporting has to move when customer commitments, labor, cash, inventory, quality, and margin are all connected.</p>
<div class="local-trust-grid">
<article><strong>Service area</strong><p>Cincinnati, Northern Kentucky, Dayton, Columbus, Louisville, Indianapolis, and remote teams across the United States.</p></article>
<article><strong>Industries served</strong><p>Manufacturing, healthcare, retail, marketing, construction, energy, logistics, professional services, distribution, and growing mid-market operators.</p></article>
<article><strong>Founder context</strong><p>Jonah brings more than 10 years in Cincinnati and deep hands-on Power BI experience across dashboard development, DAX, semantic models, RLS, refresh reliability, reporting cleanup, KPI governance, and executive analytics workflows.</p></article>
</div>
</section>'''


def powerbi_proof_section() -> str:
    return '''<section class="local-trust-section reveal-card" aria-labelledby="power-bi-proof-title">
<p class="page-kicker">Power BI depth</p>
<h2 id="power-bi-proof-title">Power BI experience beyond dashboard cosmetics.</h2>
<p>Parallax Data Lab supports Power BI work at the level where trust is usually won or lost: DAX measures, semantic models, role-level security, refresh dependencies, workspace structure, certified datasets, KPI definitions, data quality checks, and the operating cadence that determines whether leaders actually use the report.</p>
<div class="local-trust-grid">
<article><strong>Model and DAX cleanup</strong><p>Reduce duplicated measures, clarify grain, simplify relationships, separate certified metrics from exploration, and make calculations easier to explain.</p></article>
<article><strong>Reporting operations</strong><p>Improve refresh reliability, source timing, exception handling, access rules, and report ownership so dashboards do not quietly drift.</p></article>
<article><strong>Industry examples</strong><p>Power BI reporting can support healthcare utilization, retail performance, marketing funnel reporting, construction project controls, manufacturing quality and throughput, energy operations, and executive KPI scorecards.</p></article>
</div>
</section>'''


def deliverable_section(page: str) -> str:
    content = {
        "analytics-health-check": ("What the diagnostic produces", ["Dashboard trust map", "Metric ownership gaps", "Source and refresh risk list", "Prioritized next-step recommendation"]),
        "decision-system-reset": ("What the reset produces", ["Certified metric map", "Decision cadence design", "Owner and threshold model", "Report retirement and rebuild plan"]),
        "power-bi-consultant-cincinnati": ("What Power BI work can produce", ["Model and DAX review notes", "Dashboard cleanup plan", "Refresh and RLS checklist", "Embedded report readiness plan"]),
        "business-intelligence-consultant-cincinnati": ("What local analytics consulting can produce", ["Local operating metric map", "Industry-specific reporting examples", "Dashboard trust findings", "Cincinnati analytics next-step plan"]),
        "data-quality-review": ("What the review produces", ["Source trace map", "Exception register", "Trust break priority list", "Ownership recommendations"]),
        "reporting-automation-consulting": ("What automation work produces", ["Manual step inventory", "Automation readiness score", "Refresh dependency map", "Exception handling rules"]),
        "kpi-reporting-consulting": ("What KPI reporting work produces", ["Metric definition cards", "Owner map", "Executive scorecard outline", "Threshold and cadence recommendations"]),
        "dashboard-trust-governance": ("What governance work produces", ["Report inventory", "Certified metric process", "Access and RLS review", "Change control model"]),
    }.get(page)
    if not content:
        return ""
    heading, items = content
    cards = "\n".join(
        f"<article><strong>{item}</strong><p>{DELIVERABLE_COPY.get(item, 'A focused artifact with the owner, decision use, evidence, and next step documented clearly enough for the team to maintain after the engagement.')}</p></article>"
        for item in items
    )
    return f'''<section class="deliverable-proof-section reveal-card" aria-labelledby="{page}-deliverables-title">
<p class="page-kicker">What you get</p>
<h2 id="{page}-deliverables-title">{heading}</h2>
<div class="deliverable-proof-grid">
{cards}
</div>
</section>'''


def apply_page_updates(path: Path) -> None:
    if not path.exists():
        return
    text = read(path)
    original = text
    root_name = path.name if path.parent == ROOT else f"{path.parent.name}.html"
    prefix = href_prefix(path)

    text = re.sub(r"home\.css\?v=\d+", f"home.css?v={VERSION}", text)
    text = re.sub(r"home\.js\?v=\d+", f"home.js?v={VERSION}", text)

    if root_name in SOCIAL_PAGES:
        title, desc, asset = SOCIAL_PAGES[root_name]
        text = set_social_meta(text, asset)
        text = insert_after_first_section(text, share_block(path, title, asset), "share-link-panel")
        text = replace_json_ld(text, path, title, desc)

    slug = page_slug(path)
    if slug == "business-intelligence-consultant-cincinnati":
        text = insert_after_first_section(text, local_proof_section(prefix), "local-proof-title")
    if slug == "power-bi-consultant-cincinnati":
        text = insert_after_first_section(text, powerbi_proof_section(), "power-bi-proof-title")
    if slug == "about":
        text = insert_after_first_section(text, local_proof_section(prefix), "local-proof-title")

    deliverable = deliverable_section(slug)
    if deliverable and "deliverable-proof-section" not in text:
        inserted = False
        for target in (
            '<section class="local-seo-cta reveal-card"',
            '<section class="expertise-faq-section reveal-card"',
            '<section class="assessment-form-section assessment-form-refined reveal-card"',
        ):
            if target in text:
                text = text.replace(target, deliverable + "\n" + target, 1)
                inserted = True
                break
        if not inserted:
            text = text.replace("</main>", deliverable + "\n</main>", 1)

    if slug == "dashboard-trust-scorecard":
        text = text.replace('data-scorecard-delivery="direct"', 'data-scorecard-delivery="formsubmit" data-scorecard-archive="true" data-local-mail-subject="Dashboard Trust Scorecard Request"')
        if 'name="Submitted From"' not in text:
            text = text.replace('<input name="_next"', '<input name="Submitted From" type="hidden" value="Dashboard Trust Scorecard"/>\n<input name="_next"', 1)
        if "scorecard-archive-note" not in text:
            note = '''<p class="scorecard-archive-note">Submissions are emailed through FormSubmit on the hosted site. A browser-side CSV backup is also stored after submit so you can download a local archive from the scorecard page if needed.</p>'''
            text = text.replace("</form>", note + "\n</form>", 1)

    if slug in {"dashboard-trust-scorecard-download", "scorecard-thank-you"} and "scorecard-submission-export" not in text:
        export_block = '''<section class="scorecard-submission-export reveal-card" aria-labelledby="scorecard-submission-export-title">
<p class="page-kicker">Submission archive</p>
<h2 id="scorecard-submission-export-title">Download scorecard submission backup</h2>
<p>If this browser has recent scorecard requests saved locally, download a CSV copy for the submissions directory.</p>
<button type="button" data-download-scorecard-submissions>Download CSV Backup</button>
</section>'''
        text = text.replace("</main>", export_block + "\n</main>", 1)

    if text != original:
        write(path, text)


def update_insight_article(path: Path) -> None:
    text = read(path)
    original = text
    if "article-breadcrumbs" not in text:
        text = text.replace('<a class="article-back-link"', '<nav class="article-breadcrumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a><span>/</span><a href="../insights.html">Insights</a><span>/</span><span>Article</span></nav>\n<a class="article-back-link"', 1)
    if "data-copy-share=" not in text:
        canonical = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        url = canonical.group(1) if canonical else SITE
        text = text.replace('<a href="https://www.linkedin.com/sharing/share-offsite/?url=', f'<button type="button" data-copy-share="{url}">Copy Link</button>\n<a href="https://www.linkedin.com/sharing/share-offsite/?url=', 1)
    if "article-service-cta-block" not in text:
        cta = '''<section class="article-service-cta-block">
<p class="page-kicker">Turn the idea into action</p>
<h2>Use the right Parallax path for this reporting problem.</h2>
<p>Articles are useful when they clarify the issue. The next step is deciding whether the problem needs a Fit Check, a diagnostic, a Decision System Reset, Power BI support, data quality review, or governance work.</p>
<div>
<a class="primary-action" href="../free-fit-check.html">Request the Fit Check</a>
<a class="secondary-action" href="../expertise.html">Explore Expertise</a>
</div>
</section>'''
        text = text.replace('<p class="article-return-link">', cta + '\n<p class="article-return-link">', 1)
    text = re.sub(r"home\.css\?v=\d+", f"home.css?v={VERSION}", text)
    text = re.sub(r"home\.js\?v=\d+", f"home.js?v={VERSION}", text)
    if text != original:
        write(path, text)


def write_scorecard_submission_templates() -> None:
    folder = ROOT / "scorecard-submissions"
    folder.mkdir(exist_ok=True)
    csv_path = folder / "submissions.csv"
    if not csv_path.exists():
        with csv_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["submitted_at", "name", "work_email", "weakest_dimension", "additional_context", "source"])
    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(
            "# Scorecard submissions\n\n"
            "This folder is for exported Dashboard Trust Scorecard submissions.\n\n"
            "Because the marketing site is static, browser submissions cannot write directly into this repository at runtime. "
            "The hosted form sends email through FormSubmit, and the page also stores a browser-side CSV backup that can be downloaded from the thank-you or scorecard pages and archived here.\n",
            encoding="utf-8",
        )


def main() -> None:
    generate_social_images()
    for root_name, mirrors in MIRRORS.items():
        apply_page_updates(ROOT / root_name)
        for mirror in mirrors:
            apply_page_updates(ROOT / mirror)
    for page in [
        "analytics-health-check.html",
        "decision-system-reset.html",
        "dashboard-trust-scorecard.html",
        "dashboard-trust-scorecard-download.html",
        "scorecard-thank-you.html",
    ]:
        apply_page_updates(ROOT / page)
        mirror = ROOT / Path(page).with_suffix("") / "index.html"
        apply_page_updates(mirror)
    for article in (ROOT / "insights").glob("*.html"):
        if article.name != "index.html":
            update_insight_article(article)
    write_scorecard_submission_templates()


if __name__ == "__main__":
    main()

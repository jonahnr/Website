from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


FAQ_SECTION = """<section class="faq-section reveal-card">
<p class="page-kicker">FAQ</p>
<h2>Business intelligence consulting questions</h2>
<div class="faq-grid">
<article><h3>What does a business intelligence consultant do?</h3><p>A BI consultant helps teams define KPIs, clean up reporting logic, build dashboards, automate recurring reports, and make business data easier to trust.</p></article>
<article><h3>Can you help improve an existing Power BI dashboard?</h3><p>Yes. Parallax can simplify Power BI reports, improve usability, clarify metrics, and connect dashboards to the business questions leaders actually ask.</p></article>
<article><h3>What if our reporting is mostly spreadsheets today?</h3><p>That is common. The work usually starts by identifying repeated manual reporting, fragile spreadsheet logic, and the best path from spreadsheet to dashboard.</p></article>
<article><h3>Do we need a data warehouse before improving dashboards?</h3><p>No. Some teams need a stronger data foundation first, but many dashboard and reporting improvements can begin with the systems already in place.</p></article>
<article><h3>How does the Fit Check work?</h3><p>You share the reporting friction, then schedule a 1:1 review to discuss dashboard gaps, KPI visibility, and the highest-value next steps.</p></article>
</div>
</section>"""


def tighten_home(path: Path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'<script type="application/ld\+json" id="homepage-faq-schema">.*?</script>', "", text, flags=re.S)
    faq_match = re.search(r'<section class="faq-section reveal-card">.*?</section>\s*', text, flags=re.S)
    if faq_match:
        text = text[:faq_match.start()] + text[faq_match.end():]
    concrete_match = re.search(r'<section class="concrete-proof-section reveal-card">.*?</section>\s*', text, flags=re.S)
    work_match = re.search(r'<section class="work-section" id="services">', text)
    if concrete_match and work_match and concrete_match.start() > work_match.start():
        concrete = concrete_match.group(0)
        text = text[:concrete_match.start()] + text[concrete_match.end():]
        work_match = re.search(r'<section class="work-section" id="services">', text)
        text = text[:work_match.start()] + concrete + text[work_match.start():]
    path.write_text(text, encoding="utf-8", newline="\n")


def add_services_faq(path: Path):
    text = path.read_text(encoding="utf-8")
    if "Business intelligence consulting questions" not in text:
        text = text.replace('<section aria-labelledby="scorecard-lead-title"', FAQ_SECTION + '\n<section aria-labelledby="scorecard-lead-title"', 1)
    path.write_text(text, encoding="utf-8", newline="\n")


tighten_home(ROOT / "index.html")
for service_page in [ROOT / "our-offerings.html", ROOT / "our-offerings" / "index.html"]:
    add_services_faq(service_page)

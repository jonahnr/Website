from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Missing marker: {label}")
    return text.replace(old, new, 1)


def article_to_details(match: re.Match) -> str:
    question = match.group(1).strip()
    answer = match.group(2).strip()
    return f"<details><summary>{question}</summary><p>{answer}</p></details>"


def convert_faq_grids(text: str) -> str:
    def convert_grid(match: re.Match) -> str:
        body = re.sub(r"<article><h3>(.*?)</h3><p>(.*?)</p></article>", article_to_details, match.group(1), flags=re.S)
        return f'<div class="local-seo-faq-grid">\n{body}\n</div>'

    return re.sub(r'<div class="local-seo-faq-grid">\s*(.*?)\s*</div>', convert_grid, text, flags=re.S)


def ensure_minimum_faqs(text: str) -> str:
    def add_if_needed(match: re.Match) -> str:
        body = match.group(1)
        count = body.count("<details>")
        if count >= 4:
            return match.group(0)
        needed = 4 - count
        additions = []
        for _ in range(needed):
            additions.append(
                "<details><summary>What should we bring into the first conversation?</summary>"
                "<p>Bring the report, metric, manual workflow, or decision meeting where the issue shows up most clearly. A concrete example makes it easier to separate a dashboard problem from a definition, source, ownership, or cadence problem.</p></details>"
            )
        return f'<div class="local-seo-faq-grid">\n{body}\n' + "\n".join(additions) + "\n</div>"

    return re.sub(r'<div class="local-seo-faq-grid">\s*(.*?)\s*</div>', add_if_needed, text, flags=re.S)


def update_scorecard_page(text: str) -> str:
    text = text.replace(
        "<p data-lead-score-copy>The working copy will turn your lowest dimension into a printable diagnostic snapshot, evidence prompts, and a recommended next step.</p>",
        "<p data-lead-score-copy>The working copy will combine your scores into a pattern preview, diagnostic snapshot, evidence prompts, and recommended next step.</p>",
    )
    text = text.replace(
        "<div><dt>Lowest dimension</dt><dd data-lead-score-lowest>Not scored yet</dd></div>",
        "<div><dt>Pattern preview</dt><dd data-lead-score-lowest>Not scored yet</dd></div>",
    )
    text = text.replace(
        "After you score the five dimensions, submit the form to open the working scorecard, send the request through the backend, and preserve the lowest trust break for the final guidance. The email gate comes after the quick diagnostic so the page gives value first.",
        "After you score the five dimensions, submit the form to open the working scorecard and carry your scoring pattern into the final guidance. The email gate comes after the quick diagnostic so the page gives value first.",
    )
    text = text.replace(
        '<p class="scorecard-archive-note">Submissions are sent through the Parallax backend and the next screen opens immediately. A local CSV backup is also stored in this browser for your records.</p>\n',
        "",
    )
    return text


analytics_sample_new = """<section class="sample-output-deep-section reveal-card" aria-labelledby="health-sample-output-title">
<p class="page-kicker">Sample diagnostic output</p>
<h2 id="health-sample-output-title">A Health Check readout should make the next decision obvious.</h2>
<p>The paid diagnostic is not a generic audit. It produces a practical readout leaders can use to decide whether the next move is cleanup, governance, a reset, automation, or no engagement.</p>
<div class="sample-output-board">
<article><span>01</span><h3>Dashboard trust breakdown</h3><p>Ranks the reports creating the most decision friction, names the disputed metrics, and separates cosmetic dashboard issues from definition, source, and ownership problems.</p><strong>Sample finding: executive margin and shipped revenue are both visible, but neither has an agreed decision owner.</strong></article>
<article><span>02</span><h3>KPI ownership gaps</h3><p>Maps each priority metric to business owner, logic owner, source owner, decision cadence, and change-control path so debates have somewhere to land.</p><strong>Sample finding: sales, finance, and operations each maintain a different version of backlog.</strong></article>
<article><span>03</span><h3>Source reliability issues</h3><p>Traces weak signals through source systems, exports, manual adjustments, refresh timing, semantic logic, and side spreadsheets.</p><strong>Sample finding: a weekly export is treated as system truth even though late adjustments are made manually.</strong></article>
<article><span>04</span><h3>Decision cadence risks</h3><p>Identifies which dashboards are reviewed without thresholds, escalation rules, or named follow-up owners.</p><strong>Sample finding: leadership sees churn movement weekly, but no one owns the decision trigger when churn crosses threshold.</strong></article>
</div>
<div class="health-next-decision-grid" aria-label="How the diagnostic routes the next decision">
<article><span>If the issue is mostly dashboard surface</span><strong>Power BI or report cleanup</strong><p>Clean the report, retire confusing pages, and clarify the specific KPI logic that needs to be trusted.</p></article>
<article><span>If the issue is definitions and owners</span><strong>Decision System Reset</strong><p>Define metric owners, decision cadence, thresholds, and escalation paths before more dashboard build work.</p></article>
<article><span>If the issue is source trust</span><strong>Data Quality Review</strong><p>Trace the source, refresh, transformation, and manual exception path before automating or rebuilding.</p></article>
<article><span>If the issue is not severe enough</span><strong>No paid engagement yet</strong><p>Leave with a short cleanup recommendation instead of forcing a larger project where a small fix is enough.</p></article>
</div>
</section>"""


power_bi_mock = """<section class="local-seo-section power-bi-mock-section reveal-card" aria-labelledby="power-bi-mock-title">
<div class="power-bi-embed-copy">
<p class="page-kicker">Mock dashboard preview</p>
<h2 id="power-bi-mock-title">A simulated Power BI-style dashboard for the kind of cleanup this page describes.</h2>
<p>This is a lightweight Parallax-style mockup, not an embedded report. It shows the kind of operating view a Power BI engagement can move toward: fewer vanity visuals, clearer KPI ownership, visible data confidence, and a direct path from metric movement to action.</p>
</div>
<div class="power-bi-dashboard-mock" role="img" aria-label="Simulated Power BI dashboard showing KPI cards, trend chart, confidence indicators, and operating exceptions">
<div class="mock-dashboard-topbar"><span>Executive Operations</span><strong>Trusted KPI View</strong></div>
<div class="mock-kpi-row">
<article><span>Revenue</span><strong>$4.8M</strong><em>+8.4%</em></article>
<article><span>Margin</span><strong>31.2%</strong><em class="warning">Review</em></article>
<article><span>On-Time</span><strong>94.6%</strong><em>Stable</em></article>
<article><span>Data Trust</span><strong>82</strong><em class="warning">2 gaps</em></article>
</div>
<div class="mock-dashboard-body">
<div class="mock-chart-card"><span>Weekly operating signal</span><div class="mock-bars"><i style="height:42%"></i><i style="height:58%"></i><i style="height:49%"></i><i style="height:72%"></i><i style="height:66%"></i><i style="height:83%"></i><i style="height:78%"></i></div></div>
<div class="mock-chart-card"><span>Metric confidence</span><div class="mock-confidence"><b style="--v:82%">Certified KPI</b><b style="--v:63%">Source freshness</b><b style="--v:54%">Owner clarity</b></div></div>
<div class="mock-exception-card"><span>Exceptions to review</span><p>Margin variance uses two definitions across sales and finance.</p><p>Late order adjustments arrive after Monday refresh.</p><p>Backlog owner missing for regional rollup.</p></div>
</div>
</div>
</section>"""


deliverable_copy = {
    "Dashboard trust map": "A ranked view of the reports creating the most decision friction, with notes on which issues are visual, definitional, source-related, or ownership-related.",
    "Metric ownership gaps": "A list of priority KPIs with missing or unclear business owners, logic owners, source owners, and follow-up owners.",
    "Source and refresh risk list": "A practical trace of the refresh timing, exports, manual changes, and source dependencies most likely to weaken confidence.",
    "Prioritized next-step recommendation": "A clear recommendation for whether the next move is report cleanup, Data Quality Review, Decision System Reset, automation, or no paid engagement yet.",
    "Model and DAX review notes": "Specific notes on confusing measures, duplicated DAX, model relationships, grain issues, and reusable logic the team should certify.",
    "Dashboard cleanup plan": "A page-by-page plan for what to keep, consolidate, retire, rename, simplify, or rebuild so the report supports decisions more directly.",
    "Refresh and RLS checklist": "A review of refresh reliability, access roles, row-level security, source dependencies, and governance risks that can affect report trust.",
    "Embedded report readiness plan": "A launch checklist covering audience, access, refresh confidence, certified metrics, mobile usability, and whether the report is ready to publish.",
    "Published report readiness plan": "A launch checklist covering audience, access, refresh confidence, certified metrics, mobile usability, and whether the report is ready to publish.",
    "Certified metric map": "A map of priority KPIs with definitions, owners, source logic, decision use, thresholds, and change-control expectations.",
    "Decision cadence design": "A practical operating rhythm that names which decisions happen weekly or monthly, what thresholds trigger action, and who follows up.",
    "Owner and threshold model": "A model that separates business meaning, technical logic, source reliability, and action ownership so metric disputes have a clear place to land.",
    "Report retirement and rebuild plan": "A keep, consolidate, retire, or rebuild plan for dashboards and reports that have drifted away from decision use.",
    "Source trace map": "A source-to-report trace showing where fields, joins, exports, transformations, manual edits, or refresh timing can weaken confidence.",
    "Exception register": "A working register of known exceptions, impact, owner, severity, recommended fix, and review cadence.",
    "Trust break priority list": "A ranked list of the issues most likely to affect leadership decisions, so cleanup does not sprawl into low-value work.",
    "Ownership recommendations": "A practical owner model for source fixes, metric definitions, exception handling, monitoring, and ongoing change control.",
    "Metric definition cards": "Reusable cards that define each KPI, source, grain, calculation, owner, audience, decision use, and known limitations.",
    "Owner map": "A clear map of who owns metric meaning, technical logic, source quality, reporting delivery, and follow-up action.",
    "Executive scorecard outline": "A tighter executive scorecard structure that separates priority KPIs, context, thresholds, and action notes.",
    "Threshold and cadence recommendations": "Recommendations for when metrics should trigger attention, who reviews them, and how often the team should act.",
    "Manual step inventory": "A documented inventory of exports, copy-paste steps, pivots, formulas, manual edits, and judgment calls in recurring reporting.",
    "Automation readiness score": "A practical rating of which reports are stable enough to automate now and which need definition, source, or ownership cleanup first.",
    "Refresh dependency map": "A map of the systems, files, refresh schedules, transformations, and handoffs that must hold for automation to work.",
    "Exception handling rules": "Documented rules for known exceptions so automation does not hide judgment calls or spread unreliable outputs.",
    "Report inventory": "A current inventory of dashboards, reports, owners, audiences, duplicates, certified assets, and candidates for retirement.",
    "Certified metric process": "A lightweight process for approving priority metrics, documenting definitions, and keeping changes from drifting across reports.",
    "Access and RLS review": "A review of access groups, row-level security, role logic, and governance risks that can affect report confidence.",
    "Change control model": "A practical model for requesting, approving, communicating, and documenting changes to trusted reporting assets.",
}


def improve_deliverables(text: str) -> str:
    for title, copy in deliverable_copy.items():
        text = text.replace(
            f"<article><strong>{title}</strong><p>A practical artifact the team can review, reuse, and maintain after the engagement.</p></article>",
            f"<article><strong>{title}</strong><p>{copy}</p></article>",
        )
    return text


def update_analytics(rel: str) -> None:
    text = read(rel)
    text = re.sub(
        r'<section class="sample-output-deep-section reveal-card" aria-labelledby="health-sample-output-title">.*?</section>\s*<section aria-labelledby="assessment-form-title"',
        analytics_sample_new + '\n<section aria-labelledby="assessment-form-title"',
        text,
        count=1,
        flags=re.S,
    )
    form_match = re.search(r'<section aria-labelledby="assessment-form-title" class="assessment-form-section assessment-form-refined reveal-card">.*?</section>\s*', text, flags=re.S)
    if not form_match:
        raise RuntimeError("Missing analytics form")
    form_section = form_match.group(0)
    text = text[:form_match.start()] + text[form_match.end():]
    marker = '</section>\n</main>'
    text = replace_once(text, marker, form_section + marker, rel + " move form")
    text = improve_deliverables(text)
    write(rel, text)


def update_power_bi(rel: str) -> None:
    text = read(rel)
    text = re.sub(
        r'<section class="local-seo-section power-bi-embed-section reveal-card" aria-labelledby="power-bi-embed-title">.*?</section>',
        power_bi_mock,
        text,
        count=1,
        flags=re.S,
    )
    text = text.replace("Embedded report readiness plan", "Published report readiness plan")
    text = improve_deliverables(text)
    write(rel, text)


def main() -> None:
    for rel in ["dashboard-trust-scorecard.html"]:
        write(rel, update_scorecard_page(read(rel)))

    update_analytics("analytics-health-check.html")
    update_power_bi("power-bi-consultant-cincinnati.html")

    for rel in [
        "business-intelligence-consultant-cincinnati.html",
        "dashboard-trust-governance.html",
        "data-quality-review.html",
        "decision-system-reset.html",
        "expertise.html",
        "kpi-reporting-consulting.html",
        "reporting-automation-consulting.html",
    ]:
        text = improve_deliverables(read(rel))
        write(rel, text)

    for path in ROOT.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        if "local-seo-faq-grid" in text:
            text = ensure_minimum_faqs(convert_faq_grids(text))
            path.write_text(text, encoding="utf-8", newline="\n")

    print("faq-scorecard-cleanup complete")


if __name__ == "__main__":
    main()

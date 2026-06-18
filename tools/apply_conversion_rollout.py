from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text, old, new, label):
    if old not in text:
        raise RuntimeError(f"Missing marker for {label}")
    return text.replace(old, new, 1)


def write(path, text):
    path.write_text(text, encoding="utf-8")


lead_interactive = """<section class="lead-magnet-live-scorecard reveal-card" aria-labelledby="live-scorecard-title">
<div class="lead-magnet-live-intro">
<p class="page-kicker">Start before you submit</p>
<h2 id="live-scorecard-title">Score the five trust dimensions first, then send yourself the working copy.</h2>
<p>Use the quick scoring panel to get value before the form. The lowest score will tailor the final scorecard page and gives you a concrete starting point for a Fit Check.</p>
</div>
<div class="lead-magnet-live-grid" data-lead-scorecard>
<div class="lead-score-inputs" aria-label="Quick scorecard inputs">
<fieldset data-lead-score-area="Metric trust"><legend>Metric trust</legend><p>Can leaders use priority KPIs without reopening definition debates?</p><div class="lead-score-scale"><span>1 = weak / low trust</span><span>5 = strong / high trust</span></div><div class="lead-score-options"><label><input type="radio" name="lead-metric-trust" value="1">1</label><label><input type="radio" name="lead-metric-trust" value="2">2</label><label><input type="radio" name="lead-metric-trust" value="3">3</label><label><input type="radio" name="lead-metric-trust" value="4">4</label><label><input type="radio" name="lead-metric-trust" value="5">5</label></div></fieldset>
<fieldset data-lead-score-area="Ownership"><legend>Ownership</legend><p>Are definition, interpretation, and follow-up owners clear?</p><div class="lead-score-scale"><span>1 = weak / low trust</span><span>5 = strong / high trust</span></div><div class="lead-score-options"><label><input type="radio" name="lead-ownership" value="1">1</label><label><input type="radio" name="lead-ownership" value="2">2</label><label><input type="radio" name="lead-ownership" value="3">3</label><label><input type="radio" name="lead-ownership" value="4">4</label><label><input type="radio" name="lead-ownership" value="5">5</label></div></fieldset>
<fieldset data-lead-score-area="Source reliability"><legend>Source reliability</legend><p>Can the report trace back to sources, refresh rules, and known transformations?</p><div class="lead-score-scale"><span>1 = weak / low trust</span><span>5 = strong / high trust</span></div><div class="lead-score-options"><label><input type="radio" name="lead-source-reliability" value="1">1</label><label><input type="radio" name="lead-source-reliability" value="2">2</label><label><input type="radio" name="lead-source-reliability" value="3">3</label><label><input type="radio" name="lead-source-reliability" value="4">4</label><label><input type="radio" name="lead-source-reliability" value="5">5</label></div></fieldset>
<fieldset data-lead-score-area="Decision cadence"><legend>Decision cadence</legend><p>Does the dashboard connect to a recurring decision, threshold, owner, and action?</p><div class="lead-score-scale"><span>1 = weak / low trust</span><span>5 = strong / high trust</span></div><div class="lead-score-options"><label><input type="radio" name="lead-decision-cadence" value="1">1</label><label><input type="radio" name="lead-decision-cadence" value="2">2</label><label><input type="radio" name="lead-decision-cadence" value="3">3</label><label><input type="radio" name="lead-decision-cadence" value="4">4</label><label><input type="radio" name="lead-decision-cadence" value="5">5</label></div></fieldset>
<fieldset data-lead-score-area="Operational signal"><legend>Operational signal</legend><p>Can leaders see what changed, why it matters, and what needs attention?</p><div class="lead-score-scale"><span>1 = weak / low trust</span><span>5 = strong / high trust</span></div><div class="lead-score-options"><label><input type="radio" name="lead-operational-signal" value="1">1</label><label><input type="radio" name="lead-operational-signal" value="2">2</label><label><input type="radio" name="lead-operational-signal" value="3">3</label><label><input type="radio" name="lead-operational-signal" value="4">4</label><label><input type="radio" name="lead-operational-signal" value="5">5</label></div></fieldset>
</div>
<aside class="lead-score-result" data-lead-score-result>
<p class="page-kicker">Live result preview</p>
<h3>Score at least one dimension to see the likely first trust break.</h3>
<p data-lead-score-copy>The working copy will turn your lowest dimension into a printable diagnostic snapshot, evidence prompts, and a recommended next step.</p>
<dl>
<div><dt>Lowest dimension</dt><dd data-lead-score-lowest>Not scored yet</dd></div>
<div><dt>Trust average</dt><dd data-lead-score-average>-</dd></div>
<div><dt>Recommended next step</dt><dd data-lead-score-next>Start with the 3-minute scorecard.</dd></div>
</dl>
<a class="secondary-action" href="#scorecard-form-title">Send/save my result</a>
</aside>
</div>
</section>"""


analytics_deep = """<section class="sample-output-deep-section reveal-card" aria-labelledby="health-sample-output-title">
<p class="page-kicker">Sample diagnostic output</p>
<h2 id="health-sample-output-title">A Health Check readout should make the next decision obvious.</h2>
<p>The paid diagnostic is not a generic audit. It produces a practical artifact leaders can use to decide whether the next move is cleanup, governance, a reset, automation, or no engagement.</p>
<div class="sample-output-board">
<article><span>01</span><h3>Dashboard trust breakdown</h3><p>Ranks the reports creating the most decision friction, names the disputed metrics, and separates cosmetic dashboard issues from definition, source, and ownership problems.</p><strong>Sample finding: executive margin and shipped revenue are both visible, but neither has an agreed decision owner.</strong></article>
<article><span>02</span><h3>KPI ownership gaps</h3><p>Maps each priority metric to business owner, logic owner, source owner, decision cadence, and change-control path so debates have somewhere to land.</p><strong>Sample finding: sales, finance, and operations each maintain a different version of backlog.</strong></article>
<article><span>03</span><h3>Source reliability issues</h3><p>Traces weak signals through source systems, exports, manual adjustments, refresh timing, semantic logic, and side spreadsheets.</p><strong>Sample finding: a weekly export is treated as system truth even though late adjustments are made manually.</strong></article>
<article><span>04</span><h3>Decision cadence risks</h3><p>Identifies which dashboards are reviewed without thresholds, escalation rules, or named follow-up owners.</p><strong>Sample finding: leadership sees churn movement weekly, but no one owns the decision trigger when churn crosses threshold.</strong></article>
<article><span>05</span><h3>Recommended next step</h3><p>Routes the team to the smallest useful next move: a specific cleanup, Data Quality Review, Decision System Reset, Power BI model repair, or Intelligence Lab initiative.</p><strong>Sample recommendation: complete a Decision System Reset before rebuilding the executive dashboard.</strong></article>
</div>
</section>"""


reset_before_after = """<section class="before-after-proof-section reveal-card" aria-labelledby="reset-before-after-title">
<p class="page-kicker">Before and after</p>
<h2 id="reset-before-after-title">A reset changes the operating system behind the dashboard, not just the report surface.</h2>
<div class="before-after-grid">
<article class="before-card"><h3>Before the reset</h3><ul><li>Dashboard sprawl hides which reports actually support executive decisions.</li><li>Duplicated logic creates competing revenue, margin, pipeline, backlog, or quality numbers.</li><li>Metric ownership is implied, so definition disputes wait for meetings.</li><li>Decision meetings slow down because leaders debate the number before the action.</li><li>Escalation rules live in people's heads instead of in the reporting cadence.</li></ul></article>
<article class="after-card"><h3>After the reset</h3><ul><li>A governed KPI set connects each priority metric to a recurring decision.</li><li>Named owners exist for business meaning, technical logic, source reliability, and follow-up action.</li><li>Reusable reporting logic reduces dashboard-by-dashboard reconstruction.</li><li>Decision cadence, thresholds, and escalation paths are visible before the meeting starts.</li><li>Leadership has a practical operating rhythm for what changed, why it matters, and who acts next.</li></ul></article>
</div>
</section>"""


power_cleanup = """<section class="platform-proof-section reveal-card" aria-labelledby="power-bi-cleanup-title">
<p class="page-kicker">What gets cleaned up</p>
<h2 id="power-bi-cleanup-title">Power BI cleanup should make the report easier to trust, maintain, and explain.</h2>
<div class="platform-proof-grid">
<article><h3>Messy DAX and duplicated measures</h3><p>Review measures that repeat logic across pages, mix business rules into visuals, or produce slightly different answers for the same KPI.</p><strong>Output: certified measure list with owner, definition, source, and intended decision.</strong></article>
<article><h3>Slow refreshes and brittle models</h3><p>Identify refresh bottlenecks, overly heavy transformations, unused columns, unclear relationships, and model choices that make the report fragile.</p><strong>Output: model cleanup plan with performance and maintainability priorities.</strong></article>
<article><h3>Unclear semantic model</h3><p>Separate facts, dimensions, measures, and business definitions so future reports inherit stable meaning instead of rebuilding logic locally.</p><strong>Output: semantic model map and naming standards the team can reuse.</strong></article>
<article><h3>Pages with no business owner</h3><p>Retire or redesign pages that look polished but do not connect to a named decision, audience, cadence, or threshold.</p><strong>Output: report page inventory with keep, consolidate, retire, or rebuild recommendations.</strong></article>
<article><h3>RLS and governance concerns</h3><p>Clarify who should see what, how access rules are maintained, and where security design affects trust in the reporting layer.</p><strong>Output: practical governance notes for access, certification, and change control.</strong></article>
</div>
</section>
<section class="engagement-output-section reveal-card" aria-labelledby="power-bi-output-title">
<p class="page-kicker">Power BI engagement outputs</p>
<h2 id="power-bi-output-title">The goal is a Power BI environment people can keep using after launch.</h2>
<div class="engagement-output-grid">
<article><strong>Report trust review</strong><p>Which pages answer real decisions, which create confusion, and which should be retired or rebuilt.</p></article>
<article><strong>DAX and measure cleanup</strong><p>Priority measures documented with definition, owner, source, and decision context.</p></article>
<article><strong>Semantic model recommendations</strong><p>Model structure, relationships, naming, and reusable logic that reduce future dashboard drift.</p></article>
<article><strong>Refresh and reliability notes</strong><p>Known refresh risks, source dependencies, transformation issues, and maintenance priorities.</p></article>
</div>
</section>"""


quality_artifact = """<section class="exception-review-artifact reveal-card" aria-labelledby="quality-artifact-title">
<p class="page-kicker">Sample trust artifact</p>
<h2 id="quality-artifact-title">A Data Quality Review turns vague distrust into a prioritized exception map.</h2>
<p>The review is useful because it names the specific data issue, the business decision affected, who owns the fix, and how often the issue should be reviewed.</p>
<div class="exception-artifact-table" role="table" aria-label="Sample exception review artifact">
<div role="row" class="artifact-header"><span>Source issue</span><span>Business impact</span><span>Owner</span><span>Severity</span><span>Recommended fix</span><span>Follow-up cadence</span></div>
<div role="row"><span>Late order adjustments entered after dashboard refresh</span><span>Weekly shipped revenue is understated during leadership review</span><span>Operations + Finance</span><span>High</span><span>Document adjustment window and refresh dependency; expose freshness note in Power BI.</span><span>Weekly until stable</span></div>
<div role="row"><span>Customer hierarchy maintained in spreadsheet outside source system</span><span>Margin and account rollups differ by team</span><span>Sales Ops</span><span>Medium</span><span>Assign hierarchy owner and move approved mapping into governed source or model table.</span><span>Biweekly review</span></div>
<div role="row"><span>Manual exception rules not visible in report logic</span><span>Leaders cannot explain why dashboard totals differ from exported detail</span><span>Analytics Owner</span><span>High</span><span>Trace exceptions, document rules, and certify which overrides are allowed.</span><span>Weekly until resolved</span></div>
</div>
</section>"""


local_industries = """<section class="local-industry-depth reveal-card" aria-labelledby="local-industry-title">
<p class="page-kicker">Industries served</p>
<h2 id="local-industry-title">Local trust comes from understanding how reporting pressure shows up by industry.</h2>
<p>Cincinnati and Midwest analytics work often sits close to operations. The reporting problem is rarely just a visual problem; it is usually a timing, ownership, source, or decision-cadence problem inside the way the business runs.</p>
<div class="local-industry-grid">
<article><h3>Manufacturing</h3><p>Production, labor, scrap, throughput, downtime, quality, inventory, and customer commitments need one operating view so leaders can see tradeoffs before the weekly meeting.</p></article>
<article><h3>Healthcare and services</h3><p>Access, utilization, staffing, quality, service levels, and revenue-cycle signals need careful definitions because small interpretation gaps can change priorities quickly.</p></article>
<article><h3>Construction and field operations</h3><p>Project performance, backlog, labor, material timing, change orders, and margin reporting need clear owners because the source of truth often moves across systems.</p></article>
<article><h3>Retail and distribution</h3><p>Sales, margin, inventory, location performance, service levels, and fulfillment timing need dashboards that separate normal seasonality from problems requiring action.</p></article>
<article><h3>Marketing and professional services</h3><p>Pipeline, campaign performance, utilization, client profitability, and delivery capacity need a shared metric language so teams do not optimize separate reports.</p></article>
<article><h3>Energy and utilities</h3><p>Reliability, asset, field, customer, and operational signals need reporting that makes exceptions visible without burying leaders in raw data.</p></article>
</div>
</section>"""


local_faq_extra = """<article><h3>Do you support Power BI teams locally?</h3><p>Yes. Power BI support can include dashboard cleanup, DAX review, semantic model structure, refresh reliability, RLS, executive KPI reporting, and governance around which reports should be trusted.</p></article>
<article><h3>What industries do you understand in the Midwest?</h3><p>Common patterns include manufacturing, healthcare, construction, retail, distribution, marketing and services, energy, logistics, and mid-market operators where reporting has to connect finance, operations, customer commitments, and leadership cadence.</p></article>
<article><h3>Can you work with teams outside Cincinnati?</h3><p>Yes. Cincinnati is the base, but the work is built for teams across the United States. Local context helps regional teams, while the core discipline around trusted reporting, ownership, and decision systems travels well.</p></article>
<article><h3>Is this dashboard development or analytics consulting?</h3><p>It can include dashboard development, but the stronger fit is analytics consulting: clarifying metrics, owners, source trust, Power BI structure, reporting automation, and the decisions the dashboards are supposed to support.</p></article>
<article><h3>What makes local analytics consulting useful?</h3><p>Local support is useful when the consultant understands the pace, practical constraints, industry mix, and operating tradeoffs behind the numbers. The goal is not more local keywords; it is reporting that fits how the business actually runs.</p></article>"""


about_trust = """<section class="founder-trust-proof reveal-card" aria-labelledby="founder-trust-title">
<p class="page-kicker">Founder credibility</p>
<h2 id="founder-trust-title">Practical analytics experience across Power BI, reporting operations, and decision systems.</h2>
<div class="founder-trust-grid">
<article><strong>Deep Power BI experience</strong><p>Dashboard development, DAX measures, semantic models, refresh reliability, RLS, report cleanup, and executive KPI reporting.</p></article>
<article><strong>Cincinnati operating context</strong><p>More than 10 years in Cincinnati, with practical familiarity across the Midwest business mix: manufacturing, services, healthcare, construction, retail, marketing, energy, logistics, and growing operators.</p></article>
<article><strong>End-to-end analytics ownership</strong><p>Work across source logic, model design, governance, stakeholder alignment, reporting delivery, and the operating cadence needed to keep analytics trusted.</p></article>
</div>
</section>"""


def main():
    changed = []

    # Lead magnet landing page.
    for rel in ["dashboard-trust-scorecard.html"]:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        text = text.replace('href="#scorecard-form-title">Get the Scorecard</a>', 'href="#live-scorecard-title">Start the 3-minute scorecard</a>')
        text = text.replace("This page only previews the five areas so the downloaded scorecard still does the actual diagnostic work.", "Start by scoring the five areas below. The form then sends the working copy and carries your lowest dimension into the final scorecard page.")
        text = replace_once(text, '</section>\n<section class="lead-magnet-form-section reveal-card" aria-labelledby="scorecard-form-title">', f'</section>\n{lead_interactive}\n<section class="lead-magnet-form-section reveal-card" aria-labelledby="scorecard-form-title">', rel + " lead interactive")
        text = text.replace('<h2 id="scorecard-form-title">Get the printable scorecard.</h2>', '<h2 id="scorecard-form-title">Send or save the working scorecard.</h2>')
        text = text.replace('Submit the form and the next page will open the working scorecard. Your selected dimension will tailor the printable guidance, and the optional context field can capture usability, adoption, executive alignment, or anything else showing up.', 'After you score the five dimensions, submit the form to open the working scorecard, send the request through the backend, and preserve the lowest trust break for the final guidance. The email gate comes after the quick diagnostic so the page gives value first.')
        text = text.replace('<input name="Submitted From" type="hidden" value="Dashboard Trust Scorecard"/>', '<input name="Submitted From" type="hidden" value="Dashboard Trust Scorecard"/>\n<input name="Scorecard Lowest Dimension" type="hidden" data-lead-score-lowest-input/>\n<input name="Scorecard Average Score" type="hidden" data-lead-score-average-input/>\n<input name="Scorecard Scores" type="hidden" data-lead-score-summary-input/>')
        write(path, text)
        changed.append(rel)

    # Scorecard final page: stronger routing language.
    path = ROOT / "dashboard-trust-scorecard-download.html"
    text = path.read_text(encoding="utf-8")
    old = """<div class="scorecard-interpret-grid">
<article><strong>Metric trust</strong><p>Clarify the KPI definition, business meaning, lineage, and decision it supports before redesigning the report.</p></article>
<article><strong>Ownership</strong><p>Name who owns the metric definition, source logic, business interpretation, and follow-up action.</p></article>
<article><strong>Source reliability</strong><p>Inspect the source system, transformation path, refresh rule, manual adjustment, and side-spreadsheet workaround.</p></article>
<article><strong>Decision cadence</strong><p>Reconnect the report to a recurring decision, threshold, owner, action path, and escalation rule.</p></article>
<article><strong>Operational signal</strong><p>Package what changed, why it matters, what needs attention, and what leadership should do next.</p></article>
</div>"""
    new = """<div class="scorecard-interpret-grid scorecard-route-grid">
<article><strong>Metric trust</strong><p>Clarify the KPI definition, business meaning, lineage, and decision it supports before redesigning the report.</p><a href="free-fit-check.html">Recommended: Fit Check or Analytics Health Check</a></article>
<article><strong>Ownership</strong><p>Name who owns the metric definition, source logic, business interpretation, and follow-up action.</p><a href="decision-system-reset.html">Recommended: Decision System Reset</a></article>
<article><strong>Source reliability</strong><p>Inspect the source system, transformation path, refresh rule, manual adjustment, and side-spreadsheet workaround.</p><a href="data-quality-review.html">Recommended: Data Quality Review or Health Check</a></article>
<article><strong>Decision cadence</strong><p>Reconnect the report to a recurring decision, threshold, owner, action path, and escalation rule.</p><a href="decision-system-reset.html">Recommended: Decision System Reset</a></article>
<article><strong>Operational signal</strong><p>Package what changed, why it matters, what needs attention, and what leadership should do next.</p><a href="intelligence-lab.html">Recommended: Intelligence Lab or Fit Check</a></article>
</div>"""
    text = replace_once(text, old, new, "download route grid")
    text = text.replace("Bring the lowest area and evidence notes into the Fit Check.", "Bring the lowest area, evidence notes, and one real dashboard or metric example into the Fit Check. The useful conversation starts with the area that scored lowest, not the total score.")
    write(path, text)
    changed.append("dashboard-trust-scorecard-download.html")

    # Analytics Health Check proof.
    path = ROOT / "analytics-health-check.html"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, '<section aria-labelledby="assessment-form-title" class="assessment-form-section assessment-form-refined reveal-card">', analytics_deep + '\n<section aria-labelledby="assessment-form-title" class="assessment-form-section assessment-form-refined reveal-card">', "analytics deep sample")
    write(path, text)
    changed.append("analytics-health-check.html")

    # Decision System Reset proof.
    path = ROOT / "decision-system-reset.html"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, '<section class="deliverable-proof-section reveal-card" aria-labelledby="decision-system-reset-deliverables-title">', reset_before_after + '\n<section class="deliverable-proof-section reveal-card" aria-labelledby="decision-system-reset-deliverables-title">', "reset before after")
    write(path, text)
    changed.append("decision-system-reset.html")

    # Power BI proof.
    path = ROOT / "power-bi-consultant-cincinnati.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace('Book a Fit Check</a>\n<a class="secondary-action" href="how-we-help.html#platform-local-expertise">Explore Expertise</a>', 'Review a Power BI Reporting Issue</a>\n<a class="secondary-action" href="expertise.html">Explore Expertise</a>')
    text = replace_once(text, '<section class="expertise-related-articles reveal-card" aria-labelledby="power-bi-related-title">', power_cleanup + '\n<section class="expertise-related-articles reveal-card" aria-labelledby="power-bi-related-title">', "power cleanup")
    write(path, text)
    changed.append("power-bi-consultant-cincinnati.html")

    # Data quality proof.
    path = ROOT / "data-quality-review.html"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, '<section class="expertise-related-articles reveal-card" aria-labelledby="related-articles-title">', quality_artifact + '\n<section class="expertise-related-articles reveal-card" aria-labelledby="related-articles-title">', "quality artifact")
    write(path, text)
    changed.append("data-quality-review.html")

    # Cincinnati local trust.
    path = ROOT / "business-intelligence-consultant-cincinnati.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace('"areaServed": [\n    {\n      "@type": "City",\n      "name": "Cincinnati"\n    },\n    {\n      "@type": "State",\n      "name": "Ohio"\n    },\n    {\n      "@type": "Country",\n      "name": "United States"\n    }\n  ],', '"areaServed": [\n    {\n      "@type": "City",\n      "name": "Cincinnati"\n    },\n    {\n      "@type": "AdministrativeArea",\n      "name": "Northern Kentucky"\n    },\n    {\n      "@type": "City",\n      "name": "Dayton"\n    },\n    {\n      "@type": "City",\n      "name": "Columbus"\n    },\n    {\n      "@type": "State",\n      "name": "Ohio"\n    },\n    {\n      "@type": "Country",\n      "name": "United States"\n    }\n  ],')
    text = text.replace('"BI governance"\n  ],', '"BI governance",\n    "Cincinnati analytics consulting",\n    "Manufacturing reporting",\n    "Healthcare analytics",\n    "Construction reporting",\n    "Retail analytics",\n    "Energy and utilities reporting"\n  ],')
    text = replace_once(text, '<section class="expertise-related-articles reveal-card" aria-labelledby="cincinnati-related-title">', local_industries + '\n<section class="expertise-related-articles reveal-card" aria-labelledby="cincinnati-related-title">', "local industries")
    text = text.replace('</div>\n</section>\n<section class="deliverable-proof-section reveal-card" aria-labelledby="business-intelligence-consultant-cincinnati-deliverables-title">', local_faq_extra + '\n</div>\n</section>\n<section class="deliverable-proof-section reveal-card" aria-labelledby="business-intelligence-consultant-cincinnati-deliverables-title">')
    write(path, text)
    changed.append("business-intelligence-consultant-cincinnati.html")

    # Expertise focus copy.
    path = ROOT / "expertise.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace('<h2>How To Choose The Right Path</h2>\n<p>Start with the pain that keeps repeating. If leaders debate numbers, start with dashboard trust or KPI reporting. If Power BI is visible but the real problem is model structure, DAX logic, or refresh reliability, start with Power BI consulting. If data keeps getting reconciled outside the system, start with data quality review. If the team is rebuilding recurring reports by hand, start with reporting automation. If the issue is local context, Midwest industry patterns, or Cincinnati operating cadence, start with local analytics consulting.</p>', '<h2>How To Choose The Right Path</h2>\n<p>Use this hub to identify the capability behind the symptom, then move to one concrete next step. Power BI issues usually start with a report or model review. KPI disputes usually need ownership and definition work. Data quality issues need source tracing. Local Cincinnati questions need context around the operating rhythm. The buying ladder stays on the Offerings page; this page is for capability fit.</p>')
    write(path, text)
    changed.append("expertise.html")

    # Home page focus.
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace('<a class="is-optional" href="dashboard-trust-scorecard.html">Optional Diagnostic Scorecard</a>', '<a class="is-optional" href="dashboard-trust-scorecard.html">Optional 3-Minute Scorecard</a>')
    text = text.replace('<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>', '<a class="primary-action" href="free-fit-check.html">Book the Free Fit Check</a>', 1)
    write(path, text)
    changed.append("index.html")

    # About founder credibility.
    path = ROOT / "about.html"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, '<section class="about-work-examples reveal-card" aria-labelledby="about-work-title">', about_trust + '\n<section class="about-work-examples reveal-card" aria-labelledby="about-work-title">', "about founder trust")
    write(path, text)
    changed.append("about.html")

    print("\n".join(changed))


if __name__ == "__main__":
    main()

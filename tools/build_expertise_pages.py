from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YEAR = "2026"
VERSION = "125"


SOCIAL_SVG = """<a class="site-social-link site-social-linkedin" href="https://www.linkedin.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.1 8.4h3.8v11.5H5.1V8.4Zm1.9-5.7a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4Zm4.1 5.7h3.6v1.6h.1c.5-.9 1.7-1.9 3.5-1.9 3.7 0 4.4 2.4 4.4 5.6v6.2h-3.8v-5.5c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9v5.6h-3.8V8.4Z"/></svg></a>
        <a class="site-social-link site-social-youtube" href="https://www.youtube.com/@ParallaxDataLab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 7.1a3 3 0 0 0-2.1-2.1C18 4.5 12 4.5 12 4.5s-6 0-7.9.5A3 3 0 0 0 2 7.1 31.6 31.6 0 0 0 1.5 12c0 1.7.2 3.4.5 4.9A3 3 0 0 0 4.1 19c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1c.3-1.5.5-3.2.5-4.9s-.2-3.4-.5-4.9ZM10 15.2V8.8l5.6 3.2-5.6 3.2Z"/></svg></a>
        <a class="site-social-link site-social-instagram" href="https://www.instagram.com/parallaxdatalab/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.2 2.8h9.6a4.4 4.4 0 0 1 4.4 4.4v9.6a4.4 4.4 0 0 1-4.4 4.4H7.2a4.4 4.4 0 0 1-4.4-4.4V7.2a4.4 4.4 0 0 1 4.4-4.4Zm0 2A2.4 2.4 0 0 0 4.8 7.2v9.6a2.4 2.4 0 0 0 2.4 2.4h9.6a2.4 2.4 0 0 0 2.4-2.4V7.2a2.4 2.4 0 0 0-2.4-2.4H7.2Zm4.8 3a4.2 4.2 0 1 1 0 8.4 4.2 4.2 0 0 1 0-8.4Zm0 2a2.2 2.2 0 1 0 0 4.4 2.2 2.2 0 0 0 0-4.4Zm4.6-2.9a1 1 0 1 1 0 2.1 1 1 0 0 1 0-2.1Z"/></svg></a>
        <a class="site-social-link site-social-x" href="https://x.com/parallaxdatalab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on X"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.8 10.4 21.1 2h-1.7l-6.3 7.2L8 2H2.2l7.7 11-7.7 9h1.7l6.8-7.8 5.5 7.8H22l-8.2-11.6Zm-2.4 2.8-.8-1.1L4.4 3.3h2.8l5 7.1.8 1.1 6.5 9.2h-2.8l-5.3-7.5Z"/></svg></a>"""


PAGES = {
    "expertise": {
        "title": "Analytics Expertise | Power BI, KPI Reporting & Data Quality",
        "description": "Explore Parallax Data Lab expertise in Power BI consulting, KPI reporting, reporting automation, data quality review, dashboard trust, and data analytics consulting in Cincinnati.",
        "kicker": "Analytics Expertise",
        "h1": "Expertise for the reporting problems that sit underneath the dashboard request.",
        "intro": "Some teams arrive with a broad reporting problem. Others know the pain by name: Power BI reports are hard to trust, KPI reporting has drifted, manual reporting eats too much time, data quality breaks confidence, or the business needs data analytics consulting in Cincinnati from someone who understands Midwest operating context.",
        "hero_image": "assets/home-generated/help-foundation-to-intelligence-advanced.png",
        "hero_alt": "Analytics expertise map connecting Power BI reporting data quality and governance",
        "proof": ["Power BI", "KPI Reporting", "Reporting Automation", "Data Quality", "Dashboard Trust"],
        "sections": [
            ("Related Experience", "The same problems tend to show up through different doors. A Power BI request may actually be a metric-definition problem. A reporting automation request may expose weak source logic. A data quality review may reveal that nobody owns the dashboard people argue about every week. Parallax Data Lab brings those threads together so the work does not stop at a prettier report."),
            ("What Connects The Work", "The common thread is trust. Reports earn trust when the data path is understandable, the metric definitions are owned, the dashboard answers a real operating question, and the review cadence turns the number into action. The platform matters, but the business layer above the platform matters more: source logic, ownership, governance, automation readiness, and the decision rhythm leaders actually use."),
            ("Where The Details Live", "Each expertise page goes deeper on a specific pattern: Power BI systems that need clearer models and reporting structure, KPI reporting that needs shared meaning, automation that needs clean business rules before it scales, data quality problems that create reconciliation work, dashboard governance that restores confidence, and Cincinnati analytics support shaped by local operating context.")
        ],
        "cards": [
            ("Power BI Consulting", "power-bi-consultant-cincinnati.html", "assets/home-generated/power-bi-report-hero.jpg", "Power BI dashboard and semantic model consulting"),
            ("KPI Reporting", "kpi-reporting-consulting.html", "assets/home-generated/power-bi-cincinnati-kpi-governance.jpg", "KPI reporting and metric governance workflow"),
            ("Reporting Automation", "reporting-automation-consulting.html", "assets/home-generated/power-bi-cincinnati-data-quality.jpg", "Reporting automation pipeline for trusted business reporting"),
            ("Data Quality Review", "data-quality-review.html", "assets/home-generated/failure-source-of-truth.png", "Data quality review tracing reporting source issues"),
            ("Dashboard Trust & BI Governance", "dashboard-trust-governance.html", "assets/home-generated/help-situation-dashboard-trust.png", "Dashboard trust and BI governance system"),
            ("Data Analytics Consulting Cincinnati", "business-intelligence-consultant-cincinnati.html", "assets/home-generated/cincinnati-skyline-hero.jpg", "Cincinnati skyline for local data analytics consulting")
        ],
        "faq": [
            ("Should expertise pages replace offerings?", "No. The offering pages remain the product ladder. Expertise pages clarify capability, symptoms, and fit, then route the visitor to the right starting point."),
            ("Why not put everything on one services page?", "A single broad services page gets muddy quickly. Separate expertise pages let each topic show the symptoms, examples, related articles, and practical next steps a buyer needs."),
            ("How do these pages stay useful?", "Each page is built around real buyer problems, operating symptoms, examples, and decision paths, so visitors can understand what kind of help fits before booking a call.")
        ],
        "articles": [
            ("Why Nobody Trusts Your Dashboard", "insights/why-nobody-trusts-your-dashboard.html"),
            ("The Difference Between Reporting And Decision Making", "insights/the-difference-between-reporting-and-decision-making.html"),
            ("Analytics Maturity Roadmap", "insights/analytics-maturity-roadmap-reporting-to-decision-systems.html"),
        ],
    },
    "kpi-reporting-consulting": {
        "title": "KPI Reporting Consulting | Metrics Leaders Can Trust",
        "description": "KPI reporting consulting for teams that need clearer metric definitions, executive reporting cadence, ownership, dashboard trust, and decision-ready scorecards.",
        "kicker": "KPI Reporting",
        "h1": "KPI reporting consulting for metrics leaders can actually use.",
        "intro": "KPI reporting breaks when the organization has numbers but not shared meaning. The dashboard may look polished, but leaders still ask which number is right, why it changed, who owns the definition, and what decision the metric is supposed to inform. Parallax Data Lab helps teams turn scattered measures into a practical reporting system with definitions, owners, thresholds, and a cadence for action.",
        "hero_image": "assets/home-generated/power-bi-cincinnati-kpi-governance.jpg",
        "hero_alt": "KPI reporting governance dashboard with trusted executive metrics",
        "proof": ["KPI Definitions", "Metric Ownership", "Executive Cadence", "Scorecards", "Dashboard Trust"],
        "sections": [
            ("Why KPI Reporting Fails", "KPI reporting is often treated like a visualization problem. The deeper issue is usually structural. Different teams calculate the same metric differently, source systems use different timing, manual adjustments are undocumented, and executives inherit a dashboard without knowing the operating question behind each number. The result is a familiar meeting pattern: people spend the first half reconciling the number and the second half running out of time to decide what to do."),
            ("What Good KPI Reporting Includes", "Useful KPI reporting defines the business question first. It names the owner, source, refresh timing, grain, inclusion rules, exclusions, threshold logic, and expected action path. In Power BI or any other reporting layer, the visual should make those choices easier to understand instead of hiding them. The point is not a bigger metric library. It is a smaller set of measures leaders can use without stopping the meeting to reconstruct the math."),
            ("How Parallax Helps", "The engagement can start with a narrow review of one leadership scorecard or expand into a broader KPI governance reset. We identify where definitions drift, which metrics need owners, where reports should be retired, and how the weekly or monthly review should change. The goal is not to measure everything. The goal is to create a smaller set of metrics that leaders understand, use, and maintain.")
        ],
        "cards": [
            ("Metric Definition Review", "#metric-definition-review", "assets/home-generated/quote-useful-metrics.png", "Useful KPI definitions organized for leadership reporting"),
            ("Ownership Mapping", "#ownership-mapping", "assets/home-generated/quote-ownership-definitions.png", "Metric ownership definitions for KPI governance"),
            ("Executive Scorecard Design", "#executive-scorecard-design", "assets/home-generated/help-outcome-renewed-confidence.png", "Executive scorecard showing renewed trust in reporting")
        ],
        "service_blocks": [
            ("Metric Definition Review", "Clarify calculations, source systems, timing, exclusions, and interpretation rules for the KPIs that drive decisions."),
            ("Ownership Mapping", "Name who owns each metric, who can approve changes, and who explains movement when leadership asks why."),
            ("Executive Scorecard Design", "Design a scorecard or dashboard that shows trend, target, owner, confidence, and action context without overwhelming the reader."),
            ("Cadence Alignment", "Connect the reporting cycle to operating meetings so metrics create action instead of passive status updates."),
            ("Power BI KPI Cleanup", "Refactor measures, labels, pages, and semantic-model logic when Power BI is the main reporting layer."),
            ("Decision Thresholds", "Define what movement matters, what is noise, and when the team should escalate or act.")
        ],
        "faq": [
            ("Do we need new KPIs or cleaner existing KPIs?", "Usually the first step is cleaning the existing set. Most teams already have enough metrics; they need fewer disputes, clearer definitions, and stronger ownership."),
            ("Can KPI reporting work happen without Power BI?", "Yes. The work applies to Power BI, spreadsheets, CRM exports, operating reports, or executive scorecards. The platform matters, but the metric logic matters more."),
            ("Where does this fit with Decision System Reset?", "KPI reporting can be a focused expertise path. Decision System Reset is broader when the metric, dashboard, ownership, and operating cadence all need to be redesigned together.")
        ],
        "articles": [
            ("How To Build Metrics People Actually Use", "insights/how-to-build-metrics-people-actually-use.html"),
            ("KPI Governance Explained For Growing Organizations", "insights/kpi-governance-explained-growing-organizations.html"),
            ("The KPI Ownership Framework Every Leadership Team Needs", "insights/kpi-ownership-framework-every-leadership-team-needs.html"),
        ],
    },
    "reporting-automation-consulting": {
        "title": "Reporting Automation Consulting | Faster Trusted Reporting",
        "description": "Reporting automation consulting for teams that want to reduce manual reporting, improve refresh reliability, protect data quality, and automate recurring analytics workflows.",
        "kicker": "Reporting Automation",
        "h1": "Reporting automation consulting that makes reporting faster without spreading bad logic.",
        "intro": "Automation is powerful only when the reporting process is stable enough to repeat. If definitions are disputed, source data is messy, or manual edits are hiding exceptions, automation can make the wrong answer arrive faster. Parallax Data Lab helps teams decide what should be automated, what should be cleaned first, and how to build repeatable reporting workflows that leaders can trust.",
        "hero_image": "assets/home-generated/power-bi-cincinnati-data-quality.jpg",
        "hero_alt": "Reporting automation pipeline turning source data into trusted dashboards",
        "proof": ["Manual Reporting", "Refresh Reliability", "Workflow Design", "Data Quality", "Decision Cadence"],
        "sections": [
            ("The Right Automation Starting Point", "Many reporting automation requests begin with a spreadsheet that someone rebuilds every week. The visible request is speed, but the real issue may be inconsistent source pulls, hidden copy-paste logic, late-arriving data, fragile joins, or a metric that nobody owns. Automation should be designed a layer above the tool first: what business rule repeats, what exception needs judgment, what source can be trusted, and what review cadence the output supports."),
            ("What Should Be Automated", "Good candidates for automation are recurring reports with stable inputs, clear definitions, known owners, and a predictable review cycle. Poor candidates are reports where every period requires judgment, exceptions are undocumented, or leaders still disagree about what the metric means. We separate repetitive preparation from business interpretation, so automation removes waste without removing accountability."),
            ("How Parallax Helps", "Parallax reviews the current reporting workflow from source to audience. We map the manual steps, identify fragile transformations, document the business logic, and recommend the smallest automation path that reduces effort while protecting trust. That might mean upstream data cleanup, Power BI refresh improvement, a documented reporting calendar, a data quality checkpoint, or a new dashboard that replaces recurring spreadsheet assembly.")
        ],
        "cards": [
            ("Manual Step Audit", "#manual-step-audit", "assets/home-generated/help-situation-bottleneck.png", "Manual reporting bottleneck being analyzed for automation"),
            ("Repeatable Data Prep", "#repeatable-data-prep", "assets/home-generated/help-process-build-guide.png", "Repeatable data preparation and reporting workflow"),
            ("Refresh Reliability", "#refresh-reliability", "assets/home-generated/work-ongoing-optimization.png", "Reporting automation refresh reliability monitoring")
        ],
        "service_blocks": [
            ("Manual Step Audit", "Identify copy-paste work, recurring exports, fragile formulas, and hidden assumptions inside the current reporting process."),
            ("Transformation Cleanup", "Move heavy or fragile logic to the right layer, simplify repeatable transformations, and make refresh behavior easier to maintain."),
            ("Refresh Reliability Review", "Check refresh timing, dependencies, failures, source permissions, and ownership so automated reporting is not quietly stale."),
            ("Automation Readiness", "Decide which reports should be automated now and which need definition, source, or ownership cleanup first."),
            ("Reporting Calendar Design", "Align refresh cycles, review meetings, and stakeholder expectations so automation supports the operating rhythm."),
            ("Exception Handling", "Document what happens when data is late, incomplete, manually adjusted, or outside normal thresholds.")
        ],
        "faq": [
            ("Should every manual report be automated?", "No. Automate repetitive, stable work. Fix unclear definitions, source issues, and ownership gaps before automating reports that still require heavy judgment."),
            ("Can automation include Power BI?", "Yes. It can include refresh scheduling, semantic-model cleanup, dashboard replacement, and reporting governance around Power BI. The goal is to avoid burying too much business logic inside a brittle report layer."),
            ("What is the main risk?", "The main risk is scaling unclear logic. Automation should reduce manual effort while making business rules more visible, not more hidden.")
        ],
        "articles": [
            ("Five Signs Your Reporting Environment Is Breaking Down", "insights/five-signs-your-reporting-environment-is-breaking-down.html"),
            ("Where AI Actually Helps In Analytics Operations", "insights/where-ai-actually-helps-in-analytics-operations.html"),
            ("Prepare Your Reporting Environment For AI", "insights/prepare-reporting-environment-for-ai.html"),
        ],
    },
    "data-quality-review": {
        "title": "Data Quality Review | Find Why Reports Are Not Trusted",
        "description": "Data quality review for teams dealing with inconsistent metrics, source system issues, manual reporting patches, reconciliation work, and dashboard trust problems.",
        "kicker": "Data Quality Review",
        "h1": "Data quality review for teams tired of reconciling the same numbers.",
        "intro": "Data quality problems show up as reporting problems: dashboards do not match, leaders question the numbers, teams keep offline spreadsheets, and analysts spend too much time explaining exceptions. Parallax Data Lab reviews the path from source systems to reporting outputs so teams can find where trust is breaking and what needs to be fixed first.",
        "hero_image": "assets/home-generated/failure-source-of-truth.png",
        "hero_alt": "Data quality review tracing conflicting source systems into trusted reporting",
        "proof": ["Source Systems", "Manual Patches", "Metric Drift", "Reconciliation", "Trust Review"],
        "sections": [
            ("What Data Quality Means In Reporting", "Data quality is not only whether a table has blanks. It includes whether data is accurate enough for the decision, complete enough for the audience, consistent across systems, timely enough for the meeting, and traceable enough for leaders to understand. IBM describes data quality as a measure of how well data serves its intended purpose, with dimensions such as accuracy, completeness, consistency, timeliness, and validity. In a business intelligence environment, those dimensions become visible every time a dashboard is challenged."),
            ("Where Quality Breaks", "Quality issues often begin upstream: duplicated customer records, inconsistent product hierarchies, late operational entries, manual spreadsheet patches, unowned mapping tables, or business rules that changed without documentation. By the time the issue reaches Power BI or an executive scorecard, the dashboard is blamed for a problem that started much earlier. A review traces the path instead of guessing at the symptom."),
            ("How Parallax Helps", "Parallax reviews key reports, source extracts, transformations, metric definitions, and exception handling. The output is a clear map of the trust breaks: what is wrong, why it matters, who needs to own it, and which fixes should happen before more reporting automation or dashboard development. The work is practical, not academic. The goal is to restore enough confidence that leaders can act without rebuilding the answer in every meeting.")
        ],
        "cards": [
            ("Source Trace", "#source-trace", "assets/home-generated/failure-conflicting-numbers.png", "Conflicting source numbers traced for data quality review"),
            ("Exception Review", "#exception-review", "assets/home-generated/failure-definition-drift.png", "Definition drift and reporting exceptions reviewed"),
            ("Trust Map", "#trust-map", "assets/home-generated/assessment-trust-map.png", "Trust map for data quality and reporting confidence")
        ],
        "service_blocks": [
            ("Source Trace", "Follow critical numbers from source systems through transformations, manual edits, semantic models, and final reports."),
            ("Completeness Review", "Identify missing records, late data, incomplete dimensions, and fields that limit decision usefulness."),
            ("Consistency Review", "Find where systems, teams, dashboards, or spreadsheets define the same business object differently."),
            ("Exception Handling", "Document manual overrides, special cases, one-off corrections, and judgment calls that affect reported numbers."),
            ("Ownership Recommendations", "Clarify who owns source fixes, transformation logic, definitions, and ongoing monitoring."),
            ("Priority Fix Map", "Separate urgent trust breaks from nice-to-have cleanup so the team can make progress without boiling the ocean.")
        ],
        "faq": [
            ("Is this the same as a technical data audit?", "Not exactly. The review includes technical tracing, but it is focused on reporting trust and business decision impact."),
            ("Do we need perfect data before improving dashboards?", "No. You need known data. Leaders can act with imperfect data when the limits, owners, and confidence level are clear."),
            ("Can this come before automation?", "Often it should. Automating a low-quality process can make unreliable reporting spread faster.")
        ],
        "articles": [
            ("Single Source Of Truth Myth", "insights/single-source-of-truth-myth.html"),
            ("Why Data Teams Struggle To Earn Trust", "insights/why-data-teams-struggle-to-earn-trust.html"),
            ("Who Owns This Metric?", "insights/who-owns-this-metric-most-expensive-question-in-analytics.html"),
        ],
    },
    "dashboard-trust-governance": {
        "title": "Dashboard Trust & BI Governance Consulting",
        "description": "Dashboard trust and BI governance consulting for teams that need certified metrics, ownership, access rules, workspace structure, and reporting change control.",
        "kicker": "Dashboard Trust & BI Governance",
        "h1": "Dashboard trust and BI governance for teams with too many reports and not enough confidence.",
        "intro": "Dashboard trust breaks when reports multiply faster than standards. Teams create their own versions, certified datasets are unclear, access rules are informal, and leaders no longer know which report should be treated as the source of truth. Parallax Data Lab helps teams build practical BI governance that supports speed instead of burying people in process.",
        "hero_image": "assets/home-generated/help-situation-dashboard-trust.png",
        "hero_alt": "Dashboard trust and BI governance system for executive reporting",
        "proof": ["Certified Metrics", "Workspace Structure", "Access Rules", "RLS", "Change Control"],
        "sections": [
            ("Governance Should Make Reporting Easier", "BI governance is not a policy binder. It is the operating layer that helps teams know which reports are official, which metrics are certified, who can change logic, how access is granted, and when a dashboard should be retired. Microsoft notes that Power BI includes sharing, collaboration, workspaces, security, usage metrics, audit logs, and row-level security. Those capabilities are useful only when the business has clear rules for how they should be used."),
            ("Where Trust Breaks", "Trust breaks when the business has no report inventory, no definition owner, no certified metric process, no workspace standards, no refresh expectations, or no access model. Row-level security can restrict data access for specific users, but it still needs role definitions, testing, and ownership. A governance review turns these scattered decisions into a practical model people can follow."),
            ("How Parallax Helps", "Parallax maps the current dashboard environment, identifies duplicate reports, clarifies certified sources, reviews ownership, and recommends standards that fit the team's maturity. The work can include Power BI workspace structure, report lifecycle rules, RLS review, metric governance, dashboard retirement, and executive reporting cadence. The aim is not bureaucracy. The aim is a reporting environment where people can move faster because they know what to trust.")
        ],
        "cards": [
            ("Report Inventory", "#report-inventory", "assets/home-generated/help-outcome-fewer-reports.png", "Reports consolidating into fewer trusted dashboards"),
            ("Access And Security", "#access-and-security", "assets/home-generated/lab-governance-rls.png", "Governance and row level security architecture"),
            ("Certified Metrics", "#certified-metrics", "assets/home-generated/reset-metric-mapping-v2.png", "Certified metric mapping for BI governance")
        ],
        "service_blocks": [
            ("Report Inventory", "Identify active reports, owners, audiences, duplicate dashboards, and assets that should be consolidated or retired."),
            ("Certified Metric Process", "Define which metrics are official, where they live, who can change them, and how changes are communicated."),
            ("Workspace Structure", "Create practical standards for Power BI workspaces, development areas, published apps, and shared datasets."),
            ("Access And Security", "Review user roles, workspace permissions, row-level security expectations, and approval paths for sensitive data."),
            ("Change Control", "Set lightweight rules for metric changes, report updates, refresh failures, and stakeholder communication."),
            ("Governance Cadence", "Make governance maintainable with a recurring review cycle rather than a one-time cleanup.")
        ],
        "faq": [
            ("Is BI governance only for large companies?", "No. Growing teams need lightweight governance before dashboard sprawl becomes expensive."),
            ("Can governance slow people down?", "Bad governance can. Good governance makes the trusted path obvious so teams spend less time debating which report to use."),
            ("Does this include Power BI RLS?", "It can. Row-level security review fits here when access, roles, and report trust are part of the problem.")
        ],
        "articles": [
            ("Why Nobody Trusts Your Dashboard", "insights/why-nobody-trusts-your-dashboard.html"),
            ("Governance And RLS Architecture Is A Business Issue", "insights/governance-rls-architecture-business-issue.html"),
            ("Why Executive Dashboards Fail", "insights/why-executive-dashboards-fail.html"),
        ],
    },
}


def prefix_for(path: Path) -> str:
    relative = os.path.relpath(ROOT, path.parent)
    return "" if relative == "." else relative.replace("\\", "/") + "/"


def href(prefix: str, target: str) -> str:
    if target.startswith(("http://", "https://", "#")):
        return target
    return f"{prefix}{target}"


def nav_html(prefix: str) -> str:
    return f'''<header aria-label="Parallax site navigation" class="site-header">
<a aria-label="Parallax Data Lab home" class="site-brand" href="{href(prefix, 'index.html')}"><img alt="Parallax Data Lab logo" src="{href(prefix, 'assets/parallax_data_lab_original_transparent.png')}" decoding="async"></a>
<button aria-controls="primary-navigation" aria-expanded="false" aria-label="Toggle navigation" class="mobile-nav-toggle" type="button"><span></span><span></span><span></span><em>Menu</em></button>
<nav id="primary-navigation" aria-label="Primary navigation">
<a href="{href(prefix, 'index.html')}">Home</a>
<a href="{href(prefix, 'how-we-help.html')}">How We Help</a>
<div class="nav-dropdown nav-dropdown-offerings nav-dropdown-wide">
<a class="nav-dropdown-toggle" href="{href(prefix, 'our-offerings.html')}">Our Offerings</a>
<div aria-label="Offerings and expertise sections" class="nav-dropdown-menu nav-menu-hierarchy nav-menu-offerings">
<details class="nav-menu-group">
<summary class="nav-menu-section-title">Core Offerings</summary>
<a class="nav-menu-parent" href="{href(prefix, 'our-offerings.html')}"><span>Offerings Overview</span></a>
<a class="nav-menu-child nav-menu-scorecard nav-menu-path-00" href="{href(prefix, 'dashboard-trust-scorecard.html')}"><span>Diagnostic Scorecard</span><em>Optional</em></a>
<a class="nav-menu-child nav-menu-fit-check nav-menu-path-01" href="{href(prefix, 'free-fit-check.html')}"><span>Free Fit Check</span><em>Free</em></a>
<a class="nav-menu-child nav-menu-path-02" href="{href(prefix, 'analytics-health-check.html')}"><span>Analytics Health Check</span></a>
<a class="nav-menu-child nav-menu-path-03" href="{href(prefix, 'decision-system-reset.html')}"><span>Decision System Reset</span></a>
<a class="nav-menu-child nav-menu-path-04" href="{href(prefix, 'fractional-analytics.html')}"><span>Fractional Analytics</span></a>
</details>
<details class="nav-menu-group">
<summary class="nav-menu-section-title">Expertise</summary>
<a class="nav-menu-parent" href="{href(prefix, 'expertise.html')}"><span>Expertise Overview</span></a>
<a class="nav-menu-child" href="{href(prefix, 'power-bi-consultant-cincinnati.html')}"><span>Power BI Consulting</span></a>
<a class="nav-menu-child" href="{href(prefix, 'kpi-reporting-consulting.html')}"><span>KPI Reporting</span></a>
<a class="nav-menu-child" href="{href(prefix, 'reporting-automation-consulting.html')}"><span>Reporting Automation</span></a>
<a class="nav-menu-child" href="{href(prefix, 'data-quality-review.html')}"><span>Data Quality Review</span></a>
<a class="nav-menu-child" href="{href(prefix, 'dashboard-trust-governance.html')}"><span>Dashboard Trust &amp; Governance</span></a>
<a class="nav-menu-child" href="{href(prefix, 'business-intelligence-consultant-cincinnati.html')}"><span>Data Analytics Consulting Cincinnati</span></a>
</details>
</div>
</div>
<div class="nav-dropdown nav-dropdown-intelligence">
<a class="nav-dropdown-toggle" href="{href(prefix, 'intelligence-lab.html')}">Intelligence Lab</a>
<div aria-label="Intelligence Lab services" class="nav-dropdown-menu nav-dropdown-menu-intelligence nav-menu-hierarchy">
<a class="nav-menu-parent" href="{href(prefix, 'intelligence-lab.html')}"><span>Intelligence Lab Overview</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#operations-intelligence-digest')}"><span>Operations Intelligence Digest</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#governance-rls-architecture')}"><span>Governance &amp; RLS Architecture</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#enterprise-outcome-studio')}"><span>Enterprise Outcome Studio</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#predictive-risk-intelligence')}"><span>Predictive Risk Intelligence</span></a>
</div>
</div>
<a href="{href(prefix, 'insights.html')}">Insights</a>
<a href="{href(prefix, 'about.html')}">About</a>
</nav>
</header>'''


def footer_html(prefix: str) -> str:
    return f'''<footer aria-label="Site footer" class="site-footer site-footer-refined">
  <div class="site-footer-inner">
    <div class="site-footer-col site-footer-about">
      <a class="site-footer-brand" href="{href(prefix, 'index.html')}">Parallax Data Lab</a>
      <p>Parallax Data Lab provides business intelligence consulting, Power BI dashboard development, reporting automation, and analytics support for teams that need clearer data.</p>
      <p class="site-footer-location">Cincinnati, Ohio. Based in Cincinnati and serving teams across the United States.</p>
      <a class="site-footer-email" href="#" data-mail-user="jonahnr" data-mail-domain="gmail.com" data-mail-subject="Parallax Data Lab Inquiry">Email us</a>
      <a class="site-footer-contact-button" href="{href(prefix, 'about.html#contact-us')}">Contact Parallax Data Lab</a>
    </div>
    <nav aria-label="Footer navigation" class="site-footer-col">
      <h3>Pages</h3>
      <a href="{href(prefix, 'index.html')}">Home</a>
      <a href="{href(prefix, 'how-we-help.html')}">How We Help</a>
      <a href="{href(prefix, 'our-offerings.html')}">Offerings</a>
      <a href="{href(prefix, 'expertise.html')}">Expertise</a>
      <a href="{href(prefix, 'insights.html')}">Insights</a>
      <a href="{href(prefix, 'about.html')}">About</a>
      <a href="{href(prefix, 'privacy-policy.html')}">Privacy Policy</a>
    </nav>
    <nav aria-label="Footer core work" class="site-footer-col site-footer-core-work">
      <h3>Core Work</h3>
      <a href="{href(prefix, 'free-fit-check.html')}">Free Fit Check</a>
      <a href="{href(prefix, 'analytics-health-check.html')}">Analytics Health Check</a>
      <a href="{href(prefix, 'decision-system-reset.html')}">Decision System Reset</a>
      <a href="{href(prefix, 'fractional-analytics.html')}">Fractional Analytics</a>
      <a href="{href(prefix, 'intelligence-lab.html')}">Intelligence Lab</a>
    </nav>
    <nav aria-label="Footer expertise" class="site-footer-col site-footer-intel">
      <h3>Expertise</h3>
      <a href="{href(prefix, 'expertise.html')}">Expertise Overview</a>
      <a href="{href(prefix, 'power-bi-consultant-cincinnati.html')}">Power BI Consulting</a>
      <a href="{href(prefix, 'kpi-reporting-consulting.html')}">KPI Reporting</a>
      <a href="{href(prefix, 'reporting-automation-consulting.html')}">Reporting Automation</a>
      <a href="{href(prefix, 'data-quality-review.html')}">Data Quality Review</a>
      <a href="{href(prefix, 'dashboard-trust-governance.html')}">Dashboard Trust &amp; Governance</a>
      <a href="{href(prefix, 'business-intelligence-consultant-cincinnati.html')}">Data Analytics Consulting Cincinnati</a>
    </nav>
    <div class="site-footer-col site-footer-contact">
      <h3>Contact</h3>
      <a class="site-footer-secondary" href="https://calendly.com/jonahnr/parallax-data-lab-intro-call">Book a Fit Check</a>
      <a class="site-footer-secondary" href="{href(prefix, 'about.html#contact-us')}">Contact Parallax Data Lab</a>
      <div class="site-footer-social" aria-label="Parallax Data Lab social profiles">
        {SOCIAL_SVG}
      </div>
    </div>
  </div>
  <div class="site-footer-bottom">
    <p>&copy; {YEAR} Parallax Data Lab. All rights reserved.</p>
  </div>
</footer>'''


def page_url(slug: str) -> str:
    return f"https://parallaxdatalab.com/{slug}/"


def json_ld(slug: str, data: dict) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Parallax Data Lab",
        "url": page_url(slug),
        "areaServed": ["Cincinnati", "Ohio", "United States"],
        "serviceType": data["kicker"],
        "description": data["description"],
        "sameAs": [
            "https://www.linkedin.com/company/129543938/admin/dashboard/",
            "https://www.youtube.com/@ParallaxDataLab",
            "https://www.instagram.com/parallaxdatalab/",
            "https://x.com/parallaxdatalab",
        ],
    }
    return json.dumps(payload, indent=2)


def render_page(slug: str, data: dict, prefix: str) -> str:
    cards = "\n".join(
        f'''<a class="expertise-card" href="{href(prefix, link)}">
<img alt="{alt}" src="{href(prefix, img)}" loading="lazy" decoding="async">
<div><h2>{title}</h2><p>{title} work helps teams move from scattered reporting symptoms into clearer data logic, stronger ownership, and a better path from insight to action.</p><span>Explore {title}</span></div>
</a>'''
        for title, link, img, alt in data["cards"]
    )
    proof = "\n".join(f"<span>{item}</span>" for item in data["proof"])
    sections = "\n".join(
        f'''<section class="expertise-content-block reveal-card">
<h2>{heading}</h2>
<p>{body}</p>
</section>'''
        for heading, body in data["sections"]
    )
    card_details = "\n".join(
        f'''<section class="expertise-card-detail reveal-card" id="{link[1:]}">
<div>
<p class="page-kicker">{title}</p>
<h2>{title} in practice</h2>
<p>{title} connects to the operating questions behind the report: what decision the work supports, what data can be trusted, who owns the logic, how the result will be reviewed, and what action should follow.</p>
<p>The useful version is specific, documented, and tied to leadership behavior. It should reduce repeated reconciliation, make assumptions visible, and help the team decide whether the right next step is a focused cleanup, a diagnostic, a governance reset, or a broader analytics operating model change.</p>
</div>
<img alt="{alt}" src="{href(prefix, img)}" loading="lazy" decoding="async">
</section>'''
        for title, link, img, alt in data["cards"]
        if link.startswith("#")
    )
    service_blocks = ""
    if data.get("service_blocks"):
        service_blocks = '<section class="expertise-detail-grid reveal-card" aria-label="Specific consulting focus areas">\n' + "\n".join(
            f'<article id="service-{title.lower().replace(" ", "-").replace("&", "and")}"><strong>{title}</strong><p>{body}</p></article>'
            for title, body in data["service_blocks"]
        ) + "\n</section>"
    articles = "\n".join(
        f'''<a class="expertise-article-card" href="{href(prefix, link)}">
<span>Related Insight</span>
<strong>{title}</strong>
<em>Read article</em>
</a>'''
        for title, link in data.get("articles", [])
    )
    article_section = ""
    if articles:
        article_section = f'''<section class="expertise-related-articles reveal-card" aria-labelledby="related-articles-title">
<p class="page-kicker">Related Reading</p>
<h2 id="related-articles-title">Articles that go deeper on this problem.</h2>
<div class="expertise-article-grid">
{articles}
</div>
</section>'''
    faq = "\n".join(f"<article><h3>{q}</h3><p>{a}</p></article>" for q, a in data["faq"])
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{data["title"]}</title>
<meta name="description" content="{data["description"]}"/>
<link rel="canonical" href="{page_url(slug)}"/>
<link href="{href(prefix, f'home.css?v={VERSION}')}" rel="stylesheet"/>
<meta name="theme-color" content="#0b1745"/>
<link rel="icon" href="{href(prefix, 'favicon.ico')}" sizes="any"/>
<link rel="icon" type="image/png" href="{href(prefix, 'favicon.png')}"/>
<link rel="apple-touch-icon" href="{href(prefix, 'apple-touch-icon.png')}"/>
<meta content="website" property="og:type"/>
<meta content="Parallax Data Lab" property="og:site_name"/>
<meta property="og:title" content="{data["title"]}"/>
<meta property="og:description" content="{data["description"]}"/>
<meta property="og:url" content="{page_url(slug)}"/>
<meta property="og:image" content="https://parallaxdatalab.com/assets/social-preview.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{data["title"]}"/>
<meta name="twitter:description" content="{data["description"]}"/>
<meta name="twitter:image" content="https://parallaxdatalab.com/assets/social-preview.png"/>
<script type="application/ld+json">{json_ld(slug, data)}</script>
</head>
<body>
<canvas aria-hidden="true" id="constellation"></canvas>
{nav_html(prefix)}
<main class="expertise-page">
<section class="expertise-hero" aria-labelledby="expertise-title">
<div class="expertise-hero-copy motion-layer" data-depth="0.06">
<p class="page-kicker">{data["kicker"]}</p>
<h1 id="expertise-title">{data["h1"]}</h1>
<p>{data["intro"]}</p>
<div class="local-seo-proof" aria-label="{data["kicker"]} focus areas">
{proof}
</div>
<div class="hero-actions">
<a class="primary-action" href="{href(prefix, 'free-fit-check.html')}">Book a Fit Check</a>
<a class="secondary-action" href="{href(prefix, 'our-offerings.html')}">Compare Offerings</a>
</div>
</div>
<figure class="expertise-hero-media motion-layer" data-depth="-0.04">
<img alt="{data["hero_alt"]}" src="{href(prefix, data["hero_image"])}" decoding="async">
</figure>
</section>
{sections}
<section class="expertise-card-section reveal-card" aria-label="{data["kicker"]} related expertise">
<h2>Related Expertise</h2>
<div class="expertise-card-grid">
{cards}
</div>
</section>
{card_details}
{service_blocks}
{article_section}
<section class="expertise-faq-section reveal-card" aria-labelledby="expertise-faq-title">
<p class="page-kicker">Questions</p>
<h2 id="expertise-faq-title">What teams usually ask.</h2>
<div class="local-seo-faq-grid">
{faq}
</div>
</section>
<section class="local-seo-cta reveal-card" aria-labelledby="expertise-cta-title">
<p class="page-kicker">Start with fit</p>
<h2 id="expertise-cta-title">Not sure which expertise path fits your reporting problem?</h2>
<p>Start with the free Fit Check. The goal is to route the problem to the smallest useful next step, whether that is a focused expertise review or a broader offering.</p>
<a class="primary-action" href="{href(prefix, 'free-fit-check.html')}">Book a Fit Check</a>
</section>
</main>
{footer_html(prefix)}
<script src="{href(prefix, f'home.js?v={VERSION}')}"></script>
</body>
</html>
'''
    return template


def rewrite_global_blocks(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    original = text
    prefix = prefix_for(path)
    text = re.sub(r"<header aria-label=\"Parallax site navigation\" class=\"site-header\">.*?</header>", nav_html(prefix), text, count=1, flags=re.S)
    text = re.sub(r"<footer aria-label=\"Site footer\" class=\"site-footer site-footer-refined\">.*?</footer>", footer_html(prefix), text, count=1, flags=re.S)
    text = re.sub(r"home\.css\?v=\d+", f"home.css?v={VERSION}", text)
    text = re.sub(r"home\.js\?v=\d+", f"home.js?v={VERSION}", text)
    if path.name == "how-we-help.html" or path.as_posix().endswith("/how-we-help/index.html"):
        text = update_how_we_help(text, prefix)
    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")


def update_how_we_help(text: str, prefix: str) -> str:
    pattern = r'<section class="help-section expertise-path-section[^"]* reveal-card" id="platform-local-expertise">.*?</section>'
    replacement = f'''<section class="help-section expertise-path-section expertise-path-section-wide reveal-card" id="platform-local-expertise">
<h2>Platform And Local Expertise</h2>
<p class="help-lede">The core offerings remain the main engagement ladder. The Expertise hub organizes platform, KPI, automation, data quality, dashboard governance, and Cincinnati analytics paths for teams that arrive with a specific problem in mind.</p>
<div class="expertise-path-grid expertise-path-grid-wide">
<a class="expertise-path-card" href="{href(prefix, 'expertise.html')}">
<img alt="Analytics expertise hub connecting Power BI KPI reporting automation and data quality" class="help-card-image" src="{href(prefix, 'assets/home-generated/help-foundation-to-intelligence-advanced.png')}" loading="lazy" decoding="async">
<div>
<p class="page-kicker">Expertise Hub</p>
<h3>Explore Analytics Expertise</h3>
<p>Use this hub when the question is about a specific capability: Power BI, KPI reporting, reporting automation, data quality review, dashboard trust, governance, or data analytics consulting in Cincinnati.</p>
<span>Open Expertise</span>
</div>
</a>
<a class="expertise-path-card" href="{href(prefix, 'power-bi-consultant-cincinnati.html')}">
<img alt="Power BI dashboard and semantic model consulting path" class="help-card-image" src="{href(prefix, 'assets/home-generated/power-bi-logo-reference.png')}" loading="lazy" decoding="async">
<div>
<p class="page-kicker">Platform Expertise</p>
<h3>Power BI Consulting</h3>
<p>For teams that need dashboard cleanup, semantic model improvement, DAX review, KPI reporting, refresh reliability, row-level security, or reporting automation around Power BI.</p>
<span>Explore Power BI consulting</span>
</div>
</a>
<a class="expertise-path-card" href="{href(prefix, 'business-intelligence-consultant-cincinnati.html')}">
<img alt="Cincinnati skyline representing local business intelligence consulting" class="help-card-image" src="{href(prefix, 'assets/home-generated/cincinnati-skyline-hero.jpg')}" loading="lazy" decoding="async">
<div>
<p class="page-kicker">Local Expertise</p>
<h3>Data Analytics Consulting Cincinnati</h3>
<p>For Cincinnati and Midwest teams that need practical data analytics support around KPI reporting, manufacturing and operations analytics, dashboard trust, and data quality.</p>
<span>Explore data analytics consulting in Cincinnati</span>
</div>
</a>
</div>
</section>'''
    return re.sub(pattern, replacement, text, count=1, flags=re.S)


def write_pages() -> None:
    for slug, data in PAGES.items():
        flat = ROOT / f"{slug}.html"
        flat.write_text(render_page(slug, data, ""), encoding="utf-8", newline="\n")
        clean_dir = ROOT / slug
        clean_dir.mkdir(exist_ok=True)
        (clean_dir / "index.html").write_text(render_page(slug, data, "../"), encoding="utf-8", newline="\n")


def update_redirects() -> None:
    redirects = ROOT / "_redirects"
    text = redirects.read_text(encoding="utf-8") if redirects.exists() else ""
    lines = text.splitlines()
    existing = set(lines)
    additions = []
    for slug in PAGES:
        for line in (f"/{slug} /{slug}/ 301", f"/{slug}.html /{slug}/ 301"):
            if line not in existing:
                additions.append(line)
    if additions:
        lines.extend(additions)
        redirects.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_sitemap() -> None:
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    urls = set(re.findall(r"<loc>https://parallaxdatalab.com/([^<]+)</loc>", text))
    insert = ""
    for slug in PAGES:
        key = f"{slug}/"
        if key not in urls:
            insert += f"""  <url>
    <loc>https://parallaxdatalab.com/{slug}/</loc>
    <lastmod>2026-06-16</lastmod>
  </url>
"""
    if insert:
        text = text.replace("</urlset>", insert + "</urlset>")
        sitemap.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    write_pages()
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        rewrite_global_blocks(path)
    update_redirects()
    update_sitemap()


if __name__ == "__main__":
    main()

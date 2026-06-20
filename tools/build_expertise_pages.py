from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YEAR = "2026"
VERSION = "163"


SOCIAL_SVG = """<a class="site-social-link site-social-linkedin" href="https://www.linkedin.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.1 8.4h3.8v11.5H5.1V8.4Zm1.9-5.7a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4Zm4.1 5.7h3.6v1.6h.1c.5-.9 1.7-1.9 3.5-1.9 3.7 0 4.4 2.4 4.4 5.6v6.2h-3.8v-5.5c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9v5.6h-3.8V8.4Z"/></svg></a>
        <a class="site-social-link site-social-youtube" href="https://www.youtube.com/@ParallaxDataLab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 7.1a3 3 0 0 0-2.1-2.1C18 4.5 12 4.5 12 4.5s-6 0-7.9.5A3 3 0 0 0 2 7.1 31.6 31.6 0 0 0 1.5 12c0 1.7.2 3.4.5 4.9A3 3 0 0 0 4.1 19c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1c.3-1.5.5-3.2.5-4.9s-.2-3.4-.5-4.9ZM10 15.2V8.8l5.6 3.2-5.6 3.2Z"/></svg></a>
        <a class="site-social-link site-social-instagram" href="https://www.instagram.com/parallaxdatalab/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.2 2.8h9.6a4.4 4.4 0 0 1 4.4 4.4v9.6a4.4 4.4 0 0 1-4.4 4.4H7.2a4.4 4.4 0 0 1-4.4-4.4V7.2a4.4 4.4 0 0 1 4.4-4.4Zm0 2A2.4 2.4 0 0 0 4.8 7.2v9.6a2.4 2.4 0 0 0 2.4 2.4h9.6a2.4 2.4 0 0 0 2.4-2.4V7.2a2.4 2.4 0 0 0-2.4-2.4H7.2Zm4.8 3a4.2 4.2 0 1 1 0 8.4 4.2 4.2 0 0 1 0-8.4Zm0 2a2.2 2.2 0 1 0 0 4.4 2.2 2.2 0 0 0 0-4.4Zm4.6-2.9a1 1 0 1 1 0 2.1 1 1 0 0 1 0-2.1Z"/></svg></a>
        <a class="site-social-link site-social-x" href="https://x.com/parallaxdatalab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on X"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.8 10.4 21.1 2h-1.7l-6.3 7.2L8 2H2.2l7.7 11-7.7 9h1.7l6.8-7.8 5.5 7.8H22l-8.2-11.6Zm-2.4 2.8-.8-1.1L4.4 3.3h2.8l5 7.1.8 1.1 6.5 9.2h-2.8l-5.3-7.5Z"/></svg></a>"""


PAGES = {
    "expertise": {
        "title": "Analytics Expertise | Strategy, Architecture & Trusted BI",
        "description": "Explore Parallax Data Lab expertise in Power BI, KPI strategy, reporting automation, data reliability, BI governance, and analytics architecture.",
        "kicker": "Analytics Expertise",
        "h1": "Expertise for the reporting problems that sit underneath the dashboard request.",
        "intro": "Some teams arrive with a broad reporting problem. Others know the pain by name: Power BI reports are hard to trust, KPI strategy has drifted, manual reporting eats too much time, data reliability breaks confidence, or the underlying integration and analytics architecture can no longer scale.",
        "hero_image": "assets/home-generated/help-foundation-to-intelligence-advanced.webp",
        "hero_alt": "Analytics expertise map connecting Power BI reporting data quality and governance",
        "proof": ["Power BI", "KPI Strategy", "Reporting Automation", "Data Reliability", "Analytics Architecture"],
        "sections": [
            ("Where Reporting Problems Usually Start", "A dashboard request often starts with the symptom instead of the cause. One team may ask for a cleaner Power BI report because the executive view is too busy. Another may ask for automation because a recurring spreadsheet takes five hours every Monday. Another may ask for a data quality review because sales, finance, and operations keep showing different answers for the same metric. The expertise pages separate those patterns so the work starts with the real constraint, not the loudest surface complaint."),
            ("What Connects The Work", "The common thread is trust in the operating number. Reports earn that trust when the data path is understandable, metric definitions are owned, the reporting layer answers a real business question, and the review cadence turns the number into action. The platform still matters, but the business layer above it matters more: source logic, ownership, governance, automation readiness, and the decision rhythm leaders actually use."),
            ("How To Choose The Right Path", "Start with the pain that keeps repeating. If leaders debate the number, KPI reporting or data quality is usually the better entry point. If the report works but the Power BI model is fragile, start with platform expertise. If manual work is consuming analyst time, start with automation readiness. If every team has its own version of the truth, dashboard trust and governance should come first.")
        ],
        "cards": [
            ("Power BI Consulting", "power-bi-consultant-cincinnati.html", "assets/home-generated/power-bi-report-hero.jpg", "Power BI dashboard and semantic model consulting"),
            ("KPI Strategy & Executive Reporting", "kpi-reporting-consulting.html", "assets/home-generated/power-bi-cincinnati-kpi-governance.jpg", "KPI strategy and executive reporting workflow"),
            ("Reporting Automation", "reporting-automation-consulting.html", "assets/home-generated/power-bi-cincinnati-data-quality.jpg", "Reporting automation pipeline for trusted business reporting"),
            ("Data Quality & Reporting Reliability", "data-quality-review.html", "assets/home-generated/failure-source-of-truth.webp", "Data quality and reporting reliability review"),
            ("BI Governance & Dashboard Trust", "dashboard-trust-governance.html", "assets/home-generated/help-situation-dashboard-trust.webp", "BI governance and dashboard trust system"),
            ("Data Integration & Analytics Architecture", "data-integration-analytics-architecture.html", "assets/home-generated/help-foundation-to-intelligence-advanced.webp", "Integrated data and analytics architecture")
        ],
        "faq": [
            ("Should expertise pages replace offerings?", "No. The offering pages remain the product ladder. Expertise pages clarify capability, symptoms, and fit, then route the visitor to the right starting point."),
            ("Why not put everything on one services page?", "A single broad services page gets muddy quickly. Separate expertise pages let each topic show the symptoms, examples, related articles, and practical next steps a buyer needs."),
            ("How do these pages stay useful?", "Each page is built around real buyer problems, operating symptoms, examples, and decision paths, so visitors can understand what kind of help fits before booking a call."),
            ("Can multiple expertise areas be combined?", "Yes. Reporting problems often cross KPI logic, platform design, data reliability, governance, and automation. The Fit Check helps identify the smallest combination that addresses the real constraint.")
        ],
        "articles": [
            ("Why Nobody Trusts Your Dashboard", "insights/why-nobody-trusts-your-dashboard.html"),
            ("The Difference Between Reporting And Decision Making", "insights/the-difference-between-reporting-and-decision-making.html"),
            ("Analytics Maturity Roadmap", "insights/analytics-maturity-roadmap-reporting-to-decision-systems.html"),
        ],
        "card_blurbs": {
            "Power BI Consulting": "Use this path when the report layer is visible, but the real work may be model structure, DAX logic, refresh behavior, KPI definition, or report governance.",
            "KPI Strategy & Executive Reporting": "Use this path when leaders have metrics but not shared meaning, ownership, thresholds, or an executive reporting cadence that turns movement into action.",
            "Reporting Automation": "Use this path when recurring report assembly is wasting time and the team needs to decide what can safely repeat before automation scales the work.",
            "Data Quality & Reporting Reliability": "Use this path when people keep reconciling the same numbers, tracing exceptions, or explaining why dashboards and spreadsheets do not agree.",
            "BI Governance & Dashboard Trust": "Use this path when there are too many reports, unclear certified sources, loose access rules, and no practical change process for BI assets.",
            "Data Integration & Analytics Architecture": "Use this path when disconnected sources, brittle pipelines, unclear data layers, and scaling constraints are limiting analytics reliability."
        },
    },
    "data-integration-analytics-architecture": {
        "title": "Data Integration & Analytics Architecture Consulting",
        "description": "Data integration and analytics architecture consulting for reliable pipelines, scalable models, governed reporting layers, and AI-ready business data.",
        "kicker": "Data Integration & Analytics Architecture",
        "h1": "Build an analytics architecture that can scale without multiplying confusion.",
        "intro": "Reliable dashboards depend on what happens before the visual layer. Parallax helps teams connect source systems, design ingestion and transformation patterns, establish reusable business entities and semantic models, govern security and lineage, and build an architecture that supports reporting today without blocking automation, predictive analytics, or AI tomorrow.",
        "hero_image": "assets/home-generated/help-foundation-to-intelligence-advanced.webp",
        "hero_alt": "Connected data integration and analytics architecture from source systems to decision-ready reporting",
        "proof": ["Source Integration", "Data Modeling", "Pipeline Reliability", "Semantic Layers", "AI Readiness"],
        "sections": [
            ("Where Architecture Breaks", "Architecture debt shows up as slow refreshes, copied transformations, fragile joins, manual extracts, and reports that cannot explain where a number came from. Each new source or business unit adds another exception until reporting changes feel risky."),
            ("What A Practical Architecture Includes", "The right design identifies systems of record, ingestion patterns, transformation ownership, reusable business entities, semantic definitions, quality checks, security boundaries, and the reporting or intelligence products each layer needs to support."),
            ("How Parallax Helps", "Parallax maps the current data path, separates urgent reliability fixes from longer-term architecture work, and designs the smallest scalable target state. The goal is not more infrastructure. It is a dependable path from operational systems to trusted decisions.")
        ],
        "approach_heading": "Design the smallest architecture that removes today’s bottlenecks and supports tomorrow’s reporting",
        "use_case_heading": "When integration and architecture work becomes necessary",
        "use_cases": [
            ("Disconnected operational systems", "ERP, CRM, finance, service, manufacturing, and customer platforms feed reports through separate extracts with no governed integration path."),
            ("Copied transformation logic", "The same customer, revenue, product, or status logic is rebuilt in spreadsheets, pipelines, semantic models, and dashboards."),
            ("Fragile refresh dependencies", "Reports depend on undocumented jobs, personal credentials, manual file drops, or timing assumptions that fail silently."),
            ("Scaling across entities or regions", "New business units, facilities, products, or acquisitions multiply mappings and exceptions faster than the current design can absorb."),
            ("Fabric or cloud modernization", "The organization needs a practical migration path across OneLake, lakehouse, warehouse, pipelines, semantic models, workspaces, security, and capacity."),
            ("Predictive and AI readiness", "Advanced use cases need governed training data, reusable features, traceable definitions, security boundaries, monitoring, and trusted delivery into business workflows.")
        ],
        "cards": [
            ("Source & Integration Map", "#source-integration-map", "assets/home-generated/failure-source-of-truth.webp", "Source systems connected through a clear integration map"),
            ("Analytics Model Design", "#analytics-model-design", "assets/home-generated/power-bi-cincinnati-bi-model.webp", "Reusable analytics model supporting governed reporting"),
            ("Reliability & AI Readiness", "#reliability-ai-readiness", "assets/home-generated/help-foundation-to-intelligence-advanced.webp", "Reliable analytics foundation prepared for automation and AI")
        ],
        "service_blocks": [
            ("Source System Inventory", "Document systems of record, extract paths, owners, refresh expectations, and known gaps."),
            ("Integration Pattern Review", "Choose practical batch, API, event, or managed integration patterns based on business need and operating capacity."),
            ("Analytics Model Design", "Create reusable entities, facts, dimensions, metric logic, and semantic layers that reduce duplication."),
            ("Pipeline Reliability", "Add monitoring, quality checks, failure ownership, and recovery expectations to critical data paths."),
            ("Security & Governance", "Clarify access boundaries, sensitive data handling, certified layers, and change control."),
            ("Migration And Delivery Roadmap", "Sequence domains, sources, pipelines, models, testing, cutover, ownership, and adoption so architecture change creates usable reporting early."),
            ("AI Readiness", "Prepare governed datasets, reusable features, metadata, security, quality controls, and monitoring for predictive or AI-enabled use cases.")
        ],
        "delivery_examples": {
            "Source System Inventory": "A source register documents systems of record, owners, entities, extraction method, expected availability, sensitive fields, consumers, and known reliability gaps.",
            "Integration Pattern Review": "A decision matrix compares batch, API, event, managed connector, and file-based patterns against latency, volume, control, skills, cost, and recovery needs.",
            "Analytics Model Design": "A target model defines reusable customer, product, account, event, and location entities with facts, dimensions, keys, grain, history, and semantic relationships.",
            "Pipeline Reliability": "A pipeline control design adds freshness checks, quality gates, failure alerts, retry and recovery behavior, ownership, and downstream impact visibility.",
            "Security & Governance": "A data-product control sheet documents classification, workspace or layer, permissions, lineage, certification, retention, and change approval.",
            "Migration And Delivery Roadmap": "A phased roadmap sequences one reporting domain through ingestion, modeling, validation, semantic delivery, cutover, adoption, and pattern reuse.",
            "AI Readiness": "A readiness package identifies governed training or retrieval datasets, reusable features, metadata, access rules, evaluation cases, monitoring, and responsible-use boundaries."
        },
        "case_study_heading": "Two integration case studies showing different architecture paths",
        "case_studies": [
            {
                "title": "Integrating disconnected ERP, CRM, and service data into a governed reporting domain",
                "situation": "An anonymized organization produced finance, sales, and service reporting from separate extracts. Customer and product identifiers did not align, transformations were copied between reports, and each refresh depended on undocumented timing assumptions.",
                "failure": "There was no governed integration path or reusable business entity layer. Reports reconciled sources differently, pipeline failures were difficult to trace, and adding a new business unit multiplied mappings and manual work.",
                "work": "Parallax inventoried systems and owners, defined source contracts and extraction patterns, created conformed customer and product mappings, designed reporting facts and dimensions, implemented quality gates and failure ownership, and delivered the first governed domain through a reusable semantic model.",
                "outcome": "Finance, sales, and service reporting inherited the same entity definitions and integration controls. New reporting work reused the governed domain instead of rebuilding extracts and reconciliation logic.",
                "artifact": "Source inventory, system-of-record decisions, integration diagram, conformed entity model, mapping rules, quality gates, pipeline monitor, semantic model, and domain rollout roadmap."
            },
            {
                "title": "Designing a Fabric migration path without forcing a big-bang platform rewrite",
                "situation": "An existing Power BI estate had growing source volume, duplicated dataflows and semantic logic, limited lineage, and interest in OneLake, lakehouse patterns, Direct Lake, and governed predictive workloads.",
                "failure": "The organization had a platform goal but no domain sequence, capacity model, workspace design, migration criteria, security plan, or definition of which existing Power BI assets should remain in place.",
                "work": "Parallax assessed workloads and skills, selected a pilot reporting domain, designed OneLake and lakehouse or warehouse boundaries, mapped pipelines and Direct Lake semantics, established workspace, capacity, security, deployment, and monitoring standards, and created coexistence and cutover criteria.",
                "outcome": "The team gained a staged modernization path that produced an early governed data product while preserving useful Power BI assets and creating reusable standards for later domains, predictive models, and AI agents.",
                "artifact": "Fabric readiness assessment, target architecture, domain prioritization matrix, workspace and capacity plan, security model, pilot backlog, migration waves, acceptance criteria, and operating handoff."
            }
        ],
        "service_heading": "Architecture deliverables that move from current-state clarity into implementation",
        "service_intro": "The work can begin with one reporting domain, but it is designed to leave reusable patterns: source contracts, integration standards, modeled business entities, semantic logic, quality gates, security boundaries, deployment paths, and clear operational ownership.",
        "modern_callout": ("Architecture should make trusted data products easier to build and govern.", "A modern platform is valuable when it reduces duplicate logic, makes lineage and quality visible, gives teams reusable governed data products, and supports Power BI, automation, predictive models, and AI agents through the same controlled foundation."),
        "show_card_details": False,
        "faq": [
            ("Do we need a new data platform?", "Not necessarily. The first step is understanding what the current stack can support and where the real constraints are before recommending a platform change."),
            ("Can this start with one reporting domain?", "Yes. Finance, operations, revenue, or customer reporting can provide a focused starting point while establishing patterns the rest of the architecture can reuse."),
            ("Is this only for large data teams?", "No. Smaller teams often benefit most from a deliberately simple architecture because they cannot afford constant reconciliation and pipeline firefighting."),
            ("Can this include Microsoft Fabric implementation?", "Yes. The work can cover readiness, OneLake, lakehouse or warehouse design, pipelines, Direct Lake semantic models, workspaces, capacity, governance, migration sequencing, and operational handoff.")
        ],
        "articles": [
            ("Prepare Your Reporting Environment for AI", "insights/prepare-reporting-environment-for-ai.html"),
            ("The Single Source of Truth Myth", "insights/single-source-of-truth-myth.html"),
            ("Analytics Maturity Roadmap", "insights/analytics-maturity-roadmap-reporting-to-decision-systems.html")
        ],
        "card_details": {
            "Source & Integration Map": ["Map each critical source, transfer, transformation, owner, refresh expectation, and consuming report so hidden dependencies become visible.", "The result identifies brittle handoffs, duplicate extracts, missing controls, and the smallest integration changes that improve reliability."],
            "Analytics Model Design": ["Design reusable business entities and reporting models around how the organization measures customers, revenue, operations, capacity, and performance.", "This reduces copied logic and gives dashboards, automation, and advanced analysis a governed starting point."],
            "Reliability & AI Readiness": ["Add the monitoring, quality gates, lineage, and ownership needed to keep critical data products dependable.", "Once the foundation is stable, teams can evaluate predictive and AI-enabled use cases without scaling unreliable inputs."]
        }
    },
    "kpi-reporting-consulting": {
        "title": "KPI Strategy & Executive Reporting Consulting",
        "description": "KPI strategy and executive reporting consulting for clearer metric definitions, ownership, reporting cadence, dashboard trust, and decision-ready scorecards.",
        "kicker": "KPI Strategy & Executive Reporting",
        "h1": "KPI reporting consulting for metrics leaders can trust and act on.",
        "intro": "Parallax turns scattered measures into a working executive reporting system: a governed KPI layer, an executive scorecard, an automated reporting workflow, and documentation that makes definitions, ownership, thresholds, and follow-up clear.",
        "hero_image": "assets/home-generated/power-bi-cincinnati-kpi-governance.jpg",
        "hero_alt": "KPI reporting governance dashboard with trusted executive metrics",
        "proof": ["KPI Definitions", "Metric Ownership", "Executive Cadence", "Scorecards", "Dashboard Trust"],
        "sections": [
            ("From KPI alignment to a working reporting system", "Parallax does more than facilitate metric conversations. We define and govern the metric layer, build the executive scorecard, automate the reporting workflow, document calculation and ownership rules, and connect the output to the meeting cadence where leaders act."),
            ("How Parallax helps", "The engagement can begin with one scorecard or expand across a leadership reporting portfolio. We identify definition drift, assign owners, build governed measures and reporting views, automate repeatable preparation and distribution, and leave the team with operating documentation that supports ongoing use."),
            ("The result", "Leaders receive a smaller, governed metric set with accurate calculations, visible owners, consistent reporting logic, and a scorecard cadence that directs attention to material movement and accountable action.")
        ],
        "use_case_heading": "KPI reporting for the decisions leaders make repeatedly",
        "use_cases": [
            ("Executive reporting", "A concise leadership scorecard with trend, target, confidence, owner, commentary, and the decision or action each exception should trigger."),
            ("Financial performance", "Governed revenue, margin, cash, forecast, and variance logic aligned across finance systems and executive reporting."),
            ("Operations", "Throughput, backlog, capacity, quality, and service measures connected to operating thresholds and accountable owners."),
            ("Sales performance", "Pipeline, conversion, bookings, retention, and customer measures built from consistent definitions and a repeatable reporting workflow."),
            ("Compliance and risk", "Controlled scorecards that document source, calculation, evidence, owner, review cadence, and exception follow-up.")
        ],
        "modern_callout": ("Trustworthy AI reporting starts with governed KPI logic.", "Copilot and AI reporting are only dependable when KPI definitions are consistent, semantic logic is reusable, owners are clear, metadata is understandable, and access rules are enforced. Governing the metric layer improves both human reporting and AI-generated answers."),
        "show_card_details": False,
        "cards": [
            ("Metric Definition Review", "#metric-definition-review", "assets/home-generated/quote-useful-metrics.webp", "Useful KPI definitions organized for leadership reporting"),
            ("Ownership Mapping", "#ownership-mapping", "assets/home-generated/quote-ownership-definitions.webp", "Metric ownership definitions for KPI governance"),
            ("Executive Scorecard Design", "#executive-scorecard-design", "assets/home-generated/help-outcome-renewed-confidence.webp", "Executive scorecard showing renewed trust in reporting")
        ],
        "service_blocks": [
            ("Metric Definition Review", "Clarify calculations, source systems, timing, exclusions, and interpretation rules for the KPIs that drive decisions."),
            ("Ownership Mapping", "Name who owns each metric, who can approve changes, and who explains movement when leadership asks why."),
            ("Executive Scorecard Build", "Build the executive scorecard or dashboard with trend, target, owner, confidence, commentary, and action context."),
            ("Governed Metric Layer", "Implement reusable KPI logic in the semantic or reporting layer so scorecards and downstream reports use consistent definitions."),
            ("Automated Reporting Workflow", "Automate repeatable preparation, refresh, quality checks, and distribution for the executive reporting cycle."),
            ("KPI Documentation", "Deliver definition records, source and calculation notes, owners, thresholds, limitations, and change-control guidance."),
            ("Cadence Alignment", "Connect the reporting cycle to operating meetings so metrics create action instead of passive status updates."),
            ("Power BI KPI Cleanup", "Refactor measures, labels, pages, and semantic-model logic when Power BI is the main reporting layer."),
            ("Decision Thresholds", "Define what movement matters, what is noise, and when the team should escalate or act.")
        ],
        "delivery_examples": {
            "Metric Definition Review": "A KPI record compares the current calculation with the intended business rule, source grain, time zone, exclusions, refresh timing, and expected decision use.",
            "Ownership Mapping": "An ownership matrix separates the business definition owner, technical logic owner, source owner, and action owner for every priority KPI.",
            "Executive Scorecard Build": "A leadership view shows current value, target, trend, confidence, owner, commentary, and the action expected when a threshold is crossed.",
            "Governed Metric Layer": "Certified measures move repeated KPI logic into one governed semantic layer used by scorecards and downstream reports.",
            "Automated Reporting Workflow": "A scheduled workflow prepares the data, validates completeness, refreshes the scorecard, and distributes the approved view on the leadership cadence.",
            "KPI Documentation": "A searchable metric catalog records calculation logic, sources, timing, grain, inclusions, exclusions, limitations, owners, and change history.",
            "Cadence Alignment": "A weekly or monthly review agenda connects each metric exception to a decision, owner, due point, and escalation path.",
            "Power BI KPI Cleanup": "Duplicated measures are reconciled, labels and formats standardized, model logic simplified, and deprecated report-level calculations removed.",
            "Decision Thresholds": "A threshold table distinguishes normal variation, watch conditions, intervention triggers, and the business response expected at each level."
        },
        "case_study_heading": "Case study: correcting a KPI distorted by time-zone logic",
        "case_studies": [{
            "title": "Standardizing event time so operational counts reflected the real business day",
            "situation": "An operational KPI counted completed events by calendar date, but the source timestamps were stored in UTC while the business reviewed performance in local time. Events near midnight were assigned to the wrong operating day, producing inconsistent daily counts across source extracts and leadership reports.",
            "failure": "The report grouped the raw timestamp without applying the approved business time zone and daylight-saving rules. Different analysts also converted time at different stages, so otherwise identical reports could disagree.",
            "work": "Parallax traced the timestamp from source through transformation and semantic logic, confirmed the business calendar and time-zone requirement, created one standardized local event timestamp in the governed data layer, rebuilt the KPI against that field, documented late-arriving-event handling, and validated boundary cases around midnight and daylight-saving transitions.",
            "outcome": "The KPI represented the correct local operating day, daily counts reconciled across reports, and future measures inherited one documented time standard instead of repeating report-level conversions.",
            "artifact": "Time-zone decision record, UTC-to-local transformation specification, boundary-case validation table, corrected KPI definition, owner approval, and before/after reconciliation view."
        }],
        "faq": [
            ("Do we need new KPIs or cleaner existing KPIs?", "Usually the first step is cleaning the existing set. Most teams already have enough metrics; they need fewer disputes, clearer definitions, and stronger ownership."),
            ("Can KPI reporting work happen without Power BI?", "Yes. The work applies to Power BI, spreadsheets, CRM exports, operating reports, or executive scorecards. The platform matters, but the metric logic matters more."),
            ("Where does this fit with Decision System Reset?", "KPI reporting can be a focused expertise path. Decision System Reset is broader when the metric, dashboard, ownership, and operating cadence all need to be redesigned together."),
            ("Will Parallax build the scorecard and reporting workflow?", "Yes. The work can include governed KPI logic, scorecard development, automated refresh and distribution, testing, and documentation—not only alignment workshops.")
        ],
        "articles": [
            ("How To Build Metrics People Actually Use", "insights/how-to-build-metrics-people-actually-use.html"),
            ("KPI Governance Explained For Growing Organizations", "insights/kpi-governance-explained-growing-organizations.html"),
            ("The KPI Ownership Framework Every Leadership Team Needs", "insights/kpi-ownership-framework-every-leadership-team-needs.html"),
        ],
        "card_blurbs": {
            "Metric Definition Review": "Clarifies the calculation, timing, exclusions, grain, source, and business interpretation for metrics leaders keep challenging.",
            "Ownership Mapping": "Names who owns the definition, who approves changes, who explains movement, and who is accountable for the response.",
            "Executive Scorecard Design": "Turns a scattered metric set into a leadership view with trend, target, confidence, context, and next-action clarity."
        },
        "card_details": {
            "Metric Definition Review": ["A definition review is useful when the same KPI appears in multiple dashboards or spreadsheets with slightly different math. The work compares the calculation against source data, timing rules, exclusions, and the decision the metric is supposed to support.", "The output is a practical definition record: source, grain, owner, refresh cadence, business rule, known limitations, and when the metric should trigger attention."],
            "Ownership Mapping": ["Ownership mapping separates technical ownership from business ownership. The person who maintains a dataset may not be the person who can approve a change to revenue logic, service-level rules, or inventory classification.", "This prevents metric changes from drifting through side conversations and gives leaders a clear escalation path when a KPI is disputed."],
            "Executive Scorecard Design": ["A scorecard should not be a warehouse of every available measure. It should show the few measures that matter for a recurring leadership decision and include enough context to make interpretation faster.", "That usually means trend, target, threshold, owner, commentary, confidence, and a clear link to the action path for exceptions."]
        },
    },
    "reporting-automation-consulting": {
        "title": "Reporting Automation Consulting | Faster Trusted Reporting",
        "description": "Reporting automation consulting for teams that want to reduce manual reporting, improve refresh reliability, protect data quality, and automate recurring analytics workflows.",
        "kicker": "Reporting Automation",
        "h1": "Reporting automation consulting that replaces manual work without sacrificing trust.",
        "intro": "Parallax designs and implements automated reporting workflows—from data preparation and scheduled refreshes to replacement dashboards, exception alerts, distribution, monitoring, and documented handoff.",
        "hero_image": "assets/home-generated/power-bi-cincinnati-data-quality.jpg",
        "hero_alt": "Reporting automation pipeline turning source data into trusted dashboards",
        "proof": ["Manual Reporting", "Refresh Reliability", "Workflow Design", "Data Quality", "Decision Cadence"],
        "sections": [
            ("How Parallax implements automation", "We map the current workflow, stabilize the business rules that must repeat, then build the new operating path. Delivery can include automated pipelines, rebuilt transformations, replacement dashboards, monitored refreshes, exception alerts, scheduled distribution, and handoff procedures the internal team can maintain."),
            ("What stays human", "Automation handles repeatable preparation, checking, refresh, and distribution. Judgment stays visible where teams must explain exceptions, approve changes, interpret context, or decide what action follows."),
            ("The result", "The reporting cycle becomes one monitored workflow with fewer handoffs, consistent business logic, visible exceptions, dependable delivery, and documentation the internal team can support.")
        ],
        "use_case_heading": "Reporting workflows Parallax can automate",
        "use_cases": [
            ("Recurring executive reporting", "Automate source preparation, scorecard refresh, quality checks, commentary inputs, and distribution for weekly or monthly leadership reviews."),
            ("Excel-to-dashboard workflows", "Replace export, lookup, pivot, copy-paste, and manual formatting steps with a governed pipeline and maintained reporting view."),
            ("Scheduled Power BI refreshes", "Configure dependable refresh schedules, dependency checks, failure alerts, and owner response paths."),
            ("Monthly operating packs", "Build a repeatable close-to-pack workflow with consistent definitions, sections, review timing, and controlled distribution."),
            ("Exception and quality alerts", "Surface late data, missing records, threshold breaches, refresh failures, and other exceptions before the report reaches leaders."),
            ("Automated distribution", "Deliver the right report, snapshot, or exception summary to the right audience on the correct cadence with documented access rules.")
        ],
        "modern_callout": ("Repeatable reporting creates a stronger foundation for AI agents.", "Clean inputs, stable logic, explicit exception rules, monitored workflows, and documented handoffs give AI agents and automated analysis a dependable operating context. AI supports the workflow; it does not replace the controls that make the workflow trustworthy."),
        "show_card_details": False,
        "cards": [
            ("Manual Step Audit", "#manual-step-audit", "assets/home-generated/help-situation-bottleneck.webp", "Manual reporting bottleneck being analyzed for automation"),
            ("Repeatable Data Prep", "#repeatable-data-prep", "assets/home-generated/help-process-build-guide.webp", "Repeatable data preparation and reporting workflow"),
            ("Refresh Reliability", "#refresh-reliability", "assets/home-generated/work-ongoing-optimization.webp", "Reporting automation refresh reliability monitoring")
        ],
        "service_blocks": [
            ("Manual Step Audit", "Identify copy-paste work, recurring exports, fragile formulas, and hidden assumptions inside the current reporting process."),
            ("Transformation Cleanup", "Move heavy or fragile logic to the right layer, simplify repeatable transformations, and make refresh behavior easier to maintain."),
            ("Refresh Reliability Review", "Check refresh timing, dependencies, failures, source permissions, and ownership so automated reporting is not quietly stale."),
            ("Automated Pipeline Build", "Implement maintainable ingestion, transformation, validation, and delivery steps for recurring reporting."),
            ("Replacement Dashboards", "Build governed dashboards or scorecards that replace recurring spreadsheet assembly and manual status packs."),
            ("Monitoring And Alerts", "Add refresh monitoring, exception alerts, failure ownership, and recovery procedures."),
            ("Documented Handoff", "Provide workflow diagrams, business rules, schedules, support ownership, and maintenance procedures for the internal team."),
            ("Reporting Calendar Design", "Align refresh cycles, review meetings, and stakeholder expectations so automation supports the operating rhythm."),
            ("Exception Handling", "Document what happens when data is late, incomplete, manually adjusted, or outside normal thresholds.")
        ],
        "delivery_examples": {
            "Manual Step Audit": "A swimlane map captures all six source reports, exports, formulas, lookups, file locations, reviewers, deadlines, and exception decisions in the current weekly process.",
            "Transformation Cleanup": "Repeated spreadsheet cleanup rules are rebuilt as tested transformations with named fields, documented logic, and clear ownership.",
            "Refresh Reliability Review": "A dependency and schedule map identifies when each source becomes available, what can fail, how freshness is checked, and who responds.",
            "Automated Pipeline Build": "A scheduled pipeline ingests the six sources, applies governed transformations, validates expected row and key conditions, and publishes the reporting-ready table.",
            "Replacement Dashboards": "One governed dashboard replaces six manually assembled views while preserving role-specific filters and the decisions each audience needs.",
            "Monitoring And Alerts": "Refresh failures, late sources, missing records, and abnormal count changes create alerts with owner and recovery instructions.",
            "Documented Handoff": "The team receives the workflow diagram, schedules, credentials and ownership model, business-rule catalog, recovery steps, and maintenance checklist.",
            "Reporting Calendar Design": "A reporting calendar aligns source availability, pipeline completion, quality review, dashboard publication, and the leadership meeting deadline.",
            "Exception Handling": "An exception queue separates issues automation can resolve from items requiring business judgment, approval, or manual follow-up."
        },
        "case_study_heading": "Case study: consolidating six manual weekly reports into one automated workflow",
        "case_studies": [{
            "title": "Replacing hours of weekly assembly with governed reporting automation",
            "situation": "A team produced six related weekly reports from separate exports. Each report required copy-paste preparation, lookups, filters, formatting, reconciliation, and manual distribution before the combined operating review.",
            "failure": "The process depended on one person’s sequence of spreadsheet steps. Logic was duplicated across files, source timing was not visible, and a change to one report could fail to reach the other five.",
            "work": "Parallax documented every manual step and decision rule, consolidated common transformations into one reporting-ready model, built scheduled ingestion and validation, created a replacement dashboard with the required audience views, configured refresh and exception alerts, and documented the operating and recovery procedures.",
            "outcome": "Six parallel report-building paths became one monitored workflow. The team reviewed exceptions instead of rebuilding files, and the reporting logic, schedule, and support ownership became visible and maintainable.",
            "artifact": "Current-state swimlane, source dependency map, consolidated transformation specification, automated pipeline, replacement dashboard, exception log, refresh monitor, and handoff runbook."
        }],
        "faq": [
            ("Should every manual report be automated?", "No. Automate repetitive, stable work. Fix unclear definitions, source issues, and ownership gaps before automating reports that still require heavy judgment."),
            ("Can automation include Power BI?", "Yes. It can include refresh scheduling, semantic-model cleanup, dashboard replacement, and reporting governance around Power BI. The goal is to avoid burying too much business logic inside a brittle report layer."),
            ("What is the main risk?", "The main risk is scaling unclear logic. Automation should reduce manual effort while making business rules more visible, not more hidden."),
            ("Will Parallax implement the workflow?", "Yes. Engagements can include pipeline and transformation work, replacement dashboards, scheduled refreshes, monitoring, automated distribution, and documented handoff.")
        ],
        "articles": [
            ("Five Signs Your Reporting Environment Is Breaking Down", "insights/five-signs-your-reporting-environment-is-breaking-down.html"),
            ("Where AI Actually Helps In Analytics Operations", "insights/where-ai-actually-helps-in-analytics-operations.html"),
            ("Prepare Your Reporting Environment For AI", "insights/prepare-reporting-environment-for-ai.html"),
        ],
        "card_blurbs": {
            "Manual Step Audit": "Documents the exports, pivots, lookups, copy-paste steps, judgment calls, and undocumented checks that keep the current report alive.",
            "Repeatable Data Prep": "Moves repeatable cleanup rules into a maintainable path while keeping business interpretation visible to the owners.",
            "Refresh Reliability": "Checks whether automated reporting is actually current, complete, monitored, and owned when something fails."
        },
        "card_details": {
            "Manual Step Audit": ["A manual step audit is useful when a report depends on one person knowing which export to run, which rows to delete, which lookup to refresh, and which exception to ignore.", "The audit turns that hidden process into an explicit workflow so the team can decide what to automate, what to retire, and what still requires judgment."],
            "Repeatable Data Prep": ["Repeatable data prep does not mean pushing every transformation into the dashboard layer. Heavy business logic should be placed where it is easier to govern, test, and maintain.", "The goal is a simpler path from source to report, with fewer hidden edits and clearer ownership for each business rule."],
            "Refresh Reliability": ["Refresh reliability includes schedules, source permissions, late data, failure alerts, downstream dependencies, and whether anyone owns the response when a refresh breaks.", "This matters because an automated report can look polished while quietly serving stale or incomplete data."]
        },
    },
    "data-quality-review": {
        "title": "Data Quality & Reporting Reliability Consulting",
        "description": "Data quality and reporting reliability consulting for inconsistent metrics, source system issues, manual reporting patches, reconciliation work, and dashboard trust problems.",
        "kicker": "Data Quality & Reporting Reliability",
        "h1": "Data quality review for teams tired of reconciling conflicting numbers.",
        "intro": "Data quality problems show up as reporting problems: dashboards do not match, leaders question the numbers, teams keep offline spreadsheets, and analysts spend too much time explaining exceptions. Parallax Data Lab reviews the path from source systems to reporting outputs so teams can find where trust is breaking and what needs to be fixed first.",
        "hero_image": "assets/home-generated/failure-source-of-truth.webp",
        "hero_alt": "Data quality review tracing conflicting source systems into trusted reporting",
        "proof": ["Source Systems", "Manual Patches", "Metric Drift", "Reconciliation", "Trust Review"],
        "sections": [
            ("What Data Quality Means In Reporting", "Data quality is not only whether a table has blanks. In reporting, quality means the data is accurate enough for the decision, complete enough for the audience, consistent across systems, timely enough for the meeting, and traceable enough for leaders to understand. A late order status, duplicated customer record, unowned mapping table, or manually corrected spreadsheet can each break trust in a different way."),
            ("Where Quality Breaks", "Quality issues often begin upstream: duplicated customer records, inconsistent product hierarchies, late operational entries, manual spreadsheet patches, unowned mapping tables, or business rules that changed without documentation. By the time the issue reaches Power BI or an executive scorecard, the dashboard is blamed for a problem that started much earlier. A review traces the path instead of guessing at the symptom."),
            ("How Parallax Helps", "Parallax traces the issue, then helps implement the fix: correcting transformation logic, rebuilding mappings, strengthening joins, adding validation checks, documenting business rules, assigning owners, and establishing ongoing monitoring and exception alerts. The goal is known confidence and a data path that stays reliable after the review.")
        ],
        "use_case_heading": "Common data quality problems we trace and fix",
        "use_cases": [
            ("Duplicate customers", "Resolve match and merge rules, survivorship logic, identifiers, and downstream reporting impacts."),
            ("Missing or late records", "Identify where records fall out or arrive after reporting cutoffs, then add checks and visible exception handling."),
            ("Inconsistent hierarchies", "Rebuild product, customer, account, facility, or organizational mappings and document who owns changes."),
            ("Broken joins", "Correct grain, key, relationship, and transformation logic that creates duplicated or missing totals."),
            ("Undocumented overrides", "Make manual corrections and special-case rules visible, testable, approved, and maintainable."),
            ("Refresh mismatches", "Align source availability, pipeline timing, semantic refreshes, and report timestamps so users know how current the number is.")
        ],
        "modern_callout": ("Trusted reporting and trusted AI depend on the same controls.", "Automated quality checks, visible exceptions, traceable definitions, monitored pipelines, and explicit ownership improve dashboards today and prevent AI systems from confidently repeating unreliable inputs tomorrow."),
        "cards": [
            ("Source Trace", "#source-trace", "assets/home-generated/failure-conflicting-numbers.webp", "Conflicting source numbers traced for data quality review"),
            ("Exception Review", "#exception-review", "assets/home-generated/failure-definition-drift.webp", "Definition drift and reporting exceptions reviewed"),
            ("Trust Map", "#trust-map", "assets/home-generated/assessment-trust-map.webp", "Trust map for data quality and reporting confidence")
        ],
        "service_blocks": [
            ("Source Trace", "Follow critical numbers from source systems through transformations, manual edits, semantic models, and final reports."),
            ("Completeness Review", "Identify missing records, late data, incomplete dimensions, and fields that limit decision usefulness."),
            ("Consistency Review", "Find where systems, teams, dashboards, or spreadsheets define the same business object differently."),
            ("Exception Handling", "Document manual overrides, special cases, one-off corrections, and judgment calls that affect reported numbers."),
            ("Ownership Recommendations", "Clarify who owns source fixes, transformation logic, definitions, and ongoing monitoring."),
            ("Transformation And Mapping Fixes", "Correct business rules, joins, mapping tables, hierarchy logic, and repeated manual adjustments."),
            ("Validation Checks And Alerts", "Implement completeness, freshness, consistency, uniqueness, and reconciliation checks with visible exception alerts."),
            ("Ongoing Monitoring", "Define monitoring cadence, failure ownership, escalation, documentation, and the process for approving rule changes.")
        ],
        "delivery_examples": {
            "Source Trace": "A lineage view follows the disputed product count from operational entry through extracts, transformation joins, the gold table, semantic logic, and the final report filter.",
            "Completeness Review": "A validation table compares expected and received product records by source, date, facility, and status to expose missing or late data.",
            "Consistency Review": "A cross-system comparison shows where product codes, descriptions, categories, and hierarchy assignments disagree across operational and reporting systems.",
            "Exception Handling": "An exception register records temporary product overrides, business reason, approver, effective period, and the permanent correction path.",
            "Ownership Recommendations": "The ownership model separates who approves product mappings, who implements gold-table changes, who monitors exceptions, and who validates reporting impact.",
            "Transformation And Mapping Fixes": "A governed mapping table resolves product merges, replacements, corrections, and hierarchy rules once for every downstream report.",
            "Validation Checks And Alerts": "Automated tests flag unmapped products, duplicate active mappings, invalid effective dates, broken relationships, and unexpected category movement.",
            "Ongoing Monitoring": "A recurring quality review tracks open exceptions, mapping changes, failed tests, downstream impact, ownership, and resolution status."
        },
        "case_study_heading": "Case study: moving product mapping corrections out of reports and into the gold layer",
        "case_studies": [{
            "title": "Correcting post-production product errors once instead of patching every dashboard",
            "situation": "Product identifiers and hierarchy assignments were sometimes corrected after production activity had already entered reporting. Analysts maintained report-level mapping patches to merge replacement codes, correct classifications, and keep historical product counts usable.",
            "failure": "Each report carried its own correction logic. New dashboards missed old patches, merged products could be double counted, effective dates were unclear, and nobody could see which mapping represented the approved business rule.",
            "work": "Parallax traced the reporting impact, inventoried every manual mapping and merge rule, worked with the product owner to define approved identifiers and effective dates, implemented a governed mapping structure in the gold table, rebuilt downstream joins to use it, and added tests for unmapped codes, duplicate active mappings, and invalid date ranges.",
            "outcome": "Product corrections were resolved once in the governed reporting layer and inherited consistently by every report. Report-specific patches were retired, historical merges remained traceable, and new product errors surfaced through visible exceptions instead of silent dashboard logic.",
            "artifact": "Source-to-report trace, mapping decision log, effective-dated gold mapping table, merge and survivorship rules, validation suite, exception report, and downstream reconciliation checklist."
        }],
        "faq": [
            ("Is this the same as a technical data audit?", "Not exactly. The review includes technical tracing, but it is focused on reporting trust and business decision impact."),
            ("Do we need perfect data before improving dashboards?", "No. You need known data. Leaders can act with imperfect data when the limits, owners, and confidence level are clear."),
            ("Can this come before automation?", "Often it should. Automating a low-quality process can make unreliable reporting spread faster."),
            ("Does the review include fixing the problems?", "It can. The work can move from diagnosis into transformation fixes, mapping rebuilds, validation rules, exception alerts, documentation, and monitoring based on the agreed scope.")
        ],
        "articles": [
            ("Single Source Of Truth Myth", "insights/single-source-of-truth-myth.html"),
            ("Why Data Teams Struggle To Earn Trust", "insights/why-data-teams-struggle-to-earn-trust.html"),
            ("Who Owns This Metric?", "insights/who-owns-this-metric-most-expensive-question-in-analytics.html"),
        ],
        "card_blurbs": {
            "Source Trace": "Follows a disputed number from source entry through extracts, transformations, manual edits, semantic logic, and final dashboard display.",
            "Exception Review": "Separates normal business exceptions from hidden patches, one-off overrides, late entries, and rules nobody has documented.",
            "Trust Map": "Ranks trust breaks by decision impact so teams can fix the issues that matter before chasing cosmetic cleanup."
        },
        "card_details": {
            "Source Trace": ["Source tracing is useful when leaders ask why a dashboard, spreadsheet, and source system all show different answers. The work follows the number through each handoff and names where the logic changes.", "That produces a practical lineage view: source, extract, transformation, model logic, report filter, manual adjustment, and owner."],
            "Exception Review": ["Exception review looks for the business cases that quietly bend the rules: late orders, merged customers, manual credits, incomplete jobs, reclassified products, or one-off leadership adjustments.", "The point is not to eliminate every exception. It is to make exceptions visible enough that recurring reporting can handle them without rebuilding trust each month."],
            "Trust Map": ["A trust map separates issues that affect leadership decisions from issues that are annoying but low impact. This keeps the cleanup effort from spreading into everything at once.", "The map usually identifies quick fixes, owner decisions, structural source problems, and items that should be monitored rather than immediately rebuilt."]
        },
    },
    "dashboard-trust-governance": {
        "title": "BI Governance & Dashboard Trust Consulting",
        "description": "BI governance and dashboard trust consulting for teams that need certified metrics, ownership, access rules, workspace structure, and reporting change control.",
        "kicker": "BI Governance & Dashboard Trust",
        "h1": "BI governance and dashboard trust for teams with too many reports and not enough confidence.",
        "intro": "Dashboard trust breaks when reports multiply faster than standards. Teams create their own versions, certified datasets are unclear, access rules are informal, and leaders no longer know which report should be treated as the source of truth. Parallax Data Lab helps teams build practical BI governance that supports speed instead of burying people in process.",
        "hero_image": "assets/home-generated/help-situation-dashboard-trust.webp",
        "hero_alt": "Dashboard trust and BI governance system for executive reporting",
        "proof": ["Certified Metrics", "Workspace Structure", "Access Rules", "RLS", "Change Control"],
        "sections": [
            ("Governance Should Make Reporting Easier", "BI governance is not a policy binder. It is the operating layer that helps teams know which reports are official, which metrics are certified, who can change logic, how access is granted, and when a dashboard should be retired. Good governance reduces friction because people stop hunting through five versions of the same report."),
            ("Where Trust Breaks", "Trust breaks when the business has no report inventory, no definition owner, no certified metric process, no workspace standards, no refresh expectations, or no access model. A sales manager may build a helpful report that becomes unofficially official. Finance may keep a cleaner version in a spreadsheet. Operations may use a dashboard with a filter nobody else knows about. Governance turns those scattered decisions into a practical model people can follow."),
            ("How Parallax Helps", "Parallax moves beyond recommendations into implementation: consolidating and retiring reports, restructuring Power BI and Fabric workspaces, implementing certified semantic models, configuring and testing RLS, establishing deployment standards, documenting lineage and permissions, and setting up recurring governance reviews.")
        ],
        "use_case_heading": "When dashboard governance becomes necessary",
        "use_cases": [
            ("Multiple versions of the same KPI", "Different dashboards or teams publish competing logic and leadership no longer knows which result is official."),
            ("Unclear report ownership", "Important reports have technical maintainers but no accountable business owner or approval path."),
            ("Duplicated semantic models", "Teams rebuild measures and relationships in separate datasets, multiplying maintenance and trust problems."),
            ("Informal workspace access", "Permissions grow through one-off requests without a durable role, approval, or review model."),
            ("Inconsistent RLS", "Row-level security rules differ across reports or are not tested against real business access requirements."),
            ("Abandoned reports and refresh failures", "Unused assets remain visible while critical reports fail silently or lack a clear response owner.")
        ],
        "modern_callout": ("Fabric and AI readiness are governance outcomes.", "Microsoft Fabric workspaces, shared semantic models, permissions, lineage, certified data products, and deployment paths need an operating model. Copilot and AI answers are only trustworthy when the underlying metrics, access rules, and reporting assets are governed."),
        "show_card_details": False,
        "cards": [
            ("Report Inventory", "#report-inventory", "assets/home-generated/help-outcome-fewer-reports.webp", "Reports consolidating into fewer trusted dashboards"),
            ("Access And Security", "#access-and-security", "assets/home-generated/lab-governance-rls.webp", "Governance and row level security architecture"),
            ("Certified Metrics", "#certified-metrics", "assets/home-generated/reset-metric-mapping-v2.webp", "Certified metric mapping for BI governance")
        ],
        "service_blocks": [
            ("Report Consolidation And Retirement", "Implement the keep, certify, consolidate, retire, or rebuild decisions across active reporting assets."),
            ("Certified Metric Process", "Define which metrics are official, where they live, who can change them, and how changes are communicated."),
            ("Workspace And Fabric Structure", "Restructure Power BI or Fabric workspaces, development paths, published apps, shared semantic models, and certified data products."),
            ("Access, Security And RLS", "Configure and test workspace permissions, row-level security roles, approval paths, and sensitive-data boundaries."),
            ("Deployment Standards", "Implement practical development, test, release, certification, lineage, refresh, and rollback expectations."),
            ("Governance Cadence", "Run a recurring review cycle for access, asset ownership, metric changes, refresh failures, and retirement decisions.")
        ],
        "delivery_examples": {
            "Report Consolidation And Retirement": "A portfolio register assigns every report a decision: certify, consolidate, retire, rebuild, or retain temporarily with a named owner and deadline.",
            "Certified Metric Process": "A certification record connects each executive measure to its owner, definition, semantic model, tests, decision use, and controlled change path.",
            "Workspace And Fabric Structure": "A target workspace map separates development, testing, certified data products, published apps, ownership, and promotion paths.",
            "Access, Security And RLS": "A role matrix and test pack validate who can see which rows, fields, workspaces, apps, exports, and downstream artifacts.",
            "Deployment Standards": "A release checklist covers validation, approvals, lineage, refresh dependencies, rollback, stakeholder communication, and post-release monitoring.",
            "Governance Cadence": "A monthly governance agenda reviews new assets, access changes, metric changes, refresh incidents, owner gaps, and retirement progress."
        },
        "case_study_heading": "Case study: simplifying a fragmented Power BI environment without slowing delivery",
        "case_studies": [{
            "title": "Creating a trusted path through duplicated reports, semantic models, and informal access",
            "situation": "An anonymized multi-team reporting environment contained overlapping dashboards, duplicated semantic models, inconsistent KPI logic, unclear workspace ownership, one-off access grants, and recurring refresh failures with no single response owner.",
            "failure": "Users could not distinguish certified reporting from local analysis. Similar measures changed independently, RLS testing varied by report, abandoned assets remained discoverable, and governance discussions produced recommendations without a durable operating cadence.",
            "work": "Parallax inventoried reports, models, owners, audiences, refresh paths, and permissions; grouped assets by business decision; selected certified semantic models; consolidated or retired duplicates; redesigned workspace and deployment paths; tested RLS against representative roles; and established monthly governance review and change-control standards.",
            "outcome": "The environment gained a visible trusted path: certified models and published apps for governed use, controlled spaces for development, explicit access ownership, fewer duplicate assets, and a recurring forum that kept report, metric, security, and refresh decisions from drifting again.",
            "artifact": "Report and model inventory, consolidation decision register, target workspace map, certified metric catalog, RLS test matrix, deployment checklist, governance charter, and recurring review agenda."
        }],
        "faq": [
            ("Is BI governance only for large companies?", "No. Growing teams need lightweight governance before dashboard sprawl becomes expensive."),
            ("Can governance slow people down?", "Bad governance can. Good governance makes the trusted path obvious so teams spend less time debating which report to use."),
            ("Does this include Power BI RLS?", "Yes when it is in scope. Parallax can review, configure, test, and document RLS roles alongside workspace permissions and approval paths."),
            ("Can this support Microsoft Fabric and Copilot readiness?", "Yes. Workspace structure, shared semantic models, certified data products, lineage, permissions, and metric governance provide the foundation Fabric and Copilot need.")
        ],
        "articles": [
            ("Why Nobody Trusts Your Dashboard", "insights/why-nobody-trusts-your-dashboard.html"),
            ("Governance And RLS Architecture Is A Business Issue", "insights/governance-rls-architecture-business-issue.html"),
            ("Why Executive Dashboards Fail", "insights/why-executive-dashboards-fail.html"),
        ],
        "card_blurbs": {
            "Report Inventory": "Finds active reports, duplicate dashboards, unused assets, owners, audiences, and candidates for retirement or certification.",
            "Access And Security": "Reviews whether permissions, RLS roles, sensitive data paths, and approval rules match the way the business actually operates.",
            "Certified Metrics": "Defines which measures are official, where they live, who can change them, and how changes are communicated."
        },
        "card_details": {
            "Report Inventory": ["A report inventory gives the team a current map of what exists: official dashboards, shadow reports, duplicates, inactive assets, owners, audiences, and refresh expectations.", "This is often the fastest way to reduce confusion because it shows which reports should be trusted, retired, merged, or rebuilt."],
            "Access And Security": ["Access review looks beyond whether a user can open a report. It checks which roles exist, how row-level security is tested, who approves access, and whether sensitive data is exposed through workspaces or exports.", "The result should be a practical access model that can be maintained without blocking normal reporting work."],
            "Certified Metrics": ["Certified metrics give teams a known place to look for official logic. Certification should include owner, definition, source, refresh cadence, usage expectation, and change process.", "This helps analysts move faster because they can reuse trusted measures instead of rebuilding the same logic in every report."]
        },
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
<summary class="nav-menu-section-title">Core engagement paths</summary>
<a class="nav-menu-parent" href="{href(prefix, 'our-offerings.html')}"><span>Offerings Overview</span></a>
<a class="nav-menu-child nav-menu-scorecard nav-menu-path-00" href="{href(prefix, 'dashboard-trust-scorecard.html')}"><span>Diagnostic Scorecard</span><em>Optional</em></a>
<a class="nav-menu-child nav-menu-fit-check nav-menu-path-01" href="{href(prefix, 'free-fit-check.html')}"><span>Free Fit Check</span><em>Free</em></a>
<a class="nav-menu-child nav-menu-path-02" href="{href(prefix, 'analytics-health-check.html')}"><span>Analytics Health Check</span></a>
<a class="nav-menu-child nav-menu-path-03" href="{href(prefix, 'decision-system-reset.html')}"><span>Decision System Reset</span></a>
<a class="nav-menu-child nav-menu-path-04" href="{href(prefix, 'fractional-analytics.html')}"><span>Fractional Analytics</span></a>
</details>
<details class="nav-menu-group">
<summary class="nav-menu-section-title">Expertise by problem</summary>
<a class="nav-menu-parent" href="{href(prefix, 'expertise.html')}"><span>Expertise Overview</span></a>
<a class="nav-menu-child" href="{href(prefix, 'power-bi-consultant-cincinnati.html')}"><span>Power BI Consulting</span></a>
<a class="nav-menu-child" href="{href(prefix, 'kpi-reporting-consulting.html')}"><span>KPI Strategy &amp; Executive Reporting</span></a>
<a class="nav-menu-child" href="{href(prefix, 'reporting-automation-consulting.html')}"><span>Reporting Automation</span></a>
<a class="nav-menu-child" href="{href(prefix, 'data-quality-review.html')}"><span>Data Quality &amp; Reporting Reliability</span></a>
<a class="nav-menu-child" href="{href(prefix, 'dashboard-trust-governance.html')}"><span>BI Governance &amp; Dashboard Trust</span></a>
<a class="nav-menu-child" href="{href(prefix, 'data-integration-analytics-architecture.html')}"><span>Data Integration &amp; Analytics Architecture</span></a>
</details>
</div>
</div>
<div class="nav-dropdown nav-dropdown-intelligence">
<a class="nav-dropdown-toggle" href="{href(prefix, 'intelligence-lab.html')}">Intelligence Lab</a>
<div aria-label="Intelligence Lab services" class="nav-dropdown-menu nav-dropdown-menu-intelligence nav-menu-hierarchy">
<details class="nav-menu-group">
<summary class="nav-menu-section-title">Intelligence Lab</summary>
<a class="nav-menu-parent" href="{href(prefix, 'intelligence-lab.html')}"><span>Intelligence Lab Overview</span></a>
</details>
<details class="nav-menu-group">
<summary class="nav-menu-section-title">Initiatives</summary>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#operations-intelligence-digest')}"><span>Operations Intelligence Digest</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#governance-rls-architecture')}"><span>Governance &amp; RLS Architecture</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#enterprise-outcome-studio')}"><span>Enterprise Outcome Studio</span></a>
<a class="nav-menu-child" href="{href(prefix, 'intelligence-lab.html#predictive-risk-intelligence')}"><span>Predictive Risk Intelligence</span></a>
</details>
</div>
</div>
<a href="{href(prefix, 'insights.html')}">Insights</a>
<div class="nav-dropdown nav-dropdown-about">
<a class="nav-dropdown-toggle" href="{href(prefix, 'about.html')}">About</a>
<div aria-label="About Parallax Data Lab" class="nav-dropdown-menu nav-menu-hierarchy nav-dropdown-menu-about">
<a class="nav-menu-parent" href="{href(prefix, 'about.html')}"><span>About Parallax</span></a>
<a class="nav-menu-child" href="{href(prefix, 'business-intelligence-consultant-cincinnati.html')}"><span>Cincinnati Analytics Consulting</span></a>
</div>
</div>
</nav>
<div class="site-auth-actions">
<a class="site-auth-link" href="{href(prefix, 'decision-workspace.html?auth=login')}">Log in</a>
<a class="site-auth-link is-primary" href="{href(prefix, 'decision-workspace.html?auth=signup')}">Sign up</a>
</div>
</header>'''


def footer_html(prefix: str) -> str:
    return f'''<footer aria-label="Site footer" class="site-footer site-footer-refined">
  <div class="site-footer-inner">
    <div class="site-footer-col site-footer-about">
      <a class="site-footer-brand" href="{href(prefix, 'index.html')}">Parallax Data Lab</a>
      <p>Parallax Data Lab provides business intelligence consulting, Power BI dashboard development, reporting automation, and analytics support for teams that need clearer data.</p>
      <p class="site-footer-location">Cincinnati, Ohio. Based in Cincinnati and serving teams across the United States.</p>
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
      <a href="{href(prefix, 'business-intelligence-consultant-cincinnati.html')}">Cincinnati Analytics Consulting</a>
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
      <a href="{href(prefix, 'kpi-reporting-consulting.html')}">KPI Strategy &amp; Executive Reporting</a>
      <a href="{href(prefix, 'reporting-automation-consulting.html')}">Reporting Automation</a>
      <a href="{href(prefix, 'data-quality-review.html')}">Data Quality &amp; Reporting Reliability</a>
      <a href="{href(prefix, 'dashboard-trust-governance.html')}">BI Governance &amp; Dashboard Trust</a>
      <a href="{href(prefix, 'data-integration-analytics-architecture.html')}">Data Integration &amp; Analytics Architecture</a>
    </nav>
    <div class="site-footer-col site-footer-contact">
      <h3>Contact</h3>
      <a class="site-footer-secondary" href="https://calendly.com/jonahnr/parallax-data-lab-intro-call">Book a Fit Check</a>
      <a class="site-footer-secondary" href="{href(prefix, 'about.html#contact-us')}">Contact Parallax Data Lab</a>
      <a class="site-footer-email site-footer-contact-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">Email us</a>
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
<div><h2>{title}</h2><p>{data.get("card_blurbs", {}).get(title, "Use this path when the reporting problem needs clearer definitions, stronger ownership, and a practical route from insight to action.")}</p><span>Explore {title}</span></div>
</a>'''
        for title, link, img, alt in data["cards"]
    )
    proof = "\n".join(f"<span>{item}</span>" for item in data["proof"])
    show_cards = data.get("show_cards", slug == "expertise")
    card_section = ""
    if show_cards:
        card_section = f'''<section class="expertise-card-section reveal-card" aria-label="{data["kicker"]} related expertise">
<p class="page-kicker">Choose a specialty</p>
<h2>Explore the focused work</h2>
<div class="expertise-card-grid">
{cards}
</div>
</section>'''
    sections = "\n".join(
        f'''<section class="expertise-content-block reveal-card">
<h2>{heading}</h2>
<p>{body}</p>
</section>'''
        for heading, body in data["sections"]
    )
    if slug != "expertise":
        sections = f'''<section class="expertise-approach-section reveal-card" aria-labelledby="expertise-approach-title">
<p class="page-kicker">How to think about the work</p>
<h2 id="expertise-approach-title">{data.get("approach_heading", "A clear path from the visible symptom to a durable operating result")}</h2>
<div class="expertise-approach-flow">''' + "\n".join(
            f'<article><h3>{heading}</h3><p>{body}</p></article>' for heading, body in data["sections"]
        ) + "</div>\n</section>"
    card_details = "\n".join(
        f'''<section class="expertise-card-detail reveal-card" id="{link[1:]}">
<div>
<p class="page-kicker">{title}</p>
<h2>{title} in practice</h2>
<p>{data.get("card_details", {}).get(title, ["This focus area connects the visible reporting request to the operating questions behind it: what decision the work supports, what data can be trusted, who owns the logic, how the result will be reviewed, and what action should follow.", "The useful version is specific, documented, and tied to leadership behavior. It should reduce repeated reconciliation, make assumptions visible, and clarify the smallest useful next step."])[0]}</p>
<p>{data.get("card_details", {}).get(title, ["This focus area connects the visible reporting request to the operating questions behind it: what decision the work supports, what data can be trusted, who owns the logic, how the result will be reviewed, and what action should follow.", "The useful version is specific, documented, and tied to leadership behavior. It should reduce repeated reconciliation, make assumptions visible, and clarify the smallest useful next step."])[1]}</p>
</div>
<img alt="{alt}" src="{href(prefix, img)}" loading="lazy" decoding="async">
</section>'''
        for title, link, img, alt in data["cards"]
        if show_cards and link.startswith("#") and data.get("show_card_details", True)
    )
    service_blocks = ""
    if data.get("service_blocks"):
        delivery_examples = data.get("delivery_examples", {})
        service_blocks = f'''<section class="expertise-delivery-section reveal-card" aria-labelledby="expertise-delivery-title">
<p class="page-kicker">How the work is delivered</p>
<h2 id="expertise-delivery-title">{data.get("service_heading", "From diagnosis to implemented, maintainable work")}</h2>
<p class="expertise-delivery-intro">{data.get("service_intro", "The engagement is organized around concrete work products, implementation decisions, and the operating controls needed to keep the result useful.")}</p>
<div class="expertise-detail-grid" aria-label="Specific consulting focus areas">
''' + "\n".join(
            f'''<details id="service-{title.lower().replace(" ", "-").replace("&", "and")}">
<summary><strong>{title}</strong><em>View example</em></summary>
<div class="expertise-delivery-detail"><p>{body}</p><div class="expertise-delivery-example"><span>Example</span><p>{delivery_examples.get(title, "A representative output shows the current state, the implementation decision, the owner, the validation method, and how the team will maintain the work after handoff.")}</p></div></div>
</details>'''
            for title, body in data["service_blocks"]
        ) + "\n</div>\n</section>"
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
    use_case_section = ""
    if data.get("use_cases"):
        use_case_section = f'''<section class="expertise-use-case-section reveal-card" aria-labelledby="use-case-title">
<p class="page-kicker">Where this applies</p>
<h2 id="use-case-title">{data.get("use_case_heading", "Common use cases")}</h2>
<div class="expertise-use-case-grid">''' + "\n".join(
            f'<article><h3>{title}</h3><p>{body}</p></article>' for title, body in data["use_cases"]
        ) + "</div>\n</section>"
    callout_section = ""
    if data.get("modern_callout"):
        heading, body = data["modern_callout"]
        callout_section = f'''<section class="expertise-modern-callout reveal-card">
<p class="page-kicker">Modern analytics readiness</p>
<h2>{heading}</h2>
<p>{body}</p>
</section>'''
    example_section = ""
    if data.get("examples"):
        example_section = f'''<section class="expertise-project-examples reveal-card" aria-labelledby="project-example-title">
<p class="page-kicker">Anonymized example</p>
<h2 id="project-example-title">{data.get("example_heading", "How the work becomes tangible")}</h2>
<div class="expertise-project-example-grid">''' + "\n".join(
            f'<article><h3>{title}</h3><p>{body}</p></article>' for title, body in data["examples"]
        ) + "</div>\n</section>"
    case_study_section = ""
    if data.get("case_studies"):
        case_study_section = f'''<section class="expertise-case-study-section reveal-card" aria-labelledby="specialty-case-study-title">
<p class="page-kicker">Anonymized case study</p>
<h2 id="specialty-case-study-title">{data.get("case_study_heading", "How this work changes a real reporting system")}</h2>
<div class="expertise-case-study-stack">''' + "\n".join(
            f'''<article>
<h3>{study["title"]}</h3>
<dl><div><dt>Situation</dt><dd>{study["situation"]}</dd></div><div><dt>Why it failed</dt><dd>{study["failure"]}</dd></div><div><dt>Work performed</dt><dd>{study["work"]}</dd></div><div><dt>What changed</dt><dd>{study["outcome"]}</dd></div></dl>
<div class="expertise-case-artifact"><strong>Representative artifact</strong><p>{study["artifact"]}</p></div>
</article>''' for study in data["case_studies"]
        ) + "</div>\n</section>"
    share_section = f'''<section class="share-link-panel share-link-compact" aria-label="Share this page">
<span class="share-link-label">Share</span>
<button type="button" data-native-share="{page_url(slug)}" data-share-title="{data['title']}">Share Link</button>
<button type="button" data-copy-share="{page_url(slug)}">Copy</button>
<a class="share-link-social" href="https://www.linkedin.com/sharing/share-offsite/?url={page_url(slug)}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
<a class="share-link-social" href="mailto:?subject={data['title']}&amp;body={page_url(slug)}">Email</a>
</section>'''
    technology_section = ""
    if slug == "kpi-reporting-consulting":
        technology_section = f'''<section class="technology-stack-section reveal-card" aria-labelledby="technology-stack-title">
<div class="technology-logo-crop"><img src="{href(prefix, 'assets/technology-logos-cropped.webp')}" alt="Databricks dbt ThoughtSpot Sigma Omni AWS Cogniti Google Cloud Looker Microsoft Azure Power BI Qlik Snowflake Tableau and Matillion logos" loading="lazy" decoding="async"></div>
<div class="technology-stack-copy"><p class="page-kicker">Platform experience</p><h2 id="technology-stack-title">Technologies We Work With</h2><p>We work across the modern data and analytics stack so KPI definitions, governed metric layers, scorecards, and automated reporting workflows hold together from source to executive view.</p></div>
</section>'''
    faq = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in data["faq"])
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
<meta property="og:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{data["title"]}"/>
<meta name="twitter:description" content="{data["description"]}"/>
<meta name="twitter:image" content="https://parallaxdatalab.com/assets/social-preview.webp"/>
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
<a class="primary-action" href="{href(prefix, 'free-fit-check.html')}">{data.get("hero_cta", "Book a Fit Check")}</a>
<a class="secondary-action" href="{href(prefix, 'our-offerings.html')}">Compare Offerings</a>
</div>
</div>
<figure class="expertise-hero-media motion-layer" data-depth="-0.04">
<img alt="{data["hero_alt"]}" src="{href(prefix, data["hero_image"])}" decoding="async">
</figure>
</section>
{share_section}
{technology_section}
{use_case_section}
{sections}
{card_section}
{card_details}
{service_blocks}
{case_study_section}
{callout_section}
{example_section}
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
<p class="page-kicker">Focus → execution → starting point</p>
<h2>How We Help</h2>
<p class="help-lede">Start with the kind of work you need, see how Parallax executes it, then choose the smallest sensible starting point.</p>
<div class="expertise-path-grid expertise-path-grid-wide help-pathway-grid">
<a class="expertise-path-card" href="{href(prefix, 'expertise.html')}">
<img alt="Analytics expertise hub connecting Power BI KPI reporting automation and data quality" class="help-card-image" src="{href(prefix, 'assets/home-generated/help-foundation-to-intelligence-advanced.webp')}" loading="lazy" decoding="async">
<div>
<p class="page-kicker">What we focus on</p>
<h3>Expertise Hub</h3>
<p>Explore the focused work we do across Power BI, KPI strategy, reporting automation, reporting reliability, BI governance, dashboard trust, and analytics architecture.</p>
<span>Explore Expertise</span>
</div>
</a>
<a class="expertise-path-card" href="{href(prefix, 'our-offerings.html')}#offering-details-title">
<img alt="Parallax engagement paths moving from diagnosis through execution" class="help-card-image" src="{href(prefix, 'assets/home-generated/offerings-hero.webp')}" loading="lazy" decoding="async">
<div>
<p class="page-kicker">How we execute</p>
<h3>Our Offerings</h3>
<p>Compare focused diagnostics, decision-system rebuilds, and ongoing analytics leadership—each scoped around the business constraint that needs to move.</p>
<span>Compare Engagement Paths</span>
</div>
</a>
<a class="expertise-path-card" href="{href(prefix, 'free-fit-check.html')}">
<img alt="A clear starting path for choosing the right analytics engagement" class="help-card-image" src="{href(prefix, 'assets/home-generated/offerings-fit-check.webp')}" loading="lazy" decoding="async">
<div>
<p class="page-kicker">Where to begin</p>
<h3>Start With A Fit Check</h3>
<p>Bring the situation—not a preselected service. We will help identify the smallest useful next step, including when no paid engagement is needed.</p>
<span>Start The Free Fit Check</span>
</div>
</a>
</div>
</section>'''
    text = re.sub(pattern, replacement, text, count=1, flags=re.S)
    block_match = re.search(pattern, text, flags=re.S)
    situation_marker = '<section class="help-section situation-section reveal-card">'
    if block_match and situation_marker in text and block_match.start() > text.index(situation_marker):
        block = block_match.group(0)
        text = text[:block_match.start()] + text[block_match.end():]
        text = text.replace(situation_marker, block + "\n" + situation_marker, 1)
    return text


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

const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const today = "2026-06-12";
const site = "https://parallaxdatalab.com";

const categories = {
  trust: "Analytics Trust",
  governance: "KPI Governance",
  reporting: "Executive Reporting",
  leadership: "Analytics Leadership",
  ai: "AI Enablement",
  lab: "Intelligence Lab",
};

const services = {
  health: {
    label: "Analytics Health Check",
    path: "analytics-health-check.html",
  },
  reset: {
    label: "Decision System Reset",
    path: "decision-system-reset.html",
  },
  fractional: {
    label: "Fractional Analytics Leadership",
    path: "fractional-analytics.html",
  },
  powerbi: {
    label: "Power BI Advisory",
    path: "intelligence-lab.html#enterprise-outcome-studio",
  },
  lab: {
    label: "Intelligence Lab",
    path: "intelligence-lab.html",
  },
  fitCheck: {
    label: "Free Fit Check",
    path: "free-fit-check.html",
  },
};

const articles = [
  {
    title: "Why Nobody Trusts Your Dashboard",
    slug: "why-nobody-trusts-your-dashboard",
    category: categories.trust,
    service: "health",
    image: "dashboard-trust-breakdown.png",
    alt: "Layered executive dashboard signals splitting into competing metric paths",
    summary: "Dashboard trust breaks when leaders cannot trace definitions, owners, and decisions behind the numbers.",
    meta: "Learn why executives stop trusting dashboards, how reporting trust breaks, and what growing companies can do to rebuild confidence in metrics.",
    lead: "A dashboard rarely loses trust because of one wrong chart. It loses trust because the executive team learns, over time, that the numbers require translation before they can be used.",
    meeting: "The CFO brings a bookings number. Sales brings a different version from the CRM. Operations has a spreadsheet that excludes two edge cases nobody else knew about. The dashboard is technically available, but the meeting has already moved into reconciliation mode.",
    cost: "Once that pattern sets in, leaders stop asking what the metric means for the business. They ask who pulled it, when it refreshed, and whether the exception list was included. The dashboard becomes a starting point for argument instead of a source of shared focus.",
    shift: "Trust returns when the company treats the dashboard as the visible surface of an operating system: owned definitions, explicit refresh rules, documented exclusions, reusable logic, and a meeting cadence that uses the numbers for decisions.",
    example: "In one growing services company, margin dashboards were distrusted because project labor rules differed by team. The fix was not a prettier margin page. It was a short definition council, a named owner for margin logic, and one certified measure used everywhere.",
    moves: [
      "Audit the five metrics leaders argue about most and trace every version back to its source logic.",
      "Name a business owner for each metric, not only a technical report owner.",
      "Separate certified executive metrics from exploratory analysis so leaders know which numbers can be used in operating meetings.",
      "Add a visible definition panel to critical dashboards that explains inclusion rules, exclusions, grain, and refresh timing.",
      "Retire duplicate dashboard pages when they answer the same question with different logic.",
    ],
    related: ["why-executive-teams-argue-about-numbers", "five-signs-your-reporting-environment-is-breaking-down", "how-to-build-metrics-people-actually-use"],
  },
  {
    title: "Reporting Misalignment: Hidden Costs",
    slug: "hidden-cost-of-reporting-misalignment",
    category: categories.trust,
    service: "reset",
    image: "reporting-misalignment-cost.png",
    alt: "Executive reporting paths diverging into duplicated work and delayed decisions",
    summary: "Reporting misalignment quietly taxes leadership attention, operating cadence, and strategic confidence.",
    meta: "See how reporting misalignment slows decisions, weakens accountability, duplicates analytics work, and creates hidden operating drag.",
    lead: "Reporting misalignment looks like a data problem from the outside. Inside the business, it behaves like an attention tax.",
    meeting: "A weekly review starts with three teams presenting performance. Each uses a slightly different definition of active customer, recognized revenue, or delivery capacity. Nobody is trying to mislead anyone. The organization simply lacks one operating language.",
    cost: "The cost is not just duplicate reporting effort. It is delayed decisions, softened accountability, slower planning cycles, and executive energy spent negotiating definitions that should have been settled before the meeting began.",
    shift: "The cure is to align reports around the decisions they support. Reports that do not map to decisions become optional. Reports that do map to decisions need owners, definitions, and a standard cadence.",
    example: "A founder may think the analytics team needs another sprint. What the business actually needs is agreement on which revenue view is used for board reporting, which view is used for sales coaching, and which view is used for cash planning.",
    moves: [
      "Inventory recurring leadership meetings and list the metrics used in each one.",
      "Identify where the same business concept appears with different names, filters, or time windows.",
      "Choose the decision owner for each reporting pack before changing the dashboard design.",
      "Create a small certified metric layer for executive reporting and leave analysis flexibility outside it.",
      "Remove reports that no longer have a decision owner or operating cadence.",
    ],
    related: ["the-difference-between-reporting-and-decision-making", "single-source-of-truth-myth", "stop-measuring-everything-designing-executive-reporting-that-drives-action"],
  },
  {
    title: "When Dashboards Reveal Leadership Gaps",
    slug: "dashboard-problem-leadership-problem",
    category: categories.trust,
    service: "reset",
    image: "dashboard-leadership-problem.png",
    alt: "Leadership decision system sitting beneath a dashboard interface",
    summary: "Many dashboard failures start with unclear executive decisions, ownership, and operating rhythm.",
    meta: "Learn why dashboard problems often come from unclear decisions, weak ownership, and leadership cadence gaps instead of visual design.",
    lead: "Most dashboard requests start with a sentence that sounds harmless: we just need better visibility. Sometimes that is true. Often, visibility is the polite version of a leadership problem no one has named yet.",
    meeting: "Executives want a dashboard that will make performance obvious, but the team has not agreed what performance means, who owns movement, or what action follows when the number changes.",
    cost: "Without leadership clarity, the analytics team becomes the mediator. Analysts translate priorities, settle definition disputes, and absorb frustration that belongs in the operating model.",
    shift: "A useful dashboard begins with executive choices. Which decisions happen weekly? Which metrics trigger intervention? Who owns the response? What threshold creates escalation? Those answers shape the report.",
    example: "If churn is red, does customer success own the next move, sales own handoff quality, product own adoption, or finance own contraction exposure? Until leadership answers that, the churn dashboard can only display tension.",
    moves: [
      "Start dashboard work by documenting the leadership decision the page is meant to support.",
      "Ask what action will change if the metric moves before adding another visual.",
      "Assign one accountable owner for the response to each executive metric.",
      "Use thresholds and exception paths so the dashboard points toward action, not interpretation.",
      "Review whether meetings use the dashboard to make decisions or merely to narrate results.",
    ],
    related: ["why-executive-dashboards-fail", "building-executive-dashboards-that-create-accountability", "the-difference-between-reporting-and-decision-making"],
  },
  {
    title: "Single Source of Truth: Why It Fails",
    slug: "single-source-of-truth-myth",
    category: categories.trust,
    service: "health",
    image: "single-source-truth-myth.png",
    alt: "One certified metric spine supporting several business views",
    summary: "A single source of truth is useful only when leaders define the truths the business actually needs.",
    meta: "Learn why single source of truth projects fail and how governed metric views can support finance, operations, and executive reporting.",
    lead: "The phrase single source of truth sounds decisive. It promises one clean place where every number lives and every argument ends. In practice, it can become a slogan that hides hard operating choices.",
    meeting: "Finance, sales, operations, and customer success often need different views of the same business reality. The problem is not that multiple views exist. The problem is that nobody has defined which view is authoritative for which decision.",
    cost: "When a company chases one universal truth without governance, it either creates a rigid model nobody can use or a crowded warehouse where every team still rebuilds its own version.",
    shift: "The better goal is governed plurality: a certified metric spine with clear definitions, plus approved business views for planning, coaching, forecasting, and operational follow-up.",
    example: "Revenue can be recognized, booked, invoiced, collected, and forecasted. A mature company does not pretend those are the same number. It documents which revenue view belongs in which conversation.",
    moves: [
      "Define the decision context for each major metric before declaring it the source of truth.",
      "Build a certified layer for executive measures and a flexible layer for analysis.",
      "Make metric lineage understandable to business leaders, not only to technical teams.",
      "Use naming conventions that distinguish booked, recognized, billed, and collected realities.",
      "Govern changes through owners who understand the business consequences of definition drift.",
    ],
    related: ["hidden-cost-of-reporting-misalignment", "kpi-governance-explained-growing-organizations", "who-owns-this-metric-most-expensive-question-in-analytics"],
  },
  {
    title: "Reporting Environment Breakdown: 5 Signs",
    slug: "five-signs-your-reporting-environment-is-breaking-down",
    category: categories.trust,
    service: "health",
    image: "reporting-environment-breaking-down.png",
    alt: "Reporting environment showing cracks across dashboards, spreadsheets, and metric definitions",
    summary: "Reporting breakdown shows up in meetings, ownership gaps, duplicated logic, and quiet workarounds.",
    meta: "Spot the signs of reporting environment breakdown before dashboard trust, leadership cadence, manual workarounds, and decision quality erode.",
    lead: "Reporting environments rarely break all at once. They fray. At first, the symptoms look manageable: a spreadsheet here, a manual adjustment there, one extra dashboard for a special case.",
    meeting: "Then the exceptions become the system. Leaders ask for pre-meeting reconciliations. Analysts maintain too many versions. Teams trust their own extracts more than shared reporting.",
    cost: "The cost is not only messy reporting. It is the loss of operating confidence. When leaders do not believe the system, they build side channels, and those side channels make the system less trustworthy.",
    shift: "The practical response is diagnosis before rebuilding. You need to know whether the issue is data quality, metric definitions, ownership, dashboard design, source systems, or decision cadence.",
    example: "A Power BI environment can look healthy because reports load and refresh. Meanwhile, every executive still asks for a spreadsheet export because the dashboard does not answer the question in the way the business actually runs.",
    moves: [
      "Look for recurring number debates in leadership meetings.",
      "Track manual adjustments that happen outside the reporting system.",
      "Find metrics that appear in multiple reports with different filters or names.",
      "Ask which dashboards executives open without an analyst present.",
      "Identify reporting assets that no one owns but everyone depends on.",
    ],
    related: ["why-nobody-trusts-your-dashboard", "why-executive-dashboards-fail", "the-hidden-cost-of-reporting-misalignment"],
  },
  {
    title: "Metric Ownership: Who Owns the KPI?",
    slug: "who-owns-this-metric-most-expensive-question-in-analytics",
    category: categories.governance,
    service: "reset",
    image: "metric-ownership-question.png",
    alt: "A critical KPI moving from ambiguity into named business ownership",
    summary: "Metric ownership is where analytics governance becomes business accountability.",
    meta: "Learn how metric ownership closes one of the most expensive analytics gaps by assigning KPI accountability without creating bureaucracy.",
    lead: "The most expensive analytics question is not whether the number is correct. It is who owns it.",
    meeting: "A metric can be technically accurate and still operationally useless if no leader is accountable for its definition, movement, interpretation, and response.",
    cost: "When ownership is missing, analytics teams become unpaid referees. They explain why the number changed, defend logic they did not choose, and chase consensus across teams with different incentives.",
    shift: "Metric ownership does not mean one executive gets to manipulate the number. It means one business owner is responsible for the definition being fit for purpose and for coordinating the response when the metric changes.",
    example: "Gross retention may involve customer success behavior, product adoption, implementation quality, and contract structure. That does not mean it can have four equal owners. It needs one accountable owner and several contributing owners.",
    moves: [
      "Assign an accountable business owner to each executive KPI.",
      "Separate definition ownership from dashboard maintenance.",
      "Document contributing teams so ownership does not become blame.",
      "Create a change process for metric definitions before they appear in board or executive packs.",
      "Review ownership quarterly as the operating model changes.",
    ],
    related: ["kpi-ownership-framework-every-leadership-team-needs", "kpi-governance-explained-growing-organizations", "building-executive-dashboards-that-create-accountability"],
  },
  {
    title: "KPI Governance for Growing Teams",
    slug: "kpi-governance-explained-growing-organizations",
    category: categories.governance,
    service: "reset",
    image: "kpi-governance-growing-organizations.png",
    alt: "KPI governance framework connecting owners, definitions, cadence, and decisions",
    summary: "KPI governance gives growing companies a lightweight way to keep metrics useful as complexity increases.",
    meta: "KPI governance for growing teams: owners, definitions, decision cadence, metric changes, and practical rules that keep reporting useful.",
    lead: "KPI governance sounds heavier than it needs to be. For a growing company, it should not mean committees, binders, or a slow approval queue.",
    meeting: "Good governance is the set of agreements that keeps leadership metrics usable as the company adds products, teams, systems, and exceptions.",
    cost: "Without governance, every new report can quietly create a new version of the business. That feels flexible at first. Later it becomes expensive confusion.",
    shift: "The goal is to protect decision quality. Leaders need to know what a KPI means, who owns it, where it comes from, when it changes, and what action it is meant to inform.",
    example: "A company moving from founder-led reporting to department-led reporting often needs only a short metric catalog, owner map, and change protocol to prevent months of future reconciliation.",
    moves: [
      "Create a certified KPI list for executive and board reporting.",
      "Write definitions in business language before adding technical lineage.",
      "Assign accountable owners and contributing owners.",
      "Define how metric changes are proposed, reviewed, and communicated.",
      "Review the KPI set against the leadership meeting cadence, not in isolation.",
    ],
    related: ["single-source-of-truth-myth", "kpi-ownership-framework-every-leadership-team-needs", "who-owns-this-metric-most-expensive-question-in-analytics"],
  },
  {
    title: "Why Executive Teams Argue About Numbers",
    slug: "why-executive-teams-argue-about-numbers",
    category: categories.governance,
    service: "health",
    image: "executive-teams-argue-about-numbers.png",
    alt: "Executive metrics splitting into competing interpretations across leadership roles",
    summary: "Number debates are usually symptoms of unclear definitions, incentives, and decision rights.",
    meta: "Executive teams argue about numbers when metrics lack shared definitions, ownership, and decision context. Learn how to stop the cycle.",
    lead: "When executive teams argue about numbers, the surface issue is usually accuracy. The deeper issue is alignment.",
    meeting: "The sales leader trusts CRM pipeline. Finance trusts bookings after review. Customer success trusts account health. Operations trusts delivery capacity. Each number may be reasonable inside its own context, but leadership meetings require a shared operating context.",
    cost: "Repeated number debates make teams cautious. Leaders defend their function instead of solving the business problem. Analysts learn to over-explain. Decisions wait for a cleaner answer that rarely arrives.",
    shift: "The way out is not to force every team into one perspective. It is to decide which perspective governs each leadership decision and make the tradeoffs explicit.",
    example: "Pipeline coverage for sales coaching and pipeline coverage for board forecasting are related but not identical. If the company uses one phrase for both, the argument will return every month.",
    moves: [
      "Name the decision before selecting the metric version.",
      "Keep local operating views separate from executive-certified views.",
      "Document the owner and allowed use for disputed metrics.",
      "Use meeting pre-reads to resolve definition issues before leadership time.",
      "Track recurring debates as governance defects, not personality conflicts.",
    ],
    related: ["why-nobody-trusts-your-dashboard", "hidden-cost-of-reporting-misalignment", "single-source-of-truth-myth"],
  },
  {
    title: "KPI Ownership Framework for Leaders",
    slug: "kpi-ownership-framework-every-leadership-team-needs",
    category: categories.governance,
    service: "reset",
    image: "kpi-ownership-framework.png",
    alt: "KPI ownership framework showing accountable owner, contributors, cadence, and action thresholds",
    summary: "A practical KPI ownership framework connects metrics to accountability without creating blame.",
    meta: "Use a KPI ownership framework to assign accountable owners, contributors, definitions, thresholds, and decision cadence for leadership metrics.",
    lead: "KPI ownership fails when it is treated as a label in a spreadsheet. It works when it becomes part of how the leadership team manages the business.",
    meeting: "An owner is not the person who built the dashboard. An owner is the leader accountable for whether the metric is defined correctly, reviewed at the right cadence, and connected to action.",
    cost: "Without a framework, ownership becomes vague. Everyone cares about net revenue retention, margin, cycle time, or customer acquisition cost, which often means no one can make the hard call when definitions conflict.",
    shift: "A useful ownership framework has five parts: accountable owner, contributing owners, definition steward, decision cadence, and action threshold.",
    example: "For customer acquisition cost, marketing may own paid spend inputs, sales may own conversion behavior, finance may own capitalization rules, and the COO or CFO may own the executive KPI definition.",
    moves: [
      "Assign one accountable owner for the executive KPI.",
      "List contributing owners who influence the metric but do not control the definition.",
      "Name a definition steward who maintains documentation and lineage.",
      "Tie the metric to a specific meeting cadence.",
      "Set thresholds that trigger review, escalation, or intervention.",
    ],
    related: ["who-owns-this-metric-most-expensive-question-in-analytics", "kpi-governance-explained-growing-organizations", "building-executive-dashboards-that-create-accountability"],
  },
  {
    title: "How to Build Metrics People Actually Use",
    slug: "how-to-build-metrics-people-actually-use",
    category: categories.governance,
    service: "reset",
    image: "metrics-people-actually-use.png",
    alt: "Useful metrics flowing from executive decisions into team actions",
    summary: "Useful metrics are built around decisions, ownership, and behavior change, not reporting inventory.",
    meta: "Learn how to build metrics people actually use by connecting KPIs to decisions, owners, thresholds, and operating routines.",
    lead: "People do not use metrics because the chart exists. They use metrics when the number helps them make a decision they already need to make.",
    meeting: "Many companies build metric libraries from available data. The better starting point is the operating question: what decision gets better if this metric is trusted?",
    cost: "Unused metrics create noise. They make dashboards look complete while hiding the few signals that should drive focus. The result is reporting abundance and decision scarcity.",
    shift: "A useful metric has a job. It clarifies a tradeoff, exposes a risk, tracks an operating promise, or triggers action. If a metric cannot do one of those things, it may be descriptive, but it is not yet useful.",
    example: "Average time to resolution is interesting. Segmenting aging high-value customer issues by owner, escalation stage, and renewal exposure is useful because it points to action.",
    moves: [
      "Start with the decision or behavior the metric should influence.",
      "Define the audience and cadence before choosing the visualization.",
      "Write the metric definition in plain business language.",
      "Add thresholds so users know when movement matters.",
      "Remove metrics that do not change a decision, priority, or conversation.",
    ],
    related: ["stop-measuring-everything-designing-executive-reporting-that-drives-action", "the-difference-between-reporting-and-decision-making", "why-nobody-trusts-your-dashboard"],
  },
  {
    title: "Why Executive Dashboards Fail",
    slug: "why-executive-dashboards-fail",
    category: categories.reporting,
    service: "powerbi",
    image: "why-executive-dashboards-fail.png",
    alt: "Executive dashboard failing because visuals are disconnected from ownership and action",
    summary: "Executive dashboards fail when they report activity but do not support leadership decisions.",
    meta: "Executive dashboards fail for predictable reasons: unclear audience, too many metrics, weak ownership, and no decision cadence.",
    lead: "Executive dashboards fail because they are often built as reporting summaries rather than decision tools.",
    meeting: "A dashboard can be visually polished, technically impressive, and still useless if it does not match how leaders manage the business.",
    cost: "The failure mode is familiar: the CEO asks for one page, every function adds its favorite metric, the page grows crowded, and the executive team still asks for offline analysis before making decisions.",
    shift: "The strongest executive dashboards are selective. They show the few signals that matter to the current operating model, explain movement, identify accountable owners, and point toward the next conversation.",
    example: "A weekly dashboard for a services business should not simply show revenue, margin, utilization, and backlog. It should show where margin risk is emerging, which owners need to act, and what changed since the last review.",
    moves: [
      "Define the executive audience and decision cadence before designing the page.",
      "Limit the dashboard to metrics that change leadership action.",
      "Add ownership and commentary where interpretation is predictable.",
      "Separate strategic scorecards from operational drilldowns.",
      "Review adoption by observing meetings, not page view counts alone.",
    ],
    related: ["stop-measuring-everything-designing-executive-reporting-that-drives-action", "building-executive-dashboards-that-create-accountability", "dashboard-problem-leadership-problem"],
  },
  {
    title: "Executive Reporting That Drives Action",
    slug: "stop-measuring-everything-designing-executive-reporting-that-drives-action",
    category: categories.reporting,
    service: "powerbi",
    image: "executive-reporting-drives-action.png",
    alt: "Executive reporting narrowed from many metrics into a focused action system",
    summary: "Executive reporting gets stronger when leaders stop measuring everything and start measuring what drives action.",
    meta: "Design executive reporting that cuts through data noise by narrowing metrics, clarifying owners, and aligning reports to leadership decisions.",
    lead: "The easiest way to weaken executive reporting is to measure everything. It feels responsible, but it usually creates a wall of numbers that protects the organization from focus.",
    meeting: "When every metric is visible, no metric is clearly important. Leaders scan, comment, and move on. The report is busy, but the operating system is passive.",
    cost: "Too many metrics create hidden costs: slower meetings, diluted accountability, shallow commentary, and a culture where teams can always point to a different number that supports their preferred story.",
    shift: "Action-oriented reporting is intentionally selective. It distinguishes health indicators from management levers, separates context from triggers, and makes the next decision obvious.",
    example: "A COO does not need twenty charts on delivery performance every Monday. The COO needs to know which commitments are at risk, which owner is accountable, whether capacity or quality is the constraint, and what intervention is due this week.",
    moves: [
      "Classify metrics as health indicators, decision triggers, or diagnostic context.",
      "Put decision triggers in the executive view and move diagnostics into drilldowns.",
      "Require every executive metric to have an owner and action threshold.",
      "Design pages around meeting flow, not data availability.",
      "Prune metrics quarterly as strategy and operating rhythm change.",
    ],
    related: ["how-to-build-metrics-people-actually-use", "why-executive-dashboards-fail", "what-should-be-included-in-weekly-business-review"],
  },
  {
    title: "Weekly Business Review: What to Include",
    slug: "what-should-be-included-in-weekly-business-review",
    category: categories.reporting,
    service: "reset",
    image: "weekly-business-review.png",
    alt: "Weekly business review dashboard structured around decisions, risks, and accountable owners",
    summary: "A weekly business review should focus leadership attention on movement, risk, commitments, and action.",
    meta: "Learn what to include in a weekly business review so leadership meetings move beyond status updates into decisions, risks, and accountability.",
    lead: "A weekly business review should not be a parade of updates. It should be the operating meeting where leaders see what changed, what matters, who owns it, and what decision is needed.",
    meeting: "Many WBRs become department readouts because the reporting pack mirrors the org chart. Sales talks sales, operations talks operations, finance talks finance, and the cross-functional issues arrive too late.",
    cost: "The cost is a meeting that consumes leadership time without creating operating leverage. People leave informed but not aligned.",
    shift: "A strong weekly business review includes performance movement, material exceptions, forward-looking risks, owner commitments, and open decisions. The pack should make tradeoffs visible.",
    example: "Instead of showing every pipeline chart, show the pipeline change that affects the forecast, the segment responsible, the conversion risk, and the owner of the intervention before next week.",
    moves: [
      "Open with the few metrics that changed materially since the last review.",
      "Show exceptions and risks before broad status summaries.",
      "Include owner commitments from the prior week and whether they moved.",
      "Separate decisions needed from information shared.",
      "Close with the actions, owners, and follow-up cadence.",
    ],
    related: ["the-difference-between-reporting-and-decision-making", "building-executive-dashboards-that-create-accountability", "stop-measuring-everything-designing-executive-reporting-that-drives-action"],
  },
  {
    title: "Reporting vs Decision-Making",
    slug: "the-difference-between-reporting-and-decision-making",
    category: categories.reporting,
    service: "reset",
    image: "reporting-vs-decision-making.png",
    alt: "Reporting layer connecting into an executive decision-making loop",
    summary: "Reporting tells leaders what happened. Decision systems help them decide what to do next.",
    meta: "Understand the difference between reporting and decision-making, and how to turn dashboards into decision systems leaders actually use.",
    lead: "Reporting and decision making are related, but they are not the same job.",
    meeting: "Reporting describes performance. Decision making chooses a response. A company can have a large reporting environment and still have weak decision flow if dashboards do not connect to ownership, thresholds, and action.",
    cost: "When the distinction is blurred, leaders ask reports to do too much and ask meetings to compensate for the missing system. The result is more pages, more commentary, and still not enough clarity.",
    shift: "A decision system starts with the choice the business needs to make. It then defines the metric, context, owner, cadence, threshold, and follow-up loop required to support that choice.",
    example: "A churn report tells you churn increased. A decision system shows which customer segments changed, which renewal risks are material, who owns intervention, and whether the playbook changed the outcome.",
    moves: [
      "List recurring leadership decisions before inventorying reports.",
      "Map each decision to the metrics and context required to make it responsibly.",
      "Identify where reporting stops and human judgment begins.",
      "Build follow-up loops so decisions are reviewed, not forgotten.",
      "Retire reports that do not support a decision, obligation, or operating promise.",
    ],
    related: ["hidden-cost-of-reporting-misalignment", "what-should-be-included-in-weekly-business-review", "analytics-maturity-roadmap-reporting-to-decision-systems"],
  },
  {
    title: "Executive Dashboards and Accountability",
    slug: "building-executive-dashboards-that-create-accountability",
    category: categories.reporting,
    service: "powerbi",
    image: "executive-dashboards-accountability.png",
    alt: "Executive dashboard linking KPI movement to owners, actions, and follow-up cadence",
    summary: "Accountability dashboards connect metric movement to owners, thresholds, and follow-through.",
    meta: "Build executive dashboards that create accountability by tying KPIs to owners, thresholds, commitments, operating cadence, and action paths.",
    lead: "An executive dashboard should make accountability easier, not more political.",
    meeting: "The problem with many dashboards is that they show performance without showing responsibility. A number turns red, everyone sees it, and no one is sure who is supposed to do what next.",
    cost: "That gap creates either blame or avoidance. Teams debate whether the metric is fair, whether the data is complete, or whether another department caused the movement.",
    shift: "Accountability comes from context. The dashboard needs metric ownership, clear thresholds, expected response, recent commitments, and a place to see whether action happened.",
    example: "If implementation cycle time worsens, the executive view should show where work is aging, which owner controls the constraint, what commitment was made last week, and whether the risk affects revenue recognition or customer experience.",
    moves: [
      "Show the accountable owner next to the metric, not in a separate governance document.",
      "Use thresholds that distinguish noise from action-worthy movement.",
      "Add variance commentary where leaders repeatedly ask the same question.",
      "Link metric movement to current initiatives or owner commitments.",
      "Review the dashboard in the same cadence where accountability is expected.",
    ],
    related: ["kpi-ownership-framework-every-leadership-team-needs", "why-executive-dashboards-fail", "what-should-be-included-in-weekly-business-review"],
  },
  {
    title: "When Is It Time to Hire a Head of Analytics?",
    slug: "when-to-hire-head-of-analytics",
    category: categories.leadership,
    service: "fractional",
    image: "hire-head-of-analytics.png",
    alt: "Analytics leadership role emerging as reporting demand, governance, and decision needs increase",
    summary: "The right time to hire analytics leadership is when the business needs standards, prioritization, and judgment, not just more reports.",
    meta: "Learn when growing companies should hire a Head of Analytics, and when fractional analytics leadership is the better next step.",
    lead: "Companies usually consider hiring a Head of Analytics after reporting pain becomes visible. Dashboards are inconsistent. Analysts are overloaded. Executives do not trust the numbers. Teams are asking for strategy, not only reports.",
    meeting: "The question is not whether analytics work exists. It almost certainly does. The question is whether the business now needs an analytics leader to set standards, prioritize demand, design decision systems, and influence executives.",
    cost: "Hiring too early can create overhead without enough organizational readiness. Hiring too late leaves the business with scattered logic, frustrated analysts, and executives who treat analytics as a service desk.",
    shift: "The inflection point arrives when analytics decisions require tradeoffs: which metrics become certified, which requests get declined, which systems need cleanup, and how leadership will use data to run the company.",
    example: "A company with one strong analyst may not need a full-time Head of Analytics yet. But if that analyst is also expected to govern KPIs, manage executives, design Power BI standards, and settle definition disputes, leadership capacity is missing.",
    moves: [
      "Assess whether reporting demand now requires prioritization across functions.",
      "Look for unresolved metric disputes that need senior business judgment.",
      "Ask whether analysts are spending more time mediating than building.",
      "Decide whether the next need is full-time management or fractional leadership.",
      "Define the mandate before writing the job description.",
    ],
    related: ["what-fractional-analytics-leadership-actually-means", "building-analytics-function-without-hiring-full-team", "why-data-teams-struggle-to-earn-trust"],
  },
  {
    title: "Fractional Analytics Leadership Explained",
    slug: "what-fractional-analytics-leadership-actually-means",
    category: categories.leadership,
    service: "fractional",
    image: "fractional-analytics-leadership.png",
    alt: "Fractional analytics leader guiding standards, cadence, and executive decision systems",
    summary: "Fractional analytics leadership provides senior judgment and operating structure without a full-time hire.",
    meta: "Fractional analytics leadership explained: what it means, when it works, and how it helps teams improve reporting standards and decisions.",
    lead: "Fractional analytics leadership is not a part-time dashboard builder. It is senior analytics judgment applied at the cadence and scale the business actually needs.",
    meeting: "For many growing companies, the problem is not a lack of effort. It is a lack of experienced analytics leadership to set standards, push back on low-value requests, align executives, and help the team build systems that survive scale.",
    cost: "Without that leadership, the company may keep adding reports while avoiding the harder questions: what should be governed, who owns the metric, which reporting assets are trusted, and how analytics priorities connect to business strategy.",
    shift: "A fractional leader helps create the operating layer: metric governance, dashboard standards, backlog prioritization, executive reporting cadence, and coaching for existing analysts or operators.",
    example: "A COO may need someone who can translate leadership priorities into a Power BI roadmap, tell the executive team why ten metrics should be retired, and help an analyst build reusable logic instead of another one-off page.",
    moves: [
      "Use fractional leadership when the need is senior direction before full-time scale.",
      "Give the role authority to prioritize, govern, and recommend tradeoffs.",
      "Pair strategic guidance with hands-on review of dashboards and metric logic.",
      "Create a cadence for executive alignment and analyst enablement.",
      "Measure success by decision quality and trust, not only report volume.",
    ],
    related: ["when-to-hire-head-of-analytics", "building-analytics-function-without-hiring-full-team", "analytics-maturity-roadmap-reporting-to-decision-systems"],
  },
  {
    title: "Build Analytics Without a Full Team",
    slug: "building-analytics-function-without-hiring-full-team",
    category: categories.leadership,
    service: "fractional",
    image: "analytics-function-without-full-team.png",
    alt: "Lean analytics function built with leadership, standards, tooling, and focused execution",
    summary: "A company can build a credible analytics function by sequencing leadership, governance, systems, and selective execution.",
    meta: "Build an analytics function without hiring a full team by focusing on standards, metric ownership, decision cadence, and fractional leadership.",
    lead: "Not every growing company needs a full analytics team right now. Many need the benefits of an analytics function before the budget, workload, or operating model supports multiple hires.",
    meeting: "The mistake is to treat the choice as binary: hire a full team or live with scattered reporting. There is a middle path.",
    cost: "Without structure, lean analytics becomes heroic. One analyst, finance manager, or operations lead carries dashboards, ad-hoc analysis, metric disputes, and system cleanup with no clear mandate.",
    shift: "A lean analytics function needs four things: a prioritized decision agenda, a governed metric layer, reliable reporting standards, and enough senior leadership to make tradeoffs.",
    example: "A founder-led company may start with a fractional analytics leader, one internal operator, clear Power BI standards, and a monthly executive metric review before hiring specialized analysts.",
    moves: [
      "Define the decisions analytics must support in the next two quarters.",
      "Build a small certified metric layer before expanding dashboard coverage.",
      "Assign business owners for executive KPIs.",
      "Create repeatable reporting patterns in Power BI or the BI tool of choice.",
      "Use fractional leadership to guide standards until a full-time team is justified.",
    ],
    related: ["when-to-hire-head-of-analytics", "what-fractional-analytics-leadership-actually-means", "why-data-teams-struggle-to-earn-trust"],
  },
  {
    title: "Why Data Teams Struggle to Earn Trust",
    slug: "why-data-teams-struggle-to-earn-trust",
    category: categories.leadership,
    service: "fractional",
    image: "data-teams-earn-trust.png",
    alt: "Data team trust growing through clearer priorities, metric ownership, and executive alignment",
    summary: "Data teams earn trust when their work is connected to business decisions, standards, and visible follow-through.",
    meta: "Data teams struggle to earn trust when they are trapped in report queues, unclear priorities, and metric disputes. Learn how to fix it.",
    lead: "Most data teams do not struggle to earn trust because they lack technical ability. They struggle because the organization has not created the conditions for their work to be trusted.",
    meeting: "If priorities shift every week, metric definitions are unresolved, executives bypass shared dashboards, and analysts are measured by ticket completion, trust will stay fragile.",
    cost: "The data team becomes both builder and buffer. It absorbs vague requests, carries undocumented business logic, and gets blamed when leadership alignment fails.",
    shift: "Trust improves when analytics work is tied to decision outcomes. That means clear intake, governed metrics, transparent tradeoffs, visible owners, and leadership support when the team says no to low-value work.",
    example: "A data team asked to build five different revenue dashboards is not failing when executives disagree about revenue. The team is exposing a governance issue leadership needs to resolve.",
    moves: [
      "Define analytics priorities in business language, not ticket categories.",
      "Protect time for cleanup and standards, not only new requests.",
      "Make metric ownership a leadership responsibility.",
      "Give analysts access to the decision context behind requests.",
      "Evaluate analytics impact by decisions improved, not dashboards shipped.",
    ],
    related: ["when-to-hire-head-of-analytics", "who-owns-this-metric-most-expensive-question-in-analytics", "how-to-build-metrics-people-actually-use"],
  },
  {
    title: "Analytics Maturity Roadmap",
    slug: "analytics-maturity-roadmap-reporting-to-decision-systems",
    category: categories.leadership,
    service: "fractional",
    image: "analytics-maturity-roadmap.png",
    alt: "Analytics maturity roadmap moving from reporting cleanup to trusted decision systems",
    summary: "Analytics maturity is the progression from scattered reporting to trusted decision systems that guide action.",
    meta: "Use this analytics maturity roadmap to move from scattered reports and dashboard sprawl toward governed metrics and trusted decision systems.",
    lead: "Analytics maturity is not measured by the number of dashboards, tools, or data sources a company has. It is measured by whether leaders can use information to make better decisions with less friction.",
    meeting: "Many companies move through predictable stages: scattered reporting, dashboard consolidation, metric governance, executive decision cadence, and eventually decision systems that connect signals to action.",
    cost: "Skipping stages creates instability. A company that buys advanced tooling before defining metric ownership will still argue about numbers. A company that builds predictive models before fixing trust will struggle to get leaders to act on them.",
    shift: "The roadmap starts with trust. Then it moves to governance, reporting focus, leadership cadence, and selective automation. Each stage should reduce decision friction, not simply increase analytical sophistication.",
    example: "A mid-sized company does not become mature by adding another BI platform. It becomes mature when executives agree on the metrics, teams know what they own, dashboards trigger action, and follow-up is visible.",
    moves: [
      "Stabilize core reporting and remove conflicting executive numbers.",
      "Create KPI ownership and definition governance.",
      "Redesign executive reporting around decisions and action thresholds.",
      "Build leadership cadence so metrics are reviewed and acted on consistently.",
      "Add advanced analytics only where trust, ownership, and response paths already exist.",
    ],
    related: ["the-difference-between-reporting-and-decision-making", "what-fractional-analytics-leadership-actually-means", "building-analytics-function-without-hiring-full-team"],
  },
  {
    title: "AI Enablement Needs Trusted Business Data",
    slug: "ai-enablement-starts-with-trusted-business-data",
    category: categories.ai,
    service: "fractional",
    image: "ai-enablement-trusted-business-data.png",
    alt: "Executive team planning AI enablement around governed business data and trusted metrics",
    summary: "AI enablement depends on trusted definitions, clean operating context, and business owners who know how decisions should change.",
    meta: "AI enablement needs trusted business data. Learn why metric governance, decision clarity, and clean reporting context matter before AI tools create value.",
    lead: "AI enablement does not start with a model. It starts with whether the business can trust the data, definitions, and decisions the model is supposed to support.",
    meeting: "Many leadership teams want AI to summarize performance, flag risk, or recommend action. Those use cases are reasonable. But if the company already argues about core metrics, AI will amplify the confusion faster than a dashboard ever could.",
    cost: "The hidden cost is false confidence. A polished AI answer can sound decisive even when the underlying metric logic is fragmented, undocumented, or owned by no one.",
    shift: "The first AI enablement move is to identify the business decisions where AI could assist, then verify the data foundation, metric ownership, and response path behind those decisions.",
    example: "An AI assistant can summarize weekly revenue risk, but it needs to know which revenue definition matters, which exceptions are approved, and which leader owns follow-up.",
    moves: [
      "Start AI use cases with the decision to be improved, not the tool to be deployed.",
      "Certify the metrics AI will summarize or reason over.",
      "Document business definitions in language leaders and operators can validate.",
      "Create human review paths for recommendations that affect customers, revenue, or staffing.",
      "Measure AI value by faster, clearer decisions rather than volume of generated outputs.",
    ],
    related: ["single-source-of-truth-myth", "kpi-governance-explained-growing-organizations", "analytics-maturity-roadmap-reporting-to-decision-systems"],
  },
  {
    title: "Prepare Reporting for AI",
    slug: "prepare-reporting-environment-for-ai",
    category: categories.ai,
    service: "health",
    image: "prepare-reporting-environment-for-ai.png",
    alt: "Modern reporting environment being prepared for AI with governed dashboards and data context",
    summary: "Preparing reporting for AI means cleaning up definitions, lineage, access, and decision context before automation scales the noise.",
    meta: "Prepare your reporting environment for AI with practical steps around data trust, metric definitions, lineage, permissions, and executive decision context.",
    lead: "Before a company connects AI to reporting, it should ask a blunt question: would we trust a human analyst using this environment without supervision?",
    meeting: "If the answer is no, AI will not magically fix the environment. It will generate summaries from conflicting dashboards, answer questions using unclear definitions, and make stale logic feel current.",
    cost: "The risk is not only technical. It is managerial. Leaders may act on AI-generated interpretation before the organization has agreed which numbers are authoritative.",
    shift: "Preparation means making the reporting environment legible to both humans and systems: certified metrics, lineage, permissions, refresh expectations, semantic definitions, and escalation rules.",
    example: "A Power BI workspace with dozens of similar revenue reports may be usable by a veteran analyst who knows the history. It is dangerous as an AI knowledge source unless the trusted assets are clearly separated from old experiments.",
    moves: [
      "Classify dashboards as certified, operational, exploratory, or retired.",
      "Clean up duplicated measures that calculate the same KPI differently.",
      "Document refresh cadence, source systems, and known exclusions for executive assets.",
      "Review permissions before exposing sensitive reporting through AI workflows.",
      "Pilot AI on one narrow decision workflow before broad rollout.",
    ],
    related: ["five-signs-your-reporting-environment-is-breaking-down", "why-nobody-trusts-your-dashboard", "building-executive-dashboards-that-create-accountability"],
  },
  {
    title: "Where AI Helps Analytics Operations",
    slug: "where-ai-actually-helps-in-analytics-operations",
    category: categories.ai,
    service: "fractional",
    image: "ai-analytics-operations.png",
    alt: "Analytics operations team using AI to summarize risks, documentation, and reporting workflows",
    summary: "AI helps analytics operations most when it reduces friction around documentation, triage, summaries, and decision preparation.",
    meta: "See where AI helps analytics operations: reporting triage, metric documentation, executive summaries, operating digests, and decision prep.",
    lead: "AI is most useful in analytics operations when it removes friction from work the team already understands.",
    meeting: "The tempting use case is to ask AI to make the decision. The better first use case is to help humans prepare for the decision with cleaner context, faster triage, and better documentation.",
    cost: "Teams that chase broad AI transformation often miss practical wins. Analysts still answer repetitive questions, executives still need weekly summaries, and metric definitions still live in scattered documents.",
    shift: "The highest-return AI opportunities usually sit around the edges of the decision system: summarizing variance commentary, drafting metric documentation, routing report requests, flagging stale assets, and preparing executive pre-reads.",
    example: "An operations team may not need a fully autonomous planning model. It may need AI to summarize exceptions across certified dashboards and assemble the issues leaders should review on Monday.",
    moves: [
      "Use AI to support analyst judgment before automating leadership judgment.",
      "Create approved source sets so AI pulls from trusted reporting assets.",
      "Apply AI to repetitive explanation and documentation work.",
      "Keep human owners accountable for decisions, thresholds, and customer impact.",
      "Review AI outputs inside the same governance process used for reporting.",
    ],
    related: ["what-fractional-analytics-leadership-actually-means", "the-difference-between-reporting-and-decision-making", "how-to-build-metrics-people-actually-use"],
  },
  {
    title: "Operations Intelligence Digest for Leaders",
    slug: "operations-intelligence-digest-for-leadership",
    category: categories.lab,
    service: "lab",
    image: "operations-intelligence-digest-leadership.png",
    alt: "Leadership team reviewing a concise operations intelligence digest with risks and actions",
    summary: "An Operations Intelligence Digest turns scattered operational signals into a concise leadership brief focused on risk, movement, and action.",
    meta: "Learn how an Operations Intelligence Digest turns scattered data, risks, and operating signals into a focused weekly leadership brief.",
    lead: "Executives do not need more places to look. They need a better way to see what changed, why it matters, and who needs to act.",
    meeting: "An Operations Intelligence Digest is not another dashboard. It is a structured brief that pulls the most important operating signals into a concise leadership-ready view.",
    cost: "Without that kind of synthesis, leaders rely on function-by-function updates. The cross-functional story arrives late, and operational risk hides between reports.",
    shift: "The digest should combine trusted metrics, exception commentary, owner commitments, and forward-looking risk into one reviewable artifact.",
    example: "A weekly digest might surface that revenue is on plan while implementation capacity is creating renewal risk three months out. That is the kind of connection a standard dashboard pack often misses.",
    moves: [
      "Define the leadership cadence the digest will support.",
      "Select only signals that affect commitments, risks, or decisions.",
      "Pair each exception with an owner and recommended follow-up.",
      "Keep the digest concise enough to be read before the meeting.",
      "Retire sections that do not change attention or action.",
    ],
    related: ["what-should-be-included-in-weekly-business-review", "stop-measuring-everything-designing-executive-reporting-that-drives-action", "the-difference-between-reporting-and-decision-making"],
  },
  {
    title: "RLS Governance and Access Design",
    slug: "governance-rls-architecture-business-issue",
    category: categories.lab,
    service: "lab",
    image: "governance-rls-architecture-business-issue.png",
    alt: "Secure analytics access architecture with governed reporting layers and executive oversight",
    summary: "Governance and RLS architecture protect trust by making access rules, metric visibility, and business responsibility explicit.",
    meta: "Learn why RLS governance and access design are business decisions that shape reporting trust, accountability, security, and scale.",
    lead: "Row-level security sounds technical until the wrong person sees the wrong number, or the right person cannot see the context needed to make a decision.",
    meeting: "Access design shapes trust. It determines which leaders can see which customers, regions, margins, forecasts, and exceptions. When those rules are unclear, reporting becomes both risky and frustrating.",
    cost: "Poor access architecture creates two costs at once: exposure risk and decision friction. Teams either see too much, see too little, or build side exports to get around the system.",
    shift: "Good governance and RLS architecture starts with business roles, decision rights, sensitivity, and ownership. The technical implementation should follow those rules.",
    example: "A regional leader may need account-level performance for their territory, while an executive needs consolidated performance and exception visibility. Those are different access patterns, not ad-hoc permission requests.",
    moves: [
      "Map access rules to business roles and decision responsibilities.",
      "Separate sensitive detail from executive summary views.",
      "Document who approves access changes and why.",
      "Test RLS with real operating scenarios, not only technical cases.",
      "Review access architecture when the org structure or customer model changes.",
    ],
    related: ["kpi-governance-explained-growing-organizations", "who-owns-this-metric-most-expensive-question-in-analytics", "prepare-reporting-environment-for-ai"],
  },
  {
    title: "Predictive Risk Intelligence",
    slug: "dashboards-to-predictive-risk-intelligence",
    category: categories.lab,
    service: "lab",
    image: "dashboards-to-predictive-risk-intelligence.png",
    alt: "Predictive risk intelligence system connecting dashboards, alerts, customer signals, and executive action",
    summary: "Predictive risk intelligence works when dashboards, operating signals, ownership, and response paths are already connected.",
    meta: "Move from dashboards to predictive risk intelligence by connecting trusted metrics, leading indicators, owners, and intervention workflows.",
    lead: "Predictive risk intelligence is not a fancier dashboard. It is a way to connect early signals to leadership attention before the lagging metric confirms the damage.",
    meeting: "Many companies want prediction because dashboards feel backward-looking. That instinct is right, but prediction only helps if the business can act on the signal.",
    cost: "A risk score without an owner becomes another number to monitor. A model without a response path creates anxiety instead of accountability.",
    shift: "The path from dashboards to predictive risk intelligence starts with trusted historical reporting, then adds leading indicators, thresholds, owners, and intervention cadence.",
    example: "Customer risk intelligence may combine usage decline, ticket aging, stakeholder turnover, billing friction, and renewal timing. The value comes when those signals route to a clear owner before the renewal is already in danger.",
    moves: [
      "Start with the risk decisions leaders already make manually.",
      "Identify leading indicators that appear before the outcome metric moves.",
      "Validate risk signals against historical outcomes and operator judgment.",
      "Assign owners and intervention playbooks before launching scores broadly.",
      "Measure whether the system changes action, not only prediction accuracy.",
    ],
    related: ["analytics-maturity-roadmap-reporting-to-decision-systems", "operations-intelligence-digest-for-leadership", "ai-enablement-starts-with-trusted-business-data"],
  },
];

function words(text) {
  return text.replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
}

function readingMinutes(article, wordCount) {
  const complexity = {
    [categories.trust]: 0,
    [categories.governance]: 1,
    [categories.reporting]: 1,
    [categories.leadership]: 2,
    [categories.ai]: 2,
    [categories.lab]: 2,
  }[article.category] || 0;
  return Math.max(6, Math.ceil(wordCount / 235) + complexity);
}

const articleDepth = {
  "why-nobody-trusts-your-dashboard": {
    sections: [
      {
        heading: "Dashboard distrust is learned behavior",
        paragraphs: [
          "Leaders do not wake up skeptical of dashboards. They become skeptical after enough meetings where the dashboard was close but not quite right, where an exception changed the story, or where the person presenting the number had to explain which version was safe to use.",
          "The important point is that distrust is usually rational. If a dashboard has been wrong, unclear, or inconsistently interpreted, executives adapt by asking for exports, side analysis, and pre-meeting reconciliation. Those workarounds become the real reporting system."
        ]
      },
      {
        heading: "Trust depends on traceability, not visual polish",
        paragraphs: [
          "A trusted dashboard lets a leader trace the number back to the business rule quickly enough to keep the conversation moving. They do not need to inspect SQL. They do need to know what is included, what is excluded, when it refreshed, and who approved the definition.",
          "This is why redesigns often disappoint. Better color, layout, and chart choice can improve comprehension, but they do not answer the deeper questions executives ask when money, staffing, customers, or board communication depend on the result."
        ]
      },
      {
        heading: "The repair starts with the numbers people argue about",
        paragraphs: [
          "The fastest path is not a full reporting inventory. Start with the five numbers that create the most friction in leadership meetings. Those metrics reveal where ownership, definitions, source systems, and decision rights are weak.",
          "Once those measures are governed, the dashboard can become smaller and stronger. Leaders do not need every possible view; they need a reliable surface for the decisions they make repeatedly."
        ]
      }
    ],
    questions: [
      "Which dashboard numbers require explanation before anyone will act?",
      "Where do leaders still ask for spreadsheets even though a dashboard exists?",
      "Which definitions are understood by analysts but not by the executive team?",
      "What would make this dashboard safe enough to use in a board or operating review?"
    ]
  },
  "hidden-cost-of-reporting-misalignment": {
    sections: [
      {
        heading: "Misalignment taxes the operating cadence",
        paragraphs: [
          "Reporting misalignment is expensive because it consumes the highest-leverage time in the company: leadership attention. The meeting that should resolve a resource tradeoff becomes a debate about which number belongs on the screen.",
          "That tax compounds. Finance prepares one view, operations prepares another, and functional leaders learn to defend their local reporting logic before discussing the business issue itself."
        ]
      },
      {
        heading: "The cost shows up outside analytics",
        paragraphs: [
          "Misaligned reporting delays pricing decisions, hiring plans, customer interventions, sales forecasts, and margin reviews. Analytics feels like the source of the pain because the numbers are visible there, but the real cost lands in slower execution.",
          "It also weakens accountability. When leaders can choose between competing versions of the truth, a missed target can become a reporting debate instead of a performance conversation."
        ]
      },
      {
        heading: "Alignment means assigning each view a job",
        paragraphs: [
          "The answer is not to collapse every view into one universal report. Finance, sales, operations, and customer teams may need different lenses. The missing discipline is deciding which lens governs which decision.",
          "A healthy environment can support multiple views as long as their purpose is explicit. Board reporting, sales coaching, cash planning, and operational triage should not silently reuse the same metric label if they mean different things."
        ]
      }
    ],
    questions: [
      "Which recurring meetings lose time to reconciling numbers?",
      "Which departments use the same metric label for different decisions?",
      "Where does reporting conflict create delayed or softened accountability?",
      "Which views should be certified for executive use versus local analysis?"
    ]
  },
  "dashboard-problem-leadership-problem": {
    sections: [
      {
        heading: "Dashboards expose unresolved leadership choices",
        paragraphs: [
          "A dashboard cannot decide what the leadership team has avoided deciding. If the executive team has not agreed on priorities, ownership, thresholds, or escalation paths, the dashboard will simply make that ambiguity visible.",
          "This is why teams can spend weeks improving a report and still hear that it does not answer the question. The question was never only visual. It was operational."
        ]
      },
      {
        heading: "Visibility without decision rights creates more noise",
        paragraphs: [
          "Leaders often ask for visibility when they actually need a decision system. Visibility shows what happened. Decision rights clarify who owns the response, how fast they must act, and what tradeoffs are acceptable.",
          "Without that structure, a dashboard becomes a neutral display of problems. Everyone can see the red number, but no one is empowered or expected to change it."
        ]
      },
      {
        heading: "The leadership team must define the operating promise",
        paragraphs: [
          "Before a dashboard build, executives should define the promise the metric is meant to manage. Is the company promising faster implementation, better margin discipline, stronger retention, or more predictable cash?",
          "Once that promise is clear, dashboard design gets easier. The report can highlight the signal, owner, threshold, and next action instead of trying to satisfy every function equally."
        ]
      }
    ],
    questions: [
      "What leadership decision is this dashboard meant to improve?",
      "Who owns the response when the number moves?",
      "Which thresholds require action rather than commentary?",
      "What tradeoff does the executive team need to settle before redesigning the report?"
    ]
  },
  "single-source-of-truth-myth": {
    sections: [
      {
        heading: "One source does not mean one interpretation",
        paragraphs: [
          "The single source of truth phrase is useful when it pushes teams toward shared logic. It becomes harmful when leaders use it to avoid naming the different business contexts that require different views.",
          "Revenue is a good example. Booked, recognized, invoiced, collected, forecasted, and recurring revenue are all legitimate. The problem is not that multiple revenue views exist. The problem is when the company pretends they are interchangeable."
        ]
      },
      {
        heading: "The real goal is governed context",
        paragraphs: [
          "Growing companies need a certified metric spine, not a fantasy that every team will stop needing context. The certified spine defines core calculations and ownership. Contextual views adapt those metrics for specific decisions.",
          "This gives leaders the consistency they need without forcing every analysis into a rigid model that fails the moment the business asks a new question."
        ]
      },
      {
        heading: "Source-of-truth work is a governance exercise",
        paragraphs: [
          "The technical architecture matters, but source-of-truth work succeeds or fails on governance. Someone must decide which definitions are certified, where exceptions live, and how changes are communicated.",
          "Without that operating layer, a clean warehouse or semantic model becomes another place where teams build competing logic."
        ]
      }
    ],
    questions: [
      "Which metrics truly need certification across the company?",
      "Which local views are valid but should not govern executive decisions?",
      "Who can approve a change to a certified definition?",
      "Where do leaders confuse different business contexts under one metric name?"
    ]
  },
  "five-signs-your-reporting-environment-is-breaking-down": {
    sections: [
      {
        heading: "Breakdown starts as small exceptions",
        paragraphs: [
          "A reporting environment rarely announces that it is failing. It starts with one manual adjustment, one trusted spreadsheet, one shadow dashboard, and one report no one wants to retire because someone important still asks for it.",
          "Those exceptions are often reasonable at the time. The problem is that nobody comes back later to decide whether the workaround should become governed logic, be retired, or remain a temporary analysis."
        ]
      },
      {
        heading: "The visible symptoms are behavioral",
        paragraphs: [
          "The best signs of breakdown are not always technical. Look at behavior: executives request exports, analysts explain the same caveats repeatedly, operators maintain private trackers, and meetings start with reconciliation.",
          "These behaviors reveal that the formal reporting system no longer carries enough trust for the business to run on it."
        ]
      },
      {
        heading: "Diagnosis should separate cause from symptom",
        paragraphs: [
          "Slow dashboards, duplicate reports, and conflicting metrics may share a root cause, but they can also come from different issues. Data quality, definition drift, access rules, source-system changes, and unclear ownership require different fixes.",
          "A good diagnosis prevents the company from rebuilding the visual layer when the real failure is governance or ownership."
        ]
      }
    ],
    questions: [
      "Which reports are used even though no one owns them?",
      "Where do manual adjustments happen before leadership meetings?",
      "Which dashboards have been replaced by side spreadsheets?",
      "What reporting pain is caused by definitions rather than tooling?"
    ]
  },
  "who-owns-this-metric-most-expensive-question-in-analytics": {
    sections: [
      {
        heading: "Ownership is not dashboard maintenance",
        paragraphs: [
          "Metric ownership is often confused with report ownership. The person who maintains the dashboard may understand the calculation, but that does not mean they should decide what the metric means for the business.",
          "A true metric owner is accountable for the definition being fit for purpose, for communicating changes, and for coordinating the business response when movement matters."
        ]
      },
      {
        heading: "Shared influence still needs one accountable owner",
        paragraphs: [
          "Many important metrics are cross-functional. Gross retention, margin, forecast accuracy, implementation cycle time, and customer health can all be influenced by several teams.",
          "Shared influence is not the same as shared ownership. If everyone owns the metric equally, nobody can resolve definition disputes or decide what action should follow."
        ]
      },
      {
        heading: "Ownership reduces politics when it is explicit",
        paragraphs: [
          "Clear ownership is not about blame. It is about making the operating system legible. Leaders can still discuss contributing factors, but they know who is responsible for keeping the metric meaningful and action-oriented.",
          "That clarity helps analytics teams step out of the referee role and back into the role of building trustworthy decision infrastructure."
        ]
      }
    ],
    questions: [
      "Who owns the business definition, not just the dashboard?",
      "Which teams influence the metric without controlling it?",
      "Who communicates definition changes to leadership?",
      "What happens when the metric moves beyond an agreed threshold?"
    ]
  },
  "kpi-governance-explained-growing-organizations": {
    sections: [
      {
        heading: "Governance should feel lightweight but real",
        paragraphs: [
          "KPI governance for a growing organization should not be a bureaucratic program. It should be a small set of operating rules that protects the metrics leaders use to allocate time, money, and accountability.",
          "The goal is not to govern every analysis. It is to protect the measures that carry executive decisions."
        ]
      },
      {
        heading: "The catalog is only useful if it has authority",
        paragraphs: [
          "Many teams create metric dictionaries that quickly become stale. A catalog matters only when it is tied to owners, change control, reporting assets, and leadership usage.",
          "If a KPI appears in the catalog but leaders still use another version in meetings, the catalog is documentation theater."
        ]
      },
      {
        heading: "Governance must include change management",
        paragraphs: [
          "Definitions will change as products, pricing, territories, and customer models evolve. Mature governance does not prevent change; it makes change visible and controlled.",
          "Leaders should know when a definition changed, why it changed, who approved it, and whether historical comparisons are affected."
        ]
      }
    ],
    questions: [
      "Which KPIs are important enough to certify?",
      "Who can approve a KPI definition change?",
      "How are leaders notified when a definition changes?",
      "Which reports are allowed to use uncertified versions?"
    ]
  },
  "why-executive-teams-argue-about-numbers": {
    sections: [
      {
        heading: "Number arguments usually hide context arguments",
        paragraphs: [
          "Executives often argue about numbers because they are using the same metric name for different purposes. One leader is thinking about coaching, another about forecasting, another about board communication.",
          "The argument sounds technical, but the conflict is often about which decision context should govern the conversation."
        ]
      },
      {
        heading: "Functional incentives shape metric interpretation",
        paragraphs: [
          "Sales, finance, operations, and customer teams naturally emphasize different versions of performance. Those perspectives can all be useful, but they become corrosive when the leadership team has not agreed which one is authoritative.",
          "A healthy executive team can name the local view and the enterprise view without treating either as dishonest."
        ]
      },
      {
        heading: "Pre-meeting alignment protects leadership time",
        paragraphs: [
          "If a metric is regularly disputed, the dispute should be resolved before the executive meeting. Leadership time should be used for decisions, tradeoffs, and commitments.",
          "Recurring metric debates should be treated as governance defects. Once identified, they need owners, definitions, and decision rules."
        ]
      }
    ],
    questions: [
      "Which number debates repeat across meetings?",
      "Which version should govern board reporting?",
      "Which version is valid only for local operating use?",
      "Who is responsible for resolving the dispute before the next meeting?"
    ]
  },
  "kpi-ownership-framework-every-leadership-team-needs": {
    sections: [
      {
        heading: "A framework prevents ownership from becoming a label",
        paragraphs: [
          "Many companies add an owner column to a KPI list and assume ownership is solved. It is not. Ownership needs decision rights, cadence, thresholds, and a clear distinction between accountable and contributing teams.",
          "Without those elements, the owner label becomes decorative. The metric still drifts when definitions are challenged or performance moves."
        ]
      },
      {
        heading: "The accountable owner protects metric meaning",
        paragraphs: [
          "The accountable owner does not control every input. They are responsible for making sure the metric remains useful for the leadership decision it supports.",
          "That means coordinating with contributors, approving changes, and ensuring the metric is reviewed in the right operating cadence."
        ]
      },
      {
        heading: "Thresholds turn ownership into action",
        paragraphs: [
          "Ownership becomes concrete when the team agrees what movement requires response. A KPI without thresholds invites commentary. A KPI with thresholds creates an expectation of action.",
          "The framework should define what happens when the metric moves, who responds, and where follow-up is reviewed."
        ]
      }
    ],
    questions: [
      "Who is accountable for the KPI definition?",
      "Who contributes to movement but does not own the metric?",
      "Which meeting reviews the KPI?",
      "What threshold creates escalation or intervention?"
    ]
  },
  "how-to-build-metrics-people-actually-use": {
    sections: [
      {
        heading: "A useful metric has a job",
        paragraphs: [
          "Metrics people actually use are built around decisions, not availability. The first question should be what the metric helps someone decide, not whether the data can be calculated.",
          "If a metric does not shape prioritization, escalation, resource allocation, coaching, or follow-up, it may be interesting but it is unlikely to become part of the operating rhythm."
        ]
      },
      {
        heading: "Usage depends on timing and ownership",
        paragraphs: [
          "Even a well-defined metric can fail if it arrives too late or has no owner. A weekly operating metric needs to be available before the meeting and tied to someone responsible for interpreting movement.",
          "The design challenge is to make the metric appear at the moment when the user can still act."
        ]
      },
      {
        heading: "Fewer metrics can create more action",
        paragraphs: [
          "Teams often add metrics to satisfy every stakeholder. That makes dashboards feel complete but less useful. Users need hierarchy: primary signal, supporting context, and diagnostic drilldown.",
          "A metric set becomes valuable when users can tell which numbers matter now and which numbers are background context."
        ]
      }
    ],
    questions: [
      "What decision gets better if this metric is trusted?",
      "Who reviews it and at what cadence?",
      "What action should follow movement?",
      "Which related metrics are context rather than primary signals?"
    ]
  },
  "why-executive-dashboards-fail": {
    sections: [
      {
        heading: "Executive dashboards fail when they become summary pages",
        paragraphs: [
          "A summary page tries to represent the whole business. An executive dashboard should represent the decisions leaders need to make. Those are different design problems.",
          "When every function contributes its favorite number, the dashboard becomes politically inclusive but operationally weak."
        ]
      },
      {
        heading: "Executives need signal, variance, and responsibility",
        paragraphs: [
          "The executive layer should show what changed, whether it matters, and who owns the response. A chart without variance context forces leaders to interpret movement on the fly.",
          "The best dashboards reduce interpretation time. They make the important exception obvious and leave diagnostic detail one layer down."
        ]
      },
      {
        heading: "The meeting should shape the dashboard",
        paragraphs: [
          "Executive dashboards should be designed around the actual review cadence. A weekly operating review, monthly business review, and board meeting should not all use the same page.",
          "Different cadences require different levels of detail, commentary, and accountability."
        ]
      }
    ],
    questions: [
      "Which executive meeting will use this dashboard?",
      "Which decisions should the page support?",
      "What information belongs in drilldown rather than the first view?",
      "How will leaders know who owns the next action?"
    ]
  },
  "stop-measuring-everything-designing-executive-reporting-that-drives-action": {
    sections: [
      {
        heading: "Measuring everything protects the company from focus",
        paragraphs: [
          "A crowded executive report can feel responsible because nothing is omitted. In practice, it lets every team point to a number while avoiding the few signals that should drive action.",
          "Executive reporting should force prioritization. If everything is visible with equal weight, the report is not doing its job."
        ]
      },
      {
        heading: "Action reporting separates signal from context",
        paragraphs: [
          "The first page should show the metrics that trigger decisions. Diagnostic metrics can support the conversation, but they should not compete with the primary operating signals.",
          "This separation helps leaders move from explanation to commitment. They can see the issue, understand the likely driver, and assign follow-up."
        ]
      },
      {
        heading: "Metric pruning is a leadership discipline",
        paragraphs: [
          "Removing a metric can be harder than adding one because each metric has a sponsor. That is why executive reporting needs periodic pruning tied to strategy and cadence.",
          "A metric should remain in the executive view only if it changes attention, action, or accountability."
        ]
      }
    ],
    questions: [
      "Which metrics actually trigger leadership action?",
      "Which metrics are diagnostic rather than executive-level?",
      "Which numbers have stayed in the report only because they are familiar?",
      "What would leaders stop doing if this metric disappeared?"
    ]
  },
  "what-should-be-included-in-weekly-business-review": {
    sections: [
      {
        heading: "A WBR should manage movement, not narrate status",
        paragraphs: [
          "The weekly business review is most valuable when it highlights what changed since the last review and what needs leadership attention now.",
          "Department updates can inform the discussion, but they should not dominate it. The meeting should surface cross-functional risk, commitments, and decisions."
        ]
      },
      {
        heading: "The pack should separate facts from asks",
        paragraphs: [
          "A strong WBR pack makes it clear which items are informational and which require a decision. Leaders should not have to infer whether a slide is asking for action.",
          "This is where reporting design and meeting design meet. The format should make the operating ask visible."
        ]
      },
      {
        heading: "Commitments from last week matter as much as metrics",
        paragraphs: [
          "A WBR that does not revisit prior commitments becomes a status meeting. The pack should show what owners committed to, what changed, and where follow-up is still open.",
          "That discipline turns reporting into accountability instead of commentary."
        ]
      }
    ],
    questions: [
      "What changed materially since last week?",
      "Which exceptions require leadership attention?",
      "Which prior commitments need follow-up?",
      "What decisions must be made before the next review?"
    ]
  },
  "the-difference-between-reporting-and-decision-making": {
    sections: [
      {
        heading: "Reporting explains the past; decisions change the future",
        paragraphs: [
          "Reporting organizes what happened. Decision making chooses what to do next. A dashboard can support a decision, but it does not create one by itself.",
          "Companies get into trouble when they keep adding reports instead of designing the decision process those reports are supposed to inform."
        ]
      },
      {
        heading: "Decision systems need thresholds and response paths",
        paragraphs: [
          "A decision system defines when movement matters, who owns the response, and how follow-up is reviewed. Without those rules, reporting remains descriptive.",
          "The difference is visible in meetings. Reporting-heavy meetings ask what happened. Decision-oriented meetings ask what needs to change."
        ]
      },
      {
        heading: "Analytics maturity comes from closing the loop",
        paragraphs: [
          "The strongest analytics functions do not stop at insight delivery. They help the organization learn whether decisions worked.",
          "That feedback loop is what turns reporting into a management system rather than a record of activity."
        ]
      }
    ],
    questions: [
      "What decision is this report meant to improve?",
      "What threshold changes the conversation?",
      "Who owns the response?",
      "How will the leadership team review whether the decision worked?"
    ]
  },
  "building-executive-dashboards-that-create-accountability": {
    sections: [
      {
        heading: "Accountability requires more than visibility",
        paragraphs: [
          "Visibility tells the team that something changed. Accountability tells the team who owns the response and where follow-up will happen.",
          "Executive dashboards should make that chain clear. Otherwise, the red metric becomes a shared concern with no operating consequence."
        ]
      },
      {
        heading: "Owner context belongs near the metric",
        paragraphs: [
          "If leaders have to leave the dashboard to find the owner, threshold, or current commitment, the dashboard is not supporting accountability well enough.",
          "Owner context does not need to be heavy. It can be a simple label, exception note, or link to the current initiative. The point is to make responsibility visible at the moment of interpretation."
        ]
      },
      {
        heading: "Commitment tracking completes the loop",
        paragraphs: [
          "A dashboard creates accountability when it connects metric movement to commitments and then returns to those commitments in the next cadence.",
          "That loop prevents dashboards from becoming performance theater. Leaders can see whether the organization acted, not only whether the number moved."
        ]
      }
    ],
    questions: [
      "Which metrics need explicit owners on the dashboard?",
      "What threshold requires an owner response?",
      "Where are commitments captured and reviewed?",
      "How does the dashboard distinguish accountability from blame?"
    ]
  },
  "when-to-hire-head-of-analytics": {
    sections: [
      {
        heading: "The trigger is decision complexity, not report volume",
        paragraphs: [
          "A growing company may have many reports before it needs a Head of Analytics. The stronger signal is when analytics work requires senior prioritization, governance, and executive influence.",
          "If the team is constantly choosing between urgent requests, cleanup work, metric disputes, and strategic analysis, leadership capacity is becoming the constraint."
        ]
      },
      {
        heading: "The role should own standards and tradeoffs",
        paragraphs: [
          "A Head of Analytics should not simply manage a queue. The role should set standards, define trusted metrics, shape the roadmap, and help executives understand which requests are worth doing.",
          "Without that mandate, the hire can become an expensive reporting manager rather than an analytics leader."
        ]
      },
      {
        heading: "Fractional leadership can de-risk the timing",
        paragraphs: [
          "Many companies need senior judgment before they can justify a full-time leader. Fractional analytics leadership can establish governance, roadmap, and cadence while the business learns what permanent role it truly needs.",
          "This avoids hiring too early for a vague mandate or too late after reporting trust has already eroded."
        ]
      }
    ],
    questions: [
      "Is analytics demand now cross-functional and contested?",
      "Do executives need help deciding what not to build?",
      "Are analysts mediating leadership alignment issues?",
      "Would a full-time hire have a clear mandate today?"
    ]
  },
  "what-fractional-analytics-leadership-actually-means": {
    sections: [
      {
        heading: "Fractional leadership is senior judgment, not spare capacity",
        paragraphs: [
          "Fractional analytics leadership should not be treated as a part-time analyst arrangement. The value is experienced judgment applied to standards, governance, executive alignment, and team enablement.",
          "The work often includes reviewing dashboards, shaping the roadmap, coaching internal staff, and helping leadership make tradeoffs."
        ]
      },
      {
        heading: "The role bridges executives and builders",
        paragraphs: [
          "Executives often know the pain but not the analytics design required to fix it. Analysts often know the data but not the leadership tradeoff behind the request.",
          "A fractional leader translates between those layers so the team builds fewer one-off reports and more durable operating infrastructure."
        ]
      },
      {
        heading: "The engagement should leave capability behind",
        paragraphs: [
          "Good fractional work should not create dependency. It should leave behind clearer standards, better metric ownership, stronger Power BI patterns, and a more disciplined cadence.",
          "That is what separates advisory leadership from a temporary reporting resource."
        ]
      }
    ],
    questions: [
      "What senior analytics decisions are currently unresolved?",
      "Where does the team need standards rather than more output?",
      "Which executive tradeoffs need facilitation?",
      "What capability should remain after the engagement?"
    ]
  },
  "building-analytics-function-without-hiring-full-team": {
    sections: [
      {
        heading: "A function is an operating model, not a headcount plan",
        paragraphs: [
          "A credible analytics function can exist before a full team exists. It needs priorities, standards, owners, tools, and cadence.",
          "The mistake is assuming the company must choose between a full department and scattered reporting. A lean operating model can create structure before headcount scales."
        ]
      },
      {
        heading: "The first hires are not always the first needs",
        paragraphs: [
          "Companies often hire for report production because the pain is visible. But the first need may be governance, prioritization, or a reusable semantic layer.",
          "A lean function should clarify what work belongs with internal operators, what needs senior guidance, and what should be outsourced or deferred."
        ]
      },
      {
        heading: "The roadmap should protect focus",
        paragraphs: [
          "A small analytics function cannot say yes to every request. It needs a roadmap tied to business decisions, not a backlog ranked by who asked most recently.",
          "This discipline helps a lean team build trust because stakeholders understand what is being prioritized and why."
        ]
      }
    ],
    questions: [
      "Which analytics decisions matter most this quarter?",
      "What standards must exist before more reports are built?",
      "Which work should stay internal versus external?",
      "What would justify the next full-time analytics hire?"
    ]
  },
  "why-data-teams-struggle-to-earn-trust": {
    sections: [
      {
        heading: "Trust is shaped by the operating environment",
        paragraphs: [
          "Data teams are often judged on whether the business trusts analytics, but trust depends on more than technical skill. It depends on priorities, definitions, leadership support, and how requests enter the system.",
          "If the organization sends unclear requests and unresolved metric debates to the data team, trust will remain fragile no matter how capable the analysts are."
        ]
      },
      {
        heading: "Ticket queues can hide strategic work",
        paragraphs: [
          "When analytics is managed only as a request queue, the team is rewarded for output volume. Cleanup, governance, and decision design become hard to justify even though they are the work that improves trust.",
          "Leaders need to protect capacity for the structural work that makes future reporting faster and safer."
        ]
      },
      {
        heading: "Credibility grows when analytics says no well",
        paragraphs: [
          "Trusted data teams do not accept every request at face value. They clarify the decision, challenge low-value work, and explain tradeoffs in business language.",
          "That kind of pushback requires executive sponsorship. Without it, analysts become order takers and trust erodes."
        ]
      }
    ],
    questions: [
      "Are analysts measured by dashboards shipped or decisions improved?",
      "Which requests should be challenged before build work starts?",
      "Does leadership support analytics when it says no?",
      "What structural work is being deferred because urgent requests dominate?"
    ]
  },
  "analytics-maturity-roadmap-reporting-to-decision-systems": {
    sections: [
      {
        heading: "Maturity is about reducing decision friction",
        paragraphs: [
          "Analytics maturity is not a tool checklist. A company is more mature when leaders can make important decisions with less reconciliation, fewer side channels, and clearer ownership.",
          "The roadmap should therefore be measured by decision quality, not dashboard count."
        ]
      },
      {
        heading: "Skipping stages creates fragile sophistication",
        paragraphs: [
          "Advanced analytics built on untrusted reporting rarely gets adopted. Predictive models, AI assistants, and complex dashboards all depend on basic trust, definitions, and response paths.",
          "The sequence matters: stabilize reporting, govern metrics, redesign executive cadence, and then add intelligence layers where the business can act."
        ]
      },
      {
        heading: "Each stage should change how leaders work",
        paragraphs: [
          "A roadmap is useful only if each stage changes behavior. Reporting cleanup should reduce reconciliation. Governance should reduce disputes. Decision systems should increase follow-through.",
          "If a stage produces assets but no change in executive cadence, the company has improved analytics output without improving analytics maturity."
        ]
      }
    ],
    questions: [
      "Where is the company on the path from reporting to decision systems?",
      "Which trust issues must be resolved before advanced analytics?",
      "What behavior should change at the next maturity stage?",
      "Which intelligence initiatives are premature until governance improves?"
    ]
  },
  "ai-enablement-starts-with-trusted-business-data": {
    sections: [
      {
        heading: "AI amplifies the quality of the operating context",
        paragraphs: [
          "AI can summarize, retrieve, draft, and recommend quickly. That speed is useful only if the underlying business context is reliable.",
          "If definitions are disputed or dashboards conflict, AI will make the confusion feel more polished. The organization may move faster in the wrong direction."
        ]
      },
      {
        heading: "The first AI use cases should be decision-adjacent",
        paragraphs: [
          "For most growing companies, the best early AI analytics use cases support human judgment rather than replace it. Examples include summarizing variance, preparing meeting briefs, documenting metrics, and surfacing exceptions.",
          "These use cases create value while keeping decision authority with accountable leaders."
        ]
      },
      {
        heading: "Governance determines whether AI is trusted",
        paragraphs: [
          "AI enablement needs source control, metric certification, access rules, and human review. Without those guardrails, leaders will either distrust the tool or trust it too much.",
          "The work is not anti-innovation. It is what allows AI to be used responsibly in operating decisions."
        ]
      }
    ],
    questions: [
      "Which AI use cases depend on certified metrics?",
      "What sources should AI be allowed to use?",
      "Who reviews AI-generated recommendations before action?",
      "Which decisions are too sensitive for automation today?"
    ]
  },
  "prepare-reporting-environment-for-ai": {
    sections: [
      {
        heading: "AI readiness starts with reporting hygiene",
        paragraphs: [
          "Before connecting AI to reporting, leaders should know which dashboards are certified, which are exploratory, and which should be retired.",
          "Otherwise AI may retrieve stale assets, summarize unofficial metrics, or answer questions from reports that humans no longer trust."
        ]
      },
      {
        heading: "Semantic clarity matters more with AI",
        paragraphs: [
          "AI systems need business-readable definitions and context. A measure name alone is rarely enough. The system needs grain, filters, exclusions, refresh timing, and allowed use.",
          "This is where metric documentation becomes operational infrastructure rather than compliance work."
        ]
      },
      {
        heading: "Access design becomes more important",
        paragraphs: [
          "AI can make information easier to retrieve, which makes permissions more important. Leaders need to decide what data can be summarized, by whom, and at what level of detail.",
          "Reporting environments prepared for AI have clear boundaries between sensitive detail, executive summaries, and general knowledge."
        ]
      }
    ],
    questions: [
      "Which reporting assets are safe for AI retrieval?",
      "Which metrics need clearer semantic definitions?",
      "What sensitive data should be excluded from AI workflows?",
      "Where should the first narrow AI reporting pilot start?"
    ]
  },
  "where-ai-actually-helps-in-analytics-operations": {
    sections: [
      {
        heading: "AI is strongest around repeatable context work",
        paragraphs: [
          "Analytics teams spend substantial time explaining variance, documenting logic, triaging requests, and preparing leaders for meetings. AI can reduce friction in those workflows when trusted sources are defined.",
          "That is different from asking AI to own the decision. The best use cases make humans faster and better prepared."
        ]
      },
      {
        heading: "Operational AI needs approved source sets",
        paragraphs: [
          "If AI can pull from every report, document, and spreadsheet, the answer may be broad but unreliable. Teams need approved source sets for different use cases.",
          "A weekly executive summary should draw from certified metrics and current operating notes, not old dashboards or experimental analysis."
        ]
      },
      {
        heading: "Value should be measured by workflow improvement",
        paragraphs: [
          "The value of AI in analytics operations is not the number of prompts run. It is whether analysts spend less time on repetitive explanation and leaders get better prepared for decisions.",
          "Useful measures include cycle time, reduced rework, fewer duplicate questions, and clearer meeting pre-reads."
        ]
      }
    ],
    questions: [
      "Which repetitive analytics tasks consume senior time?",
      "Which source sets are approved for AI summaries?",
      "Where can AI prepare context without making the decision?",
      "How will the team measure workflow improvement?"
    ]
  },
  "operations-intelligence-digest-for-leadership": {
    sections: [
      {
        heading: "A digest is a leadership brief, not a dashboard dump",
        paragraphs: [
          "An Operations Intelligence Digest should synthesize what leaders need to know before the operating meeting. It is not a collection of every chart that changed.",
          "The digest should answer a small number of questions: what moved, why it matters, who owns the response, and what decision is needed."
        ]
      },
      {
        heading: "The strongest digest connects functions",
        paragraphs: [
          "Function-by-function updates often miss the cross-functional story. A capacity issue may create revenue risk. A support backlog may become renewal exposure. A sales mix change may affect delivery margin.",
          "The digest earns its place when it surfaces these connections before they become surprises."
        ]
      },
      {
        heading: "It should create meeting leverage",
        paragraphs: [
          "A good digest lets leaders arrive with shared context. The meeting can then focus on tradeoffs, commitments, and escalation rather than discovery.",
          "If the digest does not change the quality of the meeting, it is probably too broad, too late, or too disconnected from ownership."
        ]
      }
    ],
    questions: [
      "Which leadership meeting should the digest improve?",
      "Which risks need synthesis across functions?",
      "Who owns each exception surfaced in the digest?",
      "What should leaders decide after reading it?"
    ]
  },
  "governance-rls-architecture-business-issue": {
    sections: [
      {
        heading: "Access design shapes business behavior",
        paragraphs: [
          "RLS and access architecture decide what people can see, compare, export, and act on. Those rules affect trust and accountability, not just security.",
          "If access is too loose, sensitive data spreads. If it is too restrictive, leaders create side channels to get the context they need."
        ]
      },
      {
        heading: "Business roles should drive technical rules",
        paragraphs: [
          "The best access models start with role, decision responsibility, and sensitivity. Technical implementation should follow business design.",
          "A regional operator, executive, finance analyst, and customer-facing manager may all need different levels of detail for legitimate reasons."
        ]
      },
      {
        heading: "RLS needs governance after launch",
        paragraphs: [
          "Access rules drift as territories, products, customers, and leadership roles change. A launch-time RLS model is not enough.",
          "The company needs a process for approving access changes, testing scenarios, and reviewing whether the architecture still matches the operating model."
        ]
      }
    ],
    questions: [
      "Which business roles need which level of detail?",
      "Who approves access changes?",
      "Where do current permissions create workarounds?",
      "How often should access architecture be reviewed?"
    ]
  },
  "dashboards-to-predictive-risk-intelligence": {
    sections: [
      {
        heading: "Prediction is useful only when the business can respond",
        paragraphs: [
          "Predictive risk intelligence fails when it stops at a score. Leaders need to know what signal changed, why it matters, who owns the intervention, and how quickly action is required.",
          "A model without a response path is just a more sophisticated dashboard."
        ]
      },
      {
        heading: "Leading indicators should come from operating reality",
        paragraphs: [
          "Good risk systems combine historical data with operator judgment. Usage decline, ticket aging, stakeholder change, billing friction, and delivery delays may all matter, but their weight depends on the business model.",
          "The strongest signal set is built with the teams who understand how risk actually appears before the lagging metric moves."
        ]
      },
      {
        heading: "Risk intelligence should be reviewed as a system",
        paragraphs: [
          "Once launched, predictive intelligence needs monitoring. Leaders should review whether alerts are timely, whether owners act, and whether interventions change outcomes.",
          "Accuracy matters, but adoption and action matter just as much. A moderately accurate signal that changes behavior can be more valuable than a precise model no one uses."
        ]
      }
    ],
    questions: [
      "Which risks are visible too late today?",
      "What leading indicators appear before the outcome changes?",
      "Who owns intervention when risk is flagged?",
      "How will the company measure whether risk intelligence changes outcomes?"
    ]
  }
};

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function header(prefix = "") {
  return `<header aria-label="Parallax site navigation" class="site-header">
<a aria-label="Parallax Data Lab home" class="site-brand" href="${prefix}index.html"><img alt="Parallax Data Lab" src="${prefix}assets/parallax_data_lab_original_transparent.png"/></a>
<button aria-controls="primary-navigation" aria-expanded="false" aria-label="Toggle navigation" class="mobile-nav-toggle" type="button"><span></span><span></span><span></span><em>Menu</em></button>
<nav id="primary-navigation" aria-label="Primary navigation">
<a href="${prefix}index.html">Home</a>
<a href="${prefix}how-we-help.html">How We Help</a>
<div class="nav-dropdown nav-dropdown-offerings">
<a class="nav-dropdown-toggle" href="${prefix}our-offerings.html">Our Offerings</a>
<div aria-label="Offerings sections" class="nav-dropdown-menu nav-menu-hierarchy">
<a class="nav-menu-parent" href="${prefix}our-offerings.html"><span>Offerings Overview</span></a>
<a class="nav-menu-child nav-menu-fit-check nav-menu-path-01" href="${prefix}free-fit-check.html"><span>Free Fit Check</span><em>Free</em></a>
<a class="nav-menu-child nav-menu-path-02" href="${prefix}analytics-health-check.html"><span>Analytics Health Check</span></a>
<a class="nav-menu-child nav-menu-path-03" href="${prefix}decision-system-reset.html"><span>Decision System Reset</span></a>
<a class="nav-menu-child nav-menu-path-04" href="${prefix}fractional-analytics.html"><span>Fractional Analytics Consulting</span></a>
</div>
</div>
<div class="nav-dropdown nav-dropdown-intelligence">
<a class="nav-dropdown-toggle" href="${prefix}intelligence-lab.html">Intelligence Lab</a>
<div aria-label="Intelligence Lab services" class="nav-dropdown-menu nav-dropdown-menu-intelligence nav-menu-hierarchy">
<a class="nav-menu-parent" href="${prefix}intelligence-lab.html"><span>Intelligence Lab Overview</span></a>
<a class="nav-menu-child" href="${prefix}intelligence-lab.html#operations-intelligence-digest"><span>Operations Intelligence Digest</span></a>
<a class="nav-menu-child" href="${prefix}intelligence-lab.html#governance-rls-architecture"><span>Governance &amp; RLS Architecture</span></a>
<a class="nav-menu-child" href="${prefix}intelligence-lab.html#enterprise-outcome-studio"><span>Enterprise Outcome Studio</span></a>
<a class="nav-menu-child" href="${prefix}intelligence-lab.html#predictive-risk-intelligence"><span>Predictive Risk Intelligence</span></a>
</div>
</div>
<a href="${prefix}insights.html" aria-current="page">Insights</a>
<a href="${prefix}about.html">About</a>
</nav>
</header>`;
}

function footer(prefix = "") {
  return `<footer aria-label="Site footer" class="site-footer site-footer-refined">
  <div class="site-footer-inner">
    <div class="site-footer-col site-footer-about">
      <a class="site-footer-brand" href="${prefix}index.html">Parallax Data Lab</a>
      <p>Analytics trust, decision systems, and senior data strategy for teams ready to make reporting useful again.</p>
      <a class="site-footer-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">jonahnr@gmail.com</a>
      <a class="site-footer-contact-button" href="${prefix}about.html#contact-us">Contact Us</a>
    </div>
    <nav aria-label="Footer core pages" class="site-footer-col">
      <h3>Core pages</h3>
      <a href="${prefix}index.html">Home</a>
      <a href="${prefix}how-we-help.html">How We Help</a>
      <a href="${prefix}our-offerings.html">Our Offerings</a>
      <a href="${prefix}intelligence-lab.html">Intelligence Lab</a>
      <a href="${prefix}insights.html">Insights</a>
      <a href="${prefix}about.html">About</a>
      <a href="${prefix}privacy-policy.html">Privacy Policy</a>
    </nav>
    <nav aria-label="Footer core services" class="site-footer-col">
      <h3>Services</h3>
      <a href="${prefix}dashboard-trust-scorecard.html">Dashboard Trust Scorecard</a>
      <a href="${prefix}free-fit-check.html">Free Fit Check</a>
      <a href="${prefix}analytics-health-check.html">Analytics Health Check</a>
      <a href="${prefix}decision-system-reset.html">Decision System Reset</a>
      <a href="${prefix}fractional-analytics.html">Fractional Analytics Consulting</a>
    </nav>
    <nav aria-label="Footer intelligence lab services" class="site-footer-col site-footer-intel">
      <h3>Intelligence Lab Services</h3>
      <a href="${prefix}intelligence-lab.html#operations-intelligence-digest">Operations Intelligence Digest</a>
      <a href="${prefix}intelligence-lab.html#governance-rls-architecture">Governance &amp; RLS Architecture</a>
      <a href="${prefix}intelligence-lab.html#enterprise-outcome-studio">Enterprise Outcome Studio</a>
      <a href="${prefix}intelligence-lab.html#predictive-risk-intelligence">Predictive Risk Intelligence</a>
    </nav>
    <div class="site-footer-col site-footer-contact">
      <h3>Contact</h3>
      <a class="site-footer-secondary" href="https://calendly.com/jonahnr/parallax-data-lab-intro-call">Schedule Intro Call</a>
      <a class="site-footer-secondary" href="${prefix}about.html#contact-us">Email Jonah</a>
      <a class="site-footer-secondary" href="https://www.linkedin.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    </div>
  </div>
  <div class="site-footer-bottom">
    <p>&copy; 2026 Parallax Data Lab. All rights reserved.</p>
  </div>
</footer>`;
}

function serviceHref(service, prefix) {
  return `${prefix}${service.path}`;
}

function bodyCopy(a, options = {}) {
  const articleHref = options.articleHref || ((slug) => `${slug}.html`);
  const servicePrefix = options.servicePrefix || "../";
  const service = services[a.service];
  const fitCheck = services.fitCheck;
  const relatedLinks = a.related
    .map((slug) => articles.find((item) => item.slug === slug))
    .filter(Boolean);
  const relatedText = relatedLinks
    .map((r) => `<a href="${articleHref(r.slug)}">${esc(r.title)}</a>`)
    .join(", ");
  const categoryNote = {
    [categories.trust]: "For analytics trust issues, the repair has to make uncertainty visible and manageable. Leaders need to see where the number comes from, which assumptions are approved, and which conversations still require judgment. Hiding that complexity behind a cleaner page only delays the next trust break.",
    [categories.governance]: "For KPI governance issues, the repair has to balance clarity with speed. The organization needs enough rules to protect important decisions, but not so many rules that every analytical question becomes an approval process. Governance should make the trusted path obvious.",
    [categories.reporting]: "For executive reporting issues, the repair has to follow the meeting rhythm. The strongest report is not the most complete report; it is the report that helps the right leaders see movement, understand risk, and commit to action during the cadence where accountability happens.",
    [categories.leadership]: "For analytics leadership issues, the repair has to create decision authority. Someone has to translate business priorities into analytics standards, say no to distracting work, and help executives understand which problems require process, people, or system changes.",
    [categories.ai]: "For AI enablement issues, the repair has to connect new capabilities to trusted operating context. AI can accelerate summaries, triage, and recommendations, but only if leaders agree which data is authoritative and which human owner remains accountable for the decision.",
    [categories.lab]: "For Intelligence Lab initiatives, the repair has to turn analytical capability into a repeatable operating asset. The work should connect systems, owners, access, and leadership cadence so intelligence becomes part of how the company runs.",
  }[a.category];
  const depth = articleDepth[a.slug] || {
    sections: [
      {
        heading: "What leaders need to understand",
        paragraphs: [a.example, a.shift],
      },
      {
        heading: "Where the work gets practical",
        paragraphs: [
          "The practical work starts by separating the visible reporting request from the operating issue underneath it. Leaders need to know whether the problem is definition quality, ownership, access, cadence, source-system design, or decision behavior.",
          "That distinction matters because each problem requires a different fix. A dashboard rebuild will not solve a metric ownership issue, and a governance document will not help if the leadership meeting never uses the metric to make a decision.",
        ],
      },
      {
        heading: "How to move from reporting to action",
        paragraphs: [
          "The strongest analytics improvements create a visible change in how leaders work. Meetings get shorter, follow-up gets clearer, and the number becomes a prompt for action rather than another topic for debate.",
          "That is the standard for deciding whether the work is done. If the business has a nicer report but the same operating friction, the reporting layer has improved while the decision system has not.",
        ],
      },
    ],
    questions: [
      "What decision should this work improve?",
      "Who owns the metric or operating response?",
      "Which definition or cadence needs to be clarified?",
      "How will leaders know the change is working?",
    ],
  };
  const conclusion = `For this specific problem, the important move is to stop treating "${a.title}" as an isolated reporting request. ${a.summary} ${a.shift}`;
  const resourceNote = service && service.label !== fitCheck.label
    ? `<p>For a deeper look at the related Parallax capability, see <a href="${serviceHref(service, servicePrefix)}">${esc(service.label)}</a>. Use it as context for the kind of work that may follow once the initial fit and diagnosis are clear.</p>`
    : "";
  const sectionHtml = depth.sections
    .map((section) => `<h2>${esc(section.heading)}</h2>
${section.paragraphs.map((paragraph) => `<p>${esc(paragraph)}</p>`).join("\n")}`)
    .join("\n");
  const questionHtml = depth.questions
    .map((question) => `<li>${esc(question)}</li>`)
    .join("\n");
  const moveLabels = [
    "Define the decision boundary.",
    "Make ownership visible.",
    "Turn the report into an operating cadence.",
  ];
  const implementationHtml = a.moves
    .map((move, index) => `<p><strong>${esc(moveLabels[index] || "Protect the behavior.")}</strong> ${esc(move)} The detail that matters is making this visible in the workflow where the metric is used, not leaving it as a note in a project plan. Assign the person who can resolve disagreement, the meeting where progress will be reviewed, and the rule for changing course when the signal moves.</p>`)
    .join("\n");

  return `
<p>${esc(a.lead)}</p>
<p>${esc(a.meeting)}</p>
<p>${esc(a.cost)}</p>
${sectionHtml}
<h2>How executives should diagnose it</h2>
<p>Do not start by asking for a larger report inventory. Start with the recurring conversation where this issue creates the most friction. Look at who is in the room, what number is being debated, what action is being delayed, and which source or definition people trust when pressure rises.</p>
<p>${esc(categoryNote)}</p>
<p>A good diagnosis should produce a short list of operating causes, not a long list of reporting complaints. For this topic, pay particular attention to ${esc(a.summary.charAt(0).toLowerCase() + a.summary.slice(1))} The fix should address that cause directly enough that leaders can see what will change in the next meeting, not just in the next dashboard release.</p>
<h2>What to change first</h2>
<p>${esc(a.shift)}</p>
<ul>
${a.moves.map((move) => `<li>${esc(move)}</li>`).join("\n")}
</ul>
<h2>Implementation notes for ${esc(a.title.toLowerCase())}</h2>
${implementationHtml}
<p>There is also a sequencing issue leaders should take seriously. If the team starts with tooling, the work can look productive while the same decision friction survives underneath. If the team starts with ownership, definitions, and cadence, the eventual reporting changes have a much better chance of being adopted.</p>
<p>This is especially important in small and mid-sized companies because informal context can hide system weakness for a long time. A finance leader, operator, or founder may know which number is safe because they remember how the report was built. That knowledge does not scale cleanly when new leaders join, when the company adds locations or business lines, or when a board asks for more consistent operating visibility.</p>
<p>The practical standard is simple: a capable leader who was not involved in the original build should be able to understand the metric, trust its purpose, and know what kind of action it is meant to trigger. When that is true, analytics becomes less dependent on individual memory and more useful as shared operating infrastructure.</p>
<p>Keep the first change narrow enough to prove. One high-friction metric, one leadership cadence, or one decision workflow is usually a better starting point than a broad transformation program. The goal is to create a visible improvement in trust, ownership, or speed, then extend the pattern.</p>
<p>For executives, the test is behavioral. After the change, the leadership team should spend less time asking where the number came from and more time deciding what the number requires. If the meeting still ends with a request for another export, the system has not moved far enough.</p>
<h2>Questions to settle before the next build cycle</h2>
<ul>
${questionHtml}
</ul>
<p>Related reading from the Parallax Data Lab library: ${relatedText}.</p>
${resourceNote}
<h2>Conclusion</h2>
<p>${esc(conclusion)}</p>
<p>If this article describes what is happening inside your reporting environment, Parallax Data Lab can help. Start with the <a href="${serviceHref(fitCheck, servicePrefix)}">${esc(fitCheck.label)}</a>, a free 15-minute meeting to clarify where trust is breaking, what should be governed, and what kind of decision system your leadership team actually needs.</p>`;
}

function articlePage(a, options = {}) {
  const prefix = options.prefix || "../";
  const backHref = options.backHref || "../insights.html";
  const returnHref = options.returnHref || "../insights.html";
  const articleHref = options.articleHref || ((slug) => `${slug}.html`);
  const service = services[a.service];
  const fitCheck = services.fitCheck;
  const url = `${site}/insights/${a.slug}/`;
  const copy = bodyCopy(a, {
    articleHref,
    servicePrefix: prefix,
  });
  const wc = words(copy);
  const readTime = readingMinutes(a, wc);
  const relatedLinks = a.related
    .map((slug) => articles.find((item) => item.slug === slug))
    .filter(Boolean)
    .map((r) => `<a href="${articleHref(r.slug)}">${esc(r.title)}</a>`)
    .join("\n");
  const schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: a.title,
    description: a.meta,
    image: `${site}/assets/insights/${a.image}`,
    author: { "@type": "Organization", name: "Parallax Data Lab" },
    publisher: {
      "@type": "Organization",
      name: "Parallax Data Lab",
      logo: {
        "@type": "ImageObject",
        url: `${site}/assets/parallax_data_lab_original_transparent.png`,
      },
    },
    mainEntityOfPage: url,
    datePublished: today,
    dateModified: today,
  };
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${esc(a.title)} | Parallax Data Lab</title>
<meta content="${esc(a.meta)}" name="description"/>
<link rel="canonical" href="${url}"/>
<link href="${prefix}home.css?v=107" rel="stylesheet"/>
<meta name="theme-color" content="#0b1745"/>
<link href="${prefix}apple-touch-icon.png?v=107" rel="apple-touch-icon"/><link href="${prefix}favicon.svg?v=107" rel="icon" type="image/svg+xml"/><link href="${prefix}favicon.ico?v=107" rel="icon" sizes="any"/>
<meta content="article" property="og:type"/><meta content="Parallax Data Lab" property="og:site_name"/><meta content="${esc(a.title)} | Parallax Data Lab" property="og:title"/><meta content="${esc(a.meta)}" property="og:description"/><meta content="${url}" property="og:url"/><meta content="${site}/assets/insights/${a.image}" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="${esc(a.title)} | Parallax Data Lab" name="twitter:title"/><meta content="${esc(a.meta)}" name="twitter:description"/><meta content="${site}/assets/insights/${a.image}" name="twitter:image"/>
<script type="application/ld+json">${JSON.stringify(schema, null, 2)}</script>
</head>
<body>
<canvas aria-hidden="true" id="constellation"></canvas>
${header(prefix)}
<main class="article-page">
<article class="insight-article">
<header class="article-hero">
<div class="article-hero-copy">
<a class="article-back-link" href="${backHref}"><span aria-hidden="true">&larr;</span> Back to Insights</a>
<p class="article-category">${esc(a.category)}</p>
<h1>${esc(a.title)}</h1>
<p class="article-summary">${esc(a.summary)}</p>
<div class="article-meta"><span>${readTime} min read</span><span>Updated ${today}</span></div>
</div>
<figure class="article-hero-media">
<img src="${prefix}assets/insights/${a.image}" alt="${esc(a.alt)}"/>
</figure>
</header>
<div class="article-shell">
<aside class="article-sidebar" aria-label="Article details">
<p><strong>Summary</strong>${esc(a.summary)}</p>
<p><strong>Best next step</strong><a href="${serviceHref(fitCheck, prefix)}">${esc(fitCheck.label)}</a></p>
${service && service.label !== fitCheck.label ? `<p><strong>Relevant service</strong><a href="${serviceHref(service, prefix)}">${esc(service.label)}</a></p>` : ""}
<nav aria-label="Related articles">
<strong>Related</strong>
${relatedLinks}
</nav>
</aside>
<div class="article-content">
${copy}
<p class="article-return-link"><a href="${returnHref}">Back to Insights Library</a></p>
</div>
</div>
</article>
<section class="insights-conversion-cta reveal-card" aria-labelledby="article-fit-check-title">
<div>
<p class="page-kicker">Free 15-minute fit check</p>
<h2 id="article-fit-check-title">Turn this article into the right next analytics move.</h2>
<p>If this issue is showing up in your dashboards, reporting cadence, or leadership meetings, use the free Fit Check to clarify the problem, the likely root cause, and whether an assessment, reset, or operating digest is the right path.</p>
</div>
<div class="insights-cta-actions">
<a class="secondary-action" href="${prefix}dashboard-trust-scorecard.html">Get the Scorecard</a>
<a class="primary-action" href="${serviceHref(fitCheck, prefix)}">Request the 15-Minute Fit Check</a>
</div>
</section>
</main>
${footer(prefix)}
<script src="${prefix}home.js?v=107"></script>
</body>
</html>
`;
}

function hubPage(options = {}) {
  const prefix = options.prefix || "";
  const articleHref = options.articleHref || ((slug) => `insights/${slug}/`);
  const cards = articles
    .map((a) => {
      const wc = words(bodyCopy(a, {
        articleHref,
        servicePrefix: prefix,
      }));
      const readTime = readingMinutes(a, wc);
      return `<article class="insight-card" data-category="${esc(a.category)}">
<img src="${prefix}assets/insights/${a.image}" alt="${esc(a.alt)}"/>
<div class="insight-card-body">
<span>${esc(a.category)}</span>
<h2><a href="${articleHref(a.slug)}">${esc(a.title)}</a></h2>
<p>${esc(a.summary)}</p>
<footer><em>${readTime} min read</em><a href="${articleHref(a.slug)}">Read article</a></footer>
</div>
</article>`;
    })
    .join("\n");
  const schema = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: "Insights and Articles | Parallax Data Lab",
    description: "Articles on reporting overload, dashboard trust, KPI ownership, executive decision systems, AI readiness, operational intelligence, and analytics leadership.",
    url: `${site}/insights/`,
  };
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Analytics Insights for Reporting Overload | Parallax Data Lab</title>
<meta content="Articles on reporting overload, dashboard trust, KPI ownership, executive decision systems, AI readiness, operational intelligence, and analytics leadership." name="description"/>
<link rel="canonical" href="${site}/insights/"/>
<link href="${prefix}home.css?v=107" rel="stylesheet"/>
<meta name="theme-color" content="#0b1745"/>
<link href="${prefix}apple-touch-icon.png?v=107" rel="apple-touch-icon"/><link href="${prefix}favicon.svg?v=107" rel="icon" type="image/svg+xml"/><link href="${prefix}favicon.ico?v=107" rel="icon" sizes="any"/>
<meta content="website" property="og:type"/><meta content="Parallax Data Lab" property="og:site_name"/><meta content="Analytics Insights for Reporting Overload | Parallax Data Lab" property="og:title"/><meta content="Articles on reporting overload, dashboard trust, KPI ownership, executive decision systems, AI readiness, operational intelligence, and analytics leadership." property="og:description"/><meta content="${site}/insights/" property="og:url"/><meta content="${site}/social-preview.png" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="Analytics Insights for Reporting Overload | Parallax Data Lab" name="twitter:title"/><meta content="Articles on reporting overload, dashboard trust, KPI ownership, executive decision systems, AI readiness, operational intelligence, and analytics leadership." name="twitter:description"/><meta content="${site}/social-preview.png" name="twitter:image"/>
<script type="application/ld+json">${JSON.stringify(schema, null, 2)}</script>
</head>
<body>
<canvas aria-hidden="true" id="constellation"></canvas>
${header(prefix)}
<main class="insights-page" data-active-filter="all">
<section class="insights-hero">
<p class="page-kicker">Insights</p>
<h1>Executive articles for leaders turning data noise into decision clarity.</h1>
<p>Practical guidance on reporting overload, dashboard trust, KPI ownership, executive reporting, AI readiness, operational intelligence digests, and analytics leadership for growing companies.</p>
</section>
<section class="insights-conversion-cta insights-hub-cta reveal-card" aria-labelledby="insights-fit-check-title">
<div>
<p class="page-kicker">Free 15-minute fit check</p>
<h2 id="insights-fit-check-title">Not sure which analytics problem is actually costing you time?</h2>
<p>Use the free Fit Check to pressure-test whether the issue is dashboard trust, reporting overload, KPI ownership, decision cadence, or a missing operational digest.</p>
</div>
<div class="insights-cta-actions">
<a class="secondary-action" href="${prefix}dashboard-trust-scorecard.html">Get the Scorecard</a>
<a class="primary-action" href="${prefix}free-fit-check.html">Request the 15-Minute Fit Check</a>
</div>
</section>
<section class="insights-filter-band" aria-label="Article categories">
<button class="is-active" type="button" data-insight-filter="all">All</button>
${Object.values(categories).map((category) => `<button type="button" data-insight-filter="${esc(category)}">${esc(category)}</button>`).join("\n")}
</section>
<section class="insights-search-band" aria-label="Search articles">
<label for="insights-search">Search articles</label>
<input id="insights-search" type="search" placeholder="Search by topic, metric, AI, Power BI, governance..." data-insights-search autocomplete="off"/>
</section>
<p class="insights-results-note" data-insights-results>${articles.length} articles</p>
<section class="insight-card-grid" aria-label="Parallax Data Lab article library">
${cards}
</section>
</main>
${footer(prefix)}
<script src="${prefix}home.js?v=107"></script>
</body>
</html>
`;
}

function heroSvg(a, index) {
  const labels = a.title.split(/[?:]/)[0].slice(0, 38);
  const accentX = 180 + (index % 5) * 76;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="860" viewBox="0 0 1440 860" role="img" aria-label="${esc(a.alt)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07133a"/>
      <stop offset="0.45" stop-color="#0b1d55"/>
      <stop offset="1" stop-color="#102d6b"/>
    </linearGradient>
    <radialGradient id="glow" cx="72%" cy="28%" r="55%">
      <stop offset="0" stop-color="#d9b45f" stop-opacity="0.34"/>
      <stop offset="0.45" stop-color="#377dff" stop-opacity="0.20"/>
      <stop offset="1" stop-color="#07133a" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="18"/>
    </filter>
  </defs>
  <rect width="1440" height="860" fill="url(#bg)"/>
  <rect width="1440" height="860" fill="url(#glow)"/>
  <g opacity="0.14" stroke="#88b7ff" stroke-width="1">
    ${Array.from({ length: 15 }, (_, i) => `<path d="M0 ${120 + i * 48} C ${260 + i * 8} ${80 + i * 12}, ${520 + i * 15} ${210 + i * 18}, 1440 ${90 + i * 42}" fill="none"/>`).join("")}
  </g>
  <g transform="translate(170 150)">
    <rect x="0" y="0" width="760" height="500" rx="28" fill="#071942" stroke="#7aa7ff" stroke-opacity="0.35"/>
    <rect x="42" y="54" width="676" height="72" rx="18" fill="#122b64" stroke="#d9b45f" stroke-opacity="0.45"/>
    <g fill="#6fa8ff" opacity="0.88">
      <rect x="58" y="158" width="148" height="232" rx="16"/>
      <rect x="234" y="220" width="148" height="170" rx="16"/>
      <rect x="410" y="112" width="148" height="278" rx="16"/>
      <rect x="586" y="260" width="86" height="130" rx="16"/>
    </g>
    <path d="M72 430 C 190 320, 300 360, 420 236 S 620 158, 702 206" fill="none" stroke="#d9b45f" stroke-width="8" stroke-linecap="round"/>
    <circle cx="${accentX}" cy="${210 + (index % 4) * 35}" r="62" fill="#d9b45f" opacity="0.16" filter="url(#soft)"/>
    <text x="58" y="100" fill="#f6f8ff" font-family="Inter, Arial, sans-serif" font-size="30" font-weight="700">${esc(labels)}</text>
  </g>
  <g transform="translate(960 190)" fill="none" stroke-linecap="round">
    <circle cx="140" cy="140" r="102" stroke="#d9b45f" stroke-width="3" opacity="0.7"/>
    <circle cx="140" cy="140" r="54" stroke="#80aaff" stroke-width="2" opacity="0.8"/>
    <path d="M40 318 H 360" stroke="#80aaff" stroke-opacity="0.45" stroke-width="2"/>
    <path d="M72 370 H 310" stroke="#80aaff" stroke-opacity="0.28" stroke-width="2"/>
    <path d="M110 422 H 280" stroke="#d9b45f" stroke-opacity="0.50" stroke-width="3"/>
  </g>
</svg>`;
}

function ensureDir(dir) {
  fs.mkdirSync(path.join(root, dir), { recursive: true });
}

function write(file, content) {
  fs.writeFileSync(path.join(root, file), content.replace(/\n{3,}/g, "\n\n"), "utf8");
}

function updateShellNavigation() {
  const htmlFiles = fs.readdirSync(root).filter((file) => file.endsWith(".html") && file !== "insights.html");
  for (const file of htmlFiles) {
    const full = path.join(root, file);
    let content = fs.readFileSync(full, "utf8");
    content = content.replace(/<a href="insights\.html">Insights<\/a>\s*/g, "");
    content = content.replace(/<a href="about\.html">About<\/a>/, `<a href="insights.html">Insights</a>\n<a href="about.html">About</a>`);
    content = content.replace(/<a href="intelligence-lab\.html">Intelligence Lab<\/a>\s*<a href="about\.html">About<\/a>/, `<a href="intelligence-lab.html">Intelligence Lab</a>\n      <a href="insights.html">Insights</a>\n      <a href="about.html">About</a>`);
    content = content.replace(/<a href="insights\.html">Insights<\/a>\s*<a href="insights\.html">Insights<\/a>/g, `<a href="insights.html">Insights</a>`);
    fs.writeFileSync(full, content, "utf8");
  }
}

function appendStyles() {
  const cssPath = path.join(root, "home.css");
  let css = fs.readFileSync(cssPath, "utf8");
  const marker = "/* Insights article library */";
  if (!css.includes(marker)) {
    css += `

${marker}
.insights-page,
.article-page {
  color: #f6f8ff;
  min-height: 100vh;
  padding-top: 108px;
}
.insights-page {
  background:
    radial-gradient(circle at 14% 18%, rgba(69, 190, 255, 0.18), transparent 24rem),
    radial-gradient(circle at 86% 14%, rgba(245, 181, 68, 0.14), transparent 22rem),
    linear-gradient(180deg, rgba(13, 31, 76, 0.48), rgba(9, 24, 62, 0.88));
}
.insights-hero,
.article-hero,
.article-shell {
  width: min(1180px, calc(100% - 40px));
  margin: 0 auto;
}
.insights-hero {
  padding: clamp(56px, 9vw, 112px) 0 34px;
}
.insights-hero h1,
.article-hero h1 {
  max-width: 920px;
  margin: 0;
  color: #ffffff;
  font-size: clamp(2.45rem, 5vw, 5.9rem);
  line-height: 0.95;
  letter-spacing: 0;
}
.insights-hero p,
.article-summary {
  max-width: 760px;
  color: rgba(234, 241, 255, 0.82);
  font-size: clamp(1.04rem, 1.7vw, 1.3rem);
  line-height: 1.65;
}
.insights-filter-band {
  width: min(1180px, calc(100% - 40px));
  margin: 0 auto 30px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.insights-filter-band span,
.article-category,
.insight-card-body span {
  color: #f0c96c;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.72rem;
  font-weight: 900;
}
.insights-filter-band span {
  border: 1px solid rgba(217, 180, 95, 0.34);
  border-radius: 999px;
  padding: 9px 13px;
  background: rgba(10, 25, 70, 0.72);
}
.insight-card-grid {
  width: min(1180px, calc(100% - 40px));
  margin: 0 auto clamp(72px, 10vw, 128px);
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}
.insight-card {
  overflow: hidden;
  border-radius: 8px;
  background: linear-gradient(145deg, rgba(9, 25, 68, 0.94), rgba(17, 42, 96, 0.86));
  border: 1px solid rgba(136, 183, 255, 0.18);
  box-shadow: 0 24px 70px rgba(0, 0, 0, 0.24);
}
.insights-page[data-active-filter="all"] .insight-card {
  background: linear-gradient(145deg, rgba(13, 34, 82, 0.96), rgba(25, 58, 118, 0.9));
  border-color: rgba(136, 183, 255, 0.26);
}
.insight-card img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  display: block;
}
.insight-card-body {
  padding: 22px;
}
.insight-card h2 {
  margin: 10px 0 12px;
  font-size: clamp(1.1rem, 1.7vw, 1.45rem);
  line-height: 1.14;
}
.insight-card h2 a,
.article-content a,
.article-sidebar a {
  color: #ffffff;
  text-decoration-color: rgba(217, 180, 95, 0.8);
  text-underline-offset: 4px;
}
.insight-card p {
  color: rgba(234, 241, 255, 0.76);
  line-height: 1.58;
}
.insight-card footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-top: 18px;
}
.insight-card footer em {
  color: rgba(234, 241, 255, 0.64);
  font-style: normal;
}
.insight-card footer a,
.article-back-link {
  color: #f0c96c;
  font-weight: 900;
}
.article-hero {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(320px, 0.95fr);
  gap: clamp(28px, 5vw, 68px);
  align-items: center;
  padding: clamp(44px, 7vw, 92px) 0 42px;
}
.article-hero-media {
  margin: 0;
}
.article-hero-media img {
  width: 100%;
  border-radius: 8px;
  border: 1px solid rgba(136, 183, 255, 0.22);
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.32);
}
.article-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 22px;
}
.article-meta span {
  border: 1px solid rgba(136, 183, 255, 0.22);
  border-radius: 999px;
  padding: 8px 12px;
  color: rgba(234, 241, 255, 0.72);
  background: rgba(8, 22, 62, 0.72);
}
.article-shell {
  display: grid;
  grid-template-columns: 280px minmax(0, 760px);
  gap: clamp(26px, 5vw, 72px);
  align-items: start;
  padding-bottom: clamp(74px, 11vw, 132px);
}
.article-sidebar {
  position: sticky;
  top: 110px;
  border-radius: 8px;
  padding: 22px;
  background: rgba(8, 22, 62, 0.78);
  border: 1px solid rgba(136, 183, 255, 0.18);
}
.article-sidebar p,
.article-sidebar nav {
  margin: 0 0 18px;
  color: rgba(234, 241, 255, 0.72);
  line-height: 1.55;
}
.article-sidebar strong,
.article-sidebar a {
  display: block;
  margin-bottom: 8px;
}
.article-content {
  color: rgba(246, 248, 255, 0.88);
  font-size: 1.06rem;
  line-height: 1.78;
}
.article-content h2 {
  color: #ffffff;
  margin: 42px 0 14px;
  font-size: clamp(1.55rem, 3vw, 2.35rem);
  line-height: 1.08;
  letter-spacing: 0;
}
.article-content p {
  margin: 0 0 20px;
}
.article-content ul {
  margin: 0 0 28px;
  padding-left: 22px;
}
.article-content li {
  margin-bottom: 10px;
  padding-left: 4px;
}
@media (max-width: 980px) {
  .insight-card-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .article-hero,
  .article-shell {
    grid-template-columns: 1fr;
  }
  .article-sidebar {
    position: static;
  }
}
@media (max-width: 640px) {
  .insights-page,
  .article-page {
    padding-top: 88px;
  }
  .insight-card-grid {
    grid-template-columns: 1fr;
  }
  .insights-hero,
  .article-hero,
  .article-shell,
  .insights-filter-band,
  .insights-search-band,
  .insight-card-grid {
    width: min(100% - 28px, 1180px);
  }
  .insight-card footer {
    align-items: flex-start;
    flex-direction: column;
  }
}
`;
  }
  const polishMarker = "/* Insights article library v2 filters and spacing */";
  if (!css.includes(polishMarker)) {
    css += `

${polishMarker}
.insights-page {
  padding-top: 76px;
}
.insights-hero {
  padding: clamp(30px, 5vw, 58px) 0 8px;
}
.insights-hero h1 {
  font-size: clamp(2.35rem, 4.35vw, 4.95rem);
}
.insights-hero h1,
.article-hero h1 {
  line-height: 1.05;
  margin-bottom: 18px;
}
.insights-hero h1 + p {
  display: block;
  clear: both;
  margin-top: 0;
  margin-bottom: 0;
}
.insights-filter-band {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
  margin-top: 4px;
  margin-bottom: 10px;
  flex-wrap: wrap;
  overflow-x: visible;
  scrollbar-width: auto;
  max-width: 760px;
}
.insights-filter-band button {
  flex: 0 1 auto;
  border: 1px solid rgba(217, 180, 95, 0.34);
  border-radius: 999px;
  padding: 9px 13px;
  background: rgba(10, 25, 70, 0.72);
  color: #f0c96c;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.72rem;
  font-weight: 900;
  cursor: pointer;
  transition: border-color 180ms ease, background 180ms ease, color 180ms ease, transform 180ms ease;
}
.insights-filter-band button:hover,
.insights-filter-band button:focus-visible,
.insights-filter-band button.is-active {
  background: rgba(217, 180, 95, 0.16);
  border-color: rgba(217, 180, 95, 0.72);
  color: #ffffff;
}
.insights-filter-band button:focus-visible {
  outline: 2px solid rgba(217, 180, 95, 0.8);
  outline-offset: 3px;
}
.insights-search-band {
  width: min(1180px, calc(100% - 40px));
  margin: 6px auto 8px;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
.insights-search-band label {
  display: block;
  margin-bottom: 5px;
  color: rgba(234, 241, 255, 0.72);
  font-size: 0.78rem;
  font-weight: 900;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.insights-search-band input {
  width: min(680px, 100%);
  min-height: 42px;
  border: 1px solid rgba(136, 183, 255, 0.32);
  border-radius: 8px;
  padding: 10px 12px;
  background: rgba(7, 19, 58, 0.78);
  color: #ffffff;
  font: inherit;
  box-shadow: 0 18px 48px rgba(0, 0, 0, 0.18);
}
.insights-search-band input::placeholder {
  color: rgba(234, 241, 255, 0.48);
}
.insights-search-band input:focus {
  outline: 2px solid rgba(217, 180, 95, 0.78);
  outline-offset: 3px;
  border-color: rgba(217, 180, 95, 0.72);
}
.insight-card.is-filtered-out {
  display: none;
}
.insight-card-grid {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
.insights-results-note {
  width: min(1180px, calc(100% - 40px));
  margin: 0 auto 10px;
  color: rgba(234, 241, 255, 0.72);
  font-weight: 800;
}
.article-back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  width: fit-content;
  margin-bottom: 14px;
  border: 1px solid rgba(217, 180, 95, 0.42);
  border-radius: 999px;
  padding: 8px 12px;
  background: rgba(217, 180, 95, 0.12);
  text-decoration: none;
}
.article-back-link:hover,
.article-back-link:focus-visible,
.article-return-link a:hover,
.article-return-link a:focus-visible {
  color: #ffffff;
  border-color: rgba(217, 180, 95, 0.78);
}
.article-return-link {
  margin-top: 34px !important;
}
.article-return-link a {
  display: inline-flex;
  align-items: center;
  width: fit-content;
  border: 1px solid rgba(217, 180, 95, 0.42);
  border-radius: 999px;
  padding: 10px 14px;
  color: #f0c96c;
  font-weight: 900;
  text-decoration: none;
  background: rgba(217, 180, 95, 0.12);
}
.insight-card img,
.article-hero-media img {
  background: #07133a;
}
@media (max-width: 640px) {
  .insights-page {
    padding-top: 84px;
  }
  .insights-hero {
    padding-bottom: 12px;
  }
  .insights-filter-band {
    margin-top: 4px;
    gap: 8px;
  }
  .insights-filter-band button {
    padding: 8px 10px;
    font-size: 0.66rem;
  }
}
`;
  }
  fs.writeFileSync(cssPath, css, "utf8");
}

function updateSitemap() {
  const urls = [
    ["", "1.00", "weekly"],
    ["how-we-help/", "0.85", "monthly"],
    ["our-offerings/", "0.95", "weekly"],
    ["free-fit-check/", "0.98", "weekly"],
    ["dashboard-trust-scorecard/", "0.92", "weekly"],
    ["analytics-health-check/", "0.92", "weekly"],
    ["decision-system-reset/", "0.90", "monthly"],
    ["fractional-analytics/", "0.90", "monthly"],
    ["intelligence-lab/", "0.85", "monthly"],
    ["insights/", "0.85", "weekly"],
    ...articles.map((a) => [`insights/${a.slug}/`, "0.70", "monthly"]),
    ["about/", "0.75", "monthly"],
    ["privacy-policy/", "0.30", "yearly"],
  ];
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(([loc, priority, freq]) => `  <url>
    <loc>${site}/${loc}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${freq}</changefreq>
    <priority>${priority}</priority>
  </url>`)
  .join("\n")}
</urlset>
`;
  write("sitemap.xml", xml);
}

function updateRedirects() {
  const staticNoSlash = [
    "how-we-help",
    "our-offerings",
    "free-fit-check",
    "dashboard-trust-scorecard",
    "dashboard-trust-scorecard-download",
    "analytics-health-check",
    "decision-system-reset",
    "fractional-analytics",
    "intelligence-lab",
    "insights",
    "about",
    "privacy-policy",
    "scorecard-thank-you",
    "thank-you",
  ];
  const staticClean = [
    ["how-we-help", "how-we-help.html"],
    ["our-offerings", "our-offerings.html"],
    ["free-fit-check", "free-fit-check.html"],
    ["dashboard-trust-scorecard", "dashboard-trust-scorecard.html"],
    ["dashboard-trust-scorecard-download", "dashboard-trust-scorecard-download.html"],
    ["analytics-health-check", "analytics-health-check.html"],
    ["decision-system-reset", "decision-system-reset.html"],
    ["fractional-analytics", "fractional-analytics.html"],
    ["intelligence-lab", "intelligence-lab.html"],
    ["insights", "insights.html"],
    ["about", "about.html"],
    ["privacy-policy", "privacy-policy.html"],
    ["scorecard-thank-you", "scorecard-thank-you.html"],
    ["thank-you", "thank-you.html"],
  ];
  const articleRoutes = articles.map((article) => article.slug);
  const redirects = `# Cloudflare Pages clean URL routing for Parallax Data Lab
# This package keeps flat .html files and relative asset paths so files are easy to open locally.
# Cloudflare serves the clean public URLs and rewrites nested asset requests back to root assets.

# Shared asset rewrites for clean URL pages using relative paths
/:slug/home.css /home.css 200
/:slug/home.js /home.js 200
/:slug/assets/* /assets/:splat 200
/:slug/favicon.svg /favicon.svg 200
/:slug/favicon.ico /favicon.ico 200
/:slug/apple-touch-icon.png /apple-touch-icon.png 200
/:slug/social-preview.png /social-preview.png 200

# Shared asset rewrites for insight article paths that use ../ relative assets
/insights/home.css /home.css 200
/insights/home.js /home.js 200
/insights/assets/* /assets/:splat 200
/insights/favicon.svg /favicon.svg 200
/insights/favicon.ico /favicon.ico 200
/insights/apple-touch-icon.png /apple-touch-icon.png 200
/insights/social-preview.png /social-preview.png 200

# Shared asset rewrites for nested insight article clean URLs
/insights/:slug/home.css /home.css 200
/insights/:slug/home.js /home.js 200
/insights/:slug/assets/* /assets/:splat 200
/insights/:slug/favicon.svg /favicon.svg 200
/insights/:slug/favicon.ico /favicon.ico 200
/insights/:slug/apple-touch-icon.png /apple-touch-icon.png 200
/insights/:slug/social-preview.png /social-preview.png 200

# No-trailing-slash cleanup
${staticNoSlash.map((slug) => `/${slug} /${slug}/ 301`).join("\n")}
${articleRoutes.map((slug) => `/insights/${slug} /insights/${slug}/ 301`).join("\n")}

# Clean URL rewrites
${staticClean.map(([clean, file]) => `/${clean}/ /${file} 200`).join("\n")}
${articleRoutes.map((slug) => `/insights/${slug}/ /insights/${slug}.html 200`).join("\n")}

# Redirect old .html URLs to clean URLs
${staticClean.map(([clean, file]) => `/${file} /${clean}/ 301`).join("\n")}
${articleRoutes.map((slug) => `/insights/${slug}.html /insights/${slug}/ 301`).join("\n")}

# Homepage cleanup
/index.html / 301
`;
  write("_redirects", redirects);
}

function updateReadme() {
  const readmePath = path.join(root, "README.md");
  let readme = fs.readFileSync(readmePath, "utf8");
  if (!readme.includes("insights.html")) {
    readme = readme.replace("- `intelligence-lab.html`", "- `insights.html` - Filterable SEO article hub with executive analytics articles.\n- `insights/*.html` - Individual article pages for analytics trust, KPI governance, executive reporting, analytics leadership, AI enablement, and Intelligence Lab initiatives.\n- `intelligence-lab.html`");
    readme = readme.replace("- `home.css` - Shared styling", "- `assets/insights/*.png` - Generated article hero photos in the Parallax visual style.\n- `home.css` - Shared styling");
    readme = readme.replace("- Intelligence Lab: `intelligence-lab.html`", "- Intelligence Lab: `intelligence-lab.html`\n- Insights: `insights.html`");
  }
  readme = readme
    .replace("SEO article hub with 20 executive analytics articles", "Filterable SEO article hub with executive analytics articles")
    .replace("Individual article pages for analytics trust, KPI governance, executive reporting, and analytics leadership.", "Individual article pages for analytics trust, KPI governance, executive reporting, analytics leadership, AI enablement, and Intelligence Lab initiatives.")
    .replace("`assets/insights/*.svg` - Article hero image placeholders in the Parallax visual style.", "`assets/insights/*.png` - Generated article hero photos in the Parallax visual style.");
  fs.writeFileSync(readmePath, readme, "utf8");
}

function main() {
  ensureDir("insights");
  ensureDir(path.join("assets", "insights"));
  articles.forEach((article) => {
    const articleHtml = articlePage(article, {
      prefix: "../",
      backHref: "../insights.html",
      returnHref: "../insights.html",
      articleHref: (slug) => `${slug}.html`,
    });
    const cleanArticleHtml = articlePage(article, {
      prefix: "../../",
      backHref: "../",
      returnHref: "../",
      articleHref: (slug) => `../${slug}/`,
    });
    write(path.join("insights", `${article.slug}.html`), articleHtml);
    ensureDir(path.join("insights", article.slug));
    write(path.join("insights", article.slug, "index.html"), cleanArticleHtml);
  });
  const hubHtml = hubPage({
    prefix: "",
    articleHref: (slug) => `insights/${slug}/`,
  });
  const cleanHubHtml = hubPage({
    prefix: "../",
    articleHref: (slug) => `${slug}/`,
  });
  write("insights.html", hubHtml);
  write(path.join("insights", "index.html"), cleanHubHtml);
  [
    ["how-we-help", "how-we-help.html"],
    ["our-offerings", "our-offerings.html"],
    ["free-fit-check", "free-fit-check.html"],
    ["dashboard-trust-scorecard", "dashboard-trust-scorecard.html"],
    ["dashboard-trust-scorecard-download", "dashboard-trust-scorecard-download.html"],
    ["analytics-health-check", "analytics-health-check.html"],
    ["decision-system-reset", "decision-system-reset.html"],
    ["fractional-analytics", "fractional-analytics.html"],
    ["intelligence-lab", "intelligence-lab.html"],
    ["about", "about.html"],
    ["privacy-policy", "privacy-policy.html"],
    ["scorecard-thank-you", "scorecard-thank-you.html"],
    ["thank-you", "thank-you.html"],
  ].forEach(([clean, file]) => {
    const source = fs.readFileSync(path.join(root, file), "utf8");
    const cleanHtml = source
      .replace(/<head>/, '<head>\n<base href="../">')
      .replace(/href="#/g, `href="${file}#`);
    ensureDir(clean);
    write(path.join(clean, "index.html"), cleanHtml);
  });
  appendStyles();
  updateShellNavigation();
  updateSitemap();
  updateRedirects();
  updateReadme();

  const counts = articles.map((a) => ({ slug: a.slug, words: words(bodyCopy(a)) }));
  console.log(JSON.stringify({ generated: articles.length, counts }, null, 2));
}

main();


from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


HOME_MAIN = r'''<main class="home-page">
<section class="hero-section" id="top">
<a aria-label="Parallax Data Lab home" class="hero-brand motion-layer" data-depth="0.08" href="index.html">
<img alt="Parallax Data Lab logo" class="hero-logo" src="assets/parallax_data_lab_original_transparent.png" decoding="async">
</a>
<div aria-hidden="true" class="hero-rule"></div>
<div class="hero-copy motion-layer" data-depth="-0.05">
<h1>Business intelligence consulting for teams that no longer trust their reporting.</h1>
<p>Parallax helps growing teams consolidate dashboards, automate recurring reports, define reliable KPIs, and build executive reporting systems people can actually use.</p>
<div class="hero-fit-check" aria-label="Free Fit Check invitation">
<div class="hero-fit-check-copy">
<span class="hero-fit-check-label">Free 15-minute reporting consult</span>
<strong>Find out what is actually breaking trust—and what to fix first.</strong>
<p>Bring one dashboard, KPI, or reporting bottleneck. Leave with a practical recommendation and no sales-pressure maze.</p>
</div>
<div class="hero-actions">
<a class="primary-action" href="free-fit-check.html">Get My Free Fit Check</a>
<a class="secondary-action" href="free-fit-check.html#what-you-get">See What You’ll Get</a>
</div>
</div>
<div class="hero-expertise-nav" aria-label="Explore expertise by reporting need">
<span class="hero-expertise-label">Explore by reporting need</span>
<div class="hero-expertise-links">
<a href="power-bi-consultant-cincinnati.html"><strong>Power BI</strong><small>Build or repair dashboards</small></a>
<a href="kpi-reporting-consulting.html"><strong>KPI Strategy</strong><small>Build executive reporting that drives action</small></a>
<a href="reporting-automation-consulting.html"><strong>Reporting Automation</strong><small>Remove recurring manual work</small></a>
<a href="data-quality-review.html"><strong>Reporting Reliability</strong><small>Trace and resolve conflicting numbers</small></a>
<a href="dashboard-trust-governance.html"><strong>BI Governance</strong><small>Clarify ownership, access, and trust</small></a>
<a href="data-integration-analytics-architecture.html"><strong>Analytics Architecture</strong><small>Connect sources and build for scale</small></a>
</div>
</div>
</div>
</section>
<section class="share-link-panel share-link-compact" aria-label="Share this page">
<span class="share-link-label">Share</span>
<button type="button" data-native-share="https://parallaxdatalab.com/" data-share-title="Parallax Data Lab | Business Intelligence Consulting">Share Link</button>
<button type="button" data-copy-share="https://parallaxdatalab.com/">Copy</button>
<a class="share-link-social" href="https://www.linkedin.com/sharing/share-offsite/?url=https://parallaxdatalab.com/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
<a class="share-link-social" href="https://x.com/intent/post?text=Parallax%20Data%20Lab%20%7C%20Business%20Intelligence%20Consulting%20https%3A%2F%2Fparallaxdatalab.com%2F" target="_blank" rel="noopener noreferrer">X</a>
<a class="share-link-social" href="mailto:?subject=Parallax Data Lab | Business Intelligence Consulting&body=https://parallaxdatalab.com/">Email</a>
</section>
<section class="diagnostic-section reveal-card">
<h2>Dashboard Trust Breaks Beneath The Surface</h2>
<div class="diagnostic-panel">
<article>
<div>
<h3>Reports multiply faster than ownership.</h3>
<p>Each report solves a local need, but definitions, logic, and ownership drift unless the foundation is governed.</p>
</div>
<img alt="Abstract analytics network expanding without a clear owner" class="diagnostic-image" src="assets/home-generated/diagnostic-owner-drift.webp" loading="lazy" decoding="async">
</article>
<article>
<div>
<h3>The fix is structural, not cosmetic.</h3>
<p>Shared definitions, reusable logic, and clear owners turn dashboards back into decision tools.</p>
</div>
<img alt="Balanced analytics structure connecting dashboards and decisions" class="diagnostic-image" src="assets/home-generated/diagnostic-structural-balance.webp" loading="lazy" decoding="async">
</article>
</div>
</section>
<section aria-label="Analytics foundation problems and solutions" class="symptom-section reveal-card">
<div class="symptom-heading">
<p>Trust Breaks &gt; Fix The System</p>
<h2>The Breakpoints We Diagnose</h2>
</div>
<div aria-label="Problem card navigation" class="section-controls symptom-controls">
<button aria-label="Show previous problem set" data-carousel-prev="symptom" type="button">Prev</button>
<span data-carousel-status="symptom">1 / 2</span>
<button aria-label="Show next problem set" data-carousel-next="symptom" type="button">Next</button>
</div>
<article class="symptom-card" data-carousel-item="symptom" data-page="0">
<img alt="Business logic duplicated across analytics systems" class="symptom-image" src="assets/home-generated/symptom-business-logic-everywhere.webp" loading="lazy" decoding="async">
<div class="symptom-copy">
<h3>Business logic lives everywhere</h3>
<p>Core calculations are copied across dashboards, spreadsheets, and ad-hoc queries.</p>
<a href="insights/single-source-of-truth-myth.html">Read: Why a single source of truth fails <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="0">
<img alt="Shared metric meaning organized across teams" class="symptom-image" src="assets/home-generated/symptom-metrics-shared-meaning.webp" loading="lazy" decoding="async">
<div class="symptom-copy">
<h3>Metrics lack shared meaning</h3>
<p>The same KPI means different things depending on who built the report.</p>
<a href="insights/kpi-ownership-framework-every-leadership-team-needs.html">Read: The KPI ownership framework <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="0">
<img alt="Reports disconnected from leadership questions" class="symptom-image" src="assets/home-generated/symptom-reports-wrong-questions.webp" loading="lazy" decoding="async">
<div class="symptom-copy">
<h3>Reports answer wrong questions</h3>
<p>Reports look polished, but miss the decisions leaders actually need to make.</p>
<a href="decision-system-reset.html">See: The Decision System Reset approach <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="1">
<img alt="Analytics confidence gauge surrounded by dashboards" class="symptom-image" src="assets/home-generated/symptom-confidence-erodes.webp" loading="lazy" decoding="async">
<div class="symptom-copy">
<h3>Confidence erodes silently</h3>
<p>Meetings turn into number debates instead of action.</p>
<a href="insights/why-nobody-trusts-your-dashboard.html">Read: Why nobody trusts the dashboard <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="1">
<img alt="Analytics systems under pressure as the business scales" class="symptom-image" src="assets/home-generated/symptom-systems-scale.webp" loading="lazy" decoding="async">
<div class="symptom-copy">
<h3>Systems don't scale with the business</h3>
<p>As teams grow, every change gets slower because the foundation is unclear.</p>
<a href="data-integration-analytics-architecture.html">Explore: Architecture built for scale <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="1">
<img alt="Decisions slowing as data and reports multiply" class="symptom-image" src="assets/home-generated/symptom-decisions-slow.webp" loading="lazy" decoding="async">
<div class="symptom-copy">
<h3>Decisions slow down as data grows</h3>
<p>As reports multiply, simple questions take longer and teams default back to instinct.</p>
<a href="insights/the-difference-between-reporting-and-decision-making.html">Read: Reporting vs. decision-making <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
</section>
<section class="work-section">
<div class="work-shell reveal-card">
<div class="work-heading">
<p class="page-kicker">Built around your business</p>
<h2>Different teams arrive with different pieces missing.</h2>
<p>Some need KPI strategy. Others need reliable pipelines, fewer dashboards, stronger governance, or automation. Parallax connects the pieces and builds the smallest strategy that makes sense for the business.</p>
</div>
<div class="work-grid work-puzzle-grid">
<article>
<img alt="Analytics foundation health scan with connected dashboards and data pipelines" class="work-card-image" src="assets/home-generated/work-health-check.webp" loading="lazy" decoding="async">
<span class="work-step">01</span>
<h3>Start with the real constraint</h3>
<p>Bring the dashboard, KPI debate, manual process, architecture bottleneck, or decision that keeps slowing the team down.</p>
</article>
<article>
<img alt="Scattered metrics converging into one aligned decision layer" class="work-card-image" src="assets/home-generated/work-clear-results.webp" loading="lazy" decoding="async">
<span class="work-step">02</span>
<h3>Diagnose how the pieces connect</h3>
<p>We trace the issue across data, definitions, tools, owners, workflows, and the decisions reporting is meant to support.</p>
</article>
<article>
<img alt="Trusted metric nodes aligning across connected teams" class="work-card-image" src="assets/home-generated/work-empower-team.webp" loading="lazy" decoding="async">
<span class="work-step">03</span>
<h3>Build the right-fit strategy</h3>
<p>The answer may be a focused reliability fix, KPI reset, dashboard rebuild, governance model, automation path, or architecture roadmap.</p>
</article>
<article>
<img alt="Continuous optimization loop around monitored analytics systems" class="work-card-image" src="assets/home-generated/work-ongoing-optimization.webp" loading="lazy" decoding="async">
<span class="work-step">04</span>
<h3>Embed, transfer, and evolve</h3>
<p>We document the logic, clarify ownership, enable the team, and adjust the system as priorities and operating needs change.</p>
</article>
</div>
<a class="work-fit-link" href="free-fit-check.html">Start with a free 15-minute Fit Check <span aria-hidden="true">-&gt;</span></a>
</div>
</section>
<section aria-labelledby="proof-title" class="proof-section reveal-card">
<div class="proof-intro">
<p class="page-kicker">What you leave with</p>
<h2 id="proof-title">A clear answer to three practical questions.</h2>
<p>No abstract maturity model and no automatic recommendation to rebuild everything. The Fit Check gives you a plain-language starting point.</p>
</div>
<div class="proof-grid">
<article>
<span>01</span>
<strong>What is actually going wrong?</strong>
<p>A concise summary of the reporting, data, ownership, or workflow issue creating the visible symptom.</p>
</article>
<article>
<span>02</span>
<strong>What should happen first?</strong>
<p>The highest-value starting move—whether that is clarifying a KPI, tracing a source, retiring reports, or fixing a workflow.</p>
</article>
<article>
<span>03</span>
<strong>What level of help makes sense?</strong>
<p>A practical recommendation for a focused fix, diagnostic, rebuild, ongoing support, or no engagement at all.</p>
</article>
</div>
</section>
<section aria-labelledby="case-study-title" class="case-study-section reveal-card">
<div class="case-study-heading">
<p class="page-kicker">Anonymized client work</p>
<h2 id="case-study-title">Different business needs. Specific operating results.</h2>
<p>Company identities are protected, but scale, constraints, timelines, and outcomes are included so the work is easier to evaluate.</p>
</div>
<div class="case-study-grid">
<article>
<div class="case-study-artifact" aria-label="Dashboard consolidation visual"><span>14 reports</span><span>4 executive views</span><span>1 governed revenue definition</span></div>
<p class="page-kicker">$50M–$100M industrial software company</p>
<h3>Consolidated overlapping revenue reporting into an executive view.</h3>
<dl>
<div><dt>Problem</dt><dd>Leadership reviewed 14 overlapping dashboards with conflicting revenue logic.</dd></div>
<div><dt>Changed</dt><dd>Mapped dashboard owners, removed duplicate views, and established one governed revenue definition.</dd></div>
<div><dt>Timeline</dt><dd>3 weeks from reporting inventory to executive-ready view.</dd></div>
<div><dt>Result</dt><dd>Reduced recurring manual reporting by approximately 12 hours per month.</dd></div>
</dl>
<blockquote>"The dashboard conversation finally moved from reconciliation to action."</blockquote>
</article>
<article>
<div class="case-study-artifact case-study-artifact-alt" aria-label="Metric ownership visual"><span>5 disputed KPIs</span><span>5 named owners</span><span>1 weekly action cadence</span></div>
<p class="page-kicker">500+ employee, multi-region field services company</p>
<h3>Turned KPI debates into an owned weekly decision cadence.</h3>
<dl>
<div><dt>Problem</dt><dd>Regional leaders used different definitions for completion rate, backlog, and margin.</dd></div>
<div><dt>Changed</dt><dd>Defined each KPI, named business owners, and tied thresholds to staffing and routing decisions.</dd></div>
<div><dt>Timeline</dt><dd>2 weeks for metric ownership and decision map.</dd></div>
<div><dt>Result</dt><dd>Cut weekly review prep from multiple spreadsheet checks to one governed operating view.</dd></div>
</dl>
<blockquote>"The value was making ownership visible, not just making another report."</blockquote>
</article>
<article>
<div class="case-study-artifact case-study-artifact-third" aria-label="Automation result visual"><span>Manual exports</span><span>Automated refresh</span><span>Trusted scorecard</span></div>
<p class="page-kicker">$25M–$50M B2B services company</p>
<h3>Replaced recurring reporting assembly with a trusted scorecard workflow.</h3>
<dl>
<div><dt>Problem</dt><dd>Managers copied CRM, finance, and delivery data into recurring status reports.</dd></div>
<div><dt>Changed</dt><dd>Automated the refresh path, documented definitions, and rebuilt the scorecard around decisions.</dd></div>
<div><dt>Timeline</dt><dd>4 weeks from source review to working scorecard.</dd></div>
<div><dt>Result</dt><dd>Freed roughly 8 to 10 hours per month and reduced "which number is right?" follow-ups.</dd></div>
</dl>
<blockquote>"The scorecard became something managers trusted enough to use every week."</blockquote>
</article>
<article>
<div class="case-study-artifact case-study-artifact-fourth" aria-label="Analytics architecture result visual"><span>6 source systems</span><span>1 governed data path</span><span>Daily reliability checks</span></div>
<p class="page-kicker">$100M+ multi-entity manufacturer</p>
<h3>Created a scalable reporting architecture across disconnected operating systems.</h3>
<dl>
<div><dt>Problem</dt><dd>Six source systems fed finance and operations reporting through undocumented extracts and copied transformations.</dd></div>
<div><dt>Changed</dt><dd>Mapped systems of record, defined reusable business entities, and established one governed path into the reporting layer.</dd></div>
<div><dt>Timeline</dt><dd>6 weeks from source inventory to target architecture and first production reporting domain.</dd></div>
<div><dt>Result</dt><dd>Reduced recurring reconciliation, made failures visible, and created a stable foundation for automation and advanced analytics.</dd></div>
</dl>
<blockquote>"We finally knew where the number came from and who owned every handoff."</blockquote>
</article>
</div>
</section>
<section class="founder-credibility-section reveal-card" aria-labelledby="founder-credibility-title">
<img src="assets/jonah-founder-credibility.webp" alt="Jonah Rosenthal, founder of Parallax Data Lab" loading="lazy" decoding="async">
<div>
<p class="page-kicker">Experienced analytics leadership</p>
<h2 id="founder-credibility-title">Built by a data leader who has operated inside the problems Parallax solves.</h2>
<p>Led enterprise analytics initiatives across Fortune 500 manufacturing and SaaS organizations. Founded by a data leader with expertise in BI strategy, Power BI, data engineering, automation, governance, predictive analytics, and AI-enabled analytics.</p>
<a href="about.html">Meet the founder and learn how Parallax works <span aria-hidden="true">-&gt;</span></a>
</div>
</section>
<section class="failure-section reveal-card">
<div class="failure-heading">
<p class="page-kicker">Patterns we see</p>
<h2>Patterns We Look For</h2>
<p class="section-lede">Most trust problems come from slow drift, not one obvious failure.</p>
</div>
<div aria-label="Failure pattern navigation" class="section-controls failure-controls">
<button aria-label="Show previous failure patterns" data-carousel-prev="failure" type="button">Prev</button>
<span data-carousel-status="failure">1 / 2</span>
<button aria-label="Show next failure patterns" data-carousel-next="failure" type="button">Next</button>
</div>
<div class="stat-grid failure-grid">
<article data-carousel-item="failure" data-page="0">
<img alt="Disconnected systems creating uncertainty about the source of truth" class="failure-image" src="assets/home-generated/failure-source-of-truth.webp" loading="lazy" decoding="async">
<strong>Unclear source of truth</strong>
<p>Teams are not sure which source, dashboard, or definition should win.</p>
</article>
<article data-carousel-item="failure" data-page="0">
<img alt="Conflicting dashboards showing different versions of the same metric" class="failure-image" src="assets/home-generated/failure-conflicting-numbers.webp" loading="lazy" decoding="async">
<strong>Conflicting numbers</strong>
<p>The same metric shows up differently across reports, teams, and meetings.</p>
</article>
<article data-carousel-item="failure" data-page="0">
<img alt="Analytics system bending under growing reporting complexity" class="failure-image" src="assets/home-generated/failure-scale-breaks.webp" loading="lazy" decoding="async">
<strong>Fragile scale</strong>
<p>Every new team, region, or workflow adds reporting debt and slows change.</p>
</article>
<article data-carousel-item="failure" data-page="1">
<img alt="Repeated logic copied across dashboards and spreadsheets" class="failure-image" src="assets/home-generated/failure-duplicate-logic.webp" loading="lazy" decoding="async">
<strong>Duplicated logic</strong>
<p>Calculations get copied into dashboards, spreadsheets, and one-off queries.</p>
</article>
<article data-carousel-item="failure" data-page="1">
<img alt="Metric definitions drifting across connected reports" class="failure-image" src="assets/home-generated/failure-definition-drift.webp" loading="lazy" decoding="async">
<strong>Definition drift</strong>
<p>Metric meaning changes by team, timeframe, tool, or report builder.</p>
</article>
<article data-carousel-item="failure" data-page="1">
<img alt="Decision meeting turning into a debate over analytics numbers" class="failure-image" src="assets/home-generated/failure-number-debates.webp" loading="lazy" decoding="async">
<strong>Decision debate</strong>
<p>Meetings shift from choosing action to defending which numbers are right.</p>
</article>
</div>
<p class="section-note">These issues rarely surface all at once. Most teams experience them gradually, as definitions drift, ownership blurs, and confidence in analytics quietly erodes.</p>
</section>
<section class="trust-section reveal-card">
<h2>Outcomes After Trust Is Restored</h2>
<div aria-label="Quote navigation" class="section-controls quote-controls">
<button aria-label="Show previous quotes" data-carousel-prev="quote" type="button">Prev</button>
<span data-carousel-status="quote">1 / 2</span>
<button aria-label="Show next quotes" data-carousel-next="quote" type="button">Next</button>
</div>
<div class="quote-grid">
<article data-carousel-item="quote" data-page="0">
<img alt="Verified decision signal in a trusted analytics network" class="quote-image" src="assets/home-generated/quote-trust-restored.webp" loading="lazy" decoding="async">
<blockquote>Teams stop arguing about which numbers are right. The biggest change is not always a new dashboard. It is shared confidence in the operating metrics.</blockquote>
<div class="quote-person">
<strong>Director of Analytics</strong>
<span>Mid-market SaaS company</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="0">
<img alt="Governed metric definitions resolving into one analytics path" class="quote-image" src="assets/home-generated/quote-ownership-definitions.webp" loading="lazy" decoding="async">
<blockquote>The visible dashboard problem often resolves once metric ownership, definitions, and decision use cases become explicit.</blockquote>
<div class="quote-person">
<strong>VP of Operations</strong>
<span>Industrial &amp; Manufacturing</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="0">
<img alt="Dashboards connecting to a clear leadership decision target" class="quote-image" src="assets/home-generated/quote-leadership-decisions.webp" loading="lazy" decoding="async">
<blockquote>Analytics becomes more useful when reports are rebuilt around the way leadership actually makes tradeoffs and decisions.</blockquote>
<div class="quote-person">
<strong>Product Leader</strong>
<span>Enterprise SaaS</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="1">
<img alt="Verified decision signal in a trusted analytics network" class="quote-image" src="assets/home-generated/quote-trust-restored.webp" loading="lazy" decoding="async">
<blockquote>Follow-up questions move faster because the model, logic, and definitions are stable enough to support deeper analysis.</blockquote>
<div class="quote-person">
<strong>Revenue Operations Lead</strong>
<span>Growth-stage SaaS</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="1">
<img alt="Governed metric definitions resolving into one analytics path" class="quote-image" src="assets/home-generated/quote-ownership-definitions.webp" loading="lazy" decoding="async">
<blockquote>Teams separate operating signals from legacy noise and assign clear ownership to the metrics that should guide action.</blockquote>
<div class="quote-person">
<strong>Chief Operating Officer</strong>
<span>Multi-site Services</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="1">
<img alt="Dashboards connecting to a clear leadership decision target" class="quote-image" src="assets/home-generated/quote-leadership-decisions.webp" loading="lazy" decoding="async">
<blockquote>Analytics shifts from a dashboard queue into operating infrastructure with standards, ownership, and repeatable logic.</blockquote>
<div class="quote-person">
<strong>Head of Product</strong>
<span>B2B Platform Company</span>
<em>Outcome pattern</em>
</div>
</article>
</div>
</section>
<section class="closing-section">
<h2>Build analytics leaders can trust.</h2>
<p>Get a clear read on what is breaking and the best next step.</p>
<div class="health-check-next-steps" aria-label="What happens after you request a Fit Check">
<h3>What happens after you request a Fit Check</h3>
<ol>
<li>You share the context.</li>
<li>We identify the trust breaks.</li>
<li>You get a recommended next step.</li>
<li>You decide whether to move forward.</li>
</ol>
</div>
<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>
</section>
</main>'''


OFFERINGS_HERO_AND_LADDER = r'''<section class="offerings-hero offerings-hero-refined" id="engagements">
<div class="offerings-hero-inner motion-layer" data-depth="0.08">
<p class="page-kicker">Our Offerings</p>
<h1>Choose the right path when there is too much reporting and not enough trusted signal for decisions.</h1>
<p>Use the ladder below to avoid guessing: the scorecard is optional for self-diagnosis, the Fit Check is the core free starting point, and the paid diagnostic or advanced work only follows when the evidence supports it.</p>
<div class="entry-path-mini entry-path-core" aria-label="Parallax entry path">
<span class="is-current" aria-current="page">Start</span>
<a class="is-optional" href="dashboard-trust-scorecard.html">Optional Diagnostic Scorecard</a>
<a href="free-fit-check.html">Free Fit Check</a>
<a href="analytics-health-check.html">Entry Diagnostic</a>
<a href="intelligence-lab.html">Intelligence Lab</a>
</div><div class="offerings-actions">
<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>
<a class="secondary-offer-button" href="dashboard-trust-scorecard.html">Get the Scorecard</a>
<a class="secondary-offer-button" href="#offering-details-title">Compare Engagement Paths</a>
</div>
</div>
</section>
<section class="offerings-section offer-chooser-section reveal-card" id="offer-chooser">
<p class="page-kicker">Product ladder</p>
<h2>Move from self-diagnosis to the right level of help.</h2>
<p class="offerings-lede">Start where the problem is today. Use the free tools when you need clarity, choose a focused diagnostic when the cause is uncertain, and move into a rebuild or ongoing leadership only when the situation calls for it.</p>
<div class="offer-chooser-grid offer-chooser-grid-balanced">
<a class="offer-chooser-core offer-path-scorecard" href="dashboard-trust-scorecard.html">
<span>Optional</span>
<strong>Self-diagnose: Dashboard Trust Scorecard</strong>
<p>Use the free self-assessment if you want a structured way to name the likely trust issue before requesting the Fit Check.</p>
</a>
<a class="offer-chooser-core offer-path-fit" href="free-fit-check.html">
<span>01</span>
<strong>Route: Free Fit Check</strong>
<p>Use the free routing conversation to identify the smallest useful next step.</p>
</a>
<a class="offer-chooser-core offer-path-health" href="analytics-health-check.html">
<span>02</span>
<strong>Diagnose: Entry Diagnostic</strong>
<p>Use the paid diagnostic when dashboards, metric definitions, data models, reporting processes, pain points, and decision friction need a foundation issue map and recommended next step.</p>
</a>
<a class="offer-chooser-core offer-path-reset" href="decision-system-reset.html">
<span>03</span>
<strong>Rebuild: Decision System Reset</strong>
<p>Use the rebuild to organize decisions, metrics, owners, triggers, cadence, and escalation into a working decision system.</p>
</a>
<a class="offer-chooser-core offer-path-fractional" href="fractional-analytics.html">
<span>04</span>
<strong>Steward: Fractional Analytics</strong>
<p>Use ongoing senior ownership and governance to maintain and evolve the decision system as priorities shift.</p>
</a>
<a class="offer-chooser-core offer-path-lab" href="intelligence-lab.html">
<span>05</span>
<strong>Advance: Intelligence Lab</strong>
<p>Use advanced operational intelligence products, especially the Weekly Operational Intelligence Digest, after the foundation is trusted.</p>
</a>
</div>
</section>'''


def replace_main(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'<main class="home-page">.*?</main>', HOME_MAIN, text, count=1, flags=re.S)
    path.write_text(text, encoding="utf-8", newline="\n")


def restore_ladder(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r'<section class="offerings-hero offerings-hero-refined".*?<section aria-labelledby="scorecard-lead-title"',
        OFFERINGS_HERO_AND_LADDER + '\n<section aria-labelledby="scorecard-lead-title"',
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(r'<section class="faq-section reveal-card">.*?</section>\s*', '', text, count=1, flags=re.S)
    path.write_text(text, encoding="utf-8", newline="\n")


replace_main(ROOT / "index.html")
restore_ladder(ROOT / "our-offerings.html")

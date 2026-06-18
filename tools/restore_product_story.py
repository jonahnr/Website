from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


HOME_MAIN = r'''<main class="home-page">
<section class="hero-section" id="top">
<a aria-label="Parallax Data Lab home" class="hero-brand motion-layer" data-depth="0.08" href="index.html">
<img alt="Parallax Data Lab logo" class="hero-logo" src="assets/parallax_data_lab_original_transparent.png"/>
</a>
<div aria-hidden="true" class="hero-rule"></div>
<div class="hero-copy motion-layer" data-depth="-0.05">
<h1>Business Intelligence Consulting for Teams That Need Clearer Data</h1>
<p>Parallax Data Lab helps growing teams turn scattered business data, dashboard sprawl, manual reporting, and metric debates into trusted dashboards, executive visibility, and decision-ready analytics workflows.</p>
<div class="entry-path-mini entry-path-core" aria-label="Parallax entry path">
<span class="is-current" aria-current="page">Start</span>
<a class="is-optional" href="dashboard-trust-scorecard.html">Optional Diagnostic Scorecard</a>
<a href="free-fit-check.html">Free Fit Check</a>
<a href="analytics-health-check.html">Entry Diagnostic</a>
<a href="intelligence-lab.html">Intelligence Lab</a>
</div>
<div class="hero-proof-tags" aria-label="Business intelligence consulting proof points">
<span>Power BI dashboards</span>
<span>KPI reporting</span>
<span>analytics cleanup</span>
<span>reporting automation</span>
<span>data quality review</span>
</div>
<div class="hero-actions">
<a class="primary-action" href="free-fit-check.html">Book a Fit Check</a>
<a class="secondary-action" href="our-offerings.html">Explore Services</a>
</div>
<strong class="micro-promise">A concrete path forward.</strong>
</div>
</section>
<section class="diagnostic-section reveal-card">
<h2>Dashboard Trust Breaks Beneath The Surface</h2>
<div class="diagnostic-panel">
<article>
<div>
<h3>Reports multiply faster than ownership.</h3>
<p>Each report solves a local need, but definitions, logic, and ownership drift unless the foundation is governed.</p>
</div>
<img alt="Abstract analytics network expanding without a clear owner" class="diagnostic-image" src="assets/home-generated/diagnostic-owner-drift.webp"/>
</article>
<article>
<div>
<h3>The fix is structural, not cosmetic.</h3>
<p>Shared definitions, reusable logic, and clear owners turn dashboards back into decision tools.</p>
</div>
<img alt="Balanced analytics structure connecting dashboards and decisions" class="diagnostic-image" src="assets/home-generated/diagnostic-structural-balance.webp"/>
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
<img alt="Business logic duplicated across analytics systems" class="symptom-image" src="assets/home-generated/symptom-business-logic-everywhere.webp"/>
<div class="symptom-copy">
<h3>Business logic lives everywhere</h3>
<p>Core calculations are copied across dashboards, spreadsheets, and ad-hoc queries.</p>
<a href="https://jonahnr.github.io/enterprise-outcome-studio/" target="_blank" rel="noopener noreferrer">View example <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="0">
<img alt="Shared metric meaning organized across teams" class="symptom-image" src="assets/home-generated/symptom-metrics-shared-meaning.webp"/>
<div class="symptom-copy">
<h3>Metrics lack shared meaning</h3>
<p>The same KPI means different things depending on who built the report.</p>
<a href="https://jonahnr.github.io/enterprise-outcome-studio/" target="_blank" rel="noopener noreferrer">View example <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="0">
<img alt="Reports disconnected from leadership questions" class="symptom-image" src="assets/home-generated/symptom-reports-wrong-questions.webp"/>
<div class="symptom-copy">
<h3>Reports answer wrong questions</h3>
<p>Reports look polished, but miss the decisions leaders actually need to make.</p>
<a href="decision-system-reset.html" target="_blank" rel="noopener noreferrer">View example <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="1">
<img alt="Analytics confidence gauge surrounded by dashboards" class="symptom-image" src="assets/home-generated/symptom-confidence-erodes.webp"/>
<div class="symptom-copy">
<h3>Confidence erodes silently</h3>
<p>Meetings turn into number debates instead of action.</p>
<a href="https://jonahnr.github.io/enterprise-outcome-studio/" target="_blank" rel="noopener noreferrer">View example <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="1">
<img alt="Analytics systems under pressure as the business scales" class="symptom-image" src="assets/home-generated/symptom-systems-scale.webp"/>
<div class="symptom-copy">
<h3>Systems don't scale with the business</h3>
<p>As teams grow, every change gets slower because the foundation is unclear.</p>
<a href="https://jonahnr.github.io/enterprise-outcome-studio/" target="_blank" rel="noopener noreferrer">View example <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
<article class="symptom-card" data-carousel-item="symptom" data-page="1">
<img alt="Decisions slowing as data and reports multiply" class="symptom-image" src="assets/home-generated/symptom-decisions-slow.webp"/>
<div class="symptom-copy">
<h3>Decisions slow down as data grows</h3>
<p>As reports multiply, simple questions take longer and teams default back to instinct.</p>
<a href="https://jonahnr.github.io/Predictive-Risk-Intelligence/" target="_blank" rel="noopener noreferrer">View example <span aria-hidden="true">-&gt;</span></a>
</div>
</article>
</section>
<section class="work-section">
<div class="work-shell reveal-card">
<h2>How Teams Work With Parallax</h2>
<div class="work-grid">
<article>
<img alt="Analytics foundation health scan with connected dashboards and data pipelines" class="work-card-image" src="assets/home-generated/work-health-check.webp"/>
<h3>Free Fit Check</h3>
<p>Start with a quick dashboard and reporting Fit Check. After you submit it, you can schedule a 1:1 review to walk through reporting gaps, dashboard opportunities, and highest-value next steps.</p>
</article>
<article>
<img alt="Scattered metrics converging into one aligned decision layer" class="work-card-image" src="assets/home-generated/work-clear-results.webp"/>
<h3>Clear &amp; Custom Results</h3>
<p>We align the core metrics, logic, and ownership behind the reports leaders already use.</p>
</article>
<article>
<img alt="Trusted metric nodes aligning across connected teams" class="work-card-image" src="assets/home-generated/work-empower-team.webp"/>
<h3>Empower Your Team</h3>
<p>Teams understand which numbers to trust, where they come from, and how to use them.</p>
</article>
<article>
<img alt="Continuous optimization loop around monitored analytics systems" class="work-card-image" src="assets/home-generated/work-ongoing-optimization.webp"/>
<h3>Ongoing Support &amp; Optimization</h3>
<p>Ongoing oversight keeps reporting accurate as priorities, teams, and workflows change.</p>
</article>
</div>
</div>
</section>
<section aria-labelledby="proof-title" class="proof-section reveal-card">
<div class="proof-intro">
<p class="page-kicker">What you get</p>
<h2 id="proof-title">A practical read on what to fix first.</h2>
<p>Before a rebuild, retainer, or dashboard development project, the free fit check routes scattered symptoms toward the smallest useful next step.</p>
</div>
<div class="proof-grid">
<article>
<strong>Foundation issue map</strong>
<p>Where definitions, models, ownership, or workflows are causing confusion.</p>
</article>
<article>
<strong>Decision-flow diagnosis</strong>
<p>Which business questions reports should answer and where current assets miss.</p>
</article>
<article>
<strong>Prioritized next steps</strong>
<p>A concise recommendation for whether to diagnose, rebuild, steward, advance, or stop.</p>
</article>
</div>
</section>
<section aria-labelledby="concrete-proof-title" class="concrete-proof-section reveal-card">
<div class="concrete-proof-heading">
<p class="page-kicker">Concrete proof examples</p>
<h2 id="concrete-proof-title">What better analytics structure changes in practice.</h2>
<p>These are the operating improvements Parallax looks for when analytics trust is breaking down.</p>
</div>
<div aria-label="Proof example navigation" class="section-controls proof-controls">
<button aria-label="Show previous proof example" data-carousel-prev="proof" type="button">Prev</button>
<span data-carousel-status="proof">1 / 5</span>
<button aria-label="Show next proof example" data-carousel-next="proof" type="button">Next</button>
</div>
<div class="proof-slider">
<article class="proof-slide" data-carousel-item="proof" data-page="0">
<span>Revenue reporting</span>
<h3>3 revenue definitions across 5 recurring dashboards became 1 governed executive metric.</h3>
<div class="proof-slide-grid">
<p><strong>Before:</strong> 5 recurring dashboards showed 3 different revenue numbers across finance, sales, and leadership reviews.</p>
<p><strong>After:</strong> 1 certified revenue metric powered 2 executive views, with visible logic and one owner for future changes.</p>
</div>
</article>
<article class="proof-slide" data-carousel-item="proof" data-page="1">
<span>Dashboard consolidation</span>
<h3>14 dashboards became 4 decision-ready views.</h3>
<div class="proof-slide-grid">
<p><strong>Before:</strong> 14 dashboards covered the same weekly operating questions with overlapping filters, owners, and definitions.</p>
<p><strong>After:</strong> 4 decision-ready views replaced the sprawl, each tied to a clear audience, cadence, and action path.</p>
</div>
</article>
<article class="proof-slide" data-carousel-item="proof" data-page="2">
<span>Operating cadence</span>
<h3>6 review tabs became 1 action board for weekly ownership.</h3>
<div class="proof-slide-grid">
<p><strong>Before:</strong> 6 spreadsheet tabs and dashboard exports slowed reviews while teams validated which numbers were right.</p>
<p><strong>After:</strong> 1 action board showed thresholds, owners, and escalation paths so the next action was clear.</p>
</div>
</article>
<article class="proof-slide" data-carousel-item="proof" data-page="3">
<span>Model reliability</span>
<h3>9 copied calculations moved into 1 reusable metric layer.</h3>
<div class="proof-slide-grid">
<p><strong>Before:</strong> 9 copied calculations across 7 reports carried their own filters, joins, and business rules.</p>
<p><strong>After:</strong> 1 reusable metric layer reduced drift and gave new reporting a governed starting point.</p>
</div>
</article>
<article class="proof-slide" data-carousel-item="proof" data-page="4">
<span>Executive review flow</span>
<h3>10 recurring report asks became 3 owned decision checkpoints.</h3>
<div class="proof-slide-grid">
<p><strong>Before:</strong> 10 standing report requests pulled leaders into status updates, side checks, and repeated number validation.</p>
<p><strong>After:</strong> 3 decision checkpoints tied each review to owners, thresholds, and the action required when metrics moved.</p>
</div>
</article>
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
<img alt="Disconnected systems creating uncertainty about the source of truth" class="failure-image" src="assets/home-generated/failure-source-of-truth.webp"/>
<strong>Unclear source of truth</strong>
<p>Teams are not sure which source, dashboard, or definition should win.</p>
</article>
<article data-carousel-item="failure" data-page="0">
<img alt="Conflicting dashboards showing different versions of the same metric" class="failure-image" src="assets/home-generated/failure-conflicting-numbers.webp"/>
<strong>Conflicting numbers</strong>
<p>The same metric shows up differently across reports, teams, and meetings.</p>
</article>
<article data-carousel-item="failure" data-page="0">
<img alt="Analytics system bending under growing reporting complexity" class="failure-image" src="assets/home-generated/failure-scale-breaks.webp"/>
<strong>Fragile scale</strong>
<p>Every new team, region, or workflow adds reporting debt and slows change.</p>
</article>
<article data-carousel-item="failure" data-page="1">
<img alt="Repeated logic copied across dashboards and spreadsheets" class="failure-image" src="assets/home-generated/failure-duplicate-logic.webp"/>
<strong>Duplicated logic</strong>
<p>Calculations get copied into dashboards, spreadsheets, and one-off queries.</p>
</article>
<article data-carousel-item="failure" data-page="1">
<img alt="Metric definitions drifting across connected reports" class="failure-image" src="assets/home-generated/failure-definition-drift.webp"/>
<strong>Definition drift</strong>
<p>Metric meaning changes by team, timeframe, tool, or report builder.</p>
</article>
<article data-carousel-item="failure" data-page="1">
<img alt="Decision meeting turning into a debate over analytics numbers" class="failure-image" src="assets/home-generated/failure-number-debates.webp"/>
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
<img alt="Verified decision signal in a trusted analytics network" class="quote-image" src="assets/home-generated/quote-trust-restored.webp"/>
<blockquote>Teams stop arguing about which numbers are right. The biggest change is not always a new dashboard. It is shared confidence in the operating metrics.</blockquote>
<div class="quote-person">
<strong>Director of Analytics</strong>
<span>Mid-market SaaS company</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="0">
<img alt="Governed metric definitions resolving into one analytics path" class="quote-image" src="assets/home-generated/quote-ownership-definitions.webp"/>
<blockquote>The visible dashboard problem often resolves once metric ownership, definitions, and decision use cases become explicit.</blockquote>
<div class="quote-person">
<strong>VP of Operations</strong>
<span>Industrial &amp; Manufacturing</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="0">
<img alt="Dashboards connecting to a clear leadership decision target" class="quote-image" src="assets/home-generated/quote-leadership-decisions.webp"/>
<blockquote>Analytics becomes more useful when reports are rebuilt around the way leadership actually makes tradeoffs and decisions.</blockquote>
<div class="quote-person">
<strong>Product Leader</strong>
<span>Enterprise SaaS</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="1">
<img alt="Verified decision signal in a trusted analytics network" class="quote-image" src="assets/home-generated/quote-trust-restored.webp"/>
<blockquote>Follow-up questions move faster because the model, logic, and definitions are stable enough to support deeper analysis.</blockquote>
<div class="quote-person">
<strong>Revenue Operations Lead</strong>
<span>Growth-stage SaaS</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="1">
<img alt="Governed metric definitions resolving into one analytics path" class="quote-image" src="assets/home-generated/quote-ownership-definitions.webp"/>
<blockquote>Teams separate operating signals from legacy noise and assign clear ownership to the metrics that should guide action.</blockquote>
<div class="quote-person">
<strong>Chief Operating Officer</strong>
<span>Multi-site Services</span>
<em>Outcome pattern</em>
</div>
</article>
<article data-carousel-item="quote" data-page="1">
<img alt="Dashboards connecting to a clear leadership decision target" class="quote-image" src="assets/home-generated/quote-leadership-decisions.webp"/>
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
<a class="secondary-offer-button" href="#pricing-guidance-title">Compare Engagement Paths</a>
</div>
</div>
</section>
<section class="offerings-section offer-chooser-section reveal-card" id="offer-chooser">
<p class="page-kicker">Product ladder</p>
<h2>Move from self-diagnosis to the right level of help.</h2>
<p class="offerings-lede">The ladder is intentionally staged so buyers do not confuse a free asset, a routing conversation, a paid diagnostic, a rebuild, ongoing stewardship, and advanced intelligence work.</p>
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

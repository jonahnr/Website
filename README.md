# Parallax Data Lab Website

Static website for Parallax Data Lab at parallaxdatalab.com, centered on the Free Fit Check entry path, Analytics Health Check diagnostic, deeper decision-system services, and Intelligence Lab paths.

The compact buyer entry path shown under the relevant heroes is:

- `dashboard-trust-scorecard.html` - optional free self-diagnosis and printable scorecard for buyers who want to think before requesting a conversation.
- `free-fit-check.html` - core free 15-minute routing conversation and the main starting point for intentional buyers.
- `analytics-health-check.html` - entry paid diagnostic when the foundation needs deeper review.
- `intelligence-lab.html` - advanced operational intelligence products after the foundation is trusted.

Decision System Reset and Fractional Analytics Consulting stay in the Offerings ladder and dropdown, but they are intentionally not in the compact entry path. They are deeper engagement shapes after the first routing and diagnostic work clarifies the problem.

## GitHub Pages Entry Point

GitHub Pages serves the root URL from:

- `index.html`

Do not link to `home.html`; this project currently uses `index.html` as the live page.

## Core Files

- `index.html` - Main homepage content and section structure.
- `how-we-help.html` - How We Help page.
- `insights.html` - Filterable SEO article hub with executive analytics articles.
- `insights/*.html` - Individual article pages for analytics trust, KPI governance, executive reporting, analytics leadership, AI enablement, and Intelligence Lab initiatives.
- `intelligence-lab.html` - Intelligence Lab page.
- `our-offerings.html` - Offerings overview and path chooser.
- `analytics-health-check.html` - Internal Analytics Health Check request page with a FormSubmit-powered context form.
- `dashboard-trust-scorecard.html` - Optional lead magnet page that lets visitors score the five trust dimensions first, shows a live weakest-area result, then submits through the `/api/scorecard-submit` backend to open the working scorecard.
- `dashboard-trust-scorecard-download.html` - Interactive printable scorecard page with five 1-5 scored dimensions, five evidence checks per dimension that can drive scoring, diagnostic snapshot, compact evidence notes, tailored guidance, and print/PDF buttons.
- `decision-system-reset.html` - Decision System Reset service page.
- `decision-workspace.html` - Prototype client login/sign-up workspace for org-scoped decision, metric, dashboard, recommendation, user, and export artifacts.
- `decision-workspace-backend-plan.md` - Production auth/database migration plan for the workspace.
- `decision-workspace-schema.sql` - Draft Postgres/Supabase schema for organizations, users, memberships, artifacts, and audit events.
- `decision-workspace-api-contract.md` - API route, payload, permission, and deletion behavior contract for wiring the workspace to a backend.
- `fractional-analytics.html` - Fractional Analytics Consulting page.
- `about.html` - About page and founder context.
- `privacy-policy.html` - Privacy policy for analytics, forms, scheduling, and contact data.
- `assets/insights/*.png` - Generated article hero photos in the Parallax visual style.
- `home.css` - Shared styling, responsive layout, navigation, card visuals, subpage layouts, and carousel states.
- `home.js` - Animated background, scroll reveals, pointer motion, dropdown handling, and carousel transitions.
- `tools/optimize-assets.py` - Repeatable PNG optimization pass for oversized generated imagery.
- `ASSET-CHECKLIST.md` - Full list of every asset path referenced by the HTML and CSS.
- `sitemap.xml` - Search engine sitemap for indexable pages.
- `robots.txt` - Search crawler instructions pointing to the sitemap.

Root favicon files:

- `favicon.svg`
- `favicon.ico`
- `apple-touch-icon.png`
- `social-preview.webp`

## Live Page Behavior

The site includes:

- Sticky top navigation linking to all local pages.
- Clickable Our Offerings dropdown linking to the offerings overview and three engagement pages.
- Analytics Health Check request form that posts to `jonahnr@gmail.com` through FormSubmit.
- Dashboard Trust Scorecard flow that gives a partially ungated live result first, then posts the request and live score details to the Cloudflare Pages Function at `/api/scorecard-submit`, emails the request, archives it when KV is configured, and routes the visitor to the downloadable scorecard.
- Homepage diagnostic carousel for analytics foundation problems.
- How We Help process, outcome, and diagnostic disclosure sections.
- Offerings page that routes visitors to the right engagement path.
- Decision System Reset and Fractional Analytics Consulting pages for deeper offer detail.
- Intelligence Lab examples framed as proof/example work rather than the primary conversion path.
- About page with consistent logo navigation and founder positioning.
- Decision Workspace prototype with demo Parallax admin access, org-scoped access, local user creation, metric ownership map, decision map, dashboard trust register, recommendation action plan, and printable Decision System Reset artifact.

## Decision Workspace Prototype

Open locally at:

```text
http://127.0.0.1:8014/decision-workspace.html
```

The workspace defaults to Sign up so a first-time organization can create an org admin account. Returning demo accounts:

- Parallax admin: `admin@parallaxdatalab.com` / `parallax-admin`
- Org admin: `alex@acmeops.com` / `decision123`
- Contributor: `morgan@acmeops.com` / `decision123`
- Viewer: `taylor@northstar.com` / `decision123`

The current workspace is a static prototype. It stores orgs, users, and artifacts in browser `localStorage` and stores the active session in `sessionStorage`. It is useful for product testing and sales demos, but it is not production authentication. Before using it with real client data, replace the local demo auth with a real backend/auth layer such as Supabase, Clerk, Auth0, Cloudflare Access, or a custom Cloudflare Pages/Workers backend.

Current workspace artifacts:

- Recommendation Action Plan
- Metric Ownership Map
- Decision Map
- Dashboard Trust Register
- Users and org access
- Printable Decision System Reset export

Recent workspace capabilities:

- Site-wide Log in and Sign up controls point into the Decision Workspace, with Sign up as the default for first-time users.
- Sign up requires password confirmation, then creates a new organization and first org admin in the local prototype.
- Workspace forms include hover/focus help prompts on each field so users know what to enter.
- Parallax admins can delete the active organization only after two confirmations in the prototype.
- Dashboard names can link to a report URL.
- Dashboards include reporting source/platform and workspace/location.
- Decisions include concrete decision options, criteria, and current/default option.
- Editable rows include delete actions for permitted users.
- Viewer users remain read-only.

Production prep files:

- `decision-workspace-backend-plan.md`
- `decision-workspace-api-contract.md`
- `decision-workspace-schema.sql`

## Important Links

Primary CTA:

- Free Fit Check CTA linking to `free-fit-check.html`

Lead magnet:

- Dashboard Trust Scorecard CTA linking to `dashboard-trust-scorecard.html`
- Live scorecard stores the computed weakest dimension, average score, and score summary locally and passes those values into the backend submission.
- Scorecard form submits to `/api/scorecard-submit` in the background and then opens `/dashboard-trust-scorecard-download/` directly.
- The printable scorecard page uses that selected dimension, and any lowest score selected on the working sheet, to tailor the guidance panel before printing or saving as PDF.

Secondary CTA:

- `https://calendly.com/jonahnr/parallax-data-lab-intro-call`

Assessment form delivery:

- Form action: `https://formsubmit.co/jonahnr@gmail.com`
- FormSubmit may require first-time email activation for the recipient address before live submissions are delivered.

Scorecard backend delivery:

- Function path: `functions/api/scorecard-submit.js`
- Hosted endpoint: `/api/scorecard-submit`
- Required environment variable: `RESEND_API_KEY`
- Optional environment variable: `SCORECARD_TO_EMAIL` defaults to `jonahnr@gmail.com`
- Optional environment variable: `SCORECARD_FROM_EMAIL` defaults to `Parallax Data Lab <scorecard@parallaxdatalab.com>` and must be a verified sender in Resend.
- Optional Cloudflare KV binding: `SCORECARD_SUBMISSIONS` stores each scorecard request as a JSON record for later reference.
- Local static preview will still redirect to the scorecard download page, but email delivery only runs where the Cloudflare Pages Function is deployed.

Ribbon navigation:

- Home: `index.html`
- How We Help: `how-we-help.html`
- Intelligence Lab: `intelligence-lab.html`
- Insights: `insights.html`
- Our Offerings: `our-offerings.html`
- Analytics Health Check: `analytics-health-check.html`
- Decision System Reset: `decision-system-reset.html`
- Fractional Analytics Consulting: `fractional-analytics.html`
- About: `about.html`

## Asset Requirement

Before publishing, make sure the full `assets/` folder is committed and pushed. The current HTML and CSS reference many files under:

- `assets/`
- `assets/home-generated/`

Use `ASSET-CHECKLIST.md` as the full publishing checklist for referenced images and SVGs. If any referenced file is missing, GitHub Pages will load the page but show broken images or empty visual sections.

To recompress oversized PNG assets after adding new generated art, run:

```powershell
python tools\optimize-assets.py
```

The optimizer keeps the same filenames and only overwrites PNGs when the optimized version is materially smaller.

## Local Preview

From this folder, run:

```powershell
python -m http.server 8014
```

Then open:

```text
http://127.0.0.1:8014/
```

or:

```text
http://127.0.0.1:8014/index.html
```

## GitHub Pages Checklist

Before publishing, make sure these files and folders are committed and pushed:

- `index.html`
- `how-we-help.html`
- `intelligence-lab.html`
- `decision-workspace.html`
- `our-offerings.html`
- `analytics-health-check.html`
- `decision-system-reset.html`
- `fractional-analytics.html`
- `about.html`
- `home.css`
- `home.js`
- `README.md`
- `ASSET-CHECKLIST.md`
- `assets/`

All HTML pages currently reference:

- `home.css?v=143`
- `home.js?v=143`

If styling or JavaScript looks old after deployment, bump the version number consistently across every HTML file.

If the page shows a 404, confirm GitHub Pages is pointed at the branch and folder containing `index.html`.

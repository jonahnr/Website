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
- `dashboard-trust-scorecard.html` - Optional lead magnet request page that previews the five diagnostic areas, captures one matching weakest dimension, and includes an optional context field for secondary symptoms.
- `dashboard-trust-scorecard-download.html` - Interactive printable scorecard page with five 1-5 scored dimensions, five evidence checks per dimension that can drive scoring, diagnostic snapshot, compact evidence notes, tailored guidance, and print/PDF buttons.
- `decision-system-reset.html` - Decision System Reset service page.
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
- `social-preview.png`

## Live Page Behavior

The site includes:

- Sticky top navigation linking to all local pages.
- Clickable Our Offerings dropdown linking to the offerings overview and three engagement pages.
- Analytics Health Check request form that posts to `jonahnr@gmail.com` through FormSubmit.
- Homepage diagnostic carousel for analytics foundation problems.
- How We Help process, outcome, and diagnostic disclosure sections.
- Offerings page that routes visitors to the right engagement path.
- Decision System Reset and Fractional Analytics Consulting pages for deeper offer detail.
- Intelligence Lab examples framed as proof/example work rather than the primary conversion path.
- About page with consistent logo navigation and founder positioning.

## Important Links

Primary CTA:

- Free Fit Check CTA linking to `free-fit-check.html`

Lead magnet:

- Dashboard Trust Scorecard CTA linking to `dashboard-trust-scorecard.html`
- Scorecard request form stores the selected weakest dimension locally.
- Scorecard request form submits to FormSubmit in the background and then opens `dashboard-trust-scorecard-download.html` directly.
- The printable scorecard page uses that selected dimension, and any lowest score selected on the working sheet, to tailor the guidance panel before printing or saving as PDF.

Secondary CTA:

- `https://calendly.com/jonahnr/parallax-data-lab-intro-call`

Assessment form delivery:

- Form action: `https://formsubmit.co/jonahnr@gmail.com`
- FormSubmit may require first-time email activation for the recipient address before live submissions are delivered.

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

- `home.css?v=118`
- `home.js?v=118`

If styling or JavaScript looks old after deployment, bump the version number consistently across every HTML file.

If the page shows a 404, confirm GitHub Pages is pointed at the branch and folder containing `index.html`.

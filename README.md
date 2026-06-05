# Parallax Data Lab Homepage

Static GitHub Pages site for the Parallax Data Lab analytics foundation assessment.

## GitHub Pages Entry Point

GitHub Pages serves the root URL from:

- `index.html`

Do not link to `home.html`; this project currently uses `index.html` as the live page.

## Files

- `index.html` - Main homepage content and section structure.
- `how-we-help.html` - Local How We Help page.
- `intelligence-lab.html` - Local Intelligence Lab page.
- `our-offerings.html` - Local Our Offerings page.
- `analytics-health-check.html` - Internal Analytics Foundation Assessment request page with a FormSubmit-powered context form.
- `decision-system-reset.html` - Internal Decision System Reset engagement page.
- `fractional-analytics.html` - Internal Fractional Analytics Consulting engagement page.
- `about.html` - Local About page.
- `home.css` - Shared styling, responsive layout, ribbon nav, card visuals, subpage layouts, and carousel states.
- `home.js` - Animated background, scroll reveals, pointer motion, and click-based card/quote transitions.
- `assets/parallax-customer-intelligence-hero.png` - Background image used in the hero and Parallax sections.

## Live Page Behavior

The page includes:

- Blue top navigation ribbon linking to the local site pages.
- Clickable Our Offerings dropdown linking to the local offerings overview and three engagement pages.
- Analytics Foundation Assessment request form that posts to `jonahnr@gmail.com` through FormSubmit.
- Hero section for the Analytics Foundation Assessment.
- Diagnostic section explaining dashboard chaos as a symptom of a broken analytics foundation.
- Problems > Solutions section with six cards, shown three at a time with Prev/Next controls.
- "How Teams Work With Parallax Data" section.
- Common analytics failure pattern stats.
- Six leadership quotes, shown three at a time with Prev/Next controls.
- Final request assessment CTA.

## Important Links

Primary CTA:

- `analytics-health-check.html`

Assessment form delivery:

- Form action: `https://formsubmit.co/jonahnr@gmail.com`
- FormSubmit may require first-time email activation for the recipient address before live submissions are delivered.

Ribbon navigation:

- Home: `index.html`
- How We Help: `how-we-help.html`
- Intelligence Lab: `intelligence-lab.html`
- Our Offerings: `our-offerings.html`
- Analytics Health Check: `analytics-health-check.html`
- Decision System Reset: `decision-system-reset.html`
- Fractional Analytics Consulting: `fractional-analytics.html`
- About: `about.html`

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

Before publishing, make sure these files are committed and pushed:

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
- `assets/parallax-customer-intelligence-hero.png`

If the page shows a 404, confirm GitHub Pages is pointed at the branch and folder containing `index.html`.

If styling looks old, the assessment page references `home.css?v=12`; bump the version number in each HTML file after major CSS changes to force a browser cache refresh.

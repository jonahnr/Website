# Parallax Data Lab Homepage

Static GitHub Pages homepage for the Parallax Data Lab analytics foundation assessment.

## GitHub Pages Entry Point

GitHub Pages serves the root URL from:

- `index.html`

Do not link to `home.html`; this project currently uses `index.html` as the live page.

## Files

- `index.html` - Main homepage content and section structure.
- `home.css` - Homepage styling, responsive layout, ribbon nav, card visuals, and carousel states.
- `home.js` - Animated background, scroll reveals, pointer motion, and click-based card/quote transitions.
- `assets/parallax-customer-intelligence-hero.png` - Background image used in the hero and Parallax sections.

## Live Page Behavior

The page includes:

- Blue top navigation ribbon linking to the main Parallax Webflow pages.
- Hero section for the Analytics Foundation Assessment.
- Diagnostic section explaining dashboard chaos as a symptom of a broken analytics foundation.
- Problems > Solutions section with six cards, shown three at a time with Prev/Next controls.
- "How Teams Work With Parallax Data" section.
- Common analytics failure pattern stats.
- Six leadership quotes, shown three at a time with Prev/Next controls.
- Final request assessment CTA.

## Important Links

Primary CTA:

- `https://parallax-data.webflow.io/work/analytics-foundation-assessment`

Ribbon navigation:

- Home: `https://parallax-data.webflow.io/`
- How We Help: `https://parallax-data.webflow.io/how-we-help`
- Intelligence Lab: `https://parallax-data.webflow.io/intelligence-lab`
- Our Offerings: `https://parallax-data.webflow.io/our-offerings`
- About: `https://parallax-data.webflow.io/about`

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
- `home.css`
- `home.js`
- `assets/parallax-customer-intelligence-hero.png`

If the page shows a 404, confirm GitHub Pages is pointed at the branch and folder containing `index.html`.

If styling looks old, the page references `home.css?v=4`; bump the version number in `index.html` after major CSS changes to force a browser cache refresh.

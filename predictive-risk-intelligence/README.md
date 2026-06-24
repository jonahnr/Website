# Parallax Predictive Risk Intelligence Engine Page

Standalone customer-facing web section for Parallax Data Lab. The page positions the offering as the predictive risk intelligence engine behind the Operational Risk Digest, with the linked digest serving as the executive-facing output.

## Purpose

This page explains how industrial operational signals become leadership attention items:

- Industrial signal collection
- Pattern detection engine
- Predictive risk modeling
- Intervention prioritization
- Executive intelligence delivery

The copy is tuned for manufacturing and automotive, construction and infrastructure, aerospace, shipbuilding, energy and utilities, field operations, and other high-stakes operational risk contexts.

## Files

- `index.html` - Page content, CTAs, section anchors, generated visual assets, custom hero system visual, scoring context, and opened detail sections.
- `styles.css` - Parallax visual system, grid background layer, responsive layout, cards, bullets, and section styling.
- `script.js` - Canvas signal background, pointer-based motion, and reveal behavior.
- `assets/` - Local visual assets used by the page, including the updated Parallax logo crop and five generated engine-step images.

## Key Links

Primary digest CTA:

- `../operational-risk-digest/`

## Local Preview

From this folder, run:

```powershell
python -m http.server 8011
```

Then open:

```text
http://127.0.0.1:8011/index.html
```

## Section Anchors

The five flow cards near the top link directly to:

- `#signal-collection`
- `#pattern-detection`
- `#predictive-modeling`
- `#intervention-prioritization`
- `#executive-delivery`

Each section includes an expandable `What this can look like` breakout to help customers picture the inputs, logic, and outputs in their own operating environment.

## Scoring Context

The page references the threshold logic behind the digest in customer-facing language:

- Risk movement is compared against a trailing six-week baseline.
- The model layer uses magnitude, velocity, persistence, spread, and severity.
- Missing signal families should be reweighted rather than treated as zero.
- Digest items include validation, quality, and confidence context before they are framed as leadership-ready.

## Design Notes

- Keep the page in the Parallax dark-blue, electric-blue, and gold visual language.
- Keep customer-facing copy focused on industrial signal clarity, operational risk movement, and executive attention.
- Avoid making this read like a separate dashboard product. It should support the digest as the underlying intelligence engine.
- Use the generated PNG visuals for the five engine stages, supported by clean bullets and structured lists for input/output examples.
- Keep the page free of the removed top ribbon and navigation links.
- Keep the hero visual aligned with the same five-stage image system used in the engine section.

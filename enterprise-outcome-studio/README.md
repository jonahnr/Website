# Parallax Data Lab Enterprise Outcome Studio

A customer-facing static web app for guiding a buyer through an enterprise analytics transformation conversation. The app helps Parallax Data Lab turn reporting modernization, semantic model trust, BI automation, performance tuning, and governance packaging into a clear outcome estimate, readiness diagnosis, recommended path, and exportable buyer brief.

## Demo Flow

The interface is organized around a five-step sales/demo journey:

1. Estimate value from operating facts or a scenario preset.
2. Diagnose readiness with evidence-led maturity scoring.
3. Explain the value drivers through semantic model, performance, automation, and governance signals.
4. Match gaps to delivery capability modules.
5. Export the buyer-ready outcome package.

## What It Shows

- Enterprise benchmark proof points:
  - 75% reduction in eligible manual reporting effort
  - 25x query optimization and dashboard performance lift
  - 10x analytics delivery scale through BI engineering automation
  - RLS as an added governance package
- Scenario presets for starter, small BI team, manual-heavy enterprise, slow Power BI estate, and governed executive organization demos
- Customer-input outcome calculator using report volume, report-cycle effort, query usage, wait time, hourly cost, and automation eligibility
- Confidence labels for directional, inventory-supported, evidence-supported, and validated business cases
- Guided definitions for customer inputs so buyers understand what they are choosing
- Executive first-screen header with live annual opportunity, hours recovered, and readiness-state chips
- Branded Parallax Data Lab logo artwork and star-field background treatment across the blue studio surfaces
- Quick estimate mode and detailed report-inventory mode for mixed weekly/monthly reporting portfolios
- Simplified first-page results with advanced calculation detail available on demand
- Cumulative calculation explainers showing how reporting capacity, performance/model value, monthly value, and annual opportunity add up
- Executive snapshot cards that translate the estimate into primary signal, proof needed, and next move
- Slower-growth value weighting for very large manual-reporting and slow-dashboard estates so high-end estimates stay directional instead of exploding linearly
- 0-100 readiness score based on weighted criteria with scoring guidance bands
- Readiness score blended from 80% self-assessment plus 20% operational pressure from manual reporting, query wait, model size, and logic issues
- Fine-tuning mode after readiness completion with a reference map for the selected scoring metric
- Mutable semantic model trust layer with Power BI model-size, bad-logic, certification, duplicate-measure, and access signals
- Example semantic model relationships that update from the current fact, dimension, and access inputs
- Plain-language automation recipes with customer pain, mechanism, best fit, and proof artifacts
- Scenario-derived automation recipe values that map each recipe to the relevant reporting, query, model, logic, or governance value pool
- In-app executive brief preview with business case, evidence plan, next meeting agenda, and recommended modules
- Exportable outcome brief from the guided final package
- Editable detailed report inventory with add/delete rows
- Clickable governance package columns for comparison
- Governance packaging for Base, Scale, Audit, and RLS Add-on
- Visual capability catalog with business problem, intervention, fictional proof-company artifacts, and quiz-gated recommendation callouts
- Recommended Path page that shows a useful preview immediately, then formats the completed path like a screenshot-ready executive export with package and readout guidance

## Run Locally

This is a static site. From the repo root:

```powershell
python -m http.server 4173
```

Then open:

```text
http://localhost:4173/index.html
```

You can also open `index.html` directly in a browser, but using a local server is closer to how it runs in GitHub Pages.

If the built-in Python server is unavailable in your environment, any static server can be used. The app has no build step and no external runtime dependency.

## Deploy With GitHub Actions

This repo includes a GitHub Actions workflow at:

```text
.github/workflows/deploy-pages.yml
```

The workflow publishes the static site to GitHub Pages whenever changes are pushed to `main`.

To enable it:

1. Push this repo to GitHub.
2. In GitHub, go to **Settings > Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Push to `main`.
5. Open the Pages URL shown after the workflow finishes.

## Repo Structure

```text
.
|-- .github/
|   `-- workflows/
|       `-- deploy-pages.yml
|-- assets/
|   |-- parallax-data-lab-logo.png
|   `-- parallax-starry-background.png
|-- .nojekyll
|-- README.md
`-- index.html
```

## Future Real-Data Integration

The current app is static and uses customer-entered inputs plus benchmark assumptions. A real-data version could replace those inputs with an API or data file that supplies:

- Report inventory and ownership
- Report cycle frequency and manual effort baseline
- Query runtime and dashboard usage logs
- Semantic model metadata
- Certified metrics and glossary records
- Governance, lineage, access, and RLS policy evidence

The recommended next step is to add a small data contract such as `data/outcomes.json`, then wire the calculator to load from that file before connecting to warehouse, BI, or governance APIs.

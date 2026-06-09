# Parallax Site Updates

## Completed updates

1. Fixed broken disclosure markup by closing every `<details>` element correctly in `how-we-help.html` and `intelligence-lab.html`.
2. Standardized cache-busting versions across all HTML pages to `home.css?v=43` and `home.js?v=43`.
3. Added `ASSET-CHECKLIST.md` with every referenced image/SVG path and updated `README.md` to make the full `assets/` folder a required publishing item.
4. Tightened proof language by replacing named testimonial-style quotes with representative outcome language.
5. Reduced repetition by sharpening page-specific language around example work, proof, routing, and health-check conversion.
6. Standardized primary CTAs to `Request an Analytics Health Check` and secondary scheduling CTAs to `Schedule Intro Call`.
7. Reframed external demo/project links as examples instead of primary conversion paths.

## Additional cleanup

- Replaced mojibake CSS symbols such as `âœ“` and `âŒ„` with proper rendered symbols.
- Updated the About page navigation brand to use the same logo treatment as the rest of the site.
- Verified local `.html` links and same-page anchors.
- Verified all HTML files have balanced structural tags with the current parser check.


## 2026-06-07 Second feedback pass

- Removed the Home hero plane and blue-line overlay.
- Shortened Home symptom card example links and added consistent link treatment.
- Cleaned the How We Help success grid so all cards share the same treatment and removed the special gold card emphasis.
- Added a How We Help bridge into Intelligence Lab modules for teams past the initial foundation work.
- Standardized the Intelligence Lab bottom CTA to the offerings-style blue and gold banner with Health Check and Calendly actions.
- Added an Intelligence Lab showcase card under the three Core Paths on Our Offerings.
- Added pricing and fit guidance to Our Offerings.
- Added an At a Glance section to Analytics Health Check and clarified that the form starts as a fit review.
- Improved Decision System Reset flip-card contrast and number alignment.
- Changed Fractional Analytics hero panel from Best When to At a Glance.
- Added spacing below Fractional service images and widened the Outcomes section into a full row.

## Cleanup Pass 3

- Moved Analytics Health Check At a Glance into the hero as a side panel matching the Decision System Reset layout.
- Restyled Fractional Analytics At a Glance to match the Decision System Reset formatting and color treatment.
- Normalized Decision System Reset objective flip-card heights so item 03 no longer appears taller than the other cards.
- Added an invisible hover bridge and removed the dropdown gap so the Our Offerings menu stays open while moving from the nav item into the menu.
- Bumped shared CSS/JS cache versions to v45.


## Cleanup pass 4 – About page modernization
- Rebuilt the About page hero around the `new2.png` background asset and removed the orbit/spinning circle graphic.
- Modernized the About page layout and visual language to match the rest of the site.
- Updated About visuals to use new themed asset references: `about-why-foundation-shift.png`, `Jonah.png`, and `about-founder-cube-glow.png`.
- Changed the primary About CTA to a direct Contact Us jump and kept a secondary path to services.
- Added a Quick Navigation dropdown inside the bottom Contact section for fast section jumps.
- Updated the contact form CTA to `Request A Fit Review` for lower-friction positioning.


## Cleanup pass 5 – About hero tightening
- Shortened the About hero so it no longer dominates the page.
- Changed the At a Glance panel from a large side panel into a compact horizontal strip under the hero copy.
- Removed the Quick Navigation dropdown from the What Happens Next card.
- Included generated About assets in the package: `about-why-foundation-shift.png`, `about-founder-cube-glow.png`, and `about-systems-operating-layer.png`.
- Bumped cache references to `v=47`.


## Cleanup pass 6 – About page feedback and 10 image wiring
- Tightened the About hero again and moved the At a Glance panel back to the right side on desktop.
- Fixed hero checklist spacing so the check items do not overlap.
- Replaced the three Our Point of View icons with generated themed image assets.
- Added a parallax treatment to the Why Parallax Exists section without removing the moving constellation background.
- Replaced the four Who We Work Best With icons with generated themed image assets.
- Rebalanced the founder cube so it sits centered under the founder portrait.
- Replaced the three How Principles Become Systems icons with generated themed image assets.
- Removed the bottom contact CTA that pulled users away from the form.
- Moved the Schedule Intro Call action into What Happens Next and styled it as centered white text.
- Removed the static dot overlay from the About hero while preserving the moving background canvas.


## Cleanup pass 7 – About page layout and parallax correction
- Rebuilt the About hero as a cleaner two-column layout so text and At a Glance no longer overlap.
- Restyled About At a Glance to match the Decision System Reset service-page pattern: gold kicker, blue labels, white values.
- Removed underline styling from Contact Us links and CTAs.
- Added scroll-based parallax behavior for the Why Parallax Exists section using data-parallax-speed attributes.
- Added spacing around the founder perspective paragraph.
- Aligned the Common Wins blocks in How Principles Become Systems.
- Rewrote the bottom contact copy to speak to the customer and keep them focused on submitting the form.
- Bumped cache versions to v49.


## Cleanup pass 8 – About hero and parallax removal
- Removed the added real parallax movement from the About page Why Parallax Exists section.
- Rebuilt the About hero grid so the copy cannot collapse into narrow single-word lines or overlap the At a Glance card.
- Kept At a Glance on the right on wide screens, with automatic stacking on smaller widths.
- Moved Prefer to talk first? above the Schedule Intro Call button in What Happens Next.
- Bumped cache versions to v50.


## Cleanup pass 9 – Global background and copy polish
- Enlarged the Home hero Analytics Health Check CTA and removed underline styling.
- Added a shared subtle grid background treatment across all pages while preserving the moving constellation canvas.
- Rephrased the How We Help diagnostic disclosure from “Open the diagnostic slider” to “Open the diagnostic detail.”
- Strengthened the Intelligence Lab bridge language around premium initiatives once the foundation is stable.
- Standardized the Intelligence Lab boundaries section font styling to match the rest of the site.
- Bumped shared CSS/JS cache versions to `v=51`.

## Cleanup pass 10 – Production preparation
- Consolidated the accumulated About page override layers into one production polish section in `home.css`.
- Added a shared footer to every page with Parallax Data Lab, jonahnr@gmail.com, core links, and 2026 copyright.
- Added favicon and social preview assets: `assets/favicon.svg`, `assets/favicon.ico`, `assets/apple-touch-icon.png`, and `assets/social-preview.png`.
- Added Open Graph and Twitter preview metadata to every page.
- Added a concrete proof carousel to the homepage and wired it into `setupCarousel("proof")`.
- Standardized primary health check CTA language around “Request an Analytics Health Check.”
- Removed the static dot overlay from the About hero while keeping the moving constellation background and shared grid treatment.
- Added generated placeholder files for any previously missing image paths so the packaged preview does not render broken image icons. Replace placeholders with final branded art where applicable.
- Added responsive QA fixes for horizontal overflow and About hero text width.
- Bumped shared CSS/JS cache versions to `v=52`.


## Cleanup pass 11 – Footer, proof, background, favicon polish
- Restyled the homepage concrete proof carousel to match the Home page visual system.
- Rebuilt the footer into organized columns with core pages, services, contact, email, and copyright.
- Added Decision System Reset, Fractional Analytics Consulting, and Contact Us to the footer.
- Lightened the global page background and increased grid/constellation visibility.
- Added root-level favicon and social preview files in addition to the asset-folder copies.
- Updated favicon links in every page head and bumped cache versions to `v=53`.


## Cleanup pass 12 – Background, footer, proof, and About contrast
- Smoothed the global blue background and removed the duplicate/faded grid layer.
- Disabled legacy About page static dot pseudo-elements while preserving the moving constellation canvas.
- Restyled the Home concrete proof carousel to match the blue card system used elsewhere on the homepage.
- Added Intelligence Lab service links to the footer and direct anchors to the relevant Intelligence Lab cards.
- Removed the Intelligence Lab footer gap.
- Fixed About What Happens Next contrast and centered the Schedule Intro Call button.
- Bumped cache versions to v54.


## Cleanup pass 13 – Offerings consistency and About simplification
- Updated Offerings overview copy from “how leaders decide” to “how leaders make decisions.”
- Standardized At a Glance panels across Health Check, Decision System Reset, and Fractional Analytics using First Step & Length, Best Fit, and Outcome.
- Made the Intelligence Lab offering card match the same width system as the other offerings cards.
- Tightened Fractional Analytics formatting and spacing with final CSS overrides.
- Updated email links to include a direct mailto subject.
- Simplified the About page by removing redundant How We Work and Who We Work Best With sections.


## Cleanup pass 14 – offerings layout, health check copy, and contact routing
- Restored the Offerings overview to three equal core cards with Intelligence Lab as the lower showcase path.
- Reordered Analytics Health Check outputs so Fit Recommendation appears before Current-State Readout.
- Removed “not a generic sales sequence” language from Analytics Health Check.
- Changed Analytics Health Check response timing to within 3 business days.
- Routed the footer “Email Jonah” button to the About page contact section instead of opening mail.
- Re-centered the About page Schedule Intro Call button in What Happens Next.
- Bumped cache version to v56.


## Cleanup pass 15 – card width normalization
- Normalized card-grid widths across Home, How We Help, Offerings, Analytics Health Check, Decision System Reset, Fractional Analytics, Intelligence Lab, and About.
- Removed uneven full-width cards inside standard card rows, while preserving the established Intelligence Lab showcase placement below the three core offerings.
- Added responsive breakpoints so card groups collapse evenly at tablet and mobile sizes.
- Bumped cache version to `v=57`.


## Cleanup pass 17 – About contact balance
- Centered and widened the About Contact Us form area.
- Reduced the footprint of the What Happens Next card so it no longer dominates the bottom section.
- Kept the Schedule Intro Call button centered inside the compact next-step card.
- Updated About response timing to three business days for consistency.
- Bumped cache version to v59.

## Cleanup pass 31 - Home request polish
- Removed the light blue diagnostic panel frame from the Home dashboard-chaos section and smoothed the section back into the shared page background.
- Updated Home problem/example links so each View example opens in a new tab.
- Added a compact Health Check next-steps block near the Home CTA.
- Bumped the Home page cache references to v76.

## Cleanup pass 17 - How We Help hero CTA polish
- Added strong hero CTAs to How We Help: Request an Analytics Health Check and Compare Engagement Paths.
- Styled the hero CTA pair with a gold primary action and dark-blue secondary action to match the Parallax visual system.
- Bumped How We Help cache references to `v=77`.

## Cleanup pass 18 – Offerings fit review and interactive path finder
- Clarified that pricing is provided after the free fit review once scope is understood.
- Replaced Health Check-first language across the Offerings Overview with free fit review-first language.
- Added an interactive Pricing and Fit path finder that lets visitors select their needs and highlights the recommended offering card.
- Updated Offerings Overview CTAs to emphasize the free fit review as the first step.
- Bumped Offerings Overview shared CSS/JS references to `v=78`.

## Cleanup pass 19 - Analytics Health Check clarity
- Reframed the Analytics Health Check page around a clear three-step path: free fit review, paid scoped Health Check if needed, then a recommended next step.
- Clarified that the fit review is free and the Analytics Health Check is a paid scoped initiative.
- Added a representative sample Health Check output section with trust break, evidence pattern, decision impact, and recommendation cards.
- Changed the form submit button from `Submit Health Check Request` to `Start Fit Review`.
- Bumped the Analytics Health Check cache references to `v=79`.

## Cleanup pass 21 - Fractional Analytics engagement shape clarity
- Added hover flip-card behavior to the Fractional Analytics Engagement Shape cards.
- Added commercial clarity on the back of each card for Advisor, Operator, and Embedded Partner.
- Clarified the depth of each path: monthly advisory guidance, weekly or biweekly operating support, and recurring embedded leadership with hands-on ownership.
- Added mobile-friendly fallback behavior so the commercial details remain visible on touch devices.
- Bumped Fractional Analytics cache references to `v=81`.

## Cleanup pass 22 - Intelligence Lab project detail cleanup
- Reworked Intelligence Lab open detail panels into compact project snapshots so they no longer expand into long multi-section boxes.
- Added clearer “what you are looking at” descriptions for each Intelligence Lab example.
- Linked each example directly to its relevant project in a new tab: Operational Risk Digest, RLS Demo Webapp, Enterprise Outcome Studio, and Predictive Risk Intelligence.
- Replaced the pending Customer Health card with a live Predictive Risk Intelligence card so every example has a concrete project destination.
- Updated footer Intelligence Lab links across pages to point to the live Predictive Risk Intelligence card.
- Bumped shared cache references to `v=82`.

## Cleanup pass 36 – About consultancy positioning and credibility polish
- Cleaned the About At a Glance panel so each item uses a single divider line.
- Restyled the three About hero outcome boxes into a more modern compact card treatment.
- Reframed About copy around Parallax as a small consultancy with more consistent “we” language.
- Removed the founder cube from its framed panel treatment and widened it beneath the portrait area.
- Added a short “Why teams bring Jonah in” credibility block with common buyer situations.
- Bumped shared cache references to `v=83`.

## Cleanup pass 37 – Contrast and Fractional card stabilization
- Strengthened Analytics Health Check contrast across the path, fit, output, sample, and form sections.
- Strengthened Decision System Reset participant section contrast so headings, card labels, and body copy are consistently readable.
- Replaced the fragile Fractional Analytics Engagement Shape flip behavior with stable commercial-depth cards that show the offer details directly.
- Bumped shared cache references to `v=84`.

## Cleanup pass 32 – Fit Check CTAs and Home background polish
- Removed the dark outer background layer from the Home “How Teams Work With Parallax Data” section so the global page background remains consistent.
- Updated Home CTA button styling to use the site gold treatment more consistently.
- Renamed primary no-cost CTA language from Analytics Health Check/Fit Review to Free Fit Check across conversion cards and buttons.
- Clarified that the Analytics Health Check is the paid scoped diagnostic that may follow the free Fit Check.
- Bumped shared cache references to `v=85`.



## Cleanup pass 16 - Continuing engagement ladder and offerings polish

- Added Analytics Health Check as the first pillar in the How We Help next-step section, with free Fit Check positioning before paid scope.
- Reframed Intelligence Lab as the premium lower path once the foundation is stable.
- Reduced blank space in the Our Offerings path chooser Intelligence Lab card.
- Rebuilt Pricing and Fit into a simpler user-friendly engagement ladder.
- Replaced the generic proof/output cards with three professional sample output examples for three distinct situations.
- Removed decorative marks from the About hero outcome cards and enlarged the founder cube without reducing the portrait scale.
- Bumped shared CSS/JS cache versions to v86.


## Cleanup pass 17 - Responsive and mobile foundation

- Added a mobile navigation toggle with a stacked menu for small screens.
- Added tablet and phone breakpoints across Home, How We Help, Our Offerings, service pages, Intelligence Lab, and About.
- Converted wide multi-column sections to two-column tablet layouts and one-column mobile layouts.
- Reduced fixed heights, tightened hero spacing, and normalized CTA widths on small screens.
- Added overflow protection and responsive media handling for images, cards, forms, and footer columns.
- Bumped shared CSS/JS cache versions to v87.

## Cleanup pass 19 – Navigation active states and Intelligence Lab dropdown
- Added active-state handling for Offerings Overview and Analytics Health Check so the selected page is highlighted in the dropdown consistently.
- Added an Intelligence Lab dropdown to the primary navigation matching the Our Offerings behavior.
- Linked the Intelligence Lab dropdown to the overview and all current Intelligence Lab service anchors.
- Added dynamic navigation highlighting for Intelligence Lab hash links.
- Bumped shared cache references to `v=88`.


## Cleanup pass 24 – v89 font, fit check, and engagement shape polish
- Normalized typography across pages, forms, buttons, cards, and navigation.
- Added spacing in the How We Help situation cards so yellow action text no longer crowds white body text.
- Rebuilt Fractional Analytics Engagement Shape from three separate flip cards into one large flippable card covering Advisor, Operator, and Embedded Partner.
- Kept the Analytics Health Check page named Analytics Health Check while preserving the free Fit Check intake as the starting action.
- Restored the interactive Fit Check path finder inside Our Offerings Pricing and Fit so selected needs light up the recommended engagement card.
- Reworked Our Offerings sample outputs into three more polished scenario-based examples.
- Bumped shared CSS/JS cache versions to v89.


## Cleanup pass v90 – Home arrows, Health Check samples, Fractional shape
- Removed the duplicate Home “View example” arrow caused by the external-link pseudo-element.
- Rebuilt the Analytics Health Check sample output into a navigable three-example presentation module.
- Added three sample Health Check scenarios: dashboard trust breakdown, analytics bottleneck diagnosis, and intelligence readiness review.
- Restored the Fractional Analytics Engagement Shape as one large stable flippable card on desktop, with readable stacked behavior on tablet/mobile.
- Bumped shared CSS/JS cache versions to `v=90`.


## Targeted v92 update from v90 rollback
- Added stronger hover/focus affordance to Home View example links without reintroducing duplicate arrows.
- Restored Fractional Analytics Engagement Shape to three even flippable cards: Advisor, Operator, and Embedded Partner.
- Added a direct Free Fit Check link under Services in every footer.
- Repaired the fractional flip-card JavaScript setup and bumped cache references to v92.


## v93 – Fractional Analytics visual polish
- Widened the Fractional Analytics Engagement Shape section and cards so the three options have more room on desktop.
- Reworked flip-card behavior so each card rotates cleanly on its own center axis.
- Added stronger tablet and mobile fallbacks for the Engagement Shape cards.
- Added spacing between the Start Here title and supporting copy at the bottom of the Fractional Analytics page.
- Bumped shared CSS/JS cache references to `v=93`.

## Cleanup pass v95 – Nav hierarchy from v93 base
- Rebuilt the update from the v93 Fractional polish package to avoid reverting prior Fractional Analytics layout fixes.
- Added Free Fit Check directly into the Our Offerings top-ribbon dropdown.
- Added visual hierarchy to the Our Offerings and Intelligence Lab dropdown menus with thicker gold bars for parent pages and thinner indented gold bars for in-page destinations.
- Updated active nav logic so hash-based items like Free Fit Check and Intelligence Lab service anchors highlight without also highlighting their parent page item.
- Bumped shared CSS/JS cache versions to v95.



## Cleanup pass 31 – v96 hierarchy and Fractional flip correction
- Moved Free Fit Check under Analytics Health Check in the Our Offerings dropdown hierarchy.
- Increased visual indentation for Free Fit Check as a child path of Analytics Health Check.
- Widened Fractional Analytics engagement shape cards and corrected the card flip so each card rotates on its own center axis.
- Added extra spacing in the Fractional Analytics Start Here CTA section.
- Bumped cache versions to v96.

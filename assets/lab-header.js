(function () {
  const mount = document.querySelector("[data-lab-header]");
  if (mount) {
    const current = mount.getAttribute("data-current") || "";
    const itemClass = (key) => (current === key ? " lab-nav-current" : "");
    mount.outerHTML = `
<header aria-label="Parallax site navigation" class="lab-site-header">
  <a aria-label="Parallax Data Lab home" class="lab-site-brand" href="../index.html"><img alt="Parallax Data Lab logo" src="../assets/parallax_data_lab_original_transparent.png" decoding="async"></a>
  <button aria-controls="lab-primary-navigation" aria-expanded="false" aria-label="Toggle navigation" class="lab-mobile-nav-toggle" type="button"><span></span><span></span><span></span><em>Menu</em></button>
  <nav id="lab-primary-navigation" aria-label="Primary navigation">
    <a href="../index.html">Home</a>
    <div class="lab-nav-dropdown lab-nav-dropdown-offerings lab-nav-dropdown-wide">
      <a class="lab-nav-dropdown-toggle" href="../our-offerings.html">Our Offerings</a>
      <div aria-label="Offerings and expertise sections" class="lab-nav-dropdown-menu lab-nav-menu-hierarchy lab-nav-menu-offerings">
        <div class="lab-nav-menu-group">
          <span class="lab-nav-menu-section-title">Core engagement paths</span>
          <a class="lab-nav-menu-parent" href="../our-offerings.html"><span>Offerings Overview</span></a>
          <a class="lab-nav-menu-child" href="../dashboard-trust-scorecard.html"><span>Diagnostic Scorecard</span><em>Optional</em></a>
          <a class="lab-nav-menu-child" href="../free-fit-check.html"><span>Free Fit Check</span><em>Free</em></a>
          <a class="lab-nav-menu-child" href="../analytics-health-check.html"><span>Analytics Health Check</span></a>
          <a class="lab-nav-menu-child" href="../decision-system-reset.html"><span>Decision System Reset</span></a>
          <a class="lab-nav-menu-child" href="../fractional-analytics.html"><span>Fractional Analytics</span></a>
        </div>
        <div class="lab-nav-menu-group">
          <span class="lab-nav-menu-section-title">Expertise by problem</span>
          <a class="lab-nav-menu-parent" href="../expertise.html"><span>Expertise Overview</span></a>
          <a class="lab-nav-menu-child" href="../power-bi-consultant-cincinnati.html"><span>Power BI & Microsoft Fabric</span></a>
          <a class="lab-nav-menu-child" href="../kpi-reporting-consulting.html"><span>KPI Strategy &amp; Executive Reporting</span></a>
          <a class="lab-nav-menu-child" href="../reporting-automation-consulting.html"><span>Reporting Automation</span></a>
          <a class="lab-nav-menu-child" href="../data-quality-analytics-reliability.html"><span>Data Quality &amp; Analytics Reliability</span></a>
          <a class="lab-nav-menu-child" href="../dashboard-trust-governance.html"><span>BI Governance &amp; Dashboard Trust</span></a>
          <a class="lab-nav-menu-child" href="../data-integration-analytics-architecture.html"><span>Data Integration &amp; Analytics Architecture</span></a>
        </div>
      </div>
    </div>
    <div class="lab-nav-dropdown lab-nav-dropdown-intelligence">
      <a class="lab-nav-dropdown-toggle${current ? " lab-nav-current" : ""}" href="../intelligence-lab.html">Intelligence Lab</a>
      <div aria-label="Intelligence Lab services" class="lab-nav-dropdown-menu lab-nav-dropdown-menu-intelligence lab-nav-menu-hierarchy">
        <div class="lab-nav-menu-group">
          <span class="lab-nav-menu-section-title">Intelligence Lab</span>
          <a class="lab-nav-menu-parent" href="../intelligence-lab.html"><span>Intelligence Lab Overview</span></a>
          <a class="lab-nav-menu-child" href="../decision-workspace.html"><span>Interactive Decision Workspace Demo</span></a>
        </div>
        <div class="lab-nav-menu-group">
          <span class="lab-nav-menu-section-title">Lab initiatives</span>
          <a class="lab-nav-menu-child${itemClass("operational-risk-digest")}" href="../operational-risk-digest/index.html"><span>Operations Intelligence Digest</span></a>
          <a class="lab-nav-menu-child${itemClass("rls-demo-webapp")}" href="../rls-demo-webapp/index.html"><span>Governance &amp; RLS Architecture</span></a>
          <a class="lab-nav-menu-child${itemClass("enterprise-outcome-studio")}" href="../enterprise-outcome-studio/index.html"><span>Enterprise Outcome Studio</span></a>
          <a class="lab-nav-menu-child${itemClass("predictive-risk-intelligence")}" href="../predictive-risk-intelligence/index.html"><span>Predictive Risk Intelligence</span></a>
        </div>
      </div>
    </div>
    <div class="lab-nav-dropdown lab-nav-dropdown-case-studies">
      <a class="lab-nav-dropdown-toggle" href="../case-studies.html">Case Studies</a>
      <div aria-label="Case studies by industry" class="lab-nav-dropdown-menu lab-nav-menu-hierarchy lab-nav-dropdown-menu-case-studies">
        <div class="lab-nav-menu-group">
          <a class="lab-nav-menu-parent" href="../case-studies.html"><span>Case Studies Overview</span></a>
          <span class="lab-nav-menu-section-title">Industrial operations</span>
          <a class="lab-nav-menu-child" href="../case-studies.html#manufacturing-throughput"><span>Manufacturing</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#utilities-reliability"><span>Utilities</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#energy-operations"><span>Energy</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#construction-project-controls"><span>Construction</span></a>
        </div>
        <div class="lab-nav-menu-group">
          <span class="lab-nav-menu-section-title">Distributed operations</span>
          <a class="lab-nav-menu-child" href="../case-studies.html#logistics-service-level"><span>Logistics & Transportation</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#field-services-kpis"><span>Field Services</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#retail-multi-location"><span>Retail & Multi-Location</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#facilities-maintenance"><span>Facilities & Maintenance</span></a>
        </div>
        <div class="lab-nav-menu-group">
          <span class="lab-nav-menu-section-title">Commercial and supply chain</span>
          <a class="lab-nav-menu-child" href="../case-studies.html#healthcare-utilization"><span>Healthcare Operations</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#industrial-software-revenue"><span>Industrial Software</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#b2b-services-scorecard"><span>B2B Services</span></a>
          <a class="lab-nav-menu-child" href="../case-studies.html#distribution-supply-chain"><span>Distribution & Supply Chain</span></a>
        </div>
      </div>
    </div>
    <a href="../insights.html">Insights</a>
    <div class="lab-nav-dropdown lab-nav-dropdown-about">
      <a class="lab-nav-dropdown-toggle" href="../about.html">About</a>
      <div aria-label="About Parallax Data Lab" class="lab-nav-dropdown-menu lab-nav-menu-hierarchy lab-nav-dropdown-menu-about">
        <span class="lab-nav-menu-section-title">About</span>
        <a class="lab-nav-menu-parent" href="../about.html"><span>About Parallax</span></a>
        <a class="lab-nav-menu-child" href="../contact.html"><span>Contact</span></a>
        <a class="lab-nav-menu-child" href="../business-intelligence-consultant-cincinnati.html"><span>Local Analytics Consulting</span></a>
      </div>
    </div>
  </nav>
</header>`;
  }

  const header = document.querySelector(".lab-site-header");
  if (!header) return;

  const navToggle = header.querySelector(".lab-mobile-nav-toggle");
  const dropdowns = Array.from(header.querySelectorAll(".lab-nav-dropdown"));

  function closeDropdowns(except) {
    dropdowns.forEach((dropdown) => {
      if (dropdown !== except) {
        dropdown.classList.remove("is-open");
        dropdown.querySelector(".lab-nav-dropdown-toggle")?.setAttribute("aria-expanded", "false");
      }
    });
  }

  navToggle?.addEventListener("click", () => {
    const isOpen = header.classList.toggle("is-nav-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
    if (!isOpen) closeDropdowns();
  });

  dropdowns.forEach((dropdown) => {
    const toggle = dropdown.querySelector(".lab-nav-dropdown-toggle");
    toggle?.setAttribute("aria-expanded", "false");
    toggle?.addEventListener("click", (event) => {
      if (window.matchMedia("(max-width: 1120px)").matches) {
        event.preventDefault();
      }
      const nextOpen = !dropdown.classList.contains("is-open");
      closeDropdowns(dropdown);
      dropdown.classList.toggle("is-open", nextOpen);
      toggle.setAttribute("aria-expanded", String(nextOpen));
    });
  });

  document.addEventListener("click", (event) => {
    if (!header.contains(event.target)) {
      header.classList.remove("is-nav-open");
      navToggle?.setAttribute("aria-expanded", "false");
      closeDropdowns();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      header.classList.remove("is-nav-open");
      navToggle?.setAttribute("aria-expanded", "false");
      closeDropdowns();
    }
  });
})();

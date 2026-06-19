(function () {
  const storageKey = "parallaxDecisionWorkspace.v1";
  const sessionKey = "parallaxDecisionWorkspace.session";

  const fieldSets = {
    recommendations: [
      ["title", "Recommendation", "text", true],
      ["why", "Why it matters", "textarea", true],
      ["ownerId", "Owner", "user", true],
      ["priority", "Priority", "select", true, ["High", "Medium", "Low"]],
      ["effort", "Effort", "select", true, ["Small", "Medium", "Large"]],
      ["status", "Status", "select", true, ["Not started", "In progress", "Blocked", "Done"]],
      ["dueDate", "Due date", "date", false],
      ["related", "Related metric / dashboard / decision", "text", false],
      ["evidence", "Evidence needed", "textarea", false],
      ["nextStep", "Next step", "textarea", true]
    ],
    metrics: [
      ["name", "Metric name", "text", true],
      ["definition", "Business definition", "textarea", true],
      ["ownerId", "Owner", "user", true],
      ["contributors", "Contributors", "text", false],
      ["source", "Source system", "text", true],
      ["logic", "Calculation logic", "textarea", false],
      ["refresh", "Refresh cadence", "select", true, ["Daily", "Weekly", "Monthly", "Quarterly", "Unknown"]],
      ["decision", "Decision supported", "text", true],
      ["disputes", "Known disputes", "textarea", false],
      ["trust", "Trust status", "select", true, ["Trusted", "Needs review", "Disputed", "Unknown"]]
    ],
    decisions: [
      ["name", "Decision name", "text", true],
      ["ownerId", "Decision owner", "user", true],
      ["cadence", "Cadence", "select", true, ["Daily", "Weekly", "Monthly", "Quarterly", "Event-driven"]],
      ["metrics", "Supporting metrics", "text", true],
      ["options", "Decision options", "textarea", true],
      ["criteria", "Decision criteria", "textarea", true],
      ["selectedOption", "Current / default option", "text", false],
      ["trigger", "Trigger threshold", "textarea", false],
      ["forum", "Meeting / forum", "text", false],
      ["escalation", "Escalation path", "textarea", false],
      ["friction", "Current friction", "textarea", true]
    ],
    dashboards: [
      ["name", "Dashboard / report name", "text", true],
      ["reportUrl", "Report link", "url", false],
      ["audience", "Audience", "text", true],
      ["ownerId", "Owner", "user", true],
      ["platform", "Reporting source", "select", true, ["Power BI", "Tableau", "Looker", "Excel / Sheets", "ERP report", "CRM report", "Other"]],
      ["location", "Workspace / location", "text", true],
      ["purpose", "Purpose", "textarea", true],
      ["sources", "Source systems", "text", false],
      ["trustScore", "Trust score", "select", true, ["1", "2", "3", "4", "5"]],
      ["issues", "Known issues", "textarea", true],
      ["action", "Recommended action", "select", true, ["Keep", "Fix", "Merge", "Retire"]],
      ["priority", "Priority", "select", true, ["High", "Medium", "Low"]]
    ],
    users: [
      ["name", "Name", "text", true],
      ["email", "Email", "email", true],
      ["role", "Role", "select", true, ["Org Admin", "Owner", "Contributor", "Viewer"]],
      ["password", "Temporary password", "text", true]
    ]
  };

  const tableColumns = {
    recommendations: ["title", "ownerId", "priority", "status", "dueDate", "nextStep"],
    metrics: ["name", "ownerId", "source", "refresh", "decision", "trust"],
    decisions: ["name", "ownerId", "cadence", "options", "selectedOption", "criteria", "metrics"],
    dashboards: ["name", "platform", "location", "audience", "ownerId", "trustScore", "action", "priority"],
    users: ["name", "email", "role"]
  };

  const labels = {
    title: "Recommendation",
    why: "Why",
    ownerId: "Owner",
    priority: "Priority",
    effort: "Effort",
    status: "Status",
    dueDate: "Due",
    related: "Related",
    evidence: "Evidence",
    nextStep: "Next step",
    name: "Name",
    definition: "Definition",
    contributors: "Contributors",
    source: "Source",
    logic: "Logic",
    refresh: "Refresh",
    decision: "Decision",
    disputes: "Disputes",
    trust: "Trust",
    cadence: "Cadence",
    metrics: "Metrics",
    options: "Decision options",
    criteria: "Criteria",
    selectedOption: "Current option",
    trigger: "Trigger",
    forum: "Forum",
    escalation: "Escalation",
    friction: "Friction",
    audience: "Audience",
    reportUrl: "Report link",
    platform: "Source",
    location: "Location",
    purpose: "Purpose",
    sources: "Sources",
    trustScore: "Trust",
    action: "Action",
    email: "Email",
    role: "Role"
  };

  const helpText = {
    title: "Write the recommendation as a clear action, not a broad theme. Example: Assign owners to the five executive KPIs.",
    why: "Explain the business friction, risk, or cost this recommendation solves.",
    ownerId: "Choose the person accountable for moving this item forward.",
    priority: "Use High for work that blocks decisions, reporting trust, or executive alignment.",
    effort: "Estimate the practical lift so leaders can sequence the work.",
    status: "Track whether this is still open, in progress, blocked, or complete.",
    dueDate: "Add the target date when the next meaningful progress should happen.",
    related: "Name the metric, dashboard, decision, or reset work this recommendation supports.",
    evidence: "List what proof, screenshots, exports, examples, or stakeholder input is needed.",
    nextStep: "Write the next concrete action someone can take after this meeting.",
    name: "Use the real business name people would recognize in a meeting or reporting workspace.",
    definition: "Define the metric in business language, including what is included and excluded.",
    contributors: "Name teams or people who provide context, data, or approval.",
    source: "Name the source system or report where this number comes from.",
    logic: "Describe the calculation rule, formula, filter, or grain at a practical level.",
    refresh: "Choose how often the value should be refreshed for the decision it supports.",
    decision: "Name the recurring business decision this metric is meant to inform.",
    disputes: "Capture where people disagree about the definition, source, or interpretation.",
    trust: "Mark whether leaders can use this confidently or whether it needs review.",
    cadence: "Choose how often this decision is actually made.",
    metrics: "List the metrics or signals leaders need before choosing an option.",
    options: "List the real choices available. Example: approve overtime, rebalance routes, defer work, or add vendor capacity.",
    criteria: "Explain how leaders choose between the options, including thresholds or tradeoffs.",
    selectedOption: "Enter the default or currently favored option if one exists.",
    trigger: "Describe the condition that forces this decision, such as margin below target or backlog above threshold.",
    forum: "Name the meeting, workflow, or operating cadence where this decision should happen.",
    escalation: "Explain who decides when the normal owner cannot resolve the issue.",
    friction: "Describe what currently slows or confuses this decision.",
    audience: "Name who uses this dashboard or report.",
    reportUrl: "Paste the direct Power BI, Tableau, Looker, spreadsheet, or report URL.",
    platform: "Choose where the dashboard lives, such as Power BI, Tableau, Looker, or a spreadsheet.",
    location: "Name the workspace, folder, app, team site, or reporting source location.",
    purpose: "Explain the decision or operating conversation this dashboard should support.",
    sources: "List the underlying systems or extracts feeding the dashboard.",
    trustScore: "Score how confidently leaders can act on this dashboard today.",
    issues: "Capture known trust, ownership, definition, refresh, or duplication problems.",
    action: "Choose whether the dashboard should stay, be repaired, merged, or retired.",
    email: "Use the user's work email address.",
    role: "Choose the access level this person should have in the organization workspace.",
    password: "Create a temporary password for this prototype user."
  };

  const state = {
    data: loadData(),
    session: loadSession(),
    authMode: initialAuthMode(),
    humanChallenge: createHumanChallenge(),
    activeTab: "home",
    editing: null
  };

  function id(prefix) {
    return `${prefix}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
  }

  function createHumanChallenge() {
    const left = Math.floor(Math.random() * 8) + 2;
    const right = Math.floor(Math.random() * 7) + 3;
    return { left, right, answer: left + right };
  }

  function initialAuthMode() {
    const mode = new URLSearchParams(window.location.search).get("auth");
    return mode === "login" ? "login" : "signup";
  }

  function defaultData() {
    const org1 = "org-acme";
    const org2 = "org-northstar";
    const users = [
      { id: "u-admin", orgId: null, name: "Jonah / Parallax Admin", email: "admin@parallaxdatalab.com", password: "parallax-admin", role: "Parallax Admin" },
      { id: "u-alex", orgId: org1, name: "Alex Rivera", email: "alex@acmeops.com", password: "decision123", role: "Org Admin" },
      { id: "u-morgan", orgId: org1, name: "Morgan Lee", email: "morgan@acmeops.com", password: "decision123", role: "Contributor" },
      { id: "u-taylor", orgId: org2, name: "Taylor Grant", email: "taylor@northstar.com", password: "decision123", role: "Viewer" }
    ];

    return {
      organizations: [
        { id: org1, name: "Acme Operations Group", industry: "Distribution and field services" },
        { id: org2, name: "Northstar Manufacturing", industry: "Manufacturing" }
      ],
      users,
      recommendations: [
        { id: id("rec"), orgId: org1, title: "Assign owners to the five executive KPIs", why: "Leaders currently debate definitions before they can discuss action.", ownerId: "u-alex", priority: "High", effort: "Small", status: "In progress", dueDate: "2026-07-10", related: "Metric Ownership Map", evidence: "Current KPI list and recurring leadership meeting agenda", nextStep: "Confirm one accountable owner and one finance/data contributor per metric." },
        { id: id("rec"), orgId: org1, title: "Retire duplicate weekly operations reports", why: "Three versions of the same weekly report are creating reconciliation work.", ownerId: "u-morgan", priority: "High", effort: "Medium", status: "Not started", dueDate: "2026-07-17", related: "Dashboard Trust Register", evidence: "Screenshots or links for each duplicate report", nextStep: "Identify the report of record and mark the other two for retirement." }
      ],
      metrics: [
        { id: id("met"), orgId: org1, name: "On-time completion rate", definition: "Percent of scheduled jobs completed within the committed service window.", ownerId: "u-alex", contributors: "Operations, Dispatch, Finance", source: "Service platform", logic: "Completed on time / completed jobs", refresh: "Weekly", decision: "Where to add capacity or change routing", disputes: "Exception handling for customer reschedules", trust: "Needs review" },
        { id: id("met"), orgId: org1, name: "Gross margin by customer", definition: "Customer revenue less labor, materials, and direct service costs.", ownerId: "u-morgan", contributors: "Finance, Sales Ops", source: "ERP + payroll export", logic: "Revenue - direct costs", refresh: "Monthly", decision: "Which accounts require pricing or service model changes", disputes: "Labor allocation logic", trust: "Disputed" }
      ],
      decisions: [
        { id: id("dec"), orgId: org1, name: "Weekly capacity adjustment", ownerId: "u-alex", cadence: "Weekly", metrics: "On-time completion rate, backlog, overtime hours", options: "Approve overtime; rebalance routes; defer low-priority work; add temporary vendor capacity", criteria: "Use overtime when backlog is short-term. Rebalance routes when one region is below 90% on-time completion. Add vendor capacity when backlog exceeds two weeks.", selectedOption: "Rebalance routes first", trigger: "On-time rate below 92% for two weeks", forum: "Monday operations review", escalation: "Ops director decides routing or overtime changes", friction: "Leaders see the lagging metric but not the capacity trigger." }
      ],
      dashboards: [
        { id: id("dash"), orgId: org1, name: "Weekly Ops Scorecard", reportUrl: "https://app.powerbi.com/groups/sample/reports/weekly-ops-scorecard", audience: "COO, operations directors, finance", ownerId: "u-morgan", platform: "Power BI", location: "Executive Operations workspace", purpose: "Show capacity, service reliability, and margin pressure by region.", sources: "Service platform, ERP, payroll export", trustScore: "3", issues: "Definitions are good, but cost allocation and exception handling need approval.", action: "Fix", priority: "High" },
        { id: id("dash"), orgId: org1, name: "Legacy Regional Report", reportUrl: "", audience: "Regional managers", ownerId: "u-alex", platform: "Excel / Sheets", location: "Regional manager shared drive", purpose: "Old weekly report used before the scorecard existed.", sources: "Spreadsheet export", trustScore: "2", issues: "Duplicates several scorecard metrics with different filters.", action: "Merge", priority: "Medium" }
      ]
    };
  }

  function loadData() {
    try {
      return normalizeData(JSON.parse(localStorage.getItem(storageKey)) || defaultData());
    } catch (error) {
      return normalizeData(defaultData());
    }
  }

  function normalizeData(data) {
    const base = defaultData();
    const next = {
      schemaVersion: 2,
      organizations: Array.isArray(data.organizations) ? data.organizations : base.organizations,
      users: Array.isArray(data.users) ? data.users : base.users,
      recommendations: Array.isArray(data.recommendations) ? data.recommendations : base.recommendations,
      metrics: Array.isArray(data.metrics) ? data.metrics : base.metrics,
      decisions: Array.isArray(data.decisions) ? data.decisions : base.decisions,
      dashboards: Array.isArray(data.dashboards) ? data.dashboards : base.dashboards
    };

    next.decisions = next.decisions.map((item) => ({
      options: "",
      criteria: "",
      selectedOption: "",
      ...item
    }));
    next.dashboards = next.dashboards.map((item) => ({
      platform: "",
      location: "",
      reportUrl: "",
      ...item
    }));
    return next;
  }

  function saveData() {
    localStorage.setItem(storageKey, JSON.stringify(state.data));
  }

  function loadSession() {
    try {
      return JSON.parse(sessionStorage.getItem(sessionKey));
    } catch (error) {
      return null;
    }
  }

  function saveSession() {
    if (state.session) {
      sessionStorage.setItem(sessionKey, JSON.stringify(state.session));
    } else {
      sessionStorage.removeItem(sessionKey);
    }
  }

  function currentUser() {
    return state.data.users.find((user) => user.id === state.session?.userId) || null;
  }

  function isParallaxAdmin() {
    return currentUser()?.role === "Parallax Admin";
  }

  function canEdit() {
    const role = currentUser()?.role;
    return role === "Parallax Admin" || role === "Org Admin" || role === "Owner" || role === "Contributor";
  }

  function canManageUsers() {
    const role = currentUser()?.role;
    return role === "Parallax Admin" || role === "Org Admin";
  }

  function activeOrg() {
    return state.data.organizations.find((org) => org.id === state.session?.activeOrgId) || state.data.organizations[0];
  }

  function orgUsers() {
    const org = activeOrg();
    return state.data.users.filter((user) => user.orgId === org.id);
  }

  function orgItems(type) {
    const org = activeOrg();
    if (type === "users") return orgUsers();
    return state.data[type].filter((item) => item.orgId === org.id);
  }

  function userName(userId) {
    return state.data.users.find((user) => user.id === userId)?.name || "Unassigned";
  }

  function boot() {
    setupEvents();
    render();
  }

  function setupEvents() {
    document.querySelector("[data-login-form]")?.addEventListener("submit", handleLogin);
    document.querySelectorAll("[data-auth-mode]").forEach((button) => {
      button.addEventListener("click", () => {
        setAuthMode(button.dataset.authMode || "signup");
        if (currentUser()) {
          state.session = null;
          saveSession();
          render();
        }
        document.querySelector("[data-view='login']")?.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
    document.querySelector("[data-logout]")?.addEventListener("click", () => {
      state.session = null;
      saveSession();
      render();
    });
    document.querySelector("[data-reset-demo]")?.addEventListener("click", () => {
      if (!isParallaxAdmin()) {
        alert("Only a Parallax admin can reset demo data.");
        return;
      }
      state.data = defaultData();
      const user = currentUser();
      state.session = user ? state.session : null;
      saveData();
      render();
    });
    document.querySelector("[data-org-switch]")?.addEventListener("change", (event) => {
      state.session.activeOrgId = event.target.value;
      saveSession();
      render();
    });
    document.querySelectorAll("[data-tab-target]").forEach((button) => {
      button.addEventListener("click", () => {
        state.activeTab = button.dataset.tabTarget;
        render();
      });
    });
    document.querySelectorAll("[data-open-form]").forEach((button) => {
      button.addEventListener("click", () => openForm(button.dataset.openForm));
    });
    document.querySelector("[data-close-modal]")?.addEventListener("click", closeModal);
    document.querySelector("[data-modal]")?.addEventListener("click", (event) => {
      if (event.target.matches("[data-modal]")) closeModal();
    });
    document.querySelector("[data-print-report]")?.addEventListener("click", () => window.print());
    document.querySelector("[data-delete-org]")?.addEventListener("click", deleteActiveOrg);
    document.querySelector("[data-forgot-password]")?.addEventListener("click", handleForgotPassword);
  }

  function handleLogin(event) {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    const email = String(form.get("email") || "").trim().toLowerCase();
    const password = String(form.get("password") || "");
    if (!validateHumanCheck(form)) return;

    if (state.authMode === "signup") {
      handleSignup(form, email, password);
      return;
    }

    const user = state.data.users.find((item) => item.email.toLowerCase() === email && item.password === password);
    const error = document.querySelector("[data-login-error]");
    if (!user) {
      if (error) error.textContent = "Email or password did not match a demo account.";
      resetHumanCheck();
      return;
    }
    const activeOrgId = user.role === "Parallax Admin" ? state.data.organizations[0]?.id : user.orgId;
    state.session = { userId: user.id, activeOrgId };
    saveSession();
    render();
  }

  function handleSignup(form, email, password) {
    const error = document.querySelector("[data-login-error]");
    const orgName = String(form.get("orgName") || "").trim();
    const name = String(form.get("name") || "").trim();
    const confirmPassword = String(form.get("confirmPassword") || "");
    if (!orgName || !name) {
      if (error) error.textContent = "Add an organization name and your name to create the account.";
      return;
    }
    if (password !== confirmPassword) {
      if (error) error.textContent = "Password and confirmation must match.";
      resetHumanCheck();
      return;
    }
    if (state.data.users.some((item) => item.email.toLowerCase() === email)) {
      if (error) error.textContent = "That email already has an account. Switch to log in.";
      resetHumanCheck();
      return;
    }
    const orgId = id("org");
    const userId = id("user");
    state.data.organizations.push({ id: orgId, name: orgName, industry: "New client workspace" });
    state.data.users.push({ id: userId, orgId, name, email, password, role: "Org Admin" });
    state.data.recommendations.push({
      id: id("rec"),
      orgId,
      title: "Review Parallax recommendations and assign owners",
      why: "A recommendation only changes operations when a person owns the next step.",
      ownerId: userId,
      priority: "High",
      effort: "Small",
      status: "Not started",
      dueDate: "",
      related: "Decision System Reset",
      evidence: "Fit Check, Health Check, or Reset notes",
      nextStep: "Add the first three recommendations and assign a responsible owner."
    });
    saveData();
    state.session = { userId, activeOrgId: orgId };
    saveSession();
    if (error) error.textContent = "";
    render();
  }

  function validateHumanCheck(form) {
    const error = document.querySelector("[data-login-error]");
    const answer = Number(String(form.get("humanAnswer") || "").trim());
    if (answer !== state.humanChallenge.answer) {
      if (error) error.textContent = "Human check did not match. Try the new question.";
      resetHumanCheck();
      return false;
    }
    if (error) error.textContent = "";
    return true;
  }

  function resetHumanCheck() {
    state.humanChallenge = createHumanChallenge();
    renderHumanCheck();
  }

  async function handleForgotPassword() {
    const error = document.querySelector("[data-login-error]");
    const email = String(document.querySelector("[name='email']")?.value || "").trim().toLowerCase();
    if (!email) {
      if (error) error.textContent = "Enter your email first, then request a password reset.";
      return;
    }
    const supabaseClient = window.decisionWorkspaceSupabase?.client;
    if (!supabaseClient?.auth?.resetPasswordForEmail) {
      if (error) error.textContent = "Password reset is available after Supabase Auth is fully deployed.";
      return;
    }
    const redirectTo = `${window.location.origin}${window.location.pathname}?auth=login`;
    const { error: resetError } = await supabaseClient.auth.resetPasswordForEmail(email, { redirectTo });
    if (error) {
      error.textContent = resetError
        ? resetError.message
        : "Password reset email sent. Check your inbox.";
    }
  }

  function render() {
    const loggedIn = Boolean(currentUser() && activeOrg());
    document.querySelector('[data-view="login"]')?.classList.toggle("is-hidden", loggedIn);
    document.querySelector('[data-view="app"]')?.classList.toggle("is-hidden", !loggedIn);
    document.querySelector("[data-auth-actions]")?.classList.toggle("is-hidden", loggedIn);
    renderAuthMode();
    if (!loggedIn) return;

    renderShell();
    renderHome();
    renderTables();
    renderReport();
  }

  function setAuthMode(mode) {
    state.authMode = mode === "login" ? "login" : "signup";
    const error = document.querySelector("[data-login-error]");
    if (error) error.textContent = "";
    resetHumanCheck();
    renderAuthMode();
  }

  function renderAuthMode() {
    const isSignup = state.authMode !== "login";
    const eyebrow = document.querySelector("[data-auth-eyebrow]");
    const title = document.querySelector("[data-auth-title]");
    const copy = document.querySelector("[data-auth-copy]");
    const submit = document.querySelector("[data-auth-submit]");
    if (eyebrow) eyebrow.textContent = isSignup ? "New client workspace" : "Returning workspace";
    if (title) title.textContent = isSignup ? "Create your reporting action workspace." : "Log in to your decision workspace.";
    if (copy) {
      copy.textContent = isSignup
        ? "Start an organization account to turn recommendations into owned decisions, metrics, dashboards, and action plans."
        : "Access your organization workspace or Parallax admin view.";
    }
    document.querySelector("[data-signup-fields]")?.classList.toggle("is-hidden", !isSignup);
    document.querySelector("[data-confirm-password-wrap]")?.classList.toggle("is-hidden", !isSignup);
    if (submit) submit.textContent = isSignup ? "Create organization" : "Log in";
    document.querySelector("[data-forgot-password]")?.classList.toggle("is-hidden", isSignup);
    renderHumanCheck();
    document.querySelectorAll("[data-auth-mode]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.authMode === state.authMode);
    });
    const email = document.querySelector("[name='email']");
    const password = document.querySelector("[name='password']");
    const confirmPassword = document.querySelector("[name='confirmPassword']");
    if (email && password) {
      email.value = isSignup ? "client@example.com" : "admin@parallaxdatalab.com";
      password.value = isSignup ? "decision123" : "parallax-admin";
      password.setAttribute("autocomplete", isSignup ? "new-password" : "current-password");
      password.type = "password";
    }
    if (confirmPassword) {
      confirmPassword.value = isSignup ? "decision123" : "";
      confirmPassword.required = isSignup;
    }
  }

  function renderHumanCheck() {
    const question = document.querySelector("[data-human-question]");
    const answer = document.querySelector("[name='humanAnswer']");
    if (question) question.textContent = `Human check: what is ${state.humanChallenge.left} + ${state.humanChallenge.right}?`;
    if (answer) answer.value = "";
  }

  function renderShell() {
    const user = currentUser();
    const org = activeOrg();
    document.querySelector("[data-active-org-name]").textContent = org.name;
    document.querySelector("[data-active-user-summary]").textContent = `${user.name} - ${user.role}`;
    document.querySelector("[data-active-tab-label]").textContent = labelForTab(state.activeTab);
    document.querySelector("[data-page-title]").textContent = titleForTab(state.activeTab);
    document.querySelectorAll("[data-tab-target]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.tabTarget === state.activeTab);
    });
    document.querySelectorAll("[data-tab-panel]").forEach((panel) => {
      panel.classList.toggle("is-hidden", panel.dataset.tabPanel !== state.activeTab);
    });

    const switchWrap = document.querySelector("[data-org-switch-wrap]");
    const switcher = document.querySelector("[data-org-switch]");
    switchWrap?.classList.toggle("is-hidden", !isParallaxAdmin());
    if (switcher) {
      switcher.innerHTML = state.data.organizations.map((item) => `<option value="${item.id}">${escapeHtml(item.name)}</option>`).join("");
      switcher.value = org.id;
    }

    document.querySelectorAll("[data-open-form]").forEach((button) => {
      const type = button.dataset.openForm;
      button.disabled = type === "users" ? !canManageUsers() : !canEdit();
    });
    document.querySelector("[data-reset-demo]")?.classList.toggle("is-hidden", !isParallaxAdmin());
    document.querySelector("[data-org-admin-panel]")?.classList.toggle("is-hidden", !isParallaxAdmin());
  }

  function labelForTab(tab) {
    return {
      home: "Home",
      recommendations: "Action plan",
      metrics: "Metric ownership",
      decisions: "Decision map",
      dashboards: "Dashboard trust",
      users: "Org access",
      export: "Reset export"
    }[tab] || "Workspace";
  }

  function titleForTab(tab) {
    return {
      home: "Reporting system command center",
      recommendations: "Recommendation action plan",
      metrics: "Metric ownership map",
      decisions: "Decision map",
      dashboards: "Dashboard trust register",
      users: "Users and access",
      export: "Decision System Reset artifact"
    }[tab] || "Workspace";
  }

  function renderHome() {
    const recs = orgItems("recommendations");
    const metrics = orgItems("metrics");
    const decisions = orgItems("decisions");
    const dashboards = orgItems("dashboards");
    const openRecs = recs.filter((item) => item.status !== "Done");
    const unownedMetrics = metrics.filter((item) => !item.ownerId || item.trust !== "Trusted");
    const lowTrustDashboards = dashboards.filter((item) => Number(item.trustScore) <= 3 || item.action !== "Keep");
    const unmappedDecisions = decisions.filter((item) => !item.metrics || item.metrics.length < 5 || !item.options || !item.criteria);
    const health = calculateHealth(recs, metrics, decisions, dashboards);

    const kpis = [
      [openRecs.length, "open recommendations"],
      [unownedMetrics.length, "metrics needing ownership/review"],
      [lowTrustDashboards.length, "dashboard trust issues"],
      [unmappedDecisions.length, "decisions missing metric support"]
    ];
    document.querySelector("[data-kpi-grid]").innerHTML = kpis.map(([value, label]) => `<div class="workspace-kpi"><strong>${value}</strong><span>${label}</span></div>`).join("");

    const next = openRecs
      .slice()
      .sort((a, b) => priorityWeight(a.priority) - priorityWeight(b.priority))
      .slice(0, 5);
    document.querySelector("[data-next-actions]").innerHTML = next.length
      ? `<div class="workspace-action-list">${next.map((item) => `<div class="workspace-action-item"><strong>${escapeHtml(item.title)}</strong><span>${escapeHtml(userName(item.ownerId))} - ${escapeHtml(item.priority)} - ${escapeHtml(item.status)}</span><span>${escapeHtml(item.nextStep || "")}</span></div>`).join("")}</div>`
      : `<p class="workspace-muted">No open recommendations. Add a new action or export the reset artifact.</p>`;

    document.querySelector("[data-health-meter]").innerHTML = `<strong>${health}% healthy</strong><div class="workspace-health-bar" aria-label="Decision system health"><span style="width:${health}%"></span></div>`;
  }

  function calculateHealth(recs, metrics, decisions, dashboards) {
    const total = Math.max(1, recs.length + metrics.length + decisions.length + dashboards.length);
    const good =
      recs.filter((item) => item.status === "Done").length +
      metrics.filter((item) => item.ownerId && item.trust === "Trusted").length +
      decisions.filter((item) => item.metrics && item.options && item.criteria && item.ownerId).length +
      dashboards.filter((item) => Number(item.trustScore) >= 4 && item.action === "Keep").length;
    return Math.round((good / total) * 100);
  }

  function priorityWeight(priority) {
    return { High: 1, Medium: 2, Low: 3 }[priority] || 4;
  }

  function renderTables() {
    ["recommendations", "metrics", "decisions", "dashboards", "users"].forEach(renderTable);
  }

  function renderTable(type) {
    const table = document.querySelector(`[data-table="${type}"]`);
    if (!table) return;
    const columns = tableColumns[type];
    const editable = type === "users" ? canManageUsers() : canEdit();
    const rows = orgItems(type);
    table.innerHTML = `
      <thead><tr>${columns.map((col) => `<th>${escapeHtml(labels[col] || col)}</th>`).join("")}<th>Actions</th></tr></thead>
      <tbody>
        ${rows.map((row) => `<tr>${columns.map((col) => `<td>${formatCell(col, row[col], row, type)}</td>`).join("")}<td>${editable ? `<div class="workspace-row-actions"><button class="workspace-row-action" data-edit="${type}" data-id="${row.id}" type="button">Edit</button><button class="workspace-row-action is-danger" data-delete="${type}" data-id="${row.id}" type="button">Delete</button></div>` : `<span class="workspace-muted">Read only</span>`}</td></tr>`).join("")}
      </tbody>`;
    table.querySelectorAll("[data-edit]").forEach((button) => {
      button.addEventListener("click", () => openForm(button.dataset.edit, button.dataset.id));
    });
    table.querySelectorAll("[data-delete]").forEach((button) => {
      button.addEventListener("click", () => deleteItem(button.dataset.delete, button.dataset.id));
    });
  }

  function formatCell(key, value, row, type) {
    if (key === "ownerId") return escapeHtml(userName(value));
    if (type === "dashboards" && key === "name" && row.reportUrl) {
      return `<a class="workspace-table-link" href="${escapeHtml(row.reportUrl)}" target="_blank" rel="noopener noreferrer">${escapeHtml(value || "")}</a>`;
    }
    if (["status", "priority", "trust", "action", "role"].includes(key)) {
      const cls = ["Blocked", "High", "Disputed", "Needs review", "Fix", "Merge", "Retire"].includes(value) ? " is-risk" : ["Done", "Trusted", "Keep"].includes(value) ? " is-done" : "";
      return `<span class="workspace-status${cls}">${escapeHtml(value || "")}</span>`;
    }
    if (key === "trustScore") return `<span class="workspace-status${Number(value) <= 3 ? " is-risk" : " is-done"}">${escapeHtml(value || "")}/5</span>`;
    return escapeHtml(value || "");
  }

  function deleteItem(type, itemId) {
    if (type === "users" && !canManageUsers()) return;
    if (type !== "users" && !canEdit()) return;
    const collection = type === "users" ? state.data.users : state.data[type];
    const item = collection.find((entry) => entry.id === itemId);
    if (!item) return;
    const label = item.name || item.title || item.email || "this item";
    if (!window.confirm(`Delete ${label}? This cannot be undone in the local prototype.`)) return;
    if (type === "users" && item.id === currentUser()?.id) {
      alert("You cannot delete your own active user.");
      return;
    }
    const index = collection.findIndex((entry) => entry.id === itemId);
    collection.splice(index, 1);
    saveData();
    render();
  }

  function deleteActiveOrg() {
    if (!isParallaxAdmin()) return;
    const org = activeOrg();
    if (!org) return;
    const orgUsers = state.data.users.filter((user) => user.orgId === org.id);
    const artifactCount = ["recommendations", "metrics", "decisions", "dashboards"]
      .reduce((total, type) => total + state.data[type].filter((item) => item.orgId === org.id).length, 0);
    const firstConfirm = window.confirm(`Delete ${org.name}? This will remove ${orgUsers.length} users and ${artifactCount} workspace records from the local prototype.`);
    if (!firstConfirm) return;
    const typed = window.prompt(`Type DELETE ${org.name} to confirm organization deletion.`);
    if (typed !== `DELETE ${org.name}`) {
      alert("Organization deletion cancelled. Confirmation text did not match.");
      return;
    }
    state.data.organizations = state.data.organizations.filter((item) => item.id !== org.id);
    state.data.users = state.data.users.filter((item) => item.orgId !== org.id);
    ["recommendations", "metrics", "decisions", "dashboards"].forEach((type) => {
      state.data[type] = state.data[type].filter((item) => item.orgId !== org.id);
    });
    const nextOrg = state.data.organizations[0] || null;
    state.session = nextOrg ? { ...state.session, activeOrgId: nextOrg.id } : null;
    saveData();
    saveSession();
    render();
  }

  function openForm(type, itemId) {
    if (type === "users" && !canManageUsers()) return;
    if (type !== "users" && !canEdit()) return;

    const item = itemId ? orgItems(type).find((entry) => entry.id === itemId) : null;
    state.editing = { type, itemId };
    const modal = document.querySelector("[data-modal]");
    const form = document.querySelector("[data-item-form]");
    document.querySelector("[data-modal-title]").textContent = `${item ? "Edit" : "Add"} ${singular(type)}`;
    form.innerHTML = `<div class="workspace-form-grid">${fieldSets[type].map((field) => renderField(field, item)).join("")}</div><button class="workspace-primary-button" type="submit">${item ? "Save changes" : "Create"}</button>`;
    form.onsubmit = handleItemSubmit;
    modal.classList.remove("is-hidden");
    modal.setAttribute("aria-hidden", "false");
  }

  function renderField([name, label, kind, required, options], item) {
    const value = item?.[name] || "";
    const wide = kind === "textarea" ? " is-wide" : "";
    const labelContent = renderFieldLabel(name, label);
    if (kind === "textarea") {
      return `<label class="${wide}">${labelContent}<textarea name="${name}" ${required ? "required" : ""}>${escapeHtml(value)}</textarea></label>`;
    }
    if (kind === "select") {
      return `<label>${labelContent}<select name="${name}" ${required ? "required" : ""}>${options.map((option) => `<option value="${escapeHtml(option)}" ${option === value ? "selected" : ""}>${escapeHtml(option)}</option>`).join("")}</select></label>`;
    }
    if (kind === "user") {
      const users = orgUsers();
      return `<label>${labelContent}<select name="${name}" ${required ? "required" : ""}>${users.map((user) => `<option value="${user.id}" ${user.id === value ? "selected" : ""}>${escapeHtml(user.name)} - ${escapeHtml(user.role)}</option>`).join("")}</select></label>`;
    }
    return `<label>${labelContent}<input name="${name}" type="${kind}" value="${escapeHtml(value)}" ${required ? "required" : ""}/></label>`;
  }

  function renderFieldLabel(name, label) {
    const help = helpText[name];
    const helpMarkup = help
      ? `<span class="workspace-help-wrap"><span class="workspace-help" tabindex="0" aria-label="${escapeHtml(help)}">?</span><span class="workspace-help-popover" role="tooltip">${escapeHtml(help)}</span></span>`
      : "";
    return `<span class="workspace-field-label">${escapeHtml(label)}${helpMarkup}</span>`;
  }

  function handleItemSubmit(event) {
    event.preventDefault();
    const { type, itemId } = state.editing;
    const form = new FormData(event.currentTarget);
    const payload = {};
    fieldSets[type].forEach(([name]) => {
      payload[name] = String(form.get(name) || "").trim();
    });

    if (type === "users") {
      const existing = state.data.users.find((user) => user.id === itemId);
      const emailTaken = state.data.users.some((user) => user.email.toLowerCase() === payload.email.toLowerCase() && user.id !== itemId);
      if (emailTaken) {
        alert("That email already has access.");
        return;
      }
      if (existing) {
        Object.assign(existing, payload);
      } else {
        state.data.users.push({ id: id("user"), orgId: activeOrg().id, ...payload });
      }
    } else {
      const collection = state.data[type];
      const existing = collection.find((entry) => entry.id === itemId);
      if (existing) {
        Object.assign(existing, payload);
      } else {
        collection.push({ id: id(type.slice(0, 3)), orgId: activeOrg().id, ...payload });
      }
    }

    saveData();
    closeModal();
    render();
  }

  function closeModal() {
    const modal = document.querySelector("[data-modal]");
    modal.classList.add("is-hidden");
    modal.setAttribute("aria-hidden", "true");
    state.editing = null;
  }

  function singular(type) {
    return {
      recommendations: "recommendation",
      metrics: "metric",
      decisions: "decision",
      dashboards: "dashboard",
      users: "user"
    }[type] || "item";
  }

  function renderReport() {
    const org = activeOrg();
    const recs = orgItems("recommendations");
    const metrics = orgItems("metrics");
    const decisions = orgItems("decisions");
    const dashboards = orgItems("dashboards");
    const openHigh = recs.filter((item) => item.priority === "High" && item.status !== "Done");
    const report = document.querySelector("[data-export-report]");
    report.innerHTML = `
      <p class="workspace-eyebrow">Decision System Reset</p>
      <h2>${escapeHtml(org.name)}</h2>
      <p class="workspace-muted">Generated from the Parallax Decision Workspace. Use this as the working artifact for leadership alignment, KPI ownership, dashboard cleanup, and 30/60/90-day execution.</p>
      <div class="workspace-report-section">
        <h3>Executive summary</h3>
        <ul>
          <li>${recs.filter((item) => item.status !== "Done").length} open recommendations require ownership or follow-through.</li>
          <li>${metrics.filter((item) => item.trust !== "Trusted").length} metrics need trust review, clearer definitions, or stronger ownership.</li>
          <li>${dashboards.filter((item) => item.action !== "Keep").length} dashboards should be fixed, merged, or retired.</li>
          <li>${decisions.length} recurring decisions have been mapped to owners, cadence, and supporting metrics.</li>
        </ul>
      </div>
      <div class="workspace-report-section">
        <h3>Priority recommendations</h3>
        ${listReportItems(openHigh, (item) => `${item.title} - Owner: ${userName(item.ownerId)} - Next: ${item.nextStep}`)}
      </div>
      <div class="workspace-report-section">
        <h3>Metric ownership map</h3>
        ${listReportItems(metrics, (item) => `${item.name} - Owner: ${userName(item.ownerId)} - Trust: ${item.trust} - Decision: ${item.decision}`)}
      </div>
      <div class="workspace-report-section">
        <h3>Dashboard cleanup plan</h3>
        ${listReportItems(dashboards, (item) => `${item.name} - ${item.platform || "Unknown source"} / ${item.location || "No location"} - Action: ${item.action} - Trust: ${item.trustScore}/5 - Owner: ${userName(item.ownerId)}${item.reportUrl ? ` - Link: ${item.reportUrl}` : ""}`)}
      </div>
      <div class="workspace-report-section">
        <h3>Decision map</h3>
        ${listReportItems(decisions, (item) => `${item.name} - Options: ${item.options || "Not defined"} - Criteria: ${item.criteria || "Not defined"} - Current option: ${item.selectedOption || "Not selected"} - Cadence: ${item.cadence} - Owner: ${userName(item.ownerId)} - Metrics: ${item.metrics}`)}
      </div>`;
  }

  function listReportItems(items, mapItem) {
    if (!items.length) return `<p class="workspace-muted">No items yet.</p>`;
    return `<ul>${items.map((item) => `<li>${escapeHtml(mapItem(item))}</li>`).join("")}</ul>`;
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  boot();
})();

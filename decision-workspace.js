(function () {
  const stepOrder = ["decisions", "metrics", "cadence", "triggers", "ownership"];
  const stepLabels = {
    decisions: "Decision inventory",
    metrics: "Metric-to-decision mapping",
    cadence: "Operating cadence",
    triggers: "Trigger and action rules",
    ownership: "Ownership and escalation"
  };
  const weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  const fieldSets = {
    decisions: [
      ["decision", "Decision", "text", "Portfolio prioritization"],
      ["owner", "Owner", "text", "Head of Strategy"],
      ["frequency", "Frequency", "select", "Weekly", ["Weekly", "Monthly", "Quarterly", "Event-driven"]],
      ["pain", "Current friction", "textarea", "Decisions are made from different spreadsheets and late context."]
    ],
    metrics: [
      ["decision", "Decision supported", "text", "Portfolio prioritization"],
      ["signal", "Metric signal", "text", "ROIC, market growth, strategic fit"],
      ["source", "Source", "text", "Power BI executive scorecard"],
      ["confidence", "Confidence", "select", "Needs review", ["Trusted", "Needs review", "Disputed", "Unknown"]]
    ],
    cadence: [
      ["forum", "Forum or meeting", "text", "Weekly leadership review"],
      ["rhythm", "Rhythm", "select", "Weekly", ["Weekly", "Monthly", "Quarterly", "Event-driven"]],
      ["days", "Review day(s)", "days", ""],
      ["time", "Review time", "time", "09:00"],
      ["decisions", "Decisions reviewed", "text", "Demand forecast, capacity rebalance"],
      ["commitment", "Required output", "textarea", "Decision, owner, next action, and escalation if blocked."]
    ],
    triggers: [
      ["signal", "Metric signal", "text", "Bookings delta"],
      ["threshold", "Threshold", "text", "Below -10% quarter over quarter"],
      ["action", "Action", "text", "Adjust forecast and review pipeline coverage"],
      ["owner", "Response owner", "text", "VP Commercial"]
    ],
    ownership: [
      ["decisionOwner", "Decision owner", "text", "VP Commercial"],
      ["escalateTo", "Escalate to", "text", "COO"],
      ["timeline", "Response timeline", "select", "Within 5 business days", ["Same day", "Within 48 hours", "Within 5 business days", "Next review cycle"]],
      ["rule", "Escalation rule", "textarea", "Escalate when the owner cannot resolve the action before the next cadence review."]
    ]
  };

  const artifactColumns = {
    decisions: ["decision", "owner", "frequency", "pain"],
    metrics: ["decision", "signal", "source", "confidence"],
    cadence: ["forum", "rhythm", "days", "time", "decisions", "commitment"],
    triggers: ["signal", "threshold", "action", "owner"],
    ownership: ["decisionOwner", "escalateTo", "timeline", "rule"]
  };

  const labels = Object.fromEntries(
    Object.values(fieldSets).flat().map(([name, label]) => [name, label])
  );

  const sampleData = {
    decisions: [
      { decision: "Portfolio prioritization", owner: "Head of Strategy", frequency: "Monthly", pain: "Investment tradeoffs are debated without a common view of return, capacity, and strategic fit." },
      { decision: "Demand forecast commit", owner: "VP Commercial", frequency: "Weekly", pain: "Forecast updates are made after leaders argue about pipeline coverage and win-rate assumptions." },
      { decision: "Pricing adjustment", owner: "VP Pricing", frequency: "Event-driven", pain: "Price moves are delayed because leaders disagree on margin, elasticity, and customer risk." },
      { decision: "Operating expense reallocation", owner: "CFO", frequency: "Monthly", pain: "Budget decisions lag because the team cannot distinguish run-rate noise from structural variance." },
      { decision: "Capacity rebalance", owner: "COO", frequency: "Weekly", pain: "Staffing and vendor capacity are adjusted after service levels already miss target." }
    ],
    metrics: [
      { decision: "Portfolio prioritization", signal: "ROIC, market growth, strategic fit", source: "Executive scorecard", confidence: "Needs review" },
      { decision: "Demand forecast commit", signal: "Bookings delta, pipeline coverage, win rate", source: "CRM and finance model", confidence: "Disputed" },
      { decision: "Pricing adjustment", signal: "ASP delta, price index, elasticity", source: "Revenue operations model", confidence: "Needs review" },
      { decision: "Operating expense reallocation", signal: "OpEx percent of revenue, cost to serve, efficiency index", source: "Finance planning model", confidence: "Trusted" },
      { decision: "Capacity rebalance", signal: "Utilization, lead time, backlog", source: "Operations dashboard", confidence: "Needs review" }
    ],
    cadence: [
      { forum: "Metric signal review", rhythm: "Weekly", days: ["Tuesday"], time: "08:30", decisions: "Demand forecast commit, capacity rebalance", commitment: "Review signal movement and identify decisions that need action." },
      { forum: "Decision review", rhythm: "Weekly", days: ["Tuesday"], time: "09:00", decisions: "Pricing adjustment, operating expense reallocation", commitment: "Choose action, owner, and next checkpoint for each triggered decision." },
      { forum: "Trigger assessment", rhythm: "Weekly", days: ["Thursday"], time: "09:30", decisions: "Threshold breaches and escalations", commitment: "Confirm whether thresholds require action or executive escalation." },
      { forum: "Action commitments", rhythm: "Weekly", days: ["Thursday"], time: "10:00", decisions: "Open actions from the reset artifact", commitment: "Close the loop on assigned actions before the next review." },
      { forum: "Risk and escalation review", rhythm: "Monthly", days: ["Friday"], time: "10:30", decisions: "Portfolio prioritization, roadmap trade-offs, vendor selection", commitment: "Escalate unresolved cross-functional decisions to the right owner." }
    ],
    triggers: [
      { signal: "Bookings delta", threshold: "Below -10% quarter over quarter", action: "Adjust forecast and review pipeline coverage", owner: "VP Commercial" },
      { signal: "ROIC", threshold: "Below 12%", action: "Rebalance portfolio", owner: "Head of Strategy" },
      { signal: "ASP delta", threshold: "Below -2%", action: "Review price adjustment", owner: "VP Pricing" },
      { signal: "OpEx percent of revenue", threshold: "Above 20%", action: "Reallocate budget", owner: "CFO" },
      { signal: "Utilization", threshold: "Below 70%", action: "Adjust capacity plan", owner: "COO" }
    ],
    ownership: [
      { decisionOwner: "VP Commercial", escalateTo: "COO", timeline: "Within 48 hours", rule: "Escalate when forecast risk cannot be resolved before weekly review." },
      { decisionOwner: "Head of Strategy", escalateTo: "CEO", timeline: "Within 5 business days", rule: "Escalate when portfolio tradeoffs affect budget, capacity, or strategic commitments." },
      { decisionOwner: "VP Pricing", escalateTo: "CRO", timeline: "Within 48 hours", rule: "Escalate when margin and volume signals point to conflicting pricing actions." },
      { decisionOwner: "CFO", escalateTo: "CEO", timeline: "Within 5 business days", rule: "Escalate when reallocation affects committed budget or operating targets." },
      { decisionOwner: "COO", escalateTo: "CEO", timeline: "Same day", rule: "Escalate when capacity risk threatens service level or customer commitments." }
    ]
  };

  const state = defaultState();
  const access = {
    unlocked: false,
    email: ""
  };

  function defaultState() {
    return Object.fromEntries(stepOrder.map((step) => [step, [emptyRow(step)]]));
  }

  function emptyRow(step) {
    return Object.fromEntries(fieldSets[step].map(([name, , type]) => [name, type === "days" ? [] : ""]));
  }

  function saveState() {
    return state;
  }

  function track(eventName, params) {
    if (typeof window.gtag === "function") {
      window.gtag("event", eventName, {
        event_category: "decision_workspace",
        ...params
      });
    }
  }

  function render() {
    stepOrder.forEach(renderRows);
    renderProgress();
    renderArtifact();
    renderArtifactAccess();
  }

  function renderRows(step) {
    const list = document.querySelector(`[data-row-list="${step}"]`);
    if (!list) return;
    list.innerHTML = "";
    state[step].forEach((row, index) => {
      const article = document.createElement("article");
      article.className = "workspace-diagnostic-row";
      article.innerHTML = `
        <div class="workspace-row-top">
          <strong>${stepLabels[step]} ${index + 1}</strong>
          ${state[step].length > 1 ? `<button class="workspace-remove-row" data-remove-row="${step}" data-row-index="${index}" type="button">Remove</button>` : ""}
        </div>
        <div class="workspace-field-grid"></div>
      `;
      const grid = article.querySelector(".workspace-field-grid");
      fieldSets[step].forEach(([name, label, type, placeholder, options]) => {
        const field = document.createElement("label");
        const isWide = type === "textarea" || type === "days";
        field.className = isWide ? "is-wide" : "";
        field.innerHTML = `${label}${renderInput(step, index, name, type, placeholder, options)}`;
        grid.appendChild(field);
      });
      list.appendChild(article);
    });
  }

  function renderInput(step, index, name, type, placeholder, options) {
    const value = escapeHtml(state[step][index][name] || "");
    const common = `data-field-step="${step}" data-field-index="${index}" data-field-name="${name}"`;
    if (type === "textarea") {
      return `<textarea ${common} placeholder="${escapeHtml(placeholder)}">${value}</textarea>`;
    }
    if (type === "select") {
      const choices = options.map((option) => {
        const selected = state[step][index][name] === option ? " selected" : "";
        return `<option value="${escapeHtml(option)}"${selected}>${escapeHtml(option)}</option>`;
      }).join("");
      return `<select ${common}><option value="">Select</option>${choices}</select>`;
    }
    if (type === "days") {
      const selectedDays = Array.isArray(state[step][index][name]) ? state[step][index][name] : [];
      return `
        <div class="workspace-day-picker" ${common}>
          ${weekDays.map((day) => `
            <label>
              <input type="checkbox" value="${escapeHtml(day)}"${selectedDays.includes(day) ? " checked" : ""}>
              <span>${escapeHtml(day.slice(0, 3))}</span>
            </label>
          `).join("")}
        </div>
      `;
    }
    return `<input ${common} type="${type}" placeholder="${escapeHtml(placeholder)}" value="${value}">`;
  }

  function renderProgress() {
    const allFields = stepOrder.flatMap((step) => state[step].flatMap((row) => Object.values(row)));
    const filled = allFields.filter((value) => Array.isArray(value) ? value.length : String(value || "").trim()).length;
    const percent = allFields.length ? Math.round((filled / allFields.length) * 100) : 0;
    const bar = document.querySelector("[data-progress-bar]");
    const label = document.querySelector("[data-progress-label]");
    if (bar) bar.style.width = `${percent}%`;
    if (label) label.textContent = `${percent}% complete`;
  }

  function renderArtifact() {
    const output = document.querySelector("[data-artifact-output]");
    if (!output) return;
    const counts = Object.fromEntries(stepOrder.map((step) => [
      step,
      state[step].filter((row) => Object.values(row).some((value) => Array.isArray(value) ? value.length : String(value || "").trim())).length
    ]));
    output.innerHTML = `
      <div class="workspace-artifact-titlebar">
        <span></span>
        <div>
          <strong>Decision System Reset Artifact</strong>
          <em>Align decisions. Act on signals. Drive outcomes.</em>
        </div>
        <span></span>
      </div>
      <div class="workspace-artifact-summary">
        <div><span>Decisions</span><strong>${counts.decisions}</strong></div>
        <div><span>Signals</span><strong>${counts.metrics}</strong></div>
        <div><span>Cadences</span><strong>${counts.cadence}</strong></div>
        <div><span>Action rules</span><strong>${counts.triggers + counts.ownership}</strong></div>
      </div>
      <div class="workspace-architecture-strip">
        <article><span>01</span><strong>Decision layer</strong><p>Names what leaders actually decide.</p></article>
        <article><span>02</span><strong>Signal layer</strong><p>Connects evidence to each decision.</p></article>
        <article><span>03</span><strong>Cadence layer</strong><p>Creates the review rhythm where action happens.</p></article>
        <article><span>04</span><strong>Action layer</strong><p>Turns thresholds into response rules.</p></article>
        <article><span>05</span><strong>Accountability layer</strong><p>Clarifies who owns the response and escalation.</p></article>
      </div>
      <div class="workspace-artifact-board">
        ${renderArtifactPanel("decisions", "1", "Decision inventory", "What decisions we make")}
        ${renderArtifactPanel("metrics", "2", "Metric-to-decision mapping", "What signals we watch")}
        ${renderArtifactPanel("cadence", "3", "Operating cadence", "When we review")}
        ${renderArtifactPanel("triggers", "4", "Trigger and action design", "What we do when signals hit")}
        ${renderArtifactPanel("ownership", "5", "Ownership and escalation", "Who acts and who escalates")}
      </div>
      ${renderDecisionFlow(counts)}
    `;
  }

  function renderArtifactPanel(step, number, title, purpose) {
    const rows = state[step].filter((row) => Object.values(row).some((value) => Array.isArray(value) ? value.length : String(value || "").trim()));
    if (!rows.length) {
      return `
        <section class="workspace-artifact-panel workspace-panel-${step}">
          <header><span>${number}</span><div><h3>${escapeHtml(title)}</h3><p>${escapeHtml(purpose)}</p></div></header>
          <p class="workspace-empty-note">Add at least one item to this section.</p>
        </section>
      `;
    }
    const limitedRows = rows.slice(0, 6);
    return `
      <section class="workspace-artifact-panel workspace-panel-${step}">
        <header><span>${number}</span><div><h3>${escapeHtml(title)}</h3><p>${escapeHtml(purpose)}</p></div></header>
        <div class="workspace-panel-body">
          ${limitedRows.map((row) => renderPanelRow(step, row)).join("")}
        </div>
        ${rows.length > limitedRows.length ? `<p class="workspace-panel-more">+${rows.length - limitedRows.length} more in worksheet</p>` : ""}
      </section>
    `;
  }

  function renderPanelRow(step, row) {
    if (step === "decisions") {
      return `
        <article class="workspace-board-row">
          <strong>${escapeHtml(row.decision || "Decision")}</strong>
          <span>${escapeHtml(row.owner || "Owner TBD")}</span>
          <em>${escapeHtml(row.frequency || "Cadence TBD")}</em>
          <p>${escapeHtml(row.pain || "Current friction not yet defined.")}</p>
        </article>
      `;
    }
    if (step === "metrics") {
      return `
        <article class="workspace-board-row">
          <strong>${escapeHtml(row.decision || "Decision")}</strong>
          <div class="workspace-signal-chips">${splitSignals(row.signal).map((signal) => `<span>${escapeHtml(signal)}</span>`).join("")}</div>
          <p>${escapeHtml(row.source || "Source TBD")} - ${escapeHtml(row.confidence || "Confidence TBD")}</p>
        </article>
      `;
    }
    if (step === "cadence") {
      return `
        <article class="workspace-board-row workspace-cadence-row">
          <strong>${escapeHtml(row.forum || "Review forum")}</strong>
          ${renderMiniTimeline(row.days)}
          <em>${escapeHtml(formatCadenceTime(row) || row.rhythm || "Schedule TBD")}</em>
          <p>${escapeHtml(row.commitment || row.decisions || "Required output not yet defined.")}</p>
        </article>
      `;
    }
    if (step === "triggers") {
      const escalation = findEscalationForOwner(row.owner);
      return `
        <article class="workspace-board-row workspace-trigger-row">
          <strong>${escapeHtml(row.signal || "Signal")}</strong>
          <span>${escapeHtml(row.threshold || "Threshold TBD")}</span>
          <b>${escapeHtml(row.action || "Action TBD")}</b>
          <p>${escapeHtml(row.owner || "Response owner TBD")}</p>
          <i class="workspace-section-link-arrow" aria-label="Maps to ${escapeHtml(escalation || "escalation owner")}"></i>
        </article>
      `;
    }
    return `
      <article class="workspace-board-row workspace-owner-row">
        <strong>${escapeHtml(row.decisionOwner || "Decision owner")}</strong>
        <span>Escalate to ${escapeHtml(row.escalateTo || "TBD")}</span>
        <em>${escapeHtml(row.timeline || "Timeline TBD")}</em>
        <p>${escapeHtml(row.rule || "Escalation rule not yet defined.")}</p>
      </article>
    `;
  }

  function renderDecisionFlow(counts) {
    const readiness = Math.min(100, Math.round(((counts.decisions + counts.metrics + counts.cadence + counts.triggers + counts.ownership) / 8) * 100));
    return `
      <div class="workspace-decision-flow">
        <section class="workspace-flow-lane" aria-label="Decision architecture flow">
          ${[
            ["Inventory", "What decisions we make"],
            ["Metrics", "What signals we watch"],
            ["Cadence", "When we review"],
            ["Triggers", "What happens when signal changes"],
            ["Ownership", "Who acts and escalates"],
            ["Better decisions", "Stronger outcomes"]
          ].map(([label, copy], index, arr) => `
            <article>
              <span aria-hidden="true"></span>
              <strong>${escapeHtml(label)}</strong>
              <p>${escapeHtml(copy)}</p>
            </article>
            ${index < arr.length - 1 ? "<i></i>" : ""}
          `).join("")}
        </section>
        <aside class="workspace-outcome-card">
          <span>Outcomes</span>
          <strong>${readiness}%</strong>
          <p>Draft completeness based on populated architecture layers.</p>
          <ul>
            <li>Faster decision cycles</li>
            <li>Aligned leadership signals</li>
            <li>Clearer escalation paths</li>
            <li>Reduced reporting debate</li>
          </ul>
        </aside>
      </div>
    `;
  }

  function splitSignals(value) {
    const signals = String(value || "").split(/[,;/]+/).map((item) => item.trim()).filter(Boolean);
    return signals.length ? signals.slice(0, 4) : ["Signal TBD"];
  }

  function setActiveStep(step) {
    document.querySelectorAll("[data-step-target]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.stepTarget === step);
    });
    document.querySelectorAll("[data-step-panel]").forEach((panel) => {
      panel.classList.toggle("is-hidden", panel.dataset.stepPanel !== step);
    });
    track("workspace_step_viewed", { step });
  }

  function addRow(step) {
    state[step].push(emptyRow(step));
    saveState();
    render();
    track("workspace_row_added", { step });
  }

  function removeRow(step, index) {
    state[step].splice(index, 1);
    if (!state[step].length) state[step].push(emptyRow(step));
    saveState();
    render();
  }

  function handleFieldChange(event) {
    const field = event.target.closest("[data-field-step]");
    if (!field) return;
    if (field.classList.contains("workspace-day-picker")) return;
    const { fieldStep, fieldIndex, fieldName } = field.dataset;
    state[fieldStep][Number(fieldIndex)][fieldName] = field.value;
    saveState();
    renderProgress();
    renderArtifact();
    track("workspace_field_changed", { step: fieldStep, field_name: fieldName });
  }

  function renderArtifactAccess() {
    const output = document.querySelector("[data-artifact-output]");
    const download = document.querySelector("[data-download-pdf]");
    const status = document.querySelector("[data-unlock-status]");
    const email = document.querySelector('[data-unlock-form] input[name="email"]');
    if (output) output.classList.toggle("is-locked", !access.unlocked);
    if (download) download.classList.toggle("is-hidden", !access.unlocked);
    if (email && !access.unlocked) email.value = "";
    if (status) {
      status.textContent = access.unlocked
        ? "Artifact unlocked. You can review it on page or download the PDF."
        : "Enter a work email to reveal the artifact preview.";
    }
  }

  function handleUnlockSubmit(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const formData = new FormData(form);
    access.email = String(formData.get("email") || "").trim();
    access.unlocked = Boolean(access.email);
    if (!access.unlocked) return;
    renderArtifactAccess();
    sendUnlockAlert();
    track("decision_workspace_artifact_unlocked", { ...summaryParams(), email_domain: access.email.split("@")[1] || "" });
  }

  function summaryParams() {
    return {
      decisions_count: filledRows("decisions"),
      metrics_count: filledRows("metrics"),
      cadence_count: filledRows("cadence"),
      triggers_count: filledRows("triggers"),
      ownership_count: filledRows("ownership")
    };
  }

  function filledRows(step) {
    return state[step].filter((row) => Object.values(row).some((value) => Array.isArray(value) ? value.length : String(value || "").trim())).length;
  }

  async function downloadArtifactPdf() {
    if (!access.unlocked) {
      document.querySelector('[data-unlock-form] input[name="email"]')?.focus();
      return;
    }
    const status = document.querySelector("[data-unlock-status]");
    if (status) status.textContent = "Preparing the visual PDF...";
    const blob = await createArtifactScreenshotPdfBlob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "decision-system-reset-artifact.pdf";
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    if (status) status.textContent = "Artifact unlocked. You can review it on page or download the PDF.";
    track("artifact_pdf_downloaded", summaryParams());
  }

  function sendUnlockAlert() {
    const form = document.querySelector("[data-unlock-alert-form]");
    if (!form) return;
    const summary = summaryParams();
    setHiddenFormValue(form, "Email", access.email);
    setHiddenFormValue(form, "Decisions", summary.decisions_count);
    setHiddenFormValue(form, "Metrics", summary.metrics_count);
    setHiddenFormValue(form, "Cadence", summary.cadence_count);
    setHiddenFormValue(form, "Triggers", summary.triggers_count);
    setHiddenFormValue(form, "Ownership", summary.ownership_count);
    try {
      form.submit();
    } catch (error) {
      track("decision_workspace_alert_failed", { reason: "form_submit_error" });
    }
  }

  function setHiddenFormValue(form, name, value) {
    const input = form.querySelector(`[name="${name}"]`);
    if (input) input.value = String(value ?? "");
  }

  function buildDownloadLines() {
    const lines = [
      "Decision System Reset Artifact",
      `Email: ${access.email || "-"}`,
      `Generated: ${new Date().toLocaleString()}`,
      "",
      "Use this as a working draft only. Do not treat sample-safe worksheet entries as a final operating model.",
      ""
    ];
    stepOrder.forEach((step) => {
      lines.push(stepLabels[step]);
      lines.push("-".repeat(stepLabels[step].length));
      const rows = state[step].filter((row) => Object.values(row).some((value) => Array.isArray(value) ? value.length : String(value || "").trim()));
      if (!rows.length) {
        lines.push("No entries yet.", "");
        return;
      }
      rows.forEach((row, index) => {
        lines.push(`${index + 1}.`);
        artifactColumns[step].forEach((column) => {
          lines.push(`   ${labels[column] || column}: ${formatDownloadValue(row[column])}`);
        });
      });
      lines.push("");
    });
    lines.push("Next step: https://parallaxdatalab.com/decision-system-reset/");
    return lines;
  }

  async function createArtifactScreenshotPdfBlob() {
    const artifact = document.querySelector("[data-artifact-output]");
    if (!artifact) {
      return createPdfBlob(buildDownloadLines());
    }
    const jpeg = await renderElementToJpeg(artifact);
    if (!jpeg) {
      return createPdfBlob(buildDownloadLines());
    }
    return createImagePdfBlob(jpeg.dataUrl, jpeg.width, jpeg.height);
  }

  async function renderElementToJpeg(element) {
    const width = Math.ceil(element.scrollWidth || element.getBoundingClientRect().width);
    const height = Math.ceil(element.scrollHeight || element.getBoundingClientRect().height);
    if (!width || !height) return null;

    const clone = element.cloneNode(true);
    clone.classList.remove("is-locked");
    clone.setAttribute("xmlns", "http://www.w3.org/1999/xhtml");
    inlineComputedStyles(element, clone);
    clone.style.width = `${width}px`;
    clone.style.minHeight = `${height}px`;
    clone.style.filter = "none";
    clone.style.opacity = "1";
    clone.style.background = "#071334";
    clone.style.padding = "24px";
    clone.style.boxSizing = "border-box";

    const serialized = new XMLSerializer().serializeToString(clone);
    const svg = `
      <svg xmlns="http://www.w3.org/2000/svg" width="${width + 48}" height="${height + 48}" viewBox="0 0 ${width + 48} ${height + 48}">
        <rect width="100%" height="100%" fill="#071334"/>
        <foreignObject x="0" y="0" width="${width + 48}" height="${height + 48}">${serialized}</foreignObject>
      </svg>
    `;
    const url = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
    const image = await loadImage(url).catch(() => null);
    if (!image) return null;

    const scale = Math.min(2, Math.max(1, 1800 / (width + 48)));
    const canvas = document.createElement("canvas");
    canvas.width = Math.round((width + 48) * scale);
    canvas.height = Math.round((height + 48) * scale);
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#071334";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
    return {
      dataUrl: canvas.toDataURL("image/jpeg", 0.92),
      width: canvas.width,
      height: canvas.height
    };
  }

  function inlineComputedStyles(source, target) {
    const computed = window.getComputedStyle(source);
    target.setAttribute("style", Array.from(computed).map((name) => `${name}:${computed.getPropertyValue(name)};`).join(""));
    const sourceChildren = Array.from(source.children);
    const targetChildren = Array.from(target.children);
    sourceChildren.forEach((child, index) => {
      if (targetChildren[index]) inlineComputedStyles(child, targetChildren[index]);
    });
  }

  function loadImage(src) {
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.onload = () => resolve(image);
      image.onerror = reject;
      image.src = src;
    });
  }

  function createImagePdfBlob(dataUrl, imageWidth, imageHeight) {
    const jpegBinary = atob(dataUrl.split(",")[1] || "");
    const jpegBytes = new Uint8Array(jpegBinary.length);
    for (let index = 0; index < jpegBinary.length; index += 1) {
      jpegBytes[index] = jpegBinary.charCodeAt(index);
    }
    const pageWidth = 792;
    const pageHeight = 612;
    const margin = 24;
    const fit = Math.min((pageWidth - margin * 2) / imageWidth, (pageHeight - margin * 2) / imageHeight);
    const drawWidth = Math.round(imageWidth * fit);
    const drawHeight = Math.round(imageHeight * fit);
    const x = Math.round((pageWidth - drawWidth) / 2);
    const y = Math.round((pageHeight - drawHeight) / 2);
    const content = `q\n${drawWidth} 0 0 ${drawHeight} ${x} ${y} cm\n/Im0 Do\nQ`;
    const objects = [
      "<< /Type /Catalog /Pages 2 0 R >>",
      "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
      `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pageWidth} ${pageHeight}] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>`,
      [
        `<< /Type /XObject /Subtype /Image /Width ${imageWidth} /Height ${imageHeight} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ${jpegBytes.length} >>\nstream\n`,
        jpegBytes,
        "\nendstream"
      ],
      `<< /Length ${content.length} >>\nstream\n${content}\nendstream`
    ];
    const encoder = new TextEncoder();
    const parts = [];
    let byteOffset = 0;
    const offsets = [0];
    addPdfPart("%PDF-1.4\n");
    objects.forEach((body, index) => {
      offsets.push(byteOffset);
      addPdfPart(`${index + 1} 0 obj\n`);
      if (Array.isArray(body)) {
        body.forEach(addPdfPart);
      } else {
        addPdfPart(body);
      }
      addPdfPart("\nendobj\n");
    });
    const xref = byteOffset;
    addPdfPart(`xref\n0 ${objects.length + 1}\n0000000000 65535 f \n`);
    offsets.slice(1).forEach((offset) => {
      addPdfPart(`${String(offset).padStart(10, "0")} 00000 n \n`);
    });
    addPdfPart(`trailer\n<< /Size ${objects.length + 1} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF`);
    return new Blob(parts, { type: "application/pdf" });

    function addPdfPart(part) {
      if (part instanceof Uint8Array) {
        parts.push(part);
        byteOffset += part.length;
        return;
      }
      const bytes = encoder.encode(String(part));
      parts.push(bytes);
      byteOffset += bytes.length;
    }
  }

  function loadSample() {
    stepOrder.forEach((step) => {
      state[step] = sampleData[step].map((row) => ({ ...emptyRow(step), ...row }));
    });
    saveState();
    render();
    setActiveStep("decisions");
    track("workspace_sample_loaded", summaryParams());
  }

  function renderMiniTimeline(days) {
    const selected = Array.isArray(days) ? days : [];
    return `
      <div class="workspace-mini-timeline">
        ${weekDays.slice(0, 5).map((day) => `<span class="${selected.includes(day) ? "is-active" : ""}">${escapeHtml(day.slice(0, 3))}</span>`).join("")}
      </div>
    `;
  }

  function formatCadenceTime(row) {
    const days = Array.isArray(row.days) && row.days.length ? row.days.map((day) => day.slice(0, 3)).join(", ") : "";
    return [days, row.time].filter(Boolean).join(" - ");
  }

  function formatDownloadValue(value) {
    if (Array.isArray(value)) return value.length ? value.join(", ") : "-";
    return value || "-";
  }

  function findEscalationForOwner(owner) {
    const normalized = String(owner || "").trim().toLowerCase();
    if (!normalized) return "";
    const match = state.ownership.find((row) => String(row.decisionOwner || "").trim().toLowerCase() === normalized);
    return match?.escalateTo || "";
  }

  function createPdfBlob(lines) {
    const pageWidth = 612;
    const pageHeight = 792;
    const marginX = 54;
    const topY = 738;
    const lineHeight = 14;
    const maxChars = 82;
    const pages = [];
    let current = [];
    let y = topY;

    lines.flatMap((line) => wrapPdfLine(line, maxChars)).forEach((line) => {
      if (y < 56) {
        pages.push(current);
        current = [];
        y = topY;
      }
      current.push({ text: line, y });
      y -= lineHeight;
    });
    if (current.length) pages.push(current);

    const objects = [
      "<< /Type /Catalog /Pages 2 0 R >>",
      "",
      "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
    ];
    const catalogId = 1;
    const pagesId = 2;
    const fontId = 3;
    const pageIds = [];
    pages.forEach((pageLines) => {
      const content = [
        "BT",
        "/F1 10 Tf",
        ...pageLines.map((line) => `1 0 0 1 ${marginX} ${line.y} Tm (${escapePdf(line.text)}) Tj`),
        "ET"
      ].join("\n");
      const contentId = addObject(`<< /Length ${content.length} >>\nstream\n${content}\nendstream`);
      const pageId = addObject(`<< /Type /Page /Parent ${pagesId} 0 R /MediaBox [0 0 ${pageWidth} ${pageHeight}] /Resources << /Font << /F1 ${fontId} 0 R >> >> /Contents ${contentId} 0 R >>`);
      pageIds.push(pageId);
    });
    objects[1] = `<< /Type /Pages /Kids [${pageIds.map((id) => `${id} 0 R`).join(" ")}] /Count ${pageIds.length} >>`;

    function addObject(body) {
      objects.push(body);
      return objects.length;
    }

    let pdf = "%PDF-1.4\n";
    const offsets = [0];
    objects.forEach((body, index) => {
      offsets.push(pdf.length);
      pdf += `${index + 1} 0 obj\n${body}\nendobj\n`;
    });
    const xref = pdf.length;
    pdf += `xref\n0 ${objects.length + 1}\n0000000000 65535 f \n`;
    offsets.slice(1).forEach((offset) => {
      pdf += `${String(offset).padStart(10, "0")} 00000 n \n`;
    });
    pdf += `trailer\n<< /Size ${objects.length + 1} /Root ${catalogId} 0 R >>\nstartxref\n${xref}\n%%EOF`;
    return new Blob([pdf], { type: "application/pdf" });
  }

  function wrapPdfLine(line, maxChars) {
    const words = String(line || "").split(/\s+/);
    const wrapped = [];
    let current = "";
    words.forEach((word) => {
      const next = current ? `${current} ${word}` : word;
      if (next.length > maxChars) {
        if (current) wrapped.push(current);
        current = word;
      } else {
        current = next;
      }
    });
    wrapped.push(current);
    return wrapped.length ? wrapped : [""];
  }

  function escapePdf(value) {
    return String(value).replace(/\\/g, "\\\\").replace(/\(/g, "\\(").replace(/\)/g, "\\)");
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  document.addEventListener("click", (event) => {
    const stepButton = event.target.closest("[data-step-target]");
    if (stepButton) setActiveStep(stepButton.dataset.stepTarget);

    const addButton = event.target.closest("[data-add-row]");
    if (addButton) addRow(addButton.dataset.addRow);

    const removeButton = event.target.closest("[data-remove-row]");
    if (removeButton) removeRow(removeButton.dataset.removeRow, Number(removeButton.dataset.rowIndex));

    if (event.target.closest("[data-load-sample]")) loadSample();
    if (event.target.closest("[data-download-pdf]")) downloadArtifactPdf();
  });

  document.addEventListener("input", handleFieldChange);
  document.addEventListener("change", (event) => {
    const picker = event.target.closest(".workspace-day-picker");
    if (!picker) return;
    const { fieldStep, fieldIndex, fieldName } = picker.dataset;
    state[fieldStep][Number(fieldIndex)][fieldName] = Array.from(picker.querySelectorAll("input:checked")).map((input) => input.value);
    saveState();
    renderProgress();
    renderArtifact();
    track("workspace_field_changed", { step: fieldStep, field_name: fieldName });
  });
  document.querySelector("[data-unlock-form]")?.addEventListener("submit", handleUnlockSubmit);

  render();
  track("workspace_started", summaryParams());
})();

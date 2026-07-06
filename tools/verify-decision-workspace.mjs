import { createRequire } from "node:module";
import { stat } from "node:fs/promises";

const require = createRequire(import.meta.url);
const { chromium } = require("C:/Users/700001256/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/.pnpm/playwright-core@1.61.1/node_modules/playwright-core");

const baseUrl = process.argv[2] || "http://127.0.0.1:8123/decision-workspace.html";
const viewports = [
  { name: "desktop", width: 1440, height: 1100 },
  { name: "mobile", width: 390, height: 920 }
];

const browser = await chromium.launch({ channel: "chrome" });
const issues = [];

for (const viewport of viewports) {
  const context = await browser.newContext({ viewport, acceptDownloads: true });
  await context.addInitScript(() => {
    window.__decisionWorkspaceCls = 0;
    new PerformanceObserver((entryList) => {
      for (const entry of entryList.getEntries()) {
        if (!entry.hadRecentInput) window.__decisionWorkspaceCls += entry.value;
      }
    }).observe({ type: "layout-shift", buffered: true });
  });
  const page = await context.newPage();
  const consoleErrors = [];
  page.on("console", (message) => {
    if (message.type() === "error" && !/Failed to load resource: net::ERR_/.test(message.text())) {
      consoleErrors.push(message.text());
    }
  });

  await page.goto(baseUrl, { waitUntil: "domcontentloaded" });
  await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
  await page.evaluate(() => {
    localStorage.removeItem("parallaxDecisionWorkspace.artifactUnlocked.v1");
    localStorage.removeItem("parallaxDecisionWorkspace.unlockEmail.v1");
    localStorage.removeItem("parallaxDecisionWorkspace.diagnostic.v3");
    localStorage.removeItem("parallaxDecisionWorkspace.diagnostic.v4");
    localStorage.removeItem("parallaxDecisionWorkspace.diagnostic.v5");
  });
  await page.reload({ waitUntil: "domcontentloaded" });
  await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
  await page.waitForTimeout(500);
  const cls = await page.evaluate(() => window.__decisionWorkspaceCls || 0);
  if (cls > 0.1) issues.push(`${viewport.name}: CLS above target (${cls.toFixed(3)})`);

  const bodyText = await page.locator("body").innerText();
  if (/\b(Log in|Sign up|Password|Supabase|reCAPTCHA)\b/i.test(bodyText)) {
    issues.push(`${viewport.name}: auth copy still visible`);
  }

  const heroLoaded = await page.locator(".workspace-artifact-frame img").evaluate((img) => img.complete && img.naturalWidth > 0);
  if (!heroLoaded) issues.push(`${viewport.name}: artifact preview image did not load`);

  const overflow = await page.evaluate(() => {
    const doc = document.documentElement;
    return Math.max(doc.scrollWidth, document.body.scrollWidth) - window.innerWidth;
  });
  if (overflow > 2) issues.push(`${viewport.name}: horizontal overflow ${overflow}px`);

  const initialEmail = await page.locator('input[name="email"]').inputValue();
  if (initialEmail) issues.push(`${viewport.name}: unlock email was prefilled on fresh load`);

  await page.locator("[data-load-sample]").click();
  const summaryCounts = await page.locator(".workspace-artifact-summary strong").evaluateAll((nodes) => nodes.map((node) => Number(node.textContent || 0)));
  if (summaryCounts[0] !== 5 || summaryCounts[1] !== 5 || summaryCounts[2] !== 5 || summaryCounts[3] !== 10) {
    issues.push(`${viewport.name}: sample draft counts were not 5/5/5/10; got ${summaryCounts.join("/")}`);
  }
  const oldEscalationMapRows = await page.locator(".workspace-action-escalation-map article").count();
  if (oldEscalationMapRows) issues.push(`${viewport.name}: old bottom action-to-escalation map is still rendering`);
  const sectionLinkArrows = await page.locator(".workspace-panel-triggers .workspace-section-link-arrow").count();
  if (sectionLinkArrows !== 5) issues.push(`${viewport.name}: section 4 rows did not render five arrows toward section 5`);

  const locked = await page.locator("[data-artifact-output]").evaluate((node) => node.classList.contains("is-locked"));
  if (!locked) issues.push(`${viewport.name}: artifact was not locked before email`);
  await page.locator('input[name="email"]').fill("test@example.com");
  await page.locator("[data-unlock-form] .workspace-primary-button").click();
  const unlocked = await page.locator("[data-artifact-output]").evaluate((node) => !node.classList.contains("is-locked"));
  if (!unlocked) issues.push(`${viewport.name}: artifact did not unlock after email`);
  const alertEmail = await page.locator('[data-unlock-alert-form] input[name="Email"]').inputValue();
  if (alertEmail !== "test@example.com") issues.push(`${viewport.name}: unlock alert form was not populated with the email`);

  const downloadPromise = page.waitForEvent("download", { timeout: 10000 });
  await page.locator("[data-download-pdf]").click();
  const download = await downloadPromise.catch(() => null);
  if (!download) {
    issues.push(`${viewport.name}: PDF download did not create a file`);
  } else if (!download.suggestedFilename().endsWith(".pdf")) {
    issues.push(`${viewport.name}: download was not a PDF`);
  } else {
    const failure = await download.failure();
    if (failure) issues.push(`${viewport.name}: PDF download failed: ${failure}`);
    const path = await download.path();
    if (path) {
      const file = await stat(path);
      if (file.size < 50000) issues.push(`${viewport.name}: PDF appears too small to contain a visual screenshot (${file.size} bytes)`);
    }
  }

  if (consoleErrors.length) {
    issues.push(`${viewport.name}: console errors: ${consoleErrors.slice(0, 3).join(" | ")}`);
  }

  await context.close();
}

await browser.close();

if (issues.length) {
  console.log("Decision workspace verification failed:");
  for (const issue of issues) console.log(`- ${issue}`);
  process.exit(1);
}

console.log("Decision workspace verification passed.");

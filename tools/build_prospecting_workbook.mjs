import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const outputDir = path.join(root, "outputs", "prospecting");
const outputPath = path.join(outputDir, "parallax_best_100_outreach_targets_tomorrow.xlsx");

const sourceUrls = {
  greaterCincinnati: "https://en.wikipedia.org/wiki/List_of_companies_in_Greater_Cincinnati",
  cincinnatiEmployers: "https://en.wikipedia.org/wiki/Cincinnati",
  ohioFortune: "https://www.axios.com/local/cleveland/2025/06/03/28-ohio-companies-make-2025-fortune-500-list",
  dayton: "https://en.wikipedia.org/wiki/Dayton,_Ohio",
  daytonMetro: "https://en.wikipedia.org/wiki/Dayton_metropolitan_area",
  centralOhio: "https://en.wikipedia.org/wiki/List_of_largest_Central_Ohio_employers",
  louisville: "https://en.wikipedia.org/wiki/List_of_major_employers_in_Louisville,_Kentucky",
  indiana: "https://en.wikipedia.org/wiki/Indiana",
  fortune500: "https://en.wikipedia.org/wiki/Fortune_500",
};

const prospects = [
  ["Kroger", "Cincinnati, OH", "Retail / Grocery", "Enterprise", 97, "High", "Email + LinkedIn + phone follow-up", "No", "VP/Director Analytics, BI, Finance Ops, Merchandising Ops", "Retail creates constant KPI, margin, store ops, inventory, and category reporting friction.", "Lead with dashboard trust, metric ownership, and category/operations reporting cleanup.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["Procter & Gamble", "Cincinnati, OH", "Consumer Goods", "Enterprise", 96, "High", "Warm intro or email + LinkedIn; phone only after signal", "No", "Analytics Director, Brand Finance, Supply Chain Analytics", "Global brands and functions create complex reporting, governance, and decision cadence needs.", "Lead with governed KPI definitions and executive reporting cadence, not generic dashboard building.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["GE Aerospace", "Evendale/Cincinnati, OH", "Aerospace / Manufacturing", "Enterprise", 95, "High", "Email + LinkedIn; pursue referral through local network", "No", "Operations Analytics, Supply Chain, Finance Transformation", "Aerospace operations require traceable, trusted metrics across supply chain, engineering, and finance.", "Lead with reporting reliability, operating signal, and decision-system language.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["Total Quality Logistics", "Union Township/Cincinnati, OH", "Logistics", "Large private", 94, "High", "Phone-first to ops/analytics + email follow-up", "Maybe, after prior touch", "VP Operations, Sales Ops, BI Leader", "Brokerage and logistics teams rely on fast operational metrics, margin signals, and exception reporting.", "Offer a 15-minute reporting friction review around lane, margin, carrier, and sales dashboards.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["Fifth Third Bank", "Cincinnati, OH", "Banking", "Enterprise", 93, "High", "Email + LinkedIn; compliance-aware messaging", "No", "BI Governance, Risk Analytics, Finance Ops", "Banking has high reporting scrutiny, ownership complexity, and regulatory sensitivity.", "Lead with governance, certified metrics, and decision auditability.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["Cintas", "Mason, OH", "Business Services", "Enterprise", 92, "High", "Email + LinkedIn + phone follow-up", "No", "Operations Analytics, Service Ops, Finance", "Route density, service performance, customer operations, and branch reporting are analytics-heavy.", "Lead with operational scorecards and metric consistency across branches.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["Western & Southern Financial Group", "Cincinnati, OH", "Insurance / Financial Services", "Enterprise", 91, "High", "Email + LinkedIn; referral preferred", "No", "Finance Analytics, Insurance Ops, Data Governance", "Financial services firms need trusted definitions, risk reporting, and executive KPI governance.", "Lead with dashboard trust and source-to-decision traceability.", "Week 1 - Day 1", sourceUrls.greaterCincinnati],
  ["Cincinnati Children's Hospital Medical Center", "Cincinnati, OH", "Healthcare", "Enterprise", 90, "High", "Warm intro + email; avoid cold doorstep", "No", "Strategy Analytics, Clinical Ops Analytics, Finance Analytics", "Large health systems carry major reporting, throughput, quality, and finance analytics complexity.", "Lead with decision-ready operating metrics; be careful not to imply clinical advice.", "Week 1 - Day 2", sourceUrls.cincinnatiEmployers],
  ["TriHealth", "Cincinnati, OH", "Healthcare", "Enterprise", 89, "High", "Warm intro + email + phone to admin office", "No", "Operational Excellence, Finance Analytics, BI Director", "Health system operations need trusted definitions across service lines, access, throughput, and finance.", "Lead with reporting trust and operational cadence for leadership reviews.", "Week 1 - Day 2", sourceUrls.cincinnatiEmployers],
  ["Bon Secours Mercy Health", "Cincinnati, OH", "Healthcare", "Enterprise", 88, "High", "Warm intro + email; procurement-aware", "No", "Enterprise Analytics, Finance Transformation, Ops Analytics", "Large multi-market healthcare operations create dashboard sprawl and metric governance needs.", "Lead with governance and executive reporting clarity.", "Week 1 - Day 2", sourceUrls.ohioFortune],
  ["St. Elizabeth Healthcare", "Edgewood, KY", "Healthcare", "Large regional", 87, "High", "Email + phone to business/analytics admin", "No", "Analytics, Strategy, Finance Ops", "Regional health network with cross-site operational and finance reporting needs.", "Lead with KPI ownership and operational signal reliability.", "Week 1 - Day 2", sourceUrls.cincinnatiEmployers],
  ["Medpace", "Cincinnati, OH", "Clinical Research", "Large public", 87, "High", "Email + LinkedIn to analytics/operations", "No", "Clinical Ops Analytics, Finance, Business Operations", "Clinical trials operations are process-heavy and reporting dependent.", "Lead with operational intelligence, exception reporting, and decision cadence.", "Week 1 - Day 2", sourceUrls.greaterCincinnati],
  ["Paycor", "Cincinnati, OH", "HR Software", "Large public", 86, "High", "Email + LinkedIn", "No", "RevOps, Customer Ops Analytics, Finance Analytics", "SaaS companies need revenue, retention, customer health, and operational reporting alignment.", "Lead with customer health and revenue operations KPI consistency.", "Week 1 - Day 2", sourceUrls.greaterCincinnati],
  ["First Financial Bank", "Cincinnati, OH", "Banking", "Large regional", 86, "High", "Email + LinkedIn + phone follow-up", "No", "BI, Risk Analytics, Commercial Banking Ops", "Regional banking has reporting governance needs without Fortune 50 procurement friction.", "Lead with practical certified metrics and management reporting cleanup.", "Week 1 - Day 2", sourceUrls.greaterCincinnati],
  ["American Financial Group", "Cincinnati, OH", "Insurance", "Enterprise", 85, "High", "Email + LinkedIn; referral preferred", "No", "Finance Analytics, Claims Analytics, BI Governance", "Insurance operations produce complex claims, underwriting, finance, and risk reporting.", "Lead with metric governance and executive dashboard trust.", "Week 1 - Day 3", sourceUrls.greaterCincinnati],
  ["Cincinnati Financial", "Fairfield, OH", "Insurance", "Enterprise", 85, "High", "Email + LinkedIn; referral preferred", "No", "Claims Analytics, Finance, Underwriting Ops", "Insurance reporting depends on consistent definitions, traceable sources, and governance.", "Lead with source reliability and dashboard trust scorecard.", "Week 1 - Day 3", sourceUrls.greaterCincinnati],
  ["altafiber", "Cincinnati, OH", "Telecom", "Large regional", 84, "High", "Phone + email to operations/BI", "Maybe, after prior touch", "Operations Analytics, Customer Ops, Network Ops", "Telecom has customer, field service, network, and churn reporting needs.", "Lead with operational dashboard cleanup and signal quality.", "Week 1 - Day 3", sourceUrls.greaterCincinnati],
  ["Gorilla Glue", "Sharonville, OH", "Consumer Products", "Mid-market private", 84, "High", "Phone-first + email; respectful HQ leave-behind possible", "Yes, only as leave-behind", "Operations, Finance, Sales Analytics", "Growing consumer-products firms often outgrow spreadsheet-heavy reporting.", "Lead with sales, inventory, and leadership KPI cleanup.", "Week 1 - Day 3", sourceUrls.greaterCincinnati],
  ["Kao USA", "Cincinnati, OH", "Consumer Products", "Large regional", 83, "High", "Email + LinkedIn to finance/ops/brand analytics", "No", "Brand Analytics, Finance, Supply Chain", "Multi-brand consumer businesses need consistent commercial and operations metrics.", "Lead with business-facing metric definitions and performance reporting.", "Week 1 - Day 3", sourceUrls.greaterCincinnati],
  ["LSI Industries", "Cincinnati, OH", "Manufacturing", "Mid-market public", 83, "High", "Phone + email to operations/finance", "Maybe, after prior touch", "COO, Finance, Operations Analytics", "Manufacturer with operational, sales, and production visibility needs.", "Lead with KPI reporting and manufacturing operating cadence.", "Week 1 - Day 3", sourceUrls.greaterCincinnati],
  ["Standard Textile", "Cincinnati, OH", "Manufacturing / Healthcare Textiles", "Mid-market private", 82, "High", "Phone + email", "Maybe, after prior touch", "Operations, Supply Chain, Finance", "Complex supply chain and healthcare customer base create reporting friction.", "Lead with supply chain, inventory, and customer profitability metrics.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Michelman", "Cincinnati, OH", "Specialty Chemicals", "Mid-market private", 82, "High", "Email + phone to operations/finance", "Maybe, after prior touch", "Operations, Supply Chain, Finance Analytics", "Specialty manufacturing depends on product, customer, plant, and margin reporting.", "Lead with trusted KPI definitions across operations and commercial teams.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["The Hillman Group", "Cincinnati, OH", "Hardware / Distribution", "Large public", 82, "High", "Email + LinkedIn + phone", "No", "Sales Ops, Supply Chain, Finance", "Distribution and retail programs create reporting complexity across SKUs, customers, and replenishment.", "Lead with inventory, margin, and customer reporting trust.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Meridian Bioscience", "Cincinnati, OH", "Life Sciences", "Mid-market", 81, "High", "Email + LinkedIn", "No", "Operations Analytics, Quality, Finance", "Life sciences operations require traceable reporting and strong process discipline.", "Lead with operational reporting cleanup and decision traceability.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["CTI Clinical Trial & Consulting", "Covington, KY", "Clinical Research", "Mid-market private", 81, "High", "Email + phone", "Maybe, after prior touch", "Clinical Ops, Finance, BI", "Clinical research organizations rely on process, pipeline, and project reporting.", "Lead with project portfolio and operating signal dashboards.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Ensemble Health Partners", "Cincinnati, OH", "Revenue Cycle / Healthcare", "Large private", 81, "High", "Email + LinkedIn", "No", "Revenue Cycle Analytics, Operations, Finance", "Revenue cycle operations are KPI-heavy and management-reporting intensive.", "Lead with operational scorecards and exception reporting.", "Week 2 - Priority", sourceUrls.cincinnatiEmployers],
  ["PatientPoint", "Cincinnati, OH", "Healthcare Media / Tech", "Mid-market", 80, "Medium", "Email + LinkedIn", "No", "Customer Ops, Revenue Ops, Finance", "Healthcare media and tech businesses need revenue, customer, and operations reporting.", "Lead with revenue/customer-health metric alignment.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Divisions Maintenance Group", "Newport, KY", "Facilities Services", "Mid-market private", 80, "Medium", "Phone-first + email", "Maybe, after prior touch", "Operations, Client Success, Finance", "Facilities services create field operations and customer performance reporting needs.", "Lead with operational intelligence and exception visibility.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Castellini Group", "Cincinnati, OH", "Food Distribution", "Mid-market private", 80, "Medium", "Phone-first + email; in-person leave-behind possible", "Yes, after prior touch", "Operations, Logistics, Finance", "Perishable distribution depends on timely inventory, margin, and logistics reporting.", "Lead with operational reporting and margin visibility.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["United Dairy Farmers", "Cincinnati, OH", "Retail / Food", "Mid-market private", 79, "Medium", "Phone-first + email; in-person leave-behind possible", "Yes, after prior touch", "Operations, Finance, Category Management", "Convenience retail and food operations need store, category, and labor reporting.", "Lead with store performance and KPI trust.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Tire Discounters", "Cincinnati, OH", "Retail / Automotive Services", "Mid-market private", 79, "Medium", "Phone-first + email", "Maybe, after prior touch", "Operations, Finance, Store Ops", "Multi-location service retailers need trusted store and service metrics.", "Lead with location scorecards and operating cadence.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Roto-Rooter", "Cincinnati, OH", "Field Services", "Large private", 79, "Medium", "Phone + email to operations", "Maybe, after prior touch", "Operations, Dispatch, Finance", "Field service has dispatch, technician productivity, and customer response metrics.", "Lead with operational dashboards and reporting automation.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Graeter's Ice Cream", "Cincinnati, OH", "Food / Retail", "Mid-market private", 78, "Medium", "Phone-first + concise email; leave-behind possible", "Yes, after prior touch", "Operations, Retail, Finance", "Growing retail and wholesale food operations need sales, inventory, and store reporting.", "Lead with practical KPI reporting and weekly business review support.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Skyline Chili", "Fairfield/Cincinnati, OH", "Restaurant / Food", "Mid-market private", 78, "Medium", "Phone-first + concise email; leave-behind possible", "Yes, after prior touch", "Operations, Finance, Franchise/Store Ops", "Restaurant groups need store-level labor, sales, margin, and franchise reporting.", "Lead with store scorecards and metric definitions.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["LaRosa's Pizzeria", "Cincinnati, OH", "Restaurant / Food", "Mid-market private", 77, "Medium", "Phone-first + concise email; leave-behind possible", "Yes, after prior touch", "Operations, Finance, Store Ops", "Multi-unit restaurant operations create recurring reporting and labor/margin questions.", "Lead with weekly scorecards and reporting automation.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Perfetti Van Melle USA", "Erlanger, KY", "Consumer Goods", "Large regional", 77, "Medium", "Email + LinkedIn", "No", "Supply Chain, Finance, Sales Analytics", "Consumer goods operations need reliable commercial and supply chain reporting.", "Lead with customer/product profitability and metric governance.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Milacron / Hillenbrand", "Batavia/Cincinnati, OH", "Industrial Manufacturing", "Large public", 77, "Medium", "Email + phone to operations/finance", "No", "Operations, Finance, Supply Chain", "Industrial manufacturing has complex product, service, and operational reporting needs.", "Lead with manufacturing KPI governance and operating dashboards.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Mubea North America", "Florence, KY", "Automotive Manufacturing", "Large regional", 76, "Medium", "Phone + email", "Maybe, after prior touch", "Plant Operations, Continuous Improvement, Finance", "Automotive manufacturing is metrics-rich and reporting-reliability sensitive.", "Lead with plant KPI reporting and escalation triggers.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Feintool Cincinnati", "Cincinnati, OH", "Manufacturing", "Mid-market", 76, "Medium", "Phone + email", "Maybe, after prior touch", "Plant Manager, Operations, Finance", "Manufacturing plants often need clearer production, quality, and cost reporting.", "Lead with practical Power BI/KPI cleanup.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["OPW / Dover", "Hamilton, OH", "Industrial Manufacturing", "Large regional", 76, "Medium", "Email + phone", "No", "Operations, Finance, Supply Chain", "Industrial operations create product, customer, and service reporting demands.", "Lead with operational KPI standardization.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["AtriCure", "Mason, OH", "Medical Devices", "Mid-market public", 76, "Medium", "Email + LinkedIn", "No", "Commercial Ops, Finance, Operations Analytics", "Medical-device firms need sales, operations, quality, and leadership reporting.", "Lead with decision-ready commercial and operational dashboards.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Ethicon / Johnson & Johnson", "Cincinnati, OH", "Medical Devices", "Enterprise site", 75, "Medium", "Email + LinkedIn; referral preferred", "No", "Site Operations, Quality Analytics, Finance", "Regulated manufacturing and product operations depend on traceable metrics.", "Lead with local site reporting and decision cadence.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Rhinestahl", "Mason, OH", "Aerospace / Manufacturing", "Mid-market", 75, "Medium", "Phone + email", "Maybe, after prior touch", "Operations, Finance, Supply Chain", "Aerospace tooling and manufacturing benefit from project, quality, and delivery reporting.", "Lead with operational scorecards and reporting automation.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Clippard Instrument Laboratory", "Cincinnati, OH", "Industrial Manufacturing", "Mid-market private", 74, "Medium", "Phone-first + email; leave-behind possible", "Yes, after prior touch", "Operations, Sales Ops, Finance", "Industrial component manufacturers often have data spread across ERP, sales, and spreadsheets.", "Lead with KPI definitions and Power BI reporting cleanup.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Kinetic Vision", "Cincinnati, OH", "Engineering / Product Development", "Mid-market", 74, "Medium", "Email + LinkedIn", "Maybe, after prior touch", "Operations, Project Management, Finance", "Project-based engineering firms need utilization, pipeline, and delivery reporting.", "Lead with project and resource visibility dashboards.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Belcan", "Cincinnati, OH", "Engineering Services", "Large private", 74, "Medium", "Email + LinkedIn; phone follow-up", "No", "Operations, Finance, Delivery Analytics", "Engineering services firms have utilization, project, and client profitability reporting needs.", "Lead with operational reporting and decision cadence.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["Empower Media", "Cincinnati, OH", "Marketing / Media", "Mid-market", 73, "Medium", "Email + LinkedIn", "Maybe, after prior touch", "Operations, Client Reporting, Finance", "Agencies manage client performance, margin, utilization, and recurring reporting.", "Lead with client reporting automation and metric clarity.", "Week 2 - Priority", sourceUrls.greaterCincinnati],
  ["dunnhumby USA", "Cincinnati, OH", "Retail Analytics", "Large analytics firm", 72, "Medium", "Email + LinkedIn; partnership angle", "No", "Operations, Commercial Analytics Leadership", "Analytics-led company may have mature capability but possible partnership or overflow needs.", "Lead with partnership support around decision-system implementation.", "Week 2 - Opportunistic", sourceUrls.greaterCincinnati],
  ["84.51°", "Cincinnati, OH", "Retail Analytics", "Large analytics firm", 72, "Medium", "Email + LinkedIn; partnership angle", "No", "Client Analytics, Product Ops", "Strong analytics maturity means lower need, but partnership/referral potential is high.", "Lead with implementation support, governance, and operating rhythm.", "Week 2 - Opportunistic", sourceUrls.greaterCincinnati],
  ["UC Health", "Cincinnati, OH", "Healthcare", "Large regional", 72, "Medium", "Warm intro + email", "No", "Strategy, Finance Analytics, Operations", "Academic health systems have complex reporting and decision pathways.", "Lead with leadership reporting clarity and metric ownership.", "Week 2 - Opportunistic", sourceUrls.cincinnatiEmployers],
  ["University of Cincinnati", "Cincinnati, OH", "Higher Education", "Large institution", 70, "Medium", "Warm intro + email; target admin units", "No", "Institutional Research, Finance, Operations", "Large universities have departmental reporting sprawl and leadership dashboards.", "Lead with admin reporting cleanup, not academic analytics.", "Week 2 - Opportunistic", sourceUrls.cincinnatiEmployers],
  ["CareSource", "Dayton, OH", "Health Insurance", "Large nonprofit", 86, "High", "Email + LinkedIn + phone", "No", "Analytics, Operations, Quality, Finance", "Managed care operations are KPI-heavy with compliance and operational reporting needs.", "Lead with metric governance and operational scorecards.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Premier Health", "Dayton, OH", "Healthcare", "Large regional", 84, "High", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Regional health system with large operational reporting needs.", "Lead with trusted operating metrics and leadership cadence.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Kettering Health", "Dayton, OH", "Healthcare", "Large regional", 84, "High", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Large health network with cross-site reporting and quality/finance visibility needs.", "Lead with KPI governance and operational reporting.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Reynolds and Reynolds", "Dayton, OH", "Automotive Software", "Large private", 82, "High", "Email + LinkedIn + phone", "No", "Customer Ops, Product Ops, Finance", "Automotive software firms need customer, product, revenue, and support reporting.", "Lead with customer health and operational reporting cleanup.", "Week 3 - Dayton", sourceUrls.dayton],
  ["LexisNexis Risk Solutions", "Miamisburg/Dayton, OH", "Data / Risk Analytics", "Enterprise site", 80, "Medium", "Email + LinkedIn; partnership angle", "No", "Operations, Product Analytics, Finance", "Data-heavy firm may be mature but has complex product and operations reporting.", "Lead with implementation/governance support rather than basic BI.", "Week 3 - Dayton", sourceUrls.daytonMetro],
  ["STRATACACHE", "Dayton, OH", "Digital Signage / Technology", "Mid-market private", 80, "Medium", "Email + phone", "Maybe, after prior touch", "Operations, Sales Ops, Finance", "Hardware/software operations create inventory, customer, deployment, and support reporting needs.", "Lead with operating dashboards and customer deployment metrics.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Winsupply", "Dayton, OH", "Wholesale Distribution", "Large private", 80, "Medium", "Email + phone", "Maybe, after prior touch", "Operations, Finance, Branch Analytics", "Distributor/branch model creates rich KPI and reporting standardization needs.", "Lead with branch scorecards and certified operating metrics.", "Week 3 - Dayton", sourceUrls.dayton],
  ["AES Ohio", "Dayton, OH", "Utilities", "Large regional", 78, "Medium", "Email + LinkedIn; regulated industry tone", "No", "Operations Analytics, Customer Ops, Finance", "Utilities need operational, customer, outage, and finance reporting clarity.", "Lead with operational decision cadence and source reliability.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Yaskawa Motoman", "Miamisburg, OH", "Robotics / Manufacturing", "Large regional", 78, "Medium", "Phone + email", "Maybe, after prior touch", "Operations, Sales Engineering, Finance", "Robotics/manufacturing firms need sales, project, service, and production reporting.", "Lead with project and operations scorecards.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Dayton Superior", "Miamisburg, OH", "Construction Products", "Mid-market", 76, "Medium", "Phone + email", "Maybe, after prior touch", "Operations, Sales Ops, Finance", "Construction-products firms need sales, inventory, and operational margin reporting.", "Lead with KPI reporting and Power BI cleanup.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Fuyao Glass America", "Moraine, OH", "Automotive Manufacturing", "Large regional", 76, "Medium", "Phone + email", "Maybe, after prior touch", "Plant Operations, Finance, Continuous Improvement", "Automotive manufacturing sites have strong daily/weekly operating metric needs.", "Lead with plant scorecards and escalation triggers.", "Week 3 - Dayton", sourceUrls.dayton],
  ["DPL / Dayton Power & Light operations", "Dayton, OH", "Utilities", "Large regional", 74, "Medium", "Email + LinkedIn", "No", "Operations Analytics, Finance", "Utilities and energy operations depend on reliable reporting and management dashboards.", "Lead with decision-ready operational reporting.", "Week 3 - Dayton", sourceUrls.dayton],
  ["Cardinal Health", "Dublin, OH", "Healthcare Distribution", "Enterprise", 89, "High", "Email + LinkedIn; referral preferred", "No", "Operations Analytics, Supply Chain, Finance", "Healthcare distribution is highly metric-driven across supply chain, customers, and finance.", "Lead with trusted operations reporting and governance.", "Week 4 - Columbus", sourceUrls.ohioFortune],
  ["Nationwide", "Columbus, OH", "Insurance / Financial Services", "Enterprise", 87, "High", "Email + LinkedIn; referral preferred", "No", "Claims Analytics, Finance, Data Governance", "Insurance operations create major reporting and governance demands.", "Lead with metric ownership and executive dashboard trust.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Huntington Bancshares", "Columbus, OH", "Banking", "Enterprise", 85, "High", "Email + LinkedIn; compliance-aware", "No", "Risk Analytics, Finance, BI Governance", "Regional banking operations create reporting standards and governance needs.", "Lead with certified metrics and management reporting.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["American Electric Power", "Columbus, OH", "Utilities", "Enterprise", 83, "High", "Email + LinkedIn", "No", "Operations Analytics, Finance, Regulatory Reporting", "Utilities have capital, operations, outage, and customer reporting complexity.", "Lead with operational scorecards and traceable reporting.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["DHL Supply Chain North America", "Westerville, OH", "Logistics", "Enterprise", 83, "High", "Email + LinkedIn + phone", "No", "Operations Analytics, Customer Reporting, Finance", "Logistics and warehousing require high-quality operational dashboards.", "Lead with customer and warehouse KPI reporting trust.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Bath & Body Works", "Columbus, OH", "Retail / Consumer", "Enterprise", 82, "High", "Email + LinkedIn", "No", "Store Ops Analytics, Merchandising, Finance", "Multi-store retail needs store, category, labor, and margin reporting.", "Lead with store scorecards and KPI governance.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Victoria's Secret & Co.", "Columbus, OH", "Retail / Consumer", "Enterprise", 82, "High", "Email + LinkedIn", "No", "Merchandising Analytics, Store Ops, Finance", "Retail operations depend on consistent commercial and store-performance reporting.", "Lead with decision-ready merchandising and store metrics.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Big Lots", "Columbus, OH", "Retail", "Enterprise", 81, "Medium", "Email + LinkedIn", "No", "Store Ops, Merchandising Analytics, Finance", "Retail turnarounds and operational shifts require trusted reporting.", "Lead with executive reporting and operational signal clarity.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Wendy's", "Dublin, OH", "Restaurant / Franchise", "Enterprise", 81, "High", "Email + LinkedIn", "No", "Franchise Analytics, Ops, Finance", "Franchise restaurant systems are rich in store, labor, sales, and performance reporting needs.", "Lead with franchise/store scorecards and operational cadence.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Worthington Enterprises", "Columbus, OH", "Manufacturing", "Large public", 80, "Medium", "Email + phone", "No", "Operations, Finance, Supply Chain", "Industrial manufacturing firms need plant, product, and margin reporting alignment.", "Lead with manufacturing KPI reporting and governance.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Scotts Miracle-Gro", "Marysville, OH", "Consumer Goods / Lawn & Garden", "Large public", 80, "Medium", "Email + LinkedIn", "No", "Sales Analytics, Supply Chain, Finance", "Seasonal consumer products create demand, inventory, and retailer reporting complexity.", "Lead with forecast, inventory, and commercial KPI trust.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Vertiv", "Columbus, OH", "Infrastructure / Manufacturing", "Enterprise", 80, "Medium", "Email + LinkedIn", "No", "Operations, Supply Chain, Finance", "Infrastructure manufacturing has complex global operations and service reporting.", "Lead with operational reporting and decision cadence.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Abercrombie & Fitch Co.", "New Albany, OH", "Retail / Apparel", "Large public", 79, "Medium", "Email + LinkedIn", "No", "Merchandising, Store Ops, Finance Analytics", "Apparel retail depends on product, channel, inventory, and store reporting.", "Lead with retail KPI definitions and executive dashboards.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Bread Financial", "Columbus, OH", "Financial Services", "Large public", 79, "Medium", "Email + LinkedIn", "No", "Risk Analytics, Finance, Customer Ops", "Financial-services operations need trusted risk, customer, and portfolio reporting.", "Lead with governance and reporting reliability.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["CoverMyMeds / McKesson", "Columbus, OH", "Healthcare Technology", "Enterprise site", 79, "Medium", "Email + LinkedIn", "No", "Operations Analytics, Product Ops, Finance", "Healthcare technology workflows create operational and customer reporting needs.", "Lead with customer operations and workflow KPI clarity.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Quantum Health", "Dublin, OH", "Healthcare Navigation", "Large private", 78, "Medium", "Email + LinkedIn", "No", "Operations Analytics, Client Reporting, Finance", "Healthcare navigation relies on service, client, and outcome reporting.", "Lead with client reporting and operating signal quality.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Safelite", "Columbus, OH", "Automotive Services", "Large private", 78, "Medium", "Email + phone", "No", "Field Ops, Customer Ops, Finance", "Field service and claims workflows create scheduling, service, and customer reporting needs.", "Lead with operational scorecards and exception reporting.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["NetJets", "Columbus, OH", "Aviation", "Large private", 78, "Medium", "Email + LinkedIn", "No", "Operations, Finance, Customer Ops", "Aviation operations require reliable utilization, customer, scheduling, and service reporting.", "Lead with operating cadence and reporting trust.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["OhioHealth", "Columbus, OH", "Healthcare", "Enterprise", 77, "Medium", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Large health systems need trusted cross-site metrics and leadership dashboards.", "Lead with operational decision reporting and governance.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Root Insurance", "Columbus, OH", "Insurance Technology", "Mid-market public", 76, "Medium", "Email + LinkedIn", "No", "Insurance Ops, Finance, Growth Analytics", "Insurtech firms need claims, customer, growth, and finance reporting alignment.", "Lead with metric ownership and revenue/claims dashboards.", "Week 4 - Columbus", sourceUrls.centralOhio],
  ["Humana", "Louisville, KY", "Health Insurance", "Enterprise", 88, "High", "Email + LinkedIn; referral preferred", "No", "Analytics, Medicare Ops, Finance, Quality", "Managed healthcare is one of the strongest fits for KPI governance and operational reporting.", "Lead with trusted management reporting and operational scorecards.", "Week 5 - Louisville", sourceUrls.louisville],
  ["BrightSpring Health Services", "Louisville, KY", "Healthcare Services", "Enterprise", 85, "High", "Email + LinkedIn + phone", "No", "Operations Analytics, Finance, Quality", "Distributed healthcare services create strong need for location, service, and quality reporting.", "Lead with operating scorecards and metric ownership.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Yum! Brands", "Louisville, KY", "Restaurant / Franchise", "Enterprise", 84, "High", "Email + LinkedIn; referral preferred", "No", "Franchise Analytics, Finance, Operations", "Global restaurant/franchise operations create huge reporting and KPI governance needs.", "Lead with franchise operating metrics and decision cadence.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Brown-Forman", "Louisville, KY", "Beverage / Consumer Goods", "Enterprise", 83, "High", "Email + LinkedIn", "No", "Sales Analytics, Supply Chain, Finance", "Consumer goods companies need commercial, supply, and brand reporting clarity.", "Lead with distributor/customer reporting and executive KPIs.", "Week 5 - Louisville", sourceUrls.louisville],
  ["GE Appliances", "Louisville, KY", "Manufacturing / Consumer Durables", "Enterprise", 83, "High", "Email + LinkedIn", "No", "Operations, Supply Chain, Finance", "Large manufacturing operations need production, quality, service, and supply chain reporting.", "Lead with operational intelligence and trusted KPIs.", "Week 5 - Louisville", sourceUrls.louisville],
  ["UPS Worldport / UPS Airlines", "Louisville, KY", "Logistics / Air Cargo", "Enterprise", 82, "Medium", "Email + LinkedIn; referral preferred", "No", "Operations Analytics, Hub Operations, Finance", "Air logistics operations are metrics-rich, though procurement access is harder.", "Lead with operational exception reporting and decision cadence.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Ford Kentucky Truck Plant", "Louisville, KY", "Automotive Manufacturing", "Enterprise site", 81, "Medium", "Email + LinkedIn; local supplier/referral path", "No", "Plant Operations, Finance, Continuous Improvement", "Large plant operations create strong production, quality, and downtime reporting needs.", "Lead with plant scorecards and operational escalation triggers.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Norton Healthcare", "Louisville, KY", "Healthcare", "Large regional", 80, "Medium", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Regional health system with major reporting and performance management needs.", "Lead with cross-site leadership reporting clarity.", "Week 5 - Louisville", sourceUrls.louisville],
  ["UofL Health", "Louisville, KY", "Healthcare", "Large regional", 79, "Medium", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Academic/regional healthcare system likely has departmental reporting complexity.", "Lead with KPI governance and decision-ready dashboards.", "Week 5 - Louisville", sourceUrls.louisville],
  ["ScionHealth", "Louisville, KY", "Healthcare Services", "Large private", 79, "Medium", "Email + LinkedIn", "No", "Operations Analytics, Finance, Quality", "Healthcare services operator with distributed-site reporting needs.", "Lead with operating signal and management reporting.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Baptist Health", "Louisville, KY", "Healthcare", "Large regional", 78, "Medium", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Regional health network with leadership and service-line reporting demands.", "Lead with trusted KPI definitions and operational cadence.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Texas Roadhouse", "Louisville, KY", "Restaurant", "Large public", 78, "Medium", "Email + LinkedIn", "No", "Store Ops Analytics, Finance, Supply Chain", "Restaurant chains rely on store, labor, guest, and margin reporting.", "Lead with store scorecards and weekly business review metrics.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Papa John's", "Louisville, KY", "Restaurant / Franchise", "Large public", 77, "Medium", "Email + LinkedIn", "No", "Franchise Ops, Finance, Customer Analytics", "Franchise restaurant systems need store, franchisee, digital, and customer reporting.", "Lead with franchise KPI governance and reporting cleanup.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Farm Credit Mid-America", "Louisville, KY", "Financial Services / Agriculture", "Large regional", 77, "Medium", "Email + LinkedIn", "No", "Credit Ops, Finance, Risk Analytics", "Financial cooperative with regional operations and risk/reporting needs.", "Lead with management reporting and metric traceability.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Churchill Downs Incorporated", "Louisville, KY", "Gaming / Entertainment", "Large public", 76, "Medium", "Email + LinkedIn", "No", "Operations Analytics, Finance, Customer Analytics", "Gaming and entertainment businesses need customer, venue, finance, and operations reporting.", "Lead with customer/operations dashboards and decision cadence.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Republic Bank", "Louisville, KY", "Banking", "Regional public", 76, "Medium", "Email + LinkedIn + phone", "No", "Risk Analytics, Finance, Commercial Ops", "Regional banks are better-sized targets for practical reporting governance.", "Lead with certified metrics and executive reporting cleanup.", "Week 5 - Louisville", sourceUrls.louisville],
  ["Eli Lilly and Company", "Indianapolis, IN", "Pharmaceuticals", "Enterprise", 89, "High", "Referral + email/LinkedIn; enterprise path", "No", "Manufacturing Analytics, Finance, Commercial Ops", "Pharma has complex operations, quality, commercial, and reporting governance needs.", "Lead with decision-ready operational reporting; expect long sales cycle.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Elevance Health", "Indianapolis, IN", "Health Insurance", "Enterprise", 87, "High", "Email + LinkedIn; referral preferred", "No", "Operations Analytics, Quality, Finance", "Managed healthcare has strong fit for metric governance and operational dashboards.", "Lead with trusted KPI ownership and management reporting.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Roche Diagnostics North America", "Indianapolis, IN", "Diagnostics / Life Sciences", "Enterprise site", 84, "High", "Email + LinkedIn; referral preferred", "No", "Operations Analytics, Commercial Ops, Finance", "Diagnostics operations require traceable, reliable reporting across product and commercial teams.", "Lead with operating signal and source reliability.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Cummins", "Columbus, IN", "Manufacturing / Engines", "Enterprise", 84, "High", "Email + LinkedIn; referral preferred", "No", "Operations, Supply Chain, Finance", "Large manufacturing operations create plant, product, quality, and supply-chain reporting needs.", "Lead with operational KPI governance and plant scorecards.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Corteva Agriscience", "Indianapolis, IN", "Agriculture / Chemicals", "Enterprise", 83, "High", "Email + LinkedIn", "No", "Commercial Analytics, Supply Chain, Finance", "Agriculture/chemicals have customer, product, supply, and seasonal reporting complexity.", "Lead with commercial and supply chain metric alignment.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["OneAmerica Financial", "Indianapolis, IN", "Insurance / Financial Services", "Large private", 81, "Medium", "Email + LinkedIn + phone", "No", "Finance, Insurance Ops, BI Governance", "Insurance/financial services fit dashboard trust and reporting governance well.", "Lead with metric ownership and executive reporting.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["IU Health", "Indianapolis, IN", "Healthcare", "Enterprise", 80, "Medium", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Large health system with cross-site operational reporting needs.", "Lead with trusted operating metrics and leadership cadence.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Community Health Network", "Indianapolis, IN", "Healthcare", "Large regional", 79, "Medium", "Warm intro + email", "No", "Operations Analytics, Finance, Strategy", "Regional healthcare network with service-line, access, and finance reporting needs.", "Lead with KPI governance and dashboard trust.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Republic Airways", "Indianapolis, IN", "Aviation", "Large private", 78, "Medium", "Email + LinkedIn", "No", "Operations, Finance, Workforce Planning", "Airline operations require crew, maintenance, service, and operational reporting.", "Lead with operating dashboards and exception reporting.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Allison Transmission", "Indianapolis, IN", "Manufacturing", "Large public", 78, "Medium", "Email + phone", "No", "Operations, Finance, Supply Chain", "Manufacturing and aftermarket operations need reliable KPI reporting.", "Lead with plant and supply-chain reporting cleanup.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Simon Property Group", "Indianapolis, IN", "Real Estate / Retail", "Enterprise", 77, "Medium", "Email + LinkedIn", "No", "Operations Analytics, Finance, Asset Management", "Property portfolios need tenant, traffic, revenue, and operating metrics.", "Lead with portfolio dashboards and executive scorecards.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["OPENLANE / KAR Global", "Carmel, IN", "Automotive Marketplace", "Large public", 77, "Medium", "Email + LinkedIn", "No", "Marketplace Ops, Finance, Customer Analytics", "Marketplace businesses require seller/buyer, operations, and finance reporting alignment.", "Lead with operational intelligence and KPI definitions.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Angi", "Indianapolis, IN", "Marketplace / Home Services", "Large public", 76, "Medium", "Email + LinkedIn", "No", "Revenue Ops, Marketplace Ops, Finance", "Marketplace operations rely on funnel, customer, provider, and profitability reporting.", "Lead with marketplace KPI governance and dashboards.", "Week 6 - Indianapolis", sourceUrls.indiana],
  ["Salesforce Indianapolis", "Indianapolis, IN", "Software / CRM", "Enterprise site", 75, "Low", "Partnership/referral; not direct services pitch", "No", "Partner Ecosystem, Customer Success, RevOps", "Mature analytics stack likely lowers need, but partnership/referral route could be valuable.", "Lead with implementation/support partnership, not basic BI.", "Week 6 - Opportunistic", sourceUrls.indiana],
  ["NCAA", "Indianapolis, IN", "Sports / Nonprofit", "Large institution", 73, "Low", "Warm intro + email", "No", "Operations, Finance, Data/Insights", "Institutional reporting needs exist, but fit and procurement path may be slower.", "Lead with executive reporting clarity and operational dashboards.", "Week 6 - Opportunistic", sourceUrls.indiana],
];

function accessibilityScore(row) {
  const [company, market, industry, scale, fit, confidence, method, doorstep] = row;
  let score = fit;
  const scaleText = scale.toLowerCase();
  const marketText = market.toLowerCase();
  const methodText = method.toLowerCase();
  const industryText = industry.toLowerCase();

  if (scaleText.includes("mid-market private")) score += 26;
  else if (scaleText.includes("mid-market")) score += 20;
  else if (scaleText.includes("large private")) score += 12;
  else if (scaleText.includes("large regional")) score += 10;
  else if (scaleText.includes("regional")) score += 6;
  else if (scaleText.includes("enterprise site")) score -= 28;
  else if (scaleText.includes("enterprise")) score -= 45;
  else if (scaleText.includes("large public")) score -= 8;

  if (
    marketText.includes("cincinnati") ||
    marketText.includes("covington") ||
    marketText.includes("newport") ||
    marketText.includes("erlanger") ||
    marketText.includes("florence") ||
    marketText.includes("edgewood") ||
    marketText.includes("fairfield") ||
    marketText.includes("mason") ||
    marketText.includes("hamilton") ||
    marketText.includes("sharonville")
  ) {
    score += 20;
  } else if (marketText.includes("dayton") || marketText.includes("miamisburg") || marketText.includes("moraine")) {
    score += 11;
  } else if (marketText.includes("columbus") || marketText.includes("dublin") || marketText.includes("westerville") || marketText.includes("new albany")) {
    score += 3;
  } else if (marketText.includes("louisville")) {
    score += 1;
  } else if (marketText.includes("indianapolis")) {
    score -= 4;
  }

  if (methodText.includes("phone")) score += 10;
  if (doorstep.toLowerCase().includes("yes")) score += 8;
  if (methodText.includes("warm intro") || methodText.includes("referral")) score -= 15;
  if (methodText.includes("procurement") || methodText.includes("compliance")) score -= 8;

  if (industryText.includes("manufacturing")) score += 5;
  if (industryText.includes("distribution") || industryText.includes("logistics")) score += 5;
  if (industryText.includes("restaurant") || industryText.includes("retail") || industryText.includes("field services") || industryText.includes("facilities")) score += 4;
  if (industryText.includes("healthcare")) score += scaleText.includes("enterprise") ? -2 : 3;
  if (industryText.includes("banking") || industryText.includes("insurance")) score -= scaleText.includes("enterprise") ? 10 : 0;

  return Math.max(1, score);
}

function outreachTier(score) {
  if (score >= 112) return "Start tomorrow";
  if (score >= 96) return "Week 1 follow-up";
  if (score >= 82) return "Near-term";
  return "Later / referral";
}

const selectedProspects = prospects
  .map((row) => ({ row, tomorrowScore: accessibilityScore(row) }))
  .sort((a, b) => b.tomorrowScore - a.tomorrowScore || b.row[4] - a.row[4] || a.row[0].localeCompare(b.row[0]))
  .slice(0, 100);

if (selectedProspects.length !== 100) {
  throw new Error(`Expected 100 prospects; found ${selectedProspects.length}`);
}

const wb = Workbook.create();
const summary = wb.worksheets.add("Summary");
const targets = wb.worksheets.add("Top 100 Targets");
const cadence = wb.worksheets.add("First Week Cadence");
const scripts = wb.worksheets.add("Outreach Scripts");
const sources = wb.worksheets.add("Sources & Assumptions");

for (const ws of [summary, targets, cadence, scripts, sources]) {
  ws.showGridLines = false;
}

const colors = {
  navy: "#0B1D4D",
  blue: "#1E70E8",
  gold: "#F5C542",
  cyan: "#7DD3FC",
  pale: "#EEF6FF",
  paleGold: "#FFF6D7",
  white: "#FFFFFF",
  gray: "#E5E7EB",
  text: "#172033",
  muted: "#475569",
};

function styleTitle(ws, range, title, subtitle) {
  ws.getRange(range).merge();
  ws.getRange(range).values = [[title]];
  ws.getRange(range).format = {
    fill: colors.navy,
    font: { bold: true, color: colors.white, size: 18 },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };
  if (subtitle) {
    const row = Number(range.match(/\d+/)[0]) + 1;
    ws.getRange(`A${row}:H${row}`).merge();
    ws.getRange(`A${row}:H${row}`).values = [[subtitle]];
    ws.getRange(`A${row}:H${row}`).format = {
      fill: colors.pale,
      font: { color: colors.text, size: 10 },
      wrapText: true,
    };
  }
}

styleTitle(
  summary,
  "A1:H2",
  "Parallax Data Lab - Best 100 Outreach Targets For Tomorrow",
  "Ranked for practical outreach beginning Friday, June 19, 2026. This version prioritizes reachable regional and mid-market buyers over prestige enterprise logos."
);

summary.getRange("A4:B10").values = [
  ["Total companies", selectedProspects.length],
  ["Best first channel", "Phone + concise email for local operators; email + LinkedIn for larger regional targets"],
  ["Doorstep guidance", "Only for local mid-market/public-office leave-behinds after prior touch; never for hospitals, banks, or enterprise campuses"],
  ["Primary buyer persona", "Ops, Finance, BI, Analytics, RevOps, Supply Chain"],
  ["Top offer to lead with", "Free Fit Check or Dashboard Trust Scorecard"],
  ["Best near-term market", "Cincinnati / Northern Kentucky first, Dayton second, Columbus/Louisville third"],
  ["Main caution", "Do not pitch as replacing analysts; pitch as extra senior capacity for reporting trust, KPI ownership, and operating clarity"],
];
summary.getRange("A4:A10").format = { fill: colors.pale, font: { bold: true, color: colors.text } };
summary.getRange("B4:B10").format = { fill: colors.white, font: { color: colors.text }, wrapText: true };
summary.getRange("A4:B10").format.borders = { preset: "all", style: "thin", color: colors.gray };
summary.getRange("D4:H11").values = [
  ["How to use this workbook", "", "", "", ""],
  ["1", "Start with ranks 1-25 on Friday. These are more reachable than the Fortune 500 names: call, send a concise email, then connect/view on LinkedIn.", "", "", ""],
  ["2", "Use the method column. Do not walk into regulated/enterprise targets without a scheduled reason.", "", "", ""],
  ["3", "Use the angle column to personalize the first line around likely reporting pain.", "", "", ""],
  ["4", "Track real contact names separately in your CRM once you identify the right owner.", "", "", ""],
  ["5", "For local mid-market targets, a short printed scorecard leave-behind can work after an email/call attempt.", "", "", ""],
  ["6", "If you only have 2 hours per day, work 12-15 local companies deeply rather than spraying 100 shallow emails.", "", "", ""],
  ["", "", "", "", ""],
];
summary.getRange("D4:H4").merge();
summary.getRange("D5:H10").merge(true);
summary.getRange("D4:H10").format = { fill: colors.paleGold, font: { color: colors.text }, wrapText: true };
summary.getRange("D4:H4").format.font = { bold: true, color: colors.text };
summary.getRange("D4:H10").format.borders = { preset: "all", style: "thin", color: colors.gray };

const headers = [
  "Rank",
  "Tomorrow Priority Score",
  "Outreach Tier",
  "Company",
  "HQ / Local Market",
  "Industry",
  "Company Scale",
  "Fit Score",
  "Research Confidence",
  "Recommended Method",
  "Doorstep?",
  "Likely Buyer Persona",
  "Why This Company Fits",
  "Suggested Opening Angle",
  "Suggested Cadence",
  "Source URL",
];
targets.getRange("A1:P1").values = [headers];
targets.getRange("A2:P101").values = selectedProspects.map((item, idx) => [idx + 1, item.tomorrowScore, outreachTier(item.tomorrowScore), ...item.row]);
targets.getRange("A1:P1").format = {
  fill: colors.navy,
  font: { bold: true, color: colors.white },
  wrapText: true,
  horizontalAlignment: "center",
};
targets.getRange("A2:P101").format = { font: { color: colors.text, size: 10 }, wrapText: true, verticalAlignment: "top" };
targets.getRange("A2:A101").format = { horizontalAlignment: "center" };
targets.getRange("B2:B101").format = { horizontalAlignment: "center" };
targets.getRange("H2:H101").format = { horizontalAlignment: "center" };
targets.getRange("A1:P101").format.borders = { preset: "all", style: "thin", color: colors.gray };
targets.tables.add("A1:P101", true, "ProspectTargets");
targets.freezePanes.freezeRows(1);

const colWidths = [50, 95, 120, 190, 150, 150, 115, 75, 100, 190, 85, 210, 310, 310, 130, 230];
colWidths.forEach((w, i) => {
  targets.getRangeByIndexes(0, i, 101, 1).format.columnWidthPx = w;
});
targets.getRange("A2:P101").format.rowHeightPx = 72;
targets.getRange("A1:P1").format.rowHeightPx = 42;

const cadenceRows = [
  ["Date", "Priority", "Action", "Target Count", "What to do", "Output"],
  ["2026-06-19", "Day 1", "Ranks 1-25", 25, "Work the most reachable local/mid-market companies first. Call, send a very short email, then LinkedIn-view/connect with one likely owner.", "25 first touches + 15 calls"],
  ["2026-06-20", "Day 2", "Ranks 26-45", 20, "Send next reachable batch. Prepare a one-page scorecard leave-behind only for companies where the workbook says doorstep may fit.", "20 first touches + 8 calls"],
  ["2026-06-22", "Day 3", "Ranks 1-45 follow-up", 45, "Call all no-reply local operators. Send a second email that says you are not replacing analysts; you help clean up metric ownership and reporting trust.", "30 calls + 20 follow-ups"],
  ["2026-06-23", "Day 4", "Ranks 46-65", 20, "Work Dayton and nearby operators. Personalize around manufacturing, healthcare services, logistics, restaurant/store ops, or distribution reporting.", "20 first touches"],
  ["2026-06-24", "Day 5", "Ranks 66-85", 20, "Work Columbus/Louisville companies where buyer access is still plausible. Use referral asks for bigger names.", "20 first touches"],
  ["2026-06-25", "Day 6", "Ranks 86-100 + live opportunities", 15, "Work remaining targets only after re-touching engaged local prospects. Do not let big-company names distract from replies.", "15 first touches + booked meetings"],
  ["2026-06-26", "Day 7", "Pipeline cleanup", 100, "Update CRM/contact status, promote replies to meeting follow-up, and demote any company requiring enterprise procurement or no clear buyer.", "Clean week 2 working list"],
];
styleTitle(cadence, "A1:F2", "First Week Outreach Cadence", "The goal is not to contact all 100 blindly. The goal is to create 100 researched doors, then work the highest-reachability 25-45 with discipline.");
cadence.getRange("A4:F11").values = cadenceRows;
cadence.getRange("A4:F4").format = { fill: colors.navy, font: { bold: true, color: colors.white }, horizontalAlignment: "center" };
cadence.getRange("A5:F11").format = { fill: colors.white, font: { color: colors.text }, wrapText: true, verticalAlignment: "top" };
cadence.getRange("A4:F11").format.borders = { preset: "all", style: "thin", color: colors.gray };
cadence.tables.add("A4:F11", true, "CadencePlan");
[95, 85, 150, 90, 420, 190].forEach((w, i) => cadence.getRangeByIndexes(0, i, 12, 1).format.columnWidthPx = w);
cadence.getRange("A5:F11").format.rowHeightPx = 58;

styleTitle(scripts, "A1:H2", "Outreach Scripts & Channel Rules", "Use these as starting points. Personalize the first sentence with the company-specific angle in the target table.");
scripts.getRange("A4:H15").values = [
  ["Asset", "Use When", "Script / Rule", "", "", "", "", ""],
  ["Email subject", "Default first touch", "Quick dashboard trust question", "", "", "", "", ""],
  ["Email body", "Most companies", "Hi [Name] - I run Parallax Data Lab in Cincinnati. I am not reaching out to replace your analysts. I help teams that already have reports clean up KPI definitions, ownership, reporting logic, and the operating cadence around the numbers. I noticed [company-specific context]. If reporting trust or recurring manual reporting is creating drag, would a 15-minute fit check be worth it next week?", "", "", "", "", ""],
  ["Phone opener", "Local/private/mid-market targets", "Hi, this is Jonah with Parallax Data Lab. I help operations and finance teams when dashboards exist but leaders still debate the numbers or rely on manual reporting. Who owns KPI reporting or analytics operations for your team?", "", "", "", "", ""],
  ["LinkedIn note", "After email", "I help Cincinnati/regional teams turn dashboard sprawl and metric debates into trusted operating scorecards. Reaching out because your team looks like the kind where reporting clarity can move decisions faster.", "", "", "", "", ""],
  ["Doorstep rule", "Only for suitable local targets", "Do not walk into hospitals, banks, enterprise campuses, or regulated facilities. For local family-owned or mid-market public-office targets, bring a one-page Dashboard Trust Scorecard and say you are leaving it for the person who owns reporting/operations.", "", "", "", "", ""],
  ["Best CTA", "First touch", "Ask for a 15-minute Fit Check, not a paid project. Keep the ask small.", "", "", "", "", ""],
  ["Proof asset", "Follow-up", "Send the Dashboard Trust Scorecard or a short article like 'Why Nobody Trusts Your Dashboard' when the company appears to have dashboard trust pain.", "", "", "", "", ""],
  ["Bad pitch to avoid", "Always", "Do not open with 'I build dashboards' or 'I can do analytics for you.' That sounds like you are replacing an analyst. Open with extra senior capacity, metric ownership, reporting trust, and operating clarity.", "", "", "", "", ""],
  ["Best call blocks", "Starting 2026-06-19", "8:15-9:15 AM for operations leaders; 11:00-11:45 AM for finance/analytics follow-up; 3:30-4:45 PM for second call block.", "", "", "", "", ""],
  ["Follow-up 1", "2 business days after first touch", "Worth a quick look, or is dashboard/reporting ownership handled cleanly already? If it is not a priority, I can close the loop.", "", "", "", "", ""],
  ["Follow-up 2", "5-7 business days after first touch", "Sharing this scorecard because it is a simple way to identify whether the issue is metric trust, ownership, source reliability, decision cadence, or operational signal. Happy to compare notes if useful.", "", "", "", "", ""],
];
scripts.getRange("A4:H4").format = { fill: colors.navy, font: { bold: true, color: colors.white } };
scripts.getRange("A5:H15").format = { font: { color: colors.text }, wrapText: true, verticalAlignment: "top" };
scripts.getRange("A4:H15").format.borders = { preset: "all", style: "thin", color: colors.gray };
scripts.getRange("C5:H15").merge(true);
[130, 190, 760, 10, 10, 10, 10, 10].forEach((w, i) => scripts.getRangeByIndexes(0, i, 16, 1).format.columnWidthPx = w);
scripts.getRange("A5:H15").format.rowHeightPx = 68;

styleTitle(sources, "A1:H2", "Sources & Assumptions", "This is a prospecting list, not a verified contact database. Confirm buyer names, current role titles, procurement rules, and recent company priorities before sending.");
sources.getRange("A4:D16").values = [
  ["Source / Basis", "URL", "Used For", "Notes"],
  ["Greater Cincinnati company list", sourceUrls.greaterCincinnati, "Cincinnati HQs and significant local employers", "Used for regional company universe and local market relevance."],
  ["Cincinnati employer context", sourceUrls.cincinnatiEmployers, "Largest regional employers", "Used to prioritize healthcare, Kroger, and major institutional anchors."],
  ["Axios 2025 Ohio Fortune 500 summary", sourceUrls.ohioFortune, "Ohio Fortune-scale companies", "Used to validate Ohio large-company priority and revenue scale context."],
  ["Dayton economy and employers", sourceUrls.dayton, "Dayton prospect universe", "Used for Dayton health, tech, utility, and manufacturing targets."],
  ["Dayton metro employer list", sourceUrls.daytonMetro, "Dayton regional employer cross-check", "Used for LexisNexis and major Dayton-area employer context."],
  ["Central Ohio employer list", sourceUrls.centralOhio, "Columbus prospect universe", "Used for Columbus-area employers and locally headquartered anchors."],
  ["Louisville major employers", sourceUrls.louisville, "Louisville prospect universe", "Used for healthcare, logistics, manufacturing, and restaurant/franchise targets."],
  ["Indiana business context", sourceUrls.indiana, "Indianapolis/Indiana prospect universe", "Used for Indiana Fortune/company context and industries."],
  ["Fortune 500 overview", sourceUrls.fortune500, "Enterprise scale context", "Used for broad current Fortune 500 context where relevant."],
  ["Ranking assumption", "Internal Parallax fit model", "Fit Score", "Weighted toward reporting complexity, local/regional accessibility, likely dashboard trust pain, and realistic buyer access."],
  ["Channel assumption", "Internal Parallax outreach model", "Recommended Method", "Default is email + LinkedIn + phone. Doorstep is only for local mid-market leave-behind after prior touch."],
  ["Compliance note", "N/A", "Outreach safety", "Respect no-solicitation policies, privacy rules, building access rules, and regulated-industry procurement boundaries."],
];
sources.getRange("A4:D4").format = { fill: colors.navy, font: { bold: true, color: colors.white } };
sources.getRange("A5:D16").format = { font: { color: colors.text }, wrapText: true, verticalAlignment: "top" };
sources.getRange("A4:D16").format.borders = { preset: "all", style: "thin", color: colors.gray };
[220, 430, 260, 420].forEach((w, i) => sources.getRangeByIndexes(0, i, 17, 1).format.columnWidthPx = w);
sources.getRange("A5:D16").format.rowHeightPx = 54;

// Compact summary formatting.
[130, 360, 24, 110, 180, 180, 180, 180].forEach((w, i) => summary.getRangeByIndexes(0, i, 12, 1).format.columnWidthPx = w);
summary.getRange("A1:H2").format.rowHeightPx = 34;
summary.getRange("A4:B10").format.rowHeightPx = 36;

// Validation-friendly formatting and final render/export.
await fs.mkdir(outputDir, { recursive: true });
for (const sheetName of ["Summary", "Top 100 Targets", "First Week Cadence", "Outreach Scripts", "Sources & Assumptions"]) {
  await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
}

const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outputPath);

console.log(outputPath);
